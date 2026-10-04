#!/usr/bin/env python3
"""Validate the catalogue locally; optionally check live links without changing files."""

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen

LINK = re.compile(r'\[([^\]\n]+)\]\(([^\s)]+)\)')
ENTRY = re.compile(r'^- \[([^\]\n]+)\]\((https?://[^\s)]+)\)')
TAGS = ('iOS', 'macOS', 'tvOS', 'watchOS', 'visionOS', 'SwiftUI', 'UIKit', 'AppKit', 'Archived')
TAG_SUFFIX = re.compile(r'(?:\s+`(?:' + '|'.join(TAGS) + r')`)+$')


def anchor(heading):
    return re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')


def identity(url):
    parts = urlsplit(url)
    path = parts.path.rstrip('/')
    if parts.hostname in ('github.com', 'gist.github.com'):
        path = path.removesuffix('.git').lower()
    return (parts.hostname, path, parts.query, parts.fragment)


def validate_local(path):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    headings = [anchor(m[1]) for line in lines if (m := re.match(r'^#{1,3} (.+)$', line))]
    errors, seen, names = [], {}, []
    section = ''

    def check_order():
        if names != sorted(names, key=str.casefold):
            errors.append(f'{section}: entries are not alphabetically sorted')

    for number, line in enumerate(lines, 1):
        if line.startswith('#'):
            check_order()
            names = []
            section = line.lstrip('# ')
        if line.startswith('- [') and '](http' in line:
            match = ENTRY.match(line)
            if not match:
                errors.append(f'{number}: malformed resource entry')
                continue
            name, url = match.groups()
            names.append(name)
            key = identity(url)
            if key in seen:
                errors.append(f'{number}: duplicate resource (first at {seen[key]})')
            seen[key] = number
            if line.count('`') % 2:
                errors.append(f'{number}: unclosed code span')
            suffix = TAG_SUFFIX.search(line)
            if suffix:
                tags = re.findall(r'`([^`]+)`', suffix[0])
                expected = [tag for tag in TAGS if tag in tags]
                if tags != expected:
                    errors.append(f'{number}: duplicate or unordered tags')
        if re.search(r'\([^)]*\)\[https?://', line):
            errors.append(f'{number}: reversed Markdown link')
        for _, target in LINK.findall(line):
            if target.startswith('#') and unquote(target[1:]) not in headings:
                errors.append(f'{number}: missing heading {target}')
            elif not urlsplit(target).scheme and not target.startswith('#'):
                if not (path.parent / unquote(target.split('#')[0])).is_file():
                    errors.append(f'{number}: missing local file {target}')
    check_order()
    errors.extend(f'duplicate heading: {h}' for h, count in Counter(headings).items() if count > 1)
    return errors, sorted({url for _, url in LINK.findall(text) if url.startswith(('http://', 'https://'))})


def gh_api(endpoint, query=None):
    command = ['gh', 'api', endpoint]
    if query:
        command += ['-f', 'query=' + query]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)
        payload = json.loads(result.stdout)
    except (OSError, subprocess.TimeoutExpired, ValueError) as error:
        raise RuntimeError(f'GitHub CLI unavailable or invalid response: {error}') from error
    # GraphQL may return useful partial data with NOT_FOUND errors.
    if result.returncode and not isinstance(payload, dict):
        raise RuntimeError('GitHub CLI request failed')
    return payload


def rest_result(endpoint):
    data = gh_api(endpoint)
    if isinstance(data, dict) and 'message' in data:
        status = str(data.get('status', ''))
        return {'status': 'missing' if status in ('404', '410') else 'review',
                'detail': f'GitHub API {status}: {data["message"]}'}
    return {'status': 'ok', 'detail': 'GitHub REST API'}


def github_repositories(repositories):
    results = {}
    keys = sorted(repositories)
    for start in range(0, len(keys), 40):
        batch = keys[start:start + 40]
        fields = []
        for index, key in enumerate(batch):
            owner, name = key.split('/')
            fields.append(f'r{index}:repository(owner:{json.dumps(owner)},name:{json.dumps(name)})'
                          '{url isArchived nameWithOwner}')
        data = gh_api('graphql', 'query {' + ' '.join(fields) + '}')
        for index, key in enumerate(batch):
            alias = f'r{index}'
            repo = (data.get('data') or {}).get(alias)
            if repo:
                results[key] = {'status': 'ok', 'canonical_url': repo['url'],
                                'archived': repo['isArchived']}
            else:
                errors = [e for e in data.get('errors', []) if e.get('path') == [alias]]
                if errors and all(e.get('type') == 'NOT_FOUND' for e in errors):
                    # Confirm an absent repository using a second API before reporting it missing.
                    results[key] = rest_result('repos/' + key)
                else:
                    results[key] = {'status': 'review', 'detail': 'GitHub query failed; absence unconfirmed'}
        print(f'GitHub repositories: {min(start + 40, len(keys))}/{len(keys)}', file=sys.stderr)
    return results


