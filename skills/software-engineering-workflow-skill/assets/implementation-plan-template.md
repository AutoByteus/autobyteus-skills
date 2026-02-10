# Implementation Plan

## Scope Classification

- Classification: `Small` / `Medium` / `Large`
- Reasoning:
- Workflow Depth:
  - `Small` -> draft implementation plan (solution sketch) -> design-based runtime call stack -> runtime call stack review -> refine until review-pass -> progress tracking (design doc optional)
  - `Medium/Large` -> design doc -> design-based runtime call stack -> runtime call stack review -> implementation plan -> progress tracking

## Plan Maturity

- Current Status: `Draft` / `Call-Stack-Review-Validated` / `Ready For Implementation`
- Notes:

## Solution Sketch (Required For `Small`, Optional Otherwise)

- Use Cases In Scope:
- Touched Files/Modules:
- API/Behavior Delta:
- Key Assumptions:
- Known Risks:

## Runtime Call Stack Review Gate (Required Before Implementation)

| Use Case | Call Stack Location | Review Location | Business Flow Completeness | Structure & SoC Check | Dependency Flow Smells | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
|  | `tickets/<ticket-name>/design-based-runtime-call-stack.md` | `tickets/<ticket-name>/runtime-call-stack-review.md` | Pass/Fail | Pass/Fail |  | Pass/Fail |

## Go / No-Go Decision

- Decision: `Go` / `No-Go`
- If `No-Go`, required refinement target:
  - `Small`: refine implementation plan (and add design notes if needed), then regenerate call stack and re-review.
  - `Medium/Large`: refine design document, then regenerate call stack and re-review.

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
