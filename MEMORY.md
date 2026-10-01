# MEMORY.md：Collected-Papers-of-Fields-Medalists 持久记忆

## 当前状态

本仓库收集 1936–2022 年获奖者以及 2026 年新增获奖者的获奖相关论文、会议论文和颁奖材料，并维护 MinerU 衍生文本及逐页审计记录；详细资产地图见 README.md。截至 2026-10-01，main 分支 AUDIT-INDEX.md 有 70 篇完成标记，Drinfeld 仍登记为审计中（主线 5/32）；Drinfeld Peer worktree 已签至 p.32 并进入修复/总复核，最新观察候选 HEAD 为 `f46300d1`。Witten、Deng 候选分别为 `bc4605dc`、`3e5e964b`，均未集成、不计入篇级完成。唯一篇目集合为 140，尚有 Drinfeld 与大量未登记论文待闭环。

项目治理骨架已于 2026-10-01 建立。用户新增了剩余 MinerU Markdown 正文修复的逐处 Edit 规则，已记录于 `rulings.md#R-001`，并路由到 `AGENTS.md` 与 `ZCODE-HANDOFF-PROMPT.md#2.4`。当前工作已恢复论文队列，先处理 `1990年 - Drinfeld/Drinfeld_1974_elliptic_modules.pdf`；现有 MinerU Markdown 可用。Codex 全局 MinerU skill 位于 `/Users/aurolafly/.codex/skills/mineru/SKILL.md` 并已通过结构校验；CLI 4.0.8 可执行，但 MinerU library server 当前停止、standard 所需 GGUF 模型缺失，本轮未启动服务、下载模型或远程上传。

## 当前执行队列

| 方向 | 状态 | 下一步 | 相关 Feature |
|---|---|---|---|
| 剩余篇目的逐页审计与 Markdown 修复 | ACTIVE_WORK；用户新授权完成全部剩余篇目并采用至少 10 个并发项目 Peer；官方 Codex app 项目任务/worktree 资料未给出数值上限 | Master 不做论文初审；保留 Drinfeld 为现有活动 Peer 并新增 9 个独占 worktree 任务至 10 个活跃槽；按页数升序滚动补位；Master 连续只读审计并单写根日志/总账，候选按 exact OID 串行集成 | AUDIT-001、AUDIT-002 |

## 当前开放问题与阻塞

- `AUDIT-001` 的 Edit 修复行为尚未验证：p.4–5 已发现待修 OCR 差异，按全篇审计完成前不改 Markdown；之后须逐处手改并复读全文。
- Drinfeld main 分支仍登记 5/32：p.1–3 PASS±、p.4–5 FAIL；worker worktree 已提交 p.1–32 审计、修复和澄清 commits，最新观察 HEAD 为 `f46300d1`，但最终修复后的全文回读/修复登记尚未由 Master 直接核实，候选仍未集成，Master 未编辑论文。
- MinerU library server 当前停止；不得因 `server_not_running` 自动启动，后续若需新解析须先按 skill 的质量/隐私边界处理。现有 Markdown 可供逐页审阅。
- 用户明确 Master 不再执行逐页初审；最新指令 supersede 先前“等三个任务结束再讨论扩容”的暂缓要求。Master 负责调度、只读质量复核、共享文件集成与验收，不替 worker 初审或改论文。
- 用户明确 Master-Luna 与各 Peer 使用唯一 actor ID，并在篇级 AUDIT、页级工作日志和 Git commit subject 中写明 actor/model/effort；历史 GLM 处理不回填或改写。当前 Master 身份为 `Master-Luna | gpt-6-luna/max`。
- 现有可验证 Peer 候选为 Witten `bc4605dc`、Deng `3e5e964b`；Drinfeld worker 候选 `f46300d1` 正处于修复/总复核阶段。Witten/Deng worktree 已消失但 commit 对象仍可读，正式 thread ID 未从 app 列表发现；集成前必须核 exact paths/base。
- 下一轮待启动 9 个 Peer（补足 Drinfeld 后共 10）：Deligne 36p、Ahlfors 1930 38p、Donaldson 38p、Bourgain 38p、Perelman entropy 39p、Frey 40p、Borcherds 41p、Crandall–Lions 42p、Serre GAGA 43p。上述 MinerU Markdown 均已在相应目录确认存在；每个 Peer 只写一个独占论文目录。
- 官方 Codex 文档确认项目 task/worktree 并行工作模式，但未发现该 app task 入口的数字并发上限；API multi-agent 默认并发配置不同，不能当作 app project peer cap。10 是本轮用户指定的目标，不是平台保证值。

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
