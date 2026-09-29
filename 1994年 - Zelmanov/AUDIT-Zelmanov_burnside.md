# AUDIT — Vaughan-Lee & Zel'manov, "Bounds in the restricted Burnside problem"（J. Austral. Math. Soc. (Series A) 67 (1999), 261–271）

> mineru: standard 档云端解析（parse_mode=ocr），导出 `Zelmanov_1999_restricted_burnside_mineru/`；
> 审计依据 = 二值化渲染 `audit/pNNN.png`（pngmono 150dpi）对照
> `Zelmanov_1999_restricted_burnside__Zelmanov_1999_restricted_burnside.md`。逐页审计，一页一签。
> PDF 结构：11 页 = 印刷 pp.261–271；PDF 由 ABBYY FineReader 生成（Cambridge Core 下载件，
> 含文本层，但页脚带下载水印行）。

## p.001（PDF p.1 / 印刷 p.261）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：
  - 页眉 `J. Austral. Math. Soc. (Series A) 67 (1999), 261–271`、页码 261、Cambridge Core 下载页脚
    （IP/日期/doi 行）均未转写（系统性）
  - 题名/作者/献词/收稿日期/Communicated by E. A. O'Brien ✓
  - Abstract、1991 MSC（primary 20F05, 20D15）、Keywords and phrases ✓
  - §1 Introduction：Burnside 1902 引文（斜体）、现代表述、Golod [8] p-groups、
    B(m,n)=F_m/N（N 由 {gⁿ} 生成）、F_m 秩 m ✓ 逐字
  - 版权行 "© 1999 Australian Mathematical Society 0263-6115/99 \$A2.00 + 0.00" ✓（以 page_footnote span 保留）
- 结果：**PASS±**（±：页眉/页码/Cambridge 页脚丢弃）
- 备注：本页无内容级差异。

## p.002（PDF p.2 / 印刷 p.262）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：
  - 页眉 `262  Michael Vaughan-Lee and E. I. Zel'manov  [2]`、Cambridge 页脚未转写（系统性）
  - 斜体设问：For which values of m and n is B(m, n) finite? ✓
  - 综述段：B(m,2) 初等交换、Burnside B(m,3)/B(2,4)、Sanov [37] B(m,4)、Hall [14] B(m,6)、
    Novikov–Adjan [33–35] n≥4381、Adjan [2] n≥665、Olshanskii n>10¹⁰、Ivanov [20] n≥2⁴⁸ 且 2⁹ 整除、
    Lysenok [26] n≥8000、偶指数与二面体子群 ✓ 全部数字与引文号吻合
  - 斜体设问：Are there only finitely many finite m-generator groups of exponent n? ✓
  - R(m,n) 通用有限群、'Yes' 结论、Hall–Higman [15] 归约、Kostrikin 1959、Zel'manov [45,46] p^k ✓
- 结果：**PASS±**（±：页眉/页码/页脚）
- 备注：本页无内容级差异。

## p.003（PDF p.3 / 印刷 p.263）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：
  - 页眉 `[3]  Bounds in the restricted Burnside problem  263`、Cambridge 页脚未转写（系统性）
  - "R(m,n) of exponent n." 承接 ✓；**2. Bounds** ✓
  - "Once we know …" 段（Adjan–Razborov [3]、Kostrikin [23]、原词 "wowsers"、Grzegorczyk Gr⁵/Gr⁴、[42]）✓
  - **|R(m,p)| ≤ underbrace{m^m·^m}_{3^p}** ✓（塔式与 underbrace 标签）
  - **|G| ≤ underbrace{m^m^m}_{q^q^q}** ✓；**|G| ≤ underbrace{m^{m^{·^{·^m}}}}_{n^n^n}** ✓；
    **|G| ≤ 2^{2^{·^{2^m}}}**（n^n^n 个 2）✓ —— 四座 tower 逐符号吻合
  - "Numbers of this magnitude …" 段、Mike Newman 的观察 ✓；**|R(m,2^k)| ≥ 2^{2^{·^{2^m}}}**（k 个 2）✓
