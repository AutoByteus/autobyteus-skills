# Code Review

Use this document for `Stage 8` code review after Stage 7 API/E2E testing passes.
This gate enforces structure quality, source-file maintainability, and mandatory re-entry rules.

## Review Meta

- Ticket:
- Review Round:
- Trigger Stage: `7` / `Re-entry`
- Workflow state source: `tickets/in-progress/<ticket-name>/workflow-state.md`
- Earlier design artifact(s) reviewed as context:
- Runtime call stack artifact:
- Shared Design Principles: `shared/design-principles.md`
- Common Design Practices: `shared/common-design-practices.md`
- Code Review Principles: `stages/08-code-review/code-review-principles.md`

## Scope

- Files reviewed (source + tests):
- Why these files:

## Source File Size And Structure Audit (Mandatory)

This audit applies to changed source implementation files only.
Test files remain in review scope, but they are not subject to the `>500` hard limit or the `>220` changed-line delta gate.
Use earlier design artifacts as context only. If they conflict with shared principles or clear review findings, classify `Design Impact`.

| Source File | Effective Non-Empty Line Count | Adds/Expands Functionality (`Yes`/`No`) | `>500` Hard-Limit Check | `>220` Changed-Line Delta Gate | Scope-Appropriate SoC Check (`Pass`/`Fail`) | File Placement Check (`Pass`/`Fail`) | Preliminary Classification (`N/A`/`Local Fix`/`Validation Gap`/`Design Impact`/`Requirement Gap`/`Unclear`) | Required Action (`Keep`/`Split`/`Move`/`Refactor`) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Pass/Fail/N/A | Pass/Fail/N/A | Pass/Fail | Pass/Fail |  |  |

Rules:
- Use explicit measurement commands per changed source file:
  - effective non-empty line count: `rg -n "\\S" <file-path> | wc -l`
  - changed-line delta: `git diff --numstat <base-ref>...HEAD -- <file-path>`
- Do not place test files in this table; review them for clarity, maintainability, and evidence quality elsewhere in the code review.
- Enforcement baseline uses effective non-empty line count.
- For effective non-empty line count `<=500`, normal review applies.
- Hard limit rule: if any changed source file has effective non-empty line count `>500`, default classification is `Design Impact` and Stage 8 decision is `Fail`.
- For `>500` hard-limit cases, do not continue by default; apply re-entry mapping first.
- No soft middle band (`501-700`) and no default exception path in this workflow.
- Delta gate: if a single changed source file has `>220` changed lines in current diff, record a design-impact assessment even if file size is `<=500`.
- SoC rule: if a changed file mixes unrelated responsibilities or hides multiple owners in one boundary, mark `Scope-Appropriate SoC Check = Fail` and require `Split`/`Refactor`.
- File-placement rule: if a file path/folder obscures the owning concern or puts platform-specific code in an unrelated location, mark `File Placement Check = Fail` and record the required `Move`/`Split` action.
- During Stage 8, `workflow-state.md` should show `Current Stage = 8` and `Code Edit Permission = Locked`.

## Structural Integrity Checks (Mandatory)

| Check | Result (`Pass`/`Fail`) | Evidence | Required Action |
| --- | --- | --- | --- |
| Data-flow spine inventory clarity and preservation under shared principles |  |  |  |
| Ownership boundary preservation and clarity |  |  |  |
| Support structure clarity (support branches serve clear owners and stay off the main line) |  |  |  |
| Existing capability/subsystem reuse check (no fresh helper where an existing subsystem should own it) |  |  |  |
| Reusable owned structures check (repeated structures extracted into the right owned file instead of copied across files) |  |  |  |
| Shared-structure/data-model tightness check (no kitchen-sink base, no overlapping parallel shapes, specialization/composition used meaningfully) |  |  |  |
| Repeated coordination ownership check (shared policy has a clear owner instead of being repeated across callers) |  |  |  |
| Empty indirection check (no pass-through-only boundary) |  |  |  |
| Scope-appropriate separation of concerns and file responsibility clarity |  |  |  |
| Ownership-driven dependency check (no forbidden shortcuts or unjustified cycles) |  |  |  |
| File placement check (file/folder path matches owning concern or explicitly justified shared boundary) |  |  |  |
| Flat-vs-over-split layout judgment (layout is readable for the scope and not artificially fragmented) |  |  |  |
| Interface/API/query/command/service-method boundary clarity (one subject, one responsibility, explicit identity shape) |  |  |  |
| Naming quality and naming-to-responsibility alignment check (files, folders, APIs, types, functions, parameters, variables) |  |  |  |
| No unjustified duplication of code / repeated structures in changed scope |  |  |  |
| Patch-on-patch complexity control |  |  |  |
| Dead/obsolete code cleanup completeness in changed scope |  |  |  |
| Test quality is acceptable for the changed behavior |  |  |  |
| Test maintainability is acceptable for the changed behavior |  |  |  |
| Validation evidence sufficiency for the changed flow |  |  |  |
| No backward-compatibility mechanisms (no compatibility wrappers/dual-path behavior) |  |  |  |
| No legacy code retention for old behavior |  |  |  |

## Findings

- If none, write `None`.
- Otherwise:
  - `[CR-001] File: ... | Type: Spine/Ownership/SupportStructure/CapabilityReuse/ReusableOwnedStructures/SoC/Dependency/Placement/InterfaceBoundary/Naming/Duplication/Legacy/BackwardCompat/FileSize/Complexity/ValidationGap | Severity: Blocker/Major/Minor | Evidence: ... | Required update: ...`

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
  - earlier design artifacts updated (if required):
  - runtime call stacks + review updated (if required):

## Gate Decision

- Decision: `Pass` / `Fail`
- Implementation can proceed to `Stage 9`: `Yes` / `No`
- Mandatory pass checks:
  - All changed source files have effective non-empty line count `<=500`
  - Required `>220` changed-line delta-gate assessments are recorded for all applicable changed source files
  - Data-flow spine inventory clarity and preservation under shared principles = `Pass`
  - Ownership boundary preservation = `Pass`
  - Support structure clarity = `Pass`
  - Existing capability/subsystem reuse check = `Pass`
  - Reusable owned structures check = `Pass`
  - Shared-structure/data-model tightness check = `Pass`
  - Repeated coordination ownership check = `Pass`
  - Empty indirection check = `Pass`
  - Scope-appropriate separation of concerns and file responsibility clarity = `Pass`
  - Ownership-driven dependency check = `Pass`
  - File placement check = `Pass`
  - Flat-vs-over-split layout judgment = `Pass`
  - Interface/API/query/command/service-method boundary clarity = `Pass`
  - Naming quality and naming-to-responsibility alignment check = `Pass`
  - No unjustified duplication of code / repeated structures in changed scope = `Pass`
  - Patch-on-patch complexity control = `Pass`
  - Dead/obsolete code cleanup completeness in changed scope = `Pass`
  - Test quality is acceptable for the changed behavior = `Pass`
  - Test maintainability is acceptable for the changed behavior = `Pass`
  - Validation evidence sufficiency = `Pass`
  - No backward-compatibility mechanisms = `Pass`
  - No legacy code retention = `Pass`
- Classification rule: if the main issue is insufficient validation evidence, classify as `Validation Gap` and return to `Stage 7`; otherwise, if any mandatory structural pass check fails, do not classify as `Local Fix` by default and classify as `Design Impact` unless clear requirement ambiguity is the primary cause. Independent review may conclude that earlier design artifacts were weak or wrong.
- Wrong-location files are structural failures when the path makes ownership unclear; require explicit `Move`/`Split` or a justified shared-boundary decision.
- Notes:
