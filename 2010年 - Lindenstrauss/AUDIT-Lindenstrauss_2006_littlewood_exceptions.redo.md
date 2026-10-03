# Page-by-page redo audit — Lindenstrauss_2006_littlewood_exceptions

- 性质：**Luna 审计重做**。用户 2026-10-02 判定 Luna（Peer-P15, gpt-6-luna/max）对该篇的审计不可信，本文件对其全部页面逐页对照 PDF 原页全量重检，Luna 的旧修复（`AUDIT-Lindenstrauss_2006_littlewood_exceptions.md` 所登记者）一并重新核实；印刷原文（PDF 原页）是唯一裁决源，Luna 旧修复仅是被检对象之一。
- Actor：`Wf-R-P15`（Luna 审计重做 worker）
- Host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置；模型自报 UNKNOWN，按 SOP 身份纪律如实登记）
- PDF：`Lindenstrauss_2006_littlewood_exceptions.pdf`，48 页（印刷页 513–560），SHA-256 `8f32c468132cc9cb3441beed933fb31a3dd2799a6ab46cc79c5050492b198a36`
- 被检 Markdown：`Lindenstrauss_2006_littlewood_exceptions_mineru/Lindenstrauss_2006_littlewood_exceptions__Lindenstrauss_2006_littlewood_exceptions.md`，基线 SHA-256 `aca45d5a32ad8846a41ffa9f5c781715f5827a8a200f52ae3dd39230fff5dd5f`（重做开始时点）
- 日期：2026-10-03 12:08 EDT 开工
- 文本层判定：`pdftotext -f 1 -l 1` 于首页返回清晰完整文本（arXiv 头、刊名卷期页码、标题、作者、摘要、§1 开头、脚注均可读）→ **文本层可用，本重做采用双通道主对账**：pdftotext 逐页提取与 PNG（pngmono 150dpi）视觉核对互证；字形疑难再按需 300dpi 仲裁。
- 证据图：`audit-redo/Lindenstrauss_2006_littlewood_exceptions_p0NN.png`（pngmono 150dpi；本目录与同父目录另一篇的重做证据以短名前缀互斥）。旧 `audit/` 与旧 AUDIT 文件不动。
- 本块范围：p.1–p.9（PDF p.1–9 / 印刷 p.513–521）。

## Page entries

### p.001（PDF p.1 / 印刷 p.513）

- 证据 PNG：`audit-redo/Lindenstrauss_2006_littlewood_exceptions_p001.png`（pngmono 150dpi）；双通道辅证 `pdftotext -f 1 -l 1 -layout`（文本层可用）。
- 核对：题录（期刊卷期页码行、标题、作者行、arXiv 直印水印）、摘要、§1 与 §1.1 标题、§1.1 前三段正文、脚注（NSF 号 DMS-007133 / DMS-0140497 / DMS-0434403 / DMS-0222452、Clay fellow、AIM）。
- 结果：**PASS±**
  - 标题、作者行、摘要（含 "Hausdorff dimension zero"）、§1.1 三段、脚注全文与印刷页逐项吻合。
  - **Luna 旧修复复核**：摘要 `Hausdorf→Hausdorff`（旧 AUDIT p.001 登记）与印刷一致，修复正确，保留。
  - 登记非保留伪影（按 Witten 篇先例，不修）：①印刷页眉期刊行 "Annals of Mathematics, 164 (2006), 513–560" 未保留（MinerU 系统性丢页眉）；②左侧竖排 arXiv 水印 `arXiv:math/0612721v1 [math.DS] 22 Dec 2006` 未保留；③MD 行 11 印刷 `\mathbb{R}^k` 拍平为 `R<sup>k</sup>`（黑体拍平，不误导）。
  - 印刷原文 "unimodular lattices in three space" 与 MD 一致，忠实保留（不作数学预期改写）。
- 备注：本页无需 Edit；MD 段落跨页续接属 MinerU 页流合并（行 15 延入 p.2 内容，p.2 复核）。
