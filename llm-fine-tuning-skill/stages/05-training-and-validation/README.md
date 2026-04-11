# Stage 5 Training & Validation

## Purpose

Consume the Stage 4-prepared code, configs, and data artifacts, run training or evaluation work, and validate the implemented approach against the current success criteria.

## Enter This Stage When

- Stage 4 is complete for the current iteration
- the code, prepared data artifacts, and configs are stable enough to run training or evaluation meaningfully

Note:
- Data preparation is not owned here except for bounded integrity checks that confirm the Stage 4 outputs are usable.

## Stage-Owned Outputs

- `tickets/in-progress/<ticket-name>/training-validation-report.md`
- run logs, checkpoints or update artifacts, metrics, sample outputs, and any retained evidence artifacts

## Exit Gate

Leave Stage 5 only when the current success criteria are closed truthfully as `Passed`, `Failed`, `Inconclusive`, or explicitly waived by the user for infeasible cases.

## Local Files

- `training-validation-guide.md`
- `training-validation-template.md`
