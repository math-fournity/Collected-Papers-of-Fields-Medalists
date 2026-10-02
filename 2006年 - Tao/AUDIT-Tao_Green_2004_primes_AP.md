# AUDIT — Tao_Green_2004_primes_AP

> 状态：`CANDIDATE_NOT_CURRENT`；本篇候选审计由 Peer-P22 负责，canonical current state 由 Master-Luna 维护。
> Actor：`Peer-P22`；model：`gpt-6-luna`；reasoning effort：`max`。
> 基线：worktree HEAD `037602429d3b009f6fc468c732073eb3ddf9875f`（与任务指定基线一致）；开始时观察到 `refs/heads/main=e864b3b9dffc3456435c4bd5d0cd7553b3cd4cb8`。本篇 PDF、目标 Markdown、审计路径及 Tao 专属证据名前缀在两者间无差异。
> 源 PDF：`2006年 - Tao/Tao_Green_2004_primes_AP.pdf`；`pdfinfo` 为 56 页，Creator `LaTeX with hyperref package`，Producer `dvips + GPL Ghostscript SVN PRE-RELEASE 8.62`。完整文本层为 201,451 字符、56 个非空页、0 个 U+FFFD；按 born-digital 模式逐页以文本层为主，标题页及 1–2 页密集数学页目检，疑似符号差异以源页图/300dpi 裁片终裁。
> 源 PDF SHA-256：`d03dd6156165fc92e488b3fec35a574c8f7c9df55125cec0f3eebdf95d7256e1`。
> 修复前 MinerU Markdown SHA-256：`e7aaed689d5f085f381d57f296041ea7bde01e4d79a3cf351eb2ce150435fd92`。
> 当前唯一目标 Markdown：`2006年 - Tao/Tao_Green_2004_primes_AP_mineru/Tao_Green_2004_primes_AP__Tao_Green_2004_primes_AP.md`。PDF 与其它 MinerU 资产只读；本文件不修改根 `AUDIT-INDEX.md` 或 `AUDIT-PROGRESS.log`。

## 逐页审计

### PDF p.1/56（印刷 p.1）

- 时间：2026-10-01T16:24:13-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p001.png`（pngmono，150 dpi；标题页目检）；计数表达式终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p001_counting-expression.png`（源页 PNG，300 dpi 灰度裁片）。
- 对账范围：标题、作者、摘要、引言第 1–3 段及页脚的 1991 Mathematics Subject Classification 和资助说明；文本层按 PDF p.1 对照 Markdown 对应段落，标题页另作目检。
- 结果：**FAIL**。印刷文本层与 300 dpi 裁片均给出计数启发式 `≫ N² / logᵏ N`，后接 “k-tuples”；Markdown 第 13 行却写成 `\gg \bar { N ^ { 2 } } / \log ^ { k }` 并把分母末尾的 `N` 置于数学环境外、与后面的 `k-tuples` 粘连。这会改变公式转录，须在完成全篇审计后用 Edit 逐处修复。裁片明确显示 `N` 上无横线。
- 伴随差异（不另升 FAIL）：摘要 `suficiently` 少一个 `f`，引言 `diference` 少一个 `f`；二者仍可辨读，属拼写级 OCR 瑕疵，按 PASS± 记录且不作为数学公式错误。PDF 的 arXiv 页眉 `arXiv:math/0404188v6 [math.NT] 23 Sep 2007` 与印刷页码未收入 Markdown；正文、题名、作者和两条页脚说明均有对应内容。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.2/56（印刷 p.2）

- 时间：2026-10-01T16:29:01-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p002.png`（pngmono，150 dpi；因公式/数值差异目检）；终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p002_progressions-limsup-density.png`（300 dpi 灰度）。
- 对账范围：第 1 节收尾，包括两条已知素数等差数列、Theorem 1.1–1.2、随机子集密度下界、Acknowledgements；文本层逐页对账，并以全页图和 300 dpi 裁片核疑点。
- 结果：**FAIL**。两条印刷等差数列中的数字在 Markdown 第 24、30 行被逐位插入空格，例如印刷 `56211383760397 + 44546738095860k; k=0,1,…,22` 被写为 `5 6 2 1 … + 4 4 5 4 … k; …, 2 2`，第二条也同样被拆开；不能忠实表示印刷中的整数。Theorem 1.2 的上密度公式还多出 `\stackrel { , } { \phantom { = } }` 伪结构，源页为 `lim sup_{N→∞}`；后文 `N^{-1/2+\bar{ε}}` 多了印刷中不存在的 ε 横线。上述数值/公式差异须在全篇审计后逐处修复。
- 伴随差异：`diferent`（different）和 `Radclife`（Radcliffe）各少一个 `f`，属可辨读拼写级 OCR 瑕疵，记录为 PASS±，不与公式 FAIL 混同。PDF 的页眉作者行和印刷页码未收入 Markdown；Theorem 1.1–1.2 的文字陈述、相关人名/引文及致谢段落主体存在。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.3/56（印刷 p.3）

- 时间：2026-10-01T16:36:46-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p003.png`（pngmono，150 dpi；本篇密集数学页视觉抽验）；300 dpi 灰度裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p003_bourgain-bound.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p003_w-trick.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p003_footnote1.png`。
- 对账范围：第 2 节中 Proposition 2.1、Gowers/Rankin/Bourgain 上下界、Erdős 猜想、W-trick 说明、过渡到 Theorem 1.1–1.2 的段落及脚注 1；逐页文本层对照，并目检密集页及相关裁片。
- 结果：**FAIL**。Bourgain 上界在 Markdown 第 71 行写作 `\hat{N_0}(δ,3)`，印刷 p.3 与裁片均为 `N_0(δ,3)`，不存在帽符号。脚注 1 的正文（Markdown 第 89 行）在 “work in … rather than the more traditional …, since we are free to divide by …” 等关键位置漏掉 `\mathbb{Z}_N`、`[-N,N]`、`2,3,…,k` 等公式对象；这些对象被分拆为第 79、81、83、85、87 行的孤立 footnote 片段，不能组成印刷页上的完整句子。另 Markdown 第 63 行在 “W-trick” 两侧插入伪上标 `66` 和 `3` 并拆开字母，而 PDF 文本层与 p.3 300 dpi 裁片只印普通 “W-trick”。三项均在修复提交中逐处修复。
- 伴随差异：`diference`、`suficiently`、`estimimates` 为可辨读拼写瑕疵，列为 PASS± 候选；签页时未编辑 Markdown。running head 和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.4/56（印刷 p.4）

- 时间：2026-10-01T16:39:38-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p004.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：第 2 节中 Proposition 2.1 后的过渡、Szemerédi 定理的两种形式、Proposition 2.3 的陈述及其公式 (2.2)–(2.3)、Remark 起始部分，以及页脚 2、3。
- 结果：**PASS±**。Proposition 2.3 的参数、假设、两条不等式及结论与印刷文本层相符；页脚 2 和 3 的实质内容均有转录。印刷页在 “Another difference, if one unravels…” 处跨页续句，Markdown 同一段落继续记录后续内容，未发现该页结束处的内容缺失。
- 轻微瑕疵：`ergodictheoretical` 连写，`diferences` 少一个 `f`，页脚 `sufice`/`lef` 分别少字母；页脚 3 中等差关系公式另以独立 footnote span 出现，公式本身仍保留但位置脱离句内。页眉作者行和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.5/56（印刷 p.5）

