# Google Flow Lessons (From Real Run)

Use this playbook for creating one video in Google Flow (`labs.google/fx/tools/flow`) with either:
- text prompt only (`Video aus Text`)
- first/last frames plus prompt (`Video aus Frames`)

## Working Pattern
1. Use one UI action at a time.
2. Verify state after each action before moving on.
3. Avoid batching clicks or scripts when UI is changing.

## Fast Preflight (Always)
1. Set generation mode intentionally (`Video aus Text` or `Video aus Frames`).
2. Open `Einstellungen`.
3. Set `Modell` to `Veo 3.1 - Fast` (or latest `Veo 3.1` option available).
4. Set `Ausgaben pro Prompt` to `1` (`x1`).
5. Re-check mode/model/output once more before submit.

## Path A: Text -> One Video
1. Select `Video aus Text`.
2. Complete preflight (`Veo 3.1`, `x1`).
3. Enter prompt with real input events.
4. Confirm create button (`Erstellen`) is enabled.
5. Click create once.
6. Poll until a playable video tile with controls appears.

## Path B: First + Last Frames -> One Video
1. In image mode, generate first-frame image (`x1`) and last-frame image (`x1`).
2. Download both generated images to local disk and verify files exist.
3. Select `Video aus Frames`.
4. Complete preflight (`Veo 3.1`, `x1`).
5. For each frame slot (`add`):
6. Click `add` -> choose `upload Hochladen` -> select the local image file (first slot = first frame, second slot = last frame).
7. Verify both slots are populated (no remaining `add` controls).
8. Enter prompt with real input events.
9. Confirm create button (`Erstellen`) is enabled.
10. Click create once.
11. Poll until a playable video tile with controls appears.

## Frame Slot Gate (Required Before Submit)
1. Do not submit if any frame `add` control is still visible in the composer.
2. Required state: both `Erster Frame` and `Letzter Frame` chips are present and no `add` buttons remain.
3. If dialog overlays are visible (`Ausblenden`, `Zuschneiden und speichern`), clear them first and then re-check slot state.

## Upload Commit Rule
1. `Hochladen` + crop save can still leave slot binding incomplete momentarily.
2. After each upload, re-check the composer slot state (`Erster Frame` / `Letzter Frame`).
3. If one slot still shows `add`, reopen that slot and repeat upload/crop once.

## Prompt Reliability Rule
- Visual text alone is not enough; Flow may still treat prompt as empty.
- Preferred method: real typing semantics or value set with `input` and `change` events.
- If submit is disabled despite visible text, re-enter prompt with true typing behavior.

## Completion and Download Rule
1. Completion signal: video tile/card is present with playback/download controls.
2. Try Flow's download button first.
3. Verify local file exists on host (`/Users/normy/Downloads` or target path).
4. If file is missing locally, read `video.currentSrc` and download via host-side `curl -L`.
5. In Docker/VNC browser runtimes, expect browser download to fail host-save frequently; treat URL + `curl -L` as standard fallback.

## Common Failure Checks
1. Mode switched/reset unexpectedly after other actions.
2. Output reverted from `x1` to default (`x2`).
3. Model changed away from `Veo 3.1`.
4. Frames dropped after mode/settings changes.
5. Assuming generated images are always selectable from the in-app picker instead of uploading from local files.

## Correction Note (2026-02-20)
1. Previous assumption was wrong: generated images are not reliably selectable directly as frame assets in the picker list.
2. Correct reliable method: generate images -> download locally -> attach via `upload Hochladen` for each frame slot.
3. Treat this upload workflow as required default for controlled first/last-frame runs unless Flow behavior is re-verified in a future run.

## Continuous Update Rule
After every Google Flow run, append a concise entry to `references/learnings/google-flow/experience-log.md` using:
- `Date`:
- `Task`:
- `Context`:
- `Failure signal`:
- `Root cause`:
- `Fix that worked`:
- `Reusable rule`:

Keep entries short, concrete, and deduplicated.
