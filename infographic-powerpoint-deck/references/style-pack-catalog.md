# Style-pack catalog

Use this table to map user wording to one style pack ID.

| Pack ID | Positioning | Trigger wording (examples) | Default scene tags |
|---|---|---|---|
| `cinematic-dark` | Dramatic, epic, tense | 电影感, 史诗, 张力, 警告感 | `dramatic,night,high-contrast-symbol` |
| `editorial-light` | Bright, readable, balanced | 明亮, 清晰, 日常分享, 不要太暗 | `daylight,clean,teaching` |
| `airy-relaxed` | Soft, calm, low-pressure | 放松, 清新, 温和, 治愈感 | `airy,calm,pastel,open-space` |
| `clean-corporate` | Professional, report-like | 商务, 培训, 汇报, 专业 | `corporate,minimal,diagram-friendly` |
| `warm-sermon` | Warm, pastoral, devotional | 温暖, 牧养, 见证, 讲章, 祷告会 | `warm,heritage,pastoral,daylight` |
| `neo-tech` | Futuristic, AI/startup, dynamic | AI, 科技, 未来感, 创业, 增长 | `tech,futuristic,network,data` |
| `youth-social` | Vibrant, energetic, youth-oriented | 年轻, 活力, 社群, 传播, 新媒体 | `vibrant,social,gradient,optimistic` |
| `research-academic` | Neutral, objective, analytical | 研究, 学术, 框架, 方法论, 证据 | `academic,neutral,structured,diagram` |

## Default choice

If user intent is unclear, pick `editorial-light`.

## Routing note

- If user says “不要太暗 / 更轻松”, prefer `editorial-light` or `airy-relaxed`.
- If user asks for maximum cinematic impact, use `cinematic-dark`.
- If user needs meeting-room readability and structured delivery, use `clean-corporate`.
- If user wants warm pastoral sharing, use `warm-sermon`.
- If topic is AI/product/startup growth, use `neo-tech`.
- If audience is students/youth/community groups, use `youth-social`.
- If topic is research-heavy and evidence-driven, use `research-academic`.
