---
name: infographic-powerpoint-deck
description: Create image-based PowerPoint decks by (1) turning raw article content or notes into a detailed per-slide message plan when needed, (2) turning that message plan into a slide display plan and then a visual-production plan, (3) generating one 16:9 slide image per slide with all displayed text baked into the image (English by default; multilingual slide text supported), and (4) assembling an images-only .pptx that simply concatenates those images full-screen. Use when the user wants polished, consistent visuals with extensible style packs (cinematic dark, cinematic light, cinematic editorial, animated feature, editorial, warm pastoral, tech, youth social, academic, corporate), prefers not to hand-layout PPT objects, or wants a repeatable prompt workflow to iterate over time.
---

# Infographic PowerPoint Deck

## Default input model (raw article first)

This skill should work directly from the user's raw article content by default.

If the user provides a full article, sermon, report, or long notes:
1. Read the source content and infer the audience, burden, density, and argument/story structure.
2. Build `slides_message_plan.md` from the article structure.
3. Turn `slides_message_plan.md` into `slides_display_plan.md`.
4. Turn `slides_display_plan.md` into `slides_visual_plan.md`.
5. Write one image prompt per slide and generate the deck.

If the user already provides `slides_message_plan.md` or an equivalent content-first slide table, you can skip the article-intake step and use that directly.

Legacy compatibility:
- If an older workflow still hands you `slides_content_plan.md`, treat it as the nearest equivalent to `slides_message_plan.md`, then explicitly derive `slides_display_plan.md` before prompt writing.

If the user provides one or more reference slides/screenshots, use `references/reference_slide_intake.md` to extract the reusable visual grammar before writing prompts.

## Artifact model

Use three distinct planning artifacts:

- `slides_message_plan.md`
  - content / presenter planning only
  - what each slide is meant to teach, explain, or say in full
  - the detailed speaking content or narrative burden behind the slide
  - source/article anchors, scripture/evidence anchors, and must-preserve claims
  - what beats must stay separate

- `slides_display_plan.md`
  - what will actually be shown on the slide
  - title, verse fragment, module headers, bullets, labels, captions, footer references
  - explicit on-slide text after text-budget and archetype decisions
  - can be much shorter than the message plan

- `slides_visual_plan.md`
  - downstream visual-production planning
  - deck archetype
  - style pack choice
  - layout routing
  - scene choice
  - text budget and other production constraints

`slides_message_plan.md` is the source of truth for what the presenter means to communicate.
`slides_display_plan.md` is the source of truth for what text the audience actually sees.
`slides_visual_plan.md` is the source of truth for design and prompt production.

## Quick start (default: images-only deck, structured planning)

1. Start from either:
   - raw article content / notes and use `references/article_intake_workflow.md`, or
   - a prebuilt `slides_message_plan.md`, or
   - an underspecified content slide table that you will normalize first
   - optional reference slide images / screenshots and use `references/reference_slide_intake.md`
2. If starting from a raw article, create `slides_message_plan.md` first.
3. Infer one **deck archetype** from the approved message plan using `references/deck_archetype_routing.md`.
   - If the user explicitly requests a style, use that as an override.
4. Pick one **style pack folder**.
   - If user does not specify style and archetype does not strongly imply a different choice, default to `editorial-light`.
   - Style pack chooses the deck's visual language (palette, lighting, typography attitude, scene bias). It does **not** force one fixed layout for every slide.
5. Create `slides_display_plan.md` from `slides_message_plan.md`.
   - Decide what the audience should actually see on each slide after considering archetype, density, and likely layout family.
   - Do not force the full speaking content onto the slide.
6. Create `slides_visual_plan.md` from `slides_display_plan.md`.
   - Add style, layout, scene, and text-budget decisions here, not in the message plan.
7. Gather the style-pack material:
   - You may run `scripts/compose_style_pack_blocks.py --pack-id <id>` as a helper, or manually read the style-pack files.
   - Treat the script output as helper context only, not as the final prompt body.
   - The concrete prompt should still be authored by the model in plain instruction prose.
8. For each slide in `slides_visual_plan.md`, fill `references/prompt_template.md`:
   - Use the style-pack material as helper context and rewrite it into plain instruction prose.
   - Write the prompt instructions in English by default.
   - Paste exact required on-slide text from `slides_display_plan.md` in the user-specified language(s).
   - Add slide-specific scene layer details and icons using the visual plan.
   - Keep internal routing IDs such as `L1` or `L10` in planning metadata only. Translate the routed layout into plain composition language inside the concrete image prompt.
9. Generate each slide as one **16:9 image**.
   - Allowed slide-creation modes in this skill are **image generation** and **image editing/reference** only.
   - In the slide prompt text, explicitly include a ratio lock sentence (e.g., `Hard canvas constraint: 16:9 widescreen. Do not generate a square image.`).
   - In the tool call, explicitly set ratio config when supported (e.g., `generation_config` with `aspect_ratio: "16:9"`).
   - If consistency needs reinforcement, you may use an approved prior slide image or background exploration image as an input/edit reference, but the image tool must still render the final full slide image.
10. QA readability + text accuracy; regenerate only failed slides.
   - If any slide is not 16:9 or has text defects, regenerate the image directly.
   - Do **not** crop, pad, resize, or post-process generated images unless the user explicitly asks.
   - Do **not** render text afterward with Python/PIL/PPT overlays as part of the normal skill workflow.
11. Assemble images-only PPTX with `scripts/build_images_only_pptx.py`.

Outputs to produce in the user’s workspace:
- `slides_message_plan.md` (detailed per-slide speaking / teaching plan; source of truth for what each slide is meant to communicate)
- `slides_display_plan.md` (audience-facing on-slide text plan; source of truth for displayed text and labels)
- `slides_visual_plan.md` (visual-production plan; source of truth for archetype/style/layout/scene decisions)
- `prompts.md` (the exact prompts used for each slide)
- `slides/slide01.png ...` (final 16:9 images)
- `deck_images_only.pptx` (concatenated images)

## Optional structured slide table input

For higher-quality multi-step workflows, you may start from either a raw article or an already-structured message slide table:
- Raw article content is a valid first-class input to this skill. Use `references/article_intake_workflow.md`.
- If the upstream artifact is already `slides_message_plan.md`, preserve it as the message source of truth.
- If the upstream artifact already decides deck length, section coverage, or which beats must stay on separate slides, treat that as the controlling message plan unless the user explicitly asks for further compression or expansion.
- If the upstream content table is simple or underspecified, normalize it into `slides_message_plan.md` using `references/slide_table_normalization.md` before display planning.
- If the upstream workflow still uses the old `slides_content_plan.md` name, interpret it as a legacy message-plan artifact and derive `slides_display_plan.md` before visual planning.

## Prompt stack (minimal vs full)

- Minimal stack (recommended for most decks):
  - `references/article_intake_workflow.md` (when starting from raw article content)
  - `references/deck_archetype_routing.md` (infer the overall deck form first)
  - `references/style-pack-catalog.md` (choose pack ID)
  - `references/style-pack-system.md` (load order + composition rules)
  - `references/layout_routing_policy.md` (auto-route layouts by default)
  - `references/prompt_example_library.md` (use examples and anti-examples to avoid panel drift)
  - `references/reference_slide_intake.md` (when user wants the deck to learn from a reference slide)
  - `references/style-packs/<pack-id>/` (pack-local blocks)
  - `references/typography_spacing_lock.md`
  - `references/text_fidelity_block.md`
  - `references/negative_prompt_block.md`
- Full stack (use when you want maximum narrative + visual control):
  - Minimal stack +
  - `references/storyboard_library.md`
  - `references/shot_mood_library.md`
  - `references/scene-catalog.md`
  - `references/scene_library.md`
  - `references/layout_library.md`
  - `references/chinese_quote_compression.md` (when long Chinese quotes need splitting)

## Style-pack system (modular and scalable)

Use folderized style packs so each style is self-contained:
- Each style pack lives in `references/style-packs/<pack-id>/`.
- Each pack has its own `manifest.toml` and block files that define the look.
- Packs can inherit from `base-core` to reuse shared constraints.
- Prompts are authored from: **base-core guidance + chosen pack guidance + slide-specific content**.
- This avoids cross-file mismatch and makes new style creation deterministic.

Note: despite the Bible-themed examples, this workflow works for any topic. Swap scenes/props in `references/scene_library.md` to match your domain (product, research, training, etc.).

## Decision model (keep style, layout, and scene separate)

