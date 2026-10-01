# rulings.md：Collected-Papers-of-Fields-Medalists 用户裁定

## R-001 · 2026-10-01 · 剩余论文 Markdown 修复改为逐处 Edit

**状态**：已采纳。

**原始用户指令**：

> 剩余篇目改为以 Edit 逐处手改为主（脚本只做终验清点），速度会慢但每处更直观，请你把这个规矩记录到当前repo的AGENTS.md中，并且要求以后的AI，尽可能地亲力亲为，确保结果是被AI全面确认过的。

**归一后的当前要求**：适用于尚未完成篇目的 MinerU Markdown 正文纠错和内容级修复。由负责工作的 AI 基于 PDF/原页证据，通过当前 Host 的 `Edit` 工具逐处修改；脚本只在手工编辑之后执行只读终验与清点，不得写回或自动修复目标 Markdown。AI 还须复读最终 Markdown，并按该篇适用的原文审计方式确认修复无误、没有遗漏或引入新差异；记录页码、依据和复核结果。

**边界**：不追溯要求重做此前已经完成的篇目或修复；不改变 PDF 原件、审计分级、印刷原文优先、MinerU 初始导出与图像渲染流程。本轮用户另行要求暂不开始论文处理，因此本次只写入治理规则，没有执行任何篇目修复。

## R-002 · 2026-10-01 · 并发论文处理需记录 AI 身份

**状态**：已采纳。

**原始用户指令**：

> 边做边迭代你的并发多Peer工作系统，全部做完所有剩余的文献处理工作，以官方允许的最大并发量进行，如果不知道最大并发量就去网上搜索官方文档，如果官方文档没有写，那么就至少10个并发。你需要把你（Luna）和你的Peer处理的内容，在工作日志中记录你们的身份，以和之前的GLM模型的处理区别开来。尤其是git log。

**归一后的当前要求**：Master 使用 `Master-Luna`，每个并发论文 Worker 使用唯一 `Peer-PNN` 身份；工作记录同时写明实际配置的模型与 reasoning effort（本轮例如 `gpt-6-luna/max`）。身份应出现在每篇 AUDIT 的任务元数据/页级记录、Master 维护的根页级进度日志，以及 Peer 自己的 audit/fix/complete Git commit subject 中。Master 对主线总账和集成提交使用自己的身份，并在集成记录中保留候选 Peer、模型、exact source OID 与验证范围。

不得改写既有 Git 历史或把旧 GLM 工作追溯标成 Luna/Peer；旧记录未保存的模型身份保持未知。Git 作者字段仍由真实提交环境决定，不得伪造作者、签名或时间；用 commit subject/body 清楚记录 AI actor、model 和 effort。并发论文使用独立 worktree 和独占论文目录，Master 是唯一 canonical integrator，根级当前态由 Master 串行维护。
