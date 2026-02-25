---
name: infographic-powerpoint-deck
description: Create image-based PowerPoint decks by (1) designing a slide plan, (2) generating one 16:9 infographic slide image per slide with all text baked into the image (Chinese/English supported), and (3) assembling an images-only .pptx that simply concatenates those images full-screen. Use when the user wants a polished, consistent visual style (infographic + cinematic illustrated backgrounds with strong “画面感”), prefers not to hand-layout PPT objects, or wants a repeatable “style profile” to iterate on over time.
---

# Infographic PowerPoint Deck

## Quick start (default: images-only deck)

1. Draft a slide list (8–20 slides) with: title, verse quote(s), key points, and a “visual scene” per slide.
   - If you already have a reasoning artifact (recommended): convert `slide_extraction.md` rows into slides.
2. For each slide, write a **detailed generation prompt** that includes:
   - Global style profile (colors, layout grid, typography, background richness)
   - The **exact text that must appear** (verbatim, with punctuation)
   - Right-side visuals (scene + icons + charts)
   - Hard restrictions (no watermark/logo; no extra English unless explicitly required; readability; keep text unobstructed)
3. Generate each slide as a **single 16:9 image** using the image generation tool.
4. QA: spot-check readability + typos; regenerate only the broken slides.
5. Assemble an images-only PPTX with `scripts/build_images_only_pptx.py`.

Outputs to produce in the user’s workspace:
- `slides_plan.md` (slide-by-slide content + visuals)
- `prompts.md` (the exact prompts used for each slide)
- `slides/slide01.png ...` (final 16:9 images)
- `deck_images_only.pptx` (concatenated images)

## Recommended upstream artifact (thinking before slides)

For higher-quality decks, start from a logically structured article + extraction table:
- Use the `deep-research-article` skill to produce `article.md` and `slide_extraction.md`.
- Then generate slide images from `slide_extraction.md` (each row → one slide prompt).

## Prompt stack (minimal vs full)

- Minimal stack (recommended for most decks):
  - `references/motif_pack.md` (pick A or B)
  - `references/deck_consistency_block.md` (pick one lock block)
  - `references/typography_spacing_lock.md`
  - `references/text_fidelity_block.md`
  - `references/negative_prompt_block.md`
- Full stack (use when you want maximum “cinematic narrative” control):
  - Minimal stack +
  - `references/storyboard_library.md`
  - `references/shot_mood_library.md`
  - `references/scene_library.md`
  - `references/layout_library.md`
  - `references/chinese_quote_compression.md` (when quotes are long)

## Style profile: “Bible Sharing Cinematic Infographic v3” (recommended)

Use this as the default “look” unless the user requests otherwise:
- Canvas: 16:9 wide PPT slide image (single flat image).
- Layout: **Left 55–60% text panel** (dark frosted-glass card, rounded corners) + **Right 40–45% hero visual**.
- Palette: deep navy/indigo gradient background; body text white; emphasis gold `#F4C542`; small light-blue accents.
- Background: cinematic matte-painting scenes at **low contrast** (harbor at dusk, city wall at night, scribe desk + candle, map texture, parchment, stained-glass light).
- Iconography: thin-line vector icons; small checkmarks; subtle separators.
- Typography: Simplified Chinese (high legibility); keep lines short; avoid tiny font sizes.
- “画面感” add-ons (right side only; keep left panel clean):
  - 3-layer scene: far/mid/foreground
  - film lighting: volumetric rays, rim light, subtle vignette
  - depth cues: haze/air perspective, soft bokeh/dust motes (minimal)
- Recurring motif pack (recommended): apply a subtle, consistent motif set across every slide to make the deck feel like “one film”.
  - Default: `references/motif_pack.md` → **Motif Pack A (Keynote Cinematic)**

Note: despite the Bible-themed examples, this workflow works for any topic. Swap scenes/props in `references/scene_library.md` to match your domain (product, research, training, etc.).

## Slide prompt recipe (copy/paste template)

Read `references/prompt_template.md` and fill it per slide. Keep it extremely explicit:
- Put **all required on-slide text** under a “必须出现文字（逐字准确）” section.
- For visuals, describe **scene layers** (far/mid/foreground), plus 3–8 concrete objects.
- Specify what must be **subtle/low-contrast** so text stays readable.

If you need inspiration for “更有画面感”的场景素材与道具库, read `references/scene_library.md`.
If you need fast, reliable infographic compositions, read `references/layout_library.md`.
If you need “镜头语言/时间天气/光影情绪” presets, read `references/shot_mood_library.md`.
If you want stronger deck cohesion, read `references/motif_pack.md` and include the motif pack verbatim in every slide prompt.
If you want the deck to feel like one continuous film (less randomness), read `references/deck_consistency_block.md` and paste one lock block verbatim into every slide prompt.
If you want fewer typos and more readability, paste these into every slide prompt: `references/typography_spacing_lock.md`, `references/text_fidelity_block.md`, `references/negative_prompt_block.md`.
If you want “像分镜一样”的观看节奏，read `references/storyboard_library.md`.
If you have long verse blocks, read `references/chinese_quote_compression.md` and split quotes across slides (do not paraphrase).

## Quality bar (and how to iterate)

For each slide:
- **Readability first**: text never overlaps busy imagery; use a dedicated text panel.
- **No hallucinated text**: forbid extra words/logos/watermarks.
- **Chinese accuracy**: if any characters are wrong, regenerate that slide with:
  - shorter quote blocks,
  - “逐字准确，不得改写，不得增删标点/空格”,
  - simpler backgrounds.
- **Engagement**: add background scenes + textures + icon clusters, but keep them low-contrast.

Common failure fixes:
- Tool call fails/intermittent errors: retry after a short wait; keep prompt stable; reduce scene complexity only if repeats.
- Text too small: reduce bullet count; split into two slides; demand “大字号、舒适行距”.
- Too busy: force “背景低对比、仅右侧画面、左侧纯净面板”.

## Operating mode (be patient; avoid “probe images”)

- Image generation can be **slow**. Prefer generating the real slides directly.
- Avoid generating test/probe images (e.g. blank backgrounds) unless the user explicitly asks for diagnostics.
- If an image call fails intermittently, retry the same slide prompt after a brief pause; do not change multiple variables at once.

## Tooling constraints (important)

Some image tools only allow writing output images to specific directories (often `~/Downloads` or a workspace path). When blocked:
1. Generate images into an allowed directory (e.g. `~/Downloads/<deck_id>/`).
2. Copy images into the project/workspace output folder.

## Bundled scripts

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
- Read `references/scene_library.md` to quickly add “场景化/电影感” elements (locations + props) without making the slide messy.
- Read `references/layout_library.md` to choose a layout that matches your text density (so slides stay readable).
- Read `references/shot_mood_library.md` for cinematic shot + lighting + time-of-day presets.
- Read `references/motif_pack.md` to make the whole deck feel like a single cohesive series.
- Read `references/deck_consistency_block.md` to lock margins/light direction/texture/icon style across the whole deck.
- Read `references/typography_spacing_lock.md` to prevent tiny text and keep spacing consistent.
- Read `references/text_fidelity_block.md` to reduce Chinese typos and forbid any extra words.
- Read `references/negative_prompt_block.md` to avoid common generator artifacts (watermarks/English/UI).
- Read `references/storyboard_library.md` to give the whole deck a narrative arc.
- Read `references/chinese_quote_compression.md` to split long quotes without paraphrasing (keeps fonts large).
