# Workflow State

Use this file as the mandatory stage-control artifact for the ticket.
Update this file before every stage transition and before any source-code edit.
Stage movement is controlled by this file's Stage Transition Contract + Transition Matrix.

## Current Snapshot

- Ticket:
- Current Stage: `0` / `1` / `2` / `3` / `4` / `5` / `6` / `7` / `8` / `9` / `10`
- Next Stage:
- Code Edit Permission: `Locked` / `Unlocked`
- Active Re-Entry: `No` / `Yes`
- Re-Entry Classification (`Local Fix`/`Validation Gap`/`Design Impact`/`Requirement Gap`/`Unclear`): `N/A`
- Last Transition ID:
- Last Updated:

## Stage 0 Bootstrap Record

- Bootstrap Mode (`Git`/`Non-Git`):
- User-Specified Base Branch:
- Resolved Base Remote:
- Resolved Base Branch:
- Remote Refresh Performed (`Yes`/`No`/`N/A`):
- Remote Refresh Result:
- Ticket Worktree Path:
- Ticket Branch:

Note:
- Fill this record during Stage 0 and keep it current if Stage 0 is reopened.
- For non-git projects, mark git-only fields as `N/A`.

## Stage Gates

| Stage | Gate Status (`Not Started`/`In Progress`/`Pass`/`Fail`/`Blocked`) | Gate Rule Summary | Evidence |
| --- | --- | --- | --- |
| 0 Bootstrap + Draft Requirement | Not Started | Ticket bootstrap complete + if git repo: base branch resolved, remote freshness handled for new bootstrap, dedicated ticket worktree/branch created or reused + `requirements.md` Draft captured |  |
| 1 Investigation + Triage | Not Started | `investigation-notes.md` current + scope triage recorded |  |
| 2 Requirements | Not Started | `requirements.md` is `Design-ready`/`Refined` |  |
| 3 Design Basis | Not Started | Design basis updated for scope (`implementation.md` solution sketch or `proposed-design.md`) |  |
| 4 Future-State Runtime Call Stack | Not Started | `future-state-runtime-call-stack.md` current |  |
| 5 Future-State Runtime Call Stack Review | Not Started | Future-state runtime call stack review `Go Confirmed` (two clean rounds, no blockers/persisted updates/new use cases) |  |
| 6 Implementation | Not Started | Plan/progress current + source + unit/integration verification complete + no backward-compat/legacy retention + ownership-driven dependencies preserved + touched-file placement preserved/corrected |  |
| 7 API/E2E Testing | Not Started | API/E2E test implementation complete + acceptance-criteria and spine scenario gates complete |  |
| 8 Code Review | Not Started | Code review gate `Pass`/`Fail` recorded + all changed source files `<=500` effective non-empty lines + `>220` delta-gate assessments recorded + data-flow spine inventory/ownership/support-structure + existing-capability reuse + reusable-owned-structure extraction + repeated-coordination ownership + empty-indirection + scope-appropriate separation of concerns + file placement within the correct subsystem and folder, with any optional module grouping justified + flat-vs-over-split layout judgment + interface/API/query/command/service-method boundary clarity + naming-to-responsibility alignment + duplication/patch-on-patch complexity control + test quality + test maintainability + validation-evidence sufficiency + no-backward-compat/no-legacy checks satisfied for `Pass` |  |
| 9 Docs Sync | Not Started | Docs updated or no-impact rationale recorded |  |
| 10 Handoff / Ticket State | Not Started | Final handoff ready + explicit user verification received + ticket moved to `done` + git finalization/release complete when git repo + ticket state decision recorded |  |

## Stage Transition Contract (Quick Reference)

| Stage | Exit Condition | On Fail/Blocked |
| --- | --- | --- |
| 0 | Bootstrap complete, base-branch/worktree decision recorded, and `requirements.md` is `Draft` | stay in `0` |
| 1 | `investigation-notes.md` current + scope triage recorded | stay in `1` |
| 2 | `requirements.md` is `Design-ready`/`Refined` | stay in `2` |
| 3 | Design basis current for scope | stay in `3` |
| 4 | Future-state runtime call stack current | stay in `4` |
| 5 | Future-state runtime call stack review `Go Confirmed` (two clean rounds with no blockers/no required persisted artifact updates/no newly discovered use cases) | classified re-entry then rerun (`Design Impact`: `3 -> 4 -> 5`, `Requirement Gap`: `2 -> 3 -> 4 -> 5`, `Unclear`: `1 -> 2 -> 3 -> 4 -> 5`) |
| 6 | Source + required unit/integration verification complete, no backward-compatibility/legacy-retention paths remain in scope, ownership-driven dependencies remain valid (no new unjustified cycles/tight coupling), and touched files sit in the correct folder under the correct owning subsystem | local issues: stay in `6`; otherwise classified re-entry (`Design Impact`: `1 -> 3 -> 4 -> 5 -> 6`, `Requirement Gap`: `2 -> 3 -> 4 -> 5 -> 6`, `Unclear`: `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6`) |
| 7 | API/E2E gate closes all executable mapped acceptance criteria (`Passed` or explicit user `Waived`) and all relevant executable spines have passing scenario evidence (or explicit `N/A` rationale) | `Blocked` on infeasible/no waiver; otherwise classified re-entry |
| 8 | Code review gate decision is `Pass` with all changed source files `<=500` effective non-empty lines, required `>220` delta-gate assessments recorded, and data-flow spine inventory/ownership/support-structure + existing-capability reuse + reusable-owned-structure extraction + repeated-coordination ownership + empty-indirection + scope-appropriate separation of concerns + file placement within the correct subsystem and folder, with any optional module grouping justified + flat-vs-over-split layout judgment + interface/API/query/command/service-method boundary clarity + naming-to-responsibility alignment + duplication/patch-on-patch complexity control + test quality + test maintainability + validation-evidence sufficiency + no-backward-compat/no-legacy checks satisfied | classified re-entry then rerun |
| 9 | Docs updated or no-impact rationale recorded | stay in `9` |
| 10 | Final handoff is complete, explicit user completion/verification is received, the ticket is moved to `tickets/done/<ticket-name>/`, and, when git repo, ticket-branch commit/push + latest-personal-branch update + merge + push + release are complete | stay in `10` |

