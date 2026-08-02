# Skill Optimizer Self-Optimization Analysis

Review Status: Approved plan implemented - validation complete
Review date: 2026-08-02
Target: `skill-optimizer/`
Review scope: Consistency of the analysis-first workflow, macro-before-micro architecture, report contract, action classification, metadata, and rubric alignment.

## User Outcome

The optimizer should first understand the user's request and the target skill, record a readable analysis and improvement plan in one file, stop for user review, and edit only after explicit approval. The analysis must treat macro architecture as primary and micro wording as secondary. Optimization must include removal, movement, merging, restructuring, and keeping when those are better than adding or updating files.

## Current Package Baseline

| Path | Responsibility | Authority |
| --- | --- | --- |
| `SKILL.md` | Trigger, operating contract, workflow, approval boundary, and output contract | Primary procedure |
| `references/optimization-rubric.md` | Detailed review tests, principles, examples, and report record | Review standard |
| `agents/openai.yaml` | Display metadata and default invocation prompt | Invocation metadata |

Primary flow currently reads:

`read and map -> stabilize baseline -> ledger -> macro and micro diagnose -> write analysis and pause -> user approval -> approved edit -> validate -> macro and micro review passes -> report`

The package has one linked reference, no scripts or assets, and no competing workflow file. The three authoritative files currently have pre-existing uncommitted changes from the earlier analysis-first correction; no additional authoritative files have been changed during this review.

## Preserved Invariants

- Macro package structure, ownership, logical flow, and cross-file authority are reviewed before micro wording and economy.
- A user-visible analysis artifact is written before authoritative edits.
- The optimizer stops until the user explicitly approves the proposed plan.
- The plan can preserve, add, update, remove, move, merge, or restructure material.
- Existing behavior, safety controls, validation, recovery, and user-authority boundaries are preserved unless an approved change or demonstrated defect justifies otherwise.
- Repository-specific branch, worktree, ticket-artifact, and finalization rules remain authoritative.
- No commit, push, merge, release, or deployment occurs as an optimization side effect.

## Findings

### OPT-001 - Macro and micro analysis are not explicit report sections

Severity: Medium
Classification: Design clarity

Evidence:

- `SKILL.md` establishes the priority order, but Step 4 lists macro structure, grounding, clarity, and redundancy in one undifferentiated diagnostic list.
- The analysis template has one combined `Findings and evidence` section and one combined `Proposed improvements` section.
- The workflow therefore permits a reader or agent to mix architecture changes with sentence-level edits even though the intended reasoning order is macro first, then micro.

Impact:

The user may not be able to tell whether a proposal changes package architecture, ownership, or behavior, or merely improves wording. A micro cleanup could appear alongside an unresolved macro defect instead of being clearly downstream of it.

### OPT-002 - The report template mixes pre-approval analysis with post-edit review fields

Severity: Medium
Classification: Contract clarity

Evidence:

- `SKILL.md` says the optimizer stops before edits and that the two review passes occur after a material edit.
- The rubric's required report template places `Pass 1`, `Pass 2`, `Corrections made`, and `Redundancy removed` immediately under the pre-edit analysis record.
- `Files changed: None` does not distinguish target skill files from the newly created analysis artifact or pre-existing working-tree changes.

Impact:

The report can imply that corrections or economy changes already happened while the optimizer is supposed to be waiting. This weakens the user-facing approval boundary and makes the report's lifecycle ambiguous.

## Proposed Improvements

### 1. Explicitly separate macro and micro analysis

Action: `Update`

Affected files: `skill-optimizer/SKILL.md`, `skill-optimizer/references/optimization-rubric.md`

Plan:

- Keep macro analysis first: package topology, ownership, authority, logical flow, invariants, outputs, validation, and recovery.
- Add a distinct micro analysis section that runs only after the macro structure is coherent: wording, terminology, redundancy, qualifiers, transitions, and economy.
- Require the report to list macro findings and macro proposed actions before micro findings and micro proposed actions.
- Preserve the existing action taxonomy and the rule that micro edits cannot compensate for unresolved macro defects.

Implementation: Applied in `skill-optimizer/SKILL.md` and `skill-optimizer/references/optimization-rubric.md`.

### 2. Separate pre-approval analysis from post-approval implementation review

Action: `Restructure`

Affected file: `skill-optimizer/references/optimization-rubric.md`

Plan:

- Keep the pre-approval report fields for baseline, invariants, findings, proposed actions, assumptions, risks, and validation plan.
- Replace pre-edit `Corrections made` and `Redundancy removed` fields with proposed or pending outcomes.
- Add a clearly labeled post-approval implementation and validation section for actual changed files, validation results, macro pass, micro pass, and residual risk.
- Rename `Files changed: None` to `Target skill files changed during analysis: None`, and record the analysis artifact separately.

Implementation: Applied in `skill-optimizer/references/optimization-rubric.md`.

### 3. Preserve the current metadata and approval behavior

Action: `Keep`

Affected file: `skill-optimizer/agents/openai.yaml`

The current default prompt correctly tells the optimizer to analyze, write the report, stop for review, and apply only approved changes. No operating modes or additional process-state layer are needed.

## Risks and Open Questions

- The repository does not define a universal ticket-artifact location for skill optimization reports. The current fallback of placing `optimization-analysis.md` beside the target is acceptable, but the implementation should keep the file clearly identified as a review artifact rather than runtime guidance.
- The report lifecycle should remain one file, as requested. No separate approval or implementation state file is necessary.
- The current authoritative-file changes remain uncommitted working-tree changes. The approved refinement was applied without committing or pushing.

## Validation Results

- Re-read `SKILL.md`, `optimization-rubric.md`, and `agents/openai.yaml` in execution order: passed.
- Macro-before-micro sections and pre/post-approval report sections agree across the authoritative workflow and rubric: passed.
- The action taxonomy is identical wherever it appears: passed.
- Report fields now distinguish analysis-time and post-approval lifecycle states: passed.
- `git diff --check`: passed.
- Macro review pass: package ownership, flow, invariants, authority, outputs, validation, and handoff remain coherent.
- Micro review pass: wording is consistent, terminology is aligned, and no new redundant process-state layer was introduced.

## Review Decision

The approved plan was implemented successfully. The optimizer now explicitly analyzes macro structure before micro wording, records both in the user-visible report, and separates pre-approval analysis from post-approval implementation and validation. No operating modes or additional process-state layer were introduced.

Target skill files changed during approved implementation:

- `skill-optimizer/SKILL.md`
- `skill-optimizer/references/optimization-rubric.md`

Pre-existing working-tree change retained without modification: `skill-optimizer/agents/openai.yaml`
Analysis artifact updated: `skill-optimizer/optimization-analysis.md`
