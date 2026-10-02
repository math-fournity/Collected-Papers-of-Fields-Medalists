# 逐页审计：Douglas_1931_plateau

- 篇目：Jesse Douglas, “Solution of the Problem of Plateau”
- PDF：`Douglas_1931_plateau.pdf`（59 页；印刷页 263–321）
- 审计模式：born-digital；完整 PDF 文本层逐页对账为主，题录页与密集数学页整页 PNG 抽验；抽取丢失、压平或有疑点的字形回到源页 PNG/300dpi 裁片。
- 全篇结果：59/59 页逐页审计完成；初始判级 PASS 22、PASS± 9、FAIL 28。28 个 FAIL 修复已提交；原始逐页判级保留，不冒充修复后的重新审计。
- 覆盖声明：PDF p.1–p.59 均有单页 150dpi PNG 并由审计者逐页目检；需要判定细字形、编号、系数或上下标时，以逐页条目所链接的 300dpi 裁片为准。
- 源 PDF 证据：`pdfinfo` 为 59 页、480 × 720 pt，Producer `iTextSharp 4.1.6 by 1T3XT`；`pdffonts` 有嵌入的 Times New Roman TrueType 字体；`pdftotext -layout -enc UTF-8` 共 144,382 bytes、U+FFFD 计数 0。
- MinerU：3.4.4；`structured_content.json` 登记 59 个 `page_idx`（0–58）；元数据未提供 `doc_id`（UNKNOWN）。
- MinerU Markdown：`Douglas_1931_plateau_mineru/Douglas_1931_plateau__Douglas_1931_plateau.md`；审计前 SHA-256 `990ae67f6fe21ece944466067ad2da5811059e6362568946751da62359a9e9a3`。
- 基线：`037602429d3b009f6fc468c732073eb3ddf9875f`（期望前缀 `03760242`）；候选尚未由 Master 集成。
- 审计身份：actor=`Peer-P23`；model=`gpt-6-luna`；reasoning effort=`max`。
- 状态：`PAGE_AUDIT_COMPLETE / MARKDOWN_REPAIRS_COMMITTED / FULL_MARKDOWN_REREAD_VERIFIED`。p.43 初始 PASS 已由 300dpi 复核更正为 FAIL；复核既有裁片时另发现 p.11 (5.1) 与 p.24 (11.8′) 的积分域小写误录，具体判断见相应页级签认与 `audit(correction)` 提交。根级 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、README 和 MEMORY 由 Master 投影，本候选不修改。

## 逐页记录

### p.001/59（PDF p.1 / 印刷 p.263）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:12 -0400`。
- PNG：`audit/Douglas_1931_plateau_p001.png`（pngmono 150dpi；整页目检）。
- 核对：题名与星号脚注、作者、引言前三段、页末截断位置、四条页下注与印刷页码。
- 结果：PASS。PDF p.1 视觉页和文本层与 Markdown 对应内容一致；页末 “Here the given” 在印刷页自然续至下一页，未见漏录或误录。

### p.002/59（PDF p.2 / 印刷 p.264）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:14 -0400`。
- PNG：`audit/Douglas_1931_plateau_p002.png`（pngmono 150dpi；整页目检，密集数学页抽验）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p002_eq1-1.png`（公式 (1.1) 裁片）。
- 核对：方程 (1.1)、方程前后正文、文内脚注标记与四条页下注、页末断词及印刷页码。
- 结果：PASS。PDF p.2 整页与文本层和 Markdown 对应内容一致。`pdftotext` 将 (1.1) 的希腊字母/微分式抽取成乱码；300dpi 源页裁片确认印刷为 `d²θ/dw² + p dθ/dw + qθ = 0`，Markdown 的方程与印刷一致。

### p.003/59（PDF p.3 / 印刷 p.265）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:18 -0400`。
- PNG：`audit/Douglas_1931_plateau_p003.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p003_conformal.png`、`audit/300dpi/Douglas_1931_plateau_p003_radomark.png`、`audit/300dpi/Douglas_1931_plateau_p003_eq1-2.png`。
- 核对：对 Radó 后续工作的说明、共形映射段落、方程 (1.2)、页下注与印刷页码。
- 结果：PASS。PDF 文本层与 Markdown 的正文、断页续接和两条页下注一致。`pdftotext` 在本页将 `conformal` 抽成 `conformai`、把 `Radó†` 的 † 抽成 `f`；300dpi 裁片分别确认印刷为 `conformal`、`Radó†`。方程 (1.2) 的裁片确认上标 2、负号及各项次序均与 Markdown 相符。

### p.004/59（PDF p.4 / 印刷 p.266）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:23 -0400`。
- PNG：`audit/Douglas_1931_plateau_p004.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p004_eq1-3.png`、`audit/300dpi/Douglas_1931_plateau_p004_text-and-coordinates.png`、`audit/300dpi/Douglas_1931_plateau_p004_footnotes.png`、`audit/300dpi/Douglas_1931_plateau_p004_last-footnote.png`。
- 核对：三种方法概述、面积泛函 (1.3)、`x_i=g_i(θ)` 与指标范围、Fréchet 的 L-set 说明、七条页下注、页末“functional (§5)”及印刷页码。
- 结果：PASS。PDF 文本层和 Markdown 的本页正文/页下注对应；印刷原页裁片确认 (1.3) 为 `∬(1+p²+q²)^{1/2} dx dy = minimum`，表示式为 `x_i=g_i(θ)`、`i=1,2,…,n`，页下注原文包括 `Hilbert`、`Fréchet`、`Ueber`、`Matematica` 和 `fonctionnel`，均与 Markdown 一致。文本层中的 `ff(l...`、`Hubert`、`Frcchet`、`äs`、`lieber`、`Matemática` 与 `fonctionne'-` 属抽取字形误映；Markdown 未复制这些误读。(1.4) 位于下一印刷页，不计入本页。

### p.005/59（PDF p.5 / 印刷 p.267）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:27 -0400`。
- PNG：`audit/Douglas_1931_plateau_p005.png`（pngmono 150dpi；整页目检，密集数学页抽验）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p005_eq1-4.png`、`audit/300dpi/Douglas_1931_plateau_p005_eq1-4_label.png`、`audit/300dpi/Douglas_1931_plateau_p005_eq1-4-1_to_4-3.png`、`audit/300dpi/Douglas_1931_plateau_p005_eq1-4-1_to_4-3_labels.png`、`audit/300dpi/Douglas_1931_plateau_p005_finite-plus-infinity.png`、`audit/300dpi/Douglas_1931_plateau_p005_frechet-marker.png`。
- 核对：泛函 (1.4)、表示式 (1.4₁)/(1.4₂)、极小条件 (1.4₃)、相邻引用编号、`+∞` 与脚注标记。
- 结果：FAIL。印刷 p.267 将两条公式编号排为带下标的 `(1.4₂)`、`(1.4₃)`；Markdown 对应位置写为 `\tag{1.42}` 和 `\tag{1.43}`，丢失 `.4` 后的编号层级/下标结构。300dpi 编号裁片与整页 PNG 均可见印刷下标，PDF 页的相邻正文也分别引用 `(1.4₃)`、`(1.4₁)`。修复建议：逐处改为 `\tag{1.4_2}`、`\tag{1.4_3}`；待 59 页审计全部完成后再用 Edit 修复。其余本页公式、正文、`+∞` 与页下注和印刷一致。

### p.006/59（PDF p.6 / 印刷 p.268）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:30 -0400`。
- PNG：`audit/Douglas_1931_plateau_p006.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p006_parameter-theta.png`、`audit/300dpi/Douglas_1931_plateau_p006_Ag-plus-infinity.png`、`audit/300dpi/Douglas_1931_plateau_p006_Ag-ge-Sg-u2v2.png`、`audit/300dpi/Douglas_1931_plateau_p006_conformal.png`、`audit/300dpi/Douglas_1931_plateau_p006_Osgood-marker.png`。
- 核对：弧长参数 `θ=2πs/L`、不可求长边界的说明、面积泛函与面积关系、平面单位圆条件、共形映射及三条页下注。
- 结果：FAIL。印刷 p.268 原文是 “where generally `A(g)=+∞`”；Markdown 写成 `A(g) \equiv +\infty`，把单等号替换为恒等号。300dpi 裁片确认印刷为单等号。修复建议：将本处 `\equiv` 改成 `=`。本页其余核对项一致；裁片另确认 `θ=2πs/L`、`A(g)≥S(g)`、`u²+v²<1`，以及印刷的 `conformal` 和 `Osgood‡`；文本层分别把这些字形抽成 `8`、`^`、`conformai`、`OsgoodJ`，Markdown 对应内容正确。

### p.007/59（PDF p.7 / 印刷 p.269）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:33 -0400`。
- PNG：`audit/Douglas_1931_plateau_p007.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p007_eq2-1.png`、`audit/300dpi/Douglas_1931_plateau_p007_eq2-2.png`、`audit/300dpi/Douglas_1931_plateau_p007_boundary-values.png`、`audit/300dpi/Douglas_1931_plateau_p007_critical-zeros.png`、`audit/300dpi/Douglas_1931_plateau_p007_footnote-mark.png`、`audit/300dpi/Douglas_1931_plateau_p007_there-word.png`。
- 核对：Weierstrass 表示式 (2.1)/(2.2)、边界连续附着条件、导数同时为零的例外点、唯一性说明及 Wiener 举例的整条页下注。
- 结果：PASS。印刷 p.269 的各式、页正文、脚注标记与脚注内容均与 Markdown 一致。源页印有短语 `boundary values on. C`（句点保留，未据语法推测更改）；结尾印刷为 `there will`，Markdown 正确，PDF 文本层误抽成 `theie`。文本层还将 `\Re`、θ、导数撇号和脚注 † 映错，300dpi 裁片确认 Markdown 的 `x_i=\Re F_i(w)`、`x_i=g_i(θ)`、`F'_i(w)=0` 与 `unique.†` 均忠实于印刷。

### p.008/59（PDF p.8 / 印刷 p.270）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:37 -0400`。
- PNG：`audit/Douglas_1931_plateau_p008.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p008_dimension-n.png`、`audit/300dpi/Douglas_1931_plateau_p008_figure-caption.png`、`audit/300dpi/Douglas_1931_plateau_p008_monotonie-P.png`、`audit/300dpi/Douglas_1931_plateau_p008_footnote.png`。
- 核对：`n=2` 与 `n>2` 的命题、I 部分假设、第 3 节标题、Fig. 1 环面图/图注、proper correspondence 的定义、Fraktur 集合记号及页下注例子。
- 结果：PASS±。页面正文、Fig. 1 的方形环面及 A/B/E/D/F/G 曲线、图注 `R=ΓC`、脚注中的四个坐标函数与边界余弦/正弦式均和 PDF 印刷对应。源页裁片确认文本层的 `w=2`、`«>2`、`R=TC`、`monotonie`、`unique.!` 分别是 `n=2`、`n>2`、`R=ΓC`、`monotonic`、`unique.†` 的抽取误映；Markdown 这些内容正确。唯一可见差异是印刷用 Fraktur `𝔓` 指该曲线集合，而 Markdown 记为普通 `P`；属样式/字形简化，当前不改变本页陈述含义，记 PASS±。

### p.009/59（PDF p.9 / 印刷 p.271）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:40 -0400`。
- PNG：`audit/Douglas_1931_plateau_p009.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p009_improper-classes.png`、`audit/300dpi/Douglas_1931_plateau_p009_degenerate-tail.png`、`audit/300dpi/Douglas_1931_plateau_p009_S-main.png`、`audit/300dpi/Douglas_1931_plateau_p009_S1.png`、`audit/300dpi/Douglas_1931_plateau_p009_S2.png`、`audit/300dpi/Douglas_1931_plateau_p009_gi-constants.png`。
- 核对：proper 曲线类的闭性、improper correspondence 定义、improper 表示的两个子类、退化表示和对应坐标函数。
- 结果：FAIL。印刷原页把全部 improper representations 记作 Fraktur `𝔖`，两个子类为 `𝔖₁`、`𝔖₂`，Markdown 对应处误作 `\mathfrak{F}`、`\mathfrak{J}_{1}`、`\Im_{2}`。印刷末段是“the functions `g_i` reduce to constants”；Markdown 对应处写为 `$g$; reduce to constants`，丢失下标 `i` 并引入分号。300dpi 源页裁片核实以上符号及下标。修复建议：四处分别改为 `\mathfrak{S}`、`\mathfrak{S}_{1}`、`\mathfrak{S}_{2}` 和 `$g_i$`；全篇审计结束后用 Edit 逐处处理。其余图形叙述、正文和印刷段落顺序一致；文本层的 `monotonie` 是本页印刷 `monotonic` 的抽取误映，Markdown 保持正确。

### p.010/59（PDF p.10 / 印刷 p.272）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:42 -0400`。
- PNG：`audit/Douglas_1931_plateau_p010.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p010_representation-classes.png`。
- 核对：三点固定对应关系、所有表示类的并集等式、M/M′ 的闭性性质、调和曲面的定义及 Poisson 积分边界极限。
- 结果：FAIL。印刷 p.272 的 (1)–(3) 三条集合关系均使用 Fraktur `𝔖` 表示 p.9 定义的 improper representations；Markdown 三处把它写成 `\mathfrak{I}`（分别出现在 `\mathfrak{R}=\mathfrak{P}+\mathfrak{I}+\mathfrak{D}`、`\mathfrak{M}=\mathfrak{P}+\mathfrak{I}`、`\mathfrak{M}'=\mathfrak{P}'+\mathfrak{I}'`）。300dpi 源页裁片确认该字形为 `𝔖`，与 p.9 定义一致。修复建议：三个等式中的 `\mathfrak{I}` 各自改为 `\mathfrak{S}`；待全篇审计完成后逐处用 Edit 修复。其余本页正文顺序和说明与 PDF 对应。

### p.011/59（PDF p.11 / 印刷 p.273）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:45 -0400`。
- PNG：`audit/Douglas_1931_plateau_p011.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p011_class-MPS.png`、`audit/300dpi/Douglas_1931_plateau_p011_equation5-1.png`、`audit/300dpi/Douglas_1931_plateau_p011_correspondence.png`。
- 核对：improper correspondence 下调和面的边界、Cantor 集例子、表示类 M 的定义及公式 (5.1)。
- 结果：FAIL。印刷在本页把表示类写为 `𝔐=𝔓+𝔖`；Markdown 对应位置为 `M=P+J`， improper 类字母误成 J，且 Fraktur M/P 字形简化。印刷公式 (5.1) 的系数为 `1/(16π)`；Markdown 写成 `\frac{1}{1 6 \pi}`，在 1 与 6 之间多出空格。复核该式的 300dpi 原页裁片还确认两个积分域均为单位圆 `C`，Markdown 写成小写 `c`。修复建议：该集合等式改为 `\mathfrak{M}=\mathfrak{P}+\mathfrak{S}`，系数改为 `16\pi`，并将 `\int_c\int_c` 改成 `\int_C\int_C`；待全篇审计结束后再用 Edit 逐处修复。参数式 `t=t(θ)` 和 “monotonic function” 的印刷文字与 Markdown 一致；文本层误映的 θ 和单词尾字母由裁片确认。

### p.012/59（PDF p.12 / 印刷 p.274）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:47 -0400`。
- PNG：`audit/Douglas_1931_plateau_p012.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p012_figure-caption.png`、`audit/300dpi/Douglas_1931_plateau_p012_diagonal-theta-phi.png`、`audit/300dpi/Douglas_1931_plateau_p012_limit-markers.png`、`audit/300dpi/Douglas_1931_plateau_p012_footnotes.png`。
- 核对：积分域环面与 Fig. 2、对角线 `θ=φ`、删去的邻域 `τ₁`、不连续点的极限分支、页下注标记及页末界。
- 结果：FAIL。印刷 p.274 在“parallel but not meridian”处写 `distinct limits†`，在“intersection ... four distinct limits”处写 `distinct limits‡`；Markdown 两处都写为 `^{\ddagger}`。300dpi 裁片及底部两条脚注明确区分 † 与 ‡。修复建议：只把第一处的 `^{\ddagger}` 改为 `^{\dagger}`，保留第二处 `^{\ddagger}`。图像、图注 `Fig. 2. Torus of integration T=CC`、对角线公式和正文其余内容与印刷一致。

