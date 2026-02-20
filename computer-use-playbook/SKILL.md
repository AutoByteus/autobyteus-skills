---
name: computer-use-playbook
description: Use when tasks involve cross-application computer use (browser, file explorer, and native dialogs) and require choosing between DOM, vision, shell, and native UI automation.
---

# Computer Use Playbook

## Overview
Use this skill for end-to-end computer automation across browser and desktop surfaces. Browser use is a major track, but not the only one. Prefer deterministic methods first, then escalate to visual/native automation only when required. For browser MCP workflows, treat `tab_id` as a required handle for all stateful actions.

## Playbook Structure
1. Browser use (primary for web tasks): browser MCP tools, DOM snapshots, scripts, screenshots.
2. Filesystem use: shell-native operations for deterministic file/process work.
3. Native desktop use: coordinate and window automation only when DOM/shell are insufficient.
4. Human-in-the-loop checkpoints: login, CAPTCHA, security prompts, or policy-gated steps.

## Decision Order
1. Identify the active surface: browser page, filesystem/process, or native desktop UI.
2. For browser pages, use browser MCP tools first and keep a strict `tab_id` contract.
3. For filesystem/process work, use shell/system tools first (`rg`, `ls`, `find`, etc.).
4. Escalate to vision or native UI automation only when deterministic methods are insufficient.
5. If blocked by login, CAPTCHA, or security gates, switch to human-in-the-loop flow.
6. Verify each critical step with state checks plus screenshot evidence.

## Browser Automation (Major Track)
Use browser tools + DOM-first for browser flows. Avoid jumping to native desktop clicks while the target is still reachable by browser tools.

Preferred sequence:
1. `open_tab` and capture returned `tab_id`.
2. `navigate_to(tab_id, url)` for explicit page transitions.
3. `dom_snapshot(tab_id, ...)` or `run_script(tab_id, ...)` to identify target.
4. `run_script(tab_id, ...)` action (click/type/submit).
5. `read_page(tab_id, ...)` / `run_script(tab_id, ...)` to verify URL/title/content.
6. `screenshot(tab_id, ...)` as evidence.

Session behavior guidance:
- always pass `tab_id` for `navigate_to`, `read_page`, `screenshot`, `dom_snapshot`, `run_script`, and `close_tab`.
- never rely on implicit active-tab behavior.
- if a click opens a new tab/window, call `list_tabs`, detect the new `tab_id`, and continue explicitly on that `tab_id`.
- keep a local map of `purpose -> tab_id` when handling multiple tabs.

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

## Learning Library Structure
Use `references/learnings/` as the canonical knowledge base.

- `references/learnings/index.md`: topic registry and folder convention.
- `references/learnings/general/`: cross-task fallback logs.
- `references/learnings/<topic-slug>/`: topic-specific lessons and experience log.

Topic folder convention:
- `lessons.md` for stable workflow rules.
- `experience-log.md` for incremental run learnings.

## Continuous Learning Loop (Required)
Treat each real run as training data for future runs.

Priority contract:
- `lessons.md` is the source of truth for execution.
- `experience-log.md` is supporting evidence used to refine or extend lessons.
- If lesson and experience conflict, follow `lessons.md` and then update logs/lessons after the run.

Before starting similar work:
1. Load `references/learnings/index.md`.
2. Map the task to a topic slug (for example `google-flow`).
3. Load topic `lessons.md` first when present:
   - `references/learnings/<topic-slug>/lessons.md`
4. Load topic `experience-log.md` second when present:
   - `references/learnings/<topic-slug>/experience-log.md`
5. Load `references/learnings/general/experience-log.md` only as fallback context when topic files are missing or incomplete.
6. If the topic folder does not exist, create it with `lessons.md` and `experience-log.md`.

Before execution:
1. Extract a short run checklist from topic `lessons.md`.
2. Execute against that checklist.
3. Use experience logs only to fill gaps not covered by lessons.

During execution:
1. Capture failure signal and the exact step where it appears.
2. Record the minimal fix that resolved it.
3. Keep one-action-at-a-time execution where UI state is fragile.

After completion (or meaningful failure):
1. Append a short run note to `references/learnings/<topic-slug>/experience-log.md`.
2. Include: date, context, failure signal, root cause, fix pattern, reusable rule.
3. Keep entries concise and deduplicated by updating prior rules instead of adding noisy repeats.

## References
Load `references/computer-use-techniques.md` for command snippets and fallback templates.
Load `references/learnings/index.md` to select the right topic folder.
Load topic `references/learnings/<topic-slug>/lessons.md` first.
Load topic `references/learnings/<topic-slug>/experience-log.md` second.
Load `references/learnings/general/experience-log.md` only as fallback for cross-task patterns.
Load `references/learnings/google-flow/lessons.md` when automating Google Flow video creation.
Load `references/learnings/google-flow/experience-log.md` after lessons for incremental learnings.
