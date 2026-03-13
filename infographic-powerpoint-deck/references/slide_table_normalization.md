# Slide table normalization (content slide table -> `slides_message_plan.md`)

Use this when an upstream content slide table does not already match the preferred content-plan shape.

## Preferred upstream format

If the table already has these columns, map them 1:1 into `slides_message_plan.md`:
- `Slide role`
- `Headline (claim)` or `Core burden`
- `Source/article anchor`
- `Speaking content` or `Teaching content`
- optional `Must-preserve quote / verse / evidence lines`
- optional `Supporting points / teaching moves`
- optional `Notes on separation / pacing`

## Legacy or underspecified table

If upstream only has a simpler mix such as:
- `Headline (claim)`
- `Evidence anchor + source ID(s)`
- `Supporting bullets (2-4)` or other compact support lines
- `Visual suggestion (location + hero symbol + props)`
- `Text budget`

Then normalize as follows:

1. `Slide role`
   - Infer from the article structure and the row's job in the argument.
   - Use roles such as `opening`, `section opener`, `context`, `key-claim`, `evidence`, `contrast`, `objection`, `framework`, `application`, `transition`, or `closing`.

2. `Speaking content`
   - Build from headline + quote/evidence lines + bullet lines + surrounding explanatory logic.
   - This is the fuller narrative or teaching burden for the slide, not yet the final displayed copy.
   - Keep wording stable where explicit quotes, scripture, or evidence lines must survive intact.
   - Do not preserve an upstream `2-4 bullets` constraint as if it were the final shape of the message plan. Expand the narrative burden when the source material clearly requires more explanation.

3. `Must-preserve lines`
   - Pull out scripture anchors, verse snippets, evidence lines, or exact quotations that later display planning must not lose.

4. `Core burden`
   - State what this slide must communicate beyond the raw title.
   - Keep it content-first, not visual.

5. `Source/article anchor`
   - Map each slide back to the relevant article section, passage range, or evidence anchor.

6. `Notes on separation / pacing`
   - Record if this slide must stay separate from adjacent material.
   - Use this to preserve clarity, not to prescribe layout.

After normalization, derive `slides_display_plan.md` separately:
- choose the exact on-slide text from the fuller speaking content
- preserve must-preserve lines
- decide which lines remain speaker-only and which become visible text

Legacy visual hints can still inform later visual planning, but they should move into `slides_visual_plan.md`, not remain inside the message plan.

## Boundary QA checklist

- Every row has a non-empty speaking / teaching content block.
- Every row has a usable slide role, either carried through or inferred.
- Every row has a clear core burden.
- Every row has a source/article anchor.
- Every row preserves any required verse / quote / evidence lines before display compression happens.
- Dense rows are split when one slide would blur distinct teaching moves.
