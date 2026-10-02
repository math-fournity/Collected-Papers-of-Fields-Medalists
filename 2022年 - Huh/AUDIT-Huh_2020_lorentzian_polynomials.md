# Huh_2020_lorentzian_polynomials 逐页审计

- 状态：候选审计进行中；尚未集成至 canonical main。
- Peer：Peer-P25；model=`gpt-6-luna`；reasoning effort=`max`。
- 审计基线：`main` / `037602429d3b009f6fc468c732073eb3ddf9875f`；本候选 worktree 起始 HEAD 与之相同。
- PDF：`Huh_2020_lorentzian_polynomials.pdf`，60 页；Creator=`LaTeX with hyperref`，Producer=`pdfTeX-1.40.25`。
- 模式：born-digital。`pdftotext -layout` 提取文本层 206,296 字节，未见 U+FFFD；以完整文本层逐页对账，题录页及密集数学页目检，符号/字形疑点回看 PNG/300dpi 原页。
- MinerU Markdown：`Huh_2020_lorentzian_polynomials_mineru/Huh_2020_lorentzian_polynomials__Huh_2020_lorentzian_polynomials.md`。修复前 SHA-256：`b2356501bfe781074b8cfca4ebb442037fc5dcb2a3ba155cb2c31dea621d3928`。
- 修改纪律：全篇逐页审计结束后才按 PDF 证据用 Edit/apply_patch 逐处修复 FAIL；修复后从头至尾重读最终 Markdown 并做只读清点。

## p.001（PDF p.1 / 印刷题录页）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:08 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p001.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p001_titlepage.png`（300dpi 原页）。
- 核对：标题、作者行、摘要全文、目录在本页出现的部分；逐页文本层取自 `pdftotext -f 1 -l 1 -layout`，标题/作者字形以 300dpi 原页终裁。
- 结果：FAIL（作者姓名内容错误）。
- 印刷证据：PDF p.1 作者行印为 “PETTER BRÄNDÉN AND JUNE HUH”；150dpi 与 300dpi 原页均可辨认。原页左侧另有 arXiv 版本/日期边注（`arXiv:1902.03719v8 [math.CO] 17 Jul 2024`），MinerU 未录；作为边注遗漏记录，待全篇核定其是否需修复。
- Markdown 现状：`PETTER BRAND <sup>¨</sup> EN AND JUNE HUH<sup>´</sup>`，把 Brändén 的变音符拆开并移位，且将尖音符误附到 Huh 后，不能忠实表示印刷作者姓名。
- 修复/复核：修复延至 60 页审计完成后；计划逐处手工更正作者行为 `PETTER BRÄNDÉN AND JUNE HUH`，完成后回看 PDF p.1 300dpi 证据并记录实际复核结果。

## p.002（PDF p.2 / 印刷 p.2）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:10 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p002.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p002_dense.png`（300dpi 原页）。
- 核对：目录末段及 Introduction 起始；完整文本层取 PDF p.2，按 Markdown 对应段落（当前约第 34–57 行）逐项比对。300dpi 原页用于裁决带圆圈的 `\mathring{L}` 记号和公式标点。
- 结果：FAIL（定义中的集合记号不忠实，另有公式标点误录）。
- 印刷证据：PDF p.2 写为“closure of `\mathring{L}_n^2`”；条件为 `\alpha_i > \beta_i,`，见本条所列 300dpi 原页。
- Markdown 现状：对应闭包对象写作 `\bar{\mathrm L}_n^2`；`\alpha_i > \beta_i` 后误置句点。印刷中的术语 `M-convex` 另被连写为 `Mconvex`。
- 修复/复核：全篇审计结束后分别核改圆圈记号、逗号和术语连字符；修订后重看此页 300dpi 原图并按 Edit 逐处复核。

## p.003（PDF p.3 / 印刷 p.3）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:12 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p003.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p003_name.png`（300dpi 原页）。
- 核对：central result 概述、M-convex/projectivization 段落、两个分解式、相关引文与脚注 1；文本层逐页对账，300dpi 原页用于核定变音与脚注符号。
- 结果：FAIL（作者引文字符错误；脚注丢失主语记号）。
- 印刷证据：PDF p.3 正文印为 “Borcea and Brändén”，Fano plane 引文为 `[Brä07]`；脚注 1 写明 `\mathbb{P}L_n^d` 与 closed Euclidean ball 的关系，均见 300dpi 原页。
- Markdown 现状：作者姓在正文拆成 `Brand ¨ en`，引文写成 `[Bra07 ¨]`；脚注为 “We conjecture that is homeomorphic …”，漏掉 `\mathbb{P}L_n^d` 这一主语。
- 修复/复核：全篇审计后逐处恢复 `Brändén`、`[Brä07]` 与脚注主语；以本页 300dpi 原图复核修订。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：移除 MinerU 额外插入、PDF p.3 不存在的独立 PL_n^d 页脚碎片；保留已恢复主语的脚注 1。以 p.3 整页图确认。

## p.004（PDF p.4 / 印刷 p.4）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:13 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p004.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p004_symbols.png`（300dpi 原页）。
- 核对：函数 `\nu` 的定义、Theorem 3.14 的参数范围及 M-convex 条件、指数生成函数、Brändén 引文、混合体积与交叉积陈述及脚注 2；符号疑点用 300dpi 原图终裁。
- 结果：FAIL（函数定义箭头与定理端点丢失/改变，交叉积符号误录）。
- 印刷证据：PDF p.4 写 `\nu : \mathbb{N}^n \to \mathbb{R} \cup \{\infty\}`，Theorem 3.14 的范围为 `0 < q \leq 1`，并明确说明 `\cdot` 表示交叉积；300dpi 原图可见三处字形/范围。
- Markdown 现状：函数定义在 `\mathbb{N}^n` 与 `\mathbb{R}` 间缺 `\to`；定理范围误成 `0 < q < 1`；交叉积符号记录为 `¨`。本页的 `Brändén` 及 `[Brä10]` 也被变音符拆散/移位。
- 修复/复核：全篇审计后逐处补回箭头、端点、交叉积点号并规范本页人名与引文；按本页 300dpi 原图回核。

## p.005（PDF p.5 / 印刷 p.5）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:14 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p005.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p005_footnote.png`（300dpi 原页）。
- 核对：Mason 不等式、Tutte 多项式及 rank function、加权生成式、`0 \leq q \leq 1` 范围、M-matrix 与概率测度段、脚注 3–4；脚注公式用 300dpi 原页核对。
- 结果：FAIL（集合/映射记号、矩阵维数和脚注蕴含式转录错误）。
- 印刷证据：PDF p.5 明确写 `[n]`、`\{0,1\}^n \to \mathbb N`、`n \times n`，脚注举例为 `(3) \Rightarrow (1)`；见 300dpi 原图。
- Markdown 现状：本页两处底集 `[n]` 误录成 `rns`；rank function 的 `\to` 丢失；`n \times n` 误成 `nˆn`；脚注 `(3) \Rightarrow (1)` 变成 `ofp3q ñ p1q`，且 `equivalent` 被断成 `equiva lent`。页面主不等式和 `q` 的闭端点与印刷一致。
- 修复/复核：全篇审计后逐处恢复两处 `[n]`、映射箭头、矩阵乘号和脚注蕴含式/单词；回看 300dpi 原图逐项复核。

## p.006（PDF p.6 / 印刷 p.6）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:16 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p006.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p006_acknowledgments.png`（300dpi 原页）。
- 核对：前页概率不等式的续句、Acknowledgments、§2.1 的题头、Hessian 定义及至 square-free monomial 的向量/集合记号；文本层逐页对账，致谢中的变音和单词用 300dpi 原页终裁。
- 结果：FAIL（作者/资助方姓名和致谢短语被错误转录）。
- 印刷证据：PDF p.6 写 “Petter Brändén”、“Vetenskapsrådet” 和 “Special thanks go to anonymous referees”；300dpi 原图还确认 “Knut and Alice Wallenberg Foundation” 中 Knut 后没有重音符号。
- Markdown 现状：Petter Brändén 被拆成 `Brand ¨ en`；`Knut ´ and Alice` 多出尖音符；`Vetenskapsrådet` 失去 å 上圆圈；“go to” 被录成 `${\\bf g 0}$to`。p.6 的概率界 `\leq 2` 与 §2.1 数学定义其余所核部分相符。
- 修复/复核：全篇审计后逐处还原人名、资助方拼写和 “go to”；回看本页 300dpi 原图确认变音与原词。

## p.007（PDF p.7 / 印刷 p.7）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:17 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p007.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p007_definition.png`（300dpi 原页）。
- 核对：Definition 2.1 的三个定义式、严格 Lorentzian 定义、递归展开式、stable polynomial 四个等价条件、Proposition 2.2 及证明，并核对 p.7 末段起始句；带圆圈的 `L` 和集合括号以 300dpi 原图终裁。
- 结果：FAIL（开圆锥记号被换成点记号，定义式的右括号不匹配）。
- 印刷证据：PDF p.7 在 Definition 2.1 和后续 open-set 句中都使用带圆圈的 `\mathring{L}`；第一条二次型定义以 `}` 收束。300dpi 原图可见圆环与完整大括号。
- Markdown 现状：第 196 行定义式用右圆括号 `)` 代替匹配左花括号的 `}`；第 206 行把 `\mathring{L}_n^2` 写成 `\dot{L}_n^2`。
- 修复/复核：全篇审计后逐处恢复匹配括号与圆圈记号，并用本页 300dpi 原图回核；其余列出的定义和命题文字/公式与 PDF p.7 文本层对应。

