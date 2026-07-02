---
name: software-engineering-workflow-skill
description: "Run a lean software engineering task workflow by starting at setup and following each stage guide through investigation, requirements, design, implementation, validation, review, docs sync, and handoff."
---

# Software Engineering Workflow Skill

## Purpose

Use this skill for ordinary software engineering tasks that need disciplined execution without a heavy workflow control plane.

This skill is only a router. Each stage owns its own detailed guidance, outputs, exit condition, next step, and problem routing.

## Non-Goals

- Do not create process-control artifacts.
- Do not require a dedicated branch or worktree.
- Do not use notification tools for stage movement.
- Do not create extra architecture review artifacts beyond the stage-owned outputs.
- Do not run commit, push, merge, release, deployment, ticket archival, or branch cleanup unless the user explicitly asks.

## Stage Contract

Every stage folder should expose:

- `stage-guide.md`: authoritative stage guideline.
- optional templates/examples for artifacts owned by that stage.

When working inside a stage, follow that stage's `stage-guide.md` rather than inferring behavior from this file.

## Workflow

Start at `stages/00-bootstrap/stage-guide.md`.

Then follow the `Next Step` section in each stage guide:

1. `stages/00-bootstrap/stage-guide.md` - lightweight setup and artifact decision.
2. `stages/01-investigation/stage-guide.md` - understand current behavior and reduce uncertainty.
3. `stages/02-requirements/stage-guide.md` - clarify expected behavior and acceptance criteria.
4. `stages/03-design/stage-guide.md` - decide the implementation shape when design reasoning is useful.
5. `stages/04-implementation/stage-guide.md` - implement and run local verification.
6. `stages/05-executable-validation/stage-guide.md` - prove behavior across real executable boundaries when needed.
7. `stages/06-code-review/stage-guide.md` - review the changed code and validation evidence.
8. `stages/07-docs-sync/stage-guide.md` - update long-lived docs when impacted.
9. `stages/08-handoff/stage-guide.md` - summarize delivery and remaining risk.

## Shared References

- `shared/design-principles.md`: shared design and review language.
- `stages/06-code-review/code-review-principles.md`: detailed review principles.

## Artifact Policy

Create ticket artifacts only when they materially help the task or the user asks for them.

Default ticket location when artifacts are useful:

- `tickets/in-progress/<ticket-name>/`

Common artifact names:

- `requirements.md`
- `investigation-notes.md`
- `proposed-design.md`
- `implementation.md`
- `executable-validation.md`
- `code-review.md`
- `docs-sync.md`
- `handoff-summary.md`

Keep one canonical artifact per type. Do not create versioned duplicates by default.
