# MEMORY.md：Collected-Papers-of-Fields-Medalists 持久记忆

## 当前状态

本仓库收录菲尔兹奖得主获奖相关论文、会议论文和颁奖材料，并维护 MinerU 衍生文本及逐页审计记录；详细资产地图见 README.md。截至 2026-10-02 的旧 Peer 冻结点，`AUDIT-INDEX.md` 有 138 条记录：102 篇完成、6 篇“审计证据已收割但未完成”、28 篇“冻结无候选”、1 篇 PDF↔MinerU 映射阻塞（P37）和 1 篇冻结保全但未集成（P40）。所有此前启动的 Peer 已由用户声明停止；本机可见 16 个 Git worktree（含 main），且限定的进程检查未见独立旧 Peer Codex App Server/broker。Master 没有删除、archive、clean 或 reset 任何旧 worktree。P01–P40 的 28 个完整候选、6 个未完成证据候选以及更早的 Witten/Deng/Drinfeld 候选均已按 exact source/base/path/merge 预检收割到 main；完整分类、OID 和未提交资产边界见 `dev-docs/002-2026-10-02-旧Peer批次冻结与收割收据.md`。全仓仍有 141 个 PDF 路径、139 个 distinct PDF byte streams，与 AUDIT-INDEX 的 138 行口径不一致，尚未闭合。

项目治理骨架已于 2026-10-01 建立。用户新增的剩余 MinerU Markdown 正文逐处 Edit 规则已记录于 `rulings.md#R-001`，并路由到 `AGENTS.md` 与当前 `ZCODE-HANDOFF-PROMPT.md` §5；R-005 的确认 Gate 优先于任何 MinerU/论文动作。MinerU Skill 的最近检查快照为 2026-10-01：本地 MinerU 4.0.8 CLI 可执行，library server 当时停止、standard 所需 GGUF 模型缺失；每个缺失导出的未来 worker 必须在用户确认后重新只读核对当前运行时，只可用已就绪的本地资源，不能启停服务、下载模型、改配置或远程上传。

## 当前执行队列

| 方向 | 状态 | 下一步 | 相关 Feature |
|---|---|---|---|
| 旧 Peer 冻结与收割 | COMPLETE | 29 个 P01–P40 完整成果（含既有 P03）及 Witten/Deng/Drinfeld 已完整纳入 main；6 个未完成候选的审计证据已收割；P10/P12/P30/P41–P65 无候选，P37 映射阻塞，P40 方法范围 hold。 | AUDIT-002、R-004、R-005 |
| ZCode 接管确认 Gate | WAITING_FOR_USER_CONFIRMATION；未启动 | ZCode 先只读恢复当前真值并向用户提交机制/范围/模型/agent 数/worktree/写入集/停止方案。用户明确确认后，才可选择 App Server 或 ZCode 原生 Sub Agent；两条路线均不得自动启动。 | AUDIT-002、R-005、ZCODE-HANDOFF-PROMPT.md |
| 未完成论文的继续审计/修复 | PAUSED_BY_USER | 仅在用户之后明确确认目标 scope；若选 App Server，先确认并完成非论文控制层资格化，再另行确认论文 worker；若选 ZCode Sub Agent，确认 exact agent envelope 后才从 P17/P19/P27/P31/P32/P34、P37、P40 的记录断点继续。 | AUDIT-001、AUDIT-002、R-005 |

## 当前开放问题与阻塞（冻结后）

- P37 的 `Birkar_2016_fano_flips` 仍为唯一 PDF↔MinerU 映射阻塞：93 页 PDF 是 Caucher Birkar `arXiv:1603.05765v4`，同名 Markdown 却是 Keshvari 生产率论文。错误 bundle 原样保留；以后先生成并核验正确导出，不能改名冒充。
- P17、P19、P27、P31、P32、P34 的已收割审计实物均不等于论文完成；各自缺口和 exact OID 在冻结收据 002 与 AUDIT-INDEX 中。P40 只有 p.1–p.118/127 且证据方法范围冲突未闭合，仍不得计完成。
- P39、P34、P27 的停止 worktree 留有未提交但未被 committed AUDIT 引用的 300dpi 图；它们保留在原路径，未纳入主线，采用前需重新建立其页级来源关系。
- PDF 路径数 141、distinct byte streams 139、AUDIT-INDEX 138 行的口径差仍未闭合；不得用本次完成数推出全范围覆盖。
- R-005 将项目交接给 ZCode，并允许用户确认后选择 App Server 或 ZCode 原生 Sub Agent。两条路线均是 `NOT_RUNTIME_VERIFIED`；确认前连控制层 pilot 也不得启动。若选 App Server，shared broker 的 real-host resume/steer/restart 与 shared `CODEX_HOME` 并发仍需资格化；若选 Sub Agent，ZCode 当前 runtime 的实际 profile/隔离/递归边界仍需核验。
- MinerU library server 的旧停止状态不是自动启动许可；任何未来新解析仍须按 MinerU skill 的质量、隐私和运行边界核定。

## 2026-10-04 批次更新（ZCode 接管后 · 总攻 run）

本节覆盖上文「当前状态」所锚的 2026-10-02 冻结点之后、截至 2026-10-04 的真实变化。上文的冻结点叙述作为历史保留，不再是当前态。

**R-005 确认 Gate 已由用户解除**：用户以「全部搞完，一个都不放过」授权 workflow 总攻，并要求子代理用 GLM-5.3 Flash with Max Thinking、并发上限 50、双层 Master（会话 Master + 常驻 `Wf-Master` 协调者）。旧 batch 的 worktree/clientThreadId 一律不得当作仍在运行的 App Server session。

**已完成并收割进 main（本批次）**：
- `ribet1990` 47/47（merge `314cbf83`）
- `Deng_2018_strichartz` 34/34（merge `4fa791fd`）
- `Scholze_2012_perfectoid_published` 69/69（merge `897bee3d`，根级登记 `7c858f1f`）——全篇逐页审计完成；收尾复核另新发现并闭合 2 个此前未捕获的缺陷类（étale site 下标尖音符 23 处、math 段末多余右花括号 2 处，后者经 `git show HEAD:` 证实存在于 MinerU 原始导出）。

**当前首要阻塞：Z.AI 配额**。总攻 run 以 `stop_reason=provider` 停止，code 1310（individual-coding-plan 周/月额度耗尽），**2026-10-07 10:33 重置**。续跑改用 `zai-offpeak-idle-plan` 后实测 41 个 turn 全部在 4 秒内失败、零 token，该账户不可执行。恢复后续跑须**先做单 worker 冒烟验证账户**，再从 `dev-docs/003` 的逐篇断点账本继续。

**次要阻塞：MinerU 云端导出**。用户已授权 `--remote`；实测上传与解析成功，但结果下载主机 `cdn-mineru.openxlab.org.cn` 的证书 `notAfter=2026-10-02 23:59:59 UTC` 已过期约 2 天，TLS 握手失败，9 次重试全败。本地兜底不可用（`parse_server.local.mode=disabled`）；`--tier flash` 可跑但公式全为 `![] Formula block` 占位符、无 LaTeX，按 skill 规定不得作最终阅读质量。**未关闭 TLS 校验、未配 API Key、未启停 daemon、未改写任何目标 Markdown。** 已落盘 `dev-docs/004` 并设每 2 小时自愈 cron。受影响：9 篇导出（P30 70p、P37 93p、P59–P65，1649 页），其中 P30/P37 经实测为**导出错配**（实为 ArnLind–Hoppe–Huisken / Keshvari 论文），证书恢复后须重导并按既有 AUDIT 锚点重审。

**未闭合的技术债（本篇）**：Scholze MD 尚余 30 个 `0x0b` 控制字节，字形已 300dpi 定案为 `ϖ`，位置、行号、PDF 页与修复形态（13 DEL / 17 INS）均已逐处登记在 AUDIT「控制字节总账」。根因经本轮实测订正为 **Edit 参数通道的「定位」限制而非「表达」限制**——六类共 22 字节与 8 个 `0x0b` 已成功经 Edit 清除；卡点在于 Read 把 U+000B 渲染为不可见字符，回抄的锚点少一字节而无法逐字匹配。恢复条件：能在 Edit 参数中稳定写出字面 U+000B。

## 冻结前历史开放问题与阻塞（不作为当前执行队列）

