# High-fidelity prompt playbook

Use this when the deck quality bar is closer to polished keynote, editorial feature, teaching poster, or premium didactic slide than to a generic rough mockup.

The goal is not to add random adjectives. The goal is to make the final concrete prompt specific enough that the image model can build one particular slide, not a vague family of slides.

## What high fidelity means here

High-fidelity prompt writing means the concrete prompt names the main design systems of the slide:
- composition geometry
- text-safe zone placement
- palette and accent behavior
- material / surface feel
- typography attitude
- divider, grid, or module structure
- diagram or icon rendering language
- lighting and contrast behavior
- restraint rules and forbidden treatments

High fidelity does not mean decorative density.
Clean slides are usually higher fidelity than noisy slides because every visual decision is serving hierarchy rather than ornament.

If the prompt could describe many unrelated slides after changing only the title text, it is still too vague.

## Minimum design dimensions

The final concrete prompt should usually answer these questions in plain prose:

1. What canvas behavior is being used?
- split slide
- full-bleed overlay
- mirrored comparison board
- concept explainer board
- catalog grid

2. Where does the text live?
- left zone, lower third, top title band, calm wall area, two analytical blocks, 2x2 grid modules

3. What does the slide feel made of?
- paper, matte stone, frosted glass, warm concrete, neutral board, soft fabric grain

4. What are the actual colors?
- not `nice blue`
- instead `off-white board, dark slate text, muted deep-blue headers, restrained soft-gold rule`

5. What is the typography attitude?
- editorial serif title + clean sans body
- academic sans hierarchy
- geometric sans labels + heavier section headers

6. How is the slide structured?
- title row height
- number of lower modules
- divider placement
- module rhythm
- repeated geometry or not
- whether rules belong at the section boundary, under the heading, or not at all. Avoid redundant line systems that make the board feel busy.

7. What visual language renders the non-text content?
- thin-line diagrams
- outline icons
- precise arrows
- stylized 3D characters
- restrained realistic objects

8. How is lighting handled?
- flat academic illumination
- soft daylight with ambient fill
- rim light only on the hero side
- no vignette

9. What must be prevented?
- no boxed caption card
- no extra labels
- no busy texture through text
- no mixed styles

10. If a reference image is being used, what stays and what changes?
- what geometry stays
- what imagery zones stay
- what placeholder or unwanted elements disappear
- what exact text must replace the old content

## Layout-family expansion rules

### Split / structured slides

Do not stop at `left text / right image`.
Also specify:
- left/right proportion
- whether the panel is solid, translucent, or implied by negative space
- title alignment
- bullet spacing
- how quiet the illustration must remain

### Full-bleed overlays

Do not stop at `text directly on the image`.
Also specify:
- where the calm text-safe zone sits
- what material or environment the text sits on
- what local contrast support is allowed
- what kinds of boxes/cards are forbidden

### Didactic boards

Do not stop at `concept board` or `grid`.
Also specify:
- title band height
- exact lower module structure
- divider behavior
- board surface
- typography system
- diagram rendering language
- module rhythm and whitespace

## Typography guidance

For high fidelity, the prompt should usually include:
- title attitude
- body attitude
- label attitude
- footer/reference treatment

Examples:
- `Use a large editorial serif title with clean sans-serif body text and compact small-caps section labels.`
- `Use a disciplined academic sans hierarchy with heavier subheads, crisp body text, and restrained footer microcopy.`

Avoid generic lines like `nice font`, `clean font`, or `modern typography`.

## Material guidance

Material cues help the model make the slide feel designed:
- paper-white board
- warm off-white textured paper
- matte plaster wall
- low-reflection glass panel
- soft stone ledge
- brushed neutral poster field

These cues should be tied to the chosen style and layout, not added randomly.

## Precision rule

Better prompts do not just become longer.
They become more decision-rich.

Good:
- exact palette
- exact module structure
- exact contrast behavior
- explicit forbidden treatments
- one disciplined divider system, or none at all, instead of decorative extra lines

Weak:
- `modern`
- `clean`
- `premium`
- `high fidelity`

without any concrete expansion.

Reference/edit prompts follow the same rule:
- weak: `edit this image`, `replace the text in this image`
- better: `using the provided image as the compositional base, preserve the structure and rebuild the slide so that ...`

Keep tool mechanics out of the model-facing prompt.

## Final self-check

Before generating, ask:
- Could a designer sketch this slide from the prompt?
- Could the model know where the text sits?
- Could the model know what materials, colors, and type attitude to use?
- Could the model know what to avoid?

If not, the prompt still needs more specificity.
