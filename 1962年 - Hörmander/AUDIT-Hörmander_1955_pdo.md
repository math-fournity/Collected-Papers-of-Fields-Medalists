# AUDIT：Hörmander_1955_pdo

- 审计 actor：Peer-P33
- model：gpt-6-luna
- reasoning effort：max
- 基线：main HEAD `037602429d3b009f6fc468c732073eb3ddf9875f`
- 原件：`Hörmander_1955_pdo.pdf`，88 PDF 页；逐页图像为扫描页，含 OCR 文本层。
- MinerU Markdown：`Hörmander_1955_pdo_mineru/Hörmander_1955_pdo__Hörmander_1955_pdo.md`
- 审计模式：扫描件；每页 150dpi pngmono 目检，疑难字形/内容再以 300dpi 原页裁片仲裁。以下逐页等级以印刷页为准。
- 修复纪律：全篇逐页审计完成前不修改 MinerU Markdown。

## 总评与覆盖

- 范围：原件 PDF 88/88 页；逐页审计与原始 MinerU Markdown 对照均已完成。
- 原始 MinerU 对照等级：63 PASS、25 FAIL。等级表示修复前 MinerU 内容相对印刷页的结果；本节与逐页记录不因后续修复将 FAIL 改记为 PASS。
- 页面证据：88 张 150dpi 全页图；33 张 300dpi 仲裁裁片。审计文件引用 121 个页面/裁片路径，终验未发现缺失引用。
- MinerU doc_id：UNKNOWN。对本篇 *_mineru 导出目录递归检索 doc_id、document_id、docId 等字段未命中；不据此推断远端记录号。

## PDF p.001/88（目录前置页；未见印刷页码）
- 时间：2026-10-01 16:09:51 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p001.png`（pngmono 150dpi）
- 核对：题名、作者与所在地；目录首页从 PREFACE 162 至 CHAPTER III §3.5 的标题/页码；期刊卷期与印刷日期页脚。
- print 证据：原页图 p.001（本目录页未见印刷页码；页脚为 Acta Mathematica 94，1955-09-26）。
- 结果：PASS。已见目录条目和题录信息与 Markdown 相符；本页未见内容级差异。
- 校正（2026-10-01 16:10:59 EDT；Peer-P33 | gpt-6-luna/max）：印刷页码 162 实际见于 PDF p.002 页眉；PDF p.001 为未见页码的目录前置页。页级等级不变。

## PDF p.002/88（印刷页 162）
- 时间：2026-10-01 16:11:36 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p002.png`（pngmono 150dpi）
- 核对：目录续页 §3.6–§4.2 与 REFERENCES 条目及页码；PREFACE §0.1 全段和超双曲方程排版；§0.2 本页可见开头；印刷页眉 folio。
- print 证据：原页图 p.002（页眉印刷 folio 162；超双曲方程左右两组二阶导数均以 x/y 变量列示）。
- 结果：PASS。目录、文字和等式与 Markdown 对应段落相符；未见内容级差异。

## PDF p.003/88（印刷页 163）
- 时间：2026-10-01 16:12:11 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p003.png`（pngmono 150dpi）
- 核对：PREFACE §0.2 续段、§0.3–§0.4；CHAPTER I 标题与 §1.0 本页部分；脚注 1。
- print 证据：原页图 p.003（页眉印刷 folio 163；页末脚注引用 Višik [34]）。
- 结果：PASS。正文衔接、标题、脚注和本页可见内容与 Markdown 相符；未见内容级差异。

## PDF p.004/88（印刷页 164）
- 时间：2026-10-01 16:12:58 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p004.png`（pngmono 150dpi）
- 核对：PREFACE §0.2 末段及 CHAPTER I §1.1 开头；公式 (1.1.1)–(1.1.3)；脚注 1。
- print 证据：原页图 p.004（页眉印刷 folio 164；公式 (1.1.1) 线性关系、(1.1.2) 直和范数与 (1.1.3) 图集定义）。
- 结果：PASS。段落衔接、三式、封闭/预闭定义开头和脚注均与 Markdown 相符；未见内容级差异。

## PDF p.005/88（印刷页 165）
- 时间：2026-10-01 16:13:35 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p005.png`（pngmono 150dpi）
- 核对：Theorem 1.1 陈述及不等式 (1.1.4)、证明中的映射 (1.1.5)、直和空间内积、Lemma 1.1 陈述与证明开头。
- print 证据：原页图 p.005（页眉印刷 folio 165；(1.1.4)、(1.1.5) 及伴随算子符号可辨）。
- 结果：PASS。定理、公式、证明衔接和 Lemma 1.1 开头与 Markdown 相符；未见内容级差异。

## PDF p.006/88（印刷页 166）
- 时间：2026-10-01 16:14:00 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p006.png`（pngmono 150dpi）
- 核对：Lemma 1.1 证明收尾；Lemma 1.2 及右逆公式 (1.1.6)；Lemma 1.3 与证明；脚注 1。
- print 证据：原页图 p.006（页眉印刷 folio 166；等式 (TT^*u,u) 与 (1.1.6) 可辨）。
- 结果：PASS。两引理陈述、关键等式、证明衔接和脚注与 Markdown 相符；未见内容级差异。

## PDF p.007/88（印刷页 167）
- 时间：2026-10-01 16:17:53 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p007.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p007_eq-1.2.1.png`、`audit/300dpi/Hörmander_1955_pdo_p007_dimension.png`、`audit/300dpi/Hörmander_1955_pdo_p007_dimension-comparison.png`
- 核对：§1.2 开头；坐标指标、公式 (1.2.1) 系数的多指标上标、公式 (1.2.2)；常系数定义中的维数符号；公式 (1.2.3) 与脚注 1。
- print 证据：150dpi 原页页眉印刷 folio 167。300dpi 裁片显示 (1.2.1) 系数为 `a^{α₁…αₖ}(x)`，整个指标序列处于同一上标；常系数定义中的变量列为 `x¹,…,x^ν`，维数符号为 `ν`，空间为 `R^ν`。
- MinerU 差异：Markdown 将 (1.2.1) 写作 `a^{α₁} …^{αₖ}(x)`，改变了多指标系数的排版/结合；坐标末指标写成 `x^n`，常系数定义写成 `v-dimensional` 与 `R^v`。
- 补充复核（2026-10-02 01:29:14 EDT；Peer-P33 | gpt-6-luna/max）：(1.2.1) 左端在 Markdown 写作小写 `p u`，p.007 300dpi 公式裁片显示印刷为大写 `P u`；Grade 维持 FAIL。
- 结果：FAIL。至少公式 (1.2.1) 的上标结构与印刷原文不符；坐标及维数符号亦须按原页逐处修复。本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.008/88（印刷页 168）
- 时间：2026-10-01 16:19:13 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p008.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p008_definition-1.1.png`
- 核对：公式 (1.2.4) 与代数伴随表达式；Lemma 1.4 陈述/证明；Definition 1.1 的闭包、最小/最大算子及伴随记号；弱扩张说明。
- print 证据：原页图 p.008（页眉印刷 folio 168）；300dpi Definition 1.1 裁片确认最小算子记号为 `\overline{P}_0`，定义中的伴随算子为 `\overline{P}`。
- 结果：PASS。公式、引理、Definition 1.1 与 Markdown 的伴随记号相符；本页未见内容级差异。

