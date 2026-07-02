# Lightweight Setup Guide

## Purpose

Start the task with minimal useful setup. Do not create process artifacts unless they help the current task.

## Inputs

- user request
- repository instructions
- current workspace and branch state when relevant

## Actions

1. Decide whether durable ticket artifacts are useful.
2. If artifacts are useful, pick a short kebab-case ticket name.
3. Create or reuse `tickets/in-progress/<ticket-name>/`.
4. Capture the initial goal or requirement in `requirements.md` only when durable capture helps.
5. Use the current branch/workspace by default.

## Outputs

- no artifact by default, or
- `tickets/in-progress/<ticket-name>/` with the initial useful artifact(s)

## Exit Condition

Setup is complete when the agent knows where any task artifacts will live, or has deliberately chosen to proceed without ticket artifacts.

## Next Step

Proceed to `stages/01-investigation/stage-guide.md`.

## Problem Routing

- If the user explicitly asks for a branch/worktree, create or use it before continuing.
- If repository instructions require a setup convention, follow the repository convention.
- If setup is blocked by missing user intent, ask one concise clarifying question.
