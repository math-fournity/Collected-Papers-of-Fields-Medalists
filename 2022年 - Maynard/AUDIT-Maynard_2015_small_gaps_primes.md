# AUDIT — J. Maynard《Small gaps between primes》（arXiv:1311.4600v3，LaTeX born-digital，25p）

> mineru: standard 档云端解析；审计依据 = pdftotext 文本层逐字符对账（可靠 born-digital，0 FFFD）
> + `audit/may15p_pNNN.png`（150dpi 全 25 页已渲染；p.1/2/5/6/7/16/18/19/22 目检——含 Abstract
> [1,x]² 与 70 000 000 页、(4.2)/(4.3) 编号页、fn2 Engelsma 足注页、(4.5) 页、(6.9)-(6.14) 全页、
> (7.3)-(7.4) 页、(7.5)-(7.7) 页、(8.5)-(8.7) 全页；p.1/7 另有 300dpi 裁片终裁）。
> **伪影族**：liminf 乱码 ×14（`$\dot{}_n`/`\dot{\zeta}_n`/`\displaystyle\mathrm{f}_n`/`\mathrm{f}_n`/
> array 阵列拆断 ×3/`\phantom{}_i`/`lim$` 无 inf ×3/`l i m i n f` 拉丁化 ×3）、**方程编号错位
> 7 组 16 tag**（裸编号行 (4.2)(5.16)(6.7)(6.11)(6.19)(7.6)(7.17) 与相邻 \tag 错一位 → 拆分重编）、
> 幽灵下标碎片 ×4 组（Q<sub>We first deal…</sub>/P<sub>if the product r…</sub>/Q<sub>not square-free…</sub>/
> P<sub>dropped…measure)</sub>）、ff 连字 ×28、句号/逗号粘连 ~21、丢空格 ×12、控制字符 \x03 ×4、
> 尾部变音拆裂（Montréal/Québec/André/mathématiques）+ 地址块断行。

## 逐页签（文本层主通道 + p.1/2/5/6/7/16/18/19/22 目检）
- **p.001（题录 + Abstract + §1 前半）**：SMALL GAPS BETWEEN PRIMES/JAMES MAYNARD/arXiv:1311.4600v3
  28 Oct 2019 ✓；Abstract（GPY refinement/(1.2)→4680 polymath）✓；(1.1) liminf=0 ✓；
  **(1.2) `7 0 0 0 0 0 0 0`→70\,000\,000 修复**（300dpi 裁片证实 print 三组俩俩空格）✓；
  "contained in **[1,x]²**"——**print 即上标 2**（PNG p.1 终裁），忠实保留 ✓；
  "from Zhang's theorem **the** that number"——**print 即有 the**，源级登记 ✓ — **PASS±**（±：arXiv v3 边条未收）
- **p.002-003（§1 后半 + Theorems 1.1-1.4）**：'level of distribution θ'**¹**（`θ^{,1}` 乱码→θ'<sup>1</sup>
  足注标记重构）✓；(1.3) 定义 + fn1（different authors…×2 处 diferent 修复）✓；Bombieri-Vinogradov/
  Elliott-Halberstam/Friedlander-Granville ✓；GPY lim inf$_n$≤16 ✓；(1.4) ✓；**Theorem 1.1**
  （≪m³e^{4m}）+ Tao private communication ✓；short intervals [N, N+N^{7/12+ε}]（**`\dot{N}`→N 修复**）✓；
  linear functions L_i(n)=a_i n+b_i/Π(n) no fixed prime divisor/(1/4+o(1))log k ✓；
  **Theorem 1.2**（fraction 分母 `\in A`→⊆A 修复 + **孤儿 display `#{{h…}⊆A}` 整行删除**——print 为
  单一 fraction）✓；**Theorem 1.3**（≤600）✓；**Theorem 1.4**（EH ⇒ 12 与 600 双 display）✓ — **PASS**
- **p.004（§2 improved GPY sieve）**：(2.1) S(N,ρ) ✓；(2.2) GPY 权 w_n、λ_d=μ(d)(log(R/d))^k ✓；
  (2.3) λ_d=μ(d)F(log R/d)、F(x)=x^{k+l} ✓；`l∈ℕ`**`.`** 粘连修复 ✓；(2.4) k 维权 ✓；
  Selberg [8, Page 245]/Goldston-Yıldırım [6] ✓；(2.5) λ≈∏μ(d_i)f(d_1,…,d_k) ✓ — **PASS**
- **p.005-006（§3 Notation + §4 前半）**：§3 记号（o/O/≪ 依 k,H；ϕ,τ_r,μ；ε fixed）✓；
  W=∏_{p≤D₀}p、(4.1) D₀=log log log N ✓；variable `p ,,`→p ✓；(4.2)(4.3) S₁,S₂（**裸编号+
  错位 tag 重编修复**——(4.3) 锚 S₁ 行、S₂ 行补 \tag{4.3}）✓；**Proposition 4.1**（exponent of
  distribution `0 _ { : }`→0、λ_{d₁,…,d_k} 显式、(1+o(1))φ(W)^k N(log R)^k/W^{k+1} 主项）✓；
  𝓡_k 支撑 ✓；`{\cal F}`→F、`R supported`→→ℝ supported 修复 ✓；**Proposition 4.2**（M_k=sup、
  r_k=⌈θM_k/2⌉、lim inf_{n}(p_{n+r_k−1}−p_n)≤max(h_i−h_j)——**array 拆断 liminf 修复**）✓；
  Proof（S=S₂−ρS₁、F₀→F₁ Riemann 逼近、(4.4)、`N^{\bar\theta/2−δ}`→N^{θ/2−δ}、`M_k .` 粘连×2 修复）✓；
  **Proposition 4.3**（M₅>2、M₁₀₅>4、M_k>log k−2log log k−2；`ℕ ,,`→ℕ、M<sub>k</sub>→$M_k$）✓；
  Theorem 1.3 证明（k=105、Engelsma、**fn2 = {0,10,12,…,600} 全集 + math.mit.edu/~primegaps**
  `<sub>˜</sub>`→~ 修复）✓；Theorem 1.4 证明（θ=1−ε、M₅>2、H={0,2,6,8,12}）✓ — **PASS**
- **p.007-008（Theorems 1.1/1.2 证明 + §5 开头）**：(4.5) ✓；ε=1/k、H={first k primes greater
  than k}（`k .` 粘连修复）、diameter ≪k log k ✓；**lim inf$\phantom{}_i$→lim inf_n 修复** ✓；
  Theorem 1.2 计数（A₂ 逐素数删少数剩余类、#A₂≥r∏(1−1/p)、`r . }` 粘连修复、**s=#R₂→#A₂ 修复**、
  `s>k` 补句号）✓；binomial(s,k)/binomial(s−m,k−m)（**`\dot{h}_1′`→h₁′ 修复**）✓；
  §5 Selberg sieve manipulations、`θ ,` 粘连 + **`R \overset{.}{=}`→R= 修复**、μ(d)²=1 ⇒ pairwise coprime ✓ — **PASS**
- **p.008-011（Lemma 5.1 + 变量代换）**：Lemma 5.1（y_{r₁,…,r_k} 与 λ 互转、(5.1) S₁ 主项+
  O(y²max R²(log N)^{2k})）证明：expand/swap、(5.2)-(5.4) error ≪λ²max R²(log R)^{2k}、`λmax` 下标修复 ✓；
  s_{i,j} 引入、(5.5) ✓；(5.6)-(5.8) 反向代换 d_i|…、`q =$ $` 双 $ 修复 ✓；ymax=sup（**`\mathbf{sup}`
  ×2→\sup 修复**）、(5.9) λmax≤ymax·…链 ✓；`μ_i(d_i)` ✓ — **PASS**
- **p.011-014（Lemma 5.2 + S₂^{(m)}）**：Lemma 5.2 陈述（S₁/S₂^{(m)}/S₂ 三式）✓；
  S₂^{(m)} 展开 (5.15)（**`[d_i,e_i]]n+h_i`→`|n+h_i` 修复**）✓；(5.16)(5.17) E(N,q)/X_N
  （**裸编号错位重编 + 拆分双 display 修复**）✓；`q =$ $textstyle W∏[d_i,e_i]` 修复、
  `{ \cal O }`→O、`n+\boldsymbol{h}_m`→h_m 修复 ✓；**Q<sub>We first deal…</sub> 幽灵下标→正文** ✓；
  (5.18)-(5.20) error 项（Cauchy-Schwarz/level θ）✓；s_{i,j} 限制（**Q<sub>not square-free…</sub>→正文**、
  coprime to W or is **not square-free make no contribution**）✓；(5.21) 1/ϕ([d_i,e_i])=∑1/g(u_i) ✓；
  (5.22)-(5.24) y^{(m)} 代换/r′=∏r_i/d_i/u_i 引入 ✓；(5.25)-(5.26) S₂^{(m)} 终式+误差 ✓；
  (5.27)-(5.29) S₂ 主项/`1+O(D₀^{-1})$ This gives the result` **\x03→□ 修复** ✓；
  Lemma 5.3（y^{(m)} 与 y 关系）✓；Remark（λ 支撑扩至 d_i<R^{1/m}——`In ourproofofLemma`/
  `itfurther`/`ifwe` 丢空格修复、efective→effective）✓ — **PASS**
