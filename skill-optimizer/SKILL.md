---
name: skill-optimizer
description: "Review and improve existing skills in priority order: package structure, ownership, and cross-file consistency; content architecture and logical flow; factual and behavioral grounding; clarity and precision; and redundancy and economy. Use when an agent needs to audit or refactor a skill's main guide, references, scripts, assets, or metadata; repair content organization or wording; or make a skill shorter without weakening real safeguards."
---

# Skill Optimizer

Improve a skill as a coherent instruction system. Optimize for the smallest clear set of instructions that preserves the target skill's actual behavior, constraints, outputs, and safety boundaries.

Read [references/optimization-rubric.md](references/optimization-rubric.md) for the detailed review tests, principles, and paired examples. Keep the main guide focused on the procedure and use the reference for classification and edge cases.

Apply this priority order: package structure and ownership -> content architecture and logical flow -> factual and behavioral grounding -> clarity and precision -> redundancy and economy. Treat cross-file consistency as a gate throughout, beginning with the package structure.

## Operating contract

- Read the target skill and its linked files before editing. Treat `SKILL.md`, metadata, references, scripts, and assets as one topology.
- Review the package structure before local wording. Treat repeated content across files or sections as evidence of an ownership, boundary, or flow problem until proven otherwise.
- Establish the target skill's behavioral invariants before trying to shorten it. Include any required outputs, artifacts, worktrees, stage transitions, tool use, validation, safety controls, and user-authority boundaries.
- Preserve behavior unless the user explicitly asks for a behavior change or the target contains a demonstrable contradiction, stale path, or unsupported claim.
- Use evidence from the target files, repository instructions, available tools, trusted source material, and explicit user requirements. Label inferences and leave unresolved questions visible.
- Preserve repository-specific branch, worktree, ticket-artifact, finalization, and user-approval rules when they apply; do not replace them with this skill's default editing path. Do not commit, push, merge, release, or deploy as an optimization side effect unless explicitly requested.
- Always complete a user-visible analysis before editing. Write the analysis and proposed improvement plan to one clear file, stop for the user to review it, and edit only after explicit approval.
- Keep the target skill's conceptual scope independent from its host platform. Retain a platform, product, company, or project name only when it changes the trigger, file format, tool integration, or behavior.
- If a correction would materially change a user-visible commitment and the evidence is ambiguous, ask instead of guessing.
- Make each rule live in one authoritative file. Use short cross-references instead of copying the same rule into several files.
- Remove obsolete content explicitly and check for links, metadata, filenames, and references that still point to it.
- Keep the final result proportional. Detail that controls a fragile, costly, irreversible, security-sensitive, or user-visible behavior is not noise merely because it is long.

## Workflow

### 1. Map the package structure

Identify the target skill root and read its `SKILL.md` completely. Then enumerate its metadata, references, scripts, assets, templates, and linked paths. Read the repository instructions that govern the target.

Map the macro structure before editing individual sentences:

- the primary skill spine: trigger -> inputs and prerequisites -> core work -> outputs -> validation and recovery -> handoff;
- each file's responsibility and authoritative source of truth;
- reference and dependency direction;
- duplicated files, competing guides, repeated checklists, and stale artifacts;
- candidate add, merge, move, or remove decisions.

Do not begin sentence-level optimization until the spine, ownership boundaries, and package topology are coherent enough to support the intended behavior.

### 2. Stabilize the content architecture

Read the main guide and references in execution order. Check the hierarchy and priority of the content:

- purpose, scope, and audience;
- prerequisites and inputs;
- core workflow and decision points;
- outputs;
- validation and recovery;
- handoff;
- optional detail, examples, and reference material.

Repair misplaced sections, abrupt transitions, competing workflows, and structurally repeated rules before editing local wording. Structural redundancy usually signals a missing owner or an incorrect file or section boundary.

Capture a compact baseline:

- intended trigger and user task;
- intended audience and domain scope;
- primary instruction flow from entry to handoff;
- required outputs and validation;
- explicit constraints and failure handling;
- files that own each behavior;
- open questions and assumptions.

Do not edit while the target's behavior is still unclear.

### 3. Build an instruction ledger

For every behavior-bearing rule, identify its purpose, precondition, action, output or exit condition, authoritative owner, and evidence. Classify it as one of:

- core action;
- prerequisite or constraint;
- exception or recovery path;
- validation or quality gate;
- explanation that can be removed if it adds no decision value;
- low-value noise: a prohibition or warning that closes no plausible branch and changes no output, safety boundary, authority rule, recovery path, or validation requirement.

Use the ledger to distinguish useful guardrails from defensive noise. For every negative or prohibitive instruction, record the positive route it supports, the realistic mistake it prevents, and the distinct boundary it protects. If it only forbids work the user did not request and the workflow does not plausibly invite, classify it as noise unless removing it would change behavior. Do not catalogue filler mechanically when the skill is small, but do account for every rule whose removal could change behavior.

### 4. Diagnose the system

Diagnose the target in macro-to-micro order. Do not mix sentence-level cleanup into an unresolved package, ownership, flow, or behavioral problem.

#### Macro analysis

Check the target against the rubric for:

- package topology, ownership, authoritative sources, and structural redundancy;
- content hierarchy, priority, and macro flow;
- behavioral invariants, required outputs, validation, recovery, and handoff;
- factual or behavioral grounding, unsupported certainty, and scope drift;
- missing prerequisites, ambiguous contracts, abrupt transitions, and duplicated or contradictory rules;
- stale references, metadata drift, unused files, and obsolete boundaries.

Separate design, ownership, flow, and grounding defects from wording defects. Reordering or shortening text cannot fix a missing owner, an ambiguous contract, or an unsupported requirement.

Do not begin micro analysis until the macro structure and behavior are coherent enough to support it. If a macro defect blocks a micro decision, record the dependency in the analysis instead of guessing.

#### Micro analysis

After macro analysis is coherent, check:

- vague, ambiguous, overloaded, or imprecise wording;
- inconsistent terminology, qualifiers, conditions, or exception placement;
- low-value negative wording and defensive noise;
- repeated sentences, transitions, examples, or explanations;
- unnecessary verbosity and opportunities for concise wording without information loss.
- every instruction-bearing sentence or bullet for normal-path relevance, especially prohibitions that may only describe unrequested work;
- whether each retained negative sentence closes a plausible branch or protects a distinct safety, authority, recovery, validation, or output boundary.

Do not finish the micro pass until each negative or prohibitive sentence has a disposition: `Keep`, `Rewrite`, `Remove`, or `Move`. Micro improvements must preserve the macro structure, behavioral invariants, evidence, safety boundaries, and required outputs.

### 5. Write the analysis and pause for user review

Before changing the target skill, create one user-visible `optimization-analysis.md` at the repository's appropriate analysis or ticket-artifact path. If no repository convention exists, place it beside the target skill and identify it as a review artifact rather than a runtime instruction.

The file must be easy to scan and contain:

- `Review Status: Analysis complete - awaiting user approval`;
- the user's requested outcome and the review scope;
- the current behavior and package/file ownership baseline;
- preserved behavioral invariants, safety boundaries, and required outputs;
- a `Macro analysis` section covering package structure, ownership, flow, behavior, grounding, outputs, validation, recovery, and handoff;
- a `Micro analysis` section covering wording, terminology, redundancy, qualifiers, transitions, and economy, written only after the macro analysis is coherent;
- macro findings followed by micro findings, each with severity, evidence, and concrete impact;
- proposed improvements ordered macro first and micro second, including the exact file or boundary affected;
- an explicit action for every proposal: `Keep`, `Add`, `Update`, `Remove`, `Move`, `Merge`, or `Restructure`;
- assumptions, open questions, risks, and the validation plan;
- `Target skill files changed during analysis: None`;
- the path of the analysis artifact itself.

Optimization is not synonymous with adding or updating files. A sound proposal may keep existing material, remove obsolete material, move or merge responsibilities, split an overloaded owner, restructure the package, or conclude that no change is justified.

Stop after writing the analysis. Do not edit authoritative skill files, run implementation-oriented validation, commit, push, or perform other optimization side effects until the user explicitly approves the proposed plan. If the user changes the request, revise the analysis before editing.

### 6. Edit the authoritative sources

Apply the smallest coherent edit set:

- put the main trigger, routing, and short workflow in `SKILL.md`;
- move detailed standards, variants, examples, and checklists into directly linked references;
- keep deterministic operations in scripts and output resources in assets;
- reorder content so prerequisites precede actions, actions precede outputs, validation follows the behavior it proves, and handoff follows validation;
- resolve structural redundancy first by choosing an authoritative owner or changing the file/section boundary; only then remove repeated sentences or phrases;
- replace unsupported certainty with a grounded statement, an explicit assumption, or a question;
- replace inherited host-context labels with domain terms when the label does not change behavior; retain it when the target genuinely depends on that platform and state the dependency precisely;
- make each retained instruction concrete, scoped, and easy to act on without adding explanatory noise;
- remove a negative instruction only when the positive instruction already rules out the alternative, the alternative is not a plausible normal-path branch, and no realistic failure, safety, authority, ambiguity, recovery, validation, or output boundary is lost; move package-only scope reminders to package documentation when they are needed but do not affect runtime behavior;
- remove duplicates and stale files only after confirming their behavior is represented by the surviving authoritative source.

Do not add a new process-state layer, helper script, or reference file solely to make the package appear more complete. The required analysis file is a review output, not a runtime dependency or a new execution-state layer.

### 7. Validate the package

Review the changed package as a reader would load it:

- validate frontmatter and skill naming with the available standard skill validator;
- confirm metadata describes the actual trigger and default prompt;
- check every link and referenced path;
- check that references are directly discoverable from `SKILL.md` and do not form unnecessary deep chains;
- remove initializer placeholders and template residue; preserve literal `TODO` text when it is an intentional example or domain instruction;
- run syntax or focused checks for changed scripts when scripts exist;
- compare the baseline invariants with the optimized package.

Record limitations when a check cannot run. Do not claim a validation result that was not observed.

### 8. Perform two review passes

Always complete both passes, even when the first pass finds no issue.

1. **Macro behavior and structure:** verify package topology, file ownership, authoritative sources, content hierarchy, section priority, primary spine, intended audience and scope, preserved invariants, prerequisites, links, outputs, recovery paths, validation coverage, and handoff.
2. **Micro economy and coherence:** after the macro structure is stable, remove sentence-level redundancy, low-value defensive negatives, repeated transitions, unsupported qualifiers, and unnecessary explanations; test every prohibition against a plausible branch and a distinct boundary; then read the package in order to confirm that every retained section earns its place and no transition jumps.

After a material edit, rerun the affected checks. If the edit changes behavior or file topology, repeat both review passes.

## Output

Always create the analysis file before changing the target. After explicit user approval, update the target skill at its authoritative path, using any repository-required branch, worktree, ticket-artifact, and finalization conventions, unless the user requests a separate copy. Update the analysis status and report:

- the files changed and the behavior preserved;
- the meaningful redundancy, flow, grounding, or structure problems corrected;
- validation performed and its result;
- remaining ambiguity or risk.

Do not add README, changelog, or quick-reference files merely as package residue or side effects; preserve existing documentation when it serves a distinct audience or owns information not present in the skill.
