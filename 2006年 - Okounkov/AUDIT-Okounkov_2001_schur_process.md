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

## 本块（p.001–p.009）修复后复核收据

- 全文复读：本块 11 处修复后重读整份最终 Markdown（1297 行），逐项核对每处修改与对应页 PNG/文本层证据一致，未发现原定修复遗漏，未引入新差异。
- 只读脚本清点：`\tag` 共 42 个，编号 1–43 连续但缺 `\tag{22}`——p.14 印刷将 Theorem 1 生成函数拆编为 (21)/(22)，mineru 丢失 (22) 的公式体（md 行 613 孤立 "(22)"、行 615 Φ 函数名拍平为 `$\boldsymbol { \mathrm { { } } } ^ { \mathrm { { } } } \dot { \boldsymbol { \mathrm { { } } } } ( t , z )$`），属 p.14 块待修项，不在本块越页修改。
- 本块区（md 行 1–291）grep 无残余 "diferent/coeficient/sufices/difers" 伪影；全文同类残余 10 处均位于 p.10+（行 303/311/329/361/375/391/549/641/945/1093），已留待后续页块按页修复。
- 脚注样式块外无残余 `<sup>` 正文伪影；7 个 `images/` 引用全部存在可解析。
- 分级统计（本块）：PASS 3（p.1/3/7）、PASS± 6（p.2/4/5/6/8/9）、FAIL 0。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：audit/p010.png（pngmono 150dpi）
- 核对：§2.2.6 全节（Γ±(φ)=exp(Σ_{k=1}^∞(log φ)_{∓k}α_{±k})、(log φ)_k=p_k/k、(Γ₋(φ)v_μ,v_λ)=s_{λ/μ}(φ⁺)、式 (10) 𝕊_φ(μ,λ)=(Γ₋(φ)Γ₊(φ)v_μ,v_λ)、式 (11) 交换关系）、§2.2.7 开头（φ[m](z)=Σ_{k∈ℤ}φ_k[m]z^k）
- 结果：PASS±（4 个 ff 连字伪影已修复，PNG+文本层双证）：行 303 "coeficient"→"coefficient"；行 311 "coeficient"→"coefficient"；行 329 "diferent…diferent…difer"→"different…different…differ"。
- 备注：印刷 quirk "probablistic applications"（p010.png 与文本层 line 530 双证印刷原样）忠实保留；式 (10)(11) 编号与 𝕊 无衬线记号与印刷一致。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：audit/p011.png（pngmono 150dpi）
- 核对：Σ_{m∈ℤ}log φ[m](z) 收敛假设、Definition 2（Prob=(1/Z)∏_{m∈ℤ+1/2}𝕊_{φ[m]}(...））、Z 求和式、§2.2.8、式 (12)（时间有序积 ∏^←）、式 (13)（Γ₊(φ)v_∅=v_∅）、Z=exp(Σ_{m1<m2}Σ_k k(log φ[m1])_k(log φ[m2])_{−k})
- 结果：PASS±（三处已修复）：行 361、行 375 "coeficient"→"coefficient"（p011.png+文本层双证）；行 381 句末补印刷原页句号（p011.png 末行 "ensure the convergence of Z."）。
- 备注：(12) 式 md 中 Γ 项间多余空段为排版伪影不改；∏^←、v_∅ 记号与印刷一致。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：audit/p012.png（pngmono 150dpi）
- 核对：§2.2.9 式 (14)（Prob(λ(t)=μ)∝s_μ(∏_{m<t}φ⁺[m])s_μ(∏_{m>t}φ⁻[m])）、Schur measure [16] with parameters (14)、§2.2.10（{t_k}⊂ℤ、{λ̃(k)}={λ(t_k)}、φ̃[l]=∏_{t_{l−½}<m<t_{l+½}}φ[m]）、§2.2.11 开头（𝓛(z,s), s∈ℝ）
- 结果：PASS±（一处两修）：行 391 "coeficient"→"coefficient"（p012.png+文本层双证）且句末补印刷句号（p012.png "φ⁺[m](z) over m < t."）。
- 备注：行 415 "t_k 's" 的 mineru 上标排版伪影（${}'$）内容可读不改；印刷 quirk "with parameters (14)"（参数实为 φ[m]，印刷如此）忠实保留。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：audit/p013.png（pngmono 150dpi）
- 核对：连续时间参数式 φ[m](z)=exp(∫𝓛(z,s)ds)、§2.2.12（𝔐_q、Prob(π)∝q^{|π|}）、式 (15)（φ_{3D}[m] 分段定义）、h_k=c^k 特化与 s_{λ/μ} 分段式、𝕊_{φ_{3D}[m]} 分段式（m<0 ≺ / m>0 ≻ / otherwise 0）、q^{Σ|λ(t)|}=q^{|π|}
- 结果：PASS。公式结构、分段条件、编号 (15)、𝔐_q 花体记号全部吻合。
- 备注：md 行 456 分段式内 "m <   0," 双空格为 mineru 排版伪影不改。