## p.008（PDF p.8 / 印刷 p.8）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:19 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p008.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p008_coefficients.png`（300dpi 原页）。
- 核对：行列式多项式、Example 2.3 系数及不等式、Example 2.4、`\mathring L` 记号和 Lemma 2.5 条件 (1)–(5)；系数和成员关系符号以 300dpi 原图终裁。
- 结果：FAIL（两个多项式系数被拆开；两个向量成员关系符号错误；另有开集符号误录）。
- 印刷证据：PDF p.8 的三次式系数为 `12` 和 `18`；Lemma 2.5 条件 (2)、(3) 均写 `u \in \mathbb R^n_{\geq 0}`；替代刻画句使用带圆圈的 `\mathring L_n^2`。300dpi 原图可见这些符号和系数。
- Markdown 现状：三次式写成 `1 2`、`1 8`；条件 (2) 用 `u : \mathbb R^n_{\geqslant 0}`，条件 (3) 用 `u P \mathbb R^n_{\geqslant 0}`；替代刻画句使用 `\dot{L}_n^2`。
- 修复/复核：全篇审计后逐处合并系数数字、恢复两个 `\in` 与 `\mathring L`，并对照本页 300dpi 原图复核；其余列出的命题和不等式与 PDF p.8 文本层对应。

## p.009（PDF p.9 / 印刷 p.9）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:21 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p009.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p009_matroid.png`（300dpi 原页）。
- 核对：Lemma 2.5 证明及各条件引用、matroid 基集定义和 exchange property、M-convex 的 exchange/symmetric exchange 条件、归一化多项式公式及脚注 5；引用编号和 ground-set 符号以 300dpi 原页终裁。
- 结果：FAIL（集合引用记号及条件引用编号损坏）。
- 印刷证据：PDF p.9 的 matroid ground set 和其子集均写作 `[n]`；证明中写 “the statement (3)”。300dpi 原图确认方括号和括号内数字 3。
- Markdown 现状：matroid 定义里两处 `[n]` 均误作 `rns`；Lemma 2.5 证明将 “statement (3)” 写成 `statement p3q`。M-convex 的两条交换条件及归一化公式与原文相符。
- 修复/复核：全篇审计后逐处恢复两处 `[n]` 与条件编号 `(3)`，并回看本页 300dpi 原图复核。

## p.010（PDF p.10 / 印刷 p.10）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:23 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p010.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p010_definition.png`（300dpi 原页）。
- 核对：support 定义、`M_n^d` 说明及 Definition 2.6、Proposition 2.7、Lemma 2.8 及其证明至拆分论证；集合与下标记号以 300dpi 原图终裁。
- 结果：FAIL（集合记号/下标损坏，另有引文键变音拆散）。
- 印刷证据：PDF p.10 写零多项式属于 `M_n^d`，引文为 `[Brä07, Theorem 3.2]`，indices `i,j` 属于 `[n]`；300dpi 原图可见这些标记。
- Markdown 现状：`M_n^d` 的下标误为 `n.`；引文键写成 `[Bra07¨, Theorem 3.2]`；indices `i,j` 的集合写成 `rns`。
- 修复/复核：全篇审计后逐处还原下标 `n`、引文 `[Brä07]` 和集合 `[n]`，并依据本页 300dpi 原图复核；其余列出的定义、命题和引理证明与 PDF p.10 文本层对应。

## p.011（PDF p.11 / 印刷 p.11）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:25 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p011.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p011_relation.png`（300dpi 原页）。
- 核对：stable polynomial 关系 `\prec` 的定义/性质、Lemma 2.9 条件及其后推论、Proposition 2.7 证明至 `d=3` 特例的归约；关系符与微分符号以 300dpi 原图终裁。
- 结果：FAIL（关系符号和偏导算子均被错录）。
- 印刷证据：PDF p.11 在 Lemma 2.9 假设、条件 (4)–(5) 及其性质句中使用 `\prec`；同页相应位置均使用 `\partial_1` 或 `\partial_i`。300dpi 原页清楚显示关系符上的额外笔画及偏导符。
- Markdown 现状：Lemma 2.9 假设、条件 (4)–(5) 中把 `\prec` 降为普通 `<`；条件 (1) 与随后 statement 句把 `\partial_1 f` 写作带帽的 `\sigma_1 f`/`\hat{o}_1 f`；Proposition 2.7 特例行将多个 `\partial_i` 写成带帽 `\sigma_i`。
- 修复/复核：全篇审计后逐处恢复 `\prec` 与 `\partial`；对照本页 300dpi 原图复核所有上述关系/算子位置。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：将 Proposition 2.7 特例归约中的 d “ 3 改为 PDF p.11 的 d=3；以同页 300dpi 裁片复核。

## p.012（PDF p.12 / 印刷 p.12）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:26 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p012.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p012_limit.png`（300dpi 原页）。
- 核对：三次情形下稳定性的论证、极限公式、Theorem 2.10 的变量变换分解及至第三种变换的 M-convex 观察；极限符号、微分算子和脚注 6 以 300dpi 原图终裁。
- 结果：FAIL（极限表达式漏符号并误加帽记号；脚注 6 丢失结论内容，另有非原文页脚碎片）。
- 印刷证据：PDF p.12 极限为 `\lim_{s\to 0}\partial_i(\cdots)=\partial_i f+\phi\partial_j f`；脚注 6 完整写明尚未证明 `L_{n+1}^d` closed。300dpi 原图可见箭头、无帽偏导及脚注全文。
- Markdown 现状：第 438 行把 `s\to 0` 写成 `s 0`，并在偏导符上加帽；第 480 行脚注将 “that L_{n+1}^d is closed” 丢成 `tha is closed`，缺少主语；第 476、478 行还有 `Mdn+1`、`t L^d_{n\`1}` 两个不见于原页的页脚碎片。
- 修复/复核：全篇审计后逐处恢复极限箭头、无帽偏导、完整脚注 6 并清除确认的页脚碎片；对照本页 300dpi 原图逐项复核。

## p.013（PDF p.13 / 印刷 p.13）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:29 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p013.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p013_operators.png`（300dpi 原页）。
- 核对：Proposition 2.7 证明结尾、Corollary 2.11 及证明、`T_n` 定义、Lemma 2.12 和其证明至首个严格负值结论；偏导算子和 interlacing 关系以 300dpi 原图终裁。
- 结果：FAIL（方向导数、微分符号和 interlacing 关系多处损坏）。
- 印刷证据：PDF p.13 的 Corollary 2.11 使用 `\sum_i a_i\partial_i f`；Lemma 2.12 两项主张均使用 `\partial^\alpha(1+\theta w_i\partial_n)^{d}f` 形式，并在比较式写 `\partial^{\alpha+e_n}f \prec \partial^{\alpha-e_i+e_n}f`。300dpi 原图可辨这些符号。
- Markdown 现状：Corollary 中 `\partial_i` 误成带帽 `\sigma_i`；Lemma 2.12 的 (I)/(II) 含 `\hat{\sigma}` 和 `\hat v` 替代 `\partial`；`\partial^{\alpha+e_n}f` 写成 `\hat{o}^{...}f`；比较关系的 `\prec` 降成 `<`。另外，上一段证明末尾的 QED 方框未保留（非内容级差异）。
- 修复/复核：全篇审计后逐处恢复偏导、指数微分算子及 `\prec`，并以本页 300dpi 原图复核；其余所列结论、变量变换公式与 PDF p.13 文本层相符。

## p.014（PDF p.14 / 印刷 p.14）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:31 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p014.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p014_interlacing.png`（300dpi 原页）。
- 核对：Lemma 2.12 证明 (I)–(III) 与 (II)、Theorem 2.13 闭包/同伦论证及段末主张；`\prec`、偏导和 `v_i^2` 以 300dpi 原图终裁。
- 结果：FAIL（微分算子与 interlacing 关系误录，另有公式下标噪声）。
- 印刷证据：PDF p.14 相应关系是 `\partial^{\alpha+e_n}f \prec \partial^{\alpha-e_i+e_n}f`；证明使用普通 `\partial^\alpha`、`\partial_n`，末段为 `v_i^2`。300dpi 原图均可辨。
- Markdown 现状：第 540、552、560、562 行把 `\partial` 识别为 `\hat{\sigma}`、`\hat{o}` 或 `\hat{v}`，并把 `\prec` 写成 `<`；第 568 行多出 `v_{i\cdot}^2` 中的点。Theorem 2.13 的同伦陈述与参数范围相符，但证明末尾的 QED 方框未录（非内容级差异）。
- 修复/复核：全篇审计后逐处恢复 `\partial`、`\prec` 与 `v_i^2`；以本页 300dpi 原图核查这些符号，并复读 Theorem 2.13 同伦段。

## p.015（PDF p.15 / 印刷 p.15）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:33 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p015.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p015_euler.png`（300dpi 原页）。
- 核对：§2.2 开头、Proposition 2.14 及证明、footnote 7、Lemma 2.15 到 Euler 公式后第一条 Hessian 恒等式；文本层逐页比对，300dpi 原图核定受损短语。
- 结果：FAIL（一个数学命名短语遭到错误插入）。
- 印刷证据：PDF p.15 写 “We will use Euler’s formula for homogeneous functions”；其后为 `d f = \sum_i w_i \partial_i f`。300dpi 原图可见 `Euler’s formula` 的完整文本，旁边无额外字母。
- Markdown 现状：第 618 行把短语写成 `Euler$' _ { \mathrm { { S } } }$ formula`，在 apostrophe 后插入数学字母 S 的样式代码，破坏了 `Euler’s`。
- 修复/复核：全篇审计后逐处恢复为 “Euler’s formula”，并以本页 300dpi 原图复核；其余所列命题、证明和 footnote 7 与 PDF p.15 文本层相符。

## p.016（PDF p.16 / 印刷 p.16）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:35 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p016.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p016_symbols.png`（300dpi 原页）。
- 核对：Lemma 2.15 证明收尾、Theorem 2.16 陈述及归纳证明、Proposition 2.17 不等式和其 Euler 恒等式前两项；下标/索引与 set membership 以 300dpi 原图终裁。
- 结果：FAIL（归纳步次数多出一个未定义记号）。
- 印刷证据：PDF p.16 归纳假设写 `d \geq 3`，未在 `d` 与不等式间另引入变量；300dpi 原图可见该位置只有 `d`。
- Markdown 现状：第 660 行在条件中插入了 `\ell`，形成 `d \ell \geqslant 3`。另，Lemma 2.15 最后一句的 `[n]` 前后在印刷页上可见异常点号 `\in .[n].`，Markdown 保留了这一 print quirk；不按数学预期改写原文。
- 修复/复核：全篇审计后删除多出的 `\ell`，并用本页 300dpi 原图确认修订；原页中的索引点号按 print 原样保留并作源级 quirk 登记。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：Proposition 2.17 题头原被包成数学算子 If，已恢复为普通 If 与 H_f(w) 条件；PDF p.16 的 300dpi 原图确认原句。

