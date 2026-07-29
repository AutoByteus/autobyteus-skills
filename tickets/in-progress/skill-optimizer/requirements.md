# Skill Optimizer Requirements

## Goal

Create a reusable `skill-optimizer` skill for reviewing and improving existing skills.

## Required behavior

- **R1 Behavior preservation:** Identify the target skill's behavioral invariants before editing, including any required artifacts, worktrees, stage transitions, tool use, safety boundaries, validation, and user-facing outputs. Do not remove or weaken an invariant merely because its wording is verbose.
- **R2 Defensive wording:** Remove low-value prohibitions when the positive instruction already rules out the alternative. Keep a negative or exception when it prevents a plausible wrong action, protects safety or data, preserves user authority, handles failure, or resolves real ambiguity.
- **R3 Logical flow:** Verify that the target skill moves in a causal order from activation and inputs through actions, outputs, validation, and handoff. Repair unexplained jumps, misplaced prerequisites, and transitions that do not connect the preceding and following content.
- **R4 Grounded claims:** Check that factual claims, tool names, paths, guarantees, and strong requirements are supported by the target skill, its local references, repository evidence, or explicit user requirements. Mark assumptions and preserve unresolved questions instead of inventing facts.
- **R5 Whole-topology review:** Inspect `SKILL.md`, metadata, references, scripts, assets, and any linked files. Check links, naming, ownership, stale files, and duplicated sources of truth.
- **R6 Separation of concerns:** Keep trigger/routing guidance in `SKILL.md`, detailed standards in references, deterministic operations in scripts, and output resources in assets. Give each rule one authoritative home and use concise cross-references elsewhere.
- **R7 Proportionality:** Keep the result concise and readable, but retain detail that controls a fragile, costly, irreversible, or user-visible behavior.
- **R8 Review depth:** Perform at least two distinct review passes: first behavior, structure, grounding, and consistency; second redundancy, wording economy, transitions, and final coherence.
- **R9 Scope fit:** Detect platform, product, company, or project qualifiers that are true in the host environment but unnecessarily narrow the skill's conceptual scope. Retain such terms only when they change triggering, format, tooling, or behavior.
- **R10 Macro-first optimization:** Review package topology, file ownership, authoritative sources, content hierarchy, section priority, and primary instruction spine before sentence-level redundancy or wording cleanup. Treat structural redundancy as a boundary or ownership problem first.
- **R11 Repository boundaries:** Preserve applicable repository branch, worktree, ticket-artifact, finalization, and approval conventions. Do not perform commit, push, merge, release, or deployment as an optimization side effect without explicit authorization.
- **R12 Priority order:** State and follow the optimization priority: package structure and ownership; content architecture and logical flow; factual and behavioral grounding; clarity and precision; then redundancy and economy. Check cross-file consistency throughout.

## Out of scope

- Do not redesign the target skill's domain behavior without evidence or an explicit user request.
- Do not add process artifacts, scripts, references, or metadata fields merely to make the skill look more complete.
- Do not remove safety, failure, accessibility, privacy, destructive-action, or user-authority constraints solely because they are negative statements.

## Output expectations

The skill should guide an agent through evidence-based diagnosis, focused edits, and at least two review passes covering structure, logical flow, factual and behavioral grounding, clarity, redundancy, and consistency. It should normally optimize the target skill in place and provide a concise change summary; it should create a separate report only when requested or when durable evidence is materially useful.
