# ZCode 接管协议 —— Collected-Papers-of-Fields-Medalists

> **状态**：`CURRENT_HANDOFF / WAITING_FOR_USER_CONFIRMATION / NO_EXECUTION_AUTHORITY`
>
> **适用 Host**：ZCode Desktop 的主控会话。此文件不是 ZCode 功能探测、App Server 运行收据、Sub Agent 授权或论文完成证明。
>
> **当前基线**：本协议写入时 canonical `main` 为 `c40018765f4fb88e038d2e5940872895ab716235`；接手时必须重新核对实际 HEAD、index、工作树与 dirty 状态。
>
> **替代关系**：本文件原位替代 2026-10-01 的旧 ZCode 流程。旧文本中“直接开工”“自动 push”“不使用 Sub Agent”等内容已经失效，历史由 Git 保留，不得继续执行。

你是接手本仓库的 **ZCode 主控**。你的任务是先建立只读认知闭包、向用户提交一个可审查的确认包，并且**等待用户明确确认**。本文件本身不授权开始任何论文或控制面工作。

## 0. 不可绕过的确认 Gate

用户仅授权了“交接给 ZCode、写入本协议”。这不等于下列任何动作的许可。

在用户后续明确确认前，状态必须保持：

```text
WAITING_FOR_USER_CONFIRMATION
```

在这个状态下，ZCode 主控只能做以下**只读恢复**：读取本协议和项目 current owners、检查 Git status/HEAD/worktree、形成确认包。不得把只读恢复扩大为论文审计。

**确认前严禁：**

- 启动 `codex app-server`、broker、任何额外 Codex/model 进程、App Server smoke 或 resume；
- 创建或启动任何 ZCode Sub Agent、递归子 Agent、Project Peer 或自动化；
- 启动/停止 MinerU 服务、下载模型、运行 MinerU 解析、上传 PDF，或生成审计 PNG/裁片；
- 打开某篇论文开始逐页审计、修改 MinerU Markdown、写 AUDIT、创建 worktree、commit、tag、push、publish；
- `git reset`、`git restore`、`git clean`、`stash`、worktree remove/archive，或改写任何旧 Peer 历史；
- 把旧 `clientThreadId`、旧 worktree、旧 `turn completed`、旧 commit 或旧任务标题解释成仍可恢复/正在运行的 session。

用户确认必须直接针对一个可执行包，而不只是“可以接手”。ZCode 先向用户展示以下信息并等待答复：

```text
请求确认：
1. 执行通道：Codex CLI App Server / ZCode 原生 Sub Agent；
2. 本次仅做 non-paper pilot，还是指定一篇论文；
3. 目标论文或 pilot 的精确路径、输入 PDF/Markdown 身份与当前 base OID；
4. 主控 actor、每个 worker/agent 的实际或拟用模型与思考级别；
5. worker/agent 数量、是否并行、独立 worktree 和唯一写入路径；
6. 预期验证、停止/恢复方案、最大并发；
7. Git 范围：是否允许本地 commit；push 仍默认不允许。
```

只有用户明确确认这个包，ZCode 才可进入相应下一阶段。若用户只说“开始”，但未选择通道、作用域或写入授权，要求澄清而不自行选择。

## 1. 先恢复当前项目认知（只读）

在提交确认包前，按下列顺序读取并以实物为准：

1. `AGENTS.md`：项目硬约束、Git/并发/确认 Gate 与手工 Edit 规则；
2. `README.md`：资产地图。它目前可能有用户未提交修改，绝不修改、暂存、stash 或 reset；
3. `MEMORY.md`：当前执行队列、冻结后状态、开放问题；
4. `feature-list.md#AUDIT-001/#AUDIT-002` 与 `rulings.md#R-001` 至 `#R-005`；
5. 本文件；
6. `AUDIT-SOP.md`、`AUDIT-INDEX.md`、`AUDIT-PROGRESS.log` 末尾；
7. `dev-docs/002-2026-10-02-旧Peer批次冻结与收割收据.md`：旧 Peer 候选/集成 OID、未完成断点、未提交资产；
8. `dev-docs/001-2026-10-02-Codex-App-Server并发Peer工作流调查与试点方案.md`：仅当用户后来选择 App Server 时使用；其状态仍是 `DESIGN_DRAFT / NOT_RUNTIME_VERIFIED`。

然后只读检查：实际 repo root、`git status --short`、当前 branch/HEAD、`git worktree list`、相关未完成论文目录和引用的 AUDIT/PDF/Markdown。索引、提示词和 commit subject 只负责定位；关于论文内容、页数、候选修复和运行状态的判断必须回到 PDF、Markdown、审计实物、Git diff 与当前运行证据。