- 结果：**PASS±**（±：页眉/页码/页脚）
- 备注：tower 公式（本论文核心风险点）全部吻合。

## p.004（PDF p.4 / 印刷 p.264）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：
  - 页眉 `264  Michael Vaughan-Lee and E. I. Zel'manov  [4]`、Cambridge 页脚未转写（系统性）
  - 级数 F=F₀>F₁>F₂>⋯；F_{i+1}=(F_i)²；F_i/F_{i+1} 初等交换；F/F_k 指数 2^k；
    **|F/F_k| ≥ 2^{2^{·^{2^m}}}** ✓
  - 归纳论证（|F/F₁|=2^m；Schreier 公式；rank 1+(m−1)n；F_{k−1}/F_k 阶 2^{1+(m−1)n} > 2^n；
    Gowers [10] 与 Gr³）✓
  - Newman 猜想不等式：`\underbrace{2^{2^{·^{2^{f(m)}}}}}_k ≤ |R(m,n)| ≤ \underbrace{2^{2^{·^{2^{g(m)}}}}}_k`
    —— md 丢失塔内省略点 **·**（见 ±）；k = ⌊log₂ n⌋ ✓
  - **Conjecture A**（(p−1)-Engel 代数、Z_p、a∈L 生成幂零理想、N=N(p)、class ≤ mN、order ≤ p^{m^n}、
    p=5 由 Higman [19]、可取 N=6 [16]）✓
  - **Conjecture B**（∃ r,N；[a₁,…,a_r]；p=7 时 r=8 [41]）✓
- 结果：**PASS±**
  - ±：猜想不等式中两座 tower 的省略点 "·" 在 md 中丢失（塔高由 underbrace `k` 与上下文表达，语义不损；
    严格记法应为 `2^{2^{\cdot^{2^{f(m)}}}}`）。
- 备注：除该记法小瑕外，本页逐符号吻合。

## p.005（PDF p.5 / 印刷 p.265）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：
  - 页眉 `[5]  Bounds in the restricted Burnside problem  265`、Cambridge 页脚未转写（系统性）
  - R(m,8) 的类不能被 m 的多项式界定；指数 8 群的伴随 Lie 环 ✓
  - PI-代数段：R(L)=End_F(L) 中由 ad(a) 生成的子代数、x ad(a)=[x,a]、SPI 定义 ✓
  - **PROPOSITION 1**（Conjecture A ⟹ (p−1)-Engel 代数 SPI；SPI ⟹ Conjecture B）✓
  - PROOF（Latyshev [24] 思路；自由 (p−1)-Engel 代数、可数无限秩；Kostrikin 张成；1≤r≤p−1；
    R(L)^{p−1}；w_i = ad(x_{(p−1)(i−1)+1})ad(x_{(p−1)(i−1)+2})⋯ad(x_{(p−1)i})）✓
  - 线性相关论证、V_{m(p−1)} 子空间、Σ_{σ∈S_m}α_σ w_{1σ}⋯w_{mσ}=0 ✓；
    v₀ad(a)v₁ad(a)v₂⋯v_{N−1}ad(a)v_N = 0 ✓；线性化 Σ_{σ∈S_N}v₀ad(a_{1σ})v₁⋯ad(a_{Nσ})v_N = 0 ✓
- 结果：**PASS±**（±：页眉/页码/页脚）
- 备注：本页无内容级差异。

## p.006（PDF p.6 / 印刷 p.266）
- PNG：audit/p006.png（pngmono 150dpi）
- 核对：
  - 页眉 `266  Michael Vaughan-Lee and E. I. Zel'manov  [6]`、Cambridge 页脚未转写（系统性）
  - **(1)** v₀ad(a₁)v₁⋯ad(a_N)v_N = −Σ_{1≠σ∈S_N} v₀ad(a_{1σ})v₁⋯ad(a_{Nσ})v_N ✓
  - N-disorder 定义、V_k 张成、字典序更早的重写论证、Lemma 1 in [5, p. 176]、(N−1)^{2k}、
    dim_F(V_k) ≤ (N−1)^{2k}、dim_F(V_{m(p−1)}) ≤ (N−1)^{2m(p−1)} < m! ⟹ L 为 SPI ✓
  - Amitsur 结果（⌊d²/4⌋）、Kostrikin（L 与 R(L) 局部幂零）✓；QED `□`（原件有，md 未录——记法级）
  - Hanna Neumann 书问题 4 [29] ✓；w₂=[x₂,x₁,x₁]、w_m=[x_m,w_{m−1},w_{m−1}]、weight 2^m−1、
    w_d=1 恒等式、Hirsch-Plotkin radical 论证 ✓
- 结果：**PASS±**（±：页眉/页码/页脚；QED `□` 未录）
- 备注：本页无内容级差异。

## p.007（PDF p.7 / 印刷 p.267）
- PNG：audit/p007.png（pngmono 150dpi）
- 核对：
  - 页眉 `[7]  Bounds in the restricted Burnside problem  267`、Cambridge 页脚未转写（系统性）
  - 承接句（类被 m 的多项式界定 ⟹ 存在 d）✓
  - Zel'manov [47]、N₁(G)（全体交换正规子群之积）、N_{i+1}(G)/N_i(G) = N₁(G/N_i(G)) ✓；
    G = N_s(G)、Hanna Neumann 问题的肯定解 ✓
  - 导出列长度界：Bachmuth–Mochizuki–Walkup [4]（指数 5 不可解）、Razmyslov [36]（p^k ≥ 4）、
    derived length > ⌊log₂ m⌋ ✓
  - **3. Small exponent**：n ≤ 7 的各阶界 ——
    (1) |B(m,2)|=2^m ✓；(2) 3^{m+C(m,2)+C(m,3)}（Levi–van der Waerden [25]）✓；
    (3) 2^k、½4^m ≤ k < ½(4+2√2)^m（Mann [28]）✓；(4) |R(m,5)| ≤ 5^{m^{6m}} [16] ✓；
    (5) |B(m,6)| = 2^a·3^{b+C(b,2)+C(b,3)}、a=1+(m−1)3^{m+C(m,2)+C(m,3)}、b=1+(m−1)2^m（Hall [14]）✓；
    (6) |R(m,7)| ≤ 7^{m^{51m^8}}（Vaughan-Lee [41]）✓ —— 全部指数/系数逐符号吻合
  - **4. Use of computers** 段首 ✓
- 结果：**PASS±**（±：页眉/页码/页脚）
- 备注：小指数各界的 tower/指数全部吻合。

## p.008（PDF p.8 / 印刷 p.268）
- PNG：audit/p008.png（pngmono 150dpi）
- 核对：
  - 页眉 `268  Michael Vaughan-Lee and E. I. Zel'manov  [8]`、Cambridge 页脚未转写（系统性）
  - p-quotient 算法与 graded Lie rings 的 nilpotent quotient 算法；指数 4,5,7,8,9 群 ✓
  - PCP 定义：{a₁,…,a_n}、n 个幂关系 a_i^p = a_{i+1}^{α(i,i+1)}a_{i+2}^{α(i,i+2)}⋯a_n^{α(i,n)}、
    0 ≤ α(i,k) < p（1 ≤ i < k ≤ n）、binom(n,2) 个换位关系
    [a_i,a_j] = a_{i+1}^{α(i,j,i+1)}a_{i+2}^{α(i,j,i+2)}⋯a_n^{α(i,j,n)}、0 ≤ α(i,j,k) < p（1 ≤ j < i < k ≤ n）✓ 逐符号
  - Macdonald [27]、'Canberra nilpotent quotient algorithm'（Havas–Newman，[17]）、Newman–O'Brien [30] ✓
  - R(2,5) [18]、B(3,4) [6]、B(4,4)（1989）、B(5,4)、R(3,5)；B(6,4)/R(4,5)/R(2,7) 之难；
    R(2,7) 的 class 21 quotient 阶 **7^{17199}**；GB RAM ✓
  - Gupta–Newman [13] 与 Razmyslov [36]（class 3m−2）、Vaughan-Lee [40]（2^{k−1} < 3m−2 ≤ 2^k）、Mann [28] ✓
