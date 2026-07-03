# Handoff Guide

## Purpose

Summarize the completed engineering task clearly.

## Inputs

- implemented changes
- validation evidence
- review result
- docs-sync result or no-impact rationale
- release-note need, if relevant

## Actions

- Summarize delivered scope versus requested scope.
- Summarize important files or areas changed.
- Summarize validation performed and results.
- Summarize review result.
- Summarize docs updated or no-impact rationale.
- Record residual risk or blocked validation.
- Create release notes only when the change is user-facing or the user asks for them.
- Create `handoff-summary.md`.

## Outputs

- final assistant response
- `tickets/in-progress/<ticket-name>/handoff-summary.md`
- `tickets/in-progress/<ticket-name>/release-notes.md` when release notes are required

## Exit Condition

Handoff is complete when the user has a concise summary of what changed, how it was validated, what docs changed, and any remaining risk.

## Next Step

End the workflow.

## Problem Routing

- Do not archive or move ticket artifacts unless the user explicitly asks.
- Do not commit, push, merge, release, deploy, delete branches, or clean worktrees unless the user explicitly asks.
- If completed work is reopened, place any new ticket artifacts under `tickets/in-progress/<ticket-name>/`.
