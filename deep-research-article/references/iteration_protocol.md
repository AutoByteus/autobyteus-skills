# Iteration protocol (how humans improve a “deep research” article)

Use this after Step 4 (Logic QA) and before finalizing `article.md`.

## One iteration loop

1) **Run Logic QA**
- Use `references/logic_qa_checklist.md`.
- Identify the top 3 problems (not 20 small edits).
- Also run `references/mainline_coherence_gate.md` and `references/final_article_quality_gate.md`.

2) **Decide the fix type**
- **Thesis fix**: thesis is too broad/narrow/doesn’t match evidence → rewrite thesis + roadmap.
- **Outline fix**: moves are out of order, missing a premise, or duplicative → reorder or add a missing move.
- **Evidence fix**: claims lack support or have weak support → add quotes/data/citations; remove overclaims.
- **Clarity fix**: writing is correct but hard to follow → shorten paragraphs, add signposts, tighten definitions.
- **Mainline fix**: a section is factual but off-topic for user intent → cut/merge/reframe so it serves one roadmap move.

3) **Revise `article.md`**
- Keep structure stable unless outline changes.
- Prefer deleting weak claims over adding more content.
- Update the claim→evidence ledger if thesis/moves changed (so the deck won’t drift).
- Update “Open questions / uncertainty” so you know what’s still shaky.
- Run a one-pass relevance trim: for each section, add one sentence “why this section exists”; if you can’t, cut it.

If evidence coverage is weak:
- go back to source sweep and add better sources,
- update source dossier and extraction before rewriting.

4) **Write a short revision note (recommended)**
Add at the top of the file (or as a separate section) a 3–6 line note:
- What changed
- What is now stronger
- What is still uncertain (if anything)
- Quality score deltas (which gate dimensions improved/declined)

5) **Re-run Logic QA**
- Stop if you meet the stop criteria below.
- Otherwise repeat the loop.

## Stop criteria (when it’s “good enough” to build slides)

All must be true:
- Thesis matches the body’s proven claims.
- Each move has evidence + reasoning + implication.
- At least one strong objection/alternative is acknowledged and handled.
- No slide-critical claims rely on unstated premises.
- Language is consistent and readable (no jargon drift).
- If web research used: sources exist for load-bearing claims.
- Evidence gates are passed (`references/evidence_gates.md`).
- Mainline coherence gate is passed (`references/mainline_coherence_gate.md`).
- Final article quality gate is passed (`references/final_article_quality_gate.md`).

## Slide readiness check (fast)

Before creating `slide_extraction.md`, confirm:
- You can summarize the article in **6 slide headlines** (claims).
- You can point to the exact evidence anchor for each headline.