- **Message plan** = content-level communication model: what the presenter means to say on each slide and how many slides are needed to say it well.
- **Display plan** = audience-facing text model: what short text, labels, verse fragments, bullets, captions, and module headers should actually appear on the slide.
- **Deck archetype** = deck-level viewing model: what kind of visual presentation best fits the approved message plan.
- **Style pack** = deck-level visual language: palette, lighting, texture, typography attitude, scene bias.
- **Layout** = slide-level composition: split-panel, framework, comparison, warning, didactic teaching board, or full-bleed overlay. It should normally be auto-routed during visual planning.
- **Scene ID / visual scene** = slide-level depiction choice chosen during visual planning.
- **Text budget** = production constraint describing how much copy the chosen layout needs to carry.

Use the deck archetype to drive the rest of the decisions:
- message plan -> slide roles, source anchors, and coverage depth
- message plan + archetype + text budget -> display plan
- display plan -> on-slide text and label density
- deck archetype -> style pack
- deck archetype -> visual-plan layout bias
- slide roles + text budget -> layout routing
- slide role + source meaning -> scene choice
- optional reference slide -> prompt wording, layout bias, and possible style-pack refinement

Slide count is not a deck-skill default. It should be determined by how many slides are actually needed to deliver the content well.

Use this decision rule:
1. identify the distinct beats that need separate treatment
2. decide how much compression each beat can tolerate without hurting clarity, persuasion, or usability
3. set slide count from that coverage need

Upstream slide plans, agent instructions, runtime expectations, or user requests can constrain the deck, but they are not the core planning logic.
If an explicit brevity request would force harmful compression, preserve the content logic first and either:
- keep the richer deck, or
- consciously produce a compressed version while making that tradeoff explicit in `slides_message_plan.md`

Do not collapse a rich article into a short deck merely because the skill can make a shorter deck.

Infographic does **not** mean one universal text density.
Some decks should feel like sparse keynote slides.
Other decks should feel like self-contained didactic infographics or teaching posters with more visible words, labels, formulas, diagram captions, and explanatory sections.
Choose the density and layout family that best serves the content instead of forcing every deck toward the same low-text aesthetic.

Use one style pack across the deck by default, and let the skill choose layout **per slide** unless the user explicitly overrides it:
- Short emotional or opener slides often route to `L4`, `L5`, or `L6`.
- In cinematic, editorial, warm, airy, animated, and youth decks, short/medium context or application slides should try `L4` or `L6` before `L1` if the scene can provide a calm text-safe zone.
- Teaching, framework, comparison, and didactic poster slides often route to `L1`, `L2`, `L3`, `L7`, `L8`, `L9`, `L10`, or `L11` when structure or density requires those layouts.
- The same style pack can legitimately use both split-panel and full-bleed layouts inside one deck.
- If you need article-first intake guidance, read `references/article_intake_workflow.md`.
- If you need archetype routing guidance, read `references/deck_archetype_routing.md`.
- If you need routing guidance, read `references/layout_routing_policy.md`.

## Slide prompt recipe (copy/paste template)

Read `references/prompt_template.md` and fill it per slide. Keep it extremely explicit:
- Start from the inferred article structure, message plan, display plan, and deck archetype, not from arbitrary slide decoration.
- Put **all required on-slide text** from `slides_display_plan.md` into one exact-text block in the concrete prompt.
- If the slide is a dense didactic infographic, include every visible section header, label, callout, formula label, diagram caption, and module heading in that exact-text block rather than expecting the model to invent them correctly.
- For visuals, describe **scene layers** (far/mid/foreground), plus 3–8 concrete objects.
- For high-fidelity results, do not stop at naming the style pack or the layout family. Also specify geometry, palette/material treatment, typography attitude, divider/module structure, and lighting behavior in plain prose.
- Specify what must be **subtle/low-contrast** so text stays readable.
- Keep prompt instructions in English by default even when the required on-slide text is Chinese, German, or bilingual.
- Do not clutter concrete prompts with redundant language metadata in the default English case. Only state prompt/output language explicitly when the slide uses non-English or multilingual rendered text, or when the language setup might otherwise be ambiguous.
- Use both presentation families intentionally: split-panel / board-style infographic layouts for dense teaching content, didactic poster layouts for self-contained educational slides, and full-bleed cinematic overlay layouts for title cards, quote slides, and scene-led emotional beats.
- Treat split-panel wording as explicit layout instructions, not as generic presentation language. If the user prefers text directly on the image, route away from `L1` before writing the prompt.
- Treat `L1`-`L11` as internal routing handles, not model-facing prompt text. The image model should receive composition instructions such as `use a mirrored two-zone teaching board with a central divider`, not `use layout L9`.
- Treat style-pack files the same way: they are internal guidance material, not literal prompt fragments. The final prompt should read like direct art-direction and display instructions, not like serialized metadata.
- If the final prompt still sounds generic after removing the metadata, enrich it rather than shortening it. High-fidelity prompts normally need explicit visual specificity, not just raw content and one style label.
- For full-bleed layouts, default to direct text on the image itself with composition-based readability support. Do not ask for visible rounded rectangles, frosted cards, or caption boxes unless the user explicitly wants that treatment.
- Do not ask the user for per-slide layouts by default. Route layouts internally from slide role, text budget, display density, and overall deck style. Only use explicit `Layout hint` when the user or `slides_visual_plan.md` provides one.
- Do not ask the user for style-pack IDs by default when the article content already makes the fit obvious. Infer archetype first, then select style.

