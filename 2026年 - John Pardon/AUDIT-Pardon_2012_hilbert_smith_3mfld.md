# AUDIT — J. Pardon《The Hilbert–Smith conjecture for three-manifolds》（arXiv:1112.2324v3，LaTeX born-digital，24p）

> mineru: standard 档云端解析；审计依据 = pdftotext 文本层逐字符对账（可靠 born-digital，0 FFFD）
> + `audit/par12_pNNN.png`（150dpi 全 24 页已渲染；p.1/p.14 全页目检——含 Abstract/Conjectures
> 页与 Figure 1 genus-2 handlebody 图页；p.2/4/13/19/20 另有 150dpi 定向裁片核足注结构、
> fn3 widehat、(5.1) 区与 𝒮/S 记号）。
> **伪影族**：**足注碎片错位 ×4 组**（fn1/fn2/fn3/fn4 的正文被拆成 10+ 个 docvortex 碎片块、
> fn4 内部乱序 → 逐条按 print 重构完整足注）、ff 连字 ×26、丢箭头 ×9（k→∞、γ:[0,1/2]→B(x₁,η)、
> S̃→S ×3、F→U、MCG→Sp ×2、H¹(N⁺)→Ĥ¹(Z)、π₁(F)→π₁((M∖F)±)、H_{±,γ}）、方程编号
> 错位 5 组（(2.3)(4.6)(4.7)(4.8)(5.1) 补/重编 + 孤儿编号行 ×2 删除 + \tag{4.6} 重复去重）、
> 幽灵字符（Conjecture 1.3 处 "2"、PNext、W Tis、S_{;}、S̃ 后 P）、"“X”" 引号 → ^{66}/″、
> 变音破裂 ×7（Čech×3、Dušan Repovš/Ščepin×2、Ĭozhe Maleshich、Flächen、Hölder、Symonds'）、
> 控制字符 \x08\x0c\t ×2、𝒳→X（Lemma 3.5 iv）、π₁- 拆裂 ×5、"it's" 类粘连 ~20。

## 逐页签（文本层主通道 + p.1/14 全页目检 + 5 页定向裁片）
- **p.001（题录 + Abstract + Conjectures 1.1-1.2）**：arXiv:1112.2324v3 22 Jan 2013/题名/John
  Pardon/9 April 2012; Revised 22 January 2013 ✓；Abstract（faithful ⇒ Lie；reduction to Z_p；
  "If Z_p acts faithfully on M³"）✓；MSC 2010 Primary 57S10, 57M60, 20F34, 57S05, 57N10/
  Secondary 54H15, 55M35, 57S17/Keywords ✓；§1 faithful action 定义 ✓；**Conjecture 1.1
  (Hilbert–Smith)** ✓；Gleason [8,9]/Montgomery–Zippin [22,23]/Yamabe [46,47] ⇒ contains Z_p ✓；
  **Conjecture 1.2** ✓ — **PASS±**（±：arXiv v3 边条未收）
