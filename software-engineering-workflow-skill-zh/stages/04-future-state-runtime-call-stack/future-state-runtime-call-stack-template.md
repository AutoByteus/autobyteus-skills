# 未来态运行时调用栈（调试追踪风格）

使用此文档作为从设计基础派生的未来态（`to-be`）执行模型。
优先使用精确的 `file:function` 帧、显式分支和清晰的状态/持久化边界。
不要将此文档视为当前代码行为的现状追踪。

## 约定

- 帧格式：`path/to/file.ts:functionName(args?)`
- 边界标签：
  - `[ENTRY]` 外部入口点（API/CLI/事件）
  - `[ASYNC]` 异步边界（`await`、队列交接、回调）
  - `[STATE]` 内存状态变更
  - `[IO]` 文件/网络/数据库/缓存 IO
  - `[FALLBACK]` 非主路径分支
  - `[ERROR]` 错误路径
- 注释：使用 `# ...` 的简短行内注释。
- 不包含遗留/向后兼容分支。
- 保持调用路径中的解耦可见性：避免双向跨子系统循环和不清晰的依赖方向。

## 设计基础

- 范围分类：`Small` / `Medium` / `Large`
- 调用栈版本：`v1` / `v2` / ...
- 需求：`tickets/in-progress/<ticket-name>/requirements.md`（状态 `Design-ready`/`Refined`）
- 来源产物：
  - `Small`：`tickets/in-progress/<ticket-name>/implementation.md`（解决方案概要作为轻量级设计基础）
  - `Medium/Large`：`tickets/in-progress/<ticket-name>/proposed-design.md`
- 来源设计版本：`v1` / `v2` / ...
- 引用章节：
  - 主干清单章节：
  - 所有权章节：

## 未来态建模规则（强制）

- 即使当前代码有偏差也建模目标设计行为。
- 如果从现状到未来态的迁移需要过渡逻辑，在 `过渡说明` 中描述该逻辑；不要用当前流程替换未来态调用栈。
- 每个用例必须声明它从已批准的设计基础中行使哪些主干。
- 本文档中的 `主要端到端` 指该用例的主要顶层业务主干。一个工单可以有多个主要用例和多条主要主干。
- 如果用例主要验证一条有界局部主干（例如事件循环、worker 周期、状态机转换流程或调度器流程），明确说明而非将其隐藏在通用的端到端栈中。
- 有界局部主干始终附属于一个父所有者。它添加局部内部细节，不取代该区域更长的主要业务主干。
- `主干跨度充分性规则`（强制）：用例的主要运行时调用栈必须延伸足够远以暴露真实的业务路径，而非仅局部编辑段落。实际默认为 `4-5` 个有意义的帧，除非完整路径确实更小。
- 好的形状：
  - `浏览器 UI -> 会话引导 -> 运行时调用 -> 曝光组合器 -> 浏览器表面`
- 差的形状：
  - `曝光组合器 -> 浏览器表面`

## 用例索引（稳定 ID）

| 用例 ID | 主干 ID | 主干范围（`主要端到端`/`返回-事件`/`有界局部`） | 治理所有者 | 来源类型（`Requirement`/`Design-Risk`） | 需求 ID | 设计风险目标（若来源=`Design-Risk`） | 用例名称 | 覆盖目标（主路径/回退/错误） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UC-001 | DS-001 | 主要端到端 |  | Requirement | R-001 | N/A |  | Yes/Yes/Yes |
| UC-002 | DS-002 | 有界局部 |  | Design-Risk | R-002 | 队列重试/幂等性风险 |  | Yes/N/A/Yes |

规则：
- 每个范围内需求必须映射到此索引中的至少一个用例。
- `Design-Risk` 用例仅在技术目标/风险显式且可测试时允许。
- 每个用例必须映射到已批准主干清单中的至少一条主干。
- 当多条顶层业务路径在范围内时，多行 `主干范围 = 主要端到端` 是有效的。

## 过渡说明

- 达到目标状态所需的任何临时迁移行为：
- 临时逻辑的退役计划（如有）：

## 用例：UC-001 [名称]

### 主干上下文

- 主干 ID：
- 主干范围：
- 治理所有者：
- 为何此用例对此主干重要：
- 为何此主干跨度足够长：
- 如果 `主干范围 = 有界局部`，父所有者：

### 目标

### 前置条件

### 预期结果

### 主路径运行时调用栈

```text
[ENTRY] app/entrypoint.ts:handleRequest(...)
├── orders/validate-order-input.ts:validateInput(...)
├── orders/order-orchestrator.ts:orchestrate(...)
│   ├── persistence/load-order-state.ts:loadState(...) [IO]
│   ├── orders/transform-order.ts:transform(...) [STATE]
│   └── persistence/persist-order.ts:persist(...) [IO]
└── app/entrypoint.ts:returnResponse(...)
```

### 分支 / 回退路径

```text
[FALLBACK] 如果缓存缺失或无效
orders/order-orchestrator.ts:orchestrate(...)
├── orders/rebuild-order-from-source.ts:rebuildFromSource(...)
└── persistence/persist-order.ts:persist(...) [IO]
```

```text
[ERROR] 如果下游依赖失败
persistence/persist-order.ts:persist(...)
└── app/error-handler.ts:mapErrorToResponse(...)
```

### 状态和数据变换

- 输入载荷 -> 已验证命令：
- 检索的记录 -> 领域模型：
- 领域模型 -> 持久化载荷：

### 可观测性和调试点

- 日志发出位置：
- 度量/计数器更新位置：
- 追踪跨度（如有）：

### 设计异味 / 差距

- 是否存在遗留/向后兼容分支？（`Yes/No`）
- 是否引入了紧耦合或循环跨子系统依赖？（`Yes/No`）
- 是否检测到命名-职责漂移？（`Yes/No`）

### 开放问题

-

### 覆盖状态

- 主路径：`Covered` / `Missing`
- 回退路径：`Covered` / `Missing` / `N/A`
- 错误路径：`Covered` / `Missing` / `N/A`

## 用例：UC-002 [名称]

### 主干上下文

- 主干 ID：
- 主干范围：
- 治理所有者：
- 为何此用例对此主干重要：
- 为何此主干跨度足够长：
- 如果 `主干范围 = 有界局部`，父所有者：

### 目标

### 前置条件

### 预期结果

### 主路径运行时调用栈

```text
[ENTRY] app/entrypoint.ts:handleRequest(...)
├── feature/validate-input.ts:...
└── feature/orchestrate-request.ts:...
```

### 分支 / 回退路径

```text
[FALLBACK] 条件：
feature/fallback-path.ts:...
```

```text
[ERROR] 条件：
feature/map-error.ts:...
```

### 状态和数据变换

-

### 可观测性和调试点

-

### 设计异味 / 差距

-

### 开放问题

-

### 覆盖状态

- 主路径：`Covered` / `Missing`
- 回退路径：`Covered` / `Missing` / `N/A`
- 错误路径：`Covered` / `Missing` / `N/A`