## PDF p.009/88（印刷页 169）
- 时间：2026-10-01 16:19:54 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p009.png`（pngmono 150dpi）
- 核对：Lemma 1.4 后续说明；一元算子 `d^n/dx^n` 的例子与端点 Cauchy 数据；Definition 1.2；Lemma 1.5 与不等式 (1.2.5)；脚注 1。
- print 证据：原页图 p.009（页眉印刷 folio 169；两端点导数条件、(1.2.5) 及脚注可辨）。
- 结果：PASS。定义、边界条件、估计式及脚注均与 Markdown 相符；未见内容级差异。

## PDF p.010/88（印刷页 170）
- 时间：2026-10-01 16:23:27 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p010.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p010_lemma-1.5.png`、`audit/300dpi/Hörmander_1955_pdo_p010_remark-1.2.6.png`
- 核对：Lemma 1.5 证明续段；关于最小/最大定义域的 Remark；Lemma 1.6 与估计式 (1.2.6)；边界连续性断言及证明开头。
- print 证据：原页图 p.010 页眉印刷 folio 170；Lemma 1.5 证明裁片读作 `D_{Q_0}`；Remark 裁片先给 `D_{P_0}⊂D_{Q_0}`，再将该条件换成表面上较弱的 `D_P⊂D_Q`。
- MinerU 差异：Lemma 1.5 结论把 `D_{Q_0}` 写为 `D_{Q_\bullet}`；Remark 的最小域关系以 `P_\bullet` 代 `P_0`、漏掉 `Q_0`，且“apparently weaker”条件误留 `P_\bullet` 而应为无下标 `P`。同页 Chapter II 引言还把有界域所在空间 `R^\nu` 录成 `R^{r}`；上方这张 Remark 裁片同时显示其印刷写法 `R^\nu`。
- 补充复核（2026-10-02 00:45:43 EDT；Peer-P33 | gpt-6-luna/max）：300dpi 逐处复核确认上述下标差异，Grade 维持 FAIL。
- 补充复核（2026-10-02 01:03:15 EDT；Peer-P33 | gpt-6-luna/max）：复读 p.010 Chapter II 引言，并核对 `audit/300dpi/Hörmander_1955_pdo_p010_remark-1.2.6.png` 上方对应原句，确认 `R^{r}` 对应印刷 `R^\nu`；Grade 维持 FAIL。
- 补充复核（2026-10-02 01:18:25 EDT；Peer-P33 | gpt-6-luna/max）：Lemma 1.6 陈述还把最小定义域 `D_{P_0}` 录为 `D_{P_*}`；见已列 p010 Remark 300dpi 裁片。Grade 维持 FAIL。
- 结果：FAIL。定义域下标及空间维数符号与印刷页不符；(1.2.6) 与除上述差异外的已核段落相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.011/88（印刷页 171）
- 时间：2026-10-01 16:25:03 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p011.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p011_cauchy-space.png`、`audit/300dpi/Hörmander_1955_pdo_p011_cauchy-data.png`
- 核对：Lemma 1.7 及 (1.2.7)；§1.3、Definition 1.3 商空间 (1.3.1)；紧支撑函数的 Cauchy 数据段落；Definition 1.4 与 (1.3.2)。
- print 证据：原页图 p.011 页眉 folio 171。300dpi 裁片确认 (1.3.1) 为 `C = G_P/G_{P_0}`；Cauchy 数据段落中，印刷有三处一般定义域 `D_P` 及两处最小定义域 `D_{P_0}`。
- MinerU 差异：Markdown 将 (1.3.1) 分母记为 `G_{P_{\bullet}}` 而非 `G_{P_0}`；Cauchy 数据相关句中的五处 `D_p`，印刷前三处为 `D_P`，后两处为 `D_{P_0}`。
- 补充复核（2026-10-02 01:30:16 EDT；Peer-P33 | gpt-6-luna/max）：逐字符比对 p011 两张 300dpi 裁片和 Markdown，确认上述五处大小写/下标差异以及商空间分母差异；Grade 维持 FAIL。
- 结果：FAIL。(1.3.1) 商空间分母及五处 Cauchy 数据定义域记号与印刷原文不符；本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.012/88（印刷页 172）
- 时间：2026-10-01 16:26:12 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p012.png`（pngmono 150dpi）
- 核对：Definition 1.4 收尾、Definition 1.5、Theorem 1.2 及其证明（含 (1.3.3) 与构造的 T）；Lemma 1.8 陈述。
- print 证据：原页图 p.012（页眉印刷 folio 172；定义域包含关系、T 的公式及 Lemma 1.8 可辨）。
- 结果：PASS。边界条件定义、定理假设/结论、投影公式和引理陈述与 Markdown 相符；未见内容级差异。

## PDF p.013/88（印刷页 173）
- 时间：2026-10-01 16:26:40 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p013.png`（pngmono 150dpi）
- 核对：Lemma 1.8 证明；Theorem 1.3 陈述/证明；投影与右逆构造 T；图空间到解空间的映射表示。
- print 证据：原页图 p.013（页眉印刷 folio 173；T、ΓT 与图空间映射均可辨）。
- 结果：PASS。定理条件、投影/右逆公式和证明步骤与 Markdown 相符；未见内容级差异。

## PDF p.014/88（印刷页 174）
- 时间：2026-10-01 16:27:57 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p014.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p014_dimension-Rnu.png`
- 核对：Theorem 1.3 证明收尾；w-convergence 段落；CHAPTER II §2.0 标题及开头；常系数微分算子所在空间维数。
- print 证据：原页图 p.014 页眉 folio 174；300dpi 裁片中印刷为 `R^ν`。
- MinerU 差异：§2.0 开头将该空间记作 `R^v`，与印刷的 Greek `ν` 不同。
- 结果：FAIL。空间维数符号与原文不一致；本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.015/88（印刷页 175）
- 时间：2026-10-01 16:28:32 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p015.png`（pngmono 150dpi）
- 核对：CHAPTER II §2.0 续段；(2.0.1)–(2.0.3) 三项刻画；能量积分法说明与章节结果概述。
- print 证据：原页图 p.015（页眉印刷 folio 175；三处带波浪号的 P/Q 比值与积分界可辨）。
- 结果：PASS。三个公式的分子/分母、积分变量、严格不等式和渐近箭头与 Markdown 相符；本页其余文字及编号无差异。

## PDF p.016/88（印刷页 176）
- 时间：2026-10-01 16:29:10 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p016.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p016_dimension-Cnu.png`
- 核对：§2.1 向量空间与双线性配对；(2.1.1)–(2.1.5) 多项式/微分算子对应、Fourier 变换、Parseval 等式及 Leibniz 公式。
- print 证据：原页图 p.016（页眉印刷 folio 176）；300dpi 裁片确认多项式空间记号为 `C_\nu`，与相邻 `R^\nu` 的维数符号一致。
- MinerU 差异：段落将复向量空间记号录为 `C_v`，印刷为 `C_\nu`。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：全篇复读后复核 p.016 的 (2.1.2) 后说明；300dpi 裁片确认 `C_\nu`，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。`C_v` 中维数记号与印刷 Greek ν 不符；本页所列其他公式和指标与印刷相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.017/88（印刷页 177）
- 时间：2026-10-01 16:30:43 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p017.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p017_laplace-exponent.png`
- 核对：Taylor/Leibniz 公式 (2.1.6)；§2.2 与 Theorem 2.1 估计 (2.2.1)；Laplace 变换归一化因子；Lemma 2.1 及 (2.2.2)。
- print 证据：原页图 p.017 页眉 folio 177；300dpi 裁片中 Laplace 变换前因子指数为 `-(ν/2)`。
- MinerU 差异：Laplace 变换 Markdown 将该指数转录为 `-(r/2)`。
- 结果：FAIL。归一化因子中的维数符号与印刷原文不符；其他本页显示的公式/编号相符。本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.018/88（印刷页 178）
- 时间：2026-10-01 16:31:20 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p018.png`（pngmono 150dpi）
- 核对：Lemma 2.1 证明结尾；Theorem 2.1 证明与 (2.2.1)；§2.3 起始及 (2.3.1)、(2.3.1)'、(2.3.2)。
- print 证据：原页图 p.018（页眉印刷 folio 178；积分估计、导数多项式和三个编号均可辨）。
- 结果：PASS。证明中系数/积分项、章节标题、撇号与波浪号记号均与 Markdown 相符；未见内容级差异。

## PDF p.019/88（印刷页 179）
- 时间：2026-10-01 16:31:48 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p019.png`（pngmono 150dpi）
- 核对：Theorem 2.2 条件 (2.3.3)、Remark；证明所用的 (2.3.4)–(2.3.8) 与数组对称性说明。
- print 证据：原页图 p.019（页眉印刷 folio 179；波浪号比值、复共轭、阶乘及 Fourier 项均可辨）。
- 结果：PASS。比值、共轭、求和指标、阶乘、公式编号和段落与 Markdown 相符；未见内容级差异。

## PDF p.020/88（印刷页 180）
- 时间：2026-10-01 16:32:18 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p020.png`（pngmono 150dpi）
- 核对：Theorem 2.2 必要性证明收尾；§2.4 二次微分形式 (2.4.1)–(2.4.4)；共轭与实值条件。
- print 证据：原页图 p.020（页眉 folio 180；(2.3.9)、多重求和、复共轭及实值公式可辨）。
- 结果：PASS。求和范围、共轭位置、波浪号、公式编号和实值条件与 Markdown 相符；未见内容级差异。

