# Layout library (keep slides readable as text grows)

Pick a layout based on how much text you must embed into the image.
In normal use, the skill should auto-route this choice using `references/layout_routing_policy.md` rather than asking the user to pick slide by slide.
The split-panel layouts are only one family. This skill also supports full-bleed cinematic layouts where the image fills the slide and the text sits directly on the image using negative space, subtle tonal shaping, or lower-third positioning. Do not default to visible caption cards or frosted boxes for full-bleed layouts unless the user explicitly asks for them.
Default heuristic for cinematic/editorial/warm/story decks: if the slide can fit 1 title plus up to 4 short lines and the scene can provide a calm text-safe zone, prefer `L4`, `L5`, or `L6` before `L1`.
Default heuristic for classroom, didactic, self-contained teaching, or research poster decks: if the slide needs multiple labeled sections, diagram captions, or visible explanatory text, prefer `L9`, `L10`, or `L11` before trying to compress it into a sparse keynote layout.

## L1 — Classic structured split-panel

- **Best for:** normal text density (title + 2–5 bullets + 1–3 short quotes)
- **Layout:** left 55–60% text panel + right 40–45% hero scene
- **Notes:** safest readability, but it intentionally creates a text panel. Use it when density or structure requires a split composition, or when the user explicitly wants an infographic split-panel look.

## L2 — Framework heavy

- **Best for:** 3-column frameworks / checklists (lots of short lines)
- **Layout:** left 45–50% (title + short quote) + right 50–55% (3 cards)
- **Notes:** keep each card to 2–4 lines max; use icons + checkmarks

## L3 — Two-column text (high density)

- **Best for:** hardship lists / long lists
- **Layout:** left 60–65% text panel split into **two columns**; right 35–40% low-contrast montage
- **Notes:** increase line spacing; reduce font size only slightly; prefer compact separators when needed.

## L4 — Full-bleed direct overlay

- **Best for:** opening/closing slides, short quotes, and medium-text context slides that can use a wall/sky/architecture zone as the text-safe area
- **Layout:** full background scene; direct text overlay anchored left or center-left in a deliberately clean negative-space zone
- **Notes:** cinematic impact; use only local contrast support such as soft shadow, restrained glow, or a subtle tonal wash behind the text; never use for long lists or multi-section teaching layouts

## L5 — Full-bleed title card

- **Best for:** title slides, section openers, and key idea slides with 1 title + 1 short subtitle
- **Layout:** full-bleed hero image across the whole slide; text sits directly on the image in a clean title-safe zone with controlled shadow, glow, or subtle tonal shaping only
- **Notes:** should feel like a movie title card or premium keynote opener; keep text extremely short and avoid any obvious box, card, or banner

## L6 — Full-bleed lower-third overlay

- **Best for:** quote slides, scene-led narrative slides, emotionally strong transitions, and short/medium context slides with 2–4 short supporting lines
- **Layout:** full-bleed hero image across the whole slide; title and one short supporting line sit directly in the lower third or side edge using contrast-aware placement, not a boxed banner
- **Notes:** the scene carries most of the meaning; text should be short and bold, with readability protected by composition instead of a pasted-on panel

## L7 — Comparison cards

- **Best for:** comparison frames such as credentials vs marks or packaging vs truth
- **Layout:** left text panel (45–50%) + right two big cards (50–55%)
- **Notes:** make the cards large; keep labels short; show an arrow for narrative direction

## L8 — Warning poster

- **Best for:** deception / credibility warnings
- **Layout:** left text panel + right hero (mask/halo/shadow) + small caution badge
- **Notes:** use diagonal light beam for tension; keep shadow subtle (not horror)

## L9 — Mirrored comparison explainer

- **Best for:** expectation vs reality, before vs after, old model vs new model, experiment A vs experiment B, or any side-by-side comparison where both halves need labels and small diagrams
- **Layout:** full-width title row across the top; lower body split into left and right mirrored teaching zones with a central divider; each side may carry a short subhead, diagram, arrow/process cue, and one short conclusion/result line
- **Notes:** this is a bright didactic board, not a cinematic slide. Every visible label, annotation, and formula must be explicitly listed in the required on-slide text set.

## L10 — Concept explainer board

- **Best for:** theory/model explanations, historical figure + concept slides, why-it-works slides, strengths vs weaknesses, claim vs limitation, or concept + takeaway boards
- **Layout:** title row across the top; upper band for one portrait/object/diagram + short caption; lower band split into two analytical blocks
- **Notes:** allows more visible words than a keynote slide, but only when the section hierarchy is strong and the board stays uncluttered

## L11 — Catalog grid / repertoire board

- **Best for:** 2x2 or 2x3 grids, repertoires, reaction families, taxonomy slides, multiple methods/examples on one slide, or compact teaching atlases
- **Layout:** title row across the top; below it, a 2x2 or 2x3 grid of modules with thin dividers, generous whitespace, and repeated module structure
- **Notes:** each module may include one header, 1–2 short descriptor lines, and a mini diagram or visual cue; use this when the slide must stand alone as an information-rich teaching artifact
