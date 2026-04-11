# Stage 8 Handoff Guide

The handoff should make the current iteration easy to continue without rediscovery.

## Include

- what changed
- what was actually run
- the best current result
- what passed, failed, or remained inconclusive
- the exact dataset manifest, tokenizer or template version, and evaluation settings behind the best result
- important artifacts and where they live
- next experiments or next engineering actions
- explicit remaining risks

## Finalization Rules

- wait for explicit user verification before moving the ticket to `done`
- if the project is a git repository and the user has verified completion, perform repository finalization using the recorded bootstrap target unless the user overrides it
- if the task is reopened later, move the ticket back to `tickets/in-progress/<ticket-name>/`
