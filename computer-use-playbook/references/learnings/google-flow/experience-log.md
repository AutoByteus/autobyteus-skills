# Google Flow Experience Log

Use this file to append run-specific learnings for Google Flow automation.

## Entry Format
- Date:
- Task:
- Context:
- Failure signal:
- Root cause:
- Fix that worked:
- Reusable rule:

## Rules
- Keep entries short and concrete.
- Prefer updating existing rules instead of duplicating near-identical notes.
- Every entry should improve the next run's speed or reliability.

- Date: 2026-02-17
- Task: Create one Google Flow video from first/last frames and make it available on host
- Context: `Video aus Frames` flow with `x1` output; needed a reliable end-to-end path from compose to local playback.
- Failure signal: Prompt looked filled but Flow treated it as empty; create stayed blocked at times; browser download click did not produce host file.
- Root cause: UI internal input state was not always updated by naive value insertion; browser-managed download path can stay in runtime container.
- Fix that worked: Execute one action at a time with screenshot verification; re-enter prompt using true typing/input semantics; when host file is missing, extract `<video>.currentSrc` and run host-side `curl -L` to save the mp4.
- Reusable rule: In Flow, trust state transitions over visual text; always verify create enabled before submit and use direct URL download when browser download is not on host.

- Date: 2026-02-17
- Task: Unblock disabled create control in text/frame composer
- Context: Composer showed prompt text but submit arrow remained disabled.
- Failure signal: No generation started and warning implied empty prompt despite visible text.
- Root cause: Programmatic assignment did not trigger the exact event path Flow expects.
- Fix that worked: Focus the textarea, clear/select, then insert text with true typing semantics (for example `document.execCommand('insertText', ...)` loop), then re-check enabled state.
- Reusable rule: If visible prompt and disabled create conflict, re-enter with real typing behavior first, then verify enabled control before any submit click.
