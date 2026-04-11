---
name: llm-fine-tuning-skill
description: "Run a staged LLM fine-tuning workflow from bootstrap through investigation, requirements and success criteria, implementation planning, implementation plus data preparation, training and validation, code review, docs sync, and handoff. Use for supervised fine-tuning, preference tuning, reinforcement-style training, and other LLM adaptation work with reproducible empirical validation."
---

# LLM Fine-Tuning Skill

## Overview

Run a staged workflow for LLM fine-tuning work where the hard parts are usually investigation quality, implementation planning, data preparation, prompt or chat formatting, tokenizer correctness, and empirical validation rather than large implementation volume.
Use this skill for tasks such as supervised fine-tuning, preference tuning, reinforcement-style training, domain adaptation, data-format changes, eval-set changes, benchmark comparisons, and reproducible validation work.
This skill is method-agnostic. It can be used for adapter-based, quantized, or full-parameter tuning, but it should force the workflow to make the chosen objective and update strategy explicit instead of assuming one method.

This workflow is stage-gated.
Do not batch-generate all artifacts by default.
Advance only when the current stage gate is satisfied or a classified re-entry path says otherwise.

## Skill Layout

- `SKILL.md` is the workflow router.
- `shared/workflow-state-template.md` is the canonical stage-control artifact.
- `stages/` stores stage-owned guides and templates:
  - `stages/00-bootstrap/`
  - `stages/01-investigation/`
  - `stages/02-requirements-and-success-criteria/`
  - `stages/03-implementation-plan/`
  - `stages/04-implementation/`
  - `stages/05-training-and-validation/`
  - `stages/06-code-review/`
  - `stages/07-docs-sync/`
  - `stages/08-handoff/`

## Workflow

### Ticket Folder Convention

- For each task, create or reuse one ticket folder under `tickets/in-progress/`.
- Write active workflow artifacts in `tickets/in-progress/<ticket-name>/`.
- Archive completed tickets in `tickets/done/<ticket-name>/`.
- Move a ticket to `done` only after explicit user verification or explicit user instruction.
- If the user reopens a completed task, move the ticket back to `tickets/in-progress/<ticket-name>/` before new updates.

### Bootstrap And Worktree Setup

- Before investigation, create or reuse the ticket folder and write `requirements.md` with status `Draft`.
- If the project is a git repository:
  - resolve the base branch from explicit user instruction when provided, otherwise infer the tracked remote default or integration branch with highest confidence,
  - refresh tracked remote refs before creating a new ticket branch or worktree,
  - create or reuse a dedicated ticket worktree,
  - create or reuse a ticket branch named `codex/<ticket-name>`.
- If the environment is not a git repository, continue without worktree setup and still enforce the ticket-folder and `Draft` requirement capture.

### Workflow State File

- Create and maintain `tickets/in-progress/<ticket-name>/workflow-state.md` as the mandatory stage-control artifact.
- Initialize it during Stage 0 with:
  - `Current Stage = 0`
  - `Code Edit Permission = Locked`
  - the bootstrap record filled in
  - stage gates set to `Not Started` or `In Progress`
- Update `workflow-state.md` on every stage transition, gate decision, and re-entry declaration.

### Source-Edit Lock Rule

- No source-code edits are allowed unless `workflow-state.md` shows:
  - `Current Stage = 4`
  - `Code Edit Permission = Unlocked`
- Default state is `Locked`.
- Unlock source-code edits only after Stage 3 `Implementation Plan` is current enough to drive implementation.
- If Stage 5, 6, or 7 fails and a re-entry is required, lock source edits before taking the return path.

### Canonical Flow

- Forward path: `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8`
- Re-entry is mandatory when failures show the issue is upstream of the current stage.
- Do not stop after recording a re-entry path; resume work in the returned stage immediately unless blocked by the environment or waiting for an explicit user-only decision.

## Stage Router

### 0) Bootstrap

- Primary files:
  - `stages/00-bootstrap/README.md`
  - `stages/00-bootstrap/bootstrap-checklist.md`
- Required outcome:
  - ticket context exists,
  - `requirements.md` exists with status `Draft`,
  - `workflow-state.md` exists and records bootstrap details.

### 1) Investigation

- Primary files:
  - `stages/01-investigation/README.md`
  - `stages/01-investigation/investigation-guide.md`
  - `stages/01-investigation/investigation-notes-template.md`
- Investigation is first-class in this workflow.
- Investigation can include:
  - reading local code, configs, datasets, logs, checkpoints, and eval harnesses,
  - reading tokenizer, prompt-template, and response-formatting logic,
  - reading open-source fine-tuning repositories, framework internals, and relevant documentation,
  - checking papers, model cards, or fine-tuning references when needed,
  - running probes, small scripts, reproductions, and data sanity checks.
- Required outcome:
  - `investigation-notes.md` is a durable dossier with concrete evidence,
  - the task is triaged for scope and uncertainty,
  - later stages can reuse the findings directly.

### 2) Requirements & Success Criteria

- Primary files:
  - `stages/02-requirements-and-success-criteria/README.md`
  - `stages/02-requirements-and-success-criteria/requirements-success-criteria-guide.md`
- Required outcome:
  - `requirements.md` moves from `Draft` to `Plan-ready` or `Refined`,
  - task definition, baseline, measurable or rubric-defined outcomes, constraints, and success criteria are explicit,
  - the planned validation gate can measure pass, fail, or inconclusive results truthfully.

### 3) Implementation Plan

- Primary files:
  - `stages/03-implementation-plan/README.md`
  - `stages/03-implementation-plan/implementation-plan-template.md`
