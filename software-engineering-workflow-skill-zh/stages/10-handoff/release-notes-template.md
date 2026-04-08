# 发布说明模板

当工单产生面向用户的应用发布或 GitHub Release 正文时，使用此模板创建 `tickets/in-progress/<ticket-name>/release-notes.md` 或 `tickets/done/<ticket-name>/release-notes.md`。

规则：

- 仅面向用户
- 仅功能变更
- 所有章节合计 3 到 7 个要点
- 每个要点一行
- 不包含重构、依赖升级、测试、仅文档变更或内部实现细节
- 省略空章节而非写填充文本
- 除非用户明确要求，不包含升级步骤

模板：

```md
## 新功能
- 添加了 ...

## 改进
- 改进了 ...

## 修复
- 修复了 ...
```
