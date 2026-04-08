---
name: software-engineering-workflow-skill-zh
description: "运行分阶段的软件工程交付反馈循环，从引导到调查、需求、设计、运行时审查、实现、API/E2E 和可执行验证、代码审查、文档同步，以及带有持久产物和显式重入的最终移交。"
---

# 软件工程工作流技能

## 概述

运行分阶段的软件工程交付工作流：引导工单上下文、调查和细化需求、构建设计和未来态运行时产物、驱动实现（使用一个同时承载稳定基线和实时进度追踪的实现产物）、通过适合系统的 API/E2E 和其他可执行验证证据验证行为、应用独立代码审查、同步长期文档，并以显式用户验证的移交和仓库最终确定结束。对于中/大范围，包含按数据流主干清单、所有权、非主干关注点和派生的关注点分离组织的完整设计提案文档。
此工作流是阶段门控的。默认不批量生成所有产物。
在此技能中，未来态运行时调用栈是未来态（`to-be`）执行模型，不是当前（`as-is`）实现行为的追踪。

## 技能布局

- `SKILL.md` 是工作流路由器。它定义阶段规则并将每个阶段指向其拥有的模板/参考资料。
- `shared/` 存储多个阶段复用的跨阶段参考：
  - `shared/design-principles.md`
  - `shared/common-design-practices.md`
  - `shared/workflow-state-template.md`
- `stages/` 存储阶段拥有的模板和参考资料：
  - `stages/00-bootstrap/`
  - `stages/01-investigation/`
  - `stages/02-requirements/`
  - `stages/03-design/`
  - `stages/04-future-state-runtime-call-stack/`
  - `stages/05-future-state-runtime-call-stack-review/`
  - `stages/06-implementation/`
  - `stages/07-api-e2e/`
  - `stages/08-code-review/`
  - `stages/09-docs-sync/`
  - `stages/10-handoff/`
- 将阶段特定材料保持在匹配的阶段文件夹中。仅对真正的跨阶段参考使用 `shared/`。
- 当一个阶段有本地指南或检查清单时，优先使用该阶段拥有的文件，然后再回退到通用工作流描述。

## 术语

- `子系统` / `能力域`：拥有更广泛工作类别的较大功能区域，可包含多个文件加可选的模块分组。
- `模块`：当代码库受益时在子系统内部的可选中间分组。在此技能中，`模块` 不是一个文件或默认所有权术语的同义词。
- `文件夹` / `目录`：用于组织文件和任何可选模块分组的物理分组。
- `文件`：一个具体的源文件，是一个具体关注点应落地的主要单元。

## 工作流

### 工单文件夹约定（项目本地）

- 对每个任务，在 `tickets/in-progress/` 下创建/使用一个工单文件夹。
- 文件夹命名：使用清晰、简短的 kebab-case 名称（不需要日期前缀）。
- 在工作活跃期间将所有任务规划产物写入 `in-progress` 工单文件夹。
- 标准状态：
  - 活跃工作路径：`tickets/in-progress/<ticket-name>/`
  - 完成归档路径：`tickets/done/<ticket-name>/`
- 移动规则（强制）：仅在用户明确确认完成（例如："done"、"finished" 或 "verified"）或明确要求移动时，将工单从 `in-progress` 移到 `done`。
- 最终归档排序规则（强制）：当明确的用户完成/验证也触发仓库最终确定时，在最终提交前将工单文件夹移到 `tickets/done/<ticket-name>/`，以便提交状态包含已归档的工单路径。
- 重新打开规则（强制）：如果用户要求继续/重新打开已完成的工单，在进行新更新前将其从 `tickets/done/<ticket-name>/` 移回 `tickets/in-progress/<ticket-name>/`。
- 永远不要仅基于内部评估自动将工单移至 `done`。
- 如果用户指定了不同的位置，遵循用户指定的路径。

### 工单 + 工作树引导（强制首要操作）