- 时间：2026-10-01T16:41:47-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p005.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；脚注 4–5 终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p005_footnotes4-5.png`（300 dpi 灰度）。
- 对账范围：Proposition 2.3 的 Remark 收尾、定义测度 (2.4)、伪随机测度说明、von Mangoldt 函数与主化论证、脚注 4–5。
- 结果：**FAIL**。脚注 4 的印刷原文把 `\nu_{\mathrm{const}}` 和 `\nu` 都明确置于 `\mathbb{Z}_N` 上，并说明后者可集中在 `\mathbb{Z}_N` 的稀疏子集；Markdown 第 141 行把这些集合记号拆漏/错位（第 137、139 行仅残留孤立的 `νconst`、`Z_N`），致使脚注句子无法正确转录。脚注 5 的印刷定义为 `W = \prod_{p<w(N)} p`，而 Markdown 第 143 行把 “where W=…” 公式拆成 `and`、上下标碎片与 `Qp<w(N)`，不能忠实表示该乘积定义。两处均待全篇审计后逐处手工修复。
- 伴随差异：`dificulty` 少一个 `f`，其余正文和 (2.4) 的实质内容与源文本层相符。页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.6/56（印刷 p.6）

- 时间：2026-10-01T16:44:22-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p006.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：majorant 段落收尾、归一化算术级数计数 (2.5)、Gowers uniformity/anti-uniformity 的说明、第 3 节标题及初始记号；脚注 6–8。
- 结果：**PASS±**。公式 (2.5)、dual norm 说明及第 3 节标题与源文本层一致。PDF p.6 正文在 “we will write `o(1)` for” 处跨页续接；Markdown 第 161 行继续同一段，续页部分留待下一页核对。
- 轻微瑕疵：Markdown 把 “Gowers uniformity norms” 拆成字母间空格，脚注 7 中 `different` 少一个 `f`，并有全角逗号/数学环境边界伪影；本页未见改变公式陈述的差异。页眉作者行与印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.7/56（印刷 p.7）

- 时间：2026-10-01T16:46:22-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p007.png`（pngmono，150 dpi；本篇第二张密集数学页视觉抽验）；终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p007_asymptotic-and-map-arrows.png`（300 dpi 灰度）。
- 对账范围：o(1)/O(1) 记号说明（承接 PDF p.6）、有限集上的平均定义、Definition 3.1 及公式 (3.1)、Examples (3.2)–(3.3)。
- 结果：**FAIL**。Markdown 第 161 行将 “a quantity that tends to zero as `N→∞`” 记作 `N \infty`，漏掉极限箭头；第 169 行把印刷 `f:A→R` 写成 `f:A R`，漏掉类型映射箭头。300 dpi 裁片确认两处印刷箭头清晰存在，须在全篇审计后逐处修复。其余 Definition 3.1 与 (3.1)–(3.3) 的文字/公式在已覆盖的 p.7 范围内相符。
- 伴随差异：Markdown 第 161 行 `k _ { : }` 含多余冒号；字母及环境分隔伪影另作 PASS± 候选，不改变上述 FAIL 判定。该段在 PDF p.6–7 间跨页，p.7 从前页末尾 “for” 后接续；本页最后的 (3.3) 后文留待 p.8 核对。页眉标题与印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.8/56（印刷 p.8）

- 时间：2026-10-01T16:48:57-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p008.png`（pngmono，150 dpi；本页复杂公式/脚注疑点目检）；300 dpi 灰度裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p008_equation3-4-and-parameters.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p008_footnotes9-10.png`。
- 对账范围：p.7 公式 (3.3) 的“for all x”续句、公式 (3.4) 及参数注记、Definition 3.2 与 (3.5)–(3.6)、Remarks 的本页部分、脚注 9–10。
- 结果：**FAIL**。公式 (3.4) 后的参数组在 Markdown 第 209 行为 `(1 2, 5, 2)`，印刷为 `(12, 5, 2)`；Definition 3.2 第 213 行误写 `m_0^{-}` correlation condition，源文只有 `m_0`。正文第 211 行把 `\psi_j(x)` 错转为含双点/粗体的 `\ddot{\boldsymbol\psi}_j(x)`，改变了所指函数。
- 脚注 9–10 也有实质内容丢失：印刷脚注 9 明确给出消除局部相关性的 “W-trick”，Markdown 第 245 行在 “simple … which we will come to later” 处漏掉该术语；脚注 10 印有样本空间 `{1,…,N}`、Bernoulli 权重的取值 `ν(x)`、概率 `1/log N`，以及界 `O(1)` / `O(log^m N)`（互异/非互异 `h_j`），Markdown 第 247 行相应位置留空或脱位。300 dpi 裁片确认源文细节。上述项待全篇审计后逐处修复。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉作者行和印刷页码未收入 Markdown；本页最后的 “arithmetic” 后续段落归入 PDF p.9。

### PDF p.9/56（印刷 p.9）

- 时间：2026-10-01T16:51:22-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p009.png`（pngmono，150 dpi；复杂上标疑点目检）；参数终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p009_correlation-exponent.png`（300 dpi 灰度）。
- 对账范围：第 3 节相关条件的说明、Definition 3.3、随机子集例子、Lemma 3.4 及证明、Theorem 3.5 开头。
- 结果：**FAIL**。Definition 3.3 印刷为 `2^{k-1}`-correlation condition；Markdown 第 251 行把它拆写成 `<sup>k</sup>−<sup>1</sup>`，即 `2^k−1`，改变了本篇伪随机性的参数规格。300 dpi 裁片和 PDF 文本层共同确认印刷上标包含 `k−1`。
- 伴随差异：`sufice`/`diferent` 为少字母的可辨读拼写瑕疵；Lemma 3.4 的核心式 `(ν+ν_const)/2=(ν+1)/2` 与源文相符。页眉标题和印刷页码未收入 Markdown；Theorem 3.5 的句子在 PDF p.9 页末续至 “Let”，Markdown 段落继续该句，后半句留待 p.10 核对。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.10/56（印刷 p.10）

- 时间：2026-10-01T16:52:38-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p010.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：Theorem 3.5 的假设、(3.7)–(3.9) 与收尾说明，第 4 节标题和 Definition 4.1 的 L^q 范数、内积及指示函数定义。
- 结果：**PASS±**。Theorem 3.5 的参数、三条公式及 Section 4 的定义、公式编号与源文本层相符；定理句从 PDF p.9 续入 p.10 的部分无缺失。
- 轻微瑕疵：`en courage`、`N has being`、`Thoughout` 分别对应印刷的 “encourage”、“N as being”、“Throughout”，是拼写/分词级噪声，不改变本页公式含义。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.11/56（印刷 p.11）

- 时间：2026-10-01T16:54:13-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p011.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；映射符号裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p011_uniform-cover-arrow.png`（300 dpi 灰度）。
- 对账范围：uniform cover 定义与 (4.1)、第 5 节导言、Definition 5.1、(5.1)、d=2 示例、正性论证及 (5.2)、脚注 11。
- 结果：**FAIL**。uniform cover 的源定义明确为映射 `Φ:A→B`；Markdown 第 307 行写成 `Φ:A B`，漏失映射箭头。300 dpi 裁片确认箭头清晰存在。公式 (4.1)、(5.1) 和 (5.2) 在本页文本层对账范围内相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.12/56（印刷 p.12）

- 时间：2026-10-01T16:56:17-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p012.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：正性结论 (5.3)、Gowers uniformity norm 定义 (5.4)、Gowers Cauchy–Schwarz 与三角不等式 (5.5)、d=2 示例、U² 范数的 Fourier 表达式，至 PDF p.12 页末。
- 结果：**PASS±**。本页对账范围内的公式、上下标和编号与 PDF 文本层一致；Markdown 在 “When `f_ω` does depend on `ω_d`” 后多出一个句点，属轻微标点噪声。页末 Fourier 身份之后的文字归入 PDF p.13，未在本页定级。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.13/56（印刷 p.13）

- 时间：2026-10-01T16:57:40-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p013.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：Fourier 变换定义及脚注 12、恒等式 (5.6)、单调性关系 (5.7)、Lemma 5.2 及证明展开式 (5.8)–(5.10)。
- 结果：**PASS±**。本页已覆盖的公式、幂次、集合指标及编号与 PDF 文本层相符；Theorem/lemma 证明在页末以 (5.10) 的线性形式表达收尾，Markdown 同段继续后页内容，后续留待 p.14 核对。
- 轻微瑕疵：Markdown 第 457 行 `sufices` 少一个 `f`；脚注 12 的 `rˆole` 重音字形编码不规整但词可辨读。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.14/56（印刷 p.14）

- 时间：2026-10-01T16:59:13-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p014.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：Lemma 5.2 证明收尾、二项式消去、Proposition 5.3 陈述及 (5.11)，随后是证明的起始步骤、(5.12)–(5.13) 与 k=3 特例的引入。
- 结果：**PASS±**。表达式 (5.9)–(5.13)、参数范围及 Proposition 5.3 的结论与 PDF 文本层相符。印刷页在 k=3 特例 “Our task is to show that” 后跨页；Markdown 后接的显示公式留待 p.15 核对。
- 轻微瑕疵：Markdown 第 503 行关于 `[19, Theorem 3.2] or` 的数学环境/标点被拆乱；c_j 候选集合中的 `k−1` 也被断开排写，但字符顺序仍可恢复，未见定理陈述被改变。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.15/56（印刷 p.15）

- 时间：2026-10-01T17:01:23-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p015.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：(5.13) 的证明起始、k=3 重参数化、J₀/J₁/J₂ 定义、两次 Cauchy–Schwarz 估计及 (5.14)–(5.15)。
- 结果：**PASS±**。本页被覆盖的变量变换、指数、平均变量与 (5.14)–(5.15) 和 J₂ 展开均与源文本层一致；PDF 页末为 J₂ 的定义，Markdown 后续段落留待 p.16 核对。
- 轻微瑕疵：Markdown 第 542 行公式末多出不可见分隔符 `\right.` 及句点，印刷公式没有该尾缀；公式主体可辨且未改变估计内容。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.16/56（印刷 p.16）

- 时间：2026-10-01T17:48:27-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p016.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：J₂ 与 U² 的比较、权重 W 定义 (5.16)、误差控制及 (5.17)–(5.19)、Lemma 5.4 陈述。
- 结果：**PASS±**。公式 (5.16)–(5.19) 的变量、因子、指数、条件集合和不等式方向与印刷文本层相符；Markdown 中 `\phi_0,…,\phi_{k-1}` 的函数型签名附近漏冒号/标点，域和陪域仍可由相邻文本辨认。PDF 页末止于 Lemma 5.4 的 (5.19)，其后的 Remarks 归入 p.17。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.17/56（印刷 p.17）

- 时间：2026-10-01T18:55:07-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p017.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；索引裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p017_cauchy-index.png`（300 dpi 灰度）。
- 对账范围：Lemma 5.4 Remarks、(5.20)、Lemma 5.4 证明的 G/H 分解、Cauchy–Schwarz 步骤以及 (5.21)–(5.22)。
- 结果：**FAIL**。Lemma 5.4 证明在印刷 p.17 明确写 `\phi_{k-d-1}` 不依赖变量 `y_{k-d-1}`；Markdown 第 647 行却写成 `y<sub>k</sub>$-d-1`，把下标拆为 `k` 后再减 `d+1`，改变证明中被平均/外提的变量索引。300 dpi 裁片确认源页下标为整体 `k-d-1`。该索引须全篇审计后逐处修复。其余本页 (5.20)–(5.22) 对账相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown；Proposition 5.3 的后续证明归入 p.18。

### PDF p.18/56（印刷 p.18）

- 时间：2026-10-01T20:01:17-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p018.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：Proposition 5.3 的一般证明，函数 `φ_i` 构造、均匀覆盖映射 `Φ`、公式 (5.23)–(5.25) 及权重 W(x,h) 的两种表达。
- 结果：**PASS±**。本页变量变换、`Φ:Z_N^{k-1}→Z_N^2`、幂次、乘积指标和 (5.23)–(5.25) 均与 PDF 文本层相符；页末 U^{k−1} 范数恒等式对应 Markdown 第 746 行，之后的论述留待 p.19 核对。
- 轻微瑕疵：Markdown 第 743 行对向量记号 `ωh∈Z_N^{k-1}` 的数学环境边界排写不规整，定义其分量的文字仍在；未见改变本页数学陈述的差异。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.19/56（印刷 p.19）

- 时间：2026-10-01T20:36:23-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p019.png`（pngmono，150 dpi；复杂变量列表疑点目检）；终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p019_q1-q2-variable-lists.png`（300 dpi 灰度）。
- 对账范围：(5.25) 之后证明 Lemma 5.5 的 q=0、1、2 三组线性形式，以及 Lemma 5.5/Proposition 5.3 收尾、Section 6 开头和 (6.1)。
- 结果：**FAIL**。Markdown 第 783 行与第 789 行在 q=1/q=2 的变量列表中分别插入额外字符 `2`（写成 `h_1,…,h_{k-1} 2 y_1,…`）；印刷与 300 dpi 裁片均为 `h_1,…,h_{k-1}, y_1,…`，没有该数字。错误改变了线性形式条件应用时所列变量，须全篇审计后逐处修复。其余 q 参数组、形式族、(5.21)–(5.22) 和 (6.1) 在本页核对范围内相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.20/56（印刷 p.20）

- 时间：2026-10-01T21:08:59-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p020.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：Gowers anti-uniformity 引言、(6.1)–(6.5)、dual function (6.3)、Lemma 6.1 的两个恒等式及其假设 `|F(x)|≤ν(x)+1`。
- 结果：**PASS±**。上述范数、乘积指标、指数和身份与 PDF 文本层相符；PDF p.20 在 `|F(x)|≤ν(x)+1` 后跨页，Markdown 后续的 (6.6) 留待 p.21 核对。
- 轻微瑕疵：Markdown 第 811 行把 `uniformity` 拆成 “uni formity”，并在页脚 13 前出现孤立 `[10,13];` 片段；footnote 13 的正文仍在。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.21/56（印刷 p.21）

- 时间：2026-10-01T22:10:50-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p021.png`（pngmono，150 dpi；dual-function/footnote 疑点目检）；300 dpi 灰度裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p021_dual-function-footnote-marker.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p021_footnote15-orders.png`。
- 对账范围：Lemma 6.1 证明末尾与 (6.6)、关于多项式相位的 Remarks、(6.7)、脚注 14–15。
- 结果：**FAIL**。印刷原文在 `then` 后的上标 `14` 是脚注标号，随后为 `DF=F`；Markdown 第 883 行却转为 `\nabla^{14}\mathcal{D}F=F`，引入了源页不存在的梯度算子与指数。脚注 15 的印刷原文两次说明阶数 `k−2`（Gowers anti-uniform functions 与 polynomial eigenfunctions），Markdown 第 897 行两处均留空；`k−2` 只以孤立片段出现于第 889、891、893 行，未构成脚注句意。裁片确认这些内容及标号位置。两项待全篇审计后逐处修复。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题与印刷页码未收入 Markdown。

### PDF p.22/56（印刷 p.22）

- 时间：2026-10-01T23:15:29-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p022.png`（pngmono，150 dpi；Proposition 6.2 视觉抽验）；300 dpi 裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p022_prop6-2-contract.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p022_compact-domain.png`。
- 对账范围：Lemma 6.1 的上界 (6.6)、多项式相位 remarks、(6.7)、Proposition 6.2 的类型/紧集/均匀估计、其证明前置及 Lemma 6.3 陈述。
- 结果：**FAIL**。Proposition 6.2 第 913 行把印刷类型 `\Phi:I^K\to\mathbb R` 写成 `\Phi:I^K\mathbb R`，漏失映射箭头。第 925 行把连续函数定义域写为 `\breve I^K`，而印刷为 `I^K`；同一行还把小写渐近项 `o_{K,\Phi}(1)` 写成大写 `\mathcal O_{K,\Phi}(1)`，改变了结论的渐近强度。300 dpi 裁片确认箭头、无 breve 的定义域和小写 `o`。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉作者行和印刷页码未收入 Markdown。

### PDF p.23/56（印刷 p.23）

- 时间：2026-10-01T23:48:11-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p023.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：Lemma 6.3 的多项式 dual norm 界证明，包括 (6.9)、Gowers Cauchy–Schwarz、Hölder 指数与 uniform-cover 变量替换。
- 结果：**PASS±**。乘积展开、H 函数、指数 `2^{k-1}-1`、变量变换及 (6.9) 与 PDF 文本层相符；p.23 页末在均匀覆盖后将期望改写为 `g_{u^{(1)},…,u^{(K)}}` 的 U^{k−1} 范数，Markdown 对应至第 1008 行，未发现符号/指标差异。
- 轻微瑕疵：正文有重复 `that that`、`coeficients`/`sufices` 拼写噪声和多余逗号；不改变本页证明公式。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.24/56（印刷 p.24）

- 时间：2026-10-02T00:12:09-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p024.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：Lemma 6.3 证明从 Hölder/均匀覆盖到相关条件估计的完成，以及 Proposition 6.2 证明中 Weierstrass 逼近和首个误差界。
- 结果：**PASS±**。p.24 覆盖的范数幂次、均匀覆盖、相关条件、(6.8) 用法和 `(2+o(1))ε` 界与 PDF 文本层相符；PDF 页末在该误差界处结束，后续项留待 p.25。
- 轻微瑕疵：Markdown 第 999 行 `Fix ω..` 多一个句点，`sufices` 少一个 `f`；不改变估计内容。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.25/56（印刷 p.25）

- 时间：2026-10-02T00:18:16-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p025.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；dual norm 裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p025_dual-norm-remark.png`（300 dpi 灰度）。
- 对账范围：Proposition 6.2 证明收尾、关于 dual norm 与 Wiener norm 的 Remarks、(6.7) 推论、第 7 节引言及 Definition 7.1 的页内部分。
- 结果：**FAIL**。印刷在 Remarks 中写抽象 dual norm `\|\cdot\|_{(U^{k-1})^*}`，PDF 换行后仍是同一 norm 记号；Markdown 第 1075 行却出现 `\parallel`、不完整竖线及 `\mathcal L` 片段，缺少作为范数对象的 `\cdot`，不能忠实转录该数学量。300 dpi 裁片确认源页记号。待全篇审计后逐处修复。
- 伴随差异：同段 `Weiner` 拼作 Wiener 的 OCR 瑕疵；p.25 上本次覆盖范围内其余公式、Young 不等式和第 7 节标题/引言与文本层相符。页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.26/56（印刷 p.26）

- 时间：2026-10-02T00:23:21-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p026.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；300 dpi 裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p026_sigma-definition.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p026_prop7-2-map.png`。
- 对账范围：Definition 7.1 可测函数与条件期望/代数 join 说明、Proposition 7.2 条件和三项性质、证明至估计 (7.3)。
- 结果：**FAIL**。Markdown 第 1087 行把可测 level sets 应属于 `B` 写为 `B_{;}`；第 1097 行把 join 写成 `\bigvee_{i=1}^K B_j`，求和下标与代数索引不一致；第 1111 行把印刷类型 `\Psi_A:I\to[0,1]` 写成 `\Psi_A:I[0,1]`，漏失映射箭头。300 dpi 裁片确认 (7.2) 的箭头与源页一致。以上差异影响可测性/σ-代数/函数型转录，待全篇审计后逐处修复。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.27/56（印刷 p.27）

- 时间：2026-10-02T00:41:53-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p027.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p027_cutoff-and-sigma-join.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p027_small-atom-average.png`（300 dpi 灰度）。
- 对账范围：Proposition 7.2 证明收尾及截断函数定义、Proposition 7.3 的 σ-代数 join、(7.4)–(7.8) 和“小 atom”判据。
- 结果：**FAIL**。Markdown 第 1133 行把印刷映射 `\psi_\eta:\mathbb R\to[0,1]` 写成 `\psi_\eta:\mathbb R[0,1]`，漏映射箭头；第 1137 行的 join 将末项写成 `\widetilde{\mathcal B}_{\varepsilon,\eta}(\mathcal DF_K)`，印刷为未加 tilde 的 `\mathcal B_{\varepsilon,\eta}(\mathcal DF_K)`；第 1157 行小 atom 条件多了 `\dot{\mathbb E}` 上点，印刷为普通期望 `\mathbb E`。裁片确认三处均无相应附加符号/记号。以上改变函数型、σ-代数对象或小 atom 条件，待全篇审计后逐处修复。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown；证明在 “easy induction argument” 后续接至 p.28。

### PDF p.28/56（印刷 p.28）

- 时间：2026-10-02T00:47:28-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p028.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；型签名裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p028_psi-map-and-equation.png`（300 dpi 灰度）。
- 对账范围：Proposition 7.3 证明尾段、Remark、Section 8 标题、Proposition 8.1 及 (8.1)–(8.3)、相关理论类比段落。
- 结果：**FAIL**。Proposition 7.3 证明中印刷类型 `\Psi_A:I^K\to[0,1]`，Markdown 第 1175 行写成 `\Psi_A:I^K[0,1]`，漏失函数映射箭头；300 dpi 裁片确认箭头清晰存在。(8.1)–(8.3) 的幂次、集合和估计方向在文本层对账范围内相符。
- 伴随瑕疵：Markdown 第 1190 行期望式末尾多一个右括号，第 1193 行写 `depending in K`（印刷 `depending on K`），属于排版/文字噪声；页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.29/56（印刷 p.29）

- 时间：2026-10-02T00:54:46-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p029.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；脚注终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p029_footnote16.png`（300 dpi 灰度）。
- 对账范围：Theorem 3.5 由 Proposition 8.1 推出部分的函数分解、级数计数估计、截去例外集后的函数计数下界、算法终止说明及脚注 16。
- 结果：**FAIL**。脚注 16 印有 `f_{U^\perp}≤1+o_ε(1)`、密度下界 `δ−o_ε(1)`、通过修改 `f_{U^\perp}` 并付出 `o_ε(1)` 误差来应用 Proposition 2.3 的说明。Markdown 第 1273 行把这些数学量和误差位置留空；相关 token 虽有部分作为第 1259–1271 行的孤立 footnote span 出现，却未保留在脚注句子的论证关系中。300 dpi 裁片确认源文，需全篇审计后逐处修复。正文 (8.1)–(8.3) 及后续计数公式在本页核对范围内相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.30/56（印刷 p.30）

- 时间：2026-10-02T01:00:46-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p030.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：Theorem 3.5 证明所需的算法终止叙述、footnote 17、Proposition 8.2 的前提与 (8.4)–(8.10)。
- 结果：**PASS±**。Proposition 8.2 中 ν/F_j 的界、异常集条件、`ε^{1/2^k}` 的非 uniformity 门槛和能量准备估计均与 PDF 文本层相符；PDF 页末到 (8.10) 为止，Markdown 后续内容留待 p.31。
- 轻微瑕疵：Markdown 第 1325 行有孤立 `k,` 片段，脚注 17 正文仍完整；正文 `suficiently` 少一个 `f`。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.31/56（印刷 p.31）

- 时间：2026-10-02T01:07:52-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p031.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；sigma-algebra 索引裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p031_step3-omega.png`（300 dpi 灰度）。
- 对账范围：(8.11)–(8.15)、能量增量说明、K₀ 迭代上界及 Step 0–3 的算法描述。
- 结果：**FAIL**。Step 3 中印刷为 “exceptional set `Ω_{K+1} ⊃ Ω_K` in `B_{K+1}`”；Markdown 第 1379 行在 `B_{K+1}` 后多出 `<sub>1</sub>`，变成另一 σ-代数标识。300 dpi 裁片确认印刷没有该下标。其余 (8.11)–(8.15) 的界、能量增量指数及 K₀ 上界在本页核对范围内相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown；Step 3 后续归入 p.32。

### PDF p.32/56（印刷 p.32）

- 时间：2026-10-02T01:13:15-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p032.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；脚注终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p032_footnote18.png`（300 dpi 灰度）。
- 对账范围：Step 4 与算法终止讨论、能量 E_K 和 (8.16)、Proposition 8.1 的终止结论、Proposition 8.2 证明开头及脚注 18。
- 结果：**FAIL**。脚注 18 印刷为 “K will ultimately be bounded by K₀, which depends only on ε and k”；Markdown 第 1421 行在 “bounded by … which depends only on ε and k” 之间漏掉 `K₀`，虽有第 1415–1419 行的孤立片段 `00`、`K`、`K₀,`，但未保留脚注句中的变量关系。300 dpi 裁片确认原文为 `K₀`。其余 (8.16) 的增量系数、能量上下界和 Proposition 8.2 证明入口在本页范围内相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉作者行和印刷页码未收入 Markdown。

### PDF p.33/56（印刷 p.33）

- 时间：2026-10-02T01:19:51-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p033.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；下标核验裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p033_K-index.png`（300 dpi 灰度）。
- 对账范围：(8.11)–(8.19)，Proposition 8.2 的能量增量证明至 Cauchy–Schwarz 下界。
- 结果：**PASS±**。(8.11)、(8.17)–(8.19) 的变量、幂次及误差项与 PDF 文本层相符。源页在列举 `DF_1,…` 时写作 `DF_{K_1+1}` 并使用 `O_{K_1,ε}`，而之前的合同/式子主要写 K；300 dpi 裁片确认这是印刷页本身的 K₁ 记号，Markdown 忠实保留，作为源级 notation quirk 记录，不改正文。
- 修复状态：本页无 Markdown FAIL；签页时未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.34/56（印刷 p.34）

- 时间：2026-10-02T01:27:21-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p034.png`（pngmono，150 dpi；能量论证目检）；300 dpi 灰度裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p034-energy-expression.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p034-orthogonality-index.png`。
- 对账范围：能量增量 (8.15) 的 Pythagoras 展开、近似正交性、条件期望投影与 Proposition 8.2 收尾。
- 结果：**FAIL**。Markdown 第 1508 行展开左端平方范数时，第二个增量项 `E(f|B_{K+1})−E(f|B_K)` 后缺少一个右括号；印刷式在范数符号前有闭合括号。第 1529 行又把应为 `E(f|B_K)` 的条件期望写作 `E(f|\bar B_K)`，增加了印刷中不存在的 B 横线；300 dpi 裁片确认源式不带横线。这两处损坏能量分解/正交性论证的公式转录，待全篇审计后逐处修复。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉作者行与印刷页码未收入 Markdown。

### PDF p.35/56（印刷 p.35）

- 时间：2026-10-02T01:33:34-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p035.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：第 9 节开头、von Mangoldt 函数和拟随机主化的动机、W-trick、修正 von Mangoldt 函数定义、脚注 19–20。
- 结果：**PASS±**。`\Lambda` 的定义、主化条件、`W=\prod_{p\leq w(N)}p`、`\widetilde\Lambda(n)` 的分段定义和 W-trick 的解释与印刷文本层相符；本页在 “distribution of the primes in arithmetic progressions” 处跨页，后续未计入本页。
- 轻微瑕疵：Markdown 第 1567 行 `N _ { ; }` 是 `N` 的多余空子标记；脚注 19 的 `K=0` 被拆为独立 footnote span（第 1577 行），脚注正文相应缺少该位置；另有 `dificulty`、`afecting`、`ethis` 拼写/分词噪声。这些不改变本页主要数学定义，列为 PASS±。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.36/56（印刷 p.36）

- 时间：2026-10-02T01:42:09-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p036.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；300 dpi 灰度裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p036-epsilon-k.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p036-footnote21.png`。
- 对账范围：Dirichlet 和式续句、Proposition 9.1 的 ε_k 和主化下界、Theorem 1.1 推论、退化 r=0 贡献界、von Mangoldt 的 Möbius 恒等式及脚注 21。
- 结果：**FAIL**。脚注 21 印刷给出 `\sum_{N\le n\le2N}\Lambda(n)\gg N`，并说明以 `n ≡ b (mod W)`（b 与 W 互素）替换 `n ≡ 1 (mod W)`；Markdown 第 1619 行的和式区间与两处同余条件脱落/错位，仅剩第 1611、1613、1615、1617 行彼此分离的片段，无法忠实转录脚注论证。300 dpi 裁片确认了完整求和区间及两类剩余类。
- 伴随记录：ε_k 的印刷字面形式为 `1/2^k(k+4)!`，Markdown 以同一顺序表示；因原件使用 inline slash，本条不额外推断/规范化分母分组。Proposition 9.1 主化常数和主文其余被覆盖公式与文本层相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.37/56（印刷 p.37）

- 时间：2026-10-02T01:51:18-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p037.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；线性形式索引裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p037_linear-forms-indices.png`（300 dpi 灰度）。
- 对账范围：Definition 9.2–9.3、Lemma 9.4 及证明、Proposition 9.5 的线性形式范围/定义、公式主项和 Remarks。
- 结果：**FAIL**。Proposition 9.5 印刷条件为 `1≤i≤m`，Markdown 第 1645 行把首项 `1` 转为 `\mid`；同一行线性形式求和印刷为 `\sum_{j=1}^{t}L_{ij}x_j+b_i`，Markdown 却写成 `\sum_{i=1}^{t}L_{ij}x_j+b_i`，把求和变量 `j` 错换为自由指标 `i`。300 dpi 裁片确认两项源字符。它们改变线性形式族的定义，待全篇审计后逐处修复。
- 伴随记录：ε_k 的 inline slash 表示沿用源页字符顺序，不在本次审计中猜测或规范化分母结合方式；Lemma 9.4 主化系数、interval 和 Proposition 9.5 的渐近主项与文本层相符。页眉标题与印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.38/56（印刷 p.38）

- 时间：2026-10-02T02:04:25-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p038.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；300 dpi 裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p038_R10m.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p038_psi-sum-index.png`。
- 对账范围：Proposition 9.6 的间隔长度、Δ 与 (9.1)，Lemma 9.7，Proposition 9.8 及其证明开头和 (9.2)。
- 结果：**FAIL**。Proposition 9.6 印刷间隔长度为 `R^{10m}`，Markdown 第 1657 行写为 `R^{\dot{1}0m}`，多出 1 上方的点号；Proposition 9.8 证明第 1693 行把线性形式定义中的求和写为 `\sum_{i=1}^{t}L_{ij}x_j+b_i`，源页为 `\sum_{j=1}^{t}L_{ij}x_j+b_i`。300 dpi 裁片确认无点号且求和指标为 j。两处分别改变区间参数和线性形式定义，待全篇审计后逐处修复。
- 伴随差异：(9.1)、Lemma 9.7 与 (9.2) 在本页文本层核对范围内相符；页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.39/56（印刷 p.39）

- 时间：2026-10-02T02:12:30-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p039.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；300 dpi 裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p039_majorant-factors.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p039_footnote22.png`。
- 对账范围：Proposition 9.8 的箱体局部化、nice/non-nice tuple 估计、(9.2) 局部性论证及 footnote 22。
- 结果：**FAIL**。Markdown 第 1721 行把主化因子 `\theta_i(x)` 加成点号形式 `\dot\theta_i(x)`；第 1722 行把 `\phi(W)` 多加横线写作 `\bar\phi(W)`。此外，footnote 22 印刷写明需从 `\psi_i` 减去 N 的倍数，Markdown 第 1747 行对应句写成 “subtract a multiple of N from in the formula below”，丢失了对象 `\psi_i`；相关符号只以第 1735–1745 行的孤立片段出现。两张 300 dpi 裁片确认源页分别无额外点/横线及 footnote 对象 `\psi_i`。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.40/56（印刷 p.40）

- 时间：2026-10-02T02:18:57-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p040.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；权函数裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p040-tau-weight.png`（300 dpi 灰度）。
- 对账范围：非 nice tuple 的比例估计、Lemma 9.9 的权函数 τ_m 构造及其 q 阶矩估计。
- 结果：**FAIL**。Lemma 9.9 证明的印刷定义为 `τ_m(n):=O_m(1)∏_{p|n}(1+p^{-1/2})^{O_m(1)}`；Markdown 第 1779 行把两个 `O_m(1)` 分别加成 `\bar 1` 和 `\bar{O}_m(1)`。300 dpi 裁片确认印刷均无横线；这改变/破坏了权函数定义中的渐近常数，待全篇审计后逐处修复。本页其余非 nice tuple 占比与平均矩公式在核对范围内相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.41/56（印刷 p.41）

- 时间：2026-10-02T02:23:27-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p041.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：Lemma 9.9 的约数和矩估计收尾、Proposition 9.10 相关条件陈述、重复 h_i 的情形及 g(n) 展开。
- 结果：**FAIL**。在处理重复 h_i 的情形时，印刷证明称需粗略估计不等式 (9.3) 的左端；Markdown 第 1819 行错误引用 (9.2)（线性形式条件），而不是本页所证的相关条件不等式 (9.3)。该错引会把读者引向不同主张，属于证明引用错误。其余 (9.3)、τ(0) 和 g(n) 的表达与本页文本层相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.42/56（印刷 p.42）

- 时间：2026-10-02T02:30:12-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p042.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；线性形式索引裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p042_psi-coordinate-sum.png`（300 dpi 灰度）。
- 对账范围：Proposition 9.10 的求和展开、Proposition 9.1 收尾、Section 10 开头、Proposition 9.5 的重述与式 (10.1)–(10.2) 前的周期性论证。
- 结果：**FAIL**。Section 10 第 1853 行重述线性形式时，印刷定义为 `\psi_i(x)=\sum_{j=1}^{t}L_{ij}x_j+b_i`；Markdown 写成 `\sum_{i=1}^{t}L_{ij}x_j+b_i`，把坐标求和指标 j 换成自由指标 i。300 dpi 裁片确认印刷求和下标为 j，该差异会改变线性形式定义。式 (9.3)、Lemma 9.7 与 (10.1) 在本页核对范围内相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。页眉标题和印刷页码未收入 Markdown。

### PDF p.43/56（印刷 p.43）

- 时间：2026-10-02T02:34:46-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p043.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）。
- 对账范围：局部周期性与箱体平均的误差、(10.2)、Chinese remainder 展开、ω_X 定义、Euler 因子表达至 (10.7) 及收敛域。
- 结果：**PASS±**。周期性、D 的界、(10.2)–(10.7)、乘积索引和 Γ₁/对数积分的开头与 PDF 文本层相符。PDF 原文在周期性句中重复 “can thus can be safely defined”，Markdown 忠实保留该 source-level quirk；无需把它当成 Markdown 漏字。
- 轻微瑕疵：Markdown 把 “Observe” 拆成 `Ob- serve`，属跨行断词噪声。页眉标题和印刷页码未收入 Markdown；本页末收敛域后续留待 p.44 核对。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.44/56（印刷 p.44）

- 时间：2026-10-02T02:41:02-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p044.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；300 dpi 裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p044_lemma-opening.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p044_lemma-proof.png`。
- 对账范围：(10.5)–(10.7)、绝对收敛域、Lemma 10.1 及证明、(10.8) 首行。
- 结果：**FAIL**。Lemma 10.1 第 1941 行把印刷的非空 `X` 错写为 `X_i`；其证明同一行把条件 `|X|=1` 加成 `|\dot X|=1`。第 1942 行把印刷线性形式 `W(\psi_i-b_i)` 加成 `\dot W(\psi_i-b_i)`，并在第二个线性形式 `\psi_{i'}-b_{i'}` 后多出孤立 prime。300 dpi 裁片确认这些额外下标/点号/prime 均不在印刷原文中，会改变集合条件或线性形式记号。印刷原文确为 “none of the s pure linear forms”；此处字母 s 与 Markdown 一致，不作为差异。上述四处均在修复提交中逐处修复。
- 伴随差异：Markdown 保留了印刷行末断词 `Ob- serve`；非语义断行格式不计 FAIL。(10.5)–(10.7)、收敛域和 (10.8) 首行其余核对项相符。页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.45/56（印刷 p.45）

- 时间：2026-10-02T02:44:23-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p045.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；300 dpi 裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p045_lemma-remark.png`。
- 对账范围：(10.8) 续项、E_p 因子分解、(10.9)、Definition 10.2 的定义域与范数、Lemma 10.3 及其 Remark。
- 结果：**FAIL**。Markdown 第 1985 行把引理中的 `G_1, G_2` 识成 `G_1, :\hat G_2`，多出冒号和帽号，改变所指函数；第 1991 行把增长界 `w(N)^{O_m(w(N))}` 中的底数改为 `\dot w(N)`。300 dpi 裁片确认印刷分别为普通 `G_2` 和无点号的 `w(N)`。另第 1991 行将印刷拼写 `suffice` 写作 `sufice`，少一个 f，属轻微拼写瑕疵。待全篇审计后逐处修复。
- 伴随差异：本页其余 (10.8)–(10.9)、E_p^(1)–E_p^(3)、D_{σ}^{m} 定义与 C^k 范数、Lemma 10.3 的估计在文本层/版面核对范围内相符。页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.46/56（印刷 p.46）

- 时间：2026-10-02T02:47:17-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p046.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；主项裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p046_main-term.png`（300 dpi 灰度）。
- 对账范围：Lemma 10.3 证明结尾、Lemma 10.4 与 (10.10)、Proposition 9.5 证明收尾、Section 10 的 higher-order correlations 开头及 `\omega_X(p)` 定义。
- 结果：**FAIL**。Markdown 第 2019 行将 `G(0,0)=(1+o_m(1))(W/\phi(W))^m` 中的 `W` 加点写成 `\dot W`，并在最终主项 `((W\log R)/\phi(W))^m` 后多出数字 `2`；300 dpi 裁片确认两个差异均不在印刷原文中。另第 2021 行把 `differences` 写作 `diferences`，第 2019 行两处 `sufficiently` 均少一个 f，属轻微拼写瑕疵。第 1993 行重复分号；同一行的 `estmate` 拼法与印刷一致，予以保留。待全篇审计后逐处修复。
- 伴随差异：(10.10) 的积分式与误差项、Lemma 10.4 证明及 higher-order correlation 的 `\omega_X(p)` 定义在本页文本层/版面核对范围内相符。页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.47/56（印刷 p.47）

- 时间：2026-10-02T02:49:51-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p047.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p047_lemma10-5.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p047_factor-labels.png`（300 dpi 灰度）。
- 对账范围：Lemma 10.5 与证明、(10.11)、`\lambda_p` 形式、E_p^(0)–E_p^(3) 分解及 Lemma 10.6 的开头。
- 结果：**FAIL**。Markdown 第 2029 行将 Lemma 10.5 的 `\omega_X(p)\leqslant p^{-1}` 加点写成 `\dot\omega_X(p)`；第 2057 行把 `G_0` 写为 `\dot G_0`；第 2059 行又把 `G_1` 加撇号。两张 300 dpi 裁片确认印刷均为无额外点号/撇号的 `\omega_X(p)`、`G_0` 和 `G_1`。这些差异改变局部密度及函数名称。待全篇审计后逐处修复。
- 伴随差异：Markdown 的 `(10.11)`、`\Delta` 乘积、`\lambda_p` 与四因子定义在本页核对范围内相符；页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.48/56（印刷 p.48）

- 时间：2026-10-02T02:52:47-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p048.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p048_estimates.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p048_proof-bounds.png`（300 dpi 灰度）。
- 对账范围：Lemma 10.6 的估计 (10.12)–(10.14)、证明至 `E_p^{(0)}` 的粗界。
- 结果：**FAIL**。Markdown 第 2064 行将 (10.12)–(10.14) 的估计合并在一个数组内，并把标签 (10.13) 放在整个数组末尾；独立的 `(10.12)` 与 `(10.14)` 文本行未对应印刷位置。印刷中 (10.12)、(10.13)、(10.14) 分别标在第一条导数界、第二条指数界和 `G_0(0,0)` 乘积公式旁。另第 2077 行将两处数量级 `O_m((\log R/\log\log R)^r)` 与 `O_m(\log R/\log\log R)` 误写为以 `\log R` 自身为分母，改变项数和因子数界；同一行“导数阶数在 0 与 r 之间”也损坏成 `^r\cdot On`。300 dpi 裁片确认印刷分母为 `\log\log R`，且原句为 “of order between 0 and r”。待全篇审计后逐处修复。
- 伴随差异：第 2077 行 `diferentiating`、`dificulties` 及第 2079 行 `sufices` 各少一个 f，属轻微拼写瑕疵；`(10.15)`、两条素数和估计与 `E_p^{(0)}` 粗界在本页其余核对范围内相符。页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.49/56（印刷 p.49）