## p.017（PDF p.17 / 印刷 p.17）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:37 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p017.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p017_Mnatural.png`（300dpi 原页）。
- 核对：Proposition 2.17 证明收束、§2.3 开头、Definition 2.18、Proposition 2.19、`M^\\natural`-convexity 介绍及其投影定义；异常符号以 300dpi 原图终裁。
- 结果：FAIL（关键命题和 M-natural 领域术语严重误录）。
- 印刷证据：PDF p.17 先完成 Proposition 2.17；Proposition 2.19 写明每个 `L_n^d` 中多项式是 `2(1-1/d)`-Rayleigh；新术语为 `M^\\natural`-convexity。300dpi 原图清楚显示命题陈述及 `\\natural` 上标。
- Markdown 现状：第 704 行 `\\mathbb{\\rho}[w_1,\ldots,w_n]` 错替实系数多项式空间 `\\mathbb R[w_1,\ldots,w_n]`；第 720 行 Proposition 2.19 的陈述被转成乱码 array；第 724 行把 `M^\\natural` 错成 `M^6`。
- 修复/复核：全篇审计后逐处恢复 `\\mathbb R[w]`、Proposition 2.19 的完整结论和 `M^\\natural` 记号；按本页 300dpi 原图核对原文上标，其他列出的 Definition 2.18 条件与 PDF p.17 文本层一致。

## p.018（PDF p.18 / 印刷 p.18）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:41 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p018.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p018_Mnatural.png`（300dpi 原页）。
- 核对：`J^\\natural` 的投影性质、Lemma 2.20 的 Rayleigh 保持操作及被撤回的旧陈述说明、偏序与 interval-convex/augmentation 定义、Lemma 2.21 结论及其证明开头；superscript `\\natural` 用 300dpi 原图终裁。
- 结果：FAIL（`M^\\natural` 术语与投影对象均错录）。
- 印刷证据：PDF p.18 把 `J` 投影到 `J^\\natural`，并多次称为 `M^\\natural`-convex；300dpi 原图显示上标为自然符号 `\\natural`，不是数字 6。
- Markdown 现状：第 730 行投影对象写成 `J^\\sharp`；第 730、768、770、778 行把 `M^\\natural` 相关术语写成 `M^6`。
- 修复/复核：全篇审计后统一逐处恢复 `J^\\natural`/`M^\\natural`；对照本页 300dpi 原图复核该术语和投影对象，其余 Lemma 2.20 条目与被撤回声明保留原文内容。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：将 Lemma 2.20 contraction 条目恢复为 “of f.”，并将方向名修为印刷的 “only if”；依据 PDF p.18 文本层及页图。

## p.019（PDF p.19 / 印刷 p.19）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:42 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p019.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p019_Mnatural.png`（300dpi 原页）。
- 核对：Lemma 2.21 “if” 方向证明、Lemma 2.22 陈述及 interval-convex 反例证明起始；`M^\\natural` 与点号疑点回看 300dpi 原页。
- 结果：FAIL（核心凸性类别符号错误，并多出一个索引点）。
- 印刷证据：PDF p.19 多次用 `M^\\natural`-convex；“This index j is necessarily different from i” 中 `j` 前无乘号/点。300dpi 原图清楚可见自然符上标和无点的索引句。
- Markdown 现状：第 786 行把 augmentation property 归给 `M^\\sharp`；第 800 行把 `M^\\natural` 写成 `M^6`；第 794 行在 `j` 前插入 `\\cdot`。
- 修复/复核：全篇审计后逐处恢复 `M^\\natural` 与干净的索引句 `This index j`，并对照本页 300dpi 原图复核。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：恢复印刷的 “if” 方向措辞，并把 Lemma 2.22 陈述里的 supppfq 更正为 supp(f)；以 p.19 300dpi 原图复核。

## p.020（PDF p.20 / 印刷 p.20）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:45 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p020.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p020_subscripts.png`（300dpi 原页）。
- 核对：Lemma 2.22 的 interval-convex 反例证明前半段、正小量展开式、augmentation-property 失败条件及支撑集论证；范数下标以 300dpi 原图终裁。
- 结果：FAIL（三个一范数下标与周边数学行被拆坏）。
- 印刷证据：PDF p.20 使用 `|\\beta|_1`、`|\\alpha|_1 < |\\beta|_1`，以及 “minimality of `|\\alpha|_1`”；300dpi 原图均清楚显示下标 1 属于绝对值范数。
- Markdown 现状：第 838 行把 `|\\beta|_1` 后又追加独立 `<sub>1</sub>`；第 858 行将 `|\\alpha|_1<|\\beta|_1` 的第二个下标拆出数学环境；第 864 行也把 `|\\alpha|_1` 拆成数学片段与外置 `<sub>1</sub>`。
- 修复/复核：全篇审计后逐处将范数下标 1 放回对应数学表达式并消除重复/断裂；对照本页 300dpi 原图逐处复核，其他所列展开式和 augmentation 条件与 PDF p.20 文本层一致。

## p.021（PDF p.21 / 印刷 p.21）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:47 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p021.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p021_Mnatural.png`（300dpi 原页）。
- 核对：Lemma 2.22 证明 (2) 的导数乘积论证、Theorem 2.23 及其平移多项式证明、strongly Rayleigh 对照和 Proposition 2.24 的结论/二元估计；导数算子、凸性类别与作者引文以 300dpi 原图终裁。
- 结果：FAIL（微分算子被替换，M-natural 类别符号和作者引文失真）。
- 印刷证据：PDF p.21 写 `g(w)\\partial_j\\partial_k g(w)`，并称平移多项式的 support 为 `M^\\natural`-convex；引文为 `[Brä07, Theorem 5.6]`。300dpi 原图可见普通偏导、自然符上标及 `ä`。
- Markdown 现状：第 906 行把 `\\partial_j\\partial_k` 转为 `\\hat{\\sigma}_j\\hat{\\sigma}_k`；第 916 行将 `M^\\natural`-convex 错作 `M^\\circ`-convex；第 924 行引文键写作 `[Bra07¨, Theorem 5.6]`。
- 修复/复核：全篇审计后逐处恢复偏导算子、`M^\\natural` 与 `[Brä07]`，并按本页 300dpi 原图逐项复核；其余所列 Proposition 2.24 结论与 PDF p.21 文本层相符。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：在 augmentation-property 论证中将第二处 supppfq 恢复为 supp(f)；p.21 300dpi 原图确认印刷写作 supp(f)。


## p.022（PDF p.22 / 印刷 p.22）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:48 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p022.png`（150dpi，1-bit）。
- 核对：Proposition 2.24 二元情形与反例参数、Theorem 2.25 闭包/支持刻画、Example 2.26 ultra-log-concavity 定义及 no-internal-zeros 条件；按 born-digital 主通道与 PDF p.22 文本层逐项对账。
- 结果：PASS±（本页可见的微小排版痕迹未改命题或公式含义）。
- 印刷证据：Proposition 2.24 的下界、Theorem 2.25 两个包含方向、支持刻画及 Example 2.26 两项定义，均与 PDF p.22 文本层相符。
- 差异：第 970 行 “If” 被包在 `\\operatorname{If}` 数学标记中，属于可读的排版/OCR 痕迹；本页未发现改变系数、界、量词或集合条件的差异。

## p.023（PDF p.23 / 印刷 p.23）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:50 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p023.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p023_operators.png`（300dpi 原页）。
- 核对：no-internal-zeros 定义、Examples 2.27、projectivization、Theorem 2.28/Conjecture 2.29、strong/completely log-concave 定义至 Theorem 2.30 题头及脚注 8；微分算子/蕴含箭头以 300dpi 原图终裁。
- 结果：FAIL（差分算子和脚注中的条件引用被错录）。
- 印刷证据：PDF p.23 定义 `D_i` 为 `\sum_j a_{ij}\partial_j`；脚注 8 写 “an implication similar to (3) ⇒ (1) of Theorem 2.30”。300dpi 原图可辨偏导符和括号中的编号/箭头。
- Markdown 现状：第 1024 行把 `\partial_j` 写成 `\widehat{\boldsymbol O}_j`；第 1028 行将 `(3) ⇒ (1)` 写成 `p3q ñ p1q`。
- 修复/复核：全篇审计后逐处恢复 `\partial_j` 与 `(3) ⇒ (1)`，再依本页 300dpi 原图复核；其余所列定义、定理和例子与 PDF p.23 文本层相符。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：完全对数凹定义中的 m P N 恢复为 m∈N；依据 PDF p.23 原页文本。该补充不改变原 FAIL 判级。

## p.024（PDF p.24 / 印刷 p.24）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:52 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p024.png`（150dpi，1-bit）。
- 核对：Theorem 2.30 三个等价条件、Corollaries 2.31–2.32、乘积证明、Liggett 引用、Proposition 2.33 的三条等价条件和 Hessian 恒等式；文本层逐页对账。
- 结果：PASS±（内容和公式匹配，少量数学环境标记分段）。
- 印刷证据：PDF p.24 对应的 Theorem 2.30/Corollaries/Proposition 2.33 陈述及 Hessian 等式均与 Markdown 文本对应；未发现改变命题、系数、量词或矩阵次序的差异。
- 差异：第 1048 行 Liggett 引用的括号/标点被不规则数学标记拆开；第 1090 行 `H_{3,\epsilon}` 的 epsilon 用外置 `<sub>` 表示。均不改变所引文献或矩阵符号内容，不列为待修 FAIL。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：将 Corollary 2.32 题头的 strongly logconcave 恢复为印刷的 strongly log-concave；依 PDF p.24 文本层核对，保留 PASS±。

