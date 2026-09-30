# AUDIT — M. Viazovska《On discrete Fourier uniqueness sets in Euclidean space》（ICM 2022 会议论文，MiKTeX pdfTeX born-digital，14p）

> mineru: standard 档云端解析；审计依据 = `audit/icm22_viaz_pNNN.png`（p.3/p.4/p.5 全页抽验 +
> 300dpi p.3）+ pdftotext 文本层逐字符对账（可靠文本层，全 md 核对）。
> **⚠️ 特殊伪影族**：md 含 ~40 处 U+FFFD/丢字母（数学斜体变量 d/r/s/f/b/m/C/α 等在
> 解析中丢失），已按上下文逐一修复（见登记）。

## p.001–p.002
- 核对：题录（MSC 11F67/11F41/11G40、Keywords）✓；§1（Fourier uniqueness 定义 1.1、
  [3] sign(n)√|n| 集、Stoller [4] S(√n) 并集、**Thm 1.2**、Ramos-Stoller [5]）✓；
  M_X(r) 增长问题 ✓；§1.1 (1.1) 构造/Def 1.3 球面 design/**Thm 1.4**/"known [?]" ✓
- 结果：**PASS±**（±：①"goal of this paper give"——原刊即缺 "is to"（源级语法，忠实）；
  ②"[?]" 断引用系原刊 LaTeX \cite 破损（PNG 证实）；③U+FFFD 字形族（随修复））
## p.003
- 核对：Thm 1.4 续/§2 分解 (2.1)/**Thm 2.1**/φ_{p,n} 与 (2.2)(2.3)(2.4)(2.5)(2.6) ✓
- 结果：**PASS±**
## p.004
- 核对：(2.2)(2.3)(2.4)(2.5)(2.6) 逐式 ✓；**Laplace 算子显示式 "∂²/∂x₁²+…+∂²/∂x₁²"——
  print 末项同为 x₁²（源级 typo，应为 x_d²）——md 忠实保留**（150dpi 复核）；极坐标
  ζ=x/‖x‖ ✓；Δ_{S^{d−1}} 算子 ✓；极坐标计算两 display ✓
- 结果：**PASS±**（±：ζ=x/‖x‖ 的 md 分式排版伪影修复）
## p.005
- 核对：(2.7) Δ_{S_d}(g(r)p(x))=−deg(p)(deg(p)+d−2)g(r)p(x) ✓；λ_m 定义 ✓；f̃=Δ^α f 分解 ✓；
  §3 变换规则 display（**md 与原刊一致**）✓；**Thm 3.1** Voronoi（S_{d/2}(Γ(2),χ_d)）✓；
  N(k,ε) 定义（ζ(k−2)4π 分母）✓；N(k,ε)∼k/2πe ✓
- 结果：**PASS±**（±：χ_k/χ_d 混用系原刊自身（Thm 3.2 印 χ_d）；"straight forward" 分写）
## p.006–p.007
- 核对：**Thm 3.2**（(1)(2)(3) 三条件、Fourier 展开、系数估计 C m^{−k/2+α}n^{k/2+α}）✓；
  §4 Poincare 级数/Petersson 公式 (4.1)/𝒥_c Bessel/Kloosterman 和 [2, p.51, eq.(3.13)] ✓；
  **Lemma 4.1**/Lemma 4.2 (1)(2)/Mehler-Sonine/|S(m,n,c)|<c²/(4.2) 链 ✓；
  "Kloosterman"（245 行）与 "Klostermann"（287 行）并见——**后者系原刊源级拼写**（忠实）；
  "our choise"——源级拼写 ✓；矩阵 A 四分段定义/(4.3) B=A^{−1} 对角占优 ✓
- 结果：**PASS±**（±："Proof of part (3) is analogous"——原刊如此（Lemma 4.2 仅 (1)(2)，
  编号错位系源级，忠实）；"is the Bessel J-function is given by" 双 is 系原刊）
## p.008–p.009
- 核对：(4.4) h_ℓ 定义/(4.5) h̃_ℓ/矩阵对称性/(4.3) 应用/part(3) 系数界 (2C/(1−2ε)ε²)N^{2+ε}m^{1+ε}、
  "Analogosly"（源级拼写）✓；§5 **Lemma 5.1**（head/tail 分解/(5.1)(5.2)）✓
- 结果：**PASS±**
## p.010–p.011
- 核对：**Lemma 5.2**（Fourier 唯一性+Voronoi 结合/𝓕_d(f_p)=(−i)^{deg(p)}p(y)𝓕_{d+2deg(p)}(g_p)）✓；
  条件(1)(2)引用式/|f_p(√mζ)|m^{−deg/2} 界/𝛼̃:=α+d/4 ✓；D(n)=B̃n^Ã 搜索/N(k,ε)⩾bk/𝓝(p)=b deg(p) ✓
- 结果：**PASS±**
## p.012–p.013
- 核对：**Lemma 5.3**（D(n)=2B̃n^Ã、B̃>2max(b+1/b, CC′/b^{β+γ+1})、Ã=2𝛼̃+β+γ+2）✓；
  part(1)(2)/和的重排/C'C'(1/b)(1/b)^{β+γ}/(m/bB̃)^{(2𝛼̃+β+γ+2)/Ã} ✓；(5.3)(5.4)/Lemma 5.1 应用/
  Lemma 5.2 应用/换序/矛盾归谬 ✓；φ_{q,m}=0 (m⩾N(q))/Theorem 1.2 收尾/□ ✓
- 结果：**PASS±**
## p.014
- 核对：Acknowledgments（Stoller/Ramos）✓；Funding（SNSF）✓；**References [1]-[5] 逐条**
  （Gradshteyn-Ryzhik 8.411.10/Iwaniec "authomorphic"——**源级拼写**（automorphic）/Radchenko-
  Viazovska arXiv:1701.00265/Stoller Trans. AMS 374(11) 8045-8079/Ramos-Stroller JFA 282(12)
  109448）✓；作者块（Ecole Polytechnique Federale de Lausanne、**maryna.viazoivska@epfl.ch**
  ——源级 email 拼写（应为 viazovska），ICM 论文集即如此，忠实）✓
- 结果：**PASS±**（±：ref[4] "interpolationfrom"/ref[2] "Math ematical" 空格伪影——修复）

## 总评

- **覆盖声明**：14/14 页（p.3/p.4/p.5 全页 PNG + 300dpi p.3 抽验 + 全篇文本层逐字符核对）。
  mineru：standard 档。
- **FAIL 修复（两大类）**：①**U+FFFD/丢变量 ~40 处**（数学斜体 d/r/s/f/b/m/C/α 等按上下文
  逐一恢复）；②排版伪影（ζ 分式、χ_d)) 多余括号、interpolationfrom/Math ematical 空格、
  𝒯_c→𝒥_c 统一）。
- **源级 quirk（忠实不改，8 项）**：①"goal of this paper give" 缺 is to；②"known [?]" 断引用；
  ③Laplace 末项 ∂x₁²（应 x_d²）；④χ_k/χ_d 混用；⑤Klostermann/choise/Analogosly/
  representaion 类拼写；⑥"straight forward" 分写；⑦"is...is given" 双 is；⑧作者 email
  viazoivska。Lemma 4.2 的 "Proof of part (3)" 编号错位亦系原刊。
- **可用性结论**：修复后 md 可作该 ICM 论文忠实底本；与 dim24 arXiv 版、Annals 版审计件
  同构互补（Viazovska 三件套齐）。

### 修复登记（2026-09-29）
- U+FFFD/丢变量 ~40 处按上下文逐一恢复（d/r/s/f/m/C/α/X/b/p/q 等）；ζ 分式排版；
  𝒯_c→𝒥_c 统一；"interpolationfrom"/"Math ematical" 空格；"Schwartzfunction"→"Schwartz
  function"（若原刊排印即连写则此修复仅为可读性，md 已按文本层两种形态并存处理——登记说明）。
- Laplace 末项 ∂x₁² **撤销 FAIL**（p.4 PNG 证实原刊源级 typo，md 忠实）；χ_k/χ_d、
  Klostermann、choise、"part (3)" 编号错位、viazoivska email 均登记为源级 quirk。
- 本篇 14/14 页完成，无未决项。
