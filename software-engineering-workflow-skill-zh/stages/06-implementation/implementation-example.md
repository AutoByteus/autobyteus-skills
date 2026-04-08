# 实现示例

以下示例展示已填写的实现产物中的关键章节。并非所有章节都包含在内——仅示例说明最常用部分的用法。

## 范围分类

- 分类：`Medium`
- 理由：多个主干节点、新的所有者边界、API 行为变更和遗留移除在范围内
- 工作流深度：设计提案文档 -> 未来态运行时调用栈 -> 未来态运行时调用栈审查（迭代深度轮次直到 `Go Confirmed`）-> `implementation.md` 基线 -> 实现执行

## 文档状态

- 当前状态：`In Execution`
- 说明：审查门控通过，实现进行中

## 计划基线（冻结直到重新规划）

### 前置条件（必须全部为真）

- `requirements.md` 至少为 `Design-ready`：Yes
- 验收标准使用稳定 ID 和可衡量结果：Yes
- `workflow-state.md` 是最新的且阶段 5 证据已记录：Yes
- 调用栈审查产物存在且最新：Yes
- 所有范围内用例已审查：Yes
- 无未解决的阻塞性发现：Yes
- `Go Confirmed`，连续两轮干净：Yes
- 最后两轮已完成发现扫描：Yes
- 最后两轮无新用例：Yes

### 解决方案概要

- 范围内用例：UC-001（多房间录制）、UC-002（Worker 分配重试）
- 范围内主干清单：DS-001（主要端到端）、DS-002（有界局部）
- 主要主干跨度充分性理由：DS-001 覆盖 `UI 操作 -> 录制协调器 -> Worker 分配器 -> Zoom 适配器 -> 确认响应`，5 个有意义节点
- 主要所有者 / 主要领域主题：`RoomRecordingCoordinator`、`WorkerAllocator`
- 需求覆盖保证：R-001 -> UC-001, R-002 -> UC-002
- 目标架构形状：移除遗留分配器，统一到一个规范 `WorkerAllocator`
- 新的所有者/边界接口：无新所有者；`WorkerAllocator` API 扩展
- API/行为增量：移除 `allocateWorkerLegacy`，扩展 `allocateWorker`
- 关键假设：所有调用者均通过协调器间接使用分配器
- 已知风险：直接遗留调用者可能存在

### 实现工作表

| 变更 ID | 主干 ID | 所有者 | 关注点 | 当前路径 | 目标路径 | 操作 | 依赖于 | 实现状态 | 单元测试文件 | 单元测试状态 | 集成测试文件 | 集成测试状态 | 阶段 8 审查状态 | 说明 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-001 | DS-001 | WorkerAllocator | 统一分配逻辑 | `src/zoom/workers/allocate-worker.ts` | 相同 | 修改 | 无 | Completed | `tests/unit/allocate-worker.test.ts` | Passed | `tests/integration/recording-flow.test.ts` | Passed | Planned | 扩展以处理多房间 |
| C-002 | DS-001 | RoomRecordingCoordinator | 移除遗留分支 | `src/zoom/recording/room-recording-coordinator.ts` | 相同 | 修改 | C-001 | Completed | `tests/unit/room-recording-coordinator.test.ts` | Passed | 同上 | Passed | Planned | 移除到遗留分配器的分支 |
| C-003 | DS-001 | N/A | 遗留移除 | `src/zoom/workers/allocate-worker-legacy.ts` | N/A | 移除 | C-001, C-002 | Completed | N/A | N/A | N/A | N/A | Planned | 已验证无剩余引用 |

### 向后兼容和解耦护栏

- 引入的向后兼容机制：`None`
- 为旧行为保留的遗留代码：`No`
- 范围内保留的死代码/过时代码：`No`
- 共享数据结构保持紧凑：`Yes`
- 实现期间重新应用了共享设计/常见实践规则：`Yes`
- 主干跨度充分性得到保持：`Yes`
- 权威边界规则得到保持：`Yes`
- 解耦影响评估已完成：`Yes`
- 引入了新的紧耦合或循环依赖：`No`
- 变更的源实现文件保持在主动大小压力护栏内：`Yes`

## 执行追踪

### 进度日志

- 2026-03-26：实现启动基线已创建。
- 2026-03-26：C-001 完成 - WorkerAllocator 扩展，单元测试通过。
- 2026-03-26：C-002 完成 - 协调器遗留分支移除，集成测试通过。
- 2026-03-26：C-003 完成 - 遗留分配器文件已移除，引用扫描干净。

### 移除/重命名/遗留清理验证日志

| 日期 | 变更 ID | 项 | 执行的验证 | 结果 | 说明 |
| --- | --- | --- | --- | --- | --- |
| 2026-03-26 | C-003 | `src/zoom/workers/allocate-worker-legacy.ts` | `rg -n "allocateWorkerLegacy" src` + 针对性集成测试 | Passed | 无剩余引用 |
