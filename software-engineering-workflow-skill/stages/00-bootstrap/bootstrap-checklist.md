# Stage 0 Bootstrap Checklist

Use this checklist at the start of every ticket before investigation begins.

## Required Order

1. Create or reuse `tickets/in-progress/<ticket-name>/`.
2. If the project is a git repository, resolve the bootstrap base branch:
   - use the explicit user-specified base branch when provided,
   - otherwise infer the tracked remote default/integration branch with highest confidence.
3. If the project is a git repository and a new ticket worktree/branch is needed, refresh tracked remote refs first.
4. If the project is a git repository, create or reuse a dedicated ticket worktree for `codex/<ticket-name>`; when creating a new ticket branch, create it from the latest tracked remote state of the resolved base branch.
5. Create or update `tickets/in-progress/<ticket-name>/workflow-state.md` from `shared/workflow-state-template.md` and fill the `Stage 0 Bootstrap Record`.
6. Set `Current Stage = 0` and `Code Edit Permission = Locked`.
7. Create or update `tickets/in-progress/<ticket-name>/requirements.md` with status `Draft`.

## Bootstrap Rules

- Do not start deep investigation before the bootstrap sequence is physically written.
- Reuse the existing ticket folder and branch/worktree when they already match the ticket.
- If the ticket is being reopened from `tickets/done/<ticket-name>/`, move it back to `tickets/in-progress/<ticket-name>/` before any new artifact updates.
- If the user specifies a base branch, always use the latest tracked remote state of that branch instead of a stale local branch.
- Do not create a new ticket branch/worktree from a stale local base; refresh tracked remote refs first.
- Capture the draft requirement from user input or bug evidence first; do not wait for perfect understanding.
- If remote refresh, base-branch resolution, or ticket-worktree creation fails, keep Stage 0 blocked and record the blocker.
- If the repo is not under git, still create the ticket folder and stage artifacts in the same order.

## Minimum Stage 0 Evidence

- ticket path exists
- git/non-git bootstrap decision recorded
- if git repo: base remote/base branch recorded
- if git repo: worktree path + ticket branch recorded
- if git repo and a new ticket worktree/branch was created: remote refresh result recorded
- `workflow-state.md` initialized
- `requirements.md` exists with status `Draft`
