# Implementation Plan

## Scope Classification

- Classification: `Small` / `Medium` / `Large`
- Reasoning:
- Workflow Depth:
  - `Small` -> draft implementation plan (solution sketch) -> future-state runtime call stack -> future-state runtime call stack review (iterative deep rounds until `Go Confirmed`) -> finalize implementation plan -> implementation progress tracking -> API/E2E testing (implement + execute) -> code review gate -> docs sync -> final handoff -> wait for explicit user verification -> move ticket to `done` -> git finalization/release when git repo
  - `Medium` -> proposed design doc -> future-state runtime call stack -> future-state runtime call stack review (iterative deep rounds until `Go Confirmed`) -> implementation plan -> implementation progress tracking -> API/E2E testing (implement + execute) -> code review gate -> docs sync -> final handoff -> wait for explicit user verification -> move ticket to `done` -> git finalization/release when git repo
  - `Large` -> proposed design doc -> future-state runtime call stack -> future-state runtime call stack review (iterative deep rounds until `Go Confirmed`) -> implementation plan -> implementation progress tracking -> API/E2E testing (implement + execute) -> code review gate -> docs sync -> final handoff -> wait for explicit user verification -> move ticket to `done` -> git finalization/release when git repo

## Upstream Artifacts (Required)

- Workflow state: `tickets/in-progress/<ticket-name>/workflow-state.md`
- Investigation notes: `tickets/in-progress/<ticket-name>/investigation-notes.md`
- Requirements: `tickets/in-progress/<ticket-name>/requirements.md`
  - Current Status: `Design-ready` / `Refined`
- Runtime call stacks: `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack.md`
- Future-state runtime call stack review: `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack-review.md`
- Proposed design (required for `Medium/Large`): `tickets/in-progress/<ticket-name>/proposed-design.md`

## Plan Maturity

- Current Status: `Draft` / `Blocked By Review Gate` / `Review-Gate-Validated` / `Ready For Implementation`
- Notes:

## Preconditions (Must Be True Before Finalizing This Plan)

- `requirements.md` is at least `Design-ready` (`Refined` allowed):
- Acceptance criteria use stable IDs (`AC-*`) with measurable expected outcomes:
- `workflow-state.md` is current and Stage 5 review-gate evidence is recorded:
- Runtime call stack review artifact exists and is current:
- All in-scope use cases reviewed:
- No unresolved blocking findings:
- Future-state runtime call stack review has `Go Confirmed` with two consecutive clean deep-review rounds (no blockers, no required persisted artifact updates, no newly discovered use cases):
- Missing-use-case discovery sweeps completed for the final two clean rounds:
- No newly discovered use cases in the final two clean rounds:

## Solution Sketch (Required For `Small`, Optional Otherwise)

- Use Cases In Scope:
- Spine Inventory In Scope:
- Primary Owners / Main Domain Subjects:
- Requirement Coverage Guarantee (all requirements mapped to at least one use case):
- Design-Risk Use Cases (if any, with risk/objective):
- Target Architecture Shape (for `Small`, mandatory):
- New Owners/Modules/Boundary Interfaces To Introduce:
- Touched Files/Modules:
- API/Behavior Delta:
- Key Assumptions:
- Known Risks:

## Runtime Call Stack Review Gate Summary (Required)

| Round | Review Result | Findings Requiring Persisted Updates | New Use Cases Discovered | Persisted Updates Completed | Classification (`Design Impact`/`Requirement Gap`/`Unclear`/`N/A`) | Required Re-Entry Path | Round State (`Reset`/`Candidate Go`/`Go Confirmed`) | Clean Streak After Round |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Pass/Fail | Yes/No | Yes/No | Yes/No/N/A |  |  |  |  |
| 2 | Pass/Fail | Yes/No | Yes/No | Yes/No/N/A |  |  |  |  |
| N | Pass/Fail | Yes/No | Yes/No | Yes/No/N/A |  |  |  |  |

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
- Spine-led implementation rule: sequence work by spine and owner first; file order is derived from that structure, and any optional module grouping follows the ownership model rather than leading it.
- Mandatory modernization rule: no backward-compatibility shims or legacy branches.
- Mandatory ownership/decoupling/SoC rule: preserve clear subsystem boundaries, one-way dependency direction, and scope-appropriate file responsibilities; avoid adding tight coupling/cycles or mixed-concern files.
- Mandatory file-placement rule: keep each touched file in the folder/boundary that owns its concern; plan explicit moves when current placement is misleading.
- Choose the proper structural change for architecture integrity; do not prefer local hacks just because they are smaller.
- One file at a time is the default; use limited parallel work only when dependency edges require it.
- Update progress after each meaningful status change (file state, test state, blocker state, or design follow-up state).

## Spine-Led Dependency And Sequencing Map

| Order | Spine ID | Owner | Task / File | Depends On | Why This Order |
| --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

## File Placement Plan (Mandatory)

| Item | Current Path | Target Path | Owning Concern / Platform | Action (`Keep`/`Move`/`Split`/`Promote Shared`) | Verification |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Requirement, Spine, And Design Traceability

