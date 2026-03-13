# Layout routing policy (default: automatic)

Use this file when the user does **not** explicitly request per-slide layouts.
The skill should normally choose layouts automatically from slide role, text budget, and overall deck tone.

## User model

- User usually provides:
  - raw article content or notes
  - topic
  - audience
  - overall style / mood
- User usually does **not** provide:
  - per-slide layout instructions
- Therefore:
  - layout selection is an internal skill decision by default
  - `Layout hint` is an optional override, not a required user input
  - if a workflow uses structured planning, that hint belongs in `slides_visual_plan.md`, not `slides_message_plan.md`

## Deck-level layout bias (optional)

If the user gives an overall presentation bias, or if one is implied by the chosen deck archetype or recorded in `slides_visual_plan.md`, use it to influence the routing mix:

- `balanced` (default):
  - mix split-panel and full-bleed layouts according to slide role and text budget
- `direct-overlay-first`:
  - prefer `L4`, `L5`, `L6` for any slide that can fit 1 title plus up to 4 short lines in a calm text-safe zone
  - use `L1`, `L2`, `L3`, `L7`, `L8` only when structure or density truly requires them
- `cinematic` or `full-bleed-heavy`:
  - prefer `L4`, `L5`, `L6` whenever text budget allows
- `structured`, `teaching`, or `report-like`:
  - prefer `L1`, `L2`, `L7`; use `L4`/`L5`/`L6` mainly for openings, transitions, and closings
- `dense` or `study-heavy`:
  - prefer `L1`, `L2`, `L3`; split slides early instead of forcing too much text into full-bleed layouts
- `didactic`, `classroom`, `self-contained`, or `knowledge-poster`:
  - prefer `L9`, `L10`, `L11`, then `L2`, `L7`, and `L3`
  - allow more on-slide text when each section is explicitly structured, labeled, and diagram-led

## Per-slide auto-routing rules

If `Layout hint` is provided in `slides_visual_plan.md` or directly by the user, use it unless readability clearly fails.
If `Layout hint` is blank or missing, route automatically:

1. By slide role:
   - opening / section opener / closing -> `L5` first, then `L4` or `L6`
   - quote / emotional beat / transition -> `L6` or `L4`
   - context / key-claim / application with 1 title + up to 4 short lines -> `L4` or `L6` first when a calm text-safe zone can be built into the scene
   - teaching / key-claim / application with denser bullets, multiple sections, or framework structure -> `L1`
   - framework / checklist / process -> `L2`
   - comparison / contrast / objection -> `L7`
   - warning / deception / credibility alert -> `L8`
   - evidence-dense / long list -> `L3`
   - expectation-vs-result / before-vs-after / mirrored experiment / A-vs-B teaching comparison -> `L9`
   - concept explainer / theory model / historical figure + idea / strengths-vs-weaknesses board -> `L10`
   - repertoire / taxonomy / reaction family / 2x2 or 2x3 teaching grid -> `L11`

2. By text budget:
   - `short` -> prefer `L4`, `L5`, `L6`
   - `medium` -> prefer `L4`, `L6`, `L1`, `L2`, `L7`
   - `heavy` -> prefer `L3`, `L9`, `L10`, or `L11` before splitting if the slide is diagram-led and the sections are strongly structured
   - if the rendered text is Chinese or another CJK script and the slide is `medium` or `heavy`, bias one step earlier toward `L1` or `L2` unless the scene clearly provides a very calm direct-overlay text zone

3. By style fit:
   - cinematic, editorial, warm, airy, animated, and youth packs should default to `direct-overlay-first` unless the content is clearly structured or dense
   - cinematic packs tolerate more `L4`, `L5`, `L6`
   - research / corporate packs tolerate more `L1`, `L2`, `L3`, `L7`, `L9`, `L10`, `L11`
   - editorial-light can also support didactic poster layouts when the content needs self-contained teaching density
   - warm/editorial packs often work well as mixed decks, but should not be forced into sparse slides when the article clearly needs labeled teaching boards

## Prompt-wording guardrail

- If you choose `L1`, `L2`, `L3`, `L7`, `L8`, `L9`, `L10`, or `L11`, panel/board wording is expected because those layouts intentionally create structured information zones.
- If you choose `L4`, `L5`, or `L6`, do **not** write `text panel`, `left panel`, `caption box`, `card`, `rounded rectangle`, `frosted panel`, or similar wording in the prompt.
- If the user prefers text directly on the image, reroute away from `L1` before writing the prompt unless the slide is genuinely too dense for an overlay-safe composition.
- If you choose `L9`, `L10`, or `L11`, list every visible heading, label, formula caption, module title, and diagram annotation in the required on-slide text set rather than leaving them implicit.

## Override rules

- If the user explicitly requests one layout for the whole deck, follow that.
- If the user explicitly requests one slide treatment family, bias toward it but still protect readability.
- If the chosen layout causes text crowding, switch to a denser readable layout or split the slide.
- If a full-bleed slide starts producing boxed captions or cramped text, reroute to a cleaner full-bleed composition or a split-panel layout as needed.
