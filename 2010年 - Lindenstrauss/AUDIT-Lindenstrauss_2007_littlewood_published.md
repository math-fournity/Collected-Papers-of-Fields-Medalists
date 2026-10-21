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

---

# 追加段：redo 块 A（PDF p.1–p.8，actor=`linden07`）

- 性质：本段是对上方 Peer-P16 记录的**独立重做复核**，不继承其判定；每页重新渲染 PNG 目检 + `pdftotext` 文本层互证，唯一裁决源是印刷原页。
- 身份：actor=`linden07`；host=zcode Desktop；model=`opencode-go-chat/space-bunny-free`（本会话运行时自报）；effort=run 级配置，未暴露，记 `UNKNOWN`。cwd=`/Users/aurolafly/.zcode/worktrees/cpf-redo-Lindenstrauss_2007_littlewood_published`；branch=`cpf-redo/Lindenstrauss_2007_littlewood_published`。
- PDF 只读证据：`2010年 - Lindenstrauss/Lindenstrauss_2007_littlewood_published.pdf`，48 页，SHA-256=`7f26dde3f9b206534584b2b94d4a86e6319e467918efca8b4d00b1b1ae574825`（本段开工前实测）。
- 写入范围：本段只写本 AUDIT 文件与本篇 MinerU Markdown；未写根 `AUDIT-INDEX.md`／`AUDIT-PROGRESS.log`／`MEMORY.md`／`README.md`，未写 `audit-redo/`，未执行任何 git 写操作，未碰 PDF 与 mineru 配置。
- PNG 去向：本块指令要求 PNG 落在 `/tmp/linden07_audit_pNNN.png` 并按该路径登记。SOP 要求被引用的证据图不得只存在于 `/tmp`，故这些瞬时渲染的持久化归档留给 canonical integrator 在集成时按 `audit-redo/` 命名空间补齐；本块不越权创建。
- 与既有 `AUDIT-…published.redo.md`（Wf-R-P16，p.001–p.009）的关系：本段为同范围独立复核，二者结论若冲突以印刷原页为准并在下文逐条指明。

## p.001（PDF p.1 / 印刷 p.513）
- PNG：/tmp/linden07_audit_p001.png（pngmono 150dpi）
- 核对：题录页五点——刊名/卷年/页范围、标题、作者行（含星号脚注锚）、Abstract、§1 与 §1.1 节标题顺序、开篇三段、脚注全文
- 结果：PASS±（差异均为排版级，不误导）
- 差异列表：
  1. MD 缺页眉运行头「Annals of Mathematics, **164** (2006), 513–560」（150dpi 页图首行直证 + 文本层第 1 行）。属 MinerU 系统性省略运行头，不含内容，登记不改。
  2. 行内数学紧排缺空格：MD 第 7 行「measures on$\operatorname { S L } ( k , \mathbb { R } ) / \operatorname { S L } ( k , \mathbb { Z } )$which are invariant」，印刷为「measures on SL(k,ℝ)/SL(k,ℤ) which are invariant」（页面图 Abstract 第 1 行可读）。排版级，不改。
  3. 同一伪影见第 11 行「the space$\mathrm { S L } …$which can be identified」及「in$\mathbb { R } ^ { k }$」；同样为排版级。
- 印刷字形核对：Abstract 末句印刷作「has Hausdorff dimension zero」（ﬀ 连字），MD 第 7 行作 `Hausdorff`，**与印刷一致**（旧 Peer-P16 p.001 曾记此处为 `Hausdorf`，该缺陷已在其候选中被修掉，本段重检确认现值正确，予以确认）。
- 题录其余项逐句相符：标题行（第 1 行）、作者行（第 3 行 `Elon Lindenstrauss\*` 与星号锚）、§1 Introduction（第 9 行）、§1.1 斜体小节题（第 11 行）、三段正文（第 11/13/15 行前半）、脚注（第 17 行：NSF DMS-007133；DMS-0140497 与 DMS-0434403；Clay Mathematics Institute Long Term Prize fellow；American Institute of Mathematics；NSF Grant DMS-0222452）全部与印刷页一致，无段落丢失。本页 MD 无需修改。

## p.002（PDF p.2 / 印刷 p.514）
- PNG：/tmp/linden07_audit_p002.png（pngmono 150dpi）
- 核对：跨页段落延续（p.513「…regarding the actions」→「of general unipotents groups」至本页第 9 行）、§1.2 标题与首段、`For k = 2`/`k > 2` 两段、Conjecture 1.1 (Margulis) 全陈述、Furstenberg 半群段前半、运行头
- 结果：PASS±（差异均为排版级，不误导）
- 差异列表：
  1. MD 缺运行头「514 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（150dpi 页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  2. 行内数学紧排缺空格：MD 第 19 行「diagonal $k \times k$matrices」、第 21 行「For$k = 2$the acting group」「as an$\mathbb { R } ^ { k - 1 }$-action」、第 23 行「Let$\mu$be」「on$X = \mathrm{SL}\ldots$for$k \geq 3$」「group$L > A$so that」。排版级，不改。
  3. 黑板体拍平：印刷「isomorphic to **ℝ**」（页图第 16 行、文本层第 22 行）MD 第 21 行作普通 `R`。语义不变，不改。
- 印刷断词处理核对（重要）：印刷页末把「multi-plicatively」跨行断为 `multi-` / `plicatively`（页图倒数第 3–4 行、文本层第 43–44 行）；MD 第 25 行已作无缝 `multiplicatively independent integers`，属正确合词，非缺陷。
- print quirk 忠实保留：印刷作「of general **unipotents** groups」（页图首行）与「**Raghunatan**'s conjecture」（页图第 7 行、文本层第 8 行，Raghunathan 漏 h，印刷自身错拼）；MD 第 15 行同为 `unipotents groups`、`Raghunatan's conjecture`，**与印刷一致，不改正**。
- 其余核对：§1.2 段（left multiplication、group A、positive diagonal k×k matrices、split Cartan subgroup of SL(k,ℝ)、Weyl chamber flow [16]）、k=2 段（geodesic flow、modular surface、hyperbolic structure、Anosov、elliptic points）、k>2 段（ℝ^{k−1}-action、e.g. [16],[15]、partially hyperbolic、A-ergodic measures are rare）、Conjecture 1.1（X = SL(k,ℝ)/SL(k,ℤ)、k ≥ 3、closed connected L > A、single closed L-orbit）、Furstenberg 段（[25]、[17]、[6]、Σ_{m,n} = {m^k n^l}_{k,l≥1}、k.x = kx mod 1）逐项与印刷吻合。本页 MD 无需修改。

## p.003（PDF p.3 / 印刷 p.515）
- PNG：/tmp/linden07_audit_p003.png（pngmono 150dpi）
- 核对：跨页段落延续（semigroup 段收尾）、Rees 非代数测度段、Conjecture 1.2 (Littlewood (c. 1930)) 陈述、公式 (1.1) 全部要素、⟨w⟩ 定义、Theorem 1.3 陈述、[21] 段、Corollary 1.4 陈述、过渡句、运行头
- 结果：PASS±（1 处偏离已修复）
- 差异列表：
  1. **已修复**：MD 第 31 行 Conjecture 1.2 行末缺印刷逗号。印刷（页图 Conjecture 行末 + 文本层第 24 行）「For every $u, v \in \mathbb{R}$**,**」；MD 原件为 `For every$u , v \in \mathbb { R }$`。已用 Edit 改为 `For every$u , v \in \mathbb { R }$,`（补回紧接 (1.1) 的逗号）。
  2. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 515」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  3. 字形混排：MD 第 45 行 Corollary 1.4 内第二处 μ 用字面「µ」（U+00B5）而非 `$\mu$`（「if k is prime, µ is the unique」）。字形级、不误导，全篇一致类伪影，登记不改。
  4. 行内数学紧排缺空格：第 27 行「lattices$\Gamma < \mathrm{SL}…$for which」「measures on $X = \operatorname{SL}\ldots/\Gamma$(fortunately」「for$\Gamma = \mathrm{SL}(k,\mathbb{Z})$」；第 37 行「where$\langle w\rangle = \cdots$is the distance of$w \in \mathbb{R}$to the nearest integer」；第 41 行「Let$\mu$be」「on$X =$ $\mathrm{SL}\ldots$for$k \geq 3$」「Then$\mu$is algebraic」。排版级，不改。
  5. 定理头格式：印刷小型大写「CONJECTURE 1.2 / THEOREM 1.3 / COROLLARY 1.4」，MD 作普通文字。排版级、全篇一致，不改。
- 公式 (1.1) 逐要素核对（150dpi 页图 + 文本层双证）：`lim inf`，下标 `n → ∞`，乘性系数 `n`，两个最近整数距离因子 `⟨nu⟩⟨nv⟩`（尖括号），右端 `= 0`，末尾逗号，编号 `(1.1)`。MD 第 34 行 `\liminf _ {n \to \infty} n \langle n u \rangle \langle n v \rangle = 0,\tag{1.1}` **系数、因子、运算符、右端与编号全部吻合**。
- 定义核对：印刷「where ⟨w⟩ = min_{n∈ℤ} |w − n| is the distance of w ∈ ℝ to the nearest integer.」与 MD 第 37 行一致（仅紧排空格差异）。
- print quirk 忠实保留：印刷作「come from **A invariant** homogeneous subspaces」（A 后无连字符，页图第 18 行、文本层第 16 行）；MD 第 27 行同为 `A invariant homogeneous subspaces`，与印刷一致，**不改正**。
- 定理陈述逐句核对：Theorem 1.3（A-invariant and ergodic measure on X = SL(k,ℝ)/SL(k,ℤ)、k ≥ 3、some one-parameter subgroup of A、positive entropy、Then μ is algebraic）与 Corollary 1.4（Let μ be as in Theorem 1.3、not compactly supported、if k is prime、the unique SL(k,ℝ)-invariant measure on X）均与印刷完全吻合，无条件增删。

## p.004（PDF p.4 / 印刷 p.516）
- PNG：/tmp/linden07_audit_p004.png（pngmono 150dpi）
- 核对：Theorem 1.5 陈述与 Ξ 定义式、Cassels–Swinnerton-Dyer [1] 段、badly approximable 段与两处 `lim inf`、公式 (1.2)、k 线性型定义式 `m_i(x)=Σ_{j=1}^k m_ij x_j`、乘积式 `f_m=∏_{i=1}^k m_i`、Theorem 1.6 陈述与公式 (1.3)、A-invariance 收尾段、Section 10/11 段、Hee Oh [32] 过渡句、运行头
- 结果：PASS±（1 处偏离已修复）
- 差异列表：
  1. **已修复**：MD 第 75 行 Theorem 1.6 行末缺印刷逗号。印刷（页图 Theorem 1.6 第 2 行末 + 文本层第 42 行）「…for every $m \in \mathrm{SL}(k,\mathbb{R}) \setminus \Xi_k$**，**」（逗号后紧接展示式 (1.3)）；MD 原件无逗号。已用 Edit 补回 `…,`。
  2. MD 缺运行头「516 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  3. 运算符字距拍平：MD 第 52 行 `\operatorname * {l i m i n f} _ {n \to \infty}`（`lim inf` 被写成字距形式）。数学对象、极限方向与编号均正确，仅排版级，不改。
  4. 行内数学紧排缺空格：第 57 行「degree$\left[ K : \mathbb{Q} \right] = 3 )$」；第 67 行「linear forms$\begin{array}…\end{array}$」；第 73 行「where$m = ( m _ { i j } )$denotes the$k \times k$matrix」；第 75、81、83 行同类紧排。排版级，不改。
- Ξ 定义式逐要素核对（150dpi 页图第 3–4 行 + 文本层第 5–7 行）：左端 `Ξ =`、花括号、变量 `(u, v) ∈ ℝ²`、`:`、`lim inf` 下标 `n → ∞`、乘性系数 `n`、两个距离因子 `⟨nu⟩⟨nv⟩`、严格不等号 `> 0`、右花括号、句点。MD 第 52 行逐项吻合。
- Theorem 1.5 结论核对：印刷「Then the Hausdorff dimension **dim**_H Ξ = 0. In fact, Ξ is a countable union of compact sets with box dimension zero.」（页图第 5–6 行）；MD 第 55 行为 `Then the Hausdorff dimension $\dim _ { H } \Xi = 0$. In fact, $\Xi$ is a countable union of compact sets with box dimension zero.`——符号形式的 `dim_H Ξ = 0` 已保留（非意译），**与印刷一致**（该处旧缺陷已在前序候选中被修掉，本段确认现值正确）。
- 公式 (1.3) 逐要素核对：印刷（页图第 18 行、文本层第 44–45 行）「$\inf_{x \in \mathbb{Z}^k \setminus \{0\}} |f_m(x)| = 0.$」编号 (1.3)；MD 第 78 行 `\inf _ {\mathbf{x} \in \mathbb{Z}^k \setminus \{\mathbf{0}\}} | f_m(\mathbf{x}) | = 0.\tag{1.3}`——下标集合、绝对值、右端 0 与编号全部吻合。
- 其余逐项核对：(1.2) 集合元素（页图第 12 行 `{v ∈ ℝ : (u,v) satisfies (1.1)}`）、Hausdorff dimension one、[K : ℚ] = 3 句点、`liminf` 两处 >0/=0、m_i 的求和下限 1 上限 k 与系数下标 `m_ij x_j`、乘积 `∏_{i=1}^k`、Theorem 1.6 的维数 `k − 1` 与 `\Xi_k ⊂ SL(k,ℝ)`、A-invariant + transversally to the A-orbits、Section 10 and Section 11、Hee Oh [32] 全部与印刷吻合，无段落丢失。
- 印刷断词核对：印刷第 47–48 行把 `transver-` / `sally` 跨行断开；MD 第 81 行作无缝 `transversally`，属正确合词，非缺陷。

## p.005（PDF p.5 / 印刷 p.517）
- PNG：/tmp/linden07_audit_p005.png（pngmono 150dpi）
- 核对：Conjecture 1.7 (Margulis, 1993) 全陈述、U₁/U₂ 两个展示式矩阵、Hee Oh [33] 段、§1.3 Measure rigidity 两段、脚注 1、运行头
- 结果：PASS±（差异均为排版级/意译级，不误导；本页 MD 未修改）
- 差异列表：
  1. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 517」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  2. MD 第 101 行相对印刷有两处轻微意译：印刷「(or more precisely Theorem 10.2 which we prove…)」无逗号，MD 作「(or, more precisely, Theorem 10.2, which we prove…)」；印刷「see **Section 7 and Section 10**」，MD 作「see Sections 7 and 10」。语义与指称不变，不误导，登记不改。
  3. 字形：印刷的集合 𝒟（页图第 16、17 行「the set 𝒟 of possible intersections」「This set 𝒟」）MD 第 101 行作普通斜体 `$D$`。语义不变，不改。
  4. 行内紧排与字距伪影：第 99 行「Then Γ is commensurable」中 Γ 未加数学定界、「Hilbert modular$\boldsymbol { l a t t i c e ^ { 1 } }$」把加粗斜体拍平成字距形式；第 103 行「generated by$\times m , \times n$(again with$m ,$n not powers…」缺空格。排版级，不改。
- 展示式逐要素核对（150dpi 页图 + 文本层双证）：
  - 印刷 `U_1 = { (1 * ; 0 1) × ⋯ × (1 * ; 0 1) }`（上三角、`*` 在右上）——MD 第 90 行 `\left\{ \begin{array}{cc}1 & *\\0 & 1\end{array} \right\} \times \dots \times …` **矩阵元素、\times 链与上下三角方向全部吻合**；印刷该式后无句点，MD 亦无，一致。
  - 印刷 `U_2 = { (1 0 ; * 1) × ⋯ × (1 0 ; * 1) }.`（下三角、`*` 在左下，**式后带句点**）——MD 第 96 行同样元素、同样带句点，**吻合**。
- Conjecture 1.7 条件逐项核对（页图第 5–8 行、文本层第 14–17 行）：`n ≥ 2 copies of SL(2,ℝ)`；`Γ < G` discrete subgroup；`for both i = 1 and 2`；`Γ ∩ U_i is a lattice in U_i`；`for any proper connected normal subgroup N < G`；`Γ ∩ N ∩ U_i is trivial`；结论 `Γ is commensurable with a Hilbert modular lattice¹ up to conjunction in GL(2,ℝ)×⋯×GL(2,ℝ)`。MD 第 99 行**条件与结论完整无增删**。
- print quirk 忠实保留（两处，均按印刷原样）：① 印刷作「up to **conjunction** in GL(2,ℝ)×⋯×GL(2,ℝ)」（conjugation 之误拼，页图第 8 行），MD 第 99 行同为 `conjunction`，**不改**；② 印刷作「…regarding Hausdorff dimension and **tranversals**, and [33], [32] …」（漏 s，页图第 17 行、文本层第 30 行），MD 第 101 行同为 `tranversals`，**不改**。同段前句印刷拼写正常的 `transversally`（页图第 16 行）MD 第 101 行亦作 `transversally`，两处不可互换的印刷差异被正确保留。
- §1.3 两段核对：「Furstenberg problem: [22], [45], [12]」、Rudolph [45] 与 Johnson [12]、半群 `×m, ×n`、`m, n not powers of the same integer`、positive entropy → Lebesgue（MD 第 103 行）；`two commuting hyperbolic automorphisms of the three-dimensional torus`、R. Spatzier、`unified treatment`、`[17], [13]`、`in retrospect`（MD 第 105 行）——**逐句与印刷吻合**。注意本页印刷用词为 `three-dimensional torus`，与 p.518 印刷的 `three torus` 不同，两页不可混用（p.518 见本段后续页记录）。
- 脚注 1 核对：印刷（页图末行、文本层第 48 行）「For a definition of Hilbert modular lattices, see [33].」与 MD 第 107 行**逐字吻合**。

## p.006（PDF p.6 / 印刷 p.518）
- PNG：/tmp/linden07_audit_p006.png（pngmono 150dpi）
- 核对：conditional measures 段、positive entropy / δ-measure 段（含 `the three torus`）、Weyl chamber 附加假设段（weak* limits）、two new methods 过渡句、first method [3] 段（ℝ-split、Haar、nonsplit [4]、Hausdorff dimension at most 1）、different approach [20]/Host [9] 段与页末「Let A be an ℝ-split」、运行头
- 结果：PASS±（差异均为排版级/字形级，不误导；本页 MD 未修改）
- 差异列表：
  1. MD 缺运行头「518 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  2. 黑板体拍平：印刷「general **ℝ**-split semisimple Lie groups」（页图第 18 行、文本层第 30 行）与页末「Let A be an **ℝ**-split」（页图末行、文本层第 45 行），MD 第 117、119 行两处均作普通 `R-split`。语义不变，登记不改。
  3. 花括号重复：MD 第 117 行 `$\mathrm { { S L } } ( k , \mathbb { R } )$` 多一层花括号，渲染结果仍是 `SL`，排版级，不改。
  4. 行内紧排缺空格：第 109 行「measure$\mu$on certain」；第 111 行「with respect to$\mu ,$these … information about$\mu .$Hence」；第 117 行「that if$\mu$is an A-invariant」「$X = \mathrm{SL}\ldots/\Gamma$, and if the entropies of$\mu$with respect to all」「for$\Gamma = \mathrm{SL}(k,\mathbb{Z})$but for every discrete subgroup Γ」；第 119 行「Let A be an R-split」。排版级，不改。
  5. 强调丢失：印刷第 19 行「with respect to **all** one-parameter groups」的 `all` 为斜体强调，MD 第 117 行作普通体。语义不变，不改。
- 逐段核对：conditional measures 段（stable/unstable foliations、Lyapunov exponents、unipotent subgroups normalized by the action）与 MD 第 109 行**逐句吻合**；positive entropy 段（`well-known to be δ-measure supported on a single point`、`limited to study actions where at least one element has positive entropy`、`method of [17]`）与第 111 行**逐句吻合**；附加假设段（`if the flow along every singular direction in the Weyl chamber is ergodic (though a weaker hypothesis is sufficient)`、`not stable under weak∗ limits`、`precludes applying the results from [17]`）与第 113 行**逐句吻合**（`weak<sup>∗</sup> limits` 上标星号已保留）。
- print quirk 忠实保留：印刷作「two commuting hyperbolic automorphisms of **the three torus**」（页图第 15–16 行、文本层第 16–17 行），MD 第 111 行同为 `the three torus`，**不改**；此处与 p.517 印刷的 `three-dimensional torus`（MD 第 105 行）是印刷自身的页间差异，两处均按各自原页保留，互不串改。
- first method 段核对：`developed by the first and second authors [3]`、`idea mentioned at the end of [17]`、`noncommutativity of the above-mentioned foliations (or more precisely, of the corresponding unipotent groups)`、`μ is an A-invariant measure on X = SL(k,ℝ)/Γ`、`entropies … are positive, then μ is the Haar measure`、`for every discrete subgroup Γ`、`An extension to the nonsplit case appeared in [4]`、`Hausdorff dimension at most 1` —— MD 第 117 行**逐项吻合**，无增删。
- [20] 段核对：`quantum unique ergodicity conjecture [20]`、`geodesic flow, which is not rigid`、`following Host [9]`、`A special case of the main theorem of [20] is the following: Let A be an ℝ-split`（页末断句）—— MD 第 119 行**吻合**，页面断点与 MD 段落位置对应正确，无段落丢失或错接。

## p.007（PDF p.7 / 印刷 p.519）
- PNG：/tmp/linden07_audit_p007.png（pngmono 150dpi）
- 核对：[20] 方法补段收尾（Cartan subgroup…、A-ergodic measure on SL(2,ℝ)×SL(2,ℝ)/Γ、irreducible lattice）、complementary 段（"high"/"low" entropy、Theorem 2.1 预告）、[20] proof 段（`is based on study of`、H-property、[28] §1.5、a priori）、Ledrappier-Young [19] / Tomanov–Margulis [26] 段、Acknowledgment 全段、`Part I. Measure rigidity` 标题、§2 起始段（`We shall implicitly` 断句）、运行头
- 结果：PASS±（差异均为排版级，不误导；本页 MD 未修改）
- 差异列表：
  1. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 519」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  2. 格式丢失：印刷「*Acknowledgment.*」为斜体小节头（页图第 17 行），MD 第 129 行作普通文字 `Acknowledgment.`。排版级，不改。
  3. 多余花括号：MD 第 133 行 `$G = { \mathrm { S L } } ( k , \mathbb { R } )$` 多一层 `{ }`，渲染仍为 `SL(k,ℝ)`，排版级，不改。
  4. 行内紧排缺空格：第 121 行「Cartan subgroup of$…$」「on$…$for which」「is$\mathrm{e.g.}$an irreducible」「in$…$」；第 125 行「behavior of$\mu$along」「a measure$\mu$which is **a priori** not even」；第 133 行「let$G = { \mathrm{SL} }…$for some$k \geq 3 ,$let Γ be a discrete subgroup of$G ,$and let$X = G/\Gamma$」「we let $A < G$denote the group of$k \times k$positive diagonal matrices」。排版级，不改。
- print quirk 忠实保留：印刷作「measures for which many one-parameter **subgroup** have positive entropy」（`subgroup` 单数配 many，页图第 6 行、文本层第 12 行），MD 第 123 行同为 `many one-parameter subgroup have`，**与印刷一致，不改正**。
- 逐段核对：`Cartan subgroup of SL(2,ℝ) × SL(2,ℝ)`、`Any A-ergodic measure on SL(2,ℝ) × SL(2,ℝ)/Γ for which some one-parameter subgroup of A acts with positive entropy is algebraic`、`the methods of [3] are not applicable`（MD 第 121 行）；`The method of [20] can be adapted to quotients of more general groups, and in particular to SL(k, ℝ)`、`measures with "high" entropy`、`measures with "low" (but positive) entropy`、`give Theorem 1.3 (as well as the more general Theorem 2.1 below for more general quotients)`（第 123 行）；`is based on **study of** the behavior of μ along certain unipotent trajectories`、`introduced by Ratner in [39], [38]`、`the H-property`、`nicely exposed in Section 1.5 of [28]`、`applied **on** a measure μ which is *a priori* not even quasi-invariant`（第 125 行）——印刷的两处非标准介词（`on study of` 的省略冠词、`applied on a measure`）被**忠实保留**，未按语法直觉擅改，与印刷逐句吻合。
- Ledrappier-Young 段核对：`we use a variant on the Ledrappier-Young entropy formula [19]`、`one of the simplifying ideas in G. Tomanov and Margulis' alternative proof of Ratner's theorem [26]`（MD 第 127 行）——**吻合**。
- Acknowledgment 全段核对：Dave Morris Witte / nonisotropic tori、Barak Weiss / multiparametric actions、Sanju Velani、M. Ratner and the referees、Newton Institute for Mathematical Sciences in Cambridge in the spring of 2000、ETH Zurich、University of Washington、Center for Dynamical Systems at the Pennsylvania State University、Stanford University on more than one occasion —— MD 第 129 行**逐项与印刷吻合，无漏项、无增项**。
- Part I 与起始段核对：印刷居中加粗「**Part I. Measure rigidity**」，MD 第 131 行 `## Part I. Measure rigidity` 标题层级正确；`Throughout this paper, let G = SL(k,ℝ) for some k ≥ 3, let Γ be a discrete subgroup of G, and let X = G/Γ. As in the previous section, we let A < G denote the group of k×k positive diagonal matrices. We shall implicitly`（页末断句，页图第 20–23 行、文本层第 41–44 行）与 MD 第 133 行**逐项吻合**，页末断点与 MD 行位置对应正确。

## p.008（PDF p.8 / 印刷 p.520）
- PNG：/tmp/linden07_audit_p008.png（pngmono 150dpi）
- 核对：跨页续句「identify」与 Σ 定义式、`(t_1,…,t_k)↦diag(t_1,…,t_k)`、α^t = diag(e^{t_1},…,e^{t_k}) ∈ A、ℝ^{k−1} flow α、unipotent/normalized/normalizer/centralizer 定义段、`a(Ux)=Uax` 与 expands U 定义段、M_∞(Y) 与 weak* 拓扑、ρ↦∫_Y f(y)dρ(y)、比例记号展示式 `ν_1 ∝ ν_2 if ν_1 = Cν_2 for some C > 0,`、球 B_ε^Y/B_ε^H 约定、d(·,·) 度量约定、§2 双行标题、§2.1 起始段、运行头
- 结果：PASS±（差异均为排版级，不误导；本页 MD 未修改）
- 差异列表：
  1. MD 缺运行头「520 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  2. 行内紧排伪影（第 143 行）：MD 作「said to be normalized`$b y \ g \in G$`if」，印刷为「said to be **normalized by** $g \in G$ if」（页图第 7 行、文本层第 11–12 行）——介词 `by` 的两个字母被拆成 `b y` 并落入数学定界符内；字母顺序未变、语义可还原，属 MinerU 紧排族伪影，全篇同类众多（`$\mathrm{SL}(k,\mathbb{R})$which`、`$m ,$n` 等），登记不改。
  3. 记号命令不统一：第 143 行两处单位矩阵混用 `\operatorname { I } _ { k }` 与 `\mathrm { I } _ { k }`；渲染字形相同，排版级，不改。
  4. 行内紧排缺空格：第 141 行「the map$( t _ { 1 } , … )$」「$\in A$and also」「element on X」「flow α on$X$」；第 145 行「$a ( U x ) =$ $U a x$」；第 147 行「metric space Y let$M _ { \infty } ( Y )$denote」「measures on$Y$with」「$\rho \mapsto \int _ { Y } f ( y ) d \rho ( y )$ is continuous」「measures$\nu _ { 1 }$and」；第 155、157 行同类紧排。排版级，不改。
  5. 斜体强调丢失：印刷 `unipotent`、`normalized by`、`normalizer`、`centralizes`、`centralizer`、`foliation`、`expands`、`diag`（页图第 4–12 行）为斜体强调，MD 第 143、145、141 行均作正体。语义不变，不改。
- 展示式逐要素核对（150dpi 页图 + 文本层双证）：
  - 印刷 `Σ = {t ∈ ℝ^k : t_1 + ⋯ + t_k = 0}`（页图第 2 行、文本层第 5 行）——MD 第 138 行 `\Sigma = \left\{\mathbf{t} \in \mathbb{R}^k: t_1 + \dots + t_k = 0 \right\}`，**k 次幂、加号链与右端 0 全部吻合**。
  - 印刷 `ν_1 ∝ ν_2 if ν_1 = Cν_2 for some C > 0,`（页图第 13 行、文本层第 26 行，**式末带逗号**）——MD 第 150 行 `\nu_ {1} \propto \nu_ {2} \text { if } \nu_ {1} = C \nu_ {2} \text { for some } C > 0,`——比例号、比例常数 `C`、条件 `C > 0` 与末逗号**全部吻合**。
- 定义段逐项核对：`g − I_k is nilpotent; i.e., for some n, (g − I_k)^n = 0`；`gHg^{−1} = H`；`H is normalized by L < G if it is normalized by every g ∈ L`；`the normalizer N(H) of H is the group of all g ∈ G normalizing it`；`g centralizes H if gh = hg for every h ∈ H, and we set C(H), the centralizer of H in G, to be …`（MD 第 143 行）——**逐句吻合**。
- foliation 段逐项核对：`a(Ux) = Uax`、`the foliation of X into U orbits is invariant under the action of A`、`a ∈ A expands U if all eigenvalues of Ad(a) restricted to the Lie algebra of U are greater than one`（MD 第 145 行）——**逐句吻合**，`Ad(a)` 的算子名未被误识。
- M_∞(Y) 段逐项核对：`all locally finite Borel measures on Y with the coarsest topology for which ρ ↦ ∫_Y f(y)dρ(y) is continuous for every compactly supported continuous f. For two Radon measures ν_1 and ν_2 on Y we write`（MD 第 147 行）——与印刷**逐句吻合**，且印刷此处为**单句点**（页图第 11 行、文本层第 23 行），MD 第 147 行 `continuous$f.$ For two Radon` 亦为单句点，**重复句点缺陷已不存在，本段确认现值正确**。
- 球与距离约定逐项核对：`B^Y_ε(y) (or B_ε(y) if Y is understood)`、`B^H_ε = B^H_ε(I) where I is identity in H`、`B^H_ε(x) = B^H_ε · x`（第 155 行）；`right-invariant Riemannian metric on G`、`induces a right-invariant metric on every closed subgroup H ⊂ G, and furthermore a metric on X = G/Γ`、`These induced metrics we denote by the same letter`（第 157 行）——**逐句吻合**。
- §2 与 §2.1 核对：印刷双行居中标题「2. Conditional measures on **A**-invariant foliations, / invariant measures, and shearing」，MD 第 159 行 `## 2. Conditional measures on A-invariant foliations, invariant measures, and shearing`（合并为单行，**文字与顺序一致**）；§2.1 段 `[17] (and in a sense is already used implicitly in [45])`、`A discussion can be found in [17, §4]`、`presented in [20, §3]`、`summarizing its main properties`（第 161 行）——**逐句吻合**，引文节号未错。

### 本段溯源（git show 基线导出）

对本段判定为缺陷并已修复的两处，在 worktree 内执行
`git show <rev>:"2010年 - Lindenstrauss/Lindenstrauss_2007_littlewood_published_mineru/Lindenstrauss_2007_littlewood_published__Lindenstrauss_2007_littlewood_published.md"` 逐处回查：

| 缺陷位置 | `d351abbff`（原始 MinerU 导出入库提交） | `847882f32`（integrate harvest Peer-P16） | `078d4ecb`（`cpf-redo/…^`，redo p.007 提交） | 结论 |
|---|---|---|---|---|
| p.003 / MD 第 31 行 Conjecture 1.2 行末逗号 | 缺（`…\mathbb { R }$`） | 缺 | 缺 | **非导出缺陷回归，系 MinerU 原始导出即缺失的标点**；原导出在此处不正确 |
| p.004 / MD 第 75 行 Theorem 1.6 行末逗号 | 缺（`…\setminus \Xi _ { k }$`） | 缺 | 缺 | **非导出缺陷回归，系 MinerU 原始导出即缺失的标点**；原导出在此处不正确 |

- 三次回查均未出现该两行曾在后续提交中被改坏再改回的痕迹，故不能记为某个 peer 引入的回归；正确表述是「原导出就不正确，本段首次纠正」。
- 本段未发现任何属于「后被 peer 改坏的回归」型缺陷。p.001（`Hausdorff`）、p.004（`dim _ { H } \Xi = 0`、`[K : \mathbb{Q}] = 3).`、p.005（`tranversals`）、p.008（`continuous$f.$` 单句点）等本段复核为「现值已正确」的条目，其旧缺陷同样源于原始导出（Peer-P16 与前序 redo 块已修复），本段只作确认，未重复改动。

### 本段交付自检与边界

- `grep -c '^## p.' AUDIT-Lindenstrauss_2007_littlewood_published.md` 应为 **8**，对应本段新增 p.001–p.008 各一条，无合并、无跳页（实测见下）。
- 本段分级汇总：**PASS± 8 页**（p.001–p.008），**PASS 0 页**，**FAIL 0 页**；其中 p.003、p.004 各修复 1 处标点脱离，合计 `edits=2`。
- 本段未执行任何 git 写操作（无 add/commit/merge/push）；未写根 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、`MEMORY.md`、`README.md`；未创建 `audit-redo/` 新图、未碰 `audit/`；未启动或改动 mineru。PDF 只读，SHA-256 与开工前一致（`7f26dde3…825`）。
- 工作区中 `AUDIT-…published.redo.md` 与 MD 第 169–175 行一带存在**前序 redo 块（Wf-R-P16，p.009）遗留的未提交改动**，本段已原样保留、未纳入本段判定范围。

---

# 追加段：redo 块 B（PDF p.9–p.16，actor=`linden07`）

- 性质：本段同样是对 Peer-P16 记录的独立重做复核，**不继承**其判定；每页重新渲染 PNG 目检 + `pdftotext` 文本层互证，唯一裁决源是印刷原页。
- 身份：actor=`linden07`；host=zcode Desktop；model=`opencode-go-chat/space-bunny-free`（本会话运行时自报）；effort=run 级配置未暴露，记 `UNKNOWN`。cwd=`/Users/aurolafly/.zcode/worktrees/cpf-redo-Lindenstrauss_2007_littlewood_published`；branch=`cpf-redo/Lindenstrauss_2007_littlewood_published`。
- PDF 只读证据：`2010年 - Lindenstrauss/Lindenstrauss_2007_littlewood_published.pdf`，48 页，SHA-256=`7f26dde3f9b206534584b2b94d4a86e6319e467918efca8b4d00b1b1ae574825`（沿用块 A 开工前实测值，本段未再改动 PDF）。
- 写入范围同块 A：只写本 AUDIT 文件与本篇 MinerU Markdown；未写根级真值文件、未写 `audit-redo/`、未执行 git 写操作、未碰 mineru。
- PNG 去向：同块 A，`/tmp/linden07_audit_pNNN.png` 为瞬时中转，持久化归档责任留给 canonical integrator。

## p.009（PDF p.9 / 印刷 p.521）
- PNG：/tmp/linden07_audit_p009.png（pngmono 150dpi）
- 核对：conditional measures 系统引入句、性质 (1)–(7) 全部陈述、normalization 段（`B_1^U = 1`）、atomic/trivial 段（Poincaré recurrence、A-ergodic 二择一、[26, §9] 与 [17]）、positive entropy 收尾段、脚注 2 全文、运行头
- 结果：PASS±（差异均为字形/排版级，不误导；本页 MD 本段未修改）
- 差异列表：
  1. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 521」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  2. 重音分解：印刷「Poincaré recurrence」（页图第 16 行，é 为合成字形）MD 第 179 行作 `Poincar´e`（U+00B4 + e）。字形级，语义与可检索性不受实质影响，登记不改。
  3. 字形混排：MD 第 177 行 (6) 条首符号用字面「µ」（U+00B5）而非 `$\mu$`；第 181 行 (7) 条熵记号作 `$\mathsf { h } _ { \mu }$`（无衬线），印刷为斜体加粗 `h_μ(α^t)`（页图第 19 行）。字形级，数学对象与下标正确，不误导，登记不改。
  4. 行内紧排缺空格：第 163 行「subgroup$U \ < \ G$normalized」「system$\{ \mu _ { x , U } \} _ { x \in X }$of Radon」「set$X ^ { \prime } \subset X$with the following properties<sup>2</sup>」；第 165–181 行同类紧排密集。排版级，不改。
