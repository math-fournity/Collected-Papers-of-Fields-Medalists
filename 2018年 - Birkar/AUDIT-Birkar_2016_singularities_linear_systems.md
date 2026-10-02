# Birkar_2016_singularities_linear_systems — PDF/Markdown逐页对账

- Peer actor：`Peer-P13`
- Model / effort：`gpt-6-luna / max`
- PDF：`Birkar_2016_singularities_linear_systems.pdf`；`pdfinfo`记录46页，Creator为LaTeX with hyperref，Producer为dvips + GPL Ghostscript GIT PRERELEASE 9.22。
- 审计模式：born-digital；UTF-8 `pdftotext -layout`文本层153,141字节，未发现U+FFFD。文本层按PDF页逐页对账，题录页与密集数学页另作PNG目检；文本抽取不可靠的符号以原页图/300dpi裁片为终裁。
- Markdown：`Birkar_2016_singularities_linear_systems__Birkar_2016_singularities_linear_systems.md`；审计前SHA-256：`5beebf35a9c7e99f36509db38462da3ca95638ef66886378872acc6d89514a9f`。
- 候选基线：Peer工作树起始HEAD `037602429d3b009f6fc468c732073eb3ddf9875f`。审计开始前观察到main已推进至`e864b3b9dffc3456435c4bd5d0cd7553b3cd4cb8`（dispatch记录）；逐项比较确认本篇Markdown、索引登记与本篇目标路径未改变。此工作仍是基于`03760242`的候选，未集成。
- 审计范围：仅本PDF、上述MinerU Markdown、本篇AUDIT和此前缀专属`audit/`图像；PDF及其他MinerU资产只读。
- 初审基线：46个逐页条目按p.1–p.46顺序记录；修复前评级为39页FAIL、7页PASS±。本文件中的原始FAIL条目描述修复前差异，修复后逐处结果见末尾登记。
- 最终修复：修复了初审FAIL差异，并在全篇复读时补记和修复了遗漏差异。PASS±项目保持为轻微拼写/排版记录；它们不用于声称数学命题或证明有效。
- 修复前/后Markdown SHA-256：5beebf35a9c7e99f36509db38462da3ca95638ef66886378872acc6d89514a9f → 34c398ff3b9347d3d0ef166b1f744eef6d1936f9842a212b284529a03be38249。
- Markdown修复提交：353ad7fac129481dae280111b8f06a216b08dc01（精确目标文件单独提交）；候选仍基于037602429d3b009f6fc468c732073eb3ddf9875f，未集成。
- 修订后复核：完整回读Markdown第1行至第2343行，并按PDF p.1–p.46检查逐页内容；git diff --check通过。该检查仅支持PDF与Markdown内容忠实性，不认证定理或证明有效性。

## p.001（PDF p.1 / 印刷 p.1）
- PNG：`audit/Birkar_2016_singularities_linear_systems_p001.png`（Ghostscript `pngmono`，150dpi，1-bit）。
- 核对：题名、作者、摘要、目录条目、日期、MSC与关键词；对照PDF p.1完整文本层并目检整页PNG。
- 结果：**FAIL**——关键词末项MinerU为“minimal mode program”，原页印作“minimal model program”，错误替换了领域术语；全篇审计完成后按原页逐处手工修复。
- 次要差异：摘要中“different”被MinerU导出为“diferent”（少一个`f`）；词义可辨且不改变数学陈述，记为PASS±类OCR字形/拼写瑕疵，不据此单独批量修复。目录中缺少的子节编号与PDF目录一致，按印刷原样保留。
- 原文证据：PDF p.1关键词原文为“Keywords: Fano varieties, bounded families, linear systems, log canonical thresholds, minimal model program.”；题录页150dpi PNG可直接复核。
- 记录时间：2026-10-01 16:08 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：未另存；此born-digital页以完整PDF文本层为主证据，疑点均能由文本层辨认。
- 核对：目录续项“References 44”；引言开头、Fano有界性背景、Theorem 1.1陈述及例举已知情形前两条；逐项对照PDF p.2与MinerU p.2文本块及对应Markdown正文。
- 结果：**FAIL**——两处`Y → Z`箭头在Markdown中丢失：`Mori fibre space structure Y  Z [ 7 ]`及其后`general fibre of Y  Z`。原页分别印有“Y → Z [7]”和“Y → Z”；按原文逐处修复排版中的箭头表达。
- 次要差异：目录续项只保留“References”而省去原页页码44；`that`导出为`tha`，`pseudo-effective`/`differential`/`coefficients`各有少`f`的拼写瑕疵。这些未改变命题内容，记为PASS±类OCR瑕疵；不据此批量修复。
- 原文证据：PDF文本层原句为“the Mori fibre space structure Y → Z [7]”以及“A general fibre of Y → Z is a Fano variety X with terminal singularities.”；`pdftotext -f 2 -l 2 -layout`均保留箭头。
- 记录时间：2026-10-01 16:11 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p003_300dpi.png`（Ghostscript `pnggray`，300dpi；目检含疑点的整页）。
- 核对：已知Fano族列表、Examples 1.2–1.3、Corollary 1.4及其边界/线性等价条件；逐项比对PDF p.3文本层、300dpi原页和对应MinerU Markdown页块。
- 结果：**FAIL**——数学关系和符号有多处丢失/误增：`V₂ → V₁`、`Vₙ → Vₙ₋₁`、`X′ₙ → Xₙ`及“as n → ∞”中的箭头在Markdown缺失；集合条件`n ≥ 2`被导出成带额外双点的`stackrel{cdotcdot}{geq}`；首个参考文献`[8]`后多出原页不存在的`2`；Corollary 1.4的边界`Δ`被误成`Δ_{cdot}`。这些均可由PDF p.3原页及文本层直接裁定，待全篇审计后逐处手工修复。
- 次要差异：`coefficients`少一个`f`、`n ≥ 2`前的重复逗号等拼写/标点瑕疵，记为PASS±类；公式`K_{W_n}+(n-2)/n E=f^*K_{X_n}`及`2/n`系数、其余正文与印刷一致。
- 原文证据：300dpi原页清楚印出上述箭头、无双点的`≥`、`[8]`后逗号以及`(X, Δ)`与`K_X+Δ∼_R 0`；`pdftotext -f 3 -l 3 -layout`保留箭头和这些符号。
- 记录时间：2026-10-01 16:13 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p004_300dpi.png`（Ghostscript `pnggray`，300dpi；核对文字层疑点并目检本页正文和定义式）。
- 核对：对数Calabi–Yau有界性讨论、Cremona群Jordan性质及Corollary 1.5；核对`lct(X,B,L)`、`|A|_R`与全局阈值定义和两个等价式。
- 结果：**PASS±**——`Kähler-Einstein`在Markdown中编码为`K¨ahler-Einstein`，与原页中变音符位于`a`上方的`Kähler-Einstein`相比，重音位置错置但术语仍可辨，保留为轻微排版/编码瑕疵。其余本页陈述及阈值定义式与印刷一致。
- 原文/疑点裁定：原页300dpi图显示“McKernan”中的`c`为上标；Markdown的`M<sup>c</sup>Kernan`与印刷一致。`pdftotext`将它排成“Mc Kernan”是文本层位置顺序现象，不据此登记成Markdown差异。
- 记录时间：2026-10-01 16:14 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p005_300dpi.png`（Ghostscript `pnggray`，300dpi；目检定理1.8有界度数条件）。
- 核对：Theorem 1.6、Theorem 1.7及Theorem 1.8开头；阈值公式、假设项和`A^d`上界逐项对照PDF p.5及MinerU Markdown。
- 结果：**FAIL**——Theorem 1.8中原页条件为`A^d ≤ r`，Markdown写成`A^d ≤ r_i`，多出下标`i`；300dpi原页与PDF文本层均确认为无下标。另，原页在Theorem 1.8的三条假设前均有项目符号；Markdown只保留第二项的项目符号，使假设列表结构不完整。全篇审计完成后修正上界并恢复各假设的项目符号。
- 次要差异：`different`导出为`diferent`（两处，均少一个`f`）；这是可辨识且不改变阈值命题的拼写瑕疵，记为PASS±类，不单独批量修复。定理1.6、1.7的阈值不等式及其余假设与印刷一致。
- 原文证据：PDF p.5末段“Theorem 1.8”下原页印有三个项目符号；第二项末尾为`A^d ≤ r`。本页300dpi整页PNG清楚显示该列表和上界。
- 记录时间：2026-10-01 16:16 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p006_300dpi.png`（Ghostscript `pnggray`，300dpi；目检三组假设/结论列表和映射符号）。
- 核对：Theorem 1.8最后一条假设与阈值不等式；Theorem 1.9的假设、结论和补式；Sketch of the proof of Theorem 1.1开头列出的三个条件。
- 结果：**FAIL**——多处列表结构及映射符号丢失：Theorem 1.8最后一条`M ≥ 0`在Markdown缺少原页项目符号；Theorem 1.9中首条`(X,B)`假设、`M − (K_X+B)`假设及两条结论均缺少原页项目符号；证明Sketch开头`K_X`有m-complement、`|-mK_X|`给出双有理映射、`vol(-K_X) ≤ v`三条条件全部缺少项目符号。另，Theorem 1.9的映射`f : X → Z`被导出成`X Z`，并多出原页不存在的尾随`2`。全篇审计完成后按原页逐处修复。
- 原文证据：PDF p.6的300dpi整页图清楚显示Theorem 1.9六条假设和两条结论均带项目符号、`f : X → Z`箭头及三个证明条件的项目符号；PDF文本层同样保留映射箭头且不含尾随`2`。阈值不等式与补式内容和顺序一致。
- 记录时间：2026-10-01 16:17 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p007_300dpi.png`；`audit/300dpi/Birkar_2016_singularities_linear_systems_p007_L_300dpi.png`（300dpi整页及符号裁片）。
- 核对：Theorem 1.1证明Sketch的末项与说明、log-birationally-bounded段落、Theorem 1.6证明Sketch开头、discrepancy公式、映射及末行线性系统。
- 结果：**FAIL**——`V ⇢ X`的两处虚线箭头及`φ:Y → X`的两处映射箭头在Markdown中丢失；原页末行是`L ∈ |−K_X|_R`，Markdown在线性系统前误增`Ω`。此外原页写普通斜体`L_Y=φ^*L`，Markdown写成花体`\mathcal{L}_Y=φ^*\mathcal{L}`，改变了除子记号。全篇审计后按PDF p.7逐处修复。
- 源级文字差异：原页确实印作“Replacing X with can assume it is Q-factorial.”，缺少说明替换成什么的宾语；Markdown忠实保留。依据print优先原则不擅自补写，列入原刊文字quirk清单，不作OCR修复。
- 次要差异：`coefficients`等词有少`f`拼写，记为PASS±类。
- 原文证据：整页及L裁片显示两条`V ⇢ X`、两条`φ:Y→X`、普通斜体`L_Y=φ^*L`和`|−K_X|_R`；线性系统前无`Ω`。印刷“Replacing X with can assume…”仍是源级文字quirk，Markdown忠实保留。
- 记录时间：2026-10-01 16:18 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p008_300dpi.png`；`audit/300dpi/Birkar_2016_singularities_linear_systems_p008_T_300dpi.png`（Ghostscript `pnggray`，300dpi；第二张为疑点行裁片）。
- 核对：Theorem 1.6证明Sketch收尾及边界假设列表；Theorem 1.8证明Sketch的阈值、对数不连续度、双有理收缩和有限态射；比对PDF p.8、原页图与对应Markdown。
- 结果：**FAIL**——`X ⇢ V`、`V ⇢ X`、`Y → X`、`X → ℙ^d`四处箭头在Markdown丢失；`−(K_Y+T)`前误增第二个负号，成为`−- (K_Y+T)`；假设列表里的`ε″-lc for some fixed ε″ > 0`被多加尾随`2`；原文带引号的“degrees”误识别成`^{66}...^{55}`数字上标碎片。均按300dpi原页可辨内容列为全篇完成后的逐处修复项。
- 字形核实：PDF文本抽取未保留prime divisor中T上方的短横，但300dpi裁片清楚显示原文是带上横线的T；MinerU Markdown的`\overline{T}`忠实保留该字形，不登记为差异。其余本页不连续度公式及三个后续假设与原页一致。
- 原文证据：整页PNG显示双有理图、态射和否定号；T裁片显示该字形上方的横线。
- 记录时间：2026-10-01 16:21 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：未另存；本页疑点在born-digital PDF文本层中均可明确辨认，正文公式由文本层逐项核对。
- 核对：Theorem 1.8 Sketch收尾的双有理模型与 blowup 叙述；Acknowledgements；§2 Preliminaries开头、§2.1 Divisors与degree定义、volume公式。
- 结果：**FAIL**——Sketch中的态射`W → X`与`Y → X`在Markdown都丢失箭头；§2.1中原文为双有理映射`φ:X ⇢ Y`，Markdown误导出为普通箭头`φ:X → Y`，丢失了虚线性质。按原文恢复三处箭头类型。
- 次要差异：`coefficients`、`pseudo-effective`等出现少`f`拼写；致谢中`Păun`的重音被MinerU编码到错误字母前。这些不改变数学陈述，记为PASS±类拼写/编码瑕疵。volume的limsup定义式、取整符号及degree不等式与PDF文本层一致。
- 原文证据：PDF p.9文本层分别保留“Let W → X be the sequence…”, “If Y → X is the birational morphism…”及“φ:X 99K Y is a birational map…”；Markdown对照段中三处为无箭头或普通实线箭头。
- 记录时间：2026-10-01 16:23 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p010_300dpi.png`（Ghostscript `pnggray`，300dpi；核对核心定义、阈值条件与MMP合同记号）。
- 核对：§2.2 sub-pair/sub-lc/sub-klt/ε-lc定义、log discrepancy与Lemma 2.3；§2.4 Fano pairs；§2.5 minimal model和Mori fibre space定义。
- 结果：**FAIL**——§2.2对三种奇点条件的整段定义在Markdown严重乱码：sub-lc/sub-klt/sub-ε-lc及对应不等式被多次重复、拆序，条件无法忠实阅读；Lemma 2.3前件“ If”误成`H f`。此外四处箭头丢失/变型：log resolution`φ:W → X`、projective morphism`X → Z`、birational map`φ:X ⇢ Y/Z`（虚线）、extremal contraction`Y → T/Z`。全篇审计后依据原页逐处修复。
- 源级文字差异：原页写作“An non-klt place”，语法不规范；Markdown忠实保留，按print优先原则登记为source quirk而不改。
- 原文证据：p.10整页300dpi图及PDF文本层清楚给出各discrepancy条件：`a(D,X,B) ≥ 0`、`> 0`、`≥ ε`，并对应`coefficients of B_W ≤ 1`、`<1`、`≤1−ε`；原页亦显示上述四种映射关系。Lemma 2.3等式及Fano定义与印刷一致。
- 记录时间：2026-10-01 16:25 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p011_300dpi.png`（Ghostscript `pnggray`，300dpi；核对Lemma 2.7陈述及证明中的关系符和域标记）。
- 核对：§2.6、Lemma 2.7四项结论、证明中所有`Y`模型间态射、`Q`-线性等价式及`Γ_W`系数限制。
- 结果：**FAIL**——Lemma 2.7的第2–4条结论缺少印刷原页的项目符号；五处`Y → X`/`Y′ → Y″/X`箭头均丢失（包括引理态射、证明中的两种提取情况、后续收缩及末句所需态射）；`K_{Y′}+T′ ∼_Q 0/Y″`把下标Q误成O；“other coefficients … < 1”被导出为`< ~ 1`，多出波浪号。原页300dpi图逐项支持这些差异，待全篇审计后修复。
- 次要差异：`sufficiently`等词有少`f`拼写，另有重复句点；记为PASS±类拼写/标点瑕疵。Lemma公式`a(T,X,B)=a(T,X,Γ)=0`、pullback关系和其余不等式与原页一致。
- 原文证据：p.11整页300dpi图显示四项完整项目列表、所有五个映射箭头、Q域下标以及严格不等式`<1`。
- 记录时间：2026-10-01 16:26 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：未另存；本页所有关系符和量词都能由born-digital PDF文本层直接辨认。
- 核对：Lemma 2.7证明第二种情形；§2.8 birationally bounded / couples 定义；Theorems 2.10–2.11；§2.12 n-complement三项条件。
- 结果：**FAIL**——§2.8中多个族参数态射`V^i → T^i`、`C^i → T^i`及birational isomorphism`φ:V_t^i ⇢ X`在Markdown中缺箭头或损坏成无效符号，改变了定义中族、纤维和对象间的关系。关于`(X,B)`的系数条件中，原文“coefficients of B”被误成`B_{;}`。§2.12的三项n-complement条件在Markdown缺少原页项目标记。另，Lemma 2.7证明中的“other coefficients … < 1”仍被写成`< ~ 1`，多出波浪号；与p.11相同。
- 次要差异：有少`f`拼写（如`coefficients`），不改变陈述。Theorems 2.10–2.11的有效性界、体积上界、`|−mK_X|`及`n(K_X+B^+)∼0`等内容与PDF文本层一致。
- 原文证据：PDF p.12文本层明确写出`V^i → T^i`、`C^i → T^i`及`φ:V_t^i 99K X`，且n-complement结论下有三项独立项目；Markdown对应处的箭头形式及项目标记不完整。
- 记录时间：2026-10-01 16:28 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：未另存；本页用于判定的箭头、集合条件及假设均在born-digital PDF文本层中保留。
- 核对：Theorem 2.13的complement假设与结论、§2.14及Theorem 2.15有界性条件、§2.16 blowup sequence定义。
- 结果：**FAIL**——§2.16(1)三处态射箭头在Markdown丢失：每步blowup`X_{i+1} → X_i`、最后一步`X_p → X_{p−1}`及exceptional divisor所对应的`X_{i+1} → X_i`。另外，Theorem 2.13、Theorem 2.15的多条假设在Markdown丢失原页项目标记；文本仍分行，但不能忠实呈现各自的完整项目列表。按原页修复态射表达及列表格式。
- 原文证据：PDF p.13文本层显示Theorem 2.13和2.15的项目列表，并明确写出“each `X_{i+1} → X_i` is the blowup”及“the last blowup `X_p → X_{p−1}`”。MinerU段落中对应箭头缺失。
- 记录时间：2026-10-01 16:29 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：未另存；相关blowup态射在born-digital PDF文本层中可辨，公式内容亦可直接对账。
- 核对：Lemma 2.17递推不等式及证明；§2.16(3)的centre blowup定义；§2.18 Analytic pairs定义开头。
- 结果：**FAIL**——Lemma 2.17证明中`φ_i:X_i → X_0`的箭头在Markdown缺失；§2.16(3)中`T`作为exceptional divisor的`X_p → X_{p−1}`以及最终序列`X_p → X_{p−1} → ··· → X_0=X`各箭头都丢失。按原文恢复态射方向。
- 次要差异：`coefficients`少`f`等拼写瑕疵不改变条件；Lemma 2.17中的`μ_{E_p}φ^*Λ ≥ p+1`和递推式与PDF一致，§2.18定义开头的对象与映射内容一致。
- 原文证据：PDF p.14文本层清楚显示`X_i → X_0`、`X_p → X_{p−1}`及逐级blowup序列箭头；对应Markdown分别为空缺。
- 记录时间：2026-10-01 16:29 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：未另存；本页态射箭头、分歧条件和交数上界均可由born-digital PDF文本层直接核对。
- 核对：§2.18 analytic neighbourhood例子收尾；Lemmas 2.20–2.21的étale映射条件；§2.22 toric MMP映射；Lemma 2.24的有界小修改条件。
- 结果：**FAIL**——四处映射箭头在Markdown缺失：Lemma 2.20的有限态射`π:X → Z`、§2.22的toric morphism`X → Z`与 blowup `Y → X`、Lemma 2.24的small birational morphism`φ:Y → X`。此外Lemma 2.20中`C := π(B) := Σ b_jπ(B_j)`原是第四条假设，但Markdown从第三个项目直接接显示公式；Lemma 2.24的第一条假设`(X,B)`前同样缺项目标记。按原文修复。
- 次要差异：`étale`的重音编码成前置撇号样字符；Lemma 2.24句子中`A_Y`在“very ample divisor ... on Y”处被写为`A`，后文公式仍用`A_Y`，因此不改变可识别对象，记为PASS±。
- 原文证据：PDF p.15文本层分别显示上述四种映射、Lemma 2.20完整四项假设及Lemma 2.24两项假设。阈值等价、局部参数条件和`A^d ≤ r`与原文一致。
- 记录时间：2026-10-01 16:31 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：未另存；本页map箭头和半ample推论公式均在born-digital PDF文本层中清楚。
- 核对：Lemma 2.24结论余项及证明；§2.25、Lemma 2.26的收缩和semi-ample推论。
- 结果：**FAIL**——Lemma 2.24证明中多处族/纤维/双有理态射箭头丢失：`V^i → T^i`、`W → V`、`U → T`、`V → T`、`φ:Y → X`及`U → V`。Lemma 2.26首句的contraction`Y → X`也被导出成`Y X`。另外Lemma 2.24结论剩下三项`K_Y`为Q-Cartier、`A_Y^d ≤ l`、`A_Y−φ^*A` ample均缺原页项目符号。按原页恢复关系箭头并补全列表。
- 原文证据：PDF p.16文本层逐项显示上述箭头以及Lemma 2.24四项结论的项目符号；Markdown对应位置将箭头省略，并将p.16的三项结论写成无项目符号的独立行。Lemma 2.26公式`C+tbA=(1−t)C+t(C+bA)`与取`t=a/b`均匹配原文。
- 记录时间：2026-10-01 16:32 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.017（PDF p.17 / 印刷 p.17）
- PNG：未另存；本页证明Sketch关系符、阈值条件和常数均在born-digital PDF文本层中可读。
- 核对：§3开头的R-linear anticanonical system；Proposition 3.1三项假设与结论；证明Steps 1–3的birational-map方向、系数常数及discrepancy等式。
- 结果：**FAIL**——两处`V ⇢ X`虚线映射在Markdown缺失箭头；同一量词句中本应为普通常数`c ∈ ℝ_{>0}`却误加点号，随后上界又写作普通`c`，产生符号不一致。按PDF原文统一为普通`c`并恢复虚线箭头。Proposition 3.1第三条假设的项目符号也遗漏，但该行仍单独列出。
- 原文证据：PDF p.17文本层在Step 2和Step 3均显示`V 99K X`；Step 2的常数原文为`c ∈ ℝ_{>0}`，不是带点的c。`L ∼_R uT`、`ε′`与log discrepancy式未见内容差异。
- 记录时间：2026-10-01 16:32 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.018（PDF p.18 / 印刷 p.18）
- PNG：未另存；本页线性等价、不等式与degree记号在born-digital PDF文本层中均可核对。
- 核对：Proposition 3.1的Proof Steps 4–6；下界`deg_H Γ_V`推理、边界`Δ`构造、Theorem 1.8应用及Lemma 3.2证明开头。
- 结果：**FAIL**——Step 5原文要求`lH − Λ` ample，Markdown在该处把`Λ`误成`N`；同页下一式仍使用`Λ`，但两处不一致。Step 6的degree记号`deg_H M`被误植成带杂符号的degree下标，再接`_H M`，破坏了原文公式。
- 修复补充：Step 5内部交叉引用已恢复为原页的“by Step 3”；其余公式与PDF一致。
- 原文证据：PDF p.18文本层对应原文为“there is a bounded number l … such that lH − Λ is ample”及“the degree deg_H M = deg_H(ψ_*φ_*Ω) is bounded from above”；Markdown相应位置分别出现N与变形下标。
- 记录时间：2026-10-01 16:36 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.019（PDF p.19 / 印刷 p.19）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p019_300dpi.png`；`audit/300dpi/Birkar_2016_singularities_linear_systems_p019_L_300dpi.png`（Ghostscript `pnggray`，300dpi；第二张为L符号裁片）。
- 核对：Theorem 1.6证明Sketch后半部；两种`φ:Y→X`情形、MMP得到的`Y′→Z′`及其一般纤维；核对`L_Y`记号和后续系数估计。
- 结果：**FAIL**——四处态射箭头在Markdown缺失：两处`φ:Y → X`、Mori fibre space映射`Y′ → Z′`及随后的一般纤维映射`Y′ → Z′`。此外，原页为普通数学斜体`L_Y=φ^*L`，Markdown误写成花体`ℒ_Y=φ^*ℒ`，改变了该除子符号。均按p.19原页逐处修复。
- 原文证据：整页PNG显示所有映射箭头；`p019_L`裁片直接显示普通斜体`L_Y=φ^*L`，可与Markdown中的`ℒ_Y`花体区分。`a(T,X,B+sL)=ε′`、系数不等式及其后的相对nef/big关系与印刷一致。
- 记录时间：2026-10-01 16:38 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.020（PDF p.20 / 印刷 p.20）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p020_300dpi.png`（Ghostscript `pnggray`，300dpi；核对`φ_i`目标、`H_i′`字形及Mori fibre space箭头）。
- 核对：Proposition 3.4与Step 1目标；Step 2的`H_i`选择、LC-place收缩、birational transforms及补式；Step 3的MMP输出与LC性质。
- 结果：**FAIL**——Step 2第二种极端收缩中，原页目标是`φ_i:X_i′ → X`，Markdown给目标X误加上横线；Step 2概述中的contractions`X_i′ → X`及Step 3 Mori fibre space`X_i″ → Z_i″`在Markdown丢失箭头。另，原页使用普通斜体`H_i′=φ_i^*H_i`，Markdown把两处`H_i′/H_i`误成花体H，改动了除子记号。均以p.20 300dpi原页为据修复。
- 原文证据：整页PNG清楚显示第二映射的目标为普通`X`、`H_i′=φ_i^*H_i`为普通H，以及`X_i″→Z_i″`。Theorem条件、极限序列` t=lim t_i`与nef/big等式内容一致。
- 记录时间：2026-10-01 16:40 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.021（PDF p.21 / 印刷 p.21）
- PNG：未另存；Mori fibre space关系、LC阈值及不等式在born-digital PDF文本层中清楚。
- 核对：Proposition 3.4 Steps 3–5；Mori fibre space的base、一般纤维限制、Step 4构造D及Step 5有理系数论证。
- 结果：**FAIL**——两处`X_i″ → Z_i″`箭头丢失：一处陈述MMP结束于Mori fibre space，另一处用于“restricting to the general fibres”。按PDF页21恢复态射关系。
- 次要差异：未发现其他会改变本页数学陈述的差异；目标等式`lct(X,B,D)=t`、`e∈(0,t)`及导致矛盾的`lct(X,B,D)≤e<t`均和印刷一致。
- 原文证据：PDF p.21文本层在“Now assume the MMP ends…”与“restricting to the general fibres…”两处都明确写为`X_i″ → Z_i″`；Markdown两个位置均未保留箭头。
- 记录时间：2026-10-01 16:42 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.022（PDF p.22 / 印刷 p.22）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p022_300dpi.png`（Ghostscript `pnggray`，300dpi；核对floor记号、Proposition 4.1假设与邻域补式）。
- 核对：§4开头及Proposition 4.1两项附加假设；Step 1插值恒等式、边界floor关系；Step 2对S作adjunction后的系数集与补式。
- 结果：**FAIL**——Proposition 4.1原文是`S = ⌊Γ⌋`，Markdown将floor记号误写为`S = |Γ|`，变成绝对值式；第二项假设`αM − (K_X+Γ)` ample在Markdown缺少原页项目符号。原页300dpi图清楚显示floor括号和完整项目列表，待全篇审计后逐处修复。
- 原文证据：p.22整页PNG显示两项假设均带bullet，且`S`等于`Γ`的floor；插值等式、`K_S+B_S`的adjunction式和`n`-complement结论与原页一致。
- 记录时间：2026-10-01 16:44 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.023（PDF p.23 / 印刷 p.23）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p023_300dpi.png`（Ghostscript `pnggray`，300dpi；核对round-down/fractional-part记号和S的对象索引）。
- 核对：Proposition 4.1 Step 3的分解及pullback；Step 4边界`Θ′`、`P′`系数定义、fractional part及`P′ ≥ 0`论证开头。
- 结果：**FAIL**——Step 3中原页为`S′`是`S`的birational transform，Markdown多加下标写成`S_i`；对应态射`ψ:S′→S`仍将底对象定为S。Step 4推导`μ_{D′}P′`时，原文末式使用floor括号`⌊ Γ′−Δ′+⟨(n+1)Δ′⟩ ⌋`，Markdown却变成绝对值竖线`|...|`，改变了定义运算。以p.23原页逐处修复。
- 原文证据：p.23整页PNG清楚显示`S′`由`S`变换而来，并在系数恒等式中两侧使用floor括号；原Markdown分别有`S_i`和竖线绝对值。
- 记录时间：2026-10-01 16:46 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.024（PDF p.24 / 印刷 p.24）
- PNG：未另存；本页所有公式和floor/fractional-part运算均可由born-digital PDF文本层核对。
- 核对：Proposition 4.1 Steps 5–6；限制映射的上同调消失、补式在S′上的限制、floor与fractional-part恒等式及有效性论证。
- 结果：**PASS±**——数学等式、不等式、整数性与`⌊(n+1)Δ′⌋|S′ = ⌊(n+1)Δ′|S′⌋`均与PDF文本层一致。Markdown多处把`effective`拼成`efective`、把`coefficients`拼成`coeficients`，属于可辨且不改变内容的`ff`连字类拼写瑕疵。
- 原文证据：PDF p.24文本层与MinerU对应块在`L′+P′`分解、`H^0`限制映射、`nN′|S′`补式推导及系数估计上吻合。
- 记录时间：2026-10-01 16:47 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.025（PDF p.25 / 印刷 p.25）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p025_300dpi.png`；`audit/300dpi/Birkar_2016_singularities_linear_systems_p025_L_symbols_300dpi.png`；`audit/300dpi/Birkar_2016_singularities_linear_systems_p025_L_eq_300dpi.png`（Ghostscript `pnggray`，300dpi；后两张用于裁定花体/斜体L与round-down括号）。
- 核对：Proposition 4.1 Step 7的补式构造与`B^+`记号；Step 6中的`nR′`、限制到S′的系数公式；S上邻域的连通性论证。
- 结果：**FAIL**——`nR′`定义及后续限制公式中，原文两处都用floor括号`⌊(n+1)Δ′⌋`，Markdown误成绝对值竖线`|(n+1)Δ′|`，改变了round-down运算。原文写`S`为唯一与S相交的non-klt centre，Markdown误加圆圈下标变成`S_⊙`。此外原式区分calligraphic `𝓛`与普通`L`（`𝓛=L+P∼G`），Markdown把两种字形都写成普通L，变成自我等式`L=L+P`。以上均由p.25 300dpi原图/裁片确认，待全篇审计后逐处修复。
- 原文证据：全页图显示floor brackets与无下标的S；`p025_L_symbols`及`p025_L_eq`裁片显示第一个L为花体、加号之后的L为普通斜体。`Lambda=B^+=B+R`、补式`n(K_X+B^+)∼(n+2)M`及连通性论证其余等式与印刷一致。
- 记录时间：2026-10-01 16:50 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.026（PDF p.26 / 印刷 p.26）
- PNG：未另存；本页收缩箭头和数值线性等价在born-digital PDF文本层中明确。
- 核对：Theorem 1.9证明Step 1末尾的contraction`X → U`及`U ⇢ Z`映射；Steps 2–4中MMP、`X → V/U`、非收缩S论证与Lemma 2.7引入的双有理态射。
- 结果：**FAIL**——开头`X → U`的birational contraction在Markdown写成`X U`；Lemma 2.7引入的`φ:Y → X`以及紧随其后的“either `Y → X` is small”中箭头也都缺失。按原文恢复映射关系。
- 原文证据：PDF p.26文本层分别显示`X → U`，Lemma 2.7所需态射`Y → X`，以及small/contracting divisors的条件；`U ⇢ Z`、`X → V/U`及凸组合等式与Markdown一致。
- 记录时间：2026-10-01 16:51 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.027（PDF p.27 / 印刷 p.27）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p027_300dpi.png`（Ghostscript `pnggray`，300dpi；目检Lemma 2.7列表与Proposition 5.2的交数/交集记号）。
- 核对：Proposition 4.1余下三条Lemma 2.7结论及`Δ ≤ B`；§5/§5.1开头；Proposition 5.2的divisor-index范围、stratum假设、映射条件和degree上界。
- 结果：**FAIL**——Lemma 2.7剩余三项结论原有项目符号，Markdown均缺失；原文`Δ ≤ B`被多加尾随`2`。Proposition 5.2假设列表中的`Supp B`条目及结论列表的多条映射/degree条件缺少项目符号；`deg_{H_i} C`被误成`de β_{H_i} C`，损坏了degree记号。PDF p.27命题假设为x ∈ ⋂_1^d S_i，Markdown原先遗漏下限1，已恢复。证明内的求和/交集则沿用原刊只写数字下限的简写，并未遗漏i=。
- 原文证据：p.27整页300dpi图显示Lemma结论的三个bullet、无尾随数字的`Δ ≤ B`、degree写作`deg_{H_i} C`以及Proposition 5.2的列表结构；求和/交集下限按原页均只印数字1。
- 次要差异：`étale`的重音编码不正确，但术语仍可辨，记为PASS±类拼写/编码瑕疵。
- 记录时间：2026-10-01 16:53 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.028（PDF p.28 / 印刷 p.28）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p028_300dpi.png`（Ghostscript `pnggray`，300dpi；核对求和/交集范围、degree下标及Lemma 5.4假设）。
- 核对：Proposition 5.2证明中R_i/S_i求和与交集的印刷下限简写；Lemma 5.4三项有界度量条件及其degree上界。
- 结果：**FAIL**——Lemma 5.4中第二条件被误成`A^d ≤ r_i`，原页为`A^d ≤ r`。另外，Lemma 5.4的三条条件在Markdown均缺原页项目符号；degree记号`deg_{H_i} C`被OCR误成`de β_{H_i} C`，已经不可忠实读取。PDF及Markdown都按原刊记作`∑_1^d`、`∑_0^d`、`⋂_1^d`，未增写`i=`，这不是OCR差异。
- 原文证据：p.28整页300dpi图清楚显示无下标i的`r`、三条bullet、`deg_{H_i}C`以及下限只标数字的求和/交集简写；PDF文本层与原页图一致。
- 记录时间：2026-10-01 16:54 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.029（PDF p.29 / 印刷 p.29）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p029_300dpi.png`（Ghostscript `pnggray`，300dpi；核对Proposition 5.5条件、指标范围及degree符号）。
- 核对：Proposition 5.5八项假设与有界序列结论；证明Step 1有限态射输入及Step 2的`Θ`、centre blowup序列。
- 结果：**FAIL**——Proposition 5.5中`A^d ≤ r`被误成`A^d ≤ r_i`；`deg_A Λ ≤ r`误成`deg_A Δ ≤ r_`；zero-dimensional stratum条件后多出数字`2`。多条假设失去原页bullet；`deg_{H_i}C`再次损坏成`deβ_{H_i}C`。PDF与Markdown的`∑_1^dS_i`、`∑_1^dH_i`、`⋂_1^dS_i`均沿用原刊省略变量的下限简写，先前将其称为丢失`i=`不成立。
- 原文证据：p.29整页300dpi图显示无下标的`r`、`deg_A Λ`、无尾随数字的stratum条件、degree写作`deg_{H_i}C`和各项bullet；求和/交集的下限按原页只印1。
- 记录时间：2026-10-01 16:56 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.030（PDF p.30 / 印刷 p.30）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p030_300dpi.png`（Ghostscript `pnggray`，300dpi；核对Step 3的degree表达式及discrepancy公式）。
- 核对：Proposition 5.5 Step 2的解析邻域传递与中心爆破序列；Step 3中stratum `G`的degree估计和adjunction式；Step 4中辅助边界的ε′-lc估计。
- 结果：**FAIL**——原文估计为`deg_{H′}(C|_G) = deg_H C ≤ r`；Markdown中的degree运算符损坏成`de`加额外上标碎片（`zg`），接着才出现下标`H′`，已经无法忠实辨认该不变量。依照原页恢复degree记号。
- 原文证据：p.30文本层给出`deg_{H′} C|_G = deg_H C ≤ r`，整页300dpi图清楚显示`deg`及下标H′；相邻的discrepancy、ε′及convex-combination公式与PDF一致。
- 记录时间：2026-10-01 16:59 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.031（PDF p.31 / 印刷 p.31）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p031_300dpi.png`（Ghostscript `pnggray`，300dpi；核对Step 5的MMP对象及degree公式）。
- 核对：Proposition 5.5 Step 4凸组合延续、Step 5 toric complement、Step 6 degree界和blowup长度界；Proposition 5.7假设开头。
- 结果：**FAIL**——Step 5原文是在weighted blowup`W′`上运行`−K_{W′}`的MMP；Markdown写成`−K_W`，漏掉prime并更换了运行对象。Step 6原文的度数式`deg_{H_i} Ω = d+1`被破坏成额外点号/乱码字形。Proposition 5.7开头的若干假设还失去原页bullet标记。以上以本页300dpi图为准修复。
- 原文证据：p.31整页图清楚显示`−K_{W′}`、MMP后`W″`、`deg_{H_i}Ω=d+1`及Proposition 5.7逐项假设；PDF文本层与图像支持相同内容。
- 记录时间：2026-10-01 17:01 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.032（PDF p.32 / 印刷 p.32）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p032_300dpi.png`（Ghostscript `pnggray`，300dpi；核对假设列表、integrality条件和中心/收缩映射）。
- 核对：Proposition 5.7最后两项假设；Lemma 5.8的hyperplane restriction设置、adjunction等式、八项条件及系数界转移。
- 结果：**FAIL**——Proposition 5.7中`a(T,X,B)≤1`原有项目符号在Markdown缺失。Lemma 5.8里原条件`nΛ_H` integral被多插入`iota`；“T is a divisor on U”误成“on U_i”。证明中`φ:W → X`、`T → C`和诱导收缩`G → H`的箭头均缺失。Lemma 5.8多项假设的项目标记也未保留。p.32 300dpi原页逐项可裁定。
- 原文证据：整页PNG明确印出`nΛ_H integral`、`T`是`U`上的divisor，并显示上述三个箭头及逐条项目符号；adjunction pullback等式和最后的系数上界与印刷一致。
- 记录时间：2026-10-01 17:03 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.033（PDF p.33 / 印刷 p.33）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p033_300dpi.png`（Ghostscript `pnggray`，300dpi；核对Step 1的替换变量与Step 2的ε/2界）。
- 核对：Proposition 5.7证明Steps 1–3开头；blowup映射、替换后的变量列表、hyperplane restriction记号和外部有限点处的奇点界。
- 结果：**FAIL**——Step 1的blowup`X′ → X`在Markdown缺箭头；变量替换清单中的`X′`被误加点号成`\dot X′`。Step 2原文两处界都是`ε/2-lc`：Markdown第一处把分数丢失，只余ε，第二处把分母2排成ε的下标2。另，原页限制记号为`A_H=A|_H`，Markdown误加上波浪号为`A_H=~(A|_H)`。这些差异改变了映射、变量/限制及奇点界的表达，须按p.33原页修复。
- 修复补充：Step 2对(H,B_H)、A_H、A_H−B_H三项条件原先缺少的项目符号已逐项恢复；其余凸组合等式与印刷一致。
- 原文证据：p.33整页300dpi图显示普通`X′`、映射箭头`X′→X`、无tilde的`A_H=A|_H`及分数`ε/2`两处。
- 记录时间：2026-10-01 17:05 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.034（PDF p.34 / 印刷 p.34）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p034_300dpi.png`（Ghostscript `pnggray`，300dpi；核对log discrepancy系数、ε/2条件和MMP态射）。
- 核对：Proposition 5.7 Step 3中`Γ_V`的两种系数展开、Step 4的MMP收缩对象、Step 5的`D_Y`构造及其pullback分解。
- 结果：**FAIL**——原文`μ_TΓ_V = 1−a`后Markdown误加尾随数字`2`；页末关于`(X,B+tB)`的`ε/2-lc`条件被写成ε的下标2，丢失了分母结构。Step 4所定义的对应态射`π:Y → X`也缺少箭头。均由本页300dpi图核实，待修复。
- 原文证据：p.34整页图显示`μ_TΓ_V=1−a`、`rac{ε}{2}`及`π:Y→X`；两个含求和的`F`、`G`定义和`D_Y`线性等价式其余部分与原页一致。
- 记录时间：2026-10-01 17:07 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.035（PDF p.35 / 印刷 p.35）
- PNG：未另存；本页各degree不等式、系数界与ample关系均由born-digital PDF文本层直接核对。
- 核对：Proposition 5.5 Step 5的`D_Y`定义与推前；Step 6的ε-lc验证、`a(T,X,D)`系数估计和`3mA−D`的三个ample项；Step 7 blowup长度后的degree上界。
- 结果：**PASS±**——主要数学陈述、交数不等式和pullback/pushdown关系均与PDF文本层一致；`coefficients`、`effective`等出现少`f`的拼写瑕疵，按常见`ff`连字识别问题记为PASS±，不改变本文推理。
- 原文证据：PDF p.35文本层对应`D = H+B`、`D ∼_R (K_X+B+3dA)/t+B`、`3mA−D`分解及`μ_T ν^*L ≤ deg_J ν^*L ≤ J^d ≤ q`，与MinerU对应段落吻合。
- 记录时间：2026-10-01 17:26 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.036（PDF p.36 / 印刷 p.36）
- PNG：未另存；本页系数界、nef/ample条件及凸组合等式均能由born-digital PDF文本层逐项对照。
- 核对：Proposition 5.7证明对`J_W`系数下界的论证、`Δ_W`构造、ε′-lc与discrepancy上界、ample divisor条件；Lemma 5.9证明开头。
- 结果：**PASS±**——相关系数不等式、pullback关系、`α`凸组合及半倍`A_W`的ample条件均与PDF文本层一致。Markdown有少`f`拼写、`qif`空格粘连及“exceptional/Xprime divisor”词间空格缺失，记为PASS±排版/OCR瑕疵，不改变本页推理。
- 原文证据：PDF p.36文本层与对应MinerU内容在`J_W ≤ B_W`、`A_W−Δ_W`分解、`αa(T,X,B)≤1`及以Lemma 5.9收尾的逻辑顺序一致。
- 记录时间：2026-10-01 17:43 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.037（PDF p.37 / 印刷 p.37）
- PNG：未另存；本页假设区间、ε′/2界及ample等式在born-digital PDF文本层中清晰。
- 核对：§5.10引入；Proposition 5.11的完整假设与结论；Proof开头的ACC选择、Step 1的外部有限点lc界及hyperplane restriction条件。
- 结果：**FAIL**——Proposition 5.11中多条假设没有保留原页bullet：`(X,B)`、`A^d≤r`、`L≥0`、`A−B/A−L ample`及`(X,B+tL)`均被排成无项目符号行；结论`nΛ` integral、`mA−Λ` ample、`(X,Λ)` lc near x也缺原页bullet。它们仍各自分行，但不能准确呈现完整列表。全篇审计后恢复列表结构。
- 次要差异：Proof中“Let X,B,A,L,T,t as in the proposition”误多写一个`t`成`tt`，记为PASS±多字瑕疵，不代表新变量。Step 1的`ε′/2-lc`、`(r+1)A−B−tL`分解和限制后degree界与原文一致。
- 原文证据：PDF p.37文本层显示Prop. 5.11七项假设和四项结论均用bullet，且`tt`只有一个`t`；Proof中的公式/参数与Markdown内容吻合。
- 记录时间：2026-10-01 18:04 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.038（PDF p.38 / 印刷 p.38）
- PNG：未另存；本页`ε′/2`阈值、对数discrepancy系数和映射对象在born-digital PDF文本层中可判。
- 核对：Proposition 5.7 Proof Step 1结尾及Step 2边界`Γ_W`定义、exceptional divisor索引、`F/G`分解与系数界。
- 结果：**FAIL**——Step 2中`log resolution ψ:W → X`的箭头在Markdown缺失；“neighbourhood of H”误写成`H_{;}`；“exceptional divisors of ψ other than T”误写成“other than T_i”。两处下标引入了原页不存在的标记，需按p.38文本层逐处修正。
- 原文证据：PDF p.38文本层明确给出`ψ:W → X`、`near H`与“other than T”；`a_i`和`a_i′`仅用于exceptional divisors `E_i`，没有`T_i`。Step 1及Step 2中的ε′/2阈值公式与原文相符。
- 记录时间：2026-10-01 18:27 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.039（PDF p.39 / 印刷 p.39）
- PNG：未另存；Step 3–5的态射/双有理图关系在born-digital PDF文本层中可辨。
- 核对：Proposition 5.7 Steps 3–5；`MMP`模型`Y′`、含T的极端收缩`Y″`、ample model Y及它们间的双有理关系。
- 结果：**FAIL**——Step 3的诱导态射`Y′ → X`、Step 4的birational contraction`Y″ → X`与morphism`φ:Y → X`在Markdown缺箭头；末句的`Y ⇢ Y′`虚线箭头误成仅有破折号的文本。原PDF页39明确给出这些不同的映射关系，须恢复箭头类型。
- 原文证据：PDF p.39文本层分别出现`Y′ → X`、`Y″ → X`、`φ:Y → X`及`Y 99K Y′`；对照Markdown对应位置的箭头为空或仅有破折号。系数`ε′/2`界、MMP对象及Step 5对偶性关系与原文一致。
- 记录时间：2026-10-01 23:14 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.040（PDF p.40 / 印刷 p.40）
- PNG：未另存；纤维态射、pushdown来源与degree上界均在born-digital PDF文本层中可辨。
- 核对：Proposition 5.7 Step 5非收缩曲线上的nef论证；Step 6对`lA_Y−(K_Y+(1−ε′)T_Y)`ample的控制及相关度量上界。
- 结果：**FAIL**——`P_{Y′}`不与`Y′ → X`在φ(c)上的纤维相交一语在Markdown缺失箭头；紧接的定义应为“P_Y是P_{Y′}在Y上的pushdown”，Markdown把来源也写成P_Y，丢失了prime。另，Step 6原文条件`A^d ≤ r`在Markdown变成`A^d ≤ r 2`，多出数字2。根据p.40 PDF文本层逐处修复。
- 原文证据：PDF p.40文本层保留`Y′ → X`及`P_Y is the pushdown of P_{Y′} to Y`，上界只写`A^d ≤ r`；其余ample分解和`l`选择推理一致。
- 记录时间：2026-10-01 19:54 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.041（PDF p.41 / 印刷 p.41）
- PNG：未另存；本页ample分解、不等式和complement等式均由born-digital PDF文本层核对。
- 核对：Proposition 5.11 Proof Steps 7–8；参数`α`上界、三项ample分解及Theorem 1.9输入和complement等式。
- 结果：**PASS±**——关键式`3lA_Y−(K_Y+T_Y)`的分解、`l ≥ (1+r)ε′/(ε−ε′)`推出的nef项、`K_Y+Γ_Y+3dA_Y` ample项及`n(K_Y+Λ_Y)∼(n+2)lA_Y`均与原页文本一致。Markdown在`l≥(1+t)α`后有多余句点，并在括号化的Theorem 1.9参数末尾多一个右括号；记为PASS±标点瑕疵。
- 原文证据：PDF p.41文本层与Markdown中的Step 7代数分解、Step 8的`M=lA_Y, S=T_Y, z=x`和补式相符。
- 记录时间：2026-10-01 20:08 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.042（PDF p.42 / 印刷 p.42）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p042_300dpi.png`（Ghostscript `pnggray`，300dpi；核对`C`符号和Step 2的small morphism）。
- 核对：Theorem 1.9结尾的Λ pushdown及补式；§6开头；Proof of Theorem 1.8 Steps 1–3，尤其Lemma 2.24引用和定义`C`。
- 结果：**FAIL**——Lemma 2.24导出的small projective birational morphism`φ:Y → X`在Markdown丢失箭头；Step 3本应将`C`定义为`C := 1/2 A`，Markdown多加点号写成带点的C，后续阈值表达沿用C，使变量名称不一致。Lemma 2.24结论中的第二条`A_Y^d≤l`及`A_Y−φ^*A`在Markdown缺少原页项目符号。
- 原文证据：PDF p.42整页300dpi图显示普通无点的`C`、态射`φ:Y→X`和Lemma 2.24两条结果bullet；其他`lct`缩放恒等式和`n(K_X+Λ)∼(n+2)lA`均与原文一致。
- 记录时间：2026-10-01 20:27 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.043（PDF p.43 / 印刷 p.43）
- PNG：未另存；Step 4–6的有理数、阈值不等式与倍数取整在born-digital PDF文本层中清楚。
- 核对：Lemma 5.9证明开头；Proposition 5.11产物的再次应用；Step 4闭点约化、Step 5对`t`的正下界及Step 6把`A−B`扩大为ample的论证。
- 结果：**PASS±**——数学命题、`t`下界`(ε−ε′)/q`及`e=⌈(3d+1)/s⌉`和PDF文本层吻合。Proposition 5.11的四项结果在Markdown中只有末项保留项目符号，其余仍逐行完整陈述；另有`(3d+1)A`附近多出的点状排版符号。记为不改变本页数学关系的PASS±格式瑕疵。
- 原文证据：PDF p.43文本层显示`M=2m`替换后`t/(2m)`、`t≥(ε−ε′)/q`及`(e+1)A−B`的推导；Markdown对应公式一致，假设和结论文字未缺失。
- 记录时间：2026-10-01 20:43 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.044（PDF p.44 / 印刷 p.44）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p044_300dpi.png`（Ghostscript `pnggray`，300dpi；核对定理证明关键式与参考文献[7]）。
- 核对：Theorems 1.7/1.6/1.1证明收束、`−K_{X′}`的MMP对象、boundedness三常数`m,v,t_l`及Corollary 1.4证明；检查References [1]–[7]。
- 结果：**FAIL**——Theorem 1.1证明中原文运行`−K_{X′}`的MMP，Markdown把下标/撇号严重识别成额外粗体字母与`Π`；紧随其后的`K_X+Δ ∼_R 0`漏掉右端`0`；volume bound`vol(−K_X)≤v`被损坏成`vo. (−K_X)≤v`。这几处均改变了核心式/操作对象，待修复。
- 次要差异：Theorem 1.6参数依赖处多出一个`e`；按text layer及原页检查，References [7]的作者名以M后的上标c排印，Markdown压平为“McKernan”，不改变作者姓名，记录为排版/文本层差异；其余[1]–[7]题录信息与原页一致。
- 原文证据：p.44整页300dpi图及PDF文本层显示`−K_{X′}`、`K_X+Δ∼_R0`及`vol(−K_X)≤v`；图中[7]处的`c`确为上标式排印。正文其余补式/有界族推理顺序一致。
- 记录时间：2026-10-01 21:16 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.045（PDF p.45 / 印刷 p.45）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p045_300dpi.png`（Ghostscript `pnggray`，300dpi；核对参考文献8–37及人名上标格式）。
- 核对：References [8]–[37]逐条对照作者、题名、出版物、年份、卷期、页码与arXiv编号。
- 结果：**PASS±**——所列文献条目和题录数据与PDF文本层/原页一致；法文重音在Markdown中以组合字符形式呈现，`affine`等出现少`f`的拼写，均属不改变题录身份的编码/连字瑕疵。原页[13]、[14]、[31]中McKernan的`c`作上标，Markdown保留了上标；[26]印刷刊名缩写为“J. Di. Geom.”，按源级文字忠实保留，不改写。
- 原文证据：PDF p.45文本层完整列出[8]–[37]；300dpi整页图核对到作者名、特殊字符及卷期页码；与Markdown逐条一致。
- 记录时间：2026-10-01 21:59 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## p.046（PDF p.46 / 印刷 p.46）
- PNG：`audit/300dpi/Birkar_2016_singularities_linear_systems_p046_300dpi.png`（Ghostscript `pnggray`，300dpi；核对最后一组参考文献、作者单位和联系行）。
- 核对：References [38]–[45]逐项对照；末页DPMMS单位、地址、作者邮箱。
- 结果：**FAIL**——PDF末页在“DPMMS, Centre for Mathematical Sciences”之后还印有“University of Cambridge, Wilberforce Road, Cambridge CB3 0WB, UK”及`c.birkar@dpmms.cam.ac.uk`；MinerU Markdown只保留第一行，丢失了完整单位地址与作者邮箱。另，原页次序为References [44]后接[45]，Markdown将两条调换位置，须恢复页内顺序。
- 次要差异：Reference [42]中的`Differential`少一个`f`，`Kähler`的重音编码位置不正确，记为PASS±类拼写/编码瑕疵。References [38]–[45]的作者、标题与出版信息除次序外与原页一致。
- 原文证据：p.46整页300dpi图清楚显示[44]→[45]顺序，以及单位地址和邮箱；对应Markdown末尾仅有DPMMS首行和[45]→[44]。
- 记录时间：2026-10-01 22:30 EDT；actor=`Peer-P13`；model=`gpt-6-luna`；effort=`max`。

## 全篇回读补充发现

- p.002：Theorem 1.1两条假设原页均有项目符号，初审FAIL只记映射箭头；回读时补记并恢复。
- p.003：Corollary 1.4两条假设缺项目符号，且KX+Δ∼R0的0前有多余波浪号；均已修复。
- p.005：Theorem 1.6两条假设的项目符号原页有、Markdown缺失；已恢复。
- p.008：Step 5的(V,Δ)与(V,Δ+u⁻¹M)并列条件前两项缺bullet；已恢复。
- p.010：Lemma 2.3的If和凸组合结论行也有OCR损坏；已按PDF p.10修复。
- p.016：Lemma 2.24证明中KY∼QKU|Y及ΓU不含Y两项条件缺bullet；已恢复。
- p.007：m(KV+ΔV)∼0误插ι，已删除；p.017的replace L伪带分号下标已清除。
- p.018：Step 5交叉引用恢复为by Step 3。
- p.027：假设x∈⋂₁ᵈSi原先缺下限1，已补回；证明内其他求和/交集保持原刊只写数字下限的简写。
- p.031：补修degHi(−KPd−Θ)=1、KPd+Δ∼R0、W′⇢W″及W→Pd。
- p.037：t<r后多出的2已删除。
- p.042：Proof of Theorem 1.8引用Proposition 5.11的nΛ、mA−Λ、(X,Λ) near x三项缺bullet；已恢复。

## 逐页修复登记

以下按PDF页列出印刷原文与Markdown修复的对应关系。各项在最终全文回读时核对；具体原文证据定位见前文对应页的文本层/整页图/裁片记录。

### p.001–p.016

- p.001：关键词minimal mode program改为minimal model program。
- p.002：两处Y→Z恢复；Theorem 1.1的(X,B)、−(KX+B)两条假设补bullet。
- p.003：恢复V₂→V₁、Vₙ→Vₙ₋₁、X′ₙ→Xₙ、n→∞；n≥2的≥复原，[8]后多余2及Δ伪下标去除；Corollary 1.4两条假设补bullet并恢复KX+Δ∼R0。
- p.004：PASS±保留；McKernan上标c核对为忠实。
- p.005：Aᵈ≤rᵢ改Aᵈ≤r；Theorem 1.8列表与Theorem 1.6假设补bullet。
- p.006：f:X→Z恢复、尾随2删除；Theorem 1.8末项、Theorem 1.9列表和Theorem 1.1 proof sketch前三项补bullet。
- p.007：V⇢X两处、φ:Y→X两处恢复；ℒY改普通LY且φ*项同步改L；删除|−KX|R前的Ω及m(KV+ΔV)中插入的ι。
- p.008：X⇢V、V⇢X、Y→X、X→Pd恢复；重复负号、ε″-lc尾随2及“degrees”碎片修复；对应并列条件补bullet。
- p.009：W→X、Y→X及φ:X⇢Y恢复。
- p.010：log resolution W→X、X→Z、φ:X⇢Y/Z、Y→T/Z恢复；重写sub-lc/sub-klt/sub-ε-lc条件；Lemma 2.3的If/if和凸组合结论修复。
- p.011：Lemma 2.7四条结果补bullet；Y模型箭头、Q下标及<1复原。
- p.012：Vᶦ→Tᶦ、Cᶦ→Tᶦ、φ:Vtᶦ⇢X恢复；B伪下标去除；n-complement三条bullet补齐，<1复原。
- p.013：Theorem 2.13、2.15假设列表bullet补齐；Xi+1→Xi及Xp→Xp−1相关箭头恢复。
- p.014：φi:Xi→X0及中心爆破序列箭头恢复。
- p.015：π:X→Z、toric X→Z、Y→X、φ:Y→X恢复；Lemma 2.20第四项、Lemma 2.24首项补bullet。
- p.016：Vᶦ→Tᶦ、W→V、U→T、V→T、Y→X、φ:Y→X、U→V恢复；Lemma 2.24结果列表与证明条件补bullet；Lemma 2.26的Y→X恢复。

### p.017–p.032

- p.017：Proposition 3.1第三项补bullet；两处V⇢X恢复；带点c改普通c；replace L伪下标去除。
- p.018：lH−N改lH−Λ，degH M记号恢复，by Step 3及Step 3中的V⇢X恢复。
- p.019：两处φ:Y→X、Y′→Z′及一般纤维箭头恢复；花体ℒY改普通LY。
- p.020：Xi′→X恢复，目标X的伪横线删除；Hi′=φi*Hi统一为普通斜体H；Xi″→Zi″恢复。
- p.021：一般纤维限制中的Xi″→Zi″恢复。
- p.022：S=|Γ|改S=⌊Γ⌋；第二条假设补bullet。
- p.023：Sᵢ改S；round-down竖线改floor括号。
- p.024：PASS±保留。
- p.025：nR′定义与限制公式的三处竖线改floor括号；S圆圈下标改S；𝓛与普通L恢复区分。
- p.026：X→U两处及Y→X两处恢复。
- p.027：Lemma 2.7三项bullet及Proposition 5.2列表bullet补齐；Δ≤B尾随2删除；degHi C记号恢复；x∈⋂₁ᵈSi补下限1。
- p.028：Lemma 5.4的Aᵈ≤rᵢ改为Aᵈ≤r，三条假设bullet与degHi C记号修复。
- p.029：Proposition 5.5中rᵢ改r、degAΔ改degAΛ、stratum后尾随2删除；缺失假设bullet及degree符号修复。
- p.030：degree碎片改为degH′(C|G)=degH C≤r。
- p.031：−KW改−KW′；degHiΩ=d+1、degHi(−KPd−Θ)=1及边界KPd+Δ∼R0复原；Prop. 5.7假设bullet、W′⇢W″、W→Pd恢复。
- p.032：nιΛH改nΛH、T on Ui改T on U；φ:W→X、T→C、G→H及Lemma 5.8列表bullet恢复。

