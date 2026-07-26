# Implementation Design

## Spine

`Skill request -> target-skill inventory -> behavior and evidence ledger -> issue classification -> authoritative edits -> cross-file validation -> two review passes -> concise handoff`

The spine starts with the target skill and ends with a verified, behavior-preserving revision. It must not stop at sentence editing because file relationships, metadata, and linked resources can change the effective skill.

## Ownership and file placement

- `skill-optimizer/SKILL.md`: trigger description, compact workflow, decision rules, review-pass sequence, and direct reference routing.
- `skill-optimizer/references/optimization-rubric.md`: macro-first tests and paired examples for topology, ownership, content architecture, logical flow, scope fit, behavior, grounding, clarity, defensive wording, duplication, and final review.
- `skill-optimizer/agents/openai.yaml`: user-facing invocation metadata only.
- No script: the work is primarily contextual judgment; generic text rewrites would risk changing behavior.
- No README or extra report template: reports are optional task output, not skill instructions.

## Change inventory

- Add: completed `SKILL.md`.
- Add: `references/optimization-rubric.md`.
- Keep: generated `agents/openai.yaml` because it matches the skill creator convention.
- Remove: initializer placeholder sections; preserve intentional `TODO` examples and domain instructions.

## Validation shape

- Run the standard skill validator.
- Check that every link in the new skill resolves and that the reference remains one level below `SKILL.md`.
- Search the package for TODO/template residue and duplicated authoritative rules.
- Perform review pass one for behavior/structure/grounding and review pass two for economy/flow/coherence.

## Implemented

- Replaced the initializer placeholder with a compact, imperative workflow in `skill-optimizer/SKILL.md`.
- Added `references/optimization-rubric.md` for detailed tests and examples.
- Added an explicit scope-and-audience-fit check to catch unnecessary host-platform wording such as `Codex skills`.
- Self-applied the optimizer and narrowed two over-broad rules: preserve intentional `TODO` examples, and record validator output only after observing it.
- Self-applied the optimizer's economy pass and changed the invariant inventory to include `any` required workflow behaviors, so unrelated skills are not forced to have worktrees or stages.
- Added macro-first gates so structural redundancy and content organization are resolved before local sentence-level cleanup.
- Self-review then aligned the primary spine and content lists to `outputs -> validation/recovery -> handoff`, moved detailed ownership guidance into the macro rubric section, removed duplicated topology examples, and placed detailed flow checks before micro wording checks.
- Added repository-boundary and external-side-effect guidance so in-place optimization does not bypass required worktrees, ticket artifacts, finalization rules, or explicit commit/push approval.
- Added an explicit priority order and clarity/precision rubric layer between grounding and redundancy, with matching guidance in the main guide and invocation metadata.
- Kept `agents/openai.yaml` aligned with the skill trigger and purpose.
- Kept the package free of scripts, assets, README files, and report templates because none owns a required deterministic operation or output resource.