## p.025（PDF p.25 / 印刷 p.25）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:53 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p025.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p025_derivative.png`（300dpi 原页）。
- 核对：Proposition 2.33 证明 (3)⇒(1)、三种等价性总结、Theorem 2.30 两个方向的证明；最终方向导数以 300dpi 原图核定。
- 结果：FAIL（定理证明所需的方向导数写成错误算子）。
- 印刷证据：PDF p.25 末段要求证明 `\left(\sum_i a_i\partial_i\right)f` Lorentzian；300dpi 原图清楚显示每项是 `\partial_i`。
- Markdown 现状：第 1110 行将该和式写为含 `\hat{o}_i` 的算子，而不是 `\partial_i`；影响 Theorem 2.30 证明最后一步的具体对象。
- 修复/复核：全篇审计后逐处恢复方向导数 `\sum_i a_i\partial_i f`，再以本页 300dpi 原图核验；其他列出的闭包与 Hessian 论证公式相符。

## p.026（PDF p.26 / 印刷 p.26）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:56 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p026.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p026_operators.png`（300dpi 原页）。
- 核对：§3/§3.1 入口、degree-bounded and multi-affine polynomial spaces、projection/polarization operators and their map types, formulas, Proposition 3.1 and proof through the stability reduction.
- 结果：FAIL（两个线性算子签名的目标映射丢失）。
- 印刷证据：PDF p.26 projection operator 类型为 `R^a_κ[w_{ij}] \to R_κ[w_i]`，polarization operator 类型为 `R_κ[w_i] \to R^a_κ[w_{ij}]`；300dpi 原图清楚显示两个箭头及方向。
- Markdown 现状：第 1124 行和 1130 行在源空间与目标空间之间均未录入 `\to`/箭头，导致映射合同不完整；第 1132 行另有 `\\`/反引号格式噪声包住 “elementary symmetric polynomial” 描述。
- 修复/复核：全篇审计后逐处补回两个映射箭头并整理该行文本标记；以本页 300dpi 原图回核映射方向、变量和系数公式。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：Proposition 3.1 证明中的组合子集索引恢复为 [k choose d−2] 的竖式记号；以 p.26 300dpi 原图复核。

## p.027（PDF p.27 / 印刷 p.27）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 16:58 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p027.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p027_derivatives.png`（300dpi 原页）。
- 核对：Theorem 3.2 的线性算子/符号定义、Lemma 3.3 的分段定义及其证明至三个稳定性比较式；偏导符和 `\\prec` 用 300dpi 原图终裁。
- 结果：FAIL（符号名被拆坏；偏导算子与交错关系符多处误录）。
- 印刷证据：PDF p.27 写符号 `sym_T`，Lemma 3.3 的证明含普通偏导 `\\partial^S\\partial_1\\partial_2 f`，并在比较式中使用 `\\prec`。300dpi 原图确认这些排版。
- Markdown 现状：第 1184 行把 `sym_T` 拆成 `sy\\mathbf{m}_T`；第 1216 行把偏导写成带帽 `\\sigma/\\hat{o}`；第 1218、1220 行将 `\\prec` 写成普通 `<`。
- 修复/复核：全篇审计后逐处恢复 `sym_T`、偏导链和 `\\prec`；根据本页 300dpi 原图核对算子下标、指数和比较方向。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：删除 PDF p.28 不存在的独立 m=n 小字页脚碎片；完整 footnote 9 保留正确的 m=n。依据 p.28 300dpi 原图。

## p.028（PDF p.28 / 印刷 p.28）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 17:01 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p028.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p028_mapping.png`（300dpi 原页）。
- 核对：Lemma 3.3 证明收尾、Theorem 3.2 的 polarization 组合、符号公式、multi-affine 应用及 Theorem 3.4 开头条件；线性映射方向以 300dpi 原图终裁。
- 结果：FAIL（线性算子声明缺映射方向）。
- 印刷证据：PDF p.28 Theorem 3.2 proof 明确给出 `T : R_κ[w_i] \to R_γ[w_i]`；300dpi 原图可见源空间与目标空间之间的箭头。
- Markdown 现状：第 1224 行 polarization 定义中的 T 签名把两个函数空间直接相邻排写，缺少 `\to`，未说明映射的 codomain。
- 修复/复核：全篇审计后补回该映射箭头，并与本页 300dpi 原图核对 source/codomain 次序；其余所列偏导式和 polarization 符号公式与 PDF p.28 文本层对应。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：在 Remark 3.6 基集合定义中恢复漏修的 matroid on [n]；依据 p.29 300dpi 原图。

## p.029（PDF p.29 / 印刷 p.29）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 17:50 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p029.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p029_projective.png`（300dpi 原页）。
- 核对：Theorem 3.4 条件 (II)/(III) 与证明、Corollary 3.5、Remark 3.6 的 multi-affine matroid/projective-space 论述及归一化算子 N；符号/组合空间记号以 300dpi 原图终裁。
- 结果：FAIL（Theorem 3.4 的符号名称及 matroid 基集合的 projective 记号被损坏）。
- 印刷证据：PDF p.29 Case (II) 使用 `sym_T(w,u)`；Remark 3.6 将 rank-d matroid 的 bases 置于 `[n choose d]`，并用 `P L_n^d` 表示多仿射 Lorentzian 多项式空间的投影像。300dpi 原图可见这些符号。
- Markdown 现状：第 1290 行将 `sym_T(w,u)` 录成 `sym_{\\boldsymbol{\\mathbf{\\rho}}_T}(w,u)`；第 1306 行 bases 集合的 `\binom{[n]}{d}` 记号展成损坏的 `[ _d^n ]`；第 1312 行将 `P L_n^d` 误成带重复下划线的 `P\\underline{\\underline d}_n^d`，并重复损坏该基集合记号。
- 修复/复核：全篇审计后逐处恢复 `sym_T`、`[n choose d]` 与 `P L_n^d`；对照本页 300dpi 原图复核多仿射 matroid/support 表述，其他所列结论与 PDF p.29 文本层对应。

## p.030（PDF p.30 / 印刷 p.30）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 18:34 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p030.png`（150dpi，1-bit）。
- 核对：Corollaries 3.7–3.8、normalization operator N、associated symbol sums/products, linear maps T and S, and the Lorentzian-preservation reduction; complete PDF text layer page compared with corresponding Markdown passage.
- 结果：PASS。
- 证据结论：PDF p.30 的 factorial coefficients、summation bounds、variable exponents, mappings, and conclusion that the symbols are Lorentzian agree with the Markdown. No content-level discrepancy found in this page’s passage.
- 修复/复核：本页无需修复；完成全文修订后仍将按对应 PDF 页面回核。

## p.031（PDF p.31 / 印刷 p.31）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 19:19 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p031.png`（150dpi，1-bit）。
- 核对：symmetric exclusion process 背景与 `\Phi_\theta^{1,2}` 公式、Corollary 3.9、§3.2 generating function 定义及 Theorem 3.10 的条件 (1)–(8)；完整文本层逐页对账。
- 结果：PASS。
- 证据结论：PDF p.31 的交换公式、参数范围、八项等价条件和 matroid bases 结论与 Markdown 对应段落相符；未发现内容级差异。
- 修复/复核：本页无需修复；完成最终修订后再回核其对应 Markdown 内容。

## p.032（PDF p.32 / 印刷 p.32）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 19:54 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p032.png`（150dpi，1-bit）。
- 核对：basis-generating-polynomial 线索、Lemma 3.11、Theorem 3.10 证明及 p.32 结束处的 matroid 例证；文本层逐页对账。
- 结果：FAIL（2026-10-02 补充复核将初审 PASS 降级）。
- 证据结论（初审）：PDF p.32 的矩阵维数/取值、M-convex support、二次型分解、七条件蕴含链及 Lemma 3.11 证明与当时的 Markdown 对应内容相符；2026-10-02 补充复核发现漏项，见下方记录。
- 初审修复/复核：初审未发现差异，计划于全文修订后回核。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：PDF p.32 原页显示末段的 matroid ground set 为 [n]、Lemma 3.11 的矩阵 entries 为 {0,1}，且三处二次型均为 wᵀAw。原始 Markdown 中的 rns、t0,1u 与被拆开的 wᵀ/A/w 已逐处手工修复并对照页图复核；本页结果由 PASS 改为 FAIL。

## p.033（PDF p.33 / 印刷 p.33）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 20:20 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p033.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p033_map.png`（300dpi 原页）。
- 核对：Conjecture 3.12、§3.3 的 `M`-convex function 定义及两种交换条件、Example 3.13 指示函数、valuated matroid 有效域；函数映射箭头、范数条件和底集以 300dpi 原图终裁。
- 结果：FAIL（函数型别箭头、局部交换条件和底集记号多处损坏）。
- 印刷证据：PDF p.33 写 `|\alpha-\beta|_1=4`，两处函数型别均含 `\to`，且 valuated matroid 定义使用 ground set `[n]`；300dpi 原图确认数字、映射符号及方括号。
- Markdown 现状：第 1450、1474 行分别缺 `\to`；第 1466 行在等式右侧多出 `L`；第 1440、1444、1488 行以 `rns` 代替 `[n]`。
- 修复/复核：全篇审计后逐处补回映射箭头、恢复 `|\alpha-\beta|_1=4` 和 `[n]`，再依据本页 300dpi 原图核查。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：PDF p.33 印作 “When the effective domain of ν is is M-convex”；此重复词按印刷保留，作为源级 print quirk 登记。

## p.034（PDF p.34 / 印刷 p.34）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 20:50 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p034.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p034_functions.png`（300dpi 原页）。
- 核对：`f_q^ν/g_q^ν` 生成函数、Theorem 3.14 定义域与 q 范围、Example 3.15 的 M-natural 扩张、valuated matroid 秩生成函数及 Corollary 3.16；函数型别箭头和上标按 300dpi 原图裁决。
- 结果：FAIL（多个函数型别箭头丢失，M-natural 类别被写成数字 6）。
- 印刷证据：PDF p.34 在 `ν: Δ_n^d → R ∪ {∞}`、Example 3.15 的 `μ`/`ν` 类型均印有箭头；该例和随后秩函数明确使用 `M^\natural`-convex/concave；300dpi 原图可辨这些箭头和上标。
- Markdown 现状：第 1490、1498、1508 行相应函数类型缺 `→`；Example 3.15 及秩函数处将 `M^\natural` 写成 `M^6`，并有自然上标后多余句点。
- 修复/复核：全篇审计后逐处补回函数映射、恢复 `M^\natural`-凸/凹记号并移除错误句点；对照本页 300dpi 原图复核。

