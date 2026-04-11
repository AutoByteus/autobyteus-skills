# Implementation Plan

Write to:
- `tickets/in-progress/<ticket-name>/implementation-plan.md`

## Document Status

- Current Status: `Draft` / `Reviewing` / `Current`
- Last Updated:

## Artifact Basis

- Investigation notes: `tickets/in-progress/<ticket-name>/investigation-notes.md`
- Requirements: `tickets/in-progress/<ticket-name>/requirements.md`
- Requirements Status: `Plan-ready` / `Refined`

## Problem Framing

- Goal:
- Main hypothesis:
- Why this plan is worth running:

## Training Mode

- Objective Type: `Supervised Fine-Tuning` / `Preference Optimization` / `Reinforcement-Style Training` / `Other`
- Parameter-Update Strategy: `Adapter-Based` / `Quantized Adapter-Based` / `Full-Parameter` / `Other`
- Base Model / Starting Checkpoint:
- Why this mode is appropriate:

## Baseline And Comparison Target

- Baseline summary:
- Expected comparison:
- Risks in the baseline record:

## Data Preparation Design

Design the preparation in Stage 3.
Materialize the prepared artifacts in Stage 4.

| Dataset / Source | Ingestion Or Source Of Truth | Filtering / Cleaning | Output Schema | Split / Holdout Plan | Risks |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

- Provenance constraints:
- Privacy or policy constraints:
- Contamination or leakage checks:
- Final manifest or artifact path plan:
- Stage 4 materialization owner and method:
- Stage 5 consumption boundary:

## Prompt, Chat Template, And Tokenization Plan

- Prompt or chat template source of truth:
- Message or sample schema:
- Tokenizer version:
- Special-token assumptions:
- Label-masking rule:
- Truncation rule:
- Packing rule:
- Sequence-boundary assumptions:

## Training Recipe

- Chosen approach:
- Alternative(s) considered:
- Why the chosen approach wins for this iteration:
- Optimizer:
- Scheduler:
- Precision:
- Batch size / gradient accumulation:
- Sequence length:
- Checkpoint cadence:
- Logging cadence:

## Objective-Specific Notes

- If the objective uses preference pairs, record pair quality assumptions and pair schema:
- If the objective uses reward or judge signals, record the source and failure risks:
- If the objective uses rollouts or trajectories, record trajectory generation and filtering assumptions:

## Evaluation And Validation Plan

- Automatic metrics:
- Held-out prompt or task suite:
- Qualitative sample review plan:
- Judge or human-review plan:
- Inference or generation settings used for evaluation:
- Regression or safety checks:
- Baseline comparison method:
- Stage 4 outputs required before any Stage 5 run:

## Run Matrix

| Run ID | Purpose | Variable(s) Changed | Fixed Controls | Expected Outcome | Priority |
| --- | --- | --- | --- | --- | --- |
| RUN-001 |  |  |  |  | High |

## Reproducibility Plan

- Config source of truth:
- Seed strategy:
- Environment capture:
- Dataset manifest versioning:
- Template and tokenizer versioning:
- Generation-setting versioning:
- Artifact output locations:
- Checkpoint naming:
- Metric and sample-output logging plan:

## Implementation Handoff

| Work Item ID | Files / Configs / Scripts | Change Type (`Create` / `Modify` / `Remove`) | Why Needed | Validation Dependency |
| --- | --- | --- | --- | --- |
| W-001 |  |  |  |  |

## Risks And Open Questions

- 

## Stage 4 Entry Checklist

- `requirements.md` is `Plan-ready` or `Refined`:
- data preparation design and output manifests are explicit:
- prompt or chat-format rules are explicit:
- tokenization and label-masking rules are explicit:
- Implementation work items are explicit:
- Validation method is explicit:
- Reproducibility plan is explicit:
- Ready to unlock code edits: `Yes` / `No`
