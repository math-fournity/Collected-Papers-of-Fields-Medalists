# dev-docs

本目录用于尚未裁定的项目治理、工具或工作流调查。文档必须标明提案/调查状态、证据边界、未知和复审条件；进入稳定要求、项目规则或实现后，再写入对应 owner，不在此复制 current truth。

## 开放提案

- [001 — Codex App Server 并发 Peer 工作流调查与试点方案](001-2026-10-02-Codex-App-Server并发Peer工作流调查与试点方案.md)：`ADOPTED_DIRECTION / DESIGN_DRAFT`；调查了续传解题系统的 ACP 经验、当前 Codex CLI App Server 协议与共享 broker 缺口，提出单 worker smoke、崩溃恢复和并发资格化路线。用户已采纳后续控制方向，但尚未实现、未运行真实 App Server/model，论文 worker 仍须先通过控制层资格化。
- [002 — 旧 Peer 批次冻结与收割收据](002-2026-10-02-旧Peer批次冻结与收割收据.md)：`CURRENT_FREEZE_RECEIPT`；记录 P01–P65 的实际候选、收割、阻塞、部分结果和未提交资产边界，不替代 AUDIT-INDEX/AUDIT-PROGRESS 的当前篇级/页级状态。
