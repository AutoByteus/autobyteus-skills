# Prompt template: 16:9 rich-background infographic slide

Copy this template and fill in the bracketed parts. Keep it explicit and verbose; the model should not guess.

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
- **Do not add any text** beyond the `Must-appear text (verbatim)` section.
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
- Paste the composed bundle here.
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
- Slide role: `[opening / section opener / context / key-claim / evidence / contrast / objection / framework / application / transition / closing]`
- Scene ID (from `references/scene-catalog.md`): `[scene-id]`
  - Optional: select a ready preset from `references/scene-preset-library.md`.

### Must-appear text (verbatim)

Include **everything** that must appear on the slide, verbatim:
- `[Lead quote / anchor line 1]`
- `[Lead quote / anchor line 2]`
- `[Key point bullet 1]`
- `[Key point bullet 2]`
- `[Footer microcopy]`

Rules:
- If content comes from an upstream `slide_extraction.md` or equivalent slide table, copy from `Must-appear text (verbatim)` first.
- If content comes from a raw article intake workflow, derive this block from the inferred slide role and preserve any must-keep lines from the source.
- Keep quote blocks short; if too long, split into 2 slides.
- If any character, word, accent, punctuation mark, or spacing is wrong in output, regenerate with stricter instruction: `All must-appear text must be exact. Do not rewrite. Do not add or remove punctuation or spaces.`
- For long Chinese passages, follow `references/chinese_quote_compression.md` (split, do not paraphrase).
- If you are authoring Chinese copy from scratch rather than copying user-provided text, prefer concise fully Chinese phrasing over mixed Chinese + English abbreviations unless the user explicitly wants mixed-script text.
- Do not translate the required text unless the user explicitly asks for translation.

### Layout rules

- Style pack and layout are separate decisions. The same `pack-id` may use different layouts across slides in one deck.
- Deck archetype should influence the layout mix, but the final layout is still chosen per slide from role + text budget.
- Normally, choose layout automatically using `references/layout_routing_policy.md`.
- If an upstream artifact or user provides `Layout hint`, treat it as an override.
- State the chosen layout explicitly in the prompt after routing.
- Never use panel wording unless you actually chose a panel-based layout. The words `text panel`, `left panel`, `card`, `caption box`, `rounded rectangle`, and `frosted panel` are instructions, not harmless descriptions.
- For cinematic, editorial, warm, airy, animated, and youth packs, try a direct-overlay composition first for slides that only need 1 title plus up to 4 short lines.
- If the slide is a context, key-claim, or application slide with medium text but the scene can provide a calm wall, sky, window light, colonnade, or other text-safe zone, prefer `L4` or `L6` before falling back to `L1`.
- If using panel-based layouts (`L1`, `L2`, `L3`, `L7`, `L8`):
  - Put title at top-left or upper-left.
  - Put the quote / insight / bullet sections inside the text panel with clear section headers.
  - Keep the main hero visual away from the text panel.
- If using full-bleed layouts (`L4`, `L5`, `L6`):
  - Let the image fill the full slide.
  - Place text directly on the image.
  - Default to **no visible card, no rounded rectangle, no frosted panel, and no pasted-on caption box**.
  - Prefer environment-as-text-zone phrasing such as `reserve calm negative space in the architecture`, `let the text sit on the wall/light/sky itself`, or `keep one side compositionally quiet for direct text`.
  - Protect readability with composition first: reserve negative space, keep the background calmer under the text, and use only subtle local support such as controlled shadow, restrained glow, or a soft tonal falloff.
  - Keep text short enough that the image still carries the slide.
  - Protect readability with contrast, negative space, and restrained text count.
- Maintain generous whitespace and alignment discipline in every layout.

## 3) Visual scene (be concrete)

Describe visuals as a **scene** plus **infographic elements**:

- Far background (very low contrast): `[location + time: harbor at dawn / city wall in daylight / bright study interior / wilderness at sunrise]`
- Midground: `[main environment objects: wall, colonnade, waves, damaged boat, route line, scroll, stone path, crowd silhouettes]`
- Foreground hero (right side): `[core symbolic object or protagonist figure: cross, ring, shield, mask, scale, scissors, chain, basket, mentor figure, founder figure, guide character]`

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

## 4) Final checklist (paste)

- All specified `Must-appear text (verbatim)` content appears **exactly** in the requested language(s).
- No extra words, no watermark, no unspecified text in any language.
- Text is readable at presentation distance.
- Background is engaging but not busy.
- Deck style stays consistent with selected `pack-id` (no cross-style drift).
- For full-bleed layouts, text sits directly on the image instead of inside an obvious box or card.
