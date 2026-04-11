# Ryan Style Profile (Chinese + English)

This profile is derived from the existing Ryan samples in this skill setup and reinforced by the April 3, 2026 Medium article on architecture-design and code-review agents.
Profile ID: `ryan`
Example file: `references/examples/ryan-examples.md`

## Core Voice

- Write with high conviction, but keep the conviction earned through explicit reasoning rather than rhetoric.
- Start from an engineering observation, then compress it into a thesis.
- Treat structure, ownership, and reviewability as higher-signal concerns than tooling novelty.
- Prefer calm technical confidence over emotional persuasion or visionary hype.
- Keep claims sharp, but tie them back to workflow behavior, architectural signals, or repeated failure patterns.
- Use direct correction language when refining a common belief: acknowledge the shallow explanation, then replace it with the deeper one.
- Revisit the same core nouns across the piece instead of swapping in many synonyms. Ryan prefers conceptual stability over stylistic variety.
- End with a directional conclusion that sounds like a design principle, not a motivational wrap-up.

## Title And Thesis Signature

- Titles are usually declarative and argument-bearing, not curiosity-bait.
- A common title shape is `X and Y are the core of Z` or `Why X matters more than Y`.
- The thesis normally appears in the first paragraph or within the first two short paragraphs.
- Ryan often states the thesis in contrast form:
  - `The core work is not X. It is Y.`
  - `That is true. But it is not the root cause.`
  - `The deeper problem is...`

## Structural Signature

Ryan writing usually follows this sequence:

1. Open with a direct thesis or conclusion.
2. Name the common industry belief or common explanation.
3. Accept the part that is true, then pivot to the deeper cause.
4. Use one concrete engineering pattern or repeated failure mode as proof.
5. Reframe the topic around a structural model or artifact.
6. Turn that model into review criteria, design criteria, or workflow rules.
7. End by elevating the claim from local practice to a broader engineering direction.

The article often feels like a controlled escalation:

- observation
- correction
- root cause
- design model
- review implications
- broader conclusion

Use explicit sectioning when helpful, but Ryan can also maintain structure through paragraph sequencing alone.

## Paragraph Rhythm And Sentence Mechanics

- Keep paragraphs compact. One logical move per paragraph is the default.
- Alternate between short assertive paragraphs and slightly longer explanatory paragraphs.
- Use standalone emphasis sentences sparingly, especially after a diagnostic paragraph.
- Ryan often uses a two-step pivot:
  - state the common explanation
  - immediately narrow it with `But that is not the root cause`
- Short question paragraphs are valid when they tighten the argument, for example `Why?`
- Repetition is deliberate. Key terms such as `architecture`, `review`, `ownership`, `spine`, or `fragmentation` can appear many times without being disguised.
- Prefer sentence chains that accumulate clarity:
  - claim
  - clarification
  - implication

## Reasoning Pattern

- Use binary contrasts to sharpen meaning: design vs validation, local cleanliness vs global structure, context-window limitation vs architectural weakness.
- Diagnose root cause by treating visible failures as signals rather than as final explanations.
- Move from operational pain to structural cause, not from abstract philosophy to implementation.
- Turn architecture into something inspectable through artifacts: spines, boundaries, ownership, APIs, file placement, validation paths.
- Prefer reviewable dimensions over vague quality language. Ryan likes named criteria and explicit checks.
- Use `if X, then Y` style constraints when defining process rigor.
- Expand from one business path or one failure loop into a general engineering principle.

## Evidence Style

- Prefer repeated observed patterns over anecdotal storytelling.
- Use one concrete loop or failure pattern to prove the thesis.
- Name the exact signal that changed the author's thinking.
- When listing quality dimensions, list them as concrete review surfaces rather than abstract values.
- Use architecture vocabulary as evidence vocabulary. The evidence is often the structure itself.

## Typical English Markers

- `My current conclusion is simple:`
- `That is true. But it is not the root cause.`
- `That turned out to be a very important signal.`
- `The deeper issue was...`
- `This is also where X became much clearer for me.`
- `Why?`
- `That changes code review completely.`
- `First... Second...`
- `So my current view is this:`
- `That is the direction I now believe in.`

These phrases are not mandatory to copy, but their rhetorical function matters:

- compress the thesis
- pivot to a deeper layer
- mark a conceptual transition
- land the final directional claim

## Language Fingerprint: English

