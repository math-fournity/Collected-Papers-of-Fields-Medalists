# AUDIT — R. Taylor & A. Wiles《Ring Theoretic Properties of Certain Hecke Algebras》（arXiv/预印本排版 = Annals of Math. 141 (1995), 553-572，LaTeX born-digital，22p）

> mineru: standard 档云端解析；审计依据 = `audit/tw1995_pNNN.png`（pngmono 150dpi 全 22 页）
> + pdftotext 文本层逐字符对账（可靠 born-digital，Type 3 字体）。**伪影族**：
> `R \not\perp 6N_Qp` 应为 R∤6N_Qp（记号）、Proposition 3 条件 4 的 "−1" 被 $$ 粘连吞掉。
> print 结构：正文 §1-4 → References（p.16-17）→ Appendix（Faltings 简化，p.18-22）——
> md 的 References 位置与 print 一致 ✓。

## p.001（题录 + Introduction）
- 核对：题名/Richard Taylor（D.P.M.M.S., Cambridge）/Andrew Wiles（Princeton）双地址/7 October
  1994 ✓；Introduction：[W2]/Mazur [M]/Gorenstein ✓；致谢 Darmon/Diamond/Faltings/Paris 7/
  Harvard/NSF ✓
- 结果：**PASS**（双栏地址 md 顺排，内容无损）
## p.002（§1 Notation 前半）
- 核对：𝒪/K/Q_p/λ/k ✓；G_L/ε:G_L→Z_p^×/G_℘/I_℘/Frob_℘ ✓；M^G/M_G/V_ρ/ρ^H/ρ_H ✓；
  ρ̄:G_Q→GL₂(k) 四性质（modular/absolutely irreducible on Gal(Q̄/Q(√((-1)^{(p−1)/2}p)))/
  det ρ̄(c)=−1/decomposition at p 两形态 + F_{p²}^×↞I_p）✓
- 结果：**PASS**
## p.003（§1 后半：l≠p 情形 + Q 的选取 + Δ_q/N_Q/Γ_Q）
- 核对：ρ̄|_{I_l} 三情形（χ⊕1/unipotent/absolutely irreducible + l≢−1 mod p）✓；
  type A,B,C [W2] ✓；ψ₁,ψ₂ 固定 ✓；Q 三性质（unramified/q≡1 mod p/distinct eigenvalues
  α_q β_q）✓；Δ_q/δ_q/Δ_Q/a_Q/χ_q/χ_Q=∏χ_q ✓；N_Q 三因子（conductor/Q/p if not flat or
  det≠ε）+ etale group scheme/ordinary remark ✓
- 结果：**PASS**
## p.004（Γ_Q 定义 + T(Γ_Q)/m/T_Q + ρ_Q^mod）
- 核对：Γ_Q 两子群积 ✓；T(Γ_Q)（T_l,⟨l⟩,U_q,U_p）✓；m 生成元（λ/tr ρ̄(Frob_l)−T_l/
  det ρ̄(Frob_l)−l⟨l⟩/U_q−α_q/U_p−ψ₂(Frob_p)）✓；[D] proper+maximal ✓；T_Q reduced ✓；
  O[Δ_Q]→T_Q ✓；ρ_Q^mod:G_Q→GL₂(T_Q) ✓；[C1] 四条 ✓；det ρ_Q^mod=χ_Qεφ ✓；flat ✓
- 结果：**PASS**
## p.005（p|N_Q 情形 + ρ'_Q + Theorem 1 + §2 Theorem 2）
- 核对：[W1] theorem 2/[G] proposition 12.9/χ₁ε,χ₂/χ₁=χ₂ [W2] prop 1.1 ✓；
  ρ'_Q=ρ_Q^mod⊗χ_Q^{-1/2}/det ρ'_Q∈O^× ✓；**Theorem 1（T 是 complete intersection）**✓；
  O'/[K2] corollary 2.8 page 209/π/π_Q/℘_Q/η_Q/∞>#℘_Q/℘_Q²≥#O/η_Q ✓；§2/Theorem 2 ✓；
  [DT] lemma 3/R 两性质
