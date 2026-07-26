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
- explanation that can be removed if it adds no decision value.

Use the ledger to distinguish useful guardrails from defensive noise. Do not catalogue filler mechanically when the skill is small, but do account for every rule whose removal could change behavior.

### 4. Diagnose the system

Check the target against the rubric for:

- package topology, ownership, and structural redundancy;
- content hierarchy, priority, and macro flow;
- unsupported or overconfident claims;
- scope drift and unnecessary platform, product, company, or project qualifiers;
- missing prerequisites or abrupt transitions;
- duplicated or contradictory rules;
- low-value negative wording;
- vague, ambiguous, or overloaded wording;
- stale references, metadata drift, and unused files;
- missing outputs, validation, recovery, or handoff behavior.

Separate a wording defect from a design defect. Reordering or shortening text cannot fix a missing owner, an ambiguous contract, or an unsupported requirement.

### 5. Edit the authoritative sources

Apply the smallest coherent edit set:

- put the main trigger, routing, and short workflow in `SKILL.md`;
- move detailed standards, variants, examples, and checklists into directly linked references;
- keep deterministic operations in scripts and output resources in assets;
- reorder content so prerequisites precede actions, actions precede outputs, validation follows the behavior it proves, and handoff follows validation;
- resolve structural redundancy first by choosing an authoritative owner or changing the file/section boundary; only then remove repeated sentences or phrases;
- replace unsupported certainty with a grounded statement, an explicit assumption, or a question;
- replace inherited host-context labels with domain terms when the label does not change behavior; retain it when the target genuinely depends on that platform and state the dependency precisely;
- make each retained instruction concrete, scoped, and easy to act on without adding explanatory noise;
- remove a negative instruction only when the positive instruction already rules out the alternative and no realistic failure, safety, authority, or ambiguity boundary is lost;
- remove duplicates and stale files only after confirming their behavior is represented by the surviving authoritative source.

Do not add a new process-state layer, package report format, helper script, or reference file solely to make the package appear more complete.

### 6. Validate the package

Review the changed package as a reader would load it:

- validate frontmatter and skill naming with the available standard skill validator;
- confirm metadata describes the actual trigger and default prompt;
- check every link and referenced path;
- check that references are directly discoverable from `SKILL.md` and do not form unnecessary deep chains;
- remove initializer placeholders and template residue; preserve literal `TODO` text when it is an intentional example or domain instruction;
- run syntax or focused checks for changed scripts when scripts exist;
- compare the baseline invariants with the optimized package.

Record limitations when a check cannot run. Do not claim a validation result that was not observed.

### 7. Perform two review passes

Always complete both passes, even when the first pass finds no issue.

1. **Macro behavior and structure:** verify package topology, file ownership, authoritative sources, content hierarchy, section priority, primary spine, intended audience and scope, preserved invariants, prerequisites, links, outputs, recovery paths, validation coverage, and handoff.
2. **Micro economy and coherence:** after the macro structure is stable, remove sentence-level redundancy, low-value defensive negatives, repeated transitions, unsupported qualifiers, and unnecessary explanations; then read the package in order to confirm that every retained section earns its place and no transition jumps.

After a material edit, rerun the affected checks. If the edit changes behavior or file topology, repeat both review passes.

## Output

Update the target skill at its authoritative path, using any repository-required branch, worktree, ticket-artifact, and finalization conventions, unless the user requests a separate copy. Report:

- the files changed and the behavior preserved;
- the meaningful redundancy, flow, grounding, or structure problems corrected;
- validation performed and its result;
- remaining ambiguity or risk.

Create a separate optimization report only when the user requests one or when durable evidence is materially useful. Do not add README, changelog, or quick-reference files merely as package residue or side effects; preserve existing documentation when it serves a distinct audience or owns information not present in the skill.
