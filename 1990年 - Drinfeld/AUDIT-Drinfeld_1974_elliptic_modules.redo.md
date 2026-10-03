# AUDIT（重做）— V. G. Drinfeld, "Elliptic Modules"（p.1–p.9 批次）

- 性质：Luna 审计重做。用户 2026-10-02 判定 GPT-6 Luna 的审计不可信，本文件对 Drinfeld_1974_elliptic_modules 逐页对照 PDF 原页全量重检；Luna 旧修复（初判 32 页 PASS± 3 / FAIL 29，修订提交 145706440e02f1e1d2b5793a2f70367421cc108e）一并作为被检对象重核。
- actor：Wf-R-Drinfeld；host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置；本模型对自身 reasoning effort 无直接读取渠道，effort 标记自报 UNKNOWN，以 run 级配置 max 为准）。
- 原文 PDF：`Drinfeld_1974_elliptic_modules.pdf`，SHA-256 = `95f17bfb606dd63c8068c4a257f080590f3ed349910e25aa2f96f15b707d63a9`（本 session 实测，与派发单一致）。
- 被检 Markdown 基线：`Drinfeld_1974_elliptic_modules_mineru/Drinfeld_1974_elliptic_modules__Drinfeld_1974_elliptic_modules.md`，SHA-256 = `77dc542b8a3bd71ab217dc55c6c9801088886ca7bf5bdf92e93f8ba090a75825`（= Luna 修复后的当前态，本 session 实测；原始 mineru 产出见提交 0b0f3dd）。
- 文本层判定（2026-10-02 14:47 EDT，`pdftotext -f 1 -l 1 Drinfeld_1974_elliptic_modules.pdf -`）：**可用**，首页能提取完整英文正文（Math. USSR Sbornik 译本排版文本层，exit 0）。因此本篇采用**双通道主对账**：150dpi pngmono 页图为主证（公式、上下标、字形一律以页图裁决），pdftotext 文本层为副证（定位与散文比对）。文本层在数学区有系统性乱码（如 `<*>`→∞、`A;`→k∞、`d- 2`→d=2），不得以文本层覆盖页图判断。
- 证据图目录：`audit-redo/`（本篇 redo 专用；不动 Luna 旧 `audit/`）。
- 本批次范围：PDF p.1–p.9（印刷 p.561–569）。逐页流程 = gs pngmono 150dpi 渲染 → Read 目检 → 与 MD 对应段五点比对（题录/节标题顺序/定理编号与陈述/公式与上下标/记号）→ 分级 → 内容错误用结构化 Edit 逐处修复（含修正 Luna 旧修复中的错误；print quirk 忠实登记不改）→ 本文件落签 → 仅本篇路径 git add + commit（subject 前缀 `redo(page):`）。

## p.001（PDF p.1 / 印刷 p.561）

- PNG：audit-redo/p001.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p001_abstract.png、…_p001_adele.png、…_p001_adele_glyph600.png（600dpi）
- 核对：题录（题名/UDC/作者/摘要/Bibliography 14 items/AMS 分类脚注）、Introduction A) 开头、admissible triple 定义与四类、记号段（A、adèle 环、𝔘_f）。
- 结果：FAIL。记号段（MD 行 29）：印刷以 600dpi 定裁为 Fraktur **𝔘**（全 adèle 环）与 **𝔘_f**（去 ∞ 分量），当前 MD 写作正体 `U` 与 `$\mathfrak{A}_f$`；`\mathfrak{A}` 在本篇记号系统中未定义，属记号身份错误（Luna 旧签字仅记"页眉/页码未收"未察）。已 Edit 修复为 `$\mathfrak{U}$ … $\mathfrak{U}_f$`。旁证：pdftotext 文本层第 34–35 行 ABBYY 亦识别为 U 形（`U`/`v-`）。
- 重核 Luna 修复：摘要 `GL(2,Q)`（300dpi 确认斜体 GL）、"main result"（无 s）、`d \leq [\overline{k}_{\infty}:k_{\infty}]`、四类 triple、`$\zeta$-functions` 均与页图相符，无 Luna 引入的错误。
- 另记（PASS± 级伪影，不改）：期刊页眉两行、印刷页码 561、Copyright 行未收；triple 1)/2) 行尾分号在 MD 中脱落。
- ⚠ 跨页待查（本批次外）：p.018/p.025/p.031 Luna 将 MD 的 `𝔘_f` 改为 `𝔄_f` 的方向与 p.561 记号定义冲突，p.10–32 批次须以原页重裁核定。

## p.002（PDF p.2 / 印刷 p.562）

