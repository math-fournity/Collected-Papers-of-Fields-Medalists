# Development

可执行脚本目前集中在 `tools/`，包括 MinerU 批量导出脚本；项目主体是静态 PDF、Markdown、图像和审计文档，根入口未提供统一 build/test 命令，逐页质量验收按 `AUDIT-SOP.md` 进行。论文内容修复按根 `AGENTS.md` 使用 Edit，不用脚本写回 Markdown。修改现有文件前检查 tracked/dirty/最近 commit/HEAD；Git stage 只用精确路径并保留其它工作面变化。
