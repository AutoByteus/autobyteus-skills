# Ryan Few-Shot Examples (EN + CN + Conversion)

Use these examples to imitate structure and rhetorical motion, not to copy sentences.

## Example A: English Thesis-First Opening

### Prompt Shape

- Topic: why architecture design and code review matter more than raw code generation
- Goal: explain the core bottleneck in AI software engineering
- Audience: engineers building with coding agents

### Ryan-Style Example

`The core work in AI software engineering is not code generation itself. It is architecture design and code review. In an agentic workflow, that means the strongest leverage sits upstream: in the agent that defines structure, and in the agent that judges whether that structure remains intact while code is written.`

### Why It Works

- Thesis appears immediately.
- The opening uses contrast form: `not X, but Y`.
- The last sentence moves from the abstract claim to an operational framing.

## Example B: Root-Cause Correction Paragraph

### Prompt Shape

- Topic: why AI-generated code becomes hard to review
- Goal: replace a shallow explanation with a deeper diagnosis
- Audience: technical readers who already believe context windows are the problem

### Ryan-Style Example

`A common explanation is that AI code becomes unreviewable because agents generate too much code too quickly. That is true. But it is not the root cause. The deeper problem is architectural fragmentation. When business logic is spread across too many locally reasonable files without a clear spine or clear ownership, the reviewer must keep reconstructing the whole system from fragments.`

### Why It Works

- It acknowledges the common belief before challenging it.
- `That is true. But it is not the root cause.` is a typical Ryan pivot.
- The paragraph replaces vague criticism with a specific structural diagnosis.

## Example C: Signal-To-Diagnosis Bridge

### Prompt Shape

- Topic: what repeated context rebuilding means
- Goal: interpret an observed failure loop as an architectural signal
- Audience: engineers working with long-running coding agents

### Ryan-Style Example

`We kept seeing the same pattern. The coding agent would reread many files, recover enough context to make progress, then lose that reconstruction after compaction and begin the same cycle again. That turned out to be a very important signal. It was not only a context-window problem. It was an architecture problem.`

### Why It Works

- Starts from repeated observation rather than theory.
- Uses a short emphasis sentence to mark the turning point.
- Converts a runtime symptom into a root-cause diagnosis.

## Example D: Structured Review-Dimensions Section

### Prompt Shape

- Topic: how code review should evaluate AI-generated systems
- Goal: show that review criteria must be structural and explicit
- Audience: readers designing review workflows

### Ryan-Style Example

`That changes code review completely. Review should not begin from a pile of generated files. It should begin from the business spine and the anchored domain subjects around it. In practice, that means the review must judge concrete structural dimensions: spine clarity, ownership boundaries, API shape, separation of concerns, shared-structure tightness, validation strength, edge-case correctness, and cleanup completeness.`

### Why It Works

- Opens with a compressed transition line.
- Moves from principle to a concrete list of review surfaces.
- Uses repeated architecture nouns instead of abstract quality language.

## Example E: English Closing Pattern

### Prompt Shape

- Topic: why architecture and review are upstream infrastructure
- Goal: end with a strong directional takeaway
- Audience: technical decision-makers

### Ryan-Style Example

`If architecture stays implicit, fast code generation creates drift. If architecture becomes explicit and review stays strict, code becomes easier to inspect, easier to challenge, and easier to evolve safely. That is why architecture design agents and code review agents are not optional tools around coding. They are core infrastructure for end-to-end AI software engineering.`

### Why It Works

- Uses conditional structure to compress the argument.
- Restates the main thesis without sounding repetitive.
- Ends on an infrastructure-level claim rather than a soft summary.

## Example F: Chinese Opening Pattern

### Prompt Shape

- 主题: 为什么 AI 软件工程的核心不是写代码本身
- 目标: 说明架构设计与代码审查为什么更关键
- 读者: 使用 AI 编码智能体的工程师

### Ryan-Style Example

`AI 软件工程的核心工作，并不是代码生成本身，而是架构设计和代码审查。在 agentic workflow 里，真正决定系统质量上限的，不是让 agent 写得更快，而是让设计足够清晰、让审查足够严格。`

### Why It Works

- 开头直接给出结论。
- 保留了 `不是 X，而是 Y` 的对比结构。
- 中文表达自然，但逻辑骨架与英文一致。

## Example G: Cross-Language Conversion (Preferred Mode)

Use this when the user writes first in English and asks for Chinese adaptation.

### Source English Paragraph

`If the data-flow spine is clear, review no longer has to begin from thousands of lines of code. It can begin from the business path itself. You follow the spine, check the anchored owners, inspect the authoritative boundaries, and verify whether side concerns remain side concerns.`

### Target Chinese Adaptation

`如果 data-flow spine 足够清晰，审查就不必从成千上万行代码开始，而可以直接从业务路径开始。你先沿着 spine 去追踪，再检查锚定其上的 owner、authoritative boundary，以及那些 side concern 是否真的仍然只是 side concern。`

### Conversion Notes

- Preserve the order of reasoning, not the exact sentence boundaries.
- Keep key technical terms stable when Chinese paraphrase would reduce precision.
- Let the Chinese version sound like a native technical article, not a literal translation.

## Example H: English Factual Technical Opening

### Prompt Shape

- Topic: describe how a product implements agent teams
- Goal: explain the runtime model in a factual technical way
- Audience: engineers who dislike sales or manifesto tone

### Ryan-Style Low-Pressure Example

