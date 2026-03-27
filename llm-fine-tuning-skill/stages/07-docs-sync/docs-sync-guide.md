# Stage 7 Docs Sync Guide

Only sync docs that can now be stated truthfully from the current evidence.

## Common Targets

- training or evaluation commands
- config assumptions
- dataset or split expectations
- best-known run summary
- checkpoint handling notes
- reproduction steps
- caveats and limitations

## Rules

- do not publish optimistic claims that Stage 5 did not support
- if docs cannot yet be made truthful because implementation or evidence is still wrong, classify re-entry instead of writing around the problem
- if no durable docs are affected, record a no-impact rationale explicitly

## Exit Gate

Leave Stage 7 only when `docs-sync.md` records what changed, where it changed, and why the resulting docs are now truthful.
