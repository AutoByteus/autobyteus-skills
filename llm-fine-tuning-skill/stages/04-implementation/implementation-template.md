# Implementation & Data Preparation

Write to:
- `tickets/in-progress/<ticket-name>/implementation.md`

Use this artifact as the Stage 4 execution record.
Keep it practical and implementation-focused.
Stage 4 owns code changes and the materialization of prepared data artifacts that Stage 5 will consume.

## Upstream Artifacts

- Workflow state: `tickets/in-progress/<ticket-name>/workflow-state.md`
- Investigation notes: `tickets/in-progress/<ticket-name>/investigation-notes.md`
- Requirements: `tickets/in-progress/<ticket-name>/requirements.md`
- Implementation plan: `tickets/in-progress/<ticket-name>/implementation-plan.md`

## Document Status

- Current Status: `Draft` / `Ready For Execution` / `In Execution` / `Ready For Training`
- Last Updated:

## Stage 4 Entry Checklist

- `workflow-state.md` shows `Current Stage = 4`:
- `workflow-state.md` shows `Code Edit Permission = Unlocked`:
- `implementation-plan.md` is current:
- implementation work items are explicit:
- training, evaluation, and data-preparation entrypoints to touch are identified:

## Execution Plan

- Goal of this implementation iteration:
- Out-of-scope items:
- Main risks:

## Data Preparation Execution

- Source datasets or raw inputs consumed:
- Planned materialization outputs:
- Actual materialization outputs:
- Final training or validation manifests produced:
- Formatting, tokenization, or packing artifacts produced:
- Data validation or sanity checks:
- Can Stage 5 consume these artifacts without further mutation: `Yes` / `No`
- Remaining data risks:

## Change Inventory

| Change ID | Files / Configs / Scripts | Action (`Create` / `Modify` / `Remove`) | Purpose | Status (`Planned` / `In Progress` / `Done` / `Blocked`) |
| --- | --- | --- | --- | --- |
| C-001 |  |  |  | Planned |

## Config, Logging, And Artifact Paths

- Primary config files:
- Dataset manifest or materialization outputs:
- Prompt or chat-template source:
- Tokenizer config source:
- Output directory conventions:
- Checkpoint path plan:
- Logging and metrics sink:
- Inference or generation settings source for evaluation:
- Resume or recovery plan:

## Readiness Checks Before Stage 5

| Check | Result (`Pass` / `Fail` / `N/A`) | Evidence |
| --- | --- | --- |
| Dataset manifest or materialization resolves |  |  |
| Prompt or chat template renders expected sample |  |  |
| Tokenizer and special-token setup align with the plan |  |  |
| Objective-specific labels, rewards, or trajectories resolve |  |  |
| Training entrypoint resolves |  |  |
| Validation or evaluation entrypoint resolves |  |  |
| Evaluation generation settings resolve as planned |  |  |
| Critical config loads correctly |  |  |
| Output paths or permissions are correct |  |  |
| Smoke test or dry run passes |  |  |

## Stage 5 Handoff

- Planned runs:
- Required config identifiers:
- Required dataset manifests or split versions:
- Prepared data artifacts Stage 5 should consume directly:
- Required tokenizer or template versions:
- Required evaluation generation settings:
- Required evaluator or judge config:
- Required seeds:
- Required metrics:
- Required qualitative review artifacts:
- Required artifacts to retain:

## Progress Log

- YYYY-MM-DD: Stage 4 started.