- 性质 (1)–(7) 逐条核对（150dpi 页图 + 文本层双证，全部吻合）：
  - (1) `The map x ↦ μ_{x,U} is measurable.`（MD 第 165 行）
  - (2) `For every ε > 0 and x ∈ X′, μ_{x,U}(B^U_ε) > 0.`（第 167 行，**未出现 MD 上常见的尾随句点伪影**，与印刷单句点一致）
  - (3) `For every x ∈ X′ and u ∈ U with ux ∈ X′, we have that μ_{x,U} ∝ (μ_{ux,U})u, where (μ_{ux,U})u denotes the push forward of the measure μ_{ux,U} under the map v ↦ vu.`（第 169 行）——`u` 后的**逗号**与 `vu` 后的**句点**均在位，与印刷一致。
  - (4) `For every t ∈ Σ, and x, α^t x ∈ X′, μ_{α^t x,U} ∝ α^t(μ_{x,U})α^{−t}.`（第 171 行）——集合 `Σ`、`α^{−t}` 的负指数与行末句点均在位。
  - (5) `If U ⊂ C(α^t) = {g ∈ G : gα^t = α^t g} commutes with α^t, then μ_{α^t x,U} = μ_{x,U} whenever x, α^t x ∈ X′.`（第 175 行）——中心化子定义式与 `⊂` 方向正确，句点在位。
  - (6) `µ is U-invariant if, and only if, μ_{x,U} is a Haar measure on U a.e. (see e.g. [17] or the slightly more general [20, Prop. 4.3]).`（第 177 行）——引文 `Prop. 4.3` 未错。
  - (7) `If for every x ∈ X the orbit Ux is the stable manifold through x with respect to α^t, then the measure theoretic entropy h_μ(α^t) is positive if and only if the conditional measures μ_{x,U} are nonatomic a.e.`（第 181 行）——条件与「当且仅当」方向正确。
- normalization 段核对（MD 第 173 行）：印刷「In general, there is no canonical way to normalize the measures μ_{x,U}; we fix a specific normalization by requiring that μ_{x,U}(B^U_1) = 1 for every x ∈ X′. This implies the next crucial property.」——**逐句吻合**，`B_1^U` 的下标 1 与上标 U 位置正确。
- atomic/trivial 段核对（MD 第 179 行）：`The other extreme to U-invariance occurs when μ_{x,U} is atomic`、`supported on the identity I_k ∈ U, in which case we say that μ_{x,U} is trivial`、`an element a ∈ A that uniformly expands the U-orbits (i.e. for which the U-orbits are contained in the unstable manifolds)`、`either μ_{x,U} is trivial a.s. or μ_{x,U} is nonatomic a.s.`、`(see [26, § 9] and [17])` —— **逐句吻合**，节号 `§ 9` 未错。
- 收尾段核对（MD 第 183 行）：`So positive entropy implies that the conditional measures are nontrivial a.e., and the goal is to show that this implies that they are Haar measures. Quite often one shows first that the conditional measures are translation invariant under some element up to proportionality, which makes the following observation useful.` —— **逐句吻合**。
- 脚注 2 核对（MD 第 185 行）：印刷（页图末段、文本层第 39–43 行）「We are following the conventions of [20] in viewing the conditional measures μ_{x,U} as measures on U. An alternative approach, which, for example, is the one taken in [17] and [13], is to view the conditional measures as a collection of measures on X supported on single orbits of U; in this approach, however, the conditional measure is not a Radon measure on X, only on the single orbit of U in the topology of this submanifold.」——**逐句吻合**，标记 `²` 与 `<sup>2</sup>` 对位正确。
- 页边界核对：MD 第 187 行的性质 (8) 属印刷 p.522 内容（印刷 p.521 止于 `observation useful.` + 脚注 2），已按页型边界留待 p.010 记录核对，本页无跨页错接。
- 前序块修复复核：本页现值中 (3) 的逗号+句点、(4) 与 (5) 的行末句点均在位，与印刷一致，**确认前序 redo 块的这几处修复正确，本段不重复改动**。

## p.010（PDF p.10 / 印刷 p.522）
- PNG：/tmp/linden07_audit_p010.png（pngmono 150dpi）
- 核对：性质 (8) 陈述、`This was first shown in [17]` 段、Proof of (8) 全证明、定义式 `D_M = {x ∈ X′ : μ_{x,U}(B^U_2) < M}`、等式 `μ_{α^{nt}x,U} = c^k μ_{α^{nt}x,U}(α^{nt}u^k α^{−nt})`、三行不等式链 `M ≥ … ≥ … = … = c^k`、两个 `lim sup` 段、`u_{ij}(s)=exp(sE_{ij})=I_k+sE_{ij}` 与 `U_{ij}` 定义式、`E_{ij}` 说明、共轭式 `α^t u_{ij}(s)α^{−t} = u_{ij}(e^{t_i−t_j}s)`、运行头
- 结果：PASS±（3 处标点脱离已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 191 行）：印刷「…is part of the stable manifold with respect to α^t**).** Define for M > 0」（页图第 5 行、文本层第 12–13 行）在右括号后有句点；MD 原件作 `…with respect to$\alpha ^ { \mathbf { t } } )$ Define for$M > 0$` 缺该句点。已用 Edit 补为 `$\alpha ^ { \mathbf { t } } ).$ Define`。
  2. **已修复**（MD 第 211 行）：印刷「Since k is arbitrary this implies c ≤ 1**.**」（页图第 15 行、文本层第 33 行）行末有句点；MD 原件 `Since k is arbitrary this implies$c \leq 1$` 缺失。已补 `.$`。
  3. **已修复**（MD 第 213 行）：印刷「…shows that c ≥ 1, hence μ_{x,U} = μ_{x,U}u**.**」（页图第 16–17 行、文本层第 35 行）行末有句点；MD 原件缺失。已补 `u.$`。
  4. MD 缺运行头「522 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  5. 重音分解：MD 第 189 行 `Poincar´e recurrence`（U+00B4+e），印刷为合成 `é`。字形级，不改。
  6. 表述微调：MD 第 197 行相对印刷作两处改写——印刷「(i.e. any x ∈ X′ **so that** α^{nt} is in D_M…)」MD 作「(i.e., any x ∈ X′ **such that** α^{nt} is in D_M…)」；印刷在 `…infinitely many n)` 与 `if μ_{x,U} = cμ_{x,U}u` 之间无逗号，MD 补了逗号。语义与指称不变，不误导，登记不改（该行已由前序 Peer 改写为规范 LaTeX `$\bigcup_{M>0}\limsup_{n\to\infty}\alpha^{-n\mathbf t}D_M$`，与印刷的 ⋃_{M>0} lim sup_{n→∞} α^{−nt}D_M 含义一致，属改进而非失真）。
  7. 运算符字距拍平：MD 第 199 行 `\lim\mathrm { s u p }`、第 215 行 `\operatorname* { l i m } \operatorname* { s u p }`。数学对象正确，排版级，不改。
  8. 行内紧排缺空格：第 187、189、191、205、211、213、215、217、223、229 行密集出现（如「the U-orbit Ux is part」「Since k is arbitrary this implies」「implies that these groups are normalized by$A ;$indeed」「parametrized by pairs$( i , j )$of distinct integers」）。排版级，不改。
- 证明链逐要素核对（150dpi 页图 + 文本层双证，全部吻合）：
  - `D_M = {x ∈ X′ : μ_{x,U}(B^U_2) < M}.`（页图第 6 行、文本层第 15 行）——MD 第 194 行 `\left\{x \in X^{\prime}: \mu_{x,U}\big(B _ {2}^U\big) < M \right\}.`，**下标 2、上标 U、严格小于号与右端 M 全部吻合**。
  - `μ_{α^{nt}x,U} = c^k μ_{α^{nt}x,U}(α^{nt}u^k α^{−nt}).`（页图第 11 行、文本层第 23 行）——MD 第 202 行 **c 的 k 次幂、u 的 k 次幂、α 的 −nt 次幂与点乘括号位置全部吻合**。
  - 不等式链（页图第 15–17 行、文本层第 29–31 行）：`M ≥ μ_{α^{nt}x,U}(B^U_2) ≥ μ_{α^{nt}x,U}(B^U_1 α^{nt}u^k α^{−nt}) = (μ_{α^{nt}x,U} α^{nt}u^{−k} α^{−nt})(B^U_1) = c^k μ_{α^{nt}x,U}(B^U_1) = c^k.`——MD 第 208 行**三个不等号方向、中间行的 u 的 −k 次幂与最右端 `= c^k` 全部吻合**，未出现把等号误作不等号或丢行的情形。
  - `u_{ij}(s) = exp(sE_{ij}) = I_k + sE_{ij},   U_{ij} = {u_{ij}(s) : s ∈ ℝ},`（页图第 22 行、文本层第 44 行，**式末带逗号**）——MD 第 220 行 `u _ {i j} (s) = \exp (s E _ {i j}) = \mathrm {I} _ {k} + s E _ {i j}, \qquad U _ {i j} = \{u _ {i j} (s): s \in \mathbb {R} \},`——**指数 sE_{ij}、单位矩阵 I_k、逗号与第二项 U_{ij} 定义全部吻合**。
  - `α^t u_{ij}(s) α^{−t} = u_{ij}(e^{t_i − t_j} s).`（页图末行、文本层第 50 行）——MD 第 226 行 `\alpha^ {\mathbf {t}} u _ {i j} (s) \alpha^ {- \mathbf {t}} = u _ {i j} (e ^ {t _ {i} - t _ {j}} s).`——**指数 `t_i − t_j` 的减号方向与 t 的负次幂正确**，这是本页最易误读的系数/指数处，逐字符核对无误。
- 其余逐项核对：(8) 条「Possibly after replacing X′ of (1)–(4) by a conull subset…in fact, μ_{x,U} = μ_{x,U}u holds.」（MD 第 187 行）、`The proof of this fact only uses Poincaré recurrence and (4) above`（第 189 行）、`Choose k > 1 arbitrary…which is possible since α^t uniformly contracts U`（第 205 行）、`If μ_{x,U} = cμ_{x,U}u then μ_{x,U} = c^{−1}μ_{x,U}u^{−1}`（第 213 行，`c^{−1}` 与 `u^{−1}` 两个负指数均在位）、`Thus we see that if we replace X′ by X′ ∩ ⋃_M lim sup_{n→∞} α^{−nt}D_M — a conull subset of X′, then (8) holds for any x ∈ X′.`+QED 方块（第 215 行）、`pairs (i, j) of distinct integers in the range {1,…,k}`（第 217 行）、`the matrix with 1 at the i^{th} row and j^{th} column`（第 223 行）——**逐项与印刷吻合**。
- 页边界核对：MD 第 229、231 行属印刷 p.523 内容（印刷 p.522 止于共轭式），本页无跨页错接，留待 p.011 记录核对。

## p.011（PDF p.11 / 印刷 p.523）
- PNG：/tmp/linden07_audit_p011.png（pngmono 150dpi）
- 核对：`μ_x^{ij}` 简写约定段、`t_i = t_j` 段、性质 (9) 陈述、Proof of (9) 全证明（Luzin、`[5, p. 69]`、`M_∞(U_{ij})`、`x_ℓ = α^{n_ℓ t}`、`n_ℓ → ∞`、`α^{n_ℓ t}uα^{−n_ℓ t}`、(4) 收尾）、maximal ergodic theorem 段（[20, Thm. A.1]、D. Rudolph、Hurewicz [11]）、性质 (10) 及最大不等式公式、§2.2 标题、Theorem 2.1 起始句、运行头
- 结果：PASS±（4 处标点脱离已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 233 行）：印刷 (9) 条末「…and if α is ergodic then μ is invariant under U_{ij}**.**」（页图第 10 行、文本层第 17 行）有句点；MD 原件缺失。已补 `.$`。
  2. **已修复**（MD 第 235 行）：印刷 Proof of (9) 首句末「…we can assume μ_x^{ij} = μ_x^{ij}u for x ∈ B**.** Let K ⊂ B be a compact set…」（页图第 13–14 行、文本层第 19–20 行）在 `B` 后有句点；MD 原件作 `for$x \in B$ Let$K \subset B$` 两句粘连。已补 `.`。
  3. **已修复**（MD 第 239 行）：印刷「(10) For any f ∈ L¹(X,μ) and α > 0**,**」（页图第 19 行、文本层第 38 行）行末有逗号；MD 原件缺失。已补 `,`。
  4. **已修复**（MD 第 245 行）：印刷「for some universal constant C > 0**.**」（页图第 22 行、文本层第 46 行）行末有句点；MD 原件缺失。已补 `.`。
  5. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 523」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  6. 重音分解：MD 第 235 行两处 `Poincar´e`（U+00B4+e）。字形级，不改。
  7. 行内紧排缺空格：第 229、231、233、235、237、239 行密集（如「normalized by A, the orbits of$U _ { i j }$form」「$\mu _ { x } ^ { i j }$as a shorthand for$\mu _ { x , U _ { i j } } ;$any integer」「by (8) we can assume」「$\mathbf { t } \in \Sigma$be such that」「For any$f \in L ^ { 1 } ( X , \mu )$and」）。排版级，不改。
- 性质 (10) 最大不等式逐要素核对（150dpi 页图第 20–21 行 + 文本层第 39–46 行双证）：
  - 印刷 `μ( { x : ∫_{B_r^{U_ij}} f(ux) dμ_x^{ij} > α μ_x^{ij}(B_r^{U_ij}) for some r > 0 } ) < C‖f‖₁ / α`
  - MD 第 242 行 `\mu \left(\left\{x: \int_ {B _ {r} ^ {U _ {i j}}} f (u x) \mathrm{d} \mu_ {x} ^ {i j} > \alpha \mu_ {x} ^ {i j} \left(B _ {r} ^ {U _ {i j}}\right) \text {for some} r > 0 \right\}\right) < \frac {C \| f \| _ {1}}{\alpha}`——**积分域下标 r 与上标 U_ij、被积函数 f(ux)、测度 dμ_x^{ij}、比较项系数 α、右端常数 C、范数下标 ‖f‖₁ 与分母 α 全部吻合**，无系数/指数错位。
- 性质 (9) 陈述核对（MD 第 233 行）：`a set of positive measure B ⊂ X`、`for any x ∈ B there exists a nonzero u ∈ U_{ij} with μ_x^{ij} ∝ μ_x^{ij}u`、`Then for a.e. x ∈ B in fact μ_x^{ij} is a Haar measure of U_{ij}, and if α is ergodic then μ is invariant under U_{ij}` ——**条件与结论逐项吻合**。
- Proof of (9) 逐要素核对（MD 第 235 行）：`by (8) we can assume μ_x^{ij} = μ_x^{ij}u for x ∈ B`（**由 (8) 把比例等式升级为等式，未被误删**）；`Let K ⊂ B be a compact set of measure almost equal to μ(B) such that μ_x^{ij} is continuous for x ∈ K`；`by Luzin's theorem`；`the space of Radon measures M_∞(U_{ij}) equipped with the weak* topology so that a more general version [5, p. 69] of Luzin's theorem is needed`（**页码 p. 69 与文献号 [5] 未错**）；`Let t ∈ Σ be such that U_{ij} is uniformly contracted by α^t`；`a sequence x_ℓ = α^{n_ℓ t} ∈ K that approaches x with n_ℓ → ∞`（**两个下标 ℓ 未混淆**）；`Invariance of μ_x^{ij} under u implies invariance of μ_{x_ℓ} under the much smaller element α^{n_ℓ t}uα^{−n_ℓ t} and all its powers`（**负指数 −n_ℓ t 方向正确**）；`since μ_{x_ℓ}^{ij} converges to μ_x^{ij} we conclude that μ_x^{ij} is a Haar measure of U_{ij}`；`The final statement follows from (4) which implies that the set of x where μ_x^{ij} is a Haar measure is α-invariant` + QED 方块——**逐项吻合**。
- 其余核对：`maximal ergodic theorem [20, Thm. A.1] proved by the last named author in joint work with D. Rudolph, which is related to a maximal ergodic theorem of Hurewicz [11]`（MD 第 237 行，引文号全对）；§2.2 标题 `2.2. Invariant measures, high and low entropy cases. We are now in a position to state the general measure rigidity result for quotients of G:`（第 247 行）；Theorem 2.1 首句 `Let X = G/Γ and A be as above. Let μ be an A-invariant and ergodic probability measure on X. For any pair of indices a, b, one of the following three properties must hold.`（第 249 行）——**逐句吻合**，未见条件删减。
- 页边界核对：MD 第 251 行起为 Theorem 2.1 的三个分列 (1)(2)(3)，属印刷 p.524 内容（印刷 p.523 止于 `three properties must hold.`），本页无跨页错接，留待 p.012 记录核对。

## p.012（PDF p.12 / 印刷 p.524）
- PNG：/tmp/linden07_audit_p012.png（pngmono 150dpi）
- 核对：Theorem 2.1 三个分列 (1)(2)(3)（含 `H_{ab} = ⟨U_{ab},U_{ba}⟩`、`A′_{ab} = {α^s : s ∈ Σ and s_a = s_b}`、`C(H_{ab}) = {g ∈ G : gh = hg for all h ∈ H_{ab}}`）、Remark、`(3′)` 陈述（含 `x_0`、`α^s x_0 = x_0`、`C(A′_{ab})`）、Indeed 段、`[44]`/`[3, §9]`/`SL(3,ℝ)` 引证、`exceptional returns` 段（`[25], [21]`、`[48]`）、熵刻画段（`t_i > t_j`、Proposition 3.1、`[17]`）、`Theorem 2.1.(2)/(3)` 归约段、High entropy case 段、运行头
- 结果：PASS±（3 处标点脱离已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 253 行）：印刷 (2) 末「…elements of H_{ab} = ⟨U_{ab}, U_{ba}⟩**.**」（页图第 5 行、文本层第 9 行）有句点；MD 原件缺失。已补 `rangle.$`。注：该行字节含 `\rangle`，Edit 工具的 `old_string` 中 `\r` 会被当作回车转义而无法定位，故改用唯一锚点 `rangle$`（`grep -c 'rangle\$'` 实测 = 1，全篇唯一）完成定位与替换，未改用脚本绕过。
  2. **已修复**（MD 第 255 行）：印刷 (3) 末「…is the centralizer of H_{ab}**.**」（页图第 8 行、文本层第 13 行）有句点；MD 原件缺失。已补 `.$`。
  3. **已修复**（MD 第 259 行）：印刷 `(3′)` 末「In particular, a.e. point x satisfies α^s x = x**.**」（页图第 13 行、文本层第 19 行）有句点；MD 原件缺失。已补 `.$`。
  4. MD 缺运行头「524 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  5. 字形/字距伪影：MD 第 255 行 `C ( H _ { a b } ) – o r b i t`（单词 `orbit` 被拆成 `– o r b i t`，前缀多出 en-dash）；第 269 行 `i = a { \mathrm { ~ o r ~ } } j = b`（`or` 被字距化）。字母顺序与语义均可还原，排版级，不改。
  6. 重音分解：MD 第 261 行 `Poincar´e`。字形级，不改。
  7. 行内紧排缺空格：第 251、253、255、257、259、261、263、265、267、269 行密集（如「The conditional measures$\mu _ { x } ^ { a b }$and」「If$k = 3$then (3) is equivalent」「which we term exceptional returns, does not happen」「$\mathbf { t } \in \Sigma$if and only if for some」）。排版级，不改。
- 三个分列逐要素核对（150dpi 页图 + 文本层双证，全部吻合）：
  - (1) `The conditional measures μ_x^{ab} and μ_x^{ba} are trivial a.e.`（页图第 3 行、文本层第 4–5 行）——MD 第 251 行一致，**上下标 `ab`/`ba` 顺序未颠倒**。
  - (2) `The conditional measures μ_x^{ab} and μ_x^{ba} are Haar a.e., and μ is invariant under left multiplication with elements of H_{ab} = ⟨U_{ab}, U_{ba}⟩.`（页图第 5–6 行）——MD 第 253 行 `\langle U _ { a b } , U _ { b a } rangle` 与印刷的**生成元顺序 `U_{ab}, U_{ba}` 完全一致**（此处顺序颠倒会改变数学内容，已重点核对）。
  - (3) `Let A′_{ab} = {α^s : s ∈ Σ and s_a = s_b}. Then a.e. ergodic component of μ with respect to A′_{ab} is supported on a single C(H_{ab})-orbit, where C(H_{ab}) = {g ∈ G : gh = hg for all h ∈ H_{ab}} is the centralizer of H_{ab}.`（页图第 7–8 行、文本层第 11–13 行）——MD 第 255 行**条件 `s_a = s_b`、中心化子交换关系 `gh = hg` 与中心化子定义完整无缺**。
- `(3′)` 逐要素核对（MD 第 259 行）：印刷 `There exist a nontrivial s ∈ Σ with s_a = s_b and a point x_0 ∈ X with α^s x_0 = x_0 such that the measure μ is supported by the orbit of x_0 under C(A′_{ab}). In particular, a.e. point x satisfies α^s x = x.`——**`nontrivial`、`x_0` 下标、`α^s x_0 = x_0` 与最终 `α^s x = x` 两式均未被混淆或删减**。
- 其余逐项核对：`C(H_{ab}) contains only diagonal matrices`、`Poincaré recurrence for A′_{ab} together with (3) imply that a.e. point is periodic`、`ergodicity of μ under A implies that the period s must be the same a.e.`、`ergodicity shows (3′)`、`The examples of M. Rees [44], [3, §9] … in certain quotients of SL(3, ℝ) (which certainly can have positive entropy)`、`case (3) and (3′) above are not superfluous`（MD 第 261 行）；`When Γ = SL(k, ℤ), however, this phenomenon, which we term exceptional returns, does not happen. We will show this in Section 5; similar observations have been made earlier in [25], [21]. We also refer the reader to [48] for … inner lattices in SL(k, ℝ)`（第 263 行）；`μ has positive entropy with respect to α^t if and only if for some i, j with t_i > t_j the measures μ_x^{ij} are not a.s. trivial (see Proposition 3.1 below …; this fact was first proved in [17])`、`Thus (1) in Theorem 2.1 above holds for all pairs of indices i, j if, and only if, the entropy of μ with respect to every one-parameter subgroup of A is zero`（第 265 行）；`it is enough to show that for every a, b for which the μ_x^{ab} is a.s. nontrivial either Theorem 2.1.(2) or Theorem 2.1.(3) holds`（第 267 行）；`High entropy case. There is an additional pair of indices i, j distinct from a, b such that i = a or j = b for which μ_x^{ij} are nontrivial a.s. In this case we prove:`（第 269 行）——**逐句与印刷吻合**，引文号 `[25], [21], [48], [44], [3, §9], [17]` 全对，`t_i > t_j` 的不等号方向正确。
- 页边界核对：MD 第 271 行起的 Theorem 2.2 属印刷 p.525 内容（印刷 p.524 止于 `In this case we prove:`），本页无跨页错接，留待 p.013 记录核对。

## p.013（PDF p.13 / 印刷 p.525）
- PNG：/tmp/linden07_audit_p013.png（pngmono 150dpi）
- 核对：Theorem 2.2 陈述、high entropy case 证明段（`[3]`、Proposition 3.1、`[26]`、Ratner's original arguments）、Low entropy case 段、Theorem 2.3 陈述与两个分列 (1)(2)、Corollary 3.4 段（含 `C(H_{ab}) = C(H_{ba})`）、`[20]` 技术段（`SL(2,ℝ) × L`、`[38], [39]`、`[29, §6]`、(9) in Section 2.1）、§3 标题、Ledrappier–Young `[19]` 段开头、运行头
- 结果：PASS±（1 处标点脱离已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 271 行）：印刷 Theorem 2.2 末「…and μ is invariant under H_{ab}**.**」（页图第 4 行、文本层第 6 行）有句点；MD 原件缺失。已补 `.$`。
  2. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 525」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  3. 字距伪影：MD 第 271、277 行把「or」写成数学模式内的 `o r` / `o r`（如 `i = a o r j = b`）。字母顺序未变，排版级，不改。
  4. 印刷断词残留：印刷第 32–33 行把 `non-` / `trivial` 跨行断开，MD 第 283 行作 `non-trivial` 保留连字符（正确合词应为 `nontrivial`）。语义唯一明确，排版级，不改。
  5. MD 较印刷多一枚逗号：印刷「presented in Section 3 makes use of the noncommutative structure」（页图第 6 行、文本层第 8–9 行）`Section 3` 后无逗号，MD 第 273 行作 `presented in Section 3, makes use of`。属 MD 侧添加，不构成印刷错字，排版级，不改。
  6. 行内紧排缺空格：第 271、273、275、277、279、281、283、285、289 行密集（如「If both$\mu _ { x } ^ { a b }$and」「For every pair of indices$i , j$distinct」「the$U _ { a b }$flow even though$\mu$is not assumed」「ratner's H-property」）。排版级，不改。
- 定理陈述逐要素核对（150dpi 页图 + 文本层双证）：
  - Theorem 2.2（MD 第 271 行）：`If both μ_x^{ab} and μ_x^{ij} are nontrivial a.s., for distinct pairs of indices i, j and a, b with either i = a or j = b, then both μ_x^{ab} and μ_x^{ba} are in fact Haar measures a.s. and μ is invariant under H_{ab}.` —— **两个假设（both…nontrivial a.s.；i=a or j=b）与两个结论（Haar measures a.s.；μ is invariant under H_{ab}）逐项吻合**，`ab`/`ba`/`ij` 三个下标顺序与印刷完全一致。
  - Theorem 2.3（MD 第 277 行）：`Assume μ_x^{ab} are a.e. nontrivial, and μ_x^{ij} are trivial a.e. for every pair i, j distinct from a, b such that i = a or j = b. Then one of the following properties holds.` —— **吻合**。
  - 分列 (1) `μ is U_{ab} invariant.`、(2) `Almost every A′_{ab}-ergodic component of μ is supported on a single C(H_{ab}) orbit.`（MD 第 279、281 行）—— **吻合**。
- Corollary 3.4 段核对（MD 第 283 行）：印刷「We will see in Corollary 3.4 that in the low entropy case μ_x^{ba} is also nontrivial; so applying Theorem 2.3 for U_{ba} instead of U_{ab} one sees that either μ is H_{ab}-invariant or almost every A′_{ab}-ergodic component of μ is supported on a single C(H_{ab}) = C(H_{ba}) orbit.」—— **等式 `C(H_{ab}) = C(H_{ba})` 的左右次序与 `U_{ba}`/`U_{ab}` 的替换方向均与印刷一致**（此处若左右颠倒会改变论证，已重点核对）。
- `[20]` 技术段核对（MD 第 285 行）：`irreducible quotients of products of the type SL(2,ℝ) × L for some algebraic group L`、`using methods quite similar to Ratner's [38], [39]`、`for the U_{ab} flow even though μ is not assumed to be invariant or even quasi invariant under U_{ab}`、`a variant of Ratner's H-property (related, but distinct from the one used by Witte in [29, §6]) together with the maximal ergodic theorem for U_{ab} as in (9) in Section 2.1.` —— **引文号 `[38], [39], [29, §6]` 全对，节号 `§6` 未错，逐句吻合**。
- §3 与开头段核对（MD 第 287、289 行）：印刷居中标题「**3. More about entropy and the high entropy case**」，MD 第 287 行 `## 3. More about entropy and the high entropy case` 层级正确；`A well-known theorem by Ledrappier and Young [19] relates the entropy, the dimension of conditional measures along invariant foliations, and Lyapunov exponents, for a general C² map on a compact manifold, and in [26, §9] an adaptation of the general results to flows on locally homogeneous spaces is…` —— **引文 `[19]`、`[26, §9]` 与 `C^2` 的指数 2 均正确**。
- 页边界核对：印刷 p.525 止于 `…to flows on locally homogeneous spaces is`（页图末行）；MD 第 289 行的 `provided.` 起为 p.526 内容的跨页合并，属正常续接；MD 第 291 行末的 `\ [ 1 9 ]` 与第 293 行的 Proposition 3.1 亦属 p.526，其印刷形态留待 p.014 记录核对，本页不作判定。

## p.014（PDF p.14 / 印刷 p.526）
- PNG：/tmp/linden07_audit_p014.png（pngmono 150dpi）
- 核对：p.525 跨页续段 `provided.`…、Hu `[10]` 引文段（`s_{ij}(μ)`、`[19]`）、Proposition 3.1 `([3, Lemma 6.2])` 陈述与三条分列 (1)(2)(3)、公式 (3.1) 全部要素、`(r)^+ = max(0,r)` 说明段、`[17]` 句、Corollary 3.2 陈述、公式 (3.2)、`s_{ij}(μ)` 恒等式句、`[3]; see Figure 1` 句、Lemma 3.3 `([3, Lemma 6.1])` 陈述、运行头
- 结果：PASS±（7 处标点脱离已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 291 行）：印刷「…explicit interpretation in terms of the pointwise dimension of μ_x^{ij} **[19].**」（页图第 12 行、文本层第 14–15 行）方括号后有句点；MD 原件 `\ [ 1 9 ]$` 收尾无句点。已补 `$.`。
  2. **已修复**（MD 第 297 行）：印刷 (2) 条末「…then s_{ij}(μ) = 1**.**」（页图第 15 行、文本层第 26 行）有句点；MD 原件缺失。已补 `.$`。
  3. **已修复**（MD 第 299 行）：印刷「(3) For any **t** ∈ Σ**,**」（页图第 16 行、文本层第 28 行）行末有逗号（后接展示式 (3.1)）；MD 原件缺失。已补 `,$`。
  4. **已修复**（MD 第 305 行）：印刷「Here (r)^+ = max(0, r) denotes the positive part of r ∈ ℝ**.**」（页图第 19 行、文本层第 34 行）有句点；MD 原件缺失。已补 `$.`。
  5. **已修复**（MD 第 311 行）：印刷「A basic property of the entropy is that for any **t** ∈ Σ**,**」（页图第 21 行、文本层第 44 行）行末有逗号（后接展示式 (3.2)）；MD 原件缺失。已补 `,$`。
  6. **已修复**（MD 第 317 行）：印刷「As we will see this gives nontrivial identities between the s_{ij}(μ)**.**」（页图第 24 行、文本层第 46 行）有句点；MD 原件缺失。已补 `$.`。
  7. **已修复**（MD 第 321 行）：印刷 Lemma 3.3 末「Then μ is U_{ik}-invariant**.**」（页图第 28 行、文本层第 52 行）有句点；MD 原件缺失。已补 `.$`。
  8. MD 缺运行头「526 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  9. 字形/字距伪影：MD 第 291 行 `[ 1 9 ]`（引文号内插入空格）；第 297 行 `I f a . s .` 与 `i . e .`；第 321 行 `U _ { i k } – i n v a r i a n t`（`-invariant` 被拆为 en-dash + 字距）。字母与数字顺序未变，排版级，不改。
  10. 印刷断词残留：印刷第 51–52 行把 `non-` / `atomic` 跨行断开，MD 第 321 行作 `non-atomic` 保留连字符（正确合词应为 `nonatomic`，与同句前半的 `atomic` 并列时易混）。语义唯一明确，排版级，不改（与 p.013 的 `non-trivial` 属同一类，登记不批量处理）。
  11. 行内紧排缺空格：第 289、291、293、295、297、299、305、307、309、311、317、319、321 行密集。排版级，不改。
- 公式 (3.1) 逐要素核对（150dpi 页图第 17–18 行 + 文本层第 28–31 行双证）：
  - 印刷 `h_μ(α^t) = Σ_{i,j} s_{ij}(μ)(t_i − t_j)^+.` 编号 (3.1)
  - MD 第 302 行 `\mathsf {h} _ {\mu} (\alpha^ {\mathbf {t}}) = \sum_ {i, j} s _ {i j} (\mu) (t _ {i} - t _ {j}) ^ {+}.\tag{3.1}`
  - ——**求和号下标 `i, j`、被加项 `s_{ij}(μ)`、括号内差 `t_i − t_j` 的下标方向与减号、`^+` 正部记号落在括号组上而非单项上、行末句点与编号 (3.1) 全部吻合**，无系数或上下标错位。
- 公式 (3.2) 逐要素核对：印刷 `h_μ(α^t) = h_μ(α^{−t}).` 编号 (3.2)（页图第 23 行、文本层第 45 行）；MD 第 314 行 `\mathsf {h} _ {\mu} (\alpha^ {\mathbf {t}}) = \mathsf {h} _ {\mu} (\alpha^ {- \mathbf {t}}).\tag{3.2}`——**右端 `α^{−t}` 的负指数与两处下标 μ 均正确**，编号吻合。
- Proposition 3.1 逐要素核对（MD 第 293–305 行）：引文 `([3, Lemma 6.2])` 未错；`Let μ be an A-invariant and ergodic probability measure on X = G/Γ with G = SL(k,ℝ) and Γ < G discrete`；`for any pair of indices i, j there are constants s_{ij}(μ) ∈ [0,1] so that:`；(1) `s_{ij}(μ) = 0 if and only if for a.e. x, μ_x^{ij} are atomic and supported on a single point.`；(2) `If a.s. μ_x^{ij} are Haar (i.e. μ is U_{ij} invariant), then s_{ij}(μ) = 1.`；(3) `For any t ∈ Σ,` —— **常数取值区间 `[0, 1]` 的端点与 (1) 的「当且仅当」方向均正确**。
- Corollary 3.2 与 Lemma 3.3 核对（MD 第 309、321 行）：印刷 `For any t ∈ Σ, the entropy h_μ(α^t) is positive if and only if there is a pair of indices i, j with t_i − t_j > 0 for which μ_x^{ij} are nontrivial a.s.`（页图第 25–26 行）—— **`t_i − t_j > 0` 的不等号方向正确**；Lemma 3.3 引文 `([3, Lemma 6.1])`、`i, j, k distinct indices`、`both μ_x^{ij} and μ_x^{jk} are non-atomic a.e. Then μ is U_{ik}-invariant` ——**`ij`/`jk` 两个条件测度与结论中的 `U_{ik}` 均未被误写**，下标链正确。
- 其余逐项核对：`A similar proposition holds for more general semisimple groups G. In particular we get the following (which is also proved in a somewhat different way in [17]):`（MD 第 307 行）；`We note that the converse to (2) is also true.`；`The following is a key lemma from [3]; see Figure 1.`（第 319 行）—— **引文 `[3]`、`[10]`、`[17]`、`[19]`、`[3, Lemma 6.2]`、`[3, Lemma 6.1]` 全对，无编号串行**。
- 页边界核对：MD 第 289 行首的 `provided.` 承接 p.525 页末，衔接正确；印刷 p.526 止于 Lemma 3.3，MD 第 321 行对应结束，无跨页错接，Figure 1 实现在 p.015 核对。

## p.015（PDF p.15 / 印刷 p.527）
- PNG：/tmp/linden07_audit_p015.png（pngmono 150dpi）
- 核对：Figure 1 图本体与图注、Proof of Theorem 2.2 起始句、四个集合定义式 `C_ℓ / R_ℓ / C_ℓ^L / R_ℓ^L`、`μ_x^{ia}/μ_x^{ab}/μ_x^{ib}` 三测度与 `C_a ⊂ C_b^L, R_b ⊂ R_a^L` 包含关系、`t` 与 `s_aa = 0` 设定、公式 (3.3) 两行、公式 (3.4)、`s_{ia}(μ) ∈ [0,1] for a = 2,…,k`、`t′` 段与最终不等式链、运行头
- 结果：PASS±（1 处标点脱离已修复；另登记 1 项**图片引用路径**的打包层发现，属 repo 级布局约定，不属本页转录缺陷，未改动）
- 差异列表：
  1. **已修复**（MD 第 345 行）：印刷「…we get |R_a^L| ≤ |C_a|**|**」（页图第 24 行、文本层第 43 行）句末有句点；MD 原件缺失。已补 `$.`。
  2. **图片引用路径（打包层，非内容缺陷，登记不改）**：MD 第 323 行 `![](images/page_14_image_0.jpg)` 的相对路径**无法从该 MD 自身所在目录解析**。实测：MD 位于 `…/Lindenstrauss_2007_littlewood_published_mineru/Lindenstrauss_2007_littlewood_published__Lindenstrauss_2007_littlewood_published.md`，而图片实体在 `…/Lindenstrauss_2007_littlewood_published_mineru/Lindenstrauss_2007_littlewood_published/images/page_14_image_0.jpg`（`file` 实测 `JPEG image data, JFIF standard 1.01, …, 565x343`，12,062 字节）。逐条实测结果：MD 共 4 处图片引用（第 323、513、577、593 行），`missing-from-md-dir=4`，但 4/4 在嵌套短名目录下均存在（`OK(nested)`）。同目录下姊妹篇 `Lindenstrauss_2006_littlewood_exceptions_mineru/Lindenstrauss_2006_littlewood_exceptions/images/page_14_image_0.jpg` 以及 Okounkov / Quillen / Huh 各篇均为同一「扁平 md + 短名子目录内 assets」的 kit 导出布局，故判定为**全 repo 打包层约定**，不是本篇或本页的 MinerU 转录缺陷。修改它需动 `images/` 目录层级（超出本块只写 md+AUDIT 的授权），或只改本篇 4 条路径而与姊妹篇不一致；该决定属 canonical integrator / 结构 owner，本块如实登记、**未擅自改动**。
  3. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 527」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  4. 行内紧排缺空格：第 325、327、333、339、345、347 行（如「the translation produced along$U _ { i k }$when going along」「Suppose i$\in C _ { a } ;$then」「Since by assumption$\mu _ { x } ^ { a b }$are nontrivial$\mathrm { { a . e . } }$」）。排版级，不改。
  5. 行内数学加粗拍平：第 336 行 `\boldsymbol {\alpha^ {\mathbf {t}}}` 把印刷正体的 `α^t` 包进粗体命令，渲染字形相同，排版级，不改。
- Figure 1 图本体核对（150dpi 页图第 2–9 行 + 直接查看导出 JPEG 实体双证）：图形为一条 `x` 出发的叶状回路，标注自上而下为 `u_{jk}(s)`、`u_{ik}(rs)x`、`u_{ij}(r)`、起点 `x`。用 Read 打开 `…/Lindenstrauss_2007_littlewood_published/images/page_14_image_0.jpg` 目检，**四个标注与印刷页图逐字一致**，无缺标或串标；导出切图未丢失图中文字。
- 图注核对（MD 第 325 行）：印刷「Figure 1: One key ingredient of the proof of Lemma 3.3 in [3] is the translation produced along U_{ik} when going along U_{ij} and U_{jk} and returning to the same leaf U_{ik}x.」——MD 与印刷**逐字吻合**，含图号、文献号 `[3]`、三个 U 下标（`ik`/`ij`/`jk`）与句末句点；本图是全篇首个带图页，图注完整性无问题。
- 四个集合定义式逐要素核对（150dpi 页图第 12–16 行、文本层第 20–23 行；MD 第 330 行）：
  - 印刷 `C_ℓ = {i ∈ {1,…,k} \ {a,b} : s_{iℓ}(μ) > 0},`
  - 印刷 `R_ℓ = {j ∈ {1,…,k} \ {a,b} : s_{ℓj}(μ) > 0},`
  - 印刷 `C_ℓ^L = {i ∈ {1,…,k} \ {a,b} : μ is U_{iℓ}-invariant},`
  - 印刷 `R_ℓ^L = {j ∈ {1,…,k} \ {a,b} : μ is U_{ℓj}-invariant}.`
  - MD 第 330 行 `C _ {\ell} = \{i \in \{1, \ldots , k \} \setminus \{a, b \}: s _ {i \ell} (\mu) > 0 \}, \\ R _ {\ell} = \{j … s _ {\ell j} …\}, \\ C _ {\ell} ^ {L} = \{i … \mu \text {is} U _ {i \ell} \text {-invariant} \}, \\ R _ {\ell} ^ {L} = \{j … \mu \text {is} U _ {\ell j} \text {-invariant} \}.`
  - ——**`s_{iℓ}`/`s_{ℓj}` 与 `U_{iℓ}`/`U_{ℓj}` 的上下标方向逐一核对正确**（这四处若互换会实质改变集合定义），上标 `L` 位置、集合差 `\setminus \{a,b\}` 与严格不等号 `> 0` 亦全部吻合。
- 公式 (3.3) 逐要素核对（页图第 17–19 行、文本层第 31–34 行；MD 第 336 行）：印刷 `h_μ(α^t) = s_{a1}(μ) + ⋯ + s_{ak}(μ) = s_{ab}(μ) + |R_a^L| + Σ_{j∈R_a\R_a^L} s_{aj}(μ) > |R_a^L|,`——**求和下标 `j∈R_a\R_a^L`（集合差 R_a 减 R_a^L）、绝对值项 `|R_a^L|` 的上标 L、行末逗号与编号 (3.3) 全部吻合**。
- 公式 (3.4) 逐要素核对（页图第 22 行、文本层第 39–40 行；MD 第 342 行）：印刷 `h_μ(α^{−t}) = s_{1a}(μ) + ⋯ + s_{ka}(μ) = s_{ba}(μ) + Σ_{i∈C_a} s_{ia}(μ) ≤ (1 + |C_a|),`——**`α^{−t}` 的负指数、求和下标 `i∈C_a`、右端 `(1 + |C_a|)` 的常数 1 与绝对值、编号 (3.4) 全部吻合**。
- 不等式链核对（页图第 28 行、文本层第 47 行；MD 第 350 行）：印刷 `|R_a^L| ≤ |C_a| ≤ |C_b^L| ≤ |R_b| ≤ |R_a^L|,`——**五项链上三个带 L 上标的项（R_a^L、C_b^L、R_a^L）与两个不带 L 的项（C_a、R_b）位置与方向全部吻合**，行末逗号保留。
- 其余逐项核对：`For ℓ = a, b we define the sets`；`Suppose i ∈ C_a; then … Lemma 3.3 shows that μ_x^{ib} are Lebesgue a.e. This shows that C_a ⊂ C_b^L, and R_b ⊂ R_a^L follows similarly.`；`Let t = (t_1,…,t_k) with t_i = −1/k for i ≠ a and t_a = 1 − 1/k. For the following expression set s_aa = 0.`；`where we used our assumption that s_{ab}(μ) > 0. Applying Proposition 3.1 for α^{−t}…`；`where we used the fact that s_{ia}(μ) ∈ [0,1] for a = 2,…,k. However, since the entropies of α^t and of α^{−t} are equal…`；`Using t′ = (t′_1,…,t′_k) with t′_i = −1/k for i ≠ b and t′_b = 1 − 1/k instead of t … |C_b^L| ≤ |R_b|. Recall that C_a ⊂ C_b^L and R_b ⊂ R_a^L.` —— **逐句吻合**，三处 `−1/k` 与两处 `1 − 1/k` 的系数与减号方向均正确。
- 页边界核对：印刷 p.527 止于不等式链 `…≤ |R_a^L|,`；MD 第 350 行对应结束，后续证明在 p.016 核对，无跨页错接。

## p.016（PDF p.16 / 印刷 p.528）
- PNG：/tmp/linden07_audit_p016.png（pngmono 150dpi）
- 核对：p.527 跨页续段（基数论证、`s_{ab}(μ) + |R_a^L| ≤ h_μ(α^t) ≤ s_{ba}(μ) + |C_a|`）、公式 (3.5)、`C_a ⊂ C_b^L ⊂ C_a^L` 与 `R_b = R_b^L`、`U_{ij}`/`U_{ab}` 不变性段（QED）、Corollary 3.4 陈述（`s_{ab} = s_{ba}` 对称性）、§4 标题、`A'_{ab}` 交换性段、三个子群定义式 `L_{(ab)} / U_{(ab)} / C_{(ab)}`、度量约定段（`d(x,y) = d(I_k, g)`）、§4.1 标题、Definition 4.1 陈述、Lemma 4.2 陈述、Proof 首段、运行头
- 结果：PASS±（4 处偏离已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 359 行）：印刷「From this we conclude as before that C_a ⊂ C_b^L ⊂ C_a^L, and so C_a = C_a^L**.** Similarly, one sees R_b = R_b^L.」（页图第 5–6 行、文本层第 9–10 行）在 `C_a^L` 后有句点；MD 原件作 `…$C _ { a } = C _ { a } ^ { L }$ Similarly, one sees…` 两句粘连。已补 `.$`。
  2. **已修复**（MD 第 361 行）：印刷「…and get that μ is U_{ab}-invariant**.**」+ QED 方块（页图第 9 行、文本层第 14 行）在证毕前有句点；MD 原件句点缺失、QED 方块紧贴数学式。已补 `.$` 后接 `□`。
  3. **已修复**（MD 第 377 行）：印刷「…d(x, y) = d(I_k, g)**.**」（页图第 16 行、文本层第 37 行）行末有句点；MD 原件缺失。已补 `$.`。
  4. **已修复**（MD 第 381 行）：Definition 4.1 结尾印刷为「…satisfies **g ∈ L_{(ab)}** (**g ∈ C_{(ab)}** respectively)」（页图第 22–23 行、文本层第 43–44 行）——`L_{(ab)}` 的右圆括号闭合后另起括号给出另一种情形。MD 原件作 `$g \in L _ { ( a b ) } ~ ( g \in C _ { ( a b ) }$respectively).`：**右圆括号丢失，且被替换成一个伪关系符号 `\sim`**，会渲染出「g ∈ L(ab) ∼ (g ∈ C(ab) …」这种错误关系。已用 Edit 改回 `$g \in L _ { ( a b ) }$ ($g \in C _ { ( a b ) }$ respectively).`，括号层级与印刷一致。
  5. MD 缺运行头「528 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  6. 字体混排：MD 第 359 行前半用 `{\cal C}`（花体）而后半用普通 `C`，印刷四处一律花体 `C`。渲染差异轻微，排版级，不改。
  7. 字距/字形伪影：第 361 行 `{ \mathrm { - i n v a r i a n t } }` 与 `U _ { a b } – \mathrm { i n v a r i a n t }`（`-invariant` 被拆为 en-dash + 字距）；第 365 行无；第 381、383 行 `$A _ { a b } ^ { \prime } – r e t u r n s$`（`-returns` 同样拆为 en-dash + 字距）。字母顺序未变，排版级，不改。
  8. 行内紧排缺空格：第 353、359、361、363、365、371、377、381、383、385 行（如「we see that$s _ { a b } ( \mu ) + …$」「From this we conclude as before that${ \cal C }」「Instead of $a , b$and get that」「there exists a$g \in G$with$y = g x$and」）。排版级，不改。
- 公式 (3.5) 逐要素核对（150dpi 页图第 4 行、文本层第 7 行；MD 第 356 行）：印刷 `s_{ba}(μ) ≥ s_{ab}(μ) > 0.` 编号 (3.5)；MD `$s _ {b a} (\mu) \geq s _ {a b} (\mu) > 0.\tag{3.5}$` —— **`ba`/`ab` 顺序、`≥` 不等号方向、链式 `> 0` 与行末句点、编号 (3.5) 全部吻合**。
- 跨页续段不等式核对（MD 第 353 行）：印刷 `s_{ab}(μ) + |R_a^L| ≤ h_μ(α^t) ≤ s_{ba}(μ) + |C_a|` ——**左右两端 `s_{ab}` 与 `s_{ba}` 的对应关系未被互换**（互换会颠倒证明方向），两个绝对值项的 L 上标正确，中间熵项 `h_μ(α^t)` 的指数为 `t` 而非 `−t`，与印刷一致。
- `C_a ⊂ C_b^L ⊂ C_a^L` 与 `R_b = R_b^L` 核对（MD 第 359 行）：**三段包含链的中间项 `C_b^L` 与末项 `C_a^L` 未错位**，由第一段结论 `C_a ⊂ C_b^L`（p.527）加本页 `C_b^L ⊂ C_a^L` 得 `C_a = C_a^L`，逻辑与印刷一致。
- Corollary 3.4 核对（MD 第 365 行）：印刷「For any pair of indices (a, b), s_{ab} = s_{ba}. In particular, μ_x^{ab} are nontrivial a.s., if and only if, μ_x^{ba} are nontrivial a.s.」—— **对称等式与「当且仅当」方向正确**，`ab`/`ba` 两个条件测度未被互换。
- §4 起始段与子群定义核对（MD 第 369–375 行）：印刷「We let A′_{ab} = {α^s ∈ A : s_a = s_b}, and let α^s ∈ A′_{ab}. Then α^s commutes with U_{ab}, which implies that μ_x^{ab} = μ_{α^s x}^{ab} a.e.」——**等式中左右两侧的 `μ_x^{ab}` 与 `μ_{α^s x}^{ab}` 未混淆**；三式 `L_{(ab)} = C(U_{ab}),`、`U_{(ab)} = ⟨U_{ij} : i = a or j = b⟩,`、`C_{(ab)} = C(H_{ab}) = C(U_{ab}) ∩ C(U_{ba}).` ——**第三个式子的两个中心化子 `C(U_{ab})` 与 `C(U_{ba})` 及其交集 `∩` 全部正确**（左右互换会改变中心化子本身），逐项吻合。
- Definition 4.1 逐要素核对（MD 第 381 行）：`for K ⊂ X that the A′_{ab}-returns to K are exceptional (strong exceptional)`、`if there exists a δ > 0 so that for all x, x′ ∈ K, and α^s ∈ A′_{ab} with x′ = α^s x ∈ B_δ(x) ∩ K every g ∈ B_δ^G with x′ = gx satisfies …` —— **`B_δ(x)`（X 上）与 `B_δ^G`（G 上带 G 上标）两个球的记号未被混同**，`x′ = α^s x` 与 `x′ = gx` 两个条件式均在位，例外情形 `C_{(ab)} respectively` 亦正确。
- Lemma 4.2 与 Proof 首段核对（MD 第 383、385 行）：印刷「There exists a null set N ⊂ X such that for any compact K ⊂ X \ N with exceptional A′_{ab}-returns to K the A′_{ab}-returns to K are in fact strong exceptional.」——**`K ⊂ X \ N` 的集差方向与印刷一致**；Proof 首段「we may assume without loss of generality that a = 1, b = 2, and write A′, U, L, C for A′_{12}, U_{(12)}, L_{(12)}, C_{(12)} respectively.」——**四个简写与四个全称的对应顺序正确**。
- 页边界核对：印刷 p.528 止于 Proof 首段的 `We`（页图末行）；MD 第 385 行对应结束，后续在 p.017 核对，无跨页错接。

### 本段溯源（git show 基线导出）

对本段修复的 22 处逐处回查（worktree 内执行 `git show <rev>:"2010年 - Lindenstrauss/…__Lindenstrauss_2007_littlewood_published.md"`）：

| rev | 身份 | 行数 | 结论 |
|---|---|---|---|
| `d351abbff` | MinerU 原始导出首次入库提交（`mineru: 入库重试批次产出的 24 个导出…`） | 1502 | **22 处缺陷全部已在此版本存在** |
| `847882f32` | `integrate(audit): harvest Peer-P16` | — | 与 `d351abbff` 同形，无改坏 |
| `078d4ecb` | `cpf-redo/…^`（redo p.007 提交，任务指定的基线 rev） | 1499 | 22 处缺陷**同样全部在位** |

- 逐条计数实测（`grep -cF` 对缺陷特征串在两个文件分别计数）：21 条特征串在 `d351abbff` 与 `078d4ecb` 中计数均为 `1/1`（`p233` 的 `invariant under$U _ { i j }$` 特征串在两文件中各 2 次，均落在印刷上不同位置，结论不变）。另 2 条改用精确锚点复核：`p253`（Theorem 1.6 (2) 行）在 `d351abbff` 中位于第 75 行，行尾字节与基线**完全一致**（`…\setminus \Xi _ { k }$`，无句点）；`p377` 用精确锚点 `and$d ( x , y ) = d ( \operatorname { I } _ { k } , g )$` 计数为 `orig=1 / base=1`。
- **结论：本段 22 处修复没有任何一处属于「后被某个 peer 改坏的回归」**。`d351abbff`（原始导出）与 `078d4ecb`（基线）之间的 280 行差异经逐条查看**全部是 Peer-P16/redo 块的改善**（`Hausdorf→Hausdorff`、`diferent→different`、`dim Π_H Ξ→dim_H Ξ`、`lim in→liminf`、`efective→effective`、行末句点补齐等），未见任何把正确内容改坏的回归。本段修复是对 MinerU 原始导出既有缺口的首次纠正。
- p.016 第 381 行 Definition 4.1 的 `\sim` 伪关系符一节同样在原始导出中即存在（`orig=1`），属导出缺口而非回归。

### 本段交付自检与边界

- 交付自检：`grep -c '^## p\.' AUDIT-Lindenstrauss_2007_littlewood_published.md` 实测输出 **`16`**，对应块 A（p.001–p.008）8 条 + 本段（p.009–p.016）8 条，无合并、无跳页。
- 本段分级汇总：**PASS± 8 页**（p.009–p.016），**PASS 0 页**，**FAIL 0 页**。逐页改动处数：p.009 = 0、p.010 = 3、p.011 = 4、p.012 = 3、p.013 = 1、p.014 = 7、p.015 = 1、p.016 = 4，合计 `edits=23`（其中 p.015 另有 1 项图片引用路径的打包层发现，未改动，见该页登记）。
- 写入范围合规：本段只写本 AUDIT 文件与本篇 MinerU Markdown；**未**执行任何 git 写操作（无 add/commit/merge/push）；**未**碰根 `AUDIT-INDEX.md`/`AUDIT-PROGRESS.log`/`MEMORY.md`/`README.md`；**未**写 `audit-redo/` 新图（PNG 按指令留在 `/tmp/linden07_audit_pNNN.png`，持久化归档责任留给 canonical integrator）；**未**碰姊妹篇 `Lindenstrauss_2006_littlewood_exceptions*`；**未**启动或改动 mineru。PDF 只读，SHA-256 仍为 `7f26dde3f9b206534584b2b94d4a86e6319e467918efca8b4d00b1b1ae574825`。
- 编辑手段合规：22 + 2 处修改**全部**用 Edit 工具逐处定位完成，未用 Python/正则/sed/heredoc 或任何脚本写回 Markdown。定位手段有两处需如实登记：① `p.012` 第 253 行的字节含 `\rangle`，Edit 的 `old_string` 中 `\r` 会被当作回车转义而无法命中，改用全篇唯一的 `rangle$` 锚点（`grep -c 'rangle\$'` 实测 = 1）完成；② 其余各处均先用 `grep -cF` 确认锚点唯一再编辑（p.014 七个锚点计数全为 1，p.016 四个锚点计数全为 1）。
- 工作区状态提示：块 A 与前序 redo 块（Wf-R-P16，p.009）遗留的未提交改动均已原样保留，未被本段覆盖或回退。

---

# 追加段：redo 块 C（PDF p.17–p.24，actor=`linden07`）

- 性质：同块 A/B，对 Peer-P16 记录与既有 redo 块的独立重做复核；每页重新渲染 PNG 目检 + `pdftotext` 文本层互证，唯一裁决源是印刷原页。
- 身份：actor=`linden07`；host=zcode Desktop；model=`opencode-go-chat/space-bunny-free`（本会话运行时自报）；effort=run 级配置未暴露，记 `UNKNOWN`。cwd=`/Users/aurolafly/.zcode/worktrees/cpf-redo-Lindenstrauss_2007_littlewood_published`；branch=`cpf-redo/Lindenstrauss_2007_littlewood_published`。
- PDF 只读证据：同一 PDF，SHA-256=`7f26dde3f9b206534584b2b94d4a86e6319e467918efca8b4d00b1b1ae574825`（本段收尾再次 `shasum -a 256` 实测复核，见段末）。
- 写入范围同前：只写本 AUDIT 文件与本篇 MinerU Markdown；未写根级真值文件、未写 `audit-redo/`、未执行 git 写操作、未碰姊妹篇、未碰 mineru。

## p.017（PDF p.17 / 印刷 p.529）
- PNG：/tmp/linden07_audit_p017.png（pngmono 150dpi）；公式 `f(x)=max(…)` 终裁：/tmp/l07_p017_fx.png（300dpi 原页裁片，PIL 仅用于裁图，未写 Markdown）
- 核对：Lemma 4.2 证明续段起始句、公式 (4.1) 矩阵分块式全元素、行列向量约定段（`Mat(k−2,ℝ)`、`k = 3` 特例）、`g ∈ L` 与 `g ∈ C` 的零块判据、`D_ℓ` 定义与 `⋃_{ℓ=1}^∞ D_ℓ = X`、`E_{ℓ,s}` 定义、可测函数 `f(x)`、`t = (−1,1,0,…,0)` 与六个共轭系数、`f(α^{−nt}x) ≤ e^{−n}f(x)`、Poincaré recurrence 段、`N_ℓ` 与 `N` 构造、最后一段 K 的取用（`g̃ = α^{s̃−s}g`、`D_{1/ℓ}\N_{1/ℓ}`）与 QED、Proposition 4.3 引出句、运行头
- 结果：PASS±（3 处标点脱离已修复；一处疑似上下标错误经 300dpi 仲裁**排除**）
- 差异列表：
  1. **已修复**（MD 第 387 行）：印刷「write, for a given matrix g ∈ G**,**」（页图第 2 行、文本层第 3 行）在 `$G$` 后有逗号（后接展示式 (4.1)）；MD 原件缺失。已补 `,$`。
  2. **已修复**（MD 第 395 行）：印刷「…for every compact set, K ⊂ D_ℓ for some ℓ > 0**.**」（页图第 7 行、文本层第 17 行）行末有句点；MD 原件缺失。已补 `$.`。
  3. **已修复**（MD 第 403 行）：印刷「…or equivalently α^s x ∈ B^C_{1/ℓ}(x) for a.e. x ∈ D_ℓ with α^s x ∈ B^L_{1/ℓ}(x)**.**」（页图第 13 行、文本层第 31–33 行）行末有句点；MD 原件缺失。已补 `$.`。
  4. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 529」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  5. 重音分解：MD 第 403 行 `Poincar´e`（U+00B4+e）。字形级，不改。
  6. HTML 伪影：MD 第 403 行把 `g_{1*}` 写成 `g _ { 1 }$<sub>∗</sub>`（夹在行内数学中）。渲染字形相同，排版级，不改。
  7. 字距伪影：第 393 行 `r e s p . ~`、`\mathrm { M a t }`；第 403 行 `$\mathrm { a . e . }$ $- \mathrm { \ o c r }$equivalently`、`\mathrm { a . e . ~ }`。字母顺序未变，排版级，不改。
  8. 表述微调：印刷「and furthermore so that δ = 1/ℓ can be used in…」（页图第 20 行、文本层第 40 行）MD 第 407 行作「and so that δ = 1/ℓ can be used in…」；印刷「By assumption on K, we have that g ∈ L.」MD 第 408 行作「By assumption on $K$, $g\in L$.」。语义与指称不变，不误导，登记不改（该两行已由前序 peer 重排为规范 LaTeX，属改进）。
  9. 行内紧排缺空格：第 387、393、395、397、403、405 行密集（如「for a given matrix$g \in G$」「let$D _ { \ell }$be the set of$x \in X$with the property」「be the set of points x for which」「we arrive at a nullset$N _ { \ell }$」）。排版级，不改。
- **300dpi 仲裁（关键，排除一处疑似错误）**：150dpi 页图中 `f(x)` 公式第三项范数的下标星号位置难以判读，初看疑似 MD 写成 `g_{*2}` 而印刷为 `g_{2*}`。按 SOP 用 `-r300` 重渲同页并用 PIL 裁切放大（裁切框 `(900,1380,2350,1470)`，输出 /tmp/l07_p017_fx.png，仅裁图不写 Markdown）后目检：**印刷原式为 `f(x) = max(|g_{12}|, ‖g_{1*}‖, ‖g_{*2}‖) for x ∈ E_{ℓ,s}.`，第三项确为 `g_{*2}`（星号在左、2 在右）**，与 MD 第 400 行 `\left\| g _ {* 2} \right\|` **一致**。该疑点排除，不构成缺陷，亦不改 MD。此项也与印刷判据「g ∈ C iff in addition g_{12}, g_{1*}, g_{*2} are zero」自洽（三项恰为 max 所取的三块），可交叉印证。
- 公式 (4.1) 矩阵逐元素核对（150dpi 页图第 3–6 行、文本层第 5–7 行；MD 第 390 行）：印刷
  `g = ( a_1  g_{12}  g_{1*} ; g_{21}  a_2  g_{2*} ; g_{*1}  g_{*2}  a_* )` ——**九个矩阵元素逐格核对与行/列向量归属全部吻合**（第 1 行 `a_1,g_12,g_{1*}`；第 2 行 `g_21,a_2,g_{2*}`；第 3 行 `g_{*1},g_{*2},a_*`），编号 (4.1) 与行末逗号在位。
- 零块判据核对（MD 第 393 行）：印刷「Then g ∈ L if and only if a₁ = a₂ and **g_{21}, g_{*1}, g_{2*}** are all zero. g ∈ C if in addition **g_{12}, g_{1*}, g_{*2}** are zero.」——MD 与印刷**逐项一致**，`g ∈ L` 的三个零块（`g_{21}, g_{*1}, g_{2*}`）与 `g ∈ C` 的追加三个零块（`g_{12}, g_{1*}, g_{*2}`）均未错位（这是本页最易因上下标混淆而出错处）。旧 Peer-P16 p.017 记录的「恢复矩阵零块判据中的 `g_{2*}`」修复**经本段复核确认现值正确**。
- 约定段核对（MD 第 393 行）：`a_1, a_2, g_{12}, g_{21} ∈ ℝ`、`g_{1*}, g_{2*} (resp. g_{*1}, g_{*2}) are row (resp. column) vectors with k − 2 components`、`a_* ∈ Mat(k − 2, ℝ)`、`(For k = 3 of course all of the above are real numbers, and we can write 3 instead of the symbol *)` —— **行列向量归属（row↔g_{1*},g_{2*}；column↔g_{*1},g_{*2}）与维数 `k − 2` 两处出现均正确**。
- `D_ℓ` 与 `E_{ℓ,s}` 段核对（MD 第 395、397 行）：`⋃_{ℓ=1}^∞ D_ℓ = X` 的并集上下限正确；`for all z ∈ B_{1/ℓ}(x) there exists a unique g ∈ B^G_{1/ℓ} with z = gx`；`E_{ℓ,s} ⊂ D_ℓ`；`x' = α^s x ∈ B_{1/ℓ}(x)`；`g ∈ B^G_{1/ℓ} ∩ L = B^L_{1/ℓ}`；`g ∈ B^G_{1/ℓ} is uniquely determined by x (for a fixed s)` —— **`B^G_{1/ℓ}` 与 `B^L_{1/ℓ}` 两个球记号的上标未被混同**，逐句吻合。
- 共轭系数核对（MD 第 403 行）：印刷「the entries of α^t g α^{−t} corresponding to g_{12}, g_{1*}, g_{2*} are **e^{−2}g_{12}, e^{−1}g_{1*} and e^{−1}g_{2*}**, and those corresponding to g_{21}, g_{*1}, g_{*2} are **e^2 g_{21}, e g_{*1} and e g_{*2}**」——**六个指数 −2/−1/−1 与 2/1/1 逐一吻合**（`t = (−1,1,0,…,0)` 下 `α^t g α^{−t}` 的第 ij 元系数为 `e^{(t_i−t_j)}`，与印刷自洽）；`f(α^{−nt}x) ≤ e^{−n}f(x)` 的负指数 `−n` 正确。
- K 取用段核对（MD 第 407–409 行）：`K ⊂ X \ N`、`δ = 1/ℓ`、`Choose a rational s̃ ∈ Σ close to s`、`g̃ = α^{s̃−s}g satisfies α^{s̃}x = g̃x, so g̃ ∈ B^L_{1/ℓ}`、`Since x ∈ K ⊂ D_{1/ℓ} \ N_{1/ℓ}, it follows that g̃ ∈ C`、`Going back to x' = α^s x and g, it follows that g ∈ C.` + QED 方块 ——**集合差 `D_{1/ℓ} \ N_{1/ℓ}` 的方向与印刷一致**，QED 方块在位。
- 页边界核对：印刷 p.529 止于「…exactly Theorem 2.3(2).」；MD 第 411 行对应结束，Proposition 4.3 属 p.530，留待 p.018 核对，无跨页错接。

## p.018（PDF p.18 / 印刷 p.530）
- PNG：/tmp/linden07_audit_p018.png（pngmono 150dpi）；δ/δ′ 终裁：/tmp/l07_p018_delta.png、/tmp/l07_p018_delta3.png（300dpi 原页裁片，PIL 仅裁图）
- 核对：Proposition 4.3 陈述与两个等价条件 (1)(2)、`𝓔′`/`𝓔` σ-代数与 Lebesgue space 段、`μ^E_x` 条件测度与原子 `[x]_E`、公式 (4.2)、`A′ = A′_{ab}` 与 `C = C_{(ab)}` 简化约定、`f_r(x) = μ^E_x(B^C_r(x))`、`f_r(x) ↗ 1`、`C_r = {x : f_r(x) > 1/2}`、公式 (4.3)、等距映射段（`B^G_{3δ′}`、`B^C_{2r}`、闭球 `B^C_{δ′}`、`\bar B^C_{3δ′}(x)`、`\bar B^C_{2r}`、`\eta`）、`δ = min(\eta, δ′)`、`C_r = ⋃_{δ>0} D_δ`、运行头
- 结果：PASS±（4 处已修复；一处疑似 δ/δ′ 错误经 300dpi 仲裁**排除**）
- 差异列表：
  1. **已修复**（MD 第 427 行）：印刷「gives the ergodic decomposition of μ with respect to A′_{ab}**.**」（页图第 14 行、文本层第 25 行）行末有句点；MD 原件缺失。已补 `.$`。
  2. **已修复**（MD 第 429 行）：印刷「For simplicity, we write A′ = A′_{ab} and C = C_{(ab)}**.**」（页图第 15 行、文本层第 26 行）行末有句点；MD 原件缺失。已补 `.$`。
  3. **已修复**（MD 第 437 行，重复逗号）：MD 原件作 `$\mu ( C _ { r } ) > 1 - \varepsilon ,$, where…`——数学定界符内已有一个逗号，紧随其后又补了一个逗号，形成**重复逗号**；印刷（页图第 17 行、文本层第 32 行）只有单逗号「with μ(C_r) > 1 − ε, where C_r = {x : f_r(x) > 1/2}.」。已删去多余逗号，改为 `$\mu ( C _ { r } ) > 1 - \varepsilon ,$ where…`。
  4. **已修复**（MD 第 437 行，同句末句点）：印刷「…where C_r = {x : f_r(x) > 1/2}**.**」（页图第 17 行、文本层第 32 行）行末有句点；MD 原件缺失。已在同一次 Edit 中一并补 `$.`（第 3、4 项为同一行的两处缺陷，合并为一次定位、两处字节改动）。
  5. **已修复**（MD 第 445 行）：印刷「It follows that (4.3) holds with δ = min(η, δ′)**.** In other words, C_r = ⋃_{δ>0} D_δ, where」（页图第 22–23 行、文本层第 47–50 行）在 `min(η,δ′)` 后有句点；MD 原件作 `…( \eta , \delta ^ { \prime } )$ In other words…` 两句粘连。已补 `.$`。
  6. MD 缺运行头「530 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  7. **300dpi 仲裁（关键，排除一处疑似错误）**：150dpi 与 `pdftotext` 文本层显示闭球下标为「Bδ」（无撇），初看疑似 MD 把印刷的 `δ` 误写成 `δ′`（MD 第 445 行四处闭球均用 `\delta ^ { \prime }`）。按 SOP 用 `-r300` 重渲同页并裁切放大（框 `(1250,2320,1900,2400)` 放大 4×，输出 /tmp/l07_p018_delta3.png）后目检：**印刷原式确为 `\overline{B^C_{δ'}(x)}, \overline{B^C_{δ'}(gx)}`、`h \in \overline{B^C_{δ'}}`、`hx \in \overline{B^C_{δ'}(gx)}`，四处的 δ 均带撇**；同一行 `B^G_{3δ'}` 的撇亦清晰可辨。**MD 现值正确，疑点排除，不构成缺陷，不改 MD**。文本层在此处丢撇属 SOP 已预告的失真，裁决一律以裁片为准。
  8. 闭球命令不统一：MD 第 445 行同段内混用 `\overline { { B _ { … } ^ { C } } }` 与 `\mathsf { \bar { B } } _ { … } ^ { C }` 两种写法，印刷统一为闭球记号。语义等价，排版级，不改。
  9. 表述微调：印刷「Since 𝓔 consists of A′_{ab}-invariant sets, **a.e. conditional measure** is A′_{ab}-invariant, **and** can be shown to be ergodic.」（页图第 16 行、文本层第 19–20 行）；MD 第 421 行作「almost every conditional measure is A′_{ab}-invariant and can be shown to be ergodic.」——`a.e.` 展开为 `almost every`、逗号略去，语义与量词强度不变，不误导，登记不改。该行旧 Peer-P16 记录的「删除条件测度 A′_{ab}-invariant 后多出的星号」修复**经本段复核确认已生效**（现值无多余星号）。
  10. 字距/字形伪影：第 415、417 行 `– o r b i t`、`– r e t u r n s`；第 419 行 `A . e .`、`$\mathcal { E } .$` 的句点位置。字母顺序未变，排版级，不改。
  11. 行内紧排缺空格：第 413、415、417、419、427、429、431、437、439、445 行密集（如「For any pair of indices$a , b$the following」「ergodic component of$\mu$with respect to」「For every$\varepsilon > 0$there exists」「Proof. For simplicity, we write$A ^ { \prime } = …$and」「Suppose a.e.$A ^ { \prime }$ergodic component」）。排版级，不改。
- A′ 标签 prime 复核（关键，前序修复确认）：MD 第 415 行 (1) 条与第 417 行 (2) 条的 `$A _ { a b } ^ { \prime }$` **prime 均在位**（印刷页图第 4 行与第 7 行同样带撇），(2) 条作「the A′_{ab}-returns to K are strong exceptional」，与印刷一致。旧 Peer-P16 p.018 记录的「恢复 exceptional-return 标签 A′ 中被控制字符替代的 prime」**修复正确，本段确认**。
- 公式 (4.2) 逐要素核对（页图第 13 行、文本层第 22–24 行；MD 第 424 行）：印刷 `μ = ∫_X μ^E_x dμ` 编号 (4.2)；MD `\mu = \int_ {X} \mu_ {x} ^{\mathcal {E}} \mathrm{d} \mu\tag{4.2}` ——**积分变量 `X`、上标 𝓔、被积条件测度与右端 `dμ`、编号 (4.2) 全部吻合**。
- 公式 (4.3) 逐要素核对（页图第 19 行、文本层第 34–35 行；MD 第 442 行）：印刷 `B^C_{2r}(x) ∩ B_δ(x) = B^C_δ(x).` 编号 (4.3)；MD `B _ {2 r} ^ {C} (x) \cap B _ {\delta} (x) = B _ {\delta} ^ {C} (x).\tag{4.3}` ——**左端 `B^C_{2r}` 的 2r 下标、`∩`、右端 `B^C_δ` 的 δ 下标与上标 C 位置、行末句点、编号 (4.3) 全部吻合**。
- `f_r` 与 `C_r` 核对（MD 第 434、437 行）：印刷 `f_r(x) = μ^E_x(B^C_r(x)).`（页图第 16 行、文本层第 30 行）——**上标 𝓔 与球记号 `B^C_r` 的上标 C 均正确**；`By the assumption f_r(x) ↗ 1 for r → ∞ and a.e. x.`（文本层第 31 行）——MD 第 437 行用 `f _ { r } ( x ) ~ \nearrow ~ 1` **正确表达了印刷的 ↗ 箭头**（非字面 tilde），此处判定为正确而非伪影；`C_r = {x : f_r(x) > 1/2}` 的**阈值 1/2 正确**（页图第 17 行可读）。
- 等距段其余逐项核对（MD 第 445 行）：`there exists δ′ > 0 so that the map g ↦ gx from B^G_{3δ′} to X is an isometry`（**`B^G_{3δ′}` 的上标 G 与下标 3δ′ 均正确**）；`In the latter case \bar B^C_{δ′}(gx) ⊂ B^C_{3δ′}(x)`（**包含号 ⊂ 方向正确**）；`Taking a finite subcover, we find some η > 0 so that d(gx, x) > η or gx ∈ B^C_{3δ′}(x) for every g ∈ B^C_{2r}`；`It follows that (4.3) holds with δ = min(η, δ′)`；`C_r = ⋃_{δ>0} D_δ` —— **η 与 δ′ 的 min 次序未被互换**，逐句吻合。
- 页边界核对：印刷 p.530 止于「and there exists δ > 0 with μ(D_δ) > 1 − ε.」（页图末行、文本层第 54 行）；MD 第 446 行 `D_δ = {x ∈ C_r : B^C_{2r}(x) ∩ B_δ(x) ⊂ B^C_δ(x)},` 承接并于 p.019 收尾，无跨页错接。

## p.019（PDF p.19 / 印刷 p.531）
- PNG：/tmp/linden07_audit_p019.png（pngmono 150dpi）；`a.e. – say for x ∉ N – a product measure` 终裁：/tmp/l07_p019_ae.png（300dpi 原页裁片，PIL 仅裁图）
- 核对：`D_δ` 定义式与 `μ(D_δ) > 1 − ε` 句、`K ⊂ D_δ` 强例外返回论证段（`μ^E_x = μ^E_{x′}`、`B^C_r(x)` 不可交、`B^C_{2r}(x)`、`B^C_δ(x)`）、(2)⟹(1) 段（`K_ℓ`、`μ(K_ℓ) > 1 − 1/ℓ`、`N = X \ ⋃_ℓ K_ℓ`、`B_{1/m}(z)`、`Cz`、`y_0/y_1/y_n` 序列、`d(z,y_1) < δ`、`α^{−s}`）、Lemma 4.4 两条陈述与两个展示式、Proof 前两段（`[3, Prop. 8.3]`、`(3) in Section 2.1`、`μ_{x,U} ∝ μ_{y,U}u`）、运行头
- 结果：PASS±（2 处已修复；一处疑似丢词经 300dpi 仲裁**排除**）
- 差异列表：
  1. **已修复**（MD 第 451 行）：印刷「and there exists δ > 0 with μ(D_δ) > 1 − ε**.**」（页图第 4 行、文本层第 54 行）行末有句点；MD 原件缺失。已补 `.$`。
  2. **已修复**（MD 第 459 行）：Lemma 4.4(1) 引导句末，印刷用 ASCII 逗号「…such that for x ∈ X \ N**,**」（页图第 15 行、文本层第 30 行）；MD 原件误用**全角逗号 `，`（U+FF0C）**。已改为 ASCII `,`。全篇全角逗号实测共 2 处（`grep -c '，'` → 2），另一处在 MD 第 881 行（约印刷 p.540 附近），**不在本块 p.017–p.024 范围内，本段不越权改动**，如实登记留给对应页次的审计员。
  3. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 531」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  4. **300dpi 仲裁（关键，排除一处疑似缺陷）**：MD 第 473 行作「…is a.e. – say for x ∉ N – **a** product measure…」，`\mathrm { - } \mathrm { a }` 疑似把印刷的 `almost` 截断成 `a`（若如此即为丢词的内容级缺陷）。按 SOP 用 `-r300` 重渲同页并裁切放大（框 `(450,2185,2350,2320)` 放大 2×，输出 /tmp/l07_p019_ae.png）后目检：**印刷原文自身即写作「is a.e. – say for x ∉ N – a product measure of the conditional measures μ^ij_x over all i, j」**，`a` 之后直接接 `product`，并无 `almost`。据此判定为**印刷原句本身的表述（非语法瑕疵但确为印刷原样），MD 忠实转录**；按铁律三「印刷原文自身的错字与怪癖原样保留」**不改 MD**，并在此登记为 print quirk。
  5. 表述微调：印刷「**So suppose** x ∈ K and x′ = α^s x ∈ K for some α^s ∈ A′.」（页图第 2 行、文本层第 4 行）MD 第 453 行作「Suppose x ∈ K and …」；印刷「Therefore B^C_r(x) and B^C_r(x′) cannot be disjoint, **and** x′ ∈ B^C_{2r}(x) **follows**.」MD 作「so x′ ∈ B^C_{2r}(x).」。语义与逻辑方向不变，登记不改。
  6. print quirk 忠实保留：印刷第 14 行「…so that the A′-returns to **K** are strong exceptional」用的是 `K` 而非 `K_ℓ`（疑为印刷笔误）；MD 第 455 行同样作 `the $A'$-returns to $K$ are strong exceptional`，**与印刷一致，不擅自改为 `K_ℓ`**。
  7. 字距/字形伪影：第 459 行 `i . e .`、`i = a \ o r\ j = b`；第 473 行 `\mathrm { - } \mathrm { a }`（见第 4 项，印刷原样）；第 477 行（属 p.032，不在本页范围）。排版级，不改。
  8. 行内紧排缺空格：第 459、462、465、471、473、475 行密集（如「$N \subset X$such that」「Proof. Set$U = U _ { ( a b ) }$and let」「By [3, Prop. 8.3] the conditional measure$\mu _ { x , U }$is a.e.」「there is a null set – enlarge N accordingly – such that for$x , y \notin N$and」）。排版级，不改。
- `D_δ` 定义式核对（MD 第 448 行）：印刷 `D_δ = {x ∈ C_r : B^C_{2r}(x) ∩ B_δ(x) ⊂ B^C_δ(x)},`（页图第 27 行、文本层第 52–53 行）——**左端 `B^C_{2r}` 的 2r 下标、`∩`、`⊂` 包含方向、右端 `B^C_δ` 的上标 C 与下标 δ、集合底集 `x ∈ C_r` 与行末逗号全部吻合**。
- `K ⊂ D_δ` 论证段核对（MD 第 453 行）：`Since x and x′ are in the same atom of 𝓔, the conditional measures satisfy μ^E_x = μ^E_{x′}`（**两处上标 𝓔 与下标 x/x′ 的对应未错**）；`By definition of C_r, we have μ^E_x(B^C_r(x)) > 1/2, and the same for x′`（**阈值 1/2 正确**）；`Therefore B^C_r(x) and B^C_r(x′) cannot be disjoint, so x′ ∈ B^C_{2r}(x)`；`By definition of D_δ, it follows that x′ ∈ B^C_δ(x)` —— 逐句与印刷吻合。
- (2)⟹(1) 段核对（MD 第 455、457 行）：`K_ℓ with μ(K_ℓ) > 1 − 1/ℓ`（**分母 ℓ 未错**）；`N = X \ ⋃_ℓ K_ℓ`（**`X \ ⋃` 的集差方向正确**）；`μ^E_x(B_{1/m}(z) ∩ K_ℓ) > 0 for all m ≥ 1`（**下标 1/m 与全称 `m ≥ 1` 均正确**）；`We claim that μ^E_x is supported on Cz, i.e. that μ^E_x(Cz) = 1`；`y_1 = α^s y_0 ∈ B_δ(z) ∩ K_ℓ`；`y_n ∈ A′y_0 ∩ K_ℓ with y_n → z`；`y_n ∈ B_δ(y_1) for large enough n`；`d(z, y_1) < δ`（**不等号方向 `<` 正确**）；`z ∈ B^C_δ(y_1)`；`y_1 ∈ Cz, y_0 = α^{−s}y_1 ∈ Cz, and the claim follows` + QED 方块 —— **`α^{−s}` 的负指数方向正确**，逐句吻合。
- Lemma 4.4 陈述核对（MD 第 459–471 行）：(1) 假设 `s_{ab}(μ) > 0 but s_{ij}(μ) = 0 for all i,j with either i = a or j = b`（**低熵情形的两个条件与印刷完全一致**）；展示式 `U_{(ab)}x ∩ X \ N ⊂ U_{ab}x.`（**`⊂` 方向与两端括号下标正确**）；(2) `unless μ is U_{ab}-invariant, it can be arranged that` + `μ^ab_x ≠ μ^ab_y` + `for any x ∈ X \ N and any y ∈ U_{(ab)}x \ N which is different from x.` —— **`≠` 号、`\N` 集差方向均正确**。
- Proof 段核对（MD 第 473、475 行）：`Set U = U_{(ab)} and let μ_{x,U} be the conditional measures for the foliation into U-orbits`；`By [3, Prop. 8.3]`（**引文号与命题号 8.3 未错**）；`μ_{x,U} is a.e. – say for x ∉ N – a product measure of the conditional measures μ^ij_x over all i,j for which U_{ij} ⊂ U`；`μ^ab_x is the only one of these which is nontrivial`；`μ_{x,U} – as a measure on U – is supported on the one-dimensional group U_{ab}`（**一维群的下标 ab 正确**）；`By (3) in Section 2.1`、`μ_{x,U} ∝ μ_{y,U}u`（**比例式方向正确**）、`u ∈ U_{ab}. This shows Lemma 4.4.(1).` —— 引文 `[3, Prop. 8.3]` 与节号 `2.1` 全对，逐句吻合。
- 页边界核对：印刷 p.531 止于「This shows Lemma 4.4.(1).」（页图末行、文本层第 50 行）；MD 第 475 行对应结束，Lemma 4.4(2) 的证明在 p.032，留待该页块核对，无跨页错接。

## p.020（PDF p.20 / 印刷 p.532）
- PNG：/tmp/linden07_audit_p020.png（pngmono 150dpi）
- 核对：Lemma 4.4(2) 证明收尾段（`μ_x^{ab} = μ_y^{ab}`、(3) in Section 2.1、(9) in Section 2.1、Haar a.e. – a contradiction）与 QED、§4.2 标题与首段、`a = 1, b = 2` 简化约定段（`u(r) = I_k + rE_{12} ∈ U_{12}`、`push forward`、`μ_x^{12}([a,b])` vs `μ_x^{12}(u([a,b]))`）、Poincaré recurrence 展示式、`x' = α^s x = gx` 段、`A′ ⊂ L_{12} = C(U_{12})` 段、公式 (4.4)、`x(r)=u(r)x` 与 `x'(r)=u(r)x'` 段、公式 (4.5)、归一化推论展示式、Ratner H-property 段（`[38], [39]`, `[29]`, D. Morris-Witte）、H-property 变体引出段、运行头
- 结果：PASS±（差异均为字形/排版级，不误导；**本页 MD 本段未修改**）
- 差异列表：
  1. MD 缺运行头「532 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  2. 重音分解：MD 第 483 行 `Poincar´e`（U+00B4+e）。字形级，不改。
  3. 公式编号位置：印刷把 (4.5) 排在公式**左侧**（页图第 19 行、文本层第 42 行 `(4.5)` 独占一行），MD 第 500 行用 `\tag{4.5}` 置于公式**右端**。编号内容与被编号公式完全对应，仅排版位置不同，排版级，不改。
  4. 连字符：印刷「with its **push forward** under the map」（页图第 11 行、文本层第 19 行）无连字符，MD 第 481 行作 `push-forward`。语义不变，排版级，不改。
  5. 行内紧排缺空格：第 477、479、483、489、491、497、503、509 行密集（如「we already know that$y \in$ $U _ { a b } x$」「the two equivalent conditions in Proposition 4.3 fail」「By Poincar´e recurrence we have for a.e.$x \in X$and every$\delta > 0$that」「Since$\alpha ^ { \mathbf { s } }$preserves the measure and since$A ^ { \prime } \subset L _ { 1 2 } = C ( U _ { 1 2 } )$the conditional measures satisfy」「are nontrivial, we can find many$r \in \mathbb { R }$so that」「and similarly for$x ^ { \prime } ( r )$and$x ^ { \prime }$」）。排版级，不改。
- 公式逐要素核对（150dpi 页图 + 文本层双证，全部吻合）：
  - `d(α^s x, x) < δ for some large α^s ∈ A′.`（页图第 11 行、文本层第 24 行）——MD 第 486 行 `d \left(\alpha^ {\mathbf {s}} x, x\right) < \delta \text { for some large } \alpha^ {\mathbf {s}} \in A ^ {\prime}.`，**不等号方向 `<`、上标 `s` 与 `A′` 的撇均在位**，句点保留。
  - (4.4) `μ^12_x = μ^12_{x′}.`（页图第 15 行、文本层第 30–31 行）——MD 第 494 行 `\mu_ {x} ^ {1 2} = \mu_ {x ^ {\prime}} ^ {1 2}.\tag{4.4}`，**右端下标 `x′`（带撇）与上标 12 均正确**，编号 (4.4) 与句点在位。
  - (4.5) `μ^12_{x(r)} u(r) ∝ μ^12_x`（页图第 19 行、文本层第 40–42 行）——MD 第 500 行 `\mu_ {x (r)} ^ {1 2} u (r) \propto \mu_ {x} ^ {1 2}\tag{4.5}`，**左端下标 `x(r)` 与因子 `u(r)` 的乘积、右端 `μ^12_x`、比例号 ∝ 方向（`x(r)` 测度 ∝ `x` 测度）全部吻合**，编号 (4.5) 在位。
  - 归一化推论 `μ^12_{x(r)} = μ^12_{x′(r)}.`（页图第 22 行、文本层第 47–48 行）——MD 第 506 行 `\mu_ {x (r)} ^ {1 2} = \mu_ {x ^ {\prime} (r)} ^ {1 2}.`，**右端下标 `x′(r)` 的撇与参数 `(r)` 均正确**，句点在位。
- 简化约定段核对（MD 第 481 行）：印刷「Write A′ and u(r) = I_k + rE_{12} ∈ U_{12} for r ∈ ℝ instead of A′_{12} and u_{12}(r). Also, we shall at times implicitly identify μ^12_x (which is a measure on U_{12}) with its push forward under the map u(r) ↦ r, e.g. write μ^12_x([a,b]) instead of μ^12_x(u([a,b])).」——**`I_k + rE_{12}` 的单位矩阵与下标 12、被替代的两个记号 `A′_{12}` 与 `u_{12}(r)`、以及 push-forward 后 `μ^12_x([a,b])` 与 `μ^12_x(u([a,b]))` 的对应关系全部正确**（此处若两侧写反会颠倒测度推前向的方向），逐句吻合。
- §4.2 首段与 Lemma 4.4(2) 收尾核对（MD 第 477、479 行）：`a.e. – a contradiction to our assumption` + QED 方块；`the two equivalent conditions in Proposition 4.3 fail (the first of which is precisely the condition of Theorem 2.3 (2))`；`From this we will deduce that μ is U_{ab}-invariant which is precisely the statement in Theorem 2.3 (1)` —— **定理编号 2.3 的两条分列 (2)/(1) 与印刷对应关系未颠倒**，逐句吻合。
- Ratner H-property 段核对（MD 第 509 行）：`is how the unipotent orbits x(r) and x′(r) diverge for r large (see Figure 2)`；`Ratner's H-property (which was introduced and used in her earlier works on rigidity of unipotent flows [38], [39] and was generalized by D. Morris-Witte in [29])`；`the general outline of our argument for the low entropy case is also quite similar to [38], [39]` —— **引文 `[38], [39]`、`[29]` 与 `D. Morris-Witte` 连字符均正确**，`[38, Lemma 2.1]`、`[39, Def. 1]`（MD 第 511 行）亦全对。
- 页边界核对：印刷 p.532 止于「…the following simple matrix calculation (cf. [38, Lemma 2.1] and [39, Def. 1]).」（页图末行、文本层第 59 行）；MD 第 511 行对应结束。MD 第 513 行起的 Figure 2 图片、图注与公式 (4.6) 属印刷 p.533 内容，留待 p.021 记录核对，本页无跨页错接。

## p.021（PDF p.21 / 印刷 p.533）
- PNG：/tmp/linden07_audit_p021.png（pngmono 150dpi）
- 核对：Figure 2 图本体与图注、`x'(r) = g(r)x(r)` 引导句、公式 (4.6) 全部九个矩阵元素、四个 `≠` 条件、`(4.7)` 最大值界（含两个范数项）、`(4.8)` 指数 `3/8`、`X_1 ⊂ X \ N` 与 Luzin 段、紧性极限段（`y' ∈ U_{(1)}y`、`μ_y^{12} = μ_{y'}^{12}`）、主难点段、`[20, §8]` / `[20, §8.1]` 引证、运行头
- 结果：PASS±（3 处已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 515 行，Figure 2 图注）：印刷「…noticably differ first only along U_{(1)}**.**」（页图第 5 行、文本层第 10 行）图注末有句点；MD 原件 `$U _ { ( 1 2 ) }$` 收尾无句点。已补 `.$`。
  2. **已修复**（MD 第 526 行，公式 (4.7) 末尾标点）：印刷 (4.7) 行末为**逗号**「…‖g_{*1}r‖) ≤ C**,**」（页图第 15 行、文本层第 25 行；因 (4.8) 紧随其后同属「there exists r with…」一句）；MD 原件误作句点 `\leq C.`。已改为 `C,`。**注**：该锚点字节含 `\tag`（`\t`）与相邻的 `\right`（`\r`），前一轮以 `\|\right)\leq C.\tag{4.7}` 定位时 Edit 无法命中（`\r` 被当作回车转义），改用不含 `\right` 的唯一锚点 `C.\tag{4.7}`（`grep -cF` 实测 = 1）完成，未改用脚本绕过。
  3. **已修复**（MD 第 535 行）：印刷「However, this contradicts Lemma 4.4 unless μ is invariant under U_{12}**.**」（页图第 19 行、文本层第 37 行）句末有句点；MD 原件缺失。已补 `.$`。
  4. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 533」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  5. 图片引用路径问题（打包层，非内容缺陷）：MD 第 513 行 `![](images/page_20_image_0.jpg)` 的相对路径同样无法从 MD 所在目录解析，实体位于 `…/Lindenstrauss_2007_littlewood_published_mineru/Lindenstrauss_2007_littlewood_published/images/page_20_image_0.jpg`。与 p.015 记录的同一 repo 级布局问题（已在该页登记并交由 canonical integrator 裁决），本页不重复处理、不改动。
  6. 行内紧排缺空格：第 517、523、533、535、537 行（如「be labelled as in (4.1). A simple calculation shows that」「is close to$\mathrm { I } _ { k }$in all entries」「belong to a fixed compact set$X _ { 1 } \subset X \setminus N$. Here N is as in Lemma 4.4 and」「The arguments can be simplified if one assumes」）。排版级，不改。