| Requirement | Acceptance Criteria ID(s) | Spine ID(s) | Design Section | Use Case / Call Stack | Planned Task ID(s) | Stage 6 Verification (Unit/Integration) | Stage 7 Scenario ID(s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-001 | AC-001 | DS-001 |  | UC-001 |  | Unit/Integration | AV-001 |

## Acceptance Criteria To Stage 7 Mapping (Mandatory)

| Acceptance Criteria ID | Requirement ID | Spine ID(s) | Expected Outcome | Stage 7 Scenario ID(s) | Test Level (`API`/`E2E`) | Initial Status (`Planned`/`Blocked`) |
| --- | --- | --- | --- | --- | --- | --- |
| AC-001 | R-001 | DS-001 |  | AV-001 | API | Planned |

## Design Delta Traceability (Required For `Medium/Large`)

| Change ID (from proposed design doc) | Change Type | Planned Task ID(s) | Includes Remove/Rename Work | Verification |
| --- | --- | --- | --- | --- |
| C-001 |  |  | Yes/No | Unit/Integration + AV-Scenario |

## Decommission / Rename Execution Tasks

| Task ID | Item | Action (`Remove`/`Rename`/`Move`) | Cleanup Steps | Risk Notes |
| --- | --- | --- | --- | --- |
| T-DEL-001 |  |  |  |  |

## Step-By-Step Plan

1.
2.
3.

## Backward-Compat And Decoupling Guardrails (Mandatory)

- Backward-compatibility mechanisms introduced: `None` / `List + redesign required`
- Legacy code retained for old behavior: `No` / `Yes (blocked)`
- Decoupling impact assessment completed: `Yes` / `No`
- New tight coupling or cyclic dependency introduced: `No` / `Yes (blocked)`

## Per-File Definition Of Done

| File | Implementation Done Criteria | Unit Test Criteria | Integration Test Criteria | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Code Review Gate Plan (Stage 8)

- Gate artifact path: `tickets/in-progress/<ticket-name>/code-review.md`
- Scope (source + tests):
- line-count measurement command (`effective non-empty`):
  - effective non-empty line count: `rg -n "\\S" <file-path> | wc -l`
  - changed-line delta: `git diff --numstat <base-ref>...HEAD -- <file-path>`
- `>500` effective-line source file hard-limit policy and expected design-impact action:
- per-file diff delta gate (`>220` changed lines) assessment approach:
- Hard-limit handling details in `code-review.md` (required re-entry path and split/refactor plan):
- file-placement review approach (how wrong-folder placements will be detected and corrected):

| File | Current Line Count | Adds/Expands Functionality (`Yes`/`No`) | Ownership/SoC Risk (`Low`/`Medium`/`High`) | Required Action (`Keep`/`Split`/`Move`/`Refactor`) | Expected Review Classification if not addressed |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Test Strategy

- Unit tests:
- Integration tests:
- Stage 6 boundary: file and service-level verification, while preserving readable subsystem grouping, only (unit + integration).
- Stage 7 handoff notes for API/E2E testing:
  - expected acceptance criteria count:
  - critical flows to validate (API/E2E):
  - expected scenario count:
  - known environment constraints:
- Stage 8 handoff notes for code review:
  - predicted design-impact hotspots:
  - predicted file-placement hotspots:
  - predicted interface/API/query/command/service-method boundary hotspots:
  - files likely to exceed size/ownership/SoC thresholds:

## API/E2E Testing Scenario Catalog (Stage 7 Input)

| Scenario ID | Spine ID(s) | Source Type (`Requirement`/`Design-Risk`) | Acceptance Criteria ID(s) | Requirement ID(s) | Use Case ID(s) | Test Level (`API`/`E2E`) | Expected Outcome |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AV-001 | DS-001 | Requirement | AC-001 | R-001 | UC-001 | API |  |

## API/E2E Testing Escalation Policy (Stage 7 Guardrail)

- Classification rules for failing API/E2E scenarios:
  - choose exactly one classification for the current failure event: `Local Fix`, `Design Impact`, `Requirement Gap`, or `Unclear`.
  - do not allow any in-scope acceptance criterion to remain `Unmapped`, `Not Run`, `Failed`, or `Blocked` at Stage 7 close unless explicitly marked `Waived` by user decision for infeasible cases.
  - First run investigation screen:
    - if issue is cross-cutting, root cause is unclear, or confidence is low, set `Investigation Required = Yes`, pause implementation, and update `tickets/in-progress/<ticket-name>/investigation-notes.md` before persisting classification/re-entry records.
    - if issue is clearly bounded with high confidence, set `Investigation Required = No` and classify directly.
  - `Local Fix`: no requirement/design change needed; responsibility boundaries remain intact.
  - `Design Impact`: responsibility boundaries drift, architecture change needed, or patch-on-patch complexity appears.
  - `Requirement Gap`: missing/ambiguous requirement or newly discovered requirement-level constraint.
- Required action:
  - `Local Fix` -> update implementation/review artifacts first, then implement fix, rerun `Stage 6 -> Stage 7`, then rerun affected scenarios.
  - `Design Impact` -> set `Investigation Required = Yes` (mandatory checkpoint), update `investigation-notes.md`, then follow full-chain re-entry.
  - if requirement-level gaps are discovered during the design-impact investigation checkpoint -> reclassify as `Requirement Gap` and follow the requirement-gap path.
  - `Design Impact` (after checkpoint, still design impact) -> return to `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`; rerun affected scenarios.
  - `Requirement Gap` -> return to `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`; rerun affected scenarios.
  - `Unclear`/cross-cutting root cause -> return to `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`; rerun affected scenarios.
  - Stage 0 in a re-entry path means re-open bootstrap controls in the same ticket/worktree (`workflow-state.md`, lock state, artifact baselines); do not create a new ticket folder.
  - when `Investigation Required = Yes`, understanding-stage re-entry is mandatory before design/requirements updates.

## Cross-Reference Exception Protocol

| File | Cross-Reference With | Why Unavoidable | Temporary Strategy | Unblock Condition | Design Follow-Up Status | Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | `Not Needed` / `Needed` / `In Progress` / `Updated` |  |

## Design Feedback Loop

| Smell/Issue | Evidence (Files/Call Stack) | Design Section To Update | Action | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  | Pending |
