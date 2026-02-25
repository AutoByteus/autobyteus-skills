# Aggregated Validation

Use this document for Stage 6 aggregated validation (API/E2E).
Do not use this file for unit/integration tracking; that belongs in `implementation-progress.md`.
Stage 6 may start only after `Stage 5.5` internal code review gate result is `Pass`.

## Validation Scope

- Ticket:
- Scope classification: `Small` / `Medium` / `Large`
- Requirements source: `tickets/in-progress/<ticket-name>/requirements.md`
- Call stack source: `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack.md`
- Design source (`Medium/Large`): `tickets/in-progress/<ticket-name>/proposed-design.md`

## Coverage Rules

- Every critical requirement must map to at least one scenario.
- Every in-scope use case must map to at least one scenario, or explicitly `N/A` with rationale.
- `Design-Risk` scenarios must include explicit technical objective/risk and expected outcome.
- Manual testing is not part of the default workflow.

## Scenario Catalog

| Scenario ID | Source Type (`Requirement`/`Design-Risk`) | Requirement ID(s) | Use Case ID(s) | Level (`API`/`E2E`) | Objective/Risk | Expected Outcome | Command/Harness | Status (`Not Started`/`In Progress`/`Passed`/`Failed`/`Blocked`/`N/A`) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SV-001 | Requirement | R-001 | UC-001 | API | N/A |  |  | Not Started |

## Failure Escalation Log

| Date | Scenario ID | Failure Summary | Investigation Required (`Yes`/`No`) | Classification (`Local Fix`/`Design Impact`/`Requirement Gap`) | Action Path | `investigation-notes.md` Updated | Requirements Updated | Design Updated | Call Stack Regenerated | Review Re-Entry Round | Resolved |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | SV-001 |  |  |  |  |  |  |  |  |  | No |

Rules:
- `Local Fix` requires artifact update first, then fix, then rerun `Stage 5` + `Stage 5.5` before rerunning affected scenarios.
- `Design Impact` requires `Investigation Required = Yes` and investigation checkpoint before design write-backs.
- If requirement-level gaps are found during design-impact investigation, reclassify to `Requirement Gap`.
- No direct source-code patching is allowed before required upstream artifacts are updated.
- `Design Impact` requires full-chain re-entry: `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 5.5` before rerunning affected scenarios.
- `Requirement Gap` requires full-chain re-entry: `Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 5.5` before rerunning affected scenarios.
- unclear/cross-cutting root cause requires full-chain re-entry: `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 5.5`.

## Feasibility And Risk Record

- Any infeasible scenarios (`Yes`/`No`):
- If `Yes`, concrete infeasibility reason per scenario:
- Environment constraints (secrets/tokens/access limits/dependencies):
- Compensating automated evidence:
- Residual risk notes:

## Stage 6 Gate Decision

- Stage 6 complete: `Yes` / `No`
- Critical scenarios passed: `Yes` / `No`
- Infeasibility + compensating evidence documented (if applicable): `Yes` / `No` / `N/A`
- Unresolved escalation items: `Yes` / `No`
- Notes:
