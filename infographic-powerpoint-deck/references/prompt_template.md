# Prompt template: 16:9 image-based slide

Copy this template and fill in the bracketed parts. Keep it explicit and verbose; the model should not guess.
This file is an authoring worksheet. Before sending the final concrete prompt to the image model, flatten the chosen content into plain instruction prose.
Do not send worksheet labels such as `Title`, `Slide role`, `Scene ID`, `Required on-slide text (exact)`, `Final checklist`, `Style Pack Bundle`, `Pack`, or `Source` as literal prompt text.
If the concrete prompt could plausibly fit many unrelated slides after changing only the title text, it is too generic. Rewrite it with more slide-specific art direction.

## 0) Output + hard constraints

- Output: a **single 16:9 widescreen PPT slide image** (flat image), no separate layers.
- Keep the generated image as the final artifact by default; no crop/pad/resize/post-processing unless user explicitly requests it.
- Prompt language: **English by default**.
- On-slide text language: **English by default** unless the user explicitly provides another language or requests a bilingual/multilingual slide.
- In concrete prompts, do **not** restate `Prompt language: English` or `On-slide text language: English` when both are already the default and the prompt content is unambiguous. Only include explicit language metadata when:
  - the on-slide text is not English,
  - the prompt instructions stay in English while the rendered text uses another language,
  - the slide is bilingual/multilingual,
  - or the language setup would otherwise be ambiguous.
- Ratio lock sentence must be present in each concrete prompt: `Hard canvas constraint: 16:9 widescreen. Do not generate a square image.`
- Must be **print-sharp** and readable; no tiny fonts.
- **No watermark, no logo, no random characters, and no unspecified text in any language.**
- **Do not add any text** beyond the required on-slide text you explicitly provide for the slide.
- If the required on-slide text is Chinese, German, or bilingual, keep the prompt instructions in English and paste the required text exactly as provided.
- If the required on-slide text is Chinese, also read `references/chinese_text_rendering_playbook.md` before writing the concrete prompt.
- Final delivery mode is one full slide image rendered by the image tools. Do not add text later with Python/PIL/PPT or any other non-image-tool overlay workflow.

## 0b) Tool-call ratio lock (required)

- When calling image generation, explicitly pass ratio config when supported (for example: `generation_config` includes `aspect_ratio: "16:9"`).
- If output still is not 16:9, regenerate the same slide with stricter ratio wording in prompt and ratio config in tool call.
- If deck consistency needs reinforcement, you may supply a previous approved slide or background exploration image as an input/edit reference. The image tool must still render the final full slide image.

## 1) Global style profile (required: select one style block first)

Use style-pack composition:
- Normally choose `pack-id` after inferring the deck archetype from the source content.
- Select `pack-id` from `references/style-pack-catalog.md`.
- Optional: list all packs using `python3 scripts/compose_style_pack_blocks.py --list`.
- Compose blocks from `references/style-packs/` using:
  - `python3 scripts/compose_style_pack_blocks.py --pack-id <id>`
- The default output is prompt-ready raw style text.
- If you need debugging headers like pack names and source paths, use `--annotated` instead.
- Use the composed output as prompt material, but flatten it into plain instructions inside the final concrete prompt rather than preserving helper headings.
- If user does not specify style, infer it from the deck archetype first. If the fit is still unclear, default to `editorial-light`.

## 1b) Recurring motif pack (recommended, paste verbatim)

If you are not using style-pack composition, pick one motif pack from `references/motif_pack.md` and paste it here.

## 1c) Deck consistency lock (recommended, paste verbatim)

If you are not using style-pack composition, pick one lock block from `references/deck_consistency_block.md` and paste it here.

## 1d) Typography + fidelity locks (recommended, paste verbatim)

Paste these blocks verbatim:
- `references/typography_spacing_lock.md`
- `references/text_fidelity_block.md`
- `references/negative_prompt_block.md`

