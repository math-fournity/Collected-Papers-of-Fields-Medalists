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

## p.004（PDF p.4 / 印刷 p.1020：E₂ 变换律 + quasimodularity (2.2) + φ₁/φ₂ + (2.3)(2.4)(2.5) + Lemma 2.1）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：z^{−2}E₂(−1/z)=E₂(z)−6i/(πz)、(2.2) z⁸φ(−1/z)=φ(z)+φ₁(z)/z+φ₂(z)/z²、
  φ₁=−(6i/π)48·E₆E₄²/Δ²−(12i/π)·E₂(−49E₄³+25E₆²)/Δ²=(i/π)(725760q⁻¹+113218560+19691320320q+O(q²))
  （系数逐位 ✓）、φ₂=−36(−49E₄³+25E₆²)/(π²Δ²)=(1/π²)(864q⁻²+2218752q⁻¹+223140096+23368117248q+O(q²))
  （系数逐位 ✓）、(2.3) φ(i/t)=O(t^{−10}e^{4πt})、(2.4) φ(i/t)=O(e^{−2π/t})、
  (2.5) a(r)=−4sin(πr²/2)²∫₀^{i∞}φ(−1/z)z¹⁰e^{πir²z}dz（r>2）、Lemma 2.1 陈述与编号、
  −4sin(πr²/2)²=e^{πir²}−2+e^{−πir²} ✓
- 差异与修复：md "modular forms of **diferent** weight" 与印刷原文（文本层+PNG 双通道均为
  "different"）不符 → 已修为 "different"
- 结果：PASS（修复后）

## p.005（PDF p.5 / 印刷 p.1021：Lemma 2.1 证明的围道平移 + quasimodularity 链 + (2.6)）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：八条围道积分等式（∫_{−1}^{i∞−1}/∫₀^{i∞}/∫₁^{i∞+1} → 拆分为 ∫_{−1}^{i}+∫_i^{i∞} 等，
  被积函数 φ(−1/(z+1))(z+1)¹⁰ / φ(−1/z)z¹⁰ / φ(−1/(z−1))(z−1)¹⁰ 与 e^{πir²z} 逐项一致）、
  quasimodularity 链 φ(−1/(z+1))(z+1)¹⁰−2φ(−1/z)z¹⁰+φ(−1/(z−1))(z−1)¹⁰
  = φ(z+1)(z+1)²−2φ(z)z²+φ(z−1)(z−1)² + φ₁/φ₂ 三行 → = 2φ(z)、
  (2.6) a(r)=∫_{−1}^i+∫₁^i−2∫₀^i+2∫_i^{i∞}φ(z)e^{πir²z}dz（tag 2.6 位置正确）、
  Proposition 2/Proposition 1 of [12] 引用、Schwartz 衰减段 ✓
- 差异与修复：md "sufices" 与印刷原文（文本层+PNG 均为 "suffices"）不符 → 已修为 "suffices"；
  另 "neighborhood ofR" 空格合并为排版伪影，登记不改
- 结果：PASS（修复后）

## p.006（PDF p.6 / 印刷 p.1022：â 的围道积分、w=−1/z 换元、(2.7)–(2.10) + p(t)/p̃(r)）
- PNG：audit/p006.png（pngmono 150dpi）
- 核对：e^{πir²z}→z^{−12}e^{πir²(−1/z)} 替换说明、â(r) 四积分（第三条 ∫₀^i φ(−1/z)**z^{−2}**、
  其余 z^{−12}，与 print 一致）、w=−1/z 换元后 φ(−1−1/(w−1))(−1/w+1)¹⁰w¹⁰ /
  φ(1−1/(w+1))(−1/w−1)¹⁰w¹⁰ + 2∫_i^{i∞}φ(w) − 2∫₀^iφ(−1/w)w¹⁰、â=a 结论、
  (2.7) a(r)=4i sin(πr²/2)²∫₀^∞φ(i/t)t¹⁰e^{−πr²t}dt（**4i** 正号 ✓）、
  (2.8) t¹⁰φ(i/t)=t²φ(it)−itφ₁(it)−φ₂(it)、(2.9) t¹⁰φ(i/t)=p(t)+O(t²e^{−2πt})、
  p(t)=−864/π²e^{4πt}+725760/π·te^{2πt}−2218752/π²e^{2πt}+113218560/π·t−223140096/π²
  （系数逐位 ✓）、p̃(r)=−864/(π³(r²−4))+725760/(π³(r²−2)²)−2218752/(π³(r²−2))
  +113218560/(π³r⁴)−223140096/(π³r²)（逐位 ✓）、(2.10) ✓
- 残留排版伪影（登记不改）："For $r > 2 .$," 类双句点伪影（本页 1 处，后页同型多处统一登记）
- 结果：PASS

