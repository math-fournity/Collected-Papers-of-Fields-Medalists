# AUDIT — James Maynard, "Counting primes"（ICM 2022 会议论文，Proc. Int. Cong. Math. 2022 Vol.1，DOI 10.4171/ICM2022/206；born-digital，MiKTeX pdfTeX + hyperref）

> mineru: standard 档导出 `ICM2022_proceedings_Maynard_mineru/`；**born-digital 文本层主对账通道**
> （pdftotext 81.5KB/0 FFFD 逐点仲裁）+ PNG 抽验（题录页整页目检；150dpi 全 29 页入库）。
> 同 ICM 2022 proceedings 伪影族。

## 逐页签（29/29；文本层全对账，print 页脚 = PDF p.N − 1）

- **p.001**：标题/Abstract/MSC 11N05; 11N35, 11M06, 11N13/Keywords（**print 原文逗号后无空格：
  "Prime numbers,sieve methods,Type I/II sums"，md 一度加空格已按 print 回退**）/ICM ©+DOI ✓ —
  PASS±（© 块惯例；Keywords 空格源级）
- **p.002-003**（§1）：Question、Landau 四问题三例（𝒜=ℤ/p+2/2N−p）、Goldbach、Vinogradov 三素数
  [42]、toolkit 纲领 ✓ — PASS（修复后：�→x、suficiently、ofintegers、**"In this case A contains"**）
- **p.004-006**（§2 + §2.1 素数与零点）：ζ Euler 乘积、Explicit Formula (2.1)（Von-Mangoldt）、
  RH 结构讨论、**"treating all terms apart from x trivially"（print 原文，忠实）**、self-improving PNT、
  Goldfeld–Gross-Zagier [29,30,34] ✓ — PASS（修复后：�→L ×10、non-trivial 拉开串、[66] 引用补入）
- **p.007-009**（§2.2 零密度 + Q1/Q2 + Thm3）：Density Hypothesis、Huxley [44] 12(1−σ)/5、
  Heath-Brown [36]、Q1 Dirichlet 多项式测量式、Q2（**"/log x for some large x" mash 修**）、
  Thm 3（13/24 指数，"zeros of ζ(s) lie on finitely many vertical lines"，Pratt [66]）、
  Matomäki-Radziwiłł [54] ✓ — PASS（修复后：数字拆分 12/13/24、𝜁(s)、onfinitely）
- **p.010-012**（§2.3 + §3 筛法开头）：三条局限（**print 原文 "it require a lot of work" 忠实**）、
  Hooley Artin [43]、π* 上界、Q4（"unconditionally" 断词修）、sieve Property（**Primes are integers n**）、
  inclusion-exclusion (3.1)(3.2)、fundamental lemma ✓ — PASS（修复后：�→q/d/γ、fai→fail、degre→degree、
  esti mates→estimates）
