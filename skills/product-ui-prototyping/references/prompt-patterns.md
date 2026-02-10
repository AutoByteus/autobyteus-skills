# Prompt Patterns

Use these patterns to produce production-quality UI images, not rough concepts.

## 1) UX Criteria Coverage

Encode these criteria in prompts whenever possible:

- User goal: what job the user is trying to complete on this screen.
- Context: where the user came from and what decision they must make now.
- Platform rules: web, iOS, or Android conventions and viewport dimensions.
- Aspect ratio: explicit ratio selection per platform/flow from supported set.
- Information hierarchy: what is primary, secondary, and tertiary.
- Design system: spacing scale, typography scale, radius, elevation, tokenized colors.
- Component behavior: button/input/nav states and feedback expectations.
- Data realism: realistic labels, values, errors, and empty states.
- Accessibility intent: visible focus, readable contrast, legible text sizes, touch targets.
- Tone and brand: visual personality and copy tone boundaries.
- Acceptance checks: objective pass/fail criteria for the generated screen.

## 2) Product Base Spec (Reuse Across All Screens)

Create one canonical base spec and append it to every generation/edit prompt.

```text
Product name: {name}
Product domain: {fintech|healthcare|ecommerce|saas|...}
Persona: {role + experience level}
Primary user jobs: {job_1, job_2}
Brand tone: {professional|friendly|premium|playful|...}

Platform target: {web|ios|android}
Viewport: {e.g., 1440x1024 web, 390x844 ios, 412x915 android}
Aspect ratio: {1:1|4:3|3:4|3:2|2:3|5:4|4:5|16:9|9:16|21:9}
Density mode: {compact|comfortable}
Localization: {language + region}

Design system constraints:
- Grid: {12-col web / 4-col iOS/Android}
- Spacing scale: {4/8/12/16/24/32}
- Type scale: {sizes + line heights + weights}
- Radius tokens: {sm/md/lg}
- Elevation tokens: {level definitions}
- Color tokens: {primary/neutral/success/warning/error hex or token names}
- Icon style: {outline/filled + stroke weight}

Accessibility intent:
- Visible focus indicators for keyboard/touch navigation contexts
- Contrast target suitable for body and actionable text
- Minimum touch target intent for mobile controls
```

## 3) Production Screen Generation Template

Use for first-pass high-fidelity screens.

```text
Create a production-ready {platform} UI screen image.

Screen contract:
- Screen name: {screen_name}
- User goal on this screen: {goal}
- Entry context: {how user arrived}
- Required components: {component list}
- Primary action: {cta}
- Secondary actions: {secondary actions}
- Content blocks with priority: {ordered list}
- State to render: {default|loading|empty|error|success}
- Aspect ratio: {one supported ratio; keep constant for this platform + flow}

Behavior expectations:
- Show clear affordance for all clickable/tappable elements.
- Reflect the current state with explicit visual feedback.
- Use realistic product copy and plausible data values (no lorem ipsum).
- Preserve consistent spacing and alignment with the provided design system.

Hard constraints:
- No watermark
- No device frame
- No decorative scene outside the app UI
- No unexplained style drift from base spec
- Do not normalize/stretch/re-encode the output image unless explicitly requested
- Use absolute filesystem path for tool `output_file_path`

Apply base spec exactly:
{product_base_spec}
```

## 4) State Transition Edit Template

Use to convert one existing screen image into the next state.

```text
Edit this UI screen for trigger: {trigger}.
From state: {from_state}
To state: {to_state}

Keep unchanged:
- Layout structure
- Visual style language
- Typography scale
- Spacing rhythm
- Component shapes
- Aspect ratio (must match source image)

Change only:
- {delta_1}
- {delta_2}
- {delta_3}

Expected user feedback after trigger:
{one-sentence outcome}

Output one clean updated screen image.

Tool call path rules:
- Use absolute paths for edit input images.
- Use absolute filesystem path for tool `output_file_path`.
```

## 5) Flow-Step Generation Template

Use when a user action should navigate to a new screen/modal/sheet.

```text
Starting from this source screen, generate the immediate next UI step after action: {trigger}.

Next-step requirements:
- Destination context: {new page/modal/sheet name}
- Persisted information from previous screen: {data to carry forward}
- New decision required from user: {decision}
- Visual continuity: maintain same brand and component language
- State rendered on arrival: {default|loading|error|success}

Apply base spec exactly:
{product_base_spec}
```

## 6) Cross-Platform Adaptation Template

Use to map the same flow across web, iOS, and Android.

