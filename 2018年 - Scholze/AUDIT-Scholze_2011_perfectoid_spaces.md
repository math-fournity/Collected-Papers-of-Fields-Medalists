# Scholze, *Perfectoid Spaces* — 逐页审计

- Actor：Peer-P20
- Model：gpt-6-luna
- Reasoning effort：max
- Base：`037602429d3b009f6fc468c732073eb3ddf9875f`（共同 main 基线）
- PDF：`Scholze_2011_perfectoid_spaces.pdf`（51 页；born-digital，Creator LaTeX with hyperref，Producer pdfTeX-1.40.10；文本层 154,782 bytes）
- MinerU Markdown：`Scholze_2011_perfectoid_spaces_mineru/Scholze_2011_perfectoid_spaces__Scholze_2011_perfectoid_spaces.md`
- 审计方法：逐页完整对账 PDF 文本层与 Markdown 正文；题录页及密集数学页另作 PNG 目检；文本抽取无法唯一判断的字形按原页图/300dpi 裁片仲裁。印刷原文为准。
- 状态：`CANDIDATE_NOT_CURRENT`；只代表此 Peer worktree 的候选证据，尚未由 Master 集成。

## 总评与覆盖声明

- 初审总评：PDF p.1–p.51 共 51 页逐页对账；48 页原始分级为 `FAIL`，3 页为 `PASS±`，0 页为 `PASS`。这些是修复前的页级分级。修复登记记录了 48 个 FAIL 页的内容修复；p.28 一项经复核属误报，已从该页当前差异说明中移除；修复后没有重新给页面分级。
- 覆盖范围：51 页均有对应的 150dpi 整页 PNG，并逐页将 PDF 文本层映射到 MinerU Markdown 正文。篇级方法记录题录页和密集数学页另作 PNG 目检；无法仅凭文本层裁决的字形以本文件列出的 300dpi 裁片仲裁。此处说明逐页审计覆盖及所用视觉复核范围，不表示对每一处 PASS± 排版瑕疵都作了修复后复审。
- 修复后核对：目标 Markdown 已按修复登记所述从首行至末行完整复读（2180 行），并执行只读差异清点；这是修复核对，不是重新逐页分级。修复内容位于 `04f67d03a116a07f0cb23bd5693a191635719590`。
- MinerU `doc_id`：`UNKNOWN`（现存导出中未保留）。`middle_json.json` 的 metadata 只记录 `file_suffix=pdf` 与 producer `mineru 3.4.4`；检索本篇保留的 MinerU JSON/Markdown 导出未发现 `doc_id` 字段，因此不从其他元数据推断。

## 页级记录

### PDF p.001 / 印刷 p.1 — PASS±
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p001.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:08:43-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 对账：题名、作者、摘要、目录条目及页码、页脚日期均与印刷页相符；对应 Markdown 行 1–20。
- 差异：印刷页左侧竖排 arXiv 识别行 `arXiv:1111.4914v1 [math.AG] 21 Nov 2011` 未收入 Markdown；篇目来源与版本另由根 README 登记。该项是题录元数据遗漏，不改变正文数学内容。
- 证据：PDF p.1 文本层及入库整页 PNG；本页未发现正文公式。

### PDF p.002 / 印刷 p.2 — PASS±
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p002.png`（pngmono 150dpi；本篇密集数学页视觉抽验）
 - Page audit commit time: 2026-10-01T16:10:00-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 对账：Markdown 行 22–59 对应 Introduction 开篇至 Theorem 1.3 及其过渡句；Theorem 1.1 的两个域、完成化字段、`sharp` 映射、逆极限、Definition 1.2 的 Frobenius 条件及 Theorem 1.3 的 Galois 群结论与 PDF 文本层及 p.2 整页图一致。
- 差异：多处公式两侧空格和行内标点被 MinerU 拍平（如 `p .`、公式与单词粘连）；未发现会改变陈述的符号差异或内容丢失。
- 证据：PDF p.2 完整文本层与入库 p.2 PNG；题名、公式和定理均已目检核对。

### PDF p.003 / 印刷 p.3 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p003.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:12:03-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p003_claim14.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p003_theorem17.png`
- 对账：PDF p.3 对应 Markdown 行 60–92，涵盖 Claim 1.4、Theorem 1.5、Definition 1.6、Theorem 1.7、perfectoid algebra 示例及 Theorem 1.8(i)。
- FAIL：Markdown 行 80 把 Theorem 1.7 目标范畴写成 `K^{\bar{\flat}}`，而印刷为 `K^{\flat}`；行 86 在示例中给 `T` 加了多余上划线、把指数分母 `p` 写成 `\bar p`，并把倾斜底域 `K^{\flat}` 写成 `K^{\tilde{\flat}}`。这些符号改变了所述域/代数，须在全篇审计结束后逐处修复。
- 其他差异：Claim 1.4 的 `affine` 拼作 `afine`，引号短语及行内公式空格有 OCR 形变；Definition 1.6 把 “K-algebra” 连字符识成行内乘点 `\cdot`，语境仍可恢复。以上列为 PASS± 排版/文字瑕疵，不与上述数学 FAIL 混同。
- 证据：PDF p.3 文本层及两张 300dpi 裁片直接显示 `K^\flat`、`T^{1/p^\infty}`、`K^\flat\langle T^{1/p^\infty}\rangle`；整页 PNG 对应内容位置已复核。

### PDF p.004 / 印刷 p.4 — PASS±
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p004.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:12:55-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 对账：PDF p.4 对应 Markdown 行 94–128，覆盖 Theorem 1.8(ii)–(iv)、Theorem 1.9、Theorem 1.10–1.12 及射影空间上的 `p` 次幂映射；各范畴、底域、态射和逆极限公式与 PDF 文本层相符。
- 差异：Markdown 有多处行内公式粘连、Theorem 1.9/1.11 的 `K^\flat` 后多出游离 `[` 伪影，及 `gives` 被拆成 `g i ves`；未发现改变范畴或公式的数学差异。
- 证据：PDF p.4 完整文本层与入库整页 PNG；本页定理及坐标公式已逐项对账。

### PDF p.005 / 印刷 p.5 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p005.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:13:55-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p005_monodromy.png`
- 对账：PDF p.5 对应 Markdown 行 130–154，涵盖 monodromy filtration、Conjecture 1.13、既有结果概述、Theorem 1.14 与证明草图开头。
- FAIL：Markdown 行 130 将 `\ell`-adic 写成反引号记号两处；过滤条件把 `V(-1)`误写为 `V\bar{(-1)})`。行 132 把惯性不变量上的 `gr_j^N V` 写成 `gr_j^N \dot V`。300dpi 印刷页明确显示 `\ell`、`Fil^N_{i-2}V(-1)` 与 `gr_j^N V`，以上均须在全篇审计结束后逐处修复。
- 证据：PDF p.5 文本层与 p.5 整页 PNG；300dpi 裁片直接仲裁上述三个公式/记号。

### PDF p.006 / 印刷 p.6 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p006.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:15:15-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p006_lemma115.png`
- 对账：PDF p.6 对应 Markdown 行 156–176，覆盖逆极限例子、Lemma 1.15、其证明过渡及后续说明/致谢。
- FAIL：Markdown 行 170 将印刷的邻域 `\tilde X` 和超曲面 `Y` 分别写成点标记 `\overset{\cdot}{X}`、`\overset{\cdot}{Y}`；行 172 的证明把 `H^i(\tilde X)\to H^i(Y)` 的箭头整段漏掉，成为相邻表达式。印刷页 300dpi 裁片明确显示 `\tilde X`、`Y` 以及 `H^i(X)=H^i(\tilde X)\to H^i(Y)`，须在全篇审计结束后修复。
- 其他差异：致谢中的机构名 `Hausdorff Center` 漏一个 `f` 成为 `Hausdorf Center`；记为 PASS± 文字瑕疵。
- 证据：PDF p.6 文本层、整页 PNG 与 Lemma 1.15/映射的 300dpi 裁片。

