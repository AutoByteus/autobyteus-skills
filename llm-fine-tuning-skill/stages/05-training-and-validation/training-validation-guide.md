# Stage 5 Training & Validation Guide

Stage 5 is the main empirical evidence gate of this workflow.
Do not treat this stage as a lightweight test summary.
Stage 5 consumes the prepared code, configs, and data artifacts produced in Stage 4.
Do not move major data-preparation work into this stage; only bounded integrity checks belong here.

## Required Evidence

Record enough detail to understand and reproduce what happened:

- run identifier
- purpose of the run
- objective type
- base model and update strategy
- code or commit basis
- config identifier or config diff
- seed
- dataset manifest or split version
- prepared data artifact identifiers when they differ from the manifest
- tokenizer or template version
- inference or generation settings used for evaluation
- evaluator, judge, or human-review configuration when used
- hardware or environment
- checkpoint or update-artifact paths
- metric outputs or rubric results
- sampled outputs or rubric evaluations when relevant
- objective-specific artifacts when relevant
- baseline comparison
- anomalies, failures, or instability notes

## Required Behavior

- compare results against the success criteria in `requirements.md`
- state clearly whether each criterion is `Passed`, `Failed`, or `Inconclusive`
- record why a result is inconclusive when it cannot close the criterion
- when criteria are behavioral rather than purely numeric, record the rubric or sample-review decision that closed them
- distinguish implementation bugs, data bugs, formatting bugs, and weak training outcomes from each other
- if Stage 5 reveals missing or broken data preparation, classify the return path instead of silently redoing Stage 4 work here
- if the environment, evaluator, or required human review blocks proper evaluation, keep Stage 5 `Blocked` unless the user explicitly waives the blocked closure

## Re-Entry Guidance

- use `Local Fix` when the issue is a bounded implementation defect
- use `Plan Impact` when the implementation plan itself is wrong or incomplete
- use `Requirement Gap` when the success target or intended comparison was underspecified
- use `Investigation Gap` when missing understanding caused the bad run or invalid interpretation
- use `Unclear` when the root cause is still uncertain after analysis

## Exit Gate

Leave Stage 5 only when `training-validation-report.md` truthfully records:
- what was run,
- what happened,
- how it compares to the baseline,
- what the gate decision is,
- what the next action should be.
