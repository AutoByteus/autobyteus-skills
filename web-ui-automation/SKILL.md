---
name: web-ui-automation
description: Automate web application interfaces by locating page elements with the `browser-automation` skill and translating their browser coordinates into native mouse and keyboard input. Use when native UI input (such as xdotool/X11), not script-dispatched events, must perform the interaction.
---

# Web UI Automation

Use this skill for the shared mechanics of controlling a website or web app in a visible browser. The `browser-automation` skill observes the page and locates controls; native input performs every interaction. This skill does not define an individual website's workflow or capabilities—use its app-specific skill for those.

## Requirements

- The `browser-automation` skill is available. Follow it for the launcher, tab IDs, and error recovery.
- The target tab is shown in a visible browser window on the display that native input reaches.
- In this interaction mode, every `browser-automation` `run-script` is read-only. Do not use `__abDemo` or any script to click, focus, type, set values, dispatch UI events, or submit forms.

## Locate, map, act

1. **Locate.** Understand the page with `dom-snapshot` or `read-page`. Then run a read-only `run-script` that identifies the intended control by its role, label, text, or other useful page context and returns its current `getBoundingClientRect()`, `window.screenX`, `window.screenY`, `window.outerHeight`, `window.innerHeight`, and `document.visibilityState`. Act only when the state is `visible`; otherwise bring that tab to the front with native input and locate again.
   Modern web apps may place visible controls inside open Shadow DOM. If a visible control is missing from an ordinary query or accessibility snapshot, inspect the composed tree/open shadow roots before concluding it is unavailable.
2. **Map.** Use the center of the element as a practical click point:

   ```text
   viewport_x = rect.x + rect.width / 2
   viewport_y = rect.y + rect.height / 2
   screen_x = window.screenX + viewport_x
   screen_y = window.screenY + (window.outerHeight - window.innerHeight) + viewport_y
   ```

   This direct conversion assumes browser CSS pixels map 1:1 to native screen pixels. If browser zoom or display scaling breaks that assumption, calibrate the viewport-to-screen mapping once for the current window/display setup and reuse it until that setup changes. The result is an absolute screen-pixel target; translate it if the selected input tool uses a different coordinate system.
3. **Act.** Use native input to operate the page. `xdotool`/X11 is a useful default for mouse, keys, typing, window focus, and wheel events (`click 4`/`click 5`); native keyboard paths are often simplest. If an upload opens an operating-system file chooser, continue with native input there; keyboard shortcuts and confirmation labels vary, so use the chooser's visible `Open`/`Select` control or its working Enter shortcut rather than assuming one mnemonic.
4. **Recalculate** coordinates when page layout or browser-window geometry changes; do not reuse stale coordinates across navigation, resizing, zoom changes, tab switches, or major overlays.

## Page dialogs after native input

`browser-automation` answers a page dialog (`confirm`, `prompt`, "Leave site?") only during its own command. A dialog raised by a native action stays open, and later `browser-automation` commands against that browser fail with `PAGE_BLOCKED`. When a native action may raise one, answer it on screen with native input, using the choice the task calls for, before the next `browser-automation` command.

## Choose the right native tools

Do not treat `xdotool` as the only possible actuator. On Linux/X11, use the tools that fit the job: for example, `xdotool` for pointer/keyboard/scroll input, `xprop` or `xwininfo` for window geometry, `scrot` or `xwd` for desktop screenshots, and `xclip` for clipboard transfer. Other input tools may be appropriate when installed and compatible with the current display/session; check their coordinate units and input requirements before using them.

Check availability with `command -v`. If a needed capability is missing and an existing tool cannot do the job, install an appropriate small utility when system permissions allow, then verify it works. Do not install extra tools when the current stack is sufficient, and do not switch input mechanisms to evade a site's protections. On other operating systems, use the platform's equivalent native controls. Follow any stricter app-specific operating rules when present.

## Use judgment, not a screenshot ritual

Do not require a screenshot and full state audit after every input. Verify the result when the action is ambiguous or consequential, the layout changed, a submit/upload may have failed, or the next action depends on the outcome. Use a fresh `dom-snapshot` or read-only `run-script` for page state, and a `browser-automation` `screenshot` for page appearance. Use a desktop screenshot for native dialogs, file choosers, and anything outside the page. If the target is clear and the action is routine, proceed without redundant checks.

If an action misses, inspect the current page and window geometry again, recalculate or recalibrate the mapping, and retry based on the new state rather than blindly reusing old coordinates.
