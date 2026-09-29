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
