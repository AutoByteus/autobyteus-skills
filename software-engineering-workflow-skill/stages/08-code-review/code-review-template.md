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
- Shared Design Principles: `shared/design-principles.md`
- Common Design Practices: `shared/common-design-practices.md`
- Code Review Principles: `stages/08-code-review/code-review-principles.md`

## Scope

- Files reviewed (source + tests):
- Why these files:

## Source File Size And Structure Audit (Mandatory)

| File | Effective Non-Empty Line Count | Adds/Expands Functionality (`Yes`/`No`) | `>500` Hard-Limit Check | `>220` Changed-Line Delta Gate | Scope-Appropriate SoC Check (`Pass`/`Fail`) | Module/File Placement Check (`Pass`/`Fail`) | Preliminary Classification (`N/A`/`Local Fix`/`Validation Gap`/`Design Impact`/`Requirement Gap`/`Unclear`) | Required Action (`Keep`/`Split`/`Move`/`Refactor`) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Pass/Fail/N/A | Pass/Fail/N/A | Pass/Fail | Pass/Fail |  |  |

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
- SoC rule: if a changed file mixes unrelated responsibilities or hides multiple owners in one boundary, mark `Scope-Appropriate SoC Check = Fail` and require `Split`/`Refactor`.
- Module/file placement rule: if a file path/folder obscures the owning concern or puts platform-specific code in an unrelated location, mark `Module/File Placement Check = Fail` and record the required `Move`/`Split` action.
- During Stage 8, `workflow-state.md` should show `Current Stage = 8` and `Code Edit Permission = Locked`.

## Structural Integrity Checks (Mandatory)

| Check | Result (`Pass`/`Fail`) | Evidence | Required Action |
| --- | --- | --- | --- |
| Data-flow spine inventory preservation against design basis |  |  |  |
| Ownership boundary preservation and clarity |  |  |  |
| Support structure clarity (support branches serve clear owners and stay off the main line) |  |  |  |
| Scope-appropriate separation of concerns and file responsibility clarity |  |  |  |
| Repeated coordination ownership check (policy has a clear owner where needed) |  |  |  |
| Empty indirection check (no pass-through-only boundary) |  |  |  |
| Ownership-driven dependency check (no forbidden shortcuts or unjustified cycles) |  |  |  |
| Module/file placement check (file/folder path matches owning concern or explicitly justified shared boundary) |  |  |  |
| Flat-vs-over-split layout judgment (layout is readable for the scope and not artificially fragmented) |  |  |  |
| Interface/API/query/command/service-method boundary clarity (one subject, one responsibility, explicit identity shape) |  |  |  |
| Naming-to-responsibility alignment and drift check |  |  |  |
| Validation evidence sufficiency for the changed flow |  |  |  |
| No backward-compatibility mechanisms (no compatibility wrappers/dual-path behavior) |  |  |  |
| No legacy code retention for old behavior |  |  |  |

## Findings

- If none, write `None`.
- Otherwise:
  - `[CR-001] File: ... | Type: Spine/Ownership/SupportStructure/SoC/Dependency/Placement/InterfaceBoundary/Naming/Duplication/Legacy/BackwardCompat/FileSize/Complexity/ValidationGap | Severity: Blocker/Major/Minor | Evidence: ... | Required update: ...`

## Re-Entry Declaration (Mandatory On `Fail`)

- Trigger Stage:
- Classification (`Local Fix`/`Validation Gap`/`Design Impact`/`Requirement Gap`/`Unclear`):
- Required Return Path:
  - `Local Fix` -> update implementation artifacts first -> code fix -> rerun `Stage 6 -> Stage 7 -> Stage 8`
  - `Validation Gap` -> update Stage 7 validation coverage/evidence and rerun `Stage 7 -> Stage 8`
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
  - Data-flow spine inventory preservation = `Pass`
  - Ownership boundary preservation = `Pass`
  - Support structure clarity = `Pass`
  - Scope-appropriate separation of concerns and file responsibility clarity = `Pass`
  - Repeated coordination ownership check = `Pass`
  - Empty indirection check = `Pass`
  - Ownership-driven dependency check = `Pass`
  - Module/file placement check = `Pass`
  - Flat-vs-over-split layout judgment = `Pass`
  - Interface/API/query/command/service-method boundary clarity = `Pass`
  - Naming-to-responsibility alignment and drift check = `Pass`
  - Validation evidence sufficiency = `Pass`
  - No backward-compatibility mechanisms = `Pass`
  - No legacy code retention = `Pass`
- Classification rule: if the main issue is insufficient validation evidence, classify as `Validation Gap` and return to `Stage 7`; otherwise, if any mandatory structural pass check fails, do not classify as `Local Fix` by default and classify as `Design Impact` unless clear requirement ambiguity is the primary cause.
- Wrong-location files are structural failures when the path makes ownership unclear; require explicit `Move`/`Split` or a justified shared-boundary decision.
- Notes:
