# AUDIT — Venkatesh_2006_sparse_equidistribution

## 任务与来源

- Actor：`Peer-P36`
- Model / effort：`gpt-6-luna / max`
- 角色：Peer evidence contributor；唯一 canonical integrator 为 `Master-Luna`
- 基线：`037602429d3b009f6fc468c732073eb3ddf9875f`（本工作树 `d870`，detached；与 main 基线相同）
- 源 PDF：`Venkatesh_2006_sparse_equidistribution.pdf`，91 页；SHA-256 `c2676117a3f4b833b6354a586efeeb28ba367928bc8d83e0c310f0942ece2265`
- MinerU Markdown（审计基线）：`Venkatesh_2006_sparse_equidistribution__Venkatesh_2006_sparse_equidistribution.md`；SHA-256 `2fd195c4e0adcc00f7eab551949b27b8b71d70b3435dc9fbfdff09c3478a3fa8`
- PDF 类型：born-digital；`pdfinfo` 显示 Creator `LaTeX with hyperref package`、Producer `dvips + GPL Ghostscript SVN PRE-RELEASE 8.62`；`pdftotext -layout` 文本层 336,324 bytes，U+FFFD 数量为 0。
- 审计方式：91 页逐页对账 PDF 完整文本层与 MinerU Markdown；另目检题录/标题页及两张密集数学页的 150dpi 原页图。字形疑点以 PDF 原页 PNG/300dpi 裁片仲裁。
- MinerU 导出元数据：`middle_json.json` 标记 MinerU 3.4.4；所检 `middle_json.json` 与 `structured_content.json` 中未发现 `doc_id` 字段。
- 状态：候选审计证据，未集成到 main；本 Peer 不修改根级 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、`README.md` 或 `MEMORY.md`。

## 逐页审计

