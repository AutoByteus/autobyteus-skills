# Implementation Example

Use this as a shape example for:
- `tickets/in-progress/<ticket-name>/implementation.md`

This is not a universal format to copy mechanically.
It demonstrates how one merged file can hold:
- a stable implementation baseline
- live execution tracking through Stages 6, 7, 8, and 9

---

## Scope Classification

- Classification: `Small`
- Reasoning: request changes one primary order-submission spine and one bounded local validation flow without requiring a separate proposed design doc

## Upstream Artifacts (Required)

- Workflow state: `tickets/in-progress/order-submit-timeout/workflow-state.md`
- Investigation notes: `tickets/in-progress/order-submit-timeout/investigation-notes.md`
- Requirements: `tickets/in-progress/order-submit-timeout/requirements.md`
  - Current Status: `Design-ready`
- Runtime call stacks: `tickets/in-progress/order-submit-timeout/future-state-runtime-call-stack.md`
- Future-state runtime call stack review: `tickets/in-progress/order-submit-timeout/future-state-runtime-call-stack-review.md`
- Proposed design (required for `Medium/Large`): `N/A`

## Document Status

- Current Status: `In Execution`
- Notes: baseline finalized after Stage 5 `Go Confirmed`; execution tracking active

## Plan Baseline (Freeze Until Replanning)

### Solution Sketch (Required For `Small`, Optional Otherwise)

- Use Cases In Scope: `UC-001 submit order`, `UC-002 handle downstream timeout`
- Spine Inventory In Scope: `DS-001 request spine`, `DS-002 timeout/error spine`
- Primary Owners / Main Domain Subjects: `OrderController`, `OrderSubmissionService`, `PaymentGatewayClient`
- Requirement Coverage Guarantee: every requirement maps to at least one use case and one Stage 7 scenario
- Design-Risk Use Cases: downstream timeout should not leave duplicate order submission
- Target Architecture Shape: request enters controller, submission service owns sequencing, gateway client owns provider boundary, shared timeout mapper stays under payment subsystem
- New Owners/Boundary Interfaces To Introduce: `payment/timeout-error-mapper.ts`
- Primary file/task set: see `Implementation Work Table`
- API/Behavior Delta: timeout path now returns stable timeout code instead of generic 500
- Key Assumptions: downstream timeout remains detectable from gateway client response/error shape
- Known Risks: retry logic must not duplicate order persistence

### Runtime Call Stack Review Gate Summary (Required)

| Round | Review Result | Findings Requiring Persisted Updates | New Use Cases Discovered | Persisted Updates Completed | Classification (`Design Impact`/`Requirement Gap`/`Unclear`/`N/A`) | Required Re-Entry Path | Round State (`Reset`/`Candidate Go`/`Go Confirmed`) | Clean Streak After Round |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fail | Yes | No | Yes | Design Impact | `3 -> 4 -> 5` | Reset | 0 |
| 2 | Pass | No | No | N/A | N/A | N/A | Candidate Go | 1 |
| 3 | Pass | No | No | N/A | N/A | N/A | Go Confirmed | 2 |

### Go / No-Go Decision

- Decision: `Go`
- Evidence:
  - Final review round: `3`
  - Clean streak at final round: `2`
  - Final review gate line (`Implementation can start`): `Yes`

### Spine-Led Dependency And Sequencing Map

| Order | Spine ID | Owner | Task / File | Depends On | Why This Order |
| --- | --- | --- | --- | --- | --- |
| 1 | DS-002 | PaymentGatewayClient | `payment/timeout-error-mapper.ts` | N/A | timeout mapping is reused by the main request spine |
| 2 | DS-001 | PaymentGatewayClient | `payment/payment-gateway-client.ts` | `payment/timeout-error-mapper.ts` | provider boundary must be stable before orchestrating service |
| 3 | DS-001 | OrderSubmissionService | `orders/order-submission-service.ts` | `payment/payment-gateway-client.ts` | service owns sequencing |
| 4 | DS-001 | OrderController | `orders/order-controller.ts` | `orders/order-submission-service.ts` | entrypoint closes the request spine |

