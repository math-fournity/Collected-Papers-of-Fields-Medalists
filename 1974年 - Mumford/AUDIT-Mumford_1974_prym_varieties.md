# AUDIT — D. Mumford《Prym Varieties I》（Contributions to Analysis, Academic Press 1974, 325-355，LaTeX born-digital 重排本，26p）

> mineru: standard 档云端解析；审计依据 = pdftotext 文本层逐字符对账（可靠 born-digital，0 FFFD）
> + `audit/mum74_pNNN.png`（150dpi 全 26 页已渲染；p.1/14/22 全页/大半页目检——含题录页、
> Figure 1 图页、§7 hyperelliptic I′∪I″ 页；p.2/3/16/19/20/23/24/26 定向裁片 + 300dpi 终裁 5 处
> （λ=λ_D、Proposition π*(𝔄)、proceding、dim Γ(M)=3、𝔅 poles））。
> **伪影族**（本篇 md 质量较高，修复量小）：**文献 [16] Szpiro 整条丢失**（正文 L901 引用
> [16] 而文献表止于 [15]）→ 按 print 补入；**Part 标题**（print I/II/III 三部结构：`## I` 整条
> 丢失、`## 11` 为 II 的 OCR 数字化）→ 补/改；Ω_{c̄}→Ω_{C̃} ×7（三种变体）；Θ̃ 缺 tilde ×3
> （(6.2) resp.、Θ̃·P⁺、Corollary tangent cone）；1_{J̃}+ι → 1_j+t（L348 Prym 定义式）；
> T_{Y'K} 型：J̃ 对偶 \hat{J} 重写 ×1、λ−λ_D→λ=λ_D（NOTATIONS 定义）；J_{2-g2}→J_{2g-2}；
> Nm 括号断裂 (π*M(∑x_i)(= → 补全；𝔅 poles 斜体 B→fraktur；ιx→\iota x；proceding
> print 拼写还原；SING E→SING Ξ；×_C 下标；Proof of(ii) 粘连；$g!$→g!；NOTATIONS 两
> 条目粘行拆分。

## 逐页签（文本层主通道 + p.1/14/22 目检 + 8 页定向裁片）
- **p.001（题录 + INTRODUCTION 前半）**：Reprinted from CONTRIBUTIONS TO ANALYSIS / A Collection
  of Papers Dedicated to Lipman Bers / © 1974 ACADEMIC PRESS, INC. ✓；Prym Varieties I/DAVID
  MUMFORD/HARVARD UNIVERSITY ✓；Riemann–Prym–Wirtinger–Schottky–Jung theory ✓；π: C̃→C 双
  覆盖/J, J̃/ι/Fay [4] ✓ — **PASS±**（±：重排本无原书页眉细节）
- **p.002-003（INTRODUCTION 后半 + NOTATIONS + Part I + §1 开头）**：Θ,Θ̃ 关系/Schottky-Jung
  [15]/Riemann [13]/Farkas-Rauch [3]/"g ⩾ 4 时 J 非最一般"（**$g!$→g! 感叹号还原**）✓；
  3n moduli/(1/2)n(n+1)/3n−3 ✓；Clemens-Griffiths [2]/Murre [12]/Martens [8] ✓；
  **NOTATIONS**（k/R(X)/Pic⁰/X̂/λ_D/[divisor class of T_x⁻¹D − D]/**polarization 定义
  λ = λ_D（300dpi 终裁：减号系 = 字形，数学上唯一读法 + 第二处 print 明确 =）**/principle
  polarization（**print 即 principle，源级登记**）/[10]）✓；**Part I 标题补入**（p.2 PNG 居中
  "I"）✓；§1（S_α ≅ R_α[t_α]/(t_α²−β_α)/S = O_C ⊕ L/乘法 φ: L² ≅ O_C(−ΣP_i)/branch points/
  # = 2(−deg L) = 2n）✓ — **PASS**
- **p.003-006（§1 Jacobians + §2 CONFIGURATION）**：J = Pic⁰(C)/Albanese t, t̃/Nm 两条定义
  （(a) H¹ 图/(b) divisor π(𝔄)）✓；交换图 C̃→J̃, C→J 与 Pic⁰ 对偶图 ✓；**(t*)⁻¹ = −λ_Θ,
  (t̃*)⁻¹ = −λ_Θ̃** ✓；**π*, Nm 两性质 (i) 对偶 (ii) Nm·π* = ×2** ✓；§2 DATA I（(2.1)(2.2)
  tag 在位/**(2.3) 交换图 = 嵌入图 + 编号行（print 图编号）**）✓；ψ = λ_θX⁻¹·φ̂·λ_θY ✓；
  **DATA II**（(i)-(viii)：H₀⊂H₁⊂X₂/e_{2,X}, e_ρ/Riemann forms/(a)(b)(c) 相容性/Y = X×P/H/
  (v) H₀ = ker φ/(vi) ι 对合/(vii) σ·τ = 2_Y, τ·σ = 2_{X×P}/(viii) 维数计数 **0 ⩽ c ⩽ min(a,b)**）✓；
  证明（P = λ⁻¹(ker φ̂)⁰/v components/H ⊂ X₂×P₂/ψ: H₁ → P₂/(x,y) ∈ H 推理链/2×2 矩阵
  α,β,γ,δ（**γ = β̂**）/H maximal isotropic [10, Section 23]/#H₁^⊥ 不等式链）✓ — **PASS**
- **p.006-010（§3 DEFINITION OF THE PRYM VARIETY）**：π⁻¹(π𝔄) = 𝔄 + ι(𝔄) ⇒ π*(Nm x) = x+ι(x) ✓；
  **P = (ker Nm)⁰ = ker(1_J̃ + ι)⁰ = Im(1_J̃ − ι)（1_j+t → 1_J̃+ι 修复）** ✓；"odd" part ✓；
  Hurwitz：ĝ = 2g+n−1/dim P = g+n−1 ✓；ker(π*) ⊂ J₂/C_𝔄 未分岔覆盖/Lemma（ramified ⇒
  ker = 0；unramified ⇒ {0,𝔄}）✓；**Corollary 1**（symplectic injection ψ: J₂ ↪ P₂/(b) J̃ ≅
  J×P/{(α,ψα)}；unramified H₀ = {0,𝔄}, H₁ = {𝔅 | e₂(𝔄,𝔅) = +1}）✓；**Corollary 2**（ker ρ = P₂
  ⇒ ρ = 2λ_Ξ principal/φ(J) = {x | ιx = x}）✓ — **PASS**
- **p.010-014（§4 RELATIONS BETWEEN THETA DIVISORS + Part II）**：**Part II 标题（## 11 → ## II
  修复）** ✓；φ⁻¹θ_{Y,y} = θ_{X,x₁} + θ_{X,x₂} 问题/y ∈ P 归约/**"div. class [φ⁻¹(θ_{Y,y}) −
  φ⁻¹(θ_Y) in X] = φ̂(λ_θY(y))"** ✓；symmetric translates 脚注 †（e_*^θY(φ(x)) = e₂(D,x)）✓；
  (4.1) δ morphism 定义 ✓；σ*(O_Y(θ_Y)) = p₁*O_X(2θ_X) ⊗ p₂*L_ρ ✓；**Proposition**（B_ρ base
  points/i: P(Γ(L_ρ)) ↪ |2θ_X|/φ_ρ 交换图 = 嵌入图）✓；证明（Heisenberg G_m 正合列 ×3/σ*(s₀)
  H* 不变/χ 同构/σ*(s₀) = Σp₁*αᵢ ⊗ p₂*βᵢ/zero set 公式/(4.1) 引用一致）✓；**Proposition
  (Wirtinger)**（B 内积/ξ: X×X → X×X, (x,y) ↦ (x+y, x−y)/(4.2) θ(u+v)θ(u−v) = Σc_αβ s_α(u)s_β(v)/
  Δ(X₂) 不可约论证/det c_αβ ≠ 0/φ′_X(v) = B′(φ_X(v))）✓；**Corollary 1**（P−B_ρ → P(Γ(L_ρ))
  diagram/⟺ i(φ_ρ(y)) = B′(φ_X(x))）✓；**Corollary 2**（ρ = 2λ_θP 情形）✓ — **PASS**
- **p.014-018（§5 SPLITTING FOR JACOBIANS）**：J_k/J̃_k/⊔✓；Θ = {L ∈ J_{g−1} | Γ(L) ≠ 0} ✓；
  (π*)⁻¹(Θ̃_{−y}) = Θ_{x₁} + Θ_{x₂} ✓；𝔄：2𝔄 ≡ ΣPᵢ, π⁻¹𝔄 ≡ ΣQᵢ/R(C̃) = R(C)(√f) ✓；
  **Proposition**（Γ(C̃, π*L(Σxᵢ)) ≠ 0 ⟺ Γ(C,L) ≠ 0 or Γ(C, L(Σπxᵢ − 𝔄)) ≠ 0；π_*(O_C̃) =
  O_C ⊕ O_C(−𝔄)/even-odd 分解/中间层不分裂/正合列/χ(L) = 0 排除）✓；**Corollary 1**（y = Σxᵢ ∈
  J̃_n, x = Σπxᵢ − 𝔄 ∈ J₀ ⇒ (π*)⁻¹(Θ̃_{−y}) = Θ + Θ_{−x}；† 识别约定脚注）✓；π*x_i = πx_j 情形
  ⇒ π*(J_{g−1}) ⊂ Θ̃_{−y} ✓；**theta characteristics 选择**（(a) Nm ζ̃ = K + 𝔄/[𝔅 构造括号]/
  (b) Θ₀ = Θ_{−ζ}/(c) ζ̃ = π⁻¹ζ + δ, 2δ = ΣQᵢ）✓；**Definition compatible solutions**（z = ½Σ(xᵢ −
  ιxᵢ), w = ½(Σπxᵢ − 𝔄)/z + π*w = Σxᵢ − δ）✓；**Corollary 2**（(π*)⁻¹(Θ̃_{0,−z}) = Θ_{0,w} +
  Θ_{0,−w}）✓；**Corollary 3 (Schottky–Jung)**（2𝔅 = 𝔄/[Note that 2ζ̃ = π⁻¹(2ζ+2𝔅) = π⁻¹(K+𝔄) =
  K̃...]/(i) (π*)⁻¹(Θ̃₀) = Θ_{0,𝔅} + Θ_{0,−𝔅}/(ii) Kummer diagram + i(φ_P(0)) = B′(φ_J(𝔅))）✓；
  **Corollary 4 (Fay)**（two branch points/j = (B′)⁻¹·i isomorphism/z = ½(x−ιx), w = ½(πx−𝔄)/
  j(φ_P(z)) = φ_J(w)）✓；theta-null werte/f_a(Z) = θ[0^a](0,Z)/n=3 唯一八阶恒等式 → Schottky
  relation ✓；k ⩾ 4 区分命题（j(φ_X(X)) ∩ φ(Y) ≠ ∅ ⇒ X ≅ Y）✓ — **PASS**
- **p.018-021（Part III + §6 GEOMETRIC DESCRIPTION OF SING Ξ）**：**Part III 标题在位** ✓；
  **§6 标题 SING Ξ（E→Ξ 修复）** ✓；(a) genus/dim P = g−1/ker ρ = P₂ ≅ {0,𝔄}^⊥/{0,𝔄} ✓；
  (b) {x | ιx = x} = π*J ✓；[a = g, b = g−1, c = g−1] ✓；[11] 前文结果：Nm: J̃_{2g−2} →
  J_{2g−2}/Nm⁻¹(K) = P⁺ ⊔ P⁻/**(6.1) dim Γ(L_α) even ⟺ α ∈ P⁺ tag 在位** ✓；(6.2) **dim Γ(L_α)
  = mult. of α on Θ (resp. Θ̃)（Θ̃ tilde 修复）** ✓；**Proposition**（Θ̃ ⊃ P⁻；Θ̃·P⁺ = 2Ξ）✓；
  证明（odd ⇒ ⩾1/even positive ⇒ ⩾2/主极化限制两倍）✓；**Corollary Sing Ξ**（mult ⩾ 4 ∪ {mult
  = 2, T_{x,P⁺} ⊂ tangent cone to **Θ̃**（修复）}）✓；Kempf [7] tangent cone det(ω_ij) = 0 ✓；
  Ω_C̃ 分解 Γ(Ω_C) + Γ(Ω_C(𝔄))（**Ω_{c̄}→Ω_{C̃} ×7 修复**/"Prym differentials"）✓；
  ι*⟨s,t⟩ = ⟨t,s⟩/Symm² 与 Λ² 分解/ω⁺ symmetric, ω⁻ skew/Pfaffian ✓ — **PASS**
- **p.020-022（§6 末 Proposition + §7 DIM SING Ξ）**：**Proposition**（Nm L_α = Ω_C, dim Γ = 2
  ⇒ T_{α,P⁺} ⊂ tangent cone ⟺ **L_α ≅ π*(𝔄)(Σx_i)——print 原文即 𝔄（p.19 300dpi 终裁），
  忠实保留并登记**/sheaf M dim Γ(M) = 2）✓；证明（**"In the proceding notation"——print 排印
  错误 procedural 还原**/(ω⁻) 矩阵/⟨s,t⟩−⟨t,s⟩ tangent cone to Ξ/**let 𝔅 be the poles（B→𝔅
  修复）**/M = O_C(𝔅)/π*M(Σx_i) and 1, s/t ∈ Γ(M)（**print 即 "and 1," 300dpi 证实，忠实保留
  登记**）/dim Γ(M) = 2）✓；§7 **Theorem**（(a) hyperelliptic ⇒ Jacobian or product/
  (b) g=3 ⇒ 2-dim Jacobian/(c) g=4 ⇒ 3-dim Jacobian + hyperelliptic iff ∃ even theta char/
  (d) g ⩾ 5 ⇒ dim Sing Ξ ⩾ g−5 四情形 trigonal/elliptic double cover/g=5 even/g=6 odd）✓；
  Corollary（(P,Ξ) 非 Jacobian）✓；Case 1/Case 2/Ω_C = Nm(π*M(Σx_i)) = **M²(Σπx_i)（Nm 括号
  补全修复）**/(a)-(c) 条件/逆构造 ✓；**Lemma**（dim Sing Ξ ⩾ g−5 ⇒ almost all in case 1）✓；
  [11, pp. 186–188]/Saint-Donat [14, Lemma 2.5] 推广/W_α = Im[Λ²Γ(L_α) → Γ(Ω_C⊗𝔄)]/
  T_{α,Z} ⊂ W_α^⊥/codim ⩽ 4/decomposable 2-forms cone/s∧t = 0 链 ✓ — **PASS**
- **p.022-023（§7 证明 + hyperelliptic case + g=3/4）**：hyperelliptic：p: C → P¹/{z₁,…,z_{2g+2}}/
  **(a) {1,…,2g+2} = I′ ∪ I″, I′ = 2h+2, I″ = 2k+2（p.22 PNG 终裁：print 即 ∪ 无基数竖线，
  md 忠实）**；**I′ ∩ I″ = φ（print 即 φ，忠实）**/(b) C′, C″/(c) C̃ normalization/tower 图
  （page_21 嵌入图 ✓）/**Prym(C̃/C) ≅ J′ × J″, Ξ ↔ J′ × Θ″ + Θ′ × J″** ✓；Idea of Proof
  （四 eigensubvarieties/π*J, J′, J″/Θ 极化分裂）✓；non-hyperelliptic v ⩾ g−5 情形（(i)-(vi)
  条件/Clifford theorem/d < g−1 **Marten's theorem（print 即 Marten's，源级登记）**/d = g−1
  theta characteristics）✓；g=3（**N² ≅ Ω_C, dim Γ(M) = 3——print 原文即 M（p.23 300dpi
  终裁），忠实保留并登记**/N = O_C(1)/M = N(−z)/Ω_C ≅ N²(−2z)(πx₁+πx₂)/πx₁ = πx₂ = z/
  **L_α = π*N(x − ιx) or π*N（ι 修复）**/dim Sing Ξ = 1 ⟺ 链）✓；quintics C ⊂ P²/Clemens-
  Griffiths cubic hypersurfaces/Clemens conjecture ✓ — **PASS**
- **p.023-025（APPENDIX: A THEOREM OF MARTENS）**：strengthen Marten's theorem [8, Theorem 1]
  (see also Saint-Donat [14, Theorem 2.4]) ✓；**Theorem**（∃d, 2 ⩽ d ⩽ g−2, dim Sing W_d ⩾ g−3
  ⟺ (a) hyperelliptic (b) trigonal (c) elliptic double cover (d) nonsingular plane quintic）✓；
  Kempf [7,16]/Sing W_d = G_d¹/∃d dim ⩾ d−2 ⟺ hyperelliptic/d = 3 trigonal/d ⩾ 4 配对
  Γ(L)⊗Γ(Ω⊗L⁻¹) → Γ(Ω)/T_{L,Sing W_d} ⊂ ⊥/(A.1) 正合列 **tag 在位**/dim Im φ = g+3−dim Γ(L²)/
  dim Γ(L²) ⩾ d/G_{2d}^{d−1} ⩾ d−3/(i) d=4/(ii) d=5, g=7 ✓；(i) 情形（L₀ degree four/
  Riemann-Roch 两个 dim Γ 式/P₁,…,P_{g−6}/M = Ω⊗L₀⁻¹(−ΣPᵢ)/dim Γ(M) = 3/rational map π:
  C → P²/degree 论证/平面五次或椭圆双覆盖/两例 Sing W₄ 无穷）✓；(ii) 排除（deg L = 5/
  L² ≅ Ω(−P−Q)/irreducible 2-dim/M² ≅ Ω ⇒ dim Γ(M) ⩾ 3/theta divisor 不含全部 2-torsion
  [9, p. 346]/矛盾）✓；**Note added in proof**（Fay [4] Prop 5.7 misprint/lower limit should be
  D/remarks at top of p. 100）✓ — **PASS**
- **p.025-026（REFERENCES [1]-[16]）**：**[16] L. Szpiro 补入**（"Travaux de Kempf, Kleiman,
  Laksov," (Sem. Bourbaki, Exp. 417), Springer-Verlag, Berlin and New York, **1972 Lecture
  Notes, Vol. 317**——print 逗号缺失即此）✓；逐条核对：[1] Andreotti-Mayer Ann. Scuola Norm.
  Sup. Pisa 21 (1967) 189-238 ✓；[2] Clemens-Griffiths Ann. 95 (1972) 281-356 ✓；[3] Farkas-
  Rauch Ann. 92 (1970) 434-461 ✓；[4] Fay LNM 352 (1973) ✓；[5] Harris Ph.D. Thesis Harvard
  1972 ✓；[6] Hoyt Ann. 77 (1963) 415-423 ✓；[7] Kempf Ann. 98 (1973) 178-185 ✓；[8] Martens
  J. Reine Angew. Math. 227 (1967) 111-120 ✓；**[9] Invent. Math. 1 (1966) 无页码——print 即
  此，忠实保留** ✓；[10] Abelian Varieties Tata Inst. 1970 ✓；[11] Ann. Sci. Ecole Norm. Sup. 4
  (1971) 181-192 ✓；[12] Murre Compositio Math. 25 (1972) 161-206 ✓；**[13] "Nochtrag IV"——
  print 即此拼法（通行作 Nachtrag），p.26 300dpi 终裁忠实保留** ✓；[14] Saint-Donat Math. Ann.
  206 (1973) 157-175 ✓；**[15] "Neue Sätze über symmetralfunctionen und die Abelschen
  funktionen"——p.26 300dpi 终裁 print 即 umlaut + und（pdftotext 曾误作 and），md 忠实** ✓ —
  **PASS**

## 总评

- **覆盖声明**：26/26 页经可靠文本层逐字符对账 + md 全文交叉核对（1314 行全读）；150dpi 全
  26 页渲染，p.1/14/22 大半页目检，p.2/3/16/19/20/23/24/26 定向裁片，300dpi 终裁 5 处。
- **FAIL 修复（24 处 / 23 规则，另 +2 处手工补刀 = 25 处）**：①[16] Szpiro 整条文献补入；
  ②Part I 标题补入 + ## 11→## II；③Ω_{c̄}/Ω_{C̄}→Ω_{C̃} ×7；④Θ̃ 缺 tilde ×3；⑤1_J̃+ι
  （Prym 定义式）；⑥J̃ 对偶 \widehat{\tilde{J}}；⑦λ−λ_D→λ=λ_D；⑧J_{2-g2}→J_{2g-2}；⑨Nm 括号
  补全；⑩𝔅/ι/proceding/SING Ξ/×_C/Proof of(ii)/$g!$/NOTATIONS 粘行。
- **源级 quirk 清单（忠实不改）**：**"π*(𝔄)(Σx_i)"**（§6 Proposition 结论 print 即 𝔄——p.19
  300dpi 终裁，通行修订本作 π*M，本篇 print 权威）；**"dim Γ(M) = 3"**（§7 g=3 情形 print
  即 M，上下文应为 N——p.23 300dpi 终裁）；**"and 1, s/t ∈ Γ(M)"**（§6 证明 print 即此，
  300dpi 证实）；**"proceding"**（print 排印错误，已按 print 还原）；**"principle polarization"**
  （NOTATIONS print 即 principle）；**"Marten's theorem"**（print 即 Marten's，与 intro
  "Martens [8]" 不一致）；**"I′ ∪ I″ / I′ ∩ I″ = φ"**（p.22 终裁：∪、φ 均为 print 原貌）；
  **[9] 无页码、[13] "Nochtrag IV"、[16] "1972 Lecture Notes" 前无逗号**（均 print 即此）。
- **可用性结论**：修复后 md 可作该 1974 论文忠实底本；(2.1)-(2.3)(4.1)(4.2)(6.1)(6.2)(A.1)
  编号方程/图逐条核对全对；Theorem（§7+附录）、Propositions、Lemmas、Corollaries 1-4、
  Definitions 全部在位；参考文献 16 条逐条核对全对；4 幅嵌入图（交换图/tower）在位。本篇
  26/26 页完成，无未决项；目录内无同篇其他版本。

### 修复登记（2026-09-30）
- **共 25 处（23 规则 + 2 手工补刀）替换全部命中（0 miss）**；\tag 清单 (2.1)(2.2)(4.1)(4.2)
  (6.1)(A.1) + 图编号 (2.3)(6.2) 与 print 一致；[16] Szpiro 按 print 整条补入。fix commit 见
  父提交链。本篇 26/26 页完成，无未决项。
