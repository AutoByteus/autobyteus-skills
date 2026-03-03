# Xiaohongshu Posting Lessons

## Scope
- Applies to Xiaohongshu creator posting flows.

## Operating Mode
- Run in lesson-lock mode: execute the primary workflow first and do not improvise before documented fallbacks.

## Mandatory Primary Workflow
1. Verify creator login state before compose actions.
2. Use browser DOM-first workflow for page navigation and compose actions.
3. Draft final Chinese copy first, then paste once to avoid partial/garbled input.
4. Before publishing, verify title/body/media visibility in composer.
5. Click publish once.
6. Open the live note page and verify final rendered text/media.

## Allowed Fallbacks (Only If Primary Step Fails)
- If creator login is missing (`redirectReason=401` or equivalent), switch to human-in-the-loop and resume only after login verification.
- If a compose input path is unstable, re-focus the active editor and repeat single-step input with state checks.

## Continuous Update Rule
- If a new reliable fallback is discovered, update this `lessons.md` and log the run in `experience-log.md`.
