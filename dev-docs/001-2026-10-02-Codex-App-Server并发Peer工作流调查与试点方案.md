# Codex App Server 并发 Peer 工作流调查与试点方案

> **状态**：`ADOPTED_DIRECTION / DESIGN_DRAFT / NOT_IMPLEMENTED / NOT_RUNTIME_VERIFIED`
>
> **日期**：2026-10-02
>
> **范围**：仅调查与提出后续方案；不启动 App Server、Codex model 或论文 Peer，不处理论文内容。
>
> **当前要求**：`AUDIT-002` / `rulings.md#R-004` 规定：旧 Project Peer 批次已冻结，后续工作方向为独立 worktree 的 Codex CLI App Server；身份留痕、独占写入路径和 Master 单一集成者约束保持不变。本文件不证明控制面已经运行或已能派发论文 worker。

## 1. 决策摘要

用户已在旧 Peer 批次停止后的冻结点采纳 Codex CLI App Server 作为后续 worker 的控制方向。它能在创建时同步返回 `thread.id`，通过事件流观察线程与轮次，并提供 `thread/resume`、`turn/steer`、`turn/interrupt` 等控制方法。对比 project Peer 异步创建返回 provisional `clientThreadId` 的路径，它有机会让 worker 身份、worktree、实际 Codex thread/turn 和恢复动作建立更直接的对应关系。

但调查没有证实用户所回忆的 Codex App Server 已经在 `/Users/aurolafly/shuxuedashi-analysis-system` 这个仓库中运行。当前能找到的真实协作运行证据属于 OpenCode ACP / Devin ACP，不是 Codex CLI `app-server`。因此，续传系统可以提供的是流式观测、按任务隔离工作目录、保留每轮产物和失败恢复方面的参考经验，不能替新方案提供 Codex App Server 的运行通过证明。用户回忆的实例可能是未入库/外部运行现场，也可能是把 ACP server 泛称为 App Server；目前原因 `UNKNOWN`。

当前唯一可复用的 Codex App Server 代码底座是共享仓库 `/Users/aurolafly/codex/tools/agent_session_broker.py`：它已能按 worker `cwd` 启动独立 `codex app-server` 子进程、调用 `thread/start` 并取得 thread id、发送轮次、收事件和中断。但恢复与交互接口并未闭合：没有 `thread/resume`、`turn/steer`，broker 启动时也不会从持久状态重建 worker/session。能力索引仍为 `REVIEW_NEEDED`，当前真实 Host smoke 尚未闭合。

所以当前结论是：沿用 broker 作为“宿主进程/线程控制层”的候选设计；论文队列、PDF/Markdown 身份、页级验收仍完全归当前论文项目的 ledger、SOP 与 Master。先用不改论文的隔离任务资格化一个完整 start/observe/steer/cancel/restart/resume 链，资格化通过后才可启动首个新的 App Server worker。旧 batch 的收割分类及精确 OID 见 `dev-docs/002-2026-10-02-旧Peer批次冻结与收割收据.md`；冻结的 project Peer 状态不能由 `clientThreadId` 自动转换，未完成任务不得直接重复启动或假设可导入旧对话。

## 2. 调查快照、范围与边界

| 系统/资产 | 检查快照 | 本次使用方式与边界 |
|---|---|---|
| 论文审计项目 | 调查快照 `main@42ad5ffc8481b31e1ea640c8182a4ef1c19efbec`；旧 Peer 收割后的 current state 见收据 002 | 调查时读取项目要求、状态、AUDIT 日志/SOP；后续冻结收割独立记录 exact candidate/integration OID。既有 `README.md` 修改与 `dev-notes/` 未跟踪资产均保留，未触碰。 |
| 续传解题系统 | 用户路径 `/Users/aurolafly/shuxuedashi-analysis-system`；Git 实际根 `/Volumes/4T-SSD/HOME-Projects/shuxuedashi-analysis-system`；`main@667e960d6cbe815ab26f041be1fa584651ed5ecd` | `git status --short` clean；只读读取 AGENTS/AI-GUIDE/README、ACP 设计报告、代码和已入库的 U1/U2 原始 JSONL/导出。未运行解题管线、SOP、OpenCode、Devin 或外部数据库操作。 |
| 共享 Codex 控制 broker | `main@d039261aec53c50bb062e479114e245dd2168059` | 检查已跟踪的 broker/测试/能力索引；该 repo 同时存在未跟踪路径，本次没有在其中写入。 |
| Codex CLI | `codex-cli 0.157.0` | 仅检查版本与 `codex app-server --help`，未启动 App Server 或调用 model。CLI help 将 app-server 命令标为 experimental。 |
| 官方产品资料 | 2026-10-02 读取 | App Server API、resume/steer、sandbox 与 CODEX_HOME 语义；链接见 §11。官方材料没有给出可用于本机的 40 个独立 app-server process 容量保证。 |