- 在调查前，按以下顺序引导工作上下文：
  - 创建/使用 `tickets/in-progress/<ticket-name>/`，
  - 如果项目是 git 仓库：
    - 从明确的用户指令解析引导基础分支（当提供时）；否则以最高置信度推断跟踪的远程默认/集成分支，
    - 创建新工单工作树/分支时，先刷新跟踪的远程引用以从最新远程状态开始而非过时的本地头，
    - 在写入产物前为工单分支创建/复用专用工单工作树，
    - 创建新工单分支时，从最新的跟踪远程基础分支创建 `codex/<ticket-name>`，
  - 从用户提供的需求意图创建/更新 `requirements.md` 状态为 `Draft`。
- 在工单引导和 `requirements.md` `Draft` 物理写入前不得开始调查。
- 如果工单已存在专用工作树，复用它而非创建新的。
- 如果用户指定了基础分支，始终使用该分支的最新跟踪远程状态而非从本地副本猜测。
- 如果远程刷新或基础分支解析失败，保持阶段 0 `Blocked` 并在调查前记录阻塞项。
- 如果环境不是 git 仓库，在没有工作树设置的情况下继续，仍强制工单文件夹 + `Draft` 需求捕获。

### 工作流状态文件（强制执行产物）

- 创建并维护 `tickets/in-progress/<ticket-name>/workflow-state.md` 作为规范的阶段控制产物。
- 在阶段 0 工单引导后立即初始化，包含：
  - `Current Stage = 0`，
  - `Code Edit Permission = Locked`，
  - `Stage 0 Bootstrap Record` 填写引导模式以及（当 git 仓库时）请求的基础分支（如有）、解析的基础远程/基础分支、执行的远程刷新结果、工作树路径和工单分支，
  - 阶段门控行为 `Not Started`/`In Progress` 状态。
- 更新模型（强制）：
  - 每次阶段转换时就地重写 `Current Snapshot`，
  - 每次转换/重入追加一行到 `Transition Log`，
  - 保持 `Stage Gates` 行与证据链接/路径同步。
- 源代码编辑锁（硬规则）：
  - 除非 `workflow-state.md` 明确显示 `Code Edit Permission = Unlocked`，否则不允许源代码编辑，
  - 默认状态为 `Locked`；仅在阶段 6 前置条件满足时解锁源代码编辑。
- 重入锁规则：
  - 在任何阶段 7/8 失败时，在重入操作前设置 `Code Edit Permission = Locked`，
  - 在继续前在 `workflow-state.md` 中记录触发/分类/返回路径。
- 违规协议：
  - 如果在 `Code Edit Permission = Locked` 时编辑了源代码，在 `workflow-state.md` 中记录违规条目，
  - 暂停进一步源代码编辑，声明重入并返回所需的上游阶段路径。

### 语音通知（Speak 工具，必需）

- 使用 `Speak` 工具进行工作流状态转换更新，以便用户可以跟踪执行位置和下一步。
- 播放规则（强制）：对于必需的语音通知，明确以 `play=true` 调用 `Speak`。
- 默认不要为必需的转换通知设置 `play=false`。
- 例外：仅在用户明确要求静音模式时设置 `play=false`。
- 转换驱动的语音规则（强制）：
  - 仅在 `workflow-state.md` 因阶段转换、门控决策、重入决策或代码编辑锁/解锁变更而更新时发声，
  - 不要为低级命令执行、中间分析笔记或部分草稿发声。
- 必需的语音事件：
  - 工作流启动（`任务已接受`，`下一阶段`），
  - 每次阶段转换（`从阶段 -> 到阶段`）在 `workflow-state.md` 转换日志追加后，
  - 每次门控决策（`Pass`/`Fail`/`Blocked`）在门控证据写入后，
  - 每次重入声明（分类 + 返回路径）在 `workflow-state.md` 重入部分更新后，
  - 每次 `Code Edit Permission` 变更（`Locked`/`Unlocked`）在快照更新后。
- 语音排序规则：
  - 先更新 `workflow-state.md`，
  - 然后发出反映已持久化状态的语音通知。
- 语音消息内容（强制）：
  - 当前阶段，
  - 刚完成/变更的内容（转换或门控结果），
  - 下一阶段/操作，
  - 代码编辑锁状态（当变更时）。
- 如果多个转换紧密发生，在最终持久化更新后将它们批量为一条短消息。
- 保持每条语音消息简短（1-2 句），状态优先，面向操作。
- 如果 `Speak` 工具失败或不可用，继续工作流并以文本提供相同更新。
- 不要朗读密钥、令牌或完整的敏感载荷。

### 执行模型（严格阶段门控）

- 在明确的阶段中工作，在产生下游产物前完成每个门控。
- 在每次阶段转换前，先更新 `workflow-state.md`（快照 + 转换日志 + 门控状态），然后继续。
- 将 `workflow-state.md` 视为执行锁控制器，而非可选文档。
- 转换权威规则（强制）：阶段移动由阶段转换合约 + 转换矩阵控制。当触发条件满足时，立即转换到映射路径；不要偏好继续停留在当前阶段。
- 转换执行规则（强制）：每当 `workflow-state.md` 更新以声明阶段转换或分类重入时，默认立即进入并执行目标阶段，无需等待另一条用户消息。记录转换和描述下一步是不够的。转换在工作实际在目标阶段恢复前不算完成。仅在真正阻塞项或明确的仅用户门控时停止。
- 需求可以从用户输入/缺陷报告产物开始作为粗略的 `Draft`，在深度分析之前。
- 在工单/工作树引导完成且 `requirements.md` 状态 `Draft` 物理写入前不要开始调查。
- 在 `investigation-notes.md` 物理写入且对工单是最新的之前不要标记理解通过完成。
- 在深度理解通过完成且 `requirements.md` 达到 `Design-ready` 前不要草拟设计产物。
- 在未来态运行时调用栈审查门控对当前范围完全满足前不要最终确定 `implementation.md` 基线部分或开始执行追踪部分。
- 在 `implementation.md` 基线最终确定且其执行追踪部分初始化前不要开始实现执行。
- 在 `workflow-state.md` 中以下所有条件为真前不要开始源代码编辑：
  - `Current Stage = 6`，
  - `Code Edit Permission = Unlocked`，
  - 阶段 5 门控为 `Go Confirmed`，
  - 必需的上游产物标记为 `Pass` 并附证据。