- This stage replaces heavy software-architecture runtime modeling with a concrete implementation plan.
- Focus on:
  - dataset sourcing, curation, filtering, split assumptions, and data-preparation design,
  - prompt or chat template design,
  - tokenizer, special-token, masking, truncation, and packing behavior,
  - base model choice, objective type, and parameter-update strategy,
  - optimizer, scheduler, and fine-tuning recipe,
  - evaluation protocol, held-out prompt suites, inference settings, and sample-based validation,
  - objective-specific needs such as preference pairs, reward signals, or trajectory handling when applicable,
  - comparison matrix or ablations,
  - reproducibility plan,
  - implementation work items.
- Required outcome:
  - `implementation-plan.md` is current and can drive Stage 4 implementation and Stage 5 training or evaluation.

### 4) Implementation & Data Preparation

- Primary files:
  - `stages/04-implementation/README.md`
  - `stages/04-implementation/implementation-template.md`
- Implementation is important, but it is not the center of this workflow.
- Data preparation execution belongs here, not in Stage 5.
- This stage owns the materialization of dataset manifests, formatted samples, tokenized artifacts, or other prepared inputs that Stage 5 will consume.
- Keep the artifact execution-oriented:
  - changed files,
  - data-preparation scripts and materialized artifacts,
  - config updates,
  - commands,
  - checkpoints and logging paths,
  - smoke checks,
  - readiness for training and validation.
- Required outcome:
  - implementation matches the implementation plan closely enough to run Stage 5,
  - source edits are complete for the current iteration,
  - required data preparation is complete,
  - smoke or unit checks needed before training are complete.

### 5) Training & Validation

- Primary files:
  - `stages/05-training-and-validation/README.md`
  - `stages/05-training-and-validation/training-validation-guide.md`
  - `stages/05-training-and-validation/training-validation-template.md`
- This is the primary evidence gate of the workflow.
- Training here can mean supervised fine-tuning, preference optimization, or reinforcement-style optimization depending on the chosen objective.
- Stage 5 should consume the prepared code, configs, and data artifacts produced in Stage 4.
- Do not move substantial data-preparation work into Stage 5; only bounded integrity checks belong here.
- Record actual empirical evidence, not only intent:
  - objective type,
  - base model and parameter-update strategy,
  - run configuration,
  - commit or diff basis,
  - seed,
  - dataset manifest or split,
  - tokenizer or template version,
  - inference or generation settings used for evaluation,
  - eval harness, judge, or human-review configuration,
  - hardware or environment,
  - checkpoints or update artifacts,
  - metrics or rubric results,
  - sampled outputs when relevant,
  - objective-specific artifacts when relevant,
  - baseline comparison,
  - failure analysis,
  - pass, fail, or inconclusive decision.
- Required outcome:
  - `training-validation-report.md` truthfully closes the current success criteria,
  - blocked or infeasible cases are explicitly recorded,
  - the next action is clear.

### 6) Code Review

- Primary files:
  - `stages/06-code-review/README.md`
  - `stages/06-code-review/code-review-guide.md`
  - `stages/06-code-review/code-review-template.md`
- Run code review only after Stage 5 evidence is current.
- Review focus for LLM fine-tuning work includes:
  - data leakage,
  - data provenance and split contamination mistakes,
  - prompt or chat-template mistakes,
  - tokenizer and special-token mistakes,
  - label masking and target alignment,
  - preference-pair, reward, or trajectory wiring mistakes when applicable,
  - truncation or packing mistakes,
  - generation-setting or inference-template mistakes during evaluation,
  - eval-harness correctness,
  - checkpoint, update-artifact, and config semantics,
  - reproducibility gaps,
  - logging and artifact traceability.
- Required outcome:
  - `code-review.md` records a clear gate decision and any required re-entry classification.

### 7) Docs Sync

- Primary files:
  - `stages/07-docs-sync/README.md`
  - `stages/07-docs-sync/docs-sync-guide.md`
  - `stages/07-docs-sync/docs-sync-template.md`
- Update durable docs only after the current implementation and validation story is truthful.
- Typical sync targets:
  - training commands,
  - dataset-preparation steps and manifest identity,
  - tokenizer or chat-template assumptions,
  - base-model, objective, and update-strategy assumptions,
  - inference or generation settings used for evaluation,
  - evaluator, judge, or human-review configuration,
  - best-known run summary,
  - reproduction notes,
  - important caveats.

### 8) Handoff

- Primary files:
  - `stages/08-handoff/README.md`
  - `stages/08-handoff/handoff-guide.md`
  - `stages/08-handoff/handoff-summary-template.md`
- Finish with:
  - a clear summary of what changed,
  - best training run or best evidence,
  - open risks and next experiments,
  - explicit user verification,
  - ticket archival and repository finalization when applicable.

## Re-Entry Model

Use classified re-entry when a later stage proves the issue is upstream:

- `Local Fix`: the current iteration can be corrected by revisiting implementation directly.
- `Validation Gap`: Stage 6 lacks enough Stage 5 evidence; return to `5 -> 6`.
- `Plan Impact`: the implementation plan is no longer sound enough; return through Stage 3 before more implementation.
- `Requirement Gap`: success criteria or scope were incomplete or wrong; return through Stage 2.
- `Investigation Gap`: the evidence base is insufficient; return through Stage 1.
- `Unclear`: root cause is still uncertain or cross-cutting; reopen from Stage 0 controls and rerun the chain.

Use the transition matrix in `shared/workflow-state-template.md` as the canonical reference for gate behavior.
