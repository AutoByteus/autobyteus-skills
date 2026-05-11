# Platform Output Rules

Use these rules after style selection and before final delivery.

## WeChat (Chinese)

- Prefer concise title with a clear thesis signal.
- For builder or product-evolution topics, prefer direct openings such as `我们最开始用的是...` or `在 X 里，我们先用的是...` instead of detached meta-openers.
- Use clear section headings and visible structure.
- Keep paragraphs short for mobile reading.
- Use bullet lists for process steps and key claims.
- Use tables when they clarify stages, role decomposition, or mechanism differences, but avoid repeating the same comparison again in a later summary table.
- Keep technical terms precise; include English term in parentheses where helpful.
- For formulas, use readable LaTeX blocks and explain symbols in nearby text.
- End with a compact takeaway section ("最后的想法" style is acceptable).

## Medium (English)

- For `essay` mode, lead with thesis in the opening paragraph.
- For `factual-technical` or `paper-like` mode, lead with scope, system description, or the main observation instead of a polemical hook.
- For product-builder or system-evolution topics, prefer a direct opening from the prior system state (`we used X`, `it did Y`, `we observed Z`, `so we changed W`) instead of detached meta-openers.
- Use section headers with conceptual or technical labels, depending on mode.
- Keep argument or explanation progression explicit and skimmable.
- Use bullets for criteria, principles, and outcomes when they improve inspection; do not force list-heavy formatting in factual technical prose.
- Use tables when they clarify stages, role decomposition, or mechanism differences, but do not add a second summary table that repeats the same comparison.
- Keep close alignment between heading and section content.
- Keep equations compact and followed by plain-language interpretation.
- Avoid sales, manifesto, or founder tone unless the user explicitly requests it.
- End with a concise conclusion that restates method and implication; in factual technical mode, prefer bounded implication over directional slogan.

## Bilingual Delivery

- Keep one shared argument skeleton across languages.
- Adapt expression for each platform; do not produce literal translation.
- Preserve key terminology and logical sequence.
- If user asks for both outputs, deliver in this order:
1. WeChat Chinese draft
2. Medium English draft
3. Optional "alignment notes" (3-6 bullets) describing preserved logic

## Cross-Language Conversion Workflow (Default Preference)

Use this when the user writes in one language first, then requests the other language.

1. Lock source language and source draft as the canonical logic.
2. Extract thesis map and section intent from source.
3. Rewrite into target language with native rhythm and platform fit.
4. Run fidelity checks:
- no missing claims
- no new unsupported claims
- consistent terms and notation
5. Return target draft plus 3-6 alignment notes.
