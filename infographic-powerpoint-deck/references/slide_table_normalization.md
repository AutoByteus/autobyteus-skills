# Slide table normalization (content slide table -> `slides_content_plan.md`)

Use this when an upstream content slide table does not already match the preferred content-plan shape.

## Preferred upstream format

If the table already has these columns, map them 1:1 into `slides_content_plan.md`:
- `Slide role`
- `Headline (claim)` or `Core burden`
- `Source/article anchor`
- `Must-appear text (verbatim)`
- `Supporting bullets (2-4)`
- optional `Notes on separation / pacing`

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

3. `Core burden`
   - State what this slide must communicate beyond the raw title.
   - Keep it content-first, not visual.

4. `Source/article anchor`
   - Map each slide back to the relevant article section, passage range, or evidence anchor.

5. `Notes on separation / pacing`
   - Record if this slide must stay separate from adjacent material.
   - Use this to preserve clarity, not to prescribe layout.

Legacy visual hints can still inform later visual planning, but they should move into `slides_visual_plan.md`, not remain inside the content plan.

## Boundary QA checklist

- Every row has a non-empty `Must-appear text (verbatim)` block.
- Every row has a usable slide role, either carried through or inferred.
- Every row has a clear core burden.
- Every row has a source/article anchor.
- Dense rows are split when one slide would blur distinct teaching moves.
