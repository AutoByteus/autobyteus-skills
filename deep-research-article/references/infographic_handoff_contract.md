# Infographic handoff contract (`deep-research-article` → `infographic-powerpoint-deck`)

Purpose: make `slide_extraction.md` directly consumable by the infographic skill with minimal remapping.

## Required columns in `slide_extraction.md`

1) `Slide`  
2) `Headline (claim)`  
3) `Must-appear text (verbatim)`  
4) `Evidence anchor + source ID(s)`  
5) `Supporting bullets (2–4)`  
6) `Recommended style pack ID`  
7) `Scene ID`  
8) `Layout hint`  
9) `Text budget`

## Allowed values

- `Recommended style pack ID`:
  - `cinematic-dark`
  - `editorial-light`
  - `airy-relaxed`
  - `clean-corporate`
  - `warm-sermon`
  - `neo-tech`
  - `youth-social`
  - `research-academic`

- `Layout hint`:
  - `L1`, `L2`, `L3`, `L4`, `L5`, `L6`

- `Text budget`:
  - `short`, `medium`, `heavy`

## Mapping guidance

- If `Text budget=short`, prefer `L1` or `L4`.
- If `Text budget=medium`, prefer `L1`, `L2`, or `L5`.
- If `Text budget=heavy`, prefer `L3`; if still too dense, split into two slides.

## Quality checks before handoff

- Every row has at least one source ID for load-bearing claims.
- `Must-appear text` is copy-paste ready (no TODO placeholders).
- `Scene ID` exists in infographic scene catalog (or uses `custom:<slug>`).
- `Recommended style pack ID` is selected intentionally, not blank by default.
