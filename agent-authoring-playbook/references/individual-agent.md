# Individual Agent Track

## Goal

Create or refactor an individual agent so the role contract stays lean and the runtime skill stays explicit without duplicating the same instructions in both places.

## File Responsibilities

### `agent.md`

Keep this as the role contract only.

Recommended contents:

- short role identity
- short responsibility statement
- produced artifact or artifacts
- core ownership bullets
- communication edges
- tone

Do not put detailed runtime behavior here unless it is truly part of the role contract and would still make sense without the skill.

### `SKILL.md`

Keep this as the runtime playbook.

Recommended contents:

- purpose
- what the role owns at runtime
- primary output and template usage
- artifact-writing rules
- required reads
- ordered execution behavior
- review, validation, or classification logic
- reroute and re-entry rules
- detailed handoff payload expectations

## Clean Split Rule

Use this test:

- If the sentence answers "who is this role and what does it own?", keep it in `agent.md`.
- If the sentence answers "how exactly should the role execute?", keep it in `SKILL.md`.

## Typical Problems To Remove

- the same handoff nuance repeated in both files
- the same checklist repeated in both files
- the same review or validation standard repeated in both files
- the same artifact-writing rule repeated in both files
- examples or terminology blocks duplicated in both files

## Runtime Self-Containment

If the skill runtime expects self-contained instructions:

- keep runtime-critical instructions in `SKILL.md`
- keep referenced runtime-critical files inside the skill folder
- do not depend on unrelated external folders for required execution context unless the runtime is known to support it reliably

## Recommended Authoring Order

1. Read the current `agent.md`, `SKILL.md`, templates, and local references.
2. Decide what is role contract versus runtime playbook.
3. Cut `agent.md` down first.
4. Move or preserve detailed execution logic in `SKILL.md`.
5. Re-check for duplicated routing, artifact, and classification rules.
6. Confirm the resulting pair still fully describes the role without prompt bloat.

## Final Checklist

- `agent.md` is short enough to read as a contract, not a manual.
- `SKILL.md` contains the actual execution logic.
- The same doctrine is not explained twice.
- Artifact ownership is explicit.
- Handoff targets are explicit.
- The runtime-critical reads are inside the skill surface or clearly local to it.

