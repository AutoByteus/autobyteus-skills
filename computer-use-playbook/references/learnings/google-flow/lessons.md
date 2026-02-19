# Google Flow Lessons (From Real Run)

Use this playbook when creating a single video in Google Flow (`labs.google/fx/tools/flow`) with first/last frames.

## Working Pattern
1. Use one UI action at a time.
2. After each action, take a screenshot and verify state before the next action.
3. Do not queue multiple clicks/scripts without visual confirmation.

## Reliable Flow Sequence (Frames -> One Video)
1. Open mode dropdown and select `Video aus Frames`.
2. Verify `x1` (one output) and target model in settings.
3. Attach first and last frame images.
4. Enter prompt using an input path that triggers app state updates.
5. Confirm submit arrow/create is enabled.
6. Click create once.
7. Poll progress by screenshot until video card is complete.

## Important UI Quirks
- Visual prompt text can appear while Flow still treats prompt as empty.
- Symptom: toast says `Geben Sie vor dem Senden einen Prompt ein` even though text is visible.
- Fix: trigger true input events (or genuine typing behavior) so internal state updates.
- Switching modes/views can reset composer fields/frames; re-verify after each switch.

## Prompt Entry Guidance
- Prefer real typing semantics or framework-compatible value setting plus `input`/`change`.
- After prompt entry, verify submit control is enabled before clicking.

## Verification Checks Before Submit
- Mode shows `Video aus Frames`.
- Two frame thumbnails are present in composer.
- Prompt is present and accepted (no empty-prompt toast on submit).
- Output count is `x1`.

## Progress/Completion Checks
- While rendering, progress percentage may appear on the preview tile.
- Final success signal: playable video tile/card appears with controls (play/download/etc.).

## Troubleshooting
- If create stays disabled:
  - Re-enter prompt with true typing/input events.
  - Re-check frames are still attached (mode switches can drop them).
  - Re-open settings and verify output/model did not change.

## Continuous Update Rule
After every Google Flow run, append a concise entry to the workspace log (for example `FLOW_VIDEO_AUTOMATION_EXPERIENCE.md`) using:

- `Date`:
- `Context`:
- `Failure signal`:
- `Root cause`:
- `Fix that worked`:
- `Reusable rule`:

Keep entries short, concrete, and deduplicated.
