# 逐页审计：Werner_2001_lsw_conformal_invariance

## 审计元数据

- Actor：Peer-P31
- Model：gpt-6-luna
- Reasoning effort：max
- Role：CONTRIBUTOR；本文件与提交仍是候选，待 Master 按 exact OID 复核集成。
- 任务基线：`037602429d3b009f6fc468c732073eb3ddf9875f`（本 worktree 为该提交的 detached HEAD）。任务启动后 canonical `main` 前进至 `e864b3b9dffc3456435c4bd5d0cd7553b3cd4cb8`；核对范围内本篇 PDF、MinerU Markdown 与 `AUDIT-INDEX.md` 登记相对任务基线均无差异。
- 源 PDF：`2006年 - Werner/Werner_2001_lsw_conformal_invariance.pdf`；72 个 PDF 页面，印刷页码 1–72。
- PDF SHA-256：`58038a74579c28d16e2d5265b2a0881b88f91c3dbdf27ad0ab0f1e802a71f7a4`
- 唯一被审 MinerU Markdown：`2006年 - Werner/Werner_2001_lsw_conformal_invariance_mineru/Werner_2001_lsw_conformal_invariance__Werner_2001_lsw_conformal_invariance.md`
- 审计开始时 Markdown SHA-256：`72205f59de7fe8e03bd6492cde34adf550eb3ce44555c787f23b7f6416e41ec9`
- PDF 类型：born digital；Creator 为 `LaTeX with hyperref package`，Producer 为 `dvips + GPL Ghostscript GIT PRERELEASE 9.22`。`pdftotext` 提取 146,401 个字符、72 个分页、0 个 U+FFFD；以完整文本层逐页对账为主，题录页与密集数学页抽样目检，文本层有损或疑点回到源页图像 / 300dpi 裁片。
- MinerU 本地结构元数据记录 producer `mineru`、version `3.4.4`；可用本地导出中没有 `doc_id` 字段。

## 逐页记录

## p.001（PDF p.1 / 印刷 p.1）
- 时间：2026-10-01 16:12 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p001.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p001_affiliation.png`（源页 pnggray 300dpi 裁片）；PDF p.1 文本层；Markdown 题名、作者、摘要及页脚注块。
- 核对：题名、作者次序、摘要和印刷页码；PDF p.1 的脚注机构与支持信息。
- 结果：PASS±。题名、作者及摘要内容相符。印刷页脚注为 “Mittag-Leffler Institute” 和 “Université Paris-Sud and IUF”；MinerU 分别写作 “Mittag-Lefler Institute”（少一个 `f`）与 `Universit´e`（重音字符拆裂）。300dpi 裁片确认印刷字形为 “Leffler” 和 “Université”。两处列入全篇审计后的逐处修复清单。

## p.002（PDF p.2 / 印刷 p.2）
- 时间：2026-10-01 16:14 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p002.png`（pngmono 150dpi）；PDF p.2 文本层；Markdown 目录区（Contents 至 Bibliography）。
- 核对：目录各节标题、编号与所列印刷页码。
- 结果：PASS±。目录项目和页码与 PDF 文本层一致；MinerU 未保留该页底部单独印刷页码 `2`，属页脚编号缺失，不改变目录信息。

## p.003（PDF p.3 / 印刷 p.3）
- 时间：2026-10-01 16:15 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p003.png`（pngmono 150dpi）；PDF p.3 完整文本层；MinerU `structured_content.json` page_idx=2 与 Markdown 对应段落。
- 核对：引言开头、§1.1 两段及 §1.2 首段至印刷页末；核对数学记号 `\\mathbb{R}^d` 与行末断词衔接。
- 结果：PASS±。段落内容与 PDF 文本层对齐；PDF 印作 “Loewner’s differential equation”，Markdown 写作 “Loewner’s diferential equation”（少一个 `f`），列入逐处修复清单。印刷页脚页码 `3` 未保留在 Markdown；页末 `sto-` 与下一页续字合并不影响词义。

## p.004（PDF p.4 / 印刷 p.4）
- 时间：2026-10-01 16:17 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p004.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p004_Haeg95.png`（源页 pnggray 300dpi 裁片）；PDF p.4 文本层；MinerU page_idx=3 与 Markdown 对应段落。
- 核对：§1.2 后续两段、§1.3 开头与正文首段；核对 `sufficient` 拼写和 [Häg95] 引文键。
- 结果：PASS±。段落内容与印刷文本层对齐；Markdown 将 “sufficient” 写为 “suficient”（少一个 `f`），并将 [Häg95] 写为 `[H¨ag95]`（分音符错置）。300dpi 裁片确认印刷为 [Häg95]。两处列入逐处修复清单。印刷页脚页码 `4` 未保留。

## p.005（PDF p.5 / 印刷 p.5）
- 时间：2026-10-01 16:17 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p005.png`（pngmono 150dpi）；PDF p.5 文本层与源页图；MinerU page_idx=4、Markdown 中 loop-erasure 定义及 Wilson 算法段。
- 核对：Figure 1.1 题注、loop-erasure 递推式、UST 定义与 Wilson 算法；核对公式末尾括号/标点及参考文献指引。
- 结果：PASS±。递推式与段落信息相符；Wilson 算法句中印刷为 `T_n = T_{n-1}.) Then`，Markdown 写作 `$T_n = T_{n-1} . . )$Then`，出现重复句点且把右括号并入数学区，列入逐处修复清单。Figure 1.1 题注对应本页印刷图；印刷页脚页码 `5` 未保留。

## p.006（PDF p.6 / 印刷 p.6）
- 时间：2026-10-01 16:21 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p006.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p006_Hoelder.png` 与 `_p006_subset.png`（源页 pnggray 300dpi 裁片）；PDF p.6 文本层；MinerU page_idx=5 与 Markdown §1.3–§1.4 段落。
- 核对：Kenyon 与 UST scaling-limit 段落、§1.4 的 Loewner/SLE 描述、`κ` 条件、路径映射符号及脚注页码。
- 结果：PASS±。数学叙述和公式与印刷页对齐；Markdown 将 “differential” 写作 “diferential”（少一个 `f`），将 “Hölder” 写作 `H¨older`（分音符错置），列入逐处修复清单。文本层把 `D ⊊ C` 的关系符抽取为 `$`；300dpi 裁片确认印刷为 `D ⊊ C`，Markdown 的 `\subsetneq` 与原文相符。印刷页脚页码 `6` 未保留。

