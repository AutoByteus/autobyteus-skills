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
- Create `handoff-summary.md` only when a durable handoff artifact is useful.

## Outputs

- final assistant response, and optionally:
  - `tickets/in-progress/<ticket-name>/handoff-summary.md`
  - `tickets/in-progress/<ticket-name>/release-notes.md`

## Exit Condition

Handoff is complete when the user has a concise summary of what changed, how it was validated, what docs changed, and any remaining risk.

## Next Step

End the workflow.

## Problem Routing

- Do not move a ticket to `tickets/done/` unless the user explicitly asks or confirms completion/verification.
- Do not commit, push, merge, release, deploy, delete branches, or clean worktrees unless the user explicitly asks.
- If a completed ticket is reopened, move it back to `tickets/in-progress/<ticket-name>/` before adding new ticket artifacts.
