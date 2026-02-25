# Implementation Plan

## Scope Classification

- Classification: `Small` / `Medium` / `Large`
- Reasoning:
- Workflow Depth:
  - `Small` -> draft implementation plan (solution sketch) -> future-state runtime call stack -> future-state runtime call stack review (iterative deep rounds until `Go Confirmed`) -> finalize implementation plan -> implementation progress tracking -> internal code review gate -> aggregated API/E2E validation -> docs sync
  - `Medium` -> proposed design doc -> future-state runtime call stack -> future-state runtime call stack review (iterative deep rounds until `Go Confirmed`) -> implementation plan -> implementation progress tracking -> internal code review gate -> aggregated API/E2E validation -> docs sync
  - `Large` -> proposed design doc -> future-state runtime call stack -> future-state runtime call stack review (iterative deep rounds until `Go Confirmed`) -> implementation plan -> implementation progress tracking -> internal code review gate -> aggregated API/E2E validation -> docs sync

## Upstream Artifacts (Required)

- Investigation notes: `tickets/in-progress/<ticket-name>/investigation-notes.md`
- Requirements: `tickets/in-progress/<ticket-name>/requirements.md`
  - Current Status: `Draft` / `Design-ready` / `Refined`
- Runtime call stacks: `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack.md`
- Runtime review: `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack-review.md`
- Proposed design (required for `Medium/Large`): `tickets/in-progress/<ticket-name>/proposed-design.md`

## Plan Maturity

- Current Status: `Draft` / `Blocked By Review Gate` / `Review-Gate-Validated` / `Ready For Implementation`
- Notes:

## Preconditions (Must Be True Before Finalizing This Plan)

- `requirements.md` is at least `Design-ready` (`Refined` allowed):
- Runtime call stack review artifact exists and is current:
- All in-scope use cases reviewed:
- No unresolved blocking findings:
- Runtime review has `Go Confirmed` with two consecutive clean deep-review rounds:

## Solution Sketch (Required For `Small`, Optional Otherwise)

- Use Cases In Scope:
- Requirement Coverage Guarantee (all requirements mapped to at least one use case):
- Design-Risk Use Cases (if any, with risk/objective):
- Target Architecture Shape (for `Small`, mandatory):
- New Layers/Modules/Boundary Interfaces To Introduce:
- Touched Files/Modules:
- API/Behavior Delta:
- Key Assumptions:
- Known Risks:

## Runtime Call Stack Review Gate Summary (Required)

| Round | Review Result | Findings Requiring Write-Back | Write-Back Completed | Round State (`Reset`/`Candidate Go`/`Go Confirmed`) | Clean Streak After Round |
| --- | --- | --- | --- | --- | --- |
| 1 | Pass/Fail | Yes/No | Yes/No/N/A |  |  |
| 2 | Pass/Fail | Yes/No | Yes/No/N/A |  |  |
| N | Pass/Fail | Yes/No | Yes/No/N/A |  |  |

## Go / No-Go Decision

- Decision: `Go` / `No-Go`
- Evidence:
  - Final review round:
  - Clean streak at final round:
  - Final review gate line (`Implementation can start`):
- If `No-Go`, required refinement target:
  - `Small`: refine implementation plan (and add design notes if needed), then regenerate call stack and re-review.
  - `Medium/Large`: refine proposed design document, then regenerate call stack and re-review.
- If `No-Go`, do not continue with dependency sequencing or implementation kickoff.

## Principles

- Bottom-up: implement dependencies before dependents.
- Test-driven: write unit tests and integration tests alongside implementation.
- Mandatory modernization rule: no backward-compatibility shims or legacy branches.
- Choose the proper structural change for architecture integrity; do not prefer local hacks just because they are smaller.
- One file at a time is the default; use limited parallel work only when dependency edges require it.
- Update progress after each meaningful status change (file state, test state, blocker state, or design follow-up state).

## Dependency And Sequencing Map

| Order | File/Module | Depends On | Why This Order |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## Requirement And Design Traceability

| Requirement | Design Section | Use Case / Call Stack | Planned Task ID(s) | Stage 5 Verification (Unit/Integration) | Stage 6 Scenario ID(s) |
| --- | --- | --- | --- | --- | --- |
| R-001 |  | UC-001 |  | Unit/Integration | SV-001 |