## p.007（PDF p.7 / 印刷 p.7）
- 时间：2026-10-01 16:22 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p007.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p007_subset.png`（源页 pnggray 300dpi 裁片）；PDF p.7 文本层与题录/定理页视觉检查；MinerU page_idx=6 与 Markdown §1.5。
- 核对：Figure 1.2 题注；§1.5 首段、path metric 定义、Theorem 1.1 陈述与后续推论；核对域包含关系符号。
- 结果：PASS±。题注、路径度量、Theorem 1.1 及说明与印刷页相符。文本层在 `D ⊊ C` 处丢失包含关系符号（抽取为 `$`）；150dpi 整页和 300dpi 裁片确认原印刷为 `D ⊊ C`，Markdown 的 `\subsetneq` 保真。印刷页脚页码 `7` 未保留。

## p.008（PDF p.8 / 印刷 p.8）
- 时间：2026-10-01 16:25 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p008.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p008_bijection.png`（源页 pnggray 300dpi 裁片）；PDF p.8 完整文本层；MinerU page_idx=7 与 Markdown 的 Corollary 1.2、Peano curve 定义段。
- 核对：free/wired UST 定义、Corollary 1.2、topologist’s sine curve、primal/dual graph 对应关系与 Peano-path 构造。
- 结果：FAIL。印刷明确写有 “a bijection `e ↔ e†` between the edges of G and those of G†”；MinerU Markdown 把关系箭头漏掉，只剩 `e e†`，使该数学关系不完整。300dpi 裁片确认印刷箭头为双向箭头；列入全篇结束后的逐处修复。另有非数学拼写瑕疵：PDF “different”，Markdown “diferent”（少一个 `f`），一并列入修复清单。文本层在 `D ⊊ C` 处未提取出包含符号，150dpi 原页确认 Markdown 记为 `D ⊊ C`，与印刷一致；Corollary 中 `D ⊂ C` 也与原文一致。印刷页脚页码 `8` 未保留。

## p.009（PDF p.9 / 印刷 p.9）
- 时间：2026-10-01 16:26 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p009.png`（pngmono 150dpi）；PDF p.9 完整文本层；MinerU page_idx=8 与 Markdown Figure 1.3 图像引用及题注。
- 核对：Figure 1.3 题注与图像；Peano path 结束定义、Manhattan lattice 描述、wired/free UST 讨论及 §1.5 末段开头。
- 结果：PASS±。正文、符号与页末段落和 PDF 文本层一致；Markdown 对应的 `images/page_8_image_0.jpg` 存在且显示图、对偶图、树、对偶树与 Peano 曲线，和本页 Figure 1.3 相符。印刷页脚页码 `9` 未保留。

## p.010（PDF p.10 / 印刷 p.10）
- 时间：2026-10-01 16:27 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p010.png`（pngmono 150dpi）；PDF p.10 文本层与源页目检；MinerU page_idx=9 与 Markdown 的 Figure 1.4 图像、题注、Theorem 1.3 段。
- 核对：Figure 1.4 图及题注、UST Peano path 标度极限 Theorem 1.3、后续 SLE_8 生成路径说明与弱收敛句。
- 结果：FAIL。PDF 图题写明 “chordal SLE₈”，但 MinerU Figure 1.4 题注只写 “chordal SLE .”，漏掉下标 `8`，与该页原文不符；原图与 PDF 文本层均确认该下标。列入全篇结束后的逐处修复。另有排版级伪影：Markdown 把 `metric ρ.` 录成 `metric ρ..`，重复句点，列入修复清单。Figure 1.4 图像引用存在且与该页印刷图一致。印刷页脚页码 `10` 未保留。

## p.011（PDF p.11 / 印刷 p.11）
- 时间：2026-10-01 16:29 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p011.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p011_interval.png`（源页 pnggray 300dpi 裁片）；PDF p.11 完整文本层；MinerU page_idx=10 与 Markdown §1.5 后段。
- 核对：FK 参数域与 κ(q) 公式、`κ(0)=8` 结论、`16/κ(0)=2` 关系、反射随机游走描述和 §1.6 开头。
- 结果：FAIL。原文参数范围为 `q ∈ (0,4)`；MinerU 写为 `$q \in \mathsf { \Gamma } ( 0 , 4 )$`，把开区间左括号误识别成希腊大写字母 `Γ`，改变了数学参数域。300dpi 裁片确认印刷为 `(0,4)`。还记录两处正文差异供全篇结束后的修复：`κ(0)=8` 后 Markdown 含 U+0000/U+0001，而印刷仅为空格；印刷为 “reflected off β”，Markdown 写作 “reflected of β”（少一个 `f`）。印刷页脚页码 `11` 未保留。

## p.012（PDF p.12 / 印刷 p.12）
- 时间：2026-10-01 16:30 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p012.png`（pngmono 150dpi）；PDF p.12 文本层；MinerU page_idx=11 与 Markdown §1.6 对应段落。
- 核对：前页 §1.6 续文、两部分证明概述、Markov 性质描述及 observable / hitting-probability 段落。
- 结果：PASS±。本页陈述、符号与 PDF 文本层一致；Markdown 将 “difficult” 写作 “dificult”（少一个 `f`），列入逐处修复清单。页末句跨到下一页；印刷页脚页码 `12` 未保留。

## p.013（PDF p.13 / 印刷 p.13）
- 时间：2026-10-01 16:32 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p013.png`（pngmono 150dpi）；PDF p.13 文本层与源页图；MinerU page_idx=12 与 Markdown 的 Theorem 1.3 解释段、martingale 句及 LERW observable 段。
- 核对：observable 论述；条件概率过程的 martingale 陈述；相应的估计句；LERW 反射随机游走描述。
- 结果：FAIL。印刷把 “martingale” 在行末断为 `mar-` / `tingale`，并写明 `P[A] is estimated`；MinerU 在这些位置插入 form-feed / ETX 控制码，且在 `P[A]` 后多出连字符，造成关键概率句转写污染。150dpi 原页确认印刷无这些字符。列入逐处手工修复清单。另有两处文字差异：印刷 “different observable” 与 “reflected off β”，Markdown 分别写为 “diferent observable” 和 “reflected of β”；列入修复清单。印刷页脚页码 `13` 未保留。

## p.014（PDF p.14 / 印刷 p.14）
- 时间：2026-10-01 16:33 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p014.png`（pngmono 150dpi）；PDF p.14 完整文本层及源页；MinerU page_idx=13 与 Markdown §1.6 末段、§2 和 §2.1 开头。
- 核对：随机游走配对与 Brownian motion 的说明；Preliminaries 所需背景；Loewner/SLE 开头定义和 `D ⊊ C`。
- 结果：PASS±。段落与公式总体吻合。Markdown 将 “different fields” 写作 “diferent fields”、将 “suffices” 写作 “sufices”，并在 `(X,Y)` 后插入印刷中不存在的 `•`；均列入逐处修复清单。PDF 文本层未提取 `D ⊊ C` 的关系符，150dpi 原页确认该符号，Markdown 中的 `D ⊊ C` 与印刷相符。印刷页脚页码 `14` 未保留。