- **p.002-004（Conjectures 1.3-1.4 + Theorem 1.5 + §1.1 outline + fn1/fn2）**：**Conjecture 1.3**
  （"open set U ⊆ M, there exists ε > 0"——**幽灵 "2" 删除 + 逗号补回**；(1.1) 显示
  `f o r a l l` 修复）✓；Conjecture 1.4（almost periodic/Gottschalk [10]）✓；n=1,2
  Montgomery–Zippin [23, pp233,249] ✓；Yang [48] cohomological dimension n+2（**[48] 悬空引用
  ——print 文献表止于 [47]，源级登记**）✓；Bochner–Montgomery [4] C²/**Repovš–Ščepin [32]
  C^{0,1}（变音修复）**/Maleshich [18] C^{0,n/(n+2)+ε}/Martin [19] quasiconformal ✓；
  Raymond–Williams [31]/Wilson [45, Theorem 3] ✓；**Theorem 1.5** ✓；§1.1（p^kZ_p ≅ Z_p/
  neighborhood base/k→∞ 修复/**"close to the identity.¹" fn1 标记在位**）✓；
  **fn1 完整重构**（NSS/Yamabe [47, p364 Theorem 3]/iff ×2/p^kZ_p/Newman's theorem [24]
  Second 段——print 全文依文本层归位）✓；properties ¹²/fn2 完整重构（dimension reduction/
  ∂Z/**"with n = 2."归位**/"approximate boundary"）✓；(1.2) 交 form 矩阵 ⊕ ✓；Z/p ⊆ MCG(F)/
  Nielsen classification ✓；§1.2 Acknowledgements（Agol/Freedman/**Steve Kerckhoff**（print
  即双 f）/referee/DGE–1147470）✓ — **PASS**
- **p.004-008（§2 lattice of incompressible surfaces）**：fn3 **完整重构**（Kakimizu complex/
  "Z-equivariant order complex" of **Ŝ(Ŝ³∖K̂)**（p.4 PNG widehat 终裁）/**Ŝ³∖K̂ infinite cyclic
  cover**/not a quasicylinder technically）✓；Theorem 2.1 [3, p62 Theorem 8]（Bing）✓；
  Lemma 2.2（bicollared→PL/Theorem 2.1 应用/bicollar splice——φ₁/φ₂ 构造在位）✓；
  Lemma 2.3（Waldhausen [43, p76 Corollary 5.5]/TOP 情形 straighten）✓；Definition 2.4
  quasicylinder（Σ_g×R）✓；Lemma 2.5 三等价（H₁^lf/Poincaré dual ×2 修复）✓；
  Definitions 2.6-2.10（S_TOP/S_PL/directed/≤）✓；Lemma 2.11（ψ bijection/𝔉₁,𝔉₂ straighten）✓；
  **"S(M) 记号统一"** ✓；Lemma 2.12（equivalence iff/odd cardinality/basepoint——**π₁-
  injective 拆裂修复**；"π₁(G) → π₁(M,γ) up to inner automorphism"）✓；Lemma 2.13（trivial
  element/MCG(F)；**"π₁(M,γ).⁴ □" fn4 标记归位**）✓；**fn4 完整重构**（category γ/objects
  p ∈ γ/morphism p → p′/functor π₁(M,·): γ → Groups/isomorphism π₁(M,p) → π₁(M,p′)/
  limit/colimit——碎片归位 + 内部乱序重排）✓ — **PASS**
- **p.008-012（Lemma 2.14-2.19 + §3）**：Lemma 2.14（partially ordered——**partiallyordered
  修复**/reflexivity/antisymmetry/transitivity）✓；(2.1) van Kampen amalgam ✓；π₁(F₁) ⊆…
  论证 ✓；Lemma 2.15（ψ: S((M∖F)₋) → S(M)|≤[F]——** Representatives 控制字符 \x08\x0c\t 修复
  /F′ ≤ F″ isotopy/ψ injective/**π₁(F) → π₁((M∖F)±,γ) 箭头修复**）✓；Lemma 2.16（two
  applications）✓；Lemma 2.17（compression 操作）✓；Lemma 2.18（𝔄₋,𝔄₊ finite set）✓；
  **Lemma 2.19 (suggested by Ian Agol [1])**（lattice/(2.2) X(𝔉₁,𝔉₂) 定义）✓；证明（tame ends/
  Schoen–Yau [35]/Sacks–Uhlenbeck [33,34]/area minimizing/(2.3) **X(𝔉₁,𝔉₂;𝒢) 补 \tag**/
  Lemma 2.18 𝔉₀/Lemma 2.16 isomorphism）✓；Remark 2.20（DIFF quasicylinder）✓；
  Remark 2.21（Jaco–Rubinstein [13]/normal surfaces/𝒳(𝔉₁,…;𝒢₁) 函数空间记号——print 即
  script X，忠实保留；Kakimizu complex [14]/Schultens [36]/Przytycki–Schultens [30]）✓；
  §3 开头（integer coefficients 修复/Čech ×2 修复）✓；**Lemma 3.1**（(3.1) direct limit/
  Steenrod [39]/Spanier [38, p419]/continuity axiom；**"The p<sup>ˇ</sup>urpose" 幽灵 ˇ 删除**）✓；
  **Lemma 3.2**（(3.2) Mayer–Vietoris）✓ — **PASS**
- **p.010-012（§3.2-3.3 Alexander duality + plus operation）**：Lemma 3.3（(3.3)
  H̃Ȟ*(X) ≅ H̃_{n−1−*}(Sⁿ∖X)）✓；证明（smooth boundary/(3.4) 交换图/direct limit/final
  system；**H̃*(U) --∼--> H̃_{n−1−*} 箭头修复**）✓；§3.3 **Definition 3.4**（(3.5) X⁺；
  **"consider “X” union all…∖X”"**——^{66}/″ LaTeX 引号还原）✓；Lemma 3.5 四性质（𝒳→X ×3
  修复/`o f`→of/**"iff connected" 花括号修复**/**"W Tis" 幽灵 T 删除**/exhaustion V_i）✓；
  Lemma 3.6（final collection/exhaustion）✓；**Definition 3.7**（dimension zero **iff** 修复/
  clopen）✓；Remark 3.8（orbits finite discrete or cantor/`,` 修复）✓；Lemma 3.9（Sⁿ/Rⁿ/
  general M 三段证明）✓ — **PASS**
- **p.013-018（§4 Steps 1-5）**：§4 标题 ✓；Proof of Theorem 1.5 开头 ✓；§4.1 Step 1（B(r)/
  η=2^{-10}/(i)(ii)(iii)/**[37]) 间距修复**；Newman [24, p6 Theorem 2]/Dress [6, p204
  Theorem 1]/Smith ✓；B(3) chart/p^kZ_pB(2) ⊆ B(3) ✓；§4.2 Step 2（(4.1) **d_inv = ∫
d_{R³}(αx,αy)dµ_Harr(α)——"Harr" 为 print 原文（文本层证实），源级登记不修**）✓；
  **Lemma 4.2**（X⁺ ⊆ B(1)/Z_p-invariant）✓；**Figure 1**（page_13 嵌入图 + caption ✓ p.14
  目检 genus-2 handlebody 图在位）✓；§4.3 Step 3（K₀ Definition 4.3/x₀ lowest z-coordinate/
  **"$\mathbb{Z}_p.$-invariant" 句点-in-math ×2 修复**）✓；Lemma 4.4（K∖Z_pA path-connected/
  **"A. Then" 句号**/**"∂K. Translating" 句号**）✓；Lemma 4.5（x₁ ∉ Fix/**"Fix. First" 句号/
  x₁ = x₀/x₀ ∉ Fix**/x₂′/γ: [0,1] → B(x₁,η) **箭头修复**/**γ: [0,1/2] → B(x₁,η) "1/·"→1/2 修复**/
  **(ii)(iv) ⇒ t = min(γ⁻¹(K)∖{0})**/L₀ = γ([0,t])/L = (Z_pL₀)⁺/diameter ≤ 4η）✓；
  **Definition 4.6** Z = K ∪ L ✓ — **PASS**
- **p.015-018（§4.4-4.5）**：Lemma 4.7（Z = Z⁺/nontrivial action）✓；(4.2) Mayer–Vietoris ✓；
  **Ĥ^i(K ∩ L)（\bar K 删除）修复**/**Ĥ²(L)（ĥ→2）修复**/**K = K⁺, L = L⁺ ⇒ Z = Z⁺. 句号** ✓；
  (4.3) ✓；**"functions to Z." 双句号修复**；**q(r) 定义 (4.4) tag 在位**/**(αq−q)(r) (4.5) tag 在位**/
  "x₁ ∉ Fix Z_p, so（**`,$,` 修复**）" ✓；**Lemma 4.5 x₁,x₂ same component/"A = ∅"** ✓；
  Lemma 3.1 Ĥ¹(Z) = lim→ H¹(N⁺)/**(Z)⁺′ stray prime 修复** ✓；**Definition 4.8**（map
  **H¹(N⁺) → Ĥ¹(Z) 箭头修复**/"containing Z, and" 句点修复/Z_p-invariant）✓；§4.5；
  **Lemma 4.9**（"Definition 2.4" \it 修复/U quasicylinder/R³∖U/Z ∪ (R³∖N⁺)₀/int(F) ball [2]/
  two ends/H₂(U) = Z）✓；**Lemma 4.10**（sufficiently 修复/finite orbits/least upper bound）✓；
  **Definition 4.11**（π₁-injective/"Z_p. Denote" 句号/ext(F) 句号补）✓ — **PASS**
