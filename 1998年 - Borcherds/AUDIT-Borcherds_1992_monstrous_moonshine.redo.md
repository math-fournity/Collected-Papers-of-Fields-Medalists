# AUDIT（重做）— Borcherds_1992_monstrous_moonshine

- 性质：**Luna 审计重做**。用户 2026-10-02 判定 Luna（Peer-P07, gpt-6-luna）审计不可信，本次按 PDF 原页对全部 41 页逐页全量重检；Luna 的旧修复（fix commit `01fe4a35f8075d3a8a30a56c159660e51045f0d2` 后的 Markdown）也是被检对象，一并以 PDF 原页为准重核。
- Actor：`Wf-R-P07`。
- Host / model / effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置，自报 UNKNOWN：模型自述无法独立核实）。
- 开工时间：2026-10-03 12:17 EDT。
- 工作区：worktree `/Users/aurolafly/.zcode/worktrees/cpf-redo-Borcherds_1992_monstrous_moonshine`（分支 `cpf-redo/Borcherds_1992_monstrous_moonshine`）；只写本篇目录。
- PDF：`Borcherds_1992_monstrous_moonshine.pdf`，41 页，SHA-256 `dee2cb9c3121cf1bf8bddce952d952e0f478a39e497df8946e220e9ceffab501`（本机 shasum -a 256 实测，2026-10-03）。
- 被检 Markdown：`Borcherds_1992_monstrous_moonshine_mineru/Borcherds_1992_monstrous_moonshine__Borcherds_1992_monstrous_moonshine.md`；重做开工基线 SHA-256 `b09bb557b3f70e02088f4a542d370fd530749b086fc6c3773151f897a639cbb1`（= Luna 修复后的最终版；原始 MinerU 产出 SHA-256 `2d89f26db76e7e2187a916d82120cb40f2296092f636fc830c03f8373ea75b18`，commit `4e5d9aabe`，可由 Git 恢复）。
- 文本层判定：`pdftotext -f 1 -l 1`（poppler，/opt/homebrew/bin/pdftotext）首页提取成功、全文可读 → **文本层可用**，采用「PDF 文本层 + 150dpi PNG 目检」**双通道主对账**；印刷原文仍是唯一裁决源，文本层仅作对照通道，文本层自身伪影（如断词、上标拍平）不作为判定依据。
- 渲染证据：本篇 `audit-redo/`（`pngmono` 150dpi，`p001.png`–`p041.png`，本块先做 p.001–p.009）；不动旧 `audit/`。
- 分级：PASS / PASS±（瑕疵但不误导）/ FAIL（数学内容错误或整段丢失，登记"以原图为准"并修复）。
- print quirk 纪律：印刷原文的错字/排版 quirk 忠实保留登记，绝不按数学预期静默改正。
- 全局备注（一次登记，不再逐页重复）：MinerU 导出在行文与行内公式衔接处普遍缺空格（如 `Suppose that$V = …`）、数字/系数被拆成带空格的 TeX 片段（如 `2 ^ { 46 }`）、引用以纯文本形式出现。这些是全文件性的排版风格伪影，不妨碍语义；除非页面特有或误导，不计入分级。
- 进度口径：按任务边界，本块不写 repo 根 `AUDIT-PROGRESS.log`；重做进度以本文件逐页条目与本块逐页 commit 为准。
- 本块范围：p.001–p.009（全篇 41 页重检的后续块另行分派）。

## p.001（PDF p.1 / 印刷 p.1）

- PNG：audit-redo/p001.png（pngmono 150dpi，本块实渲染实读）。
- 核对：题录（标题/期刊卷期页码/作者地址）、摘要全文、目录 1–15 条顺序与措辞、节标题「1 Introduction.」、Theorem 1.1 开头（V=⊕_{n∈Z}V_n、[16,17]、T_g(q)=Σ_{n∈Z}Tr(g|V_n)q^n）。
- 文本层通道：pdftotext 首页与 PNG 一致。
- 结果：**PASS**。
- 备注：MD 行文/地址把印刷断行连字 `Cam-bridge` 并为 `Cambridge`（跨行连字符合并，属正确修复，非内容变更）。Luna 旧修复逐项对印刷复核：摘要 `Co_1`（印刷 Co₁ ✓）、`affine`（印刷 affine ✓）、引文 `[16,17]`（✓）均正确；旧审计所列 `Cam bridge`/`repre sentation`/`afine`/`C o _ { 1 }`/`\lceil 1 6 , 1 7 \rceil` 在当前 MD 已不存在。Theorem 1.1 在印刷页尾断于 `…q^n is`，MD 相应断句位置一致（续文归 p.002 核对）。无修复动作。
