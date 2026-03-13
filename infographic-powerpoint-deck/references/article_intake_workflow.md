# Article intake workflow (default when user provides raw content)

Use this when the user provides a full article, sermon notes, research writeup, teaching memo, or other long-form source content instead of a prebuilt slide table.

The most important rule: do not compress into final slide copy too early.
The first planning artifact should capture what the speaker means to teach on each slide, not just the short text that will eventually be rendered on the image.

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

2. Build `slides_message_plan.md` from the article structure:
   - opener
   - context
   - key claims
   - evidence / examples
   - contrast / objection if present
   - application / takeaway
   - closing
   - for each slide, record the fuller speaking / teaching burden, not only the future visible slide text

3. Decide how much slide separation each move needs:
   - what must stay on its own slide
   - what can be combined safely
   - what would become confusing if compressed

4. Record the source/article anchor, speaker burden, supporting points, and must-preserve lines for each slide.

5. After the message plan exists, choose a deck archetype using `references/deck_archetype_routing.md`.
   - Archetype selection should be based on the source content **and** the approved message plan, not on raw topic words alone.
   - A fast provisional guess during reading is acceptable, but the committed archetype should reflect the actual slide burdens in `slides_message_plan.md`.

6. Only after the message plan and archetype are approved, derive `slides_display_plan.md`:
   - what title, verse fragment, bullets, labels, captions, or footer references should actually appear on the slide
   - what can stay in the speaker burden without being displayed
   - how much display compression the chosen deck archetype and text budget allow

The intake portion of the workflow culminates in `slides_message_plan.md`.
Once that exists, continue the overall skill flow with archetype selection, display planning, visual planning, and prompt writing.
Do not skip directly from raw article to final slide prompt text.

## Planning rules

- Do not ask the user for per-slide layouts by default.
- Do not ask the user for style-pack IDs by default.
- Do not apply a global default slide count.
- Do not confuse speaking content with displayed text.
- `slides_message_plan.md` may hold 100-300 words of narrative burden for one slide when needed, while the eventual `slides_display_plan.md` might show only a title, a verse line, and 2-4 short bullets.
- Determine deck length from coverage quality first:
  - how many distinct moves need separate slides
  - how much compression each move can tolerate
  - whether the resulting sequence still teaches, persuades, or explains cleanly
- If an upstream agent or structured plan already sets deck length or coverage, use it as a planning constraint, not as a substitute for thinking.
- User brevity requests or runtime constraints can justify compression, but the skill should make that tradeoff explicit rather than pretending the shorter deck is equally complete.
- Split dense sections early instead of overloading one slide.
- Preserve the source argument flow; do not turn a serious article into disconnected visual slogans.
- Record the deck-length rationale in `slides_message_plan.md` so downstream review can tell whether the plan is over-compressed or over-expanded.

## Output expectation

`slides_message_plan.md` should include a short strategy header before the slide list:
- inferred audience
- inferred tone
- target deck length or range, with rationale
- source burden / story arc
- any explicit user overrides

Each slide row or section should ideally record:
- slide role
- core burden
- fuller speaking / teaching content
- source/article anchor
- must-preserve quotes, scripture references, or evidence lines
- notes on what must stay separate

`slides_display_plan.md` should then record, per slide:
- title
- on-slide text (verbatim)
- verse or source footer if needed
- visible module headers / labels
- display text budget