## p.007（PDF p.7 / 印刷 p.1023：a 的特殊值 + Taylor 展开 + φ 的 Ansatz 五维空间）
- PNG：audit/p007.png（pngmono 150dpi）
- 核对：a(r) 在 √(2k)（k>2）二阶零点（p̃ 无极点）、a(0)=113218560i/π、a(√2)=725760i/π、
  a′(√2)=−4437504√2i/π（逐位 ✓）、a(2)=0、a′(2)=−3456i/π、
  Taylor a(r)=113218560i/π−223140096i/π·r²+O(r⁴)、归一化后 √2 处值 1/156、导数 −107√2/2730、
  2 处导数 −1/32760、归一 Taylor 1−3587/1820·r²+O(r⁴)、高阶项非有理说明、
  Δ²φ 为 weight 16 depth 2 holomorphic quasimodular 的 Ansatz、五维空间
  E₄⁴, E₆²E₄, E₆E₄²E₂, E₄³E₂², E₆²E₂²、由 (2.3)(2.4) 定 φ（[4] 数值猜想对照）✓
- 残留排版伪影（登记不改）："with $k > 2 .$," 双句点；"around $r = 0$" 两处句末句点缺失；
  "the eigenfunction$^{a,}$" 上标合并
- 结果：PASS

## p.008（PDF p.8 / 印刷 p.1024：§3 开头 + theta 函数与变换律 + (3.1)(3.2) ψ_I/ψ_S/ψ_T）
- PNG：audit/p008.png（pngmono 150dpi）
- 核对：§3 标题 "The −1 eigenfunction"、Θ₀₀/Θ₀₁/Θ₁₀ 三条级数定义、六条 |₂S/|₂T 变换律
  （含 Θ₁₀⁴|₂T=−Θ₁₀⁴）、slash operator (g|_kM)(z)=(cz+d)^{−k}g((az+b)/(cz+d))、
  M∈SL₂(ℝ)、**(3.1) ψ_I=[7Θ₀₁²⁰Θ₁₀⁸+7Θ₀₁²⁴Θ₁₀⁴+2Θ₀₁²⁸]/Δ²
  =2q⁻²−464q⁻¹+172128−3670016q^{1/2}+47238464q−459276288q^{3/2}+O(q²)**（系数逐位 ✓）、
  weight −10 for Γ(2)、**(3.2) ψ_S=ψ_I|_{−10}S=−[7Θ₁₀²⁰Θ₀₁⁸+7Θ₁₀²⁴Θ₀₁⁴+2Θ₁₀²⁸]/Δ²
  =−7340032q^{1/2}−918552576q^{3/2}+O(q^{5/2})**（逐位 ✓）、
  ψ_T=[7Θ₀₀²⁰Θ₁₀⁸−7Θ₀₀²⁴Θ₁₀⁴+2Θ₀₀²⁸]/Δ²=2q⁻²−464q⁻¹+172128+3670016q^{1/2}
  +47238464q+459276288q^{3/2}+O(q²)（符号逐项 ✓）、ψ_S+ψ_T=ψ_I 与 Jacobi 恒等式 ✓
- 差异与修复：S/T 矩阵被 mineru 拍平为 "\binom{0}{1}\overset{-1}{0}…"（T 阵末元素丢失）→
  已按 p.8 原图重建 S=(0 −1; 1 0)、T=(1 1; 0 1)（同 e8 篇矩阵重建先例）
- 结果：PASS（修复后）

## p.009（PDF p.9 / 印刷 p.1025：(3.3)(3.4) + b(r) 定义 + Lemma 3.1 + 围道平移两式）
- PNG：audit/p009.png（pngmono 150dpi）
- 核对：(3.3) ψ_I(it)=O(e^{4πt})（t→∞）、(3.4) ψ_I(it)=O(t¹⁰e^{−π/t})（t→0）、
  b(r)=−4sin(πr²/2)²∫₀^{i∞}ψ_I(z)e^{πir²z}dz（r>2）、Lemma 3.1 陈述与编号（eigenvalue −1）、
  Proposition 6 of [12]、代入式 −4sin(πr²/2)²=**e^{−πir²}−2+e^{πir²}**（与 §2 顺序相反，
  md 两处均与 print 一致 ✓）、b(r) 两组围道等式（∫_{−1}^{i∞−1}ψ_I(z+1) − 2∫₀^{i∞}ψ_I
  + ∫₁^{i∞+1}ψ_I(z−1) = ∫_{−1}^i ψ_T + ∫₁^i ψ_T − 2∫₀^i ψ_I + 2∫_i^{i∞}(ψ_T−ψ_I)；
  应用 ψ_T−ψ_I=−ψ_S 后末项 −2∫_i^{i∞}ψ_S）、ψ_I(z+1)=ψ_I(z−1)=ψ_T(z)、i∞±1→i∞ 端点说明 ✓
- 差异与修复：md "for$r > 2$2" 句末多出游离字符 "2"（print 为 "for r > 2,"，文本层+PNG 双通道
  无此 2）→ 已修为 "for$r > 2$,"；
  残留伪影（登记不改）："to $r \ \leq \ 2 .$," 双句点
- 结果：PASS（修复后）




