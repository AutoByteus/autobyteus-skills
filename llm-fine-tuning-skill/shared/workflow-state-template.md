# Workflow State

Use this file as the mandatory stage-control artifact for the ticket.
Update it before every stage transition and before any source-code edit.

## Current Snapshot

- Ticket:
- Current Stage: `0` / `1` / `2` / `3` / `4` / `5` / `6` / `7` / `8`
- Next Stage:
- Code Edit Permission: `Locked` / `Unlocked`
- Active Re-Entry: `No` / `Yes`
- Re-Entry Classification (`Local Fix` / `Validation Gap` / `Plan Impact` / `Requirement Gap` / `Investigation Gap` / `Unclear`): `N/A`
- Last Transition ID:
- Last Updated:

## Stage 0 Bootstrap Record

- Bootstrap Mode (`Git` / `Non-Git`):
- User-Specified Base Branch:
- Resolved Base Remote:
- Resolved Base Branch:
- Default Finalization Target Remote:
- Default Finalization Target Branch:
- Remote Refresh Performed (`Yes` / `No` / `N/A`):
- Remote Refresh Result:
- Ticket Worktree Path:
- Ticket Branch:

Note:
- Fill this record during Stage 0 and keep it current if Stage 0 is reopened.
- For non-git projects, mark git-only fields as `N/A`.

## Stage Gates

| Stage | Gate Status (`Not Started` / `In Progress` / `Pass` / `Fail` / `Blocked`) | Gate Rule Summary | Evidence |
| --- | --- | --- | --- |
| 0 Bootstrap | Not Started | Ticket bootstrap complete, draft `requirements.md` created, and `workflow-state.md` initialized |  |
| 1 Investigation | Not Started | `investigation-notes.md` current and durable enough to support downstream stages |  |
| 2 Requirements & Success Criteria | Not Started | `requirements.md` is `Plan-ready` or `Refined`, with measurable success criteria |  |
| 3 Experiment Plan | Not Started | `experiment-plan.md` current and implementation-ready |  |
| 4 Implementation | Not Started | `implementation.md` current, planned source/config changes completed for the iteration, and training-ready smoke checks complete |  |
| 5 Training & Validation | Not Started | `training-validation-report.md` current with run evidence, metric outcomes, and explicit gate decision |  |
| 6 Code Review | Not Started | `code-review.md` records a pass or fail decision with deep-learning-specific review checks completed |  |
| 7 Docs Sync | Not Started | `docs-sync.md` current and durable docs updated or truthful no-impact rationale recorded |  |
| 8 Handoff | Not Started | `handoff-summary.md` current, explicit user verification received, ticket moved to `done`, and repository finalization complete when applicable |  |

## Stage Transition Contract

| Stage | Exit Condition | On Fail / Blocked |
| --- | --- | --- |
| 0 | Bootstrap complete and `requirements.md` is `Draft` | stay in `0` |
| 1 | `investigation-notes.md` current with scope and evidence | stay in `1` |
| 2 | `requirements.md` is `Plan-ready` or `Refined` with measurable success criteria | stay in `2` |
| 3 | `experiment-plan.md` is current enough to drive implementation and validation | stay in `3` |
| 4 | Implementation for the current iteration is complete and training-ready | local issues: stay in `4`; otherwise classified re-entry |
| 5 | Training and validation evidence closes the current success criteria truthfully | `Blocked` when environment, compute, or data constraints prevent closure without explicit user decision; otherwise classified re-entry |
| 6 | Code review decision is `Pass` and mandatory review checks are satisfied | classified re-entry |
| 7 | Docs are updated or truthful no-impact rationale is recorded | classified re-entry or stay in `7 (Blocked)` for external docs blockers |
| 8 | Handoff summary is complete, explicit user verification is received, ticket moved to `done`, and finalization is complete when applicable | stay in `8` |

## Transition Matrix

