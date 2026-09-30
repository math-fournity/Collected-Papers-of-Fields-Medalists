# AUDIT — Gil Kalai《The Work of June Huh》（IMU laudatio/ICM 2022 会议论文完整版，MiKTeX pdfTeX born-digital，16p）

> mineru: standard 档云端解析；审计依据 = `audit/laudatio_huh_pNNN.png`（pngmono 150dpi 全 16 页）
> + pdftotext 文本层逐字符对账（可靠）。**伪影族**：U+FFFD/丢数学斜体变量 **86 处**（全篇 G/M/n/X/
> d/k/j/H/F/Y/K/ψ/g/f/i）、缺空格/缺字母（ofthe/ofa/ofmy/can b/Franci/associat/tha/variet/
> combinatoria/uni modality/deletioncontraction 等 ~18 处）、stray paren ×3、标题+§4/§4.1 节标题
> 粘并 ×2、ff→f 连字（coeficients/diferent/Birkhof/afinely/Jef/Geof——登记不改）。

## p.001（题录页）
- 核对：题名两行（"The Work of June Huh" / "Gil Kalai"，**md 粘并为一行 → FAIL**）/Abstract
  （Fields Medal citation 全文五项成果）/MSC 05E14; 52C35, 05B35, 05C31, 14T15, 52B40/
  Keywords ✓；ICM 2022 footer（DOI 10.4171/ICM2022/2/11）页眉未收（惯例）
- 结果：**FAIL（单点）**：标题粘并。
## p.002（引言 + D–W/Mason 概览）
- 核对：HRW 猜想 [32,56,64]/Read 特例/Huh [33] 2009/Huh–Katz [36] 2010/AHK [1] 2015 ✓；
  配置 𝒫：**n 点/d 维空间/dimension i**（md U+FFFD×3 → FAIL）；(of rank d)/size k（FFFD×2）；
  Motzkin 1936/1951 [50]/de Bruijn–Erdős 1948 ✓；式(1) wᵢ≤w_{d−i}, i≤[d/2] ✓；Lenz [43]/
  Huh–Schröter–Wang [38] ✓；"Mathias Lenz"——print 即此拼写（ref[43] 为 Matthias，源级不一致，
  忠实）；Mihail–Vazirani/AOGV [4]/Brändén–Huh [13] ✓
- 结果：**FAIL（FFFD×5）**
## p.003（§1 四色/色多项式）
- 核对：§1/§1.1 标题 ✓；Theorem 1（Appel–Haken 1976）——md "can b properly"→be（**FAIL**）；
  **Francis** Guthrie（md "Franci" → **FAIL**）；Birkhoff/Whitney/Tutte/deletion-contraction
  （md "deletioncontraction" 丢连字符 → **FAIL**）；式(2) χ_G+χ_{G/e}=χ_{G\e} ✓；minor 句 H/G/G
  （FFFD×3）+orientations of G（FFFD×1）→ **FAIL**；Stanley [59] 传递定向 ✓
- 结果：**FAIL（多点）**
## p.004（§1.2 Read 猜想 + §2.1 开头）
- 核对：Heron/Read 猜想/式(4) log-concave ✓；Theorem 2 χ_G(x)（print 斜体 x；md \boldsymbol{x}
  → **FAIL 记号**）+of every graph G（FFFD）；survey [15,16,62]/polytopes [11]/Young lattices [63] ✓；
  Matoušek [46] annus mirabilis 引文（md "ofmy"×2 缺空格 → **FAIL**）；§2/§2.1 标题 ✓；
  X={x₁,…,xₙ}/"We can associate with X"（md "associat"+FFFD → **FAIL**）
- 结果：**FAIL（多点）**
## p.005（§2.1 matroid 公理 + §2.2 图→拟阵）
- 核对：五要素 bullets（**X/Y FFFD×8 → FAIL**）；(1)(2) 公理（print 末位正体 "subsets of Y"——
  源级混排，忠实）；K*={S⊂X: X\S⊄M} ✓；§2.2：**G/n/n/F**（FFFD×4 → FAIL）；**subgraph H/is n/
  components of H**（FFFD×3 → FAIL）
- 结果：**FAIL（FFFD 11 处）**
## p.006（Figure 1 + §2.3 特征多项式）
- 核对：Figure 1（page_5_image_0 ✓ 拟阵类包含图）+ 图注（Geoff Whittle——md "Geof" ff 登记不改；
  "proved **that** matroids"——md "tha" → **FAIL**）✓；§2.3 标题/(i)(ii)(iii) ✓；"characteristic
  function"——print 即此（源级，忠实）；式(5) ✓；Theorem 3（AHK [1]）——md "ofthe
  characteristicpolynomial ofa"缺空格+FFFD(M) → **FAIL**
- 结果：**FAIL（两点）**
## p.007（Huh–Katz/AHK 论证 + §3 定理 4）
- 核对：Milnor 数/wonderful compactification [21]/Khovanskii–Teissier ✓；[1] 引文块：Chow ring
  of M×2/[matroid] M（**FFFD×3 → FAIL**）、**toric variety**（md "variet" → **FAIL**）、A*(M)_ℝ/
  X(Σ_M) ✓；§3/§3.1 标题（de Bruĳn ĳ 连字 print 即此）✓；Theorem 4 + Gallai–Sylvester 归纳证明 ✓；
  Ryser [54] ✓
- 结果：**FAIL（FFFD×4）**
## p.008（Figure 2 + Ryser 证明 + Motzkin/式(6)）
- 核对：Figure 2（page_7_image_0 ✓ Fano/Vámos/non-Pappus）+ 图注：**field F/characteristic of F**
  （FFFD×2 → **FAIL**；"if and only the characteristic"——print 即此源级，忠实）✓；Ryser：
  b_i=<c_i,c_i>/"**i**th line (b_i>1)."（md "�th"+**多余 ")"** → **FAIL**）；Σαᵢcᵢ=0/
  0=<Σ,Σ>=Σαᵢ²(bᵢ−1)+(Σαᵢ)² ✓；"there is bĳection ψ(p)"——print 即缺 a（源级，忠实）；
  Motzkin：**n/d/n**（FFFD×3 → **FAIL**）；"describe a matroid"——print 即此（源级，忠实）；式(6) ✓
- 结果：**FAIL（FFFD×5+stray paren）**
## p.009（§3.2 Theorem 5 + §4/§4.1 开头）
- 核对：Theorem 5（BHMW 2020 [12]）：**M/k-flats of M/k,j**（FFFD×5 → **FAIL**）、
  **rank(M)**（md "r a n k" 斜体分写 → **FAIL 记号**）；(1)(2)+ψ（FFFD）；(3) ℚℒᵏ(M)→ℒʲ(M)
  （print 即 ℚ 仅在源侧——忠实；md **多余 ")"** → **FAIL**）；w₁,…,wₙ（print 即 n，忠实）/
  式(7)/Mason 加强式 (3/2)·(w₁−1)/(w₁−2)·w₁w₃ ✓；Seymour [57] ✓；**§4 与 §4.1 双标题粘并**
  → **FAIL**；ICERM 引言 ✓
- 结果：**FAIL（多点）**
## p.010（三大思想 + §4.2 PD/HL/HR）
- 核对：Sturmfels 热带/Stanley 极化 Hodge/McMullen flip 连通性 ✓；**g-theorem/g-conjecture**
  （FFFD×2 → **FAIL**；print 斜体 𝑔）；"Fleischer and Yuzvinsky"/"Tessier"——print 即此拼写
  （p.7 为 Feichtner/Teissier，源级不一致，忠实）；§4.2 标题 ✓；(PD)/(HL)/(HR) 引入后正文两处用
  "(HD)"——print 即此（源级不一致，忠实）；φₖ: Aₖ→Aₖ+1 ✓
- 结果：**FAIL（FFFD×2）**
## p.011（标准猜想五例 + Remarks + §5.1 开头）
- 核对：五例清单/Grothendieck [31]/Soergel/Elias–Williamson [23] ✓；**"Kazhdan–Lusztig"**
  （md "– Lusztig" 断行丢连 → **FAIL**）；Remarks 1) Hall-Laman/anisotropy [53]/AHK-P-P [3]/
  Karu–Xiao [42] ✓；2) "Lefshetz"——print 即此缺 t（源级，忠实）、(HL)(HR) ✓；§5/§5.1 标题 ✓；
  **M/n/M/k**（FFFD×4 → **FAIL**）；**stray ")"** after i_k(M)（print 无 → **FAIL**）；
  三个 Mason 强度式 ✓
