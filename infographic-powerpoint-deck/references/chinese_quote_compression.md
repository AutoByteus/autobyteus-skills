# Chinese quote compression & splitting (long verses → readable slides)

Goal: keep Chinese text **accurate** while preventing tiny fonts and wall-of-text slides.

## When to split

Split into 2+ slides if any is true:
- Quote block > 3 lines at comfortable font size
- Bullets > 5
- Mixed: long quote + long list on one slide

## Safe splitting patterns (no paraphrase)

1) **Verse chunking** (recommended)
- Slide A: verse chunk 1 + 2 bullets (why it matters)
- Slide B: verse chunk 2 + 2 bullets (application)

2) **Quote vs explanation**
- Slide A: quote only (plus 1 key line)
- Slide B: explanation framework (no quote, or 1 short anchor line)

3) **List overflow**
- Slide A: first half of list + same scene
- Slide B: second half of list + same scene (slight camera change)

## Pasteable rules block

```text
长经文排版规则（必须遵守）：
- 不得改写经文：只能拆分显示，不能同义替换。
- 若经文过长：必须拆成多页，每页引用不超过 3 行（以舒适大字号为准）。
- 拆分时保持原句顺序；可用省略号“……”仅在原文已出现或用户允许时使用。
- 若需要解释：优先把解释放到下一页，不要让一页同时塞满长引用+长要点。
```

