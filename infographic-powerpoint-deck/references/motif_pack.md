# Recurring motif packs (deck cohesion booster)

Legacy component library. Preferred flow is style-pack composition (`references/style-packs/`).
Use this file when manually mixing motif and consistency blocks.

Use a motif pack to make a deck feel like a single cohesive series. Keep motifs **subtle**, mostly on the right side / far background, and never behind the main text in a way that hurts readability.

Tip: for even stronger cohesion (margins/light direction/texture consistency), combine with `references/deck_consistency_block.md` and paste one lock block into every slide prompt.

## Motif Pack A (Keynote Cinematic)

Include these on every slide (subtle, consistent):
- **Gold geometry ring**: a thin-line gold circle/halo motif (same line width every slide), placed near the hero symbol area.
- **Dust motes in light**: a small amount of floating particles visible only inside light beams (very minimal).
- **Parchment grain overlay**: ultra-low-contrast texture across the whole canvas (5–10% strength).
- **Signature divider line**: a gold hairline separator under the title or between sections (consistent style).
- **Soft vignette**: slight darkening at corners (very light; consistent).

Do:
- Keep the ring + divider line in consistent positions (within a narrow range).
- Keep motif contrast low; motifs should be felt, not noticed.

Avoid:
- Large repeated patterns behind text.
- High-contrast rings that look like logos.

## Motif Pack B (Movie Poster Epic) — stronger impact

Include these on every slide (still controlled):
- **Diagonal key light**: one consistent directional “beam” angle across the deck (e.g., top-right → center).
- **Gold foil accents**: tiny specular glints on 1–2 props only (ring, chain cut, wax seal).
- **Horizon silhouette**: a recurring far-background silhouette band (harbor/city wall/colonnade) at the same vertical level, blurred.
- **Atmospheric haze**: stronger depth separation (far background soft + cool; foreground warmer).
- **Title glow**: a very subtle outer glow on the main title only (low strength).

Do:
- Use wide/medium shots more often to feel “cinematic”.
- Keep silhouettes low contrast so the text area stays clean.

Avoid:
- Overly dramatic contrast that fights the typography.
- Too many glints (looks cheap).

## Motif Pack C (Editorial Airy) — bright + relaxed

Include these on every slide (lightweight, clean):
- **Soft paper/fabric grain**: very light texture, mostly visible in flat areas.
- **Gentle daylight gradient**: subtle top-left to bottom-right brightness flow (no dark corners).
- **Accent dot/line system**: tiny geometric dots or thin dividers in style accent color.
- **Text-edge support**: minimal soft glow or tonal shaping around the text area when needed for separation.
- **Clean icon halo**: faint neutral halo around key icons, no dramatic rim light.

Do:
- Keep motifs nearly invisible at first glance; they should only improve coherence.
- Prefer bright, low-noise backgrounds so text is easy to read.

Avoid:
- Any vignette or heavy shadow treatment.
- Overdecorating with too many pattern elements.

## How to apply (pasteable blocks)

When writing slide prompts, add one of these (depending on which pack you chose):

### Pack A pasteable block
```text
This slide must include all elements from Motif Pack A (Keynote Cinematic). Keep them low-contrast and series-consistent, and do not reduce main text readability.
```

### Pack B pasteable block
```text
This slide must include all elements from Motif Pack B (Movie Poster Epic). Keep them low-contrast and series-consistent, and do not reduce main text readability.
```

### Pack C pasteable block
```text
This slide must include all elements from Motif Pack C (Editorial Airy). Keep them bright, low-noise, and series-consistent, and do not reduce text readability.
```