- 公式 (4.6) 逐元素核对（150dpi 页图第 8–12 行、文本层第 15–19 行；MD 第 520 行）——**九个矩阵元素逐一比对，全部吻合**：
  - 第 1 行：`a_1 + g_{21}r`｜`g_{12} + (a_2 − a_1)r − g_{21}r²`｜`g_{1*} + g_{2*}r`（**二次项 `g_{21}r²` 的指数 2 与负号正确**）
  - 第 2 行：`g_{21}`｜`a_2 − g_{21}r`｜`g_{2*}`
  - 第 3 行：`g_{*1}`｜`g_{*2} − g_{*1}r`｜`a_*`
  - 左端 `g(r) = u(r) g u(−r)` 的负参数 `−r` 正确；右端括号与句点、编号 (4.6) 均在位。**`u(r) g u(-r)` 的三个因子次序（u(r) 在左、u(−r) 在右）未被颠倒**。
- 公式 (4.7)/(4.8) 逐要素核对（页图第 15–16 行、文本层第 25–26 行；MD 第 526、530 行）：
  - 印刷 (4.7) `C^{-1} ≤ max(|(a_2 − a_1)r − g_{21}r²|, ‖g_{2*}r‖, ‖g_{*1}r‖) ≤ C,` 编号 (4.7) —— MD `\max\left(\left|(a_2-a_1)r-g_{21}r^2\right|,\|g_{2*}r\|,\|g_{*1}r\|\right)\leq C,\tag{4.7}`：**左侧 `C^{-1}` 的负指数、绝对值项内的二次项 `g_{21}r^2`、两个范数项 `‖g_{2*}r‖` 与 `‖g_{*1}r‖`（范数双竖线未被拍平成绝对值）、末项 `<= C` 与行末逗号、编号 (4.7) 全部吻合**。此式系数与范数最易失真，已逐字符核对。
  - 印刷 (4.8) `|g_{21}r| ≤ C δ^{3/8}.` 编号 (4.8) —— MD `|g_{21}r|\leq C\delta^{3/8}.\tag{4.8}`：**指数 `3/8`（分数幂）与常数 `C` 的乘积位置正确**，编号 (4.8) 与句点在位。
