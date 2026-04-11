# Stage 1 Investigation Guide

Investigation is any activity needed to build accurate technical understanding before planning or implementation.
In this workflow, investigation is first-class and often deeper than implementation.

## Investigation Can Include

- reading local code, configs, scripts, logs, checkpoints, dataset manifests, and data loaders
- tracing current fine-tuning, evaluation, and inference entrypoints
- inspecting prompt or chat templates, tokenizer configuration, truncation, packing, and label masking behavior
- inspecting dataset provenance, schema normalization, filtering, deduplication, split assumptions, and contamination risks
- reading open-source implementations, papers, or framework internals
- checking model cards, method references, or official documentation when needed
- running probes, reproductions, sanity checks, and small measurement scripts

## Artifact Standard

- Update `tickets/in-progress/<ticket-name>/investigation-notes.md` in place.
- Treat it as a durable dossier, not a short recap.
- Keep concrete evidence:
  - file paths,
  - functions,
  - commands,
  - URLs,
  - search queries,
  - relevant logs, examples, or metric excerpts,
  - implications for later stages.

## Required Contents

- task framing, goals, and main unknowns
- scope triage (`Small` / `Medium` / `Large`) with rationale
- exact sources consulted
- current fine-tuning, evaluation, and inference entrypoints
- current base model, update strategy, objective type, data flow, and eval flow as understood
- current tokenizer, prompt-template, label-masking, and sequence-boundary behavior
- relevant paper, framework, or reference-implementation findings that influence the plan
- dataset provenance, schema, split, filtering, and contamination understanding
- baseline or prior-result understanding
- constraints:
  - compute,
  - memory,
  - runtime,
  - dataset availability,
  - evaluator or judge availability,
  - reproducibility limitations
- design and planning implications
- open questions that still matter to Stage 2 or Stage 3

## Investigation Rules

- Do not keep important findings only in memory.
- Do not replace detailed evidence with a thin narrative summary.
- If external sources are used, record the exact source and the concrete fact taken from it.
- If later stages expose missing understanding, reopen Stage 1 and append the new evidence.

## Exit Gate

Leave Stage 1 only when `investigation-notes.md` is detailed enough that Stage 2 and Stage 3 can reuse it directly.
