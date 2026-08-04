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

## Follow-up self-optimization review: low-value noise detection

Review Status: Approved - implementation complete
Review date: 2026-08-04

### User request and scope

The user identified a sentence in an article-writing skill that says, in effect:

> Use the bundled research skill when needed; do not add another research agent or another writing skill.

The first clause is useful routing. The second clause answers an unasked question and prohibits work that the user was not considering. The user wants the optimizer to detect this kind of irrelevant defensive language reliably and to include concrete examples in its rubric.

Scope is limited to the optimizer package itself:

- `skill-optimizer/SKILL.md`;
- `skill-optimizer/references/optimization-rubric.md`;
- the existing self-analysis artifact and metadata only where consistency requires it.

No article-writing files or other repositories are in scope for this self-optimization pass.

### Current behavior and package ownership baseline

The optimizer already has relevant controls:

- `SKILL.md` asks for clarity, precision, redundancy, economy, and low-value negative wording checks.
- The instruction ledger classifies rules as core action, constraint, exception/recovery, validation gate, or removable explanation.
- The rubric's defensive-wording section says to remove a prohibition when the positive instruction is sufficient, the alternative is not realistic, and no safety or authority boundary is lost.
- The rubric includes a generic bus-choice example and examples of necessary destructive-action defenses.

The gap is specificity and auditability. The rubric does not explicitly test whether a prohibition merely blocks an unrequested action that the target workflow does not plausibly invite. It also does not include the exact “do not add another agent/skill” pattern, so an optimizer can classify that sentence as a package-ownership safeguard and preserve it even when it adds no runtime decision value.

### Preserved invariants and user-authority boundaries

Any approved change must preserve:

- safety, privacy, destructive-action, security, user-approval, and external-side-effect boundaries;
- realistic ambiguity handling and recovery paths;
- package topology, ownership, cross-file consistency, and stale-reference checks;
- the analysis-before-editing and explicit-approval contract;
- the action taxonomy: `Keep`, `Add`, `Update`, `Remove`, `Move`, `Merge`, `Restructure`;
- the macro-before-micro review order;
- the ability to retain a negative instruction when it closes a plausible, costly, or authoritative failure path.

The intended behavior change is only to improve detection of low-value noise. It must not turn the optimizer into a blind positive-language rewriter.

## Macro analysis

### Package structure and ownership

**Finding SELF-M-1 — Medium — the noise rule is split between the main procedure and rubric without a named decision gate.**

The main skill mentions low-value defensive wording, while the rubric explains it under defensive wording, but neither names a dedicated “normal-path relevance” or “unasked branch” test. The instruction ledger also has no explicit category for a prohibition that does not change behavior.

Impact: the optimizer may notice the sentence but fail to classify it as removable noise, especially when the sentence uses package or ownership vocabulary such as “agent,” “skill,” “workflow,” or “do not add.”

**Finding SELF-M-2 — Low — the existing example is too generic for agent-skill authoring.**

The bus example proves the general principle, but it does not cover a common skill-writing failure: explaining package architecture inside a runtime skill when the positive routing instruction is already sufficient.

Impact: future optimizations can repeat the same preservation error even though the general rubric principle is technically present.

### Content architecture and logical flow

The effective optimizer path should make the economy decision explicit:

`read instruction -> identify normal action -> test each prohibition against a plausible branch -> preserve only distinct boundaries -> rewrite/remove noise`

The current flow reaches this decision indirectly through general micro analysis. A named test should run after the macro behavior contract is established and before sentence-level wording is accepted.

### Behavioral grounding, outputs, validation, recovery, and handoff

The proposed check is grounded in the optimizer’s existing purpose: preserve behavior while removing unnecessary instructions. It does not require a new artifact, script, or process state. The output remains the same user-visible analysis report and approved target edits.

When a sentence is ambiguous, the optimizer should record the uncertainty rather than remove it. When the sentence protects a real external side effect, safety boundary, approval boundary, or plausible misroute, it remains. When it only says not to invent unrequested package components, it is normally removable or belongs in package/team documentation rather than the runtime skill.

## Micro analysis

### Wording and terminology

Add stable terms:

- **normal-path relevance:** does this sentence affect the requested run?
- **plausible-branch test:** what realistic mistake does this prohibition prevent?
- **unasked-work test:** is it warning against work the user did not request and the workflow does not invite?
- **distinct-boundary test:** does removal weaken safety, authority, recovery, validation, or ownership?

### Qualifiers and exceptions

The new test must explicitly preserve negative instructions for:

- destructive or external actions;
- security, privacy, or authorization boundaries;
- genuinely ambiguous branches;
- required artifacts or validation;
- obsolete paths that must not remain active;
- realistic scope drift that the target workflow could otherwise cause.

It should flag as noise a sentence that merely says not to create another agent, skill, file, process, or workflow when the user did not request that work, the package already defines the owner, and the positive instruction already routes the task correctly.

### Redundancy and economy

The new rule should live primarily in `optimization-rubric.md`, with one short cross-reference in `SKILL.md`. The exact example should live in the rubric, not be copied into the main workflow or metadata.

## Findings and evidence summary

- **SELF-M-1 Medium:** no named normal-path/unasked-branch gate for defensive noise.
- **SELF-M-2 Low:** existing examples do not cover “do not add another agent/skill” package-noise language.
- **SELF-micro Medium:** the current rule can be interpreted as a general style preference instead of a behavior-preserving classification test.

## Proposed improvements

### Macro actions