- 结果：**FAIL（FFFD×4+stray paren+断行连字）**
## p.012（strong/ultra-strong + §5.2 + Conclusion 开头）
- 核对：strong (1+1/k)/ultra-strong (1+1/k)(1+1/(n−k)) ✓；"Mathias Lenz showed [43]"（源级 ✓）；
  **"unimodality"**（md "uni modality" → **FAIL**）；§5.2：**M/X/Y**（FFFD×3 → **FAIL**）；
  min(|Y||, Ȳ|)——print 即此乱式（源级，忠实）；"edges between Y to its complement"——print 即此
  （源级）；**M**/ℝᵈ/**"discrete n-dimensional discrete cube"**（print 即 n 且 discrete×2——源级；
  FFFD → **FAIL**）；Feder–Mihail [24]/AOGV [4] ✓；Conclusion ✓
- 结果：**FAIL（FFFD×4）**
## p.013（Funding + References [1]-[13]）
- 核对：Funding ERC 834735/ISF 2669/21 ✓；**[1] "combinatorial geometries"**（md
  "combinatoria" → **FAIL**）/Ann. 188 (2018) 381–452 ✓；[2][3] arXiv ✓；[4] Duke 170 (2021)
  3459–3504 ✓（"polyno mials" 断行族登记）；[5]-[13] 抽验 ✓（[6] JCTB 96/38–49、[8] Contemp.
  Math. 98、[9] Tohoku 57/273–292、[10] suficiency——ff 登记、[12] arXiv:2010.06088）
- 结果：**FAIL（单点）**
## p.014（References [14]-[32]）
- 核对：[14]-[17] ✓（[16] Jerusalem Combinatorics '93/Contemp. Math. 178）；[18] Birkhoff
  （md "Birkhof" ff 登记不改）/Ann. 14 (1912) 42–46 ✓；[19][20] arXiv ✓；**[21] "459–494.
  36–70."——print 即此冗尾（源级，忠实）**✓；[22] PAMS 47/504–512 ✓；[23] Ann. 180/1089–1136 ✓；
  [24][25] ✓；[26][27] ✓；[28] Notices 61/736–743（Geoff——ff 登记）✓；[29]-[31] ✓；
  **[32] 双括号 "…Institute), Oxford, 1972)"——print 即此（源级，忠实）**✓
- 结果：**PASS±**（±：ff/断行家族登记）
## p.015（References [33]-[51]）
- 核对：[33] JAMS 25 (2012) 907–927 ✓；[34] ICM 2018 Vol. IV 3093–3111 ✓；[35] CDM 2016
  1–46 ✓；[36] Math. Ann. 354/1103–1116 ✓；[37] Acta 218/297–317 ✓；[38] JEMS 24/1335–1351 ✓；
  [39] Jeff（ff 登记）✓；[40] Salaün ✓；[41] Invent. 157/419–447 ✓；[42] arXiv:2204.07758 ✓；
  **[43] "Matthias Lenz, The f-vector"（FFFD(f) → FAIL；正文 "Mathias" 系源级不一致）**✓；
  [44][45] ✓；[46] EuroCG'11 ✓；[47]-[49] McMullen ✓；[50] TAMS 70/451–464 ✓；[51] Okounkov ✓
- 结果：**FAIL（单点）**
## p.016（References [52]-[66] + 作者块）
- 核对：[52]-[66] 抽验 10 条 ✓（[54] de Bruĳn ĳ print 即此、[56] "Congress International des
  Mathématicians (Nice ,1970)"——print 即此源级、[61] ICM 1983 Warsaw 447–453、[64][65] Welsh、
  [66] Whitney 57/509–533）；作者块 Gil Kalai/HUJ+Reichman/**kalai@math.huji.ac.il**
  （md "ac.i" 丢 l → **FAIL**）
- 结果：**FAIL（单点）**

## 总评

- **覆盖声明**：16/16 页逐页目检（150dpi 全页）+ 文本层逐字符对账（可靠 born-digital）。
  mineru：standard 档。
- **FAIL 修复（四大类）**：①**U+FFFD/丢数学斜体变量 86 处**全部按文本层恢复（G/M/n/X/d/k/j/
  H/F/Y/K/ψ/g/f/i）；②缺空格/缺字母 ~18 处（ofthe/ofa/ofmy/ofthis/then,for/uni modality/can b/
  Franci/associat/tha/variet/combinatoria/deletioncontraction/Kazhdan– Lusztig 等）；③stray
  paren ×3 + 标题/§4 双节标题粘并 ×2 + \boldsymbol{x}→x + "r a n k"→\mathrm{rank} 记号归位；
  ④邮箱 ac.i→ac.il。
- **源级 typo 清单（忠实不改）**：Mathias Lenz（正文×2）vs Matthias Lenz（ref[43]）；(HL) vs (HD)
  混用；"characteristic function"（式(5) 前）；"describe a matroid"；"if and only the
  characteristic"；"there is bĳection"（缺 a）；"edges between Y to its complement"；
  "bases of the matroids"；"a hard Lefshetz theorem"；Fleischer/Tessier（p.10）vs
  Feichtner/Teissier（p.7）；"discrete n-dimensional discrete cube"（n 且 discrete×2）；
  min(|Y||, Ȳ|) 乱式；ref[21] "459–494. 36–70."；ref[32] 双括号；ref[56] "Congress
  International des Mathématicians (Nice ,1970)"；de Bruĳn/bĳection ĳ 连字；ff→f 连字族
  （coeficients/ofthe 系空格另修/diferent/Birkhof/afinely/Geof/Jef/suficiency）。
- **可用性结论**：修复后 md 可作该 laudatio 忠实底本。参考文献 66 条抽验 24 条全对
  （除上述源级 quirk）。
