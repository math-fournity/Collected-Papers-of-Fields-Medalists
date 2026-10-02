# AUDIT-serre1987 — Sur les représentations modulaires de degré 2 de Gal(Q̄/Q)

状态：Wf-P43 分块候选审计（本 worker 负责 p.001-009）；页级发现即时以结构化 Edit 修复并随当页 commit；仍待 Master 按精确 commit 集成复核。

- actor=Wf-P43; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置；实际 effort 自报 UNKNOWN）。
- 开工时间：2026-10-02 13:34 EDT。
- 基线 commit：`8aa00fdde6167c8f6785c00c4feaed84518ad692`（分支 `cpf/serre1987`）；写入范围仅限 `1998年 - Wiles/` 下本篇 Markdown、本 AUDIT 文件与 `audit/serre1987_*` 证据图片。
- PDF：`serre1987.pdf`，52 页（Duke Math. J. 54 (1987)，印刷 p.179-230）；原件 SHA-256：`8048919db24dcb972435aaaa2a74d1168d0fe533af3aa26c6c809b12ddaee038`。
- 待审 MinerU Markdown：`serre1987_mineru/serre1987__serre1987.md`；审计前 SHA-256：`8671749d84b93434d89c346542964c0226ea21073423e1921b0410c95f5e4e61`。
- MinerU 导出：`middle_json.json` 与 `structured_content.json` 均登记 52 页；producer 为 MinerU 3.4.4（tier=basic, parse_mode=ocr）；导出中无 `doc_id` / `document_id` 字段。
- 文本层通道判定（2026-10-02，`pdftotext -f 1 -l 1 serre1987.pdf` 输出正常）：文本层可用 → 全程「文本层主对账 + PNG 视觉核验」双通道；文本层含扫描字符映射噪声（如 `p` 代 ρ、`e` 代 ε、`Fermai` 代 Fermat、`©` 印作 `0`），符号真值一律以 PNG 视觉（疑难字形 300 dpi 裁片）为准。
- 页码映射：PDF p.N = 印刷 p.(178+N)。

## p.001（PDF p.1 / 印刷 p.179）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 13:34 EDT。
- PNG：`audit/serre1987_p001.png`（pngmono，150 dpi）。
- 核对：题录（标题/作者/献词）、期刊页眉、摘要全部九段（含 ρ: G_Q → GL₂(F̄ₚ)、n° 1.2/1.3、n°s 2.2-2.4）、致谢 Tate/Fontaine 两段、页脚收稿日期。
- 结果：FAIL。印刷页脚收稿日期 “Received December 5, 1986.” 在 Markdown 全文缺失（grep 无命中）；已依本页原图在题录区（献词行后）补入。其余文字、公式与记号逐句吻合。
- 备注：期刊页眉 “Vol. 54, No. 1 / DUKE MATHEMATICAL JOURNAL © / 1987” 与页码 179 未收入 Markdown——排版级差异，常规不收，不改。摘要中印刷斜体强调词（conjecture、conducteur d'Artin、poids）在 Markdown 为正体纯文本，排版级，不误导。
