# Code Review

## Decision

Pass. No blocking findings remain.

## Pass 1: behavior and structure

- Checked that the description triggers on skill auditing/refactoring and names the relevant package surfaces.
- Checked preservation of outputs, artifacts, worktrees, stage transitions, tools, validation, safety controls, and user authority as explicit invariants.
- Checked that factual grounding requires target-file, repository, tool, trusted-source, or user evidence and escalates ambiguous material changes.
- Checked that conceptual scope remains independent from the host platform unless a platform label changes behavior, format, tooling, or triggering.
- Checked the primary flow: baseline -> ledger -> diagnosis -> authoritative edits -> package validation -> two review passes -> output.
- Checked that optimization order is explicit and macro-first: package structure and ownership -> content architecture and logical flow -> factual and behavioral grounding -> clarity and precision -> redundancy and economy.
- Checked ownership: `SKILL.md` owns routing, the reference owns detailed tests, and metadata owns invocation presentation.
- Checked the reference path, metadata file, absence of initializer residue, and validator result.

Finding corrected during this pass: the warning against adding a report format was narrowed to a `package report format`, so it does not conflict with the optional working-context review record described in the reference.

## Pass 2: economy and coherence

- Removed template scaffolding and kept the main guide compact and procedural.
- Kept detailed examples and edge cases in the reference rather than duplicating them in `SKILL.md`.
- Preserved the bus-55 distinction: remove prohibitions against implausible alternatives, but retain constraints that prevent realistic destructive, unauthorized, unsafe, ambiguous, or unsupported actions.
- Read the sections in order and confirmed that prerequisites precede actions, actions precede validation, and the output section provides a concrete stopping point.
- Generalized a repository-specific workflow-state warning into the reusable `process-state` principle.
- Added paired good/bad examples for each major rubric area, including the `skills` versus `Codex skills` scope distinction.
- Removed the remaining host-context wording from the live skill trigger; `Codex` now appears only in the deliberate scope counterexample and the genuine package-format example.
- No unexplained transition jumps, contradictory file conventions, unsupported local paths, or stale package files remain.

Residual risk: the skill's quality still depends on the agent correctly identifying the target skill's actual invariants; ambiguous user-visible behavior changes are therefore explicitly surfaced rather than guessed.

## Self-optimization review

The optimizer was applied to its own package.

Pass 1 found and corrected:

- an over-broad `remove TODOs` instruction that could delete intentional examples or domain text;
- a factual example that stated validator output without explicitly requiring the check to have run;
- a package documentation rule that needed to preserve existing docs with a distinct audience;

Pass 2 found and corrected:

- an invariant-inventory sentence that could imply every skill needs worktrees and stage transitions. It now says `any required` behaviors.

Final result: the self-targeted package passes the same scope, behavior, grounding, flow, redundancy, topology, and two-pass review that it instructs other skills to undergo.

## Macro-first refinement

The review identified that the prior ledger-first sequence could encourage local wording analysis before structural diagnosis. The package now requires:

1. package topology, ownership, authoritative sources, and primary spine;
2. content hierarchy, section priority, and macro flow;
3. behavior-bearing rule analysis;
4. local redundancy and wording economy.

Structural redundancy is explicitly treated as a boundary or ownership signal before any repeated phrase is removed.

The follow-up self-review found and corrected:

- inconsistent `handoff` ordering in the main guide and rubric;
- detailed ownership guidance appearing after micro-level checks;
- duplicated topology examples in the macro rubric section;
- detailed logical-flow checks appearing after defensive wording.

The current rubric sequence is macro structure and ownership -> content architecture and priority -> logical flow -> scope and audience fit -> behavior contract -> factual grounding -> clarity and precision -> defensive wording -> remaining redundancy and authority -> effective-skill review. The two-pass review record follows those checks as the final gate.

Final consistency scan also aligned the content-architecture example with the canonical recovery-aware flow.

This review round also corrected the in-place output default so repository-specific worktree, ticket-artifact, finalization, and approval rules remain authoritative, and commit/push/merge/release/deployment actions remain explicitly gated.

## Latest self-optimization pass

The prior priority list named clarity but did not give it a dedicated review stage. Added an explicit clarity-and-precision stage after factual and behavioral grounding and before defensive wording and redundancy cleanup. Aligned the same priority order across `SKILL.md`, `optimization-rubric.md`, `agents/openai.yaml`, and the requirements record.

## Current self-optimization pass

Pass 1 found no live package topology, ownership, flow, grounding, or behavior defects. Pass 2 found stale historical wording in the ticket record: an obsolete line-count claim, an older rubric-order summary, and a note that could imply all `TODO` text was removed. Updated those records without changing the skill's behavior. The final stale scan now leaves platform-specific wording only in deliberate rubric examples.