### p.033–p.046

- p.033：X′→X恢复，dot X′改X′；两处ε/2-lc及AH=A|H恢复；Step 2三条bullet补齐。
- p.034：μTΓV=1−a删除尾随2；ε下标2改ε/2；π:Y→X恢复。
- p.035–p.036：PASS±保留。
- p.037：Proposition 5.11假设/结论bullet补齐；t<r后多余2删除；tt按PASS±保留。
- p.038：W→X两处恢复；H_;改H、Tᵢ改T。
- p.039：Y′→X、Y″→X、φ:Y→X及Y⇢Y′恢复。
- p.040：Y′→X补箭头；pushdown来源P_Y改P_Y′；Aᵈ≤r后尾随2删除。
- p.041：PASS±保留。
- p.042：φ:Y→X恢复，带点C改普通C；Lemma 2.24及Proof of Theorem 1.8引用Proposition 5.11的bullet补齐。
- p.043：PASS±保留，列表bullet格式与点状排版仍按初审范围不改。
- p.044：−KX′的MMP对象恢复；KX+Δ∼R0补0；vol(−KX)≤v修复；终读确认参数依赖无多余e。
- p.045：PASS±保留。
- p.046：[44]调整到[45]之前；补DPMMS之后的University of Cambridge地址和c.birkar@dpmms.cam.ac.uk。

