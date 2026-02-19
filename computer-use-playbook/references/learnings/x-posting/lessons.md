# X Posting Lessons

## Scope
- Applies to Expost/X posting from `https://x.com/compose/post`.

## Core Rules
- Use DOM-first and verify login state before compose actions.
- If login/2FA/CAPTCHA appears, pause for human intervention and resume only after verification.
- Treat text entry as human-in-the-loop when X rejects scripted input behavior.
- Never publish when text is expected but composer text is empty.

## Pre-Publish Checklist
- Confirm active composer elements are the primary pair: editor + `tweetButton`.
- Confirm final post text is present in the active editor and matches intended copy.
- Confirm image attachment state matches intent.
- For text-only posts, no media preview is required.
- For image posts, at least one attached media preview must be visible.
- Confirm `Post` button is enabled.

## Publish Verification Checklist
- Open profile immediately after click.
- Confirm newest status URL.
- Confirm rendered text content is correct.
- Confirm media count is correct.
- Capture one evidence screenshot.

## Recovery Playbook
- If malformed or image-only post is published by mistake, open the status URL first.
- Delete the bad post.
- Re-compose from a clean composer.
- Require explicit text confirmation before repost.

## Practical Notes From Run
- X can render multiple compose surfaces (`tweetTextarea_0`, `tweetButton`, `tweetButtonInline`) at once.
- Script-visible text can still fail to serialize into final published tweet payload.
- Safest flow: automate navigation/media/verification, require human-confirmed text before final publish.
