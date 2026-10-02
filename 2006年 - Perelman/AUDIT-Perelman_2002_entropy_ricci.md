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