If you need article-first intake guidance, read `references/article_intake_workflow.md`.
If you need deck archetype selection guidance, read `references/deck_archetype_routing.md`.
If you need inspiration for more cinematic scene material and prop ideas, read `references/scene_library.md`.
If you need stable scene IDs + tags for selection/filtering, read `references/scene-catalog.md`.
If you need copy-ready visual scene blocks, read `references/scene-preset-library.md`.
If you need fast, reliable infographic compositions or full-bleed title-card layouts, read `references/layout_library.md`.
If you need automatic routing rules for when to use each layout, read `references/layout_routing_policy.md`.
If you need concrete good/bad prompt examples before writing prompts, read `references/prompt_example_library.md`.
If the user gives a screenshot or example slide and wants the skill to learn from it, read `references/reference_slide_intake.md`.
If you need shot-language / time-of-day / weather / lighting presets, read `references/shot_mood_library.md`.
If you need style modularity, read `references/style-pack-system.md` and use `scripts/compose_style_pack_blocks.py`.
If you want fewer typos and more readability, paste these into every slide prompt: `references/typography_spacing_lock.md`, `references/text_fidelity_block.md`, `references/negative_prompt_block.md`.
If you want storyboard-like viewing rhythm, read `references/storyboard_library.md`.
If a slide uses language-specific rendering constraints or long non-Latin quote blocks, read the relevant reference note before writing the concrete prompt (for example, `references/chinese_quote_compression.md`).

## Quality bar (and how to iterate)

For each slide:
- **Message fit first**: the deck should reflect the structure and intent of the article and the richer message plan, not just produce isolated pretty slides.
- **Display discipline second**: the slide should show only what the audience needs to see, not the entire speaking content.
- **Readability first**: text never overlaps busy imagery; use either a dedicated text panel or a deliberately clean overlay-safe region, depending on the selected layout.
- **Auto-layout first**: unless the user explicitly overrides, let the skill choose the layout from slide role, text budget, and style rather than forcing one composition family.
- **No hallucinated text**: forbid extra words/logos/watermarks.
- **Text fidelity in the requested language/script**: if any character, accent, word, or punctuation is wrong, regenerate that slide with:
  - shorter quote blocks,
  - `All required on-slide text must be exact. Do not rewrite. Do not add or remove punctuation or spaces.`,
  - simpler backgrounds.
- **Engagement**: add background scenes + textures + icon clusters, but keep them low-contrast.
- **Didactic density is allowed when the content needs it**: a self-contained teaching slide may legitimately carry more visible words than a keynote slide, as long as hierarchy, spacing, and diagram structure stay clear.

Common failure fixes:
- Deck feels visually polished but structurally wrong: revisit `references/article_intake_workflow.md` and the message/display boundary; fix the slide roles or display compression before rewriting prompts.
- Tool call fails/intermittent errors: retry after a short wait; keep prompt stable; reduce scene complexity only if repeats.
- Text too small: reduce bullet count; split into two slides; demand large type and comfortable line spacing.
- Slide feels too empty for an infographic teaching use case: reroute to `L9`, `L10`, or `L11` and explicitly include the needed labels, captions, formulas, or comparison headings instead of pretending the content is sparse.
- Too busy: force a low-contrast background, keep the scene mostly on the right, and keep the left panel clean.
- Deck too dark: switch to `editorial-light` or `airy-relaxed`, disable vignette, force daylight scene IDs, and add brightness override.
- Full-bleed overlay feels boxed in: remove visible cards, rounded rectangles, frosted panels, and boxed banners; ask for direct text on the image with only subtle local contrast support.
- Panel drift appears on a cinematic/editorial/warm slide: compare against `references/prompt_example_library.md`, reroute `L1` to `L4` or `L6`, and remove any `text panel` wording before retrying.
- Auto-routed layout feels wrong: reroute the slide using `references/layout_routing_policy.md`; do not keep forcing a weak layout just because an earlier guess picked it.
- Language/script fidelity drifts: shorten copy first, simplify the background, use the relevant language-specific rendering reference, and only then adjust style/layout.
- Ratio mismatch: regenerate that slide with stricter 16:9 constraint in prompt; do not crop or otherwise post-process.
  - Ensure both prompt text and tool-call config specify 16:9 in the same retry.