## p.015（PDF p.15 / 印刷 p.15）
- 时间：2026-10-01 16:36 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p015.png`（pngmono 150dpi）；PDF p.15 文本层及整页数学式目检；MinerU page_idx=14 与 Markdown capacity 定义、Loewner 方程 (2.1)/(2.2) 段。
- 核对：圆盘归一化映射、capacity 参数化、驱动函数 `W(t)` 定义、Loewner 方程分子/分母与负号、初始条件、hull 定义及 `\overline{U}` 量词。
- 结果：PASS±。数学公式 (2.1)/(2.2)、变量与编号均与印刷页相符。文本层漏掉量词 `z ∈ \overline{U}` 的 overline，150dpi 源页确认印刷有 overline 且 Markdown 保留。Markdown 有 “differential”→“diferential”与 “sufficient”→“suficient”两处少一个 `f` 的文字误差，列入逐处修复清单。印刷页脚页码 `15` 未保留。

## p.016（PDF p.16 / 印刷 p.16）
- 时间：2026-10-01 16:36 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p016.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p016_capacity.png`（源页 pnggray 300dpi 裁片）；PDF p.16 文本层与整页 Loewner 方程视觉核对；MinerU page_idx=15 与 Markdown 径向/弦向 Loewner 描述。
- 核对：径向 SLE 驱动函数、域内重参数化、upper-half-plane hydrodynamic normalization、`z → ∞`、capacity-from-infinity 定义及方程 (2.3)/(2.4)。
- 结果：FAIL。印刷写明 “where `z → ∞` in H”，MinerU 写成 `z ∞`，丢失趋向箭头；印刷映射为 `g: H minus K → H`，MinerU 的映射关系中丢失 `→`；capacity 定义印为 `lim_{z→∞}(g_t(z)-z)z/2`，MinerU 把 `lim` 与下标箭头转写成 `lim ℓ_{z ∞}`。300dpi 裁片确认 capacity 极限式。另记一处非打印字符：径向驱动函数段末的 Brownian-motion 句号后，Markdown 插入 NUL/SOH 后才接 “Often”；150dpi 原页显示为普通句间间隔。上述差异会影响定义与阅读，列入全篇修复清单。印刷页脚页码 `16` 未保留。

## p.017（PDF p.17 / 印刷 p.17）
- 时间：2026-10-01 16:39 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p017.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p017_domain.png`、`_p017_bounds.png`（源页 pnggray 300dpi 裁片）；PDF p.17 文本层；MinerU page_idx=16 与 Markdown hull 定义及 Lemma 2.1 证明。
- 核对：chordal hull 域/映射、Lemma 2.1 的 k(t) 与直径界、upper-bound 证明中的 z/t/K_t 记号和印刷断句。
- 结果：FAIL。印刷为 `g_t: H minus K_t → H`，Markdown 映射关系丢失 `→`；印刷不等式含 `|z-W(0)| ≥ 4δ`、`t ≤ δ²` 和 `z ∉ K_t`，Markdown 分别加入 z 上点、≤ 上点及 K_t 上点，300dpi bounds 裁片确认印刷均无这些点。目标转写还把 “differential” 写成 “diferential”，并把 “sufficient/suffices” 写成 “suficient/sufices”，列入逐处修复。印刷与 Markdown 均为碰撞项 `W(z)`，按印刷原文记录，不按预期记号改写。PDF 文本层把 `z ∈ overline H` 的 overline 抽掉，300dpi/domain 裁片确认 Markdown 保留了该 overline。印刷页脚页码 `17` 未保留。

## p.018（PDF p.18 / 印刷 p.18）
- 时间：2026-10-01 16:40 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p018.png`（pngmono 150dpi）；PDF p.18 文本层与整页 harmonic-measure 公式目检；MinerU page_idx=17 与 Markdown 的 lower-bound 计算及 §2.2 开头。
- 核对：capacity/harmonic-measure 等式、`diam K_t < 1/10` 前提、`A_t` 集合定义、单调性与直径上界证明；核对 grid-domain inner-radius 定义。
- 结果：FAIL。印刷前提写作 `diam K_t ≤ 1/10, we have`；MinerU 在该界后多出 `R`（`≤ 1/10 R`），改变了该推导条件，150dpi 原页确认无 `R`。还记录文字/排版瑕疵：两处 “suffices” 被写作 “sufices”，且 “for all s ≤ t,” 被写作 `s ≤ t_:`；列入逐处修复清单。`A_t` 定义中的 `overline U` 与内半径公式均与印刷相符。印刷页脚页码 `18` 未保留。

## p.019（PDF p.19 / 印刷 p.19）
- 时间：2026-10-01 16:43 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p019.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p019_domainclass.png`（源页 pnggray 300dpi 裁片）；PDF p.19 文本层及源页目检；MinerU page_idx=18 与 Markdown Proposition 2.2。
- 核对：V∂(D) 的定义、z → v 边界极限、harmonic-measure 比值 λ、ε → 0 关系、Proposition 2.2 不等式。
- 结果：FAIL。印刷中的 `z → v` 与 `ε → 0` 两个极限/趋向箭头在 MinerU Markdown 中均丢失；300dpi 裁片还确认印刷的域族符号为 script D，Markdown 写成 Fraktur D。上述定义和参数关系需要按印刷逐处恢复。另有文本差异：印刷为 “a random walk first exits D at v”，Markdown 写作 “first exists D at v”；“suffices” 也写为 “sufices”。印刷与 Markdown 都保留了源文用词 “not loose anything”，记录为源级原文，不擅自改正。印刷页脚页码 `19` 未保留。

## p.020（PDF p.20 / 印刷 p.20）
- 时间：2026-10-01 16:44 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p020.png`（pngmono 150dpi）；PDF p.20 文本层与源页视觉核对；MinerU page_idx=19 与 Markdown Lemma 3.1、过程定义及 Lemma 3.2 条目。
- 核对：LERW reversal 命题、条件退出事件、Γ/γ 路径分解、n_j/Γ_j 定义与 Markovian property 前两条。
- 结果：PASS±。命题、路径下标和两条条件分布陈述与印刷相符；PDF “time-reversal of β” 在 MinerU Markdown 中写成数学区内 `o f β`，仅有内部空格/格式瑕疵，列入逐处修复清单。印刷页脚页码 `20` 未保留。