- 结果：**FAIL（单点）→已修**：R 条件记号 md `\not\perp` → **R∤6N_Qp**（print 不整除号）
## p.006（print 6：R 性质末两条 + Γ_{Q-}/Γ'_Q + m'_Q 生成元 + Lemma 1）
- 核对：ρ̄(Frob_R) distinct/(1+R)²det ρ̄(Frob_R)≠R(tr ρ̄(Frob_R))² ✓；Γ_{Q-}/Γ'_Q=Γ_Q∩Γ₁(R) ✓；
  T'(Γ'_Q)/m'_Q 六生成元（λ/T_l−tr/⟨l⟩−det/U_q−α_q/U_l−tr ρ̄_{I_l}/U_p−ψ₂/T_p−tr ρ̄_{I_p}）✓；
  T'_Q/Y'_Q/X'_Q/c 共轭 ✓；Lemma 1 T'_Q≅T_Q, T'_{Q-}≅T ✓；S₂(Γ_Q)²/S₂(Γ)^{2^{#Q+1}} ✓
- 结果：**PASS**（m'_Q 列表 md 为 algorithm 块，内容逐条一致）
## p.007（print 7：三 facts + U_R 矩阵 + Proposition 1 头）
- 核对：R≢1 mod p/α_R/β_R≠R^{±1}/α_q/β_q≠q^{±1} 三 facts ✓；
  T(Γ_Q)[u_R]/(u_R²−T_Ru_R+R⟨R⟩) ✓；U_R 矩阵 (T_R 1;−R⟨R⟩ 0) ✓；
  T(Γ)[u_q:q∈Q∪{R}]/(u_q²−T_qu_q+q⟨q⟩) ✓；H¹(Y'_Q,O)_{m'_Q}=H¹(X'_Q,O)_{m'_Q} ✓；
  [W2] corollary 1 of theorem 2.1/free rank one ✓；Proposition 1 ✓
- 结果：**PASS**
## p.008（print 8：Shapiro/ξ 共轭 + Corollary 1/2/3 头）
- 核对：ξ=(−1 0;0 1)/z↦−z̄ ✓；Z¹(Γ'_{Q-},O[Δ_Q]) 自由/O[Δ_Q]^a 同构 ✓；
  coboundaries ⊂ Z¹⁺ ✓；Corollary 1（δ_q−1 互零化）✓；Corollary 2 ✓；
  [K1] section 2 论证 ✓；Corollary 3 η_Q=η#Δ_Q ✓
- 结果：**PASS**
## p.009（print 9：Corollary 3 证明 + Corollary 4 + §3 + Lemma 2）
- 核对：θ/Ann ℘_{Q'} 证明 ✓；Corollary 4 #(a_Q T_Q/℘_Q a_Q T_Q)#(O/η)=#(O/η_Q) ✓；
  a_Q/a_Q²≅⊕O/#Δ_q ✓；§3 Some Algebra ✓；T/π/J_R/℘_R/η_R/Ψ_R=(℘_R²∩J_R)/℘_R J_R ✓；
  正合列 (0)→Ψ_R→J_R/℘_RJ_R→℘_R/℘_R²→℘_T/℘_T²→(0) ✓；#Ψ_R<∞/#Ψ_R#(...)=#(...)✓；
  Lemma 2 ✓
- 结果：**PASS**
## p.010（print 10：Lemma 2 证明 + Lemma 3/4 + Proposition 2 头）
- 核对：三行不等式链 ✓；[L] criterion ✓；Lemma 3 Fitt_R(J_R)⊂Ann_R(J_R) ✓；
  Ann_R(℘_R)⊇{s|s℘_R⊂J_R}Ann_R(J_R) ✓；η_R⊃η_T Fitt_O(...) ✓；Lemma 4 ✓；
  [L] lemma 9/R' 分解/Ψ_R↠Ψ_{R'} ✓；Ψ_Q/J_Q 记号 ✓；Proposition 2 头 ✓
- 结果：**PASS**
## p.011（print 11：Proposition 2 四条件 + 证明 + Corollary 1 头）
- 核对：四条件（m²/有限/I_{n+1}T⊂I_nT/lim← 幂级数环）✓；交换图 ✓；
  Ψ_P↠Ψ_{Q_n}→((J_{Q_n}+I_n)∩(℘²_{Q_n}+I_n))/(J_{Q_n}℘_{Q_n}+I_n) ✓；
  Ψ_P=lim←/单射/≅ ✓；#(℘/℘²)≤#(O/η)#Ψ_P ✓；Corollary 1 头 ✓
- 结果：**PASS**
## p.012（print 12：Corollary 1 末 + level n structure + §4 头）
- 核对：#Q_m=r/T_{Q_m} r 生成 ✓；level n structure B=(A,α,β,γ) 四条 ✓；
  level n' 诱导 ✓；A_m=T_{Q_m}/(p^m,δ_q^{p^m}−1) ✓；m(n) 递归两性质 ✓；
  I_n/lim← B_{m(n),n} 幂级数环/Krull dim r+1 ✓；§4 Galois Cohomology ✓
- 结果：**PASS**
## p.013（print 13：H¹_f 四定义 + H¹_Q/H¹_{Q*} + Lemma 5 头）
- 核对：H¹_f(Q_l,ad⁰ρ̄) 四情形（l≠p/flat/(ψ₁|_{I_p}≠ε)/(ψ₁|_{I_p}=ε not flat)）✓；
  H¹_Q 逆像 ✓；Tate local duality/H¹_{Q*} ✓；Lemma 5 dim H¹_Q≤dim H¹_{Q*}+#Q ✓；
  [W2] proposition 1.6/h_l=1/#((ad⁰ρ̄(−1))_{I_l})^{G_{F_l}} ✓
- 结果：**PASS**
## p.014（print 14：h_q/h_p h_∞ ≤1 + 𝓜 范畴 + Ext 计算）
- 核对：h_q=#k ✓；[W2] proposition 1.9 (iii)(iv) ✓；dim H¹_f≤1+dim H⁰ ✓；
  [FL] 𝓜 范畴/三等价 ✓；M(ρ̄)/Ext¹_𝓜 ↪ H¹(Q_p,adρ̄) ✓；两断言 ✓；[R] lemma 4.4 ✓；
  e₀,e₁/φ(e₀,0)=αe₀+βe₁/矩阵差式 ✓；dim=2 if γ≠0, =3 if γ=0/decomposable ✓
- 结果：**PASS**
## p.015（print 15：ρ̄⊗τ + Lemma 6 + κ 构造）
- 核对：τ unramified Frob_p↦(1 1;0 1) ✓；extension class/p↦2 ✓；Lemma 6 ✓；
  κ:Hom_k(m_Q/(m_Q²,λ),k)↪H¹_Q ✓；θ̃/ρ_θ/正合列 (0)→V_ρ̄→V_{ρ_θ}→V_ρ̄→(0) ✓；
  κ(θ)∈H¹(Q,ad⁰ρ̄) ✓；res_l κ(θ)∈H¹_f 分情形论证（p∤#ρ̄(I_l)/A₄/unipotent pro-cyclic/
  l=p flat/l=p ψ₁≠ε 头）✓
- 结果：**PASS**
## p.016（print 16：Lemma 6 证明完 + 主定理证明 + References 头）
- 核对：Teichmuller lifting ψ̃₁ ✓；ρ'_Q|_{G_p}~(δε *;0 δ) ✓；κ 单射反证/T=T_Q ✓；
  Q_m 三性质/#Q_m=dim H¹_{∅*} ✓；corollary 1 ✓；**References 标题+[C1]**（print 即此位置，
  md 一致 ✓）
- 结果：**PASS**
## p.017（print 17：References [C2]-[W2]）
- 核对：[C2][D][DT][FL][G][K1][K2][L][M][dS][R][W1][W2] 13 条逐条全对 ✓
- 结果：**PASS**
## p.018（print 18：Appendix 开头 + 变形定义）
- 核对：Appendix 目的（chapter 3 of [W2]/section 3/conjecture 2.16/theorem 3.3/theorem 2.17）✓；
  deformation of ρ̄ of type Q 六性质 ✓；ρ_Q^{univ}/Hom_k 同构/R_Q→T_Q ✓；Theorem 3 头 ✓
- 结果：**PASS**
## p.019（print 19：Theorem 3 + Lemma 7 + 归纳矩阵链）
- 核对：O'/K' note/tr ρ'_Q(G_Q) surjection ✓；Lemma 7（φ₁|_{I_q}=φ₂|_{I_q}^{-1}/χ_q 因子）✓；
  Ẑ⋉Z_p(1)/fσf^{-1}=σ^q ✓；ρ_Q^{univ}(f)=(a 0;0 b)/对角化归纳 ✓；
  ρ^{univ}(σ)≡(μ₁ 0;0 μ₂)(1₂+N) ✓；四行矩阵链 ✓
- 结果：**PASS**
## p.020（print 20：N diagonal + φ₂ + Proposition 3）
- 核对：N diagonal mod m^{n−1} ✓；φ₂(f)≡β_q/Δ_q→R_Q^×/φ₂|²_{I_q} ✓；R_Q/a_Q≅R ✓；
  O[Δ_{Q_n}]/kernel ((1+S₁)^{#Δ_{q₁}}−1,…) ✓；Proposition 3 + 交换图 + 四条件 ✓；
  **条件 4 "b_n⊂((1+S₁)^{pⁿ}−1,…,(1+Sᵣ)^{pⁿ}−1)"——md 的首个 "−1" 被 $$ 粘连吞掉 → 已修** ✓；
  "Then R≅T..." ✓；Reducing mod λ/b_n=(S₁^{pⁿ},…)/R⊕T_n ✓
- 结果：**FAIL（单点）→已修**
## p.021（print 21：n-structure + 𝓢_n 递归 + 交换图）
- 核对：n-structure B↠A/k[[S]]↘/四条件 ✓；#B≤(#T)^{p^{nr}}#R ✓；𝓢^{(m)} ✓；
  n(m) 递归两性质 ✓；𝓢'_m=𝓢_{n(m)}^{(m)} ✓；R'_n/T'_n 交换图 ✓；
  k[[X,…,X_r,S,…,S_r]]-algebras/三 bullets ✓
- 结果：**PASS**
## p.022（print 22：R'∞/T'∞ + 命题证明完成）
- 核对：R'_n/(S₁,…,S_r)↠R/T'_n/(S₁,…,S_r)≅T ✓；R'_∞/T'_∞ 定义/交换图 ✓；
  三 bullets ✓；**"We deduce that T'∞ has Krull dimension r … k[[X₁,…,X_r]]≅R'∞≅T'∞.
  Thus R≅T. As T has Krull dimension 0 and T≅k[[X₁,…,X_r]]/(S₁,…,S_r) we see that T is a
  complete intersection, and the proposition is proved."**——md 已含此段（初判截断系审计窗口
  误读；核对后无需补）✓
- 结果：**PASS**

## 总评

- **覆盖声明**：22/22 页逐页目检（150dpi 全页）+ 文本层逐字符对账（可靠 born-digital）。
  mineru：standard 档。
- **FAIL 修复（2 处）**：①R 选取条件记号 `\not\perp`→`\nmid`（print 不整除号 ⊮/∤）；②
  Proposition 3 条件 4 首个 "−1" 被 `$$` 粘连吞掉 → 补回 "((1+S₁)^{pⁿ} **− 1**, …"。
- **md 完整性说明**：References 位置（正文后、Appendix 前）与 print 一致；Appendix 含
  Faltings 简化的完整证明（至 "the proposition is proved."），无截断——初判截断系审计读取
  窗口误读，复核后撤销。
- **源级 quirk 清单（忠实不改）**：无（本篇 print 无明显 typo；[K1] 标题 "Almost complete
  intersections are not Gorenstein" 与 print 一致）。
- **可用性结论**：修复后 md 可作该 Annals 论文忠实底本；全部定义/定理/引理/推论/交换图逐一
  核对全对；参考文献 14 条逐条全对。本篇 22/22 页完成，无未决项；与 wiles1995（109p，待审）、
  frey1986/ribet1990/serre1987（待审）同目录。

### 修复登记（2026-09-30）
- **2 组替换全部命中**（\not\perp→\nmid；Prop3 条件 4 补 "−1"）；附录结尾段经复核确认 md 原已
  完整（初判截断撤销，见 p.022 签）。fix commit 见父提交链。
- 本篇 22/22 页完成，无未决项。
