# AUDIT — H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska《The sphere packing problem in dimension 24》（Ann. of Math. 185 (2017), 1017–1033 已刊版；arXiv 1603.06518）

> mineru: standard 档云端解析，导出 `Viazovska_2016_sphere_packing_dim24_mineru/`；
> 审计依据 = 二值化渲染 `audit/dim24_pNNN.png`（pngmono 150dpi）对照
> `Viazovska_2016_sphere_packing_dim24__Viazovska_2016_sphere_packing_dim24.md`。逐页审计，一页一签。
> PDF 结构：17 页（pikepdf 重打包，born-digital pdfTeX 件——文本层可用 pdftotext 逐字符对账）。

## p.001（PDF p.1 / 印刷 p.1017）
- PNG：audit/dim24_p001.png（pngmono 150dpi）
- 核对：题录（标题/五作者/Annals 185 (2017), 1017–1033 头行）✓；Abstract ✓；§1 开头
  （two [11]/three [7],[8]/eight [12]、[1],[9] expositions）✓；**Theorem 1.1** ✓；
  脚注两条（Miller NSF DMS-1500562 + CNS-1526333；© 2017 authors）✓
- 结果：**PASS±**（±：①页眉 DOI 行与页码 1017 未收；②arXiv 侧栏戳
  "arXiv:1603.06518v4 [math.NT] 6 Sep 2026" 未收——戳记惯例）
- 备注：本 PDF 为已刊 Annals 版（arXiv 1603.06518 的 v4 排版），born-digital，文本层完整。

## p.002（PDF p.2 / 印刷 p.1018）
- PNG：audit/dim24_p002.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：π¹²/12! = 0.0019295743… ✓；格/周期堆积定义（[5, p. 140] R¹⁰ 例）✓；
  **Theorem 1.2 (Cohn and Elkies [2])**：——**原刊即印 "Let f : ℝⁿ → ℝⁿ"**（数学上应预期
  →ℝ；PNG+文本层双证）——md 忠实 ✓；(n/2)!(r/2)ⁿ ✓；Fourier 归一化与径向约定 ✓；
  "Optimizing the bound from **Theorem 1.1**"——原刊即印 1.1（应预期 1.2；源级笔误）——md 忠实 ✓
- 结果：**PASS±**（±：页眉 "1018 COHN, KUMAR, MILLER, RADCHENKO, and VIAZOVSKA" 与页码未收）
- 备注：Theorem 1.2 定义域/陪域与交叉引用号两处系原刊排印，对照 arXiv 版可进一步查证（本研究不代改）。

## p.003（PDF p.3 / 印刷 p.1019）
- PNG：audit/dim24_p003.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：r=2 双根条件（√(2k), k=2,3,…）✓；[2] §8 唯一性论证 ✓；Cohn-Miller [4] 猜想、
  quasimodular 路线（weight −8 depth 2 / weight −10 Γ(2)）✓；**§2 +1 eigenfunction** ✓；
  **(2.1) φ 定义**：25E₄⁴−49E₆²E₄+48E₆E₄²E₂+(−49E₄³+25E₆²)E₂²）/Δ²，q-展开
  −3657830400q−314573414400q²−13716864000000q³+O(q⁴)——数字逐位吻合 ✓；E_k 定义 ✓；
  Δ = (E₄³−E₆²)/1728 = q−24q²+252q³+O(q⁴) ✓；Δ 无零点句 ✓
- 结果：**PASS±**（±：①页眉/页码 1019 未收；②"k = 2,3,…,."处 md 多一逗号（原刊为省略号+句点）
  ——单字符排版级）

## p.004（PDF p.4 / 印刷 p.1020）
- PNG：audit/dim24_p004.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：weight −8 depth 2 句 ✓；z^{-2}E₂(−1/z)=E₂(z)−6i/(πz) ✓；**(2.2)** ✓；
  φ₁/φ₂ 定义与 q-展开（725760/113218560/19691320320；864/2218752/223140096/23368117248）
  ——数字逐位吻合 ✓；**(2.3)** φ(i/t)=O(t^{−10}e^{4πt}) ✓；**(2.4)** ✓；**(2.5)** a(r) 定义 ✓；
  Lemma 2.1 ✓；Proof 开头（[12]、different weight、−4sin² 分解式）✓
- 结果：**FAIL（单点）**：md 行 "(2.3) … as $t\ \infty,$"——**丢失 → 箭头**（原刊/文本层
  "as t → ∞"）。修复建议：补 \to。（注：md 行 125/309 "neighborhood $o f\ \mathbb{R}$" 的
  "o f" 分字与行 127 "diferent" ff→f 为排版级伪影。）

## p.005（PDF p.5 / 印刷 p.1021）
- PNG：audit/dim24_p005.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：围道分解（∫_{-1}^{i∞−1} − 2∫_0^{i∞} + ∫_1^{i∞+1} 拆为六段）✓ md 结构逐项吻合；
  拟模性组合 = 2φ(z)（(z+1)²/…/φ₂ 三行展开）✓；**(2.6)** ✓；Proposition 1 [12] Schwartz 估计 ✓
