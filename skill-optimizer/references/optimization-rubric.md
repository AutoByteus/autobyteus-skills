# Skill Optimization Rubric

Use this reference after reading the target skill. It supplies the principles, tests, and paired examples behind the compact workflow in `SKILL.md`. A principle states what to preserve; a rubric test makes it reviewable.

Apply the rubric in this order: package structure and ownership -> content architecture and logical flow -> factual and behavioral grounding -> clarity and precision -> redundancy and economy. Check cross-file consistency at every level.

## 1. Map macro structure and ownership

Review the skill package as a system before reviewing individual sentences. Map the package tree, reference graph, primary instruction spine, file responsibilities, authoritative sources, and obsolete or competing artifacts.

The primary skill spine usually looks like:

`trigger -> inputs and prerequisites -> core work -> outputs -> validation and recovery -> handoff`

Ask:

- Does each file own one coherent concern?
- Is there one authoritative source for each rule, transition, schema, or quality gate?
- Do references support the main guide, or do they introduce competing workflows?
- Are files split, merged, named, and placed according to responsibility?
- Are repeated sections or files symptoms of a missing owner or wrong boundary?

Good:

```text
SKILL.md: trigger, scope, and primary workflow
references/: detailed standards and examples
scripts/: deterministic checks
assets/: output resources
agents/openai.yaml (when present): invocation metadata
```

Bad:

```text
SKILL.md, README.md, and two references each define competing workflows or duplicate quality gates.
```

Use this ownership model unless the target has a justified local convention:

| Concern | Preferred owner |
| --- | --- |
| Trigger, scope, routing, compact workflow | `SKILL.md` |
| Detailed standards, variants, examples, checklists | `references/` |
| Deterministic transformations or probes | `scripts/` |
| Files copied or used in generated output | `assets/` |
| User-facing invocation metadata, when present | `agents/openai.yaml` |

Challenge:

- a reference that is not linked from the main guide;
- a script whose behavior is described differently in prose;
- a template that encodes a rule nowhere else and is not identified as authoritative;
- multiple files that independently define the same transition, schema, or quality gate;
- a vague helper/reference file that owns no concrete concern;
- a README or quick-reference file that duplicates the skill instead of serving a real external audience.

Fix the ownership or boundary problem before deleting repeated sentences. Structural redundancy is usually an architecture signal; local wording cleanup comes later.

## 2. Map content architecture and priority

After the file topology is clear, read the content in execution order. Check whether the sections are prioritized and connected as a coherent path:

`purpose and scope -> prerequisites -> core workflow -> decisions -> outputs -> validation and recovery -> handoff -> optional detail`

Check that:

- the primary path is visible before edge cases and examples;
- prerequisites appear before dependent actions;
- core instructions are not buried under reference detail;
- optional branches are conditional and do not compete with the main path;
- each section contributes a new decision, action, constraint, output, or recovery path;
- transitions explain dependency or causality instead of decorating a jump.

Good:

```text
Purpose -> scope -> workflow -> outputs -> validate or recover -> handoff
```

Bad:

```text
Examples -> rare exceptions -> repeated checklist -> purpose -> main workflow
```

Repair section order, hierarchy, and boundaries before optimizing individual phrases.

## 3. Test logical flow

Read the skill in execution order, not only by heading. A coherent default path usually has this shape:

`trigger -> inputs and prerequisites -> main action -> outputs -> validation and recovery -> handoff`

Check that:

- the trigger establishes why the skill applies;
- prerequisites appear before the action that relies on them;
- each stage or section names its result or exit condition;
- transitions explain a real dependency, not just add connective prose;
- exceptions sit next to the action they modify;
- validation follows the behavior it proves;
- optional branches do not interrupt the main path without a clear condition;
- the final section leaves the agent with a concrete stopping point.

Flag a jump when a reader must infer a missing input, owner, decision, or next step. Repair it by adding the missing relationship or moving the content, not by adding generic transition words.

Good:

```text
Trigger -> inputs -> inspect -> edit -> validate or recover -> handoff
```

Bad:

```text
Validate the result. First decide what the skill is supposed to do.
```

The bad order asks for evidence before defining the behavior it should prove.

## 4. Check scope and audience fit

