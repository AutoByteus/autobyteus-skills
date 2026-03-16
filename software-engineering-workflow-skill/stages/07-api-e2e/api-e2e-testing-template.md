# API/E2E Testing

Use this document for Stage 7 API/E2E test implementation and execution.
Do not use this file for unit/integration tracking; that belongs in `implementation-progress.md`.
Stage 7 starts after Stage 6 implementation (source + unit/integration) is complete.

## Testing Scope

- Ticket:
- Scope classification: `Small` / `Medium` / `Large`
- Workflow state source: `tickets/in-progress/<ticket-name>/workflow-state.md`
- Requirements source: `tickets/in-progress/<ticket-name>/requirements.md`
- Call stack source: `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack.md`
- Design source (`Medium/Large`): `tickets/in-progress/<ticket-name>/proposed-design.md`

## Coverage Rules

- Every critical requirement must map to at least one scenario.
- Every in-scope acceptance criterion (`AC-*`) must map to at least one executable scenario.
- Every in-scope use case must map to at least one scenario, or explicitly `N/A` with rationale.
- Every relevant spine from the approved design basis must map to at least one scenario, or explicitly `N/A` with rationale.
- `Design-Risk` scenarios must include explicit technical objective/risk and expected outcome.
- Use stable scenario IDs with `AV-` prefix (for example: `AV-001`).
- Manual testing is not part of the default workflow.
- Stage 7 cannot close while any acceptance criterion is `Unmapped`, `Not Run`, `Failed`, or `Blocked` unless explicitly marked `Waived` by user decision for infeasible cases.
- During Stage 7 execution, `workflow-state.md` should show `Current Stage = 7` and `Code Edit Permission = Unlocked`.
- Stage 7 includes test-file/harness implementation and test execution.

## Acceptance Criteria Coverage Matrix (Mandatory)

| Acceptance Criteria ID | Requirement ID | Criterion Summary | Scenario ID(s) | Current Status (`Unmapped`/`Not Run`/`Passed`/`Failed`/`Blocked`/`Waived`) | Last Updated |
| --- | --- | --- | --- | --- | --- |
| AC-001 | R-001 |  | AV-001 | Not Run | YYYY-MM-DD |

## Spine Coverage Matrix (Mandatory)

| Spine ID | Spine Scope (`Primary End-to-End`/`Return-Event`/`Bounded Local`) | Governing Owner | Scenario ID(s) | Coverage Status (`Unmapped`/`Planned`/`Passed`/`Failed`/`Blocked`/`N/A`) | Notes |
| --- | --- | --- | --- | --- | --- |
| DS-001 |  |  | AV-001 | Planned |  |

## Scenario Catalog

| Scenario ID | Spine ID(s) | Source Type (`Requirement`/`Design-Risk`) | Acceptance Criteria ID(s) | Requirement ID(s) | Use Case ID(s) | Level (`API`/`E2E`) | Objective/Risk | Expected Outcome | Command/Harness | Status (`Not Started`/`In Progress`/`Passed`/`Failed`/`Blocked`/`N/A`) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AV-001 | DS-001 | Requirement | AC-001 | R-001 | UC-001 | API | N/A |  |  | Not Started |

## Failure Escalation Log

| Date | Scenario ID | Failure Summary | Investigation Required (`Yes`/`No`) | Classification (`Local Fix`/`Design Impact`/`Requirement Gap`/`Unclear`) | Action Path | `investigation-notes.md` Updated | Requirements Updated | Design Updated | Call Stack Regenerated | Review Re-Entry Round | Resolved |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | AV-001 |  |  |  |  |  |  |  |  |  | No |

Rules:
- Before final classification, run an investigation screen:
  - if issue scope is cross-cutting, root cause is unclear, or confidence is low, set `Investigation Required = Yes` and update `investigation-notes.md` first.
  - if issue is clearly bounded with high confidence, classification can proceed directly.
- For each failing scenario, update acceptance-criteria matrix statuses before and after re-entry.
- `Local Fix` requires artifact update first, then fix, then rerun `Stage 6 -> Stage 7` before rerunning affected scenarios.
- `Design Impact` requires `Investigation Required = Yes` and investigation checkpoint before design artifact updates.
- If a potential fix introduces compatibility wrappers/dual-path behavior/legacy retention, degrades decoupling (tight coupling/cycles), or keeps code in the wrong concern folder, classify as `Design Impact` (not `Local Fix`).
- If requirement-level gaps are found during design-impact investigation, reclassify to `Requirement Gap`.
- No direct source-code patching is allowed before required upstream artifacts are updated.
- `Design Impact` requires full-chain re-entry: `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7` before rerunning affected scenarios.
- `Requirement Gap` requires full-chain re-entry: `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7` before rerunning affected scenarios.
- `Unclear`/cross-cutting root cause requires full-chain re-entry: `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`.
- Stage 0 in a re-entry path means re-open bootstrap controls in the same ticket/worktree (`workflow-state.md`, lock state, artifact baselines); do not create a new ticket folder.

## Feasibility And Risk Record

- Any infeasible scenarios (`Yes`/`No`):
- If `Yes`, concrete infeasibility reason per scenario:
- Environment constraints (secrets/tokens/access limits/dependencies):
- Compensating automated evidence:
- Residual risk notes:
- User waiver for infeasible acceptance criteria recorded (`Yes`/`No`):
- If `Yes`, waiver reference (date/user decision):

## Stage 7 Gate Decision

- Stage 7 complete: `Yes` / `No`
- All in-scope acceptance criteria mapped to scenarios: `Yes` / `No`
- All relevant spines mapped to scenarios: `Yes` / `No`
- All executable in-scope acceptance criteria status = `Passed`: `Yes` / `No`
- All executable relevant spines status = `Passed`: `Yes` / `No` / `N/A`
- Critical executable scenarios passed: `Yes` / `No`
- Any infeasible acceptance criteria: `Yes` / `No`
- Explicit user waiver recorded for each infeasible acceptance criterion (if any): `Yes` / `No` / `N/A`
- Unresolved escalation items: `Yes` / `No`
- Ready to enter Stage 8 code review: `Yes` / `No`
- Notes:
