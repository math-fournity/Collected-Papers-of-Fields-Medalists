# AUDIT — Henry Cohn, "The work of Maryna Viazovska"（ICM 2022 会议论文，Proc. Int. Cong. Math. 2022 Vol.1，DOI 10.4171/ICM2022/213；born-digital，MiKTeX pdfTeX + hyperref）

> mineru: standard 档导出 `IMU_laudatio_Viazovska_2022_mineru/`；**born-digital 文本层主对账通道**
> （pdftotext 全文 59.6KB/0 FFFD 逐点仲裁）+ PNG 抽验（题录页 + 密集数学页整页目检，300dpi 墓碑终裁 1 组）。
> print 页脚 = PDF p.N − 1（p.001 为题录页无页码；p.002 起 footer 1, 2, …, 23）。

## p.001（题录页）
- PNG：audit/laud_p001.png（整页目检）
- 核对：标题/作者/Abstract/MSC 2020（52C17; 11F03, 11H31）/Keywords ✓；
  **ICM logo + © 2022 IMU + "Preliminary version…" + DOI 10.4171/ICM2022/213 印刷页存在，md 未收
  （mineru 惯例；兄弟篇 Maynard/Huh/DC laudatio md 一致，不补）**
- 结果：PASS±（©/DOI 块按惯例丢弃）

## p.002（print 1：§1 开头 + 足注 1）
- 文本层 ✓：sphere packing 问题陈述、materials science/information theory、足注 1 全文
  （"as large a fraction as possible" 精确化/robust/equivalent formulations）与 md 足注 span 逐字 ✓
- 结果：PASS

## p.003（print 2：Thue/Hales + 密度数值）
- 文本层 ✓：Thue [26] 六邻居/π/√12=0.9068…/Hales [16] 计算证明+formally verified [17]/π/√18=0.7404… ✓；
  修复：数字拆分（1 2/1 8/0.9068/0.7404）+ 句末 \dots 补入
- 结果：PASS（修复后）

## p.004（print 3：E8/Leech + 定理 1.1/1.2 + Sarnak）
- 文本层 ✓：error-correcting codes/R^d 指数far apart/E8 root lattice/Λ24/Theorem 1.1 π⁴/384.
  与 1.2 π¹²/12!.（**print 句号在 ! 后，md 已补**）/Sarnak "stunningly simple"/[6,20]/[12,15,25] ✓；
  修复：384/12 数字拆分+句号、"diferent branches"→different、stray 句号 mash（rank d,/D_d./d=1,8./√2,,）
- 结果：PASS（修复后）

## p.005（print 4：§2 格定义 + 球体积公式）
- 文本层 ✓：Λ 离散子群 rank d、r=½min_{x∈Λ∖{0}}|x|、
  **球体积 print 原文即 π^{d/2} r^n/(d/2)!（n！应为 d 的出版笔误；display 同）——md r^n 忠实保留 + 源级登记**、
  Γ(d/2+1)/covolume 定义 ✓；修复："(d/2)!$!" 双感叹号/"(d/2)$! means" 数学边界
- 结果：PASS（修复后；r^n 源级）

## p.006（print 5：D_d 与洞）
- 文本层 ✓：D_d 定义（坐标和为偶）/D₃=FCC/D₄,D₅ 最优/shallow (1,0,…,0)/deep (√(d/4))/√2 距离 ✓；
  修复： stray 句号"$D_d.$,"、stray 括号")$)"、�→d ×2
- 结果：PASS（修复后）

## p.007（print 6：E8 密度 + Figure 2 + LP bound 头）
- 文本层 ✓：r=√2/2、covol(R⁸/E8)=1、π⁴/384=0.2536…、Coxeter plane 30-fold、Delsarte [13]、Cohn–Elkies [7]、
  Fourier 归一化 e^{-2πi⟨x,y⟩} ✓；修复："0.2536… It"吞词、数字拆分、Figure 2 说明句号
- 结果：PASS（修复后）

## p.008（print 7：Schwartz 函数 + Theorem 2.1 + Figure 3）
- 文本层 ✓：rapidly decreasing/Schwartz 定义、Theorem 2.1 三条件 (1)(2)(3)、
  "at most vol(B^d_{r/2}) = π^{d/2}(r/2)^d/(d/2)!." ✓；Figure 3 说明 [1]/[12] ✓；
  修复："Schwartzfunction and � …$H$"→"Schwartz function and $r$…If"、(2) 式内句号、定理尾句号、
  "fre quencies"、"only diference"、"magicfunctions"、Figure 3 前后文