- 时间：2026-10-02T02:56:44-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p049.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；主项与脚注裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p049_bound.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p049_footnote23.png`（300 dpi 灰度）。
- 对账范围：Lemma 10.4 应用于 (10.5) 的上界、Proposition 9.6 证明收尾、Remark、Section 11 开头及脚注 23。
- 结果：**FAIL**。脚注 23 的 Markdown 正文（第 2129 行）没有包含印刷句中的序列 `N_1,N_2,\ldots\to\infty`、对象 `N_j` 和因子 `O(1)`；这些符号分别落在脚注正文前的独立 `page_footnote` 片段中（第 2123、2125、2127 行），使脚注句子显示为 “make the prime” 和 “giving up a factor of at most” 而缺少对应数学对象。300 dpi 脚注裁片确认原句是 “make the N_j prime, giving up a factor of O(1) at most”。需全篇审计后在修复时将对象恢复到脚注句中。
- 伴随差异：Markdown 第 2119 行把 “only off by a constant” 写成 “only of by a constant”，第 2113 行 `suficiently` 少一个 f，均为轻微文本瑕疵。Lemma 10.4 上界的幂、Proposition 9.6 收尾主项、Remark 与本页其余 Section 11 正文在核对范围内相符；页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.50/56（印刷 p.50）

- 时间：2026-10-02T03:00:14-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p050.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；终裁裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p050_squares.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p050_maps-and-bounds.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p050_footnote24.png`（300 dpi 灰度）。
- 对账范围：Section 11 首段收尾、平方和进展例子、Chen 素数段、一般 transference principle 段及脚注 24–26。
- 结果：**FAIL**。Markdown 第 2131 行将平方和等差数列最后一项中的 `n+1` 写成带点加号 `n+\dot{+}1`。第 2133 行把 Chen 定理下界中的 `N` 改为 `\mathcal N`，并将进展数下界分母的 `N` 加横线写成 `\bar N`。第 2135 行将 `F_i:\mathbb N\to\mathbb N` 的映射箭头漏掉。300 dpi 裁片确认这些表达在印刷原文中分别是普通加号、普通 `N` 及显式映射箭头。脚注 24 正文（第 2147 行）还缺失印刷中的变体 `\Lambda_R(Wn+b)\Lambda_R(Wn+b+2)`、条件 `1\leq b<W`、`b,b+2` 及其与 `W` 互素的对象；相关片段分散在前置独立 `page_footnote` 行 2137–2145，未进入脚注句子。300 dpi 脚注裁片确认原文完整写有该乘积与条件。待全篇审计后逐处修复。
- 伴随差异：第 2121 行 `affect`、第 2133 行 `effect` 均少一个 f；脚注 26 的法文刊名 `Mathématique` 重音符号位置也有 OCR 偏差。页眉作者行和印刷页码未收入 Markdown；脚注 25–26 的其余 note-added-in-press 内容在核对范围内相符。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.51/56（印刷 p.51）

- 时间：2026-10-02T03:04:25-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p051.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账并检查本页版面）。
- 对账范围：Section 11 末段、Appendix A 标题与导言、Lemma A.1 零点自由区域与 ζ 估计、Γ₀/Γ₂ 定义及其说明。
- 结果：**PASS±**。零点自由区域、ζ 的主部/倒数界、(A.1) 两条曲线定义及其与 Γ₁ 的相对位置均与 PDF 文本层和页面图相符。轻微文字差异：第 2135 行 `affine` 少一个 f 写作 `afine`，`Szemerédi` 的重音符号位置不符；第 2165 行 `if` 被拆写为 `i f`，且 `sufficiently` 少一个 f。页眉标题、印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.52/56（印刷 p.52）

- 时间：2026-10-02T03:07:20-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p052.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账并检查本页版面）；趋于关系裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p052_contour-limit.png`（300 dpi 灰度）。
- 对账范围：Lemma A.2 的 (A.2)–(A.3) 与估计证明、Lemma A.3 的假设/积分展开式、证明中的第一次轮廓平移及留数。
- 结果：**FAIL**。Markdown 第 2229 行把 “when `\Im(z),\Im(z')\to\infty`” 写成 `\Im(z),\Im(z') \infty`，漏掉两处趋于箭头，使衰减条件的数学关系丢失。300 dpi 裁片确认印刷符号为 `\Im(z),\Im(z')\to\infty`。待全篇审计后逐处修复。
- 伴随差异：第 2229 行 `difficulties` 少一个 f；(A.2)–(A.3)、Lemma A.3 主积分/导数项、轮廓转移方向及留数公式在本页核对范围内相符。页眉作者行和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.53/56（印刷 p.53）

- 时间：2026-10-02T03:10:51-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p053.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；300 dpi 裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p053_residue-derivative.png`、`audit/300dpi/Tao_Green_2004_primes_AP_p053_imaginary-parts.png`。
- 对账范围：I₁/I₂ 分拆、双极点留数与 I₁ 估计、I₂ 的第二次轮廓平移、(A.4)–(A.5) 及凸性界论证。
- 结果：**FAIL**。Markdown 第 2237 行把印刷的留数项 `\partial f/\partial z'(0,0)` 写成 `\partial\bar f/\partial z'(0,0)`，多出横线。第 2245 行漏掉 `|\Im z'|\to\infty` 的趋于箭头。第 2271 行将三处 `\Im` 条件误写成 `\mathfrak T`、`\mathbb S` 和 `\bar{\mathbb S}`：分别对应凸性界前提 `|\Im(z+z')|\geqslant1/100`、有界虚部条件 `|\Im z|,|\Im z'|\leqslant t`，以及小虚部情形 `|\Im(z+z')|\leqslant1/100`。300 dpi 裁片确认源页三处均为虚部符号 `\Im`，不是这些字母/横线。该差异使关键分情况条件不可读；待全篇审计后逐处修复。
- 伴随差异：第 2245 行 `sufficient` 少一个 f 写作 `suficient`。I₁/I₂ 留数公式、(A.4)–(A.5) 的主不等式及结论在本页其余核对范围内相符；页眉标题和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.54/56（印刷 p.54）

- 时间：2026-10-02T03:14:43-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p054.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账）；归纳积分与 H 定义裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p054_induction-formulas.png`（300 dpi 灰度）。
- 对账范围：Proof of Lemma 10.4 的 I(G,m) 定义与归纳式、(A.6)、m→m+1 步骤及辅助函数 H 的类型/定义。
- 结果：**FAIL**。Markdown 第 2304 行第二个积分的分母把印刷 `z_j'^2` 写为下标 `z_{j'^{2}}`，将平方从变量转录到下标；第 2307 行把 `H:\mathcal D_\sigma^m\to\mathbb C` 的映射箭头漏掉。300 dpi 裁片确认分母平方作用于 `z_j'`，且 H 的定义域到值域之间有显式箭头。待全篇审计后逐处修复。
- 伴随差异：积分定义中的乘积上限 `s` 与估计中的 `\mathcal D_\sigma^s` 均与 PDF 原文一致，故不作为差异。(A.6)、归纳的第一积分、误差项及 H 的偏导/轮廓积分在本页其余核对范围内相符；页眉作者行和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

### PDF p.55/56（印刷 p.55）

- 时间：2026-10-02T03:17:55-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p055.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账并检查本页版面）。
- 对账范围：Lemma 10.4 归纳证明收尾等式与 References [1]–[17]。
- 结果：**PASS±**。归纳结论中的三行范数/误差估计及参考文献 [1]–[17] 的作者、题名、刊物、卷期与页码在本页核对范围内相符，包括 [14] 的 `g(T^{n^2}x)`。轻微 OCR 瑕疵：多处 `Szemerédi`、`Erdős`、`Turán` 的重音符号落位异常；不影响条目识别。页眉标题和印刷页码未收入 Markdown。
- 修复状态：本页无 FAIL；签页时未编辑 Markdown。

### PDF p.56/56（印刷 p.56）

