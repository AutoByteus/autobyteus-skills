# State And Service Architecture

Use this reference when a prototype has multiple screens, shared user actions, or asynchronous service behavior.

## Ownership

| Concern | Preferred owner |
| --- | --- |
| Input text, open menu, selected tab, hover, focus | component-local state |
| Reusable browser behavior | composable |
| Stable service contract and adapter construction | `services/` |
| Deterministic fake responses and delays | `mock-services/` or `scenarios/` |
| Shared records, mutations, loading, success, and error status | Pinia store |
| URL-level navigation and route params | Vue Router |

The prototype should normally follow:

```text
view/component
  -> store action or composable
  -> service interface
  -> selected mock adapter
  -> store state
  -> view/component
```

Components should not import scenario fixtures or choose mock responses directly. A scenario selector belongs at adapter construction or application setup, not inside every button handler.

## Store Rules

- Keep one store focused on one product concern, not one store for the whole app.
- Store actions own pending, success, empty, and error transitions for shared requests.
- Do not store duplicate derived values when a computed getter can derive them.
- Keep secrets and production credentials out of fixtures, local storage, logs, and screenshots.
- Make retries and repeated actions deterministic and idempotent when the product expects them to be safe.
- Keep component-only presentation state out of Pinia.

Minimal shape:

```ts
export const useProjectsStore = defineStore("projects", () => {
  const projects = ref<Project[]>([]);
  const status = ref<"idle" | "loading" | "ready" | "error">("idle");
  const error = ref<string | null>(null);

  async function loadProjects() {
    status.value = "loading";
    error.value = null;
    try {
      projects.value = await projectsService.list();
      status.value = "ready";
    } catch {
      status.value = "error";
      error.value = "Unable to load projects.";
    }
  }

  return { projects, status, error, loadProjects };
});
```

The service dependency can be injected through a factory or app-level setup so tests and scenarios replace the adapter without changing the store contract.
