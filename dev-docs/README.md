# dev-docs

本目录用于尚未裁定的项目治理、工具或工作流调查。文档必须标明提案/调查状态、证据边界、未知和复审条件；进入稳定要求、项目规则或实现后，再写入对应 owner，不在此复制 current truth。

## 开放提案

- [001 — Codex App Server 并发 Peer 工作流调查与试点方案](001-2026-10-02-Codex-App-Server并发Peer工作流调查与试点方案.md)：`ADOPTED_DIRECTION / DESIGN_DRAFT`；调查了续传解题系统的 ACP 经验、当前 Codex CLI App Server 协议与共享 broker 缺口，提出单 worker smoke、崩溃恢复和并发资格化路线。R-005 将它定位为 ZCode 可在用户确认后选择的一条路径；尚未实现、未运行真实 App Server/model，控制层 pilot 和论文 worker 都须先获得确认。
- [002 — 旧 Peer 批次冻结与收割收据](002-2026-10-02-旧Peer批次冻结与收割收据.md)：`CURRENT_FREEZE_RECEIPT`；记录 P01–P65 的实际候选、收割、阻塞、部分结果和未提交资产边界，不替代 AUDIT-INDEX/AUDIT-PROGRESS 的当前篇级/页级状态。
- [003 — GLM 配额耗尽停因与 worktree 断点账本](003-2026-10-04-GLM配额耗尽停因与worktree断点账本.md)：`CURRENT_RUN_BLOCKER_RECEIPT`；记录 2026-10-04 总攻 run 因 `zai-individual-coding-plan` 配额耗尽（code 1310，2026-10-07 10:33 重置）停摆的实证、换账户到 `zai-offpeak-idle-plan` 后 turn 全部不可执行的负面证据，以及 18 个论文 worktree 的逐篇已签页/末页/closeout/脏文件实算账本与恢复步骤。它是断点恢复凭据，不表示这些篇目已完成。
