# AUDIT — Okounkov_2001_schur_process

> 论文：A. Okounkov, N. Reshetikhin, *Correlation function of Schur process with application to local geometry of a random 3-dimensional Young diagram*（arXiv:math/0107056v3，2003-01-31 版，35 页）。
> actor=Wf-P10；host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）。
> PDF SHA-256 = 83bd21a169bc03393390b95428324eec8a9511cefa1df7968bd48c4fa5bde4f1。
> MD 基线 SHA-256 = ad6a88a9e361adf0407b097ab68b5c4f158506460d0a4c245fc7b1ab623a846d。
> 审计开始：2026-10-02 13:39 EDT。
> 文本层判定：`pdftotext -f 1 -l 1` 首页输出完整可读 → **文本层可用**，全程采用「文本层主对账 + PNG 视觉核验」双通道。
> 分级与格式遵循 worktree 根 `AUDIT-SOP.md`「流程（每页 7 步）」「审计说明格式」「审计后修复」三节；本篇审计 p.1–p.35，本块覆盖 p.1–p.9。

---

## 总评（全篇 35 页审计完成后补记）

- **覆盖声明**：本篇 p.1–p.35 全部 35 页逐页审计完成（非抽查、全页覆盖），每页均执行「gs pngmono 150dpi 渲染 → PNG 目检 → pdftotext 文本层主对账 → 五点比对 → 落签 → 逐页 commit」；图片证据 audit/p001.png–p035.png 共 35 张随审计提交。
- **分级统计**：PASS 11（p.1/3/7/13/14/16/24/26/29/33/35）、PASS± 23、FAIL 1（p.17——Theorem 1 生成函数 (22) 公式体与编号被 mineru 整体丢失，已按 p017.png 修复，见修复登记）。
- **系统性 mineru 瑕疵（均已逐页按原图证据修复）**：① ff 连字丢失（coefficient/different/differ/differences/suffices/Wulff 等，共 15 处）；② "→" 箭头丢失或变形为 "~ ~"（r→+0、N→∞、q→1 等，共 8 处）；③ 句末句号丢失（10 处）；④ 花括号 {λ(t)} 丢失（2 处）；⑤ ∅ 字形丢失（1 处）；⑥ (21)/(22) 双编号公式被合并致 (22) 丢失（1 处，FAIL 级）；⑦ 记号拍平（𝕊→S、𝔹 mathtt、ℜ 丢失、基向量 k 下划线丢失，共 5 处）；⑧ 重音分解 Poincar´e（1 处）；⑨ Figure 5 题注丢逗号、γ< 后多余 <sub> 伪影、双逗号（3 处）。累计修复约 52 处，全部有页级 PNG/文本层双证。
- **印刷 quirk 清单（忠实保留不改，均有 PNG 证据）**："weights a partitions λ"、邮箱 "reshetik@math.berkeley.edu"、"This determinants can be also interpreted"、"a bijection of the of the"、"probablistic"、"the meaning of (6) in unambiguous"、"correlation functions asymptotics"、"certain rhombi tiling"、"of π, is a particular specialization"、"in the Figure 3"、"equivalent to following parametrization"、"the points of the intersection of γ> and γ< the minima"（缺 are）、"the limit correlation are trivial"、"with parameters (14)"、v_λ 中 "λ_4−5/2"（印刷 typo）、"see the formula"、References 中 "transfer-impendances"/"condmat/0212456"/"math.ph/0006020"/"Pacific J. Math 9"。
- **mineru doc_id**：UNKNOWN——导出文件 middle_json.json 与 structured_content.json 中均无 doc_id 字段。
- **修复登记**：唯一 FAIL（p.17 (22) 公式体与编号丢失）已在该页审计 commit `32f8def8` 内按 p017.png 修复（拆分 tag{21}/tag{22}、删孤立 "(22)" 残行、恢复 Φ 函数名、修 if 伪影补句号）；原始 mineru md 基线见 commit `0b0f3dd2`（SHA-256 = ad6a88a9e361adf0407b097ab68b5c4f158506460d0a4c245fc7b1ab623a846d）。PASS± 级排版伪影按 SOP 默认不批量改（仅妨碍阅读/检索的内容级错误逐处修复），登记在各页条目备注。
- **收稿日期**：本 PDF 为 arXiv 版（math/0107056v3, 2003-01-31），印刷无收稿日期栏，无从核对，非缺失。

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

## p.014（PDF p.14 / 印刷 p.14）
- PNG：audit/p014.png（pngmono 150dpi）
- 核对：Z_{3D}=exp(Σ_{m1,m2=1/2}^∞Σ_k q^{k(m1+m2)}/k)=∏_{m1,m2}(1−q^{m1+m2})^{-1}=∏_{n=1}^∞(1−q^n)^{-n}（McMahon）、§2.3/§2.3.1、Definition 3、ρ(U)=Prob(U⊂𝔖({λ(t)}))、式 (16)、§2.3.2（u_i 排序 t1≤t2≤…≤tn、t_0=−∞）、式 (17)
- 结果：PASS。全部吻合；上块移交的 (22) 缺失问题位于 Theorem 1（§2.3.4），不在本页，待后续页处理。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：audit/p015.png（pngmono 150dpi）
- 核对：R_U 算子（双重 ∏^← 嵌套）、§2.3.3、Ψ_x(t)=Ad(∏_{m>t}Γ₊(φ[m])∏_{m<t}Γ₋(φ[m])^{-1})·ψ_x、ρ(U)=(←∏Ψ_{x_i}(t_i)Ψ*_{x_i}(t_i)v_∅,v_∅)、Lemma 1 (Wick formula) 与式 (18)、K_A(i,j) 分段、K((t1,x1),(t2,x2)) 分段式
- 结果：PASS±（一处已修复）：行 549 "sufices"→"suffices"（p015.png+文本层双证，ff 连字丢失）。
- 备注：行 549 "$A _ { i } \mathrm { ^ { * } s }$/$A _ { j } ^ { * } \mathrm { { ^ { s } } }$" 撇号排版伪影（印刷为 A_i's / A_j^*'s）数学无损、可辨认，登记不改；Lemma 1 斜体排版（Let/Then/Proof 斜体）为 LaTeX 强调，非错误。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：audit/p016.png（pngmono 150dpi）
- 核对：t₁≠t₂/t₁=t₂ 反对易注记段、§2.3.4、式 (19)（ψ(z)、ψ*(z) 生成元）、Ψ(t,z)=Ad(...)·ψ(z)、Ad(Γ±(φ)) 两关系、Ψ=Φψ 与 Ψ*=Φ^{-1}ψ、式 (20)（Φ(t,z)=∏_{m>t}φ⁻[m](z^{-1})/∏_{m<t}φ⁺[m](z^{-1})）、(ψ(z)ψ*(w)v_∅,v_∅)=√(zw)/(z−w) 两式及 |z|>|w|、|z|<|w| 条件
- 结果：PASS。全部吻合；PNG 确认 (20) 编号位于 Φ 定义式右侧，与 md tag{20} 一致（pdftotext 将编号提取至页末属阅读顺序伪影，以 PNG 为准）。

## p.017（PDF p.17 / 印刷 p.17）
- PNG：audit/p017.png（pngmono 150dpi）
- 核对：Theorem 1（ρ(U)=det(K(u_i,u_j))、生成函数 (21)/(22)）、§2.3.5、式 (23)（Φ_{3D}）、式 (24)（(z;q)_∞ 量子 dilogarithm）、Φ_{3D} 的 (q^{1/2}/z;q)_∞/(q^{1/2+t}z;q)_∞ 分段式
- 结果：FAIL→已修复（本页为上块移交的 (22) 缺失问题所在页，修复后内容与印刷一致）。修复 4 处（均以 p017.png 为准）：① md 行 609–611 印刷为两个连续编号公式——(21) 𝕂_{t1,t2}(z,w)=Σ_{x1,x2∈ℤ+½}z^{x1}w^{−x2}K((t1,x1),(t2,x2))，(22) 其等号续行 =√(zw)/(z−w)·Φ(t1,z)/Φ(t2,w)——mineru 将两行挤入单 tag{21} array 且丢失 (22) 编号 → 拆分为 tag{21} 与 tag{22} 两个独立公式（左端 𝕂 无衬线 \mathsf K 保留）；② 删除孤立 "(22)" 残行（原行 613，mineru 丢公式体的残骸）；③ 原行 615 函数名拍平 "$\boldsymbol{\mathrm{}}^{\mathrm{}}\dot{\boldsymbol{\mathrm{}}}(t,z)$" → "$\Phi ( t , z )$"（PNG：Here the function Φ(t,z) is defined by (20)）；④ 同句 "\ i f" 伪影改 "if" 并补印刷句号（PNG 句末 "if t_1 < t_2."）。
- 备注：修复后 (21)(22) 编号连续，全文 \tag 恢复 1–43 完整（见本块收据清点）；(23)(24) 与分段式核对无误。

## p.018（PDF p.18 / 印刷 p.18）
- PNG：audit/p018.png（pngmono 150dpi）
- 核对：§2.3.6、𝔖̃(π)={(j−i, π_{ij}−(i+j−1)/2)}、式 (25)（(x,y,z)↦(t,h)=(y−x, z−(x+y)/2)）、Figure 3（水平瓦片图与题注）、𝔖̃(π)⊂ℤ×½ℤ、(t,h)∈𝔖̃(π)⟺(t,x+|t|/2)∈𝔖({λ(t)})
- 结果：PASS±（两处已修复）：① 行 641 "diferent"→"different"（p018.png+文本层双证，ff 连字）；② 行 671 "if λ(t) corresponds" → "if $\{ \lambda ( t ) \}$ corresponds"（p018.png 印刷有花括号，与 p.006 同类 mineru 丢括号）。
- 备注：Figure 3 图片引用 images/page_17_chart_8.jpg 存在；题注 "corresponding to diagram in Figure 1"（无 the，印刷如此）忠实一致。

## 本块（p.010–p.018）修复后复核收据

- 全文复读：本块 13 处修复后重读整份最终 Markdown（1299 行），逐项核对每处修改与对应页 PNG/文本层证据一致，未发现原定修复遗漏，未引入新差异。
- 只读脚本清点：`\tag` 恢复 43 个、编号 1–43 完整（p.017 修复使 \tag{22} 回归，(21)/(22) 相邻结构见行 610/614）；全文残余 ff 伪影仅剩 p.19+ 两处（行 947 "diferences"→Theorem 2 所在 p.24、行 1095 "difers…diferent"→§3.1.14 所在 p.30），按页证据纪律留待后续页块；7 个 images/ 引用全部存在；audit/ 内 p001–p018 页图 18 张齐全。
- 分级统计（本块）：PASS 3（p.13/14/16）、PASS± 5（p.10/11/12/15/18）、FAIL 1（p.17，(22) 公式体与编号丢失，已在该页 commit 内按 p017.png 修复并复核）。

## p.019（PDF p.19 / 印刷 p.19）
- PNG：audit/p019.png（pngmono 150dpi）
- 核对：Corollary 1（Prob({(t_i,h_i)}⊂𝔖̃(π))=det[K_{3D}(...)]）、式 (26)（二重围线积分与 z^{h1+(|t1|+1)/2}w^{−h2−(|t2|−1)/2} 权重）、§3/§3.1/§3.1.1、式 (27)（∫_γ e^{MS(x)}dx→0）、§3.1.2 开头
- 结果：PASS±（一处已修复）：行 709 句末补句号（p019.png "for all but finitely many points x ∈ γ."）。
- 备注：印刷 quirk "how suitable is the formula (22)"、"a much wider variety of specialization"（无复数 s）忠实保留；K_{3D} 记号与 (26) 结构全部吻合。

## p.020（PDF p.20 / 印刷 p.20）
- PNG：audit/p020.png（pngmono 150dpi）
- 核对：Lemma 2（r³|π|→2ζ(3), r→+0）、𝔼|π| 推导链（q(d/dq)Z_{3D}/Z_{3D}=Σn²q^n/(1−q^n)=Σn²q^{nk}=Σq^k(1+q^k)/(1−q^k)³~2ζ(3)/r³）、Var|π|=o(r^{−6})、§3.1.3、rt_i→τ/rh_i→χ、Δt/Δh、τ≥0 对称性
- 结果：PASS±（四处箭头/符号丢失已修复，均 p020.png 双证）：① 行 713 "and$r  + 0$"→"and$r \to + 0$"；② 行 719 句末补句号（"sampled from the measure 𝔐_q."）；③ 行 735 证明末补印刷的 □ 符号；④ 行 739/741 "$r ~  ~ + 0$"→"$r \to + 0$"（mineru 将箭头 → 拍成 "~ ~"）。
- 备注：本页确认 mineru 存在系统性 "→" 丢失/变形伪影，后续页同类问题逐页对照修复。

## p.021（PDF p.21 / 印刷 p.21）
- PNG：audit/p021.png（pngmono 150dpi）
- 核对：§3.1.4、式 (28)（ln(z;q)_∞~r^{−1}∫ln(1−w)/w dw=−r^{−1}dilog(1−z)）、dilog 定义、S(z;τ,χ) 定义与解析域 cuts (0,1)/(e^τ,+∞)、式 (29)、临界点方程 (1−1/z)(1−e^{−τ}z)=e^{−τ/2−χ}、式 (30)/(31)
- 结果：PASS±（四处已修复，均 p021.png 双证）：① 行 755 "$r  + 0$"→"$r \to + 0$"；② 行 767 句末补句号（"(1,+∞)."）；③ 行 775 句末补句号（"(e^τ,+∞)."）；④ 行 777 "$r  + 0$"→"$r \to + 0$"。
- 备注：公式 (28)–(31) 全部吻合。

## p.022（PDF p.22 / 印刷 p.22）
- PNG：audit/p022.png（pngmono 150dpi）
- 核对：§3.1.5（S(z̄;τ,χ)=overline{S(z;τ,χ)}、S+S(e^τ/z)=−(τ/2+χ)τ、ℜS 在 γ 上常值 −(τ/2+χ)τ/2、z(d/dz)S=3τ/2−χ−ln|e^τ−z|²）、式 (32)、向量场 ∇(ℜS)=(z²/e^τ)(d/dz)S、§3.1.6 围线变形 ∫_{(1±ε)γ}dz∫_{(1∓ε)γ}dw、γ>,γ<,γ+,γ− 定义开头
- 结果：PASS±（一处已修复）：行 857 "the gradient of S" → "the gradient of$\Re S$"——p022.png 与文本层双证印刷为 "gradient of ℜS"，md 丢 ℜ。
- 备注：Figure 4/5 图片引用（page_22_image_0/2.jpg）在本页与下页交界，已验证文件存在；(32) 与圆交结构全部吻合。

## p.023（PDF p.23 / 印刷 p.23）
- PNG：audit/p023.png（pngmono 150dpi）
- 核对：整页插图页——Figure 4（γ 圆上 ℜS 梯度场，标注 z_c/z̄_c/γ/e^τ/e^{τ/2}/e^{3τ/4−χ/2}）与 Figure 5（γ> dashed、γ< dotted、γ± 弧与 θ* 角），两图题注
- 结果：PASS±（一处已修复）：Figure 5 题注 md 原为 "$\gamma _ { > } ( \mathrm { d a s h e d } )$$\gamma _ { < } ( \mathrm { d o t t e d } )$" 两 math 块相接无标点，p023.png 印刷为 "Contours γ>(dashed), γ<(dotted), and γ±" → 补 ", "。
- 备注：Figure 4 题注 "Gradient of ℜS(z) on the circle γ={|z|=e^{τ/2}}" 与 md 一致；图内标注与式 (32)/(33) 几何关系一致。

## p.024（PDF p.24 / 印刷 p.24）
- PNG：audit/p024.png（pngmono 150dpi）
- 核对：γ± 弧定义、K_{3D}=∫^{(1)}+∫^{(2)} 分解、∫^{(1)}=(1/(2πi)²)∫_{γ<}dz∫_{γ>}dw、∫^{(2)} 量子 dilog 比式、∫^{(1)}→0 (r→+0)、§3.1.7、(1−e^{−τ}w)^{Δt} 极限、w=e^τw′ 替换与 e^{−τ(Δh+Δt/2)} 前因子、Definition 4（𝔹_±(k,l;z)=(1/2πi)∫_z̄^z(1−w)^k w^{−l−1}dw，路径过 (0,1)/(−∞,0)）
- 结果：PASS。全部吻合；行 902/908 的 "r \rightarrow + 0" 箭头完整无缺。
- 备注：印刷 quirk "with the same integrand in as in (26)"（"in as in"，印刷原样）忠实保留；行 909 "e$- \tau ( \Delta h + \Delta t / 2 )$" 上标拆分为正文+math 的 mineru 排版伪影，内容可辨，不改；"\operatorname { i f }" 伪影不改。

## p.025（PDF p.25 / 印刷 p.25）
- PNG：audit/p025.png（pngmono 150dpi）
- 核对：§3.1.8（ℜS 在 γ< 上最大、(29)/(27) 引用）、§3.1.9、式 (33)（{z*,z̄*} 两圆交，ℑz*>0）、z* 延拓定义、式 (34)（分段）、Theorem 2 完整陈述与 det[𝔹_±(Δt_{ij}, Δh_{ij}+Δt_{ij}/2; z*)]
- 结果：PASS±（七处已修复，均 p025.png 双证）：① 行 923 "$\gamma _ { < }$" 后删 mineru 多余的 "<sub><</sub>"（印刷无重复字符）；② 行 925 "$z _ { c } ,$," 双逗号 → "$z _ { c }$,"；③ 行 941 "as$r  + 0$"→"as$r \to + 0$"；④ 行 947 "diferences"→"differences"（ff 连字，上块移交项之一，本页结清）；⑤ 行 951 "as$r  + 0$"→"as$r \to + 0$"；⑥ Theorem 2 主式 "\mathtt {B}"→"\mathsf {B}"（p025.png 与 Definition 4 同为无衬线 𝔹，统一 md 记号）；⑦ 行 957 句末补句号（"t_i − t_j ≥ 0."）。
- 备注："(33)and (34)" 缺空格为排版伪影不改；Theorem 2 斜体陈述为 LaTeX 强调。