- 结果：**PASS±**（±：页眉/页码 1021 未收；"sufices" ff→f 伪影）

## p.006（PDF p.6 / 印刷 p.1022）
- PNG：audit/dim24_p006.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：Fourier 交换（e^{πir²z}→z^{−12}e^{πir²(−1/z)}）与 b̂a 展示 ✓；w=−1/z 替换展示 ✓；
  â=a 证明收尾 □ ✓；**(2.7)** ✓；**(2.8)** ✓；**(2.9)** ✓；
  p(t)（−864/π²、725760/π、−2218752/π²、113218560/π、−223140096/π²）✓；
  p̃(r) 五项（π³(r²−4)/(r²−2)²/(r²−2)/r⁴/r² 分母）✓——数字逐位吻合；**(2.10)** ✓
- 结果：**PASS±**（±：页眉 "1022 COHN, KUMAR, …" 与页码未收）

## p.007（PDF p.7 / 印刷 p.1023）
- PNG：audit/dim24_p007.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：(2.10) 对所有 r 成立、a: R→iR ✓；√(2k) 二阶零点、p̃ 无极点 ✓；
  特殊值 a(0)=113218560i/π、a(√2)=725760i/π、a′(√2)=−4437504√2i/π、a(2)=0、a′(2)=−3456i/π ✓；
  Taylor a(r)=113218560i/π−223140096i/π·r²+O(r⁴) ✓；重标定 1/156、−107√2/2730、−1/32760、
  1−3587/1820·r²+O(r⁴) ✓；高阶项非有理句 ✓；Ansatz 段开头 ✓
- 结果：**PASS±**（±：①页眉/页码 1023 未收；②"for all r" 被转写为上标乱码 "$^r\cdot$"、
  "o f" 分字——排版级）

## p.008（PDF p.8 / 印刷 p.1024）
- PNG：audit/dim24_p008.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：§3 −1 eigenfunction 开头 ✓；Θ₀₀/Θ₀₁/Θ₁₀ 定义 ✓；变换律六条（|₂S/|₂T）✓；
  |ₖM 算子公式 ✓；**(3.1) ψ_I**（7Θ₀₁²⁰Θ₁₀⁸+7Θ₀₁²⁴Θ₁₀⁴+2Θ₀₁²⁸)/Δ²；q-展开
  2q^{−2}−464q^{−1}+172128−3670016q^{1/2}+47238464q−459276288q^{3/2}+O(q²)）——数字逐位吻合 ✓；
  weight −10 for Γ(2) 句 ✓；ψ_S 开头 ✓
- 结果：**FAIL（单点）**：S/T 矩阵转写结构乱码——md 作
  "S = {\binom{0}{1}}\quad{\overset{}{0}}\end{array}−1…"（binom 嵌套破碎）；文本层证实原刊为
  **S = (0 −1; 1 0)，T = (1 1; 0 1)**。修复建议：按原文重建两矩阵。

## p.009（PDF p.9 / 印刷 p.1025）
- PNG：audit/dim24_p009.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：**(3.3)** ψ_I(it)=O(e^{4πt})（t→∞ 箭头在 ✓）/**(3.4)** O(t¹⁰e^{−π/t})（t→0 ✓）；
  b(r) 定义 ✓；**Lemma 3.1** ✓；Proof（Proposition 6 [12]、−4sin² 分解 e^{−πir²}−2+e^{πir²}、
  围道移位四行、ψ_I(z±1)=ψ_T、i∞±1→i∞ 端点移位论证、ψ_T−ψ_I=−ψ_S）✓；
  解析延拓到 r≤2 + Schwartz 收尾 ✓
- 结果：**FAIL（单字符）**：md 行 "for $r > 2$2" 末尾多一孤立 "2"（原刊为 "for r > 2,"；
  Perelman "4" 同类 mineru 幻觉）。修复建议：删尾部 "2"。
- 备注：± 页眉 "THE SPHERE PACKING PROBLEM IN DIMENSION 24 1025" 未收。

## p.010（PDF p.10 / 印刷 p.1026）
- PNG：audit/dim24_p010.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：b̂=−b 论证（Proposition 5 [12]、四项积分、w=−1/z、ψ_I|S=ψ_S/ψ_S|S=ψ_I/ψ_T|S=−ψ_T
  三方程）✓；**(3.5)** ✓；ψ_I(it) 展开（2e^{4πt}−464e^{2πt}+172128+O(e^{−πt})）✓；
  积分 2/(π(r²−4))−464/(π(r²−2))+172128/(πr²) ✓；b 的特殊值（b(0)=b(√2)=b(2)=0、
  b′(√2)=928iπ√2、b′(2)=−8πi）✓
- 结果：**PASS±**（±：页眉 "1026 COHN, KUMAR, …" 未收）

## p.011（PDF p.11 / 印刷 p.1027）
- PNG：audit/dim24_p011.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：b(r)=−172128πir²+O(r⁴) Taylor ✓；Ansatz 段（weight 14 Γ(2)、八维空间
  Θ₀₁^{4i}Θ₁₀^{28−4i}、三维子空间）✓；§4 开头、f(r)=−πi/113218560·a(r)−i/(262080π)·b(r) ✓；
  Taylor 系数 −14347/5460 与 −205/156 ✓；根与特殊值（f′(2)=−1/16380、1/156、−146√2/4095、
  −5√2/117）✓；(2.7)+(3.5)⇒f(r) 组合式 ✓
- 结果：**FAIL（单字符）**：md 行 397 "$\psi_I .$**9** the asymptotic"——多一孤立 "9"
  （文本层无；mineru 幻觉，Perelman "4" 同类）。修复建议：删 "9"。
- 备注：± 页眉/页码 1027 未收。

## p.012（PDF p.12 / 印刷 p.1028）
- PNG：audit/dim24_p012.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：A(t) 两表达式（π/28304640·t¹⁰φ(i/t)−1/(65520π)ψ_I(it) 等）✓；**(4.1)** ✓；
  ψ_S 显示式 ✓；φ(it)≤0 归约与 Lemma A.1 预告 ✓；**(4.2)**/**(4.3)** B(t) ✓；**(4.4)** ✓；
  "(4.2) holds for r>√2"（√2 根号 md 正确保留）✓；B(t) 渐近与 e^{4πt} 相消论证 ✓
