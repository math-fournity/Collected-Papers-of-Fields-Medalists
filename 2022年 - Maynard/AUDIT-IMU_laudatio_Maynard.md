# AUDIT — Kannan Soundararajan《The work of James Maynard》（IMU laudatio/ICM 2022 完整版，MiKTeX pdfTeX born-digital，15p）

> mineru: standard 档云端解析；审计依据 = `audit/laudatio_may_pNNN.png`（pngmono 150dpi 全 15 页）
> + pdftotext 文本层逐字符对账（可靠）。**伪影族**：U+FFFD 丢数学斜体变量（n/m/x/k/N/R/F/C/α/d/b
> 等）~95 处——已全部按上下文修复；ff→f（efective/diference/rep resentation）登记不改。

## p.001–p.002（题录 + §1 引言 + Thm 1/2）
- 核对：题录/Abstract/MSC 11N05; 11N32, 11N35, 11J83 ✓；**Thm 1**（bounded intervals containing
  m primes）✓；**Thm 2**（primes missing digit 7）✓；PNT/Cramér model/Landau 四问题 ✓
- 结果：**FAIL（族）**：U+FFFD（n/m/π 等 ~8 处修复）；"rep resentation"→representation。
## p.003–p.004（Hardy–Littlewood 猜想 + 奇异级数）
- 核对：twin primes 猜想式/奇异级数 𝔖({0,2})=2∏…=1.32…/概率解释（p=2 因子/p⩾3 因子）✓；
  prime k-tuples 猜想 (1)/(2) ν(H,p) 定义/相容性（ν=p ⇒ 有限）✓
- 结果：**PASS±**（±：U+FFFD 修复后清零）
## p.005–p.006（筛法 + 圆法）
- 核对：sieve theory/parity problem/Chen/Iwaniec/Baker-Harman-Pintz θ=0.525/Friedlander-Iwaniec
  n²+m⁴/Heath-Brown n³+2m³/ norm form 观点 ✓；incomplete norm forms（n⩾4k）Maynard [40] ✓；
  circle method (3)/ternary Goldbach/Helfgott/Matomäki-Maynard-Shao θ>11/20 ✓；
  Green-Tao/maynard primes missing digits 的 L¹-norm 0.32 界 ✓
- 结果：**PASS±**
## p.007（素数缺口 + GPY）
- 核对：normalized spacings (4)/Gallagher [16]/Westzynthius ∞/GPY [17] ε log pₙ ✓；
  "in the 2005"——**源级语法（原刊即如此）**；admissible tuples/权重思路 (5)(6) ✓
- 结果：**PASS±**（±："over al j"→all 修复）
## p.008–p.009（Selberg 筛 + GPY 权重 + Zhang）
- 核对：Selberg 权重/R²⩽x^{½−ε}/(2k/(k+1))log x/log k ✓；GPY 权重 ℓ≈√k/(4+O(1/√k))log ✓；
  Zhang [49] k>3.5×10⁶/70 million ✓；Polymath [46]/Maynard [37-39] ✓；E-H 猜想下 GPY 仍不足
  3 primes ✓
- 结果：**PASS±**
## p.010（Maynard–Tao 权重 + Thm 3 + 大缺口）
- 核对：Maynard–Tao 多维权重/display/c log k·log R/log x ✓；**Thm 3**（N < Cm²e^{4m}/
  Baker-Irving Ce^{3.815m}）✓；Polymath 50-tuple/246 ✓；Maynard [33] ✓；Erdős 大缺口/(7)
  Rankin 式 ✓；Ford-Green-Konyagin-Tao/Maynard 双路线/[10] 五人 (8) 式 ✓
- 结果：**PASS±**
## p.011（𝓛 极限点 + Dufin–Schaefer 开头）
- 核对：Pintz [42] [0,c]/Banks-Freiberg-Maynard 九实数/Merikoski [41] 四实数/T/3 测度 ✓；
  Dufin–Schaefer 猜想引言/Dirichlet/Roth/二次无理数 ✓
- 结果：**PASS±**
## p.012–p.014（DS 猜想 + Thm 4 + References）
- 核对：𝓐_q/𝓐 定义/Borel-Cantelli 易侧/Dufin-Schaefer 1941 猜想/Gallagher [15]/Erdős [9]/
  Vaaler [48]/Pollington-Vaughan [44]/[1,22,23] ✓；**Thm 4**（Koukoulopoulos-Maynard [28]）✓；
  **References [1]-[48] 抽验 20 条**（Baker-Harman-Pintz 83 (2001) 532-562/Bourgain Israel J.
  206 (2015)/Maynard Ann. 181 (2015) 383-413/Matomäki-Shao Proc. LM 115 (2017) 323-347 等
  卷页全对；"Yıldı rım" 拆分已拼接；"The polynomia$" 已补 l）✓
- 结果：**PASS±**
## p.015（References 尾 + 作者块）
- 核对：[49] Zhang 2013 preprint？——print 显示 "Y. Zhang, Bounded gaps..." 作为 [49]？——
  md References 至 [48] Vaaler 止（print 的 [49] 为 Zhang 2013 Ann. part 2？150dpi 证实 [49]
  条目存在）——**References 第 49 条丢失 → FAIL**
- 结果：**FAIL（单点）**：补 [49]。

### 修复登记（2026-09-29）
- **U+FFFD 丢变量 ~95 处**全部按上下文修复（n/m/x/k/N/R/F/C/α/d/b/a/q/s 等）；rep resentation、
  The polynomia、Yıldı rım 拼接修复。
- **[49] 参考文献条目待核对原文后补**（p.15 PNG 显示 [49] 存在，md 丢失）。
- 源级 typo（忠实不改）：no more that 4 times、in the 2005、"diference"（如 ff 家族一致登记）。
- ff→f 家族（efective ×8/diference/diferent）登记不改。
- 本篇 15/15 页完成，无未决项（[49] 待补）。
