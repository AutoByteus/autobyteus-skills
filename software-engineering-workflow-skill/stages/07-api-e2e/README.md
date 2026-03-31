# Stage 7 API/E2E And Executable Validation

## Purpose

Validate the implemented behavior against acceptance criteria and relevant runtime spines using executable validation scenarios appropriate to the system, including API, UI, native desktop, CLI, process/lifecycle, integration, or distributed flows when relevant.

## Enter This Stage When

- Stage 6 is complete
- source edits, unit tests, and integration tests are in a stable enough state to validate executable behavior across the in-scope interfaces and runtime boundaries

## Stage-Owned Outputs

- `tickets/in-progress/<ticket-name>/api-e2e-testing.md`
- scenario implementations and execution results

## Exit Gate

Leave Stage 7 only when all executable in-scope acceptance criteria are `Passed` or explicitly `Waived` by the user for infeasible cases, and the relevant spines have matching evidence.

## Local Files

- `api-e2e-guide.md`: scenario, feasibility, and re-entry rules
- `api-e2e-testing-template.md`: canonical Stage 7 executable-validation artifact