## p.021（PDF p.21 / 印刷 p.21）
- 时间：2026-10-01 16:48 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p021.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p021_driving.png`（源页 pnggray 300dpi 裁片）；PDF p.21 文本层与整页目检；MinerU page_idx=20 与 Markdown Lemma 3.2/3.3 及 §3.2 开头。
- 核对：Lemma 3.2 clause 3 与 proof 收尾、Lemma 3.3 的条件期望、驱动角 ϑ(t) 与 W(t) 的表示。
- 结果：FAIL。印刷关系为 `W(t)=W(0) exp(iϑ(t))`，MinerU 写成 `W(t)=dot W(0) exp(iϑ(t))`；300dpi 裁片确认是 `W(0)`，不是时间导数。Markdown 还在 ϑ 参数句中插入 NUL/SOH，在 “strong Markov property” 中插入 backspace，并在 Lemma 3.3 的条件句结尾混入连字符/ETX；150dpi 原页均无这些字符。Lemma 3.1 的 “time-reversal of β” 被排成 `o f β`，列入轻微排版修复。印刷页脚页码 `21` 未保留。

## p.022（PDF p.22 / 印刷 p.22）
- 时间：2026-10-01 16:50 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p022.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p022_bounds.png`（源页 pnggray 300dpi 裁片）；PDF p.22 文本层与 Proposition 3.4 公式目检；MinerU page_idx=21 与 Markdown Proposition 3.4 / proof sketch。
- 核对：停时 m 定义、概率事件、(3.1)–(3.4) 四个公式、(3.3) 半径范围与论证正文。
- 结果：FAIL。印刷事件写作 `P[γ₀=u₀]`，Markdown 将方括号误识别为 `\lceil ... \rceil`（ceiling）；(3.3) 印刷界为 `rad₀(D)/200 < |v| < rad₀(D)/5`，Markdown 将 `rad₀` 识成 `rad l₀` 并把 `200` 拆成 `2 0 0`。300dpi 裁片确认以上印刷记号；这些差异改变概率事件或半径范围，列入全篇逐处修复。另有 “obtained by” 前插入连字符/ETX、停时式的 `or` 被分裂、 “different/sufficient” 拼写丢 `f` 与 “rough geometry” 多出 `S` 等转写瑕疵。域族符号在本页印刷为 script D，Markdown 使用 Fraktur D；一并列入记号修复。印刷页脚页码 `22` 未保留。

## p.023（PDF p.23 / 印刷 p.23）
- 时间：2026-10-01 16:52 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p023.png`（pngmono 150dpi）；PDF p.23 文本层与 Lemma 3.5/Proposition 3.4 证明页目检；MinerU page_idx=22 与 Markdown 证明草图、(3.5)/(3.6) 及 h_j^+ 求和式。
- 核对：rough geometry 文字、Green’s-function bounds (3.5)/(3.6)、径向条件及 Proposition 3.4 证明中的角度/时间增量和 visits 求和定义。
- 结果：PASS±。公式、常数、下标与印刷页相符。Markdown 把 “rough geometry of γ” 写成 “rough Sgeometry of γ”，并把印刷的 “rough-geometry of D” 写成多一条连字符且夹有控制字符的文本；另有 “different/sufficient” 漏 `f` 的拼写差异，均列入逐处修复。印刷页脚页码 `23` 未保留。

## p.024（PDF p.24 / 印刷 p.24）
- 时间：2026-10-01 16:53 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p024.png`（pngmono 150dpi）；PDF p.24 文本层；MinerU page_idx=23 与 Markdown 的条件期望等式 (3.7)–(3.9)、λ 差值式 (3.10) 与 Z_j 展开式 (3.11)。
- 核对：E[h_j^+ | γ[0,j]]、求和望远镜关系、条件期望近似、Green’s function 递推和 Loewner 展开误差项。
- 结果：PASS±。公式系数、下标、绝对值及编号 (3.7)–(3.11) 与 PDF 一致。Markdown 把 “sufficiently/different” 分别少一个 `f`，并在 “We freely use this shorthand below” 前插入多余连字符和控制字符；均列入逐处修复。印刷页脚页码 `24` 未保留。

## p.025（PDF p.25 / 印刷 p.25）
- 时间：2026-10-01 16:54 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p025.png`（pngmono 150dpi）；PDF p.25 文本层与关键不等式/展开式整页目检；MinerU page_idx=24 与 Markdown Proposition 3.4 证明续段。
- 核对：Koebe 1/4 theorem 的半径包含式、(3.12) 期望估计、(3.7)/(3.8)/(3.9) 的后续比较及 Taylor 展开前提。
- 结果：FAIL。印刷包含式末项为 `(rad₀(D)/5)U`；MinerU 写成 `(rad₀(D)/overline{5})U`，给普通数字 `5` 添加横线。150dpi 源页清楚确认 `5` 上无横线，公式记号需按印刷修复。另有 “sufficiently/different” 漏 `f` 的文字差异，列入逐处修复清单。印刷页脚页码 `25` 未保留。

## p.026（PDF p.26 / 印刷 p.26）
- 时间：2026-10-01 16:56 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p026.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p026_taylor.png`（源页 pnggray 300dpi 裁片）；PDF p.26 文本层；MinerU page_idx=25 与 Markdown Taylor 展开、(3.13) 和两个试探顶点构造。
- 核对：(3.13) 两项系数与期望、Taylor 展开的变量 `Z_m−Z`、`U/30` 与 `iU/30` 试探点、参数范围 `R∈(0,1)`。
- 结果：FAIL。印刷 Taylor 展开变量为 `Z_m−Z`，MinerU 多出下标 `i`（`Z_m−Z_i`）；印刷试探点为 `U/30` 与 `iU/30`，Markdown 将 `30` 拆写为 `3 0`；印刷范围为 `R∈(0,1)`，Markdown 把左括号误识别成 `Γ`。300dpi 裁片确认 `Z_m−Z` 与 `U/30`。这些偏差改变 Taylor 变量、数值和参数域，列入全篇修复。式 (3.13) 其余系数/幂次与印刷一致；另有 “different” 少一个 `f` 的文字瑕疵。印刷页脚页码 `26` 未保留。

## p.027（PDF p.27 / 印刷 p.27）
- 时间：2026-10-01 16:57 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p027.png`（pngmono 150dpi）；PDF p.27 文本层；MinerU page_idx=26 与 Markdown Remark 3.6 末尾、Theorem 3.7 及 Lemma 3.8 开头。
- 核对：Radon–Nikodym martingale 收尾、Theorem 3.7 概率界与 Brownian time scaling `B(2t)`、Skorokhod embedding 引入。
- 结果：PASS±。公式、量词与定理内容和 PDF 文本层一致；Markdown 将 “a coupling of γ”/“If” 的字符分隔为 `o f`/`I f`，只影响排版阅读，列入修复清单。印刷页脚页码 `27` 未保留。

## p.028（PDF p.28 / 印刷 p.28）
- 时间：2026-10-01 16:58 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p028.png`（pngmono 150dpi）；PDF p.28 文本层与 (3.14)–(3.16) 及时间界整页目检；MinerU page_idx=27 与 Markdown Lemma 3.8 / Theorem 3.7 proof。
- 核对：Skorokhod stopping-time identities (3.14)/(3.15)、r₁ 的选择、N 的上取整值、t_N 容量界与条件增量 (3.16)。
- 结果：PASS±。条件期望、停止时间、N 与容量界在数学含义上和原文相符。MinerU 将印刷的 `20T`、`10T` 及 `20T` 分别写为 `2 0 T`、`1 0 T`、`2 0 T`，并将 “If” 分成 `I f`；这些空格与拆字影响公式可读性，列入逐处修复。印刷页脚页码 `28` 未保留。

