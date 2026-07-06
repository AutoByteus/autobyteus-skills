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
- Ground factual claims in the user's source material, corrections, cited evidence, or clearly marked inference. Do not invent product behavior, motivations, outcomes, timelines, or causal mechanisms to make the prose feel complete.
- Use direct correction language when refining a common belief: acknowledge the shallow explanation, then replace it with the deeper one.
- Revisit the same core nouns across the piece instead of swapping in many synonyms. Ryan prefers conceptual stability over stylistic variety.
- Prefer exact referents over rhetorical compression. If the article distinguishes between human doer, software work surface, application logic, agent runtime, and delivery boundary, keep those nouns separate instead of collapsing them into one cleaner but less accurate word.
- End with a directional conclusion that sounds like a design principle, not a motivational wrap-up.
- Keep structural clarity as the invariant, but treat rhetorical intensity as adjustable.
- Do not force correction language, binary contrast, or manifesto energy when the user asks for factual or paper-like prose.
- When the author is describing their own product, workflow, or runtime change, prefer builder ownership language such as `we used`, `we observed`, and `we changed`.

## Important Boundary

- Ryan's strongest samples in this skill are essay-like Medium pieces.
- That does not mean every Ryan-aligned draft should sound like a strategy essay.
- If the user asks for `factual`, `scientific`, `paper-like`, `technical note`, `architecture note`, or objects to sales tone, keep Ryan's structure discipline and terminology stability but downshift the rhetoric.

## Ryan Variant Map

Treat Ryan as one writing system with multiple controlled variants, not as one fixed sound.

| Variant | Use when | Opening stance | Allowed pressure | Main risk to avoid |
| --- | --- | --- | --- | --- |
| `essay-thesis` | the user wants a strong Medium argument or strategic viewpoint | direct thesis in paragraph 1 | medium to high | sounding like a manifesto when evidence is still thin |
| `factual-technical` | the user wants a technical explanation or engineering note | scope, mechanism, or main observation first | low | drifting into unnecessary contrast or commentary |
| `builder-direct` | the user is describing their own product, workflow, runtime change, or internal observation | `we used`, `we observed`, `we changed` | low to medium | slipping back into detached analyst prose |
| `paper-report` | the user wants a more formal, report-like, or scientific style | scope, method, observations, limitations | low | becoming dry but still carrying essay pivots |

Default selection:

- if the user speaks from firsthand product/workflow ownership, choose `builder-direct`
- if the user asks for factual or technical explanation, choose `factual-technical`
- if the user asks for scientific/report-like prose, choose `paper-report`
- use `essay-thesis` only when the user clearly wants argument pressure

## Direction Cues And Override Rules

Use the user's revision language as a hard routing signal:

| User feedback | Ryan direction change |
| --- | --- |
| `too salesy`, `too much Medium tone`, `too much rhetoric` | move to `factual-technical` or `paper-report`; remove contrastive hooks unless essential |
| `be direct`, `start with what we used`, `write practically` | move to `builder-direct`; start from prior system state |
| `sounds like someone else built it` | restore builder ownership language throughout |
| `too repetitive` | compress transitions and remove repeated restatements of the same central claim |
| `not accurate` plus new details | replace generic mechanism with the user-supplied causal chain immediately |

Revision precedence inside Ryan:

1. factual accuracy
2. mechanism accuracy
3. ownership stance
4. logical flow
5. rhetorical pressure
6. sentence polish

## Title And Thesis Signature

- Titles are usually declarative and argument-bearing, not curiosity-bait.
- A common title shape is `X and Y are the core of Z` or `Why X matters more than Y`.
- The thesis normally appears in the first paragraph or within the first two short paragraphs.
- Ryan often states the thesis in contrast form:
  - `The core work is not X. It is Y.`
  - `That is true. But it is not the root cause.`
  - `The deeper problem is...`
- In factual technical mode, titles may be descriptive rather than argumentative.
- In factual technical mode, the opening may begin with scope, implementation context, or observed behavior instead of a contrastive thesis.
- In builder-report mode, the opening may begin directly from the prior system state: what was used, what it was supposed to do, and where it started to break.
- In paper-report mode, the opening may begin from scope, system boundary, or observed runtime condition without any thesis compression at all.

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

### Builder-Report Variant

When the user is describing their own system evolution, prefer this sequence:

1. what we were using
2. what that system already did well
3. where it started to break
4. why we changed the design
5. what the new structure is
6. what we observed after the change
7. what bounded conclusion follows

This variant should feel direct and practical. Do not open with `This article explains...` or `This note describes...` if a concrete builder opening is available.

When the article is a derivation about architecture or system structure, builder-direct can also use this sequence:

1. what the older system was
2. who or what was actually doing the work
3. what changed
4. what the new decomposition is
5. what new boundary or artifact model follows
6. what practical UI or workflow consequence follows
7. what bounded conclusion follows

### Paper-Report Variant

When the user wants a more scientific or report-like article, prefer this sequence:

1. scope or system under discussion
2. relevant implementation or workflow structure
3. observed behavior or limitation
4. mechanism behind that behavior
5. redesign or comparison if relevant
6. bounded conclusion
7. limitations or next implications when useful

This variant should feel factual and low-pressure. It should not inherit Medium-style thesis pressure by accident.

## Rhetorical Pressure Control

Use one of these pressure levels explicitly:

- `Low`: factual technical prose. Start from scope, implementation, builder context, or observation. Keep conclusions bounded. Prefer direct system openings when the author is speaking from firsthand product experience.
- `Medium`: Ryan's normal technical-essay mode. Thesis appears early, but claims still stay mechanism-backed.
- `High`: only when the user clearly wants manifesto, strong persuasion, or founder-style positioning.

Default to `Low` for technical requests unless the user explicitly asks for a more argumentative article.

Variant-pressure alignment:

- `essay-thesis` normally uses `Medium`
- `factual-technical` normally uses `Low`
- `builder-direct` normally uses `Low` or restrained `Medium`
- `paper-report` uses `Low`

## Ryan Factual Technical Variant

When the user wants paper-like or report-like prose:

- keep Ryan's structural discipline and repeated terminology
- reduce thesis pressure in the opening
- present mechanism and evidence before interpretation
- replace sharp correction language with bounded statements
- avoid `not X, but Y` unless it is truly necessary
- avoid lines such as `that changed everything`, `the future is`, or `what changed our thinking` unless reflective voice is explicitly requested
- let the conclusion sound like a constrained finding, not a slogan
- avoid detached report openers such as `this note describes` when the user wants direct builder voice
- avoid reopening the same claim in the intro, body transition, and conclusion when one clear statement is enough
- avoid switching variants mid-draft, such as opening in `builder-direct` and closing in `essay-thesis`

## Paragraph Rhythm And Sentence Mechanics

- Keep paragraphs compact. One logical move per paragraph is the default.
- Alternate between short assertive paragraphs and slightly longer explanatory paragraphs.
- Use standalone emphasis sentences sparingly, especially after a diagnostic paragraph.
- Ryan often uses a two-step pivot:
  - state the common explanation
  - immediately narrow it with `But that is not the root cause`
- Short question paragraphs are valid when they tighten the argument, for example `Why?`
- Repetition is deliberate. Key terms such as `architecture`, `review`, `ownership`, `spine`, or `fragmentation` can appear many times without being disguised.
- Repeated terminology is not the same as repeated claims. Reuse key nouns, but do not restate the same paragraph-level point unless it advances the argument.
- Prefer sentence chains that accumulate clarity:
  - claim
  - clarification
  - implication
- When the draft uses words like `runtime`, `system`, `surface`, or `application`, make sure the referent is recoverable in the same paragraph. Ryan prefers stable referents to stylistic variation.

## Reasoning Pattern

- Use binary contrasts to sharpen meaning: design vs validation, local cleanliness vs global structure, context-window limitation vs architectural weakness.
- Diagnose root cause by treating visible failures as signals rather than as final explanations.
- Move from operational pain to structural cause, not from abstract philosophy to implementation.
- For architecture derivation articles, move from prior system decomposition to new decomposition before claiming UI or workflow consequences.
- Turn architecture into something inspectable through artifacts: spines, boundaries, ownership, APIs, file placement, validation paths.
- Prefer reviewable dimensions over vague quality language. Ryan likes named criteria and explicit checks.
- Use `if X, then Y` style constraints when defining process rigor.
- Expand from one business path or one failure loop into a general engineering principle.

## Evidence Style

