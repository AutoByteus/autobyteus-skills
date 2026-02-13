# Implementation Plan

## Scope Classification

- Classification: `Small` / `Medium` / `Large`
- Reasoning:
- Workflow Depth:
  - `Small` -> draft implementation plan (solution sketch) -> proposed-design-based runtime call stack -> runtime call stack review -> refine until review-pass -> progress tracking (proposed design doc optional)
  - `Medium` -> proposed design doc -> proposed-design-based runtime call stack -> runtime call stack review (minimum 3 rounds) -> implementation plan -> progress tracking
  - `Large` -> proposed design doc -> proposed-design-based runtime call stack -> runtime call stack review (minimum 5 rounds) -> implementation plan -> progress tracking

## Plan Maturity

- Current Status: `Draft` / `Blocked By Review Gate` / `Call-Stack-Review-Validated` / `Ready For Implementation`
- Notes:

## Preconditions (Must Be True Before Finalizing This Plan)

- Runtime call stack review artifact exists:
- All in-scope use cases reviewed:
- No unresolved blocking findings:
- Minimum review rounds satisfied:
  - `Small`: >= 1
  - `Medium`: >= 3
  - `Large`: >= 5
- Final gate decision in review artifact is `Implementation can start: Yes`:

## Solution Sketch (Required For `Small`, Optional Otherwise)

- Use Cases In Scope:
- Touched Files/Modules:
- API/Behavior Delta:
- Key Assumptions:
- Known Risks:

## Runtime Call Stack Review Gate (Required Before Implementation)

| Round | Use Case | Call Stack Location | Review Location | Naming Naturalness | File/API Naming Clarity | Business Flow Completeness | Structure & SoC Check | Unresolved Blocking Findings | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  | `tickets/<ticket-name>/proposed-design-based-runtime-call-stack.md` | `tickets/<ticket-name>/runtime-call-stack-review.md` | Pass/Fail | Pass/Fail | Pass/Fail | Pass/Fail | Yes/No | Pass/Fail |
| 2 |  | `tickets/<ticket-name>/proposed-design-based-runtime-call-stack.md` | `tickets/<ticket-name>/runtime-call-stack-review.md` | Pass/Fail | Pass/Fail | Pass/Fail | Pass/Fail | Yes/No | Pass/Fail |
| 3 (required for `Medium`; required hardening round for `Large`) |  | `tickets/<ticket-name>/proposed-design-based-runtime-call-stack.md` | `tickets/<ticket-name>/runtime-call-stack-review.md` | Pass/Fail | Pass/Fail | Pass/Fail | Pass/Fail | Yes/No | Pass/Fail |
| 4 (required hardening round for `Large`) |  | `tickets/<ticket-name>/proposed-design-based-runtime-call-stack.md` | `tickets/<ticket-name>/runtime-call-stack-review.md` | Pass/Fail | Pass/Fail | Pass/Fail | Pass/Fail | Yes/No | Pass/Fail |
| 5 (required gate-eligible round for `Large`) |  | `tickets/<ticket-name>/proposed-design-based-runtime-call-stack.md` | `tickets/<ticket-name>/runtime-call-stack-review.md` | Pass/Fail | Pass/Fail | Pass/Fail | Pass/Fail | Yes/No | Pass/Fail |
| N (optional) |  | `tickets/<ticket-name>/proposed-design-based-runtime-call-stack.md` | `tickets/<ticket-name>/runtime-call-stack-review.md` | Pass/Fail | Pass/Fail | Pass/Fail | Pass/Fail | Yes/No | Pass/Fail |

## Go / No-Go Decision

- Decision: `Go` / `No-Go`
- Evidence:
  - Review rounds completed:
  - Final review round:
  - Final review gate line (`Implementation can start`):
- If `No-Go`, required refinement target:
  - `Small`: refine implementation plan (and add design notes if needed), then regenerate call stack and re-review.
  - `Medium/Large`: refine proposed design document, then regenerate call stack and re-review.
- If `No-Go`, do not continue with dependency sequencing or implementation kickoff.

## Principles

- Bottom-up: implement dependencies before dependents.
- Test-driven: write unit tests (and integration tests when needed) before or alongside implementation.
- Mandatory modernization rule: no backward-compatibility shims or legacy branches.
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
