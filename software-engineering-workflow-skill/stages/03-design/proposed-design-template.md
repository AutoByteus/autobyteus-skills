# Proposed Design

Use this template only when a short solution sketch is not enough.

Write to:
- `tickets/in-progress/<ticket-name>/proposed-design.md`

## Design Meta

- Ticket:
- Date:
- Source requirements:
- Source investigation notes:
- Shared principles: `shared/design-principles.md`

## Goal

- Intended change:
- In scope:
- Out of scope:

## Current State

- Relevant entrypoints:
- Current owners/boundaries:
- Current coupling or placement issues:
- Relevant files:
- Constraints or unknowns:

## Target Design Summary

- Chosen direction:
- Why this direction:
- Main behavior/data-flow:
- Key ownership decision:
- Key validation expectation:

## Data-Flow Spine

Write the important flow as a short chain.

Example:
- `UI action -> API handler -> domain service -> repository -> persisted result`

| Spine ID | Flow | Why It Matters | Owner |
| --- | --- | --- | --- |
| DS-001 |  |  |  |

## Ownership And Boundaries

| Owner / Boundary | Owns | Must Not Own | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

Checks:

- The primary owner is clear.
- Off-spine concerns have explicit owners.
- Callers use the authoritative public boundary instead of depending on that boundary and its internals at the same time.
- Dependency direction follows ownership.

## File And Interface Plan

| File / Interface | Action (`Add`/`Modify`/`Move`/`Remove`) | Responsibility | Owner | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Checks:

- File paths match owning concerns.
- Names match responsibilities.
- Interfaces expose one clear subject and explicit identity shape.
- Shared structures are tight and not overloaded with unrelated optional fields.

## Cleanup Plan

| Item To Remove / Rename / Move | Why | Replacement / New Owner | Verification |
| --- | --- | --- | --- |
|  |  |  |  |

## Validation Plan

| Acceptance Criterion / Behavior | Verification Method | Durable Asset Needed? | Notes |
| --- | --- | --- | --- |
|  | Unit / Integration / Executable / Review | Yes/No |  |

## Risks And Open Questions

| Risk / Question | Impact | Resolution |
| --- | --- | --- |
|  |  |  |

## Design Decision

- Decision: `Proceed` / `Revise` / `Blocked`
- Rationale:
- Next step:
