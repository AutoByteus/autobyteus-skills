# Deck-level consistency blocks (reduce randomness across slides)

Legacy component library. Preferred flow is style-pack composition (`references/style-packs/`).
Use this file when manually selecting consistency rules.

Paste **one** block into every slide prompt. This acts like a “style lock” so the deck feels coherent across slides.

## Block 1 — Cinematic Keynote Lock

Paste this verbatim:

```text
本套PPT为同一系列（系列一致性强制规则）：
- 版式锁定：左侧文字毛玻璃面板占画面宽度 58%（允许±2%），右侧插画区占 42%（允许±2%）。文字面板必须保持同一圆角半径与同一透明度风格，位置与边距一致（标题区、正文区、页脚区的间距一致）。
- 字体锁定：标题、分标题、引用、要点、页脚的字号层级固定；行距舒适；任何一页不得出现超小字。
- 光源锁定：主光方向固定为右上 → 左下（体积光/光束同一角度），仅在右侧插画区出现；左侧文字面板区域不得出现强光束。
- 轮廓光锁定：右侧主物（十字架/面具/天平/盾牌等）使用同一强度的金色轮廓光（rim light），不要忽强忽弱。
- 地平线/剪影锁定：远景“城市/海港/城墙/柱廊”剪影带保持同一高度区间（画面下部 35%–45% 区域），始终低对比虚化。
- 纹理锁定：全套使用同一“超低对比羊皮纸颗粒”覆盖（约 5–10% 强度），不可忽有忽无。
- 图标锁定：线性图标统一线宽、统一风格（thin-line），勾选/分隔线统一金色发光强度。
- 禁止：不得添加任何额外文字（尤其是英文、logo、水印、随机字符）。
- 可读性硬约束：所有文字必须清晰锐利，高对比；背景不得侵入文字面板造成干扰。
```

## Block 2 — Movie Poster Epic Lock (stronger impact)

Paste this verbatim:

```text
本套PPT为电影海报风格系列（系列一致性强制规则）：
- 版式锁定：左侧文字面板占 55%（允许±2%），右侧插画占 45%（允许±2%）；文字面板更干净，背景更叙事但仍低对比。
- 主光锁定：固定一束斜向强主光（右上 → 中央），所有页保持同一角度；允许轻微暗角增强聚焦。
- 远景剪影锁定：每页远景必须有同一类型“地标剪影带”（海港/城墙/柱廊/荒野地平线），位置一致、虚化一致。
- 金色强调锁定：每页只允许 1–2 处“金色高光点”（戒指/蜡封/锁链断裂/光环），其他金色均为低对比细线。
- 颗粒与雾锁定：空气透视更明显（远景更冷更软），前景略暖；保持一致。
- 文字硬约束：任何一页不得因“海报感”牺牲文字可读性；所有指定中文逐字准确。
- 禁止：不得添加额外文字/英文/logo/水印/随机字符。
```

## Block 3 — Editorial Light Lock (bright + relaxed)

Paste this verbatim:

```text
本套PPT为明亮编辑风系列（系列一致性强制规则）：
- 版式锁定：左侧浅色文字卡片占 56%（允许±2%），右侧插画区占 44%（允许±2%）；卡片阴影轻微且一致。
- 背景亮度锁定：整体中高亮度，禁止大面积深色背景压暗页面；禁止暗角（vignette）。
- 光源锁定：以自然漫射光为主（可从左上或右上统一入光）；不使用强戏剧化体积光。
- 色彩锁定：主背景使用浅色系（米白/浅灰/浅蓝），正文使用深灰蓝高对比；强调色统一且克制。
- 纹理锁定：仅允许极弱纸纹/布纹（低噪点），不可出现明显颗粒或脏污质感。
- 图标锁定：线性图标统一线宽与圆角，色彩跟随强调色，避免高饱和混乱配色。
- 文字硬约束：任何一页不得牺牲可读性；所有指定中文逐字准确。
- 禁止：不得添加额外文字/英文/logo/水印/随机字符。
```

## How to use

- Add the chosen block under a “系列一致性锁定” section in every slide prompt.
- Match the block with style pack from `references/style-pack-catalog.md`:
  - `cinematic-dark` → Block 1 or 2
  - `editorial-light` / `airy-relaxed` / `clean-corporate` → Block 3
- Combine with `references/motif_pack.md` (motifs) + `references/prompt_template.md` (structure).