## Operating mode (be patient; avoid “probe images”)

- Image generation can be **slow**. Prefer generating the real slides directly.
- Avoid generating test/probe images (e.g. blank backgrounds) unless the user explicitly asks for diagnostics.
- If an image call fails intermittently, retry the same slide prompt after a brief pause; do not change multiple variables at once.
- Default delivery mode is **raw outputs**: keep generated images as-is and assemble the PPT directly from them.
- If you create a background exploration image to stabilize later generations, treat it only as an image-tool reference input, not as a canvas for later text overlay or any non-image-tool composition step.

## Tooling constraints (important)

Some image tools only allow writing output images to specific directories (often `~/Downloads` or a workspace path). When blocked:
1. Generate images into an allowed directory (e.g. `~/Downloads/<deck_id>/`).
2. Copy images into the project/workspace output folder.

## Bundled scripts

### `scripts/compose_style_pack_blocks.py`
- Compose inherited style-pack blocks into one paste-ready bundle.
- Use before prompt writing to prevent style mismatch.

Run:
```bash
python3 scripts/compose_style_pack_blocks.py --pack-id editorial-light
```

### `scripts/create_style_pack.py`
- Scaffold a new style pack folder with manifest + block templates.
- Use when existing packs are not enough and you need fast extension.

Run:
```bash
python3 scripts/create_style_pack.py --pack-id warm-minimal --display-name "Warm Minimal" --keywords "warm,balanced" --scene-tags "warm,clean"
```

### `scripts/build_images_only_pptx.py`
- Assemble an images-only PPTX by concatenating `slide*.png` full-screen in filename order.
- Use when the user wants “PPT = concatenated images”, with no PPT text boxes.

Dependencies (install if missing):
```bash
python3 -m pip install python-pptx
```

Run:
```bash
python3 scripts/build_images_only_pptx.py --images-dir /path/to/slides --out /path/to/deck.pptx
```

## References
- Read `references/prompt_template.md` when you need a high-detail prompt skeleton that produces the “rich background infographic” style reliably.
- Read `references/article_intake_workflow.md` when the user gives full article content and expects the skill to infer the deck strategy.
- Read `references/deck_archetype_routing.md` when deciding what overall presentation form best fits the article.
- Read `references/style-pack-system.md` for composition rules and how to add new style packs.
- Read `references/style-pack-catalog.md` for intent-to-style routing and pack selection.
- Read `references/style-packs/` for self-contained style definitions.
- Read `references/slide_table_normalization.md` to normalize underspecified upstream content slide tables into `slides_message_plan.md` before display and visual planning.
- Read `references/scene-catalog.md` for reusable scene IDs and tags.
- Read `references/scene-preset-library.md` for ready-to-paste scene visual blocks.
- Read `references/scene-entry-template.md` when adding new scene IDs to the catalog.
- Read `references/scene_library.md` to quickly add scene-based / cinematic elements (locations + props) without making the slide messy.
- Read `references/layout_library.md` to choose a layout that matches your text density (so slides stay readable).
- Read `references/layout_routing_policy.md` to auto-route layouts when the user does not explicitly request them.
- Read `references/shot_mood_library.md` for cinematic shot + lighting + time-of-day presets.
- Read `references/motif_pack.md` to make the whole deck feel like a single cohesive series.
- Read `references/deck_consistency_block.md` to lock margins/light direction/texture/icon style across the whole deck.
- Read `references/typography_spacing_lock.md` to prevent tiny text and keep spacing consistent.
- Read `references/text_fidelity_block.md` to reduce text errors and forbid any extra words in any language.
- Read `references/negative_prompt_block.md` to avoid common generator artifacts (watermarks/unspecified text/UI).
- Read `references/storyboard_library.md` to give the whole deck a narrative arc.
- Read `references/chinese_quote_compression.md` only when the required on-slide text is Chinese and long enough to need splitting without paraphrasing.