- 结果：PASS（修复后）

## p.009（print 8：magic functions 猜想 + Poisson 求和 + Proof of Thm 2.1）
- 文本层 ✓：r=√2 与 r=2 猜想、"optimized only for d=1, 8, and 24."、Poisson summation formula、
  Λ* 对偶格、证明开头 |x|≧r for x∈Λ∖{0} ✓；修复：粘连词×3、�→f、"follows tha"→that
- 结果：PASS（修复后）

## p.010（print 9：证明收尾 ■ + 径向化 + Figure 4）
- 文本层 ✓：1=f(0)≧Σ…≧f̂(0)/vol、bounded above by vol(B^d_{r/2})、
  **墓碑 300dpi 终裁 = 实心 ■（print 原字形，md 忠实；audit/laud_p008_qed_300.png）**、
  "This reason is that"（print 语法 quirk 忠实）、E8*=E8、√(2n) 距离 ✓；
  修复："vo(“→vol(、Figure 4 说明 �→f + "Fourie"→Fourier、� 系 ×5、f′(√2n) 句号
- 结果：PASS（修复后；■/This reason 源级）

## p.011（print 10：不确定性 + Figure 5 + 1999 回忆 + Hales 引文）
- 文本层 ✓：f̂̂=f/f± 分解、single root √2/double roots √2n、Bourgain–Clozel–Kahane [4,8]、
  Figure 5 说明、Elkies 1999/Viazovska 中学、Hales "I felt that it would take a Ramanujan to find it" [19] ✓；
  修复："function$f 2$"→"$f$?"、"dificult/dificulties"、smart-quote 乱码 $^{66}\mathrm{I}$/it^{\prime\prime}
  → 正常引号、"th asymptotic"→the
- 结果：PASS（修复后）

## p.012（print 11：§3 模形式 + ζ + Eisenstein (3.1)）
- 文本层 ✓：SL₂(Z) 参考书 [24]/[5,14,28]、ζ(s) 定义、Euler 偶整数公式、Eisenstein (3.1)
  （1/2ζ(k) 归一化）、格 {mz+n} ✓；修复：�→s、数字/标点
- 结果：PASS（修复后）

## p.013（print 12：E_k 奇偶 + 足注 2 + Figure 6 + SL₂(Z) 矩阵）
- 文本层 ✓：(3.1) 绝对收敛 k≧3、奇 k 消零、interesting.² 标记、两条函数方程 E_k(z+1)=E_k(z)，
  E_k(−1/z)=z^k E_k(z)、T=(1 1;0 1)/S=(0 −1;1 0)、
  **足注 2 按 print 重构**（"…computing Σ_{n∈Z∖{0}} n^{−k} explicitly for all integers k > 1."，
  原 3 个 docvortex 碎片含 "k > 1.� > 1."/"Í_{�∈Z\{0}}" 幽灵碎片）✓；
  修复：足注 2 重构、γ 矩阵 garble（{a atop c d}b→pmatrix）、stray 括号/句号 ×4、H→𝓗
- 结果：PASS（修复后）

## p.014（print 13：weight-k action + 模形式定义 + q-series + E4/E6 + Δ）
- PNG：audit/laud_p014.png（整页目检）+ 文本层 ✓
- 核对：(f|_k γ)(z)=(cz+d)^{-k}f((az+b)/(cz+d))、γ=(a b;c d)、E_k|_kγ=E_k (k>2)、
  modular form 定义/holomorphic at infinity、f(z)=Σa_n e^{2πinz}、meromorphic/holomorphic at infinity、
  **"e^{2πiz}→0" 丢箭头已补**、q-series 命名、E₄=1+240Σσ₃qⁿ/E₆=1−504Σσ₅qⁿ、
  Δ=(E₄³−E₆²)/1728=q∏(1−qⁿ)²⁴ (3.2) ✓；修复：modularform ofweight、coeficient(s)、-series 丢 q、
  plain "SL₂(Z)"（print 原文）保留、数字拆分
- 结果：PASS（修复后；SL₂(Z) plain 源级）

