# Internal Code Review

Use this document for `Stage 5.5` pre-aggregated-validation code review.
This gate enforces structure quality, source-file maintainability, and mandatory re-entry rules.

## Review Meta

- Ticket:
- Review Round:
- Trigger Stage: `5` / `6` / `Re-entry`
- Design basis artifact:
- Runtime call stack artifact:

## Scope

- Source files reviewed (exclude tests):
- Why these files:

## Source File Size And SoC Audit (Mandatory)

| File | Current Line Count | Adds/Expands Functionality (`Yes`/`No`) | `>300` SoC Assessment | `>400` Hard Check | Preliminary Classification (`N/A`/`Local Fix`/`Design Impact`/`Requirement Gap`) | Required Action (`Keep`/`Split`/`Move`/`Refactor`) |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Pass/Fail | Pass/Fail |  |  |

Rules:
- For changed source file line count `>300`, SoC assessment is mandatory.
- For changed source file line count `>400` with functionality expansion, default classification is `Design Impact`.
- `>400` exception is allowed only with explicit rationale and split plan.

## Findings

- If none, write `None`.
- Otherwise:
  - `[CR-001] File: ... | Type: SoC/Layering/Naming/Duplication/FileSize/Complexity | Severity: Blocker/Major/Minor | Evidence: ... | Required update: ...`

## Re-Entry Declaration (Mandatory On `Fail`)

- Trigger Stage:
- Classification (`Local Fix`/`Design Impact`/`Requirement Gap`):
- Required Return Path:
  - `Local Fix` -> update implementation artifacts first -> code fix -> rerun `Stage 5` + `Stage 5.5`
  - `Design Impact` -> `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 5.5`
  - `Requirement Gap` -> `Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 5.5`
  - unclear/cross-cutting -> `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 5.5`
- Upstream artifacts required before code edits:
  - `investigation-notes.md` updated (if required):
  - `requirements.md` updated (if required):
  - design basis updated (if required):
  - runtime call stacks + review updated (if required):

## Gate Decision

- Decision: `Pass` / `Fail`
- Implementation can proceed to `Stage 6`: `Yes` / `No`
- Notes:
