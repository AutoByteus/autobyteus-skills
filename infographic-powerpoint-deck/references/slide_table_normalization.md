# Slide table normalization (`slide_extraction.md` or legacy slide table -> slide prompts)

Use this when an upstream `slide_extraction.md` or equivalent slide table does not already match the preferred handoff shape.

## Preferred upstream format

If the table already has these columns, map them 1:1:
- `Slide role` -> slide role used by layout routing and prompt framing
- `Headline (claim)` -> slide title / claim headline
- `Must-appear text (verbatim)` -> `Must-appear text (verbatim)` section in the slide prompt
- `Supporting bullets (2-4)` -> bullet section
- `Recommended style pack ID` -> `pack-id`
- `Scene ID` -> scene selection
- `Layout hint` -> optional layout override (L1-L8); choose independently from the style pack
- `Text budget` -> density check/splitting rule

## Legacy or underspecified table

If upstream only has a simpler mix such as:
- `Headline (claim)`
- `Evidence anchor + source ID(s)`
- `Supporting bullets (2-4)`
- `Visual suggestion (location + hero symbol + props)`
- `Text budget`

Then normalize as follows:

1. `Slide role`
   - Infer from the article structure and the row's job in the argument.
   - Use roles such as `opening`, `section opener`, `context`, `key-claim`, `evidence`, `contrast`, `objection`, `framework`, `application`, `transition`, or `closing`.

2. `Must-appear text (verbatim)`
   - Build from headline + quote/evidence lines + bullet lines.
   - Keep wording stable; do not paraphrase if explicit quotes are provided.

3. `Recommended style pack ID`
   - Infer by topic and tone:
     - faith/devotional -> `warm-sermon` or `editorial-light`
     - bright cinematic / hopeful narrative -> `cinematic-light`
     - premium keynote / polished campaign feel -> `cinematic-editorial`
     - animated / family / character-led -> `animated-feature-bright`
     - AI/startup/product -> `neo-tech`
     - youth/community -> `youth-social`
     - research/objective analysis -> `research-academic`
     - if unclear -> `editorial-light`

4. `Scene ID`
   - Match from `scene-catalog.md` by semantic overlap.
   - If no exact match, use `custom:<slug>` and still provide visual detail.

5. `Layout hint`
   - Optional override only.
   - If blank, auto-route layout using `references/layout_routing_policy.md`.
   - Pick layout from text budget and slide role, not from style pack alone.
   - `short` -> `L4`, `L5`, or `L6`
   - `medium` -> `L4` or `L6` when the slide still fits a calm overlay-safe text zone; otherwise `L1`, `L2`, or `L7`
   - `heavy` -> `L3` (or split into two slides)

## Boundary QA checklist

- Every row has a non-empty `Must-appear text (verbatim)` block.
- Every row has a usable slide role, either carried through or inferred.
- Every row has a valid `pack-id`.
- Every row has a scene decision (`Scene ID` or `custom:<slug>`).
- If `Layout hint` is present, it matches both text budget and slide role.
- Heavy rows are either `L3` or split.