## p.026（PDF p.26 / 印刷 p.26）
- PNG：audit/p026.png（pngmono 150dpi）
- 核对：Remark 1（[5] Proposition 8.5 / Conjecture 13.5）、Remark 2、§3.1.10、K_{3D}((t,h),(t,h))→ρ_*(τ,χ)（rt→τ, rh→χ）、Corollary 2（ρ_*=θ*/π）、式 (35)（θ*=arccos(cosh(τ/2)−e^{−χ}/2)）、等值线 θ*(τ,χ)=kπ/8, k=0..8
- 结果：PASS。全部吻合。
- 备注：印刷 quirk "the limit correlation are trivial"（correlation 单数，印刷原样）忠实保留。

## p.027（PDF p.27 / 印刷 p.27）
- PNG：audit/p027.png（pngmono 150dpi）
- 核对：Figure 6（密度等值线图与题注）、§3.1.11、Corollary 3（discrete sine kernel：det[sin(θ_*(h_i−h_j))/(π(h_i−h_j))], as r→+0）、§3.1.12、标准积分（β^k / −β^k / 0 分段）、|w−1|⋚e^{−τ/4−χ/2} 条件
- 结果：PASS±（一处已修复）：行 1007 "as$r  + 0$"→"as$r \to + 0$."（p027.png 印刷 "as r → +0." 有箭头有句号，md 两者皆缺）。
- 备注：行 1003 "$i f t _ { 1 } = t _ { 2 } = . .$." 的 if 进 math 与省略号断点为 mineru 排版伪影，内容可辨不改；𝔹_± 无衬线记号此处 md 已正确用 \mathsf。

## 本块（p.019–p.027）修复后复核收据

- 全文复读：本块 19 处修复后重读整份最终 Markdown（重点行 700–1039 区段及全文清点），逐项核对每处修改与对应页 PNG/文本层证据一致，未发现原定修复遗漏，未引入新差异。
- 只读脚本清点：grep 验证 "r ~  ~ + 0"/"r  + 0"/"diferences"/"<sub><</sub>" 全文零残余，"r \to + 0" 现共 8 处（含本块修复 6 处）；`\tag` 保持 43 个（1–43 完整）；残余 ff 伪影仅剩行 1095（§3.1.14 所在 p.30，下块）；7 个 images/ 引用齐全；audit/ 内 p001–p027 页图 27 张。
- 移交下块（p.028+）：① 行 1027 §3.1.12 正文 "$\mathtt { B } _ { \pm } ( k , l ; z _ { * } )$" 应为 $\mathsf{B}$（与 (36) 及印刷无衬线 𝔹 统一），该句印刷在 p.28，按页证据纪律未越页修改；② 行 1095 "difers…diferent"（p.30）；③ p.028 的 PNG 已渲染于 audit/p028.png（本块未提交，供下块使用）。
- 分级统计（本块）：PASS 2（p.24/26）、PASS± 7（p.19/20/21/22/23/25/27）、FAIL 0。本块系统性发现：mineru 大量丢失 "→" 箭头（变形为 "~ ~" 或直接丢失）与句末句号，均已逐页按 PNG 修复。

## p.028（PDF p.28 / 印刷 p.28）
- PNG：audit/p028.png（pngmono 150dpi）
- 核对：§3.1.12 结尾与式 (36)（𝔹_± 二重积分形式，|w|=e^{−τ/2}/|z|=e^{τ/4+χ/2}）、§3.1.13、式 (37)（z(τ,χ)=∫_{−∞}^χ(1−ρ_*(τ,s))ds）、式 (38)（z(τ,χ)=(1/π)∫_0^{π−θ*} s sin s ds/(cos s+cosh(τ/2))）、式 (39)（x/y 坐标）、§3.1.14 开头
- 结果：PASS±（两处已修复）：① 行 1027 "$\mathtt { B } _ { \pm } ( k , l ; z _ { * } )$"→"$\mathsf { B } _ { \pm } ( k , l ; z _ { * } )$"——p028.png 首行印刷为无衬线 𝔹_±(k,l;z*)，与式 (36) 及 Definition 4 统一（上块移交项①，本页结清）；② 行 1033 句末补句号（p028.png "where the plus sign corresponds to k ≥ 0."）。
- 备注：印刷 quirk "such as the one in the Figure 3"（多余 the，印刷原样）忠实保留；行 1057 "shown in Figure 7" 后无句号与印刷一致。

## p.029（PDF p.29 / 印刷 p.29）
- PNG：audit/p029.png（pngmono 150dpi）
- 核对：Figure 7（limit shape 3D 图与题注，引用 images/page_28_image_0.jpg 存在）、ρ_*(τ,χ)=(1/4π²)∬ du dv/(1+e^{χ/2+τ/4+iu}+e^{χ/2−τ/4+iv})、z(τ,χ)=(1/2π²)∬ ln|1+…| du dv、[3] 参数化 (x,y,z)=(f−2lnA, f−2lnB, f−2lnC)、f(A,B,C) 定义
- 结果：PASS。全部吻合。
- 备注：印刷 quirk "is equivalent to following parametrization"（缺 the，p029.png 确认）忠实保留。

