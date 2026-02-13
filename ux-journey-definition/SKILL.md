---
name: ux-journey-definition
description: "Define a practical, story-first product experience before UI prototyping. Use when you need one canonical artifact that explains what users see, what they can do, and how screens transition."
---

# UX Journey Definition

## Overview

Create one canonical artifact, `experience-story.md`, that captures the product story, main journey, screen-by-screen behavior, and transition mapping. This is the upstream input for `$product-ui-prototyping`.

## Default Output

- `ui-prototypes/<prototype-name>/experience-story.md`
- If the user specifies a different path, follow the user path.

## Workflow

### Audible Notifications (Speak Tool, Optional But Supported)

- If the user asks for spoken updates, enable notification mode for the current journey-definition task.
- Use the `Speak` tool for milestone-level updates so the user does not need to watch the screen continuously.
- Minimum speak events when enabled:
  - product story + main journey draft completed,
  - screen stories + alternate/error paths completed,
  - transition index completed,
  - canonical artifact write completed (`experience-story.md` written/updated),
  - quality gate result (`Pass`/`Needs fixes`),
  - handoff-ready status for `$product-ui-prototyping`.
- Speak trigger policy:
  - speak only after milestone content is physically written,
  - do not speak for partial drafts,
  - batch close-together milestone updates into one short message.
- Keep each spoken message short (1-2 sentences), status-first, with one clear next step.
- If the `Speak` tool fails or is unavailable, continue workflow and provide the same update in text.
- Do not speak secrets, tokens, or full sensitive payloads.

### 1) Capture Product Story

Write one short paragraph:
- who the user is,
- what they are trying to achieve,
- what success looks like.

Keep this concrete and product-facing.

### 2) Write Main Journey (Happy Path)

Write a numbered flow from entry to success.
Each step should include:
- what the user does,
- what the system does,
- which `screen_id` is involved.

Prioritize one critical flow first before expanding.

### 3) Write Screen Stories

For each screen, describe behavior in plain language with stable IDs.

Required shape:
- `screen_id`
- user arrives from
- user sees
- user can do (`action_id`)
- system behavior for each action
- states to prototype (`default`, `loading`, `success`, `error`, `empty` when applicable)

### 4) Capture Alternate/Error Paths

Document only meaningful branches:
- validation failures,
- empty/no-results states,
- recoverable errors.

For each branch, state:
- trigger/condition,
- what user sees,
- recovery action and destination.

### 5) Build Transition Index

Create a single transition table that links interactions to movement.

Columns:
- `transition_id`
- `trigger`
- `from_screen`
- `to_screen`
- `expected_feedback`

Use IDs consistently across the whole document.
- If audible notification mode is enabled, announce completion after the transition index is physically written.

### 6) Record Blocking Questions

List only blockers that can change behavior or flow.
Do not include cosmetic/open-ended discussion items.

## Canonical Artifact Template

Use this structure in `experience-story.md`:

```markdown
# Experience Story: <prototype-name>

## 1) Product Story
<one short paragraph>

## 2) Main Journey
1. ...
2. ...

## 3) Screen Stories

### screen_id: <screen_id>
- User arrives from: ...
- User sees:
  - ...
  - ...
- User can do:
  - `<action_id>`: ...
- System behavior:
  - when `<action_id>` -> <feedback> -> go to `<next_screen_id>`
- States to prototype: default, loading, success, error, empty

## 4) Alternate And Error Paths
- If <condition>, show <state/message>, then user can <recovery action>.

## 5) Transition Index
| transition_id | trigger | from_screen | to_screen | expected_feedback |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |

## 6) Blocking Questions
- <question> (owner: <name>)
```

## Practical Rules

- Keep it practical and short. Avoid heavy theory.
- No `out-of-scope` section by default.
- Focus on behavior and navigation, not design tokens.
- Keep each screen section to 5-8 bullets.
- Every action must define both feedback and next destination.

## Quality Gate

- One clear happy path exists from entry to success.
- Every major trigger maps to a target screen/state.
- Screen IDs and transition IDs are consistent.
- Error and empty states include recovery actions.
- The document can be directly used by `$product-ui-prototyping`.
- If audible notification mode is enabled, announce quality-gate result after validation completes.

## Handoff To Prototyping

When visual prototyping is requested next, invoke `$product-ui-prototyping` with:
- `ui-prototypes/<prototype-name>/experience-story.md`
- product constraints from this document
- chosen platform (`web`, `ios`, `android`)

Then generate state images, flow maps, and viewer artifacts based on the transition index and screen stories.
- If audible notification mode is enabled, announce handoff-ready completion after `experience-story.md` is written/updated.
