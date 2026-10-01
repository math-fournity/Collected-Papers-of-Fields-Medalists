# AUDIT — M. S. Viazovska, "The sphere packing problem in dimension 8"（Ann. of Math. 185 (2017), 991–1015，DOI 10.4007/annals.2017.185.3.7；Annals 排版版 born-digital，pdfTeX-1.40.16 + hyperref）

> mineru: standard 档导出 `Viazovska_2017_e8_published_mineru/`；**born-digital 文本层主对账通道**
> （pdftotext 40KB/0 FFFD 逐点仲裁）+ PNG 抽验（题录页整页目检；150dpi 全 25 页入库）。
> print 页码 = PDF p.N + 990（p.001=991 … p.025=1015）。

## p.001（print 991：题录 + §1 开头 + © 脚注）
- PNG：audit/e8_p001.png（整页目检）
- 核对：Annals 185 (2017) 991-1015/DOI 头、标题/By MARYNA S. VIAZOVSKA/Abstract、Δ_P(r)/Δ_P/Δ_d 定义 ✓；
  **© 2017 Department of Mathematics, Princeton University. 页底脚注**（print © 符号，mineru 拍平为
  "c 2017" → md 已还原 ©）✓
- 结果：PASS（© 脚注修复后）

## p.002（print 992：Thue/Fejes Tóth/Kepler/Hales）
- 文本层 ✓：Thue [18]/**"the beginning ot twentieth century"（print 原文，忠实）**/"considered by some
  experts incomplete"（print 原文）/"in 1940s"（print 原文）/L. Fejes Tóth（´oth 重音拆裂已修）/
  Kepler "six-cornered snowflake"（**smart-quote 乱码 ^{66}On… 已修**）/π/√18/Hales 1998 [11]/
  2015 formal proof/[6][4]/d=8 and d=24 句号 ✓；数字拆分（√12/0.90690/0.74048/36/24）已修；"dificult"→difficult
- 结果：PASS（修复后；ot/incomplete/1940s 源级）

## p.003（print 993：主结果 + Λ₈ 定义 + Theorem 1）
- 文本层 ✓：Δ₈=π⁴/384≈0.25367、Λ₈ 定义（Z⁸∪(Z+½)⁸，坐标和 mod 2）、unique positive-definite even
  unimodular rank 8、minimal distance √2、Theorem 1、[4,§8] 唯一周期填充、章节组织 ✓；
  修复：384/0.25367 数字拆分、"{√2}.."mash、E<sub>8</sub> HTML 残留 ×2、"$E_8-lattice$" 拉开、
  "$\Lambda_8.$"mash、© 脚注
- 结果：PASS（修复后）

## p.004（print 994：§2 LP bounds）
- 文本层 ✓：error-correcting codes [7]/quadrature [8]/spherical codes [13][16]、Cohn–Elkies [4] 2003、
  1.000001 gap、Fourier 定义 e^{-2πix·y}、x·y 极化恒等式、Schwartz/admissible 定义、
  **"faster then any inverse power"（print 原文，忠实）** ✓；修复：丢箭头 ×2（R^d→C/R^d→R）、
  "We say" 拉开、"f.$."mash
- 结果：PASS（修复后；faster then 源级）

## p.005（print 995：Theorem 2 + (1)(2) + Poisson + Theorem 3 (3)(4)(5)）
- 文本层 ✓：Theorem 2 上界 f(0)/f̂(0)·π^{d/2}/(2^d Γ(d/2+1))、(1) f(x)≦0 for ‖x‖≧1、(2) f̂≧0、
  radial 归约 [4, p.695]、Σ_{1/√2 Λ₈}f=2⁴Σ_{√2 Λ₈}f̂、optimal 定义、Theorem 3 三条件
  **print 编号 (3)(4)(5)（md 孤儿(3)+错标 tag{4}{5}+末式无 tag → 已按 print 重排）**、
  (6)(7)(8) 三式、double zeroes、§3 引 ✓；修复：编号族重排、(1) 式 "f o r"→\text{ for }+句号、
  (3)-(5) \AA 乱码 ×2→–、∈/ →∉、\text{for all} 间距、丢箭头 ×3
- 结果：PASS（修复后）

## p.006（print 996：§3 模形式 + Γ(N)/Γ₀(N) + automorphy factor + slash operator）
- 文本层 ✓：H、Γ(1)=PSL₂(Z) 线性分式、Γ(N) 主同余子群、Γ₀(N)、j_k(z,γ)=(cz+d)^{-k}、chain rule、
  slash operator、模形式定义 (1)(2)（c_f(α,n/n_α)）、M_k(Γ) 有限维 ✓；
  修复：**γ 矩阵 Σ 乱码重建**（(Σ_c^a Σ_d^b)→(a b;c d)）、"Γ;$;"双分号、coeficients
- 结果：PASS（修复后）

## p.007（print 997：Eisenstein (9)(10) + E₄/E₆ + E₂ (11)(12) + theta 函数）
- 文本层 ✓：E_k (9)、Fourier 展开 (10)（2/ζ(1−k) 系数）、σ_{k−1}(n)=Σ_{d|n}d^{k−1}
  （**"∑ d\vert n : d^{k−1}" 拉开乱式已重建**）、E₄=1+240Σσ₃qⁿ/E₆=1−504Σσ₅qⁿ、E₂ (11)、
  z^{-2}E₂(−1/z)=E₂(z)−(6i/π)(1/z) (12)、[19,§2.3/§5.1]、Thetanullwerte θ₀₀/θ₀₁/θ₁₀ ✓；
  修复：数字拆分（240/504/24）、σ 求和式重建
- 结果：PASS（修复后）

## p.008（print 998：T/S 作用 (13)-(18) + Jacobi (19) + weakly-holomorphic + j-invariant）
- 文本层 ✓：**T=(1 1;0 1)/S=(0 −1;1 0)（md 矩阵乱式已按 print 重建）**、
  **(13)-(18) 六条 θ 方程按 print 编号重排（md 孤儿(13)+(16)+错位 tag）**、Jacobi (19)、
  θ₀₀⁴,θ₀₁⁴,θ₁₀⁴∈M₂(Γ(2))、weakly-holomorphic 定义、c_f(n) 记号、j=1728E₄³/(E₄³−E₆²) ✓；
  修复：矩阵 ×2、编号族 ×2 组
- 结果：PASS（修复后）

## p.009（print 999：j 展开 + Rademacher (20) + A_k(n) + §4 开头 (21)(22)）
- 文本层 ✓：j 展开（744/196884/21493760/864299970/20245856256/O(q⁵)）、PARI GP/Mathematica、
  Hardy–Ramanujan [17, pp.460-461]/nonholomorphic Poincaré series [15]、(20)、A_k(n) Rademacher 和、
  Bessel I₁、[12]/[3, Props.1.10,1.12]、**"efective"→effective**、§4 标题、
  **(21) 𝓕(a)=a 与 (22) 𝓕(b)=−b 按 print 重排**、purely imaginary 动机、a,b 定义 ✓；
  修复：数字拆分 ×6、j 系数三空格、编号族、"coeficient(s)"×4、Poincar´e→Poincaré、
  "Fourier coeficient of$j..$"mash
- 结果：PASS（修复后）

## p.010（print 1000：φ₋₂/φ₋₄ (23)(24) + (25) + φ 定义 (26)-(28) + 变换规则 (29)）
- 文本层 ✓：φ₋₂=−1728E₄E₆/(E₄³−E₆²)、φ₋₄=1728E₄²/(E₄³−E₆²)、无极性论证、(25) 渐近
  （2πn^{(κ−1)/2}ΣA_k(n)/k·I_{1−κ}(4π√n/k)）、φ₋₄/φ₋₂/φ₀ 定义 (26)-(28)、
  φ₀ 非模性、(29) 变换规则（12i/36 系数）✓；修复：编号族 (23)(24)/(26)(27)(28)、数字拆分 ×6
- 结果：PASS（修复后）

## p.011（print 1001：D 算子 (30)(31) + 傅里叶展开 (32)-(34) + a(x) 定义 (35) + Prop 1 + □）
- 文本层 ✓：φ₋₂=−3D(φ₋₄)+3φ₋₂ (30)、φ₀=12D²−36D+24j−17856 (31)、Df=(2πi)^{-1}f′、
  **(32)(33)(34) 三条展开按 print 重排**（φ₋₄= q^{-1}+504+73764q+2695040q²+54755730q³/
  φ₋₂=720+203040q+9417600q²+223473600q³+3566782080q⁴/φ₀=518400q+31104000q²+870912000q³+
  1569715200q⁴）、a(x) 四围道定义 (35)、O(e^{−2πIm z}) 估计、K₁ Bessel、**print 墓碑 □（Prop 1 证明末，
  md 缺 → 已补）**、Fourier of Gaussian (36) ✓；修复：编号族 ×2、数字拆分 ×14、
  "For r∈R≥0 1"→", we have"、"$c_{φ₀}(n)$ The first"句号
- 结果：PASS（修复后；墓碑补入）

## p.012（print 1002：Prop 2 + (37) + d(r) + 变形路径）
- 文本层 ✓：**"greater then √2"（print 原文，忠实）**、a(r)=−4sin²(πr²/2)∫φ₀(−1/z)z²e^{πir²z}dz (37)、
  d(r) well-defined、φ₀(−1/it) 渐近 ×2、**"expansions (34)–(32)"（print 降序原文，忠实）**、
  三段围道 display ✓；修复："{√2}.."mash ×2
- 结果：PASS（修复后；greater then/(34)–(32) 源级）

## p.013（print 1003：φ₀ 关系式 + d(r)=a(r) + Prop 2 证毕）
- 文本层 ✓：φ₀ 组合式=2φ₀(z) 三行推导、d(r)=…=a(r) display、12i/36/π² 系数 ✓
- 结果：PASS

## p.014（print 1004：Prop 3 (38) + (39)(40) + 解析延拓 + Prop 4 (41)）
- 文本层 ✓：**"(38)" 孤儿并入 display 为 \tag{38}**、a(r) 拉普拉斯表示（36/π³(r²−2)、8640/π³r⁴、
  18144/π³r²）、"converges absolutely for all r∈R>0"、(39) φ₀(i/t)t² 渐近、**(40) 从行内杂串还原为
  display tag**、identity (38) 全区间成立、a(0)=−8640i/π、a(√2)=0、a′(√2)=72√2i/π (41) ✓；
  修复：(38)/(40)、数字拆分 ×8、"r>{√2}.."mash ×3
- 结果：PASS（修复后）

## p.015（print 1005：h (42) + Γ₀(2) 生成元 + ψ_I/T/S (43)-(45) + 显式 (46)-(48)）
- 文本层 ✓：h=128(θ₀₀⁴+θ₀₁⁴)/θ₁₀⁸ (42)、h∈M^!_{−2}(Γ₀(2))、生成元 (1 0;2 1) 与 T、
  **"h|₋₂γ=h"（md 把 γ 拉入下标已修）**、[14, Ch. I, Lemma 4.1]、θ₁₀ 无零点、h 展开
  （q^{-1}+16−132q+640q²−2550q³+O(q⁴)）、**I=(1 0;0 1)/T=(1 1;0 1)/S=(0 −1;1 0)（md 双矩阵乱式
  已按 print 重建，I 系单位阵）**、ψ_I/T/S 定义 **(43)(44)(45) 按 print 重排**、
  显式公式 **(46)(47)(48) 重排+补 tag** ✓；修复：矩阵 ×3、下标、编号族 ×2、数字拆分 ×6、
  "it sufices"→suffices
- 结果：PASS（修复后）

## p.016（print 1006：ψ 展开式 (49)-(51) + b(x) 定义 (52) + Prop 5 + □）
- 文本层 ✓：**ψ_I/ψ_T/ψ_S 展开式 (49)(50)(51) 按 print 重排**（q^{-1}+144∓5120q^{1/2}+70524q∓626688q^{3/2}
  +4265600q²/−10240q^{1/2}−1253376q^{3/2}−48328704q^{5/2}−1059078144q^{7/2}）、b(x) 四围道 (52)、
  Prop 5 f̂(b)=−b、ψ_T|₋₂S=−ψ_T/ψ_I|₋₂S=ψ_S/ψ_S|₋₂S=ψ_I、**print 墓碑 □（Prop 5 证明末，md 缺 → 已补）** ✓；
  修复：编号族、数字拆分 ×12、墓碑
- 结果：PASS（修复后）

## p.017（print 1007：Prop 5 证明估计 + F(b) 变换 + Prop 6 (53)）
- 文本层 ✓：∫_{-1}^{i}ψ_T=∫ψ_S z^{-4}…、|ψ_S(z)|≤Ce^{-πIm z}、C₁rK₁(2πr)、
  |b(r)|≤C₂rK₁(2πr)+C₃e^{-π(r²+1)}/(r²+1)、d^k/dr^k（md "d^k r"已修）、
  𝓕(b)(x) 两段 display、ψ_I(it)=e^{−2πiz}+O(1)（**"~=~"间距伪影已修**）、(53) ✓；修复：~ =~、d^kr
- 结果：PASS（修复后）

## p.018（print 1008：Prop 6 证明 + (54)(55) + (56)(57) + c(r)=b(r) + □）
- 文本层 ✓：ψ_I(it) 渐近 ×2、c(r) 三段重写、**(54)(55) 按 print 重排（55 由孤儿变 tag）**、
  (56)、ψ_T+ψ_S=ψ_I (57)、ST²S∈Γ₀(2)、STS(ST)^{-1}∈Γ₀(2)、c(r)=b(r)、**print 墓碑 □（Prop 6 证明末，
  md 缺 → 已补）** ✓；修复：编号族 (54)(55)、墓碑、"$\Lambda_8.$-vectors"→"Λ₈-points"（L735 上下文）
