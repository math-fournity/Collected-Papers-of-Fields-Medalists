# AUDIT — Lindenstrauss_2007_littlewood_published

## 任务与证据边界

- 状态：`CANDIDATE_NOT_CURRENT`。本候选来自 Peer-P16；Master-Luna 是唯一 canonical integrator。
- Peer 身份：actor=`Peer-P16`；model=`gpt-6-luna`；reasoning effort=`max`。
- 基线：任务指定 main HEAD `03760242`；本 worktree 起始 HEAD=`037602429d3b009f6fc468c732073eb3ddf9875f`，起始工作区干净。
- 只读源：`Lindenstrauss_2007_littlewood_published.pdf`；`pdfinfo` 确认 48 页，印刷页码 513–560。PDF 与本篇 Markdown 映射符合本任务及 `AUDIT-INDEX.md` 第 97 行的 48 页登记。
- 出口：仅在本候选中创建本 AUDIT 与 `audit/Lindenstrauss_2007_littlewood_published_pNNN.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_*.png`；本篇 Markdown 是唯一允许修改的现有正文。根索引和进度日志由 Master 维护，本 Peer 不修改。
- README 冲突待 canonical owner 处理：根 `README.md` 第 524 行把同一 PDF 记为 79 页；直接 PDF 页数、任务预期和 AUDIT-INDEX 登记均为 48。该 README 行不在本 Peer 写入范围内。
- PDF 类型：born-digital。`pdftotext -layout` 成功提取 136,195 字节，48 个 form-feed 页段，U+FFFD 数量为 0；`pdffonts` 显示嵌入的 Computer Modern Type 1C 字体。
- MinerU：`middle_json.json` 登记 48 页、MinerU 3.4.4、`basic` tier、`txt` parse mode。现有导出 JSON 未找到 `doc_id` 字段。
- 方法：以 `pdftotext -layout` 的完整文本层逐 PDF 页对账 MinerU Markdown，并回到印刷页图核终裁疑字/符号。全部 48 页已按 150dpi `pngmono` 渲染；born-digital 抽检整页视觉检查题录页 p.1 与密集数学页 p.17、p.38。需进一步裁决的字符另存本篇前缀的 300dpi 裁片。修复只在全篇审计结束后开始；终修后需从头到尾重读整个 Markdown。

## PDF p.001 / 印刷 p.513

- 时间：2026-10-01 20:19:01 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p001.png`（150dpi `pngmono`）；印刷字形终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p001_hausdorff.png`（300dpi 原页裁片）。
- Markdown 定位：题录、Abstract 与开篇段落，尤其当前第 7 行。
- 核对：刊名/卷年/印刷页范围、标题、作者、摘要、节标题顺序、摘要数学对象及脚注。
- 结果：`PASS±`。
- 差异：摘要把印刷的 `Hausdorff` 写成 `Hausdorf`，丢失 ligature `ﬀ` 的第二个 `f`。PDF 文本层与 300dpi 裁片均支持印刷字形为 `Hausdorff`；这是 MinerU 正文的可检索拼写瑕疵，不是印刷原文 quirk。标记全篇审计结束后逐处人工修复，并复核修订值。
- 复核：题名、作者和摘要其余语义与 p.513 相符；Abstract/行间数学的空格与 LaTeX 扁平化另属排版瑕疵，本页没有发现数学命题改变或段落缺失。

## PDF p.002 / 印刷 p.514

- 时间：2026-10-01 20:26:00 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p002.png`（150dpi `pngmono`）；字形/印刷拼写证据：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p002_different_ligature.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p002_print_quirk_raghunatan.png`。
- Markdown 定位：第 15、19–25 行；包含跨 p.513/p.514 的段落延续、§1.2、Conjecture 1.1 及其后续说明。
- 核对：正文论述次序、SL(k,R)/SL(k,Z) 与 A 的作用、Weyl chamber flow 段落、Conjecture 1.1 的条件与结论、印刷跨行断词。
- 结果：`PASS±`。
- 差异：Markdown 第 19 行把 `different` 写成 `diferent`，少了第二个 `f`；第 21 行 `For k > 2` 后的标点误成句点再逗号，印刷是逗号；第 25 行保留了由印刷行末断开的 `multi-plicative` / `multi-plicatively` 连字符，影响连续检索。均标记全篇审计结束后逐处手工修复。
- 源级 quirk：印刷本确实写作 `unipotents groups` 及 `Raghunatan`（该处为姓名拼写）；对应 Markdown 忠实转录，不按语法或作者姓名预期改写。
- 复核：300dpi 裁片确认 `different` 的双 f，以及印刷原件自身的 `Raghunatan` 拼写；Conjecture 1.1 的完整假设与结论在 Markdown 中保留，未发现公式或段落遗漏。

## PDF p.003 / 印刷 p.515

- 时间：2026-10-01 20:26:45 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p003.png`（150dpi `pngmono`）；字形裁决：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p003_eq_1_1.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p003_difference.png`。
- Markdown 定位：第 25–47 行；含 Littlewood 猜想 (1.1)、其最近整数距离定义、Theorem 1.3 和 Corollary 1.4。
- 核对：跨页引言段落、invariant-measure 论述、公式 (1.1) 的 `lim inf`、系数 n、两个最近整数距离因子及等式右端 0，方程号和后续定理陈述。
- 结果：`PASS±`。
- 差异：Markdown 第 27 行把印刷的 `difference` 写成 `diference`，缺少第二个 `f`；300dpi 裁片支持按 `difference` 修复以保留可检索正文。
- 复核：300dpi 公式裁片确认 (1.1) 的印刷运算符、角括号、两个因子和方程号；Markdown 对应公式及定义均吻合。页内其余已核标题/定理顺序与内容相符，无段落缺失。

## PDF p.004 / 印刷 p.516

- 时间：2026-10-01 20:27:26 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p004.png`（150dpi `pngmono`）；终裁裁片：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p004_theorem_1_5.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p004_lim_inf_text.png`。
- Markdown 定位：第 52–85 行，含 Theorem 1.5、最近整数逼近说明、Theorem 1.6 及等式 (1.3)。
- 核对：Ξ 集定义、`lim inf` 运算符、Hausdorff 维数记号、计数并集陈述、方程 (1.2)/(1.3) 与 Theorem 1.6 的 `k−1` 维数。
- 结果：`FAIL`。
- 内容差异：第 55 行把印刷 `dim_H Ξ` 识别为 `dim Π_H Ξ`，并将“In fact, Ξ is”拆成损坏的数学/文字片段，改变了 Theorem 1.5 的结论表达；第 59 行两处 `lim inf` 被拆成不完整运算符，破坏对坏逼近数集合的定义。300dpi 裁片确认印刷内容，需在全篇审计后修复这些位置。
- 文字瑕疵：第 55、59、65、75、81 行的 `Hausdorf` 均丢失 `Hausdorff` 的第二个 `f`；第 65 行 `efective` 少一个 `f`。均为可检索正文错误，列入全篇完成后逐处手改。
- 复核：第 52 行 Ξ 的定义、(1.2)、Theorem 1.6、(1.3) 与 A-invariance 陈述已逐项对照 p.516；除上述所列差异外，顺序和内容相符。

## PDF p.005 / 印刷 p.517

- 时间：2026-10-01 20:28:01 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p005.png`（150dpi `pngmono`）；字形证据：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p005_conjecture_n_ge_2.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p005_print_typos.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p005_print_tranversals.png`。
- Markdown 定位：第 87–105 行；包括 Conjecture 1.7、群 U₁/U₂ 的矩阵定义、后续应用和 §1.3 起始部分。
- 核对：Conjecture 1.7 的前提/结论与 n 范围、U₁/U₂ 矩阵、Γ 的子群条件、Hilbert modular lattice 结论、下方推论和脚注。
- 结果：`FAIL`。
- 内容差异：印刷开头是 G 为 `n ≥ 2` 个 SL(2,R) 的直积；Markdown 第 87 行只留下不可见的 `\hphantom{0}` 和 `copies`，漏掉 `n ≥ 2` 这一猜想前提，改变了命题范围。第 101 行在 `n\geq3` 后也漏句点，粘连下一句 “As explained…”。300dpi 裁片确认命题前提；页图/文本层确认句界，终修时一并恢复。
- 可检索文字瑕疵：第 101 行的 `Hausdorf` 多次漏掉第二个 `f`；按印刷拼写逐处修复。
- 源级 quirk：印刷本写作 `up to conjunction` 与 `tranversals`；300dpi 裁片确认这些拼写确实来自 PDF，Markdown 忠实保留，禁止按预期词改写。
- 复核：U₁/U₂ 两个矩阵、Γ 的 lattice/normal subgroup 条件及后续 n≥3 说明均与 p.517 对应；除漏掉的 n≥2 外未发现公式或段落缺失。

## PDF p.006 / 印刷 p.518

- 时间：2026-10-01 20:36:16 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p006.png`（150dpi `pngmono`）；文字终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p006_text_typos.png`。
- Markdown 定位：第 109–119 行；从 conditional measures 的技术背景至 quantum unique ergodicity 的过渡段。
- 核对：条件测度与不变叶层、熵条件、[17]/[3]/[20] 方法关系、R-split 群上的结论及段落顺序。
- 结果：`PASS±`。
- 差异：第 113 行 `suficient`、第 115 行 `dificulty`、第 117 行 `Hausdorf`、第 119 行 `diferent` 分别缺少印刷双 f ligature 的一个 `f`；300dpi 页裁片确认印刷拼写。标记全篇结束后逐处恢复拼写，便于正文阅读与检索。
- 复核：条件测度、熵、Haar measure 及引用关系均与 p.518 相符；没有发现命题含义改变、定理条件遗漏或整段丢失。

## PDF p.007 / 印刷 p.519

- 时间：2026-10-01 20:36:49 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p007.png`（150dpi `pngmono`）。
- Markdown 定位：第 121–133 行；覆盖高熵/低熵两种方法、Acknowledgment 与 Part I 起始定义。
- 核对：SL(2,R)×SL(2,R) 的例子、Theorem 1.3 方法互补性、Ratner H-property、熵公式引用、作者致谢、G/Γ/X 的定义。
- 结果：`PASS±`。
- 差异：第 121 行数学环境结束后缺少印刷中的句点；第 123 行 `with“low”` 少一个排版空格。属于可读性/标点瑕疵，不改变定理内容。
- 复核：群、熵条件、定理引用和致谢姓名/机构均与 p.519 对应；没有发现数学符号误置或段落遗漏。

## PDF p.008 / 印刷 p.520

- 时间：2026-10-01 20:37:16 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p008.png`（150dpi `pngmono`）；球记号裁决：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p008_ball_notation.png`。
- Markdown 定位：第 135–161 行；包括 Σ 与 Lie algebra 的识别、unipotent/normalizer/centralizer 定义、Radon 测度空间、比例记号、球记号和 §2.1。
- 核对：Σ 的方程与参数化映射、群定义、A 对 U 轨道的作用、weak* 拓扑、测度比例以及不同度量球的记号。
- 结果：`FAIL`。
- 内容差异：第 155 行把印刷 `B^H_ε(x) = B^H_ε · x` 识别成带点的 `B^{\dot H}_ε(x) = \dot B^H_ε · x`，在球记号上额外引入两个点，改变数学符号。p.520 的 300dpi 裁片确认印刷只有上标 H 和群作用乘点；需全篇审计后逐处手工修正。
- 其他瑕疵：第 143 行 `gH g^{-1}=H` 后出现双分号；第 157 行度量句号落入数学分隔符。排版/标点错误不改变本页其余定义。
- 复核：第 135 行 `identify`、Σ 定义、`mapsto`、U unipotent 条件、Radon 测度积分定义及 `ν₁ ∝ ν₂` 均与 p.520 相符；没有段落缺失。

## PDF p.009 / 印刷 p.521

- 时间：2026-10-01 20:37:48 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p009.png`（150dpi `pngmono`）；符号及脚注终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p009_X_prime.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p009_footnote_2.png`。
- Markdown 定位：第 163–183 行为 (1)–(7) 与熵讨论；第 185–191 行为脚注 2。
- 核对：Radon 条件测度的七项性质、Haar/atomic 两端、正熵刻画、脚注 2 对 [20] 与 [17]/[13] 两种记号约定的说明。
- 结果：`FAIL`。
- 内容差异：脚注 2 被导出成三个独立的 docvortex 片段（第 185 行 `U;`、第 187 行 `µx,U`、第 189 行 `[17]`）及一个主段（第 191 行）；主段出现 `taken in and [13]` 和 `single orbits of in this approach`，引用 [17] 与 `U` 脱离句子，脚注读起来残缺/失序。p.521 300dpi 裁片给出完整印刷文本；全篇结束后将逐处手工合并为一段并复核。
- 复核：顶部源图确认 co-null set 使用 `X′` prime，Markdown 的 `X^\prime` 一致；性质 (1)–(7) 中 measurable、push-forward、共轭关系、Haar 等价与 entropy 条件均与 p.521 相符，无其他已发现的数学陈述遗漏。

## PDF p.010 / 印刷 p.522

- 时间：2026-10-01 20:38:26 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p010.png`（150dpi `pngmono`）；终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p010_limsup_claim.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p010_conull_sentence.png`。
- Markdown 定位：第 193–232 行；覆盖性质 (8)、其 Poincaré recurrence 证明、集合 D_M 与 limsup 论证、Uᵢⱼ 定义和共轭公式。
- 核对：性质 (8) 的比例不变性、D_M 定义、limsup 表达式、常数 c/k 不等式链、conull 子集句、uᵢⱼ(s) 公式及 α 共轭指数。
- 结果：`FAIL`。
- 内容差异：Markdown 第 205 行把印刷 `for any n, k` 写成 `n_{:}, k`，凭空引入 colon 下标并损坏证明变量；300dpi p.522 裁片确认原文为普通 n 与 k，需手工恢复。第 211 行 `suficiently` 少一个 f，另作拼写修复。
- 源级 quirk：印刷本的括号说明也写作“`α^{nt}` is in D_M”，本身没有 x；PDF 页图与文本层一致。不得按上下文预期补入 x。`lim sup` 在 Markdown 被字母间隔/拆开，记为 `PASS±` 排版瑕疵；该运算符及 n→∞、α^{-nt}D_M 成分仍可辨，终修时可规范为 `\limsup_{n\to\infty}` 并人工复核。
- 复核：p.522 其余被核公式 (8)、D_M 球测度界、c^k 等式、最后的 conull 结论以及 uᵢⱼ 共轭公式顺序吻合；本页 FAIL 仅由错误下标造成。

## PDF p.011 / 印刷 p.523

- 时间：2026-10-01 20:42:41 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p011.png`（150dpi `pngmono`）；终裁裁片：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p011_mu_ij.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p011_maximal_ergodic_formula.png`。
- Markdown 定位：第 235–255 行；包括条件测度记号、性质 (9) 及证明、最大遍历定理 (10)、Theorem 2.1 引入。
- 核对：Uᵢⱼ 轨道叶层、非平凡条件测度与 Haar 结论、Poincaré recurrence 论证、性质 (10) 的积分/球测度/阈值比及通用常数。
- 结果：`FAIL`。
- 内容差异：第 241 行最后一句把印刷 `µ_x^{ij}` 写成 `\dot{µ}_x^{ij}`，额外加了时间导数点，改变条件测度记号。p.523 300dpi 裁片确认印刷无点，需手工删除该点。
- 复核：性质 (9) 其余条件与证明链匹配；(10) 的积分域、`f(ux)`、条件测度、阈值不等式及 `C ||f||₁/α` 上界已对照裁片，均吻合。

## PDF p.012 / 印刷 p.524

- 时间：2026-10-01 20:43:45 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p012.png`（150dpi `pngmono`）；符号终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p012_group_H_ab.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p012_remark_3_prime.png`。
- Markdown 定位：第 257–275 行；覆盖 Theorem 2.1 三种情形、Remark (3′)、例子解释及进入 high entropy case 的条件。
- 核对：条件测度 (1)/(2) 的 Haar/trivial 分支、H_ab 的生成子群记号、A′_ab 轨道、centralizer、remark 标签 (3′) 与周期点陈述。
- 结果：`FAIL`。
- 内容差异：第 259 行把印刷 `H_{ab}=\langle U_{ab},U_{ba}\rangle` 读成 `\left. U_{ab},U_{ba}\right.`，丢失生成子群的角括号，改变 H_ab 定义；第 265 行把 remark 标签的 prime 导出为控制字符 `U+0006`，标签不可可靠显示。补充比对发现第 261 行把印刷的普通斜体 `A'_{ab}` 写成 `\mathcal A'_{ab}`，误加花体样式。p.524 的 300dpi 裁片 `audit/300dpi/Lindenstrauss_2007_littlewood_published_p012_group_H_ab.png` 确认 H_ab 括号及 A 的字形，需全篇结束后手工恢复。
- 补充复核：2026-10-01 20:51:00 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。该字形差异与本页同一处的 A′ 定义逐字符对照后确认。
- 复核：Theorem 2.1 的三种分支均有 Markdown 对应；A′_ab、centralizer 条件、x₀ 周期关系和后续例子段落次序与 p.524 相符。

## PDF p.013 / 印刷 p.525

- 时间：2026-10-01 20:44:28 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p013.png`（150dpi `pngmono`）。
- Markdown 定位：第 277–295 行；含 Theorem 2.2、high/low entropy 分支、Theorem 2.3 两种结论、U_ab 方法说明及 §3 起始。
- 核对：Theorem 2.2 的条件/结论、Theorem 2.3 的假设和互斥情形、低熵情形 U_ba 推论、Ratner H-property 与最大遍历定理引用、下一节的过渡句。
- 结果：`PASS±`。
- 差异：第 279 行在 `G` 后多出重复逗号，另有 `a.s.` 等间距/标点扁平化；不改变数学陈述。
- 复核：两个定理各自的测度条件、H_ab/C(H_ab) 轨道结论、章节标题与引用位置均与 p.525 对应；未发现公式或段落遗漏。

## PDF p.014 / 印刷 p.526

- 时间：2026-10-01 20:45:28 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p014.png`（150dpi `pngmono`）；印刷双 f 终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p014_diffeomorphisms.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p014_different.png`。
- Markdown 定位：第 295–327 行；含熵与一维条件测度关系、Proposition 3.1、Corollary 3.2、熵对称式 (3.2) 和 Lemma 3.3。
- 核对：Proposition 3.1 的 sᵢⱼ 取值/原子条件/Haar 条件、熵公式 (3.1)、Corollary 3.2 条件、(3.2) 对称式及 Lemma 3.3 的非原子假设和不变性结论。
- 结果：`PASS±`。
- 差异：第 297 行 `difeomorphisms`、第 313 行 `diferent` 分别漏掉双 f ligature 的一个 `f`；300dpi 裁片确认印刷为 `diffeomorphisms` / `different`，列入全篇结束后的逐处拼写修复。第 303、311、315、327 行另有 `If`、`max`、`if`、`invariant` 字母间隔伪影，含义仍可辨。
- 复核：条件测度维数与熵的定义式、指标次序及 (3.1)/(3.2) 的求和/对称关系均与 p.526 对应；未发现公式项、编号或段落缺失。

## PDF p.015 / 印刷 p.527

- 时间：2026-10-01 20:46:25 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p015.png`（150dpi `pngmono`）；图注/公式裁片：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p015_figure_caption.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p015_eq_3_3_3_4.png`。
- Markdown 定位：第 329–356 行；含 Figure 1 嵌图与图注、Theorem 2.2 的集合定义、熵等式 (3.3)/(3.4) 及集合基数链。
- 核对：PDF 图中 Uᵢₖ(rs)x、Uᵢⱼ(r)、Uⱼₖ(s) 三个标签与 Markdown 引用的 `images/page_14_image_0.jpg` 一致；图注文字存在且对应印刷内容；核对 Cℓ/Rℓ 定义、(3.3)/(3.4) 的求和指标/不等号与末尾链式界。
- 结果：`PASS±`。
- 差异：Markdown 第 331 行图注末尾缺少印刷句号，公式变量周围另有 LaTeX 空格/排版扁平化；没有发现图、图注或等式内容缺失。
- 复核：300dpi 图注及公式裁片确认 caption、(3.3)、(3.4) 与 PDF 一致；MinerU 的 figure 位图为只读来源，本 Peer 未改写或复制其原件。

## PDF p.016 / 印刷 p.528

- 时间：2026-10-01 20:51:41 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p016.png`（150dpi `pngmono`）；符号终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p016_A_subgroup.png`。
- Markdown 定位：第 359–391 行；含 (3.5)、Corollary 3.4、§4 的 A′_ab 子群定义、L(ab)/U(ab)/C(ab) 及 Definition 4.1/Lemma 4.2。
- 核对：熵界与 (3.5)、s_ab=s_ba 对称性、A′_ab 的定义与不变测度关系、三个子群定义、exceptional/strong exceptional 的量词与结论。
- 结果：`FAIL`。
- 内容差异：第 375 行把印刷的普通斜体 `A'_{ab}` 写为 `\mathcal A'_{ab}`，误加 calligraphic 样式，并与同句后半段的普通 `A'_{ab}` 不一致。p.528 300dpi 裁片确认印刷为普通 A；需手工统一为 `A'_{ab}`。
- 复核：等式 (3.5)、Corollary 3.4 的 s_ab/s_ba 对称关系、L/U/C 定义与 Definition 4.1 的量词和 L/C 分支均与 p.528 对应。

## PDF p.017 / 印刷 p.529

- 时间：2026-10-01 20:52:35 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p017.png`（150dpi `pngmono`；此页亦为密集数学页整页视觉抽检）；矩阵条件终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p017_matrix_text.png`。
- Markdown 定位：第 396–415 行；覆盖矩阵表示 (4.1)、L/C 的判别、D_ℓ/E_{ℓ,s} 定义、f(x) 及收缩递推。
- 核对：矩阵各块/向量维数、g∈L 与 g∈C 的充要条件、D_ℓ 的唯一 g、f(x) 的三个分量、α^t 共轭收缩因子与 Poincaré recurrence 结论。
- 结果：`FAIL`。
- 内容差异：第 399 行把判据中的 `g_{2*}` 写成损坏的 `g_{2}2*`（额外出现第二个 2，星号下标被拆坏），致使 L 的零块条件不正确。p.529 300dpi 裁片与矩阵 (4.1) 确认应为 `g_{2*}`；全篇审计结束后逐处修复。
- 复核：矩阵 (4.1) 的九个块及 (e^{-2}g₁₂, e^{-1}g₁*, e^{-1}g₂*) 收缩项均与本页原图一致；D_ℓ 与 E_{ℓ,s} 的余下条件未发现遗漏。

## PDF p.018 / 印刷 p.530

- 时间：2026-10-01 20:53:08 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p018.png`（150dpi `pngmono`）；条件不变性字形裁决：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p018_E_invariance.png`。
- Markdown 定位：第 417–455 行；覆盖 Proposition 4.3、ergodic decomposition、条件测度积分 (4.2) 及 (1)⇒(2) 的证明开头。
- 核对：两个等价条件、E′/E σ-algebra、条件测度常值关系、A′_ab 不变性、积分分解、f_r/C_r 与 (4.3) 的球交等式。
- 结果：`FAIL`。
- 内容差异：第 425 行把“conditional measure is A′_ab-invariant”写成 `A′_{ab}{}^{*}`-invariant，额外增加星号，改变不变性所指的作用。p.530 300dpi 裁片确认印刷两处都为 A′_ab，无星号；需手工删去多余标记。
- 复核：Proposition 4.3 的 (1)/(2) 与式 (4.2)/(4.3) 内容、集合包含方向和测度界均与 p.530 对应；未发现其他实质差异。

## PDF p.019 / 印刷 p.531

- 时间：2026-10-01 20:53:45 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p019.png`（150dpi `pngmono`）；条件测度字形/文本终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p019_conditional_measure.png`。
- Markdown 定位：第 457–479 行；包含 Proposition 4.3 (1)⇒(2) 收尾、(2)⇒(1) 的条件测度证明和 Lemma 4.4。
- 核对：K_ℓ/N 定义、Ergodic component 条件测度 μ_x^E、支持集 C z 的证明、y₀/y₁/yₙ 轨道、Lemma 4.4 两个断言及后续条件测度关系。
- 结果：`FAIL`。
- 内容差异：第 461 行多处把条件测度 `\mu_x^{\mathcal E}` 识别为 `\mu_x^{\varepsilon}`，并把“for `\mu_x^{\mathcal E}`-a.e. `y_0`”整段并入错误下标/符号，破坏了分解测度对象和遍历性量词；p.531 300dpi 裁片确认印刷为脚本 E。全篇结束后须按原文逐处恢复测度标记及 `a.e.` 位置。
- 文字瑕疵：第 459 行 `sufices` 少一个 f，第 475 行 `diferent` 少一个 f；作为可检索拼写错误列入逐处修复。
- 复核：Proposition 4.3 证明从强 exceptional returns 得出支撑轨道的论证、Lemma 4.4(1) 的 U(ab) 轨道包含结论与 p.531 对应；本页 FAIL 集中在 conditional-measure 标签/量词。

## PDF p.020 / 印刷 p.532

- 时间：2026-10-01 20:54:24 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p020.png`（150dpi `pngmono`）；关系式终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p020_recurrence_equation.png`。
- Markdown 定位：第 481–515 行；覆盖 Lemma 4.4(2) 的反证、§4.2 证明纲要、Poincaré recurrence、式 (4.4)/(4.5) 与 Ratner H-property 过渡。
- 核对：条件测度相等导致 Haar 矛盾的论证、u(r) 的参数化、推前记号、回归点 x′ 的定义、(4.4)/(4.5) 与 x(r)/x′(r) 的关系。
- 结果：`FAIL`。
- 内容差异：第 493 行把印刷 `x' = α^s x = g x` 写成 `x' = α^s = g x`，丢失 x 因子，改变回归点定义；第 485 行在 `\mu_x^{12}([a,b])` 后多出无来源的 `1`。p.532 300dpi 裁片确认两处应分别保留 `α^s x` 与不带尾随 1 的区间记号；需手工修正。
- 复核：式 (4.4)/(4.5)、条件测度推前关系、两条轨道 x(r)/x′(r) 及后续 H-property 说明与 p.532 对应；除上述两项外未发现命题或段落遗漏。

## PDF p.021 / 印刷 p.533

- 时间：2026-10-01 20:58:15 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p021.png`（150dpi `pngmono`）；图注/编号终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p021_fig2_caption.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p021_eq_4_7_4_8.png`。
- Markdown 定位：Figure 2 与图注第 517–519 行；矩阵关系和 (4.7)/(4.8) 第 521–543 行。
- 核对：Figure 2 图与图注、(4.6) 的共轭矩阵、非 exceptional return 的四种情形、(4.7) 最大值界、(4.8) 的 g₂₁r 界及后续 X₁ 连续性段落。
- 结果：`FAIL`。
- 内容差异：印刷把最大值界单独编号为 (4.7)，把 `|g₂₁r| ≤ Cδ^{3/8}` 单独编号为 (4.8)；Markdown 第 529 行仅留裸 `(4.7)`，随后第 532 行把两条合入同一个数组并只标为 (4.8)，丢失等式与编号对应关系。另在收尾段把 `\mu_z^{12}` 写成带额外点号的 `\dot\mu_z^{12}`，且等式后漏句点；p.533 整页图确认应为普通 `\mu_z^{12}.`。需恢复两条分别编号的显示公式并去掉伪点/补回句点。
- 文字差异/源级 quirk：图注第 519 行把印刷 `differ` 写为 `difer`，少一个 f；印刷自身的 `noticably` 亦为原文拼写，保持不改。300dpi 图注裁片确认这两个字形。
- 复核：矩阵 (4.6) 的九个块、(4.7)/(4.8) 两个数值界、收尾条件测度标记及图中 x(r)/x′(r) 走向与 p.533 对应；主要 FAIL 为公式标签与分组错位，另有一处条件测度点号误识。

## PDF p.022 / 印刷 p.534

- 时间：2026-10-01 20:58:59 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p022.png`（150dpi `pngmono`）；prime 字形终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p022_A_prime.png`。
- Markdown 定位：第 543–567 行；含 low-entropy 假设、N 的扩张、X₁/X₂/X₃ 构造、式 (4.9)–(4.11) 和 §4.4 起始。
- 核对：A′ 返回定义与量词、X₁/X₂/X₃ 测度余量、(4.9)/(4.10)/(4.11) 积分/区间/指标、后续 z′=α^s z 条件。
- 结果：`FAIL`。
- 内容差异：第 543、545、567 行多处把 A′ prime 输出为 HTML 上标中的控制字符 `U+0006`，破坏 subgroup 标签且无法可靠显示；p.534 裁片确认均应为 prime。第 549 行还把文献 `[20, App. A]` 拆成 `[2 0, App. A]`，需恢复引用号。
- 复核：(4.9) 的区间积分与 `(1−ε²)` 测度界、(4.10) 的 X(ρ) 集及 (4.11) 两个时间平均式均与 p.534 对应；本页实质差异在 prime/control 字符及参考编号格式。

## PDF p.023 / 印刷 p.535

- 时间：2026-10-01 20:59:37 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p023.png`（150dpi `pngmono`）；双 f 字形裁片：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p023_different.png`。
- Markdown 定位：第 569–595 行；包括 z′ 与 κ(z,z′)、(4.12)、取 r 的范数估计、Figure 3、Lemma 4.5 与 (4.13)。
- 核对：κ 的四个控制项/区间上界、r=κ^{-1} 的分情形论证、Figure 3 的 x/x′ 轨迹及图注、Lemma 4.5 参数 T/η/θ 和 conditional-measure 比值。
- 结果：`PASS±`。
- 差异：第 579 行两处将印刷 `differ` / `difference` 写成 `difer` / `diference`，各少一个 `f`；300dpi 裁片确认印刷双 f，列入全篇后的逐处拼写修复。
- 复核：式 (4.12) 的绝对值/范数、`1/2` 指数、(4.7)/(4.8) 引用及式 (4.13) 的 ρS/S 区间比例均相符；Figure 3 位图及 caption 均保留。

## PDF p.024 / 印刷 p.536

- 时间：2026-10-01 21:00:23 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p024.png`（150dpi `pngmono`）。
- Markdown 定位：第 601–631 行，并核对第 597/599 行嵌入的 Figure 4 图与 caption。
- 核对：Q₁/Q₂/Q₃ 定义及密度、y=α^{-w t}x 的代换、(4.10) 测度界、条件测度比值变换和 (4.13) 结论；比较图中的 z/x/y、u(S)x、u(ρS)x、u(1)y 标注与随附 MinerU 位图。
- 结果：`PASS±`。
- 源级 quirk：印刷句本身写作 `A direct calculations shows`；Markdown 忠实保留，不擅改原文语法。Equation (4.13) 和 Figure 4 caption 与印刷相符，嵌图的路径图及全部点/轨道标签也匹配。
- 复核：公式右端的 1/2 比值、S=e^{2w}=e^{θ−ητ}、P′ 对 z′ 的对称构造及下一 Lemma 过渡均存在；未发现 OCR 数学内容错误或段落缺失。

## PDF p.025 / 印刷 p.537

- 时间：2026-10-01 21:01:14 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p025.png`（150dpi `pngmono`）。
- Markdown 定位：第 633–671 行；覆盖 Lemma 4.6、(4.14)、κ_a/κ_u、矩阵 (4.15)、κ 的界 (4.16) 与 P_a/P_u 定义。
- 核对：T 的 1/4 因子、ε<1/100、(1)–(3) 条件、ρ^{-5}R、两条条件测度半质量不等式、(4.15) 的矩阵指数、(4.16) 的 3/4 与 3/8 指数及区间端点。
- 结果：`PASS±`。
- 差异：第 671 行在印刷区间 `[4T,5T]` 后多一个 `]`，应去掉以保持公式分隔正确；第 633 行 `If` 和部分 display math 存在字母间隔/空格扁平化，含义仍可辨。
- 复核：(4.14) 两个 x/x′ 的区间测度界、(4.15) 全矩阵共轭和 (4.16) 所有界及 P_a/P_u 的定义均与 p.537 对应，无数学项遗漏。

## PDF p.026 / 印刷 p.538

- 时间：2026-10-01 23:02:43 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p026.png`（150dpi `pngmono`）；终裁裁片：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p026_A_prime.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p026_differences.png`。
- Markdown 定位：第 671–706 行；完成 P_u/P_a 密度交集，进入 §4.5 并构造 x(r), x′(r) 与矩阵 g̃(r)。
- 核对：S_u 与 κ_u 关系、四集合交集的密度、x/x′∈X₂、条件测度相等、P/P′ 定义及 g̃(r) 的矩阵块。
- 结果：`FAIL`。
- 内容差异：第 681 行用控制字符 `U+0006` 代替 `A′` 中的 prime，破坏 returns 所依赖的群标签；p.538 300dpi 裁片确认应为 A′，须手工恢复。
- 文字瑕疵：第 679 行两处 `diference` 少一个 f；300dpi 裁片确认印刷为 `difference`，列入拼写修复。
- 跨页排版差异：第 4.4 段在 p.538 末尾停于 “we can find … αˢ∈A′”，并在 p.539 另起孤立的 “with z′=…” 从句；两页相邻源文确认它们属于同一句，终修时接回。
- 复核：P_a/P_u 的定义、S_a/S_u、P_a∩P_a′∩P_u∩P_u′ 的密度下界和 g̃(r) 各矩阵块与 p.538 对应，无其他已发现的内容差异。

## PDF p.027 / 印刷 p.539

- 时间：2026-10-01 23:18:05 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p027.png`（150dpi `pngmono`）；公式/编号终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p027_eq_4_20_4_21.png`。
- Markdown 定位：第 711–764 行；包括 (4.18) 推导、R 的极值控制、(4.19)–(4.22) 及后续非 exceptional returns 序列。
- 核对：g̃₂₁r 上界、(4.19) 极值范围、两个 cancellation 例外条件及其方程号、ρ²/2 界、(4.22) 下界、ρ^{-5}R/ρ^{-4}R 区间论证。
- 结果：`FAIL`。
- 内容差异：Markdown 第 723 行把标量 `(a₂−a₁)r` 写成带多余下标的 `(a₂−a₁)_i r`；且印刷 (4.20) 的最大值下界被标为 (4.21)，印刷 (4.21) 的近抵消不等式则没有对应标签。p.539 的 300dpi 裁片确认 scalar 和编号配对，需恢复。
- 文字瑕疵：第 723 行 `diferences` 少一个 f，按字形证据逐处拼写修复。
- 复核：同页 (4.19)、(4.22)、ρ^{-4}≤max≤ρ^{-5}、ρ^{-6}−ρ^{-5}>0 及末尾条件测度相等式均与原文对应；本页实质 FAIL 是多余下标和 (4.20)/(4.21) 错位。

## PDF p.028 / 印刷 p.540

- 时间：2026-10-01 23:37:58 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p028.png`（150dpi `pngmono`）；prime 字形裁决：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p028_A_prime.png`。
- Markdown 定位：第 767–793 行；含 compactness 得出两点的矛盾、§5、A-normalized SL(2,R) 子群背景、Theorem 5.1、Proposition 5.2 及 Lemma 5.3 开头。
- 核对：y′∈Uy 且 y′≠y、conditional measure 连续性、Theorem 5.1 的三个特征值结论、Proposition 5.2 的整数矩阵推论与特征多项式论证。
- 结果：`FAIL`。
- 内容差异：Markdown 第 773、775 行把 A′ 中的 prime 导出为 `U+0006` 控制字符，污染 ergodic/invariant measure 的群标签；p.540 300dpi 裁片确认印刷为 A′，需恢复 prime。
- 文字瑕疵：第 789 行 `coeficients` 少一个 f；印刷为 `coefficients`，列入拼写修复。
- 复核：Theorem 5.1 三个 eigenvalue conditions、Proposition 5.2 的不存在性陈述与根的重数论证均与 p.540 对应。

## PDF p.029 / 印刷 p.541

- 时间：2026-10-01 23:54:45 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p029.png`（150dpi `pngmono`）；特征值表达式终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p029_diag_eigenvalues.png`；外幂极限裁片：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p029_wedge_limit.png`。
- Markdown 定位：第 793–848 行；覆盖 Lemma 5.3、对数特征值扰动界、锥构造、外幂论证及 (5.1)。
- 核对：Lemma 5.3 的谱隔离前提、f=diag(e^{λ_i}) 的定义、η_i/λ′_i 关系、锥 K/K′、范数增长和 (5.1) 的求和界。
- 结果：`FAIL`。
- 内容差异：第 795 行把印刷 `diag(e^{λ_1},e^{λ_2},…,e^{λ_m})` 写为 `diag(e_1^λ,e_2^λ,…,e_m^λ)`，把下标从指数 λ_i 移到底数 e_i，改变矩阵特征值定义。p.541 300dpi 裁片确认应为 e 的 λ_i 次幂，需修复。
- 其他伪影：第 845 行在 `Clearly` 前有 U+0018 控制字符，应在逐处人工修复时移除；外幂极限处的 `(f′∧f′)^n` 与印刷 `f′^n∧f′^n` 依外幂表示的乘法关系相符，裁片未见数学偏差。
- 复核：本页 (5.1) 的绝对值求和、C_iδ 界、以及谱距 <1/2 推论与 p.541 对应；FAIL 集中在 f 的对角特征值表示。

## PDF p.030 / 印刷 p.542

- 时间：2026-10-02 00:01:27 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p030.png`（150dpi `pngmono`）。
- Markdown 定位：第 851–887 行；从 Lemma 5.3 的谱间距推论，经过 Theorem 5.1 证明与 (5.2)，至 §6 结论起始。
- 核对：λ_i′ 两两不同/实正特征值推论、a(t)∈A′ 及 λ₁=λ₂ 条件、U₁ 构造与对称性、t₀ 界、Poincaré recurrence、(5.2)、f′ 特征值误差界和章节转换。
- 结果：`PASS±`。
- 差异：第 853 行 `a=1` 与 `b=2` 之间缺少标点/空格；若干 display math 与变量间距扁平化。数学条件和矩阵指数未变。
- 复核：U₁ 的底块因子 e^{-2r/(k−2)}h、γ̃∈U₁a(t)∩gΓg^{-1}、|λᵢ−λⱼ|t>2 与 |λ′ᵢ−λᵢt|<3/4 均与 p.542 对应。

## PDF p.031 / 印刷 p.543

- 时间：2026-10-02 00:36:09 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p031.png`（150dpi `pngmono`）；群符号/脚注证据：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p031_normalized_by_A.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p031_footnote_3.png`。
- Markdown 定位：第 889–903 行；覆盖 Theorem 2.1 的 (1)/(2)、等价关系与 H 的构造、Ratner 定理过渡、Theorem 6.1 及脚注 3。
- 核对：两个条件测度分支、等价关系闭包、H=∏SL(kᵢ,R)、H 对 A 的规范化、class A 定义、Theorem 6.1 与脚注3的引文说明。
- 结果：`FAIL`。
- 内容差异：第 895 行把印刷 “H is normalized by A” 误成 “by A_i”，添加不存在的下标；同一行另在 “permuting the indices” 中混入 U+0005 控制字符。脚注 3 在 Markdown 中分成独立 `G,` 片段和缺 G 的主句（第 901/903 行），导致“closed subgroup of G”断裂；p.543 300dpi 裁片确认该 G 应并回脚注句中。
- 复核：Theorem 2.1 的二分、H 的直积结构、Theorem 6.1 的前提与结论及其余脚注文字均有对应；FAIL 集中在 A 的下标和脚注/控制字符。

## PDF p.032 / 印刷 p.544

- 时间：2026-10-02 00:43:43 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p032.png`（150dpi `pngmono`）；终裁裁片：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p032_S_N_G.png`、`audit/300dpi/Lindenstrauss_2007_littlewood_published_p032_h0_block.png`。
- Markdown 定位：第 907–933 行；含 S_N^G(L) 正规化集、Lemma 6.2、h₀ 块矩阵、V_g 不变空间、逃逸轨迹及 Theorem 1.3 收尾。
- 核对：H̃ 的归属关系、保持 Haar 测度的 normalizer 记号/轨道、h₀ 的块对角结构、式 (6.1)、V_g 的有理维数论证、a(t)gm→0 及最终 H=L 推导。
- 结果：`FAIL`。
- 内容差异：第 915 行把印刷的 h₀=diag(h′₀,I_{k−k′}) 块矩阵拆成 `\\binom{h'_0}{0}`、游离 I 与 `\\int`，丢失右上零块和完整下块布局，无法保持 h₀ 的 block-diagonal 条件；p.544 300dpi 裁片确认原矩阵。第 907 行 S_N^G(L) 的上下标/组符号和末尾 “-orbit” 也被拆成 `S N_G(L)_{\\neg Orbit}`，需按印刷记号恢复。
- 源级 quirk：PDF 确实写作 `conjunction by g preserves Haar measure`；按 print 优先原则原样保留，不改为 conjugation。
- 复核：式 (6.1) 两个不动向量空间、整数向量选择和逃逸结论均与 p.544 对应；本页 FAIL 集中在 normalizer-set 记号和 h₀ 块矩阵。

## PDF p.033 / 印刷 p.545

- 时间：2026-10-02 01:02:26 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p033.png`（150dpi `pngmono`）；群作用/不变性证据：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p033_AH_invariant.png`。
- Markdown 定位：第 935–959 行；覆盖 Lemma 6.2 推出 sum k_i=k、S_N^G(H)=AH、Corollary 1.4 及 Part 2/§7 起始。
- 核对：sum k_i 的完备性结论、normalizer 集等式、AH-orbit 上的不变概率测度、Corollary 1.4 的有理群/各向异性环面论证及 mod m 子群描述。
- 结果：`FAIL`。
- 内容差异：第 945 行把印刷 `AH-invariant` 错排为数学下标 `AH_{-}`-invariant；将文字连字符误纳入 H 的下标，改变群名。p.545 300dpi 裁片确认原文是 AH 后接普通连字符。
- 额外控制字符：第 937 行含 U+0005，夹在逃逸轨迹句的 “of A” 周围，属 MinerU 伪字符，应手工移除。
- 源级 quirk：`This show` 及关于 A≅R^{k−1} “compact” 的措辞来自印刷原文；与 Markdown 相符，保留并作为 source quirk，不按数学预期修改。
- 复核：S_N^G(H)=N_G(H)=AH、单一 AH-orbit、Corollary 1.4 的 L reductive 及最终 L=SL(k,R) 条件均与 p.545 对应；主要 FAIL 是 AH-invariant 记号污染。

## PDF p.034 / 印刷 p.546

- 时间：2026-10-02 01:16:34 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p034.png`（150dpi `pngmono`）；维数记号终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p034_dim_H.png`。
- Markdown 定位：第 961–1004 行；覆盖 Hausdorff measure/dimension、box dimension、(7.1)–(7.4)、乘积空间估计及 topological entropy 定义 (7.5)。
- 核对：Hausdorff 维数下标、ε-cover infimum、dim_H/dim_box 关系、Lipschitz invariant statement、countable-union formula、product metric 与 entropy 极限。
- 结果：`FAIL`。
- 内容差异：第 967 行把印刷的 `dim_H(B)` 转录成 `dim_{·H}(B)`，额外引入点状下标，改变 Hausdorff dimension 符号。p.546 300dpi 裁片确认应为 `dim_H(B)`；需修正。
- 文字瑕疵：本页多处 `Hausdorf`、`diferent`、`suficient` 分别丢失双 f 中一个 f，影响术语检索；列入全篇结束后的逐处拼写修复。
- 复核：方程 (7.1)–(7.5) 的表达式与标签存在，分母 |log ε|、ε→0/N→∞ 次序、计数可分集合和 product-space max metric 与 p.546 对应；FAIL 集中在正文 dim_H 记号。

## PDF p.035 / 印刷 p.547

- 时间：2026-10-02 01:34:12 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p035.png`（150dpi `pngmono`）；map notation 终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p035_map_arrow.png`。
- Markdown 定位：第 1010–1053 行；覆盖 finite-partition entropy、metric entropy 的超确界/变分原理和 §8/ Lemma 8.1 起始。
- 核对：H_μ(P) 求和、P∨Q common refinement、h_μ(T,P) 的条件分割、(7.6)/(7.7) 以及 T 的定义域/陪域。
- 结果：`FAIL`。
- 内容差异：第 1027 行把印刷 `T:Y→Y` 转成 `T : Y Y`，丢失 map arrow，未完整表示连续映射的陪域。p.547 的 300dpi 裁片确认箭头清晰，需恢复为 `T:Y\to Y`。
- 复核：finite partition entropy、(7.6) 对分割取 supremum、h_μ(T)≤h_top(T)、(7.7) 对不变测度取 supremum 与 p.547 相符；本页 FAIL 集中在 T 的函数签名。

## PDF p.036 / 印刷 p.548

- 时间：2026-10-02 02:18:55 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p036.png`（150dpi `pngmono`）。
- Markdown 定位：第 1055–1084 行；局部空间同胚、U/V/C 子群、乘积坐标 (8.1) 及 Lemma 8.2。
- 核对：C/U/V 的收缩定义、按矩阵系数判定、g_Cg_Ug_V 唯一分解、(8.1) 距离比较、Lemma 8.2 的 ε/λ/N 前提和结论。
- 结果：`PASS±`。
- 差异：第 1075 行把 “conjugation with a” 拆成 `with $^{a,}$`，引入游离上标和逗号；PDF 文本层保留了普通 a。该处是可读性/格式瑕疵，后续可逐处恢复为短语。
- 复核：U/V 定义的正负极限方向、C 的固定点条件、(8.1) 中最大距离与 Lemma 8.2 的指数增长结论均与 p.548 对应，无公式项缺失。

## PDF p.037 / 印刷 p.549

- 时间：2026-10-02 02:29:49 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p037.png`（150dpi `pngmono`）；结论裁片：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p037_entropy_conclusion.png`。
- Markdown 定位：第 1087–1109 行；覆盖 Proposition 8.3、(8.2)、(N,ε)-分离集构造、熵增长结论和 Lemma 8.4 起始。
- 核对：两种命题分支、P_y 条件、F_N 的基数界、Lemma 8.2 导出的分离性以及最后的拓扑熵主张。
- 结果：`FAIL`。
- 内容差异：第 1105 行写为 `h_top(α^t)`，印刷结论是 `h_top(a|_K)`；Markdown 丢掉了熵所取的限制空间 K，扩大了主张范围。p.549 300dpi 裁片确认原文为 `a|_K`，需恢复。
- 文字瑕疵：第 1103 行 `sufices`、第 1105 行 `diferent` 分别少一个 f，列入人工拼写修复。
- 复核：Proposition 8.3 的两个备选、分离集证明与 `b log λ > 0` 的阈值推导均与 p.549 对应；主要 FAIL 是最后熵主张漏掉 restriction K。

## PDF p.038 / 印刷 p.550

- 时间：2026-10-02 02:59:29 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p038.png`（150dpi `pngmono`；此页亦为密集数学页整页视觉抽检）；共轭式终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p038_conjugation.png`。
- Markdown 定位：第 1111–1143 行；包括 Lemma 8.4 的积球包含、U/V 扩张、距离分解 (8.3)、迭代分离及 Lemma 8.5。
- 核对：右不变度量估计、a 对 U/V 的共轭扩张、f=f_C f_U f_V 分解、(8.3)、选择 |n|<N 的分离点结论。
- 结果：`FAIL`。
- 内容差异：第 1119 行把印刷 `B_{c_1^{-1}r}^{G}` 误写为 `B_{c_1^{-1}r}^{\dot G}`，并将 `a^{-1}fa` 写成 `a^{-1}f\dot a`，两处额外添加点号并改变作用符号。p.550 300dpi 裁片确认原式为无点的 G 和 a，需逐处删除伪点。
- 复核：Lemma 8.4 的 `a^n gx` 分离结论、(8.3) 常数因子及 Lemma 8.5 的 entropy/dimension 二分与 p.550 相符；FAIL 集中在共轭式的错误点标记。

## PDF p.039 / 印刷 p.551

- 时间：2026-10-02 03:14:59 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p039.png`（150dpi `pngmono`）。
- Markdown 定位：第 1145–1180 行；§9 上半部，覆盖 upper semi-continuity 动机、条件熵定义/基本性质和 metric entropy 的条件表示。
- 核对：a-invariant measures 的 weak* 收敛主张、σ-algebra atoms、条件测度、条件熵加法/单调性/零值判据及 h_μ(T,Q) 公式。
- 结果：`PASS±`。
- 差异：`lim sup`、entropy 标识符与投影分割公式有 LaTeX 空格/字母间隔扁平化；运算符与求和范围仍可辨，未发现公式方向或量词改变。
- 复核：本页段落顺序、条件熵四项性质与 `T^{-n}Q` 条件表示均与 p.551 对应；未发现公式编号、变量或段落遗漏。

## PDF p.040 / 印刷 p.552

- 时间：2026-10-02 03:28:24 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p040.png`（150dpi `pngmono`）；Lemma 8.4 引用证据：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p040_lemma_8_4_reference.png`。
- Markdown 定位：第 1185–1211 行；相对熵公式 (9.1)/(9.2)、Lemma 9.1 与 proof of Proposition 9.2 的设置部分。
- 核对：T-invariant σ-algebra 条件、条件熵分解、有限分割序列及 Borel σ-algebra、K′ 的交集指标、Lemma 8.4 的半径前提和沿 P 的轨道 σ-algebra。
- 结果：`PASS±`。
- 差异：第 1209 行把印刷 `\bigcap_{n\geq0}a^nK` 转为 `\bigcap_{n>0}a^nK`；在本段 aK⊂K 前提下交集结果不变，但应按原式校正。第 1211 行在 “Lemma 8.4” 后插入 `\AA`；p.552 300dpi 裁片确认原文无此符号，应移除。
- 复核： (9.1)/(9.2)、Q_m 的细化与零边界性质、条件 entropy vanishing 条件及 aK=K 的归一化设置与 p.552 对应；所列差异不改变本页目标结论。

## PDF p.041 / 印刷 p.553

- 时间：2026-10-02 04:11:34 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p041.png`（150dpi `pngmono`）；分割原子项裁片：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p041_partition_index.png`。
- Markdown 定位：第 1213–1251 行；覆盖同一 Ã-atom 推出 y=f_Cx、相对熵为零的证明，以及 Bi,j,g_C,ℓ 可数集构造。
- 核对：f_Cf_Uf_V 分解、距离界、(9.2) 熵分解、B_i,j,g_C,ℓ 定义、Q_i/Q_j 归属、抽取 g_C 近似和最终 i=j 推论。
- 结果：`FAIL`。
- 内容差异：第 1245 行把印刷 `a^n x ∈ Q_i` 重复转录成 `Q_i` 后又追加一个下标 i，形成损坏的 partition label；p.553 300dpi 裁片确认原文只有 Q_i。第 1213 行另有 `K$\$belong` 的多余转义符，需清理。
- 复核：与 Ã 的同一原子、g_C^{-1}Q_j 邻域、Poincaré recurrence 选出的 a^n x 及由同一 Ã-atom 推出 i=j 的证明次序相符；本页 FAIL 集中在 Q_i 标签。

## PDF p.042 / 印刷 p.554

- 时间：2026-10-02 04:12:43 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p042.png`（150dpi `pngmono`）；分割 join 操作终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p042_subadditive_infimum.png`。
- Markdown 定位：第 1253–1287 行；Corollary 9.3 的上半连续证明、有限分割 Q 的熵比较、次可加性推论及 §10 开始。
- 核对：Corollary 9.3 的量词/邻域、(1/N)H_μ(Q) 估计、弱* 邻域、h_ν(a) 上界及最后 subadditive infimum 中的 join 运算符。
- 结果：`FAIL`。
- 内容差异：第 1275 行将印刷 `\bigvee_{n=0}^{M-1} a^n \mathcal P`（分割的共同细化）识别为带横线的 `\bar{\mathsf V}`，改变条件分割运算符；p.554 300dpi 裁片确认是大 vee/join。第 1277 行节标题把 `Hausdorff` 拼成 `Hausdorf`；第 1287 行把印刷 `Mahler’s criterion` 污染为 `Mahler\mathrm{Ω^{,}s}`，页图与 `pdftotext -layout` 可确认原文短语。全篇审计后须逐处手工恢复。
- 格式瑕疵：第 1263 行在 `$\mu$` 后有多余转义 dollar，且 “make sure that 1” 的 1 与下一公式分子重复，需在手工整理相邻正文时清理。
- 复核：Corollary 9.3 的弱* 邻域控制和熵上界推理其余部分与 p.554 对应；FAIL 集中在条件分割符号及 §10 标题/criterion 拼写污染。

## PDF p.043 / 印刷 p.555

- 时间：2026-10-02 04:19:20 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p043.png`（150dpi `pngmono`）；标量/向量字形终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p043_cone_scalars.png`。
- Markdown 定位：第 1289–1317 行；开头定义 cone，随后是 Theorem 10.1 及完整证明。
- 核对：cone 的正标量与向量变量、Theorem 10.1 的有界轨道集与 Hausdorff 维数结论、(10.1)、Proposition 8.3 的二分、变分原理/平均测度、弱* 极限和遍历分解的证明链。
- 结果：`FAIL`。
- 内容差异：第 1289 行将印刷的普通标量 `r` 写成粗体 `\boldsymbol{r}`，而同句条件 `r > 0` 明确表明其为标量；300dpi 原页裁片确认该 `r` 不加粗。第 1305 行在 `aD_\rho \subset D_\rho.` 后插入无印刷对应物的 U+000E 控制字符。第 1297 行 `Hausdorf` 漏掉一个 `f`，第 1315 行 `afine` 漏掉 `f`。全篇审计后逐处手工修正并按原页复核。
- 复核：Theorem 10.1 中 `D_\rho` 的定义、紧性/正熵二分、对 `\nu_N` 的平均及熵相等式、`A`-不变弱* 极限和最终矛盾均与 p.555 对应；已列差异之外未发现该证明链缺段或条件/结论改变。

## PDF p.044 / 印刷 p.556

- 时间：2026-10-02 04:22:43 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p044.png`（150dpi `pngmono`）；映射及集合定义终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p044_psi_map.png`。
- Markdown 定位：第 1319–1351 行；transversal box dimension 定义、Theorem 10.2 与证明，及 §11 开头。
- 核对：横截集合和 `g_{ii}=1` 条件、Theorem 10.2 的有界 A-orbit 与维数结论、中心子群及球乘积、度量 `d_O`、双 Lipschitz 映射 `\psi`、`P/P'` 的定义关系和熵二分。
- 结果：`FAIL`。
- 内容差异：第 1339 行漏掉印刷映射 `\psi:O\to\mathrm{SL}(k,\mathbb R)` 中的 `\to`；300dpi 裁片确认该箭头。第 1341 行把恢复集合中的 `f_C` 写成分离的 `f c`，丢失大写 C 下标；同一裁片确认原文为 `(f_C,f_U,f_V)`。第 1327 行 `Hausdorf` 漏掉一个 `f`。全篇审计后按原页恢复映射与下标并逐处修正拼写。
- 复核：Theorem 10.2 的集合定义、`k-1` 维数结论、紧集 `D_\rho`、`P'` 横截切片及其到 `D_\rho` 的像和最终维数推论顺序与 p.556 对应；除已列箭头/下标/拼写问题外，证明的关键包含关系与熵限制条件均保留。

## PDF p.045 / 印刷 p.557

- 时间：2026-10-02 04:24:25 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p045.png`（150dpi `pngmono`）；命题/下确界终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p045_littlewood_inf.png`；Dirichlet 步骤终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p045_dirichlet_epsilon.png`。
- Markdown 定位：第 1351–1393 行；Proposition 11.1、(11.1)/(11.2) 及其双向证明。
- 核对：Littlewood 条件与 `A^+`-轨道无界等价、`A^+` 半群、`\delta_{\mathbb R^k}` 的下确界、整数向量缩短、乘积估计、Dirichlet 逼近步骤及最终选择 `r,s` 的证明。
- 结果：`FAIL`。
- 内容差异：第 1365 行把印刷 `\inf_{a\in A^+}` 错转为 `\complement_{a\in A^+}`，破坏了论证中的下确界条件；p.557 300dpi 裁片确认是 `inf`。第 1373 行在 `\delta_{\mathbb R^k}` 后多出一个 `k`。第 1393 行在 `|qn(qnu+qm_1)|<\varepsilon^2` 后多出一个 `2`，并将定义条件 `for r,s` letter-space 成 `f o r`。全篇审计后逐处手工修正这些符号/字符。
- 源级 quirk：印刷原文自身写作 “By the the properties”；p.557 页图与文本层均显示重复冠词。Markdown 忠实保留，禁止顺手删改。
- 复核：方程 (11.1) 与 (11.2)、`(u,v)` 到 `\tau_{u,v}` 的格点构造、三坐标乘积界及 Dirichlet 推导的变量替换均与 p.557 相符；已列错误集中在下确界记号和 OCR 杂字。

## PDF p.046 / 印刷 p.558

- 时间：2026-10-02 04:26:17 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p046.png`（150dpi `pngmono`）；参考文献/重复作者符号终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p046_references.png`；作者地址/邮箱字形终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p046_affiliations.png`。
- Markdown 定位：第 1395–1425 行；Theorems 1.5/1.6 的证明、作者机构信息及 References [1]–[10]。
- 核对：Theorem 1.5 的嵌入与不稳定流形推论、Theorem 1.6 的向量范数条件、机构/地址、参考文献 [1]–[10] 的作者、标题、刊名及卷年页码。
- 结果：`FAIL`。
- 内容差异：第 1395 行两处 `Hausdorf` 少一个 `f`，且 `\mathbf t=(-2,1,1)` 后漏句点。第 1397 行 `m\notin\Xi_k` 后多出一个分号。第 1399 行第一机构地址丢失 `Clay Mathematics Institute` 后、`Cambridge` 后以及 `NJ` 后的逗号。第 1401 行把印刷邮箱 `katok_a@math.psu.edu` 中的下划线转录为空格。References [4]、[7] 的印刷重复作者长划线在第 1413、1419 行完全漏失；p.558 300dpi 裁片确认两处长划线。第 1425 行 `difeomorphisms` 少一个 `f`；裁片确认印刷为 `diffeomorphisms`。全篇审计后逐处修正并核对。
- 复核：Theorems 1.5/1.6 的映射、Hausdorff 维数结论和范数不等式均在 Markdown 中保留；References [1]–[10] 的题名、出版信息及其余作者与 p.558 对应。引用 [4]/[7] 的作者重复标记及上述拼写/标点是本页确认的差异。

## PDF p.047 / 印刷 p.559

- 时间：2026-10-02 04:40:39 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p047.png`（150dpi `pngmono`）；参考文献字形/重复作者终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p047_references.png`。
- Markdown 定位：第 1427–1469 行，References [11]–[32]。
- 核对：各条作者（包括重复作者长划线）、题名、期刊/丛书、卷年页码、出版信息与 preprint 标记。
- 结果：`FAIL`。
- 内容差异：References [16]、[17]、[24]、[27] 在第 1437、1439、1453、1459 行漏掉印刷的重复作者长划线；[25] 第 1455 行只留下一个 em dash，未保留印刷的三长划线。p.559 300dpi 裁片确认这些作者继承标记。第 1435 行 `Diferential` 少一个 `f`，第 1443 行 `difeomorphisms` 少一个 `f`。第 1437 行把 `Études` 的重音误放到 `Math` 后并破坏刊名标点；原页为 `Inst. Hautes Études Sci. Publ. Math. 79`，由裁片确认。全篇审计后逐处恢复作者标记、拼写、重音与刊名标点。
- 复核：References [11]–[32] 的其余作者、题名、出版物与卷年页码同 p.559 对应；[32] 的行末断词 `arith-` 在 Markdown 合并成完整单词 `arithmeticity`，无需修复。

## PDF p.048 / 印刷 p.560

- 时间：2026-10-02 04:43:08 UTC；actor=`Peer-P16`；model=`gpt-6-luna`；effort=`max`。
- PNG：`audit/Lindenstrauss_2007_littlewood_published_p048.png`（150dpi `pngmono`）；参考文献/收稿日期终裁：`audit/300dpi/Lindenstrauss_2007_littlewood_published_p048_references_dates.png`。
- Markdown 定位：第 1471–1503 行；References [33]–[49]；PDF 页末另有收稿/修订日期。
- 核对：References [33]–[49] 的作者/重复作者标记、题名中的数学符号、出版信息、卷年页码，以及 `(Received ...)` 与 `(Revised ...)` 两项日期。
- 结果：`FAIL`。
- 内容差异：第 1471 行 [33] 题名把 `H × ··· × H` 丢成两个相邻的 `H`；第 1485 行 [40] 将 `Zürich` 的重音误拆/错位为 `Z¨urich`，并漏掉重复作者长划线；第 1489 行 [42] 漏掉同一作者标记；第 1495 行 [45] 丢失 `×2`、`×3` 的乘号；第 1499 行 [47] 漏掉重复作者长划线。p.560 300dpi 裁片确认这些符号/标记。Markdown 在 [49] 后结束，漏掉 PDF 页末的 `(Received September 5, 2003)` 与 `(Revised January 25, 2005)`。全篇审计后逐处恢复。
- 源级 quirk：印刷本 [39] 作者栏自身为 `38`，而非作者名或重复作者线；印刷本 [40] 出版者自身拼作 `Birkhuser`。p.560 页图/裁片与文本层支持这两项印刷原貌；Markdown 忠实保留，禁止按预期改正。
- 复核：References [33]–[49] 的其余作者、题名、卷年页码和出版信息与 p.560 相符；References [41]、[43] 的重复作者长划线已保留，Received/Revised 日期为本页发现的页末漏录。

## 全篇终修总结与修复登记

- 全篇审计覆盖 PDF p.001–p.048（印刷 p.513–p.560）；原始 Markdown 基线的逐页等级为 `PASS` 0 页、`PASS±` 15 页、`FAIL` 33 页。这些是修复前基线判级，不是修复后的重新判级。
- 只读原件 PDF SHA-256：`7f26dde3f9b206534584b2b94d4a86e6319e467918efca8b4d00b1b1ae574825`。
- 原始 MinerU Markdown SHA-256：`52ea7deb84759ca9a6074968dcd23883cd0307c6194cb3ec931dfbca4df4937e`；该字节版本最后修改提交：`d351abbff700768968605937fac5c051de31bb0a`。
- 修复后的 Markdown SHA-256：`e92b0d19bd406e72c798834ac2b52e0660d6be0d143a4cd06ed96e675f7c75f9`；正文修复提交：`ed58d2e1bc15d51ea20d7b6288855eaae0d374ad`。
- 下列记录逐页对应前文 PDF 页图 `audit/Lindenstrauss_2007_littlewood_published_pNNN.png`，并使用每页记录所列的 300dpi 原页裁片处理字形/数学符号疑难。修复后已从头至尾复读最终 Markdown，并在后续 p.5、p.21 与 p.26 修订后再次完整复读；以下逐项是与终稿核对后的修复结果。

