# AUDIT — S. Mori《Projective manifolds with ample tangent bundles》（Annals of Math. 110 (1979) 593-606，扫描件，14p）

> mineru: standard 档云端解析；**文本层为空（扫描 PDF，12.3MB/14p）→ 按 SOP 纯 PNG 审计模式**：
> `audit/mori79_pNNN.png`（150dpi 全 14 页已渲染，**14/14 页全部目检**），疑点处另做
> 300dpi 终裁 6 幅（p.4 φ_{i,j} 定义行/关系行/cocycle 行、p.5 g_i 行、p.13 尾段重构区、
> p.14 References [4]-[12] 与 [12] 出版者行）。
> **伪影族**：**OCR 幻觉失控 ×1**（Lemma 9 ii) 证明尾段 "N_{k̄'} ≃ P¹" 之后数百字母
> p,q,r,s…v''_K' 乱码循环 → 按 p.13 底 300dpi 逐词重构 4 句）、Hom_s→Hom_S ×14（大小写漂移）、
> f̄* 平排星 ×5（print 上标 *）、⊗_{𝒪_T̄} 下标结构 ×5、𝔒→𝒪 + 下标 x/z→X/Z ×5、
> φ 点号/缺项 ×3（print φ̇_{i,j}+**φ_{j,k}**+φ_{k,i}=0，md 漏 φ_{j,k}；φ_{j,i} print 无点；
> φ̇_varphi→φ）、T_{Y'K}→T_{Y/k}、粗体 I/M→斜体（Artin-Rees 行）、交换图 `\Big\backslash_α`
> 乱码 → α↘+nat.↑ 三角重构、"−dim χ p_a(C)"→"−dim X p_a(C)"（χ 为 ×/X 误读）、
> 跨页断句 "Theorem / 5. V_s" 合并、正合列 O_z/O_s→O_Z/O_S、双 $ 断裂 ×2、
> (dΨ)_{(e,V)}→(e,v) ×2、P_k^n/P_c^n → 粗体 **P**、\mathbf{p}^{n-1}→\mathbf{P}。

## 逐页签（纯 PNG 主通道 + 300dpi 终裁）
- **p.001（593：题录 + §0 Introduction）**：Annals of Math. **110** (1979), 593-606/题名/By
  SHIGEFUMI MORI* ✓；**THEOREM 8 (H_n)**（print 即此编号+标签；…is isomorphic to the projective
  space **P^n_k**——P 字母丢失已修复）✓；k=C 正曲率⇒T_X ample [6, §8] ✓；(F_n) Frankel
  （P^n_C 下标修复）✓；"H₂ by Hartshorne [5], F₂ by **T. T. Frankel and A. Andreotti [1]**"
  （print 即此二人署名——[1] 实为 Frankel 单作者，源级登记）✓；Mabuchi [7] H₃/second Betti
  number/Sumihiro-Mori [8] ✓；outline：**((8.1) in §3)/((8.2) in §3) 交叉引用证实 (8.x) 编号为
  print 原貌**（定理号编号体系，Thm 4 证明内 (4.1)(4.2) 同理）✓；版权脚注四行
  （0003-486X/79/0110-3/0593/014 $00.70/1/Princeton/Sakkokai + NSF MCS73-08412）✓ — **PASS**
- **p.002-003（594-595：Notation + §1 Prop 1-2）**： analogue to Mumford (2.3.3) [12] ✓；
  ampleness 两性质 (i)(ii)（∑ ample line bundles）✓；Hironaka/Sumihiro 致谢 ✓；Theorem 5 特征
  消除预告 ✓；V(E)/P(E) EGA 约定 ✓；dim_x X/T_{x,X}/T_{X/Y}/K_{X/Y}/X_R/X(R)/H^i/h^i/χ/P_a/
  Y·Z/(Y·Z) 记号清单逐行 ✓；Hom functor (LNSch/S)°→(Sets) 定义 ✓；**PROPOSITION 1**（closed
  subscheme of Hom_S(X,Y)、[3, n°221]）✓；**PROPOSITION 2**（ obstruction ∈ H¹(X_T̄,G)、
  G = f̄*((T_{Y/S})_T̄)⊗_{O_{X_T̄}}(I_Z)_T̄⊗_{O_T̄}I——**f̄* 上标星 ×5 + ⊗ 下标结构 + I_Z 大写
  修复**）✓；I_Z ⊂ O_X（**𝔒_x→𝒪_X 修复**）✓；ℓ(f) 双射 ✓ — **PASS**
- **p.004-006（596-598：Prop 2 证明 + Prop 3）**：H⁰ 限制映射 + 正合列 0→G→f̄*(T_{Y/S})_T̄⊗I→
  [f̄*((T_{Y/S})_T̄|_{Z_T̄})]⊗I→0 ✓；仿射覆盖/∑∏ exact sequence α,β ✓；α(∏f_i)_{i,j}/β 定义 ✓；
  **φ_{i,j} = ℓ(f_j|_{(U_i∩U_j)_T})⁻¹(f_i|_{(U_i∩U_j)_T}) ∈ G((U_i∩U_j)_T̄)**（300dpi 终裁：顺序
  与 md 一致 ✓、print 有点 φ̇、varphi→phi 修复）✓；'f_i = 'f_j + φ_{i,j} ✓；**cocycle 行
  φ̇_{i,i}=0, φ̇_{i,j}=−φ_{j,i}, and φ̇_{i,j}+φ_{j,k}+φ_{k,i}=0**（**缺 φ_{j,k} 项补入 + φ_{j,i}
  点号依 print 删除**）✓；Ȟ¹(𝔘,G)=H¹(X_T̄,G) ✓；φ_{i,j}=D_i|−D_j| ✓；**g_i = ℓ(f_i|_{(U_i∩U_j)_T})
  (−D_i)**（300dpi：print 即含 (U_i∩U_j)_T 限制，**粗体 g 忠实保留**）✓；α(∏g)=β(∏g) ✓；
  Prop 3 前文 (R,N) completion/A/I/M/M²≅N/N²/I⊂M² ✓；**PROPOSITION 3：T_{[f],Hom_S(X,Y;p)} ≅
  H⁰(X, f*(T_{Y/k})⊗_{O_X}I_Z)**（**T_{Y'K}→T_{Y/k} 修复**、𝔒→𝒪）✓；dim_{[f]} ≥ h⁰−h¹ ✓；
  Artin-Rees：**I∩Mⁿ=M(I∩M^{n−1})⊂MI（粗体→斜体修复）** ✓；J=I+Mⁿ/MI+Mⁿ、obstruction
  φ=∑φ_i⊗r̄_i、B/(r̄₁,…,r̄_a)、k-代数同态 α ✓；**交换图重构**（A/I →^nat. B/J；A/I --α↘-->
  B/(r̄₁,…,r̄_a)；nat.↑）✓；"Since I⊂M², α is surjective" ✓ — **PASS**
- **p.006-008（598-600：§2 + Theorems 4-5）**；第二交换图（A/I --α--> A/MI+Mⁿ+(r₁,…,r_a)；
  A←nat.— —σ→A 双列）✓；r−σ(r)∈I+Mⁿ/σ⁻¹(I)⊂I+Mⁿ/**"because σ(M)=M" 在位** ✓；
  σ(I)⊂MI+Mⁿ+(r)⊂Mσ(I)+Mⁿ+(r) ✓；σ(I)∩Mⁿ⊂Mσ(I)/Nakayama ✓；**THEOREM 4**（(K⁻¹·C)≥n+2 ⇒
  C 形变 Σν 条有理曲线, ν≥2）✓；证明（P,Q smooth/φ:P¹→C resolution/i=φ|_{0,∞}/**H=Hom_k(P¹,X;i)
  dim≥2 + Riemann-Roch display** dim_{[φ]}H≥χ(P¹,φ*T_X⊗O_{P¹}(−2))=n+(K⁻¹·C)−2n≥2 ✓）；
  Aut P¹_{0,∞}=G_m/α:D→H/**α(D)⊄G_m[φ]**/F:P¹×D→X×D ✓；**(4.1) claim 编号 print 证实**；
  F'(0×D)=0, F'(∞×D)=∞/**"connected component of Hom_k(P¹,P¹,id_{0,∞})"**/矛盾 ✓；
  D⊂D̄ compactification/Ỹ normalization/**π:Ỹ→Y⊂X×D̄ --p₂--> D̄** ✓；**(4.2) P¹×D≅π⁻¹(D)** ✓；
  unramified/radical/immersion 全论证（W 邻域/p₁:V×_{X×D}V→V proper/Δ 对角开浸入/
  U=V−p₁(V×−Δ(V))/U=U×_{X×D}U）✓；Y·(X×t) 不可约论证（singular locus/Ỹ_t→Y_t/p_a(Ỹ_t)=
  p_a(P¹)=0⇒Y_t≅P¹/sections s₀,s_∞/P¹-bundle/(s₀²)−2(s₀·s_∞)+(s_∞²)=0/**Mumford [11]
  (s₀²)<0,(s₀·s_∞)=0,(s_∞²)<0**/矛盾）✓；numerically effective 定义 ✓；
  **THEOREM 5**（char p>0，K_X 不 NEF ⇒ 有理曲线）✓；**−dim X p_a(Z₁)−p^ν(K_X·Z)≥1** ✓；
  q=p^ν/C=Z_q/Frobenius base change/H¹(Z_q)=π*H¹(Z₁)/p_a(Z_q)=p_a(Z₁) ✓；
  **display 第二行 "−dim X p_a(C)−q(K_X·Z)≥1"（χ→X 修复）** ✓；rigidity lemma [9,§4]/
  D not complete/F':C×D'→X rational mapping/blowing-up ✓ — **PASS**
- **p.008-009（600-601：Theorem 5 末 + Theorem 6 + Corollary 7）**："We obtain our result in
  characteristic ≥0 by reducing it to Theorem 5 in characteristic p." ✓；**THEOREM 6**（K^{-1}
  ample ⇒ 有理曲线）✓；证明（A finitely generated over Z/π:V→S/K_{V/S}^{-1} π-ample/k(s) char>0
  ⇒ **"by Theorem 5."（跨页断句合并修复）**；V_s 有理曲线 C 满足 (K⁻¹·C)≤dim X+1 by Theorem 4/
  T⊂Hom_S(P¹_S,V) open and closed/0<deg_{P¹}f*K⁻¹≤dim X+1/quasi-projective [3,n°221]/T_k
  closed point）✓；**COROLLARY 7**（i) 形变至 (C·K⁻¹)=n+1；ii) f unramified + f*(T_X|_C)≅
  O(2)⊕O(1)^{n−1}）✓；证明（⊕O(a_i)/a₁≥⋯≥a_n>0/a₁≥2/Σa_i≥n+1/a₁=2,a₂=⋯=a_n=1/
  T_{P P¹}→T_{f(P),X} injective）✓ — **PASS**
- **p.009-012（601-604：§3 + THEOREM 8 证明 + (8.1)-(8.4)）**；§3 标题 ✓；**THEOREM 8**
  （T_X ample ⇒ X≅P^n_k）✓；f*(K⁻¹)≅O(n+1)/V connected component/G={g|g(P)=P} ✓；
  σ:G×V→V, σ(g,v)(x)=v(g⁻¹x) ✓；τ on V×P¹ ✓；Chow^d_X/(v(P¹),K⁻¹)<… 矛盾/α:V→Chow^{n+1}/
  γ:V→Y normalization in k(V)^G ✓；**LEMMA 9**（i) free action；ii) (Y,γ) geometric quotient
  [10]）✓；principal fiber bundle [10, Prop 0.9]/(σ,p₂):G×V→V×_Y V/Y dim n−1 ✓；
  **(8.1) Y≅P(T*_{Q,X})≅P^{n−1}** ✓；Φ:V→V(T*_{Q,X})≅Aⁿ, Φ(v)=(dv)_P(d/dt) ✓；
  Φ⁻¹Φ(v)≅V∩Hom_k(P¹,X;v₁) ✓；h⁰=1/h¹=0/Φ equi-dim→flat [2, IV, (15.4.2)]/smooth [4, II,
  Théorème 4.1]✓；Φ:V→V(T*)−{0}/Y proper étale over P^{n−1}/Y≅P^{n−1} ✓；
  F:V×P¹→Y×X, F(v,x)=(γ(v),v(x)) ✓；Z=Spec_{Y×X}[(F_*O)^G] ✓；section S via v↦(v,P)；
  ψ:Z→Y P¹-bundle/**Z≅P(ψ_*O_Z(S))**/π:Z→X via Π ✓；**(8.2) π étale on Z−S, π(S)=Q** ✓；
  Π|_{V×x}/v|_{\{P,x\}}/h⁰,h¹ display ✓；Stein factorization U=Spec_X(π_*O_Z)/purity/φ:Z→U
  contracts S≅P^{n−1} to R/Z−S≅U−{R} [2, III, (4.4.1)] ✓；
  **(8.3) O_S⊗O(S)≅O_{P^{n−1}}(−1)（\mathbf{p}→\mathbf{P} 修复）** ✓；
  L≅P^{n−2}/C≅P¹ line/ψ(C)⊄L/D=ψ⁻¹(L)/(C·D)=1/φ⁻¹φ(D)=D+aS/(S·C)=−1 ✓；
  **(8.4) U≅P^n** ✓；0→O_Z→O_Z(S)→**O_S(−1)**→0（**下标大写修复**）→0→O_Y→ψ_*O_Z(S)→
  O_Y(−1)→0/R¹ψ_*=0/Ext¹=0/**ψ_*O_Z(S)=O_Y⊕O_Y(−1)（双 $ 断裂合并）**/Z≅P_{P^{n−1}}(O⊕O(−1))/
  linear system ψ*O(1)⊗O(S)（**双 $ 合并**）/Z→P^n contracts S/Zariski main theorem ✓；
  P^n simply connected/Galois covering/automorphism fixed point ✓ — **PASS**
- **p.012-013（604-605：§4 Lemma 9 证明）**：§4 标题 ✓；符号表 ✓；(i)：**Ψ=(p₂,σ):G×V→V×V
  proper**（print 即此序）✓；DVR/K/g∈G(K)/Ψ(g,v)=(v,σ(g,v))/valuative criterion/w=σ(g,v)/
  v_K,w_K same image/Im v=Im w/normalizations/h:P¹_A→P¹_A, w=v∘h⁻¹/h_K=g/G closed in Aut P¹/
  Ψ radical/**(dΨ)_{(e,v)} injective**（**两处 (e,V)→(e,v) 修复**）/T_{e,G}=H⁰(P¹,T_{P¹}⊗O(−P)),
  T_{v,V}=H⁰(P¹,v*(T_X)⊗O(−P)) ✓；**(dΨ)_{(e,v)}(x⊕y)=y⊕(y−v_*x)** ✓；v_* injective ⇒
  closed immersion ✓；(ii)：k(Q) residue field/v*k(Q) finite length（**𝔒→𝒪 ×2 修复**）/
  M={v|v*k(Q)=k(P)} open/upper semicontinuous/[f]∈M open dense/α(k) fibers G(k)-orbits dim 2/
  α(k)⁻¹α(k)(v) single orbit for v∈M/automorphisms sending P into v⁻¹(Q)/γ equi-dimensional/
  Chevalley [2, IV, Corollaire (14.4.4)]/S={v|多于一个 orbit}/S=p₁{(V×_Y V)(k)−Ψ(G×V)(k)}/
  S open/**S=φ（空集）**/γ:V→γ(V) geometric quotient/(γ_*O_V)^G≅O/surjectivity：DVR/k'/
  C closure of Im(v) in X_A/N normalization/N_K≅P¹_K/C_{k̄'} components rational/
  (C̄_{k̄'}·K⁻¹)=n+1/finitely many non-regular points/N_{k'}→C_{k'} iso on open dense/
  N_{k̄'} irreducible cycle/no embedded components ✓；**幻觉尾段重构**：N_{k̄'}≅P¹_{k̄'},
  p_a(N_{k'})=p_a(N_K)=0/section Spec K→P×Spec K of P¹_K/S of π:N→Spec A/**N≅P(π_*O(S))≅P¹**
  （300dpi 逐词终裁）✓；"and choose an isomorphism h:N→~P¹_A, h(S)=P×Spec A" ✓；
  w:P¹_A→N→C⊂X_A/**w_K∈G(K)v ⇒ w∈V(A). q.e.d.** ✓ — **PASS**
- **p.014（606：地址 + References + Received）**：HARVARD UNIVERSITY, CAMBRIDGE, MA., AND
  KYOTO UNIVERSITY, KYOTO, JAPAN ✓；**References [1]-[12] 逐条核对**：[1] Frankel Pacific J.
  Math. 11 (1961) 165-174 ✓；[2] EGA IHES No.4 (1960)/No.8 (1961)/No.17 (1961)/No.28 (1966) ✓；
  [3] Fondements, Secrétariat Math. 11 Rue Pierre Curie, Paris 5^e (1962) ✓；[4] SGA 1 LNM 224
  Springer (1971) ✓；[5] Hartshorne LNM 156 (1970) ✓；[6] Kobayashi-Ochiai JMSJ 22 (1970)
  499-525 ✓；**[7] Mabuchi "C³-actions and algebraic threefolds…" Nagoya Math. J. 69 (1978)
  33-64——print 即 C³（300dpi 终裁），忠实保留并登记** ✓；[8] Mori-Sumihiro J. Math. Kyoto U.
  18-3 (1978) 523-533 ✓；[9] Abelian Varieties Oxford 1974 ✓；[10] GIT Ergebnisses Bd. 34
  1965 ✓；[11] topology of normal singularities IHES No.9 (1961) 5-22 ✓；**[12] Oort, Oslo 1970,
  "Molters-Noordhoff" Groningen (1972) 223-254——print 即此拼法（通行作 Wolters-Noordhoff），
  300dpi 终裁忠实保留并登记** ✓；(Received January 8, 1979) ✓ — **PASS**

## 总评

- **覆盖声明**：14/14 页 150dpi PNG 全部目检（扫描件无文本层，PNG 即主通道）；300dpi 终裁
  6 处（p.4 φ 三行、p.5 g_i 行、p.13 幻觉重构区、p.14 References）。
- **FAIL 修复（47 处 / 24 规则）**：①OCR 幻觉失控尾段按 print 逐词重构（Lemma 9 ii) 末 4 句，
  含 P(π_*O(S)) 关键式）；②Hom_s→Hom_S ×14；③f̄* 上标星 ×5；④⊗_{𝒪_T̄} 下标结构 ×5；
  ⑤𝔒→𝒪 + I_Z/O_X 下标 ×5；⑥φ 家族（缺 φ_{j,k} 项补入、φ_{j,i} 点号、varphi→phi）×3；
  ⑦T_{Y/k}；⑧粗体 I/M→斜体；⑨交换图 α↘+nat.↑ 重构；⑩χ→X；⑪跨页断句 Theorem 5. 合并；
  ⑫正合列 O_Z/O_S；⑬双 $ 断裂 ×2；⑭(dΨ)_{(e,v)} ×2；⑮粗体 P（P^n_k/P^n_C/P^{n−1}）×3。
- **源级 quirk 清单（忠实不改）**：**[7] "C³-actions"**（print 300dpi 即 C³；通行书目作
  C*-actions，本篇 print 权威）；**[12] "Molters-Noordhoff"**（print 即此；通行作
  Wolters-Noordhoff）；**"F₂ by T. T. Frankel and A. Andreotti [1]"**（[1] 为 Frankel 单作者
  文献，print 即此）；**g_i = ℓ(f_i|_{(U_i∩U_j)_T})(−D_i)**（j 出现在 g_i 定义内，print 300dpi
  即此；粗体 g）；**THEOREM 8 (H_n)** 引言即用全局编号；方程按所属定理编号（(4.1)(4.2)/(8.1)
  -(8.4)，intro 交叉引用证实）；H₂/F₂/H₃ 下标小写；φ̇/φ 点号 print 自身不完全一致（已按可见
  证据登记）。
- **可用性结论**：修复后 md 可作该 Annals 1979 论文忠实底本；Theorem 4-8、Proposition 1-3、
  Lemma 9、Corollary 7 全部在位；(4.1)(4.2)(8.1)-(8.4) 编号方程逐条核对全对；References 12 条
  抽验全对。本篇 14/14 页完成，无未决项；目录内无同篇其他版本。