- 结果：**PASS±**（±：页眉/页码/页脚）
- 备注：本页无内容级差异。

## p.009（PDF p.9 / 印刷 p.269）
- PNG：audit/p009.png（pngmono 150dpi）
- 核对：
  - 页眉 `[9]  Bounds in the restricted Burnside problem  269`、Cambridge 页脚未转写（系统性）
  - 指数 7/8/9 群：Grunewald–Havas–Mennicke–Newman [12]、M 由 (a⁴b⁴)², b² 生成；
    Newman [31] class 14 quotient、M class ≥4、order ≥2⁶；Ivanov [20] k≥48 ⟹ class ≤ k ✓
  - graded Lie rings 算法：E(m,p)（自由 (p−1)-Engel 代数）、R(m,p)→E(m,p) 同态、
    Kostrikin 手算 E(2,5)（5³⁴、class 12）、Havas–Wall–Wamsley [18]、Wall [44]、R(2,5) 阶 5³⁴、
    E(3,5)/E(2,7) ✓
  - multilinear identities K_n=0、[40, Thm 2.4.7/2.5.1]、W(m,p)、同态链 L(m,p)→W(m,p)→E(m,p)、
    W(3,5)/W(2,7) 阶 5^{2282}/7^{20418}、class 17/29、L(m,5)=W(m,5)（m=2,3）✓
  - [16] R(m,5) class ≤6m、order ≤5^{m^{6m}}；[41] R(m,7) class ≤51m⁸、order ≤7^{m^{51m^8}} ✓
- 结果：**PASS±**（±：页眉/页码/页脚）
- 备注：本页全部数字/指数逐项吻合。

## p.010（PDF p.10 / 印刷 p.270）
- PNG：audit/p010.png（pngmono 150dpi）
- 核对：**References [1]–[28] 逐条**（作者/题名/期刊卷年页/丛书卷号）——全部吻合：
  [1] Ackermann（Math. Ann. 99 (1928), 118–133）；[2] Adjan（Ergebnisse 95, 1979）；
  [3] Adjan–Razborov（Uspekhi Mat. Nauk 42 (1987), 3–68）；[4] Bachmuth–Mochizuki–Walkup（BAMS 76 (1970), 638–640）；
  [5] Bahturin（VNU 1987）；[6] Bayes–Kautsky–Wamsley（LNM 372, 82–89）；[7] Burnside（Quart. J. 33 (1903), 230–238）；
  [8] Golod（Izv. 28 (1964), 273–276）；[9] Gorenstein（Plenum 1982）；[10] Gowers personal communication；
  [11] Graham–Rothschild–Spencer（Wiley 1990）；[12] Grunewald–Havas–Mennicke–Newman（LNM 806, 49–188）；
  [13] Gupta–Newman（LNM 372, 330–332）；[14] Hall（Illinois J. Math. 2 (1958), 764–786）；
  [15] Hall–Higman（Proc. LMS 6 (1956), 1–42）；[16] Havas–Newman–Vaughan-Lee（J. Symb. Comp. 9 (1990), 653–664）；
  [17] Havas–Newman（LNM 806, 211–230）；[18] Havas–Wall–Wamsley（Bull. Austral. 10 (1974), 459–470）；
  [19] Higman（PCPS 52 (1956), 381–390）；[20] Ivanov（IJAC 4 (1994), 1–308）；[21] Kostrikin（Izv. 23 (1959), 3–34）；
  [22] ——（Mat. Sb. 110 (1979), 3–12）；[23] ——（Around Burnside, Springer 1990）；[24] Latyshev（Uspekhi 27 (1972), 213–214）；
  [25] Levi–Van der Waerden（Abh. Hamburg 9 (1933), 154–158）；[26] Lysenok（Izv. Ross. 60 (1996), 3–224）；
  [27] Macdonald（JAMS Ser. A 17 (1974), 102–112）；[28] Mann（J. London Math. Soc. 26 (1982), 64–76）
  - "——"（同作者省略符）在 md 中保留 ✓