## PDF p.021/88（印刷页 181）
- 时间：2026-10-01 16:32:51 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p021.png`（pngmono 150dpi）
- 核对：二次型微分公式；散度恒等式 (2.4.5)–(2.4.6)；Lemma 2.2 及证明；Lemma 2.3 陈述开头。
- print 证据：原页图 p.021（页眉 folio 181；η_k 因子、负号、散度及反对称张量记号可辨）。
- 结果：PASS。求和指标、η 项符号、坐标微分和引理陈述与 Markdown 相符；未见内容级差异。

## PDF p.022/88（印刷页 182）
- 时间：2026-10-01 16:33:24 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- 300dpi 裁片：audit/300dpi/Hörmander_1955_pdo_p022_sum-dimension-nu.png
- PNG：`audit/Hörmander_1955_pdo_p022.png`（pngmono 150dpi）
- 核对：Lemma 2.3 证明中的 (2.4.7)、Euler 等式、反对称 (G^{ik}) 构造与 (2.4.8)；§2.5 Parseval 等式 (2.5.1)。
- print 证据：原页图 p.022（页眉 folio 182）；300dpi 裁片确认 (2.4.7) 与 Euler 等式的求和上限均为 Greek ν。
- MinerU 差异：(2.4.7) 的求和上限录为 v，原页为 ν。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：扩展复核本篇维数符号后检查 p.022 的 (2.4.7)；300dpi 原页确认其求和上限为 ν，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。(2.4.7) 求和上限维数符号与印刷原文不符；其余已列公式与本页对应文字相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.023/88（印刷页 183）
- 时间：2026-10-01 16:34:43 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p023.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p023_lemma-2.6.png`
- 核对：Lemma 2.4 与 (2.5.2)–(2.5.4)；Lemma 2.5；Lemma 2.6 的曲面积分；§2.6 起始及 (2.6.1)。
- print 证据：原页图 p.023 页眉 folio 183；300dpi 裁片确认 Lemma 2.6 的 u 上方是波浪号（tilde），不是横 bar。
- 结果：PASS。积分式、共轭变量、符号系数及 Lemma 2.6 的 tilde 均与 Markdown 相符；未见内容级差异。

## PDF p.024/88（印刷页 184）
- 时间：2026-10-01 16:35:18 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p024.png`（pngmono 150dpi）
- 核对：公式 (2.6.2)–(2.6.6)；积分分部与 Schwarz 不等式；Lemma 2.7 中域宽定义及导数估计。
- print 证据：原页图 p.024（页眉 folio 184；虚部因子、共轭项、域宽 (B^k) 及系数 (m) 可辨）。
- 结果：PASS。公式系数、导数阶数、共轭位置、域宽和公式编号与 Markdown 相符；未见内容级差异。

## PDF p.025/88（印刷页 185）
- 时间：2026-10-01 16:35:51 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p025.png`（pngmono 150dpi）
- 核对：Lemma 2.7 归纳证明与 (2.6.6)；Lemma 2.8 及 (2.6.7)；Theorem 2.2 充分性证明 (2.6.8)；§2.7 起始标题。
- print 证据：原页图 p.025（页眉 folio 185；(2\delta=B^k)、((m-1)B^k)、(|Q(D)u|) 估计可辨）。
- 结果：PASS。归纳系数、估计常数、平方范数及章节切换与 Markdown 相符；未见内容级差异。

## PDF p.026/88（印刷页 186）
- 时间：2026-10-01 16:36:20 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- 300dpi 裁片：audit/300dpi/Hörmander_1955_pdo_p026_xi-nu-example.png
- PNG：`audit/Hörmander_1955_pdo_p026.png`（pngmono 150dpi）
- 核对：§2.7 Schrödinger 与 heat 两个例子；(2.7.1)–(2.7.5)；Definition 2.1 与脚注 1。
- print 证据：原页图 p.026（页眉 folio 186）；300dpi 裁片确认 (2.7.1)–(2.7.5) 中末变量的维数指标为 Greek ν。
- MinerU 差异：公式后说明把 “one in ξ_ν” 录为 ξ_v。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：扩展维数符号复核时回看 p.026 的说明句；300dpi 原页确认 ξ_ν，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。说明句中的维数下标与印刷不符；本页其他多项式项、正负号和求和范围相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.027/88（印刷页 187）
- 时间：2026-10-01 16:36:51 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- 300dpi 裁片：audit/300dpi/Hörmander_1955_pdo_p027_derivative-sum-dimension.png
- PNG：`audit/Hörmander_1955_pdo_p027.png`（pngmono 150dpi）
- 核对：Theorem 2.3 及两部分证明；不等式 (2.7.6)；π(ξ)、r(ξ) 分解与 (Q/P) 比值估计。
- print 证据：原页图 p.027（页眉 folio 187）；300dpi 裁片确认导数平方和中的求和上限为 Greek ν。
- MinerU 差异：式 (2.7.6) 前的导数平方和将求和上限录为 v，印刷为 ν。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：扩展维数符号复核时检查 p.027 的 Theorem 2.3 证明；300dpi 原页确认求和上限为 ν，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。导数平方和的维数上限与印刷原文不符；其余已核条件、偏导变量、幂次和比值估计相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.028/88（印刷页 188）
- 时间：2026-10-01 16:37:27 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p028.png`（pngmono 150dpi）
- 核对：Theorem 2.4；可分变量多项式与向量分解；Theorem 2.5；比较界及 (2.7.7)；证明的有限维基展开开头。
- print 证据：原页图 p.028（页眉 folio 188；μ<ν、分块向量、波浪号分母与线性包关系可辨）。
- 结果：PASS。可分变量、比较常数、分母因子、严格不等式及求和指标与 Markdown 相符；未见内容级差异。

## PDF p.029/88（印刷页 189）
- 时间：2026-10-01 16:37:56 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p029.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p029_theorem-2.6-domain.png`
- 核对：Theorem 2.5 证明收尾；§2.8 起始；Theorem 2.6 假设、(2.8.1) 与反向连续性断言；证明中的 (2.8.2) 及 Fourier 积分开头。
- print 证据：原页图 p.029（页眉 folio 189）；300dpi 裁片确认 Theorem 2.6 的量词对象为 `D_{P_0}`；(2.8.1) 积分商与编号可辨。
- MinerU 差异：Theorem 2.6 首句将 `D_{P_0}` 录为 `D_{P_*}`。
- 补充复核（2026-10-02 01:19:51 EDT；Peer-P33 | gpt-6-luna/max）：此前页签 PASS 未识别该下标差异；300dpi 裁片确认 Markdown `D_{P_*}` 与印刷 `D_{P_0}` 不同，Grade 改为 FAIL；先前 PASS 提交保留在 Git 历史。
- 结果：FAIL。Theorem 2.6 假设中的最小定义域下标与印刷原文不符；本页其余已核公式与编号相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.030/88（印刷页 190）
- 时间：2026-10-01 16:38:24 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p030.png`（pngmono 150dpi）
- 核对：Theorem 2.6 证明中的 (2.8.3)–(2.8.5)；Theorem 2.7 陈述；Fourier–Hölder 指数与积分幂次。
- print 证据：原页图 p.030（页眉 folio 190；波浪号分母、(2.8.5)、(2p/(p-2)) 与 (p') 指数可辨）。
- 结果：PASS。范数平方、积分测度、Sobolev 指数及 Hölder 幂次与 Markdown 相符；未见内容级差异。

## PDF p.031/88（印刷页 191）
- 时间：2026-10-01 16:38:57 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p031.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p031_minimal-domain.png`、`audit/300dpi/Hörmander_1955_pdo_p031_domain-subscript-review.png`
- 核对：Example 1 的最小定义域；Theorem 2.6 连续性判据及图空间表示；Theorem 2.7 两例；(2.8.7) 迹限制定义与结尾说明；Theorem 2.8 条件开头。
- print 证据：原页图 p.031 页眉 folio 191；裁片确认 Example 1、Theorem 2.6 和两处迹限制说明均用 `D_{P_0}`，图空间为 `G_{P_0}`。
- MinerU 差异：Example 1 把 `D_{P_0}` 录为 `D_{P_*}`；Theorem 2.6 段落将 `D_{P_0}`、`G_{P_0}` 分别录为 `D_{P_\bullet}`、`G_{P_\bullet}`；迹限制定义有一处写 `D_P`（漏掉 `0`），结尾 “roughly” 句又将 `D_{P_0}` 录为 `D_{P_*}`。
- 补充复核（2026-10-02 01:21:46 EDT；Peer-P33 | gpt-6-luna/max）：复读 p.031 对应 Markdown 与两张 300dpi 裁片后，将此前记录的两处差异补全为上述五处最小域下标差异；Grade 维持 FAIL，原 PASS 提交保留在 Git 历史。
- 结果：FAIL。五处最小定义域下标与图空间标签转录不符；本页其余已核公式、编号及变量维数相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.032/88（印刷页 192）
- 时间：2026-10-01 16:39:30 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p032.png`（pngmono 150dpi）
- 核对：Theorem 2.8 条件 (2.8.8)；坐标变换；(2.8.9)–(2.8.12)；正交子空间积分变量与 Fourier 常数。
- print 证据：原页图 p.032（页眉 folio 192；μ/ν 上下限、ν−μ 指数、Sigma′ 面元及 (2.8.10) 指数分解可辨）。
- 结果：PASS。变换后的维数、积分域、常数幂次和公式编号与 Markdown 相符；未见内容级差异。

## PDF p.033/88（印刷页 193）
- 时间：2026-10-01 16:40:05 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p033.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p033_fourier-normalization-2.8.8.png`
- 核对：(2.8.13)–(2.8.17)；平面限制、有限指标和、(t_\alpha) 定义、正定二次型与 Fourier 面积分估计。
- print 证据：原页图 p.033（页眉 folio 193；α/β 指标、μ 维限制、ψ_{αβ} 共轭项与积分常数可辨）；300dpi 裁片确认延续公式中的归一化因子为 `(2π)^{-ν/2}`。
- MinerU 差异：Markdown 将该归一化指数写为 `(2π)^{-v/2}`；原页 300dpi 裁片中的维数符号为 Greek `ν`。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：整篇复读时核对 p.033 的 (2.8.8) 延续公式，发现此前页签未覆盖该归一化因子；300dpi 原页裁片确认 `ν`，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。归一化指数的维数符号与印刷原文不符；(2.8.13)–(2.8.17) 所列积分变量、复共轭、阶乘、求和范围和估计方向相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.034/88（印刷页 194）
- 时间：2026-10-01 16:40:43 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p034.png`（pngmono 150dpi）
- 核对：(2.8.18) 超平面迹条件；Theorem 2.8 证明收尾的 Fourier 常数/测度；Lemma 2.9 与 (2.8.19) 被积函数和上界；证明开头。
- print 证据：原页图 p.034（页眉 folio 194；ν−μ 次幂、正负无穷积分限及 4n² 上界可辨）。
- 结果：PASS。积分区域、归一化常数、波浪号、分母平方和不等式方向与 Markdown 相符；未见内容级差异。

## PDF p.035/88（印刷页 195）
- 时间：2026-10-01 16:41:14 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p035.png`（pngmono 150dpi）
- 核对：Lemma 2.9 估计的 (I_1,I_2) 分拆与 4n² 界；Theorem 2.9 超平面迹估计/法向导数定义；distinguished representative 构造开头。
- print 证据：原页图 p.035（页眉 folio 195；(n^2) 系数、法向量 N 的求和及 Σ 迹记号可辨）。
- 结果：PASS。积分限、幂次、法向导数下标和代表元构造条件与 Markdown 相符；未见内容级差异。

