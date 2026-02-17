---
name: computer-use-playbook
description: Use when tasks involve cross-application computer use (browser, file explorer, and native dialogs) and require choosing between DOM, vision, shell, and native UI automation.
---

# Computer Use Playbook

## Overview
Use this skill for end-to-end computer automation across browser and desktop surfaces. Browser use is a major track, but not the only one. Prefer deterministic methods first, then escalate to visual/native automation only when required.

## Playbook Structure
1. Browser use (primary for web tasks): browser MCP tools, DOM snapshots, scripts, screenshots.
2. Filesystem use: shell-native operations for deterministic file/process work.
3. Native desktop use: coordinate and window automation only when DOM/shell are insufficient.
4. Human-in-the-loop checkpoints: login, CAPTCHA, security prompts, or policy-gated steps.

## Decision Order
1. Identify the active surface: browser page, filesystem/process, or native desktop UI.
2. For browser pages, use browser MCP tools first (DOM/scripting/screenshot).
3. For filesystem/process work, use shell/system tools first (`rg`, `ls`, `find`, etc.).
4. Escalate to vision or native UI automation only when deterministic methods are insufficient.
5. If blocked by login, CAPTCHA, or security gates, switch to human-in-the-loop flow.
6. Verify each critical step with state checks plus screenshot evidence.

## Browser Automation (Major Track)
Use browser tools + DOM-first for browser flows. Avoid jumping to native desktop clicks while the target is still reachable by browser tools.

Preferred sequence:
1. `open_tab` (or `open_tab` with URL if available)
2. `dom_snapshot` or `run_script` to identify target
3. `run_script` action (click/type/submit)
4. verify URL/title/content
5. `screenshot` as evidence

Session behavior guidance:
- treat the most recently opened tab as the active default for subsequent actions.
- keep all follow-up actions on the active tab unless an explicit tab switch is required.
- pass `tab_id` only when disambiguation is needed across multiple intentional tabs.
- after any action that may open a new tab, verify URL/title before continuing.

Escalation triggers:
- dynamic overlays not stable via selectors,
- canvas/rendered controls,
- consent dialogs where selector path is inconsistent,
- native picker launched from browser (file upload dialog).

Do not overuse fallback:
- if a browser tool can do it, stay in browser tools.
- use native automation only for cross-app boundaries (OS dialogs, non-DOM UI).

## File Explorer and Filesystem Automation
Prefer shell-native methods before GUI clicking.

Use shell when possible:
- search files: `rg --files`, `find`
- move/copy/rename: `mv`, `cp`, `mkdir`
- inspect metadata: `ls -la`, `stat`

Use native UI only when the workflow is GUI-only:
- OS file picker from browser/app,
- drag-drop interactions not scriptable via API,
- app-specific explorer panes.

## Native UI Automation
Use native UI automation for interactions outside application DOM/API.

Typical tools:
- `xdotool` for key/click/type,
- `xprop` / `xwininfo` for window targeting.

Guidelines:
- ensure window focus before typing,
- prefer keyboard-driven deterministic paths,
- keep retries bounded and observable,
- re-check application state after each action.

## Human-in-the-loop rules
Pause and ask for user intervention when blocked by:
- login/2FA challenges,
- CAPTCHA or anti-bot checkpoints,
- legal/security confirmation screens that require explicit human intent.

When waiting for user action:
1. explain exactly what the user must do and where.
2. issue an audible notification using `speak` so the user notices immediately.
3. wait, then re-check state (`url`, `title`, element visibility, screenshot) before continuing.

## Special Cases
### Consent dialogs
- DOM-first click (`Accept all`/`Reject all`/localized variants).
- if selector fails but button is visible, use coordinate/native fallback.
- confirm modal is not visible and main interaction path works.

### CAPTCHA / anti-bot challenges
- do not attempt bypass logic.
- capture evidence and report blocked state clearly.
- require human-in-the-loop completion.
- notify user with `speak` when intervention is required.

### Login and account security gates
- try normal DOM steps first for username/password field fill and submit.
- if SSO, passkey, device approval, or 2FA requires human action, pause and request user action.
- after user confirms completion, re-snapshot and continue from verified page state.

### File uploads
- use DOM file input assignment if available.
- if native picker opens, switch to native UI automation.
- verify upload appears in page/app state.

## Verification Standard
Every important step should end with both:
1. state evidence (URL/title/content/element state), and
2. visual evidence (screenshot path).

If blocked, report:
- attempted method,
- blocker reason,
- evidence collected,
- next safe fallback.

## References
Load `/Users/normy/.codex/skills/computer-use-playbook/references/computer-use-techniques.md` for command snippets and fallback templates.
