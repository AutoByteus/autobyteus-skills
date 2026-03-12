# Negative prompt block (avoid common generator failures)

Paste this block into every slide prompt to prevent unwanted artifacts.

```text
Negative constraints (must avoid):
- Do not include watermarks, logos, brand marks, QR codes, URLs, UI chrome, buttons, app windows, or subtitle bars.
- Do not include any unspecified words, letter strings, random characters, or meaningless symbols in any language.
- Do not include readable text on street signs, posters, book pages, maps, or documents. Use no-text texture only.
- Do not make the background so complex that the text area becomes hard to read. Do not let high-contrast texture cut through the text panel or text support zone.
- For full-bleed layouts, do not add an obvious rounded rectangle, frosted caption card, white box, or pasted-on text panel unless the user explicitly requests that treatment.
- Do not include horror or gore. Do not include photoreal celebrity faces or recognizable real-person portraits unless the user explicitly asks.
- Do not mix incompatible visual styles in one slide (for example cartoon + photoreal + 3D at the same time).
```
