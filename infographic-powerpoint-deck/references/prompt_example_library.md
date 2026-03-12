# Prompt example library

Use one nearby example before writing real slide prompts.
Copy the structure and wording pattern, not the exact content.

## Rule zero

- If your prompt says `text panel`, `left panel`, `card`, `caption box`, `rounded rectangle`, or `frosted panel`, you are explicitly asking the model to create a panel-based layout.
- Do not use those words for `L4`, `L5`, or `L6`.
- For cinematic, editorial, warm, airy, animated, and youth packs, start from a direct-overlay example first and only fall back to a split-panel example when the text is too dense.

## Anti-example: this wording causes a panel

Use this only when you truly want a split-panel slide:

```text
Use layout L1 left text panel with right narrative illustration.
Put a clean readable text panel on the left side covering about 55% of the slide.
Keep the right side secondary to the text panel.
```

Expected result:
- the model creates a visible text block or panel zone
- this is correct for structured split-panel slides
- this is wrong if the user wants text directly on the image

## Example A: cinematic-light context slide with direct overlay

Use when:
- story or context slide
- 1 title plus up to 4 short lines
- user wants text directly on the image

```text
Use layout L4 full-bleed scene with direct overlay.
Full-bleed image edge to edge.
Keep the figure group on the right half of the frame.
Reserve calm architectural negative space on the left for text directly on the image itself.
Let the text sit on a bright wall, sunlit colonnade surface, or soft daylight falloff rather than inside any shape.
No panel, no placard, no inset rectangle, no split-screen block, no pasted card.
```

## Example B: full-bleed lower-third quote or resolve slide

Use when:
- emotional beat, quote, prayer, or resolve
- 1 title plus 2 to 4 short supporting lines

```text
Use layout L6 full-bleed lower-third overlay.
Keep the lower third calmer and simpler so the text can sit directly on the image.
Put the text directly on the slide surface, not inside any shape.
No card, no panel, no ribbon, no rounded rectangle, no subtitle bar.
```

## Example C: legitimate split-panel slide

Use when:
- 5+ bullets
- multiple sections
- framework/checklist/comparison structure
- report-like or academic delivery matters more than cinematic immersion

```text
Use layout L1 left text panel with right narrative illustration.
Put the title and bullet sections inside the left text panel with generous spacing.
Keep the right illustration low-contrast and secondary.
```

When this example is correct:
- the panel is not a bug
- the structure is doing real readability work

## Example D: Simplified Chinese structured split slide

Use when:
- Simplified Chinese on-slide text
- medium-density teaching or strategy slide
- readability and text fidelity matter more than cinematic immersion

```text
Use layout L1 left text panel with right narrative illustration.
Prompt instructions are in English. Render all on-slide text in printed Simplified Chinese exactly as provided.
Use large bold clean sans-serif Chinese typography.
Do not translate, paraphrase, summarize, stylize, or change any character.
Do not add English letters.
Keep the right-side illustration free of readable labels, chart text, interface text, document text, and stray Chinese words.
Keep the right illustration calm and secondary.
```

Why this example exists:
- Chinese medium-density slides often hold fidelity better in a structured split layout
- the right-side image still carries narrative mood, but the text stays controlled
