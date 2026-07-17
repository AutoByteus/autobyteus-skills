# Handoff Guide

## Purpose

Summarize the completed engineering task clearly.
When the user explicitly asks for repository finalization, release, publication, or deployment, ensure the ticket branch is based on the latest tracked remote base before finalizing or deploying.

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
- If the user explicitly asks for repository finalization, release, publication, or deployment:
  - refresh tracked remote refs for the base branch recorded during bootstrap,
  - check whether the latest tracked remote base has advanced beyond the ticket branch's current integration point,
  - integrate the latest tracked remote base into the ticket branch before finalization/deployment work; use the repository's documented integration method, defaulting to merge unless project policy requires rebase,
  - if new base commits were integrated, rerun at least one relevant executable check or smoke path against the integrated state and record the command/result,
  - if the branch was already current, record the checked remote base reference and why no rerun was needed,
  - if integration conflicts, changes effective behavior, or post-integration checks fail, keep handoff blocked and route the issue instead of finalizing or deploying a stale state.
- If user verification happened before a later base-branch refresh, do not blindly finalize the older verified state. Bring the ticket branch current, rerun required checks, update affected docs or handoff artifacts, and obtain renewed verification when the user-facing handoff state materially changes.
- Create release notes only when the change is user-facing or the user asks for them.
- Create `handoff-summary.md` after any required latest-base integration refresh so the handoff reflects the current integrated branch state.

## Outputs

- final assistant response
- `tickets/in-progress/<ticket-name>/handoff-summary.md`
- `tickets/in-progress/<ticket-name>/release-notes.md` when release notes are required
- latest-base integration/finalization readiness evidence when repository finalization, release, publication, or deployment is explicitly requested

## Exit Condition

Handoff is complete when the user has a concise summary of what changed, how it was validated, what docs changed, and any remaining risk.

## Next Step

End the workflow.

## Problem Routing

- Do not archive or move ticket artifacts unless the user explicitly asks.
- Do not commit, push, merge, release, deploy, delete branches, or clean worktrees unless the user explicitly asks. Once the user asks for repository finalization, release, publication, or deployment, the latest-base integration refresh above is mandatory before that work proceeds.
- If completed work is reopened, place any new ticket artifacts under `tickets/in-progress/<ticket-name>/`.