- 结果：**PASS±**（±：页眉/页码/页脚）
- 备注：文献区零差异。

## p.011（PDF p.11 / 印刷 p.271，**末页**）
- PNG：audit/p011.png（pngmono 150dpi）
- 核对：**References [29]–[47] 逐条 + 作者地址**——
  [29] H. Neumann（Ergebnisse 37, Springer 1967）✓；[30] Newman–O'Brien（IJAC 6 (1996), 593–605）✓；
  [31] Newman（Bull. LMS 25 (1993), 263–264）✓；[32] Newman–Vaughan-Lee（ERA AMS 4 (1998), 1–3）✓；
  [33] Novikov–Adjan I（Izv. 32 (1968), 212–244）✓；[34] II（251–524）✓；[35] III（709–731）✓；
  [36] Razmyslov（Izv. 42 (1978), 833–847）✓；[37] Sanov（Leningrad 10 (1940), 166–170）✓；
  [38] Sims（Cambridge 1994）✓；[39] Vaughan-Lee（JAMS Ser. A 49 (1990), 386–398）✓；
  [40] ——（The restricted Burnside problem, 2nd ed., Oxford 1993）✓；[41] ——（TAMS 346 (1994), 617–640）✓；
  [42] Vaughan-Lee–Zel'manov（J. Algebra 162 (1993), 107–145）✓；[43] ——（IJAC 6 (1996), 735–744）✓；
  [44] Wall（Bull. Austral. 19 (1978), 11–28）✓；[45] Zel'manov（Izv. Math. USSR 36 (1991), 41–60）✓；
  [46] ——（Mat. Sb. 182 (1991), 568–592）✓；[47] ——（IJAC 3 (1993), 583–609）✓
  - 作者地址：Christ Church / Oxford, OX1 1DP / England / URL / e-mail（vlee）与 Department of Mathematics /
    PO Box 208283 / 10 Hillhouse Avenue / New Haven CT 06520-8283 / USA / e-mail（zelmanov）两栏在 md 中按行交错
    （内容完整，版式交错——见 ±）；ref [45] "Zel' manov" 多一空格（见 ±）
- 结果：**PASS±**
  - ±1：作者双栏地址在 md 中逐行交错（vlee 栏与 zelmanov 栏的 6 行交替排列）——内容完整，仅版式交错；
  - ±2：ref [45] "E. I. Zel' manov" 撇号后多一空格（他处均作 Zel'manov）。
- 备注：文献 [29]–[47] 卷页年逐条吻合。

## 总评
- **覆盖声明**：11 页全部逐页审计（audit/p001–p011.png，pngmono 150dpi）。
- 结论分布：**PASS± ×11；FAIL ×0**——无内容级数学/公式错误。
- 本论文核心风险点（6 座指数塔、PCP 生成关系、小指数各界、Conjecture A/B、文献 47 条）全部逐符号吻合。
- 系统性瑕疵：①页眉（`[n] Bounds in the restricted Burnside problem` + 页码 + 作者名）与 Cambridge Core
  下载页脚全部未转写；②p.264 两座 tower 的省略点 "·" 丢失（p.263 的塔保留了 "·"）；
  ③QED `□` 未录；④p.271 作者双栏地址按行交错；⑤ref [45] "Zel' manov" 多一空格。
- 忠实性正面案例（勿改）：原词 "wowsers"；tower 的 underbrace 分组与标签（3^p / q^q^q / n^n^n）。
- 可用性：全 11 页文本、公式与文献可放心引用；**无 FAIL 项**。
- mineru 解析信息：mineru 3.4.4 / tier=basic / parse_mode=ocr（PDF 由 ABBYY FineReader 生成、含文本层）。