### PDF p.007 / 印刷 p.7 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p007.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:16:28-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p007_valuation.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p007_valuation_ring.png`
- 对账：PDF p.7 对应 Markdown 行 178–210，覆盖 Adic spaces 开篇、Definition 2.1–2.2、Remark 2.3–2.4 及 valuation support 的引入。
- FAIL：Markdown 行 202 把 valuation 的类型映射 `R \to \Gamma \cup \{0\}` 漏成 `R \; \Gamma \cup \{0\}`；行 208 在值群商中多出 `K` 上方的点，写为 `\dot K^\times/R^\times`，而印刷为 `K^\times/R^\times`。300dpi 原页分别清楚显示箭头与无点的 `K`；须于全篇审计结束后修复。
- 证据：PDF p.7 文本层与入库整页 PNG；两个 300dpi 裁片仲裁映射与商群记号。

### PDF p.008 / 印刷 p.8 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p008.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:18:38-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p008_definition26.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p008_spa.png`
- 对账：PDF p.8 对应 Markdown 行 210–254，覆盖 Definition 2.5–2.7、Tate algebra/affinoid 定义、Spa 与 rational subset、Remark 2.8。
- FAIL：Markdown 行 222 把 Tate algebra 定义中的开邻域基 `aR_0` 写成 `aR`，丢掉下标 0；同一条后面的 bounded 定义仍有 `aR_0`。印刷页及 300dpi Definition 2.6 裁片均明确显示 `aR_0`。
- 其他差异：`affinoid` 多次拼作 `afinoid`、Definition 2.6(ii) 多一个右括号，且 `i.e.` 被 OCR 拆坏；列为 PASS± 文字/排版瑕疵。Definition 2.7 的 Spa 等价类符号另经 300dpi 对照，与 PDF 相符。
- 证据：PDF p.8 文本层、整页 PNG 与 300dpi 定义/ Spa 裁片。

### PDF p.009 / 印刷 p.9 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p009.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:19:55-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p009_definition213.png`
- 对账：PDF p.9 对应 Markdown 行 256–300，覆盖 Definition/Proposition 2.9、Proposition 2.10–2.12、Definition 2.13 与 Proposition 2.14 开头。
- FAIL：Markdown 行 284 的 rational subset 分母写为 `q`，印刷为 `g`；开邻域参数写为 `a\in\bar{k^\times}`，印刷为 `a\in k^\times`；completion pair 中写成 `\bar{\hat B}`，印刷为 `\hat B`。行 294 丢失 `(R,R^+)\to(S,S^+)` 与 `Spa(S,S^+)\to Spa(R,R^+)` 两个映射箭头，并把第二个 map 误呈为 `Spa\varrho`。这些变动影响 rational domain、拓扑与泛性质的定义，须于全篇审计结束后逐处修复。
- 证据：PDF p.9 文本层与整页 PNG；Definition 2.13 / Proposition 2.14 的 300dpi 裁片逐符号显示 `g`、`k^\times`、`\hat B` 与两个箭头。

### PDF p.010 / 印刷 p.10 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p010.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:22:38-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p010_sheaf.png`
- 对账：PDF p.10 对应 Markdown 行 302–348，覆盖结构层的定义、Proposition 2.15、Definition 2.16 与 Theorem 2.17。
- FAIL：Markdown 行 310 把 `|f_i/g|≤1` 的分母写成 `q`；行 326 将两个局部极大理想都写成 `\{f\mid f\,|f(x)|\cdots\}`，多出一个 `f`；行 346 把 Theorem 2.17 的条件词 `If` 写成 `H`。PDF p.10 的 300dpi 裁片分别显示分母 `g`、条件 `|f(x)|` 与 `If (R,R^+)`，均须在全篇审计结束后逐处修复。
- 证据：PDF p.10 文本层、整页 PNG 与定义/命题区域 300dpi 裁片。

### PDF p.011 / 印刷 p.11 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p011.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:25:04-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 对账：PDF p.11 对应 Markdown 行 356–390，覆盖 Definition 2.18、Proposition 2.19、Example 2.20 的 Tate algebra 与 valuation tree 前四类点。
- FAIL：Markdown 行 374 在经典点的求值映射中漏掉 `R\to k` 的箭头，变成 `R k`；印刷页公式为 `R\to k,\ f=\sum a_nT^n\mapsto\sum a_nx^n`。页图还确认 PDF p.11 中的 valuation-tree 图形与 MinerU 引用的 `images/page_10_image_7.jpg` 图形相符。
- 其他差异：`affinoid`/`coefficients` 有文字拼写瑕疵及行内空格被压平，列为 PASS±。
- 证据：PDF p.11 完整文本层与入库整页 PNG；MinerU 图与从 PDF p.11 提取的原始图形逐项视觉比对。

### PDF p.012 / 印刷 p.12 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p012.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:26:32-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p012_rank2.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p012_bijection.png`
- 对账：PDF p.12 对应 Markdown 行 392–440，覆盖 rank-2 valuations、valuation tree 的点型分类及 Theorem 2.21。
- FAIL：Markdown 行 436 在 Theorem 2.21 的 bijection 右侧集合 `\{qc opens in X^{ad}\}` 后多出上标 `2`；印刷只结束该集合并接逗号，未有脚注或平方标记。该上标会把目标读成集合的平方，须在全篇审计后删除。
- 源级 quirk：PDF p.12 在定义符号中印出字面 `?\in\{<,>\}` 作为符号选择标记；Markdown 相同，忠实保留，不将其改成猜测的 Greek 字母。
- 证据：PDF p.12 文本层、整页 PNG；rank-2 定义与 bijection 的 300dpi 裁片确认 literal `?` 及无上标 `2`。

### PDF p.013 / 印刷 p.13 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- PNG：`audit/Scholze_2011_perfectoid_spaces_p013.png`（pngmono 150dpi）
 - Page audit commit time: 2026-10-01T16:28:48-04:00 (Git committer timestamp; page note and evidence were committed together.)
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p013_formal_model.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p013_taut.png`
- 对账：PDF p.13 对应 Markdown 行 442–480，覆盖 non-admissible cover、Theorem 2.22 的 formal model 专门化与逆极限、Definition 2.23。
- FAIL：Markdown 行 456 把 Theorem 2.22 的 formal scheme `\mathfrak X` 写成普通 `X`，与后文泛纤维 `X` 混同；行 462 扩张到局部环化空间态射中漏掉 `(X^{ad},O^+_{X^{ad}})\to(\mathfrak X,O_{\mathfrak X})` 的箭头；行 480 把 `\overline U` 的闭包上划线丢掉，变成 `closure U of U`。300dpi 原页确认三个记号。
- 图像核对：Markdown 引用的 MinerU 图 `images/page_12_image_4.jpg` 与 PDF p.13 嵌入图及入库整页图中的 type (5) 示意图一致。
- 证据：PDF p.13 文本层与整页 PNG；Theorem 2.22 与 Definition 2.23 的 300dpi 裁片、PDF 原嵌入图对照。

### PDF p.014 / 印刷 p.14 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:15:11Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p014.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p014_berkovich_maps.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p014_varpi.png`
- 对账：PDF p.14 对应 Markdown 行 482–510，覆盖 Theorem 2.24、Berkovich/adics maps、Proposition 2.25、Definition 2.26 与 Proposition 2.27。
- FAIL：Markdown 行 494 漏掉 `X^{Berk}\to X^{ad}` 与 retract `X^{ad}\to X^{Berk}` 两个箭头；行 496 在 retraction 的目标对象上给 `ad` 加了多余上划线，且同句中的两处态射箭头也丢失；行 498 的 fibre map 同样缺箭头。Proposition 2.25 行 502、504 把印刷的 `\varpi`-adic/`\varpi`-divisible 记号误成字面 `$`；行 504 第二个 kernel map 漏 `\to`；Proposition 2.27 行 510 漏掉 `(R,R^+)\to(K,K^+)`。300dpi 原页确认这些箭头、目标对象和 `\varpi`。
- 其他差异：`Hausdorff` 拼成 `hausdorf`、`affinoid` 拼成 `afinoid` 等文字瑕疵，列为 PASS±。
- 证据：PDF p.14 完整文本层、入库整页图与 Theorem 2.24/Proposition 2.25 的 300dpi 裁片。

### PDF p.015 / 印刷 p.15 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:17:05Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p015.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p015_filtration.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p015_varpi.png`
- 对账：PDF p.15 对应 Markdown 行 512–553，覆盖 Definition 2.28、Proposition 2.29、Perfectoid fields 开篇、Lemma 3.2 与 Lemma 3.4(i)。
- FAIL：Markdown 行 514 丢失 Proposition 2.29 两处 ` (R,R^+)\to(K,K^+)` / ` (R,R^+)\to(L,L^+)` 箭头；行 550 把“the right-hand side is independent of `\\varpi`”中的 `\\varpi` 误成字面 `$`。印刷页图和 300dpi 裁片确认箭头与 `\\varpi`。
- PASS±：Lemma 3.2 的 `p`-divisible 被渲成 `p\\cdot`-divisible，并在证明末尾多出孤立 `$2`；原文图显示连字符与普通 “as desired”，不影响可恢复的结论。
- 证据：PDF p.15 文本层与整页 PNG；Proposition 2.29 映射及 Lemma 3.2 / 3.4 的 300dpi 裁片。

### PDF p.016 / 印刷 p.16 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:18:46Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p016.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p016_tilt_definitions.png`
- 对账：PDF p.16 对应 Markdown 行 556–626，覆盖 Lemma 3.4(ii)–(iv)、Remark 3.5 与 Lemma 3.4 证明 (i)–(ii)。
- FAIL：Markdown 行 556 把 `K^\circ/\varpi` 写成 `K^\circ/$`；行 592 把 Remark 3.5 中被重新定义的元素 `\varpi` 写成字面 `$`；行 610 把“`x_n-x_n'` is divisible by `\varpi`”写成“divisible by `$`”。300dpi 印刷页三处均为同一 `\varpi` 字形，需在全篇审计完成后逐处修复。
- 证据：PDF p.16 文本层、整页 PNG 与 300dpi tilt-definition 裁片。

### PDF p.017 / 印刷 p.17 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:20:26Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p017.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p017_proposition38.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p017_poly_field.png`
- 对账：PDF p.17 对应 Markdown 行 628–670，覆盖 Lemma 3.4(iii)–(iv)、Proposition 3.6、Theorem 3.7 与 Proposition 3.8 证明开头。
- FAIL：Markdown 行 670 将证明所取多项式的系数环写成 `K^{\mathfrak{po}}[X]`；PDF p.17 明确为 `K^{\flat\circ}[X]`，即倾斜域的幂有界整数环上的多项式。这改变了多项式 `Q` 的定义域，须在全篇审计结束后修复。
- PASS±：行 634 在 `K^\flat` 后多出游离 `[`，且 Prop. 3.8 的句子/行内公式有 OCR 粘连；源页核心陈述仍可辨认。
- 证据：PDF p.17 文本层与整页 PNG；Proposition 3.8 公式的 300dpi 裁片明确显示 `Q\in K^{\flat\circ}[X]`。

### PDF p.018 / 印刷 p.18 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:23:00Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p018.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p018_almost.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p018_hom.png`
- 对账：PDF p.18 对应 Markdown 行 672–726，覆盖 Proposition 3.8 证明收尾、Almost mathematics 开篇至 Proposition 4.4 及 `alHom` 定义。
- FAIL：Markdown 行 672 将证明中的“constant term `P(y^\sharp)` is divisible by `\varpi`”写成 divisible by `$`；行 700 将最终迭代界写成 `\dot\varpi^{N/p^m}` 且把“for all `m`”损成 `m_{:}`；行 724 将 `Hom_{K^{\circ a}}(X,Y)` 多出 `\delta`，变成 `Hom_{\delta_{K^{\circ a}}}(X,Y)`。300dpi 印刷页显示无点的 `\varpi`、普通整数指标 `m` 与正确 Hom 下标。
- 证据：PDF p.18 文本层、整页 PNG 与 almost-math 公式/Hom 的 300dpi 裁片。

### PDF p.019 / 印刷 p.19 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:24:52Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p019.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p019_flatness.png`
- 对账：PDF p.19 对应 Markdown 行 728–768，覆盖 Propositions 4.5–4.6、Definition/Proposition 4.7 及其证明。
- FAIL：Markdown 行 762 把系数环写为 `K^{\circ\circ}`（并夹有 `_{-algebra}` OCR 碎片），印刷为 `K^\circ`-algebra；行 766 两次把变量 `\epsilon` 写成控制字符 U+000F（分别在 annihilation bound 和 “for all” 条件中），损坏 Definition/Proposition 4.7(iii) 的参数陈述。300dpi 原页清楚显示 `K^\circ` 与 `\epsilon`。
- 证据：PDF p.19 文本层、入库整页 PNG 与 300dpi flatness 裁片；Markdown 原行已只读确认含 U+000F。

### PDF p.020 / 印刷 p.20 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:26:33Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p020.png`（pngmono 150dpi）
- 对账：PDF p.20 对应 Markdown 行 770–816，覆盖 Remark 4.8、Example 4.9、Proposition 4.10、Theorem 4.11 及 Definition 4.12–4.13。
- FAIL：Markdown 行 804、806、812 在三条态射定义中都将 `A\to B` 漏成 `A\;B`：unramified morphism、étale morphism 与 finite étale morphism 的定义均失去 source/target 箭头。PDF p.20 文本层与整页 PNG 均保留 `A\to B`，须在全篇审计结束后逐处修复。
- 证据：PDF p.20 完整文本层与入库整页 PNG；此 born-digital 页的箭头由文本层逐项对账。

### PDF p.021 / 印刷 p.21 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:28:03Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p021.png`（pngmono 150dpi）
- 对账：PDF p.21 对应 Markdown 行 818–870，覆盖 trace morphism/trace form、Remark 4.15、Theorem 4.16–4.17 与 Definition 5.1(i)–(ii)。
- FAIL：Markdown 行 824 将 trace morphism `tr_{P/A}` 写成 `t\cdot_{P/A}`；行 832、834、836 分别漏掉 `B\to A`、Remark 4.15 中的两条 `B_*\to End(...)` / `B\to End(...)` 及 Theorem 4.16 的 `A\to B`；行 840、846 把 `\varpi`-adic completion 和 reduction 写成字面 `$`；行 862 的 Frobenius 映射 `R^\circ/\varpi\to R^\circ/\varpi` 漏掉中间箭头。这些差异破坏态射/trace/reduction 规格，须在全篇审计后逐处修复。
- 证据：PDF p.21 完整文本层与入库整页 PNG；born-digital 原文逐页保留上述箭头、`tr_{P/A}` 与 `\varpi`。

### PDF p.022 / 印刷 p.22 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:29:53Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p022.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p022_perfectoid_definition.png`
- 对账：PDF p.22 对应 Markdown 行 872–926，覆盖 Definition 5.1(iii)、Theorem 5.2 与 Lemma 5.3(i)–(iii) 的完整页内证明。
- FAIL：Markdown 行 872 把 perfectoid `K^{\circ a}/\varpi`-algebra 的基环写成 `K^{\circ a}/$`；行 894 把 torsion 条件写成“no `$`-torsion”。修复复核时又核实：行 900 两处 adic completion 参数仍为字面 `$`，且将右侧对象 `M_*` 错写成 `M`；行 910 两处 torsion 条件也将 `\varpi` 写成 `$`。PDF p.22 原图显示这些位置均为 `\varpi`，Lemma 5.3(iv) 的右侧对象为 `M_*`。
- PASS±：行 880 类别预告旁有游离数字 `8` 伪影，PDF 只作省略号/过渡；不影响后续类别定义。
- 证据：PDF p.22 文本层、整页 PNG 与 300dpi 定义/条件裁片。

### PDF p.023 / 印刷 p.23 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:33:27Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p023.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p023_tilting_algebra.png`
- 对账：PDF p.23 对应 Markdown 行 928–966，覆盖 Lemma 5.3(iii)–(iv) 的续段、Proposition 5.5、Lemmas 5.6–5.7 及 Proposition 5.8 结论。
- FAIL：Markdown 行 928 漏掉乘以 `\epsilon` 引出的 injection arrow，且本页的 `\epsilon` 多处退化为控制字符；行 930、936、944 把 `\varpi`-adic completion 写成字面 `$`；行 956 将 Lemma 5.7 中的指数 `k/p` 与 `(k-1)/p` 损成 `\kappa/p`、乱码分子 `dS/p`，并插入孤立数字 `1`，同时把 torsion 元 `\varpi` 写为 `$`；行 960 丢失 Frobenius 商环组合映射中的两处 `\to`。这些缺陷改动了变量、完备化理想或证明映射，须全篇审计后逐处修复。
- 证据：PDF p.23 文本层与整页 PNG；300dpi 裁片逐项显示 `\epsilon`、`\varpi`、`k/p`、`(k-1)/p` 与两条箭头。