## p.001（PDF p.1 / 印刷 p.1）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p001.png`（pngmono 150dpi）
- 核对：题名、作者、摘要、目录、§1 首段；将 PDF p.1 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1–26 行），并目检本页原图。
- 结果：FAIL。
- 差异：PDF 摘要末句印作 “Fourier coefficients of automorphic forms”；Markdown 摘要写作 “Fourier coeficients of automorphic forms”，漏掉 `coefficients` 中第二个 `f`。PDF 文本层与 150dpi 原页图一致，属 MinerU 内容级拼写差异；待全篇审计完成后逐处手工修复。
- 核验时间：2026-10-01 16:12 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p002.png`（pngmono 150dpi）
- 核对：PDF p.2 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 26–42 行；该页首句接续前页段落），并核对 §1.1 总览和结果摘要至 §4 开头。
- 结果：FAIL。
- 差异：PDF p.2 的 Thm. 3.2 摘要印作 “Fourier coefficients of automorphic forms”；Markdown 将 `coefficients` 写成 `coeficients`，漏掉第二个 `f`。本页其余已核段落、目录结果和 §4 开头与 PDF 页文本层对应；页眉/页码属于版面元素。
- 核验时间：2026-10-01 16:15 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。
## p.003（PDF p.3 / 印刷 p.3）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p003.png`（pngmono 150dpi）；字形仲裁裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p003_Grossencharacter.png`（PDF p.3，pnggray 300dpi）。
- 核对：PDF p.3 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 44–60 行），含 Prop. 4.1/4.2 摘要、§6/§7 摘要和脚注 1–2；对 `Grössencharacter` 重音位置做 300dpi 原页仲裁。
- 结果：FAIL。
- 差异：PDF 印作 `sufficient`、`PGL₂`、`Grössencharacter`、`different`；Markdown 对应处分别为 `suficient`、正文 `PGL` 与游离 page-footnote `PGL₂`、`Gr¨ossencharacter`、`diferent`。300dpi 裁片确认重音点在 `ö` 上，且 PDF 正文将下标 2 排在 `PGL` 后；后三处需恢复连写/重音位置，漏字母项待全篇后手工修复。
- 核验时间：2026-10-01 16:18 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p004.png`（pngmono 150dpi）。
- 核对：PDF p.4 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 62–76 行），含 §1.1 末段、§1.2 开头及权重向量示例的本页部分。
- 结果：FAIL。
- 差异：PDF 印作 `coefficients`、`difference`、两处 `effective`；Markdown 分别为 `coeficients`、`diference`、`efective`。公式上下文 `$L(\pi, \frac12+it)$` 与文本层一致，但 Markdown 在 `$k>1$` 后多出一个分号；`For m ∈ Z, let` 被录为 `$m \in Z .$let`，且 `SL(2,R)-subrepresentation` 前多出 `)`，本页末的逗号被误作句点。均按 PDF p.4 文本层记为待修差异。
- 核验时间：2026-10-01 16:19 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p005.png`（pngmono 150dpi）。
- 核对：PDF p.5 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 78–94 行），覆盖 §1.2 后半、§1.3 标题与 §1.3.1 开头至本页页底。
- 结果：FAIL。
- 差异：PDF p.5 写作 `Fourier coefficients`、`different points`、`a more down-to-earth fashion`；Markdown 分别为 `Fourier coeficients`、`diferent points`、`a a more down-to-earth fashion`。前两项漏录 `f`，后一处重复录入 `a`；需手工修复。
- 核验时间：2026-10-01 16:21 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p006.png`（pngmono 150dpi）；脚注标记裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p006_footnote3.png`；脚注正文复核裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p006-footnote3-full.png`（均为 PDF p.6，pnggray 300dpi）。
- 核对：PDF p.6 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 94–132 行）；目检密集数学页，逐项核对公式 (1.1)–(1.3) 的积分域、指数、\(\check{\sigma}\)、不等式、变量和编号。
- 结果：FAIL。
- 差异：PDF 印作 `coefficients`、`suffice`、`different choices`、`efficient`、`differently`，Markdown 对应为 `coeficients`、`sufice`、`diferent choices`、`eficient`、`diferently`；另将 `\nu_i \to \nu,` 的逗号误录为句点后再接逗号。PDF p.6 “analytic number theory”后的脚注标记是上标 `3`，Markdown 写作 `\overset \sim {3}`；300dpi 裁片确认是普通上标数字。公式 (1.1)–(1.3) 核对一致。脚注中的 `G_2` 与四次/八次积分式分散到相邻 page-footnote spans，但这些可见片段仍在 Markdown 中，记作排版伪影。
- 核验时间：2026-10-01 16:23 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p007.png`（pngmono 150dpi）；`L-functions` 原页裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p007_L-functions.png`（PDF p.7，pnggray 300dpi）。
- 核对：PDF p.7 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 126–160 行），覆盖 §1.3.2、公式 (1.4)、§1.3.3 开头及脚注 3 延续；对 `L-functions` 连字符位置做 300dpi 原页仲裁。
- 结果：FAIL。
- 差异：印刷为行末断词 `L-` / `functions`，构成普通连字符 `L-functions`；Markdown 写作 `$L_{-}$ functions`，多出下标负号，300dpi 裁片确认连字符在基线线上。另，PDF `Y_i`-periods 前没有句点，Markdown 在连字符前多录句点；均值公式 `\int_{-T}^{T}|\zeta(1/2+it)|^4dt \sim T\log(T)^4` 的 Markdown 编码在 `\sim` 后多出 `}` 并拆开数学定界符。公式 (1.4) 的求和、平方、极限和积分范围与 PDF 相符。脚注 3 的 `G_2`、`\zeta(1/2+it)` 与后续说明被分到多个 page-footnote spans，内容片段仍在。
- 核验时间：2026-10-01 16:25 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p008.png`（pngmono 150dpi）；系数界裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p008_coefficient_bound.png`（PDF p.8，pnggray 300dpi）。
- 核对：PDF p.8 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 162–180 行），含公式 (1.5)、相关性解释和 Fourier 系数示例引入；用 300dpi 裁片核对系数界的绝对值线、上标和逗号。
- 结果：FAIL。
- 差异：`effect`、`effective`、`different`、`Fourier coefficients` 在 Markdown 中分别为 `efect`、`efective`、`diferent`、`Fourier coeficients`。句子 `Thus, for ν_i-typical P` 的下标 `i` 在 Markdown 中丢失；`on X.` 后的句点也缺失。系数界处 Markdown 把 `|a_n| ≤ C n^{5/6}, by A. Good` 写成 `\left. a_n \right. ≤ C n^{5/6} 2 by A. Good`，绝对值线丢失、多出数字 `2`；300dpi 裁片确认原文是 `|a_n| ≤ C n^{5/6}, by A. Good`。前一界 `|a_n| ≤ Cn, a bound` 的逗号误录成句点。公式 (1.5) 的加权平方和与内积右端相符。
- 源级 print quirk：原页实际印有 “such the value” 和 “w.r.t. the the uniform measure”；Markdown 与原页一致，故保留，不据语法预期改写。
- 核验时间：2026-10-01 16:28 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p009.png`（pngmono 150dpi）；脚注 4 裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p009_footnote4.png`（PDF p.9，pnggray 300dpi）。
- 核对：PDF p.9 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 182–222 行），覆盖公式 (1.6)–(1.8)、horocycle 参数化和 van der Corput 脚注 4；目检本页密集公式并对脚注求和/相关和裁片仲裁。
- 结果：FAIL。
- 差异：`Fourier coefficient` 在 Markdown 拼作 `Fourier coeficient`。公式 (1.6)–(1.8) 的主体与印刷一致（公式 (1.6) 原页没有 `dx`，故不补）。脚注 4 的 `\sum_{k=1}^{K} c_k`、相关和 `\sum_{k=1}^{K} c_k c_{k+h}` 以及 `c_k=f((k+i)/n), K=n` 在 Markdown 分散成损坏的 `P^K k=1` / 上下标片段、缺失分数线，并在末尾多出 `n`；300dpi 裁片核实印刷式样。
- 核验时间：2026-10-01 16:31 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p010.png`（pngmono 150dpi）。
- 核对：PDF p.10 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 224–262 行），含公式 (1.9)–(1.11)、horocycle 混合估计及系数界推论；对箭头、常数下标和 `Γ` 记号查看原页图。
- 结果：FAIL。
- 差异：PDF 写作 `y → ∞`，Markdown 在该处只写 `$y \infty$`，漏掉趋于箭头。`C_F` 后的依赖变量在 PDF 是普通 `F`，Markdown 写成 `F_{;}`，多出分号下标；δ 依赖项的 `Γ` 也被编码成带空内容的下标。PDF 的 `sufficiently small power` 在 Markdown 为 `suficiently`，漏掉第二个 `f`。公式 (1.9)–(1.11) 及其幂、积分范围和误差项与原页相符。
- 源级 print quirk：PDF p.10 原文印作 “We now use come to the equidistribution part of the argument.”，Markdown 保留该措辞，按印刷原文优先原则不改。
- 核验时间：2026-10-01 16:33 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p011.png`（pngmono 150dpi）；`\tilde f` 裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p011_tilde-f.png`（PDF p.11，pnggray 300dpi）。
- 核对：PDF p.11 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 264–282 行），覆盖 §1.3.5 两个观点、函数记号与 §1.4 开头；对 `\tilde f` 字形做 300dpi 原页仲裁。
- 结果：FAIL。
- 差异：PDF 第一个观点写作 `dg. It is simple`；Markdown 在句点后插入了额外数字 `2`。PDF 第二个观点为 `t \mapsto \tilde f(x_n n(t))`，Markdown 写成 `t \mapsto \bar f(x_n n(t))`；300dpi 裁片确认印刷为波浪号 `\tilde`。另，`Fourier coefficients` 被写成 `Fourier coeficients`，漏掉第二个 `f`。
- 核验时间：2026-10-01 16:34 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p012.png`（pngmono 150dpi）；作者姓名裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p012_acknowledgement_names.png`（PDF p.12，pnggray 300dpi）。
- 核对：PDF p.12 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 282–304 行），含 §1.4、§1.5 前半和致谢人名；用 300dpi 裁片核对 `Strömbergsson` 与 `André` 的重音。
- 结果：FAIL。
- 差异：本页三处 `Fourier coefficients` 在 Markdown 中均写成 `Fourier coeficients`，漏掉第二个 `f`；致谢中的 `Andreas Strömbergsson`、`André Reznikov` 分别误录为 `Str¨ombergsson`、`Andr´e`，300dpi 裁片确认重音位置应在 `o` 与 `e` 上。另，PDF 印作 `mean-value theorems`，Markdown 合并为 `meanvalue theorems`，缺连字符。基线 Markdown 第 304 行跨页：PDF p.12 在 “which uses the idea of changing” 后换页，p.13 才续为 “the test vector”；后续内容按 p.13 核对。
- 核验时间：2026-10-01 16:37 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p013.png`（pngmono 150dpi）。
- 核对：PDF p.13 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 304–326 行），覆盖致谢跨页续句、§1.5 后半、§1.6 及 §2.1 通用记号至卷积关系。
- 结果：FAIL。
- 差异：PDF 印作 `suffered`，Markdown 为 `sufered`，漏掉第二个 `f`。在 `g \cdot f` 定义中，PDF 写作 “the right translate of f by g, i.e.”，Markdown 在 `g` 前多录 `^`、并将逗号包入公式。卷积定义使用普通群 `G`，Markdown 多出下标 `\ell` 写成 `G_\ell`；此外 `A ≤ cB.` 后的句点在 Markdown 中缺失。其余平移、点质量及 (σ₁⋆σ₂) 兼容关系与本页对应。
- 核验时间：2026-10-01 16:38 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p014.png`（pngmono 150dpi）；300dpi 裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p014_Ad.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p014_absolute-value.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p014_different.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p014_character-arrow.png`。
- 核对：PDF p.14 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 328–352 行），覆盖 §2.1 后段、§2.2–2.3、§2.4 开头；对 `Ad(g)`、绝对值映射、局部不同理与特征箭头做 300dpi 字形仲裁。
- 结果：FAIL。
- 差异：PDF 定义 `Ad(g)` 为 `X ↦ gXg^{-1}`，Markdown 对应公式被损坏成 `^{4·} X g X g^{-1...}`；原页绝对值映射为 `x ↦ |x|_v`，Markdown 多插入 `\mathbf{\Phi}`。PDF `different` 被写为 `diferent`；`\mathfrak{o}_{F_v}` 被误成 `\mathfrak{o}_{F_\tau}`；“finite place v of F”中的 `F` 多出分号下标。两处 `sufficiently` 均拼作 `suficiently`。本页 §2.4 的字符 `\omega: Z(\mathbb A_F) \to \mathbb C^\times` 在 Markdown 中漏掉 `\to` 箭头；300dpi 裁片确认原页有该箭头。
- 核验时间：2026-10-01 16:41 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p015.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p015_avx.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p015_Kv.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p015_accomodate.png`（均为 PDF p.15，pnggray 300dpi）。
- 核对：PDF p.15 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 352–400 行），覆盖 §2.4 后段、公式 (2.1)–(2.3)、GL₂ 紧子群记号及脚注 5–6；对群下标和脚注局部字形作 300dpi 仲裁。
- 结果：FAIL。
- 差异：PDF 在 “notions of ‘size’” 中以引号括住普通单词，Markdown 写成 `^{66} size^{9}`，多出上下标数字。`g_f=(g_v)_{v\text{ finite}} \in G(\mathbb A_{F,f})` 前，Markdown 另插入 `\mathbf{\{}`。PDF 的紧子群是 `K_v`，Markdown 首次写为 `K_\tau`；300dpi 裁片确认是下标 `v`。脚注 5 的 `different notation` 在 Markdown 中为 `diferent`。
- 源级 print quirks：PDF 印作 `a_v(x)`，随后括号内却写 `a(y)`；300dpi 裁片确认 `x` 是印刷原文，保留该变量不一致。脚注原文将 `accommodate` 拼作 `accomodate`；Markdown 忠实保留，勿据常规拼法改写。
- 核验时间：2026-10-01 16:44 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p016.png`（pngmono 150dpi）；记号裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p016_measure-notation.png`（PDF p.16，pnggray 300dpi）。
- 核对：PDF p.16 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 402–436 行），覆盖 §2.5 的有限处紧群、公式 (2.4)、字符取值及 §2.6 至离散群计数测度。
- 结果：FAIL。
- 差异：`\mu_X` 在 Markdown 写成 `\mu \mathbf{x}`；局部紧子群质量处将 `\mathfrak{o}_{F_v}^{\times}` 的 `v` 误录为 `\tau`。体积归一化式 `\operatorname{vol}(F_\infty/\mathfrak{o}_F)=1` 在 Markdown 丢掉 `l` 并将 `\mathfrak{o}_F` 变成 `0_F`；Haar 测度段 `N(F_v)` 前多出点号 `\dot{}`。句末还多出 `\rangle`。300dpi 裁片核对了体积与 `N(F_v)` 两处。
- 源级 print quirks：原页确实写作 “to be the be the kernel”，并在定义 `K[q^{e_q}]` 后的商中使用 `\varpi_q^m`；Markdown 对应一致，照录、不按预期参数修正。
- 核验时间：2026-10-01 16:47 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.017（PDF p.17 / 印刷 p.17）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p017.png`（pngmono 150dpi）；证明结束符裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p017_proof-marker.png`（PDF p.17，pnggray 300dpi）。
- 核对：PDF p.17 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 438–466 行），覆盖概率测度说明、§2.7 投影定义、公式 (2.5) 及 Lemma 2.1 证明。
- 结果：FAIL。
- 差异：PDF 写作 `they differ by some constant`，Markdown 为 `they difer by some constant`，漏掉第二个 `f`。证明结尾 PDF 印有空方框 `□`，Markdown 则含私有字符 U+0003；300dpi 裁片确认应还原为方框符号，不能将它删除。公式 (2.5) 的共轭 `\overline{\chi(y)}` 及两因子投影内容与原页相符。
- 核验时间：2026-10-01 16:48 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.018（PDF p.18 / 印刷 p.18）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p018.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p018_Hecke-measure-index.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p018_alpha-3-26.png`（PDF p.18，pnggray 300dpi）。
- 核对：PDF p.18 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 468–496 行），覆盖 Hecke 测度定义、公式 (2.6)–(2.7)、Ramanujan 参数和 §2.9.1 开头；300dpi 裁片仲裁 μ 的 ℓ-幂下标及 `3/26`。
- 结果：FAIL。
- 差异：PDF 定义 `\mu_{\ell^r}^*`，Markdown 写成类似 `\mu_{[r]}^*`；公式 (2.6) 的求和项应含 `\mu^*_{\ell^{r-2k}}`，Markdown 漏掉底数 `\ell`。该页三处 `different` / `suffice` / `compatible` 分别误为 `diferent`、`sufice`、`compatiable`；`suffice` 的漏字母又出现于 §2.9.1 首段。`v\mid nm` 条件被拆为 `<sup>v</sup>|<sup>nm</sup>`，并把 `L^2(\Gamma\backslash SL_2(\mathbb R))` 后多录一个右括号。
- 复核：源码中的两处 “3 / 2 6” 均处于 TeX 数学环境，空格被忽略，排版值仍为 3/26，不作为内容差异或修复项。（更正复核：2026-10-02 05:15 EDT；Peer-P36）
- 核验时间：2026-10-01 16:50 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.019（PDF p.19 / 印刷 p.19）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p019.png`（pngmono 150dpi）。
- 核对：PDF p.19 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 496–530 行），覆盖 Sobolev 半范数条件、§2.9.2、公式 (2.8)–(2.9) 与结尾表示空间说明；并目检本页公式/记号。
- 结果：FAIL。
- 差异：首段两个 `suffice` 都拼为 `sufice`。半范数允许取值 `∞`，Markdown 在 “take the value” 后漏掉了 `\infty`；`finite-valued` 被并成 `finitevalued`。PDF 定义 `\|g\|` 为算子范数，Markdown 漏掉双竖线；“monomials in B”与“Changing B”中的基底 `B` 均在 Markdown 丢失；“replacing B by another basis”亦漏掉 `B`。均值定理比较式中的 `f(xg)` 与 `S_{\infty,1}(f)` 在 Markdown 多出横线，成为 `f(\bar{x}g)`、`S_{\infty,1}(\bar f)`。本页最后的 `L^2(\Gamma\backslash G)` 后多一个右括号。公式 (2.8)、(2.9) 的求和/导数阶和范数不等式与 PDF 相符。
- 核验时间：2026-10-01 16:52 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.020（PDF p.20 / 印刷 p.20）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p020.png`（pngmono 150dpi）。
- 核对：PDF p.20 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 532–554 行），含 adelic Sobolev 构造、公式 (2.10)–(2.11) 和范数参数省略约定；目检本页定义式。
- 结果：FAIL。
- 差异：PDF 写作 `This will suffice for our purposes`，Markdown 的 `suffice` 漏掉第二个 `f`。公式 (2.10) 后的说明在 PDF 为 “the sum ranges over \(\mathcal D\) that are monomials in \(\mathcal B\) of order ≤ d”，Markdown 把 \(\mathcal D\) 与 \(\mathcal B\) 两个变量均留空。公式 (2.10)、(2.11) 与默认 β=1/p 的约定其余部分对应原页；(2.11) 印刷索引写作 `\sum_i \psi_j`，Markdown 保留了同一印刷形式。
- 核验时间：2026-10-01 16:53 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.021（PDF p.21 / 印刷 p.21）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p021.png`（pngmono 150dpi）；fraktur-q 裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p021_fraktur-q.png`（PDF p.21，pnggray 300dpi）。
- 核对：PDF p.21 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 556–578 行），覆盖 §2.10 的 conductor 例子、⋆-pre-Sobolev 定义、Remark 2.1 和 Hilbert 范数构造。
- 结果：FAIL。
- 差异：印刷索引 `[K_{\max}:K_f]=2`，Markdown 在 `2` 上方误加横线写作 `\bar{2}`。`K_{q,\psi}^{*}` 的 stabilizer 被描述为 stabilizes `\psi`，Markdown 多出分号下标写成 `\psi_{;}`。Hilbert 构造中的 `e_{\mathfrak q^m}=E_{\mathfrak q^m}-E_{\mathfrak q^{m-1}}`，Markdown 将 fraktur `\mathfrak q` 写成粗体 `\mathbf q`；300dpi 裁片确认原字形为 fraktur q。其余投影与加权和结构对应原页。
- 核验时间：2026-10-01 16:55 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.022（PDF p.22 / 印刷 p.22）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p022.png`（pngmono 150dpi）；archimedean conductor 裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p022_Cond-v.png`（PDF p.22，pnggray 300dpi）。
- 核对：PDF p.22 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 580–620 行），覆盖 §2.11、公式 (2.12)–(2.14)、§2.12.1 及 analytic conductor 定义至本页页底；核对 Cond_v 符号和 equation numbering。
- 结果：FAIL。
- 差异：PDF 分别将乘积估计标为 (2.12)、平移估计标为 (2.13)；Markdown 将 (2.12) 独立留空，把乘积估计式标成 (2.13)，而平移估计式未标号。公式 (2.14) 在 PDF 为一个跨行的绝对差值及其 `\ll_\epsilon` 上界，Markdown 将主体和上界拆成两个 math display，并把 tag 留在主体一侧。句中 `in effect` 被拼成 `in efect`。解析导体公式原文为 `\operatorname{Cond}_v(\pi)=\prod_j(1+|\mu_{j,v}|)^{\deg(v)}`；Markdown 将 `Cond_v` 误作 `\mathbf{\Sigma}_v`，并把乘积索引错成 `v`，300dpi 裁片确认原式。基线 Markdown 第 620 行继续到 p.23；此页核到 PDF p.22 “We then” 为止，余句在 p.23 对账。
- 源级 print quirk：本页先定义有限导子的指数 `m_v`，随后印刷同段在底行写作模 `\varpi_v^m`；Markdown 忠实照录该印刷形式。
- 核验时间：2026-10-01 16:58 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.023（PDF p.23 / 印刷 p.23）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p023.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p023_finite-conductor.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p023_dual-representations.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p023_Im-z.png`（均为 PDF p.23，pnggray 300dpi）。
- 核对：PDF p.23 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 620–644 行），含导子分解、Remark 2.2、§2.12.3、§3 引言及 §3.1 记号 (3.1)；裁决对偶表示 hat、有限导子幂标和上半平面虚部记号。
- 结果：FAIL。
- 差异：有限导子理想写成 `\prod_v \mathfrak q_v^{m_v}` 后，Markdown 多插入数字 `2`；300dpi 原页无此数字。Markdown 将对偶集写成 hat/tilde 错位的 `\widetilde{\mathrm{GL}_2}(\widehat{F_\infty})` 一类形式，且一般 place 的双对偶记号分组不完整；PDF 是 `\widehat{\mathrm{GL}_2(F_\infty)}` / `\widehat{\mathrm{PGL}_2(F_\infty)}` 及对应的 `F_v` 版本，300dpi 裁片确认。§3.1 引言的 `different` 漏写一个 `f`。上半平面条件 PDF 为 `\Im(z)>0`，Markdown 误作 `\mathbb S(z)>0`；裁片确认印刷符号。第 3.1 定理陈述在 PDF p.24 开始，不属于本页。
- 核验时间：2026-10-01 17:21 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.024（PDF p.24 / 印刷 p.24）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p024.png`（pngmono 150dpi）；平滑函数/轨道记号裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p024_smooth-normalization.png`（PDF p.24，pnggray 300dpi）。
- 核对：PDF p.24 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 646–684 行），含 Theorem 3.1、公式 (3.1)–(3.4) 的前两式、指数阈值和 Lemma 3.1 开头；对轨道符号及平滑函数归一式做 300dpi 仲裁。
- 结果：FAIL。
- 差异：Theorem 3.1 的轨道集合在 Markdown 中未闭合 `\}`，且 `j\in\mathbb N` 断出数学环境。PDF 写作 `G_2`-orbits，Markdown 两处误生成 `G_{2^{-\mathrm{Orbits}}}`。PDF 要求 `f\in C^{\infty}(\Gamma\backslash SL_2(\mathbb R))`，Markdown 写成 `C^{\mathsf{io}}`；归一条件 `\int_{-\infty}^{\infty}g(x)\,dx=1` 被损坏为 `\bar\rho` 字符片段。300dpi 裁片确认这两处原页符号与公式。公式 (3.2)–(3.4) 和 `\gamma_{\max}` 的 `16(3-2\alpha)` 分母与 PDF 相符。
- 轻微差异：姓名缩写后 `N. Shah` 在 Markdown 缺少空格。
- 核验时间：2026-10-01 18:10 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.025（PDF p.25 / 印刷 p.25）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p025.png`（pngmono 150dpi）；证明结束符裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p025_proof-marker.png`（PDF p.25，pnggray 300dpi）。
- 核对：PDF p.25 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 686–722 行），覆盖 Lemma 3.1 证明、估计 (3.5)–(3.6)、Theorem 3.1 证明的开头及 (3.7)–(3.8)。
- 结果：FAIL。
- 差异：公式 (3.5) 在原页有编号，Markdown display 未带 `\tag{3.5}`。`matrix coefficients` 拼为 `matrix coeficients`；“as `K → ∞`”的箭头在 Markdown 丢失。Lemma 3.1 证明结束的印刷空方框 `□` 被 MinerU 导出为 U+0003；300dpi 裁片确认应保留为空方框符号。其余 (3.5)–(3.8) 中的积分范围、共轭项、指数和求和范围与 PDF 页图对应。
- 核验时间：2026-10-01 19:07 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.026（PDF p.26 / 印刷 p.26）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p026.png`（pngmono 150dpi）；证明结束符裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p026_proof-marker.png`（PDF p.26，pnggray 300dpi）。
- 核对：PDF p.26 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 724–738 行），含 Theorem 3.1 证明收尾、Remark 3.1 和 §3.2 开头至一般群的定义。
- 结果：FAIL。
- 差异：`differs` 被写作 `difer`；Remark 3.1 的 `effective/effectively` 多处漏 `f`，`sufficiently` 漏第二个 `f`；§3.2 的 `Fourier coefficients` 写作 `Fourier coeficients`；`effort` 写作 `efort`。指数映射原文为 `exp: \mathfrak g \to G`，Markdown 漏掉箭头。Theorem 3.1 证明结尾的空方框 `□` 被写成 U+0003；300dpi 裁片确认方框应保留。
- 核验时间：2026-10-01 20:00 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.027（PDF p.27 / 印刷 p.27）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p027.png`（pngmono 150dpi）；等变关系裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p027_measure-equivariance.png`（PDF p.27，pnggray 300dpi）。
- 核对：PDF p.27 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 740–784 行），覆盖周期轨道测度 (3.9)、混合/等分布估计 (3.10)–(3.11)、Theorem 3.2 与其证明开头。
- 结果：FAIL。
- 差异：PDF 将矩阵系数估计标为 (3.10)，轨道等分布估计标为 (3.11)；Markdown 在 (3.10) 标签后又把第一式标作 (3.11)，第二式未标号。条件中的 `o` 被录成 `i f o`，多出 `i f`；多项式映射 `\mathbb R \to \operatorname{End}(\mathfrak g)` 漏掉 `\to`。`Fourier coefficients` 在句中拼成 `Fourier coeficients`。300dpi 裁片还确认 \(\overline{\psi(u)}\) 的横线确实存在，Markdown 对此录写正确，不作为差异。
- 源级 print quirk：PDF 原句为 “The relevance to this to ‘Fourier coefficients’ …”，Markdown 忠实保留重复的 `to`，不按语法预期删改。
- 核验时间：2026-10-01 20:26 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.028（PDF p.28 / 印刷 p.28）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p028.png`（pngmono 150dpi）；证明结束符裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p028_proof-marker.png`（PDF p.28，pnggray 300dpi）。
- 核对：PDF p.28 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 786–826 行），含公式 (3.13)–(3.15)、Remark 3.2 的 Fourier 系数界和 Remark 3.3。
- 结果：FAIL。
- 差异：公式 (3.14) 的 PDF 第二行是 `\ll H^{-\kappa_1}S_{\infty,\dim(K)}(f)^2`，Markdown 丢掉了该处的 `\ll`。在紧接着 “We choose H ... to conclude” 的证明结尾、Remark 3.2 之前，原页有空方框 `□`，Markdown 中缺失；300dpi 裁片确认其位置。`Fourier coefficients` 在两处分别（aₙ 界处及 Remark 3.3 末段）写成 `Fourier coeficients`，均漏掉第二个 `f`。其余 (3.13) 与 (3.15) 的主体、积分域和误差项相符。
- 核验时间：2026-10-01 20:51 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.029（PDF p.29 / 印刷 p.29）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p029.png`（pngmono 150dpi）。
- 核对：PDF p.29 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 828–848 行），覆盖 Remark 3.3 后半、Remark 3.4、§4 与 Prop. 4.1 开头。
- 结果：FAIL。
- 差异：本页三处 `Fourier coefficients` 相关表述中，首处 Markdown 写成 `Fourier coeficients`，漏掉第二个 `f`。Remark 3.4 的 spectral gap 空间在 PDF 是 `\Gamma\backslash G`，Markdown 丢掉了反斜线而写成 `\Gamma G`。Lp 记号说明后的 Markdown 出现无对应印刷文字的 `Q ∈<sub>` 片段；PDF 页图只见 “Thus, e.g.” 后接范数示例。
- 源级 print quirk：§4 开头原页确实重复印作 “and and X”；Markdown 同样保留，勿据语法预期删除。
- 核验时间：2026-10-01 21:26 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.030（PDF p.30 / 印刷 p.30）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p030.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p030_alpha-ratio.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p030_embeddings.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p030_footnote10.png`（均为 PDF p.30，pnggray 300dpi）。
- 核对：PDF p.30 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 848–890 行），覆盖 Prop. 4.1 的假设与界 (4.1)–(4.2)、经典解释和脚注 8–10；以裁片复核分数/映射箭头和脚注变量。
- 结果：FAIL。
- 差异：嵌入 `Y(p)\hookrightarrow Y(1)\times Y(1)` 的箭头在 Markdown 漏掉；函数映射 `(x_1,x_2)\mapsto f_1(x_1)f_2(x_2)` 被写成向下箭头。短语 `subconvexity for` 被拆写为 `$f o r$`。脚注 10 漏了 `f_1,f_2`（“and f₁,f₂ are everywhere spherical”），并把“all of f₁,f₂,φ are unramified”写成无主语的 “all of are unramified”；300dpi 裁片核实这些原文内容。公式 (4.1)、(4.2) 的支持集、L⁴/L² 范数及主指数结构与印刷相符。
- 复核：Kim 参数“3 / 2 6”和下界“1 / 2 6”位于 TeX 数学环境，忽略空格后分别排作 3/26、1/26；PDF 与 Markdown 数值相同。（更正复核：2026-10-02 05:15 EDT；Peer-P36）
- 核验时间：2026-10-01 22:06 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.031（PDF p.31 / 印刷 p.31）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p031.png`（pngmono 150dpi）。
- 核对：PDF p.31 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 892–916 行），覆盖 Prop. 4.1 证明起始、公式 (4.3)、Ramanujan 估计 (4.4) 及投影说明。
- 结果：FAIL。
- 差异：PDF 写作 `Rankin-Selberg ... standard L-functions`，Markdown 合并成 `Lfunctions`，漏连字符。公式 (4.4) 的 PDF 结构是先对左侧差取绝对值，再以 `≤ 2q^{\alpha-1/2}\|h_1\|_{L^2}\|h_2\|_{L^2}` 作上界；Markdown 把该 `≤` 和右端放进绝对值环境内部，改变了不等式结构。公式 (4.3) 的共轭因子与换序重写同原页相符。
- 核验时间：2026-10-01 22:30 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.032（PDF p.32 / 印刷 p.32）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p032.png`（pngmono 150dpi）；公式裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p032_Hecke-estimates.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p032_lambda-prime.png`（PDF p.32，pnggray 300dpi）。
- 核对：PDF p.32 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 918–966 行），覆盖公式 (4.5)–(4.9)、Hecke 特征值及总变差估计、脚注 11。
- 结果：FAIL。
- 差异：PDF 的 Ramanujan 特征值条件写作 `|λ([ℓ])| ≤ 2`；Markdown 把素理想符号 `ℓ` 错成 `\boldsymbol{\rho}`，300dpi 裁片确认原字形是 `ℓ`。句子 `we denote by λ(n) the nth Hecke eigenvalue` 在 Markdown 多出 `be`。脚注 11 中 (f_1\otimes\chi)、(f_2\otimes\chi) 和 (GL_2(\mathfrak o_{F,\mathfrak p})) 相关条件被拆成多个 page-footnote spans；其主句分别出现 `invariant by if p|n`、`However, always fixes...` 与残缺 `)-span`，无法从连续 Markdown 正文读回 PDF 的完整限制。
- 复核：300dpi 公式裁片确认 (4.7)–(4.8) 的内外绝对值层次与积分测度相符，故未列为差异。原页在 `\varphi\star\sigma=\lambda\varphi_3` 中确实将小数字 3 印在 φ 后；其意图在单页证据下未判定，Markdown 照录并保留未知。
- 核验时间：2026-10-01 23:16 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.033（PDF p.33 / 印刷 p.33）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p033.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p033_sign-choice.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p033_proof-marker.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p033_prop42-conductor.png`（均为 PDF p.33，pnggray 300dpi）。
- 核对：PDF p.33 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 968–1012 行），覆盖 (4.10)–(4.14)、Iwaniec 选系数、Prop. 4.2 参数及脚注 12；裁决 `sign` 共轭、ℓ 记号、命题函数变量和证明结束符。
- 结果：FAIL。
- 差异：素理想条件 `|\lambda([\ell])|\leq2` 在 Markdown 把 `\ell` 误成 `\rho`。`|S|` 前多出点号；“denote by `\lambda(\mathfrak n)` the nth Hecke eigenvalue” 多出 `be`。Prop. 4.2 的函数在 PDF 是普通 `F\in C^\infty(X\times X)`，Markdown 使用 `\mathcal F`；其表示的底域为 `F`，Markdown 写成 `F_z`。式 (4.13) 后 PDF 印有空方框 `□`，Markdown 漏失；300dpi 裁片核实。
- 复核：定义 `a_n` 的两支确有 `\overline{\operatorname{sign}(\lambda(\mathfrak n))}` 共轭横线；公式 (4.7)–(4.8) 中积内/外绝对值层次与 PDF 相符。PDF 原文在 `\varphi\star\sigma=\lambda\varphi_3` 中确有一个小数字 3，Markdown 照录，意图未由本页判定；TeX 数学源码中的 `3 / 2 6` 与 `1 / 1 7` 空格在数学排版中忽略，实际仍分别为 3/26 与 1/17；不作为数值差异。（更正复核：2026-10-02 05:15 EDT；Peer-P36）
- 核验时间：2026-10-02 00:07 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.034（PDF p.34 / 印刷 p.34）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p034.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p034_equation-416.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p034_inner-product-identity.png`（PDF p.34，pnggray 300dpi）。
- 核对：PDF p.34 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1014–1058 行），覆盖 Prop. 4.2 证明、公式 (4.15)–(4.17) 与 Sobolev 范数使用。
- 结果：FAIL。
- 差异：`difference` 在证明首句拼作 `diference`；后文 `coefficients` 的两处都拼作 `coeficients`。解释 `\chi(x)` 的印刷句子 “Here, as before, χ(x) denotes the function … on PGL₂(F)\PGL₂(A_F)” 在 Markdown 被拆成两个独立 display，仅留下 `χ(x)` 与 `g↦χ(det(g))` 碎片，连接词及定义域文字丢失。另，`\|\sigma\|` 在 Markdown 用 `\boldsymbol{\sigma}` 加粗，与原页普通 `\sigma` 字形不符。300dpi 裁片确认 (4.16) 的 `dx_1dx_2` 确在 PDF 中；另一个裁片确认定义恒等式本身按印刷也未显式写测度微分，因此不报为遗漏。
- 核验时间：2026-10-02 00:15 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.035（PDF p.35 / 印刷 p.35）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p035.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p035_prop42-proof-marker.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p035_h-s-formula.png`（PDF p.35，pnggray 300dpi）。
- 核对：PDF p.35 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1060–1086 行），覆盖 Prop. 4.2 结论、§5 应用引言、式 (5.1) 和 Theorem 5.1 开头。
- 结果：FAIL。
- 差异：PDF 句子 “in effect” 在 Markdown 写成 `in efect`。Theorem 5.1 中 “fix t ∈ R” 被破坏为 `\mathcal f x t` 一类字符片段。Prop. 4.2 结尾处 PDF 印有空方框 `□`，Markdown 为 U+0003；300dpi 裁片确认空方框。
- 复核：式 (5.1) 前对 `h(s)` 的定义经 300dpi 裁片确认含外层共轭和 `1-\overline{s}`，Markdown 对应形式相符，不作为差异。
- 核验时间：2026-10-02 00:18 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.036（PDF p.36 / 印刷 p.36）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p036.png`（pngmono 150dpi）。
- 核对：PDF p.36 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1088–1122 行），覆盖 Theorem 5.1 的三项界、隐常数说明、Kim 参数段、§5.1 引言和脚注 13。
- 结果：FAIL。
- 差异：Theorem 5.1 总结中 `differs from the L-function` 漏掉一个 `f`，写成 `difers`。指数 `1/13`、`1/100`、`1/600` 经页图核对与 PDF 一致（Markdown 公式内空格不改变这些分数）。
- 复核：Kim 参数的 TeX 数学源码“3 / 2 6”中的空格被忽略，实际排作 3/26；其数值与 PDF 相同，不应列为差异。（更正复核：2026-10-02 05:15 EDT；Peer-P36）
- 核验时间：2026-10-02 00:20 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.037（PDF p.37 / 印刷 p.37）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p037.png`（pngmono 150dpi）；证明结束符裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p037_proof-marker.png`（PDF p.37，pnggray 300dpi）。
- 核对：PDF p.37 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1124–1176 行；line 1174 跨至 p.38），覆盖 Prop. 5.1 两种积分表示、逐项条件和证明收据。
- 结果：FAIL。
- 差异：有限 Schwarz–Bruhat 函数集合在 PDF 明确命名为 `\mathcal F`，Markdown 在“fixed finite set …”处漏掉该标识，后文 `\Psi\in\mathcal F` 才出现。`\operatorname{Cond}(\pi_\infty)` 中的 `\pi_\infty` 被 Markdown 加下划线；dual `\widehat{\operatorname{PGL}_2(F_\infty)}` 的 hat 分组也被拆开。条件 (1) 的英文连接词 `and` 在 Markdown 被拆成 `a n d`；条件 (2) 的 `\operatorname{PGL}_2(\mathfrak o_{F_v})` 后多出 `\mathrm{~}`；条件 (3) 的 `\|\varphi\|_{L^2(X)}` 被写成 `k^{\varphi}k`。证明末尾 PDF 印有 `□`，Markdown 未记录，300dpi 裁片确认。
- 源级 print quirks：该页原文拼作 “Schwarz function” 与 “Schwarz Bruhat functions”（未加 `t`），Markdown 一致照录；不按常见术语拼法回改。
- 页界：基线 Markdown 第 1174 行在本页停于 “We begin by remarking that”，其后到有限导子比较的续句归 p.38 核对。
- 核验时间：2026-10-02 00:24 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.038（PDF p.38 / 印刷 p.38）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p038.png`（pngmono 150dpi）；脚注裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p038_footnote15.png`（PDF p.38，pnggray 300dpi）。
- 核对：PDF p.38 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1174–1240 行），覆盖 Proposition 5.1 后续、函数 `I(s)`、估计 (5.6)–(5.9) 及脚注 15。
- 结果：FAIL。
- 差异：功能方程记号 `\Lambda` 后 Markdown 多出分号下标；两处“rapid decay as `\Im(s)\to\infty`”在 Markdown 漏掉趋于箭头；`\ll_\epsilon N(\mathfrak p)^{\kappa+\epsilon}` 的 `\ll_\epsilon` 后又多出一个游离 `\epsilon`。脚注 15 被拆散在多条 page-footnote spans：`\sum_g` 只剩下标 `g`，`N\log(N)^3` 被拆成 `N` 与残缺 `g(N)^3`，`t\ne0` 变为 `t 6=0`，句子无法连续读回；300dpi 裁片确认印刷脚注原式与文本。
- 复核：(5.8)、(5.9) 的 exponent 中 raw TeX 将 `26` 写成 `2 6`，但公式环境会忽略这些空格，页图显示数值为 `1/26`；不把这一空格差异记为数学数值改变。(h(s)=s(1-s)(s-\tfrac12)^2\overline{I(1-\overline{s})}) 与 PDF 相符。
- 核验时间：2026-10-02 00:41 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.039（PDF p.39 / 印刷 p.39）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p039.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p039_integral-factor.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p039_dual-GL2.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p039_proof-marker.png`（均为 PDF p.39，pnggray 300dpi）。
- 核对：PDF p.39 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1242–1291 行），覆盖导数界 (5.10)、(L)-值推导、双变量函数 (I(z_1,z_2))、(5.11)–(5.13) 及 (E_h) 定义。
- 结果：FAIL。
- 差异：(h(s)) 与 (I(s)) 的 rapid-decay 文字将 `\Im(s)\to\infty` 录成 `\Im(s)\infty`，漏掉趋于箭头。对偶空间应为 `\widehat{\mathrm{GL}_2(F_\infty)}`，Markdown 把 hat 分散到 `\mathrm{GL}_2` 与 `F_\infty`。另将 `differentiation` 拼成 `diferentiation`；p.39 的证明末尾印有空方框 `□`，Markdown 编码为 U+0003，300dpi 裁片确认。
- 复核：PDF p.39 的增长界与 MinerU Markdown 均为 `C^{|\Re(t)|+|\Re(t')|}`；该处没有额外乘 `C`，不属于 Markdown 修复项。此前将其列为差异的判断已撤回。
- 源级记法现象：式 (5.11) 首次展开的第二个 Λ 因子在原页未重复写 `\pi`，下一行展开式则显式写出 `\pi`；Markdown 保留两行原有记法，不按上下文补字。
- 页界：line 1291 为本页 `E_h` 定义；随后的应用 Prop. 4.2 文字从 p.40 开始。
- 核验时间：2026-10-02 00:46 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.040（PDF p.40 / 印刷 p.40）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p040.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p040_proof-marker.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p040_beta-notation.png`（PDF p.40，pnggray 300dpi）。
- 核对：PDF p.40 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1294–1342 行），覆盖 Prop. 4.2 导子界、公式 (5.14)、Theorem 6.1、测试向量说明及经典积分 (6.3)。
- 结果：FAIL。
- 差异：`sufficient`、`different`、`suffice`、`Fourier coefficients` 分别出现为 `suficient`、`diferent`、`sufice`、`Fourier coeficients`。Sobolev 指数在 PDF 是 `\max(\beta,d)`，Markdown 对 β 加了点号；300dpi 裁片确认原文为普通 β。式 (5.14) 后证明结尾的空方框 `□` 在 Markdown 中保留为 U+0003，300dpi 裁片核对原页。`horocycles. The general version` 的句点后在 Markdown 少空格。式 (6.1)、(6.2) 的指数分别核为 `1/24`、`1/200`；式 (6.3) 的积分区间及 `dy/y` 与原页相符。
- 核验时间：2026-10-02 00:49 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.041（PDF p.41 / 印刷 p.41）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p041.png`（pngmono 150dpi）。
- 核对：PDF p.41 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1326–1351 行；起始段落跨页，只核对 p.41 上的文字），覆盖 §6 经典说明步骤 (1)–(4)、公式 (6.3)，以及 6.1 节测度定义 (6.4)。
- 结果：FAIL。
- 差异：步骤 (2) 中 `suffice` 漏掉第二个 `f`，`Fourier coefficients` 写成 `Fourier coeficients`。步骤 (3) 的句号后缺空格（`horocycles.The`），原页为 `horocycles. The`。本页 (6.1)、(6.2) 的指数与 (6.3) 的积分测度 `dy/y`、(6.4) 的测度定义核对相符。
- 核验时间：2026-10-02 00:51 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.042（PDF p.42 / 印刷 p.42）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p042.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p042_classical-measure.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p042_L-unram-index.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p042_proof-marker.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p042_reference-notation.png`（均为 PDF p.42，pnggray 300dpi）。
- 核对：PDF p.42 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1354–1394 行；第 1394 行跨至 PDF p.43，本条只核到 p.42 页底的 “depending”），覆盖 §6.1 后续说明、Proposition 6.1 条件及 (6.5)–(6.6)、截断界、证明和 Proposition 6.2 的开头。
- 结果：FAIL。
- 差异：经典解释中的 μ_z(f) 原页为 \(f(x/q+iz)\chi(x)\)，Markdown 改成 \(f(x/q+\overline{iz})\overline{\chi}(x)\)，多出两个共轭；300dpi 裁片确认。定义 \(L_{\mathrm{unr}}\) 的乘积指标，原页为 \(\prod_{\chi_v\ \mathrm{unram.}}\)，Markdown 写成 \(\prod_{\chi,\mathrm{unram.}}\)，漏掉局部下标 \(v\)；裁片确认。Proposition 6.1 证明后原页有空方框 \(□\)，Markdown 漏掉；裁片确认。提及 (10.9) 时原页为普通字体，Markdown 将编号加粗为 `\boldsymbol{10.9}`；裁片确认。
- 复核：公式 (6.5)、(6.6) 与两条截断估计的主体、指数和导子因子均与原页相符。p.42 上 Proposition 6.2 只核到行末 “depending”；后续文字及公式属于 p.43。
- 核验时间：2026-10-02 01:10 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.043（PDF p.43 / 印刷 p.43）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p043-43.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p043_equation-68.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p043_quoted-phi.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p043_proof-marker.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p043_invariant-product.png`（均为 PDF p.43，pnggray 300dpi）。
- 核对：PDF p.43 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1394–1444 行；第 1394 行从 p.42 跨页，仅核本页续文），覆盖 Proposition 6.2、估计 (6.8)、§6.2 开头、主定理证明起始和脚注 16。
- 结果：FAIL。
- 差异：提及 (10.9) 时原页为普通字体，Markdown 将编号加粗为 `\boldsymbol{10.9}`。Proposition 6.2(1) 的 `and` 在公式行被拆成 `a n d`；(4) 的 “for each¹⁶ K ≥ 1” 被拆成带数学间距的 `e a c h ^ {16}`，脚注正文仍保留。证明估计的经典集合 \(\{x/q+iz\}_{0\le x\le q-1}\) 后，Markdown 多出 `2` 并拆坏 `if z` 的数学定界符。估计 (6.8) 的不变子群乘积印为 \(\prod_{\mathfrak q} K_0[\mathfrak q^{s_{\mathfrak q}}]\)，Markdown 写成 \(\Pi_{\mathfrak q} K_0[\mathfrak q^{s_{\mathfrak q}}]\)；300dpi 裁片确认原页是乘积符号。Proposition 6.2 证明末尾的空方框 \(□\) 在 Markdown 缺失；裁片确认。主定理证明中的 `the “ϕ” of Prop. 6.1` 被损坏为 `^{66} \varphi ^{,5}`；300dpi 裁片确认印刷只有引号包围的 \(\varphi\)。同段集合名原页为大写 \(S\)（印刷为花体字形），Markdown 写成小写 `s`。
- 复核：估计 (6.8) 的积分项、`max(qz,1/(qz))`、幂次和 Sobolev 因子与原页一致；(6.7)、Proposition 6.2(2)–(4) 的主体界与不变性陈述也核对相符。脚注 16 的正文在 Markdown 中保留。
- 页界：第 1394 行从 Proposition 6.2 的开头跨页；该行 p.43 部分自 “only on F)” 起。第 1444 行脚注 16 为本页页底内容。
- 核验时间：2026-10-02 01:10 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.044（PDF p.44 / 印刷 p.44）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p044-44.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p044_equation-610.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p044_equations-612-613.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p044_invariance-kappa.png`（均为 PDF p.44，pnggray 300dpi）。
- 核对：PDF p.44 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1446–1488 行），覆盖测度 \(\sigma\) 与 (6.9)、平滑截断 (6.10)–(6.11)、Cauchy–Schwarz 估计 (6.12) 及 Sobolev 界 (6.13)。
- 结果：FAIL。
- 差异：原页称 \(f\star\sigma\) 对 \(K_0[\mathfrak q^{s_{\mathfrak q}}]\) 不变的条件为每个 \(\mathfrak q\mid\mathfrak m\)；Markdown 写成 “for each q m”，漏掉整除符号。`For each prime ideal ... ∈ S, let` 中 Markdown 在 `S` 后插入句点。参数 \(\kappa\) 的引文为 “slightly smaller than 1,”；Markdown 在逗号后增加 `\dag`，300dpi 裁片确认原页无该符号。
- 复核：(6.9)–(6.13) 的求和指标、卷积测度、积分分解、Sobolev 范数次序及指数结构均与原页相符；(6.10) 第一项和 (6.12) 左侧原页本身未显式写 \(d^{\times}z\)，Markdown 对应一致，不列作差异。
- 源级 print quirk：原页与 Markdown 均在 “a geometric version of the approximate functional equation).” 中保留了多余右括号；照录原文。
- 核验时间：2026-10-02 01:18 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.045（PDF p.45 / 印刷 p.45）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p045-45.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p045_proof-marker.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p045_h-definition.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p045_footnotes17-18.png`（均为 PDF p.45，pnggray 300dpi）。
- 核对：PDF p.45 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1490–1542 行），覆盖 (6.14)–(6.17)、Theorem 6.1 收尾、§6.3 起始及脚注 17–18。
- 结果：FAIL。
- 差异：Theorem 6.1 证明结尾原页印有空方框 \(□\)，Markdown 以 U+0003 代替；300dpi 裁片确认。`with κ′, the norm` 在 Markdown 的 κ′ 后多出句点。关于 \(h\) 的句子，Markdown 在数学定界符内的 `h ,` 后又接正文逗号，形成双逗号；后文 \(\operatorname{Cond}_{\infty}(\chi)\cdot q\) 的乘法点被写成普通句点，并把句末点也放进数学定界符。页脚 17 的正文在 Markdown 漏掉 “constant term of f” 中的 \(f\)，而 `f,` 被拆为孤立 page-footnote span；另有与本页印刷内容无对应的孤立 `X` span。行末脚注 17 标记在正文中是普通 `17`，原页排为上标。
- 复核：式 (6.14)–(6.17) 的主体、积分域、共轭与权重因子同原页相符；尤其 \(h=(s-\tfrac12)^2s(1-s)\overline{I(1-\overline{s})}\) 的双重共轭经裁片确认。原页 \(\alpha=3/26\)，Markdown 数学环境中的 `3 / 2 6` 忽略空格后亦为 3/26，不列为数值差异。脚注 18 正文保留。
- 源级 print quirk：正文 “we remark that that this is ‘almost’ obvious” 在 PDF 与 Markdown 中均有重复 `that`；保留印刷原文。
- 核验时间：2026-10-02 01:23 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.046（PDF p.46 / 印刷 p.46）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p046-46.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p046_quoted-h.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p046_6-20-convexity.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p046_proof-marker.png`（均为 PDF p.46，pnggray 300dpi）。
- 核对：PDF p.46 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1544–1580 行），覆盖 (6.18)–(6.20)、非尖点情形估计的结尾、(6.2) 推论和 §7 引言。
- 结果：FAIL。
- 差异：原文将 (6.10) 前定义的对象引作带引号的 `“h”`，Markdown 损坏为 `^{66} h^{\prime\prime}`；300dpi 裁片确认是引号，不是上标或双撇。`sufficiently` 漏掉第二个 `f`，并把 `N:` 的冒号放入数学定界符。§7 首段的 `different flavor` 在 Markdown 写为 `diferent flavor`，漏掉 `f`。关于 \(L(1/2,\chi)\) 的结论后，原页有空方框 \(□\)，Markdown 用 U+0003 代替；裁片确认。
- 复核：(6.18)–(6.20) 的积分、Sobolev 因子、导子项和幂次均与原页相符。Markdown 数学环境中的 `24 / 25` 与 `1 / 200` 忽略空格后分别为原页 \(24/25\) 与 \(1/200\)，不列作数值差异。
- 源级 print quirk：凸性估计的被积式在 PDF 印作 `|L(1/2+it,χ)|L(1/2-it,χ)|^2|Φ|^2` 这一绝对值竖线次序；Markdown 同样照录，本页不据预期改写它。
- 核验时间：2026-10-02 01:27 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.047（PDF p.47 / 印刷 p.47）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p047-47.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p047_extension-torus.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p047_map-norm.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p047_theorem-limit.png`（均为 PDF p.47，pnggray 300dpi）。
- 核对：PDF p.47 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1582–1612 行），覆盖 §7.1 的 Heegner 点定义、映射 \(\mathscr H\)、Theorem 7.1 及 §7.2 开头。
- 结果：FAIL。
- 差异：PDF 为 \(E=F(\sqrt{-\mathbf d})\)，Markdown 给 \(E\) 加了点号成为 `\dot{E}`；定义环面时，Markdown 在 `\operatorname{Res}` 后插入乘点，原页没有该符号。映射定义原文为 \(\mathscr H:T_E(\mathbb A_F)/T_E(F)\to\mathbf X\)，Markdown 使用 \(\mathcal H\) 且漏掉 \(\to\)。下一句中的 \([\mathbf d]_\infty\) 原页直接包含于两个 \(\operatorname{PGL}_2\) 群之间，Markdown 多加 \(\Gamma\)。范数公式原页为 \(\mathrm N(\mathbf d)=|\mathfrak o_F/\mathbf d\mathfrak o_F|\)，Markdown 把 \(\mathfrak o_F\) 误录为 \(\pmb\sigma_F\)；300dpi 裁片确认。`F-torus` 被录作带下标负号的 `F_-`-torus。Theorem 7.1 的 “measures \(\nu_E\)” 漏掉下标 \(E\)，`N(d) → ∞` 漏掉趋于箭头；裁片确认。`effective rate` 被拼作 `efective rate`。Markdown 在 \(\mathbb Q\) 后录成 `Q..`，比原页多一个句点。
- 复核：式 (7.1)、(7.2)、Theorem 7.1 的误差界主体及 §7.2 中 \(E_i=F(\sqrt{\mathbf d_i})\) 与原页相符；本页只记录上述可见差异。
- 核验时间：2026-10-02 01:31 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.048（PDF p.48 / 印刷 p.48）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p048-48.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p048_weight-proof.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p048_H-measures.png`（均为 PDF p.48，pnggray 300dpi）。
- 核对：PDF p.48 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1614–1644 行），覆盖 §7.2 的 split-prime 条件、Theorem 7.2 及证明开头至 (7.4) 和脚注 19。
- 结果：FAIL。
- 差异：两处 `different` 均漏掉 `f`，写成 `diferent`。脚注 19 在原页紧接 `Rankin-Selberg L-functions` 后以上标标记，Markdown 将 `19` 作为正文数字直接接在句末；脚注正文虽保留。`fixed prime of F.` 后，Markdown 在 `F` 后录入双句点。权重函数定义中原页为 \(\mathrm N(\mathfrak q)\)，Markdown 把变量录成 \(P\)。定理证明里 “Let \(\mathcal S\) be the set” 的 \(\mathcal S\) 在 Markdown 遗失；同段 \(T_E(\mathbb A_F)\)-flow 被拆成 `-\mathbb A ow`。原页对 \(\Upsilon_q(\varpi_q)\) 的文字明确为 valuation \(\pm1\)，Markdown 只录 `1`；300dpi 裁片确认。测度定义、卷积关系及 (7.3)–(7.4) 中原页的脚本体 \(\mathscr H\) 多处被 Markdown 写成 \(\mathcal H\)；裁片确认。
- 复核：Theorem 7.2 的分母、收敛箭头与 (7.3)–(7.4) 的指数、范数项主体均与原页相符；脚注 19 内容保留。
- 核验时间：2026-10-02 01:36 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.049（PDF p.49 / 印刷 p.49）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p049-49.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p049_size-notation.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p049_H-integral.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p049_proof-marker.png`（均为 PDF p.49，pnggray 300dpi）。
- 核对：PDF p.49 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1646–1687 行），覆盖 (7.5)–(7.6)、Theorem 7.2 结尾、§8 开头及 Remark 8.1(1)–(4)。
- 结果：FAIL。
- 差异：原页 “the set \(\mathcal S\) has size” 中的集合名在 Markdown 写成小写 `$s$`。求和后替换 \(|\mathcal S|=\mathrm{wt}(E_i,\delta_1)\) 时，原页仍使用花体 \(\mathcal S\)，Markdown 改成粗体 \(\boldsymbol S\)。式 (7.6) 的被积函数使用脚本体 \(\mathscr H(t)\)，Markdown 写成 \(\mathcal H(t)\)；300dpi 裁片确认。`sufficiently` 漏掉第二个 `f`。Theorem 7.2 结尾原页有空方框 \(□\)，Markdown 以 U+0003 代替；裁片确认。
- 复核：(7.5)–(7.6) 的范数、指数、积分域与余项主体及 Remark 8.1(1)–(4) 的公式/条件均与原页相符。
- 核验时间：2026-10-02 01:39 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.050（PDF p.50 / 印刷 p.50）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p050-50.png`（pngmono 150dpi）。
- 核对：PDF p.50 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1690–1742 行），覆盖 Remark 8.1(4) 结尾、Lemma 8.1 的乘积估计及证明、(8.1)–(8.2)，和 Lemma 8.2 及其证明。
- 结果：FAIL。
- 差异：Lemma 8.1 的证明开头，原文为 “For any monomial \(\mathcal D\) of degree d in \(\mathcal B\)”；Markdown 在 “monomial” 后与 “in” 后均漏掉符号。随后总结 (8.2) 时原文说三处求和指标 \(\mathcal D\) 遍历 \(\mathcal B\) 中次数 \(\le d\) 的单项式；Markdown 漏掉 \(\mathcal D\)，并把花体 \(\mathcal B\) 写成粗体 \(\boldsymbol B\)。Lemma 8.1 证明末尾的空方框在 Markdown 缺失；Lemma 8.2 证明末尾的空方框被 U+0003 替代。
- 复核：(8.1)、(8.2) 的积分域、求和范围与 (L^p/L^{2p}) 范数，Lemma 8.1 最终 Sobolev 界，以及 Lemma 8.2 的群作用、子群指数和范数幂次与原页相符。
- 核验时间：2026-10-02 01:42 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.051（PDF p.51 / 印刷 p.51）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p051-51.png`（pngmono 150dpi）。
- 核对：PDF p.51 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1744–1795 行），覆盖 Lemma 8.3 插值界、§8.1.1 的 Kirillov 模型说明、(8.3)–(8.4) 及 Lemma 8.4 的实/复数域界。
- 结果：FAIL。
- 差异：Lemma 8.3 的括号说明后，Markdown 多出 `\jmath`，PDF 原页仅以右括号结束。Lemma 8.3 证明末尾原页有空方框，Markdown 漏掉。在 Lemma 8.4 实数情形的单项式基句中，Markdown 在 `Lie(GL_2(F_v))` 后多一个右括号。原页证明式印作导数 \(d^j f/d^j y\)，Markdown 同样照录，此处不按常见排版预期改动。
- 复核：(8.3)、(8.4) 的变量、积分域、导数阶次，及 Lemma 8.4 实/复数域估计中的导子幂、权函数与求和范围均与原页相符。
- 核验时间：2026-10-02 01:44 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.052（PDF p.52 / 印刷 p.52）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p052-52.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p052_casimir.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p052_reduction-maps.png`（均为 PDF p.52，pnggray 300dpi）。
- 核对：PDF p.52 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1798–1836 行），覆盖 Lemma 8.4 的证明及 8.2 reduction theory 定义、(8.5)–(8.6) 和高度函数构造。
- 结果：FAIL。
- 差异：局部导子因子原文为 \(\operatorname{Cond}_v(\pi_v)^2\)，Markdown 在 \(\pi_v\) 上加了共轭横线。Casimir 推导原文写 \(efv=\tfrac12(\lambda+h-h^2)v\)，Markdown 损坏成 \(\mathcal I v=\tfrac12(\bar\lambda+h-h^2)v\)；300dpi 裁片确认两个符号差异。`differential` 两处漏掉 `f`，写成 `diferential`；句子 `where ...` 前的逗号误成句点；`R` 句后缺少句点，导致 “A similar proof” 紧接在公式变量之后。Lemma 8.4 证明末尾的空方框被 U+0003 代替。Reduction theory 段落在 `Given g∈GL₂(A_F)` 后多一个右括号；高度函数的两个映射目标中，Markdown 分别漏掉 \(\to\)：\(B(F)\backslash GL_2(\mathbb A_F)\to\mathbb R_{>0}\) 和 \(GL_2(F)\backslash GL_2(\mathbb A_F)\to\mathbb R\)。两处 `sufficiently` 漏 `f`。
- 复核：(8.5)–(8.6) 的行列式、有限/无限处范数及分母乘积与原页一致；高度函数分段定义与最终 \(\mathbf X\to\mathbb R_{\ge T_0}\) 映射也核对相符。
- 核验时间：2026-10-02 01:47 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.053（PDF p.53 / 印刷 p.53）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p053-53.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p053-indexes.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p053-Omega-u.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p053-Lemma86-gamma.png`（均为 PDF p.53，pnggray 300dpi）。
- 核对：PDF p.53 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1838–1868 行），覆盖 Lemma 8.5 及其证明、(8.7)–(8.8)、Lemma 8.6 开头至行末范数映射陈述。
- 结果：FAIL。
- 差异：`suffice` 在两处分别误作 `sufice`、`sufices`；`affect` 漏掉 `f`。第一处 `for each g∈\mathfrak S(T), that` 后多一个右括号。`g=a_g k'_g, where` 中 Markdown 在 \(k'_g\) 后多录分号。下一行 \(a_g^{-1}a_\gamma n_\gamma a_g\) 被误为 \(a_q^{-1}a_\gamma n_\gamma a_g\)；300dpi 裁片确认原页下标为 g。计数结果 `O(ht(x)) distinct cosets` 前 Markdown 多一个右括号。\(\Omega'\) 只依赖于 \(U\)，Markdown 给 \(U\) 加了点号。Lemma 8.6 开头的固定参数原页是 \(\gamma\)，Markdown 多加下标 i。Lemma 8.5 证明结尾的空方框被 U+0003 代替。
- 复核：(8.7)–(8.9) 的关系式、紧集包含、\(\beta\) 取值范围及 \(\operatorname{ht}(g)\) 估计主体与原页相符；Lemma 8.6 本页后续在下一页继续。
- 核验时间：2026-10-02 01:51 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.054（PDF p.54 / 印刷 p.54）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p054-54.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p054_decomposition.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p054_normalization.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p054_projective-pair.png`（均为 PDF p.54，pnggray 300dpi）。
- 核对：PDF p.54 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1868–1909 行；第 1868 行由 p.53 跨页），覆盖 Lemma 8.6 证明收尾、Lemma 8.7 陈述/证明开头及 (8.12)–(8.13)。
- 结果：FAIL。
- 差异：紧集分解原页使用普通 \(P\) 和局部整数环 \(\mathfrak o_{F,v}\)；Markdown 将 \(P\) 写成 \(\mathcal P\)，把 \(F\) 写成 \(\mathcal F\)，并将 \(\mathfrak o\) 误作粗体 \(\vartheta\)；300dpi 裁片确认。Lemma 8.6 证明后原页空方框在 Markdown 缺失。`K_{\max}` 后，Markdown 在逗号前多录句点；“\(Z(F)\)-coset”中的连字符也被误成句点。Lemma 8.7 开头 `independent of g.` 后出现重复句点。`difficult`、两处 `sufficiently`、`affect` 分别误作 `dificult`、`suficiently`、`afect`；`suffices` 漏第二个 `f`，写作 `sufices`。证明中 \(\mathfrak S(T_0)\to\mathbf X_{\mathrm{GL}(2)}\) 被录成 \(\Im(T_0)\mathbf X_{\mathrm{GL}(2)}\)，丢掉 \(\mathfrak S\) 并漏箭头；`replacing g by gz` 则带有多余的下标标记。式 (8.13) 前的 \(F^2\) 后，Markdown 多出一个 `2`。
- 复核：式 (8.12)–(8.13) 的高度公式、局部范数和项目化计数条件主体同原页相符。原页 “the result also be deduced” 保留该印刷句法，不按语法预期改写。
- 核验时间：2026-10-02 01:56 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.055（PDF p.55 / 印刷 p.55）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p055-55.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p055_ideals.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p055_norm-principal.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p055_lattice-count.png`（均为 PDF p.55，pnggray 300dpi）。
- 核对：PDF p.55 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1912–1946 行），覆盖有界代表元替换、理想类代表、(8.14)–(8.15) 及格点计数估计。
- 结果：FAIL。
- 差异：嵌入 \(\mathbb R_{>0}\to\mathbb A_{\mathbb Q}^{\times}\to\mathbb A_F^{\times}\) 中，Markdown 把 \(\mathbb Q\) 写成 \(\mathbb O\)；“compact subset \(\Omega\subset\mathbb A_F^{\times}\)”又误用 \(\in\)。原页类群代表 \(\widetilde{\mathfrak J}_i\) 的 tilde 在 Markdown 丢失，并在若干后续位置把 \(\mathfrak J_i\) 误成 \(\mathfrak I_i\)。理想 \(c\mathfrak o_F+d\mathfrak o_F\) 中的 \(\mathfrak o_F\) 多次被录成粗体零 \(\pmb 0_F\)；有限处 \(\mathfrak o_{F,v}\) 也误成粗体 \(\vartheta_{F,v}\)。代表元句中原页一个分号，Markdown 重复录入两个。式 (8.14) 后的范数结论原页为 \(\mathrm N((c))^2\le Y^{-1}|x|_{\mathbb A}^{-1}\)，Markdown 在括号上加横线且给两个负号加点。无限处的 \(|x|_v\) 被写成 \(|x|_{\imath}\)。`unaffected` 两处漏 `f`；`suffice/suffices` 四处漏 `f`。末段晶格所取的 \(\mathfrak J_i\) 也在 Markdown 误录为 \(\mathfrak I_i\)。
- 复核：(8.14)–(8.15) 的求和范围、无限处乘积和界的幂次结构与原页相符；本条列出其间符号和值域的可见偏差。
- 核验时间：2026-10-02 02:01 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.056（PDF p.56 / 印刷 p.56）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p056-56.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p056_matrix-coefficient.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p056_proof-marker.png`（均为 PDF p.56，pnggray 300dpi）。
- 核对：PDF p.56 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1948–1978 行；第 1978 行在 “an easy computation shows” 处跨到 p.57），覆盖 (8.15) 推导收尾、(8.11) 的高度界、§9 引言和矩阵系数界 (9.1) 的开头证明。
- 结果：FAIL。
- 差异：分箱论证原页为 \(\prod_i(1+M_i)\ll T\)，Markdown 写成 \(\Pi_i(1+\dot M_i)\ll T\)，将乘积符号改为大写 Pi 并给 \(M_i\) 加点。Lemma 8.7 的证明结尾原页有空方框，Markdown 漏掉；300dpi 裁片确认。`coefficients` 在 §9.1 标题及下一段各漏掉一个 `f`，写成 `coeficients`。
- 复核：每个主理想对应的 \((Y^{-1/2}|x|_{\mathbb A}^{1/2})^{1+\epsilon}\) 计数界、主理想数界、(8.11) 的 \(T^{-1}\) 上界以及 (9.1) 的维数和增长因子与原页相符。
- 源级 print quirk：(9.1) 的内积在 PDF 原样排为 `\langle \pi(a(x)w_1,w_2\rangle`，左圆括号没有对应右括号；Markdown 保留此印刷形式，不按预期修补。
- 核验时间：2026-10-02 02:06 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.057（PDF p.57 / 印刷 p.57）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p057-57.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p057_equation-94.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p057_equation-95.png`（均为 PDF p.57，pnggray 300dpi）。
- 核对：PDF p.57 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 1978–2012 行；第 1978 行承接 p.56，第 2012 行在 p.57 页底结束于 “elementary estimate”），覆盖 (9.1) 论证续段、(9.2)–(9.5)、§9.1.2 的 Sobolev 推广引言。
- 结果：FAIL。
- 差异：本页续段中的 `matrix coefficients` 两处均拼成 `coeficients`；§9.1.2 中的 `effective mixing` 拼成 `efective mixing`。描述 \(V\subset L^2(\Gamma\backslash SL_2(\mathbb R))\) 时，Markdown 在右括号后多一个 `)`。式 (9.4) 的 Markdown 除正确编号 (9.4) 外还多带 `\tag{3.4}`。式 (9.5) 的二重和项 \(\|f_1^{(n)}\|_2\|f_2^{(m)}\|_2\) 中，Markdown 漏掉第二因子的下标 2；300dpi 裁片确认。
- 复核：(9.2)–(9.3) 的投影算子、子群指数与范数因子，以及 (9.5) 右端分离求和后的 \(f_1,f_2\) 两个因子同原页一致。
- 源级 print quirk：(9.4) 在 PDF 中可见 \(\pi\) 后的左括号未被配对闭合；Markdown 保留该印刷形式，不凭预期补括号。
- 核验时间：2026-10-02 02:11 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.058（PDF p.58 / 印刷 p.58）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p058-58.png`（pngmono 150dpi）。
- 核对：PDF p.58 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2012–2054 行；第 2012 行接续 p.57，第 2054 行在 “Indeed, it” 后跨至 p.59），覆盖 (9.6)、§9.2 定义、Lemma 9.1 的 (9.7)–(9.9) 及证明至本页底。
- 结果：FAIL。
- 差异：Lemma 9.1 证明中的 “the measure on \(\mathbf X\), where the constant C depends only on U” 在 Markdown 把逗号写成句点，变成 “measure on X. where…”。本页物理页底内的 `sufficiently` 漏掉第二个 `f`；同一句续至 p.59 的 `suffices` 归 p.59 记录。其余 (9.6)–(9.9) 的范数、积分和高度因子与原页相符。
- 源级 print quirk：原页在 “Note that in (9.6) that the factor …” 中重复 `that`，Markdown 忠实保留。
- 核验时间：2026-10-02 02:15 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.059（PDF p.59 / 印刷 p.59）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p059-59.png`（pngmono 150dpi）。
- 核对：PDF p.59 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2054–2090 行；第 2054 行从 p.58 跨页），覆盖 Lemma 9.1 证明收尾、Lemma 9.2 全文及 Lemma 9.3 全文。
- 结果：FAIL。
- 差异：续接 Lemma 9.1 时，原文 `suffices` 被写为 `sufices`。对 \(F_\infty/\Lambda\) 上函数定义 \(\|G\|_{(i)}\) 的句子，原文为 “where \(\mathcal D\) varies over all monomials …”，Markdown 在 “where” 后漏掉 \(\mathcal D\)。Lemma 9.2 的格 \(\Lambda\) 定义及关于 \(\Omega\) 的句子中均出现重复逗号。后续范数估计原文为 \(\operatorname{ht}(x)^{-k}(\operatorname{ht}(x)^{1/p}PS_{p,d'}(f))\)，Markdown 把 `ht` 的字母 `h` 拆成独立的 `h` 后再接 \(\mathrm t(x)\)，且在 \(d'\gg1\) 后漏掉句点。Lemma 9.1、9.2、9.3 三个证明结束处的空方框均在 Markdown 中被 U+0003 替代。
- 差异（续）：Lemma 9.3 证明把 `Applying` 拆成公式中的 `A` 与后续 `pplying`，并把 `Df, for D` 的逗号误成句点；`sufficiently` 在定理句和证明句中均漏 `f`。三处 proof marker 均可见于原页图。
- 复核：Lemma 9.1 的第二个积分界、Lemma 9.2 的高度指数与 Sobolev 参数，以及 Lemma 9.3 的 \(3/2\) 指数和投影范数不等式与原页相符。
- 核验时间：2026-10-02 02:21 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.060（PDF p.60 / 印刷 p.60）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p060-60.png`（pngmono 150dpi）。
- 核对：PDF p.60 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2092–2126 行；第 2126 行跨至 p.61，本条核至 “When we flow this”），覆盖 §9.3 引言、§9.3.1 假设、Lemma 9.4 和证明的平滑截断设置。
- 结果：FAIL。
- 差异：§9.3 首句在 `semisimple group` 后 Markdown 用冒号替代逗号；`equidistribution of U-orbits` 被拆成带双连字符的 `U --orbits`。`effective` 两处分别误为 `Efective`、`efective`，`different context` 漏 `f` 写成 `diferent context`。Lemma 9.4 的 `x_0∈\Gamma\backslash SL_2(\mathbb R)` 后，Markdown 多出一个右括号。
- 复核：Lemma 9.4 的假设、(9.11) 的误差指数与 Sobolev 范数，以及 (g_\delta\) 和 \(\mu_\delta\) 的积分定义均与原页相符。
- 核验时间：2026-10-02 02:25 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.061（PDF p.61 / 印刷 p.61）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p061-61.png`（pngmono 150dpi）。
- 核对：PDF p.61 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2126–2176 行；第 2126 行承接 p.60，第 2176 行在 “sum of all” 后跨至 p.62），覆盖 Lemma 9.4 证明主体、(9.12)–(9.15)、优化步及 §9.3.2 开头。
- 结果：FAIL。
- 差异：矩阵 `coefficients` 在本页漏掉第二个 `f`，写成 `coeficients`。Lemma 9.4 证明结束处原页有空方框，Markdown 漏掉。§9.3.2 句尾的 `as y → 0` 在 Markdown 漏掉趋于箭头。定义半单群的段落中，原页将 Lie 代数记为花体 \(\mathfrak g\)，将其负根空间和记为 \(\mathfrak u\)；Markdown 两处都写成普通字母 `g`、`u`。
- 复核：(9.12)–(9.15) 的卷积核、截断误差、Sobolev 因子、指数和最终选取 \(\delta^2=T^{\alpha-1/2}\) 与原页相符。
- 核验时间：2026-10-02 02:28 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.062（PDF p.62 / 印刷 p.62）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p062-62.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p062_tensor-proof.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p062-sobolev-bound.png`（均为 PDF p.62，pnggray 300dpi）。
- 核对：PDF p.62 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2176–2210 行），覆盖 Lemma 9.5 的混合界与证明、闭 horosphere 测度 \(\nu_T\)、Lemma 9.6 的衰减界及平滑核 (9.17)。
- 结果：FAIL。
- 差异：Lemma 9.5 证明中的 `sufficiently` 漏掉 `f`，`in effect` 漏掉第二个 `f`。在“unitary dual of \(\widehat G\)”之后，Markdown 多录一个句点。Lemma 9.5 证明结尾的空方框被 U+0003 替代。Lemma 9.6 函数空间写作 \(C^\infty(\Gamma\backslash\dot G)\)，原页没有 \(G\) 上的点。平滑核导数界中，Markdown 写成带点的 \(\stackrel{\cdot}{\ll}\)，并在指数后多出 `2`；300dpi 裁片确认原页为普通 \(\ll\epsilon^{-l-\dim(G)}\)，没有附加数字。
- 复核：式 (9.16) 的两条相关衰减界、\(\kappa_2\) 定义、\(\nu_T\) 归一化以及 (9.17) 的导数次序与幂次均与原页相符。
- 核验时间：2026-10-02 02:32 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.063（PDF p.63 / 印刷 p.63）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p063-63.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p063_Hecke-ideal.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p063_smoothing-proof.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p063_root-space-text.png`（均为 PDF p.63，pnggray 300dpi）。
- 核对：PDF p.63 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2212–2252 行），覆盖 Lemma 9.6 证明收尾、§9.4 开头、Lemma 9.7 陈述与证明。
- 结果：FAIL。
- 差异：Lemma 9.6 证明结尾原页有空方框，Markdown 缺失。证明中 `suffices` 两处及 `sufficiently` 两处均漏掉 `f`；一个 parenthetical 末尾还多出孤立数字 `0`。Lemma 9.7 将素理想 \(\mathfrak f\) 写成普通 `f`，包括“f an ideal of F”的陈述及证明中两处 \(\mathrm N(\mathfrak f)\)；300dpi 裁片确认原页使用 Fraktur \(\mathfrak f\)。关于 Hecke 轨道随 \(z\to\infty\) 等分布的句子漏掉趋于箭头。Lemma 9.7 证明末尾空方框被 U+0003 代替。
- 源级 print quirk：该证明中原文写作 “Let \(b\) the sum of non-negative root spaces …”，漏掉系词 `be`；Markdown 保留该原印刷句法。
- 复核：式 (9.18)–(9.20) 的卷积、Sobolev 指数及 Hecke 平均项结构与原页相符。
- 核验时间：2026-10-02 02:36 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.064（PDF p.64 / 印刷 p.64）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p064-64.png`（pngmono 150dpi）。
- 核对：PDF p.64 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2254–2298 行；第 2298 行跨至 p.65），覆盖 Lemma 9.8 陈述/证明、(9.21)–(9.22) 及 §9.4 的 p-adic 轨道引言。
- 结果：FAIL。
- 差异：Y(p) 等分布的极限 `p → ∞` 在 Markdown 漏掉趋于箭头。Lemma 9.8 条件句中的 `invariant. Then` 在 Markdown 少了句点后的空格；说明 “PGL₂(...)-invariance” 时，原页使用连字符，Markdown 错录为句点。Lemma 9.8 证明末尾原页有空方框，Markdown 未记录。页末对 p-adic 轨道的说明中，`e.g. p-adic` 被录成双句点，且 “when p varies” 的 p 前多出上标 `66`。
- 复核：(9.21)、(9.22) 的积分域、Hecke 平均、投影与 (N(\mathfrak q)^{(2\alpha-1)/p+\epsilon}) 界的主体均与原页相符。
- 核验时间：2026-10-02 02:44 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.065（PDF p.65 / 印刷 p.65）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p065-65.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p065_lemma99-ideals.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p065_eta-definitions.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p065_eta-q-definition.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p065_footnote20.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p065_mu-subscript.png`（均为 PDF p.65，pnggray 300dpi）。
- 核对：PDF p.65 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2298–2362 行；第 2298 行承接 p.64），覆盖 Lemma 9.9、(9.23)–(9.25)、古典 Hecke 轨道说明及脚注 20。
- 结果：FAIL。
- 差异：Lemma 9.9 中的素理想 \(\mathfrak f\) 在陈述和若干 `\mathfrak q\mid\mathfrak f` 条件里被写成普通 `f`，且多处丢掉整除符号。局部定义 \(\tilde\eta_q=\delta_{a(\varpi^{-e_q})}\star\sigma_q\) 中，Markdown 把 \(\varpi\) 录成 \(\mathfrak w\)，并在 \(K_0[\mathfrak q^{s_q}]\) 的两侧因子前加入点号/错误字形；裁片确认。古典说明中的 \(\{z+i/p\}_{0\le i\le p-1}\) 在 Markdown 将公式拆开，集合下标不再作为下标附着于闭括号。脚注 20 被拆为许多孤立 page-footnote spans；变量、树的顶点距离、两个集合之间的关系以及 Iwasawa 分解等语句在合并文本中丢失或错序，无法从 Markdown 的脚注正文连续读回印刷说明。
- 复核：式 (9.23) 的导子/范数因子与截断项，式 (9.24)–(9.25) 的两项 Hecke 测度关系，以及 \(s_q\ge1\) 的概率测度定义主体同原页相符。原页与 Markdown 都印作 “as as follows”，保留源级重复。
- 核验时间：2026-10-02 02:53 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.066（PDF p.66 / 印刷 p.66）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p066-66.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p066_expansion-sigma.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p066_estimate-930.png`（均为 PDF p.66，pnggray 300dpi）。
- 核对：PDF p.66 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2364–2414 行），覆盖 Lemma 9.9 证明主体、(9.26)–(9.30) 及下一 Lemma 的古典解释。
- 结果：FAIL。
- 差异：式 (9.26) 的 \(\eta_{\mathfrak f}\) 和 \(\tilde\eta_{\mathfrak f}\) 在 Markdown 把理想下标写成普通罗马体 `f`。定义 \(\sigma_S\) 时，原页的 \(\mu_{\mathfrak q^{e_q-1}}\) 被写成 \(\mu_{\mathfrak q^{e_q}-1}\)，把减 1 移到幂外；300dpi 裁片确认。页末的经典空间应为 \(\mathrm{SL}_2(\mathbb Z)\backslash\mathbb H\)，Markdown 在反斜线后多出 `l`。Lemma 9.9 证明结束的空方框由 U+0003 代替。
- 复核：(9.27)–(9.30) 的子集求和、Sobolev/导子因子、高度取最大值和 (9.26) 代回结构均与原页相符。
- 核验时间：2026-10-02 03:04 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。
## p.067（PDF p.67 / 印刷 p.67）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p067-67.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p067_eta-proof.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p067_eta-proof-end.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p067_eisenstein-routing.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p067_eisenstein-prose.png`（均为 PDF p.67，pnggray 300dpi）。
- 核对：PDF p.67 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2416–2452 行），覆盖 Lemma 9.10、(9.31)–(9.32)、§10 引言及 §10.1 基本性质导言。
- 结果：FAIL。
- 差异：Lemma 9.10 的素理想 \(\mathfrak f\) 在正文 “f is an integral ideal” 及若干 \(\mathfrak q\mid\mathfrak f\) 条件中变成普通 `f`，并丢掉整除符号。陈述中的 \(K_0[\mathfrak q^{s_q}]\) 后，Markdown 多出下标 \(\mathfrak i\)。式 (9.32) 后的乘积中，首个局部测度指标被录成重复下标 \(\mathfrak q_{\mathfrak q}^{e_q}\)；原页是 \(\mathfrak q^{e_q}\)，裁片确认。Lemma 9.10 证明结尾空方框缺失。Holomorphic 约定的段落在 `holomorphic in s.` 后，Markdown 插入无对应原文的 \(\mathbf\mu^{\mathfrak s}\)；引文 `Jacquet [17, §19]` 则变成 `[17, 19]`。检验闭曲线积分句中的 `suffices` 漏 `f`。
- 复核：Lemma 9.10 的主估计 (9.31) 和本地平均恒等式 (9.32) 的积分域、归一化、导子幂与截断因子主体同原页相符。
- 核验时间：2026-10-02 03:09 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.068（PDF p.68 / 印刷 p.68）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p068-68.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p068_Eisenstein-formulas.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p068_Schwarz-norm.png`（均为 PDF p.68，pnggray 300dpi）。
- 核对：PDF p.68 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2454–2500 行），覆盖 Schwarz-Bruhat 函数、Schwarz 范数 (10.1)、Eisenstein 级数定义及其 (10.2)–(10.4) 基本性质。
- 结果：FAIL。
- 差异：`constant-coefficients` 与 `differential` 分别漏掉 `f`，写成 `constant-coeficients`、`diferential`。(10.2) 右端原文是 \(f_\Psi(g)\)，Markdown 漏掉下标 \(\Psi\)；Eisenstein 级数定义的求和项原文是 \(f_\Psi(s,\gamma g)\)，Markdown 写成 \(f(s,\gamma g)\)。在极点留数中，原页的积分域 \(\mathbb A_F^2\) 被误作 \(\mathbb A_E^2\)。垂直条带快速衰减句的 Markdown 将 \(1-s\) 分割到两个数学定界符，并破坏绝对值的成对结构。`F^2\subset\mathbb A_F^2` 中的普通 \(\subset\) 被加点。GL₂ 作用的 `GL₂(A_F)-action` 中连字符被写成句点；(10.4) 的 \(h\cdot\Psi\) 中心乘点也被写成句点。
- 复核：变换函数 \(f_\Psi(s,g)\) 的积分核、(10.3) Fourier 变换、函数方程及留数表达式其余部分与原页相符。
- 核验时间：2026-10-02 03:16 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.069（PDF p.69 / 印刷 p.69）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p069-69.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p069_dictionary.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p069_Mellin-integral.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p069_fourier-expansion.png`（均为 PDF p.69，pnggray 300dpi）。
- 核对：PDF p.69 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2502–2540 行；第 2540 行在 “Moreover, without loss of generality” 后跨至 p.70），覆盖 Example 10.1、Remark 10.1、Lemma 10.1、(10.1)–(10.7) 及 Lemma 10.2 证明起始。
- 结果：FAIL。
- 差异：Example 10.1 中 \(F=\mathbb Q\) 被写成花体 \(\mathcal F\)；\(\Psi=\prod_v\Psi_v\) 漏了 \(\Psi_v\) 的下标 v，且有限处最大紧集误录为 \(F_v\) 而漏掉上标 2。描述下降到 \(SL_2(\mathbb R)\) 的函数时，Markdown 在 g 前加了点号。式 (10.2) 右端漏掉 \(f_\Psi\) 的 \(\Psi\) 下标，Eisenstein 级数定义也把 \(f_\Psi(s,\gamma g)\) 写成 \(f(s,\gamma g)\)。极点留数的积分域原页为 \(\mathbb A_F^2\)，Markdown 写成 \(\mathbb A_E^2\)。垂直条带衰减句被 Markdown 拆断数学定界符，破坏 \(|s(1-s)E_\Psi(s,g)|\) 的绝对值分组；“\(F^2\subset\mathbb A_F^2\)”中普通包含符号被加点。GL₂ 作用的 `GL₂(A_F)-action` 连字符被写成句点，式 (10.4) 的 \(h\cdot\Psi\) 中心点也变为句点。Schwarz 范数描述中的 `constant-coefficients`、`differential` 分别漏 `f`。Lemma 10.1 Mellin 积分中的 \(F_v^\times\) 被写为 `F_*`，\(d^\times x\) 被拆成带冒号的定界符；关于 Dedekind \(\zeta\)-function of F at v 的说明也被拆坏。Lemma 10.1 证明末尾方框以 U+0003 代替；Lemma 10.2 证明的 `suffice` 漏 `f`。
- 复核：式 (10.3)、(10.5) 其余部分、函数方程、极点描述与快速衰减指数主体同原页相符。
- 源级 print quirk：式 (10.6) 在 PDF 原样印作 \(\cos(2\pi n y)\)，Markdown 同样照录；本页不按 Fourier 展开常见形式改成 x。
- 核验时间：2026-10-02 03:22 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.070（PDF p.70 / 印刷 p.70）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p070-70.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p070_constant-term.png`（PDF p.70，pnggray 300dpi）。
- 核对：PDF p.70 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2540–2589 行；第 2540 行承接 p.69），覆盖 Lemma 10.2 证明续文、Lemma 10.3 常数项/证明、(10.8)–(10.12) 和 Lemma 10.4 开头。
- 结果：FAIL。
- 差异：Lemma 10.3 常数项定义中的积分微分在 Markdown 被破坏为 array 相关片段后另接 `dx`，原页为普通 `dx`。双陪集分解中应为 \(\int_{n\in N(\mathbb A_F)}f_\Psi(s,wng)\,dn\)，Markdown 将微分变量录成 `ds`；300dpi 裁片确认。Poisson 求和恒等式后 Markdown 在 “The result follows” 前插入游离字符 `b`。Lemma 10.3 证明末尾空方框由 U+0003 代替。
- 复核：(10.8) 的两个积分域及商群替换、(10.9)–(10.12) 的截断定义、函数界与高度幂次同原页相符。
- 源级 print quirk：PDF 与 Markdown 均在 “it follows that that the product” 中重复 `that`；保留原文。
- 核验时间：2026-10-02 03:28 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.071（PDF p.71 / 印刷 p.71）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p071-71.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p071_local-Whittaker.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p071_Bruhat-integrals.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p071_footnote21.png`、`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p071_equation-1016.png`（均为 PDF p.71，pnggray 300dpi）。
- 核对：PDF p.71 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2586–2640 行），覆盖 Lemma 10.4 结尾、Lemma 10.5、(10.13)–(10.16) 和脚注 21。
- 结果：FAIL。
- 差异：Lemma 10.4 的 `suffice` 漏 `f`，并将 `Fourier coefficients` 拼作 `coeficients`。局部 Whittaker 积分中的字符应为 \(e_{F_v}\)，Markdown 漏掉下标 v。式 (10.15) 两个商集均使用左陪集符号 `\backslash`；Markdown 写成集合差 `\setminus`。Fourier 变换 \(\widehat{\varphi_2}(y)\) 下的积分变量在原页也是 y，本页仅据字面保留，不替换成 t。Lemma 10.5 证明结尾空方框被 U+0003 替代。脚注 21 在 Markdown 中被拆成 \(\bar E_\Psi\)、\(f_\Psi\)、\(E_\Psi\) 等孤立 span，余下句子缺词并错序，不能连续读回原脚注。
- 复核：(10.13)、(10.14)、(10.16) 的积分核与公式主体相符；(10.16) 第二行的积分变量域照录原页显示，不按变量代换预期重排。
- 核验时间：2026-10-02 03:35 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.072（PDF p.72 / 印刷 p.72）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p072-72.png`（pngmono 150dpi）。
- 核对：PDF p.72 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2642–2675 行），覆盖 Remark 10.2、Corollary 10.1、§10.2 开头、Schwartz 函数类 \(\mathcal H(\kappa)\)、(10.18) 及 Lemma 10.6 陈述。
- 结果：FAIL。
- 差异：`different` 漏掉第二个 `f`，拼作 `diferent`；`difficulties` 漏 `f`，拼作 `dificulties`；`differs` 漏 `f`，拼作 `difers`。Corollary 10.1 的 “the characteristic function of \(\mathfrak o_v^2\)” 被 Markdown 拆成 `o f {\mathfrak o_v^2}`，在 “of” 中插入空格并加入无对应原文的花括号。
- 复核：Corollary 10.1 的 (10.17) 局部因子、Lemma 10.6 的积分路径、(10.18) 加权范数及 \(L^\infty\) 界主体均与原页相符。
- 源级 print quirk：原页与 Markdown 均将 Remark 10.2 开头印作 “Remark that”；保留该措辞。
- 核验时间：2026-10-02 03:43 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.073（PDF p.73 / 印刷 p.73）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p073-73.png`（pngmono 150dpi）。
- 核对：PDF p.73 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2678–2716 行），覆盖 Lemma 10.6 证明、Remark 10.3 的显式常数控制及 §10.3 二变量 wave-packet 的经典说明/增长界。
- 结果：FAIL。
- 差异：Lemma 10.6 证明在 “Applying Lem. 10.2 one more time ... we conclude” 之后、Remark 10.3 之前，PDF 印有空方框 `□`，Markdown 原先以 U+0003 代替；原页图 p.73 显示该方框。Remark 10.3 开头原页写作 \(\Psi=\prod_v\Psi_v\)，随后说明“the \(\Psi_v\) are regarded as fixed for v finite”；Markdown 在第一个并列分句中重复插入一次 \(\Psi_v\)。
- 复核：(10.19) 的三项分解、(10.20)–(10.21) 的 Schwartz/Sobolev 范数界，以及 wave-packet 上界 `A(y_1,y_2)` 与 `L^4` 可积性陈述与原页相符。
- 源级 print quirk：原页将 wave-packet 写为 `E_h(z_1,z_2)= \int h(it_1,it_2)E^*(1/2+it,z_1)E^*(1/2+it',z_2) dt dt'`，积分变量为 `t,t'` 而 h 的输入为 `t_1,t_2`；Markdown 忠实保留。
- 核验时间：2026-10-02 03:46 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.074（PDF p.74 / 印刷 p.74）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p074-74.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p074_contract-notation.png`（PDF p.74，pnggray 300dpi）。
- 核对：PDF p.74 完整文本层与 MinerU Markdown 对账（基线 Markdown 第 2718–2772 行），覆盖 Lemma 10.7、Definition 10.1 条件 (1)–(2)、(10.22)–(10.24)、Lemma 10.8 陈述和证明开头。
- 结果：FAIL。
- 差异：Lemma 10.7 中映射应为 \(M:U\to\mathbb R\)，Markdown 漏掉 \(\to\)。Definition 10.1(1) 的原符号为 \(h'\)，Markdown 多加下标 `i`；`neighbourhood` 漏掉 `h`，拼作 `neigbourhood`。增长条件应使用 \(h(\sigma+it,\sigma'+it')\)，Markdown 将第二个 \(t'\) 写成 \(t\)；300dpi 裁片确认。
- 复核：(10.22)–(10.24) 的增长权重、边界积分范数及 Lemma 10.8 的高度比值界与原页相符。
- 源级 print quirk：Lemma 10.7 原页句子为 “there is, a continuous function M”; Markdown 忠实保留了该逗号，不按语法预期删除。
- 核验时间：2026-10-02 03:55 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.075（PDF p.75 / 印刷 p.75）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p075-75.png`（pngmono 150dpi）。
- 核对：PDF p.75 文本层与 MinerU Markdown 对账（基线 Markdown 第 2774–2828 行；第 2828 行仅核至原页末词 “This”，其余续至 p.76），覆盖 (10.25)–(10.29)、Lemma 10.8 证明结尾、Lemma 10.9 及 §11 引言开头。
- 结果：FAIL。
- 差异：首句 `suffice` 在 Markdown 拼作 `sufice`。公式编号整体错位：独立的 `(10.25)` 未附着于 \(I_0\)，\(I_0,I_1,I_2\) 分别误标为 (10.26)、(10.27)、(10.28)，而 \(I_3\) 缺少 (10.28)；PDF 将 (10.25)–(10.28) 依次标在 \(I_0\)–\(I_3\) 上。Markdown 在移线后的 \(\Re(t')=0\) 后漏句点。\(I_3\) 末尾估计式和 Lemma 10.9 证明末尾的原页空心方框均被 MinerU 写成 U+0003 控制字符。
- 复核：除上述拼写、编号、标点和证明结束符外，(10.25)–(10.29) 的被积项与估计、Lemma 10.9 的 \(p<4/(1-2\kappa)\) 条件和积分表达式，以及 §11 引言在本页可见部分与原页相符。
- 核验时间：2026-10-02 04:01 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.076（PDF p.76 / 印刷 p.76）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p076-76.png`（pngmono 150dpi）。
- 核对：PDF p.76 文本层与 MinerU Markdown 对账（基线 Markdown 第 2828–2864 行；第 2828 行从前页末词 “This” 续读，本页范围止于第 2864 行末词 “quotient”），覆盖 §11 引言续文、Hypothesis 11.1、Rankin–Selberg 小节开头及 (11.2)–(11.3)。
- 结果：FAIL。
- 差异：原页 “effort” 在 Markdown 拼作 “efort”；\(F=\mathbb Q\) 的句子中原页为 \(\pi_1,\pi_2,\pi_3\)，Markdown 将最后一个 \(\pi_3\) 的下标丢失；作者名原页为 Böcherer，Markdown 把变音符号置于字母 o 前，写作 “B¨ocherer”。
- 复核：(11.1) 的三重积 L 值与周期比值、指数 \(1+\epsilon\)，(11.2)–(11.3) 的积分域、被积项、测度及常数 \(c_F\) 均与原页相符。
- 源级 print quirk：原页证明句写作 “this has not carried out”，缺少语法上预期的 “been”；Markdown 忠实保留，不据语法推断补词。
- 核验时间：2026-10-02 04:02 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.077（PDF p.77 / 印刷 p.77）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p077-77.png`（pngmono 150dpi）。
- 核对：PDF p.77 文本层与 MinerU Markdown 对账（基线 Markdown 第 2864–2902 行；第 2864 行从前页末词 “quotient” 续读），覆盖 (11.4)–(11.7) 与 Lemma 11.1。
- 结果：FAIL。
- 差异：局部 Whittaker 向量的原记号 \(W_{j,v}\) 被拆损为 \(W_{j,\ell}\)<sub>v</sub>；Lemma 11.1 的单位元值条件中，Markdown 在 \(W_{2,v}\) 上多出共轭横线；原页 \(\mathfrak{o}_v\) 被识作 \(\mathfrak{o}_{\iota}\)；\(\mathrm{PGL}_2(\mathfrak{o}_v)\)-invariant 后多出一个右括号。Lemma 11.1 证明末尾原页空心方框被写成 U+0003 控制字符。
- 复核：(11.4) 的 Fourier 展开和商空间积分、(11.5) 的因子分解、(11.6)–(11.7) 的局部积分及 Steinberg 表示公式与原页相符。
- 源级 print quirk：Lemma 11.1 首句原页写作 “Suppose \(W_{1,v}, W_{2,v}\) the new vectors” 而缺少谓语；Markdown 忠实保留，不按语法预期补词。
- 核验时间：2026-10-02 04:04 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.078（PDF p.78 / 印刷 p.78）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p078-78.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p078-topology-notation.png`（PDF p.78，300dpi）。
- 核对：PDF p.78 文本层与 MinerU Markdown 对账（基线 Markdown 第 2904–2918 行；第 2918 行仅核至原页末词 “The”，后续文字续至 p.79），覆盖 §11.2.2 的局部表示拓扑与连续 Whittaker 赋值讨论。
- 结果：FAIL。
- 差异：原页引号中的 “good” 在 Markdown 中被误识为含 \Delta 与星号的标记串。原页脚本体 \(\mathscr S\) 被写为 \(\mathcal S\)；两个 \(W^{\mathscr S}\) 分别多出点号、横线。诱导特征 \(\mu,\nu\) 被加粗为 \(\boldsymbol{\mu},\boldsymbol{\nu}\)。局部 L 因子商的分子 \(W_\pi\) 被多加波浪号，积分测度 \(d^\times y\) 也多出波浪号。Markdown 将 “coefficients” 拼为 “coeficients”，将 “suffices” 拼为 “sufices”。300dpi 裁片核实脚本体、W 上的附加记号和 L 因子积分符号。
- 复核：闭集紧致性、连续性条件 (1)–(2)、\(q_v^{ks}\) 有限 Laurent 多项式表达及次数局部有界的论述，在本页范围内与原页相符。
- 核验时间：2026-10-02 04:08 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.079（PDF p.79 / 印刷 p.79）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p079-79.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p079-lemma11-2.png`（PDF p.79，300dpi）。
- 核对：PDF p.79 文本层与 MinerU Markdown 对账（基线 Markdown 第 2918–2955 行；第 2918 行从前页末词 “The” 后续读），覆盖 §11.2.2 结尾、Lemma 11.2 及 (11.8)。
- 结果：FAIL。
- 差异：Lemma 11.2(3) 的 “data as in (2)” 被误识为 \(\boldsymbol{\mathscr Z}\)。(3a) 列表上限原页为 \(C\)，Markdown 多加下标 \(i\)；(3b) 的积分域原为 \(F_v^\times\)，Markdown 写成 \(F_\ast^\times\)。证明中的第二个连续赋值原为 \(\pi_{2,v}\)，Markdown 变成 \(\pi_{2,\boldsymbol{\tau}}\)；证明中合适常数 \(C\) 也多出下标 \(i\)。Markdown 将 “coefficients” 拼作 “coeficients”，将 “sufficiently” 拼为 “suficiently”，将 “continuously” 拼为 “continously”。证明末尾原页空心方框被写成 U+0003 控制字符。
- 复核：Lemma 11.2 的局部因子商、全纯性、非零数据选择、(3c) 的增长界及 Lemma 11.3 的 (11.8) 与原页相符。
- 源级 print quirk：原页证明中写作 “given fix momentarily”，Lemma 11.2 连续性积分项印作 \(\int |W_{i,v}(a(y)|^2 d^\times y\)（缺少右括号），Lemma 11.3 则写作 “a certain constant absolute constant c”；Markdown 忠实保留这些原文形态。
- 核验时间：2026-10-02 04:12 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.080（PDF p.80 / 印刷 p.80）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p080-80.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p080-lemma11-4.png`（PDF p.80，300dpi）。
- 核对：PDF p.80 文本层与 MinerU Markdown 对账（基线 Markdown 第 2958–2992 行），覆盖 Lemma 11.3 证明、Lemma 11.4 陈述与证明及脚注 22。
- 结果：FAIL。
- 差异：Lemma 11.3 证明中的积分域原为 \(\mathbb A_F^2\)，Markdown 将下标 F 识作粗体 r；“differs” 漏写一个 f，且该证明末尾和 Lemma 11.4 证明末尾的两个空心方框均被写成 U+0003 控制字符。Lemma 11.4 中有界子集的帽号原在 \(\mathrm{PGL}_2\) 上，Markdown 移到 \(F_\infty\) 上；“real number” 被拆损为 `num\imath b e r`，第 (3) 项的 “is” 被拆成带间距的 `i s`。证明漏掉 “Let B” 中的 B。脚注 22 又把 PGL 识成 FGL，并把帽号置于 F 上。
- 复核：Lemma 11.4 的 \(\Phi(s)\) 定义、(1)–(4) 的界及非分歧不变性条件、局部新向量构造和 L² 范数论证与原页相符。
- 核验时间：2026-10-02 04:17 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.081（PDF p.81 / 印刷 p.81）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p081-81.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p081-lemma11-5.png`（PDF p.81，300dpi）。
- 核对：PDF p.81 文本层与 MinerU Markdown 对账（基线 Markdown 第 2994–3032 行；第 3032 行仅核至原页末词 “The”，后续续至 p.82），覆盖 Lemma 11.5、(11.9)–(11.10) 及选取局部数据的证明。
- 结果：FAIL。
- 差异：Lemma 11.5 有界子集记号中，原页帽号只覆盖 \(\mathrm{PGL}_2\)，Markdown 将帽号扩展至包含 \(F_\infty\) 的整个表达式。(1) 中 “and” 被拆成 `a n d`；(2) 末尾分号及与 (3) 的项目分隔丢失。说明局部平移的原记号为 \(a([\mathfrak p])_v\)，Markdown 将下标 v 识为花体 c。
- 复核：(11.9)、(11.10) 的全局积分、L 函数分母、指数 \(1/2-t\)、两个局部因子乘积及 archimedean 数据选择陈述与原页相符。
- 源级 print quirk：引理证明回指 (11.6) 时原文为 “as long as one of \(\pi_1,\pi_2\) were cuspidal”；Markdown 忠实保留其原有主谓数不一致。
- 核验时间：2026-10-02 04:20 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.082（PDF p.82 / 印刷 p.82）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p082-82.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p082-local-rs.png`（PDF p.82，300dpi）。
- 核对：PDF p.82 文本层与 MinerU Markdown 对账（基线 Markdown 第 3032–3056 行；第 3032 行从前页末词 “The” 后续读），覆盖 Lemma 11.5 证明结尾、§11.3 开头、(11.11)、Lemma 11.6 陈述及其证明开头。
- 结果：FAIL。
- 差异：Lemma 11.5 证明末尾，原页积分域为 \(F_v^\times\)，Markdown 误成 \(\mathcal F_\eta^\times\)；“suffice” 两处均漏写一个 f；\(K_v\)-finite 中多出句点；证明末尾空心方框被写成 U+0003 控制字符。单位群测度归一化中的原下标 \(F_v\) 被写为 \(F_\tau\)，且 \(d^\times x,dx\) 之间被插入句点。
- 复核：第二个 Whittaker 模型使用 \(\overline{\psi(x)}\) 与原页相符；(11.11) 的 \(K_0\) 子群、Lemma 11.6 的局部因子比值和 \(W(z)\) 的 Kirillov 记号与原页相符。
- 源级 print quirk：原页将整数环写作 \(\mathfrak o_{F_v}=\{x\in F_v^\times:v(x)\ge0\}\)，排除了 0；Markdown 忠实保留该印刷定义。
- 核验时间：2026-10-02 04:24 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.083（PDF p.83 / 印刷 p.83）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p083-83.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p083-local-equations-footnote23.png`（PDF p.83，300dpi）。
- 核对：PDF p.83 文本层与 MinerU Markdown 对账（基线 Markdown 第 3058–3108 行），覆盖 (11.12)–(11.15) 及脚注 23。
- 结果：FAIL。
- 差异：原页 \(F_v\)-points 在 Markdown 中插入句点，成为 `F_v .-points`。Iwasawa 公式的积分域原为 \(A^\times K_v\)，Markdown 将 \(A^\times\) 降为 \(A\times\)。脚注 23 的两条函数方程在 Markdown 被拆散为多个 HTML footnote span，分子、分母和积分符号的上下标顺序破损，不能保留原页的完整等式结构。
- 复核：(11.12)–(11.14) 的 Mellin 积分与 Whittaker 函数分段值、(11.15) 的商空间积分及 \(I(s)\) 的 \((1-q_v^{-2s})^{-1}\) 因子与原页相符；300dpi 裁片核对了函数方程脚注和 \(A^\times K_v\) 积分域。
- 核验时间：2026-10-02 04:28 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.084（PDF p.84 / 印刷 p.84）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p084-84.png`（pngmono 150dpi）。
- 核对：PDF p.84 文本层与 MinerU Markdown 对账（基线 Markdown 第 3110–3148 行），覆盖 (11.16)、Lemma 11.6 计算结尾、§11.4 开头、μ_z 定义及 Lemma 11.7 陈述。
- 结果：FAIL。
- 差异：Lemma 11.6 证明末尾的原页空心方框被写成 U+0003 控制字符。双陪集论证中 \(K_v\) 后多插一个句点。Lemma 11.7 结尾，原页在 \(\theta\) 的绝对值公式后有句点，Markdown 漏掉该标点。
- 复核：(11.16) 的两个双陪集积分、\(I(s)\) 的闭式及其 L 因子化简、\(L_{unr}\) 的有限非分歧因子乘积、\(\mu_z\) 定义和 Lemma 11.7 的积分公式与原页相符。
- 核验时间：2026-10-02 04:32 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.085（PDF p.85 / 印刷 p.85）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p085-85.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p085-different-conductor.png`（PDF p.85，300dpi）。
- 核对：PDF p.85 文本层与 MinerU Markdown 对账（基线 Markdown 第 3150–3191 行），覆盖 Lemma 11.7 证明、Lemma 11.8 陈述及证明开头至 (11.20)。
- 结果：FAIL。
- 差异：Lemma 11.7 证明末尾的原页空心方框被写成 U+0003 控制字符；\(\mathfrak{o}_{F_v}^\times\)-invariant 中的 “invariant” 被拆成带间隔的字母串。Lemma 11.8 对不同理想赋值的原指数为 \(\varpi^{d_v}\)，Markdown 在 \(d_v\) 上多加点号；“of \(F_v\)” 后误插冒号；“different” 漏写一个 f。
- 复核：(11.17) 的加性特征积分、Gauss 和绝对值、(11.18)–(11.20) 的归一化积分、Sobolev 界及无穷处 \(W_v(y)\) 构造与原页相符。
- 核验时间：2026-10-02 04:35 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.086（PDF p.86 / 印刷 p.86）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p086-86.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p086-lemma11-9-footnotes.png`（PDF p.86，300dpi）。
- 核对：PDF p.86 文本层与 MinerU Markdown 对账（基线 Markdown 第 3194–3248 行），覆盖 Lemma 11.8 结尾、截断积分引言、Lemma 11.9、其 Mellin 变换证明及脚注 24–25。
- 结果：FAIL。
- 差异：前段原页使用普通 L(1/2, π×χ)，Markdown 改成花体 L；“affecting” 漏写一个 f，且 “μ_z-integral” 被转换为带间距的字母标记。Lemma 11.8 证明末尾原页空心方框被写成 U+0003 控制字符。Lemma 11.9 证明末尾的取值句原为 “Take sigma=1/2+epsilon in the + case, -1/2-epsilon in the - case”，Markdown 将句子切成字母间隔的 TeX 标记并插入多余字符；“previous Lemma. Take” 之间还丢失空格。脚注 24–25 被切分成多个 HTML span，footnote 24 的 A_F^× 与 product_v F_v^× 关系次序破损；footnote 25 漏掉 support 后的 W_v，并把 K∞-finite 缩损为 finite。
- 复核：(11.21) 的无穷处积分乘积、theta' 的有限素因子表达、Lemma 11.9 两个截断积分界、Mellin 反演公式和上界主项与原页相符。
- 源级 print quirk：原页写作 “the second assertion if the Lemma is clear”，Markdown 忠实保留该印刷文字，不按语法猜测改成其他词。
- 核验时间：2026-10-02 04:39 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.087（PDF p.87 / 印刷 p.87）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p087-87.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p087-11-10-footnote26.png`（PDF p.87，300dpi）。
- 核对：PDF p.87 文本层与 MinerU Markdown 对账（基线 Markdown 第 3250–3300 行），覆盖 (11.22)、Lemma 11.10、(11.23)、其证明开头及脚注 26。
- 结果：FAIL。
- 差异：“sufficiently” 漏写一个 f；(11.22) 在 Markdown 公式中被错排成 `(1 1. 2 2)`；证明末尾空心方框被写成 U+0003 控制字符。Lemma 11.10 证明中，定义域原为 F_v²，Markdown 在指数 2 上加横线；Ψ_v(x,y) 定义之后重复了分号。脚注 26 被严重截损：E*(s,z) 与其修正项定义、q⁻¹ 求和积分及其等于 q⁻¹/²ΛΛ 的关系式均未保留在 Markdown 的 HTML footnote span 中。
- 复核：两个 (11.22) 解析界及局部因子乘积、Lemma 11.10 的周期积分、全纯延拓和 (11.23) 的导子增长界与原页相符。
- 核验时间：2026-10-02 04:46 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.088（PDF p.88 / 印刷 p.88）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p088-88.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p088-fourier-local-integrals.png`（PDF p.88，300dpi）。
- 核对：PDF p.88 文本层与 MinerU Markdown 对账（基线 Markdown 第 3302–3342 行），覆盖 Lemma 11.10 证明中的无穷处测试函数构造、(11.24)–(11.28) 及证明结尾。
- 结果：FAIL。
- 差异：“of rapid decay” 在 Markdown 多出 b，变成 “bof rapid decay”；“coefficient” 漏写一个 f；(11.27) 后的 “Re(s) ≫ 1” 多出数字 9。局部因子界中 (C^{1+|\Re(s)|}) 的绝对值右竖线被移到指数括号外；“sufficiently” 拼为 “suficiently”。Lemma 11.10 证明末尾的原页空心方框缺失。
- 复核：(11.24) 的 Schwartz 范数界、(11.25)–(11.26) 的局部 Mellin 积分、(11.27) 的全局 Fourier 展开、(11.28) 的积表达及其余连续性界与原页相符。
- 核验时间：2026-10-02 04:49 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.089（PDF p.89 / 印刷 p.89）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p089-89.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p089-lemma11-11.png`（PDF p.89，300dpi）。
- 核对：PDF p.89 文本层与 MinerU Markdown 对账（基线 Markdown 第 3344–3388 行），覆盖 Lemma 11.11、(11.29)–(11.31) 及证明结尾。
- 结果：FAIL。
- 差异：原页两处使用乘积单位群 ∏_v o_v^×；Markdown 第一处将 o_v 识作粗体 sigma，第二处将乘积符号 ∏ 错写为大写 Π。末段界中的 Cond(χ)^(1+2ε) 在 Markdown 给 χ 和数字 2 多加点号；Re(s)=1/2 后误插句点。“suffice” 拼为 “sufice”。Lemma 11.11 证明末尾原页空心方框被写成 U+0003 控制字符。
- 复核：(11.30) 的三步等式、(11.31) 的 Mellin 积分关系、(11.29) 的快速衰减界、I± 的截断估计及其参数范围与原页相符。
- 核验时间：2026-10-02 04:52 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.090（PDF p.90 / 印刷 p.90）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p090-90.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p090-references.png`（PDF p.90，300dpi）。
- 核对：PDF p.90 文本层与 MinerU Markdown 对账（基线 Markdown 第 3392–3450 行），覆盖 References [1]–[30]。
- 结果：FAIL。
- 差异：Refs. [1]–[3] 的 “André” 与 [17] 的 “Hervé” 均把 é 误写成独立急音符号置于 e 前；[1] “Sér.”、[7] “algébriques”、[29] “Grössencharakteren” 的变音符号也分别错置。[4] 将 Études 的急音符号挪到 “Sci.” 后。Refs. [1]、[8] 的 “coefficients” 均少一个 f；[30] 的 “ff.” 被截成 “f.”。Ref. [28] URL 在斜杠与波浪号之间插入空格并把波浪号转成 TeX 重音命令。
- 复核：References [1]–[30] 的其余作者、篇名、卷期、页码及年份和 PDF 相符。
- 源级 print quirk：Ref. [9] 原页作者名后直接接篇名（“P. Cohen Hyperbolic distribution…”），未印句点；Markdown 忠实保留，不补标点。
- 核验时间：2026-10-02 04:56 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## p.091（PDF p.91 / 印刷 p.91）
- PNG：`audit/Venkatesh_2006_sparse_equidistribution_p091-91.png`（pngmono 150dpi）；裁片：`audit/300dpi/Venkatesh_2006_sparse_equidistribution_p091-references.png`（PDF p.91，300dpi）。
- 核对：PDF p.91 文本层与 MinerU Markdown 对账（基线 Markdown 第 3452–3468 行），覆盖 References [31]–[39]。
- 结果：FAIL。
- 差异：Ref. [35] 的 “Strömbergsson”、[36] 的 “Szemerédi”、以及 [37] 的 “propriétés / arithmétiques / symétrie” 均被拆成错置的独立变音符号。Ref. [37] 第二个法文条目将 “automorphes” 多识一个 h，写成 “automorphhes”。
- 复核：References [31]–[39] 的卷期页码、其余姓名与篇名及出版年份和原页相符。
- 核验时间：2026-10-02 04:59 EDT。
- Actor：`Peer-P36`；model=`gpt-6-luna`；effort=`max`。

## 修复登记（最终复核）

- 修复角色：`Peer-P36 | gpt-6-luna/max`。
- 来源 PDF：`Venkatesh_2006_sparse_equidistribution.pdf`，SHA-256 `c2676117a3f4b833b6354a586efeeb28ba367928bc8d83e0c310f0942ece2265`。
- 修复前 MinerU Markdown：父文件提交 `e2ecf051043c2683576c8c19c6cdf66d7e05c6af`，SHA-256 `2fd195c4e0adcc00f7eab551949b27b8b71d70b3435dc9fbfdff09c3478a3fa8`。
- 修复提交：`075a8291dc8264b2904f68cdb490088d3c87e708` (`fix(md): Venkatesh p.1-91 audited corrections [Peer-P36 | gpt-6-luna/max]`)。提交只包含目标 MinerU Markdown；修复后的 SHA-256 为 `642a4fc5eb2ef85b7826286a9e601a6eff417ec43b671bb705262e096e31350b`。
- 逐页修复范围：本文件 p.001–p.091 各页的 `差异` 记录是逐项修复索引，列明 PDF 页码、基线 Markdown 差异和对应页图/300dpi 裁片。各项内容级 OCR 错误已逐处手工修复；不按语法或数学预期改写原刊印刷 quirk，且已确认的 TeX 空格 false positive（p.018、p.030）没有被当作数值差异修改。
- 需要重构或特别核对的修复包括：p.006 脚注 3 上标及其正文（正文用全幅裁片 `audit/300dpi/Venkatesh_2006_sparse_equidistribution_p006-footnote3-full.png` 复核）；p.028 公式 (3.14) 的 `\ll` 与 Theorem 3.2 证明结束符；p.045 与 p.073 的证明结束方框；p.066 式 (9.27) 中指数 (e_{\mathfrak q}-1)；p.071 脚注 21；p.075 公式 (10.25)–(10.28) 编号；p.083 脚注 23 两条局部函数方程；p.086 脚注 24–25；p.087 脚注 26；p.090–p.091 的参考文献变音符号、拼写及 URL。
- 审计记录更正：p.028 方框位于 “We choose H ... to conclude” 之后、Remark 3.2 之前；p.039 的增长界 `C^{|Re(t)|+|Re(t')|}` 与 PDF 完全一致，先前 extra-`C` 差异判断已撤回。p.073 证明结束方框在最终复核时补入页级差异记录，并已修复。
- 最终复核：2026-10-02 对修复后的 **3340 行 Markdown 从头至尾完整复读**，并按 p.001–p.091 的 born-digital 文本层/页图及已登记的 300dpi 裁片回核本次修改，没有发现遗漏的内容级差异或编辑引入的新差异。只读终验确认 U+0003 计数为 0，`git diff --check` 通过；未运行测试。
- 结论范围：这一复核支持最终 Markdown 与本论文印刷 PDF 的文字和记号转录相符，不表示对论文数学证明有效性作了验证。原文中已登记的 print quirk 与仅属版面表现的 PASS± 项继续按审计说明保留。
- 集成状态：此提交是 Peer-P36 的 branch-local 候选；未集成到主线，也未修改 Master 所有的根级 `AUDIT-INDEX.md` 或 `AUDIT-PROGRESS.log`。
