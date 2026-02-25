# Prompt template: 16:9 “rich background infographic” slide

Copy this template and fill in the bracketed parts. Keep it explicit and verbose; the model should not guess.

## 0) Output + hard constraints

- Output: a **single 16:9 widescreen PPT slide image** (flat image), no separate layers.
- Language: **Simplified Chinese** (or specify bilingual).
- Must be **print-sharp** and readable; no tiny fonts.
- **No watermark, no logo, no random characters; no English unless it is explicitly included in “必须出现文字”.**
- **Do not add any text** beyond the “必须出现文字” section.

## 1) Global style profile (paste as-is, tweak if needed)

- Visual: modern infographic + cinematic concept illustration / matte painting background; layered (far/mid/foreground) but clean.
- Layout: left **55–60% text panel** (dark frosted-glass card, rounded corners) + right **40–45% hero visual**.
- Palette: deep navy/indigo gradient background; body text white; emphasis gold `#F4C542`; tiny light-blue highlights.
- Typography: crisp Simplified Chinese, comfortable line spacing; ensure punctuation is correct.
- Background rule: background scenes and textures must be **low-contrast** so text stays dominant.
- Cinematic lighting (right side): volumetric rays, rim light, subtle vignette, minimal dust motes (do not reduce readability).

## 1b) Recurring motif pack (recommended, paste verbatim)

Pick one motif pack from `references/motif_pack.md` and paste it here. Then include the same motif pack on **every** slide prompt.

## 1c) Deck consistency lock (recommended, paste verbatim)

Pick one lock block from `references/deck_consistency_block.md` and paste it here. Then include the same lock block on **every** slide prompt.

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

### 必须出现文字（逐字准确）

Include **everything** that must appear on the slide, verbatim:
- `[引言/经文摘句 1]`
- `[引言/经文摘句 2]`
- `[要点 bullet 1]`
- `[要点 bullet 2]`
- `[页脚小字]`

Rules:
- Keep quote blocks short; if too long, split into 2 slides.
- If any character is wrong in output, regenerate with stricter instruction: “逐字准确，不得改写，不得增删标点/空格”.
 - For long verses, follow `references/chinese_quote_compression.md` (split, don’t paraphrase).

### Layout rules

- Put title at top-left, large.
- Put “经文摘句/要点” inside the left text panel with clear section headers (gold).
- Keep the right hero visual free of text.
- Maintain generous whitespace and alignment grid.

## 3) Visual scene (be concrete)

Describe visuals as a **scene** plus **infographic elements**:

- Far background (very low contrast): `[地点 + 时间：海港黄昏/城墙夜色/抄写室烛光/荒野清晨…]`
- Midground: `[主要环境物：城墙、柱廊、海浪、破船、路线、卷轴、石板路、人群剪影…]`
- Foreground hero (right side): `[核心象征物：十字架、婚戒、盾牌、面具、天平、剪刀、锁链、筐子…]`

Add 3–8 concrete objects/icons to reinforce meaning:
- `[图标 1]` (e.g., thin-line icon + subtle glow)
- `[图标 2]`

Depth + storytelling cues (optional but recommended):
- Camera feel: `[wide shot / medium shot]` with gentle depth-of-field.
- Atmosphere: `[mist/haze]` for air perspective; `[water reflection / moonlight]` for mood.
- Motion hint: `[rope lowering basket / waves breaking / spotlight beam]` (implied, not literal animation).

## 4) Final checklist (paste)

- All specified Chinese text appears **exactly**.
- No extra words, no watermark, no English.
- Text is readable at presentation distance.
- Background is engaging but not busy.