### PDF p.024 / 印刷 p.24 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:35:26Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p024.png`（pngmono 150dpi）
- 对账：PDF p.24 对应 Markdown 行 968–1002，覆盖 Proposition 5.8–5.9、Theorem 5.10 与 Theorem 5.11 的变形障碍陈述。
- FAIL：Markdown 行 974 把 Frobenius 诱导的映射 `R^\circ/\varpi\to R^\circ/\varpi` 漏掉箭头，变成两个相邻商环。PDF p.24 文本层和整页图均保留该箭头；这改变了 Proposition 5.9 证明所称的映射。
- 证据：PDF p.24 完整文本层与入库整页 PNG。

### PDF p.025 / 印刷 p.25 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:37:56Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p025.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p025_deformation.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p025_corollary516.png`
- 对账：PDF p.25 对应 Markdown 行 1004–1046，覆盖 Theorem 5.12、Proposition 5.13、Remark 5.14、Proof、Remark 5.15 与 Corollary 5.16。
- FAIL：Markdown 行 1006 漏掉 lifting morphism `f:S\to S'` 的箭头；行 1008 把 target algebra `S_0'` 写成带 acute 的 `S_0^{\acute{\prime}}`，并把 lift `f:S\to S'` 写成 `f:S\dot{S}'`；行 1014 漏掉 `\Phi:R\to R` 的箭头；行 1044 将 Corollary 5.16 的 superscript `a` 多写成 `\underline a`。原页裁片显示普通 prime、映射箭头与不带下划线的 superscript `a`。
- PASS±：Remark 5.14 末尾的 `0` 多了点标记，但等式数值不变；保留为排版瑕疵。
- 证据：PDF p.25 文本层、整页 PNG 与 Theorem 5.12 / Corollary 5.16 的 300dpi 裁片。

### PDF p.026 / 印刷 p.26 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:47:32Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p026.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p026_cotangent_triangle.png`
- 对账：PDF p.26 对应 Markdown 行 1046–1092，覆盖 Corollary 5.16 的证明、Theorem 5.10 的 inverse-limit lifting 证明及 Proposition 5.17 的定义开头。
- FAIL：Markdown 行 1059 将 Theorem 5.10 证明的 cotangent-complex triangle 三项公式损成 `\mathbb L \frac{a}{A}/...` 等错位片段，丢失各复形项的代数与底环上下标；PDF p.26 的 300dpi 原图显示三项依次基于 `(K^\circ/\varpi)^a`、`(K^\circ/\varpi^n)^a` 与 `(K^\circ/\varpi^{n-1})^a`，并由箭头相连。Markdown 行 1070 又把 `\varpi`-adically complete 写成字面 `$`-adically complete。两处均须在全篇审计结束后逐处修复。
- 证据：PDF p.26 文本层、入库整页 PNG 与 cotangent triangle 的 300dpi 裁片。

### PDF p.027 / 印刷 p.27 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T04:56:17Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p027.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p027_tilt_lift.png`
- 对账：PDF p.27 对应 Markdown 行 1102–1148，覆盖 Proposition 5.17 的倾斜构造/证明、Remark 5.19、Proposition 5.20 与 Lemma 5.21 开头。
- FAIL：Markdown 行 1102 把 Frobenius 作用的目标写成 `(A/\varpi)`，漏掉 printed `_*`，实际印刷映射为 `\Phi:(A/\varpi)_*\to(A/\varpi)_*`；行 1110 将 `A^\flat_*` 所属的 `K^{\flat\circ}` 底代数损成 `K^{\circ}_{-}`；行 1132 把 “`R^\circ` is `\varpi`-adically complete” 写为字面 `$`-adically complete。以上更改了 Hom/almost-elements 域与完备化理想，须全篇审计结束后修复。
- 其他差异：行 1130 的 `R^\flat` 后多出游离 `[`、行 1118 的 “we go” 被拆开，列为 PASS± 排版伪影。
- 证据：PDF p.27 文本层与整页 PNG；300dpi 裁片直接显示 `_*` 目标、`K^{\flat\circ}` 与 `\varpi`-adic completion。

### PDF p.028 / 印刷 p.28 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T05:05:22Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p028.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p028_etale_proof.png`
- 对账：PDF p.28 对应 Markdown 行 1150–1180，覆盖 Lemma 5.21 证明收尾、Proposition 5.22–5.23、Remark 5.24 及 Proposition 5.23 证明开头。
- FAIL：Markdown 行 1168 将 `A[t^{-1}]` 错写成 `\bar A[t^{-1}]`；行 1170 把正交补 `S_0^\perp` 写成 `S_0^\bot`；行 1176 把目标 `R^\circ` 加了多余上划线并把 `S^{\circ a}`错成 `S^{\acute\circ}`；行 1178 丢掉映射 `S^\circ\to R^{\circ n}` 的箭头，且把 `\epsilon` 换成控制字符；行 1180 把 `\varpi^N e` 拆成 `\varpi^N_e`。300dpi 原页逐项确认这些符号。
- 图像核对：Markdown 的 MinerU 图 `images/page_27_image_6.jpg` 与 PDF p.28 的 tilting categories 图在内容上相符。
- 证据：PDF p.28 文本层、整页 PNG 与 300dpi proof 裁片。

### PDF p.029 / 印刷 p.29 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T05:13:09Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p029.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p029_etale_proof.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p029_epsilon_maps.png`
- 对账：PDF p.29 对应 Markdown 行 1182–1216，覆盖 Proposition 5.23 证明尾段、Theorem 5.25 与 Theorem 3.7 的两种证明。
- FAIL：Markdown 行 1182 把参数 `\epsilon` 写成控制字符，并将有限和项 `b_i` 错成 `\overline{b_i}`；行 1198 也把“multiplication by `\epsilon`”中的变量变成控制字符。300dpi 原页显示 `\epsilon e=\sum a_i\otimes b_i`、(b_i) 无上划线，并在复合映射处两次使用同一 `\epsilon`。
- PASS±：行 1192 的 map `R^{\circ n}\to S^\circ` 后多出游离数字 `2`；印刷只结束该映射并接公式，记作多余 OCR 伪影。
- 图像核对：Markdown 引用的 `images/page_28_image_8.jpg` 与 PDF p.29 页内 commutative tilting diagram 相符。
- 证据：PDF p.29 文本层与整页 PNG；有限 étale proof / `\epsilon e` maps 的 300dpi 裁片及原页 diagram。

### PDF p.030 / 印刷 p.30 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T05:25:04Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p030.png`（pngmono 150dpi）
- 对账：PDF p.30 对应 Markdown 行 1218–1246，覆盖 Section 6 开篇、Definitions/Lemma 6.1–6.2、Theorem 6.3 声明及证明结构概述。
- FAIL：Markdown 行 1244 把证明概述中的映射 `X\to X^{\flat}` 漏掉箭头，变成 `X X^{\flat}`；PDF p.30 文本层明确写出 map `X\to X^{\flat}` is continuous。这是该节证明路线的态射声明，须在全篇审计后修复。
- PASS±：`affinoid` 多处拼作 `afinoid`、行内数学周围空格被压平；其余定义与 Theorem 6.3(i)–(iv) 的范畴/公式均与 PDF 相符。
- 证据：PDF p.30 完整文本层与入库整页 PNG。

### PDF p.031 / 印刷 p.31 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T05:31:15Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p031.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p031_lemma64.png`
- 对账：PDF p.31 对应 Markdown 行 1248–1298，覆盖 Theorem 6.3 证明开头、Lemma 6.4(i)–(iii) 及特征 p 情形证明至 almost-isomorphism。
- FAIL：Markdown 行 1248、1250 两次把 map `X\to X^{\flat}` 漏成相邻的 `X X^{\flat}`；行 1254 将 rational subset `U=U(f_1,\ldots,f_n/g)` 的分母写成未定义的 `a`；行 1256、1284 把 source `\varpi`-adic completion 写为字面 `$`-adic。p.31 原页 300dpi 图明确显示箭头、分母 `g` 与 `\varpi`。
- PASS±：行 1254 余有 `N_{;}` 类别的轻微排版/标点伪影；本页其他已核公式与陈述相符。
- 证据：PDF p.31 文本层、整页 PNG 与 Lemma 6.4/其证明的 300dpi 裁片。

### PDF p.032 / 印刷 p.32 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T05:37:41Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p032.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p032_general_case.png`
- 对账：PDF p.32 对应 Markdown 行 1300–1366，覆盖 Lemma 6.4(i) 特征 p 证明的结束、General K 的 (i)⇒(ii) 论证、(i)/(iii) 证明开头及 composite map。
- FAIL：Markdown 行 1320 把本段标题写为 `(i)⇒(i)`，而 PDF p.32 为 `(i)⇒(ii)`；紧随其后的正文同样明确说明本段由 (i) 推出 (ii)，故标题错误会误导证明依赖关系。修复复核还发现行 1334 的 `\varpi`-adic completion、行 1354 的 `\varpi`-adically complete 均被写成字面 `$`-adic 形式；PDF p.32 原图均显示 `\varpi`。
- 证据：PDF p.32 文本层、整页 PNG 与 general-K 推导的 300dpi 裁片。

### PDF p.033 / 印刷 p.33 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T05:44:11Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p033.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p033_induction_condition.png`
- 补充裁片：`audit/300dpi/Scholze_2011_perfectoid_spaces_p033_epsilon_membership.png`（同页引理归纳证明的额外高分辨率观察）
- 对账：PDF p.33 对应 Markdown 行 1366–1435，覆盖 Lemma 6.4(i)–(iii) 的结尾及 Lemma 6.5 的陈述、误差估计和归纳起步。
- FAIL：Markdown 行 1430 将归纳假设 `\epsilon(c)\in\mathbb Z[1/p]` 误写成带点的 `\dot\in`；PDF p.33 原页和 300dpi 裁片均为普通集合成员符号 `\in`，点标记会改变该条件的语义。
- 证据：PDF p.33 文本层与整页 PNG；Lemma 6.5 归纳条件的 300dpi 裁片。

### PDF p.034 / 印刷 p.34 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T05:49:58Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p034.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p034_varpi_divisibility.png`
- 对账：PDF p.34 对应 Markdown 行 1438–1508，覆盖 Lemma 6.5 的归纳构造与误差估计、Corollary 6.7(i) 开头。
- FAIL：Markdown 行 1444 把 “`\varpi`-adic completion”写成字面 `$`-adic completion；行 1456 把 “`\varpi` divides `r_i-s_i^\sharp`”写成字面 `$` divides。PDF p.34 300dpi 原图两处均为同一 `\varpi`，这些换字改变了完成拓扑与整除条件。
- 证据：PDF p.34 文本层、整页 PNG 与 300dpi completion/divisibility 裁片。

### PDF p.035 / 印刷 p.35 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T05:56:27Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p035.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p035_pfinite.png`
- 对账：PDF p.35 对应 Markdown 行 1502–1540，覆盖 Corollary 6.7–6.8、Definition 6.9 与 Proposition 6.10 开头。
- FAIL：Markdown 行 1512 把 Corollary 6.7(iii) 的 morphism `X\to X^{\flat}` 写成 `X X^{\flat}`；行 1514 将 “after increasing `\epsilon` slightly” 中的 `\epsilon` 写成控制字符 U+000F；行 1522 把局部上同调论证中的 `\varpi`-adic completion 写成字面 `$`-adic；行 1536 也把 Definition 6.9 中 `R^+` 的 `\varpi`-adic completion 写成字面 `$`-adic。PDF p.35 原图分别显示态射箭头、参数 `\epsilon` 和两处 `\varpi`。
- PASS±：`affinoid` 多处拼作 `afinoid`、若干公式周围的空格/段落边界受 OCR 影响；未发现其余内容性差异。
- 证据：PDF p.35 文本层、整页 PNG 与 Definition 6.9 的 300dpi 裁片。

### PDF p.036 / 印刷 p.36 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:02:30Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p036.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p036_cohomology.png`
- 对账：PDF p.36 对应 Markdown 行 1542–1588，覆盖 Proposition 6.10 的有限 Čech 复形与开映射定理证明、Proposition 6.11 开头。
- FAIL：Markdown 行 1552 把 cohomology group “annihilated by some power of `\varpi`”写成 some power of `$`。PDF p.36 的 300dpi 原页显示这是同一 topologically nilpotent element `\varpi`，此处不能按美元符号解释。
- PASS±：行 1588 的 “K-algebras”附近 `-` 被标成 `\mathfrak{-}`，以及局部空格/行断开有 OCR 瑕疵；其余本页复形与证明步骤对得上。
- 证据：PDF p.36 文本层、整页 PNG 与 cohomology 条件的 300dpi 裁片。

### PDF p.037 / 印刷 p.37 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:09:04Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p037.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p037_direct_limit.png`
- 对账：PDF p.37 对应 Markdown 行 1590–1622，覆盖 Proposition 6.11(iii)–(iv)、Lemma 6.13、Proposition 6.14 的陈述及特征 p 证明开头。
- FAIL：Markdown 行 1590 把 exactness up to `\varpi`-power 写成 `$`-power；行 1598 把直限中的 `\mathcal O^+_{X_j}(U_j)` 错写成 `\mathcal O^+_{X_i}(U_j)`；行 1602 缺 `K\langle T_i\rangle\to R` 的像映射箭头，并把 (K^\circ\langle T_i\rangle) 错成 `\bar K^\circ\langle T_i\rangle`；行 1604 将“larger J containing g”损成 `containing^{g,}`，把 induced map 的 source pair 多加上划线且丢失 `\to(R,R^+)`，并把 completion 写成 `$`-adic；行 1606 topology 同样将 `\varpi` 写成 `$`；行 1618 将 `\mathcal O_X^{\circ a}` 写成 `\mathcal O_X^{o a}`；行 1620 的 completion parameter 也写成 `$`。PDF p.37 的 300dpi 原页与文本层逐项显示相反记号/映射。
- 证据：PDF p.37 文本层、整页 PNG 与 finite direct-limit construction 的 300dpi 裁片。

### PDF p.038 / 印刷 p.38 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:20:16Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p038.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p038_etale_topology.png`
- 对账：PDF p.38 对应 Markdown 行 1622–1644，覆盖 Lemma 6.13 的逆极限论证结尾、Theorem 6.3 证明结束、Definitions 6.15–6.16、Proposition 6.17–6.18。
- FAIL：Markdown 行 1624 将 original sequence reduced modulo `\varpi` 写成字面 `$`；行 1642 把 Proposition 6.18 中的结构映射 `X\to Y\leftarrow Z` 丢成 `\right.` / `\left.`，使纤维积所依赖的图式不完整；行 1644 又将 `\varpi`-torsion free 写成 `$`-torsion free。PDF p.38 原图显示对应字符为 `\varpi`，并明确给出两条结构映射。
- PASS±：行 1634 的等号前多出冒号，行 1636 在 `X^{\flat}` 后多出孤立 `[`；这些是轻微 OCR/排版伪影。本页其他已经核对的 tilting 与纤维积陈述相符。
- 证据：PDF p.38 文本层与整页 PNG；characteristic-0 结尾及 Proposition 6.18 的 `\varpi` 和态射图式见 300dpi 裁片。

### PDF p.039 / 印刷 p.39 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:22:56Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p039.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p039_definition71_morphism.png`
- 对账：PDF p.39 对应 Markdown 行 1646–1684，覆盖 Section 7 开篇、Definitions 7.1–7.2 及两处 étale/strongly étale 交换图。
- FAIL：Markdown 行 1652 将 Definition 7.1(i) 中代数对之间的态射 `(R,R^+)\to(S,S^+)` 漏掉箭头，只留下并列对象，丢失了“morphism”的源与目标关系；PDF p.39 原图及 300dpi 裁片均清楚显示 `\to`。
- PASS±：行 1648 将 “where A” 识成 “were A”，行 1654 将普通文本 “of Y” 切分为行内公式 `$o f Y$`，行 1668 将 “difference” 拼成 “diference”；均为局部 OCR/拼写瑕疵，不影响本页定义结构。Markdown 所引 `images/page_38_image_8.jpg` 与 `images/page_38_image_16.jpg` 的两幅交换图均与 PDF p.39 相符。
- 证据：PDF p.39 文本层、整页 PNG、Definition 7.1(i) 的 300dpi 裁片及两幅内嵌交换图的视觉比对。

