# Stage 0 Bootstrap

## Purpose

Create or reuse the ticket working context before investigation starts.
This stage establishes the ticket folder, bootstrap branch/worktree decision, initial `requirements.md`, and the initial `workflow-state.md` control record.

## Enter This Stage When

- work is starting for a new ticket
- a later-stage `Unclear` path requires reopening Stage 0 controls in the same ticket context
- the ticket is being reopened from `tickets/done/`

## Stage-Owned Outputs

- `tickets/in-progress/<ticket-name>/workflow-state.md`
- `tickets/in-progress/<ticket-name>/requirements.md` with status `Draft`
- `Stage 0 Bootstrap Record` filled in `workflow-state.md`

## Exit Gate

Leave Stage 0 only when bootstrap is complete, the base branch/worktree decision is recorded, and `requirements.md` physically exists with status `Draft`.

## Local Files

- `bootstrap-checklist.md`: detailed bootstrap order and minimum evidence
