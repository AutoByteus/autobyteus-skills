# Final article quality gate (human-like “ready to publish?” check)

Run this after logic/evidence/objectivity/mainline checks.

Score each dimension from 1 to 5:
- 1 = unacceptable
- 3 = workable but weak
- 5 = publication-ready

## Dimensions

1) **Mainline focus**
- The article stays on the declared mainline.
- Background/context supports the thesis instead of competing with it.
- No section feels “interesting but off-topic.”

2) **Reasoning quality**
- Claims, evidence, and implications are explicit.
- Transitions are causal/logical, not just sequential.
- Strongest objection is handled fairly.

3) **Evidence discipline**
- Load-bearing claims are traceable to source IDs.
- Triangulation/caveats match confidence level.
- No conclusion overstates evidence strength.

4) **Audience fit**
- Language, examples, and depth match intended audience.
- The reader can answer “what should I do with this?” after each major move.
- Tone matches user-requested style (e.g., practical, pastoral, academic).

5) **Actionability**
- Takeaways are specific enough to apply.
- Guardrails are concrete (not abstract warnings only).
- The article can be transformed into slide claims without ambiguity.

## Red-flag auto-fail conditions

Any one of these means fail:
- A core section fails the relevance test in `mainline_coherence_gate.md`.
- A load-bearing claim lacks a source ID or caveat.
- A major conclusion relies on a single weak/tertiary source.
- The article contradicts the declared out-of-scope boundary.

## Pass threshold

Pass only if:
- no red-flag auto-fail exists, and
- all five dimensions score >= 4.

If not passed:
- revise the top 2 weakest dimensions first,
- update `revision_log.md`,
- rerun this gate.

