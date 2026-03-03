# X Posting Experience Log

## Entry Format
- Date:
- Task:
- Context:
- Failure signal:
- Root cause:
- Fix that worked:
- Reusable rule:

- Date: 2026-02-18
- Task: Publish X post from browser automation
- Context: Composer had dual textboxes (`tweetTextarea_0`) and dual buttons (`tweetButton`, `tweetButtonInline`) on `x.com/compose/post`.
- Failure signal: Programmatic text insertion appeared in editor but published posts were image-only or malformed text.
- Root cause: X composer did not treat script-based insertion as trusted user text input for final payload; media upload still succeeded.
- Fix that worked: Use human-in-the-loop for text entry; automation may safely handle media attach and final post click after manual typing confirmation.
- Reusable rule: For X posting, require manual typing/paste confirmation before clicking `Post`; verify live post text and media immediately on profile.

- Date: 2026-02-18
- Task: Create reusable Expost experience checklist
- Context: Multiple failed publish variants occurred (malformed hashtags and image-only outcomes) despite visible composer text.
- Failure signal: Composer UI looked correct before publish, but live post payload did not match intended content.
- Root cause: Compose surface ambiguity plus non-trusted scripted text behavior in X.
- Fix that worked: Encode strict pre-publish and post-publish gates; require human-confirmed text input when needed.
- Reusable rule: For Expost, shipping quality comes from verification gates, not from compose UI appearance alone.

- Date: 2026-02-25
- Task: Publish user-authored engineering viewpoint to X
- Context: User expected full-length argument and precise wording, but draft was compressed and reframed.
- Failure signal: Published copy was much shorter than user intent and tone drifted toward marketing language.
- Root cause: Agent applied unnecessary short-form assumption (legacy 280-char bias) and skipped explicit user draft approval gate.
- Fix that worked: Add mandatory pre-publish user approval, preserve user voice, and remove default truncation for Premium-capable accounts.
- Reusable rule: For X posting, never shorten unless explicitly required; full draft approval is a hard gate before publish.

- Date: 2026-02-25
- Task: Publish approved long-form X post with two article links and GitHub workflow link
- Context: Needed full-length Premium-capable post and exact approved text.
- Failure signal: Direct DOM insertion kept post buttons disabled (`tweetButtonInline`/`tweetButton`) despite visible text.
- Root cause: Composer treated script-inserted text as non-trusted input on this surface.
- Fix that worked: Use `https://x.com/compose/post?text=...` prefill for trusted text, confirm visible long draft in active editor, click enabled `tweetButtonInline`, then verify newest status URL and rendered content.
- Reusable rule: For long X posts, prefer compose URL prefill over raw script insertion; trust publish only after live profile/status verification.

- Date: 2026-02-26
- Task: Repost full-length X draft after user rejected compressed version
- Context: User explicitly required LinkedIn-length wording on X Premium and removed the prior short post.
- Failure signal: Prior run used a shorter draft than requested.
- Root cause: Agent applied the wrong drafting constraint for this user/account expectation.
- Fix that worked: Prefilled the exact long draft via `https://x.com/compose/post?text=...`, verified editor length and enabled `tweetButtonInline`, published, then verified live status URL and opening sentence.
- Reusable rule: When user asks for same-as-LinkedIn content on X, publish the full approved draft verbatim unless the user asks to shorten.

- Date: 2026-02-26
- Task: Prepare X draft for workflow-state-machine infographic share (no publish)
- Context: User requested post preparation and planned to attach image manually before posting.
- Failure signal: None.
- Root cause: N/A.
- Fix that worked: Navigated to `https://x.com/compose/post?text=...` with URL-prefilled draft, verified non-empty active editor and enabled post button, then captured screenshot evidence.
- Reusable rule: For draft-only X runs, prefer compose URL prefill and stop at verified-ready state (do not click `Post`).

- Date: 2026-02-26
- Task: Publish approved workflow-update post on X
- Context: User approved final draft and requested direct publish.
- Failure signal: None.
- Root cause: N/A.
- Fix that worked: Used compose URL prefill with approved text, clicked enabled `tweetButton`, then verified newest profile post text and captured status URL.
- Reusable rule: For X publish, confirm newest profile post contains the exact opening line and capture the status URL immediately after posting.
