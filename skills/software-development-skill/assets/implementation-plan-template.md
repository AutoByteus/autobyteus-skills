# Implementation Plan

## Scope Classification

- Classification: `Small` / `Medium` / `Large`
- Reasoning:
- Workflow Depth:
  - `Small` -> draft implementation plan (solution sketch) -> runtime simulation -> refine same plan until simulation-validated -> progress tracking (design doc optional)
  - `Medium/Large` -> design doc -> runtime simulation -> implementation plan -> progress tracking

## Plan Maturity

- Current Status: `Draft` / `Simulation-Validated` / `Ready For Implementation`
- Notes:

## Solution Sketch (Required For `Small`, Optional Otherwise)

- Use Cases In Scope:
- Touched Files/Modules:
- API/Behavior Delta:
- Key Assumptions:
- Known Risks:

## Use Case Simulation Gate (Required Before Implementation)

| Use Case | Simulation Location | Primary Path Covered | Fallback/Error Covered (If Relevant) | Gaps | Status |
| --- | --- | --- | --- | --- | --- |
|  | `docs/simulated-runtime-call-stack.md` | Yes/No | Yes/No |  | Pending |

## Simulation Cleanliness Checklist (Pre-Implementation Review)

| Check | Result | Notes |
| --- | --- | --- |
| Use case is fully achievable end-to-end | Pass/Fail |  |
| Separation of concerns is clean per file/module | Pass/Fail |  |
| Boundaries and API ownership are clear | Pass/Fail |  |
| Dependency flow is reasonable (no accidental cycle/leaky cross-reference) | Pass/Fail |  |
| No major structure/design smell in call stack | Pass/Fail |  |

## Go / No-Go Decision

- Decision: `Go` / `No-Go`
- If `No-Go`, required refinement target:
  - `Small`: refine implementation plan (and add design notes if needed), then re-simulate.
  - `Medium/Large`: refine design document, then re-simulate.

## Principles

- Bottom-up: implement dependencies before dependents.
- Test-driven: write unit tests (and integration tests when needed) before or alongside implementation.
- One file at a time is the default: complete a file and its tests before moving on when dependency graph is clean.
- Exception rule for rare cross-referencing: allow temporary partial implementation only when necessary, and record the design smell and follow-up design change.
- Update progress after each meaningful status change (file state, test state, blocker state, or design follow-up state).

## Dependency And Sequencing Map

| Order | File/Module | Depends On | Why This Order |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## Design Delta Traceability (Required For `Medium/Large`)

| Change ID (from design doc) | Change Type | Planned Task ID(s) | Includes Remove/Rename Work | Verification |
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

| File | Implementation Done Criteria | Unit Test Criteria | Integration Test Criteria | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Cross-Reference Exception Protocol

| File | Cross-Reference With | Why Unavoidable | Temporary Strategy | Unblock Condition | Design Follow-Up Status | Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | `Not Needed` / `Needed` / `In Progress` / `Updated` |  |

## Design Feedback Loop

| Smell/Issue | Evidence (Files/Call Stack) | Design Section To Update | Action | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  | Pending |

## Test Strategy

- Unit tests: 
- Integration tests: 
- Test data / fixtures: 
