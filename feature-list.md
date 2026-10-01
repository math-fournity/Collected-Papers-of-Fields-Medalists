# feature-list.md：Collected-Papers-of-Fields-Medalists 当前需求账本

> 本文件回答系统应该怎样。实际实现和验证必须回到代码、配置、测试和运行实物。
> 新建或发生语义/交付变化的 Feature 用 `SRC/DES/IMP/VER/EVD` 路由到来源、设计、实现、
> 验证和实现证据包；证据包可以由多个 Features 共用，不强制每 Feature 单独建闭包文件。

## 状态语义

裁定：候选 / 已采纳 / 已废止。交付：未开始 / 部分实现 / 已实现待验证 / 已验证。

## 项目边界

| ID | 类型 | 当前要求 | 来源 | 裁定 | 交付 | 认知锚点 |
|---|---|---|---|---|---|---|
| AUDIT-001 | 工作方法约束 | 剩余篇目的 MinerU Markdown 正文纠错由 AI 用 Edit 逐处手改；脚本只做只读终验/清点；AI 按原文证据全面复核改动和最终全文。 | `rulings.md#R-001` | 已采纳 | 已记录；实际执行待验证 | SRC:`rulings.md#R-001`；DES:`AGENTS.md#剩余篇目的-MinerU-Markdown-修复`；IMP:`ZCODE-HANDOFF-PROMPT.md#2.4`；VER:`未运行`；EVD:`后续各篇 AUDIT 修复登记 |

| AUDIT-002 | 证据来源与协作 | 并发论文处理须为 Master 与每个 Peer 分配唯一 AI actor；在篇级 AUDIT、页级工作日志和 Git commit 中记录 actor、实际模型/effort，清楚区分历史 GLM 处理；独立 worktree/论文目录，Master 独占维护根级当前态与集成。 | `rulings.md#R-002` | 已采纳 | 已记录；实际执行待验证 | SRC:`rulings.md#R-002`；DES:`AUDIT-SOP.md#AI-身份与并行Worktree日志`；IMP:`AUDIT-PROGRESS.log`、各篇 `AUDIT-*.md` 与 Git history；VER:`本轮工作进行中`；EVD:`Peer 候选提交与 Master 集成收据` |

## 锚点合同

- `SRC`：ruling/spec/issue；`DES`：stable design/ADR；`IMP`：code/config/schema/runtime；
  `VER`：test/run/receipt；`EVD`：逐 Feature claim-to-asset-to-evidence 报告或等价 evidence bundle。
- `已验证` 必须五类可解析；缺失类别要显式降级，不能用“见相关文件”或 Feature 状态替代证据。
- 既有自由文本锚点在被触碰前可标 `LEGACY_PARTIAL`；没有直接证据时不要补猜。
