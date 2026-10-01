# Operations

本仓库没有生产部署服务。论文处理工作会使用本机工具或外部 MinerU 服务；是否可运行须按需在当前环境核实，运行中断通过 `AUDIT-PROGRESS.log` 恢复。MinerU GUI/server 的保护边界见当前 `ZCODE-HANDOFF-PROMPT.md`，不得为了脚本检查停止或重启用户正在使用的服务。若引入常驻服务或自动作业，再补充启停、监控与恢复 runbook。