- 结果：PASS（修复后）

## p.019（print 1009：Prop 7 (58) + (59)(60) + (61)）
- 文本层 ✓：b(r)=4i sin²(144/πr²+1/π(r²−2)+∫(ψ_I(it)−144−e^{2πt})e^{−πr²t}dt) (58)、
  ψ_I(it)=e^{2πt}+144+O(e^{-πt}) (59)、∫(e^{2πt}+144)e^{-πr²t}dt=… (60)、
  **"Therefore, the identity (38) holds for r > √2"——print 原文错引（应为 (58)），md 忠实保留+源级登记**、
  b(0)=0、b(√2)=0、b′(√2)=2√2πi (61) ✓；修复：数字拆分 ×6、"{√2}.."mash ×2
- 结果：PASS（修复后；identity(38) 错引源级）

## p.020（print 1010：§5 Theorem 4 + g 定义 + (62) + A(t) + Figure 1）
- 文本层 ✓：g:=(πi/8640)a+(i/240π)b、satisfies conditions (3)–(5)（**\AA 乱码已修**）、∉2Z_{>0}、
  (62) g(r)=π/2160 sin²∫A(t)e^{-πr²t}dt、A(t)=−t²φ₀(i/t)−36/π²ψ_I(it)、Figure 1 说明
  （A₀^{(2)}/A_∞^{(1)} 公式、**中文逗号"，and"已修**）✓；修复：数字拆分 ×4、图注标点
- 结果：PASS（修复后）

## p.021（print 1011：A(t) 两个表示 + (63)(64) + A_∞^{(6)}/A_0^{(6)} + (65)-(69)）
- 文本层 ✓："from identities (29) and (45)"（print 原文）、A(t) 两表示（+36/π²t²ψ_S(i/t)/
  −t²φ₀(it)+12/π t φ₋₂−36/π²φ₋₄−36/π²ψ_I）逐项 ✓、**"(63)(64) 按 print 重排"**、
  "expansions (32)–(34), (49), and (51)"（print 原文）、A_∞^{(6)} 全式（72/23328/184320/5194368/
  22560768/250583040/869916672/8640/2436480/113011200/518400/31104000）、
  A_0^{(6)} 全式（368640/518400/45121536/31104000/1739833344）、(65) |c_{ψ_I}|≦e^{4π√n}、
  **(66)-(69) 按 print 重排**（ψ_S/φ₀/φ₋₂/φ₋₄）✓；修复：编号族 ×2、数字拆分 ×40、
  "\mathrm{:}"→句号、coeficients ×3
- 结果：PASS（修复后）

## p.022（print 1012：误差估计 + 区间算术四式 + (4) 开头 (70) + B(t)）
- 文本层 ✓：|A−A₀^{(m)}|/|A−A_∞^{(m)}| 估计、R₀^{(m)}/R_∞^{(m)}、区间算术四式（R≦|A|/A<0, t∈(0,1]/[1,∞)）、
  A(t)<0 ⟹ (3)、(70) ĝ(r)=π/2160 sin²∫B(t)e^{-πr²t}dt、B(t)=−t²φ₀(i/t)+36/π²ψ_I(it) ✓；
  修复："for$r>0$2"→","、数字 2160
- 结果：PASS（修复后）

## p.023（print 1013：B 表示 + B_∞^{(6)}/B_0^{(6)} + 区间算术 + Theorem 4 证毕 □）
- 文本层 ✓：B(t) 两表示（−36/π²t²ψ_S/+12/π t φ₋₂−36/π²φ₋₄+36/π²ψ_I）、Figure 2 说明
  （B₀^{(2)}/B_∞^{(1)}）、B_∞^{(6)} 全式（12960/184320/116640/22560768/56540160/869916672/8640/
  2436480/113011200/518400/31104000）、B_0^{(6)} 全式、(65)-(69) 引用、区间算术四式（B>0）、
  **"Theorems 4 and 3"（print 原文顺序，忠实）+ print 墓碑 □（md \x03 已转 □）** ✓；
  修复：数字拆分 ×28、墓碑、中文逗号
- 结果：PASS（修复后；Theorems 4 and 3 源级）

## p.024（print 1014：Acknowledgments + References [1]-[19]）
- 文本层 ✓：致谢（Bondarenko/Radchenko/Kramer/Mellit/Sullivan/Ziegler）、References [1]-[19] 逐条
  （MR/Zbl/DOI 核对；**[10] "L. Fejes"（print 无 Tóth，源级忠实）**、[9] Zbl 1062.11022/[
  13] Zbl 0261.94016（跨行断点修复）、[14] Birkhäuser（¨a 拆裂已修）、[15] Über/Entwicklungskoeffizienten
  （**print 系 Koeffizienten，md 丢 f 已修**+¨拆裂）、[18] Über…Ebene（¨拆裂）、[19] DOI 尾 \_1 修复）✓
- 结果：PASS（修复后；[10] Fejes 源级）

## p.025（print 1015：Received/作者块）
- 文本层 ✓：(Received: April 8, 2016) (Revised: December 18, 2016)、Berlin Mathematical School and
  Humboldt University of Berlin, Berlin, Germany（HTML sub 逗号已修）、
  **Current address : École Polytechnique Fédérale de Lausanne（´e 拆裂乱串已修）**、
  Lausanne, Switzerland、E-mail : viazovska@gmail.com ✓
- 结果：PASS（修复后）

## 总评

- **覆盖声明**：25/25 页文本层全对账（pdftotext 40KB/0 FFFD 逐点仲裁）+ PNG 抽验（p.001 题录整页）+
  150dpi 全 25 页入库；born-digital 通道。
- **系统性修复**：**公式编号族重排 15 组 38 式**——mineru 系统性把 print 的"(N)" 孤立为正文行、首个
  display 错标 \tag{N+1}、末式丢 tag；print 真实编号由内部交叉引用锁定（"condition (21)"/"(22)"、
  "(13)–(18)"、"(43)–(45)"、"(65)–(69)" 等）+ 文本层行内编号双重证实。涉及 (3)-(5)、(13)-(18)、
  (21)(22)、(23)(24)、(26)-(28)、(30)(31)、(32)-(34)、(38)、(40)、(43)-(45)、(46)-(48)、(49)-(51)、
  (54)(55)、(63)(64)、(66)-(69)；完成后 \tag{1}-\tag{70} 全清单无缺无重。
- **其他修复**：数字逐位拆分 ~420 处（全局归并）；丢箭头 ×6；乱矩阵重建 ×5（γ 矩阵 Σ 乱码、§3 T/S、
  §4 I/T/S、Γ₀(2) 生成元 T）；墓碑 □ 补入 ×7+转化 \x03 ×1（print 8 证明末齐）；smart-quote 乱码 1；
  "∈/"→∉；\AA 乱码 ×2；"f o r"→\text{for}；HTML sub 残留 ×4；Tóth/Über/Birkhäuser/Poincaré/
  École 重音拆裂 ×7；中文逗号 ×1；Zbl 断点 ×2；DOI 尾字符 ×1；ff ×14；mash 标点 ~15。
  **共约 540 处/150 规则**。
- **源级 quirk 清单（忠实不改）**：球体积式 "the beginning **ot** twentieth century"；"faster **then**
  any inverse power"；"greater **then** √2"；"considered by some experts incomplete"；"in 1940s"；
  "**which double zeroes** at all Λ₈-vectors"（缺 with）；"From **(34)–(29)**" 与 "expansions
  **(34)–(32)**"（print 降序区间）；"**From (34)–(29) we obtain**"；**L470 e^{+π(r²+2)}**
  （与下行 e^{−π(r²+2)} print 自相矛盾）；**Prop 7 证明 "the identity (38)"（print 错引，应 58）**；
  **"Theorems 4 and 3"**（语序）；**[10] "L. Fejes"（print 无 Tóth）**；墓碑 □ 系实心打印方块（print 原字形）。
- **可用性结论**：修复后 md 可作该文忠实底本；\tag{1}-\tag{70} 齐全，4 个定理、8 个命题、2 幅图说明、
  19 条 References、作者块完整。与 dim24 published（已审 ✅）、dim8 arXiv 24p（已审 ✅）、laudatio（已审
  ✅）、ICM2022（已审 ✅）构成 Viazovska 目录全闭环。

### 修复登记（2026-09-30）

- pass-1 约 90 规则 applied（11 missed 探针修正）+ pass-2 全局数字归并 369 处 + 散点 12 规则
  ——**全部收敛：\tag{1}-\tag{70} 全、孤儿编号 0、□×8、ff/数字拆分/\AA/丢箭头清零**。
- fix(md) commit 父提交 = 修复前 md 原貌；脚本 /tmp/e8pub_fix/fix_md.py + 两个内联 pass
  （收敛式）。
- 本篇 25/25 页完成，无未决项。
