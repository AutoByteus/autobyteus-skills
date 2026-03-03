# LinkedIn Posting Experience Log

## Entry Format
- Date:
- Task:
- Context:
- Failure signal:
- Root cause:
- Fix that worked:
- Reusable rule:

- Date: 2026-02-18
- Task: Publish AutoByteus skills post on LinkedIn with infographic image
- Context: User requested a LinkedIn post describing 4 skills and attaching infographic media.
- Failure signal: Feed selectors were noisy; hidden video modal (`role=dialog`) caused false positives; direct `fetch` from GitHub raw URL failed in-page.
- Root cause: LinkedIn UI has multiple modal surfaces and strict browser/network constraints for media source fetch.
- Fix that worked: Use stable route `https://www.linkedin.com/preload/sharebox/`, upload media via file input with local base64 payload, then proceed `Next` -> editor -> `Post`.
- Reusable rule: For LinkedIn posting, prefer `/preload/sharebox/` compose flow and verify success via toast + opened post URL + rendered post text/media.

- Date: 2026-02-18
- Task: Replace low-resolution image in published LinkedIn post
- Context: User reviewed the post and flagged image quality as unacceptable.
- Failure signal: Edit flow exposed alt-text edits only; no reliable media replacement path on the existing published post.
- Root cause: LinkedIn post edit does not provide dependable image-replacement controls for this post type.
- Fix that worked: Recreate post via `https://www.linkedin.com/preload/sharebox/`, attach a generated `1600x900` image through `#media-editor-file-selector__file-input`, then publish and verify the new share URL.
- Reusable rule: If media quality is wrong after publish, do not iterate in edit mode; delete/repost and verify image artifacts include HD variants (for example `1600x900`).

- Date: 2026-02-18
- Task: Add follow-up attribution comment under published LinkedIn post
- Context: User requested a comment saying the post was fully driven by Codex.
- Failure signal: Global button search did not find a generic `Post` action for comments.
- Root cause: LinkedIn uses a comment-form-specific submit button (`Comment`) instead of the composer `Post` button.
- Fix that worked: Fill the comment editor in `form.comments-comment-box__form` and click `button.comments-comment-box__submit-button--cr`.
- Reusable rule: For LinkedIn comments, scope actions to the comment form and submit via the form-specific `Comment` button, then verify text appears in the comments list.

- Date: 2026-02-18
- Task: Publish Phone AV Bridge launch post
- Context: Needed to post from logged-in LinkedIn compose modal and verify publication.
- Failure signal: Draft insertion appeared to run but editor stayed effectively blank and `Post` was disabled.
- Root cause: LinkedIn Quill compose modal rejected plain DOM insertion path.
- Fix that worked: Use `document.execCommand('insertText', ...)` into `.ql-editor[role="textbox"]`, then verify `Post` enabled before clicking.
- Reusable rule: In LinkedIn compose, do not trust script success alone; require checkpoint sequence: editor text visible -> `Post` enabled -> live post URL contains opening sentence.

- Date: 2026-02-18
- Task: Add comment under existing LinkedIn post
- Context: Needed a follow-up comment on a freshly published post.
- Failure signal: Submit button absent in form until text entry.
- Root cause: LinkedIn comment form lazily exposes submit control after editor content changes.
- Fix that worked: Fill `.ql-editor` first, then locate/click `comments-comment-box__submit-button--cr`.
- Reusable rule: For LinkedIn comments, do not search submit globally before typing; type first, then submit within `comments-comment-box__form`.

- Date: 2026-02-18
- Task: Post humorous Codex-attribution comment under existing LinkedIn post
- Context: Needed emoji-heavy follow-up clarifying previous comment was by Codex.
- Failure signal: First combined insert+submit script reported no submit button.
- Root cause: UI delay before comment submit control becomes queryable after input.
- Fix that worked: Use two-phase action: insert draft, then re-query and click `comments-comment-box__submit-button--cr`.
- Reusable rule: For LinkedIn comments, avoid one-shot insert+submit scripts; separate into staged actions with a post-input re-query.

- Date: 2026-02-25
- Task: Publish long-form text post with external references and workflow link
- Context: User-approved draft required exact wording plus source links and GitHub workflow reference.
- Failure signal: First insertion path showed long text, then editor collapsed to partial content with many blank lines.
- Root cause: LinkedIn Quill composer intermittently dropped content with the initial insertion method.
- Fix that worked: Use `https://www.linkedin.com/preload/sharebox/`, insert via `editor.textContent` + `InputEvent`, verify full expected length, verify `Post` enabled, publish, then verify live post text on share URL.
- Reusable rule: For long LinkedIn posts, never trust first insertion result; require length check + start/end text check before clicking `Post`.

- Date: 2026-02-26
- Task: Publish Codex voice-update post after feed-surface automation failure
- Context: Feed page interactions did not reliably open the composer using synthetic clicks.
- Failure signal: On `https://www.linkedin.com/feed/`, `Start a post` clicks were ignored and no editor/post controls became available.
- Root cause: Feed-surface event path was unreliable for scripted interaction in this run.
- Fix that worked: Switched to `https://www.linkedin.com/preload/sharebox/`, inserted into `.ql-editor[role="textbox"]` using Quill-compatible text insertion, verified `Post` enabled, published, then used `View post` toast link and verified live post text.
- Reusable rule: If feed composer fails to open, immediately pivot to `/preload/sharebox/` and complete publish via Quill checks.

- Date: 2026-02-26
- Task: Prepare LinkedIn draft for workflow-state-machine infographic share (no publish)
- Context: User requested efficient cross-platform post preparation and planned to attach image manually.
- Failure signal: None.
- Root cause: N/A.
- Fix that worked: Opened `https://www.linkedin.com/preload/sharebox/`, inserted long-form draft into `.ql-editor[role=\"textbox\"]` with `InputEvent`, verified expected text length and `Post` enabled, then captured screenshot evidence.
- Reusable rule: For draft-only LinkedIn runs, stop before publish and hand off with verified composer text + screenshot evidence.

- Date: 2026-02-26
- Task: Publish approved workflow-update post on LinkedIn
- Context: User approved final draft text and requested immediate publish.
- Failure signal: Screenshot capture retried due intermittent timeout on LinkedIn rendered page.
- Root cause: LinkedIn page screenshot call intermittently timed out while waiting for font/render stability.
- Fix that worked: Publish from `/preload/sharebox/` via `button.share-actions__primary-action`, verify success via toast + share URL (`/feed/update/...`), then rely on existing captured evidence screenshot.
- Reusable rule: For LinkedIn publish, treat toast + canonical post URL as primary success criteria; screenshot is supporting evidence and may require retry.
