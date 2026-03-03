# Code Review

Use this document for `Stage 8` code review after Stage 7 API/E2E testing passes.
This gate enforces structure quality, source-file maintainability, and mandatory re-entry rules.

## Review Meta

- Ticket:
- Review Round:
- Trigger Stage: `7` / `Re-entry`
- Workflow state source: `tickets/in-progress/<ticket-name>/workflow-state.md`
- Design basis artifact:
- Runtime call stack artifact:

## Scope

- Files reviewed (source + tests):
- Why these files:

## Source File Size And SoC Audit (Mandatory)

| File | Effective Non-Empty Line Count | Adds/Expands Functionality (`Yes`/`No`) | `>500` Hard-Limit Check | `>220` Changed-Line Delta Gate | Preliminary Classification (`N/A`/`Local Fix`/`Design Impact`/`Requirement Gap`/`Unclear`) | Required Action (`Keep`/`Split`/`Move`/`Refactor`) |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Pass/Fail/N/A | Pass/Fail/N/A |  |  |

Rules:
- Use explicit measurement commands per changed source file:
  - effective non-empty line count: `rg -n "\\S" <file-path> | wc -l`
  - changed-line delta: `git diff --numstat <base-ref>...HEAD -- <file-path>`
- Enforcement baseline uses effective non-empty line count.
- For effective non-empty line count `<=500`, normal review applies.
- Hard limit rule: if any changed source file has effective non-empty line count `>500`, default classification is `Design Impact` and Stage 8 decision is `Fail`.
- For `>500` hard-limit cases, do not continue by default; apply re-entry mapping first.
- No soft middle band (`501-700`) and no default exception path in this workflow.
- Delta gate: if a single changed source file has `>220` changed lines in current diff, record a design-impact assessment even if file size is `<=500`.
- During Stage 8, `workflow-state.md` should show `Current Stage = 8` and `Code Edit Permission = Locked`.

## Decoupling And Legacy Rejection Checks (Mandatory)

| Check | Result (`Pass`/`Fail`) | Evidence | Required Action |
| --- | --- | --- | --- |
| Shared-principles alignment check (`SoC` cause, emergent layering, decoupling directionality) |  |  |  |
| Layering extraction check (repeated coordination policy extracted into orchestration/registry/manager boundary where needed) |  |  |  |
| Anti-overlayering check (no unjustified pass-through-only layer) |  |  |  |
| Decoupling check (low coupling, clear dependency direction, no unjustified cycles) |  |  |  |
| No backward-compatibility mechanisms (no compatibility wrappers/dual-path behavior) |  |  |  |
| No legacy code retention for old behavior |  |  |  |

## Findings

- If none, write `None`.
- Otherwise:
  - `[CR-001] File: ... | Type: SoC/Decoupling/Layering/Naming/Duplication/Legacy/BackwardCompat/FileSize/Complexity | Severity: Blocker/Major/Minor | Evidence: ... | Required update: ...`

## Re-Entry Declaration (Mandatory On `Fail`)

- Trigger Stage:
- Classification (`Local Fix`/`Design Impact`/`Requirement Gap`/`Unclear`):
- Required Return Path:
  - `Local Fix` -> update implementation artifacts first -> code fix -> rerun `Stage 6 -> Stage 7 -> Stage 8`
  - `Design Impact` -> `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`
  - `Requirement Gap` -> `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`
  - `Unclear`/cross-cutting -> `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`
  - Stage 0 in a re-entry path means re-open bootstrap controls in the same ticket/worktree (`workflow-state.md`, lock state, artifact baselines); do not create a new ticket folder.
- Upstream artifacts required before code edits:
  - `investigation-notes.md` updated (if required):
  - `requirements.md` updated (if required):
  - design basis updated (if required):
  - runtime call stacks + review updated (if required):

## Gate Decision

- Decision: `Pass` / `Fail`
- Implementation can proceed to `Stage 9`: `Yes` / `No`
- Mandatory pass checks:
  - All changed source files have effective non-empty line count `<=500`
  - Required `>220` changed-line delta-gate assessments are recorded for all applicable changed source files
  - Shared-principles alignment check = `Pass`
  - Layering extraction check = `Pass`
  - Anti-overlayering check = `Pass`
  - Decoupling check = `Pass`
  - No backward-compatibility mechanisms = `Pass`
  - No legacy code retention = `Pass`
- Classification rule: if any mandatory pass check fails, do not classify as `Local Fix` by default; classify as `Design Impact` unless clear requirement ambiguity is the primary cause.
- Notes:
