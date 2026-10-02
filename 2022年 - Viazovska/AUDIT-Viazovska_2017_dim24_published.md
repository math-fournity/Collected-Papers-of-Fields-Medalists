# AUDIT — H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, "The sphere packing problem in dimension 24"（Ann. of Math. 185 (2017), 1017–1033，DOI 10.4007/annals.2017.185.3.8；Annals 排版版 born-digital）

> - actor：`Wf-P41`
> - host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置 max，模型自报 UNKNOWN）
> - 开工时间：2026-10-02 12:30
> - PDF SHA256：`2d1f2b131259a92ffbe77d4d3d04e96c899597fa41581ad5ea13554c62bc958d`
> - MD 基线 SHA256（mineru 原始导出，修复前）：`bed8ba550cc6795d2dd730cbf788d1738dc988c4916cecbbce86fd7f2f84de31`
> - 对账通道：born-digital 文本层（`pdftotext -layout` 逐页）主对账 + 150dpi pngmono 整页目检；
>   print 页码 = PDF p.N + 1016（p.001=1017 … p.017=1033）。
> - 本块范围：p.1–p.9（p.10–p.17 由后续块处理）。

## 总评（全 17 页完成后补；Wf-P41，2026-10-02）

- **覆盖**：p.001–p.017 全部 17 页逐页审计完成（同 actor 两块连续执行：p.1–9 + p.10–17），
  非抽查；每页 PNG（audit/p001–p017.png，pngmono 150dpi）+ born-digital 文本层双通道对账。
- **等级分布**：PASS± 1 页（p.002，仅排版伪影+print quirk 登记）；其余 16 页 PASS（其中 12 页
  含修复，均修复后 PASS）；无 FAIL 未决项。
- **修复合计 40 处**（逐处计数：p.1×2、p.4×1、p.5×1、p.8×1、p.9×1、p.11×5、p.12×2、
  p.13×5、p.14×13、p.15×4、p.16×3、p.17×2；每处可溯源至页码+原图+文本层，见各页条目）：
  题录期刊头补回与 © 还原（p.1）；转写错字族 diferent/coeficients/sufices/dificult/
  dificulties/ineficient 等按 print 逐一还原；mineru 结构性损伤重建——S/T 矩阵（p.8）、
  −1/16380 乱码与无效命令 \overrightharpoon（p.11）、As t→∞ 丢箭头（p.13）、DOI URL 乱码
  （p.13）、Lemma A.1 脚注 1 六块乱序重排（p.14）、Viazovska 地址块乱序+重音还原（p.17）；
  游离字符与断行 URL 并行（p.9/p.11 Letπii/p.16 ×2/[8] arXiv/[13] DOI）。
- **print quirk 忠实保留登记**（不改）：p.2 "Optimizing the bound from Theorem 1.1"（语义应指
  Theorem 1.2，双通道确认系印刷原状）；p.15 Lemma A.2 证明中 t≤1 情形经换元后原文写
  "for t ≥ 1"（同属印刷原状）。排版级伪影（数字空格、双句点族、<sub>,</sub> 逗号、small caps
  拍平等）按 SOP 登记不改。
- **mineru doc_id**：导出目录仅含 images/、middle_json.json、structured_content.json，
  无 doc_id 落盘，无法登记（非遗漏）。
- **MD 终态**：mineru 原始导出（基线 SHA bed8ba55…）→ 逐页结构化 Edit 修复 → 全文复读核验
  → 只读脚本清点（命令与结果：`grep -c "coeficients|diferent|sufice|dificult|…"` = 0、
  游离字符/无效命令模式 = 0、`grep -c 'tag{'` = 20（(2.1)–(2.10)/(3.1)–(3.5)/(4.1)–(4.5)
  齐全）、关键系数与修复串逐项 ≥1；含复读补修 p.13 "dificult"→difficult 一处）；
  修复链完整保留于 git 历史（17 个页级 commit + 本总评 commit）。


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

## p.010（PDF p.10 / 印刷 p.1026：b̂=−b 收尾 + (3.5) + b 特殊值）
- PNG：audit/p010.png（pngmono 150dpi）
- 核对：Proposition 5 of [12] 路线、b̂(r) 四积分（全 z^{−12}：∫_{−1}^iψ_T + ∫₁^iψ_T
  − 2∫₀^iψ_I − 2∫_i^{i∞}ψ_S）、w=−1/z 换元后 ∫₁^iψ_T(−1/w)w¹⁰ + ∫_{−1}^iψ_T(−1/w)w¹⁰
  + 2∫_i^{i∞}ψ_I(−1/w)w¹⁰ + 2∫₀^iψ_S(−1/w)w¹⁰（积分限与系数逐项 ✓）、
  ψ_I|_{−10}S=ψ_S、ψ_S|_{−10}S=ψ_I、ψ_T|_{−10}S=−ψ_T 三方程及来源说明、
  (3.5) b(r)=**−4i**sin(πr²/2)²∫₀^∞ψ_I(it)e^{−πr²t}dt（负号 ✓）、
  ψ_I(it)=2e^{4πt}−464e^{2πt}+172128+O(e^{−πt})、
  ∫₀^∞(…)e^{−πr²t}dt=2/(π(r²−4))−464/(π(r²−2))+172128/(πr²)、
  r≥0 全轴公式（括号内符号 +2e^{4πt}+464e^{2πt}−172128 ✓）、analytic continuation 说明、
  b(r) 在 √(2k)（k>2）二阶零点、b(0)=b(√2)=b(2)=0、b′(√2)=928iπ√2、b′(2)=−8πi ✓
- 残留排版伪影（登记不改）："satisfies${\widehat b} = -b .$ we" 双句点+丢逗号
- 结果：PASS

## p.011（PDF p.11 / 印刷 p.1027：§3 收尾 Ansatz + §4 开头 f(r) 定义 + A(t) + (4.1) 前置）
- PNG：audit/p011.png（pngmono 150dpi）
- 核对：b(r)=−172128πir²+O(r⁴)、b maps ℝ to iℝ、(3.1) Ansatz（Δ²ψ_I weight 14 for Γ(2)、
  八维空间 Θ₀₁^{4i}Θ₁₀^{28−4i}, i=0..7、约束 ψ_S+ψ_T=ψ_I 三维、(3.3)(3.4) 定 ψ_I）、
  §4 标题 "Proof of Theorem 1.1"、**f(r)=−πi/113218560·a(r) − i/(262080π)·b(r)**、
  f(0)=f̂(0)=1、二次 Taylor 系数 −14347/5460 与 −205/156、根在 √(2k)（k=2,3,…）、
  f′(2)=−1/16380（Lemma 5.1 in [4]）、√2 处值 1/156 导数 −146√2/4095、
  f̂ 在 √2 处值 1/156 导数 −5√2/117、(2.7)+(3.5) → f(r)=sin(πr²/2)²∫₀^∞A(t)e^{−πr²t}dt、
  **A(t)=π/28304640·t¹⁰φ(i/t) − 1/(65520π)·ψ_I(it) = π/28304640·t¹⁰φ(i/t) + 1/(65520π)·t¹⁰ψ_S(i/t)**、
  f(r)≤0（r≥2 等号仅 √(2k)）、∫₀^∞A(t)e^{−πr²t}dt<0（r>2 收敛）✓
- 差异与修复（均为 mineru 转写错/乱，print 均正确）：①行 412 段首 "Letπii" 游离字符 →
  "Let"（print 为 "Let" + 显示式）；②"Taylor coeficients" → "coefficients"（print 双 f）；
  ③第二个 f̂ 写成无效命令 $\overrightharpoon{f}$ → $\widehat{f}$（print 为 f̂）；
  ④"f′(2) = −1/$\frac{\d}{\dt}$16380" 乱码 → "$-1/16380$"（print −1/16380）；
  ⑤"it sufices" → "it suffices"（print suffices）
- 残留排版伪影（登记不改）："For $r > 2 .$," 双句点；ψ<sub>I</sub> HTML 下标残留
- 结果：PASS（修复后）

