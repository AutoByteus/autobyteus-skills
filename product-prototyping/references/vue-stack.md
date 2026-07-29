# Vue Prototype Stack

Use this reference when bootstrapping a new standalone prototype or checking whether an existing prototype follows the default stack.

## Default Choices

- Vue 3 with Single-File Components, Composition API, and TypeScript.
- Vite with the `vue-ts` template.
- Tailwind CSS for layout, responsive behavior, and visual styling.
- `@lucide/vue` for interface actions.
- Vue Router for multiple URL-level views or flows.
- Pinia for shared product/domain state and async service status; use composables and component state for local concerns.
- Vitest plus `@vue/test-utils` for focused component and state tests when the prototype has non-trivial interaction logic.
- Playwright or an existing browser runner for critical-path checks.

Use the versions and package manager already selected by the target project. Do not mix Tailwind setup generations or replace an existing package manager lockfile without a reason.

## Typography And Fonts

- Start with a system UI font stack so the prototype has no external font dependency and renders consistently offline.
- Add a product or brand font only when typography is part of the design decision. Prefer a self-hosted package such as Fontsource or a checked-in licensed font asset over a runtime Google Fonts request.
- Define font family, weight, size, line-height, and tracking as a small token set. Keep body text, labels, controls, headings, and display type visibly distinct without excessive type scale.
- Load only the weights and styles the prototype uses. Verify long labels and localized text at narrow widths.

## New Project Bootstrap

From the directory that should contain the prototype:

```bash
npm create vite@latest <prototype-name> -- --template vue-ts
cd <prototype-name>
npm install
npm install @lucide/vue
npm install tailwindcss @tailwindcss/vite
```

Add the behavior-driven packages only when the prototype needs them:

```bash
npm install vue-router pinia
npm install -D vitest @vue/test-utils
```

For a single-screen flow, local component state and a mock service may be enough. Add only the packages that represent real product behavior or reduce a concrete interaction risk.

Configure the Tailwind Vite plugin in `vite.config.ts` and import Tailwind in the main stylesheet according to the installed Tailwind version. For the current Vite-plugin setup, the key pieces are:

```ts
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [vue(), tailwindcss()],
});
```

```css
@import "tailwindcss";
```

Run the generated project before making product changes:

```bash
npm run dev
npm run build
```

Use the project's own scripts when they differ. Vite performs TypeScript transpilation but does not replace a separate typecheck; run the repository's configured typecheck when available.

## Recommended Prototype Structure

```text
src/
  assets/
  components/       # reusable product UI components
  composables/      # reusable UI behavior and state
  layouts/          # product shell and navigation
  services/         # stable service interfaces and factories
  mock-services/    # service interfaces and scenario adapters
  router/           # route definitions when needed
  scenarios/        # deterministic review scenarios
  stores/           # Pinia stores for shared domain state and async service status
  views/            # route-level product screens
  App.vue
  main.ts
```

Keep mock service calls behind small interfaces so the frontend can later replace an adapter without rewriting components. Keep scenario data near the adapter, not embedded in visual components.

For multi-view flows, prefer this boundary:

```text
component/view -> Pinia store action -> service adapter -> store state -> component/view
```

See [state-and-service-architecture.md](state-and-service-architecture.md) for ownership rules and a minimal store example.

## Stack Boundaries

- Do not add a backend, database, authentication provider, or production API solely to make a prototype run.
- Do not add a component library when Tailwind and a few local components are sufficient.
- Do not add every library in this document by default. Add each dependency only when it removes real prototype risk or represents an important product decision.
- Use `@headlessui/vue` for complex accessible primitives when needed; keep application-specific styling in Tailwind and local components.
- Use `@vueuse/core` for repeated browser/composition utilities instead of writing one-off lifecycle or storage helpers.
- Use `vee-validate` with `zod` for complex forms with cross-field rules; simple forms should use native Vue state and validation.
- Use `@tanstack/vue-query` only when the prototype must demonstrate server-state caching, refetching, invalidation, or optimistic updates. Mock service adapters remain the boundary.
- Use one primary component/primitive approach. Do not combine a full UI kit with Headless UI or duplicate competing component systems unless the existing product already requires it.
- Use supplied project design tokens or components when extending an existing prototype.
- Keep production integration gaps explicit in `prototype-assumptions.md`.

## Official References

- [Vue quick start](https://vuejs.org/guide/quick-start.html)
- [Vite getting started](https://vite.dev/guide/)
- [Tailwind CSS with Vite](https://tailwindcss.com/docs/installation/using-vite)
- [Vue Router](https://router.vuejs.org/guide/)
- [Pinia](https://pinia.vuejs.org/introduction.html)
- [VueUse](https://vueuse.org/guide/)
- [Vitest](https://vitest.dev/guide/)
- [Vue Test Utils](https://test-utils.vuejs.org/guide/)
- [Playwright](https://playwright.dev/docs/running-tests)
- [Fontsource](https://fontsource.org/)
