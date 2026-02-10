---
name: product-ui-prototyping
description: "Design and validate product UI behavior as visual state prototypes before coding. Use when tasks ask how screens should change after user actions (click, tap, submit), when non-developers need to review web/iOS/Android UX flows, or when teams need interaction-state assets and acceptance checks for implementation."
---

# Product UI Prototyping

## Overview

Turn product ideas into testable UI behavior using generated and edited screen images. Produce state-by-state visuals, click-through transition logic, and a lightweight behavior test matrix that product, design, and engineering can review before implementation.

## Prototype Folder Convention (Project-Local)

- For each prototype effort, create/use one folder under the current project's `ui-prototypes/` directory:
  - `ui-prototypes/<prototype-name>/`
- Keep all prototype artifacts in that folder so each prototype remains self-contained.
- Use clear kebab-case for `<prototype-name>`.
- Keep image assets separated by platform:
  - `ui-prototypes/<prototype-name>/images/web/<flow>/...`
  - `ui-prototypes/<prototype-name>/images/ios/<flow>/...`
  - `ui-prototypes/<prototype-name>/images/android/<flow>/...`
- Keep flow maps separated by platform and flow:
  - `ui-prototypes/<prototype-name>/flow-maps/<platform>/<flow>.json`
- Keep a manifest that maps each image to its exact generation/edit prompt:
  - `ui-prototypes/<prototype-name>/image-prompt-manifest.md`
  - `ui-prototypes/<prototype-name>/prompts/<platform>/<flow>/<screen>-<state>.md`
- If the user specifies a different location, follow the user-specified path.

## Workflow

### Tool Execution Discipline

- Execute image tool calls strictly one at a time.
- Do not run multiple generate/edit image calls in parallel for different screens/states.
- Wait for each call to finish, inspect the output, then issue the next call.
- For multi-screen/multi-state batches, process a deterministic queue sequentially.
- When calling image tools, always use absolute filesystem paths.
- Always pass an absolute `output_file_path` for generated/edited images.
- For edit calls, use absolute paths for source images.

### Aspect Ratio Discipline

- Specify an explicit aspect ratio in every image generation prompt.
- Use only supported ratios: `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `5:4`, `4:5`, `16:9`, `9:16`, `21:9`.
- For each platform + flow, keep one fixed ratio across all screens/states to avoid distortion drift.
- For edits, keep the same ratio as the baseline source image.
- Do not normalize, stretch, or re-encode generated images unless the user explicitly asks.

### 1) Define Product Intent And Constraints

- Define target platform (`web`, `ios`, `android`) and viewport assumptions.
- Define target aspect ratio per platform/flow from the supported ratio list.
- Define user personas, primary jobs-to-be-done, and critical paths.
- Define design constraints: brand tone, accessibility needs, component style, and data density.
- Define fidelity level (`wireframe`, `mid`, `high`) before generating assets.
- Define whether each flow is state-only or click-through simulation.

### 2) Map Screens, Actions, And States

- Create a state transition table for each flow:
  - `screen`
  - `trigger` (click/tap/submit/navigation/system event)
  - `from_state`
  - `to_state`
  - `expected_feedback` (visual + microcopy)
- Cover at minimum: `default`, `focus`, `pressed`, `disabled`, `loading`, `success`, `error`, and `empty` where applicable.
- Prioritize one critical flow first, then expand to secondary flows.

### 3) Create One Canonical Product Base Spec

- Build one reusable `product_base_spec` (platform, viewport, typography, spacing, tokens, accessibility intent).
- Reuse the same base spec in all generate/edit prompts to prevent style drift between screens.

### 4) Generate Baseline Screens

- Generate net-new screens with the image generation tool.
- Run generation sequentially: one screen per tool call, then review result before the next.
- Include explicit ratio in each generation prompt and keep it constant for that platform + flow.
- Use absolute `output_file_path` in every generation tool call.
- Save the exact prompt used for each generated image to:
  - `ui-prototypes/<prototype-name>/prompts/<platform>/<flow>/<screen>-default.md`
- Use deterministic style instructions and the shared base spec to keep typography, spacing, iconography, and color consistent across screens.
- Save outputs in a stable structure:
  - `ui-prototypes/<prototype-name>/images/<platform>/<flow>/<screen>-default.png`

### 5) Edit Interaction States From Baselines

- Derive state variants with the image editing tool so layout and visual identity remain stable.
- Run edits sequentially: one state update per tool call, then review result before the next.
- Preserve the source image ratio for every edit call.
- Use absolute paths for edit inputs and `output_file_path`.
- Save the exact prompt used for each edited image to:
  - `ui-prototypes/<prototype-name>/prompts/<platform>/<flow>/<screen>-<state>.md`
- Edit only state-relevant deltas:
  - Hover/focus rings
  - Pressed depth
  - Disabled contrast
  - Loading affordance
  - Validation/success/error messages
- Save outputs as:
  - `ui-prototypes/<prototype-name>/images/<platform>/<flow>/<screen>-<state>.png`

### 6) Maintain Image/Prompt Manifest (Required)

- Maintain `ui-prototypes/<prototype-name>/image-prompt-manifest.md` in real time.
- Treat this manifest as the latest source of truth (current artifact set only).
- Add one row per image artifact (`default` and each edited state).
- For each row, record at minimum:
  - `Use Case`
  - `Platform`
  - `Flow`
  - `Screen`
  - `State`
  - `Situation/Purpose`
  - `Image Path`
  - `Prompt Path`
  - `Source` (`Generate`/`Edit`)
  - `Parent Image` (for edited states)
- Ensure every image in `images/` has exactly one matching manifest row.
- Remove stale/legacy rows when images or prompts are replaced or deleted.
- Keep only active image/prompt pairs for the current prototype revision.

### 7) Connect Screens For Click-Through Simulation

- For click-through flows, create one flow map per platform+flow:
  - `ui-prototypes/<prototype-name>/flow-maps/<platform>/<flow>.json`
- Include per-link definitions:
  - `screen`
  - `trigger`
  - `hotspot` (`x`, `y`, `width`, `height`)
  - `target_screen`
  - `transition` (`instant`, `fade`, `slide`)
- Keep hotspot naming deterministic so non-developers can review and iterate quickly.

### 8) Assemble Behavior Test Matrix

- Produce `ui-prototypes/<prototype-name>/ui-behavior-test-matrix.md` with one row per transition.
- Include:
  - `flow`
  - `screen`
  - `trigger`
  - `expected next state image`
  - `acceptance check`
  - `open question / risk`
- Mark blocking issues where any trigger has ambiguous or missing feedback.

### 9) Deliver Review Package For Non-Developers

- Produce a concise review packet:
  - `ui-prototypes/<prototype-name>/ui-prototype-spec.md` with assumptions, flow summary, and behavior rules
  - `ui-prototypes/<prototype-name>/image-prompt-manifest.md` for prompt/image traceability
  - `ui-prototypes/<prototype-name>/flow-maps/<platform>/<flow>.json` for click-through linkage
  - `ui-prototypes/<prototype-name>/viewer/<platform>/<flow>/` local click-through viewer files
  - Image gallery links grouped by flow and platform
  - Explicit unresolved decisions for product/design sign-off
- Keep wording product-facing and avoid implementation jargon when possible.

### 10) Publish Local Click-Through Viewer

- For each platform+flow image set, copy the viewer template into:
  - `ui-prototypes/<prototype-name>/viewer/<platform>/<flow>/`
- Configure each viewer instance to load its matching map file:
  - `../../../flow-maps/<platform>/<flow>.json`
- Serve the workspace root locally and open:
  - `http://localhost:4173/ui-prototypes/<prototype-name>/viewer/<platform>/<flow>/index.html`
