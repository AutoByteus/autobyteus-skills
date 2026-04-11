---
name: bilingual-style-article-writer
description: Write and revise publish-ready Chinese (WeChat) and English (Medium) articles in configurable author styles. Use when the user provides ideas, rough notes, or sample articles and asks Codex to match an existing style profile or create a new profile for any author, then iterate drafts until final.
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
- Ask for objective, audience, and one-sentence takeaway.
- Ask for expected technical depth (math rigor, engineering detail, examples, references).
- If user does not specify mode, default to `original-draft` in one language first.

2. Load the correct style profile.
- Read `references/style-registry.md`.
- Normalize profile id to lowercase hyphen-case (for example: `Ryan Zheng` -> `ryan-zheng`).
- If profile exists in registry, read its mapped file under `references/profiles/`.
- If example file exists for that profile in registry, load it before drafting.
- If profile does not exist, create `references/profiles/<profile-id>.md` from `references/profiles/profile-template.md`, add a row in `style-registry.md`, and set status to `bootstrapping`.
- For `bootstrapping` status, require 2-5 sample articles before final drafting.

3. Build the argument skeleton first.
- Produce title options.
- Produce a section-by-section outline with section purpose.
- State the thesis explicitly.
- List the evidence or examples each section will use.
- Confirm this skeleton with the user before full drafting.

4. Draft with native-language expression.
- For `original-draft`, write fully in the chosen source language.
- For `cross-language-conversion`, treat source article as the canonical logic and rewrite into target language with native flow.
- Keep the same thesis and argument skeleton across languages.
- Do not literal-translate paragraph by paragraph.
- Rewrite naturally for each language while preserving logic, examples, and claims.
- For math-heavy content, define symbols on first use and keep notation stable.

5. Run quality and style checks.
- Check logic continuity: each section must push the thesis forward.
- Check style alignment against the chosen profile constraints.
- Check platform fit using `references/platform-output-rules.md`.
- In `cross-language-conversion`, add fidelity checks:
- no claim loss
- no invented claims
- notation and terms stay consistent
- If the user asks for revisions, apply focused passes: `logic`, `voice`, `depth`, `length`, or `title`.

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
