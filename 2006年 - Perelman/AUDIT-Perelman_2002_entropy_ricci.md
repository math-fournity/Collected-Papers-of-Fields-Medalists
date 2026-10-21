# 逐页审计：The entropy formula for the Ricci flow and its geometric applications

- actor=Peer-P05; model=gpt-6-luna; effort=max
- 身份类别：Peer 候选审计记录；canonical integrator 为 Master-Luna。此文件与提交尚未由 Master 集成。
- 基线：`e04c4a9603818cfa2d71271942f696115783c33b`（工作树 HEAD；detached）。
- PDF：`Perelman_2002_entropy_ricci.pdf`；39 页；SHA-256 `945e278613c45ea1ab617b28c3095783d0e68958dc0546dfcfa9b42b9674fbe1`。
- 审计对象 MinerU Markdown：`Perelman_2002_entropy_ricci_mineru/Perelman_2002_entropy_ricci__Perelman_2002_entropy_ricci.md`；审计前 SHA-256 `2e048e359da9b28283294b6639103b039718b281ed3965548141a58b01a1f416`。
- MinerU 导出：`docvortex.middle` / `structured_content`，schema 2.0，producer MinerU 3.4.4，39 页；已检查的导出元数据未提供 `doc_id` 字段（未知，未推断）。
- 模式：born-digital。Poppler `pdftotext -layout` 提取 106,888 字节，0 个 U+FFFD；PDF Creator `dvips(k) 5.86`、Producer `GPL Ghostscript 10.01.2`。逐页签认以 PDF 文本层与对应 Markdown 内容逐页核对，题录页及密集数学页另用 150dpi 整页 PNG 抽验；文本层丢失或压平的字形回到原页图裁决。
- 范围边界：核对印刷文本、题录、段落、公式表示、编号、脚注与参考文献的转录忠实度；不独立验证论文中的数学命题。全部页面签认后再修复 Markdown。

## p.001/39（PDF p.1 / 印刷 p.1）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T15:52:28-04:00
- PNG：`audit/entropy_ricci/p001.png`（pngmono，150dpi；题录页整页目检）。
- 核对：左边 arXiv 标识、题名、作者、居中日期、Introduction 标题、开篇 Ricci flow 方程及正文首段/作者脚注；对照 PDF p.1 文本层与 MinerU Markdown 第 1、3、5、7、9 行。
- 结果：FAIL。除页边的 arXiv 标识及印刷页码 1 未收录外，标量曲率公式中的 Ric 被 Markdown 拆成 R i c；PDF p.1 文本层与 p001.png 显示印刷为 Ric。其余本页核对内容吻合，行间公式在 Markdown 中保留了结构。
- 源级 quirk：同一印刷页左边 arXiv 标识为 `arXiv:math/0211159v1 [math.DG] 11 Nov 2002`，居中日期却印为 `November 26, 2024`；Markdown 忠实保留居中日期。按印刷原文优先规则登记此原件内部日期差异，不作修正。

## p.002/39（PDF p.2 / 印刷 p.2）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T15:59:39-04:00
- PNG 裁片：`audit/entropy_ricci/300dpi/p002_text_glyphs.png`（PDF p.2，pnggray，300dpi；核对 `[H 4, §26]`、`t → ∞` 及原文拼写）。
- 核对：Introduction 首段跨页续文、Hamilton 收敛定理段、微分 Harnack 段、颈缩与手术段；对照 PDF p.2 文本层及 MinerU Markdown 第 9、13、15 行。
- 结果：FAIL。Markdown 有 `difeomorphisms`、`diferential`、`diferent`（两处）、`suficient`；印刷分别为 `diffeomorphisms`、`differential`、`different`、`sufficient`。式 `$t  \infty$` 丢失印刷的趋于箭头 `t → ∞`；引文 `[H 4, 26]` 丢失印刷的节号符号 `§`。这些差异均由 p.2 原文文字层确认；300dpi 裁片进一步确认符号与上下文。Markdown 未保留印刷页码 2。
- 源级 quirk：PDF p.2 印作 `a priory assumptions`；文字层与 300dpi 裁片一致。Markdown 同样如此，按 print 保留，不改成 `a priori`。

## p.003/39（PDF p.3 / 印刷 p.3）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:03:28-04:00
- PNG 裁片：`audit/entropy_ricci/300dpi/p003_kahler.png`（PDF p.3，pnggray，300dpi；核对 Kähler 的变音符）。
- 核对：Hamilton 手术计划段结尾、Hamilton–Tian 说明、Ricci flow 与 RG flow 段、全文结构导读开头与 subsection/References 说明；对照 PDF p.3 文本层及 MinerU Markdown 第 15、17、19、21、23、25、27–33 行。
- 结果：FAIL。Markdown 的 `$t$` 后缺印刷 `→ ∞`；`[Gaw, 3]` 及结构导读中 §1–§13 的多处章节引用均漏掉印刷符号 `§`；`insuficient`、`diferent`、`diferential`、`difeomorphisms` 分别漏写 `f`；两处 `K¨ahler` 将印刷的 `Kähler` 变音符放错位置。300dpi 裁片确认两处印刷字形均为 `Kähler`。另见 Markdown `expressions ,` 的空格伪影，属不影响含义的格式瑕疵，暂不列为内容修复。
- 页码：印刷页码 3 未保留在 Markdown。

## p.004/39（PDF p.4 / 印刷 p.4）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:05:58-04:00
- PNG：未单独保存；born-digital 主通道为 PDF 文本层逐页对账，本页不属于 150dpi 图像抽验页。
- 核对：论文结构导读后半（§2–§13 的段落说明）、subsections 星号说明与 `[Cao-C]` 引文；对照 PDF p.4 文本层及 MinerU Markdown 第 29、31、33 行。
- 结果：FAIL。PDF p.4 在导读中多次印有章节符号 `§`（如 `§2`、`§3`、`§4`…`§10`、`§11`、`§12`、`§13`），Markdown 对应位置只留数字，导致章节引用符号丢失。导读句子与章节顺序其余部分对应；未发现段落缺失。Markdown 未保留印刷页码 4。

## p.005/39（PDF p.5 / 印刷 p.5）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:06:59-04:00
- PNG：`audit/entropy_ricci/p005.png`（pngmono，150dpi；密集数学页整页抽验之一）。
- 核对：§1 标题、泛函 `F` 与第一变分、`1.2` Proposition、演化方程及编号 (1.1)–(1.3)；对照 PDF p.5 文本层与 MinerU Markdown 第 35、37、40、43、45、47、50、56、59、62 行，并目检 150dpi 页图中的公式结构与编号位置。
- 结果：FAIL。Markdown 第 43 行两处 `difeomorphism` 对应印刷 `diffeomorphism`，另有 `diferent choices` 对应印刷 `different choices`；属于 `ff` 字形转录遗漏。其余本页核对的公式、上下标、积分、梯度与 (1.1)–(1.3) 编号均吻合。Markdown 未保留印刷页码 5。

## p.006/39（PDF p.6 / 印刷 p.6）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:11:40-04:00
- PNG：`audit/entropy_ricci/p006.png`（pngmono，150dpi；第二张密集数学整页抽验图）。疑点裁片：`audit/entropy_ricci/300dpi/p006_trace_and_refs.png`（pnggray，300dpi）。
- 核对：(1.4) 与随后的单调性不等式；Remark 1.3 的加权 Bochner–Lichnerowicz 公式、迹恒等式及 Bianchi 恒等式；星号历史注记和 §6 引文；§2 标题及 2.1 breather 定义开头。对照 PDF p.6 文本层、150dpi 整页和 300dpi 裁片，以及 Markdown 第 65–89 行。
- 结果：FAIL。Markdown 将迹恒等式中的印刷下标 `R_{ij}^{m}` 记作 `R_{ii}^{m}`；星号注记编号印作 `1.4*`，Markdown 写成 `1·4*`；`[H 4, §6]` 与 `[D, §6]` 均漏掉 `§`。另有 `efective`→印刷 `effective`、`difeomorphism`→`diffeomorphism`、`difer only`→`differ only`。300dpi 裁片确认 `R_{ij}^{m}` 指标、`1.4*` 标点及两处节号符号；式 (1.4)–不等式及其余核对的公式结构与编号吻合。Markdown 未保留印刷页码 6。

## p.007/39（PDF p.7 / 印刷 p.7）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:15:38-04:00
- PNG 裁片：`audit/entropy_ricci/300dpi/p007_weight.png`（PDF p.7，pnggray，300dpi；核对 λ 定义中的测度权重）。
- 核对：2.1 trivial breather / Ricci soliton 定义续文、Gaussian soliton；2.2 的 λ 特征值定义；2.3 的单调性主张与导数不等式。对照 PDF p.7 文本层与 MinerU Markdown 第 89–113 行，并以裁片复核 `e^{-f}` 指数。
- 结果：FAIL。Markdown 将 λ 定义中的积分权重写成 `e^{-\check{f}}`，印刷为 `e^{-f}`；300dpi 裁片确认无 `\check{}`。另外 `difer only` 对应 `differ only`（漏 `f`），`difeomorphism` 两处对应 `diffeomorphism`，`dificult` 对应 `difficult`。其余核对的 (2.2) 定义、尺度不变量及导数不等式结构与 PDF 相符。Markdown 未保留印刷页码 7。

## p.008/39（PDF p.8 / 印刷 p.8）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:18:35-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p008_heat_operator.png（PDF p.8，pnggray，300dpi；核对共轭热算子的方框星号及 (3.4) 公式）。
- 核对：2.4 等号情形证明、2.5* 引文、§3 标题、W 泛函定义与约束、演化方程 (3.3)、共轭热算子定义及单调性公式 (3.4)；对照 PDF p.8 文本层和 MinerU Markdown 第 115–145 行。
- 结果：FAIL。印刷引文 [H 6, §2] 在 Markdown 中缺少 §。印刷句为 Clearly W is invariant，Markdown 漏掉主语 W。印刷共轭热算子符号为 □*，Markdown 分别误识为 Ξ* 与 Π*；300dpi 裁片确认印刷字形为方框加星号。其余 (3.1)–(3.4) 的积分、指数、上下标与编号对应。Markdown 未保留印刷页码 8。

## p.009/39（PDF p.9 / 印刷 p.9）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:24:47-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p009_limit_and_integral.png（PDF p.9，pnggray，300dpi；核对“converge”附近引号及归一化高斯权重）。
- 核对：μ/ν 定义与极限、3.1 Claim 证明、缩放度量与归一化积分、不等式及 3.2 Remark；对照 PDF p.9 文本层与 MinerU Markdown 第 147–177 行。
- 结果：FAIL。原文 “Now let τ → 0” 的趋于箭头在 Markdown 中丢失；归一化因子原文为 (2π)^(-n/2)，Markdown 错作 (2π̄)^(-n/2)，300dpi 裁片确认 π 上无横线；“efforts” 被写为 “eforts”，漏一个 f。其余核对的缩放泛函及 (3.2)–(3.4) 相关表达吻合。Markdown 未保留印刷页码 9。源页 “converge” 两侧均印作右双引号，Markdown 忠实保留，按源级 quirk 记录、不改。

## p.010/39（PDF p.10 / 印刷 p.10）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:26:31-04:00
- PNG：audit/entropy_ricci/p010.png（整页，150dpi）及 audit/entropy_ricci/300dpi/p010_volume.png（核对公式中的 Vol 字样）；born-digital 主通道仍为 PDF 文本层逐页对账。
- 核对：4.1 反证证明（塌缩球、μ 趋于负无穷及单调性矛盾）、4.2 κ-noncollapsed 定义、尺度缩放关系及闭流上的尺度结论；对照 PDF p.10 文本层及 Markdown 第 181–185 行。
- 结果：FAIL。Markdown 在 4.1 定义与证明中三处把印刷 Vol 拆写为 V o l，并将 dist_{t_k} 写成 d i s t_{t_k}；PDF p.10 整页与 300dpi 裁片确认印刷为 Vol、dist。原先从 Markdown 第 177 行记录的一个 Vol 间距瑕疵属于 PDF p.10，应在本页归属。Markdown 未保留印刷页码 10。PDF p.10 在 “for all t ∈ [0,T)” 处结束，下一句在 p.11 续接，Markdown 将该段落连续排在后续行中。

## p.011/39（PDF p.11 / 印刷 p.11）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:29:05-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p011_curvature_bound.png（PDF p.11，pnggray，300dpi；核对曲率界 Q_k 的指数位置）。
- 核对：§4 Corollary 的曲率假设与极限结论；§5 标题、canonical ensemble 分区函数/熵/涨落公式、流上的能量熵公式及段末转页；对照 PDF p.11 文本层与 MinerU Markdown 第 187–213 行。
- 结果：FAIL。§4 Corollary 的印刷条件是 |Rm|(x,t) ≤ C Q_k；Markdown 在 Q_k 后多出一个孤立的 2。300dpi 裁片确认印刷无平方指数。Markdown 把两处 “of” 分别拆坏（“a subsequence o f the scalings” 与 “scalings o f g_ij”）；印刷两处均为完整单词。§5 引言漏掉印刷中的泛函名称 W（“the functional W, introduced…”）；页末 “sufficiently” 漏写一个 f。Markdown 未保留印刷页码 11。

## p.012/39（PDF p.12 / 印刷 p.12）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:31:50-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p012_rimannian_quirk.png（PDF p.12，pnggray，300dpi；仲裁原文中的 Rimannian 拼写）。
- 核对：5.1 末尾熵的非负性、τ 趋零/趋无穷陈述、5.2/5.3*、§6 标题、6.1 扩维度量及 6.2 度量构造开头；对照 PDF p.12 文本层及 MinerU Markdown 第 213–244 行。
- 结果：FAIL。Markdown 在三处删掉趋于箭头：τ→0（两处）与 τ→τ_i>0；另将 sufficiently 写作 suficiently。p.12 的 6.2 首句中一处 diffeomorphism 被写作 difeomorphism，且 “apply to g̃ a (small) diffeomorphism” 的 a 被包装为不必要的 mathrm{~a~}；随后 “horizontal diffeomorphism” 位于 PDF p.13，将在 p.13 条目中核记。5.3* 脚注/小节标识拆入数学文本（当前写为 “5.$3^{*}$”），虽然可辨认但不利于定位，计划改为可检索的普通文本标识。源级 quirk：正文印作 “Rimannian geometry”（漏 e），300dpi 裁片确认；Markdown 忠实保留，不改。Markdown 未保留印刷页码 12。

## p.013/39（PDF p.13 / 印刷 p.13）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:34:55-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p013_geodesics.png（PDF p.13，pnggray，300dpi；核对最短测地线长度积分）。
- 核对：§6.1 曲率张量/热方程说明收尾；6.2 水平微分同胚与其余度量分量；6.3 最短测地线长度积分。对照 PDF p.13 文本层和 MinerU Markdown 第 233–256 行；p.13 页图确认长度积分及其被积函数。
- 结果：FAIL。6.2 的 “horizontal diffeomorphism” 在 Markdown 写成 “horizontal difeomorphism”，漏一个 f。其余本页核对的度量分量、超曲面体积/标量曲率表达及长度积分与印刷页吻合。印刷页码 13 未保留。PDF p.13 在长度积分后结束；渐近展开式从 p.14 开始，不计入本页核对范围。

## p.014/39（PDF p.14 / 印刷 p.14）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:38:02-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p014_L_length.png（PDF p.14，pnggray，300dpi；核对 7.1 的 L-length 印刷符号）。
- 核对：6.3 的渐近展开、约化体积表达与单调性说明；6.4* 解释；§7 标题、7.1 的 L-长度定义与第一变分导入。对照 PDF p.14 文本层和 MinerU Markdown 第 260–289 行。
- 结果：FAIL。7.1 印刷写作 “associate its ℒ-length”，Markdown 在 “its” 后遗漏 ℒ（现为 “its -length”）。300dpi 裁片确认印刷符号为花体 ℒ。其余核对的展开式、约化体积、§7 的参数区间、L-长度积分及 δ_Y(ℒ) 引入吻合。Markdown 未保留印刷页码 14；PDF p.14 在 δ_Y(ℒ)= 处结束，展开公式在 p.15。

## p.015/39（PDF p.15 / 印刷 p.15）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:40:23-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p015_L_shortest.png、audit/entropy_ricci/300dpi/p015_L_geodesic.png（PDF p.15，pnggray，300dpi；核对 ℒ-shortest / ℒ-geodesic 记号与 τ→0）。
- 核对：§7 第一变分公式 (7.1)、ℒ-geodesic 方程 (7.2)、约化长度 L 的梯度与时间导数关系，以及演化恒等式 (7.3)；对照 PDF p.15 文本层和 300dpi 裁片、Markdown 第 292–312 行。
- 结果：FAIL。Markdown 在 7.1 文字中漏掉 ℒ-shortest/L-geodesic 记号的花体 ℒ：如 “Thus -geodesics”、“an -shortest curve”、“every such -shortest curve”；又把印刷的 “ℒ-geodesic” 写成了带下标/上标的 “L_C^- geodesic”。同段还丢失 τ→0 的箭头。裁片确认这些位置均为花体 ℒ 且印有趋于箭头。式 (7.1)–(7.3) 的运算式与编号吻合。Markdown 未保留印刷页码 15；PDF p.15 在 (7.3) 后结束，Harnack 表达 H 的说明从 p.16 开始。

## p.016/39（PDF p.16 / 印刷 p.16）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:41:44-04:00
- PNG：未单独保存；born-digital 主通道为 PDF 文本层逐页对账，本页不属于 PNG 抽验页。
- 核对：Harnack 表达式 H 的说明、(7.4)–(7.6)、二阶变分展开、导数恒等式、(7.7) 与 ODE (7.8)；对照 PDF p.16 文本层和 MinerU Markdown 第 315–357 行。
- 结果：FAIL。PDF 在二阶变分展开结束后另起正文单词 “Now”，引出 d/dτ 恒等式；Markdown 将一个额外的 “Now” 塞进前一数学 array（\text{Now}），又在下一行重复正文 “Now”。(7.4)–(7.8) 的已核公式结构与编号相符。Markdown 未保留印刷页码 16；p.16 在 (7.8) 后结束。

## p.017/39（PDF p.17 / 印刷 p.17）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:43:15-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p017_jacobi.png（PDF p.17，pnggray，300dpi；核对 ℒ-geodesic / ℒ-Jacobi 记号）。
- 核对：ODE 解的长度关系与 Hessian 上界；(7.9)、Hamilton 矩阵 Harnack 表达 H(X,Y)、(7.10)；末尾 ℒ-Jacobi 场定义。对照 PDF p.17 文本层、300dpi 裁片与 MinerU Markdown 第 362–395 行。
- 结果：FAIL。末段多处花体 ℒ 遗失：Markdown 写成 “-geodesic”、“-Jacobi”、“-geodesics”；原文均为 ℒ 前缀。原文末句是 “For an ℒ-Jacobi field Y”，Markdown 将该标识误作带 “-,1” 的 ℒ_{-,1}。300dpi 裁片确认原文各处为花体 ℒ 且没有 “-,1” 下标。式 (7.9)–(7.10) 及 H(X,Y) 中各项按文本层核对吻合。Markdown 未保留印刷页码 17；PDF p.17 在 “|Y(τ̄)|=1 we have” 处结束。

## p.018/39（PDF p.18 / 印刷 p.18）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:46:26-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p018_L_map.png、audit/entropy_ricci/300dpi/p018_reduced_distance.png（PDF p.18，pnggray，300dpi；核对 ℒ 指标和 geodesic 记号）。
- 核对：(7.11) Jacobi 场估计、(7.12) Jacobian 界、约化距离导数、(7.13)–(7.15) 约化体积/拉普拉斯不等式；对照 PDF p.18 文本层和 MinerU Markdown 第 395–439 行。
- 结果：FAIL。Markdown 在 “Ỹ is … Jacobi” 处漏 ℒ；“L-exponential map” 之前漏 ℒ；把 “ℒ-geodesic” 写成带多余负号下标的 ℒ₋-geodesic；“along an ℒ-geodesic” 的连接标点错误；“along γ” 误加下标冒号；“differential” 写作 “diferential”。全篇源文本复扫还发现 p.18 的两条公式及 Harnack 说明中三处 “Ric” 被字母间插空格；“as τ→0” 漏箭头。裁片确认原文 Jacobian map 及 geodesic 前缀为花体 ℒ，且没有额外负号下标；PDF p.18 文本层确认 Ric 与 τ→0。式 (7.11)–(7.15) 其余核对部分与文本层一致。Markdown 未保留印刷页码 18；p.18 在 “The lower bound for” 处转页。