## PDF p.036/88（印刷页 196）
- 时间：2026-10-01 16:41:48 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p036.png`（pngmono 150dpi）
- 核对：distinguished representative 构造续段；Theorem 2.10 与 (2.8.20)；Example 1 起始及脚注 1。
- print 证据：原页图 p.036（页眉 folio 196；(2^{-n}) 几何权、(P_0) 定义域、(2.8.20) 与边界脚注可辨）。
- 结果：PASS。几何权、最小域下标、乘积估计和例子条件与 Markdown 相符；未见内容级差异。

## PDF p.037/88（印刷页 197）
- 时间：2026-10-01 16:42:39 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p037.png`（pngmono 150dpi）
- 核对：Theorem 2.10 两个例子；乘积求导式；Lemma 2.10 的平移/微分不变性与 Taylor 展开。
- print 证据：原页图 p.037（页眉 folio 197；Laplace/wave 算子、偏导顺序、α 多重指标求和可辨）。
- 结果：PASS。乘积公式、导数变量、(x^1) 依赖条件及 Lemma 2.10 的系数排列与 Markdown 相符；未见内容级差异。

## PDF p.038/88（印刷页 198）
- 时间：2026-10-01 16:43:29 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p038.png`（pngmono 150dpi）
- 核对：Theorem 2.11 局部性与分割统一；Theorem 2.12；Lemma 2.11 卷积逼近证明；边界点讨论开头。
- print 证据：原页图 p.038（页眉 folio 198；所有 (P_0) 下标、有限覆盖求和和卷积导数等式可辨）。
- 结果：PASS。最小域下标、α 指标、求和范围、卷积关系与 Markdown 相符；未见内容级差异。

## PDF p.039/88（印刷页 199）
- 时间：2026-10-01 16:44:23 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p039.png`（pngmono 150dpi）
- 核对：Theorem 2.13 边界正则条件；法向导数强收敛说明；必要性/充分性证明至本页末；半空间卷积条件。
- print 证据：原页图 p.039（页眉 folio 199；(x_0,Sigma,N,delta y) 记号、法向导数和卷积项可辨）。
- 结果：PASS。点/平面条件、方向内积、收敛量及卷积支撑条件与 Markdown 相符；未见内容级差异。

## PDF p.040/88（印刷页 200）
- 时间：2026-10-01 16:44:53 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p040.png`（pngmono 150dpi）
- 核对：Theorem 2.13 边界条件收尾；Weyl 引理段；Definitions 2.2–2.3 与 (2.8.21)；Lemma 2.12 证明及 (2.8.22)。
- print 证据：原页图 p.040（页眉 folio 200；(m-1) 阶横向导数条件、平移不变式与幂次凸组合可辨）。
- 结果：PASS。定义量词、lineality 公式、次数条件和范数幂次与 Markdown 相符；未见内容级差异。

## PDF p.041/88（印刷页 201）
- 时间：2026-10-01 16:45:26 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p041.png`（pngmono 150dpi）
- 核对：Theorem 2.14 与证明；关于 (P_0^n) 域的 Remark；§2.9、映射 (2.9.1) 与 Theorem 2.15 条件 (2.9.2)。
- print 证据：原页图 p.041（页眉 folio 201；连续迭代的 n、平方可积比值和趋零箭头可辨）。
- 结果：PASS。幂次、定义域、映射和渐近条件与 Markdown 相符；未见内容级差异。

## PDF p.043/88（印刷页 203）
- 时间：2026-10-01 16:47:55 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p043.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p043_dimension.png`
- 核对：Theorem 2.15 反向紧性证明与 (2.9.7)–(2.9.10)；Theorem 2.16 映射/条件 (2.9.11)–(2.9.12)；Theorem 2.17 起始。
- print 证据：原页图 p.043 页眉 folio 203；300dpi 裁片中 Theorem 2.16 的维数上界符号与正文的维数符号同形，为 Greek ν。
- MinerU 差异：Theorem 2.16 写为 “dimension less than v”；该位置的印刷符号为 ν。
- 结果：FAIL。维数符号与印刷记号不符；本页其余连续性条件和序列公式相符。本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.042/88（印刷页 202）
- 时间：2026-10-01 16:45:57 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p042.png`（pngmono 150dpi）
- 核对：Theorem 2.15 正向紧性证明；(2.9.3)–(2.9.4)；紧集尾部估计与子列 Cauchy 论证；反向证明中的 (2.9.5)–(2.9.6)。
- print 证据：原页图 p.042（页眉 folio 202；ε² 尾估计、频率分离条件及 (u_n) 振荡序列可辨）。
- 结果：PASS。频率变量、极限次序、ε 幂次、波浪号分母与 Markdown 相符；未见内容级差异。

