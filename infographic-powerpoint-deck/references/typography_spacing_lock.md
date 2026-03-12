# Typography + spacing lock (image-only deck)

Paste this block into every slide prompt to reduce “tiny text” and improve readability.

```text
Typography and spacing hard constraints (required):
- Canvas: 16:9. Safe margins: at least 4% whitespace on every edge. No text touching the edge.
- Text support zone: must match the selected layout and style pack. Split-panel layouts may use a defined panel. Full-bleed layouts must place text directly on the image with subtle local contrast support only, not an obvious card or box.
- Title hierarchy:
  - Main title: very large, bold, ideally one line, maximum two lines, comfortable leading.
  - Section headers / subheads: use the style-pack accent color and remain clearly legible.
  - Quotes / supporting text: slightly smaller than bullets or on the same tier, but never tiny.
  - Bullets: maximum two lines each. Split into additional slides if needed.
  - Footer: small but still readable at presentation distance.
- Line length and spacing:
  - Latin-script languages (English, German, etc.): prefer roughly 6-12 words per line in dense text blocks.
  - CJK languages: prefer roughly 18-22 characters per line before wrapping.
  - If Chinese fidelity is fragile, shorten further and target roughly 12-18 characters per line on title/supporting lines before wrapping.
  - Line spacing must be at least 1.25x the character height.
- Text volume limits (recommended):
  - Standard slide: quotes up to 3 lines, bullets up to 5 items.
  - High-density list slide: use a two-column text-panel layout and reduce background detail.
- Contrast hard constraints:
  - The text support zone and body text must maintain strong contrast (target roughly WCAG 4.5:1 or better).
  - If the background is bright, use dark body text. If the background is dark, use light body text.
- Forbidden:
  - No tiny text.
  - No decorative novelty fonts.
  - No decorative or calligraphic Chinese fonts unless the user explicitly asks for that treatment.
  - No background texture or contrast crossing through the text area in a way that hurts readability.
  - No obvious pasted-on white box, frosted caption card, or rounded rectangle for full-bleed cinematic layouts unless the user explicitly asks for that style.
```