def http_result(url):
    missing_responses = 0
    for attempt in range(2):
        try:
            request = Request(url, headers={'User-Agent': 'Mozilla/5.0 (resource-link-validator)'})
            with urlopen(request, timeout=20) as response:
                body = response.read(65536).decode('utf-8', errors='replace').lower()
                blocked = response.status == 202 or '<title>just a moment' in body or 'cf-chl-' in body
                return {'status': 'review' if blocked else 'ok', 'http_status': response.status,
                        'canonical_url': response.url,
                        'detail': 'Possible bot challenge' if blocked else 'HTTP GET; content relevance requires review'}
        except HTTPError as error:
            missing_responses += error.code in (404, 410)
            result = {'status': 'missing' if error.code in (404, 410) else 'review',
                      'http_status': error.code, 'detail': f'HTTP {error.code}'}
        except (URLError, TimeoutError, OSError) as error:
            result = {'status': 'review', 'detail': str(error)}
        if attempt == 0:
            time.sleep(1)
    if result['status'] == 'missing' and missing_responses < 2:
        result['status'] = 'review'
        result['detail'] += '; absence not confirmed on both attempts'
    return result


def check_online(urls):
    repositories = set()
    for url in urls:
        parsed = urlsplit(url)
        parts = parsed.path.strip('/').split('/')
        if parsed.hostname == 'github.com' and len(parts) >= 2:
            repositories.add('/'.join(parts[:2]).removesuffix('.git').lower())
    metadata = github_repositories(repositories)
    results = []
    for url in urls:
        parsed = urlsplit(url)
        parts = parsed.path.strip('/').split('/')
        if parsed.hostname == 'github.com' and len(parts) >= 2:
            key = '/'.join(parts[:2]).removesuffix('.git').lower()
            result = dict(metadata[key])
            if len(parts) > 2 and result['status'] == 'ok':
                if parts[2] in ('tree', 'blob') and len(parts) >= 4:
                    ref = quote(unquote(parts[3]), safe='')
                    tail = '/'.join(parts[4:])
                    endpoint = f'repos/{key}/contents/{tail}?ref={ref}'
                    result = rest_result(endpoint)
                else:
                    result = {'status': 'review', 'detail': 'Unsupported GitHub subpage; inspect manually'}
        elif parsed.hostname == 'github.com':
            result = rest_result('users/' + parts[0])
        elif parsed.hostname == 'gist.github.com' and len(parts) >= 2:
            result = rest_result('gists/' + parts[1])
        else:
            result = http_result(url)
        results.append({'url': url, **result})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--readme', type=Path, default=Path(__file__).with_name('README.md'))
    parser.add_argument('--online', action='store_true', help='check live URLs using authenticated gh and HTTP GET')
    parser.add_argument('--report', type=Path, help='write JSON evidence (requires --online)')
    args = parser.parse_args()
    if args.report and not args.online:
        parser.error('--report requires --online')
    errors, urls = validate_local(args.readme)
    for error in errors:
        print('ERROR: ' + error, file=sys.stderr)
    print(f'Local validation: {len(errors)} error(s), {len(urls)} unique external URLs.')
    if errors:
        return 1
    if not args.online:
        return 0
    try:
        results = check_online(urls)
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 2
    if args.report:
        args.report.write_text(json.dumps({'checked_at': datetime.now(timezone.utc).isoformat(),
                                          'results': results}, indent=2) + '\n', encoding='utf-8')
    for result in results:
        if result['status'] != 'ok':
            print(f'{result["status"].upper()}: {result["url"]} — {result.get("detail", "")}')
    counts = Counter(result['status'] for result in results)
    print('Live validation: ' + ', '.join(f'{count} {status}' for status, count in sorted(counts.items())))
    # An inconclusive run must never look like a clean audit.
    return 1 if counts['missing'] else 2 if counts['review'] else 0


if __name__ == '__main__':
    sys.exit(main())
