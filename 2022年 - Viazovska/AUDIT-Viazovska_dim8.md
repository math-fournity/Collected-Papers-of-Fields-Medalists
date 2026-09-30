# AUDIT — M. S. Viazovska《The sphere packing problem in dimension 8》（arXiv:1603.04246v2，LaTeX born-digital，24p）

> mineru: standard 档云端解析；审计依据 = pdftotext 文本层逐字符对账（可靠 born-digital，0 FFFD）
> + `audit/via8_pNNN.png`（150dpi 全 24 页已渲染；p.1/18/20 全页目检——含 E₈ 定义页、
> Proposition 7/(58)-(61) 页、区间算术估计页）。
> **伪影族**：丢箭头 → ×7（ℝᵈ→ℂ/ℝ、‖x‖→∞、a,b:ℝ⁸→iℝ）、"f o r" 粘连 ×2（(1)/(3) 式）、
> Fejes Tóth/Über/László/Poincaré 变音拆裂 ×6、E₈-- 连字符重复、Λ_{8^-P}oints 乱码、
> "far all"（print 即此，曾修后依 PNG 还原）、(38)/(58) 交叉引用错位 ×2、Figure 1/2 图题
> 公式碎裂、"𝔊(0,∞)" 乱码、Ziegler 前多余空格、which double zeroes 缺 have。

## 逐页签（文本层主通道 + p.1/18/20 全页目检）
- **p.001（题录 + §1 Introduction 前半）**：题名/Maryna S. Viazovska/April 5, 2017/Keywords/
  MSC 52C17,11F03,11F30 ✓；sphere packing constant/Δ_P(r)/limsup/Δ_d sup 定义 ✓；
  **"The number be want to know"——print 即此源级 typo，忠实** ✓；Thue/"beginning **ot**
  twentieth century"——print 即此源级，忠实/Fejes Tóth 1940s [10]/π/√12≈0.90690（句号修复）✓；
  Kepler 1611/Hales 1998+2015 formal proof ✓；[6][4] ✓ — **PASS±**（±：arXiv 边条未收）