## PDF p.044/88（印刷页 204）
- 时间：2026-10-01 16:48:33 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p044.png`（pngmono 150dpi）
- 核对：Theorem 2.17 证明中的 (M_C)、齐次分解与 (2.9.13)；Lemma 2.13 陈述/归纳证明开头。
- print 证据：原页图 p.044（页眉 folio 204；交集上下限、τ 替换和多重导数长度 (m-1) 可辨）。
- 结果：PASS。线性空间交集、齐次阶数、替换变量和引理条件与 Markdown 相符；未见内容级差异。

## PDF p.045/88（印刷页 205）
- 时间：2026-10-01 16:49:06 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- 300dpi 裁片：audit/300dpi/Hörmander_1955_pdo_p045_dimension-integrability.png
- PNG：`audit/Hörmander_1955_pdo_p045.png`（pngmono 150dpi）
- 核对：Lemma 2.13 证明收尾；Theorem 2.17 归纳部分；Lemma 2.14 可积指数；Theorem 2.18 的 Lq 范围。
- print 证据：原页图 p.045（页眉 folio 205；(P_m,R) 分解、(	ilde P) 幂次和 ν 维数阈值可辨）。
- MinerU 差异：Lemma 2.14 的阈值录为 q>v，随后一句的 “constant v” 也应为 Greek ν。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：扩展维数符号复核时检查 p.045 的 Lemma 2.14；300dpi 原页确认阈值和说明句均为 ν，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。Lemma 2.14 的可积阈值及其说明句的维数符号与印刷不符；本页其他已核多项式次数、lineality 交集和 Theorem 2.18 范围相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.046/88（印刷页 206）
- 时间：2026-10-01 16:49:43 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- 300dpi 裁片：audit/300dpi/Hörmander_1955_pdo_p046_lineality-intersection-dimension.png
- PNG：`audit/Hörmander_1955_pdo_p046.png`（pngmono 150dpi）
- 核对：(2.9.14)–(2.9.15) lineality 空间恒等式；齐次多项式证明；多项式系统的“complete/weaker”定义；Lemma 2.14 的 A/B 两操作。
- print 证据：原页图 p.046（页眉 folio 206）；300dpi 裁片显示 (2.9.15) 等式的三处求和上限均为 Greek ν。
- MinerU 差异：(2.9.15) 展开等式中的三个求和上限均录为 v，印刷为 ν。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：复查 lineality 空间恒等式 (2.9.15)；300dpi 原页确认三处上限均为 ν，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。(2.9.15) 三处求和上限的维数符号与印刷不符；其余已核交集次序、系统定义和 A/B 操作条件相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.047/88（印刷页 207）
- 时间：2026-10-01 16:50:14 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p047.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p047_minimal-domain.png`
- 核对：(2.9.16)–(2.9.17) lineality 条件；Lemma 2.14 积分归纳；§2.10 开头关于 Q(D)u 最小定义域的陈述。
- print 证据：原页图 p.047（页眉 folio 207）；300dpi 裁片明确显示 §2.10 该处为 `u∈D_{P_0}`。
- MinerU 差异：对应句在 Markdown 中用 bullet 作为 P 的下标；印刷为数字 0。
- 补充复核（2026-10-02 00:48:49 EDT；Peer-P33 | gpt-6-luna/max）：此前页签 PASS 未覆盖 §2.10 开头；300dpi 核验后当前 Grade 改为 FAIL。
- 结果：FAIL。最小域符号与印刷页不符；lineality 公式与积分推导相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.048/88（印刷页 208）
- 时间：2026-10-01 16:51:25 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- 300dpi 裁片：audit/300dpi/Hörmander_1955_pdo_p048_lineality-intersection-dimension.png
- PNG：`audit/Hörmander_1955_pdo_p048.png`（pngmono 150dpi）
- 核对：§2.10 平移/微分不变性与 Lq 比值；Lemma 2.15 多项式代数和 lineality 恒等式；§2.11 起始段。
- print 证据：原页图 p.048（页眉 folio 208）；300dpi 裁片确认 Lemma 2.15 lineality 恒等式的求和上限为 Greek ν。
- MinerU 差异：Lemma 2.15 证明中的求和上限录为 v，印刷为 ν。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：扩展维数符号复核时检查 p.048 的 Lemma 2.15；300dpi 原页确认求和上限为 ν，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。lineality 恒等式的求和上限与印刷不符；本页其他已核内容相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.049/88（印刷页 209）
- 时间：2026-10-01 16:51:56 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p049.png`（pngmono 150dpi）
- 核对：Theorem 2.19 条件与 (2.11.1)–(2.11.4)；缩放函数定义/极限；Theorem 2.20 及其推论。
- print 证据：原页图 p.049（页眉 folio 209；μ/ν 维数、ε 标度和带星求和可辨）。
- 结果：PASS。子空间条件、幂次标度、有限指标和以及连续逆结论与 Markdown 相符；未见内容级差异。

## PDF p.050/88（印刷页 210）
- 时间：2026-10-01 16:52:29 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p050.png`（pngmono 150dpi）
- 核对：CHAPTER III §3.0 标题与全节摘要；最大域/局部型算子结果；作者延后谱渐近研究的说明。
- print 证据：原页图 p.050（页眉 folio 210；章节标题、定义域包含关系、段落引用编号及文献号可辨）。
- 结果：PASS。术语、量词、阶数比较、章节编号和谱理论段落与 Markdown 相符；未见内容级差异。

## PDF p.051/88（印刷页 211）
- 时间：2026-10-01 16:53:02 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p051.png`（pngmono 150dpi）
- 核对：§3.1 起始；定义域估计 (3.1.1)；Theorem 3.1 两种情形；必要不等式 (3.1.2)、(3.1.3)、(3.1.4) 与 Lemma 3.1 陈述。
- print 证据：原页图 p.051（页眉 folio 211；复数 ζ、指数符号、k 阶导数和积分权重可辨）。
- 结果：PASS。域关系、常数项、指数衰减和多项式依赖陈述与 Markdown 相符；未见内容级差异。

## PDF p.052/88（印刷页 212）
- 时间：2026-10-01 16:53:33 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p052.png`（pngmono 150dpi）
- 核对：Lemma 3.1 resultant 证明与 (3.1.6)；Lemma 3.2 的 Lüroth 特例陈述及因式/可除性证明开头。
- print 证据：原页图 p.052（页眉 folio 212；ζ₁ 多项式展开、结果式因子积和 K⊂R⊂K[x] 环包含可辨）。
- 结果：PASS。次数指标、resultant 变量、系数非零条件、环包含关系与 Markdown 相符；未见内容级差异。

## PDF p.053/88（印刷页 213）
- 时间：2026-10-01 16:54:07 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p053.png`（pngmono 150dpi）
- 核对：Lemma 3.2 迭代除法证明收尾；Lemma 3.3.1 与 (3.1.7) 参数化；代数曲线论证及脚注 1。
- print 证据：原页图 p.053（页眉 folio 213；θ/η 函数递降、P=p(W)/Q=q(W) 参数式与 van der Waerden 脚注可辨）。
- 结果：PASS。多项式次数递减、参数代入关系、变量替换及脚注与 Markdown 相符；未见内容级差异。

## PDF p.054/88（印刷页 214）
- 时间：2026-10-01 16:54:36 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p054.png`（pngmono 150dpi）
- 核对：(3.1.8) 后情形 I/II；q′ 与 p′ 的重根论证；(3.1.9)–(3.1.11) 及多项式微分展开。
- print 证据：原页图 p.054（页眉 folio 214；绝对值平方差、重数条件、〈z₀,ζ〉代入与二项式系数可辨）。
- 结果：PASS。两情形条件、复变量/实向量角色、重数及公式指标与 Markdown 相符；未见内容级差异。

## PDF p.055/88（印刷页 215）
- 时间：2026-10-01 16:55:25 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p055.png`（pngmono 150dpi）
- 核对：Theorem 3.1 非实方向情形；(3.1.10)–(3.1.13)；q 重根函数 f(u)；指数加权积分不等式。
- print 证据：原页图 p.055（页眉 folio 215；实/复向量内积、k 阶导数零点重数和指数权可辨）。
- 结果：PASS。向量条件、二项式系数、q 导数次数、指数和不等式方向与 Markdown 相符；未见内容级差异。

## PDF p.056/88（印刷页 216）
- 时间：2026-10-01 16:56:13 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p056.png`（pngmono 150dpi）
- 核对：Theorem 3.1 证明收尾；uniform continuity Remark；§3.2 null-solution 定义与 Theorem 3.2；脚注 1。
- print 证据：原页图 p.056（页眉 folio 216；积分界、半空间条件、characteristic 符号和 Mychkis 脚注可辨）。
- 结果：PASS。指数权重与积分限、定义量词、唯一性引用和脚注与 Markdown 相符；未见内容级差异。

