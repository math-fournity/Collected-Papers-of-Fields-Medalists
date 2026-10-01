# MEMORY.md：Collected-Papers-of-Fields-Medalists 持久记忆

## 当前状态

本仓库收集 1936–2022 年获奖者以及 2026 年新增获奖者的获奖相关论文、会议论文和颁奖材料，并维护 MinerU 衍生文本及逐页审计记录；详细资产地图见 README.md。截至 2026-10-01，AUDIT-INDEX 有 110 条论文记录，其中 70 篇完成、40 篇已分派。全仓有 141 个 PDF 路径；本轮 SHA-256 清点发现两个 byte-identical 双副本组，因此只有 139 个 distinct PDF byte streams。该结果不自动等于逻辑论文总数；AUDIT-INDEX 仍声明 140，数量口径冲突待闭合。Drinfeld 候选 HEAD `f46300d1`、Witten `bc4605dc`、Deng `3e5e964b` 尚未集成、不计入完成。Git worktree list 观察到 40 个 Peer worktrees（另有 main 共 41 个 checkout）；主线根进度现含本轮新增的 372 条页级候选收据，另有一条 Donaldson p.10 候选等级修订和一条 Deligne 报告签名复核更正（Master commit `3845fb56`）。这些均不等于页面内容已由 Master 接受或篇目已集成。

项目治理骨架已于 2026-10-01 建立。用户新增了剩余 MinerU Markdown 正文修复的逐处 Edit 规则，已记录于 `rulings.md#R-001`，并路由到 `AGENTS.md` 与 `ZCODE-HANDOFF-PROMPT.md#2.4`。当前工作已恢复论文队列，先处理 `1990年 - Drinfeld/Drinfeld_1974_elliptic_modules.pdf`；现有 MinerU Markdown 可用。Codex 全局 MinerU skill 位于 `/Users/aurolafly/.codex/skills/mineru/SKILL.md` 并已通过结构校验；CLI 4.0.8 可执行，但 MinerU library server 当前停止、standard 所需 GGUF 模型缺失，本轮未启动服务、下载模型或远程上传。

## 当前执行队列

| 方向 | 状态 | 下一步 | 相关 Feature |
|---|---|---|---|
| 剩余篇目的逐页审计与 Markdown 修复 | ACTIVE_WORK；用户要求立即维持 40 个项目 Peer 并发；官方 Codex app 项目任务入口未公布数值上限 | 40 个 Peer worktree 仍在（Master 不计）；36/40 至少有一笔 `audit(page)` commit，P10、P12、P30、P37 尚无页级 commit。最近一轮向主线追加 372 条标准页级候选收据，涉及 32 个 Peer actor。`list_threads` 仍只返回 Master task、没有这些 Peer 的正式 threadId，因此 40 个 Peer Session 当前活跃数不可验证；4 个无提交槽位是否仍在运行也未知。不能仅凭 worktree 把“40 个活动 Session”说成已证实，且在终态未知时不重复分派重叠写集。Master 不做论文初审，负责只读质量/路径审计、根级日志与总账、按 exact OID 串行集成 | AUDIT-001、AUDIT-002 |

## 当前开放问题与阻塞

- `AUDIT-001` 的 Edit 修复行为尚未验证：p.4–5 已发现待修 OCR 差异，按全篇审计完成前不改 Markdown；之后须逐处手改并复读全文。
- Drinfeld main 分支仍登记 5/32：p.1–3 PASS±、p.4–5 FAIL；worker worktree 已提交 p.1–32 审计、修复和澄清 commits，最新观察 HEAD 为 `f46300d1`，但最终修复后的全文回读/修复登记尚未由 Master 直接核实，候选仍未集成，Master 未编辑论文。
- MinerU library server 当前停止；不得因 `server_not_running` 自动启动，后续若需新解析须先按 skill 的质量/隐私边界处理。现有 Markdown 可供逐页审阅。
- 用户明确 Master 不再执行逐页初审；最新指令 supersede 先前“等三个任务结束再讨论扩容”的暂缓要求。Master 负责调度、只读质量复核、共享文件集成与验收，不替 worker 初审或改论文。
- 用户明确 Master-Luna 与各 Peer 使用唯一 actor ID，并在篇级 AUDIT、页级工作日志和 Git commit subject 中写明 actor/model/effort；历史 GLM 处理不回填或改写。当前 Master 身份为 `Master-Luna | gpt-6-luna/max`。
- 现有可验证 Peer 候选为 Witten `bc4605dc`、Deng `3e5e964b`；Drinfeld worker 候选 `f46300d1` 正处于修复/总复核阶段。Witten/Deng worktree 已消失但 commit 对象仍可读，正式 thread ID 未从 app 列表发现；集成前必须核 exact paths/base。
- P01–P09 分别由独立 worktree 从 `e04c4a96` 起步，并已出现带 Peer ID/model/effort 的逐页提交；P10–P39 分别从 `03760242` 起步。Codex app 的 create_thread 返回 30 个 `clientThreadId`，正式 `threadId` 仍未在 list_threads 中显示，不能将 client ID 传给 wait/read/message；依托共享 Git worktree 做只读监测。P01 Deligne 候选 HEAD `9857d0ccb8d2d54cc3d1298e8d7c389242478d17` 的 AUDIT p.6–p.22（包含 p.12）均缺显式 PASS/PASS±/FAIL 行，p.23 有结果行；主线 17:33 REVIEW 更正了先前误称 p.12 有结果的复核记录。相关页及本篇均不得据此视为通过或集成完成。
- 当前唯一篇目总数的证据口径仍未闭合：PDF 实物数量、SHA-256 distinct byte streams 数与 AUDIT-INDEX 声明的 140 行口径不一致。完成全范围声明前须逐文件交叉核对目录、重复副本、篇级索引与已存在 AUDIT 候选，不将少看/多算的资产默默排除。
- 官方 Codex 文档确认项目 task/worktree 并行工作模式，但未发现该 app task 入口的数字并发上限；API multi-agent 默认并发配置不同，不能当作 app project peer cap。40 是用户本轮的最低操作目标，不是平台保证值。
- 当前 Codex 任务列表只暴露 Master 任务，Peer 的正式 threadId/status 仍不可见；40 个 worktree 只证明 40 个隔离 checkout 已注册，不能证明 40 个 Session 此刻都在运行。36 个 checkout 有页级提交、32 个 Peer actor 在最近收据区间产生了新提交，证明这批候选有近期执行证据；不补足另 4 个 lane 的 Session 终态证据。

## 当前有效约束摘要

- 剩余 MinerU Markdown 正文修复须使用 `Edit` 逐处手工编辑，脚本只做人工修复后的只读终验/清点；详细规则见 `AGENTS.md`，操作说明见 `ZCODE-HANDOFF-PROMPT.md#2.4`。
- `AUDIT-INDEX.md` 是篇级进度唯一真值，`AUDIT-PROGRESS.log` 是页级恢复点；历史 handoff 快照不覆盖这两个 owner。

## 开放事故

- 当前无已确认 `OPEN_INCIDENT`。

## 已关闭事故注册表

实际记录的 `status` 必须是 `CLOSED_INCIDENT`；空表不编造事故。

| ID | status | closed_at | closure evidence | still-valid lesson | reopen_if | current route |
|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - |

## 已验证事实

- main 分支 AUDIT-INDEX.md 有 70 篇带完成标记，Drinfeld 32p 登记为 审计中（5/32）；这只证明 canonical 登记状态，不代表未集成 peer 候选已完成。
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