### File Placement Plan (Mandatory)

| Item | Current Path | Target Path | Owning Concern / Platform | Action (`Keep`/`Move`/`Split`/`Promote Shared`) | Verification |
| --- | --- | --- | --- | --- | --- |
| timeout mapper | `orders/order-service.ts` | `payment/timeout-error-mapper.ts` | payment provider boundary | Move | confirm no timeout-mapping logic remains in orders subsystem |
| order submission orchestration | `orders/order-service.ts` | `orders/order-submission-service.ts` | order submission sequencing | Split | verify service owns only order-submission flow |

### Implementation Work Table (Primary Tracker)

| Change ID | Spine ID(s) | Owner | Concern | Current Path | Target Path | Action (`Create`/`Modify`/`Move`/`Split`/`Remove`) | Depends On | Implementation Status (`Planned`/`In Progress`/`Completed`/`Blocked`) | Unit Test File | Unit Test Status (`Planned`/`Passed`/`Failed`/`N/A`) | Integration Test File | Integration Test Status (`Planned`/`Passed`/`Failed`/`N/A`) | Stage 8 Review Status (`Planned`/`Passed`/`Failed`/`N/A`) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | DS-002 | PaymentGatewayClient | timeout mapping ownership | `orders/order-service.ts` | `payment/timeout-error-mapper.ts` | Move | N/A | Completed | `tests/unit/payment/timeout-error-mapper.test.ts` | Passed | N/A | N/A | Passed | timeout mapping removed from orders subsystem |
| T-002 | DS-001 | PaymentGatewayClient | provider boundary timeout handling | `payment/payment-gateway-client.ts` | `payment/payment-gateway-client.ts` | Modify | T-001 | Completed | `tests/unit/payment/payment-gateway-client.test.ts` | Passed | `tests/integration/orders/order-submit.integration.test.ts` | Passed | Passed | gateway client now delegates timeout shaping to payment-owned mapper |
| T-003 | DS-001 | OrderSubmissionService | order submission sequencing | `orders/order-service.ts` | `orders/order-submission-service.ts` | Split | T-002 | Completed | `tests/unit/orders/order-submission-service.test.ts` | Passed | `tests/integration/orders/order-submit.integration.test.ts` | Passed | Passed | sequencing now isolated in service |
| T-004 | DS-001 | OrderController | request entrypoint update | `orders/order-controller.ts` | `orders/order-controller.ts` | Modify | T-003 | Completed | `tests/unit/orders/order-controller.test.ts` | Passed | `tests/integration/orders/order-submit.integration.test.ts` | Passed | Passed | controller now delegates to submission service |

### Requirement, Spine, And Design Traceability