## PDF p.057/88（印刷页 217）
- 时间：2026-10-01 16:57:03 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p057.png`（pngmono 150dpi）
- 核对：Theorem 3.2 证明中的 Puiseux 展开、积分构造/收敛估计及半空间消失结论；Corollary 3.1。
- print 证据：原页图 p.057（页眉 folio 217；k/p 指数、求和起点、复指数支路和 ρ′ 权重可辨）。
- 结果：PASS。级数幂、积分路径、指数实部估计与推论方向和 Markdown 相符；未见内容级差异。

## PDF p.058/88（印刷页 218）
- 时间：2026-10-01 16:57:38 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p058.png`（pngmono 150dpi）
- 核对：§3.3 “local type” 问题背景；Definition 3.1 两种等价表述；Theorem 2.12 推论；Lemma 3.4 与脚注 1。
- print 证据：原页图 p.058（页眉 folio 218；D_P/D_{P_0} 边界、局部平方可积条件和闭包域说明可辨）。
- 结果：PASS。最大/最小域区分、局部性条件、紧子域映射及脚注与 Markdown 相符；未见内容级差异。

## PDF p.059/88（印刷页 219）
- 时间：2026-10-01 16:58:18 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p059.png`（pngmono 150dpi）
- 核对：(3.3.1)–(3.3.5)；指数权重界；Lemma 3.5 局部型估计；Lemma 3.6 的复平移增长条件。
- print 证据：原页图 p.059（页眉 folio 219；|Im ζ| 条件、δ 指数、Ω′/Ω 测度比及复 lineality 记号可辨）。
- 结果：PASS。域、范数、指数符号、增长模空间和公式编号与 Markdown 相符；未见内容级差异。

## PDF p.060/88（印刷页 220）
- 时间：2026-10-01 16:59:13 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p060.png`（pngmono 150dpi）
- 核对：Lemma 3.7 条件 (3.3.6)、平移比值极限 (3.3.7) 与 ε 估计；Lemma 3.8 陈述开头。
- print 证据：原页图 p.060（页眉 folio 220；η/ξ 范数范围、B+ε⁻¹ 截断和乘积零点因子可辨）。
- 结果：PASS。量词、范数阈值、乘积项和收敛比值与 Markdown 相符；未见内容级差异。

## PDF p.061/88（印刷页 221）
- 时间：2026-10-01 16:59:47 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p061.png`（pngmono 150dpi）
- 核对：Lemma 3.8 导数比值与 Taylor 展开；(3.3.8)–(3.3.10)；Theorem 3.3 等价条件 I–III。
- print 证据：原页图 p.061（页眉 folio 221；导数阶、平移和/系数抵消及 Λ(P) 模条件可辨）。
- 结果：PASS。导数指标、求和系数、比值极限及条件量词与 Markdown 相符；未见内容级差异。

## PDF p.062/88（印刷页 222）
- 时间：2026-10-01 17:00:29 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p062.png`（pngmono 150dpi）
- 核对：Theorem 3.3 条件 IV/V 与等价性证明；complete 情形说明；§3.4 基本解定义 (3.4.1)；Theorem 3.4 首项性质。
- print 证据：原页图 p.062（页眉 folio 222；IV 中 |η|≤A、V 的模 lineality 极限及 (x\ne0) 条件可辨）。
- 结果：PASS。五条件编号、uniformity 范围、分布卷积式与 Theorem 3.4 陈述和 Markdown 相符；未见内容级差异。

## PDF p.063/88（印刷页 223）
- 时间：2026-10-01 17:02:27 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p063.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p063_fourier-normalization.png`
- 核对：Theorem 3.4 性质 II 与 Remarks；基本解定义 (3.4.2)–(3.4.3)；复积分构造引入及实零点说明。
- print 证据：原页图 p.063 页眉 folio 223；300dpi 裁片显示 (3.4.2)、(3.4.3) 的归一化指数均为 −ν/2。
- MinerU 差异：(3.4.2) 指数录为 −v/2；(3.4.3) 的指数与印刷 ν 一致。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：全篇复读时重新对照 p.063 300dpi 裁片，发现 (3.4.2) 的 Markdown 指数为 v 而原页为 Greek ν；Grade 由 PASS 改为 FAIL。
- 结果：FAIL。(3.4.2) 的 Fourier 归一化指数维数符号与印刷不符；(3.4.3) 和本页其他已核定义相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.064/88（印刷页 224）
- 时间：2026-10-01 17:04:12 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p064.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p064_equations-3.4.5-6.png`
- 核对：路径分解公式 (3.4.4)；E=E₁+E₂ 分拆；(3.4.6) 两部分积分；E₂ 解析性、公式后的脚注 1；基本解恒等式。
- print 证据：原页图 p.064 页眉 folio 224；300dpi 裁片明确将 `E=E₁+E₂` 标为 (3.4.5)，将 E₁/E₂ 积分表达式标为 (3.4.6)；页底只见完整脚注 1，无独立 ξ 片段。
- MinerU 差异：Markdown 留有独立 `(3.4.5)` 行，却把 `E=E₁+E₂` 标为 `(3.4.6)`，随后两积分式又无该编号，导致公式编号错移；此外，脚注 1 前多出一条独立 docvortex `ξ` 碎片。
- 补充复核（2026-10-02 02:00:02 EDT；Peer-P33 | gpt-6-luna/max）：定位此前误记为 p.082 的孤立 `ξ` 后，按页面序列回到 p.064 核对；其 Markdown 碎片位于 (3.4.6) 后的脚注 1 前，p.064 原页无对应独立符号，Grade 维持 FAIL。
- 结果：FAIL。(3.4.5)–(3.4.6) 编号错移且脚注前多出孤立 ξ 碎片；本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.065/88（印刷页 225）
- 时间：2026-10-01 17:04:56 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p065.png`（pngmono 150dpi）
- 核对：E₂ 解析公式 (3.4.7)；卷积 Fourier 证据 (3.4.8)；Lemma 3.9 极小距离定义 (3.4.9) 与方程组 (3.4.10)。
- print 证据：原页图 p.065（页眉 folio 225；ν 归一化指数、|ξ|=R 区域、卷积支撑及变量距离条件可辨）。
- 结果：PASS。E₂ 积分域、(3.4.8) 积分下限、距离定义和 τ/b 渐近式与 Markdown 相符；未见内容级差异。

## PDF p.066/88（印刷页 226）
- 时间：2026-10-01 17:06:01 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p066.png`（pngmono 150dpi）
- 核对：Lemma 3.9 代数消元/ Puiseux 论证收尾；Lemma 3.10 距离下界；Lemma 3.11 导数估计 (3.4.11)；两条脚注。
- print 证据：原页图 p.066（页眉 folio 226；多项式等式组、ξ 距离指数 d、(k+j)! 与绝对值幂次可辨）。
- 结果：PASS。消元变量、指数、常数幂、导数阶数和脚注与 Markdown 相符；未见内容级差异。

