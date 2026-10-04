import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

import validation


class LocalValidationTests(unittest.TestCase):
    def check(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'README.md'
            path.write_text(text)
            return validation.validate_local(path)[0]

    def test_valid_catalogue_with_internal_anchor_and_inline_code(self):
        text = ('# Resources\n\n[Contents](#views)\n\n## Views\n\n'
                '- [Alpha](https://github.com/example/Alpha) - Uses `UIView`. `iOS` `UIKit`\n'
                '- [Beta](https://github.com/example/Beta) - Description. `Archived`\n')
        self.assertEqual(self.check(text), [])

    def test_case_and_scheme_differences_do_not_hide_duplicate_github_urls(self):
        errors = self.check('# List\n- [Alpha](http://github.com/Example/Project/)\n'
                            '- [Beta](https://github.com/example/project)\n')
        self.assertTrue(any('duplicate resource' in error for error in errors))

    def test_broken_navigation_and_missing_files_fail(self):
        errors = self.check('# List\n[Broken](#absent)\n[Instructions](missing.md)\n')
        self.assertTrue(any('missing heading' in error for error in errors))
        self.assertTrue(any('missing local file' in error for error in errors))

    def test_sorting_and_unclosed_code_are_reported(self):
        errors = self.check('# List\n- [Z](https://example.com/z) - `UIView\n'
                            '- [A](https://example.com/a)\n')
        self.assertTrue(any('alphabetically' in error for error in errors))
        self.assertTrue(any('unclosed' in error for error in errors))

    def test_duplicate_tags_and_reversed_links_are_reported(self):
        errors = self.check('# List\n- [A](https://example.com/a) - (Tutorial)[https://example.com/b] `iOS` `iOS`\n')
        self.assertTrue(any('tags' in error for error in errors))
        self.assertTrue(any('reversed' in error for error in errors))


class OnlineValidationTests(unittest.TestCase):
    @patch('validation.gh_api')
    def test_partial_graphql_response_preserves_success_and_confirms_absence(self, api):
        api.side_effect = [
            {'data': {'r0': {'url': 'https://github.com/new/available',
                             'nameWithOwner': 'new/available', 'isArchived': True}, 'r1': None},
             'errors': [{'type': 'NOT_FOUND', 'path': ['r1']}]},
            {'message': 'Not Found', 'status': '404'},
        ]
        with contextlib.redirect_stderr(io.StringIO()):
            result = validation.github_repositories({'old/available', 'old/missing'})
        self.assertEqual(result['old/available']['status'], 'ok')
        self.assertTrue(result['old/available']['archived'])
        self.assertEqual(result['old/missing']['status'], 'missing')
        self.assertEqual(api.call_args.args, ('repos/old/missing',))

    @patch('validation.gh_api', return_value={'message': 'Bad credentials', 'status': '401'})
    def test_authentication_failure_is_not_a_missing_repository(self, api):
        with contextlib.redirect_stderr(io.StringIO()):
            result = validation.github_repositories({'owner/project'})
        self.assertEqual(result['owner/project']['status'], 'review')

    @patch('validation.time.sleep')
    @patch('validation.urlopen')
    def test_http_404_requires_repeated_absence(self, open_url, sleep):
        open_url.side_effect = [HTTPError('https://example.com', 404, 'Missing', {}, None)] * 2
        result = validation.http_result('https://example.com')
        self.assertEqual(result['status'], 'missing')
        self.assertEqual(open_url.call_count, 2)

    @patch('validation.time.sleep')
    @patch('validation.urlopen')
    def test_tls_failure_followed_by_404_is_inconclusive(self, open_url, sleep):
        open_url.side_effect = [URLError('certificate error'), HTTPError('https://example.com', 404, 'Missing', {}, None)]
        self.assertEqual(validation.http_result('https://example.com')['status'], 'review')

    @patch('validation.time.sleep')
    @patch('validation.urlopen')
    def test_forbidden_rate_limits_and_server_errors_are_not_deletions(self, open_url, sleep):
        for code in (403, 429, 500):
            with self.subTest(code=code):
                open_url.side_effect = [HTTPError('https://example.com', code, 'Blocked', {}, None)] * 2
                self.assertEqual(validation.http_result('https://example.com')['status'], 'review')

    @patch('validation.rest_result', return_value={'status': 'missing'})
    @patch('validation.github_repositories', return_value={'owner/project': {'status': 'ok'}})
    def test_existing_repository_does_not_hide_missing_subdirectory(self, repositories, rest):
        result = validation.check_online(['https://github.com/owner/project/tree/main/examples'])
        self.assertEqual(result[0]['status'], 'missing')
        rest.assert_called_once_with('repos/owner/project/contents/examples?ref=main')

    @patch('validation.check_online', return_value=[{'url': 'https://example.com', 'status': 'review'}])
    @patch('validation.validate_local', return_value=([], ['https://example.com']))
    def test_inconclusive_cli_run_exits_nonzero_and_writes_evidence(self, local, online):
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / 'report.json'
            with patch('sys.argv', ['validation.py', '--online', '--report', str(report)]), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(validation.main(), 2)
            self.assertIn('"status": "review"', report.read_text())


if __name__ == '__main__':
    unittest.main()
