---
name: deep-learning-experiment-workflow-skill
description: "Run a staged deep-learning experiment workflow from bootstrap through investigation, requirements and success criteria, experiment planning, implementation, training and validation, code review, docs sync, and handoff. Use for model training, fine-tuning, ablations, evaluation, and reproducible empirical validation."
---

# Deep Learning Experiment Workflow Skill

## Overview

Run a staged workflow for deep-learning work where the hard parts are usually investigation quality, experiment definition, and empirical validation rather than large implementation volume.
Use this skill for tasks such as model training, fine-tuning, architecture changes, loss-function changes, data-pipeline changes, ablations, benchmark comparisons, and reproducible evaluation work.

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
  - `stages/03-experiment-plan/`
  - `stages/04-implementation/`
  - `stages/05-training-validation/`
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
- Unlock source-code edits only after Stage 3 `Experiment Plan` is current enough to drive implementation.
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
  - reading local code, configs, logs, checkpoints, and datasets,
  - reading open-source repositories and relevant documentation,
  - checking papers or model references when needed,
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
  - task definition, baseline, metrics, thresholds, constraints, and success criteria are explicit,
  - the planned validation gate can measure pass, fail, or inconclusive results truthfully.

### 3) Experiment Plan

- Primary files:
  - `stages/03-experiment-plan/README.md`
  - `stages/03-experiment-plan/experiment-plan-template.md`
- This stage replaces heavy software-architecture runtime modeling.
- Focus on:
  - chosen hypothesis and rationale,
  - model or algorithm changes,
  - data and split assumptions,
  - loss, optimizer, scheduler, and training recipe,
  - evaluation protocol,
  - ablations or comparison matrix,
  - reproducibility plan,
  - implementation work items.
- Required outcome:
  - `experiment-plan.md` is current and can drive Stage 4 implementation and Stage 5 training or evaluation.

### 4) Implementation

- Primary files:
  - `stages/04-implementation/README.md`
  - `stages/04-implementation/implementation-template.md`
- Implementation is important, but it is not the center of this workflow.
- Keep the artifact execution-oriented:
  - changed files,
  - config updates,
  - commands,
  - checkpoints and logging paths,
  - smoke checks,
  - readiness for training and validation.
- Required outcome:
  - implementation matches the experiment plan closely enough to run Stage 5,
  - source edits are complete for the current iteration,
  - smoke or unit checks needed before training are complete.

### 5) Training & Validation

- Primary files:
  - `stages/05-training-validation/README.md`
  - `stages/05-training-validation/training-validation-guide.md`
  - `stages/05-training-validation/training-validation-template.md`
- This is the primary evidence gate of the workflow.
- Record actual empirical evidence, not only intent:
  - run configuration,
  - commit or diff basis,
  - seed,
  - data version or split,
  - hardware or environment,
  - checkpoints,
  - metrics,
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
- Review focus for deep-learning work includes:
  - data leakage,
  - train or eval mode mistakes,
  - metric correctness,
  - label and mask alignment,
  - checkpoint and config semantics,
  - numerical stability,
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
  - config assumptions,
  - dataset or split expectations,
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
  - best run or best evidence,
  - open risks and next experiments,
  - explicit user verification,
  - ticket archival and repository finalization when applicable.

## Re-Entry Model

Use classified re-entry when a later stage proves the issue is upstream:

- `Local Fix`: the current iteration can be corrected by revisiting implementation directly.
- `Validation Gap`: Stage 6 lacks enough Stage 5 evidence; return to `5 -> 6`.
- `Plan Impact`: the experiment plan is no longer sound enough; return through Stage 3 before more implementation.
- `Requirement Gap`: success criteria or scope were incomplete or wrong; return through Stage 2.
- `Investigation Gap`: the evidence base is insufficient; return through Stage 1.
- `Unclear`: root cause is still uncertain or cross-cutting; reopen from Stage 0 controls and rerun the chain.

Use the transition matrix in `shared/workflow-state-template.md` as the canonical reference for gate behavior.