## 2. 冻结后的真实工作状态

旧 Peer 批次已停止，且已由 Codex Master 收割/登记；ZCode 不得重新启动或复制它们。

| 分类 | 当前状态 | ZCode 的含义 |
|---|---|---|
| 已完成 | 102/138 条 INDEX 项 | 不重做，不因旧工作树仍存在而重新审计。完成只表示 PDF→Markdown 转录审计/修复证据闭合，不表示数学证明被独立验证。 |
| 审计证据已收割但未完成 | P17、P19、P27、P31、P32、P34 | 只可在用户确认后从已记录断点继续；先核 current main、候选 OID、目标 Markdown 与 AUDIT。 |
| 映射阻塞 | P37 `Birkar_2016_fano_flips` | 93 页 Birkar PDF 与 Keshvari Markdown 错配。先有正确导出并完成映射核验，不能改名冒充。 |
| hold、未集成 | P40 Wang–Zahl | 只到 p.118/127，且 AUDIT-SOP 与旧 handoff 的方法范围冲突未闭合；不能接着写或合并，先让用户确认复核范围。 |
| 冻结无候选 | P10、P12、P30、P41–P65 | 旧派发/clientThreadId 不构成已开始工作；不得直接“resume”。 |

六篇未完成项目的已知最小续办点如下；这只是确认包的候选，不是自动队列：

| 项目 | 已保全状态 | 真正继续前要完成的工作 |
|---|---|---|
| P17 Mirzakhani simple geodesics | p.1–p.8/49 初审，未修复 | 从 p.9 审到 p.49，再统一手工修复/全文复读。 |
| P19 Margulis English | 50/50 初审，修复/终读未闭合 | 按现有 FAIL 证据逐处修复，再完整复读。 |
| P27 Quillen handwritten | 66/66 初审，修复未开始 | 使用现有页级证据手工修复，再完整复读。 |
| P31 Werner | p.1–p.57/72 初审，未修复 | 从 p.58 续审，再统一修复/全文复读。 |
| P32 Novikov | 86/86 初审与修复候选 | 重新完整复读修复后 Markdown，并登记终验。 |
| P34 EGA III | 90/90 初审，修复未开始 | 按现有页级证据手工修复，再完整复读。 |

精确 candidate/integration OID、P07/P16 页数元数据冲突、P39/P34/P27 未提交 300dpi 文件及其哈希在冻结收据中；不从这张摘要推断额外事实。

## 3. 角色、身份和 Git 边界

确认后，用户指定的 ZCode 主控才是获准 scope 的 `CANONICAL_INTEGRATOR`。它必须：

- 采用一个新的、可追溯的实际 actor ID；不冒充或回写历史 `Master-Luna` / `Peer-PNN` 身份；
- 记录实际 Host、模型、思考级别、提示词/工具/权限边界，不把请求参数当成运行证据；
- 只让 worker 写自己唯一的论文目录、目标 Markdown、篇级 AUDIT 与唯一前缀的证据图；
- 串行维护根级 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、`MEMORY.md`，并只在接受 exact candidate 后更新 current truth；
- 对每个候选核对 source/base/target OID、路径所有权、dirty/index、最终 diff、证据和验证；
- 保留旧 candidate、worktree、未跟踪文件和历史，不为“清理”丢弃资料。

`README.md` 的当前未提交修改属于用户。任何 ZCode worker 都不得触及它。`dev-notes/` 是本地对话归档，不应被纳入业务 commit。push、远端发布、历史重写、删除或 worktree 清理在本协议下全部未授权。

## 4. 确认后可选的执行通道

### A. Codex CLI App Server 路线

这是一个**外部 Codex CLI 进程**，不是“ZCode 原生 ACP”。ZCode 只有在当前实际工具面允许它创建/观察该进程、且用户在确认包中选定这一通道时才可使用它。

确认后的第一步仍不是论文：在独立、可丢弃、**不含论文资产写入**的 worktree 运行一个范围明确的 control-plane pilot。它至少要留下可复核的实际证据：

1. 实际 Codex CLI/App Server 版本、可用模型/思考级别与权限配置；
2. 精确 cwd 与独立 worktree；`thread.id`、`thread.sessionId`、每个 `turn.id`，以及事件流；
3. `thread/start` → 观察 → `turn/steer` → 正常完成或精确 interrupt 的链；
4. 停止并重启 App Server 后，用已保存的 `thread.id` 做 `thread/read`/`thread/resume`，同时核对 Git/worktree/PID/事件状态；
5. sandbox、shared `CODEX_HOME`、模型重路由、worker session 混淆和错误恢复的实际结果。

