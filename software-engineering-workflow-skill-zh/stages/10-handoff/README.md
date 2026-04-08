# 阶段 10 最终移交

## 目的

持久化最终交付摘要，等待用户明确验证，归档工单，在适用时执行仓库定稿，运行任何适用的发布/出版/部署步骤，并完成所需的工单工作树/分支清理。

## 进入此阶段条件

- 阶段 9 已完成
- 工程交付已完成，工作流准备等待用户验证

## 阶段拥有的输出

- `tickets/in-progress/<ticket-name>/handoff-summary.md`
- 需要时 `tickets/in-progress/<ticket-name>/release-notes.md`
- 适用时的归档工单状态和仓库定稿记录
- 适用时的发布/出版/部署记录
- 适用时的定稿后工作树/分支清理记录

## 退出门控

仅在用户明确确认完成或验证，且任何所需的移至 done、仓库定稿、适用的发布/出版/部署工作以及所需的定稿后清理均已完成或明确记录为不需要时，才离开阶段 10。

## 本地文件

- `handoff-guide.md`：移交、验证暂停和定稿规则
- `handoff-summary-template.md`：规范的移交摘要结构
- `release-notes-template.md`：适用时的发布说明结构