## p.015（print 14：ΘE8 = E4 + 240σ₃(n) + 足注 3 + Γ(2) + U(z)）
- 文本层 ✓：theta series/N_n 定义/ΘE8 两条函数方程/weight 4/ΘE8=E4（N₀=1）/**240σ₃(n)**/squared norm 2n、
  **足注 3 按 print 重构**（"…need not satisfy (f|_kγ)(z+1)=(f|_kγ)(z), but … (f|_kγ)(z+n)=(f|_kγ)(z) for
  some positive integer n and thus has a Fourier expansion in e^{2πiz/n}=q^{1/n}."，原 7 个碎片
  含 "�|<sub>�</sub> �"/"e^{2���/�}=q^{1/�}" 幽灵）✓；Γ(2) 定义/index 6/U(z) ✓；
  修复：足注 3 重构、240σ₃ 后 stray 括号、数字拆分、�→n
- 结果：PASS（修复后）

## p.016（print 15：U,V,W (3.3) + §4 单根 + f± + warm-up + (4.1)）
- 文本层 ✓：W=U|₂T、V=U−W、(3.3) 六条 T/S 作用、U^k…W^k 张成、§4 标题、f̂̂=f/f± 定义、
  warm-up g 一阶根 √n、−1 eigenfunction、(4.1) g(x)=½∫ψ(z)e^{πiz|x|²}dz ✓；
  修复："�, �, and$W$"→U,V、"U$and �"→W、weight 2k、"U^k,…,W^k" 补省略号与句号、
  "diferent"、"obtain$f.$"→"$f$. contour integral"（integra 截断）
- 结果：PASS（修复后）

## p.017（print 16：周期性 (4.2) + g(√n)=a₋ₙ + ĝ + Γ=⟨S,T²⟩ + ψ₀/Δ）
- 文本层 ✓：ψ(z+2)=ψ(z)/(4.2)、正交性 g(√n)=½∫…=a₋ₙ、ĝ(y)=½∫ψ(z)z^{−4}e^{πi(−1/z)|y|²}dz、
  (i/z)^{d/2} 因子、u=−1/z 换元、ĝ(y)=−½∫ψ(−1/u)u²e^{πiu|y|²}du、ψ|₋₂S、
  Γ=⟨S,T²⟩ index 3、ψ|₋₂T²=ψ (i.e., ψ(z+2)=ψ(z))、cusp i∞、ψ=ψ₀/Δ ✓（PNG 整页目检同）；
  修复："ĝ=−g\ i f ψ|₋₂S=ψ"→"if"+句号、"\ ( i.e. )" 乱括号、q·-series、�→S/n/d、
  "suficiently"、"dificulties in 𝓗,,"、(S 与 T² 生成元)
- 结果：PASS（修复后）

## p.018（print 17：ψ₀ 张成 + α/β/γ + q-expansions + (4.3) + g 值 + Poisson）
- 文本层 ✓：U⁵,U⁴W,…,W⁵、α:=U⁵−6U³W²+4U²W³、β:=U⁴W−3U³W²+2U²W³、γ:=−U³W²+4U²W³−5UW⁴+2W⁵、
  六条 q-expansions（−q^{−1}−40q^{−1/2}+752/−1024+90112q/−16q^{−1/2}+256/−512−20480q/
  256−10240q^{1/2}/−2q^{−1}−32）、(4.3) ψ=(2β−α)/Δ=q^{−1}+8q^{−1/2}−240−6176q^{1/2}−⋯、
  g 值分段（−240/8/1/0）、Poisson over Z⁸ and E8 ✓；修复：数字拆分 ×12、�→q/ψ、S/T 生成元
- 结果：PASS（修复后）

## p.019（print 18：四行围道重排 + (4.4) + 解析延拓 + 大 display + 可去奇点）
- 文本层 ✓：|x|²>2 suffice、−1→−1+i∞/1→1+i∞ 分拆、e^{−πi|x|²}−e^{πi|x|²}/2、
  "the third line uses the fact that"（**"1 + i B" 幽灵串删除**）、∫_{−1+iR}^{1+iR}→0、
  ψ(u−1)=ψ(u+1)、**"si(π|x|²)"→sin**、(4.4)、ψ(it+1)=e^{2πt}−8e^{πt}−240+6176e^{−πt}−⋯、
  延拓 display（(x²−2)/(x²−1)/x² 三项+残余积分）、removable singularities at 0,1,√2. ✓；
  修复：幽灵串、si→sin、"for all$x,,"、句号 ×3、数字拆分 ×5
- 结果：PASS（修复后）

## p.020（print 19：§5 双根 + f₋ 公式 + −4sin² 分解 + 围道 display）
- 文本层 ✓：f₋(x)=−4i sin(π|x|²/2)²∫_{0}^{i∞}…、−4sin²=e^{−πi|x|²}+e^{πi|x|²}−2、
  三段围道 display、ψ holomorphic + 指数有界、shift contours 后 display、Figure 7 ✓；
  修复："suficiently"、Figure 7 说明 "� (�)"→f₋(x) + 句号、"for all$x.$."
- 结果：PASS（修复后）

## p.021（print 20：f̂₋ display + 函数方程 + Γ(2) 归约 + ψΔ 张成 α,β）
- 文本层 ✓：Fourier transform 替换 z^{−4}e^{πi|y|²(−1/z)} 四段 display、u=−1/z 交换围道、
  ψ|₋₂TS=−ψ|₋₂T⁻¹、2ψ|₋₂S=2ψ−ψ|₋₂T−ψ|₋₂T⁻¹、T²∈Γ(2)、ψ|₋₂TS=−ψ|₋₂T 与 ψ=ψ|₋₂T+ψ|₋₂S、
  S²=I、ψΔ weight 10、**"under S and T"（md 的 $T_{\ast}$ 系 mineru 字形伪影已修）**、
  α:=2U⁴W−4U³W²+U²W³+UW⁴、β:=5U⁴W−10U³W²+5U²W³+W⁵ ✓；
  修复：T_* 伪影、S²=I..、spanned b→by、"set$u=−1/z,,"、ψΔ、句号
- 结果：PASS（修复后）

## p.022（print 21：q-expansions + ψ=−5α+2β/Δ + a₁ 极点 + (5.1) + 正性 + f₊ 构造）
- 文本层 ✓：α/Δ=−16q^{−1/2}+768+⋯、β/Δ=q^{−1}−40q^{−1/2}+2064+⋯、ψ=−5α+2β/Δ=2q^{−1}+288+⋯、
  q^{−1/2} 项消除动机、analytically continue、a₂e^{2πt}+a₁e^{πt}+a₀、三项极点 display、
  (a₂,a₁,a₀)=(2,0,288)、single root √2/double roots √2n、ψ(it)→0⁺、(5.1) ψ=W³(5U²−5UW+2W²)/Δ、
  ψ(it)>0 正性论证、f₊ 定义 ✓；修复：数字拆分 ×5、"\cdot\cdot\cdot\ as\ "吞词、"t 0+"丢箭头、
  stray 括号/句号 ×5、"radius√2,,"×2、f.$Constructing、quasimodularform
- 结果：PASS（修复后）

## p.023（print 22：φ 函数方程 + χ + E₂ quasimodular + Figure 8 + magic function f）
- 文本层 ✓：φ|₋₂TS=φ|₋₂T⁻¹、2φ|₋₂S=−2φ+φ|₋₂T+φ|₋₂T⁻¹、factor of −1、(ST)³=I、χ:=φ|₋₂S invariant under T、
  χ|₀S=χ (equivalently (χ|₋₂S)(z)=z²χ(z))、quasimodular depth 2、
  E₂=1−24Σσ₁qⁿ、z^{−2}E₂(−1/z)=E₂(z)−6i/(πz)、quasimodular form 定义、
  χ=(E₂E₄−E₆)²/Δ、Figure 8 说明（**print 真用 𝜑（varphi）字形，md \varphi 忠实保留**）、
  rescale f₊(0)=1/f₋′(√2)=f₊′(√2)、f(x) 与 f̂(y) 两条 display ✓；
  修复：\lrcorner→₋₂、"\mathrm{if~}"、stray 括号 ×2、coefficients、quasimodular form weight k、
  句号 ×2、数字 24、𝜑 保留判定（文本层 𝜙/𝜑 两个不同码位）
- 结果：PASS（修复后；\varphi 源级）

## p.024（print 23：不等式检验 + §6 插值定理 + §7 展望 + References + 作者块）
- 文本层 ✓：f(x)≦0 for |x|≧2/f̂(y)≧0、φ(it)+ψ(it)<0 与 φ(it)−ψ(it)>0、asymptotics+interval arithmetic、
  miracle 总结、§6 Radchenko–Viazovska [23] Theorem 6.1、Cohn–Kumar–Miller–Radchenko–Viazovska [11]
  Theorem 6.2 ((8,1)/(24,2)) 与 universal optimality Theorem 6.3、§7 Klein-Gordon [2]/d=2 (4/3)^{1/4}/
  modular bootstrap [18]、References [1]–[28] 逐条（arXiv/DOI 全部核对）、
  作者块 Henry Cohn/Microsoft Research New England/cohn@microsoft.com ✓；
  修复："for all ,"→for all y、"dificult"、"interva arithmetic"、Theorem 6.1/6.2 粘连（thatfor/
  Schwartzfunction×2/$\to$R）、(d,n₀) 后 stray 括号、"f o r n≥n₀" letter-spacing、
  References 16 处粘连/断词（High-dimensional/bounds for/et fonctions positives/Soc./via modular forms/
  of points/of the/interpolation formulas/Bounds for/proof of the/A formal proof of the/
  magic functions/Visualizing modular forms/réseau E8/Elliptic modular forms/The 1–2–3 of Modular Forms）
- 结果：PASS（修复后）

## 总评

- **覆盖声明**：24/24 页文本层全对账（pdftotext 59.6KB/0 FFFD）+ PNG 抽验 3 页整页目检
  （p.001 题录/p.014 密集数学/p.008-300dpi 墓碑）+ 150dpi 全 24 页渲染入库；born-digital 通道。
- **通道仲裁判例**：文本层与 md 冲突处一律以文本层为准（其来自 PDF 实际字形 CMap）；
  文本层无法区分的字形（𝜑 vs 𝜙）以码位差异判 print 原貌；墓碑字形 300dpi 终裁。
- **FAIL 修复（4 类）**：①足注 2、足注 3 按 print 重构（原 10 个 docvortex 碎片含幽灵公式碎片）；
  ②smart-quote 乱码（$^{66}\mathrm{I}$…it^{\prime\prime}）→正常引号；③丢箭头 ×2（e^{2πiz}→0、t→0+）；
  ④吞词/截断 ×6（follows tha/contour integra/si(→sin(/th asymptotic/Fourie/fre quencies）。
- **系统性修复**：丢字形 � ×47（斜体 r/d/f/k/s/n/q/t/y 依上下文恢复）；ff 连字 ×26；粘连词 ×19；
  数字逐位拆分 ×24；stray 括号/句号/逗号 mash ×21；letter-spaced 记号 ×3；H→𝓗 ×2；γ 矩阵重建 1；
  T_* 伪影 1；References 粘连 16。**共约 190 处/120 规则**（pass-1 约 135 规则 + pass-2 17 规则 + 散点 3）。
- **源级 quirk 清单（忠实不改）**：球体积公式 **π^{d/2}r^n/(d/2)!（n 系 print 笔误，应 d）**正文与
  display 两处；墓碑 **实心 ■**（300dpi 证实）；"This reason is that"；"SL₂(Z)"（generator ring 处
  plain Z）；图 8 说明 **𝜑（varphi）字形**（正文用 𝜙，文本层码位互异）；[26] Forhandlingerne 条目
  无 "møder"；©/DOI 块未收（mineru 惯例，兄弟篇一致）。
- **可用性结论**：修复后 md 可作该文忠实底本；8 个编号公式 (3.1)-(3.3)/(4.1)-(4.4)/(5.1) 齐全，
  3 个定理/3 个 Figure 说明/28 条 References/作者块完整。与 dim8 arXiv 版（已审 ✅）、dim24 published
  （已审 ✅）、ICM2022 Viazovska（已审 ✅）构成 Viazovska 目录闭环。

### 修复登记（2026-09-30）

- pass-1 约 135 规则 applied（11 规则 missed 经探针修正）+ pass-2 17 规则 applied + 散点 2 规则
  ——**全部收敛：� 清零/数字拆分清零/ff 粘连清零/docvortex=3（足注 1+2+3）/tag 8 组齐全**。
- fix(md) commit 父提交 = 修复前 md 原貌（audit(page) 提交不含 md 改动）；脚本
  /tmp/viazovska_laudatio_pub/fix_md.py + fix_md2.py（收敛式，missed→探针→修正二段收敛）。
- 本篇 24/24 页完成，无未决项。
