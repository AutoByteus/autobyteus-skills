# Workflow State

Mandatory stage-control artifact for the ticket.
Update before every stage transition and before any source-code edit.
Use `shared/workflow-control.md` for the transition contract, transition matrix, workflow-state rules, and re-entry rules.

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
- Default Finalization Target Remote:
- Default Finalization Target Branch:
- Remote Refresh Performed (`Yes`/`No`/`N/A`):
- Remote Refresh Result:
- Ticket Worktree Path:
- Ticket Branch:

Note:
- Fill this record during Stage 0 and keep it current if Stage 0 is reopened.
- Unless the user explicitly overrides Stage 10 later, the default finalization target should match the resolved base remote/branch recorded here.
- For non-git projects, mark git-only fields as `N/A`.

## Stage Gates

| Stage | Gate Status (`Not Started`/`In Progress`/`Pass`/`Fail`/`Blocked`) | Gate Rule Summary | Evidence |
| --- | --- | --- | --- |
| 0 Bootstrap + Draft Requirement | Not Started | Ticket bootstrap complete + if git repo: base branch resolved, remote freshness handled for new bootstrap, dedicated ticket worktree/branch created or reused + `requirements.md` Draft captured |  |
| 1 Investigation + Triage | Not Started | `investigation-notes.md` current + scope triage recorded |  |
| 2 Requirements | Not Started | `requirements.md` is `Design-ready`/`Refined` |  |
| 3 Design Basis | Not Started | Design basis updated for scope (`implementation.md` solution sketch or `proposed-design.md`) |  |
| 4 Future-State Runtime Call Stack | Not Started | `future-state-runtime-call-stack.md` current |  |
| 5 Future-State Runtime Call Stack Review | Not Started | Future-state runtime call stack review `Go Confirmed` (two clean rounds, no blockers/persisted updates/new use cases) + spine span sufficiency passes for all in-scope use cases |  |
| 6 Implementation | Not Started | `implementation.md` current + source + unit/integration verification complete + Stage 6 structural checks satisfied |  |
| 7 API/E2E + Executable Validation | Not Started | executable validation implementation complete + acceptance-criteria and spine scenario gates complete |  |
| 8 Code Review | Not Started | code review decision recorded + scorecard complete + mandatory Stage 8 review checks satisfied |  |
| 9 Docs Sync | Not Started | `docs-sync.md` current + docs updated or no-impact rationale recorded |  |
| 10 Handoff / Ticket State | Not Started | `handoff-summary.md` current + explicit user verification received + ticket moved to `done` + repository finalization into resolved target branch complete when git repo + any applicable release/publication/deployment step completed or explicitly recorded as not required + required post-finalization worktree/branch cleanup complete when applicable + ticket state decision recorded |  |

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
- Transition/Re-entry completion rule: recording the path is not enough; resume work immediately and treat re-entry as incomplete until work has actually resumed in the returned stage.
- Default resume condition: `Resume immediately into the first returned stage, without waiting for another user message, unless blocked or waiting on an explicit user-only gate. Re-entry is not complete until work has actually resumed in that returned stage.`
- Stage 5 re-entry normally uses `Design Impact` / `Requirement Gap` / `Unclear` only (not `Local Fix`).
- Stage 6 re-entry uses `Local Fix` (stay in `6`) or non-local classified return path (`Design Impact`/`Requirement Gap`/`Unclear`) before further source edits.
- Stage 9 blocked docs sync uses `Local Fix` / `Requirement Gap` / `Unclear` when docs cannot yet be made truthful; stay in `9` only for external docs blockers that do not require upstream artifact changes.
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