- P37 的 `Birkar_2016_fano_flips` 前置映射失败：93 页 PDF 首页确为 Caucher Birkar 的 `arXiv:1603.05765v4`，而唯一同名 MinerU Markdown 是 Abolfazl Keshvari 的生产率分析论文。P37 0/93、worktree 论文文件未改；等待用户向 P37 task 发送新提示词。正确 MinerU 导出应先在独立路径生成/核验，不能改名冒充或覆盖当前错配 bundle。
- `AUDIT-001` 的 Edit 修复行为尚未验证：p.4–5 已发现待修 OCR 差异，按全篇审计完成前不改 Markdown；之后须逐处手改并复读全文。
- Drinfeld main 分支仍登记 5/32：p.1–3 PASS±、p.4–5 FAIL；worker worktree 已提交 p.1–32 审计、修复和澄清 commits，最新观察 HEAD 为 `f46300d1`，但最终修复后的全文回读/修复登记尚未由 Master 直接核实，候选仍未集成，Master 未编辑论文。
- MinerU library server 当前停止；不得因 `server_not_running` 自动启动，后续若需新解析须先按 skill 的质量/隐私边界处理。现有 Markdown 可供逐页审阅。
- 用户明确 Master 不再执行逐页初审；最新指令 supersede 先前“等三个任务结束再讨论扩容”的暂缓要求。Master 负责调度、只读质量复核、共享文件集成与验收，不替 worker 初审或改论文。
- 用户明确 Master-Luna 与各 Peer 使用唯一 actor ID，并在篇级 AUDIT、页级工作日志和 Git commit subject 中写明 actor/model/effort；历史 GLM 处理不回填或改写。当前 Master 身份为 `Master-Luna | gpt-6-luna/max`。
- 现有可验证 Peer 候选为 Witten `bc4605dc`、Deng `3e5e964b`；Drinfeld worker 候选 `f46300d1` 正处于修复/总复核阶段。Witten/Deng worktree 已消失但 commit 对象仍可读，正式 thread ID 未从 app 列表发现；集成前必须核 exact paths/base。
- P01–P09 分别由独立 worktree 从 `e04c4a96` 起步，并已出现带 Peer ID/model/effort 的逐页提交；P10–P39 分别从 `03760242` 起步。Codex app 的 create_thread 返回 30 个 `clientThreadId`，正式 `threadId` 仍未在 list_threads 中显示，不能将 client ID 传给 wait/read/message；依托共享 Git worktree 做只读监测。P01 Deligne 候选 HEAD `9857d0ccb8d2d54cc3d1298e8d7c389242478d17` 的 AUDIT p.6–p.22（包含 p.12）均缺显式 PASS/PASS±/FAIL 行，p.23 有结果行；主线 17:33 REVIEW 更正了先前误称 p.12 有结果的复核记录。相关页及本篇均不得据此视为通过或集成完成。
- 当前唯一篇目总数的证据口径仍未闭合：PDF 实物数量、SHA-256 distinct byte streams 数与 AUDIT-INDEX 声明的 140 行口径不一致。完成全范围声明前须逐文件交叉核对目录、重复副本、篇级索引与已存在 AUDIT 候选，不将少看/多算的资产默默排除。
- 官方 Codex 文档确认项目 task/worktree 并行工作模式，但未发现该 app task 入口的数字并发上限；API multi-agent 默认并发配置不同，不能当作 app project peer cap。40 是用户本轮的最低操作目标，不是平台保证值。
- 当前 Codex 任务列表只暴露 Master 任务，Peer 的正式 threadId/status 仍不可见；worktree 数量不证明同数 Session 此刻都在运行。P40 创建请求返回 provisional clientThreadId 且新 worktree 已出现；不能把 client ID 用于 wait/read/message，也不能将 worktree 存在说成 turn 已启动。P40 的实际 model/effort 状态仍待运行时证据确认。
- 当前新分派为 2026 Hong Wang/Zahl Kakeya；PDF 127 页、MinerU Markdown 存在、未见对应 AUDIT/Index/page-progress 记录。其他未分派 PDF 的完整交叉核对仍待继续；不得复用旧摘要中的“Viazovska dim24”候选，因为当前 AUDIT-INDEX 第 33 行已登记该 17 页篇为完成。
- Codex CLI App Server 被作为未来 Peer 控制方式调查，当前仅为 `DRAFT_PROPOSAL`（见 `dev-docs/001-2026-10-02-Codex-App-Server并发Peer工作流调查与试点方案.md`）。续传解题系统现存、可复核的流式运行证据是 OpenCode/Devin ACP；在其 tracked 当前实现与已查 Git 历史中未找到 Codex CLI `app-server` 接线，用户所指的 App Server 运行实例仍待定位。共享 `agent_session_broker.py` 已有 Codex app-server facade，但当前能力索引为 `REVIEW_NEEDED`，缺 resume/steer/启动后 worker-session 恢复和真实 Host smoke。未启动服务器/model；不迁移或重复派发现有 project Peer；R-003 的 40 个顶层 Peer 要求不变。

## 当前有效约束摘要

- 剩余 MinerU Markdown 正文修复须使用 `Edit` 逐处手工编辑，脚本只做人工修复后的只读终验/清点；详细规则见 `AGENTS.md`，ZCode 接管后的业务合同见 `ZCODE-HANDOFF-PROMPT.md` §5（但当前仍在确认 Gate，尚未授权执行）。
- `AUDIT-INDEX.md` 是篇级进度唯一真值，`AUDIT-PROGRESS.log` 是页级恢复点；历史 handoff 快照不覆盖这两个 owner。

## 开放事故

- 当前无已确认 `OPEN_INCIDENT`。

## 已关闭事故注册表

实际记录的 `status` 必须是 `CLOSED_INCIDENT`；空表不编造事故。

| ID | status | closed_at | closure evidence | still-valid lesson | reopen_if | current route |
|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - |

## 已验证事实

- 当前 `AUDIT-INDEX.md` 有 138 条记录，其中 102 条标为完成；完成/部分/冻结分类与 exact source/integration OID 已由冻结收据 002 交叉记录。该统计仍不解决 PDF 路径/unique-byte-stream/索引行数的总量冲突。
- `/Users/aurolafly/.codex/skills/mineru/SKILL.md` 通过 `quick_validate.py`；该结构校验不证明 MinerU 解析质量或本项目页面审计已通过。
- bootstrap layout validator 报告治理入口布局完整；这不证明 `AUDIT-001` 的未来行为已验证。

## 研究与工作日志

### E001 · 2026-10-01 · 建立治理骨架并记录手工修复要求

- 新增项目级认知入口与唯一要求路由，记录 `Edit` 逐处修复、脚本只读终验和 AI 全文复核要求。
- 验收本轮没有处理论文；篇级计数保持 70/140，真实执行行为留待未来合规篇目验证。

### E002 · 2026-10-01 · 配置 Codex MinerU 入口并恢复逐页审计队列

- 复核 ZCode Session `sess_dc635a68-9c5c-40c1-9fda-f2bee682a468`：其最后一 turn 因 ZCode 5 小时用量上限中断在 handoff 文件基线检查后；当前 repo 的 R-001/§2.4 规则已由后续工作写入，本条只把未入索引候选的登记步骤补入 §5。
- 将现存 MinerU CLI 绑定为 Codex 全局 skill；版本、模型状态和服务状态均做了只读核验，没有运行新解析、启动服务、下载模型或远程上传。
- 将 Drinfeld 32 页以 5/32 登记并追加 START、p.1–3 PASS±、p.4–5 FAIL；确认并记录 p.4–5 OCR 差异及印刷内部矛盾；Markdown 尚未修改。

