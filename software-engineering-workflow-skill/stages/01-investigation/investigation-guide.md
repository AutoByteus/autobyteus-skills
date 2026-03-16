# Stage 1 Investigation Guide

Investigation is any activity needed to build accurate understanding and verify assumptions.

## Investigation Can Include

- reading code, docs, configs, schemas, logs, and data
- running commands, reproductions, probes, or traces
- writing small scripts or focused tests
- checking APIs, external references, or internet sources when needed

## Minimum Outputs

- `tickets/in-progress/<ticket-name>/investigation-notes.md` updated in place
- current entrypoints and boundaries identified
- touched owners, modules, and likely file-placement concerns identified
- constraints, unknowns, and design implications recorded
- scope triage (`Small` / `Medium` / `Large`) recorded with rationale

## Investigation Rules

- Do not keep results only in memory.
- If later stages expose unclear or cross-cutting issues, reopen Stage 1 and append new evidence.
- Investigation should reduce uncertainty enough for `requirements.md` to become `Design-ready`.