## p.012（PDF p.12 / 印刷 p.1028：(4.1)–(4.4) + ψ_S 公式 + (4.2) 收敛半径 √2 论证）
- PNG：audit/p012.png（pngmono 150dpi）
- 核对：A(t)=π/28304640·t¹⁰(φ(i/t)+432/π²·ψ_S(i/t))、**(4.1) φ(it)+432/π²·ψ_S(it)≤0**、
  ψ_S=−[7Θ₁₀²⁰Θ₀₁⁸+7Θ₁₀²⁴Θ₀₁⁴+2Θ₁₀²⁸]/Δ² → ψ_S(it)≤0、归约为 φ(it)≤0（Lemma A.1，
  t≥1/t≤1 分情形）、**(4.2) f̂(r)=sin(πr²/2)²∫₀^∞B(t)e^{−πr²t}dt**、
  **(4.3) B(t)=π/28304640·t¹⁰φ(i/t)+1/(65520π)·ψ_I(it) = π/28304640·t¹⁰φ(i/t)−1/(65520π)·t¹⁰ψ_S(i/t)**
  （与 A(t) 镜像符号 ✓）、**(4.4) φ(it)−432/π²·ψ_S(it)≥0**（Lemma A.2）、
  (4.2) 实际对 r>√2 成立论证（B(t)=O(te^{2πt})、e^{4πt} 项相消、analytic continuation、
  不能延拓到 (0,∞) 否则 f̂ 在 √2 为零）、f̂≥0 for r≥√2、0<r<√2 需细分析 ✓
- 差异与修复：两处 "sufices"（(4.1) 前与 (4.4) 前）→ "suffices"（print 双通道均为 suffices）
- 残留排版伪影（登记不改）："for $r > \sqrt{2} .$," / "not just $r > 2 .$" 双句点族
- 结果：PASS（修复后）

## p.013（PDF p.13 / 印刷 p.1029：B(t) 减项论证 + (4.5) + §4 定理收尾 + Appendix A 开头）
- PNG：audit/p013.png（pngmono 150dpi）
- 核对：B(t)=1/39·te^{2πt}−10/(117π)·e^{2πt}+O(t)、[1,∞) 减项贡献
  ∫₁^∞(…)e^{−πr²t}dt=(10−3π)(2−r²)+3)/(117π²(r²−2)²)·e^{−π(r²−2)}（0<r<√2 非负）、
  剩余项 ∫₀^1+∫₁^∞（符号 −1/39·te^{2πt}+10/(117π)e^{2πt} ✓）对 r>0 收敛、
  **(4.5) B(t)≥1/39·te^{2πt}−10/(117π)·e^{2πt}**（t≥1，Lemma A.3）、
  §4 收尾（f 满足 Theorem 1.2 假设、根仅 r=√(2k)、[2] §8 → 唯一最密周期填充、
  Theorem 1.1 证毕）、Appendix A 标题与前四段（Sturm 定理 + truncated q-series、
  ancillary file appendix.txt、DOI 10.4007/annals.2017.185.3.8、arXiv 1603.06518、
  PARI/GP [10]）✓
- 差异与修复（print 均正确，双通道核验）：①"As t ∞" 丢箭头 → "As$t \to \infty$"；
  ②"it sufices to prove"（(4.5) 前）→ "suffices"；③"take a diferent approach" →
  "different"（print p.13 文本层 "different"）；④DOI URL 乱码
  "$\mathrm{https}//\mathrm{doi.org}/10$ 4007/…" → 纯文本 "https://doi.org/10.4007/annals.2017.185.3.8"
  （print 跨行 "10. / 4007"，与 p.1 题录 DOI 一致；便于检索）；⑤【全文复读补登】段末
  "not dificult to check" → "difficult"（print p.13 末句 "not difficult to check in any
  computer algebra system"，初审遗漏、复读发现后补修，证据同 p013.png）
- 结果：PASS（修复后）