## PDF p.067/88（印刷页 227）
- 时间：2026-10-01 17:06:40 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- 300dpi 裁片：audit/300dpi/Hörmander_1955_pdo_p067_fourier-normalization-3.4.15.png
- PNG：`audit/Hörmander_1955_pdo_p067.png`（pngmono 150dpi）
- 核对：Lemma 3.11 导数估计；(3.4.12) 根距界；导数项数；分布 (3.4.13)、阶数条件 (3.4.14) 与 (3.4.15) 积分分部项。
- print 证据：原页图 p.067（页眉 folio 227）；300dpi 裁片显示 (3.4.15) 的 Fourier 归一化因子为 (2π)^{-ν/2}。
- MinerU 差异：(3.4.15) 的归一化指数录为 −v/2，印刷为 −ν/2。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：扩展维数符号复核后检查 p.067 的 (3.4.15)；300dpi 原页确认指数为 Greek ν，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。(3.4.15) 的 Fourier 归一化指数与印刷不符；导数阶、因子计数、根距指数和分布定义相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.068/88（印刷页 228）
- 时间：2026-10-01 17:07:36 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p068.png`（pngmono 150dpi）
- 核对：(3.4.16) 边界项；积分核上界与 (b(l-j-r)-(k-j)>0)；连续函数 G 与估计 (3.4.17)；解析项 I 的 (3.4.18) 定义。
- print 证据：原页图 p.068（页眉 folio 228；求和上限 l−1、r,d 指数、球面边界项和 Fourier 常数可辨）。
- 结果：PASS。阶乘/二项式系数、幂次、求和范围及 (3.4.17) 与 Markdown 相符；未见内容级差异。

## PDF p.069/88（印刷页 229）
- 时间：2026-10-01 17:08:18 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p069.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p069_dimension-Rv.png`
- 核对：(3.4.19) 局部解析项估计；Theorem 3.5 向量空间维数与导数界 (3.4.20)；§3.5 证明开头。
- print 证据：原页图 p.069 页眉 folio 229；300dpi 裁片中向量 y 所属空间的维数上标为 Greek ν。
- MinerU 差异：Theorem 3.5 把该空间转录为 R^v。
- 补充复核（2026-10-02 00:50:26 EDT；Peer-P33 | gpt-6-luna/max）：此前 PASS 未识别上标差异；300dpi 对照后当前 Grade 改为 FAIL。
- 结果：FAIL。该维数符号与印刷 ν 不符；(3.4.19)–(3.4.20) 数值估计及 parametrix 文字相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.070/88（印刷页 230）
- 时间：2026-10-01 17:09:05 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p070.png`（pngmono 150dpi）
- 核对：(3.5.2)–(3.5.4) parametrix/convolution identities；local L² 推导；§3.6 与 Theorem 3.6 开头。
- print 证据：原页图 p.070（页眉 folio 230；Dirac 项、ω 的支撑、卷积分解和 P^k 域可辨）。
- 结果：PASS。卷积顺序、导数算子、支撑条件与 Theorem 3.6 量词和 Markdown 相符；未见内容级差异。

## PDF p.071/88（印刷页 231）
- 时间：2026-10-01 17:43:56 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- 300dpi 裁片：audit/300dpi/Hörmander_1955_pdo_p071_derivative-sum-dimension.png
- PNG：`audit/Hörmander_1955_pdo_p071.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p071_my-by.png`
- 核对：Theorem 3.6 证明与 Lemma 3.12 估计；Theorem 3.7 假设/闭图论证开头及指数解；“by means” 文字核验。
- print 证据：原页图 p.071 页眉 folio 231；两张 300dpi 裁片分别确认 “my means” 源级字形及导数求和范围的 Greek ν。
- 源级 print quirk：保留印刷原文 “my means”；MinerU Markdown 转录相同，不作更正。
- MinerU 差异：Theorem 3.7 证明中两处对空间坐标求和的上限录为 v，印刷为 ν。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：扩展维数符号复核时核对 Theorem 3.7 的两处求和；300dpi 原页确认上限均为 Greek ν，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。Theorem 3.7 证明中两处求和上限的维数符号与印刷不符；保留 “my means” 印刷原文，该文字并非 OCR 错误，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.072/88（印刷页 232）
- 时间：2026-10-01 17:59:17 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p072.png`（pngmono 150dpi）
- 核对：Theorem 3.7 证明收尾；Definition 3.2 与 (3.6.2)；Theorem 3.8 的 ρ(y) 定义 (3.6.3)；卷积表示 (3.6.4)–(3.6.5)。
- print 证据：原页图 p.072（页眉 folio 232；导数方向、Gamma 阶数、log 比值及卷积变量可辨）。
- 结果：PASS。上确界范围、逆指数定义、导数和积分变量及公式编号与 Markdown 相符；未见内容级差异。

## PDF p.073/88（印刷页 233）
- 时间：2026-10-01 18:32:15 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p073.png`（pngmono 150dpi）
- 核对：Theorem 3.8 证明收尾及 Gamma 界；null solution 增长估计 (3.6.6)–(3.6.7)；Remark；§3.7 / Lemma 3.13 开头。
- print 证据：原页图 p.073（页眉 folio 233；Γ(n/b)、α 指数、Taylor 估计和自伴算子条件可辨）。
- 结果：PASS。Gamma 参数、增长指数、泰勒项和 §3.7 条件与 Markdown 相符；未见内容级差异。

## PDF p.074/88（印刷页 234）
- 时间：2026-10-01 18:57:32 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p074.png`（pngmono 150dpi）
- 核对：Lemma 3.13 半有界性证明；自伴扩张与 Friedrichs 边界说明；谱分解 (3.7.1) 与 B∞ 函数算子 (3.7.2)。
- print 证据：原页图 p.074（页眉 folio 234；Parseval 符号、奇偶阶例外、扩张包含关系及谱积分式可辨）。
- 结果：PASS。正负界、算子包含、阶数条件和 B∞/谱积分记号与 Markdown 相符；未见内容级差异。

## PDF p.075/88（印刷页 235）
- 时间：2026-10-01 20:07:18 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p075.png`（pngmono 150dpi）
- 核对：Lemma 3.14 及 (3.7.3)–(3.7.7)；谱算子范数估计、点值表示、紧集/凸集条件。
- print 证据：原页图 p.075（页眉 folio 235；k 次谱乘子、varkappa、点值泛函及距离平方项可辨）。
- 结果：PASS。算子范数、谱函数、上确界域及距离估计与 Markdown 相符；未见内容级差异。

## PDF p.076/88（印刷页 236）
- 时间：2026-10-01 20:23:34 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- 300dpi 裁片：audit/300dpi/Hörmander_1955_pdo_p076_derivative-sum-dimension.png
- PNG：`audit/Hörmander_1955_pdo_p076.png`（pngmono 150dpi）
- 核对：谱核构造中 (3.7.8) 的内部正则估计、核定义 (3.7.9)、连续性 ε 论证与 B_k 集合说明。
- print 证据：原页图 p.076（页眉 folio 236）；300dpi 裁片确认 (3.7.8) 求和上限为 Greek ν。
- MinerU 差异：(3.7.8) 中导数平方和的求和上限录为 v，印刷为 ν。
- 补充复核（2026-10-02；Peer-P33 | gpt-6-luna/max）：扩展维数符号复核时检查 p.076 的 (3.7.8)；300dpi 原页确认上限为 ν，Grade 由 PASS 改为 FAIL。
- 结果：FAIL。(3.7.8) 的求和上限维数符号与印刷不符；核定义和连续性 ε 论证相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.077/88（印刷页 237）
- 时间：2026-10-01 20:32:41 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p077.png`（pngmono 150dpi）
- 核对：Theorem 3.9 连续核性质与 (3.7.10)–(3.7.12)；反线性共轭算子、(3.7.13)–(3.7.14) 和核光滑性推论。
- print 证据：原页图 p.077（页眉 folio 237；核积分次序、共轭位置、P′作用变量与 λ^n α 可辨）。
- 结果：PASS。积分变量、共轭核对称性、算子作用变量和谱参数幂次与 Markdown 相符；未见内容级差异。

## PDF p.078/88（印刷页 238）
- 时间：2026-10-01 20:43:05 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p078.png`（pngmono 150dpi）
- 核对：Theorem 3.10 光滑核与 (3.7.15) 两个积分；相关文献评述；§3.8 起始及展开式 (3.8.1)。
- print 证据：原页图 p.078（页眉 folio 238；Q(D)/Q(D′) 作用变量、积分变量 x/x′ 和 η 幂次可辨）。
- 结果：PASS。双积分对应变量、核光滑性陈述、引用和多项式展开与 Markdown 相符；未见内容级差异。

## PDF p.079/88（印刷页 239）
- 时间：2026-10-01 20:50:49 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p079.png`（pngmono 150dpi）
- 核对：§3.8 局部型算子必要条件；(3.8.1)–(3.8.2) 多项式展开；实系数情形下次数下降；Theorem 3.11 陈述开头。
- print 证据：原页图 p.079（页眉 folio 239；最高 t 次系数、p(η)=0 条件及 m−2/m−4 次数界可辨）。
- 结果：PASS。次数指标、线性部分、实值/半有界假设和 Theorem 3.11 参数与 Markdown 相符；未见内容级差异。