Determine what kind of skill the target is meant to be and who or what it serves. Use domain language by default. Treat platform, product, company, or project labels as justified only when they change the skill's trigger, package format, tool integration, or behavior.

Ask:

- Is this qualifier required to execute the skill, or does it only describe the environment where the skill was found?
- Does removing it broaden the wording without changing the action or output?
- Does the user's request use a general concept that the skill has narrowed without evidence?
- Are platform-specific terms confined to the actual platform-dependent instructions?

Good:

```text
Review and improve existing skills for clarity and logical flow.
```

Bad when platform behavior is not involved:

```text
Review and improve existing Codex skills for clarity and logical flow.
```

Keep the qualifier when it names a real dependency:

```text
Validate the Codex package's SKILL.md frontmatter and agents/openai.yaml metadata.
```

The first pair concerns scope. The last example concerns an actual package format and is therefore behaviorally meaningful.

## 5. Establish the behavior contract

Before judging wording, list the target skill's observable commitments:

- when it triggers and when it does not;
- what the agent reads first;
- which actions are required, optional, or forbidden;
- what files, artifacts, responses, or external effects it produces;
- what validation proves completion;
- what safety, privacy, destructive-action, accessibility, or user-approval boundaries it protects;
- how it handles ambiguity, failure, re-entry, and handoff.

Treat these commitments as invariants. A sentence may be verbose and still be necessary if deleting it changes one of them.

Before editing, record the baseline, findings, and proposed improvement plan in one user-visible analysis artifact. For every proposed change, name the affected file or boundary and classify the action as `Keep`, `Add`, `Update`, `Remove`, `Move`, `Merge`, or `Restructure`. Optimization may correctly result in deletion, relocation, consolidation, boundary changes, or no change; it is not limited to adding or updating existing files. Stop for explicit user approval after the analysis and before changing authoritative sources.

Good:

```text
Preserve the required artifact and validation steps while simplifying their wording.
```

Bad:

```text
Remove the artifact step because the workflow looks too long.
```

The bad version changes behavior without first proving that the artifact is obsolete.

## 6. Check factual grounding

For each factual or authoritative statement, identify its source:

- explicit user requirement;
- target skill or directly linked reference;
- repository instruction or observed file/tool;
- trusted external documentation;
- clearly labeled inference.

Challenge statements that:

- name a file, tool, API, path, default, or guarantee that does not exist in the inspected sources;
- convert a suggestion into a universal rule without evidence;
- claim that a stage, artifact, or integration always happens when the package makes it conditional;
- infer user intent from convenience rather than explicit scope;
- describe an outcome that the skill does not validate.

Correct them by verifying, narrowing the claim, labeling the assumption, asking a question, or removing the claim. Do not fill evidence gaps with plausible-sounding prose.

Good, after the check has actually run:

```text
The available repository validator reports `Skill is valid!`.
```

Do not write that result unless the validator was run and produced it.

Bad:

```text
The skill always creates a worktree.
```

The bad claim is invalid unless the inspected workflow makes that behavior unconditional.

## 7. Improve clarity and precision

After structure, flow, and grounding are stable, improve local wording without changing the intended behavior.

Check that:

- each instruction has a clear actor, action, object, and expected result when those details matter;
- terms are concrete and consistent with the target skill's vocabulary;
- qualifiers, conditions, and exceptions are placed next to the rule they modify;
- one sentence or bullet does not hide several unrelated decisions;
- shortening a sentence does not remove scope, evidence, or recovery information.

Good:

```text
Record the validator output after the check completes.
```

Bad:

```text
Handle validation clearly and make sure everything is correct.
```

The bad wording is vague about the actor, action, evidence, and completion condition.

## 8. Classify defensive wording

Do not remove every negative sentence. Test what branch it closes.

### Remove or rewrite low-value defense

Remove a prohibition when all of these are true:

1. The positive instruction already determines the correct action.
2. The prohibited alternative is not a realistic interpretation of the task.
3. Removing it does not weaken safety, user authority, recovery, or a required output.
4. The sentence adds no distinct decision, exception, or validation rule.

Bad low-value defense:

```text
Take bus 55. Do not take buses 27 or 28.
```

