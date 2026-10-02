# feature-list.md：Collected-Papers-of-Fields-Medalists 当前需求账本

> 本文件回答系统应该怎样。实际实现和验证必须回到代码、配置、测试和运行实物。
> 新建或发生语义/交付变化的 Feature 用 `SRC/DES/IMP/VER/EVD` 路由到来源、设计、实现、
> 验证和实现证据包；证据包可以由多个 Features 共用，不强制每 Feature 单独建闭包文件。

## 状态语义

裁定：候选 / 已采纳 / 已废止。交付：未开始 / 部分实现 / 已实现待验证 / 已验证。

## 项目边界

| ID | 类型 | 当前要求 | 来源 | 裁定 | 交付 | 认知锚点 |
|---|---|---|---|---|---|---|
| AUDIT-001 | 工作方法约束 | 剩余篇目的 MinerU Markdown 正文纠错由 AI 用 Edit 逐处手改；脚本只做只读终验/清点；AI 按原文证据全面复核改动和最终全文。R-005 的用户确认 Gate 是实际执行前置，不因本 Feature 已采纳而自动启动论文处理。 | `rulings.md#R-001`、`rulings.md#R-005` | 已采纳；执行等待用户确认 | 已记录；实际执行待验证 | SRC:`rulings.md#R-001/#R-005`；DES:`AGENTS.md#剩余篇目的-MinerU-Markdown-修复`、`ZCODE-HANDOFF-PROMPT.md` §5；IMP:`未启动`；VER:`未运行`；EVD:`后续各篇 AUDIT 修复登记` |

| AUDIT-002 | 证据来源、并发与控制面 | Master 与每个 worker 使用唯一 AI actor；篇级 AUDIT、页级工作日志和 Git commit 记录 actor/模型/effort，历史 GLM 身份不回填。旧 Project Peer 批次已冻结并按候选实物收割。ZCode 接手后，只有用户明确确认的 scope 才可选择独立 worktree 的 Codex CLI App Server，或 ZCode 当前 runtime 实际提供的原生 Sub Agent；两条路都必须记录实际 actor/model/effort、输入身份、独占写入集与恢复边界。App Server 仍需先做无论文写入的 start/observe/steer/restart/resume 资格化；ZCode Sub Agent 则需用户确认 exact agent envelope。确认前禁止启动任何 worker、pilot、MinerU 或论文处理；已确认的 ZCode integrator 独占根级 current truth 与串行集成。 | `rulings.md#R-002`、`rulings.md#R-003`、`rulings.md#R-004`、`rulings.md#R-005` | 已采纳；执行仍等待用户确认 | 旧批次收割已完成；ZCode 接管文档已就绪，未启动任何控制面 | SRC:`rulings.md#R-002/#R-003/#R-004/#R-005`；DES:`AUDIT-SOP.md#AI-身份与并行Worktree日志`、`ZCODE-HANDOFF-PROMPT.md`、`dev-docs/001-2026-10-02-Codex-App-Server并发Peer工作流调查与试点方案.md`；IMP:`AUDIT-PROGRESS.log`、各篇 `AUDIT-*.md` 与 Git history；VER:`确认后按所选通道执行的非论文资格化/host envelope 核验`；EVD:`dev-docs/002-2026-10-02-旧Peer批次冻结与收割收据.md`、ZCode handoff receipt、Peer 候选与 Master 集成收据 |

## 锚点合同

- `SRC`：ruling/spec/issue；`DES`：stable design/ADR；`IMP`：code/config/schema/runtime；
  `VER`：test/run/receipt；`EVD`：逐 Feature claim-to-asset-to-evidence 报告或等价 evidence bundle。
- `已验证` 必须五类可解析；缺失类别要显式降级，不能用“见相关文件”或 Feature 状态替代证据。
- 既有自由文本锚点在被触碰前可标 `LEGACY_PARTIAL`；没有直接证据时不要补猜。
