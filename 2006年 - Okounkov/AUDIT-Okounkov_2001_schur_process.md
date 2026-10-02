# AUDIT — Okounkov_2001_schur_process

> 论文：A. Okounkov, N. Reshetikhin, *Correlation function of Schur process with application to local geometry of a random 3-dimensional Young diagram*（arXiv:math/0107056v3，2003-01-31 版，35 页）。
> actor=Wf-P10；host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）。
> PDF SHA-256 = 83bd21a169bc03393390b95428324eec8a9511cefa1df7968bd48c4fa5bde4f1。
> MD 基线 SHA-256 = ad6a88a9e361adf0407b097ab68b5c4f158506460d0a4c245fc7b1ab623a846d。
> 审计开始：2026-10-02 13:39 EDT。
> 文本层判定：`pdftotext -f 1 -l 1` 首页输出完整可读 → **文本层可用**，全程采用「文本层主对账 + PNG 视觉核验」双通道。
> 分级与格式遵循 worktree 根 `AUDIT-SOP.md`「流程（每页 7 步）」「审计说明格式」「审计后修复」三节；本篇审计 p.1–p.35，本块覆盖 p.1–p.9。

---

## p.001（PDF p.1 / 印刷 p.1）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：题录（标题/作者/脚注邮箱）、Abstract 全文、§1、§1.1、§1.1.1 首句
- 结果：PASS。标题、作者 "Andrei Okounkov and Nikolai Reshetikhin∗"、Abstract 逐句、节标题顺序、§1.1.1 首句与脚注全部吻合。印刷原样 quirk 忠实保留于 md：错字 "weights a partitions λ"、邮箱 "reshetik@math.berkeley.edu"（印刷即如此，非 md 错）。
- 备注：mineru 把该页脚注排版为 docvortex-page-footnote 样式块，属导出格式非内容错误；相邻处 "where$s _ { \lambda }$" 缺空格为 mineru 排版级伪影，不妨碍阅读，不按 quirk 改。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：§1.1.1 续（Schur process 序列式与 Prob∝∏𝕊^(t) 式）、§1.1.2 全节、𝔖({λ(t)}) 定义式、行列式式 det(K(u_i,u_j))
- 结果：PASS±（两处 mineru 伪影已修复，见下）。正文与公式全部吻合：𝕊^(t)(λ(t),λ(t+1)) 无 ∏ 下标（印刷如此）、𝔖 定义式 t,i∈Z（斜体 Z，印刷如此）、U⊂ℤ×(ℤ+½) 黑体 Z 均与 md 一致。
- 修复：① md 行 19 `{<sup>λ(t)</sup>} <sup>such</sup> <sup>that</sup>` → `{λ(t)} such that`——p.002.png 显示 "such that" 为正常正文字号，非上标；② md 行 39 `$U \subset \mathbb { Z } \times ( \mathbb { Z } + { \frac { 1 } { 2 } } )$` 句末补印刷原页的句号。
- 备注：印刷 quirk 忠实保留不改：语法瑕疵 "This determinants can be also interpreted"、"Our main interest in this paper are"。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：§1.2/§1.2.1/§1.2.2 节标题顺序、公式 (1)（Prob(π)∝q^{|π|}, 0<q<1）、引文编号 [3]/[19]/[2,4,5,13]/[14]/Conjecture 13.5 in [5]
- 结果：PASS。全部吻合；印刷 quirk 忠实保留："correlation functions asymptotics"、"of π, is a particular specialization"、"certain rhombi tiling"、"plane partition, is an old subject"。
- 备注：md 行 63 "$\operatorname { A s } q \to 1$" 将 "As" 放入 math operator，排版级伪影（渲染为直立体 As，与印刷一致观感），不改。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：§1.2.3 全节、§1.3 Universality、§1.4 Acknowledgments（NSF DMS-0096246/DMS-0070931、CRDF RM1-2244）、§2/§2.1 节标题
- 结果：PASS±（一处内容错误已修复）：md 行 75 "We compute the q  1 limit" 丢失箭头，印刷原页为 "the q → 1 limit"（p004.png 第 2 段首行清晰可见）→ 修复为 "$q \to 1$"。
- 备注：其余文字、资助号、节标题顺序、引文编号（(24)/Corollary 1/Theorem 2/Section 3.1.12/[5]/[1]/[10]/[9]/Section 3.2.3）全部吻合。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：§2.1.1（分划定义式 λ=(λ₁≥λ₂≥λ₃≥⋯≥0)、∅ 记号、[15]）、Schur process 序列式 {λ(t)}, t∈ℤ、§2.1.2 平面分划定义、(x,y)↦π_{⌈x⌉,⌈y⌉}、矩阵 (2)（rows 5 3 2 1 / 4 3 1 1 / 3 2 1 / 2 1）
- 结果：PASS±（两处内容错误已修复）：① md 行 101 "denoted by ." 丢失 ∅（p005.png 明示 "denoted by ∅."）→ 补 "$\varnothing$"；② md 行 109 "diferent"——pdftotext 文本层与 p005.png 均为 "different"，系 mineru 丢 ff 连字伪影（非印刷 quirk）→ 改 "different"。
- 备注：全文文本层预检确认印刷自身 quirk "of the of the"（§2.1.3，后页核）与 "probablistic"（§2.2.6）为印刷原样，md 忠实保留不改；其余 ff 词（coeficient/sufices 等）待到所在页逐一对照后处理。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：audit/p006.png（pngmono 150dpi）
- 核对：Figure 1（3D diagram π 图与题注）、对角切片式 (3)（λ(t)=(π_{i,t+i}), i≥max(0,−t)）、interlacing 条件 (4)、interlace 定义 λ₁≥μ₁≥λ₂≥μ₂≥λ₃≥…、示例链 (2)≺(3,1)≺(4,2)≺(5,3,1)≻(3,1)≻(2,1)≻(1)、§2.1.3 𝔖(λ) 映射与 |𝔖∖(ℤ+½)<0|=|(ℤ+½)<0∖𝔖|<∞
- 结果：PASS±（一处已修复）：md 行 161 "the configuration λ(t)" 丢花括号，印刷原页为 "the configuration {λ(t)}"（p006.png 可见）→ 补 "$\{ \lambda ( t ) \}$"。
- 备注：印刷 quirk "is a bijection of the of the set of partitions"（p006.png 与文本层 line 264 双证）忠实保留；Figure 1 图片引用 images/page_5_image_0.jpg 存在且可解析（mineru 内部页索引命名，非 md 错误）。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：audit/p007.png（pngmono 150dpi）
- 核对：映射 (5)（{λ(t)}↦𝔖({λ(t)})⊂ℤ×(ℤ+½)）、Figure 2（点场与非相交路径图及题注）、§2.2/§2.2.1、Prob∝∏_{t∈ℤ}𝕊^(t)(λ(t),λ(t+1)) 式
- 结果：PASS。公式、编号 (5)、∏ 下标 t∈ℤ、图题注全部吻合；图片引用 images/page_6_chart_4.jpg 存在可解析。
- 备注：印刷原文两处均写 "as in Figure 2"/"shown in Figure 2"（第二句亦指 Figure 2，印刷如此）忠实保留；行 187 句末无句号与印刷一致。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：audit/p008.png（pngmono 150dpi）
- 核对：§2.2.2（φ(z)=Σ_{k∈ℤ}φ_k z^k、winding number 0/geometric mean 1 条款）、§2.2.3（X={x_i},Y={y_i}∈𝔖、无限行列式 (6) det(φ_{y_i−x_j})）、§2.2.4 Wiener-Hopf 分解 φ(z)=φ⁺(z)φ⁻(z)
- 结果：PASS±（三处 ff 连字丢失已修复，文本层+PNG 双证）：① 行 207 "coeficient"→"coefficient"；② 行 233 "diferent regularizations difer"→"different regularizations differ"；③ 行 235 "diferent"→"different"。
- 备注：公式、节编号、tag (6) 全部吻合；"well defined"（无连字符）与印刷一致。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：audit/p009.png（pngmono 150dpi）
- 核对：φ^{±}(z)=1+Σ_{k∈±ℕ}φ_k^{±}z^k、Jacobi-Trudy 式 det(φ^+_{λ_i−μ_j+j−i})=s_{λ/μ}(φ^+)、specialization (7) h_k=φ_k^+、(8) s_{λ/μ}(φ^+)=0 (μ⊄λ)、Definition 1 与 (9) S_φ(μ,λ)=Σ_ν s_{μ/ν}(φ⁻)s_{λ/ν}(φ⁺)、h_k=φ⁻_{−k}、Cauchy-Binet 段与 (φ_{i−j})=(φ^+_{i−j})(φ^−_{i−j})
- 结果：PASS±（两处已修复）：① md 行 276 (9) 式左端 "S _ {\phi}" 被拍平为斜体 S，印刷（p009.png Definition 1 公式）为无衬线 𝕊_φ，且 md 式 (10) 等处均作 \mathsf{S}，内部不一致 → 改 "\mathsf {S} _ {\phi}"；② 行 291 句末补印刷原页句号（"…ν such that ν ⊂ µ, λ."）。
- 备注：印刷 quirk "the meaning of (6) in unambiguous"（应为 is，印刷原样，PNG+文本层双证）忠实保留；行 253 "$\phi ^ { - } ( z ) = 1 \ : ( \mathrm { o r } \ : \phi ^ { + } ( z ) = 1 )$" 的 "\ :" 空距伪影为 mineru 排版级伪影，内容无误，不改。