- 在实现执行完成且必需的单元/集成验证和阶段 6 现代化/所有权依赖检查满足前不要开始阶段 7。
- 在阶段 7 可执行验证门控为 `Pass` 前不要开始代码审查。
- 在代码审查完成前不要开始测试后 `docs/` 同步。
- 在测试后 `docs/` 同步完成（或记录明确的无影响决策和理由）前不要关闭任务；在任何必需的阶段 10 用户验证/归档/最终确定工作完成前不要标记最终完成。
- 用户验证保持规则（强制）：阶段 9 通过后，持久化移交摘要并保持阶段 10 开放直到用户明确确认完成/验证。在该用户信号前不要提交、推送、合并、运行发布/出版/部署工作或将工单移至 `done`。
- 发布注释产物规则（适用时强制）：如果工单导致面向用户的应用发布或任何 GitHub Release 正文，阶段 10 还必须在最终发布前持久化 `tickets/in-progress/<ticket-name>/release-notes.md` 及简短的面向用户的功能注释。如果不适用，在移交摘要中记录明确的 `release-notes not required` 理由。
- 仓库最终确定规则（git 仓库强制）：在收到明确的用户完成/验证信号后且在阶段 10 标记完成前，先将工单文件夹移至 `tickets/done/<ticket-name>/`，然后在工单分支上提交所有范围内变更（包括移动的工单文件），推送工单分支到远程，从远程更新已解析的最终确定目标分支，将工单分支合并到该更新的目标分支，并推送更新的目标分支。
- 发布/出版/部署规则（有条件）：仓库最终确定后，如果项目有适用的已记录发布、出版、打标签或部署步骤，运行该项目特定方法。如果没有此类步骤适用，在移交摘要中记录 `release/publication/deployment not required`。
- 最终确定目标规则（强制）：使用阶段 0 的 `Resolved Base Remote` 和 `Resolved Base Branch` 作为默认的阶段 10 合并目标，除非用户后来明确覆盖该目标。
- 最终确定后清理规则（当存在专用工单工作树/分支时强制）：仓库最终确定和任何适用发布工作完成后，移除阶段 0 中记录的专用工单工作树，运行工作树修剪清理，并在本地工单分支完全合并到已解析的最终确定目标且不再需要时删除该本地工单分支。除非明确的用户指令或已记录的项目策略要求，否则不要删除远程分支。
- 阶段 10 阻塞规则（强制）：如果在用户确认后移动到 `tickets/done/`、提交、推送、目标分支更新、合并或必需的最终确定后清理失败，保持阶段 10 `In Progress`/`Blocked`，在 `workflow-state.md` 中记录阻塞项，不要标记最终移交完成。
- 在收到明确的用户完成确认前将工单文件夹保持在 `tickets/in-progress/` 下。
- `Small` 范围例外：在审查前草拟 `implementation.md`（仅解决方案概要部分）作为设计输入是允许的，但此草案不解锁实现启动。
- 未来态运行时调用栈审查必须作为迭代深度审查轮次运行（不是一次性审查）。
- `Go Confirmed` 不能在阻塞轮次的必需上游产物更新后立即声明。
- 稳定性规则（强制）：仅在连续两轮深度审查报告无阻塞项、无需持久化产物更新且无新发现用例后解锁 `Go Confirmed`。
- 第一轮干净为临时的（`Candidate Go`），第二轮连续干净为确认（`Go Confirmed`）。
- 缺失用例发现规则（强制）：每轮阶段 5 必须运行专门的缺失用例发现扫描。
- 如果发现新用例、需要持久化产物更新或发现阻塞项，阶段 5 轮次不干净。
- 任何需要设计/调用栈更新的审查发现都是阻塞性的。
- 阶段 5 分类重入映射（强制）：
  - `Design Impact`：返回 `阶段 3 -> 阶段 4 -> 阶段 5`。
  - `Requirement Gap`：返回 `阶段 2 -> 阶段 3 -> 阶段 4 -> 阶段 5`。
  - `Unclear`：返回 `阶段 1 -> 阶段 2 -> 阶段 3 -> 阶段 4 -> 阶段 5`。
- 阶段 6 非本地重入规则（强制）：如果阶段 6 问题被分类为 `Design Impact`、`Requirement Gap` 或 `Unclear`，在 `workflow-state.md` 中记录分类 + 返回路径，设置 `Code Edit Permission = Locked`，并在进一步源代码编辑前转换到映射的上游阶段路径。
- 重入声明规则（强制）：当实现后门控发现问题时，在任何代码编辑前明确记录触发阶段、分类和必需的返回阶段路径。
- 重入完成规则（强制）：在分类重入记录且目标返回路径持久化在 `workflow-state.md` 后，默认立即恢复第一个返回阶段，无需等待另一条用户消息。
- 无直接补丁规则（强制）：对于实现后门控发现，不要先编辑源代码。根据分类路径先更新必需的上游产物。
- 重入映射（强制）：
  - `Local Fix`：更新实现产物，然后实施修复，然后重跑 `阶段 6 -> 阶段 7`；阶段 7 通过后继续到 `阶段 8`。
  - `Design Impact`：返回 `阶段 1 -> 阶段 3 -> 阶段 4 -> 阶段 5 -> 阶段 6 -> 阶段 7`；阶段 7 通过后继续到 `阶段 8`。
  - `Requirement Gap`：返回 `阶段 2 -> 阶段 3 -> 阶段 4 -> 阶段 5 -> 阶段 6 -> 阶段 7`；阶段 7 通过后继续到 `阶段 8`。
  - `Unclear`（或跨领域根因）：返回 `阶段 0 -> 阶段 1 -> 阶段 2 -> 阶段 3 -> 阶段 4 -> 阶段 5 -> 阶段 6 -> 阶段 7`；阶段 7 通过后继续到 `阶段 8`。
- 重入路径中的阶段 0 意味着在同一工单/工作树中重新打开引导控制；不创建新的工单文件夹。

### 规范阶段序列（快速映射）

