---
name: bilingual-style-article-writer
description: Write and revise publish-ready Chinese (WeChat) and English (Medium) articles or factual technical notes in configurable author styles. Use when the user provides ideas, rough notes, or sample articles and asks Codex to match an existing style profile or create a new profile for any author, then iterate drafts until final.
---

# Bilingual Style Article Writer

Use this skill to convert raw ideas into clear, publishable writing with explicit voice control.

## Workflow

1. Lock the target before writing.
- Ask for mode: `original-draft`, `cross-language-conversion`, or `dual-draft`.
- Ask for platform: `WeChat`, `Medium`, or both.
- Ask for language: `Chinese`, `English`, or bilingual.
- In `cross-language-conversion`, ask for explicit `source language` and `target language`.
- Ask for author/style profile name.
- Ask for rhetorical mode: `essay`, `factual-technical`, `paper-like`, or `hybrid`.
- Ask for objective, audience, and one-sentence takeaway.
- Ask for expected technical depth (math rigor, engineering detail, examples, references).
- If user does not specify mode, default to `original-draft` in one language first.
- If user does not specify rhetorical mode, default to `factual-technical` for technical topics and `essay` only when the request clearly asks for a persuasive article.
- Do not assume that naming an author profile automatically authorizes high-rhetoric prose. Profile controls voice and structural habits; rhetorical pressure is a separate choice.
- If the user objects to prior drafts with phrases like `too salesy`, `too indirect`, `too much like an article about the article`, `too much contrast`, `too repetitive`, or `too detached`, treat those as hard style constraints for the next pass, not as soft preferences.

2. Load the correct style profile.
- Read `references/style-registry.md`.
- Normalize profile id to lowercase hyphen-case (for example: `Ryan Zheng` -> `ryan-zheng`).
- If profile exists in registry, read its mapped file under `references/profiles/`.
- If example file exists for that profile in registry, load it before drafting.
- If the selected profile defines internal variants or stance modes, choose one explicitly before outlining. Record it in working notes as `profile + variant + rhetorical mode`.
- Prefer profile variants that answer the user's actual stance request, not the loudest version of the profile.
- If profile does not exist, create `references/profiles/<profile-id>.md` from `references/profiles/profile-template.md`, add a row in `style-registry.md`, and set status to `bootstrapping`.
- For `bootstrapping` status, require 2-5 sample articles before final drafting.

3. Build the argument skeleton first.
- Produce title options.
- Produce a section-by-section outline with section purpose.
- For `essay`, state the thesis explicitly and list the evidence or examples each section will use.
- For `factual-technical` or `paper-like`, state the scope, system/object under discussion, evidence basis, and bounded conclusion path instead of forcing a debate frame.
- For derivation-heavy architecture or system articles, preserve the user's reasoning chain instead of jumping straight to the conclusion. Prefer: prior system -> who or what did the work -> what changed -> new decomposition -> outputs and boundaries -> UI or workflow consequence -> bounded conclusion.
- If the user provides a practical sequence such as `we used X -> it did Y -> we observed Z -> we changed to W -> we noticed Q`, preserve that sequence as the article spine instead of rewriting it into a generic essay structure.
- If the user supplies a more exact runtime or product mechanism during revision, replace the earlier generic explanation with that mechanism. Do not keep the vague abstraction once a more concrete causal chain is available.
- If the user distinguishes between `software as work surface`, `software as state holder`, `human as doer`, and `agent runtime as doer`, preserve those distinctions explicitly. Do not compress them into a cleaner but less accurate sentence.
- For product-builder or architecture-migration topics, prefer this default section order unless the user asks otherwise:
  1. prior system or workflow
  2. what it already did well
  3. where it started to break
  4. why the redesign was made
  5. what the new structure is
  6. what was observed after the change
  7. bounded practical implication
- Do not force a contrastive hook such as `not X, but Y` unless the user explicitly wants argumentative prose or the source material already depends on that turn.
- Confirm this skeleton with the user before full drafting.

4. Draft with native-language expression.
- For `original-draft`, write fully in the chosen source language.
- For `cross-language-conversion`, treat source article as the canonical logic and rewrite into target language with native flow.
- Keep the same thesis and argument skeleton across languages.
- Do not literal-translate paragraph by paragraph.
- Rewrite naturally for each language while preserving logic, examples, and claims.
- Preserve the chosen rhetorical mode across revisions and conversions. In `factual-technical` mode, prefer mechanism -> evidence -> implication order over persuasion-first framing.
- In builder-report narratives, prefer direct subject-first openings such as `In AutoByteus, we first used...` over detached meta-openers like `This article explains...` or `This note describes...`, unless the user explicitly wants report prose.
- Keep the subject exact at sentence level. If the draft says `runtime`, `system`, `application`, or `interface`, make sure the reader can tell which one it means from local context; use the longer noun when precision matters.
- For math-heavy content, define symbols on first use and keep notation stable.

