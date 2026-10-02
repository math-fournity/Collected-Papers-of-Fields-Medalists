# AUDIT — H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, "The sphere packing problem in dimension 24"（Ann. of Math. 185 (2017), 1017–1033，DOI 10.4007/annals.2017.185.3.8；Annals 排版版 born-digital）

> - actor：`Wf-P41`
> - host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置 max，模型自报 UNKNOWN）
> - 开工时间：2026-10-02 12:30
> - PDF SHA256：`2d1f2b131259a92ffbe77d4d3d04e96c899597fa41581ad5ea13554c62bc958d`
> - MD 基线 SHA256（mineru 原始导出，修复前）：`bed8ba550cc6795d2dd730cbf788d1738dc988c4916cecbbce86fd7f2f84de31`
> - 对账通道：born-digital 文本层（`pdftotext -layout` 逐页）主对账 + 150dpi pngmono 整页目检；
>   print 页码 = PDF p.N + 1016（p.001=1017 … p.017=1033）。
> - 本块范围：p.1–p.9（p.10–p.17 由后续块处理）。

## p.001（PDF p.1 / 印刷 p.1017：题录页 + §1 开头 + Theorem 1.1 + 页底脚注）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：题录——标题 "The sphere packing problem in dimension 24"、作者行 "By Henry Cohn, Abhinav
  Kumar, Stephen D. Miller, Danylo Radchenko, and Maryna Viazovska"、期刊头
  **"Annals of Mathematics 185 (2017), 1017–1033" + DOI 10.4007/annals.2017.185.3.8**、
  Abstract 全文、§1 前两段、Theorem 1.1 陈述（ℝ²⁴、only periodic packing、up to scaling and
  isometries）、页底脚注 NSF DMS-1500562/CNS-1526333 与 © 脚注 ✓
- 差异与修复：① mineru 丢失期刊头两行（185 (2017), 1017–1033 + DOI URL）→ 已按 p.1 原文补回；
  ② 页底 © 脚注拍平为 "c 2017"（print 为 ©）→ 已还原为 "© 2017"（同 e8 篇 p.001 先例）
- 结果：PASS（修复后）

## p.002（PDF p.2 / 印刷 p.1018：Theorem 1.2 + Fourier 归一化）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：密度值 π¹²/12! = 0.0019295743…、[6] §2.8、lattice/periodic packing 定义段（[5, p. 140]
  ℝ¹⁰ 例）、Theorem 1.2 (Cohn and Elkies [2]) 全陈述——f: ℝⁿ→ℝⁿ Schwartz、f(0)=f̂(0)=1、
  f(x)≤0 for |x|≥r、f̂(y)≥0、上界 π^{n/2}/(n/2)!·(r/2)ⁿ、Γ(n/2+1) 说明、Fourier 归一化
  f̂(y)=∫_{ℝⁿ}f(x)e^{−2πi⟨x,y⟩}dx、radial 等同段与 ∫_{ℝ²⁴}f(|x|)e^{−2πi⟨x,y⟩}dx、
  页末 "Optimizing the bound…" 段 ✓
- print quirk 忠实登记（不改）：印刷原文写 "Optimizing the bound from **Theorem 1.1** requires
  choosing the right auxiliary function f"（语义上应指 Theorem 1.2；文本层与 p.2 PNG 双通道一致，
  系印刷原状）→ MD 保持 "Theorem 1.1" 不改
- 残留排版伪影（登记不改，无误导）：数字展开 "0. 0 0 1 9 …" 空格拆分；Theorem 1.2 内
  "\textit{r a}" 斜体合并与 "r,," 双逗号；"$f . .$" 双句点；"|x|=r" 与 "|y|=r" 两处句末句点缺失
- 结果：PASS±

## p.003（PDF p.3 / 印刷 p.1019：§2 开头 + quasimodular form (2.1) + E_k 与 Δ 定义）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：r=2 与半径 √(2k)（k=2,3,…）根条件、[2] §8 唯一性论证、[4] 特殊值猜想、
  weight −8/depth 2 与 weight −10/Γ(2) 双特征值函数路线、§2 标题 "The +1 eigenfunction"、
  **(2.1) φ = [(25E₄⁴−49E₆²E₄)+48E₆E₄²E₂+(−49E₄³+25E₆²)E₂²]/Δ²
  = −3657830400q − 314573414400q² − 13716864000000q³ + O(q⁴)**（三处系数逐位核对 PNG ✓）、
  q=e^{2πiz}、E_k(z)=1+2/ζ(1−k)·Σ_{n≥1}Σ_{d|n}d^{k−1}e^{2πinz}、
  Δ=(E₄³−E₆²)/1728=q−24q²+252q³+O(q⁴)、Δ 在上半平面无零点 ✓
- 结果：PASS