## 最终核验与Git收据

- 修复前Markdown SHA-256：5beebf35a9c7e99f36509db38462da3ca95638ef66886378872acc6d89514a9f。修复后：34c398ff3b9347d3d0ef166b1f744eef6d1936f9842a212b284529a03be38249；文件共2343行。
- 初审评级39 FAIL、7 PASS±；登记中的FAIL差异已修复。PASS±保留页：p.004、p.024、p.035、p.036、p.041、p.043、p.045。
- fix(md)独立提交：353ad7fac129481dae280111b8f06a216b08dc01。audit(record)提交：恢复p.014顺序7c8c2994；校正p.007符号裁片及p.027–p.029源符号记录ea0d1994。
- audit(page)提交OID按页：p.001 7b7abdbe；p.002 154c4472；p.003 13f0e0eb；p.004 bf6ad672；p.005 bc9e840e；p.006 32916753；p.007 31cf909c；p.008 fe8ff232；p.009 133f5bfc；p.010 d99b385b；p.011 8c2195ea；p.012 108aa809；p.013 5d32ea4b；p.014 e5867b30；p.015 ccf08f60；p.016 40f93c2b；p.017 4b7c48bf；p.018 efaed60e；p.019 f2ca4027；p.020 be24b9d1；p.021 42310f89；p.022 3e808e40；p.023 458e10e2；p.024 0812e5d6；p.025 8c084be3；p.026 13b71623；p.027 47621bbf；p.028 68c93afb；p.029 ff133632；p.030 86ae8228；p.031 54901993；p.032 96e4498f；p.033 780d145d；p.034 18b39d6c；p.035 dabb6161；p.036 22bd9755；p.037 53071beb；p.038 e7ade0e2；p.039 598ebf4b；p.040 61237ae4；p.041 21963e63；p.042 22f02799；p.043 d9d31c7f；p.044 82a929c9；p.045 6ebf7015；p.046 b620efb4。
- 最终复核：Markdown第1–2343行全文回读并与PDF p.1–p.46逐页核对；证据包括born-digital文本层、p.1整页PNG及审计登记的300dpi整页图/裁片。git diff --check通过；未运行测试。
- main只读快照（2026-10-02 06:09:38 UTC）：42ad5ffc8481b31e1ea640c8182a4ef1c19efbec；从基线到该main的本篇owned paths无差异，AUDIT-INDEX仍登记审计中。候选未集成；AUDIT-INDEX和AUDIT-PROGRESS由Master维护。
- 证据边界：此工作确认印刷PDF与MinerU Markdown之间的文本、公式记号、映射和所列排版忠实性，不验证论文定理或证明。
- SOP偏差：p.014条目顺序以7c8c2994恢复；p.039页提交在p.046后补录，但46页均在Markdown修复前完成审计；p.007裁片/notation记录校正以ea0d1994提交。只改本篇Markdown/AUDIT及本篇证据图；未改PDF、其他论文、主线索引/日志或远端。
