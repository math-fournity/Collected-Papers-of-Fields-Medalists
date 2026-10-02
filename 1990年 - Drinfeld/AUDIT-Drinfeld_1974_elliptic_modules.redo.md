# AUDIT（重做）— V. G. Drinfeld, "Elliptic Modules"（p.1–p.9 批次）

- 性质：Luna 审计重做。用户 2026-10-02 判定 GPT-6 Luna 的审计不可信，本文件对 Drinfeld_1974_elliptic_modules 逐页对照 PDF 原页全量重检；Luna 旧修复（初判 32 页 PASS± 3 / FAIL 29，修订提交 145706440e02f1e1d2b5793a2f70367421cc108e）一并作为被检对象重核。
- actor：Wf-R-Drinfeld；host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置；本模型对自身 reasoning effort 无直接读取渠道，effort 标记自报 UNKNOWN，以 run 级配置 max 为准）。
- 原文 PDF：`Drinfeld_1974_elliptic_modules.pdf`，SHA-256 = `95f17bfb606dd63c8068c4a257f080590f3ed349910e25aa2f96f15b707d63a9`（本 session 实测，与派发单一致）。
- 被检 Markdown 基线：`Drinfeld_1974_elliptic_modules_mineru/Drinfeld_1974_elliptic_modules__Drinfeld_1974_elliptic_modules.md`，SHA-256 = `77dc542b8a3bd71ab217dc55c6c9801088886ca7bf5bdf92e93f8ba090a75825`（= Luna 修复后的当前态，本 session 实测；原始 mineru 产出见提交 0b0f3dd）。
- 文本层判定（2026-10-02 14:47 EDT，`pdftotext -f 1 -l 1 Drinfeld_1974_elliptic_modules.pdf -`）：**可用**，首页能提取完整英文正文（Math. USSR Sbornik 译本排版文本层，exit 0）。因此本篇采用**双通道主对账**：150dpi pngmono 页图为主证（公式、上下标、字形一律以页图裁决），pdftotext 文本层为副证（定位与散文比对）。文本层在数学区有系统性乱码（如 `<*>`→∞、`A;`→k∞、`d- 2`→d=2），不得以文本层覆盖页图判断。
- 证据图目录：`audit-redo/`（本篇 redo 专用；不动 Luna 旧 `audit/`）。
- 本批次范围：PDF p.1–p.9（印刷 p.561–569）。逐页流程 = gs pngmono 150dpi 渲染 → Read 目检 → 与 MD 对应段五点比对（题录/节标题顺序/定理编号与陈述/公式与上下标/记号）→ 分级 → 内容错误用结构化 Edit 逐处修复（含修正 Luna 旧修复中的错误；print quirk 忠实登记不改）→ 本文件落签 → 仅本篇路径 git add + commit（subject 前缀 `redo(page):`）。

## p.001（PDF p.1 / 印刷 p.561）

- PNG：audit-redo/p001.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p001_abstract.png、…_p001_adele.png、…_p001_adele_glyph600.png（600dpi）
- 核对：题录（题名/UDC/作者/摘要/Bibliography 14 items/AMS 分类脚注）、Introduction A) 开头、admissible triple 定义与四类、记号段（A、adèle 环、𝔘_f）。
- 结果：FAIL。记号段（MD 行 29）：印刷以 600dpi 定裁为 Fraktur **𝔘**（全 adèle 环）与 **𝔘_f**（去 ∞ 分量），当前 MD 写作正体 `U` 与 `$\mathfrak{A}_f$`；`\mathfrak{A}` 在本篇记号系统中未定义，属记号身份错误（Luna 旧签字仅记"页眉/页码未收"未察）。已 Edit 修复为 `$\mathfrak{U}$ … $\mathfrak{U}_f$`。旁证：pdftotext 文本层第 34–35 行 ABBYY 亦识别为 U 形（`U`/`v-`）。
- 重核 Luna 修复：摘要 `GL(2,Q)`（300dpi 确认斜体 GL）、"main result"（无 s）、`d \leq [\overline{k}_{\infty}:k_{\infty}]`、四类 triple、`$\zeta$-functions` 均与页图相符，无 Luna 引入的错误。
- 另记（PASS± 级伪影，不改）：期刊页眉两行、印刷页码 561、Copyright 行未收；triple 1)/2) 行尾分号在 MD 中脱落。
- ⚠ 跨页待查（本批次外）：p.018/p.025/p.031 Luna 将 MD 的 `𝔘_f` 改为 `𝔄_f` 的方向与 p.561 记号定义冲突，p.10–32 批次须以原页重裁核定。

## p.002（PDF p.2 / 印刷 p.562）

- PNG：audit-redo/p002.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p002_GLdf.png（GL(d,𝔘_f) 与 Theorem 1 𝔘_f^*）、…_p002_GL2U.png（Theorem 2 2) 与 GL(2,𝔘)）
- 核对：elliptic A-module of rank d 定义、level I 结构定义、N_I/N=lim← 段、Theorem 1、Theorem 1) 2) 两项、d=1,2 过渡段、B) Outline 至 §9、cusp form 编辑注。
- 结果：FAIL。adèle 环记号 4 处：MD 行 41 `GL(d,\mathfrak{A}_f)`、行 43 `\mathfrak{A}_f^*`、行 45 `GL(2,\mathfrak{A}_{f})`、行 49 `GL(2,\mathfrak{A})`，印刷均为 Fraktur **𝔘**（U 形，与 p.561 记号定义一致；300dpi 逐处核验）。已 Edit 逐处改为 `\mathfrak{U}_f` / `\mathfrak{U}`。
- 重核 Luna 修复：Theorem 2 陈述结构（H^1(N̄,Q̄_l)≃⊕_i U_i⊗W_i、U_i=⊗U_i^p、Gal(Q̄_p/Q_p)）、1) 中 L(s,W_i^p)=L(s−1/2,Û_i^p)、2) 中 Hom_{GL(2,R)}(Π,A_0)、P_1(R)、Outline 的 Ω^d/§§1 and 4/[14] 均与页图相符，无 Luna 引入的错误。
- 另记（PASS± 级伪影，不改）：页眉 "562 V. G. DRINFEL'D" 未收。
