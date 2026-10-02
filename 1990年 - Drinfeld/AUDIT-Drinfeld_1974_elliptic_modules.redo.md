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
