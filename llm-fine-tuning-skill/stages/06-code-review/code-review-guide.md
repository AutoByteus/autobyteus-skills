# Stage 6 Code Review Guide

Run code review only after Stage 5 evidence is current enough to judge the implementation truthfully.

## Mandatory Review Focus

- data leakage or split contamination risk
- data provenance and dataset-manifest integrity
- prompt or chat-template correctness
- tokenizer and special-token correctness
- metric correctness and aggregation correctness
- label, mask, target, and sequence-boundary alignment
- preference-pair, reward, or trajectory wiring when applicable
- truncation and packing correctness
- evaluation generation-setting correctness
- checkpoint, update-artifact, merge, and load semantics
- evaluator or judge correctness
- config hygiene and config traceability
- seed handling and reproducibility notes
- numerical stability or silent failure risk
- logging and retained-evidence sufficiency
- dead code or stale fine-tuning and dataset-preparation paths left in scope

## Re-Entry Guidance

- `Local Fix`: bounded implementation issue
- `Validation Gap`: Stage 5 evidence is too weak or incomplete
- `Plan Impact`: implementation plan is not coherent enough
- `Requirement Gap`: success criteria or intended comparison is incomplete
- `Investigation Gap`: key technical understanding is still missing
- `Unclear`: root cause is cross-cutting or still unknown

## Exit Gate

Leave Stage 6 only when `code-review.md` records a clear `Pass` or `Fail` decision and any non-pass outcome includes a re-entry classification.
