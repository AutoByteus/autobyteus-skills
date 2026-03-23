# Stage 5 Call-Stack Review Guide

## Purpose

Stage 5 is a deep review gate, not a lightweight approval pass.
It checks whether the design basis and future-state runtime model are coherent enough to unlock implementation.

## Inputs

- current design basis from Stage 3
- current future-state runtime call stacks from Stage 4
- `shared/design-principles.md`
- `shared/common-design-practices.md`

## Review Loop

1. Run a deep review round.
2. Run a dedicated missing-use-case discovery sweep.
3. Record findings in `future-state-runtime-call-stack-review.md`.
4. If updates are required, classify the round as `Design Impact`, `Requirement Gap`, or `Unclear`.
5. Follow the classified upstream path, update the required artifacts there, and then return to Stage 5 for the next round.
6. Track clean-review streak state as `Reset`, `Candidate Go`, or `Go Confirmed`.

## Review Dimensions

Every round should judge at least:

- architecture fit for the use case
- data-flow spine clarity and spine inventory completeness
- ownership clarity and support-structure clarity
- boundary placement and ownership-driven dependency quality
- file-placement alignment with the owning subsystem or folder
- flat-vs-over-split layout quality
- interface and service-method boundary clarity
- alignment with the target design basis
- use-case coverage completeness and source traceability
- naming quality and naming-to-responsibility alignment
- redundancy, simplification opportunity, and cleanup completeness
- no backward compatibility and no legacy-retention mechanisms

## Go-Confirmed Rule

Do not unlock implementation on one clean round.
The gate is `Go Confirmed` only after two consecutive deep-review rounds find:

- no blockers
- no required persisted artifact updates
- no newly discovered use cases

The first clean round is `Candidate Go`.
The second consecutive clean round is `Go Confirmed`.

## Re-Entry Discipline

- Record classification and return path in both `future-state-runtime-call-stack-review.md` and `workflow-state.md` before moving upstream.
- Apply required updates in the correct upstream stage, not only in Stage 5 notes.
- Start the next round from the updated files, not from memory.

## Exit Gate

This stage is complete only when the review artifact shows `Go Confirmed` with the required two-round clean streak.