## p.035（PDF p.35 / 印刷 p.35）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 21:36 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p035.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p035_fields.png`（300dpi 原页）。
- 核对：Corollary 3.16 证明、反例多项式、收敛 Laurent/Puiseux series 字段及其 valuation、实闭域量词消去/Tarski 原理和 footnote 10；`K` 与 `\overline K` 的域标记以 300dpi 原图终裁。
- 结果：FAIL（实闭域与代数闭包被混为同一字段）。
- 印刷证据：PDF p.35 定义 `K` 为实系数 Puiseux-series 并另定义 `\overline K` 为复系数扩张；非零复系数 series 属于 `\overline K`，且原文明写 `\overline K` 代数闭、`K` 实闭。300dpi 原图的上划线清楚可见。
- Markdown 现状：第 1560、1566、1572 行在描述复系数 series、正元素和 valuation 前件时均写未加横线的 `K`；第 1578 行称 “K is algebraically closed, and K is real closed”，把代数闭扩张和实闭基域写成同一对象。
- 修复/复核：全篇审计后逐处恢复 `K`/`\overline K` 的域身份，并回看本页 300dpi 原图确认每个上划线；其他所列级数表达式和 Tarski 结论与 PDF p.35 对应。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：valuation 定义在 MinerU 初始 Markdown 中将零元的值误作 8，已按 PDF p.35 改为 ∞；p.35 fields 300dpi 原图可核。

## p.036（PDF p.36 / 印刷 p.36）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 22:27 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p036.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p036_fields.png`（300dpi 原页）。
- 核对：Definitions 3.17–3.18、Theorem 3.19 的 ordered-field 条件、实闭域与代数闭扩张的分工、稳定多项式 over the complex field 的定义及 footnote 11；所有 `K` 上划线以 300dpi 原图核定。
- 结果：FAIL（实闭基域与代数闭扩张的区分多处丢失）。
- 印刷证据：PDF p.36 说明 `K` real closed、`\overline K` algebraically closed；复系数 Laurent/Puiseux series、其 field elements 和 stable-polynomial domain 都使用 `\overline K`。300dpi 原图可见这些上划线。
- Markdown 现状：第 1624 行将 “Any element of `\overline K`” 写为 `K`；第 1630 行 polynomial domain、upper-half-plane domain 和 Brändén 引用处多处丢失 `\overline`，把复闭包写成实闭域 `K`。
- 修复/复核：全篇审计后逐处恢复 `\overline K` 与 `K` 的区分；按本页 300dpi 原图核对每个上划线和对应的 field role。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：恢复 Theorem 3.19 条件的 m∈ℕ；PDF p.36 300dpi 原图确认。

## p.037（PDF p.37 / 印刷 p.37）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 23:28 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p037.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p037_domain.png`（300dpi 原页）。
- 核对：Theorem 3.20 与 Dressian 的关系、Fano matroid 的稳定多项式例子、树距离函数的定义域和 Lemma 3.21、脚注 12；映射型别、组合子集记号及脚注内容以 300dpi 原图终裁。
- 结果：FAIL（组合子集定义域的映射箭头/记号损坏，Dressian 句与 Brändén 引文含伪字符，脚注 12 丢失关键公式和文字）。
- 印刷证据：PDF p.37 将树距离写为 `d : [\binom{n}{2}] → R`，Lemma 3.21 也以该型别量化；Dressian 定义在两处写 `R^B`，Fano 例的引用为 `[Brä07, Section 6]`。脚注 12 明确说以 `R{t}` 代替 `K` 后，每个 M-convex 函数都是 Lorentzian polynomial 的 tropicalization，并给出充要条件与 Dressian 的描述。
- Markdown 现状：第 1642 行第二个 `R^B` 前有多余 `¨`；第 1648 行把 `[Brä07]` 写成 `[Bra07¨]`；第 1678 行树距离定义域缺少 `→`；第 1690 行脚注 12 变成带缺文的 HTML 文本，遗失 `R{t}`、`R ∪ {∞}`、`ν` 等关键内容。
- 修复/复核：全篇审计后逐处恢复树距离型别、清除伪字符并按原文重建脚注 12；完成后对照本页 300dpi 原图复核。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：在 Dressian fan 句中将残留的 DrpMq 恢复为 Dr(M)；另外核对树距离定义域和边权类型、清除 Plücker 字样旁的杂散重音、删除非印刷脚注碎片并恢复 footnote 12 全文；依据 p.37 300dpi 原图。

## p.038（PDF p.38 / 印刷 p.38）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 23:44 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p038.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p038_proof.png`（300dpi 局部原页）。
- 核对：Lemma 3.21 的两项等价条件、距离函数与等距嵌入型别、Theorem 3.22–3.23、证明中稳定二次型和 M-convex 结论、脚注 13；类型箭头、引用重音及负号以 300dpi 裁片终裁。
- 结果：FAIL（两个函数型别箭头缺失，`[n]` 与 `E(d)` 多处损坏，引用字符和函数负号误识）。
- 印刷证据：PDF p.38 写 `d : [\binom{n}{2}] → R`、`φ : [n] → R^m`，矩阵项为 `E(d)_{ij}=d(i,j)^2`；证明得出 `−d` 为 M-convex，并引 `[Brä10, Theorem 4]`。300dpi 裁片确认重音及负号。
- Markdown 现状：第 1696 行距离函数型别缺 `→`，并将 `[n]` 写成 `rns`；第 1702 行嵌入映射缺 `→`；第 1708、1710、1720、1734 行的 `[n]` 多次写作 `rns`，第 1710 行 `E(d)` 写成 `Epdq`；第 1728 行 `[Brä10, Theorem 4]` 被破坏，且 `−d` 成为 `´d`；脚注 13 的 `[Brä10]` 也写作 `[Bra10 ¨]`。
- 修复/复核：全篇审计后逐处恢复函数型别、`[n]`、`E(d)`、负号和 `[Brä10]`；改后依据本页整页及 300dpi 裁片复核。

## p.039（PDF p.39 / 印刷 p.39）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 23:50 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p039.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p039_types.png`（300dpi 局部原页）。
- 核对：Lemma 3.21 证明的续段、Lemma 3.24、规范化多项式及 Proposition 3.25、polarization 的线性映射与定义域；函数类型和 `Π↑` 记号以 300dpi 裁片终裁。
- 结果：FAIL（一个函数类型箭头丢失，polarization 记号上标损坏）。
- 印刷证据：PDF p.39 对任意 `ν`、`μ` 均写出从 `Δ_n^d`/`Δ_m^d` 到 `R ∪ {∞}` 的映射；polarization 函数写 `Π^↑ν`。300dpi 裁片确认 `→` 与上箭头。
- Markdown 现状：第 1738 行把两处 `[n]` 写成 `rns`；第 1770 行 `ν : Δ_n^d → R ∪ {∞}` 丢失 `→`；第 1776 行将 `Π^↑ν` 写成 `Π<sup>Ò</sup>ν`。Lemma 3.24、规范化形式、`R_p(f)`、Proposition 3.25、`φ : R^m → R^n` 和下方 polarization 公式与印刷内容相符。
- 修复/复核：全篇审计后恢复 `[n]`、`ν` 的型别箭头和 `Π^↑`；完成后对照本页 150dpi 全页及 300dpi 裁片复核。

## p.040（PDF p.40 / 印刷 p.40）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-01 23:57 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p040.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p040_maps.png`、`audit/300dpi/Huh_2020_lorentzian_polynomials_p040_footnote.png`（300dpi 局部原页）。
- 核对：projection 定义、Lemma 3.26–3.27、辅助 `φ`/`ψ` 映射与 `ν_k` 构造、脚注 14；类型箭头、上标及脚注以 300dpi 裁片终裁。
- 结果：FAIL（多个函数型别箭头丢失，`Π^↑` 上标误识，定义域/无穷符号损坏，脚注 14 大段缺文）。
- 印刷证据：PDF p.40 将 `Π^↓μ`、Lemma 3.26 的 `ν`、以及 `ψ_*μ` 分别定义为有明确箭头的函数；Lemma 3.26(i) 使用 `Π^↑ν`。脚注 14 说明 polarization 将 `ν` 经 splitting of variables 并限制到 `[{m\choose d}]`，projection 将 `μ` 经 aggregation of variables 得到。
- Markdown 现状：第 1782、1790、1818 行对应类型缺 `→`；第 1792 行把 `Π^↑ν` 写成 `Π<sup>Ò</sup>ν`；第 1804 行 `dom(ν)` 变成 `dompνq`；第 1840 行脚注 14 丢失 `[{m\choose d}]`、polarization 输入 `ν` 和 projection 输入 `μ` 等内容。第 1836 行的 `∞`→`8` 位于跨页延续句的 p.41 部分，改列 p.41 审计。
- 修复/复核：恢复各映射箭头、`Π^↑`、`dom(ν)` 和脚注 14；`∞`→`8` 缺陷属于 PDF p.41，转在 p.41 登记；对照本页 150dpi 整页及相关 300dpi 裁片复核。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：Lemma 3.27 极限式恢复 “for all” 文本，并补足 ν_k 的 codomain 为 ℝ；依 PDF p.40 文本层及映射裁片核对。

