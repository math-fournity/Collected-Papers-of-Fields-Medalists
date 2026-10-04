# dev-docs

本目录用于尚未裁定的项目治理、工具或工作流调查。文档必须标明提案/调查状态、证据边界、未知和复审条件；进入稳定要求、项目规则或实现后，再写入对应 owner，不在此复制 current truth。

## 开放提案

- [001 — Codex App Server 并发 Peer 工作流调查与试点方案](001-2026-10-02-Codex-App-Server并发Peer工作流调查与试点方案.md)：`ADOPTED_DIRECTION / DESIGN_DRAFT`；调查了续传解题系统的 ACP 经验、当前 Codex CLI App Server 协议与共享 broker 缺口，提出单 worker smoke、崩溃恢复和并发资格化路线。R-005 将它定位为 ZCode 可在用户确认后选择的一条路径；尚未实现、未运行真实 App Server/model，控制层 pilot 和论文 worker 都须先获得确认。
- [002 — 旧 Peer 批次冻结与收割收据](002-2026-10-02-旧Peer批次冻结与收割收据.md)：`CURRENT_FREEZE_RECEIPT`；记录 P01–P65 的实际候选、收割、阻塞、部分结果和未提交资产边界，不替代 AUDIT-INDEX/AUDIT-PROGRESS 的当前篇级/页级状态。
- [003 — GLM 配额耗尽停因与 worktree 断点账本](003-2026-10-04-GLM配额耗尽停因与worktree断点账本.md)：`CURRENT_RUN_BLOCKER_RECEIPT`；记录 2026-10-04 总攻 run 因 `zai-individual-coding-plan` 配额耗尽（code 1310，2026-10-07 10:33 重置）停摆的实证、换账户到 `zai-offpeak-idle-plan` 后 turn 全部不可执行的负面证据，以及 18 个论文 worktree 的逐篇已签页/末页/closeout/脏文件实算账本与恢复步骤。它是断点恢复凭据，不表示这些篇目已完成。§5 记录本轮已收割两篇（ribet1990、Deng_2018_strichartz），§5.1 记录唯一一次总 Master 代提交 worker 未提交内容的完整实测复核依据，§5.2 记录四篇不可采信的过早 closeout。
- [004 — MinerU 云端 CDN 证书过期阻塞 9 篇导出](004-2026-10-04-MinerU云端CDN证书过期阻塞9篇导出.md)：`EXTERNAL_BLOCKER_RECEIPT`；在用户授权云端导出后实测到，mineru.net 上传与解析均成功（P30 的 70 页已在云端解析），但结果下载主机 `cdn-mineru.openxlab.org.cn` 的 `*.openxlab.org.cn` 证书已于 2026-10-02 23:59:59 UTC 过期，TLS 握手失败导致 CLI 报 `ConnectError`。同时坐实 P30/P37 的现有导出 Markdown 实为另外两篇论文（P30 是 ArnLind–Hoppe–Huisken，P37 是 Keshvari），并按 SOP 完成 P59–P65 共 7 篇 1649 页的 gs 分卷（14 卷、单卷最大 141 页、逐篇验证无丢页，产物在仓库外 `/tmp/mineru-vol/`）。§5 列出未自行决定的事项：未关闭 TLS 校验、未配置 API Key、未启停 daemon、未改写目标 Markdown。
