---
name: deep-research-article
description: "Do deep research and synthesize it into one logically structured article with clear thesis, argument flow, evidence, objections, and takeaways. Use when the user wants thinking before slides: sermon notes, Bible passage study, policy/tech explainers, product narratives, or any topic where the presentation should be built from a strong reasoning artifact. Output includes (1) one cohesive article and (2) a slide-extraction table for turning the article into an image-only deck."
---

# Deep Research Article

## Overview (two artifacts)

Produce:
1) `article.md`: one coherent article with strong reasoning and transitions
2) `slide_extraction.md`: a table that maps the article into slide-sized claims + supporting evidence + suggested visuals

This skill is intentionally topic-agnostic. For image-only decks, pair it with the `infographic-powerpoint-deck` skill after the article is approved.

## Workflow

### Step 0 — Confirm constraints (ask 3–6 quick questions)

Ask only what’s necessary:
- Audience + use case (sermon, lesson, blog, internal memo)
- Desired length (minutes or word count)
- Language (CN/EN/bilingual) and tone (academic / pastoral / simple)
- For Bible: translation/version and whether to include cross-references
- For general topics: must-use sources or “no web research” constraint

### Step 1 — Research notes (separate from writing)

Start by choosing a source strategy (so “deep research” isn’t just vibes). See `references/source_strategy.md`.

Create a scratchpad of:
- Key definitions/terms
- What the text/topic actually claims (avoid assumptions)
- Alternative interpretations / objections
- 5–12 “load-bearing” facts with sources (if web research is used)

For Bible passages:
- Note structure (pericope boundaries), repeated words, contrasts, commands, warnings, comfort.
- Identify “center of gravity” (main burden) and what the text is **not** saying.

Recommended artifact: create `research_notes.md` using `references/research_notes_template.md`.

### Step 1b — Claim→evidence ledger (prevents unsupported leaps)

Before drafting, build a small table that forces every major claim to have an evidence anchor.
- Use `references/claim_evidence_ledger_template.md`.
- Mark each claim’s **confidence** and what would falsify it.

### Step 2 — Argument outline (the real engine)

Write an outline that is easy to defend:
- Thesis (one sentence)
- 3–6 supporting moves (each is a claim → evidence → implication)
- Guardrails: what to omit, what not to overclaim
- Transition logic: why move A leads to move B

### Step 3 — Draft `article.md`

Use the skeleton in `references/article_skeleton.md`.

Rules:
- Prefer short paragraphs with explicit signposting (“因此/所以/因为/然而”).
- Separate observation vs application.
- If you used web research: include a sources section with links (or footnotes).

### Step 4 — Logic QA pass

Run the checklist in `references/logic_qa_checklist.md` and fix issues before moving on.

### Step 4b — Iterate until it “locks” (human-like drafting)

Deep research writing is normally iterative. Use `references/iteration_protocol.md`:
- revise thesis/outline if QA reveals gaps
- rewrite sections for clarity and scope
- add/remove evidence so every claim is supported
- repeat QA until stop criteria are met

### Step 4c — Revision log (recommended for real iteration)

Humans keep track of what changed; do the same to avoid thrash:
- Add a short “Revision notes” section to `article.md`, or keep a separate `revision_log.md`.
- Use `references/revision_log_template.md`.

### Step 5 — Create `slide_extraction.md` (presentation-ready mapping)

Use the table template in `references/slide_extraction_template.md`.

Each slide row should have:
- Slide headline (one claim, not a topic)
- Exact quote(s) or evidence anchor
- 2–4 bullets (supporting logic)
- Visual scene suggestion (location + hero symbol set + props)
- “Text budget” note (short / medium / heavy) so slide layout can be chosen later

## Output files (recommended)

- `article.md`
- `slide_extraction.md`
- `research_notes.md` (recommended for iteration)
- `revision_log.md` (optional, but helpful)

## References
- Read `references/article_skeleton.md` when drafting `article.md`.
- Read `references/source_strategy.md` to pick sources and record uncertainty.
- Read `references/research_notes_template.md` to structure `research_notes.md`.
- Read `references/claim_evidence_ledger_template.md` to prevent unsupported claims.
- Read `references/logic_qa_checklist.md` for the reasoning QA pass.
- Read `references/iteration_protocol.md` for iterative improvement and stop criteria.
- Read `references/revision_log_template.md` to track iterations cleanly.
- Read `references/slide_extraction_template.md` to map an article to slide-sized units.
