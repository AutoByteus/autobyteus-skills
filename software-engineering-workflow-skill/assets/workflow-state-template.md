# Workflow State

Use this file as the mandatory stage-control artifact for the ticket.
Update this file before every stage transition and before any source-code edit.

## Current Snapshot

- Ticket:
- Current Stage: `0` / `1` / `2` / `3` / `4` / `5` / `5.5` / `6` / `7` / `8`
- Next Stage:
- Code Edit Permission: `Locked` / `Unlocked`
- Active Re-Entry: `No` / `Yes`
- Re-Entry Classification (`Local Fix`/`Design Impact`/`Requirement Gap`/`Unclear`): `N/A`
- Last Transition ID:
- Last Updated:

## Stage Gates

| Stage | Gate Status (`Not Started`/`In Progress`/`Pass`/`Fail`/`Blocked`) | Gate Rule Summary | Evidence |
| --- | --- | --- | --- |
| 0 Bootstrap + Investigation | Not Started | Ticket bootstrap complete + `requirements.md` Draft + investigation notes current |  |
| 1 Requirements | Not Started | `requirements.md` is `Design-ready`/`Refined` |  |
| 2 Design Basis | Not Started | Design basis updated for scope (`implementation-plan.md` sketch or `proposed-design.md`) |  |
| 3 Runtime Modeling | Not Started | `future-state-runtime-call-stack.md` current |  |
| 4 Review Gate | Not Started | Runtime review `Go Confirmed` (two clean rounds) |  |
| 5 Implementation | Not Started | Plan/progress current + unit/integration verification complete |  |
| 5.5 Internal Code Review | Not Started | Internal review gate `Pass`/`Fail` recorded |  |
| 6 Aggregated Validation | Not Started | AC closure + API/E2E scenario gate complete |  |
| 7 Docs Sync | Not Started | Docs updated or no-impact rationale recorded |  |
| 8 Handoff / Ticket State | Not Started | Final handoff complete + ticket state decision recorded |  |

## Pre-Edit Checklist (Stage 5 Only)

- Current Stage is `5`: `Yes` / `No`
- Code Edit Permission is `Unlocked`: `Yes` / `No`
- Stage 4 gate is `Go Confirmed`: `Yes` / `No`
- Required upstream artifacts are current: `Yes` / `No`
- Pre-Edit Checklist Result: `Pass` / `Fail`
- If `Fail`, source code edits are prohibited.

## Re-Entry Declaration

- Trigger Stage (`5.5`/`6`):
- Classification (`Local Fix`/`Design Impact`/`Requirement Gap`/`Unclear`):
- Required Return Path:
- Required Upstream Artifacts To Update Before Code Edits:
- Resume Condition:

## Transition Log (Append-Only)

| Transition ID | Date | From Stage | To Stage | Reason | Classification | Code Edit Permission After Transition | Evidence Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | YYYY-MM-DD | 0 | 1 | Requirements refined to design-ready | N/A | Locked | requirements.md, workflow-state.md |

## Audible Notification Log (Optional Tracking)

| Date | Trigger Type (`Transition`/`Gate`/`Re-entry`/`LockChange`) | Summary Spoken | Speak Tool Result (`Success`/`Failed`) | Fallback Text Logged |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Transition | Stage 0 complete, moving to Stage 1 requirements refinement. | Success | N/A |

## Process Violation Log

| Date | Violation ID | Violation | Detected At Stage | Action Taken | Cleared |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | V-001 | Source code edited while `Code Edit Permission = Locked` | 2 | Stopped edits, declared re-entry, updated upstream artifacts | No |
