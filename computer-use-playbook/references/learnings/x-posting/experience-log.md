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
