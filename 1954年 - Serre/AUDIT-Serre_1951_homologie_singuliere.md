# AUDIT — Serre_1951_homologie_singuliere

> 逐页视觉审计说明，格式依 `AUDIT-SOP.md`「审计说明格式」。
> 印刷页码换算：印刷页 = PDF 页 + 423（PDF p.1 为 JSTOR 封面，PDF p.2 = 印刷 p.425）。

- actor=Wf-P45
- host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF SHA256=1420abbef07ec179ce1cbad72dec745b05a9f386fe1dbbeeaf98817835f9f69f
- MD 基线 SHA256=cb13117e5f47226c41b61d39cff1b1760463ea47ea772c1b8ee6a2c6f571b6aa（mineru 原始导出 `Serre_1951_homologie_singuliere_mineru/Serre_1951_homologie_singuliere__Serre_1951_homologie_singuliere.md`）
- 审计开始：2026-10-02 13:47
- 审计范围：本文件当前分块审计 p.1–p.9（后续分块由后续 ask 延续）
- 文本层判定：**可用**（JSTOR OCR 文本层；首页 `pdftotext -f 1 -l 1` 成功输出封面文字，p.2–p.3 数学正文页亦能输出全部段落文本）。但 OCR 噪声明显（例：`L'int6retde`、`getodesiques`、`memoireest` 等粘连/错字），故全程采用「**文本层主对账 + PNG 视觉核验**」双通道：文本层用于定位与文字对账，凡字形、上下标、公式、记号一律以 150dpi PNG（pngmono）视觉核验为最终裁决。
- mineru doc_id：UNKNOWN（导出目录未含 doc_id 元数据，仅 `full.md` 等产物；如需可在 `structured_content.json` 侧另行核查）

---

## p.001（PDF p.1 / JSTOR 封面页）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：题录页（JSTOR cover）——刊名、标题 "Homologie Singuliere Des Espaces Fibres"、Author(s): Jean-Pierre Serre、Source: The Annals of Mathematics, Second Series, Vol. 54, No. 3 (Nov., 1951), pp. 425-505、Published by、Stable URL、Accessed: 18/05/2012 10:32、两段 JSTOR 条款文字
- 结果：PASS±
- 差异：①md（第 14–15 行后）缺印刷页末句 "Annals of Mathematics is collaborating with JSTOR to digitize, preserve and extend access to The Annals of Mathematics." 及页脚 "http://www.jstor.org"——JSTOR 封面样板，非论文内容，不误导，不修；②印刷页 "available at" 与 URL 分两行，md 合并为一行——排版级，不修。其余题录字段逐项吻合。
- 备注：本页为 JSTOR 自动生成封面；该缺失句建议阅读时忽略。