Pilot 通过后，**再次**向用户确认目标论文与 worker envelope；不得从 pilot 自动推进到论文。若恢复、ID、cwd、模型、权限或 worktree 对账失败，状态为 `RECONCILIATION_REQUIRED`，停止写入，不重发整篇 prompt，不创建替代 worker。

共享 `agent_session_broker.py` 是候选底座而非已验证产品能力；已有调查没有证明其真实 Host 的 resume/steer/restart 路径闭合。不要把设计文档、fake test、`thread completed` 或进程退出写成论文完成。

### B. ZCode 原生 Sub Agent 路线

此路线只在 ZCode **当前实际**提供原生 Sub Agent 能力、并且用户确认 exact envelope 后可用。不得把 Codex 的 Sub Agent 模型 allowlist、profile 名称、CLI/ACP 假设或权限规则照搬到 ZCode。

确认包必须额外写清：

- 每个 Sub Agent 的数量、单一目标、非目标、实际模型与思考级别；
- read/write scope、独立 worktree 与唯一写入路径；
- context 输入、允许工具、禁止外部动作、递归=`false`；
- 返回格式（`Claims / Evidence / Conflicts / Unknowns / Mutations / Verification / Recommendation`）；
- 等待、纠偏、失败、重试、关闭及由 ZCode 主控验收/集成的方案。

默认采用一个受控 worker；没有用户对并发数和具体写入范围的明确确认，不得扩大为多个 Sub Agent。Sub Agent 完成只是候选证据，ZCode 主控必须重新核 exact diff、PDF/Markdown/AUDIT 证据、测试与未提交状态后才可集成。

## 5. 任一通道下都不变的论文业务合同

确认后的真实论文工作仍受 `AUDIT-SOP.md`、`AGENTS.md` 和 R-001 约束：

1. 先做 PDF↔Markdown 映射 Gate；标题、作者、页数、文件身份不一致即停。P37 的错误 Markdown 不能被重命名或覆盖来伪造映射。
2. 原始 PDF 是转录裁决源；print quirk/错字忠实保留并登记，不能按数学预期静默改正。
3. MinerU Markdown 只能用当前 Host 的结构化 Edit 工具逐处人工修改。禁止 Python、正则、`sed`、Perl、heredoc 或其他批量写回；若 Edit 不可用，暂停该篇。
4. 每处修改必须链接到 PDF 页和足够原文证据；疑难字形按当前 SOP 做原页/300dpi 仲裁。
5. 修复后必须完整复读最终 Markdown，逐项回核页面证据；脚本仅用于只读清点，不能替代内容核验。
6. PDF 原件只读；不得在未获确认时启动 MinerU server、下载模型、远程上传或改变运行配置。
7. worker 的 `turn completed`、Sub Agent final、Git commit、PNG 存在或页面计数都不是篇目完成判据；完成需要当前 SOP 的审计、修复、全文复读、验证和 canonical integration 证据。

## 6. 首次向用户的正确回复

在本协议的 Gate 下，ZCode 的第一条业务回复应当是一个**确认请求**，类似：

> 我已只读恢复当前冻结状态：102 篇完成，6 篇保全审计证据但未完成；P37 映射阻塞，P40 仍 hold。我尚未启动 App Server、Sub Agent、MinerU、论文处理或 Git 写入。请确认本次采用 App Server 或 ZCode 原生 Sub Agent；确认目标（例如 P17/P19/P27/P31/P32/P34/P37/P40 或非论文 pilot）、模型/思考级别、agent/worker 数、worktree/写入范围以及是否仅允许本地 commit。收到明确确认前我会保持 `WAITING_FOR_USER_CONFIRMATION`。

不要把以上示例当成确认本身，也不要在用户没有选择 scope 时替用户挑选论文或并发数。

## 7. 交接完成与停止条件

本协议完成的含义仅是：ZCode 能从 current owners 恢复项目、知道旧工作已冻结、能正确请求确认，并能在确认后选择受控通道。它不表示任何新论文已开始或 App Server/Sub Agent 已可用。

若发现 HEAD、README dirty、INDEX、PDF、MinerU、候选 OID、worktree、实际 ZCode capability 或用户确认与本文件不一致：停止相关动作，说明直接证据和冲突，回到用户确认。不要为了“接手成功”而启动替代 worker、修改根总账或清理旧资产。
