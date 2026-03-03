# Google Flow Experience Log

Use this file to capture run-specific learnings for Google Flow automation.

## Entry Template
Use this exact structure for each new run:

```md
## [GF-YYYY-MM-DD-XX] Short task title
- Date:
- Workflow:
- Context:
- Failure signal:
- Root cause:
- Fix that worked:
- Reusable rule:
- Tags:
```

## Logging Rules
1. Keep entries short, concrete, and directly reusable.
2. Prefer updating an existing rule over adding a duplicate rule.
3. Each entry should contain one clear failure-to-fix mapping.
4. Include `Workflow` and `Tags` so entries are filterable.

## Run Index
| ID | Date | Workflow | Task | Key reusable rule |
| --- | --- | --- | --- | --- |
| GF-2026-02-17-01 | 2026-02-17 | Video aus Frames | Create one video and ensure host download | Verify create-enabled state and use direct URL download when browser download does not land locally. |
| GF-2026-02-17-02 | 2026-02-17 | Text/Frames composer | Unblock disabled create control | If prompt is visible but submit is disabled, re-enter with true typing behavior. |
| GF-2026-02-20-01 | 2026-02-20 | Video aus Text | Generate one creative Veo 3.1 video | Re-verify mode/model/output (`Video*`, `Veo 3.1*`, `x1`) right before submit. |
| GF-2026-02-20-02 | 2026-02-20 | Download | Save generated video to local machine | If local file is missing after click download, use `video.currentSrc` + `curl -L`. |
| GF-2026-02-20-03 | 2026-02-20 | Video aus Frames | Generate controlled first/last-frame Veo 3.1 video | INVALIDATED: frame-picker selection was assumed reliable without upload confirmation. |
| GF-2026-02-20-04 | 2026-02-20 | Video aus Frames (Correction) | Correct frame attachment workflow | Generate images, download locally, then attach via `upload Hochladen` for each frame slot. |
| GF-2026-02-20-05 | 2026-02-20 | Video aus Frames (Validated rerun) | Create and download controlled geek-animal video | Clear blocking dialogs, enforce no-`add` frame-slot gate, and use direct URL download fallback in Docker runtime. |
| GF-2026-02-20-06 | 2026-02-20 | Video aus Frames (Strict checkpoint run) | Generate with explicit first/last download+upload checkpoints | Validate both frame files on host, bind both slots, and verify endpoint adherence by frame similarity check. |

## Entries

## [GF-2026-02-17-01] Create one video and ensure host download
- Date: 2026-02-17
- Workflow: `Video aus Frames`, output `x1`
- Context: Needed a reliable end-to-end path from compose to local playback.
- Failure signal: Prompt looked filled but Flow treated it as empty; create stayed blocked at times; browser download click did not produce host file.
- Root cause: UI input state was not always updated by naive value insertion; browser-managed download path can stay in runtime container.
- Fix that worked: Execute one action at a time with screenshot verification; re-enter prompt using true typing/input semantics; when host file is missing, extract `video.currentSrc` and run host-side `curl -L`.
- Reusable rule: Trust state transitions over visible text, verify create enabled before submit, and fall back to direct URL download when needed.
- Tags: `prompt-state`, `download`, `frames`, `x1`

## [GF-2026-02-17-02] Unblock disabled create control
- Date: 2026-02-17
- Workflow: Text/frames composer
- Context: Composer showed prompt text but submit arrow remained disabled.
- Failure signal: No generation started and warning implied empty prompt despite visible text.
- Root cause: Programmatic assignment did not trigger the exact event path Flow expects.
- Fix that worked: Focus textarea, clear/select, then insert text with true typing semantics (for example `document.execCommand('insertText', ...)` loop), then re-check enabled state.
- Reusable rule: If visible prompt and disabled create conflict, re-enter with real typing behavior first.
- Tags: `prompt-state`, `submit-disabled`

## [GF-2026-02-20-01] Generate one creative Veo 3.1 video
- Date: 2026-02-20
- Workflow: `Video aus Text`
- Context: New project opened in German locale; composer defaulted to image mode and settings defaulted to 2 outputs.
- Failure signal: Initial composer state was `Bild erstellen` with `x2`, which would waste credits and miss required model/output constraints.
- Root cause: Flow preserved defaults instead of desired video + single output settings.
- Fix that worked: Switch mode to `Video aus Text`, open `Einstellungen`, set `Ausgaben pro Prompt` to `1`, confirm `Modell Veo 3.1 - Fast`, then submit once after prompt input events.
- Reusable rule: On every run, verify mode/model/output explicitly right before submit.
- Tags: `veo-3.1`, `x1`, `defaults`, `text-to-video`

## [GF-2026-02-20-02] Download generated video locally
- Date: 2026-02-20
- Workflow: Download from completed video tile
- Context: Completed Veo 3.1 video had `Herunterladen` control.
- Failure signal: Clicking in-browser download did not create a new file in `/Users/normy/Downloads`.
- Root cause: Browser-managed download path did not land in host filesystem for this runtime session.
- Fix that worked: Read `video.currentSrc` from page and save with host-side `curl -L` to a concrete local path.
- Reusable rule: Always verify local file creation after Flow download click; if missing, use direct URL + `curl`.
- Tags: `download`, `host-filesystem`, `fallback`

## [GF-2026-02-20-03] Controlled first/last-frame video run
- Date: 2026-02-20
- Workflow: `Video aus Frames` with `Veo 3.1 - Fast`, output `x1`
- Context: Generated two storyboard images (start/end intent), then switched to frame mode and attached assets through the frame picker.
- Failure signal: Frame picker tiles were visually unlabeled (`Ein Medien-Asset...`), so first/last assignment was ambiguous by text alone.
- Root cause: Picker UI exposes thumbnails without prompt labels in selectable tile text.
- Fix that worked: Partial only; slot fill state was observed but source asset identity was not reliably guaranteed.
- Reusable rule: INVALIDATED by user verification. Do not treat this entry as valid source-of-truth for frame identity.
- Tags: `frames`, `picker-ui`, `veo-3.1`, `x1`, `invalidated`

## [GF-2026-02-20-04] Postmortem correction for frame identity
- Date: 2026-02-20
- Workflow: `Video aus Frames` with local upload
- Context: User confirmed produced video did not match intended generated geek-animal frames.
- Failure signal: Final video content mismatch indicated wrong frame source assignment.
- Root cause: Assumed generated in-app images could be reliably selected directly from picker list; actual reliable path requires explicit local upload (`Hochladen`).
- Fix that worked: Correct process is: generate frame images -> download both to local disk -> in each frame slot click `add` -> choose `upload Hochladen` -> select exact local first/last files.
- Reusable rule: For controlled frame-to-video runs, use local upload as mandatory default; never assume picker tiles correspond to just-generated frames.
- Tags: `frames`, `upload`, `postmortem`, `correction`, `source-of-truth`

## [GF-2026-02-20-05] Validated rerun with frame workflow and host download
- Date: 2026-02-20
- Workflow: `Video aus Frames` with `Veo 3.1 - Fast`, output `x1`
- Context: Continued run in Docker-backed browser runtime (`autobyteus/chrome-vnc`) and completed end-to-end generation.
- Failure signal: Hidden dialogs (`Ausblenden`, prior crop flow) and prompt-event mismatch temporarily blocked reliable submission state; browser click download did not create host file.
- Root cause: Overlay state obscured controls during frame operations; Flow textarea required stronger typing semantics; runtime download path remained container-side.
- Fix that worked: Clear overlays first, verify frame gate state (no remaining `add` in composer), re-enter prompt with real typing semantics (`execCommand`/input events), submit once, and save final clip with `video.currentSrc` + host-side `curl -L`.
- Reusable rule: In Docker/VNC runs, enforce a strict pre-submit gate (model `Veo 3.1`, `x1`, no frame `add`) and assume direct URL download fallback.
- Tags: `frames`, `veo-3.1`, `x1`, `docker-runtime`, `download-fallback`, `dialog-guard`

## [GF-2026-02-20-06] Strict checkpoint run with endpoint verification
- Date: 2026-02-20
- Workflow: `Video aus Frames` with `Veo 3.1 - Fast`, output `x1`
- Context: Executed requested checkpoint sequence: create first frame -> download -> host verify; create last frame -> download -> host verify; then upload each into frame slots and generate.
- Failure signal: After second upload crop-save, one `add` slot still remained until UI state settled and slot binding completed.
- Root cause: Slot commit can lag after upload/crop flow; immediate check can report transient incomplete state.
- Fix that worked: Re-check slot chips and `add` count after each upload; proceed only when both chips (`Erster Frame`, `Letzter Frame`) are visible and no `add` remains.
- Reusable rule: Use strict gates at each phase: host file existence gate for downloads, slot-complete gate for uploads, then submission.
- Tags: `frames`, `upload`, `download`, `checkpoint`, `slot-commit`, `verification`