When the destination and bus choice are already unambiguous, keep `Take bus 55` and remove the second sentence.

Good necessary defense:

```text
Do not push until the user explicitly requests repository finalization.
```

This closes a real external-side-effect boundary, so it is not redundant.

### Keep or sharpen valuable defense

Keep a negative or exception when it blocks a plausible and costly mistake, such as:

- a destructive action without explicit approval;
- a security or privacy violation;
- a bypass of an authoritative boundary;
- a missing validation or recovery path;
- an unsupported claim presented as fact;
- an ambiguity where two actions are genuinely plausible;
- an obsolete path that must not remain active;
- an external side effect that the user did not authorize.

When keeping it, state the reason or boundary precisely. Prefer `Do not push until the user asks for repository finalization` to a vague collection of warnings about unrelated git actions.

## 9. Resolve remaining redundancy and authority

After the macro topology and content architecture are clear, group remaining repeated rules by meaning, not just identical wording. For each group:

1. Choose the file that owns the rule.
2. Keep the complete rule there.
3. Replace other copies with a short pointer when discoverability requires it.
4. Remove copies that add no routing value.

Look for redundancy across:

- frontmatter, `SKILL.md`, and `agents/openai.yaml`;
- the main guide and references;
- prose rules and checklists;
- templates and the instructions that describe them;
- current files and stale/deprecated files.

Do not count necessary repetition as a defect when a short reminder is required at a high-risk action boundary. The reminder should point back to the authoritative rule and add no conflicting variant.

Good:

```text
Keep one canonical transition table; link to it from the workflow guide.
```

Bad when these files have no distinct audience or contract:

```text
Copy the same transition table into the guide, reference, README, and template.
```

The bad shape creates several sources that can drift.

## 10. Review the effective skill, not just individual files

After edits, reconstruct what the agent will actually do:

- combine frontmatter trigger behavior with the body;
- follow every linked reference required by the workflow;
- inspect metadata and package topology;
- resolve conditionals and exceptions;
- check that a later rule does not contradict an earlier one;
- verify that required artifacts and validation still have an owner.

An individually polished file can still produce a confusing skill when its links, metadata, or neighboring files disagree.

Good:

```text
Frontmatter, main guide, reference, and metadata all describe the same audience and trigger.
```

Bad:

```text
Frontmatter says "skills" while the body silently restricts the task to "Codex skills".
```

## 11. Required analysis and two-pass review record

The pre-edit analysis must be written to the user-visible `optimization-analysis.md` rather than remaining only in working context. Use this record:

```text
Review Status: Analysis complete - awaiting user approval
User request and scope:
Current behavior and package ownership baseline:
Preserved invariants and user-authority boundaries:
Macro analysis:
- Package topology and ownership:
- Authoritative sources and boundaries:
- Logical flow and content architecture:
- Behavioral grounding and invariants:
- Outputs, validation, recovery, and handoff:
Micro analysis (only after macro analysis is coherent):
- Wording and terminology:
- Qualifiers, conditions, and exceptions:
- Redundancy, transitions, and economy:
Findings and evidence:
- Macro findings:
- Micro findings:
Proposed improvements:
- Macro actions, in order:
- Action (`Keep`/`Add`/`Update`/`Remove`/`Move`/`Merge`/`Restructure`):
- Affected file or boundary:
- Reason and expected effect:
- Micro actions, in order:
- Action (`Keep`/`Add`/`Update`/`Remove`/`Move`/`Merge`/`Restructure`):
- Affected file or boundary:
- Reason and expected effect:
Assumptions and open questions:
Validation plan:
Target skill files changed during analysis: None
Analysis artifact:

Post-approval implementation and validation record (fill only after approval):
- Approval recorded:
- Target files changed:
- Behavior preserved or intentionally changed:
- Validation performed and result:

Macro review pass:
- Invariants checked:
- Grounding issues:
- Flow or ownership issues:
- Cross-file issues:

Micro review pass:
- Redundancy removed:
- Defensive wording retained and why:
- Transitions repaired:
- Final residual risk:
```

Before approval, record material defects in the analysis and stop. After approval, if either pass finds a material defect, edit the authoritative source and rerun the relevant validation. Do not close the review by merely noting a known problem.
