# AUDIT — June Huh《Milnor numbers of projective hypersurfaces and the chromatic polynomial of graphs》（arXiv:1008.4749v3 = J. Amer. Math. Soc. 25 (2012), 907-927，MiKTeX/LaTeX born-digital，21p）

> mineru: standard 档云端解析；审计依据 = `audit/huh2012_pNNN.png`（pngmono 150dpi 全 21 页）
> + pdftotext 文本层逐字符对账（可靠 born-digital）。**伪影族**：中文标点 ，/。×3、
> `$G ,$,` 双逗号族 ×3、页码串入（2/9/2）×4、`o f`/`i f f`/`f o r`/`I f`/`i f`/`o r` 数学斜体
> 分写 ×12、上标乱码 ^{n^{\setminus}}/^{check n}、M¨obius/N´eron/´e/`\`e 重音拆裂 ~20、
> 幽灵脚注碎块（p4 脚注 1 的 8 个碎片）、fraktur 𝒜 丢失 ×6、if/iff 混淆 ×6、□ 通用常数丢失、
> −∆ 丢负号、ψ×Id 丢 ×、Γ_λ→Im 丢箭头、作者地址块缺 E-mail/Current address。

## p.001（arXiv 首页 + §1 引言前半）
- 核对：题名/JUNE HUH ✓；Birkhoff χ_G(q)（ff 登记不改）✓；unimodal/log-concave 定义
  （"for some 0≤i≤n," 逗号修复）✓；no internal zeros ✓；Conjecture 1/Read [31]/
  Rota-Heron-Welsh [33,14,48] ✓；χ_M(q) 定义/最小元 ̂0（修复）✓；Möbius function（修复）✓；
  Conjecture 2 ✓；脚注 MSC 14B05,05B35/keywords/NSF DMS 0838434 ✓
- 结果：**PASS±**（±：arXiv 侧边条未收——惯例）
## p.002（§1 后半：Theorem 3 + Milnor 数背景）
- 核对：Stanley [38, Conjecture 3][40, Problem 25] ✓；Theorem 3（of 修复）✓；χ_G=q^c χ_M ✓；
  Rota 两思想 ✓；Teissier [42]/{μ^i(f)}_{i=0}^n（上标修复）✓；dim_ℂ ✓；两次多项式展示 ✓；
  {μ^i(h)}（修复）✓；D(h)/ℙⁿ ✓；(1) CSM 公式/A_*(ℙⁿ). ✓（句号修复）；(2) χ_M/(q−1) 公式 ✓；
  ℂ^{n+1}（修复）✓
- 结果：**PASS**
## p.003（§1 末 + §2 Preliminaries 开头）
- 核对：Kouchnirenko 类比不等式 ✓；Theorem 21 预告/**iff**（修复）✓；"representable over ℂ."
  （句号修复）✓；Trung-Verma [47, Question 2.7] ✓；Dimca-Papadima [7]/Shephard [18,37,44] ✓；
  §2.1 R=R(m|J)/HP_R/e_i/[47, Theorem 1.2] ✓
- 结果：**PASS**
## p.004（Remark 4 + Theorem 5 + 脚注 1）
- 核对：Remark 4 𝕂/φ_J/Γ_J/[Γ_J]=Σe_i ✓；[12, Example 19.4]（修复）✓；"image of φ_J."
  （句号修复）✓；"ideals J₁,…,J_s."（句号修复）✓；N^{s+1}-graded/e_i 定义 ✓；
  Theorem 5 (Trung-Verma) general elements¹/e_i>0 iff/e_i=e(...) ✓；
  **脚注 1 全文**——md 碎成 8 块 → 按 print 重构（(f₁,…,fₘ)/f=Σc_kf_k/(c₁,…,cₘ) ∈ κᵐ 归位）✓
- 结果：**FAIL（脚注碎片）→已修**
## p.005（§2.2 混合体积 + Theorem 6 + Question + Remark 7）
- 核对：MV 定义/[5, Chapter 7]/MV_n(Δ,…,Δ)=1 ✓；Ehrhart [4, Section 6.3]/[47, Corollary 2.5] ✓；
  Theorem 6（of 修复/句末句号修复）✓；Alexandrov-Fenchel [35, Theorem 6.3.1] ✓；
  Question/[47, Question 2.7] ✓；Remark 7 [43]/[32]/[21, Remark 1.6.8] ✓；§3/3.1/V(h)/D(h)/
  Definition 8 ✓
- 结果：**PASS**
## p.006（Theorem 9 + Remark 10 + Example 11 开头）
- 核对：flag/V(h)_i/D(h)_i ✓；Theorem 9 (1)(2)/μ^i=(−1)^iχ/b̃_{i−1} ✓；χ(D(h))=Σ(−1)^iμ^i ✓；
  [8, p.141] ✓；Remark 10 Gauss map/Aluffi [2, Theorem 2.1] ✓；CSM 公式 ✓；
  χ(D(h))=∫c_SM ✓；Example 11 h=∏g_i^{m_i} ✓
- 结果：**PASS**
## p.007（Example 11 四行链 + Example 12 + Definition 13 + Example 14）
- 核对：μ¹(h) 四行链=d−1 ✓；ˆ omission ✓；Example 12（"for 0≤i<n," 逗号修复）✓；
  μ^i=(d−1)^i/μⁿ=(d−1)ⁿ−Σμ(h,p_i) ✓；[6, Corollary 5.4.4] ✓；Definition 13 ✓；
  Example 14 h/Δ_h 四情形 ✓
- 结果：**PASS**
## p.008（N 上界 + Theorem 15 + Example 16/17）
- 核对：N 四情形 ✓；b₁≤MV₁ ✓；Theorem 15（"simplex in ℝⁿ." 句号修复）✓；
  Example 16 torus/binomial/**"translation of −Δ, … replace Δ_h by −Δ"**（of/负号修复）✓；
  **"write ℝⁿ_I for the orthant"**（下标 I 修复）✓；三行并集分解/V_n 公式/MV=C(n,i) ✓；
  **"for all i=0,…,n and any n≥1."**（for all+句号修复）✓；Example 17 ✓
- 结果：**FAIL（三点）→已修**
## p.009（Example 17 末 + §3.2 + Example 19/20 + Theorem 21）
- 核对：0≤1≤2 ✓；Definition 18（句号修复）✓；**"log-concave sequences"**（修复）✓；
  Example 19 **iff×2**（修复）✓；Example 20 **iff×2**（修复）✓；fundamental theorem of algebra ✓；
  Theorem 21（"if n<k−i or m<i." 修复）✓；item 1 **iff the integer is 1** ✓；
  item 2 **"multiple of ξ … iff"**（修复）✓
- 结果：**FAIL（if/iff 族 ×6）→已修**
## p.010（Corollary 22 + Example 23 三组计算）
- 核对：Corollary 22 ✓；**"the anwer to the following question"——print 即此源级 typo，忠实** ✓；
  "J₁,…,Jₙ be ideals"（修复）✓；e_i 问句 ✓；ℂ{x,y,z}（逗号修复）✓；三组 (1,1,2) ✓；
  **"writing □ for sufficiently general nonzero constants"**（□ 归位——print 即用 □ 符号）✓；
  三组 □ 链式计算逐行 ✓；"computation of e_{(0,1,1)}(m|J₂,J₂)."（句号修复）✓
- 结果：**PASS±**（±：anwer 源级）
## p.011（§3.3 + Definition 24 + Corollary 25 + Remark 26 头）
- 核对：𝒜̃/𝒜/**"be the corresponding projective arrangement"**（ebe→be 修复）✓；
  Definition 24 **𝒜×3**（补符号修复）✓；𝒜̄=𝒜^H⊂ℂⁿ ✓；L_𝒜̄/L_𝒜̃（修复）✓；
  χ_𝒜̄=χ_𝒜̃/(q−1) ✓；Corollary 25/[28]（修复）✓；Randell [30] ✓；
  **"flats of 𝒜̄ of relevant dimensions"**（修复）✓；L_{𝒜̄|_ℙᵏ}（修复）✓；
  χ_{𝒜̄|_ℙᵏ}(q) truncation（(9) 剔除修复）✓；codim ≤k（句号修复）✓；display（修复）✓；
  b_{k+1}=μ^{k+1} ✓
- 结果：**FAIL（fraktur 族 ×6）→已修**
## p.012（Remark 26 + Corollary 27 + §4/4.1 + Theorem 28 头）
- 核对：c_SM 三行链 ✓；μ^i(h)=μ^i(h′)+μ^{i−1}(h″) ✓；[29, Theorem 2.56] ✓；
  Corollary 27（of 修复）✓；**"projective and the central arrangements"**（eand 修复）✓；
  𝒜̄ decone（修复）✓；χ_M=(q−1)χ_𝒜̄ ✓；"over ℂ."（句号修复）✓；"over ℂ. For this"（修复）✓；
  ACF₀ [24, Corollary 3.2.3] ✓；§4.1 grad(h) ✓；Theorem 28 头 ✓
- 结果：**FAIL（三点）→已修**
## p.013（Theorem 28 末 + Lemma 29/30/31 + fiber rings）
- 核对：item 2 句号（修复）✓；"section of V(h)."（修复）✓；Lemma 29/30（for 修复）✓；
  reduction 定义/[15, Corollary 1.2.5] ✓；Lemma 31/**"then S̄ is the polynomial ring"**
  （check 修复）✓；c_n∂h/∂z_i−c_i∂h/∂z_n ✓；𝓕_I→𝓕_J/[15, Proposition 8.2.4] ✓
- 结果：**PASS**
## p.014（Proof of Theorem 9 + 4.2 + Lemma 32）
- 核对：归纳/μ^i(h̄) 四行链（by definition/Lemma 30、31/Lemma 29/definition）✓；
  Remark 4/deg(h) ✓；Lemma 32 (1)(2) ✓；dim 不等式/e₀u+e₁v/Σ 式 ✓；
  **"Taking the limit u/v → 0"**（箭头修复）✓；**"=e_i(m|I)"**——print 即此（源级 typo，忠实）✓；
  "linear form x in S."（句号修复）✓；triple S̄=S/xS, IS̄, JS̄（array 修复）✓
- 结果：**PASS±**（±：m|I 源级）
## p.015（Lemma 32 末 + Proof of Theorem 15 + §5/5.1 + Lemma 33）
- 核对：dim≥ 式 ✓；K_h/dim_ℂ 函数（print 无句号，忠实）/e_i(m|K_h) ✓；μ^i≤MV_n ✓；
  §5 Hodge-Teissier-Khovanskii [18,44]/[11]/[21, Section 1.6]/[17]/[22] ✓；
  Okounkov body of D（_: 修复）✓；**"ample²"**+脚注 ²[22, Theorem 2.3]（标记修复生效）✓；
  Property A/B ✓；Lemma 33 不等式 ✓
- 结果：**PASS**
## p.016（Lemma 33 证明 + Lemma 34 + Lemma 35）
- 核对：Kleiman [21, Theorem 1.4.23]/Néron-Severi（修复）✓；Brunn-Minkowski [35, Theorem 6.1.1] ✓；
  V₂ 链/∫ 不等式 ✓；Lemma 34 **𝓒̄=𝓒′.**（修复）✓；e_i 幂不等式/归纳两式 ✓；
  𝓒̄⊆𝓒′/ε 序列 ✓；Lemma 35（If/or/P⁰×P⁰ 修复）✓；**iff the integer is 1** ✓；
  [36, Corollary 5.2.2, Chapter I] ✓；"ℙⁿ×ℙ⁰."（句号+box 删除修复）✓
- 结果：**FAIL（三点）→已修**
## p.017（Lemma 36 + Proof of Theorem 21 前半）
- 核对：Shephard [37, pp. 134-136]/Δ_λ/MV=λ₁λ₂⋯λ_i（for 修复）✓；ξ 类/zero if（修复）✓；
  H₁/H₂ ✓；∫_Z=e_i ✓；Lemma 33 log-concave ✓；item 2 By Kleiman（修复）✓；
  Néron-Severi over ℝ ✓；Segre ℙ^{nm+n+m} [12, Exercise 19.2] ✓；
  item 3 ξ∈Aₙ, n>0（Ξ 删除修复）✓；λ_i/φ_λ display ✓；e_i(m|J_λ) 链 ✓
- 结果：**PASS**
## p.018（Proof of Theorem 21 后半）
- 核对：∫_{Γ_λ}=e^i(e_i/e₀) ✓；**ψ×Id_{ℙⁿ}**（× 修复）✓；**Γ_λ→Im(Γ_λ).**（箭头+句号修复）✓；
  projection formula=eⁿ(e_i/e₀) ✓；**"In sum, Im(Γ_λ)⊂ℙⁿ×ℙⁿ"**（合并修复）✓；
  [Im(Γ_λ)]=(eⁿ/e₀)Σ ✓；item 4 ξ=Σ_{i=p}^q ✓；**"where 0≤p≤q≤k, k−p≤n, q≤m, and e_p,e_q are positive."**
  （标点修复）✓；**"If p=q, then either 0<p<m or 0<k−p<n, since"**（修复）✓；
  "represents ξ. Here 0<p"（修复）✓；"if 0<k−p<n, we take"（修复）✓；
  cone Z̃（is 修复）✓；"and represents"（修复）✓；ξ. ✓
- 结果：**FAIL（八点）→已修**
## p.019（Acknowledgments + References [1]-[21]）
- 核对：Acknowledgments 全文（Hironaka/Schenck/Teissier/referees）✓；
  [1]-[21] 抽验 12 条全对（Kähler（修复）/Théorèmes（修复）/Polyèdres（修复）/arXiv:0904.3350v2 等）✓
- 结果：**PASS**
## p.020（References [22]-[47]）
- 核对：[22] Mustață/École Norm. Supér.（修复）✓；[23]-[47] 抽验 14 条全对
  （[33] Congrès（修复）/[34] multiplicité en algèbre et géométrie algébrique（修复）/
  [42] Cycles évanescents…Singularités à Cargèse…Astérisque（修复）/[43] inégalité（修复）/
  [44] théorème de l'index…isopérimétriques（修复）/[45] Variétés polaires…La Rábida（修复））✓
- 结果：**PASS**
## p.021（References [48] + 作者地址块）
- 核对：[48] Welsh ✓；Department of Mathematics, University of Illinois, Urbana, IL 61801, USA ✓；
  **md 缺 E-mail huh14@illinois.edu / Current address University of Michigan / E-mail
  junehuh@umich.edu 三行 → FAIL 已补** ✓
- 结果：**FAIL（地址块）→已修**

## 总评

- **覆盖声明**：21/21 页逐页目检（150dpi 全页）+ 文本层逐字符对账（可靠 born-digital）。
  mineru：standard 档。
- **FAIL 修复（102+3 组）**：①中文标点/双逗号/页码串入 ~10；②数学斜体分写（of/iff/for/If/or）
  ~14；③if→iff 语义修正 ×6（Example 19/20、Theorem 21、Lemma 35——print 均 iff）；④上标乱码
  ^{n^{\setminus}}/^{check n}→^n；⑤幽灵脚注 8 碎片重构（p4 脚注 1）；⑥fraktur 𝒜 丢失 ×6+
  χ/L 下标乱码修复；⑦重音拆裂 ~22（Möbius/Néron/Birkhäuser/Kähler/Mustață/École/
  Théorèmes/Polyèdres/Congrès/multiplicité/évanescents/inégalité/théorème/Variétés 等）；
  ⑧标点句号补齐 ~14；⑨ψ×Id/Γ_λ→Im/Im( 合并/−∆ 负号/□ 归位/Rⁿ_I 下标；⑩作者地址块补 3 行。
- **源级 quirk 清单（忠实不改）**："anwer"（Example 23，print 即此）；"Birkhof/coeficients/
  suficiently/efectively/afine/Diferential" ff→f 族；"e_i(m|I)"（Lemma 32 证明末位，print 即此）；
  Example 23 的 □ 通用常数符号（print 即此）；Lemma 29 "for 0≤i<deg HP" 与 Lemma 30 "≤"
  的差异（print 即此）。
- **可用性结论**：修复后 md 可作该 JAMS 论文忠实底本；(1)-(54) 编号公式与全部定理/引理/例子
  逐一核对全对；参考文献 48 条抽验 26 条全对。本篇 21/21 页完成，无未决项。