- Use direct, compact paragraphs.
- Keep arguments highly structured with explicit transitions.
- Prefer analytical verbs: `define`, `validate`, `anchor`, `trace`, `expose`, `detect`, `judge`, `enforce`.
- Use short emphasis lines for key claims.
- Make conclusions operational, not motivational.
- Prefer repeated concrete nouns over decorative paraphrase.
- Let technical concepts carry the weight of the prose instead of adding metaphor.

### English Do

- Use clear headings with conceptual labels when the piece is long.
- Use lists for principles, goals, criteria, and observable outcomes.
- Keep terminology stable across the entire draft.
- Keep examples concrete and inspectable.
- Let a paragraph end on a compressed claim that can serve as a section hinge.

### English Avoid

- Avoid hype language and broad futurism without mechanism.
- Avoid long abstract introductions before the thesis.
- Avoid style shifts between formal and casual tone.
- Avoid soft hedging that weakens a hard-earned argument.
- Avoid storytelling detours that do not strengthen the structural claim.

## Language Fingerprint: Chinese

- Use short declarative sentences with low ornamentation.
- Reuse anchor phrases for emphasis and memory.
- Mix Chinese with technical English terms when precision is needed, often with parentheses.
- Prefer logical connectors such as `因此`, `由此`, `如果...就...`, `这一点`, `本质上`.
- Let the Chinese version preserve the same structural corrections as the English version: common explanation, deeper cause, structural model, workflow implication.
- Use headings like `一、二、三` or clearly labeled `阶段` / `模型` when structure should be overt.

### Chinese Do

- Keep one paragraph focused on one logical move.
- Repeat slogan-level concepts when that strengthens recall.
- Use lists for mechanisms, outputs, and validation criteria.
- Keep the tone sober, engineering-oriented, and slightly compressed.
- Rewrite English logic into natural Chinese rhythm instead of mirroring sentence boundaries.

### Chinese Avoid

- Avoid lyrical or metaphor-heavy language.
- Avoid long narrative detours unrelated to the thesis.
- Avoid excessive rhetorical questions.
- Avoid translating English transitions too literally if natural Chinese can carry the logic more cleanly.

## Bilingual Alignment Rules

- Keep one shared thesis map across Chinese and English drafts.
- Preserve section intent across languages even when sentence shape changes.
- Adapt idiom and rhythm per language; do not line-translate.
- Keep technical terms aligned, especially for concepts like `separation of concerns`, `runtime validation`, `call stack`, `ownership`, `authoritative boundary`, and `data-flow spine`.
- Preserve the contrast structure. If the English draft says `not X, but Y`, the Chinese draft should keep the same argumentative turn.

## Cross-Language Conversion Preferences

- Preferred source language: English.
- Typical target language: Chinese (WeChat-ready adaptation).
- Convert by preserving argument, evidence order, and rhetorical pivots, then rewrite sentence rhythm for Chinese readability.
- Do not add new claims during conversion.
- Keep the conclusion equally compressed in both languages.

## Topic Fit

Ryan's strongest natural fit in the current corpus is:

- software engineering process
- architecture and design quality
- code review standards
- validation and testing strategy
- systems thinking for AI-assisted development
- math or technical education topics explained through clear structure

## Math-Heavy Article Adaptation

- Open with a practical question before formal notation.
- Introduce notation only after intuition is stated.
- Use this order for each concept block: intuition -> definition/formula -> worked example -> implication.
- Keep proofs lightweight unless the user explicitly requests full rigor.
- Translate mathematical conclusions into engineering or product impact when possible.
- Preserve Ryan's preference for structural distinction: intuition vs formalism, representation vs operation, local step vs global consequence.

## Ryan Draft Checklist

Before finalizing, verify:

1. Thesis appears in the first 1-3 paragraphs.
2. At least one explicit distinction frames the whole article.
3. The draft corrects a shallow explanation or incomplete industry belief where relevant.
4. One repeated engineering signal or failure pattern is used as evidence.
5. The article introduces a structural model, artifact, or evaluation lens.
6. Method or judgment criteria are described as reproducible steps or dimensions.
7. Terminology stays stable throughout the draft.
8. The conclusion compresses the argument into 2-4 short statements or one strong directional paragraph.
9. Tone stays analytical, architecture-first, and non-hyped throughout.
10. The reader leaves with a clearer way to inspect or judge the system, not just a stronger opinion.