- **p.014-017（§6 + Lemmas 6.1-6.3）**：§6 motivation（eigenvalue equation (6.1)/(6.2)、
  `equationfor` 修复、`k>2`**`.`** 补句号、`λ .$` 粘连修复）✓；(6.3) y=F(log r_i/log R)、
  **`F:ℝ^k→ℝ` 箭头修复 + `≤` 断裂 1} 重接** ✓；**P<sub>if the product r…</sub> 幽灵下标→正文、
  `y_*`→y 修复** ✓；`choice of y . .` 粘连修复 ✓；**Lemma 6.1**（γ(p)/p≤1−A₁、−L≤∑γ log p/p−log z/w≤A₂、
  `w≤z .` 粘连修复、g totally multiplicative、`G'_max` 定义 + `\mathbf{sup}`、`Then` 前补句号）✓；
  (6.4) S₁ 主项 ✓；Lemma 6.2（(6.5) drop (u_i,u_j)=1 代价、(6.6)、(6.7)(6.8) **裸编号重编**、
  (6.9) I_k(F) 显式 + `F_max^2φ(W)^k N(log R)^k/W^k` 换行断裂修复）✓；
  **Lemma 6.3**（`y_{r₁,…,r_k} ,,` 双逗号修复、J_k^{(m)}(F) 定义）证明：(6.10)-(6.14)、
  (6.11)(6.12) **裸编号重编**、(6.15)-(6.18)、(6.19)(6.20) **裸编号重编**、(6.21)(6.22) ✓；
  Remark（G(∑t_i) 特例→GPY (2.3) 等价）✓；Remark（Tao alternative、`ofProposition`/
  `ofGoldston`/`Ourfunction` 丢空格、diferentiated 修复）✓ — **PASS**
- **p.017-020（§7 large k 权）**：(7.1) M_k ✓；Remark（𝓛_k 特征方程、`equationfor` 已修）✓；
  (7.3) F=∏g(kt_i)（**`g:[0,∞]→ℝ` 箭头修复**）✓；`J_k^{(1)}(F)$ Similarly` 补句号、
  **`I_k \stackrel{.}{=}`→I_k= 修复** ✓；center of mass（**`\begin{array} 断裂 du 重接` 修复**）、
  **P<sub>dropped…measure)</sub> 幽灵下标→正文** ✓；γ=∫g²、(7.4) I_k≤k^{−k}γ^k ✓；
  (7.5) 下界、`support of $^{g,}$`→g 修复 ✓；(7.6)(7.7) **裸编号重编 + aligned 拆分修复** ✓；
  (7.8) μ<1−T/k、`η=(k−T)/(k−1)−μ`、(7.9)、`u_i ,,` 双逗号修复 ✓；(7.10)-(7.13) E_k 二阶矩控制 ✓；
  (7.14)、(7.15) Lagrangian、**`(g(t) \dot{-} … \dot{\beta}`→g(t)−αg²−βtg² 修复** ✓；
  (7.16) g(t)=1/(2α+2βt)、`functions g is of the form` **print 即此（p.18 目检）源级登记** ✓；
  (7.17)(7.18) **裸编号重编 + 拆分修复** ✓；`1+AT=e^A`、μ=1/(1−e^{−A})−A^{−1}、
  **`$ Substituting$(7.17)into$(7.14)` 粘连修复** ✓；(7.19)-(7.21)、A=log k−2log log k
  （**`- 2$log log$k`→−2log log k 修复**）、M_k≥log k−2log log k−2、`~ > ~`/`~ = ~` 波浪修复 ✓ — **PASS**
