# 调查笔记示例

## 调查状态

- 当前状态：`Current`
- 范围分类：`Medium`
- 分类理由：涉及 API 行为、worker 分配逻辑和房间状态协调
- 调查目标：理解为何 `Start Recording All Occupied Rooms` 有时会复用错误的 worker 分配路径
- 需解决的主要问题：
  - 请求从何处进入运行时主干？
  - 哪个所有者实际决定 worker 分配？
  - 不正确的行为是由过时的辅助逻辑还是需求歧义引起的？

## 来源日志

| 日期 | 来源类型（`Code`/`Doc`/`Spec`/`Web`/`Repo`/`Issue`/`Command`/`Trace`/`Log`/`Data`/`Setup`/`Other`） | 确切来源 / 查询 / 命令 | 为何咨询 | 相关发现 | 需要跟进 |
| --- | --- | --- | --- | --- | --- |
| 2026-03-25 | Command | `rg -n "Start Recording All Occupied Rooms\|worker allocation" src` | 查找入口点和所有权 | 找到 UI 入口点、服务路径和一个过时的回退辅助函数 | 否 |
| 2026-03-25 | Code | `src/zoom/recording/start-recording-all-occupied-rooms.ts` | 检查请求入口点 | 入口点委托给 `RoomRecordingCoordinator` | 否 |
| 2026-03-25 | Code | `src/zoom/recording/room-recording-coordinator.ts` | 检查房间分配的所有者 | 协调器仍咨询遗留的 `allocateWorkerLegacy` 分支 | 是 |
| 2026-03-25 | Code | `src/zoom/workers/allocate-worker-legacy.ts` | 验证回退是否仍在使用 | 遗留分支复制了新分配器 80% 的逻辑 | 是 |
| 2026-03-25 | Web | `https://developers.zoom.example/recording-api` | 确认合作伙伴系统房间录制限制 | 主机每个已占用房间集只能调度一个录制 worker | 否 |
| 2026-03-25 | Repo | `https://github.com/zoom-example/recording-sdk-sample` @ `9b17c4d` | 验证上游示例如何处理多房间 worker 分配 | 示例应用通过一个规范分配器回调路由多房间录制 | 否 |
| 2026-03-25 | Trace | 本地已占用多房间会话复现 | 验证实际失败路径 | 仅在两个房间同时被占用时发生错误的 worker 选择 | 否 |

## 当前行为 / 代码库发现

### 入口点和边界

- 主要入口点：
  - `src/zoom/recording/start-recording-all-occupied-rooms.ts`
- 执行边界：
  - UI 操作 -> 录制协调器 -> worker 分配器 -> Zoom 适配器
- 所属子系统 / 能力域：
  - `zoom/recording`
  - `zoom/workers`
- 涉及的可选模块：
  - 不需要
- 文件夹 / 文件放置观察：
  - `allocate-worker-legacy.ts` 位于正确的子系统下，但应该被移除而非保留

### 相关文件 / 符号

| 路径 | 符号 / 区域 | 当前职责 | 发现 / 观察 | 所有权 / 放置影响 |
| --- | --- | --- | --- | --- |
| `src/zoom/recording/start-recording-all-occupied-rooms.ts` | `startRecordingAllOccupiedRooms` | 请求入口点 | 薄入口点，放置看起来正确 | 保留在录制入口点下 |
| `src/zoom/recording/room-recording-coordinator.ts` | `RoomRecordingCoordinator` | 编排房间录制流程 | 当前所有者仍分支到遗留 worker 分配 | 可能保留所有者，移除回退分支 |
| `src/zoom/workers/allocate-worker.ts` | `allocateWorker` | 主要 worker 分配 | 新路径已覆盖大多数正常情况 | 共享核心应保留在此 |
| `src/zoom/workers/allocate-worker-legacy.ts` | `allocateWorkerLegacy` | 旧的回退分配器 | 近似重复的逻辑加上额外的过时假设 | 候选移除，而非扩展 |

### 运行时 / 探针发现

| 日期 | 方法（`Repro`/`Trace`/`Probe`/`Script`/`Test`/`Setup`） | 确切命令 / 方法 | 观察 | 影响 |
| --- | --- | --- | --- | --- |
| 2026-03-25 | Trace | 本地已占用房间复现 | 当第二个房间进入分配路径时出现失败 | worker 分配决策可能是缺陷中心 |
| 2026-03-25 | Probe | 协调器分配器调用周围的临时日志 | 多房间情况下仍选择遗留路径 | 设计和实现应移除双路径行为 |

### 外部代码 / 依赖发现

- 检查的上游仓库 / 包 / 示例：
  - `https://github.com/zoom-example/recording-sdk-sample`
- 版本 / 标签 / 提交 / 发布：
  - 提交 `9b17c4d`
- 检查的文件、端点或示例：
  - 示例录制协调器和多房间回调接线
- 学到的相关行为、合约或约束：
  - 上游示例从未通过第二个回退分配器路由此流程
- 置信度和新鲜度：
  - 中高 / 2026-03-25

### 复现 / 环境设置

- 所需服务、模拟或仿真器：
  - 带有已占用房间固件的本地 Zoom 适配器存根
- 所需配置、特性标志或环境变量：
  - 录制特性标志已启用
- 所需固件、种子数据或账户：
  - 一个主机会话中的两个已占用房间固件
- 为调查克隆/下载的外部仓库、示例或产物：
  - 录制 SDK 示例仓库已本地克隆用于行为比较
- 对调查产生实质影响的设置命令：
  - 双房间已占用状态的本地固件引导
- 临时调查专用设置的清理说明：
  - 在根因置信度建立后移除临时日志

## 外部 / 互联网发现

| 来源 | 事实 / 约束 | 为何重要 | 置信度 / 新鲜度 |
| --- | --- | --- | --- |
| `https://developers.zoom.example/recording-api` | 每个已占用房间集一个录制 worker | 分配器必须避免对相同已占用集的重复 worker 分配 | 高 / 2026-03-25 |

## 约束

- 合作伙伴 API 约束 worker 分配形状
- 当前代码仍携带双路径分配器分裂
- 上游示例确认双路径分裂是本地遗留行为，而非合作伙伴必需行为

## 未知项 / 开放问题

- 未知项：是否有任何隐藏的消费者仍直接调用 `allocateWorkerLegacy`
- 为何重要：安全移除取决于此
- 计划的跟进：运行仓库范围搜索和运行时追踪以查找直接遗留调用

## 影响

### 需求影响

- 需求应明确说明多房间已占用录制必须使用一个一致的分配策略

### 设计影响

- 设计应移除遗留分配器路径而非扩展它
- 协调器应依赖一个规范的分配所有者

### 实现 / 放置影响

- 实现应在范围内删除过时的遗留 worker 分配代码
- 阶段 8 应验证没有重复的分配器逻辑残留

## 重入补充

### 2026-03-26 重入更新

- 触发原因：阶段 7 可执行验证发现分配器在重试条件下仍存在分歧
- 新证据：重试路径通过一个过时的适配器包装器进入 `allocateWorkerLegacy`
- 更新的影响：设计和实现必须移除该包装器并保持一个规范的分配器路径