## p.029（PDF p.29 / 印刷 p.29）
- 时间：2026-10-01 17:00 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p029.png`（pngmono 150dpi）；PDF p.29 文本层与 (3.17)–(3.20) 公式页目检；MinerU page_idx=28 与 Markdown martingale 差分、Brownian stopping-time 界及 Y_n/Z_n 定义。
- 核对：条件二阶矩、martingale 差分、(3.19)/(3.20) 上界、Y_n 的平方增量与 Z_n 定义。
- 结果：FAIL。印刷定义 `Y_n` 接近 `2 t_{m_n}`；MinerU Markdown 写作 `2 : t_{m_n}`，插入冒号改变了该乘法系数与容量项的关系。150dpi 原页确认印刷为 `2 t_{m_n}`。其余可见的条件期望、下标、幂次和编号 (3.17)–(3.20) 与印刷相符；印刷页脚页码 `29` 未保留。

## p.030（PDF p.30 / 印刷 p.30）
- 时间：2026-10-01 17:01 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p030.png`（pngmono 150dpi）；PDF p.30 完整文本层与 (3.21)/(3.22) 概率界整页目检；MinerU page_idx=29 与 Markdown Z′_n 补偿和平方矩估计段。
- 核对：Z′_n 的定义、martingale 性质、E[Z′_N²] 累积界、Doob 界及 (3.21)/(3.22) 的事件阈值。
- 结果：FAIL。印刷定义 `Z′_n = Z_n − Σ E[Z_j−Z_{j−1} | F_{j−1}]` 并随后称其为 `F_n`-martingale；MinerU 在补偿和式之后及 `F_n`-martingale / 二阶矩句间插入多处 NUL/SOH/ETX/form-feed 和 `<sub>` 标记，破坏了补偿定义与马丁格尔说明的连续数学排版。150dpi 原页确认该处为正常求和式及 `F_n`-martingale 文本。概率界 (3.21)/(3.22) 的阈值、指数与系数相符。印刷页脚页码 `30` 未保留。

## p.031（PDF p.31 / 印刷 p.31）
- 时间：2026-10-01 17:03 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p031.png`（pngmono 150dpi）；PDF p.31 完整文本层与 path-metric / Theorem 3.9 段视觉抽验；MinerU page_idx=30 与 Markdown §3.4 对应内容。
- 核对：Hausdorff-metric 文字、path metric 定义、闭单位圆盘内反例路径、Theorem 3.9 状态空间和收敛对象。
- 结果：PASS±。度量定义、定理陈述与印刷一致，Markdown 也保留了闭圆盘 overline。仅发现 “Hausdorff” 写作 “Hausdorf”（少一个 `f`），列入逐处修复清单。印刷页脚页码 `31` 未保留。

## p.032（PDF p.32 / 印刷 p.32）
- 时间：2026-10-01 17:05 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p032.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p032_compactness.png`（源页 pnggray 300dpi 裁片）；PDF p.32 完整文本层与紧致性论证目检；MinerU page_idx=31 与 Markdown path-space 定义、Lemma 3.10。
- 核对：path-space 名称 `X_Υ`、路径映射方向、compactness lemma 的对象、`diam` 模量、s(t) 求和起始指标及严格单调叙述。
- 结果：FAIL。300dpi 裁片确认印刷使用 `𝓧_Υ`（空间记号）并以 `diam(γ̂[s₁,s₂])` 定义 ε；MinerU 分别误成 `χ_r(U)` 和 `dim(γ̂[…])`。印刷路径映射是普通 `→`，Markdown 在箭头上添加点。印刷的级数为 `Σ_{n≥0} 2^{2−n}=8`，Markdown 改为 `n>0`，该范围下和不等于 8；同时把 “continuous and strictly” 写成含多余 `P` 的 “continuous Pand strictly”。这些不一致破坏 path-space 紧致性陈述和求和公式，列入全篇修复。印刷页脚页码 `32` 未保留。

## p.033（PDF p.33 / 印刷 p.33）
- 时间：2026-10-01 17:07 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p033.png`（pngmono 150dpi）；PDF p.33 文本层与 Lemma 3.10–3.12 证明上下文；MinerU page_idx=32 与 Markdown compact-set 及 tameness 论证。
- 核对：X_Υ(D) 的紧致闭集命题、直径概率界、tameness 概率陈述及 proof 中的集合资格判断。
- 结果：FAIL。原文 Lemma 3.12 proof 判断 `γ ∉ X_Υ(D)`；Markdown 将其写成 `γ ∉ X_Y(D)`，把定义参数 `Υ` 换成了拉丁字母 Y，与前面的 `X_Υ` 不同，改变被检验的路径集合。PDF p.33 原页确认该处为 `X_Υ(D)`。本页余下概率界和引理陈述与印刷一致；印刷页脚页码 `33` 未保留。

## p.034（PDF p.34 / 印刷 p.34）
- 时间：2026-10-01 17:10 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p034.png`（pngmono 150dpi）；PDF p.34 文本层；MinerU page_idx=33 与 Markdown Lemma 3.12 准确率/准环事件部分。
- 核对：概率界 (3.23)/(3.24)、(β,α)-quasi-loop 定义、事件概率控制与 X_Υ(D) 结论。
- 结果：PASS±。本页数学不等式、指数和集合引用与印刷文本相符；Markdown 在 “given above” 与 “remains to verify” 附近夹有控制字符，属于排版污染但不改变本页结论，列入逐处清理。印刷页脚页码 `34` 未保留。

## p.035（PDF p.35 / 印刷 p.35）
- 时间：2026-10-01 17:08 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p035.png`（pngmono 150dpi）；PDF p.35 文本层与 (3.26)–(3.28) 源页目检；MinerU page_idx=34 与 Markdown quasi-loop 概率界及 Lemma 3.13 参数化。
- 核对：quasi-loop 覆盖概率、X_Υ^r(D) 与 X_{Υ*}(U) 映射、diam/dist 不等式和 Koebe/harmonic-measure 下界。
- 结果：PASS±。集合参数、(3.26)–(3.28) 的变量和不等式与原页一致；Markdown 在 `c₁=ε/4` 后插入 NUL，并把 “sufficient” 写成 “suficient”（少一个 `f`），且有重复分号，列入逐处清理。印刷页脚页码 `35` 未保留。

## p.036（PDF p.36 / 印刷 p.36）
- 时间：2026-10-01 17:13 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p036.png`（pngmono 150dpi）；PDF p.36 完整文本层与 Lemma 3.14 视觉核对；MinerU page_idx=35 与 Markdown convergence-relations 命题。
- 核对：Lemma 3.13 的 extremal-distance 推论、Lemma 3.14 的输入收敛、逆映射局部一致收敛及曲线局部一致收敛结论。
- 结果：FAIL。印刷 Lemma 3.14 明确给出 `Wⁿ → W`、`f_tⁿ → f_t`、`γⁿ → γ` 三项收敛；MinerU Markdown 把这三处箭头全部漏掉，只剩相邻变量并写“locally uniformly”，缺失关系符使核心收敛条件不完整。150dpi 原页和 PDF 文本层均确认三个箭头。Lemma 3.13 末另有 NUL 控制字符，列入清理。印刷页脚页码 `36` 未保留。

