# Reference slide intake

Use this when the user provides one or more example slides, screenshots, keynote slides, pitch-deck slides, or design references and says things like:

- `learn from this slide`
- `use this style`
- `follow this layout`
- `make the deck feel like this example`
- `add this as another style`

This is not model training. It is a reusable extraction workflow:
- inspect the reference
- abstract the visual grammar
- reuse that grammar in prompts
- optionally turn it into a new reusable style pack or prompt example

## What to extract from a reference slide

For each strong example, capture:

1. Layout family
- direct overlay or split-panel
- title-safe zone
- text anchor area
- whether the text sits on architecture/sky/light or inside a deliberate panel
- text density tolerance

2. Visual language
- palette
- brightness / contrast
- lighting direction
- texture level
- realism vs stylization
- cinematic vs editorial vs report-like feel

3. Typography behavior
- serif vs sans attitude
- title scale
- line spacing
- alignment
- spacing rhythm
- whether the text feels embedded into the scene or separated from it

4. Scene grammar
- figure placement
- camera angle
- depth treatment
- prop density
- how negative space is created for text

5. Anti-patterns to avoid
- obvious white box
- too many bullets
- poster-noisy clutter
- dark text on noisy background
- copied logos or branding marks

## Decision rule: what should be updated?

After extracting the reference, decide which reusable level it belongs to:

### A. One-off deck reference

Use when:
- the user only wants this look for the current deck
- the example is specific but not broad enough to justify a new pack

Do:
- add a short `reference-derived style note` to `slides_plan.md`
- use the reference image as an allowed input/edit reference if helpful
- write prompts using the extracted wording pattern

Do not:
- create a new style pack unless the pattern is clearly reusable

### B. Prompt example / layout example

Use when:
- the example mainly teaches a composition trick
- the same layout behavior could help many future decks

Do:
- add or update examples in `references/prompt_example_library.md`
- add routing notes in `references/layout_routing_policy.md` or `references/layout_library.md` if needed

### C. New style pack or style-pack refinement

Use when:
- the example has a distinct reusable visual language
- the user is likely to want the same family again
- palette, lighting, and text treatment are different enough from existing packs

Do:
- either refine the nearest existing pack
- or scaffold a new pack with `scripts/create_style_pack.py`
- register it in `references/style-pack-catalog.md`

## Reuse rule

When learning from a reference slide:
- abstract the design principles
- do not copy exact branding, logos, or copyrighted text
- translate the reference into reusable descriptors such as:
  - `direct-overlay-first`
  - `architectural negative space`
  - `editorial serif title with cinematic daylight`
  - `lower-third text anchored on calm sky`

## Output expectation

If a reference slide is provided, add a short section near the top of `slides_plan.md`:

- `Reference slide signals`
- `Chosen reusable interpretation`
- `Nearest style pack`
- `Any new prompt example or pack created`

## Fast heuristic

- If the user says `use this exact feel` and the slide is mostly one good composition idea, update `prompt_example_library.md`.
- If the user says `we will use this kind of look again and again`, refine or add a style pack.
- If the user only wants the current deck to resemble it, keep it local to the deck and use reference-derived prompt notes.
