# Stage 5 Training & Validation Guide

Stage 5 is the main empirical evidence gate of this workflow.
Do not treat this stage as a lightweight test summary.

## Required Evidence

Record enough detail to understand and reproduce what happened:

- run identifier
- purpose of the run
- code or commit basis
- config identifier or config diff
- seed
- dataset or split version
- hardware or environment
- checkpoint paths
- metric outputs
- baseline comparison
- anomalies, failures, or instability notes

## Required Behavior

- compare results against the success criteria in `requirements.md`
- state clearly whether each criterion is `Passed`, `Failed`, or `Inconclusive`
- record why a result is inconclusive when it cannot close the criterion
- distinguish implementation bugs from weak experimental outcomes
- if the environment blocks proper evaluation, keep Stage 5 `Blocked` unless the user explicitly waives the blocked closure

## Re-Entry Guidance

- use `Local Fix` when the issue is a bounded implementation defect
- use `Plan Impact` when the experiment plan itself is wrong or incomplete
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
