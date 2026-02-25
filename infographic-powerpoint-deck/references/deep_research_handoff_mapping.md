# Deep-research handoff mapping (`slide_extraction.md` → slide prompts)

Use this when upstream `slide_extraction.md` comes from `deep-research-article`.

## Preferred upstream format

If upstream table already has these columns, map 1:1:
- `Headline (claim)` → slide title / claim headline
- `Must-appear text (verbatim)` → “必须出现文字（逐字准确）”
- `Supporting bullets (2–4)` → bullet section
- `Recommended style pack ID` → `pack-id`
- `Scene ID` → scene selection
- `Layout hint` → layout choice (L1–L6)
- `Text budget` → density check/splitting rule

## Legacy upstream format (older table)

If upstream only has:
- `Headline (claim)`
- `Evidence anchor + source ID(s)`
- `Supporting bullets (2–4)`
- `Visual suggestion (location + hero symbol + props)`
- `Text budget`

Then normalize as follows:

1. `Must-appear text (verbatim)`
   - Build from headline + quote/evidence lines + bullet lines.
   - Keep wording stable; do not paraphrase if explicit quotes are provided.

2. `Recommended style pack ID`
   - Infer by topic and tone:
     - faith/devotional → `warm-sermon` or `editorial-light`
     - AI/startup/product → `neo-tech`
     - youth/community → `youth-social`
     - research/objective analysis → `research-academic`
     - if unclear → `editorial-light`

3. `Scene ID`
   - Match from `scene-catalog.md` by semantic overlap.
   - If no exact match, use `custom:<slug>` and still provide visual detail.

4. `Layout hint`
   - `short` → `L1` or `L4`
   - `medium` → `L1` / `L2` / `L5`
   - `heavy` → `L3` (or split into two slides)

## Boundary QA checklist

- Every row has a non-empty `Must-appear text (verbatim)` block.
- Every row has a valid `pack-id`.
- Every row has a scene decision (`Scene ID` or `custom:<slug>`).
- Heavy rows are either `L3` or split.