Optional (for stronger narrative): `references/storyboard_library.md`
Optional (for long Chinese passages): `references/chinese_quote_compression.md`
Optional (recommended for Chinese decks): `references/chinese_text_rendering_playbook.md`
Optional (recommended for routing + wording calibration): `references/prompt_example_library.md`

## 2) Slide-specific content (fill in)

### Title
- Title (exact): `[Slide title, including source range if relevant]`
- Slide role: `[opening / section opener / context / key-claim / evidence / contrast / objection / framework / application / transition / quote / emotional beat / closing / other role if needed]`
- Scene ID (from `references/scene-catalog.md` or `slides_visual_plan.md`): `[scene-id]`
  - Optional: select a ready preset from `references/scene-preset-library.md`.

### Required on-slide text (exact)

Include **everything** that must appear on the slide, verbatim:
- `[Lead quote / anchor line 1]`
- `[Lead quote / anchor line 2]`
- `[Key point bullet 1]`
- `[Key point bullet 2]`
- `[Footer microcopy]`

Rules:
- If content comes from an upstream `slides_display_plan.md`, copy from that first.
- If the workflow still uses the legacy `slides_content_plan.md` name, treat it as a message-plan artifact, not as final slide copy, and derive the display text explicitly before writing the prompt.
- If content comes from a raw article intake workflow, do not jump directly from the article to final display text. Derive a message plan first, then a display plan, then copy this block from the display plan.
- Keep quote blocks short; if too long, split into 2 slides.
- If the slide is a didactic infographic or teaching-poster layout, include every visible section header, label, formula caption, module title, and diagram annotation here. Do not expect the model to invent accurate labels on its own.
- If any character, word, accent, punctuation mark, or spacing is wrong in output, regenerate with stricter instruction: `All required on-slide text must be exact. Do not rewrite. Do not add or remove punctuation or spaces.`
- For long Chinese passages, follow `references/chinese_quote_compression.md` (split, do not paraphrase).
- If you are authoring Chinese copy from scratch rather than copying user-provided text, prefer concise fully Chinese phrasing over mixed Chinese + English abbreviations unless the user explicitly wants mixed-script text.
- Do not translate the required text unless the user explicitly asks for translation.

Important boundary:
- `Required on-slide text (exact)` is only the audience-facing visible text.
- It is not the full speaking content or the full teaching burden for the slide.

### High-fidelity prompt rule

For a high-fidelity slide, the final concrete prompt should usually specify all of these:
- exact composition family in plain language
- text-zone placement and approximate width/height behavior
- palette direction with 2-5 concrete color/material cues
- typography attitude and hierarchy
- surface/material treatment behind the text or board
- divider, grid, or module structure when the slide is didactic
- hero visual / diagram subject
- 3-8 supporting objects, symbols, or mini-modules
- lighting direction and contrast behavior
- explicit prohibitions for clutter, extra labels, or unwanted card/panel treatment

Do not stop at shorthand such as `editorial-light`, `didactic`, `clean`, or `modern`.
Translate those into concrete visual instructions the model can actually render.

### Layout rules