- **p.013-015**（Lemma 5/6 + 高维筛）：F/f(κ,η,γ)、linear sieve 最优、**A^± = {n∈[x, x+x^{γ+ε} : λ(n)=∓1}
  ——print 原文缺 "]"，忠实**、Liouville、delay-differential、Q7/Q8、Chen twist [9] ✓ — PASS（修复后：
  �→x/g/κ/k、there arefunctions、thefollowing、diferent integers d）
- **p.016-018**（§3.2 奇偶现象 + §4 旁路）：sieve weights、**"right had side"（print 原文忠实）**、
  **"will be off by a factor of at least 2"（print off，md 原误 of 已修）**、Brun-Titchmarsh [69]、
  **"this is off by a factor of roughly 2"（print off 已修）**、Thm 9 bounded gaps（246/O(e^{3.815k})/
  Baker-Irving [3]）、pigeonhole、**h₁<⋯<h_K（"< . . <" 乱串已修）**、Elkies Thm 10（ℓ's 乱串修）、
  **"reduce to a much counting problem"（print 原文缺词，忠实）**、Thm 11 large gaps（Erdős-Rankin 型
  分母单层 log log log x，print 即此）、Tao [74] 2-point Chowla ✓ — PASS（修复后）
- **p.019-021**（§5 BV/EH/超平方根屏障）：BV Theorem 13、Elliott-Halberstam Conjecture 1、
  （**print "…conjecture. For example, the bound 246…improved to 12"——句号断句为 print 原文**）、
  square-root barrier、Fouvry/BFI [5-7,22]、Thm 14 triply well-factorable（**wellfactorable→well-factorable**）、
  Lichtman [51]、Zhang [82]/AFHB [1,23]、Q15（**"for any a, A" 按 print**）、Q16 四因子和 ✓ — PASS（修复后）
- **p.022-024**（§6 双线性 + Type I/II + Vaughan + Harman）：(6.1)(6.2)、m's/nm（�� 乱串修）、
  parity 传递论证、Type I/II ranges 定义（**[0<sub>,γ</sub> HTML 行→[0, γ]；". β_ℓ" 杂串删**）、
  roles of **n, m**（按 print）、Lemma 18 Vaughan's identity、**lim inf Φ 乱码→liminf_{x→∞}、
  lim sup 同修**、Harman sieve [35]、Q19/Q20 ✓ — PASS（修复后）
- **p.025-027**（§7 thin sets + 三组例）：#𝓐_d 整数性限制、(7.1)、**"#𝓡→#𝓐 系 mineru 花体误读，×7 修正**、
  Type I [0,1−θ]/Type II [θ,1−2θ]（**md 误作 x 幂区间已按 print 修**）、Vaughan [76] 非齐次逼近、
  incomplete norm forms [65]、Jia [48] 9/28、short intervals 0.525 [2]、Watt [79]、Heath-Brown [38]
  a³+2b³、Matomäki [53]、restricted digits [64]、HBL [41]/Merikoski [67]/Xiao [81]/FI [27]、
  Q21、Legendre ✓ — PASS（修复后）
- **p.028**（§8 进一步算术信息 + §9 lift）：Linnik identity [52]、τ′_j、Heath-Brown identity [36]、
  divisor function AP [24,25,37]、Buchstab、**"Even if the … arithmetic information in insufficient"——
  "in" 系 print 原文（语法 quirk），insufficient 拼写已修**、Sato-Tate [14]、Q22、Q23、lift、
  中间比较集 B、Q24、Drappeau [12,13] ✓ — PASS（修复后）
- **p.029**（§10 + Ack + References [1]-[82]）：Siegel 零点局限、指数和、Titchmarsh [13]、Pitt [70]
  391/392、Green-Tao [32]/[33]/[55,73]、**"seem harder that the classical"（print 原文忠实）**、
  quadratic Dedekind L-function、致谢（**Royal Society Wolfson/ERC 851318**）、References 82 条逐条
  （**ofMath. ×10 修**；[42] "Annals of Mathematic Studies"、[56] "möbius"、[59] "Unifrorm"、
  [72] Diference、[77] "Dirichet" 均 print 原文忠实；[9] "larger even integer" 系 Chen 论文原题 ✓）、
  作者块（Mathematical Institute, Oxford, England OX1 4AU）✓ — PASS（修复后）

## 总评

- **覆盖声明**：29/29 页文本层全对账 + PNG 抽验（p.001 整页）+ 150dpi 全 29 页入库；born-digital 通道。
- **系统性修复**：丢字形 � ×35+（x/T/q/d/z/γ/κ/k/L/n/m/E/a/A/αn 按上下文）；"#𝓡→#𝓐" ×7（mineru
  花体误读）；数学结构修复：⇒ 误读为 =（Lemma 6 displays ×2）、"< . . <"→⋯<、Type I/II 区间
  x-幂→指数区间、lim inf Φ 乱码、[0<sub>,γ</sub> HTML 行、". β_ℓ" 杂串、e^{th} 拉开、非断行 −λ(n)；
  引用补入 [66]（Pratt）；数字拆分（12/13/24/9-28/0.525 等）；ff ×17（coeficients/diferent/dificult/
  suficient/sufice/requried/typcially/efective/wellfactorable/Availble/arithmeti）；粘连 ×14（ofintegers/
  showfor/somefixed/oneproduce/boundfor/estimatefor/overprimes/ofthe/properties ofthe/l i f t/givenfixed/
  ofsets/ofinterest/ofMath.×10）；"A contain"→contains；"of by"→off ×2。**共约 240 处/110 规则**。
- **源级 quirk 清单（忠实不改）**："the beginning **right had side**"；"**it require** a lot of work"；
  "reduce to **a much** counting problem"（缺 simpler）；"**Even if the** … information **in** insufficient"
  （print 原文 in）；"seem **harder that** the classical"；Keywords 行逗号后无空格；Keywords 逗号
  无空格；"A^± = {n ∈ [x, x+x^{γ+ε} : …"（print 缺 "]")；"apart from x trivially"；"; under the
  Elliott-Halberstam conjecture. For example…"（句号断句）；Theorem 11 分母单层 log log log x；
  [42] "Annals of Mathematic Studies"；[56] "möbius" 小写；[59] "Unifrorm"；[72] "Diference"（题首大写）；
  [77] "Dirichet"；©/DOI 块未收（惯例）。
- **可用性结论**：修复后 md 可作该文忠实底本；(2.1)、(3.1)(3.2)、(6.1)(6.2)、(7.1) 及各定理/引理/
  问题编号齐全，82 条 References 与作者块完整。与 Maynard arXiv/published small gaps（均已审 ✅）、
  laudatio（已审 ✅）、popular exposition（待审）构成 Maynard 目录闭环。

### 修复登记（2026-09-30）

- pass-1 约 150 规则 applied + pass-2 38 + 内联终清 9（脚本迭代中的结构性错误已按铁律 3 整文件重写
  纠正——初版脚本把两类循环头写混，未污染 md）。
- fix(md) commit 父提交 = 修复前 md 原貌；脚本 /tmp/maynard_icm_fix/fix_md.py + fix2.py + 内联 pass。
- Keywords 无空格一度误加空格，经 p.001 PNG 证实 print 原貌后回退（审计即权威）。
- 本篇 29/29 页完成，无未决项。
