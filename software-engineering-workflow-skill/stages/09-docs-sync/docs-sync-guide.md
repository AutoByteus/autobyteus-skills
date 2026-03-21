# Stage 9 Docs Sync Guide

Use this guide after Stage 7 and Stage 8 are complete.

## Why This Stage Exists

- ticket artifacts explain how one change was delivered, but they are not the durable source of truth
- long-lived project understanding should survive after the ticket is archived
- Stage 9 promotes stable design, runtime, ownership, and operational knowledge into long-lived docs
- this stage is important because future engineers should be able to understand the current system from project docs without reconstructing history from old tickets

## Canonical Policy

- long-lived project truth belongs in project docs such as `docs/` and `ARCHITECTURE.md`
- ticket artifacts remain task-local records, not the permanent source of truth

## Stage 9 Artifact

- create/update `tickets/in-progress/<ticket-name>/docs-sync.md`
- use it to record:
  - which long-lived docs were reviewed,
  - which docs were updated,
  - what durable design/runtime knowledge was promoted,
  - what was removed or replaced,
  - or why there is truly no docs impact

## Update When Changed

- subsystems, files, optional module groupings when relevant, or public interfaces
- runtime flows or operational behavior
- renamed, moved, or removed components
- testing or operating procedures that changed with the feature

## What Good Stage 9 Output Should Explain

- what changed
- why it changed
- what the current architecture/runtime shape is now
- which boundaries, subsystems, files, or APIs are now important to understand
- which old components, paths, or concepts were removed or replaced
- which operational or validation expectations changed

## Required Output

- update existing docs in place when they already cover the feature
- create missing docs only when no current doc covers the functionality
- record `Updated` or `No impact` with rationale in `docs-sync.md`
- avoid duplicate overlapping docs when one canonical doc can be updated in place

## Stage 9 Rules

- do not skip docs sync just because tests passed
- if there is no docs impact, say so explicitly
- do not treat this as cosmetic cleanup; docs must explain the codebase as it now exists
- when ticket-local design knowledge should become durable project knowledge, promote it into `docs/` or other canonical docs instead of leaving it only under `tickets/`
- docs sync is complete only when the documentation matches the final implemented behavior