| 阶段 | 名称 | 核心交付物/门控 | 代码编辑权限 |
| --- | --- | --- | --- |
| 0 | 引导 + 草拟需求 | 工单/工作树引导完成 + `requirements.md` = `Draft` | Locked |
| 1 | 调查 + 分类 | `investigation-notes.md` 最新 + 范围分类完成 | Locked |
| 2 | 需求细化 | `requirements.md` 达到 `Design-ready`/`Refined` | Locked |
| 3 | 设计基础 | `implementation.md` 解决方案概要（`Small`）或 `proposed-design.md`（`Medium/Large`） | Locked |
| 4 | 未来态运行时调用栈 | `future-state-runtime-call-stack.md` 最新 | Locked |
| 5 | 未来态运行时调用栈审查 | `Go Confirmed`（连续两轮干净，无阻塞/持久化更新/新用例）+ 所有范围内用例主干跨度充分性通过 | Locked |
| 6 | 源代码实现 + 单元/集成 | 源代码 + 必需的单元/集成检查完成 + 无向后兼容/遗留保留 + 所有权依赖质量保持 + 已触及文件正确放置 | Unlocked |
| 7 | API/E2E + 可执行验证门控 | 可执行验证场景已实现且验收标准 + 主干覆盖闭环完成 | Unlocked |
| 8 | 代码审查门控 | 代码审查决策已记录（`Pass`/`Fail`）含所有强制检查 | Locked |
| 9 | 文档同步 | `docs-sync.md` 最新 + `docs/` 更新完成或记录无影响理由 | Locked |
| 10 | 最终移交 | 交付摘要就绪 + 明确用户验证 -> 移动工单到 `done` -> 仓库最终确定 + 清理 | Locked |

### 阶段转换合约（执行）

| 阶段 | 退出条件（转换前必须为真） | 失败/阻塞时 | 通过后下一阶段 |
| --- | --- | --- | --- |
| 0 引导 + 草拟需求 | 工单/工作树引导完成且 `requirements.md` 状态为 `Draft` | 留在 `0` 直到引导完成 | `1` |
| 1 调查 + 分类 | `investigation-notes.md` 最新且范围分类已记录 | 留在 `1` 直到调查证据完成 | `2` |
| 2 需求 | `requirements.md` 为 `Design-ready`（或 `Refined`） | 留在 `2` 直到需求设计就绪 | `3` |
| 3 设计基础 | 设计基础产物最新 | 留在 `3` 并修改设计基础 | `4` |
| 4 未来态运行时调用栈 | `future-state-runtime-call-stack.md` 对范围内用例最新 | 留在 `4` 并重新生成 | `5` |
| 5 未来态运行时调用栈审查 | 达到 `Go Confirmed`（连续两轮干净） | 分类重入（`Design Impact`：`3->4->5`，`Requirement Gap`：`2->3->4->5`，`Unclear`：`1->2->3->4->5`） | `6` |
| 6 源代码 + 单元/集成 | 源实现完成、测试通过、无向后兼容/遗留路径、所有权依赖有效、已触及文件正确放置 | 本地问题留在 `6`；非本地分类重入 | `7` |
| 7 API/E2E + 可执行验证门控 | 验证场景已实现且所有验收标准为 `Passed`（或明确 `Waived`） | 按分类重入 | `8` |
| 8 代码审查门控 | 代码审查决策为 `Pass` 且所有强制检查满足 | 按分类重入 | `9` |
| 9 文档同步 | `docs-sync.md` 最新且文档更新完成或记录无影响理由 | 分类重入或留在 `9 (Blocked)` | `10` |
| 10 最终移交 | 移交摘要完成、用户确认、工单已归档、仓库最终确定完成 | 留在 `阶段 10` 直到完成 | 结束 |

### 转换矩阵（通过/失败/阻塞）

