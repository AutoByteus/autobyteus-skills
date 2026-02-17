# Implementation Plan

## Scope Classification

- Classification: `Small` / `Medium` / `Large`
- Reasoning:
- Workflow Depth:
  - `Small` -> draft implementation plan (solution sketch) -> proposed-design-based runtime call stack -> runtime call stack review (iterative deep rounds until `Go Confirmed`) -> finalize implementation plan -> progress tracking
  - `Medium` -> proposed design doc -> proposed-design-based runtime call stack -> runtime call stack review (iterative deep rounds until `Go Confirmed`) -> implementation plan -> progress tracking
  - `Large` -> proposed design doc -> proposed-design-based runtime call stack -> runtime call stack review (iterative deep rounds until `Go Confirmed`) -> implementation plan -> progress tracking

## Upstream Artifacts (Required)

- Investigation notes: `tickets/<ticket-name>/investigation-notes.md`
- Requirements: `tickets/<ticket-name>/requirements.md`
  - Current Status: `Draft` / `Design-ready` / `Refined`
- Runtime call stacks: `tickets/<ticket-name>/proposed-design-based-runtime-call-stack.md`
- Runtime review: `tickets/<ticket-name>/runtime-call-stack-review.md`
- Proposed design (required for `Medium/Large`): `tickets/<ticket-name>/proposed-design.md`

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
- One file at a time is the default; use limited parallel work only when dependency edges require it.
- Update progress after each meaningful status change (file state, test state, blocker state, or design follow-up state).

## Dependency And Sequencing Map

| Order | File/Module | Depends On | Why This Order |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## Requirement And Design Traceability

| Requirement | Design Section | Use Case / Call Stack | Planned Task ID(s) | Verification |
| --- | --- | --- | --- | --- |
| R-001 |  | UC-001 |  | Unit/Integration/E2E |

## Design Delta Traceability (Required For `Medium/Large`)

| Change ID (from proposed design doc) | Change Type | Planned Task ID(s) | Includes Remove/Rename Work | Verification |
| --- | --- | --- | --- | --- |
| C-001 |  |  | Yes/No |  |

## Decommission / Rename Execution Tasks

| Task ID | Item | Action (`Remove`/`Rename`/`Move`) | Cleanup Steps | Risk Notes |
| --- | --- | --- | --- | --- |
| T-DEL-001 |  |  |  |  |

## Step-By-Step Plan

1. 
2. 
3. 

## Per-File Definition Of Done

| File | Implementation Done Criteria | Unit Test Criteria | Integration Test Criteria | E2E Criteria | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Test Strategy

- Unit tests:
- Integration tests:
- E2E feasibility: `Feasible` / `Not Feasible`
- If E2E is not feasible, concrete reason and current constraints:
- Best-available non-E2E verification evidence when E2E is not feasible:
- Residual risk notes:

## Test Feedback Escalation Policy (Execution Guardrail)

- Classification rules for failing integration/E2E tests:
  - First run investigation screen:
    - if issue is cross-cutting, root cause is unclear, or confidence is low, set `Investigation Required = Yes`, pause implementation, and update `tickets/<ticket-name>/investigation-notes.md` before classification write-back.
    - if issue is clearly bounded with high confidence, set `Investigation Required = No` and classify directly.
  - `Local Fix`: no requirement/design change needed; responsibility boundaries remain intact.
  - `Design Impact`: responsibility boundaries drift, architecture change needed, or patch-on-patch complexity appears.
  - `Requirement Gap`: missing/ambiguous requirement or newly discovered requirement-level constraint.
- Required action:
  - `Local Fix` -> implement fix and keep structure clean.
  - `Design Impact` -> stop implementation; update design basis; regenerate call stacks; re-run review to `Go Confirmed`.
  - `Requirement Gap` -> stop implementation; update `requirements.md` to `Refined`; update design basis; regenerate call stacks; re-run review to `Go Confirmed`.
  - when `Investigation Required = Yes`, understanding-stage re-entry is mandatory before design/requirements updates.

## Cross-Reference Exception Protocol

| File | Cross-Reference With | Why Unavoidable | Temporary Strategy | Unblock Condition | Design Follow-Up Status | Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | `Not Needed` / `Needed` / `In Progress` / `Updated` |  |

## Design Feedback Loop

| Smell/Issue | Evidence (Files/Call Stack) | Design Section To Update | Action | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  | Pending |