### E003 · 2026-10-01 · 并发论文处理方案评估

- 已核对 Witten 1982（32 页）与 Deng 2018 Strichartz（34 页）均有干净的 PDF 与 MinerU Markdown，可作为 Drinfeld 之后的独立候选。
- 用户批准 Witten/Deng 两个 GPT‑6 Luna/Max worktree 后又要求 Master 不再做论文初审，因此新增 Drinfeld p.6–32 续办 peer。三项 worktree 均已实际推进；Master 持续只读审计过程和结果，不新增 peer，待三项完成后再评估扩容。

### E004 · 2026-10-01 · Peer Worker 连续质量审计

- 用户明确授权 Master 在三项任务执行期间持续审计 worker 结果；Master 负责调度、只读质量复核、共享文件集成和验收，不代替 worker 做首次逐页审阅或修改论文。
- Witten worker 于候选提交 bc4605dc 报告 32/32 页审计完成，AUDIT 文件有 32 个页面条目、32 张 150dpi 全页图、24 张 300dpi 局部图，并声明最终修订后完整复读 Markdown；改动路径仅在 Witten 目录，worktree 当前干净。Master 已抽核 p.31 ref [2]、p.7 Taylor 余项和 p.15 Morse 指数，均与裁片一致。修复表登记 p.1/p.4 commit 8219e7a9，先前的未登记疑虑已解除。仍有可见 SOP 偏差：内容级修复提交穿插在全篇审阅结束前；另 p.22 的签名/图片记录在同时涉及 p.17/p.22 的 audit(evidence) 提交中，没有独立 p.22 audit(page) 提交。候选尚未集成到根级索引/进度，正式 task 终态也未在 list_threads 显示。
- Drinfeld p.16 的 AUDIT 条目称印刷 X_I、Markdown X_r；将其 300dpi 原页与 p.2 已明确的 X_I 字形并置后，p.16 印字更像小写 r，故暂列 possible false positive / print quirk，待 worker 重新裁决。p.32 审计把 Received 17/DEC/73 列为 Markdown 漏录，但 Git 基线和当前 Markdown 都已有该行、源页也印有；该差异是确定误报。p.32 的 Translated by M. B. NATHANSON 确实缺失。另抽核 p.25 的 𝔄_f^* / 𝔘_f^* 差异，300dpi 页图支持 worker 所记的字形差异。
- Deng worker 的候选审计/修复现已提交且 worktree 干净：基线审计及 34 页逐页对账表在 32f9f43d，Markdown 修复为独立提交 89626f5b0d57ceddef0b8ba12a8fc42519bf8c8c，最终修复后 PASS/全文复读报告及 fix OID 收据在 3e5e964bf50dd41e0ac2c31699a5746d292a616e。报告记载 1,783 行全文回读、修复后最终 SHA-256 60f572494701abc6fe95882c753a3b0f86660a98f866cc7767d8a25d8910dd1b；Master 抽核 p.1 题名和 p.10 标签与印刷相符。候选仍未集成；34 页审计汇总集中一笔 audit commit，仍有每页密集提交的 SOP 偏差。
- 根 AUDIT-PROGRESS.log 仍停在 main 上的 Drinfeld p.5；worker branch-local 页签尚未进入共享恢复日志。三个 peer 的正式 thread ID 也仍未在 list_threads 中可见，当前只能以 worktree 状态/提交做只读监测。
- 用户要求等待三个 peer 全部结束、审阅结果后再讨论并发扩容，明确不要现在启动 10 个；滑动窗口/10 个上限均未被采纳或验证。

### E005 · 2026-10-01 · 扩容至 40 个 Peer 并登记 actor

- 新的用户指令将当前并发目标提高到 40 个 Peer，覆盖并取代 E004 末尾的暂缓扩容状态；Master-Luna 仍只负责调度、只读审计、根级记录和集成。
- `e04c4a96` 注册并分派 P01–P09，`3dfa4a64` 记录其 dispatch；`03760242` 建立路径级互斥规则并注册 P10–P39，`e864b3b9` 记录第二批 dispatch。最新只读 `git worktree list` 共 41 个 checkout（main + 40 Peer）。P01–P09 已产生 page commit；P10–P39 的工作树正在初始化/启动，截至当前快照其中至少 8 个可见论文路径文件变化。
- create_thread 为新批次返回 `clientThreadId` 而非 formal `threadId`；list_threads 尚未列出这些任务。不要把 client ID 用于 thread 读写/等待；当前用精确 worktree、提交、AUDIT 证据监控。以后的任务按页数队列滚动补位，仍待处理的首项/可恢复项以 AUDIT-INDEX、PDF 清单与 MinerU 导出实物核定。
- 40 是用户要求的 Worker 并发数，不是官方平台能力上限声明；官方 Codex app 的公开并行任务/worktree材料未发现数值上限。

### E006 · 2026-10-01 · 40 Peer worktree 与页级收据复核