- PNG：audit-redo/p002.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p002_GLdf.png（GL(d,𝔘_f) 与 Theorem 1 𝔘_f^*）、…_p002_GL2U.png（Theorem 2 2) 与 GL(2,𝔘)）
- 核对：elliptic A-module of rank d 定义、level I 结构定义、N_I/N=lim← 段、Theorem 1、Theorem 1) 2) 两项、d=1,2 过渡段、B) Outline 至 §9、cusp form 编辑注。
- 结果：FAIL。adèle 环记号 4 处：MD 行 41 `GL(d,\mathfrak{A}_f)`、行 43 `\mathfrak{A}_f^*`、行 45 `GL(2,\mathfrak{A}_{f})`、行 49 `GL(2,\mathfrak{A})`，印刷均为 Fraktur **𝔘**（U 形，与 p.561 记号定义一致；300dpi 逐处核验）。已 Edit 逐处改为 `\mathfrak{U}_f` / `\mathfrak{U}`。
- 重核 Luna 修复：Theorem 2 陈述结构（H^1(N̄,Q̄_l)≃⊕_i U_i⊗W_i、U_i=⊗U_i^p、Gal(Q̄_p/Q_p)）、1) 中 L(s,W_i^p)=L(s−1/2,Û_i^p)、2) 中 Hom_{GL(2,R)}(Π,A_0)、P_1(R)、Outline 的 Ω^d/§§1 and 4/[14] 均与页图相符，无 Luna 引入的错误。
- 另记（PASS± 级伪影，不改）：页眉 "562 V. G. DRINFEL'D" 未收。

## p.003（PDF p.3 / 印刷 p.563）

- PNG：audit-redo/p003.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p003_sumlimit.png（⊕ 上限与 Λ̃ 定义句）、…_p003_prop11.png（Prop 1.1 引导句）、…_p003_name.png（致谢段人名）
- 核对：B) Outline 收尾（§§10 and 11）、[14]/[6]/[3] 段与 GL(2,A) Schottky 句、致谢、§1 标题、formal group 定义（F(x,F(y,z))=F(F(x,y),z)、D: End F→B、φ'(0)）、加法例、τ 与 B{{τ}} 交换律 τb=b^pτ、formal O-module 定义（D∘f=γ）、germ mod deg n、Λ_O 函子与 gradation 段（⊕_{k=0}^{n-1}Λ_O^k→ψB、ψ(ab)=ψ(a)ψ(b)、ψ(1)=1、Λ̃_O 因子）、Prop 1.1 引导句。
- 结果：FAIL。三处内容级差异：
  1. Prop 1.1（MD 行 81）：印刷 `Λ̃_O^{n-1}`（带 tilde，与其定义句及 Prop 1.3 一致），MD 缺 tilde；已 Edit 为 `$\widetilde{\Lambda}_O^{n-1}$`。
  2. 行 59/61 人名：印刷 `Pjateckiĭ-Šapiro`（ĭ=U+012D breve 在 i 上，Š=U+0160 caron 在大写 S 上；300dpi name 裁片），MD 写 `Pjateckiš-Sapiro`（caron 错置于 i、S 无 caron）；已两处定向 Edit 更正。
- 重核 Luna 修复/存留项：⊕_{k=0}^{n-1} 上限印刷确为 n−1（MD 本已相符）；formal group/module 各定义式、τ 交换律均与页图相符。
- 另记（PASS± 级伪影，不改）：页眉 "ELLIPTIC MODULES 563" 未收。

## p.004（PDF p.4 / 印刷 p.564）

- PNG：audit-redo/p004.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p004_rel3.png（关系(2)(3)）、…_p004_prooftilde.png（Proof 首句 Λ̃）、…_p004_Fpk.png（F_{p^k} 两处关系符）
- 核对：Prop 1.1 关系 (1)(2)(3) 与证明四个 display、C_n 注、B) Prop 1.2 两项及证明（φ(a∘b)=aφ(b)+b^{p^k}φ(a)、s=φ(a)/(a^{p^k}−a)）、C) 节设置、Prop 1.3 两项及其证明 1)。
- 结果：FAIL（1 处）。Proof 首句（MD 行 101）：印刷 `Λ̃_O^{n-1}`（tilde 清晰可辨，与 p.563 Prop 1.1 陈述一致），MD 缺 tilde；已 Edit 为 `$\widetilde{\Lambda}_O^{n-1}$`。
- 重核 Luna 修复：关系 (1) 的 `h(a)`/`h(a)∘p`、证明 display 的全部 `h(·)`、Prop 1.3 两项的 `h(a)`/`(a^n−a)h(b)=(b^n−b)h(a)` 均与印刷相符（Luna 由 `b` 改 `h` 的方向正确）。
- print quirk 登记（不改）：① 关系 (3) 印刷右端为 `h(a, b)`（带逗号，与证明中 `h(ab)` 写法不一致，系原文排印原样）；② Prop 1.2 证明第二个 `If O ⊂ F_{p^k}` 印刷无否定斜线（同段 `a ∉ F_{p^k}` 的 ∉ 斜线清晰），数学上应为 ⊄，忠实保留。MD 两处均与印刷原样一致。
- 另记（PASS± 级伪影，不改）：页眉 "564 V. G. DRINFEL'D" 未收。