- 时间：2026-10-02T03:22:09-0400；actor=`Peer-P22`；model=`gpt-6-luna`；effort=`max`。
- 源页证据：`audit/Tao_Green_2004_primes_AP_p056.png`（pngmono，150 dpi；born-digital 页，以文本层逐页对账并检查本页版面）；作者联系信息裁片：`audit/300dpi/Tao_Green_2004_primes_AP_p056_affiliations.png`（300 dpi 灰度）。
- 对账范围：References [18]–[45]、参考文献末尾及作者机构/联系方式。
- 结果：**FAIL**。目标 Markdown 在第 2415 行 [45] 条后即结束；PDF p.56 其后仍有两组作者资料，均未收入：School of Mathematics, University Walk, Bristol, BS8 1TW 与 b.j.green@bristol.ac.uk；Department of Mathematics, University of California at Los Angeles, Los Angeles, CA 90095 与 tao@math.ucla.edu。300 dpi 裁片确认这些机构地址和邮箱位于印刷页末，属于本篇内容缺漏。待全篇审计后补入。
- 伴随差异：参考文献中 `Szemerédi`、`Rödl`、`Ramaré`、`Théorie`、`Über` 等重音符号落位有 OCR 瑕疵，且 [26] 的 em dash 未保留，属轻微文字差异；[45] 标题在印刷原文中重复两次，Markdown 忠实保留该 source-level quirk。页眉作者行和印刷页码未收入 Markdown。
- 修复状态：待 56 页初审全部完成后统一处理 FAIL；本次签页未编辑 Markdown。

## 修复与全篇复核（Peer-P22）

- 时间：2026-10-02T05:08:46-0400；actor=Peer-P22；model=gpt-6-luna；effort=max。
- 阶段说明：上文每个页面的等级和修复状态记录的是该页初审签署时的状态；完整首审完成后才开始统一手工修复。首审仍为 FAIL 38 页、PASS± 18 页、PASS 0 页；本登记说明首审 FAIL 的后续处置。
- 唯一目标：本篇指定的 MinerU Markdown。PDF 和根 AUDIT-INDEX.md、AUDIT-PROGRESS.log 均未修改。
- 修复执行：fix(md) commit aae3e06020676e772fa4ea48ecbcab698005856a；基于用户指定的精确候选基线 037602429d3b009f6fc468c732073eb3ddf9875f。
- 哈希：源 PDF SHA-256=d03dd6156165fc92e488b3fec35a574c8f7c9df55125cec0f3eebdf95d7256e1；修复前 Markdown SHA-256=e7aaed689d5f085f381d57f296041ea7bde01e4d79a3cf351eb2ce150435fd92；最终 Markdown SHA-256=d33a3f6bef647cb886852d9012f6c159496ef9c76ffdc729e3cb7337393e33d8。
- 最终复读：COMPLETE；修复后从首行到末行复读全部 2,355 行，并按逐页记录回核 56 页涉及的最终公式、正文和脚注。相关修复点均对照相应 PDF 文本层及本文件所列源页图/裁片；未发现新增 FAIL。原 PASS± 页中的轻微断词、可辨读拼写及重音 OCR 瑕疵仍按其初审记录保留。
- 机械核对：fix(md) 提交前 git diff --check 通过；目标 Markdown 修复前基线为 TRACKED_CLEAN，PDF 与本篇其它资产保持只读。
- Current Truth：仍为 CANDIDATE_NOT_CURRENT，未集成、未修改共享 ref/tag、未 push。最终与主线 refs/heads/main=42ad5ffc8481b31e1ea640c8182a4ef1c19efbec 比较时，本任务拥有的 PDF、目标 Markdown、审计文件、Tao 专属证据前缀及根进度入口相对指定基线均无主线改动。

首审 FAIL 页的逐处修复摘要如下。原页证据路径见同编号页面记录中的 PDF 文本层、150 dpi 全页图及所列 300 dpi 裁片。

| PDF 页 | 已修复差异 |
|---:|---|
| 1 | 恢复启发式公式的普通 N²、完整 log^k N 分母和公式/k-tuples 边界。 |
| 2 | 恢复两条素数等差数列整数、lim sup(N→∞) 上密度公式，以及无横线的 ε。 |
| 3 | 去掉 N₀ 上的伪帽号；恢复脚注 1 中 Z_N、[-N,N]、2,…,k 等句内对象；清除 W-trick 周围伪上标 66/3。 |
| 5 | 恢复脚注 4 的 ν_const、ν 与 Z_N 对象，并恢复脚注 5 的 W=∏(p<w(N))p 定义。 |
| 7 | 补回 N→∞ 与 f:A→R 的映射箭头。 |
| 8 | 恢复参数 (12,5,2)、m₀ 记号、ψ_j(x)，并补齐脚注 9–10 的 W-trick、随机子集变量、界和公式。 |
| 9 | 恢复 2^(k−1)-correlation condition。 |
| 11 | 补回 uniform cover 映射 Φ:A→B 的箭头。 |
| 17 | 恢复整体下标 y_(k−d−1)。 |
| 19 | 删除 q=1/q=2 变量列表中多出的数字 2。 |
| 21 | 将伪梯度 ∇^14 还原为脚注 14 标记及 DF=F；在脚注 15 恢复两处 k−2 阶数。 |
| 22 | 恢复 Φ:I^K→R，删除 I^K 上的伪 breve，并将大写 O 还原为小写 o。 |
| 25 | 恢复 dual norm ||·||_(U^(k−1))*. |
| 26 | 恢复可测集所属 B、join 求和下标 i 和 Ψ_A:I→[0,1]。 |
| 27 | 恢复 ψ_η:R→[0,1]；删除最后 σ-代数上的伪 tilde 和期望符号上的伪点号。 |
| 28 | 恢复 Ψ_A:I^K→[0,1]。 |
| 29 | 在脚注 16 恢复 f_(U⊥)≤1+o_ε(1)、δ−o_ε(1) 和修改 f_(U⊥) 的误差对象。 |
| 31 | 删除 B_(K+1) 后的伪下标 1。 |
| 32 | 在脚注 18 恢复迭代上界 K₀。 |
| 34 | 闭合能量范数公式括号，并把条件期望中的 B̄_K 还原为 B_K。 |
| 36 | 在脚注 21 恢复 Λ(n) 求和区间及 n≡1/b (mod W)、(b,W)=1 的关系。 |
| 37 | 恢复 1≤i≤m 和线性形式求和下标 j。 |
| 38 | 删除 R^(10m) 指数中的伪点号，并在 Proposition 9.8 恢复求和下标 j。 |
| 39 | 删除 θ_i 的伪点号、φ(W) 的伪横线，并在脚注 22 恢复 ψ_i、区间、盒子和常数项对象。 |
| 40 | 在 τ_m(n) 中恢复两个普通 O_m(1) 渐近因子。 |
| 41 | 将重复 h_i 情形的交叉引用从 (9.2) 改为 (9.3)。 |
| 42 | 在 Section 10 重述线性形式时恢复坐标求和下标 j。 |
| 44 | 删除 X_i、点缀 X、点缀 W 及第二线性形式后的孤立 prime。 |
| 45 | 将 G₁,G₂ 中 G₂ 的伪冒号/帽号去掉，并恢复无点号的 w(N)。 |
| 46 | 恢复主项中的普通 W，并删除主项后多出的数字 2。 |
| 47 | 删除 ω_X、G₀、G₁ 上多出的点号/撇号。 |
| 48 | 分别归置 (10.12)–(10.14) 标签；将 log R/log R 修为 log R/log log R，并恢复 “order between 0 and r”。 |
| 49 | 将脚注 23 的 N₁,N₂,…→∞、N_j 和 O(1) 放回脚注句子，移除分离碎片。 |
| 50 | 恢复平方和进展的普通加号、Chen 估计中的普通 N、F_i 映射箭头，并补齐脚注 24 的两个 Λ_R 因子及参数/互素条件。 |
| 52 | 补回两处 Im(z), Im(z′)→∞ 的趋于箭头。 |
| 53 | 删除留数项 f 上的伪横线；恢复第二处 Im(z′)→∞ 与三处 A.5 虚部条件 Im。 |
| 54 | 将 z_j′² 的平方还原到变量上，并补回 H:D_σ^m→C 的映射箭头。 |
| 56 | 补入 Tao 与 Green 的两组机构地址及邮箱。 |