## p.030（PDF p.30 / 印刷 p.30）
- PNG：audit/p030.png（pngmono 150dpi）
- 核对：§3.1.14 结尾（与 [3] 相差因子 2）、§3.2/§3.2.1（围线变形普遍原理）、§3.2.2（各向异性扰动 q^{|m|}→q^{V(m)}）、§3.2.3（Res_{z=w}(dz/(z−w))(Φ(t1,z)/Φ(t2,w))=1、∫^{(2)}=(1/2πi)∫_{γ±}dw/w^{Δx+1}）
- 结果：PASS±（两处已修复）：① 行 1095 "difers…diferent"→"differs…different"（p030.png+文本层双证，上块移交项②，本页结清）；② 行 1123 句末补句号（p030.png "in the variable Δx."）。
- 备注：印刷 quirk "the points of the intersection of γ> and γ< the minima of the function ℜS(z)"（缺 are，印刷原样）与破折号 "— on the other" 忠实保留。

## p.031（PDF p.31 / 印刷 p.31）
- PNG：audit/p031.png（pngmono 150dpi）
- 核对：§3.2.4（φ_Planch[m] 分段特化 e^{√αz}/e^{√αz^{−1}}/1、K_Planch 二重积分式）、§3.2.5（α→∞ 渐近、S_Planch=z−z^{−1}−(ξ/2)ln z、临界点 |ξ|<2 时 e^{±iθ}、θ=arccos(ξ/2)、K_Planch→sin(θΔ)/(πΔ)）
- 结果：PASS±（一处已修复）：行 1137 句末补句号（p031.png "see [1, 8]."）。
- 备注：Bessel/Bessel functions、poissonized 拼写与印刷一致；数学内容零差异。

## p.032（PDF p.32 / 印刷 p.32）
- PNG：audit/p032.png（pngmono 150dpi）
- 核对：§3.2.6（depoissonization、等价系综）、§3.2.7 与式 (40)（K 的系数提取式）、Airy 核恒等式、§3.2.8（[7] Airy process）、附录 A 开头（Λ^{∞/2}V、v_S=s₁∧s₂∧s₃∧…）
- 结果：PASS±（两处已修复）：① 行 1167 "as$N  \infty$"→"as$N \to \infty$"（p032.png 印刷 N → ∞，箭头丢失）；② 行 1191 "spanned by k"→"spanned by$\underline { k }$"——p032.png 印刷基向量 k 带下划线，md 附录他处（如行 1219）均用 \underline{{k}}，本处丢失。
- 备注：Airy 核公式与 (40) 的系数记号 [z^{x₁+m}w^{−x₂−m}] 全部吻合。

## p.033（PDF p.33 / 印刷 p.33）
- PNG：audit/p033.png（pngmono 150dpi）
- 核对：S₊/S₋ 有限性条件、Λ^{∞/2}V 内积与 {v_S} 正交基、v_λ=λ₁−1/2∧λ₂−3/2∧λ₄−5/2∧…、v_∅ vacuum、ψ_k 外乘定义 ψ_k(f)=k∧f、canonical anti-commutation、式 (41)（ψ_kψ*_k v_S 分段）、α_n 定义与 Heisenberg 关系 [α_n,α_m]=nδ_{n,−m}、式 (42)、式 (43)
- 结果：PASS。全部吻合。
- 备注：印刷 quirk 两处忠实保留：① v_λ 定义中 "λ_4−5/2"（按 wedge 序应为 λ_3，印刷 typo，md 原样保留）；② "see the formula"（无编号悬空引用，印刷原样）。

## p.034（PDF p.34 / 印刷 p.34）
- PNG：audit/p034.png（pngmono 150dpi）
- 核对：References [1]–[14] 逐条（作者/标题/刊名/卷期页年/arXiv 号）
- 结果：PASS±（两处已修复）：① [3] "Wulf"→"Wulff"——p034.png 印刷 "the Wulff crystal"（双 f），md 丢 ff 连字；② [13] "Poincar´e"→"Poincaré"——p034.png 印刷 "Ann. Inst. H. Poincaré"，md 重音分解伪影（妨碍检索）。
- 备注：印刷原样 quirk 忠实保留：[2] "transfer-impendances"（应 impedances）、[7] "condmat/0212456"（无连字符）、[9] "math.ph/0006020"、[12] "Pacific J. Math 9"（Math 后无点）——均与印刷逐字一致。

