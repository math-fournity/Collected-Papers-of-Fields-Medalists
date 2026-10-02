# MEMORY.md：Collected-Papers-of-Fields-Medalists 持久记忆

## 当前状态

本仓库收录菲尔兹奖得主获奖相关论文、会议论文和颁奖材料，并维护 MinerU 衍生文本及逐页审计记录；详细资产地图见 README.md。截至 2026-10-02，AUDIT-INDEX 有 136 条记录：71 篇完成、40 篇原有分派（其中 P37 的 Fano 论文被错配 MinerU 导出阻塞，P40 仍在产出候选），另登记 P41–P65 共 25 篇新 Peer 任务。25 个 Codex project create_thread 请求均获接受并返回 provisional clientThreadId；最新 worktree 快照共 52 个，其中 21 个新 worktree 位于基线 dc234aee，4 个请求当前无对应 checkout；正式 task 状态和实际运行模型/effort 未逐个核验。并行创建期间，较早快照63个降至当前52个，11个既有 checkout 路径现不可见；Master 未运行清理，宿主归档/清理原因与恢复能力 UNKNOWN。全仓有141个 PDF 路径；SHA-256 清点发现两个 byte-identical 双副本组、139个 distinct PDF byte streams；逻辑统计口径仍与 INDEX 的140声明不一致，尚未闭合。Donaldson 1983（Peer-P03）已集成于8713f2fc；Witten bc4605dc与Deng 3e5e964b有完整Peer候选待Master集成。P40在worktree 716d已提交到p.66，p.67图像草稿未签；候选仍因方法范围复核未闭合而不计完成。

项目治理骨架已于 2026-10-01 建立。用户新增的剩余 MinerU Markdown 正文逐处 Edit 规则已记录于 `rulings.md#R-001`，并路由到 `AGENTS.md` 与 `ZCODE-HANDOFF-PROMPT.md#2.4`。MinerU Skill 的最近检查快照为 2026-10-01：本地 MinerU 4.0.8 CLI 可执行，library server 当时停止、standard 所需 GGUF 模型缺失；每个缺失导出的 Peer 必须重新只读核对当前运行时，只可用已就绪的本地资源，不能启停服务、下载模型、改配置或远程上传。

## 当前执行队列

| 方向 | 状态 | 下一步 | 相关 Feature |
|---|---|---|---|
| 剩余篇目的逐页审计与 Markdown 修复 | ACTIVE_WORK；用户要求将所有尚未并发处理的文档任务同时派发 | AUDIT-INDEX 现在为 136 条：71 完成、40 原有分派、25 个新 Peer create_thread 请求已接受。P37 0/93 映射阻塞，用户将向 P37 窗口发送新提示词；其原 worktree a829 当前不在 Git worktree 列表中。P40 在 worktree 716d 已提交 p.1–p.69，p.69 已提交；观察时 clean；方法冲突未解，候选不计完成。新批次均有 provisional clientThreadId；21 个新 checkout 可见、4 个无对应 checkout，formal thread 状态与实际运行模型/effort 未核；worktree 总数下降原因/恢复能力未知。Master 只做调度、审计身份/路径/证据、维护根总账并串行集成，不亲自逐页审计或修复论文 | AUDIT-001、AUDIT-002 |

## 当前开放问题与阻塞

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