- Use per-platform/per-flow viewers for product/design review so each image set can be reviewed directly.

## Prompt Patterns And Checklists

- Read and reuse `references/prompt-patterns.md` for:
  - UX criteria coverage and product base spec
  - Production screen generation and state edit templates
  - Image/prompt manifest template and logging checklist
  - Flow-step and cross-platform adaptation templates
  - Click-through flow map template, viewer compatibility rules, and acceptance checklist

## Default Outputs

- `ui-prototypes/<prototype-name>/ui-prototype-spec.md`
- `ui-prototypes/<prototype-name>/ui-behavior-test-matrix.md`
- `ui-prototypes/<prototype-name>/image-prompt-manifest.md`
- `ui-prototypes/<prototype-name>/prompts/<platform>/<flow>/*.md`
- `ui-prototypes/<prototype-name>/flow-maps/<platform>/<flow>.json` (required for click-through simulation)
- `ui-prototypes/<prototype-name>/viewer/<platform>/<flow>/index.html`
- `ui-prototypes/<prototype-name>/viewer/<platform>/<flow>/viewer.css`
- `ui-prototypes/<prototype-name>/viewer/<platform>/<flow>/viewer.js`
- `ui-prototypes/<prototype-name>/images/web/<flow>/*.png`
- `ui-prototypes/<prototype-name>/images/ios/<flow>/*.png`
- `ui-prototypes/<prototype-name>/images/android/<flow>/*.png`

## Quality Gate

- Ensure every critical trigger produces clear, visible feedback within one state transition.
- Ensure states are visually consistent across platforms and flows.
- Ensure aspect ratio is explicitly defined and consistent for each platform + flow.
- Ensure no generated image is normalized/stretched in a way that distorts UI geometry.
- Ensure every image has a corresponding prompt record in `image-prompt-manifest.md`.
- Ensure manifest contains only latest active artifacts (no stale legacy entries).
- Ensure error and empty states include recovery guidance.
- Ensure accessibility cues (focus visibility, contrast intent, readable hierarchy) are represented in mockups.
- Ensure each click-through trigger in each flow map points to a valid target screen.
- Ensure viewer navigation works for each clickable hotspot and start screen in each platform+flow viewer.

## Handoff

- Hand off approved behavior specs and state assets to implementation.
- If engineering planning is requested next, invoke `$software-engineering-workflow-skill` with `ui-prototypes/<prototype-name>/ui-prototype-spec.md`, `ui-prototypes/<prototype-name>/ui-behavior-test-matrix.md`, relevant `ui-prototypes/<prototype-name>/flow-maps/<platform>/<flow>.json` files, `ui-prototypes/<prototype-name>/image-prompt-manifest.md`, and viewer behavior notes as inputs.
