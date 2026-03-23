# Prompt example library

Use one nearby example before writing real slide prompts.
Copy the structure and wording pattern, not the exact content.

## Rule zero

- If your prompt says `text panel`, `left panel`, `card`, `caption box`, `rounded rectangle`, or `frosted panel`, you are explicitly asking the model to create a panel-based layout.
- Do not use those words for `L4`, `L5`, or `L6`.
- Internal layout labels such as `L1`, `L4`, `L9`, or `L10` are for the skill, not for the image model. Prefer composition wording in the concrete prompt.
- For didactic boards, a good prompt may still be highly structured without asking for visible boxes. Structure can come from zones, dividers, arrows, alignment, and spacing rhythm.
- For cinematic, editorial, warm, airy, animated, and youth packs, start from a direct-overlay example first and only fall back to a split-panel example when the text is too dense.

## Anti-example: this wording causes a panel

Use this only when you truly want a split-panel slide:

```text
Use a classic structured split slide with a left text zone and a right narrative illustration zone.
Put a clean readable text panel on the left side covering about 55% of the slide.
Keep the right side secondary to the text panel.
```

Expected result:
- the model creates a visible text block or panel zone
- this is correct for structured split-panel slides
- this is wrong if the user wants text directly on the image

## Anti-example: this wording is too generic for high fidelity

Do not stop here:

```text
Create a 16:9 slide in editorial-light didactic style.
Use a concept explainer board.
Make it clean and readable.
```

Why this is weak:
- it names style and layout, but does not tell the model what geometry to build
- it gives no palette, material, divider, typography, or module instructions
- it leaves too much room for generic output
- it can also cause the model to invent decorative divider lines everywhere because the hierarchy is underspecified

## Anti-example: this wording leaks tool mechanics into the prompt

Do not write prompts like this:

```text
Edit this image and replace the placeholder text.
Use the input image as an edit target.
I know you may not be able to edit images, but try to keep the same layout.
```

Why this is weak:
- it talks like a tool API instead of art direction
- it invites the model to respond at the capability layer instead of the visual-result layer
- it wastes prompt budget on mechanics the tool call already handles

Better:

```text
Using the provided image as the compositional base, keep the same overall board geometry and rebuild the slide as a finished teaching board.
Preserve the current module structure and imagery zones.
Replace all placeholder text with the exact required text and remove every stray label or extra symbol.
```

## Example A: cinematic-light context slide with direct overlay

Use when:
- story or context slide
- 1 title plus up to 4 short lines
- user wants text directly on the image

```text
Use a full-bleed scene with direct overlay.
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
Use a full-bleed lower-third overlay.
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
Use a classic structured split slide with a left text zone and a right narrative illustration zone.
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
Use a classic structured split slide with a left text zone and a right narrative illustration zone.
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

## Example E: didactic mirrored comparison explainer

Use when:
- expectation vs reality
- before vs after
- old model vs new model
- two experiments or two cases must be compared side by side with labels

```text
Use a mirrored two-zone teaching board with a central divider.
Put one large title row across the top.
Split the lower body into two mirrored teaching zones with a central divider.
Each side may include a short subhead, a labeled diagram, one process arrow, and one short result line.
Keep the background bright and diagram-friendly, not scenic.
Every visible label, formula, and annotation must be included in the required on-slide text.
Do not invent extra labels.
```

## Example F: concept explainer board

Use when:
- one historical figure, model, or concept anchors the slide
- the top half needs one hero portrait/object/diagram
- the lower half needs strengths vs weaknesses, claim vs limitation, or cause vs effect

```text
Use a concept explainer board.
Put the title across the top.
Use the upper band for one portrait, object, or concept diagram plus one short caption.
Split the lower band into two analytical blocks with strong section headers.
Allow more visible words than a keynote slide, but keep the board clean and self-contained.
Do not let the model improvise extra labels beyond the provided text.
```

## Example F2: high-fidelity concept explainer board

Use when:
- the slide needs a more polished, specific didactic result
- the generic board prompt is not enough

```text
Use a bright concept explainer board on a warm off-white paper-like surface.
Place one strong title row across the top left, occupying roughly the top 18% of the slide.
Use the upper middle band for one large portrait or concept diagram, centered slightly left, with one short caption directly beneath it.
Split the lower half into two analytical blocks with a thin vertical divider and aligned section headers.
Use dark slate text, muted deep-blue section headers, and one restrained soft-gold hairline rule for emphasis.
Keep the typography disciplined: large editorial or academic title, clean readable body text, strong spacing, no tiny labels.
Use thin-line diagrams, precise process arrows, and clean module edges rather than scenic atmosphere.
Keep the board bright, quiet, and self-contained with no cinematic clutter, no decorative background scene, and no extra labels beyond the provided text.
```

## Example G: catalog grid / repertoire board

Use when:
- four or six methods / reactions / categories / cases must appear on one slide
- the slide should stand alone as a compact teaching board

```text
Use a catalog teaching grid.
Put the title across the top.
Below it, create a 2x2 or 2x3 teaching grid with thin dividers and generous whitespace.
Each module may contain one short header, one or two descriptor lines, and a mini diagram or icon.
Keep the background almost white and highly readable.
Every visible module label must be included in the required on-slide text.
```

## Example H: reference-guided board refinement

Use when:
- a prior generated base image already has the right overall structure
- the final slide should preserve the composition but improve text fidelity or cleanliness

```text
Using the provided image as the compositional base, keep the same board geometry, divider placement, and overall bright editorial teaching style.
Preserve the upper hero diagram zone and the lower analytical blocks.
Rebuild the slide as a clean finished teaching board with exact readable text and no placeholder chrome.
Render only the required title, section text, and footer reference.
Remove every stray label, lorem ipsum fragment, arrow stub, dot cluster, watermark, and extra symbol.
```

## Example I: whiteboard-sketch technical explainer

Use when:
- the user wants a hand-drawn teaching feel
- the slide needs technical detail but should still feel approachable
- diagrams, arrows, and UI/process modules are part of the teaching style

```text
Create a bright whiteboard-sketch explainer slide on a warm paper-white surface with faint sketchbook texture.
Use a large clean bold title, crisp readable body text, and blue marker-like arrows and accent strokes.
Build the slide as a concept board with one strong title row, one central diagram or UI sketch module, and one right-side or lower-side explanation block.
Keep the text typed and readable, but let the arrows, boxes, and icons feel hand-drawn.
Use rounded sketch-outline boxes, thin blue connector lines, and restrained doodled technical callouts.
Keep the slide bright, friendly, and self-contained with no cinematic shading and no corporate gloss.
```

Better when the reference feels organized but not boxed:

```text
Create a bright whiteboard-sketch explainer slide on a warm paper-white surface with faint sketchbook texture.
Let the slide feel carefully choreographed rather than templated.
Use one strong title row, one central teaching diagram, and surrounding explanation zones arranged by spacing, curved arrows, and alignment rather than heavy card containers.
Keep the text typed and readable, but let the connectors, dividers, and emphasis strokes feel hand-drawn in blue marker.
Use only light separator strokes or soft implied lanes where needed; avoid turning every section into a visible rectangle.
Keep the slide bright, technical, and self-contained with no cinematic shading and no corporate gloss.
```

## Example J: illustrative-cinematic teaching board

Use when:
- the user wants immersive illustrative atmosphere without sketch-note roughness
- the slide should feel scene-rich and cinematic, but still teach clearly
- the deck needs more information than a sparse keynote slide

```text
Create a bright illustrative-cinematic teaching slide on a warm ivory board with subtle vellum or plaster-like texture.
Build the slide as an immersive concept board rather than a visible template.
Place one strong title row across the top with generous breathing room.
Let the background carry a polished illustrated environment with soft spatial depth, such as an atrium, archive, bridge, city threshold, or symbolic interior that supports the teaching theme.
In the main teaching area, arrange one hero diagram, object grouping, or figure cluster with surrounding explanatory modules choreographed by spacing, divider rhythm, and elegant arrows rather than heavy card boxes.
Use dark slate text, muted deep-blue structure lines, and restrained soft-gold emphasis accents.
Keep the information richer than a keynote slide but cleaner than a textbook scan: readable labels, calm hierarchy, and no scratchy strokes, no doodle marks, and no visible whiteboard feel.
```

## Density note

- Do not assume a good infographic slide is always low-text.
- Some decks are sparse keynote decks.
- Others are self-contained didactic infographics where more words are correct because the slide itself is delivering the explanation.
- In those cases, route into `L9`, `L10`, or `L11` instead of stripping information away.
- When the user wants higher fidelity, increase specificity rather than only increasing adjectives. Good prompts get better by adding concrete geometry, palette, material, divider, and typography instructions.
