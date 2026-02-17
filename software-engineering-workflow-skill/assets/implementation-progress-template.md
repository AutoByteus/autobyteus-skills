# Implementation Progress

This document tracks implementation and test progress in real time at file level, including blockers and required escalation paths.

## When To Use This Document

- Create this file at implementation kickoff after pre-implementation gates are complete:
  - investigation notes written and current,
  - requirements at least `Design-ready`,
  - future-state runtime call stack review gate is `Go Confirmed` (two consecutive clean deep-review rounds),
  - implementation plan finalized.
- Update it continuously while implementing.
- Record every meaningful change immediately: file status transitions, test status changes, blockers, classification decisions, and escalation actions.

## Kickoff Preconditions Checklist

- Scope classification confirmed (`Small`/`Medium`/`Large`):
- Investigation notes are current (`tickets/<ticket-name>/investigation-notes.md`):
- Requirements status is `Design-ready` or `Refined`:
- Runtime review final gate is `Implementation can start: Yes`:
- Runtime review reached `Go Confirmed` with two consecutive clean deep-review rounds:
- No unresolved blocking findings:

## Legend

- File Status: `Pending`, `In Progress`, `Blocked`, `Completed`, `N/A`
- Unit/Integration/E2E Test Status: `Not Started`, `In Progress`, `Passed`, `Failed`, `Blocked`, `N/A`
- Failure Classification: `Local Fix`, `Design Impact`, `Requirement Gap`, `N/A`
- Investigation Required: `Yes`, `No`, `N/A`
- Design Follow-Up: `Not Needed`, `Needed`, `In Progress`, `Updated`
- Requirement Follow-Up: `Not Needed`, `Needed`, `In Progress`, `Updated`

## Progress Log

- YYYY-MM-DD: Implementation kickoff baseline created.

## Scope Change Log

| Date | Previous Scope | New Scope | Trigger | Required Action |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Small | Medium | Example: architectural complexity exceeded small-scope assumptions | Update requirements/design basis as needed, regenerate call stacks, rerun review to `Go Confirmed`, then resume implementation. |

## File-Level Progress Table

| Change ID | Change Type | File | Depends On | File Status | Unit Test File | Unit Test Status | Integration Test File | Integration Test Status | E2E Scenario | E2E Status | Last Failure Classification | Last Failure Investigation Required | Cross-Reference Smell | Design Follow-Up | Requirement Follow-Up | Last Verified | Verification Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-001 | Modify | `src/example-a.ts` | `src/example-core.ts` | Blocked | `tests/unit/example-a.test.ts` | Blocked | `tests/integration/example-a.integration.test.ts` | Failed | `checkout-happy-path` | Not Started | Design Impact | Yes | `src/example-a.ts <-> src/example-core.ts` | Needed | Not Needed | YYYY-MM-DD | `pnpm exec vitest --run tests/unit/example-a.test.ts` | Waiting for boundary refactor. |
| C-002 | Add | `src/example-core.ts` | N/A | In Progress | `tests/unit/example-core.test.ts` | In Progress | N/A | N/A | N/A | N/A | N/A | N/A | None | Not Needed | Not Needed | YYYY-MM-DD | `pnpm exec vitest --run tests/unit/example-core.test.ts` | Implementing base interfaces. |
| C-003 | Remove | `src/example-util.ts` | N/A | Completed | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | None | Not Needed | Not Needed | YYYY-MM-DD | `rg -n "example-util" src tests` | Utility removed and references cleaned. |

## Failed Integration/E2E Escalation Log (Mandatory)

| Date | Test/Scenario | Failure Summary | Investigation Required (`Yes`/`No`) | `investigation-notes.md` Updated | Classification (`Local Fix`/`Design Impact`/`Requirement Gap`) | Action Path Taken | Requirements Updated | Design Updated | Call Stack Regenerated | Review Re-Entry Round | Resume Condition Met |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | `tests/integration/example-a.integration.test.ts` | Missing flow branch for fallback path | Yes | Yes | Design Impact | Paused implementation, reopened investigation, then updated design basis | No | Yes | Yes | Round 6 | Yes |

Rules:
- If issue scope is large/cross-cutting or root cause confidence is low, `Investigation Required` must be `Yes` and understanding-stage re-entry is required before requirements/design updates.
- `Design Impact` requires pause -> design update -> call stack regeneration -> review re-entry until `Go Confirmed`.
- `Requirement Gap` requires pause -> `requirements.md` update (`Refined`) -> design update -> call stack regeneration -> review re-entry until `Go Confirmed`.

## E2E Feasibility Record

- E2E Feasible In Current Environment: `Yes` / `No`
- If `No`, concrete infeasibility reason:
- Current environment constraints (tokens/secrets/third-party dependency/access limits):
- Best-available non-E2E verification evidence:
- Residual risk accepted:

## Blocked Items

| File | Blocked By | Unblock Condition | Owner/Next Action |
| --- | --- | --- | --- |
| `src/example-a.ts` | `src/example-core.ts` | Core API finalized and tests pass | Resume implementation after boundary update. |

## Design Feedback Loop Log

| Date | Trigger File(s) | Smell Description | Design Section Updated | Update Status | Notes |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | `src/example-a.ts`, `src/example-core.ts` | Bidirectional dependency caused blocked implementation order. | `tickets/<ticket-name>/proposed-design.md` (or `tickets/<ticket-name>/implementation-plan.md` solution sketch for `Small`) -> boundary section | In Progress | Introduce boundary interface to remove cross-reference. |

## Remove/Rename/Legacy Cleanup Verification Log

| Date | Change ID | Item | Verification Performed | Result | Notes |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | C-003 | `src/example-util.ts` | import/reference scan + targeted tests | Passed | No remaining references. |

## Docs Sync Log (Mandatory Post-Implementation)

| Date | Docs Impact (`Updated`/`No impact`) | Files Updated | Rationale | Status |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Updated | `docs/example-feature.md` | Runtime flow changed and new module added | Completed |

## Completion Gate

- Mark `File Status = Completed` only when implementation is done and required tests are passing or explicitly `N/A`.
- For `Rename/Move`/`Remove` tasks, verify obsolete references and dead branches are removed.
- Mark implementation execution complete only when:
  - implementation plan scope is delivered (or deviations are documented),
  - required unit/integration tests pass,
  - feasible E2E scenarios pass, or E2E infeasibility is documented with concrete reason/constraints and best-available non-E2E evidence,
  - docs synchronization result is recorded (`Updated` or `No impact` with rationale).