`This note describes how agent teams are implemented in AutoByteus and summarizes the runtime behavior we have observed in recent software-engineering workflows. The main observation is that the workflow becomes more stable when each member operates with a narrow responsibility, a durable artifact boundary, and explicit handoff rules. The sections below focus on the runtime and workflow mechanisms that produce that behavior.`

### Why It Works

- Opens with scope instead of a slogan.
- States the main observation without forcing a contrastive hook.
- Keeps the tone analytical while preserving clear structure.

## Example H2: English Builder-Direct Opening

### Prompt Shape

- Topic: explain why a team design replaced a single workflow skill
- Goal: write from the builder's perspective without sales tone
- Audience: engineers who want a practical system-evolution explanation

### Ryan-Style Low-Pressure Example

`In AutoByteus, we first used one end-to-end software-engineering workflow skill. It already handled investigation, design, implementation, validation, code review, and final handoff in one structured flow. When the tasks became larger, we started to see the same pressure point: one agent had to carry too many stage-specific responsibilities at once. That is why we kept the workflow and moved the runtime to a dedicated agent team.`

### Why It Works

- Opens directly from the prior system state.
- Uses builder ownership language without sounding promotional.
- Preserves factual flow: prior system, capability, limitation, redesign.

## Example H3: Builder-Direct Mechanism Correction

### Prompt Shape

- Topic: explain more precisely why a single-agent workflow struggled
- Goal: replace a generic explanation with the actual runtime mechanism
- Audience: technical readers who care about correctness more than rhetoric

### Ryan-Style Low-Pressure Example

`The pressure did not come only from one agent handling many stages. On larger tickets, repeated compaction forced the agent to rebuild part of its working context again and again. At the same time, the agent had to carry the workflow state itself: current stage, re-entry conditions, artifact obligations, and finalization rules. So part of the token budget was being spent on maintaining the workflow process, not only on the local engineering task.`

### Why It Works

- Replaces a broad abstraction with the concrete runtime mechanism.
- Keeps builder-direct factual tone.
- Moves from observed behavior to bounded explanation without dramatizing it.

## Example I: Factual Technical Evidence Paragraph

### Prompt Shape

- Topic: explain why a team workflow stays stable
- Goal: describe the mechanism without essay-like rhetoric
- Audience: technical readers evaluating architecture

### Ryan-Style Low-Pressure Example

`In the current software-engineering team, members do not continuously coordinate through freeform discussion. They usually work until an artifact is produced, then hand off the cumulative artifact set to the next specialist. This reduces repeated context reconstruction and keeps the coordination surface smaller and easier to inspect.`

### Why It Works

- States behavior first, then implication.
- Uses no forced diagnosis language.
- Keeps nouns concrete and stable.

## Example J: Factual Technical Closing

### Prompt Shape

- Topic: summarize the practical value of a team design
- Goal: end with a bounded conclusion rather than a manifesto
- Audience: engineers reading a technical note

### Ryan-Style Low-Pressure Example

`Taken together, these behaviors suggest that the practical value of the team structure is not only parallelism. It is responsibility partitioning under explicit runtime coordination. In the current implementation, that appears to be the main reason the workflow remains stable across design, implementation, validation, and review stages.`

### Why It Works

- Keeps the conclusion bounded to the observed implementation.
- Still compresses the central claim.
- Avoids product-marketing tone.

## Example K: Anti-Pattern And Fix

### Too Detached / Too Salesy

`This article explains a major breakthrough in how AutoByteus rethinks AI software engineering. What changed our thinking was not just that the workflow worked, but that it revealed a deeper future for agent teams.`

### Better Ryan Builder-Direct

`In AutoByteus, we first used one end-to-end workflow skill. It worked well on small tickets. The limit appeared on larger tickets, where repeated compaction and workflow-state bookkeeping started consuming too much context. That is why we moved the same workflow into a dedicated agent team.`

### Why The Fix Is Better

- Removes promotional framing.
- Restores builder ownership.
- States mechanism instead of slogan.

## Example L: Redundancy Anti-Pattern And Fix

### Too Repetitive

`The workflow was already strong. The important point is that the workflow was already strong. This is why the practical value is that the workflow was already strong but the runtime was not ideal.`

### Better Compressed Version

`The workflow itself was already complete. The problem appeared in how one agent had to carry it at runtime.`

### Why The Fix Is Better

- Keeps the core distinction.
- Removes empty transition phrases.
- Preserves the claim in one clean sentence instead of three restatements.

## Reusable Micro-Templates

### English Thesis Pivot

`The visible problem is X. The deeper problem is Y.`

### English Diagnostic Pivot

`That is true. But it is not the root cause.`

### English Signal Marker

`That turned out to be a very important signal.`

### English Section Transition

`That changes code review completely.`

### English Directional Close

`That is the direction I now believe in.`

### English Factual Opening

`This note describes X and summarizes the observed behavior of Y.`

### English Builder-Direct Opening

`In Product X, we first used Y. It already handled Z. When scope increased, we started to see Q. That is why we changed the runtime to W.`

### English Mechanism Correction

`The earlier explanation was too broad. The more exact mechanism was X, which caused Y during long-running execution.`

### English Factual Close

`Taken together, these observations suggest X in the current implementation.`

### Chinese Thesis Pivot

`表面上的问题是 X，更深层的问题其实是 Y。`

### Chinese Section Transition

`这会彻底改变我们做代码审查的方式。`

### Chinese Directional Close

`这就是我现在更相信的方向。`