- **p.021-023（§8 small k + Prop 4.3 证明）**：(8.1) F=P|𝓡_k ✓；symmetric average 论证、
  `ofthe` 修复 ✓；**Lemma 8.1**（(1−P₁)^a P_j^b 积分、G_{b,j}(x) 多项式、`j .` 粘连修复）证明：
  (8.2) 归纳/(8.3) beta function/(8.4)-(8.6) ✓；`ofa polynomial` ×2 修复 ✓；**Lemma 8.2**
  (I_k/J_k 二次型、γ_{…} 系数) 证明：(8.7)-(8.10) ✓；`sufices` 修复 ✓；(8.11)、`P .$` 粘连修复 ✓；
  **Lemma 8.3**（A₁^{-1}A₂ 最大特征值、(8.12)-(8.14)、`ofthe ratio` 修复、`a^TA₂a` 补句号）✓；
  Proof of parts (1)(2)：42 monomials b+2c≤11（`≤$ 11` 断裂修复）、`42×42` 修复、
  **(8.15) λ≈4.0020697…>4（`4. 0 0 2 0 6 9 7` 修复）**、`k=105` ×3 修复 ✓；(8.16) P 多项式、
  **(8.17) M₅≥1 417 255/708 216>2（数字间距修复）** ✓ — **PASS**
- **p.023-025（§9 + References + 尾块）**：Acknowledgements（Granville/Heath-Brown/Koukoulopoulos/
  Tao、EPSRC EP/P505216/1、CRM-ISM、**Universit´e de Montr´eal→Université de Montréal 修复**）✓；
  References [1]-[9] 逐条核对（Elliott-Halberstam 1970/Friedlander-Granville 1989/GPY products
  2009/Primes in tuples III **diference→difference 修复**/tuples I `ofMath`→of Math + `Math.(2)`→
  Math. (2) 修复/GY 2007/**Polymath [7] Preprint**/Selberg 1991/Zhang to appear）✓；
  **fn3**（`$^3\mathrm{An}$`→<sup>3</sup>An ancillary Mathematica<sup>R</sup> file…www.arxiv.org）✓；
  尾块地址（**Centre de recherches math´ematiques…拆断双行→逐字重构 Montréal (Québec) H3T 1J4 +
  E-mail address: maynardj@dms.umontreal.ca**）✓ — **PASS**

## 总评

- **覆盖声明**：25/25 页经可靠文本层逐字符对账 + md 全文交叉核对（1033 行全读，含 §6-§8 全部
  引理/方程）；150dpi 全 25 页渲染，p.1/2/5/6/7/16/18/19/22 九页目检、p.1/p.7 另 300dpi 终裁。
- **FAIL 修复（152 处 / 125 规则，两轮）**：①liminf 乱码 ×14；②方程编号错位 7 组 16 tag
  （裸编号行与相邻 \tag 错一位，全部拆分重编，修复后 \tag 清单 1.1-8.17 与 print 完全一致、
  无重复无缺失）；③幽灵下标碎片 ×4 组还原为正文；④ff 连字 ×28；⑤句号/逗号粘连 ~21；
  ⑥丢空格 ×12；⑦控制字符 \x03×4→□；⑧Theorem 1.2 分母 ∈→⊆ + 孤儿 display 删除；
  ⑨s=#𝓡₂→#𝓐₂、[d_i,e_i]]→|、dot{h}₁′、dot{N}、bar θ、overset/stackrel 点等号、\boldsymbol h、
  {\cal O}{\cal F}、\mathbf{sup}、y_*；⑩数字间距（70 000 000/4.0020697/1 417 255/708 216/42×42）；
  ⑪尾部变音 + 地址块重构。
- **源级 quirk 清单（忠实不改）**：**"from Zhang's theorem the that number"**（p.1 print 即有
  the，300dpi 证据）；**"functions g is of the form 1/(1+At)"**（p.18 print 即此）；**"We comment
  the polynomials"**（缺 that，p.22 print 即此）；**"recall that from Section 2 that"**（p.6 print
  即此）；"(and there are k elements, …greater than k.)" 句号在括号内；[1,x]² 上标（print 即此）；
  footnote 3 Mathematica^R；Yıldırım ı 逐字保留。
- **可用性结论**：修复后 md 可作该 arXiv v3 论文忠实底本；(1.1)-(8.17) 全部 97 个编号方程
  逐条核对编号与内容全对；Theorems 1.1-1.4、Propositions 4.1-4.3、Lemmas 5.1-5.3/6.1-6.3/
  8.1-8.3 全部在位；References 9 条 + fn1/fn2/fn3 三足注完整。本篇 25/25 页完成，无未决项；
  与 Maynard published（31p，Annals 181 (2015) 383-413，待审）同目录。
