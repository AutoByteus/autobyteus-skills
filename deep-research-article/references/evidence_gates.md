# Evidence gates (hard checks before final article)

Run this with `logic_qa_checklist.md`.

## Gate 1 — Source sufficiency
- Normal mode: >= 8 sources
- Deep mode: >= 12 sources
- At least 2 source types (primary + secondary preferred)

If user/policy constraints make these minimums impossible:
- explicitly declare `constrained evidence mode`
- reduce claim strength and widen caveats
- do not present conclusions as high-confidence

## Gate 2 — Triangulation
- Every load-bearing claim has:
  - >= 2 independent sources, OR
  - explicit caveat and reduced claim strength

## Gate 3 — Counterevidence
- At least 2 meaningful counter-position sources are represented.
- The article addresses their strongest points, not strawmen.

## Gate 4 — Citation traceability
- Every major claim in `article.md` maps to source IDs in the ledger.
- Source links are present in the Sources section.

## Gate 5 — Time validity (when relevant)
- For time-sensitive topics, include recent sources and clearly state dates.
- If evidence may have shifted, explicitly mark uncertainty.

If any gate fails: return to source sweep/extraction before finalizing.
