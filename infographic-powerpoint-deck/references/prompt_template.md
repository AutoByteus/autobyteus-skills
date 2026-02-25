# Prompt template: 16:9 “rich background infographic” slide

Copy this template and fill in the bracketed parts. Keep it explicit and verbose; the model should not guess.

## 0) Output + hard constraints

- Output: a **single 16:9 widescreen PPT slide image** (flat image), no separate layers.
- Language: **Simplified Chinese** (or specify bilingual).
- Must be **print-sharp** and readable; no tiny fonts.
- **No watermark, no logo, no random characters; no English unless it is explicitly included in “必须出现文字”.**
- **Do not add any text** beyond the “必须出现文字” section.

## 1) Global style profile (required: select one style block first)

Use style-pack composition:
- Select `pack-id` from `references/style-pack-catalog.md`.
- Optional: list all packs using `python3 scripts/compose_style_pack_blocks.py --list`.
- Compose blocks from `references/style-packs/` using:
  - `python3 scripts/compose_style_pack_blocks.py --pack-id <id>`
- Paste the composed bundle here.
- If user does not specify style, default to `editorial-light`.

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
Optional (for long verses): `references/chinese_quote_compression.md`

## 2) Slide-specific content (fill in)

### Title
- Title (exact): `[标题，含经文范围]`
- Scene ID (from `references/scene-catalog.md`): `[scene-id]`
  - Optional: select a ready preset from `references/scene-preset-library.md`.

### 必须出现文字（逐字准确）

Include **everything** that must appear on the slide, verbatim:
- `[引言/经文摘句 1]`
- `[引言/经文摘句 2]`
- `[要点 bullet 1]`
- `[要点 bullet 2]`
- `[页脚小字]`

Rules:
- If content comes from `deep-research-article/slide_extraction.md`, copy from `Must-appear text (verbatim)` first.
- Keep quote blocks short; if too long, split into 2 slides.
- If any character is wrong in output, regenerate with stricter instruction: “逐字准确，不得改写，不得增删标点/空格”.
 - For long verses, follow `references/chinese_quote_compression.md` (split, don’t paraphrase).

### Layout rules

- Put title at top-left, large.
- Put “经文摘句/要点” inside the left text panel with clear section headers (accent color from selected style).
- Keep the right hero visual free of text.
- Maintain generous whitespace and alignment grid.

## 3) Visual scene (be concrete)

Describe visuals as a **scene** plus **infographic elements**:

- Far background (very low contrast): `[地点 + 时间：海港清晨/城墙白天/抄写室明亮室内/荒野晨光…]`
- Midground: `[主要环境物：城墙、柱廊、海浪、破船、路线、卷轴、石板路、人群剪影…]`
- Foreground hero (right side): `[核心象征物：十字架、婚戒、盾牌、面具、天平、剪刀、锁链、筐子…]`

Add 3–8 concrete objects/icons to reinforce meaning:
- `[图标 1]` (e.g., thin-line icon + subtle glow)
- `[图标 2]`

Depth + storytelling cues (optional but recommended):
- Camera feel: `[wide shot / medium shot]` with gentle depth-of-field.
- Atmosphere: `[clean daylight / soft haze / warm interior]` according to selected style pack.
- Motion hint: `[rope lowering basket / waves breaking / spotlight beam]` (implied, not literal animation).

## 4) Final checklist (paste)

- All specified Chinese text appears **exactly**.
- No extra words, no watermark, no English.
- Text is readable at presentation distance.
- Background is engaging but not busy.
- Deck style stays consistent with selected `pack-id` (no cross-style drift).