### PDF p.040 / 印刷 p.40 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:25:11Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p040.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p040_henselian_completion.png`
- 对账：PDF p.40 对应 Markdown 行 1686–1715，覆盖 Definition 7.2 后的 tilting 陈述、Lemma 7.3 及证明、Proposition 7.4 和 Lemma 7.5(i) 的范畴等价。
- FAIL：Markdown 行 1686 把 tilt 映射的目标 `Y^{\flat}` 写成 `\dot{Y}^{\flat}`；行 1690 把 Lemma 7.3(ii) 中 `C^+` 在 `D` 内的整闭包写成在 `D_i` 内；行 1694 漏掉 `X\times_Y Z = \mathrm{Spa}(D,D^+)` 中的等号。行 1706 把 `\varpi`-adic completion 写成字面 `$`-adic；行 1710 再次将 `\varpi`-adically complete 写成 `$`-adically complete，并把直限 `\varinjlim A_i` 的陈述损坏为含多余 `K^\circ` 与 `(\varpi)` 的 `lim` 表达。原页分别给出未加点的 `Y^{\flat}`、整闭包在 `D` 中、等号、以及 `\varpi`-adic 与直限记号。
- PASS±：行 1706 在 `\widehat A[\varpi^{-1}]` 后多出右方括号；属可恢复的 OCR/排版伪影。
- 证据：PDF p.40 文本层与整页 PNG；Proposition 7.4、直限段及 Lemma 7.5(i) 公式中的 `\varpi` 与直限见 300dpi 裁片。

### PDF p.041 / 印刷 p.41 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:27:30Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p041.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p041_henselian_cover.png`
- 对账：PDF p.41 对应 Markdown 行 1718–1758，覆盖 Lemma 7.5(i)–(ii) 及证明、Proposition 7.6 及证明、Proposition 7.7 及证明。
- FAIL：Markdown 行 1728 将 henselian 条件 `\varpi` 写成字面 `$`，并把 `\varinjlim A_i` 记成没有直限箭头的 `lim A_i`；这改变了所用环的完备化/直限条件。行 1748 将 `Y_i=\mathrm{Spa}(R_i,R_i^+)` 中的 `\mathrm{Spa}` 错加上划线，变成 `\mathrm{\bar{Spa}}`。PDF p.41 文本层及 300dpi 原图分别显示 `\varpi`、带箭头的直限及普通 `\mathrm{Spa}`。
- PASS±：行 1752 的 `affinoid` 拼作 `afinoid`；为可恢复的拼写 OCR 瑕疵，其余本页有限 étale 类别等价与局部化陈述和 PDF 相符。
- 证据：PDF p.41 文本层与整页 PNG；henselian 条件、直限记号及 `Y_i` 的 Spa 表达见 300dpi 裁片。

### PDF p.042 / 印刷 p.42 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:29:14Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p042.png`（pngmono 150dpi）
- 对账：PDF p.42 对应 Markdown 行 1760–1793，覆盖 Corollary 7.8、Theorem 7.9(i)–(iii) 及证明至第一条 Čech exact sequence。
- FAIL：Markdown 行 1760 漏掉复合态射前提中的 `g:Y\to Z` 箭头；行 1776 把 strongly finite étale cover `V\to U` 写成 `V U`；行 1786 也把结论处的 `V\to U` 写成 `V U`；行 1790 将 glued space 的结构态射 `Y\to X` 写成 `Y X`。这些箭头明确记录 Corollary 7.8 的复合对象及 Theorem 7.9 局部覆盖与粘合后的态射关系，PDF p.42 原图均可辨认。
- PASS±：行 1780 在 `X^{\flat}` 后多出孤立 `[`；`afinoid` 拼写、少量空格和断行伪影可恢复，Theorem 7.9 的范畴等价与有限 étale cover 的论证其余部分与原页相符。
- 证据：PDF p.42 文本层与整页 PNG；Corollary 7.8 和 Theorem 7.9 证明中的四处结构态射逐项按原图核对。

### PDF p.043 / 印刷 p.43 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:31:33Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p043.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p043_etale_cohomology.png`
- 对账：PDF p.43 对应 Markdown 行 1796–1838，覆盖 Theorem 7.9(ii)–(iii) 的证明结尾、Proposition 7.10、Definitions 7.11、Theorem 7.12、Proposition 7.13 及 Definition 7.14 开头。
- FAIL：Markdown 行 1816 两次漏掉 induced morphism of sites 的箭头 `X_{\mathrm{et}}\to Y_{\mathrm{et}}`；行 1826 把几乎元素记号 `\mathcal O_X^{\circ a}` 写成 `\mathcal O_X^{o a}`，丢失圆圈算子；行 1834 将 exact up to a bounded `\varpi`-power 写成 bounded `$`-power。PDF p.43 与 300dpi 原图明确给出两处 site 映射、`\circ a` 记号和 `\varpi`。
- PASS±：行 1820 在 `K^{\flat}` 后多出孤立 `[`；行 1828 将 “suffices” 拼成 “sufices”。这些不改变相邻数学主张。
- 证据：PDF p.43 文本层与整页 PNG；Proposition 7.13 几乎元素 Čech 复形及有界 `\varpi`-幂裁片见 300dpi 图。

### PDF p.044 / 印刷 p.44 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:33:58Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p044.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p044_inverse_limits.png`
- 对账：PDF p.44 对应 Markdown 行 1840–1886，覆盖 Definition 7.14、Remarks 7.15、Propositions 7.16、Theorem 7.17、Corollaries 7.18–7.19，以及 Section 8 与 Definition 8.2(i) 开头。
- FAIL：Markdown 行 1840 在 Definition 7.14 的 `X\sim\varprojlim X_i` 及底层空间映射 `|X|\to\varprojlim|X_i|` 中丢失逆极限/映射箭头；行 1848 把 Remark 7.15 的逆极限条件写为 `\varinjlim X_i`（直接极限）；行 1850 漏掉 étale morphism `Y\to X_i` 的箭头；行 1852 在“底层空间映射为双射”及 homeomorphism 结论两处都丢了 `|X|\to\varprojlim|X_i|`；行 1856 把 Theorem 7.17 的引用 `Definition 7.14` 损成 `Definition 7.1\textmu`。这些差异改变逆系统定义、态射关系或定理所依赖的定义编号，PDF p.44 原图与 300dpi 裁片均可核实。
- 证据：PDF p.44 文本层与整页 PNG；Definition 7.14、Remark 7.15、Proposition 7.16 和 Theorem 7.17 中的逆极限箭头、方向及定义编号见 300dpi 裁片。

### PDF p.045 / 印刷 p.45 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:37:49Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p045.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p045_character_lattice.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p045_toric_notation.png`
- 对账：PDF p.45 对应 Markdown 行 1888–1928，覆盖 Definition 8.2(ii)、Theorem 8.3、Definition/Proposition 8.4、adic/perfectoid toric-space 构造及 Theorem 8.5 开头。
- FAIL：Markdown 行 1916 把“闭单位球”例中的 adic toric space `\mathcal X_\Sigma^{\mathrm{ad}}` 误成 `\bar\chi_\Sigma^{\mathrm{ad}}`，并把 formal completion 的基环 `k^\circ` 写成 `k^{\mathrm{o}}`；行 1918 又将 perfectoid space `\mathcal X_\Sigma^{\mathrm{perf}}` 写成 `\chi_\Sigma^{\mathrm{perf}}`。行 1924 在 Banach 空间基的指数条件中把配对 `\langle u,v_i\rangle` 写成不可见界定符 `\left.u,v_i\right.`，丢失了对偶配对。PDF p.45 原图及 300dpi 裁片核实这些符号与对象。
- PASS±：行 1904 将 “an element of” 切分进 `$o f$` 行内公式；行 1926 “etc.” 后多出句点，均为可恢复的 OCR/标点伪影。
- 证据：PDF p.45 文本层、整页 PNG，以及 Theorem 8.3/Definition 8.4 的 character-lattice 裁片和 adic/perfectoid toric-space 记号裁片。

