# AUDIT — Allyn Jackson《The Work of Akshay Venkatesh》（ICM 2018 会议报告，pdfTeX born-digital，5p）

> mineru: standard 档云端解析；审计依据 = `audit/icm18_venkatesh_pNNN.png`（pngmono 150dpi）+
> pdftotext 文本层逐字符对账。

## p.001
- 核对：题录 ✓；数论地位段（bedrock/analysis-algebra-combinatorics-geometry）✓；
  Venkatesh 特质段（black boxes/unexpected connections）✓；三例预告 ✓；二次型开篇
  （x²+xy+7y²+yz+12z²/quadratic form 定义/x² 与 w²+x²+y²+z²/Lagrange 1770）✓
- 结果：**PASS±**（±：页眉未收）

## p.002
- 核对：Gauss Disquisitiones 1801/P represents Q（m≥n）/Hilbert 第 11 问题/Hsia-Kitaoka-Kneser
  1978（m≥2n+3）✓；2008 Ellenberg-Venkatesh **m≥n+5**——原刊句末有句号（文本层证实），
  **md 丢句号 → FAIL**；lattices/Minkowski 几何数/dynamics ✓
- 结果：**FAIL（单点）**：补 "m ≥ n + 5." 句号。

## p.003
- 核对：Ratner 定理（early 1990s）及其变体应用 ✓；subconvexity（2005 preprint/2010 published/
  Michel）✓；unique factorization/ring R={a+b√−5}/9 的两种分解 ✓；class number/Cohen-Lenstra
  1984 heuristics（1/3 vs 43%）✓；2016 Ellenberg-Westerland function fields ✓
- 结果：**FAIL（单点）**："Her theorem **pre-dicts**"——原刊 "predicts"（mineru 留跨行连字残迹；
  文本层 predict）。修复：pre-dicts→predicts。

## p.004
- 核对：homological stability/Hurwitz spaces/Cohen-Lenstra 部分验证 ✓；第三例 conjectures/
  2017-2018 seminars ✓；Langlands Program/FLT（Wiles+Taylor）/Taylor-Wiles 方法/Shimura
  varieties ✓；locally symmetric spaces/homology/motivic cohomology ✓；"ascent towards a full
  understanding of the Langlands Program." ✓——但其后原刊还有收尾段（跨 p.4-p.5）
- 结果：**FAIL（跨页整段丢失，见 p.005）**

## p.005
- 核对：原刊收尾段（文本层全文）：**"Most mathematicians are either problem-solvers or
  theory-builders. Akshay Venkatesh is both. What is more, he is a number theorist who has
  developed an unusually deep understanding of several areas that are very different from number
  theory. This breadth of knowledge allows him to situate number theory problems in new contexts
  that provide just the right setting to highlight the true nature of the problems. Only 36 years
  of age, Venkatesh will continue to be an outstanding leader in mathematics for years to come."**
  ——**md 整段丢失 → FAIL（跨 p.4-p.5）**
- 结果：**FAIL（整段丢失）**

## 总评

- **覆盖声明**：5/5 页逐页目检 + pdftotext 文本层逐字符对账。mineru：standard 档。
- **FAIL 清单（3 点）**：①m≥n+5 丢句号（p.2）；②pre-dicts→predicts（p.3）；③收尾段整段丢失
  （p.4-p.5，~70 词）。
- **原刊排印 quirk（忠实保留）**：spaces "harbor"（原刊如此）；ff→f 家族（diferent/afirmed——
  文本层为 different/affirmed，登记不改）。
- **可用性结论**：修复后 md 可作该报告忠实底本。

### 修复登记（2026-09-29）
- m≥n+5 补句号；pre-dicts→predicts；补收尾段（Most mathematicians…for years to come.，
  依文本层原文）。fix commit 见 `git log --grep 'fix(md): ICM2018 Venkatesh'`。
