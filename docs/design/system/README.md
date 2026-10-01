# System Design

当前系统由三条相连的仓库内职责组成：根目录和获奖者目录保存 PDF/衍生材料；`AUDIT-SOP.md` 与当前 ZCode handoff 定义人工逐页比对流程；`AUDIT-INDEX.md`/`AUDIT-PROGRESS.log` 与逐篇 AUDIT 记录保存篇级/页级证据。批量 MinerU 导出脚本位于 `tools/mineru_batch.py`。尚无独立系统架构文档；若采集流程、持久状态或审计角色出现跨组件变化，再建立稳定设计。