## p.005（PDF p.5 / 印刷 p.565）

- PNG：audit-redo/p005.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p005_alpha.png、…_p005_hpib.png；600dpi 终裁：…_p005_alpha600.png、…_p005_hpib600.png、…_p005_hbar600.png、…_p005_prop15a600.png、…_p005_proof1q600.png；旁证（p.564）：…_p004_prop13_1line600.png、…_p004_prop13q600.png
- 核对：Prop 1.3 证明 1) 续与 2)、Prop 1.4 及证明、Corollary 两项、Prop 1.5 1)a)/1)b)/2) 全部 display、证明、加法判别 Corollary、D) 节标题。
- 结果：FAIL（3 处印刷忠实性回退，均为 Luna 旧修复或其遗漏）：
  1. 行 133 `α ↦ ?/π`：600dpi 确认印刷分子为斜体 **f**（升部+横杠+降部；同页 `h(p)`、`p^{n-1}` 与 p.564 `α = pu/π` 的斜体 p 均无升部，字形可区分）。Luna 将原 mineru 忠实的 `f` "修复"为 `p`，违反印刷忠实；已 Edit 回退为 `$\alpha \mapsto f/\pi$`（α 的修正保留）。**erratum 登记**：按 Prop 1.3 2) 数学上应为 p/π，印刷误排为 f/π，按原样保留。
  2. 行 135 首项：600dpi 确认印刷为 **h(π^b)**（π 带上标 b，字形完整非噪声），同句后文 `h̄(πb)` 无上标——印刷自身不一致。当前 MD（含 Luna 修复后）缺该上标；已 Edit 为 `$h(\pi^b) = \pi h(b) = \pi^{n}h(b)$`。**erratum 登记**：数学上应为 πb，上标系误排，按原样保留。
  3. 行 147 Prop 1.5 a)：600dpi 确认印刷为 "not a power of **g**"（g 与同片 `(G,g)`/`deg n` 同形；b) 行为直降部 q，同片可区分；p.564 Prop 1.3 1) 与 p.565 证明 1) 均为 q）。原 mineru 的 `g` 忠实，Luna "修复"为 `q` 违反印刷忠实；已 Edit 回退为 `$g$`。**erratum 登记**：数学上应为 q，印刷误排为 g，按原样保留。
- 重核 Luna 修复（其余）：全部 `h(·)` 系（含 `(a^n−a)h(b)=(b^n−b)h(a)`、`h(π)`、`h̄` 横线）与印刷相符；Prop 1.4/1.5 各 display（含 `h·p/π·C_n`、`h·(a^n−a)/π·x^n`）相符。
- 另记（PASS± 级伪影，不改）：页眉 "ELLIPTIC MODULES 565" 未收；行 135 印刷在前三项下有细横线（扫描/印痕），不转写。

## p.006（PDF p.6 / 印刷 p.566）

- PNG：audit-redo/p006.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p006_prop16.png；600dpi 终裁：…_p006_prop16_600.png、…_p006_prop16_3_h600.png、…_p006_Lambda_formula600.png、…_p006_Lambda_sub600.png、…_p006_sub_final.png；旁证（Luna 旧存证，只读）：audit/300dpi/Drinfeld_1974_elliptic_modules_p006.png
- 核对：homomorphism 定义句、height 定义（φ(x)=ψ(x^{p^k})、log_p q|k、k/log_p q）、O′-height remark、Prop 1.6 三项及证明、Prop 1.7 两项及 normal 条件 1)–3) 与证明 a)/b)/c)。
- 结果：FAIL（1 处印刷忠实性回退）。Prop 1.6 证明 1)（MD 行 205）：印刷为 `λ: Λ_0 ≃ O[g_1, g_2, …] → E`，下标为**数字 0**（600dpi 三方对照：p.566 该下标与 p.563 `k=0` 数字零同为窄长椭圆，而 p.563/564/565 的 `Λ_O` 下标均为宽圆字母 O）。Luna 将原 mineru 忠实的 `Λ_0` "修复"为 `Λ_O`，违反印刷忠实；已 Edit 回退为 `\Lambda_0`。**erratum 登记**：数学上应为 Λ_O（与 pp.563–565 记号一致），印刷此处误排数字 0，按原样保留。
- print quirk 登记（不改）：同一证明行的高度参数印刷作 **b**（`q^b−1`、`height b`，字形与 3) 行的双拱 h 可区分），与本页 3)/Prop 1.7 通篇的 h 不一致，系印刷混用；原 mineru 与当前 MD 的 b 忠实，保留。Luna 本页签字未涉此处，无改动。
- 重核 Luna 修复：Prop 1.7 的 normal 条件 1)–3) 及证明 a)b)c) 的全部 `h`（`q^h`、`F_{q^h}`、`1/h`）与印刷相符（Luna 由 b 改 h 方向正确）；height 定义式与 remark 相符。
- 另记（PASS± 级伪影，不改）：页眉 "566 V. G. DRINFEL'D" 未收。

