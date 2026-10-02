# AUDIT — Smirnov_2010_conformal_invariance（Duminil-Copin & Smirnov, "Conformal invariance of lattice models"，70 页）

- actor：Wf-P30
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置，自报 UNKNOWN）
- PDF：Smirnov_2010_conformal_invariance.pdf，SHA-256 = dfc298f2b1b7bd5b26bb5dfa2a3ed3c25e27248924c2703711c69cbd19194cc5（70 页，pdfinfo 核实）
- MD 基线：Smirnov_2010_conformal_invariance_mineru/Smirnov_2010_conformal_invariance__Smirnov_2010_conformal_invariance.md，SHA-256 = b4b2cd09c397fbcb0449c4ec8f457439a85c2a91a5d4975515fa10e0272d95b8（1743 行）
- 通道判定：`pdftotext -f 1 -l 1` 首页输出完整可读（标题/作者/摘要/目录）→ **文本层可用**，全程「文本层主对账 + PNG 视觉核验」双通道。
- 审计开始：2026-10-02 13:34 EDT

## ⚠️ 开工即发现的全局异常（阻断逐页内容对账与修复）

**MinerU 导出与 PDF 是两篇不同的论文，MD 中不存在本篇任何对应段。**

证据（2026-10-02，本 worktree 内实际读取）：

1. PDF p.1（pdftotext + PNG p001.png 双通道）：标题 "Conformal invariance of lattice models"，作者 Hugo Duminil-Copin and Stanislav Smirnov，arXiv:1109.1549v4 [math.PR] 21 Jun 2012。
2. MD 第 1–2 行（`head -60`）：标题 "MULTI LINEAR FORMULATION OF DIFFERENTIAL GEOMETRY AND MATRIX REGULARIZATIONS"，作者 "JOAKIM ARNLIND, JENS HOPPE, AND GERHARD HUISKEN"。
3. `grep -in "conformal invariance|Smirnov|Ising|Duminil"` 全 MD 仅命中 1 行，且为 "sur**prisingly**" 含 "ising" 的假阳性；MD 内无任何 Ising/SLE/fermionic observable/Smirnov 内容。
4. MinerU 原始导出 `Smirnov_2010_conformal_invariance_mineru/Smirnov_2010_conformal_invariance/structured_content.json`：`is_full_document: true`，33 页，page 0 首块即 Arnlind–Hoppe–Huisken 标题；同目录 images/ 共 248 个公式图，页号仅覆盖 page_1–page_31（33 页论文），与本篇 70 页规模不符。

结论：整个 MinerU 导出（MD + structured_content.json + images）属于 Arnlind–Hoppe–Huisken "Multi linear formulation of differential geometry and matrix regularizations"（约 33 页），对本篇 PDF 是**整文档错源**，不是逐页转写瑕疵。按 `REMAINING_PAPER_MARKDOWN_EDIT_V1` 与 AUDIT-SOP，这不是可用逐处 Edit 修复的内容级错误，也不允许把人工重打的文本冒充 MinerU 导出；正确处置是**对本篇 PDF 重新执行 MinerU 初始导出**后重审。该处置超出本块（p.1–9 审计）授权范围，本块按指示「先完成能完成的页」：逐页渲染 PNG、双通道核对 PDF 原文、逐页落签；因 MD 无对应段，p.1–9 全部记 **FAIL（对应段整文档缺失，以原图为准）**，不做任何 MD 修复（fixes = 空）。

---

## p.001（PDF p.1 / 印刷 p.1）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：题录页——标题 "Conformal invariance of lattice models"；作者 Hugo Duminil-Copin and Stanislav Smirnov；日期 November 27, 2024（arXiv v4 编译日期）；Abstract 全文；Contents §1–§6.4 与页码；左缘 arXiv:1109.1549v4 [math.PR] 21 Jun 2012 竖排水印；页脚印刷页码 1。
- 结果：FAIL——MD（b4b2cd0… 基线）为 Arnlind–Hoppe–Huisken 另一篇论文，本页对应段（标题/摘要/目录）整文档缺失，以原图为准。
- 备注：印刷 quirk 登记——目录 §6.2 原文作 "sub-sequential limits of FK-Ising interfaces are Loewner chains"（行首小写 s），p.43 正文节标题同式样；后续 MinerU 重导出后仍须忠实保留，不得按数学惯例改写。文本层（pdftotext -layout）与 PNG 视觉逐项一致。
