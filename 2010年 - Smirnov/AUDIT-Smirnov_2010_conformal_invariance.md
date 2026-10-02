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

## p.002（PDF p.2 / 印刷 p.2）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：目录续 §7（7.1–7.3）、§8（8.1–8.5）及页码；§1 Introduction 开篇（Lenz-Ising 史、[Len20]/[Isi25]/[Hei28]/[Pei36]/[KW41a, KW41b]）；公式 Hamiltonian E_Λ(σ) ∶= −∑_{x∼y} σ_x σ_y、µ_{β,Λ}(σ) ∶= e^{−βE_Λ(σ)}/Z_{β,Λ}、Z_{β,Λ} ∶= ∑_{σ̃∈{−1,1}^Λ} e^{−βE_Λ(σ̃)}；页脚印刷页码 2。
- 结果：FAIL——MD 无任何对应段（整文档错源为 Arnlind 等），以原图为准。
- 备注：文本层与 PNG 双通道一致；公式中 ∶= 冒号等号、下标 β,Λ 与指数 −βE_Λ(σ) 印刷清晰，后续重导出时按此对账。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：Figure 1（三幅 Ising 构型图，pngmono 下呈半调网纹）及图注 "Ising configurations at β < β_c, at β = β_c, and β > β_c respectively."；Onsager/Yang/McCoy-Wu/Lieb-Baxter/Fisher-Kasteleyn/Kac-Ward 历史段；脚注 1（"This result represented a shock for the community…"）；引文 [Ons44][KO50][Yan52][MW73][Pal07][Lie67, Bax89][Fis66, Kas61][KW52][She60][Vdo65][DZM+99, Cim10][Fis98]；页脚印刷页码 3。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：Figure 1 为位图插图，pngmono 150dpi 下仅见网纹属正常二值化现象；后续 MinerU 重导出需保留该图并抽 300dpi 复核图注 β 关系方向。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：universality/CFT 段与引文 [PP66, Kad66][BPZ84b, BPZ84a][ISZ88][Sch00]；Dobrushin boundary conditions 段（Ω_δ ⊂ δZ²，arcs ∂_ab/∂_ba，+1/−1 自旋固定）；斜体预测展示式 "For any (Ω,a,b) and any conformal map ψ ∶ Ω → C, the random curve ψ ○ γ_(Ω,a,b) has the same law as γ_(ψ(Ω),ψ(a),ψ(b))"；SLE(κ) 定义（driving process √κ B_t，(B_t) standard Brownian motion）；脚注 2 "i.e. one-to-one holomorphic maps"、脚注 3 "In fact the interface is not unique…"；页脚印刷页码 4。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：印刷 quirk 登记——脚注 3 末 "the closest interface to ∂_ab" 的下标 ab 排印位置偏高（近乎上标位），文本层提取为 "to ∂\nab"；重导出对账时按此原样登记，不作"改正"。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：Figure 2 及图注 "An interface between + and − in the Ising model."；Main result 1 (Theorem 2.10) critical Ising → SLE(κ=3)；Main result 2 (Theorem 3.13) critical FK-Ising → SLE(κ=16/3)；[LPSA94] 数值实验段、Cardy's formula [Car92]、Smirnov [Smi01]；crossing probability 记号 C_δ(Ω,A,B,C,D)；页脚印刷页码 5。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：两条 Main result 的定理编号（2.10/3.13）与 κ 值（3 与 16/3）为后续重导出对账的关键锚点；文本层与 PNG 双通道一致。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：audit/p006.png（pngmono 150dpi）
- 核对：fermionic observable 段（Definition 2.9、Theorem 2.11）；discrete complex analysis 应用段及引文 [Ken00][Lov04][Ste05][Mer01][BS08]；Acknowledgments 整段（Búzios, Brazil, August 2010 Clay Mathematics Institute Summer School；致谢 Sidoravicius/Benoist/Cimasoni/Hammond；资助 EU Marie-Curie RTN CODY、ERC AG CONFRA、Swiss FNS、RF Government grant 11.G34.31.0026）；§1.1 Organization of the notes 开篇（Section 2/3 概述）；页脚印刷页码 6。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：Acknowledgments 为重导出对账的高风险段（人名地名带重音：Búzios、Stéphane；长资助编号 11.G34.31.0026），文本层与 PNG 双通道逐项一致。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：audit/p007.png（pngmono 150dpi）
- 核对：§1.1 续（Section 4–8 概述，含 s-holomorphic/spin-holomorphic 与 Loewner chains 表述）；§1.2 Notations；§1.2.1 Primal, dual and medial graphs——rotated square lattice L 顶点集 e^{iπ/4}Z²、边 [xy]、x ∼ y、primal graphs、boundary ∂G（<4 邻居）、dual graph G⋆ 与 L⋆（无限面不对应对偶点）、medial lattice L◇ 与 medial graph G◇、L◇ 为 L 旋转 1/√2 缩放、black/white faces、L◇ 边绕 black faces 逆时针定向；§1.2.2 Approximations of domains——√2δL 记 L_δ（mesh-size √2δ）、L◇_δ（mesh-size δ）、Ω_δ = Ω ∩ L_δ；页脚印刷页码 7。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：印刷 quirk 登记——"Note that L◇ is" 处菱形上标基线略下沉（PNG 与文本层断行 "vertices of L ◇ / √ corresponding…" 均可见）；√2δ 的根号覆盖范围以 PNG 为准（只盖 2）。重导出对账时 L/L⋆/L◇ 的星号与菱形记号需逐个核对。