5. Run quality and style checks.
- Check logic continuity: each section must push the central claim, scope explanation, or bounded conclusion forward.
- Check style alignment against the chosen profile constraints.
- Check platform fit using `references/platform-output-rules.md`.
- Check rhetorical fit:
- no sales tone unless explicitly requested
- no forced binary contrast
- no inflated claims beyond the provided evidence
- In `factual-technical` or `paper-like` mode, verify that observations or system description appear before strong conclusions and that causal claims stay bounded.
- If the chosen profile has variants, verify the draft stayed inside the selected variant instead of drifting into a louder neighboring variant.
- Check standards precedence in this order:
- factual accuracy from user-supplied corrections
- mechanism accuracy
- referent and terminology accuracy
- structure and logic flow
- voice/style matching
- platform polish
- Run a terminology-precision pass on technical drafts:
- keep `application logic`, `application UI`, `agent runtime`, `agent team runtime`, `delivery boundary`, and `artifact` distinct when the article relies on those distinctions
- if the user says the draft feels `vague`, assume some subjects are under-specified and expand them explicitly
- do not trade away causal accuracy just to make the sentence shorter or more elegant
- Check redundancy aggressively:
- each section must add at least one new fact, mechanism, example, or implication
- do not restate the same central claim in the opening, transition section, and conclusion unless the function clearly changes
- if one comparison table already carries the main contrast, do not add a second summary table that says the same thing
- trim repeated phrases such as `the important point is`, `this is why`, or `the practical value is` when they introduce no new information
- For builder narratives, verify the opening uses firsthand ownership language and that the body does not drift back into detached analyst narration.
- For revised drafts, verify that earlier user complaints have been actively removed rather than only softened.
- In `cross-language-conversion`, add fidelity checks:
- no claim loss
- no invented claims
- notation and terms stay consistent
- If the user asks for revisions, apply focused passes: `logic`, `voice`, `depth`, `length`, `title`, or `tone-temperature`.
- Strong extra revision passes for technical architecture articles:
- `subject-precision`: replace vague nouns with exact system components
- `derivation-flow`: ensure each section follows from the previous one rather than jumping to a conclusion early
- `transition-smoothing`: fix inter-sentence jumps where the referent or causal chain becomes hard to track

## Rhetorical Modes

- `essay`: argument-bearing, thesis-forward, suitable for Medium-style opinion or strategy pieces.
- `factual-technical`: neutral technical prose, scope-first, evidence-led, low rhetorical pressure.
- `paper-like`: more formal and report-like; emphasize definitions, observations, method, limitations, and bounded conclusions.
- `hybrid`: structurally clear article prose with restrained rhetoric; useful when the user wants readability without essay pressure.

When profile guidance and rhetorical mode conflict, obey the explicit rhetorical mode request.

## Direction Selection Cues

Map common user cues to writing direction explicitly:

| User cue | Default response |
| --- | --- |
| `too salesy`, `too much Medium tone`, `too much rhetoric` | switch to `factual-technical` or `paper-like`; lower rhetorical pressure immediately |
| `be direct`, `start from what we used`, `write from our product perspective` | choose builder-first structure and builder ownership voice |
| `too detached`, `sounds like someone else built it` | use `we built`, `we used`, `we observed`, `we changed` |
| `too repetitive`, `don’t repeat again and again` | remove duplicate summary sections, repeated contrast pivots, and second comparison tables |
| `more factual`, `scientific`, `paper-like` | lead with scope/mechanism/observation, not thesis compression |
| `this is not accurate` plus added mechanism detail | replace generic causal explanation with the new precise mechanism |
| `this feels vague` | run a terminology-precision pass and replace blurred nouns with explicit system components |

When multiple cues appear, obey them in this order: accuracy -> directness/ownership -> rhetoric reduction -> redundancy reduction -> polish.

## Output Modes

- `Outline`: title options plus detailed structure.
- `Single-language draft`: one full WeChat or Medium article.
- `Cross-language conversion`: source article -> target-language adapted article.
- `Bilingual pair`: CN + EN drafts with aligned thesis and argument order.
- `Polish pass`: revised draft plus compact change log.

## Resources

- `references/style-registry.md`: profile status and loading order.
- `references/profiles/profile-template.md`: template for any new author profile.
- `references/profiles/ryan.md`: deep style fingerprint from provided samples.
- `references/profiles/normy.md`: Normy bootstrapping profile (can be updated later).
- `references/examples/ryan-examples.md`: Ryan few-shot examples for EN/CN and conversion behavior.
- `references/examples/normy-examples.md`: placeholder for future Normy examples.
- `references/examples/example-template.md`: template for adding examples for any new profile.
- `references/platform-output-rules.md`: WeChat/Medium packaging rules.
