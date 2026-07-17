---
name: software-engineering-workflow-skill
description: "Run a durable staged software engineering task workflow with ticket artifacts and git worktree setup, following each stage guide through investigation, requirements, design, implementation, validation, review, docs sync, and handoff."
---

# Software Engineering Workflow Skill

## Purpose

Use this skill for ordinary software engineering tasks that need durable stage artifacts without a separate workflow control artifact.

This skill is only a router. Each stage owns its own detailed guidance, outputs, exit condition, next step, and problem routing.

## Entry Trigger

Activate this workflow when the user request involves any of:

- **Creating, modifying, debugging, or analyzing source code** — scripts, programs, libraries, applications, tools, tests, configuration files, or build definitions
- **Designing or implementing software features** — adding, extending, refactoring, or removing behavior
- **Writing or generating code assets** — HTML games, CLI tools, API endpoints, database migrations, automation scripts, or any source-file delivery
- **Setting up or modifying software project infrastructure** — dependency configs, CI/CD, container definitions, deployment manifests

Do NOT activate this workflow when the task is purely operational or investigative without code change — file moves, data queries, read-only environment inspection, one-shot shell pipelines, text extraction, or similar shell-only tasks that do not produce durable code artifacts.

When you activate this workflow, start at `stages/00-bootstrap/stage-guide.md`.

## Task Scale & Stage Selection

Match workflow weight to task size. The goal is durable artifacts for future reference, not bureaucratic overhead.

| Task scale | Typical examples | Recommended stage coverage |
|---|---|---|
| **Small / self-contained** | Single-file script, quick prototype, one-file change, standalone creative code (e.g. HTML game in one file) | Bootstrap → Requirements → Implementation → Handoff. Create ticket folder, brief `requirements.md`, implementation notes, and handoff summary. Skip or formally skip investigation, design, formal code review, and docs sync when the scope is obvious. |
| **Medium / deliberate** | Multi-file feature, refactor, new API endpoint, cross-component change | Bootstrap → Investigation → Requirements → Design → Implementation → Validation → Handoff. Include investigation when the domain is unfamiliar or behavior is unclear. |
| **Large / multi-change** | Cross-cutting change, new service, complex debug, breaking change with migration | All stages: Bootstrap → Investigation → Requirements → Design → Implementation → Validation → Code Review → Docs Sync → Handoff |

**How to decide:** If you can confidently describe the code change, its boundaries, and the validation check in under 30 seconds of thought, the task is Small. If you need to read existing code to understand the change area, it is at least Medium. If the change touches multiple repos, services, or has breaking or data-migration implications, it is Large.

When a stage is formally skipped, record the skip in the handoff summary with a one-line rationale.

## Non-Goals

- Do not create separate workflow control artifacts.
- Do not use notification tools for stage movement.
- Do not create extra architecture review artifacts beyond the stage-owned outputs.
- Do not run commit, push, merge, release, deployment, ticket archival, or branch cleanup unless the user explicitly asks. When the user does explicitly ask for repository finalization, release, publication, or deployment, follow Stage 08's latest-base integration refresh before proceeding.

## Stage Contract

Every stage folder exposes:

- `stage-guide.md`: authoritative stage guideline.

Stage folders may also include templates/examples for richer stage artifacts owned by that stage.

When working inside a stage, follow that stage's `stage-guide.md` rather than inferring behavior from this file.

## Workflow

Start at `stages/00-bootstrap/stage-guide.md`.

Then follow the `Next Step` section in each stage guide:

1. `stages/00-bootstrap/stage-guide.md` - ticket, requirement, and worktree setup.
2. `stages/01-investigation/stage-guide.md` - understand current behavior and reduce uncertainty.
3. `stages/02-requirements/stage-guide.md` - clarify expected behavior and acceptance criteria.
4. `stages/03-design/stage-guide.md` - decide the implementation shape when design reasoning is useful.
5. `stages/04-implementation/stage-guide.md` - implement, run local verification, and inspect rendered frontend quality when the change affects UI.
6. `stages/05-executable-validation/stage-guide.md` - record executable validation evidence or no-additional-boundary rationale.
7. `stages/06-code-review/stage-guide.md` - review the changed code and validation evidence.
8. `stages/07-docs-sync/stage-guide.md` - update long-lived docs when impacted.
9. `stages/08-handoff/stage-guide.md` - summarize delivery and remaining risk; when finalization, release, publication, or deployment is explicitly requested, refresh/integrate the latest tracked remote base before proceeding.

## Shared References

- `shared/design-principles.md`: shared design and review language.
- `stages/06-code-review/code-review-principles.md`: detailed review principles.

## Artifact Policy

Create a ticket folder and durable artifacts for every reached stage.

Default ticket location:

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
- `release-notes.md` when release notes are required

Keep one canonical artifact per type. Do not create versioned duplicates by default.
