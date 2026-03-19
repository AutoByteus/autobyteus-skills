# Stage 9 Docs Sync Guide

Use this guide after Stage 7 and Stage 8 are complete.

## Canonical Policy

- long-lived project truth belongs in project docs such as `docs/` and `ARCHITECTURE.md`
- ticket artifacts remain task-local records, not the permanent source of truth

## Update When Changed

- subsystems, files, optional module groupings when relevant, or public interfaces
- runtime flows or operational behavior
- renamed, moved, or removed components
- testing or operating procedures that changed with the feature

## Required Output

- update existing docs in place when they already cover the feature
- create missing docs only when no current doc covers the functionality
- record `Updated` or `No impact` with rationale in `implementation-progress.md`

## Stage 9 Rules

- do not skip docs sync just because tests passed
- if there is no docs impact, say so explicitly
- docs sync is complete only when the documentation matches the final implemented behavior
