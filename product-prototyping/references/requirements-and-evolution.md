# Requirements And Evolution

Use this reference to turn a prototype into precise, durable product requirements and to evolve it without losing prior decisions.

## Artifact Ownership

| Artifact | Authority |
| --- | --- |
| `product-requirements.md` | Feature-level scope, user outcomes, acceptance criteria, constraints, and non-goals |
| `experience-story.md` | User journey narrative, screen intent, and product language |
| `ui-behavior-test-matrix.md` | Canonical transition-by-transition behavior and acceptance checks |
| `prototype-assumptions.md` | Mock boundaries, simplifications, unresolved questions, and production gaps |
| `prototype-change-log.md` | History of additions, changes, removals, affected journeys, and regression evidence |
| `prototype-runbook.md` | How reviewers run and inspect the current prototype |

Do not copy the same transition table into multiple artifacts. Link to the behavior matrix when a requirement needs transition-level detail.

## Feature Record

Use a stable, never-reused ID such as `FEAT-001` or `CHANGE-014`. A compact requirement record should state:

```text
ID:
Type: add | change | remove
Status: proposed | approved | implemented | verified | deferred
User outcome:
In scope:
Out of scope:
Actors and permissions:
Entry conditions:
Acceptance criteria:
Affected screens and transition IDs:
Service boundary and data shape:
Required states: loading, success, empty, error, recovery
Responsive/accessibility/content constraints:
Visual direction and design tokens:
Open decisions and assumptions:
```

Acceptance criteria should describe observable behavior. Prefer “a failed save preserves the entered values and exposes a retry action” over “the form calls the save handler.”

Only the user or designated product owner can move a requirement to `approved`. The agent may propose, implement, verify, or defer a requirement, but must not silently treat an assumption as approved scope.

## Change Control

When extending an existing prototype, first read the current `product-requirements.md`, `experience-story.md`, `ui-behavior-test-matrix.md`, `prototype-change-log.md`, `prototype-assumptions.md`, and `prototype-runbook.md`. Then:

1. Create a never-reused feature/change ID and classify the request as `add`, `change`, or `remove`.
2. Record the request and affected feature IDs in `prototype-change-log.md`.
3. Decide whether existing behavior is preserved, intentionally changed, or removed.
4. Update `product-requirements.md` and mark the affected requirement status.
5. Update `experience-story.md` for journey or copy changes.
6. Update `ui-behavior-test-matrix.md` for transition changes and keep IDs stable where possible.
7. Update only the required scenarios, services, stores, and screens.
8. Verify the changed path plus previously accepted regression paths.
9. Record evidence, limitations, and any production implementation gap.

For removals, delete or mark obsolete behavior in every authority and remove dead UI, routes, scenarios, and documentation. Do not leave compatibility language unless the product explicitly requires it.

Keep each change-log entry compact and evidence-based:

```text
Change ID:
Revision/date:
Request:
Type: add | change | remove
Affected requirement IDs:
Affected transition IDs:
Preserved behavior:
Changed behavior:
Validation run:
Result: verified | partial | deferred
Known production gap:
```

## Requirement Precision Gate

A feature is ready for implementation discussion only when:

- its user outcome and scope are unambiguous;
- acceptance criteria are observable and testable;
- affected screens and transition IDs are identified;
- success, loading, empty, error, and recovery behavior is defined where relevant;
- service inputs, outputs, and mocked production gaps are stated;
- visual direction, hierarchy, and design-token intent are recorded;
- accessibility, responsive, content, and permission constraints are recorded;
- unrelated existing journeys have a regression check;
- unresolved decisions are visible rather than encoded as hidden assumptions.
