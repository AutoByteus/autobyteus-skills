# Investigation Notes Example

## Investigation Status

- Current Status: `Current`
- Scope Triage: `Medium`
- Triage Rationale: touches API behavior, worker allocation logic, and room-state coordination
- Investigation Goal: understand why `Start Recording All Occupied Rooms` sometimes reuses the wrong worker allocation path
- Primary Questions To Resolve:
  - where does the request enter the runtime spine?
  - which owner actually decides worker allocation?
  - is the incorrect behavior caused by stale helper logic or by requirement ambiguity?

## Source Log

| Date | Source Type (`Code`/`Doc`/`Web`/`Command`/`Trace`/`Log`/`Data`/`Other`) | Exact Source / Query / Command | Why Consulted | Relevant Findings | Follow-Up Needed |
| --- | --- | --- | --- | --- | --- |
| 2026-03-25 | Command | `rg -n "Start Recording All Occupied Rooms|worker allocation" src` | find entrypoints and ownership | found UI entrypoint, service path, and one stale fallback helper | No |
| 2026-03-25 | Code | `src/zoom/recording/start-recording-all-occupied-rooms.ts` | inspect request entrypoint | entrypoint delegates to `RoomRecordingCoordinator` | No |
| 2026-03-25 | Code | `src/zoom/recording/room-recording-coordinator.ts` | inspect owner for room allocation | coordinator still consults legacy `allocateWorkerLegacy` branch | Yes |
| 2026-03-25 | Code | `src/zoom/workers/allocate-worker-legacy.ts` | verify whether fallback is still used | legacy branch duplicates 80 percent of the new allocator logic | Yes |
| 2026-03-25 | Web | `https://developers.zoom.example/recording-api` | confirm partner-system room recording limits | host can only schedule one recording worker per occupied room set | No |
| 2026-03-25 | Trace | local repro with occupied multi-room session | verify actual failure path | wrong worker selection occurs only when two rooms are occupied at once | No |

## Current Behavior / Codebase Findings

### Entrypoints And Boundaries

- Primary entrypoints:
  - `src/zoom/recording/start-recording-all-occupied-rooms.ts`
- Execution boundaries:
  - UI action -> recording coordinator -> worker allocator -> Zoom adapter
- Owning subsystems / capability areas:
  - `zoom/recording`
  - `zoom/workers`
- Optional modules involved:
  - none required
- Folder / file placement observations:
  - `allocate-worker-legacy.ts` sits under the correct subsystem but should likely be removed instead of retained

### Relevant Files / Symbols

| Path | Symbol / Area | Current Responsibility | Finding / Observation | Ownership / Placement Implication |
| --- | --- | --- | --- | --- |
| `src/zoom/recording/start-recording-all-occupied-rooms.ts` | `startRecordingAllOccupiedRooms` | request entrypoint | thin entrypoint, placement looks correct | keep under recording entrypoints |
| `src/zoom/recording/room-recording-coordinator.ts` | `RoomRecordingCoordinator` | orchestrates room recording flow | current owner still branches into legacy worker allocation | likely keep owner, remove fallback branch |
| `src/zoom/workers/allocate-worker.ts` | `allocateWorker` | primary worker allocation | new path already covers most normal cases | shared core should stay here |
| `src/zoom/workers/allocate-worker-legacy.ts` | `allocateWorkerLegacy` | old fallback allocator | near-duplicate logic with extra stale assumptions | candidate for removal, not extension |

### Runtime / Probe Findings

| Date | Method (`Repro`/`Trace`/`Probe`/`Script`/`Test`) | Exact Command / Method | Observation | Implication |
| --- | --- | --- | --- | --- |
| 2026-03-25 | Trace | local occupied-room repro | failure appears when the second room enters allocation path | worker allocation decision is the likely defect center |
| 2026-03-25 | Probe | ad hoc logging around coordinator allocator call | legacy path still selected for multi-room case | design and implementation should remove dual-path behavior |

## External / Internet Findings

| Source | Fact / Constraint | Why It Matters | Confidence / Freshness |
| --- | --- | --- | --- |
| `https://developers.zoom.example/recording-api` | one recording worker per occupied room set | allocator must avoid duplicate worker assignment for same occupied set | High / 2026-03-25 |

## Constraints

- partner API constrains worker assignment shape
- current code still carries a dual-path allocator split

## Unknowns / Open Questions

- Unknown: whether any hidden consumer still calls `allocateWorkerLegacy` directly
- Why it matters: safe removal depends on this
- Planned follow-up: run repo-wide search and runtime trace for direct legacy calls

## Implications

### Requirements Implications

- requirements should explicitly say multi-room occupied recording must use one consistent allocation policy

### Design Implications

- design should remove the legacy allocator path instead of extending it
- coordinator should depend on one canonical allocation owner

### Implementation / Placement Implications

- implementation should delete stale legacy worker allocation code in scope
- Stage 8 should verify no duplicate allocator logic remains

## Re-Entry Additions

### 2026-03-26 Re-Entry Update

- Trigger: Stage 7 API/E2E validation found the allocator still diverges under retry conditions
- New evidence: retry path enters `allocateWorkerLegacy` through one stale adapter wrapper
- Updated implications: design and implementation must remove that wrapper and keep one canonical allocator path
