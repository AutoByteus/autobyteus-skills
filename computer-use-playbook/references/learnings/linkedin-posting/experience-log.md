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

- Date: 2026-02-19
- Task: Publish AutoByteus Server TS open-source announcement on LinkedIn
- Context: Needed a long-form technical launch post with branch/capability details and immediate publication.
- Failure signal: No blocking failure; compose route had multiple similarly named controls.
- Root cause: LinkedIn UI includes non-compose controls containing "Post" labels, which can mislead naive selectors.
- Fix that worked: Use `https://www.linkedin.com/preload/sharebox/`, insert text into `.ql-editor[role="textbox"]` with `document.execCommand('insertText', ...)`, click the exact `Post` button, then verify via success toast and live share URL.
- Reusable rule: For LinkedIn launches, pin to `/preload/sharebox/`, scope to editor + exact composer `Post`, and require two proofs: success toast and live post URL containing the opening sentence.

- Date: 2026-02-20
- Task: Publish distributed-agents architecture post on LinkedIn with infographic
- Context: Posted long-form technical copy plus one infographic via `https://www.linkedin.com/preload/sharebox/`.
- Failure signal: Attempted in-page `fetch('http://127.0.0.1:8765/...')` for generated local image failed.
- Root cause: LinkedIn compose runs on HTTPS; mixed-content/local fetch path was blocked.
- Fix that worked: Generate infographic directly in-browser canvas, attach via `#media-editor-file-selector__file-input`, then `Next` -> `Post`.
- Reusable rule: For LinkedIn HTTPS composer, avoid local HTTP media fetch; use in-browser canvas-to-file upload when deterministic local file bridging is blocked.
