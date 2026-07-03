# Docs Sync Guide

## Purpose

Update long-lived project documentation when the delivered behavior changes what future readers need to know.

Ticket artifacts explain one change, but they are not the durable source of truth.

## Inputs

- implemented changes
- validation and review results
- existing docs such as `docs/`, README files, and `ARCHITECTURE.md`
- ticket artifacts when they contain durable design or runtime knowledge

## Actions

- Review existing canonical docs that might be affected.
- Update existing docs in place when possible.
- Create a new doc only when no current doc owns the topic.
- Promote stable behavior, design, runtime, ownership, validation, or operational knowledge into long-lived docs.
- Avoid duplicate overlapping docs.
- Record no-impact rationale when docs do not need changes.

Update docs when the change affects:

- public or developer-facing behavior
- subsystem boundaries, file ownership, or architecture
- runtime flows or operational behavior
- renamed, moved, or removed components
- testing, deployment, or support procedures

## Outputs

- updated long-lived docs when needed
- `tickets/in-progress/<ticket-name>/docs-sync.md` with update details or no-impact rationale

## Exit Condition

Docs sync is complete when long-lived docs are updated where needed, or a clear no-impact rationale is recorded.

## Next Step

Proceed to `stages/08-handoff/stage-guide.md`.

## Problem Routing

- If docs reveal final implementation is wrong or incomplete, return to implementation.
- If intended behavior is missing or ambiguous, return to requirements.
- If ownership/API/placement is unclear, return to design.
- If root cause is unclear, return to investigation.
