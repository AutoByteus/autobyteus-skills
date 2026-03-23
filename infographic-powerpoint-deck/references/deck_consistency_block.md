# Deck-level consistency blocks (reduce randomness across slides)

Optional helper library. Preferred flow is style-pack composition (`references/style-packs/`).
Use this file when manually selecting consistency rules.
Consistency locks help stabilize a deck, but they do not replace concrete slide-level prompt detail.
They are guidance for rhythm and coherence, not permission to force every slide into a visible template.

Paste **one** block into every slide prompt. This acts like a “style lock” so the deck feels coherent across slides.

## Block 1 — Cinematic Keynote Lock

Paste this verbatim:

```text
This deck is one cohesive series (consistency rules are mandatory):
- Layout lock: if using split-panel slides, keep a stable reading balance with the text zone a little wider than the illustration zone. If using full-bleed slides, keep the same text anchor area and direct-overlay behavior across all slides instead of introducing visible cards.
- Type lock: keep a fixed hierarchy for title, section headers, quotes, bullets, and footer. Comfortable leading. No tiny text on any slide.
- Type attitude lock: keep the same title/body/label personality across the full deck instead of drifting between unrelated font moods.
- Light-direction lock: the main light direction stays fixed from upper-right to lower-left. Strong beams belong only in the illustration zone, never across the main text area.
- Rim-light lock: the right-side hero object uses the same gold rim-light intensity on every slide.
- Horizon / silhouette lock: keep the far-background silhouette band (city / harbor / wall / colonnade) at a consistent height in the lower 35%-45% of the frame, always low-contrast and softly blurred.
- Texture lock: apply the same ultra-low-contrast parchment-grain texture across the full deck at roughly 5%-10% strength.
- Icon lock: use a consistent thin-line icon style and consistent glow strength for checkmarks and dividers.
- Cleanliness lock: use decorative rules sparingly. Do not place extra underlines or repeated separators around already-readable headings.
- Forbidden: no extra text, logos, watermarks, or random characters.
- Readability hard constraint: all text must stay sharp and high-contrast; the background must not interfere with the main text area.
```

## Block 2 — Movie Poster Epic Lock (stronger impact)

Paste this verbatim:

```text
This deck is a movie-poster-style series (consistency rules are mandatory):
- Layout lock: default to full-bleed composition with direct text on the image in a stable anchor zone. If a split-panel variant is used, keep the text zone slightly dominant and the illustration zone secondary. Do not introduce visible caption cards into the full-bleed version.
- Key-light lock: use one diagonal primary light beam from upper-right toward center at the same angle on every slide. A slight vignette is allowed only when it improves focus.
- Landmark-silhouette lock: each slide includes the same class of far-background landmark silhouette (harbor / wall / colonnade / wilderness horizon) with consistent placement and blur.
- Gold-accent lock: each slide uses only 1-2 gold highlight points. All other gold elements stay as low-contrast fine lines.
- Type attitude lock: preserve one poster-like title style and one body/label style across the full series.
- Grain and haze lock: keep stronger atmospheric depth separation, with cooler softer far backgrounds and slightly warmer foregrounds.
- Text hard constraint: do not sacrifice readability for poster drama. All required text must appear exactly.
- Forbidden: no extra text, logos, watermarks, or random characters.
```

## Block 3 — Editorial Light Lock (bright + relaxed)

Paste this verbatim:

```text
This deck is a bright editorial series (consistency rules are mandatory):
- Layout lock: if using split-panel slides, keep the text zone modestly wider than the illustration zone. If using full-bleed slides, keep a stable clean text zone and direct-overlay behavior with no obvious caption box.
- Brightness lock: keep overall medium-high brightness. Do not let large dark areas make the slide feel dim. No vignette.
- Lighting lock: rely on natural diffused light from a consistent upper-left or upper-right direction. No dramatic volumetric beams.
- Color lock: use light backgrounds (off-white / light gray / pale blue), dark gray-blue body text with strong contrast, and restrained accent colors.
- Type attitude lock: keep one calm editorial/corporate typography system across title, subhead, labels, bullets, and footer.
- Texture lock: only very weak paper or fabric texture with low noise. No dirty grain or grunge.
- Icon lock: use consistent thin-line icons with matched geometry and accent color treatment.
- Cleanliness lock: keep the deck visually quiet. If a title or section is already clear, do not add extra underlines or decorative rules.
- Text hard constraint: readability is non-negotiable. All required text must appear exactly.
- Forbidden: no extra text, logos, watermarks, or random characters.
```

## Block 4 — Illustrative Cinematic Lock (immersive + didactic)

Paste this verbatim:

```text
This deck is an illustrative-cinematic teaching series (consistency rules are mandatory):
- Layout lock: keep the deck scene-rich but clearly didactic. Use calm illustrated reading zones, elegant dividers, and soft module structure instead of heavy visible cards.
- Cleanliness lock: keep divider language restrained and functional. Do not underline every heading or stack multiple rule treatments around the same module.
- Brightness lock: keep the base bright and readable. Use warm ivory or pale-stone fields with soft atmospheric depth, not dark theatrical contrast.
- Color lock: keep dark slate text, muted deep-blue structure lines, and restrained soft-gold emphasis stable across the deck.
- Type attitude lock: preserve one premium editorial or luminous humanist title style, one crisp body style, and one refined label style across the full series.
- Illustration lock: keep icon, diagram, and scene rendering polished and cohesive; no scratchy sketch texture, no doodle marks, and no abrupt drift into flat corporate UI or photoreal grit.
- Spatial-depth lock: allow gentle depth and illustrated architecture or symbolic setting, but never let the atmospheric layer compete with the teaching modules.
- Text hard constraint: all required text must appear exactly and remain fully readable.
- Forbidden: no extra text, logos, watermarks, random characters, or visible pasted-on caption cards.
```

## How to use

- Add the chosen block under a `Series consistency lock` section in every slide prompt.
- Match the block with style pack from `references/style-pack-catalog.md`:
  - `cinematic-dark` → Block 1 or 2
  - `editorial-light` / `airy-relaxed` / `clean-corporate` → Block 3
  - `illustrative-cinematic` → Block 4
- Combine with `references/motif_pack.md` (motifs) + `references/prompt_template.md` (structure).
- For full-bleed slides, keep the text directly on the image and use composition-based readability support rather than a visible box.
- For didactic or whiteboard-style slides, let consistency show up through spacing rhythm, divider behavior, accent color, arrow language, and typography attitude rather than exact boxed geometry.