## Transition Matrix (Reference)

| Trigger | Required Transition Path | Gate Result |
| --- | --- | --- |
| Normal forward progression | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10` | Pass |
| Stage 5 blocker (`Design Impact`) | `3 -> 4 -> 5` | Fail |
| Stage 5 blocker (`Requirement Gap`) | `2 -> 3 -> 4 -> 5` | Fail |
| Stage 5 blocker (`Unclear`) | `1 -> 2 -> 3 -> 4 -> 5` | Fail |
| Stage 6 failure (`Local Fix`) | stay in `6` | Fail |
| Stage 6 failure (`Design Impact`) | `1 -> 3 -> 4 -> 5 -> 6` | Fail |
| Stage 6 failure (`Requirement Gap`) | `2 -> 3 -> 4 -> 5 -> 6` | Fail |
| Stage 6 failure (`Unclear`/cross-cutting root cause) | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6` | Fail |
| Stage 7 failure (`Local Fix`) | `6 -> 7` | Fail |
| Stage 7 failure (`Design Impact`) | `1 -> 3 -> 4 -> 5 -> 6 -> 7` | Fail |
| Stage 7 failure (`Requirement Gap`) | `2 -> 3 -> 4 -> 5 -> 6 -> 7` | Fail |
| Stage 7 failure (`Unclear`/cross-cutting root cause) | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7` | Fail |
| Stage 7 infeasible criteria without explicit user waiver | stay in `7` | Blocked |
| Stage 8 failure (`Local Fix`) | `6 -> 7 -> 8` | Fail |
| Stage 8 failure (`Validation Gap`) | `7 -> 8` | Fail |
| Stage 8 failure (`Design Impact`) | `1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Fail |
| Stage 8 failure (`Requirement Gap`) | `2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Fail |
| Stage 8 failure (`Unclear`/cross-cutting root cause) | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Fail |
| Stage 10 awaiting explicit user verification | stay in `10` | In Progress |
| Stage 10 archival/repository finalization blocked | stay in `10` | Blocked |

Note:
- In re-entry paths, Stage 0 means re-open bootstrap controls in the same ticket/worktree (`workflow-state.md`, lock state, artifact baselines); do not create a new ticket folder.
- For Stage 5 failures, record classified re-entry first; then persist artifact updates in the returned upstream stage before running the next Stage 5 round.
- Stage 10 can remain `In Progress` while waiting for explicit user completion/verification before moving the ticket to `done` and starting repository finalization.

## Pre-Edit Checklist (Stage 6 Source-Code Edits)

- Current Stage is `6`: `Yes` / `No`
- Code Edit Permission is `Unlocked`: `Yes` / `No`
- Stage 5 gate is `Go Confirmed`: `Yes` / `No`
- Required upstream artifacts are current: `Yes` / `No`
- Pre-Edit Checklist Result: `Pass` / `Fail`
- If `Fail`, source code edits are prohibited.

## Re-Entry Declaration

- Trigger Stage (`5`/`6`/`7`/`8`):
- Classification (`Local Fix`/`Validation Gap`/`Design Impact`/`Requirement Gap`/`Unclear`):
- Required Return Path:
- Required Upstream Artifacts To Update Before Code Edits:
- Resume Condition:

Note:
- Stage 5 re-entry normally uses `Design Impact` / `Requirement Gap` / `Unclear` only (not `Local Fix`).
- Stage 6 re-entry uses `Local Fix` (stay in `6`) or non-local classified return path (`Design Impact`/`Requirement Gap`/`Unclear`) before further source edits.
- Stage 8 may use `Validation Gap` when the main issue is insufficient Stage 7 coverage/evidence rather than code or design drift.

## Transition Log (Append-Only)

| Transition ID | Date | From Stage | To Stage | Reason | Classification | Code Edit Permission After Transition | Evidence Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | YYYY-MM-DD | 0 | 1 | Bootstrap complete, moving to investigation | N/A | Locked | requirements.md, workflow-state.md |

## Audible Notification Log (Optional Tracking)

| Date | Trigger Type (`Transition`/`Gate`/`Re-entry`/`LockChange`) | Summary Spoken | Speak Tool Result (`Success`/`Failed`) | Fallback Text Logged |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Transition | Stage 0 complete, moving to Stage 1 investigation. | Success | N/A |

## Process Violation Log

| Date | Violation ID | Violation | Detected At Stage | Action Taken | Cleared |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | V-001 | Source code edited while `Code Edit Permission = Locked` | 3 | Stopped edits, declared re-entry, updated upstream artifacts | No |