| 触发 | 必需的转换路径 | 说明 |
| --- | --- | --- |
| 正常前进通过 | `0->1->2->3->4->5->6->7->8->9->10` | 仅在每个阶段门控为 `Pass` 时使用。 |
| 阶段 5 阻塞分类 `Design Impact` | `3->4->5` | 问题明确在主干/所有权/边界决策中。 |
| 阶段 5 阻塞分类 `Requirement Gap` | `2->3->4->5` | 发现缺失/模糊的需求。 |
| 阶段 5 阻塞分类 `Unclear` | `1->2->3->4->5` | 根因不确定或跨领域。 |
| 阶段 6 失败分类 `Local Fix` | 留在 `阶段 6` | 在阶段 6 内修复。 |
| 阶段 6 失败分类 `Design Impact` | `1->3->4->5->6` | 重新打开调查检查点然后重入设计链。 |
| 阶段 6 失败分类 `Requirement Gap` | `2->3->4->5->6` | 先更新需求然后重跑下游链。 |
| 阶段 6 失败（`Unclear`） | `0->1->2->3->4->5->6` | 在同一工单中重新打开阶段 0 控制。 |
| 阶段 7 失败分类 `Local Fix` | `6->7` | 先更新产物，然后代码修复，然后重跑场景。 |
| 阶段 7 失败分类 `Design Impact` | `1->3->4->5->6->7` | 重新打开调查然后重入设计链。 |
| 阶段 7 失败分类 `Requirement Gap` | `2->3->4->5->6->7` | 先更新需求然后重跑下游链。 |
| 阶段 7 失败（`Unclear`） | `0->1->2->3->4->5->6->7` | 重跑完整链。 |
| 阶段 8 失败分类 `Local Fix` | `6->7->8` | 修复并重跑测试门控后重新审查。 |
| 阶段 8 失败分类 `Validation Gap` | `7->8` | 先加强阶段 7 覆盖/证据。 |
| 阶段 8 失败分类 `Design Impact` | `1->3->4->5->6->7->8` | 重新打开调查然后返回设计链。 |
| 阶段 8 失败分类 `Requirement Gap` | `2->3->4->5->6->7->8` | 返回需求然后重跑完整下游链。 |
| 阶段 8 失败（`Unclear`） | `0->1->2->3->4->5->6->7->8` | 重跑完整链。 |
| 阶段 9 阻塞分类 `Local Fix` | `6->7->8->9` | 需要小的具体实现或产物修正。 |
| 阶段 9 阻塞分类 `Requirement Gap` | `2->3->4->5->6->7->8->9` | 缺失或模糊的预期行为。 |
| 阶段 9 阻塞分类 `Unclear` | `0->1->2->3->4->5->6->7->8->9` | 最终行为太不清楚或跨领域。 |
| 阶段 10 等待用户验证 | 留在 `阶段 10 (In Progress)` | 等待明确的用户完成/验证。 |
| 阶段 10 归档/最终确定阻塞 | 留在 `阶段 10 (Blocked)` | 记录阻塞项并解决。 |

### 0) 引导工单 + 捕获草拟需求

- 使用 `stages/00-bootstrap/bootstrap-checklist.md`。
- 运行强制首要操作序列：创建/使用工单文件夹，解析基础分支，创建/复用工作树，创建 `workflow-state.md`，捕获初始需求快照（`requirements.md` 状态 `Draft`）。
- 在阶段 0 引导和 `requirements.md` `Draft` 物理写入前不要运行深度调查。

### 1) 调查 + 理解通过 + 分类

- 使用 `stages/01-investigation/investigation-guide.md`。
- 创建/更新 `tickets/in-progress/<ticket-name>/investigation-notes.md`，在调查期间持续更新。将其视为持久证据日志而非简短摘要。
- 调查不是只读的：需要时积极复现问题、运行聚焦的命令/测试、编写小型诊断脚本。
- 最小代码库理解通过：识别入口点、执行边界、已触及文件、受影响的子系统/所有者、预期的规范文件位置、当前命名约定和可能使设计假设无效的未知项。
- 分类为 `Small`、`Medium` 或 `Large`。
- 在 `requirements.md` 达到 `Design-ready` 前不要草拟设计产物或运行时调用栈。

### 2) 将需求文档细化为设计就绪（强制）

- 使用 `stages/02-requirements/requirements-refinement-guide.md`。
- 创建/更新 `tickets/in-progress/<ticket-name>/requirements.md`。
- 需求成熟度流程：`Draft` -> `Design-ready` -> `Refined`。
- 每个需求包含稳定的 `requirement_id` 和明确的预期结果。
- 每个验收标准包含稳定的 `acceptance_criteria_id` 和可衡量的预期结果。

