# Stage 0 Bootstrap Checklist

Run this stage before investigation.

## Mandatory Sequence

1. Create or reuse `tickets/in-progress/<ticket-name>/`.
2. If the project is a git repository:
   - resolve the base branch,
   - refresh tracked remote refs before new bootstrap,
   - create or reuse a dedicated worktree,
   - create or reuse `codex/<ticket-name>`.
3. Create `tickets/in-progress/<ticket-name>/requirements.md` with status `Draft`.
4. Create `tickets/in-progress/<ticket-name>/workflow-state.md` from `shared/workflow-state-template.md`.
5. Set:
   - `Current Stage = 0`
   - `Code Edit Permission = Locked`
   - Stage 0 gate to `In Progress`
6. Fill the Stage 0 bootstrap record.

## Exit Gate

Leave Stage 0 only when:
- ticket context exists,
- `requirements.md` exists with status `Draft`,
- `workflow-state.md` exists and records bootstrap details.

## Notes

- If bootstrap cannot resolve the base branch or refresh remote state when required, keep Stage 0 `Blocked`.
- If the environment is non-git, mark git-only fields as `N/A` and continue.