### p.013/59（PDF p.13 / 印刷 p.275）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:50 -0400`。
- PNG：`audit/Douglas_1931_plateau_p013.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p013_bound-top.png`、`audit/300dpi/Douglas_1931_plateau_p013_inequality-5-2.png`、`audit/300dpi/Douglas_1931_plateau_p013_footnotes-bottom.png`。
- 核对：上界 `d²/sin²(δ/2)`、递减区域序列及补集积分、无穷条带分割、式 (5.2) 和页底脚注。
- 结果：FAIL。印刷页底只有两条完整脚注（† 对 `Δ_r^*(g)` 的严格正性说明；‡ 对 `|θ−φ|` 的小弧定义）。Markdown 在两条完整脚注前额外插入四个独立碎片 `<small>`：`g`、`Δ_r^*(g)`、`By |θ−φ|` 和 `φ`；源页裁片无对应独立文字，这些碎片与完整脚注内容重叠。修复建议：全篇审计完成后逐处移除这四个多余碎片，保留两条完整脚注。公式 (5.2)、正文和两条脚注的完整内容均与印刷一致。

### p.014/59（PDF p.14 / 印刷 p.276）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:52 -0400`。
- PNG：`audit/Douglas_1931_plateau_p014.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p014_equation5-3.png`、`audit/300dpi/Douglas_1931_plateau_p014_bound-and-inequality54.png`、`audit/300dpi/Douglas_1931_plateau_p014_footnote-bottom.png`。
- 核对：泛函 `Δ_r(g)` 的定义 (5.3)、被积函数上界、正性论证、区间条件 (5.4) 及页底脚注。
- 结果：FAIL。印刷 (5.3) 的系数为 `1/(16π)`；Markdown 写为 `\frac{1}{1 6 \pi}`，将 `16` 拆开。页底印刷脚注只有完整的 † 注释，句末为 `p` 并在此页换页；Markdown 在完整脚注之前另有孤立 `<small>p</small>`，该位置在源页无独立字样。修复建议：分母逐处还原为 `16\pi`，移除孤立 `p` 块并保留完整脚注。上界与 (5.4) 裁片和 Markdown 一致。

### p.015/59（PDF p.15 / 印刷 p.277）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:54 -0400`。
- PNG：`audit/Douglas_1931_plateau_p015.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p015_sum-A.png`、`audit/300dpi/Douglas_1931_plateau_p015_transform-6-1.png`、`audit/300dpi/Douglas_1931_plateau_p015_substitute-6-2.png`、`audit/300dpi/Douglas_1931_plateau_p015_integral-6-3.png`、`audit/300dpi/Douglas_1931_plateau_p015_transform-6-4-footnote.png`。
- 核对：级数式 (5.5)、Möbius 变换 (6.1)、变量替换 (6.2)、核积分变换、实分式变换 (6.4) 与页下注。
- 结果：PASS。PDF 文本层与 Markdown 的本页正文和公式相符。300dpi 裁片确认 (6.1)/(6.4) 上的横线、(6.2) 末尾印刷的中心点和 † 脚注标记，以及 (6.3) 的 `1/(4π)`、无穷积分端点和 `(x−y)²` 分母；Markdown 对应正确。文本层把 θ、φ 的字形压错，源页裁片确认 Markdown 中的变量和横线。

### p.016/59（PDF p.16 / 印刷 p.278）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:56 -0400`。
- PNG：`audit/Douglas_1931_plateau_p016.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p016_formula6-5.png`、`audit/300dpi/Douglas_1931_plateau_p016_jacobian-identities.png`、`audit/300dpi/Douglas_1931_plateau_p016_invariance-equality.png`。
- 核对：变换后泛函 (6.5)、Jacobian 三式、`A(\bar g)=A(g)` 的不变性结论、等价表示与 `\mathfrak M/\mathfrak M'` 下界关系。
- 结果：PASS±。三组核心公式的横线、上下限、平方项及被积测度均与 PDF 印刷一致；源页裁片确认变换后等式是 `A(\bar g)=A(g)`，Markdown 具备对应横线和公式。正文中集合符号 `\mathfrak M`、`\mathfrak M'` 在 Markdown 以普通 M/M′ 排印，属于 Fraktur 字形简化；本页关系、对象和上下界仍可区分，记为轻微字形差异。

### p.017/59（PDF p.17 / 印刷 p.279）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 16:59 -0400`。
- PNG：`audit/Douglas_1931_plateau_p017.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p017_A-L-set.png`、`audit/300dpi/Douglas_1931_plateau_p017_sequence-definitions.png`。
- 核对：L-set 的收敛公理、Bolzano–Weierstrass 紧致性、闭集/极值集定义、连续实值函数定义及下半连续条件 (7.1)。
- 结果：PASS±。全文定义与 Markdown 对应，式 (7.1) 的严格不等号及 ε 界限也与印刷相同。300dpi 首段裁片确认文本层抽成 `set 21`、`Z,-set` 的字样分别是集合名 A 与 `L-set`；Markdown 内容正确，但印刷集合名的装饰字形在 Markdown 简化为普通 A，记为轻微字形差异。

### p.018/59（PDF p.18 / 印刷 p.280）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 17:27 -0400`。
- PNG：`audit/Douglas_1931_plateau_p018.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p018_alternative-7-2.png`、`audit/300dpi/Douglas_1931_plateau_p018_tag-7-2.png`、`audit/300dpi/Douglas_1931_plateau_p018_liminf.png`、`audit/300dpi/Douglas_1931_plateau_p018_representation-set-symbols.png`、`audit/300dpi/Douglas_1931_plateau_p018_graphs-set-symbol.png`。
- 核对：下半连续性的序列表述 (7.2)、等价 liminf 表述、全体拓扑表示的集合符号、L-set 紧致性陈述及 Fréchet 定理引用。
- 结果：FAIL。(7.2) 原印刷为 `(7.2) if ...; and ...; then U(a)≤L`，Markdown 把 `if` 错放进 `\tag{7.2) if}`，并省去数组中 `and`、`then` 两个词。300dpi 裁片确认源页含这三个句内词，且不等号确为 `≤`；后面的 `U(a)≤liminf` 与 Markdown 相符。另，表示全部 proper/improper/degenerate representations 的两个正文位置，印刷符号为 Fraktur capital R `\mathfrak{R}`，Markdown 用 `\Re`（实部符号）代替，见 `representation-set-symbols.png` 与 `graphs-set-symbol.png`。修复建议：恢复 (7.2) 的 if/and/then 位置及干净标签，并将这两处 `\Re` 分别改成 `\mathfrak{R}`；全篇审计结束后再用 Edit 修复。

### p.019/59（PDF p.19 / 印刷 p.281）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 18:14 -0400`。
- PNG：`audit/Douglas_1931_plateau_p019.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p019_equation9-1.png`、`audit/300dpi/Douglas_1931_plateau_p019_L-set-R-symbol.png`、`audit/300dpi/Douglas_1931_plateau_p019-positive-increment.png`。
- 核对：L-set 曲线长度有界条件、极值集结论、级数部分和 `A_r(g)`、增量正性及式 (9.1)。
- 结果：FAIL。式 (9.1) 的印刷系数为 `1/(16π)`；Markdown 将分母写作 `1 6 π`，多出空格。首页段的“curve of Fraktur R is rectifiable”指表示类 `\mathfrak{R}`，Markdown 用 `\Re`（实部符号）代替；300dpi 符号裁片确认印刷为 Fraktur capital R。修复建议：把该处 `\Re` 改为 `\mathfrak{R}`，将公式分母 `1 6 \pi` 改为 `16 \pi`；全篇审计完成后逐处用 Edit 修复。另核验了“each `Δ_r(g)>0`”的印刷增量符号，Markdown 正确；文本层把 Δ 误读成 A。

### p.020/59（PDF p.20 / 印刷 p.282）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 18:52 -0400`。
- PNG：`audit/Douglas_1931_plateau_p020.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p020_sequence-9-2.png`、`audit/300dpi/Douglas_1931_plateau_p020_epsilon-estimates.png`、`audit/300dpi/Douglas_1931_plateau_p020_comparison-9-5-9-6.png`、`audit/300dpi/Douglas_1931_plateau_p020_infinity-footnotes.png`。
- 核对：定理 9 下的单调函数序列、式 (9.2)–(9.6)、`U(a)=+∞` 情形与页底脚注。
- 结果：FAIL。印刷页在 `U(a_1), U(a_2), …, U(a_m), …` 后的正文续为 “tends to `+∞`.”，其下方才开始唯一的 † 脚注。Markdown 把这句拆成两个多余 `<small>` 脚注片段 `to +∞` 与 `† tends to +∞.`，造成正文缺词并重复/误标脚注；300dpi 页底裁片确认正文与脚注分界。修复建议：删除这两个碎片，并在序列公式后恢复普通正文 `tends to $+\infty$.`；保留完整的 † 注。式 (9.2) 的印刷符号是 `≤`，文本层误抽成 `=`，Markdown 中的 `≤` 正确；(9.3)–(9.6) 的次序和关系符也与原页相符。

### p.021/59（PDF p.21 / 印刷 p.283）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 19:55 -0400`。
- PNG：`audit/Douglas_1931_plateau_p021.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p021_eq9-7-9-8.png`、`audit/300dpi/Douglas_1931_plateau_p021_lower-bound-M.png`、`audit/300dpi/Douglas_1931_plateau_p021_minimizing-sequence.png`、`audit/300dpi/Douglas_1931_plateau_p021_footnotes.png`。
- 核对：无限极限情形的推导 (9.7)/(9.8)、下界 M≥0、最小化序列 (10.1)/(10.2) 与两条页下注。
- 结果：FAIL。印刷页底只有完整的 † 与 ‡ 两条注释；Markdown 在两条完整脚注之前还插入五个独立碎片 `<small>`：`g^{\bullet}`、`≥ A(g^0)`、`+∞)`、`A(g)` 和 `M>0.`，这些内容均已出现在后面的完整脚注中，源页无独立行。另，第二条印刷脚注标记为 double dagger ‡，Markdown 标为 dagger †。300dpi 底部裁片确认脚注的两种标记和两条完整正文。修复建议：逐处移除五个碎片，并将第二条注的标记从 `\dagger` 改为 `\ddagger`；全篇审计结束后用 Edit 修复。下界印刷为 M≥0，公式 (9.7)/(9.8) 的关系符及最小化序列与 Markdown 相符。

### p.022/59（PDF p.22 / 印刷 p.284）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 20:27 -0400`。
- PNG：`audit/Douglas_1931_plateau_p022.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p022_lower-semicontinuity-bound.png`、`audit/300dpi/Douglas_1931_plateau_p022_harmonic-minimality.png`、`audit/300dpi/Douglas_1931_plateau_p022_series-11-1.png`、`audit/300dpi/Douglas_1931_plateau_p022_M-prime-set.png`。
- 核对：从 (10.1) 提取紧子列、由下半连续性推出 `A(g*)≤M`、极小值等号、调和面极小条件及幂级数 (11.1) 和脚注。
- 结果：PASS±。Markdown 与印刷的推导次序和公式一致；300dpi 裁片确认文本层把 `A(g*)≤M` 误抽成等号，Markdown 正确，并核实 (11.1) 的系数 `a_{i0}/2`、求和起点/上限、`w^p` 与 †。印刷在表示类处用 Fraktur `𝔐'`；Markdown 后续一句简化成普通 `M'`，属字形差异，不改变此句所指集合。

### p.023/59（PDF p.23 / 印刷 p.285）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 20:42 -0400`。
- PNG：`audit/Douglas_1931_plateau_p023.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p023_equations11-2-to-11-6.png`、`audit/300dpi/Douglas_1931_plateau_p023_equation11-7.png`。
- 核对：Fourier 系数 (11.2)、幂级数 (11.3)、逐项求导式 (11.4)/(11.4′)、卷积系数 (11.5)、求和指标范围 (11.6) 及双重积分 (11.7)。
- 结果：PASS。PDF p.285 文本层逐页对账与 Markdown 内容一致；多个公式被抽取成符号乱码。300dpi 裁片确认 (11.2) 的两个系数均为正 `1/π`，并确认各式中的导数撇号、复指数负号、`p/q` 权重、`p,q≥1` 及 (11.7) 的 `1/π²` 和双重积分微分次序均与 Markdown 相符。

### p.024/59（PDF p.24 / 印刷 p.286）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 21:06 -0400`。
- PNG：`audit/Douglas_1931_plateau_p024.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p024_formulas11-8-to-11-10.png`、`audit/300dpi/Douglas_1931_plateau_p024_formulas11-11-to-operator.png`、`audit/300dpi/Douglas_1931_plateau_p024_equation11-11-exponent.png`。
- 核对：积分抵消式 (11.8)/(11.8′)、乘积重写式 (11.9)、系数公式 (11.10)、有限求和 (11.11)–(11.11′)、代换 (11.12)、几何级数及微分算子。
- 结果：FAIL。复核该页既有 300dpi 裁片发现 (11.8′) 两个积分的区域在印刷中都是单位圆 `C`，Markdown 写为小写 `c`；裁片确认这一字形。修复建议：仅把 (11.8′) 中两个 `\int_c` 改为 `\int_C`。页内其他公式的正负号、`p/q` 指数、求和指标、`ζ/z` 代换、幂次和 (11.7)–(11.12) 的连接均与 Markdown 相符。文本层将部分积分与复指数抽取为乱码；方程 (11.11) 指数中的可见点是前项乘法点，不是 q 上的重音。

### p.025/59（PDF p.25 / 印刷 p.287）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 21:46 -0400`。
- PNG：`audit/Douglas_1931_plateau_p025.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p025_equation11-13.png`、`audit/300dpi/Douglas_1931_plateau_p025_derivation-first-term.png`、`audit/300dpi/Douglas_1931_plateau_p025_derivation-second-term.png`。
- 核对：公式 (11.13) 的有限和闭式、代换 (11.14)、ζ/z 指数恒等式、第一/第二项化简及本页末的合并式。
- 结果：FAIL。印刷 p.287 在正文 “we get” 与 “The calculation of the first and second terms” 之间完整排有公式 (11.13)：`\sum_{p,q} p\zeta^p\cdot qz^q=(m+1)\zeta z(\zeta^m+z^m)(\zeta-z)^{-2}-2\zeta z(\zeta^{m+1}-z^{m+1})(\zeta-z)^{-3}`。Markdown 只有 `(11.13)` 编号而没有公式本体；这是一整条缺失公式。300dpi 源页裁片记录印刷公式；待全篇审计结束后用 Edit 在编号后补回公式。其余 11.14 及逐项化简与印刷对应。

### p.026/59（PDF p.26 / 印刷 p.288）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 22:19 -0400`。
- PNG：`audit/Douglas_1931_plateau_p026.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p026_bracket-reduction.png`、`audit/300dpi/Douglas_1931_plateau_p026_kernel-series.png`、`audit/300dpi/Douglas_1931_plateau_p026_coefficients-11-15.png`。
- 核对：第一/第二项合并化简、由 (11.13) 得到的核和、积分系数 (11.10) 及实部/虚部系数 (11.15)。
- 结果：PASS。印刷与 Markdown 的负号、`sin²δ`/`sin³δ` 分母、`(m±1)` 下标、指数 `e^{-miσ}` 和 (11.15) 中 θ±φ 的二分角均相符；文本层严重压平符号，300dpi 裁片确认公式内容与 Markdown 一致。

### p.027/59（PDF p.27 / 印刷 p.289）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 22:40 -0400`。
- PNG：`audit/Douglas_1931_plateau_p027.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p027_limit-value.png`、`audit/300dpi/Douglas_1931_plateau_p027_transformations-12-1-12-2.png`、`audit/300dpi/Douglas_1931_plateau_p027_transformed-integrals.png`、`audit/300dpi/Douglas_1931_plateau_p027_footnote.png`。
- 核对：被积函数极限值、变换 (12.1)/(12.2)、导数与逆变换、变换后两条 `A(g)` 积分及 † 脚注。
- 结果：FAIL。印刷 p.289 的两条变换后积分各自系数均为 `1/(16π)`；Markdown 两处均写 `\frac{1}{1 6 \pi}`，拆开了数字 `16`。此外 Markdown 在完整脚注前多出独立 `<small>§17</small>`，原页只有包含 `§17` 的完整 † 注。修复建议：逐处把两个分母改为 `16\pi`，移除独立 `§17` 碎片并保留完整脚注。其余 (12.1)、(12.2)、导数符号和极限式由 300dpi 源页裁片确认与印刷相符。

### p.028/59（PDF p.28 / 印刷 p.290）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 23:06 -0400`。
- PNG：`audit/Douglas_1931_plateau_p028.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p028_integrals-12-3-12-4.png`、`audit/300dpi/Douglas_1931_plateau_p028_restriction-12-6.png`。
- 核对：变换积分 (12.3)/(12.4)、各自的 C/S 系数与分母、条带分解、级数定义及复参数范围 (12.6)。
- 结果：FAIL。印刷中 (12.3) 的 `C_m` 与 `S_m` 两条积分，以及 (12.4) 的 `C_{mr}` 与 `S_{mr}` 两条积分，系数均为 `1/(16π)`；Markdown 四处写为 `\frac{1}{1 6 \pi}`。整页 300dpi 裁片确认四处均为 16π。修复建议：四处分别去掉 `1` 与 `6` 之间的空格。另，(12.6) 印刷式末为句点，Markdown 用 `\cdot`；记作轻微终止标点差异，不改变参数条件本身。