```text
Adapt this screen from {source_platform} to {target_platform}.

Preserve:
- Information hierarchy
- Interaction meaning
- Brand style and tone

Adjust for target platform:
- Navigation paradigm
- Input and keyboard behavior
- Touch target sizing and spacing
- Safe-area and viewport constraints

Output one production-ready adapted screen image.
```

## 7) UX Designer Acceptance Checklist

Accept output only if all criteria pass:

- Goal clarity: user can tell the primary action within 3 seconds.
- Hierarchy: key content appears first, supporting content is clearly secondary.
- Alignment: no visible spacing rhythm breaks or misaligned controls.
- System consistency: components match one coherent design language.
- State clarity: loading/error/success/disabled cues are unmistakable.
- Copy quality: labels and messages are realistic and product-appropriate.
- Accessibility intent: focus, contrast, legibility, and touch intent are visible.
- Flow continuity: current screen logically connects to previous/next states.

## 8) Prompting Anti-Patterns

Avoid these patterns because they lower quality:

- Vague requests such as "make it modern" without constraints.
- Missing platform/viewport, causing unstable layout choices.
- Mixing multiple visual styles in one prompt.
- Allowing placeholder text/data for final-quality images.
- Requesting too many state changes in one edit operation.
- Omitting hard constraints that prevent watermarks/device chrome.

## 9) Image/Prompt Manifest Template

Use this to keep prompt-to-image traceability for every generated or edited artifact.

File location:
- `ui-prototypes/<prototype-name>/image-prompt-manifest.md`

Recommended table:

| Artifact ID | Use Case | Platform | Flow | Screen | State | Situation/Purpose | Source (`Generate`/`Edit`) | Parent Image | Image Path | Prompt Path | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 | Checkout happy path | web | checkout | cart | default | Cart view before submit | Generate | N/A | `ui-prototypes/<prototype-name>/images/web/checkout/cart-default.png` | `ui-prototypes/<prototype-name>/prompts/web/checkout/cart-default.md` |  |
| A-002 | Checkout happy path | web | checkout | checkout | loading | Show pending payment processing | Edit | `.../cart-default.png` | `ui-prototypes/<prototype-name>/images/web/checkout/checkout-loading.png` | `ui-prototypes/<prototype-name>/prompts/web/checkout/checkout-loading.md` |  |

Logging rules:
- Add/refresh the manifest row immediately after each image tool call.
- Ensure each image has exactly one matching manifest row.
- Ensure `Prompt Path` stores the exact prompt text used for the final image.
- Treat manifest as latest source of truth; remove stale/legacy rows when artifacts are replaced or deleted.
- Keep only active image/prompt entries for the current prototype revision.

## 10) Click-Through Flow Map Template

Use this schema to connect static images into a simulated interaction flow.

File location:
- `ui-prototypes/<prototype-name>/flow-maps/<platform>/<flow>.json`

```json
{
  "flow_name": "checkout",
  "platform": "web",
  "start_screen": "cart-default",
  "screens": [
    {
      "id": "cart-default",
      "image": "../../images/web/checkout/cart-default.png"
    },
    {
      "id": "checkout-loading",
      "image": "../../images/web/checkout/checkout-loading.png"
    },
    {
      "id": "checkout-success",
      "image": "../../images/web/checkout/checkout-success.png"
    }
  ],
  "transitions": [
    {
      "from_screen": "cart-default",
      "trigger": "click:checkout-button",
      "hotspot": { "x": 1024, "y": 820, "width": 220, "height": 56 },
      "to_screen": "checkout-loading",
      "transition": "instant"
    },
    {
      "from_screen": "checkout-loading",
      "trigger": "system:success",
      "to_screen": "checkout-success",
      "transition": "fade"
    }
  ]
}
```

Validation rules:

- Ensure every `from_screen` and `to_screen` exists in `screens`.
- Ensure each interactive trigger has one deterministic target.
- Keep hotspot rectangles inside image bounds.
- Use consistent trigger naming (`click:*`, `tap:*`, `system:*`).

## 11) Viewer Compatibility Rules

Use these rules so per-platform/per-flow viewers can load and play each flow correctly:

- Place each flow map at `ui-prototypes/<prototype-name>/flow-maps/<platform>/<flow>.json`.
- Keep each `screens[].image` path relative to the flow-map file location.
- Keep `start_screen` present in `screens`.
- For interactive triggers (`click:*` and `tap:*`), always provide `hotspot`.
- Use `system:*` triggers only for non-click transitions.
- Keep hotspot coordinates in source-image pixel space.
- For each image set, keep a viewer bundle at `ui-prototypes/<prototype-name>/viewer/<platform>/<flow>/`.
- Keep `ui-prototypes/<prototype-name>/viewer/<platform>/<flow>/index.html` configured to load `../../../flow-maps/<platform>/<flow>.json`.