- Prefer repeated observed patterns over anecdotal storytelling.
- Use one concrete loop or failure pattern to prove the thesis.
- In essay mode, naming the exact signal that changed the author's thinking can be effective.
- In factual technical mode, state the observation directly instead of dramatizing the signal.
- When the user provides a more exact runtime explanation, prefer that exact mechanism over a broader abstract summary.
- If the source material does not establish a causal bridge, keep the transition bounded or ask for the missing mechanism instead of supplying a plausible explanation as fact.
- Preserve distinctions like `software as work surface` versus `human as doer` when the article depends on that difference.
- When listing quality dimensions, list them as concrete review surfaces rather than abstract values.
- Use architecture vocabulary as evidence vocabulary. The evidence is often the structure itself.
- If a table already captures the main mechanism or comparison, the prose around it should interpret or transition, not restate the same rows.

## Anti-Patterns

Avoid these common Ryan failure modes:

- opening with detached meta-lines like `This article explains...` when builder-direct voice is clearly better
- using `not X, but Y` multiple times in the same draft when one direct sentence would be clearer
- sounding like an outside analyst when the article is about the author's own system
- keeping a generic high-level explanation after the user has supplied a more precise mechanism
- collapsing distinct system components into vague nouns like `runtime`, `system`, or `interface` after the user has already clarified the boundary
- restating the same conclusion in the introduction, a transition section, and the ending
- using a second table or closing summary that merely repeats the first comparison table

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

These phrases are essay-mode markers, not mandatory defaults. Use them only when the requested rhetorical mode actually needs that pressure.

Builder-direct markers:

- `In AutoByteus, we first used...`
- `For small tickets, this worked well.`
- `When the tasks became larger, we started to see...`
- `That is why we changed...`
- `After the split, we noticed...`
- `The cost was not only task context...`
- `Part of the token budget was being spent on maintaining the workflow itself...`

Paper-report markers:

- `The current workflow has...`
- `The observed limitation appears in...`
- `This behavior is most visible when...`
- `The main mechanism is...`
- `Taken together, these observations suggest...`

Low-rhetoric correction markers:

- `The earlier explanation was too broad.`
- `The more exact mechanism is...`
- `The main cost appeared in...`

Their rhetorical function matters:

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
- Avoid sales tone, founder evangelism, or product-marketing cadence unless explicitly requested.
- Avoid repeated `not X, but Y` pivots when a direct factual sentence would be clearer.
- Avoid interpretive phrases like `very important signal` when the underlying observation can be stated directly.
- Avoid inflated directional claims such as `the future is ...` unless the user clearly wants a visionary essay.
- Avoid opening in detached analyst mode when the user is clearly speaking as the builder.
- Avoid concluding in grand strategic language when the body stayed factual and bounded.

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
- Preserve the contrast structure only when the source draft actually uses it. Do not inject a `not X, but Y` turn during conversion if the source is factual or paper-like.

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
   In factual technical mode, a clear scope statement or main observation can replace a hard thesis hook.
2. At least one explicit distinction frames the whole article.
3. The draft corrects a shallow explanation or incomplete industry belief where relevant.
4. One repeated engineering signal or failure pattern is used as evidence.
5. The article introduces a structural model, artifact, or evaluation lens.
6. Method or judgment criteria are described as reproducible steps or dimensions.
7. Terminology stays stable throughout the draft.
8. The conclusion compresses the argument into 2-4 short statements or one strong directional paragraph.
9. Tone stays analytical, architecture-first, and non-hyped throughout.
10. The reader leaves with a clearer way to inspect or judge the system, not just a stronger opinion.
11. The rhetorical mode (`essay` vs `factual-technical` vs `paper-like`) is explicit and matched.
12. No sales-tone drift, forced contrast, or unearned persuasion remains in factual technical drafts.
13. The opening stance is correct for the request: thesis-first, scope-first, or builder-direct.
14. No duplicate summary section or repeated comparison table restates the same point without adding new information.
15. The Ryan variant (`essay-thesis`, `factual-technical`, `builder-direct`, or `paper-report`) is explicit and the draft does not drift into another variant.
16. If the piece is firsthand product narration, at least the opening and one later section clearly preserve builder ownership language.
17. If the user supplied a more precise runtime or workflow mechanism during revision, the final draft uses that mechanism instead of the earlier generic abstraction.
18. If the user objected to sales tone, detachment, or repetition, the final draft contains explicit evidence that those failure modes were removed.
19. No factual claim, product behavior, motivation, outcome, timeline, or causal mechanism is introduced without source support or an explicit inference marker.