本轮无代码、配置或论文内容改动，也没有启动任何新的 Peer 或模型。文档“调查过”不等于 App Server 已部署/运行/通过验收。

## 3. 续传解题系统中真正可复用的证据

### 3.1 后端名称与实际接线

该仓库的项目事实把两代/两条后端路径区分如下：

- `AGENTS.md` 描述 P27 legacy 续传管线通过 `devin -p` 和 tmux 执行，并由 continuation launcher、monitor、collector 与控制面管理；解题管线内部仍串行。
- `AGENTS.md` 将 v2 标为开发中的 OpenCode ACP + Ox Alpha observer/solver 流程。
- 当前 [src/v2_pipeline.py](/Users/aurolafly/shuxuedashi-analysis-system/src/v2_pipeline.py) 以 `opencode acp --cwd <work_dir>` 启子进程，调用 ACP `initialize`/`session/new`，经 `session/set_config_option` 设 model/effort 并验证回显，再以 `session/prompt` 执行任务，实时收集 ACP 通知并归档每轮资产；该函数收尾调用 `session/close` 并结束子进程。Round 级续传通过归档内容决定下一个绝对 Round，而不是恢复 Codex `thread.id`。
- 当前所查 tracked `src/`、`monitoring/`、`scripts/`、`tests/`、`docs/`、`dev-docs/` 中没有发现 Codex CLI `app-server` / `thread/start` / `thread/resume` 接线；对该仓库 `main` 全历史的 `git log -G` 搜索也没有命中。这个结论只覆盖上述仓库路径、tracked 文件与可查询 Git history；不排除未入库的机器现场、其他仓库或过去的 Codex Desktop task。用户所指具体 App Server 运行仍待 session/run locator 确认。

需要严格区分：OpenCode/Devin 的 ACP `sessionId` 和 Codex App Server 的 `thread.id` 是不同协议、标识和恢复接口。当前项目报告里的 ACP 运行数据不能被称为 Codex App Server evidence。

### 3.2 可直接核对的 ACP 运行样本

续传系统仍然提供了实用的控制面经验：不同 work unit 有自己的 cwd/session；启动时显式设置 model/effort 并核验回显；通知流实时保存在 JSONL；每轮的 prompt、trajectory、结果和审计对象分开持久化；调度器保持业务并发/队列语义，不把模型调用数量当成业务成功数。

| 样本 | 直接核查到的记录 | 它能支持的结论 | 它不能支持的结论 |
|---|---|---|---|
| WP-U1 smoke，2026-08-21 | tracked `tmp/wp_u1_opencode_run.log` 与 `tmp/wp_u1_devin_run.log` 记录启动命令、ACP `initialize/session/new/session/prompt`、session id、事件数、`end_turn` 和 `/tmp` 写读成功；对应通知 JSONL 可逐行解析。报告记载 OpenCode 1.18.21、Devin 3000.4.25。 | 当时这两个具体 ACP 配置在小型文件写读 smoke 上成功；通知流可实时观测。 | 不能证明 Codex App Server、resume/cross-process recovery、40 并发或后续 CLI 版本行为。 |
| WP-U2 内容完整性，2026-08-21 | tracked `tmp/wp_u2/c_acp.jsonl` 有 12,076 行、JSONL 全部可解析；独立聚合得到 12,062 个 `agent_thought_chunk`、合计 95,884 字符、0 个 `agent_message_chunk`。`c_meta.json` 记录 963.3 秒与 `end_turn`。对 `c_native_export2.json` 只比较 assistant-role 内容：reasoning 为 95,884 字符，与通知流完全相同；assistant text 为 0。导出的 user prompt 另有 871 字符，不能计入 assistant message。 | 该 OpenCode ACP 样本里 reasoning 通知与同 session 原生 export 的 assistant reasoning 字符总量一致；raw logs 和 export 都可用于事后重建。 | `end_turn` 不代表数学题已解；本样本无 assistant message，报告将其视为预算耗尽/零正文形态。不能把 transport 完成状态代替业务验收，也不能外推所有模型/版本。 |