## p.037（PDF p.37 / 印刷 p.37）
- 时间：2026-10-01 18:49 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p037.png`（pngmono 150dpi）；PDF p.37 文本层及局部一致收敛论证整页目检；MinerU page_idx=36 与 Markdown Theorem 3.9 proof、capacity continuity 段。
- 核对：Wⁿ→W、ρ(β_n,β)→0、重参数化 ε_n 的收敛关系、t_n→t 与 γ̃ⁿ 的局部一致收敛结论。
- 结果：FAIL。印刷中四处明确收敛箭头在 MinerU Markdown 丢失：`Wⁿ → W`、`ρ(β_n,β) → 0`、`γ̃ⁿ ∘ ε_n → γ̃` 与 `t_n → t`；分别把变量/量词并列成无关系表达，影响弱收敛到局部一致收敛的论证。150dpi 原页确认箭头均存在。另有 “Hausdorff” 写作 “Hausdorf”（少一个 `f`）。印刷页脚页码 `37` 未保留。

## p.038（PDF p.38 / 印刷 p.38）
- 时间：2026-10-01 19:30 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p038.png`（pngmono 150dpi）；PDF p.38 完整文本层及极限论证整页目检；MinerU page_idx=37 与 Markdown capacity/compactness proof。
- 核对：耦合下 `ρ(φ_δ⁻¹∘γ_δ,β)→0`、`φ_δ→φ` 局部一致、(3.29)–(3.30) 概率界及定理结尾。
- 结果：FAIL。PDF 明确写有 `ρ(φ_δ⁻¹∘γ_δ,β) → 0` 与 `φ_δ → φ`；MinerU Markdown 在这两处漏掉收敛箭头，只保留相邻项，影响对耦合收敛和核定理推论的陈述。150dpi 源页确认箭头存在。(3.29)/(3.30) 与后续概率界的箭头/阈值匹配。印刷页脚页码 `38` 未保留。

## p.039（PDF p.39 / 印刷 p.39）
- 时间：2026-10-01 20:08 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p039.png`（pngmono 150dpi）；PDF p.39 文本层与整页 Figure 4.1 目检；MinerU page_idx=38 与 Markdown Figure 4.1 引用/题注和 Peano-grid 顶点定义。
- 核对：4.1 setup、Figure 4.1 图像/题注、边界弧及 q/κ 区间、Peano 顶点格与 adjacency 合同。
- 结果：FAIL。印刷明确规定 “v,u neighbor iff |v−u|=1/2”；Markdown 写成 “neighbor if |v−u|=1/2”，漏掉第二个 `f`，把双向定义降成单向条件。该邻接关系决定图 G 的边集合。图像 `images/page_38_image_0.jpg` 存在且与印刷 Figure 4.1 相符；另有 “different”→“diferent” 拼写漏字。印刷页脚页码 `39` 未保留。

## p.040（PDF p.40 / 印刷 p.40）
- 时间：2026-10-01 20:27 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p040.png`（pngmono 150dpi）；PDF p.40 文本层与边界图整页目检；MinerU page_idx=39 与 Markdown Figure 4.2 及树/Peano 顶点定义。
- 核对：Figure 4.2 boundary-data 图；adjacency 的三种距离规则；β_a、β_b 的 dual-tree 隶属条件及 D(α,β,a,b) 边界定义。
- 结果：FAIL。印刷规定 `β_a ∈ β`，Markdown 写为 `β_a ∈ β_{:}`，在树集合符号后插入冒号/下标，改变了边界条件。源页图和 PDF 文本确认没有该冒号。Figure 4.2 图像 `images/page_39_image_0.jpg` 存在且与印刷图一致。印刷页脚页码 `40` 未保留。

## p.041（PDF p.41 / 印刷 p.41）
- 时间：2026-10-01 20:42 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p041.png`（pngmono 150dpi）；PDF p.41 完整文本层与 orientation-graph 构造目检；MinerU page_idx=40 与 Markdown orientation 标记、out/in-degree 论证。
- 核对：H/H† 生成树关系、Peano grid 的朝向定义、γ 的边集定义、每个 Peano vertex 的出/入度与反向构造。
- 结果：FAIL。印刷将有向 Peano graph 明确记作 `G→`（原叙述说以带箭头的 G 区别定向图）；MinerU 多处只写 `G`、`G_{} ` 或句点，丢失这个方向标记。该标记随后用于 edge set 和 out-degree / in-degree 论证，丢失会使图对象定义不完整。150dpi 原页确认印刷带箭头。其余树、边交点与邻接记号和本页原文相符；印刷页脚页码 `41` 未保留。

## p.042（PDF p.42 / 印刷 p.42）
- 时间：2026-10-01 20:56 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p042.png`（pngmono 150dpi）；PDF p.42 文本层与 Dirichlet–Neumann 定义整页目检；MinerU page_idx=41 与 Markdown 逆向建树、orientation-marked graph、离散差分定义。
- 核对：T†(γ*) 回构式、T↦γ(T) 双射、G→ 定向图标记及 Δ_{H,E0,E1,E2}ĥ 的定义/调和函数条件。
- 结果：FAIL。印刷为 `T†(γ*) := β_{ℓ+1}(γ*)`，Markdown 在开括号上误加点；印刷用 `G→` 表示定向图，Markdown 多处写成空下标 `G_{}`，丢失方向标记。离散算子中印刷定义 `dĥ[v,u]`，Markdown 首项把帽子移到 d 上，且谐函数条件把 `ĥ(v)=0` 录成双点 `¨h(v)=0`；这些差异改变算子/方程记号。页内亦有控制字符和重复分隔符，按印刷逐处修复。印刷页脚页码 `42` 未保留。