## p.035（PDF p.35 / 印刷 p.35）
- PNG：audit/p035.png（pngmono 150dpi）
- 核对：References [15]–[19] 逐条（Macdonald 1995、Okounkov Selecta Math. 7 (2001) 57–81 math.RT/9907127、Okounkov 2002 Kluwer、Praehofer-Spohn math.PR/0105240、Vershik 1997 Vienna talk）
- 结果：PASS。[15]–[19] 逐字吻合；本页为全文末页，页码 35 完整收尾。
- 备注：本 PDF 为 arXiv 版（math/0107056v3），印刷无收稿日期（received date）栏，无从核对，非缺失。

## 本块（p.028–p.035）修复后复核收据与全篇完结

- 全文复读：本块 9 处修复后重读整份最终 Markdown（1298 行），逐项核对每处修改与对应页 PNG/文本层证据一致，未发现遗漏，未引入新差异。
- 只读脚本清点（全篇终验）：ff 连字/箭头/伪影 grep 全文零残余；`\tag` 43 个（1–43 完整）；7 个 images/ 引用可解析；audit/ 内 p001–p035 页图 35 张齐全。
- 分级统计（本块）：PASS 3（p.29/33/35）、PASS± 5（p.28/30/31/32/34）、FAIL 0。上块移交两项均已在本块结清：行 1027 \mathtt→\mathsf（p.028）、行 1095 difers…diferent（p.030）。
- 全篇 35 页审计至此完成，总评见文件头；AUDIT-INDEX 登记与根级进度日志由 Master 集成时更新（Peer 不写根级）。

## 终验复读收据（full re-read receipt）

- **复读范围**：修复后完整重读最终 Markdown 全文 1298 行（前半 1–660、后半 660–1299），逐项回核全部修复与页面证据一致、原定修复无遗漏、无新差异。
- **终验发现并修复**：行 1139（p.31）"see [1, 8].." 双句号——系 p.031 补句号修复时 old_string 前缀匹配未吞原句号所致，位于前两块复读盲区，本次全文复读捕获，已修复为单句号（依据 p031.png 印刷 "see [1, 8]."）。除该处外无其他新差异。
- **抽查覆盖声明**：本篇非抽查，为全页审计——p.1–p.35 每页均经 pngmono 150dpi PNG 目检 + pdftotext 文本层主对账双通道五点比对；References [1]–[19] 逐条核对；本收据复读为修复后第 4 次全文复读（块级 3 次 + 本次终验）。
- **只读清点（终验命令与结果）**：`grep -nE 'diferen|coeficient|sufices|difers|\$r  \+ 0\$|r ~  ~|<sub><</sub>|\\mathtt'` → NONE；`grep -c 'Wulff|Poincaré|differences'` → 各 1；`\tag` 43 个（1–43 完整）；7 个 images/ 引用可解析；audit/ 页图 p001–p035 共 35 张。
- **复读收据**：`wc -l` = 1298 行；`shasum -a 256` = 56e7f240edbc47ea79489169915d1d51c09073c92da44980894a5fe9a8209cd3（2026-10-02 终验时点）。

### 修复登记（逐处：页码/内容/依据/commit）

