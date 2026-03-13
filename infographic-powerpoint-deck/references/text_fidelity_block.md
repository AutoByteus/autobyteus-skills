# Text fidelity block (prevent typos / extra words)

Paste this block into every slide prompt when exact on-slide text matters in any language.

```text
Text fidelity hard constraints (required):
- Every piece of required on-slide text must appear exactly as provided.
- Preserve the original language, script, case, accents, punctuation, spacing, and intentional line breaks.
- For Chinese decks, preserve the requested script exactly as well: Simplified stays Simplified; Traditional stays Traditional.
- Do not rewrite, translate, paraphrase, autocomplete, or substitute synonyms unless the user explicitly asks.
- Do not add any text that is not listed as required on-slide text.
  - This includes extra words or glyphs in English, Chinese, German, pinyin, fake subtitles, logos, watermarks, random characters, street signs, book text, or poster text.
- If the background includes books, scrolls, maps, or documents, they must use no-text texture only. Do not generate readable letters or words.
- If the slide text is Chinese, keep the non-text illustration zone free of readable interface labels, dashboard labels, chart labels, book text, document text, and extra Chinese words.
- Text must be sharp, legible, and artifact-free. No blur, ghosting, garbling, or broken glyphs.
- If the output contains wrong or extra text, regenerate the slide and simplify the background, increase panel opacity, enlarge text, or split the content across slides.
```