## p.043（PDF p.43 / 印刷 p.43）
- 时间：2026-10-01 21:21 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p043.png`（pngmono 150dpi）；PDF p.43 文本层与 Dirichlet–Neumann / 4.2 开篇整页目检；MinerU page_idx=42 与 Markdown Proposition 4.2、UST Peano path 和 conformal maps。
- 核对：`\hat{h}` 与 Dirichlet–Neumann 边界值、Peano path 所在有向图、φ₀/φₙ 映射方向、φₙ−φ₀ 收敛和 capacity-at-infinity 渐近式。
- 结果：FAIL。印刷把 UST Peano path 放在 `G→ ∩ D̄` 中，Markdown 写为 `G_{} ∩ D̄`，丢失定向图标记；印刷映射 `φ₀=φ:D→H` 在 Markdown 变成 `D H`，丢失映射箭头；capacity 渐近条件 `z→∞` 的箭头也被漏掉。150dpi 源页确认这些符号。另有 “sufficiently” 写作 “suficiently” 的少字母差异，列入逐处修复。印刷页脚页码 `43` 未保留。

## p.044（PDF p.44 / 印刷 p.44）
- 时间：2026-10-01 21:52 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p044.png`（pngmono 150dpi）；PDF p.44 文本层与 Prop. 4.3 / (4.1)–(4.2) 源页目检；MinerU page_idx=43 与 Markdown 的条件期望和半径假设。
- 核对：m 的首次越界定义、(4.1)/(4.2) 的系数 8 与条件概率、`rad₀(D_k) ≥ r₀` 及 harmonic-measure 条件。
- 结果：FAIL。印刷条件是 `rad₀(D_k) ≥ r₀`；Markdown 写成 `ra l₀(D_k) ≥ r₀`，将下标 0 前额外插入字母 l，破坏半径参数记号。150dpi 原页确认 `rad₀`。图 4.3 及估计公式其余可见符号相符。印刷页脚页码 `44` 未保留。

## p.045（PDF p.45 / 印刷 p.45）
- 时间：2026-10-01 22:19 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p045.png`（pngmono 150dpi）；PDF p.45 文本层与 Proposition 4.3 证明整页目检；MinerU page_idx=44 与 Markdown harmonic-measure 函数 h、等式 (4.3)–(4.5) 及 D̃_n 条件。
- 核对：h(z) 公式、(4.4)/(4.5) 的值、radial-domain 条件、对 D̃_n 中 η_n 的构造及条件期望。
- 结果：FAIL。印刷写作 “Assume that Q₀ intersects D̃_n”；MinerU Markdown 写成 `Q₀ intersects D_n`，漏掉 ~ 标记，换成了不同的域对象，后续 η_n 的构造因此指向错误集合。150dpi 原页清楚显示 D̃_n。其余本页 h(z)、(4.4)/(4.5) 系数和幂次与印刷相符；印刷页脚页码 `45` 未保留。

## p.046（PDF p.46 / 印刷 p.46）
- 时间：2026-10-01 22:41 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p046.png`（pngmono 150dpi）；PDF p.46 文本层与 (4.6)–(4.5) 化简、Theorem 4.4 目检；MinerU page_idx=45 与 Markdown 概率展开及收敛定理声明。
- 核对：Taylor 展开中的系数 24、(4.1)/(4.2) 联立、D→H 共形映射、capacity-from-infinity 参数化与 Brownian bound。
- 结果：FAIL。Theorem 4.4 印刷映射为 `φ:D → H`，Markdown 丢失 `→`；印刷将 `γ̂:=φ∘γ` 参数化为 “capacity from ∞”，Markdown 在公式后多出 `2` 且省掉 `∞`。半径条件印作 `rad₀(D)>r₁`，Markdown 将 `rad₀` 拆为 `r a d₀`。以上损坏定理的域映射/参数边界；原页确认这些记号。方程化简中的 24 在 Markdown 写作 `2 4`，另列入数字排版修复。印刷页脚页码 `46` 未保留。

## p.047（PDF p.47 / 印刷 p.47）
- 时间：2026-10-01 23:23 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p047.png`（pngmono 150dpi）；PDF p.47 文本层与基点移动论证整页目检；MinerU page_idx=46 与 Markdown Theorem 4.4 proof / z₀ 半径比较。
- 核对：式 (4.7) 控制条件、z₀ 的尺度、Koebe distortion 导出的 `rad_{z₀}(D)` 比较及 theorem 结束句。
- 结果：FAIL。印刷写作 `rad_{z₀}(D) ≥ c rad₀(D)`；MinerU 将半径下标写成 `·z₀`，添加了点，改变中心的标记。150dpi 原页确认下标仅为 `z₀`。Markdown 还在 “φ(0) is close to i” 前插入连字符/ETX 控制字符；列入逐处清理。页脚之后开始 §4.3；印刷页码 `47` 未保留。

## p.048（PDF p.48 / 印刷 p.48）
- 时间：2026-10-01 23:38 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p048.png`（pngmono 150dpi）；PDF p.48 完整文本层与 conformal-map convergence / capacity 参数化整页目检；MinerU page_idx=47 与 Markdown φ_R、γ̂、g_t 和 Lemma 4.6。
- 核对：`lim_{R→∞}R⁻¹φ_R⁻¹=φ⁻¹`、γ̂ 的 capacity-from-infinity 参数化、g_t 的源/目标域、(4.8) 条件。
- 结果：FAIL。印刷写明 `lim_{R→∞} R⁻¹ φ_R⁻¹(z)=φ⁻¹(z)`，Markdown 把极限下标的 R 换成 `·`；印刷将 γ̂ 参数化为 capacity from `∞`，Markdown 漏掉该端点；印刷映射 `g_t:H\γ̂[0,t]→H`，Markdown 将目标平面写成 `F`。150dpi 原页确认这些符号。Prop. 4.5 与 Lemma 4.6 的概率阈值和 (4.8) 其余内容吻合。印刷页脚页码 `48` 未保留。

## p.049（PDF p.49 / 印刷 p.49）
- 时间：2026-10-01 23:57 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p049.png`（pngmono 150dpi）；PDF p.49 文本层与 Lemma 4.6 proof 整页目检；MinerU page_idx=48 与 Markdown δ_R / length(η) 极限及 (4.9)–(4.11)。
- 核对：δ_R 随 R 的极限、极端长度到零的推导、事件 X₀/X₁ 定义和三个概率界。
- 结果：FAIL。印刷两处写作 `lim_{R→∞} δ_R=0` 与 `lim_{R→∞} length(η)=0`；Markdown 对应极限下标都丢失 `→`（`R ∞`），缺少所取极限方向。150dpi 源页确认箭头；(4.9)–(4.11) 的量词、事件关系和阈值相符。另有 “suffices/sufficiently” 少一个 `f` 的拼写差异，列入逐处修复。印刷页脚页码 `49` 未保留。

## p.050（PDF p.50 / 印刷 p.50）
- 时间：2026-10-02 00:12 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p050.png`（pngmono 150dpi）；PDF p.50 文本层与 separator/annulus 论证整页目检；MinerU page_idx=49 与 Markdown Figure 4.4 引用和证明段。
- 核对：η 对无穷远的分离关系、外圆盘记号 B、三个连通分支、树/对偶树路径连接与 Figure 4.4。
- 结果：FAIL。印刷两处写明相关曲线段与 `∞` 分离；Markdown 在“separates … from ∞”及后续复述中都漏掉 `∞`。印刷还定义 “Let B denote the open disk”，Markdown 写成 “Let denote the open disk”，漏掉变量 B，致使后文引用的圆盘未定义。150dpi 原页确认两处符号/变量；Figure 4.4 的 `images/page_49_image_0.jpg` 存在并与印刷示意图相符。印刷页脚页码 `50` 未保留。