### 核心现代化策略（强制）

- 强制立场：无向后兼容且无遗留代码保留。
- 不要保留遗留行为、遗留 API、兼容包装器、双写路径或仅为旧流程保留的回退分支。

### 共享设计原则（设计 + 审查，强制）

- 设计和审查必须使用相同的原则和词汇。
- 使用 `shared/design-principles.md` 作为阶段 3 设计工作和阶段 5 审查的主要共享参考。
- 使用 `shared/common-design-practices.md` 作为辅助实践。
- 使用 `stages/08-code-review/code-review-principles.md` 作为阶段 8 审查参考。
- 核心原则：`数据流主干清单和清晰度`、`所有权清晰度和边界封装`、`围绕主干的非主干关注点`。
- `主干跨度充分性规则`（强制）：主要主干必须足够长以暴露真实业务路径。实际默认为 `4-5` 个有意义的节点。
- `权威边界规则`（强制）：当一个边界是领域主题的权威公共入口点时，其上方的调用者应依赖该边界而非同时依赖该边界及其内部拥有的机制之一。

### 3) 草拟设计提案文档

- `Medium/Large` 必需。`Small` 可选。
- 前置条件：`requirements.md` 为 `Design-ready`（或 `Refined`）。
- 从数据流主干开始设计：识别主要执行/数据流主干、命名主线节点、定义所有权、识别非主干关注点。
- 使用 `stages/03-design/proposed-design-template.md`。

### 4) 按用例构建未来态运行时调用栈

- 所有大小（`Small`、`Medium`、`Large`）必需。
- 对每个用例，从入口点到完成在调试追踪格式中编写未来态运行时调用栈。
- 使用 `stages/04-future-state-runtime-call-stack/future-state-runtime-call-stack-template.md`。

### 5) 审查未来态运行时调用栈（未来态 + 架构 + 命名 + 整洁门控）

- 创建 `future-state-runtime-call-stack-review.md` 作为强制审查产物。
- 以明确轮次运行审查并在同一审查产物中记录每轮。
- 每轮运行专门的缺失用例发现扫描。
- 门控 `Go` 标准：连续两轮深度审查无阻塞项、无需持久化产物更新且无新发现用例。
- 使用 `stages/05-future-state-runtime-call-stack-review/future-state-runtime-call-stack-review-template.md`。

### 6) 实现源代码 + 单元/集成并追踪进度

- 使用自底向上、测试驱动的方法。
- 在阶段 5 门控 `Go Confirmed` 后，最终确定 `implementation.md` 基线，然后开始执行。
- 在首次源代码编辑前更新 `workflow-state.md`：`Current Stage = 6`，`Code Edit Permission = Unlocked`。
- 强制规则：无向后兼容垫片、无遗留分支、清理死代码、保持所有权依赖有效、文件正确放置、主动源文件大小压力（`>500` 已避免、`>220` 变更行在阶段 6 期间评估）。
- 使用 `stages/06-implementation/implementation-template.md`。

### 7) 实现 API/E2E 和其他可执行验证并运行阶段 7 门控（强制）

- 阶段 6 完成后立即运行。
- 创建/更新 `tickets/in-progress/<ticket-name>/api-e2e-testing.md`。
- 持久验证优先规则：先实现或更新应留在仓库中的验证测试和资产。
- 验收标准闭环：每个范围内验收标准必须映射到至少一个可执行场景。
- 每条相关主干必须映射到至少一个场景。
- 使用 `stages/07-api-e2e/api-e2e-testing-template.md`。

### 8) 运行代码审查门控（强制，测试后）

- 仅在阶段 7 门控为 `Pass` 后运行。
- 在阶段 8 进入时设置 `Code Edit Permission = Locked`。
- 创建/更新 `tickets/in-progress/<ticket-name>/code-review.md`。
- 源文件大小策略（强制）：变更源文件 `>500` 有效非空行 => `Design Impact` + `Fail`。`>220` 变更行增量需要设计影响评估。测试文件不受此限制。
- 强制审查评分卡：按规范顺序的十个分类（`数据流主干清单和清晰度` 到 `清理完整性`），每个分类 `>= 9.0` 为干净通过。
- 使用 `stages/08-code-review/code-review-template.md`。