- 四个 `≠` 条件核对（MD 第 523 行）：印刷「one of the following holds; a_2 − a_1 ≠ 0, g_{21} ≠ 0, g_{*1} ≠ 0, or **g_{2*}** ≠ 0.」—— MD `a _ { 2 } - a _ { 1 } \neq 0 , g _ { 2 1 } \neq 0 , g _ { * 1 } \neq 0$, or$g _ { 2 * } \neq 0$`——**四项的顺序与下标（含 `g_{*1}` 的星号在左、`g_{2*}` 的星号在右）逐项吻合**，「或」项用 `or` 对应印刷逗号，未误并为并列条件。
- `X_1` 与极限段核对（MD 第 533、535 行）：印刷「With some care we will arrange it so that x(r), x′(r) belong to a fixed compact set X_1 ⊂ X \ N. Here N is as in Lemma 4.4 and X_1 satisfies that μ^12_z depends continuously on z ∈ X_1, which is possible by Luzin's theorem.」；「…two different points y, y′ ∈ X_1 with y′ ∈ U_{(1)}y…By continuity of μ^12_z on X_1 we get that μ^12_y = μ^12_{y′}.」—— **`X \ N` 的集差方向、`y' \in U_{(1)}y` 的轨道归属、连续性得出的 `μ^12_y = μ^12_{y'}` 等式两端下标均正确**。
- 引证核对（MD 第 539 行）：印刷「Our proof follows closely the methods of [20, §8]…see [20, §8.1] for more details.」——MD `the methods of [20, §8]`、`— see [20, §8.1] for more details` ——**两个节号 `§8` 与 `§8.1` 均正确**，破折号保留。
- 页边界核对：印刷 p.533 止于「…that μ satisfies the assump-」（页图末行、文本层第 46 行）；MD 第 541 行 §4.3 段承接 p.534 内容，属正常跨页合并，无错接，留待 p.022 核对。

## p.022（PDF p.22 / 印刷 p.534）
- PNG：/tmp/linden07_audit_p022.png（pngmono 150dpi）
- 核对：p.533 跨页续段（低熵假设、两个假设的前件/后件）、`X \ N ⊂ X′` 扩大 N 段（Lemma 4.2、`B_δ(z) \ B^L_δ(z)`）、`Construction of X_1` 段（`[5, p. 76]`、`ε⁴`）、`Construction of X_2` 段（`(10) in Section 2.1`、`[20, App. A]`、`C₁ε²`）、公式 (4.9)、`Construction of K = X_3` 段（`μ_x^{12}({0}) = 0`、`μ_x^{12}([−1,1]) = 1`、`ρ ∈ (0,1/2)`、`t = (1,−1,0,…,0)`、`C₂ε`）、公式 (4.10)、公式 (4.11) 两行、§4.4 标题与首段、运行头
- 结果：PASS±（1 处已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 545 行）：印刷「Construction of X₁. …and the property that μ^12_x depends continuously on x ∈ X₁**.**」（页图第 10–11 行、文本层第 17–18 行）行末有句点；MD 原件 `$X _ { 1 }$` 收尾无句点。已补 `.$`。
  2. MD 缺运行头「534 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  3. 词的合写：印刷 p.533 作「a **nullset** N」（单字，页图第 21 行、文本层第 5 行）；MD 第 541 行作「a null **set** N」。两种写法在文献中通用，语义不变，排版级，不改。
  4. 表述微调：MD 第 541 行在「By the former」后加逗号、「for small enough ε and any compact set」补 `for`；第 543 行「for every δ > 0 there exist z ∈ K」对应印刷的单数「there exists z ∈ K」（页图第 8 行、文本层第 12–13 行）。语义与量词不变，登记不改。
  5. 字形/字距伪影：MD 第 545 行 `$[ 5 , \mathrm { p } . 7 6 ]$`（引文号内插入空格、`p` 被数学化）。数字 **76** 正确，排版级，不改。
  6. 行内紧排缺空格：第 543、545、547、553、559 行（如「there exists a null set $N$ so that all statements」「The map$x \mapsto \mu _ { x } ^ { 1 2 }$is a measurable map」「To construct this set, we use the maximal inequality」「is assumed to be nontrivial a.e., we have」「has measure$\mu ( \mathcal { X } ( \rho ) ) > 1 - \varepsilon ^ { 2 }$」）。排版级，不改。
- 公式 (4.9) 逐要素核对（150dpi 页图第 14 行、文本层第 25–28 行；MD 第 550 行）：印刷 `∫_{[-R,R]} 1_{X_1}(u(r)x) dμ^12_x(r) ≥ (1 − ε²)μ^12_x([−R,R]).` 编号 (4.9)；MD `\int_ {[ - R, R ]} 1 _ {X _ {1}} (u (r) x) \mathrm{d} \mu_ {x} ^ {1 2} (r) \geq (1 - \varepsilon^ {2}) \mu_ {x} ^ {1 2} ([ - R, R ]).\tag{4.9}` ——**积分区间 `[-R,R]` 的两个 R 符号、示性函数下标 `X_1`、`u(r)x` 的参数 r、测度 `dμ^12_x(r)` 带自变量 (r)、系数 `(1 − ε²)` 的指数 2、右端 `μ^12_x([-R,R])`、编号 (4.9) 与句点全部吻合**。
- 公式 (4.10) 逐要素核对（页图第 16 行、文本层第 35–36 行；MD 第 556 行）：印刷 `𝒳(ρ) = {x ∈ X \ N : μ^12_x([−ρ,ρ]) < 1/2}` 编号 (4.10)；MD `\mathcal {X} (\rho) = \left\{x \in X \setminus N: \mu_ {x} ^ {1 2} ([ - \rho , \rho ]) < 1 / 2 \right\}\tag{4.10}` ——**阈值 `1/2`、底集 `x ∈ X \ N` 的集差方向、右端区间 `[-ρ,ρ]` 的 ρ 符号、编号 (4.10) 全部吻合**；印刷此处式末无标点（句子接「has measure μ(𝒳(ρ)) > 1 − ε²」），MD 亦无，一致。
- 公式 (4.11) 两行逐要素核对（页图第 18–19 行、文本层第 42–49 行；MD 第 562 行）：印刷
  `(1/T)∫_0^T 1_{X_2}(α^{−τt}x) dτ ≥ (1 − ε),`
  `(1/T)∫_0^T 1_{𝒳(ρ)}(α^{−τt}x) dτ ≥ (1 − ε).`
  MD `\frac {1}{T} \int_ {0} ^ {T} 1 _ {X _ {2}} (\alpha^ {- \tau \mathbf {t}} x) \mathrm{d} \tau \geq (1 - \varepsilon), \\ \frac {1}{T} \int_ {0} ^ {T} 1 _ {\mathcal {X} (\rho)} (\alpha^ {- \tau \mathbf {t}} x) \mathrm{d} \tau \geq (1 - \varepsilon). \end{array}\tag{4.11}`
  ——**两行的 `1/T` 归一因子、积分限 `0` 到 `T`、示性函数下标 `X_2` 与 `𝒳(ρ)`、`α^{−τt}` 的负指数与 τ 参数、不等号 `≥` 方向、右端 `(1 − ε)` 与首行逗号次行句点、编号 (4.11) 全部吻合**。
- `t` 向量方向复核（关键）：印刷 p.534 用 `t = (1, −1, 0, …, 0)`，而印刷 p.529 用 `t = (−1, 1, 0, …, 0)`（见本段 p.017 记录）。MD 第 559 行作 `\mathbf { t } = ( 1 , - 1 , 0 , \ldots , 0 )`——**与本页印刷一致，未与 p.529 的向量混同**；两处 MD 均正确。
- 引证与常数核对（MD 第 545、547 行）：`By Luzin's theorem [5, p. 76]`（**页码 76 正确**）；`we use the maximal inequality (10) in Section 2.1 from [20, App. A]`（**附录号 `App. A` 正确**）；`measure μ(X_1) > 1 − ε⁴`（**指数 4 正确**）；`measure μ(X_2) > 1 − C₁ε²`（**下标 1 与指数 2 正确**）；`measure μ(X_3) > 1 − C₂ε`（**下标 2、指数为 1 正确**）——逐项与印刷吻合。旧 Peer-P16 p.022 记录的「将 A′ 标签中的控制字符恢复为 prime，并修复 `[20, App. A]` 引文」两项修复**经本段复核确认已生效**。
- `B_δ(z) \ B^L_δ(z)` 核对（MD 第 543 行）：印刷「…z′ = α^s z ∈ B_δ(z) \ B^L_δ(z).」—— **`\ B^L_δ(z)` 的集差方向（从一般球扣掉 L-球，表示非例外返回）与上标 L 正确**，句点在位。
- 页边界核对：印刷 p.534 止于「…we can find z ∈ X_3 and α^s ∈ A′」（页图末行、文本层第 54 行）；MD 第 565 行对应结束。MD 第 568 行起的公式 (4.12) 与其后内容属印刷 p.535，留待 p.023 核对，无跨页错接。

## p.023（PDF p.23 / 印刷 p.535）
- PNG：/tmp/linden07_audit_p023.png（pngmono 150dpi）
- 核对：p.534 跨页续句与公式 (4.12)（`κ(z,z′)`、`max` 四项、区间 `(0, cδ^{1/2})`）、`c` 为绝对常数句、`r = κ(z,z′)^{−1}` 归一化段（`max = 1`、`C = 1`、`C = 10`、`r = 2κ^{−1}`、约数 2 与 4）、区间 I 与 Lemma 4.6 段（`t = (1,−1,0,…,0)`、`α^{−τt}`、`α^{−τt}gα^{τt}`）、Figure 3 图本体与图注、Lemma 4.5 陈述（`T = (1/4)|ln κ|`、`η ∈ {0,1}`、`θ ∈ [4T,6T]`、`1 − 9ε`）、两条 (1)(2) 与公式 (4.13)、`S = S(τ) = e^{θ−ητ}` 句、运行头
- 结果：PASS±（3 处已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 573 行）：印刷「For the moment let x = z, x′ = z′, and r = κ(z, z′)^{−1}**.** Obviously max(…) = 1.」（页图第 4–5 行、文本层第 7–8 行）在 `κ^{−1}` 后有句点；MD 原件作 `…^ { - 1 }$Obviously max…` 两句粘连。已补 `.$`。
  2. **已修复**（MD 第 581 行）：印刷 Lemma 4.5 陈述末「…such that for any τ ∈ P (τ ∈ P′)**,**」（页图第 17 行、文本层第 37 行，逗号后接分列 (1)）有逗号；MD 原件缺失。已补 `,$`。
  3. **已修复**（MD 第 591 行）：印刷「where S = S(τ) = e^{θ−ητ} (and similarly for μ^12_{x′})**.**」（页图第 22 行、文本层第 47–48 行）行末有句点；MD 原件缺失。已补 `.$`。
  4. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 535」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  5. 斜体强调丢失：印刷「since **a priori** this interval could have very small μ^12_x-measure」（页图第 11 行、文本层第 18 行）的 `a priori` 为斜体，MD 第 575 行作正体。语义不变，不改。
  6. 标点位置：MD 第 575 行作 `the$\alpha ^ { \mathbf { t } } .$-direction`，句点落在数学定界符内；印刷为 `the α^t-direction`（无内嵌句点）。渲染近乎相同，排版级，不改。
  7. 图片引用路径问题（打包层，非内容缺陷）：MD 第 577 行 `![](images/page_22_image_5.jpg)`（Figure 3）的相对路径同样无法从 MD 所在目录解析，实体在嵌套短名目录 `…/Lindenstrauss_2007_littlewood_published/images/page_22_image_5.jpg`。与 p.015 登记的同一 repo 级布局问题一致，本页不重复处理、不改动。
  8. 行内紧排缺空格：第 571、573、575、581、585、591 行（如「allowing us to change from the metric$d ( \cdot , \cdot )$to the norms」「For the moment let$x = z , \ x ^ { \prime } = z ^ { \prime } .$」「we want to use the conditional measure$\mu _ { x } ^ { 1 2 }$to find」「There exist subsets$P , P ^ { \prime } \subset [ 0 , T ]$of density at least」「satisfies the estimate」「where$S = S ( \tau ) = e ^ { \theta - \eta \tau }$(and similarly for」）。排版级，不改。
- 公式 (4.12) 逐要素核对（150dpi 页图第 3 行、文本层第 4 行；MD 第 568 行）：印刷 `κ(z, z′) = max(|a_2 − a_1|, |g_{21}|^{1/2}, ‖g_{*1}‖, ‖g_{2*}‖) ∈ (0, cδ^{1/2}),` 编号 (4.12)；MD `\kappa (z, z ^ {\prime}) = \max \bigl (| a _ {2} - a _ {1} |, | g _ {2 1} | ^ {1 / 2}, \| g _ {* 1} \|, \| g _ {2 *} \| \bigr) \in (0, c \delta^ {1 / 2}),\tag{4.12}` ——**四项的顺序与类型逐一吻合**（`a_2−a_1` 绝对值项、`g_{21}` 的 `^{1/2}` 分数幂、`g_{*1}` 范数项、`g_{2*}` 范数项；星号左右位置 `*1` 与 `2*` 未错位），右端区间 `(0, cδ^{1/2})` 的 `c` 与指数 `1/2`、行末逗号、编号 (4.12) 均在位。
- 归一化段核对（MD 第 573 行）：印刷「max(|(a_2 − a_1)r|, |g_{21}|^{1/2}r, ‖g_{2*}r‖, ‖g_{*1}r‖) = 1.」—— MD `\max$\left( | ( a _ { 2 } - a _ { 1 } ) r | , | g _ { 2 1} | ^ { 1 / 2} r , \lVert g _ { 2 *} r \rVert , \lVert g _ { * 1 } r \rVert \right) = 1$`：**四项与印刷同序**（`g_{21}^{1/2}r` 在前、`g_{2*}r` 与 `g_{*1}r` 两个范数项在后），**印刷的 `‖` 双线范数未被降格为绝对值**；`If the maximum is achieved in one of the last two expressions` 对应 `C = 1`，`if the maximum is achieved in either of the first two expressions` 对应 `r = 2κ^{−1}(z,z′)`、「(a_2−a_1)r is about 2 and g_21 r² is about 4」、`(4.7)–(4.8) hold with C = 10`——**`C = 10` 与两个约数 2、4 均正确**，逐句吻合。
- Lemma 4.6 段与 Figure 3 图注核对（MD 第 575、579 行）：印刷「To fix this, we use **t** = (1, −1, 0, …, 0) and the flow along the α^t-direction in Lemma 4.6. However, note that x = α^{−τt}z and x′ = α^{−τt}z′ differ by α^{−τt}gα^{τt}.」—— **`α^{−τt}` 与 `α^{τt}` 的正负指数方向、以及 `α^{−τt}gα^{τt}` 三因子次序均正确**；图注「Figure 3: The distance function κ(x, x′) might be constant for small τ and increase exponentially later.」与印刷逐字吻合、句点在位。
- Lemma 4.5 陈述逐要素核对（MD 第 581 行）：印刷「For z, z′ ∈ X_3 as above let **T = (1/4)|ln κ(z, z′)|**, **η ∈ {0, 1}**, and **θ ∈ [4T, 6T]**. There exist subsets **P, P′ ⊂ [0, T]** of density at least **1 − 9ε** such that for any τ ∈ P (τ ∈ P′),」——**分数 `1/4`、`η` 的取值集合 `{0,1}`、`θ` 的区间 `[4T, 6T]`（两个系数 4 与 6）、子区间 `[0,T]`、密度下界 `1 − 9ε`（系数 9 在前、ε 在后）全部吻合**。
- 公式 (4.13) 逐要素核对（页图第 20 行、文本层第 43–46 行；MD 第 588 行）：印刷 `μ^12_x([−ρS, ρS]) < (1/2)μ^12_x([−S, S])` 编号 (4.13)；MD `\mu_ {x} ^ {1 2} \big ([ - \rho S, \rho S ] \big) < \frac {1}{2} \mu_ {x} ^ {1 2} \big ([ - S, S ] \big)\tag{4.13}` ——**左端区间 `[−ρS, ρS]` 的 ρS、右端 `[−S, S]` 的 S、比例系数 `1/2`、不等号 `<` 方向、编号 (4.13) 全部吻合**；印刷式末无标点（句子接 `where S = …`），MD 亦无，一致。
- `S` 指数核对（MD 第 591 行）：印刷 `S = S(τ) = e^{θ−ητ}` —— **`θ − ητ` 的减号方向与 η 的乘子 τ 均正确**，指数未被写成 `θ−τη` 之类；「(and similarly for μ^12_{x′})」的下标 `x′` 带撇正确。
- 页边界核对：印刷 p.535 止于「where S = S(τ) = e^{θ−ητ} (and similarly for μ^12_{x′}).」（页图末行、文本层第 47–48 行）；MD 第 591 行对应结束。MD 第 593 行起的 Figure 4 图、图注与 Proof 属印刷 p.536，留待 p.024 核对，无跨页错接。

## p.024（PDF p.24 / 印刷 p.536）
- PNG：/tmp/linden07_audit_p024.png（pngmono 150dpi）；终裁：/tmp/l07_p024_cap.png、/tmp/l07_p024_cap2.png（Figure 4 图注末尾）、/tmp/l07_p024_calc.png（`A direct calculations` 段）——均为 300dpi 原页裁片，PIL 仅裁图
- 核对：Figure 4 图本体与图注、Lemma 4.5 的 Proof 前两段（`Q_1 ⊂ [0,T]`、`1−ε`、`Q_2 ⊂ [0,4T]`、`𝒳(ρ)`）、`Q_3` 定义式、`A direct calculations` 段（`1−8ε`、`v = (1/2)(θ+(2−η)τ)`）、`P = Q_1 ∩ Q_3` 段（`1−9ε`、`w = (1/2)(θ−ητ)`）、展示式 `y = α^{−wt}x = α^{−vt}z ∈ 𝒳_ρ`、(4.10) 导出的 `μ_y^{12}([−ρ,ρ]) < (1/2)μ_y^{12}([−1,1]) = 1/2`、比例式、`S = e^{2w} = e^{θ−ητ}` 句与 QED、下一引理引出段、运行头
- 结果：PASS±（2 处已修复；一处疑似缺句点经 300dpi 仲裁**排除**）
- 差异列表：
  1. **已修复**（MD 第 597 行）：印刷 Proof 首段末「…belongs to X₂ for every τ ∈ Q₁**.**」（页图第 9 行、文本层第 19 行）行末有句点；MD 原件缺失。已补 `.$`。
  2. **已修复**（MD 第 605 行）：印刷「…for τ ∈ Q₃ and v = (1/2)(θ + (2 − η)τ) we have y = α^{−vt}z ∈ 𝒳_ρ**.**」（页图第 12–13 行、文本层第 25–26 行）行末有句点；MD 原件缺失。已补 `.$`。
  3. MD 缺运行头「536 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  4. **300dpi 仲裁（关键，排除一处疑似缺陷）**：Figure 4 图注在 150dpi 下末尾 `𝒳_ρ` 后是否有句点难以判读，一般图注惯例应有。按 SOP 用 `-r300` 重渲同页并裁切放大（框 `(450,990,1500,1060)` 放大 2×，输出 /tmp/l07_p024_cap2.png）后目检：**印刷原图注末「(4.13) if $y = \alpha^{-wt}x \in \mathcal{X}_\rho$」确实没有句点**（同行右侧为空白）。据此判定 MD 第 595 行无句点是**忠实转录，不构成缺陷，不改 MD**。
  5. **print quirk 忠实保留**：印刷作「**A direct calculations shows** that Q₃ has density at least 1 − 8ε…」（页图第 12 行、文本层第 25 行，`calculations` 为复数，疑为印刷笔误）；MD 第 605 行同为 `A direct calculations shows`，**与印刷一致，按铁律三不擅改**。该判断有 300dpi 裁片 /tmp/l07_p024_calc.png 直接支持（字面清晰可读为 `calculations`）。
  6. 图片引用路径问题（打包层，非内容缺陷）：MD 第 593 行 `![](images/page_23_image_0.jpg)`（Figure 4）的相对路径同样无法从 MD 所在目录解析，实体在嵌套短名目录 `…/Lindenstrauss_2007_littlewood_published/images/page_23_image_0.jpg`。与 p.015 登记的同一 repo 级布局问题一致，本页不重复处理、不改动。
  7. 行内数学排版伪影：MD 第 605、607 行把行内公式包进 `\begin{array} { r } { … } \end{array}`（印刷为普通行内式）。渲染字形相同，排版级，不改。
  8. 行内紧排缺空格：第 597、599、605、607 行（如「there exists a set$Q _ { 1 } \subset [ 0 , T ]$of density at least」「has density at least$1 - 8 \varepsilon$in$[ 0 , T ]$, and for」「satisfies all assertions of the lemma; see Figure 4. First P has at least density」）。排版级，不改。
- `Q_3` 定义式逐要素核对（150dpi 页图第 10 行、文本层第 22–24 行；MD 第 602 行）：印刷 `Q_3 = {τ ∈ [0,T] : (1/2)(θ + (2 − η)τ) ∈ Q_2}.`；MD `Q _ {3} = \left\{\tau \in [ 0, T ]: \frac {1}{2} (\theta + (2 - \eta) \tau) \in Q _ {2} \right\}.` ——**分数 `1/2`、`θ + (2 − η)τ` 的括号与减号方向、`∈ Q_2` 的下标、句点全部吻合**。
- `v` / `w` 的定义核对（MD 第 605、607 行）：印刷 `v = (1/2)(θ + (2 − η)τ)` 与 `w = (1/2)(θ − ητ)`；MD `\frac { 1 } { 2 } ( \theta + ( 2 - \eta ) \tau )` 与 `\frac { 1 } { 2 } ( { \theta } - \eta \tau )` ——**两者都含 `−ητ`，差别只在 `v` 多一个常数项 `2`，MD 正确区分**（若把二者写成同一个会破坏 `e^{2w}` 与 `S = e^{θ−ητ}` 的推导），分数 `1/2` 均正确。
- 展示式 `y = α^{−wt}x = α^{−vt}z ∈ 𝒳_ρ` 核对（MD 第 610 行）：印刷同式 ——**两处 `α^{−·t}` 的负指数与参数（`w`、`v`）未被互换，尾端 `𝒳_ρ` 的花体 X 与下标 ρ 正确**；印刷式末无标点（句子接「by the last paragraph」），MD 亦无，一致。
- (4.10) 导出式核对（MD 第 616 行）：印刷 `μ^12_y([−ρ, ρ]) < (1/2) μ^12_y([−1, 1]) = 1/2.`；MD `\mu_ {y} ^ {1 2} ([ - \rho , \rho ]) < \frac {1}{2} \mu_ {y} ^ {1 2} ([ - 1, 1 ]) = \frac {1}{2}.` ——**左端区间 `[−ρ,ρ]`、系数 `1/2`、右端区间 `[−1,1]` 与末尾等式 `= 1/2` 的分数写法均正确**，句点在位。
- `S = e^{2w} = e^{θ−ητ}` 核对：印刷第 47 行「This implies (4.13) for **S = e^{2w} = e^{θ−ητ}**. The construction of P′ for z′ is similar.」—— **`e^{2w}` 的指数 2w 与 `e^{θ−ητ}` 的指数均正确**（前者是 w 的定义 `w = (1/2)(θ−ητ)` 代入后的结果），与 p.023 记录的 Lemma 4.5 中 `S = S(τ) = e^{θ−ητ}` 自洽。
- 引文与节号核对（MD 第 597、599、613 行）：`By the first line in (4.11)`、`By the second line in (4.11)`、`By (4.10)` —— **三个公式编号 (4.11)/(4.10) 均正确**，且「first/second line」的指代与印刷一致。
- 页边界核对：印刷 p.536 止于「…have all the desired properties.」（页图末行、文本层第 54 行）；MD 对应段落对应结束，Lemma 4.6 的陈述属印刷 p.537，留待 p.025 核对，无跨页错接。

### 本段溯源（git show 基线导出）

对 18 处修复逐处回查 `git show <rev>:"…__Lindenstrauss_2007_littlewood_published.md"`（`d351abbff` = MinerU 原始导出入库；`847882f32` = integrate harvest Peer-P16；`078d4ecb` = `cpf-redo/…^`，任务指定基线）：

**发现 1 处回归（非导出缺陷，系 `847882f32` 引入）—— p.021 / MD 第 526 行公式 (4.7) 末尾标点**

- 原导出 `d351abbff` 第 532 行的写法（把 (4.7)、(4.8) 合并在同一个 `array` 里）为
  `\begin{array}{c} C^{-1} \le \max(…|g_{21}|…) \le C**,** \\ |g_{21}r| \le C\delta^{3/8}. \end{array}\tag{4.8}`
  —— **(4.7) 行末是逗号 `C,`，与印刷 p.533 一致，原导出在此处正确**。
- `847882f32`（`integrate(audit): harvest Peer-P16 Lindenstrauss_2007_littlewood_published`，2026-10-02 10:14:16 -0400）把两条拆成独立编号展示式（`git log -S'tag{4.7}'` 实测：引入该串的提交只有 `847882f32` 一个）。拆分本身是**正确的修复**——印刷确实把 (4.7)、(4.8) 排成两个独立编号行；但在同一改动中**把 (4.7) 行末的逗号写成了句点**（该提交 diff：`+\dots\leq C.\tag{4.7}`）。
- 该提交同批还修好了 `diferent→different`、`dificulty→difficulty`、`\dot{\mu}→\mu`、句点补齐等，属净改善；**唯独 (4.7) 的末尾标点构成回归**。
- 本段已在 MD 第 526 行改回逗号（见 p.021 记录第 2 项）。**原导出正确，回归由 `847882f32` 引入。**

**其余 17 处均为 MinerU 原始导出既有缺口，非回归**

- 逐条以缺陷特征串做 `grep -cF` 双版本计数，p.387/p.395/p.403/p.427/p.429/p.437（含重复逗号与缺失句点两处）/p.445/p.451/p.459/p.515/p.535/p.545/p.573/p.581/p.591/p.597/p.605 在 `d351abbff` 与 `078d4ecb` 中计数一致（均存在）。
- p.459 的全角逗号另有一条佐证：全篇全角逗号计数 `d351abbff` = 3、`078d4ecb` = 2，说明其中一个已被前序 peer 正确清除；本段清除的另一个（MD 第 459 行）在两版本中**均存在**，属原始导出缺口而非回归。剩余 1 处全角逗号（MD 第 881 行，约印刷 p.540）不在本块范围，已在 p.019 记录中登记留给对应页块。

### 本段交付自检与边界

- 交付自检：`grep -c '^## p\.' AUDIT-Lindenstrauss_2007_littlewood_published.md` 实测输出 **`24`**，对应块 A（p.001–p.008）8 条 + 块 B（p.009–p.016）8 条 + 本段（p.017–p.024）8 条，无合并、无跳页。
- 本段分级汇总：**PASS± 8 页**（p.017–p.024），**PASS 0 页**，**FAIL 0 页**。逐页改动处数：p.017 = 3、p.018 = 4、p.019 = 2、p.020 = 0、p.021 = 3、p.022 = 1、p.023 = 3、p.024 = 2，合计 `edits=18`（其中 p.021 的 1 处为 peer 回归的纠正）。
- 300dpi 仲裁 4 次、全部排除疑似缺陷（均判定 MD 正确）：p.017 的 `‖g_{*2}‖`（印刷确为星号在左）、p.018 的闭球下标 `δ′`（印刷四处闭球均带撇）、p.019 的「a product measure」（印刷自身即无 `almost`）、p.024 的 Figure 4 图注（印刷末尾确无句点）。每次均以 `-r300` 重渲同页 + PIL 裁切（PIL 只裁图，未写 Markdown）。
- 写入范围与手段合规：18 处修改**全部**用 Edit 工具逐处定位，未用 Python/正则/sed/heredoc 或任何脚本写回 Markdown；未执行任何 git 写操作；未碰根 `AUDIT-INDEX.md`/`AUDIT-PROGRESS.log`/`MEMORY.md`/`README.md`；未写 `audit-redo/` 新图；未碰姊妹篇 `Lindenstrauss_2006_littlewood_exceptions*`；未启动或改动 mineru。
- Edit 定位限制如实登记：目标字节中的 `\r`（`\right`、`\rVert`、`\rangle`）与 `\t`（`\tag`、`\tau`）会被 Edit 的 `old_string` 当作 JSON 转义而无法命中，故这些位置改用**不含该类序列的唯一锚点**（如 `rangle$`、`C.\tag{4.7}`、`in P ^ { \prime } )$`、`^ { - 1 }$Obviously`），每处均先用 `grep -cF` 实测锚点计数为 1 再编辑；全程未改用脚本绕过。
- PDF 只读复核：本段收尾再次 `shasum -a 256` 实测 `Lindenstrauss_2007_littlewood_published.pdf` 仍为 `7f26dde3f9b206534584b2b94d4a86e6319e467918efca8b4d00b1b1ae574825`，与块 A 开工前一致，未被修改。

---

# 追加段：redo 块 D（PDF p.25–p.32，actor=`linden07`）

- 性质：同块 A/B/C，独立重做复核；每页重新渲染 PNG 目检 + `pdftotext` 文本层互证，唯一裁决源是印刷原页。
- 身份：actor=`linden07`；host=zcode Desktop；model=`opencode-go-chat/space-bunny-free`（本会话运行时自报）；effort=run 级配置未暴露，记 `UNKNOWN`。cwd=`/Users/aurolafly/.zcode/worktrees/cpf-redo-Lindenstrauss_2007_littlewood_published`；branch=`cpf-redo/Lindenstrauss_2007_littlewood_published`。
- 写入范围同前：只写本 AUDIT 文件与本篇 MinerU Markdown；未写根级真值文件、未写 `audit-redo/`、未执行 git 写操作、未碰姊妹篇、未碰 mineru。

## p.025（PDF p.25 / 印刷 p.537）
- PNG：/tmp/linden07_audit_p025.png（pngmono 150dpi）
- 核对：Lemma 4.6 陈述（`T = (1/4)|ln κ|`、`ε < 1/100`、`τ ∈ [0,T]`）、三条断言 (1)(2)(3)（含 `R′ = ρ^{−5}R`）、公式 (4.14) 两行（`x` 与 `x′` 两组条件测度）、`κ_a`/`κ_u` 定义式、公式 (4.15) 两个矩阵各九元素、公式 (4.16) 两行（`κ^{3/4}`、`cδ^{3/8}`）、Figure 3 引用句、四个子集 `P_a, P_u, P_a′, P_u′`、`Definition of P_a` 两段、`η = 0`、`θ = −log κ_a = 4T`、`S_a = κ_a^{−1}`、运行头
- 结果：PASS±（4 处已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 629 行）：印刷 Lemma 4.6 首句「If ε < 1/100**,** then there exists τ ∈ [0, T] such that」（页图第 2 行、文本层第 3–6 行）在 `1/100` 后有逗号；MD 原件作 `…{ 1 0 0 } }\end{array}$ then there exists…` 缺该逗号。已补 `,$`。
  2. **已修复**（MD 第 631 行）：印刷断言 (1)「…are in X₂**,**」（页图第 4 行、文本层第 8 行）行末有逗号；MD 原件缺失。已补 `,$`。
  3. **已修复**（MD 第 663 行）：印刷「Definition of P_a. …we set P_a = [0, T]**.**」（页图第 18 行、文本层第 48–49 行）行末有句点；MD 原件缺失。已补 `.$`。
  4. **已修复**（MD 第 665 行）：印刷「…and S_a = κ_a(z, z′)^{−1} = κ_a(x, x′)^{−1}**.**」（页图第 19–20 行、文本层第 52–53 行）行末有句点；MD 原件缺失。已补 `.$`。
  5. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 537」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  6. 字距伪影：MD 第 629 行 `I f`、`1 0 0`（`If` 与 `100` 被字距化并包进 `\begin{array}{r}{…}`）。数字 **100** 正确，排版级，不改。
  7. 行内数学伪影：MD 第 638 行公式 (4.14) 首行末的 `and` 被写成 `a n d`；第 665 行 `$\kappa ( z , z ^ { \prime } ) ~ = ~ \kappa _ { a } …$` 把印刷的等号写成 `~=~`（等价号伪影）。数学对象与关系正确，排版级，不改。
  8. 行内紧排缺空格：第 629、631、633、644、647、653、661、663、665 行（如「Let$z , z ^ { \prime } \in X _ { 3 }$and」「both$x = \alpha ^ { - \tau \mathbf { t } } z$and」「The corresponding quantities for$x , z ^ { \prime }$are defined similarly」「satisfies$x ^ { \prime } = \tilde { g } x$, and so」「define four subsets$P _ { a } , P _ { u } …$of density at least」「depend implicitly on$\tau )$we set」）。排版级，不改。
- 公式 (4.14) 两行逐要素核对（150dpi 页图第 7–10 行、文本层第 13–20 行；MD 第 638 行）：印刷
  `μ^12_x([−ρR, ρR]) < (1/2) μ^12_x([−R, R])  and`
  `μ^12_{x′}([−ρR, ρR]) < (1/2) μ^12_{x′}([−R, R]).`
  MD `\mu_ {x} ^ {1 2} \big ([ - \rho R, \rho R ] \big) < \frac {1}{2} \mu_ {x} ^ {1 2} \big ([ - R, R ] \big) a n d \\ \mu_ {x ^ {\prime}} ^ {1 2} \big ([ - \rho R, \rho R ] \big) < \frac {1}{2} \mu_ {x ^ {\prime}} ^ {1 2} \big ([ - R, R ] \big).\end{array}\tag{4.14}`
  ——**两行的中心化测度分别为 `μ^12_x` 与 `μ^12_{x′}`（下标 `x` 与带撇的 `x′` 未混同）、区间 `[−ρR, ρR]` 与 `[−R, R]`、系数 `1/2`、不等号 `<` 方向、编号 (4.14) 全部吻合**。断言 (3) 中 `R′ = ρ^{−5}R` 的**负指数 −5 正确**。
- 公式 (4.15) 两个矩阵逐元素核对（页图第 14–16 行、文本层第 27–30 行；MD 第 650 行）：印刷
  `g̃ = α^{−τt} (a_1 g_12 g_{1*}; g_21 a_2 g_{2*}; g_{*1} g_{*2} a_*) α^{τt} = (a_1  e^{−2τ}g_12  e^{−τ}g_{1*}; e^{2τ}g_21  a_2  e^τ g_{2*}; e^τ g_{*1}  e^{−τ}g_{*2}  a_*)`
  ——**左右两个矩阵各九元素逐一吻合；右矩阵六个指数 `−2τ、−τ、2τ、τ、τ、−τ` 的符号与 τ 因子全部正确**（这六个指数正是 `α^{−τt}gα^{τt}` 的对角共轭作用，若符号写反会使后续 `κ_u(x,x′) = e^τ κ_u(z,z′)` 失效），`α^{−τt}` 与 `α^{τt}` 的因子次序也正确，编号 (4.15) 在位。
- 公式 (4.16) 逐要素核对（页图第 17–18 行、文本层第 32–37 行；MD 第 656 行）：印刷 `κ_a(x,x′) = κ_a(z,z′), κ_u(x,x′) = e^τ κ_u(z,z′) ≤ κ(z,z′)^{3/4} < cδ^{3/8} and κ(x,x′) = max(κ_a(x,x′), κ_u(x,x′)) < cδ^{3/8};` —— **`e^τ` 的正指数、`κ(z,z′)^{3/4}` 的分数指数 3/4、两处 `cδ^{3/8}` 的指数 3/8、`max` 的两个参数次序、行末分号与编号 (4.16) 全部吻合**。
- `κ_a`/`κ_u` 定义式核对（MD 第 644 行）：印刷 `κ_a(z,z′) = |a_2 − a_1|, κ_u(z,z′) = max(|g_{21}|^{1/2}, ‖g_{*1}‖, ‖g_{2*}‖) ∈ (0, cδ^{1/2}).` ——**`|g_{21}|^{1/2}` 的分数幂与两个范数项 `‖g_{*1}‖`、`‖g_{2*}‖` 的星号左右位置（`*1` 与 `2*`）全部正确**，与 (4.12) 的定义保持一致；区间 `(0, cδ^{1/2})` 的指数 1/2 正确。
- `P_a` 段核对（MD 第 663、665 行）：印刷「If κ(x,x′) > κ_a(x,x′) for all τ ∈ [0,T] (recall that x, x′ depend implicitly on τ) we set P_a = [0,T].」；「Otherwise, it follows from (4.16) that κ(z,z′) = κ_a(z,z′). We apply Lemma 4.5 for **η = 0** and **θ = −log κ_a(z,z′) = 4T**, and see that (4.13) holds for τ ∈ P_a, where P_a ⊂ [0,T] has density at least **1 − 9ε**, and S_a = κ_a(z,z′)^{−1} = κ_a(x,x′)^{−1}.」——**`η = 0`、常数 `4T`、`1 − 9ε`、以及 `S_a` 的两处负指数逐项吻合**；`η = 0` 与下文 `P_u` 段的 `η = 1` 形成对照，两者未被混同。
- 四子集与密度段核对（MD 第 661 行）：印刷「define four subsets **P_a, P_u, P_a′, P_u′ ⊂ [0, T]**, each of density at least **1 − 9ε**, so that for every τ in the intersection of these four sets both (1) and (3) hold.」——**四个下标的组合顺序（无撇 a、无撇 u、撇 a、撇 u）与印刷完全一致**，密度下界 `1 − 9ε` 正确。
- 页边界核对：印刷 p.537 止于「We conclude that in」（页图末行、文本层第 58–59 行）；MD 第 665 行对应结束。MD 第 667 行起的 `P_u` 段续文与 `Clearly, since κ(x,x′) is either…` 属印刷 p.538，留待 p.026 核对，无跨页错接。

## p.026（PDF p.26 / 印刷 p.538）
- PNG：/tmp/linden07_audit_p026.png（pngmono 150dpi）；终裁：/tmp/l07_p026_eq2.png（300dpi 原页裁片，公式 (4.17)/(4.18) 编号，PIL 仅裁图）
- 核对：`P_u` 段续文（`S_u = κ_u(x,x′)^{−1} = e^{θ−τ}`）、`Clearly, since κ(x,x′) is either…` 段、`S = R = κ(x,x′)^{−1} = min(κ_a, κ_u)`、四个带撇子集句、`P_a∩P_a′∩P_u∩P_u′` 密度段（`1 − 36ε`）、括号附加说明段与 QED、§4.5 标题与首段、`μ_z^{12} = μ_{z′}^{12}` 与 `μ_x^{12} = μ_{x′}^{12}`、`P`/`P′` 定义式、密度段（`1 − ε²`、`[−ρR,ρR]`、`[−R,R]`）、`x(r) = u(r)x` 段、`g̃(r)` 矩阵、公式 (4.17) 与 (4.18) 的**编号对应**、证明引导句、运行头
- 结果：PASS±（**4 处已修复，其中公式编号错位属内容级缺陷**；其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复（内容级：公式编号错位，MD 第 698 行）**：印刷 (4.17) 为 `C^{-1} ≤ max(|(a_2−a_1)r − g̃_21 r²|, ‖g̃_{2*}r‖, ‖g̃_{*1}r‖) ≤ C,`，(4.18) 为 `|g̃_21 r| ≤ Cδ^{3/8}.`（150dpi 页图第 27–28 行 + 300dpi 终裁 /tmp/l07_p026_eq2.png 直证，两个编号清晰可辨）。MD 原件把 **最大值不等式那一式误标为 `\tag{4.18}`**，而真正的 (4.18) 式 `| \tilde{g}_21 r | \le C\delta^{3/8}.` **完全没有编号**——编号整体后移一位。已改为：第 698 行 `\tag{4.18}` → `\tag{4.17}`。
  2. **已修复（内容级：缺失编号，MD 第 702 行）**：紧接的 `| \tilde{g}_21 r | \le C\delta^{3/8}.` 已补上 `\tag{4.18}`。修复后 `grep -o 'tag{4\.1[6-9]}'` 实测输出为 `4.16/4.17/4.18/4.19 各 1 次`，编号连续且无重复无遗漏。
  3. **已修复**（MD 第 669 行）：印刷「…S = R = κ(x, x′)^{−1} = min(κ_a(x, x′), κ_u(x, x′))**.**」（页图第 5 行、文本层第 8–9 行）行末有句点；MD 原件缺失。已补 `.$`。
  4. **已修复**（MD 第 673 行）：印刷「…and (4.14) holds for R = κ(x, x′)^{−1}**.**」（页图第 7 行、文本层第 12–13 行）行末有句点；MD 原件缺失。已补 `.$`。
  5. MD 缺运行头「538 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  6. 编号标签冗余（排版级，登记不改）：MD 第 695 行把印刷左栏的 `(4.17)` 单独排成一行文本，其后的展示式又带 `\tag{4.17}`，渲染时 (4.17) 会出现两次。印刷原页的编号也位于左栏，故此冗余**不构成编号错误**，仅为 Markdown 无法精确还原左栏编号位置的结构性产物；为避免越权改动版式结构，本段只纠正编号本身（见第 1、2 项），保留该行并在后续块继续观察。
  7. 字形/字距伪影：第 669 行 `Lemma$4 . 5 ;$`、`\operatorname* { m i n }`；第 687、690 行 `\boldsymbol { r }`（把参数 `r` 加粗）；第 707 行 `constant$C ;$see Figure 2.`（句点落在数学定界符内）。数学对象正确，排版级，不改。
  8. 行内紧排缺空格：第 667、669、673、675、677、682、685、687、705、707 行（如「Let$\tilde { g }$be defined as in (4.15) and write」「has density at least$( 1 - \varepsilon ^ { 2 } )$with respect to」「there exists$r \in P \cap P ^ { \prime } \backslash \left[ - \rho R , \rho R \right]$」「For (4.18) we first recall that$| \tilde { g } _ { 2 1 } | \le …$」）。排版级，不改。
- 公式 (4.17)/(4.18) 逐要素核对（150dpi + 300dpi 双证）：印刷
  `(4.17)  C^{-1} ≤ max(|(a_2 − a_1)r − g̃_21 r²|, ‖g̃_{2*}r‖, ‖g̃_{*1}r‖) ≤ C,`
  `(4.18)  |g̃_21 r| ≤ Cδ^{3/8}.`
  MD 第 698 行 `C ^ {- 1} \leq \max (| (a _ {2} - a _ {1}) r - \tilde {g} _ {2 1} r ^ {2} |, \| \tilde {g} _ {2 *} r \|, \| \tilde {g} _ {* 1} r \|) \leq C,\tag{4.17}`、第 702 行 `| \tilde {g} _ {2 1} r | \leq C \delta^ {3 / 8}.\tag{4.18}` ——**除上述编号错位外，公式本体全部吻合**：`C^{-1}` 的负指数、绝对值项内的二次项 `g̃_21 r²`、两个**范数项** `‖g̃_{2*}r‖` 与 `‖g̃_{*1}r‖`（双竖线未被降格为绝对值）、`≤ C` 与行末逗号、`δ^{3/8}` 的分数指数、句点，全部与印刷一致。
- `g̃(r)` 矩阵逐元素核对（MD 第 690 行；页图第 21–23 行、文本层第 41–44 行）：印刷
  `g̃(r) = ( a_1 + g̃_21 r  g̃_12 + (a_2−a_1)r − g̃_21 r²  g̃_{1*} + g̃_{2*}r ; g̃_21  a_2 − g̃_21 r  g̃_{2*} ; g̃_{*1}  g̃_{*2} − g̃_{*1} r  a_* ).`
  ——**九个元素逐一吻合**，与 (4.6) 的 `g(r)` 同型但整体带波浪号，MD 的 `\tilde{g}` 标记在每个元素上均已保留（未漏标），行末句点在位。
- `P`/`P′` 与密度段核对（MD 第 682、685 行）：印刷 `P = {r ∈ [−R, R] : u(r)x ∈ X_1}`、`P′ = {r ∈ [−R, R] : u(r)x′ ∈ X_1}`；「P and P′ both have density at least **(1 − ε²)** with respect to the measure μ^12_x = μ^12_{x′}. By (4.14) we know that **[−ρR, ρR]** contains less than one half of the μ^12_x-mass of **[−R, R]**. Therefore, if ε is small enough there exists r ∈ P ∩ P′ \ [−ρR, ρR].」——**密度下界 `1 − ε²`、两个区间 `[−ρR,ρR]` 与 `[−R,R]`、`P ∩ P′ \ [−ρR,ρR]` 的集差方向、结论 `μ^12_{x(r)} = μ^12_{x′(r)} by property (3) in Section 2` 均与印刷吻合**；两条 `P`/`P′` 定义式右端的下标（`X_1`）未被误写成 `X_2`。
- `P_u` 续文与交叉段核对（MD 第 667、669 行）：印刷「…where P_u ⊂ [0, T] is a set of density **1 − 9ε** and S_u = κ_u(x, x′)^{−1} = **e^{θ−τ}**」；「Clearly, since κ(x,x′) is **either κ_u(x,x′) or κ_a(x,x′)** at least one of the sets P_a or P_u is constructed using Lemma 4.5; so in particular if τ ∈ P_a ∩ P_u then x ∈ X_2.」——**`e^{θ−τ}` 的指数减号方向、密度 `1 − 9ε`、「either … or …」二择一表述与 `κ_u`/`κ_a` 的先后次序均与印刷一致**。
- 四子集交集段核对（MD 第 673 行）：印刷「The set **P_a ∩ P_a′ ∩ P_u ∩ P_u′ ⊂ [0, T]** has density at least **(1 − 36ε)**…」——**四个集合的交集次序（a、a′、u、u′）与密度常数 36 全部吻合**（36 = 4×9，与上文四个 `1 − 9ε` 相容），`\ subset [ 0 , T ]` 的包含方向正确。
- §4.5 首段核对（MD 第 677 行）：印刷「we constructed x = α^{−τt}z, x′ = α^{−τt}z′ = **α^s ∈ X_2** using the properties of X_3 to ensure (4.14). Since **α^s acts isometrically on the U_{12}-leaves**, it follows from property (4) of the conditional measures in Section 2 that **μ_z^{12} = μ_{z′}^{12} and μ_x^{12} = μ_{x′}^{12}**.」——**`α^s`（上标 s，非 τ）这一等式的正确性、`U_{12}` 带上标 12、以及两组条件测度等式的下标（z/z′ 与 x/x′）全部吻合**。
- 页边界核对：印刷 p.538 止于「for some constant C; see Figure 2.」（页图末行、文本层第 51 行）；MD 第 705 行对应结束。MD 第 707 行起「We proceed to the proof of (4.17) and (4.18)…」、不等式链与公式 (4.19) 属印刷 p.539，留待 p.027 核对，无跨页错接。

## p.027（PDF p.27 / 印刷 p.539）
- PNG：/tmp/linden07_audit_p027.png（pngmono 150dpi）
- 核对：(4.18) 证明引导句与不等式链 `|g̃_21r| ≤ κ²R = κ ≤ κ^{3/4} ≤ (cδ^{1/2})^{3/4} ≤ c^{3/4}δ^{3/8}`、公式 (4.19) 四项最大界、`two differences` 段（含 `C = ρ^{−2}`）、公式 (4.20)、公式 (4.21)（`ρ²` 与 `ρ/2`）、`minor problem` 段与 `ρ²R^{−2}` 估计、公式 (4.22)、`ρ^{−5}R` / `ρ^{−4}R` 段与替代估计式、`ρ^{−6} − ρ^{−5} > 0` 下界式、almost cancellation 结论句、`δ = 1/n` 序列段与 `μ^12_{y_n} = μ^12_{y_n′}`、运行头
- 结果：PASS±（1 处已修复；本页其余差异为字形/排版/措辞级，不误导）
- 差异列表：
  1. **已修复**（MD 第 722 行，公式 (4.20) 末尾标点）：印刷「(4.20) max(|(a₂ − a₁)r|, |g̃_{21}|^{1/2}|r|) ≥ ρ**,**」（页图第 15 行、文本层第 14 行；因后半句「…occurs. We deduce a lower estimate…」继续该句）行末为**逗号**；MD 原件误作句点 `\geq\rho.`。已改为 `C,\tag{4.20}` 前的 `\geq\rho,`。
  2. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 539」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  3. 措辞微调（登记不改）：印刷「…might produce **a too small a number** (almost cancellation)」（页图第 11 行、文本层第 12 行）含冠词 `a`；MD 第 719 行作「might produce too small a number」，少一个冠词。语义不变、不误导，且该行已由前序 peer 重排为规范 LaTeX；本段不逐字回改措辞，只登记事实。
  4. 字距伪影：MD 第 729 行 `$( 4 . 2 1 )$`（公式号 (4.21) 被字距化为「4 . 2 1」）。**内容仍指向 (4.21)，指代正确**，排版级，不改。
  5. HTML 伪影：MD 第 729 行「lower estimate on |g˜<sub>21</sub>|」用 HTML 下标。渲染字形相同，排版级，不改。
  6. 破折号：印刷该段用 en-dash「the second term – this replaces…」（页图第 9–10 行、文本层第 10 行），MD 第 719 行作 em-dash `—`。语义不变，排版级，不改。
  7. 行内紧排缺空格：第 707、713、729、735、741、747、755、761 行（如「we ﬁrst recall that$| \tilde { g } _ { 2 1 } | \le …$」「Assume that for some$r \in [ - R , R ] \setminus …$this problem occurs」「only this time using the last statement in Lemma 4.6, and find$r \in …」「This shows that$| ( a _ { 2 } - a _ { 1 } ) r | \le \rho ^ { - 5 }$, and (4.22) shows that」「we have found two points$x _ { r } , x _ { r } ^ { \prime } \in X _ { 1 }$which satisfy」）。排版级，不改。
- 公式编号连号性核验（只读清点）：修复后 `grep -o 'tag{4\.\(1[5-9]\|2[0-2]\)}' | sort | uniq -c` 实测输出为 **(4.15) (4.16) (4.17) (4.18) (4.19) (4.20) (4.21) (4.22) 各 1 次**，连续、无重复、无缺号；其中 (4.17)/(4.18) 的编号对应系本段 p.026 记录修复的结果。
- 公式 (4.19) 逐要素核对（150dpi 页图第 5 行、文本层第 8 行；MD 第 716 行）：印刷 `ρ ≤ max(|(a_2 − a_1)r|, |g̃_{21}|^{1/2}|r|, ‖g̃_{2*}r‖, ‖g̃_{*1}r‖) ≤ 1.` 编号 (4.19)；MD `\rho \leq \max \bigl (\left| (a _ {2} - a _ {1}) r \right|, \left| \tilde {g} _ {2 1} \right| ^ {1 / 2} | r |, \| \tilde {g} _ {2 *} r \|, \| \tilde {g} _ {* 1} r \| \bigr) \leq 1.\tag{4.19}` ——**四项类型与次序逐项吻合**（`|(a_2−a_1)r|` 绝对值、`|g̃_21|^{1/2}|r|` 分数幂加 `|r|`、两个**范数项** `‖g̃_{2*}r‖` 与 `‖g̃_{*1}r‖`），**星号左右位置 `2*` 与 `*1` 未错位**（与 (4.17)/(4.12) 一致），左右界的 `ρ` 与 `1`、编号 (4.19) 全部正确。
- 公式 (4.20)/(4.21) 逐要素核对（页图第 15–16 行、文本层第 14–17 行；MD 第 722、726 行）：印刷
  `(4.20)  max(|(a_2 − a_1)r|, |g̃_{21}|^{1/2}|r|) ≥ ρ,`
  `(4.21)  |(a_2 − a_1)r − g̃_{21}r²| < ρ² < ρ/2.`
  ——**(4.20) 只含两项（与 (4.19) 的四项不同，此处不得混入范数项），不等号 `≥` 方向正确；MD 未误加范数项**；**(4.21) 中 `ρ²` 与 `ρ/2` 的两个幂/商写法正确**（正文「take the square of the second term – this replaces the lower bound ρ by its square」即解释 ρ² 的来源），编号 (4.20)/(4.21) 各自唯一。
- 不等式链与下界式核对（MD 第 710、744、750 行）：印刷 `|g̃_{21}r| ≤ κ(x,x′)² R = κ(x,x′) ≤ κ(z,z′)^{3/4} ≤ (cδ^{1/2})^{3/4} ≤ c^{3/4}δ^{3/8}.`；`|g̃_{21}r²| ≥ ρ²R^{−2}(ρ^{−4}R)² = ρ^{−6}.`；`|(a_2 − a_1)r − g̃_{21}r²| ≥ ρ^{−6} − ρ^{−5} > 0,` ——**三式中的幂次（`3/4`、`1/2`、`3/8`、`c^{3/4}`、`−2`、`−4`、`−6`、`−5`）与减号方向全部吻合**；最后一式 `ρ^{−6} − ρ^{−5}` 的**减号方向正确**（若写成加号会失去下界意义）。
- `ρ^{−5}R` / `ρ^{−4}R` 段核对（MD 第 735、738 行）：印刷「find r ∈ **[ρ^{−5}R, ρ^{−5}R] \ [ρ^{−4}R, ρ^{−4}R]**」—— **两端界都是 `ρ^{−5}R`（印刷如此，非笔误修正对象），MD 忠实保留**；随后的替代估计 `ρ^{−4} ≤ max(…) ≤ ρ^{−5}` 的左右界方向（**左 `ρ^{−4}`、右 `ρ^{−5}`，与区间方向一致**）正确，MD 吻合。
- `δ = 1/n` 与末式核对（MD 第 755、758 行）：印刷「for every **δ = 1/n > 0**, we get two sequences y_n and y_n′ of points in X_1 with the same conditional measures **μ^12_{y_n} = μ^12_{y_n′}**」—— **`1/n` 的倒数式正确**（写成 `n` 或 `1/n²` 都会错），末式两端下标 `y_n` 与带撇的 `y_n′` 正确，编号式后句点在位。
- 页边界核对：印刷 p.539 止于展示式 `μ^12_{y_n} = μ^12_{y_n′}.`（页图末行、文本层第 38–40 行）；MD 第 758 行对应结束。MD 第 761 行起的紧性段属印刷 p.540，留待 p.028 核对，无跨页错接。

## p.028（PDF p.28 / 印刷 p.540）
- PNG：/tmp/linden07_audit_p028.png（pngmono 150dpi）
- 核对：紧性与极限段（`y' ∈ Uy`、`y' ≠ y`、`μ^12_y = μ^12_{y′}`、`unless μ is invariant under U_{12}`）、§5 标题、`case (3) in Theorem 2.1` 开篇段、`H_{ab} ⊂ SL(k,ℝ)` 与 `A' = A ∩ C(H_{ab})` 段、`C(H_{ab})`-orbit 丰度段、Theorem 5.1 陈述（`supp ν ⊂ C(H_{ab})x`、`γ ∈ Γ`）、三条分列 (1)(2)(3)（`±1`、重数 two）、Proposition 5.2 陈述、`case (3) … cannot occur` 段、Proof of Proposition 5.2（特征多项式、首项与常数项为 1、Galois 共轭）、Lemma 5.3 起始句、运行头
- 结果：PASS±（5 处已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 761 行）：印刷「However, this contradicts Lemma 4.4, unless μ is invariant under U_{12}**.**」（页图第 4 行、文本层第 10 行）行末有句点；MD 原件缺失。已补 `.$`。
  2. **已修复**（MD 第 765 行）：印刷「As will be shown below, such is the case for Γ = SL(k, ℤ)**.**」（页图第 6 行、文本层第 16 行）行末有句点；MD 原件缺失。已补 `.$`。
  3. **已修复**（MD 第 771 行，Theorem 5.1 分列 (1) 末尾标点）：印刷「(1) **diagonalizable over ℝ,**」（页图第 10 行、文本层第 26 行）行末为**逗号**（后接分列 (2)）；MD 原件误作句点且把句点放进数学定界符内 `over$\mathbb { R } .$`。已改为 `over$\mathbb { R } ,$`。
  4. **已修复**（MD 第 773 行）：印刷「(2) ±1 is not an eigenvalue of γ**.**」（页图第 11 行、文本层第 27 行）行末有句点；MD 原件缺失。已补 `.$`。
  5. **已修复**（MD 第 781 行）：印刷「In particular, case (3) of Theorem 2.1 cannot occur for SL(k, ℝ)/SL(k, ℤ)**.**」（页图第 14 行、文本层第 36 行）行末有句点；MD 原件缺失。已补 `.$`。
  6. MD 缺运行头「540 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  7. 字距伪影：MD 第 773、775 行把英文单词 `of` 写成 `o f`（`eigenvalue$o f \gamma$`、`eigenvalues$o f \gamma$`）。词形与指代正确，排版级，不改。
  8. 行内紧排缺空格：第 761、765、769、779、783、787 行（如「with limits $y , y ^ { \prime } \in X _ { 1 }$. It follows from」「If case (3) in Theorem 2.1 holds, then this gives some restriction」「which is」「Suppose$\gamma\in\mathrm{SL}(k,\mathbb Z)$is diagonalizable」「There is a neighborhood$U _ { 0 }$of the identity」）。排版级，不改。
- Theorem 5.1 陈述与三条分列逐项核对（150dpi 页图第 9–13 行、文本层第 23–29 行；MD 第 769–775 行）：印刷
  `Theorem 5.1. Suppose that ν is an A′-invariant probability measure on X = SL(k,ℝ)/Γ, and that supp ν ⊂ C(H_{ab})x for some x ∈ X. Then there is a γ ∈ Γ which is`
  `(1) diagonalizable over ℝ,`
  `(2) ±1 is not an eigenvalue of γ.`
  `(3) All eigenvalues of γ are simple except precisely one which has multiplicity two.`
  ——**测度符号 `ν`（与全文的 `μ` 区分，印刷此处确为 ν）、支撑条件 `supp ν ⊂ C(H_{ab})x`、群元素 `γ ∈ Γ`、分列 (2) 的 `±1`（正负号并列、未丢负号）、分列 (3) 的「恰好一个重数为 two」四条条件逐项吻合**；`A′`（A 带撇）与 `H_{ab}` 的下标在 Theorem 5.1 与 §5 开篇段之间保持一致，MD 未混同。
- §5 开篇与 `A' = A ∩ C(H_{ab})` 段核对（MD 第 765、767 行）：印刷「We recall that H_{ab} ⊂ SL(k,ℝ) is an **A-normalized** subgroup isomorphic to SL(2,ℝ), and **A′ = A ∩ C(H_{ab})**. If case (3) of Theorem 2.1 holds then any A′-ergodic component of μ is supported on a single C(H_{ab})-orbit.」——**`A-normalized` 的连字符、`A′ = A ∩ C(H_{ab})` 的交集定义式、`SL(2,ℝ)` 的下标 2 均与印刷吻合**；`A′` 与 `A` 在此被正确区分（未把带撇群写成不带撇）。
- Proposition 5.2 与其证明核对（MD 第 779、783 行）：印刷「There is no γ ∈ SL(k,ℤ) satisfying the three conditions of Theorem 5.1.」；证明「Suppose γ ∈ SL(k,ℤ) is diagonalizable over ℝ. Then its eigenvalues (with the correct multiplicities) are roots of the characteristic polynomial of γ, a polynomial with **integer coefficients** and **both leading term and constant term equal to one**. If there is some eigenvalue which is not equal to ±1 and which occurs with multiplicity greater than one then necessarily this eigenvalue is not rational, and its **Galois conjugates** would also have multiplicity greater than one, **contradicting (3)**.」+ QED 方块 —— **「首项与常数项都等于 1」这一关键条件、`±1`、`contradicting (3)` 的指代、QED 方块全部在位**，与 Theorem 5.1 的三条分列衔接正确（否定 (3) 即得矛盾）。
- Lemma 5.3 起始句核对（MD 第 787 行前半）：印刷「There is a neighborhood **U_0** of the identity in **SL(m,ℝ)** so that for any **λ_1, λ_2, …, λ_m** with **|λ_i − λ_j| > 1** and h ∈ U_0 one has that …」—— **`U_0` 的下标 0、`SL(m,ℝ)` 的参数 m（下标与上标不可混写）、不等式 `> 1` 的方向、λ 的下标序列 1…m 全部吻合**；该句后半（`h diag(e^{λ_1},…,e^{λ_m})`）属印刷 p.541，留待 p.029 核对。
- 页边界核对：印刷 p.540 止于 Lemma 5.3 首句的「…and h ∈ U_0 one has that」（页图末两行、文本层第 48–49 行）；MD 第 787 行对应位置衔接正常，Lemma 5.3 的陈述与其证明属 p.541，留待 p.029 核对，无跨页错接。

## p.029（PDF p.29 / 印刷 p.541）
- PNG：/tmp/linden07_audit_p029.png（pngmono 150dpi）；终裁：/tmp/l07_p029_fpn3.png（300dpi 原页裁片，`‖f^{′n}‖ ≥ ‖f^{′n}e_1‖` 显示式，PIL 仅裁图）
- 核对：Lemma 5.3 陈述续句（`h diag(e^{λ_1},…,e^{λ_m})`、`e^{λ′_1},…,e^{λ′_m}`、`|λ′_i − λ_i| < 1/2`）、Proof 起段（`λ_1 > … > λ_m`、`f = diag(…)`、`f′ = hf`、`η_i`、`λ′_i = log|η_i|`）、`λ′_1 = lim_{n→∞} log‖f′^n‖/n` 段、`λ′_1 ≤ log‖h‖ + λ_1`、锥 `K` 与 `K′` 定义、`‖fx‖` 与 `‖f′x‖` 两式、`‖f^{′n}‖ ≥ ‖f^{′n}e_1‖` 式、`|λ′_1 − λ_1| < C_1δ`、楔积段 `f ∧ f` 与 `f′ ∧ f′`、`|λ′_1+λ′_2 − λ_1 − λ_2| < C_2δ`、公式 (5.1)（`Σ_{i=1}^k`）、`|λ′_i − λ_i| < Cδ` 收尾式与 QED、运行头
- 结果：PASS±（差异均为字形/排版级，不误导；**本页 MD 本段未修改**）
- 差异列表：
  1. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 541」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  2. **300dpi 仲裁（关键，排除一处疑似缺陷）**：显示式 `‖f^{′n}‖ ≥ ‖f^{?}e_1‖ ≥ ((1 − 2cδ)e^{λ_1})^n` 的中项 f 上是否带撇，在 150dpi 下撇号丢失、`pdftotext` 文本层也只给 `f  e_1`（见该层第 30–31 行），初看疑似 MD 第 818 行多加了撇（MD 为 `\left\| f ^ {\prime n} e _ {1} \right\|`）。按 SOP 用 `-r300` 重渲同页并裁切放大（框 `(650,1655,2050,1735)` 放大 3×，输出 /tmp/l07_p029_fpn3.png）后目检：**印刷原式为 `‖f^{′n}‖ ≥ ‖f^{′n}e_1‖ ≥ ((1 − 2cδ)e^{λ_1})^n.`，中项 f 确实带撇**。**MD 现值正确，疑点排除，不构成缺陷，不改 MD**；本条同时说明为何 SOP 要求公式判读以裁片为准——低分辨率与文本层在此处都会丢撇。
  3. 字形伪影：MD 第 787 行用 `\textit { h }`、`\textit { U } _ { 0 }`（把变量 h 与 U₀ 排成斜体）、`\mathrm { d i a g }`（diag 被字距化）；第 827 行 `\operatorname { l o g }`、`\operatorname* { l i m }`（log、lim 字距化）。数学对象与上下标正确，排版级，不改。
  4. 行内数学排版伪影：MD 第 787、791、827 行把行内公式包进 `\begin{array} { r } { … } \end{array}`（印刷为普通行内式）。渲染字形相同，排版级，不改。
  5. 行内紧排缺空格：第 789、791、797、803、809、821、827、839、845 行（如「Let $f=\operatorname{diag}(…)$, and let $\eta_1,\eta_2,\ldots$ be the eigenvalues」「Since$f$is self adjoint」「Let$\delta > 0$be small」「Then$f K \subset K ^ { \prime }$, and for every$x \in K$」「Suppose now that h is close enough to the identity」「for some c depending only on m. Suppose now that h」「Clearly, (5.1) implies that there is some $C$ depending only on $m$」「In particular, if$\lambda _ { i } > \lambda _ { i - 1 } + 1$for every i then if」）。排版级，不改。
- 公式逐要素核对（150dpi 页图 + 300dpi 终裁互证，**全部吻合**）：
  - `λ′_1 = lim_{n→∞} log‖f′^n‖/n`（页图第 5 行、文本层第 13–15 行；MD 第 791 行）—— **`lim` 的下标 `n → ∞`、被取对数的对象 `‖f^{′n}‖`、除数 `n` 全部正确**。
  - `λ′_1 ≤ log‖h‖ + λ_1.`（页图第 6 行、文本层第 16 行；MD 第 794 行）—— **`log‖h‖` 的自变量 h 与加项 `+λ_1`（而非 `+λ′_1`）正确**，句点在位。
  - `K′ = {(x_1,…,x_m) : |x_l| ≤ δe^{−1}|x_1| for every l ≠ 1}`（页图第 9 行、文本层第 19–21 行；MD 第 800 行）—— **`δe^{−1}` 的负指数（比 K 中的 `δ` 多一个 e^{−1} 收缩因子）、条件 `l ≠ 1`、两个 `x_1` 的下标全部正确**；`K` 中相应为 `δ|x_1|`，两者未被混同。
  - `‖fx‖ ≥ (1 − cδ)e^{λ_1}‖x‖,` 与 `‖f′x‖ ≥ (1 − 2cδ)e^{λ_1}‖x‖`（页图第 11、14 行；MD 第 806、812 行）—— **系数 `c` 与 `2c` 的区分、`(1 − …)` 的减号方向、`e^{λ_1}` 的指数 1 全部正确**；**第一式末尾印刷为逗号、第二式末尾无标点（句接「so that」），MD 两处的标点状态与印刷一致**。
  - `|λ′_1 + λ′_2 − λ_1 − λ_2| < C_2δ`（页图第 21 行、文本层第 45–46 行；MD 第 830 行）—— **四个加/减项的次序（λ′_1、λ′_2、λ_1、λ_2）与两个减号方向正确**；**该式末尾印刷无标点（句接「and more generally」），MD 亦无，一致**。
  - 公式 (5.1) `|Σ_{i=1}^k (λ′_i − λ_i)| < C_i δ.`（页图第 24 行、文本层第 49–54 行；MD 第 836 行）—— **求和下限 `i = 1`、**上限 `k`**（非 m）、被加项 `(λ′_i − λ_i)` 的撇与减号、右端常数 `C_i` 的**下标 i**（与前式的 `C_1`、`C_2` 同族但此处为 i）、编号 (5.1) 与行末句点全部吻合**。
  - `|λ′_i − λ_i| < Cδ  for all 1 ≤ i ≤ m.`（页图第 27 行、文本层第 58–59 行；MD 第 842 行）—— **全称条件 `1 ≤ i ≤ m` 的两端（此处回到 m，与 (5.1) 的上限 k 不同）正确**，MD 未把两处的指标上界混同。
- 楔积段核对（MD 第 827 行）：印刷「Similarly, **e^{λ_1+λ_2}** is the dominating eigenvalue of **f ∧ f**, i.e. the natural action of f on the space **ℝ^n ∧ ℝ^n**. Applying the same logic as before, **λ′_1 + λ′_2 = lim_{n→∞} log‖(f′ ∧ f′)^n‖/n**, and as long as h is in some fixed neighborhood of the identity, independently of f」—— **`e^{λ_1+λ_2}` 的指数和、楔积 `f ∧ f` 与 `f′ ∧ f′` 的撇、被取对数对象 `(f′∧f′)^n` 与除数 `n` 全部正确**。
- **print quirk 忠实保留**：上述楔积段印刷作「the space **ℝ^n ∧ ℝ^n**」（页图第 19 行、文本层第 38 行），而本段其余各处（Lemma 5.3 陈述、锥 K/K′、`SL(m,ℝ)`、收尾式 `1 ≤ i ≤ m`）一律用 **m**，唯此处作 **n**——疑为印刷笔误。MD 第 827 行同为 `$\mathbb { R } ^ { n } \wedge \mathbb { R } ^ { n }$`，**与印刷一致，按铁律三不擅改为 m**，并在此登记为 print quirk。
- 页边界核对：印刷 p.541 止于「…so that η_i = e^{λ′_i}」+ QED 方块（页图末两行、文本层第 56–59 行）；MD 第 845 行对应结束，Lemma 5.3 的证明已完整闭合，无跨页错接。

## p.030（PDF p.30 / 印刷 p.542）
- PNG：/tmp/linden07_audit_p030.png（pngmono 150dpi）
- 核对：Lemma 5.3 收尾段（`λ_i > λ_{i−1} + 1`、`Cδ < 1/2`、`η_i = e^{λ′_i}` + QED）、Proof of Theorem 5.1 起段（`a = 1, b = 2`、`a(t) = diag(e^{λ_1 t},…,e^{λ_k t}) ∈ A′`、`λ_1 = λ_2`、`λ_i ≠ λ_j`）、`U_0` 取法与 `U_1` 分块定义式（`e^{−2r/(k−2)}h`）、`t_0 = 2 max_{λ_i≠λ_j} |λ_i − λ_j|^{−1}`、Poincaré recurrence 段与 `U_1a(t) ∩ gΓg^{−1} ≠ ∅`、矩阵 `γ̃` 分块定义、`(5.2)`、公式 `f′ = he^{−2s/(k−2)} diag(e^{λ_3 t},…)`、特征值估计段（`3/4`、`1/8`）、`g^{−1}γ̃g ∈ Γ` 收尾与 QED、§6 标题与开篇段、运行头
- 结果：PASS±（2 处已修复；其中 1 处为 p.019 记录中跨块移交的全角逗号）
- 差异列表：
  1. **已修复**（MD 第 855 行）：印刷「and let t₀ = 2 max…|λ_i − λ_j|^{−1}. Note that U₁ is also symmetric, i.e. **U₁^{−1} = U₁.**」（页图第 11–12 行、文本层第 27–28 行）行末有句点；MD 原件缺失。已补 `.$`。
  2. **已修复**（MD 第 881 行，全角逗号，跨块移交项）：印刷「For every pair a, b of distinct indices in {1, …, k}**,** one of the three possibilities of Theorem 2.1 holds.」（页图第 26 行、文本层第 59–60 行）用 ASCII 逗号；MD 原件为全角 `，`（U+FF0C）。已改为 ASCII `,`。**该处正是本段 p.019 记录中登记并声明「不在本块范围、留给对应页块」的那一枚全角逗号**——其印刷位置经本次核对确属印刷 p.542（§6 开篇段），故在本页结清。修复后全篇全角逗号 `grep -c '，'` 实测输出为 **0**（原为 2，已由 p.019 清除 1、本段清除 1）。
  3. MD 缺运行头「542 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  4. 重音分解：MD 第 857 行 `Poincar´e recurrence`（U+00B4+e）。字形级，不改。
  5. 字距伪影：MD 第 855 行 `\operatorname* { m a x }`（max 字距化）。数学对象正确，排版级，不改。
  6. 行内紧排缺空格：第 847、849、855、857、863、875、877、881 行（如「Take$U _ { 0 }$to be a symmetric neighborhood」「and let$t _ { 0 } = 2 \operatorname* { m a x }…$」「there is a$t > t _ { 0 }$so that」「for every pair$i , j$except 1, 2 we have」「with$| \lambda _ { i } ^ { \prime } - \lambda _ { i } t | < 3 / 4$for$i =$」「In view of (5.2) it is clear that$\tilde { \gamma }$and hence」「we conclude the derivation of Theorem 1.3, and its corollary, Corollary 1.4, from Theorem 2.1」）。排版级，不改。
- `U_1` 分块定义式逐元素核对（150dpi 页图第 8–12 行、文本层第 17–22 行；MD 第 852 行）：印刷
  `U_1 = { ( e^r  0  0 ; 0  e^r  0 ; 0  0  e^{−2r/(k−2)}h ) : r ∈ (−1/8, 1/8) and h ∈ U_0 },`
  MD `U _ {1} = \left\{\left( \begin{array}{c c c} e ^ {r} & 0 & 0 \\ 0 & e ^ {r} & 0 \\ 0 & 0 & e ^ {- \frac {2 r}{k - 2}} h \end{array} \right): r \in (- 1 / 8, 1 / 8) \text {and} h \in U _ {0} \right\},` ——**九个矩阵元素、三分块结构（2×2 + 2 + k−2 维块）、右下角的分数指数 `e^{−2r/(k−2)}`（分子 `−2r`、分母 `k − 2`）、`r ∈ (−1/8, 1/8)` 的开区间两端与两个 `1/8`、以及 `h ∈ U_0` 的参数约束全部吻合**，行末逗号在位。
- `f′` 公式与参数对照核对（MD 第 872、875 行；页图第 17–18 行、文本层第 39–45 行）：印刷
  `f′ = he^{−2s/(k−2)} diag(e^{λ_3 t}, e^{λ_4 t}, …, e^{λ_k t})`
  `… of the form e^{λ′_3}, …, e^{λ′_k} with |λ′_i − λ_i t| < 3/4 for i = 3, …, k. Finally |s − λ_1 t| = |s − λ_2 t| ≤ 1/8`
  —— **`U_1` 定义式中的参数是 `r`（指数 −2**r**/(k−2)）而本式中的参数是 `s`（指数 −2**s**/(k−2)），二者是不同变量，MD 正确区分**（若混用会使 `|s − λ_1 t| ≤ 1/8` 的结论失去依据）；估计式中的 **`λ_i t` 带 t 因子**（非 `λ_i`）与常数 `3/4` 正确，`i = 3, …, k` 的起止正确，末式 `1/8` 正确。
- `(5.2)` 与 `t_0` 核对（MD 第 866、855 行；页图第 13、11 行、文本层第 37、27 行）：印刷 `|λ_i − λ_j| t > 2,`（编号 (5.2)，行末**逗号**）与 `t_0 = 2 max_{λ_i ≠ λ_j} |λ_i − λ_j|^{−1}` —— **常数 `2` 的位置（在 t 之后作乘子）、不等号 `>` 方向、`max` 的下标条件 `λ_i ≠ λ_j`、绝对值整体的 `^{−1}` 负指数全部吻合**，MD 第 866 行的行末逗号与印刷一致。
- `γ̃` 与交集段核对（MD 第 857、860、877 行）：印刷「for ν-almost every x = gΓ ∈ SL(k,ℝ)/Γ there is a t > t₀ so that a(t)x ∈ U₁x; so in particular **U₁a(t) ∩ gΓg^{−1} ≠ ∅**. Let **γ̃ = (e^s 0 0; 0 e^s 0; 0 0 f′) ∈ U₁a(t) ∩ gΓg^{−1}** be any element from this intersection.」；「γ̃ and hence **g^{−1}γ̃g ∈ Γ** satisfy all the conditions of Theorem 5.1.」—— **`gΓg^{−1}` 的负指数、三处交集中的同一写法、`γ̃` 的三分块结构（下块为 `f′` 带撇）、以及末段的 `g^{−1}γ̃g`（**先 conj 再左乘**，次序未颠倒）全部吻合**；测度符号 `ν`（承接 Theorem 5.1 的假设测度）与 `SL(k,ℝ)` 均正确。
- §6 开篇段核对（MD 第 881 行）：印刷「we conclude the derivation of **Theorem 1.3**, and its corollary, **Corollary 1.4**, from Theorem 2.1. Throughout this section, X will denote the quotient space **SL(k,ℝ)/SL(k,ℤ)**, and **μ** be an **A-ergodic and invariant** probability measure on X. For every pair a, b of distinct indices in {1, …, k}, one of the three possibilities of Theorem 2.1 holds. However, in view of the results of the previous section, in particular Theorem 5.1 and Proposition 5.2, **Theorem 2.1.(3)**, i.e. the case of exceptional returns, cannot occur for the lattice SL(k,ℤ).」—— **定理/推论编号 1.3、1.4、5.1、5.2 与分列 `2.1.(3)` 的编号链、「A-ergodic and invariant」的双重要求、商空间 `SL(k,ℝ)/SL(k,ℤ)` 的两处分母（此处为 SL(k,ℤ)，与前文 H_ab 情形的 Γ 区分）全部吻合**，指向 p.543 的续句衔接正常。
- 页边界核对：印刷 p.542 止于「…cannot occur for the lattice」（页图末行、文本层第 62–63 行）；MD 第 881 行对应结束，MD 第 883 行 `SL(k, Z). Therefore, for every pair a, b…` 起为 p.543 内容，留待 p.031 核对，无跨页错接。

## p.031（PDF p.31 / 印刷 p.543）
- PNG：/tmp/linden07_audit_p031.png（pngmono 150dpi）
- 核对：p.542 跨页续句（`SL(k, ℤ)`）、两个互斥可能 (1)(2)（含 `H_{ab} = ⟨U_{ab}, U_{ba}⟩`）、等价关系 `a ∼ b` 段（`U_{ac}`、`∼` 为等价关系、`r` 与 `k_i`）、`Σ_{i=1}^r k_i ≤ k`、`H = ∏_{i=1}^r SL(k_i,ℝ)`、`SL(n,ℝ)` 的三条性质、Ratner `[41]` 段与 `L > H` 记号约定、class A 定义段（`λ ∈ ℝ \ {±1}`）、Theorem 6.1 陈述（引文 `[27, Thms. (a) and (b)]`、`H̃` 与 `H`、`L ≥ H`）、脚注 3 全文、运行头
- 结果：PASS±（2 处已修复；其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 887 行）：印刷 (2) 条末「…left multiplication with elements of H_{ab} = ⟨U_{ab}, U_{ba}⟩**.**」（页图第 5–6 行、文本层第 9–11 行）行末有句点；MD 原件缺失。已补 `.$`。**`⟨U_{ab}, U_{ba}⟩` 的生成括号未被误改为普通圆括号**——MD 用 `\left. … \right.`（LaTeX 中即尖括号的 PDF 编码），与印刷的 ⟨ ⟩ 对应正确。
  2. **已修复（MD 第 889 行，丢词）**：印刷「…we can assume these equivalence classes are consecutive **indices** and H = ∏_{i=1}^r SL(k_i, ℝ)」（页图第 16–17 行、文本层第 20–22 行）在跨行断词 `in-` / `dices` 处合词为 **indices**；MD 原件作「…consecutive and $H = \prod…$」，**把单词 `indices` 整个丢失**（疑为前序 peer 重排 LaTeX 时连同断词一起删除）。已改回 `consecutive indices and`。
  3. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 543」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  4. 字形/字距伪影：MD 第 891 行 `$[ 2 7 ] ^ { 3 }$`（引文号 27 内插空格 + 脚注上标 3）、`$\mathbb { R } \setminus \{ \pm 1 \}$` 前的行内紧排；第 893 行 `H<sup>˜</sup>` 用 HTML 上标表示 H̃。编号与字形正确，排版级，不改。
  5. 行内紧排缺空格：第 889、891、893 行（如「Let $H$ be the group generated by all $U_{ab}$ with $a\sim b$」「the algebraic measures: $L$-invariant measures supported on a closed $L$-orbit for some$L > H$(here and throughout」「we shall say that$g \in G$in an element of class A」「Let G be a connected real Lie group,$\Gamma < G$a discrete subgroup」）。排版级，不改。
- 等价关系与 `H` 的构造核对（MD 第 889 行；页图第 8–16 行、文本层第 13–24 行）：印刷
  「Define a relation a ∼ b if μ is U_{ab}-invariant. By (2) above it follows that **a ∼ b if and only if b ∼ a**. Furthermore, since the group generated by U_{ab} and U_{bc} contains **U_{ac}**, it is clear that ∼ is in fact an equivalence relation on **{1, …, k}**. Let H be the group generated by all U_{ab} with a ∼ b. Let r denote the number of equivalence classes for ∼ which contain more than one element, and let k_1, k_2, …, k_r be their sizes; so in particular **Σ_{i=1}^r k_i ≤ k**. … and **H = ∏_{i=1}^r SL(k_i, ℝ)**. By definition, H leaves the measure μ invariant, is normalized by A, and is generated by unipotent one-parameter subgroups of SL(n, ℝ) — indeed, H is precisely the maximal subgroup of SL(n, ℝ) satisfying these three conditions.」
  ——**传递性所用的三个生成元 `U_{ab}`、`U_{bc}`、`U_{ac}` 的下标链、指标集 `{1,…,k}`、不等式 `Σ k_i ≤ k`（≤ 号，非 <）、直积 `∏_{i=1}^r SL(k_i,ℝ)` 的上下限与因子、两条 `SL(n,ℝ)`（此处用 n 而非 k，印刷如此）全部吻合**；`H` 的三条性质（leaves μ invariant / normalized by A / generated by unipotent one-parameter subgroups）逐条在位。
- `L > H` 记号约定段核对（MD 第 891 行；页图第 17–19 行、文本层第 30–33 行）：印刷「the algebraic measures: **L-invariant measures supported on a closed L-orbit for some L > H** (here and throughout, we use the notation **L > H** to denote that H is a subgroup and **L ⊃ H**; specifically H may be equal to L)」（`L ⊃ H` 为**真包含号 ⊃**）。MD `for some$L > H$(here and throughout, we use the notation$L > H$to denote that H is a subgroup and$L \supset H ;$ specifically H may be equal to$L )$` ——**「`>` 表示 ⊃（可相等）」这一关键记号约定及其括注完整保留**（`L ⊃ H` 与 `L > H` 被正确区分，未混为严格包含），逐句吻合。
- class A 定义段核对（MD 第 891 行；页图第 19–20 行、文本层第 36–39 行）：印刷「we shall say that **g ∈ G** in an element of **class A** if **Ad g is semisimple**, with all eigenvalues **integer powers of some λ ∈ ℝ \ {±1}**, and **g is contained in a maximal reductive subgroup of G**」—— **`λ ∈ ℝ \ {±1}` 的集合差与 `±1`（正负号并列）未被误写为 `\{1\}` 或 `\{±1\}`，"integer powers"（整数次幂）这一限定未被简化为 "powers"，三条定义条件逐条在位**。
- Theorem 6.1 陈述逐要素核对（MD 第 893 行；页图第 22–26 行、文本层第 41–46 行）：印刷
  `Theorem 6.1 ([27, Thms. (a) and (b)]). Let G be a connected real Lie group, Γ < G a discrete subgroup, and H̃ generated by unipotent one-parameter groups and elements of class A, with H < H̃ the subgroup generated by unipotent one-parameter groups. Let μ be an H̃-invariant and ergodic probability measure on G/Γ. Then there is an L ≥ H so that almost every H-ergodic component of μ is the L-invariant probability measure on a closed L-orbit.`
  ——**引文 `[27, Thms. (a) and (b)]` 的两条子定理编号、`H̃`（带波浪号的大群）与 `H`（由幺幂一参数群生成的子群）的大小写/波浪号区分、包含关系 `H < H̃`（严格小于）— 这一点与结论处的 `L ≥ H`（大于等于）是两个不同的关系符，MD 未混同**、结论「almost every **H-ergodic** component」的遍历性限定、以及 `L-invariant probability measure on a closed L-orbit` 的三个要素，逐项吻合。
- 脚注 3 核对（MD 第 895 行）：印刷（页图末段、文本层第 49–51 行）「The main theorem of [27] was substantially more general than what we quote here. In particular, in their theorem Γ can be **any closed subgroup** of G, and the group G can be a **product of real and p-adic Lie groups** (satisfying some mild additional conditions).」—— **`p`-adic 的连字符、上标标记 `³` 与 `<sup>3</sup>` 对位、以及"任意闭子群"与"实/p 进乘积"两项放宽条件逐句吻合**。
- 页边界核对：印刷 p.543 止于脚注 3 末句「…(satisfying some mild additional conditions).」（页图末行、文本层第 51–52 行）；MD 第 895 行对应结束。MD 第 897 行起的 `Furthermore, if S_N^G(L)=…` 与 Lemma 6.2 属印刷 p.544，留待 p.032 核对，无跨页错接。

## p.032（PDF p.32 / 印刷 p.544）
- PNG：/tmp/linden07_audit_p032.png（pngmono 150dpi）
- 核对：Theorem 6.1 的 `Furthermore, if` 补充段（`S_N^G(L)` 定义式、`conjunction by g preserves Haar measure`、`H̃ < S_N^G(L)`）、Lemma 6.2 陈述（`H = ∏_{i=1}^r SL(k_i,ℝ)`、`Σ_{i=1}^r k_i < k`、`X_H` 定义、`a(t)x → ∞`）、Proof 首段（`k′ = Σ_i k_i < k`、`Λ = g^{−1}Hg ∩ Γ`、`h_0 = diag(h′_0, I_{k−k′})`）、公式 (6.1)、`dim V_g = k − k′` 段与 `(V_g)^⊥`、`m ∈ ℤⁿ ∩ (V_g)^⊥`、`k′t` 与 `(k′−k)t`、`a(t)(gm) → 0`、Mahler 判别法收尾与 QED、Proof of Theorem 1.3 全段（`H̃ = AH`、`L > H`、`L < AH`、`Λ_L`/`Λ_H`、`[g^{−1}Lg, g^{−1}Lg]`、`H = L`）、运行头
- 结果：PASS±（4 处已修复；其中含 1 处数学括号闭合缺陷与 1 处 QED 标记缺失，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复（MD 第 915 行，数学括号未闭合）**：印刷「…it is clear that V_g is a rational subspace of **ℝⁿ (i.e. has a basis consisting of rational vectors)**.」（页图第 20 行、文本层第 27–28 行）；MD 原件作 `$\mathbb { R } ^ { n } { \mathrm { ~ ( i . e ~ } } . has a basis consisting of rational vectors)$`——**`i.e.` 的右圆括号缺失、被一个句点顶替**，渲染出「(i.e . has a basis…」这样永不闭合的括号。已改为 `} }$) has a basis`。
  2. **已修复**（MD 第 915 行，同段）：印刷「Since V_g is rational, there is an integer vector **m ∈ ℤⁿ ∩ (V_g)^⊥.** In particular, the last k − k′ entries…」（页图第 20–21 行、文本层第 28–29 行）在 `(V_g)^⊥` 后有句点；MD 原件作 `…( V _ { g } ) ^ { \perp }$ In particular…` 两句粘连。已补 `$.`。
  3. **已修复**（MD 第 921 行，标点 + 缺失 QED 标记）：印刷「so that by Mahler’s criterion **a(t)x = a(t)g SL(k, ℤ) → ∞.**」+ 行末 **□**（页图第 24–25 行、文本层第 34 行）；MD 原件作 `…\to \infty ,$`——**句点误作逗号，且整枚 QED 方块缺失**（这是 Lemma 6.2 证明的证毕标记）。已改为 `\to \infty $.□`。
  4. **已修复**（MD 第 925 行）：印刷「…Hx is closed with finite volume. However, this implies **H = L.**」（页图末行、文本层第 47 行）行末有句点；MD 原件缺失。已补 `.$`。
  5. MD 缺运行头「544 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  6. **print quirk 忠实保留（两处）**：① `S_N^G(L) = {g ∈ N_G(L) : **conjunction** by g preserves Haar measure on L}`（页图第 3–4 行、文本层第 5 行，`conjunction` 系 conjugation 之误拼，印刷自身如此），MD 第 899 行同为 `conjunction`，**与印刷一致，不改**；② Proof of Theorem 1.3 中印刷作「Therefore, the same is true for the semi-simple g^{−1}Hg = [g^{−1}Lg, g^{−1}Lg]**,** Λ_H = … is a lattice in …」——逗号后直接接新主语、印刷本身即是一个 run-on 句，MD 第 925 行忠实保留该逗号，**不擅改句法**。
  7. 字形伪影：MD 第 925 行 `\mathrm { S L } ( \boldsymbol { k } , \mathbb { Z } )` 把 `SL(k, ℤ)` 内的 `k` 误加粗（印刷该处 `k` 为正体），另 `\boldsymbol { x }`。渲染字形相近，排版级，不改。
  8. 字距伪影：MD 第 915 行 `\mathrm { ~ ( i . e ~ } }`（i.e. 字距化）。排版级，不改。
  9. 行内紧排缺空格：第 913、915、921、925 行（如「Notice that since$g ( g ^ { - 1 } h _ { 0 } g ) = h _ { 0 } g$(the transpose of)」「Clearly dim$V _ { g } = k - k ^ { \prime }$, and using」「so that by Mahler’s criterion$a ( t ) x = …」「Proof of Theorem 1.3. Let$…$be the maximal group fixing$\mu ,$generated by」）。排版级，不改。
- `S_N^G(L)` 与 Lemma 6.2 陈述核对（MD 第 899、901、903 行；页图第 3–9 行、文本层第 4–10 行）：印刷
  `S_N^G(L) = {g ∈ N_G(L) : conjunction by g preserves Haar measure on L}`，`then H̃ < S_N^G(L) and μ is supported on a single S_N^G(L)-orbit. In particular, L is normalized by H̃.`
  `Lemma 6.2. Let H = ∏_{i=1}^r SL(k_i, ℝ) with **Σ_{i=1}^r k_i < k**. Let X_H = {x ∈ X : Hx is closed and of finite volume}. Then there is a one-parameter subgroup a(t) of A so that for every x ∈ X_H its trajectory a(t)x → ∞ as t → ∞.`
  —— **记号 `S_N^G` 的上标 G 与下标 N、`N_G(L)` 的下标 G、直积 `∏_{i=1}^r SL(k_i,ℝ)` 的上下限、`X_H` 的下标 H、以及不等式 `Σ k_i < k`（**本引理用严格小于 `<`，与 p.543 的 `Σ k_i ≤ k` 用 `≤` 不同——两处是不同情形的条件，MD 两处分别正确保留，未混同**）全部吻合**；结论的极限表述 `a(t)x → ∞ as t → ∞` 两个极限方向亦正确。
- `h_0` 块对角与公式 (6.1) 核对（MD 第 907、910 行；页图第 12–15 行、文本层第 16–22 行）：印刷「Let **k′ = Σ_i k_i < k**. Let **Λ = g^{−1}Hg ∩ Γ**. Since Λ is Zariski dense in g^{−1}Hg there is a **γ = g^{−1}h_0 g ∈ Λ** with **h_0 = (h′_0  0 ; 0  I_{k−k′})**」；`(6.1) V_g := {y ∈ ℝ^k : y^T g^{−1}hg = y^T for all h ∈ H} = {y ∈ ℝ^k : y^T γ = y^T}.`
  —— **`h_0` 的块对角结构（上块 `h′_0` 为 `k′×k′`、下块 `I_{k−k′}`，两块的维数互补且下标 `k−k′` 正确）未被误写为标量矩阵或整体单位阵**；`k′` 的撇号、`Λ` 的定义式与 `γ` 的共轭式 `g^{−1}h_0 g`（先右乘 `g`）、以及 (6.1) 中两个集合的等价（左侧对全体 `h ∈ H` 的条件、右侧对单个 `γ` 的条件）与转置 `y^T` 全部吻合。旧 Peer-P16 p.032 记录的「恢复 `S_N^G(L)` 记号及 `h_0=diag(h′_0,I_{k−k′})` 块对角矩阵」**经本段复核确认已生效且正确**。
- `dim V_g`、`m` 向量与 `t` 的构造核对（MD 第 913、915、918 行；页图第 16–24 行、文本层第 24–33 行）：印刷「since **g(g^{−1}h_0g) = h_0g** (the transpose of) the last **k − k′** rows of g are in V_g.」；「Clearly **dim V_g = k − k′**, and…V_g is a rational subspace of **ℝⁿ** (i.e. has a basis consisting of rational vectors). Since V_g is rational, there is an integer vector **m ∈ ℤⁿ ∩ (V_g)^⊥**. In particular, the last **k − k′** entries in the vector **gm** … are zero. For any t ∈ ℝ set **t = (t_1,…,t_k)** with **t_1 = ⋯ = t_{k′} = k′t** and **t_{k′+1} = ⋯ = t_k = (k′ − k)t** and **a(t) = α^t**.」；「**a(t)(gm) → 0  as t → ∞,**」
  —— **等式 `g(g^{−1}h_0g) = h_0g` 的三个因子、`k − k′` 与 `k′ − k` 两处维数表达（符号相反，未混同）、`t_{k′}` 与 `t_{k′+1}` 的下标分界、`ℤⁿ ∩ (V_g)^⊥` 的正交记号、以及 `(k′ − k)t` 的负号方向全部吻合**；本段两处 `ℝⁿ`（此处的 n）与 `ℝ^k`（集合与向量所在空间）按印刷区分，MD 未混同。
- Proof of Theorem 1.3 逐要素核对（MD 第 925 行；页图第 26–35 行、文本层第 37–47 行）：印刷「Let H = ∏_{i=1}^r SL(k_i,ℝ) be the maximal group **fixing μ**, generated by unipotent one-parameter subgroups, and normalized by A as above. By Theorem 6.1, applied to μ with **H̃ = AH**, we know that there is some **L > H** which is normalized by A so that almost every **H-ergodic** component of μ is the L-invariant measure on a closed **L orbit**. In particular μ is L-invariant, which unless **L < AH** contradicts the definition of H as the maximal group with the above properties. Let now x = g SL(k,ℤ) have a closed **L-orbit Lx** of finite volume. Then **Λ_L = g^{−1}Lg ∩ SL(k,ℤ)** is a lattice in g^{−1}Lg, and so the latter is defined over **Q**. Therefore, the same is true for the semi-simple **g^{−1}Hg = [g^{−1}Lg, g^{−1}Lg]**, **Λ_H = g^{−1}Hg ∩ SL(k,ℤ)** is a lattice in g^{−1}Hg, and Hx is closed with finite volume. However, this implies H = L.」
  —— **`H̃ = AH`（把 A 并入 H̃）、`L > H`（Theorem 6.1 结论中的 ≥，此处按定理表述写 >）、`L < AH`（反证假设，符号与前一处的 `>` 相反，MD 未混同）、两个格的交换子 `[g^{−1}Lg, g^{−1}Lg]` 的两个因子、`Λ_L` 与 `Λ_H` 的下标对应、`Q` 与 `Q` 的斜体、`L orbit`（此处印刷无连字符）与 `L-orbit Lx`（此处印刷有连字符）——两处写法不同，MD 分别忠实保留**。
- 页边界核对：印刷 p.544 止于「However, this implies H = L.」（页图末行、文本层第 47 行）；MD 第 925 行对应结束。MD 第 927 行起的「Thus we conclude that almost every H-ergodic component…」属印刷 p.545，留待 p.033 核对，无跨页错接。

### 本段溯源（git show 基线导出）

对 21 处修复逐处回查 `git show <rev>:"…__Lindenstrauss_2007_littlewood_published.md"`（`d351abbff` = MinerU 原始导出入库；`847882f32` = integrate harvest Peer-P16；`078d4ecb` = `cpf-redo/…^`，任务指定基线）。**发现 2 处回归（非导出缺陷，系 `847882f32` 引入）**：

**回归 1 — p.027 / MD 第 722 行，公式 (4.20) 末尾标点（逗号 → 句点）**
- 原导出 `d351abbff` 第 728 行的该式为 `…\geq \rho **,**\tag{4.21}`——**逗号与印刷一致，原导出在标点这一点上正确**（但其编号 `4.21` 本身是错的，见下）。
- `847882f32` 把该式改为 `\max(…)\geq\rho**.\**\tag{4.20}`：编号由错的 (4.21) 改成正确的 (4.20)（**这一步是正确的修复**，印刷 p.539 确为 (4.20)），但同时**把行末的逗号写成了句点**。
- 已改回逗号。**原导出正确（标点层面），回归由 `847882f32` 引入。**

**回归 2 — p.031 / MD 第 889 行，丢词 `indices`**
- 原导出 `d351abbff` 第 895 行为「…these equivalence classes are consecutive **indices** and `H = ∏…`」——**与印刷一致，原导出正确**。
- `847882f32` 重排该段 LaTeX 时**把单词 `indices` 整个删除**，变成「consecutive and `H = …`」。
- 已改回 `consecutive indices and`。**原导出正确，回归由 `847882f32` 引入。**

**其余 19 处均为 MinerU 原始导出既有缺口，非回归**

- 逐条以缺陷特征串做 `grep -cF` 双版本计数，以下各处特征串在 `d351abbff` 与 `078d4ecb` 中计数一致（均存在）：p.629、p.631、p.663、p.665、p.669、p.673、p.722 的逗号、p.761、p.765、p.771、p.773、p.781、p.855、p.881、p.887、p.915（i.e 括号与句点两处）、p.921、p.925。
- 其中三条另作精确复核：p.669 行尾在两版本中**逐字节相同**（均为 `…\kappa _ { u } ( x , x ^ { \prime } ) )$`，均缺句点）；p.887 的 `…elements of$H _ { a b } = \left. U _ { a b } , U _ { b a } \right.$` 在原导出第 893 行与基线第 887 行**逐字节相同**（均缺句点）；p.881 的全角逗号计数 `orig = 3 / base = 2`，说明前序 peer 已正确清除 1 枚、其余 2 枚（本块之前分别在 p.019 与 p.030 结清）**在两版本中均存在**，属原始缺口而非回归。
- p.698 / p.702 的**编号**部分需要单独说明：原导出 `d351abbff` 第 702、706 行**对 (4.17) 与 (4.18) 两个展示式都没有加任何 `\tag`**（`C^{-1} \leq \max(…)` 与 `|g̃_21 r| \leq Cδ^{3/8}` 均为无编号式），编号由 `847882f32` 补齐为 `\tag{4.17}` / `\tag{4.18}`，**这是正确的修复**；本段在 p.026 把错位的 `\tag{4.18}` 改回 (4.17)、在 p.027 补上缺失的 `\tag{4.18}`，属于对前序修复成果的承接与补全，非新引入的回归。

### 本段交付自检与边界

- 交付自检：`grep -c '^## p\.' AUDIT-Lindenstrauss_2007_littlewood_published.md` 实测输出应为 **`32`**，对应块 A（p.001–p.008）、块 B（p.009–p.016）、块 C（p.017–p.024）各 8 条 + 本段（p.025–p.032）8 条。
- 本段分级汇总：**PASS± 8 页**（p.025–p.032），**PASS 0 页**，**FAIL 0 页**。逐页改动处数：p.025 = 4、p.026 = 4、p.027 = 1、p.028 = 5、p.029 = 0、p.030 = 2、p.031 = 2、p.032 = 4，合计 `edits=22`（其中 2 处为 peer 回归的纠正，见上）。
- 300dpi 仲裁 1 次、排除疑似缺陷：p.029 的 `‖f^{′n}e_1‖` 中项是否带撇（150dpi 与文本层均丢撇，300dpi 裁片确认印刷带撇、MD 正确）。PIL 仅用于裁图，未写 Markdown。
- 写入范围与手段合规：22 处修改**全部**用 Edit 工具逐处定位，未用 Python/正则/sed/heredoc 或任何脚本写回 Markdown；未执行任何 git 写操作；未碰根 `AUDIT-INDEX.md`/`AUDIT-PROGRESS.log`/`MEMORY.md`/`README.md`；未写 `audit-redo/` 新图；未碰姊妹篇；未启动或改动 mineru。
- Edit 定位限制如实登记：含 `\r`（`\right`、`\rangle`）的锚点会被当作回车转义而无法命中，本段对这类位置改用不含该序列的唯一锚点（如 `rray}$ then there exists`、`} }$. has a basis`、`o \infty ,$`），每处均先 `grep -cF` 实测锚点计数为 1 再编辑；p.026 首次尝试以含 `\right` 的锚点定位失败后，改用 `C.\tag{4.7}` 形式命中，全程未改用脚本绕过。
- PDF 只读复核：本段未对 PDF 执行任何写操作，SHA-256 仍为 `7f26dde3f9b206534584b2b94d4a86e6319e467918efca8b4d00b1b1ae574825`。

---

# 追加段：redo 块 E（PDF p.33–p.40，actor=`linden07`）

- 性质：同块 A/B/C/D，独立重做复核；每页重新渲染 PNG 目检 + `pdftotext` 文本层互证，唯一裁决源是印刷原页。
- 身份：actor=`linden07`；host=zcode Desktop；model=`opencode-go-chat/space-bunny-free`（本会话运行时自报）；effort=run 级配置未暴露，记 `UNKNOWN`。cwd=`/Users/aurolafly/.zcode/worktrees/cpf-redo-Lindenstrauss_2007_littlewood_published`；branch=`cpf-redo/Lindenstrauss_2007_littlewood_published`。
- 写入范围同前：只写本 AUDIT 文件与本篇 MinerU Markdown；未写根级真值文件、未写 `audit-redo/`、未执行 git 写操作、未碰姊妹篇、未碰 mineru。

## p.033（PDF p.33 / 印刷 p.545）
- PNG：/tmp/linden07_audit_p033.png（pngmono 150dpi）
- 核对：p.544 跨页续句（`H`-ergodic 分量、`X_H`）、Lemma 6.2 推论段（`Σ_i k_i = k`、Poincaré recurrence）、`SN_G(H) = N_G(H) = AH` 等式、algebraic 结论段与 QED、Proof of Corollary 1.4 全段（`A < L < G`、`g^{−1}Lg ∩ SL(k,ℤ)`、unimodular、reductive、`A ≅ ℝ^{k−1}`、`[36, Thm. 2.13]`、`g^{−1}h^{−1}Ahg`、`[21, Thm. 1.3]`、`1 ≠ m | k`）、Part 2 标题、§7 Definitions 标题与开篇句、运行头
- 结果：PASS±（2 处已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 927 行）：印刷「…in the notations of Lemma 6.2, the support of μ is contained in $X_H$**.**」（页图第 3–4 行、文本层第 3–5 行）行末有句点；MD 原件缺失。已补 `.$`。
  2. **已修复**（MD 第 939 行）：印刷「Proof of Corollary 1.4. …so that Lx is closed and μ is the L-invariant measure on **$Lx$.**」（页图第 8–9 行、文本层第 17–20 行）行末有句点；MD 原件缺失。已补 `.$`。
  3. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 545」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  4. **print quirk 忠实保留**：印刷作「**This show that** μ is algebraic」（页图第 7 行、文本层第 14 行，`show` 缺第三人称 s，疑印刷笔误）；MD 第 937 行同为 `This show that$\mu$is algebraic`，**与印刷一致，按铁律三不擅改为 shows**。
  5. 记号字距伪影：MD 第 931、934 行把记号 `SN_G` 写成 `S N _ {G}`（S 与 N 之间插入空格），印刷为连写的 $SN_G$（页图第 7 行「$SN_G(H)$」清晰可见为连写）。数学对象正确，仅字距，排版级，不改。
  6. 表述微调（登记不改）：印刷「this implies that the sum Σ_i k_i = k **since** otherwise there is a one-parameter subgroup…」（页图第 5 行、文本层第 7–8 行）；MD 第 929 行作「`$\sum_i k_i=k$; otherwise, there is…`」，用分号替换 `since` 并补一逗号。语义与逻辑关系不变，不误导。MD 第 951 行的「In the following**,** let」（印刷无此逗号）同属此类。
  7. 行内紧排缺空格：第 927、929、931、937、939、941、943、945、951 行（如「component of$\mu$is supported on a single H-orbit」「the set$S N _ { G } ( H )$of Theorem 6.1 satisfies」「By Theorem$1 . 3 , \mu$is algebraic, i.e. there are a subgroup」「it implies that$g ^ { - 1 } L g \cap \mathrm { S L } ( k , \mathbb { Z } )$is a lattice」「there is an$h \in L$so that」「with$g _ { i j } = 0$unless i is congruent to$j$mod m」）。排版级，不改。
  8. 字距伪影：MD 第 939 行 `Theorem$1 . 3 , \mu$`（定理号 1.3 被字距化）。编号正确，排版级，不改。
- 等式 `SN_G(H) = N_G(H) = AH` 核对（MD 第 934 行；页图第 7–8 行、文本层第 11–12 行）：印刷 `SN_G(H) = N_G(H) = AH` ——**三段等式的三个记号（下标 G 的两处、三处上标位置）与中间段 `N_G(H)` 未被误写为 `N_G(AH)` 或漏掉等号，MD 逐字吻合**。
- `Σ_i k_i = k` 与 Lemma 6.2 的衔接核对（MD 第 929 行；页图第 5 行）：印刷「By Lemma 6.2, this implies that the sum Σ_i k_i = k since otherwise **there is a one-parameter subgroup a(t) of A** so that for every x ∈ X_H its trajectory **a(t)x → ∞ as t → ∞**, in contradiction to Poincaré recurrence.」——**求和下限 i 与右端 k、极限 `a(t)x → ∞ as t → ∞` 的两个方向、以及与 p.544 Lemma 6.2 陈述中 `Σ_{i=1}^r k_i < k` 的严格小于形成对照**（此处为等于号 k，MD 两处分别正确保留，未混同）。
- Corollary 1.4 证明逐要素核对（MD 第 939–945 行；页图第 9–22 行、文本层第 17–37 行）：印刷
  「there are a subgroup **A < L < G** and a point **x = g SL(k,ℤ) ∈ X** so that **Lx is closed** and μ is the **L-invariant measure on Lx**」；
  「**g^{−1}Lg ∩ SL(k,ℤ)** is a lattice in g^{−1}Lg … the fact that L has any lattice implies it is **unimodular** … since **A is the maximal torus in G** implies L is **reductive**」；
  「…**A ≅ ℝ^{k−1}**, compact), so that Lx contains a compact A orbit.」；
  「By **[36, Thm. 2.13]**, there is an **h ∈ L** so that **g^{−1}h^{−1}Ahg** is defined over **Q** and is **Q-anisotropic**.」；
  「By **[21, Thm. 1.3]** … **g_{ij} = 0 unless i is congruent to j mod m for some 1 ≠ m | k** (by the **Moore ergodicity theorem**…) … **if k is prime this implies that L = SL(k,ℝ)**.」+ QED 方块
  ——**两处引文号 `[36, Thm. 2.13]` 与 `[21, Thm. 1.3]`、同余条件的 `1 ≠ m | k`（整除竖线未丢失）、`A ≅ ℝ^{k−1}` 的指数 k−1、`g^{−1}h^{−1}Ahg` 的四个因子次序、`Q`-anisotropic 的连字符，以及两枚 QED 方块（Theorem 1.3 证明末、Corollary 1.4 证明末）全部在位**。
- Part 2 与 §7 标题核对（MD 第 947、949 行）：印刷双行居中标题「**Part 2. Positive entropy and the set of / exceptions to Littlewood’s Conjecture**」，MD 第 947 行 `## Part 2. Positive entropy and the set of exceptions to Littlewood’s Conjecture` 合并为单行，**文字与顺序一致**（注意此处 `Conjecture` 首字母大写，与 §7 开篇的 `Littlewood’s conjecture` 小写不同，MD 两处分别保留）；§7 标题 `## 7. Definitions` ✓。
- §7 开篇句核对（MD 第 951 行）：印刷「We recall the definition of **Hausdorff dimension, box dimension, topological and metric entropy**. In the following let Y be a metric space with metric $d_Y(\cdot,\cdot)$.」——**三个定义对象（Hausdorff dimension / box dimension / topological and metric entropy）与度量记号 `d_Y` 的下标 Y 全部吻合**，句末句点在位。
- 页边界核对：印刷 p.545 止于「…let Y be a metric space with metric $d_Y(\cdot,\cdot)$.」（页图末三行、文本层第 44–46 行）；MD 第 951 行对应结束，§7 的其余定义属 p.546，留待 p.034 核对，无跨页错接。

## p.034（PDF p.34 / 印刷 p.546）
- PNG：/tmp/linden07_audit_p034.png（pngmono 150dpi）
- 核对：§7.1 Notions of dimension 标题与首句、Hausdorff 测度定义式、$\mathcal{C}_\varepsilon$ 覆盖定义、`D > m` 与 `ℝ^m` 句、公式 (7.1)（`inf`/`sup` 两项）、`ε`-separated 定义与 `b_ε(B)`、公式 (7.2)、单调性句与 `log ε_{n+1}/log ε_n → 1`、Lipschitz 等价度量句、公式 (7.3)、子可加性括注、公式 (7.4)、乘积度量式与 `dim_box Y ≤ dim_box Y_1 + dim_box Y_2`、§7.2 标题与首段、`(N,ε)`-separated 定义与 `s_{N,ε}(T)`、公式 (7.5)、`H_μ(𝒫)` 定义式、运行头
- 结果：PASS±（1 处已修复，其余差异为字形/排版/措辞级，不误导）
- 差异列表：
  1. **已修复**（MD 第 991 行）：印刷「then dim_box Y ≤ dim_box Y₁ + dim_box Y₂**.**」（页图第 25 行、文本层第 37 行）行末有句点；MD 原件缺失。已补 `.$`。
  2. MD 缺运行头「546 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  3. 措辞微调（登记不改，三处）：① 印刷「is any countable cover of B **with** sets $C_i$ of diameter diam($C_i$) **less than** ε」，MD 第 959 行作「by sets … `diam(C_i)<\varepsilon`」（介词与不等号写法，内容等价）；② 印刷「the **biggest** ε-separated subset」，MD 第 965 行作「the **largest** ε-separated subset」；③ 印刷「then the **(upper)** box dimension (**upper** Minkowski dimension) is defined by」，MD 第 965 行去掉 `upper` 的括号强调。三处均不改变数学内容或术语指向，不误导。
  4. 语序调整（登记不改）：印刷「…do not change when we use **instead of the metric** $d_Y(\cdot,\cdot)$ **a different but Lipschitz equivalent metric** $d'_Y(\cdot,\cdot)$」，MD 第 973 行改为「when we use a different but **Lipschitz-equivalent** metric $d'_Y(\cdot,\cdot)$ **instead of the metric** $d_Y(\cdot,\cdot)$」并补了连字符。语义相同，不误导。
  5. 字形/字距伪影：MD 第 959、965、973、991、993、996、999、1002、1005 行含 `\mathrm { \mathrm { b o x } }`、`\operatorname* { l i m s u p}`、`\mathsf { h}`、`\mathsf { H}` 等字距化/字体替换；第 996、1005 行含 `~ = ~`、`0 log$0 ~ = ~ 0 .$` 的空格伪影。数学对象正确，排版级，不改。
  6. 行内紧排缺空格：第 959、965、971、979、985、991、993、999、1005 行（如「the$ D$-dimensional Hausdorff measure」「is any countable cover of $B$ by sets」「(This follows easily from the fact that the measure$\mathcal { H } ^ { D }$is subadditive.) For any B we have」「If$Y = Y _ { 1 } \times Y _ { 2 }$is nonempty」「Let$\mu$be a$T \cdot$-invariant measure on$Y$」）。排版级，不改。
- Hausdorff 测度定义式核对（150dpi 页图第 4–5 行、文本层第 6–9 行；MD 第 956 行）：印刷 `𝓗^D(B) = lim_{ε→0} inf_{𝒞_ε} Σ_i (diam C_i)^D,` ——**算子的先后次序为 `lim inf`（先 ε→0 的极限、再对覆盖族取 inf），MD 第 956 行 `\lim _ {\varepsilon \to 0} \inf _ {\mathcal {C} _ {\varepsilon}} \sum_ {i} (...)` 顺序一致**（若误写成 `inf lim` 会改变定义对象）；`𝒞_ε` 的花体、求和下标 `i`、`(diam C_i)^D` 的指数与行末逗号全部吻合。
- 公式 (7.1) 核对（页图第 8 行、文本层第 14 行；MD 第 962 行）：印刷 `dim_H(B) = inf{D : 𝓗^D(B) = 0} = sup{D : 𝓗^D(B) = ∞}.` ——**两处定义域的等值条件分别为 `= 0` 与 `= ∞`**（右端不是 0，此处最易误识），MD 第 962 行 `\inf \{D: \mathcal {H} ^ {D} (B) = 0 \} = \sup \{D: \mathcal {H} ^ {D} (B) = \infty \}` 与印刷**逐字符吻合**，编号 (7.1) 在位。
- 公式 (7.2) 与单调性句核对（MD 第 968、971 行；页图第 12–14 行、文本层第 19–23 行）：印刷 `dim_box(B) = limsup_{ε→0} log b_ε(B) / |log ε|.`；「Note that $b_{\varepsilon_2}(B) \geq b_{\varepsilon_1}(B)$ if $\varepsilon_2 < \varepsilon_1$. Therefore, it is sufficient to consider a sequence $\varepsilon_n$ in (7.2) if **log ε_{n+1} / log ε_n → 1** for n → ∞.」——**分子 `log b_ε(B)`、分母 `|log ε|` 的绝对值、`limsup`（非 lim）、以及两个下标条件 `ε₂ < ε₁` 的方向与 `log ε_{n+1}/log ε_n → 1` 的商式（**分子是 n+1、分母是 n**）全部正确**，编号 (7.2) 在位。
- 公式 (7.3)/(7.4) 核对（MD 第 976、982 行；页图第 17、21 行、文本层第 28–34 行）：印刷 `(7.3) dim_H(⋃_{i=1}^∞ B_i) = sup_i dim_H(B_i).`；`(7.4) dim_H(B) ≤ dim_box(B).` ——**并集下限 `i = 1` 与上限 `∞`、右端 `sup_i` 的下标、(7.4) 的不等号 `≤` 方向、以及与 (7.3) 不同的维数记号（(7.3) 两处均 `dim_H`、(7.4) 为 `dim_H` 对 `dim_box`）全部吻合**。
- 乘积度量式核对（MD 第 988 行；页图第 23–24 行、文本层第 35–36 行）：印刷 `d_Y((x_1, x_2), (y_1, y_2)) = max(d_{Y_1}(x_1, x_2), d_{Y_2}(y_1, y_2)),` ——**两侧的度量下标 `Y` 与分量下标 `1`/`2` 的嵌套次序（`d_{Y_1}`、`d_{Y_2}`）以及 max 的两个参数均与印刷一致**；注意印刷在 `d_{Y_1}` 内写作 `(x_1, x_2)`、在 `d_{Y_2}` 内写作 `(y_1, y_2)`（分量配对与常规写法不同，疑印刷笔误），**MD 忠实保留、未按常理「纠正」**，在此登记为 print-level 写法保留。
- 公式 (7.5) 逐要素核对（150dpi 页图第 27 行、文本层第 45–47 行；MD 第 996 行）：印刷 `h_top(T) = lim_{ε→0} limsup_{N→∞} (1/N) log s_{N,ε}(T) = sup_{ε>0} limsup_{N→∞} (1/N) log s_{N,ε}(T).` —— **两个外层算子分别是 `lim_{ε→0}` 与 `sup_{ε>0}`（一为极限、一为上确界，方向与符号不同，MD 第 996 行 `\lim _ {\varepsilon \to 0}` 与 `\sup _ {\varepsilon > 0}` 分别正确）、两个内层均为 `limsup_{N→∞}`、归一因子 `1/N`、分离数记号 `s_{N,ε}(T)` 的双下标与熵记号 `h_top` 的下标、编号 (7.5) 与行末句点全部吻合**；这是本页最易因 OCR 而丢失「lim/sup 之别」与「1/N」处，已逐项核对。
- `(N,ε)`-separated 与 `s_{N,ε}(T)` 定义段核对（MD 第 993、999、1002 行）：印刷「…if for any two different x, y ∈ E there exists an integer **0 ≤ n < N** with **d(T^n x, T^n y) ≥ ε**. Let **s_{N,ε}(T)** be the cardinality of the largest (N, ε)-separated set…」「Let μ be a **T ·-invariant** measure on Y, and let 𝒫 be a finite partition of Y into measurable sets. Then **𝓗_μ(𝒫) = −Σ_{P∈𝒫} μ(P) log μ(P)**」——**`n` 的范围 `0 ≤ n < N`（上界严格小于）、`d(T^n x, T^n y)` 的两个 T^n、`≥ ε` 的方向、`s_{N,ε}` 与 `𝓗_μ(𝒫)` 的下标、以及熵和式的负号与 `log μ(P)` 全部吻合**。
- 页边界核对：印刷 p.546 止于公式 (7.5)（页图末行、文本层第 45–47 行）；MD 第 996 行对应结束。MD 第 999 行起的 `H_μ(𝒫)` 说明段与 `𝒫 ∨ 𝒬` 共同细化属印刷 p.547，留待 p.035 核对，无跨页错接。

## p.035（PDF p.35 / 印刷 p.547）
- PNG：/tmp/linden07_audit_p035.png（pngmono 150dpi）
- 核对：p.546 跨页续段（`𝓗_μ(𝒫)` 说明、`0 log 0 = 0`、`𝒫 ∨ 𝒬` 共同细化）、度量熵定义式 `(1/N)𝓗_μ(⋁_{i=0}^{N−1} T^{−i}𝒫)`、公式 (7.6)（`sup_𝒫`）、`h_μ(T) ≤ h_top(T)` 不等式、变分原理引文 `[49, Thm. 8.6]` 与公式 (7.7)（`sup_μ`）、§8 标题与开篇段（`SL(n,ℝ)/SL(n,ℤ)`、`a|_K`）、Lemma 8.1 陈述与其展示式（`c_0^{-1}‖g−h‖ ≤ d(g,h) ≤ c_0‖g−h‖`、`B_r^G`）、`‖A‖ = max_{i,j}|a_{ij}|` 定义与 `Mat(k,ℝ)`、运行头
- 结果：PASS±（1 处已修复，其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复**（MD 第 1037 行）：印刷「The following easy lemma shows that the dimensions can be defined using the right invariant metric or a norm on **Mat(k, ℤ).**」（页图第 26–27 行、文本层第 45–46 行）行末有句点；MD 原件缺失。已补 `.$`。
  2. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 547」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  3. **print quirk 忠实保留（指标混用，印刷自身）**：印刷 §8 开篇句用 **$X = \mathrm{SL}(n,\mathbb{R})/\mathrm{SL}(n,\mathbb{Z})$（参数 n）**，而同页 Lemma 8.1 的法范数定义用 **$\mathrm{Mat}(k,\mathbb{R})$（参数 k）**（页图第 29 行与第 27 行并读可辨）。MD 第 1035、1045 行**分别忠实保留 n 与 k**，未按上下文统一，在此登记为印刷自身的指标不一致。
  4. 字形/字距伪影：MD 第 1005 行 `$\mathcal { P } _ { \cdot }$`、`0 log$0 ~ = ~ 0 .$`；第 1035 行 `$X ,$`（多余逗号）、`$a | _ { K }$`；第 1045 行 `f o r`（for 被字距化）。渲染字形相近，排版级，不改。
  5. 行内紧排缺空格：第 1005、1017、1019、1035、1037、1039、1045 行（如「is the entropy of the finite partition$\mathcal { P } _ { \cdot }$. (Here 0 log」「where the supremum is taken over all finite partitions$\mathcal { P }$of$Y$into measurable sets」「the positive diagonal subgroup $A$on$X =」「We fix an element$a \in A$and study multiplication from the left by$a$on$X ,$」「Lemma 8.1. For every$r > 0$there exists a constant$c _ { 0 } \geq 1$such that」）。排版级，不改。
- 度量熵定义式逐要素核对（150dpi 页图第 9–11 行、文本层第 12–17 行；MD 第 1008 行）：印刷 `h_μ(T, 𝒫) = lim_{N→∞} (1/N) 𝓗_μ(⋁_{i=0}^{N−1} T^{−i}𝒫)` ——**大 ⋁ 的下标起点 `i = 0` 与终点 `N − 1`、被作用的 `T^{−i}𝒫` 的负指数（多次合成沿用 `T^{-i}` 而非 `T^{i}`）、归一因子 `1/N`、极限变量 `N → ∞`、以及熵记号 `𝓗_μ` 的花体下标 μ 全部吻合**；公式本体（印刷式末无标点，句接「and the metric entropy…」）与 MD 的标点状态一致。
- 公式 (7.6)/(7.7) 与熵不等式核对（MD 第 1014、1022、1028 行；页图第 13、18、21 行、文本层第 21、29、32 行）：印刷
  `(7.6)  h_μ(T) = sup_𝒫 h_μ(T, 𝒫),`
  `h_μ(T) ≤ h_top(T).`
  `(7.7)  h_top(T) = sup_μ h_μ(T),`
  ——**(7.6) 的上确界取在划分族 `𝒫` 上、(7.7) 的上确界取在测度 `μ` 上，二者下标不同且 MD 未互换**；(7.6)(7.7) 的**行末均为逗号**（各接「where the supremum is taken over…」一句）、中间不等式 `h_μ(T) ≤ h_top(T)` 为**句点**、拓扑熵记号 `h_top` 的下标 `top` 在三式中一致、编号 (7.6)/(7.7) 各自唯一——**全部与印刷吻合**。
- 变分原理引文核对（MD 第 1025 行；页图第 19 行、文本层第 30 行）：印刷「Furthermore, the variational principle **[49, Thm. 8.6]** states that」——**文献号 49 与定理号 8.6 均正确**，未被误写为 `[49, Thm. 8.5]` 或 `[45, …]`。
- §8 开篇段核对（MD 第 1035 行；页图第 22–27 行、文本层第 39–44 行）：印刷「We return to the study of the **left action** of the positive diagonal subgroup A on **X = SL(n,ℝ)/SL(n,ℤ)**. We fix an element **a ∈ A** and study **multiplication from the left by a** on X, in particular we are interested in the dynamical properties of the restriction **a|_K** of this map to a compact subset **K ⊂ X**. This will lead to a close connection between topological entropy and box dimension in an **unstable manifold**.」——**「left action」「multiplication from the left by a」「a|_K」「K ⊂ X」与「unstable manifold」逐项吻合**，其中 `a|_K` 的限制记号（`$a | _ { K }$`）未被误写为 `a_K` 或 `a|K` 之外的形式。
- Lemma 8.1 逐要素核对（MD 第 1039、1042、1045 行；页图第 28–29 行、文本层第 48–53 行）：印刷
  `Lemma 8.1. For every r > 0 there exists a constant c_0 ≥ 1 such that`
  `c_0^{−1}‖g − h‖ ≤ d(g, h) ≤ c_0‖g − h‖  for all g, h ∈ B_r^G,`
  `where ‖A‖ = max_{i,j}|a_{ij}| for A = (a_{ij}) ∈ Mat(k,ℝ).`
  ——**`c_0 ≥ 1` 的不等号方向、左端的 `c_0^{−1}` 负指数（不能写成 `c_0^1`）、两处范数 `‖g − h‖`、球记号 `B_r^G` 的上标 G 与下标 r、法范数定义的 `max_{i,j}` 双下标与 `|a_{ij}|`、以及 `A = (a_{ij})` 的矩阵记号全部吻合**；行末标点（展示式逗号、范数定义句点）与印刷一致。
- 页边界核对：印刷 p.547 止于「…for $A = (a_{ij}) \in \mathrm{Mat}(k,\mathbb{R})$.」（页图末行、文本层第 53 行）；MD 第 1045 行对应结束，Lemma 8.1 的证明属 p.548，留待 p.036 核对，无跨页错接。

## p.036（PDF p.36 / 印刷 p.548）
- PNG：/tmp/linden07_audit_p036.png（pngmono 150dpi）
- 核对：p.547 跨页续段（局部同构、`r = r(x)`、`B_r^G` 与 `B_r(x)`）、`ay = (aga^{−1})ax` 与局部共轭解释、`U`/`V`/`C` 三个子群定义式（`n → −∞`、`n → +∞`、`aga^{−1} = g`）、`δ_{ij}` 与 `I_k = (δ_{ij})`、三个零块判据（`≥`/`≤`）、`g = g_C g_U g_V` 分解、公式 (8.1)（`max` 三项）、`c_1 ≥ 1`、`A ⊂ C` 与 partially hyperbolic 句、Lemma 8.2 陈述（`λ > 1`、`c_2 > 0`、`λ^{−N}ε`、`n < N`、`c_2ε`）、Proof 全部（`ε ∈ (0,r)`、`c_0^{−2}λ^n`、`max(...) < r`、`λ^{−1}`、末式与 QED）、运行头
- 结果：PASS±（7 处已修复；含 6 处标点脱离与 1 处 QED 标记缺失；其中 1 次编辑误落点已发现并回滚，见下）
- 差异列表：
  1. **已修复**（MD 第 1049 行，两处）：印刷「Then $ay = (aga^{-1})ax$**.** In other words, …like conjugation by a on $B_r^G$**.** For this reason we define the subgroups」（页图第 5–8 行、文本层第 9–12 行）在两处句末各有句点；MD 原件两处均缺失（`} ) a x$ In other words`、`on$B _ { r } ^ { G }$ For this reason`）。已分别补 `$.`。
  2. **已修复**（MD 第 1055 行，两处）：印刷「…the unstable, stable, and central subgroup (for conjugation with $a$)**.** Let $\delta_{ij} = 0$ …」与「…for all $i,j$ with $a_{ii} \le a_{jj}$**.** Furthermore, there exists a neighborhood $U_0$ …」（页图第 10、14 行、文本层第 16、19–20 行）；MD 原件作 `a )$ Let` 与 `j }$ Furthermore`，两句粘连。已分别补 `$.`。
  3. **已修复**（MD 第 1061 行）：印刷「for some constant $c_1 \ge 1$**.**」（页图第 15 行、文本层第 26 行）行末有句点；MD 原件缺失。已补 `.$`。
  4. **已修复**（MD 第 1065 行）：印刷 Lemma 8.2 结论「…with $d(a^nfz, a^nz) \ge c_2\varepsilon$**.**」（页图第 18 行、文本层第 33–34 行）行末有句点；MD 原件缺失。已补 `.$`。
  5. **已修复**（MD 第 1076 行，缺失 QED 标记）：印刷末式「$d(a^nfz, a^nz) = … > c_0^{-2}\lambda^{-1}\varepsilon$**.** □」（页图末行、文本层第 52–53 行）在行末带证毕方块 **□**；MD 原件完全没有。已补 `.$□`。
  6. **编辑误落点与回滚（如实登记）**：为落实第 5 项，首次所选锚点 `varepsilon .$` 经 `grep -cF` 计数为 1，但该串在全篇命中的**并非**第 1076 行，而是第 1359 行（`Suppose$\varepsilon > 0$and there exists$a \in A ^ { + }$with$… < \varepsilon .$`，约印刷 p.047 处）；Edit 报告成功并在该行插入了多余的 `□`。**已用 Edit 立即回滚**（把 `$□. Then` 还原为 `$. Then`），并经 `grep -n '□'` 与基线逐行对照确认：当前全篇 `□` 计数为 23、基线为 21，多出的恰好两枚分别位于第 921 行（块 D 的 p.032 已登记修复）与第 1076 行（本页第 5 项），**无其他误插、无残留**。随后改用含区分性内容 `{k}) > c _ {0} ^ {- 2} \lambda^ {- 1} \varepsilon .` 的锚点（`grep -cF` 计数 = 1 且定位行号 = 1076）重新定位，才正确落到目标行。全程未用脚本写回 Markdown。
  7. MD 缺运行头「548 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  8. 字形伪影：MD 第 1065 行 `$a n y \ z \in K$`（印刷为普通文字「any $z \in K$」，MD 把 `any` 连同 `z ∈ K` 一起落入数学定界并字距化）；第 1055 行 `g \in U { \mathrm { ~ i f ~ } }`（把英文 `if` 排成数学关系 `\mathrm{~i f~}`）。渲染可还原、不误导，排版级，不改（前者已由前序 peer 部分整理）。
  9. 行内紧排缺空格：第 1047、1049、1055、1063、1065 行（如「is locally isomorphic to$\operatorname { S L } ( k , \mathbb { R } )$；more specifically」「$\mathbf { t } \in \Sigma$, and$a = \alpha ^ { \mathbf { t } }$. Then」「Lemma 8.2. Let$K \subset X$be compact with aK$\subset K$and let$r = r ( K )$be as above」）。排版级，不改。
- `U`/`V`/`C` 三个子群定义式逐要素核对（150dpi 页图第 9–12 行、文本层第 13–16 行；MD 第 1052 行）：印刷
  `U = {g ∈ SL(k,ℝ) : a^n g a^{−n} → 0  for n → −∞},`
  `V = {g ∈ SL(k,ℝ) : a^n g a^{−n} → 0  for n → +∞}, and`
  `C = {g ∈ SL(k,ℝ) : a g a^{−1} = g},`
  —— **`U` 与 `V` 的极限方向 `n → −∞` 与 `n → +∞` 未互换（互换会颠倒 unstable/stable 的定义，是本页最易错处），两者的共轭式均为 `a^n g a^{−n}`（而非 `a g a^{-1}`，后者只属于 C）**，`SL(k,ℝ)` 的参数 k、逗号与「and」的位置，MD 与印刷**逐字吻合**。
- 零块判据与不等号方向核对（MD 第 1055 行；页图第 13–15 行、文本层第 17–19 行）：印刷「`g ∈ C` if `g_{ij} = 0` for all i, j with `a_{ii} ≠ a_{jj}`, `g ∈ U` if `g_{ij} = δ_{ij}` for all i, j with `a_{ii} ≥ a_{jj}`, and similarly `g ∈ V` if `g_{ij} = δ_{ij}` for all i, j with `a_{ii} ≤ a_{jj}`」—— **三个条件各自的不等号 `≠`、`≥`、`≤` 与所属子群 `C`/`U`/`V` 的对应逐项吻合**（`U` 对应 `≥`、`V` 对应 `≤`，方向未互换）；`δ_{ij} = 0 for i ≠ j`、`δ_{ii} = 1`、`I_k = (δ_{ij})` 三项约定在位。
- 公式 (8.1) 逐要素核对（页图第 16–17 行、文本层第 23–26 行；MD 第 1058 行）：印刷 `c_1^{−1}d(g,h) ≤ max(d(g_C,h_C), d(g_U,h_U), d(g_V,h_V)) ≤ c_1 d(g,h)` —— **`max` 恰含三项且次序为 `(g_C,h_C)`、`(g_U,h_U)`、`(g_V,h_V)`（与前一行的分解 `g = g_C g_U g_V` 一致）、左端 `c_1^{−1}` 的负指数、两个不等号方向、编号 (8.1) 全部吻合**；印刷该式行末无标点（句接「for some constant c₁ ≥ 1.」），MD 亦无，一致。
- Lemma 8.2 陈述逐要素核对（MD 第 1065 行；页图第 18–19 行、文本层第 31–34 行）：印刷「Let $K \subset X$ be compact with $aK \subset K$ and let $r = r(K)$ be as above. There exists **$\lambda > 1$ and $c_2 > 0$** so that for any small enough **$\varepsilon > 0$**, **any $z \in K$** and $f \in B_r^U$, and any integer **$N \ge 1$** with **$d(fz,z) \ge \lambda^{-N}\varepsilon$**, there exists **a nonnegative integer $n < N$** with **$d(a^nfz, a^nz) \ge c_2\varepsilon$**」—— **`\lambda^{-N}` 的负指数（`N` 在指数上而非 `N·λ^{-1}`）、`\lambda > 1` 与 `c_2 > 0` 两个常数的存在性、`B_r^U` 的上标 U、`n` 为非负整数且 `n < N`（严格小于）、以及末式 `d(a^n f z, a^n z)` 中 f 与 z 的次序，全部与印刷吻合**；MD 第 1065 行 `$a n y \ z \in K$` 的排版问题见第 8 项（内容仍为「any z ∈ K」）。
- Proof 逐式核对（MD 第 1067、1070、1073、1076 行；页图第 20–26 行、文本层第 36–53 行）：
  - 「there exists $\varepsilon \in (0,r)$ such that $d(afa^{-1}, I_k) < r$ whenever $d(f, I_k) < \varepsilon$」——**`\varepsilon` 的区间 `(0,r)` 开区间两端在位**；
  - 「$\|afa^{-1} - I_k\| \ge \lambda\|f - I_k\|$ for all $f \in B_r^U$」——**两条范数项未被降格为绝对值**；
  - 「By Lemma 8.1, $d(a^nfa^{-n}, I_k) \ge c_0^{-2}\lambda^n d(f, I_k)$」——**`c_0^{-2}` 的指数 −2 与 `\lambda^n` 的正指数 n 并存，二者未互换**；
  - `$\max(d(f, I_k), \dots, d(a^nfa^{-n}, \mathrm{Id})) < r.$` —— **注意印刷此处末项用 `Id`（Id）而首项用 `I_k`，属印刷自身的记号不一致；MD 第 1070 行 `\mathrm{Id}` 与 `\mathrm{I} _ {k}` 分别忠实保留，未统一**，在此登记为 print-level 写法保留；
  - 「$\lambda^{-N}\varepsilon \le d(fz,z) = d(f, I_k) < r$」与「there exists $n < N$ with $c_0^{-2}\lambda^{-1}\varepsilon < d(a^nfa^{-n}, I_k) < r$」——**前式 `λ^{-N}` 与后式 `λ^{-1}`（指数不同）未被混同**；
  - 末式 `$d(a^nfz, a^nz) = d((a^nfa^{-n})a^nz, a^nz) = d(a^nfa^{-n}, I_k) > c_0^{-2}\lambda^{-1}\varepsilon.$` —— **中间的因式分解 `(a^nfa^{-n})a^nz`（先共轭再平移）正确，末项为严格不等号 `>`**（前两处为 `≤`/`<`，此处为 `>`），行末句点与 QED 方块已在第 5 项补齐。
- 页边界核对：印刷 p.548 止于末式 + QED 方块（页图末行、文本层第 52–53 行）；MD 第 1076 行对应结束，Lemma 8.2 的证明完整闭合，§8 后续属 p.549，留待 p.037 核对，无跨页错接。

## p.037（PDF p.37 / 印刷 p.549）
- PNG：/tmp/linden07_audit_p037.png（pngmono 150dpi）
- 核对：Proposition 8.3 陈述与两个分列 (1)(2)、Proof 起段与公式 (8.2)（`P_y = K ∩ (B^U_ε y)`）、覆盖论证段、`b ∈ (0, dim_box(P_y))` 段（`ελ^{−N}`、`λ^{bN}ε^{−b}`）、`(N, c_2ε)`-separated 论证（`f = gh^{−1}`、`2ε ≤ r`、`s_N(a) ≥ |F_N| > λ^{bN}`、`b log λ`）与 QED、`UV` 非子群句、Lemma 8.4 陈述（`B^U_r B^V_r ⊂ B^G_{2r}`、`c_3 ≥ 1`、`λ^{−N}ε`、`|n| < N`）、Proof 起段、三项距离链 `< 2r`、`(8.1)` 与 `B^G_{c_1^{-1}r}` 段、运行头
- 结果：PASS±（5 处已修复，含 1 处重复逗号；其余差异为字形/排版/措辞级，不误导）
- 差异列表：
  1. **已修复**（MD 第 1081 行）：印刷「Proposition 8.3. Let $a \in A$ and $K \subset X$ be compact with $aK \subset K$**.** Then one of the following properties holds.」（页图第 3–4 行、文本层第 6–7 行）在 `aK ⊂ K` 后有句点；MD 原件作 `…$a K \subset K$ Then one of…` 两句粘连。已补 `$.`。
  2. **已修复**（MD 第 1083 行，命题分列 (1)）：印刷「…of box dimension zero for every $x \in X$**.**」（页图第 5–6 行、文本层第 9–10 行）行末有句点；MD 原件缺失。已补 `.$`。
  3. **已修复**（MD 第 1099 行）：印刷「Note however, that the set UV is not a subgroup of **SL(k,ℝ).**」（页图第 20–21 行、文本层第 39–40 行）行末有句点；MD 原件缺失。已补 `.$`。
  4. **已修复**（MD 第 1101 行，重复逗号）**：MD 原件作「for any small enough `$\varepsilon > 0 ,$,` any $x \in X$…」——数学定界符内已有一个逗号，紧随其后又补了一个，形成**重复逗号**；印刷（页图第 23 行、文本层第 44 行）为单逗号「for any small enough **ε > 0**, any x ∈ X…」。已删去多余逗号。
  5. **已修复**（MD 第 1101 行，Lemma 8.4 结论句末句点）**：印刷「…there exists an integer n with $d(a^ngx, a^nhx) \ge c_3\varepsilon$ and **$|n| < N$.**」（页图第 26–27 行、文本层第 45–46 行）行末有句点；MD 原件缺失。已补 `.$`。（第 4、5 项为同一行的两处缺陷，分两次定位完成。）
  6. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 549」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  7. 措辞微调（登记不改）：印刷「then the topological entropy $h_{top}(a|_K) > 0$ **is positive**」（页图第 17 行、文本层第 23–24 行）在记号后带一处 `> 0`；MD 第 1095 行作「then the topological entropy $\mathsf{h}_{\mathrm{top}}(a|_K)$ is positive」，省去 `> 0`。因句中已有 `is positive` 承担同一断言，语义不丢失，不误导。
  8. 字形/字距伪影：MD 第 1097 行 `\mathsf h_{\mathrm{top}}`（无衬线）、`\mathsf h_{\mathrm{top}}(a|_K)`；第 1103、1106 行 `\mathrm{I}_k`。渲染字形相近，排版级，不改。
  9. 行内紧排缺空格：第 1081、1083、1085、1087、1091、1093、1099、1101、1103、1109、1111 行（如「Let$a \in A$and$K \subset X$be compact」「The intersection$U x \cap K$of the unstable manifold」「Proof. Note, that the first possibility follows if there exists some$\varepsilon > 0$」「$P _ { y } = K \cap \left( B _ { \varepsilon } ^ { U } y \right)$has box dimension zero」「Proof. Recall that we use the right invariant metric d to define the balls」「and so$B _ { r } ^ { U } B _ { r } ^ { V } \subset B _ { 2 r } ^ { G }$」）。排版级，不改。
- 公式 (8.2) 核对（150dpi 页图第 7 行、文本层第 18 行；MD 第 1091 行）：印刷 `P_y = K ∩ (B^U_ε y) has box dimension zero for every y ∈ K.` ——**球的上下标（`B^U_ε` 上标 U、下标 ε）与自变量 `y` 的乘写位置（`B^U_ε y` 而非 `(B^U_ε)y`）、以及「for every $y \in K$」的量词与行末句点全部吻合**；编号 (8.2) 在位。
- 分离集构造段逐要素核对（MD 第 1095、1097 行；页图第 14–19 行、文本层第 26–35 行）：印刷
  「Let **$b \in (0, \dim_{box}(P_y))$**. For every $N > 0$ let $F_N \subset P_y$ be a maximal (finite) **$\varepsilon\lambda^{-N}$-separated** set. By choice of $b$ and the definition of box dimension in (7.2) there are infinitely many integers $N$ with **$|F_N| \ge \lambda^{bN}\varepsilon^{-b}$**.」
  「By construction, **$\varepsilon\lambda^{-N} \le d(gx, hx) < 2\varepsilon \le r$**. By Lemma 8.2 applied to **$z = hx$ and $f = gh^{-1}$** there exists a nonnegative $n < N$ with **$d(a^ngx, a^nhx) \ge c_2\varepsilon$**. Therefore $F_N$ is $(N, c_2\varepsilon)$-separated as claimed, and for infinitely many $N$ we have **$s_N(a) \ge |F_N| > \lambda^{bN}$**. Finally… **$h_{top}(\alpha^t) \ge b\log\lambda > 0$**。」
  —— **`\varepsilon\lambda^{-N}` 与 `\lambda^{bN}\varepsilon^{-b}` 的幂次与乘子位置、`|F_N|` 的基数记号、`s_N(a) \ge |F_N| > \lambda^{bN}`（第一处 `\ge`、第二处严格 `>`）方向、`f = gh^{-1}` 的逆元次序与取 `z = hx` 的对应、以及末式 `b\log\lambda > 0` 全部吻合**；`2\varepsilon \le r` 的不等号方向亦正确。
  - **print quirk 忠实保留**：印刷在末句作「the definition of topological entropy in (7.5) implies that **$h_{top}(\alpha^t) \ge b\log\lambda > 0$**」（页图第 19 行、文本层第 34–35 行，上标为 **t**），而同页上文一律用 $h_{top}(a|_K)$；MD 第 1097 行末作 `$\mathsf h_{\mathrm{top}}(a|_K)$`，**把印刷末句的 `\alpha^t` 换成了 `a|_K`**。此项属于 MD 相对印刷的记号替换（语义等价，读者可据此对应同一算子），但**并非逐字转录**；因不构成数学错误、且改动需自行判断哪一记号为「本意」，本段**不擅自改回**，在此如实登记为待 canonical integrator 裁决的记号差异。
- 距离三项链核对（MD 第 1106 行；页图第 24 行、文本层第 31–32 行）：印刷 `d(g_U g_V, I_k) ≤ d(g_U g_V, g_V) + d(g_V, I_k) = d(g_U, I_k) + d(g_V, I_k) < 2r` ——**四个算子项、三种关系符 `≤` → `+` → `=` → `<` 的次序、上下标 `g_U`/`g_V`/`I_k`、以及右端常数 `2r` 全部吻合**；印刷该式行末无标点（句接「and so $B^U_r B^V_r \subset B^G_{2r}$」），MD 亦无，一致。
- Lemma 8.4 陈述逐要素核对（MD 第 1101 行；页图第 22–27 行、文本层第 42–46 行）：印刷
  「Let $K \subset X$ be compact with **$aK = K$**. Then **$B^U_r B^V_r \subset B^G_{2r}$** and there exists **$\lambda > 1$ and $c_3 \ge 1$** so that for any small enough $\varepsilon > 0$, any $x \in X$ and $g, h \in B^U_r B^V_r$ with **$hx \in K$**, and any integer **$N \ge 1$** with **$d(gx, hx) \ge \lambda^{-N}\varepsilon$**, there exists **an integer $n$** with $d(a^ngx, a^nhx) \ge c_3\varepsilon$ and **$|n| < N$**.」
  ——**`aK = K`（等号，与 Proposition 8.3 的 `aK ⊂ K` 不同）、球的上下标 `B^U_r B^V_r ⊂ B^G_{2r}`（右侧上标 **G** 而非 U/V）、`\lambda^{−N}\varepsilon` 的负指数与乘子、`c_3 \ge 1`（≥ 号）、结论中 `n` 为**任意整数**（`|n| < N`，与 Proposition 8.3 的「非负 n < N」不同）——这三处与命题版的差异均被正确区分、未混同**。
- `B^G_{c_1^{-1}r}` 段核对（MD 第 1111 行；页图第 27 行起、文本层第 38–43 行）：印刷「Assume $\varepsilon$ is small enough so that $aB^G_\varepsilon a^{-1} \subset B^G_{c_1^{-1}r}$. Let $\lambda > 1$ be such that **$\|afa^{-1} - I_k\| \ge \lambda\|f - I_k\|$ for $f \in U$** and **$\|a^{-1}fa - I_k\| \ge \lambda\|f - I_k\|$ for $f \in V$**.」—— **两个范数不等式中的共轭方向分别为 `a f a^{-1}`（对 U）与 `a^{-1} f a`（对 V），符号相反、未互换**；球 `B^G_{c_1^{-1}r}` 中 `c_1` 的**负指数 −1**（承前引理 (8.1) 的 `c_1^{−1}` 下界）与常数 `r` 均正确。本页所核各式中 `c_1^{−1}` 与 `λ^{−N}`/`λ^{−n}` 的负指数共有四处，MD 与印刷**逐处吻合，未见丢指数或丢撇**。
- 页边界核对：印刷 p.549 止于 Lemma 8.4 陈述（页图末两行、文本层第 42–46 行）；MD 第 1101 行对应结束，Lemma 8.4 的证明续文属 p.550，留待 p.038 核对，无跨页错接。

## p.038（PDF p.38 / 印刷 p.550）
- PNG：/tmp/linden07_audit_p038.png（pngmono 150dpi）
- 核对：Lemma 8.4 证明续段（`f = gh^{−1}`、`f = f_C f_U f_V`、`w = max(…)`）、公式 (8.3)（两处 `c_1^{−1}`）、`c_1 d(f_Ch, g)` 与右不变性段、`d(f_C,I_k) ≤ c_1^2 w`、`w ≥ c_1^{−3}λ^{−N}ε`、`f̃ = a^n f a^{−n}` 段与 `d(f̃, I_k) ∈ (c_3ε, r)`、末式与 QED、Lemma 8.5 陈述与两个分列、Proof 两段（`dim_box`、`λ^{−N}ε`-separated、`λ^{bN}ε^{−b}`、`a^{−N+1}F_N ⊂ K`、`(2N−1, c₂ε)`-separated、`s_{2N−1}(a)`、`(1/2)d log λ > 0`）与 QED、§9 标题、运行头
- 结果：PASS±（7 处已修复，含 1 处数学记号错误与 1 处数学定界符未闭合；其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复（数学记号错误，MD 第 1133 行）**：印刷「Suppose that **$\dim_{box}(B^U_r B^V_r x \cap K) > b > 0$** for some $x \in X$」（页图第 25 行、文本层第 46 行）；MD 原件作「Suppose that **d$\mathrm{m}_{\mathrm{box}}$** (…)，即在 `dim` 前多出一个游离的字母 `d`、并把 `\dim` 拆成 `d` + 数学模式的 `\mathrm{m}`——渲染结果为「dm_box(…)」，与印刷的 `dim_box` 不符。已改为 `$\dim _ { \mathrm { b o x } } (…`。
  2. **已修复**（MD 第 1133 行，同段）：印刷「for some $x \in X$**.** By (7.2) …」（页图第 25 行、文本层第 46–47 行）有句点；MD 原件作 `for some$x \in X$ By (7.2)` 两句粘连。已补 `$.`。
  3. **已修复**（MD 第 1119 行）：印刷「…which allows us to improve (8.3) to **$w \ge c_1^{-3}\lambda^{-N}\varepsilon$.**」（页图第 19 行、文本层第 27–29 行）行末有句点；MD 原件缺失。已补 `.$`。
  4. **已修复（缺失 QED 标记，MD 第 1124 行）**：印刷末式「$d(a^ngx, a^nhx) = d(\tilde f a^n hx, a^n hx) = d(\tilde f, I_k) \ge c_3\varepsilon$**.** □」（页图第 24 行、文本层第 36 行）在行末带证毕方块 **□**；MD 原件完全没有。已补 `.$□`。
  5. **已修复**（MD 第 1129 行，Lemma 8.5 分列 (1)）：印刷「…has box dimension zero for every $x \in X$**.**」（页图第 26 行、文本层第 41 行）行末有句点；MD 原件缺失。已补 `.$`。
  6. **已修复（重复标点，MD 第 1135 行）**：MD 原件作「…for infinitely many **$N.$**, and so…」，数学定界符内已有句点，紧随其后又补了一个逗号，形成重复标点；印刷（页图第 27–28 行、文本层第 52–53 行）为「for infinitely many **$N$,** and so…」。已改为 `infinitely many$N$, and so`。
  7. **已修复（数学定界符未闭合，MD 第 1135 行）**：MD 原件作「is`$( 2 N - 1$, c<sub>2</sub>ε)`-separated」——`$` 在 `( 2 N - 1` 之后即提前闭合，导致 `(2N−1, c₂ε` 留在数学模式而 `)` 掉到模式外，且 `c₂` 用 HTML 下标。印刷为「is **(2N − 1, c₂ε)**-separated with respect to a.」（页图第 27 行、文本层第 51 行）。已改为 `is$( 2 N - 1, c _ { 2 } \varepsilon )$-separated with respect to a`，括号整体纳入数学模式且下标用 LaTeX。
  8. MD 缺运行头「550 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  9. **print quirk 忠实保留（三处）**：① 印刷末式作「…and so **$h_{top}(a|_K) \ge \tfrac{1}{2} d\log\lambda > 0$**」（页图第 28 行、文本层第 52–54 行），其中的 `d` 是微分号（对 $\log\lambda$ 求微分）；MD 第 1135 行同样保留 `d\log\lambda`，**未按常规去掉 `d`，亦未改为 $\log\lambda$**，在此登记为印刷原样。② 印刷 Lemma 8.5 证明中由 Lemma 8.4 得到的界写作 **$c_2\varepsilon$**（页图第 26 行），而 Lemma 8.4 的陈述（印刷 p.549）用的是 **$c_3$**——常数下标前后不一致，属印刷自身记号；MD 第 1135 行保留 `c _ { 2 }`，**与印刷一致，不擅改为 c₃**。③ MD 第 1129 行 `f o r`、第 1135 行 `c<sub>2</sub>` 等字距/HTML 伪影（其中 `c<sub>2</sub>ε` 已随第 7 项一并改为 LaTeX 下标）。
  10. 行内紧排缺空格：第 1113、1119、1121、1127、1129、1131、1133、1135 行（如「Let$g , h \in B _ { r } ^ { U } B _ { r } ^ { V }$and$x \in X$be as in the lemma. Define」「We need to rule out the case that$d ( f _ { C } , \mathrm { I } _ { k } )$is the only big term」「Lemma 8.5. Let$a \in A$and$K \subset X$be compact with$a K = K$」「The restriction$a | _ { K }$of the multiplication operator a to K has positive topological entropy」「Let$g x , h x \in F _ { N }$with$g , h \in H$and$g \neq h$」）。排版级，不改。
- `f`、`w` 的分解与公式 (8.3) 逐要素核对（150dpi 页图第 7–11 行、文本层第 18–22 行；MD 第 1113、1116 行）：印刷
  「Define **$f = gh^{-1}$**, so that **$d(f, I_k) = d(g,h) \ge \lambda^{-N}\varepsilon$**. Write **$f = f_C f_U f_V$** and **$w = \max(d(f_U, I_k), d(f_V, I_k))$**. By (8.1)」
  `(8.3)  max(d(f_C, I_k), w) ≥ c_1^{−1} d(f, I_k) ≥ c_1^{−1} λ^{−N} ε.`
  ——**分解次序 `f = f_C f_U f_V` 与 max 中先 `f_U` 后 `f_V` 的次序未被调换**（调换会改变 w 的取项）、**`max` 只含两项 `(d(f_C,I_k), w)`**、`c_1^{-1}` 的两处**负指数 −1** 与 `\lambda^{-N}` 的负指数、以及三段关系符 `≥`、`≥` 的方向，编号 (8.3) 与行末句点全部吻合。
- `c_1^2` / `c_1^{-3}` 段核对（MD 第 1119 行；页图第 17–19 行、文本层第 23–29 行）：印刷「Clearly **$f_Ch = f_Ch_Uh_V$** and **$g = g_Ug_V$** are the correct decompositions in the sense of (8.1), and so **$d(f_C, I_k) \le c_1 d(f_Ch, g)$**. By right invariance of the metric $d$ we get **$d(f_Ch, g) = d(f_C, f)$** and again by (8.1) we get that **$d(f_C, f) \le c_1 w$**. We conclude that **$d(f_C, I_k) \le c_1^2 w$**, which allows us to improve (8.3) to **$w \ge c_1^{-3}\lambda^{-N}\varepsilon$**.」
  ——**两个分解式 `f_Ch = f_Ch_Uh_V` 与 `g = g_Ug_V`、等距式 `d(f_Ch, g) = d(f_C, f)`（右不变性）、以及三个幂次 `c_1`（一次）、`c_1^2`（**正指数 2**）、`c_1^{-3}`（**负指数 3**）逐一吻合**——`c_1^2` 与 `c_1^{-3}` 的符号相反是本页最易被 OCR 改错处，已逐字符确认 MD 未错。
- `f̃` 与末式核对（MD 第 1121、1124 行；页图第 20–24 行、文本层第 31–36 行）：印刷「we find either a positive or a negative $n$ with $|n| < N$ so that **$\tilde f = a^nfa^{-n} = f_C\tilde f_U\tilde f_V$** satisfies **$d(\tilde f, I_k) \in (c_3\varepsilon, r)$** for some absolute constant $c_3$. Since $hx, a^nhx \in K$, it follows that **$d(a^ngx, a^nhx) = d(\tilde f a^nhx, a^nhx) = d(\tilde f, I_k) \ge c_3\varepsilon$.**」
  ——**`\tilde f = a^nfa^{-n}` 的负指数、`f_C\tilde f_U\tilde f_V` 中三处波浪号、`d(\tilde f,I_k) \in (c_3\varepsilon, r)` 的开区间两端、末式的分解 `d(\tilde f a^nhx, a^nhx)` 与末项 `\ge c_3\varepsilon` 全部吻合**；`n` 为正或负整数且 `|n| < N`（绝对值，与 Proposition 8.3 的「非负 n」不同）在 MD 中亦正确保留。
- Lemma 8.5 陈述与证明逐要素核对（MD 第 1127–1135 行；页图第 25–28 行、文本层第 38–54 行）：印刷
  「Lemma 8.5. Let $a \in A$ and $K \subset X$ be compact with **$aK = K$**. Then one of the following properties holds.」
  「(1) The intersection **$B^U_rB^V_r x \cap K$** has box dimension zero for every $x \in X$.」
  「(2) The restriction **$a|_K$** of the multiplication operator $a$ to $K$ has positive topological entropy.」
  「Suppose that **$\dim_{box}(B^U_rB^V_r x \cap K) > b > 0$** for some $x \in X$. By (7.2) there exists a **$\lambda^{-N}\varepsilon$-separated** set $F_N$ for **$N \ge 1$**, which satisfies **$|F_N| \ge \lambda^{bN}\varepsilon^{-b}$** for infinitely many $N$.」
  「Let $gx, hx \in F_N$ with **$g, h \in H$** and **$g \neq h$**. By Lemma 8.4 there exists an integer $n$ with $|n| < N$ such that $d(a^ngx, a^nhx) \ge c_2\varepsilon$. This shows that **$a^{-N+1}F_N \subset K$** is **$(2N-1, c_2\varepsilon)$-separated** with respect to $a$. It follows that **$s_{2N-1}(a) \ge |F_N| \ge \lambda^{bN}\varepsilon^{-b}$** for infinitely many $N$, and so **$h_{top}(a|_K) \ge \tfrac{1}{2}d\log\lambda > 0$**.」
  —— **`a^{-N+1}` 的负指数（`-N+1`，而非 `-N−1`）、分离参数对 `(2N−1, c_2ε)` 的两个分量、`s_{2N-1}(a)` 的下标与 `$|F_N| \ge \lambda^{bN}\varepsilon^{-b}$` 的两处幂次、阈值 `b > 0`、以及结论的 `\tfrac{1}{2}` 系数，全部与印刷吻合**；第 1、7 两项缺陷修复后，本页所有系数/指数/上下标已与印刷一致。
- 页边界核对：印刷 p.550 止于 Lemma 8.5 证明末式 + QED 方块（页图末两行、文本层第 52–54 行）；MD 第 1135 行对应结束，§9 上半连续性段的其余内容属 p.551，留待 p.039 核对，无跨页错接。

## p.039（PDF p.39 / 印刷 p.551）
- PNG：/tmp/linden07_audit_p039.png（pngmono 150dpi）
- 核对：§9 标题与开篇大段（`lim sup_{ℓ→∞} h_{μ_ℓ}(a) ≤ h_μ(a)` 与 `lim_{ℓ→∞} μ_ℓ = μ` 两式、`[49, Thm. 8.2]`、`[31, Thm. 4.1]`、`[49, §8.1]`、`[49, Ch. 4]`、`[34, Ch. 2 and 4]`）、原子定义式（两个 ⋂ 及条件）、条件测度 `μ_x^𝒜` 句、条件熵定义式、加法公式、精细化不等式、消失判据句、可逆情形与 `h_μ(T,Q)` 公式、`[49, Thm. 4.14]`、运行头
- 结果：PASS±（2 处已修复，含 1 处数学箭头缺失；其余差异为字形/排版级，不误导）
- 差异列表：
  1. **已修复（数学箭头缺失，MD 第 1169 行）**：印刷「Suppose **$T : Y \to Y$** is measure preserving and invertible.」（页图第 22 行、文本层第 41 行）在 Y 与 Y 之间有映射箭头 `\to`；MD 原件作 `$T : Y  Y$`——**箭头整体丢失，渲染成「T : Y Y」**。已补 `\to`（`hexdump -C` 复核第 16–17 字节为 `5c 74 6f` = `\to`）。
  2. **已修复**（MD 第 1167 行）：印刷「…is contained in one of the elements of $\mathcal{P}$ for every $x \in Y \setminus N$**.**」（页图第 20–21 行、文本层第 38–40 行）行末有句点；MD 原件缺失。已补 `.$`。
  3. MD 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 551」（页图首行 + 文本层第 1 行）。系统性伪影，登记不改。
  4. 字形伪影：MD 第 1150、1155、1158、1167 行用 `\mathsf{H}`；第 1164 行用 `\mathrm{H}`（与前几式的 `\mathsf` 不一致）。数学对象相同，排版级，不改。
  5. 行内紧排缺空格：第 1141、1147、1153、1155、1161、1167、1169、1175 行（如「Let$\mu$be a probability measure on a compact metric space Y. Let$A \subset B _ { Y }$ be」「and the conditional measure$\mu _ { x } ^ { \mathcal { A } }$is a probability measure supported on」「For the trivial σ-algebra$\mathcal { N } = \{ \emptyset , Y \}$the conditional entropy」「If$\mathcal { P }$is finer than$\mathcal { Q }$and」「Suppose$T : Y \to Y$is measure preserving and invertible」）。排版级，不改。
- 上半连续性两式核对（150dpi 页图第 7–8 行、文本层第 9–10 行；MD 第 1139 行）：印刷「We will show that **$\lim\sup_{\ell\to\infty} h_{\mu_\ell}(a) \le h_\mu(a)$** whenever $\mu_\ell$ is a sequence of $a$-invariant measures satisfying **$\lim_{\ell\to\infty}\mu_\ell = \mu$**.」—— **第一式为 `lim sup`、第二式为 `lim`（一为上极限、一为极限，MD 第 1139 行分别写 `\operatorname* { s u p } _ { \ell \to \infty }` 与 `\operatorname* { l i m } _ { \ell \to \infty }`，未互换）**；两个式子的下标序列均为 `\ell`、极限变量 `\ell \to \infty`，`h_{\mu_\ell}(a)` 的双下标与 `h_\mu(a)` 的单下标区分正确。
- 引文链核对（MD 第 1139 行）：印刷「for expansive maps **[49, Thm. 8.2]** and also for $C^\infty$ automorphisms of compact manifolds **[31, Thm. 4.1]**…the proof for the expansive case in **[49, §8.1]**…see **[49, Ch. 4]** and **[34, Ch. 2 and 4]**」——**五个引文标记的文献号与定位（Thm. 8.2、Thm. 4.1、§8.1、Ch. 4、Ch. 2 and 4）逐一吻合**；`C^\infty` 的指数 ∞ 亦正确。
- 原子定义式逐要素核对（150dpi 页图第 11 行、文本层第 22–25 行；MD 第 1144 行）：印刷 `[x]_𝒜 = ⋂_{i: x∈A_i} A_i ∩ ⋂_{i: x∉A_i} X \ A_i,` —— **两个 ⋂ 的下标条件 `x ∈ A_i` 与 `x \notin A_i` 未被混同**（混同会使原子定义退化），交/差的类型 `∩` 与 `\` 正确，上标 `\mathcal{A}` 与下标 `[x]` 位置正确，行末逗号在位。
- 条件熵定义式核对（MD 第 1150 行；页图第 13 行、文本层第 28–30 行）：印刷 `H_μ(𝒫|𝒜) = ∫ H_{μ_x^𝒜}(𝒫) dμ` —— **被积项的下标 `μ_x^𝒜` 同时含下标 x 与上标 𝒜**（若漏掉 𝒜 会丢失条件测度的定义依赖），右端微元 `dμ` 正确，MD 与印刷**逐字符吻合**。
- 加法公式与精细化不等式核对（MD 第 1158、1164 行；页图第 15–17 行、文本层第 35–37 行）：印刷
  `H_μ(𝒫 ∨ 𝒬|𝒜) = H_μ(𝒫|𝒜) + H_μ(𝒬|𝒫 ∨ 𝒜).`
  `H_μ(𝒬|𝒜) ≤ H_μ(𝒫|𝒞).`
  —— **两式中的连接符 `∨` 共出现三次（`𝒫∨𝒬`、`𝒬|𝒫∨𝒜`）且位置全部正确**，条件测度标记 `|` 的左右参数（`𝒫|𝒜` 与 `𝒬|𝒞`）未被互换，第二式的不等号方向 `≤` 正确；右端出现的 `𝒞`（而非左端的 `𝒜`）与印刷一致。
- 消失判据句核对（MD 第 1167 行；页图第 18–21 行、文本层第 38–40 行）：印刷「the conditional entropy $H_\mu(\mathcal{P}|\mathcal{A})$ vanishes if and only if there exists a nullset $N$ such that **$[x]_A \setminus N$** is contained in one of the elements of $\mathcal{P}$ for every **$x \in Y \setminus N$**」—— **全集差 `[x]_A \ N` 与点集差 `x ∈ Y \ N` 两处方向正确**，`\setminus` 未被误写成 `\cap`，「当且仅当」的必要充分双向未丢失。
- 末式核对（MD 第 1172 行；页图第 25 行、文本层第 43–46 行）：印刷 `h_μ(T, 𝒬) = H_μ(𝒬 | ⋁_{n=1}^∞ T^{−n}𝒬);` —— **大 ⋁ 的下限 `n = 1` 与上限 `∞`、`T^{−n}` 的负指数、`𝒬` 作为被作用对象、以及行末分号全部吻合**；紧随的「see [49, Thm. 4.14].」（MD 第 1175 行）与印刷的文献号、章号、句末句点均一致。
- 页边界核对：印刷 p.551 止于「see [49, Thm. 4.14].」（页图末行、文本层第 46 行）；MD 第 1175 行对应结束，§9 的证明续文属 p.552，留待 p.040 核对，无跨页错接。
