# Chinese quote compression & splitting (long passages -> readable slides)

Goal: keep Chinese text **accurate** while preventing tiny fonts and wall-of-text slides.

If you need broader Chinese rendering guidance beyond quote splitting, also read `references/chinese_text_rendering_playbook.md`.

## When to split

Split into 2+ slides if any is true:
- Quote block > 3 lines at comfortable font size
- Bullets > 5
- Mixed: long quote + long list on one slide

## Safe splitting patterns (no paraphrase)

1) **Quote chunking** (recommended)
- Slide A: quote chunk 1 + 2 bullets (why it matters)
- Slide B: quote chunk 2 + 2 bullets (application)

2) **Quote vs explanation**
- Slide A: quote only (plus 1 key line)
- Slide B: explanation framework (no quote, or 1 short anchor line)

3) **List overflow**
- Slide A: first half of list + same scene
- Slide B: second half of list + same scene (slight camera change)

## Copy shaping note

- If the user already provided exact Chinese text, keep it exact.
- If you are drafting or translating Chinese copy for the slide, prefer shorter fully Chinese lines over mixed Chinese + Latin abbreviations unless the user explicitly wants mixed-script text.

## Pasteable rules block

```text
Chinese long-quote layout rules (required):
- Do not rewrite the quoted text. You may split it across slides, but do not paraphrase or swap in synonyms.
- If the quotation is too long, split it into multiple slides. Keep each quoted section to no more than 3 lines at a comfortable large font size.
- Preserve the original sentence order when splitting. Use an ellipsis only if it already exists in the source text or the user explicitly allows it.
- If explanation is needed, prefer moving the explanation to the next slide instead of cramming a long quote and long bullets onto one slide.
```