### p.029/59（PDF p.29 / 印刷 p.291）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-01 23:53 -0400`。
- PNG：`audit/Douglas_1931_plateau_p029.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p029_Qm-label.png`、`audit/300dpi/Douglas_1931_plateau_p029_complex-denominators.png`、`audit/300dpi/Douglas_1931_plateau_p029_mod-2pi-equations.png`。
- 核对：复参数圆域记号、两分母的零点条件、方程组 (12.7)、模 `2π` 的解以及解析函数结论。
- 结果：PASS±。300dpi 裁片确认圆域在印刷中写作 `C_m`（PDF 文本层误读为 Q），式 (12.7) 两个条件均带实部参数 `μ`，下一步推出 `θ=φ (mod 2π)`，与 Markdown 的核心内容相符。两个 mod 条件在 Markdown 的 `\tag` 字符串里分别缺少开括号（写作 `mod 2π).`、`mod 2π);`），而印刷将它们排作 `(mod 2π).`、`(mod 2π);`；这是不影响模值含义的标点/排式差异，记 PASS±。

### p.030/59（PDF p.30 / 印刷 p.292）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:11 -0400`。
- PNG：`audit/Douglas_1931_plateau_p030.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p030_denominators-13-1.png`、`audit/300dpi/Douglas_1931_plateau_p030_expansions-13-3-13-4-product.png`。
- 核对：分母非零表达式 (13.1)、σ/δ 代换、倒数正弦平方的 Taylor 展开 (13.3)、分子展开 (13.4) 及其乘积的一阶项。
- 结果：PASS。源页裁片确认 (13.1) 的两组 cos/sin 分母与 (13.3)/(13.4) 的正负号、系数和一阶 λ 项均与 Markdown 相符；文本层将部分 σ、δ 及指数压成乱码，Markdown 公式对应正确。

### p.031/59（PDF p.31 / 印刷 p.293）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:17 -0400`。
- PNG：`audit/Douglas_1931_plateau_p031.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p031_Qm-label.png`、`audit/300dpi/Douglas_1931_plateau_p031_expansion-13-5.png`、`audit/300dpi/Douglas_1931_plateau_p031_expansion-13-5-prime.png`、`audit/300dpi/Douglas_1931_plateau_p031_ranges-13-6-13-7.png`。
- 核对：展开式 (13.5)/(13.5′)、级数收敛半径条件 (13.6)/(13.7)、文本中的参数域 `C_m`。
- 结果：FAIL。印刷第二个展开式编号为 `(13.5′)`；Markdown 把该编号写在数组首项中，并拆成 `(1 3. 5 ^ {\prime})`，与源页的数字序列不一致。300dpi 编号裁片确认印刷写作 `(13.5′)`。修复建议：把该编号逐处还原成 `(13.5')` 或等价清晰的 `\tag{13.5'}`，全篇审计完成后用 Edit 修复。方程主体 (13.5′)、条件 (13.6)/(13.7) 与 Markdown 相符；域名是 `C_m`，文本层的 `Q_m` 为误映，源页裁片确认 Markdown 正确。

### p.032/59（PDF p.32 / 印刷 p.294）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:20 -0400`。
- PNG：`audit/Douglas_1931_plateau_p032.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p032_uniform-bounds-13-8.png`、`audit/300dpi/Douglas_1931_plateau_p032_bounded-factor.png`。
- 核对：条件 (13.8)、函数 `|F|` 的有界性、Cauchy 系数估计、Weierstrass 几何级数比较、被积乘数 `≤d²`。
- 结果：PASS。PDF 文本层中 rho 与 mu 等字形被抽取混淆；300dpi 源页裁片确认 `|λ|=ρ₀<1/m`、`|A_k(θ,φ)|≤B/ρ^k`、`|A_k(θ,φ)λ^k|≤B(ρ₀/ρ)^k` 及 `Σ_i[g_i(θ)-g_i(φ)]²≤d²`，均与 Markdown 对应公式相符。

### p.033/59（PDF p.33 / 印刷 p.295）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:23 -0400`。
- PNG：`audit/Douglas_1931_plateau_p033.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p033_derivatives-13-10.png`、`audit/300dpi/Douglas_1931_plateau_p033_radius-14-1.png`、`audit/300dpi/Douglas_1931_plateau_p033_bound-14-2.png`。
- 核对：导数系数 (13.10)、解析圆域范围 (14.1)、积分界 (14.2) 与导数系数下标/公式编号。
- 结果：FAIL。(13.10) 中 `C'_{mr}(0)` 与 `S'_{mr}(0)` 两个系数，以及 (14.2) 的积分界，各有 Markdown 系数 `1 6 π` 拆分；印刷均为 `16π`。S′ 系数的分子中，Markdown 写 `(n−1)`，源页为 `(m−1)`。此外 Markdown 的 (13.10) 数组中在 S′ 公式前多出孤立 `. 1 0)`；印刷编号 `(13.10)` 只出现一次。300dpi 裁片确认这些差异。修复建议：逐处还原三个 `16π` 系数、把 S′ 分子第二项的 `n` 改为 `m`，并删除数组内重复残片；全篇审计结束后用 Edit 修复。域半径 (14.1) 的关系式相符。

### p.034/59（PDF p.34 / 印刷 p.296）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:26 -0400`。
- PNG：`audit/Douglas_1931_plateau_p034.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p034_formula14-3.png`、`audit/300dpi/Douglas_1931_plateau_p034_extension14-4-14-5.png`、`audit/300dpi/Douglas_1931_plateau_p034_majorant-series.png`。
- 核对：`Q(θ,φ,λ)` 的定义与延拓值 (14.3)/(14.3′)、参数闭域 (14.4)、界 (14.5) 及级数主控项。
- 结果：FAIL。(14.2) 中 `|C_{mr}(λ)|` 的积分系数印刷为 `1/(16π)`，Markdown 写为 `\frac{1}{1 6 \pi}`，把 `16` 拆开；300dpi 裁片确认印刷系数。另，PDF 在 (14.5) 的右侧印出带点的 `\dot{Δ}_{r}(g)`，但紧接着比较的主控级数写作未加点的 `Δ_1(g)+Δ_2(g)+…`；这是源页内部记号不一致，Markdown 按公式保留带点写法并原样记录。修复建议：只还原 (14.2) 系数为 `16\pi`，不要改写源页的 (14.5) 记号；全篇审计结束后用 Edit 修复。

### p.035/59（PDF p.35 / 印刷 p.297）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:41 -0400`。
- PNG：`audit/Douglas_1931_plateau_p035.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p035_derivatives-14-7.png`、`audit/300dpi/Douglas_1931_plateau_p035_relations-15.png`、`audit/300dpi/Douglas_1931_plateau_p035_interval-16-1.png`；p.31 参照：`audit/300dpi/Douglas_1931_plateau_p031_expansion-13-5-prime.png`。
- 核对：(C'_m(0),S'_m(0)) 的积分 (14.7)/(14.7′)、关系 (15) 及实 λ 区间 (16.1)。
- 结果：FAIL。(14.7) 与 (14.7′) 的 Markdown 公式分别把编号切成 `(1 4. 7)` 和 `(1 4. 7′)`；两条积分系数分别写成 `1 6 π`，印刷均为 `16π`。300dpi p.297 裁片确认式号与系数。另有源页内部不一致：印刷 p.293 的 (13.5′) 使用 (sin((m-1)(θ-φ)/2)) 与 (cos(m(θ+φ)/2))，而印刷 p.297 的 (14.7′) 排为 (sin((m+1)(θ-φ)/2)) 与 (cos(m(θ-φ)/2))；两页的 Markdown 分别遵循各自印刷，不将此差异归为转录错误。修复建议：仅修复 p.297 的式号排字和两处 `16π` 空格；不得依 p.293 改写 p.297 的印刷表达式。

### p.036/59（PDF p.36 / 印刷 p.298）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:45 -0400`。
- PNG：`audit/Douglas_1931_plateau_p036.png`（pngmono 150dpi；页级对账图）。
- 核对：式 (16.2)–(16.4)、最小曲面说明及第 17 节开头到末行 “approach to P”。
- 结果：PASS。将 PDF p.36（印刷 p.298）的逐页文字和显示公式与结构化原页文本及 Markdown 对照；λ、C'_m(0)、S'_m(0)、A_m/B_m=0、平方导数和、实部表示及 A(g)=+∞ 均相符，段落边界也与页末一致。抽取文本将若干希腊字形/数学字形近似成拉丁字符，150dpi 页图确认了相应印字；没有发现需局部放大的疑难字形。

### p.037/59（PDF p.37 / 印刷 p.299）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:49 -0400`。
- PNG：`audit/Douglas_1931_plateau_p037.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p037_eq-17-3-17-4.png`。
- 核对：式 (17.1)–(17.4)、Fig. 3、被积式极限说明及页末冒号。
- 结果：FAIL。Markdown 的 (17.3) 系数写作 `1/(1 6 π)`，印刷为 `1/(16π)`；该式积分区域的 Markdown 上标为 `S′`，印刷裁片确认为 `S_ε`。300dpi 裁片同时确认系数、求和项和两个积分式区域：后续 (17.4) 的区域为 `S`。Fig. 3 图形与提取图片 `images/page_36_image_6.jpg` 相符；(17.1)、(17.2)、(17.4) 及后续页末文字未发现转录差异。修复建议：仅将 (17.3) 的系数改为 `16π`，积分区域改为 `S_ε`；全篇审计结束后用 Edit 修复。

### p.038/59（PDF p.38 / 印刷 p.300）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:53 -0400`。
- PNG：`audit/Douglas_1931_plateau_p038.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p038_eval-17-5.png`。
- 核对：式 (17.5)、积分原函数和端点代入、发散结论、§18 开头及式 (18.1)。
- 结果：PASS±。式 (17.5)、一般二重积分端点公式、混合二阶导数、原函数、A(g)=+∞ 及式 (18.1) 均与印刷相符。Markdown 在该页段开头保留孤立页眉碎片 `[January`；原印刷页眉完整为 “JESSE DOUGLAS [January”。另，印刷 p.300 的端点代入式最后一个对数项本身以 `δ−` 后缺项的形式出现，300dpi 裁片确认 Markdown 忠实保留此印刷不完整处；按原文优先原则不补造缺失符号。上述差异不改变正文含义或发散结论。

### p.039/59（PDF p.39 / 印刷 p.301）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:54 -0400`。
- PNG：`audit/Douglas_1931_plateau_p039.png`（pngmono 150dpi；页级对账图）。
- 核对：式 (18.2)–(18.5)、Fatou 极限结论、§18 推导及 Fatou 脚注。
- 结果：PASS±。微分积分式、虚部核、两个分量极限与推论、Fatou 引文和正文均与印刷一致。版面上 (18.4′) 的式号和 (18.5) 右侧的分量范围 `(i=1,…,n)` 在 Markdown 中分别与公式分行，数字和数学内容仍完整、无歧义；无内容修复项。

### p.040/59（PDF p.40 / 印刷 p.302）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:56 -0400`。
- PNG：`audit/Douglas_1931_plateau_p040.png`（pngmono 150dpi；页级对账图）。
- 核对：§18 结束论证、§II/§19 标题、式 (19.1)–(19.4)、页脚完整注释。
- 结果：FAIL。正文推导、节次转换、式 (19.1)–(19.4) 与两条有编号脚注均相符；但 Markdown 在完整脚注段落之外另有独立 `<small>` 残片：`d'A`、`Γ,`、`$x_i=f_i(t)$`、`$x_i=S_{im}(t)$`、`$\Gamma^{(m)}$`、`I,`、`$t=\omega_m(\theta)$`、`C,`、`C`、`§17`、`l=0,` 及再次出现的 `$t=\omega_m(\theta)$`。印刷 p.302 中这些串只属于页面下方的一段完整注释或正文，没有各自独立的小字脚注；完整注释本身已保留。修复建议：全篇审计结束后移除上述独立残片，保留完整注释和正文。

### p.041/59（PDF p.41 / 印刷 p.303）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:58 -0400`。
- PNG：`audit/Douglas_1931_plateau_p041.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p041_eq-19-8.png`。
- 核对：式 (19.5)–(19.10)、Jordan 极限构造、参数变换及连续收敛说明。
- 结果：FAIL。式 (19.8) 印刷为 `x_i=g_i(θ)=f_i(ω(θ))`，Markdown 将 `f_i` 错录成 `f^i`；300dpi 原页裁片确认 `i` 为下标。修复建议：全篇审计结束后只把 (19.8) 的 `f ^ {i}` 改为 `f _ {i}`。另，正文两处 Fraktur `𝔐′` 在 Markdown 中写作普通 `M′`，属不致误导的字形简化，不改变集合记号含义。其余式 (19.5)–(19.7)、(19.9)–(19.10) 与对应文字相符。

### p.042/59（PDF p.42 / 印刷 p.304）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 00:59 -0400`。
- PNG：`audit/Douglas_1931_plateau_p042.png`（pngmono 150dpi；页级对账图）。
- 核对：式 (19.11)–(19.13)、极限换序论证、§20 起段及式 (20.1)。
- 结果：PASS。三个极限/导数公式、统一有界与零测集文字、由 (19.11) 得到的结论、§20 的 improper-kind 论证和距离平方公式 (20.1) 均与 PDF p.42（印刷 p.304）相符；没有发现需放大仲裁的字形或内容差异。

### p.043/59（PDF p.43 / 印刷 p.305）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:01 -0400`。
- PNG：`audit/Douglas_1931_plateau_p043.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p043_transform.png`（复核后补充）。
- 核对：Fig. 4、几何变换定义 (20.2)、线性分式式 (20.3)、函数作用式 (20.4)、边界值关系 (20.5) 及求导式。
- 结果：FAIL。Fig. 4 与 MinerU 图片 `images/page_42_image_1.jpg` 一致，(20.2)–(20.5) 及页末导数公式相符；但 300dpi 原页裁片确认几何变换在 “to be called” 后标作 `𝔊`，同页后文也继续用该符号，Markdown 却先写 `T`（“to be called T”“T has the linear fractional form”），随后又写 `\mathfrak G`。这是同一变换符号前后不一致。修复建议：全篇审计结束后将 p.305 这两处 `T` 按印刷统一改为 `\mathfrak G`。

### p.044/59（PDF p.44 / 印刷 p.306）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:05 -0400`。
- PNG：`audit/Douglas_1931_plateau_p044.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p044_transform.png`。
- 核对：(20.6)–(20.7)、边界函数极限、分段积分极限及 §20 结论。
- 结果：FAIL。除变换名称外，本页极限推导、(20.6)/(20.7) 与结束结论均与印刷相符；p.306 原页 300dpi 裁片确认 “image A by” 后为该 Möbius 变换的逆 `𝔊^{-1}`，Markdown 写作 `T^{-1}`，延续了 p.305 的记号误写。修复建议：全篇审计结束后将 p.306 的 `T^{-1}` 改为 `\mathfrak G^{-1}`，与 p.305 的印刷记号统一。

### p.045/59（PDF p.45 / 印刷 p.307）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:06 -0400`。
- PNG：`audit/Douglas_1931_plateau_p045.png`（pngmono 150dpi；页级对账图）。
- 核对：Part III 标题与导言、§21 开头、式 (21.1)–(21.4)。
- 结果：PASS。Part III/§21 标题与导言、面积积分表示 (21.1)、Fourier 系数式 (21.2)、径向极限定义 (21.3)，以及 `F_i′=∂U_i/∂u−i∂U_i/∂v` 均与 PDF p.45（印刷 p.307）相符；公式次序和页末位置一致。

### p.046/59（PDF p.46 / 印刷 p.308）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:08 -0400`。
- PNG：`audit/Douglas_1931_plateau_p046.png`（pngmono 150dpi；页级对账图）。
- 核对：恒等式 (21.5)、Green 公式、(21.6)–(21.9)、三角正交关系及两条脚注。
- 结果：PASS。(21.5) 的模平方分解、Green 边界积分、Fourier 展开与径向导数 (21.7)/(21.8)、三角正交积分和 Parseval 型结果 (21.9) 的系数/指标均与 PDF p.46（印刷 p.308）相符；Picard 两条脚注也完整对应，未见额外或丢失正文。

### p.047/59（PDF p.47 / 印刷 p.309）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:11 -0400`。
- PNG：`audit/Douglas_1931_plateau_p047.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p047_eq-21-10-21-11.png`、`audit/300dpi/Douglas_1931_plateau_p047_factor-21-11-21-12.png`。
- 核对：式 (21.10)–(21.12)、级数求和公式及逐项积分的有界因子。
- 结果：FAIL。印刷将系数关系标为 (21.10)，紧接着将 `\sum mρ^{2m}\cos m(θ−φ)` 余弦级数标为 (21.11)。Markdown 在 (21.10) 公式前另放孤立文本 `(21.11)`，其后公式仍带 `\tag{21.10}`；真正的余弦级数式没有对应编号。300dpi 裁片确认此编号错位。两条级数等式、逐项积分因子 `−1/(2π²)\sum_{i=1}^{m}[g_i(θ)−g_i(φ)]²` 与 (21.12) 的分式均忠实于印刷。修复建议：全篇审计结束后移除 (21.10) 前孤立的 `(21.11)`，并将编号 (21.11) 放到余弦级数公式上。

### p.048/59（PDF p.48 / 印刷 p.310）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:13 -0400`。
- PNG：`audit/Douglas_1931_plateau_p048.png`（pngmono 150dpi；页级对账图）。
- 核对：式 (21.13)–(21.15) 前的极限论证、J/I 定义、支配比值及 Lebesgue 极限步骤。
- 结果：PASS±。(21.13) 的积分与 `A(g)`、J/I 简记、(21.14) 支配不等式、比值的两个因子和有限 `A(g)` 情形下的积分极限均与 PDF p.48（印刷 p.310）相符；Lebesgue 脚注完整。Markdown 将 (21.14) 式号独立排在不等式前，而不是与不等式同行，编号仍清晰对应。

### p.049/59（PDF p.49 / 印刷 p.311）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:14 -0400`。
- PNG：`audit/Douglas_1931_plateau_p049.png`（pngmono 150dpi；页级对账图）。
- 核对：式 (21.15)、有限/无限面积情形结论、Fourier 表示 (21.2) 的极限论证、§22 标题与式 (22.1)。
- 结果：PASS。(21.15) 两行积分等式、下半连续性文字、Abel 定理与正项级数论证、(21.2) 的 Fourier 系数和式以及 §22 的面积泛函定义和 E/F/G 公式 (22.1) 均与 PDF p.49（印刷 p.311）相符；未见公式缺项或脚注残片。

### p.050/59（PDF p.50 / 印刷 p.312）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:15 -0400`。
- PNG：`audit/Douglas_1931_plateau_p050.png`（pngmono 150dpi；页级对账图）。
- 核对：式 (22.2)–(22.7)、等号成立条件、Part IV 标题及 §23 开头。
- 结果：PASS。面积泛函 `S(g)`、(22.3) 的能量泛函、(22.4) 不等式、等号条件 (22.5)、极小曲面判别式 (22.6)、`A(g)≥S(g)` (22.7) 与 PDF p.50（印刷 p.312）相符；Part IV 标题和 §23 开头的平面 Jordan 曲线条件亦完整。

### p.051/59（PDF p.51 / 印刷 p.313）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:16 -0400`。
- PNG：`audit/Douglas_1931_plateau_p051.png`（pngmono 150dpi；页级对账图）。
- 核对：Riemann/Osgood–Carathéodory 导言、边界表示 (23.1)–(23.2)、条件 (23.3)、Poisson 公式 (23.4) 及导数关系。
- 结果：PASS。平面 Jordan 曲线与 `Δ` 的叙述、(23.1)–(23.4) 中边界函数、实部调和函数、导数平方条件、两条 Poisson 积分及 `F_1′=±iF_2′` 均与 PDF p.51（印刷 p.313）相符；Osgood 脚注对应完整。

### p.052/59（PDF p.52 / 印刷 p.314）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:18 -0400`。
- PNG：`audit/Douglas_1931_plateau_p052.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p052_eq-23-5-23-6.png`、`audit/300dpi/Douglas_1931_plateau_p052_eq-23-7.png`。
- 核对：(23.5)–(23.8)、由导数关系积分得到的 F(w)、全纯映射单射论证及 Cauchy 计数公式。
- 结果：PASS。复数坐标关系、(23.5)/(23.6) 的恒等记号、(23.7) 的点上等式符号 `\doteq`、唯一原像陈述和 (23.8) Cauchy 公式均与 PDF p.52（印刷 p.314）相符；300dpi 裁片确认了 `≡` 与 `\doteq` 的字形区别，Markdown 保留正确。

### p.053/59（PDF p.53 / 印刷 p.315）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:21 -0400`。
- PNG：`audit/Douglas_1931_plateau_p053.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p053_eq-23-11.png`、`audit/300dpi/Douglas_1931_plateau_p053_footnotes.png`。
- 核对：式 (23.9)–(23.11)、辩值数论证、无分歧/无临界点论证及本页脚注。
- 结果：FAIL。Markdown 的 (23.11) 在 `\left\{\begin{array}{ll}` 后把 `1` 与 `0` 两种情形挤入同一行，且未闭合 `array`/左花括号；印刷明确分为 “1 if interior / 0 if exterior” 两行并闭合分段式，300dpi 裁片确认。页脚另有独立 `<small>` 残片 `$\Gamma_{\rho}$`、`$W=F(w)$`，与完整脚注中的相同字符串重复；第二条完整脚注标记在印刷为 `‡`，Markdown 写作 `\dagger`，而正文引用为 `\ddagger`。修复建议：全篇审计结束后按原图还原 (23.11) 分段式、移除两条独立残片，并将第二条脚注标记还原为 `\ddagger`。

### p.054/59（PDF p.54 / 印刷 p.316）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:23 -0400`。
- PNG：`audit/Douglas_1931_plateau_p054.png`（pngmono 150dpi；页级对账图）。
- 核对：(23.12) Cauchy 表达式、§24 面积泛函值域及 Osgood 脚注。
- 结果：PASS。Cauchy 积分表示 (23.12)、`A(g*)` 等于内面积、`inner area Γ ≤ A(g) ≤ +∞` 的值域以及相应的连续表示论证均与 PDF p.54（印刷 p.316）相符；Osgood exterior-content 脚注完整，无多余脚注残片。

### p.055/59（PDF p.55 / 印刷 p.317）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:26 -0400`。
- PNG：`audit/Douglas_1931_plateau_p055.png`（pngmono 150dpi；页级对账图）。
- 300dpi：`audit/300dpi/Douglas_1931_plateau_p055_theorem-functional.png`。
- 核对：定理 25 的参数表示、`A(g)` 两种积分表示、可达值域、极小表示及 Cauchy 映射结论。
- 结果：FAIL。定理 (A(g)) 第一积分式的 PDF 系数为 `1/(16π)`，Markdown 写作 `1/(1 6 π)`；300dpi 裁片确认。另外，两个积分区域在原页均标为单位圆 `C`，Markdown 将 `C` 错录成小写 `c`。第二个面积差商积分、内面积下界、线性分式变换及映射结论均与印刷一致。修复建议：全篇审计结束后将系数恢复为 `16π`，并把两个 `\int_c` 的下标改为 `\int_C`。

### p.056/59（PDF p.56 / 印刷 p.318）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:27 -0400`。
- PNG：`audit/Douglas_1931_plateau_p056.png`（pngmono 150dpi；页级对账图）。
- 核对：Dirichlet 泛函末段、§V/§26 开头、Koebe 映射说明、(26.1)–(26.2) 及 Radó 脚注。
- 结果：PASS。Dirichlet 泛函的比较文字、polyhedron `Π` 的共形参数化、(26.1) 边界表示、第一基本形式及由 `E=G, F=0` 得到的面积分解 (26.2) 均与 PDF p.56（印刷 p.318）相符；Koebe/Radó 脚注完整，未见内容残片。

### p.057/59（PDF p.57 / 印刷 p.319）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:28 -0400`。
- PNG：`audit/Douglas_1931_plateau_p057.png`（pngmono 150dpi；页级对账图）。
- 核对：(26.3)–(26.12)、由多面体逼近一般曲面的下确界论证及子列/极限表示。
- 结果：PASS。(26.3) 的 Dirichlet 最小性比较、(26.4)–(26.6) 的面积下界、Lebesgue 面积下极限 (26.7)、最小参数表示 (26.8)–(26.10)、(26.11) 的面积等式和二次子列 (26.12) 均与 PDF p.57（印刷 p.319）相符；原印刷 “proper representation. of Γ” 的标点间隔也由 Markdown 保留。

### p.058/59（PDF p.58 / 印刷 p.320）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:30 -0400`。
- PNG：`audit/Douglas_1931_plateau_p058.png`（pngmono 150dpi；页级对账图）。
- 核对：(26.13)–(26.19) 的下半连续性/面积极限论证及 §27 开头。
- 结果：PASS。下半连续性不等式 (26.14)、面积下界 (26.15)–(26.16)、两种最小表示比较 (26.17)–(26.19) 与 PDF p.58（印刷 p.320）一致；“non-finite-area-spanning” 条件下最小面积性质可能空泛的 §27 开头亦完整。

### p.059/59（PDF p.59 / 印刷 p.321）
- 审计者：actor=`Peer-P23`；model=`gpt-6-luna`；effort=`max`；时间=`2026-10-02 01:31 -0400`。
- PNG：`audit/Douglas_1931_plateau_p059.png`（pngmono 150dpi；页级对账图）。
- 核对：Peano 曲线反例构造、四段 Jordan 曲线、投影面积发散论证、Hadamard 边值例及结尾署名。
- 结果：PASS±。螺旋边长、区间分割、四段曲线、xy 投影面积无穷、Hadamard 的 Fourier 边值/调和延拓级数及两条脚注均与 PDF p.59（印刷 p.321）相符。MIT/剑桥署名文字完整保留，但 MinerU 将其拆为两条独立 `<small>` 块；作为版式碎片，不改变署名内容或结尾含义。

## 全篇审计总评与修复登记

- 审计结论：PDF 59 页均完成逐页原页对照；最终分级为 PASS 22 / PASS± 9 / FAIL 28。PASS± 的字号、字形简化和不误导版式差异依 `AUDIT-SOP.md` 保留，未纳入默认修复。
- 审计边界：原始 PDF 未改；审计期间 MinerU Markdown 未改，其审计前/修复前 SHA-256 为 `990ae67f6fe21ece944466067ad2da5811059e6362568946751da62359a9e9a3`。下表逐项汇总 28 个 FAIL 页的人工修复目标；页级条目保有原图、300dpi 证据与完整差异说明。
- 修复收据：单独 `fix(md)` 提交 `a7f1776126de9a6c5811f10f85bb14d2ca01d8ec`；原始 MinerU Markdown 所在提交 `a33f22f3b0bcf430149ea06d98e65076266acc9e`。修复前 SHA-256 `990ae67f6fe21ece944466067ad2da5811059e6362568946751da62359a9e9a3`；修复后 SHA-256 `696ccf5351b332804ba5c77b4e9a332892edb1f5e9d8a57fc3a58c558ce6fd81`。
- 最终复读与只读核验：修复后由首行至末行复读完整 Markdown（2,384 行），逐项对照上表 28 条修复登记及所链接的 PDF 页图/裁片；复读覆盖闭合，没有声称进行修复后重新审计。`git diff --check` 通过；针对登记错误模式的只读搜索无残留命中；审计表仍为 59/59 连续且有 28 条 FAIL 修复登记。未运行测试。
- 修复与集成状态：候选从 exact base `037602429d3b009f6fc468c732073eb3ddf9875f` 开始；候选尚未由 Master 集成，也未 push。Peer 不写根进度日志或总账。

| PDF / 印刷页 | FAIL 修复登记（以对应页级条目原图为准） |
|---|---|
| p.5 / 267 | 将 (1.4₂)/(1.4₃) 的错误标签 `1.42`、`1.43` 分别恢复为 `\tag{1.4_2}`、`\tag{1.4_3}`。 |
| p.6 / 268 | 将 “where generally” 后的 `A(g) \equiv +\infty` 改为 `A(g)=+\infty`。 |
| p.9 / 271 | 将 improper 类与子类符号分别改成 `\mathfrak{S}`、`\mathfrak{S}_1`、`\mathfrak{S}_2`；把段末 `$g$;` 改为 `$g_i$`。 |
| p.10 / 272 | 三条集合等式中的 `\mathfrak{I}` 均改为 `\mathfrak{S}`，包括带撇号项。 |
| p.11 / 273 | 定义式改为 `\mathfrak{M}=\mathfrak{P}+\mathfrak{S}`；(5.1) 分母 `1 6 \pi` 改为 `16\pi`，两个积分域 `c` 改为 `C`。 |
| p.12 / 274 | “parallel but not meridian” 段的第一个脚注标记从 `\ddagger` 改为 `\dagger`，第二处保留 `\ddagger`。 |
| p.13 / 275 | 删除完整两条脚注之前多出的四个独立 `<small>` 碎片：`g`、`\Delta_r^*(g)`、`By |\theta-\phi|`、`\phi`；保留完整脚注。 |
| p.14 / 276 | (5.3) 分母 `1 6 \pi` 改为 `16\pi`；删除完整脚注前孤立的 `<small>p</small>`。 |
| p.18 / 280 | 修复 (7.2)：让 `if ...; and ...; then ...` 按印刷语序作为陈述文本，式号仅保留 `(7.2)`；两处表示类符号 `\Re` 改为 `\mathfrak{R}`。 |
| p.19 / 281 | (9.1) 分母 `1 6\pi` 改为 `16\pi`；表示类符号 `\Re` 改为 `\mathfrak{R}`。 |
| p.20 / 282 | 删除正文序列后多出的 `to +∞` 与 `† tends to +∞.` 两个脚注碎片；在序列后恢复普通正文 “tends to $+\infty$.”，保留完整 † 脚注。 |
| p.21 / 283 | 删除完整注释前的五个重复碎片 `$g^\bullet$`、`\geq A(g^0)`、`+∞)`、`$A(g)$`、`M>0.`；第二条脚注标记由 `\dagger` 改为 `\ddagger`。 |
| p.24 / 286 | (11.8′) 两个积分区域小写 `c` 改为单位圆 `C`。 |
| p.25 / 287 | 在 (11.13) 后补回印刷整式 `\sum_{p,q} p\zeta^p\cdot qz^q=(m+1)\zeta z(\zeta^m+z^m)(\zeta-z)^{-2}-2\zeta z(\zeta^{m+1}-z^{m+1})(\zeta-z)^{-3}`。 |
| p.27 / 289 | 两个变换积分的分母 `1 6\pi` 均改为 `16\pi`；删除完整脚注前的孤立 `<small>§17</small>`。 |
| p.28 / 290 | (12.3) 与 (12.4) 的四个分母 `1 6\pi` 均改为 `16\pi`。 |
| p.31 / 293 | 将错排的 `(1 3. 5 ^ {\prime})` 还原为清晰的 `(13.5′)` 式号；不改公式主体。 |
| p.33 / 295 | 三处 `1 6\pi` 改为 `16\pi`；S′ 分子第二项 `(n−1)` 改为 `(m−1)`；删除多余 `. 1 0)` 标签碎片。 |
| p.34 / 296 | (14.2) 分母 `1 6\pi` 改为 `16\pi`；保留印刷在 (14.5) 内部的 `\dot\Delta_r` 记号不一致。 |
| p.35 / 297 | 修复 (14.7)/(14.7′) 两个公式标签；两处分母 `1 6\pi` 改为 `16\pi`。保留 p.297 与 p.293 之间的源页表达差异。 |
| p.37 / 299 | (17.3) 分母改为 `16\pi`；积分区域 `S′` 改为 `S_\epsilon`。 |
| p.40 / 302 | 删除完整页脚注之外的 12 个独立 OCR 残片：`d'A`、`Γ,`、`$x_i=f_i(t)$`、`$x_i=S_{im}(t)$`、`$\Gamma^{(m)}$`、`I,`、`$t=\omega_m(\theta)$`、`C,`、`C`、`§17`、`l=0,`、重复的 `$t=\omega_m(\theta)$`；保留完整脚注与正文。 |
| p.41 / 303 | (19.8) 中把 `f ^ {i}` 改为 `f _ {i}`，恢复印刷下标。保留 `\mathfrak{M}'` 被简化为普通 M′ 的 PASS± 样式差异。 |
| p.43 / 305 | 将同一几何变换名的前两处 `T` 改为 `\mathfrak{G}`，与后文及原页 `𝔊` 统一。 |
| p.44 / 306 | 将 `T^{-1}` 改为 `\mathfrak{G}^{-1}`，与 p.305 同一变换名统一。 |
| p.47 / 309 | 移除 (21.10) 关系式前误置的孤立 `(21.11)`；将编号 (21.11) 放在余弦级数公式，保留 (21.10) 原标签。 |
| p.53 / 315 | 将 (23.11) 恢复为两行分段式并闭合 array/大括号；删除 `$\Gamma_{\rho}$` 与 `$W=F(w)$` 两个独立脚注碎片；将第二条脚注标记 `\dagger` 改为 `\ddagger`。 |
| p.55 / 317 | 定理 A(g) 第一积分的分母 `1 6\pi` 改为 `16\pi`；两个积分区域下标小写 `c` 改为单位圆 `C`。 |
