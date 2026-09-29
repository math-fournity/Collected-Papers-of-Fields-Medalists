# AUDIT — S. Smale《Generalized Poincaré's Conjecture in Dimensions Greater Than Four》

> mineru: standard 档云端解析，导出 `Smale_1961_generalized_poincare_mineru/`；
> 审计依据 = 二值化渲染 `audit/pNNN.png`（pngmono 150dpi）对照
> `Smale_1961_generalized_poincare__Smale_1961_generalized_poincare.md`。逐页审计，一页一签。
> PDF 结构：17 页（PDFlib 3.02 生成）。

## p.001（PDF p.1 / JSTOR 封面页）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：JSTOR 封面（题名/作者/Annals 74 (1961), 391-406/Stable URL/使用条款三段）逐字转写 ✓
- 结果：**PASS±**（±：底部 "http://uk.jstor.org/ Fri Mar 17 02:07:43 2006" 下载戳记行未收——戳记惯例）

## p.002（PDF p.2 / 印刷 p.391）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：
  - 题录（标题/作者/Received October 11, 1960/Revised March 27, 1961）✓；引言段（Poincaré 问题、
    generalized conjecture、n ≥ 5）✓
  - **THEOREM A** ✓；announced in [20] ✓
  - **THEOREM B**：原刊即印 "which has the **homotopy** of Sⁿ"（应为 homotopy type，源级笔误）
    ——md 忠实保留，不代改 ✓
  - Stallings [Bull. Amer. Math. Soc., 66 (1960), 485–488] ✓；nice function 定义 ✓
  - **THEOREM C**（(m−1)-connected、n ≥ 2m、(n,m) ≠ (4,2)、M₀ = Mₙ = 1、Mᵢ = 0）✓
  - cellular structure 段 ✓；脚注 *（Alfred P. Sloan Fellow）✓
- 结果：**PASS±**（±：①页眉 "ANNALS OF MATHEMATICS Vol. 74, No. 2, September, 1961 Printed in
  Japan" 与页码 391 未收；②Theorem B 缺 "type" 系原刊实物）

## p.003（PDF p.3 / 印刷 p.392）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：Theorem D（Morse [13]）✓；§1 handlebodies 预告（s-disks, k in number, Heegard）✓；
  **THEOREM F**（M=H∪H′, H∩H′=∂H=∂H′, 𝓗(2m+1,k,m)）✓；**THEOREM G**（type numbers = Betti
  numbers、𝓗(2m,k,m)）✓；Morse relation [12] 注 ✓；**THEOREM H**（一个极大一个极小、
  S^{2m−1} 交）✓；J-equivalence 定义（[25]/[10]、∂V ≅ M₁⊔(−M₂)、deformation retract）✓；
  **THEOREM I**（(m−1)-connected、2m+1 维、J-equivalent、m≠1 ⇒ diffeomorphic）✓
- 结果：**PASS±**（±：页眉 "392 STEPHEN SMALE" 与页码未收）

## p.004（PDF p.4 / 印刷 p.393）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：orientation preserving 段 ✓；[10, Problem 5] + Milnor counter-example 插语（括号相邻系
  原刊排印）✓；Milnor [10, p. 33]/Mazur [7]/[9, p. 440] 段 ✓；𝓗ⁿ 定义段 ✓
  - **THEOREM J** ✓；**微分结构表**：n=3,5,7,9,11,13,15 ↔ 0, 0, 28, 8, 992, 3, 16256——逐格吻合
    （|Θ₉|=8 系原刊实物，忠实保留）✓
  - countable/unique structures 段（[9, p. 442]、Munkres [14]、Milnor [8]）✓；Γⁿ/Aⁿ/i: Γⁿ→Aⁿ、
    p: Aⁿ→𝓗ⁿ 段 ✓
- 结果：**PASS±**（±：页眉 "POINCARÉ CONJECTURE 393" 与页码未收）

## p.005（PDF p.5 / 印刷 p.394）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：**THEOREM K**（(a) Aⁿ→𝓗ⁿ→0, n≠3,4；(b) Γⁿ→Aⁿ→0, n even≠4；(c) 0→Aⁿ→𝓗ⁿ, n odd≠3；
  Γⁿ=Aⁿ/Aⁿ=𝓗ⁿ 推论）✓；(a)/(b)/(c) 来源句 ✓；Kervaire [4] ✓；**THEOREM L** ✓
  - W₀ 论证：Theorem 4.1 [10] k=3、∂W₀→S¹¹、12-disk、H⁶(M, π₅(SO(12)))=0、index 8、
    Lemma 3.7 [10]、Bott [1] ✓ 逐字
  - **THEOREM M** ✓；Schoenflies/Mazur [7] 段 ✓；Poincaré duality 论证段（∂C homotopy sphere、
    attach 2m-disk、Theorem H）✓
- 结果：**PASS±**（±：页眉 "394 STEPHEN SMALE" 与页码未收）

## p.006（PDF p.6 / 印刷 p.395）
- PNG：audit/p006.png（pngmono 150dpi）
- 核对：Palais [17] 承接段 ✓；Theorem B 证明段（[Munkres 15]、double W、Mazur [7]）✓；
  **THEOREM N**（Hauptvermutung for closed cells）✓；Hirsch [3]/Whitehead [27] 论证 ✓；
  **THEOREM O**（Hauptvermutung for spheres）✓；Gluck [2] 段 ✓；program 段（[21]、F/G）✓；
  proofs similar 段 ✓
- 结果：**PASS±**（±：页眉 "POINCARÉ CONJECTURE 395" 与页码未收）
