# Experiment Plan

Write to:
- `tickets/in-progress/<ticket-name>/experiment-plan.md`

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

## Baseline And Comparison Target

- Baseline summary:
- Expected comparison:
- Risks in the baseline record:

## Approach Summary

- Chosen approach:
- Alternative(s) considered:
- Why the chosen approach wins for this iteration:

## Planned Model / Algorithm Changes

| Area | Planned Change | Why | Risk |
| --- | --- | --- | --- |
| Model / Architecture |  |  |  |
| Loss / Objective |  |  |  |
| Data Pipeline / Sampling / Augmentation |  |  |  |
| Optimizer / Scheduler |  |  |  |
| Checkpointing / Logging |  |  |  |

## Data And Evaluation Assumptions

- Train split:
- Validation split:
- Test split:
- Data version or source assumptions:
- Evaluation protocol:
- Leakage checks:

## Experiment Matrix

| Experiment ID | Purpose | Variable(s) Changed | Fixed Controls | Expected Outcome | Priority |
| --- | --- | --- | --- | --- | --- |
| EXP-001 |  |  |  |  | High |

## Reproducibility Plan

- Config source of truth:
- Seed strategy:
- Environment capture:
- Artifact output locations:
- Checkpoint naming:
- Metric logging plan:

## Implementation Handoff

| Work Item ID | Files / Configs / Scripts | Change Type (`Create` / `Modify` / `Remove`) | Why Needed | Validation Dependency |
| --- | --- | --- | --- | --- |
| W-001 |  |  |  |  |

## Validation Plan

- Which success criteria each experiment addresses:
- Primary metrics to record:
- Baseline comparison method:
- Failure or inconclusive conditions to detect early:

## Risks And Open Questions

- 

## Stage 4 Entry Checklist

- `requirements.md` is `Plan-ready` or `Refined`:
- Implementation work items are explicit:
- Validation method is explicit:
- Reproducibility plan is explicit:
- Ready to unlock code edits: `Yes` / `No`
