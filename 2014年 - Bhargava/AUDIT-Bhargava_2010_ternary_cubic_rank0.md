# AUDIT — M. Bhargava & A. Shankar《Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0》（arXiv:1007.0052v2，LaTeX born-digital，25p）

> mineru: standard 档云端解析；审计依据 = pdftotext 文本层逐字符对账（可靠 born-digital，0 FFFD）
> + `audit/bha2010_pNNN.png`（150dpi 全 25 页已渲染；p.1/16 全页目检 + 300dpi 终裁 5 处
> ——Ⅲ[3]、5∥Disc、5∥Cond、3∤v₅、(−2J/p) Legendre）。
> **伪影族**：Ⅲ[3]→"X[3]"、5∥/3∤ → "k"/乱 mathbin、变音拆裂（Veränderlichen/Nekovář/
> Astérisque/Séminaire/Birkhäuser/Sér）×8、丢箭头、"$;" 标点粘连 ~15、"12^s"/"E^{I,𝓘}"/
> "sati fy"/"going of"/"E^*" 等。

## 逐页签（文本层主通道 + p.1/16 全页目检）
- **p.001（题录 + §1 Introduction 前半）**：题名/两作者/December 25, 2013 ✓；height H(E_{A,B})
  定义/[9] 2-Selmer 平均 3/1.5 ✓；**Theorem 1**（3-Selmer 平均 4）/**Corollary 2**（1⅙<1.17）✓；
  Theorem 3（同余条件族）/Theorem 4（rank 0 正比例）✓；Theorem 5（Ⅲ finite 假设 rank 1）✓ —
  **PASS±**（±：arXiv 边条未收）
- **p.002-004（§1 后半）**：Theorem 6（analytic rank 0）/Corollary 7（BSD 正比例）✓；
  binary quartic [9]/mwrank ✓；V_ℤ/SL₃(ℤ)/invariants I,J/(1) Hessian/(2) 𝓗(𝓗(f))/(3) Δ=(4I³−J²)/27 ✓；
  Aronhold S,T（S=16I,T=32J）✓；H(f) (4)/degree 12/"degree 12" 乱码修复 ✓；strong irreducibility
  定义 ✓；**Theorem 8** (a)(b) 32/45、128/45 ζ(2)ζ(3)X^{5/6} ✓；eligibility/Theorem 9
  （mod 64 十条 + mod 27 四条——两列逐条核对全对）✓；"generalized binary quartics" [15][25] ✓；
  **Theorem 10** (a)(b) 3ζ(2)ζ(3) ✓；n-covering 定义/两张交换图（Figure page_4_image_1）✓；
  soluble/locally soluble ≅ E(ℚ)/nE(ℚ), Sₙ(E) ✓；Cassels [14, Theorem 1.3]/(5) Jac(C) 方程 ✓；
  S_σ 构造四 bullet/[15] minimization ✓；de Jong [20]/4+ε(q) ✓；论文组织（[6] averaging
  method/cusps going off 修复）✓ — **PASS**
- **p.005-007（§2.1 Reduction theory）**：V_ℝ^±/GL₃⁺/flexes 9（Bezout）✓；Weierstrass 形 (6)
  （I=−3A,J=−27B）✓；L⁺/L⁻ 基本集 ✓；bounded coefficients ✓；**Lemma 12**（stabilizer=3）✓；
  𝓕=N′A′Kλ Siegel set/K,A′,N′,Λ 定义（大式阵）✓；ν(a)/multiset/(7) m(f) ✓；measure 0 论证 ✓；
  R_X(h·L±) ✓；Lemma 19 前引/averaging ✓ — **PASS**
- **p.008-010（§2.2-2.4）**：G₀/dh 归一化（s₁^{-6}s₂^{-6}）✓；(8) N(S;X)/C_{G₀}=3∫dh ✓；
  B(n,s₁,s₂,λ,X)/(9) ✓；**Lemma 13**（cuspidal regions/x³,x²y,x²z 系数界）✓；✷ ✓；
  V_ℤ^red/**Lemma 14**（main body negligible）✓；**Proposition 15 (Davenport)** ✓；
  λ∈[c₁,X^{1/36}] ✓；(10) 误差 O(X^{3/4}) ✓；主项/(11) N=⅓Vol ✓；§2.3/**Proposition 16**
  (12) 4/9 变测度/𝓕_PGL₃/3ζ(2)ζ(3) [35] ✓；(13)/(14)/(15) 8/5、32/5 ✓；**(16)** Vol=32ζζ/15、
  128ζζ/15 ✓；§2.4/Theorem 17 (17) ✓ — **PASS**
- **p.011-013（§2.4 末-2.6）**：**Theorem 18**（weighted (18)/φ̃_{p_j}）✓；§2.5 Lemma 14 证明
  （p≡1 mod 3/三个立方类/S_p 密度 1/p/(19) 发散）✓；**Lemma 19**（bigstab/ō(X^{5/6}) 乱码修复）
  ✓；Jac(f) Weierstrass 嵌入/3-torsion=flexes/f_b 非剩余/(20) ✓；§2.6/**Proposition 20**
  （Weierstrass cubic/[3, Equation 1.5]/c₄/16,c₆/32）✓；**Proposition 21 (Kraus [33])**
  (a)(b)(c) ✓；**Lemma 22**（144 translates of ⅟₃₆ℤ×⅟₂₇ℤ）✓；**Proposition 23** (a)(b)
  32/135、128/135（**第二 (a)→(b) 标签修复**）✓ — **PASS**
- **p.014-016（§2.7 + §3 开头）**：acceptable 函数定义 ✓；**Theorem 24** (21) ✓；
  **Proposition 25** (22) tail estimate/W_p^{(1)}/W_p^{(2)} ✓；[7, Theorem 3.3] (23)/(24) ✓；
  nodal/[0:0:1]/(25) 映射/**Lemma 26**（3 to 1）✓；(26)/(27) ✓；§3/(28) E(A,B)/p⁴∤A if p⁶∣B ✓；
  (29)(30) I=−3A,J=−27B/H′ ✓；F_Σ/Σ_∞/large family 定义 ✓；**Theorem 27** ✓；
  §3.1 扭作用 (31)/K-soluble ✓ — **PASS**
- **p.016-018（§3.1 末-3.3）**：**p.16 全页目检**（Proposition 29/30/Lemma 12 证明/
  Proposition 31 (32) 双积分式/脚注 1 PGL₃(ℚ)-equivalence class 定义）✓；
  **Proposition 28**（𝒯_E 注入/E(K)[3] stabilizer）✓；**Proposition 29**/[24, Remark 2.8] ✓；
  [15, Theorem 1.1]/**Proposition 30**（footnote 1）✓；Lemma 12 证明（[27, Chapter 13]）✓；
  §3.2 **Proposition 31**（𝒥 常数/(32)）✓；**Proposition 32**（(33) |𝒥|_p 公式——分式结构
  逐项核对）✓；**Lemma 33**（(p²−p)#PGL₃(𝔽_p)/triples (C,L,B)）✓；**Lemma 34**（p≠3:1,p=3:3，
  引 Lemma 40）✓；|𝒥|_p=|3|_p(p−1)/(pVol(π(S))) ✓；Vol(π(S)) 三情形（(p−1)/p、2/81、2）✓；
  𝒥=4/9 ✓ — **PASS**
- **p.019-021（§3.3-3.4）**：m(f)/m_p(f) 定义（Aut_ℚ/Aut_ℤ 权）✓；**Proposition 35**
  （m(f)=∏m_p(f)）✓；S(F)/S_p(F)/**Proposition 36**（(34) M_p(V,F) 局部质量）✓；
  M_p(F) (35)/M∞(F;X) (36)/M∞(V,F;X) ✓；**Theorem 37** (37)=[9, Theorem 3.17] ✓；
  bad at p/**Proposition 38**（Lang-Weil [34]/Hensel/γ=diag(p^{−a},1,p^b) 论证）✓；
  **Theorem 39** (38) 极限式 ✓；证明 (39) 三行链（4/9 消去）✓；**Lemma 40**（p≠3/p=3/
  Lutz [39, Chapter 7, Proposition 6.3]/snake lemma 图 page_19_image_7）✓；正合列 ✓ — **PASS**
- **p.022-023（§4 rank 0/1 + Theorem 41/42）**：62.5% ✓；奇偶分布策略 ✓；Nekovář [36]（变音修复）✓；
  **Theorem 41**（25% rank 0；Ⅲ finite ⇒ 5/12>41.6% rank 1）✓；family F 构造预告 ✓；
  **Theorem 42 (Dokchitser–Dokchitser)**（r_p(E)=s_p−t_p 奇偶=root number）✓；
  证明：100% r_p=s_p/平均≤4/50% 奇数 ⇒ ≥3 元素/偶数平均≤5/size 1,9,≥9 ⇒ 至少半数 =1 ✓；
  **Ⅲ[3] trivial（"X[3]"→Ⅲ[3] 300dpi 修复）**/Cassels square/size 3,27,≥27/平均≤7/5/6=3 ✓；
  root number ω(E)=−∏ω_p(E)/[37]/split ⟺(−2J/p)=1/J(E_{−1})=−J(E)/p≡1 mod 4 ✓；
  family F 三条件（2-adic units/square-free away from 2/Δ′≡1 mod 4）✓；[41, Lemma 12] ✓ — **PASS**
