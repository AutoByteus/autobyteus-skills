# 阶段 2 需求细化指南

使用本指南将 `requirements.md` 从 `Draft` 转化为 `Design-ready` 或 `Refined`。

## 质量要求

- 需求描述可验证的行为，而不仅仅是叙述性意图
- 每个需求有一个稳定的 `requirement_id`
- 每个验收标准有一个稳定的 `acceptance_criteria_id`
- 预期结果足够可衡量以驱动阶段 7 验证

## 最低章节

- 状态
- 目标 / 问题陈述
- 范围内用例
- 验收标准
- 约束 / 依赖
- 假设
- 开放问题 / 风险

## 必需映射

- 需求到用例覆盖
- 验收标准到场景意图
- 确认的范围分类（`Small` / `Medium` / `Large`）

## 阶段 2 规则

- 从最新的 `investigation-notes.md` 细化，而非仅凭记忆
- 在需求达到 design-ready 之前不要进入阶段 3
- 如果后续阶段揭示行为差距，原地更新同一 `requirements.md` 并标记为 `Refined`