## p.007（PDF p.7 / 印刷 p.567）

- PNG：audit-redo/p007.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p007_absnorm.png（绝对值记号句）、…_p007_example.png（A=F_q[x] 例子）
- 核对：Prop 1.7(c) 收尾（dim L/πL=h²、1/h、τ^{log_p q}a=a^q τ^{log_p q}）、§2 标题、§2A τ 环与 ε/D（D(Σb_iτ^i)=b_0）、全篇记号段（k_ν、| |_ν、A={x||x|_ν≤1}）、"char" 定义、elliptic A-module 定义、§2B deg 映射（=p^n）、Prop 2.1 两项及证明、rank 定义、F_q[x] 例子。
- 结果：FAIL（4 处）：
  1. 记号段绝对值（MD 行 235）：印刷为一对空杠加下标——`| |_ν is the normed absolute value`、`we write | | for | |_∞`、`the completion of A at | |_ν`；MD 单杠 `|_{\nu}`/`|_{\infty}` 丢一杠（且 "we write |_ν for |_∞" 语义不通）。已三处 Edit 为 `$|\ |_{\nu}$`/`$|\ |$ for $|\ |_{\infty}$`/`$|\ |_{\nu}$`。
  2. 例子（MD 行 255）：印刷为 "one can take any element of the form **(x)** + Σ_{j=1}^d a_j τ^{j log_p q}"——无 φ（同句 "In place of φ(x)" 对照；300dpi 确认）。原 mineru 忠实，Luna 补入 φ 违反印刷；已 Edit 回退为 `$(x) + \sum\ldots$`。**erratum 登记**：数学上应为 φ(x)，印刷脱落 φ，按原样保留。
- 重核 Luna 修复（其余，均相符）：1.7(c) 的 h²/1/h、`τ^{log_p q}`；§2A 的 `τ^i`（原 r^i）、`D(Σ_0^n b_iτ^i)=b_0`；Prop 2.1(b) 首式 `deg φ(a)·deg φ(b)` 的中点与印刷一致；例子中 `τ^{j log_p q}`（log_p 真下标）。
- 另记（PASS± 级伪影，不改）：页眉 "ELLIPTIC MODULES 567" 未收。

## p.008（PDF p.8 / 印刷 p.568）

- PNG：audit-redo/p008.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p008_prop23b.png（Prop 2.3(b) 指数）、…_p008_qexp600.png
- 核对：Prop 2.2 结论（|a|^d、i(a)≠0、 torsion ⊕(K_ν/A_ν)^{j_ν}、j_ν<d）、证明、Corollary、formal A-module remark（d−j_ν）、§2C isogeny 定义（αφ(a)=ψ(a)α）、Prop 2.3 a)/b) 及证明（uφ(a)=ψ(a)u、D(ψ(a))=[i(a)]^n、i(aⁿ)=i(a)）、Corollary、Prop 2.4 陈述与 proof 1) 开头。
- 结果：PASS±。全部内容项与印刷相符，本轮无需修改。重核 Luna 修复：`(K_ν/A_ν)^{j_ν}` 上标 j_ν、证明 `j_ν`、Prop 2.3(b) `t^{q^b}`（300dpi 确认指数为单闭碗 **b**，非 h——Luna 此处记号判断正确；与本文 height 通篇用 h 的不一致系印刷原样，quirk 登记）均忠实保留。
- 另记（PASS± 级伪影，不改）：页眉 "568 V. G. DRINFEL'D" 未收。

## p.009（PDF p.9 / 印刷 p.569）

- PNG：audit-redo/p009.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p009_recursion.png；600dpi 终裁：…_p009_tau_ref600.png（b_iτ^i 已知 τ）、…_p009_ajj600.png（a_j 后字形）、…_p009_recursion600.png、…_p009_api600.png（左指数 400%）
- 核对：Prop 2.4 证明 1) 收尾与 2)（|a|_ν<1、lim← 单射链、⊗_A A_ν 单射）、Corollary（End X、d²、⊗_A k_∞）、§3 标题、lattice/morphism 定义、Prop 3.1、Weierstrass 乘积 f(z)=zΠ(1−z/a)、Lemma g(z)=Π(z−α) 及证明、Γ 并集论证（L̄/Γ≃L̄、P_a 次数 |a|^d）、proof 2) 设置与递推式。
- 结果：FAIL（2 处）：
  1. proof 2) 正文（MD 行 317）：印刷为 "φ(a) = a + Σ_1^s a_j **r**^j"——600dpi 字形为斜体 r（单竖干+x高度右臂），与同证明开头清晰印刷的 τ（顶部横杠+中垂干，见 b_iτ^i、L{{τ}}）完全不同形。原 mineru 的 r 忠实，Luna 一并改为 τ 违反印刷；已 Edit 回退为 `a_j r^j`。**erratum 登记**：数学上应为 τ^j（φ(a) ∈ K{τ} 系数比较的上下文），印刷此处脱落 τ 的横杠排成 r，按原样保留；同句相邻的 b_iτ^i 印刷确为 τ，Luna 该处修改正确。
  2. 递推式（MD 行 320）：印刷为 **(a^{p^i} − a)b_i = Σ_{j=1}^s a_j b_{i-j}^{p^j}**——左侧 a 的指数为两层 p^i（600dpi/400% 确认小 p 在 i 下方；系数比较 fa=φ(a)f 亦要求 a^{p^i}）。当前 MD（含 Luna 修复）只有 a^i；Luna 澄清记录"扫描原式为 (a^i−a)b_i"与页图不符。已 Edit 补为 `a ^ {p ^ {i}}`。Σ 下限印刷为 j=1（j 带点/降部，非 i）。
- 重核 Luna 修复（其余，均相符）：`f = 1 + Σ_1^∞ b_i τ^i ∈ L{{τ}}`、`fa = φ(a)f`（无多余负号/点）、Corollary 与 proof 2) 各式。
- 另记（PASS± 级伪影，不改）：页眉 "ELLIPTIC MODULES 569" 未收。

## 批次总评（p.1–p.9 重做完成；2026-10-02）

- 覆盖声明：PDF p.1–p.9（印刷 p.561–569）逐页全检完毕，9/9 页落签；每页 150dpi 整页 PNG + 疑难处 300dpi/600dpi 仲裁裁片均存 `audit-redo/`，随页提交。逐页流程=渲染→目检→五点比对→分级→Edit 修复→落签→仅本篇路径提交，未写任何根级文件。
- 判定汇总：PASS± 1（p.008）、FAIL 8（p.001–p.007、p.009）。本批次共修 MD 17 处，其中**印刷忠实性回退 6 处**（均为 Luna 旧修复方向错误：p.005 f/π、p.005 g、p.006 Λ_0、p.007 (x)、p.009 r^j，及 p.002 起的 𝔄_f→𝔘_f 系（4 处，方向依据 p.561 记号定义 600dpi 定裁））；**Luna 漏修补齐 5 处**（p.001 行29 正体 U、p.003/004 两处 Λ̃ tilde、p.003 人名 ĭ/Š 两处、p.007 空杠对 | | 三处、p.009 a^{p^i} 补 p——后者 Luna 澄清记录与页图不符）；**Luna 修复经复核正确**的包括 p.004–005 的 h 系、p.006–007 的 τ 系/log_p q、p.008 的 t^{q^b}（指数确为 b，Luna 正确）与 j_ν 系。
- print quirk 登记（忠实保留、未改）：关系(3) `h(a, b)` 带逗号（p.004）；`O ⊂ F_{p^k}` 第二处无否定斜线（p.004）；Prop 1.6 证明 height 参数 b 与通篇 h 混用（p.006）；Prop 2.3(b) `t^{q^b}` 的 b（p.008）；erratum 级：`α ↦ f/π`（p.005）、`h(π^b)`（p.005）、`power of g`（p.005）、`Λ_0`（p.006）、`(x) + Σ`（p.007）、`a_j r^j`（p.009）。
- 跨页待查（p.10–32 批次必读）：① p.018/p.025/p.031 Luna 将 `𝔘_f` 改为 `𝔄_f` 的方向与 p.561 记号定义冲突，须以原页重裁核定（本批次证据：印刷为 Fraktur U）；② p.029 起如遇 `Pjateckii-Šapiro` 书目拼写，p.563 正文印刷带 ĭ（ĭ=U+012D），书目是否同形须独立核验；③ p.010 的 `p^{-i}` 类指数与 p.009 的 `a^{p^i}` 同族，建议 600dpi 复核。
- 最终 Markdown 复读收据：本 run 结束后已从头至尾复读全文 1136 行（1–347 为本 run 逐页工作区，348–1136 零改动区复读确认结构完整至 `Translated by M. B. NATHANSON`）；`git diff 8aa00fdd..HEAD` 枚举本 run 全部 MD 变更=17 处，逐项与本文件各页记录一致，无误伤。只读清点：行 1–330 残余 `\mathfrak{A}` = 0；`\mathfrak{U}` = 6 处（行 29×2、41、43、45、49），与页证一一对应。
- 基线与结果 SHA：MD 基线 `77dc542b8a3b…`（= Luna 修复后态）；最终 `e4ba86b7425f455ade3a20ca7ec8c0a1a71d875336f0e729580c19a90753fd9a`。逐页 commit：6679b8c9(p.001) / 1ccc6e82(p.002) / c0a4ba76(p.003) / 597c427d(p.004) / 411b1c26(p.005) / f80b9835(p.006) / e56f4e09(p.007) / 815bf9ae(p.008) / 89accf54(p.009)。

## p.010（PDF p.10 / 印刷 p.570）

- PNG：audit-redo/p010.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p010_proofopen.png（Prop 4.2 陈述末行 + Proof 首行）、…_p010_qexp600.png（q^h 指数 400%）
- 核对：Prop 3.1 proof 2) 收尾（c_i=|b_i|^{p^{-i}}、(1/a)Γ/Γ≃(A/(a))^d）与 proof 3)（f_2(αz)=P(f_1(z))、P(f_1(z))=f_2(αz)）、Corollary、§4 标题、§4A 设置（Ô^{nr}、Residue ≅ Ô^{nr}/(π)）、deformation 定义、Prop 4.1 及证明、isomorphic 定义、Prop 4.2 陈述、Proof 首行（q^h−1）。
- 结果：FAIL（1 处印刷忠实性回退）。Prop 4.2 陈述（MD 行 341）：印刷为 **Ô^{nr}[[t_1, …, t_{b−1}]]**（下标 b，300dpi 与同裁片证明行 q^h 的双拱 h 字形可区分），MD（含 Luna 修复）为 t_{h-1}；已 Edit 回退为 `t_{b-1}`。**erratum 登记**：数学上应为 h−1（同句 "finite height h"），印刷排成 b——与 p.566 Prop 1.6 证明的 b/h 混用同族，按原样保留。
- 重核 Luna 修复：递归估计两处 `p^{-i}`（c_i=|b_i|^{p^{-i}}、|a_j|^{p^{-i}}）与印刷相符（Luna 由 p-i 修复方向正确）；Proof 首行印刷确为 q^h−1（MD 相符，无需改）。
- 另记（PASS± 级伪影，不改）：页眉 "570 V. G. DRINFEL'D" 未收。

### p.010 勘误（本页落签后 600dpi 复核，随 p.011 commit 修正）

- p.010 条目中"Proof 首行印刷确为 q^h−1（MD 相符，无需改）"的记录**有误**：600dpi/400% 终裁（audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p010_qh600.png）显示 p.570 证明行印刷为 **q^b − 1**（闭碗 b），先前 300dpi 读判（…_p010_proofopen.png / …_p010_qexp600.png）将 b 误读为 h。已补 Edit 行 343：q^h − 1 → q^b − 1。p.570 的 b 记号与 p.571 通篇 b（见下条）连贯：变形函子语境印刷通篇用 b（t_{b-1}、i ≤ b−1、q^b−1、Σ^{b−1}），erratum 登记不变（数学上均为 h）。

## p.011（PDF p.11 / 印刷 p.571）

- PNG：audit-redo/p011.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p011_F0.png（(F^0,f^0) 段）、…_p011_phipsi.png（Let φ: 段）；600dpi 终裁：…_p011_qh600.png（q^b 指数）
- 核对：(F^0,f^0) 万能变形段、2-cocycle 定义与三组关系式、coboundary 定义、Lemma 1) 2)（含印刷 quirk "The exists"，MD 行 369 忠实保留）及证明、φ/ψ 同态构造段、(Δ_i,δ_i) 次数式、cohomology 基论证、a) 两条 coboundary congruence（x^n 与 x^{q^i}，C_{q^{i+h}}、(a^{q^{i+h}}−a)/π、h_i≠0）。
- 结果：FAIL（印刷忠实性回退，b 记号 7 处）。印刷（300dpi+600dpi 定裁）在本页通篇作 **t_{b-1}**（×5）、**1 ≤ i ≤ b−1**、**j < q^b − 1**、**Σ_{i=1}^{b-1}**；MD（含 Luna 修复）均为 h 系。已 Edit：行 345（t_{h-1}×2、h-1、q^h−1 → b 系）与行 375（t_{h-1}×3、Σ_{i=1}^{h-1} → b 系）。**erratum 登记**：数学上均为 h（finite height h 的 h−1），印刷 b/h 混用延续 p.566/p.570 同族，按原样保留。
- 重核 Luna 修复：cocycle 三组关系式、coboundary 式、(Δ_i,δ_i) ≡ 0 mod deg q^i / ≢ 0 mod deg(q^i+1)、mod m^r 两处（Luna 由 m' 修复）、a) 两条 congruence 全部与页图相符。
- 另记（PASS± 级伪影，不改）：页眉 "ELLIPTIC MODULES 571" 未收。

## p.012（PDF p.12 / 印刷 p.572）

- PNG：audit-redo/p012.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p012_D0.png（D_0 ≃ Ô^{nr}[[t_1,…]] 行）、…_p012_Lemma.png（Lemma 1) t_r,… 行）
- 核对：b) cocycle congruence 两式（v[(x+y)^n−…] 与 h·p/π·C_n）、§4B 设置（finite height h、n ∈ Z, n ≥ 0）、level-n 结构定义（φ: ((1/π^n)O/O)^h → m、f_{π^n}、Π_{α∈((1/π^n)O/O)^h}）、唯一结构段、Prop 4.3 三项（e_i (i=1,…,h)、O/(π)^n-模、D_m → D_n finite and flat）、Proof a)（D_0 ≃ Ô^{nr}[[t_1,…,t_{h-1}]]、0 ≤ r ≤ h、Φ_r、Π_{((1/π)O/O)^r}）、Lemma（L_r regular、e_i (i=1,…,r)、t_r,…,t_{h-1}、L_{r-1} → L_r finite and flat）、Proof 开头（θ_i = φ_{r-1}(e_i)）。
- 结果：PASS±。全部内容项与印刷相符，本轮无需修改。300dpi 确认本页两处 `t_{h-1}` 印刷均为**双拱 h**——印刷的 b 记号混用止于 p.571，本页回到 h；Luna 本页的 h 系修复（§4B height、f_{π^n}、level-n 结构指数等）经复核方向正确、MD 与印刷一致。 display 中 φ/ϕ 字形差异系印刷两种 phi 变体，MD 分用 \phi/\varphi 忠实。
- 另记（PASS± 级伪影，不改）：页眉 "572 V. G. DRINFEL'D" 未收。

### p.012 勘误（本页落签后 600dpi 复核，随 p.013 commit 修正）

- p.012 条目中"两处 `t_{h-1}` 印刷均为双拱 h"的记录**有误**：600dpi/400% 两页同倍率对照（audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p013_hb_compare.png）显示 p.572 的 D_0 basis 行与 Lemma 行的 t 下标同为**闭碗 b**（与 p.573 同款字形一致；先前 300dpi 读判 h 有误）。已补 Edit：行 421（D_0 ≃ Ô^{nr}[[t_1,…,t_{b-1}]]）与行 427（t_r,…,t_{b-1}）。p.012 判级由 PASS± 更正为 **FAIL**（2 处印刷忠实性回退，erratum：数学上均为 h−1）。

## p.013（PDF p.13 / 印刷 p.573）

- PNG：audit-redo/p013.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p013_Lr_display.png、…_p013_trh600.png；600dpi：…_p013_hb_compare.png（t 下标 b）、…_p013_yh_bn.png（r = h）、…_p013_eih_line.png（e_i (1≤i≤h)、((1/π^n)O/O)^h）、…_p013_Dnp1_full.png（D display 全式）、…_p013_prop44_P.png（imbedding display）
- 核对：g(x) 分式、φ_r 同态与 θ_r、L_r/(θ_1,…,θ_r,t_r,…) = Ô^{nr}/(π) display、local parameters 段、Π_{((1/π)O/O)^r}、injective 论证（Σα_iθ_i 属于平方）、Setting r = h、b) 段（e_i (1≤i≤h)、b_i）、D_{n+1} display、regular 段、Prop 4.4 陈述（P ⊂ ((1/π^n)O/O)^h、H def display、imbedding ((1/π^m)O/O)^h → ((1/π^n)O/O)^h/P）、Proof 开头。
- 结果：FAIL（3 处）：
  1. L_r/(θ_1,…,θ_r,t_r,…) = Ô^{nr}/(π) display（MD 行 445）与 local parameters 散文（行 447）：印刷 `t_r, …, t_{b-1}`（闭碗 b，600dpi 两页对照确认）；已 Edit 两处 t_{h-1} → `t_{b-1}`。**erratum 登记**：数学上为 h−1（同页 "Setting r = h" 印 h、e_i (1≤i≤h) 印 h、((1/π^n)O/O)^h 印 h——印刷仅在 t 下标处混用 b）。
  2. D_{n+1} display（MD 行 460）：印刷为 `D_n[[y_1, …, y_n]]/(f_π(y_1) − b_1, …, f_π(y_h) − b_h)`——同一 display 内首个 y 排 **n**、第二个排 h（600dpi：n 无升部双拱、h 有升部，字形可区分）；已 Edit 首个 y_h → `y_n`。**erratum 登记**：数学上均为 y_h，display 首位误排。
- 重核 Luna 修复：e_i (1≤i≤h)、((1/π^n)O/O)^h、P ⊂ ((1/π^n)O/O)^h、imbedding display 两处 ^h、Prop 4.4 全部陈述与 Proof 开头均与印刷相符（Luna 本页 h 系修复在独立 h 位正确；其 t 下标 h 读判有误已在本条更正）。
- 另记（PASS± 级伪影，不改）：页眉 "ELLIPTIC MODULES 573" 未收。

## p.014（PDF p.14 / 印刷 p.574）

- PNG：audit-redo/p014.png（pngmono 150dpi）；300dpi 仲裁：audit-redo/300dpi/Drinfeld_1974_elliptic_modules_p014_pim.png（((1/π^m)O/O)^? 上标）、…_p014_jh.png（level-n 结构 ^{j+h} 与 display）、…_p014_dimjh.png（dimension j+h）
- 核对：Prop 4.4 proof 收尾（tangent mapping、((1/π^m)O/O)^? → maximal ideal D_n、structure of level m）、§4C divisible O-module 定义（F/F_loc ≃ Spf R × (K/O)^j、splitting 序列）、finite height h、level-n 结构（((1/π^n)O/O)^{j+h} → Mor(Spf R, F)、epimorphism display）、Prop 4.5（G_loc height h、E_n ≃ D_n[[d_1,…,d_j]]、dimension j+h、E_m → E_n finite and flat）、Proof（Exp(Γ, Mor(Spf R, F))、[Mor(Spf R, F)]^j）、Remark（O'^* 作用、Spf E' = (Spf E)^Γ）。
- 结果：FAIL（1 处印刷忠实性回退）。Prop 4.4 proof（MD 行 481）：印刷 `((1/π^m)O/O)^**b**`（300dpi 闭碗 b，与同页 j+h 的双拱 h 可区分），MD（含 Luna 修复）为 ^h；已 Edit 回退为 `^b`。**erratum 登记**：数学上为 h，印刷误排 b——延续 §4 的 b/h 混用（p.566/570–573 同族）。
- 重核 Luna 修复：level-n 结构的 `^{j+h}`（散文+display）、Prop 4.5 的 `dimension j + h` 均印刷确为 h（300dpi 有升部双拱，Luna 此三处由 b 改 h 方向正确）；Exp/[Mor]^j/Remark 各式相符。
- 另记（PASS± 级伪影，不改）：页眉 "574 V. G. DRINFEL'D" 未收。

## p.015（PDF p.15 / 印刷 p.575）

- PNG：audit-redo/p015.png（pngmono 150dpi）
- 核对：§5 标题、§5A Prop 5.1 两项（f_j = Σ_{i=0}^{d_j} a_{ij}τ^i、a_{d_jj}、操作元 h、hf_1 = f_2h）及证明（m²=0、hf_1 = f_2h = a_02h、τ^{d+n}、d = d_1 = d_2）、Prop 5.2 陈述与 conjugation display、存在性证明（a_n/a_d^{p^{n-d}} 两处、τ^{n-d}）、§5B elliptic A-module over S 定义、standard module remark（Σ^{d log p|a|}、L^{1-p^i}）、V(I)/X_I 段（finite flat、étale）。
- 结果：PASS±。全部内容项与印刷相符，本轮无需修改。重核 Luna 修复（均正确）：操作元 `h`（原矿 b）、系数比较 `τ^{d+n}`（原矿 r）、`d = d_1 = d_2`（原矿 d=d_2=d）、分母 `a_d^{p^{n-d}}` 两处（原矿 p^{n-1}）——印刷逐一确证。
- 另记（PASS± 级伪影，不改）：页眉 "ELLIPTIC MODULES 575" 未收。
