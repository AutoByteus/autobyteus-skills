---
name: product-prototyping
description: Define, build, and evolve runnable browser-based product prototypes with Vue 3, Vite, TypeScript, Tailwind CSS, mocked service scenarios, real UI state and interaction logic, precise requirements artifacts, and browser validation. Use when a product needs to be explored before implementation, when non-technical or technical reviewers need an executable product definition, or when an existing prototype needs new features, behavior changes, or requirement updates.
---

# Product Prototyping

## Purpose

Build a production-shaped front-end prototype that lets people experience, review, and evolve a product before production backend implementation. Keep user-facing UI behavior real and simulate service boundaries with deterministic local scenarios.

Treat the prototype as a product-definition artifact. It should expose user journeys, screen behavior, states, transitions, assumptions, and unresolved decisions through an executable browser experience, not only through prose or static images.

Use “production-shaped” precisely: the prototype should have credible UI architecture, a deliberate visual direction, real state transitions, explicit service boundaries, accessibility intent, responsive behavior, and reviewable validation. It is not production-ready by default; do not imply that mocked security, persistence, integrations, scalability, observability, or backend behavior have been validated.

## Default Stack

Use these default prototype choices for new standalone prototypes, adding conditional packages only when the product behavior needs them:

- Vue 3 Single-File Components with the Composition API and TypeScript.
- Vite for project scaffolding, development, and builds.
- Tailwind CSS for styling and responsive layout.
- `@lucide/vue` for interface icons.
- Vue Router when the prototype has multiple URL-level screens or flows.
- Pinia for shared product/domain state and asynchronous service status; keep purely local presentation state in components or composables.
- Vitest and `@vue/test-utils` when focused component and state checks protect meaningful interaction logic.
- Playwright or the project's existing browser runner for critical-path smoke checks when available.

Read [vue-stack.md](references/vue-stack.md) for bootstrap commands and the default project structure. Use the existing project's package manager and scripts when working inside an existing prototype.
Read [state-and-service-architecture.md](references/state-and-service-architecture.md) when a prototype has multiple views, shared state, or asynchronous service flows. Read [requirements-and-evolution.md](references/requirements-and-evolution.md) when creating or changing features. Do not install every optional library by default; choose the smallest stack that supports the product behavior being reviewed.

## Operating Principles

- Define the product behavior before building screens, but keep the definition concise and executable.
- Make frontend state, navigation, form behavior, validation, feedback, loading, success, error, empty, and recovery behavior real.
- Fake service logic behind explicit local adapters. Do not scatter hard-coded response branches across components.
- Keep the normal data flow explicit: view/component -> store action or composable -> service adapter -> state update -> view. Store actions own shared asynchronous status; components own local visual state.
- Generate deterministic scenarios for the states that matter to product decisions, including success, validation failure, empty data, permission denial, slow response, timeout, and recoverable failure.
- Treat user corrections and supplied product facts as authoritative. Mark unknowns and assumptions instead of inventing approved behavior.
- Treat every feature addition, change, or removal as a requirements change with an explicit feature ID and a recorded impact on existing journeys.
- Keep the prototype easy for non-technical reviewers to run and understand.
- Treat aesthetic quality as a product requirement, not a final decoration pass. Match visual language to the product, audience, and use context; refine hierarchy, spacing, typography, color, surfaces, iconography, imagery, and state polish until the experience feels intentional and specific.
- Use generated or edited images only as optional visual assets, references, or content. Do not use image hotspots as the primary UI implementation.
- Preserve unrelated user changes and existing project conventions when extending an existing prototype.

## Prototype Package

For a new standalone prototype, use one self-contained folder under the current project:

`ui-prototypes/<prototype-name>/`

Keep the following artifacts in that folder:

- `product-requirements.md`: canonical feature scope, user outcomes, acceptance criteria, constraints, non-goals, and unresolved decisions.
- `experience-story.md`: product story, critical journeys, screen behavior, transitions, states, and open questions.
- `ui-behavior-test-matrix.md`: canonical prototype transitions, expected feedback, acceptance checks, and risks.
- `prototype-assumptions.md`: mocked services, deliberately simplified behavior, unresolved decisions, and production gaps.
- `prototype-change-log.md`: feature/change IDs, dates or revisions, affected journeys, implementation status, and regression evidence.
- `scenarios/`: deterministic service scenarios and review notes when more than one scenario is needed.
- Vue/Vite application files and source code.
- `prototype-runbook.md`: concise start command, review paths, scenario selection, and known limitations.
- `screenshots/` only when screenshots are useful for requirements review or comparison.

When an existing prototype already uses another package path, continue in that package rather than creating a competing folder. When an existing application is not Vue/Vite, do not rewrite it silently; create an isolated Vue prototype or ask for explicit migration permission.

For feature additions, behavior changes, and removals, follow the change-control sequence in [requirements-and-evolution.md](references/requirements-and-evolution.md) before implementation and after validation. Do not treat a new screen, component, or mock response as a complete feature until its user outcome and acceptance behavior are recorded.

## Workflow

### 1. Inspect The Target Workspace

- Confirm the active workspace and inspect current changes before editing.
- Locate the existing application, prototype package, `package.json`, lockfile, and documented commands.
- Decide whether to bootstrap a new Vue/Vite prototype or extend an existing Vue/Vite prototype.
- Preserve unrelated changes and do not replace an existing application just to force the default stack.

### 2. Define The Product Experience

Create or update `product-requirements.md` and `experience-story.md` before implementing the main flow. Use [requirements-and-evolution.md](references/requirements-and-evolution.md) for the compact feature record. Capture only the behavior needed to make the prototype meaningful:

- product story: user, goal, and observable success
- feature IDs, scope, non-goals, acceptance criteria, constraints, and open decisions
- primary journey from entry to success
- screen IDs, actions, visible feedback, and system behavior
- states required for each important action
- meaningful alternate, error, empty, loading, and recovery paths
- transition IDs and destinations
- viewport, visual direction, accessibility, content, and brand constraints
- blocking questions and explicitly stated assumptions

Prioritize one critical journey before expanding to secondary flows. Do not add a domain-specific cognitive framework unless the product itself requires one.

### 3. Define Behavior And Service Scenarios

Before building the full UI, create `ui-behavior-test-matrix.md` and define the service scenarios that support the critical journey.

For each important transition, record:

- `transition_id`
- flow, screen, trigger, `from_state`, and `to_state`
- expected visible feedback
- service scenario used
- acceptance check
- open question or risk

Identify service boundaries from the user's observable needs: authentication, search, payments, generation, file upload, notifications, permissions, or other integrations. Define their mock inputs, outputs, delays, failures, and state changes in [mock-service-scenarios.md](references/mock-service-scenarios.md).
Choose the smallest realistic scenario set from the application catalog in [mock-service-scenarios.md](references/mock-service-scenarios.md); cover the main success path plus the failures most likely to change the product decision.

Keep `product-requirements.md` as the feature-level product contract, `experience-story.md` as the user-experience intent, and `ui-behavior-test-matrix.md` as the executable transition contract. Do not maintain a second competing transition definition.

### 4. Bootstrap Or Inspect The Frontend

For a new prototype:

- scaffold Vue 3 + Vite + TypeScript in the chosen prototype folder;
- add Tailwind CSS and Lucide Vue icons;
- add Vue Router only when route-level navigation helps the review;
- add Pinia when shared product/domain state or asynchronous service status crosses views;
- add Vitest and `@vue/test-utils` when focused component/state checks will protect a meaningful interaction;
- replace the starter screen with the prototype shell before building secondary screens.

For an existing Vue/Vite prototype, inspect and reuse its current structure, design tokens, components, scripts, and dependencies. Run the smallest existing install, typecheck, lint, or build command that establishes a working baseline before changing it.

### 5. Implement The Product Surface

Build the critical journey as a real frontend:

- create a stable app shell, navigation, responsive layout, and reusable components;
- implement real UI state transitions with Vue reactivity and composables;
- connect components to mock service adapters rather than inline fake responses;
- call shared mock services through store actions or composables so components remain focused on rendering and user intent;
- represent loading, success, error, empty, disabled, and recovery states where they affect the decision;
- keep copy concrete and product-facing; do not expose implementation jargon in the reviewed product surface;
- use Tailwind for layout and styling and Lucide icons for familiar interface actions;
- define typography tokens and a readable type hierarchy; use a system font stack by default and self-host a product or brand font only when the design calls for it;
- use accessible unstyled primitives such as `@headlessui/vue` for complex menus, dialogs, listboxes, or comboboxes when local controls would create interaction risk;
- establish a coherent visual system before polishing individual screens: type scale, spacing rhythm, color roles, borders, radii, shadows, icon sizing, and interactive states;
- replace starter-template styling with domain-specific composition, copy, data density, imagery, and visual details that make the product recognizable;
- preserve keyboard focus, readable hierarchy, contrast intent, and responsive behavior;
- make scenario selection available to reviewers through a clear review control, query parameter, or documented local configuration without confusing it with a production feature.

Do not build every possible screen before validating the critical flow. Run the prototype early, inspect it, and adapt the next implementation step to observed behavior.

### 6. Validate The Runnable Prototype

Run the prototype locally and validate the actual browser experience:

- install dependencies with the project-native package manager;
- run the development server and record the review URL;
- exercise the critical journey from the documented entry point;
- run each required service scenario and verify visible feedback and recovery;
- check desktop and narrow mobile layouts;
- inspect keyboard focus, readable text, labels, and obvious accessibility failures;
- perform a visual-quality pass on the entry screen and critical states using browser screenshots at desktop and narrow mobile sizes;
- correct visual hierarchy, spacing, typography, contrast, color roles, icon consistency, alignment, loading/error/empty-state polish, and accidental overflow or overlap;
- run the project build and available typecheck, lint, unit, or browser checks;
- capture screenshots only when they help compare or communicate the result.

Read [prototype-review.md](references/prototype-review.md) for the review gate. Do not report a prototype as runnable until the start command, entry route, and critical path have been verified.

### 7. Deliver For Product Review

Update `prototype-runbook.md` with:

- install and start commands;
- local review URL and entry route;
- critical journeys to try;
- available scenarios and how to select them;
- validated states and known limitations;
- questions requiring product or design decisions.

Report what is real in the frontend, what is mocked, what was verified, and what remains outside the prototype. Keep the package easy for a product manager or non-technical reviewer to use without reading the source code.

## Quality Gate

Before handoff, verify:

- the prototype starts with the documented command;
- the critical journey is runnable from the documented entry route;
- every delivered feature/change has a requirement ID, user outcome, acceptance criteria, and change-log entry;
- `experience-story.md` and the implementation agree on screens, actions, states, and destinations;
- `product-requirements.md`, the behavior matrix, and the implementation agree about current scope and removals;
- every critical transition has visible feedback and an acceptance check;
- required service scenarios produce deterministic, reviewable outcomes;
- no service behavior is faked through scattered component-specific branches;
- loading, error, empty, disabled, and recovery states are covered where relevant;
- the visual direction is coherent, product-specific, and carried through the shell, content, controls, and important states;
- typography, spacing, color, surfaces, iconography, imagery, and component states feel deliberately designed rather than starter-template or generic;
- desktop and narrow mobile screenshots show polished composition with no avoidable overlap, clipping, awkward wrapping, or layout drift;
- desktop and narrow mobile layouts remain usable;
- keyboard focus, labels, contrast intent, and readable hierarchy are represented;
- build and available project checks pass, or failures are documented;
- mock boundaries, assumptions, and production gaps are documented;
- no unsupported product behavior is presented as approved fact.

## Handoff

Hand off the runnable prototype, `product-requirements.md`, `experience-story.md`, `ui-behavior-test-matrix.md`, `prototype-assumptions.md`, `prototype-change-log.md`, and `prototype-runbook.md` to product, design, or implementation review.

When implementation planning is requested, use the prototype artifacts as requirements evidence. Treat the prototype as an executable product definition and discovery tool, not as proof that the eventual backend or production architecture is complete.
