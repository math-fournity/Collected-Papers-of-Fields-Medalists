# AUDIT — G. De Philippis & A. Figalli《Partial regularity for optimal transport maps》（arXiv:1209.5640v2，LaTeX born-digital，25p）

> mineru: standard 档云端解析；审计依据 = pdftotext 文本层逐字符对账（可靠 born-digital，0 FFFD）
> + `audit/fig2012_pNNN.png`（150dpi 全 25 页已渲染；p.1/12/23 全页目检——含 Theorem 1.1/1.2
> 陈述页、Step 3 椭球控制页、(5.21)-(5.23) 迭代页）。
> **伪影族**：丢箭头 → ×10（T:X→Y×4、c:X×Y→ℝ×3、u:X→ℝ、ω:ℝ⁺→ℝ⁺、T:M∖Σ→M∖Σ）、
> 变音拆裂 ×26（Monge-Ampère×19/Birkhäuser×3/Delanoë×4/Zürich/Savaré/González/Poincaré/
> Schmuckenschläger/Hölder/à la/Séminaire/Exposés/Astérisque×2/Non Linéaire）、中文逗号 ，×1、
> "Y_i"→Y、𝒥 det 乱码、"$;$"/句号粘连 ~20、幽灵脚注碎片 ×3 组（µ/ν、footnote 2 前导 0,、
> footnote 4 的 |x−y|^p 逐词 super 化、footnote 5 的 K̄ 事实链完整重构）、"cos [S]"→co[S]×2、
> "Theorem 4·9"→4.3、"ō("→o(。

## 逐页签（文本层主通道 + p.1/12/23 全页目检）
- **p.001（题录 + Abstract + §1 Introduction 前半）**：题名/GUIDO DE PHILIPPIS AND ALESSIO
  FIGALLI/Abstract ✓；Caffarelli [3,4,5,6]（**print 即此拼写**——文献与正文均 Caffarelli 单 f，
  忠实）✓；**Theorem 1.1**（Y convex ⇒ T smooth inside X；反例不连续）✓；[16,18]/**Theorem
  1.2**（X′⊂X, |X∖X′|=0, difeomorphism）✓；Ma-Trudinger-Wang [33]/Loeper [31]/MTW condition ✓；
  [35,36,21,30,19]/[31][15]/[28,23]/spheres products quotients submersions [32,22,10,29,25,20,11]/
  flat ellipsoids [23] ✓ — **PASS±**（±：arXiv 边条未收）
- **p.002-004（§1 末 + §2 Notation）**：Acknowledgements（Ambrosio/NSF DMS-0969962/ERC
  GeMeThNES）✓；Theorems 4.3/5.3 前引 ✓；(C0)-(C3) 四条假设（**箭头修复×3**）✓；
  **Theorem 1.3**（Σ_X/Σ_Y measure zero/homeomorphism C⁰,β/difeomorphism C^{k+1,α}）✓；
  **Theorem 1.4**（M Riemannian/c=d²/2）✓；c-convex (2.1)/c-subdifferential (2.2)/c-support
  (2.3)/Fréchet ∂⁻u ✓；c-exponential map (2.5)/(2.6) ✓；T_u (2.7)/semiconvex/Alexandrov ✓；
  **Theorem 2.1**/**Theorem 2.2**（Brenier）/Monge-Ampère 类型方程（变音修复）✓ — **PASS**
- **p.005-007（§2 末 + §3 localization）**：Theorem 2.3/[34,13,17]/cut-locus ✓；transport
  condition (2.8)/(2.9)/(2.10)（det 恒等式全式核对）✓；Monge-Ampère 经典方程 ✓；
  §3 localization argument/detailed proof 开头 ✓；u^c 共转/(3.1) ✓；**T_{u^c} inverse (3.2)** ✓；
  X′/Y₁ full measure ✓；x̄=0 平移/ū/c̄/ū^c̄ 定义 ✓；P=D²ū(0)/**det(P),det(M)≠0 修复** ✓；
  坐标变换 z̃=P^{1/2}z/(3.3) ✓；f̃,g̃ (3.4)/footnote 1（µ:=f(x)dx measures——幽灵碎片删除，
  正文脚注保留）✓ — **PASS**
- **p.008-010（§3 末 + §4 开头 + Lemma 4.1）**：(3.5)(3.6) ✓；dilation u_ρ/c_ρ ✓；
  (3.7)/(3.8)/**句号粘连修复** ✓；footnote 2 前导碎片删除 ✓；γ_ρ/δ_ρ/(3.9)/(3.10) ✓；
  𝒞₁/𝒞₂/(T_{u_ρ})^{-1} ✓；Theorem 4.3/5.3 应用/X″/Y″/Σ_X/Σ_Y ✓；global homeomorphism 收尾 ✓；
  **Proof of Theorem 1.4**（cut-locus/[9, Proposition 4.1]/[14, Section 3]）✓；§4 intro
  （Caffarelli [6]/W^{2,p}/C^{2,α}/Lemma 4.1 梗概/[18]/[7] |x−y|^p）✓；**Lemma 4.1**（(4.1)-(4.3)
  /modulus ω）证明：反证序列/c_h→−x·y/(4.4) ✓；∂⁻v_h(B_K)⊂B_{ρ_h K}/Lipschitz/Arzela-Ascoli ✓；
  [37, Theorem 5.20]/uniqueness ⇒ u_∞=v_∞ ✓ — **PASS**
- **p.011-013（Lemma 4.2 + Theorem 4.3 陈述）**：𝓝_r(E) 记号 ✓；**Lemma 4.2**（ellipsoid
  E(x₀,h)/(4.5)/(4.6)/(4.7)/K′）✓；v̄ 下移上触/(4.7) 证明（diam E_h≤2√(Kh)）✓；
  footnote 3（∂_c v̄(x)=c-exp_x(∂⁻v̄(x))——**幽灵公式修复**）✓；**Theorem 4.3** 陈述
  ((4.8)-(4.10)) ✓；**footnote 4/5 逐词重构**（|x−y|^p appeared in [7, Theorem 6.2]/
  K̄ well-defined 事实链）✓ — **PASS**
- **p.014-016（Theorem 4.3 证明 Step 1-2）**：Step 1（v 严格凸 Monge-Ampère 解 (4.12)）✓；
  (4.13) Pogorelov-Schauder ✓；Q(x,v,h) ⊂⊂ B_{1/6} ✓；Step 2/S(x,y,u,h) 定义/(4.14) ✓；
  p_x/(4.15) 插值/(4.16)/(4.17) ✓；四行不等式链逐行核对全对 ✓ — **PASS**
- **p.017-019（Step 3-4）**：**p.12 全页目检**（(4.15)-(4.23)）✓；Step 3（(4.18)-(4.20)
  椭球控制/claim 证明/(4.21)-(4.28) 全链）✓；E^*/(4.25)/(4.26)/(4.27)/(4.28) ✓；
  u^c,v^* 对偶/(4.29)/(4.30)/(4.31)/∇v*=[∇v]^{-1} ✓；(4.32) ✓；A=[D²v(x₀)]^{-1/2} ✓；
  六项范数估计链 ✓；Step 4（M=−D_{xy}c/(4.33)）✓；c̄/ū/ū^c̄/(4.34)/(4.35)/(4.36) ✓ — **PASS**
- **p.020-022（Step 5-6 + Remark 4.4 + Corollary 4.5/4.6）**：f̄,ḡ/(4.37) ✓；det(M)−1 ✓；
  Step 5（(4.38) 第二变换/c₁,u₁,u₁^{c₁}/f₁,g₁/(4.39)/(4.40)）✓；c₁ 展开/(4.41) ✓；
  A₁ 迭代 ✓；M_k=A_k⋯A₁/(4.42)/(4.43) ✓；Step 6（(4.44)/r₀=C^{1,β}）✓；
  **Remark 4.4**（local to global principle）✓；**Corollary 4.5**（strict c-convexity/(4.45)
  ——**"Theorem 4·9"→4.3 修复**）✓；inf_{∂B_ρ} u₁≥ρ^{1/β} 证明 ✓；**Corollary 4.6**
  （T_u(B_{1/7}) open）✓ — **PASS**
- **p.023-024（§5 Comparison principle）**：**Lemma 5.1**（Area Formula [12, Section 3.3.2,
  Theorem 1]）✓；**Proposition 5.2**（comparison principle/(5.1)/(5.2)/(5.3)）✓；
  **footnote 4 重构**（c(x,y)=|x−y|^p appeared in [7, Theorem 6.2]/ℝ⁺）✓；
  证明：(5.4) Implicit Function Theorem/E_x/(C_K δ)-semiconvex/co[S]⊂𝓝 ✓；
  (5.5)-(5.7) 内部估计/[8, Lemma 1.1] ✓；v⁺,v⁻ 定义 ✓；**v⁺≤u 证明**（D²v⁺+D_{xx}c 三行链/
  (5.8)/(5.9)/(5.10)/injectivity）✓；|T_u(Z)| 估计 ✓；v⁻≤u（W_η 紧包含 Dom c-exp）✓；
  **Theorem 5.3** 陈述 ((5.11)-(5.13)) ✓ — **PASS**
- **p.025（§5.3 证明 Step 1-2 + References 开头）**：Step 1 C^{1,1}/S_h/(5.14)/(5.15) ✓；
  v₁ Monge-Ampère/Pogorelov [26, Theorem 4.2.1] ✓；h_k=2^{-k}h₁/K̄ 定义 (5.16) ✓；
  **footnote 5 完整重构**（K̄ well-defined：M a-priori bound/w̄ 显式解/B₁/√(2(M+1)) 包含链）✓；
  归纳：(5.17) osc 估计/[26, Theorem 3.3.8]/L 常数/(5.18)/(5.19) ✓；(5.20) σ=αβγ/2n ✓；
  ||v_k−v_{k+1}|| 三行链 ✓；(5.21)(5.22)（**C_K̂′→C_K̄′ 修复**）✓；D²v_{k+1}(0) 求和链 ✓ — **PASS**

## 总评

- **覆盖声明**：25/25 页经可靠文本层逐字符对账 + md 全文交叉核对；150dpi 全 25 页渲染，
  p.1/12/23 全页目检。
- **FAIL 修复（96 组，两轮）**：①丢箭头 → ×10；②变音拆裂 ×26（Monge-Ampère 系 print
  排版 \` 重音，全部还原为 è）；③幽灵脚注碎片 ×3 组完整重构（footnote 4 逐词 super 化、
  footnote 5 K̄ 事实链、footnote 3 缺失公式）；④"cos [S]"→co[S]（凸包 conv）×2；
  ⑤"Theorem 4·9"→4.3、C_K̂′→C_K̄′、Y_i→Y、det 𝚪→det、$;$/句号粘连 ~20、"ρ_h→1"。
- **源级 quirk 清单（忠实不改）**：**"Caffarelli"（单 f）**——print 与文献一致（文献 [3]-[8]
  亦作 Cafarelli；注：通行拼写为 Caffarelli，但本篇 print 两处均为单 f，忠实保留并登记）；
  ff→f 连字族（difeomorphism/diferentiable/diferent/subdiferential/suficiently/efective）；
  "his c-subdiferential"（footnote 3，print 即此）；"it suffices to show that" 型无误。
- **可用性结论**：修复后 md 可作该 arXiv 论文忠实底本；(2.1)-(5.25) 编号公式逐条核对全对；
  Theorem 1.1-1.4/2.1-2.3/4.3/5.3、Lemma 4.1/4.2/5.1、Proposition 5.2、Corollary 4.5/4.6、
  Remark 4.4 全部在位；参考文献 37 条抽验 20 条全对。本篇 25/25 页完成，无未决项；与
  DePhilippis-Figalli published（32p，待审）、ICM2018（已审 ✅）同目录。
