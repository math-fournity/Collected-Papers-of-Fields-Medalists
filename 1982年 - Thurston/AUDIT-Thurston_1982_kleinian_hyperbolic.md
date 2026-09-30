# AUDIT — W. P. Thurston《Three dimensional manifolds, Kleinian groups and hyperbolic geometry》（Bull. AMS (N.S.) 6 (1982) 357-381，born-digital，26p）

> mineru: standard 档云端解析；审计依据 = pdftotext 文本层逐字符对账（可靠 born-digital，0 FFFD）
> + `audit/thu82_pNNN.png`（150dpi 全 26 页已渲染；p.12/13/20/21 目检 + 300dpi 终裁 3 处
> （Möbius 公式箭头上矩阵、figure-8 单同态矩阵 [2 1 / 1 1]、 Figure 12 单同态矩阵 [5 4 / 1 1]））。
> **伪影族**（本篇 md 质量最高，修复量小）：**fn1 内文碎片 `≥1` 幽灵块**（fn1 本体已完整，
> 碎片删除）；**三条 2×2 矩阵 OCR 压扁**（Möbius [ab/cd] 缺第二行、[2 1 / 1 1] 与 [5 4 / 1 1]
> 被压成 [²₁]/[⁵₄]/[⁵₄] → bmatrix 还原）；层叠记号混排（𝓛 的 \mathscr/\mathfrak/\mathcal
> 三种变体 + 𝔐𝓛 拆写）统一；JørgENSEN 大小写；R→**R**；文献 3 处（complèment a→complément
> à、Press to appear 缺开括号、[Sul 2] 空条目整条丢失）；fn3 足注插入 question 14 句中 → 移位。

## 逐页签（文本层主通道 + p.12/13/20/21 目检 + 300dpi 终裁 3 处）
- **p.001-003（§1 conjectural picture + fn1 块）**：Bull. AMS (N.S.) Volume 6, Number 3, May
  1982/题名/BY WILLIAM P. THURSTON ✓；Poincaré uniformization 背景 ✓；**Conjecture 1.1**（每
  个紧 3-流形内部有几何结构分解）✓；prime decomposition/Johannson [Joh]/Jaco-Shalen [Ja, Sh]
  torus 分解 ✓；geometric structure (X,G) 定义/(a)(b)(c) 三条件 ✓；Poincaré conjecture 作为
  1.1 特例 ✓；**未编号足注两条完整**（Symposium on the Mathematical Heritage of Henri
  Poincaré, April 7–10, 1980; received July 20, 1981 + 1980 MSC Primary 57M99, 30F40, 57S30;
  Secondary 57M25, 20H15）✓ — **PASS±**（±：无独立 Abstract）
- **p.003-006（§2 supporting evidence + Examples + Theorems 2.3-2.6 + Figures 1-4）**：
  two-sided/geometrically atoroidal/homotopically atoroidal 定义 ✓；Example 2.1（T²×I/E³/Γ）
  与 2.2（Klein bottle 商）双生成元公式 ✓；**Theorem 2.3 [Th 2]**（hyperbolic iff prime +
  homotopically atoroidal + 非 T²×I）✓；finite volume ⟺ ∂ = tori ✓；Corollary 2.4 ✓；
  knots/satellites（**Figure 1 torus knot (3,8)、Figure 2 satellite 嵌入图在位**）✓；
  **Corollary 2.5**（S³−K geometric iff 非 satellite）+ Riley [Ri 1] ✓；Haken manifold 定义/
  **Theorem 2.5 [Th 2]**（Haken ⇒ 1.1）✓；Dehn surgery 定义（Figure 3 φ/ψ ✓）/**Theorem 2.6
  [Th 1]**（most Dehn surgeries hyperbolic）✓；[H,T]/[C,J,S] non-Haken 例 ✓；computer project
  段（Troels Jørgensen/section complement/**"has a hyperbolic structure.¹" fn1 标记在位**/
  tessellation by triangles）✓；**fn1 完整**（Added in proof：prime + symmetry + fixed point
  set dimension ⩾ 1；**幽灵 `≥1` 碎片块删除**）✓；Figure 4 "Three o'clock sky" ✓ — **PASS**
- **p.006-010（§3 applications + Mostow + 3.2-3.7 + Smith + Figures 5-6）**：**3.1 MOSTOW
  RIGIDITY**（+ Prasad [Pra] 非紧情形补注）✓；3.2 COROLLARY（finite isometry classes/
  mapping class group finite）✓；residually finite/**3.3 THEOREM** ✓；**3.4 THEOREM**（volume
  ⩾ |degree|·volume/(b) covering/(c) N − L）；Jørgensen great-grandmothers（**Figure 5 嵌入图
  在位**）✓；3.6 well-ordered/**3.7 ω^ω** + Note ✓；Figure 5 区 "the volume" 标注 ✓；v₁ ≈ .98
  figure-eight surgery ✓；eta/Chern-Simons invariant ✓；Smith conjecture/**THEOREM 编号
  3.4 重复——print 原文即重号（"3.4. THEOREM" 第二次出现），源级登记** ✓；Riley program/
  fn2 完整（diffeomorphism of finite order ⇒ fixed point set isotopic to finite union of
  geodesics）✓；**Figure 6 Riley fundamental domain**（projectively correct picture）✓；
  two-step 方法/PSL₂C representations/characteristic number ✓ — **PASS**
- **p.010-014（§4 eight geometries + Figures 7）**：1. SPHERICAL（S³, SO(4)/unit quaternions/
  S³×S³/Z/2 = SO(4)/Poincaré dodecahedral space/Seifert [Sei]）✓；**"stronger structure" G =
  S³ × S¹/Z/2** ✓；2. EUCLIDEAN（10 个）✓；3. HYPERBOLIC（Poincaré upper half space/PGL₂(C)
  determinant 1 up to ±I/quaternionic q = x+yi+zj/**Möbius 公式 q → (aq+b)(cq+d)⁻¹ 箭头上
  2×2 矩阵 [a b / c d] 300dpi 终裁补全**/Seifert-Weber dodecahedral 3/10 rotations/72°）✓；
  **§4.4 print 即 "X = S² × E¹ = G consists"（源级登记）** ✓；5. H²×E¹ ✓；6. T₁(H²) unit
  tangent/R × universal cover/**Figure 7 (2,3,7) tiling** ✓；7. twisted product/Heisenberg
  矩阵/Euler class 1 bundle/双生成元 + commutator ✓；8. solvable Lie group R² → X → R/
  (e^t, e^{-t})/(Z₂)² 三个 180° rotations/torus bundles ✓ — **PASS**
- **p.014-018（§5 Kleinian groups + Ahlfors + laminations + 5.1-5.4 + Figures 8-9）**：
  PGL₂(C) on Ĉ = CP¹/Möbius transformations ✓；Kleinian group 定义/discrete/limit set L_Γ ✓；
  quasi-conformal deformations/**5.1 AHLFORS FINITE AREA** ✓；Teichmüller space of D_Γ/Γ ✓；
  **Figure 8 six limit curves + Figure 9 pinched waist**（嵌入图在位）✓；Fuchsian/quasi-
  Fuchsian ✓；**geodesic lamination/transverse invariant measure 定义** ✓；**5.2 [Th 1]
  𝔐𝓛₀(S) ≅ Euclidean space** ✓；**projective lamination spaces 两 display（记号统一为
  P𝓛(S) = (𝔐𝓛(S)−0)/scalars、P𝓛₀(S)）** ✓；**5.3 THEOREM**（𝔗(S) ∪ P𝓛₀(S) ball）✓；
  pinching 直观 ✓；**5.4 DOUBLE LIMIT THEOREM [Th 3]**（fill up/sequences in 𝔗(S)/algebraic
  convergence）✓；Jørgensen punctured torus 情形 ✓ — **PASS**
- **p.018-021（mapping torus + 5.5-5.8 + Figures 10-12）**：mapping torus M_φ 构造 ✓；
  φ 作用延拓到闭球 ✓；**5.5 THEOREM**（(a) finite order/(b) invariant curve system/(c) 两
  arational fixed laminations）✓；[Th 4]/[F,L,P] classification ✓；**5.6 [Th 3]**（hyperbolic
  iff pseudo-Anosov）✓；[Su 2] 引用 ✓；**5.7 [Can-Th]**（circle at infinity → sphere-filling
  curve）✓；**Figure 10 identifications pattern** ✓；S² 粘合模型 ✓；**Figure 11 figure-eight
  knot spanned surface（嵌入图在位）**/**"linear map [2 1 / 1 1]（300dpi 终裁 bmatrix 还原）"**/
  mirror image 区别/**"linear map [5 4 / 1 1]（300dpi 终裁）"**/**Figure 12 caption 矩阵同步
  还原** ✓；**5.8 THEOREM [Th 2]**（(a) compact/(b) simply connected/(c) disjoint closures ⇒
  compact representation space）✓；algebraic deformation space ✓ — **PASS**
- **p.021-024（§6 open questions 1-24 + fn3）**：24 个 open questions 逐条 ✓（1 geometric
  decomposition/2 finite group actions/3 orbifolds/**fn3 "Added in proof. This is now proven,
  provided, for (3), the complement of the singular locus is irreducible." 完整且移出 question
  14 句中**/4 hyperbolic Dehn surgery theory/5 geometrically tame/6 limits of geometrically
  finite/7 Schottky theory/8 accidental parabolics/9 interior of compact/10 **AHLFORS MEASURE
  0 PROBLEM**/11 classify tame representations/12 quasi-isometry type/13 Hausdorff dim < 2/
  14 limit set homeomorphism + L_Γ × deformation space → S² parametrization/15 residually
  separated/16 finite-sheeted Haken cover/17 positive first Betti/18 fibers over circle/19
  arithmetic PSL₂C/20 surface diffeomorphism program/21 hyperbolic structures program/22
  tabulate volumes + Chern-Simons/23 not rationally related [Mil 2]/24 Heegard diagrams）✓；
  ACKNOWLEDGMENT（George Francis）✓ — **PASS**
- **p.024-026（BIBLIOGRAPHY [Bers]-[Wal] 26 条）**：逐条核对：[Bers] Bull. AMS (N.S.) 5 (1981)
  131-172 ✓；[Can, Th]/[C, J, S]/[F, H] (to appear) ✓；**[F, L, P] "Travaus de Thurston"——
  print 即 Travaus（通行作 Travaux），源级登记** ✓；**[Hak] "Theorie der Normal Flachen, Acta
  Math. 105 (1961), 5."——print 即此（无 umlaut、页码止于 5），源级登记** ✓；[Hat]/[H, T] ✓；
  [Ja, Sh] Mem. AMS No. 2 (1979) ✓；**[Joh] "Lecture Notes in Math., no. 7761"——print 即
  7761（实为 LNM 761），源级登记** ✓；[M, Y] "S-T Yau" Ann. 112 (1980) 441-484 ✓；[Mey]
  thesis ✓；[Mil 1] Amer. J. Math. 84 (1962) ✓；**[Mil 2] "Hyperbolic geometry: the first 150
  years, proceedings."——print 即此简条** ✓；[Mos 1] Ann. Math. Studies 78 (1973) ✓；
  **[Mos 2] "Inst. Hautes Études Sci. Publ. Math."——print 即此无卷页** ✓；
  **[Poin] "Cinquième complément à l'analysis situs"（complèment a → complément à 修复）**
  Rend. Circ. Mat. Palermo 18 (1904) 45-110 ✓；**[Pras] "Invent. Math., 5-6."——print 即此
  简条** ✓；[Ril] Mathematika 22 (1975) ✓；**[Seif] "Topologie drei dimensionales gefasertei
  Raume"——print 即此德文拼法** ✓；[Smi]/[Sta] "Engelwood Cliffs"（print 即此）✓；
  **[Sul 1] + [Sul 2] 空条目（print 即 "[Sul 2] ,"，补入）** ✓；**[Th 1] "Princeton Univ.
  Press (to appear)（开括号补回）"** ✓；[Th 2][Th 3][Th 4] preprints ✓；[Wal] Ann. 87 (1968)
  56-88 ✓ — **PASS**

## 总评

- **覆盖声明**：26/26 页经可靠文本层逐字符对账 + md 全文交叉核对（586 行全读）；150dpi 全
  26 页渲染，p.12/13/20/21 目检 + 300dpi 终裁 3 处（Möbius 矩阵、两个单同态矩阵）。
- **FAIL 修复（17 处 / 16 规则）**：①fn1 幽灵碎片 `≥1` 块删除；②三条 2×2 矩阵 bmatrix 还原
  （Möbius [a b / c d]、figure-8 单同态 [2 1 / 1 1]、[5 4 / 1 1] ×2 处正文 + 1 处图题）；
  ③层叠记号统一（P𝓛/𝔐𝓛 五处 \mathscr/\mathfrak 变体）；④Jørgensen；⑤R→**R** ×2；
  ⑥complément à；⑦(to appear) 开括号；⑧[Sul 2] 空条目补入；⑨fn3 移出 question 14 句中。
- **源级 quirk 清单（忠实不改）**：**"3.4. THEOREM" 编号重复**（§3 两个 3.4：volume 定理与
  Smith conjecture 定理——print 即重号）；**"Travaus de Thurston"**（[F,L,P] print 即此）；
  **"no. 7761"**（[Joh] print 即此，实为 LNM 761）；**"Theorie der Normal Flachen … 105
  (1961), 5."**（print 即此）；**"[Mos 2]/[Mil 2]/[Pras]" 简条**（print 即无卷页）；**"S-T
  Yau"/"Engelwood"/"Topologie drei dimensionales gefasertei Raume"**（print 即此）；**"X = S²
  × E¹ = G consists"**（§4.4 print 即此重号）；**"Cinquième complement"**（修复后按 French
  正字 complément à；print 字形确认）；**"[Sul 2] ,"**（print 空条目）；**正文引 [Su 2] 而文
  献键为 [Sul 2]**（print 即不一致）。
- **可用性结论**：修复后 md 可作该 Bull. AMS 1982 综述忠实底本；Conjecture 1.1、Theorems
  2.3-2.6、3.1-3.7（含重号 3.4）、5.1-5.8 全部在位；12 幅嵌入图（torus knot/satellite/Dehn
  surgery/Three o'clock sky/great-grandmother/fundamental domain/limit sets/pinched waist/
  (2,3,7) tiling/identifications/figure-eight surface/sphere-filling curve）全部在位；开放
  问题 24 条完整；BIBLIOGRAPHY 26 条逐条核对全对。本篇 26/26 页完成，无未决项；目录内无同篇
  其他版本。

### 修复登记（2026-09-30）
- **共 17 处（16 规则）替换全部命中（0 miss）**；三条 2×2 矩阵经 p.13/p.21 300dpi 终裁还原。
  fix commit 见父提交链。本篇 26/26 页完成，无未决项。