- Style pack and layout are separate decisions. The same `pack-id` may use different layouts across slides in one deck.
- Deck archetype should influence the layout mix, but the final layout is still chosen per slide from role + text budget.
- Normally, choose layout automatically using `references/layout_routing_policy.md`.
- If `slides_visual_plan.md` or the user provides `Layout hint`, treat it as an override.
- Keep internal routed layout IDs such as `L1`, `L4`, or `L10` out of the concrete image prompt.
- Instead, translate the chosen layout into plain composition language the image model can actually use.
- If you need to record the internal route for human traceability, keep it outside the concrete prompt body in planning metadata or `prompts.md` notes.
- Never use panel wording unless you actually chose a panel-based layout. The words `text panel`, `left panel`, `card`, `caption box`, `rounded rectangle`, and `frosted panel` are instructions, not harmless descriptions.
- For cinematic, editorial, warm, airy, animated, and youth packs, try a direct-overlay composition first for slides that only need 1 title plus up to 4 short lines.
- If the slide is a context, key-claim, or application slide with medium text but the scene can provide a calm wall, sky, window light, colonnade, or other text-safe zone, prefer `L4` or `L6` before falling back to `L1`.
- If the slide is a self-contained didactic explainer with mirrored comparisons, labeled diagrams, strengths-vs-weaknesses blocks, or 2x2 teaching grids, prefer `L9`, `L10`, or `L11` over compressing it into a sparse keynote layout.
- Translation guide from internal route to model-facing prompt language:
  - `L1`: describe a classic structured split slide with a left text zone and a right supporting illustration zone.
  - `L2`: describe a framework board with 3 structured modules or cards.
  - `L3`: describe a high-density two-column text layout with a quiet supporting image area.
  - `L4`: describe a full-bleed scene with direct overlay in a calm negative-space zone.
  - `L5`: describe a full-bleed title card with a clean title-safe zone.
  - `L6`: describe a full-bleed lower-third or side-edge overlay with text directly on the image.
  - `L7`: describe a comparison slide with one text zone and two large comparison modules.
  - `L8`: describe a warning poster with a text zone and one cautionary hero image.
  - `L9`: describe a mirrored two-zone teaching board with a central divider.
  - `L10`: describe a concept explainer board with a title row, upper hero/diagram band, and lower analytical blocks.
  - `L11`: describe a catalog or teaching grid with 2x2 or 2x3 repeated modules.
- If using panel-based or board-style layouts (`L1`, `L2`, `L3`, `L7`, `L8`, `L9`, `L10`, `L11`):
  - Put title at top-left or upper-left.
  - Put the quote / insight / bullet / label sections inside the text panel or information zones with clear section headers.
  - Keep the main hero visual or diagram modules away from the densest text zones.
  - For `L9`, `L10`, or `L11`, use thin dividers, repeated module structure, and bright clean surfaces rather than cinematic scenery.
- If using full-bleed layouts (`L4`, `L5`, `L6`):
  - Let the image fill the full slide.
  - Place text directly on the image.
  - Default to **no visible card, no rounded rectangle, no frosted panel, and no pasted-on caption box**.
  - Prefer environment-as-text-zone phrasing such as `reserve calm negative space in the architecture`, `let the text sit on the wall/light/sky itself`, or `keep one side compositionally quiet for direct text`.
  - Protect readability with composition first: reserve negative space, keep the background calmer under the text, and use only subtle local support such as controlled shadow, restrained glow, or a soft tonal falloff.
  - Keep text short enough that the image still carries the slide.
  - Protect readability with contrast, negative space, and restrained text count.
- Maintain generous whitespace and alignment discipline in every layout.
- Do not strip necessary labels, formulas, or captions merely to imitate a low-text deck. If the slide is meant to teach as a self-contained infographic, keep the information and route into the correct didactic layout instead.

## 3) Visual structure (be concrete)

Before finalizing the concrete prompt, make sure it covers these design dimensions in plain prose:
- canvas behavior: full-bleed, split, board, grid, or comparison
- geometry: title band, lower modules, divider positions, quiet text-safe zones, approximate proportions
- color/material: surface color, accent color, paper/glass/stone/fabric feel, contrast level
- typography feel: serif vs sans attitude, editorial vs academic tone, boldness, spacing discipline
- lighting: daylight, ambient fill, rim light, haze, or flat academic illumination
- diagram/icon language: thin-line, outlined, filled, sketched, engraved, or stylized 3D
- restraint rules: what must stay low-contrast, simplified, or absent

If any of those dimensions is still vague, enrich the prompt before generating.

Choose the structure that matches the routed layout.

### A. Scene-led layouts (`L1`-`L8`)

