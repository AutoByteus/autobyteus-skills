# Article intake workflow (default when user provides raw content)

Use this when the user provides a full article, sermon notes, research writeup, teaching memo, or other long-form source content instead of a prebuilt slide table.

## User model

- User usually provides:
  - raw article content
  - rough notes
  - a draft essay / sermon / report
  - optional audience or tone preference
- User usually does **not** provide:
  - style-pack ID
  - per-slide layout instructions
  - slide-by-slide scene design

Therefore the skill should infer the deck strategy from the source content first.

## Intake steps

1. Read the source content and infer:
   - core thesis
   - intended audience
   - tone and emotional energy
   - content density
   - narrative shape
   - must-preserve quotes or lines

2. Choose a deck archetype using `references/deck_archetype_routing.md`.

3. Build the slide plan from the article structure:
   - opener
   - context
   - key claims
   - evidence / examples
   - contrast / objection if present
   - application / takeaway
   - closing

4. Set a text budget for each slide:
   - `short`
   - `medium`
   - `heavy`

5. Choose one deck-level style pack from the archetype unless the user explicitly overrides style.

6. Auto-route layout for each slide using `references/layout_routing_policy.md`.

7. Write one concrete image prompt per slide using `references/prompt_template.md`.

## Planning rules

- Do not ask the user for per-slide layouts by default.
- Do not ask the user for style-pack IDs by default.
- Prefer 6-15 slides for a normal long-form article unless the user asks for a different size.
- Split dense sections early instead of overloading one slide.
- Preserve the source argument flow; do not turn a serious article into disconnected visual slogans.

## Output expectation

`slides_plan.md` should include a short strategy header before the slide list:
- inferred audience
- inferred tone
- inferred deck archetype
- chosen style pack
- routing bias
- any explicit user overrides
