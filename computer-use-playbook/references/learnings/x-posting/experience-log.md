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

- Date: 2026-02-19
- Task: Publish Linux support announcement on X
- Context: `x.com/compose/post` rendered two compose surfaces and `tweetButton` in dialog looked enabled even when editor text was empty.
- Failure signal: Button state alone was inconsistent with expected text-required gating.
- Root cause: Multiple concurrent compose surfaces (`inDialog` vs inline) made naive selector checks unreliable.
- Fix that worked: Scope strictly to dialog composer (`[role="dialog"] [data-testid="tweetTextarea_0"]` + `[data-testid="tweetButton"]`), require `textLen > 0`, then verify on profile and status URL.
- Reusable rule: For Expost, gate publish on dialog-scoped editor content, not button-enabled state, and always verify newest `/status/` text payload.

- Date: 2026-02-19
- Task: Publish AutoByteus Server TS open-source announcement on X
- Context: Needed text-only launch post with repo URL and branch positioning.
- Failure signal: On `x.com/compose/post`, scripted text appeared in dialog editor but `tweetButton` remained disabled.
- Root cause: X treated DOM-inserted content as non-trusted input for publish gating in that compose surface.
- Fix that worked: Fallback to `x.com/intent/post?text=...` so X prefilled the draft server-side, confirm dialog `tweetButton` enabled, publish, then verify via captured status URL (`/status/2024435831205683266`) and syndication API payload.
- Reusable rule: If `/compose/post` keeps `tweetButton` disabled after scripted insert, switch to `intent/post` prefill and validate final text from the status payload, especially if browser automation session becomes unstable post-click.

- Date: 2026-02-20
- Task: Publish distributed-agents architecture post on X with infographic
- Context: Needed reliable text payload plus one infographic media attachment.
- Failure signal: N/A (preventive path selected due known compose instability).
- Root cause: Prior runs showed scripted text insertion can serialize incorrectly in `/compose/post`.
- Fix that worked: Use `https://x.com/intent/post?text=...` prefill, attach media through visible `input[type=file]` using in-browser canvas-generated PNG, publish, and verify via newest `/status/` URL.
- Reusable rule: For X, prioritize `intent/post` for text reliability and pair it with file-input media attach plus status-URL verification.
