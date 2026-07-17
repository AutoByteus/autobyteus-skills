# Bootstrap Guide

## Purpose

Start the task by creating durable ticket context and, in git repositories, an isolated task worktree.

## Inputs

- user request
- repository instructions
- current workspace and branch state when relevant

## Actions

1. Pick a short kebab-case ticket name derived from the task description.
2. Create or reuse `tickets/in-progress/<ticket-name>/`.
3. Check whether the current workspace is inside a git repository: `git rev-parse --show-toplevel 2>/dev/null` or `git status --short 2>/dev/null`.
4. **If the workspace is a git repository**, create or reuse a dedicated task branch/worktree before writing stage artifacts. Start from the latest tracked remote state of the resolved base branch.
5. **If the workspace is NOT a git repository** (e.g. a temp workspace, a standalone output directory), skip git branching. The ticket folder under the project or workspace root is sufficient for durable artifact isolation.
6. Create or update `tickets/in-progress/<ticket-name>/requirements.md` with the initial goal or requirement.

## Outputs

- `tickets/in-progress/<ticket-name>/`
- `tickets/in-progress/<ticket-name>/requirements.md`
- dedicated task branch/worktree when the workspace is a git repository

## Exit Condition

Setup is complete when the ticket folder exists, `requirements.md` captures the initial request, and the git worktree/branch decision is settled (either branch created and checked out, or non-repository workspace acknowledged).

## Next Step

Proceed to `stages/01-investigation/stage-guide.md`.

## Problem Routing

- If a git repository cannot create or reuse a dedicated branch/worktree, record the blocker in `requirements.md` and ask one concise question before continuing.
- If repository instructions require a setup convention, follow the repository convention.
- If setup is blocked by missing user intent, ask one concise clarifying question.
- In a non-git workspace, proceed directly to the next stage without branching — the ticket folder provides sufficient artifact structure.