### PDF p.046 / 印刷 p.46 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:41:24Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p046.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p046_tilt_comparison.png`
- 对账：PDF p.46 对应 Markdown 行 1930–1973，覆盖 Theorem 8.5(i)–(v) 及证明、Proposition 8.6 及证明、Proposition 8.7 声明和其 graded-ring 构造。
- FAIL：Markdown 行 1930、1932 两次把 Theorem 8.5 的 perfectoid toric space `\mathcal X_{\Sigma,K}^{\mathrm{perf}}` 误写成 `\chi_{\Sigma,K}^{\mathrm{perf}}`；行 1950 将 étale topoi 的 morphism `V_{\mathrm{et}}^{\sim}\to U_{\mathrm{et}}^{\sim}` 漏成两个并列对象。PDF p.46 原图及 300dpi 裁片确认此对象符号和态射箭头。
- PASS±：行 1968 在 `X_{\Sigma,K^{\flat}}` 后多出孤立 `[`；Markdown 所引 `images/page_45_image_8.jpg` 的 commutative diagram 与 PDF p.46 相符。
- 证据：PDF p.46 文本层、整页 PNG、Theorem 8.5 的 300dpi 记号裁片及内嵌交换图比对。

### PDF p.047 / 印刷 p.47 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:44:34Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p047.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p047_epsilon.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p047_elladic.png`
- 对账：PDF p.47 对应 Markdown 行 1976–2008，覆盖 Proposition 8.7 证明余段、Corollary 8.8、Section 9 标题及局部伽罗瓦群 inertia character 的引入。
- FAIL：Markdown 行 1984 在 “for some `\epsilon`” 处写入控制字符（U+000F），丢失邻域不等式所用的正数参数；行 2008 将 “`\ell`-adic” 与 “pro-`\ell`-quotient” 中的 `\ell` 误成反引号。PDF p.47 原图及 300dpi 裁片明确显示 `\epsilon` 和 `\ell`。
- PASS±：行 1976 与 2004 的 `K^{\flat}` 后各多出孤立 `[`；行 2008 在 `\ell^n` 与 “-th roots” 之间多出句点。均是可恢复的符号/标点伪影。
- 证据：PDF p.47 文本层、整页 PNG；Proposition 8.7 的 `\epsilon` 与 Section 9 的 `\ell` 记号见两张 300dpi 裁片。

### PDF p.048 / 印刷 p.48 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:47:54Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p048.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p048_representations_weights.png`、`audit/300dpi/Scholze_2011_perfectoid_spaces_p048_etale_proof_arrow.png`
- 对账：PDF p.48 对应 Markdown 行 2016–2056（至印刷 p.48 页末）；覆盖 Proposition 9.1、Definition/Proposition 9.2、Conjecture 9.3、L-functions 解释、Theorem 9.4 及其证明概述开头。Markdown 行 2056 的证明概述继续到印刷 p.49，本记录只核对 p.48 范围。
- FAIL：Markdown 行 2016 将 Proposition 9.1 的表示对象 `\overline{\mathbb Q}_\ell` 写成带反引号下标的 `Q̄_\``，丢失 `\ell`-adic 系数域；行 2036 把 Conjecture 9.3 的 `\operatorname{gr}_j^N V` 写为 `\operatorname{gr}_i^N V`，错换了对应权重的 filtration 次指标；行 2038 再次将 “`\ell`-adic cohomology” 中的 `\ell` 写成反引号；行 2056 漏掉 Theorem 9.4 证明概述的态射 `f:X\to C\setminus\{x\}` 箭头。PDF p.48 文本层及 300dpi 原图逐项显示正确系数域、`j` 次指标、`\ell` 和态射箭头。
- PASS±：行 2016 在 “for all `\sigma\in I_1`” 后多出孤立数字 `9`；行 2022 将 “effect” 拼成 “efect”。这些是可恢复的 OCR/排版伪影。
- 证据：PDF p.48 文本层与整页 PNG；Proposition 9.1、Conjecture 9.3、Theorem 9.4 证明概述的 300dpi 裁片。

### PDF p.049 / 印刷 p.49 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:51:00Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p049.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p049_lemma95_field.png`
- 对账：PDF p.49 对应 Markdown 行 2056–2087，覆盖 Theorem 9.4 证明概述结尾、Lemma 9.5、Theorem 9.6 及证明、Theorem 9.7 和 Galois-equivariant cohomology map。行 2056 承接 p.48 的证明概述；此处按 p.49 原页核对其续文。
- FAIL：Markdown 行 2058 把 Lemma 9.5 中的 “`\ell`-adic representation” 写成反引号下标；行 2064 把 Theorem 9.6 证明中 completed perfection 的基域 `k'=\mathbb F_q((t))` 错写成 `k'=\mathbb F_q(\mathbf\Sigma(t))`，丢失 Laurent-series 记号并插入无关的 `\Sigma`。PDF p.49 文本层及 300dpi 裁片显示 `\ell` 和 `\mathbb F_q((t))`。
- PASS±：行 2056 在 `V^{I_k}` 前重复插入半截 `V^{I}` 字样；行 2064 的 `K^{\flat}` 与 `t=\varpi^{\flat}` 后各多出孤立 `[`。Markdown 引用的 `images/page_48_image_9.jpg` 交换图与 PDF p.49 原图相符。
- 证据：PDF p.49 文本层与整页 PNG；Lemma 9.5、Theorem 9.6 的 300dpi 裁片及内嵌交换图比对。

### PDF p.050 / 印刷 p.50 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:54:07Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p050.png`（pngmono 150dpi）
- 300dpi 仲裁：`audit/300dpi/Scholze_2011_perfectoid_spaces_p050_etale_notation.png`
- 对账：PDF p.50 对应 Markdown 行 2092–2144，覆盖 Lemma 9.8 证明及 References [1]–[15]。
- FAIL：Markdown 行 2101 将 cohomology target 的 residue-field tilt `\mathbb C_p^{\flat}` 写成 `\mathbb C_p^b`；行 2110 把 étale-site 下标 `\acute{\mathrm{et}}` 写成 `\dot{\mathrm{et}}`；行 2112 又把相同下标写成带帽的 `\hat{\mathrm{et}}` / 带点的 `\dot{\operatorname{et}}`。这些装饰属于对象/算子记号的一部分，PDF p.50 以 `\flat` 与 `\acute{\mathrm{et}}` 记载，300dpi 原图可辨。
- PASS±：References [1]–[15] 的作者名重音有分离的重音符号或额外标点（如 [2]、[3]、[8]、[10]），但姓名、题名与书目序号可恢复；本页未见条目缺失。
- 证据：PDF p.50 文本层、整页 PNG 与 Lemma 9.8 proof 的 300dpi 记号裁片；References [1]–[15] 与原页逐项核对。

### PDF p.051 / 印刷 p.51 — FAIL（以原图为准）
- Actor/model/effort：Peer-P20 / gpt-6-luna / max
- Page audit event time：2026-10-02T06:56:38Z (UTC)
- PNG：`audit/Scholze_2011_perfectoid_spaces_p051.png`（pngmono 150dpi）
- 对账：PDF p.51 对应 Markdown 行 2146–2180，覆盖 References [16]–[33]。
- FAIL：Markdown 行 2180 将 [33] 标题 “Monodromy weight filtration is independent of `\ell`” 中的 `\ell` 写成反引号；PDF p.51 明确印作花体小写 `\ell`，这会改变论文标题的符号。
- PASS±：其余条目的编号、作者、题名主体、年份与出处均能和原页对应；OCR 对重音和断行有可恢复伪影（例如 [20] 的 “Étale”、[24] 的 “Périodes p-adiques”、[29] 的 “Über”）。未发现条目遗漏。
- 证据：PDF p.51 文本层与整页 PNG；References [16]–[33] 与印刷原页逐项核对。

### 修复登记

