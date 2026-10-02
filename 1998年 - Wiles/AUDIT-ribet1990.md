# AUDIT-ribet1990 — 逐页视觉审计记录

> 依据 `AUDIT-SOP.md`「流程（每页 7 步）」「审计说明格式」「审计后修复」执行；一页一条，逐页交错落签。

- 论文：K.A. Ribet, *On modular representations of Gal(Q̄/Q) arising from modular forms*, Inventiones mathematicae **100** (1990), 431–476。
- PDF：`1998年 - Wiles/ribet1990.pdf`（47 页；p.1 为 Göttingen 数字化收藏封面/条款页，p.2–47 为正文扫描页，对应印刷 p.431–476，即 PDF p.N（N≥2）↔ 印刷 p.429+N）。
- 待审 Markdown：`1998年 - Wiles/ribet1990_mineru/ribet1990__ribet1990.md`（mineru 3.4.4 导出；`middle_json.json` 47 页；导出 metadata 未含独立 doc_id，记 UNKNOWN）。
- actor = Wf-P42；host/model/effort = zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）。
- PDF SHA-256 = `08f8ebfda40855d0f6d9e90e1dc352eb6576ecc44cc7c6e6ca3d448d724503b4`（开工实测与任务给定一致）。
- MD 基线 SHA-256 = `8fa0375dd53408c63acd0170755d4457643c365c0fdd652e542e772d612c68bf`（开工实测与任务给定一致）。
- 文本层判定：**不可用**——`pdftotext -f 1 -l 1` 仅得收藏封面 3 行题录；p.2/3/5/10/20/47 抽测均无文本层（0–1 字符）。全程采用**纯 PNG 逐页视觉审计**（gs pngmono 150dpi 单页渲染 → 目检 → 与 Markdown 比对）。
- 审计开始：2026-10-02 13:58 -0400（date 实取）。
- 本文件按页序追加；全部页完成后在文末补「总评 + 抽查覆盖声明 + mineru doc_id」。

## p.001（PDF p.1 / 收藏封面页，无印刷页码）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 13:58 -0400。
- PNG：`audit/ribet1990_p001.png`（pngmono，150 dpi）；仲裁裁片：`audit/300dpi/ribet1990_p001_header.png`、`audit/300dpi/ribet1990_p001_contact.png`、`audit/300dpi/ribet1990_p001_terms_line.png`（pnggray，300 dpi）。
- 核对：封面题录块（题名/作者/刊名/卷页）、Terms and Conditions 全文、Purchase a CD-ROM 全文、两处 Contact 地址块、图片引用 `images/page_0_image_15.jpg`（存在 ✓）。
- 发现（修复前）：①mineru 丢封面左上题录块（"On modular representations of Gal (.../Q) arising from modular forms. / by Ribet, K.A. / in Inventiones mathematicae / volume 100; pp. 431 - 476"）；②MD "Niedersaechssische" 为 OCR 拼写误，300 dpi 裁片确认印刷为 "Niedersaechsische"（单 s；CD-ROM 块处 MD 本即正确）；③印刷原样 "Conditions.With the usage"（句号后无空格），mineru 规范化为 "Conditions. With"。
- 修复（本页 commit，依据上述 300 dpi 裁片）：①在文件首补入题录块五段；②Niedersaechssische→Niedersaechsische；③还原 "Conditions.With"。
- 印刷原文 quirk：封面题录写 "Gal (.../Q)"（GDZ 生成器无法排 Q̄ 上划线，字面三点省略）——修复①按印刷原样保留，不改为 Gal(Q̄/Q)。
- 结果：PASS±（三项瑕疵均已当场修复闭环；修复后与原图逐项吻合）。

## p.002（PDF p.2 / 印刷 p.431）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:05 -0400。
- PNG：`audit/ribet1990_p002.png`（pngmono，150 dpi）；仲裁裁片：`audit/300dpi/ribet1990_p002_assume.png`（pnggray，300 dpi）。
- 核对：题录（题名/K.A. Ribet/地址）、节标题顺序（1. Introduction → The Main Theorem）、表示 ρ: G → GL(2, F)、l ≥ 3、odd/eigenvalues +1, −1、trace(ρ)、finite at p 定义（[34]/[35], §2.8）、p ≢ 1 (mod l) 行间公式、段尾 "Our new" 接下页 ✓。
- 印刷原文 quirk：印刷首行即 "Assume that **ρ** is a prime which exactly divides N (we write p ∥ N)"——主语排成 ρ（数学预期为 p），300 dpi 裁片确证为印刷原样；MD 与印刷一致，忠实保留不改。
- 备注：页眉 "Invent. math. 100, 431–476 (1990) / Inventiones mathematicae © Springer-Verlag 1990" 为 mineru 惯例不收录；完整题录信息已在本 MD 文章题名块与 p.001 封面补录块中。
- 结果：PASS。

## p.003（PDF p.3 / 印刷 p.432）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:10 -0400。
- PNG：`audit/ribet1990_p003.png`（pngmono，150 dpi）。
- 核对：Theorem 1.1 (Main Theorem) 陈述与条件 1. p ≢ 1 (mod l)、2. N is prime to l；Corollary 1.2；Fermat 方程 a^l+b^l+c^l=0；Frey 曲线 y²=x(x−a^l)(x+b^l)；V=E[l]；(4.1.9)/(4.1.12)；证明结尾 "we have a contradiction." ✓ 全部与印刷一致。
- 备注：定理与推论陈述的斜体排版未保留（如条件 2 印刷为斜体 "*N* is *prime to l*"，MD 为正体）——mineru 惯例排版级伪影，不误导，按 SOP 默认不批量修；证明结束符 □ 未收录（惯例）。
- 结果：PASS±。
