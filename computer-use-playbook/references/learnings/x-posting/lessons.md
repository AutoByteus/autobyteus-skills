# X Posting Lessons

## Scope
- Default compose route is `https://x.com/intent/post?text=...` for reliable server-side text prefill.
- Use `https://x.com/compose/post` only as fallback when intent flow is unavailable.

## Core Rules
- Use DOM-first and verify login state before compose actions.
- If login/2FA/CAPTCHA appears, pause for human intervention and resume only after verification.
- Scope composer checks to the active dialog (`[role="dialog"]`) to avoid surface ambiguity.
- Never publish when expected text is empty in the dialog editor.

## Pre-Publish Checklist
- Confirm active composer elements are dialog-scoped: editor + `[data-testid="tweetButton"]`.
- Confirm final post text is present in dialog editor and matches intended copy.
- Confirm image attachment state matches intent.
- For text-only posts, no media preview is required.
- For image posts, at least one attached media preview must be visible.
- Confirm dialog `Post` button is enabled (`disabled === false`).

## Publish Verification Checklist
- Open profile immediately after click.
- Confirm newest status URL.
- Confirm rendered text content is correct.
- Confirm media count is correct.
- Capture one evidence screenshot.

## Recovery Playbook
- If malformed or image-only post is published by mistake, open the status URL first.
- Delete the bad post.
- Re-compose from a clean composer using `intent/post` prefill.
- Re-verify dialog text and media before repost.

## Practical Notes From Run
- X can render multiple compose surfaces (`tweetTextarea_0`, `tweetButton`, `tweetButtonInline`) at once.
- Script-visible text can fail to serialize in `/compose/post`.
- Prefer `intent/post` to avoid non-trusted scripted text failures.
- For media, attach through visible `input[type="file"]`; if local fetch is blocked, generate image in-browser (canvas -> File) and upload via DataTransfer.