- 修复前工作提交：a4506510a6d4b92d5af2c17def69499d9276a2f1；此提交中的目标 Markdown SHA-256 为 97b9a18436ab2c6caf5bf744a3ddffa6d5732b144c86a8584f9444b83c240337。
- 原始 MinerU 文件提交：a33f22f3b0bcf430149ea06d98e65076266acc9e；原始 Markdown SHA-256 为 97b9a18436ab2c6caf5bf744a3ddffa6d5732b144c86a8584f9444b83c240337。
- 修复提交：04f67d03a116a07f0cb23bd5693a191635719590；只改目标 MinerU Markdown。修复后 Markdown SHA-256 为 b1d9a9cacfb558bc708950583ba6d89f9591ebcc242a0ec9da6a29ed9ee981ed。
- 覆盖：原审计列出的 48 个 FAIL 页均已按页级记录修复；每项均以相应 PDF 文本层、整页 PNG 或该页 300dpi 裁片为依据，并在修复后全文复读中核对。页级 PASS± 记录仍保持原始审计结论，本登记不把修复冒充为重新分级。
- 额外审计更正：p.22 补入 Definition 5.3(iv) completion/torsion 参数与 M_* 次标记差异；p.32 补入两处 varpi-adic completion 差异；p.35 补入 epsilon 控制字符及另一处 varpi-adic completion 差异。p.28 原 FAIL 记录中的“line 1156 缺少 B 上划线”经原页与 Markdown 复核为误判，已从当前审计 owner 中移除；该行无需修复。
- 最终全文核对：从第 1 行读到文件末尾共 2180 行；逐项比对所有 FAIL 修复、原页证据与对应 Markdown 上下文。只读清点确认本次 FAIL 对应的 dollar-sign 记号、反引号 ell、U+000F、误写指数/态射和已列对象符号均已清除或纠正。U+0003 仍有 39 处（保留原有 MinerU 控制标记，未作批量修改）；源文打印 quirk 与 PASS± 排版瑕疵保留。

| PDF 页 | 修复内容 | 修复后核对 |
| --- | --- | --- |
| p.03 | Theorem 1.7 的 K-flat 目标；例中 T、p 指数与倾斜底域。 | 对照 p.3 页图及 Theorem 1.7 裁片。 |
| p.05 | ell-adic 系数域、V(-1)、gr_j^N V。 | 对照 p.5 monodromy 裁片。 |
| p.06 | tilde-X、Y 及 H^i 映射箭头。 | 对照 p.6 Lemma 1.15 裁片。 |
| p.07 | valuation 的 R 到 Gamma 映射、K 的乘法群商。 | 对照 p.7 valuation 裁片。 |
| p.08 | Tate algebra 的邻域基 aR_0。 | 对照 p.8 Definition 2.6 裁片。 |
| p.09 | rational subset 分母 g、k×、hat-B 与两个泛性质态射。 | 对照 p.9 Definition 2.13/Proposition 2.14 裁片。 |
| p.10 | rational denominator g、局部极大理想条件及 Theorem 2.17 的 If。 | 对照 p.10 sheaf 裁片。 |
| p.11 | 经典点求值映射 R 到 k。 | 对照 p.11 页图及 valuation-tree 图。 |
| p.12 | Theorem 2.21 目标集合后的多余上标 2。 | 对照 p.12 bijection 裁片。 |
| p.13 | formal scheme mathfrak-X、specialization morphism、closure U-bar。 | 对照 p.13 formal-model 裁片。 |
| p.14 | Berkovich/adic maps、retraction、kernel map、varpi 条件及 afinoid pair 箭头。 | 对照 p.14 map/varpi 裁片。 |
| p.15 | 两个 affinoid-pair 态射及 varpi-independence。 | 对照 p.15 filtration/varpi 裁片。 |
| p.16 | 三处 varpi 在 quotient、Remark 3.5 与 proof 中恢复。 | 对照 p.16 tilt-definition 裁片。 |
| p.17 | Proposition 3.8 多项式系数环 K^{flat-circle}[X]。 | 对照 p.17 polynomial-field 裁片。 |
| p.18 | varpi 参数、m 指标及 almost-Hom 下标。 | 对照 p.18 almost/Hom 裁片。 |
| p.19 | K-circle coefficient ring 与两处 epsilon。 | 对照 p.19 flatness 裁片。 |
| p.20 | 三条 unramified/étale morphism 的 A 到 B。 | 对照 p.20 定义文本层。 |
| p.21 | trace 记号、B/A 等态射、varpi-adic 条件与 Frobenius arrow。 | 对照 p.21 文本层。 |
| p.22 | K-circle-a/varpi base、torsion 条件、completion 条件及 M_*。 | 对照 p.22 perfectoid-definition 裁片。 |
| p.23 | epsilon、varpi-adic 条件、Lemma 5.7 的 k/p 指数与 Frobenius composite arrows。 | 对照 p.23 tilting-algebra 裁片。 |
| p.24 | Frobenius quotient 的自映射箭头。 | 对照 p.24 文本层。 |
| p.25 | S 到 S'、普通 prime、Phi 自映射与 Corollary 5.16 的 a 上标。 | 对照 p.25 deformation 裁片。 |
| p.26 | cotangent-complex triangle 三项与 varpi-adic completion。 | 对照 p.26 triangle 裁片。 |
| p.27 | Frobenius starred target、K-flat-circle base、varpi-adic completion。 | 对照 p.27 tilt/lift 裁片。 |
| p.28 | A[t^-1]、S_0-perp、R-circle、circ-a、epsilon arrow 与 varpi^N e。 | 对照 p.28 étale-proof 裁片；B-bar 保留原状。 |
| p.29 | epsilon 参数、b_i 上划线及 proof 中复用的 epsilon。 | 对照 p.29 étale-proof/epsilon-map 裁片。 |
| p.30 | Theorem 6.3 proof-outline 的 X 到 X-flat。 | 对照 p.30 页图。 |
| p.31 | 两处 X 到 X-flat、rational denominator g、varpi-adic completion。 | 对照 p.31 Lemma 6.4 裁片。 |
| p.32 | 一般 K 部分标题 (i) 到 (ii)；两处 varpi-adic completion。 | 对照 p.32 general-case 页图/裁片。 |
| p.33 | epsilon(c) 的普通集合成员符号。 | 对照 p.33 induction-condition 裁片。 |
| p.34 | varpi-adic completion 与 varpi-divisibility。 | 对照 p.34 divisibility 裁片。 |
| p.35 | X 到 X-flat、epsilon 参数、两处 varpi-adic completion。 | 对照 p.35 页图与 pfinite 裁片。 |
| p.36 | cohomology group 的 varpi-power annihilator。 | 对照 p.36 cohomology 裁片。 |
| p.37 | exactness 的 varpi-power、direct-limit object、K<T_i> 到 R、D 中的整闭包、source pair 态射、varpi 与 O_X^{circ-a}。 | 对照 p.37 direct-limit 裁片。 |
| p.38 | 两处 varpi 与纤维积图 X 到 Y 从 Z 到 Y。 | 对照 p.38 etale-topology 裁片。 |
| p.39 | Definition 7.1 affinoid-pair morphism arrow。 | 对照 p.39 Definition 7.1 裁片。 |
| p.40 | Y-flat 目标、D 而非 D_i、fibre-product equality、varpi-adic/直限条件。 | 对照 p.40 henselian-completion 裁片。 |
| p.41 | henselian varpi 与 direct-limit arrow；ordinary Spa。 | 对照 p.41 henselian-cover 裁片。 |
| p.42 | Corollary 7.8 与 Theorem 7.9 中 g、V/U、Y/X 四条态射。 | 对照 p.42 页图。 |
| p.43 | 两处 morphism of sites、O_X^{circ-a} 与 varpi-power。 | 对照 p.43 étale-cohomology 裁片。 |
| p.44 | inverse-limit definitions/directions、Y 到 X_i、Definition 7.14 引用。 | 对照 p.44 inverse-limit 裁片。 |
| p.45 | toric-space X 记号、k-circle、dual pairing brackets。 | 对照 p.45 toric-notation 裁片。 |
| p.46 | 两处 perfectoid toric-space X 记号及 étale-topoi morphism。 | 对照 p.46 tilt-comparison 裁片和图。 |
| p.47 | epsilon 参数、ell-adic 与 pro-ell 记号。 | 对照 p.47 epsilon/ell-adic 裁片。 |
| p.48 | Qbar-ell coefficient field、gr_j index、ell-adic、f 到 C minus x。 | 对照 p.48 representation/weight/proof 裁片。 |
| p.49 | Lemma 9.5 ell-adic 与 F_q((t)) Laurent-series field. | 对照 p.49 lemma95-field 裁片及交换图。 |
| p.50 | C_p-flat tilt 与三处 étale-site accents。 | 对照 p.50 étale-notation 裁片。 |
| p.51 | Reference [33] title 的 ell symbol。 | 对照 p.51 References 页图。 |