- **p.016-018（Lemma 4.12-4.14）**：**Lemma 4.12**（homomorphism Z_p → MCG(F)/"groups
  appearing in **(4.6)–(4.9)**"（**\_/- 乱码 → –**）/"map MCG(F) → Aut(H₁(F))"（**拆 $ 合并 +
  句号**））✓；**(4.6) 交换图补 \tag**（H¹(N⁺)→H¹(int F)→Ĥ¹(Z), ↓H¹(F)）✓；**(4.7)
  H₁(Z) → H₁(int F) 补 tag**/**(4.8) H₁(M∖N⁺) → H₁(ext F) 重编（原错标 4.7）**/**孤儿 "(4.8)"
  行删除**/**(4.9) H₁(F) ≅ H₁(int) ⊕ H₁(ext) tag 核实** ✓；证明（**",$,我们" 修复 ×1**/
  ψ_α^t (4.10)/T_α/**"fixes Z, N⁺, and F." 修复**/**"from Z_p." 句号**/**(4.11) 组合式**/
  isotopic via ψ_β^t∘T_β∘ψ_α^t∘T_β⁻¹∘(ψ_{βα}^t)⁻¹/**"compact subset of U"（\dot U 修复）**）✓；
  **Lemma 4.13**（sufficiently 修复/**F → U 箭头修复**/"identity in Z_p." 句号/image nontrivial/
  (4.6)/**H¹(int F) → H¹(F)（ĥ→1）修复**/"H¹(R³) ≠ 0). Thus" 句号）✓；**Lemma 4.14**（rank
  four submodule/(4.12) 矩阵 ⊕/loops α₁,α₂,β₁,β₂/linking lk(α_i,β_j) = δ_ij（**句号修复**）/
  (4.7)(4.8)(4.9) 引用一致）✓；**"isomorphic to Z/p, and（`,$,` 修复）"** ✓；Remark 4.15
  （punctured genus two/α₁,β₁ enough/K₀ genus one）✓ — **PASS**