- **p.002-004（§1 末 + §2 Linear programming）**：Δ₈=π⁴/384≈0.25367 ✓；E₈ lattice 定义
  （mod 2）✓；unique/unimodular/minimal √2/**E₈-- 连字符修复** ✓；Theorem 1 ✓；[4, Section 8]
  unique periodic ✓；论文组织（a,b 双零点）✓；error-correcting codes [7]/quadrature [8]/
  spherical codes [13,16]/[5]/[2] ✓；Cohn-Elkies 2003/1.000001 ✓；Fourier transform 定义/
  x·y 恒等式/Schwinger/admissible ✓；**Theorem 2 (Cohn-Elkies)** (1)(2)/f(0)/f̂(0) ✓；
  "i. e." ✓；Poisson (1/√2 Λ₈)=2⁴(√2Λ₈) ✓/optimal 定义 ✓ — **PASS**
- **p.005-007（§2 末 + §3 Modular forms）**：**Theorem 3** (3)(4)(5)（f o r 粘连修复）✓；
  [4, Conjecture 8.1]/R⁸ uniqueness ✓；(6)-(8) double zeroes 推导 ✓；导数 vanish/hint ✓；
  §3 H/Γ(1)=PSL₂(ℤ)/Γ(N)/Γ₀(N) ✓；automorphy factor j_k/chain rule/slash operator ✓；
  modular form 定义/c_f(α,n/n_α) ✓；M_k(Γ) 有限维 ✓；Eisenstein (9)(10)/E₄/E₆ 系数 ✓；
  E₂ (11)/(12) quasimodular [20, Section 5.1] ✓ — **PASS**
- **p.008-010（§3 theta + §4 开头）**：theta functions θ₀₀/θ₀₁/θ₁₀（Thetanullwerte）✓；
  T,S 生成元/(13)-(18) 变换式 ✓；Jacobi identity (19) ✓；M₂(Γ(2)) ✓；weakly-holomorphic
  定义/M_k^!(Γ) ✓；j=1728E₄³/(E₄³−E₆²) 展开式 ✓；PARI GP/Mathematica ✓；Hardy-Ramanujan
  [17, p. 460-461]/Poincaré series [15] ✓；**(20) c_j(n) 渐近式**（A_k(n) Kloosterman 和/
  I₁ Bessel/[1, Section 9.6]）✓；[12, p.660-662]/[3, Propositions 1.10 and 1.12] ✓ — **PASS**
- **p.011-013（§4 函数 a 构造）**：𝓕(a)=a (21)/𝓕(b)=−b (22)/**"which have double zeroes"
  修复** ✓；φ_{−2} (23)/φ_{−4} (24) ✓；**"upper half-plane"（plain→plane 修复）** ✓；
  (25) c_φ_κ 渐近式 ✓；φ_{−4} (26)/φ_{−2} (27)/φ₀ (28) ✓；变换规则 (29) ✓；D 算子/(30)(31) ✓；
  (32)(33)(34) Fourier 展开逐系数核对全对 ✓ — **PASS**
- **p.014-016（(35) 定义 a + Proposition 1）**：(35) 四项围道积分 ✓；绝对一致收敛/O(e^{−2πiz}) ✓；
  **Proposition 1**（Schwartz + â=a）证明：|c_φ₀(n)|≤2e^{4π√n}/C₁ 估计/K₁ Bessel/最后项
  C₃(2√2πr)/(r²+2) 式 ✓；(36) Gaussian 变换（z^{−4} 因 dim 8）✓；换序/w=−1/z/周期性/=a(y) ✓ — **PASS**
- **p.017-018（Proposition 2/3/4 + Proposition 5/6/7 开头）**：**Proposition 2** (37)
  sin² 分解/良好定义/(29)→O 估计/路径变形/三式相加=2φ₀ ✓；**Proposition 3** (38) 四项显式
  （36/π³(r²−2)−8640/π³r⁴+18144/π³r²+积分）✓/(39)/(40) ✓/解析延拓 ✓；
  **Proposition 4** (41) a(0)=−i8640/π, a(√2)=0, a′(√2)=i72√2/π ✓；
  h (42)=128(θ₀₀⁴+θ₀₁⁴)/θ₁₀⁸ ∈ M_{−2}^!(Γ₀(2)) ✓；[14, Chapter I Lemma 4.1] ✓；h 展开 ✓；
  I,T,S/ψ_I (43)/ψ_T (44)/ψ_S (45) ✓；(46)(47)(48) ✓ — **PASS**
- **p.018（print 18：(56)(57) + Proposition 7 + Proposition 8）**：**p.18 全页目检** ✓；
  (49)(50)(51) ψ 展开逐系数核对全对 ✓；(52) b 定义四项 ✓；**Proposition 5**（b̂=−b）证明
  ✓；ψ_T|S=−ψ_T 等 ✓；𝓕(b) 计算 ✓；**Proposition 6** (53)（**"double roots at Λ₈-points"
  乱码修复**）/c(r)/ψ_I 估计/(54)(55)/(56)/(57) ψ_T+ψ_S=ψ_I 证明（ST²S∈Γ₀(2)）✓；
  **Proposition 7** (58)（144/πr²+1/π(r²−2)+积分）✓/(59)/(60)/**"(58) holds for r>√2"
  交叉引用修复（原误 38）**✓；解析延拓 ✓；**"far all"——print 即此源级 typo，忠实（依 PNG
  p.18 还原）**✓；**Proposition 8** (61) b(0)=0, b(√2)=0, b′(√2)=2√2πi ✓ — **PASS**
- **p.019-021（§5 Proof of Theorem 3）**：**Theorem 4**（g=(πi/8640)a+(i/240π)b——print 即
  编号 Theorem 4，忠实）✓；(62) g(r)=π/2160 sin²∫A(t)e^{−πr²t} ✓；A(t)=−t²φ₀(it)−36/π²ψ_I(it) ✓；
  **Figure 1 图题公式碎裂修复**（A₀^{(2)}=−368640/π² t²e^{−π/t}；A∞^{(1)}=−72/π²e^{2πt}+
  8640/π t−23328/π²）✓/**"t∈(0,∞)" 乱码修复**✓；(63)(64) A₀^{(n)}/A∞^{(n)} ✓；
  A∞^{(6)} 六项逐系数核对全对 ✓；A₀^{(6)} 五项 ✓；[3, Proposition 1.12]/**(65)-(69)**
  Fourier 系数界逐条 ✓；R₀^{(m)}/R∞^{(m)} ✓；区间算术四条不等式 ✓；A(t)<0 ⇒ (3) ✓ — **PASS**
- **p.020（print 20：B(t) 部分）**：**p.20 全页目检**（(63)-(69) 页）✓；(70) ĝ(r)=π/2160 sin²∫B(t) ✓；
  B(t) 两表示 ✓；**Figure 2 图题**（B₀^{(2)}=368640/π² t²e^{−π/t}；B∞^{(1)}=8640/π t−23328/π²）✓；
  B∞^{(6)} 六项 ✓；B₀^{(6)} 五项 ✓；区间算术四条 ✓；B(t)>0 ⇒ (4) ✓；
  (5) 由 Propositions 4 and 8 ✓；Theorems 4 and 3 ✓ — **PASS**
- **p.022-024（Acknowledgments + References + 地址）**：Bondarenko/Radchenko/Kramer/Sullivan/
  Ziegler/referees ✓；**References [1]-[20] 逐条抽验 14 条全对**（[6] László Fejes Tóth
  Festschrift（变音修复）✓/[10] L. Fejes Tóth, Über die dichteste Kugellagerung（修复）✓/
  [15] Ueber——print 即此拼写，忠实/[18] Thue Über…in einer Ebene（修复）✓）✓；
  Berlin Mathematical School/Str. des 17. Juni 136/Humboldt/viazovska@gmail.com ✓ — **PASS**

## 总评

- **覆盖声明**：24/24 页经可靠文本层逐字符对账 + md 全文交叉核对；150dpi 全 24 页渲染，
  p.1/18/20 全页目检。
- **FAIL 修复（47 组，三轮）**：①丢箭头 → ×7；②"f o r" 粘连 ×2（(1)/(3)）；③变音 ×6
  （Fejes Tóth/Über/László/Poincaré）；④E₈-- 连字符/Λ_{8^-P}oints/"which have" 补词/
  𝔊(0,∞)/图题碎裂 ×2；⑤(38)/(58) 交叉引用各 1；⑥"upper half-plain"→plane、far-all 依
  PNG p.18 **还原为源级**；⑦句号/逗号/空格 ~15；⑧N∈ℕ 双空格粘连。
- **源级 quirk 清单（忠实不改）**："The number be want to know"；"beginning ot twentieth
  century"；"far all r∈ℝ≥0"；[15] "Ueber die Entwicklungskoefizienten"（print 即此旧式
  拼写）；"Theorem 4" 编号承接 §5 证明 Theorem 3（print 即此）；ff→f 连字族
  （dificult/coeficients/efective/sufices）。
- **可用性结论**：修复后 md 可作该 arXiv 论文忠实底本；(1)-(70) 编号公式逐条核对全对；
  Figure 1-2 在位；参考文献 20 条抽验 14 条全对。本篇 24/24 页完成，无未决项；与 dim24
  （已审 ✅）、e8_published（25p，待审）、dim24_published（17p，已审 ✅）、ICM2022（已审 ✅）、
  laudatio（24p，待审）同目录。

### 修复登记（2026-09-30）
- **三轮共 47 组替换全部命中**（含 far-all 依 p.18 PNG 还原为源级）；(1)-(70) 公式全对。
  fix commit 见父提交链。本篇 24/24 页完成，无未决项。