| Requirement | Acceptance Criteria ID(s) | Spine ID(s) | Design Section | Use Case / Call Stack | Planned Task ID(s) | Stage 6 Verification (Unit/Integration) | Stage 7 Scenario ID(s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-001 | AC-001 | DS-001 | Solution Sketch | UC-001 | T-001, T-002 | Unit + Integration | AV-001 |
| R-002 | AC-002 | DS-002 | Solution Sketch | UC-002 | T-001 | Unit + Integration | AV-002 |

### Step-By-Step Plan

1. Extract timeout mapping into payment-owned file.
2. Update payment gateway client to use the new mapper.
3. Split orchestration responsibility out of `orders/order-service.ts`.
4. Update controller to call the new submission service.
5. Run unit/integration tests and continue into Stage 7.

## Execution Tracking (Update Continuously)

### Progress Log

- 2026-03-19: baseline finalized after Stage 5 `Go Confirmed`
- 2026-03-19: extracted timeout mapper into payment subsystem
- 2026-03-19: split order submission orchestration into dedicated service

### Implementation Work Updates

Use this section only for execution-only details that do not belong in the main work table above.

| Change ID | Last Failure Classification | Last Failure Investigation Required | Cross-Reference Smell | Design Follow-Up | Requirement Follow-Up | Last Verified | Verification Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | N/A | No | None | Not Needed | Not Needed | 2026-03-19 | `pnpm vitest --run tests/unit/payment/timeout-error-mapper.test.ts` | timeout mapping removed from orders subsystem |
| T-003 | N/A | No | None | Not Needed | Not Needed | 2026-03-19 | `pnpm vitest --run tests/integration/orders/order-submit.integration.test.ts` | sequencing now isolated in service |

### API/E2E Testing Scenario Log (Stage 7)

| Date | Scenario ID | Spine ID(s) | Governing Owner | Source Type (`Requirement`/`Design-Risk`) | Acceptance Criteria ID(s) | Requirement ID(s) | Use Case ID(s) | Level (`API`/`E2E`) | Status | Failure Summary | Investigation Required (`Yes`/`No`) | Classification (`Local Fix`/`Design Impact`/`Requirement Gap`/`Unclear`) | Action Path Taken | `investigation-notes.md` Updated | Requirements Updated | Design Updated | Call Stack Regenerated | Resume Condition Met |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-03-19 | AV-001 | DS-001 | OrderSubmissionService | Requirement | AC-001 | R-001 | UC-001 | API | Passed | N/A | No | N/A | N/A | No | No | No | No | Yes |
| 2026-03-19 | AV-002 | DS-002 | PaymentGatewayClient | Design-Risk | AC-002 | R-002 | UC-002 | API | Passed | N/A | No | N/A | N/A | No | No | No | No | Yes |

### Code Review Structural Summary (Stage 8)

| Date | Review Round | Data-Flow Spine Inventory Preservation (`Pass`/`Fail`) | Ownership Boundary Preservation (`Pass`/`Fail`) | Support Structure Clarity (`Pass`/`Fail`) | Existing Capability/Subsystem Reuse (`Pass`/`Fail`) | Reusable Owned Structures Check (`Pass`/`Fail`) | Repeated Coordination Ownership (`Pass`/`Fail`) | Empty Indirection Check (`Pass`/`Fail`) | Ownership-Driven Dependency Check (`Pass`/`Fail`) | Scope-Appropriate SoC Check (`Pass`/`Fail`) | File Placement Check (`Pass`/`Fail`) | Flat-Vs-Over-Split Layout Judgment (`Pass`/`Fail`) | Interface/API/Query/Command/Service Boundary Clarity (`Pass`/`Fail`) | Naming-To-Responsibility Check (`Pass`/`Fail`) | Duplication/Patch-Layering Control (`Pass`/`Fail`) | Test Quality (`Pass`/`Fail`) | Test Maintainability (`Pass`/`Fail`) | Validation Evidence Sufficiency (`Pass`/`Fail`) | No Backward-Compatibility Mechanisms (`Pass`/`Fail`) | No Legacy Retention (`Pass`/`Fail`) | Classification (`Local Fix`/`Validation Gap`/`Design Impact`/`Requirement Gap`/`Unclear`) | Decision (`Pass`/`Fail`) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-03-19 | 1 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | N/A | Pass | clean Stage 8 review |

### Docs Sync Log (Mandatory Post-Testing + Review)

| Date | Docs Impact (`Updated`/`No impact`) | Files Updated | Rationale | Status |
| --- | --- | --- | --- | --- |
| 2026-03-19 | Updated | `docs/order-submission.md` | timeout behavior and service ownership changed | Completed |

### Completion Gate

- Stage 6 implementation execution complete: `Yes`
- Stage 7 API/E2E testing complete: `Yes`
- Stage 8 code review complete: `Yes`
- Stage 9 docs sync complete: `Yes`

---

Use this example as a shape guide only.
Keep the real document scoped to the actual ticket and avoid carrying sections that have no value for that change.