- 40 个 Peer worktree 已在同一 repo common-dir 中可见；P01–P09 产生了 156 个逐页 audit commits，P10–P39 已创建 30 个独立 worktree 任务（create_thread 返回 clientThreadId，正式 threadId 尚未显示）。Master 没有编辑论文，只读检查任务范围、分支提交和篇级 AUDIT。
- Master 在 `e10cd162` 将 P01–P09 已提交页签作为候选进度写入 `AUDIT-PROGRESS.log`，每行带 Peer/model/effort/source OID 并标成 candidate-not-integrated。身份抽查确认 Git subjects 带正确 Peer ID；但 P01 Deligne 的 AUDIT p.6–p.11 缺显式结果字段，尽管相应 page commits 带 FAIL；已标注审计记录不完整，等待后续用户授权/正式任务通信或候选最终回执，不做静默更改。
- 当前尚未把任何 Witten/Deng/Drinfeld/新 Peer 论文目录候选集成至 main；AUDIT-INDEX 的 40 个“审计中”分配项不等于 40 篇完成。

### E007 · 2026-10-01 · 扩展 candidate page 收据监测

- 在 `eca58d6f` 的 156 条 P01–P09 page receipt 后，Master 又从 40 个 worktree 收录了 376 条新提交收据；包括 Drinfeld 旧 Peer p.6–p.32（actor ID 未在启动时分配，故明确记 `UNKNOWN_LEGACY_DRINFELD`；model/effort 来自该任务的既有配置）。全部记录带 source OID 且为 candidate-not-integrated，不改论文内容。
- 截至该快照，40 个工作树中 36 个至少已有一笔 page commit；P10、P12、P30、P37 尚未出现 page commit。P01 Deligne p.6–p.11 的审计结果行仍未写入；需要正式任务回执/用户授权沟通或候选修复后再重新审查，Master 未修改其文件。

### E008 · 2026-10-01 · 校验 PDF 重复副本与篇目总数口径

- 只读对 141 个 PDF 路径逐一执行 SHA-256，发现两个重复组：`2010年 - Smirnov/Duminil-Copin_Smirnov_2010_honeycomb.pdf` 与 `2022年 - Duminil-Copin/Duminil-Copin_Smirnov_2010_honeycomb.pdf`（`11335571f5118514b5f761ad3d750e11b5537b1390aa3444742339b86e65bb8a`）；`2010年 - Smirnov/Smirnov_2010_conformal_invariance.pdf` 与 `2022年 - Duminil-Copin/Smirnov_2010_conformal_invariance.pdf`（`dfc298f2b1b7bd5b26bb5dfa2a3ed3c25e27248924c2703711c69cbd19194cc5`）。因此 distinct PDF byte streams 为 139，而旧 Index/header 数字为 140；还需判明统计范围/文档项口径，不覆盖或改写既有 140 声明。
- P10–P39 当前队列只审计每组内容一个 canonical source；重复副本不重复跑页审计，但需在最终完整盘点中确认其消费者/目录归属。

### E009 · 2026-10-01 · 40 Peer 并发持续监测与候选收据复核

- 重查 OpenAI 官方 Codex app 资料：支持并行 project threads/worktrees，但没有找到该项目任务入口的数值并发上限；Agents API 的 subagent 并发配置是不同机制，不能代替 Codex app Peer 上限。按用户 R-003 继续维持 40 个 Peer worktree 槽位。
- 直接 `git worktree list` 观察为 main + 40 Peer checkout。36/40 Peer worktrees 至少有一笔 `audit(page)` commit；P10、P12、P30、P37 尚无页级 commit。该事实是 checkout/commit 证据，不证明对应 Session 仍 active 或 terminal。`list_threads` 返回本 Master task，但未返回 Peer 正式 threadId；当前不安全地重复启动同篇替代任务，也不把 clientThreadId 传给 wait/read/message。
- 本轮从 Peer 工作树按各自共同 base 扫描并发现 372 条此前未写入主线的标准 `audit(page)` commit 收据，覆盖 32 个 Peer actor、时间段 2026-10-01 16:43–17:32 EDT；另识别 3 条不应重复记作标准 PAGE 的提交（Drinfeld p.31 说明性提交、Donaldson p.13 supplement 已在既有 PAGE 收据引用、Donaldson p.10 supplement 作为等级修订单独记录）。对这 372 条页级候选的 992 个 changed-path 记录核对未发现根级 current-owner 路径或跨 Peer 文件路径碰撞。主线进度追加和修订记录提交为 `3845fb56`；候选仍未集成，路径检查不等于纸面内容验收。
- Donaldson p.10 的原候选 PAGE `3e42f4d8` 记录 PASS±；Peer-P03 的补充提交 `0832a3b3` 把候选等级改为 FAIL，称 300dpi 裁片显示 Markdown `0(ε)` 与印刷 `O(ε)` 不同。根日志已记为 `PAGE-REVISION`；Master 尚未独立核对原页图，不接受或集成该结论。
- Deligne Peer-P01 当前候选 HEAD `9857d0ccb8d2d54cc3d1298e8d7c389242478d17` 中，p.6–p.22 页面说明缺显式结果行，p.23 已写结果。Master 在主线追加 REVIEW 更正，明确包括 p.12 的既有判断有误；未改 Peer 论文文件。
- 新一轮用户消息重申“立即开启40并发”，没有改变 R-003 的目标值。当前已证明 40 个 Peer worktrees 存在且持续有候选提交，但 40 个并行 Session 的精确活动数仍 `UNKNOWN`；不把 worktree count 或部分 actors 的近期提交外推为 40 active sessions。