### 9) 同步项目文档（强制，测试后 + 审查后）

- 使用 `stages/09-docs-sync/docs-sync-guide.md`。
- 创建/更新 `tickets/in-progress/<ticket-name>/docs-sync.md`。
- 使用 `stages/09-docs-sync/docs-sync-template.md`。
- 阶段 7 和阶段 8 完成后更新项目 `docs/` 文件夹下的文档。
- 如果无文档影响，记录明确的 "No docs impact" 决策和理由。

### 10) 最终移交

- 仅在实现、阶段 7 验证、阶段 8 代码审查和文档同步全部完成后完成移交。
- 创建/更新 `tickets/in-progress/<ticket-name>/handoff-summary.md`。
- 使用 `stages/10-handoff/handoff-guide.md` 和 `stages/10-handoff/handoff-summary-template.md`。
- 移交摘要写入后，保持阶段 10 开放直到用户明确确认完成/验证。
- 用户确认后：移动工单到 `tickets/done/` -> 仓库最终确定 -> 发布/出版（如适用）-> 工作树/分支清理。

## 输出默认值

如果用户未指定文件路径，按阶段顺序写入项目本地工单文件夹：

- 阶段 0：创建工单文件夹 + `workflow-state.md` + `requirements.md`（`Draft`）
- 阶段 1：`investigation-notes.md`
- 阶段 2：更新 `requirements.md`
- 阶段 3：`Small` 开始 `implementation.md`；`Medium/Large` 创建 `proposed-design.md`
- 阶段 4：`future-state-runtime-call-stack.md`
- 阶段 5：`future-state-runtime-call-stack-review.md`
- 阶段 6：最终确定/更新 `implementation.md` + 执行源实现
- 阶段 7：`api-e2e-testing.md`
- 阶段 8：`code-review.md`
- 阶段 9：`docs-sync.md` + 更新 `docs/`
- 阶段 10：`handoff-summary.md` + （如适用）`release-notes.md` + 仓库最终确定

## 模板和参考资料

- 共享：
  - `shared/design-principles.md`
  - `shared/common-design-practices.md`
  - `shared/workflow-state-template.md`
- 阶段 0 引导：
  - `stages/00-bootstrap/bootstrap-checklist.md`
- 阶段 1 调查：
  - `stages/01-investigation/investigation-guide.md`
- 阶段 2 需求：
  - `stages/02-requirements/requirements-refinement-guide.md`
- 阶段 3 设计：
  - `stages/03-design/proposed-design-template.md`
- 阶段 4 未来态运行时调用栈：
  - `stages/04-future-state-runtime-call-stack/future-state-runtime-call-stack-template.md`
- 阶段 5 未来态运行时调用栈审查：
  - `stages/05-future-state-runtime-call-stack-review/future-state-runtime-call-stack-review-template.md`
- 阶段 6 实现：
  - `stages/06-implementation/implementation-template.md`
  - `stages/06-implementation/implementation-example.md`
- 阶段 7 API/E2E + 可执行验证：
  - `stages/07-api-e2e/README.md`
  - `stages/07-api-e2e/api-e2e-guide.md`
  - `stages/07-api-e2e/api-e2e-testing-template.md`
- 阶段 8 代码审查：
  - `stages/08-code-review/README.md`
  - `stages/08-code-review/code-review-guide.md`
  - `stages/08-code-review/code-review-principles.md`
  - `stages/08-code-review/code-review-template.md`
- 阶段 9 文档同步：
  - `stages/09-docs-sync/docs-sync-guide.md`
  - `stages/09-docs-sync/docs-sync-template.md`
- 阶段 10 移交：
  - `stages/10-handoff/README.md`
  - `stages/10-handoff/handoff-guide.md`
  - `stages/10-handoff/handoff-summary-template.md`
  - `stages/10-handoff/release-notes-template.md`
