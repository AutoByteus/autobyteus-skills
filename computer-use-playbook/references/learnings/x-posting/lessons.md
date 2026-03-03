# X Posting Lessons

## Scope
- Applies to X/Twitter/Expost posting via `https://x.com/compose/post`.

## Operating Mode
- Run in lesson-lock mode: execute the primary workflow first and do not improvise before documented fallbacks.

## Core Rules
- Verify login state first; if login/2FA/CAPTCHA appears, pause for human intervention.
- Never publish until the user explicitly approves the exact final draft for this run.
- Preserve user voice and structure; do not reframe into marketing copy unless requested.
- Never publish when expected text is empty in the active editor.
- Do not auto-shorten by default; only compress when the user requests it or platform capability requires it.

## Mandatory Primary Workflow
1. Build `https://x.com/compose/post?text=...` using URL-encoded approved draft.
2. Navigate to the compose URL and wait for the composer to settle.
3. Verify the active editor is non-empty and contains the intended opening line.
4. Verify publish control is enabled on the same compose surface:
   - prefer enabled `tweetButtonInline` when present,
   - otherwise use enabled `tweetButton`.
5. Verify media state matches intent:
   - text-only: no media required,
   - media post: at least one media preview visible.
6. Click publish once.
7. Open profile immediately and capture the newest status URL.
8. Open the status URL and verify rendered opening line and media count.
9. Capture one evidence screenshot.

## Allowed Fallbacks (Only If Primary Step Fails)
- If compose URL prefill fails due platform behavior, use active-editor insertion with real input semantics (`execCommand('insertText', ...)` or equivalent `input`/`change` event flow), then re-run all pre-publish gates.
- If no publish control is enabled, re-check active composer surface and focus state before any new insertion attempt.
- If UI is blocked by auth/security gates, switch to human-in-the-loop; do not bypass.

## Recovery
- If a malformed or image-only post is published, open status URL first, delete the bad post, then repost from a clean composer using the primary workflow.