### E010 · 2026-10-01 · 集成 Donaldson 候选并重审下一分派项

- Peer-P03 Donaldson 候选 exact source `93f5cdcbbfea6a708d5b7186ee1d6baeb16b8c0a` 从 `e04c4a9603818cfa2d71271942f696115783c33b` 分支；变更仅在 Donaldson 目录。Master核验 AUDIT 有 38/38 个逐页结果行和 27 项修复登记；Peer 报告称 66 个引用图片路径均有效、38 张全页 PNG 齐全（Master 未逐项重算）。报告所记完整 1,449 行 Markdown 复读后 SHA-256 为 `a22812e11e24ebbddde35767b454a47957949df592d97b72a689568b83eb74a5`，实物匹配；PDF SHA-256 也与报告一致。独立 spot-check p.10 的 300dpi 裁片与修复后的 `O(ε)` 一致。本次是基于完整 Peer 报告、哈希、隔离路径和有限原页抽核的 Master 接纳，不是 Master 重做 38 页审计。
- 候选经 Master merge 集成为 `8713f2fcfbfaa30443b754d0f012a2cb8fe77350`；AUDIT-INDEX 从 70/40 更新至 71 完成/39 审计中，README 仅新增 Donaldson AUDIT 文件资产行，AUDIT-PROGRESS 追加 REVIEW/DONE/COMMIT。README 里用户已有的治理入口改动继续保持未暂存、未提交。
- 重新核对下一候选时发现旧工作记忆里的 Viazovska dim24 17 页篇并非未分派：`AUDIT-INDEX.md` 第 33 行明确登记为完成。该候选从当前派单队列退休；先完成新的物理 PDF—篇级索引—AUDIT/Markdown 对账，再决定 Peer-P40 负责哪一篇。
- P03 完成稿提供一个可回收的纸篇 worker lane；但 Codex app 仍未暴露该 Peer 的正式 threadId/终态。worktree 清洁与最终集成是已观察的交付证据，不等于 Host 返回了 task terminal receipt；新分派路径必须互斥，不冒充已验证的会话关闭。

### E011 · 2026-10-01 · 分派 Peer-P40 至 Hong Wang/Zahl 127 页论文

- 直接核对 README 用户纳入范围、原 PDF 与 MinerU 导出：PDF 为 `2026年 - Hong Wang/Wang_Zahl_2025_kakeya_dim3.pdf`，127 页、SHA-256 `631e8b2118e3d03ded2d5fe79f9acdf74353877d143e9887a3c31278cd13ed01`；现有 Markdown 为 `Wang_Zahl_2025_kakeya_dim3_mineru/Wang_Zahl_2025_kakeya_dim3__Wang_Zahl_2025_kakeya_dim3.md`。在当前 main 的 AUDIT-INDEX、AUDIT-PROGRESS 和目录内未发现该论文的审计记录。
- `create_thread` 接受 P40 project task，并返回 provisional `clientThreadId=client-new-thread:f75d4b98-f061-4f9d-95ad-705fba4ad6d7`；其 worktree `716d` 已出现，HEAD 精确等于创建前 main `57d314dbffc2c61f5351e44e6a3fd6793229414f`，初始化时干净；后续观察到未提交 AUDIT 与 p.1 PNG 草稿。正式 threadId/list_threads 仍未出现，故不声称 Host 返回了 active/terminal 状态。
- 显式 `thinking="max"` 与 `model="gpt-6-luna"` 的 create_thread 组合被工具拒绝；本机配置只读核查显示默认 `model="gpt-6-luna"`、`model_reasoning_effort="max"`。因此 P40 创建时指定 model、未传 thinking override 以继承该已核默认值；任务 prompt 要求 Worker 开始前核实实际配置，不匹配即停止。运行时模型/effort 尚未确认，未静默降级到其他模型/effort。
- AUDIT-INDEX 现为 111 行记录、71 篇完成、40 篇审计中；P40 具体 write set 是独占 Hong Wang 论文 Markdown、AUDIT 报告和带唯一短名前缀的 audit 图片。P40 的 Master DISPATCH 与 REVIEW 记录将与本工作单元其他 canonical 更新一并提交。
- Master 对 P40 p.1 草稿的只读图像核验确认 PDF 印刷为 “Hausdorff”，MinerU Markdown 写成 “Hausdorf”；但该页图像为 1275×1650 8-bit RGB，而现行 AUDIT-SOP 要求 150dpi pngmono 1-bit。该页尚无 audit(page) commit/signoff；正式 threadId 不可见，Master 不能向 provisional clientThreadId 发送纠正。
### E012 · 2026-10-01 · P40 页级候选持续审计与进度收据恢复

