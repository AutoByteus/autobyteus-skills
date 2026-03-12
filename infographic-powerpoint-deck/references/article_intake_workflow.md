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

3. Build `slides_content_plan.md` from the article structure:
   - opener
   - context
   - key claims
   - evidence / examples
   - contrast / objection if present
   - application / takeaway
   - closing

4. Decide how much slide separation each move needs:
   - what must stay on its own slide
   - what can be combined safely
   - what would become confusing if compressed

5. Record the source/article anchor and must-appear text for each slide.

The article-intake workflow stops at `slides_content_plan.md`.
Style, layout, scene, and prompt writing happen later in the visual-planning stage.

## Planning rules

- Do not ask the user for per-slide layouts by default.
- Do not ask the user for style-pack IDs by default.
- Do not apply a global default slide count.
- Determine deck length from coverage quality first:
  - how many distinct moves need separate slides
  - how much compression each move can tolerate
  - whether the resulting sequence still teaches, persuades, or explains cleanly
- If an upstream agent or structured plan already sets deck length or coverage, use it as a planning constraint, not as a substitute for thinking.
- User brevity requests or runtime constraints can justify compression, but the skill should make that tradeoff explicit rather than pretending the shorter deck is equally complete.
- Split dense sections early instead of overloading one slide.
- Preserve the source argument flow; do not turn a serious article into disconnected visual slogans.
- Record the deck-length rationale in `slides_content_plan.md` so downstream review can tell whether the plan is over-compressed or over-expanded.

## Output expectation

`slides_content_plan.md` should include a short strategy header before the slide list:
- inferred audience
- inferred tone
- target deck length or range, with rationale
- source burden / story arc
- any explicit user overrides
