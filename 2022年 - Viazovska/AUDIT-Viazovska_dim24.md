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
