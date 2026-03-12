# Chinese text rendering playbook

Use this file when the rendered on-slide text is Chinese.
The prompt instructions can stay in English, but the Chinese copy itself needs stricter handling than English.

## What worked in practice

- Lock the script explicitly when needed: `Simplified Chinese` or `Traditional Chinese`.
- Tell the model to render all on-slide text in printed Chinese exactly as provided.
- Use large, bold, clean sans-serif Chinese typography.
- Prefer shorter lines and shorter total copy than an equivalent English slide.
- If you are drafting Chinese copy from scratch, prefer fully Chinese wording over mixed Chinese + Latin abbreviations unless the user explicitly wants mixed-script text.
  - Example: `人工智能` is safer than `AI` inside an otherwise Chinese slide.
- Keep the illustration zone free of readable labels, chart text, dashboard text, document text, book text, or stray Chinese words.
- When Chinese text volume is medium or heavy, structured split layouts such as `L1` or `L2` are usually safer than direct-overlay full-bleed layouts.

## Common failure patterns

- Mixed-script drift: the model adds English letters, pinyin, or hybrid labels.
- Character drift: one or two characters are replaced, simplified incorrectly, or visually broken.
- Busy-scene drift: the image invents readable Chinese words inside books, signs, dashboards, or wall details.
- Density drift: the slide tries to carry too much Chinese text at once and shrinks the typography too far.

## Authoring rules

1. Keep required Chinese text exact when the user already provided it.
2. If you are translating or drafting Chinese copy for the slide:
   - keep the wording short,
   - keep it idiomatic and fully Chinese when possible,
   - avoid jargon-heavy mixed-script lines unless the user explicitly wants that style.
3. Shorten before you stylize. If fidelity is weak, reduce copy length and simplify the background before changing the overall style pack.
4. Use calmer, text-safe zones and more structured layouts sooner than you would for English.

## Pasteable Chinese fidelity block

```text
Prompt instructions are in English. Render all on-slide text in printed Simplified Chinese exactly as provided. Use large bold clean sans-serif Chinese typography. Do not translate, paraphrase, summarize, stylize, or change any character. Do not add English letters. Keep the non-text illustration zone free of readable labels, chart text, document text, interface text, and stray Chinese words. If any character is uncertain, regenerate the exact provided Chinese instead of inventing new text.
```

Adjust `Simplified Chinese` to `Traditional Chinese` when needed.

## Fast heuristic

- Chinese + short title card or short quote: `L4`, `L5`, or `L6` can work if the scene gives you a very calm text-safe zone.
- Chinese + medium teaching/context slide: bias toward `L1`.
- Chinese + framework/checklist/process: bias toward `L2`.
- Chinese + heavy content: split early instead of shrinking the type.