- 从 41 个 Peer worktree 的 exact base/history 扫描，发现 38 条此前未投影到根日志的标准 audit(page) commits（覆盖 24 个 Peer actor，时间 20:59–21:48 EDT）；该切片有 99 个 changed-path 记录、86 个 distinct paths，无根级 owner 写入或跨 Peer 路径冲突。Master 将保留 exact source OID、actor/model/effort 并标 candidate_not_integrated。
- P40 已提交 p.1–p.51 页级候选，p.52 image/AUDIT 为未提交草稿；提交 subject/AUDIT 行标 Peer-P40/gpt-6-luna/max，但正式 threadId/status 未显示。
- p.1–p.17 图片为 8-bit RGB；AUDIT-SOP 的通用 pngmono 条款与 ZCODE-HANDOFF 的 born-digital 文本层主对账/PNG 抽验路线存在方法范围疑问。Master 保留该冲突、不接纳候选、不通过 clientThreadId steering。p.1 报告把 Hausdorf→Hausdorff 记为单处 PASS±，而 Markdown 搜索发现至少 5 处；全篇修复后须逐处复核。
- Peer-P03 Donaldson 已在 8713f2fc 集成；Peer-P40 target 为 Hong Wang/Zahl。其余论文继续按精确候选、纸篇隔离和串行 Master 集成推进。
### E014 · 2026-10-01 · Peer 候选页签持续收据与 P40 审计方法复核

- 从 41 个 Peer worktree 按各自精确 base 对账，本批找到 76 条先前未写入根日志的标准 audit(page) commits，覆盖 24 个 Peer actor，commit 时间 21:52–23:30 EDT。对应 204 条 changed-path 记录、152 个 unique paths（以路径审计原始 receipt 为准），未发现根级 current-owner 路径或跨 Peer 文件碰撞。根日志逐条保存 full source OID，仍标 candidate_not_integrated。
- P40 已提交 p.1–p.21，p.22 图像/报告为未提交草稿；Git subjects 标 Peer-P40/gpt-6-luna/max。正式 threadId/status 仍不可见，不能向 provisional clientThreadId 发消息或调用 wait/read。
- P40 p.1–p.21 的页图为 8-bit RGB；现行 AUDIT-SOP 逐页流程指定 pngmono 1-bit，而 ZCODE-HANDOFF 对 born-digital 论文规定文本层主对账与 PNG 抽验。AGENTS 将逐页审计方法路由给 AUDIT-SOP，因此Master保持“模式范围未闭合/候选暂不接受”审计状态，不自行改治理文件或论文。
- P40 p.1 报告的 Hausdorf→Hausdorff 差异在 MinerU Markdown 中至少重复五处，不能按单一 occurrences 的描述完成修复验收；该工作须留待全篇审计后逐处手改与全文复核。
### E015 · 2026-10-02 · 扩展派单至所有未并行文献候选

- 交叉核对 PDF 路径、INDEX/AUDIT、页数、MinerU 导出和 PDF SHA 后登记 Peer-P41–P65 共 25 篇未覆盖任务；排除与已审 Smirnov 论文 byte-identical 的 Duminil-Copin 副本，Witten/Deng 已有完整候选留待 Master 集成；Viazovska dim24 published 与 arXiv 版 SHA 不同，作为独立任务。
- 25 个 Codex project create_thread 请求均获接受，基线 dc234aee28ba87a6dff9bebf14ac2186733c06aa；请求模型 gpt-6-luna，effort 继承已核 host default max。全部返回 provisional clientThreadId，当前不可用于 wait/read/message。最新 worktree 快照为52个（22个新 checkout 位于该基线，3个请求尚未映射），新 Peer 的正式 thread/status、实际 model/effort仍未逐个核验。
- 同一异步准备窗口内，worktree 总数从先前63降至52，11个之前观察到的目录（含 P37 a829）当前缺席；Master未执行 cleanup/remove，宿主处理原因与缺失 untracked 资产的恢复能力均 UNKNOWN。不得据此声称旧任务完成或 dirty 内容已保全。
- P40 已观察到 p.1–p.54 候选提交，p.55图像/AUDIT草稿未签；AUDIT-SOP 与 Handoff 方法范围冲突仍未闭合。P37 Fano flips 0/93，等待用户向 P37 task 窗口发新提示词。
### E016 · 2026-10-02 · Peer worktree 状态复核

- 在 25 个新 project create_thread 请求均被接受后，当前 `git worktree list` 为52项（含main），其中21个新checkout仍精确停在注册基线dc234aee；4个新请求没有可映射的checkout。P41–P65 formal threadId/turn status未在list_threads出现，不能称25 turn都active。
- 与更早的63项快照对比，11个先前已列出的旧worktree路径当前不存在，包括P37的a829；Master未调用archive/remove/clean。11个旧HEAD commit对象均能从对象库读取，但其中6个HEAD当前不被branch refs包含；这只证明commit对象现存，不证明未提交/未跟踪资产可恢复。应用归档收据未在当前Master任务可见。
- P40 worktree在本次观察时已提交p.1–p.66并留下p.67图像草稿；页面候选尚不接受，方法范围冲突仍待闭合。

### E017 · 2026-10-02 · Codex App Server 并发 Peer 工作流调查