## p.051（PDF p.51 / 印刷 p.51）
- 时间：2026-10-02 00:13 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p051.png`（pngmono 150dpi）；PDF p.51 文本层；MinerU page_idx=50 与 Markdown §4.6 proof 中的树/对偶树路径及 (4.9)–(4.11) 收尾。
- 核对：X₁/X₀ 事件分解、χ/χ† 树路径、D′ 边界交叉条件、(4.11) 结论和 Proposition 4.5 的一致连续估计。
- 结果：PASS±。路径集合、概率阈值与推理顺序和 PDF 文本层一致；该段在 Markdown 末尾含多余控制字符/句点，列入清理。印刷页脚页码 `51` 未保留。

## p.052（PDF p.52 / 印刷 p.52）
- 时间：2026-10-02 00:15 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p052.png`（pngmono 150dpi）；PDF p.52 文本层及 Theorem 4.8 声明整页目检；MinerU page_idx=51 与 Markdown Peano-path convergence theorem。
- 核对：Theorem 4.7 的 Chordal SLE₈ 路径断言、Theorem 4.8 的边界条件近似、终点和 capacity 参数化，以及 path-space 收敛模式。
- 结果：FAIL。Theorem 4.8 印刷近似对象为 `(D^R, α^R, β^R)`，终点映射为 `b → ∞`，且 `γ̂` 参数化为 capacity from `∞`。Markdown 在近似三元组外加 closure 横线、漏写终点 `∞`，并省去参数化的 `∞`，改变定理输入与收敛对象。150dpi 原页确认印刷记号。其余 Theorem 4.7/4.8 概率与 path-space 陈述相符；印刷页脚页码 `52` 未保留。

## p.053（PDF p.53 / 印刷 p.53）
- 时间：2026-10-02 00:17 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p053.png`（pngmono 150dpi）；PDF p.53 完整文本层与 Theorem 4.7 / Theorem 1.3 proof 目检；MinerU page_idx=52 与 Markdown Corollaries 4.9–4.10。
- 核对：径向 SLE₈ 的扩张结论、`R→∞` 的映射极限、从 b 起算的容量段、尾部回归条件及路径反演表达式。
- 结果：PASS±。各定理、路径参数及概率结论与印刷一致；Markdown 在 Corollary 4.9 句首/`t>0` 后插入控制字符，并在 Theorem 1.3 的极限下标 `R→∞` 前多出一个点。两者列入逐处排版修复清单。印刷页脚页码 `53` 未保留。

## p.054（PDF p.54 / 印刷 p.54）
- 时间：2026-10-02 00:19 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p054.png`（pngmono 150dpi）；PDF p.54 源页目检与文本层；MinerU page_idx=53 与 Markdown discrete derivatives、Lemma 5.1 和 Lemma 5.2 开头。
- 核对：差分算子定义、Lemma 5.1 的调和函数签名/值域和 (5.1)、D_δ 集合及 Lemma 5.2 约束开头。
- 结果：FAIL。印刷 Lemma 5.1 定义的是 `h: V(D)∪V∂(D) → R`，Markdown 写成变量 `ι`，且漏掉映射箭头；随后 (5.1) 却用 `h`，使函数合同自相矛盾。Lemma 5.2 开头又插入无意义的 `\{satisfy\}` 标记，截断 D_δ 的条件句。150dpi 原页确认函数变量与箭头以及 `D_δ satisfy rad₀(D) ≥ …` 的正常文本。印刷页脚页码 `54` 未保留。

## p.055（PDF p.55 / 印刷 p.55）
- 时间：2026-10-02 00:20 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p055.png`（pngmono 150dpi）；PDF p.55 文本层；MinerU page_idx=54 与 Markdown Lemma 5.2 的离散导数界及 Koebe 网格链。
- 核对：Lemma 5.2 的绝对值导数估计、离散导数定义、v_j 的邻距/局部半径条件与 k=0 论证。
- 结果：PASS±。本页 (5.2)、导数索引和 `rad_{v_{j−1}}(D)/10` 条件与 PDF 一致。Markdown 将 “sufficiently small” 写作 “suficiently small”（少一个 `f`），列入修复清单；印刷页脚页码 `55` 未保留。

## p.056（PDF p.56 / 印刷 p.56）
- 时间：2026-10-02 00:24 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p056.png`（pngmono 150dpi）；`audit/300dpi/Werner_2001_lsw_conformal_invariance_p056_signatures.png`（源页 pnggray 300dpi 裁片）；PDF p.56 文本层与 Lemma 5.3 证明整页目检；MinerU page_idx=55 与 Markdown function signatures 和 compactness subsequence。
- 核对：Lemma 5.3 中 h/h* 的定义域值域、(5.3)、反证序列、缩放函数 hⁿ，以及局部一致子序列所用的映射。
- 结果：FAIL。印刷 `h:V(D)∪V∂(D)→[0,∞)` 与 `h*:D→[0,∞)` 两个函数签名在 Markdown 均漏掉 `→`；300dpi 裁片确认。紧致性证明所用映射是 `h_n∘ψ_{D_n}^{−1}`，Markdown 漏掉下标 n，写成 `h_n∘ψ_D^{−1}`，使缩放域与函数不匹配。Markdown 还把页面续接处多出一个 `2` 接在 v 条件前；列入清理。印刷页脚页码 `56` 未保留。

## p.057（PDF p.57 / 印刷 p.57）
- 时间：2026-10-02 00:26 EDT；actor=Peer-P31；model=gpt-6-luna；effort=max。
- 证据：`audit/Werner_2001_lsw_conformal_invariance_p057.png`（pngmono 150dpi）；PDF p.57 文本层；MinerU page_idx=56 与 Markdown 离散导数极限 (5.4) 和 Lemma 5.4 的 boundary-hitting 条件。
- 核对：(5.4) 的导数阶数/一致收敛、Lemma 5.4 的边界邻近阈值、距离集合、击中先后与概率上界。
- 结果：PASS±。逐阶离散导数收敛与 Lemma 5.4 的集合条件、绝对值和概率界与 PDF 相符；页面内容在 MinerU 文本中连续。印刷页脚页码 `57` 未保留。
