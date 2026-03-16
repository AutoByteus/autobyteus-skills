# Stage 0 Bootstrap Checklist

Use this checklist at the start of every ticket before investigation begins.

## Required Order

1. Create or reuse `tickets/in-progress/<ticket-name>/`.
2. If the project is a git repository, create or switch to `codex/<ticket-name>`.
3. Create or update `tickets/in-progress/<ticket-name>/workflow-state.md` from `shared/workflow-state-template.md`.
4. Set `Current Stage = 0` and `Code Edit Permission = Locked`.
5. Create or update `tickets/in-progress/<ticket-name>/requirements.md` with status `Draft`.

## Bootstrap Rules

- Do not start deep investigation before the bootstrap sequence is physically written.
- Reuse the existing ticket folder and branch/worktree when they already match the ticket.
- Capture the draft requirement from user input or bug evidence first; do not wait for perfect understanding.
- If the repo is not under git, still create the ticket folder and stage artifacts in the same order.

## Minimum Stage 0 Evidence

- ticket path exists
- branch/worktree decision recorded
- `workflow-state.md` initialized
- `requirements.md` exists with status `Draft`