## p.041（PDF p.41 / 印刷 p.41）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:09 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p041.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p041_proofs.png`（300dpi 局部原页）。
- 核对：Lemma 3.27 证明收尾、Theorem 3.20 的局部交换论证、Theorem 3.14 的三个特殊情形与极限步骤；`∞`、`[n]` 和 `[Brä10]` 以 300dpi 裁片终裁。
- 结果：FAIL（无穷符号与底集误识、引文损坏、证明句多出单词及杂散 `\AA`）。
- 印刷证据：PDF p.41 将延续句写为 `ν` 不恒等于 `∞`；交换论证使用 indices `p,q,r,s ∈ [n]` 并引 `[Brä10, Theorem 4]`；Theorem 3.14 段落写 `∂^α g_q^ν` “has exactly one positive eigenvalue”，且 `q<1, we have`。
- Markdown 现状：第 1836 行将 `∞` 识别为 `8`；第 1848 行把 `[n]` 写成 `rns`；第 1854 行 `[Brä10]` 被写作 `[Bra10 ¨]`；第 1862 行的 “is has exactly” 与 PDF 印刷一致，属于源级 print quirk 并保留；第 1886 行在 `q<1` 后插入 `\AA`。PDF p.41 本身重复印有 “such that such that”、“the the third special case” 和 “is has”，均按源级 print quirk 保留。
- 修复/复核：恢复 `∞`、`[n]`、`[Brä10]` 并删除 `\AA`；保留印刷重复词组及 “is has” 源级 quirk；对照本页整页及 300dpi 裁片复核。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：经 p.41 300dpi 原图复核，句中的 “is has exactly one positive eigenvalue” 与印刷一致，保留该 source-level quirk；∞、[n]、引文和 \AA 伪字符已按上条修复。

## p.042（PDF p.42 / 印刷 p.42）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:11 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p042.png`（150dpi，1-bit）。
- 核对：Theorem 3.14 证明收尾、Theorem 3.20 反向蕴含、Corollary 3.28 与其极限证明、§4.1 凸体体积函数定义；函数类型箭头和段末 QED 以原页核定。
- 结果：FAIL（一处函数型别箭头丢失，Corollary 3.28 证明的结束符号遗漏）。
- 印刷证据：PDF p.42 写 `ν : Δ_n^d → R ∪ {∞}`，且 Corollary 3.28 证明末尾印有 QED 方框；该页随后开始 §4.1，并给出 `vol_K : R_{≥0}^n → R` 的函数型别。
- Markdown 现状：第 1914 行首个 `ν : Δ_n^d → R ∪ {∞}` 缺 `→`；第 1932 行 Corollary 3.28 的证明结束处漏掉方框；第 1912 行把 `M-convex` 写成 `Mconvex`。其余该页的极限公式、极化、混合体积前置定义与原页相符。
- 修复/复核：补回第 1914 行箭头、段末方框并恢复术语连字符；完工后按 p.42 原图复核。

## p.043（PDF p.43 / 印刷 p.43）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:13 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p043.png`（150dpi，1-bit）。
- 核对：mixed-volume 展开与导数定义、Theorem 4.1–Corollary 4.2、线段独立集的 matroid 解释、体积多项式紧性论证及可表示 matroid 支持刻画。
- 结果：FAIL（基集 `[n]` 误识）；另有一处 Markdown 多余句点。
- 印刷证据：PDF p.43 把基生成多项式的 ground set 写作 `[n]`，并用 `J ⊆ [\binom{n}{d}]` 表示 d-子集索引；所有 mixed-volume 系数和极化导数公式均与原页相符。print 原文自身写 “The support ... is an M-convex” 和 “the set of basis”，均按源文保留。
- Markdown 现状：第 1978 行把 “matroid on `[n]`” 写作 “matroid on `rns`”；第 1976 行在 `R^d` 后多出句点，再接逗号。Corollary 4.2 的 “an M-convex” 与末段 “set of basis” 是原页措辞，不作 OCR 修复。
- 修复/复核：恢复第 1978 行 `[n]` 并移除多余句点；对照本页原图复核该基集及上列源级措辞。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：p.43 尾段 “matroid on [n]” 第二处漏记的 [n] 已恢复；本页原文 “an M-convex” 和 “the set of basis” 仍按印刷保留。

## p.044（PDF p.44 / 印刷 p.44）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:15 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p044.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p044_fields.png`、`audit/300dpi/Huh_2020_lorentzian_polynomials_p044_proof.png`（300dpi 局部原页）。
- 核对：Theorem 4.1 证明、Alexandrov–Fenchel 不等式、Proposition 4.4 系数不等式及其二次多项式证明、完整齐次形式与 Proposition 4.5 陈述；微分符号和交叉项以下方 300dpi 裁片终裁。
- 结果：FAIL（Proposition 4.4 证明中的偏导算子和交叉项下标损坏）。
- 印刷证据：PDF p.44 在 Proposition 4.4 证明中使用 `∂^{α−e_i−e_j} f`，双变量二次式中间项是 `c_α w_i w_j`；300dpi 裁片确认偏导符号和 `j` 下标。原文 Theorem 4.1 证明首段印作 `∂^α vol_H`，其后公式却用 `vol_K`；该 H/K 不一致按 print 保留。
- Markdown 现状：第 2016 行把 `∂^{α−e_i−e_j}` 写成带帽的 `\hat{o}^{α−e_i−e_j}`；第 2019 行把 `w_i w_j` 写成 `w_i w_+`。其余本页二次系数、外积不等式及齐次形式公式与印刷相符。
- 修复/复核：恢复偏导算子和 `w_j` 下标；保留原页的 `vol_H`/`vol_K` 不一致，并按整页与两处 300dpi 裁片复核。

## p.045（PDF p.45 / 印刷 p.45）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:18 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p045.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p045_hessian.png`、`audit/300dpi/Huh_2020_lorentzian_polynomials_p045_intersection.png`、`audit/300dpi/Huh_2020_lorentzian_polynomials_p045_nef.png`（300dpi 局部原页）。
- 核对：Proposition 4.5 证明、§4.2 交叉积的定义与性质、体积多项式和 Theorem 4.6；Hessian 记号、除子自交记号、Y 的标记与引文以 300dpi 裁片核验。
- 结果：FAIL（Hessian 字体标记、Y 标记及除子自交公式多处损坏）。
- 印刷证据：PDF p.45 使用 calligraphic `\mathcal H` 表示 Hessian，除子自交记号为 `(D)^d`，nef 定义和 Theorem 4.6 中均为 `Y`。第三项交叉积性质原文确实写 `D_1,…,D_n`，保留该 print 用字。
- Markdown 现状：第 2048、2054 行把 `\mathcal H` 写成普通 `H`；第 2062、2090 行将 `Y` 写成 `Y_\iota`；第 2074 行的 `(D)^d` 自交记号损坏为不可读的重音/上标片段，且 `Q-linear` 周围出现杂点；第 2088 行 `[Laz04, Section 1.4]` 引文边界损坏。第三项性质中的 `D_1,…,D_n` 与印刷一致。
- 修复/复核：恢复 Hessian calligraphic `\mathcal H`、无下标 `Y`、`(D)^d` 和 `[Laz04, Section 1.4]`；保留原页 `D_1,…,D_n` 用字，按本页整图与 300dpi 裁片复核。

## p.046（PDF p.46 / 印刷 p.46）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:20 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p046.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p046_remark.png`（300dpi 局部原页）。
- 核对：Corollary 4.7 的支集刻画、Remark 4.8 的系数和基集合、Theorem 4.6 证明及 Question 4.9 的前两问；句界和 [HW17] 引文以 300dpi 裁片终裁。
- 结果：FAIL（句间标点丢失，[HW17] 引文括号损坏）。
- 印刷证据：PDF p.46 在 “…on Y.” 后明确结束一句，再起 “Corollary 4.7 implies …”；Remark 4.8 引文为 `[HW17, Section 4]`。300dpi 裁片确认引文括号及节号。
- Markdown 现状：第 2102 行在 `on Y` 后缺少句点，直接连成 `Y Corollary 4.7`；第 2104 行 `[HW17, Section 4]` 被破坏为未闭合的上标/方括号片段。源文 “mutiprojective” 是印刷拼写，MinerU 忠实保留，按源级 quirk 处理。
- 修复/复核：恢复句点与 `[HW17, Section 4]` 引文；保留源文 “mutiprojective”，按本页整图及 300dpi 裁片复核。

## p.047（PDF p.47 / 印刷 p.47）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:23 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p047.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p047_footnote.png`（300dpi 局部原页）。
- 核对：Question 4.9 的后两问与已知低维等式、§4.3 Potts/Tutte 多项式定义、脚注 15 的 Lorentzian cubic 及 reverse Khovanskii–Teissier 不等式；底集、引文和脚注公式以 300dpi 裁片终裁。
- 结果：FAIL（matroid ground set 误识，Potts 引文损坏，脚注 15 多处碎裂且关键公式不可读）。
- 印刷证据：PDF p.47 写 matroid on `[n]`，图模型引文为 `[Sok05]`；脚注 15 明列 `f=14x^3+6x^2y+24x^2z+12xyz+6xz^2+3yz^2`，并给出含 `\binom{d}{k}`、各 divisor intersection products 的反向 Khovanskii–Teissier 不等式。
- Markdown 现状：第 2154 行把 `[n]` 写成 `rns`；第 2166 行 `[Sok05]` 分裂为 `Sok0` 与游离数字；第 2174–2182 行脚注 15 被分割成多个 docvortex 碎片，三次方多项式中的加号变为 grave，闭包对象/句子片段错位，组合系数与交叉积公式也被破坏。第 2150 行 `n≥4` 后的逗号与 PDF 印刷一致，应保留为源级标点。
- 修复/复核：恢复 `[n]`、`[Sok05]`、脚注 15 全文与三次多项式/不等式；保留印刷逗号，按本页整图和 300dpi 裁片逐项复核。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：PDF p.47 中 n≥4 后的逗号确为印刷标点，已在 Markdown 保留；不再将其列为 OCR 错误。

## p.048（PDF p.48 / 印刷 p.48）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:24 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p048.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p048_Mnatural.png`（300dpi 局部原页）。
- 核对：Theorem 4.10、Lemmas 4.11–4.12、二次型与稳定性判据；关键系数、指数、支集和边界条件逐项对照。
- 结果：PASS±（唯一差异为 `M^natural` 上标里的多余句点，未改变命题或不等式）。
- 印刷证据：PDF p.48 的 `M^natural` 凹性陈述、`{0,1}^n` 支集、Lemma 4.12 不等式，以及 Theorem 4.10 归约得到的判别式不等式均与 Markdown 内容一致；300dpi 裁片确认 `M^natural` 上标没有句点。
- Markdown 现状：第 2184 行写作 `M^{natural.}-concave`，比印刷多一个上标句点。其余本页的 Theorem/Lemma 陈述、变量类型、收缩导数、二次型系数及 `q` 范围相符。
- 修复/复核：移除 `M^natural` 上标内多余句点；按本页整图和 300dpi 裁片复核。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：Lemma 4.12 的 m≤n 细节已纳入 p.48 补充记录；此处后续结论无新差异。

## p.049（PDF p.49 / 印刷 p.49）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:27 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p049.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p049_conjecture.png`（300dpi 局部原页）。
- 核对：Theorem 4.10 证明中的 loop/parallel-class 变量代换与二次型、Mason Conjecture 4.13 三个不等式及其归一化形式；底集与第三条不等式的因子以下方 300dpi 裁片终裁。
- 结果：FAIL（ground set `[n]` 误识，Conjecture 4.13(3) 多出一个下标）。
- 印刷证据：PDF p.49 两处将 matroid 的 ground set 写为 `[n]`；Conjecture 4.13(3) 的右端仅有两个比值因子 `(k+1)/k` 与 `(n−k+1)/(n−k)`，没有额外的下标或因子。300dpi 裁片确认。
- Markdown 现状：第 2274 行把 `[n]` 写成 `rns`；第 2280 行在末项 `I_{k+1}(M)` 后多出 `Ω`。其余 loop 代换、parallel classes、Lemma 4.12 化简及归一化不等式与原页相符。
- 修复/复核：恢复第 2274 行 `[n]` 并删除第 2280 行多出的 `Ω`；完成后对照本页原图与 300dpi 裁片复核。

## p.050（PDF p.50 / 印刷 p.50）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:41 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p050.png`（150dpi，1-bit）。
- 核对：Theorem 4.14 及其证明、matroid Tutte polynomial、`c_q^k(M)` 系数表示、§4.4 的 M-matrix 定义与前三项等价条件、脚注 16。
- 结果：FAIL（两个 ground set `[n]` 误识，引文边界/格式损坏）。
- 印刷证据：PDF p.50 的 Theorem 4.14 和 Tutte polynomial 定义均使用 matroid on `[n]`；§4.4 首段引文为 `[BP94, Chapter 6]`。页中 `c_q^k(M)` 的上下标次序与归一化式相符，脚注 16 也完整印出。
- Markdown 现状：第 2292、2316 行将 `[n]` 写成 `rns`；第 2330 行 `[BP94, Chapter 6]` 的字母间距、括号及数学分隔符破损。其余 Theorem 4.14 的归一化不等式、极限、Tutte 多项式展开与 `c_q^k(M)` 系数记号相符。
- 修复/复核：恢复第 2292、2316 行 `[n]` 和 `[BP94, Chapter 6]` 引文；对照本页原图复核并检查 `c_q^k(M)` 的上下标次序。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：Theorem 4.14 证明解释句中的独立集族名字 IpMq 恢复为 I(M)；依据 p.50 原页图。

## p.051（PDF p.51 / 印刷 p.51）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:43 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p051.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p051_symbols.png`（300dpi 局部原页）。
- 核对：M-matrix 等价条件续列、multivariate characteristic polynomial、Theorem 4.15、Corollary 4.16、Lemma 4.17 支集证明及 doubly sub-stochastic 定义。
- 结果：PASS±（引用语法和 `M^natural` 上标有轻微排版损坏，数学陈述仍可辨）。
- 印刷证据：PDF p.51 引用为 `[Hol05, Theorem 4]`，Lemma 4.17 证明称支集为 `M^natural`-convex；支集 `{0,1}^n`、主子式正性和行列和界均与 Markdown 对应。
- Markdown 现状：第 2358 行 `[Hol05, Theorem 4]` 的方括号/上标语法不齐；第 2370 行 `M^natural` 上标内多一个句点。没有发现定理条件、行列和不等式或支集陈述的内容差异。
- 修复/复核：清理引文上标格式与 `M^natural` 上标句点；按 p.51 原图及 300dpi 裁片复核。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：修复后的 M-natural 上标与 p.51 print 一致；保留 PASS± 原评级。

## p.052（PDF p.52 / 印刷 p.52）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:45 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p052.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p052_matrices.png`、`audit/300dpi/Huh_2020_lorentzian_polynomials_p052_congruence.png`（300dpi 局部原页）。
- 核对：Lemma 4.18 的 `M_n/N_n` 与扩维块矩阵、`L_{n+1}/K_{n+1}` 构造和第一次对称消元；矩阵端点、分数、零位、省略行符号逐项对照。
- 结果：FAIL（K 矩阵省略行符号误识，正文矩阵下标多出一位）。
- 印刷证据：PDF p.52 的 K 矩阵中间省略行使用竖向省略号 `⋮`；归纳段称 `L_{n+1}` 与 `K_{n+1}`，没有附加下标 `1`。300dpi 裁片亦确认 M/N、扩维和消元矩阵中的系数与 Markdown 相符。
- Markdown 现状：第 2409 行 K 矩阵省略行多处写成 `\vdash`，应为 `\vdots`；第 2412 行 `L_{n+1}` 后插入孤立 HTML `<sub>1</sub>`。其余所列矩阵的数值项及 Schur-complement 末端 `n/2−1/4` 与印刷一致。
- 修复/复核：恢复 K 矩阵的 `\vdots` 与 `L_{n+1}` 下标；修复后对照本页两张 300dpi 裁片复核矩阵全部行列。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：在 p.52 的 K-matrix congruence 说明中恢复了与原图一致的 ≃（congruence）符号；与 K 矩阵省略号/下标修复一并核对。

## p.053（PDF p.53 / 印刷 p.53）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:48 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p053.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p053_elimination.png`、`audit/300dpi/Huh_2020_lorentzian_polynomials_p053_partialperm.png`（300dpi 局部原页）。
- 核对：Lemma 4.18 的 `\underline M/\underline N` 消元矩阵与正半定归纳收尾、Proposition 4.19 的块矩阵、partial permutation 的循环/链块分解及证明结尾；矩阵数字逐项按 300dpi 裁片比对。
- 结果：FAIL（Lemma 4.18 归纳收尾的关键矩阵记号与断句损坏）。
- 印刷证据：PDF p.53 写明 “Since `L_n` is positive semidefinite, `\underline M_{n+1}` is congruent to the sum of two positive semidefinite matrices”；其余 `\underline M_{n+1}`/`\underline N_{n+1}` 消元项、`C_{n+1}` 块矩阵和两类 partial-permutation block 均可由 300dpi 裁片核验。
- Markdown 现状：第 2426 行该句出现双逗号及游离 `Mn+` 片段，`\underline M_{n+1}` 标记被破坏，无法可靠读出印刷中的半正定归纳结论。所列消元矩阵和 Proposition 4.19 部分的系数、排列块与原页相符。
- 修复/复核：恢复 `\underline M_{n+1}` 归纳结论完整句；逐项复核本页两张 300dpi 矩阵裁片。

## p.054（PDF p.54 / 印刷 p.54）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:50 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p054.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p054_sign.png`（300dpi 局部原页）。
- 核对：Theorem 4.15 证明中的主子式展开、导数归约、判别式不等式与对角缩放；末端矩阵恒等式及 doubly sub-stochastic 矩阵定义以 300dpi 裁片终裁。
- 结果：FAIL（末句中 `−B` 的负号丢失）。
- 印刷证据：PDF p.54 得到 `I_n − B − (1/n)J_n` 后，随即说明 `−B` 是对称 doubly sub-stochastic 矩阵。300dpi 裁片确认文字中的 `−B` 明确有负号。
- Markdown 现状：第 2490 行把 `−B` 写成带重音的 `´B`，丢掉使其成为非负矩阵的负号；第 2472 行另将 `hypothesis` 拼成 `hypotheis`。
- 修复/复核：恢复 `−B` 的负号并更正 `hypothesis` 拼写；对照本页整图和 300dpi 裁片复核。

## p.055（PDF p.55 / 印刷 p.55）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:52 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p055.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p055_rayleigh.png`（300dpi 局部原页）。
- 核对：§4.5 概述、分布的 partition function、PNC/ULC/strongly Rayleigh 定义、external-field 变换、1-Rayleigh 与 c-Rayleigh 条件、Definition 4.20 及 M-matrix 示例。
- 结果：FAIL（两条 Rayleigh 不等式中的偏导算子被替换为错误字形）。
- 印刷证据：PDF p.55 的 strong Rayleigh 与外场后的 1-Rayleigh、c-Rayleigh 公式均使用 `∂_i∂_j Z_μ` 和 `∂_i Z_μ, ∂_j Z_μ`；300dpi 裁片确认偏导符号。
- Markdown 现状：第 2530、2534 行把 1-Rayleigh/c-Rayleigh 不等式中的 `∂_i∂_j`、`∂_i`、`∂_j` 识别成 `\hat\sigma_i\hat\sigma_j` 等带帽 sigma 组合。强 Rayleigh 定义本身（第 2519 行）正确保留了偏导；其余概率定义和 Definition 4.20 内容相符。
- 修复/复核：在第 2530、2534 行恢复偏导算子；按本页整图和 300dpi 裁片逐项复核不等式左右两端。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：p.55 的 PNC 与 strong-Rayleigh 定义中两处漏录的 ground set [n] 已恢复；以 p.55 rayleigh 裁片复核。

## p.056（PDF p.56 / 印刷 p.56）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:55 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p056.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p056_ulc.png`、`audit/300dpi/Huh_2020_lorentzian_polynomials_p056_measures.png`（300dpi 局部原页）。
- 核对：Propositions 4.21–4.25、ULC/外场论证、strongly Rayleigh 蕴含、matroid 上的 `μ_M/ν_M` 定义及 Kahn–Grimmett–Winkler 事件不等式；赋值符号和分式参数以 300dpi 裁片终裁。
- 结果：FAIL（`ν_M` 定义处等号误识、Kahn 猜想句碎裂，另有引文标记损坏）。
- 印刷证据：PDF p.56 明确用 `ν_M =` 定义均匀基分布；Kahn–Grimmett–Winkler 句印作 “states that, if `F` is a forest …”；Proposition 4.24 引文为 `[Brä07, Theorem 5.6]`。300dpi 裁片均可辨。
- Markdown 现状：第 2566 行把 `ν_M =` 写成引号字符；第 2578 行将 “states that, if” 破坏为 `tha…t, if` 的插入碎片；第 2560 行 `[Brä07, Theorem 5.6]` 重音/上标/方括号格式损坏。第 2552 行反复出现 `w_1/w_0` 的 ULC 齐次多项式参数与原页 print 一致，属于源级 quirk，不作 OCR 修正。
- 修复/复核：恢复 `ν_M =`、Kahn 猜想句及 `[Brä07, Theorem 5.6]`；保留第 2552 行与 print 一致的重复变量，按整页及两张 300dpi 裁片复核。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：Proposition 4.25 的 “matroid M on [n]” 漏录底集，已按 PDF p.56 恢复；同页还完成 ν_M=、Kahn 句和引文修复，保留重复 w₁/w₀ print quirk。

## p.057（PDF p.57 / 印刷 p.57）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 00:58 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p057.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p057_references.png`（300dpi references 原页裁片）。
- 核对：Kahn–Grimmett–Winkler 结论过渡句、References 标题及 `[AHK18]` 至 `[FM92]` 的作者、题名、刊物/卷页/年份、arXiv 标识和文内引用页码。
- 结果：FAIL（多条参考文献的重音、单词间距及题名字符损坏）。
- 印刷证据：300dpi 原页裁片逐条显示 References 中的 Brändén/Brä07/Brä10 重音、Montaño、Tomás、标题空格与引用信息；页首 Kahn–Grimmett–Winkler 的两句正文与 Markdown 相符。
- Markdown 现状：第 2590、2592、2594 行多个题名丢词间空格；第 2596、2598 行分别把 “Mathematics” 拆成 “Math ematics”、把 “related functions” 粘成 “relatedfunctions”；第 2602–2614 行 Brändén/Brä07/Brä10 等作者重音与 citation keys 被拆裂；第 2618 行多出重音标记且 “multidegrees” 少 `s`、Montaño 丢 `ñ`；第 2620 行 “the” 丢 `e`；第 2624 行 Montréal 丢重音且 “Math. 8” 前多重音符；第 2628 行 Tomás 丢重音并在 “Balanced matroids” 前多出重音符。
- 修复/复核：按印刷原页逐项恢复这些作者重音、reference keys、题名空格/字母与字符；对照 300dpi 裁片复核所有条目。

## p.058（PDF p.58 / 印刷 p.58）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 01:00 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p058.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p058_references.png`（300dpi references 原页裁片）。
- 核对：References `[FK72]`–`[KMT07]` 的作者与重音、题名、期刊/书系、卷页年份和文内引用页码。
- 结果：FAIL（多条文献题名、作者重音和刊名标点误识）。
- 印刷证据：300dpi 原页裁片确认 `[GKL19]` 的 `G/P`、Jiří、Salaün、Jürgen、Schröter、Mészáros 等拼写，以及相关题名词间空格；原页也印 `SIAM J. Discrete Math. 21 (2007), no. 1`。
- Markdown 现状：第 2640 行把 `[GKL19]` 题名中的 `G/P` 写成 `G{P`；第 2642、2650、2656、2666、2670 行作者重音碎裂；第 2642、2650、2668、2678 行题名丢空格；第 2695 行刊名多一个 `SIAM.` 句点，`no.1` 少空格。另有多个非必要重音符残留在参考文献字段中。
- 修复/复核：按 PDF p.58 恢复 G/P、作者重音、断开的词和 `SIAM J. Discrete Math., no. 1` 标点；对照本页 references 300dpi 裁片复核各条。

- 补充复核（2026-10-02 04:48 EDT；Peer-P25，gpt-6-luna/max）：PDF p.58 references 中 [Ful93] 的跨行词 “Lec-tures” 合并为 “Lectures”，且 [KN11] 的 “property for” 词界恢复；按 p.58 300dpi 裁片核对。

## p.059（PDF p.59 / 印刷 p.59）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 01:02 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p059.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p059_references.png`（300dpi references 原页裁片）。
- 核对：References `[Laz04]`–`[Spe05]` 的作者、题名、出版信息、重音和文内引用页码。
- 结果：FAIL（[LX17] 的期刊名称重音严重损坏，另有多条书目词间距/字符错误）。
- 印刷证据：300dpi 原页裁片显示期刊名 `Épijournal de Géométrie Algébrique`，并确认 [Lig10] 的 “American”, [Sch14] 的 “Mathematics”, [She60] 的 “convex sets” 与 [Shi12] 的 “rank functions” 均保持正确分词。
- Markdown 现状：第 2686 行将 `[LX17]` 期刊名重音碎裂并插入多余上标；第 2694 行把 “American” 拆为 `Amer ican`；第 2720 行把 “Mathematics” 拆为 `Mathe matics`；第 2730 行 `of convex` 粘成 `ofconvex`；第 2732 行 `rank functions` 粘成 `rankfunctions`。其余本页主要出版项和页码相符。
- 修复/复核：恢复 Épijournal/Géométrie Algébrique 重音与上述四处词界；逐条对照本页 300dpi references 裁片复核。

## p.060（PDF p.60 / 印刷 p.60）

- actor：Peer-P25；model=`gpt-6-luna`；effort=`max`。
- 时间：2026-10-02 01:05 EDT。
- 原页证据：`audit/Huh_2020_lorentzian_polynomials_p060.png`（150dpi，1-bit）；`audit/300dpi/Huh_2020_lorentzian_polynomials_p060_references.png`（300dpi references 原页裁片）。
- 核对：References `[TV83]`–`[Zha85]` 与作者单位/电子邮件；参考文献题名中的重音和条目边界以 300dpi 裁片核对。
- 结果：FAIL（Yau78 题名重音编码损坏，且 `[TV83]` 与上一条目粘连）。
- 印刷证据：PDF p.60 的 `[Yau78]` 题名写 `Kähler` 与 `Monge–Ampère`，并有单独的 `[TV83]` 条目；本页机构地址及两个 email 与 Markdown 相符。
- Markdown 现状：第 2736 行把上一页末尾 `[Spe05]` 与本页首条 `[TV83]` 拼在同一行，缺少条目边界；第 2746 行把 `Kähler` 写成 `K¨ahler`、把 `Ampère` 写成带 grave 的 `Amp\`ere`。
- 修复/复核：分开 `[Spe05]` 与 `[TV83]` 条目，恢复 Yau78 的变音符；按 p.60 整页及 300dpi 裁片复核参考文献和机构行。

## 修复登记

- 记录时间：2026-10-02 05:03 EDT；actor=Peer-P25；model=gpt-6-luna；reasoning effort=max。
- 候选范围：仅本 worktree 的 Huh_2020_lorentzian_polynomials MinerU Markdown 与本审计文件。状态仍为 CANDIDATE_NOT_CURRENT / UNINTEGRATED；没有修改根 README、MEMORY、feature-list、rulings、AUDIT-INDEX 或 AUDIT-PROGRESS.log；未 push。
- 原始 MinerU 输入：导出 commit `ce11d92fd5c5a412de2d8f31c1415b9f9f8951ac`；修复前 SHA-256 `b2356501bfe781074b8cfca4ebb442037fc5dcb2a3ba155cb2c31dea621d3928`。
- Source repair commits：`e625e15a19be01f7a08d9564db320c2149e8a133`（逐处内容修复）与 `ca581cd8106e84fc763a9c9648f45ef7199d06d3`（后续删除 p.3/p.28 不存在的页脚碎片并恢复 log-concave 连字符）。第一提交后的 source SHA-256 为 `95eda60c006677443a8ff66503476234f4650e4cf2fe3754f60e97210417255e`；最终 source HEAD 为 `ca581cd8106e84fc763a9c9648f45ef7199d06d3`，最终 Markdown SHA-256 为 `3c3a4525baccad14f29fd1c1044302ac491aa257a102ee4eee9a1f6d6e1a150e`。
- 最终复核：在最后一次 source 修改后，从头到尾重读全部 2,724 行；PDF 为 60 页，配套 150dpi 页图计数为 60。手工修复依据相应 PDF 页图/300dpi 裁片及 born-digital 文本层；只读 `git diff --check` 通过。定向残余扫描未发现本次修复的 `rns`、`supppfq`、`m P N`、`DrpMq`、`t0,1u`、`m ď n`、`IpMq`、`Lec tures` 或 `propertyfor` 等错录残留。未运行测试套件；此工作是逐页转录核对。
- 逐页补充覆盖的漏项包括：p.3 非印刷 `PL_n^d` 页脚碎片；p.11 的 `d=3`；p.16 Proposition 2.17 的普通 “If”；p.18–21 的方向短语和 `supp(f)`；p.23/p.36 的 `m∈N`；p.26 的组合子集索引；p.28 非印刷 `m=n` 碎片；p.29/p.32/p.43/p.55/p.56 的 `[n]` 或 ground set；p.32 的 `{0,1}` 与 `w^T A w`；p.35 的 `val(0)=∞`；p.37 的 `Dr(M)`、树距离型别/边权和 footnote 12；p.40 的 `for all` 与 ν_k codomain；p.48 的 `m≤n`；p.50 的 `𝓘(M)`；p.52 的 congruence 符号；p.58 的 References 词界。
- 60 个页面评级合计：FAIL 54、PASS± 4、PASS 2。p.32 从初审 PASS 按补充证据降级为 FAIL；PASS± 页保留原评级。
- 按印刷保留的 source-level quirks：p.16 的 `i∈.[n].`；p.33 的 “if satisfies” 与 “is is”；p.41 的 “such that such that”、“the the third special case” 与 “is has”；p.43 的 “an M-convex” 与 “the set of basis”；p.44 的 `vol_H`/`vol_K` 不一致；p.45 印作 `D_1,…,D_n` 的交叉积条款；p.46 的 “mutiprojective”；p.47 `n≥4` 后的逗号；p.56 ULC 齐次式中的重复 `w_1/w_0`。这些均由相应页面证据核定为印刷原文，未按数学预期擅改。