## PDF p.080/88（印刷页 240）
- 时间：2026-10-01 21:16:36 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p080.png`（pngmono 150dpi）
- 核对：Theorem 3.11 证明中的 (3.8.3)–(3.8.5)；导数展开、算术/几何均值界及指数和；定理后的闭合性质。
- print 证据：原页图 p.080（页眉 folio 240；2k 阶、(3.8.4) 求和上限、R 幂次和负指数界可辨）。
- 结果：PASS。次数、求和范围、系数和局部型条件证明与 Markdown 相符；未见内容级差异。

## PDF p.081/88（印刷页 241）
- 时间：2026-10-01 21:49:53 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p081.png`（pngmono 150dpi）
- 核对：Theorem 3.12；近似式 (3.9.1)–(3.9.2)；局部有限覆盖、分割统一、级数收敛与支持包含论证。
- print 证据：原页图 p.081（页眉 folio 241；ε/2^k 指数、范数两项及局部有限覆盖可辨）。
- 结果：PASS。闭包域结论、范数误差、索引范围和 L² 收敛说明与 Markdown 相符；未见内容级差异。

## PDF p.082/88（印刷页 242）
- 时间：2026-10-01 22:17:45 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p082.png`（pngmono 150dpi）
- 300dpi 裁片：`audit/300dpi/Hörmander_1955_pdo_p082_Rv-footnote.png`
- 核对：CHAPTER IV §4.0 引言；主类型/近似自伴约束及低阶项说明；§4.1 公式 (4.1.1) 与维数脚注 1。
- print 证据：原页图 p.082 页眉 folio 242；300dpi 脚注裁片显示 ambient space 上标为 Greek ν。
- MinerU 差异：印刷页只有脚注 “It is sufficient here to suppose that Ω is a domain in `R^\nu`.”；Markdown 的完整脚注将空间记作 `R^{\prime\prime}`，其前另有 `Ω` 和 `R^\nu` 两条 docvortex 碎片，原页无对应的独立内容。
- 补充复核（2026-10-02 02:06:15 EDT；Peer-P33 | gpt-6-luna/max）：页面边界复核确认先前提到的孤立 `ξ` 实际位于 p.064 的 (3.4.6) 后，并非 p.082；p.082 保留的发现为上述两条脚注碎片，Grade 维持 FAIL。
- 结果：FAIL。完整脚注维数符号有误且多出两条孤立碎片；本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.083/88（印刷页 243）
- 时间：2026-10-01 22:28:57 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p083.png`（pngmono 150dpi）
- 核对：(4.1.2) characteristic polynomial；对称多线性形式；张量 R/S 定义 (4.1.3)–(4.1.4) 及恒等式 (4.1.5)。
- print 证据：原页图 p.083（页眉 folio 243；j 求和范围、ζ/̅ζ 次数与对称张量指标可辨）。
- 结果：PASS。求和上下限、槽位次序、R−S 定义与核心张量恒等式和 Markdown 相符；未见内容级差异。

## PDF p.084/88（印刷页 244）
- 时间：2026-10-01 22:36:06 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p084.png`（pngmono 150dpi）
- 核对：§4.2 引言的空间维数符号；(4.1.6)–(4.1.7) 张量 Q 定义与恒等式；Theorem 4.1 假设、估计 (4.2.1) 及证明中的能量恒等式起始。
- print 证据：原页图 p.084（页眉 folio 244）；300dpi 裁片 `audit/300dpi/Hörmander_1955_pdo_p084_dimension-Rnu.png` 显示 §4.2 引言球邻域所在空间为 `R^\nu`。
- MinerU 差异：§4.2 引言将空间记号录为 `R^v`，与印刷的 `R^\nu` 不同。
- 补充复核（2026-10-02 01:13:13 EDT；Peer-P33 | gpt-6-luna/max）：此前页签 PASS 未覆盖 §4.2 引言维数；300dpi 裁片确认 Markdown `R^v` 与印刷 `R^\nu` 不同，Grade 改为 FAIL。
- 结果：FAIL。§4.2 引言的空间维数记号与印刷原文不符；本页张量定义、求和范围及 Theorem 4.1 已核假设和估计相符，本页所列差异已由下方修复登记中的独立 fix(md) 提交修正；FAIL 保留为修复前 MinerU 等级。

## PDF p.085/88（印刷页 245）
- 时间：2026-10-01 22:51:01 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p085.png`（pngmono 150dpi）
- 核对：Theorem 4.1 能量恒等式 (4.2.2)；阶数范数定义 (4.2.3)；积分估计 (4.2.4)–(4.2.7)。
- print 证据：原页图 p.085（页眉 folio 245；m−1 阶范数、δ 因子、R/S 张量和求和上下限可辨）。
- 结果：PASS。微分阶、范数类型、估计常数和各式符号与 Markdown 相符；未见内容级差异。

## PDF p.086/88（印刷页 246）
- 时间：2026-10-01 23:14:39 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p086.png`（pngmono 150dpi）
- 核对：Theorem 4.1 证明中的 (4.2.8)–(4.2.13)；Q/G 张量散度项、范数阶估计及小邻域闭合条件。
- print 证据：原页图 p.086（页眉 folio 246；1/i 因子、导数阶 m−2/m−1、δ 收缩和 Kδ 条件可辨）。
- 结果：PASS。分部积分项、范数阶、常数因子和 (4.2.13) 与 Markdown 相符；未见内容级差异。

## PDF p.087/88（印刷页 247）
- 时间：2026-10-01 23:30:54 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p087.png`（pngmono 150dpi）
- 核对：Theorem 4.1 余论；References [1]–[16] 的作者、题名、期刊/丛书、卷期、年份、页码与语言标注。
- print 证据：原页图 p.087（页眉 folio 247；全页文献 1–16 可读）。
- 结果：PASS。参考文献字段与印刷目录逐条相符；保留了原拼写、缩写、变音及印刷标点，未见 MinerU 差异。

## PDF p.088/88（印刷页 248）
- 时间：2026-10-02 00:14:55 EDT
- actor：Peer-P33；model：gpt-6-luna；effort：max
- PNG：`audit/Hörmander_1955_pdo_p088.png`（pngmono 150dpi）
- 核对：References [17]–[35] 的作者、题名、期刊/丛书、卷期、年份、页码与语言标注。
- print 证据：原页图 p.088（印刷 folio 248；参考文献 17–35 全页可读）。
- 结果：PASS。各条目与 MinerU Markdown 对应段落相符；保留原文变音、大小写、期刊缩写和印刷拼写，未见差异。

## 修复登记

- 时间：2026-10-02
- actor：Peer-P33；model：gpt-6-luna；reasoning effort：max
- 修复提交：c00640af36398df482ebb49a05ffde9fde3a4ec3（独立 fix(md) 提交，仅含 MinerU Markdown）。
- 原始 MinerU 文件来源：commit a33f22f3b0bcf430149ea06d98e65076266acc9e；该提交中文件 SHA-256 为 d90b7c0ee62dd38415d5146d9f5f59cdf584c3df9a5f3f34e68c90ba518199ba。
- 修复前候选文件 SHA-256：3f7e2eca60efe9a73c1b6488c6bd746ee2b7d4f9bb403716eda8d7ecc96bf51a。它与原始导出仅有末尾换行差异；该字节差异来自保留既有 restore commit，不涉及内容改写。
- 修复后文件 SHA-256：c806c7f4f92962c70fbfc3846d7e82d01575ae6cff2d26db5f7b25a3173595e0。
- 修复方式与范围：以 apply_patch 对目标 Markdown 逐个位置手工修订，共 53 处，分布于 PDF p.007(5)、p.010(7)、p.011(6)、p.014(1)、p.016(1)、p.017(1)、p.022(1)、p.026(1)、p.027(1)、p.029(1)、p.031(5)、p.033(1)、p.043(1)、p.045(2)、p.046(3)、p.047(1)、p.048(1)、p.063(1)、p.064(4)、p.067(1)、p.069(1)、p.071(2)、p.076(1)、p.082(3)、p.084(1)。
- 最终复核：手工完整复读修复后的 3,515 行 Markdown；逐处将新增修复对照本文件所列印刷页证据，随后执行只读符号残余检索、引用文件存在性核验、PDF 页数核验及 git diff --check。PDF 为 88 页，页面图 88 张，300dpi 裁片 33 张，121 个引用路径全部存在。
- 历史边界：commit 9dde4136 曾把 p.064 审计与 Markdown 修改混在同一提交；随后由 additive restore commit 256d9319 恢复原始 OCR 内容，未改写历史。本次最终 Markdown 修复由上列独立提交完成。
- 集成状态：本记录与修复提交仍属 Peer-P33 候选；未更新根级 AUDIT-INDEX.md、AUDIT-PROGRESS.log，也未集成或 push。