| PDF 页 / 印刷页 | 修复登记与终稿复核 |
|---|---|
| p.001 / 513 | 将摘要 `Hausdorf` 修为 `Hausdorff`；对照 p.001 全页图及 `p001_hausdorff` 裁片，终稿已确认。 |
| p.002 / 514 | 修正 `diferent` 的两处漏字母拼写及 `k>2` 句界标点；合并印刷断行造成的 `multi-plicative(ly)`；恢复损坏的 `n`/`m` 文字关系。保留印刷本的 `unipotents groups` 与 `Raghunatan`。对照 p.002 页图及 `p002_different_ligature` 裁片，终稿已确认。 |
| p.003 / 515 | 将 `diference` 修为 `difference`；(1.1) 的公式、最近整数距离和编号已对照 p.003 页图及相应 300dpi 裁片复核。 |
| p.004 / 516 | 重建 Theorem 1.5 中 `dim_H Ξ=0` 与 “In fact, Ξ is …” 句子；恢复两处 `lim inf` 表达式；修正 `Hausdorff` 与 `effective` 拼写。对照 `p004_theorem_1_5`、`p004_lim_inf_text` 裁片，终稿已确认。 |
| p.005 / 517 | 恢复 Conjecture 1.7 的 `n≥2` 前提；补回 `n≥3` 后句点，并整理后续 GL(2) 直积、集合 D 与维数说明中的 OCR/标点损坏。保留印刷拼写 `up to conjunction`、`tranversals`。对照 `p005_conjecture_n_ge_2` 及印刷拼写裁片，终稿已确认。 |
| p.006 / 518 | 修正 `suficient`、`dificulty`、`Hausdorf`、`diferent` 的双 f 拼写。对照 p.006 页图及 `p006_text_typos` 裁片，终稿已确认。 |
| p.007 / 519 | 补回行末句点并恢复 “with ‘low’” 中的空格；定理与段落内容已对照 p.007 页图复读。 |
| p.008 / 520 | 恢复 H-球作用式 `B^H_ε(x)=B^H_ε·x`，去除球与群记号中的伪点。对照 `p008_ball_notation` 裁片，终稿已确认。 |
| p.009 / 521 | 将被拆成多个 docvortex 片段、引用与 `U` 脱离的脚注 2 按印刷页重组为完整文本；相邻 X′ 记号也已复核。对照 `p009_footnote_2`、`p009_X_prime` 裁片，终稿已确认。 |
| p.010 / 522 | 恢复 `for any n,k` 中的普通变量，修复 `limsup` 及其变量/量词，并修正 `sufficiently`；保留印刷原文没有 x 的 “α^{nt} is in D_M”。对照 p.010 页图及两张终裁裁片，终稿已确认。 |
| p.011 / 523 | 删除条件测度 `μ_x^{ij}` 上的伪导数点，并整理最大遍历公式格式。对照 `p011_mu_ij`、`p011_maximal_ergodic_formula` 裁片，终稿已确认。 |
| p.012 / 524 | 恢复 `H_{ab}=⟨U_{ab},U_{ba}⟩` 的生成子群括号、普通斜体 `A'_{ab}` 和 remark 标签 prime。对照 `p012_group_H_ab`、`p012_remark_3_prime` 裁片，终稿已确认。 |
| p.013 / 525 | 删除 `G` 后的重复逗号；其余间距扁平化不改变陈述。对照 p.013 页图，终稿已确认。 |
| p.014 / 526 | 将 `difeomorphisms`、`diferent` 修为 `diffeomorphisms`、`different`。对照 p.014 页图及双 f 裁片，终稿已确认。 |
| p.015 / 527 | 补回图注句点并整理相关公式排版；图、图注与等式已对照 p.015 页图和公式裁片复核。 |
| p.016 / 528 | 将误排的花体 `\mathcal A'_{ab}` 统一为印刷普通斜体 `A'_{ab}`。对照 `p016_A_subgroup` 裁片，终稿已确认。 |
| p.017 / 529 | 恢复矩阵零块判据中的 `g_{2*}`。对照 `p017_matrix_text` 裁片，终稿已确认。 |
| p.018 / 530 | 恢复 exceptional-return 标签 A′ 中被控制字符替代的 prime，并删除条件测度 `A'_{ab}`-invariant 后多出的星号。对照 `p018_E_invariance` 裁片及 p.018 页图，终稿已确认。 |
| p.019 / 531 | 将条件测度误识别的 `ε` 恢复为脚本 `\mathcal E`，把 `μ_x^{\mathcal E}`-a.e. 量词放回正确位置；修正 `suffices`、`different`。对照 `p019_conditional_measure` 裁片，终稿已确认。 |
| p.020 / 532 | 恢复 `x'=α^s x=gx` 中丢失的 x 因子，并删除 `μ_x^{12}([a,b])` 后多出的 `1`。对照 `p020_recurrence_equation` 裁片，终稿已确认。 |
| p.021 / 533 | 将 (4.7) 最大值界与 (4.8) 不等式分开并恢复各自编号；删除 `μ_z^{12}` 上的伪点，并补回句末句点。对照 `p021_eq_4_7_4_8` 裁片，终稿已确认。 |
| p.022 / 534 | 将 A′ 标签中的控制字符恢复为 prime，并修复 `[20, App. A]` 引文。对照 `p022_A_prime` 裁片及 p.022 页图，终稿已确认。 |
| p.023 / 535 | 修复 `differ`、`difference` 的双 f 拼写，并整理相邻数学记号。对照 p.023 页图及 `p023_different` 裁片，终稿已确认。 |
| p.024 / 536 | 未改正文；经页图、文本层复核，保留印刷原文的 `A direct calculations shows`，不把 print quirk 当作 MinerU 错误。 |
| p.025 / 537 | 删除 `[4T,5T]` 后多出的 `]`，恢复公式分隔。对照 p.025 页图，终稿已确认。 |
| p.026 / 538 | 将控制字符恢复为 A′ prime，修正两处 `difference`；与 p.027 合并原 PDF 跨页拆开的 “we can find … α^s∈A′ with z′=…” 同一句。对照 `p026_A_prime`、`p026_differences` 及相邻 p.027 页图，终稿已确认。 |
| p.027 / 539 | 恢复标量 `(a₂−a₁)r`（删除多余下标），将最大值界与近抵消不等式分别标为 (4.20)/(4.21)，并修正 `differences`。跨页句已与 p.026 衔接。对照 `p027_eq_4_20_4_21` 裁片，终稿已确认。 |
| p.028 / 540 | 恢复 A′ 中被控制字符替代的 prime，并将 `coefficients` 拼写补全。对照 `p028_A_prime` 裁片，终稿已确认。 |
| p.029 / 541 | 恢复 `diag(e^{λ_1},…,e^{λ_m})` 的特征值指数位置，清理外幂极限表达式中的控制/排版伪影。对照 `p029_diag_eigenvalues`、`p029_wedge_limit` 裁片，终稿已确认。 |
| p.030 / 542 | 整理 `a=1`、`b=2` 条件间的标点和间距；矩阵指数及条件已对照 p.030 页图复核。 |
| p.031 / 543 | 删除 “normalized by A” 中不存在的下标 i 和混入的控制字符；重组被拆开的脚注 3，恢复 “closed subgroup of G”。对照 `p031_normalized_by_A`、`p031_footnote_3` 裁片，终稿已确认。 |
| p.032 / 544 | 恢复 `S_N^G(L)` 记号及 `h_0=\operatorname{diag}(h'_0,I_{k-k'})` 块对角矩阵。保留印刷原文 `conjunction by g preserves Haar measure`。对照 `p032_S_N_G`、`p032_h0_block` 裁片，终稿已确认。 |
| p.033 / 545 | 将 `AH` 与 `invariant` 间的排版错误改为普通连字符 `AH-invariant`。保留印刷原文 `This show` 及 “compact” 措辞。对照 `p033_AH_invariant` 裁片，终稿已确认。 |
| p.034 / 546 | 将 `dim_{·H}(B)` 恢复为 `dim_H(B)`，修正本页 `Hausdorff`、`different`、`sufficient` 等双 f 拼写及维数/度量排版。对照 `p034_dim_H` 裁片，终稿已确认。 |
| p.035 / 547 | 恢复映射陪域箭头 `T:Y\to Y`。对照 `p035_map_arrow` 裁片，终稿已确认。 |
| p.036 / 548 | 整理被拆坏的 “conjugation with a” 短语，移除游离上标和逗号。对照 p.036 页图，终稿已确认。 |
| p.037 / 549 | 将熵结论从错误的 `h_{top}(α^t)` 修为 `h_{top}(a\|_K)`，并修正 `suffices`、`different`。对照 `p037_entropy_conclusion` 裁片，终稿已确认。 |
| p.038 / 550 | 删除 `G` 与共轭式 `a^{-1}fa` 上的伪点，恢复正确的群球和作用记号。对照 `p038_conjugation` 裁片，终稿已确认。 |
| p.039 / 551 | 未改正文；保留尚可辨认且未改变求和范围/运算符的公式间距扁平化。p.039 页图复核未发现需修正文内容。 |
| p.040 / 552 | 将交集下标 `n>0` 改回印刷的 `n\geq0`，删除 Lemma 8.4 后无来源的 `\AA`。对照 `p040_lemma_8_4_reference` 裁片，终稿已确认。 |
| p.041 / 553 | 删除多余转义 `$`，修复 `a^n x∈Q_i` 中重复的分割下标。对照 `p041_partition_index` 裁片，终稿已确认。 |
| p.042 / 554 | 恢复共同细化的 `\bigvee_{n=0}^{M-1}a^n\mathcal P`，修正 `Hausdorff` 与 `Mahler’s criterion`，删除多余数学分隔符和重复的 `1`。对照 `p042_subadditive_infimum` 裁片，终稿已确认。 |
| p.043 / 555 | 将锥定义中的普通标量 `r` 恢复为非粗体，删除 U+000E 控制字符，修正 `Hausdorff`、`affine`。对照 `p043_cone_scalars` 裁片，终稿已确认。 |
| p.044 / 556 | 恢复 `\psi:O\to\mathrm{SL}(k,\mathbb R)` 的箭头和集合中的 `f_C` 下标，并修正 `Hausdorff`。对照 `p044_psi_map` 裁片，终稿已确认。 |
| p.045 / 557 | 将 `\complement` 修为 `\inf`，删除 `\delta_{\mathbb R^k}` 后多出的 `k` 与不等式后多出的 `2`，恢复 `for r,s`。保留印刷原文 `By the the properties`。对照 `p045_littlewood_inf`、`p045_dirichlet_epsilon` 裁片，终稿已确认。 |
| p.046 / 558 | 补回 Theorem 1.5 句点及地址标点，恢复邮箱 `katok_a@math.psu.edu` 的下划线；补回参考文献 [4]、[7] 的重复作者长划线并修正 `diffeomorphisms`。对照 `p046_affiliations`、`p046_references` 裁片，终稿已确认。 |
| p.047 / 559 | 补回 [16]、[17]、[24]、[27] 的重复作者长划线及 [25] 的三长划线；修正 `Differential`、`diffeomorphisms` 和 `Inst. Hautes Études Sci. Publ. Math. 79` 的重音/标点。对照 `p047_references` 裁片，终稿已确认。 |
| p.048 / 560 | 恢复 [33] 标题中的 `\mathbb H\times\cdots\times\mathbb H`、`Zürich` 重音、[40]/[42]/[47] 的重复作者标记及 [45] 的 `\times2`/`\times3`；补录 `(Received September 5, 2003)` 与 `(Revised January 25, 2005)`。保留 print quirk `[39]` 作者栏 `38` 和出版社拼法 `Birkhuser`。对照 `p048_references_dates` 裁片，终稿已确认。 |

### 终稿只读核验与范围

- 终稿 Markdown 复读后只读清点：48 个按序页节均在；引用的 PNG 均存在（108 个实际图片引用，另有模板 glob），48 张全页图存在；针对本次差异的拼写/控制字符残留数为 0；`\tag{}` 共 45 个且无重复；`git diff --check` 通过。脚本仅读取/清点，没有写入或格式化 Markdown；未新增或运行测试。
- 根 `README.md` 第 524 行将同一文件标为 79 页，与 PDF 实际 48 页及 `AUDIT-INDEX.md` 第 97 行的 48 页登记仍冲突；该根 README、`AUDIT-INDEX.md` 与 `AUDIT-PROGRESS.log` 均不属于 Peer-P16 写入范围，留给 canonical integrator 裁决/更新。
- 本报告和修复提交仍是 `CANDIDATE_NOT_CURRENT`，等待 Master-Luna 对 exact candidate OID、页面证据和目标分支变化做集成复核；本 Peer 未更新根进度/索引，也未 push。
