# Style Registry

Use this file as the single source of truth for available writing profiles.

## Active Profiles

| profile_id | display_name | status | languages | file | example_file | primary use | source basis |
|---|---|---|---|---|---|---|---|
| ryan | Ryan | ready | Chinese, English | references/profiles/ryan.md | references/examples/ryan-examples.md | Technical strategy essays, software engineering analysis, architecture-first arguments | User-provided WeChat and Medium samples in this skill setup |
| normy | Normy | bootstrapping | Chinese, English (pending corpus) | references/profiles/normy.md | references/examples/normy-examples.md | Personal-style article drafting after corpus intake | No fixed corpus yet |

## Load Order

1. Read this registry.
2. Resolve the requested author to `profile_id` (lowercase hyphen-case).
3. Read the selected profile file from the `file` column.
4. If `example_file` is not empty, read it for few-shot guidance.
5. Read platform rules from `platform-output-rules.md`.
6. Draft only after profile + platform constraints are loaded.

## Add New Author Profile

When a requested author is not listed:

1. Create `references/profiles/<profile-id>.md` from `references/profiles/profile-template.md`.
2. Create `references/examples/<profile-id>-examples.md` from `references/examples/example-template.md`.
3. Link that path in the `example_file` column.
4. Append a new row in the Active Profiles table with:
- `status=bootstrapping`
- best-known languages
- new profile file path
- new or placeholder example file path
- source basis as `Pending corpus`
5. Ask for 2-5 sample articles before final drafting.

## Profile Update Protocol

When the user provides sample articles for any profile:

1. Tag sample metadata: author, language, platform, date, topic, link/source.
2. Extract style signals:
- Thesis style and confidence level.
- Paragraph rhythm and sentence length.
- Section structure and transition patterns.
- Typical verbs, connectors, and framing phrases.
- Preferred evidence types (examples, case studies, lists, claims).
3. Update only the relevant profile file.
4. Keep profile differences explicit; do not merge voices.
5. Switch status from `bootstrapping` to `ready` only after stable traits are observed across at least 3 samples.