| # | 页 | 修复内容 | 依据 | commit |
|---|----|---------|------|--------|
| 1 | p.002 | `{<sup>λ(t)</sup>} <sup>such</sup> <sup>that</sup>`→`{λ(t)} such that`（伪上标还原） | p002.png | f464484c |
| 2 | p.002 | 行39 句末补句号 | p002.png | f464484c |
| 3 | p.004 | 行75 `q  1`→`$q \to 1$`（箭头丢失） | p004.png | abc4b1bf |
| 4 | p.005 | 行101 `denoted by .`→补 `$\varnothing$` | p005.png | efb4ec76 |
| 5 | p.005 | 行109 `diferent`→`different` | p005.png+文本层 | efb4ec76 |
| 6 | p.006 | 行161 `configuration λ(t)`→补 `$\{ \lambda ( t ) \}$` | p006.png | eb121382 |
| 7 | p.008 | 行207 `coeficient`→`coefficient` | p008.png+文本层 | d27b9310 |
| 8 | p.008 | 行233 `diferent…difer`→`different…differ` | p008.png+文本层 | d27b9310 |
| 9 | p.008 | 行235 `diferent`→`different` | p008.png+文本层 | d27b9310 |
| 10 | p.009 | 行276 式(9) `S_\phi`→`\mathsf{S}_\phi` | p009.png | d82d1626 |
| 11 | p.009 | 行291 句末补句号 | p009.png | d82d1626 |
| 12 | p.010 | 行303 `coeficient`→`coefficient` | p010.png+文本层 | 9c22a2e1 |
| 13 | p.010 | 行311 `coeficient`→`coefficient` | p010.png+文本层 | 9c22a2e1 |
| 14 | p.010 | 行329 `diferent×2+difer`→`different×2+differ` | p010.png+文本层 | 9c22a2e1 |
| 15 | p.011 | 行361 `coeficient`→`coefficient` | p011.png+文本层 | 5612f524 |
| 16 | p.011 | 行375 `coeficient`→`coefficient` | p011.png+文本层 | 5612f524 |
| 17 | p.011 | 行381 句末补句号 | p011.png | 5612f524 |
| 18 | p.012 | 行391 `coeficient`→`coefficient` 且句末补句号 | p012.png+文本层 | 96a28c54 |
| 19 | p.015 | 行549 `sufices`→`suffices` | p015.png+文本层 | bf26e7c0 |
| 20 | p.017 | (21)/(22) 拆分为两个独立 tag 公式（恢复 \tag{22}） | p017.png | 32f8def8 |
| 21 | p.017 | 删除孤立 `(22)` 残行 | p017.png | 32f8def8 |
| 22 | p.017 | 拍平函数名→`$\Phi ( t , z )$` | p017.png | 32f8def8 |
| 23 | p.017 | `\ i f`→`if` 且句末补句号 | p017.png | 32f8def8 |
| 24 | p.018 | 行641 `diferent`→`different` | p018.png+文本层 | 36767308 |
| 25 | p.018 | 行671 `if λ(t)`→`if $\{ \lambda ( t ) \}$` | p018.png | 36767308 |
| 26 | p.019 | 行709 句末补句号 | p019.png | 8f8b91e6 |
| 27 | p.020 | 行713 `r  + 0`→`$r \to + 0$` | p020.png | f8be26db |
| 28 | p.020 | 行719 句末补句号 | p020.png | f8be26db |
| 29 | p.020 | 行735 证明末补 □ | p020.png | f8be26db |
| 30 | p.020 | 行739/741 `r ~  ~ + 0`→`$r \to + 0$` | p020.png | f8be26db |
| 31 | p.021 | 行755 `r  + 0`→`$r \to + 0$` | p021.png | 9521b15d |
| 32 | p.021 | 行767 句末补句号 | p021.png | 9521b15d |
| 33 | p.021 | 行775 句末补句号 | p021.png | 9521b15d |
| 34 | p.021 | 行777 `r  + 0`→`$r \to + 0$` | p021.png | 9521b15d |
| 35 | p.022 | 行857 `gradient of S`→补 `$\Re S$` | p022.png+文本层 | 0b919622 |
| 36 | p.023 | Figure 5 题注两 math 块间补逗号 | p023.png | e036510a |
| 37 | p.025 | 行923 删 `$\gamma_<$` 后多余 `<sub><</sub>` | p025.png | ee12e7a2 |
| 38 | p.025 | 行925 `$z_c ,$`双逗号→`$z_c$,` | p025.png | ee12e7a2 |
| 39 | p.025 | 行941 `r  + 0`→`$r \to + 0$` | p025.png | ee12e7a2 |
| 40 | p.025 | 行947 `diferences`→`differences` | p025.png+文本层 | ee12e7a2 |
| 41 | p.025 | 行951 `r  + 0`→`$r \to + 0$` | p025.png | ee12e7a2 |
| 42 | p.025 | 行956 `\mathtt{B}`→`\mathsf{B}` | p025.png | ee12e7a2 |
| 43 | p.025 | 行957 句末补句号 | p025.png | ee12e7a2 |
| 44 | p.027 | 行1007 `r  + 0`→`$r \to + 0$.`（箭头+句号） | p027.png | 707bfa63 |
| 45 | p.028 | 行1027 `\mathtt{B}`→`\mathsf{B}` | p028.png | 1ffe8782 |
| 46 | p.028 | 行1033 句末补句号 | p028.png | 1ffe8782 |
| 47 | p.030 | 行1095 `difers…diferent`→`differs…different` | p030.png+文本层 | f360e6fe |
| 48 | p.030 | 行1123 句末补句号 | p030.png | f360e6fe |
| 49 | p.031 | 行1139 句末补句号（终验修正为单句号） | p031.png | 20c4c612（原修）/本次收据 commit（双句号修正） |
| 50 | p.032 | 行1167 `N  \infty`→`$N \to \infty$` | p032.png | 49958d87 |
| 51 | p.032 | 行1191 `k`→`$\underline { k }$`（基向量下划线） | p032.png | 49958d87 |
| 52 | p.034 | [3] `Wulf`→`Wulff` | p034.png+文本层 | fd20f9e9 |
| 53 | p.034 | [13] `Poincar´e`→`Poincaré` | p034.png+文本层 | fd20f9e9 |

- 登记合计：53 条修复记录（对应 49 次 Edit，其中 #49 含终验双句号修正）；无未登记修复。
- residualIssues：无。
