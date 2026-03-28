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

| Date | Source Type (`Code`/`Doc`/`Spec`/`Web`/`Repo`/`Issue`/`Command`/`Trace`/`Log`/`Data`/`Setup`/`Other`) | Exact Source / Query / Command | Why Consulted | Relevant Findings | Follow-Up Needed |
| --- | --- | --- | --- | --- | --- |
| 2026-03-25 | Command | `rg -n "Start Recording All Occupied Rooms|worker allocation" src` | find entrypoints and ownership | found UI entrypoint, service path, and one stale fallback helper | No |
| 2026-03-25 | Code | `src/zoom/recording/start-recording-all-occupied-rooms.ts` | inspect request entrypoint | entrypoint delegates to `RoomRecordingCoordinator` | No |
| 2026-03-25 | Code | `src/zoom/recording/room-recording-coordinator.ts` | inspect owner for room allocation | coordinator still consults legacy `allocateWorkerLegacy` branch | Yes |
| 2026-03-25 | Code | `src/zoom/workers/allocate-worker-legacy.ts` | verify whether fallback is still used | legacy branch duplicates 80 percent of the new allocator logic | Yes |
| 2026-03-25 | Web | `https://developers.zoom.example/recording-api` | confirm partner-system room recording limits | host can only schedule one recording worker per occupied room set | No |
| 2026-03-25 | Repo | `https://github.com/zoom-example/recording-sdk-sample` @ `9b17c4d` | verify how upstream sample handles multi-room worker assignment | sample app routes multi-room recording through one canonical allocator callback | No |
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

| Date | Method (`Repro`/`Trace`/`Probe`/`Script`/`Test`/`Setup`) | Exact Command / Method | Observation | Implication |
| --- | --- | --- | --- | --- |
| 2026-03-25 | Trace | local occupied-room repro | failure appears when the second room enters allocation path | worker allocation decision is the likely defect center |
| 2026-03-25 | Probe | ad hoc logging around coordinator allocator call | legacy path still selected for multi-room case | design and implementation should remove dual-path behavior |

### External Code / Dependency Findings

- Upstream repo / package / sample examined:
  - `https://github.com/zoom-example/recording-sdk-sample`
- Version / tag / commit / release:
  - commit `9b17c4d`
- Files, endpoints, or examples examined:
  - sample recording coordinator and multi-room callback wiring
- Relevant behavior, contract, or constraint learned:
  - upstream sample never routes this flow through a second fallback allocator
- Confidence and freshness:
  - Medium-High / 2026-03-25

### Reproduction / Environment Setup

- Required services, mocks, or emulators:
  - local Zoom adapter stub with occupied-room fixture
- Required config, feature flags, or env vars:
  - recording feature flag enabled
- Required fixtures, seed data, or accounts:
  - two occupied rooms in one host session fixture
- External repos, samples, or artifacts cloned/downloaded for investigation:
  - recording SDK sample repo cloned locally for behavior comparison
- Setup commands that materially affected the investigation:
  - local fixture bootstrap for dual-room occupied state
- Cleanup notes for temporary investigation-only setup:
  - remove ad hoc logging after root-cause confidence is established

## External / Internet Findings

| Source | Fact / Constraint | Why It Matters | Confidence / Freshness |
| --- | --- | --- | --- |
| `https://developers.zoom.example/recording-api` | one recording worker per occupied room set | allocator must avoid duplicate worker assignment for same occupied set | High / 2026-03-25 |

## Constraints

- partner API constrains worker assignment shape
- current code still carries a dual-path allocator split
- upstream sample confirms the dual-path split is local legacy behavior rather than required partner behavior

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