## Design Delta Traceability (Required For `Medium/Large`)

| Change ID (from proposed design doc) | Change Type | Planned Task ID(s) | Includes Remove/Rename Work | Verification |
| --- | --- | --- | --- | --- |
| C-001 |  |  | Yes/No | Unit/Integration + SV-Scenario |

## Decommission / Rename Execution Tasks

| Task ID | Item | Action (`Remove`/`Rename`/`Move`) | Cleanup Steps | Risk Notes |
| --- | --- | --- | --- | --- |
| T-DEL-001 |  |  |  |  |

## Step-By-Step Plan

1. 
2. 
3. 

## Per-File Definition Of Done

| File | Implementation Done Criteria | Unit Test Criteria | Integration Test Criteria | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Internal Code Review Gate Plan (Stage 5.5)

- Gate artifact path: `tickets/in-progress/<ticket-name>/internal-code-review.md`
- Source-file scope only (exclude tests):
- `>300` line changed source files SoC assessment approach:
- `>400` line changed source file policy and expected action:
- Allowed exceptions and required rationale style:

| File | Current Line Count | Adds/Expands Functionality (`Yes`/`No`) | SoC Risk (`Low`/`Medium`/`High`) | Required Action (`Keep`/`Split`/`Move`/`Refactor`) | Expected Review Classification if not addressed |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Test Strategy

- Unit tests:
- Integration tests:
- Stage 5 boundary: file/module/service-level verification only (unit + integration).
- Stage 5.5 handoff notes for internal code review:
  - predicted design-impact hotspots:
  - files likely to exceed size/SoC thresholds:
- Stage 6 handoff notes for aggregated validation:
  - critical flows to validate (API/E2E):
  - expected scenario count:
  - known environment constraints:

## Aggregated API/E2E Validation Scenario Catalog (Stage 6 Input)

| Scenario ID | Source Type (`Requirement`/`Design-Risk`) | Requirement ID(s) | Use Case ID(s) | Validation Level (`API`/`E2E`) | Expected Outcome |
| --- | --- | --- | --- | --- | --- |
| SV-001 | Requirement | R-001 | UC-001 | API |  |

## Aggregated Validation Escalation Policy (Stage 6 Guardrail)

- Classification rules for failing aggregated validation scenarios:
  - choose exactly one classification for the current failure event: `Local Fix`, `Design Impact`, or `Requirement Gap`.
  - First run investigation screen:
    - if issue is cross-cutting, root cause is unclear, or confidence is low, set `Investigation Required = Yes`, pause implementation, and update `tickets/in-progress/<ticket-name>/investigation-notes.md` before classification write-back.
    - if issue is clearly bounded with high confidence, set `Investigation Required = No` and classify directly.
  - `Local Fix`: no requirement/design change needed; responsibility boundaries remain intact.
  - `Design Impact`: responsibility boundaries drift, architecture change needed, or patch-on-patch complexity appears.
  - `Requirement Gap`: missing/ambiguous requirement or newly discovered requirement-level constraint.
- Required action:
  - `Local Fix` -> update implementation/review artifacts first, then implement fix, rerun `Stage 5` + `Stage 5.5`, then rerun affected scenarios.
  - `Design Impact` -> set `Investigation Required = Yes` (mandatory checkpoint), update `investigation-notes.md`, then follow full-chain re-entry.
  - if requirement-level gaps are discovered during the design-impact investigation checkpoint -> reclassify as `Requirement Gap` and follow the requirement-gap path.
  - `Design Impact` (after checkpoint, still design impact) -> return to `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 5.5`; rerun affected scenarios.
  - `Requirement Gap` -> return to `Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 5.5`; rerun affected scenarios.
  - unclear/cross-cutting root cause -> return to `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 5.5`; rerun affected scenarios.
  - when `Investigation Required = Yes`, understanding-stage re-entry is mandatory before design/requirements updates.

## Cross-Reference Exception Protocol

| File | Cross-Reference With | Why Unavoidable | Temporary Strategy | Unblock Condition | Design Follow-Up Status | Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | `Not Needed` / `Needed` / `In Progress` / `Updated` |  |

## Design Feedback Loop

| Smell/Issue | Evidence (Files/Call Stack) | Design Section To Update | Action | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  | Pending |
