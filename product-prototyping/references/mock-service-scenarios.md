# Mock Service Scenarios

Use this reference to simulate backend and integration behavior while keeping the frontend behavior real.

## Boundary Pattern

Define a small service interface from the user's observable need, then provide a deterministic local adapter.

```ts
export interface SearchService {
  search(query: string): Promise<SearchResult>;
}

export function createSearchService(scenario: SearchScenario): SearchService {
  return {
    async search(query) {
      await wait(scenario.delayMs);
      if (scenario.error) throw scenario.error;
      return scenario.result(query);
    },
  };
}
```

Keep the interface stable while changing scenarios. Components should call the service and handle its states; they should not know which scenario generated the response.

## Typical Application Scenario Catalog

Select scenarios from the product's actual service boundaries. The catalog is a menu, not a requirement to implement every state.

| Product boundary | Useful scenario set |
| --- | --- |
| Identity and access | signed out, sign-in success, invalid credentials, expired session, role denied, invitation pending |
| Lists and search | populated, empty, slow response, no match, pagination, service failure |
| Create and edit | valid save, field validation, duplicate/conflict, unsaved changes, save success, save failure |
| Detail and delete | loaded, missing record, delete success, delete rejected, undo or recovery |
| Plans and payments | checkout success, declined payment, pending, canceled, plan limit |
| Files and imports | upload progress, invalid file, duplicate, partial result, queue failure, download failure |
| Collaboration | invitation, comment success, stale update, permission change, concurrent edit conflict |
| Notifications and live updates | unread items, mark read, reconnect, stale data, refresh failure |
| AI and generation | queued, streaming or partial, complete, unsupported input, moderation block, retry |
| Long-running work | queued, running, completed, failed, canceled, retry |

For most product reviews, implement one representative success path and two to four risky states. Add more only when they change an important decision or expose a separate UI contract.

## Scenario Coverage

Choose scenarios that affect product decisions. Common categories include:

| Scenario | What the UI must demonstrate |
| --- | --- |
| `success` | normal result, confirmation, or next-step navigation |
| `validation-error` | field-level or form-level correction path |
| `empty` | no-result explanation and useful next action |
| `loading` | progress feedback without duplicate submission |
| `slow-response` | the experience while waiting and any cancel/retry behavior |
| `permission-denied` | explanation, safe fallback, and destination |
| `timeout` | recoverable failure and retry behavior |
| `service-error` | failure copy, support path, or safe recovery |
| `partial-data` | incomplete content and what remains actionable |
| `long-running` | intermediate progress and completion/failure outcomes |

Do not add every scenario by habit. Include the smallest set that can change a product decision or expose a risky assumption.

## Scenario Selection

Use one of these approaches:

- a documented default scenario for the main review path;
- a query parameter such as `?scenario=timeout` for deterministic testing;
- a clearly labeled local review control when non-technical reviewers need to switch scenarios;
- a test-only factory or fixture when scenario selection should stay out of the visible prototype.

Do not present development-only scenario controls as production product features. Document how reviewers access them in `prototype-runbook.md`.

## Service Rules

- Keep delays deterministic and short enough for review.
- Keep fixtures small but representative: include enough records to show hierarchy, long labels, empty states, and relevant edge cases; generate large volumes only when scale, pagination, or virtualization is part of the product decision.
- Return realistic data shapes, labels, and quantities rather than generic placeholder values.
- Use synthetic values only. Never put real credentials, personal data, customer data, or production exports in fixtures, screenshots, logs, or local storage.
- Keep error categories distinct when the UI should respond differently.
- Make repeated actions idempotent in the mock where the product expects retry behavior.
- Simulate persistence locally only when it changes the journey; do not create a fake database by default.
- Record service assumptions and missing production semantics in `prototype-assumptions.md`.
- Never use mock responses to silently approve an unconfirmed product rule. Mark the rule as an assumption.

## Review Evidence

For each scenario used in a critical journey, record:

- scenario name and purpose;
- service boundary being simulated;
- input and output shape;
- visible UI states and recovery behavior;
- whether the scenario was exercised in the browser;
- remaining production integration gap.