## p.019/39（PDF p.19 / 印刷 p.19）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:47:47-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p019_L_tags.png、audit/entropy_ricci/300dpi/p019_volume.png（PDF p.19，pnggray，300dpi；核对 ℒ-Jacobi、ℒ-exponential、ℒ-geodesic 记号和 Vol 字样）。
- 核对：7.2 的曲率算子/Harnack 界与 (7.16)–(7.17)；7.3 的局部塌缩推论证明（缩放/体积参数、ℒ-exponential map、轨迹段及约化体积比较），对照 PDF p.19 文本层与 MinerU Markdown 第 441–455 行。
- 结果：FAIL。Markdown 把 “differential Harnack” 写作 “diferential Harnack”；“for ℒ-Jacobi fields”、“using the ℒ-exponential map” 和 “give rise to ℒ-geodesics” 中的花体 ℒ 均缺失。全篇源文本复扫还发现 p.19 的 Ric 公式被字母间插空格，约化体积定义中的 Vol 被拆为 “V o l”；p019_volume.png 确认印刷为 Vol。其余 (7.16)–(7.17) 参数幂次、指数与比较关系吻合。Markdown 未保留印刷页码 19。

## p.020/39（PDF p.20 / 印刷 p.20）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:51:36-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p020_lemma_distances.png、audit/entropy_ricci/300dpi/p020_ball_radius_quirk.png（PDF p.20，pnggray，300dpi；核对距离下标与局部塌缩定义的球半径）。
- 核对：7.4* 变分理论注记；8.1 κ-collapsed 定义；8.2 定理及反证开头；8.3 Lemma (a) 的距离/曲率条件与 barrier inequality。对照 PDF p.20 文本层和 MinerU Markdown 第 457–475 行。
- 结果：FAIL。Markdown 在 8.2 证明中把印刷的 dist_{1/2}(x,x0) 写成 “dis⟂_{1}(x,x0)”（dist 字符串与 1/2 下标均损坏）；300dpi 裁片确认原文是 dist_{1/2}。8.3(a) 多处 Ric / dist 被拆成字母间空格，且 differential 漏一个 f；8.2 中 “efficiently” 也写作 “eficiently”，8.1 中 “if” 被拆成 “i f”，均由文本层及原页可复核。源级 quirk：8.1 定义印作球 B(x0,r²)（尺度文字为 r），300dpi 裁片确认确有平方；Markdown 忠实保留，不按量纲预期改正。Markdown 未保留印刷页码 20。

## p.021/39（PDF p.21 / 印刷 p.21）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T16:54:27-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p021_distance_lemma.png、p021_maximum_principle.png、p021_operator.png（均为 PDF p.21，pnggray，300dpi；核对 8.3 距离/曲率条件、h 的距离函数、2n+1 与方框算子）。
- 核对：8.3(b) 距离速度估计；Lemma (a) 的 d_t / Δd 变分界；续写定理证明中的 h、(8.1)–(8.4) 及 barrier inequality。对照 PDF p.21 文本层、三张 300dpi 裁片与 MinerU Markdown 第 477–510 行。
- 补核时间（America/New_York）：2026-10-01T16:57:28-04:00；actor=Peer-P05; model=gpt-6-luna; effort=max。此前页内签认已提交，补核将 p.21 覆盖范围补足到印刷页末。
- 结果：FAIL。Markdown 的 [H 4, §17] 漏掉 §；公式末尾的 “at t=t0” 被写成 “a t t=t0”；8.3(b) 的 Ric、dist 及证明中的 Ric、dist 被拆成字母间空格。8.2 定理续证的距离函数 d(y,t)=dist_t(x,x0) 被写成 disΦ_U(x,x0)，且 h(x,1)=2n+1 被误编码成带上划线加号的表达式；300dpi 裁片确认印刷为 dist_t(x,x0) 和普通 2n+1。式 (8.1)–(8.4) 其余核对项吻合，方框算子与 Markdown 的 Box 符号相符。源级 quirk：证明印作 d(x1,t0)=r0（第二参数是 t0 而非 x0），300dpi 原页确认如此，忠实保留；h 定义印作 d(y,t)=dist_t(x,x0)，保留源页中的 x。Markdown 未保留印刷页码 21。

## p.022/39（PDF p.22 / 印刷 p.22）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:01:01-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p022_conjugate_operator.png、p022_heat_integrals.png、p022_or_spacing.png（PDF p.22，pnggray，300dpi；核对共轭热算子、hu 积分及 “M,or” 印刷间距）。
- 核对：8.2 最大值论证收尾与 (8.2)–(8.4)；§9 标题、9.1 Proposition 及 (9.1)、9.2/9.3 Corollaries、9.4 不等式 (9.2)；对照 PDF p.22 文本层与 MinerU Markdown 第 513–543 行。
- 结果：FAIL。§9 标题的 “Differential” 写成 “Diferential”，漏一个 f。9.1 共轭热算子在 Markdown 误写为 Π*，印刷为 □*；300dpi 裁片确认方框星号。9.3 的积分把印刷普通标量 u 写成粗体 u；裁片确认为普通斜体 u。9.2 的 M,or 在 Markdown 被拆成 “M , o r”；源页确实印成逗号后无空格的 “M,or”，按印刷保留该源级间距异常，但应去掉 OCR 插入的字母内空格。其余 9.1、9.2 与 (9.2) 的符号/系数匹配。Markdown 未保留印刷页码 22。

## p.023/39（PDF p.23 / 印刷 p.23）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:05:02-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p023_heat_operators.png、p023_f_time.png、p023_boundary_volume.png（PDF p.23，pnggray，300dpi；核对 □/□*、f_t、∂Ω）。
- 核对：9.4 证明的演化不等式；9.5 约化距离推论；9.6 热算子、伴随算子与特征解近时条件；9.7 历史说明；10.1 伪局部性定理的初始体积假设。对照 PDF p.23 文本层、裁片及 MinerU Markdown 第 545–557 行。
- 结果：FAIL。9.5 中原文 □* 被 Markdown 识作 `Σ*`。9.6 的热算子 `\bigsqcup`、伴随 `\bar{\sqcup}^*`，以及积分分部式中的 `d\Pi`/`d\Pi^*` 均不符印刷的 □/□* 记号；近时条件两处将方框算子写作 `\sqsupset` 或 `\bigtriangledown`。原页裁片确认为空方框及其星号；f̄/t 分式则与印刷相符，非错误。9.7 两处 “differential” 被写成 “diferential”；10.1 的 Vol(∂Ω) 被误识为带横线的 ∂Ω，裁片确认无横线。Markdown 未保留印刷页码 23。

## p.024/39（PDF p.24 / 印刷 p.24）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:10:50-04:00
- PNG：未单独保存；born-digital 主通道为 PDF 文本层逐页对账，本页不属于 PNG 抽验页。
- 核对：10.1 定理后的解释、反证证明概要、尺度归一化与 Claim 1 构造；对照 PDF p.24 文本层及 MinerU Markdown 第 559–579 行。
- 结果：FAIL。Markdown 将印刷的 cut-off 写成 cut-of（漏 f）；球记号 B(x0,r0) 的逗号丢失；“Or ,”在逗号前插入空格。Claim 1 起句的 “if” 还被拆成 “i f”。其余本页核对的尺度、曲率阈值、量词与不等式结构吻合。Markdown 未保留印刷页码 24；p.24 在 Claim 1 的 d(x_k,t_k) ≤ (2A + 处结束，下一页续接。

## p.025/39（PDF p.25 / 印刷 p.25）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:15:02-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p025_claim3.png（PDF p.25，pnggray，300dpi；核对 “Proof of Claim 3 (sketch)” 标签）。
- 核对：Claim 1 末尾续句、Claim 2 命题及证明、反证序列的 ε/δ 极限、Claim 3 与其 sketch 开头；对照 PDF p.25 文本层和 MinerU Markdown 第 577–603 行。
- 结果：FAIL。反证步骤中印刷 “ε→0, δ→0”，Markdown 写成 ε、δ 后直接跟 0，箭头缺失。印刷 “Proof of Claim 3 (sketch)” 被 OCR 误作 “Proof of Claim 𝓑 (s k e t c h)”；300dpi 裁片确认编号为 3、单词为 sketch。Claim 3 sketch 的其余参数与极限论证对应。Markdown 未保留印刷页码 25；本页在 “flat man-” 断词处转页。

## p.026/39（PDF p.26 / 印刷 p.26）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:18:58-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p026_heat_cutoff.png、p026_entropy_bound.png、p026_sign_anomaly.png（PDF p.26，pnggray，300dpi；核对方框热算子、截断 annulus、归一化指数及两条印刷估计式的符号差异）。
- 核对：Claim 3 injectivity-radius 分支结尾；cut-off 函数 h 与热算子积分估计；熵/对数 Sobolev 矛盾；10.2 体积下界 Corollary。对照 PDF p.26 文本层、两张裁片及 MinerU Markdown 第 603–621 行。
- 结果：FAIL。Markdown 将 cut-off 写成 cut-of；Box h 的三处输出分别误作 \boxed{1}h、\boxed{d\Omega}h、Theta h，300dpi 裁片确认印刷均为方框算子 h；归一化指数把 n 误成 i；积分中的普通 v 误作粗体 v；annulus 的 B\setminus B 被误成带左箭头的球；\bar h 定义多一个右括号；10.2 Corollary 与说明括号间缺空格。p.26 若干数字也在单个数值内部插入空格（10A、20A、100n、100\epsilon^2 等），300dpi 裁片支持按连续数值修复。源级 quirk：同页注记确印 d_t−Δt（而邻近 h 公式印 d_t−Δd），照 print 保留；“we”ll” 的弯引号也照印保留。另一个原件内部符号差异也照录：中间估计式印为 \([-\bar t|\nabla\tilde f|^2-\tilde f-n]\)，其后对数 Sobolev 表达式印为 \([-\frac12|\nabla f|^2-f+n]\)，未按数学预期统一符号。Markdown 未保留印刷页码 26。

## p.027/39（PDF p.27 / 印刷 p.27）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:22:59-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p027_volume_diffeo.png（PDF p.27，pnggray，300dpi；核对 Vol 符号、diffeo 拼写）。
- 核对：10.3 伪局部性定理、10.4 Corollary 体积条件、10.5 Cheeger finiteness remark、10.6*、§11.1 古解假设及 trace Harnack 公式 (11.1)；对照 PDF p.27 文本层和 MinerU Markdown 第 623–641 行。
- 结果：FAIL。10.3 中印刷 Vol 被 MinerU 拆写为 “V ol”，10.4 的两个印刷 Vol 字样也被拆坏，其中一个另将字母 o 误作带点字形；300dpi 裁片确认原页均为普通 Vol。10.5 缩写 “diffeo finiteness theorem” 与印刷相符，并非拼写错误；§11.1 “differential Harnack” 漏一个 f，写作 “diferential”。10.3 的尺度范围、曲率界、距离条件及 (11.1) 公式其余核对吻合。Markdown 未保留印刷页码 27。

## p.028/39（PDF p.28 / 印刷 p.28）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:24:40-04:00
- PNG：未单独保存；born-digital 主通道为 PDF 文本层逐页对账，本页不属于 PNG 抽验页。
- 核对：11.1 κ-noncollapsing/entropy 条件续文；11.2 的约化体积选点与 blow-down soliton 命题/证明概要；11.3 二维 corollary；11.4 渐近体积比定义开头。对照 PDF p.28 文本层及 MinerU Markdown 第 643–655 行。
- 结果：FAIL。11.2 的距离表达式 dist_{t0−τ̄} 被写作 dis_{t0−τ̄}（漏 t）；11.4 的体积比中 Vol 被拆为 “V o l”，影响检索；证明中 lim_{τ→0} 的箭头丢失。其余约化体积单调性、极限常数与 soliton 方程按文本层核对吻合。Markdown 未保留印刷页码 28。

## p.029/39（PDF p.29 / 印刷 p.29）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:30:42-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p029_asymptotic_volume.png、p029_asymptotic_ratio_symbol.png（PDF p.29，pnggray，300dpi；核对渐近体积比的希腊字母 ν）。
- 核对：11.4 渐近体积比定义、ν=0 命题及维数归纳证明；11.5 体积/曲率 blow-up corollary 与 κ-noncollapsing 反证。对照 PDF p.29 文本层和 MinerU Markdown 第 655–667 行。
- 结果：FAIL。原文把渐近体积比命名为希腊字母 ν，Markdown 在定义处漏掉该符号，并把命题 ν=0 误写成畸形的 calligraphic V。300dpi 裁片确认原字形为 ν，且 11.5 证明中的 ν(t) 也误作 cal V(t)。此外 d(x)→∞、k→∞、t→−∞ 三处趋于箭头丢失；“splits off a line” 写成 “splits of a line”；引文 [H 4, §22] 漏掉 §；Vol 被拆成 “V o l”。其他 blow-up 界与不等式经文本层核对吻合。Markdown 未保留印刷页码 29。

## p.030/39（PDF p.30 / 印刷 p.30）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:32:10-04:00
- PNG：未单独保存；born-digital 主通道为 PDF 文本层逐页对账，本页不属于 PNG 抽验页。
- 核对：11.6 Corollary (a)/(b) 及尺度/体积论证、曲率下界变体、11.7 三维闭流拓扑说明开头；对照 PDF p.30 文本层与 MinerU Markdown 第 669–681 行。
- 结果：FAIL。11.6(a) 的时间区间印为 t0≤t≤0，Markdown 在 0 后多出孤立的 2；11.6(b) “in place of t0” 被拆成 “in place o f t0”；证明中多处 dist 与 Vol 字母间插入空格，影响记号检索。复读还发现半径/时间区间中的若干 LaTeX 控制词被写成双反斜线形式（如 \\frac、\\bar、\\prime），已按 PDF p.30 文本层恢复为单反斜线命令。曲率估计的参数、体积假设及 11.7 叙述其余对应。Markdown 未保留印刷页码 30。

## p.031/39（PDF p.31 / 印刷 p.31）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:33:43-04:00
- PNG：未单独保存；born-digital 主通道为 PDF 文本层逐页对账，本页不属于 PNG 抽验页。
- 核对：11.7 紧致性定理证明后半与 11.8 ε-neck 定义、corollary 开头；对照 PDF p.31 文本层和 MinerU Markdown 第 681–691 行。
- 结果：FAIL。原文 “splits off a line” 在 Markdown 写成 “splits of a line”；ε-neck 定义中的 dist_0 被拆成字母间空格；“after scaling with factor Q, ε-close” 中的逗号误成孤立点号；corollary 起句的 “if” 与 “11.1” 被拆出空格。PDF p.31 在 corollary 的 “and” 处转页，Markdown 后续句子位于下一页条目范围。印刷页码 31 未保留。

## p.032/39（PDF p.32 / 印刷 p.32）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T17:51:58-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p032_z2_quotient.png（PDF p.32，pnggray，300dpi；仲裁 Z₂ quotient 的连字符位置）。
- 核对：11.8 Corollary 续文、11.9/11.10*、§12 标题/12.1 定义与定理、反证证明首段；对照 PDF p.32 文本层和 MinerU Markdown 第 691–707 行。
- 结果：FAIL。11.8 续文把印刷 diam M_ε 写作带点的 Ṁ_ε；11.9 的印刷 Z₂-quotients 被写成 Z_{2^-}，300dpi 裁片确认减号是 2 后的连字符而非上标。11.10* 引文的 §16–22 记号在 Markdown 写成带空格的 \S；§12 定理的 “Given” 字母被拆开，ε-close 也被拆作字母串，dist_{t0} 的字母间插入空格。其余定理条件与 Harnack 公式结构吻合。Markdown 未保留印刷页码 32；证明段在 “does not” 处续页。

## p.033/39（PDF p.33 / 印刷 p.33）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T19:08:44-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p033_claim2_distance.png、p033_singular_point.png（PDF p.33，pnggray，300dpi；核对 dist 下标、R 趋于无穷及页末断点）。
- 核对：12.1 反证论证开头、Claim 1、Claim 2 的测地线距离条件及 proof 的两种极限情形，直至印刷页末；对照 PDF p.33 文本层/裁片与 MinerU Markdown 第 707–717 行。
- 结果：FAIL。Claim 2 条件中的印刷 dist_{t̄}(x̄,z) 被 Markdown 误识成 dist_{bar-iota}(x̄,z)；“let γ”及“for each y”出现字母间空格；R(x,t̄)→∞ 被写成带横线的 “- to infinity”。复读还发现 Claim 2 记号中的多处 LaTeX 控制词带了双反斜线，已按 PDF p.33 文本层及裁片恢复为单反斜线命令。300dpi 裁片确认距离下标为 t̄、比较量确为趋于无穷。PDF p.33 仅到 “the region beyond”，后续 singular-point 极限论证属 p.34。Markdown 未保留印刷页码 33。

## p.034/39（PDF p.34 / 印刷 p.34）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T19:33:04-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p034_page_detail.png（PDF p.34，pnggray，300dpi；核对奇点标签 o、距离算子及曲率界）。
- 核对：§12.1 证明中第一奇点极限的结束部分；缩放极限延拓；Hamilton Harnack 曲率估计与 dist 比较；非紧情形的分离距离论证开头。对照 PDF p.34 文本层/裁片及 MinerU Markdown 第 717–723 行。
- 结果：FAIL。原页将奇点标签印作小写 o，Markdown 首处改成大写 O，并把两处邻近 o 写成不必要的上标/逗号格式；300dpi 图确认均为正文小写 o。Markdown 将 “differential Harnack” 写成 “diferential Harnack”，把 R(x,t) 写成带横线的 R̃(x,t)，并将 dist_t / dist_{t0} 多处误识为 Φ 或拆坏的 dis-t。页末的非紧情形句子在 PDF p.34 以逗号转页，Markdown 续句属 p.35。印刷页码 34 未保留。

## p.035/39（PDF p.35 / 印刷 p.35）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T19:55:54-04:00
- PNG：未单独保存；born-digital 主通道为 PDF 文本层逐页对账，本页不属于 PNG 抽验页。
- 核对：p.34 非紧情形论证的句尾续文；12.2 Theorem 与其 Claim 证明开头；12.3 Theorem 声明至页末；对照 PDF p.35 文本层与 MinerU Markdown 第 723–737 行。
- 结果：FAIL。12.2 Claim 中 “differential” 写作 “diferential”；R(x,1)→∞ 的箭头在 Markdown 中丢失；dist_1/dist_{t̄} 多处字母拆分。12.3 开头的 “closed three-manifold” 在 Markdown 连写为 “closed threemanifold”。其余阈值、尺度和 Claim 参数按文本层吻合。PDF p.35 在 12.3 的时间区间中途结束；后续距离与 φ 条件归 p.36。印刷页码 35 未保留。

## p.036/39（PDF p.36 / 印刷 p.36）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T20:43:53-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p036_time_variable.png、p036_rm_t.png（PDF p.36，pnggray，300dpi；分别核对 Rm(x,t) 中的 t 与 13.1 的 t R̃m 记号）。
- 核对：12.3 Theorem 结尾、time-slice curvature bound 证明、12.4 Corollary、13.1 归一化曲率介绍与 theorem 开头；对照 PDF p.36 文本层/裁片及 MinerU Markdown 第 737–749 行。
- 结果：FAIL。12.3 证明句 “fix these values of τ,K, consider …” 在 Markdown 的 K 后多出一个 2。随后 Rm(x,t) 被写成 Rm(x, dot t)；300dpi 裁片确认印刷为普通 t。复读还发现 12.4 的估计式中多个 LaTeX 控制词带了双反斜线，已按 PDF p.36 文本层恢复为单反斜线命令。12.4 的尺度估计其余条件/幂次与文本层吻合，13.1 归一化曲率定义亦与裁片对应。印刷页码 36 未保留；13.1 定理的正文续到 p.37。

## p.037/39（PDF p.37 / 印刷 p.37）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T21:09:47-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p037_time_sequence.png（PDF p.37，pnggray，300dpi；核对 thick-thin 段中的 t 序列极限）。
- 核对：13.1 normalized-curvature 说明、thick-thin Theorem (a)/(b) 与随后的大尺度拓扑讨论、开放问题；13.2 奇点/手术讨论；对照 PDF p.37 文本层与 MinerU Markdown 第 747–757 行。
- 结果：FAIL。两处 “sufficiently” 写成 “suficiently”，开放问题中的 t→∞ 丢失箭头；thick-thin 段中 t→0 和 w→0 的箭头也丢失。300dpi 裁片确认印刷确为 t→0：虽与同段“large t”语境不协调，仍按 print 保留，不擅自改成 ∞。Markdown 未保留印刷页码 37。

## p.038/39（PDF p.38 / 印刷 p.38）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T21:36:10-04:00
- PNG 裁片：audit/entropy_ricci/300dpi/p038_bibliography.png、p038_interior_word.png（PDF p.38，pnggray，300dpi；核对参考文献字形与 Interior 断字）。
- 核对：13.2 收尾、13.3*、References 从 [A] 至 [Gaw]；对照 PDF p.38 文本层和 MinerU Markdown 第 757–785 行。
- 结果：FAIL。13.3 的 “differential-geometric” 漏一个 f；[B-Em] 的 “Diffusions” 被写作 “Difusions”；[Ch-Co] 与 [C] 两条期刊名中的 “Jour. Diff. Geom.” 均漏一个 f。300dpi 参考文献裁片确认双 f。源级 quirk：[E-Hu] 参考文献正文印刷为 “In terior estimates”（单词 Interior 中有间隔），300dpi 裁片确认；Markdown 同样如此，按原样保留、不合并。Markdown 未保留印刷页码 38；p.38 在 [Gaw] 条目后结束。

## p.039/39（PDF p.39 / 印刷 p.39）
- actor=Peer-P05; model=gpt-6-luna; effort=max
- 时间（America/New_York）：2026-10-01T22:04:20-04:00
- PNG：`audit/entropy_ricci/p039.png`（整页，150dpi；参考文献文字层对账并目检 PDF 页面）。
- 核对：References 从 [G] 至 [Lott]；对照 PDF p.39 文本层、整页 PNG 与 MinerU Markdown 第 787–815 行。

- 结果：FAIL。[H 1]、[H 2]、[H 3]、[H 4] 与 [Hu] 的期刊名中，印刷 `Diff. Geom.` 被 Markdown 写成 `Dif. Geom.`（[H 4] 为 `Surveys in Dif. Geom.`）；[I] 的 `Diff. Geo. Appl.` 被写成 `Dif. Geo. Appl.`，共 6 处漏写一个 `f`。印刷 [H 6] 的 `three-manifolds` 被写成 `threemanifolds`，漏掉连字符；同页 [I] 条目中的 `three-manifolds` 也确认该连字符。其余本页核对的参考文献题名、卷期、年份与页码相符。Markdown 未保留印刷页码 39。

## 全文修复与最终复核记录

- actor=Peer-P05; model=gpt-6-luna; effort=max
- 最终复核日期：2026-10-02（America/New_York）。
- 状态：`CANDIDATE_REPAIRED_NOT_CANONICAL`；canonical integrator 为 Master-Luna，尚待集成。
- 源 PDF SHA-256：`945e278613c45ea1ab617b28c3095783d0e68958dc0546dfcfa9b42b9674fbe1`。
- MinerU Markdown 修复前 SHA-256：`2e048e359da9b28283294b6639103b039718b281ed3965548141a58b01a1f416`。
- MinerU Markdown 修复后 SHA-256：`ccf3ba4849988c0e5b20e889195e473b8c1aeadde7ebd560f9e9b8df15026883`。
- 修复提交：`03f07a9d0d790ca39365ccd6085c3750cc96a2af`（单独的 `fix(md)` 提交）；本次审计记录与新增原页裁片提交：`4addb0ca05a86263f1a365f3040ba5e1402c6b3c`。
- 修复范围：应用 p.001–p.039 页面记录中由 PDF 文本层/原页图支持的 Markdown 转录修正，包括公式记号和上下标、遗失的趋于箭头与章节符号、断开的 Ric/Vol/dist 与普通单词、错识字母/数字、方框热算子、花体 ℒ、ν 和 Z₂、空格及参考文献拼写/连字符。各页具体异同、证据定位与保留事项以对应 p.001–p.039 条目为准。
- p.026、p.030、p.033、p.036 的最终复读还发现目标 Markdown 中有几处多余的 LaTeX 双反斜线；已按原页恢复单反斜线命令。p.026 原件符号差异由新增 `audit/entropy_ricci/300dpi/p026_sign_anomaly.png` 直接核对。
- 最终人工复读覆盖修复后的完整 Markdown 第 1–815 行。只读终验确认：审计页标题为有序、唯一的 39 页；目标 Markdown 与审计记录均无控制字符或 U+FFFD；目标 Markdown 无 `\\` 后接 LaTeX 命令的残留；`git diff --check` 通过。未运行测试；审计范围是原页转录忠实度，不是对论文数学命题作独立证明验证。
- 保留的原页 quirk 包括：p.1 左侧 arXiv 日期与居中日期不一致；印刷中的 “a priory”、“Rimannian”、“B(x₀,r²)”、“d(x₁,t₀)=r₀”、“M,or”、“dₜ−Δt”、“we”ll”、“t→0” 和 “In terior”；以及 p.026 的中间估计式 `−n` 与后续对数 Sobolev 表达式 `+n` 差异。均按 print 保留，没有依据上下文或数学预期静默更正。印刷页边信息/页码未并入连续正文 Markdown，已在逐页条目中标明。
- 仅本 Peer worktree 有效；未修改根 README、MEMORY、AUDIT-INDEX 或 AUDIT-PROGRESS，未推送。上述修复与验收结论仍是候选记录，等待 Master-Luna 对 exact commits、Markdown 和证据直接复核并集成。

---

# 第二轮独立逐页复核（Workflow「审计 perelmanE」；范围 PDF p.1–p.8，共 8 页）

- 复核方式：每页单独 `gs -sDEVICE=pngmono -r150` 渲染 → Read 工具亲眼目检该页 PNG → 读 Markdown 对应段 → 五点比对 → 立即落签，页与页之间不批量合并。
- 审计时目标 Markdown SHA-256：`0843d9af2b86d9365b3aec41b697974143a940b52f53047c7729a1e28cd5f126`；源 PDF SHA-256（`shasum -a 256` 实测，只读）：`945e278613c45ea1ab617b28c3095783d0e68958dc0546dfcfa9b42b9674fbe1`。
- 溯源基线：`git show cpf-redo/Perelman_2002_entropy_ricci^:"2006年 - Perelman/Perelman_2002_entropy_ricci_mineru/Perelman_2002_entropy_ricci__Perelman_2002_entropy_ricci.md"`（worktree 内执行），用于判定所记缺陷属 MinerU 导出缺陷还是后续 peer 引入的回归。
- 证据留存：本轮渲染图 `/tmp/perelmanE_audit_pNNN.png`；p.1–p.8 同名 150dpi 常驻副本已存在于 repo 内 `2006年 - Perelman/audit-redo/pNNN.png`，条目中一并引用，满足 SOP「审计图片不得只存 /tmp」。本轮写集合限定为目标 Markdown 与本篇 AUDIT，不新增图片文件。
- 位置对照：本轮新增 p.001–p.008 条目，与上文 Peer-P05 的 p.001/39–p.039/39 旧记录并存（两轮互相独立，旧记录未被改写）。

## p.001（PDF p.1 / 印刷 p.1）
- PNG：/tmp/perelmanE_audit_p001.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p001.png`）
- 核对：题录页——标题「The entropy formula for the Ricci flow and its geometric applications」、作者「Grisha Perelman∗」、居中日期行「November 26, 2024」、页边竖排 arXiv 标识、节标题「Introduction」、第 1 段三处行间公式（$\frac{d}{dt}g_{ij}(t)=-2R_{ij}$；$Rm_t=\triangle Rm+Q$；$R_t=\triangle R+2|\mathrm{Ric}|^2$）、引文 [H 1] 与 [H 1,H 2]、页底作者脚注全文、印刷页码 1；对照 Markdown 第 1、3、5、7、9、11 行与 `pdftotext -f 1 -l 1 -layout` 文本层。
- 结果：PASS
- 备注：（a）印刷正文行末断字 `pinched point-` / `wisely`（p001.png 正文倒数第 5–4 行；文本层作 `point-wisely`）在 Markdown 中已合为 `pointwisely`，属跨行断字还原，不判缺陷。（b）源级 quirk 忠实保留：页边竖排标识印 `arXiv:math/0211159v1 [math.DG] 11 Nov 2002`，居中日期却印 `November 26, 2024`；Markdown 只录居中日期，与印刷一致，不改。（c）页边 arXiv 竖排标识与印刷页码 `1` 属页边信息，原导出与当前 Markdown 均未并入正文（`grep -n arXiv` 全文仅命中参考文献 [Lott] 一处），按 print 忠实，不判缺陷。（d）正文「…or positive curvature operator」在印刷 p.1 断行，续文「in dimension four converge, modulo scaling, to metrics of constant positive curvature.」印于 p.2，Markdown 合并为同段；该跨页衔接在 p.2 条目复核。（e）本轮无改动。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：/tmp/perelmanE_audit_p002.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p002.png`）
- 核对：p.1 续文「in dimension four converge, modulo scaling, to metrics of constant positive curvature.」；无曲率假设段（$T$、$t$ close to $T$、[H 9]、「a convergence theorem ,」、`(modulo diffeomorphisms)`、$(- \infty , T)$、Ivey [I]、[H 4]、[H 3]、「a differential Harnack inequality」、[H 4,§26]）；手术段（[H 5]、four-manifolds、「a priory assumptions」、$t\to\infty$、$\widetilde{Rm}(x,t)=tRm(x,t)$、[H 6]、「no counterexample to the Thurston geometrization conjecture can」）；印刷页码 2；对照 Markdown 第 13、15 行与 `pdftotext -f 2 -l 2 -layout` 文本层。
- 结果：PASS
- 备注：（a）跨页衔接已核实：p.1 段末「or positive curvature operator」与本页首行「in dimension four converge, modulo scaling, to metrics of constant positive curvature.」在 Markdown 中合并为同一段，文字逐字衔接无增删。（b）旧审计曾记的 `difeomorphisms / diferential / diferent / suficient / t \infty 缺箭头 / [H 4,26] 缺 §` 在当前 Markdown 中均已消失：`grep -o` 实测 `diffeomorphisms`×2、`differential`×11、`sufficient`×6、`H 4, §26`×1、`\to \infty` 箭头形式存在（`all time $t \to \infty$`），且对 `difeomorphisms|diferential|diferent|suficient` 的反向 grep 无命中。（c）印刷原样 quirk 忠实保留：`a convergence theorem ,`（逗号前空格）、`a priory assumptions`（原文错字）、`without any a priory assumptions`，Markdown 同文不改。（d）行末断字 `ap-proaches`、`ten-sor`、`nonneg-ative`、`ar-bitrary` 已合并为完整词，不判缺陷。（e）印刷页码 2 未并入 Markdown（页边信息，与 p.1 同处理）。（f）本轮无改动。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：/tmp/perelmanE_audit_p003.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p003.png`）
- 核对：p.2 续文「occur among them. Thus, the implementation of Hamilton program would imply the geometrization conjecture for closed three-manifolds.」；Hamilton program 段（$t\to\infty$、「bounded normalized curvature」、「by our earlier (partly unpublished) work」）；Hamilton-Tian 段（`Kähler-Ricci flow on Kähler manifolds` 的变音符位置）；第 2 段编号项（RG flow、`[Gaw,§3]`、`insufficient`、Wilsonian picture）；第 2 段续（`an hierarchy`、`Space`、gradient-like）；第 3 段编号项开篇（`In §1`、`In §2, 3`、`diffeomorphisms`、`The easy (and known)`）；印刷页码 3；对照 Markdown 第 17、19、21、23、25、27 行。
- 结果：PASS
- 备注：（a）旧审计记录的「$t\to\infty$ 箭头丢失」在当前 Markdown 已修复：第 17 行作 `for all time $t \to \infty$ necessarily has bounded normalized curvature`，与印刷一致（`grep -o -E '.{12}\\to ?\\infty.{6}'` 实测本页对应串为 `all time $t \to \infty$ nece`）。（b）变音符：`grep -o -E '.{6}hler'` 实测两处均为 `Kähler`（`Kähler-Ricci flow on Kähler manifolds`），与印刷一致；旧审计所述「K¨ahler 变音符放错位置」已不存在。（c）节号符号齐全：`Gaw,§3`、`4, §26`、`§1`–`§13` 全部带 §（实测命中列表见本轮 grep）。（d）旧审计所述 `insufficient / diferent / diferential / difeomorphisms` 漏 f 现象已不存在：实测 `insufficient`×1、`sufficient`×1、`sufficiently`×4，反向 grep `difeomorphisms|diferential|suficient` 无命中。（e）印刷原样 quirk 保留：`an hierarchy`（原文如此）Markdown 同文，不改。（f）行末断字 `so-lution`、`con-jecture`、`back-ground`、`compo-nents`、`sug-gests`、`diffeomor-phisms` 已合并为完整词。（g）印刷页码 3 未并入 Markdown。（h）末句「The easy (and known)」在 p.3 断行，续文见 p.4 条目。（i）本轮无改动。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：/tmp/perelmanE_audit_p004.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p004.png`）
- 核对：p.3 续文「case of metrics with negative minimum of scalar curvature is treated in §2;」；单调性公式 (3.4)、L.Gross、§4 injectivity radius、§5 entropy/canonical ensemble、§6 `formal expressions ,` 与 Riemannian manifold of potentially infinite dimension、Bishop-Gromov、§7–§10、`differential Harnack inequality`、`Li-Yau`、`can not`、sections 1 through 10、`three manifolds`；§11 段（`singularities ( they must satisfy`、`noncollapsing assumption`）；§12 段（almost nonnegative curvature、Hamilton and Ivey result、forward and backward in time）；§13 段；星号说明段与 `[Cao-C]`；印刷页码 4；对照 Markdown 第 29、31、33 行。
- 结果：PASS±
- 差异（排版级，不误导，按 SOP 默认不改）：印刷 p.3→p.4 的第 3 段是**一个连续段落**（p.3 末行「The easy (and known)」→ p.4 首行「case of metrics with negative minimum of scalar curvature is treated in §2;」），Markdown 把它在页界处拆成两段：第 27 行以「The easy (and known)」结尾、第 28 行空行、第 29 行另起「case of metrics with negative minimum…」。文字内容无增删（见下方机械对账），仅段落边界与印刷不一致。
- 机械对账（只读脚本，不写 Markdown）：`pdftotext -f 4 -l 4 -layout` 与 Markdown 第 29/31/33 行做词级 `difflib.SequenceMatcher`，ratio=0.9921，仅 3 处差异，全部可解释：(1) `for mula` ← 印刷行末断字 `This for-`/`mula`；(2) `noncollaps ing` ← 印刷断字 `noncollaps-`/`ing`；(3) delete `4` ← 印刷页码。文字层本身逐字对应。
- 备注：（a）印刷原样 quirk 忠实保留且 Markdown 同文：`formal expressions ,`（逗号前空格）、`singularities ( they must satisfy`（括号后空格）、`can not`（分写）、`three manifolds`（无连字符）。（b）全部 § 节号（§2、§3、§4、§5、§6、§7、§8、§9、§10、§11、§12、§13）与式号 (3.4) 齐全，星号说明作 `\*` 转义，与印刷一致。（c）印刷页码 4 未并入 Markdown。（d）本轮无改动。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：/tmp/perelmanE_audit_p005.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p005.png`）
- 核对：节标题「1 Ricci flow as a gradient flow」；1.1 泛函 $\mathcal{F}=\int_M (R+|\nabla f|^2)e^{-f}dV$；一阶变分三行 display 公式逐项（$\delta\mathcal{F}(v_{ij},h)=\int_M e^{-f}[-\triangle v+\nabla_i\nabla_j v_{ij}-R_{ij}v_{ij}$ / $-v_{ij}\nabla_i f\nabla_j f+2<\nabla f,\nabla h>+(R+|\nabla f|^2)(v/2-h)]$ / $=\int_M e^{-f}[-v_{ij}(R_{ij}+\nabla_i\nabla_j f)+(v/2-h)(2\triangle f-|\nabla f|^2+R)],$）；1.1 正文（$\delta g_{ij}=v_{ij}$、$\delta f=h$、$v=g^{ij}v_{ij}$、`iff`、$dm=e^{-f}dV$、$\mathcal{F}^m=\int_M (R+|\nabla f|^2)dm$、`log(dV/dm)`、gradient flow $(g_{ij})_t=-2(R_{ij}+\nabla_i\nabla_j f)$）；1.2 Proposition 陈述（$t\in[0,T]$、$\mathcal{F}^m\le\frac{n}{2T}\int_M dm$）；Proof 首句 $\int_M dm=1$；式 (1.1)、(1.2)、(1.3) 逐项与式号；印刷页码 5；对照 Markdown 第 35、37、39–41、43、45、47、49–51、53、55–57、59、61–63 行与 `pdftotext -f 5 -l 5 -layout` 文本层。
- 结果：PASS±
- 差异（排版级，不误导，按 SOP「PASS± 排版级伪影默认不改」处理）：印刷把 1.2 的命题正文（`Suppose that the gradient flow for F^m exists for t ∈ [0,T]. Then at t = 0 we have F^m ≤ n/(2T)∫_M dm.`）与 `Proof.` 印为**斜体**，Markdown 一律以正体排出（`grep -c '\*[A-Za-z]'` 实测全文斜体标记数 = 0，说明这是 MinerU 的全篇字体样式拍平，非本页漏识；p.5 是全文首次出现斜体）。文字与数学内容本身逐字对应。
- 备注：（a）关键逻辑词核对通过：印刷「vanishes identically **iff** the measure $dm=e^{-f}dV$ is kept fixed」，Markdown 第 43 行为 `vanishes identically iff`，旧审计所记的 `if`（丢 ff）已不存在。（b）三个式号实测齐全且顺序正确：`\tag{1.1}`（`(g_ij)_t=-2(R_ij+∇_i∇_j f), f_t=-R-△f,`）、`\tag{1.2}`（`F^m_t=2∫|R_ij+∇_i∇_j f|^2 dm`）、`\tag{1.3}`（`(g_ij)_t=-2R_ij, f_t=-△f+|∇f|^2-R,`），系数、指数、上下标与印刷逐项一致（含 (1.1) 的 `−R − △f` 顺序与 (1.3) 的 `−△f + |∇f|² − R` 顺序）。（c）1.2 命题末印刷无句号，Markdown 第 45 行同样无句号，按 print 保留。（d）印刷页码 5 未并入 Markdown。（e）印刷 p.5 末行止于 (1.3)，续文「and retain (1.2) in the form」印于 p.6，已在 p.6 条目复核。（f）本轮无改动。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：/tmp/perelmanE_audit_p006.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p006_barm.png、/tmp/perelmanE_p006_bianchi.png（该页 600dpi 重渲后用 PIL 裁切放大；PIL 仅用于裁图，未写任何 Markdown）
- 核对：`and retain (1.2) in the form` 与式 (1.4)；`Now we compute` 与 $\mathcal{F}_t\ge\frac{2}{n}\int(R+\triangle f)^2e^{-f}dV\ge\frac{2}{n}(\int(R+\triangle f)e^{-f}dV)^2=\frac{2}{n}\mathcal{F}^2,$；`and the proposition follows.`；1.3 Remark 全部 Bochner–Lichnerowicz 公式（$\nabla^*\nabla u_i=(d^*d+dd^*)u_i-R_{ij}u_j$、$\nabla^*\nabla\psi=\delta^2\psi-\tfrac14R\psi$、$\delta^*=\delta$、$\nabla^{*m}$ 系列、$\delta^m\psi=\delta\psi-\tfrac12(\nabla f)\cdot\psi$、$R^m_{ij}$ 与 $R^m$ 的定义、$g^{ij}R^m_{ij}=R+\triangle f\ne R^m$、Bianchi 恒等式、$\mathcal{F}^m=\int_M R^m dm=\int_M g^{ij}R^m_{ij}dm$）；1.4\* DeTurck 段（`[H 4,§6]`）；dilaton 段（`[D,§6]`）；Bakry–Emery `[B-Em]` / `[Lott]`；节标题 `2 No breathers theorem I`；2.1 breather 定义开头（$t_1<t_2$、$\alpha>0$、`steady, shrinking and`）；印刷页码 6；对照 Markdown 第 65–69、71、73–75、77、79、81、83、85、87、89 行。
- 结果：FAIL（两处印刷所无的上划线 + 一处句点缺失；已按原图修复，以原图为准）
- 差异与修复（逐处 Edit，均由 600dpi 裁片直接证实）：
  1. Markdown 第 79 行定义列表写作 `R _ { i j } ^ { \bar { m } } =`，即在上标 $m$ 上多出一条**印刷没有的上划线**；600dpi 裁片 `/tmp/perelmanE_p006_barm.png` 显示印刷为 $R^m_{ij}$，$m$ 上无横线。已 Edit 改为 `R _ { i j } ^ { m } =`。
  2. 同行 Bianchi 恒等式中间项写作 `\nabla _ { i } \bar { R _ { i j } ^ { m } } -`，即整项被加框；600dpi 裁片 `/tmp/perelmanE_p006_bianchi.png` 显示印刷为 $\nabla_i R^m_{ij}-R_{ij}\nabla_i f$，无横线。已 Edit 改为 `\nabla _ { i } R _ { i j } ^ { m } -`。
  3. 该式末尾印刷有句点（`= 1/2∇_jR^m.`），Markdown 原写作 `$ Now`，句点缺失。已随第 2 处同一 Edit 补为 `R ^ { m }$. Now`。修复后实测 `grep -o -E '\\bar \{ (m|R _ \{ i j \} \^ \{ m \})[^}]*\}'` 对目标 Markdown 无命中。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:"2006年 - Perelman/Perelman_2002_entropy_ricci_mineru/Perelman_2002_entropy_ricci__Perelman_2002_entropy_ricci.md"` 实测，`\bar { R _ { i j } ^ { m } }` 与 `R _ { i j } ^ { \bar { m } }` 两处横线**在原始导出中即已存在**（各 1 处），故三处均为 **MinerU 导出缺陷，非任何 peer 引入的回归**。特别说明：既有 `AUDIT-Perelman_2002_entropy_ricci.redo.md` 的 p.006 条目把第 2 处判为「印刷 quirk（$R$ 上有短横），MD 忠实保留」——本次 600dpi 裁片推翻该判定，印刷并无该横线，该「保留」实为对导出伪影的误认。
- 备注：（a）印刷本身在同段并列两种拼写：`Bochner-Lichnerovicz formulas`（首次）与 `modified Bochner-Lichnerowicz formulas`（后一次）；Markdown 两处分别保留、未统一，忠实 print。（b）[H 4, §6]、[D, §6] 的 § 齐全。（c）节标题层级与 2.1 编号正确，$\alpha=1$、$\alpha<1$、$\alpha>1$ 三情形与印刷一致；本段在印刷止于 `steady, shrinking and`，续文属 p.7。（d）印刷页码 6 未并入 Markdown。（e）p.5→p.6 跨页衔接已核实：「and retain (1.2) in the form」紧接 p.5 的 (1.3) 式，Markdown 第 63–65 行衔接正确。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：/tmp/perelmanE_audit_p007.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p007.png`）
- 核对：p.6 续文「expanding breathers, respectively.」与 Trivial breathers / Ricci solitons 整段（`dy-namical`、`modulo diffeomorphism and scaling`、`periodic orbits and fixed points respectively)`、$R_{ij}+cg_{ij}+\nabla_ib_j+\nabla_jb_i=0$、$b_i=\frac12\nabla_i a$、`$a=-|x|^2/2$` 段末句点）；§2 导语段（`on closed M`、`not scale invariant`、`discussed in section 3`）；2.2 全段（$\lambda(g_{ij})=\inf\mathcal{F}(g_{ij},f)$、$\int_Me^{-f}dV=1$、`lowest eigenvalue of the operator -4△+R`、formula (1.4)、$R_{ij}+\nabla_i\nabla_jf=0$）；2.3 与 Claim（$\bar\lambda(g_{ij})=\lambda(g_{ij})V^{2/n}(g_{ij})$、`nonpositive`）；Indeed 括注（$dV/dt>0$、`for every t`、$-\frac{d}{dt}\log V=\frac1V\int RdV\ge\lambda(t)$、`can not be nonnegative`）；`Proof of the claim.`；三行 display 不等式链（$d\bar\lambda(t)/dt\ge 2V^{2/n}\int|R_{ij}+\nabla_i\nabla_jf|^2e^{-f}dV+\frac2nV^{(2-n)/n}\lambda\int-RdV\ge$ / $2V^{2/n}[\int|R_{ij}+\nabla_i\nabla_jf-\frac1n(R+\triangle f)g_{ij}|^2e^{-f}dV+$ / $\frac1n(\int(R+\triangle f)^2e^{-f}dV-(\int(R+\triangle f)e^{-f}dV)^2)]\ge0,$）；印刷页码 7；对照 Markdown 第 89、91、93、95、97、99、101、103–105、106–108 行。
- 结果：PASS±（一处句点缺失，已按原图修复）
- 差异与修复（Edit，逐字可定位）：Markdown 第 89 行段末 `$a = - | x | ^ { 2 } / 2$` 后**缺句点**，而印刷为 `a = −|x|²/2.`（150dpi PNG 目检 + `pdftotext -bbox` 该行末 token 实测为 `'/2.'`，y=273.3–285.2pt，双通道互证）。已 Edit 补为 `$a = - | x | ^ { 2 } / 2$.`。修复后实测 `grep -o -E 'and\$a = - \| x \| \^ \{ 2 \} / 2\$\.'` 命中。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对 `and$a = - | x | ^ { 2 } / 2$\.` 实测命中数 = 0，即原始导出即缺该句点——属 **MinerU 导出缺陷，非 peer 回归**。
- 备注：（a）排版级伪影登记不改：正体词被 MinerU 写成带字间空格的 `\mathrm {…}`，本页两处为 `\mathrm { A t }`（对应印刷 `At each time`）与 `\mathrm { l o g }`（对应印刷 `log V`）；同族伪影全篇共 `\mathrm { e x p }`×6、`\mathrm { s o }`×2 等（`grep -o -E '\\mathrm \{ [^}]*\}'` 清点），渲染后仍是可读正体，不误导数学内容，按 SOP「PASS± 排版级伪影默认不改」处理。（b）印刷中的 `(Thus, … fixed points respectively).` 与 `At each time` 之间的句读结构在 Markdown 中一致；`$R_{ij}+\nabla_i\nabla_jf = 0$` 中的 `0` 在 Markdown 落在数学环境外（`} \end{array}$ 0 for$f$`），系 MinerU 行间切分所致，语义无歧义，登记不判缺陷。（c）Claim 及其 `Proof of the claim.` 在印刷为斜体，Markdown 正体（与 p.5 同属全篇字体拍平）。（d）三行不等式链末的逗号 `,` 在 Markdown 中保留，与印刷一致。（e）印刷页码 7 未并入 Markdown。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：/tmp/perelmanE_audit_p008.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p008_becausef.png、p008_eq31.png、p008_eq33.png、p008_eq34.png、p008_boxstar.png（该页 600dpi 重渲后用 PIL 裁切放大，PIL 仅用于裁图）
- 核对：p.7 续文「where f is the minimizer for $\mathcal{F}$.」；2.4 全段（`non-constant Ricci curvature`、`Euler-Lagrange`、$2\triangle f-|\nabla f|^2+R=const.$、$\triangle f-|\nabla f|^2=const=0$、**被测字形** `because ∫(△f−|∇f|²)e^{−f}dV = 0`、`maximum principle`）；2.5\* 段（`[H 6,§2]`、$RV^{2/n}$）；节标题 `3 No breathers theorem II`；3.1 段（$\lambda>0$、`denoted by τ`）；式 (3.1)、(3.2)、(3.3)、(3.4) 的系数/指数/上下标与式号逐项；`τ > 0. Clearly W is invariant under simultaneous scaling`；方框热算子 $\square^*u=0$、$u=(4\pi\tau)^{-\frac n2}e^{-f}$、$\square^*=-\partial/\partial t-\triangle+R$；印刷页码 8；对照 Markdown 第 115、117、119、121、123、126、129、132、135、138、141、144 行。
- 结果：PASS±（仅排版级伪影，无内容缺陷；本轮未改动 Markdown）
- 差异（排版级，不误导，按 SOP 默认不改）：
  - 第 117 行 `Thus,$\triangle f - |\nabla f|^2 = c o n s t = 0$`：印刷的斜体 `const` 被拍平成带字间空格的 `c o n s t`；同句前一处的 `=const.` 则在数学环境外。字面可读，语义无歧义。
  - 第 117 行 `$R { + \triangle f }$`：印刷连贯的 $R+\triangle f$ 被拆出一个落在数学环境外的 `+`，纯切分伪影。
  - 第 119 行编号 `$\mathbf { 2 . 5 ^ { * } }$`：印刷的粗体小节号 `2.5*` 被写成粗体数学式，而同类的 `2.4.`、`3.1.` 为正体文本，编号体系内部不一致但不产生歧义。
- 备注：（a）**曾疑似缺陷、经裁片排除**：第 117 行 `because$\begin{array}{r}\int{(\triangle f-|\nabla f|^2)e^{-f}dV=0}\end{array}$` 的积分号，在 150dpi 下曾被读作普通斜体 $f$（`pdftotext -bbox` 该行也确实只吐出一个孤立 token `x=153.0-158.6, y=223.2-251.9`，高度 28.7pt 远超同行正文字高 12pt）。600dpi 裁片 `/tmp/perelmanE_p008_becausef.png` 显示该字形确为长积分号 ∫，故 Markdown 的 `\int` **忠实印刷，不判缺陷**。（b）四个式号实测齐全、内容逐项一致：\tag{3.1} `\mathcal{W}(g_{ij},f,\tau)=\int_M[\tau(|\nabla f|^2+R)+f-n](4\pi\tau)^{-\frac{n}{2}}e^{-f}dV,`、\tag{3.2} `\int_M(4\pi\tau)^{-\frac{n}{2}}e^{-f}dV=1,`、\tag{3.3} `(g_{ij})_t=-2R_{ij},\ f_t=-\triangle f+|\nabla f|^2-R+\frac{n}{2\tau},\ \tau_t=-1`、\tag{3.4} `d\mathcal{W}/dt=\int_M 2\tau|R_{ij}+\nabla_i\nabla_jf-\frac{1}{2\tau}g_{ij}|^2(4\pi\tau)^{-\frac{n}{2}}e^{-f}dV.`（含句末句点）。三处指数 $-\frac{n}{2}$ 与两处 $\frac{n}{2\tau}$、$\frac{1}{2\tau}$ 的分子分母均由 600dpi 裁片 `p008_eq31/eq33/eq34.png` 逐个确认。（c）方框热算子：600dpi 裁片 `p008_boxstar.png` 确认印刷为「方框 + 上标星号」，文本层作 `✷∗`；Markdown 的 `\Box ^ { * }` 忠实，未退化为 □ 或 ⊠。（d）[H 6, §2] 的 § 齐全；`$R V ^ { \frac { 2 } { n } }$` 与印刷 $RV^{2/n}$ 一致（文本层把分子 2 单独排到上一行，属 `-layout` 伪影，非印刷差异）。（e）本页与 p.9 的页界已核实：印刷 p.8 止于 (3.4) 式，p.9 首句为 `Therefore, if we let µ(gij,τ)=inf W(gij,f,τ) over smooth f satisfying (3.2),`（Markdown 第 147 行），归属 p.9，不在本轮范围。（f）印刷页码 8 未并入 Markdown。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：/tmp/perelmanE_audit_p009.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p009_phi.png（该页 600dpi 重渲后用 PIL 裁切放大，PIL 仅用于裁图）
- 核对：µ/ν 定义段（$\mu(g_{ij},\tau)=\inf\mathcal{W}(g_{ij},f,\tau)$、`satisfying (3.2)`、$\nu(g_{ij})=\inf\mu(g_{ij},\tau)$、`nondecreasing along the Ricci flow`、`lim_{\tau\to\infty}\mu(g_{ij},\tau)=+\infty$、`the first eigenvalue of -4△+R`、`there is no shrinking breathers other than gradient solitons,`）；Claim 陈述；Proof of the Claim. (sketch) 全段（$\bar\tau>0$、`[0,\bar\tau]`、`u=(4\pi\tau)^{-n/2}e^{-f}`、`a δ-function at t = τ̄, τ(t) = τ̄ − t`、$\mu(g_{ij},\bar\tau)\le\mathcal{W}(g_{ij}(0),f(0),\tau(0))<0$ `by (3.4)`）；`Now let τ → 0` 与 display $\mathcal{W}(\frac12\tau^{-1}g_{ij},f^\tau,\frac12)=\mathcal{W}(g_{ij},f^\tau,\tau)=\mu(g_{ij},\tau)\le c<0.$；`The metrics ½τ^{-1}g_ij "converge"`、`∫_{\mathbb{R}^n}(2\pi)^{-n/2}e^{-f}dx=1`、display $\int_{\mathbb{R}^n}[\frac12|\nabla f|^2+f-n](2\pi)^{-n/2}e^{-f}dx<0$；Gaussian log Sobolev 段（`f = |x|²/2 − 2 log φ`、`integrate by parts`、`left to the reader`）；3.2 Remark 全段（`the equality cases`、`R_ij − g_ij − ∇_ib_j − ∇_jb_i = 0`、`(1−2t)g_ij(0)`、$\mu(g_{ij}(t),\frac12-t)=\mu(g_{ij}(0),\frac12)$、`R_ij + ∇_i∇_jf − g_ij = 0`、止于 `this is easy if M`）；印刷页码 9；对照 Markdown 第 147、149、151、153、155–157、159、161–163、165、167 行。
- 结果：PASS±（一处字形变体，排版级，按 SOP 默认不改；无内容缺陷）
- 差异（排版级，不误导）：第 165 行印刷的希腊字母为**直画 φ（`\varphi`）**，Markdown 写作 `\phi`；600dpi 裁片 `/tmp/perelmanE_p009_phi.png` 与 `pdftotext` 文本层（该 token 实测为 U+03C6 φ）双证。该变体在 TeX 中渲染为 ϕ，与印刷 φ 视觉不同，但指同一字母、不改变任何数学内容，按 SOP「PASS± 排版级伪影默认不改」登记不修。同页另有全篇性的正体算子字母间距扁平化（`\operatorname* { i n f }`×2、`\operatorname* { l i m }`），与 p.7 的 `\mathrm { l o g }` 同族，一并登记。
- 备注：（a）两处 display 的**句末标点**与印刷一致：$\cdots\le c<0.$ 带句点，$\int\cdots<0$ 无句点，均已核对（若误补或误删即成缺陷）。（b）印刷原样 quirk 保留：`there is no shrinking breathers`（原刊语法）、`the existence of minimizer`（无冠词）。（c）Claim 与 `Proof of the Claim.` 在印刷为斜体，Markdown 正体（与 p.5/p.7/p.8 同属全篇字体拍平）。（d）页界已核实：印刷 p.9 止于 3.2 Remark 的 `this is easy if M`，续文 `is closed, but can also be done with more efforts on some complete M, for instance when M is the Gaussian soliton.` 及 3.3\* 印于 p.10；Markdown 把续文并入第 167 行同一段、3.3\* 落在第 169 行，均属 p.10 范围，不计入本页。（e）机械对账（只读脚本）：词级 difflib ratio=0.688，低分全部来自公式记号编码差异（LaTeX 控制词 vs 文本层符号流，如 `\operatorname* { i n f }`↔`inf`、`\bar {\tau}`↔`τ̄`、`\frac {1}{2}`↔`1 2`、`\mathbb {R}^n`↔`ℝ^n`），非内容差异；除 φ 外无任何实词增删，唯一 delete 项为印刷页码 `9`。（f）印刷页码 9 未并入 Markdown。（g）本轮无改动。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：/tmp/perelmanE_audit_p010.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p010_rel41.png、p010_rel42.png（该页 600dpi 重渲 + PIL 裁切并 3× 放大，PIL 仅用于裁图）
- 核对：p.9 续文「is closed, but can also be done with more efforts on some complete M, for instance when M is the Gaussian soliton.」；3.3\* 段（`The no breathers theorem in dimension three was proved by Ivey [I]`、`almost nonnegative curvature estimate`）；Logarithmic Sobolev 段（`see [G] for a survey and bibliography up to the year 1992`、`Bakry-Emery [B-Em]`、`Ecker [E 1]`）；节标题 `4 No local collapsing theorem I`；章节导语（`monotonicity formula (3.4)`）；4.1 定义段（`on [0,T). We say`、$t_k\to T$、$B_k=B(p_k,r_k)$、`at times t_k, such that`、$r_k^2/t_k$ is bounded、**$|Rm|(g_{ij}(t_k))\le r_k^{-2}$**、$r_k^{-n}Vol(B_k)\to0.$）；Theorem 陈述（`If M is closed and T < ∞`）；Proof 全段（$\mu(g_{ij}(t_k),r_k^2)\to-\infty$、`f_k(x) = −log φ(dist_{t_k}(x,p_k)r_k^{−1}) + c_k`、`equal 1 on [0,1/2], decreasing on [1/2,1], and very close to 0 on [1,∞)`、$c_k\to-\infty$、$\mu(g_{ij}(0),t_k+r_k^2)\to-\infty.$、`However this is impossible, since t_k+r_k^2 is bounded.`）；4.2 Definition 全段（`κ-noncollapsed on the scale ρ`、`r < ρ`、**$|Rm|(x)\le r^{-2}$**、`x ∈ B`、`has volume at least κr^n.`）；`It is clear that a limit of κ-noncollapsed metrics`段（$\alpha^2g_{ij}$、`scale αρ`、$\kappa=\kappa(g_{ij},T)>0$、`scale T^{1/2}`、`for all t ∈ [0,T),`）；印刷页码 10；对照 Markdown 第 167、169、171、173、175、177、179、181、183、185 行。
- 结果：FAIL（5 处印刷标点缺失/错置，已按原图逐处修复，以原图为准）
- 差异与修复（逐处 Edit；标点类证据为 `pdftotext -f 10 -l 10 -layout` 文本层 + 150dpi 原页目检双通道，互证一致）：
  1. 第 177 行 `on$[ 0 , T )$ We say that` → 印刷 `[0, T ).` 后**缺句点**。已改为 `on$[ 0 , T )$. We say that`。
  2. 第 177 行 `at times$t _ { k } .$such that` → 印刷为逗号 `$t_k$, such that`，Markdown 把逗号**误作句点**。已改为 `at times$t _ { k }$, such that`。
  3. 第 177 行段末 `$r _ { k } ^ { - n } Vol ( B _ { k } ) \to 0$` → 印刷 `→ 0.` **缺句点**。已补为 `…\to 0$.`。
  4. 第 181 行 `\to - \infty$ However this is impossible` → 印刷 `→ −∞.` 后**缺句点**（文本层作 `we get µ(gij(0), tk + rk2 ) → −∞.` 换行接 `However this is impossible,`）。已补为 `\to - \infty$. However this is impossible`。
  5. 第 183 行段末 `has volume at least$\kappa r ^ { n }$` → 印刷 `κr^n .` **缺句点**。已补为 `has volume at least$\kappa r ^ { n }$.`。
  - 修复后以 `git show HEAD:<md>` 与当前文件做字符级 difflib 复核，第 177/181/183 行恰好产生上述 5 处增改，无任何夹带改动。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:"2006年 - Perelman/Perelman_2002_entropy_ricci_mineru/Perelman_2002_entropy_ricci__Perelman_2002_entropy_ricci.md"` 实测，`on$[ 0 , T )$ We say that`、`at times$t _ { k } .$such that`、`\to - \infty$ However`、`has volume at least$\kappa r ^ { n }$` 四串在该导出中均原样存在（第 3 处的段末形态 `in$B _ { k }$and$r _ { k } ^ { - n } Vol ( B _ { k } ) \to 0$` 亦命中），故 5 处**全部是 MinerU 导出缺陷，无一为 peer 引入的回归**。
- 备注：（a）**一处疑似数学差异、经裁片排除**：4.1 的 $|Rm|(g_{ij}(t_k))\le r_k^{-2}$ 在 150dpi 下曾被读作 `≪`（并一度怀疑 MinerU 用 `\leq` 顶替了 `≪`）。600dpi 裁片 `/tmp/perelmanE_p010_rel41.png`（3× 放大）显示为**单条 ≤**（一个尖括号 + 一条横线，非双尖括号 `≪`），且与 4.2 处的 `/tmp/perelmanE_p010_rel42.png` 字形完全一致；文本层亦作 `≤`。故 Markdown 的 `\leq` 忠实印刷，**不判缺陷**。（b）Theorem 陈述、Proof 全部不等式与 `dist_{t_k}(x,p_k)r_k^{-1}`、$\mathcal{F}$ 型记号均逐项对应；`φ` 仍是 p.9 已登记的 `\phi`/`\varphi` 字形变体（本页两处），同族不重复计。（c）印刷原样 quirk 保留：`Logarithmic Sobolev inequalities is a vast area`（原刊语法）、`this argument requires the existence of minimizer`（无冠词）、`4.2. Definition We say`（Definition 后无句点）。（d）Theorem、Proof、Definition 在印刷为斜体，Markdown 正体（全篇字体拍平）。（e）印刷 `Vol` 为正体而 Markdown 作普通文本 `Vol`，属字体拍平，不误导。（f）页界已核实：印刷 p.10 止于 `for all t ∈ [0,T),`，续文 `provided it exists on this interval. Therefore, …` 与 Corollary 印于 p.11。（g）印刷页码 10 未并入 Markdown。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：/tmp/perelmanE_audit_p011.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p011.png`）
- 核对：p.10 续文「provided it exists on this interval. Therefore, using the convergence theorem of Hamilton, we obtain the following」；Corollary 全段（$t\in[0,T)$、`T < ∞`、$t_k\to T$、$p_k\in M$、$Q_k=|Rm|(p_k,t_k)\to\infty$、`|Rm|(x,t) ≤ CQ_k, whenever t < t_k`、`(a subsequence of) the scalings`、`is κ-noncollapsed on all scales for some κ > 0.`）；节标题 `5 A statistical analogy`；章节导语（`the functional W, introduced in section 3`）；5.1 段（$\beta^{-1}$、$Z=\int\exp(-\beta E)d\omega(E)$、``density of states''`、$\langle E\rangle=-\frac{\partial}{\partial\beta}\log Z$、`S = β<E> + log Z`、$\sigma=\langle(E-\langle E\rangle)^2\rangle=\frac{\partial^2}{(\partial\beta)^2}\log Z$）；`Now fix a closed manifold M with a probability measure m` 段（$(g_{ij})_\tau=2(R_{ij}+\nabla_i\nabla_j f)$、`dm = udV`、`u = (4πτ)^{-n/2}e^{-f}`、`log Z = ∫(-f + n/2)dm`、括注 `(We do not discuss here … can be found)`）；三条 display 逐项（$\langle E\rangle=-\tau^2\int_M(R+|\nabla f|^2-\frac{n}{2\tau})dm,$／$S=-\int_M(\tau(R+|\nabla f|^2)+f-n)dm,$／$\sigma=2\tau^4\int_M|R_{ij}+\nabla_i\nabla_jf-\frac{1}{2\tau}g_{ij}|^2dm$）；`Alternatively, we could prescribe …`（`t-derivatives by minus τ-derivatives in (3.3 )`）；`Clearly, σ is nonnegative;` 段止于 `for all sufficiently`；印刷页码 11；对照 Markdown 第 187、189、191、193、195、197、199–201、203–205、207–209、211、213 行。
- 结果：PASS±（一处句点缺失，已按原图修复）
- 差异与修复（Edit）：第 189 行 Corollary 段末 `…for some$\kappa > 0$` **缺句点**，印刷为 `for some κ > 0.`（150dpi 目检 + `pdftotext -f 11 -l 11 -layout` 文本层 `is κ-noncollapsed on all scales for some κ > 0.` 双证）。已 Edit 补为 `…for some$\kappa > 0$.`；该锚串 `grep -c -F` 实测唯一。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对同一锚串实测命中数 = 1（无句点形态），即原始导出即缺——属 **MinerU 导出缺陷，非 peer 回归**。
- 备注：（a）三条 display 的**句末标点**逐条核对与印刷一致：`<E> = …dm,` 与 `S = …dm,` 均带逗号，`σ = …dm` 无标点，Markdown 全部照实，未误补。（b）印刷原样 quirk 保留：`(a subsequence of )` 与 `(3.3 )` 两处括号内侧空格，Markdown 同文不改。（c）正体算子字母间距扁平化（`\begin{array}…e x p(-…)\end{array}`）为 p.7/p.9 同族排版伪影，登记不判缺陷。（d）Corollary、5.1 正文在印刷为斜体，Markdown 正体（全篇字体拍平）。（e）页界已核实：印刷 p.11 止于 `for all sufficiently`，续文 `small τ > 0 (by proposition 1.2)` 印于 p.12，已在 p.12 条目复核。（f）印刷页码 11 未并入 Markdown。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：/tmp/perelmanE_audit_p012.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p012_manifold.png、p012_Rplus_index.png（该页 600dpi 重渲 + PIL 裁切放大，PIL 仅用于裁图）
- 核对：p.11 续文「small τ > 0 (by proposition 1.2).」及 `Furthermore, if (a) … δ-function …` 整段（`u_i`、`τ → τ_i > 0`、`τ_i → 0`、`In case (a) … positive limit.`）；`If the flow is defined for all sufficiently large τ …` 段（`Hamilton's terminology`、`entropy S as τ → ∞`、`whenever S stays bounded.`）；5.2 Remark 全段（`renormalization group flow`、`averaging over higher energy states`、`the exponential factor.`）；5.3\* 段（`Chow [C]`、`no relation between his formula and ours.`）；`The interplay of statistical physics and (pseudo)-riemannian geometry …` 段；节标题 `6 Riemannian formalism in potentially infinite dimensions`；章节导语（含拼写核对）；6.1 句与流形记号 $\widetilde{\mathcal{M}}=M\times\mathbb{S}^N\times\mathbb{R}^+$；度量 display 四项逐项（$\tilde g_{ij}=g_{ij}$、$\tilde g_{\alpha\beta}=\tau g_{\alpha\beta}$、$\tilde g_{00}=\frac{N}{2\tau}+R$、$\tilde g_{i\alpha}=\tilde g_{i0}=\tilde g_{\alpha0}=0,$）；`where i,j …` 段（`S^N factor`、`coordinate τ on ℝ^+ has index 0;`、`backward Ricci flow (g_ij)_τ = 2R_ij`、`constant curvature 1/(2N)`、`coincide (modulo N^{-1}) with the components of the`）；印刷页码 12；对照 Markdown 第 213、215、217、219、221、223、225、227、229–231、233 行。
- 结果：PASS±（仅排版级伪影，无内容缺陷；本轮未改动 Markdown）
- 差异（排版级，不误导，按 SOP 默认不改）：第 233 行 `the coordinate$\tau$on R<sup>+</sup> has index 0` 用 HTML `<sup>` 上标且丢失了**黑板粗体**；600dpi 裁片 `/tmp/perelmanE_p012_Rplus_index.png`（6× 放大）确认印刷为双竖笔画的 ℝ⁺。同一 Markdown 文件第 227 行对同一符号却写作 `\mathbb { R } ^ { + }`，属导出内部体例不一致；渲染后仍读作 R⁺，不改变任何数学内容。（另有 `5.2 Remark` 等斜体被拍平，与 p.5/p.7/p.8/p.11 同族。）
- 备注：（a）**两处曾疑似缺陷、经裁片+文本层排除**：(i) 第 225 行作 `Rimannian geometry`，而节标题第 223 行与 `(pseudo)-riemannian` 均为 `Riemannian`；`pdftotext -f 12 -l 12 -layout` 实测该行原文即作 `using the formalism of Rimannian geometry.`（双 n），Markdown **忠实保留原刊错字，不判缺陷、不改**。(ii) 第 227 行流形记号，150dpi 下曾被读作花体 $\mathcal{M}$ 带波浪号；600dpi 裁片 `/tmp/perelmanE_p012_manifold.png`（4× 放大）显示为**普通斜体 M 加波浪号**（无花体笔画），文本层亦作 `M̃`（U+004D+U+0303），故 `\tilde { M }` 忠实，不判缺陷。（b）度量 display 的系数 $\frac{N}{2\tau}$ 与加项 $+R$、末项逗号，以及 `1/(2N)`、`N^{-1}` 的指数与上下标，均逐项与原页一致（`-layout` 文本层 `g̃00 = N/(2τ) + R` 互证）。（c）行末断字 `infi-nite`、`de-scription`、`tem-perature` 已合并为完整词。（d）印刷页码 12 未并入 Markdown。（e）页界已核实：印刷 p.12 止于 `with the components of the`，续文 `matrix Harnack expression (and its traces), discovered by Hamilton [H 3].` 印于 p.13（`pdftotext -f 13` 实测），归 p.13 条目。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：/tmp/perelmanE_audit_p013.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p013_gammadot.png（该页 600dpi 重渲 + PIL 裁切并 5× 放大，PIL 仅用于裁图）
- 核对：p.12 续文「matrix Harnack expression (and its traces), discovered by Hamilton [H 3].」；热方程/共轭热方程段（`mod N^{-1}`、`via Laplace equation on M̃ for functions and volume forms respectively`、`u satisfies the heat equation on M iff ũ (the extension of u to M̃ constant along the S^N fibres)`、`△̃ũ = 0`、`ũ* = τ^{-(N-1)/2} ũ`、`0 mod N^{-1} on M̃.`）；6.2 全段（`isometric to g̃ (mod N^{-1})`、`backward m-preserving Ricci flow`、`( given by equations (1.1)`、`minus τ-derivatives`、`dm = (4πτ)^{-n/2}e^{-f}dV )`、`mapping each point (x^i, y^α, τ) into (x^i, y^α, τ(1 - 2f/N))`）；display 一（$\tilde g^m_{ij}$、$\tilde g^m_{\alpha\beta}=(1-\frac{2f}{N})\tilde g_{\alpha\beta}$、$\tilde g^m_{00}=\tilde g_{00}-2f_\tau-\frac f\tau$、$\tilde g^m_{i0}=-\nabla_if$、$\tilde g^m_{i\alpha}=\tilde g^m_{\alpha0}=0;$）；`then apply a horizontal (that is, along the M factor) diffeomorphism` 段（$(g^m_{ij})_\tau=2(R_{ij}+\nabla_i\nabla_jf)$、`(mod N^{-1})`）；display 二、三逐项；`Note that the hypersurface τ =const …` 段（`τ^{N/2}e^{-f}`、`1/τ(N/2 + τ(2△f − |∇f|² + R) + f) mod N^{-1}`、`the entropy S multiplied by the inverse temperature β`）；6.3 段（`Ricci-flatness`、`Bishop-Gromov relative volume comparison theorem`、`metric ball in (M̃, g̃) centered at some point p where τ = 0`、`shortest geodesic`、`orthogonal to the S^N fibre`、`γ(τ)`）；页末 display $\int_0^{\tau(q)}\sqrt{\frac{N}{2\tau}+R+|\dot\gamma_M(\tau)|^2}\,d\tau$；印刷页码 13；对照 Markdown 第 233、235、237–239、241、243–245、247–249、251、253、255–257 行。
- 结果：PASS±（一处句点缺失，已按原图修复）
- 差异与修复（Edit）：第 233 行（p.12→p.13 合并段落的 p.13 部分）末 `…0 mod$N ^ { - 1 }$on$\tilde { M }$` **缺句点**，印刷为 `0 mod N^{−1} on M̃ .`（`pdftotext -f 13 -l 13 -layout` 实测 `0 mod N on M̃ .` 换行后另有 `-1` 上浮，双通道一致）。已 Edit 补为 `…on$\tilde { M }$.`；锚串 `grep -c -F` 实测唯一。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对无句点形态实测命中数 = 1，即原始导出即缺——属 **MinerU 导出缺陷，非 peer 回归**。
- 备注：（a）**一处疑似数学差异、经裁片排除**：页末 display 的被积项，150dpi 下曾被读作「v 加波浪号」（疑 MinerU 以 `\dot{\gamma}` 顶替了 `\tilde v`）；600dpi 裁片 `/tmp/perelmanE_p013_gammadot.png`（5× 放大）清晰显示为 **γ 加圆点**（$\dot\gamma_M(\tau)$，下标 $M$），`pdftotext` 该 token 亦作 `γ̇`（U+03B3+U+0307）。故 Markdown 的 `\dot {\gamma} _ {M}` **忠实印刷，不判缺陷**。（b）排版级伪影登记不改：第 233 行 `(mod N −<sup>1</sup>)` 用 HTML `<sup>` 上标，与同段其余 `$N ^ { - 1 }$` 的 LaTeX 体例不一致（与 p.12 的 `R<sup>+</sup>` 同族）。（c）印刷原样 quirk 全部保留：`( given by equations (1.1)` 括号后空格、`(mod N −1 )` 括号前空格、`minus τ -derivatives`、`τ =const` 等距缺失；Markdown 同文不改。（d）四条 display 的系数 $\frac{2f}{N}$、$\frac f\tau$、$\frac{N}{2}$、$\tau^{N/2}$、指数 $-(N-1)/2$ 与句末标点（一式 `;`、二式 `,`、三式无标点）逐项与原页一致；page 13 的 display 一、二之后正文均无句点（续接 display），Markdown 未误补。（e）页界已核实：印刷 p.13 止于 `…dτ`，续行 `= … + O(N^{-2})` 印于 p.14（`pdftotext -f 14` 实测），归 p.14 条目。（f）印刷页码 13 未并入 Markdown。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：/tmp/perelmanE_audit_p014.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p014_Lline.png、p014_Lx.png（该页 600dpi 重渲 + PIL 裁切并放大，PIL 仅用于裁图）
- 核对：p.13 续行 display $= \sqrt{2N\tau(q)} + \frac{1}{\sqrt{2N}}\int_0^{\tau(q)}\sqrt\tau(R+|\dot\gamma_M(\tau)|^2)d\tau + O(N^{-\frac32})$；`Thus a shortest geodesic should minimize` 段（$\mathcal{L}(\gamma)=\int_0^{\tau(q)}\sqrt\tau(R+|\dot\gamma_M(\tau)|^2)d\tau,$、`entirely in terms of M`、`Let L(q_M) denote the corresponding infimum`、`metric sphere in M̃ of radius √(2Nτ(q))`、`O(N^{-1})-close`、`hypersurface τ = τ(q)`、$V(\mathbb{S}^N)\int_M(\sqrt{\tau(q)}-\frac{1}{2N}L(x)+O(N^{-2}))^N dx$、`ratio … to √(2Nτ(q))^{N+n}`、`constant times N^{-n/2} times`）；reduced volume display $\int_M\tau(q)^{-n/2}\exp(-\frac{1}{\sqrt{2\tau(q)}}L(x))dx + O(N^{-1})$；`The computation suggests …` 段（`denote by Ṽ(τ(q))`、`as τ decreases`）；6.4\* 全段（`Chow and Chu [C-Chu 1,2]`、`M × ℝ`、`dual to theirs.`）；`Our formula for the reduced volume … [Hu] …` 段；节标题 `7 A comparison geometry approach to the Ricci flow`；7.1 段（`$0 < \tau_1 \le \tau \le \tau_2$`、`its L-length`）；display $\mathcal{L}(\gamma)=\int_{\tau_1}^{\tau_2}\sqrt\tau(R(\gamma(\tau))+|\dot\gamma(\tau)|^2)d\tau$；`(of course, R(γ(τ)) and |γ̇(τ)|² are computed using g_ij(τ))`；`Let X(τ) = γ̇(τ), and let Y(τ) …`；页末 `δ_Y(L) =`；印刷页码 14；对照 Markdown 第 259–261、263、265–267、269、271、273、275、277、279–281、283、285、287–289 行。
- 结果：PASS±（一处 HTML 上标体例伪影，排版级；无内容缺陷；本轮未改动 Markdown）
- 差异（排版级，不误导，按 SOP 默认不改）：第 263 行 `a metric sphere in M<sup>˜</sup> of radius` 用 HTML `<sup>` 承载波浪号，而同页其余 $\tilde M$ 一律写作 `\tilde { M }`；体例不一致，但渲染后仍为 M̃，不改变任何数学内容。（与 p.12 的 `R<sup>+</sup>`、p.13 的 `(mod N −<sup>1</sup>)` 同族。）
- 备注：（a）**一处疑似记号差异、经裁片排除**：150dpi 下 `Let L(q_M)`、`−\frac{1}{2N}L(x)`、`exp(−…L(x))` 三处的 L 底部看似带下划线（疑为 $\underline{L}$）。600dpi 裁片 `/tmp/perelmanE_p014_Lline.png`（5×）与 `/tmp/perelmanE_p014_Lx.png`（6×）分别放大这两处，显示均为**普通斜体 L**，其下方的短横只是 L 自身的衬线笔尾，并非下划线。故 Markdown 的 `L ( q _ { M } )`／`L ( x )` **忠实印刷，不判缺陷**。（b）首行 display 的余项指数经 bbox 逐 token 确认为分数 `−3/2`（分子 `3` y=132.7–136.8、分母 `2` y=139.1–143.2），与 Markdown `O (N ^ {- \frac {3}{2}})` 一致。（c）其余系数/指数逐项一致：$\frac{1}{\sqrt{2N}}$、$\frac{1}{2N}$、$-\frac{n}{2}$、$\frac{1}{\sqrt{2\tau(q)}}$、$O(N^{-1})$、$O(N^{-2})$、$)^{N}$、$^{N+n}$。（d）印刷原样 quirk 保留：`( of course,` 无（此处为 `(of course,` 正常），而 6.4\* 段 `[C-Chu 1,2]` 的逗号无空格、`Huisken monotonicity formula` 无冠词，均照 print。（e）显示式的**句末标点**核对：`\mathcal{L}(\gamma)=…d\tau ,` 带逗号（续接 "an expression"），`(of course, …g_ij(τ))` 收尾双括号无句点，`δ_Y(L) =` 无句点（续 p.15），Markdown 三处均照实，未误补。（f）页界已核实：印刷 p.14 止于 `δ_Y(L) =`，续式印于 p.15。（g）印刷页码 14 未并入 Markdown。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：/tmp/perelmanE_audit_p015.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p015_firstvar.png（该页 600dpi 重渲 + PIL 裁切并 3.2× 放大，PIL 仅用于裁图）
- 核对：式 (7.1) 三行 display 逐项（$\int\sqrt\tau(<Y,\nabla R>+2<\nabla_Y X,X>)d\tau$ 的对称化、`+2\frac{d}{d\tau}<Y,X>`、`-2<Y,\nabla_X X>`、`-4Ric(Y,X)`、`2\sqrt\tau<X,Y>|_{\tau_1}^{\tau_2}`、被积项 $\nabla R-2\nabla_X X-4Ric(X,\cdot)-\frac1\tau X$）；`Thus $\mathcal{L}$-geodesics must satisfy`；式 (7.2)（$\nabla_X X-\frac12\nabla R+\frac{1}{2\tau}X+2Ric(X,\cdot)=0$）；`Given two points p,q and τ₂ > τ₁ > 0 …` 全段（`$\mathcal{L}$-shortest`、`$\sqrt\tau X(\tau)$ has a limit as $\tau\to0$`、`denote by L(q,τ̄)`、`$0\le\tau\le\bar\tau$`、`unique for all pairs (q,τ̄)`、`barrier sense`、`the sense of distributions.`）；`The first variation formula (7.1) implies that …` 段（**被测公式** $\sqrt{L(q,\bar\tau)}=2\sqrt{\bar\tau}X(\bar\tau)$、`$|\nabla L|^2=4\bar\tau|X|^2=-4\bar\tau R+4\bar\tau(R+|X|^2)$`、`We can also compute`）；display $L_{\bar\tau}(q,\bar\tau)=\sqrt{\bar\tau}(R+|X|^2)-\langle X,\nabla L\rangle=2\sqrt{\bar\tau}R-\sqrt{\bar\tau}(R+|X|^2)$；`To evaluate R + |X|² we compute (using (7.2))`；式 (7.3) 三行 display（$R_\tau+\langle\nabla R,X\rangle+2\langle\nabla_X X,X\rangle+2Ric(X,X)$ ／ $R_\tau+\frac1\tau R+2\langle\nabla R,X\rangle-2Ric(X,X)-\frac1\tau(R+|X|^2)$ ／ $=-H(X)-\frac1\tau(R+|X|^2),$）；印刷页码 15；对照 Markdown 第 289–293、295、297–299、301、303、305–307、309、311–313 行。
- 结果：FAIL（一处数学内容错误，已按原图修复，以原图为准）
- 差异与修复（Edit）：第 303 行印刷为 **$\sqrt{L(q,\bar\tau)}=2\sqrt{\bar\tau}X(\bar\tau)$**（L 在根号内），Markdown 却写成 **`\nabla L ( q , \bar { \tau } ) = 2 \sqrt { \bar { \tau } } X ( \bar { \tau } )`**——把根号 $\sqrt{\cdot}$ 误识为梯度算子 $\nabla$，公式由「$L$ 的平方根」变成「$L$ 的梯度」，是**改变数学内容的记号错误**。证据：600dpi 裁片 `/tmp/perelmanE_p015_firstvar.png` 清晰显示左端为带根横的方根号覆盖 L（`√L(q, τ̄) = 2√τ̄X(τ̄),`），`pdftotext -bbox` 亦记录该行 x=368.8–400.1 的 token 为 `∇L(q,` 且整 token 下探至 y=475.9（根号下伸），同行右端的 `√`（x=438.2–448.2, y=446.0–466.4）则明显是独立根号。已 Edit 改为 `implies that$\sqrt { L ( q , \bar { \tau } ) } = 2 \sqrt { \bar { \tau } } X ( \bar { \tau } )$,`；锚串 `grep -c -F` 实测唯一，修复后字符级 difflib 显示第 303 行仅发生 `\nabla` → `\sqrt {` + ` }` 两处改动，无夹带。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对同一锚串实测命中数 = 1（原样含 `\nabla L`），即**原始导出即为此错**，属 **MinerU 导出缺陷，非任何 peer 引入的回归**。附带印证：该错与紧接的下一句 `so that $|\nabla L|^2 = 4\bar\tau|X|^2$` 自洽——由 $\sqrt{L}=2\sqrt{\bar\tau}X$ 平方才得 L 的表达式，印刷的 `so that` 正是这个平方步骤；若真是 $\nabla L$ 则无需 `so that`。（按铁律二，此处仅用作交叉印证，最终依据仍以原页裁片为准。）
- 备注：（a）式 (7.1)/(7.2)/(7.3) 的系数 $\frac12$、$\frac{1}{2\tau}$、$\frac1\tau$、`-4Ric(Y,X)`、`2\sqrt\tau<X,Y>|_{\tau_1}^{\tau_2}` 及 (7.3) 行末逗号，均逐项与原页一致。（b）第 306 行的 `$\langle X,\nabla L\rangle$` 中印刷**确为梯度算子 ∇L**（非根号），已用同页文本层 `− < X, ∇L >` 交叉确认，Markdown 此处正确，未误改——与第 303 行是两种不同记号，不可混同。（c）印刷原样 quirk 保留：`is $\mathcal{L}$-geodesic`（冠词缺 the）。（d）页界已核实：印刷 p.15 止于 (7.3) 式，`where H(X) is the Hamilton's expression for the trace Harnack inequality (with t = −τ). Hence,` 及式 (7.4) 印于 p.16（Markdown 第 315–319 行），归 p.16 条目。（e）印刷页码 15 未并入 Markdown。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：/tmp/perelmanE_audit_p016.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p016.png`）
- 核对：`where H(X) is the Hamilton's expression for the trace Harnack inequality (with t = −τ). Hence,`；式 (7.4)（$\bar\tau^{\frac32}(R+|X|^2)(\bar\tau)=-K+\frac12L(q,\bar\tau),$）；`where K = K(γ, τ̄) denotes the integral ∫₀^{τ̄}τ^{3/2}H(X)dτ, which we'll encounter a few times below. Thus we get`；式 (7.5)（$L_{\bar\tau}=2\sqrt{\bar\tau}R-\frac{1}{2\bar\tau}L+\frac{1}{\bar\tau}K$）；式 (7.6)（$|\nabla L|^2=-4\bar\tau R+\frac{2}{\sqrt{\bar\tau}}L-\frac{4}{\sqrt{\bar\tau}}K$）；`Finally we need to estimate the second variation of L. We compute`；二阶变分 display 两行逐项（$Y\cdot Y\cdot R$、`2<∇_Y∇_Y X,X>`、`2|∇_Y X|²` ／ `2<∇_X∇_Y Y,X>`、`2<R(Y,X),Y,X>`、`2|∇_X Y|²`）；`Now` 与 $\frac{d}{d\tau}\langle\nabla_Y Y,X\rangle=\langle\nabla_X\nabla_Y Y,X\rangle+\langle\nabla_Y Y,\nabla_X X\rangle+2Y\cdot Ric(Y,X)-X\cdot Ric(Y,Y),$；`so, if Y(0) = 0 then`；display $\delta_Y^2(\mathcal{L})=2\langle\nabla_Y Y,X\rangle\sqrt{\bar\tau}+$ 与续行 ∫（$\nabla_Y\nabla_Y R$、`2<R(Y,X),Y,X>`、`2|∇_X Y|²`）及第三行（`+ 2∇_X Ric(Y,Y) − 4∇_Y Ric(Y,X))dτ,`）；`where we discarded the scalar product of −2∇_Y Y with the left hand side of (7.2). Now fix the value of Y at τ = τ̄, assuming |Y(τ̄)| = 1, and construct Y on [0, τ̄] by solving the ODE`；式 (7.8)（$\nabla_X Y=-Ric(Y,\cdot)+\frac{1}{2\tau}Y$）；印刷页码 16；对照 Markdown 第 315、317–319、321、323–325、327–329、331、333–335、337、339–341、343、345–347、349–351、353、355–357 行。
- 结果：PASS
- 备注：（a）四个带横线 τ（$\bar\tau$）的记号逐处核对无误：`K(\gamma,\bar\tau)`、$\bar\tau^{\frac32}$、$L_{\bar\tau}$、$|\nabla L|^2$、$\int_0^{\bar\tau}$、`$\tau=\bar\tau$`、$|Y(\bar\tau)|=1$、`$[0,\bar\tau]$`。（b）全部系数与符号经原页目检 + `pdftotext -f 16 -l 16 -layout` 文本层双通道确认：(7.5) 的 `-1/(2τ̄)L + (1/τ̄)K`、(7.6) 的 `+2/√τ̄ L − 4/√τ̄ K`、(7.8) 的 **`+`**$\frac{1}{2\tau}Y$（文本层 `∇X Y = −Ric(Y, ·) + 1/(2τ) Y` 确认正号，未被误改为负号）均与印刷一致。（c）印刷原样 quirk 保留：`is the Hamilton's expression`（冠词用 the）、`which we'll encounter`（弯引号）。（d）二阶变分的两个 display 在印刷为上下两行、Markdown 合并为一个 `array`（第二行以 `=` 开头），属排版合并，文字与公式无增删。（e）页界已核实：印刷 p.16 止于式 (7.8) 与页码 16；`We compute / d/dτ<Y,Y> = … / so |Y(τ)|² = τ/τ̄ …` 印于 p.17（`pdftotext -f 17` 实测），对应 Markdown 第 359–365 行，不计入本页。（f）印刷页码 16 未并入 Markdown。（g）本轮无改动。

## p.017（PDF p.17 / 印刷 p.17）
- PNG：/tmp/perelmanE_audit_p017.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p017_eq710.png、p017_hess1.png、p017_hess2.png（该页 600dpi 重渲 + PIL 裁切放大，PIL 仅用于裁图）
- 核对：`We compute` 与 $\frac{d}{d\tau}\langle Y,Y\rangle=2Ric(Y,Y)+2\langle\nabla_X Y,Y\rangle=\frac1\tau\langle Y,Y\rangle,$；`so |Y(τ)|² = τ/τ̄, and in particular, Y(0) = 0. Making a substitution into (7.7), we get`；$Hess_{\mathcal{L}}(Y,Y)\le$ 两行 display（$\int_0^{\bar\tau}\sqrt\tau(\nabla_Y\nabla_Y R+2\langle R(Y,X),Y,X\rangle+2\nabla_X Ric(Y,Y)-4\nabla_Y Ric(Y,X)$ 续 $+2|Ric(Y,\cdot)|^2-\frac2\tau Ric(Y,Y)+\frac{1}{2\tau\bar\tau})d\tau$）；`To put this in a more convenient form, observe that` 与两行 display（$Ric_\tau+\nabla_X Ric+2Ric(\nabla_X Y,Y)$ 续 $Ric_\tau+\nabla_X Ric+\frac1\tau Ric-2|Ric(Y,\cdot)|^2,$）；`so` 与式 (7.9)（$\frac{1}{\sqrt{\bar\tau}}-2\sqrt{\bar\tau}Ric(Y,Y)-\int_0^{\bar\tau}\sqrt\tau H(X,Y)d\tau,$）；`where` 与 H(X,Y) 两行 display；`is the Hamilton's expression for the matrix Harnack inequality (with t = −τ). Thus`；式 (7.10)（**被测公式**）；`A field Y(τ) along 𝓛-geodesic γ(τ) is called 𝓛-Jacobi, if it is the derivative of a variation of γ among 𝓛-geodesics. For an 𝓛-Jacobi field Y with |Y(τ̄)| = 1 we have`；页末 display $\frac{d}{d\tau}|Y|^2=2Ric(Y,Y)+2\langle\nabla_X Y,Y\rangle=2Ric(Y,Y)+2\langle\nabla_Y X,Y\rangle$；印刷页码 17；对照 Markdown 第 359–363、365、367–369、371、373–375、377、379–381、383、385–387、389、391–393、395、397–399 行。
- 结果：FAIL（一处数学内容错误，已按原图修复，以原图为准）
- 差异与修复（Edit）：第 392 行式 (7.10) 印刷为 $\triangle L\le-2\sqrt{\bar\tau}R+\frac{n}{\sqrt{\bar\tau}}-\frac{1}{\bar\tau}K$，Markdown 三处却全写作**无上划线的 $\tau$**（`- 2 \sqrt {\tau} R`、`\frac {n}{\sqrt {\tau}}`、`\frac {1}{\tau}`）。在本节语境中 $\tau$ 是变动积分变量、$\bar\tau$ 是固定末端时刻，二者是不同量，故这是改变数学内容的记号错误。证据：600dpi 裁片 `/tmp/perelmanE_p017_eq710.png`（3.5×）逐字显示三处均为 $\bar\tau$（根号内与分母里的短横清晰可辨）；同页式 (7.9)（第 380 行）本已正确写作 `\bar {\tau }`，可作内部对照。已 Edit 改为 `\triangle L \leq - 2 \sqrt {\bar {\tau }} R + \frac {n}{\sqrt {\bar {\tau }}} - \frac {1}{\bar {\tau }} K\tag{7.10}`；锚串 `grep -c -F` 实测唯一，修复后字符级 difflib 显示第 392 行仅新增 3 组 `bar {` + ` }`，无夹带。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对同一锚串实测命中数 = 1（原样为无划线写法），即**原始导出即缺三条上划线**，属 **MinerU 导出缺陷，非任何 peer 引入的回归**。
- 备注：（a）**一处疑似记号差异、经裁片排除**：两处 $Hess$ 的下标，150dpi 下曾被读作花体 $\mathcal{L}$；600dpi 裁片 `/tmp/perelmanE_p017_hess1.png`（5×）显示为**普通斜体 L**（印刷在正文处确实另用 $\mathcal{L}$ 写作 `𝓛-geodesic`、`𝓛-Jacobi`，Markdown 对应写作 `\mathcal {L}`，两处分别正确），故 `Hess _ {L}` 忠实，不判缺陷。（b）第 368 行 array 内 `Hess _ {L} (Y, Y) \leq \\ \int_…` 的 `\\` 是**合法的行分隔符**：印刷正把「Hess_L(Y,Y) ≤」与随后的积分分作两行排布，该 array 复现同一换行。另实测全文件 `grep -o -E '\\\\[a-zA-Z]+'` 无命中，即不存在旧审计曾修过的「多余双反斜线命令」类缺陷。（c）H(X,Y) 式中的 `2 < R(Y,X)Y,X >`（两参数内积）与 (7.7) 式中的 `2 < R(Y,X),Y,X >`（三参数）是印刷本身的两种不同写法，Markdown 分别照实，未统一。（d）式 (7.9)、被积上界 $\int_0^{\bar\tau}$、Hess display 中的 $\frac{1}{2\tau\bar\tau}$、$|Y(\tau)|^2=\frac{\tau}{\bar\tau}$ 等带横线 τ 均已逐处核对正确，本页仅 (7.10) 一处漏划。（e）页界已核实：印刷 p.17 止于 $\frac{d}{d\tau}|Y|^2$ display 与页码 17，该 display 无句末标点，续文属 p.18。（f）印刷页码 17 未并入 Markdown。

## p.018（PDF p.18 / 印刷 p.18）
- PNG：/tmp/perelmanE_audit_p018.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p018.png`）
- 核对：p.17 续行 display $=2Ric(Y,Y)+\frac1{\sqrt{\bar\tau}}Hess_{\mathcal L}(Y,Y)\le\frac1{\bar\tau}-\frac1{\sqrt{\bar\tau}}\int_0^{\bar\tau}\tau^{\frac12}H(X,\tilde Y)d\tau,$（式 7.11）；`where Ỹ is obtained by solving ODE (7.8) with initial data Ỹ(τ̄) = Y(τ̄).`（**被测标点**）；`Moreover, the equality in (7.11) holds only if Ỹ is 𝓛-Jacobi and hence` 与 $\frac{d}{d\tau}|Y|^2=2Ric(Y,Y)+\frac1{\sqrt{\bar\tau}}Hess_{\mathcal L}(Y,Y)=\frac1{\bar\tau}$；`Now we can deduce an estimate for the jacobian J …` 段（`𝓛-exp_𝒳(τ̄) = γ(τ̄)`、`X as the limit of √τ γ̇(τ) as τ → 0`）；式 (7.12)（$\frac{n}{2\bar\tau}-\frac12\bar\tau^{-\frac32}K,$）；`with equality only if 2Ric + \frac1{\sqrt{\bar\tau}}Hess_{\mathcal L} = \frac1{\bar\tau}g.`、`Let l(q,τ) = \frac{1}{2\sqrt{\tau}}L(q,τ) be the reduced distance.`、`Then along an 𝓛-geodesic γ(τ) we have (by (7.4))`；display $\frac{d}{d\tau}l(\tau)=-\frac{1}{2\bar\tau}l+\frac12(R+|X|^2)=-\frac12\bar\tau^{-\frac32}K,$；`so (7.12) implies that τ^{-n/2}exp(−l(τ))J(τ) is nonincreasing in τ along γ,`（**被测标点**）`and monotonicity is strict …`；`Ṽ(τ) = ∫_M τ^{-n/2}exp(−l(q,τ))dq.`、`( Alternatively, one could obtain the same monotonicity by integrating the differential inequality`；式 (7.13)（$l_{\bar\tau}-\triangle l+|\nabla l|^2-R+\frac{n}{2\bar\tau}\ge0,$）；`which follows immediately from (7.5), (7.6) and (7.10). Note also a useful inequality`；式 (7.14)（$2\triangle l-|\nabla l|^2+R+\frac{l-n}{\bar\tau}\le0,$）；`which follows from (7.6), (7.10).)`；`On the other hand, if we denote L̄(q,τ) = 2√τ L(q,τ), then from (7.5), (7.10) we obtain`；式 (7.15)（$\bar L_{\bar\tau}+\triangle\bar L\le2n$）；`Therefore, the minimum of L̄(·, τ̄) − 2nτ̄ …` 段与括注开头 `(The lower bound for`；印刷页码 18；对照 Markdown 第 399–403、405、407、409–411、413、415–417、419、421–423、425、427–429、431、433、435–437、439 行。
- 结果：PASS±（两处印刷标点缺失，已按原图修复）
- 差异与修复（逐处 Edit；证据为 150dpi 目检 + `pdftotext -f 18 -l 18 -layout` 文本层双通道）：
  1. 第 405 行 `with initial data$\tilde { Y } ( \bar { \tau } ) = Y ( \bar { \tau } )$ Moreover,` **缺句点**，印刷为 `Ỹ(τ̄ ) = Y (τ̄ ).`（文本层明载句点）。已改为 `$Y ( \bar { \tau } )$. Moreover,`。
  2. 第 419 行 `is nonincreasing in$\tau$along$\gamma$ and monotonicity is strict` **缺逗号**，印刷为 `along γ ,`（文本层明载逗号）。已改为 `along$\gamma$, and monotonicity is strict`。
  - 两处锚串 `grep -c -F` 均实测唯一；修复后字符级 difflib 显示第 405、419 行各仅新增一个字符（`.` 与 `,`），无夹带。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对两处锚串实测命中数均为 1（原样缺标点），故**两处均为 MinerU 导出缺陷，非任何 peer 引入的回归**。
- 备注：（a）**三处疑似数学差异、经 bbox 文本层逐 token 排除（Markdown 均正确）**：(i) 式 (7.12) 的 `\bar{\tau}^{-\frac32}`——同行的 `\frac{n}{2\bar\tau}` 与 `\bar\tau^{-\frac32}` 两个 τ token 分别在 bbox 中报为 `τ̄`（x=304.6–315.5 与 x=340.8–345.9），证实印刷此处三处**全带划线**，Markdown 写法正确；(ii) `Let l(q,τ) = \frac{1}{2\sqrt{\tau}}L(q,τ)`——该行根号下的 τ token（x=422.0–425.8）文本层报为**无划线** `τ`，而同句稍前的 `\frac1{\sqrt{\bar\tau}}Hess_{\mathcal L}` 根号下的 τ 报为 `τ̄`，两者可直接对照，故无划线的 `\sqrt {\tau }` 忠实；(iii) `L̄(q,τ) = 2√τ L(q,τ)` 与 (7.15) 的 `L̄_τ̄ + △L̄ ≤ 2n`——150dpi 下曾读作波浪号 L̃，但 `pdftotext -bbox` 该两处 token 实测为 `L̄`（U+004C + U+0304 组合长音符，即**上划线**而非 U+0303 波浪号），Markdown 的 `\bar { L }` 忠实，未误改。（b）注意印刷在同一页同时使用 `L̄`（带划线）与 `Ṽ`（带波浪号）两种记号，Markdown 分别写作 `\bar { L }` 与 `\tilde { V }`，未混同。（c）排版级伪影登记不改：`\mathrm { e x p }` 与 `\mathcal { L } \mathrm { e x p } _ { X }` 的正体字母间距扁平化（与 p.7/p.9 同族）。（d）式 (7.13)/(7.14)/(7.15) 的分式结构与 $l-n$、$\frac{n}{2\bar\tau}$ 等逐项一致；(7.15) 末无标点，Markdown 亦无，未误补。（e）页界已核实：印刷 p.18 止于 `(The lower bound for`（第 439 行括注的续文），归 p.19 条目。（f）印刷页码 18 未并入 Markdown。

## p.019（PDF p.19 / 印刷 p.19）
- PNG：/tmp/perelmanE_audit_p019.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p019_epsdef.png、halfeps2.png、expeps2.png、gammaT2.png（该页 600dpi 重渲 + PIL 裁切并 3× 放大，PIL 仅用于裁图）
- 核对：p.18 续文 `l is much easier to obtain since the evolution equation R_τ = −△R − 2|Ric|²` 与 $R(\cdot,\tau)\ge-\frac{n}{2(\tau_0-\tau)}$（$\tau\in[0,\tau_0]$）；7.2 全段（`nonnegative curvature operator`、`Hamilton's differential Harnack inequalities`、`$H(X,Y)\ge-Ric(Y,Y)(\frac1\tau+\frac1{\tau_0-\tau})\ge-R(\frac1\tau+\frac1{\tau_0-\tau})|Y|^2`、$H(X)\ge-R(\frac1\tau+\frac1{\tau_0-\tau})$、`whenever τ is bounded away from τ₀`、`(say, τ ≤ (1−c)τ₀, c > 0)`）；式 (7.16)（$|\nabla l|^2+R\le\frac{Cl}{\tau},$）；`and for 𝓛-Jacobi fields Y`；式 (7.17)（$\frac{d}{d\tau}\log|Y|^2\le\frac1\tau(Cl+1)$）；7.3 全段（`weakened version of the no local collapsing theorem 4.1`、$t_k-r_k^2\le t\le t_k$、**被测记号四处**：$\tau_k(t)=t_k-t,\ p=p_k,\ \epsilon_k=r_k^{-1}Vol(B_k)^{\frac1n}$、$\frac12\epsilon_k^{-\frac12}$、`$\exp(-\frac12\epsilon_k^{-\frac12})$`、`$\gamma(t_k-\frac12T)=q_k$` 与 `$t\in[0,\frac12T]$`；以及正确项 $\tilde V_k(\epsilon_k r_k^2)<3\epsilon_k^{\frac n2}$、`2\epsilon_k^{\frac n2}`、`min l_k(\cdot,t_k-\frac12T)\le\frac n2`、`Ṽ_k(t_k) ≤ Ṽ_k(ε_k r_k²)`）；`A similar argument shows … is bounded below by κ.` 段；印刷页码 19；对照 Markdown 第 439、441、443–445、447、449–451、453、455 行。
- 结果：PASS
- 备注：（a）**四处曾高度疑似数学错误、经 600dpi 裁片逐一举证排除，Markdown 全部正确、本轮未改动**：`$r_k^{-1}$` 与 `$Vol(B_k)^{\frac{1}{n}}$`（裁片 `epsdef.png`：150dpi 下我读作 $r_k^{-n}$ 与 $Vol(B_k)^{-\frac n2}$，实为 $r_k^{-1}$ 与 $Vol(B_k)^{\frac1n}$）；`$\frac12\epsilon_k^{-\frac12}$`（裁片 `halfeps2.png`：150dpi 下读作 $-\frac n2$，实为 $-\frac12$）；`$\exp(-\frac12\epsilon_k^{-\frac12})$`（裁片 `expeps2.png`：同上）；`$\gamma(t_k-\frac12T)=q_k$` 与 `$t\in[0,\frac12T]$`（裁片 `gammaT2.png`：150dpi 下读作 $\frac n2 T$，实为 $\frac12 T$）。四处的共同成因是 150dpi 下上标小分数的分子「1」笔画过细被误读为「n」；`pdftotext -layout` 的公式区同样被分子/分母分行打散，不能单独作为判据，故一律回到裁片。（b）本条与 p.10 的 ≤/≪、p.12 的 M/𝓜、p.13 的 γ̇/ṽ、p.14 的 L/Ł、p.15 的 √L/∇L、p.18 的 L̄/L̃ 同属「150dpi 小字形误读」类，已全部以裁片或 bbox 逐 token 裁决。（c）式 (7.16) 末的逗号、(7.17) 末无标点，与印刷一致，Markdown 未误补。（d）7.2 段中 $\frac1{\tau_0-\tau}$ 的分母确为 $\tau_0-\tau$（非 $\tau_0$），文本层 `1/(τ0 − τ)` 与原页互证，Markdown 正确。（e）排版级伪影登记不改：第 441 行 `( \mathrm { s a y } , \tau \le ( 1 - c ) \tau _ { 0 } , c > 0 )` 的正体字母间距扁平化（与 p.7/p.9/p.11 同族）。（f）印刷原样 quirk 保留：印刷 `let τ_k(t) = t_k − t, p = p_k, ε_k = …` 三个逗号后均有空格。（g）页界已核实：印刷 p.19 止于 `is bounded below by κ.` 与页码 19；7.4\* 段与节标题 `8 No local collapsing theorem II` 印于 p.20（Markdown 第 457–459 行），不计入本页。（h）印刷页码 19 未并入 Markdown。

## p.020（PDF p.20 / 印刷 p.20）
- PNG：/tmp/perelmanE_audit_p020.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p020.png`）
- 核对：7.4\* 全段（`natural modifications of those in the classical variational theory of geodesics`、`[L-Y]`、``length''`、`a linear parabolic equation`）；节标题 `8 No local collapsing theorem II`；8.1 句（**被测标点**）；Definition 全段（`κ-collapsed at (x₀,t₀) on the scale r > 0`、`$|Rm|(x,t)\le r^{-2}$ for all (x,t) satisfying dist_{t₀}(x,x₀) < r and t₀ − r² ≤ t ≤ t₀`、`metric ball B(x₀,r²) at time t₀`、`less than κr^n.`，**被测标点**）；8.2 Theorem 全段（`For any A > 0 there exists κ = κ(A) > 0`、`0 ≤ t ≤ r₀²`、`|Rm|(x,t) ≤ r₀^{-2}`、`dist_0(x,x₀) < r₀`、`at time zero is at least A^{-1}r₀^n`、`can not be κ-collapsed on the scales less than r₀`、`at a point (x, r₀²) with dist_{r₀²}(x,x₀) ≤ Ar₀.`，**被测标点**）；Proof 全段（`By scaling we may assume r₀ = 1`、`dist_1(x,x₀) = A`、`constructions of 7.1 choosing p = x, τ(t) = 1 − t`、`on the scale r ≤ 1`、`Ṽ(r²) must be very small`、`Ṽ(1) can not be small unless min l(x,1/2) over x satisfying dist_{1/2}(x,x₀) ≤ 1/10 is large.`、`estimate l, or equivalently L̄, in that ball`、`Recall that L̄ satisfies the differential inequality (7.15)`）；8.3 Lemma 与 (a) 段（`Suppose Ric(x,t₀) ≤ (n−1)K when dist_{t₀}(x,x₀) < r₀`、`d(x,t) = dist_t(x,x₀) satisfies at t = t₀ outside B(x₀,r₀)`）；display $d_t-\triangle d\ge-(n-1)(\frac23Kr_0+r_0^{-1})$；括注 `(the inequality must be understood in the barrier sense, when necessary)`；印刷页码 20；对照 Markdown 第 457、459、461、463、465、467、469、471–473、475 行。
- 结果：PASS±（三处印刷句点缺失，已按原图修复）
- 差异与修复（逐处 Edit；证据为 150dpi 目检 + `pdftotext -f 20 -l 20 -layout` 文本层双通道）：
  1. 第 461 行 8.1 句末 `that was used in$7 . 3$` **缺句点**，印刷为 `used in 7.3.`。已补为 `that was used in$7 . 3$.`。
  2. 第 463 行 Definition 末 `at time$t _ { 0 }$is less than$\kappa r ^ { n }$` **缺句点**，印刷为 `at time t0 is less than κr^n .`。已补句点。
  3. 第 465 行 8.2 Theorem 末 `\leq A r _ { 0 }$` **缺句点**，印刷为 `≤ Ar0 .`。已补句点。
  - 三处锚串 `grep -c -F` 均实测唯一；修复后字符级 difflib 显示第 461、463、465 行各仅新增一个 `.`，无夹带。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对三处锚串实测命中数均为 1（原样缺句点），故**三处均为 MinerU 导出缺陷，非任何 peer 引入的回归**。
- 备注：（a）**四处小分数曾高度疑似被改成 n/2，经 bbox 逐 token 排除（Markdown 全部正确）**：`min l(x,\frac12)` 与 `dist_{\frac12}(x,x₀) ≤ \frac{1}{10}`——bbox 实测分子 token 分别为 `1`(x=261.7–266.0, y=467.8–475.8)、`1`(x=386.8–390.4)、`1`(x=446.5–450.8)，均为单个窄字形「1」而非「n」；Lemma (a) 的 `\frac{2}{3}Kr_0` 经文本层分子 `2`／分母 `3` 分行互证。四处均与 Markdown 一致。（b）同页 `\bar { L }` 与 `L<sup>¯</sup>` 两种写法并存（同一段内指同一记号 L̄，渲染一致），与 `7 . 3`／`7 . 1` 的编号字母间距扁平化、`${ \bf 7 . 4 ^ { * } }$` 的粗体数学编号同属排版级伪影，登记不判缺陷、不改。（c）式 (7.16)-式 (7.17) 等前页式号引用、以及 `$0\le t\le r_0^2$` 的上下界方向与 `A^{-1}r_0^n` 的负指数，均与印刷一致。（d）8.3 Lemma 在印刷无独立编号式；其 (a) 的 display 末无标点（紧接括注），Markdown 亦无，未误补。（e）页界已核实：印刷 p.20 止于括注与页码 20；(b) 分支（`cf. [H 4, §17]`）印于 p.21，归 p.21 条目。（f）印刷页码 20 未并入 Markdown。

## p.021（PDF p.21 / 印刷 p.21）
- PNG：/tmp/perelmanE_audit_p021.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p021.png`）
- 核对：(b) 分支全段（`cf. [H 4,§17]`、`Ric(x,t₀) ≤ (n−1)K when dist_{t₀}(x,x₀) < r₀`、`or dist_{t₀}(x,x₁) < r₀`、`Then`）；display $\frac{d}{dt}dist_t(x_0,x_1)\ge-2(n-1)(\frac23Kr_0+r_0^{-1})$ at $t=t_0$；`Proof of Lemma.` (a) 段（$d_t(x)=\int_\gamma-Ric(X,X)$、`shortest geodesic between x and x₀`、`X is its unit tangent vector, On the other hand,`、$\triangle d\le\sum_{k=1}^{n-1}s''_{Y_k}(\gamma)$、`vanishing at x₀`、`orthonormal basis at x when complemented by X`、`second variation along Y_k of the length of γ`、`Take Y_k to be parallel between x and x₁, and linear between x₁ and x₀, where d(x₁,t₀) = r₀.`（**被测标点**）`Then`）；两行 display 逐项（$\int_{r_0}^{d(x,t_0)}-Ric(X,X)ds+\int_0^{r_0}(\frac{s^2}{r_0^2}(-Ric(X,X))+\frac{n-1}{r_0^2})ds$ 续 $=\int_\gamma-Ric(X,X)+\int_0^{r_0}(Ric(X,X)(1-\frac{s^2}{r_0^2})+\frac{n-1}{r_0^2})ds\le d_t+(n-1)(\frac23Kr_0+r_0^{-1})$）；`The proof of (b) is similar.`；`Continuing the proof of theorem, apply the maximum principle to the function` 段（$h(y,t)=\phi(d(y,t)-A(2t-1))(\bar L(y,1-t)+2n+1)$、`equal 1 on (-∞, 1/20)`、`rapidly increasing to infinity on (1/20, 1/10)`）；式 (8.1)（$2(\phi')^2/\phi-\phi''\ge(2A+100n)\phi'-C(A)\phi,$）；`for some constant C(A) < ∞. …` 段（`$\bar L+2n+1\ge1$ for $t\ge\frac12$`、`min h(y,1) ≤ h(x,1) = 2n+1`、`min h(y,\frac12) is achieved for some y satisfying d(y,\frac12) ≤ \frac1{10}.`（**被测标点**）`Now we compute`）；式 (8.2)、(8.3)、(8.4)（方框算子 □h、`-2<\nabla\phi\nabla\bar L>`、`(\bar L_t-\triangle\bar L)\phi`、`+2(\phi')^2/\phi`）；`At a minimum point of h we have ∇h = 0, so (8.2) becomes`；印刷页码 21；对照 Markdown 第 477、479–481、483、485–487、489、491、493–495、497、499–501、503–505、507、509–511 行。
- 结果：PASS±（两处印刷句点缺失，已按原图修复）
- 差异与修复（逐处 Edit；证据为 150dpi 目检 + `pdftotext -f 21 -l 21 -layout` 文本层双通道）：
  1. 第 483 行 `where$d ( x _ { 1 } , t _ { 0 } ) = r _ { 0 }$ Then` **缺句点**，印刷为 `d(x1 , t0 ) = r0 . Then`（文本层明载句点）。已补为 `= r _ { 0 }$. Then`。
  2. 第 497 行 `$d ( y , { \frac { 1 } { 2 } } ) \leq { \frac { 1 } { 10 } }$ Now we compute` **缺句点**，印刷为 `d(y, ½) ≤ 1/10 . Now we compute`（文本层该句点被 -layout 拆到独立行）。已补为 `…{ \frac { 1 } { 10 } }$. Now we compute`。
  - 两处锚串 `grep -c -F` 均实测唯一；修复后字符级 difflib 显示第 483、497 行各仅新增一个 `.`，无夹带。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对两处锚串实测命中数均为 1（原样缺句点），故**两处均为 MinerU 导出缺陷，非任何 peer 引入的回归**。
- 备注：（a）**一处曾疑似标点错误、经文本层排除**：第 483 行 `X is its unit tangent vector, On the other hand,` 的逗号——150dpi 下我读作句点，但 `pdftotext` 文本层作 `unit tangent vector, On the other hand,`，证实**印刷原样即用逗号**（而非句点），Markdown 忠实照 print 保留，未「纠正」，不判缺陷。（b）本页全部小分数（$\frac23$、$\frac1{20}$、$\frac1{10}$、$\frac12$、$100n$、$2n+1$）均逐处核对一致；其中 (8.1) 的 `100n` 已确认不是 `l00n` 或 `100η`。（c）方框热算子 □h 在 (8.2)(8.4) 印为「方框 + h」，Markdown 用 `\Box h`，文本层作 `✷h`，三通道一致；\bigtriangleup（(a) 段）与 \triangle（display）两种三角算子字形是印刷/导出的同义变体，不判缺陷。（d）第 480 行印刷作 `at  t = t0`（`at` 后有空格，斜体间距排布），Markdown 作 `at $t = t _ {0}$`，可读且语义无歧义，登记不判缺陷。（e）印刷原样 quirk 保留：`Proof of Lemma. (a) Clearly,`（逗号）；Markdown 未把 (8.3) 的缩进排布当作缺陷。（f）页界已核实：印刷 p.21 止于式 (8.4) 与页码 21，续文印于 p.22。（g）印刷页码 21 未并入 Markdown。

## p.022（PDF p.22 / 印刷 p.22）
- PNG：/tmp/perelmanE_audit_p022.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p022_integrals.png（该页 600dpi 重渲 + PIL 裁切并 3× 放大，PIL 仅用于裁图）
- 核对：`Now since d(y,t) ≥ 1/20 whenever φ′ ≠ 0, and since Ric ≤ n − 1 in B(x₀,1/20),`（**被测标点**）`we can apply our lemma (a) to get d_t − △d ≥ −100(n−1) on the set where φ′ ≠ 0. Thus, using (8.1) and (7.15), we get`；display $\square h\ge-(\bar L+2n+1)C(A)\phi-2n\phi\ge-(2n+C(A))h$；`This implies that min h can not decrease too fast, and we get the required estimate.`；节标题 `9 Differential Harnack inequality for solutions of the conjugate heat equation`；9.1. Proposition 全段（`0 ≤ t ≤ T`、`u = (4π(T−t))^{-n/2}e^{-f}`、`conjugate heat equation □*u = −u_t − △u + Ru = 0`、`v = [(T−t)(2△f − |∇f|² + R) + f − n]u`、`satisfies`）；式 (9.1)（$\square^*v=-2(T-t)|R_{ij}+\nabla_i\nabla_jf-\frac{1}{2(T-t)}g_{ij}|^2$）；`Proof. Routine computation.`；`Clearly, this proposition immediately implies the monotonicity formula (3.4); its advantage over (3.4) shows up when one has to work locally.`；9.2. Corollary；9.3. Corollary（`then v ≤ 0 for all t < T.`，**被测标点**）；其 Proof（`ordinary heat equation h_t = △h`、`$\frac{d}{dt}\int hu=0$ and `$\frac{d}{dt}\int hv\ge0$`、**被测公式** `the limit of ∫hv as t → T is nonpositive`、`But it is easy to see, that this limit is in fact zero.`）；9.4. Corollary 与式 (9.2)（$-\frac{d}{dt}f(\gamma(t),t)\le\frac12(R(\gamma(t),t)+|\dot\gamma(t)|^2)-\frac{1}{2(T-t)}f(\gamma(t),t)$）；印刷页码 22；对照 Markdown 第 511–513、515–517、519、521、523、525–527、529、531、533、535、537、539、541–543 行。
- 结果：FAIL（一处数学内容错误 + 两处标点缺失；已按原图逐处修复，以原图为准）
- 差异与修复（逐处 Edit）：
  1. 第 537 行 Proof 段 `the limit of hv as$t \to T$ is nonpositive` —— **积分号 ∫ 丢失**：印刷为 `the limit of $\int hv$ as $t\to T$`，Markdown 写成裸的 `hv`。这是把「$\int hv$ 的极限」错成「$hv$ 的极限」，改变数学内容。600dpi 裁片 `/tmp/perelmanE_p022_integrals.png` 清晰显示该处为 `the limit of ∫ hv as t → T`（同一裁片亦确认上一句的 `\frac{d}{dt}\int hu = 0` 与 `\frac{d}{dt}\int hv \ge 0` 两处 ∫ 在 Markdown 中本已正确保留，只有「limit of」后这一处丢失）。已 Edit 为 `the limit of$\int h v$ as$t \to T$ is nonpositive`。
  2. 第 535 行 9.3 Corollary 末 `then$v \leq 0$for all$t < T$` **缺句点**，印刷为 `for all t < T.`。已补句点。
  3. 第 513 行 `in$B ( x _ { 0 } , \textstyle \frac { 1 } { 20 } )$ we can apply our lemma` **缺逗号**，印刷为 `B(x0 , 1/20 ), we can apply`。已补为 `…{ \frac { 1 } { 20 } )$, we can apply our lemma`。
  - 三处锚串 `grep -c -F` 均实测唯一；修复后字符级 difflib 显示第 513 行新增 `,`、第 535 行新增 `.`、第 537 行把 ` hv` 换成 `$\int h v$`，无夹带。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对三处锚串实测命中数均为 1（含原样缺失 ∫ 的 `the limit of hv as$t \to T$`），故**三处均为 MinerU 导出缺陷，非任何 peer 引入的回归**。
- 备注：（a）说明：`pdftotext -f 22 -l 22 -layout` 在本段把三处 ∫ 全部吞掉（输出作 `dtd hu = 0`、`the limit of hv as t → T`），若只看文本层会误判为「印刷无积分号」；按 ask 的规定，公式一律回到裁片判读，故以 600dpi 裁片为准。（b）方框热算子在 (9.1) 前印为 □\*、在 (8.2)(8.4) 前印为 □，Markdown 分别用 `\Box ^ { * }` 与 `\Box`，与印刷的区分一致，未混同。（c）9.1 中 $u=(4\pi(T-t))^{-\frac n2}e^{-f}$ 的负指数、式 (9.1) 的 $-\frac{1}{2(T-t)}$、式 (9.2) 的 $-\frac{1}{2(T-t)}$ 及首项负号，经原页与文本层双通道核对一致。（d）排版级伪影登记不改：`\mathrm { ( a ) }`（`lemma (a)`）与 `\textstyle` 的正体/紧凑排版扁平化。（e）印刷原样 quirk 保留：`But it is easy to see, that this limit is in fact zero.`（`see,` 后多余逗号），Markdown 同文不改。（f）页界已核实：印刷 p.22 止于式 (9.2) 与页码 22；`Under assumptions of the previous corollary`（9.4 正文）与其续文印于 p.23。（g）印刷页码 22 未并入 Markdown。

## p.023（PDF p.23 / 印刷 p.23）
- PNG：/tmp/perelmanE_audit_p023.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p023_ft_half.png、boxfbar_tight.png、Rbound2.png（该页 600dpi 重渲 + PIL 裁切放大，PIL 仅用于裁图）
- 核对：p.22 续文 Proof（$f_t=-\triangle f+|\nabla f|^2-R+\frac{n}{2(T-t)}$、`and $v\le0$ we get`、**被测记号** $f_t+\frac{1}{2}R-\frac12|\nabla f|^2-\frac{f}{2(T-t)}\ge0$、**被测记号** $-\frac{d}{dt}f(\gamma(t),t)=-f_t-\langle\nabla f,\dot\gamma(t)\rangle\le -f_t+\frac12|\nabla f|^2+\frac12|\dot\gamma|^2$、`Summing these two inequalities, we get (9.2).`）；9.5. Corollary 全段（`where the limit δ-function is concentrated`、`$f(q,t)\le l(q,T-t)$`、`where l is the reduced distance, defined in 7.1, using p and τ(t) = T − t.`，**被测标点**）；`Proof. Use (7.13) in the form □*exp(−l) ≤ 0.`（**被测标点**）；9.6 Remark 全段（`infinitesimal behavior of the fundamental solutions`、`(g_ij)_t = A_ij(t)`、$\square=\frac{\partial}{\partial t}-\triangle$、$\square^*=-\frac{\partial}{\partial t}-\triangle-\frac12A$、$\frac{d}{dt}\int uv=\int((\square u)v-u(\square^*v))$、`(Here $A=g^{ij}A_{ij}$.)`、$u=(-4\pi t)^{-\frac n2}e^{-f}$ for $\square^*$、`starting as δ-function at some point (p, 0).`（**被测标点**）、**被测记号** $(\square\bar f+\frac{\bar f}{t})(q,t)$、`where $\bar f=f-\int fu$`、`of the order $O(1)$ for $(q,t)$ near $(p,0)$`、`$A_{ij}=-2R_{ij}$`、**被测记号** $(\square\bar f+\frac{\bar f}{t})(q,t)=o(1)$、`in fact, it is $O(|pq|^2+|t|)$ in this case.`）；9.7\* 全段（`[L-Y]`、`Hamilton [H 7,8]`、`[E 2]`）；节标题 `10 Pseudolocality theorem`；10.1. Theorem 全段（`For every α > 0 there exist δ > 0, ε > 0`、`$0\le t\le(\epsilon r_0)^2$`、**被测记号** `$R(x)\ge-r_0^{-2}$`、`$Vol(\partial\Omega)^n\ge(1-\delta)c_nVol(\Omega)^{n-1}$`、`$c_n$ is the euclidean isoperimetric constant`、$|Rm|(x,t)\le\alpha t^{-1}+(\epsilon r_0)^{-2}$、`whenever $0<t\le(\epsilon r_0)^2$, $d(x,t)=dist_t(x,x_0)<\epsilon r_0$.`，**被测标点**）；印刷页码 23；对照 Markdown 第 543–545、547、549、551、553、555、557 行。
- 结果：PASS±（四处印刷句点缺失，已按原图修复）
- 差异与修复（逐处 Edit；证据为 150dpi 目检 + `pdftotext -f 23 -l 23 -layout` 文本层双通道）：
  1. 第 547 行 9.5 Corollary 末 `using p and$\tau ( t ) = T - t$` **缺句点**，印刷为 `τ (t ) = T − t .`。已补句点。
  2. 第 549 行 `Proof. Use (7.13) in the form$\Box ^ { * } \mathrm { e x p } ( - l ) \le 0$` **缺句点**，印刷为 `✷∗ exp(−l) ≤ 0 .`。已补句点。
  3. 第 551 行 `starting as δ-function at some point$( p , 0 )$ Then for general` **缺句点**，印刷为 `at some point (p, 0 ).`。已补句点。
  4. 第 557 行 10.1 Theorem 末 `< \epsilon r _ { 0 }$` **缺句点**，印刷为 `< ǫr0 .`。已补句点。
  - 四处锚串 `grep -c -F` 均实测唯一（第 4 处因同串在 8.2 Proof 段亦出现，另以 `^ { 2 } , d ( x , t ) = dist _ { t } …` 前缀锁定唯一）；修复后字符级 difflib 显示第 547、549、551、557 行各仅新增一个 `.`，无夹带。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对四处锚串实测命中数均为 1（原样缺句点），故**四处均为 MinerU 导出缺陷，非任何 peer 引入的回归**。
- 备注：（a）**四处曾高度疑似数学错误、经 600dpi 裁片逐一举证排除，Markdown 全部正确**：(i) $f_t+\frac{t}{2}R-\frac{t}{2}|\nabla f|^2$——裁片 `ft_half.png`（3×）显示两处分数均为 $\frac{1}{2}$（非 $\frac{t}{2}$），文本层亦作 `21 R− 12 |∇f |2`，MD 的 `\frac{1}{2}` 正确；(ii) `$-\nabla f,\dot\gamma(t)>\ \ge\ -f_t+\cdots$`——150dpi 下读作 `≥`，但文本层作 `−ft − < ∇f, γ̇(t) >≤ −ft + 21 |∇f |2 + 21 |γ̇|2`，即印刷确为 `≤`，MD 的 `\leq` 正确；(iii) `$(\square\bar f+\frac{\bar f}{t})(q,t)$`——裁片 `boxfbar_tight.png`（9×）显示 □ 后与分数分子上**两个 f 都带短横**，文本层亦作 `(✷f¯+ ft )(q, t)`，MD 的双 `\bar { f }` 正确；(iv) `$R(x)\ge-r_0^{-2}$`——裁片 `Rbound2.png`（8×）显示上标明确为 `-2`（负号与 2 同行），文本层作 `R(x) ≥ −r0−2`，MD 的 `^ { - 2 }` 正确。四处共同成因仍是 150dpi 下小字形（分数 1、≤/≥、短横、上标负号）不可靠，判据一律回到裁片与 bbox 文本层。（b）`$Vol(\partial\Omega)^n\ge(1-\delta)c_nVol(\Omega)^{n-1}$` 的 $\partial\Omega$ 边界算子与 n / n−1 两个指数、`(4\pi t)^{-\frac n2}`、`[H 7,8]` 的 §、`$O(|pq|^2+|t|)$` 均逐项核对一致。（c）排版级伪影登记不改：`\mathrm { e x p }` 与 `\bigtriangleup` 的字体/字形变体（同 p.7/p.9/p.11/p.18 族）。（d）印刷原样 quirk 保留：`9.6 Remark`（Remark 后无句点）、`(Here $A=g^{ij}A_{ij}$.)` 括点内句点位置。（e）页界已核实：印刷 p.23 止于 10.1 Theorem 与页码 23；`Thus, under the Ricci flow, the almost singular regions …` 印于 p.24。（f）印刷页码 23 未并入 Markdown。

## p.024（PDF p.24 / 印刷 p.24）
- PNG：/tmp/perelmanE_audit_p024.png（pngmono 150dpi）；仲裁裁片 /tmp/perelmanE_p024_integralV2.png（该页 600dpi 重渲 + PIL 裁切并 4× 放大，PIL 仅用于裁图）
- 核对：`Thus, under the Ricci flow, the almost singular regions …` 段（`can not instantly significantly influence`、`via renormalization group flow`、`on higher energy scale`、`a slightly lower energy scale.`）；Proof 全段（`It is an argument by contradiction`、`$(x̄,t̄)$ not far from $(x_0,0)$`、`starting as δ-function at $(x̄,t̄)$`、`the corresponding nonpositive function v as in 9.3`、`compared to t̄^{-1}`、`$\int v$ at time t`、`intervals t̄ − t of the order of $|Rm|^{-1}(x̄,t̄)$`、**被测公式** `By monotonicity we conclude that ∫v is bounded away from zero at t = 0.`、`using (9.1) and an appropriate cut-off function`、`the integral of v over $B(x_0,r)$`、`close to 1`、`compared to $r_0$`、`isoperimetric constant in $B(x_0,r_0)$`）；`Now let us go into details …` 段（`By scaling assume that $r_0 = 1$`、`α is small, say $\alpha<\frac{1}{100n}$`、`denote by $M_\alpha$ the set of pairs $(x,t)$, such that $|Rm|(x,t)\ge\alpha t^{-1}$.`（**被测标点**））；Claim 1 全段（`$0\le t\le\epsilon^2$`、`$A\epsilon<\frac{1}{100n}$`、`$|Rm|(x,t)>\alpha t^{-1}+\epsilon^{-2}$`、`$d(x,t)<\epsilon$`、`$(\bar x,\bar t)\in M_\alpha$`、`$0<\bar t\le\epsilon^2$`、`$d(\bar x,\bar t)<(2A+1)\epsilon$`）；式 (10.1)（$|Rm|(x,t)\le4|Rm|(\bar x,\bar t),$）；`whenever` 与式 (10.2)（$(x,t)\in M_\alpha,\ 0<t\le\bar t,\ d(x,t)\le d(\bar x,\bar t)+A|Rm|^{-\frac12}(\bar x,\bar t)$）；`Proof of Claim 1.` 全段（`as a limit of a (finite) sequence $(x_k,t_k)$`、`$0<t_1\le\epsilon^2$`、`$|Rm|(x_1,t_1)\ge\alpha t^{-1}+\epsilon^{-2}$`、`satisfying (10.2), but not (10.1)`、`$4^{k-1}|Rm|(x_1,t_1)\ge4^{k-1}\epsilon^{-2}$`、止于 `and therefore,$d ( x _ { k } , t _ { k } ) \leq ( 2 A +$`）；印刷页码 24；对照 Markdown 第 559、561、563、565、567–569、571、573–575、577 行。
- 结果：FAIL（一处数学内容错误 + 一处标点缺失，已按原图修复，以原图为准）
- 差异与修复（逐处 Edit）：
  1. 第 561 行 `By monotonicity we conclude that v is bounded away from zero at$t = 0$.` —— **积分号 ∫ 丢失**：印刷为 `By monotonicity we conclude that $\int v$ is bounded away from zero at $t=0$.`，Markdown 写成裸的 `v`。这把「$\int v$ 远离零」错成「$v$ 远离零」，改变数学内容。600dpi 裁片 `/tmp/perelmanE_p024_integralV2.png`（4×，覆盖 `|Rm|^{-1}(x̄,t̄). By monotonicity we conclude that ∫ v is bounded away from`）逐字可见该长积分号；同段稍前的 `then one can show that$\scriptstyle \int v$at time t` 在 Markdown 中 ∫ 本已保留，仅此一处丢失。已 Edit 为 `By monotonicity we conclude that$\int v$ is bounded away from zero`。
  2. 第 563 行 `$M _ { \alpha }$the set of pairs$( x , t )$, such that$| R m | ( x , t ) \geq \alpha t ^ { - 1 }$` **缺句点**，印刷为 `|Rm|(x, t) ≥ αt−1 .`。已补句点。
  - 两处锚串 `grep -c -F` 均实测唯一；修复后字符级 difflib 显示第 561 行仅把 ` v` 包成 `$\int v$`、第 563 行仅新增一个 `.`，无夹带。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对两处锚串实测命中数均为 1（含原样缺失 ∫ 的 `conclude that v is bounded away from zero`），故**两处均为 MinerU 导出缺陷，非任何 peer 引入的回归**。
- 备注：（a）说明：`pdftotext -f 24 -l 24 -layout` 在本处把该 ∫ 吞掉（输出作 `By monotonicity we conclude that v is bounded away from zero at t = 0.`），与 p.22 同类现象——仅看文本层会误判为「印刷无积分号」；按 ask 规定公式以裁片为准，故以 600dpi 裁片为裁决依据。（b）本页两处 $\frac{1}{100n}$、式 (10.2) 的 $-\frac12$ 指数、$4^{k-1}$、$(2A+1)\epsilon$ 等小分数与小指数，经原页目检 + 文本层逐 token 核对一致（分子 token 均实测为单个窄字形 `1`），未出现 p.19/p.20/p.23 那类 1↔n 误判。（c）打印中 `ᾱ`、`t̄` 一律作横线标注；Markdown 的 `\bar { x }`、`\bar { t }` 与之一致。（d）印刷原样 quirk 保留：`Or , using the interpretation`（逗号前空格）、`Claim 1.`（编号与正文间无空格）。（e）页界已核实：印刷 p.24 止于 `and therefore, $d(x_k,t_k)\le(2A+$`，续行 `1)ε. Since the solution is smooth, …` 印于 p.25（对应 Markdown 第 579 行），归 p.25 条目，不计入本页。（f）印刷页码 24 未并入 Markdown。

## p.025（PDF p.25 / 印刷 p.25）
- PNG：/tmp/perelmanE_audit_p025.png（pngmono 150dpi；常驻副本 `2006年 - Perelman/audit-redo/p025.png`）
- 核对：p.24 续文 `1)ε. Since the solution is smooth, the sequence is finite, and its last element fits.`；Claim 2 陈述（`For (x̄,t̄), constructed above, (10.1) holds whenever`）；式 (10.3)（$\bar t-\frac12\alpha Q^{-1}\le t\le\bar t,\ dist_{\bar t}(x,\bar x)\le\frac1{10}AQ^{-\frac12},$）；`where $Q=|Rm|(\bar x,\bar t)$.`（**被测标点**）；Proof of Claim 2 全段（`it must satisfy (10.1) or (10.2)`、$Q\ge\alpha\bar t^{-1}$、$\bar t-\frac12\alpha Q^{-1}\ge\frac12\bar t$、`belongs to $M_\alpha$`、`by the triangle inequality`、`using lemma 8.3(b)`、`as t decreases from t̄ to t̄ − ½αQ⁻¹`、$\frac1{10}AQ^{-\frac12}$、$AQ^{-\frac12}$ centered at $x_0$.（**被测标点**））；`Continuing the proof of the theorem …` 段（`$\epsilon\to0,\delta\to0$`、`by reducing ε, we'll assume that`）；式 (10.4)（$|Rm|(x,t)\le\alpha t^{-1}+2\epsilon^{-2}$ whenever $0\le t\le\epsilon^2$ and $d(x,t)\le\epsilon$）；`Take $A=\frac{1}{100n\epsilon}\to\infty$, construct (x̄,t̄) …` 段（$u=(4\pi(\bar t-t))^{-\frac n2}e^{-f}$、`starting from δ-functions at (x̄,t̄)`、`corresponding nonpositive functions v.`）；Claim 3 全段（`$\tilde t\in[\bar t-\frac12\alpha Q^{-1},\bar t]$`、`the integral $\int_B v$`、`where B is the ball at time $\tilde t$ of radius $\sqrt{\bar t-\tilde t}$ centered at x̄.`）；Proof of Claim 3 (sketch) 全段（`invariant under scaling`、`limit of scalings of g_ij(t) at points (x̄,t̄) with factors Q`、`the injectivity radii … are bounded away from zero`、`$|Rm|(x̄,t̄)=1$ and $|Rm|(x,t)\le4$ when $\bar t-\frac12\alpha\le t\le\bar t$`、`the limit manifold`、`$\int_B v$ can not be zero for $\tilde t=\bar t-\frac12\alpha$`、`the evolution equation (9.1)`、`a gradient shrinking soliton`、`incompatible with $|Rm|(x̄,t̄)=1$.（**被测标点**））；`If the injectivity radii of the scaled metrics tend to zero … a flat man-`；印刷页码 25；对照 Markdown 第 579、581、583–585、587、589、591、593–595、597、599、601、603 行。
- 结果：PASS±（三处印刷句点缺失，已按原图修复）
- 差异与修复（逐处 Edit；证据为 150dpi 目检 + `pdftotext -f 25 -l 25 -layout` 文本层双通道）：
  1. 第 587 行 `where$Q = | R m | ( \bar { x } , \bar { t } )$` **缺句点**，印刷为 `where Q = |Rm|(x̄, t̄).`。已补句点。
  2. 第 589 行 Proof of Claim 2 末 `…centered at$x _ { 0 }$` **缺句点**，印刷为 `centered at x0 .`。已补句点。
  3. 第 601 行 Proof of Claim 3 末 `incompatible with$| R m | ( \bar { x } , \bar { t } ) = 1$` **缺句点**，印刷为 `with |Rm|(x̄, t̄) = 1.`。已补句点。
  - 三处锚串 `grep -c -F` 均实测唯一；修复后字符级 difflib 显示第 587、589、601 行各仅新增一个 `.`，无夹带。
- 溯源：`git show cpf-redo/Perelman_2002_entropy_ricci^:…md` 对三处锚串实测命中数均为 1（原样缺句点），故**三处均为 MinerU 导出缺陷，非任何 peer 引入的回归**。
- 备注：（a）登记不改的排版级差异：(i) 第 589、597 行各有一个**全角逗号 `，`（U+FF0C）**代替印刷的半角逗号——全篇仅此 3 处（第三处在 Markdown 第 673 行，属 p.30），属 MinerU 字符类伪影，不误导数学内容；(ii) 第 589 行 `as t decreases from t<sup>¯</sup> to$\bar { t } - \frac { 1 } { 2 } \alpha Q ^ { - 1 }$` 中第一个 $\bar t$ 被写成 HTML `<sup>¯</sup>` 而同句第二个是 `\bar { t }`（与 p.12/p.13/p.14 的 `<sup>` 同族），渲染仍为 t̄；(iii) 印刷 `Claim 3.As`（编号后无空格）在 Markdown 作 `Claim 3. As`（多一空格）。（b）公式逐项核对一致：(10.3) 的 $\frac12$、$\frac1{10}$、$Q^{-\frac12}$，(10.4) 的 `2ε^{-2}`，`$A=\frac{1}{100n\epsilon}$`，$u=(4\pi(\bar t-t))^{-\frac n2}e^{-f}$，Claim 3 的 $\int_B v$、$\sqrt{\bar t-\tilde t}$、$|\!Rm\!|\le4$ 与 $\bar t-\frac12\alpha\le t\le\bar t$ 均与印刷相符（该页小分数分子经 bbox 逐 token 实测为单个 `1`，未出现 1↔n 误判）。（c）印刷原样 quirk 保留：`we'll` 的弯引号、`violating the statement; by reducing ε` 的分号。（d）页界已核实：印刷 p.25 止于 `a flat man-`（断词），续行印于 p.26（Markdown 第 603 行起）；印刷页码 25 未并入 Markdown。
