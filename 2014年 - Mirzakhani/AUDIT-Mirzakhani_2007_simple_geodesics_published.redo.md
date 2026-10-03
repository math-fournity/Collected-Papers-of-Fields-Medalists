# AUDIT-Mirzakhani_2007_simple_geodesics_published.redo — Luna 审计重做（逐页全量重检）

- 性质：Luna 审计重做。用户 2026-10-02 判定 Luna 审计不可信，本文件按 PDF 原页逐页全量重检，
  Luna 旧修复（已并入 MinerU Markdown 基线）一并重核；印刷原文（PDF）是唯一裁决源。
- actor：Wf-R-P11
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- 日期：2026-10-03 12:03 EDT 起
- 原文 PDF：`2014年 - Mirzakhani/Mirzakhani_2007_simple_geodesics_published.pdf`（44 页）
  SHA-256 = `c19a088d97b2b3223481341d059ef7836ea9f575f580d3bf574d0b475e7615cf`
- 被检 Markdown 基线：`2014年 - Mirzakhani/Mirzakhani_2007_simple_geodesics_published_mineru/Mirzakhani_2007_simple_geodesics_published__Mirzakhani_2007_simple_geodesics_published.md`
  SHA-256 = `65320689fcaaa8fcbdc4133f224bfba5e9d298c8f8056362e9770a2b5aa43527`（重做起点）
- 证据图：`2014年 - Mirzakhani/audit-redo/`（pngmono 150dpi，p0NN.png；旧 `audit/` 不动）
- 文本层判定：`pdftotext -f 1 -l 1` 首页输出干净（题录、Contents 全部可读）→ **文本层可用，
  本篇采用双通道主对账**：每页 gs pngmono 150dpi PNG 目检 + pdftotext 该页文本逐句对账；
  两者均以 PDF 原页为准，冲突时以 300dpi 裁剪仲裁（如有）。
- 印刷页码换算：Invent. math. 167, 179–222 (2007)；PDF p.N = 印刷 p.(178+N)。
- 分级：PASS / PASS±（瑕疵但不误导）/ FAIL（数学内容错误或整段丢失）。
- 修复纪律：Markdown 内容错误用结构化 Edit 逐处修复（含修正 Luna 旧修复中的错误），每处可溯源该页
  证据；print quirk 忠实登记不改；每页一提交 `redo(page): …`。

---

## p.001（PDF p.1 / 印刷 p.179）
- PNG：audit-redo/p001.png（pngmono 150dpi）；旁证：pdftotext -f 1 -l 1（文本层干净）。
- 核对：题录（刊名卷期页眉头 Invent. math. 167, 179–222 (2007)、DOI 10.1007/s00222-006-0013-2、标题、
  作者、Princeton 单位与 e-mail、Oblatum 19-VII-2005 & 17-VII-2006、Published online: 12 October 2006 –
  © Springer-Verlag 2006）；Contents 1–8 条目与页码 179/186/190/194/203/206/211/217；§1 Introduction
  首段；首段公式 $V_{g,n}(L_1,\ldots,L_n)$、$\mathcal{M}_{g,n}$、$(\mathbb{R}_{\ge0})^n$、$\mathbf{Mod}_{g,n}$、
  $\mathcal{T}_{g,n}(L)$。
- 结果：**PASS±**。
- 差异（不误导的排版伪影，未改动）：
  - 行内公式前后空格合并：L27 "the volume$V_{g,n}...$of the moduli space"、L29 "Given$L=..." 等；
  - Contents 点线简化为 "....."（L16–23）。
- Luna 旧修复重核：刊眉头补录（MD L3–4）与原页一致；L27 无 $\bar{V}$（原页即 $V_{g,n}$）、
  L29 $(\mathbb{R}_{\ge0})^n$ 与原页下标 ≥0 一致——两处旧修复正确，维持。
- 备注：页断在 "We"（L29 末），其后内容属 p.2。