- **p.018-021（§5 + Lemma 5.1）**：**Lemma 5.1**（intersection form of F restricted to
  H₁(F)^{Z/p} taken modulo p rank ≤ 2）✓；Symonds [40, pp389–390 Theorem B]/Chen–Glover–
  Jensen [5, Theorem 1.1]（**拆 $ 修复**）/**"Symonds' result"（撇号补回）**/Nielsen [25] ✓；
  证明（classify all Z/p ⊆ MCG(F)/Nielsen [26] realization/**Kerckhoff [15]（双 f 修复）**/
  **notation switch：S̃ = F, 𝒮 = F/(Z/p), S = coarse space of 𝒮（script S 记号依 p.20 PNG
  修复 ×3）**/**S̃ → S cover 箭头修复**/α ∈ H¹(S, Z/p)/g, n）✓；**(5.1) case display 补 \tag +
  孤儿 "(5.1)" 行删除**（n = 0: (0 p;−p 0)^{⊕(g−1)} ⊕ (0 1;−1 0)；n > 0: (0 p;−p 0)^{⊕g}）✓；
  n = 0 情形（**MCG(Σ_g) → Sp(2g,Z) → Sp(2g,Z/p) 双箭头修复**/Sp transitive/Poincaré dual
  nonseparating ℓ/cut and glue p copies/H₁(S̃) ≅ H₁(Σ₁) ⊕ H₁(Σ_{g−1})^{⊕p}（**\bar H₁ 删除 +
  句号修复**）/multiplied by p）✓；n > 0 情形（orbifold points ∈ 𝒮/r_i evaluation/
  **"S̃ → S, and hence"（句点-in-math 修复）**/r_i(α) ≠ 0/∂𝒟 = ∂(𝒮∖𝒟) null-homologous in 𝒮
  （**S_{;} 修复**）/n ≥ 2 句号）✓；reduction（**"PNext" 幽灵 P 删除**/𝒟 ⊆ 𝒮/Take D and
  S∖𝒟/S′, S′′/⟨α, ∂D⟩ = Σr_i(α) = −r_n(α) ≠ 0（**断裂合并**）/**∂D lifts to single
  separating loop in S̃, exhibits S̃ as connected sum（S̃/幽灵 P 修复）**/H₁(S̃) = H₁(S̃′) ⊕
  H₁(S̃′′)) ✓；Case g = 0（**"in S, where"（S_{;} 修复）**/cellular chains/1-cycles/weights/
  **"lifts of e." 句号**/H₁(S̃)^{Z/p} = 0）✓；**Case n = 2（(5.2) 正合列 tag 在位**/(r₁,r₂)/+/α ∈
  A := (r₁,r₂)⁻¹(1,−1)/MCG(S rel {p₁,p₂}) transitive/**"on A. Let" 句号**/[ℓ] Poincaré dual/
  Dehn twist/**S̃ → S explicitly 箭头修复**/H₁(Σ_g)^{⊕p}/multiplied by p）✓ — **PASS**
