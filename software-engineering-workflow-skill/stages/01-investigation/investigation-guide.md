# Stage 1 Investigation Guide

Investigation is any activity needed to build accurate understanding and verify assumptions.

## Investigation Can Include

- reading code, docs, configs, schemas, logs, and data
- running commands, reproductions, probes, or traces
- writing small scripts or focused tests
- checking APIs, external references, or internet sources when needed

## Artifact Standard

- Update `tickets/in-progress/<ticket-name>/investigation-notes.md` in place.
- Treat `investigation-notes.md` as a durable investigation dossier, not a brief recap.
- Write enough detail that later stages can reuse the findings directly instead of repeating the same search/research work unless the facts have changed.
- Use short synthesis sections for readability, but keep the concrete evidence paths, URLs, queries, commands, findings, and implications in the artifact.

## Required Contents

- investigation goals, questions, or hypotheses
- scope triage (`Small` / `Medium` / `Large`) with rationale
- exact sources consulted:
  - local file paths
  - URLs / external docs
  - commands run
  - search queries used when material
- current entrypoints, execution boundaries, owners, modules, folders, and likely file-placement concerns
- constraints, unknowns, and design implications
- enough codebase/runtime/API detail that later stages do not need to rediscover the same facts from scratch

## Investigation Rules

- Do not keep results only in memory.
- Do not collapse detailed evidence into a thin summary if later stages would need that detail again.
- When internet or external documentation research is used, record the exact source and the specific fact or constraint taken from it.
- When codebase search is used, record the exact files, symbols, or paths that matter, not only the conclusion.
- When commands, probes, traces, or reproductions are used, record what was run and the result that mattered.
- If later stages expose unclear or cross-cutting issues, reopen Stage 1 and append new evidence instead of replacing earlier findings silently.
- Investigation should reduce uncertainty enough for `requirements.md` to become `Design-ready`.