- **p.024-025（§4.2 + Acknowledgments + References）**：**Theorem 43 (Skinner–Urban)** (a)-(d)
  （**5∥Cond/3∤v₅ 修复**）✓；ρ̄(E,3)/[40, Theorem 2] ✓；**Theorem 44**（5∥Disc/50% root +1/
  25% analytic rank 0）✓；Duke [23, Theorem 1]/[16, Proposition 2.12] ✓；family F 条件 ✓；
  Theorem 6 and Corollary 7 ✓；Acknowledgments（Cremona/de Jong/Fisher/Ho/Poonen/Shah/
  Skinner/Stoll/Testa/Urban/Wang/NSF DMS-1001828）✓；**References [1]-[41] 逐条抽验 18 条全对**
  （[2] Veränderlichen（变音修复）✓/[23] C. R. Acad. Sci. Paris Sér. I Math.（修复）✓/
  [26] courbes elliptiques（补词修复）✓/[36] Nekovář, Astérisque 310（修复）✓）✓ — **PASS**

## 总评

- **覆盖声明**：25/25 页经可靠文本层逐字符对账 + md 全文交叉核对；150dpi 全 25 页渲染，
  p.1/16 全页目检 + 300dpi 终裁 5 处（Ⅲ[3]/5∥Disc/5∥Cond/3∤v₅/(−2J/p)）。
- **FAIL 修复（50 组，两轮）**：①Ⅲ[3]→"X[3]"（300dpi p.22 定谳 Ⅲ 符号）；②**5∥Disc(E)/
  5∥Cond(E)/3∤v₅(Cond(E))**——"k" 形 ∥/∤ 号恢复 ×4；③p²∤Δ 的 † 形乱码 ×5；④变音 ×8
  （Veränderlichen/Nekovář×2/Astérisque/Séminaire de Théorie/Birkhäuser×2/Sér./courbes
  elliptiques）；⑤"E^{I,𝓘}"→E^{I,J}；⑥标点粘连 ~20（"rank 0;$that$i s"、"at most^{7,}"、
  "degree 12^s"、"over 𝒬."、Q 普通体→blackboard 等）；⑦E^*→E、ō( )→o( )、posesses→possesses。
- **源级 quirk 清单（忠实不改）**：无重大源级 typo（本篇为精校 arXiv v2）；ff→f 连字族
  （diferent/dificult/coeficients/suficiently）。
- **可用性结论**：修复后 md 可作该 arXiv 论文忠实底本；(1)-(41) 编号公式逐条核对全对；
  Theorem 1-44/Corollary 2,7/Proposition 15-38/Lemma 12-14,19,22,26,33,34,40 全部在位；
  参考文献 41 条抽验 18 条全对。本篇 25/25 页完成，无未决项；与 ternary_cubic_published
  （35p，待审）同目录。
