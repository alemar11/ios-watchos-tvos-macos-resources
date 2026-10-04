# Contributing

Keep the catalogue focused on Apple-platform development and related Swift tooling.

## Resource entries

- Add each resource once, under the most specific functional topic. Put SwiftUI controls next to other controls of the same type.
- Sort entries alphabetically by displayed name within each topic, ignoring case.
- Prefer the original project's canonical HTTPS URL. Preserve a subdirectory or branch when the resource is specifically about that example.
- Write a short factual description. Keep tutorials and supporting articles inside the relevant entry, with descriptive link text.
- Add only supported platform or framework tags, in this order: `iOS`, `macOS`, `tvOS`, `watchOS`, `visionOS`, `SwiftUI`, `UIKit`, `AppKit`, `Archived`.
- Use the project's documentation or author-supplied topics as evidence for tags. Do not infer every supported platform from the language or repository name.
- Keep accessible archived repositories and mark them `Archived`. An old last commit alone is not a reason to remove an entry.
- When adding or renaming a heading, update the Contents table in `README.md`.

Entry format:

```markdown
- [Project name](https://example.com/project) - Short description. `iOS` `SwiftUI`
```

## Validation

Python 3.10 or later is sufficient; no Python packages are required.

```sh
python3 validation.py
python3 -m unittest discover -s tests
```

The local check validates alphabetical ordering, duplicate resource URLs, heading anchors, local file links, code spans and tag ordering. It does not make network requests.

For live availability checks, install GitHub CLI and authenticate your own account with `gh auth login` first, then run:

```sh
python3 validation.py --online --report /tmp/resource-links.json
```

GitHub repositories are checked in batches through authenticated `gh api graphql`. Missing repositories are checked again through the REST API; linked files, directories, branches, profiles and gists are checked individually. Other sites use HTTP GET with a timeout and a second attempt after an error.

Exit codes:

- `0`: requested checks passed.
- `1`: local catalogue errors or missing URLs.
- `2`: inconclusive availability checks, authentication/API problems or network failures.

The report records canonical repository URLs and archive status for maintainers to review; the checker never edits the catalogue. A successful HTTP response only establishes reachability. Inspect redirects and page content to catch parked domains, unrelated replacements, login pages and bot challenges.

Confirm missing sources before removing them. Update moved links when the original project or article is still available. Keep `403`, `429`, timeouts, TLS errors and server failures pending review; these do not prove that a resource has disappeared. Record removals, replacements and unresolved checks in `docs/link-audit.md` with the audit date.