- 将新报告写入 `dev-docs/001-2026-10-02-Codex-App-Server并发Peer工作流调查与试点方案.md`，状态明确为 `DRAFT_PROPOSAL / NOT_IMPLEMENTED / NOT_RUNTIME_VERIFIED`。R-003 的并发与身份要求保持不变；本轮没有启动 Codex App Server、模型、论文 Peer，也没有进入论文处理。
- 只读复核续传系统 `shuxuedashi-analysis-system` 的 `main@667e960d6cbe815ab26f041be1fa584651ed5ecd`：当前 root/代码把 P27 legacy 后端描述为 Devin CLI/tmux，把 v2 后端描述为 OpenCode ACP；`src/v2_pipeline.py` 每个 Round 启动 `opencode acp`、建立 ACP `sessionId`、采集通知并归档 Round。U1 的 OpenCode/Devin ACP smoke 日志确实报告 `/tmp` 文件写读成功；U2 的 OpenCode ACP 实验记录 12,062 个 thought chunks、95,884 字符，且 tracked `c_native_export2.json` 的 assistant reasoning 也是 95,884 字符。U2 同时记录 `end_turn`、零 agent message，不能把协议轮次结束认作解题成功。`046` 对 `session/list` 崩溃恢复的说明是设计；当前所查 `src` 未见其实现。当前 tracked repo/`git log` 搜索未发现 Codex CLI App Server (`thread/start`/`thread/resume`) 的接线；外部/未跟踪运行现场仍属 `UNKNOWN`。
- 共享 Codex repo `main@d039261aec53c50bb062e479114e245dd2168059` 的 broker 已按 worker `cwd` 启动独立 `codex app-server` 子进程并调用 `thread/start`，但只将 `thread.id` 放入进程内 session map；已有 private event/wire 线索，启动后不重建 worker、不调 `thread/resume`，也未暴露 `turn/steer`。默认 `max_workers=32`（可配置）只是该 broker admission setting，不是 OpenAI 并发上限；能力索引的 Codex real-host post-fix smoke 仍 open。官方 App Server 资料确认 ID、resume、turn/steer 和 sandbox API，但将 App Server 命令标为 experimental/不支持 production workload；共享 `CODEX_HOME` 的多进程锁/40-worker容量尚未实测。
- 方案借用续传系统 ACP 的 per-work-unit process、实时流、持久化每轮产物、以业务状态和文件证据复核结果；不把 ACP 运行记录改称 Codex App Server 验证，也不复用其“end_turn=结束”作成功判据。后续若采纳，先做无论文写入的单 worker fake/real smoke，再验证进程重启恢复、exact CWD/权限、multi-process shared state，最后测量实际 40 个唯一 thread/worker；具体阶段和 stop/fallback 判据见报告。

### E018 · 2026-10-02 · 旧 Peer 批次冻结、候选收割与 App Server 切换

- 用户声明所有曾启动的 Peer Worker 已停止。Master 以候选 Git history、页签连续性、AUDIT 修复/全文复读收据、路径隔离、未提交资产和 merge preflight 检查旧批次；没有删除、archive、clean 或 reset 任何 worktree。当前 `git worktree list` 为 16（含 main）；限定进程检查未见独立旧 Peer Codex App Server/broker，这只是本机当时的有界观察。
- P01–P40 中，28 个完整候选被新 Master 提交收割、P03 已在 `8713f2fc`，合计 29 个完整 P 结果；P17/P19/P27/P31/P32/P34 的审计证据收割但明确保持未完成；P10/P12/P30 无候选，P37 映射阻塞，P40 到 `422ed58a` 的 p.118/127 且有方法范围冲突、未集成。P41–P65 仅有 provisional create receipt，未发现可验证 worker 产物。更早的 Witten `bc4605dc`、Deng `3e5e964b`、Drinfeld `f46300d1` 也已收割为 `3429efe7`、`16381c63`、`d2e6bdac`。所有 exact OID、分类和未提交资产边界见收据 002。
- `AUDIT-INDEX.md` 已成为冻结后的当前篇级真值（138 条：102 完成、6 证据已收割未完成、28 冻结无候选、P37 阻塞、P40 hold）；`AUDIT-PROGRESS.log` 追加冻结/收割/控制模式收据。P07/P16 的 README 页数冲突未改写用户 README；PDF 路径数 141、distinct byte streams 139、索引行数 138 的口径冲突保持开放。
- 用户已通过 R-004 采纳“后续使用 Codex CLI App Server”的方向；该方向仍未实现/未通过真实 Host 验证。下一步是无论文写入的 start/observe/steer/interrupt-or-complete/restart/resume 资格化。论文继续处理由用户暂缓，资格化前不会派发或重启任何论文 worker。

### E019 · 2026-10-02 · ZCode 接管协议与确认 Gate

- 用户要求把工作交接给 ZCode，并说明 ZCode 在未来可使用 Codex App Server 或自己的 Sub Agent；同时明确要求真正开始动手前必须再次确认。R-005 将这写为当前要求：ZCode 只可做只读恢复并提交确认包；确认前禁止 App Server、control-plane pilot、Sub Agent、MinerU、论文处理、Git 写入和 push。
- 已将过时的 `ZCODE-HANDOFF-PROMPT.md` 原位替换为当前接管协议，明确旧文“自动开工/自动 push/不使用 Sub Agent”失效。新协议保存冻结批次、未完成候选、P37/P40 边界、用户 README dirty、Git 保护、App Server 与原生 Sub Agent 两条路线、每条路线的确认/资格化/恢复边界以及 ZCode 首次确认请求模板。
- R-005 允许选择两条未来路径，但不证明 ZCode 原生 Sub Agent 或 Codex App Server 已可运行。App Server 是独立 Codex CLI 进程而非 ZCode 原生 ACP；选择前后都须核验实际 Host 能力。当前执行队列为 `WAITING_FOR_USER_CONFIRMATION`，没有启动新 worker、模型或服务。