- Far background (very low contrast): `[location + time: harbor at dawn / city wall in daylight / bright study interior / wilderness at sunrise]`
- Midground: `[main environment objects: wall, colonnade, waves, damaged boat, route line, scroll, stone path, crowd silhouettes]`
- Foreground hero (right side): `[core symbolic object or protagonist figure: cross, ring, shield, mask, scale, scissors, chain, basket, mentor figure, founder figure, guide character]`
- Surface/material treatment near text: `[sunlit plaster wall / matte stone / soft paper texture / calm fogged glass / smooth warm concrete]`
- Palette and contrast control: `[ivory + slate + muted gold / pale blue-gray + charcoal / warm parchment + deep brown-gray]`

Add 3–8 concrete objects/icons to reinforce meaning:
- `[Icon 1]` (e.g., thin-line icon + subtle glow)
- `[Icon 2]`

If the slide needs a human or character figure:
- Specify role, age range, silhouette, wardrobe, pose, facial expression, gaze direction, and whether the rendering should feel realistic, stylized cinematic, or stylized 3D animated.
- Keep the figure composition readable and away from the main text zone.

Depth + storytelling cues (optional but recommended):
- Camera feel: `[wide shot / medium shot]` with gentle depth-of-field.
- Atmosphere: `[clean daylight / soft haze / warm interior]` according to selected style pack.
- Motion hint: `[rope lowering basket / waves breaking / spotlight beam]` (implied, not literal animation).
- Typography/material integration: `[title sits on the wall itself / body text sits over a calm sky falloff / lower quote aligns with the stone ledge]`

### B. Board / didactic layouts (`L9`, `L10`, `L11`)

Describe the slide as a **clean teaching surface** plus **explicit diagram modules**, not as a cinematic location:

- Base surface: `[bright neutral board / clean paper-white surface / light academic poster field / muted warm classroom surface]`
- Structure: `[mirrored halves / top band + lower two analytical blocks / 2x2 grid / 2x3 grid / central divider / thin section rules]`
- Primary visual module: `[portrait / theory sketch / molecule / reaction scheme / icon set / comparison diagram]`
- Secondary modules: `[mini diagrams / process arrows / labeled captions / repeated grid cells / evidence callouts]`
- Divider and spacing behavior: `[thin neutral dividers / generous whitespace / repeated module rhythm / aligned caption baselines]`
- Palette and accent system: `[off-white board + slate text + muted gold rule / paper-white + deep blue headers + pale gray rules]`
- Typography feel: `[editorial serif title + clean sans body / academic sans hierarchy / textbook-like bold section headers]`
- Diagram rendering language: `[thin-line vector diagrams / clean outline icons / restrained sketched chemistry symbols / precise process arrows]`

Rules for didactic boards:
- Keep the surface bright, quiet, and diagram-friendly rather than scenic.
- Use clean module structure and repeated geometry instead of environmental depth.
- Treat labels, formulas, and annotations as explicit display text, not decorative texture.
- If a portrait or object appears, it should sit inside the board composition, not as a cinematic hero shot competing with the text.
- Make module geometry explicit in the concrete prompt: top band height, number of lower modules, where dividers sit, and which module holds the hero diagram.
- If the slide depends on disciplined academic or editorial tone, specify the typography attitude and divider/accent behavior directly instead of assuming the style pack will imply it strongly enough.

## 4) Final checklist (paste)

- All specified required on-slide text appears **exactly** in the requested language(s).
- No extra words, no watermark, no unspecified text in any language.
- Text is readable at presentation distance.
- Background or board surface is engaging but not busy.
- Deck style stays consistent with selected `pack-id` (no cross-style drift).
- For full-bleed layouts, text sits directly on the image instead of inside an obvious box or card.
- Internal layout IDs are not exposed in the concrete model-facing prompt.
- Worksheet headings are not exposed in the concrete model-facing prompt.