1. **Update — `skill-optimizer/SKILL.md`**
   - Add an instruction-ledger classification for low-value noise: a sentence that closes no plausible branch and changes no output, safety boundary, authority rule, recovery path, or validation requirement.
   - Add a micro-pass test: ask what realistic mistake a prohibition prevents; if the answer is “none” or only “work the user never requested,” remove or move it.
   - Keep the existing preservation rule for safety, authority, ambiguity, recovery, validation, and external side effects.

2. **Update — `skill-optimizer/references/optimization-rubric.md`**
   - Add a named `Normal-path relevance and unasked-work test` under defensive wording.
   - Add the exact paired example:

     ```text
     Keep: Use the bundled research skill when source investigation is needed.
     Remove from the runtime skill: Do not add another research agent or another writing skill.
     ```

   - Explain that package architecture belongs in package/team ownership documentation unless it changes runtime behavior.
   - Add a second paired example showing a necessary negative boundary, such as explicit approval before pushing or deleting files.

3. **Keep — `skill-optimizer/agents/openai.yaml`**
   - No metadata or invocation change is needed.

### Micro actions

1. Replace vague “defensive noise” wording with the three concrete tests: normal-path relevance, plausible branch, and distinct boundary.
2. Require the analysis report to identify removed or retained prohibitions and the branch each one closes.
3. Preserve concise positive instructions when they already determine the correct action.

### Action classification summary

- **Keep:** current macro-before-micro order, behavior contract, approval boundary, action taxonomy, safety exceptions, and existing examples.
- **Add:** explicit normal-path relevance, plausible-branch, unasked-work, and distinct-boundary tests plus agent/skill-specific examples.
- **Update:** `SKILL.md` and `optimization-rubric.md` wording and micro-pass contract.
- **Remove:** no existing safety rule; remove only ambiguity that allows routine package-architecture prohibitions to survive as runtime instructions.
- **Move:** package-only “do not add another agent/skill” constraints should move to package/team documentation when they are needed at all.
- **Merge:** combine existing low-value-negative and defensive-wording guidance under the named noise-detection test.
- **Restructure:** make noise classification an explicit micro-pass gate rather than an optional interpretation.

## Assumptions, open questions, risks, and validation plan

### Assumptions

- The user wants the reusable optimizer skill improved for future audits, not only the article-writing skill corrected again.
- The existing optimizer repository is the authoritative location for this skill.
- The user accepts a new rubric example and decision test without adding a separate workflow stage or artifact.

### Open questions

- None block the proposed change. The only implementation choice is whether the exact example belongs in the rubric or main skill; the recommendation is rubric only with a short main-skill cross-reference.

### Risks

- Over-aggressive noise removal could delete a real package, safety, or authority boundary. The distinct-boundary test prevents this.
- The phrase “unasked work” must not suppress useful scope constraints when a workflow realistically invites the wrong action. The plausible-branch test preserves those cases.
- Adding more rubric prose could itself become noise. Keep the new section short and example-led.

### Validation plan after approval

1. Validate optimizer frontmatter, metadata, links, and package topology.
2. Verify the new tests and paired examples appear once in the authoritative rubric and are discoverable from `SKILL.md`.
3. Apply the new test to the article-writing example and confirm it classifies the routing sentence as `Keep` and the unasked agent/skill prohibition as `Remove` or `Move`.
4. Apply the same test to necessary external-side-effect, security, approval, and recovery examples and confirm they remain `Keep`.
5. Run `git diff --check` and any available standard validator.
6. Perform macro and micro review passes, including a self-noise audit of the optimizer changes.

Target skill files changed during analysis: None

Analysis artifact: `/Users/normy/autobyteus_org/autobyteus-skills/skill-optimizer/optimization-analysis.md`

### Post-approval implementation and validation record

- Approval recorded: User approved implementation by requesting the optimizer update and asking for the article-writing example to be added as a negative example.
- Target files changed: `skill-optimizer/SKILL.md`, `skill-optimizer/references/optimization-rubric.md`, and this review artifact.
- Behavior preserved or intentionally changed: Existing macro-before-micro review order, analysis-before-edit approval gate, safety and user-authority boundaries, and action taxonomy are preserved. The micro review now requires an explicit normal-path, plausible-branch, unasked-work, and distinct-boundary decision for each prohibition.
- Validation performed and result:
  - Confirmed the rubric is linked from `SKILL.md` and the new named test is present in the authoritative reference.
  - Confirmed the article-writing pair classifies the routing sentence as `Keep` and the unasked agent/skill prohibition as `Remove` or `Move`.
  - Confirmed external-side-effect and security/approval categories remain protected by the retained-defense guidance.
  - Ran `git diff --check`: passed.
  - Ran frontmatter/link/package checks: passed by focused inspection; no repository-specific standard validator was present in the package.

### Macro review pass

- Invariants checked: package ownership, analysis-before-edit approval, macro-before-micro order, safety, authority, validation, recovery, and output boundaries.
- Grounding issues: none introduced.
- Flow or ownership issues: the new noise test is placed in the micro review path and the detailed examples remain in the rubric.
- Cross-file issues: none found; `SKILL.md` points to the rubric as the detailed source.

### Micro review pass

- Redundancy removed: no existing safety guidance was removed; the new wording makes the existing low-value-negative rule operational.
- Defensive wording retained and why: external side effects, security/privacy, destructive actions, unsupported claims, required outputs/validation, ambiguity, and obsolete paths remain protected.
- Transitions repaired: the micro pass now explicitly tests each prohibition before final economy cleanup.
- Final residual risk: an unusual workflow may still require judgment about whether a branch is plausible; the analysis must record that uncertainty rather than silently deleting the rule.
