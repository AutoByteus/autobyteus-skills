# Computer Use Techniques Reference

## Browser-First Rule
For browser tasks:
1. Use browser MCP tools first (`open_tab`, `dom_snapshot`, `run_script`, `screenshot`).
2. Keep work in the active tab by default.
3. Escalate to vision/native only when the target is not reliably reachable by DOM methods.

## Active Tab Default Pattern
1. Open a tab once and treat it as active context.
2. Run follow-up actions on that active tab by default.
3. Use explicit `tab_id` only when multiple tabs are intentionally in play.
4. After actions that can open new tabs, confirm current URL/title before continuing.
5. If the active tab closes, explicitly re-establish the active tab before the next action.

## Browser Consent Pattern (DOM-first)
1. Query visible buttons and normalize labels.
2. Match `accept all` / localized variants.
3. Click target button.
4. Verify modal visibility is false.
5. Re-check search/content availability.

## Login / 2FA Human-Handoff Pattern
1. Attempt standard DOM flow for username/password only.
2. If blocked by SSO device approval, passkey, OTP app, or enterprise gate, stop automation.
3. Ask user for intervention with explicit instruction.
4. Send audible notification with `speak` (for example: "Please complete login in the browser, then tell me to continue.").
5. Resume only after verification with URL/title/DOM state and screenshot evidence.

## CAPTCHA Pattern
1. Detect challenge UI and record evidence.
2. Do not attempt bypass logic.
3. Request human completion and notify with `speak`.
4. Re-check page state after user confirms completion.

## Browser Navigation Safety
After click/submit:
1. Poll `window.location.href` and `document.title`.
2. Retry on transient execution-context errors.
3. Avoid redundant second navigation unless first action clearly failed.

## Vision Grounding Pattern
1. Capture screenshot.
2. Run coordinate finder with precise target text.
3. Apply click at coordinates.
4. Re-capture screenshot and confirm state changed.

## Native File Picker Pattern (X11)
When browser opens OS picker:
1. focus window: `xdotool search --name "Chrome" windowactivate`
2. type path: `xdotool type --delay 20 "/path/to/file"`
3. confirm: `xdotool key Return`
4. verify upload in page state.

## File Explorer Pattern
Prefer shell for deterministic operations:
- locate: `rg --files | rg "name"`
- inspect: `ls -la <dir>`
- move/copy: `mv`, `cp`

Use GUI explorer automation only for GUI-constrained flows.

## Failure Report Template
- action: what was attempted
- method: DOM / shell / vision / native
- evidence: URL/title/screenshot path
- blocker: exact error or UI state
- next fallback: concrete next step