- 结果：**PASS±**（±：页眉 "1028 COHN, KUMAR, …" 未收）

## p.013（PDF p.13 / 印刷 p.1029）
- PNG：audit/dim24_p013.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：B(t)=1/39·te^{2πt}−10/(117π)e^{2πt}+O(t) ✓；[1,∞) 减法项积分
  =(10−3π)(2−r²)+3)/117π²(r²−2)²·e^{−π(r²−2)} ✓；(4.5) ✓；Theorem 1.1 证明完成 ✓；
  Appendix A 开头（Sturm 定理路线、ancillary file appendix.txt、PARI/GP [10]、arXiv 1603.06518）✓
- 结果：**PASS±**（±：页眉/页码 1029 未收；"inequalit" 类 ff→f 伪影若干）

## p.014（PDF p.14 / 印刷 p.1030）
- PNG：audit/dim24_p014.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：Sturm/截断策略段 ✓；系数界（E₂: 24(n+1)²、E₄: 240(n+1)⁴、E₆: 504(n+1)⁶、
  Θ⁴: 24(n+1)²）✓；乘法界 (n+1)^{ℓ+m+1} ✓；φΔ²/ψ_IΔ²/ψ_SΔ² 与 t≥1/t≤1 分情形 ✓；
  **Lemma A.1** 陈述与 t≥1 证明（1/535、513200655360(n+1)²⁰、Σ_{n=50}^∞<10^{−50}、
  σ+10^{−50}q⁶ 在 (0,1/535) 不变号）✓ 数字逐位吻合
- 结果：**FAIL（脚注区）**：脚注 1 的 md 转写碎片化且缺损——①"Both Θ⁴₀₀ **and have**
  nonnegative coefficients"（丢 Θ⁴₁₀）；②"in the variable **from which**"（丢 q^{1/2},）；
  ③出现乱码重复 "Θ⁴₀₁=Θ⁴₀₀−Θ⁴₁₀**.Θ01 = Θ00 − Θ40**"。文本层全文：
  "¹Both Θ⁴₀₀ and Θ⁴₁₀ have nonnegative coefficients, and their sum is the theta series of the
  D₄ root lattice in the variable q^{1/2}, from which one can bound their coefficients.
  Furthermore, Θ⁴₀₁ = Θ⁴₀₀ − Θ⁴₁₀." 修复建议：以文本层重建脚注 1。
- 备注：± 页眉 "1030 COHN, KUMAR, …" 未收。

## p.015（PDF p.15 / 印刷 p.1031）
- PNG：audit/dim24_p015.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：A.1 证明收尾（q→0 极限负、(2.8) 转换、π 有理界 ⌊10¹⁰π⌋/10¹⁰、1≤t≤1/(23q^{1/2})、
  te^{−πt}≤e^{−π}≤1/23、(0,e^{−π}) 与 (0,1/23) Sturm）✓；分数幂必要性注 ✓；
  **Lemma A.2** 陈述与 t≥1 证明开头（φ−432ψ_S/π²)Δ² 截断）✓
- 结果：**PASS±**（±：页眉/页码 1031 未收）

## p.016（PDF p.16 / 印刷 p.1032）
- PNG：audit/dim24_p016.png（pngmono 150dpi）；文本层 pdftotext 逐字符对账
- 核对：A.2 证明收尾（q^{1/2} 多项式、(2.2)/(3.2) 归约、10^{−50}q⁶）✓；"not optimized"
  方法注 ✓；**Lemma A.3** + 证明（Δ² 清分母、Sturm）✓；**References [1]-[5]** 逐条
  （Notices 64 (2017), 102-115/arXiv 1611.01685；Ann. 157 (2003), 689-714；Ann. 170 (2009),
  1003-1050；preprint arXiv 1603.04759；Conway-Sloane Grundl. 290）——刊名/卷页/编号逐条吻合 ✓
- 结果：**PASS±**（±：页眉 "1032 COHN, KUMAR, …" 未收）
