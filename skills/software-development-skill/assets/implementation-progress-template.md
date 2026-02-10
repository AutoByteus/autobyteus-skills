# Implementation Progress

This document tracks implementation and test progress at file level, including dependency blockers.

## When To Use This Document

- Create this file at implementation kickoff after required pre-implementation artifacts are ready:
  - `Small`: runtime simulation complete and implementation plan is simulation-validated.
  - `Medium/Large`: design doc + runtime simulation complete and implementation plan ready.
- Update it in real time while implementing.
- Record every meaningful change immediately: file status transitions, test status changes, blockers, and design feedback-loop actions.

## Legend

- File Status: `Pending`, `In Progress`, `Blocked`, `Completed`, `N/A`
- Unit/Integration Test Status: `Not Started`, `In Progress`, `Passed`, `Failed`, `Blocked`, `N/A`
- Design Follow-Up: `Not Needed`, `Needed`, `In Progress`, `Updated`

## Progress Log

- YYYY-MM-DD: Implementation kickoff baseline created (derived from required pre-implementation artifacts for the current scope).

## Scope Change Log

| Date | Previous Scope | New Scope | Trigger | Required Action |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Small | Medium | Example: cross-referencing blocker discovered | Deepen `tickets/<ticket-name>/simulated-runtime-call-stack.md` and start/update `tickets/<ticket-name>/design.md`. |

## Completion Gate

- Mark `File Status = Completed` only when implementation is done and required tests are in a passing state (`Passed`) or explicitly `N/A`.

## File-Level Progress Table

| Change ID | Change Type | File | Depends On | File Status | Unit Test File | Unit Test Status | Integration Test File | Integration Test Status | Cross-Reference Smell | Design Follow-Up | Last Verified | Verification Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-001 | Modify | `src/example-a.ts` | `src/example-core.ts` | Blocked | `tests/unit/example-a.test.ts` | Blocked | `tests/integration/example-a.integration.test.ts` | Not Started | `src/example-a.ts <-> src/example-core.ts` | Needed | YYYY-MM-DD | `pnpm exec vitest --run tests/unit/example-a.test.ts` | Waiting for `example-core` API to stabilize. |
| C-002 | Add | `src/example-core.ts` | N/A | In Progress | `tests/unit/example-core.test.ts` | In Progress | N/A | N/A | None | Not Needed | YYYY-MM-DD | `pnpm exec vitest --run tests/unit/example-core.test.ts` | Implementing base interfaces. |
| C-003 | Remove | `src/example-util.ts` | N/A | Completed | N/A | N/A | N/A | N/A | None | Not Needed | YYYY-MM-DD | `grep -RIn \"example-util\" src tests` | Utility removed and references cleaned. |

## Blocked Items

| File | Blocked By | Unblock Condition | Owner/Next Action |
| --- | --- | --- | --- |
| `src/example-a.ts` | `src/example-core.ts` | Core API finalized and unit tests pass | Resume implementation after core merge. |

## Design Feedback Loop Log

| Date | Trigger File(s) | Smell Description | Design Doc Section Updated | Update Status | Notes |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | `src/example-a.ts`, `src/example-core.ts` | Bidirectional dependency caused blocked implementation order. | `tickets/<ticket-name>/design.md` -> File/Module boundaries | In Progress | Introduce boundary interface to remove cross-reference. |

## Remove/Rename Verification Log

| Date | Change ID | Item | Verification Performed | Result | Notes |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | C-003 | `src/example-util.ts` | import/reference scan + targeted tests | Passed | No remaining references. |
