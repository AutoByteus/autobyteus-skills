---
name: software-engineering-workflow-skill
description: "Run a staged software-engineering delivery feedback loop from bootstrap through investigation, requirements, design, runtime review, implementation, API/E2E and executable validation, code review, docs sync, and final handoff with durable artifacts and explicit re-entry."
---

# Software Engineering Workflow Skill

## Overview

Run a stage-gated software-engineering workflow from ticket bootstrap through final handoff.
Canonical stage map, shared references, and default artifact paths are below.
Use `shared/workflow-control.md` for transition and re-entry control.
Use the stage folders for the detailed behavior of each stage.

## Canonical Files

- `shared/workflow-control.md`
  - stage movement and re-entry control
  - workflow-state enforcement and code-edit lock rules
  - transition notifications
- `shared/design-principles.md`
  - single canonical design doctrine for Stage 3, Stage 5, and Stage 8
- `shared/workflow-state-template.md`
  - shape of the `workflow-state.md` execution-control artifact created in Stage 0 and maintained through Stage 10

## Structure

- Stage 0: ticket bootstrap and reopen rules.
- Stage 10: explicit user verification, archival, finalization, release/publication/deployment, and cleanup rules.
- `shared/workflow-control.md`: transition, re-entry, workflow-state, edit-lock, and notification rules.
- `shared/design-principles.md`: shared design doctrine for Stage 3, Stage 5, and Stage 8.
- Stage folders: detailed instructions, templates, examples, and stage-specific checks.

## Stage Map

Use `shared/workflow-control.md` for the transition contract, transition matrix, workflow-state rules, edit-lock rules, and re-entry execution rules.
Use the local stage files first. The top-level skill does not duplicate the detailed operating rules that belong to those stage owners.

| Stage | Primary Goal | Canonical Artifact(s) | Local Owner Files |
| --- | --- | --- | --- |
| 0 | bootstrap ticket context and capture draft requirement | `workflow-state.md`, `requirements.md` (`Draft`) | `stages/00-bootstrap/bootstrap-checklist.md` |
| 1 | build durable investigation context and triage scope | `investigation-notes.md` | `stages/01-investigation/investigation-guide.md`, `stages/01-investigation/investigation-notes-template.md`, `stages/01-investigation/investigation-notes-example.md` |
| 2 | refine requirements to design-ready quality | `requirements.md` | `stages/02-requirements/requirements-refinement-guide.md` |
| 3 | produce the design basis for the current scope | `implementation.md` solution sketch (`Small`) or `proposed-design.md` (`Medium/Large`) | `stages/03-design/design-guide.md`, `stages/03-design/proposed-design-template.md` |
| 4 | model future-state runtime behavior per use case | `future-state-runtime-call-stack.md` | `stages/04-future-state-runtime-call-stack/future-state-runtime-call-stack-guide.md`, `stages/04-future-state-runtime-call-stack/future-state-runtime-call-stack-template.md` |
| 5 | review future-state runtime behavior until stable | `future-state-runtime-call-stack-review.md` | `stages/05-future-state-runtime-call-stack-review/future-state-runtime-call-stack-review-guide.md`, `stages/05-future-state-runtime-call-stack-review/future-state-runtime-call-stack-review-template.md` |
| 6 | execute implementation from a reviewed baseline | `implementation.md` | `stages/06-implementation/implementation-guide.md`, `stages/06-implementation/implementation-template.md`, `stages/06-implementation/implementation-example.md` |
| 7 | implement and run executable validation | `api-e2e-testing.md` | `stages/07-api-e2e/README.md`, `stages/07-api-e2e/api-e2e-guide.md`, `stages/07-api-e2e/api-e2e-testing-template.md` |
| 8 | run independent code review | `code-review.md` | `stages/08-code-review/README.md`, `stages/08-code-review/code-review-guide.md`, `stages/08-code-review/code-review-principles.md`, `stages/08-code-review/code-review-template.md` |
| 9 | promote ticket-local truth into durable docs | `docs-sync.md` | `stages/09-docs-sync/README.md`, `stages/09-docs-sync/docs-sync-guide.md`, `stages/09-docs-sync/docs-sync-template.md` |
| 10 | handoff, wait for explicit verification, finalize, and clean up | `handoff-summary.md`, `release-notes.md` when applicable | `stages/10-handoff/README.md`, `stages/10-handoff/handoff-guide.md`, `stages/10-handoff/handoff-summary-template.md`, `stages/10-handoff/release-notes-template.md` |

## Default Artifact Paths

If the user does not specify paths, use project-local ticket artifacts under `tickets/in-progress/<ticket-name>/`:

| Stage | Default Artifact Path(s) |
| --- | --- |
| 0 | `tickets/in-progress/<ticket-name>/workflow-state.md`, `tickets/in-progress/<ticket-name>/requirements.md` |
| 1 | `tickets/in-progress/<ticket-name>/investigation-notes.md` |
| 2 | `tickets/in-progress/<ticket-name>/requirements.md` |
| 3 | `tickets/in-progress/<ticket-name>/implementation.md` (`Small`) or `tickets/in-progress/<ticket-name>/proposed-design.md` (`Medium/Large`) |
| 4 | `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack.md` |
| 5 | `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack-review.md` |
| 6 | `tickets/in-progress/<ticket-name>/implementation.md` |
| 7 | `tickets/in-progress/<ticket-name>/api-e2e-testing.md` |
| 8 | `tickets/in-progress/<ticket-name>/code-review.md` |
| 9 | `tickets/in-progress/<ticket-name>/docs-sync.md` |
| 10 | `tickets/in-progress/<ticket-name>/handoff-summary.md`, `tickets/in-progress/<ticket-name>/release-notes.md` when applicable |

After explicit user verification and Stage 10 archival, the ticket-local artifacts move under `tickets/done/<ticket-name>/`.