原始文件目前可在上述 source repo 定位；其正文含数学提示/思考，报告不复制内容。U1/U2 详细分析分别见 [042-ACP双后端基线复验报告.md](/Users/aurolafly/shuxuedashi-analysis-system/dev-docs/042-ACP双后端基线复验报告.md) 与 [043-ACP内容完整性三路实验报告.md](/Users/aurolafly/shuxuedashi-analysis-system/dev-docs/043-ACP内容完整性三路实验报告.md)。

### 3.3 Resume 经验的准确状态

[046-OpenCode-ACP管线详细设计.md](/Users/aurolafly/shuxuedashi-analysis-system/dev-docs/046-OpenCode-ACP管线详细设计.md) 提议 launcher 重启后按 `session/list {cwd: work_dir}` 找回 OpenCode `sessionId`，再用 `opencode export` 取回 trajectory；同一报告也指出 `session/list` 没有完成状态字段，因此不应用它判断任务成功。这个是 OpenCode ACP 的设计/恢复构想，不是 Codex App Server `thread/resume`，也不等于当前 `src/v2_pipeline.py` 已实现它：目前所查 v2 代码为每个 Round 新建 OpenCode 进程/session，最后 close/terminate；业务续传点是已归档 Round 文件和下一绝对 Round。故只借鉴“进程恢复先对账会话 id、cwd 和持久化业务资产”的原则，不能把 046 当作 App Server 已通过 resume 的实测。

## 4. Codex App Server 官方能力与未验证项

官方 App Server JSON-RPC 能提供所需控制原语：

| API/字段 | 设计上的用途 | 方案必须遵守的语义 |
|---|---|---|
| `thread/start` | 新建一篇论文的 Codex conversation | 调用 response 会返回 `thread.id`，可在建 thread 后立即写入任务 ledger；同时保存 `thread.sessionId`。 |
| `thread/resume` | App Server 重启后重开已存 thread | 传入保存的 `thread.id`；不能用 `clientThreadId`、cwd 或名字推算。 |
| `thread/read` / `thread/list` | 不启动 turn 地读取状态/列表 | `thread/read` 可返回 `notLoaded`、`idle`、`systemError` 或 active 状态；`thread/list` 有精确 cwd filter。 |
| `turn/start` | 启动一个 worker turn | 每轮显式传入 `threadId`、worktree `cwd`、model、effort 和 sandbox policy；记录返回的 `turn.id`。 |
| `turn/steer` | 轮中追加控制输入 | 需要匹配的 `expectedTurnId`；不支持在 steer 请求里改 cwd、model、sandbox。 |
| `turn/interrupt` | 中断活动轮次 | 用精确 `threadId + turnId`；等待 `turn/completed` 并核验最终状态，不把 interrupt response 当作 worker 已停止。 |
| `item/*` / `turn/*` events | 流式监控/工作记录 | 事件证明观察到的协议行为，不单独证明论文页面审计正确或最终修复已提交。 |

Root thread 的 `thread.sessionId` 一般与自己的 `thread.id` 相同；fork 之后，tree root session id 可能不同。因此 resume 主键固定为 `thread.id`，并把 `thread.sessionId` 另存作 lineage。App Server 支持 thread/page history 持久化并允许重启后 resume；它不承诺 app-server 崩溃时的 shell 子进程、已执行工具动作或半写入文件自动恢复。重启的恢复合同必须包含进程与 worktree 对账。