| Trigger | Required Transition Path | Gate Result |
| --- | --- | --- |
| Normal forward progression | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Pass |
| Stage 4 failure (`Local Fix`) | stay in `4` | Fail |
| Stage 4 failure (`Plan Impact`) | `1 -> 3 -> 4` | Fail |
| Stage 4 failure (`Requirement Gap`) | `2 -> 3 -> 4` | Fail |
| Stage 4 failure (`Investigation Gap`) | `1 -> 2 -> 3 -> 4` | Fail |
| Stage 4 failure (`Unclear`) | `0 -> 1 -> 2 -> 3 -> 4` | Fail |
| Stage 5 failure (`Local Fix`) | `4 -> 5` | Fail |
| Stage 5 failure (`Plan Impact`) | `1 -> 3 -> 4 -> 5` | Fail |
| Stage 5 failure (`Requirement Gap`) | `2 -> 3 -> 4 -> 5` | Fail |
| Stage 5 failure (`Investigation Gap`) | `1 -> 2 -> 3 -> 4 -> 5` | Fail |
| Stage 5 failure (`Unclear`) | `0 -> 1 -> 2 -> 3 -> 4 -> 5` | Fail |
| Stage 5 blocked by environment, compute, or dataset availability | stay in `5` | Blocked |
| Stage 6 failure (`Local Fix`) | `4 -> 5 -> 6` | Fail |
| Stage 6 failure (`Validation Gap`) | `5 -> 6` | Fail |
| Stage 6 failure (`Plan Impact`) | `1 -> 3 -> 4 -> 5 -> 6` | Fail |
| Stage 6 failure (`Requirement Gap`) | `2 -> 3 -> 4 -> 5 -> 6` | Fail |
| Stage 6 failure (`Investigation Gap`) | `1 -> 2 -> 3 -> 4 -> 5 -> 6` | Fail |
| Stage 6 failure (`Unclear`) | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6` | Fail |
| Stage 7 blocked docs-sync result (`Local Fix`) | `4 -> 5 -> 6 -> 7` | Fail |
| Stage 7 blocked docs-sync result (`Requirement Gap`) | `2 -> 3 -> 4 -> 5 -> 6 -> 7` | Fail |
| Stage 7 blocked docs-sync result (`Investigation Gap`) | `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7` | Fail |
| Stage 7 blocked docs-sync result (`Unclear`) | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7` | Fail |
| Stage 7 blocked by external docs or access issue only | stay in `7` | Blocked |
| Stage 8 awaiting explicit user verification | stay in `8` | In Progress |
| Stage 8 archival or finalization blocked | stay in `8` | Blocked |

## Pre-Edit Checklist

- Current Stage is `4`: `Yes` / `No`
- Code Edit Permission is `Unlocked`: `Yes` / `No`
- Stage 3 gate is `Pass`: `Yes` / `No`
- Required upstream artifacts are current: `Yes` / `No`
- Pre-Edit Checklist Result: `Pass` / `Fail`

If `Fail`, source-code edits are prohibited.

## Re-Entry Declaration

- Trigger Stage (`4` / `5` / `6` / `7`):
- Classification (`Local Fix` / `Validation Gap` / `Plan Impact` / `Requirement Gap` / `Investigation Gap` / `Unclear`):
- Required Return Path:
- Required Upstream Artifacts To Update Before More Source Edits:
- Resume Condition:

Note:
- Recording the re-entry path is not enough; work should resume in the returned stage immediately unless blocked by the environment or waiting on the user.

## Transition Log

| Transition ID | Date | From Stage | To Stage | Reason | Classification | Code Edit Permission After Transition | Evidence Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | YYYY-MM-DD | 0 | 1 | Bootstrap complete, moving to investigation | N/A | Locked | requirements.md, workflow-state.md |

## Process Violation Log

| Date | Violation ID | Violation | Detected At Stage | Action Taken | Cleared |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | V-001 | Source code edited while `Code Edit Permission = Locked` | 3 | Stopped edits, declared re-entry, updated upstream artifacts | No |