## p.014（PDF p.14 / 印刷 p.1030：Appendix A 方法论 + Lemma A.1 证明前半 + 脚注 1）
- PNG：audit/p014.png（pngmono 150dpi）
- 核对：q 级数逼近+截断误差方法论（factors of t/π、Sturm 定理+精确有理算术）、
  系数增长控制：E₂ 被 24(n+1)²、E₄ 被 240(n+1)⁴、E₆ 被 504(n+1)⁶ 界、Θ₀₀⁴/Θ₀₁⁴/Θ₁₀⁴ 的
  q^{n/2} 系数 ≤ 24(n+1)²、级数乘积界 (n+1)^{ℓ+m+1}、φΔ²/ψ_IΔ²/ψ_SΔ² 多项式界、
  t≥1 用 q=e^{−2πt}、t≤1 换 1/t（z↦−1/z）、**Lemma A.1：t>0 时 φ(it)<0**、
  t≥1 情形：q=e^{−2πt}<1/535、φΔ² 系数 ≤ 513200655360(n+1)²⁰、
  Σ_{n=50}^∞ 513200655360(n+1)²⁰/535^{n−6} < 10^{−50}（逐位 ✓）、σ+10^{−50}q⁶ 在 (0,1/535) 不变号、
  **脚注 1：Both Θ₀₀⁴ and Θ₁₀⁴ have nonnegative coefficients, … D₄ root lattice …
  q^{1/2} … Furthermore, Θ₀₁⁴ = Θ₀₀⁴ − Θ₁₀⁴.** ✓
- 差异与修复（print 均为 coefficients/difficult/different/inefficient/suffice，双通道核验）：
  ①行 518 "coeficients become rational" → coefficients；
  ②行 520 段内 9 处词形修复："coefi cients"→coefficients、"coeficients/coeficient"×5→
  coefficients/coefficient、"dificult"→difficult、"diferent powers"→different、"ineficient"→
  inefficient、"sufice"→suffice；
  ③行 522 "coeficient bounds"→coefficient bounds；④行 530 "coeficient of q^n"→coefficient；
  ⑤**脚注 1 整段重排**：mineru 碎成 6 个乱序小块（含重复乱行 "Θ01 = Θ40 − Θ40 ."、
  两处 "coeficients"、"Both and have…" 主语丢失、"in the variable from which…" 宾语丢失）
  → 已按 p014.png 页底脚注原样合并为单条完整脚注
- 结果：PASS（修复后）

## p.015（PDF p.15 / 印刷 p.1031：Lemma A.1 证明后半 + Lemma A.2 全证明）
- PNG：audit/p015.png（pngmono 150dpi）
- 核对：q→0 极限负、φ(it)<0 for t≥1、(2.8) 归约 −t²φ(it)+itφ₁(it)+φ₂(it)>0、
  π 的有理界 ⌊10¹⁰π⌋/10¹⁰ 或 ⌈10¹⁰π⌉/10¹⁰、1≤t≤1/(23q^{1/2})（te^{−πt}≤e^{−π}≤1/23）、
  q^{1/2}<1/23、截断误差 ≤10^{−50}q⁶、q^{1/2} 多项式在 (0,e^{−π}) 为正、Sturm 放大到 (0,1/23)、
  分数幂不可避免说明、**Lemma A.2：φ(it)−432/π²·ψ_S(it)>0**、同法证明（q⁵⁰ 截断、
  (φ−432ψ_S/π²)Δ²、ψ_S 含 q^{1/2} 幂）、t≤1 情形经 (2.2)(3.2) 归约为
  −t²φ(it)+itφ₁(it)+φ₂(it)−432/π²·ψ_I(it)<0（print 原文即写 "for t ≥ 1"，忠实）、
  "Of course these proofs are by no means optimized" 段 ✓
- 差异与修复（print 双通道均为 coefficients/different/difficulties）：
  ①"control the coeficients" → coefficients；②"rational coeficients" → coefficients；
  ③"a diferent upper bound" → different；④"no dificulties" → difficulties
- 残留排版伪影（登记不改）："as$q \to 0$" 后句点缺失、"factors of t and$\pi .$but" 双句点 ×2、
  "Lemma$\mathrm{A.1}$ For" 句点缺失
- 结果：PASS（修复后）

## p.016（PDF p.16 / 印刷 p.1032：Lemma A.3 + References [1]–[10]）
- PNG：audit/p016.png（pngmono 150dpi）
- 核对：**Lemma A.3：t≥1 时 B(t) > 1/39·te^{2πt} − 10/(117π)·e^{2πt}**（严格不等号 ✓）、
  证明（乘 Δ²、q⁵⁰ 截断、误差 ≤10^{−50}q⁶、Sturm 收尾）、References 头、
  **[1]–[10] 逐条核对**：[1] Cohn Notices 64 (2017) 102–115 + noti1474；[2] Cohn–Elkies Ann. 157
  (2003) 689–714 + MR 1973059 + Zbl 1041.52011 + math/0110009；[3] Cohn–Kumar Ann. 170 (2009)
  1003–1050 + MR 2600869 + Zbl 1213.11144 + math.MG/0403263；[4] Cohn–Miller preprint 2016 +
  arXiv 1603.04759；[5] Conway–Sloane Grundl. 290 1999 + MR 1662447 + Zbl 0915.52003；
  [6] Ebeling Adv. Lect. Math. 2013 + MR 2977354 + Zbl 1257.11066；[7] Hales Ann. 162 (2005)
  1065–1185 + MR 2179728 + Zbl 1096.52010；[8] Hales et al. 22 作者名单逐姓核对 ✓ +
  Forum of Mathematics, Pi + arXiv 1501.02155；[9] de Laat–Vallentin Nieuw Arch. Wiskd. 17
  (2016) 184–192 + 1607.02111；[10] PARI/GP 2.9.1 2016 Bordeaux ✓
- 差异与修复（print 双通道核验）：①"Lemma A.3. For all$t \geq 1$2" 游离 2 → ","（print 逗号，
  与 p.9 同型）；②"$10^{-50}q^6$2 and Sturm's" 游离 2 → ", and"（print 逗号）；③
  [8] "arXiv 1501. 02155"（print 跨行 "1501. / 02155"）→ 并行 "1501.02155"（同 [7] DOI 并行先例）
- 残留排版伪影（登记不改）：参考文献作者 small caps 拍平（H. COHN→H. Cohn 等，mineru 一致风格）
- 结果：PASS（修复后）

## p.017（PDF p.17 / 印刷 p.1033：References [11]–[13] + 收稿日期 + 五单位地址邮箱）
- PNG：audit/p017.png（pngmono 150dpi）
- 核对：**[11] Thue** Forhandlingerne ved de Skandinaviske Naturforskeres 14 (1892) 352–353 +
  Zbl 24.0259.01；**[12] Viazovska dim 8** Ann. 185 (2017) 991–1015 + arXiv 1603.04246 +
  DOI …185.3.7；**[13] Zagier** The 1-2-3 of Modular Forms 2008 pp.1–103 + MR 2409678 +
  Zbl 1259.11042 + DOI 10.1007/978-3-540-74119-0_1；**(Received: May 23, 2016)**；
  五地址块逐条：Microsoft Research New England（cohn@microsoft.com）、Stony Brook
  （thenav@gmail.com）、Rutgers（miller@math.rutgers.edu）、Max Planck Bonn → Current address
  Abdus Salam ICTP Trieste（danradchenko@gmail.com）、Berlin Mathematical School and Humboldt
  University of Berlin → Current address École Polytechnique Fédérale de Lausanne
  （viazovska@gmail.com）——邮箱、城市、顺序均与 print 一致 ✓
- 差异与修复（依据 p017.png）：①[13] DOI "978-3-540-74119-0 1"（print 实为下划线 _1，
  提取时空格化）→ "978-3-540-74119-0_1."；②**Viazovska 地址块乱序重排**：mineru 把
  "Lausanne, Switzerland" 提到 E-mail 之前、把 "Current address : École Polytechnique
  Fédérale de Lausanne," 连同孤儿重音符 "<sup>´</sup>" 甩到末行 → 已按 print 顺序重建为
  Berlin/Germany → Current address École Polytechnique Fédérale de Lausanne（重音还原 É/é，
  删孤儿 ´）→ Lausanne/Switzerland → E-mail
- 残留排版伪影（登记不改）：地址块逗号被包为 <sub>,</sub>（基线检测伪影，五块一致，
  不改变内容）；作者 small caps 拍平同 p.16
- 结果：PASS（修复后）