官方 2026-10-02 文档把 `codex app-server` 命令标为 experimental、并说明不支持 production workload；对 CI/纯 job automation 文档更倾向 Codex SDK。论文 Peer 需要实时 event/steer 的人机监督，所以 App Server 候选仍有其用途，但应先作为本地实验性控制器资格化，不宣称 production-grade 或官方保证 40 并发。[Codex App Server](https://learn.chatgpt.com/docs/app-server) · [Codex SDK 选型说明](https://learn.chatgpt.com/docs/codex-sdk)。

官方 `CODEX_HOME` 定义包含配置、认证、logs、sessions、skills；不同 worktree 路径不会自动形成不同用户状态库。若每个子进程都用默认 home，它们共享此状态根；若每个 worker 设置独立 `CODEX_HOME`，则同时要解决 auth/config/skills 安装与恢复，不应仅为了隔离而复制凭据。多个 app-server 进程同时读写 shared CODEX_HOME/SQLite 的安全性与容量没有在本机验证，必须列为 pilot 验收项。[Codex 环境变量](https://learn.chatgpt.com/docs/config-file/environment-variables)。

## 5. 当前 broker 可复用部分与明确缺口

共享实现 [agent_session_broker.py](/Users/aurolafly/codex/tools/agent_session_broker.py) 在当前 `d039261aec53c50bb062e479114e245dd2168059` 已具备：

- worker 使用指定 `cwd` 创建 `codex app-server --listen stdio://` 子进程；`session/new` 对应 `thread/start`，将 `thread.id` 暴露为 facade `sessionId`，同时保存 native session tree ID 与 `instructionSources`。
- `session/prompt` 映射 `turn/start`，`session/cancel` 映射 `turn/interrupt`；相同 worker 的 turn 串行，不同 worker 可并发。
- 系统客户端可控制启动/session/prompt/cancel；Observer 只能读状态和序号化事件。完整 wire/stderr 留在 private worker directory；Observer 目前看到的是摘要/长度，不会拿到完整模型正文。
- fake app-server fixture 与 tests 覆盖 thread/start、一次 turn、delta/completed 映射，但目前没有 `thread/resume`、`turn/steer`、broker 进程重启后恢复 worker map 或 real-host restart smoke 的覆盖。Raw events/wire 存在，不代表 controller 能自动从它们恢复内存态。
- `state.json` 是 broker 身份/worker 计数摘要；worker/session map 存在运行时对象中。Codex adapter 捕获 thread id，但没有启动后 rehydrate `thread/list`/`thread/resume` 路径。
- broker `--max-workers` 当前默认 32，可配置更高；这只是 broker admission setting，不是 Codex/账户/主机支持的 concurrency 上限。共享 capability index `CAP-ACP-MULTIHOST-BROKER` 标 `REVIEW_NEEDED`，理由包括 app-server real-host post-fix smoke 尚未完成。

因此不新建项目控制平台，也不把业务队列迁进共享 broker；先在该 broker 现有 `CodexAppServerAdapter`/control surface 中补最小 durable lifecycle 与 steer，再由论文项目 Master ledger 保持篇目成功语义。这里记录的是 proposed work，不是已合并代码。

## 6. 拟议控制面与写入边界

```text
Master / CANONICAL_INTEGRATOR
  ├─ 论文项目调度：AUDIT-INDEX + AUDIT-PROGRESS，唯一拥有项目当前态
  ├─ 每个 Peer-PNN：独立、手动保留的 Git worktree；精确 base OID 与单篇互斥写入集
  └─ 私有 broker system/observer 接口
       └─ Codex App Server child（stdio://，process cwd = worktree）
            └─ 一个 thread per paper；turns 推进页审计与审核/修复阶段
```

职责分层：

- 论文项目 scheduler 决定 PDF/MinerU 输入、Peer ID、prompt、单篇 success criteria、页级 receipt、重试资格与是否 DONE；共享 broker 不决定论文内容或 PAGE PASS/FAIL。
- broker 是唯一 app-server stdio 所有者：System 角色可创建/恢复 thread、prompt/steer/cancel/stop；Observer 仅只读 worker/thread/turn 状态、事件序列与安全摘要；Observer 请求不得进入 model context。
- 一个 Peer 只拥有其论文目录里明确登记的 Markdown、篇级 AUDIT、证据图路径；PDF read-only；不能写根 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、README、MEMORY 或其它 Peer 文件。
- Master 是唯一 canonical integrator；接收 exact candidate OID 后按 `AUDIT-SOP` 做证据与提交审查，根页级进度/篇级索引由 Master 串行更新。Worktree 隔离 index/files，不是文件权限边界。

### 建议保存的最小关联字段

每次派发/启动要能从 `Peer-PNN` 找到完全相同的 task/artifact；至少持久化：

| Owner | 字段 |
|---|---|
| 论文业务 ledger / `AUDIT-PROGRESS` DISPATCH/START | `Peer-ID`、actor、请求的 model/effort、paper short name、PDF SHA-256、MinerU SHA-256、prompt/template version+SHA-256、repo common-dir、branch、绝对 worktree path、base OID、owned paths、`workerId`、Codex `thread.id`、`thread.sessionId`、app-server/CLI version、创建时间。Thread IDs 非 secret，但仅写任务所需信息。 |
| broker 私有 worker state | process PID/argv-safe identity、server cwd、worker/thread/turn ids、last known status、last completed turn、current active turn、事件序号、wire/stderr locator、resume candidate/last reconciliation timestamp。权限维持 0700 目录、0600 文件；不存 access token。 |
| per-page project receipt | 既有格式：实际时间、论文/页码、评级、Peer actor/model/effort、source page commit OID、`candidate_not_integrated` 等状态。Thread ID 可作 DISPATCH/START locator，不用它代替 commit/page evidence。 |

业务 ledger 与 broker 的各自 owner 需在实现时选唯一 canonical record；避免在多个文件复制一整份“当前 worker 状态”。私有 wire 是协议历史 evidence，broker state 是恢复索引，`AUDIT-PROGRESS.log` 是论文页级事件，三者职责不同。Thread/turn id 不足以证明 worktree 内容与 thread history 对应，必须同时核对 repo path、base、PDF/Markdown hash 和 Git状态。

## 7. 建议启动、监控与恢复流程

### 新 Peer

1. Master 在当前 accepted target HEAD 上准备唯一 handoff branch / worktree；先核 common-dir、clean/dirty baseline、精确 `base_oid`、唯一 `Peer-PNN` 和互斥 write set。避免把 Codex-managed disposable worktree 生命周期当作唯一恢复保障。
2. 检查 Worker 当前 Codex CLI/schema、model list 与 supported reasoning efforts；`gpt-6-luna/max` 不用默认值猜。为该 worktree 固定 sandbox writable root，默认关闭不需要的 network，broker 保持 approval default-deny。`agents.enabled=false` 或同等 feature guard 应禁用嵌套 subagent fanout，实际配置需回显/行为验证；40 指顶层 paper Peer，不是每个 Peer 内再派子 Agent。
3. 启动 broker worker 时进程 `cwd`=唯一绝对 worktree；`thread/start.cwd`=同一 worktree；用 `thread/started` response 的真实 `thread.id` 保存，另存 `thread.sessionId` 与 `instructionSources`。不使用 `clientThreadId` 代替 App Server thread id；不把 project task 转成 App Server thread 的结果预设为自动历史迁移。
4. 首个 `turn/start` 显式传入 `cwd`、准确 model/effort、sandbox、approval policy 和一个完整单篇任务 prompt，并记录 `turn.id`。保留 `model/rerouted`、command execution cwd、fileChange 和 `turn/completed.status` 等 event。协议 `completed` 不是 PDF 对照或审计完成。
5. Observer 实时展示 worker/session/turn、pid、last event、命令 cwd、page progress commit 与 broker error；正文/trajectory 默认保持 private，不向所有 observer 广播。Master 对高风险结论通过私有 wire/最终文件/OID 直接核验。
6. 需要调整活动轮次时用 `turn/steer` 并传精确 `expectedTurnId`；如果需要更改 worktree、sandbox 或 model，先 interrupt 并新开后续 turn，不试图在 steer 里修改这些字段。取消后等待终态及进程后置条件。
7. 每页立即使用论文项目既定 audit(page) + commit 规则，commit path 精确、subject 带真实 Peer/model/effort。完成 Markdown 修改仍须全篇 `Edit` 手工修复 + 全文复核；App Server 不改这条业务验收合同。

### App Server / broker 意外退出

```text
detect exact worker PID/socket/wire EOF
  -> freeze worktree (do not remove/reset/reassign)
  -> inspect project and broker durable mapping
  -> thread/read + thread/list(cwd=exact worktree)
  -> reconcile active/last turn, child processes, git status/diff, last page receipt
  -> only then restart server and thread/resume(saved thread.id)
  -> verify instructionSources/CWD/model config, then issue a new turn if warranted
```

关键安全语义：`thread/resume` 恢复已保存的 conversation thread，不等于中断中的子进程或工具动作一定继续；App Server 退出可能和 shell 子进程、文件写入、Git 落盘发生在不同时间点。必须先检查精确 PID/process tree、wire terminal、thread status、`git status`/diff、未跟踪图片与最近 audit(page) commit。若上一轮的副作用不明，状态标 `RECONCILIATION_REQUIRED`，不自动重发整篇 prompt，不并行创建替代 Peer，也不清理工作树。重新派发只能由 Master 在处理完旧 candidate/dirty state 后显式决定。

Broker 重启后如果还找不到 worker map，应由持久恢复记录 + exact `thread.id` 重建，而不是基于 cwd 搜索后不加核验地连接任意 thread。若 `thread/read` 不存在、resume 失败、model/effort不匹配、cwd/hash冲突或 Host状态不明，停止该 Peer 的写操作并保留 worktree；回退到基于 Git/page receipts 的人工恢复。`thread/shellCommand` 官方说明会在 thread sandbox 之外执行 full-access 用户 shell 命令，不纳入通用 system/observer API。

## 8. 安全、质量与容量约束

1. **实验性边界**：`codex app-server` 当前官方标记为 experimental，不把设计文档或单次 smoke 写为 production support。若真实 smoke 不可靠，保留现有项目 Peer task 流程。
2. **工作区边界**：Git worktree 提供独立 working tree/index，不提供 OS sandbox。显式 `sandboxPolicy.workspaceWrite.writableRoots=[exact worktree]`，确认通过 Codex 实际权限配置生效；共享 PDF/MinerU 资料均从本 worktree 读取。原始 PDF read-only，只有论文 owner 文件集可写。
3. **共享状态根**：首个试点先用现有 CODEX_HOME 以便进程重启后能查到同一 thread；确认 2–4 个并发 App Server 进程对 shared CODEX_HOME/SQLite 的稳定性、竞争和日志一致性。不要把每 Peer `CODEX_HOME` 当免费隔离方式，因为 auth/config/skills/sessions 也随之切换。专用 SQLite home、多个服务共用 daemon 属于备选，需单独对照，不先同时引入两种恢复结构。
4. **模型身份**：每次 thread/turn 请求固定 `gpt-6-luna/max`；先查询 App Server `model/list` 支持信息，后检验运行中的模型/effort、warning、`model/rerouted` 和账户 usage。精确目标未确认就不开始论文；不将配置请求或模型名字符串当作运行证据。
5. **防扇出**：Peer 是顶层 session；运行配置关闭 Codex nested multi-agent tools，并保留 PreToolUse transcript-depth guard。40 不能被 child-agent fanout 偷换为更多写者。
6. **控制与保密**：stdio 只由 broker 所有；本机 Unix socket system/observer 分权并按 0600 token 验证。Raw wire、stderr、prompt、model response 保存到受限私有目录，通常输出只列 IDs、状态、长度/计数与 repo artifact locator。状态日志防 prompt/secret 明文泄漏。
7. **并发/资源**：本机 shared broker 默认 `max-workers=32`；改成 40 只放宽项目 broker 限流，不证明 App Server、账户用量、CPU/RAM、磁盘、图像渲染和 JSONL I/O 可承受 40。官方没有在 App Server 页给本机 multi-process 的 numeric cap；需从 1→少量并发→目标 40 分阶段记录 PID、峰值内存、转轮时长、失败/限流与每 Peer 真正处于 active 的 thread 数。现存 project Peer 不能重复计入，也不能把 worktree 数当 active sessions 数。
8. **完整性**：worker 页面评级始终以原 PDF 与现行 `AUDIT-SOP` 判据为准。App Server `turn.status=completed`、`end_turn`、消息数、文件时间戳、线程存在或 Peer 自述都不是论文完成判据。
9. **Worktree 生命周期**：考虑手动 `git worktree` 保留 branch/commit/dirty 状态；本机清理责任由 Master 控制并检查活进程、未提交/未跟踪文件和 commit 可达性。不因 App Server/peer chat archived 而清理候选资产；不要调用 `remove/clean/reset` 清除未审核工作树。

## 9. 分阶段实施与验收建议

本轮授权仅覆盖调查、写方案与只读证据审阅，以下是候选未来验收，不表示已获授权执行。

| 阶段 | 工作 | PASS / 停止条件 |
|---|---|---|
| P0 — source/runtime 归属闭合 | 用户确认所称“续传系统 App Server”具体 Host/Session/运行样本；再核对 Codex CLI 与其完整 tracked/runtime 证据。 | 仍没有 exact App Server run locator 时，继续把旧项目证据标 `ACP_REFERENCE_ONLY` / App Server evidence `UNKNOWN`。 |
| P1 — fake adapter contract | 在 fake app-server 测 `initialize → thread/start → exact id mapping → turn/start/events → steer expectedTurnId → interrupt`；测试错误与 observer ACL。 | 无跨 Peer 写入、错误 IDs 被拒绝；失败证明不夸大真实运行。 |
| P2 — 单 worker harmless smoke | 在明确的 synthetic/disposable Git worktree 中跑一轮，不读写任何论文目录；核 model/max、instructionSources、sandbox/CWD、live event、steer/cancel、process/status。 | `gpt-6-luna/max` 无 reroute/override，权限限定精确路径，保存 thread/turn ID与 raw evidence；失败时不升级。此阶段需启动真实 App Server/model，当前未执行。 |
| P3 — resume/fault smoke | 在 synthetic workspace完成 turn 后退出 App Server，重新启动/initialize，先 `thread/read` 再 `thread/resume(saved thread.id)`；另用受控 marker 工具测试 turn 中断/Server 退出后进程和文件副作用对账。 | 同 thread 可读/续用；不会自动双跑；active/partial child 能确定性停止或被隔离；worktree 内容、thread 与 manifest 对应。若 Host 不提供足够信号，就明确留下 manual-reconciliation barrier。 |
| P4 — 多 worktree concurrency | 2–4 个独立 worktree/thread 同时跑 synthetic tasks；确认 shared `CODEX_HOME`/SQLite、进程监控、distinct model/session/thread IDs、observer 隔离、broker restart 恢复和工作树互斥。 | 无 session/thread 混淆、无 cross-write、无未发现 orphan、每个 process/session 有唯一稳定 locator；资源使用可观察且失败可恢复。 |
| P5 — 40 Peer qualification | 在当前业务调度器下实际启动 40 个 unique top-level Peer/App Server turns；保持 single integrator，保留回执；分批进入 40 不取消 40 的验收目标。 | 40 个真实 active turn/session 有 host/runtime 证据，模型与 effort 核准，worker/worktree/输入 hashes 唯一，资源和限流可接受；否则报告实际数值和具体失败证据，不把 40 worktree 或 createThread acceptance 写成 40 active。 |

每一阶段保留 exact CLI/server/schema version、配置、prompt/template hash、worktree base OID、stderr/raw wire receipt、PID/CWD/thread/turn ids、status 与实际 command。所有实测均在 synthetic worktree；只有 P5 用户明确允许正式切换之后，才可将新 App Server 方式绑定论文任务。若 P2–P4 不通过，止于设计/实现候选，不继续扩至 40。

## 10. 兼容现有 Peer 派单与回退

- 当前 Codex Project Peer `clientThreadId` 是 App 创建接口的 provisional identity；它不是 Codex App Server 的 `thread.id`。App Server 新 thread 不自动导入旧 project Peer 的 prompt、turn 或 thread 历史。
- P41–P65 和 P37/P40 等旧控制面任务，在用户未决定迁移前继续按其自身 formal thread/worktree/page receipt 对账；禁止另开一条同篇 App Server worker 来“补位”。若将一篇在途任务迁移，Master 先取得原 task status/worktree exact base/dirty diff/last page commit，再交接到唯一新 thread，保留旧候选和身份历史，不能抹掉或把两边进度相加。
- 迁移前后均适用 R-002/R-003 actor 语义：Master/Peer ID唯一、模型/effort如实留痕、Master唯一集成者。Codex Project 与 App Server protocol 的 IDs 不互换；任何 task/thread identity alias 都必须以明确 mapping receipt 为准。
- App Server 出错时不取消整个论文队列：停止向受影响 Peer 再送 turn，保存 worktree/raw evidence；由 Master按当前 Git/SOP 人工恢复，或在明确关闭/提交后从安全新 worktree按业务 state 重新派发。共享 broker 不创建自己的纸篇完成状态。

## 11. 开放决策、停止条件与来源

### 尚未闭合的问题

1. 用户所忆 App Server 的准确 Host/项目内 session/task/run id 是什么？本次 shuxuedashi repo 的 tracked evidence 是 ACP 运行，不是 Codex App Server；该差异仍需用户给具体历史 locator 才能追溯。
2. 当前 Codex CLI `0.157.0` 对目标账号支持 `gpt-6-luna/max` 吗？`model/list` 和真实无害 turn 回显是什么？本轮未运行。
3. 40 个独立 App Server 进程在 shared `CODEX_HOME`/SQLite 下是否安全、可恢复、可用？无本机并发 smoke；官方资料无数字保证。
4. Worker 文档的 model/effort、tool catalog、instruction sources、sandbox roots 是否在 `thread/resume` 后恢复并能核对？需要 exact runtime evidence。
5. App Server 进程退出时由 Codex 子工具启动的 shell/renderer 存活、继续/停止和文件落盘的实际故障语义是什么？目前只可按需 fault-inject，不假定 resume 可恢复子进程。

### 主要复核入口

- 论文项目 current requirements: `feature-list.md#AUDIT-002`; original concurrency ruling: `rulings.md#R-003`; audit process: `AUDIT-SOP.md#AI-身份与并行Worktree日志`。
- 用户指定的续传 repo: `/Users/aurolafly/shuxuedashi-analysis-system/AGENTS.md`, `README.md`, `src/v2_pipeline.py`, `dev-docs/042-ACP双后端基线复验报告.md`, `043-ACP内容完整性三路实验报告.md`, `045-双管线执行后端架构设计.md`, `046-OpenCode-ACP管线详细设计.md`, `062-OpenCode-Key池与ACP实例生命周期规范.md`。
- Shared broker: `/Users/aurolafly/codex/tools/agent_session_broker.py`; tests: `/Users/aurolafly/codex/tests/test_agent_session_tools.py`; capability status: `/Users/aurolafly/skills-devin/CAPABILITY_INDEX.md#CAP-ACP-MULTIHOST-BROKER`。
- Current official product contract, accessed 2026-10-02: [Codex App Server API](https://learn.chatgpt.com/docs/app-server); [Codex `CODEX_HOME` / state roots](https://learn.chatgpt.com/docs/config-file/environment-variables); [Codex configuration sample, including multi-agent defaults](https://learn.chatgpt.com/docs/config-file/config-sample); [Codex SDK vs App Server guidance](https://learn.chatgpt.com/docs/codex-sdk).

**复审触发**：用户提供 App Server 运行 locator；shared broker real-host smoke changes to verified; local Codex CLI/schema/model/config changes; concurrent process state/capacity test results; current project R-003 or dispatch ledger changes. 在这些证据出现前，本文件保持 DRAFT_PROPOSAL，实际 App Server 适用性与 40 并发容量保持 `NOT_VERIFIED`。
