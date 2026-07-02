# Implementation Example

This example shows the intended size of a lightweight implementation artifact.

## Inputs

- Investigation notes: `tickets/in-progress/order-submit-timeout/investigation-notes.md`
- Requirements: `tickets/in-progress/order-submit-timeout/requirements.md`
- Design sketch: this file

## Solution Sketch

- Current behavior: order submission retries indefinitely when the payment provider times out.
- Target behavior: stop after three attempts and return a typed timeout result.
- Owning boundary/files: `OrderSubmissionService` owns retry policy; payment adapter only exposes provider calls.
- API/interface changes: no public API shape change.
- File placement decision: keep service and tests in existing order subsystem.
- Obsolete code to remove: ad hoc retry loop inside controller.
- Risks/open questions: ensure existing transient-error behavior still retries.

## Implementation Plan

| Task ID | File/Area | Action | Owner/Concern | Depends On | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| T-001 | `OrderSubmissionService` | Modify | retry policy | none | Done | add max-attempt handling |
| T-002 | controller | Modify | remove misplaced retry loop | T-001 | Done | delegate to service |
| T-003 | service tests | Modify | timeout and transient retry coverage | T-001 | Done | includes edge case |

## Test Strategy

- Unit tests: service retry and timeout cases.
- Integration tests: existing order submission integration suite.
- API/E2E/CLI/process/lifecycle validation: not required; behavior is covered at service boundary.
- Known validation constraints: none.

## Execution Log

| Time/Date | Update | Evidence/Command | Result | Follow-Up |
| --- | --- | --- | --- | --- |
| 2026-03-19 | Implemented max-attempt policy | `pytest tests/orders/test_submission.py` | Passed | Review diff |

## Validation Summary

- Unit/integration result: passed.
- Executable validation result: N/A, service-boundary behavior covered by integration tests.
- Acceptance criteria covered: timeout after three attempts; transient success before limit.
- Blocked or waived validation: none.

## Review Prep

- Changed source files: order submission service and controller.
- Changed tests: order submission tests.
- Related files reviewed: payment adapter contract.
- Known risks for code review: retry ownership should remain in service, not controller.
- Docs impact: none.

## Completion Check

- Implementation complete: yes.
- Required tests pass: yes.
- No obsolete code left in scope: yes.
- File placement remains coherent: yes.
- Validation evidence is sufficient: yes.
- Ready for code review: yes.