- **p.021-024（References [1]-[47]）**：47 条逐条核对：[1] Agol MathOverflow 74935/**"Rˆ3"
  print 即此拼写，忠实保留** ✓；[2] Alexander PNAS 10(1) 1924 ✓；[3] Bing 1959 ✓；
  **[4] differentiable（修复）** ✓；[5] Chen–Glover–Jensen JP J. Geom. Topol. 11(2) 2011 ✓；
  [6] Dress Topology 8 (1969) ✓；[7] Freedman–Hass–Scott Invent. Math. 71 (1983) ✓；
  [8][9] Gleason Duke 18 (1951)/Ann. 56 (1952) ✓；[10] Gottschalk Bull. AMS 64 (1958) ✓；
  [11] Gulliver Ann. 97 (1973) ✓；[12] Hamilton Quart. J. Math. 27 (1976) ✓；
  **[13] J. Differential Geom.（修复）** ✓；[14] Kakimizu Hiroshima 22 (1992) ✓；
  [15] Kerckhoff Ann. 117 (1983) ✓；[16] Kirby–Siebenmann Princeton 1977（with Milnor/
  Atiyah notes, Annals Studies 88）✓；[17] Joo Sung Lee Commun. Korean Math. Soc. 12 (1997)
  ✓；**[18] Ĭozhe Maleshich（caron 归位）+ Hölder（修复）Uspekhi 52 (1997)** ✓；
  [19] Martin ERA AMS 5 (1999) ✓；[20] Mahan Mj Geom. Topol. 16 (2012) ✓；
  **[21] Affine（Afine 修复）** Moise Ann. 56 (1952) ✓；[22][23] Montgomery–Zippin ✓；
  [24] Newman Quart. J. Math. os-2(1) 1931（**print 即 os-2，忠实保留**）✓；
  **[25] Flächen（修复）** Danske Vid. Selsk 15 (1937) ✓；[26] Nielsen Acta Math. 75 (1943) ✓；
  [27][28] Osserman ✓；[29] Papakyriakopoulos Ann. 66 (1957) ✓；[30] Przytycki–Schultens
  TAMS 364 (2012) ✓；[31] Raymond–Williams Ann. 78 (1963) ✓；**[32] Dušan Repovš/
  Evgenij Ščepin（变音归位 + 标题内幽灵 ˘ 删除）Math. Ann. 308 (1997)** ✓；[33][34] Sacks–
  Uhlenbeck ✓；[35] Schoen–Yau Ann. 110 (1979) ✓；[36] Schultens J. Topol. 3 (2010) ✓；
  [37] P. A. Smith Ann. 42 (1941) ✓；[38] Spanier Ann. 49 (1948) ✓；[39] Steenrod Amer. J.
  Math. 58 (1936) ✓；[40] Symonds TAMS 306 (1988) ✓；[41] Tao Manuscript 2012
  terrytao.wordpress.com ✓；**[42] diffeomorphisms（修复）** Thurston Bull. AMS 19 (1988) ✓；
  **[43] sufficiently large（修复）** Waldhausen Ann. 87 (1968) ✓；[44] Walsh TAMS 217
  (1976) ✓；[45] Wilson Duke 40 (1973) ✓；[46][47] Yamabe Ann. 58 (1953) ×2 ✓ — **PASS**

## 总评

- **覆盖声明**：24/24 页经可靠文本层逐字符对账 + md 全文交叉核对（682 行全读）；150dpi 全
  24 页渲染，p.1/p.14 全页目检，p.2/4/13/19/20 定向裁片核足注/widehat/(5.1)/𝒮 记号。
- **FAIL 修复（116 处 / 92 规则）**：①足注碎片错位 ×4 组完整重构（fn1 NSS+Yamabe+Newman
  两动机、fn2 dimension reduction、fn3 Kakimuzu widehat、fn4 category/limit-colimit——碎片
  块删除、正文归位、fn4 内部乱序重排）；②方程编号 5 组补/重编 + 孤儿行 ×2 + \tag{4.6} 重复
  去重，修复后 \tag 清单 1.1-5.2 共 24 个与 print 一致无重复；③丢箭头 ×9；④ff 连字 ×26；
  ⑤变音 ×7 组（Čech/Dušan Repovš/Ščepin/Ĭozhe Maleshich/Flächen/Hölder/Symonds'）；⑥幽灵
  字符（Conjecture 1.3 处 "2"/PNext/W Tis/S_{;}×2/S̃ 后 P/p<sup>ˇ</sup>urpose/`·`）；⑦引号
  “X”/X” 还原；⑧𝒳→X（Lemma 3.5 iv）；⑨π₁- 拆裂 ×5；⑩句号/逗号-in-math ~25；⑪Kerckhoff
  双 f ×2；⑫控制字符 \x08\x0c\t ×2；⑬粗体/斜体杂项（boldsymbol S→𝒮、\dot U、\bar H₁、
  \bar K、ĥ→裸 H、(Z)⁺′）。
- **源级 quirk 清单（忠实不改）**：**"µ_Harr"**（(4.1) Haar 测度 print 即拼 Harr，文本层证实）；
  **"Yang [48]"**（print 正文引用 [48] 而文献表止于 [47]，悬空引用）；**"Rˆ3"**（[1] MathOverflow
  引文 print 即 caret 拼写）；**"os-2(1)"**（[24] Quart. J. Math. 旧刊编号 print 即此）；
  **"contradicts"**（fn2 "would like to conclude… and therefore contradicts" print 即第三人称
  直陈式）；**"it's just K₀"**（§4.3 print 即缩写）；**"if we make U thick enough"**（Remark
  4.15 print 即此）；[18] 作者 "Ĭozhe Maleshich"（print 罗马化即此形）。
- **可用性结论**：修复后 md 可作该 arXiv v3 论文忠实底本；(1.1)-(5.2) 全部 24 个编号方程
  逐条核对编号与内容一致；Conjectures 1.1-1.4、Theorem 1.5、Theorems 2.1/4-8 编号命题、
  Lemmas 2.2-2.19/3.1-3.9/4.2-4.14/5.1、Definitions 2.4-2.10/3.4/3.7/4.1/4.3/4.6/4.8/4.11 全部
  在位；四条足注完整重构；References 47 条抽验全对；Figure 1 嵌入图在位。本篇 24/24 页完成，
  无未决项；目录内无同篇其他版本。
