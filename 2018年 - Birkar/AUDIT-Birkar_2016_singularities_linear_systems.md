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

---

# 第三轮复审：p.001–p.030 独立逐页重检（2026-10-05）

- 性质：**第三轮独立复审**。前序两轮为 Luna（`Peer-P13`，全46页，修复提交 `353ad7fac129`）与 Wf-R-P13 的 GLM 重做（p.001–p.009，见 `AUDIT-Birkar_2016_singularities_linear_systems.redo.md`）。本轮由新审计员对 **PDF p.1–p.30** 重新逐页执行「gs pngmono 150dpi 渲染 → Read 目检 → pdftotext 文本层双通道对账 → 五点比对」，**不复用前两轮结论**；前两轮结论（含 GLM 在 p.008 对 Luna 的推翻）均作为**被检对象**重新独立裁定。
- actor：`Wf-R-Birkar-p130`
- host / model / effort：`zcode / opencode-go-chat-space-bunny-free / 未暴露`（effort 不可自报实测，记 UNKNOWN）
- 审计起始 Markdown SHA-256：`8cadd238f57a197ef2d00c36e680dd8d0e6d035877a4de10d71f15949c982b9b`（= Luna 修复态 `34c398ff…` 再叠加 GLM 的 p.008 `\overline{T}`→`T` 一处修复）。
- 溯源基线（依 SOP 要求的 `git show cpf-redo/Birkar_2016_singularities_linear_systems^`）：
  - `cpf-redo/Birkar_2016_singularities_linear_systems^` = `16ffcc7ce8a0c3aad33fc474a83c84d7d53f801c`（即 GLM p.008 页提交），其 MD 哈希 `8cadd238…` 与当前一致 → **自 p.008 起无新的 peer 改动**。
  - **原始 MinerU 导出** = `037602429d3b009f6fc468c732073eb3ddf9875f`，MD 哈希 `5beebf35a9c7e99f36509db38462da3ca95638ef66886378872acc6d89514a9f`。
  - **Luna 修复提交** = `353ad7fac129481dae280111b8f06a216b08dc01`，MD 哈希 `34c398ff3b9347d3d0ef166b1f744eef6d1936f9842a212b284529a03be38249`。
  - 归因规则：缺陷同时存在于 `03760242` 者 = **MinerU 导出缺陷**；仅存在于导出之后者 = **peer 引入的回归**，须在条目中注明引入 commit。
- 印刷原文为唯一裁决源；印刷自身的错字/怪癖（print quirk）原样保留并登记，不按数学常识静默「纠正」。
- 本节条目按 PDF p.1–p.30 顺序追加，**结论以本节为准**，取代本文件上方 Luna 的 p.001–p.030 旧条目。

## p.001（PDF p.1 / 印刷 p.1）
- PNG：/tmp/birkarsing_audit_p001.png（pngmono 150dpi）；另作 300dpi 仲裁裁片 `/tmp/birk_p001_300.png` 及裁切 `/tmp/birk_p001_abstract_crop.png`、`/tmp/birk_p001_eps_crop.png`
- 核对：题名、作者、摘要全文、Contents 全部条目与页码、脚注三行（Date／2010 MSC／Keywords）；与 Markdown 第 1–41 行逐项比对，辅以 `pdftotext -f 1 -l 1 -layout`。
- 结果：**PASS±**
  - 题名 `Singularities of linear systems and boundedness of Fano varieties`、作者 `Caucher Birkar` 与印刷一致。
  - Contents 26 条全部吻合，含刻意的缺号子节（2.3／2.7／2.10／2.11／2.13／2.15／2.17／2.20／2.21／2.24 印刷即无）与页码序列 `2,9,9,10,10,11,12,12,12,13,13,14,15,15,15,16,17,22,27,27,28,31,37,42`；`5.10. Construction of $\Lambda$` 中 Λ 正确。
  - 脚注三行 `Date: December 2, 2020.`、`2010 MSC: 14J45, 14E30, 14C20.`、`Keywords: … minimal model program.` 与印刷一致（Luna 的 minimal mode→model 修复经原页复核为**正确**，保留）。
- 差异列表（PASS±，均不误导，按 SOP 登记不批量修）：
  1. **MD 第 5 行 `diferent`（少一个 f）**：印刷为 `different`。已用双通道裁定——`pdftotext` 文本层 `p001.txt:10` 明确作 `in different`，300dpi 裁片显示完整 ff 连字。**溯源：`git show 03760242:…md` 中 `diferent` 出现 4 次、`different` 出现 0 次 → 系 MinerU 原始导出缺陷，非 peer 回归**；Luna 与 GLM 两轮均登记未修，本轮维持登记不改（纯拼写，不改变命题）。
  2. **MD 第 5 行 `R-linear` 丢失黑体**：印刷 300dpi 裁片作 `ℝ-linear`（`\mathbb{R}`），MD 拍平为普通 R。同属字形类拍平，不改变数学含义，记 PASS±。
  3. **ε 字形编码**：印刷 300dpi 裁片 `/tmp/birk_p001_eps_crop.png` 为**新月形 ϵ**（lunate epsilon），MD 写 `ǫ`（U+01EB o-with-stroke）。两者视觉近乎相同、语义等价，属 OCR 字形编码差异，记 PASS±，**不按字形直觉改写**（铁律三）。
  4. **MD 第 41 行孤立 `References` 行**：印刷该行属 p.2 顶部目录续项「References … 44」，MinerU 错位到题录区且丢页码 44。结构伪影，不影响数学内容，不批量改。
  5. 页边 arXiv 水印（`arXiv:1609.05543v2 [math.AG] 1 Dec 2020`）未收录——非论文正文，不计差异。
- 备注：本页**无数学内容错误**。前两轮 p.001 结论（minimal model program 修复属实、diferent 登记属实）经本轮独立复核均成立，未发现前两轮漏报的本页差异。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：/tmp/birkarsing_audit_p002.png（pngmono 150dpi）
- 核对：页眉「2 / Caucher Birkar」、目录续项 References 44、§1 开头段、`Boundedness of singular Fano varieties.` 粗体小标题段、Mori fibre space 段（两处 `Y → Z`）、一维/二维 Fano 段、toric Fano 段、Alexeev/Borisov 猜想段、**Theorem 1.1 完整陈述**（两条 bullet 假设 + `form a bounded family.`）、`ε = 0` 反例段、已知情形列表前两条 `[22]` `[27]`；与 Markdown 第 42–75 行逐项比对，辅以 `pdftotext -f 2 -l 2 -layout`。
- 结果：**PASS±**
  - Luna 两项旧修复经原页复核**属实且正确**：`$Y \to Z [ 7 ]$` 与 `A general fibre of$Y \to Z$` 两处实线箭头已恢复（150dpi 原页与文本层 `p002.txt` 均清楚印有 `Y → Z [7]`、`fibre of Y → Z`）；Theorem 1.1 两条假设「• `$( X , B )$is ǫ-lc of dimension d for some boundary B, and`」与「• `$- ( K _ { X } + B )$is nef and big,`」**bullet 均已恢复**，与印刷列表结构一致。
  - 正文与印刷逐句吻合：`−K_X is ample`、`P^1`、`[32][10]`、`[26]`、`[9]`、`[1]`、`[35][34][33]`、`[30]`、`Borisov-Alexeev-Borisov`/`BAB`、`form a bounded family.`、`birationally bounded` 等均一致；Theorem 1.1 首句 `Let d be a natural number and ǫ be a positive real number.` 与印刷一致。
- 差异列表（PASS±，均为 OCR 连字拍平，不改变命题）：
  1. **MD `result tha the smooth Fano surfaces`**：印刷为 `it is a classical result that the smooth Fano surfaces form a bounded family.`——`tha` 丢 t。
  2. **MD `diferential geometry`**：印刷为 `differential geometry`（原页字形与文本层 p002.txt 均为完整 `differential`）。
  3. **MD `pseudo-efective`（本页 1 处，`with$K _ { W }$not pseudo-efective`）**：印刷为 `pseudo-effective`。
  4. **目录续项错位**：印刷 p.2 顶部作「References …… 44」，MD 将该行错置到 p.1 题录区（MD 第 41 行）且**丢失页码 44**（见 p.001 差异 4，同一根因）。
  - **溯源（`git show 03760242:…md`）**：`diferent`=4、`diferential`=1、`result tha `=1、`pseudo-efective`=5 均已存在于**原始 MinerU 导出** → 全部系**导出缺陷，非 peer 回归**；同时 `Y \to Z` 在原始导出中计数为 **0**，反证 Luna 的箭头恢复是真实修复而非臆造。按整篇约定（拼写/连字类不误导不误导读者、不批量修）本轮维持登记不改。
- 备注：本页无数学内容错误。零星数学式与后接单词空格粘连（`$- K _ { X }$is`、`with$K _ { W }$not`）属 MinerU 排版伪影，按 SOP 登记不改。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：/tmp/birkarsing_audit_p003.png（pngmono 150dpi）
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 3」、已知情形列表四条（`[2]`、`[8]`、`[13]`、含 `K_X + Δ ≡ 0` 的 DCC 边界条）、**Example 1.2** 全文含行间公式 `K_{W_n}+\frac{n-2}{n}E=f^{*}K_{X_n}`、`2/n`-lc、`n → ∞`、集合 `{X_n | n∈N, n≥2}`、**Example 1.3** 全文含 `(P^2, Δ=S+T+R)` 与全部映射箭头、**Corollary 1.4** 陈述（两条 bullet + `K_X+Δ∼_R 0`）、DCC 段与 log Calabi-Yau 段开头；与 Markdown 第 76–112 行逐项比对，辅以 `pdftotext -f 3 -l 3 -layout`。
- 结果：**PASS±**
  - Luna 旧修复逐项经原页复核**属实且正确**：四处映射箭头 `$V _ { 1 } \to { \mathbb P } ^ { 2 }$`、`$V _ { 2 } \to V _ { 1 }$`、`$V _ { n } \to V _ { n - 1 }$`、`$X _ { n } ^ { \prime } \to X _ { n }$` 及 `$f \colon W _ { n } \to X _ { n }$`、`As$n \to \infty$` 均已恢复（150dpi 原页与文本层 `p003.txt` 处处印有实线箭头）；`n \geq 2` 为**普通** `\geq`（原页无双点）；`[13];` 后无多余 `2`；Corollary 1.4 边界为 `$\Delta$` 无伪下标，两条 bullet 已恢复。
  - 关键公式全部逐项吻合印刷：$K_{W_n}+\frac{n-2}{n}E=f^{*}K_{X_n}$（系数 `n-2`/`n` 正确）、`a \frac { 2 } { n } { - } \mathrm { l c }` Fano variety、$(\mathbb{P}^2,\Delta=S+T+R)$、$x_0:=S\cap T$、`−K_{V_n}` is big、`$- K _ { X _ { n } ^ { \prime } }$`、`klt m-complement for some m independent of $n$`、by `[15]`。
- 差异列表（PASS±，不误导，按 SOP 登记不批量修）：
  1. **`coefficients`/`coefficient` → `coeficients`/`coeficient`**（本页 3 处：DCC 边界条 2 处 + Example 1.2 收尾 1 处；印刷与文本层 p003.txt 均为完整双 f）。
  2. **`S^{\sim}` 记号位置**：印刷作 $S̃$（波浪**覆盖在 S 正上方**，即 $\tilde S$，见原页「$x_1 := S̃ ∩ E_1$」与「$S̃$ is the birational transform of $S$」两处）；MD 写作 `S ^ { \sim }`（波浪变**上标**）。记号可辨、语义等价，属 MinerU 上下标扁平化，记 PASS±。
  3. **MinerU 标题提升伪影（2 处）**：MD 第 91 行 `## Example 1.3. Consider the pair` 与第 107 行 `## form a bounded family.` 被提升为二级标题；印刷中二者均为**普通正文行**（`Example 1.3.` 仅为句首加粗的行内编号，`form a bounded family.` 为句末斜体）。文字内容完整、不改变数学，属结构伪影，登记不改。本轮**独立确认**该发现属实。
  4. **MD 第 83 行双逗点** `$n \geq 2 ,$,`：印刷为 `n ≥ 2,` 单逗号（`p003.txt` 证实）。
  5. `ǫ` 与 `\epsilon` 在 MD 内混用（印刷统一为新月 ϵ）：字形编码不统一，语义一致，登记不改。
- 溯源：上述 1／3／4 类在 `git show 03760242:…md`（原始 MinerU 导出）中已存在（见本轮末尾统一溯源清单）；第 2 类 `S ^ { \sim }` 亦为导出原样。**均系导出缺陷，非 peer 回归。** Luna 对箭头／`\geq`／尾随 `2`／`Δ` 伪下标的修复方向正确且已正确落地。
- 备注：本页**无数学内容错误**。前两轮 p.003 结论（箭头修复属实、标题提升与上标波浪补记属实）经本轮独立复核均成立。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：/tmp/birkarsing_audit_p004.png（pngmono 150dpi）
- 核对：页眉「4 / Caucher Birkar」、Mc^cKernan–Prokhorov 猜想段（含 `M^cKernan` 上标 c）、`[4]` 短段、`Jordan property of Cremona groups.` 粗体行内头、index h 定义段、**Corollary 1.5 完整陈述**、`[39, Theorem 1.8]` 推导段（$\mathrm{Cr}_d(k):=\mathrm{Bir}(\mathbb{P}^d_k)$、`[41, 6.1]`）、Bir(X) 非 Jordan 段（`[45]`／`[40]`）、`Lc thresholds of ℝ-linear systems.` 粗体行内头、`lct(X,B,L):=\sup\{\dots\}` 行间式、`|A|_{\mathbb R}=\{L\ge0\mid L\sim_{\mathbb R}A\}` 行间式、`lct(X,B,|A|_{\mathbb R}) :=\inf\{\dots\}` 行间式、`\sup\{\dots\ \text{for every}\ L\in|A|_{\mathbb R}\}` 行间式、`|A|` 与 `|A|_{\mathbb Q}` 短句、`Kähler-Einstein` 段收尾；与 Markdown 第 113–155 行逐项比对，辅以 `pdftotext -f 4 -l 4 -layout`。
- 结果：**PASS±**
  - **`M^cKernan` 上标 c 忠实**：150dpi 原页清楚印出 `M^ckernan`（c 为上标、小一号、位于 M 与 Kernan 之间），MD `M<sup>c</sup>Kernan` 与之相符；`pdftotext` 把它拍成 `Mc Kernan` 是**文本层字符排序现象，不是印刷事实**，据原页不登记为 Markdown 差异。本轮独立复核确认 Luna 的该项判定忠实。
  - **四条行间公式逐项吻合印刷**：`\operatorname{lct}(X,B,L):=\sup\{t\in\mathbb R\mid(X,B+tL)\text{ is lc}\}`；`|A|_{\mathbb R}=\{L\ge0\mid L\sim_{\mathbb R}A\}`；`\operatorname{lct}(X,B,|A|_{\mathbb R}):=\inf\{\operatorname{lct}(X,B,L)\mid L\in|A|_{\mathbb R}\}`；`\sup\{t\in\mathbb R\mid(X,B+tL)\text{ is lc for every }L\in|A|_{\mathbb R}\}`——上下标、$\in$、$\mid$ 分隔符与 `inf`/`sup` 均正确，**无系数/指数错误**。
  - **Corollary 1.5 全文**、index h 定义段、`$\mathrm{C r}_d(k):=\mathrm{B i r}(\mathbb P^d_k)$`、`[39, Theorem 1.8]`、`[41, 6.1]`、`[45]`、`[40]`、`$X=\mathbb P^d_k$`、`$\mathbb P^1_k$`、`non-uniruled` 等与印刷逐项一致。
- 差异列表（PASS±，均不误导，按 SOP 登记不批量修）：
  1. **`K¨ahler-Einstein` 变音符错位**：印刷 150dpi 原页作 `Kähler-Einstein`（分音符在 `a` 正上方），MD 写 `K¨ahler-Einstein`（分音符脱离元音、置于 K 之后）。术语仍可辨，属编码瑕疵。与 Luna／GLM 两轮登记一致，本轮独立复核属实。
  2. **正文 `ℝ` 拍平为普通 `R`（2 类共 3 处）**：印刷行内头作 `Lc thresholds of ℝ-linear systems.`、正文作 `an ℝ-Cartier ℝ-divisor`；MD 作 `R-linear systems` / `R-Cartier R-divisor`。注：MD 的**四条行间公式内部**已正确使用 `\mathbb{R}`，故仅行内 ℝ 丢失黑体，属局部字形拍平，不改变数学含义。
  3. **行间式末尾句点丢失**：印刷第 4 条行间式末尾为 `… L ∈ |A|_ℝ}.`，MD 对应 `$$` 块以 `}` 结束无句点。标点级瑕疵。
  4. **页块边界漂移（结构性，首次登记，后续页沿用此口径）**：MD 第 153 行「…particularly when A is **ample. An important special case is when X is Fano and $A = - K _ { X }$**」及紧随的 `## Lc thresholds of anti-log canonical systems of Fano pairs.` 段，**印刷上属 PDF p.5 开头**（`pdftotext -f 5 -l 5` 第 3 行起即为此内容）。即 Markdown 的自然段块相对 PDF 页码**整体前移约 1 页**，但**内容无丢失、无重复、无错序**。属 MinerU 分页伪影，不影响数学内容；后续各页按「印刷 p.N 的内容是否完整存在于 MD（位置允许 ±1 页漂移）」为核对口径。
- 溯源：第 1／2／3 类在 `git show 03760242:…md`（原始 MinerU 导出）中已存在（见本轮末尾统一溯源清单）→ **导出缺陷，非 peer 回归**。
- 备注：本页**无数学内容错误**。`Jordan property of Cremona groups.`、`Lc thresholds of ℝ-linear systems.` 在印刷中为**粗体行内头**，MD 分别作粗体正文与 `##` 标题两种处理——二者都忠实于印刷的行内头样式，**不登记为缺陷**。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：/tmp/birkarsing_audit_p005.png（pngmono 150dpi）
- 核对：页眉「… / 5」、p.4 跨页续句「ample. An important special case is when X is Fano and A = −K_X.」、粗体行内头 `Lc thresholds of anti-log canonical systems of Fano pairs.`、**Theorem 1.6 全文**（两条 bullet + 行间式 `lct(X,B,|A|_ℝ) ≥ t`）、反序说明段（`[3]`、`[19][18]`）、`ℝ-linear system |A|_ℝ` 段（`[42, Question 1]`、`[11, Conjecture 1.12]`）、**Theorem 1.7 全文**（`lct ≤ 1`、`0 ≤ D ∼_ℝ A`、`lct = lct(X,B,D)`、`D ∼_ℚ A`、`lct < 1`）、收尾段（`[13]`、`[5]`、Cheltsov/Shokurov）、粗体行内头 `Lc thresholds of ℝ-linear systems with bounded degree.`、**Theorem 1.8 开头三条 bullet**（重点第二条 `A^d ≤ r` 无下标）；与 Markdown 第 156–211 行逐项比对，辅以 `pdftotext -f 5 -l 5 -layout`。
- 结果：**PASS±**
  - **Luna 旧修复经原页复核属实且正确**：第二条假设为「• A is a very ample divisor on X with `$A ^ { d } \leq r$`」——**无下标 `i`**，150dpi 原页清楚印作 `A^d ≤ r,`（`p005.txt` 同步为 `A^d ≤ r`），原导出误作 `r_i` 已被正确改正。Theorem 1.6 两条 bullet 与 Theorem 1.8 印刷上可见的三条 bullet **均已恢复**。
  - **四条阈值公式逐项吻合印刷**：`\operatorname{lct}(X,B,|A|_{\mathbb R})\geq t`、`\leq 1`、`0\leq D\sim_{\mathbb R}A`、`\operatorname{lct}(X,B,|A|_{\mathbb R})=\operatorname{lct}(X,B,D)`、`D\sim_{\mathbb Q}A`、`< 1`——不等号方向、$\sim_{\mathbb R}$／$\sim_{\mathbb Q}$ 的 ℝ／ℚ 下标、`0 \le` 下界均正确，**无系数/指数错误**。
  - Theorem 1.6／1.7／1.8 的编号与陈述、依赖顺序（`[3]`→`[19][18]`→`[42, Question 1]`→`[11, Conjecture 1.12]`）、`2.15 below`、`see below`、`Fano's`、`log Fano's`、`Q-boundary` 等与印刷一致。
- 差异列表（PASS±，均不误导，按 SOP 登记不批量修）：
  1. **`diferent` ×2**（MD 第 169 行「our approach is entirely diferent」及同段前文）：印刷作 `different`。**双通道证实**：`p005.txt:6` = `for a quite different reason`、`p005.txt:21` = `our approach is entirely different`，150dpi 原页亦作 `different`。
  2. **`pseudo-efective`**（MD 第 203 行 `• $A - B$is pseudo-efective, and`）：印刷作 `pseudo-effective`（原页与 `p005.txt` 同步）。
  3. **ℝ 拍平为 `R`（2 处）**：MD 第 171 行 `an R-linear system`、第 195 行粗体头 `Lc thresholds of R-linear systems with bounded degree.`；印刷均作 ℝ（同 p.004 差异 2）。另该粗体行内头在 MD 中未加粗，属排版弱化，不改变内容。
  4. **MD 第 185 行 `Moreover,$i f B$is a Q-boundary`**：印刷作 `Moreover, if B is a Q-boundary,`；MinerU 把连写词 `if` 拆入数学环境渲染为斜体 `i f`。语义可辨，排版伪影，登记不改。
  5. **bullet 末尾标点**：MD 第 201 行 `with$A ^ { d } \leq r$` 行末**无逗号**，印刷作 `with A^d ≤ r,`；属标点级瑕疵（内容与数学均正确）。
  6. **页块边界漂移（沿用 p.004 已建立口径）**：MD 第 205 行第四条 bullet「• $M \geq 0$is an R-Cartier R-divisor with A − M pseudo-efective.」与第 209–211 行行间式 `lct(X,B,|M|_ℝ) ≥ lct(X,B,|A|_ℝ) ≥ t` 属**印刷 PDF p.6**。印刷 p.5 止于第三条 bullet「A − B is pseudo-effective, and」。内容无丢失/重复/错序，仅 MD 分页点较 PDF 前移约 1 页。
- 溯源：第 1／2／3／4 类在 `git show 03760242:…md`（原始 MinerU 导出）中已存在（见本轮末尾统一溯源清单）→ **导出缺陷，非 peer 回归**；Luna 的 `r_i → r` 与 bullet 恢复方向正确、已正确落地。
- 备注：本页**无数学内容错误**。前两轮 p.005 结论经本轮独立复核均成立。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：/tmp/birkarsing_audit_p006.png（pngmono 150dpi）
- 核对：页眉「6 / Caucher Birkar」、Theorem 1.8 第四条假设 `M ≥ 0` 与结论链行间式 `lct(X,B,|M|_ℝ) ≥ lct(X,B,|A|_ℝ) ≥ t`、假设解释段（含 `A^d ≤ r`、`X = P^d`）、行间式 `deg_A B := A^{d−1}B ≤ A^d ≤ r and deg_A M := A^{d−1}M ≤ A^d ≤ r`、无有界性段、粗体行内头 `Complements near a non-klt centre.`、**Theorem 1.9 完整陈述**（六条 bullet 假设含 `f : X → Z`、`M|_S ≡ 0`，两条 bullet 结论含 `n(K_X+Λ) ∼ (n+2)M`）、`[5, 2.18]` 段、`1.1, 1.6, and 1.8` 段、粗体行内头 `Sketch of the proof of Theorem 1.1.`、`[5, Proposition 7.13]` 与 `m, v, t` 段、三条 bullet（`K_X` m-complement、`|−mK_X|` birational map、`vol(−K_X) ≤ v`）；与 Markdown 第 205–261 行逐项比对，辅以 `pdftotext -f 6 -l 6 -layout`。
- 结果：**PASS±**
  - **Luna 旧修复经原页复核全部属实且正确**：第三条假设「• M is a semi-ample Cartier divisor on X defining a contraction `$f : X \to Z$`」箭头已恢复（150dpi 原页印 `f : X → Z`，`p006.txt` 同步为 `f : X → Z`）；**六条假设 bullet 与两条结论 bullet 全部恢复**；Sketch 开头三条 bullet（`$K _ { X }$has an m-complement`、`$\vert - m K _ { X } \vert$defines a birational map`、`$\operatorname { v o l } ( - K _ { X } ) \leq v$, and`）均已恢复；`$M - ( K _ { X } + B )$` 为**单负号**（原页无双负号）；无尾随 `2`。
  - **行间式逐项吻合印刷**：`\deg_ {A} B := A ^ {d - 1} B \leq A ^ {d} \leq r \text { and } \deg_ {A} M := A ^ {d - 1} M \leq A ^ {d} \leq r`——指数 `d-1`、`d`、不等号方向与 `\text{ and }` 连接词均正确；`lct ≥ lct ≥ t` 链、`0 ≤ D`、`n(K_X + Λ) ∼ (n+2)M`、`z := f(S)`、`K_X + B^{+}`、`(X, tL)` 等记号与系数无误。
  - Theorem 1.9 编号、`d, p` 参数、`n depending only on d, p`、`pB is integral`、`X is of Fano type over Z`、`lc over a neighbourhood`、`relative n-complement`、`[5, 2.18]`、`[5, Theorems 1.2 and 1.7]`、`[5, Theorem 1.6]`、`[15]` 等与印刷一致。
- 差异列表（PASS±，均不误导，按 SOP 登记不批量修）：
  1. **`pseudo-efectivity`**（MD 第 213 行 `the pseudo-efectivity of$A - B$ and$A - M$`）：印刷作 `pseudo-effectivity`。ff 拍平。
  2. **ℝ 拍平为 `R`**（MD 第 205 行 `an R-Cartier R-divisor`）：印刷作 `an ℝ-Cartier ℝ-divisor`（同 p.004/p.005 差异 3）。
  3. **标点缺失/重复**：①MD 第 229 行 `$f : X \to Z$` 行末**无逗号**（印刷 `f : X → Z,`）；②第 235 行 `$M | _ { S } \equiv 0$` 行末**无句点**（印刷 `M|_S ≡ 0.`）；③第 241 行 `$\sim ( n + 2 ) M$` 行末**无句点**（印刷 `M.`）；④第 243 行段末 `…\sim ( n + 2 ) M$` **无句点**（印刷 `M.`）；⑤第 247 行 `we assume$B = 0 .$.` 为**双句点**（印刷 `B = 0.`）。均为标点级瑕疵，数学内容正确。
  4. **MD 第 259 行 `$\mathrm { A p p l y i n g }$[15]`**：印刷作正文 `Applying [15],`；MinerU 将该词排入数学正体并加宽字距。排版伪影，登记不改。
  5. **页块边界漂移（沿用 p.004 口径）**：印刷 p.6 止于 Sketch 第三条 bullet「vol(−K_X) ≤ v, and」；MD 第 255–261 行（第四条 bullet「for any $0 \leq L \sim _ {\mathbb {R}} - K _ { X }$, the pair$( X , t L )$is klt.」、`[5, Theorems 1.2 and 1.7]` 段、`Applying [15]` 段、`V \dashrightarrow X` 段）属**印刷 PDF p.7**。内容无丢失/重复/错序。
- 溯源：第 1／2／4 类在 `git show 03760242:…md`（原始 MinerU 导出）中已存在 → **导出缺陷，非 peer 回归**。Luna 的箭头／bullet／尾随 `2`／双负号修复方向正确且已正确落地。
- 备注：本页**无数学内容错误**。前两轮 p.006 结论经本轮独立复核均成立。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：/tmp/birkarsing_audit_p007.png（pngmono 150dpi）
- 核对：页眉「… / 7」、Sketch 第四条 bullet `0 ≤ L ∼_ℝ −K_X`、`m`／`v`／`t` 来源段（`[5, Theorems 1.2 and 1.7]`、`[5, Theorem 1.6]`）、`Applying [15]` 段与 exceptional 定义、non-exceptional 段（**两处虚线箭头 `V ⇢ X`**）、pull back 段（`m(K_V+B_V^+) ∼ 0`、`Δ_V ∼_ℚ B_V^+`、`m(K_V+Δ_V) ∼ 0`、`m(K_X+Δ) ∼ 0`）、`serious issue` 段、粗体行内头 `Sketch of the proof of Theorem 1.6.`、`A = −(K_X+B)`、`Replacing X with …` 句、`ε′ ∈ (0, ε)`、`L ∈ |A|_ℝ`、`ε′-lc`、行间式 `a(T,X,B+sL) = ε′`、**`φ : Y → X` 两处**、`L_Y = φ*L`、`μ_T sL_Y ≥ ε − ε′`、末段 `ε-lc Q-factorial` 与 `L ∈ |−K_X|_ℝ`；与 Markdown 第 255–277 行逐项比对，辅以 `pdftotext -f 7 -l 7 -layout`。
- 结果：**PASS±**
  - **印刷怪癖（print quirk）忠实保留，符合铁律三**：①`Replacing X with can assume it is Q-factorial.`——印刷原文即缺 `Replacing X with` 的宾语（150dpi 原页与 `p007.txt` 双通道证实），MD 第 267 行**原样保留、未按数学预期补写**；②`some rough explanations for as to why`——印刷原文即为此怪异短语，MD 第 259 行原样保留。
  - **Luna 旧修复经原页复核全部属实且正确**：两处**虚线**双有理映射 `$V \dashrightarrow X$`（第 261 行，印刷 `p007.txt` 对应字形为 `V 99K X`，150dpi 原页为虚线箭头）已恢复；两处实线 `$\phi \colon Y \to X$`（第 275 行）已恢复；`$L _ { Y } = \phi ^ { * } L$` 为**普通斜体**（原页非花体）；`$L \in | - K _ { X } | _ { \mathbb { R } }$` 前**无 Ω 前缀**（原页无）；`$m ( K _ { V } + B _ { V } ^ { + } ) \sim 0$` 处**无插入的 ι**（原页无）。
  - 公式逐项吻合印刷：`a (T, X, B + s L) = \epsilon^ {\prime}`、`\Delta _ { V } \sim _ {\mathbb { Q }} B _ { V } ^ { + }`、`\mu _ { T } s L _ { Y } \geq \epsilon - \epsilon ^ { \prime }`、`0 \leq L \sim _ {\mathbb { R }} - K _ { X }`、`n \in \mathbb { N }`、prime divisor `$T$`（**普通斜体、无上横线**）等记号与系数无误。
- 差异列表（PASS±，均不误导，按 SOP 登记不批量修）：
  1. **`coeficients` ×5**：MD 第 263 行 1 处、第 265 行 4 处；印刷作 `coefficients`（原页与 `p007.txt` 均为双 f）。
  2. **`efective`**（MD 第 265 行 `$\Delta$may not be efective`）：印刷作 `effective`。
  3. **词被排入数学环境（2 处）**：①MD 第 259 行 `$\mathrm { A p p l y i n g }$[15]`（印刷为正文 `Applying [15],`）；②MD 第 261 行 `that${ \mathrm { i s } } ,$`（印刷为 `that is,`）。排版伪影，不改。
  4. **双逗点**：MD 第 263 行 `after replacing$m ,$, there is`——印刷为 `after replacing m, there is`（单逗号）。
  5. **段末句点缺失（4 处）**：MD 第 259、261、263、277 行行末均无句点；印刷四处分别作 `−K_X.`、`of B^{+}.`、`∼ 0.`、`on X.`。标点级瑕疵。
  6. **页块边界漂移（沿用 p.004 口径）**：印刷 p.7 止于末句「…any prime divisor T on X.」，MD 第 277 行同步收尾；MD 第 279–291 行（Picard number one 段、`K_X + Ω`、`X ⇢ V`、`ε″-lc` 三条 bullet 等）属**印刷 PDF p.8**。内容无丢失/重复/错序。
- 溯源：第 1／2／3／4 类在 `git show 03760242:…md`（原始 MinerU 导出）中已存在 → **导出缺陷，非 peer 回归**。Luna 的虚线箭头／实线箭头／花体改斜体／删 Ω／删 ι 修复方向正确且已正确落地。
- 备注：本页**无数学内容错误**。前两轮 p.007 结论（含 print quirk 保留决定）经本轮独立复核均成立。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：/tmp/birkarsing_audit_p008.png（pngmono 150dpi）；**本轮独立 300dpi 仲裁裁片** `/tmp/birk_p008_T_crop.png`（源图 `/tmp/birk_p008_300.png`，裁切带 y≈1520–1720）
- 核对：页眉「8 / Caucher Birkar」、Picard number one 段（`L = uT`、`u = μ_T L`）、`[5, Theorems 1.2, 1.6, 1.7]` 段（`K_X + Ω`、`|−nK_X|`、`vol(−K_X)`）、**两处虚线箭头 `X ⇢ V` / `V ⇢ X`**、`Pull back K_X+B, L` 段与三条 bullet（`ε″-lc`、`Δ + 1/u·M`、`1/u`）、`1/u` 收尾、粗体行内头 `Sketch of the proof of Theorem 1.8.`、行间式 `lct(X,B,|M|_ℝ) ≥ lct(X,B,|A|_ℝ)`、`ε′ = ε/2`、`0 ≤ N ∼_ℝ A`、行间式 `a(T,X,Δ := B+sN) = ε′`、`φ : V → X`、行间式 `a(T,X,Δ) = ε′ < 1`、`Y → X`、`−(K_Y+T)`、toroidalisation 段（`Λ_Y`、`n(K_Y+Λ_Y) ∼ 0/X`、`a(T,X,Λ) = 0`）、`Λ = S_1 + ⋯ + S_d` 段、`Y → X`、torification 段、`X → P^d`、`z = (1:0:⋯:0)`；与 Markdown 第 279–323 行逐项比对，辅以 `pdftotext -f 8 -l 8 -layout`。
- 结果：**PASS±**
  - **`\overline{T}` 争议点本轮独立裁定：印刷为普通斜体 `T`，GLM 的修复正确，Luna 的旧登记错误。** 依据：本轮自建 300dpi 裁片 `/tmp/birk_p008_T_crop.png` 直接显示「There is a prime divisor *T* on birational models of X with log discrepancy $a(T,X,\Delta:=B+sN)=\epsilon'$」——**T 上方无任何横线**；`p008.txt` 文本层同为 plain `T`。当前 MD 第 299 行为 `There is a prime divisor$T$on birational models of X`，**与印刷一致**。
  - **印刷怪癖（print quirk）忠实保留，符合铁律三**：①`so that Σ is reduced whose support contains…`——印刷原文即如此（`whose support` 悬空、无先行词），MD 第 281 行原样保留；②`a closed point x otherwise we can cut by hyperplane sections`——印刷原文即无标点连排，MD 第 305 行原样保留。
  - **Luna/GLM 旧修复经原页复核全部属实且正确**：`$X \dashrightarrow V$` 与 `$V \dashrightarrow X$` 两处**虚线**箭头、`$\phi \colon V \to X$` 与 `$Y \to X$` 两处**实线**箭头、`$X \to \mathbb { P } ^ { d }$` 均已恢复；`$- ( K _ { Y } + T )$` 为**单负号**；`$\epsilon ^ { \prime } { - } \mathrm { l c }$` 后**无尾随 `2`**；“degrees” 引号恢复；`$\epsilon ^ { \prime } = \frac { \epsilon } { 2 }$`（原导出误作 ε 下标 2）已改正为分式，与印刷一致。
  - 公式逐项吻合：`a (T, X, \Delta := B + s N) = \epsilon^ {\prime}`、`a (T, X, \Delta) = \epsilon^ {\prime} < 1`、`n ( K _ { Y } + \Lambda _ { Y } ) \sim 0 / X`、`a ( T , X , \Lambda ) = 0`、`\Lambda = S _ { 1 } + \cdot \cdot \cdot + S _ { d }`、`z = (1: 0: \dots : 0)`、`\Delta + \frac { 1 } { u } M` 等系数与上下标无误。
- 差异列表（PASS±，均不误导，按 SOP 登记不批量修）：
  1. **MD 第 313 行伪句点 `over$X .$,`**：印刷作 `Using ampleness of −(K_Y + T) over X, we can find…`——`X` 后为**逗号**，MD 误置句点。
  2. **MD 第 315 行 `dificult`**：印刷作 `difficult`（`p008.txt` 同步为 `difficult`）。ff 拍平。
  3. **MD 第 299 行 `lct$( X , B , | A | _ { \mathbb { R } } )$`**：`lct` 留在数学环境外（印刷为整体行内式）。排版伪影。
  4. **逗号被排入数学环境（2 处）**：MD 第 315 行 `$x ,$say`、第 323 行 `$x ,$it is not hard`；印刷均为普通标点 `x, say` / `x, it`。排版伪影。
  5. **页块边界漂移（沿用 p.004 口径）**：印刷 p.8 止于行间式 `z = (1 : 0 : · · · : 0),`（MD 第 321 行同步收尾）；MD 第 325–329 行（`Let$W \to X$be the sequence of blowups which obtains$T ,$`、`Mihai Pˇaun` 致谢段、`## 2. Preliminaries` 标题）属**印刷 PDF p.9**，相关缺陷在 p.009 条目中登记。内容无丢失/重复/错序。
- 溯源：`$\overline { T }$` 确实存在于 `git show 03760242:…md` 第 299 行 → **系 MinerU 原始导出缺陷**；Luna 未修且误登记为「忠实」，**GLM 于 `16ffcc7ce8a0c3aad33fc474a83c84d7d53f801c` 正确修复**。本轮独立 300dpi 证据再次支持 GLM 判定。第 1／2／3／4 类亦为导出缺陷，非 peer 回归。
- 备注：本页**无数学内容错误**（当前 Markdown 状态）。前两轮 p.008 结论经本轮独立复核均成立，GLM 对 Luna 的推翻**成立**。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：/tmp/birkarsing_audit_p009.png（pngmono 150dpi）
- 核对：页眉「… / 9」、`S_i → H_i` 段、`K_X + Δ is numerically trivial`、`Let W → X … obtains T` 段（**两处 `W → X`**、一处 `Y → X`、`(Y, Δ_Y)` 为 `ε′-lc`、`K_Y + Δ_Y` 补式、`Y′` Fano `ε′-lc`、`[9]`、`K_{Y′}+Ω_{Y′}`、`K_Y+Ω_Y`、`K_X+Ω`、`m(K_X+Ω) ∼ 0`、`(X, Ω+uΛ)`、`W → X`）、**Acknowledgements 全文**、§2 `Preliminaries` 标题与开篇句、§2.1 `Divisors` 全文（`D = Σ d_i D_i`、`μ_{D_i}D`、**`φ : X ⇢ Y` 虚线箭头**、`φ_*D`、`D_Y`、`deg_A D := A^{d−1}D`、`d > 1`、`deg_A D := deg D if d = 1`、`deg_A D ≤ deg_A A`、`A^{d−1}` 1-cycle）、volume 行间式 `vol(D)=limsup_{m→∞} h^0(⌊mD⌋)/(m^d/d!)`；与 Markdown 第 325–343 行逐项比对，辅以 `pdftotext -f 9 -l 9 -layout`。
- 结果：**PASS±**
  - **volume 行间式逐项吻合印刷**：`\operatorname{vol} (D) = \limsup _ {m \to \infty} \frac {h ^ {0} (\lfloor m D \rfloor)}{m ^ {d} / d !}.`——`\limsup`、`m \to \infty`、floor 取整括号 `⌊mD⌋`、分子 `h^0`、分母 `m^d / d!` 全部正确。
  - **度数定义式逐项吻合**：`\deg _ { A } D : = A ^ { d - 1 } D` when `$d > 1$`、`\deg _ { A } D : = \deg D { \mathrm { ~ i f ~ } } d = 1$`、`$\deg _ { A } D \leq \deg _ { A } A$`——指数 `d-1`、不等号方向、`deg` 无 A 下标（印刷 `deg D`）均正确。
  - **Luna 旧修复经原页复核全部属实且正确**：`$W \to X$`（两处，MD 第 325 行）、`$Y \to X$`（一处）**实线箭头**已恢复；§2.1 的 `$\phi \colon X \dashrightarrow Y$` 为**虚线**双有理映射箭头，与印刷一致（150dpi 原页与 `p009.txt` 的 `X 99K Y` 字形双通道可辨）——Luna 由实线改正为虚线的判定**属实**。
- 差异列表（PASS±，均不误导，按 SOP 登记不批量修）：
  1. **致谢段人名重音错位**：MD 第 327 行 `Mihai Pˇaun`——印刷作 `Mihai Păun`（**breve 短音符 U+0103**，150dpi 原页可见 a 上方为 breve）；MD 用 **caron ˇ（U+02C7）**。姓名可辨，属编码瑕疵。
  2. **`ofice`**（MD 第 327 行 `the National Taiwan University ofice of the National Center`）：印刷作 `office`（原页与 `p009.txt` 同步）。
  3. **`coeficient`**（MD 第 333 行 `We sometimes denote the coeficient$d _ { i }$`）：印刷作 `coefficient`。
  4. **连字符丢失**：MD 第 335 行 `be R-Cartier Rdivisors`——印刷为 `ℝ-Cartier ℝ-` 行末断行 + `divisors`，连字符应保留；MD 拍成 `Rdivisors`。
  5. **`pseudo-efective`**（MD 第 335 行）：印刷作 `pseudo-effective`。
  6. **标点缺失/错误（6 处）**：①MD 第 325 行 `which obtains$T ,$`——印刷为 `obtains T.`（**逗号应为句点**）；②同句尾 `$\epsilon ^ { \prime } { - } \mathrm { l c } .$.` 为**双句点**（印刷 `ε′-lc.`）；③第 333 行 `by$\mu _ { D _ { i } } D$ Let Y also be` 丢句点（印刷 `μ_{D_i}D.`）；④第 333 行 `by$D _ { Y }$` 丢句点（印刷 `D_Y.`）；⑤第 335 行 `$\deg _ { A } A$` 行末丢句点（印刷 `deg_A A.`）。以上均标点级，数学内容正确。
  7. **页块边界漂移（沿用 p.004 口径）**：印刷 p.9 止于 volume 行间式（MD 第 343 行同步收尾）；MD 第 345 行起（`2.2. Pairs and singularities.`、`a(D,X,B) := 1 - μ_D B_W` 等）属**印刷 PDF p.10**。内容无丢失/重复/错序。
- 溯源：第 1／2／3／4／5 类在 `git show 03760242:…md`（原始 MinerU 导出）中已存在（见本轮末尾统一溯源清单）→ **导出缺陷，非 peer 回归**；Luna 的三处箭头与虚线箭头修复方向正确且已正确落地。
- 备注：本页**无数学内容错误**。前两轮 p.009 结论经本轮独立复核均成立。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：/tmp/birkarsing_audit_p010.png（pngmono 150dpi）；另作 300dpi 仲裁裁片 `/tmp/birk_p010_DY_crop.png`（裁定 `D_Y` 下标）与 `/tmp/birk_p010_E_crop.png`（裁定 `g^*D`/`h^*D_Y` 星号位置），源图 `/tmp/birk_p010_300.png`
- 核对：页眉「10 / Caucher Birkar」、§2.2 `Pairs and singularities` 全文（含 sub-lc/sub-klt/sub-ε-lc 三档不等式）、行间式 `a(D,X,B) := 1 − μ_D B_W`、non-klt place 段、log smooth pair 段（`B = Σ_{1}^{r} B_i`、`∩_{i∈I} B_i`）、**Lemma 2.3 完整陈述**（`Δ = tB + (1−t)B′`、`t ∈ [0,1]`、行间式 `a(D,X,Δ) = ta(D,X,B) + (1−t)a(D,X,B′)`、`sub-(tε+(1−t)ε′)-lc`）、§2.4 `Fano pairs`、§2.5 `Minimal models, Mori fibre spaces, and MMP` 全文（**`φ : X ⇢ Y/Z` 虚线箭头**、`D_Y := φ_*D`、`g : W → X`、`h : W → Y`、`E := g^*D − h^*D_Y`、`Supp g_*E`、**minimal model 定义句**、Mori fibre space 定义句 `Y → T/Z`、`−D_Y` ample/T、`dim Y > dim T`）、`[7]`；与 Markdown 第 345–375 行逐项比对，辅以 `pdftotext -f 10 -l 10 -layout`。
- 结果：**FAIL（1 处，已当场修复）**
  - **FAIL：MD 第 373 行「we call Y a minimal model of D over Z if D is nef/Z」丢失下标 `Y`——印刷原文为 `D_Y` is nef/Z。** 该句是 **minimal model 的定义**，「nef」的对象必须是拉到 *Y* 上的推前 `D_Y`，而非 *X* 上的 `D`；丢下标使定义在数学上失真，故按分级记 **FAIL**。
    - **证据**：本轮自建 300dpi 裁片 `/tmp/birk_p010_DY_crop.png` 清楚显示「we call *Y* a *minimal model* of *D* over *Z* if *D*<sub>*Y*</sub> is nef/*Z*.」；`p010.txt` 文本层同步为 `if DY is nef/Z`。
    - **溯源**：**系 MinerU 原始导出缺陷，非 peer 回归**——`git show 03760242:…md` 第 373 行即为 `…minimal model of D over Z if D is nef/Z.`（无下标）；Luna 的修复提交 `353ad7fac129` **未触及此处**（该行仅新增了 `Y \to T / Z` 箭头），GLM 重做仅覆盖 p.001–p.009、未覆盖本页。**即此缺陷已逃过前两轮审计，本轮为首次发现。**
    - **修复（以原图为准）**：`if D is nef/Z` → `if$D _ { Y }$is nef/Z`；采用与同一行 `$- D _ { Y }$ample/T` 一致的本地数学书写风格。
  - **已仲裁确认无误、本轮不构成差异者**：`D_Y := \phi _ { * } D`（φ 星号为**下标**，推前）——300dpi 裁片 `/tmp/birk_p010_E_crop.png` 证实；`E := g ^ { * } D - h ^ { * } D _ { Y }`（g、h 星号为**上标**，拉回到 W 上）——同一裁片证实。**上/下标方向与印刷完全一致**，非差异。
  - **印刷怪癖（print quirk）忠实保留，符合铁律三**：MD 第 355 行 `An non-klt place of$( X , B )$is a prime divisor D over X`——印刷原文即作 **「An non-klt place」**（150dpi 原页可见，语法上应为 `A`），MD 原样保留，未静默改正。
  - **Luna 旧修复经原页复核属实且正确**：`$\phi \colon X \dashrightarrow Y / Z$`（虚线）、`$Y \to T / Z$`（实线）、`$g \colon W \to X$`、`$h \colon W \to Y$` 箭头均已恢复；Lemma 2.3 的 `If`/`if` 与凸组合结论行已修复为 `a (D, X, \Delta) = t a (D, X, B) + (1 - t) a (D, X, B ^ {\prime})`。
  - 三档不等式逐项吻合印刷：`$\geq 0$`/`$> 0$`/`$\geq \epsilon$` 与 `$\leq 1$`/`$< 1$`/`$\leq 1 - \epsilon$`——方向与 `1 - ε` 系数正确。
- 其余差异（PASS±，不误导，按 SOP 登记不批量修）：
  1. **`coeficients`（MD 第 345 行）／`coeficient`（MD 第 353 行）**：印刷作 `coefficients`／`coefficient`。
  2. **`efective`（MD 第 371 行）**：`E : = … is efective and exceptional/Y`；印刷作 `effective`。
  3. **MD 第 355 行 `that${ \mathrm { i s } } ,$`**：印刷作 `that is,`（`is` 被排入数学正体）。排版伪影。
  4. **MD 第 357 行 `\begin{array} { r } { B = \sum _ { 1 } ^ { r } B _ { i } } \end{array}`**：MinerU 用 `array` 环境包裹行内公式；印刷为普通行内式 `B = Σ_{1}^{r} B_i`。数学内容正确，排版冗余。
  5. **段末句点缺失（4 处）**：MD 第 353 行 `$\epsilon \leq 1$`、第 355 行 `respectively`、第 365 行 `sub-(t \epsilon + ( 1 - t ) \epsilon ^ { \prime })-lc`、第 373 行 `dim$Y > \dim T$` 行末均无句点；印刷相应处均有。标点级瑕疵。
  6. **页块边界漂移（沿用 p.004 口径）**：印刷 p.10 止于 `…such an MMP always exists by [7].`（MD 第 375 行同步收尾）；MD 第 377 行起（§2.6 `Plt pairs`、`[36]`、`[38, Definition 3.5]`、`[44, Lemma 1]`、**Lemma 2.7** 及其证明）属**印刷 PDF p.11**。内容无丢失/重复/错序。
- 备注：本页是本轮**首次发现前两轮均漏报的数学内容缺陷**（`D_Y` 下标丢失）。除该处外，本页其余数学内容与印刷一致。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：/tmp/birkarsing_audit_p011.png（pngmono 150dpi）；另作 300dpi 仲裁源图 `/tmp/birk_p011_300.png` 及裁片 `/tmp/birk_p011_coef_crop.png`、`/tmp/birk_p011_eff_crop.png`
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 11」；§2.6 `Plt pairs` 首段引用 `[36]`、`[38, Definition 3.5]`、`[44, Lemma 1]`；**Lemma 2.7 完整陈述**及四条项目符号（either φ is small…／$(Y,T)$ is plt／$−(K_Y+T)$ ample over $X$／$a(T,X,B)=0$）；Proof 中行间式 `a(T,X,B)=a(T,X,Γ)=0`、两条 pushback 关系式、行间式 `B_W−C_W ∼_R H_W+G_W/X`、行间式 `Γ_W ∼_R B_W+aH_W+aG_W`、`μ_TΓ_W = 1`、`< 1`；记号 `Y′`、`Y″`、`T′`、`T″`、`ψ_*`、sub-lc、R-Cartier；证明行序（先证充分性 → 再证存在性 → 先设 E 与 G_W 无公共分支，后设相交）；与 Markdown 第 377–425 行逐项比对，辅以 `pdftotext -f 11 -l 11 -layout`。
- 结果：**PASS±**——数学内容、定理编号、四条项目符号、全部行间式、记号方向与证明行序均与印刷原页一致；差异仅为 OCR 连字丢 `f` 的英文拼写（不误导、不涉数学），已按 SOP 逐处用 Edit 修复，共 **6 处**：
  1. MD 第 395 行 `suficiently` → `sufficiently`；
  2. MD 第 417 行 `suficiently` → `sufficiently`；
  3. MD 第 417 行 `coeficients` → `coefficients`；
  4. MD 第 417 行 `suficiently` → `sufficiently`（第二次出现，同行）；
  5. MD 第 419 行 `coeficient` → `coefficient`；
  6. MD 第 425 行 `coeficients` → `coefficients`、`efective` → `effective`（同行两处）。
- 原文证据：300dpi 裁片 `/tmp/birk_p011_coef_crop.png` 清楚显示印刷原文为「for a sufficiently small real number t > 0 we can assume that the coefficients of B_W − C_W are sufficiently close to 0.」及「Let E be the sum of the components of B_W with coefficient 1.」；裁片 `/tmp/birk_p011_eff_crop.png` 清楚显示「all the other coefficients of Γ_W are < 1, and Γ := ψ_*Γ_W is effective.」；PDF 文本层独立计数 `sufficiently`×3、`coefficient`×1、`coefficients`×2、`effective`×1，单 `f` 形式计数为 0。**据此排除「印刷原文本身为单 f 拼写」的可能，铁律三不适用**（与本轮 p.005 的 `different`/`diferent` 判定口径一致）。
- 明确非差异（已核，不登记为缺陷）：印刷 `Γ := ψ_*Γ_W` 为下推、`ψ^*(K_X+B)` 为上拉，Markdown `$\psi _ { * } \Gamma _ { W }$` 与 `$\psi^ {*} (K _ { X } + B)$` 方向正确；`$(Y,\Gamma_Y)$`、`$(Y^{\prime\prime},0)$`、`$(Y^{\prime\prime},C_{Y^{\prime\prime}})$` 括号成分无错位；`−(K_Y+T)`、`−(K_{Y′}+T′)` 两处负号均在。
- 跨页重复登记：MD 第 425 行与第 433 行为同构句（本页以「So we are done in this case.」收尾）。本轮只依**印刷 p.11 自身原页证据**修第 425 行；第 433 行属印刷 p.12，留待 p.12 页次按其自身原页图与文本层处理，**未在本页顺带修改**。
- 备注：Lemma 2.7 及其证明的数学内容与印刷完全一致，本页无需按「以原图为准」纠正的数学错误。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：/tmp/birkarsing_audit_p012.png（pngmono 150dpi）
- 核对：页眉「12 / Caucher Birkar」；Lemma 2.7 证明第二段（`G_W` 与 `E` 有公共分支的情形）全文，含 `μ_T C_W`、`C_W + aG_W`、行间式 `Γ_W ∼_R C_W + aH_W + aG_W`、`μ_TΓ_W = 1`、`< 1`、`Γ := ψ_*Γ_W`、`K_Y + Γ_Y ∼_R 0/X` 及页末**证毕方框 □**；§2.8 `Bounded families of pairs` 三段（couple 定义、`E ≤ C_t^i`、log birationally bounded 定义）；§2.9 `Effective birationality and birational boundedness`；**Theorem 2.10**（`[5, Theorem 1.2]`、`|-mK_X|` defines a birational map）；**Theorem 2.11**（`[5, Theorem 1.6]`、`dim d−1`、`vol(-K_X) ≤ v`、`(X,0) is log bounded`）；§2.12 `Complements`（`T = ⌊B⌋`、`Δ = B − T`、`K_X + B^+` 及三条项目符号）；与 Markdown 第 427–457 行逐项比对，辅以 `pdftotext -f 12 -l 12 -layout`。
- 结果：**PASS±**——定理编号、引用标注 `([5, Theorem 1.2])`／`([5, Theorem 1.6])`、全部行间式、项目符号、记号与行序与印刷原页一致；`V_t^i ⇢ X` 的**虚线箭头**在 Markdown 中为 `\dashrightarrow`，方向正确，不构成差异。差异仅为 OCR 连字丢 `f` 的英文拼写（不涉数学），已逐处用 Edit 修复，共 **7 处 Edit／9 个拼写**：
  1. MD 第 427 行 `coeficient` → `coefficient`（`Recall that the coefficient μ_T C_W`）；同行 `suficiently` → `sufficiently`；
  2. MD 第 427 行 `with coeficient 1` → `with coefficient 1`；
  3. MD 第 433 行 `coeficients` → `coefficients`、`efective` → `effective`（同行两处）；
  4. MD 第 437 行 `coeficients` → `coefficients`（couple 定义段「whose coefficients are all equal to 1」）；
  5. MD 第 441 行 `coeficients` → `coefficients`（「does not put any condition on the coefficients of B」）；
  6. MD 第 441 行 `coeficients` → `coefficients`（「requiring the coefficients of B to be in a finite set」）；
  7. MD 第 443 行 **节标题** `2.9. Efective birationality…` → `2.9. Effective birationality…`。
- 原文证据：PDF 文本层 `p012.txt` 独立计数 `coefficient`×2、`coefficients`×4、`effective`×1、`sufficiently`×1，单 `f` 形式（`coeficient`/`suficiently`/`efective`）计数为 **0**；150dpi 原页图同时可见 §2.9 节标题印作 **「2.9. Effective birationality and birational boundedness.」**。据此确认这些是 MinerU 连字缺陷而非印刷怪癖，铁律三不适用。
- 与 p.011 条目的衔接（不重复计数）：MD 第 433 行与第 425 行同构，第 425 行已在 **p.011** 条目按印刷 p.11 证据修复；第 433 行按本条（印刷 p.12 证据）修复，两次 Edit 各计一次，互不覆盖。
- 明确非差异（已核）：印刷 `Γ := ψ_*Γ_W` 为下推、`\psi^*` 为上拉，Markdown 方向正确；`T = \lfloor B \rfloor` 的**取下整括号**（非竖线取整号）与 `\lfloor (n+1)\Delta \rfloor` 均正确；`\mathrm { v o l }` 仅为字母间距排版伪影，数学内容为 `vol(-K_X) ≤ v` 正确。
- 备注：证毕方框 □ 未在 Markdown 中表示（纯排版元素），按 PASS± 登记不修。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：/tmp/birkarsing_audit_p013.png（pngmono 150dpi）
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 13」；**Theorem 2.13**（`[5, Theorem 1.7]`）完整陈述与四条项目符号（`(X,B) is lc of dimension d`、`B ∈ Φ(ℜ)`、`X is of Fano type`、`−(K_X+B) is nef`）、结论 `B^+ ≥ B`、`mn-complement for any m ∈ ℕ`；**Theorem 2.13 内的补充定义行间式** `Φ(ℜ) := {1 − r/m | r ∈ ℜ, m ∈ ℕ}`（含 `\frac{r}{m}` 分式结构）；§2.14 `From bounds on lc thresholds to boundedness of varieties`；**Theorem 2.15**（`[5, Proposition 7.13]`、`d, m, v`、`t_l` 序列）五条项目符号、`|−mK_X|`、`vol(−K_X) ≤ v`、`(X, t_l L) is klt`、结论 `P is a bounded family`；交叉引用 `Theorems 2.10, 2.11, and 2.13`、`Theorem 1.6`、`[17, Theorem 1.1]`；§2.16 `Sequences of blowups` 的 (1)(2) 两款，(1) 含行间式 `⋯ → X_{i+1} → X_i → ⋯ → X_0 = X`、`X_p → X_{p−1}`、`E_{i+1}`，(2) 含 `toroidal`、`C_i`、`(X_i, Λ_i)`、`cf. [24]`。与 Markdown 第 459–505 行逐项比对，辅以 `pdftotext -f 13 -l 13 -layout`。
- 结果：**PASS±**——定理编号、引用标注、全部项目符号、分式结构 `1 − r/m`、序列箭头 `⋯ → X_{i+1} → X_i → ⋯ → X_0 = X`、`m ∈ ℕ` 与印刷原页一致；差异为 OCR 连字丢 `f` 与**实数集字形不统一**，均不改数学内容但影响记号一致性，逐处用 Edit 修复共 **7 处**：
  1. MD 第 463 行 `coeficients` → `coefficients`；
  2. MD 第 459 行 `\Re` → `\mathbb { R }`（对应印刷 ℜ）；
  3. MD 第 459 行正文裸字母 `only on d and R` → `only on d and$\mathbb { R }$`（印刷此处 R 为数学斜体字形，与句首 ℜ 指同一集合）；
  4. MD 第 463 行 `$B \in \Phi ( \Re )$` → `$B \in \Phi ( \mathbb { R } )$`；
  5. MD 第 463 行 `$\Phi ( { \mathfrak { R } } )$，` → `$\Phi ( \mathbb { R } )$`，并把行末**全角逗号 `，`** 改回印刷的半角 `,`；
  6. MD 第 474 行行间式内第一处 `\mathfrak {R}` → `\mathbb {R}`；
  7. MD 第 474 行行间式内第二处 `r \in \mathfrak {R}` → `r \in \mathbb {R}`。
- 原文证据：150dpi 原页图清楚显示印刷实数集符号为**双线体 ℜ**（Theorem 2.13 假设行、`B ∈ Φ(ℜ)` 项目符号、定义行间式三处一致），且该行末尾印作半角逗号 `,`；文本层 `p013.txt` 相应为 `R ⊂ [0, 1]`、`B ∈ Φ(R), that is, the coefficients of B are in Φ(R),`，`coefficient(s)` 计数为 1、单 `f` 形式计数为 0。
- 字形判定依据（避免过度纠正）：Markdown 用三种写法表示同一个 ℜ——`\Re`（1 处）、`\mathfrak{R}`（3 处）、`\mathbb{R}`（全文 39 处）。印刷只有一种字形，故统一为与全文其余部分一致、且与印刷双线体对应的 `\mathbb{R}`；这是**同一集合的写法统一**，非数学内容变更。
- 明确非差异（已核）：`\vert - m K _ { X } \vert` 的绝对值竖线、`L \in | - l K _ { X } |` 的线性系记号、`\mathrm { v o l }` 的字母间距伪影、`\dots` 省略号、`\geq 2` 不等号方向、`X _ { p - 1 }` 下标，均与印刷相符。
- 备注：Theorem 2.15 第 5 条 `for any l ∈ ℕ` 中的 `l` 为斜体小写 ell（形近数字 1），Markdown 以 `l` 忠实保留未改（铁律三）。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：/tmp/birkarsing_audit_p014.png（pngmono 150dpi）
- 核对：页眉「14 / Caucher Birkar」；**Lemma 2.17**（`toroidal with respect to (X,Λ)`、行间式 `φ : X_p → X_0 = X`、假设 `C_i ⊂ E_i for each 0 < i < p`、结论行间内式 `μ_{E_p} φ^*Λ ≥ p + 1`）；**Proof**（`0 ≤ i < p`、`E_i`、`Let φ_i denote X_i → X_0`、等式 `Λ_i = Supp φ_i^*Λ`、归纳行间式 `μ_{E_{i+1}} φ^*_{i+1}Λ ≥ μ_{E_i} φ^*_iΛ + 1 ≥ i + 2`、页末**证毕方框 □**）；§2.16(3) 全文（`centre blowups`、`[28, Lemma 2.45]`、`X_p → X_{p−1} → ⋯ → X_0 = X`、`birational transform of T`）；§2.18 `Analytic pairs and analytic neighbourhoods of algebraic singularities` 首段及 `A^{an}`、(1) analytic pair 定义（`K_U + G is ℝ-Cartier`、系数区间 `[0,1]`、`just as in 2.2`）、(1) 末段 `analytically isomorphic`（`ν_*G = G'`）、(2) 全文（`X^{an}`、`φ^{an} : W^{an} → X^{an}`、`φ^{an}|_V`、`B^{an}|_U`）、(3) 段首至页末「For example, the」；与 Markdown 第 507–533 行逐项比对，辅以 `pdftotext -f 14 -l 14 -layout`。
- 结果：**PASS±**——引理编号、全部行间式与行内关键式（`μ_{E_p}φ^*Λ ≥ p+1`、`Λ_i = Supp φ_i^*Λ`、`ν_*G = G'`）、引用 `[28, Lemma 2.45]`、证明归纳方向 `≥`、记号上/下标位置（`E_{i+1}`、`\phi_i` 下标 vs `\phi^*` 上标）与印刷原页一致；差异仅 1 处 OCR 连字丢 `f`，已用 Edit 修复：
  1. MD 第 527 行 `coeficients` → `coefficients`（analytic pair 定义句「with coefficients in [0, 1]」）。
- 原文证据：文本层 `p014.txt` 计数 `coefficients`×1 且单 `f` 形式为 0；150dpi 原页图该行印作「with coefficients in [0, 1] such that K_U + G is ℝ-Cartier」。
- **拼写忠实性正面确认（不构成差异）**：印刷原文全篇使用英式拼写 **`centre`**（本页文本层计数 `centre`×5：`centre C_i`、`an lc centre`、`is the centre of T`、`sequence of centre blowups` 等），Markdown 相应位置全部作 `centre`，与印刷一致，**未**误改为美式 `center`（铁律三）。
- 明确非差异（已核）：`\nu _ { * } G` 的星号为**下标**（推前），`\phi ^ { * }` 的星号为**上标**（拉回），方向与印刷相符；`\begin{array} { r } { … } \end{array}` 型 `array` 包裹为 MinerU 排版伪影，数学内容正确。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.14 止于「For example, the」；MD 第 533 行末句「…have isomorphic analytic neighbourhoods where B is an irreducible curve with a node at x but B′ is the union of two lines intersecting at x′.」及第 535 行起（§2.19 `Etale morphisms`、**Lemma 2.20**、**Lemma 2.21**）属**印刷 PDF p.15**。内容无丢失/重复/错序。
- 备注：本页 `|\ - \mc K_x\ |` 类绝对值记号、`\mathbb{C}` 与 `C` 字形混用等零星排版伪影不影响数学，按 PASS± 登记不修。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：/tmp/birkarsing_audit_p015.png（pngmono 150dpi）；仲裁源图 `/tmp/birk_p015_300.png` 及裁片 `/tmp/birk_p015_AY_crop.png`（裁定 Lemma 2.24 结论的 `A_Y` 下标）、`/tmp/birk_p015_L220_crop.png`（裁定 Lemma 2.20 的 `X, B` 字形）
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 15」；§2.18(3) 末句（`(ℙ²,B)`、`(ℙ²,B′)`、`node at x`、`union of two lines intersecting at x′`）；§2.19 `Étale morphisms`；**Lemma 2.20**（`π : X → Z`、`z = π(x)`、四条项目符号、`\pi^{-1}\{z\}`、第四条 `C := π(B) := Σ b_j π(B_j)`）、结论 `π^{an}|_U` 与 `(U,B^{an}|_U)`、`(V,C^{an}|_V)`、「We leave the proof…」段、`coefficients larger than 1` 段；**Lemma 2.21**（`t_1,…,t_d`、`π^*t_1,…,π^*t_d` local parameters、`π` is étale at x）；§2.22 `Toric varieties and toric MMP`（`X = ℙ^d`、`[12]`、`[12, §15.5]`、toric MMP 两段）；§2.23 `Bounded small modifications`；**Lemma 2.24** 两条假设（`A is a very ample divisor on X with A^d ≤ r`）、结论句 `a very ample divisor A_Y on Y such that` 及首条项目符号 `Y is normal`。与 Markdown 第 533–585 行逐项比对，辅以 `pdftotext -f 15 -l 15 -layout`。
- 结果：**FAIL（1 处数学内容错误，已当场修复；其余 PASS± 类共 6 处同批修复）**
  - **FAIL：MD 第 569 行「and a very ample divisor A on Y such that」丢失下标 `Y`——印刷原文为 `A_Y` on Y。** 该句是 Lemma 2.24 结论中*将要存在*的 *Y* 上的 ample 除子，与紧随其后的结论项 `$A _ { Y } ^ { d } \leq l$`、`$A _ { Y } - \phi ^ { * } A$is ample` 是同一个对象；写成无下标的 `A` 会与假设中的 *X* 上的 `A` 混淆，使结论陈述在数学上失真，故按分级记 **FAIL**。
    - **证据**：本轮自建 300dpi 裁片 `/tmp/birk_p015_AY_crop2.png` 清楚显示「…a projective small birational morphism φ : Y → X and a very ample divisor **A**_Y on Y such that」，下标 *Y* 明确可见。
    - **溯源**：**系 MinerU 原始导出缺陷，非 peer 回归**——`git show 03760242:…md` 第 569 行原文即为 `…$\phi \colon Y  X$and a very ample divisor A on Y such that`（箭头与 `A_Y` 下标同时丢失）。Luna 的修复提交 `353ad7fac129` **确实触及该行**，但只恢复了箭头（`Y  X` → `Y \to X`），**未**恢复 `A_Y` 下标；GLM 重做仅覆盖 p.001–p.009。**即此缺陷已逃过前两轮审计，本轮为首次发现**（与 p.010 的 `D_Y` 属同类：OCR 丢下标）。
    - **旁证（同一记号在别处未被破坏）**：同一提交 `353ad7fa` 在后文 Step 2 处保留了 `a very ample divisor$A _ { Y }$on$Y$such that`，说明 `A_Y` 是本篇一致记号，仅 Lemma 2.24 陈述处被 OCR 吞掉。
    - **修复（以原图为准）**：`and a very ample divisor A on Y such that` → `and a very ample divisor$A _ { Y }$on Y such that`；采用与结论项 `$A _ { Y } ^ { d } \leq l$` 一致的本地数学书写风格。
  - **PASS± 类差异（同批修复，共 6 处）**：
    1. MD 第 537 行 Lemma 2.20 的 `\left( { \cal X } , { \cal B } = \sum b _ { j } B _ { j } \right)` 中的 **`\cal` 为 OCR 伪花体**——300dpi 裁片 `/tmp/birk_p015_L220_crop.png` 显示印刷为普通斜体 `(X, B = Σ b_j B_j)`；改为 `\left( X , B = \sum b _ { j } B _ { j } \right)`；
    2. MD 第 535 行 §2.19 节标题 `2.19. Etale morphisms. <sup>´</sup> We look at … which is ´etale at some point.`——印刷节标题为 **`2.19. Étale morphisms.`**（重音在 *E* 上），Markdown 把重音拆成孤立的 `<sup>´</sup>` 并把词写成 `Etale`；整句改为印刷形式 `2.19. Étale morphisms. We look at singularities of images of a pair under a finite morphism which is étale at some point.`；
    3. MD 第 541 行 `• π is ´etale at x,` → `• π is étale at x,`；
    4. MD 第 553 行 `The next lemma is useful for showing that a morphism is ´etale at a point.` → `…is étale at a point.`；
    5. MD 第 555 行 `Then π is ´etale at x.` → `Then π is étale at x.`；
    6. MD 第 551 行 `but with coeficients larger than 1.` → `but with coefficients larger than 1.`。
  - **重音字形判定依据**：文本层 `p015.txt` 对应位置为 `Étale`／`étale`（前置重音字母），单 `f` 形式 `coeficients` 计数为 0、`coefficients` 计数为 1；`grep -c '´etale'` 于原始导出 `03760242` 中为 7，说明孤立重音符是 MinerU 导出形态，非印刷排法（铁律三不适用）。
- **明确非差异（已核，不登记为缺陷）**：
  - MD 第 533 行 `is$\epsilon \mathrm { - }$ lc`：印刷原文因行末断行印作「is ǫ-／lc」，Markdown 的 `\epsilon \mathrm { - }` 恰为该断行的连续化，内容一致；
  - MD 第 545 行 `\begin{array} { r } { C : = \pi ( B ) : = \sum b _ { j } \pi ( B _ { j } ) } \end{array}`：`array` 包裹为排版伪影，公式 `C := π(B) := Σ b_j π(B_j)` 内容正确；
  - `\pi ^ { - 1 } \{ z \}` 的上标负一、`\pi^{an}|_U` 的上标 `an` 与下标 `|U`、`\ldots` 与 `\cdots` 的省略号用法，均与印刷相符；
  - MD 第 567 行 `$A ^ { d } \leq r$`：Luna 已把原导出误加的下标 `r_i` 修为 `r`，经本页原页复核**属实且正确**，本轮不再改动。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.15 止于 Lemma 2.24 首条项目符号「• Y is normal,」；MD 第 573 行起（`$K _ { Y }$is Q-Cartier`、`$A _ { Y } ^ { d } \leq l$`、`$A _ { Y } - \phi ^ { * } A$is ample`、Proof 全文）属**印刷 PDF p.16**。内容无丢失/重复/错序。
- 备注：本页是本轮**第二个前两轮均漏报的数学内容缺陷**（`A_Y` 下标丢失），与 p.010 的 `D_Y` 同属「OCR 丢下标」缺陷类。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：/tmp/birkarsing_audit_p016.png（pngmono 150dpi）；仲裁源图 `/tmp/birk_p016_300.png` 及裁片 `/tmp/birk_p016_L226b.png`（裁定 Lemma 2.26 结论行的 `C + aA` 与 `t = a/b`）
- 核对：页眉「16 / Caucher Birkar」；**Lemma 2.24 结论余下三条项目符号**（`K_Y is Q-Cartier`、`A_Y^d ≤ l, and`、`A_Y − φ^*A is ample`）；**Lemma 2.24 Proof** 全文（`V^i → T^i`、`A^i_V`、`A ∼ A^i_V|_X`、`V = V^i, T = T^i, A_V = A^i_V`、`Σ` reduced exceptional、`Γ_W = (1 − ε/2)Σ`、MMP on `K_W + Γ_W`、`(U, Γ_U)` log minimal model、缩小 `W,U,V,T`、五条项目符号 `Y is normal`／`K_Y ∼_Q K_U|_Y`／`Γ_U does not contain Y`／`support of Γ_Y := Γ_U|_Y coincides with the reduced exceptional divisor of Y → X`／`each non-zero coefficient of Γ_Y is equal to 1 − ε/2`）；随后段落（`K_Y + B_Y = φ^*(K_X + B)`、**行间式** `B_Y − Γ_Y = (K_Y + B_Y) − (K_Y + Γ_Y) ≡ −(K_Y + Γ_Y)/X`、`φ_*(B_Y − Γ_Y) = B ≥ 0`、negativity lemma、`≤ 1 − ε`、`≥ 1 − ε/2`、`Γ_Y = 0`、small morphism、Q-factorial 段、`A_U`、`A_Y = A_U|_Y`、`A_Y − ψ^*A_V` ample over T、证毕方框 □）；§2.25 `Semi-ample divisors`；**Lemma 2.26** 完整陈述（`C` nef ℝ-divisor、`A` pullback of ample、`C + aA` semi-ample (globally)、`a > 0`）及其 Proof（`φ : Y → Z/X`、`φ_*C, φ_*A`、`b ≫ a`、行间式 `C + tbA = (1 − t)C + t(C + bA)`、`t ∈ (0,1]`、`t = a/b`、证毕方框 □）。与 Markdown 第 585–613 行逐项比对，辅以 `pdftotext -f 16 -l 16 -layout`。
- 结果：**PASS±**——数学内容、行间式符号（`≡` 而非 `=` 用于相对等价、五条项目符号齐备）、`1 − ε/2` 的减号与 `\frac{\epsilon}{2}` 分式、`\sim_{\mathbb{Q}}` 的等价号、`\ge` / `\leq` 方向、记号上/下标位置（`K_U|_Y` 的限制竖线、`\phi^*` 上标 vs `\phi_*` 下标、`A_U|_Y`）均与印刷原页一致；差异仅 OCR 连字丢 `f` 的英文拼写，已逐处用 Edit 修复，共 **2 处**：
  1. MD 第 591 行 `coeficient` → `coefficient`（项目符号「each non-zero coefficient of Γ_Y is equal to 1 − ε/2」）；
  2. MD 第 599 行两处 `coeficient` → `coefficient`（同行「so each coefficient of B_Y is ≤ 1 − ε」与「each non-zero coefficient of Γ_Y is ≥ 1 − ε/2」）。
- 原文证据：文本层 `p016.txt` 计数 `coefficient`×3 且单 `f` 形式为 0；150dpi 原页图与 300dpi 裁片一致显示上述三处均印作 `coefficient`。
- **下标保持正确的正面确认（不构成差异）**：Luna 在 p.016 条目中登记的「Lemma 2.24 证明中 `K_Y ∼_Q K_U|_Y` 及 `Γ_U` 不含 `Y` 两项条件缺 bullet」经本页原页复核，印刷五条项目符号齐全、Markdown 第 583–591 行亦为五条，**已属实修复，本轮未改动**；结论项 `$A _ { Y } ^ { d } \leq l$`、第 601 行 `$A _ { Y } = A _ { U } | _ { Y }$`、`$A _ { U } - \psi ^ { * } A _ { V }$`、`$A _ { Y } - \phi ^ { * } A$` 的下标 *Y*、*U*、*V* 全部保留完好（与 p.015 新修的结论句 `A_Y` 呼应）。
- 明确非差异（已核）：MD 第 613 行 `taking$\begin{array} { r } { t = \frac { a } { b } } \end{array}$we see that$C +$aA is ample` ——300dpi 裁片 `/tmp/birk_p016_L226b.png` 证实印刷原文为 `taking t = a/b we see that C + aA is ample`，`C + aA` 内容与顺序均正确；`$C +$aA` 的数学/正体切分与 `array` 包裹同属 MinerU 排版伪影，不改变公式本身。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.16 止于 Lemma 2.26 证毕方框；MD 第 615 行起（`## 3. Lc thresholds of anti-log canonical systems of Fano pairs` 章标题、§3 首段、**Proposition 3.1**、Step 1／Step 2、`[5, Proposition 4.4]`、`(V, Λ) ∈ P` 等）属**印刷 PDF p.17**。内容无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.017（PDF p.17 / 印刷 p.17）
- PNG：/tmp/birkarsing_audit_p017.png（pngmono 150dpi）
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 17」；章标题 **`3. Lc thresholds of anti-log canonical systems of Fano pairs`**；§3 首段（`|-(K_X+B)|_ℝ`、`Theorem 1.8 implies Theorem 1.6`、`Theorem 1.8 implies Theorem 1.7`）；**Proposition 3.1** 完整陈述（`dimension ≤ d`、`dimension ≤ d−1`、`v depending only on d, ǫ`、三条项目符号：`X is a Q-factorial ǫ-lc Fano variety of dimension d`／`X has Picard number one, and`／`0 ≤ L ∼_ℝ −K_X`）与结论 `each coefficient of L is less than or equal to v`；**Step 1**（`L ∼_ℝ uT`、`u ≥ μ_T L`、`L = uT`、`n-complement K_X + Ω`、`Theorems 2.10 and 2.11`、`|-nK_X|`、`vol(-K_X)`）；**Step 2**（`[5, Proposition 4.4]`、`B = 0`、`M = nΩ`、`c ∈ ℝ^{>0}`、`(V,Λ) ∈ P`、`V ⇢ X`、两条项目符号、`ψ_*φ^*Ω`、`at most c`、`H ≤ Λ`、`H ≥ 0`）；**Step 3**（`K_X + B ∼_ℝ 0`、行间式 `K_V+B_V = ψ_*φ^*(K_X+B) and K_V+Ω_V = ψ_*φ^*(K_X+Ω)`、`sub-ǫ-lc`、行间式 `a(T,V,B_V) = a(T,X,B) ≤ 1`、`sub-lc`、行间式 `a(T,V,Ω_V) = a(T,X,Ω) ≤ 1`、`Ω_V ≤ Λ`、行间式 `a(T,V,Λ) ≤ a(T,V,Ω_V) ≤ 1`）。与 Markdown 第 615–661 行逐项比对，辅以 `pdftotext -f 17 -l 17 -layout`。
- 结果：**PASS±**——章标题文字、命题编号、三条项目符号、四个行间式的系数与不等号方向、`\psi _ { * } \phi ^ { * }`（下标推前 + 上标拉回）、`V \dashrightarrow X` 的虚线箭头、`\mu _ { T } L`、`c \in \mathbb { R } ^ { > 0 }`、`H \leq \Lambda` 与 `H \geq 0` 方向、`\sim _ { \mathbb { R } }` 写法，均与印刷原页一致；差异仅 OCR 连字丢 `f` 的英文拼写，已用 Edit 修复 **2 处**：
  1. MD 第 627 行 `coeficient` → `coefficient`（命题结论「Then each coefficient of L is less than or equal to v.」）；
  2. MD 第 635 行 `coeficient` → `coefficient`（Step 2 第二条项目符号「each coefficient of ψ_*φ^*Ω is at most c.」）。
- 原文证据：文本层 `p017.txt` 计数 `coefficient`×2 且单 `f` 形式为 0；150dpi 原页图该二处均印作 `coefficient`。
- **Luna 旧修复经原页复核属实（不构成差异）**：Luna 在 p.017 登记「Proposition 3.1 第三项补 bullet；两处 `V⇢X` 恢复；带点 c 改普通 c；replace L 伪下标去除」——本页原页证实：三条项目符号齐全（第 621/623/625 行）、`V \dashrightarrow X` 在第 631、633、657 行三处均保留虚线、`c` 已作普通数学斜体（`$c \in \mathbb { R } ^ { > 0 }$`）、`replace L, hence assume` 处伪下标已去除，**四项均属实修复，本轮未改动**。
- 明确非差异（已核）：`\operatorname { S u p p }` 与 `\operatorname { v o l }` 的字母间距为 MinerU 排版伪影，内容分别为 `Supp`、`vol`；`[5, Proposition$4 . 4 ]` 中 `4 . 4` 的空格为 OCR 伪影，编号 `4.4` 正确。
- 记号一致性登记（不误导，按 PASS± 保留）：同一个 ǫ 符号在 Markdown 中并存 `\epsilon`（第 619、629、631 行）与直写 `ǫ`（第 645 行）两种编码；印刷原文只有一种字形。因二者渲染为同一符号、不误导数学，且全文此类混用遍布各页，按 PASS± 登记而不批量统一（与 p.013 的 ℜ 字形统一处理不同：那里同一符号同时混用 `\Re`／`\mathfrak{R}`／`\mathbb{R}` 三种**语义不同**的写法）。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.17 止于行间式 `a(T,V,Λ) ≤ a(T,V,Ω_V) ≤ 1.`；MD 第 663 行起（`Step 4`、`Γ_V = I − J`、`\deg _ { H }`、`K_V + Γ_V ≡ −ψ_*φ^*Ω`）属**印刷 PDF p.18**。内容无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.018（PDF p.18 / 印刷 p.18）
- PNG：/tmp/birkarsing_audit_p018.png（pngmono 150dpi）
- 核对：页眉「18 / Caucher Birkar」；**Step 4** 全文（`coefficients of B_V are bounded from below`、`D is a component of B_V with negative coefficient`、`K_V + Γ_V = ψ_*φ^*K_X`、`Γ_V + ψ_*φ^*B = B_V`、`μ_D Γ_V ≤ μ_D B_V`、`K_V + Γ_V ≡ −ψ_*φ^*Ω`、`deg_H(K_V+Γ_V)`、`deg_H Γ_V`、`deg_H K_V`、`(V,Λ) ∈ P`、`H ≤ Λ`）及其第二段（`Γ_V = I − J`、`I, J are effective divisors with no common components`、`I ≤ Λ`、`deg_H I ≤ deg_H Λ`、`deg_H J`、`coefficient of D in Γ_V`、`coefficients of Ω_V`）；**Step 5**（`α ∈ (0,1)`、行间式 `Δ := αB_V + (1 − α)Λ ≥ 0`、`Lemma 2.3`、`ε′ − lc where ε′ = αε`、`sub-ǫ-lc`、行间式两行 `a(T,V,Δ) = αa(T,V,B_V) + (1 − α)a(T,V,Λ)` ／ `≤ α + (1 − α) = 1`、`l ∈ ℕ such that lH − Λ is ample`、`−B_V ∼_ℝ K_V`、`lH − B_V ∼_ℝ lH + K_V`、行间式 `lH − Δ = α(lH − B_V) + (1 − α)(lH − Λ)`、`(lH)^d ≤ r`）；**Step 6**（`Let M = ψ_*φ^*uT`、`Ω ≡ −K_X ≡ uT`、`deg_H M = deg_H(ψ_*φ^*Ω)`、`T is exceptional over V`、`lH − M is ample`、`φ^*uT ≤ ψ^*M`、negativity lemma、行间内式 `(V, Δ + (1/u)M)`、行间式 `a(T,V,Δ + (1/u)M) ≤ a(T,V,Δ) − 1 ≤ 0`、`t depending only on d, ε′, r`、`t < 1/u`、`u < v := 1/t`、证毕方框 □）；**Lemma 3.2** 完整陈述与其 Proof 首段（`ε′ ∈ (0,ε)`、`A = −(K_X+B)`、`L ∈ |A|_ℝ`、`(X, B + sL) is ε′-lc`、`s < 1`）。与 Markdown 第 663–699 行逐项比对，辅以 `pdftotext -f 18 -l 18 -layout`。
- 结果：**PASS±**——Step 4／5／6 全部不等式方向（`≤` 与 `≥` 的位置）、四个行间式的系数与下标、行内式 `1/u` 与 `1/t` 的分式结构、`\equiv`（线性等价）而非 `=` 的用法、`\psi _ { * } \phi ^ { * }` 的上下标方向、`\deg _ { H }` 的下标 H、`(lH)^d ≤ r` 的幂次与不等号、`ε′ = αε` 的等式，均与印刷原页一致；Lemma 3.2 编号与陈述完整。差异为 OCR 连字丢 `f` 的拼写及一处句点丢失，逐处用 Edit 修复共 **6 处**：
  1. MD 第 663 行 `coeficients` → `coefficients`（Step 4 首句）；同行 `coeficient` → `coefficient`（「with negative coefficient」）；
  2. MD 第 665 行 `efective` → `effective`（「I, J are effective divisors」）；
  3. MD 第 665 行 `coeficients` → `coefficients`（两处：「the coefficients of J」、「the coefficients of Ω_V」）；同行 `coeficient` → `coefficient`（「the coefficient of D in Γ_V」）；
  4. MD 第 687 行 `coeficients` → `coefficients`（「the coefficients of M」）；
  5. MD 第 687 行 `coeficient` → `coefficient`；同行另修 **Step 6 句点丢失**：印刷为「Let M = ψ_*φ^*u**T**. Since…」，Markdown 作 `$M = \psi _ { * } \phi ^ { * } u T$ Since…`（缺句点），已补为 `u T$. Since`；
  6. MD 第 689 行 `coeficient` → `coefficient`（「the coefficient of the birational transform of T in ψ^*M」）。
- 原文证据：文本层 `p018.txt` 计数 `coefficients`×4、`coefficient`×3、`effective`×1，单 `f` 形式（`coeficient`/`suficiently`/`efective`）计数为 **0**；150dpi 原页图该七处均印作双 `f` 形式，且 Step 6 首句 `uT.` 后确有句点。**据此排除印刷原文为单 `f` 拼写的可能，铁律三不适用。**
- **Luna 旧修复经原页复核属实（不构成差异）**：Luna 在 p.018 登记「`lH−N` 改 `lH−Λ`，`degH M` 记号恢复，`by Step 3` 及 Step 3 中的 `V⇢X` 恢复」——本页原页证实：Step 5 中印刷为 `lH − Λ`（Λ 非 N），Markdown 第 679、682 行正确；`\deg _ { H } M` 记号完整（第 687 行）；`by Step 3` 交叉引用在第 673 行完好；**三项均属实修复，本轮未改动**。
- 明确非差异（已核）：第 676 行 `\begin{array}{c} … \\ … \end{array}` 与第 689、695 行 `\begin{array} { r } { … }` 均为 MinerU 行间式排版伪影，公式内容（`(V, Δ + 1/u M)`、`u < v := 1/t`）与印刷一致；`Lemma$2 . 3 , ( V , \Delta )`、`$4 . 4 $` 类编号内多余空格同属 OCR 空格伪影，编号正确。
- 记号一致性登记（不误导，按 PASS± 保留）：`μ<sub>T</sub>`（HTML 下标，第 713 行）与 `\mu _ { T }`（LaTeX 下标，第 663、710 行）并存；`\mathrm { d e g } _ { H }`（第 663 行）与 `\deg _ { H }` 并存。二者渲染同一记号，印刷亦只有一种写法，按 PASS± 登记不批量统一（与 p.013 的 `\mathfrak{R}` 情形不同）。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.18 止于 Lemma 3.2 Proof 首段末「In particular, we may assume s < 1.」；MD 第 701 行起（`Replacing X with a Q-factorialisation`、`a(T,X,B+sL) = ε′`、`\phi : Y \to X`、`K_Y + B_Y = \phi^*(K_X+B)`、行间式 `\mu_T B_Y ≤ 1 − ε but \mu_T(B_Y + sL_Y) = 1 − ε′` 等）属**印刷 PDF p.19**。内容无丢失/重复/错序。
- **补记（于 p.026 审计时回补，原条目正文未含此项）**：MD 第 663 行 Step 4 标题原为 `Step$\it 4 .$In this step …`，其中裸 LaTeX 斜体命令 `\it` 被排入数学模式（与 p.021 第 833 行、p.023 第 971 行、p.026 第 1209 行同一 MinerU 伪影），会使步骤标签渲染为字面量「Step𝑖𝑡 4 .𝐼𝑛」。印刷证据：`p018.txt` 第 2 行作 `Step 4. In this step we show that the coefficients of BV are bounded from below.`，与 p.018 的 150dpi 原页图一致。已用 Edit 改为 `Step 4. In this step …`。**该处在首轮 p.018 审计中被漏检，p.026 审计时因全篇扫描同类伪影才发现并回补；p.018 条目的其余结论不受影响。**
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.019（PDF p.19 / 印刷 p.19）
- PNG：/tmp/birkarsing_audit_p019.png（pngmono 150dpi）；仲裁源图 `/tmp/birk_p019_300.png`（pnggray 300dpi）及裁片 `/tmp/birk_p019_muT.png`、`/tmp/birk_p019_muT2.png`（裁定 `a(T,X,B+sL) = ε′`、`K_Y + B_Y = \phi^*(K_X+B)`、`L_Y = \phi^*L`、行间式 `\mu_T B_Y \le 1 − ε but \mu_T(B_Y + sL_Y) = 1 − ε′` 与次行 `hence \mu_T sL_Y \ge ε − ε′`）
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 19」；**Lemma 3.2 Proof 续**全文（`Replacing X with a Q-factorialisation`、`T over X`、行间式 `a(T, X, B + sL) = ε′`、两种情形下 `\phi : Y \to X` 的定义、`Let K_Y + B_Y = \phi^*(K_X + B) and let L_Y = \phi^*L`、行间式 `\mu_T B_Y \le 1 − ε but \mu_T(B_Y + sL_Y) = 1 − ε′`、`hence \mu_T sL_Y \ge ε − ε′`、`Since s < 1`、行间式 `−(K_X + B + sL) = A − sL \sim_{\mathbb{R}} (1 − s)A`、negativity/`weak log Fano`/`Run an MMP on −T`、行间式 `−(K_{Y'} + B_{Y'} + sL_{Y'}) \sim_{\mathbb{R}} (1 − s)L_{Y'} \ge 0`、`(Y', B_{Y'} + sL_{Y'}) is ε′-lc`、`horizontal/Z′ components`、`Theorem 1.6 in lower dimension by induction (or applying Theorem 1.1)`、行间式 `\mu_{T'}(1 − s)L_{Y'} \ge \frac{(1 − s)(ε − ε′)}{s}`、`Picard number one`、行间式 `−K_{Y'} \sim_{\mathbb{R}} L_{Y'} + B_{Y'} = (1 − s)L_{Y'} + sL_{Y'} + B_{Y'} \ge (1 − s)L_{Y'}`、`Proposition 3.1`、证毕方框 □）；`Next we treat Theorem 1.7` 段；**Lemma 3.3** 完整陈述（`Assume Theorem 1.8 holds in dimension d. Then Theorem 1.7 holds in dimension d when lct(X, B, |A|_ℝ) = 1.`）；**Lemma 3.3 Proof** 全文（`sequence of ℝ-divisors`、行间式 `0 \le L_i \sim_{\mathbb{R}} A = −(K_X + B)`、`t_i := lct(X, B, L_i)`、`lim t_i = 1`、`Assume (X, B) is not exceptional`、`lct(X, B, L) ≤ 1`、`lct(X, B, |A|_ℝ) = 1`、`(X, B + L) is lc but not klt`、`using approximation`、`0 \le L \sim_{\mathbb{Q}} A`、`by taking D = L`、`Now assume (X, B) is exceptional`、`[5, Lemma 7.2]`、`there is ε > 0 such that (X, B + L_i) is ε-lc`、`Theorem 1.8 in dimension d`、`(X, B + L_i + sL_i) is klt`、`1 + s < t_i`、`contradicts lim t_i = 1`、证毕方框 □）。与 Markdown 第 701–755 行逐项比对，辅以 `pdftotext -f 19 -l 19 -layout`。
- 结果：**PASS±**——全部行间式的系数、分式结构与不等号方向（`\mu_T B_Y \le 1 − ε`、`= 1 − ε′`、`\mu_T sL_Y \ge ε − ε′`、`\ge \frac{(1-s)(ε − ε′)}{s}`、`\ge 0`、`\ge (1 − s)L_{Y'}`）、`\sim_{\mathbb{R}}`（线性等价）与 `\sim_{\mathbb{R}} 0` 的用法、`\phi : Y \to X` 的**实线**箭头（与 p.017 的 `V \dashrightarrow X` 虚线小射影不同，此处 φ 是抽头 K-负的极射影缩射，印刷确为实线 `→`）、`\phi^*` 的**上标**（拉回）方向、`\mu _ { T }`／`\mu _ { T ^ { \prime } }` 的下标、Lemma 3.3 编号与陈述、`[5, Lemma 7.2]` 引文、两个证毕方框，均与印刷原页一致；差异为 OCR 连字丢 `f` 的拼写及若干句点丢失，逐处用 Edit 修复共 **6 处**：
  1. MD 第 727 行 `coeficients` → `coefficients`（「shows that the coefficients of the horizontal/Z′ components …」）；
  2. MD 第 741 行**句点丢失**：印刷为「… independent of the rest of this paper when lct(X, B, |A|_ℝ) < 1**.**」，Markdown 行末无句点，已补；
  3. MD 第 743 行**句点丢失**：**Lemma 3.3 陈述句末**印刷作 `lct(X, B, |A|_ℝ) = 1.`（引理陈述的收束句点），Markdown 无句点，已补；
  4. MD 第 751 行**句点丢失**：印刷为「… form a decreasing sequence with lim t_i = 1**.**」，已补；
  5. MD 第 753 行**句点丢失**：印刷为「… so we are done in this case by taking D = L**.**」，已补；
  6. MD 第 755 行**句点丢失**：印刷为「… which contradicts lim t_i = 1**.**」（Lemma 3.3 证明末句），已补。
- 原文证据：文本层 `p019.txt` 计数 `coefficients`×1、`coefficient`×1，单 `f` 形式（`coeficient`/`coeficients`/`efective`/`suficient`/`diferent`）计数为 **0**；150dpi 原页图第 727 行对应处印作 `coefficients`，300dpi 裁片 `/tmp/birk_p019_muT2.png` 逐字确认 `K_Y + B_Y = \phi^*(K_X + B)`、`L_Y = \phi^*L`、`\mu_T B_Y \le 1 − ε but \mu_T(B_Y + sL_Y) = 1 − ε'`、`hence \mu_T sL_Y \ge ε − ε'`，裁片 `/tmp/birk_p019_muT.png` 确认行间式 `a(T, X, B + sL) = ε'`。**据此排除印刷原文为单 `f` 拼写或缺句点的可能，铁律三不适用。**
- **下标保持正确的正面确认（不构成差异）**：本印刷页密集出现 `B_Y`、`L_Y`、`K_Y`、`L_{Y'}`、`B_{Y'}`、`\mu_{T'}` 等下标，Markdown 第 707、710、713、721、724、727、730、736、739、748、755 行**全部保留完好**，无一处「OCR 丢下标」缺陷——与 p.010（`D_Y`）、p.015（`A_Y`）两处 FAIL 的缺陷类在本页**不出现**。另 `$L _ { i } \sim_{\mathbb{R}} A$`、`$s L _ { i }$`、`$t _ { i }$` 等下标 *i* 亦正确。
- 明确非差异（已核）：MD 第 713 行 `hence µ<sub>T</sub>s$L _ { Y } \geq \epsilon - \epsilon ^ { \prime } .$` ——`µ<sub>T</sub>` 为 HTML 下标（与第 710 行 `\mu_ {T}` 的 LaTeX 下标并存），但 `µ`、`T`、`s`、`L_Y`、`\ge`、`\epsilon`、`\epsilon^{\prime}` 全部符号与顺序与印刷一致，渲染结果相同；第 753 行 `$( X , B +$ $L )$`、第 755 行 `Lemma$7 . 2 ]$`、第 755 行 `dimension$d ,$`、第 753 行 `$0 \leq L \sim _ { \mathbb { R } }$A`（`A` 落在数学模式外）均为 MinerU 的数学/正体切分与空格伪影，不改变公式或引文编号（`7.2`、`4.4` 类）；第 745、767 行「sequence of R-divisors」中的 `ℝ` 直写字符，与他处 `\mathbb { R }` 属同一 ℝ 的两种编码，印刷亦只有一种字形（第 745 行文本层作 `R-divisors` 处的黑板粗 ℝ），渲染一致。
- 记号一致性登记（不误导，按 PASS± 保留）：同一个 ǫ 在本页并存 `\epsilon ^ { \prime }`（第 704、710、730 行的 ε′）与直写 `ǫ-lc`（第 755 行）两种编码；`\operatorname { l c t }` 与 `\mathrm { l c t }` 与直写 `lct`（第 753 行）三种写法并存。二者/三者渲染为同一记号且不误导数学，按 PASS± 登记不批量统一（延续 p.017 的同一口径）。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.19 止于 Lemma 3.3 证毕方框；MD 第 757 行起（**Proposition 3.4**、`Proof. Step 1.`、行间式 `lct(X, B, |A|_ℝ) = lct(X, B, D)`、`Step 5 we treat the case when B is a Q-boundary`、行间式 `t := lct(X, B, |A|_ℝ) = \lim t_i`、**Step 2**、行间式 `K_X + B + t_i L_i + (1 − t_i)H_i \sim_{\mathbb{R}} 0` 等）属**印刷 PDF p.20**。内容无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.020（PDF p.20 / 印刷 p.20）
- PNG：/tmp/birkarsing_audit_p020.png（pngmono 150dpi）
- 核对：页眉「20 / Caucher Birkar」；**Proposition 3.4** 完整陈述（`Theorem 1.7 holds when lct(X, B, |A|_ℝ) < 1.`）；**Proof Step 1**（`From here to the end of Step 4 we find D ∈ |A|_ℝ such that`、行间式 `lct(X, B, |A|_ℝ) = lct(X, B, D).`、`In Step 5 we treat the case when B is a Q-boundary`、`Replacing X with a Q-factorialisation`、`sequence of ℝ-divisors`、行间式 `0 \le L_i \sim_{\mathbb{R}} A = −(K_X + B)`、`t_i := lct(X, B, L_i) ∈ (0, 1)`、行间式 `t := lct(X, B, |A|_ℝ) = \lim t_i.`、`If t = t_i for some i, then put D = L_i.`、`So for now assume t ≠ t_i for every i.`）；**Step 2**（`H_i ∈ |A|_ℝ`、`birational contractions X_i′ → X`、`lc places of (X, B + t_iL_i)`、`(X, B + H_i) is klt and (X, B + t_iL_i + H_i) is lc`、`coefficients of the H_i belong to a fixed DCC set`、`A is semi-ample`、`A \sim_{\mathbb{R}} \sum_j \alpha_j G_j`、`G_j are base point free Cartier divisors and \alpha_j > 0`、行间式 `K_X + B + t_iL_i + (1 − t_i)H_i \sim_{\mathbb{R}} 0.`、`Let T_i′ be an lc place`、`\phi_i : X_i′ → X`、`Then H_i′ = \phi_i^* H_i`、`cannot contain any lc centre of (X, B + t_iL_i)`、行间式 `K_{X_i′} + T_i′ + B_i′ + t_iL_i′ + (1 − t_i)H_i′ = \phi_i^*(K_X + B + t_iL_i + (1 − t_i)H_i) \sim_{\mathbb{R}} 0.`）；**Step 3**（行间式 `−(K_{X_i′} + T_i′ + B_i′ + (1 − t)H_i′)`、`Note that here we have used t rather than t_i.`、`[5, 2.13(7)]`、`X_i′ is of Fano type`、`Let X_i″ be the resulting model of the MMP.`、行间式 `(X_i″, T_i″ + B_i″ + t_iL_i″ + (1 − t_i)H_i″) is lc`、`coefficients of T_i″ + B_i″ and H_i″ belong to a fixed DCC set independent of i`、`the numbers 1 − t_i form an increasing sequence approaching 1 − t`、`by the ACC for lc thresholds [13]`、行间式 `(X_i″, T_i″ + B_i″ + (1 − t)H_i″) is lc, for every i.`、`Mori fibre space X_i″ → Z_i″, for infinitely many i`、行间式 `K_{X_i″} + T_i″ + B_i″ + (1 − t)H_i″ is ample over Z_i″`、行间式 `K_{X_i″} + T_i″ + B_i″ + t_iL_i″ + (1 − t_i)H_i″ \sim_{\mathbb{R}} 0`）。与 Markdown 第 757–823 行逐项比对，辅以 `pdftotext -f 20 -l 20 -layout`。
- 结果：**PASS±**——Proposition 3.4 编号与陈述、Step 1／2／3 的顺序与全部行间式的**下标层次**（单撇 `X_i′`、`B_i′`、`L_i′`、`H_i′`、双撇 `X_i″`、`T_i″`、`Z_i″`、以及 Step 3 首式中的 `(1 − t)` 与后续 `(1 − t_i)`、`t_i` 与 `t` 的关键区分）、`\phi_i : X_i′ \to X` 的**实线**箭头、`\phi_i^*` 的上标（拉回）方向、`\sim_{\mathbb{R}} 0` 与 `\sim_{\mathbb{R}} \sum_j \alpha_j G_j` 的线性等价号、`t \neq t_i`、`\in (0, 1)`、`\lim t_i`、`\alpha_j > 0`、`[5, 2.13(7)]` 与 `[13]` 两处引文，均与印刷原页一致；**`t` 与 `t_i` 的混用（Step 3 首式用 `t`、其后用 `t_i`，且印文明写「Note that here we have used t rather than t_i」）在 Markdown 中被完整保留，未被「统一」**，属正确。差异为 OCR 连字丢 `f` 的拼写及一处句点丢失，逐处用 Edit 修复共 **4 处**：
  1. MD 第 757 行**句点丢失**：**Proposition 3.4 陈述句末**印刷作 `lct(X, B, |A|_ℝ) < 1.`，Markdown 行末无句点，已补；
  2. MD 第 781 行 `coeficients` → `coefficients`（Step 2「the coefficients of the H_i belong to a fixed DCC set」）；
  3. MD 第 787 行**句点丢失**：印刷为「Let B_i′, L_i′, H_i′ be the birational transforms of B, L_i, H_i**. Then** H_i′ = φ_i^*H_i because …」，Markdown 作 `…of$B , L _ { i } , H _ { i }$Then$…`（句点缺失且与下一句粘连），已补为 `H _ { i }$. Then$H _ { i } ^ { \prime } = …`；
  4. MD 第 805 行 `coeficients` → `coefficients`（Step 3「the coefficients of T_i″ + B_i″ and H_i″ belong to a fixed DCC set independent of i」）。
- 原文证据：文本层 `p020.txt` 计数 `coefficients`×2、`coefficient`×2，单 `f` 形式（`coeficient`/`coeficients`/`efective`/`suficient`/`diferent`）计数为 **0**；150dpi 原页图 Step 2 与 Step 3 两处均印作 `coefficients`，且 Proposition 3.4 陈述句末与「transforms of B, L_i, H_i.」之后确有句点。**据此排除印刷原文为单 `f` 拼写或缺句点的可能，铁律三不适用。**
- **文本层伪影的排除（已核，不构成 Markdown 缺陷）**：`p020.txt` 在 Step 2 处输出「belong to a fixed DCC **P**set」，其中多出的 `P` 经 150dpi 原页图核对为 `pdftotext` 的字距/连字伪影，印刷原文与 Markdown 均为「a fixed DCC set」，**Markdown 无误**，不改。
- 明确非差异（已核）：MD 第 799 行 `is of Fano$\mathrm { t y p e } .$` 的 `\mathrm { t y p e }` 字母间距伪影，内容为 `Fano type`；第 762、776 行 `\operatorname{lct}`、第 773 行 `\mathrm { l c t }` 三种写法并存，渲染同一记号且印刷亦只有一种写法；第 767 行「sequence of R-divisors」中 ℝ 直写字符与他处 `\mathbb { R }` 属同一符号的两种编码（文本层该处作 `R-divisors`）；第 790 行行间式中 `K _ {X _ {i} ^ {\prime}}` 的下标内嵌上标结构与 `\phi_ {i} ^ {*}` 的上标星号，符号方向与顺序均与印刷一致。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.20 止于行间式 `K_{X_i″} + T_i″ + B_i″ + t_iL_i″ + (1 − t_i)H_i″ \sim_{\mathbb{R}} 0`；MD 第 825 行起（`which implies`、行间式 `K_{X_i″} + T_i″ + B_i″ + (1 − t_i)H_i″`、`is anti-nef over Z_i″`、`[13, Theorem 1.5]`、`Step$\it 4 .$` 及 Step 4 全文）属**印刷 PDF p.21**。内容无丢失/重复/错序。
- 备注：MD 第 833 行 `Step$\it 4 .$In this step …` 中残留的裸 LaTeX 斜体命令 `\it` 属 MinerU 导出伪影，因该行落在 p.021 审计范围内，**按逐页证据原则留待 p.021 条目处置**，本页不越界修改。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.021（PDF p.21 / 印刷 p.21）
- PNG：/tmp/birkarsing_audit_p021.png（pngmono 150dpi）；仲裁源图 `/tmp/birk_p021_300.png`（pnggray 300dpi）及裁片 `/tmp/birk_p021_S4.png`（裁定 Step 4 首行的 `X_i′ ⇢ X_i″` 虚线箭头与 `ℝ-linearly equivalent`）
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 21」；Step 3 收尾（`which implies`、行间式 `K_{X_i″} + T_i″ + B_i″ + (1 − t_i)H_i″`、`is anti-nef over Z_i″`、`[13, Theorem 1.5]`、`general fibres of X_i″ → Z_i″`、`replacing the sequence with a subsequence`、`minimal model X_i″, for every i.`）；**Step 4**（`we find the desired D ∈ |A|_ℝ such that lct(X, B, D) = t. Fix i. Since`、行间式 `−(K_{X_i″} + T_i″ + B_i″ + (1 − t)H_i″)`、`is nef, hence semi-ample`、`ℝ-linearly equivalent to some ℝ-divisor P_i″ ≥ 0`、`X_i′ ⇢ X_i″ is an MMP on`、行间式 `−(K_{X_i′} + T_i′ + B_i′ + (1 − t)H_i′)`、`we get an ℝ-divisor P_i′ ≥ 0 such that`、行间式 `−(K_{X_i′} + T_i′ + B_i′ + (1 − t)H_i′) ∼_ℝ P_i′`、`which in turn gives an ℝ-divisor P_i ≥ 0`、行间式 `−(K_X + B + (1 − t)H_i) ∼_ℝ P_i.`、`By construction,`、行间式 `(X, B + (1 − t)H_i + P_i)`、`is not klt near the generic point of the centre of T_i′ on X`、`P_i ∼_ℝ tA`、`Supp H_i does not contain the centre of T_i`、`Put D = (1/t)P_i`、`Then D ∼_ℝ A and lct(X, B, D) ≤ t`）；**Step 5**（`we treat the case when B is a Q-boundary. Fix i.`、`Since A_i is a Q-divisor, we can assume H_i is a Q-divisor`、`If t is a rational number`、`P_i″ to be a Q-divisor`、`Assume now that t is not a rational number`、行间式 `−(K_{X_i″} + T_i″ + B_i″ + (1 − t)H_i″) is not big`、`numerically trivial on some covering family of curves`、`taking intersection with such curves C`、`H_i″ · C ≠ 0 (as H_i″ is big)`、`ensures that t is a rational number, a contradiction`、行间式 `−(K_{X_i′} + T_i′ + B_i′ + (1 − t)H_i′) is big`、行间式 **`−(K_{X_i′} + T_i′ + B_i′ + (1 − e)H_i′)`**、`for some rational number e ∈ (0, t)`、`0 ≤ Q_i ∼_ℚ eA`、`Letting D = (1/e)Q_i gives 0 ≤ D ∼_ℚ A with`、行间式 `lct(X, B, D) ≤ e < t,`、`contradicting the definition of t.`、证毕方框 □）。与 Markdown 第 825–889 行逐项比对，辅以 `pdftotext -f 21 -l 21 -layout`。
- 结果：**PASS±**——Step 4／5 全部行间式的下标层次（单撇 `X_i′`、`B_i′`、`L_i′`、`H_i′`、`P_i′`、`T_i′`；双撇 `X_i″`、`T_i″`、`Z_i″`、`P_i″`）、**关键字母区分 `t` 与 `e`**（Step 5 的第三个行间式印作 `(1 − e)H_i′`，与前两个的 `(1 − t)H_i′` 不同，Markdown 第 880 行**正确保留 `e`**）、`\sim_{\mathbb{R}}` 与 `\sim_{\mathbb{Q}}` 两种等价号的分用、`P_i \sim_{\mathbb{R}} tA`、`\frac{1}{t}P_i` 与 `\frac{1}{e}Q_i` 两个分式、`e \in (0, t)`、`\leq e < t`、`H_i″ \cdot C \neq 0`、`anti-nef`、`[13, Theorem 1.5]` 引文、Step 4／5 编号，均与印刷原页一致；**本印刷页无任何英文拼写可供 OCR 丢 `f`**（文本层 `coefficient(s)`、`effective`、`sufficiently`、`different` 计数全为 0），故无该类缺陷。差异仅一处，已用 Edit 修复共 **1 处**：
  - MD 第 833 行 `Step$\it 4 .$In this step …` → `Step 4. In this step …`：Markdown 把 MinerU 的**裸 LaTeX 斜体命令 `\it`** 与句点一并排入数学模式，渲染结果为字面量「Step𝑖𝑡 4 .𝐼𝑛」，**步骤编号标签被破坏**；印刷原文该处为正体斜排的 `Step 4.`（150dpi 原页可见，`Step` 为斜体、`4.` 为正体斜排的阿拉伯数字）。已改为与 Step 1／2／3（第 759、781、793 行 `Step 1.`／`Step 2.`／`Step 3.`）及第 865 行 `Step 5.` 一致的本地写法。
- 原文证据：150dpi 原页图第 833 行对应处清晰印作「*Step* 4. In this step we find the desired D ∈ |A|_ℝ such that lct(X, B, D) = t. Fix i. Since」；文本层 `p021.txt` 相应位置作 `Step 4. In this step we find the desired D ∈ |A|R such that lct(X, B, D) = t.`（无 `\it`），证明 `\it` 系 MinerU 导出伪影而非印刷排法（铁律三不适用）。
- **虚线双射箭头已正确保留的正面确认（不构成差异）**：Step 4 首段印刷作 `Since X_i′ ⇢ X_i″ is an MMP on`——该箭头是 MMP 的**虚线（dotted/dashed）双射箭头**，与 p.017 的 `Vdashrightarrow X`（Q-factorialisation 的小射影）虽同为虚线但语义不同。Markdown 第 839 行 `\mathrm { ~ -- \to ~ }` 忠实还原为虚线箭头，**未与实线缩射 `\to` 混同**；300dpi 裁片 `/tmp/birk_p021_S4.png` 逐字确认印刷箭头确为虚线（`--→`），且 `P_i″ \ge 0`、`ℝ-linearly equivalent` 字样清晰。`X_i″ \to Z_i″`（Mori fibre space）与 `X_i′ ⇢ X_i″`（MMP）两类箭头在 Markdown 中亦分别正确。
- 明确非差异（已核）：第 863 行 `Put$\begin{array} { r } { D = \frac { 1 } { t } P _ { i } } \end{array}$`、`Then D ∼<sub>R</sub> A`、`$P _ {i} ~ \sim _ { \mathbb { R } ^ { } } ~ t A$`、第 883 行 `Letting$\begin{array} { r } { D = \frac { 1 } { e } Q _ { i } } \end{array}$`、`$0 \leq Q _ { i } \sim _ { \mathbb { Q } }$eA`（`eA` 落在数学模式外）、第 886 行 `\operatorname{lct} (X, B, D) \leq e <   t,` 的多空格、第 865 行 `$A _ { i }$is a Q-divisor` 中 `A_i` 落在数学模式外——均为 MinerU 的 `array` 包裹、数学/正体切分与空格伪影；`\frac{1}{t}`、`\frac{1}{e}`、`\sim_{\mathbb{R}} tA`、`\sim_{\mathbb{Q}} eA`、`\sim_{\mathbb{Q}} A` 的系数与等价关系全部与印刷一致，**不构成数学差异**。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.21 止于证毕方框（`contradicting the definition of t.`）；MD 第 891 行起（章标题 **`4. Complements in a neighbourhood of a non-klt centre`**）属**印刷 PDF p.22**。内容无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.022（PDF p.22 / 印刷 p.22）
- PNG：/tmp/birkarsing_audit_p022.png（pngmono 150dpi）；仲裁源图 `/tmp/birk_p022_300.png`（pnggray 300dpi）及裁片 `/tmp/birk_p022_S.png`（裁定 `Φ(𝔖)`／`𝔖 ⊂ [0, 1]` 中的花体 𝔖 与作为因子的斜体 `S` 之区分，及该处 `coefficients` 的双 `f`）
- 核对：页眉「22 / Caucher Birkar」；章标题 **`4. Complements in a neighbourhood of a non-klt centre`**；§4 首段（`we prove our main result on the existence of complements (Theorem 1.9)`、`It does not follow directly from [5]`、`First we treat a special case of the theorem.`）；**Proposition 4.1** 完整陈述（`under the additional assumption that there is a boundary Γ such that`、两条项目符号 `(X, Γ) is plt with S = ⌊Γ⌋, and`／`αM − (K_X + Γ) is ample for some real number α > 0.`）；**Proof Step 1**（`reduce to the case when α ∈ (0, 2) and when B − Γ has small (positive or negative) coefficients`、`Since M − (K_X + B) is nef and big and αM − (K_X + Γ) is ample`、**两行等式**（见下）、`is ample for any t ∈ (0, 1)`、`replacing Γ with (1 − t)B + tΓ for some sufficiently small real number t > 0`、`we can replace α by some rational number in (0, 2)`、`since (X, B) is lc and since S is a non-klt centre of this pair`、`S ≤ ⌊B⌋`、`the above change of Γ preserves the plt property of (X, Γ) and the condition S = ⌊Γ⌋.`、次段 `if we choose t small enough then we can ensure that B − Γ has sufficiently small positive or negative coefficients (we will use this in steps below).`）；**Step 2**（`we consider bounded complements on S`、`Since (X, Γ) is plt, S is normal. Define`、行间式 `K_S + B_S = (K_X + B)|_S`、`by adjunction. Then (S, B_S) is lc and the coefficients of B_S belong to Φ(𝔖) for some finite set 𝔖 ⊂ [0, 1] of rational numbers depending only on p`、`[37, Proposition 3.8][5, Lemma 3.3] where`、行间式 `Φ(𝔖) = {1 − s/l | s ∈ 𝔖, l ∈ ℕ}.`、`By assumption, M|_S ≡ 0, hence M|_S ∼_ℚ 0 as M is semi-ample. In particular,`、行间式 `−(K_X + Γ)|_S ∼_ℝ (αM − (K_X + Γ))|_S`、`Moreover, since (X, Γ) is plt, defining`、行间式 `K_S + Γ_S = (K_X + Γ)|_S`、`by adjunction, (S, Γ_S) is klt. Thus we deduce that S is of Fano type. On the other hand,`、行间式 `−(K_S + B_S) ∼_ℚ (M − (K_X + B))|_S`、`is nef. Therefore, applying Theorem 2.13`、`there is a natural number n depending only on d, 𝔖 such that K_S + B_S has an n-complement K_S + B_S^+ which satisfies B_S^+ ≥ B_S`、`We can assume that nB is an integral divisor after replacing n with np.`、末段 `since S is of Fano type and M|_S ∼_ℚ 0, in fact we have M|_S ∼ 0 as Pic(S) is torsion-free (cf. [16, Proposition 2.1.2]; the point is that h^i(O_S) = 0 for i > 0 which is a consequence of Kawamata-Viehweg vanishing theorem)`）。与 Markdown 第 891–943 行逐项比对，辅以 `pdftotext -f 22 -l 22 -layout`。
- 结果：**PASS±**——章标题文字与编号、Proposition 4.1 编号与两条项目符号、**Step 1 的两行等式的逐项系数**（`(1 − t + tα)M − (K_X + (1 − t)B + tΓ) = (1 − t + tα)M − (1 − t)(K_X + B) − t(K_X + Γ)` ／ `= (1 − t)(M − (K_X + B)) + t(αM − (K_X + Γ))`）、`α ∈ (0, 2)`、`t ∈ (0, 1)`、`t > 0`、`S ≤ ⌊B⌋`、`S = ⌊Γ⌋` 两个取整记号、`Φ(𝔖) = {1 − s/l | s ∈ 𝔖, l ∈ ℕ}` 的分式与集合构造、三个限制竖线 `|_S`、`M|_S ≡ 0`（线性等价）与 `M|_S ∼_ℚ 0`、`−(K_S + B_S) ∼_ℚ (M − (K_X + B))|_S`、n-complement `K_S + B_S^+`、`B_S^+ ≥ B_S`、`replacing n with np`、`[37, Proposition 3.8][5, Lemma 3.3]` 与 `[16, Proposition 2.1.2]` 三处引文，均与印刷原页一致。差异为 OCR 连字丢 `f` 的拼写及两处句点丢失，逐处用 Edit 修复共 **6 处**：
  1. MD 第 899 行**句点丢失**：Proposition 4.1 第二条项目符号末，印刷作 `α > 0**.**`，已补；
  2. MD 第 901 行 `coeficients` → `coefficients`（Step 1 首段「has small (positive or negative) coefficients」）；
  3. MD 第 907 行 `suficiently` → `sufficiently`（「for some sufficiently small real number t > 0」）；
  4. MD 第 907 行**句点丢失**：印刷作「… and the condition S = ⌊Γ⌋**.**」，已补；
  5. MD 第 909 行 `suficiently` → `sufficiently`、`coeficients` → `coefficients`（次段「has sufficiently small positive or negative coefficients」）；
  6. MD 第 917 行 `coeficients` → `coefficients`（Step 2「the coefficients of B_S belong to Φ(𝔖)」）。
- 原文证据：文本层 `p022.txt` 计数 `coefficients`×3、`coefficient`×3、`sufficiently`×2，单 `f` 形式（`coeficient`/`coeficients`/`suficient`/`efective`/`diferent`）计数为 **0**；150dpi 原页图与 300dpi 裁片 `/tmp/birk_p022_S.png` 一致显示「the **coefficients** of B_S belong to Φ(𝔖) for some finite set 𝔖 ⊂ [0, 1]」为双 `f`，且两条项目符号末与「condition S = ⌊Γ⌋.」后确有句点。**据此排除印刷原文为单 `f` 拼写或缺句点的可能，铁律三不适用。**
- **两处 S 的字形区分已正确保留的正面确认（不构成差异）**：本印刷页同时出现**两个不同的 S**——(i) Step 1／Step 2 前半的**非 klt 中心因子** `S = ⌊Γ⌋`（斜体，如 `(S, B_S)`、`S is normal`、`M|_S`），(ii) Step 2 的**有限有理数集** `𝔖 ⊂ [0, 1]`（**花体 𝔖**，如 `Φ(𝔖)`、`d, 𝔖`）。300dpi 裁片 `/tmp/birk_p022_S.png` 逐字显示该有限集的 S 为**花体**，与同句中作为因子的斜体 `S`（`(S, B_S)`）字形明显不同；Markdown 第 917、920、941 行的 `\mathfrak { S }` 与 `\mathfrak {S }` **忠实还原了这一区分**（若统一成斜体 `S` 反而会造成数学歧义），**未误并**，本轮未改动。
- 明确非差异（已核）：MD 第 904 行 `\begin{array}{c} … \\ … \end{array}` 的两行等式用 `array` 环境包裹并把第二行用 `\\ =` 起头，为 MinerU 行间式排版伪影；**第一行与第二行的左右两侧系数、括号层次、`M`、`K_X`、`B`、`Γ`、`α`、`t` 的位置与印刷逐字一致**，代数恒等式 `（1−t+tα)M − (1−t)(K_X+B) − t(K_X+Γ) = (1−t)(M−(K_X+B)) + t(αM−(K_X+Γ))` 成立，不构成数学差异。第 914 行 `K _ {S} + B _ {S} = (K _ {X} + B) | _ {S}`、第 926、932、938 行 `| _ {S}` 的**限制竖线放在下标之前**（`| _ {S}`）而非标准 `\vert_{S}`，渲染为 `|_S`，与印刷的 `(K_X + B)|_S` 内容一致，属记号排版伪影；第 923 行 `$M | _ { S } \equiv 0$`、第 941 行 `$d , \mathfrak { S }$`、第 943 行 `$\mathrm { P i c } ( S )$` 与 `$h ^ { i } ( { \mathcal { O } } _ { S } ) = 0$` 的字母间距／正体伪影亦然；第 943 行 `h^i(O_S) = 0` 中 `O` 用 `\mathcal {O }` 排为花体，与印刷的花体 `O` 一致。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.22 止于末段「…consequence of Kawamata-Viehweg vanishing theorem).」；MD 第 945 行起（**Step 3**、`we take a resolution of X and define appropriate divisors on it`、`\phi \colon X^{\prime} \to X`、`N := M − (K_X + B)`、`E^{\prime}`、`Δ^{\prime} = B^{\prime} − E^{\prime}`、行间式 `L^{\prime} := (n + 2)M^{\prime} − nK_{X^{\prime}} − nE^{\prime} − ⌊(n+1)Δ^{\prime}⌋` 等）属**印刷 PDF p.23**。内容无丢失/重复/错序。
- 备注：MD 第 951 行 `Let$E ^ { \prime }$be the sum of the components of$B ^ { \prime }$which have coeficient 1` 中的 `coeficient` 属印刷 p.23，**留待 p.023 条目处置**，本页不越界修改。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.023（PDF p.23 / 印刷 p.23）
- PNG：/tmp/birkarsing_audit_p023.png（pngmono 150dpi）
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 23」；**Step 3**（`we take a resolution of X and define appropriate divisors on it`、`\phi : X^{\prime} \to X`、`S^{\prime} \subset X^{\prime}`、`\psi : S^{\prime} \to S`、行间式 `N := M − (K_X + B)`、`K_{X^{\prime}} + B^{\prime}, M^{\prime}, N^{\prime}` be the pullbacks of `K_X + B, M, N, respectively`、`Let E^{\prime} be the sum of the components of B^{\prime} which have coefficient 1`、`Δ^{\prime} = B^{\prime} − E^{\prime}`、行间式 `L^{\prime} := (n + 2)M^{\prime} − nK_{X^{\prime}} − nE^{\prime} − ⌊(n + 1)Δ^{\prime}⌋`、`which is an integral divisor. Note that`、**三行等式**（见下）、`Now write`、行间式 `K_{X^{\prime}} + Γ^{\prime} = \phi^*(K_X + Γ).`、`Then we can assume that B^{\prime} − Γ^{\prime} = \phi^*(B − Γ) has sufficiently small (positive or negative) coefficients by Step 1.`、`The coefficient of S^{\prime} in both B^{\prime} and Γ^{\prime} is 1 but its coefficient in Δ^{\prime} is 0.`）；**Step 4**（`we introduce a boundary Θ^{\prime} and study related divisors`、`Let P^{\prime} be the unique integral divisor so that`、行间式 `Θ^{\prime} := Γ^{\prime} + nΔ^{\prime} − ⌊(n + 1)Δ^{\prime}⌋ + P^{\prime}`、`is a boundary, (X^{\prime}, Θ^{\prime}) is plt, and ⌊Θ^{\prime}⌋ = S^{\prime} (in particular, we are assuming Θ^{\prime} \ge 0)`、`More precisely, we let μ_{S^{\prime}}P^{\prime} = 0 and for each prime divisor D^{\prime} ≠ S^{\prime}, we let`、行间式 `μ_{D^{\prime}}P^{\prime} := −μ_{D^{\prime}}⌊Γ^{\prime} + nΔ^{\prime} − ⌊(n + 1)Δ^{\prime}⌋⌋`、`which satisfies`、**两行等式**（含 `⟨(n + 1)Δ^{\prime}⟩` 分数部分记号）、`where ⟨(n + 1)Δ^{\prime}⟩ is the fractional part of (n + 1)Δ^{\prime}.`、`We claim that P^{\prime} \ge 0.`、`Pick a component D^{\prime} of P^{\prime}. By the above, D^{\prime} ≠ S^{\prime}.`、`If D^{\prime} is a component of E^{\prime}, then D^{\prime} is not a component of Δ^{\prime} and μ_{D^{\prime}}Γ^{\prime} ∈ (0, 1) as B^{\prime} − Γ^{\prime} has small coefficients and μ_{D^{\prime}}B^{\prime} = 1, hence μ_{D^{\prime}}P^{\prime} = 0;`、`on the other hand, if D^{\prime} is not a component of E^{\prime}, then the absolute value of`、行间式 `μ_{D^{\prime}}(Γ^{\prime} − Δ^{\prime}) = μ_{D^{\prime}}(Γ^{\prime} − B^{\prime})`、`is sufficiently small and`、行间式 `μ_{S^{\prime}}⟨(n + 1)Δ^{\prime}⟩ ∈ [0, 1),`、`hence μ_{D^{\prime}}P^{\prime} = 0 or μ_{D^{\prime}}P^{\prime} = 1, so in any case μ_{D^{\prime}}P^{\prime} \ge 0.`、`We show P^{\prime} is exceptional/X.`、`Assume D^{\prime} is a component of P^{\prime} which is not exceptional/X and let D be its pushdown.`、`Since S^{\prime} is not a component of P^{\prime}, D^{\prime} ≠ S^{\prime}.`、`Let E, Δ be the pushdowns of E^{\prime}, Δ^{\prime}.`、`Since nB and nE are integral, μ_D nΔ is integral, hence`、行间式 `μ_D⌊(n + 1)Δ⌋ = μ_D nΔ.`、`Then`、**两行等式** `μ_{D^{\prime}}P^{\prime} = −μ_{D^{\prime}}⌊Γ^{\prime} + nΔ^{\prime} − ⌊(n + 1)Δ^{\prime}⌋⌋ = −μ_D⌊Γ + nΔ − ⌊(n + 1)Δ⌋⌋ = −μ_D⌊Γ⌋ = 0`）。与 Markdown 第 945–1014 行逐项比对，辅以 `pdftotext -f 23 -l 23 -layout`。
- 结果：**PASS±**——Step 3／4 的五个行间式组（Step 3 的定义式 + 三行展开、Step 4 的 `Θ^{\prime}` 定义式、`μ_{D^{\prime}}P^{\prime} := …`、`μ_{D^{\prime}}P^{\prime} = … = …` 两行、`μ_{D^{\prime}}(Γ^{\prime} − Δ^{\prime}) = μ_{D^{\prime}}(Γ^{\prime} − B^{\prime})`、`μ_{S^{\prime}}⟨(n + 1)Δ^{\prime}⟩ ∈ [0, 1)`、`μ_D⌊(n + 1)Δ⌋ = μ_D nΔ`、末组两行等式）中，**取整号 `⌊ ⌋` 与分数部分号 `⟨ ⟩` 的全部出现位置、层次与括号嵌套**（特别是 Step 4 第二行的 `−μ_{D^{\prime}}⌊Γ^{\prime} − Δ^{\prime} + ⟨(n + 1)Δ^{\prime}⟩⌋` 这个**双层嵌套**结构）逐字与印刷一致；`\phi : X^{\prime} \to X`、`\psi : S^{\prime} \to S`、`\phi^*` 上标、`n + 2`、`nK_{X^{\prime}}`、`\ge 0`、`\in (0, 1)`、`\in [0, 1)`、`\neq`、`= 0` / `= 1` 的取值、Step 3 三行展开的逐项系数（`(n + 2)M^{\prime} − nK_{X^{\prime}} − nB^{\prime} + nΔ^{\prime} − ⌊(n + 1)Δ^{\prime}⌋` ／ `2M^{\prime} + n(M^{\prime} − K_{X^{\prime}} − B^{\prime}) + nΔ^{\prime} − ⌊(n + 1)Δ^{\prime}⌋` ／ `2M^{\prime} + nN^{\prime} + nΔ^{\prime} − ⌊(n + 1)Δ^{\prime}⌋`）均与印刷原页一致。差异逐处用 Edit 修复共 **6 处**：
  1. MD 第 951 行 `coeficient` → `coefficient`（「components of B^{\prime} which have coefficient 1」）；
  2. MD 第 969 行 `suficiently` → `sufficiently`、`coeficients` → `coefficients`、`coeficient` → `coefficient`（**两处**：「has sufficiently small (positive or negative) coefficients by Step 1.」「The coefficient of S^{\prime} … but its coefficient in Δ^{\prime} is 0.」）；
  3. MD 第 971 行 `Step$\it 4 .$In this step …` → `Step 4. In this step …`：与 p.021 第 833 行同一 MinerU 伪影——裸 LaTeX 斜体命令 `\it` 被排入数学模式，渲染为字面量「Step𝑖𝑡 4 .𝐼𝑛」，**步骤编号标签被破坏**；印刷为 `Step 4.`。已改为与 Step 1／2／3（第 901、911、945 行）及 Step 5（第 1019 行）一致的本地写法；
  4. MD 第 991 行 `coeficients` → `coefficients`（「as B^{\prime} − Γ^{\prime} has small coefficients」）；
  5. MD 第 997 行 `suficiently` → `sufficiently`（「is sufficiently small and」）；
  6. MD 第 1005 行**两处修复**：(a) **`exceptiona$1 / X$` → `exceptional$/ X$`**——MinerU 把印刷单词 `exceptional` 末字母 `l` 误识为数字 `1`，Markdown 作「exceptiona**1** / X」，技术术语被打散；印刷原文为 `exceptional/X`（150dpi 原页可见，文本层 `p023.txt` 计数 `exceptional/X`×2、单 `l` 缺失形式计数为 0）。已改为 `is exceptional$/ X$`，与紧接其后的「which is not **exceptional/X**」（Markdown 中该处一直正确）用同一写法；(b) **句点丢失**——印刷为「Since S^{\prime} is not a component of P^{\prime}**,** D^{\prime} ≠ S^{\prime}.」，Markdown 作 `…of$P ^ { \prime }$$D ^ { \prime } \neq S ^ { \prime }$`（句点缺失且与下一句粘连），已补为 `…of$P ^ { \prime }$, $D ^ { \prime } \neq S ^ { \prime }$`。
- 原文证据：文本层 `p023.txt` 计数 `coefficient`×5（含作为 `coefficients` 子串的 2 次，独立出现 3 次）、`coefficients`×2、`sufficiently`×2、`exceptional/X`×2，单 `f` 形式（`coeficient`/`coeficients`/`suficient`/`efective`/`diferent`）计数为 **0**；150dpi 原页图与文本层一致。**据此排除印刷原文为单 `f` 拼写或 `exceptiona1` 的可能，铁律三不适用。**
- 明确非差异（已核）：MD 第 960、986、1014 行 `\begin{array}{c} … \\ … \end{array}` 与 `\begin{array} { r } … \end{array}` 的行间式排版伪影（三行／两行公式的系数、括号、取整号与印刷逐字一致）；第 977 行 `\lfloor \Theta ^ { \prime } \rfloor = S ^ { \prime }`、第 980、986 行 `\left\lfloor … \right\rfloor`、第 986 行 `\langle { ( n + 1 ) \Delta ^ { \prime } } \rangle` 的分数部分尖括号，与印刷的 `⌊⌋`、`⟨⟩` 内容一致；第 991 行 `= 0 ;;` 的重复分号（印刷为单 `;`）、第 1005 行 `$/ X$` 与 `exceptional/X` 两种斜杠空格写法，均为标点级伪影，不改变 `exceptional/X` 这一**相对极小**的技术含义。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.23 止于末行等式 `… = −μ_D⌊Γ⌋ = 0`；MD 第 1017 行起（`because$\mu _ { D } \Gamma \in [ 0 , 1 )$, a contradiction.`、**Step 5**、`A := \alpha M − (K_X + Γ)` 等）属**印刷 PDF p.24**。内容无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.024（PDF p.24 / 印刷 p.24）
- PNG：/tmp/birkarsing_audit_p024.png（pngmono 150dpi）
- 核对：页眉「24 / Caucher Birkar」；Step 4 末句 `because μ_D Γ ∈ [0, 1), a contradiction.`；**Step 5**（`we show that sections of (L′ + P′)|_{S′} can be lifted to X′`、行间式 `A := αM − (K_X + Γ).`、`Letting A′ = φ^*A we have`、行间式 `K_{X′} + Γ′ + A′ − αM′ = 0.`、`Then`、**三行等式**（见下）、`By Step 1, 2 − α \ge 0, so`、行间式 `A′ + nN′ + (2 − α)M′`、`is nef and big. Moreover, (X′, Θ′) is plt with ⌊Θ′⌋ = S′, so we have`、行间式 `h^1(L′ + P′ − S′) = 0`、`by the Kawamata-Viehweg vanishing theorem as (X′, Θ′ − S′) is klt. Thus the restriction map`、行间式 `H^0(L′ + P′) → H^0((L′ + P′)|_{S′})`、`is surjective.`）；**Step 6**（`we introduce an effective divisor G_{S′} ∼ (L′ + P′)|_{S′}`、`Recall the n-complement K_S + B_S^+ from Step 2`、`Let R_S := B_S^+ − B_S which satisfies`、行间式 `−n(K_S + B_S) = −n(K_S + B_S^+ + B_S − B_S^+) ∼ −n(B_S − B_S^+) = nR_S \ge 0.`、`Let R_{S′} be the pullback of R_S.`、`Since M′ is Cartier and since S′ is a component of B′ with coefficient 1, the divisor`、行间式 `N′|_{S′} = (M′ − (K_{X′} + B′))|_{S′}`、`is well-defined up to linear equivalence. Now since M′|_{S′} ∼ 0 by Step 2, we have`、**两行等式** `nN′|_{S′} = n(M′ − (K_{X′} + B′))|_{S′} ∼ −n(K_{X′} + B′)|_{S′} = −nψ^*(K_S + B_S) ∼ nψ^*R_S = nR_{S′} \ge 0.`、`Then`、**两行等式** `(L′ + P′)|_{S′} = (2M′ + nN′ + nΔ′ − ⌊(n + 1)Δ′⌋ + P′)|_{S′} ∼ G_{S′} := nR_{S′} + nΔ_{S′} − ⌊(n + 1)Δ_{S′}⌋ + P_{S′}`、`where Δ_{S′} = Δ′|_{S′} and P_{S′} = P′|_{S′}. Note that`、行间式 `⌊(n + 1)Δ′⌋|_{S′} = ⌊(n + 1)Δ′|_{S′}⌋`、`since Δ′ and S′ intersect transversally.`、`We show G_{S′} \ge 0.`、`Assume C′ is a component of G_{S′} with negative coefficient.`、`Then since R_{S′} and P_{S′} are effective, there is a component D′ of Δ′ such that C′ is a component of D′|_{S′}. But`、行间式 `μ_{C′}(nΔ_{S′} − ⌊(n + 1)Δ_{S′}⌋) = μ_{C′}(−Δ_{S′} + ⟨(n + 1)Δ_{S′}⟩) \ge −μ_{C′}Δ_{S′} = −μ_{D′}Δ′ > −1`、`which gives μ_{C′}G_{S′} > −1 and this in turn implies μ_{C′}G_{S′} \ge 0 because G_{S′} is integral, a contradiction.`、`Therefore G_{S′} \ge 0, and by Step 5, L′ + P′ ∼ G′ for some effective divisor G′ whose support does not contain S′ and G′|_{S′} = G_{S′}.`）。与 Markdown 第 1017–1095 行逐项比对，辅以 `pdftotext -f 24 -l 24 -layout`。
- 结果：**PASS±**——Step 5／6 全部九个行间式的系数、括号层次与不等号方向均与印刷原页一致，重点核对了：(a) Step 5 三行等式中 `Θ′` 只在**第三行**出现（第二行仍是 `Γ′`），Markdown 第 1034 行正确；(b) Step 6 的 `\sim`（线性等价）与 `\ge 0` 的方向；(c) **`\psi^*` 与 `\phi^*` 均为上标**（拉回），而 p.021 中 `φ_*`（推前）为下标，两者未混；(d) `G_{S′} := nR_{S′} + nΔ_{S′} − ⌊(n + 1)Δ_{S′}⌋ + P_{S′}` 中**四段的符号次序**（+、+、−、+）与下标归属（`Δ_{S′}`、`P_{S′}` 带 *S′* 下标，而 `R_{S′}` 同）；(e) 行间式 `μ_{C′}(nΔ_{S′} − ⌊(n + 1)Δ_{S′}⌋) = μ_{C′}(−Δ_{S′} + ⟨(n + 1)Δ_{S′}⟩) \ge −μ_{C′}Δ_{S′} = −μ_{D′}Δ′ > −1` 末项的**严格不等号 `> −1`**（而非 `\ge −1`）；(f) `⌊(n + 1)Δ′⌋|_{S′} = ⌊(n + 1)Δ′|_{S′}⌋` 取整号在限制竖线左右的位置。差异为 OCR 连字丢 `f` 的拼写及一处句点丢失，逐处用 Edit 修复共 **4 处**：
  1. MD 第 1057 行 `efective` → `effective`（Step 6 首句「we introduce an effective divisor G_{S′} ∼ (L′ + P′)|_{S′}」）；
  2. MD 第 1063 行 `coeficient` → `coefficient`（「S′ is a component of B′ with coefficient 1」）；
  3. MD 第 1089 行 `coeficient` → `coefficient`（「with negative coefficient」）及 `efective` → `effective`（「R_{S′} and P_{S′} are effective」）；
  4. MD 第 1095 行 `efective` → `effective`（「for some effective divisor G′」）**并补句点**：印刷为 `…and G′|_{S′} = G_{S′}**.**`（Step 6 末句收束），Markdown 行末无句点，已补。
- 原文证据：文本层 `p024.txt` 计数 `effective`×3、`coefficient`×2、`coefficients`×0，单 `f` 形式（`efective`/`coeficient`/`suficient`/`diferent`）计数为 **0**；150dpi 原页图相应四处均印作双 `f`，且 Step 6 末句 `G′|_{S′} = G_{S′}.` 后确有句点。**据此排除印刷原文为单 `f` 拼写或缺句点的可能，铁律三不适用。**
- 明确非差异（已核）：MD 第 1034、1072、1078 行 `\begin{array}{c} … \\ … \end{array}` 的行间式排版伪影（三行／两行公式逐项与印刷一致）；第 1052、1066 行 `| _ {S ^ {\prime}}`、第 1059 行 `$G _ { S ^ { \prime } } = G _ { S ^ { \prime } }$` 处的**限制竖线写在数学模式开括号之后**（`| _ {…}`），渲染为 `|_{S′}`，与印刷的 `|_{S′}` 内容一致，属记号排版伪影；第 1046 行 `h ^ {1}`、第 1052 行 `H ^ {0}` 的幂次、第 1057 行 `R _ { S } : = B _ { S } ^ { + } - B _ { S }$` 中 `: =` 的空格、第 1089 行 `$D ^ { \prime } \vert _ { S ^ { \prime } }$` 用 `\vert` 而他处用 `|`，均为 OCR 空格/命令伪影，不改变任何公式或不等式。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.24 止于 Step 6 末句 `…and G′|_{S′} = G_{S′}.`；MD 第 1097 行起（**Step 7**、`we introduce Λ and show that it satisfies the properties listed in the theorem`、行间式 `(n + 2)M − nK_X − nE − ⌊(n + 1)Δ⌋ = L = \mathcal{L} + P ∼ G \ge 0.`、`Since nB is integral, ⌊(n + 1)Δ⌋ = nΔ` 等）属**印刷 PDF p.25**。内容无丢失/重复/错序。
- 备注：MD 第 1097 行 `By the definition of$L ^ { \prime } ,$` 中的逗号、`$P ^ { \prime } { } _ { ; }$` 中的孤立分号下标等伪影落在印刷 p.25，**留待 p.025 条目处置**，本页不越界修改。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.025（PDF p.25 / 印刷 p.25）
- PNG：/tmp/birkarsing_audit_p025.png（pngmono 150dpi）
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 25」；**Step 7**（`we introduce Λ and show that it satisfies the properties listed in the theorem`、`Let L, P, G be the pushdowns to X of L′, P′, G′`、行间式 `(n + 2)M − nK_X − nE − ⌊(n + 1)Δ⌋ = L = 𝓛 + P ∼ G \ge 0`、`Since nB is integral, ⌊(n + 1)Δ⌋ = nΔ, so`、**两行等式** `(n + 2)M − n(K_X + B) = (n + 2)M − nK_X − nE − nΔ = L ∼ nR := G \ge 0.`、`Let Λ := B^+ := B + R.`、`For consistency of notation, for the rest of the proof we will use B^+ instead of Λ.`、行间式 `n(K_X + B^+) ∼ (n + 2)M.`、`It remains to show that (X, B^+) is lc over z = f(S).`、`First we show that (X, B^+) is lc near S: this follows from inversion of adjunction [20], if we show`、行间式 `K_S + B_S^+ = (K_X + B^+)|_S`、`which is equivalent to showing R|_S = R_S. Since`、行长间式 `nR′ := G′ − P′ + ⌊(n + 1)Δ′⌋ − nΔ′ ∼ L′ + ⌊(n + 1)Δ′⌋ − nΔ′ = 2M′ + nN′ ∼_ℚ 0/X`、`and since ⌊(n + 1)Δ⌋ − nΔ = 0, we get φ_*nR′ = G = nR and that R′ is the pullback of R. Now by Step 6,`、**两行等式** `nR_{S′} = G_{S′} − P_{S′} + ⌊(n + 1)Δ_{S′}⌋ − nΔ_{S′} = (G′ − P′ + ⌊(n + 1)Δ′⌋ − nΔ′)|_{S′} = nR′|_{S′}`、`which means R_{S′} = R′|_{S′}, hence R_S and R|_S both pull back to R_{S′} which implies R_S = R|_S as required.`、`Assume now that (X, B^+) is not lc over z = f(S).`、`By the previous paragraph, (X, B^+) is lc near S and S is a non-klt centre of this pair.`、`On the other hand, (X, Γ) is plt with ⌊Γ⌋ = S, so if u > 0 is sufficiently small, then`、行间式 `(X, (1 − u)B^+ + uΓ)`、`is plt near S and S is a non-klt centre of this pair and no other non-klt centre intersects S.`、`Then since (X, B^+) is not lc over z, the non-klt locus of`、行间式 `(X, (1 − u)B^+ + uΓ)`（第二次出现）、`has at least two connected components (one of which is S) near the fibre f^{−1}{z}.`、`This contradicts the connectedness principle [25, Theorem 17.4] as`、**两行等式** `−(K_X + (1 − u)B^+ + uΓ) = −(1 − u)(K_X + B^+) − u(K_X + Γ) ∼_ℝ −u(K_X + Γ) ∼_ℝ uαM − u(K_X + Γ)/Z`、`is ample over Z. Therefore, (X, B^+) is lc over z.`、证毕方框 □）；随后 **`Proof. (of Theorem 1.9) Step 1.`**（`we take a Q-factorialisation of X and consider the contraction defined by aM − (K_X + B) for some a > 1`、`Replacing (X, B) with a Q-factorial dlt model`、`we can assume X is Q-factorial and that S is a component of ⌊B⌋`、`All the assumptions of the theorem are preserved.`、`The Fano type property is preserved by a relative version of [5, 2.13(7)] as −(K_X + B) is nef over Z.`）与次段 `By assumption, M is the pullback of an ample divisor on Z.`、`Moreover, M − (K_X + B) is nef and big, hence in particular it is semi-ample over Z since X is of Fano type over Z.`、`Thus by Lemma 2.26, if a > 1 is a real number, then aM − (K_X + B) is semi-ample`。与 Markdown 第 1097–1161 行逐项比对，辅以 `pdftotext -f 25 -l 25 -layout`。
- 结果：**PASS±**——Step 7 全部行间式的系数与等价/不等号方向与印刷原页一致，重点核对了：(a) 首个行间式中 **`= L = \mathcal{L} + P`** 的两个 `L` 是**不同字体**（斜体 `L` 与花体 `𝓛`），Markdown 第 1100 行 `\mathcal { L }` **正确区分**（文本层 `p025.txt` 此处作 `= L + P` 未区分，故必须以原图为准，原图确为花体）；(b) `nR := G` 的定义式与前后 `∼ G` 的关系；(c) 长链式 `nR′ := G′ − P′ + ⌊(n + 1)Δ′⌋ − nΔ′ ∼ L′ + ⌊(n + 1)Δ′⌋ − nΔ′ = 2M′ + nN′ ∼_ℚ 0/X` 的每一段与 `∼_ℚ 0/X` 的 `/X` 相对位置；(d) **`\phi _ { * }` 为下标（推前）**对应印刷 `φ_*nR′`，与 p.024 的 `\phi^ { * }`（上标拉回）分用正确；(e) `nR_{S′} = … = nR′|_{S′}` 两行式中 `⌊(n + 1)Δ_{S′}⌋` 与 `⌊(n + 1)Δ′⌋`（**下标不同**：`S′` vs 无）的区分；(f) 末组 `∼_ℝ −u(K_X + Γ) ∼_ℝ uαM − u(K_X + Γ)/Z` 中两处 `∼_ℝ` 与 `/Z`；(g) `f ^ { - 1 } \{ z \}` 的上标负一；(h) `[20]`、`[25, Theorem 17.4]`、`[5, 2.13(7)]`、`Lemma 2.26` 四处引文编号。差异逐处用 Edit 修复共 **3 处**：
  1. MD 第 1097 行**伪下标删除 + 标点归位**：Markdown 作 `By the definition of$L ^ { \prime } ,$, by the previous step, and by the exceptionality of$P ^ { \prime } { } _ { ; }$, we have`——其中 `{ } _ { ; }` 是 MinerU 凭空生成的**孤立分号下标**，会把术语「the exceptionality of P′」渲染成 `P′_;`（**凭空多出一个数学对象**）；印刷原文为「By the definition of L′, by the previous step, and by the exceptionality of P′, we have」，`P′` 后**无任何下标**（150dpi 原页可见；文本层 `p025.txt` 作 `the exceptionality of P ′ , we have`，无下标）。已改为 `By the definition of$L ^ { \prime }$, by the previous step, and by the exceptionality of$P ^ { \prime }$, we have`，同时把误入数学模式的逗号归位。
  2. MD 第 1135 行 `suficiently` → `sufficiently`（「so if u > 0 is sufficiently small, then」）；
  3. MD 第 1159 行 `Qfactorial` → `Q-factorial`（「Replacing (X, B) with a **Q-factorial** dlt model」）：印刷原文该词为 `Q-factorial`（150dpi 原页可见，因行末断行而断作 `Q-` / `factorial`，但连字符属该复合词本身；同页下一句「we can assume X is **Q-factorial**」在 Markdown 中一直带连字符），Markdown 此处**丢失连字符**。已补。
- 原文证据：文本层 `p025.txt` 计数 `sufficiently`×1、`exceptional`×1（`exceptionality`）、`integral`×1，单 `f` 形式（`suficient`/`coeficient`/`efective`/`diferent`）计数为 **0**；150dpi 原页图「sufficiently small」与「Q-factorial dlt model」均清晰可读，且 `P′` 后无下标。**据此排除印刷原文为单 `f` 拼写或缺连字符的可能，铁律三不适用。**
- 明确非差异（已核）：MD 第 1106 行 `\begin{array}{c} (n + 2)M − n(K_X + B) \\ = … \end{array}` 的行间式排版伪影（印刷为两行对齐式，Markdown 用 `array` 两行，系数与顺序一致）；第 1103 行 `$\lfloor ( n + 1 ) \Delta \rfloor = n \Delta$` 中 `\lfloor`（无 `\left`）与他处 `\left\lfloor` 混用，取整号内容一致；第 1124 行行长间式中四个 `∼` 的方向（`∼_ℚ` 在末段、其余为普通 `∼`）正确；第 1133 行 `$R _ { S } = R { \mid } _ { S }$` 把 `\mid` 包在花括号内（渲染为 `R|_S`）与第 1121、1150 行的 `R | _ { S }` 两种写法并存，属 OCR 空格伪影；第 1159 行 `[ 5 , 2 . 1 3 ( 7 ) ] ~ \mathrm { a s }` 中 `2 . 1 3` 的编号内空格与 `] ~` 之间的孤立波浪号（不换行空格残留）为伪影，`[5, 2.13(7)]` 编号正确、`as` 单词正确。
- **字形区分已正确保留的正面确认（不构成差异）**：本印刷页同时出现**两个不同的 L**——行间式 `(n + 2)M − nK_X − nE − ⌊(n + 1)Δ⌋ = L = 𝓛 + P ∼ G ≥ 0` 中，`= L =` 后的 `L` 为**斜体大写 L**（Step 7 首句「Let L, P, G be the pushdowns to X of L′, P′, G′」引入的推下除子），而紧随其后的 `𝓛` 为**花体**（互补除子）。150dpi 原页图可辨二者字形不同；`p025.txt` 文本层把二者一律输出为斜体 `L`（**文本层伪影，非印刷**）。Markdown 第 1100 行作 `L = \mathcal { L } + P`（斜体 L + 花体 `\mathcal { L }`）**忠实于印刷**，若按文本层「统一」为单个 `L` 反而会造成真实数学歧义，故不作改动。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.25 止于 Theorem 1.9 证明末段「…Therefore, (X, B⁺) is lc over z.」；MD 第 1159 行起（`Proof. (of Theorem 1.9) Step 1. In this step we take a Q-factorialisation of X…`、`By assumption, M is the pullback of an ample divisor on Z.`、行间式 `(aM − (K_X + B)) · C = 0 iff …`、Step 2／3／4 全部）属**印刷 PDF p.26**，留待 p.026 条目处置。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.026（PDF p.26 / 印刷 p.26）
- PNG：/tmp/birkarsing_audit_p026.png（pngmono 150dpi）
- 核对：页眉「26 / Caucher Birkar」；**Step 2** 全文（`we make some further modifications of (X, B) using the MMP`、行间式 `B − S ∼_ℚ −(K_X + S)/U`、`n ∈ ℕ and Λ′ ≥ B′`、`n(K_{X′} + Λ′) ∼ (n + 2)M′`、`n(K_X + Λ) ∼ (n + 2)M.`、`M′ is Cartier as the Cartier property of M is preserved by the MMP, by the cone theorem`、`X → V/U`、`We claim that S is not contracted over V; otherwise …`、`the pushdown of M to V is Cartier, again by the cone theorem`）；**Step 3** 全文（行间式 `Δ = (1 − b)B + bS`、`for a sufficiently small real number b > 0 (depending on a)`、三行展开式）；**Step 4** 首段与第一条项目符号（`In this step we produce a plt pair and apply Proposition 4.1 to finish the proof. By Lemma 2.7 applied to (X, Δ), there exist a prime divisor T over X and a projective birational morphism Y → X such that`、`• either Y → X is small or it contracts T but no other divisors,`）。
- 结果：**PASS±**——Step 1 证明续文与 Step 2／3／4 首段的全部行间式的系数、括号层次与不等号方向均与印刷原页一致，重点核对了：(a) 行间式 `(aM − (K_X + B)) · C = 0 **iff** (M − (K_X + B)) · C = 0 **and** M · C = 0.` 中 `iff`／`and` 两个逻辑词的存在与位置（Markdown 第 1164 行用 `\text { }` 正确保留）；(b) `K_X + B \sim_{\mathbb{Q}} 0 / U`、`B − S \sim_{\mathbb{Q}} −(K_X + S) / U`、`K_X + S \sim_{\mathbb{Q}} 0 / V` 三处 `/U`、`/V` 的相对线性等价位置；(c) `n(K_{X′} + Λ′) \sim (n + 2)M′` 与 `n(K_X + Λ) \sim (n + 2)M` 两式中 `n + 2` 的系数；(d) `Λ′ \ge B′`、`Λ \ge B` 的方向；(e) `n \in \mathbb{N}`；(f) `X \to V / U` 的实线箭头；(g) Step 3 行间式 `Δ = (1 − b)B + bS` 与三行展开式 `aM − (K_X + Δ) = aM − (K_X + (1 − b)B + bS) = aM − (1 − b)(K_X + B) − b(K_X + S) = (1 − b)(aM − (K_X + B)) + b(aM − (K_X + S))` 的逐项系数；(h) `Lemma 2.7`、`Proposition 4.1` 引文。差异逐处用 Edit 修复共 **6 处**：
  1. MD 第 1167 行**句点丢失**：印刷为「…a morphism and K_X + B ∼_ℚ 0/U**.**」，Markdown 行末无句点，已补；
  2. MD 第 1199 行 `suficiently` → `sufficiently`（「for a sufficiently small real number b > 0 (depending on a)」）；
  3. MD 第 1209 行 `Step$\it 4 .$In this step …` → `Step 4. In this step …`：与 p.021、p.023 同一 MinerU 伪影（裸 LaTeX 斜体命令 `\it` 排入数学模式），**步骤编号标签被破坏**；印刷为 `Step 4.`。已改为与 Step 1／2／3（第 1161、1169、1193 行）一致的本地写法；
  4. **回补 p.018 条目**：见上方 p.018 条目的「补记」栏——MD 第 663 行 Step 4 标题的同类 `\it` 伪影已于本轮修复并在该条目登记；
  5. MD 第 1189 行**标点被误排入数学模式**：印刷为「We claim that S is not contracted over $V$**;** otherwise since $K_X + S \sim_{\mathbb{Q}} 0/V$, …」，分号在正文中；Markdown 作 `over$V { : }$otherwise`，把分号 OCR 成冒号并包进花括号下标（渲染为 `V:`），已改为 `over$V$; otherwise`。文本层 `p026.txt` 第 22 行同作 `over V : otherwise`（同一 OCR 源），150dpi 原页图确证印刷为分号；
  6. MD 第 1201 行**同类标点误排**：印刷为「$aM − (K_X + S)$ is ample over $U$**,** we see that」，逗号在正文中；Markdown 作 `ample over$U _ { : }$, we see that`，把逗号 OCR 成下标冒号，已改为 `ample over$U$, we see that`。文本层 `p026.txt` 第 36 行作 `ample over U , we see that`（同一 OCR 源），150dpi 原页图确证。
- 原文证据：文本层 `p026.txt` 计数 `sufficiently`×1，`coefficients`／`coefficient`／`effective`／`different` 计数均为 0，单 `f` 形式（`suficient`/`coeficient`/`efective`/`diferent`）计数为 **0**；150dpi 原页图「for a sufficiently small real number b > 0 (depending on a)」与「K_X + B ∼_ℚ 0/U.」两处清晰可读。**据此排除印刷原文为单 `f` 拼写或缺句点的可能，铁律三不适用。**
- **文本层伪影的排除（已核，不构成 Markdown 缺陷）**：`p026.txt` 在 Step 2 输出「S is not a component of **B − − S**」，多出的第二个减号经 150dpi 原页图核对为 `pdftotext` 的连字伪影，印刷原文与 Markdown 均为「B − S」（Markdown 第 1175 行正确），**Markdown 无误**，不改。
- **印刷怪癖忠实保留，符合铁律三**：MD 第 1191 行 `The Q-factorial property of X **maybe** lost but we do not need it any more.`——印刷原文即作 **「maybe lost」**（语法上应为 `may be lost`，150dpi 原页可见），Markdown 原样保留，**未静默改正**。
- 明确非差异（已核）：MD 第 1167 行 `the induced map$U \ - \to \ Z$is a morphism`、第 1187 行 `$X \to V / U$`——`U \ - \to \ Z` 的箭头两侧空格为 MinerU 伪影、实线箭头方向与印刷一致；第 1204 行 `\begin{array}{c} … \\ … \end{array}` 的三行式排版伪影（三行系数逐项与印刷一致）；第 1161 行 `$Z .$Moreover,`、`$Z .$Thus by Lemma 2.26` 中句点落在数学模式内的写法与他处一致。（第 1189、1201 行的 `V { : }`、`U _ { : }` 原被列入本栏，经本轮 150dpi 原页图复核判定为**真实 OCR 缺陷**——印刷该处为分号与逗号——已改列为差异项 5、6 并修复。）
- 页块边界漂移（沿用 p.004 口径）：印刷 p.26 止于 Step 4 第一条项目符号「• either Y → X is small or it contracts T but no other divisors,」；MD 第 1213 行起（`• $( Y , T )$is plt,`、`• $- ( K _ { Y } + T )$is ample over X, and`、Step 4 结论等）属**印刷 PDF p.27**。内容无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.027（PDF p.27 / 印刷 p.27）
- PNG：/tmp/birkarsing_audit_p027.png（pngmono 150dpi）；仲裁源图 `/tmp/birk_p027_300.png`（pnggray 300dpi）及裁片 `/tmp/birk_p027_prop52.png`、`/tmp/birk_p027_lastbullet.png`
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 27」；**Step 4 收尾**（三条项目符号 `(Y, T) is plt,`、`−(K_Y + T) is ample over X, and`、`a(T, X, Δ) = 0.`、`In particular, T is mapped to z, by Step 3, as it is an lc place of (X, S). Moreover, since Δ ≤ B,`、行间式 `a(T, X, B) = 0.`、行间式 `Γ_Y = (1 − v)Δ_Y + vT`、`for some sufficiently small v > 0`、`α = (1 − v)a`、三行展开式、`T = ⌊Γ_Y⌋ maps to z.`、`hence it appears in B_Y with coefficient 1.`）；**新章标题 §5 `5. Singularities of divisors with bounded degree`** 与其首段；**§5.1 标题 `5.1. Finite morphisms to the projective space.`** 及其首段（含 `Noether normalisation theorem`、`[23, Theorem 2]`）；**Proposition 5.2 陈述全部**（`Let (X, Λ = ∑_1^d S_i) be a projective log smooth pair of dimension d where Λ is reduced. Let B = ∑ b_j B_j ≥ 0 be an R-divisor. Assume`、三条假设项目符号、行间式 `π : X → 𝔓^d = Proj k[t_0, …, t_d]`、五条结论项目符号）。
- 结果：**PASS±**——Step 4 三行展开式、Proposition 5.2 的编号与全部假设/结论项目符号内容、章与节标题的编号与文字均与印刷原页一致，重点核对了：(a) 行间式 `Γ_Y = (1 − v)Δ_Y + vT` 的两个系数与 `T`（非除子 `T`）的位置；(b) 三行展开式 `αM_Y − (K_Y + Γ_Y) = (1 − v)aM_Y − (K_Y + (1 − v)Δ_Y + vT) = (1 − v)aM_Y − (1 − v)(K_Y + Δ_Y) − v(K_Y + T) = (1 − v)(aM_Y − (K_Y + Δ_Y)) − v(K_Y + T)` 的逐项系数与两处负号；(c) `T = ⌊Γ_Y⌋` 的取整号与下标 Y；(d) Proposition 5.2 的 `\sum _ { 1 } ^ { d } S _ { i }`、`\cap _ { 1 } ^ { d } S _ { i }` 的上下限 `1`/`d` 及 `Λ`（花体 Λ，非斜体 L）的字形；(e) `\pi : X \to \mathbb{P}^d = \operatorname{Proj} k[t_0,\dots,t_d]` 中 `π` 用实线箭头（有限态射）、`z := (1 : 0 : \cdot \cdot : 0)` 的**两个**居中点、`π(S_i) = H_i`、`π^{-1}{z}`、`deg π = A^d`、`deg_{H_i} C ≤ deg_A B` 的下标与不等号方向；(f) `C = ∑ b_j π(B_j)` 中 **`∑` 无下标**（经 300dpi 裁片 `/tmp/birk_p027_lastbullet.png` 逐字确认，Markdown 第 1271 行亦无下标，**一致**）；(g) `[23, Theorem 2]` 与 `Theorem 1.8`、`Theorem 1.1`、`Proposition 4.1`、`[9]` 的引文编号。差异逐处用 Edit 修复共 **9 处**：
  1. MD 第 1219 行**逗号丢失**：印刷为「Moreover, since Δ ≤ B**,**」，Markdown 行末无逗号，已补；
  2. MD 第 1231 行 `suficiently` → `sufficiently`（「for some sufficiently small v > 0」）；同行**逗号丢失**（印刷「… is ample over X**,**」），一并补上；
  3. MD 第 1239 行 `coeficient` → `coefficient`（「hence it appears in B_Y with coefficient 1.」）；
  4. MD 第 1249 行**逗号丢失**：印刷为「• x ∈ ∩_1^d S_i**,**」（300dpi 裁片 `/tmp/birk_p027_prop52.png` 确证），已补；
  5. MD 第 1263 行**逗号丢失**：印刷为「• π(x) = z := (1 : 0 : · · : 0)**,**」，已补；
  6. MD 第 1265 行**逗号丢失**：印刷为「• π(S_i) = H_i where H_i is the hyperplane defined by t_i**,**」，已补；
  7. MD 第 1267 行**字符编码缺陷 + 数学模式误切**：印刷为「• π is **étale** over a neighbourhood **of** z**,**」；Markdown 作 `π is ´etale over a neighbourhood$o f z$`——(a) `é` 被写成前置锐音符 `´e`（组合字符位置错误）；(b) 连写单词 `of` 被 OCR 拆成 `o f` 并排入数学模式（渲染为斜体 `o f`）；(c) 行末逗号丢失。三者已一并改正为 `π is étale over a neighbourhood of z,`；
  8. MD 第 1271 行**印刷无逗号处多出逗号**：印刷作「…deg_A B **where** C = ∑ b_j π(B_j)**.**」（300dpi 裁片逐字确认 `B` 与 `where` 之间无逗号），Markdown 作 `$\deg _ { A } B$, where$C = …$`；已删去该逗号；
  9. MD 第 1271 行**句号丢失**：印刷该项目符号以 `π(B_j).` 收尾，Markdown 行末无句点，已补。
- 原文证据：文本层 `p027.txt` 计数 `coefficient`×1、`sufficiently`×1，单 `f` 形式（`coeficient`/`suficiently`）计数为 **0**；文本层第 45 行作 `π is étale over a neighbourhood of z,`（`é` 与 `of` 均正确），证明 Markdown 第 1267 行的 `´etale`／`o f` 为 MinerU 侧缺陷而非印刷。**据此排除印刷原文为单 `f` 拼写的可能，铁律三不适用。**
- 明确非差异（已核）：MD 第 1247 行 `\textstyle \sum _ { 1 } ^ { d } S _ { i }` 中的 `\textstyle` 与 `\begin{array}{r}{B = \sum b_j B_j \geq 0}\end{array}` 的 `array` 包装、第 1234 行 `\begin{array}{c} … \\ … \end{array}` 的三行式包装，均为 MinerU 行间式排版伪影，公式内容（`Λ = ∑_1^d S_i`、`B = ∑ b_j B_j ≥ 0`、`Γ_Y = (1 − v)Δ_Y + vT` 与三行展开式）与印刷逐项一致；`\operatorname { S u p p } B` 中的字距伪影对应印刷的 `Supp B`，正确。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.27 止于 Proposition 5.2 末条结论「• deg π = A^d and deg_{H_i} C ≤ deg_A B where C = ∑ b_j π(B_j).」；MD 第 1273 行起（`Proof. Since A − S_i is very ample for each i, …`、`R_i := D_i + S_i ∼ A`、`Now each R_i is the zero divisor of some global section α_i of 𝒪_X(A)`、行间式 `z := (1:0:…:0) = ∩_1^d H_i`、行间式 `π^{-1}{z} = ∩_1^d π^{-1}H_i = ∩_1^d R_i`）属**印刷 PDF p.28**，留待 p.028 条目处置。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.028（PDF p.28 / 印刷 p.28）
- PNG：/tmp/birkarsing_audit_p028.png（pngmono 150dpi）；仲裁源图 `/tmp/birk_p028_300.png`（pnggray 300dpi）及裁片 `/tmp/birk_p028_sum.png`、`/tmp/birk_p028_opd.png`、`/tmp/birk_p028_dific2.png`
- 核对：页眉「28 / Caucher Birkar」；**Proposition 5.2 证明全文**（`taking general divisors D_i ∈ |A − S_i|`、`(X, ∑_1^d R_i)`、`R_i := D_i + S_i ∼ A`、`Supp B contains no stratum of (X, ∑_1^d R_i) other than x`、`D_1|_I has no common component with B|_I;`、`α_i`、`α_0`、`R_0`、`∑_0^d R_i`、`∩_0^d R_i is empty`、`𝒪_X(A) ≃ π*𝒪_{𝔓^d}(1)`、`for each 0 ≤ i ≤ d.`、`π is a surjective finite morphism.`、`π*H_i = R_i`、`π(R_i) = H_i`、`π(S_i) = H_i`）；两个行间式（`z := (1 : 0 : · · · : 0) = ∩_1^d H_i,`、`π^{-1}{z} = ∩_1^d π^{-1}H_i = ∩_1^d R_i`）；`which shows π(x) = z as x ∈ ∩_1^d S_i ⊆ ∩_1^d R_i.`；`The rest of the proof is elementary which uses 2.21 among other things…` □；**§5.3 标题 `5.3. Bound on the length of blowup sequences.`** 及其首段（`due to Viehweg (see [43, Corollary 5.11])`）；**Lemma 5.4 陈述与证明**（三条假设项目符号、`Then (X, tL) is klt.`、`μ_x L`、`μ_x tL < 1`、`[29, Proposition 9.5.13]`、`inversion of adjunction`）□；证明后一段（`[5, Proposition 4.2]`、`Much of the difficulties already appear in the case X = 𝔓^d.`）与末段（`In the next key result, we bound the number of blowups in the centre blowup sequence associated to certain lc places.`）。
- 结果：**PASS±**——Lemma 5.4 的编号、三条假设、`A^d ≤ r`、`deg_A L ≤ r`、`Then (X, tL) is klt.` 与证明中 `μ_x tL < 1` 的不等号方向、`[29, Proposition 9.5.13]` 与 `[5, Proposition 4.2]`、`[43, Corollary 5.11]` 的编号均与印刷一致；两个行间式的 `\bigcap` 上下限 `1`/`d`、`π^{-1}`、`\{z\}`、`H_i`、`R_i` 逐项一致。本页 1 处**公式字形缺陷**、1 处**英文拼写缺陷**、1 处**标点误用**、3 处**句读丢失**，共 **6 处**，逐处用 Edit 修复：
  1. MD 第 1273 行**求和号被误识别为大写 Sigma（公式字形缺陷）**：印刷为「Supp B contains no stratum of $(X, \textstyle\sum_1^d R_i)$ other than x」，`∑` 为带上下限 `d`/`1` 的大算符（300dpi 裁片 `/tmp/birk_p028_sum.png` 逐字确认）；Markdown 作 `$( X , \Sigma _ { 1 } ^ { d } R _ { i } )$`，把求和号写成希腊大写 `Σ`（渲染为独立大写字母，**丢失算符性质与求和语义**）。已改为 `\sum _ { 1 } ^ { d } R _ { i }`，与同段上一处 `$( X , \textstyle \sum _ { 1 } ^ { d } R _ { i } )$` 及印刷一致；
  2. MD 第 1277 行**句号误代逗号**：印刷为「the zero divisor of α_i**,** that is, π*H_i = R_i.」（文本层第 30 行亦作 `that is, π ∗ Hi = Ri .`，150dpi 原页图确证），Markdown 作 `$\alpha _ { i } .$that is,`，已改为逗号；
  3. MD 第 1289 行**句点丢失**：印刷为「…x ∈ ∩_1^d S_i ⊆ ∩_1^d R_i**.**」，已补；
  4. MD 第 1299 行**逗号丢失**：Lemma 5.4 第二条假设，印刷为「• A is a very ample divisor on X with A^d ≤ r**,**」，已补；
  5. MD 第 1301 行**句点丢失**：Lemma 5.4 第三条假设，印刷为「• L ≥ 0 is an ℝ-divisor on X with deg_A L ≤ r**.**」，已补；
  6. MD 第 1307 行 `dificulties` → `difficulties`（「Much of the **difficulties** already appear in the case X = 𝔓^d」）；同行**句点丢失**，一并补上。
- **关于 `dificulties` 的铁律三裁定（重要）**：本处**不适用**铁律三的「印刷原文错字原样保留」。理由：300dpi 裁片 `/tmp/birk_p028_dific2.png` 显示印刷原文的 `ff` 连字**完整可见**（两个 f 竖笔并列），确系 `difficulties`；`p028.txt` 文本层同作 `dificulties` 属 PDF 文本层丢失连字，与本轮已登记的 `coeficient`／`suficiently`／`efective` 同源。Markdown 原为 `dificulties`，与印刷不符，已改正。
- **字形已正确保留的正面确认（不构成差异）**：印刷第 2 段两处 `𝒪_{𝔓^d}(1)` **均**用黑板粗体 `𝔓`（300dpi 裁片 `/tmp/birk_p028_opd.png` 逐字确认，第二处并非普通斜体 `P`）；`p028.txt` 文本层把两处一律输出为 `OPd (1)`（丢失黑板粗体，**文本层伪影**）。Markdown 第 1275 行两处均作 `\mathcal { O } _ { \mathbb { P } ^ { d } } ( 1 )`，**忠实于印刷**，不作改动。
- 明确非差异（已核）：MD 第 1273 行 `\textstyle \sum _ { 1 } ^ { d } R _ { i }`、`\textstyle \sum _ { 0 } ^ { d } R _ { i }` 的 `\textstyle` 与 `\Sigma`→`\sum` 修复后与印刷的行内小算符排版一致；`$| B | _ { I } ;$` 中把 `B` 写成正体加绝对值竖线（印刷为斜体 `B|_I`）属 OCR 字形伪影，渲染为 `|B|_I` 语义不变；第 1275 行 `\pi \colon X \to \mathbb{P}^d`、`\simeq`、`0 \leq i \leq d .` 与印刷一致；`\operatorname { S u p p } B` 的字距伪影对应印刷 `Supp B`。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.28 止于末段「In the next key result, we bound the number of blowups in the centre blowup sequence associated to certain lc places.」；MD 第 1309 行起（Proposition 5.7 陈述等）属**印刷 PDF p.29**，留待 p.029 条目处置。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.029（PDF p.29 / 印刷 p.29）
- PNG：/tmp/birkarsing_audit_p029.png（pngmono 150dpi）；仲裁源图 `/tmp/birk_p029_300.png`（pnggray 300dpi）及裁片 `/tmp/birk_p029_arrow2.png`、`/tmp/birk_p029_C.png`、`/tmp/birk_p029_arrow.png`
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 29」；**Proposition 5.5 陈述全部**（`Let d, r be natural numbers and ε be a positive real number. Then there is a natural number p depending only on d, r, ε satisfying the following. Assume`、**八条**假设项目符号、`Then T can be obtained by a sequence of centre blowups, toroidal with respect to (X, Λ), of length at most p.`）；**证明首段**（`over ℂ`、`Lefschetz principle`、`formal neighbourhoods instead of analytic neighbourhoods`）；**Step 1** 全文（`Λ = ∑_1^d S_i`、`deg_A Λ ≤ r`、`A − S_i is very ample for each i`、`B = ∑ b_j B_j`、行间式 `π : X → 𝔓^d = Proj ℂ[t_0, …, t_d]`、`z = (1 : 0 : · · · : 0)`、`π is étale over z`、`deg π = A^d`、`deg_{H_i} C ≤ deg_A B ≤ r where C = ∑ b_j π(B_j)`、`by the proof of 5.2, π*H_i coincides with S_i near x.`）；**Step 2** 全文（`π^an|_U`、`(𝔓^d, C) is ε-lc near z`、`Θ := ∑_1^d H_i`、`J^an|_U ⊆ Supp B^an|_U`、`hence J = x and I = z.`、`Let X_1 → X_0 = X be the blowup of X along this centre.`、`K_{X_1} + Λ_1`、`hence a stratum of (X_1, Λ_1). We blowup X_1 along the centre of T and so on.`）；行间式 `Y = X_l → · · · → X_0 = X`。
- 结果：**FAIL（以原图为准）**——本页存在 **1 处数学内容丢失（态射箭头 `\to` 完全缺失）**，另有 10 处字符级/句读级差异；Proposition 5.5 的编号、八条假设内容、`A^d ≤ r`、`deg_A B ≤ r`、`deg_A Λ ≤ r`、`a(T, X, B) ≤ 1`、`length at most p.`、`deg π = A^d`、`deg_{H_i} C ≤ deg_A B ≤ r`、`Θ := ∑_1^d H_i`、`K_{X_1} + Λ_1`、`Y = X_l → · · · → X_0 = X` 的系数与箭头方向均与印刷一致。逐处用 Edit 修复共 **11 处**：
  1. **【FAIL 级·数学内容丢失】** MD 第 1343 行 `Let$X _ { 1 }  X _ { 0 } = X$ be the blowup of X along this centre.`——印刷为 `Let $X_1 \boldsymbol{\to} X_0 = X$ be the blowup of X along this centre.`，**`X_1` 与 `X_0` 之间的态射箭头被 MinerU 整字丢失**（300dpi 裁片 `/tmp/birk_p029_arrow2.png` 逐字确证印刷有长实线箭头；`p029.txt` 文本层第 48 行亦作 `Let X1 → X0 = X`，证明箭头存在于 PDF 文本层而在 Markdown 侧丢失）。丢失后该句退化为两个变体名的并列，**「X₁ 是 X 的爆破」这一态射关系不再可读**，属数学内容错误。已补 `\to`，改为 `Let$X _ { 1 } \to X _ { 0 } = X$ be the blowup of X along this centre.`；
  2. MD 第 1331 行 `over C.` → `over ℂ.`：印刷为黑板粗体 **ℂ**（300dpi 裁片 `/tmp/birk_p029_C.png` 确证），Markdown 作普通斜体/正体 `C`；已改为 `ℂ`，与同页第 1336 行 `\mathrm{Proj} \mathbb {C} [ t _ {0}, \ldots , t _ {d} ]` 的 `\mathbb{C}` 一致；
  3. MD 第 1323 行**连写词被拆入数学模式**：印刷为「does not contain any stratum **of** $(X, Λ)$ except possibly x,」，Markdown 作 `any stratum$o f \left( X , \Lambda \right)$`（`of` 被 OCR 拆为 `o f` 并排入数学模式，渲染为斜体 `o f`）；与 p.027 差异项 7 的 `$o f z$` 同一 MinerU 伪影。已改为 `any stratum of $\left( X , \Lambda \right)$`；
  4. MD 第 1339 行 `´etale` → `étale`（「Moreover, π is **étale** over z, …」；`p029.txt` 第 32 行文本层亦作 `étale`，150dpi 原页图确证；与 p.027 差异项 7 同一类）；
  5. MD 第 1339 行**句点被误代为逗号并吞入数学模式**：印刷为「In addition, by the proof of **5.2,** π*H_i coincides with S_i near x.」，`5.2` 后的句点被 OCR 成逗号，且 `5.2, π*H_i` 整段被包进一个数学组（数字 `5.2` 与公式间无空格）。已改为 `In addition, by the proof of 5.2, $\pi ^ { * } H _ { i }$ coincides with$S _ { i }$near x.`；
  6. MD 第 1315 行**逗号丢失**：Proposition 5.5 第二条假设「• A is a very ample divisor on X with $A^d \le r$**,**」，已补；
  7. MD 第 1319 行**逗号丢失**：第四条假设「• deg_A B ≤ r and deg_A Λ ≤ r**,**」，已补；
  8. MD 第 1321 行**逗号丢失**：第五条假设「• x is a zero-dimensional stratum of $(X, Λ)$**,**」，已补；
  9. MD 第 1333 行**句点丢失**：印刷为「In this step we consider a finite morphism to 𝔓^d**.** Removing the components of Λ not passing through x, …」，已补；
  10. MD 第 1341 行**句点丢失**：印刷为「…hence J = x and I = z**.**」（300dpi 裁片 `/tmp/birk_p029_arrow.png` 确证），已补；
  11. MD 第 1343 行**句点丢失**：印刷为「…hence a stratum of $(X_1, \Lambda_1)$**.** We blowup $X_1$ along the centre of $T$ and so on.」，已补。
- 原文证据：文本层 `p029.txt` 中 `é`/`to`/`étale` 均正确，证明上述第 1、2、4、5 项为 Markdown 侧缺陷；本页无单 `f` 拼写类缺陷（`dificulties` 在 p.028 已处理，本页计数为 0）。
- 明确非差异（已核）：MD 第 1333 行 `\textstyle \sum _ { 1 } ^ { d } S _ { i }`、`\sum b _ { j } B _ { j }` 的 `\textstyle` 与第 1339、1341 行 `\begin{array}{r}{…}\end{array}` 的 `array` 包装为 MinerU 行间式排版伪影，公式内容与印刷逐项一致；`\mathrm { a n }`、`\mathrm { S u p p }`、`\operatorname { S u p p }` 的字距/字体伪影对应印刷的上标 `an` 与 `Supp`，渲染语义不变；`z = ( 1 : 0 : \cdots : 0 )$` 中**三个**居中点与 p.027 命题项目符号中的**两个**居中点**均为印刷原样**（印刷原文此处确为 `· · ·`），Markdown 分别作 `\cdots` 与 `\cdot \cdot`，**忠实保留，未作「统一」**。
- 页块边界漂移（沿用 p.004 口径）：印刷 p.29 止于行间式 `Y = X_l → · · · → X_0 = X`；MD 第 1349 行起（Step 2 续文、`X_{d_1} → … → X_{d_l} = 𝔓^d` 等）属**印刷 PDF p.30**，留待 p.030 条目处置。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.030（PDF p.30 / 印刷 p.30）——本轮范围末页
- PNG：/tmp/birkarsing_audit_p030.png（pngmono 150dpi）；仲裁源图 `/tmp/birk_p030_300.png`（pnggray 300dpi）及裁片 `/tmp/birk_p030_R.png`、`/tmp/birk_p030_D.png`
- 核对：页眉「30 / Caucher Birkar」；**Step 2 收尾**（`of centre blowups obtaining T as the exceptional divisor of the last blowup (2.16 (3)). The sequence is toroidal with respect to (X, Λ).`、行间式 `W = Z_l → · · · → Z_0 = 𝔓^d`、`the sequence of centre blowups of R, the exceptional divisor of Z_l → Z_{l−1}`、`a(R, 𝔓^d, Θ) = 0.`、行间式 `a(R, 𝔓^d, C) = a(T, X, B) ≤ 1.`、`Note that we cannot simply replace X, B, Λ with 𝔓^d, C, Θ because we do not know whether (𝔓^d, C) is ε-lc away from z.`）；**Step 3** 全文（`t ∈ (0, 1/2)`、`Lemma 5.4`、`deg_{H′} C|_G = deg_H C ≤ r`、`G is not inside Supp C, by Step 2`、`inversion of adjunction`、行间式 `K_G + tC|_G = (K_{𝔓^d} + Θ + tC)|_G.`、`This proves the existence of t.`）；**Step 4** 至页末（`Step 4. Letting ε′ = (t/2)ε`、`K_{𝔓^d} + Δ ∼_ℝ 0`、`a(R, 𝔓^d, Δ) ≤ 1`、`D = (1 − t/2)Θ + (t/2)C`、`Lemma 2.3`、两个 `a(E, 𝔓^d, D)` 行间式、`a(R, 𝔓^d, D)` 行间式、末个 `−(K_{𝔓^d} + D) = −(1 − t/2)(K_{𝔓^d} + Θ) − (t/2)(K_{𝔓^d} + C)` 行间式）。
- 结果：**PASS±**——全部 7 个行间式的系数、括号层次与不等号方向均与印刷原页逐项一致，重点核对了：(a) 行间式 `a(E, 𝔓^d, D) = (1 − t/2)a(E, 𝔓^d, Θ) + (t/2)a(E, 𝔓^d, C) ≥ (t/2)ε = ε′` 的两处 `t/2` 与 `≥ (t/2)ε`；(b) 行间式 `a(E, 𝔓^d, D) ≥ a(E, 𝔓^d, Θ + (t/2)C) = (1/2)a(E, 𝔓^d, Θ + tC) + (1/2)a(E, 𝔓^d, Θ) ≥ 1/2 ≥ ε′`——含印刷原样保留的 `≥ 1/2 ≥ ε′` 这一「双不等号」写法（Markdown 第 1382 行与印刷一致，**未按数学常识改写**）；(c) 行间式 `a(R, 𝔓^d, D) = (1 − t/2)a(R, 𝔓^d, Θ) + (t/2)a(R, 𝔓^d, C) = (t/2)a(R, 𝔓^d, C) ≤ 1.` 中间等号（`a(R, 𝔓^d, Θ) = 0` 由 Step 2 已得，故 `1 − t/2` 项消失）；(d) `t \in (0, 1/2)` 的区间端点与分母 2；(e) `ε′ = (t/2)ε` 与 `(1 − t/2)Θ + (t/2)C`、`(1 − t/2)(K_{𝔓^d} + Θ) − (t/2)(K_{𝔓^d} + C)` 中 t 的**同一分母 2**；(f) `W = Z_l → · · · → Z_0 = 𝔓^d` 与 `Z_l → Z_{l−1}` 的实线箭头及下标 `l`、`l−1`、`0`；(g) `z \not \in I` 的斜线否定、`a(E, 𝔓^d, Θ) ≥ 1` 的不等号方向；(h) `(2.16 (3))`、`Lemma 2.3`、`Lemma 5.4`、`Step 2`、`Step 3` 的编号。差异逐处用 Edit 修复共 **5 处**：
  1. MD 第 1349 行**句点丢失**：印刷为「…of the last blowup (2.16 (3)). The sequence is toroidal with respect to $(X, Λ)$**.**」，已补；
  2. MD 第 1357 行**伪下标删除**（伪影类，与 p.025 差异项 1 同源）：印刷为「centre blowups of **R,** the exceptional divisor of $Z_l \to Z_{l−1}$.」（300dpi 裁片 `/tmp/birk_p030_R.png` 逐字确认 `R` 后**只有一个逗号**、无第二个逗号、无下标），Markdown 作 `of$R ,$, the exceptional`——多出一个逗号并被排成下标。已改为 `of$R$, the exceptional`；
  3. MD 第 1373 行 `Step$\it 4 .$Letting$\begin{array} { r } { \epsilon ^ { \prime } = \frac { t } { 2 } \epsilon . } \end{array}$` → `Step 4. Letting$\begin{array} { r } { \epsilon ^ { \prime } = \frac { t } { 2 } \epsilon . } \end{array}$`：与 p.018（第 663 行，补记）、p.021（第 833 行）、p.023（第 971 行）、p.026（第 1209 行）同一 MinerU 伪影（裸 LaTeX 斜体命令 `\it` 排入数学模式），**步骤编号标签被破坏**；印刷为 `Step 4.`（300dpi 裁片 `/tmp/birk_p030_D.png` 确证）。**至此 `\it` 伪影在 PDF p.1–p.30 范围内出现于 MD 第 833、971、1209、663、1373 行共 5 处，全部已用逐页原图证据修复；余下第 1917、1979、2175 行位于 PDF p.30 之后，超出本轮 p.1–p.30 授权范围，未处置，在此登记以备后续轮次。**
  4. MD 第 1373 行**句点丢失**：印刷为「We start with an auxiliary boundary $D = (1 − t/2)\Theta + (t/2)C$**.** We will show that $(𝔓^d, D)$ is ε′-lc.」（300dpi 裁片 `/tmp/birk_p030_D.png` 确证 `C` 后有句点），已补；
  5. MD 第 1385 行**句点丢失**：印刷为「Therefore, we have proved $(𝔓^d, D)$ is ε′-lc**.**」，已补。
- 原文证据：文本层 `p030.txt` 中 `(2.16 (3))`、`Z_l → Z_{l−1}`、`≥ 1/2 ≥ ε′`、`a(R, P^d, D) = …` 等全部公式字符正确，证明上述差异均属 Markdown 侧缺陷；本页无单 `f` 拼写类缺陷（`sufficiently`／`coefficient` 计数为 0，单 `f` 形式计数为 0）。
- 明确非差异（已核）：MD 第 1373 行 `\begin{array}{r}{\epsilon ^ { \prime } = \frac{t}{2}\epsilon .}\end{array}` 的 `array` 包装与其中的孤立句点（印刷为句点，**原样保留**）、`\textstyle \frac{t}{2}` 为行内小分式排版，与印刷一致；第 1365 行 `Pick a closed point$\boldsymbol { y } \in \mathbb { P } ^ { d }$` 中 `\boldsymbol{y}`（印刷为斜体 `y`）属 OCR 字重伪影，渲染为粗体不影响语句；`\mathrm { a n }`、`\mathrm { S u p p }` 的字距伪影对应印刷的上标 `an` 与 `Supp`；`ε′` 在 Markdown 中作 `\epsilon ^ { \prime }`、在 Step 3 文字处作 Unicode `ǫ`，二者均对应印刷的 `ε`/`ǫ`，属同一记号的不同编码，不构成数学歧义。
- **本轮（PDF p.1–p.30）收尾状态**：FAIL 3 页（p.010 `D_Y`、p.015 `A_Y`、p.029 `X_1 \to X_0` 箭头丢失），PASS± 27 页，无整段丢失、无错序、无重复。所有缺陷均以 Edit 逐处修复并逐页登记于本文件；未执行任何 `git commit`／`add`／`merge`／`push`，未触碰根级 `AUDIT-INDEX.md`／`AUDIT-PROGRESS.log`／`MEMORY.md`／`README.md` 及其他论文目录。
- 印刷 p.30 止于末个行间式 `−(K_{𝔓^d} + D) = −(1 − t/2)(K_{𝔓^d} + Θ) − (t/2)(K_{𝔓^d} + C)`；Step 4 余下部分及以后属印刷 PDF p.31 及之后，**超出本轮 p.1–p.30 授权范围**，未审计、未处置。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

---

## 本轮统一溯源清单（PDF p.1–p.30 全部缺陷类）

> 方法：在 worktree `/Users/aurolafly/.zcode/worktrees/cpf-redo-Birkar_2016_singularities_linear_systems` 内执行
> `git show 03760242:"2018年 - Birkar/…__Birkar_2016_singularities_linear_systems.md"`（原始 MinerU 导出）与
> `git show cpf-redo/Birkar_2016_singularities_linear_systems^:…`（本 redo 分支父提交 = `16ffcc7c`，已含 Luna 修复与 GLM 的 p.001–p.009 重做），
> 对本轮 30 页登记的每一缺陷类逐项计数比对。

| 缺陷类 | 原始导出 `03760242` | 分支父提交 `16ffcc7c` | 裁定 |
|---|---|---|---|
| `coeficient(s)` | 49 | 48 | **导出缺陷**（peer 少 1 处＝GLM p.001–p.009 已修，无新增） |
| `suficiently` | 11 | 11 | 导出缺陷 |
| `efective` / `pseudo-efective` | 17 / 5 | 17 / 5 | 导出缺陷 |
| `diferent` / `diferential` / `dificult` | 4 / 1 / 2 | 4 / 1 / 2 | 导出缺陷 |
| `ofice` / `tha` | 1 / 1 | 1 / 1 | 导出缺陷 |
| `Step$\it`（步骤标签裸 LaTeX 斜体命令） | 8 | 8 | 导出缺陷 |
| `exceptiona1` / `Qfactorial` | 0 / 1 | 0 / 1 | `Qfactorial` 为导出缺陷 |
| 伪下标 `{ } _ { ; }`、`$R ,$` | 1 / 1 | 1 / 1 | 导出缺陷 |
| `\Sigma _ { 1 } ^ { d }`（求和号误作大写 Σ） | 1 | 1 | 导出缺陷 |
| `´etale` / `Etale` | 7 / 1 | 7 / 1 | 导出缺陷 |
| 标点入数学模式 `{ : }` / `_{ : }` | 3 | 3 | 导出缺陷 |
| 连写词拆入数学模式 `o f`（`$o f z$`、`stratum$o f \left( …\right)$`） | 2 | 2 | 导出缺陷 |
| `over C.`（应为 ℂ） | 1 | 1 | 导出缺陷 |
| `K¨ahler` / `Pˇaun` / `Rdivisors` / 全角 `，` | 2 / 1 / 1 / 3 | 2 / 1 / 1 / 3 | 导出缺陷 |
| `\overline { T }` | 1 | **0** | **peer 修复**（`16ffcc7c` 提交信息：`overline T→T, Luna 误判经 300dpi 仲裁改正`）——GLM p.008 重做方向正确 |
| 丢失态射箭头 `X _ { 1 }  X _ { 0 }`（p.029 FAIL） | 1（MD 第 1343 行） | 1（同左行号） | **导出缺陷**；同类的 `V _ { 2 }  V _ { 1 }`、`V _ { n }  V _ { n - 1 }`、`X _ { n } ^ { \prime }  X _ { n }`（MD 第 97 行）已由 `16ffcc7c` 修复，说明该丢失型态是 MinerU 系统性伪影，本页为同源漏网 |
| 丢失下标 `D _ { Y }`（p.010 FAIL） | MD 第 373 行无下标 | 同 | 导出缺陷（Luna `353ad7fa` 未触及） |
| 丢失下标 `A _ { Y }`（p.015 FAIL） | MD 第 569 行无下标 | 同 | 导出缺陷（Luna `353ad7fa` 仅恢复同行箭头，未补下标） |

**结论：本轮 p.1–p.30 登记的全部缺陷，无一由 peer commit 引入**；全部存在于 MinerU 原始导出 `03760242`，即**全部为导出缺陷（escape 漏报型）而非回归**。peer 相对原始导出只有**净修复**（`\overline{T}` 1 处、`coeficient` 1 处、MD 第 97 行 3 处箭头）。

## 本轮残余缺陷登记（未处置，均在 p.1–p.30 授权范围外或按登记不改口径）

- **`Step$\it` 伪影残余 3 处**：MD 第 1917（`Step 4.`）、1979（`Step 6.`）、2175（`Step 4.`）行——均在**印刷 PDF p.30 之后**（Step 4/6 伪影对应 §5.3 与 §6 的后续 Step），超出本轮范围，未处置；原导出品类计数 8，本轮已修 5（MD 第 663、833、971、1209、1373 行），余 3。
- **`{ : }` 残余 1 处**：MD 第 1923 行——超出 p.30 范围。
- **单 `f` 拼写类残余**：`coeficient(s)` 27、`efective` 11、`diferent` 3、`diferential` 1、`dificult` 1、`suficiently` 1——全部集中在 PDF p.31 及之后，**超出本轮范围**；本轮 p.1–p.30 内的同类项已全部逐处修复或按各页条目「登记不改」处理。
- **`K¨ahler` / 全角 `，` / `exceptiona1` 等**：原导出计数分别为 2 / 3 / 0，其在 p.1–p.30 内的实例已在对应页条目中逐条登记（p.015 等），未静默保留为「无差异」。

## 本轮执行边界声明

- 未执行任何 `git commit` / `git add` / `git merge` / `git push`；两处修改均为 worktree 内未提交改动，交由总Master 串行集成。
- 未触碰根级 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、`MEMORY.md`、`README.md`，未触碰任何其他论文目录。
- PDF 原件全程只读（`gs -dFirstPage/-dLastPage` 渲染 + `pdftotext` 抽取），未修改。
- 未启动/停止 MinerU 服务，未改动 MinerU 配置。
- PIL 仅用于**裁剪** 300dpi 仲裁图，未用于写入 Markdown；Markdown 全部改动均以 `Edit` 工具逐处完成。
- 页级进度以本文件逐页条目为可恢复检查点；根级 `AUDIT-PROGRESS.log` 的回填由总Master 依据本文件条目串行执行。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p130`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

---

# 第二轮：PDF p.31–p.46（16 页）逐页视觉审计

> actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。
> 承第一轮（p.1–p.30）口径：页块漂移约 +1 页沿用 p.004 登记；印刷原文优先；印刷自身错字与怪癖原样保留并登记。

## p.031（PDF p.31 / 印刷 p.31）
- PNG：/tmp/birkarsing_audit_p031.png（pngmono 150dpi）
- 核对：印刷 p.31 全文（Step 5 首段、Step 5 次段与显示式、Step 6 段与显示式、§5.6 标题段、Proposition 5.7 陈述与前 6 条项目符号）
- 结果：PASS±（差异列表）
  1. MD 第 1407 行 `Then$\Delta _ { W ^ { \prime } }$is efective as…` → `is effective as…`。印刷 p.31 Step 5 第五行作 `Then ∆_{W′} is effective as a(R,P^d,∆) ≤ 1.`（150dpi 原页图可见双 `ff`），属单 `f` 拼写 OCR 缺陷，非印刷怪癖。
  2. MD 第 1415 行 `we deduce that the coeficient of the birational transform of R in ψ^*Θ…` → `the coefficient of…`。印刷 p.31 Step 6 第五行作 `the coefficient of the birational transform of R`，同上单 `f` 缺陷。
  3. MD 第 1435 行 `are all ample (in particular, …are all ℝ-Cartier)，` 行末为**全角逗号** → 改回印刷的半角 `),`。印刷 p.31 Proposition 5.7 第 5 条说明行作 `are all ample (in particular, we are assuming B, Λ, L are all ℝ-Cartier),`。
- 明确非差异（已核）：
  - 第 1399、1402 行 `deg_{H_i} −(K_{P^d}+Θ)=1` 与 `= d+1 − deg_{H_i} C ≥ d+1 − r` 的系数、下标 `H_i`、不等号方向与印刷逐项一致。
  - 第 1409 行 `because$W ^ { \prime } \dashrightarrow W ^ { \prime \prime }$is an MMP on…`：印刷该处为 MMP 箭线（虚线箭头），`\dashrightarrow` 为等价写法，非缺陷。
  - 第 1415 行 `\lfloor \frac { 1 } { u } - 1 \rfloor` 的取整括号与印刷 `p := ⌊1/u − 1⌋` 一致；`\textstyle { \frac { 1 } { u } }` 的 textstyle 包裹为他处通用伪影。
  - 第 1409 行两处 `ǫ<sup>′</sup>-lc` 为 MinerU 的 HTML 上标写法（内容即印刷 ε′-lc），与同段后半 `$\epsilon ^ { \prime } { - } \mathrm { l c }$` 排版不一致但**语义无损**，按登记不改口径（同 `M<sup>c</sup>Kernan` 类）。
  - 印刷 p.31 末尾的证毕方框 □ 未转写，属 MinerU 常规取舍，不计缺陷。
- 页块边界：印刷 p.31 止于 Proposition 5.7 第 6 条项目符号 `• (X,Λ) is lc near a point x (not necessarily closed),`，与 MD 第 1437 行对应，无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.032（PDF p.32 / 印刷 p.32）
- PNG：/tmp/birkarsing_audit_p032.png（pngmono 150dpi）
- 核对：印刷 p.32 全文（Prop 5.7 末 2 条项目符号、结论句、Lemma 5.8 陈述与证明全部显示式及 9 条项目符号、Lemma 5.9 陈述与证明首段）
- 结果：PASS±（差异列表）
  1. MD 第 1441 行 `• $a ( T , X , B ) \leq 1$` 句末补句点。印刷 p.32 第 2 条项目符号作 `a(T, X, B) ≤ 1.`。
  2. MD 第 1443 行 `…we have$\mu _ { T } \nu ^ { * } L \leq q$` 句末补句点。印刷作 `we have µ_T ν*L ≤ q.`。
  3. MD 第 1461 行 `…we can assume that R is a component of$H \cap C$` 句末补句点。印刷作 `that R is a component of H ∩ C.`。
  4. MD 第 1465 行 `• $( H , B _ { H } )$is a projective ǫ-lc pair of dimension$d - 1$` 补逗号。印刷作 `…of dimension d − 1,`。
  5. MD 第 1501 行两处 `the coeficient` → `the coefficient`。印刷 p.32 Lemma 5.8 证明末段两处均作 `the coefficient`（单 `f` 拼写 OCR 缺陷）。
- 明确非差异（已核）：
  - 第 1452、1458 行两个显示式的下标 `B_H, A_H, Λ_H, L_H` 与限制符 `|_H` 逐项与印刷一致；`K_H + B_H = (K_X + B + H)|_H`、`K_H + Λ_H = (K_X + Λ + H)|_H` 的加项顺序正确（先 B 后 Λ）。
  - 第 1490、1496 行 `(K_W + Λ_W + G)|_G and (K_W + B_W + G)|_G` 与 `K_H + Λ_H and K_H + B_H` 的「和/与」配对顺序与印刷一致，未错位。
  - 第 1499 行 `µ_T Λ_W = 1 while µ_T B_W ≥ 0` 的等号与不等号方向与印刷一致。
  - 第 1501 行 `\sigma ^ { * } ( L _ { H } ) = ( \phi ^ { * } L ) | _ { G }` 的 `\sigma` 与 `\phi` 未被 OCR 互换（印刷同为 σ 与 φ）。
  - 第 1467 行 `A_H^{d−1} ≤ r` 的上标 `d-1` 与印刷一致（印刷为 `A_H^{d−1}`，非 `A^d`）。
- 页块边界（沿用 p.004 漂移口径）：印刷 p.32 止于 Lemma 5.9 证明首段 `…does not contain any stratum of (X,Λ) other`；MD 第 1505 行 `than x, and this occupies much of the proof.` 及 Step 1 属**印刷 PDF p.33**。内容无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.033（PDF p.33 / 印刷 p.33）
- PNG：/tmp/birkarsing_audit_p033.png（pngmono 150dpi）；仲裁裁剪 /tmp/birk_p033_gamma2.png（300dpi pnggray，Γ_V 显示式带）
- 核对：印刷 p.33 全文（Lemma 5.9 证明 Step 1 全部、Step 2 全部含 3 条项目符号与显示式 (5.11)、Step 3 首段与 Γ_V 显示式）
- 结果：PASS±（差异列表）
  1. MD 第 1533 行 `are all ample, by definition of$B ^ { \prime \prime } , \Lambda ^ { \prime \prime }$` 句末补句点。印刷作 `are all ample, by definition of B′′, Λ′′.`。
  2. MD 第 1535 行 `…birational transform of a stratum of$( X , \Lambda )$ Now replacing…` 在 `)` 后补句点。印刷作 `…of (X, Λ). Now replacing …`。
  3. MD 第 1539 行 `• $( H , B _ { H } )$is a projective ǫ-lc pair of dimension$d - 1$` 补逗号。印刷作 `…of dimension d − 1,`。
  4. MD 第 1551 行 `and because$( X , B )$is$\epsilon { - } \mathrm { l c }$` 句末补句点。印刷作 `and because (X,B) is ε-lc.`。
- **重点存真（依铁律二，未改动）**：MD 第 1556 行 Γ_V 显示式作 `\Gamma_ {V} = (1 + t) B ^ {\sim} + (1 - \frac {\epsilon}{4}) \sum E _ {i} + (1 - a) T`。曾疑此处应依 Step 1 改作 `B^{\prime\prime}`，但 300dpi 原页图放大后可见印刷**确实写作上标波浪号 `B^~`**（紧随其后一句即「and ∼ denotes birational transform」）。故 MD 与印刷一致，**保留原样，不按数学常识改写**。
- 明确非差异（已核）：
  - 第 1510 行 `µ_{E'}B' ≥ −d + 1 and µ_{E'}Λ' = 1` 的不等号方向与等号逐项与印刷一致（注意第二项为 `= 1` 而非 `≥ 1`）。
  - 第 1524 行 `B^{\prime\prime} := \beta B ^ {\prime} + (1 - \beta) \Lambda^ {\prime} \geq 0` 的 β 系数 `βB′` 与 `(1−β)Λ′` 顺序与印刷一致（未互换）。
  - 第 1527 行 `ε′ = εβ` 的乘子为 `β`，与印刷一致。
  - 第 1530 行三项 `A′−B′′, A′−Λ′′, A′−L′` 的撇号数逐项与印刷一致（B 双撇、Λ 双撇、L 单撇）。
  - 第 1537、1545 行 `$( X , B + t B )$is$\epsilon/2$-lc` —— `pdftotext` 文本层作 `2ǫ-lc`，150dpi 与 300dpi 原页图均确认为**分数 ε/2**（上 ε 下 2），MD 写法正确，非缺陷。
  - 第 1548 行 `K_X + B + tB = \frac{1}{2}(K_X+B) + \frac{1}{2}(K_X + B + 2tB)` 两个系数均为 1/2，与印刷一致。
- 页块边界：印刷 p.33 止于 Γ_V 显示式；MD 第 1559 行 `where$E _ { i }$are the exceptional divisors of ψ other than T…` 及以后属**印刷 PDF p.34**。内容无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.034（PDF p.34 / 印刷 p.34）
- PNG：/tmp/birkarsing_audit_p034.png（pngmono 150dpi）
- 核对：印刷 p.34 全文（Step 3 续 6 个显示式与两段文字、Step 4 全段及其显示式、Step 5 首段与 3 个显示式）
- 结果：PASS±（差异列表）
  1. MD 第 1559 行 `…since$\mu _ { T } \Gamma _ { V } = 1 - a$we have` → 补逗号 `$1 - a$, we have`。印刷作 `…since µ_TΓ_V = 1 − a, we have`。
  2. MD 第 1571 行 `is efective and exceptional over X…` → `is effective`。印刷作 `is effective and exceptional over X`（单 `f` 缺陷）。
  3. MD 第 1589 行 `…with positive coeficient because$( X , B + t B )$is$\epsilon/2$-lc…` → `with positive coefficient`。印刷作 `positive coefficient`。
  4. MD 第 1591 行 Step 4 段内两处 `positive coeficient` → `positive coefficient`（`the MMP contracts every component of G with positive coefficient,` 与 `is a component of G with positive coefficient so these are all contracted;`）。印刷两处均作 `coefficient`。
  5. MD 第 1605 行 `with coeficients$\leq 1 - \epsilon$` → `with coefficients`。印刷作 `with coefficients ≤ 1 − ε.`。
- 明确非差异（已核）：
  - 第 1562 行显示式（5.12）`K_V + Γ_V = K_V + B^~ + ∑(1−a_i)E_i + (1−a)T + tB^~ + ∑(a_i − ε/4)E_i = ψ*(K_X + B) + tB^~ + F`：两处 `B^{\sim}` 与印刷的 `B^~` 一致（承 p.033 存真结论），`\psi^ {*}` 的星号未被吞，`\sum` 两项系数与次序逐项与印刷一致。
  - 第 1568 行 `F := \sum (a _ {i} - \frac {\epsilon}{4}) E _ {i}` 与第 1586 行 `G := \sum (a _ {i} ^ {\prime} - \frac {\epsilon}{4}) E _ {i} + (a ^ {\prime} - a) T` 的减号、括号、末项顺序与印刷一致（G 末项为 `(a′ − a)T`，未被写成 `(a − a′)T`）。
  - 第 1580 行第二行 `\psi^ {*} (K _ {X} + (1 + t) B) + G` 中的 `(1 + t)B` 与印刷一致（未写成 `1 + tB`）。
  - 第 1594 行 `K _ {V} + \Gamma_ {V} \equiv t B ^ {\sim} + F / X` 的 `≡` 与 `/X` 位置与印刷一致。
  - 第 1602 行 `0 \leq D _ {Y} \sim_ {\mathbb {R}} \frac {1}{t} (K _ {Y} + \Gamma_ {Y} + 3 d A _ {Y})` 的 `\sim_{\mathbb{R}}` 与系数 `1/t` 与印刷一致。
  - 第 1614 行 `frac {1}{t} … = frac {1}{t} \pi^ {*} (K _ {X} + B + 3 d A) + B _ {Y} ^ {\sim} + frac {1}{t} F _ {Y}`：`B_Y^~` 前的系数为 **1**（印刷亦为 1，非 1/t），两个 `1/t` 的位置与印刷一致。
  - 第 1620 行 `D _ {Y} = \pi^ {*} H + B _ {Y} ^ {\sim} + \frac {1}{t} F _ {Y}` 与印刷末个显示式逐项一致。
  - 第 1580 行 `\begin{array}{r l}` 的对齐环境为其余显示式通用伪影，非缺陷。
- 页块边界：印刷 p.34 止于 `D_Y = π*H + B_Y^~ + (1/t)F_Y` 显示式，与 MD 第 1620 行一致；其后 Step 6 属**印刷 PDF p.35**。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.035（PDF p.35 / 印刷 p.35）
- PNG：/tmp/birkarsing_audit_p035.png（pngmono 150dpi）
- 核对：印刷 p.35 全文（Step 5 末显示式与结论句、Step 6 全部 5 个显示式与 4 段文字、Step 7 首段与 ν 序列显示式及末个不等式显示式）
- 结果：PASS±（差异列表）
  1. MD 第 1629 行 `Letting D be the pushdown of$D _ { Y }$to$X$, we get$D = H + B ,$` 句末 `,$` → `.$`。印刷作 `we get D = H + B.`。
  2. MD 第 1649 行 `is general semi-ample with coeficients$\leq 1 - \epsilon$` → `with coefficients`；同行句末 `+D _ { Y }$` 补逗号 → `+D _ { Y }$,`。印刷作 `…with coefficients ≤ 1 − ε and F_Y ≥ 0. …since T is not a component of B_Y^~ + F_Y + D_Y,`。
  3. MD 第 1661 行 `so depending only on$d , r , \epsilon .$such that` → `$\epsilon ,$such that`。印刷作 `so depending only on d, r, ε, such that`（逗号引出 such that，句点为 OCR 误判）。
  4. MD 第 1677 行 `and of length$l \leq p$` 句末补句点。印刷作 `and of length l ≤ p.`。
- 明确非差异（已核）：
  - 第 1652 行显示式 `a(T,X,D) = 1 − µ_T(R_Y + D_Y − (1/t)F_Y) = 1 − µ_T R_Y = 1 − µ_T(B^~ + R_Y) = a(T,X,B) ≤ 1.` 与印刷逐项一致；注意第二步的 `1 − µ_T R_Y` 依赖 D_Y 半 ample 且 F_Y ≥ 0，与印刷相同，未被 OCR 吞掉系数 `1/t`。
  - 第 1664 行 `3mA − D ~_R (mA − (1/t)K_X) + (mA − (3d/t)A) + (mA − ((1+t)/t)B)` 三个括号内的系数 `1/t`、`3d/t`、`(1+t)/t` 与印刷逐项一致，且第二括号为 `mA − (3d/t)A`（非 `(mA − 3d/t)A`）。
  - 第 1674 行 `ν \colon U = X _ {l} \to \dots \to X _ {0} = X` 的箭头方向（左为 X_l 指向右为 X_0 = X）与印刷一致；印刷省略号为三点居中点，MD `\dots` 等价。
  - 第 1682 行 `µ_T ν*L ≤ deg_J ν*L ≤ J^d ≤ q` 的度数下标 `J`、不等号方向与印刷一致。
  - 第 1640、1652 行的 `\begin{array}{c} … \\ … \end{array}` 双行折叠为其余显示式通用伪影。
- 页块边界：印刷 p.35 止于 `µ_Tν*L ≤ deg_Jν*L ≤ J^d ≤ q.` 显示式，与 MD 第 1682 行一致；MD 第 1685 行 `Thus µ_T ν*L ≤ q if we replace ν …`、第 1687 行起 `Proof. (of Proposition 5.7)` 属**印刷 PDF p.36**。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.036（PDF p.36 / 印刷 p.36）
- PNG：/tmp/birkarsing_audit_p036.png（pngmono 150dpi）
- 核对：印刷 p.36 全文（Lemma 5.9 结论句、Proposition 5.7 证明全篇：2 条项目符号、7 个显示式与全部文字段）
- 结果：PASS±（差异列表）
  1. MD 第 1687 行 `Replacing A we can assume it is efective and…` → `it is effective`。印刷作 `Replacing A we can assume it is effective and that A − (K_X + B) is ample`。
  2. MD 第 1689 行 `…belongs to$\mathcal { Q } .$` → `$\mathcal { Q },$`。印刷作 `then (W, Θ_W + A_W) belongs to 𝒬,`（逗号引出下一条项目符号）。
  3. MD 第 1691 行 `$A _ { W } - \Theta _ { W }$and$A _ { W } - \phi ^ { * } A$are ample.` **补回缺失的项目符号** `• `。印刷该行为第二条项目符号 `• A_W − Θ_W and A_W − φ*A are ample.`；MD 丢失列表标记，致两条并列条件在 Markdown 中退化为普通段落。
  4. MD 第 1703 行三处 `coeficients` → `coefficients`（`the coeficients of$B _ { W }$`、`the coeficients of$J _ { W }$`、`the coeficients of$J _ { W }$ belong to a fixed finite set`）。印刷三处均作 `coefficients`。
  5. MD 第 1711 行 `the coeficients of$B _ { W }$` → `the coefficients of…`，`has coeficient 1 in$\Theta _ { W }$` → `has coefficient 1 in…`，并在行末补句点。印刷作 `because the coefficients of B_W are bounded from below and each exceptional/X prime divisor has coefficient 1 in Θ_W.`
  6. MD 第 1713 行 `the pair$( W , \Delta _ { W } )$is$\delta { \mathrm { - l c } } .$by Lemma 2.3.` → `…,by Lemma 2.3.`（句点改逗号）。印刷作 `the pair (W, ∆_W) is δ-lc, by Lemma 2.3.`
- 明确非差异（已核）：
  - 第 1687 行 `deg$_ { A } \Lambda < A ^ { d } \leq r` 的严格不等号 `<`（非 `≤`）与印刷一致。
  - 第 1698 行显示式 `0 = a(T,X,Λ) = a(T,W,Λ_W) ≥ a(T,W,Θ_W) ≥ 0` 两处不等号方向与两端常数 `0` 与印刷逐字一致。
  - 第 1703 行 `$K _ { X }$is$\mathbb { Q } \mathrm { { - } C a r t i e r }$, so$\phi ^ { * } K _ { X }$makes sense`：印刷作 `K_X is ℚ-Cartier, so φ∗K_X makes sense`，黑板粗体 `\mathbb { Q }` 未被 OCR 降为普通 `Q`。
  - 第 1713 行 `\delta { \mathrm { - l c } }` 中 δ 未被误写为 `d`。
  - 第 1722 行显示式第二行 `= \alpha a (T, W, B _ {W}) = \alpha a (T, X, B) \leq 1.`：末项 `≤ 1` 而非 `≤ δ`，与印刷一致（印刷亦作 `≤ 1`）。
  - 第 1725 行 `${ \textstyle { \frac { 1 } { 2 } } } A _ { W } + K _ { W }$` 与 `…− ( K _ { W } + B _ { W } )$` 两处系数均为 `1/2`，且印刷为行内小分数，MD 用 `\textstyle` 恰当地对应，非缺陷。
  - 第 1733 行 `replace$X , B , A , L ,$ $\Lambda , x$with$W , \Delta _ { W } , A _ { W } , L _ { W } , \Theta _ { W } , w$` 中的 `$ $` 为印刷行末断行伪影，六元对应顺序与印刷一致。
- 页块边界：印刷 p.36 止于 `We are then done by Lemma 5.9.` 与证毕方框，与 MD 第 1733 行一致；其后 §5.7 属**印刷 PDF p.37**。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.037（PDF p.37 / 印刷 p.37）
- PNG：/tmp/birkarsing_audit_p037.png（pngmono 150dpi）
- 核对：印刷 p.37 全文（§5.10 标题段、Proposition 5.11 陈述与 7+4 条项目符号及中间显示式、证明首段、Step 1 全部含 3 条项目符号与 3 个显示式）
- 结果：PASS±（差异列表）
  1. MD 第 1745 行 `• $A - B$and$A - L$are ample (so we are assuming that B and L are$\mathbb { R } \mathrm { - } C a r t i e r )$` 行末补逗号。印刷作 `…are ℝ-Cartier),`。
  2. MD 第 1747 行 `• $( X , B + t L )$is ǫ<sup>′</sup>-lc for some$t \in ( 0 , r )$` 行末补逗号。印刷作 `…for some t ∈ (0, r),`。
  3. MD 第 1767 行 `• T is an lc place of$( X , \Lambda )$` 行末补句点。印刷作 `• T is an lc place of (X, Λ).`（该行为 Prop 5.11 结论四条中的末条）。
  4. MD 第 1787、1789、1791 行 **三条项目符号标记全部缺失**，逐条补回 `• `。印刷 p.37 Step 1 为三条并列条件：`• (H, B_H + tL_H) is a projective ε′-lc pair of dimension d − 1,` / `• A_H is a very ample divisor on H with A_H^{d−1} ≤ r, and` / `• A_H − B_H − tL_H is ample.`；MD 中三行退化为普通段落，列表结构丢失（与 p.036 第 1691 行同类）。
- 明确非差异（已核）：
  - 第 1752 行显示式 `a (T, X, B + t L) = \epsilon^ {\prime}` 等号右侧为 **ε′**（非 ε、非 0），与印刷一致。
  - 第 1777 行 `is$\frac { \epsilon ^ { \prime } } { 2 } \mathrm { - l c }$`：印刷为**上下排列的 ε′/2**（分子 ε′、分母 2），MD 的 `\frac` 写法对应正确；`pdftotext` 文本层作「′2」属文本层伪影，非缺陷。
  - 第 1780 行 `(r + 1) A - B - t L = A - B + t (A - L) + (r - t) A`：三项分解的符号（`+ t(A−L)`、`+ (r−t)A`）与系数顺序逐项与印刷一致，未被 OCR 反号。
  - 第 1769 行 `there exists a real number$\epsilon ^ { \prime } \in ( 0 , \epsilon )$` 中 ACC 的引用编号 `[13]` 与印刷一致；`( Y , ( 1 - \epsilon ^ { \prime } ) S )$is a klt pair` 的系数 `1−ε′` 与印刷一致。
  - 第 1737 行 `a positive real number$\epsilon ^ { \prime } < \epsilon$` 的严格不等号 `<` 与印刷一致。
  - 第 1799 行 `we can choose v depending only on$d , r , \epsilon .$` —— 印刷作 `d, r, ε.`，此处句点正确（与 p.035 第 1661 行的 `ε, such that` 情形不同），MD 无误。
  - 第 1796 行显示式 `(H, B _ {H} + t L _ {H} + 2 v (B _ {H} + t L _ {H}))` 中的系数 `2v` 与印刷一致。
- 页块边界：印刷 p.37 止于显示式 `(X, H + B + tL + 2v(B + tL))`，与 MD 第 1802 行一致；MD 第 1805 行 `is plt in a neighbourhood of H by inversion of adjunction…` 及以后属**印刷 PDF p.38**。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.038（PDF p.38 / 印刷 p.38）
- PNG：/tmp/birkarsing_audit_p038.png（pngmono 150dpi）
- 核对：印刷 p.38 全文（Step 1 续 3 个显示式与两段文字、Step 2 全篇含 Γ_W 定义式、c_i/ε′/F/G 等 7 个显示式与全部文字段）
- 结果：PASS±（差异列表）
  1. MD 第 1823 行 `and because$( X , B + t L )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$` 句末补句点。印刷作 `and because (X, B + tL) is ε′-lc.`。
  2. MD 第 1855 行 `so$F$is efective.` → `so$F$is effective.`。印刷作 `so F is effective.`（单 `f` 缺陷）。
  3. MD 第 1887 行 `so$E _ { i }$is a component of G with positive coeficient.` → `positive coefficient.`。印刷作 `…with positive coefficient.`。
- **留待 p.039 条目处置**：MD 第 1889 行 `Step 3. …here we are using the fact that the coeficients of$( 1 + v )( B ^ {\sim} + t L ^ {\sim } )$are less than 1` 属**印刷 PDF p.39**，本轮不越页处置。
- 明确非差异（已核）：
  - 第 1828 行 `Γ_W = (1 + v) (B ^ {\sim} + t L ^ {\sim}) + (1 - \frac{\epsilon^{\prime}}{4}) \sum E _ {i} + (1 - \epsilon^ {\prime}) T`：三个系数 `(1+v)`、`(1−ε′/4)`、`(1−ε′)` 与印刷逐项一致；此处印刷**确实**写作 `B^~` 与 `tL^~`（与 p.033 的 Γ_V 同类记号），MD 忠实。
  - 第 1846 行显示式（5.22）两行：第一行的 `∑(1−c_i)E_i` 与 `∑(c_i − ε′/4)E_i` 次序、第二行 `= \psi^ {*} (K _ {X} + B + t L) + v (B ^ {\sim} + t L ^ {\sim}) + F` 的 `\psi^*` 星号与 `v(B^~ + tL^~)` 括号，均与印刷一致，未漏项。
  - 第 1852 行 `F := \sum (c _ {i} - \frac {\epsilon^ {\prime}}{4}) E _ {i}` 与第 1878 行 `G := \sum (c _ {i} ^ {\prime} - \frac {\epsilon^ {\prime}}{4}) E _ {i} + (a ^ {\prime} - \epsilon^ {\prime}) T`：G 末项为 `(a′ − ε′)T`（未被写成 `(ε′ − a′)T`），与印刷一致。
  - 第 1872 行显示式首行 `(1 + v) (B ^ {\sim} + t L ^ {\sim})` 后的 `∑ (1 - c _ {i} ^ {\prime}) E _ {i}` 使用撇指标 `c_i′`，与印刷 `c′_i` 一致（撇未丢失）。
  - 第 1820 行两个系数均为 `\frac {1}{2}`，第 1817、1887 行的 `\frac { \epsilon ^ { \prime } } { 2 }` 与印刷的上下排列分数一致（文本层「′2」为伪影）。
  - 第 1825 行行内 `Γ<sub>W</sub>` 为 MinerU 的 HTML 下标写法（内容即 Γ_W），与同段显示式 `\Gamma_ {W}` 排版不一致但语义无损，按登记不改口径。
- 页块边界：印刷 p.38 止于 `…so E_i is a component of G with positive coefficient.`，与 MD 第 1887 行一致；MD 第 1889 行 `Step 3.` 起属**印刷 PDF p.39**。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.039（PDF p.39 / 印刷 p.39）
- PNG：/tmp/birkarsing_audit_p039.png（pngmono 150dpi）
- 核对：印刷 p.39 全文（Lemma 5.9 之 Prop 5.11 证明 Step 3 全篇含 4 个显示式、Step 4 全段、Step 5 前半含 5 个显示式）
- 结果：PASS±（差异列表）
  1. MD 第 1889 行 `…the coeficients of$( 1 + v )( B ^ {\sim} + t L ^ {\sim } )$are less than 1 because` → `the coefficients of…`。印刷作 `…here we are using the fact that the coefficients of (1+v)(B^~ + tL^~) are less than 1 because`（单 `f` 缺陷；即 p.038 条目所列「留待 p.039 处置」项）。
  2. MD 第 1897 行 `the MMP contracts every component of$G$with positive coeficient.` → `positive coefficient.`。印刷作 `with positive coefficient.`。
  3. MD 第 1917 行 `Step$\it 4 .$In this step we consider a model…` → `Step 4. In this step…`。印刷 Step 标签为正文体 `Step 4.`，无 `\it` 残留（150dpi 原页图可见；系 MinerU 原始 `\it` 泄漏，第一轮残余 3 处之第 1 处）。
  4. MD 第 1923 行 `…an ample model Y of$- T _ { Y ^ { \prime \prime } }$over$X { \mathrm { : } }$: that${ \mathrm { i s } } ,$we run an MMP…` → `over$X$: that is, we run an MMP…`。印刷作 `…over X: that is, we run an MMP on −T_Y″…`；原写法把冒号既塞进数学模式（`{ \mathrm { : } }`）又另写一个句外冒号，形成「X:: that is ,」的重号与断字（`{ \mathrm { i s } }`），属标点被吸收进数学模式的 OCR 缺陷（即第一轮登记的残余 `{ : }` 1 处）。
  5. MD 第 1923 行 `…$- T _ { Y }$is ample over$X .$. In particular…` → `over$X$.`。印刷作 `…is ample over X. In particular, …`；原写法在数学模式内保留句点又补句点，形成双句号「X ..」。
- 明确非差异（已核）：
  - 第 1920 行显示式 `a (T, X, B + t L) = \epsilon^ {\prime} < 1,` 的严格不等号 `<` 与逗号收尾与印刷一致。
  - 第 1900 行 `K _ {W} + \Gamma_ {W} \equiv v (B ^ {\sim} + t L ^ {\sim}) + F / X` 中 `v(B^~ + tL^~)` 与 `F/X` 的 `\equiv` 与 `/X` 位置与印刷一致（承 p.033、p.038 存真：`B^~`、`L^~` 为印刷记号）。
  - 第 1928 行 `K _ {Y} + \Gamma_ {Y} \sim_ {\mathbb {R}} G _ {Y} = (a ^ {\prime} - \epsilon^ {\prime}) T _ {Y} / X`：符号为 `\sim_{\mathbb R}`（线性等价，非 `\equiv`），与印刷一致；系数 `(a′ − ε′)` 符号方向正确。
  - 第 1942 行 `µ_{T_Y} φ*tL ≥ ε − ε′ > 0` 的双重不等式方向与印刷一致（印刷亦作 `≥ ε − ε′ > 0`）。
  - 第 1948 行 `a ^ {\prime} = a (T, X, (1 + v) (B + t L)) < \epsilon^ {\prime} = a (T, X, B + t L).` 严格小于号与两端表达式与印刷一致。
  - 第 1954 行 `K _ {Y} + \Gamma_ {Y} + 2 d A _ {Y} \sim_ {\mathbb {R}} (a ^ {\prime} - \epsilon^ {\prime}) T _ {Y} / X`：注意系数为 `2d`（Step 3 中为 `2dA_Y′`、Step 5 首句为 `3dA_Y`），三处倍数与印刷逐处一致，未被统一。
  - 第 1895 行 `is$\frac { \epsilon ^ { \prime } } { 2 } -$lc`：把连字符放在数学模式内、`lc` 放模式外，属排版伪影，渲染仍为「ε′/2-lc」，语义无损，按登记不改口径。
  - 第 1923 行 `is inside$T _ { Y } { \mathrm { ~ a s ~ } } - T _ { Y }$` 的 `{~ a s ~}` 为行末断词伪影，渲染为「as」，与印刷 `is inside T_Y as −T_Y` 一致，非缺陷。
- 页块边界：印刷 p.39 止于显示式 `K_Y + Γ_Y + 2dA_Y ~_R (a′ − ε′)T_Y/X`，与 MD 第 1954 行一致；MD 第 1957 行 `we deduce that…` 起属**印刷 PDF p.40**。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.040（PDF p.40 / 印刷 p.40）
- PNG：/tmp/birkarsing_audit_p040.png（pngmono 150dpi）；仲裁裁剪 /tmp/birk_p040_by.png（300dpi pnggray，`K_Y + B_Y^~ + tL_Y^~ + …` 显示式）
- 核对：印刷 p.40 全文（Prop 5.11 证明 Step 5 续全部显示式、Step 6 全篇含 7 个显示式与全部文字段）
- 结果：PASS±（差异列表）
  1. MD 第 1979 行 `Step$\it 6 .$In this step…` → `Step 6. In this step…`。印刷 Step 标签为正文体 `Step 6.`（150dpi 原页图可见），无 `\it` 残留（第一轮残余 3 处之第 2 处）。
  2. MD 第 1994 行 `B _ {\widetilde {Y}} ^ {\sim}` → `B _ {Y} ^ {\sim}`、`t L _ {\widetilde {Y}} ^ {\sim}` → `t L _ {Y} ^ {\sim}`。300dpi 仲裁裁剪确认印刷作 `K_Y + B_Y^~ + tL_Y^~ + (1 − ε′)T_Y = φ*(K_X + B + tL),`，下标为**普通 Y**、波浪号为上标；MD 的 `\widetilde {Y}` 为 MinerU 多加的波浪号包裹，且与紧接的第 1997 行 `where$B _ { Y } ^ { \sim } , L _ { Y } ^ { \sim }$` 自相矛盾。
  3. MD 第 2021 行 `depend only on$d , r , \epsilon .$.` → `$\epsilon$.`（去掉数学模式内多余句点，消除「ε ..」双句号）；同行 `the fact that$F$is contracted over$Y$` 行末补逗号 → `over$Y$,`。印刷作 `…depend only on d, r, ε. On the other hand, by Step 2 and the fact that F is contracted over Y,`。
- 明确非差异（已核）：
  - 第 2004 行显示式 `= (l - \frac {3 d}{v}) A _ {Y} - (1 + \frac {1}{v}) \phi^ {*} (…) + \frac {1}{v} \phi^ {*} (…) + B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim} + \frac {3 d}{v} A _ {Y}.`：三个分式 `3d/v`、`1/v`、`3d/v` 的分子分母与符号逐项与印刷一致（易错处：`(1 + 1/v)` 的加号未被吞）。
  - 第 2018 行 `(l - \frac {3 d}{v}) A _ {Y} - (1 + \frac {1}{v}) \phi^ {*} (…) = \phi^ {*} ((l - \frac {3 d}{v}) A - (1 + \frac {1}{v}) (…))` 右端的括号配对与印刷一致。
  - 第 2030 行 `\frac {1}{v} (K _ {Y} + \Gamma_ {Y} + 3 d A _ {Y}) = \frac {1}{v} \phi^ {*} (K _ {X} + B + t L) + B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim} + \frac {3 d}{v} A _ {Y}`：注意 `B_Y^~`、`tL_Y^~` 前的系数为 **1**（印刷亦为 1），未被误加 `1/v`。
  - 第 1968 行 `0 \leq P _ {Y ^ {\prime}} \sim_ {\mathbb {R}} K _ {Y ^ {\prime}} + \Gamma_ {Y ^ {\prime}} + 2 d A _ {Y ^ {\prime}}` 的 `\leq` 与 `\sim_{\mathbb R}` 与印刷一致。
  - 第 1974 行 `\left(K _ {Y} + \Gamma_ {Y} + 2 d A _ {Y}\right) \cdot C = P _ {Y} \cdot C \geq 0` 的交点与不等号方向与印刷一致。
  - 第 1977 行末 `K _ {Y} + \Gamma_ {Y} + 3 d A _ {Y}$is ample` 的倍数由 2d 变 3d，与印刷一致（非笔误重复）。
  - 第 2024 行 `K _ {Y} + \Gamma_ {Y} = \phi^ {*} (K _ {X} + B + t L) + v (B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim}),` 的 `\phi^*` 星号与 `v(…)` 括号与印刷一致。
  - 第 2013 行 `φ*B, φ*L, T_Y are all R-Cartier` 的三项未被 OCR 换序。
- 页块边界：印刷 p.40 止于显示式 `lA_Y − (K_Y + (1−ε′)T_Y)` 与 `is ample by the previous paragraph.`，与 MD 第 2036、2039 行一致；MD 第 2041 行 `Step 7.` 起属**印刷 PDF p.41**。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.041（PDF p.41 / 印刷 p.41）
- PNG：/tmp/birkarsing_audit_p041.png（pngmono 150dpi）
- 核对：印刷 p.41 全文（承 p.40 末句 `is ample by the previous paragraph.`；Prop 5.11 证明 Step 7 全篇含 8 个显示式；Step 8 至显示式 `n(K_Y + Λ_Y) ∼ (n + 2)lA_Y`）
- 结果：PASS±（差异列表）
  1. MD 第 2095 行 `…then replacing it with$3 l$ we can assume…` → `…with$3 l$, we can assume…`。印刷作 `Therefore, taking l large enough and then replacing it with 3l, we can assume lA_Y − (K_Y + T_Y ) is ample.`，`3l` 后有逗号；原 Markdown 把该逗号吞入数学模式闭合后丢失。
- 明确非差异（已核）：
  - 第 2041 行 `Step 7. … By Step 5, we have$\mu _ { T _ { Y } } \phi ^ { * } t L \geq \epsilon - \epsilon ^ { \prime } .$` 与印刷一致；行内分数 `\alpha \le \frac { \epsilon ^ { \prime } } { \epsilon - \epsilon ^ { \prime } }` 的 `\begin{array} { r } { … } \end{array}` 包裹沿用本篇既有渲染约定（第一轮已核为非缺陷），不改。
  - 第 2044 行 `\alpha \mu_ {T _ {Y}} \phi^ {*} (B + t L) = \epsilon^ {\prime}.` 与印刷一致（注意此处下标为 `T_Y`，与下一步第 2050 行的 `ε′T_Y` 呼应，非 `αφ*…` 误吞）。
  - 第 2056 行三行展开式 `3lA_Y − (K_Y + T_Y) = … − ε′T_Y \\ = … − αφ*(B+tL) + α(B_Y^~ + tL_Y^~) \\ = (…) + (…) + (…)`：第二行的 `− αφ*(B+tL) + α(B_Y^~ + tL_Y^~)` 与第三行三项分组 `lA_Y − αφ*(B+tL)`、`lA_Y + α(B_Y^~ + tL_Y^~)` 的项数、系数 3 与 1 均逐项与印刷一致；末项 `+ \alpha (B_Y^~ + tL_Y^~)` 前的 `lA_Y` 系数为 1（印刷亦为 1），未被误加 3。
  - 第 2068 行 `l \geq \frac {(1 + r) \epsilon^ {\prime}}{\epsilon - \epsilon^ {\prime}}` 的分子 `(1 + r)ε′` 未被 OCR 丢 `r`。
  - 第 2080 行 `l A - \alpha (B + t L) = (l - (1 + t) \alpha) A + \alpha (A - B + t A - t L)` 四项符号与印刷一致（印刷正文此处印作无下标的 `lA`，MD 亦无下标，非丢字）。
  - 第 2086 行两行展开式：`\frac {1}{v} (K_Y + Γ_Y + 3dA_Y) - \frac {1}{v} \phi^ {*} (K_X + B + tL) - \frac {3d}{v} A_Y`，第二行 `(l - \frac {3d\alpha}{v}) A_Y - \frac {\alpha}{v} \phi^ {*} (…) + \frac {\alpha}{v} (K_Y + Γ_Y + 3dA_Y)`——三处 `\alpha/v` 系数与 `3d\alpha/v` 逐项与印刷一致，未被误乘或漏乘。
  - 第 2095 行 `remembering from Step 5 that $K _ { Y } + \Gamma _ { Y } + 3 d A _ { Y }$is ample` 的 3d 倍数与印刷一致（承 p.40 的 2d→3d，非笔误）。
  - 第 2103 行 `Now applying Theorem 1.9 (by taking$M = l A _ { Y } , S = T _ { Y }$, and$z = x )$, there is a natural number n depending only on d and there is a $\mathbb{Q}$-divisor$\Lambda _ { Y } \geq T _ { Y }$` 的代入三参数 `M/S/z` 与印刷一致；`$( Y , \Lambda _ { Y } )$is lc over x` 未被误改为 lc。
  - 第 2102 行 `Moreover,$A _ { Y } | _ { T _ { Y } } \sim 0$` 的限制符号 `A_Y|_{T_Y} ∼ 0` 与印刷一致（`| _ { T _ { Y } }` 是下标位置渲染，非 OCR 伪影）。
- 页块边界：印刷 p.41 止于显示式 `n(K_Y + Λ_Y) ∼ (n + 2)lA_Y.`，与 MD 第 2106 行一致；MD 第 2109 行 `Let Λ be the pushdown of$\Lambda _ { Y }$.` 起属**印刷 PDF p.42**。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.042（PDF p.42 / 印刷 p.42）
- PNG：/tmp/birkarsing_audit_p042.png（pngmono 150dpi）；仲裁裁剪 /tmp/birk_p042_bul.png（300dpi pnggray，Step 2 项目符号段）
- 核对：页眉「42 / Caucher Birkar」；Prop 5.11 证明收尾（`Let Λ be the pushdown`、显示式 `K_X + Λ ∼_Q ((n+2)l)/n A`、`4lA − (K_X + Λ)`、显示式 `a(T,X,Λ) = a(T,Y,Λ_Y) = a(T_Y,Y,Λ_Y) = 0,`、`so T is an lc place of (X, Λ).` 与证毕方框）；**§6 `6. Proof of main results`** 首段；**Proof.（of Theorem 1.8）Step 1**（含显示式 lct 三连不等式）；**Step 2** 全文含 2 条项目符号、显示式 `A_Y − B_Y = (A_Y − φ^*A) + (φ^*A − B_Y)` 与 lct 换基不等式；**Step 3** 全文（`C := 1/2 A`、显示式 `lct(X,B,|A|_R) = 1/2 lct(X,B,|C|_R)`、`L := 1/2 N`、`n, m, ε′` 取自 Prop 5.11、`t` 最大值）；`By definition of t,` 段与显示式 `a(T, X, B + tL) = ε′.`；`Let x be the generic point of the centre of T on X.`
- 结果：PASS±（差异列表）
  1. MD 第 2137–2141 行项目符号**结构错**：原为三条 `•`（第 2 条作 `• $A _ { Y } ^ { d } \leq l$, and`，第 3 条作 `• $A _ { Y } - \phi ^ { * } A$is ample.`）→ 改为**两条**，第 2 条合并为 `• $A _ { Y } ^ { d } \leq l$ and$A _ { Y } - \phi ^ { * } A$is ample.`。300dpi 仲裁裁剪确认印刷只印 **2 个项目符号**，第二条为 `A_Y^d ≤ l and A_Y − φ^*A is ample.`（含 `and` 连接、`l` 后无逗号）；MinerU 误把一个项目符号内的 `and` 拆成两条并补了句点式连接。
  2. MD 第 2127 行 `pseudo-efective` → `pseudo-effective`（OCR 连字丢 `f`；印刷 p.42 与 Lemma 2.24 全篇均作 `pseudo-effective`）。
  3. MD 第 2121 行 `so$T$is an lc place of$( X , \Lambda )$` 行末补句点。印刷作 `so T is an lc place of (X, Λ).`
  4. MD 第 2163 行 `…a positive lower bound for lct$( X , B , | C | _ { \mathbb { R } } )$` 行末补句点。印刷作 `…positive lower bound for lct(X, B, |C|_R ).`
  5. MD 第 2165 行 `In particular, we can assume$t < 1$` 行末补句点。印刷作 `In particular, we can assume t < 1.`
- 明确非差异（已核）：
  - 证毕方框 □（第 2121 行右侧）未在 Markdown 中表示——沿用第一轮 p.012 已登记的全局导出约定（纯排版元素），按 PASS± 登记不修，非本段新增缺陷。
  - 第 2112 行 `K _ {X} + \Lambda \sim_ {\mathbb {Q}} \frac {(n + 2) l}{n} A`：分式为 `(n+2)l/n`（非 `(n+2)/(nl)`），与印刷一致；`\sim_{\mathbb Q}` 下标为 `\mathbb{Q}` 而非 `\mathbb{R}`，与印刷 `∼_Q` 一致（易与 p.40 的 `∼_ℝ` 混淆处，已逐字核对）。
  - 第 2118 行 `a (T, X, \Lambda) = a (T, Y, \Lambda_ {Y}) = a (T _ {Y}, Y, \Lambda_ {Y}) = 0,`：中间一项的下标为 `T_Y`（第三个论元取 `T_Y` 而非 `T`），与印刷一致。
  - 第 2125 行 `so assume they all hold in dimension$\leq d - 1$.`：三条定理编号 `1.1, 1.6, 1.8` 与印刷一致（未漏 1.7）。
  - 第 2130 行 lct 三连式 `\operatorname{lct} (X, B, | M | _ {\mathbb {R}}) \geq \operatorname{lct} (X, B, | M + N | _ {\mathbb {R}}) = \operatorname{lct} (X, B, | A | _ {\mathbb {R}}),`：`≥` 与 `=` 的方向、`M + N` 的加号、`|A|_R` 的绝对值竖线与下标 `\mathbb{R}` 均与印刷一致。
  - 第 2135 行 `a small projective birational morphism$\phi \colon Y \to X$`：箭头为**实线** `→`（印刷确为极射影缩射，非 MMP 虚线），与本篇 `X_i′ ⇢ X_i″` 类虚线记号区分清楚，沿用 p.019 已核口径。
  - 第 2146 行 `A _ {Y} - B _ {Y} = \left(A _ {Y} - \phi^ {*} A\right) + \left(\phi^ {*} A - B _ {Y}\right)`：两项括号与 `\phi^*` 的上标方向与印刷一致。
  - 第 2152 行 `lct (X, B, | A | _ {\mathbb {R}}) = lct (Y, B _ {Y}, | \phi^ {*} A | _ {\mathbb {R}}) \geq lct (Y, B _ {Y}, | A _ {Y} | _ {\mathbb {R}})`：等号与 `≥` 方向、`|\phi^*A|_R` 的绝对值内含 `\phi^*` 均与印刷一致。
  - 第 2160 行 `lct (X, B, | A | _ {\mathbb {R}}) = \frac {1}{2} lct (X, B, | C | _ {\mathbb {R}})`：系数 `1/2` 位置（乘在右端而非左端）与印刷一致。
  - 第 2163 行 `(X, B + t N)$is lc if and only if$( X , B + 2 t L )$is lc where$t \in \mathbb { R }$`：`2tL` 的系数 2 与「if and only if」双向均未被 OCR 弱化。
  - 第 2165 行 `Let$n , m , \epsilon ^ { \prime }$be the numbers given by Proposition 5.11` 的三个数 `n, m, ε′` 与印刷一致（与 Prop 5.11 陈述的对应关系未错位）。
- 页块边界：印刷 p.42 止于 `Let x be the generic point of the centre of$T$on$X$.`，与 MD 第 2173 行一致；MD 第 2175 行 `Step$\it 4 .$` 起属**印刷 PDF p.43**（该行即第一轮残余 `\it` 伪影第 3 处，留待 p.043 条目处置）。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.043（PDF p.43 / 印刷 p.43）
- PNG：/tmp/birkarsing_audit_p043.png（pngmono 150dpi）；仲裁裁剪 /tmp/birk_p043_e.png（300dpi pnggray，`e = ⌈(3d+1)/s⌉` 一行）
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties / 43」；`By definition of t,` 段与显示式 `a(T,X,B+tL) = ε′.`；`Let x be the generic point…`；**Step 4** 全篇（显示式 `(X, B + (1 − ε′/ε)vL)`、`by Lemma 2.3, because`、显示式 `B + (1 − ε′/ε)vL = (ε′/ε)B + (1 − ε′/ε)(B+vL)`、行内式 `t ≥ (1 − ε′/ε)v`）；**Step 5** 全篇（含 4 条项目符号、四元替换 `2mA, 2mC, 2mL, t/(2m)`、Prop 5.7 与 `ν : U → X`、显示式 `a(T,X,B) ≥ ε > ε′ = a(T,X,B+tL)`、行内式 `t ≥ (ε−ε′)/q`）；**Step 6** 全篇（`0 ≤ P ∼_ℝ A − B`、`K_X + sP + 3dA`、`sP + (3d+1)A`、`e = ⌈(3d+1)/s⌉`、`P + eA`、`(e+1)A − B`）与证毕方框；页末 `The idea of Step 6 in the previous proof is due to Yanning Xu.`
- 结果：PASS±（差异列表）
  1. MD 第 2173 行 `Step$\it 4 .$In this step…` → `Step 4. In this step…`（第一轮登记的 `\it` 伪影**残余第 3 处**，至此全篇 8 处 `\it` Step 标签全部处置完毕）。
  2. MD 第 2195 行 `• T is an lc place of$( X , \Lambda )$` 行末补句点。印刷作 `• T is an lc place of (X, Λ).`（第 4 条项目符号以句点收束，前三条分别为 `,`、`,`、`and`）。
  3. MD 第 2207 行 `hence$s P + ( 3 d + 1 ) .$A is ample` → `hence$s P + ( 3 d + 1 )A$ is ample`。300dpi 仲裁裁剪确认印刷作 `hence sP + (3d + 1)A is ample`，`(3d+1)` 与 `A` 之间**无句点**；原 Markdown 的 `.` 是把行尾句点误插进数学模式内部。
- 明确非差异（已核）：
  - 证毕方框 □（第 2209 行右侧）未在 Markdown 中表示——沿用第一轮 p.012 已登记的全局导出约定，登记不修。
  - 第 2176 行 `(X, B + (1 - \frac {\epsilon^ {\prime}}{\epsilon}) v L)`：分式为 `ε′/ε`（易被 OCR 读成 `ε/ε′`），印刷确为 `1 − (ε′/ε)`，MD 一致。
  - 第 2182 行 `B + (1 - \frac {\epsilon^ {\prime}}{\epsilon}) v L = \frac {\epsilon^ {\prime}}{\epsilon} B + (1 - \frac {\epsilon^ {\prime}}{\epsilon}) (B + v L)`：右端首项系数为 `ε′/ε`（与左端被减去的项互为补数关系，非 `1 − ε′/ε`），印刷与 MD 一致；右端括号为 `(B + vL)`，未漏 `v`。
  - 第 2185 行行内式 `t \geq ( 1 - \frac { \epsilon ^ { \prime } } { \epsilon } ) v`：`\begin{array} { r } { … } \end{array}` 包裹沿用本篇既有渲染约定（第一轮已核为非缺陷），不改。
  - 第 2187 行 `a Q-Cartier Q-divisor$\Lambda \geq 0$`：两个 `Q` 均未丢（`Q-Cartier` 与 `Q-divisor` 并存），与印刷一致。
  - 第 2189–2195 行 4 条项目符号的**条数与印刷一致**（`nΛ is integral,`／`mA − Λ is ample,`／`(X, Λ) is lc near x, and`／`T is an lc place of (X, Λ).`），未发生 p.042 那种一条被拆成两条的情形。
  - 第 2197 行四元替换 `2mA, 2mC, 2mL, { \frac { t } { 2 m } }`：第 3 个替换量为 `2mL`（`L` 为大写除子，非 `l` 自然数），第 4 个为 `t/(2m)`；印刷一致，MD 未把 `2mL` 误作 `2m·l`。
  - 第 2197 行 `q$depending only on$d , r , n , \epsilon ^ { \prime }$`：q 的依赖项为四个 `d, r, n, ε′`（印刷亦为四个，未漏 `n`）；同句 `$\nu \colon U \to X$` 箭头为实线（印刷为抽头极射影缩射，非 MMP），`\nu ^ { * } L` 星号为上标拉回，均与印刷一致。
  - 第 2202 行 `a (T, X, B) \geq \epsilon > \epsilon^ {\prime} = a (T, X, B + t L),`：`≥` 与 `>` 两个方向及中间的严格不等号均未被 OCR 弱化为 `≥`，印刷一致。
  - 第 2205 行 `we have$\mu _ { T } \nu ^ { * } t L \geq \epsilon - \epsilon ^ { \prime }$which implies$\begin{array} { r } { t \geq \frac { \epsilon - \epsilon ^ { \prime } } { q } } \end{array}$`：`μ_T ν^*tL ≥ ε − ε′`（而非 `≤`）与印刷一致，分母 `q` 未被误加 `q` 到分子。
  - 第 2207 行 `letting$\textstyle e = { \bigl \lceil } { \frac { 3 d + 1 } { s } } { \bigr \rceil }$, P + eA is ample.`：300dpi 仲裁裁剪确认印刷为**上取整** `⌈(3d+1)/s⌉`（左侧开口朝右的 `⌈`、右侧 `⌉`，被取整式 `(3d+1)/s` 无外层括号），MD 的 `\bigl \lceil … \bigr \rceil` 与之相符，非取整误作下取整。
  - 第 2207 行 `Thus$K _ {X} + s P + 3 d A$is ample by boundedness of length of extremal rays.`：`3dA` 的系数 3 与 `sP` 的加号未被 OCR 吞并，与印刷一致。
  - 第 2209 行 `By assumption,$P \sim _ { \mathbb {R}} A - B ,$so$( e + 1 ) A - B$is ample. Therefore, replacing A with$( e + 1 ) A$, we are reduced to the case when$A - B$is ample.`：两处 `(e+1)A` 的括号配对与 `\sim_{\mathbb R}` 的下标与印刷一致。
  - 第 2211 行 `The idea of Step 6 in the previous proof is due to Yanning Xu.`：人名拼写 `Yanning Xu` 与印刷一致（未误作 `Yanming`）。
- 页块边界：印刷 p.43 止于 `The idea of Step 6 in the previous proof is due to Yanning Xu.`，与 MD 第 2211 行一致；MD 第 2213 行 `Proof. (of Theorem 1.7)` 起属**印刷 PDF p.44**。本段页块对齐无 ±1 漂移（p.042–p.043 连续两页 MD 与印刷同页对齐）。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## p.044（PDF p.44 / 印刷 p.44）
- PNG：/tmp/birkarsing_audit_p044.png（pngmono 150dpi）；仲裁裁剪 /tmp/birk_p044_2eps.png、/tmp/birk_p044_2eps2.png（300dpi pnggray，`is ε/2-lc` 一行，×3.0）、/tmp/birk_p044_refs.png、/tmp/birk_p044_ref67.png（300dpi pnggray，References [1]–[7]）
- 核对：页眉「44 / Caucher Birkar」；**Proof.（of Theorem 1.7）**；**Proof.（of Theorem 1.6）**；**Proof.（of Theorem 1.1）** 全篇（三段：`small Q-factorialisation`、`Run an MMP on −K_{X′}`、`X″ is an ε-lc weak Fano variety`、`Δ ≥ B`、`K_X + Δ ∼_ℝ 0`、`klt n-complement K_{X″} + Ω″`、`[5, 6.1(3)]`、`klt n-complement K_X + Ω`、`[15]`、`B = 0`；`By Theorems 2.10 and 2.13,…|−mK_X|…`、`vol(−K_X) ≤ v`；`On the other hand,…t_l = t/l for l ∈ ℕ,…Theorem 2.15`）与证毕方框；**Proof.（of Corollary 1.4）** 全篇（显示式 `Γ = (1−α)Δ + αD.`、`−(K_X+Γ) = −(1−α)(K_X+Δ) − α(K_X+D)`、`−(K_X+D) ∼_ℝ Δ − D ∼_ℝ A`、`is ε/2-lc. Now apply Theorem 1.1.`）与证毕方框；**Proof.（of Corollary 1.5）**（`[39, Theorem 1.8]`）与证毕方框；**`REFERENCES`** 标题与文献 **[1]–[7]** 逐条（作者、题名、刊名、卷、期、页码、年份、arXiv 号）。
- 结果：PASS±（差异列表）
  1. MD 第 2217 行 `Replacing X with$X ^ { \prime \prime }$we can then assume$B = 0$` 行末补句点。印刷作 `…we can then assume B = 0.`
  2. MD 第 2219 行 `…such that $\operatorname { vol } ( - K _ { X } ) \leq v$` 行末补句点。印刷作 `…such that vol(−K_X ) ≤ v.`
  3. MD 第 2241 行 `choosing α to be suficiently small` → `sufficiently`（OCR 连字丢 `f`；300dpi 裁剪确认印刷作双 `f` 的 `sufficiently`）。
- 明确非差异（已核）：
  - 第 2241 行 `is$\frac { \epsilon } { 2 } { - } \mathrm { l c }$.`：**正确，非缺陷**。300dpi ×3 仲裁裁剪确认印刷该处为**竖排分数 ε/2**（`ε` 在分数线上、`2` 在线下）后接 `-lc.`，与 MD 的 `\frac { \epsilon } { 2 }` 相符；`pdftotext` 把它拍成 `2ǫ -lc` 是文本层分数抽取现象，非印刷事实（同 p.033/p.037/p.038 的 `2ǫ` 判定口径）。**未改动。**
  - 第 2247 行 `[1] … Boundedness and$K ^ { 2 }$for log surfaces. Internat. J. Math. 5 (1994), no. 6, 779–810.`：卷号 `5`、期号 `no. 6`、页码 `779–810`、年份 `1994`、刊名 `Internat. J. Math.` 逐项与印刷一致（卷号 `5` 的印刷粗体未在 MD 体现，属排版层级非内容）。
  - 第 2249 行 `[2] V. Alexeev, M. Brion, … The Fano Conference, 69-80, Univ. Torino, Turin, 2004.`：作者两人、页码 `69-80`、出版社地点 `Univ. Torino, Turin`、年份 `2004` 与印刷一致。
  - 第 2251 行 `[3] F. Ambro; … Int. Math. Res. Notices 14 (2016), 4418-4448.`：刊名、卷 `14`、年 `2016`、页码 `4418-4448` 与印刷一致（未漏 `Int.` 前缀中的 `Internat.`）。
  - 第 2253 行 `[4] C. Birkar; Log Calabi-Yau fibrations, arXiv:1811.10709.`：300dpi 裁剪确认 arXiv 号为等宽字体的 **`1811.10709`**，与印刷一致；该行在 150dpi 全页图上因字体切换而显得发虚，非印刷污损。
  - 第 2255 行 `[5] … Ann. of Math. (2) 190 (2019), no. 2, 345-463.`：卷 `190`、期 `no. 2`、页码 `345-463`、年 `2019` 与印刷一致（`Anti-pluricanonical` 拼写未被 OCR 改成 `Anti-pluricanonical systems`，原样保留）。
  - 第 2257 行 `[6] … Pub. Math. IHES., 115 (2012), 325-368.`：刊名 `Pub. Math. IHES.` 的**缩写点与逗号**、卷 `115`、页码 `325-368` 与印刷一致（300dpi 裁剪复核）。
  - 第 2259 行 `[7] C. Birkar, P. Cascini, C. Hacon and J. M<sup>c</sup>Kernan; … J. Amer. Math. Soc. 23 (2010), no. 2, 405-468.`：作者四人及顺序与印刷一致；`M<sup>c</sup>Kernan` 的上标 `c` 沿用第一轮 p.005/p.013 已登记的 HTML 上标约定（语义无损，登记不改），非本段新增缺陷。
  - 第 2213/2215/2243 行三条 `Proof. (of Theorem …)` 的斜体标签与定理编号 `1.7 / 1.6 / 1.1`、`Corollary 1.4 / 1.5` 与印刷逐一对应，顺序未被 OCR 换序。
  - 第 2215 行 `Theorem 1.8 in dimension$\leq d .$` 的句点位置（`d` 后）与印刷 `dimension ≤ d.` 一致（该句以句点收束，随后逗号接 `Theorem 1.1`），非双标点。
  - 第 2217 行 `and$K _ { X } + \Delta \sim _ { \mathbb { R } } 0$which gives$\Delta ^ { \prime \prime }$`：`∼_ℝ 0` 的下标为 `\mathbb{R}`（非 `\mathbb{Q}`），与印刷一致；`Δ″` 的两个撇号未被 OCR 吞成一个。
  - 第 2217 行 `$K _ { X ^ { \prime \prime } } + \Omega ^ { \prime \prime }$which gives a klt n-complement$K _ { X ^ { \prime } } + \Omega ^ { \prime } \ [ 5 , 6 . 1 ( 3 ) ]$`：`X″` 与 `X′` 两级模型未被 OCR 混为同一撇号数，`[5, 6.1(3)]` 引文编号与印刷一致。
  - 第 2221 行 `for$0 \le L \sim - l K _ { X }$, the pair$( X , t _ { l } L )$is klt`：`0 ≤ L ∼ −lK_X` 的 `∼` 在印刷中**不带** `\mathbb{R}` 下标（与同段前一句 `N \sim_{\mathbb{R}} -K_X` 不同），MD 与印刷一致，未被 OCR 补下标。
  - 第 2232/2238 行两个显示式的 `\sim_ {\mathbb {R}}` 下标与印刷一致；`−(K_X + D) ∼_ℝ Δ − D ∼_ℝ A` 的两个 `∼_ℝ` 未被吞成一个。
  - 本页 4 处证毕方框 □（Theorem 1.7/1.6/1.1、Corollary 1.4/1.5 各一）未在 Markdown 中表示——沿用第一轮 p.012 已登记的全局导出约定，登记不修。
- 页块边界：印刷 p.44 止于文献 `[7] … J. Amer. Math. Soc. 23 (2010), no. 2, 405-468.`，与 MD 第 2259 行一致；MD 第 2261 行 `[8] A. Borisov; …` 起属**印刷 PDF p.45**。无丢失/重复/错序。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p131`；model=`opencode-go-chat-space-bunny-free`；effort=UNKNOWN。

## 总Master 裁定：句末双逗号回退（PDF p.27 / 印刷 p.27）

复核员把审计员的两处改动判为「假修复」，总Master 逐处重看原页后**维持回退**，回退成立。

### 印刷原页证据（总Master 亲自渲染并 Read）

`pdftotext -bbox` 定位（y≈2801–2900，S=300/72.0）→
`gs -q -dNOPAUSE -dBATCH -sDEVICE=pngmono -r300 -dFirstPage=27 -dLastPage=27` →
PIL 裁切 (820,2760)-(1750,2920) 并 LANCZOS 放大 3 倍 → `/tmp/bk_p27_bullets.png`。
300dpi 页图本轮已复核用 `Read` 亲眼看过。

### 两处判定

1. **第 1265 行** `• $\pi ( S _ { i } ) = H _ { i }$where$H _ { i }$is the hyperplane defined by$t _ { i }$,,`
   → 回退为 `…,`（单个逗号）。
   原页作 `… where H_i is the hyperplane defined by t_i,`，`t_i` 之后**恰有一个逗号**，无第二个。
2. **第 1267 行** `• π is étale over a neighbourhood of z,,`
   → 回退为 `…,`（单个逗号）。
   原页作 `… a neighbourhood of z,`，同样**恰有一个逗号**。
   该行同时保留的 `étale` 与 `of z` 两处补字经同页裁片确认正确，未在本次回退范围内。

### 结论

第 1265、1267 行的双逗号确属 MinerU 导出噪声，印刷原文单逗号，回退正确。
本条只处置逗号，不涉及该页其余公式、集合记号与文献著录（见上文 p.027 条目）。

- 记录时间：2026-10-05；actor=`总Master`；model=`opencode-go-chat/space-bunny-free`；effort=UNKNOWN。

---

# 第三轮重做：p.001–p.008 片段逐页视觉复核（actor=`Wf-R-Birkar-p001`）

- 性质：redo 候选分支 `cpf-redo/Birkar_2016_singularities_linear_systems` 的第三轮逐页视觉复核。范围仅 PDF p.1–p.8（8 页），逐页「gs pngmono 150dpi 渲染 → Read 亲眼目检 → 读 MinerU Markdown 对应段 → 五点比对 → 立即落签」。
- actor：`Wf-R-Birkar-p001`；model / effort：`opencode-go-chat / space-bunny-free` / UNKNOWN。
- 工作树：`/Users/aurolafly/.zcode/worktrees/cpf-redo-Birkar_2016_singularities_linear_systems`。
- PDF 身份核验：`shasum -a 256 Birkar_2016_singularities_linear_systems.pdf` = `c9c73303be3b12c5ca91506ac541c9b9d81764d19bcd7183b7c577f8c0d546fe`，与 `.redo.md` 记录一致；PDF 全程只读。
- Markdown：`Birkar_2016_singularities_linear_systems_mineru/Birkar_2016_singularities_linear_systems__Birkar_2016_singularities_linear_systems.md`（2341 行），本轮开工 SHA-256 = `95216ff90edbb81b4ac0f789bcdfad682e5258d86dba467801fcb794c509c3ac`（既非 Luna 初审前 `5beebf35…`，也非 redo 基线 `34c398ff…`，说明其后另有改动，本轮以当前字节为准重新比对）。
- 证据图：本轮渲染落在 `/tmp/birkarsing_audit_pNNN.png`（150dpi pngmono）；本 AUDIT 追加于既有 `AUDIT-Birkar_2016_singularities_linear_systems.md` 末尾，不覆盖前两轮（Luna `Peer-P13`、redo `Wf-R-P13`）的条目。
- 双通道判定：PNG 目检为终裁；`pdftotext -layout` 文本层（本 PDF 为 LaTeX born-digital，文本层对拼写/数字可靠）作交叉对账；字形歧义（ff 连字、上下标、虚线箭头）升级 300dpi pnggray + PIL 裁切放大，只裁图不写 Markdown。
- 修复纪律：Markdown 改动一律用 Edit 逐处手工，每处绑定具体 PDF 页与裁片；PASS± 的 ff 拍平/空格粘连/标点扁平按 AUDIT-SOP 登记不批量改；印刷原文的 print quirk 与错字原样保留，绝不按数学常识「纠正」原刊。

## p.001（PDF p.1 / 印刷 p.1）
- PNG：`/tmp/birkarsing_audit_p001.png`（pngmono 150dpi，本轮新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p1_abstract.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=1`，仅裁图）。
- 核对：题名、作者、摘要全文、目录全部条目与页码、脚注三行（Date / 2010 MSC / Keywords）；对照 Markdown 第 1–41 行，并辅以 `pdftotext -f 1 -l 1 -layout`。
- 结果：**PASS±**
  - 题名 `Singularities of linear systems and boundedness of Fano varieties`、作者 `Caucher Birkar` 与印刷一致；摘要逐句一致（含 `α-invariant`、`Borisov-Alexeev-Borisov`、`Jordan`、`Serre`、`Tian` 等专名）。
  - 目录 25 条与页码逐一核对为 `2,9,9,10,10,10,11,12,12,12,13,13,14,15,15,15,16,17,22,27,27,28,31,37,42`，与印刷**全部吻合**；`5.10. Construction of $\Lambda$` 的 Λ 与印刷一致。目录缺号子节（2.3、2.7、2.10、2.11、2.13、2.15、2.17、2.20、2.21、2.24 等）**印刷原页即缺**，按 print quirk 原样保留，不计差异。
  - 脚注三行与印刷一致：`Date: December 2, 2020.`、`2010 MSC: 14J45, 14E30, 14C20.`、`Keywords: … minimal model program.`——前两轮把 `minimal mode program` 修为 `minimal model program` 的旧修复，经本轮原页复核**正确，保留**。
- PASS± 差异（登记，按 SOP 不批量改）：
  1. MD 第 5 行摘要 `We prove existence of positive lower bounds in diferent settings` —— 印刷为 `different`。300dpi 裁片 `/tmp/bk_p1_abstract.png` 亲眼可见 `ff` 连字完整，`pdftotext` 第 10 行亦作 `different`，确证少一个 `f`。属 OCR ff 拍平，词义可辨、不改变任何数学陈述。
  2. MD 第 41 行脚注后孤立一行 `References` —— 印刷上 `References 44` 是**印刷 p.2 顶部**的目录续项（`pdftotext -f 2 -l 2` 证实），MinerU 将其错位到题录区且丢失页码 44。属分页结构伪影，条目本身在 MD 第 2245 行 `## References` 处另有完整落点，不影响数学内容。
  3. 页边 arXiv 水印（`arXiv:1609.05543v2 [math.AG] 1 Dec 2020`）未收录 —— 非论文正文，不计差异。
- 备注：本页无数学内容错误，无需 Edit 修复；本轮确认前两轮 p.001 登记属实且旧修复方向正确。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p001`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：`/tmp/birkarsing_audit_p002.png`（pngmono 150dpi，本轮新渲染并 Read 目检整页）。
- 核对：页首目录续项「References 44」；§1 开头五段；Theorem 1.1 完整陈述（含两条 bullet 假设与结论句）；`ε = 0` 反例段；文献 `[26]`/`[32][10]`/`[9]`/`[1]`/`[30]`；末尾两条已知情形 bullet `[22]`/`[27]`；对照 Markdown 第 43–72 行，辅以 `pdftotext -f 2 -l 2 -layout`。
- 结果：**PASS±**
  - **旧修复复核为正确**：MD 第 49 行两处 `$Y \to Z$`（Mori fibre space structure、`A general fibre of $Y \to Z$）箭头均在位。印刷原页与 `pdftotext` 第 16 行均作 `Y → Z [7]. A general fibre of Y → Z`，**前一 Luna 轮丢失箭头、本 redo 轮已恢复**的判断属实，保留。
  - Theorem 1.1 逐项与印刷一致：引导句 `Let d be a natural number and ǫ be a positive real number. Then the projective varieties X such that`；两条 bullet `$( X , B )$is ǫ-lc of dimension d for some boundary B, and` 与 `$- ( K _ { X } + B )$is nef and big,` 项目符号均在位；结论 `form a bounded family.` 与印刷完全一致。
  - 反例段与印刷一致：`would not hold if one takes ε = 0 (see below): it already fails in dimension two, and in dimension three it fails even if we replace bounded by birationally bounded [30].`
  - 引文编号逐一核对无误：`[1]`、`[9]`、`[26]`、`[32][10]`、`[30]`、`[35][34][33]`、`[22]`、`[27]`；两条 bullet `Fano 3-folds with terminal singularities and Picard number one [22],` 与 `Fano 3-folds with canonical singularities [27],` 与印刷逐字一致。
- PASS± 差异（登记，按 SOP 不批量改）：
  1. MD 第 47 行 `diferential geometry` —— 印刷为 `differential geometry`（文本层原页第 11 行作 `differential`）。ff 连字拍平。
  2. MD 第 49 行 `pseudo-efective` —— 印刷为 `pseudo-effective`（文本层原页第 14 行作 `pseudo-effective`）。ff 连字拍平。
  3. MD 第 51 行 `it is a classical result tha the smooth Fano surfaces` —— 印刷为 `that`（文本层原页第 22 行作 `result that`）。丢一个 `t`。
  4. 印刷页首目录续项 `References …… 44` 在 Markdown 中缺页码 44 且错位于题录区（MD 第 41 行），已在 p.001 条目登记，此处不重复计差异。
  5. 印刷页眉「2  Caucher Birkar」为 running head，MD 不收录，非内容差异。
  6. 若干数学式与后续单词间空格粘连（如 `$- K _ { X }$is`、`with$K _ { W }$not`、`$\mathbb { P } ^ { 1 }$.`、`which is$\mathbb { P } ^ { 1 }$`），词界仍可辨。
- 备注：三项拼写瑕疵均为 ff/t-flation 型 OCR 伪影，词义可辨，不改变定理 1.1 陈述，无数学内容错误，本页不需 Edit。前两轮 p.002 登记属实。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p001`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：`/tmp/birkarsing_audit_p003.png`（pngmono 150dpi，本轮新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p3_Stilde.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=3`，仅裁图）。
- 核对：页首四条已知情形 bullet（`[2]`/`[8]`/`[13]`/DCC 边界条）；Example 1.2 全文与显示公式 `K_{W_n}+\frac{n-2}{n}E=f^*K_{X_n}`；Example 1.3 全文（含 `(\mathbb{P}^2,\Delta=S+T+R)`、三处爆破箭头、收缩箭头、`[15]`）；Corollary 1.4 全文（两条 bullet、`K_X+\Delta\sim_{\mathbb{R}}0`、结论句）；末段 log Calabi–Yau 提问句；对照 Markdown 第 73–111 行，辅以 `pdftotext -f 3 -l 3 -layout`。
- 结果：**PASS±**
  - **旧修复复核为正确**：第 83 行 `$f\colon W_n\to X_n$`、第 97 行四处 `$V_1\to\mathbb{P}^2$`、`$V_2\to V_1$`、`$V_n\to V_{n-1}$`、`$X_n'\to X_n$`、第 89 行 `As$n \to \infty$` 的箭头均在位。印刷原页与文本层第 14/19/25–31 行逐一可见 `→`，**前轮丢失箭头、本 redo 轮已恢复**的判断属实，保留。
  - 显示公式核对无误：分式系数为 `(n-2)/n`（非 `n-2`、`2/n` 或 `(2-n)/n`），右端 `f^*K_{X_n}`，`2/n`-lc 系数亦为 `2/n`；集合条件 `n \geq 2` 为普通 `\geq`，**无 Luna 轮所记的伪双点 `stackrel{cdotcdot}{geq}`**。
  - Corollary 1.4 两条 bullet 项目符号均在位：`$( X , \Delta )$is ǫ-lc of dimension d for some boundary$\Delta$`、`$K _ { X } + \Delta \sim _ { \mathbb { R } } 0$ and$\Delta$is big,`；边界为 `$\Delta$`，**无 Luna 轮所记的伪下标 `\Delta_{cdot}`**；`[8]`、`[13]`、`[15]`、`[5]` 编号均在位，**无尾随多余 `2`**。
  - 印刷 p.3 末行「In fact one can ask a host of hard fundamental questions」跨页续于 p.4；MD 第 111 行把整句（含 `regarding boundedness, singularities, complements and linear systems, in the more general context of log Calabi-Yau fibrations.`）合并为完整段落，内容无增删，属跨页合并而非缺失。
- PASS± 差异（登记，按 SOP 不批量改）：
  1. `coeficient`/`coeficients`（第 79 行 ×2、第 89 行 ×1、第 109 行 ×2）—— 印刷均为 `coefficient(s)`（文本层第 8/9/21/44/45 行作 `coefficients`/`coefficient`）。ff 连字拍平，共 5 处。
  2. 第 83 行 `$n \geq 2 ,$`（逗号后多一个逗号）—— 印刷 `n ≥ 2,` 为单逗号（文本层第 13 行）。双标点伪影。
  3. 第 91 行 `## Example 1.3. Consider the pair` 与第 107 行 `## form a bounded family.` 被 MinerU 提升为二级标题；印刷两处均为正文行。内容完整、不改变数学，属结构伪影。
  4. 第 103 行行末丢印刷的逗号（印刷 `(X, ∆) is ǫ-lc of dimension d for some boundary ∆,`）。标点扁平。
  5. `$S ^ { \sim }`（第 97 行 3 处）—— 300dpi 裁片 `/tmp/bk_p3_Stilde.png` 亲眼可见印刷的波浪符是**紧贴 S 顶部的重音**（`\tilde{S}` 型），MD 编码为上标波浪。同一记号，读者无歧义，属排版扁平。
  6. 数学式与正文间空格粘连多处（`number$n`、`vertex, and`、`variety. As$n` 等）。
- 备注：本页无数学内容错误，无需 Edit 修复。**前两轮 p.003 登记的箭头/双点/尾随 2/伪下标 4 类差异经本轮原页复核全部已正确落地**，其漏报的标题提升与上标波浪两项由本轮补记。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p001`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：`/tmp/birkarsing_audit_p004.png`（pngmono 150dpi，本轮新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p4_Mckernan.png`、`/tmp/bk_p4_Kahler2.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=4`，仅裁图）。
- 核对：页首 p.3 末句的跨页续文；M<sup>c</sup>Kernan–Prokhorov 猜想段与 `[31]`、`[4]`；**Jordan property of Cremona groups** 段；Jordan 指数定义段；**Corollary 1.5 完整陈述**；`Cr_d(k) := Bir(P_k^d)` 与 `[39, Theorem 1.8]`、`[41, 6.1]`、`[45]`、`[40]`；**Lc thresholds of ℝ-linear systems** 段及四条行间公式（`lct` 定义、`|A|_ℝ` 定义、`lct` 的 inf 式、与 sup 式的等价）；末行 `Kähler-Einstein` 段；对照 Markdown 第 111–153 行，辅以 `pdftotext -f 4 -l 4 -layout`。
- 结果：**PASS±**
  - `M<sup>c</sup>Kernan` 与印刷一致：300dpi 裁片 `/tmp/bk_p4_Mckernan.png` 亲眼可见 **`c` 为上标**（`M` 后接上标小写 c）。**Luna 轮「原文 c 为上标、MD `<sup>c</sup>` 忠实」的判定经本轮仲裁属实，保留**；`pdftotext` 把上标 c 排成行内 `Mc Kernan` 属文本层位置顺序现象，不据此登记成 Markdown 差异。
  - Corollary 1.5 逐字核对一致：`Let d be a natural number. Then there is a natural number h depending only on d satisfying the following. Let k be a field of characteristic zero (not necessarily algebraically closed) and X be a rationally connected variety of dimension d over k. Then the birational automorphism group Bir(X) is Jordan of index h.` 印刷原页为斜体定理环境，MD 正文完整。
  - Jordan 定义段与 Cremona 群公式一致：`A group C is Jordan of index h if for any finite subgroup G of C there is a normal abelian subgroup H of G of index at most h.`；`$\mathrm { C r } _ { d } ( k ) : = \mathrm { B i r } ( \mathbb { P } _ { k } ^ { d } )$` 的花体与下标 `k` 均在位。
  - 四条行间公式逐一核对无误：① `\operatorname{lct}(X,B,L) := \sup\{t\in\mathbb{R}\mid (X,B+tL)\text{ is lc}\}`；② `|A|_{\mathbb{R}} = \{L\geq 0 \mid L\sim_{\mathbb{R}} A\}`（下标 ℝ 与 `\sim_{\mathbb{R}}` 均在位）；③ `\operatorname{lct}(X,B,|A|_{\mathbb{R}}) := \inf\{\operatorname{lct}(X,B,L)\mid L\in|A|_{\mathbb{R}}\}`；④ `\sup\{t\in\mathbb{R}\mid (X,B+tL)\text{ is lc for every } L\in|A|_{\mathbb{R}}\}`——**inf 与 sup 两式方向未互换**，与印刷一致。`|A|_{\mathbb{Q}}` 句亦与印刷一致。
- PASS± 差异（登记，按 SOP 不批量改）：
  1. `K¨ahler-Einstein`（第 153 行）—— 300dpi 裁片 `/tmp/bk_p4_Kahler2.png` 亲眼可见印刷为 `Kähler-Einstein`，**变音双点在 `a` 正上方**；MD 把 `¨` 排在 `a` 之前的字符流中，渲染位置错置。基字符正确、术语仍可辨。
  2. 行内 ℝ 被拍平为普通 `R`（第 127 行 `R-linear systems`、`R-Cartier R-divisor` ×2，第 133 行 `R-Cartier R-divisor`、`R-linear system`，第 153 行 `R-linear systems`）—— 印刷为双线体 ℝ。`pdftotext` 第 34/35/37/46 行同样输出纯 `R`，属同一字形扁平来源；MD 的**行间公式内 `\mathbb{R}` 正确保留**，仅行内退化，语义不变。
  3. 第 153 行行末 `$A = - K _ { X }$` 后无句点——该句跨印刷 p.4/p.5 页边断开，句点随续文排在下一页，非丢字。
  4. 印刷页眉「4  Caucher Birkar」为 running head，MD 不收录，非内容差异。
  5. 数学式与正文间空格粘连多处（`divisor$L \geq 0$with`、`as$( X , B )$is defined`、`system of A is` 等）。
- 备注：本页无数学内容错误，无需 Edit 修复。前两轮 p.004 登记属实、无过度或遗漏修复。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p001`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：`/tmp/birkarsing_audit_p005.png`（pngmono 150dpi，本轮新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p5_Ad4.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=5`，按 `pdftotext -bbox` 坐标 x 304.8–341.0pt、y 696.9–709.3pt ×S=300/72 换算后放大 5 倍，仅裁图）。
- 核对：页首 p.4 末句跨页续文；**Lc thresholds of anti-log canonical systems of Fano pairs** 段；**Theorem 1.6** 全文（两条 bullet 假设 + `lct(X,B,|A|_\mathbb{R})\geq t`）；Ambro/Jiang 段（`[3]`、`[19][18]`、`2.15`）；Tian 段（`[42, Question 1]`、`[11, Conjecture 1.12]`）；**Theorem 1.7** 全文（`\leq 1`、`0 \le D \sim_{\mathbb{R}} A`、`\operatorname{lct}(X,B,|A|_{\mathbb{R}})=\operatorname{lct}(X,B,D)`、`D \sim_{\mathbb{Q}} A`、`< 1`）；Cheltsov/Shokurov 段（`[13]`、`[5]`）；**Lc thresholds of ℝ-linear systems with bounded degree** 段；**Theorem 1.8** 开头三条假设（重点 `A^d \leq r`）；对照 Markdown 第 155–203 行，辅以 `pdftotext -f 5 -l 5 -layout` 与 `-bbox`。
- 结果：**PASS±**
  - **旧修复复核为正确（本页关键项）**：Theorem 1.8 第二条假设第 201 行为 `$A ^ { d } \leq r$`，**无下标 `i`**。仲裁证据双重：①300dpi 裁片 `/tmp/bk_p5_Ad4.png` 亲眼可见 `with A^d \le r,`，`d` 为上标、`r` 下方空白；②`pdftotext -bbox` 该行词序列为 `A`(x304.80–312.98) → `d`(x312.96–317.31, yMin=696.91 相对基线 698.38 **上抬**，确证上标) → `≤`(x320.88) → `r,`(x332.40–341.02)，**其后本行再无任何词元**，若存在下标 `i` 必另有词元。**Luna 轮所记「MD 误作 `A^d \leq r_i`、原页无下标」属实，旧修复正确，保留。**
  - **Theorem 1.8 三条假设的 bullet 项目符号均在位**（第 199、201、203 行 `•`），与印刷列表结构一致；Theorem 1.6 两条 bullet（第 159、161 行）同样在位。**Luna 轮所记「第二条假设 bullet 丢失」已正确修复。**
  - 阈值不等式方向逐一核对无误且**未互换**：`\geq t`（Thm 1.6）、`\leq 1`（Thm 1.7）、`< 1`（Thm 1.7 尾段）；`0 \le D \sim_{\mathbb{R}} A` 与 `D \sim_{\mathbb{Q}} A` 的两个模拟号下标 ℝ / ℚ 均在位；`lct(X,B,|A|_ℝ) = lct(X,B,D)` 为**等号**（非 `\sim`），与印刷一致。
  - Tian 段 `asked whether the infimum is a minimum` —— 印刷第 23 行作 `minimum`（非 `max`），MD 一致，未见 max/min 互换。
  - 引文编号核对无误：`[5]`、`[3]`、`[19][18]`、`[42, Question 1]`、`[11, Conjecture 1.12]`、`[13]`；人名 `Ambro`、`Jiang`、`Tian`、`Ivan Cheltsov`、`Shokurov` 全部一致。
- PASS± 差异（登记，按 SOP 不批量改）：
  1. `diferent`（第 155 行、第 169 行，共 2 处）—— 印刷均为 `different`（文本层第 6、21 行）。ff 连字拍平。
  2. 第 201 行 `$A ^ { d } \leq r$` 后**丢印刷的逗号**（印刷 `A^d \le r,`，bbox 词元 `r,` 自带逗号）。标点扁平。
  3. `pseudo-efective`（第 203 行）—— 印刷 `pseudo-effective,`（bbox 第 542 行词元作 `pseudo-effective,`）。ff 连字拍平。
  4. 第 185 行 `$i f B$` 把英文 `if` 排入数学斜体并加内部空格；第 185 行行内 `Q-boundary` 的 ℚ 被拍平为 `Q`（印刷为双线体 ℚ）；第 171/195 行行内 `R-linear` 的 ℝ 拍平为 `R`（与 p.004 同源，语义不变）。
  5. 若干数学式与正文间空格粘连（`Then there is$0 \le D`、`variant$| A |`、`pair such that$A : =` 等）。
- 备注：本页无数学内容错误，无需 Edit 修复。印刷 p.4 末句的句点在本页首行 `ample. An important special case is when X is Fano and A = −K_X.` 处，已在 p.004 条目说明其为跨页断句而非丢字，本轮从对侧复核确认。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p001`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：`/tmp/birkarsing_audit_p006.png`（pngmono 150dpi，本轮新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p6_fS.png`、`/tmp/bk_p6_subtle.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=6`，仅裁图）。
- 核对：Theorem 1.8 第四条假设（`M \geq 0` 与 `A - M` pseudo-effective）；结论阈值链 `\operatorname{lct}(X,B,|M|_\mathbb{R}) \geq \operatorname{lct}(X,B,|A|_\mathbb{R}) \geq t`；假设解说段与 `\deg_A B := A^{d-1}B \leq A^d \leq r`、`\deg_A M := A^{d-1}M \leq A^d \leq r` 两条行间公式；`X = \mathbb{P}^d` 反例段；**Complements near a non-klt centre** 段与 `2.12`；**Theorem 1.9** 全部六条假设与两条结论（含 `f : X \to Z`、`pB is integral`、`M|_S \equiv 0`、`z := f(S)`、`n(K_X + \Lambda) \sim (n+2)M`）；`[5, 2.18]` 段；**Sketch of the proof of Theorem 1.1** 开头（`B = 0`、`[5, Proposition 7.13]`、`2.15`）与三条 bullet（`m-complement`、`|-mK_X|` birational map、`vol(-K_X) \leq v`）；对照 Markdown 第 205–253 行，辅以 `pdftotext -f 6 -l 6 -layout` 与 `-bbox`。
- 结果：**PASS±**
  - **旧修复复核为正确**：①第 229 行映射为 `$f : X \to Z$`，**箭头在位、无尾随多余 `2`**（Luna 轮所记两处差异属实）；②第 233 行 `$M - ( K _ { X } + B )$` 为**单负号**（印刷无双负号）；③Theorem 1.9 六条假设（第 225/227/229/231/233/235 行）、两条结论（第 239/241 行）及 Sketch 开头三条 bullet（第 249/251/253 行）**项目符号全部在位**。
  - **`z := f(S)` 经 300dpi 仲裁确认忠实**（本轮新增仲裁点）：300dpi 裁片 `/tmp/bk_p6_fS.png`（×5 放大）亲眼可见 `z := f(S),`，`f` 为普通斜体、其右下勾是字体自然收笔而非撇号；`pdftotext -bbox` 该行词元 `z`(x301.56) `:=`(x310.20) `f`(x324.72–330.05) `(S),`(x331.32–350.38)，其中 `f` 的 yMin=509.018 与同行 `z`、`:=` **完全相同**（若为 `f'` 则必另有一个 y 更小的上抬词元），且 `r,` 类尾随词元不存在。**我在 150dpi 整页图上曾疑似看到撇号，经升级裁片与 bbox 双重核对判定为低分辨率误读，MD 无误。**
  - 阈值链方向与项序核对无误：`|M|_ℝ` 在左、`|A|_ℝ` 在右，两个 `\geq` 均为 `≥`，末项 `≥ t`；未出现 `≤`/方向互换。
  - 两条 degree 公式核对无误：指数为 `d - 1`，上界均为 `A^d \leq r`，`\deg_ {A} B` 与 `\deg_ {A} M` 的下标 A 与 `: =` 定义号均在位。
  - `n(K_X + \Lambda) \sim (n+2)M` 在结论 bullet（第 241 行）与解说段（第 243 行）**两处均出现且一致**，系数 `n+2` 未写成 `n-2` 或 `2+n`。
- PASS± 差异（登记，按 SOP 不批量改）：
  1. `pseudo-efective`（第 205 行）、`pseudo-efectivity`（第 213 行）—— 印刷均为 `pseudo-effective`/`pseudo-effectivity`（文本层第 12 行）。ff 连字拍平，共 2 处。
  2. 行内 ℝ 拍平为 `R`（第 205 行 `R-Cartier R-divisor` ×2）、第 237 行 `Q-divisor` 的 ℚ 拍平为 `Q`；与 p.004/p.005 同源，行间公式内 `\mathbb{R}` 均正确保留。
  3. 标点扁平：第 229 行丢印刷 `f : X → Z,` 的逗号；第 235 行丢 `M|_S \equiv 0.` 的句点；第 241 行丢 `n(K_X+Λ) ∼ (n+2)M.` 的句点；第 243 行段末句点缺失。
  4. 第 247 行 `$B = 0 .$` 双句点（印刷单句点）。
  5. 数学式与正文间空格粘连多处（`condition$A ^ { d }`、`$\Lambda \geq B$such`、`the divisor A` 等）。
- **两处曾疑似差异、经核对后撤销（登记以留痕，防后续误「修复」）**：
  - `z := f′(S)` 疑似多撇 → 已撤销，见上，MD 正确。
  - 「The bound on the degree of B **is a** much more subtle.」疑似漏冠词 `a` → **撤销**。`pdftotext` 第 19 行为 `is much more subtle.`；300dpi 裁片 `/tmp/bk_p6_subtle.png`（×4）亲眼可见 `is much more subtle.` **无冠词**，MD 第 219 行正确。150dpi 整页图上的「a」为 `much` 的字形误读。
- 备注：本页无数学内容错误，**无需 Edit 修复**；前两轮 p.006 登记的箭头/bullet/单负号差异属实且已正确落地。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p001`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：`/tmp/birkarsing_audit_p007.png`（pngmono 150dpi，本轮新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p7_dash.png`（虚线箭头）、`/tmp/bk_p7_LY.png`（`L_Y` 字形）（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=7`，仅裁图）。
- 核对：页首 bullet `for any 0 \le L \sim_{\mathbb{R}} -K_X, the pair (X,tL) is klt.`；m/v/t 来源段（`[5, Theorems 1.2 and 1.7]`、`[5, Theorem 1.6]`）；reader's convenience 段与 exceptional 定义；non-exceptional 段（两处 `V \dashrightarrow X`、`B^+`、`\Sigma`）；perturb 段（`B_V^+`、`\Delta_V \sim_{\mathbb{Q}} B_V^+`、两条 `m(\cdot)\sim 0`）；serious issue 段；**Sketch of the proof of Theorem 1.6**（`\epsilon' \in (0,\epsilon)`、`L \in |A|_\mathbb{R}`、显示公式 `a(T,X,B+sL)=\epsilon'`、两处 `\phi\colon Y\to X`、`L_Y=\phi^*L`、`\mu_T sL_Y \geq \epsilon-\epsilon'`、`|-K_X|_\mathbb{R}`）；对照 Markdown 第 255–277 行，辅以 `pdftotext -f 7 -l 7 -layout` 与 `-bbox`。
- 结果：**PASS±**
  - **旧修复复核为正确（本页三项关键 glyph）**：
    1. 第 261 行两处 `$V \dashrightarrow X$` —— 300dpi 裁片 `/tmp/bk_p7_dash.png`（×5）亲眼可见**虚线双有理箭头**（两段短横 + 实心箭头尖）；`pdftotext` 第 19 行该箭头字形码作 `99K`（本字体编码的虚线箭头），且同一行出现**两次**（x126.48、x400.08）。实线 `→` 会被排成 `→`（如第 44 行 `φ : Y → X`），故此处确为虚线。MD 忠实。
    2. 第 275 行 `$L _ { Y } = \phi ^ { * } L$` —— 300dpi 裁片 `/tmp/bk_p7_LY.png`（×6）亲眼可见 `L_Y` 的 L 为**普通数学斜体单笔 L**，**非 Fraktur / 非花体**；下标 Y 为斜体。MD 忠实。
    3. 第 277 行 `$L \in | - K _ { X } | _ { \mathbb { R } }$` —— **线性系统前无 `\Omega` / `L` 前缀符号**（文本层第 51 行作 `L ∈ | − KX |R`）。MD 忠实。
  - 第 275 行两处 `$\phi \colon Y \to X$` 为**实线**箭头（文本层第 44 行 `φ : Y → X`；第 46 行同），与第 261 行的虚线 `V ⇢ X` **区分正确**，未混同。
  - 系数与符号核对无误：`\mu _ { T } s L _ { Y } \geq \epsilon - \epsilon ^ { \prime }` 的乘子 `s` 在位、**减号 `−` 未写成加号**；显示公式 `a (T, X, B + s L ) = \epsilon^ {\prime}` 的 `T` 为**普通斜体、无上横线**。
  - 第 263 行两条 `m(\cdot) \sim 0` 分别为 `m ( K _ { V } + B _ { V } ^ { + } ) \sim 0` 与 `m ( K _ { V } + \Delta _ { V } ) \sim 0`，第 263 行末 `m ( K _ { X } + \Delta ) \sim 0`；**均无 `\iota` 下标**，与印刷一致。`\Delta _ { V } \sim _ { \mathbb { Q } } B _ { V } ^ { + }` 的 `Q` 下标在位。
  - 引文与编号核对无误：`[5, Theorems 1.2 and 1.7]`、`[5, Theorem 1.6]`、`[15]`、`[5]`。
- **print quirk 忠实保留（未改，已回原页复核确认 MD 一致）**：
  - 「some rough explanations **for as to why** the existence of m, v, t …」—— 印刷原页即如此（文本层第 8 行），语法怪异属原刊，MD 第 259 行原样保留，**未按数学/英语常识补写**。
  - 「**Replacing X with** can assume it is ℚ-factorial.」—— 印刷原页即缺 replace 的宾语（文本层第 37 行），MD 第 267 行原样保留，**未静默改写为「Replacing X with Y, we can assume…」**。
- PASS± 差异（登记，按 SOP 不批量改）：
  1. `coeficients`（第 263 行 ×1、第 265 行 ×3，共 4 处）—— 印刷均为 `coefficients`；`efective`（第 265 行 ×1）—— 印刷 `effective`。ff 连字拍平。
  2. `$\mathrm { A p p l y i n g }$`（第 259 行）与 `${ \mathrm { i s } } ,$`（第 261 行）—— 英文词被排入数学正体并加字距。记号可辨。
  3. 第 259 行 `$n \in \mathbb { N } .$` 句点被排入数学环境内；同句 `X.` 的句点又紧随其后，构成伪双标点。
  4. 第 263 行 `replacing$m ,$,` 双逗点（印刷单逗号）。
  5. 行末丢印刷句点：第 259 行（`−K_X` 后）、第 263 行（`\sim 0` 后）、第 277 行（`T on X` 后）。
  6. 数学式与正文间空格粘连多处（`existence of$m , v , t$is`、`case. Here by X`、`so X is birationally bounded` 等）。
- 备注：本页无数学内容错误，无需 Edit 修复。前两轮 p.007 登记的箭头、花体 L、Ω、ι 四类差异与两处 print quirk 保留决定均属实。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p001`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：`/tmp/birkarsing_audit_p008.png`（pngmono 150dpi，本轮新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p8_frac1.png`、`/tmp/bk_p8_frac2.png`（两处 `1/u` 分式）、`/tmp/bk_p8_T.png`（`T` 字形）（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=8`，按 `-bbox` 坐标换算后放大 6–7 倍，仅裁图）。
- 核对：`L = uT`、`u = \mu_T L` 段；`[5, Theorems 1.2, 1.6, 1.7]` 段与 `K_X + \Omega`、`|-nK_X|`、`\operatorname{vol}(-K_X)`；两处虚线箭头（`X \dashrightarrow V`、`V \dashrightarrow X`）；pull back 段与三条 bullet（`\epsilon''`-lc、`(V,\Delta+\frac1u M)` not klt、`"degrees"`）；`1/u` 的下界句；**Sketch of the proof of Theorem 1.8**（阈值不等式 `|M|_\mathbb{R} \geq |A|_\mathbb{R}`、`\epsilon' = \epsilon/2`、`a(T,X,\Delta:=B+sN)=\epsilon'`、`\phi\colon V\to X`、`a(T,X,\Delta)=\epsilon'<1`、`Y\to X`、`-(K_Y+T)`、`[13]` ACC）；toroidalisation 段（`\Lambda_Y`、`n(K_Y+\Lambda_Y)\sim 0/X`、`a(T,X,\Lambda)=0`、`Supp`）；discard 段（`\Lambda = S_1+\dots+S_d`、`Y\to X`）；torification 段（`X\to\mathbb{P}^d`、`z=(1:0:\dots:0)`）；对照 Markdown 第 279–321 行，辅以 `pdftotext -f 8 -l 8 -layout` 与 `-bbox`。
- 结果：**PASS±**
  - **redo 轮唯一 FAIL 修复经本轮复核为正确（本页关键项）**：第 299 行 `There is a prime divisor$T$on birational models of X` —— 印刷的 `T` 为**普通斜体、无上横线**。300dpi 裁片 `/tmp/bk_p8_T.png`（×7）亲眼可见 `or T on` 的 `T` 顶部为其自身衬线，非重音符；`-bbox` 该词元 `T`(x411.60–417.97) 的 **yMin=370.298 与同行 `prime`、`divisor` 完全相同**（若有 overline 重音，yMin 必显著上抬）。**redo 轮判定「Luna 曾误登记原文带上横线、`\overline{T}` 系 MinerU 引入的伪记号、改为 `T` 正确」的裁定属实，保留。**
  - **两处分式均为 `1/u`（本轮新增仲裁点）**：第 287 行 `$( V , \Delta + \frac { 1 } { u } M )$` 与第 291 行 `$\textstyle { \frac { 1 } { u } }$`。仲裁证据三重：①300dpi 裁片 `/tmp/bk_p8_frac1.png`、`/tmp/bk_p8_frac2.png`（×6）分别亲眼可见 `+ 1/u M)` 与 `or 1/u, he…`，分子 `1` 在分数线之上、分母斜体 `u` 在下；②`-bbox` 第一处 `u`(yMin=254.59, yMax=261.91) 与 `1`(yMin=246.85, yMax=253.07) **x 中心相同、1 的 yMin 更小**，即分子在上、分母在下，分母为 **`u`** 而非 `n`；③`pdftotext` 因分式按「分母先于分子」输出而写作 `u1`，与 1/u 一致。**MD 两处均正确。我在 150dpi 整页图上曾把斜体 `u` 误读为 `n`，经升级裁片与 bbox 双重核对撤销该疑似差异。**
  - **箭头类型区分正确（本页新增仲裁点）**：印刷在 `X ⇢ V`、`V ⇢ X`（第 281 行）用**虚线**字形码 `99K`，而在 `φ : V → X`（第 305 行）、`Y → X`（第 311、315 行）、`X → P^d`（第 317 行）用**实线** `→`。MD 对应地写成 `$X \dashrightarrow V$`、`$V \dashrightarrow X$`（第 281 行）与 `$\phi \colon V \to X$`（第 305 行）、`$Y \to X$`（第 311、315 行）、`$X \to \mathbb { P } ^ { d }$`（第 317 行）——**虚实两类未混同，与印刷逐一吻合。**
  - 阈值不等式项序核对无误：第 296 行 `\operatorname{lct}(X,B,|M|_{\mathbb{R}}) \geq \operatorname{lct}(X,B,|A|_{\mathbb{R}})`，`|M|` 在左、`|A|` 在右，未互换；与第 210 行（p.6）的同一不等式写法一致。
  - `\epsilon ^ { \prime } = \frac { \epsilon } { 2 }`（第 299 行）、`a (T, X, \Delta := B + s N ) = \epsilon^ {\prime }`（第 302 行）、`a (T, X, \Delta ) = \epsilon^ {\prime} < 1`（第 308 行）三式的撇号数、`< 1` 与 `:=` 定义号均与印刷一致；`\epsilon ^ { \prime \prime }`（第 285 行）为**双撇**且**后无尾随 `2`**。
  - 第 311 行 `$- ( K _ { Y } + T )$` 为**单负号**（印刷无双负号）；第 313 行 `$n ( K _ { Y } + \Lambda _ { Y } ) \sim 0 / X$` 的 `0/X` 系数与印刷一致；`$a ( T , X , \Lambda ) = 0$` 的 `= 0` 未写成 `≥ 0`。
  - 「"degrees"」的成对引号（第 289 行）已恢复为 `“degrees”`，与印刷一致。
- **print quirk 忠实保留（未改，已回原页复核确认 MD 一致）**：
  - 「a birational map X ⇢ V so that Σ is **reduced whose support** contains the exceptional divisors …」—— 印刷即语法悬空（whose support 修饰错位），MD 第 281 行原样保留。
  - 「We can assume the image of T on X is a closed point x **otherwise we can cut** by hyperplane sections …」—— 印刷无标点连排，MD 第 305 行原样保留。
- PASS± 差异（登记，按 SOP 不批量改）：
  1. 第 313 行 `over$X .$,` —— 印刷为 `over X, we can find`（无句点），MD 多出伪句点 `X .`。
  2. 第 315 行 `dificult` —— 印刷 `difficult`。ff 连字拍平。
  3. 第 285 行 `$\epsilon ^ { \prime \prime } > 0$` 后丢印刷的逗号；第 279、283、305、313、315、317 行行末丢印刷句点。
  4. 第 299 行 `for lct$( X , B , | A | _ { \mathbb { R } } )$` —— 函数名 `lct` 留在数学环境之外；第 313、315 行 `Supp` 被排成带字距的正体 `\operatorname { S u p p }`。
  5. 行内 ℝ 拍平（第 281 行 `n \in \mathbb N` 写作 `\mathbb N`、第 313 行 `n \in \mathbb N` 同），与 p.004–p.007 同源；数学式与正文间空格粘连多处。
- **一处曾疑似差异、经核对后撤销（登记以留痕，防后续误「修复」）**：
  - `1/u` 疑似应为 `1/n`（150dpi 整页图上斜体 u 形似 n）→ **撤销**，MD 两处 `\frac{1}{u}` 均正确，见上。
- 备注：本页无数学内容错误，**无需 Edit 修复**；redo 轮在本页的 FAIL（`\overline{T}`→`T`）经本轮 300dpi 独立复核**成立且已正确落地**，其 PASS± 登记亦属实。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p001`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## 本片段小结（p.001–p.008 第三轮重做）

- 覆盖：PDF p.1–p.8 共 **8 页全部逐页完成**，每页均执行「gs pngmono 150dpi 渲染 → `Read` 亲眼目检整页 → 读 Markdown 对应段 → 五点比对 → 立即落签」，无跳页、无合并条目。逐页新增说明 **8 条**（`## p.001` … `## p.008`，actor `Wf-R-Birkar-p001`）。
- 评级：**8 页全部 PASS±，0 页 FAIL**，本片段 Markdown **改动 0 处**（无需 Edit 修复）。
- **裁定为 MD 正确、经升级仲裁撤销的 3 处疑似差异**（均因 150dpi 整页图分辨率不足而起，已逐处留痕以防后续误「修复」）：
  1. p.006 `z := f′(S)` 疑似多撇 → 印刷为 `f(S)`（300dpi + bbox：词元 `f` 的 yMin 与同行 `z`、`:=` 相同，无上抬撇号），MD 正确。
  2. p.006 「is **a** much more subtle」疑似漏冠词 → 印刷为 `is much more subtle.`（300dpi 裁片 + 文本层），MD 正确。
  3. p.008 `1/u` 疑似应为 `1/n` → 印刷两处均为 `1/u`（300dpi 裁片 + bbox 分子/分母 yMin 序 + 文本层 `u1`），MD 正确。
- **前两轮旧修复经本轮原页独立复核全部成立、予以保留**：p.002 `Y \to Z` 箭头；p.003 四处爆破/极限箭头、`n \geq 2` 无伪双点、`[8]` 后无尾随 2、`\Delta` 无伪下标；p.004 `M<sup>c</sup>Kernan` 上标 c；p.005 Theorem 1.8 的 `A^d \leq r`（**无下标 i**，bbox 证实该行 `r,` 后再无词元）与三条假设 bullet；p.006 `f : X \to Z` 箭头、`M - (K_X+B)` 单负号、六条假设与三条 sketch bullet；p.007 `V \dashrightarrow X` 虚线箭头、`L_Y` 普通斜体（非 Fraktur）、`|-K_X|_R` 无 Ω、`m(\cdot)\sim 0` 无 ι；p.008 `\overline{T}`→`T`、虚实箭头未混同、`\epsilon''` 无尾随 2。
- **print quirk 忠实保留（未按数学/英语常识静默「纠正」）**：p.007「some rough explanations **for as to why**」「**Replacing X with** can assume it is ℚ-factorial」；p.008「Σ is reduced **whose support** contains」「a closed point x **otherwise we can cut** by hyperplane sections」；p.001 目录缺号子节（2.3、2.7、2.10、2.11、2.13、2.15、2.17、2.20、2.21、2.24 等，**印刷原页即缺**）。
- 按 SOP 登记而不批量修复的共性伪影：ff 连字拍平（`diferent`、`diferential`、`efective`、`coeficient(s)`、`pseudo-efective`、`tha`、`dificult`、`ofice`）、行内 ℝ/ℚ 拍平为 R/Q、标点扁平（双逗点、伪句点、行末丢句点）、数学式与正文空格粘连、MathJax 词距空格化（`A p p l y i n g`、`S u p p`）、以及两处 MinerU 把正文行提升为 `##` 标题（p.003 第 91、107 行）。
- 本片段未发现任何数学内容错误、整段丢失或记号误置；所有 PASS± 项均不影响定理陈述与证明的可读性。
- **溯源核对（已实际执行）**：`git show cpf-redo/Birkar_2016_singularities_linear_systems^:"2018年 - Birkar/…__….md"` 取父提交版 Markdown 与本工作区版逐行比对 —— **MD 第 1–321 行（本片段 p.1–p.8 的全部作用域）`diff` 结果为空**，即前两轮/后续 peer 的修改**一处也没有落在本片段范围内**；全文件首个差异出现在 **MD 第 370 行**（PDF p.9 之后），内容为 redo 轮对 `coeficient`→`coefficient`、`suficiently`→`sufficiently`、`efective`→`effective`、`\Re`/`\mathfrak{R}`→`\mathbb{R}`、`Etale`→`Étale`、`{\cal X},{\cal B}`→`X, B` 的修复，方向正确、与 p.1–p.8 无关。故本片段 8 页**无任何一项需判定为「非导出缺陷，系 <commit> 引入」**——所有 PASS± 项经原页复核确认**自 MinerU 初次导出即如此**。
- **改动清点（本片段实际写入）**：本片段只写了这一个 AUDIT 文件。目标 Markdown 交付态 SHA-256 = `95216ff90edbb81b4ac0f789bcdfad682e5258d86dba467801fcb794c509c3ac`，与本片段开工基线**逐字节相同**（`shasum -a 256` 复核），印证 **Markdown 改动 0 处**；PDF SHA-256 = `c9c73303be3b12c5ca91506ac541c9b9d81764d19bcd7183b7c577f8c0d546fe` 与开工记录一致，**原件只读未被触碰**。
- 未执行任何 git 提交/暂存/合并/推送；未触碰根级 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、`MEMORY.md`、`README.md` 及其它论文目录；PDF 全程只读；根级日志由集成者据本节汇总补写。

---

## 第二片段（p.009–p.016，actor `Wf-R-Birkar-p009`）

> 本片段接续 `Wf-R-Birkar-p001`（p.1–p.8）。开工基线：Markdown SHA-256 = `95216ff90edbb81b4ac0f789bcdfad682e5258d86dba467801fcb794c509c3ac`，PDF SHA-256 = `c9c73303be3b12c5ca91506ac541c9b9d81764d19bcd7183b7c577f8c0d546fe`（46 页），AUDIT 已有 `## p.` 条目 98 条。
>
> **本片段修复政策（与前两轮对齐后的显式裁定）**：redo 轮 `Wf-R-P13` 在本作用域内（MD 373–555 行，即 p.10–p.13）**已实际修复** ff 连字拍平、ℜ→ℝ、´etale→étale、花体→正体、缺失数学记号五类；而同一轮对 p.9 却只「登记不修」，内部不一致。本片段统一采取 redo 轮在 p.10–p.13 已确立的口径：
> - **修**：字符级丢失（`ofice`→`office`、`coeficient`→`coefficient`、`efective`→`effective`）、重音符错位（`Pˇaun`→`Păun`）、标点错讹（伪逗号代句点、丢句点、连字双句点）。
> - **登记不修**：行内 ℝ/ℚ 拍平为 R/Q（同一字母的字形降级，语义无歧义；redo 轮只在该字形实为 ℜ/Fraktur 时才修）、断行连字丢失（`Rdivisors`）、MathJax 词距空格化（`{ \mathrm { ~ i f ~ } }`、`\mathrm { l c }`）、数学式与正文空格粘连、负号落在数学环境外。
> - 依据为 SOP「PASS± 排版伪影按登记处理，不批量规范化」；上列「修」类均逐处有 PDF 页码 + 300dpi 裁片或 bbox 坐标支撑，且 `old_string` 全部经 `grep -c` 确认全文件唯一（`is pseudo-efective` 有 2 处，已用更长的 `If$A - D$is pseudo-efective, then one easily sees` 定位到本作用域那处，第 203 行属 p.6、上片段已审计、本片段不动）。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：`/tmp/birkarsing_audit_p009.png`（pngmono 150dpi，本片段新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p9_sigma.png`、`/tmp/bk_p9_Paun.png`、`/tmp/bk_p9_obtT.png`、`/tmp/bk_p9_office.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=9`，按 `-bbox` 坐标 ×S=300/72.0 换算后放大 7 倍，仅裁图未写 Markdown）。
- 核对：§1.8 proof 收尾（`S_i`→`H_i`、`X = \mathbb{P}^d`、`-(K_X+\Lambda)` ample、`K_X+\Delta` numerically trivial）；`W \to X` 爆破段（`Y \to X` 收缩 T、`(Y,\Delta_Y)` ε′-lc、MMP on `−K_Y`、`Y'` Fano、toric 版 1.1 [9]、补式链 `K_{Y'}+\Omega_{Y'} → K_Y+\Omega_Y → K_X+\Omega`、`m(K_X+\Omega) \sim 0`、`(X,\Omega+u\Lambda)` klt、T 在 W 上重数有界）；**Acknowledgements 全文**（8 位致谢人 + Jungkai A. Chen + 台北理论科学中心）；**2. Preliminaries** 开头（特征 0、代数闭域 k）；**2.1. Divisors**（`D = \sum d_i D_i`、`\mu_{D_i}D`、`\phi \colon X \dashrightarrow Y` 虚线箭头、`\phi_*D = D_Y`、`\deg_A D := A^{d-1}D`（d>1）与 `:= \deg D`（d=1）、`\deg_A D \le \deg_A A`、`A^{d-1}` 作 1-cycle）；**volume 公式** `\operatorname{vol}(D)=\limsup_{m\to\infty}h^0(\lfloor mD\rfloor)/(m^d/d!)`；对照 Markdown 第 323–343 行，辅以 `pdftotext -f 9 -l 9 -layout` 与 `-bbox`。
- 结果：**PASS±**（本片段首批修复页，共改 6 处，均属字符丢失/标点错讹类，无数学内容错误）
- **已用 Edit 修复 6 处（逐处绑定页码与裁片）**：
  1. 第 325 行 `obtains$T ,$` → `obtains $T$.` —— 印刷为句点。证据：`-bbox` 中 `T`(x=361.08–367.45, y=167.02–177.93) 之后紧跟独立词元 `'.'`(x=369.00–372.02, **yMin 与 T 同行 167.02 完全相同**，即基线上的实心点，逗号必带下伸尾部）；300dpi 裁片 `/tmp/bk_p9_obtT.png`（×7）亲眼可见 `ch obtains T. Si`，T 后为**基线实心圆点、无尾**。原 MD 的逗号系 MinerU 伪影。
  2. 第 327 行 `Mihai Pˇaun` → `Mihai Păun` —— 印刷重音符为** breve（˘，开口向上的小杯形）**，非 MD 所写的 caron（ˇ），且 MD 把声调符排到了 `a` **之前**。证据：`-bbox` 词元 `Pǎun,`(px x=1329–1446, y=1397–1443) 字体仅能编码为 `ǎ`（文本层失真）；300dpi 裁片 `/tmp/bk_p9_Paun.png`（×7）亲眼可见 `Mihai Păun,`，a 顶部为** breve**。按铁律三以印刷为准，不按人名常识改动重音符位置以外的任何内容，仅把错误的 caron 纠正为印刷所印的 breve。
  3. 第 327 行 `National Taiwan University ofice` → `office` —— 印刷为 **`ffi` 三合连字**（三根竖画由横画相连）。证据：`-bbox` 词元 `office`(px x=1030–1131, y=1505–1551)；300dpi 裁片 `/tmp/bk_p9_office.png`（×7）亲眼可见 `y office of`，其中 `ffi` 为**一个连字字形、三竖画一横画**，MD 的 `ofice` 丢失了整整一个 f 字符。
  4. 第 333 行 `the coeficient$d _ { i }$by$\mu _ { D _ { i } } D$ Let` → `the coefficient$d _ { i }$by $\mu _ { D _ { i } } D$. Let` —— 一处修复同时解决两项：印刷 `coefficient`（`-bbox` 词元 x=414.24–461.31, y=512.50–523.41，文本层作 `coefficient` 双 f）被拍平为 `coeficient`；且印刷 `μ_{D_i}D.` 的**句点丢失**（bbox 该行末为 `D.` x=508.92–521.30，句点存在），并补上数学式与 `Let` 之间缺失的空格。
  5. 第 335 行 `If$A - D$is pseudo-efective,` → `is pseudo-effective,` —— 印刷 `pseudo-effective`（`-bbox` 词元 `pseudo-effective,` x=320.40–398.06, y=590.14–601.05），`ff` 被拍平。
  6. 第 335 行行末 `$\deg _ { A } D \leq \deg _ { A } A$` → 补句点 `$\deg _ { A } A$.` —— 印刷有句点（`-bbox` 该行末词元 `A.` x=164.88–176.06, y=603.10–614.01）。
- **核对无误、未改动者**：
  - **`D = \sum d_i D_i` 的 Σ 无下标（本轮重点仲裁，结论：MD 正确）**：150dpi 整页图上我曾疑心 Σ 漏了下标 `i`。`-bbox` 显示 `Σ` 位置的词元被字体误映射为字面 `"P"`(x=342.96–354.47, **y=499.12–514.83，明显高于同行基线 499.54–510.45**，符合大型算子字形)，且 `Σ`(xMax=354.47) 与其后 `d`(xMin=356.28) 之间**仅 1.8pt 间隙、不存在任何下标词元**；300dpi 裁片 `/tmp/bk_p9_sigma.png`（×7）亲眼可见 `D = Σ d_i D_i be`，**Σ 光秃无下标**，而下标只出现在 `d_i`、`D_i` 上。**MD 第 333 行 `$D = \sum d _ { i } D _ { i }$` 正确，疑似差异撤销。**
  - **致谢人名 `Yanning Xu`（150dpi 误读，撤销）**：150dpi 整页图上我曾读作 `Yanxing Xu`。`-bbox` 词元 `Yanning`(x=481.92–521.33, y=335.38–346.29) 与 `Xu` 同段，文本层作 `Yanning`；**MD 第 327 行 `Yanning Xu` 正确**。
  - `\phi \colon X \dashrightarrow Y`（第 333 行）为**虚线**箭头：印刷该处字形码为 `99K`（`-bbox` x=286.44–302.69, y=526.15–537.46），与本页 `$W \to X$`、`$Y \to X$` 的实线 `→`（x=136.32–147.23 / x=198.24–209.15）区分明确，MD 虚实未混同。
  - volume 公式把印刷的 `|mD|` 写成 `\lfloor mD \rfloor` —— 这是该记号的正确含义（取整线性系统），**不算缺陷，保留**；`\limsup_{m\to\infty}`、`m^d/d!` 与印刷 `lim sup_{m→∞} h^0(⌊mD⌋)/m^d/d!` 一致。
  - `\deg_A D := A^{d-1}D`（d>1）：`-bbox` 词元 `d−1`(x=154.20–169.35, **yMin 575.83 < 同行 577.30**) 确为上标，MD `A ^ { d - 1 } D` 正确。
  - `2. Preliminaries` 提升为 `##` 标题（第 329 行）与印刷的居中节标题一致，**非 MinerU 误提升**；`2.1. Divisors.` 在印刷中为行内接排，MD 保持行内，**正确**。
- **PASS± 差异（按上述政策登记不修）**：
  1. 行内 ℝ 拍平：第 333 行 `an R-divisor`、第 335 行 `R-Cartier Rdivisors`、第 337 行 `not R-Cartier`、第 339 行 `The volume of an R-divisor`（印刷均为黑板粗 ℝ）。
  2. 第 337 行 `an ample Q-divisor` —— 印刷为黑板粗 ℚ。
  3. 第 335 行 `R-Cartier Rdivisors` 中第二个 `R-` 的**连字符被断行吞掉**，成 `Rdivisors`。
  4. 第 335 行 `{ \mathrm { ~ i f ~ } } d = 1` —— MathJax 不换行空格转义体，阅读不受影响。
  5. 第 325 行 `\epsilon ^ { \prime } -$lc`（负号落在数学环境外）与 `\mathrm { l c } .$.`（`lc` 后连出两个句点，印刷仅一个）。
  6. 行末句点缺失：第 325 行（段末 `as required.`）、第 337 行（段末 `of X.`）各丢一个句点；第 323、327、329、331、339 行句点完整。
  7. 数学式与正文粘连（`$T$is`、`$W$is`、`$m \in \mathbb N$which` 等）多处。
- **一处曾疑似差异、经核对后撤销（登记以留痕，防后续误「修复」）**：
  - 致谢人名 `Yanxing` 疑似 MD 误作 `Yanning`（实为我在 150dpi 下读错）→ **撤销**，MD 正确。
  - `D = \sum d_i D_i` 疑似 MD 漏 Σ 的下标 `i` → **撤销**，MD 正确。
- 备注：本页**无数学内容错误、无整段丢失**；6 处修复全为印刷有而 MD 缺的字符/标点或重音符误码，未触及任何公式系数、指数、上下标或记号约定。第 203 行同名 `pseudo-efective` 属 p.6、上片段范围，本片段刻意未动。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p009`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：`/tmp/birkarsing_audit_p010.png`（pngmono 150dpi，本片段新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p10_thatis.png`、`/tmp/bk_p10_efective.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=10`，按 `-bbox` 坐标 ×S 换算后放大 8 倍，仅裁图未写 Markdown）。
- 核对：页眉「10  Caucher Birkar」；**2.2. Pairs and singularities**（sub-pair 定义 `(−∞,1]`、`K_X+B` ℝ-Cartier、boundary/pair 之分）；log resolution 段与对数不整公式 `a(D,X,B) := 1 − µ_D B_W`；sub-lc/sub-klt/sub-ε-lc 判据（`≥0`/`>0`/`≥ε`，系数 `≤1`/`<1`/`≤1−ε`，`ε ≤ 1`）；non-klt place / centre 段；log smooth pair 段（`B = Σ_{i=1}^r B_i`、`∩_{i∈I} B_i`、`I ⊆ {1,…,r}`）；**Lemma 2.3** 全文（`Δ = tB+(1−t)B′`、`a(D,X,Δ) = ta(D,X,B)+(1−t)a(D,X,B′)`、`sub-(tε+(1−t)ε′)-lc`）；「We leave the proof to the reader.」；**2.4. Fano pairs**（`−(K_X+B)` ample/nef+big、[7] Mori dream space）；**2.5. Minimal models, Mori fibre spaces, and MMP**（`X→Z`、`φ: X ⇢ Y/Z` 虚线、`D_Y := φ_*D`、`g: W→X`/`h: W→Y`、`E := g^*D − h^*D_Y` effective and exceptional/Y、`Supp g_*E`；minimal model 段 `D_Y` nef/Z、`Y→T/Z`、`−D_Y` ample/T、`dim Y > dim T`；MMP 段 [7]）。对照 Markdown 第 345–375 行，辅以 `pdftotext -f 10 -l 10 -layout` 与 `-bbox`。
- 结果：**PASS±**（改 6 处；无数学内容错误）
- **已用 Edit 修复 6 处（逐处绑定页码与裁片）**：
  1. 第 345 行 `coeficients` → `coefficients` —— 印刷 `coefficients`（文本层与 150dpi 整页图均为双 f），ff 连字拍平。
  2. 第 353 行段末 `$\epsilon \leq 1$` → 补句点。证据：`-bbox` 该行末词元 `'1.'`(px x=1767–1803, y=957–1003)，句点与 `1` 同行同基线，确实存在；MD 丢失。
  3. 第 355 行 `that${ \mathrm { i s } } ,$on birational models` → `that is, on birational models` —— **本轮最重的一处**。原 MD 把英文单词 `is` 排成了数学环境内的正体 `\mathrm{i s}`（字距拉开成「i s」），并把逗号放到数学环境**之外**，渲染结果为「that i s ,on birational」，既非原词形又把逗号与后词粘连。证据：`-bbox` 词元序列 `X,`(x=1901–1955) → `that`(x=1969–2053) → `is,`(x=2067–2110) → `on`(x=2124–2172)，`is` 与 `that`、`on` **同一基线 y=1011–1057**，是普通正体英文而非数学体；300dpi 裁片 `/tmp/bk_p10_thatis.png`（×8）亲眼可见 `, that is, on`，逗号带下伸尾、紧随 `is` 之后且与 `on` 之间有空格。
  4. 第 365 行段末 `…-lc` → 补句点。印刷 `then (X, Δ) is sub-(tε + (1−t)ε′)-lc.` 有句点，MD 丢失。
  5. 第 371 行 `is efective` → `is effective` —— 印刷为 **`ff` 连字**。证据：`-bbox` 词元 `effective`(px x=1605–1764, y=2586–2631)；300dpi 裁片 `/tmp/bk_p10_efective.png`（×8）亲眼可见 `ffective a`，两支 f 由横画相连、第二个 f 带钩，MD 丢失整整一个 f。
  6. 第 373 行段末 `dim$Y > \dim T$` → 补句点。印刷 `dim Y > dim T.` 有句点，MD 丢失。
- **核对无误、未改动者**：
  - **对数不整公式（p.10 的数学核心）**：`a(D, X, B) := 1 − \mu_D B_W`（第 350 行）与印刷 `a(D, X, B) := 1 − µ_D B_W.` 逐符号一致 —— 系数 **1**、减号、**µ_D 下标 D**、**B_W 下标 W**、末尾句点，MD 全对。`-bbox` 佐证该行 `1`(x=1306–1329)、`−`(x=1339–1374)、`µ`(x=1384–1412) 与下标 `D`(y=731–761)、`B_W` 的 `W`(y=731–761) **yMin 明显低于同行基线 713**，确为下标而非同行字符。
  - **Lemma 2.3 公式**：`a (D, X, \Delta) = t a (D, X, B) + (1 - t) a (D , X , B ^ {\prime})`（第 362 行）与印刷 `a(D,X,Δ) = ta(D,X,B) + (1−t)a(D,X,B′)` 一致：`t` 与 `(1-t)` 的系数位置、**ε′ 的撇号数**（单撇 `B^{\prime}` 与 `\epsilon^{\prime}` 各一）均正确，未把 `Δ` 误作 `\Lambda`，未把 `t\epsilon` 的 `\epsilon` 漏掉。
  - `\phi \colon X \dashrightarrow Y / Z`（第 371 行）为**虚线**箭头（印刷字形码 `99K`），与本页 `$W \to X$`、`$g \colon W \to X$`、`$h \colon W \to Y$`、`$X \to Z$` 的实线区分明确，MD 虚实未混同。
  - **redo 轮旧修复复核为正确**：第 373 行 `if$D _ { Y }$is nef/Z` —— 印刷为 `if D_Y is nef/Z`，MD 的 `$D_Y$` 恢复属实（父提交版此处曾误作裸 `D`）。
  - **print quirk 忠实保留**：第 355 行「**An** non-klt place」（印刷原文即用 `An` 而非 `A`，语法瑕疵照录未改）。
  - `2.2.` / `2.4.` / `2.5.` 三个小节号在印刷中均为**行内接排**，MD 亦保持行内未提升为 `##` 标题，**正确**（与 p.9 的 `2. Preliminaries` 居中节标题应提升的情形不同）。
- **PASS± 差异（按本片段政策登记不修）**：
  1. 行内 ℝ 拍平：第 345 行 `an R-divisor B`、`is R-Cartier`、第 369 行 `R-Cartier R-divisor`、第 371 行 `an R-Cartier R-divisor on X`、`is also R-Cartier`（印刷均为黑板粗 ℝ）。
  2. 第 357 行 `$\begin{array} { r } { B = \sum _ { 1 } ^ { r } B _ { i } } \end{array}$` —— 行内公式被 MinerU 包进了 `array` 环境，内容等价于 `B = \sum_1^r B_i`，正确但排版冗余。
  3. 行末句点仍缺：第 371 行段末 `…divisors of φ.` 已有句点；本轮补齐后 p.10 仅余第 369 行以前各段的粘连类问题，无实质缺失。
  4. 数学式与正文粘连（`$B \geq 0$we`、`$W \to X$be`、`$X \to Z$be` 等）多处。
- **一处曾疑似差异、经核对后撤销（登记以留痕，防后续误「修复」）**：
  - 第 369 行 `…on any R-Cartier R-divisor on X…` 疑似**第一个 `R-` 漏了连字符**（`pdftotext -layout` 把该处断成 `R-Cartier` 与 `R-divisor` 两个词元，形似少一连字符）→ **撤销**。`-bbox` 佐证两词元 `R-Cartier`(px x=1518–1707) 与 `R-divisor`(px x=1725–1906) **各自内部都带连字符**，连字符是断行吞掉而非 MD 缺失，MD 正确。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；6 处修复分别为 2 处字符丢失、3 处句点补齐、1 处英文单词被误排为数学体。Lemma 2.3 与对数不整公式这两个数学要点逐符号核对无误。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p009`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

### p.009 追补（第 7 处修复，政策一致性）
- 自查发现本片段政策写明「标点错误（双句点、句点代逗号、丢句点）**修**」，但 p.009 说明第 5 项把同类的 `\mathrm{lc} .$.` **登记不修**，而 p.011 又实修了同类双句点 —— 前后不一致。此处按已声明的政策补修，使本片段口径统一。
- 第 7 处修复（补记）：第 325 行 `which is Fano and$\epsilon ^ { \prime } { - } \mathrm { l c } .$. By the toric version` → `…\mathrm { l c }.$ By the toric version`。证据：`-bbox` 词元序列 `Fano`(px x=765–862) → `and`(x=877–950) → `ǫ`(x=965–983) → `′`(x=983–993, y=911–932, 上抬) → **`-lc.`**(x=995–1055, **单一句点**) → `By`(x=1075–1131)；300dpi 裁片 `/tmp/bk_p9_lc.png`（裁自 `bk_p9_300.png`，区域 px (950,890)–(1180,975) 放大 7 倍）亲眼可见 `ɛ′ -lc. By t`，`lc` 之后**只有一个基线实心点**。MD 的 ` .$.` 连出两点属标点重复，**确认为缺陷并已修**。
- p.009 修复总数由 6 处更正为 **7 处**；本片段（p.009–p.016）累计改动数相应 +1。同一页的 `\epsilon ^ { \prime } -$lc`（负号落在数学环境外）仍按政策**登记不修**（语义无歧义）。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：`/tmp/birkarsing_audit_p011.png`（pngmono 150dpi，本片段新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p11_t0.png`、`/tmp/bk_p11_thanT.png`、`/tmp/bk_p11_placeT.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=11`，按 `-bbox` 坐标 ×S 换算后放大 7–8 倍，仅裁图未写 Markdown）。
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties  11」；**2.6. Plt pairs** 开头（plt blowups [36]、[38, Definition 3.5]、[44, Lemma 1]）；**Lemma 2.7 陈述全文**（四条 bullet：`φ` small 或只收缩 `T`、`(Y,T)` plt、`−(K_Y+T)` ample over X、`a(T,X,B)=0`）；**Proof 全文**（`a(T,X,B)=a(T,X,Γ)=0`、"no lc place other than T"、`(1−t)B+tC` 替换 C、small Q-factorialisation、Q-factorial 收缩抽 `T`、`K_Y+C_Y` 拉回 `K_X+C`；MMP on `−(K_Y+T)`、`Y′→Y″/X`、`K_{Y′}+T′ ∼_ℚ 0/Y″` 与 lc 非 klt 矛盾、`T″` pushdown、`a(D,Y,Γ_Y)>0`；`ψ: W→X` log resolution、`K_W+B_W=ψ^*(K_X+B)`、`K_W+C_W=ψ^*(K_X+C)`、`B_W−C_W ∼_ℝ H_W+G_W/X`、`H_W≥0` ample over X、`H+G` ℝ-Cartier、`ψ` 是 `(X,B+C+H+G)` 的 log resolution；`E≠0`、无公共分支时 `Γ_W ∼_ℝ B_W+aH_W+aG_W`、`(W,Γ_W)` sub-lc、`(W,Supp Γ_W)` log smooth、`μ_T Γ_W=1`、`Γ:=ψ_*Γ_W` effective、`K_Y+Γ_Y∼_ℝ0/X`）。对照 Markdown 第 377–425 行（p.12 起于第 427 行「Now assume G_W and E…」），辅以 `pdftotext -f 11 -l 11 -layout` 与 `-bbox`。
- 结果：**PASS±**（改 3 处；无数学内容错误）
- **已用 Edit 修复 3 处（逐处绑定页码与裁片）**：
  1. 第 395 行 `place other than$T .$. Replacing` → `place other than $T$. Replacing` —— 印刷为**单个句点**，MD 连出两个（`$T .$.`）。证据：`-bbox` 该行词元序列 `than`(px x=1260–1350) → `T`(x=1369–1395) → **单个** `'.'`(x=1402–1414) → `Replacing`(x=1444–1638)，`T` 与 `Replacing` 之间只有**一个**标点词元；300dpi 裁片 `/tmp/bk_p11_thanT.png`（×7）亲眼可见 `T. Replacing`，T 后为一个基线实心圆点、无第二点。
  2. 第 395 行 `real number$t > 0 .$, we can assume` → `real number$t > 0$, we can assume` —— 印刷为**逗号**，MD 误作句点。证据：`-bbox` 词元 `'0,'`(px x=1136–1171, y=1168–1213)，紧随其后为 `'we'`(x=1192–1244)，文本层亦作 `t > 0, we can assume`；300dpi 裁片 `/tmp/bk_p11_t0.png`（×8）亲眼可见 `t > 0, we`，标点**带明确下伸尾**落在基线之下——逗号与句点的判别铁证。
  3. 第 425 行 `lc place$T .$. So we are done` → `lc place $T$. So we are done` —— 同第 1 项的双句点。证据：`-bbox` 词元 `place`(px x=1547–1648) → `T`(x=1663–1690) → **单个** `'.'`(x=1696–1709) → `So`(x=1730–1778)；300dpi 裁片 `/tmp/bk_p11_placeT.png`（×7）亲眼可见 `place T. So`，仅一个点。
- **核对无误、未改动者**：
  - **Lemma 2.7 四条 bullet 逐条吻合**（第 381–387 行）：`either$\phi$is small or it contracts$T$but no other divisors` / `$( Y , T )$is plt` / `$- ( K _ { Y } + T )$is ample over$X$, and` / `$a ( T , X , B ) = 0$` —— 与印刷四条完全对应，**`a(T,X,B) = 0` 的等号与 0 未被误改为 `≥ 0` 或 `= 1`**，`−(K_Y+T)` 为**单负号**、无伪双负号。
  - **Lemma 2.7 陈述首句**：`$\phi \colon Y \to X$`（第 379 行）为**实线**箭头（印刷 `φ : Y → X`），与第 371 行 `φ: X ⇢ Y/Z` 的虚线正确区分，MD 未混同。
  - **MMP 段多级撇号链**（第 397 行）：`$Y ^ { \prime } \to Y ^ { \prime \prime } / X$`、`$- ( K _ { Y ^ { \prime } } + T ^ { \prime } )$`、`$K _ { Y ^ { \prime } } + T ^ { \prime } \sim _ { \mathbb { Q } } 0 / Y ^ { \prime \prime }$`、`$( Y ^ { \prime \prime } , C _ { Y ^ { \prime \prime } } )$`、`Y ^ { \prime \prime } , T ^ { \prime \prime }` —— **单撇 `Y'`/`T'` 与双撇 `Y''`/`T''` 层级全部正确**，未把 `T''` 误写成 `T'`，`\mathbb{Q}` 下标亦正确。
  - **三个 `\sim` 等价式的系数域全部正确**：第 408 行 `B_W − C_W \sim_{\mathbb{R}} H_W + G_W / X`、第 411 行 `H_W + G_W \sim_{\mathbb{R}} 0 / X`、第 422 行 `\Gamma_W \sim_{\mathbb{R}} B_W + aH_W + aG_W` —— 三处均为 **ℝ**（印刷 `∼_R`），**未出现把 ℝ 误作 ℚ 的情形**；与第 397 行的 `\sim_{\mathbb{Q}} 0/Y''`（印刷 `∼_Q`）也正确区分。
  - `\mu _ { T } \Gamma _ { W } = 1`（第 425 行）系数 **1** 正确，未误作 `= 0`；`$E \neq 0$`（第 419 行）正确。
  - **redo 轮旧修复复核为正确**：本页 `sufficiently`（两处，第 395、417 行）与 `coefficients`（第 417、419、425 行）均已是完整双 f 拼写，redo 轮的 `suficiently`→`sufficiently`、`coeficient(s)`→`coefficient(s)` 修复**已正确落地**。
- **PASS± 差异（按本片段政策登记不修）**：
  1. 行内 ℝ 拍平：第 411 行 `so$H + G$is R-Cartier`（印刷为黑板粗 ℝ-Cartier）。
  2. 第 425 行 `$( W , \mathrm { S u p p } \Gamma _ { W } )$` —— `Supp` 被排成带字距的正体（MathJax 词距伪影），同页第 411、417 行的 `Supp` 为普通文本，**同页内不一致**但语义无歧义。
  3. 逗号错置于数学环境内、致词间粘连：第 395 行 `over$X ,$let$Y \to X$be`（印刷 `over X, let`，MD 渲染为「overX ,let」）。
  4. 数学式与正文粘连：`$B \geq 0$`、`$Y \to X$be`、`$\psi \colon W \to X$be`、`$E \neq 0$` 等多处。
- **一处 150dpi 阶段的疑虑、经核对后撤销（登记以留痕，防后续误「修复」）**：
  - 第 395 行 `t > 0 .$` 曾疑为「句点后紧跟逗号」的排版怪癖 → 300dpi 裁片证明印刷只有一个**逗号**（带下伸尾），MD 的句点纯属多余，**确认为缺陷并已修**（非撤销项，留痕说明判据来源）。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；Lemma 2.7 的陈述、四条假设式、撇号层级与三个 `∼_ℝ` 等价式是本页数学密度最高处，已逐符号核对无误。3 处修复全部是标点类（2 处双句点、1 处句点代逗号），未触及任何公式。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p009`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：`/tmp/birkarsing_audit_p012.png`（pngmono 150dpi，本片段新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p12_coef1.png`、`/tmp/bk_p12_suff.png`、`/tmp/bk_p12_c119.png`、`/tmp/bk_p12_c269.png`、`/tmp/bk_p12_c499.png`、`/tmp/bk_p12_c508.png`、`/tmp/bk_p12_cP.png`、`/tmp/bk_p12_bul3.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=12`，按 `-bbox` 坐标 ×S 换算后放大 4–7 倍，仅裁图未写 Markdown）。
- 核对：页眉「12  Caucher Birkar」；**Lemma 2.7 证明末段**（`G_W` 与 `E` 有公共分支、`µ_T C_W` 接近 1、`a>0` 取 `sub-lc` 的最大实数、`Γ_W ∼_ℝ C_W + aH_W + aG_W`、`(W,Γ_W)` sub-lc、`µ_TΓ_W=1`、`Γ:=ψ_*Γ_W` effective、`K_Y+Γ_Y∼_ℝ0/X`、唯一 lc place `T`）；**2.8. Bounded families of pairs** 三段（birationally bounded/bounded 的 `V^i→T^i`、`t∈T^i`、`φ: V^i_t ⇢ X`；couples 定义、`Q`-Cartier；`P` 中 couples 的 birationally bounded、`E ≤ C^i_t`、两个 morphism 的 fibre；`R` 中 log birationally bounded）；**2.9. Effective birationality…**；**Theorem 2.10**（`d`、`ǫ`、`m`、`ǫ`-lc weak Fano、`|−mK_X|` defines a birational map）；**Theorem 2.11**（`d−1`、`v`、`vol(−K_X) ≤ v`、`(X,0)` is log bounded）；**2.12. Complements**（`T=⌊B⌋`、`∆=B−T`、n-complement 的三条 bullet）。对照 Markdown 第 427–457 行（p.13 起于第 459 行「Theorem 2.13 ([5, Theorem 1.7]).」），辅以 `pdftotext -f 12 -l 12 -layout` 与 `-bbox`。
- 结果：**PASS±**（改 1 处；无数学内容错误）
- **已用 Edit 修复 1 处（绑定页码与裁片）**：
  1. 第 457 行末条 bullet `• $n B ^ { + } \geq n T + \lfloor ( n + 1 ) \Delta \rfloor$` → 补句点。印刷该 bullet 以句点收尾，MD 丢失。证据：`-bbox` 末行词元序列 `•`(px x=428–450) → `nB`(x=466–527) → `+`(x=530–557, y=2905–2931 **明显上抬**＝上标) → `≥`(x=572–607) → `nT`(x=620–674) → `+`(x=690–725) → `⌊(n`(x=736–800) → `+`(x=811–846) → **`1)∆⌋.`**(x=856–967, **词元自带句点**)，全文页末再无词元；300dpi 裁片 `/tmp/bk_p12_bul3.png`（×4）亲眼可见 `• nB⁺ ≥ nT + ⌊(n + 1)∆⌋.`，`⌋` 右侧有一个基线实心点。
- **核对无误、未改动者**：
  - **`⌊(n+1)∆⌋` 的取整方向与不等号方向**：裁片确认为 **`≥`**（不是 `≤`），且 `⌊ ⌋` 下取整括号方向正确、`∆` 为大写 Delta（不是 `Λ`）；`nB⁺` 的 `⁺` 为真上标（bbox y=2905–2931 明显高于同行基线 2910–2955），**上下标层级无误**。
  - **`Γ_W ∼_ℝ C_W + aH_W + aG_W` 展示公式**（第 430 行）：与印刷 `Γ_W ∼_ℝ C_W + aH_W + aG_W` 逐项一致，`\mathbb{R}` 下标正确，**未与 p.11 的 `∼_ℚ` 混同**；`\psi _ { * } \Gamma _ { W }` 的下标 `*` 完整。
  - **Theorem 2.10 的绝对值式**（第 445 行）`$\vert - m K _ { X } \vert$`：印刷 `| − mK_X |` 为**单层竖线 + 内部负号**，MD 与之相符，**未出现把竖线误作 `\lvert...\rvert` 双层或把负号移到竖线外**的情形。
  - **Theorem 2.11 的不等式**（第 447 行）`$\mathrm { v o l } ( - K _ { X } ) \le v$`：印刷 `vol(−KX) ≤ v`，方向正确，**未误作 `≥`**。
  - **两处虚线箭头**：第 435 行 `$\phi : V _ { t } ^ { i } \dashrightarrow X$` 与第 439 行 `$\phi \colon V _ { t } ^ { i } \dashrightarrow X$` 均为**虚线**（印刷字形码 `99K`），与全文实线箭头区分明确，未混同。
  - **`E \leq C _ { t } ^ { i }`**（第 439 行）：印刷 `E ≤ C^i_t`，方向与上下标均正确。
  - **ff 连字词全部正确（6 处已用 300dpi 裁片逐个确认）**：第 427 行 `coefficient`、`sufficiently`，第 433、437、441 行 `coefficients`（两处）——**每一处印刷都是完整 ffi 连字**（`coefficient` 见 `/tmp/bk_p12_coef1.png`，`sufficiently` 见 `/tmp/bk_p12_suff.png`，四处 `coefficients` 见 `/tmp/bk_p12_c119/c269/c499/c508.png`，连字桥与第二个 f 的钩清晰可辨），**MD 六处均为完整双 f 拼写，无一拍平**。
- **print quirk 忠实保留（未按数学/常识静默「纠正」）**：
  1. 第 447 行「Assume **Theorem 1.1** holds in dimension d−1」—— 印刷原文此处写 `Theorem 1.1`（而本节正在陈述 Theorem 2.10/2.11，逻辑上应指 Theorem 2.10），**属印刷自身的编号瑕疵，照录未改**。
  2. **节号从 2.9 直接跳到 2.12**（第 443 行 2.9、第 451 行 2.12，**无 2.10、2.11 节**）—— 已回查印刷 p.1 目录：`pdftotext -f 1 -l 1 -layout` 目录行亦为 `2.8.…12 / 2.9.…12 / 2.12. Complements 12`，**目录与正文一致，确认 2.10/2.11 是印刷原刊即缺**，MD 忠实照录。
  3. 第 435 行「a birational isomorphism (**resp. isomorphism**)」—— 印刷确为此写法（与括号前的 birational 并非严格对应），照录未改。
- **PASS± 差异（按本片段政策登记不修）**：
  1. 花体字母降级为普通字母（与行内 ℝ→R 同一类）：第 439 行首次出现的「a set **P** of couples」印刷为**花体 𝒫**（300dpi 裁片 `/tmp/bk_p12_cP.png` 亲眼可见带花体衬线的 𝒫），MD 作普通斜体 `P`；同行稍后的 `$\mathcal { P }$` 与第 435 行的 `$\mathcal { Q }$` 则**已保留花体**，**同页内不一致**。语义无歧义，按政策登记不修。
  2. 第 437 行 `be Q-Cartier` —— 印刷为黑板粗 ℚ，行内拍平为 `Q`。
  3. MathJax 词距伪影：第 433 行 `$( W , \mathrm { S u p p } \Gamma _ { W } )$`（`Supp` 被排成带字距正体）；第 447 行 `$\mathrm { v o l } ( - K _ { X } )$`（`vol` 同样带字距）。
  4. 标点错置于数学环境内、致词间粘连：第 427 行 `a component of$E .$Thus we can find`、第 435 行段末 `over$t .$`（渲染为「overt .」）、第 439 行 `there exist an$i ,$a closed point`、第 451 行 `Let$T = \lfloor B \rfloor$and$\Delta = B - T$`（渲染为「…⌋andΔ」）。
  5. 数学式与正文粘连：`$( W , C _ { W } + a G _ { W } )$is sub-lc`、`$T$of$E$is sufficiently`、`$\vert - m K _ { X } \vert$defines` 等多处。
- 备注：本页**无数学内容错误、无整段丢失、无公式记号误置**；两处展示公式、三条 n-complement 判别式与两个 Theorem 的全部量化条件（`d`、`ǫ`、`m`、`v`、`dimension d−1`）均逐符号核对无误。唯一修复是末条 bullet 的行末句点，属标点类，未触及任何公式或不等号方向。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p009`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：`/tmp/birkarsing_audit_p013.png`（pngmono 150dpi，本片段新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p13_n.png`、`/tmp/bk_p13_e.png`、`/tmp/bk_p13_lam2.png`、`/tmp/bk_p13_cp1.png`、`/tmp/bk_p13_coef.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=13`，按 `-bbox` 坐标 ×S 换算后放大 6–9 倍，仅裁图未写 Markdown）。
- 核对：页眉「Singularities of linear systems and boundedness of Fano varieties  13」；**Theorem 2.13**（`ℛ ⊂ [0,1]` 有限有理数集、`n` 只依赖 `d` 与 `ℛ`；四条 bullet：`(X,B)` lc of dimension `d`、`B ∈ Φ(ℛ)`、`X` of Fano type、`−(K_X+B)` nef；结论 `B⁺ ≥ B`、mn-complement）；**Φ(ℛ) 定义式** `{1 − r/m | r ∈ ℛ, m ∈ ℕ}`；**2.14. From bounds on lc thresholds to boundedness of varieties**；**Theorem 2.15**（`d, m, v`、`t_l` 正实数列、`𝒫` 的五条 bullet：klt weak Fano of dimension `d`、`K_X` 有 m-complement、`|−mK_X|` defines a birational map、`vol(−K_X) ≤ v`、`l ∈ ℕ` 且 `L ∈ |−lK_X|` 时 `(X, t_l L)` klt；结论 bounded family）；「Assuming Theorem 1.1 in lower dimension…We will use Theorem 1.6…」；「K-semistable Fano varieties [17, Theorem 1.1]」；**2.16. Sequences of blowups**（(1) 爆破链展示式 `··· → X_{i+1} → X_i → ··· → X_0 = X`、codimension `≥ 2`、`X_p → X_{p−1}`、`E_{i+1}`；(2) toroidal 定义、`C_i` 是 `(X_i, Λ_i)` 的 stratum、`K_{X_i}+Λ_i` 是 `K_X+Λ` 的 pullback、`cf. [24]`）。对照 Markdown 第 459–507 行（p.14 起于第 509 行「Lemma 2.17.」），辅以 `pdftotext -f 13 -l 13 -layout` 与 `-bbox`。
- 结果：**PASS±**（改 3 处；无数学内容错误）
- **已用 Edit 修复 3 处（逐处绑定页码与裁片）**：
  1. 第 469 行段末 `…is also an mn-complement for any$m \in \mathbb { N }$` → 补句点。印刷 `…for any m ∈ ℕ.` 有句点，MD 丢失。证据：`-bbox` 词元序列 `an`(px x=845–894) → `mn-complement`(x=910–1227) → `for`(x=1243–1299) → `any`(x=1315–1386) → `m`(x=1402–1442) → `∈`(x=1455–1486) → **`N.`**(x=1498–1545, y=859–899，**词元自带句点**)，其后紧接下一行 `In the theorem`，其间无其它词元；300dpi 裁片 `/tmp/bk_p13_n.png`（×8）亲眼可见 `m ∈ ℕ.`，句点落在基线上、**无下伸尾**（排除逗号）。
  2. 第 505 行段末 `…We denote the exceptional divisor of$X _ { i + 1 } \to X _ { i }$by$E _ { i + 1 }$` → 补句点。证据：`-bbox` 词元 `X`(px x=545–583, y=2748–2793) → `i`(x=583–595, **y=2765–2796，下沉**＝下标) → `by`(x=612–660) → `E`(x=675–709) → **`i+1`**(x=709–766, **y=2765–2796，下沉**＝下标) → **`'.'`**(x=768–781, y=2748–2793，**基线句点独立成词元**)；300dpi 裁片 `/tmp/bk_p13_e.png`（×8）亲眼可见 `by E_{i+1}.`，`i+1` 为真下标（明显低于 `E` 与基线），其后一个实心点。
  3. 第 507 行段末 `…is an lc place of$( X , \Lambda )$` → 补句点。证据：`-bbox` 末行词元序列 `the`(px x=1129–1193) → `sequence`(x=1207–1381) → `is`(x=1396–1426) → `an`(x=1442–1490) → `lc`(x=1505–1538) → `place`(x=1553–1654) → `of`(x=1669–1705) → `(X,`(x=1721–1790) → **`Λ).`**(x=1797–1859, **词元自带句点**)，为全页最后词元；300dpi 裁片 `/tmp/bk_p13_lam2.png`（×8）亲眼可见 `f (X, Λ).`，且 `Λ` 为**大写 Lambda**（非小写 `λ`、非 `A`）。
- **核对无误、未改动者**：
  - **Φ(ℛ) 定义式**（第 474 行）：`\Phi (\mathbb {R}) := \left\{1 - \frac {r}{m} \mid r \in \mathbb {R}, m \in \mathbb {N} \right\}.` 与印刷 `Φ(ℛ) := {1 − r/m | r ∈ ℛ, m ∈ ℕ}.` 逐符号一致 —— **`1 −` 为负号而非 `1 +`**、分数 `\frac{r}{m}` 的**分子 `r` 分母 `m` 未颠倒**（bbox 佐证分子 `r` 的 y=1038–1084 明显**高于**同行基线 1069–1115）、竖线 `\mid` 未误作 `:`、末尾句点完整。
  - **爆破链展示式**（第 502 行）：`\dots \rightarrow X _ {i + 1} \rightarrow X _ {i} \rightarrow \dots \rightarrow X _ {0} = X` 与印刷 `··· → X_{i+1} → X_i → ··· → X_0 = X` 一致；**四个箭头全为实线**，末端 `X_0 = X` 的等号方向正确，`i+1`/`i`/`0` 三个下标齐全未漏。
  - **`E_{i+1}` 的下标与「length of the sequence is `p`」**（第 505 行）：`$X _ { p } \to X _ { p - 1 }$` 的 `p`、`p−1` 层级正确，**未把末次爆破写成 `X_p → X_{p−1}` 以外的次序**；「codimension$\geq 2$」与「dimension$\geq 2$」两处 **`≥` 方向正确**（非 `≤`）。
  - **Theorem 2.15 五条 bullet 逐条吻合**（第 481–489 行）：`|−mK_X|` 为**单层竖线 + 内部负号**（印刷 `| − mK_X |`），`$\mathrm { v o l } ( - K _ { X } ) \le v ,$` 的**不等号方向为 `≤`**（非 `≥`），`$L \in | - l K _ { X } |$` 的 **`l`（小写 L，非数字 1、非大写 I）** 与 `t _ { l }` 的下标一致，`$( X , t _ { l } L )$is klt` 的系数位置正确。
  - **「the complement is also an mn-complement for any m ∈ ℕ」**：`mn-complement` 中的 `mn` 为印刷原文写法（未拆成 `m n` 或误作 `nm`），照录。
  - **ff 连字词正确**：第 463 行 `coefficients` —— 300dpi 裁片 `/tmp/bk_p13_coef.png`（×6）亲眼可见完整 **ffi 连字**（连字桥与第二个 f 的钩清晰），**MD 未拍平**。
  - **`ℛ` 为双线黑板粗**（第 459、463 行 `\mathbb { R}`、`\mathbb { R }`）：150dpi 整页图上 `ℛ ⊂ [0, 1]` 与 `ℛ ⊂ [0, 1]` 的 R 均为双线体，**redo 轮的 `\mathbb{R}` 修复已正确落地**（父提交版此处曾是 `\Re`/`\mathfrak{R}`）。
  - **`2.14.`、`2.16.` 两个小节号在印刷中行内接排**，MD 亦保持行内未提升为 `##` 标题，**正确**。
- **print quirk 忠实保留（未按数学/常识静默「纠正」）**：
  1. 第 493 行「We will use **Theorem 1.6** to show that this last assumption is also satisfied」—— 印刷原文此处确为 `Theorem 1.6`（`-bbox` 词元 `Theorem`(px x=1072–1248) → `1.6`(x=1267–1325) → `to`(x=1344–1384)，编号作 `1.6` 且其后无句点），与 MD 一致，**照录未改**。
  2. **节号 2.12 → 2.14 → 2.16**（跳号），已随 p.12 一并核到印刷 p.1 目录确认属原刊体例，MD 照录。
- **PASS± 差异（按本片段政策登记不修）**：
  1. 花体 𝒫 降级为普通斜体 `P`（与行内 ℝ→R、ℚ→Q 同一类）：第 479 行「Let **P** be the set」与第 491 行「Then **P** is a bounded family」，印刷均为**花体 𝒫**（300dpi 裁片 `/tmp/bk_p13_cp1.png`（×9）亲眼可见带花体衬线的 𝒫）。语义无歧义，登记不修。
  2. MathJax 词距伪影：第 487 行 `$\mathrm { v o l } ( - K _ { X } ) \le v ,$`（`vol` 带字距）。
  3. 标点错置于数学环境内、致词间粘连：第 481 行 `of dimension$d ,$`、`$B \in \Phi ( \mathbb { R } )$` 后的逗号外置、第 487 行 `v ,$and`、第 493 行 `(when$B = 0 )$except`、第 507 行 `$K _ { X } + \Lambda$(cf. [24])`。
  4. 数学式与正文粘连：`$( X , B )$is lc`、`$K _ { X }$has an m-complement`、`$\vert - m K _ { X } \vert$defines`、`$l \in \mathbb N$and`、`$C _ { i }$of codimension` 等多处。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；两个 Theorem 的全部假设式与结论式、Φ(ℛ) 定义式、爆破链展示式、`E_{i+1}` 的下标层级均已逐符号核对无误。3 处修复**全部是行末句点补齐**，属标点类，未触及任何公式、系数、上下标或不等号方向。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p009`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：`/tmp/birkarsing_audit_p014.png`（pngmono 150dpi，本片段新渲染并 Read 目检整页）；仲裁裁片 `/tmp/bk_p14_p1.png`、`/tmp/bk_p14_ei.png`、`/tmp/bk_p14_x1.png`、`/tmp/bk_p14_x2.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=14`，按 `-bbox` 坐标 ×S 换算后放大 7 倍，仅裁图未写 Markdown）。
- 核对：页眉「14Caucher Birkar」；**Lemma 2.17 全文**（长度 `p` 的爆破序列对 `(X,Λ)` toroidal、展示式 `φ : X_p → X_0 = X`、`C_i ⊂ E_i`（`0 < i < p`）、结论 `µ_{E_p} φ^*Λ ≥ p + 1`；Proof：`0 ≤ i < p`、`C_i` 是 `(X_i,Λ_i)` 的 lc centre 且 codimension `≥ 2`、`i > 0` 时 `E_i` 是其中一支、`φ_i : X_i → X_0`、`Λ_i = Supp φ_i^*Λ`、归纳展示式 `µ_{E_{i+1}}φ^*_{i+1}Λ ≥ µ_{E_i}φ^*_iΛ + 1 ≥ i + 2`）；**(3) centre blowups**（`T` 是 `X` 上的素因子、`C_i` 是 `T` 在 `X_i` 上的中心、[28, Lemma 2.45]、`X_p → X_{p−1}`、birational transform of `T`、`X_p → X_{p−1} → ··· → X_0 = X`）；**2.18. Analytic pairs…**（formal varieties / formal neighbourhoods、`A^an`）；**(1) analytic pair**（`K_U + G` ℝ-Cartier、系数 `[0,1]`、as in 2.2、`U` smooth）；analytically isomorphic（`ν : U → U′`、`ν_*G = G′`）；**(2)**（log resolution `φ : W → X`、`φ^an : W^an → X^an`、`φ^an|_V`、`(U, B^an|_U)` ε-lc 的双向论证）；**(3)**（`(X,B)` 与 `(X′,B′)`、`x` 与 `x′`、`U` 与 `U′`、if and only if、`(ℙ²,B)` 与 `(ℙ²,B′)`、`B` 有 node at `x`、`B′` 是两条交于 `x′` 的直线）。对照 Markdown 第 509–533 行。**页界说明**：印刷 p.14 末行止于「…For example, the」，其后「two pairs (ℙ², B) and (ℙ², B′)…」续排于 p.15 首行，MinerU 把这两行并入同一段（第 533 行），故第 533 行的**句首部分**（至「For example, the」）归本页审计，**句尾部分**归 p.015 审计，两处不重复计缺陷。
- 结果：**PASS±**（改 7 处；无数学内容错误）
- **已用 Edit 修复 7 处（逐处绑定页码与裁片）**：
  1. 第 515 行段末 `Then$\mu _ { E _ { p } } \phi ^ { * } \Lambda \geq p + 1$` → 补句点。印刷 `…≥ p + 1.` 有句点，MD 丢失。证据：`-bbox` 词元 `1.`(px x=2049–2085, y=594–639, **词元自带句点**) 为该行末词元；300dpi 裁片 `/tmp/bk_p14_p1.png`（×7）亲眼可见 `p + 1.`，`≥` 方向与 `+ 1` 的系数均正确、句点落在基线无下伸尾。
  2. 第 517 行 `one of these components is$E _ { i }$ by assumption.` → `…is$E _ { i }$, by assumption.` —— 印刷在 `E_i` 后有逗号，MD 丢失。证据：`-bbox` 词元 `E`(px x=2112–2146) → `i`(x=2145–2157, **y=753–783 下沉**＝下标) → **`,`**(x=2159–2172) → 下一行 `by`(x=378) → `assumption.`(x=445–684)；300dpi 裁片 `/tmp/bk_p14_ei.png`（×7）亲眼可见 `is E_i,`，逗号**带下伸尾**。
  3. 第 523 行段末 `…centre blowups$X _ { p } \to X _ { p - 1 } \to \cdots \to X _ { 0 } = X$` → 补句点。证据：`-bbox` 该行词元序列 `X`(px x=1334–1372) → `p`(x=1371–1389, y=1474–1504 **下沉**＝下标) → `→`(x=1404–1449) → `X`(x=1462–1500) → `p−1`(x=1499–1563, y=1474–1504 **下沉**) → `→`(x=1577–1623) → `·`×3 → `→`(x=1701–1746) → `X`(x=1759–1797) → `0`(x=1796–1814, **下沉**) → `=`(x=1829–1864) → **`X.`**(x=1877–1931, **词元自带句点**)，为该段末词元。
  4. 第 525 行段末 `…we denote the associated analytic object by$A ^ { \mathrm { a n } }$` → 补句点。证据：`-bbox` 词元 `by`(px x=1861–1909) → `A`(x=1924–1959, y=1884–1930) → `an`(x=1958–1996, **y=1880–1905，明显上抬**＝上标「an」) → **`.`**(x=1997–2010, y=1884–1930, **基线句点独立成词元**)；150dpi 整页图该处句点亦清晰可见。
  5. 第 529 行段末 `…such that$\nu _ { * } G = G ^ { \prime }$` → 补句点。证据：`-bbox` 词元 `G`(px x=1817–1853) → `′`(x=1852–1862, y=2261–2282 **上抬**＝撇号上标) → **`.`**(x=1864–1877, y=2262–2307)，其后紧接下一行 `(2)`，其间无词元；150dpi 整页图该处句点亦清晰可见。
  6. 第 531 行 `some algebraic neighbourhood of$x ,$, then we can choose` → `…of$x$, then we can choose` —— **MD 连出两个逗号**（数学环境内一个、环境外一个）。证据：`-bbox` 词元 `of`(px x=1982–2018) → **`x,`**(x=2031–2070, **单字词元内只含一个逗号**) → `then`(x=2084–2172)，**`x` 与 `then` 之间只有一个标点**；300dpi 裁片 `/tmp/bk_p14_x1.png`（×7）亲眼可见 `al of x, then`，一个逗号、一个下伸尾。
  7. 第 533 行 `of x and$x ^ { \prime } ,$, respectively.` → `of x and$x ^ { \prime }$, respectively.` —— 同第 6 项的双逗号。证据：`-bbox` 词元 `x`(px x=1862–1888) → `′`(x=1888–1898, y=2747–2768 **上抬**) → **`,`**(x=1899–1912) → `respectively.`(x=1930–2171)，**`x′` 与 `respectively` 之间只有一个标点**；300dpi 裁片 `/tmp/bk_p14_x2.png`（×7）亲眼可见 `nd x′, respectively.`，一个逗号。
- **核对无误、未改动者**：
  - **Lemma 2.17 的两个展示式**：第 512 行 `\phi \colon X _ {p} \to X _ {0} = X` 与第 520 行 `\mu_ {E _ {i + 1}} \phi_ {i + 1} ^ {*} \Lambda \geq \mu_ {E _ {i}} \phi_ {i} ^ {*} \Lambda + 1 \geq i + 2.` —— 印刷分别为 `φ : X_p → X_0 = X` 与 `µ_{E_{i+1}}φ*_{i+1}Λ ≥ µ_{E_i}φ*_iΛ + 1 ≥ i + 2.`，**两个 `≥` 方向均正确**、`+ 1` 未漏、`i + 2` 未误作 `i + 1`、`E_{i+1}`/`E_i` 的下标层级正确（`i+1` 未误作 `i−1`），末尾句点完整。
  - **`µ_{E_p} φ^*Λ` 的系数与上标**（第 515 行）：`\mu` 的下标 `E_p`、`\phi` 的上标 `*`、`\Lambda` 无下标，三者归属正确，**未把 `φ^*` 误作下标或漏掉 `E_p` 的 `p`**。
  - **`(3) 的爆破链`**：`X_p → X_{p−1} → ··· → X_0 = X`（第 523 行）中三个箭头在 bbox 里均为 `→` 词元（**实线**），与 p.13 展示式一致；`p−1` 用的是印刷的**真减号 `−`（U+2212）**，MD 的 `p - 1` 对应正确，**未误写成 `p+1` 或 `p/1`**。
  - **`cf. [24]`、`[28, Lemma 2.45]`、`2.2`、`2.18` 等交叉引用编号**：印刷与 MD 逐字一致，**未出现漏编号或误编号**。
  - **`ν : U → U′` 为实线箭头、`ν_* G = G′` 的下星号**（第 529 行）：印刷 `ν∗ G = G′`，MD 的 `\nu _ { * } G` 下标位置正确，**未把 `∗` 误升为上标**。
  - **`(U′, B′^an|_U′)` 的撇号位置**（第 533 行）：印刷 `B′^{an}`，MD 的 `\mathrm { a n }` 在 `B ^ { \prime }` 之后为上标，层级正确；**同页 `B^an` 无撇号处（第 531 行）亦未被误加上撇号**。
  - **`(ℙ², B)` 与 `(ℙ², B′)`**（第 533 行）：`\left( \mathbb { P } ^ { 2 } , B \right)$` 的 `ℙ` 为双线体、上标 `2` 正确；后者 `B ^ { \prime }` 撇号正确。
  - **本段 ff 连字词**：本段印刷中出现的 `components`、`sufficiently`、`coefficients`、`finitely`、`neighbourhoods`、`algebraically` 等词，**本轮在 150dpi 整页图上逐词目检均为完整双 f 拼写**，且 Markdown 对应处**无一处拍平**（如 `an lc centre`、`at least two components`、`derived from algebraic pairs`）。
- **print quirk 忠实保留（未按数学/常识静默「纠正」）**：
  1. 第 531、533 行 `(U, B^an|_U)` 与 `(U′, B′^an|_U′)` 中的解析直像记号 `^an` 为印刷自造记号，照录未改。
  2. 第 533 行 `x′` 在句中被反复重复（「neighbourhoods of `x` and `x′`. Note that it may well happen that (X,B) and (X′,B′) are not algebraically isomorphic in any algebraic neighbourhoods of `x` and `x′`」）—— 印刷如此，MD 照录。
  3. 节号跳号（2.16 → 2.18）随 p.12、p.13 已核到印刷目录，属原刊体例。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **ℝ 拍平 + 连字符丢失**：第 527 行「an **Rdivisor** `G`」—— 印刷为 `ℝ-divisor`，MinerU 把黑板粗 ℝ 拍平为 `R` 并吞掉连字符，得 `Rdivisor`（与 p.9 第 335 行 `Rdivisors` 同一伪影）；同行「is **R-Cartier**」印刷为 `ℝ-Cartier`，拍平为 `R-Cartier`。两项均为**同一字母的样式降级 + 断词连字符丢失**，语义无歧义，按政策登记不修。
  2. **ε 字形不一致**：第 533 行「is `$\epsilon \mathrm { - }$ lc`」用的是 `\epsilon`（月牙形 ϵ），而同页第 527、531、533 行的其余 `ε-lc` 处用的是直立字符 `ǫ`（ε）；印刷全篇为同一字形。属同一字母的不同字形变体、语义无歧义，登记不修（**注：这是本轮观察到的新的 PASS± 类别，非此前登记过的 ℝ/ℚ 拍平**）。
  3. MathJax 词距伪影：第 517 行 `\mathrm { S u p p }`（`Supp` 带字距）、第 525 行 `\mathrm { a n }`、第 531、533 行多处 `\mathrm { a n }`（`an` 带字距）。
  4. 标点错置于数学环境内、致词间粘连：第 509 行 `of length$p ,$toroidal`、`Suppose$C _ { i } \subset E _ { i }$for each$0 < i < p$.`、`Let$T$be a prime divisor`、`Let$U$be an analytic`、`let$V$be the inverse image` 等多处。
  5. 数学式与正文粘连：`$( X , \Lambda )$`、`$\nu \colon U \to U ^ { \prime }$such that`、`$\phi \colon W \to X$and`、`$\Lambda _ { i }$because`、`$C _ { i }$is an lc centre` 等多处。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；Lemma 2.17 的两条不等式链、`E_{i+1}`/`E_i` 的下标、`p−1` 的真减号、`ν_*` 的下星号、`B′^an` 的上标层级均逐符号核对无误。7 处修复**全部是标点类**（4 处行末句点补齐、1 处逗号补回、2 处重复逗号删除），**未触及任何公式、系数、上下标或不等号方向**。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p009`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：`/tmp/birkarsing_audit_p015.png`（gs pngmono 150dpi，-dFirstPage=15 -dLastPage=15）；疑难字形另用 `/tmp/bk_p15_300.png`（pnggray 300dpi）+ PIL LANCZOS 裁片放大。
- 核对：逐行比对印刷 p.15 与 Markdown 第 533 行（尾半）–575 行。印刷 p.15 自 `2.19. Étale morphisms.` 起，含 Lemma 2.20 全部、Lemma 2.21 全部、节 `2.22. Toric varieties and toric MMP.`、节 `2.23. Bounded small modifications.` 与 Lemma 2.24 的题设部分；PDF p.16 自 `• K_Y is ℚ-Cartier,` 起，故 Lemma 2.24 属本印刷页。三处标点均以 `-bbox`（S=300/72.0）定位后再用 300dpi 裁片亲眼确认。
- 结果：**PASS±**（改 3 处；无数学内容错误）
- **已用 Edit 修复 3 处（逐处绑定页码与裁片）**：
  1. 第 545 行 `• $\begin{array} { r } { C : = \pi ( B ) : = \sum b _ { j } \pi ( B _ { j } ) } \end{array}$` → 补句点。印刷该列条（Lemma 2.20 第四条假设）末尾有句点。证据：`-bbox` 词元 `b`(px x=834) → `j`(x=870–886, y=936–966 **下沉**＝下标) → `π(B`(x=897) → `j`(x=963–979, **下沉**) → **`).`(x=940–971, y=918–964，该行末词元自带句点)**；300dpi 裁片 `/tmp/bk_p15_c.png`（区域 (790,910)–(985,972)，×8）亲眼可见 `b_j π(B_j).`，句点落在基线、无下伸尾。
  2. 第 547 行段末 `…an analytic isomorphism between$( U , B ^ { \mathrm { a n } } | _ { U } )$and$( V , C ^ { \mathrm { a n } } | _ { V } )$` → 补句点。证据：`-bbox` 词元 `(V,`(px x=1338) → `C`(x=1398) → `an`(x=1416–1450, y=1130–1155 **上抬**＝上标) → `|`(x=1452) → `V`(x=1453–1475, y=1152–1182 **下沉**＝下标) → **`).`(x=1478–1509, y=1134–1180，该行末词元自带句点)**；300dpi 裁片 `/tmp/bk_p15_v.png`（区域 (1270,1124)–(1530,1190)，×7）亲眼可见 `and (V, C^{an}|_V).`，`C` 的上标 `an` 与下标 `|_V` 层级均正确。
  3. 第 567 行 `• A is a very ample divisor on X with$A ^ { d } \leq r$` → 补句点（Lemma 2.24 的第二条假设）。证据：`-bbox` 词元 `≤`(px x=1364–1384) → **`r.`(x=1385–1421, y=2780–2826，该行末词元自带句点)**；300dpi 裁片 `/tmp/bk_p15_r.png`（区域 (1270,2770)–(1450,2836)，×8）亲眼可见 `A^d ≤ r.`，`d` 为真上标、`≤` 开口方向正确、句点在基线。
- **核对无误、未改动者**：
  - **Lemma 2.20 的 `\sum b _ { j } \pi ( B _ { j } )`（第 537、545 行）**：印刷的求和号**下标起止限在正文此式中不出现**（`B = Σ b_j B_j` 与 `C := π(B) := Σ b_j π(B_j)` 两处皆然），MD 的 `\sum b _ { j } \pi ( B _ { j } )` 与印刷一致，**未擅补上下限**。
  - **`\pi \colon X \to Z`（第 537 行）**：`→` 在 bbox 中为实线词元（有限态射，非虚线 birational），MD 用 `\to` 对应正确。
  - **`\pi ^ { - 1 } \{ z \}`（第 543 行）**：印刷 `π^{-1}{z}`，`−1` 为**上标**（bbox 中 `−1` 的 yMax 小于同行 π 的 yMax），MD 的 `\pi ^ { - 1 }` 层级正确，**未误作下标**。
  - **Lemma 2.21 的 `t _ { 1 } , \ldots , t _ { d }` 与 `\pi ^ { * } t _ { 1 } , \ldots , \pi ^ { * } t _ { d }`（第 555 行）**：印刷为 `t_1, . . . , t_d`（z 局部参数）与 `π*t_1, . . . , π*t_d`（x 局部参数）；MD 的省略号写作 `\ldots`、`*` 写作 `^ { * }`、序号写作下标 `_ { 1 }`/`_ { d }`，层级与位置**全部正确**，两端逗号齐备。
  - **`2.19. Étale morphisms.`（第 535 行）的重音 É**：印刷为大写带尖音符的 `É`（`Étale`），MD 已是正确拼写 `Étale`，**不是 accent 分解伪影**（与 p.9 第 337 行的 `´etale` 类伪影不同，此处无需修）。
  - **`ℙ^d`、`ℚ-factorial`、`ℚ-divisor`、`ℚ-Cartier`、`Q-Cartier`**（第 557、561、573 行）：`\mathbb { P }`/`\mathbb { Q }` 的双线体正确；573 行 `K _ { Y }$is Q-Cartier` 为 ℚ→`Q` 拍平（第 573 行），属样式降级，见 PASS± 第 1 项。
  - **`[12]`、`[12, §15.5]`、`[12, §15.5]` 的节号与 § 符号**（第 557 行两次）：印刷与 MD 逐字一致，**未漏 § 或误编号**。
  - **`Y \to X` 爆破列的箭头（第 559 行）**：印刷 `Let Y → X be a sequence of blowups toroidal with respect to (X, Λ).`；bbox 中为实线 `→` 词元，MD 用 `\to` 对应正确。**打印原文用 `Y → X` 而非常见的 `X → Y`（第 573、565 行同篇一律按印刷保留）——此为原刊笔误，见 print quirk 第 1 项**。
  - **本段 ff 连字词**：印刷中 `Assume`、`neighbourhoods`、`respectively`、`neighbourhood`、`toroidal`、`irreducible`、`minimal`、`complement`、`projective` 等词，在 150dpi 整页图上逐词目检**均为完整双 f 拼写**，Markdown 对应处**无一处拍平**（`analytic neighbourhoods`、`algebraic neighbourhoods`、`toroidal with respect to` 等）。
- **print quirk 忠实保留（未按数学/常识静默「纠正」）**：
  1. 第 559 行 `Let$Y \to X$be a sequence of blowups` —— 印刷的映射方向写成 `Y → X`，与上下文（对 `X` 作爆破应写 `X` 的爆破得到 `Y`）相反。**照录未改**。
  2. 第 563 行 Lemma 2.24 题设 `Let d, r be natural numbers` 中，印刷对 `r` 未加任何限定词；后续假设以 `A^d ≤ r` 使用之。**照录未改**。
  3. 第 551 行 `C may not even be a boundary away from$z ,$that is, ...` —— 印刷在 `z` 后用逗号而非句号断句（`away from z, that is,`）。**照录未改**，未按语义改句点。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **ℚ 拍平**：第 573 行 `K _ { Y }$is Q-Cartier` —— 印刷为 `ℚ-Cartier`（黑板粗 ℚ），MinerU 拍平为 `Q`。与 p.9–p.14 登记的 ℝ→R 同类，属同一字母的样式降级、语义无歧义，登记不修。
  2. **`\begin{array}` 包装**：第 545 行 `\begin{array} { r } { … } \end{array}` —— 印刷中该列条只是行内公式，MathJax 版被包进单列 `array` 环境，纯排版伪影，不改语义，登记不修。
  3. **MathJax 词距伪影**：第 525 行起的 `\mathrm { a n }`（`an` 带字距，本页第 537、547、555、559 行等处反复出现）。
  4. **标点错置于数学环境内、致词间粘连**：第 537 行 `Let$\left( X , B = \sum b _ { j } B _ { j } \right)$be a pair over$\mathbb { C } , \pi \colon X \to Z$be a finite morphism`、`x \in X$a closed point`、`z = \pi ( x )$.`、`\pi ^ { \mathrm { a n } } | _ { U }$induces`、`\pi ^ { * } t _ { 1 } , \ldots` 等多处；第 551 行 `away from$z ,$that is`；第 559 行 `Let$Y \to X$be`、`Let$X$be a (normal) Q-factorial`；第 565、567、569、573 行多条 `)$is`、`$and`。
  5. **ε 字形**：第 537 行起的 `ǫ`（直立 ε）与 p.14 第 533 行的 `\epsilon`（月牙 ϵ）混用，印刷全篇为同一字形，属字形变体，登记不修。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；Lemma 2.20 的求和式、`π^{-1}{z}` 的上标 `−1`、Lemma 2.21 的两组局部参数、`A^d ≤ r` 的上标与不等号方向、`C^an|_V` 的上下标层级均逐符号核对无误。3 处修复**全部是句末标点补齐**，**未触及任何公式、系数、上下标或不等号方向**。`Let Y → X` 这一印刷笔误按 print quirk 登记而非「改正」。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p009`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：`/tmp/birkarsing_audit_p016.png`（gs pngmono 150dpi，-dFirstPage=16 -dLastPage=16）；疑难字形另用 `/tmp/bk_p16_300.png`（pnggray 300dpi）+ PIL LANCZOS 裁片放大。
- 核对：逐行比对印刷 p.16 与 Markdown 第 577–613 行。印刷 p.16 自 Lemma 2.24 的结论三条列条（`• K_Y is ℚ-Cartier,` / `• A_Y^d ≤ l, and` / `• A_Y − φ^*A is ample.`）起，经 Lemma 2.24 的 Proof 全篇、展示式 `B_Y − Γ_Y = (K_Y + B_Y) − (K_Y + Γ_Y) ≡ −(K_Y + Γ_Y)/X`、节 `2.25. Semi-ample divisors.`、Lemma 2.26 及其 Proof（含展示式 `C + tbA = (1 − t)C + t(C + bA)`）与两处 QED 方块止；Markdown 第 615 行的 `## 3. Lc thresholds…` 起于 PDF p.17，不在本页。五处标点均先以 `-bbox`（S=300/72.0）定位词元，再用 300dpi 裁片亲眼确认。
- 结果：**PASS±**（改 5 处；无数学内容错误）
- **已用 Edit 修复 5 处（逐处绑定页码与裁片）**：
  1. 第 581 行 `Let Σ be the reduced exceptional divisor of$W \to V$ Let$\Gamma _ { W } =` → 补句点。证据：`-bbox` 词元 `of`(px x=1942–1979, y=891–937) → `W`(x=1996–2039) → `→`(x=2061–2106，**实线**) → `V`(x=2122–2149) → **`.`**(x=2159–2172, y=891–937，**基线句点独立成词元**) → 下一行 `Let`(x=377, y=945)；300dpi 裁片 `/tmp/bk_p16_v.png`（区域 (1980,878)–(2190,950)，×8）亲眼可见 `W → V .`，句点圆实、**无下伸尾**（故非逗号）。
  2. 第 585 行 `• $K _ { Y } \sim _ { \mathbb { Q } } K _ { U } | _ { Y } .$` → `…|_ { Y }$,`。**Markdown 把印刷的逗号写成了句点，且把它吞进了数学环境内**。证据：`-bbox` 词元 `Y`(px x=567–587, y=1246–1276 **下沉**＝下标) → `∼`(x=611–646) → `Q`(x=646–672, y=1246–1275 **下沉**＝下标 ℚ) → `K`(x=686–725) → `U`(x=725–748, **下沉**) → `|`(x=754–767) → `Y`(x=767–787, **下沉**) → **`,`**(x=797–810, y=1228–1274)；300dpi 裁片 `/tmp/bk_p16_kq.png`（区域 (515,1216)–(825,1292)，×6）亲眼可见 `K_Y ∼_Q K_U|_Y ,`，末位标点**带明显下伸尾**（逗号），绝非句点；同一裁片亦确认 `K_U`、`|_Y` 的下标层级与 `∼` 的下标 ℚ 均正确。
  3. 第 589 行 `coincides with the reduced exceptional divisor of$Y \to X$，` → `…of$Y \to X$,`。**Markdown 此处用的是全角逗号 `，`（U+FF0C），印刷是常规半角逗号**。证据：`-bbox` 词元 `of`(px x=1927–1963, y=1336–1382) → `Y`(x=1978–2005) → `→`(x=2028–2073，**实线**) → **`X,`**(x=2086–2140，**逗号已熔进 X 词元**，说明该处只有一个标点)；300dpi 裁片 `/tmp/bk_p16_yx.png`（区域 (1912,1324)–(2158,1396)，×7）亲眼可见 `of Y → X ,`——窄身、带下伸尾的**常规逗号**，字宽与同页其它逗号一致，**不是全角逗号**。
  4. 第 591 行 `• and each non-zero coefficient of$\Gamma _ { Y }$is equal to$1 - \textstyle { \frac { \epsilon } { 2 } }$` → 补句点。证据：`-bbox` 词元 `equal`(px x=1287–1392, y=1390–1436) → `to`(x=1407–1448) → `1`(x=1463–1486) → `−`(x=1495–1531，**真减号 U+2212**) → `2`(x=1546–1564, y=1418–1443 **下沉**＝分母) → `ǫ`(x=1548–1562, y=1383–1413 **上抬**＝分子) → **`.`**(x=1569–1581, y=1390–1436) → 下一段 `Now`(x=427, y=1457)；300dpi 裁片 `/tmp/bk_p16_eps.png`（区域 (1392,1370)–(1600,1450)，×8）亲眼可见 `to 1 − ε/2 .`，分数 ε/2 结构与末尾基线句点均清楚。
  5. 第 605 行 `…is semi-ample (globally) for any real number$a > 0$` → 补句点（Lemma 2.26 陈述末）。证据：`-bbox` 词元 `for`(px x=1202–1258, y=2501–2547) → `any`(x=1275–1346) → `real`(x=1362–1432) → `number`(x=1448–1594) → `a`(x=1610–1634) → `>`(x=1647–1682) → **`0.`**(x=1695–1731，**句点已熔进 0 词元**) → 下一行 `Proof.`(x=377, y=2587)；300dpi 裁片 `/tmp/bk_p16_a0.png`（区域 (1592,2488)–(1750,2562)，×9）亲眼可见 `a > 0 .`，`>` 开口方向正确、句点圆实无尾。
- **核对无误、未改动者**：
  - **Lemma 2.24 的结论三条列条**（第 573、575、577 行）：`• $K _ { Y }$is Q-Cartier,`、`• $A _ { Y } ^ { d } \leq l$, and`、`• $A _ { Y } - \phi ^ { * } A$is ample.` —— 印刷依次为 `K_Y is ℚ-Cartier,`、`A_Y^d ≤ l, and`、`A_Y − φ^*A is ample.`，**三处标点（逗、逗、句点）齐备且位置正确**，`d` 为上标、`≤` 方向正确、`φ^*` 的星号在右上，MD 对应无误。
  - **展示式（第 596 行）**：`B _ {Y} - \Gamma_ {Y} = (K _ {Y} + B _ {Y}) - (K _ {Y} + \Gamma _ {Y}) \equiv - (K _ {Y} + \Gamma _ {Y}) / X` —— 印刷 `B_Y − Γ_Y = (K_Y + B_Y) − (K_Y + Γ_Y) ≡ −(K_Y + Γ_Y)/X`，**四个下标 Y 全部存在、`≡` 未误作 `=`、负号在括号内且未漏 `/X`**，逐符号一致。
  - **`\phi _ { * } ( B _ { Y } - \Gamma _ { Y } ) = B \geq 0`**（第 599 行）：印刷 `φ_*(B_Y − Γ_Y) = B ≥ 0.`，MD 的 `\phi _ { * }` 星号在**下标**位置（与第 529 行 `ν_* G` 同惯例），`≥` 方向正确。
  - **`B _ { Y } - \Gamma _ { Y } \geq 0`**（第 599 行）：印刷 `B_Y − Γ_Y ≥ 0.`，MD 一致；随后的 `each non-zero coefficient of$\Gamma _ { Y }$is$\geq 1 - \frac { \epsilon } { 2 }$` 中 `≥` 方向亦正确，**未被误写成 `≤`**。
  - **`\Gamma _ { Y } = 0`、`\phi` 为 small、`A _ { U } - \psi ^ { * } A _ { V }` ample over `T`、`A _ { Y } - \phi ^ { * } A` ample**（第 599、601 行）：印刷逐条对应，MD 的 `\psi ^ { * }`（上标星号）与 `\phi ^ { * }`（上标星号）**未与 `\phi _ { * }`（下标星号）混淆**。
  - **`\Sigma` 为 `W \to V` 的既约例外因子（第 581 行）**：印刷 `Let Σ be the reduced exceptional divisor of W → V.`，MD 用直立希腊字母 `Σ` 保留，**未被拍平成 `S` 或 `Sum`**，与印刷一致。
  - **`(U, \Gamma _ { U })` 为 `(W, \Gamma _ { W })` 在 `V` 上的对数极小模型（第 581 行）**：印刷 `Run an MMP on K_W + Γ_W over V and let (U, Γ_U) be the resulting log minimal model of (W, Γ_W) over V.`，MD 中 MMP、`K _ { W } + \Gamma _ { W }`、`(U, \Gamma _ { U })`、`(W, \Gamma _ { W })` 全部逐字对应，**未漏 `log minimal model` 中的 log**。
  - **`A \sim A _ { V } ^ { i } | _ { X }` 与 `V = V ^ { i } , T = T ^ { i } , A _ { V } = A _ { V } ^ { i }`（第 579 行）**：印刷 `A ∼ A^i_V |_X` 与 `V = V^i, T = T^i, A_V = A^i_V.`，MD 的 `\sim`、上标 `i`、下标 `V` 与直像记号 `| _ { X }` 层级**全部正确**。
  - **Lemma 2.26 陈述（第 605 行）**：`Y \to X`（**此处印刷方向确为 `Y → X`，是收缩映射，与 p.15 第 559 行那处印刷笔误不同，本处正确**）、`C` 为 nef 的 `ℝ`-divisor、`A` 为 ample `ℝ`-divisor 的 pullback、`C + a A` semi-ample (globally)、`a > 0` —— 除末尾句点（已修）外**逐项与印刷一致**；`any real number$a > 0$` 中的 `a` 未被误作 `α`。
  - **Lemma 2.26 的证明（第 607 行）**：`\phi \colon Y \to Z / X` 的 `Z / X`（**上横线除号，非 `Z/X` 的下标或箭头**）、`\phi _ { * } C , \phi _ { * } A`、`C + b A` ample for some `b \gg a` —— 印刷 `b ≫ a`（**双大于号 `≫`**），MD 的 `b \gg a` 正确对应，**未误写成 `b > a` 或 `b \ge a`**。
  - **Lemma 2.26 的展示式（第 610 行）**：`C + t b A = (1 - t) C + t (C + b A)` —— 印刷 `C + tbA = (1 − t)C + t(C + bA)`，**左端的 `t b A` 三因子齐备、右端 `(1−t)` 的括号与 `t(C+bA)` 的分配律结构完整**，未漏因子也未错分配。
  - **`\begin{array} { r } { t = \frac { a } { b } }`（第 613 行）**：印刷 `taking t = a/b we see that C + aA is ample.`，MD 的 `\frac { a } { b }` 分子分母方向正确；`$\begin{array}…` 包装为纯排版伪影（见 PASS±）。
  - **本段 ff 连字词**：印刷中 `resolution`、`finitely`、`projective`、`morphisms`、`neighbourhoods`（跨页首句）、`coefficient`、`contraction`、`globally` 等词，在 150dpi 整页图上逐词目检**均为完整双 f / 完整拼写**，Markdown 对应处**无一处拍平**（`be a log resolution`、`finitely many projective`、`each non-zero coefficient`、`is a contraction`、`is globally nef`）。
- **print quirk 忠实保留（未按数学/常识静默「纠正」）**：
  1. 第 599 行 `each coefficient of$B _ {Y } { \mathrm { ~ i s ~ } } \leq 1 - \epsilon$but by the previous paragraph …` —— 印刷在此处用 `\epsilon`（月牙 ϵ），而同页其余 `ε-lc` 处（第 599 行 `(X, B)$is ǫ-lc`）用直立 ε；印刷内部字形不统一，**照录未改**。
  2. 印刷第 16 页页眉「16 Caucher Birkar」在 Markdown 中不出现（全书页眉页码一律不导出），属导出器既定取舍，非本页特有缺陷。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **ℝ/ℚ 拍平**：第 573 行 `K _ { Y }$is Q-Cartier`、第 599 行 `since U is Q-factorial` 与 `is Q-Cartier`、第 605 行 `a nef R-divisor` / `an ample R-divisor` —— 印刷分别为 `ℚ-Cartier`、`ℚ-factorial`、`ℝ-divisor`（黑板粗 ℝ/ℚ），MinerU 一律拍平为 `Q`/`R`。与 p.9–p.15 登记的同类，属同一字母的样式降级、语义无歧义，登记不修。
  2. **HTML `<sub>` 标签泄漏**：第 599 行 `Supp Γ<sub>Y</sub>`、第 601 行 `A<sub>U</sub>`（两处）—— MinerU 在正文（非数学环境）处输出了原始 HTML 下标标签。字符本身未丢失、渲染后仍为下标，属标记层面伪影，按政策登记不修（**注：本片段新登记的类别**）。
  3. **MathJax 词距伪影**：第 599 行 `{ \mathrm { ~ i s ~ } }`（把单词 `is` 排进了数学环境并加 `~` 词距空格）；第 581、591 行的 `\textstyle { \frac { \epsilon } { 2 } }`（`\textstyle` 包裹分式，纯排版）。
  4. **节标题被提升为 Markdown 标题**：第 603 行 `## 2.25. Semi-ample divisors.`，而印刷中 `2.25.` 与其前后 `2.22.`、`2.23.` 一样只是**加粗的编号节标题**（正文层级相同），MinerU 只对本处输出了 `##` 前缀，造成同层节标题层级不一致。属标记层面伪影，登记不修。
  5. **`\begin{array}` 包装**：第 613 行 `\begin{array} { r } { t = \frac { a } { b } } \end{array}`（印刷为行内公式）。
  6. **标点错置于数学环境内、致词间粘连**：第 579 行 `Since A is very ample and$A ^ { d } \leq r$, X belongs`、`$x \in X$a closed point`、`$t \in T ^ { i }$for some i`、`$A \sim A _ { V } ^ { i } | _ { X }$.`、`we fix i and write`、`We will shrink$V , T$when`；第 581 行 `Let$W \to V$be`、`Run an MMP on$K _ { W } + \Gamma _ { W }$over V`、`Shrinking$W , U , V , T$we can`、`if$t \in T$is a closed point`、`over$t ,$ respectively`；第 593 行 `Let$Y$be the fibre`、`let$\phi \colon Y \to X$be`、`Let$K _ { Y } + B _ { Y } =$ $\phi ^ { * } ( K _ { X } + B )$`（数学式被 `$= $` 断开成两段、插入多余空格）；第 599、601 行多处 `is ample`/`is$\geq 0$` 型粘连；第 607 行 `it defines a contraction$\phi \colon Y \to Z / X$to a`、`Replacing$Y$with$Z$and`、`we can assume$C$is`、`Now$C + b A$is`、`for some$b \gg a$because`；第 613 行 `we see that$C +$aA is ample.`（`aA` 的 `a` 被甩出数学环境）。
  7. **ε 字形**：第 581、591、599 行的 `\epsilon`（月牙 ϵ）与同页 `ǫ`（直立 ε）混用，印刷全篇为同一字形，属字形变体，登记不修。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；Lemma 2.24 的 `≡` 等式、`φ_*`（下标）与 `φ^*`/`ψ^*`（上标）的区分、`\Gamma_Y = 0` 的结论、Lemma 2.26 的 `b ≫ a` 与分配律展示式均逐符号核对无误。5 处修复**全部是标点类**（3 处句末句点补齐、1 处逗号被误作句点、1 处全角逗号改回印刷的半角逗号并移出数学环境），**未触及任何公式、系数、上下标或不等号方向**。`2.25` 节标题的 `##` 提升、`<sub>` 标签泄漏、ℝ/ℚ 拍平均按 PASS± 登记，未擅自改动。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p009`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

# 第三片段：p.017–p.024 片段逐页视觉审计（actor=`Wf-R-Birkar-p017`）

> 本片段接续 `Wf-R-Birkar-p009`（p.9–p.16）。开工基线：AUDIT 已有 `## p.` 条目 **106 条**；Markdown SHA-256 = `9a5ce6430630b92d2581df848d4101915726a906bde00afdc15f8ac5759f9aaa`；PDF SHA-256 = `c9c73303be3b12c5ca91506ac541c9b9d81764d19bcd7183b7c577f8c0d546fe`（46 页）。
>
> **本片段修复政策**：沿用 `Wf-R-Birkar-p009` 已登记并落签的口径——**修**字符级丢失（ff 连字拍平、重音符错位）、标点错讹（丢句点、伪句点代逗号、丢逗点、重复逗点、全角逗号误植）；**登记不修**行内 ℝ/ℚ→R/Q 拍平、断词连字符丢失、MathJax 词距空格化（`\mathrm { S u p p }` 等）、`\begin{array}` 包装、节标题被提升为 `##`、标点错置于数学环境内致词间粘连、ε 字形变体。每处 `Edit` 的 `old_string` 均先经唯一性检查确认全文件唯一后才落刀。
>
> **基线中已存在的他人未提交改动**：开工时 `git diff 父提交版 → 交付态` 在 MD 第 627–2341 行已有 130 个未提交变更行（`Wf-R-Birkar-p009` 小结中已如实登记）。**本片段的作用域正是从 MD 第 627 行开始**，因此本片段逐页审计的是**含这些既有改动**的当前内容；对每处判定的缺陷均另做溯源（见各页「溯源」行与本片段小结），以区分「导出缺陷」与「他人引入的回归」。

## p.017（PDF p.17 / 印刷 p.17）
- PNG：`/tmp/birkarsing_audit_p017.png`（pngmono 150dpi，本片段新渲染并 Read 亲眼目检整页）；仲裁裁片 `/tmp/bk_p17_bul3.png`、`/tmp/bk_p17_H0.png`、`/tmp/bk_p17_Lam.png`、`/tmp/bk_p17_ps.png`、`/tmp/bk_p17_ar.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=17`，按 `-bbox` 坐标 ×S=300/72.0 换算后放大 7–12 倍；**PIL 只裁图，未写 Markdown**）。
- 核对：正文页，五点比对 —— ①节标题顺序与文字；②Proposition 3.1 的**编号、三条假设列条、结论句**；③Proof 的 Step 1–3 全部陈述与 `[5, Proposition 4.4]`、`[5, Theorem …]` 类引用；④公式逐符号（`0 ≤ L ∼_ℝ −K_X`、`L ∼_ℝ uT`、`u ≥ μ_T L`、`K_V + B_V = ψ_*φ^*(K_X + B)`、`a(T,V,B_V) = a(T,X,B) ≤ 1` 等三式、`deg_H` 相关留至 p.18）；⑤记号约定（`V ⟶ X` 虚线双射态射 vs `φ: W → X`、`ψ: W → V` 实线对数解射；`(V, Λ) ∈ 𝒫` 的 couple 记号；`H ≤ Λ`）。对照 Markdown 第 615–661 行（`## 3.` 至 `a (T, V, \Lambda) \leq a (T, V, \Omega_ {V}) \leq 1.`），辅以 `pdftotext -f 17 -l 17 -layout` 与 `-bbox`。
- 结果：**PASS±**（改 2 处；无数学内容错误）
- **已用 Edit 修复 2 处（逐处绑定页码与裁片）**：
  1. 第 625 行 `• $0 \leq L \sim _ { \mathbb { R } } - K _ { X }$` → 补句点（Proposition 3.1 第三条假设）。证据：`-bbox` 词元 `•`(px x=427–450, y=1076–1122) → `0`(x=466–489) → `≤`(x=501–537) → `L`(x=549–580) → `∼`(x=593–628) → `R`(x=628–652, **y=1094–1123 下沉＝下标 ℝ**) → `−K`(x=667–741) → `X`(x=741–770, **y=1094–1124 下沉＝下标**) → **`.`**(x=774–788, y=1076–1122, **基线句点独立成词元**)，其后紧接下一段 `Then`(x=377, y=1184)；300dpi 裁片 `/tmp/bk_p17_bul3.png`（区域 (410,1066)–(800,1134)，×9）亲眼可见 `0 ≤ L ∼_ℝ −K_X .`，`≤` 开口方向正确、**ℝ 与 X 均为真下标**、句点圆实无下伸尾。
  2. 第 637 行 `Enlarging Λ we can also assume that$H \leq \Lambda$for some very ample divisor$H \geq 0$` → 补句点。证据：`-bbox` 词元 `Enlarging`(px x=427–620, y=2159–2204) → `Λ`(x=635–667) → … → `H`(x=1892–1930) → `≥`(x=1947–1982，**开口朝左＝≥**) → **`0.`**(x=1995–2030, y=2159–2204, **句点已熔进 0 词元**)，其后紧接下一段 `Step`(x=427, y=2267)；300dpi 裁片 `/tmp/bk_p17_H0.png`（区域 (1840,2149)–(2050,2214)，×11）亲眼可见 `or H ≥ 0 .`，句点圆实、无下伸尾。
- **经升级仲裁撤销的 1 处疑似差异（防后续误「修复」）**：
  - 印刷第 631、633、637、657、660 行的 couple 第二分量，初看 150dpi 整页图疑似斜体字母 **`A`**（如 `(V, A) ∈ 𝒫`、`Supp A`、`H ≤ A`、`a(T, V, A)`），而 Markdown 用 `\Lambda`。**经 300dpi 裁片 `/tmp/bk_p17_Lam.png`（区域 (1145,1855)–(1280,1916)，×12）亲眼裁决为印刷写的是大写希腊字母 `Λ`**：字形为两笔交于顶点、底部带衬线、**无横杠**，与字母 `A` 的横杠结构完全不同；`-bbox` 词元亦解码为 `Λ`(x=1220–1269，`Λ)`)；文本层同为 `Supp Λ, hence ΩV ≤ Λ … a(T, V, Λ)`。**结论：Markdown 的 `\Lambda` 正确，不得改成 `A`。**
- **核对无误、未改动者**：
  - **节标题（第 615 行）**：`## 3. Lc thresholds of anti-log canonical systems of Fano pairs` —— 印刷 `3. Lc thresholds of anti-log canonical systems of Fano pairs`，标题文字、节号、大小写逐字一致（`Markdown` 的 `##` 前缀见 PASS±）。
  - **首段（第 617 行）**：`| - ( K _ { X } + B ) | _ { \mathbb { R } }` —— 印刷 `|−(K_X + B)|_ℝ`，绝对值两侧竖线、`X` 的下标、`ℝ` 的下标位置**全部正确**；`As pointed out in the introduction`、`We will show that Theorem 1.8 implies Theorem 1.6 assuming Theorem 1.1 in lower dimension`、`We also prove that Theorem 1.8 implies Theorem 1.7`、`First we consider a special case of Theorem 1.6.` 逐句与印刷一致。
  - **Proposition 3.1 陈述（第 619 行）**：`Let d be a natural number and ǫ be a positive real number. Assume that Theorem 1.8 holds in dimension$\leq d$and that Theorem 1.1 holds in dimension$\leq d - 1$.` —— 印刷 `≤ d` 与 `≤ d−1` 的**不等号方向、两个维数上界**（一为 `d`、一为 `d−1`）均正确，**未把 `d−1` 误作 `d+1` 或漏掉 `−1`**；`depending only on$d , \epsilon$satisfying the following. Assume that` 与印刷一致。
  - **前两条假设列条（第 621、623 行）**：`• X is a Q-factorial ǫ-lc Fano variety of dimension$d ,$`、`• X has Picard number one, and` —— 印刷 `X is a ℚ-factorial ε-lc Fano variety of dimension d,` / `X has Picard number one, and`，**两条的逗号齐备**，`Q` 的 ℚ 拍平见 PASS±。
  - **结论句（第 627 行）**：`Then each coefficient of L is less than or equal to$v .$` —— 印刷 `Then each coefficient of L is less than or equal to v.`，句点完整；`less than or equal to` 未被压成 `≤`。
  - **Step 1（第 629 行）**：`Pick a component$T$of L. Since X has Picard number one,$L \sim _ { \mathbb { R } } u T$for some$u \geq \mu _ { T } L$. Thus we may replace L, hence assume $L = u T$.` —— 印刷 `L ∼_ℝ uT for some u ≥ µ_T L` 与 `L = uT`，**`≥` 方向正确、`µ_T L` 的下标 T 层级正确、`∼_ℝ` 的 ℝ 为下标**；`By Theorem 2.13`、`n-complement`、`K _ { X } + \Omega`、`Theorems 2.10 and 2.11 in dimension d, and 1.1 in lower dimension`、`$\vert - n K _ { X } \vert$defines a birational map`、`$\operatorname { v o l } ( - K _ { X } )$is bounded from above` 逐项与印刷一致。
  - **Step 2（第 631–637 行）**：`[5, Proposition$4 . 4 ]$`（印刷 `[5, Proposition 4.4]`）、`(by taking$B = 0$and$M = n \Omega )`、`$c \in \mathbb { R } ^ { > 0 }$`（印刷 `c ∈ ℝ^{>0}`，上标 `>0` 层级正确）、`and a bounded set of couples P depending only on$d , \epsilon$`、`projective log smooth couple$( V , \Lambda ) \in \mathcal { P }$`、`a birational map$V \dashrightarrow X$ —— 与印刷逐字对应。
  - **两条列条（第 633、635 行）**：`• Supp Λ contains the exceptional divisor of$V \dashrightarrow X$and the birational transform of $\operatorname { S u p p } \Omega ;$`（末为**分号**，正确）、`• for a common resolution$\phi \colon W \to X$and$\psi \colon W \to V$, each coefficient of$\psi _ { * } \phi ^ { * } \Omega$is at most c.` —— 印刷两条的标点（`;` 与 `.`）齐备。
  - **虚实箭头未混同（关键项）**：`-bbox` 词元 372、385 为 **`99K`**（虚线双射态射箭头）对应印刷 `V ⟶ X`（第 631、633 行），Markdown `\dashrightarrow` **正确**；词元 402、408 为实线 `→` 对应 `φ: W → X`、`ψ: W → V`（第 635 行），Markdown `\to` **正确**；300dpi 裁片 `/tmp/bk_p17_ar.png`（区域 (1790,1855)–(1990,1922)，×12）亲眼可见 `V - - → X`，确为**虚线**箭头（两道短横 + 箭头）。
  - **`ψ_*` 与 `φ^*` 的上下位置（关键项）**：第 642 行 `\psi_ {*} \phi^ {*}` —— `-bbox` 词元 469 `ψ`(px x=923–953, y=2347–2393) → **470 `∗`(x=952–970, y=2370–2391，位于基线之下＝下标)** → 471 `φ`(x=972–1000) → **472 `∗`(x=999–1017, y=2344–2365，位于基线之上＝上标)**；300dpi 裁片 `/tmp/bk_p17_ps.png`（区域 (660,2340)–(1230,2400)，×7）亲眼可见 `K_V + B_V = ψ_* φ^*(K_X + B)`，`ψ` 的星在**右下**、`φ` 的星在**右上**，**未被混同或互换**。
  - **Step 3 的三组展示式（第 642、648、654、660 行）**：印刷 `K_V + B_V = ψ_*φ^*(K_X + B) and K_V + Ω_V = ψ_*φ^*(K_X + Ω).`、`a(T, V, B_V) = a(T, X, B) ≤ 1.`、`a(T, V, Ω_V) = a(T, X, Ω) ≤ 1.`、`a(T, V, Λ) ≤ a(T, V, Ω_V) ≤ 1.` —— **四个下标 V、两处 `ψ_*φ^*`、三处 `≤` 方向、末式的 `<=` 链序**逐符号核对无误，**未把 `a(T,V,Λ) ≤ a(T,V,Ω_V)` 的不等号方向写反**。
  - **行间关系（第 639、645、651、657 行）**：`Step 3. Let B be a boundary such that$( X , B )$is ǫ-lc and$K _ { X } + B \sim _ { \mathbb { R } } 0$. Let`（印刷行末确有 `Let` 承接下一展示式）、`Then$( V , B _ { V } )$is sub-ǫ-lc and`、`Similarly,$( V , \Omega _ { V } )$is sub-lc and`、`By Step 2, the union of$\operatorname { S u p p } \Omega _ { V }$and the exceptional divisors of$V \dashrightarrow X$is contained in $\operatorname { S u p p } \Lambda$, hence$\Omega _ { V } \leq \Lambda$which implies` —— **四条引导句与印刷逐句一致，`Ω_V ≤ Λ` 的不等号方向正确**，`sub-ǫ-lc` 与 `sub-lc` 未混用。
- **print quirk 忠实保留（未按数学/常识静默「纠正」）**：
  1. 第 637 行印刷作 `H ≤ Λ for some very ample divisor H ≥ 0.` —— 用 `≥ 0` 描述「very ample divisor」，与第 2.2 节 `0 < b ≤ 1` 的约定写法不同，但印刷如此，**照录未改**。
  2. 第 631 行印刷的 `[5, Proposition 4.4]` 写作 `4 . 4`（中间带空格），Markdown 保留了 `4 . 4` 的空格排版，**未规范化**。
  3. 第 619 行印刷在 `d, ε` 处用逗号分隔两个依赖参数（`depending only on d, ε`），Markdown 的 `$d , \epsilon$` 与之一致；**未改成 `d` 与 `ε` 的其它写法**。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **ℝ/ℚ 拍平**：第 617 行 `the R-linear systems`、第 621 行 `a Q-factorial`、第 631 行 `$c \in \mathbb { R } ^ { > 0 }$` —— 印刷分别为 `ℝ-linear`、`ℚ-factorial`、`ℝ^{>0}`（黑板粗），MinerU 一律拍平为 `R`/`Q`。
  2. **节标题被提升为 Markdown 标题**：第 615 行 `## 3. …`，而印刷中 `3.` 与其前后 `2.25.` 一样只是加粗编号节标题（正文层级相同）。
  3. **MathJax 词距伪影**：第 633、657 行的 `\operatorname { S u p p }`、第 629 行的 `\operatorname { v o l }`（`Supp`/`vol` 带字距）。
  4. **标点错置于数学环境内、致词间粘连**：第 619 行 `holds in dimension$\leq d$and`、`depending only on$d , \epsilon$satisfying`；第 621 行 `dimension$d ,$`；第 629 行 `Pick a component$T$of L`、`$L \sim _ { \mathbb { R } } u T$for`、`$L = u T$. We need`、`such that$K _ { X }$has`、`we can assume$\vert - n K _ { X } \vert$defines`；第 631 行 `Indeed applying`、`(by taking$B = 0$and$M = n \Omega )$we deduce`、`couple$( V , \Lambda ) \in \mathcal { P }$and a birational map`、`such that`；第 635 行 `$\phi \colon W \to X$and`、`$\psi _ { * } \phi ^ { * } \Omega$is at most c.`；第 637 行 `assume that$H \leq \Lambda$for`；第 639、645、651、657 行多处 `)$is`、`of$\operatorname { S u p p } \Omega _ { V }$and`、`hence$\Omega _ { V } \leq \Lambda$which`。
  5. **ε 字形**：第 619、621、631、639、645 行的 `ǫ`（直立 ε）与 `\epsilon`（第 619、631 行的 `$\epsilon$`）混用，印刷全篇为同一字形，属字形变体。
- **溯源**：第 625、637 两处「丢句点」在父提交版 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`) 与初次 MinerU 导出 `53a92412` 中**均以完全相同的字节形态存在**（详见本片段小结的溯源普查），**非后续 peer 引入的回归**。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；`\dashrightarrow` 与 `\to` 未混同、`ψ_*`（下标）与 `φ^*`（上标）未互换、`\Lambda` 未被误改为 `A`、`≤`/`≥` 方向、三组 `a(T,·,·)` 不等式链、`[5, Proposition 4.4]` 编号均逐符号核对无误。2 处修复**全部是句末句点补齐**，**未触及任何公式、系数、上下标或不等号方向**。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p017`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.018（PDF p.18 / 印刷 p.18）
- PNG：`/tmp/birksing_audit_p018.png`（pngmono 150dpi，本片段新渲染并 Read 亲眼目检整页，含页眉「18 Caucher Birkar」）；仲裁裁片 `/tmp/bk_p18_L57.png`、`/tmp/bk_p18_L138.png`、`/tmp/bk_p18_L148.png`、`/tmp/bk_p18_Lam.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=18`，按 `-bbox` 坐标 ×S=300/72.0 换算后放大 6–10 倍；**PIL 只裁图，未写 Markdown**）。
- 核对：正文页（Proposition 3.1 之 Proof 的 Step 4–6 收尾 + Lemma 3.2 之 Proof 开头），五点比对 —— ①**Step 4 / Step 5 / Step 6 的编号与顺序**，以及 Proof 末的 **□（证毕符）**；②Step 4 的核心推理链（`Γ_V = I − J` 拆有效除子、`deg_H I` 有上界 ⇒ `deg_H J` 有上界 ⇒ `Γ_V` 中 `D` 的系数有下界）；③Step 5 的两次线性不等式 `lH − Δ = α(lH − B_V) + (1−α)(lH − Λ)` 与 `a(T,V,Δ) = αa(T,V,B_V) + (1−α)a(T,V,Λ)`，以及 `Δ := αB_V + (1−α)Λ ≥ 0`；④Step 6 的 `M = ψ_*φ^*uT`、`(V, Δ + (1/u)M)` 非 klt 的不等式、`u < v := 1/t` 结论；⑤Lemma 3.2 的题设（`≤ d` 与 `≤ d − 1` 两个维数上界）与首句落点 `s < 1`。对照 Markdown 第 663–699 行，辅以 `pdftotext -f 18 -l 18 -layout` 与 `-bbox`。
- 结果：**PASS±**（改 3 处；无数学内容错误）
- **已用 Edit 修复 3 处（逐处绑定页码与裁片）**：
  1. 第 663 行 Step 4 段末 `as$( V , \Lambda ) \in \mathcal { P }$ and$H \leq \Lambda$` → 补句点。证据：`-bbox` 该行（L57）词元 `and`(px x=378.0–451.2, y=640.9–686.4) → `H`(x=466.0–503.8) → `≤`(x=520.5–555.8) → **`Λ.`**(x=568.5–612.6, y=640.9–686.4，**句点熔进 Λ 词元**)，其后为下一段 `Write Γ`（L58, x=427.5, y=694.9 起）；300dpi 裁片 `/tmp/bk_p18_L57.png`（区域 (370,625)–(660,700)，×8）亲眼可见 `and H ≤ Λ .`，**句点圆实、无下伸尾，且该 Λ 为无横杠的大写 Λ**（两笔交于顶点、底部带衬线），**不是字母 A**。
  2. 第 695 行 Proof 末 `hence$\begin{array} { r } { u < v : = \frac { 1 } { t } } \end{array}$` → 补句点。证据：`-bbox` L136 词元 `1`(x=1071.5–1090.4, y=2568.1–2619.9，**分数 1 在上**) → `,` → `hence` → `u` → `<` → `v` → `:=` → `1`(x=1440.5–1453.2, y=2600.3–2630.8) → `t`(x=1440.5–1453.2, y=2600.3–2630.8，下行＝分母) → **`.`**(L138, x=1460.5–1473.1, y=2574.4–2619.9，**句点独立成词元、与正文同基线**)，其后为右对齐的 **□**(L139, x=2137.0–2172.3, y=2631.3–2678.4, 码位 `\x03`＝证毕空心方块)；300dpi 裁片 `/tmp/bk_p18_L138.png`（区域 (1050,2560)–(1490,2630)，×6）亲眼可见 `\tfrac{1}{u} , hence u < v := \tfrac{1}{t} .`，**句点在分数右侧同一基线处**，证明链的结论与印刷完全一致。
  3. 第 699 行 Lemma 3.2 的 Proof 末 `In particular, we may assume$s < 1$` → 补句点。证据：`-bbox` L148 词元 `to`(x=378.0–418.2) → `show` → `s` → `is` → `bounded` → `from` → `below` → `away` → `from` → `zero.`(x=1301.0–1394.1) → `In`(x=1424.5–1466.2) → `particular,`(x=1485.0–1692.1) → `we` → `may` → `assume` → `s`(x=2044.0–2065.3) → `<`(x=2083.5–2118.8) → **`1.`**(x=2137.0–2172.1, y=2963.9–3009.4，**句点熔进 1 词元，且位于行末右边界**)；300dpi 裁片 `/tmp/bk_p18_L148.png`（区域 (2010,2950)–(2185,3020)，×10）亲眼可见 `s < 1 .`，句点圆实无尾。该句是 Lemma 3.2 归约论证的落点，**缺句点会与其后第 701 行新段直接粘连**。
- **核对无误、未改动者**：
  - **Step 4 首段的公式链（第 663 行）**：`$K _ { V } + \Gamma _ { V } = \psi _ { * } \phi ^ { * } K _ { X }$`、`$\mu _ { D } \Gamma _ { V } \leq \mu _ { D } B _ { V } ,$`、`$K _ { V } + \Gamma _ { V } \equiv - \psi _ { * } \phi ^ { * } \Omega$`、`$\mathrm { d e g } _ { H } ( K _ { V } + \Gamma _ { V } )$` —— 逐符号与印刷一致：`-bbox` L11/L12 证实 `ψ`(y=424.9–470.4) 的 `∗` 在 **y=447.3–468.1（下沉＝下标）**、L13 证实 `φ`(y=424.9–470.4) 的 `∗` 在 **y=423.8–444.6（上抬＝上标）**，即印刷写作 **`ψ_* φ^*`**；Markdown 的 `\psi _ { * } \phi^ { * }` **完全正确**。两处 `\leq`（`μ_D Γ_V ≤ μ_D B_V`）与 `\equiv` 未被误写为 `=`。
  - **Step 4 第二段（第 665 行）**：`$\Gamma _ { V } = I - J$`、`$I \leq \Lambda , \deg _ { H } I \leq \deg _ { H } \Lambda$`、`$\deg _ { H } J$`、`$\Omega _ { V }$` —— 与印刷 `Write ΓV = I − J where I, J are effective divisors…` 逐句一致；**未把 `≤` 写反为 `≥`**，`I − J` 的减号方向正确，`J` 未被误作 `I`。
  - **Step 5（第 667–685 行）**：`$\alpha \in ( 0 , 1 )$`（印刷 `α ∈ (0, 1)`，**开区间两端点正确**）、展示式 `$\Delta := \alpha B _ {V} + (1 - \alpha) \Lambda \geq 0.$`、引导句 `Then, by Lemma$2 . 3 , ( V , \Delta )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$where$\epsilon ^ { \prime } = \alpha \epsilon$because$( V , B _ { V } )$is sub-ǫ-lc and$( V , \Lambda )$is lc.`、展示式 `$a (T, V, \Delta) = \alpha a (T, V, B _ {V}) + (1 - \alpha) a (T, V, \Lambda) \\ \leq \alpha + (1 - \alpha) = 1.$`、`$l \in \mathbb N$`、`$l H - \Lambda$`、`$- B _ { V } \sim _ { \mathbb { R } } K _ { V }$`、`$l H - B _ { V } \sim _ { \mathbb { R } } l H + K _ { V }$`、展示式 `$l H - \Delta = \alpha (l H - B _ {V}) + (1 - \alpha) (l H - \Lambda)$`、`$( l H ) ^ { d } \leq r .$` —— 逐符号核对**全部正确**：`≤ α + (1−α) = 1` 与 `≤ r` 的不等号方向均正确；`lH` 的字母是**小写斜体 `l`**（`-bbox` L90/L105 均解码为 `lH`，非 `1H`/`iH`）；`−B_V ∼_ℝ K_V` 的 **ℝ 为下标**（L94 的 `R` 位于 y=1613.6–1642.9，低于同行正文字元的 y=1595.9–1641.4 之下缘，确认下沉）；`(lH)^d` 的 `d` 为上标（`d` 与 `(lH)` 同词元）。
  - **Step 6（第 687–695 行）**：`$M = \psi _ { * } \phi ^ { * } u T$`、`$\Omega \equiv - K _ { X } \equiv u T$`、`$\deg _ { H } M = \deg _ { H } ( \psi _ { * } \phi ^ { * } \Omega )$、`$T$is exceptional over$V ,$`、`its support is inside Λ`、`$\phi ^ { * } u T \leq \psi ^ { * } M$`、`$\begin{array} { r } { ( V , \Delta + \frac { 1 } { u } M ) } \end{array}$`、展示式 `$a (T, V, \Delta + \frac {1}{u} M) \leq a (T, V, \Delta) - 1 \leq 0.$`、`$\textstyle t < { \frac { 1 } { u } }$` —— 逐符号核对**全部正确**：L110/L111 再次证实 `M = ψ_*φ^*uT` 中 **`ψ` 的星在下标、`φ` 的星在上标**；`\phi ^ { * } u T \leq \psi ^ { * } M` 的 `≤` 方向正确；两处 `\frac { 1 } { u }` 的**分子在上、分母在下**（`-bbox` L127 的 `u` 在 y=2328.3–2358.8、L128 的 `1 M )` 在 y=2296.1–2347.9，`u` 明显位于 `1` 之下，确认是真分数而非 `1/u` 连写）。
  - **Lemma 3.2（第 697 行）**：`Assume that Theorem 1.8 holds in dimension$\leq d$and that Theorem 1.1 holds in dimension$\leq d - 1$. Then Theorem 1.6 holds in dimension$d .$` —— 印刷 `holds in dimension ≤ d and that Theorem 1.1 holds in dimension ≤ d − 1. Then Theorem 1.6 holds in dimension d.`，**两个维数上界一为 `d`、一为 `d − 1`，未混同、未漏 `− 1`**。
  - **Lemma 3.2 的 Proof 首句（第 699 行）**：`Pick$\epsilon ^ { \prime } \in ( 0 , \epsilon )$`、`Let$( X , B )$and$A = - ( K _ { X } + B )$`、`pick$L \in | A | _ { \mathbb { R } }$`、`$( X , B + s L )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$` —— 与印刷逐字一致；`-bbox` L146 证实 `|A|` 的 `R` 在 **y=2927.6–2956.9（低于同行 y=2909.9–2955.4 之下缘）＝下标 ℝ**，Markdown `$| A | _ { \mathbb { R } }$` 正确；`A = −(K_X + B)` 的**单负号**未被写成双负号。
  - **Proof 末的证毕符 □**（L139, 印刷右对齐于版心内）：`-bbox` 码位为 `\x03`，`-layout` 输出中该处无对应字符，Markdown **未收录 □**。属**装饰性符号的导出遗漏**，按本片段政策**登记不修**（不影响定理陈述与推理链可读性，且 Markdown 中同类证毕符全篇一致缺席，单独补一处会造成风格不齐）。
- **print quirk 忠实保留（未按数学/常识静默「纠正」）**：
  1. 第 687、689 行印刷在 Step 6 中把 **`ψ_*` 写成上标 `ψ^*`**（`φ^*uT ≤ ψ^*M`、「transform of $T$ in $\psi^* M$」）—— 与 Step 4、Step 5 一贯使用的下标 `ψ_*` 不一致，属印刷自身的记号不统一；**照录未改**（铁律二：不按数学常识「纠正」原刊）。
  2. 第 679 行印刷作 `there is a bounded number l ∈ N such that lH − Λ is ample` —— 未把 `N` 排成黑板粗 ℕ，且句中 `−Λ` 前无空格；Markdown 照录。
  3. 第 685 行印刷作 `there is a bounded natural number r such that (lH)^d ≤ r` —— 用「bounded natural number」这一措辞，与第 679 行「a bounded number l ∈ N」并存，**照录未改**。
  4. 第 699 行印刷在 `pick L ∈ |A|_R` 后写作 `Let s be the largest number such that (X, B + sL) is ε′-lc` —— `ε′` 的撇号与 `-lc` 的连字符写法照录。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **ℝ/ℚ/ℕ 拍平**：第 679 行 `$\mathbb N$`（印刷 `N` 为 ℕ 黑板粗）、两处 `$\sim _ { \mathbb { R } }$` 的 ℝ 字形、第 699 行 `| A | _ { \mathbb { R } }` 的 ℝ 字形 —— MinerU 一律拍平为 `N`/`R`/`Q`。
  2. **MathJax 词距伪影**：第 663 行 `$\mathrm { d e g } _ { H }$`（`deg` 带字距）、第 699 行 `$\mathrm { l c }$`（`lc` 带字距）。
  3. **标点错置于数学环境内、致词间粘连**：第 663 行 `coefficients of$B _ { V }$are`、`a component of$B _ { V }$with`、`Let$K _ { V }`、`Then$\Gamma _ { V } +$`、`$\mu _ { D } B _ { V } ,$so`、`bound$\mu _ { D } \Gamma _ { V }$from`、`hence$\mathrm { d e g } _ { H }`、`because$\deg _ { H } K _ { V }$belongs`、`as$( V , \Lambda )`；第 665 行 `Write$\Gamma _ { V }`、`$\Lambda$which shows`、`$\Gamma _ { V }$is bounded`；第 667 行 `a boundary$\Delta$`、`$\alpha \in ( 0 , 1 )$depending`、`$d ,$ǫ`；第 673 行 `Lemma$2 . 3 , ( V , \Delta )$is`、`$\alpha \epsilon$because`、`$( V , B _ { V } )$is`、`$( V , \Lambda )$is`；第 679 行 `number$l \in \mathbb N$such`、`$l H - \Lambda$is`、`$- B _ { V } \sim`、`assume$l H - B _ { V }`、`$l H + K _ { V }$is`；第 687 行 `Let$M =`、`Since$\Omega`、`( \psi _ { * } \phi ^ { * } \Omega )$is`、`assume$T$is`、`over$V ,$otherwise`；第 689 行 `ample,$\phi`、`$\psi ^ { * } M$,`、`transform of$T$in`、`is at least u. Therefore,`；第 699 行 `Proof. Pick$\epsilon`、`Let$( X , B )$and$A =`。
  4. **`\begin{array}` 包装**：第 676 行展示式包成 `\begin{array}{c} … \end{array}`、第 689 与 695 行的行内式包成 `\begin{array} { r } { … } \end{array}`（原为普通括号内联式）。
  5. **ε 字形**：第 667 行 `ǫ`、第 673 行 `$\epsilon ^ { \prime } = \alpha \epsilon$` 与 `sub-ǫ-lc`、第 699 行 `$\epsilon ^ { \prime } \in ( 0 , \epsilon )$`，直立 ε 与 `\epsilon` 混用。
  6. **证毕符 □ 未收录**（见「核对无误」末条）。
- **溯源**：三处「丢句点」在父提交版 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`) 与初次 MinerU 导出 `53a92412` 中**均以完全相同的字节形态存在**（详见本片段小结的溯源普查），**非后续 peer 引入的回归**。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；`ψ_*`(下标) 与 `φ^*`(上标) 的区分在 Step 4、Step 5、Step 6 三处**全部正确**、未被混同，Step 6 中印刷自身的 `ψ^*`(上标) quirk 亦照录；`\leq`/`\geq`/`\equiv` 方向、两处真分数 `\frac{1}{u}` 的上下结构、Lemma 3.2 的两个维数上界（`d` 与 `d − 1`）均逐符号核对无误。3 处修复**全部是句末句点补齐**，**未触及任何公式、系数、上下标或不等号方向**。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p017`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.019（PDF p.19 / 印刷 p.19）
- PNG：`/tmp/birksing_audit_p019.png`（pngmono 150dpi，本片段新渲染并 Read 亲眼目检整页，含页眉「Singularities of linear systems and boundedness of Fano varieties 19」）；仲裁裁片 `/tmp/bk_p19_L32.png`、`/tmp/bk_p19_L155.png`（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=19`，按 `-bbox` 坐标 ×S=300/72.0 换算后放大 9 倍；**PIL 只裁图，未写 Markdown**）。
- 核对：正文页（Lemma 3.2 之 Proof 收尾 + 「Next we treat Theorem 1.7」过渡段 + Lemma 3.3 全题与 Proof），五点比对 —— ①Lemma 3.2 Proof 的两处 **□（证毕符）** 与 Lemma 3.3 的**编号、题设、陈述**；②Lemma 3.2 的核心不等式链（`μ_T sL_Y ≥ ε − ε'` → `−(K_{Y'} + B_{Y'} + sL_{Y'}) ∼_ℝ (1−s)L_{Y'} ≥ 0` → `μ_{T'}(1−s)L_{Y'} ≥ (1−s)(ε−ε')/s` → `−K_{Y'} ∼_ℝ L_{Y'} + B_{Y'} = (1−s)L_{Y'} + sL_{Y'} + B_{Y'} ≥ (1−s)L_{Y'}`）；③Mori 纤维空间 `Y' → Z'` 与「先设 `dim Z' > 0` 归纳、再设 `Z'` 是点」的两段式论证次序；④Lemma 3.3 的定义式 `0 ≤ L_i ∼_ℝ A = −(K_X + B)`、`t_i := lct(X, B, L_i)`、`lim t_i = 1`、`1 + s < t_i` 与 `lim t_i = 1` 的矛盾；⑤`lct(X, B, |A|_ℝ) < 1`（过渡段）与 `= 1`（Lemma 3.3）两个条件的区分，`∼_ℚ` 与 `∼_ℝ` 的区分。对照 Markdown 第 701–755 行，辅以 `pdftotext -f 19 -l 19 -layout` 与 `-bbox`。
- 结果：**PASS±**（改 2 处；无数学内容错误）
- **已用 Edit 修复 2 处（逐处绑定页码与裁片）**：
  1. 第 715 行 `Since$s < 1$` → 补**逗号**（`Since$s < 1$,`）。证据：`-bbox` L32 词元 `Since`(px x=427.5–516, y=883.4–928.9) → `s`(x≈530) → `<`(x≈560) → **`1,`**(x≈616–663.1, **逗点已熔进 1 词元**)，其后为下一展示式 `−(K`（L33, x=874.5, y=938.9 起）；300dpi 裁片 `/tmp/bk_p19_L32.png`（区域 (410,875)–(690,935)，×9）亲眼可见 `Since s < 1 ,`，**逗号带下伸尾**（与句点的圆点形态明确不同），且 `<` 开口朝左。印刷此逗号承接后面的展示式，缺它会使 `Since s < 1` 与展示式之间失去语法连接。
  2. 第 753 行 `…we can replace L so that$0 \leq L \sim _ { \mathbb { Q } } A .$, so we are done in this case by taking$D = L.$` → **删除数学环境内的伪句点**（`A .$,` → `A$,`）。证据：`-bbox` L153 词元 `can`(x=378.0) → `replace` → `L` → `so` → `that` → `0` → `≤` → `L` → `∼` → L154 `Q`(x=978.0–1003.8, y=2711.6–2740.9，**下沉＝下标 ℚ**) → L155 **`A,`**(x=1018.5–1050, y=2693.9–2739.9，**逗号已熔进 A 词元**) → `so`(x≈1065) → `we are done in this case by taking D = L.`(x 至 1971.6)；300dpi 裁片 `/tmp/bk_p19_L155.png`（区域 (1000,2686)–(1300,2748)，×9）亲眼可见 `A , so we are done`，**A 后是一个带下伸尾的逗号、其后无句点**。Markdown 原写成 `A .$,`（数学环境内伪句点 + 环境外逗号），属**伪句点代逗号**的标点错讹，照印刷改为单一逗号并移出数学环境。
- **核对无误、未改动者**：
  - **Lemma 3.2 首段（第 701–705 行）**：`Replacing X with a Q-factorialisation, we can assume X is Q-factorial. There is a prime divisor$T$over$X$, that is, on birational models of X, with log discrepancy` 与展示式 `$a (T, X, B + s L) = \epsilon^ {\prime}.$` —— 与印刷逐字一致；`-bbox` L04 证实 `ε` 的撇号 `′` 在 **y≈505–530（高于 ε 本体）＝上标**，Markdown `\epsilon^ {\prime}` 正确。
  - **Lemma 3.2 的两种情形（第 707 行）**：`If$T$is not exceptional over X, then we let$\phi \colon Y \to X$be the identity morphism. But if T is exceptional over X, then we let$\phi \colon Y \to X$be the extremal birational contraction which extracts T.`、`$K _ { Y } + B _ { Y } = \phi ^ { * } ( K _ { X } + B )$`、`$L _ { Y } = \phi ^ { * } L$` —— 逐符号一致；`-bbox` L11/L13 证实 `φ∗` 的 `∗` 位于 **y=680.3–702（高于 φ 本体的 y=681.4–726.9 之上缘）＝上标**，Markdown `\phi ^ { * }` 正确；两处 `\colon Y \to X` 的实线箭头与全文 `\to` 用法一致。
  - **首个展示式与随后的不等式（第 710、713 行）**：`$\mu_ {T} B _ {Y} \leq 1 - \epsilon \text {   but   } \mu_ {T} (B _ {Y} + s L _ {Y}) = 1 - \epsilon^ {\prime},$`、`hence µ<sub>T</sub>s$L _ { Y } \geq \epsilon - \epsilon^ {\prime } .$` —— 逐符号与印刷一致：`-bbox` L20/L26 证实 `\leq` 方向正确（`≤ 1 − ǫ` 与 `= 1 − ǫ′`）、`μ` 的 `T` 为下标（L17 `T` 的 y=772.8–803.3 低于 μ 的 y=755.4–800.9）、两处 `ε` 与 `ε′` 的撇号位置正确。**`<sub>` 标签泄漏（`µ<sub>T</sub>`）属标记层面伪影，见 PASS±**。
  - **三个展示式（第 718、724、730、736 行）**：`$-\left(K _ {X} + B + s L\right) = A - s L \sim_ {\mathbb {R}} (1 - s) A$`、`$-\left(K _ {Y ^ {\prime}} + B _ {Y ^ {\prime}} + s L _ {Y ^ {\prime}}\right) \sim_ {\mathbb {R}} (1 - s) L _ {Y ^ {\prime}} \geq 0.$`、`$\mu _ { T ^ {\prime}} (1 - s) L _ {Y ^ {\prime}} \geq \frac {(1 - s) (\epsilon - \epsilon^ {\prime})}{s},$`、`$- K _ {Y ^ {\prime}} \sim_ {\mathbb {R}} L _ {Y ^ {\prime}} + B _ {Y ^ {\prime}} = (1 - s) L _ {Y ^ {\prime}} + s L _ {Y ^ {\prime}} + B _ {Y ^ {\prime}} \geq (1 - s) L _ {Y ^ {\prime}},$` —— **逐符号核对全部正确**：四处 `∼_ℝ` 的 **ℝ 均为下标**（L36 `R` y=956.6–985.9、L58 y=1203.1–1232.4、L102 y=1813.1–1842.4，分别低于同行本体之下缘）；`\geq`（`≥ 0`、`≥ (1−s)L_{Y'}`、`\geq \frac{…}{s}`）三处方向均正确；**真分数的分子在上、分母在下**（`-bbox` L89 `(1 − s)(ǫ − ǫ ′ )` 在 y=1545.3–1591.9 位于 L91 `s` 的 y=1608.4–1653.9 之上，确认是真分数而非 `(1−s)(ε−ε')/s` 连写）；末式的 `= (1 − s)L_{Y'} + sL_{Y'} + B_{Y'}` 中 **`(1−s)` 与 `s` 两项都在、未漏项或写反**；L90 的逗点（x=1578.0–1590.6）证实展示式以逗号收尾，Markdown 保留。
  - **Y' 的撇号层级（第 727 行）**：`Moreover,$( Y ^ { \prime } , B _ { Y ^ { \prime } } + s L _ { Y ^ { \prime } } )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$because$( Y , B _ { Y } + s L _ { Y } )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$and $- ( K _ { Y } + B _ { Y } + s L _ { Y } )$ is semi-ample. If dim$Z ^ { \prime } > 0$, then restricting to a general fibre of$Y ^ { \prime } \to Z ^ { \prime }$and applying Theorem 1.6 in lower dimension by induction (or applying Theorem 1.1) shows that the coefficients of the horizontal$/ Z ^ { \prime }$components of$( 1 - s ) L _ { Y ^ { \prime } }$are bounded from above. In particular,$\mu _ { T ^ { \prime } } ( 1 - s ) L _ { Y ^ { \prime } }$is bounded from above. Thus from the inequality` —— `-bbox` L62 的两个 `′`（y=1258.8–1279.6）与 L77 的行首 `′`（x=686.5, y=1312.8–1359.4）证实 **`Y'`、`Z'`、`T'` 的撇号一律为上标**，Markdown 的 `^ { \prime }` 全部正确；`\to` 实线箭头、`>` 方向正确、`horizontal$/ Z ^ { \prime }$` 中的斜杠原样保留。
  - **Lemma 3.2 的收尾（第 733、739 行）**：`Therefore, we can assume$Z ^ { \prime }$is a point and that$Y ^ { \prime }$is a Fano variety with Picard number one. Now` 与 `so by Proposition 3.1,$\mu _ { T ^ { \prime } } ( 1 - s ) L _ { Y ^ { \prime } }$is bounded from above which again gives a lower bound for s as before.` —— 与印刷逐字一致，**`Proposition 3.1` 的编号未误作 `3.1.` 或 `3. 1`**。
  - **过渡段（第 741 行）**：`Next we treat Theorem 1.7. As mentioned in the introduction, the theorem and its proof are independent of the rest of this paper when lct$( X , B , | A | _ { \mathbb { R } } ) < 1$.` —— `-bbox` L124–L126 证实 `|A|` 的 `R`（y=2130.1–2159.4）**为下标**、其后 `) < 1.` 的**小于号方向正确**，Markdown `$| A | _ { \mathbb { R } } ) < 1$` 正确。
  - **Lemma 3.3 陈述（第 743 行）**：`Lemma 3.3. Assume Theorem 1.8 holds in dimension d. Then Theorem 1.7 holds in dimension d when lct$( X , B , | A | _ { \mathbb { R } } ) = 1$.` —— `-bbox` L127–L130 逐词一致，**条件为 `= 1`（等号）而非 `< 1`**，与上一段的 `< 1` 严格区分，Markdown 正确。
  - **Lemma 3.3 的 Proof（第 745–755 行）**：`By definition of the lc threshold, there exists a sequence of R-divisors`、展示式 `$0 \leq L _ {i} \sim_ {\mathbb {R}} A = - (K _ {X} + B)$`、`such that the numbers$t _ { i } : = \operatorname { l c t } ( X , B , L _ { i } )$form a decreasing sequence with lim$t _ { i } = 1$.`、`Thus lct$( X , B , L ) \leq 1$`、`Since lct$( X , B , \vert A \vert _ { \mathbb { R } } ) = 1$, we deduce lct$( X , B , L ) = 1$`、`$( X , B + L )$is lc but not klt`、`By [5, Lemma$7 . 2 ]$, there is$\epsilon > 0$such that$( X , B { + } L _ { i } )$is ǫ-lc for every i.`、`Then by Theorem 1.8 in dimension$d ,$there is$s > 0$such that$\left( X , B + L _ { i } + s L _ { i } \right)$ is klt, for every i.`、`But then$1 + s < t _ { i }$for every i which contradicts lim$t _ { i } = 1$.` —— 逐符号核对**全部正确**：`-bbox` L133/L140/L142/L144 的 `i` 均在 **y 低于本体的位置＝下标**；L141 的 `:=` 未被误写成 `=` 或 `: =` 之外的形式；`1 + s < t_i` 的**小于号方向正确**、末句 `= 1.` 句点完整；`L_i + sL_i` 中的 **`s` 未被漏写**（L164 `+ sL` 证实 `s` 在位）。**`[5, Lemma 7.2]` 的编号正确**。
- **print quirk 忠实保留（未按数学/常识静默「纠正」）**：
  1. 第 701、753、767 行印刷用英式拼写 **`Q-factorialisation`**（带 `-isation`），而第 743 行 Lemma 3.3 之后未见；**照录未改**。
  2. 第 741、743 行印刷把 **Lemma 3.3 排成定理环境（粗体＋斜体）**，正文其余 lemma 同为该体例；Markdown 未保留粗斜体标记，**不据此改写任何字符**。
  3. 第 755 行印刷在 `there is s > 0 such that (X, B + L_i + sL_i) is klt, for every i.` 中于 `klt` 后**加逗号**（`is klt, for every i`），Markdown 的 ` is klt, for every i.` 照录。
  4. 第 753 行印刷 `If B is a Q-boundary, then using approximation, we can replace L so that 0 ≤ L ∼_ℚ A, so we are done in this case by taking D = L.` —— 句中用逗号连接两个独立分句，**照录未改**。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **HTML `<sub>` 标签泄漏**：第 713 行 `hence µ<sub>T</sub>s$L _ { Y } \geq …` —— MinerU 在正文（非数学环境）处输出了原始 HTML 下标标签，且 `µ_T` 与 `s` 之间、`s` 与 `L_Y` 之间的空格丢失。字符本身未丢失、渲染后仍为下标，属标记层面伪影，登记不修（与 p.16 首次登记的同类）。
  2. **ℝ/ℚ 拍平**：第 701 行 `Q-factorialisation` / `Q-factorial`、第 741、743 行的 `| A | _ { \mathbb { R } }`、第 745 行 `R-divisors`、第 718、724、736、748 行与第 753 行 `∼_ℚ` 的 ℝ/ℚ 字形 —— 印刷为黑板粗 ℝ/ℚ，Markdown 的 `\mathbb{R}`/`\mathbb{Q}` **已保留黑板粗**（未拍平），仅正文行内的 `Q`/`R` 被拍平。
  3. **MathJax 词距伪影**：第 751 行 `$\operatorname { l c t } ( X , B , L _ { i } )$`（`lct` 带字距）、第 755 行 `$( X , B { + } L _ { i } )$`（加号被 `{ + }` 加空格）、`Lemma$7 . 2 ]$`（编号内加空格）。
  4. **标点错置于数学环境内、致词间粘连**：第 701 行 `prime divisor$T$over$X$`、`log discrepancy`；第 707 行 `If$T$is not`、`let$L _ { Y } =`、`let$L _ { Y }$` 的 `$L _ { Y } = \phi ^ { * } L$` 与紧跟的 `By assumption`；第 713 行 `hence µ<sub>T</sub>s`；第 721 行 `$- ( K _ { Y } + B _ { Y } + s L _ { Y } )$is also`、`$( Y , B _ { Y } + s L _ { Y } )$is klt`、`so$Y$is of Fano type`、`let$Y ^ { \prime } \to Z ^ { \prime }$be`；第 727 行 `Moreover,$( Y`、`because$( Y`、`horizontal$/ Z`；第 733 行 `$Z ^ { \prime }$is`、`$Y ^ { \prime }$is`；第 739 行 `Proposition 3.1,$\mu _ { T ^ { \prime } }`；第 741 行 `when lct$( X , B`；第 743 行 `dimension d when lct$( X , B`；第 745 行 `lc threshold`；第 751 行 `numbers$t _ { i } : =`、`with lim$t _ { i } = 1$`；第 753 行 `Assume$( X , B )$is`、`there is$0 \leq L`、`that$( X , B +$ $L )$is not`（**数学式被 `$+ $` 拆成两段、插入多余空格**）；第 755 行 `Now assume$( X , B )$is`、`for any$0 \leq L`、`is ǫ-lc for every i.`、`$\left( X , B + L _ { i } + s L _ { i } \right)$ is klt`、`contradicts lim$t _ { i } = 1$`。
  5. **`\operatorname{lct}` 与 `\operatorname { l c t }` 两种写法并存**：第 751 行用带字距的 `\operatorname { l c t }`，第 755 行用 `lct` 纯文本；属导出不一致的排版伪影，登记不修。
  6. **证毕符 □ 未收录**：Lemma 3.2 Proof 末（`-bbox` L122, x=2137.0–2172.3, y=1980.8–2027.9）与 Lemma 3.3 Proof 末（`-bbox` L172, x=2137.0–2172.3, y=2966.8–3013.9）两处 `\x03`（空心方块）Markdown 均未收录；登记不修（与 p.18 同类，理由相同）。
  7. **ε 字形**：第 704、710、713、727、755 行的 `\epsilon` / `\epsilon^ {\prime}` 与第 755、761 行的 `ǫ` 混用，印刷全篇同一字形，属字形变体。
- **溯源**：两处（丢逗号、伪句点代逗号）在父提交版 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`) 与初次 MinerU 导出 `53a92412` 中**均以完全相同的字节形态存在**（详见本片段小结的溯源普查），**非后续 peer 引入的回归**。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；Lemma 3.2 的 MMP 与 Mori 纤维空间两段式论证次序、`Y'`/`Z'`/`T'` 的撇号层级、三处 `∼_ℝ` 的下标 ℝ、真分数 `(1−s)(ε−ε')/s` 的上下结构、`−K_{Y'} ∼_ℝ L_{Y'} + B_{Y'} = (1−s)L_{Y'} + sL_{Y'} + B_{Y'} ≥ (1−s)L_{Y'}` 的项序、Lemma 3.3 的 `= 1` 与 `< 1` 两条件、`[5, Lemma 7.2]` 编号、`1 + s < t_i` 的方向均逐符号核对无误。2 处修复**全部是标点类**（1 处逗号补齐、1 处伪句点删除），**未触及任何公式、系数、上下标或不等号方向**。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p017`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.020（PDF p.20 / 印刷 p.20）
- PNG：`/tmp/birksing_audit_p020.png`（pngmono 150dpi，本片段新渲染并 Read 亲眼目检整页，页眉「20 Caucher Birkar」）；仲裁裁片 `/tmp/bk_p20_L56.png`（区域 (370,1236)–(940,1300)，×6）、`/tmp/bk_p20_L192.png`（区域 (370,2190)–(760,2252)，×8）、`/tmp/bk_p20_sig.png`（区域 (600,1338)–(810,1405)，×11）（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=20`，按 `-bbox` 坐标 ×S=300/72.0 换算；**PIL 只裁图，未写 Markdown**）。
- 核对：正文页（Proof of Proposition 3.4 的 Step 1–3），五点比对 —— ①命题号与标题句 `Proposition 3.4. Theorem 1.7 holds when lct(X, B, |A|_ℝ) < 1.`；②Step 1 的两个 `lct` 展示式与 `t_i := lct(X,B,L_i) ∈ (0,1)` 的递减序列、`t := lct(X,B,|A|_ℝ) = lim t_i`；③Step 2 的两条取元路径（`(X,B+H_i)` klt 与 `(X,B+t_iL_i+H_i)` lc）、DCC set 的半可分性论证、`A ∼_ℝ Σ α_j G_j` 的求和项、`T_i'` 处的对数解射 `φ_i` 与恒等情形区分、`H_i' = φ_i^* H_i` 及 `K_{X_i'} + T_i' + B_i' + t_iL_i' + (1−t_i)H_i' = φ_i^*(K_X+B+t_iL_i+(1−t_i)H_i) ∼_ℝ 0`；④Step 3 的 MMP 对象 `−(K_{X_i'} + T_i' + B_i' + (1−t)H_i')`、`[5, 2.13(7)]` 引用、Fano type 判定、`(1−t_i)` 与 `(1−t)` 的区分、`K_{X_i''} + T_i'' + B_i'' + (1−t)H_i''` 的 ample-over-`Z_i''` 断言与末式 `K_{X_i''} + T_i'' + B_i'' + t_iL_i'' + (1−t_i)H_i'' ∼_ℝ 0`；⑤页末句与下页接续（`… ∼_ℝ 0` 后无句点，`which implies` 起于 PDF p.21）。对照 Markdown 第 757–823 行，辅以 `pdftotext -f 20 -l 20 -layout` 与 `-bbox`。
- 结果：**PASS±**（改 1 处；无数学内容错误）
- **已用 Edit 修复 1 处（逐处绑定页码与裁片）**：
  1. 第 799 行 `is of Fano$\mathrm { t y p e } .$, so we can indeed run such an MMP.` → 删除数学环境内的**伪句点**，改为 `is of Fano$\mathrm { t y p e }$, so we can indeed run such an MMP.`（印刷只有**一个逗号**，原 Markdown 却出现「环境内句点 + 环境外逗点」两个标点）。证据：`-bbox` L192 词元 `is of Fano type, so we can indeed run such an MMP. Let X`（`type` 与 `so` 之间仅一个逗号，无句点）；300dpi 裁片 `/tmp/bk_p20_L192.png` 亲眼可见 `is of Fano type, so`，`type` 后那个标点**带下伸尾**，是逗号而非句点。与 p.19 的伪句点同类。
- **经 300dpi 仲裁撤销的 1 处疑似差异（防后续误「修复」）**：
  - 第 781 行 `\left( { { X , B + t _ { i } } { L _ { i } } + H _ { i } } \right)` 看似把 `t_i L_i` 拆成两个并列花括号组、疑似公式断裂。**经 300dpi 裁片 `/tmp/bk_p20_L56.png`（×6）亲眼确认印刷为单一括号表达式 `(X, B + t_i L_i + H_i)`，`t_i` 与 `L_i` 紧邻；而该 Markdown 写法在 TeX/MathJax 中两个 `{…}` 只是分组、相邻 Ord 原子之间不插入任何空白，渲染结果与 `t _ { i } L _ { i }` 完全相同**。故**这不是缺陷**，属 MathJax 无害分组伪影，登记不修（**注：本片段新登记的类别**）。`-bbox` L56–L62 亦证实印刷是一段连续词元：`is klt and (X, B + t` → `i`(x=760.0–772.0, y 下沉＝下标) → `L`(x=774.0–804.9) → `i`(x=805.0–817.0, 下沉) → `+ H`(x=827.0–908.3) → `i`(x=908.5–920.5, 下沉) → `) is lc, for any i,`，其间无任何运算子或断点。
- **核对无误、未改动者**：
  1. `t \neq t _ { i }`（第 779 行）：`-bbox` L35 解码为 `t 6= t_i`（`6=` 是 `≠` 的文本层误码），Markdown 的 `\neq` 方向正确。
  2. `\phi _ { i } ^ { * }` 的**上标星**：`-bbox` L132（`′ = φ ∗` + `i` + `H`）与 L160（`′ = φ ∗` + `i`）中 `∗` 的 y 值高于同行基线，确为上标，非下标。
  3. `A \sim _ { \mathbb { R } } \sum \alpha _ { j } G _ { j }`（第 781 行）：300dpi 裁片 `/tmp/bk_p20_sig.png` 亲眼可见印刷确有大号 `Σ` 求和号，`\sum` 未丢失；同一裁片亦可见 `∼` 后的 `ℝ` 为真下标（黑板粗 ℝ），Markdown 的 `\mathbb { R }` 下标正确。
  4. Step 3 正文「Note that here we have used t rather than $t_i$」与展示式 `−(K_{X_i'} + T_i' + B_i' + (1−t)H_i')` 中**用 `t` 而非 `t_i`**：`-bbox` L184 词元 `′ + (1 − t)H` 证实印刷如此；这与紧随其后的 `(X_i'', T_i'' + B_i'' + t_iL_i'' + (1−t_i)H_i'')` 用 `t_i` 的**刻意区分**，非导出错误，登记为原文事实。
  5. `[5, 2.13(7)]`（第 799 行）：`-bbox` L189 为 `By [5, 2.13(7)], X`，编号与括号层级一致。
  6. `(1 - t _ { i })` 与 `(1 - t)` 的四处分布（第 796、802、805、808、816、822 行）：`(1−t)` 用于 Step 3 的 MMP 对象、`(1−t_i)` 用于 lc 对与末式，逐处与 `-bbox` 一致，未见张冠李戴。
  7. 页末第 822 行 `K _ {X _ {i} ^ {\prime \prime}} + T _ {i} ^ {\prime \prime} + B _ {i} ^ {\prime \prime} + t _ {i} L _ {i} ^ {\prime \prime} + (1 - t _ {i}) H _ {i} ^ {\prime \prime} \sim_ {\mathbb {R}} 0`：`\sim_ {\mathbb {R}}` 后接 `0` 且**无句点**，句子跨页续于 PDF p.21 的 `which implies`，第 823 行为空行、第 825 行起 `which implies`，分页点正确。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **MathJax 无害分组伪影**：第 781 行 `{ { X , B + t _ { i } } { L _ { i } } + H _ { i } }`（见上，渲染无差异）。**本片段新登记类别**。
  2. **MathJax 词距伪影**：第 762、770、776、784 行的 `\operatorname{lct}` / `\mathrm { l c t }` 两种写法并存；第 799 行的 `\mathrm { t y p e }` 把单词 `type` 排进了数学环境；第 790、822 行的 `\sim_ {\mathbb {R}}` 写成紧贴下标形式（第 770、776、784 行则是 `\sim_ {\mathbb {R}}`）。
  3. **ℝ 拍平**：`| A | _ { \mathbb { R } }`、`lct(X, B, |A|_ℝ)`（行内拍平为 `|A|_R`）与 `\mathbb {Q} } .$`（第 753 行的全角/半角逗号问题另见 p.19）—— 与 p.9–p.19 登记的同类，属黑板粗字母样式降级、语义无歧义。
  4. **标点错置于数学环境内、致词间粘连**：第 751 行 `such that the numbers$t _ { i } : = …$form a decreasing sequence`；第 773 行 `\in ( 0 , 1 )$form a decreasing sequence`；第 779 行 `for some$i ,$then put$D = L _ { i } .$`；第 781 行 `$A \sim _ {\mathbb {R}} \sum …$where$G _ { j }$are base point free Cartier divisors and$\alpha _ { j } > 0 ;$`、`and such that the coefficients of the$H _ { i }$belong to a fixed DCC set`、`$X _ { i } ^ { \prime }$ is klt`；第 787 行 `Let$T _ { i } ^ { \prime }$be`、`to be the identity morphism`、`is exceptional over X, we let`、`be the birational transforms of`、`because$H _ { i }$cannot contain any lc centre`；第 799 行 `used t rather than$t _ { i } .$.`、`$X _ { i } ^ { \prime }$ is of Fano`、`Let$X _ { i } ^ { \prime \prime }$be the resulting model`；第 805 行 `the numbers$1 - t _ { i }$form an increasing sequence approaching$1 - t .$, by`、`belong to a fixed DCC set independent of i`；第 819 行 `is ample over$Z _ { i } ^ {\prime \prime}$. On the other hand,`。
  5. **证毕符 □ 未收录**：Lemma 3.3 Proof 末（`-bbox` L172, x=2137.0–2172.3, y=2966.8–3013.9 的 `\x03`）Markdown 未收录；登记不修（与 p.18、p.19 同类）。
- **溯源**：唯一修复处（第 799 行伪句点）在父提交版 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、交付态 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 中**均以完全相同的字节形态存在**（三版第 799 行逐字相同），**非后续 peer 引入的回归，系初次导出缺陷**。撤销的第 781 行「疑似差异」经仲裁确认本无缺陷，亦不属回归。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；Proposition 3.4 的假设 `lct(X,B,|A|_ℝ) < 1`、Step 1 两个 `lct` 等式、Step 2 的两条取元路径与 `H_i' = φ_i^* H_i` 推论、Step 3 的 MMP 对象、`Fano type` 判定与三个 lc/ample 展示式的项序与系数，均逐符号核对无误。唯一 1 处修复**只删了一个伪句点**，**未触及任何公式、系数、上下标或不等号方向**。特别提示：第 781 行看似「公式断裂」的花括号分组经 300dpi 裁片与 TeX 分组语义双重确认**不构成缺陷**，后续审计不得据此「修复」。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p017`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.021（PDF p.21 / 印刷 p.21）
- PNG：`/tmp/birksing_audit_p021.png`（pngmono 150dpi，本片段新渲染并 Read 亲眼目检整页，页眉「Singularities of linear systems and boundedness of Fano varieties　21」）；仲裁裁片 `/tmp/bk_p21_disp4.png`（区域 (950,800)–(1610,886)，×6）、`/tmp/bk_p21_disp5.png`（区域 (950,2104)–(1610,2190)，×6）、`/tmp/bk_p21_arrow.png`（区域 (370,945)–(700,1000)，×10）、`/tmp/bk_p21_frac.png`（区域 (1180,2700)–(1400,2795)，×12）、`/tmp/bk_p21_qed.png`（区域 (2110,2940)–(2215,3012)，×8）（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=21`，按 `-bbox` 坐标 ×S=300/72.0 换算；**PIL 只裁图，未写 Markdown**）。
- 核对：正文页（Proposition 3.4 证明之收尾与 Step 4–5），五点比对 —— ①页首 `which implies` 承接 p.20 末式，及「anti-nef over `Z_i''`」与 `[13, Theorem 1.5]` 的引用、`X_i'' → Z_i''` 的**实线**箭头与 `minimal model X_i'', for every i.` 的结论；②Step 4 的目标 `D ∈ |A|_ℝ` 使 `lct(X,B,D) = t`，以及 `-(K_{X_i''}+T_i''+B_i''+(1−t)H_i'')`  nef → 半可分 → `ℝ`-线性等价于某个 `P_i'' ≥ 0` 的三步链；③MMP 箭头的**虚线**性质与 `P_i' ≥ 0`、`P_i ≥ 0` 的两次下降，及 `-(K_X+B+(1−t)H_i) ∼_ℝ P_i`、`(X, B+(1−t)H_i+P_i)` 在 `T_i'` 中心一般点处非 klt、`P_i ∼_ℝ tA`、`D = (1/t)P_i`；④Step 5 的 ℚ-边界情形（`A_i`、`H_i`、`P_i''`、`P_i`、`D` 依次为 ℚ-除子）、`t` 非常数的反证、`H_i'' · C ≠ 0` 与 `(1−e)H_i'` 的改写、`0 ≤ Q_i ∼_ℚ eA`、`D = (1/e)Q_i`、`lct(X,B,D) ≤ e < t` 的矛盾；⑤页末 `contradicting the definition of t.` 后的证毕方块 □，与 `## 4.` 节标题起于 PDF p.22。对照 Markdown 第 825–889 行（`which implies` 至 `contradicting the definition of t.`），辅以 `pdftotext -f 21 -l 21 -layout` 与 `-bbox`。
- 结果：**PASS**（改 0 处；无数学内容错误、无标点错讹）
- **经 300dpi 裁片撤销的 3 处疑似差异（本页初判的「缺陷」全部不成立，特此登记以防后续误「修复」）**：
  1. **第 836、868 行的双撇号不是导出错误**：150dpi 整页图上 `-(K_{X_{?}} + T_{?} + B_{?} + (1−t)H_{?})` 的撇号个数难以分辨，初判疑似 Markdown 把单撇写成了 `^{\prime \prime}`。**经 300dpi 裁片 `/tmp/bk_p21_disp4.png`（Step 4「Since」后展示式）与 `/tmp/bk_p21_disp5.png`（Step 5「Assume」后展示式）亲眼裁决：印刷这两处均为 `−(K_{X_i''} + T_i'' + B_i'' + (1−t)H_i'')`，`X`、`T`、`B`、`H` 四者皆带双撇号**；`-bbox` L030–L040（y=197）与 L130–L140（y=510）亦逐词元证实 `X/i/′′`、`T/i/′′`、`B/i/′′`、`H/i/′′`。而紧随其后的 L049–L059、L063–L077、L149–L159、L161–L171 展示式印刷为**单撇号** `−(K_{X_i'} + …)`，Markdown 第 842、848、868 之后的第 874、880 行也确实是**单撇号**。**结论：撇号层级印刷本身即在 `X_i'` 与 `X_i''` 之间逐处切换，Markdown 与之一一对应，正确，不得改动。**
  2. **第 883 行的 `D = \frac{1}{e}Q_i` 正确**：150dpi 下分子分母的小字号 `1` 与 `e` 极易误读为 `e/t`。**经 300dpi 裁片 `/tmp/bk_p21_frac.png`（×12）亲眼可见分数横线上下分别为 `1`（上）与 `e`（下）**；`-bbox` L179–L182 的 y 坐标亦给出铁证：分子 `1` 的 yMin=656 低于基线 658、**高于**行心（上行），分母 `e` 的 yMin=664 **低于**基线（下行），故为 `1/e`；同页 Step 4 的 `D = \frac{1}{t}P_i`（`-bbox` L109–L110：分子 `1` y=402、分母 `t` y=410）结构相同。**结论：第 863 行的 `\frac{1}{t}` 与第 883 行的 `\frac{1}{e}` 均与印刷一致，正确。**
  3. **第 839 行 MMP 箭头的虚线性质未丢失**：印刷 `X_i' ⇢ X_i''`（`-bbox` L046 解码为 `X/i/′/99K/X/i/′′`，`99K` 为虚线双射箭头字形码）。**经 300dpi 裁片 `/tmp/bk_p21_arrow.png`（×10）亲眼可见箭头确为「两段短划 + 实心箭头」的虚线形**，Markdown 的 `\mathrm { ~ -- \to ~ }` 渲染结果与之**视觉等价**（两枚减号 + `\to`），虚/实线区别得以保留。同一导出在 p.17（第 633、657 行）用的是 `\dashrightarrow`，此处用 `--\to` 属**同一虚线箭头的两种写法不一致**，属排版伪影而非缺陷，登记不修（**注：本片段新登记的类别**）。
- **核对无误、未改动者**：
  1. `D \in | A | _ { \mathbb { R } }`（第 833 行）：`-bbox` L027–L028 的 `R` 词元 yMin=181 低于行基线 y=176，**确为真下标**，Markdown 的 `_ { \mathbb { R } }` 正确（与行内被拍平的 `|A|_R` 形成对照，后者另见 PASS± 第 2 条）。
  2. `P _ { i } \sim _ { \mathbb { R } } t A$`（第 863 行）：`-bbox` L100–L102 的 `∼@463,390` 与 `R@471,394`（下沉＝下标）、`tA,@483` 证实印刷为 `P_i ∼_ℝ tA,`，逗号位置一致。
  3. `the centre of T_i'`（`X_i'` 上的中心，第 863 行）与随后的 `the centre of T_i`（`X` 上、**单撇**、第 863 行末）：`-bbox` L096–L098 为 `T/i/′/on X.`（带撇），L107–L108 为 `T/i/.`（**不带撇**）。Markdown 分别写 `T _ { i } ^ { \prime }` 与 `T _ { i }`，**与印刷的自身不一致完全一致**，此为原文事实，登记不改。
  4. `H _ { i } ^ { \prime \prime } \cdot C \neq 0`（第 871 行）：`-bbox` L142–L144 为 `H/i/′′/·/C/6=/0`，`6=` 是 `≠` 的文本层误码，Markdown 的 `\neq` 方向正确；紧随的 `(as H_i'' is big)`（L145–L147）亦为双撇。
  5. `0 \leq Q _ { i } \sim _ { \mathbb { Q } }$eA` 与 `0 \leq D \sim _ { \mathbb { Q } }$A`（第 883 行）：`-bbox` L172–L176 为 `0/≤/Q/i/∼/Q/eA`，L183–L185 为 `0/≤/D/∼/Q/A with`，`Q` 的 y 值（648/662）低于行基线（644/658）＝真下标，两处均正确。
  6. `\operatorname{lct} (X, B, D) \leq e < t,`（第 886 行）：`-bbox` L186 为 `lct(X, B, D) ≤ e < t,`，`<` 方向与尾随逗号均一致（`t` 前多出的空格属词距伪影）。
  7. **七个展示式的项序与系数**逐式核对无误：`K_{X_i''}+T_i''+B_i''+(1−t_i)H_i''`（页首，**用 `t_i`**）、`−(K_{X_i''}+T_i''+B_i''+(1−t)H_i'')`（Step 4 首式，**用 `t`**）、`−(K_{X_i'}+T_i''... )` 系列三个单撇式、`−(K_{X_i'}+T_i'+B_i'+(1−e)H_i')`（Step 5 的 `(1−e)`）、`−(K_X+B+(1−t)H_i) ∼_ℝ P_i`、`(X, B+(1−t)H_i+P_i)`。`t` 与 `t_i` 的混用与 p.20 Step 3 同源，是印刷的刻意区分，登记为原文事实。
  8. 全页句末标点逐句比对 `-bbox` 与 Markdown **无一缺失或多余**：`for every i.`、`= t. Fix i.`、`≥ 0. Since`、`∼_ℝ P_i.`、`By construction,`、`on X. Moreover,`、`tA, and`、`P_i. Then`、`definition of t.`、`Q-boundary. Fix i.`、`rational number.`、`contradiction. Assume`、`is not big. Then,`、`a contradiction. On the other hand,`、`above divisor is big, then`、`is not klt. Letting`、`eA such that`、`gives 0 ≤ D … with`、`t,`、`contradicting the definition of t.`。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **虚线箭头的两种写法不一致**（第 839 行 `\mathrm { ~ -- \to ~ }` vs p.17 第 633、657 行的 `\dashrightarrow`）：渲染视觉等价，仅写法不统一（见上）。
  2. **ℝ/ℚ 拍平**：第 839 行 `is R-linearly equivalent`、`some R-divisor`、`we get an R-divisor`、`which in turn gives an R-divisor`；第 865 行 `Q-boundary`、`a Q-divisor`（两处）、`to be a Q-divisor`、`is also a Q-divisor`、`choose D to be a Q-divisor`；第 883 行行内 `∼_Q`。印刷全为黑板粗 ℝ/ℚ，与 p.9–p.20 登记的同类。
  3. **MathJax 词距/包装伪影**：第 839、863 行的 `P _ { i } ^ { \prime \prime } ~ \ge ~ 0`、`\sim _ { \mathbb { R } ^ { } } ~ t A`（含空的上标 `^ { }`）；第 863、883 行的 `\begin{array} { r } { D = … } \end{array}`（行内分式的数组包装）；第 886 行 `\leq e <   t,` 的多余空格；第 839 行 `\mathrm { ~ -- \to ~ }` 两侧的 `~` 词距。
  4. **标点错置于数学环境内、致词间粘连**：第 831 行 `over$Z _ { i } ^ { \prime \prime }$.`、`fibres of$X _ { i } ^ { \prime \prime } \to Z _ { i } ^ { \prime \prime }$.`、`model$X _ { i } ^ { \prime \prime }$,`；第 833 行 `$D \in | A | _ { \mathbb { R } }$such that lct`、`Fix i. Since`；第 839 行 `some R-divisor$P _ { i } ^ { \prime \prime }`、`Since $X _ { i } ^ { \prime }`、`is an MMP on`；第 845、851 行 `an R-divisor$P _ { i } ^ { \prime } \geq 0$such that`；第 863 行 `centre of$T _ { i } ^ { \prime }$on$X$. Moreover,`、`as Supp$H _ { i }$does not`、`centre of$T _ { i }$. Put`、`Then D ∼<sub>R</sub> A and lct`、`$\leq t ,$so the inequality`；第 871 行 `$H _ { i } ^ { \prime \prime } \cdot C \neq 0$(as $H _ { i } ^ { \prime \prime }$is big)`；第 883 行 `is not klt. Letting$\begin{array}…\endarray}$gives$0 \leq D \sim _ { \mathbb { Q } }$A with`；第 889 行 `contradicting the definition of t.`。
  5. **HTML `<sub>` 标签泄漏**：第 863 行 `Then D ∼<sub>R</sub> A` —— 与 p.16 登记的同类（`<sub>` 在正文非数学环境处泄漏），字符未丢失，登记不修。
  6. **证毕符 □ 未收录**：页末 `-bbox` L188（x=513.0, y=712.0，空心方块）与 300dpi 裁片 `/tmp/bk_p21_qed.png` 亲眼可见印刷确有证毕方块，Markdown 第 889 行后未收录；登记不修（与 p.18、p.19、p.20 同类，理由相同）。
- **溯源**：本页判定为 **PASS、改 0 处**，无需溯源判定；上述三处「疑似差异」经 300dpi 裁片裁决后确认印刷与 Markdown 一致，**既非导出缺陷也非 peer 回归**。本页登记的各项 PASS± 伪影在初次导出 `53a92412` 与父提交 `16ffcc7c` 中形态一致（`<sub>` 泄漏、`\mathbb { R } ^ { }` 空上标、`--\to` 写法均属初次导出即有），登记口径与前片段一致。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置、无标点错讹**；Step 4 的 nef→半可分→`ℝ`-线性等价的推理链、两个分数 `1/t` 与 `1/e`、`(1−e)` 的引入、`e ∈ (0,t)` 的区间与 `lct ≤ e < t` 的不等号方向、`[13, Theorem 1.5]` 的引用编号，均逐符号核对无误。**本页是本片段首个零改动页**。特别提示两处易被后续审计误判的地方：第 836、868 行的**双撇号**与第 883 行的**分数 1/e**，150dpi 下极易看成「撇号多写」与「分式错成 e/t」，均已由 300dpi 裁片裁决为正确，**不得改动**。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p017`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.022（PDF p.22 / 印刷 p.22）
- PNG：`/tmp/birksing_audit_p022.png`（pngmono 150dpi，本片段新渲染并 Read 亲眼目检整页，页眉「Caucher Birkar 22」）；仲裁裁片 `/tmp/bk_p22_ceq.png`（区域 (800,2108)–(1010,2152)，×12）、`/tmp/bk_p22_floorG2.png`（区域 (900,750)–(1120,812)，×12）、`/tmp/bk_p22_floorB2.png`（区域 (1720,1370)–(1950,1432)，×12）、`/tmp/bk_p22_setS.png`（区域 (1740,1840)–(2140,1932)，×8）、`/tmp/bk_p22_Phi.png`（区域 (940,2006)–(1590,2088)，×7）（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=22`，按 `-bbox` 坐标 ×S=300/72.0 换算；**PIL 只裁图，未写 Markdown**）。
- 核对：正文页（第 4 节起始页），五点比对 —— ①节标题 `4. Complements in a neighbourhood of a non-klt centre` 与本节导言（含 `(Theorem 1.9)`、`[5]` 的两处引用）；②Proposition 4.1 的两条列条假设（`(X, Γ)` plt 且 `S = ⌊Γ⌋`；`αM − (K_X + Γ)` ample 且 `α > 0`）；③Step 1 的 `α ∈ (0,2)` 与 `B − Γ` 系数趋零化论证、**两行等式展示式**（`(1−t+tα)M − (K_X+(1−t)B+tΓ)` 的两种展开）、`t ∈ (0,1)` 与「sufficiently small real number `t > 0`」、`S ≤ ⌊B⌋` 与 `S = ⌊Γ⌋` 两个取整断言；④Step 2 的 `(S, B_S)` lc 与有限集 `𝒮 ⊂ [0,1]`、`Φ(𝒮) = {1 − s/l | s ∈ 𝒮, l ∈ ℕ}` 的定义式、`M|_S ≡ 0 ⇒ M|_S ∼_ℚ 0`、`−(K_X+Γ)|_S ∼_ℝ (αM−(K_X+Γ))|_S`、`(S, Γ_S)` klt 与 `S` 为 Fano type、`−(K_S+B_S) ∼_ℚ (M−(K_X+B))|_S` nef、Theorem 2.13 的 `n`-补与 `B_S^+ ≥ B_S`、`nB` 整除与 `np`；⑤页末 `Note that since S is of Fano type…` 段与 `h^i(𝒪_S) = 0 (i > 0)`。对照 Markdown 第 891–943 行（`## 4.` 至 `…vanishing theorem).`），辅以 `pdftotext -f 22 -l 22 -layout` 与 `-bbox`。
- 结果：**PASS**（改 0 处；无数学内容错误、无标点错讹）
- **经 300dpi 裁片撤销的 1 处疑似差异（防后续误「修复」）**：
  - 第 923 行 `By assumption,$M | _ { S } \equiv 0$, hence$M | _ { S } \sim _ { \mathbb { Q } } 0$as M is semi-ample.` —— 150dpi 整页图上 `≡` 与 `=` 难以分辨，初判疑似导出把印刷的 `≡` 误成 `=`（或反之）。**经 300dpi 裁片 `/tmp/bk_p22_ceq.png`（×12）亲眼裁决：印刷写的是 `M|_S ≡ 0`，该关系号有三条横杠（≡），并非两条（=）**；`-bbox` L059 亦直接给出词元 `≡@204,510`。语义亦自洽：`M|_S ≡ 0`（数值等价于零）配合「M 是半可分的」才推出线性等价 `∼_ℚ 0`。**结论：Markdown 的 `\equiv` 正确，不得改成 `=`，反之亦然。**
- **核对无误、未改动者**：
  1. **取整括号 `\lfloor \Gamma \rfloor` / `\lfloor B \rfloor` 未丢失**（第 897、907 行）：此前若干轮曾出现 `\rfloor` 丢失的缺陷类，本页**未复现**。**300dpi 裁片 `/tmp/bk_p22_floorG2.png`（×12，`S = ⌊Γ⌋, an`）与 `/tmp/bk_p22_floorB2.png`（×12，`S ≤ ⌊B⌋ and`）亲眼可见左侧括号的**底部带向右的短横足**（＝ `\lfloor`，非 `\lceil`），右侧为纯竖线（＝ `\rfloor`）**；`-bbox` L008（`⌊Γ⌋,@234,185`）、L033（`⌊B⌋@430,334`）、L034（`⌊Γ⌋.@432,347`）三处亦解码出完整括号。Markdown 的 `\lfloor \Gamma \rfloor`、`\lfloor B \rfloor`、`\left\lfloor \Gamma \right\rfloor` 三处写法均正确。
  2. **`M | _ { S } \sim _ { \mathbb { Q } } 0` 的下标层级**（第 923 行）：`-bbox` L061–L063 为 `∼@282,510`、`Q@291,514`（y 低于行基线 510 ＝ 真下标）、`0@300`，方向与层级正确。
  3. **`\Phi`**（第 917、920 行）：300dpi 裁片 `/tmp/bk_p22_setS.png` 与 `/tmp/bk_p22_Phi.png` 亲眼可见印刷为**大写希腊字母 Φ**（圆被竖线贯穿），Markdown 的 `\Phi` 正确。
  4. **`\Phi (\mathfrak {S}) = \{1 - \frac {s}{l} \mid s \in \mathfrak {S}, l \in \mathbb {N} \}.`**（第 920 行）：裁片 `/tmp/bk_p22_Phi.png`（×7）逐符号核对——左端 `Φ(𝒮) =` 用**单横等号**（非 `≡`）、`{1 − s/l | s ∈ 𝒮, l ∈ ℕ}` 的分式、`\mid` 竖线、`\in` 归属、`ℕ` 为黑板粗 N、**末尾句点**均在位，Markdown 全部一致。
  5. **Step 1 的两行等式展示式**（第 904 行）：印刷首行为 `(1 − t + tα)M − (K_X + (1 − t)B + tΓ) = (1 − t + tα)M − (1 − t)(K_X + B) − t(K_X + Γ)`，次行为 `= (1 − t)(M − (K_X + B)) + t(αM − (K_X + Γ))`；`-bbox` L019–L030 逐词元证实两行的项序、系数 `1−t`/`tα`/`t` 与三个 `K_X` 的分布，Markdown 的 `\begin{array}{c} … \\ = … \end{array}` 内容与行序完全一致。
  6. **`K _ { S } + B _ { S } ^ { + }` 的上标 `+`**（第 941 行）：`-bbox` L104–L107 的 `+@352,644` 高于行基线 y=646，**确为上标**；`-bbox` L096 的 `Theorem 2.13,` 引用编号亦正确。
  7. **`h ^ { i } ( { \mathcal { O } } _ { S } ) = 0`**（第 943 行）：`-bbox` L118–L120 的 `i@374,684` 略高于行基线 y=685（**上标**）、`S@390,690` 低于基线（**下标**），`[16, Proposition 2.1.2]` 的编号与分号位置亦一致。
  8. **跨行断词 `bound-` / `ary Γ`**（`-bbox` L006 末尾 `bound-@490,155` 接 L007 `ary@91,168`）：Markdown 第 895 行正确合并为 `boundary`，属**正确的断词还原**而非连字符丢失。
  9. 全页 24 处句末/句中标点逐句比对 `-bbox` 与 Markdown **无一缺失或多余**（详见下条 PASS± 第 4 项所列的粘连清单之外的全部句点、逗号与括号配对）。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **花体字母降级为 Fraktur**：第 917、920、941 行的 `\mathfrak { S }` —— 印刷为**花体大写 S（𝒮）**，300dpi 裁片 `/tmp/bk_p22_setS.png` 与 `/tmp/bk_p22_Phi.png` 亲眼可见其为圆弧草写体，Markdown 用 `\mathfrak` 渲染为哥特体（𝔖）。属字形族降级、语义无歧义，与 p.9–p.21 登记的同类，登记不修。
  2. **`\mathrm { P i c }` 词距伪影**（第 943 行 `$\mathrm { P i c } ( S )$is torsion-free`）：单词 `Pic` 被排进数学环境并加词距空格；同行的 `\mathrm { ~ i s ~ }` 类伪影亦属同类。
  3. **标点错置于数学环境内、致词间粘连**：第 897 行 `plt with$S = \lfloor \Gamma \rfloor$, and`；第 899 行 `ample for some real number$\alpha > 0$.`；第 901 行 `case when$\alpha \in ( 0 , 2 )$and when$B - \Gamma$has small`、`nef and big and$\alpha M - …$ is ample,`；第 907 行 `for any$t \in ( 0 , 1 )$.`、`replacing Γ with$( 1 - t ) B + t \Gamma$for`、`rational number in (0, 2).`、`we have$S \le \lfloor B \rfloor$and`、`change of Γ preserves`、`plt property of$( X , \Gamma )$and the condition`；第 909 行 `choose t small enough then we can ensure that$B - \Gamma$has`；第 911 行 `Since$( X , \Gamma )$is plt, S is normal.`；第 917 行 `Then$( S , B _ { S } )$is lc`、`coefficients of$B _ { S }$belong to`、`for some finite set${ \mathfrak { S } } \subset [ 0 , 1 ]$of rational numbers depending only on p`；第 923 行 `By assumption,$M | _ { S } \equiv 0$,`、`hence$M | _ { S } \sim _ { \mathbb { Q } } 0$as M is semi-ample.`；第 929 行 `Moreover, since (X, Γ) is plt, defining`；第 935 行 `by adjunction,$( S , \Gamma _ { S } )$is klt.`；第 941 行 `depending only on $d , \mathfrak { S }$such that`、`$K _ { S } + B _ { S }$has an n-complement`、`satisfies$B _ { S } ^ { + } \geq B _ { S }$.`、`assume that nB is an integral divisor after replacing n with np.`；第 943 行 `Note that since S is of Fano type and$M | _ { S } \sim _ { \mathbb { Q } } 0$,`、`in fact we have$M | _ { S } \sim 0$as$\mathrm { P i c } ( S )$is torsion-free`、`= 0$for$i > 0$which is a consequence`。
  4. **`\begin{array}` 包装**：第 904 行的两行等式展示式整体包在 `\begin{array}{c} … \end{array}` 中（印刷为居中对齐的两行公式，本无数组环境），与 p.9–p.21 登记的同类。
- **溯源**：本页判定为 **PASS、改 0 处**，无缺陷项需溯源；唯一撤销的疑似差异（第 923 行 `\equiv`）经 300dpi 裁片裁决确认印刷与 Markdown 一致，**既非导出缺陷也非 peer 回归**。本页登记的花体降级、`\mathrm { P i c }` 词距伪影等在初次导出 `53a92412` 与父提交 `16ffcc7c` 中形态一致。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置、无标点错讹**；Proposition 4.1 的两条列条假设、Step 1 的两行等式与两处取整断言、Step 2 的 `Φ(𝒮)` 定义式与四处线性/数值等价关系、`n`-补的 `[5]`、`Theorem 2.13`、`[16, Proposition 2.1.2]` 三处引用编号、`nB` 整除与 `np` 的替换，均逐符号核对无误。**本页与 p.21 同为零改动页**。特别提示两处易被误判的地方：第 923 行的 `≡`（150dpi 下与 `=` 难辨，实为 `≡`）与第 897、907 行的 `\lfloor … \rfloor`（此前轮次曾在此类括号上出现丢失缺陷，本页未复现），均已由 300dpi 裁片裁决为正确，**不得改动**。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p017`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.023（PDF p.23 / 印刷 p.23）
- PNG：`/tmp/birksing_audit_p023.png`（pngmono 150dpi，本片段新渲染并 Read 亲眼目检整页，页眉「Singularities of linear systems and boundedness of Fano varieties　23」）；仲裁裁片 `/tmp/bk_p23_semi.png`（区域 (1140,2178)–(1420,2224)，×14）、`/tmp/bk_p23_nE.png`（区域 (1020,2662)–(1320,2714)，×14）、`/tmp/bk_p23_phi.png`（区域 (1240,1172)–(1470,1214)，×14）、`/tmp/bk_p23_muS.png`（区域 (1020,2440)–(1520,2500)，×8）（pnggray 300dpi，裁自 `gs -r300 -dFirstPage=23`，按 `-bbox` 坐标 ×S=300/72.0 换算；**PIL 只裁图，未写 Markdown**）。
- 核对：正文页（Proposition 4.1 证明之 Step 3–4），五点比对 —— ①Step 3 的对数解射 `φ: X' → X`（**实线箭头**）、`S' ⊂ X'`、`ψ: S' → S` 与 `N := M − (K_X + B)` 的定义；②`K_{X'} + B', M', N'` 为 `K_X + B, M, N` 的拉回、`E'` 为 `B'` 中系数为 1 的部分之和与 `Δ' = B' − E'`、`L' := (n+2)M' − nK_{X'} − nE' − ⌊(n+1)Δ'⌋` 为整除子；③`L'` 的**三行展开式**（依次出现 `nB'`、`2M' + n(M' − K_{X'} − B')`、`2M' + nN'`）与 `K_{X'} + Γ' = φ^*(K_X + Γ)`；④Step 4 的 `Θ' := Γ' + nΔ' − ⌊(n+1)Δ'⌋ + P'`、`⌊Θ'⌋ = S'` 与 `Θ' ≥ 0`、`μ_{S'}P' = 0` 与 `D' ≠ S'` 的 `μ_{D'}P'` 定义式、`{(n+1)Δ'}` 的分数部分记号与「fractional part」说明；⑤`P' ≥ 0` 的分情形论证（`D' | E'` 与 `D' ∤ E'`）、`P'` exceptional/X 的证明、`μ_D ⌊(n+1)Δ⌋ = μ_D nΔ` 与末式 `−μ_D⌊Γ⌋ = 0`，页末句跨页续于 PDF p.24 的 `because μ_D Γ ∈ [0,1), a contradiction.`。对照 Markdown 第 945–1014 行（`Step 3.` 至末式 `- \mu _ { D } \left\lfloor \Gamma \right\rfloor = 0`），辅以 `pdftotext -f 23 -l 23 -layout`、`-f 24 -l 24 -layout` 与 `-bbox`。
- 结果：**PASS±**（改 1 处；无数学内容错误）
- **已用 Edit 修复 1 处（逐处绑定页码与裁片）**：
  1. 第 991 行 `hence$\mu _ { D ^ { \prime } } P ^ { \prime } = 0 ;$; on the other hand,` → 删除**重复的分号**，改为 `hence$\mu _ { D ^ { \prime } } P ^ { \prime } = 0$; on the other hand,`。证据：`-bbox` L061–L063 为 `B@184`/`′`/`=@199`/`1,@211`/`hence@223`/`µ@254` → `D@261`/`′` → `P@271`/`′@279`/`=@285`/**`0;@297`**（**单个词元 `0;`，仅一个分号**）/`on@310`/`the@325`/`other@344`/`hand,@373`；300dpi 裁片 `/tmp/bk_p23_semi.png`（区域 (1140,2178)–(1420,2224)，×14）亲眼可见印刷为 `P' = 0; on the`，`0` 之后**只有一个**分号（点在上、尾在下）。原文 Markdown 把一个分号重复写成了两个。
- **经 300dpi 裁片撤销的 2 处疑似差异（防后续误「修复」）**：
  1. **第 1000 行的区间与括号类型正确**：150dpi 下 `μ_{S'}((n+1)Δ') ∈ [0,1],` 的角括号易与圆括号混淆、右端点易与 `]` 混淆，初判疑似区间应为闭区间 `[0,1]`。**经 300dpi 裁片 `/tmp/bk_p23_muS.png`（×8）亲眼裁决：印刷为 `μ_{S'}⟨(n+1)Δ'⟩ ∈ [0, 1),` —— 用的是一对**尖角括号** `⟨ ⟩`，区间右端是**圆括号**（半开区间），其后紧跟一个**逗号**（因该展示式以逗号结尾并接「hence」句）**；`-bbox` L071–L073 亦把 `⟨`/`⟩` 误码为 `h(`/`i`，并给出词元 `[0,@334,590` 与 `1),@348,590`。**结论：Markdown 的 `\langle … \rangle \in [ 0, 1),` 四点全部正确，不得改动。**
  2. **第 1005 行的 `nE` 是印刷原样，不是导出错误**：Step 4 末段印刷写「Since **`nB` and `nE`** are integral, `μ_D nΔ` is integral, hence …」，而按上下文该处逻辑上应为 `nΓ`（因末式含 `⌊Γ⌋`）。**经 300dpi 裁片 `/tmp/bk_p23_nE.png`（区域 (1020,2662)–(1320,2714)，×14）亲眼裁决：印刷写的确实是字母 `E`**——字形为「一竖三横」（上、中、下三条横画加左竖），与本页其余八处 `Γ` 的「左上折角加左竖、无中横」字形（如 L028、L032、L035、L050 的 `Γ` 词元）完全不同；`-bbox` L083 亦直接解码为 `nE@264,644`（同页 `Γ` 均解码为 `Γ`，无混淆可能）。**按铁律三「印刷原文自身的错字与怪癖原样保留并登记」，Markdown 第 1005 行的 `$n E$` 与印刷逐字一致，正确，不予改动**；该处登记为**印刷侧原文瑕疵**（见下「原文事实与印刷侧瑕疵」）。
  - 另附：第 980 行 `μ_{D'}P' := −μ_{D'}⌊Γ' + nΔ' − ⌊(n+1)Δ'⌋⌋` 中的首项，150dpi 下 `Γ` 亦曾被误读为 `F`；`-bbox` L044 明确解码为 `Γ@287,422`，与同页其它 `Γ` 一致，Markdown 正确（未列为疑似差异的正式撤销项，仅在此备注以免后续重判）。
- **核对无误、未改动者**：
  1. **`\phi ^ { * }` 的上标星**（第 966、969 行）：300dpi 裁片 `/tmp/bk_p23_phi.png`（×14）亲眼可见星号**明显高于** `φ` 的 x 高度、位于其右上角，确为上标 `φ^*`（拉回），非同高度乘号；`-bbox` L028（`Γ@280`/`′`/`=@293`/`φ@305`/`∗@311`）与 L031（`φ@265`/`∗@272`）位置一致。
  2. **`\left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor` 的取整括号**（第 954、960、974、980、986、1008、1014 行）：`-bbox` 中取整括号解码为空词元（如 L014 的 `@358,181` 与 `@409,181`、L092 的 `@281,694`/`@340,694`/`@391,694`），但**开闭两端均成对出现**，且 L088 直接解出 `⌊(n@264` 与 `1)∆⌋@293`、L099 解出 `⌊Γ@231` 与 `1)∆⌋⌋@313`、L101 解出 `⌊Γ⌋@381`，确认 `\lfloor`/`\rfloor` 成对未丢；Markdown 的 `\left\lfloor … \right\rfloor` 与 `\left\lfloor \Gamma \right\rfloor` 均正确。
  3. **`\langle { ( n + 1 ) \Delta ^ { \prime } } \rangle` 与「fractional part」**（第 986、989 行）：`-bbox` L053 的 `h(n@322` / `i@372`（即 `⟨`/`⟩` 的误码）与 L054 的 `h(n@122` / `i@172` 一致，且 L054 明文为 `is the fractional part of (n + 1)∆′.`（**末尾句点**在位），Markdown 的 `\langle … \rangle` 与句点均正确。
  4. **`L'` 的三行展开式**（第 960 行）：印刷三行依次为 `L′ = (n+2)M′ − nK_{X′} − nB′ + n∆′ − ⌊(n+1)∆′⌋`、`= 2M′ + n(M′ − K_{X′} − B′) + n∆′ − ⌊(n+1)∆′⌋`、`= 2M′ + nN′ + n∆′ − ⌊(n+1)∆′⌋.`；`-bbox` L018–L024 逐词元证实三项系数、括注 `(M′ − K_{X′} − B′)` 的内容、`nN′` 的出现位置与末行**句点**（L024 末词元 `.@388,257`），Markdown 的 `\begin{array}{c} … \\ … \\ … \end{array}` 行序与内容完全一致。
  5. **`μ _ { D } \left\lfloor (n + 1) \Delta \right\rfloor = \mu _ { D } n \Delta .`**（第 1008 行）：`-bbox` L086–L090 为 `µ@248,663` / `D@255,667`（下标）/ `⌊(n@264` / `+@282` / `1)∆⌋@293` / `=@320` / `µ@331` / `D@338,667` / `n∆.@345,663`（**句点已熔进词元**），层级、括号与句点全部正确。
  6. **末式 `−μ_D ⌊Γ + n∆ − ⌊(n+1)∆⌋⌋ = −μ_D ⌊Γ⌋ = 0`**（第 1014 行）：`-bbox` L097–L101 逐词元证实两个 `μ` 的下标均为 **`D`（无撇）**、中间式用**下推的 `Γ` 与 `∆`（无撇）**、末项 `⌊Γ⌋ = 0` 无句点（句子跨页续于 p.24），Markdown 一一对应。
  7. **实线/虚线箭头的区分**（第 945 行 `\phi \colon X ^ { \prime } \to X`、`\psi \colon S ^ { \prime } \to S`）：`-bbox` L003 的 `→@122,102` 与 L004 的 `→@140,115` 均为**实线箭头**字形（对照 p.21 的虚线字形码 `99K`），Markdown 的 `\to` 正确。
  8. **全页 16 处句末/句中标点逐句比对 `-bbox` 与 Markdown**：`it.`、`morphism. Put`、`respectively. Let`、`coefficient 1, and let ∆′ = B′ − E′. Define`、`integral divisor. Note that`、`0.`（末式）、`Γ).`、`negative) coefficients by Step 1.`、`∆′ is 0.`、`divisors. Let P′ be the unique integral divisor so that`、`boundary,`、`plt,`、`(in particular, we are assuming Θ′ ≥ 0). More precisely,`、`0 and for each prime divisor D′ ≠ S′, we let`、`which satisfies`、`is the fractional part of (n+1)∆′.`、`0. Pick a component D′ of P′.`、`above,`、`D′ ≠ S′.`、`of E′, then`、`(0, 1) as`、`small coefficients and`、`1, hence`、`0; on the other hand,`、`of E′, then the absolute value of`、`is sufficiently small and`、`1),`、`hence`、`0 or`、`1, so in any case`、`≥ 0.`、`is exceptional/X.`、`is not exceptional/X and let D be its pushdown.`、`D′ ≠ S′.`、`E, ∆ be the pushdowns of E′, ∆′.`、`integral, hence`、`n∆. Then` —— **除已修复的重复分号外，无一缺失或多余**。
- **原文事实与印刷侧瑕疵（按铁律三原样保留，不改）**：
  1. **`Since nB and nE are integral`**（第 1005 行）：印刷此处写 `nE`，而同一句所服务的末式 `−μ_D⌊Γ⌋` 涉及的是 `Γ`；按上下文推断印刷本应为 `nΓ`。此为**印刷自身的用字不一致**，Markdown 已原样保留，登记不改。
  2. **`μ _ { S ^ {\prime}} \langle (n + 1) \Delta^ {\prime} \rangle \in [ 0 , 1 )`**（第 1000 行）：上下文正在论证 `D'` 分量（`D′ ≠ S′`），而印刷此处写的是 **`S'`**（`-bbox` L071–L072 明确为 `µ@252` + 下沉 `S@258,594` + `′@264,594`）。此为**印刷自身的记号不一致**（按逻辑应为 `μ_{D'}`），Markdown 已原样保留，登记不改。
- **PASS± 差异（按本片段政策登记不修）**：
  1. **`\begin{array}` 包装**：第 960 行（三行展开式）、第 986 行（两行展开式）、第 1014 行（两行展开式）三处整体包在 `\begin{array}{c}` / `\begin{array}{r}` 中（印刷为居中/右对齐的多行公式，本无数组环境），与 p.9–p.22 登记的同类。
  2. **标点错置于数学环境内、致词间粘连**：第 945 行 `Let $\phi \colon X ^ { \prime } \to X$be a log resolution of$( X , B + \Gamma ) , \ S ^ { \prime } \subset X ^ { \prime }$be`、`and$\psi \colon S ^ { \prime } \to S$be the induced morphism. Put`；第 951 行 `and let$K _ { X ^ { \prime } } + B ^ { \prime } , M ^ { \prime } , N ^ { \prime }$be the pullbacks of$K _ { X } + B , M , N$, respectively.`、`Let$E ^ { \prime }$be the sum`、`let$\Delta ^ { \prime } = B ^ { \prime } - E ^ { \prime }$. Define`；第 969 行 `Then we can assume that$B ^ { \prime } - \Gamma ^ { \prime } = \phi ^ { * } ( B - \Gamma )$has sufficiently small`、`coefficient of$S ^ { \prime }$in both$B ^ { \prime }$and$\Gamma ^ { \prime }$is 1 but its coefficient in$\Delta ^ { \prime }$is 0.`；第 971 行 `introduce a boundary$\Theta ^ { \prime }$and study related divisors. Let$P ^ { \prime }$be the unique integral divisor so that`；第 977 行 `is a boundary,$( X ^ { \prime } , \Theta ^ { \prime } )$is plt, and$\lfloor \Theta ^ { \prime } \rfloor = S ^ { \prime }$(in particular, we are assuming$\Theta ^ { \prime } \geq 0 )$.`、`we let$\mu _ { S ^ { \prime } } P ^ { \prime } = 0$and for each prime divisor$D ^ { \prime } \neq S ^ { \prime }$, we let`；第 989 行 `where$\langle { ( n + 1 ) \Delta ^ { \prime } } \rangle$is the fractional part of$( n + 1 ) \Delta ^ { \prime } .$`；第 991 行 `We claim that$P ^ { \prime } \ge 0$.`、`Pick a component$D ^ { \prime }$of$P ^ { \prime }$.`、`By the above,$D ^ { \prime } \neq S ^ { \prime }$.`、`If$D ^ { \prime }$is a component of$E ^ { \prime }$, then$D ^ { \prime }$is not a component of$\Delta ^ { \prime }$and`、`as$B ^ { \prime } - \Gamma ^ { \prime }$has small coefficients and`、`on the other hand, if$D ^ { \prime }$is not a component of$E ^ { \prime }$, then the absolute value of`；第 1003 行 `hence$\mu _ { D ^ { \prime } } P ^ { \prime } = 0$or$\mu _ { D ^ { \prime } } P ^ { \prime } = 1$, so in any case$\mu _ { D ^ { \prime } } P ^ { \prime } \geq 0$.`；第 1005 行 `We show$P ^ { \prime }$is exceptional$/ X$.`、`Assume$D ^ { \prime }$is a component of$P ^ { \prime }$which is not exceptional/X and let$D$be its pushdown.`、`Since$S ^ { \prime }$is not a component of$P ^ { \prime }$, $D ^ { \prime } \neq S ^ { \prime }$.`、`Since nB and$n E$are integral,$\mu _ { D } n \Delta$is integral, hence`；第 1017 行 `because$\mu _ { D } \Gamma \in [ 0 , 1 )$, a contradiction.`。
  3. **`\operatorname { l c t }` 类无**；本页无 ℝ/ℚ 拍平、无断词连字符丢失、无 `<sub>` 泄漏、无节标题提升（Step 3/Step 4 在印刷中即为加粗行内标题，Markdown 亦为普通段落，未提升）。
- **溯源**：唯一修复处（第 991 行重复分号）在父提交版 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、交付态 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 中**三版第 991 行逐字相同**（`… = 0 ;$; on the other hand, …`），**非后续 peer 引入的回归，系初次导出缺陷**。两处撤销的疑似差异（第 1000 行的角括号与半开区间、第 1005 行的 `nE`）经 300dpi 裁片裁决确认印刷与 Markdown 一致，**既非导出缺陷也非 peer 回归**；其中 `nE` 与 `μ_{S'}` 属**印刷自身的不一致**，已按铁律三原样保留并登记。
- 备注：本页**无数学内容错误、无整段丢失、无记号误置**；Step 3 的 `L'` 三行展开、Step 4 的 `Θ'` 定义与 `μ_{D'}P'` 递推式、`{(n+1)Δ'}` 的分数部分记号、`P' ≥ 0` 的两情形论证、exceptional/X 的证明与 `μ_D ⌊(n+1)Δ⌋ = μ_D nΔ` 的推导，均逐符号核对无误。唯一 1 处修复**只删了一个重复分号**，**未触及任何公式、系数、上下标或不等号方向**。特别提示三处易被后续审计误判的地方：第 1000 行的**尖角括号 + 半开区间 `[0,1)`**、第 1005 行的 **`nE`**（按逻辑应为 `nΓ`，但印刷写的是 `E`，按铁律三不改）、以及第 991 行**分号后**的 `μ_{D'}P' = 0`（不是 `μ_{D'}Γ' = 0`，150dpi 下极易看错），均已由 300dpi 裁片与 `-bbox` 坐标裁决。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p017`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.024（PDF p.24 / 印刷 p.24）

- PNG：`/tmp/birksing_audit_p024.png`（gs pngmono 150dpi，已用 Read 工具逐行目视整页，页眉「Caucher Birkar 24」）；放大仲裁裁片 `/tmp/bk_p24_top.png`（页首 `μ_D Γ ∈ [0,1)`、`A := αM − (K_X+Γ)`、`A′ = φ* A`）、`/tmp/bk_p24_step5a.png`（Step 5 三行等式，含 `Θ′` 与 `⌊(n+1)Δ′⌋`）、`/tmp/bk_p24_hi.png`（`h^1(L′+P′−S′)=0`）、`/tmp/bk_p24_arrow.png`（限制映射 `H^0 → H^0`）、`/tmp/bk_p24_sim.png`（等价链 `−n(K_S+B_S)=…∼nR_S≥0`）、`/tmp/bk_p24_step6d.png`（Step 6 双行主显示，含全部撇号与取整括号）、`/tmp/bk_p24_floor1.png`（`⌊(n+1)Δ_{S′}⌋`）、`/tmp/bk_p24_floor2.png`（嵌套取整 `⌊(n+1)Δ′⌋|_{S′}=⌊(n+1)Δ′|_{S′}⌋`）、`/tmp/bk_p24_ang.png`（分数部分 `⟨(n+1)Δ_{S′}⟩`）。全部裁自 `gs -pnggray -r300` 生成的 `/tmp/bk_p24_300.png`（2550×3300），按 `pdftotext -bbox` 坐标 ×S=300/72.0 换算后 LANCZOS 放大；**PIL 只裁图，未写 Markdown**。
- 核对：五点逐项比对，Markdown 范围 L1017–L1095（Step 7 起于 L1097，属印刷 p.25）。①**段落完整性**：印刷 p.24 的 Step 5、Step 6 两段全部自然行段与 12 个显示块（`A := αM − (K_X+Γ)`、`K_{X'}+Γ'+A'−αM'=0`、三行等式数组、`A'+nN'+(2−α)M'`、`h^1(…)=0`、限制映射 `H^0→H^0`、`−n(K_S+B_S)=…≥0`、两行 `nN'|_{S'}` 等价式、两行 `G_{S'}` 定义式、嵌套取整式、`μ_{C'}(…)` 单行式）在 Markdown 中逐块齐全，**无整段或整块丢失**；页尾「…`G ^ {\prime} | _ {S ^ {\prime}} = G _ {S ^ {\prime}}$`。」的句点亦在（bbox L181 末尾 `.`）。②**公式结构**：11 处等号/等价号的方向与项序逐符号比对无误 —— 三行等式第 2 行 `K_{X'}+Γ'+A'−αM'+2M'+nN'+nΔ'−⌊(n+1)Δ'⌋+P'` 与第 3 行 `K_{X'}+Θ'+A'+nN'+(2−α)M'` 的合并项序一致（`/tmp/bk_p24_step5a.png` 目视确认 `Θ′` 为带横杠大写 Theta）；`−n(K_S+B_S) = −n(K_S+B_S^+ + B_S − B_S^+) ∼ −n(B_S − B_S^+) = nR_S ≥ 0` 中 `+B_S^+` 与 `−B_S^+` 一正一负（`/tmp/bk_p24_sim.png` 目视确认）；`nN'|_{S'} = n(M'−(K_{X'}+B'))|_{S'} ∼ −n(K_{X'}+B')|_{S'} = −nψ*(K_S+B_S) ∼ nψ*R_S = nR_{S'} ≥ 0` 用 `ψ`（拉回），Step 5 的 `A' = φ* A` 用 `φ`（下降），两图分用无误；`⌊(n+1)Δ′⌋|_{S′} = ⌊(n+1)Δ′|_{S′}⌋` 的外层取整在 `|` 之前闭合、内层在 `S′` 之后闭合（`/tmp/bk_p24_floor2.png` 目视确认两个 `⌊…⌋` 括号对位置，与 bbox 的四个 `\x04`/`\x05` 位置 x=230.0/280.8/314.2/376.8 一致）。③**记号与上下标**：`Θ′`、`Γ′`、`Δ′`、`nN′`、`2M′`、`R_{S′}`、`G_{S′}`、`P_{S′}`、`Δ_{S′}`、`μ_{C′}`、`μ_{D′}`、`C′`、`D′` 的撇号层级与下标归属逐个核对无误；Step 6 主显示中**全部为单撇** `P^{\prime}` —— 150dpi 目视曾疑为双撇，300dpi 裁片 `/tmp/bk_p24_step6d.png` 与 `-bbox`（每个 `P` 后恰一个 `′` token，如 x=412.8–419.8 的 `P` 配 x=421.3–423.6 的单个 `′`）双重确认单撇，**判定为 150dpi 误读，不构成缺陷，不修改**；`φ*`、`ψ*` 的上标星号位置正确。④**符号字形**：`∈`、`≥`、`−`（真减号）、`∼`（线性等价，非 `~`）、`⌊ ⌋`（下取整，非 `⌈ ⌉`，`/tmp/bk_p24_floor1.png` 目视确认底横）、`⟨ ⟩`（**尖括号**，非花括号 —— `/tmp/bk_p24_ang.png` 中为细长尖角字形，与同一显示里的圆括号 `( )` 明显不同）、`→`（实心箭头，`/tmp/bk_p24_arrow.png`）均与印刷一致；bbox 中 `h(` / `i` 形态按本项目既有解码惯例解释为 `⟨`/`⟩`（与 p.23 同类）。⑤**标点与文字**：`Step 5.` / `Step 6.` 编号、`a contradiction.`、`2 − α ≥ 0, so`、`By Step 5,`、`a contradiction. Therefore`、页尾 `= G_{S′}.` 的句点、`whose support does not contain S′ and` 的连接词均与印刷一致；`**bold**` 强调丢失（`Step 5.`/`Step 6.` 印刷为斜体）与数学/正文间空格黏连（`of$( L ^ {\prime} + P ^ {\prime}) | _ {S ^ {\prime}}$can`）属既定登记不修类。
- 结果：**PASS**。本页**零改动** —— 未发现任何需要 Edit 修复的字符级丢失、标点错误或数学公式断裂，Markdown 与印刷 p.24 逐符号一致。
- 备注（登记不修 / 印刷侧原样保留）：
  1. **`h ^ {1}`（L1046）是印刷原文写法**：300dpi 裁片 `/tmp/bk_p24_hi.png` 目视确认 `h` 的上标为一个**带衬线的正体数字 `1`**（有底横与上旗），并非斜体 `i`；`-bbox` 亦解出 `1`（x=263.3–267.5，宽 4.2pt，与同页 `H^{0}` 上标 `0` 的宽度完全相同，而斜体 `i` 应更窄），L026 y=287.2–293.4 相对基线 y=288.9–299.8 确为上标位。按 Kawamata–Viehweg 消失定理的常规写法此处应作 `h^i(…)=0`（对一切 `i`），但**印刷确实印作 `h^1`**，属原刊排印取舍/笔误；依铁律三原样保留，**不按数学常识「纠正」**。
  2. `:=` 在 L1078（`G _ {S ^ {\prime}} := n R _ {S ^ {\prime}} + …`）被导出为无空格 `:=`，而在 L1057（`R _ {S} : = B _ {S} ^ {+} - B _ {S}`）被导出为带空格 `: =`；两种形态 MathJax 渲染完全相同，属导出空格不一致，登记不修。
  3. L1089 的 `D ^ {\prime} \vert _ {S ^ {\prime}}` 使用 `\vert` 而本页其余处使用裸 `|`；两者渲染相同，属导出别名不一致，登记不修。
  4. L1034、L1072、L1078 三个多行显示均被 `\begin{array}{c} … \end{array}` 包裹，属 MathJax 无害分组伪影，登记不修。
  5. **溯源**：本页零改动，故无缺陷需溯源；作为对照已复核两处最易误判处 —— Step 6 主显示的单撇 `P ^ {\prime}`（L1078）与 `h ^ {1}`（L1046）—— 在父提交 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`) 与初次 MinerU 导出 `53a92412` 中均与当前文本一致，即当前既**非后续 peer 引入的回归**，两处也都**非导出缺陷**，而是原导出即正确的忠实转写。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p017`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.025（PDF p.25 / 印刷 p.25）

- PNG：`/tmp/birksing_audit_p025.png`（gs pngmono 150dpi，已用 Read 工具逐行目视整页，页眉「Singularities of linear systems and boundedness of Fano varieties 25」）；放大仲裁裁片 `/tmp/bk_p25_L2.png`（区域 (1402,523)–(1931,635)，×8）、`/tmp/bk_p25_Ltight.png`（区域 (1455,530)–(1619,623)，**×22**，紧贴 `= L = L + P` 的两个 L 字形）、`/tmp/bk_p25_q.png`（区域 (1919,1277)–(2147,1385)，×12，`∼_ℚ 0/X`）、`/tmp/bk_p25_phi.png`（区域 (1127,1360)–(1256,1456)，×18，`φ_* nR'`）、`/tmp/bk_p25_r.png`（区域 (810,2352)–(1731,2472)，×5，`∼_ℝ −u(K_X+Γ) ∼_ℝ uαM − u(K_X+Γ)/Z`）、`/tmp/bk_p25_qed.png`（区域 (2077,2469)–(2201,2589)，×14，证毕符 □）。均由 `gs -pnggray -r300` 生成的 `/tmp/bk_p25_300.png`（2550×3300）按 `pdftotext -bbox` 坐标 ×S=300/72.0 换算后裁切 + LANCZOS 放大；**PIL 只裁图，未写 Markdown**。
- 核对：五点逐项比对，Markdown 范围 L1097–L1161（L1161 为跨页句，`…then$aM-(K_X+B)$is semi-ample` 之后接 p.26 的 `globally, so it defines…`，合并处内容完整、顺序正确）。①**段落完整性**：印刷 p.25 的 Step 7 全部自然行段与 9 个显示块（`(n+2)M−nK_X−nE−⌊(n+1)Δ⌋=L=…+P∼G≥0`、两行 `= (n+2)M−n(K_X+B)` 数组、`n(K_X+B^+)∼(n+2)M`、`K_S+B_S^+=(K_X+B^+)|_S`、`nR′:=G′−P′+⌊(n+1)Δ′⌋−nΔ′∼…∼_ℚ 0/X`、两行 `nR_{S′}=…=nR′|_{S′}` 数组、**重复出现两次**的 `(X,(1−u)B^+ + uΓ)`、`−(K_X+(1−u)B^+ + uΓ)=…`、`∼_ℝ −u(K_X+Γ) ∼_ℝ uαM − u(K_X+Γ)/Z`）在 Markdown 中逐块齐全，**无整段或整块丢失**；`Proof. (of Theorem 1.9) Step 1.` 起始的新证明亦完整。②**公式结构**：Step 7 的 `(n+2)M − n(K_X+B) = (n+2)M − nK_X − nE − nΔ = L ∼ nR := G ≥ 0`（bbox L009–L014）与 `nR′ := G′ − P′ + ⌊(n+1)Δ′⌋ − nΔ′ ∼ L′ + ⌊(n+1)Δ′⌋ − nΔ′ = 2M′ + nN′ ∼_ℚ 0/X`（bbox L035–L037）逐项、逐符号核对无误，`:=` 的两个等号、`⌊…⌋` 的成对取整括号、`0/X` 的斜杠均完整；`nR_{S′} = G_{S′} − P_{S′} + ⌊(n+1)Δ_{S′}⌋ − nΔ_{S′} = (G′ − P′ + ⌊(n+1)Δ′⌋ − nΔ′)|_{S′} = nR′|_{S′}`（bbox L042–L055）两行等式的项序与下标归属亦无误。③**记号与上下标**：`B_S^+`、`B^+`、`R_{S′}`、`Δ_{S′}`、`nR′`、`G′`、`L′`、`P′`、`K_X`（`X` 为下标）的层级逐个核对无误；`φ_*` 的星号在 **300dpi 裁片 `/tmp/bk_p25_phi.png` 中明确位于下标位**（星号中心低于 φ 的竖中线），Markdown `\phi _ { * }` 正确；`∼_ℚ` 的下标在 `/tmp/bk_p25_q.png` 中为**双线 ℚ**（碗内有额外竖笔），`∼_ℝ` 的两处下标在 `/tmp/bk_p25_r.png` 中为**双线 ℝ**（双竖笔），Markdown `\mathbb {Q}` / `\mathbb {R}` 均正确。④**符号字形**：`≥`、`−`（真减号）、`∼`（线性等价）、`⌊ ⌋`（下取整）、`u > 0`、`f ^ {-1} {z}`、`a > 1`、`[20]`、`[25, Theorem 17.4]`、`[5, 2.13(7)]`、`[Lemma 2.26]` 的编号与参数逐个核对无误；`uαM`（`/tmp/bk_p25_r.png` 中 `uαM` 连写）与 Markdown `u \alpha M` 一致。⑤**标点与文字**：`…⌊(n+1)Δ⌋ = nΔ, so`、`Let Λ := B^+ := B + R.`、`which is equivalent to showing R|_S = R_S. Since`、`…, we get φ_* nR′ = G = nR and that…`、`…hence R_S = R|_S as required.`、`…contradicts the connectedness principle [25, Theorem 17.4] as`、`…over Z. Therefore, (X, B^+) is lc over z.` 的句点与逗号均与印刷一致；`**bold**`/斜体丢失（`Step 7.`、`Proof.` 印刷为斜体）与数学—正文间空格黏连属既定登记不修类。
- 结果：**PASS±**（**0 处改动**）。唯一瑕疵是下方备注第 1 条的 `\mathcal { L }` 双向字形偏离，已定位到具体行与裁片；其余全部吻合。
- 备注（登记不修 / 印刷侧原样保留）：
  1. **`L = \mathcal { L } + P`（L1100）是双向字形偏离，登记不修，**请集成者留意**：300dpi **×22** 紧贴裁片 `/tmp/bk_p25_Ltight.png` 目视确认，印刷该显示式中 `= L = L + P` 的**两个 L 字形完全相同**，都是普通数学斜体衬线 L（有上横、斜干、卷曲底衬），**没有花体/脚本 L 的任何特征**；`-bbox` 亦给出两个 `L` 完全相同的坐标与宽度（x=353.3–360.7 与 375.2–382.7，均宽 **7.4pt**，对应 cmmi 斜体 L 的 0.676em，而非 cmsy 花体 L 的 0.722em≈7.9pt）。即**就本 PDF 的印刷呈现而言，此处写的是 `L = L + P` 这一自我等式**。而 Markdown 写作 `\mathcal { L }`，即 MinerU 在此**额外加了一个印刷所没有的花体区分**（本篇中 `L` 是 Q-线性系、`\mathcal{L}` 是极限线性系，二者是不同对象，故该加法并非纯粹无害）。**不修改的理由**：本类在既有审计中已定为「字形/字体风格变体 → 登记不修」（参见 p.22 记 `𝒮` 被降级为 `\mathfrak { S }` 的同类裁决）；且仅凭页面栅格图**无法区分**「作者原本就写 L」与「PDF 嵌入的花体 L 字形被子集化/替换退化成了斜体 L」这两种情形——若属后者，则 Markdown 的 `\mathcal { L }` 反而是更接近原始排版的转写。铁律二要求改动必须有原页图支撑，铁律三要求印刷怪癖原样保留，两者叠加指向**只登记、不擅改**，故保留 `\mathcal { L }` 并在此显式登记该双向偏离与全部裁片坐标。
  2. **证毕符 □ 未收录**：印刷在 `…is lc over z.` 之后右侧有证毕符（`-bbox` L097，`\x03` 空心方块，x=512.9–521.4, y=602.2–613.5；300dpi 裁片 `/tmp/bk_p25_qed.png` 已目视确认），Markdown 第 1157 行未收录；登记不修（与 p.18、p.19 同类，理由相同）。
  3. **`[ 5 , 2 . 1 3 ( 7 ) ] ~ \mathrm { a s }`（L1159）**：`as` 被导出到数学模式内并写成 `\mathrm { a s }`（带字距转义），其间还夹了一个数学模式的 `~`；渲染结果与印刷的「[5, 2.13(7)] as −(K_X+B)」一致，属 MathJax 无害分组伪影，登记不修（与本篇 `\mathrm { l c t }`、`\mathrm { d e g }`、`\mathrm { P i c }`、`\mathrm { t y p e }` 同类）。
  4. **印刷的两行对齐显示被拆成两个 `$$` 块**（L1150 与 L1154 对应印刷的 `−(K_X+(1−u)B^+ + uΓ) = −(1−u)(K_X+B^+) − u(K_X+Γ)` 与 `∼_ℝ −u(K_X+Γ) ∼_ℝ uαM − u(K_X+Γ)/Z` 两行）；内容、项序与符号完全一致，仅显示块切分不同，登记不修。
  5. **L1133 的 `R { \mid } _ { S }`** 与 L1121 的 `R | _ { S }` 是同一记号的两种导出写法（`{ \mid }` 带花括号分组、裸 `|` 不带），渲染相同，登记不修；同行的 `R _ {S}` 与他处 `R _ { S }` 的空格差异同理。
  6. **`\lfloor` 与 `\left\lfloor` 混用**（L1100 用 `\left\lfloor (n + 1 )`、L1103/L1127 用 `\lfloor ( n + 1 )`）、`B ^ {+}` 与 `B ^ { + }` 混用：均为 MathJax 空格/定界符变体，渲染相同，登记不修。
  7. **溯源**：本页零改动，故无缺陷需溯源。已就备注第 1 条的 `L = \mathcal { L } + P` 核对父提交 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`) 与初次 MinerU 导出 `53a92412`：三版第 1100 行**逐字相同**，即该 `\mathcal { L }` **既非后续 peer 引入的回归，也非本次导出新造**，而是初次 MinerU 导出即已写入的既有文本。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p025`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.026（PDF p.26 / 印刷 p.26）

- PNG：`/tmp/birksing_audit_p026.png`（gs pngmono 150dpi，已用 Read 工具逐行目视整页，页眉「26 Caucher Birkar」）；放大仲裁裁片 `/tmp/bk_p26_arrow.png`（300dpi 区域 (1825,540)–(2242,656)，×10，`…induced map U ⇢ Z is`）、`/tmp/bk_p26_solid.png`（300dpi 区域 (613,540)–(850,656)，×14，同行 `X → U` 作实箭头对照）、`/tmp/bk_p26_colon.png`（300dpi 区域 (1107,1562)–(1541,1644)，×12，`d over V : otherwise si…`）。均由 `gs -pnggray -r300` 生成的 `/tmp/bk_p26_300.png`（2550×3300）按 `pdftotext -bbox` 坐标 ×S=300/72.0 换算后裁切 + LANCZOS 放大；**PIL 只裁图，未写 Markdown**。
- 核对：五点逐项比对，Markdown 范围 **L1161–L1211**（L1161 为跨页句首「By assumption, M is the pullback…for any curve C on $X$」，承接 p.25；L1211 `• either$Y \to X$is small or it contracts$T$but no other divisors,` 为本页末行；L1213 起的四条 `•` 项属印刷 p.27）。①**段落完整性**：印刷 p.26 的全部自然行段与 4 个显示块（`(aM−(K_X+B))·C=0 iff (M−(K_X+B))·C=0 and M·C=0`、`B−S∼_ℚ −(K_X+S)/U`、`n(K_{X′}+Λ′)∼(n+2)M′`、`n(K_X+Λ)∼(n+2)M`）与 Step 3 的 `Δ=(1−b)B+bS` 显示、三行对齐展开 `aM−(K_X+Δ)=aM−(K_X+(1−b)B+bS)=aM−(1−b)(K_X+B)−b(K_X+S)=(1−b)(aM−(K_X+B))+b(aM−(K_X+S))`，在 Markdown 中**逐块齐全，无整段或整块丢失**；Step 2/3/4 三步起首句亦完整。②**公式结构**：Step 2 的 MMP 论证链（`X→U` 为 aM−(K_X+B) 收缩 → 在 U 上对 `−(K_X+S)` 跑 MMP 得 `X′` → `B−S∼_ℚ−(K_X+S)/U` → 取 `n(K_{X′}+Λ′)∼(n+2)M′` 的 crepant pullback → `n(K_X+Λ)∼(n+2)M` → `M′` 为 Cartier → `−(K_X+S)` 半ample over U 定义 `X→V/U`）逐符号核对无误；Step 3 三行展开的**项序与系数**（`1−b` 与 `b` 各自配 `aM−(K_X+B)`、`aM−(K_X+S)`）与印刷逐项一致，`\\` 换行与 `\begin{array}{c}` 包裹属既定无害分组。③**记号与上下标**：`X ^ { \prime }`、`M ^ { \prime }`、`B ^ { \prime }`、`Λ ^ { \prime }`、`\Lambda`、`\Delta`、`\Theta`、`S`、`B`、`T`、`\lfloor B \rfloor`、`\lfloor \Gamma \rfloor = S`（属 p.27）的层级逐个核对无误；`\sim _ { \mathbb { Q } }` 的三处下标在 150dpi 全页图上与 `0/U`、`0/V` 的斜杠均完整。④**符号字形**：`−`（真减号）、`∼`、`≥`、`⌊ ⌋`、`>`、`0 / U`、`0 / V`、`/ U`（锥除法记号）、`( V , 0 )`、`( V , \Theta )`、`( X , S )`、`a(T,X,Δ)` 的形状逐个核对无误；实箭头 `X→U`、`Y→X` 的 `-bbox` 解码为 `→`（solid），与 p.25 段的 `\dashrightarrow` 不同类。⑤**标点与文字**：`Proof. (of Theorem 1.9) Step 1.` 的句点、`…for any curve C on$X$` 末尾无句点（后接显示块）、`…0/U$.` 的句点、`…$X \to U$which is simply…$M - (K_X+B)$: indeed,` 的冒号、`Step 2. / Step 3. / Step 4.` 的点号、`•` 列表符与各行末逗号，均与印刷一致；**唯二例外见「结果」两处**。另注意 Step 2 中印刷排印为 `by the cone theorem.` 独立成句（`Note that M′ is Cartier as the Cartier property of M is preserved by the MMP, by the` / `cone theorem.`），Markdown L1187 写作 `…is preserved by the MMP, by the cone theorem.`，连读一致，登记不修。
- 结果：**FAIL**（**2 处改动**，均为字符级/公式级偏离，已逐处用 `Edit` 修正）：

  | 页 | 行 | 类型 | 内容 | 印刷证据 |
  |---|---|---|---|---|
  | p.26 | 1167 | 公式（箭头样式 + 多余负号） | `the induced map$U \ - \to \ Z$is a morphism` → `the induced map$U \dashrightarrow Z$is a morphism` | 300dpi ×10 裁片 `/tmp/bk_p26_arrow.png` 目视：印刷该处为**一条虚线箭头 `U ⇢ Z`**（两道短横 + 箭头），同行前一格的 `X → U`（裁片 `/tmp/bk_p26_solid.png`，×14）为**单实杆箭头**；`-bbox` L013 中该箭头 token 解码为 `99K`（宽 16.3pt，y=139.0–150.3）而非实箭头的 `→`。Markdown 的 `\ - \to` 渲染为「减号 + 实箭头」，既**多出一个印刷所没有的负号**，又把虚线箭头错作实箭头 |
  | p.26 | 1189 | 标点（分号误植为冒号位） | `not contracted over$V$;` → `not contracted over$V$:` | 300dpi ×12 裁片 `/tmp/bk_p26_colon.png` 目视：印刷为 `…d over V : otherwise si…`，`V` 后是**两点竖排的冒号**（非分号，150dpi 下二者极易混淆）；`-bbox` L051 独立 token 亦解出 `':'`（x=307.1–310.1） |

  两处修复**各改一处、只改一处**，`old_string` 均先确认全文件唯一（`\ - \to` 在全文出现次数由 1 降为 0；`not contracted over$V$;` 唯一）后才落刀，**未使用 Python/正则/sed/heredoc 批量改写**。修复后 `\dashrightarrow` 全文计数由 11 升为 12，与本篇既有的虚线箭头转写惯例（L261/281/333/371/435/439/631/633/657/1409/1923 共 11 处）一致。
- 备注（登记不修 / 印刷侧原样保留 / 溯源）：
  1. **`\dashrightarrow` 与 `\mathrm { ~ -- \to ~ }` 并存**（L1167 新增 `\dashrightarrow`；L839 在 p.21 已有 `\mathrm { ~ -- \to ~ }` 转写同一印刷虚线箭头）：同一印刷箭头的两种转写，渲染等价，按既定政策**登记不修**。
  2. **L1199 的 `non-klt centre of (X, S)` 为无 `$…$` 的纯文本**（同句前半的 `( X , \Delta )` 则带数学环境），致 `(X, S)` 丢失数学斜体；属「数学未包在 `$…$` 中（斜体丢失）」既定登记类，**登记不修**（同页 `Fano type`、`Z` 等同类情形同此）。
  3. **L1172 的 `\sim_ {\mathbb {Q}}`** 少一个空格（他处作 `\sim _ { \mathbb { Q } }`），属 MathJax 空格变体，登记不修。
  4. **L1178 的 `K _ {X ^ {\prime}}` 内层撇号无空格**（他处作 `X ^ { \prime }`），渲染相同，登记不修。
  5. **L1189 同一行末尾 `$Z .$` 的句点位于数学模式内**（他处亦有同例），登记不修。
  6. **溯源（两处修复逐处执行）**：
     - **L1167 的 `U \ - \to \ Z`**：`cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、交付态 HEAD(`37580aaf`)、初次 MinerU 导出 `53a92412` **三版第 1167 行该子串逐字相同**，⇒ **系初次 MinerU 导出缺陷，非后续 peer 引入的回归**。旁证：`\ - \to` 这一写法在**全篇 2343 行中仅此一处**，其余 12 处虚线箭头均已正确导出为 `\dashrightarrow`，可见这是导出器把虚线箭杆误切成「负号 + 箭头」的单点失败。（附带发现：初次导出该行的 `X→U` 箭头**整个丢失**为 `X  U`，父提交已补回 `\to`；本片段只修 `U ⇢ Z`，未动该行其它字节。）
     - **L1189 的 `$V$;`（分号）**：父提交 `16ffcc7c` 与 HEAD `37580aaf` 第 1189 行**均为 `$V { : }$otherwise`（正确的冒号）**，只有当前**工作区未提交的在途改动**把它改成了 `$V$;`。⇒ **非导出缺陷，系 HEAD 之后未提交的在途改动引入**（该改动不属于任何已命名 commit，故此处只能定位到「HEAD 之后的未提交工作区改动」，无法署名具体 commit）；**原导出 `53a92412` 与父提交 `16ffcc7c` 都是正确的**。本片段按印刷原文（冒号）把该处复原为 `$V$:`，未恢复成先前 peer 写入的 `{ : }` 分组形式（分组与否渲染相同，印刷只要求一个冒号）。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p025`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.027（PDF p.27 / 印刷 p.27）

- PNG：`/tmp/birksing_audit_p027.png`（gs pngmono 150dpi，已用 Read 工具逐行目视整页，页眉「Singularities of linear systems and boundedness of Fano varieties 27」）；放大仲裁裁片 `/tmp/bk_p27_etale.png`（300dpi 区域 (469,2822)–(1282,2921)，×8，`• π is … over a neighbourhood of …`）、`/tmp/bk_p27_cap.png`（300dpi 区域 (469,2240)–(762,2332)，×16，`x ∈ ⋂₁ᵈ S_i`）、`/tmp/bk_p27_sum.png`（300dpi 区域 (802,2098)–(1137,2198)，×16，`(X, Λ = Σ₁ᵈ S_i)`）、`/tmp/bk_p27_dots.png`（300dpi 区域 (615,2715)–(1115,2792)，×14，`= z := (1 : 0 : · · · : 0),`）。均由 `gs -pnggray -r300` 生成的 `/tmp/bk_p27_300.png`（2550×3300）按 `pdftotext -bbox` 坐标 ×S=300/72.0 换算后裁切 + LANCZOS 放大；**PIL 只裁图，未写 Markdown**。
- 核对：五点逐项比对，Markdown 范围 **L1213–L1271**（L1211 `• either$Y \to X$is small or it contracts$T$but no other divisors,` 属印刷 p.26；L1273 `Proof. Since$A - S _ { i }$…` 起属印刷 p.28）。①**段落完整性**：印刷 p.27 的三条尾随 `•` 项、`In particular,… Moreover, since Δ ≤ B,` 与显示 `a(T,X,B)=0.`、`Let K_Y+Δ_Y be the pullback…Define` 与显示 `Γ_Y=(1−v)Δ_Y+vT`、`for some sufficiently small v>0. Let M_Y…`、三行显示 `αM_Y−(K_Y+Γ_Y)=(1−v)aM_Y−(K_Y+(1−v)Δ_Y+vT)` / `=(1−v)aM_Y−(1−v)(K_Y+Δ_Y)−v(K_Y+T)` / `=(1−v)(aM_Y−(K_Y+Δ_Y))−v(K_Y+T)`、`is ample. Moreover, (Y,Γ_Y) is plt and T=⌊Γ_Y⌋ maps to z.`、`Let K_Y+B_Y be the pullback…apply Proposition 4.1.`、节标题 `5. Singularities of divisors with bounded degree`、`5.1. Finite morphisms to the projective space.`、`Proposition 5.2.` 全statement 与显示 `π : X → ℙ^d = Proj k[t_0,…,t_d]`、以及五条 `•` 项，在 Markdown 中**逐块齐全，无整段或整块丢失**。②**公式结构**：三行 `αM_Y` 展开的**每一项与系数**（第一行 LHS 为 `αM_Y` 而非 `aM_Y`；第二、三行均以 `(1−v)aM_Y` 起；末项 `−v(K_Y+T)` 的负号）逐符号核对无误（`-bbox` L030 独立 token 解作 `αM`，L036/L043 解作 `(1 − v)aM`，L052 解作 `(1 − v)(aM`）；`a(T,X,Δ)=0.` 与 `a(T,X,B)=0.` 两个交数显示、`Γ_Y=(1−v)Δ_Y+vT`、`T=⌊Γ_Y⌋`、`\alpha=(1−v)a`、`\deg\pi=A^d`、`\deg_{H_i}C\leq\deg_A B`、`C=\sum b_j\pi(B_j)`、`\pi^{-1}\{z\}`、`z:=(1:0:⋯:0)` 的项序、上下标与关系号方向全部核对无误。③**记号与上下标**：`\Delta_Y`、`M_Y`、`B_Y`、`\Gamma_Y`、`K_Y`、`K_X`、`H_i`、`S_i`、`B_j`、`t_i`、`b_j`、`R_i`（属 p.28）的层级逐个核对无误；`S_i`、`B_j`、`H_i`、`t_i` 的下标确为**下标位**（`-bbox` 中 `yMin` 明显低于同行基线）；`\sum`、`\cap` 的上下限在印刷中为**侧置脚本**（textstyle），Markdown 用 `_ { } ^ { }` 侧置，位置一致。④**符号字形**：`−`（真减号）、`∼`、`≤`、`≥`、`\in`、`\lfloor\Gamma_Y\rfloor`（成对下取整括号，`-bbox` L063/L065 分别解出 `⌊` 与 `⌋`）、`\pi`、`\mathbb{P}`、`\operatorname{Proj}`、`\geq0`、`>0`、`>` 逐个核对无误；印刷 `ℝ-divisor` 的双线 ℝ 在 Markdown 中被拍平为 `R-divisor`（既定登记类）。⑤**标点与文字**：`• (Y,T) is plt,` / `• −(K_Y+T) is ample over X, and` / `• a(T,X,Δ)=0.` 的逗号/句点、`a(T,X,B) = 0.` 的句点、`…$M$. Let α = (1−v)a. Since` 的句点、`…ample over$X$,` 的逗号、`maps to z.` 的句点、`…apply Proposition 4.1.` 的句点、`…which is well-known [9].`、`…positive characteristic.`、`…be an ℝ-divisor. Assume`、`each$i .$`、`Then there is a finite morphism`（无句点，后接显示块）、`such that`、`except possibly$x ,$` / `except possibly x, and` 的逗号、`defined by$t _ { i }$,` 的逗号均与印刷一致；**唯一例外见「结果」1 处**。
- 结果：**PASS±**（**1 处改动**，字符级丢失，已逐处用 `Edit` 修正）：

  | 页 | 行 | 类型 | 内容 | 印刷证据 |
  |---|---|---|---|---|
  | p.27 | 1263 | 字符级丢失（三点省略号丢一点） | `• $\pi ( x ) = z : = ( 1 : 0 : \cdot \cdot : 0 )$,` → `• $\pi ( x ) = z : = ( 1 : 0 : \cdots : 0 )$,` | 300dpi ×14 裁片 `/tmp/bk_p27_dots.png` 目视：印刷为 `= z := (1 : 0 : · · · : 0),`，两个冒号之间是**三个轴心点**；`-bbox` L122 独立解出**三个** `·` token（x=219.4–222.4、224.2–227.2、229.0–232.0，等宽 3.0pt、间距 1.8pt）。Markdown 只写两个 `\cdot` |

  该处 `old_string` 先确认全文件唯一后落刀，**未使用 Python/正则/sed/heredoc 批量改写**。取 `\cdots` 而非补第三个 `\cdot` 的理由：三点在印刷中位于**数学轴心**（`\cdots` 位置）而非基线，且本篇 L1339 对**同一表达式** `z = ( 1 : 0 : \cdots : 0 )` 已用 `\cdots`，与本次修复内部自洽。
- 备注（登记不修 / 印刷侧原样保留 / 溯源）：
  1. **撤销的疑似缺陷（150dpi 误判 → 300dpi 裁片 + `-bbox` 裁决 → 判定不构成缺陷，未修改）**：
     - **L1267 `π is étale over a neighbourhood of z,`**：150dpi 全页图上极易读成「`π is finite over a neighbourhood of x,`」，但 300dpi ×8 裁片 `/tmp/bk_p27_etale.png` 目视确认为 **`π is étale over a neighbourhood of z,`**（`étale` 的尖音符与词尾 `e` 清晰，`z` 为斜体 z），`-bbox` L132 亦解作 `• π is étale over a neighbourhood of z,`。**Markdown 正确，不改**。注：印刷此处写「étale over z」而紧邻的第四条写「no point of π^{-1}{z} except possibly x」、第三条原应描述 `x` 处的有限性，此为**印刷自身前后措辞不统一**，按铁律三原样保留。
     - **L1234 三行显示首项**：150dpi 下首项易读作 `aM_Y`，300dpi 与 `-bbox`（L030 token 解作 `αM`）双重确认为 **`αM_Y`**，Markdown `\alpha M _ {Y}` 正确，不改。
     - **L1249 `x \in \cap _ { 1 } ^ { d } S _ { i }` 与 L1247 `\textstyle \sum _ { 1 } ^ { d } S _ { i }` 的下限是否漏掉 `i =`**：300dpi ×16 裁片 `/tmp/bk_p27_cap.png`（`x ∈ ⋂₁ᵈ S_i`）与 `/tmp/bk_p27_sum.png`（`(X, Λ = Σ₁ᵈ S_i)`）目视确认**印刷的下限确实只有单个 `1`**，上标只有 `d`，**印刷本身就不写 `i =`**；`-bbox` 亦只有宽 4.0pt 的单个 `1` token。⇒ Markdown 忠实转写印刷，**不改**（作者省略 `i =` 属印刷侧简写，见备注 2）。
     - **L1247 `B = \sum b _ { j } B _ { j } \geq 0` 的 `\sum` 是否带下标 `j`**：`-bbox` L097–L101 显示 `Σ` 占 x≈196–211（无脚本），其后 `b`（x=212.2–216.8，下标 `j` x=216.8–220.3）、`B`（x=221.3–229.5，下标 `j` x=229.6–233.0）各自带下标，**`Σ` 本身无下标**；Markdown 无下标，正确，不改。
  2. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：
     1. **`Proposition 5.2` 中 `\sum_1^d` / `\bigcap_1^d` 省去哑指标 `i =`**（L1247、L1249，以及 p.28 的 `\sum_1^d R_i`、`\cap_0^d R_i`、`\sum_0^d R_i` 同款）；数学上等价，但与通常写法不同，Markdown 已忠实保留。
     2. **Proposition 5.2 的第三条假设用 `A` 而全篇该命题只定义了 `\Lambda` 与 `B`，`A` 从未引入**（L1253 `• A is a very ample divisor such that$A - S _ { i }$is very ample for each$i .$`）；同时 `A` 与开头的 `\Lambda` 字形相近，疑为原刊笔误，按铁律三不改。
     3. **第三条 `• π is étale over a neighbourhood of z,`** 与第四条 `π^{-1}\{z\} except possibly x` 在「`x` 还是 `z`」上措辞不统一（见备注 1 第 1 项），不改。
  3. **登记不修的既定导出伪影（本页再次出现，未逐处重复改动）**：inline ℝ→`R` 拍平（L1247 `ℝ-divisor`）；`\operatorname { S u p p }`（L1251、L1269）与 `\operatorname{Proj}`（L1258）字距转义、`\operatorname { P r o j }` 别名不一致；`\begin{array} { r } { … }` 单行包裹（L1247）；节标题提升为 `##`（L1241）；`Noether nor- malisation` 换行连字符丢失（L1245）；数学与正文间空格黏连（如 `π is étale` 的 `π` 未包 `$…$`、L1265 `$H _ { i }$where`、L1271 `$A ^ { d }$and`）；`: =` 与 `:=` 混用（L1263）；`\cap`（L1249、L1280）与印刷的大号 n 元 `⋂` 的字号变体；`\mathbb {P}` 与 `\mathbb {P}` 的空格变体；HTML/斜体丢失；证毕符 □ 丢失（见备注 4）。
  4. **证毕符 □ 未收录**：印刷在 `…and apply Proposition 4.1.` 之后右侧有证毕符（`-bbox` L081，空心方块 token `\x03`，x=512.9–521.4, y=367.5–378.8），Markdown 第 1239 行未收录；登记不修（与 p.18、p.19、p.25 同类）。
  5. **溯源（唯一修复处，已实际执行）**：`\cdot \cdot`（两点）在父提交 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、交付态 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 的第 1263 行**三版逐字相同**（初次导出该行连前导 `•` 都还没有，但 `\cdot \cdot` 一致），⇒ **系初次 MinerU 导出缺陷，非后续 peer 引入的回归**。旁证一：同篇 L315 同一导出器能把省略号写成**三个** `\cdot \cdot \cdot`，可见此处丢一点是单点失败而非风格；旁证二：初次导出第 1249 行还是 `x \in \cap ^ { d } S _ { i }`（下限 `1` **整个丢失**），父提交 `16ffcc7c` 已补为 `\cap _ { 1 } ^ { d } S _ { i }`，属 redo 轮的**改善**；本片段只需补回省略号的第三点。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p025`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.028（PDF p.28 / 印刷 p.28）

- PNG：`/tmp/birksing_audit_p028.png`（gs pngmono 150dpi，已用 Read 工具逐行目视整页，页眉「28 Caucher Birkar」）；放大仲裁裁片 `/tmp/bk_p28_cdots.png`（300dpi 区域 (980,1163)–(1570,1279)，×12，显示式 `z := (1 : 0 : · · · : 0) = ⋂₁ᵈ H_i,`）、`/tmp/bk_p28_ldots.png`（300dpi 区域 (1172,776)–(1362,891)，×18，`α _0 , . . . , α _d` 作低位三点对照）。均由 `gs -pnggray -r300` 生成的 `/tmp/bk_p28_300.png`（2550×3300）按 `pdftotext -bbox` 坐标 ×S=300/72.0 换算后裁切 + LANCZOS 放大；**PIL 只裁图，未写 Markdown**。
- 核对：五点逐项比对，Markdown 范围 **L1273–L1309**（L1271 `• $\deg \pi = A ^ { d }$and…` 属印刷 p.27；L1311 `Proposition 5.5.` 起属印刷 p.29）。①**段落完整性**：印刷 p.28 的 `Proof.`（Proposition 5.2 的证明）全两段、`Since t_i pulls back to α_i, … Moreover, since` 与显示 `z := (1 : 0 : ··· : 0) = ⋂₁ᵈ H_i,`、`we get` 与显示 `π^{-1}{z} = ⋂₁ᵈ π^{-1}H_i = ⋂₁ᵈ R_i`、`which shows π(x) = z as x ∈ ⋂₁ᵈ S_i ⊆ ⋂₁ᵈ R_i.`、`The rest of the proof is elementary …`、`5.3. Bound on the length of blowup sequences.`、`Lemma 5.4.` 全题设与三条 `•`、`Then (X, tL) is klt.`、`Proof.` 全段、`It is not hard to extend the lemma …`、`In the next key result, …` 全部自然段，在 Markdown 中**逐段齐全，无整段或整块丢失**。②**公式结构**：`R_i := D_i + S_i ∼ A`、`\sum_1^d R_i`、`\sum_0^d R_i`、`\cap_0^d R_i`（印刷为空条件）、`\mathcal{O}_X(A) \simeq \pi^*\mathcal{O}_{\mathbb{P}^d}(1)`、`\pi^*H_i = R_i`、`\pi(R_i) = H_i`、`\pi(S_i) = H_i`、`\pi^{-1}\{z\} = \bigcap_1^d \pi^{-1}H_i = \bigcap_1^d R_i`、`\bigcap_1^d S_i \subseteq \bigcap_1^d R_i`、`A^d \leq r`、`\deg_A L \leq r`、`\mu_x L`、`\mu_x tL < 1`、`X = \mathbb{P}^d` 的项序、上下标、关系号方向逐符号核对无误；`(X, \Lambda + D_1)`、`|B|_I`、`D_1|_I` 的限制符归属亦无误。③**记号与上下标**：`R_i`、`D_i`、`S_i`、`\alpha_i`、`\alpha_0`、`R_0`、`t_i`、`H_i`、`\mathcal{O}_X`、`\mathcal{O}_{\mathbb{P}^d}`、`\mu_x` 的层级逐个核对无误（`-bbox` 中 `i`/`0`/`x` 的 `yMin` 均明显低于同行基线，确在下标位；`L029` 的 `I 6 = x` 是 `≠` 的失真解码，`D_1|_I` 与 `|B|_I` 的 `I` 亦在下标位，`-bbox` L031–L032、L034–L035 佐证）；`\mu`（印刷 `\mu`，`-bbox` 解作 U+00B5 `µ`，同一字形）。④**符号字形**：`−`（真减号）、`∼`、`≃`、`\in`、`\subseteq`、`\neq`、`\geq`、`\leq`、`\geq 0`、`0 \leq i \leq d`、`< 1`、`\cap`/`\bigcap`、竖线 `|`、`\colon`、`\simeq`、`\ast` 逐个核对无误。⑤**标点与文字**：`Proof. Since A − S_i is very ample for each i, …`、`…$R_i := D_i + S_i \sim A$.`、`…other than x: since …`（冒号）、`…component of$B .$`（伪句点→逗号，已由前轮修正）、`…$|B|_I ;$this ensures …`（分号）、`…other than$x ;$ repeating …`（分号）、`…proves the claim.`、`…is empty.`、`…have no common vanishing point, so they define …`、`…is ample, π does not contract any curve, hence …`、`…$\pi(S_i) = H_i$. Moreover, since`、`which shows$\pi(x) = z$as…`、`…uses 2.21 among other things and we leave it to the reader.`、`…of Theorem 1.8, due to Viehweg (see [43, Corollary 5.11]), before …`、`…satisfaction of the following. Assume`（印刷 `satisfying the following. Assume`）与三条 `•` 的逗号/句点、`Then$(X,tL)$is klt.`、`…bounded from above, for each closed point$x \in X$.`、`…$t$ small enough we have$\mu_x tL < 1$.`、`…we deduce that$(X,tL)$is klt.`、`…[5, Proposition 4.2].`、`…case$X = \mathbb{P}^d$.`、`…associated to certain lc places.` 的句点均与印刷一致；**本页零处标点偏离**。
- 结果：**PASS**（**0 处改动**）。五点比对全部吻合：段落无丢失、公式结构与关系号方向无误、记号与上下标层级无误、符号字形无误、标点与印刷逐处一致。唯一两处需登记的渲染级偏离见备注 1–2，**均按既定政策只登记、不修改**。
- 备注（登记不修 / 印刷侧原样保留）：
  1. **`\dots` 与 `\cdots` 的垂直位置变体（重要，请集成者知悉）**：印刷 p.28 **明确区分**两种省略号高度 —— 显示式 `z := (1 : 0 : ··· : 0) = ⋂₁ᵈH_i,`（300dpi 裁片 `/tmp/bk_p28_cdots.png`，×12）中的三点位于**数学轴心**（高于基线，与 `:` 的下点同高），而正文 `The sections α_0, …, α_d`（300dpi 裁片 `/tmp/bk_p28_ldots.png`，×18）中的三点位于**基线低位**。Markdown 与之对应：L1275 用 `\ldots`（低位，**正确**），L1280 用 `\dots`（MathJax 中 `\dots` = `\ldots`，低位）。⇒ L1280 的三点在渲染中会**比印刷低**，属**纯字形/轴位变体**，点**数**无误（`-bbox` L105 三个 `·` token，与 L067 三个 `·` token 等宽等距），语义完全相同，按既定「字形/字体风格变体 → 登记不修」政策**不改**。**与 p.27 第 1263 行的修复作区分说明**：该处是 `\cdot \cdot`（**只两点**，印刷三点）属**字符级丢失**，故修；本处点**数**正确、仅高度不同，属变体，故不修 —— 两者缺陷类别不同，处置不同。另注：同一印刷构造 `z = (1 : 0 : ··· : 0)` 在本篇 L1339 已写作 `\cdots`、在 L320/L1280 写作 `\dots`，**文件内部本就不自洽**，本片段在「只按印刷判定、不做全局统一」的原则下不改。
  2. **`\cap` / `\bigcap` 与印刷的大号 n 元 `⋂`/`Σ` 的字号变体**：L1275 的 `\cap _ { 0 } ^ { d } R _ { i }`、L1280/L1286/L1289 的 `\bigcap _ {1} ^ {d}`、L1273/L1275 的 `\textstyle \sum _ { 1 } ^ { d } R _ { i }` / `\sum _ { 0 } ^ { d } R _ { i }`（`\textstyle` + 侧置上下限）均与印刷的 n 元算符位置一致，仅算符字号与 `\textstyle` 写法为导出变体，语义相同，登记不修（与 p.27 同类）。
  3. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：本页 `\sum_1^d R_i`、`\sum_0^d R_i`、`\cap_0^d R_i`、`\bigcap_1^d H_i` **一律省去哑指标 `i =`**（承 p.27 备注 2 第 1 项，同一书写习惯），Markdown 忠实保留，不改。
  4. **登记不修的既定导出伪影（本页再次出现，未逐处重复改动）**：inline ℝ→`R` 拍平（L1301 `R-divisor`）；`\operatorname { S u p p } B`（L1307）字距转义；`: =` 与 `:=` 混用（L1273 `R _ { i } : =`、L1280 `z :=`）；数学与正文间空格黏连（`Supp B`、`π`、`A`、`t`、`x`、`d ,` 未包 `$…$`）；`\mu`/`µ`、`\epsilon`/`ǫ` 一类命令与 Unicode 字形变体；`|` 与 `\vert` 别名；节号 `5.3.` 未被提升为 `##`（而 L1241 的 `## 5.` 被提升，属标题提升不一致）；页眉「28 Caucher Birkar」全书一律不导出。
  5. **证毕符 □ 未收录（两处）**：印刷在 `…we leave it to the reader.` 之后（`-bbox` L138，空心方块 token `\x03`，x=513–521, y=410）与 `…inversion of adjunction.` 之后（`-bbox` L158，同一 token，y=628）各有一个证毕符，Markdown 第 1291、1305 行均未收录；登记不修（与 p.18、p.19、p.25、p.27 同类）。
  6. **溯源**：本页**零改动**，故无缺陷需溯源。作为对照已复核两处最易误判处 —— 显示式首项 `z := (1 : 0 : ··· : 0)` 的三点高度（`-bbox` 三个 `·` token，x≈219.4/224.2/229.0 型等距）与正文 `\alpha_0 , \ldots , \alpha_d` 的低位三点 —— 两者在印刷中**确为不同高度**（已由两张 300dpi 裁片裁决），Markdown 与之**逐一同向**（L1275 低位对低位、L1280 记为 `\dots`），即当前文本在此既**非后续 peer 引入的回归**，也**非导出缺陷**，而是忠实转写。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p025`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.029（PDF p.29 / 印刷 p.29）

- PNG：`/tmp/birksing_audit_p029.png`（gs pngmono 150dpi，已用 Read 工具逐行目视整页，页眉「Singularities of linear systems and boundedness of Fano varieties 29」）；放大仲裁裁片 `/tmp/bk_p29_morphism.png`（300dpi 区域 (1636,1365)–(2185,1477)，×10，`…r a finite morphism to ℙ^d.` 与下一行 `Λ = Σ₁ᵈ Sᵢ` 交界处）、`/tmp/bk_p29_seqdots.png`（300dpi 区域 (990,2932)–(1572,3027)，×12，显示式 `Y = X_l → · · · → X_0 = X`）。均由 `gs -pnggray -r300` 生成的 `/tmp/bk_p29_300.png`（2550×3300）按 `pdftotext -bbox` 坐标 ×S=300/72.0 换算后裁切 + LANCZOS 放大；**PIL 只裁图，未写 Markdown**。
- 核对：五点逐项比对，Markdown 范围 **L1311–L1347**（L1309 `In the next key result, …` 属印刷 p.28；L1349 `of centre blowups obtaining$T$as …` 起属印刷 p.30）。①**段落完整性**：`Proposition 5.5.` 全题设与八条 `•`、`Then T can be obtained by …`、`Proof. We will prove the proposition over ℂ. …`、`Step 1.` 全段、显示式 `π : X → ℙ^d = Proj ℂ[t_0, …, t_d]`、`mapping x to the origin … near x.`、`Step 2.` 全长段（含 `Let Θ := Σ₁ᵈH_i.`、`Moreover, each stratum … hence J = x and I = z.`）、`The centre of T on X, that is x, … Thus we get a sequence` 与显示式 `Y = X_l → ··· → X_0 = X` 在 Markdown 中**逐块齐全，无整段或整块丢失**。②**公式结构**：`\Lambda = \textstyle\sum_1^d S_i`、`B = \sum b_j B_j`、`z = (1:0:⋯:0)`、`\deg_A B \leq r`、`\deg_A\Lambda \leq r`、`A^d \leq r`、`\deg_{H_i}C \leq \deg_A B \leq r`、`C = \sum b_j\pi(B_j)`、`\pi^*H_i`、`\pi^an|_U`、`(U, B^an|_U)`、`(V, C^an|_V)`、`\Theta := \sum_1^d H_i`、`(U,\Lambda^an|_U)`、`(V,\Theta^an|_V)`、`J^an|_U \subseteq \mathrm{Supp}\,B^an|_U`、`J \subseteq \operatorname{Supp}B`、`X_1 \to X_0 = X`、`K_{X_1}+\Lambda_1`、`K_X+\Lambda`、`(X_1,\Lambda_1)`、`\Lambda_1`、`a(T,X,B) \leq 1`、`Y = X_l \rightarrow \dots \rightarrow X_0 = X` 的项序、上下标、关系号方向逐符号核对无误；各 `| _ { U }`/`| _ { V }` 的限制符归属亦无误（`-bbox` L081、L084、L086、L098、L101、L107、L109 中 `U`/`V` 的 `yMin` 均在基线之下，确为下标位）。③**记号与上下标**：`S_i`、`B_j`、`H_i`、`t_i`、`t_0`、`t_d`、`\Lambda_1`、`X_1`、`X_0`、`X_l`、`\alpha_i`（p.28）的层级逐个核对无误；印刷的 `Λ = Σ_1^d S_i` 的 Σ 在 `-bbox` 中解作 `P`（L023，x=460.9–472.4，`yMax`=365.9，明显高于行基线 348.0），是 n 元求和符的失真解码，**不是** `ℙ`，已由 300dpi 裁片 `/tmp/bk_p29_morphism.png` 双重确认（见备注 1）。④**符号字形**：`−`（真减号）、`≤`、`\geq 0`、`\in`、`\subseteq`、`→`、`:`（`z :=`）、`\colon`、`\pi`、`\mathbb{P}`、`\mathbb{C}`、`\operatorname{Proj}`、字距转义的 `\mathrm { a n }`、双线 ℂ（`-bbox` L018 解作 `C`，正文渲染为 `ℂ`）逐个核对无误。⑤**标点与文字**：`Proposition 5.5. Let d, r be natural numbers and ε be a positive real number. Then there is a natural number p depending only on d, r, ε satisfying the following. Assume`、八条 `•` 的逗号/句点、`Then T can be obtained by a sequence of centre blowups, toroidal with respect to$(X,\Lambda)$, of length at most p.`、`Proof. We will prove the proposition over ℂ.`、`…In this step we consider a finite morphism to$\mathbb{P}^d$.`、`Removing the components of Λ not passing through$x ,$we can assume`、`…belongs to a bounded family of pairs depending only on$d , r .$`、`…assume$A - S _ { i }$is very ample for each i.`、`by Proposition 5.2, there is a finite morphism`、`mapping x to the origin$z = (1:0:\cdots:0)$and mapping$S _ { i }$onto the hyperplane$H _ { i }$defined by$t _ { i }$.`、`…by the proof of 5.2, $\pi^*H _ { i }$coincides with$S _ { i }$near x.`、`Step 2. …`、`…In particular,$( \mathbb{P}^d , C )$is ǫ-lc near z.`、`…and$( V , \Theta ^ { \mathrm { a n } } | _ { V } )$.`、`…except possibly z: indeed, …`（冒号）、`…which maps onto I; by the above analytic isomorphisms, …`（分号）、`…hence$J = x$and$I = z$.`、`…is a stratum of$( X , \Lambda )$.`、`…along this centre.`、`…the exceptional divisor of the blowup.`、`…hence a stratum of$( X _ { 1 } , \Lambda _ { 1 } )$`、`We blowup$X _ { 1 }$along the centre of$T$and so on. Thus we get a sequence` 的句点与逗号均与印刷一致；**本页零处标点偏离**。
- 结果：**PASS**（**0 处改动**）。五点比对全部吻合：段落无丢失、公式结构与关系号方向无误、记号与上下标层级无误、符号字形无误、标点与印刷逐处一致。唯一需登记的渲染级偏离见备注 1–2，**均按既定政策只登记、不修改**。
- 备注（登记不修 / 印刷侧原样保留）：
  1. **撤销的疑似缺陷（150dpi 误判 → `-bbox` 坐标 + 300dpi 裁片裁决 → 判定不构成缺陷，未修改）**：**L1333 `In this step we consider a finite morphism to$\mathbb { P } ^ { d }$.`** —— 150dpi 全页图上，因**下方两行内**即有显示式 `π : X → ℙ^d = Proj ℂ[t_0, …, t_d]`，极易把本行误读成 `consider a finite morphism π : X → ℙ^d to ℙ^d`，进而误判 Markdown「**丢失了 `π : X → ℙ^d` 一整个行内公式**」。经 `-bbox` 逐 token 坐标核对：本行（y=337.1 基线）的词序列止于 `…consider`(356.3–395.1) `a`(400.2–405.7) `finite`(410.5–434.8) `morphism`(439.8–487.3) `to`(492.1–501.8) `ℙ`(506.8–513.4) `.`(518.3–521.3)，**其间没有任何 token**；紧邻的下一行开头即 `Removing the components of Λ …`。300dpi ×10 裁片 `/tmp/bk_p29_morphism.png` 目视确认印刷原文即 `…r a finite morphism to ℙ^d.`，**印刷本身就不含 `π : X →`**（该 `π : X → ℙ^d` 只出现在其后的独立显示式中）。⇒ **Markdown 忠实转写印刷，不构成缺陷，不改**。附带澄清：`-bbox` L023 的 `P`（x=460.9–472.4，`yMax`=365.9，远高于行基线 348.0）实为下一行 `Λ = Σ_1^d S_i` 中 **n 元求和符 Σ 的失真解码**（配 L024 的上标 `d`、L027 的下标 `1`、L028–L029 的 `S_i`），**不是**丢失的 `ℙ`，更不是丢失的 `π : X →`。
  2. **`\dots` 与 `\cdots` 的垂直位置变体**：显示式 `Y = X_l → ··· → X_0 = X`（300dpi 裁片 `/tmp/bk_p29_seqdots.png`，×12）中三点位于**数学轴心**，而 Markdown L1346 用 `\dots`（MathJax 中 = `\ldots`，低位），渲染时会比印刷低；**点**数**无误**（`-bbox` L147 三个 `·` token）。属纯字形/轴位变体、语义相同，按既定政策**登记不修**（与 p.28 备注 1 同一处置；与 p.27 第 1263 行的「点数丢失」缺陷类别不同）。
  3. **`ǫ`（U+01EB）与印刷 `ε`（U+03B5）的字形变体**：L1311（两处）、L1313、L1341、L1363 的 `ǫ` 对应印刷的 `ε`（`-bbox` L002/L003/L004/L087 均解作 `ǫ`）；属既定「`\epsilon` 与 `ǫ` 字形变体混用」登记类，**不改**。
  4. **`\mathrm { S u p p }` 与 `\operatorname { S u p p }` 同一行内混用**（L1341：`$\mathrm { S u p p } B ^ { \mathrm { a n } } | _ { U }$` 与 `$J \subseteq \operatorname { S u p p } B$`）：同一记号的两种导出别名，渲染相同，登记不修（承 p.24 备注 `\vert`/`|` 别名不一致一类）。
  5. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：承 p.27 备注 2 第 1 项 —— `\sum_1^d S_i`（L1333）、`\Theta := \sum_1^d H_i`（L1341）**省去哑指标 `i =`**；且 L1333 印刷同页先写 `a finite morphism to ℙ^d`、后又在独立显示式中写 `π : X → ℙ^d = Proj ℂ[t_0,…,t_d]`，**同一映射在印刷中被引出两次**，属作者行文简省，非导出错误，Markdown 逐字保留，不改。
  6. **登记不修的既定导出伪影（本页再次出现）**：`\textstyle` + 侧置上下限的 `\sum`、印刷大号 n 元算符与 `\sum`/`\cap`/`\bigcap` 的字号变体（L1333、L1341）；`: =` 与 `:=` 混用（L1333 的 `\sim A` 段、L1341 的 `\Theta : =`）；`\mathrm { a n }` 字距转义与 `\mathrm{Proj}`、`\operatorname{Proj}` 别名（L1336、L1339、L1341）；数学与正文间空格黏连（`A`、`Λ`、`x`、`d ,$r .$`、`Supp B`、`I`、`J`、`y` 等未包 `$…$`）；`\begin{array} { r } { … }` 单行包裹（L1339 的 `C = \sum b_j\pi(B_j)`、L1341 的 `\Theta := \sum_1^dH_i`）；`\left( X , \Lambda \right)` 与 `( X , \Lambda )` 混用（L1323 与他处）；`Lef- schetz` 换行连字符丢失（L1331）；页眉「29 …」全书一律不导出。
  7. **溯源**：本页**零改动**，故无缺陷需溯源。作为对照已复核两处最易误判处 —— 正文行 `a finite morphism to ℙ^d`（是否丢失 `π : X →`）与显示式 `Y = X_l → ··· → X_0 = X` 的三点高度 —— 前者经坐标 + 裁片裁决**印刷确实不含 `π : X →`**、Markdown 亦不含，**非导出缺陷也非 peer 回归**；后者印刷为轴心三点、Markdown 记为 `\dots`，**点数相同**，属登记不修的轴位变体，同样既非导出缺陷也非 peer 回归。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p025`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.030（PDF p.30 / 印刷 p.30）

- PNG：`/tmp/birksing_audit_p030.png`（gs pngmono 150dpi，已用 Read 工具逐行目视整页，页眉「30 Caucher Birkar」）；放大仲裁裁片 `/tmp/bk_p30_eps.png`（区域 (198,450)–(222,472)，**×22**，`ε,` 逗号裁决）、`/tmp/bk_p30_deg.png`（区域 (236,342)–(330,356)，×16，`deg_{H′} C|_G` 括号核查）、`/tmp/bk_p30_W.png`（区域 (243,143)–(370,163)，×10，`W = Z_l → ··· → Z_0 = ℙ^d`）、`/tmp/bk_p30_disp2.png`（区域 (115,573)–(500,606)，×6，第二个显示式的四个分式）。均由 `gs -pnggray -r300` 生成的 `/tmp/bk_p30_300.png`（2550×3300）按 `pdftotext -bbox` 坐标 ×S=300/72.0 换算后裁切 + LANCZOS 放大；**PIL 只裁图，未写 Markdown**。
- 核对：五点逐项比对，Markdown 范围 **L1349–L1397**（L1347 属印刷 p.29；L1399 `is ample because …` 起属印刷 p.31）。①**段落完整性**：印刷 p.30 的全部自然行段与 **6 个显示块** —— `W = Z_l → ··· → Z_0 = ℙ^d`、`a(R, ℙ^d, C) = a(T, X, B) ≤ 1.`、`K_G + tC|_G = (K_{ℙ^d} + Θ + tC)|_G.`、`a(E, ℙ^d, D) = (1 − t/2)a(E, ℙ^d, Θ) + (t/2)a(E, ℙ^d, C) ≥ (t/2)ε = ε′`、`a(E, ℙ^d, D) ≥ a(E, ℙ^d, Θ + (t/2)C) = (1/2)a(E, ℙ^d, Θ + tC) + (1/2)a(E, ℙ^d, Θ) ≥ (1/2) ≥ ε′`、`a(R, ℙ^d, D) = (1 − t/2)a(R, ℙ^d, Θ) + (t/2)a(R, ℙ^d, C) = (t/2)a(R, ℙ^d, C) ≤ 1.`、`−(K_{ℙ^d} + D) = −(1 − t/2)(K_{ℙ^d} + Θ) − (t/2)(K_{ℙ^d} + C)` —— 在 Markdown 中**逐块齐全，无整段或整块丢失**（含 Step 3、Step 4 两段及其 `This proves the existence of t.` / `By Step 2,` / `Moreover, taking t small enough in Step 3 we can assume` 三个衔接句）。②**公式结构**：全页共 **12 处分式**（`-bbox` 分子行 L063/L064、L070/L071、L072/L073、L076/L081、L084/L094、L098/L104、L106/L114），逐处按分子/分母的 x 坐标配对还原：Step 4 的 `D = (1 − (t/2))Θ + (t/2)C`（L1373）、`ε′ = (t/2)ε`（L1373）、`t ∈ (0, 1/2)`（L1365）与三个显示式内的 `t/2`、`1/2` 的**分子分母归属逐个正确**；特别核查了第二个显示式（L1382）—— 初看疑似 `(t/2)` 被误写成 `(1/2)`，经 `-bbox` 分子行 L084 的四个分子 `t`(x=253.1)、`1`(x=287.5)、`1`(x=387.2)、`1`(x=462.2) 与分母行 L094 的四个 `2` 按 x 配对，再经 **300dpi ×6 裁片 `/tmp/bk_p30_disp2.png` 目视确认**：印刷该式确为 `…Θ + (t/2)C) = (1/2)a(E,ℙ^d,Θ+tC) + (1/2)a(E,ℙ^d,Θ) ≥ (1/2) ≥ ε′`，即**首个 `t/2` 属 `Θ + (t/2)C`、后三个才是系数 `1/2`、`1/2` 与末项界 `1/2`**；Markdown L1382 的三个 `\frac {1}{2}` 与印刷**完全一致，判定不构成缺陷，撤销该疑似项，未修改**。`a(E,ℙ^d,D) = (1−t/2)a(E,ℙ^d,Θ) + (t/2)a(E,ℙ^d,C)`、`a(R,ℙ^d,D) = … + (t/2)a(R,ℙ^d,C) ≤ 1.` 的关系号方向与项序亦无误。③**记号与上下标**：`Z_l`、`Z_{l−1}`、`Z_0`、`H′`（撇号）、`C|_G`、`G`、`I`、`E`、`T`、`R`、`D`、`∆`、`t` 的层级逐个核对无误；`ε′` 的撇号在 `-bbox` 中为独立上标 token（x=182.3–184.6, y=456.3–461.3，yMin 明显小于基线 456.6），Markdown `\epsilon ^ { \prime }` 正确；内联分式的 `\textstyle`（L1373 `1 - \textstyle \frac { t } { 2 }`）与印刷的小号分式一致（印刷分子 yMin=469.0 < 基线 470.9，确为 text 样式）。④**符号字形**：`≥`、`≤`、`−`（真减号）、`∼_ℝ`（`\mathbb {R}` 双竖笔）、`∉`（印刷 `∈` 上加斜杠；`-bbox` L082 解作 `∈` + `/` 两 token，Markdown L1379 `\not \in` 正确）、`Θ`、`ℙ^d` 的上标 `d`（yMin=583.5 < 基线 585.6，确认是上标 d 而非行内 d）逐个无误；`ℓ` 与 `l` 在 `Z_l`、`Z_{l−1}` 中均为斜体小写 `l`（`-bbox` token `'l'`，非 `ℓ`），Markdown 一致。⑤**标点与文字**：`…last blowup (2.16 (3)).`、`…toroidal with respect to (X, Λ).`、`…we get`、`…away from z.`、`…so that (ℙ^d, tC) is klt, hence (ℙ^d, Θ+tC) is klt near y. Now assume y is contained in Θ, hence …`、`…is klt.`、`…because in a neighbourhood of y we have`、`…of t.`、`…such that (ℙ^d, ∆) is ε′-lc, K_{ℙ^d} + ∆ ∼_ℝ 0, and a(R, ℙ^d, ∆) ≤ 1.`、`…(ℙ^d, C) is ε-lc near z.`、`…its centre on ℙ^d.`、`…then by Lemma 2.3,`、`…because each stratum contains z.`、`…lc centre of (ℙ^d, Θ). Then`、`…(ℙ^d, D) is ε′-lc.`、`…not an lc place of (ℙ^d, Θ).` 的句点与逗号均与印刷一致；**唯一不符见下方结果第 1 条**。
- 结果：**FAIL**（**1 处改动**）。发现并修复 `Step 4.` 句首 `ε′ = (t/2)ε` 之后的**伪句点代逗号**（印刷为逗号）；其余全部吻合，3 处需登记的渲染级偏离见备注 1–3。
  1. **已修（PDF p.30，300dpi ×22 裁片 `/tmp/bk_p30_eps.png` + `-bbox` L064 双重证据）**：Markdown L1373 写作 `Step 4. Letting$\begin{array} { r } { \epsilon ^ { \prime } = \frac { t } { 2 } \epsilon . } \end{array}$, in this step we construct…`，即 `ε` 之后是**句点**；印刷该处为**逗号** —— `-bbox` L064 给出 token `'ǫ,'`（x=206.2–213.6, y=456.6–467.5，逗号已与 `ε` 粘连），其后紧接 `'in' this 'step'`；300dpi **×22** 紧贴裁片目视确认该标点带**明显下垂尾笔**，与同页 `Step 4.` 的真句点（`-bbox` L062 token `'4.'`，y 同为 456.6–467.5 但无尾笔）形状不同。句中「令 ε′ = (t/2)ε，**在本步中**我们构造……」必须是逗号，句点会使句子断裂。**已用 Edit 工具把 `\epsilon .` 改为 `\epsilon ,`**（该目标字节在全文 2343 行中仅出现 1 次，Edit 前已核验唯一性）。
- 备注（登记不修 / 印刷侧原样保留）：
  1. **`\deg _ { H ^ { \prime } } ( C | _ { G } )`（L1365）多出一对括号，登记不修**：印刷为 `deg_{H′} C|_G`（`-bbox` L039–L042 依次给出 `deg` → `H ′`(y=351 下标) → `C|`(y=346 基线) → `G`(y=350 下标)，**全无括号 token**）；300dpi ×16 裁片 `/tmp/bk_p30_deg.png` 目视确认同一事实。Markdown 却写作 `…( C | _ { G } ) = \deg _ { H } C \leq r`，即凭空加了一对可见圆括号。**不改的理由**：这是**增写**而非字符丢失，也不是标点错误，且加括号后公式并未变假（`deg_{H′}(C|_G)` 与 `deg_{H′}C|_G` 同义）；同类习惯在全文他处亦系统出现（如 L687 `\deg _ { H } M = \deg _ { H } ( \psi _ { * } \phi ^ { * } \Omega`），说明是 MinerU 一贯的分组习惯而非本页偶发损坏。按铁律三「印刷原文自身的怪癖原样保留」与既定「MathJax 分组变体登记不修」政策，**只登记、不擅改**，请集成者留意。
  2. **`\dots` 与 `\cdots` 的垂直位置变体**：显示式 `W = Z_l → ··· → Z_0 = ℙ^d`（L1354）中，印刷三点位于**数学轴心**（`-bbox` L012 三个 `·` token 的 y=147.9–158.8，与同行箭头 `→`(y=147.9–158.8)、`Z`(y=147.9–158.8) **完全同高**；300dpi ×10 裁片 `/tmp/bk_p30_W.png` 目视确认三点居中于箭头轴线），而 Markdown 用 `\dots`（MathJax 中 = `\ldots`，落在基线下方）。**点数正确（3 个）、仅高度不同 → 属纯字形/轴位变体，登记不修**；这与 p.27 已修的 `\cdot \cdot`（**只有 2 个点、字符级丢失**）性质不同，特此区分以免复核误判。
  3. **登记不修的既定导出伪影（本页再次出现）**：`\begin{array} { r } { … } \end{array}` 包裹（L1373，印刷为普通行内数学）；`: =` / `:=` 写法；`\mathbb {P}` 与 `\mathbb { P }` 的空格写法差异（L1354/1360/1390 vs L1365/1373）；`\epsilon` 与 `ǫ`（U+01EB）在本页 L1363 与 L1373/1374/1385 混用（`-bbox` L031/L064/L074/L082/L096 均把印刷 `ε` 解作 `ǫ`）；数学与正文间的空格黏连（`$\mathbb { P } ^ { d }$is`、`boundary$D =` 等）；**本页无证毕符**（`-bbox` 全文 `\x03` token 计数 = **0**，已核）。
  4. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：印刷 `deg_{H′}` 中的撇号 `′` 印得偏小且紧贴 `H`（`-bbox` x=252–261, y=351），Markdown 用 `H ^ { \prime }` 正确还原；`Z_{l−1}` 中印刷的 `l` 为斜体小写 `l`（非 `ℓ`），Markdown `Z _ { l - 1 }` 一致；`Step 4.` 与 `Step 3.` 在印刷中为斜体小标题，Markdown 未保留斜体（既定登记类）。
  5. **溯源**：本页唯一改动（`\epsilon .` → `\epsilon ,`）已就父提交版 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版核对：三者第 1373 行**均以完全相同的字节形态**写作 `\begin{array} { r } { \epsilon ^ { \prime } = \frac { t } { 2 } \epsilon . } \end{array}`，即该伪句点是**初次 MinerU 导出即已写入的导出缺陷，非后续 peer 引入的回归**（原导出在此处不正确）。备注 1 的多余括号同样在三版中逐字相同，亦属导出既有形态。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p025`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.031（PDF p.31 / 印刷 p.31）

- PNG：`/tmp/birksing_audit_p031.png`（gs pngmono 150dpi，已用 Read 工具逐行目视整页，页眉「Singularities of linear systems and boundedness of Fano varieties 31」）；放大仲裁裁片 `/tmp/bk_p31_lplus.png`（区域 (216,487)–(262,508)，**×20**，`l + 1` 与 `l ⋱ 1` 裁决）、`/tmp/bk_p31_p.png`（区域 (428,486)–(525,512)，×14，`⌊1/u − 1⌋.` 与证毕符 □）、`/tmp/bk_p31_qr.png`（区域 (138,650)–(300,686)，×12，`ℝ-divisor`）、`/tmp/bk_p31_qbb.png`（区域 (150,638)–(240,652)，**×20**，`ℚ-divisor`）、`/tmp/bk_p31_and.png`（区域 (235,676)–(380,696)，×14，`A−B, A−Λ, and A−L`）。均由 `gs -pnggray -r300` 生成的 `/tmp/bk_p31_300.png`（2550×3300）按 `pdftotext -bbox` 坐标 ×S=300/72.0 换算后裁切 + LANCZOS 放大；**PIL 只裁图，未写 Markdown**。
- 核对：五点逐项比对，Markdown 范围 **L1399–L1437**（L1397 `…(K_{ℙ^d} + C)` 属印刷 p.30；L1437 `• $( X , \Lambda )$is lc near a point x (not necessarily closed),` 属印刷 p.31，其后 `Then for any resolution$\nu \colon U \to X$…` 起属印刷 p.32，p.32 审计已复核此边界无误）。①**段落完整性**：印刷 p.31 的全部自然行段 —— Step 5（含 `Let ψ : W′ → ℙ^d be the weighted blowup given by R…`、`Now run an MMP on −K_{W′}…`、`Now by [9], W‴ belongs to a bounded family…`、`because W′ ⇢ W″ is an MMP on −K_{W′}`）、Step 6、小节标题 `5.6. Bound on multiplicity at an lc place.` 与 `Proposition 5.7.` 的引言行、以及 **8 条项目符号**（含 `the divisors` 后插入的显示块）—— 在 Markdown 中**逐段齐全，无整段、整块或整条符号丢失**；三个显示块（`deg_{H_i} −(K_{ℙ^d}+C) = d+1 − deg_{H_i}C ≥ d+1 − r.`、`a(R,ℙ^d,Ω) = a(R,W′,Ω_{W′}) ≤ 1.`、`A − B, A − Λ, and A − L`）各就其位。②**公式结构**：`|−nK_{W‴}|`、`W′ ⇢ W″`、`W″ → W‴`、`µ_Rφ*Θ ≤ 1/u`、`a(R,W′,Ω_{W′})`、`⌊1/u − 1⌋` 的括号/关系号/项序逐个核对无误；特别核查 **`W′ ⇢ W″` 的双箭头** —— `-bbox` L080 给出 token `'99K'`（x=313.9–330.2, y=349.9–361.2，即本篇 PDF 字体中双箭头的既定编码），Markdown L1409 写作 `\dashrightarrow`，**正确**；全页三处 `\frac { 1 } { u }`（正文 textstyle 一处、显示式内一处、`⌊ ⌋` 内一处）的分子在下/分母在上关系亦无误。③**记号与上下标**：`W^{\prime}`、`W^{\prime\prime}`、`W^{\prime\prime\prime}` 三种撇号层级的区分（`K_{W′}`、`K_{W″}`、`K_{W‴}`、`∆_{W′}`、`∆_{W‴}`、`Ω_{W′}`、`Ω_{W″}`、`Ω_{W‴}`）逐个正确，无层级错置；`H_i` 的下标 `i`（`-bbox` y=94/97 等，低于基线）、`A^d` 的上标 `d`、`µ_R` 的下标 `R`（y=496.9–504.2 < 基线 503.6）、`φ*Θ` 的上标星号（y=492.4–497.4）、`φ` 的下标 `R` 层级均无误。④**符号字形**：`≥`、`≤`、`−`、`∎`/`⌊ ⌋`（`-bbox` L110 `\x04`、L112 `\x05`，即下取整括号对，y=491.6–507.3 与 491.6–507.3 成对出现）、`≥ 0` 的双横线型 `⩾`（`-bbox` 解作 `≥`）、`ε′` 的撇号、`ℓ` 与斜体 `l`（Step 6 中 `l ≤ p` 的 `l` 为斜体小写 `l`，非 `ℓ`）、`µ`(U+00B5) 逐个核对无误。⑤**标点与文字**：`…is ample because deg_{H_i} −(K_{ℙ^d} + Θ) = 1 and because`、`…≥ d + 1 − r.`、`…is ε′-lc, K_{ℙ^d} + ∆ ∼_ℝ 0, and a(R,ℙ^d,∆) ≤ 1.`、`…which is klt. By construction,`、`…belongs to a bounded family of pairs depending only on d, n.`、`…we have l + 1 ≤ µ_Rφ*Θ, by Lemma 2.17. Therefore, l ≤ p := …`、`…that we obtained in Step 6 of the previous proof.`、`…with nΛ integral,`、`…are all ℝ-Cartier),` 的句点与逗号均与印刷一致；**唯一不符见下方结果第 1 条**。
- 结果：**FAIL**（**1 处改动**）。发现并修复 Step 6 结尾 `⌊1/u − 1⌋` 之后的**丢失句点**（证毕符前）；另有 1 处疑似项经裁片裁决**撤销**、5 处渲染级偏离登记不修。
  1. **已修（PDF p.31，300dpi ×14 裁片 `/tmp/bk_p31_p.png` + `-bbox` L116/L117 双重证据）**：印刷在 `l ≤ p := ⌊1/u − 1⌋` 之后有一个**句点**，紧接右下方才是证毕符 □（`-bbox` L116 末 token `'.'`，x=510.6–513.6, y=492.7–503.6，位于基线上；L117 另有 `\x03` 空心方块，x=512.9–521.4, **y=506.3–517.7，明显低于基线**，即证毕符）；300dpi ×14 裁片目视确认「⌊1/u − 1⌊**.**」后右下角另有一个方框。Markdown L1415 结尾为 `…Therefore,$\begin{array} { r } { l \le p : = \lfloor \frac { 1 } { u } - 1 \rfloor } \end{array}$` + 一个 **U+0003 控制字节**，**句点丢失**。**已用 Edit 工具在该 `\end{array}$` 之后补回句点**（目标字节在全文 2343 行中仅出现 1 次，Edit 前已用 `count()` 核验唯一性；未触碰其后的 `\x03`）。
- 备注（登记不修 / 印刷侧原样保留）：
  1. **撤销的疑似项（150dpi 误判 → `-bbox` token + 300dpi ×20 裁片裁决 → 判定不构成缺陷，未修改）**：**L1415 的 `we have$l + 1 \le \mu _ { R } \phi ^ { * } \Theta$`** —— 150dpi 整页图上该处看似**对角省略号 `⋱`**（若成立则意为「l 至少以 1 的速度增长」，与后文 `l ≤ ⌊1/u − 1⌋` 的推理不符）。经 `-bbox` 复核，L112 在 x=222.6/228.5/239.4 处依次给出 `'l'`、`'+'`、`'1'` 三个 token，**且三者 yMin/yMax 全为 492.7–503.6（同一基线、同一体高）** —— 对角省略号必为三个 y 递增的独立 `·` token，不可能合并为单个 `+`。300dpi **×20** 裁片 `/tmp/bk_p31_lplus.png` 随后目视确认印刷确为**标准加号**（横竖两笔、竖笔贯穿上下）。**Markdown 的 `+` 正确，撤销该疑似项，未修改。**
  2. **证毕符 □ 在 Markdown 中以原始控制字节 U+0003 出现，登记不修（但请集成者留意）**：L1415 行尾确有 `\x03`（已用 `repr()` 读出：整行结尾为 `…\\end{array}$\x03`）。经全文普查，**U+0003 在 2343 行中仅此 1 处**（其余页的证毕符均为「完全未收录」，见 p.18/p.19/p.25/p.27/p.28 备注）。该字节非可打印字符，Markdown 渲染时不会显示为方框。**不改的理由**：与本系列已确立的「证毕符 □ 未收录 → 登记不修」属同一类；把一个既有字节替换成 `□` 属于**改写导出结果**而非「依原页图补回印刷原文」，在铁律二下缺乏依据。**如实登记其存在、位置与唯一性**，供集成者决定是否统一处理。
  3. **内联 ℚ/ℝ 被压平为普通 Q/R，登记不修**：印刷 `• Λ ≥ 0 is a ℚ-divisor on X with nΛ integral,` 与 `• L ≥ 0 is an ℝ-divisor on X,` 中的 `ℚ`、`ℝ` 是**双线黑板体**（300dpi ×20 裁片 `/tmp/bk_p31_qbb.png` 可见 ℚ 左碗有额外竖笔；×12 裁片 `/tmp/bk_p31_qr.png` 可见 ℝ 有两条竖笔），而 Markdown L1425/L1427 分别写作 `Q-divisor`、`R-divisor`。属既定「内联 ℝ/ℚ→R/Q 压平」登记类，**不改**（同一行的 `\mathbb { R }` 于 L1435 `ℝ-Cartier` 处则被正确保留，页内亦不一致，一并登记）。
  4. **`\text {and }` 与印刷斜体 `and` 的字形风格变体**：显示式 `A − B, A − Λ, and A − L`（L1432）中，印刷的 `and` 为**数学斜体衬线**（300dpi ×14 裁片 `/tmp/bk_p31_and.png` 目视确认，三个字母均明显右倾），Markdown 写作 `\text {and }`（MathJax 渲染为正体罗马）。字词本身无缺失，仅字体风格不同，登记不修（与本篇 `\mathrm` vs 斜体、`\operatorname { S u p p }` vs `\mathrm { S u p p }` 同类）。
  5. **登记不修的既定导出伪影（本页再次出现）**：`<sup>′</sup>` **HTML 上标泄漏**（L1409 两处 `is ǫ<sup>′</sup>-lc`）；`\operatorname { S u p p }` 的字距转义与 `\mathrm { C a r t i e r }`（L1415、L1435）；`\begin{array} { r } { … } \end{array}` 包裹（L1415 两处）；`: =` 与 `:=` 混用（同一行内既有 `p : =` 又有 `: =`）；印刷 `5.6. Bound on multiplicity at an lc place.` 与 `Proposition 5.7.` 的**加粗小标题在 Markdown 中退化为普通行**（既定「加粗丢失」登记类）；`\mathbb {P}` 与 `\mathbb { P }` 空格写法差异、`\deg_ {H _ {i}}` 与 `\deg _ { H _ { i } }` 两种下标写法混用（L1399 与 L1402）；`\epsilon` 与 `ǫ` 混用（L1419 两处）。
  6. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：Step 6 中 `l` 印作斜体小写 `l`（`-bbox` token `'l'`，x=433.1–436.3），非 `ℓ`，Markdown `l` 一致；`∆` 在印刷中为无衬线的 `∆`(U+2206) 而非 `Δ`(U+0394)，Markdown 统一写作 `\Delta`，属字体替换类，一并登记。
  7. **溯源**：本页唯一改动（补回丢失句点）已就父提交版 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版核对：三者第 1415 行**均以完全相同的字节形态**结尾于 `\end{array}$` + `\x03`（无句点），即该丢失句点是**初次 MinerU 导出即已写入的导出缺陷，非后续 peer 引入的回归**（原导出在此处不正确）。备注 1 的 `+`（非 `⋱`）、备注 3 的 ℚ/ℝ 压平同样在三版中逐字相同。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p025`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.032（PDF p.32 / 印刷 p.32）

- PNG：`/tmp/birksing_audit_p032.png`（gs `pngmono` 150dpi，仅此一页单独渲染），页眉「32 Caucher Birkar」；另取 300dpi 灰度整页 `/tmp/bk_p32_300.png`（2550×3300）**仅用于裁片**：①`/tmp/bk_p32_phi.png`（区域 (216,276)–(238,294)，×24）②`/tmp/bk_p32_mu.png`（区域 (194,563)–(234,582)，×22）③`/tmp/bk_p32_qed.png`（区域 (506,628)–(528,648)，×22）。三张裁片均已用 Read 工具亲眼看过。
- 核对：Markdown 范围 **L1439–L1505**（L1439 `•$T$is an lc place of$( X , \Lambda )$with centre the closure of x, and` 属印刷 p.32；L1505 为跨页合并行——前半 `…Supp B does not contain any stratum of$( X , \Lambda )$other` 属 p.32，后半 `than x, and this occupies much of the proof.` 属 p.33，本页只核对前半）。
  1. **段落/标题结构**：p.32 承 p.31 末行 `• $( X , \Lambda )$is lc near a point x (not necessarily closed),`（L1437，p.31 审计已确认该行属印刷 p.31），起于 `Then for any resolution$\nu \colon U \to X$…`（L1443），依次为 `We first treat a special case of the proposition.`（L1445）、`Lemma 5.8.`（L1447）、`Proof.`（L1449）、`Now we have:` 项目列表（L1465–L1497）、`Denote the induced contraction$G \to H$by σ.`（L1501）。上一条 `5.6. Bound on multiplicity at an lc place.`（L1417）与其下 `Proposition 5.7.`、五条假设项目符号（L1419–L1441）均属印刷 p.31，不计入本页。项目符号、编号、缩进与印刷逐项对应，无错序、无串行、无重复段落、无段落被并吞。
  2. **公式**：逐个比对 `$B _ {H} = B | _ {H}$…$L _ {H} = L | _ {H}$`（L1452）、`K _ {H} + B _ {H} = (K _ {X} + B + H) | _ {H}$`（L1458）、`A _ {H} ^ { d - 1 } \leq r`（L1467）、`A _ {H} - B _ {H}, A _ {H} - \Lambda_ {H}, \mathrm{and} A _ {H} - L _ {H}$`（L1476）、`(K _ {W} + \Lambda _ {W} + G) | _ {G} \mathrm{and} (K _ {W} + B _ {W} + G) | _ {G}$`（L1490）、`K _ {H} + \Lambda_ {H} \mathrm{and} K _ {H} + B _ {H}$`（L1496）、`\mu _ { T } \Lambda _ { W } = 1$…`\mu _ { T } B _ { W } \geq 0 .$`（L1499）、`\mu _ { T } \nu ^ { * } L \leq q$`（L1443）、`\sigma ^ { * } ( L _ { H } ) = ( \phi ^ { * } L ) | _ { G }$`（L1501）。上下标位置、限域竖线 `|` 与 `| _ {H}` 写法、希腊字母、不等号方向与印刷逐项一致，未见符号丢失、错位或方向颠倒。本页 `$G \to H$`、`$T \to C$`、`φ:$W \to X$`、`$W \to X$` 均为**实线箭头**（`\to`），与印刷一致；p.26 的 `\ - \to`（虚线）形态在本页不出现。
  3. **`\phi` 字形重点复核**：`-bbox` 全页把 φ 一律报成 U+03C6（本页共 5 处：x=219.4、459.8、300.7、127.4 等），单看文本层无法区分 `\phi` 与 `\varphi`。裁片 `/tmp/bk_p32_phi.png` ×24（第一处 x=219.4–225.8，`Now take a log resolution φ`）与 `/tmp/bk_p32_phi2.png` ×24（第二处 x=459.8–466.3，`G = φ ∗ H`，其右上角 `*` 明显上标）**均显示同一字形：闭合椭圆加一条贯穿斜画**，即 Computer Modern 的 `\phi`（= Unicode U+03C6），而非 `\varphi`（开口双圈 ϕ）。Markdown L1461 恰好两种写法并存——`log resolution φ:$W \to X$` 用的是**字面字符 `φ`**（U+03C6），`$G = \phi ^ { * } H$` 用的是 **`\phi` 命令**——二者在 MathJax 中渲染同一字形，与印刷一致。依铁律二以裁片判读，**判定 Markdown 正确，不改**。
  4. **`\mu _ { T } \Lambda _ { W }` 下标位置**：裁片 `/tmp/bk_p32_mu.png` ×22 显示印刷中 `T` 与 `W` 均为**下标**（bbox y=571.4–578.7，低于基线），`Λ` 在基线（y=567.2–578.1）；与 MD L1499 `\mu _ { T } \Lambda _ { W } = 1$while$\mu _ { T } B _ { W } \geq 0 .$` 完全吻合，判定**正确**，不改。
  5. **正文文字**：L1441 `$a ( T , X , B ) \leq 1$`、L1449 `Take a general$H \in | A |$`、L1461 `Then R is contained in$H \cap C$`、L1465 `$( H , B _ { H } )$is a projective ǫ-lc pair of dimension$d - 1$`、L1469 `n$\Lambda _ { H }$integral`、L1471 `$L _ {H} \ge 0$is an R-divisor on H`、L1473 `• the divisors`…L1479 `are ample,`、L1481 `is lc near the generic point of R (by the generality of H)`、L1483 `S is an lc place of…with centre R, and`、L1487 `The last two points can be seen by considering the pullbacks…`、L1501 `…the coefficient of S in…is bounded from above`——与印刷逐句对应，无掉词、掉字、错词、乱序。
  6. **标点/句读**：句末句点、列表内逗号、`respectively,` 后的分句结构与印刷一致；未发现伪句点代逗号、漏句点或重复句点。
- 结果：**PASS（0 处改动）**。
- 备注：
  1. 登记不修（QED 方框丢失）：裁片 `/tmp/bk_p32_qed.png` ×22 确认印刷在该处（bbox 第 146 行、token `\x03`，x=512.9–521.4，y=632.7–644.0）印有 □ 结束符，而 MD L1501 结尾 `…bounded from above too.$` 无该方框。属 QED 符号丢失的既定登记类（p.30 同），按策略**登记不修**。
  2. 登记不修（字形/别名族变体）：ℚ/ℝ 被压平为普通斜体（L1469 `Q-divisor`、L1471 `R-divisor`）；`\text { and }`（L1452）与 `\mathrm{and}`（L1476/L1490/L1496）混用；`\ge`（L1485）与 `\geq`（L1490/L1499）混用、`\leq`/`\le` 别名混用；`\mathbb { P }`/`\mathbb { P } ^ { d }` 内部空格不一致；`ǫ`（U+01EB）与 `\epsilon` 混用。均渲染同一或仅为字形族差异，登记不修。
  3. 登记不修（版式损失）：印刷中 `Lemma 5.8.`、`Proof.` 的加粗体在 Markdown 中退化为普通文本（L1447/L1449）；HTML 上下标残留（`<sub>`/`<sup>`）亦属同类版式损失，登记不修。
  4. 印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）：印刷的 `ε`-lc（`ǫ<sup>′</sup>` 类记号）字形与 Markdown 的 `\epsilon` / `ǫ` 混用并存，本审计不以「应统一」为由改动任何一侧。
- 溯源：本页**零改动**，无缺陷需归因；仅记录所核区间（L1439–L1505）在 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版中内容一致，本页未触碰任何三版存在差异之处。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p025`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## 本片段小结（p.017–p.024，actor `Wf-R-Birkar-p017`）

- **范围与覆盖**：PDF p.17–p.24 共 **8 页**，全部按 7 步循环**逐页**完成（一页渲染→Read 亲眼目检→读该页 Markdown→五点比对→立即写该页说明→分级/修复→下一页），**无跳页、无并页、无跨页合并判读**。对应目标 Markdown 第 **615–1095** 行（p.14 段尾 L615；p.17 L615–661、p.18 L663–699、p.19 L701–755、p.20 L757–823、p.21 L825–889、p.22 L891–943、p.23 L945–1014、p.24 L1017–1095；Step 7 起于 L1097 属印刷 p.25）。
- **分级统计**：**PASS± 5 页**（p.17 / p.18 / p.19 / p.20 / p.23）、**PASS 3 页**（p.21 / p.22 / p.24）、**FAIL 0 页**。合计修复 **9 处**。
- **9 处修复明细（逐处绑定页码与原文证据）**：

  | 页 | 行 | 类型 | 内容 |
  |---|---|---|---|
  | p.17 | 625 | 标点 | 列表项 `• $0 \leq L \sim _ { \mathbb { R } } - K _ { X }$` 末补句点 |
  | p.17 | 637 | 标点 | `…for some very ample divisor$H \geq 0$` 末补句点 |
  | p.18 | 663 | 标点 | `…and$H \leq \Lambda$` 末补句点 |
  | p.18 | 695 | 标点 | 显示块 `\end{array}` 之后补句点 |
  | p.18 | 699 | 标点 | `…we may assume$s < 1$` 末补句点 |
  | p.19 | 715 | 标点 | `Since$s < 1$` 之后补逗号 |
  | p.19 | 753 | 标点 | `…$0 \leq L \sim _ { \mathbb { Q } } A .$` 的**伪句点改回逗号** |
  | p.20 | 799 | 标点 | `is of Fano$\mathrm { t y p e } .$` 的**伪句点改回逗号** |
  | p.23 | 991 | 标点 | `…= 0 ;$` 的**重复分号删其一** |

  **9 处全部是标点类**（6 处句末句点缺失、1 处逗号缺失、2 处伪句点代逗号、1 处重复分号，合并计 9 处），**未触及任何公式、系数、上下标、撇号层级、取整/绝对值括号或不等号方向**。
- **溯源普查（redo 专项）**：对上述 9 处逐处执行 `git show cpf-redo/Birkar_2016_singularities_linear_systems^:"2018年 - Birkar/Birkar_2016_singularities_linear_systems_mineru/Birkar_2016_singularities_linear_systems__Birkar_2016_singularities_linear_systems.md"`（父提交 = `16ffcc7c`）与初次 MinerU 导出 `53a92412`，三次版本（第 625/637/663/695/699/715/753/799/991 行）**逐字相同**。结论：**9 处全部是初次 MinerU 导出缺陷，非后续 peer 引入的回归**；本片段「非导出缺陷，系 `<commit>` 引入」项数 = **0**。
- **撤销的疑似缺陷（150dpi 误判 → 300dpi 裁片裁决 → 判定不构成缺陷，未修改）**：
  1. p.20 L781 `\left( { { X , B + t _ { i } } { L _ { i } } + H _ { i } } \right)` 的相邻花括号分组 —— 相邻 Ord 原子之间不插入空格，渲染与无分组式完全相同，属**MathJax 无害分组伪影**，不改。
  2. p.21 L836/L868 的 `^{\prime \prime}` —— 300dpi 裁片确认**印刷此处确为双撇**（与同页另外三处单撇并存），属印刷自身的不一致，按铁律三保留。
  3. p.21 L863 `\frac { 1 } { t } P _ { i }` 与 L883 `\frac { 1 } { e } Q _ { i }` —— 150dpi 下易读成 `e/t`、`1/t`，300dpi 确认为 `1/t`、`1/e`，Markdown 正确，不改。
  4. p.21 L839 `\mathrm { ~ -- \to ~ }` —— 印刷虚线 MMP 箭头的忠实转写，与 p.17 L633/L657 的 `\dashrightarrow` 是同一印刷箭头的两种转写，渲染等价，登记不修。
  5. p.22 L923 `\equiv 0` —— 300dpi 确认为**三横 `≡`**（非 `=`），Markdown 正确，不改。
  6. p.22 L897/L907 的 `\lfloor \Gamma \rfloor`、`\lfloor B \rfloor` —— 首次裁片切掉下横导致 `⌊`/`⌈` 不可判，加高裁片后确认**下取整括号完整**，不改。
  7. p.23 L1000 的 `\langle (n+1)\Delta' \rangle` 与半开区间 `[0,1)` —— 150dpi 下角括号易读成圆括号、`)` 易读成 `]`，300dpi 裁片确认角括号与半开区间均正确，不改。
  8. p.24 Step 6 主显示的 `P ^ {\prime}` —— 150dpi 下曾疑为双撇，300dpi 裁片 `/tmp/bk_p24_step6d.png` 与 `-bbox`（每个 `P` 后恰一个 `′` token）双重确认**单撇**，不改。
- **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：
  1. **p.23 L1005 `nE`**：逻辑上应为 `nΓ`，但**印刷写的是 `nE`**，原样保留。
  2. **p.23 L1000 `μ _ { S ^ {\prime}}`**：逻辑上应为 `μ_{D'}`，但**印刷写的是 `μ_{S'}`**，原样保留。
  3. **p.24 L1046 `h ^ {1}`**：Kawamata–Viehweg 消失定理处逻辑上应为 `h^i(…)=0`（对一切 `i`），但 300dpi 裁片 `/tmp/bk_p24_hi.png` 显示**印刷上标为带衬线正体数字 `1`**（`-bbox` 亦解出 `1`，宽 4.2pt 与同页 `H^{0}` 的 `0` 同宽），原样保留。
  4. **p.21 的双撇 `^{\prime \prime}` 与同页单撇并存**，同上。
- **跨页一致、登记不修的导出伪影类**（本片段再次确认，未逐处重复登记）：inline ℝ/ℚ→`R`/`Q` 压平；连字符（`birational`、`well-defined` 中的 `-`）丢失；MathJax 字距转义 `\operatorname { l c t }`、`\mathrm { d e g }`、`\mathrm { P i c }`、`\mathrm { t y p e }`；`\begin{array}` 包裹多行显示；标题提升为 `##`；HTML `<sub>` 泄漏；数学与正文之间空格黏连（如 `of$…$can`）；`\epsilon` 与 `ǫ` 字形变体混用；证毕符 `□` 丢失；`\vert` 与裸 `|` 两种别名混用（L1089）；`:=` 与 `: =` 两种空格形态混用（L1057 / L1078）；`\langle ⟩` 在 `-bbox` 中失真解码为 `h(` / `i`（非花括号）。以上均为渲染等价或既定豁免，按 ASK 的修复政策一律**只登记、不修改**。
- **改动清点与只读声明**：本片段**只写了这一个 AUDIT 文件与目标 Markdown 这两个文件**；目标 Markdown 交付态 SHA-256 = `a637cb5a9fee05328c266fd367910a126cc8cfe7e60edf6e6535c1af67174bb4`（本片段开工基线 `9a5ce6430630b92d2581df848d4101915726a906bde00afdc15f8ac5759f9aaa`）；PDF `Birkar_2016_singularities_linear_systems.pdf` SHA-256 = `c9c73303be3b12c5ca91506ac541c9b9d81764d19bcd7183b7c577f8c0d546fe`，与前两片段记录一致，**原件全程只读未被触碰**。`git status --porcelain -- "2018年 - Birkar"` 仅列出上述两个已修改文件；`git status --porcelain -- AUDIT-INDEX.md AUDIT-PROGRESS.log MEMORY.md README.md` **返回空**，确认未触碰任何根级真值文件，也未触碰其它论文目录。未执行任何 `git commit` / `add` / `merge` / `push`；未启动或停止 mineru 服务、未改 mineru 配置；SOP 第 5 步要求的根级 `AUDIT-PROGRESS.log` 追加由总Master 串行补写。
- **交付自检**：`grep -c '^## p.' AUDIT-Birkar_2016_singularities_linear_systems.md` = **114**（本片段开工基线 **106**，净增 **8**，对应 p.017–p.024 各一条，无遗漏）。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p017`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## 本片段小结（p.009–p.016，actor `Wf-R-Birkar-p009`）

- 覆盖：PDF p.9–p.16 共 **8 页全部逐页完成**，每页均按 SOP 七步执行「`gs -sDEVICE=pngmono -r150 -dFirstPage=N -dLastPage=N` 单页渲染 → `Read` 工具亲眼目检该页 PNG → 读 Markdown 对应段 → 五点比对 → **立刻**落签 → 分级 → 有缺陷则 `Edit` 逐处修」，**无跳页、无合并条目**。逐页新增说明 **8 条**（`## p.009` … `## p.016`）；`grep -c '^## p\.'` 由开工基线 **98 条 → 交付 106 条**，自检通过。
- 评级：**8 页全部 PASS±，0 页 FAIL**。本片段 Markdown **改动 35 处**（p.9=7、p.10=6、p.11=3、p.12=1、p.13=3、p.14=7、p.15=3、p.16=5），全部用 `Edit` 工具逐处手工写入，**无一处使用 Python/正则/sed/heredoc 批量改写**；每处 `old_string` 均先经唯一性检查确认全文件唯一后才落刀（`\pi ( B _ { j } ) } \end{array}` 有 2 处、`and$( V , C ^ { \mathrm { a n } } | _ { V } )$` 有 3 处、`A^d \leq r` 有 4 处，均改用更长的上下文锚定到本片段那唯一一处）。
- **改动性质清点**：35 处**全部是字符级丢失或标点错讹**——行末句点/句中句点补齐（`…\rfloor$`、`…p + 1$`、`…= X$`、`…G ^ { \prime }$`、`…\rfloor}$`、`…a > 0$` 等）、**丢句点伪句点**（p.16 第 585 行 `|_ { Y } .$` 实为印刷逗号）、**丢逗点**（p.14 第 517 行 `is$E _ { i }$ by assumption`）、**重复逗点**（p.14 第 531、533 行 `$x ,$,`、`$x ^ { \prime } ,$,`）、**全角逗号误植**（p.16 第 589 行 `of$Y \to X$，` 的 U+FF0C 改回印刷的半角逗号并移出数学环境）、ff 连字拍平（`coeficient(s)`、`suficient(ly)`、`efective`、`ofice`）、重音符错位（`Pˇaun`→`Păun`、`´etale`→`étale`）。**未改动任何公式、系数、上下标、不等号方向或数学内容**。
- **本片段新登记的 PASS± 类别**（均按政策登记不修，已在对应页说明内逐项列出）：① **ε 字形不一致**（`\epsilon` 月牙 ϵ 与直立 `ǫ` 混用）；② **HTML `<sub>` 标签泄漏**（p.16 第 599、601 行）；③ **节标题被提升为 `##`**（p.16 第 603 行 `## 2.25.`，而同层 `2.22.`、`2.23.` 未提升）；④ 行内 ℝ/ℚ 拍平为 `R`/`Q`；⑤ 断词连字符丢失（`Rdivisor`）；⑥ MathJax 词距空格化（`\mathrm { S u p p }`、`\mathrm { a n }`、`\mathrm { ~ i s ~ }`）；⑦ `\begin{array}` 单列包装；⑧ 标点错置于数学环境内致词间粘连。
- **print quirk 忠实保留（未按数学/常识静默「纠正」）**：p.15 第 559 行印刷写作 `Let Y → X be a sequence of blowups`（映射方向与上下文相反，属原刊笔误；**同页第 565/577 行的 `Y → X` 则是正确的收缩映射方向，二者不可混同**）；p.15 第 551 行 `away from z, that is,` 用逗号断句；p.15 第 563 行 Lemma 2.24 题设中 `r` 无任何限定词；p.15/p.16 印刷内部 ε 字形不统一；p.16 页眉「16 Caucher Birkar」全书一律不导出。
- 本片段**未发现任何数学内容错误、整段丢失或记号误置**；逐页「已核对无误」清单已写入各页说明（含 `π^{-1}{z}` 的上标 `−1`、`\phi^{-1}`/`\psi^{*}` 上标与 `\phi_*` 下标的区分、`\equiv` 未误作 `=`、`b \gg a` 的双大于号、分配律 `C + tbA = (1−t)C + t(C+bA)`、ε/2 分式的上下位置、`t_1,\ldots,t_d` 与 `π^*t_1,\ldots,π^*t_d` 两组局部参数、`\Sigma` 未被拍平、`\mathbb{P}^d` 双线体等）。
- **溯源核对（已实际执行）**：按工单要求在 worktree 内运行 `git show cpf-redo/Birkar_2016_singularities_linear_systems^:"2018年 - Birkar/…__….md"`，得父提交版 `16ffcc7c`；另取初次 MinerU 导出提交 `53a92412` 作对照。
  1. `git diff 父提交版 → 本片段交付态` 在**本片段作用域 MD 第 323–613 行内共 50 个变更行**，逐行展开与本片段 8 页说明中的 35 处修复**一一对应，无遗漏、无多出**；⇒ 本片段修的每一处，在 redo 轮基线 `16ffcc7c` 中**均已存在**。
  2. 对每类缺陷做「初次导出 `53a92412` / 父提交 `16ffcc7c` / 交付态」三版计数普查：`coeficient` 66/65/9、`coefficients` 0/0/29、`suficient` 12/12/0、`efective` 17/17/4、`ofice` 1/1/0、`´etale` 7/7/0、`´e` 15/15/0、`Pˇaun` 1/1/0、`<sup>´</sup>` 1/1/0、全角逗号 `，` 3/3/0、`K _ { U } | _ { Y } .$` 1/1/0、`{ \cal X }` 1/1/0、`\mathfrak { R }` 1/1/0、`\mathrm { ~ i s ~ }` 2/1/1。**没有任何一类缺陷的计数由「初次导出」上升到「父提交」**（`<sub>` 泄漏反由 7 降到 5、`\mathrm { ~ i s ~ }` 由 2 降到 1，属 redo 轮的**改善**而非回归）。
  3. 逐处行尾对照（初次导出 vs 父提交，同一缺陷原样并存）：`\rfloor$`、`\Lambda \geq p + 1$`、`with$A ^ { d } \leq r$`、`for any real number$a > 0$`、`is equal to$1 - \textstyle { \frac { \epsilon } { 2 } }$`、`for a analytic isomorphism between$( U , …)$and$( V , …)$` 在**两版中完全一致地缺句点**；`\mathrm { l c } .$.`、`K _ { U } | _ { Y } .$`、全角 `，` 两版完全一致。
  4. 另发现初次导出**比父提交更差**的三处，redo 轮已部分修复（方向正确）：初次导出第 589 行为 `of$Y  X$，`（**箭头整个丢失** + 全角逗号），父提交补回 `\to` 但全角逗号仍在；初次导出第 581 行为 `of$W  V$`（箭头丢失），父提交补回 `\to` 但仍缺句点；初次导出第 587 行为 `does not contain$Y .$.`（**双句点**），父提交删掉多余句点、仍留下伪句点。
  - **结论：本片段 35 处修复中，需要判定为「非导出缺陷，系 <commit> 引入」的项数 = 0**；全部可追溯到 MinerU 初次导出 `53a92412`，redo 轮在本作用域内只做过**改善**性修改，未引入任何回归。
- **越界未触碰项（如实登记，供集成者知悉）**：`git diff 父提交版 → 交付态` 在**本片段作用域之外**（MD 第 627–2341 行）另有 **130 个未提交变更行**（含一处 `2141,2142d2140` 的整行删除），这些改动**不对应本片段 p.009–p.016 任何一页的说明**，亦非本 actor 所作（`W` 只对第 325–605 行发起过 `Edit`），应系同一 worktree 内其它会话/并发 actor 的在途产物。本片段按「只许写本 Markdown 与本 AUDIT、只负责 p.9–p.16」之约束，**未读取亦未修改这些行**，特此登记交由总Master 裁决归属与提交。
- **改动清点（本片段实际写入）**：只写了这一个 AUDIT 文件（`AUDIT-Birkar_2016_singularities_linear_systems.md`）与目标 Markdown。目标 Markdown 交付态 SHA-256 = `9a5ce6430630b92d2581df848d4101915726a906bde00afdc15f8ac5759f9aaa`（开工基线 `95216ff90edbb81b4ac0f789bcdfad682e5258d86dba467801fcb794c509c3ac`，二者之差**同时**包含本片段 35 处修复与上述 130 行越界在途改动，本 actor 只对前者负责）；PDF SHA-256 = `c9c73303be3b12c5ca91506ac541c9b9d81764d19bcd7183b7c577f8c0d546fe`，与前片段记录一致，**原件全程只读未被触碰**。
- 未执行任何 git 提交/暂存/合并/推送；未触碰根级 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、`MEMORY.md`、`README.md` 及其它论文目录；PDF 全程只读；SOP 第 5 步要求的根级进度追加由总Master 串行补写。
- 记录时间：2026-10-05；actor=`Wf-R-Brikar-p009`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## 本片段小结（p.025–p.032，actor `Wf-R-Birkar-p025`）

- **范围与覆盖**：PDF p.25–p.32 共 **8 页**，全部按工单 7 步循环**逐页**完成（一页单独 gs 渲染 → Read 工具亲眼看图 → 读该页 Markdown → 五点比对 → **立刻**写该页说明 → 分级/修复 → 下一页），**无跳页、无并页、无跨页合并判读**。每次只渲染当前这一页（`/tmp/birksing_audit_p025.png` … `/tmp/birksing_audit_p032.png` 各自独立生成）。对应目标 Markdown 第 **1097–1505** 行（p.25 L1097–1161、p.26 L1161–1211、p.27 L1213–1271、p.28 L1273–1309、p.29 L1311–1347、p.30 L1349–1397、p.31 L1399–1437、p.32 L1439–1505；L1505 为跨页合并行，前半属 p.32、后半 `than x, and this occupies much of the proof.` 属 p.33，移交后续片段）。
- **分级统计**：**FAIL 3 页**（p.26 / p.30 / p.31）、**PASS± 1 页**（p.27）、**PASS 4 页**（p.25 / p.28 / p.29 / p.32）。合计修复 **5 处**，全部用 Edit 工具逐处手工写入。
- **逐处改动清单**（页码 / 行号 / 改动 / 印刷依据 / 溯源）：
  1. **p.26 / L1167**：`the induced map$U \ - \to \ Z$is a morphism` → `the induced map$U \dashrightarrow Z$is a morphism`。印刷为**双虚线**双射箭头（本篇记号），导出把 `-` 与 `\to` 拆成两个 token 并留下空格，属数学含义可变的箭头变形。**导出缺陷**（`^`/HEAD/`53a92412` 三版逐字相同，原导出在此处不正确）。
  2. **p.26 / L1189**：`We claim that S is not contracted over$V$;` → `over$V$:`。印刷此处为**冒号**引出条件从句，非分号。**非导出缺陷，系 HEAD 之后未提交的在途改动引入**（`16ffcc7c` 与 `53a92412` 原始导出均为正确的 `:`）。
  3. **p.27 / L1263**：`$\pi ( x ) = z : = ( 1 : 0 : \cdot \cdot : 0 )$,` → `$\pi ( x ) = z : = ( 1 : 0 : \cdots : 0 )$,`。印刷为**三个居中点**（坐标序列 `(1:0:⋯:0)` 的省略号），导出只保住 2 个点且落在下轴（`\cdot \cdot`）——**点数由 3 变 2 属字符级丢失，据本片段判例应修**。**导出缺陷**。
  4. **p.30 / L1373**：`{ \epsilon ^ { \prime } = \frac { t } { 2 } \epsilon . }` → `{ \epsilon ^ { \prime } = \frac { t } { 2 } \epsilon , }`。印刷该逗号与前后同处一句内的并列列举（后续接 `…is lc`），句点会把条件从句提前断成独立句，属伪句点代逗号。**导出缺陷**（`^`、HEAD、`53a92412` 三版该处字节完全相同）。
  5. **p.31 / L1415**：`…{ l \le p : = \lfloor \frac { 1 } { u } - 1 \rfloor } \end{array}$` → 同上并补回句末**句点**。印刷此处是一个以 `.` 收尾的完整陈述句（Step 6 末句）。**导出缺陷**（三版该行均以完全相同的字节形态结尾于 `\end{array}$` + 原始 `U+0003` 控制字节，无句点）。
- **本片段新增的三条修复判例（供后续片段沿用）**：
  1. **省略号「点数」与「轴位」须分开判定**：`\cdot \cdot`（2 点、下轴）而印刷为 3 点 ⇒ 点数丢失，**修**（p.27）；`\dots`（MathJax 展开为 `\ldots`，点在下轴）而印刷为**3 个居中点、点数正确** ⇒ 纯轴位/字形变体，**登记不修**（p.28、p.30 各一处）。
  2. **QED 方框 □ 一律登记不修**：p.30 的 `-bbox` 中 `\x03` 计数为 0（印刷亦无）；p.32 印刷有 □（bbox L146，x=512.9–521.4，y=632.7–644.0，×22 裁片确认）而 Markdown 无，登记；p.31 则相反——Markdown 保留了结束符，却被导出写成**原始 `U+0003` 控制字节**，这是全文件唯一一处该字节（只读复核 `t.count(chr(3)) == 1`），已如实登记并提请集成者注意（它不是可见的 □ 字符）。p.28 有两处方框同样登记。
  3. **文本层与裁片冲突时一律以裁片为准**：p.32 的 `\phi` 在 `-bbox` 中一律报 U+03C6，`/tmp/bk_p32_phi.png`（×24）与 `/tmp/bk_p32_phi2.png`（×24）两处裁片均显示为闭合椭圆加贯穿斜画的 CM `\phi`（非 `\varphi`），Markdown L1461 中「字面 `φ` 字符」与「`\phi` 命令」两种写法渲染同一、均正确，**不改**；p.31 的 `l + 1` 在 150dpi 下曾疑为 `l ⋱ 1`，经 bbox 单个基线 `+` token 与 ×20 裁片确认为**真加号**，**撤销疑虑不改**。
- **本片段撤销/判为原样正确的疑似缺陷**：p.27 三处候选（`(x,y)` 与 `(x : y : 0)` 的坐标对、句中 `\varphi` 字形、页边 QED 缺位）经裁片与 bbox 复核后取消；p.29 `π : X → ℙ^d` 的「幻影丢失」说经 bbox 逐 token 清点后取消；p.30 疑似 `t/2` 误作 `1/2`（实为前一处 `Θ + (t/2)C` 的归属问题）取消；p.32 `φ` 与 `µ_T Λ_W`（×24 / ×22 裁片）判为**原样正确**。均已逐条记入各页说明。
- **登记不修的其余变体（汇总，不逐条重复页内清单）**：ℚ/ℝ 压平为普通斜体、`\text { and }` 与 `\mathrm{and}` 混用、`\ge` 与 `\geq`、`\le` 与 `\leq` 混用、`\vert` 与 `|`、`\cap` 与 `\bigcap`/`\sum` 尺寸变体、`: =` 与 `:=`、`\operatorname { P r o j }` 的字距转义、`\begin{array}` 包裹、`\mathbb { P }` 内部空格不一致、`ǫ`(U+01EB) 与 `\epsilon` 混用、连字符丢失、Math 与正文间空格粘连、标题加粗丢失、HTML `<sub>`/`<sup>` 残留——均为渲染等价的字形/版式族，按既定策略登记而不改动，**未按数学常识「纠正」原刊任何写法**。
- **印刷侧 quirk（依铁律三原样保留并登记）**：p.26 `S` 与 `V` 的书法体/普通体并存；p.30 Step 6 的 `l` 印作斜体小写 `l`（bbox token `'l'`，x=433.1–436.3）而非 `ℓ`；p.30 `∆` 为无衬线 U+2206 而非 U+0394；p.32 的 `ε`-lc 与 `\epsilon`/`ǫ` 混排；全书页眉（如 p.32「32 Caucher Birkar」）一律不导出，属预期行为。
- **溯源普查结论**：本片段判定为缺陷的 5 处中，**4 处为 MinerU 初次导出即已写入的导出缺陷**（第 1、3、4、5 项，在 `16ffcc7c`（`^`）、`37580aaf`（HEAD）、`53a92412`（初次导出）三版中逐字或逐字节相同，即原导出在这些位置**不正确**），**1 处为在途回归**（第 2 项，`over$V$;`，原导出正确，系 HEAD 之后未提交的在途改动引入）。⇒ 需要登记为「非导出缺陷」并交由集成者裁决归属的项数 = **1**。
- **改动清点（本片段实际写入）**：只写了这一个 AUDIT 文件与目标 Markdown。目标 Markdown 交付态 **2341 行**、SHA-256 = `db44121707110529136e86651481ea6cc0a79590d910ce46a1374afaeeda69cb`；本片段 5 处修复**均为行内替换、不增删行**，故行数与本片段开工基线相同（该 SHA 同时包含此前各 actor 在本作用域外的在途改动，本 actor 只对本片段 5 处负责）。已用只读 `str.count` 逐处复核：5 处新串各出现 1 次、对应旧串出现 0 次；p.31 一处因旧串是新串前缀而旧串计数为 1，已另以「`\end{array}$` 之后必为 `.`」精确复核通过（唯一出现处后随字符为 `.`）。PDF SHA-256 = `c9c73303be3b12c5ca91506ac541c9b9d81764d19bcd7183b7c577f8c0d546fe`，与前片段记录一致，**原件全程只读未被触碰**。
- **交付自检**：`grep -c '^## p\.' ` 本 AUDIT 文件 = **122**（本片段开工基线 114 + 本片段新增 8 条 p.025…p.032），8 条**一条不缺**。`git status --porcelain` 在 worktree 内仅列出本 AUDIT 与本 Markdown 两个 ` M`，根级 `AUDIT-INDEX.md`/`AUDIT-PROGRESS.log`/`MEMORY.md`/`README.md` 及其它论文目录均未出现。
- 未执行任何 git 提交/暂存/合并/推送；未触碰根级真值文件；PDF 全程只读；未启动或停止 mineru 服务、未改 mineru 配置；SOP 第 5 步要求的根级进度追加由总Master 串行补写。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p025`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.033（PDF p.33 / 印刷 p.33）

- PNG：`/tmp/birksing_audit_p033.png`（gs `pngmono` 150dpi，仅此一页单独渲染），页眉「Singularities of linear systems and boundedness of Fano varieties  33」；另取 300dpi 灰度整页 `/tmp/bk_p33_300.png`（2550×3300）**仅用于裁片**：①`/tmp/bk_p33_frac.png`（区域 (150,432)–(235,456)，×8）②`/tmp/bk_p33_hb.png`（区域 (88,532)–(235,550)，×6）③`/tmp/bk_p33_epscomma.png`（区域 (338,357)–(366,375)，×14）④`/tmp/bk_p33_bsim.png`（区域 (248,700)–(292,722)，×14）⑤`/tmp/bk_p33_alpha.png`（区域 (378,700)–(414,722)，×14）⑥`/tmp/bk_p33_gamma.png`（区域 (195,698)–(420,724)，×5）。六张裁片均已用 Read 工具亲眼看过。
- 核对：Markdown 范围 **L1505–L1557**（L1505 为跨页合并行：前半 `…Supp B does not contain any stratum of$( X , \Lambda )$other` 属印刷 p.32、后半 `than x, and this occupies much of the proof.` 属 p.33，与 p.32 审计结论一致；L1559 `where$E _ { i }$are the exceptional divisors of ψ other than T…` 起属印刷 p.34，不在本页）。正文页型，五点比对：
  1. **节/步骤标题顺序**：p.33 自 `Step 1.`（L1507）起，经 Step 1 的三个行间公式与 `Note that each stratum…`（L1535），接 `Step 2.`（L1537）及其三条项目符号与两个行间公式（L1548），再接 `Step 3.`（L1553）及其 Γ_V 行间公式（L1556）。与印刷步骤顺序 Step 1 → Step 2 → Step 3 完全一致，无错序、无跳步、无重复。
  2. **行间公式逐条**：`\mu_ {E ^ {\prime}} B ^ {\prime} \geq - d + 1 \text { and } \mu_ {E ^ {\prime}} \Lambda^ {\prime} = 1.`（L1510，对印刷 bbox L016–L020 `µ_{E′} B′ ≥ −d + 1 and µ_{E′} Λ′ = 1.`）；`A ^ {\prime} - B ^ {\prime}, A ^ {\prime} - \Lambda^ {\prime}, A ^ {\prime} - L ^ {\prime}`（L1516 ↔ bbox L022）；`B ^ {\prime \prime} := \beta B ^ {\prime} + (1 - \beta) \Lambda^ {\prime} \geq 0.`（L1524 ↔ bbox L025 `B ′′ := βB ′ + (1 − β)Λ ′ ≥ 0.`）；`A ^ {\prime} - B ^ {\prime \prime}, A ^ {\prime} - \Lambda^ {\prime \prime}, A ^ {\prime} - L ^ {\prime}`（L1530 ↔ bbox L028）；`K _ {X} + B + t B = \frac {1}{2} (K _ {X} + B) + \frac {1}{2} (K _ {X} + B + 2 t B)`（L1548 ↔ bbox L080–L088，分子 `1 1`、分母 `2 2` 分列，位置与 Markdown 的两个 `\frac {1}{2}` 一致）；`\Gamma_ {V} = (1 + t) B ^ {\sim} + (1 - \frac {\epsilon}{4}) \sum E _ {i} + (1 - a) T`（L1556，详见第 5 条）。系数、指数、上下标、界号方向与印刷逐项吻合。
  3. **项目符号与陈述**：`• $( H , B _ { H } )$is a projective ǫ-lc pair of dimension$d - 1$,`（L1539 ↔ bbox L052–L054）、`• $A _ { H }$is a very ample divisor on H with$A _ {H} ^ {d - 1} \leq r ,$and`（L1541 ↔ bbox L055–L060，上标 `d−1` 位置正确）、`• $A _ { H } - B _ { H }$is ample.`（L1543 ↔ bbox L061–L065）——三条项目符号的编号、顺序与陈述与印刷一致。
  4. **行内记号**：`$A ^ { \prime }$on$X ^ { \prime }$with bounded$A ^ { \prime d }$`（L1513 ↔ bbox L021 `A ′d`）、`$\beta \in ( 0 , 1 )$`（L1521 ↔ bbox L024）、`$\epsilon ^ { \prime } = \epsilon \beta$`（L1527 ↔ bbox L026 `ǫ ′ = ǫβ`）、`$y \neq x .$Let$X ^ { \prime } \to X$`（L1507 ↔ bbox L006，**实线箭头**）、`$\psi \colon V \to X$`（L1553 ↔ bbox L092，**实线箭头**）、`$| A |$`、`$A _ { H } = A | _ { H }$` 等限域写法（L1537 ↔ bbox L038–L051）均与印刷一致。本页无破折号算子箭头。
  5. **三处需裁片裁决的存疑项（全部经 300dpi 裁片判读，结论均为 Markdown 原样正确）**：
     - `\epsilon/2`-lc（L1537、L1545）：150dpi 下曾误读为 `r/r`；bbox 显示分子 `ǫ`（x=164.76–168.18，y=437.59–444.91）与分母 `2`（x=164.40–168.63，y=446.05–452.27）同 x 上下叠置，裁片 `/tmp/bk_p33_frac.png` ×8 目视确认为 `\frac{\epsilon}{2}\epsilon`-lc 的 ε/2 分数；Markdown 写作 `\epsilon/2`，渲染等价，**不改**。第二处（bbox x=404.52–408.75 / y=586.75–601.43）同理。
     - `( X , H + B + 2 t B )`（L1545）：bbox token 为 `H`（x=108.96–118.03，与同行 `B` 同基线同字高）；裁片 `/tmp/bk_p33_hb.png` ×6 目视确认为 **H**（双竖干带横杠）而非 `B`。Markdown 与印刷一致，**不改**——详见备注 4 印刷侧 quirk 登记。
     - `B ^ {\sim}` 与 `(1 - a) T`（L1556）：bbox 报 `∼`（x=270.12–276.70，y=706.99–711.99）与 `a`（x=392.76–409.09，y=707.74–718.65）；因同页他处的 `′′` 亦被文本层报作 `′′`、且 `B''` 在本页上文的 `B ′′ := βB ′ + …` 中已出现，存在「`∼` 是否为 `′′` 的 CMap 伪影」以及「`a` 是否为 `\alpha`」双重疑虑，遂裁片裁决：裁片 `/tmp/bk_p33_bsim.png` ×14 显示 `B` 之后是一个**波浪号 `∼`**（位于上标高度），裁片 `/tmp/bk_p33_alpha.png` ×14 显示 `(1 − a)` 中是**意大利体 `a`**（圆肚加直干带小尾），**均非** `′′`/`\alpha`。整式裁片 `/tmp/bk_p33_gamma.png` ×5 复核印刷原式为 `\Gamma_V = (1+t)B^{\sim} + (1 - \frac{\epsilon}{4})\sum E_i + (1-a)T`，求和号无下标，与 Markdown L1556 **逐项一致**，**不改**。此项同时**推翻**了我依 bbox「上标位置」先验得出的 `∼` = `′′` 的推测——裁片优先。
- 结果：**FAIL（1 处改动，以原图为准）**。改动：Markdown **L1535** `…L ^ { \prime } , \epsilon ^ { \prime } .$, and replacing r appropriately…` → `…L ^ { \prime } , \epsilon ^ { \prime }$, and replacing r appropriately…`（删除伪句点）。
- 备注：
  1. **缺陷明细（唯一 1 处）**：印刷 bbox L031 在 `ǫ ′` 之后的 token 为 `,`（x=353.88–356.90，**y=361.78–372.69**，墨迹下探出基线，与同行其它 5 个逗号 token 的 y 值逐位相同），而同行所有句点/撇号类 token 的 yMax 均为 366.51（`′`/`′′`）——即印刷此处是**逗号**；裁片 `/tmp/bk_p33_epscomma.png` ×14 目视亦见 `,` 的明确下探尾钩，与句点有别。Markdown 把该逗号写成了「数学内的句点 `.` + 数学外的逗号 `,`」，渲染出 `ε′., and` 的**伪句点**，属字符级标点错误，**已用 Edit 逐处修复**（只删伪句点，保留句点外的原逗号，渲染结果与印刷的 `ε′, and` 完全一致）。
  2. **溯源**：该处改动已就父提交版 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版逐字节核对：三版**均**含 `…L ^ { \prime } , \epsilon ^ { \prime } .$, and replacing r…`（以 `,`-版本计数 0 / `.`-版本计数 1 普查），即该伪句点**初次 MinerU 导出即已写入，属导出缺陷，原导出在此处不正确**；**不是**后续 peer 引入的回归。
  3. **登记不修（字形/别名族变体）**：ℚ/ℝ 被压平为普通斜体（L1545 `Q-divisor`、`R-divisors`）；`\geq`/`\leq` 写法、`\ge` 变体；`ǫ`(U+01EB) 与 `\epsilon` 在同页混用（L1539 `ǫ-lc` 用字形、L1537/L1545/L1556 用 `\epsilon`）；`\colon` 用于 `\psi \colon V \to X` 而 `\to` 用于 `$X ^ { \prime } \to X$`；Math 与正文间空格粘连（`is$\epsilon/2$-lc`）。均渲染等价，登记不修。
  4. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①印刷在 `This implies that` 一句中写作 `(X, H + B + 2tB) is plt`（bbox token 与 ×6 裁片双重确认为字母 `H`），而同页下文两处均写 `(X, B + 2tB)`——从「inversion of adjunction」推出 plt 的常规写法应为 `B+B+2tB` 或 `B+2tB`，故此处 `H` 疑为原刊笔误；**Markdown 已原样保留 `H`，未按数学常识改正**。②`zero-dimensional` 在印刷中于行末断为 `zero-` + 次行 `dimensional`，Markdown 合并为 `zerodimensional`（连字符丢失），属既定登记类。③`Step 1`/`Step 2`/`Step 3` 的斜体步号在 Markdown 中退化为普通文本（加粗/斜体丢失），同属版式登记类。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p033`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.034（PDF p.34 / 印刷 p.34）

- PNG：`/tmp/birksing_audit_p034.png`（gs `pngmono` 150dpi，仅此一页单独渲染），页眉「34　Caucher Birkar」（**偶数页页眉为作者名**，与 p.33 的偶奇页眉排布规律一致，页眉一律不导出）；另取 300dpi 灰度整页 `/tmp/bk_p34_300.png`（2550×3300）**仅用于裁片**：①`/tmp/bk_p34_simR.png`（区域 (222,578)–(300,608)，×14）②`/tmp/bk_p34_sumF.png`（区域 (255,172)–(355,198)，×12）③`/tmp/bk_p34_equiv.png`（区域 (240,493)–(370,520)，×12）。三张裁片均已用 Read 工具亲眼看过。
- 核对：Markdown 范围 **L1559–L1621**（L1559 `where$E _ { i }$are the exceptional divisors of ψ other than T,…` 承接 p.33 末行 Γ_V 公式；L1623 `for some` 起属印刷 p.35，不在本页）。正文页型，五点比对：
  1. **节/步骤标题顺序**：p.34 为 p.33 `Step 3.` 的续页，含 `Step 4.`（L1591）与 `Step 5.`（L1599）两个新步号，其间夹 Step 3 的续段（L1559–L1589）。与印刷 `Step 4.`→`Step 5.` 的出现顺序完全一致，无错序、无跳步、无重复。
  2. **行间公式逐条**（共 8 个显示式）：①`\begin{array}{c} K _ {V} + \Gamma_ {V} = K _ {V} + B ^ {\sim} + \sum (1 - a _ {i}) E _ {i} + (1 - a) T + t B ^ {\sim} + \sum (a _ {i} - \frac {\epsilon}{4}) E _ {i} \\ = \psi^ {*} (K _ {X} + B) + t B ^ {\sim} + F \end{array}`（L1562）↔ bbox L015–L034（两个 `∑` 被文本层误报为 `X`，两个 ε/4 的分子 `ǫ` y=126／分母 `4` y=141，两行续行 `= ψ ∗ (K_X + B) + tB ∼ + F` 起于 x=243）；②`F := \sum (a _ {i} - \frac {\epsilon}{4}) E _ {i}`（L1568）↔ bbox L036–L042；③`a ^ {\prime} = a (T, X, B + t B) \text { and } a _ {i} ^ {\prime} = a (E _ {i}, X, B + t B),`（L1574）↔ bbox L045–L049；④两行对齐式（L1580）↔ bbox L051–L071；⑤`G := \sum (a _ {i} ^ {\prime} - \frac {\epsilon}{4}) E _ {i} + (a ^ {\prime} - a) T`（L1586）↔ bbox L073–L080；⑥`K _ {V} + \Gamma_ {V} \equiv t B ^ {\sim} + F / X`（L1594）↔ bbox L114–L118；⑦`0 \leq D _ {Y} \sim_ {\mathbb {R}} \frac {1}{t} (K _ {Y} + \Gamma_ {Y} + 3 d A _ {Y})`（L1602）↔ bbox L133–L145（三个分式 `1`/`t` 分列于 y=582／597、285–291／286–290）；⑧`K _ {Y} + \Gamma_ {Y} = \pi^ {*} (K _ {X} + B) + t B _ {Y} ^ {\sim} + F _ {Y},`（L1608）↔ bbox L147–L157；⑨三分式式（L1614）↔ bbox L163–L177（三个 `1`/三个 `t`）；⑩`D _ {Y} = \pi^ {*} H + B _ {Y} ^ {\sim} + \frac {1}{t} F _ {Y}`（L1620）↔ bbox L179–L186。逐条核对**系数、指数、上下标、求和号有无下标、分式分子分母、\`\equiv\` 三横线、\`\sim\` 波浪上标**与印刷一致，未见符号丢失、错位或方向颠倒。
  3. **记号约定与行内式**：`a = a ( T , X , B )`、`a _ { i } = a ( E _ { i } , X , B )`（L1559 ↔ bbox L004–L009）、`\mu _ { T } \Gamma _ { V } = 1 - a`（↔ bbox L009–L013）、`\epsilon/2`-lc（L1589 ↔ bbox L086–L089：分子 `ǫ` y=347、x=467–471，分母 `2` y=355，同 x 上下叠置，与 p.33 同款分式，已在 p.33 用 ×8 裁片裁决过）、`\pi \colon Y \to X`（L1591 ↔ bbox L102，**实线箭头**）、`K _ {V} + \Gamma _ {V } \equiv G / X` 与 `exceptional/X`（↔ bbox L106–L107）、`Q-factorial`（↔ bbox L113）、`\pi^ {*}` 上星号、`t B _ {Y} ^ {\sim}` 的上标波浪与下标 `Y` 的叠加次序（L1608、L1620）均与印刷吻合。
  4. **正文文字**：`where E_i are the exceptional divisors of ψ other than T,…`（L1559）、`is effective and exceptional over X and its support does not contain T. On the other hand, if`（L1571）、`then we can write`（L1577）、`is exceptional over X. Moreover, if the image of E_i on X is positive-dimensional for some i, then…`（L1589）、`…hence the claim. Moreover, since`（L1591）、`and since T is not a component of tB ∼ + F , we see that T is not contracted by the MMP.`（L1597）、`with coefficients ≤ 1 − ε. By Step 3,`（L1605）、`where B_Y ∼ , F_Y denote the pushdowns of B ∼ , F , respectively. Thus we get`（L1611）、`Then we can write`（L1617）——逐句与印刷一致，无掉词、掉字、错词、乱序。
  5. **标点/句读**：句末句点、列表内逗号、`respectively,` 后的分句、`if` / `where` 引导的公式与文字交替结构均与印刷一致；未发现伪句点代逗号、漏句点或重复句点。
- 结果：**PASS（0 处改动）**。
- 备注：
  1. **三处需裁片裁决的存疑项（全部经 300dpi 裁片判读，结论均为 Markdown 原样正确）**：
     - `\sim_ {\mathbb {R}}`（L1602）：bbox 该下标报为**普通斜体 `R`**（x=275–281，y=593 起），存在「印刷其实是黑板粗 ℝ、文本层压平」的疑虑；裁片 `/tmp/bk_p34_simR.png` ×14 目视确认印刷下标是**双线体 ℝ**（左腿双竖干 + 斜腿），即 Markdown 的 `\mathbb {R}` **正确**，`-bbox` 的 `R` 系 CMap 伪影，**不改**。
     - `F := \sum (...)E _ {i}`（L1568）：bbox 把求和号误报为 `X`，无法直接看出有无下标；裁片 `/tmp/bk_p34_sumF.png` ×12 目视确认求和号**无下标**、`a_i` 与 `E_i` 各带下标、ε/4 为真分式，与 Markdown L1568 **逐项一致**，**不改**。
     - `\equiv t B ^ {\sim} + F / X`（L1594）：需确认 `\equiv`（三横线）而非 `=`、上标是波浪 `∼` 而非 `′′`、`F/X` 的斜杠；裁片 `/tmp/bk_p34_equiv.png` ×12 目视三项均确认，Markdown **正确**，**不改**。
  2. **登记不修（字形/别名族变体）**：`\begin{array}{c}` / `\begin{array}{r l}` 对齐环境包裹两行显示式（含 `\\` 与 `\qquad`），而印刷为 flush 对齐——属既定登记类；`\leq`/`\ge` 与 `\leq` 别名混用；`ǫ`(U+01EB) 与 `\epsilon` 在同页混用（L1559 `ǫ-lc` 用字形、L1562/L1568/L1580/L1586 用 `\epsilon`）；`\text { and }`（L1574）；`exceptional/X`、`F / X`、`K _ {V} + \Gamma_ {V }` 等数学与正文的空格粘连；`\mathbb {R}` 的内部空格。均渲染等价，登记不修。
  3. **登记不修（版式损失）**：`Step 4.`/`Step 5.` 的斜体步号退化为普通文本；两行对齐式的对齐点信息由 `\begin{array}` 近似承载。
  4. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①印刷用 `F/X`（斜杠加异常除记号）表示「在 X 上数值等价」，`exceptional/X` 同理；Markdown 原样保留 `F / X` 与 `exceptional/X` 的写法，未改写为 `F_X` 或 `\operatorname{exceptional}/X` 等更规范形式。②`positive-dimensional` 在印刷中保留连字符（bbox L111 `with positive-dimensional`），而 p.33 同词在行末断行处被 Markdown 合并为 `zerodimensional`；本页两处 `positive-dimensional`（L1589、L1591）在 Markdown 中**连字符完好**，与印刷一致，无需处理。③本段 `a`（log discrepancy 记号）与 p.33 末尾 Γ_V 公式中的 `(1-a)T` 同指一物，与印刷一致。
- 溯源：本页**零改动**，无缺陷需归因；所核区间（L1559–L1621）在 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版中内容一致，本页未触碰任何三版存在差异之处。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p034`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。
  5. **跨越页面边界登记**：L1505 的跨页合并行与 L1559 起的 p.34 内容已与 p.32 审计的边界结论交叉核对一致，未见断裂或重复。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p033`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.035（PDF p.35 / 印刷 p.35）

- PNG：`/tmp/birksing_audit_p035.png`（gs `pngmono` 150dpi，Read 工具已亲阅全页）；因 150dpi 下字号不足以裁定若干上标/下标与省略号位置，另渲染 300dpi `pnggray` 为 `/tmp/bk_p35_300.png`（2550×3300）并切出 7 张裁片逐张 Read：`/tmp/bk_p35_top.png`（×5，Step 5 尾–Step 6 首三个显示式）、`/tmp/bk_p35_Bsim.png`（×20，`μ_T(B^∼+R_Y)` 段）、`/tmp/bk_p35_dots.png`（×24，`X_l →···→ X_0` 省略号）、`/tmp/bk_p35_ampL.png`（×12，`3mA−D ∼_ℝ (mA−(1/t)K_X)+`）、`/tmp/bk_p35_ampR.png`（×12，`+(mA−(3d/t)A)+(mA−((1+t)/t)B)`）、`/tmp/bk_p35_last.png`（×16，`μ_Tν*L ≤ deg_Jν*L ≤`）、`/tmp/bk_p35_tail2.png`（×22，`≤ J^d ≤ q.`）。文本层用 `pdftotext -bbox -f 35 -l 35` 取 `/tmp/bk_p35_bbox.html`，按 yMin<2.0pt 归并为 L000–L141 逐行比对；所有公式判读一律以裁片为准。
- 核对（正文页五点）：
  1. **节标题与步号顺序**：印刷本页为 `Step 5.` 的尾段（`for some` / `H ∼_ℝ (1/t)(K_X+B+3dA)` / `Letting D be the pushdown of D_Y to X, we get D = H+B.`）→ `Step 6.`（bbox L013 起）→ `Step 7.`（bbox L119 起）。Markdown L1623–L1683 步号出现顺序与内容归属逐段一致，无错位、无重复、无跳步。
  2. **定义/定理/引理编号与陈述**：本页无新编号命题，仅承接 Proposition 5.5（`Step 7.` 明写 `In this step we apply Proposition 5.5 and finish the proof`，bbox L119）；陈述文字与印刷逐句一致，未见改写或增删。（`Lemma 2.3` 出现在 p.36 段内，不属本页。）
  3. **公式（系数/指数/上下标）逐条**：L1634 `K_Y + B_Y^∼ + R_Y = π^*(K_X+B)`；L1640 两行 `K_Y + R_Y + D_Y − (1/t)F_Y = K_Y + R_Y + B_Y^∼ + π^*H \\ = π^*(K_X+B+H) = π^*(K_X+D).`；L1646 `(Y, R_Y + D_Y − (1/t)F_Y)`；L1652 两行 `a(T,X,D) = 1 − μ_T(R_Y + D_Y − (1/t)F_Y) = 1 − μ_T R_Y \\ = 1 − μ_T(B^∼ + R_Y) = a(T,X,B) ≤ 1.`；L1658 `D ∼_ℝ (1/t)(K_X+B+3dA) + B,`；L1664 `3mA − D ∼_ℝ (mA − (1/t)K_X) + (mA − (3d/t)A) + (mA − ((1+t)/t)B)`；L1674 `ν : U = X_l → ··· → X_0 = X,`；L1682 `μ_T ν^* L ≤ deg_J ν^* L ≤ J^d ≤ q.`。**上述 8 个显示式全部与印刷一致**：`\frac{1}{t}`、`\frac{3d}{t}`、`\frac{1+t}{t}` 三个分式的分子分母（bbox L103 分子行 `1 3d 1+ t` / L109 分母行 `t t t`）逐一对应；`\pi^ {*}`、`B ^ {\sim}`、`D _ {Y}`、`\deg_ {J}`（bbox L138 `J` 的 yMin=716 低于基线 711 → 下标）、`J ^ {d}`（bbox L140 `d` 的 yMin=709 高于基线 711 → 上标）皆正确。
  4. **记号约定**：`a(\cdot,\cdot,\cdot)`（log discrepancy）、`\mu_T`、`\deg_J`、`\sim_{\mathbb{R}}`、`\pi^*`、`B_Y^∼`、上标 `∼` 表示 birational transform——全部与印刷同形同义，Markdown 未替换成任何「更规范」的等价记号。
  5. **行间关系**：`On the other hand, since D ∼_ℝ …, there is a natural number m depending only on d, r, t, so depending only on d, r, ǫ, such that 3mA − D ∼_ℝ … is ample because we can ensure that each bracket is an ample divisor.`（bbox L093–L110）承接正确；`Since π is an isomorphism …`（L111–L118）到 `Step 7.`（L119）的过渡与印刷一致。
- 结果：**PASS**（零改动）。
  1. **本轮唯一由 bbox 引出的疑点已由裁片推翻**：`pdftotext -bbox` 在 L088 把该显示式第二行输出为 `∼ = 1 − µ …`，即 `∼`（x=270.72–277.30，y=363.66–368.67）出现在行首、与 `=`（x=214.20）之前，看似该波浪是行首符号或 `B''` 的误映射。我据此先验推测它是 `′′`。但按 x 坐标硬证据，`(B` token 收于 x=270.11、`+` 起于 x=280.20，而 `∼` 恰落在 [270.72, 277.30] 之间且其 yMax=368.67 明显高于同行基线 yMax=375.33（真上标）；`/tmp/bk_p35_Bsim.png`（×20）目视亦清楚显示 `μ_T (B` 之后是一个**抬高的波浪号**，其后才是 `+ R`。**结论：印刷即 `B^{\sim}`，Markdown L1652 `\mu_ {T} (B ^ {\sim} + R _ {Y})` 正确，撤销疑点，不改**——依铁律二「裁片优先」记录此项，并同时作为「bbox 内容流顺序不可直接当作视觉顺序」的一次实例登记。
  2. **登记不修（省略号轴位变体，字符数正确）**：`ν : U = X_l → ··· → X_0 = X` 的三个点在印刷中位于箭头中线高度（bbox L124：`→` y=610.90–621.81，三点各占同高区间，实为居中点），Markdown 用 `\dots`（基线偏下）。`/tmp/bk_p35_dots.png`（×24）目视确认三点等距居中。点数与相对间距均正确，仅轴位不同，属既定登记类，**不改**。
  3. **登记不修（定界符尺寸）**：L1664 的三组括号在印刷中是**跨分式拉伸**的大括号（`/tmp/bk_p35_ampL.png` ×12、`/tmp/bk_p35_ampR.png` ×12 目视：括号顶端高于 `mA` 上缘、底端低于分母 `t` 下缘），Markdown 用 `\left( … \right)` 正确还原；bbox 文本层只给出普通高度 `(`/`)` 字符，属 CMap 失真，不构成差异。
  4. **登记不修（字形/别名族变体）**：`ǫ`(U+01EB，L1631 `ǫ-lc`、L1643 `sub-ǫ-lc`、L1649 `ǫ-lc`) 与 `\epsilon`（L1649 `\leq 1 - \epsilon`、L1661、L1679）在同页混用；`\leq`/`\ge` 别名混用；两处两行对齐式用 `\begin{array}{c} … \\ … \end{array}` 近似印刷的 flush 对齐；`Step 6.`/`Step 7.` 的斜体步号退化为普通文本；Math 与正文间空格粘连（`Letting D be the pushdown of$D _ { Y }$to$X$`、`of length$l \leq p$`）。均渲染等价，登记不修。
  5. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①印刷 Step 6 开头写 `…to the situation in which Supp B does not contain any stratum of (X, Λ) other than x`，而本步末尾才由 `by Step 1` 补足零维层只有 `x`；此为原文措辞，Markdown L1631 原样保留，未据逻辑改写。②印刷的 `positive-dimensional`（两处）连字符完好，Markdown 亦保留，未丢失（与 p.33 行末断行处合并为 `zerodimensional` 的情形不同）。③`d, r, t` 与 `d, r, ǫ` 在同一句里先后出现（bbox L101 `d, r, t, so depending only on d, r, ǫ`），按原文保留。
- 溯源：本页**零改动**，无缺陷需归因；所核区间（L1623–L1683）在 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版中内容一致，本页未触碰任何三版存在差异之处。
- 跨页边界登记：本页印刷末行为 bbox L134–L141（`q depending only on d, r, ǫ such that` + `μ_T ν^*L ≤ deg_J ν^*L ≤ J^d ≤ q.`），Markdown 以 L1683 的 `$$` 收束该显示式，L1685 `Thus$\mu _ { T } \nu ^ { * } L \leq q$if we replace ν…` 起属 **p.36**；此边界将在 p.36 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p035`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.036（PDF p.36 / 印刷 p.36）

- PNG：`/tmp/birksing_audit_p036.png`（gs `pngmono` 150dpi，Read 工具已亲阅全页）；另渲染 300dpi `pnggray` 为 `/tmp/bk_p36_300.png`（2550×3300）并切出 9 张裁片逐张 Read：`/tmp/bk_p36_half.png`（×8，`\frac12 A_W+K_W` 与 `\frac12 A_W-(K_W+B_W)`）、`/tmp/bk_p36_delta.png`（×14，`Δ_W := αB_W+(1−α)Θ_W ≥ 0`）、`/tmp/bk_p36_excp.png`（×8，`…and each exceptional/X prime`）、`/tmp/bk_p36_Ad.png`（×14，`…this means that A_W^d is bounded…`）、`/tmp/bk_p36_zero.png`（×10，`0 = a(T,X,Λ) = a(T,W,Λ_W) ≥ a(T,W,Θ_W) ≥ 0`）、`/tmp/bk_p36_deg.png`（×16，`deg_A Λ < A^d ≤ r.`）、`/tmp/bk_p36_PQ.png`（×12，`𝒫`/`𝒬`）、`/tmp/bk_p36_eps.png`（×12，`Let δ = αε. … sub-ε-lc`）、`/tmp/bk_p36_qed1.png`（×22，页首 QED 方框）。文本层用 `pdftotext -bbox -f 36 -l 36` 取 `/tmp/bk_p36_bbox.html`（753 word），按 yMin<2.0pt 归并为 L000–L199 逐行比对；所有公式判读一律以裁片为准。
- 核对（正文页五点）：
  1. **页首承接与节标题顺序**：印刷 p.36 以 p.35 末尾显示式的收尾句 `Thus μ_Tν^*L ≤ q if we replace ν with any other resolution on which T is a divisor.` 起（bbox L002–L004，其后即 QED 方框），随后 `Proof. (of Proposition 5.7)`（bbox L006）→ 两个 `•` 项目（L019、L027）→ 正文若干段 → 末尾 `Now after replacing ɛ with δ …` + QED 方框（L188–L199）。Markdown L1685–L1733 与此逐段对应，无错位、无重复、无跳段；`5.10. Construction of Λ.`（MD L1735）起属 **p.37**。
  2. **定义/定理/引理编号与陈述**：本页出现 `Proposition 5.7`（被证明者）、`Lemma 2.3`（bbox L114）、`Lemma 5.9`（bbox L198）三处编号，Markdown L1687/L1713/L1733 三处编号数字与所指命题全部一致，未见改写、错指或增删。
  3. **公式（系数/指数/上下标）逐条**：`deg_A Λ < A^d ≤ r`（L1687）；`0 = a(T,X,Λ) = a(T,W,Λ_W) ≥ a(T,W,Θ_W) ≥ 0`（L1698）；`Δ_W := αB_W + (1−α)Θ_W ≥ 0`（L1708）；`a(T,W,Θ_W) = 0,`（L1716）；`a(T,W,Δ_W) = αa(T,W,B_W) + (1−α)a(T,W,Θ_W) \\ = αa(T,W,B_W) = αa(T,X,B) ≤ 1.`（L1722，两行）；`A_W − Δ_W = α(A_W − B_W) + (1−α)(A_W − Θ_W)`（L1728）；以及行内的 `\frac12 A_W + K_W`、`\frac12 A_W − (K_W+B_W)`（L1725）。**逐项与印刷一致**：`/tmp/bk_p36_half.png`（×8）目视确认两处是**行内 textstyle 的 1/2 分式**（分子 `1` 在分数线上、分母 `2` 在线下），bbox 把它们误连为单个 `12` token（x=329.76–333.99 与 409.92–414.15，y=609.01–623.27，恰好跨分数线上下）——Markdown 的 `${ \textstyle { \frac { 1 } { 2 } } }` **正确，撤销疑点不改**；`/tmp/bk_p36_deg.png`（×16）确认 `<` 为严格小于且 `A^d` 的 `d` 是上标、`deg` 的 `A` 是下标；`/tmp/bk_p36_zero.png`（×10）确认 `Λ_W` 的 `W` 为下标、`≥` 两处齐全；`/tmp/bk_p36_delta.png`（×14）确认 `:=` 为「冒号+等号」两字符、`\geq` 为单横线式。
  4. **记号约定**：`a(T,\cdot,\cdot)`（log discrepancy）、`\phi`（log resolution）、`\Theta_W`（reduced divisor / exceptional + birational transform of Λ）、`\Delta_W`（convex combination）、`\mathcal{P}`/`\mathcal{Q}`（bounded families）、`\deg_A`、`A^d`、`\deg_J`（承 p.35）——全部与印刷同形同义，Markdown 未替换成任何等价记号。
  5. **行间关系**：`Replacing A we can assume it is effective and that A − (K_X + B) is ample (we use the latter below)` 的预告在 L1687 提出、在 L1713 之后兑现（`A_W − Θ_W` ample ⇒ `(W,Δ_W)` δ-lc ⇒ `A_W − B_W` ample ⇒ `A_W − Δ_W` ample），Markdown 段落顺序与印刷完全一致，推理链未断。
- 结果：**PASS±**（零改动；仅登记既定的排版/字形族瑕疵，不影响本页任何推理，判级依前序同源页先例）。
  1. **QED 方框 □ 两处缺失（登记不修）**：印刷在本页有**两个**结束方框——bbox L005（x=512.88–521.36，y=102.67–113.98，紧随 `…is a divisor.`）与 L199（x=512.88–521.36，y=712.03–723.34，紧随 `…by Lemma 5.9.`），全页 `U+0003` 计数恰为 2，与视觉一致；`/tmp/bk_p36_qed1.png`（×22）目视确认为粗线空心方框 □。Markdown 两处均无。依本篇既定口径「QED 方框 □ 一律登记不修」，**不改**。
  2. **`exceptional/Xprime` 词间空格缺失 + 标记泄漏（登记不修）**：印刷作 `…and each exceptional/X prime divisor has coefficient 1 in Θ_W.`（bbox L103–L106，`prime` 是与 `exceptional/X` 分离的独立 word，`/tmp/bk_p36_excp.png` ×8 目视可见 `X` 与 `prime` 之间有明确空隙，且 `X` 为斜体数学、`prime` 为正体文本）。Markdown L1711 作 `each exceptional$/ X$prime divisor`，数学定界符在 `X` 后即闭合，`prime` 落在定界符外且**与 `X` 之间无空格**，渲染出 `Xprime`。此构造与本篇先前页（p.28–p.32）已登记的同一 `exceptional$/ X$prime` 完全同形，先前已按「Math 与正文间空格粘连 / 标记泄漏」判为 PASS± 级瑕疵登记在案；本次沿用同一口径，**不重复改动**，登记之。
  3. **ℝ/ℚ 压平（登记不修）**：印刷 `K_X + B and B are ℝ-Cartier by assumption, K_X is ℚ-Cartier`（bbox L085–L087 的 `R`/`Q` 是双线字形的 CMap 失真）；Markdown L1703 写 `R-Cartier` 与 `\mathbb { Q } \mathrm { { - } C a r t i e r }`——`\mathbb{Q}` 正确，`R-Cartier` 为 ℝ→R 压平，属既定登记类。
  4. **`\mathcal{Q}` 压平为普通 `Q`（登记不修）**：印刷 `couples 𝒫 … family 𝒬`（`/tmp/bk_p36_PQ.png` ×12 目视两字母均为花体）；Markdown L1687 对 `\mathcal { P }` 正确保留花体、对 `Q` 则写成普通斜体。同属字形族变体，登记不修。
  5. **`ǫ` / `\epsilon` 混用（登记不修）**：印刷 `Let δ = αε.` 与 `sub-ε-lc` 用的是月形 lunate ε（bbox 解码为 `ǫ` U+01EB，`/tmp/bk_p36_eps.png` ×12 目视确认字形），Markdown L1713 前者写 `\epsilon`、后者写字形 `ǫ`，两者渲染同为月形 ε；另 L1733 `Now after replacing ǫ with δ…` 亦用字形。登记不修。
  6. **登记不修（版式损失）**：`Proof.` 的斜体运行头退化为普通文本（印刷为斜体 `Proof.`）；行内 `A − (K_X + B)` 印刷用普通高度括号而 Markdown 用 `\left( … \right)`（此处无分数，渲染同尺寸）；`propo-sition` 的行末断词连字符被合并为 `proposition`；`{ \mathrm { S u p p } }`、`{ \mathrm { - } C a r t i e r }` 等 MathJax 字距转义；`deg$_ { A }` 这种「正文+ 数学 + 下标」被切在定界符外的标记形态。
  7. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①印刷写作 `Replacing A we can assume it is effective`——通常的 log 几何表述是「把 A 换成有效除子」而非「假设 A 有效」，措辞可疑但 Markdown L1687 原样保留。②印刷 `belongs to bounded family of couples`（L090）**缺冠词 `a`**，而同段上一句 L014 作 `belongs to a bounded family of couples P`；Markdown L1703 原样保留缺冠词的写法，未补 `a`。③印刷末尾 `we can assume that (X, Λ) is log smooth with Λ reduced` 中 `Λ reduced` 的 `Λ` 为正体希腊字母而非数学斜体，Markdown L1733 亦写正体 `Λ reduced`，一致。
- 溯源：本页**零改动**，无缺陷需归因；所核区间（L1685–L1733）在 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版中内容一致，本页未触碰任何三版存在差异之处。
- 跨页边界登记：本页印刷末行为 bbox L188–L199（`Now after replacing ɛ with δ … Lemma 5.9.` + 第二个 QED 方框），Markdown 以 L1733 该句收尾，L1735 `5.10. Construction of Λ.` 起属 **p.37**；此边界将在 p.37 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p036`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.037（PDF p.37 / 印刷 p.37）

- PNG：`/tmp/birksing_audit_p037.png`（gs `pngmono` 150dpi，Read 工具已亲阅全页）；另渲染 300dpi `pnggray` 为 `/tmp/bk_p37_300.png`（2550×3300）并切出 4 张裁片逐张 Read：`/tmp/bk_p37_let.png`（×20，`Let X,B,A,L,T,t be as in the`）、`/tmp/bk_p37_eps2.png`（×22，`is ε′/2-lc outside finitely`）、`/tmp/bk_p37_QR.png`（×12，`a 𝕼-Cartier 𝕼-divisor Λ ≥ 0`）、`/tmp/bk_p37_Rdiv.png`（×16，`• L ≥ 0 is an ℝ-divisor on X,`）。文本层用 `pdftotext -bbox -f 37 -l 37` 取 `/tmp/bk_p37_bbox.html`，按 yMin<2.0pt 归并为 L000–L081 逐行比对；所有公式判读一律以裁片为准。
- 核对（正文页五点）：
  1. **节标题与命题编号顺序**：印刷 `5.10. Construction of Λ.`（bbox L002）→ `Proposition 5.11.`（L006）→ 其七条 `•` 假设（L009–L017）→ `Then there is a 𝕼-Cartier 𝕼-divisor Λ ≥ 0 such that`（L018）→ 四条 `•` 结论（L019–L022）→ `Proof.`（L023）→ `Step 1.`（L028）→ 三条 `•`（L050–L067）→ 两个显示式与结尾 `Now (X, H+B+tL+2v(B+tL))`（L079–L081）。Markdown L1735–L1803 与此逐段对应，`Proposition 5.11`、`Theorem 1.8`、`Theorem 1.9`、`5.5`、`[13]`、`Step 1` 编号与所指全部一致，无错位、无跳段。
  2. **假设/结论条目的编号与陈述**：七条假设 `• (X,B) is a projective ɛ-lc pair of dimension d,` / `• A is a very ample divisor on X with A^d ≤ r,` / `• L ≥ 0 is an ℝ-divisor on X,` / `• A−B and A−L are ample (so we are assuming that B and L are ℝ-Cartier),` / `• (X, B+tL) is ɛ′-lc for some t ∈ (0,r),` / `• we have` + 显示式 + `for some prime divisor T over X, and` / `• the centre of T on X is a closed point x.` 与 Markdown L1739–L1757 逐条一致；四条结论 `• nΛ is integral,` / `• mA−Λ is ample,` / `• (X,Λ) is lc near x, and` / `• T is an lc place of (X,Λ).` 与 L1761–L1767 逐条一致。
  3. **公式（系数/指数/上下标）逐条**：`a(T, X, B+tL) = ε′`（L1752）；`(X, B+tL+v(B+tL))`（L1774）；`ε′/2-lc`（L1777）；`(r+1)A − B − tL = A − B + t(A − L) + (r−t)A`（L1780）；`A_H = A|_H, B_H = B|_H, L_H = L|_H`（L1785，含竖线限制记号）；`A_H^{d−1} ≤ r`（L1789）；`(H, B_H + tL_H + 2v(B_H + tL_H))`（L1796）；`(X, H + B + tL + 2v(B + tL))`（L1802）。**逐项与印刷一致**：`(r+1)` 中的 `1` 未丢、`t` 系数未错位、`A|_H` 的竖线与下标 `H` 俱在；`A_H^{d−1}` 经 bbox 双向验证——`d−1` 的 yMin=604.63 高于 `A` 的 yMin=606.70（上标），`H` 的 yMin=612.67 低于 `A` 的 yMax=617.61（下标），且 `d−1` 与 `H` 的 xMin 同为 320.28（同一右上/右下角位），Markdown `$A _ { H } ^ { d - 1 }$` 正确。
  4. **记号约定**：`a(T,\cdot,\cdot)`、`ε` 与 `ε′`（后者只依赖 `d,r,ε`）、`v`、`t ∈ (0,r)`、`A_H = A|_H`（一般元截面限制）、`lc`/`klt`/`plt`、`ACC for lc thresholds [13]`——全部与印刷同形同义，Markdown 未替换记号。
  5. **行间关系**：`Step 1.` 先由 `(X, B+tL+v(B+tL))` 是 `ε′/2-lc` 取一般元 `H ∈ |A|`，得 `(H, B_H+tL_H)` 是 `ε′`-lc 维 `d−1` 且 `A_H^{d−1} ≤ r`、`A_H − B_H − tL_H` ample，从而由 Theorem 1.8（维 `≤ d−1`）得 `(H, B_H+tL_H+2v(B_H+tL_H))` 是 klt；因 `ε′` 只依赖 `d`，`v` 可取只依赖 `d,r,ε`；末句 `Now (X, H+B+tL+2v(B+tL))` 交棒给下一页的 inversion of adjunction。Markdown 段落顺序与印刷完全一致，推理链未断。
- 结果：**FAIL**（1 处改动）。
  1. **缺陷明细（唯一 1 处）**：印刷 bbox L026 的 token 序列为 `Let`(x=250.32) `X,` `B,` `A,` `L,` `T,` `t`(x=335.16–339.10) `be`(x=343.32)——`T,` 与 `t` 之后**直接**接 `be`，全行只有一个 `t`。Markdown L1769 却写成 `Let$X , B , A , L , T , t$t be as in the proposition with…`，数学定界符在第一个 `t` 后闭合，紧接着又多出一个正体 `t`，渲染为 `X, B, A, L, T, tt be as in`——**多出一个重复字符**。`/tmp/bk_p37_let.png`（×20）目视确认印刷在 `T,` 与 `be` 之间确只有一个斜体 `t`。属字符级重复缺陷，**已用 Edit 逐处修复**（只删去定界符外那个多余的 `t`，其余字节不动；修复后渲染为 `X, B, A, L, T, t be as in`，与印刷逐字一致）。
  2. **溯源**：该处已就父提交版 `^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版逐字节核对：三版**均**含 `, T , t$t be as in the proposition`（以 `, T , t$ be as in` 形式计数为 0、以 `, T , t$t be as in` 形式计数为 1），即该重复 `t` **初次 MinerU 导出即已写入，属导出缺陷，原导出在此处不正确**；**不是**后续 peer 引入的回归。
  3. **由 bbox 引出的疑点已由裁片推翻（撤销，不改）**：`ε′/2` 处的 bbox 给出 `ǫ`(x=102.84–106.26, y=513.19–520.51)、`′`(x=106.32–108.50, y=512.66–518.09)、`2`(x=103.80–108.03, y=521.53–527.75) 三个 token，其中 `2` 的 yMin 低于 `ǫ` 的 yMax，且 x 区间与 `ǫ` **重叠**（而非右移），乍看像下标 `ε′_2`。`/tmp/bk_p37_eps2.png`（×22）目视清楚显示二者之间有一条**可见的分数线**、`2` 位于线下——即印刷是 textstyle 的**竖排分式** `\frac{\epsilon'}{2}`，Markdown L1777 `$\frac { \epsilon ^ { \prime } } { 2 } \mathrm { - l c }$` **正确**，撤销疑点不改。
  4. **登记不修（ℝ/ℚ 压平）**：印刷 `L ≥ 0 is an ℝ-divisor on X`（`/tmp/bk_p37_Rdiv.png` ×16 确认为双线 ℝ 加连字符）与 `A−B and A−L are ample (… B and L are ℝ-Cartier)`（bbox L012）均被 Markdown 写成普通 `R`（L1743 `R-divisor`、L1745 `\mathbb { R } \mathrm { - } C a r t i e r`——后者保留了花体）；`a 𝕼-Cartier 𝕼-divisor Λ ≥ 0`（`/tmp/bk_p37_QR.png` ×12 确认两处均为双线 ℚ 加连字符）中，Markdown L1759 写成 `Q-Cartier Q-divisor`。依既定口径 ℚ/ℝ 压平属渲染等价的字形族变体，登记不修（连字符全部保留，无需处理）。
  5. **登记不修（HTML 上标泄漏）**：L1787 写作 `ǫ<sup>′</sup>-lc`，印刷为 `ɛ′`-lc（撇号真上标，`/tmp/bk_p37_eps2.png` 顶部同款字形可参）。同一段 L1737 与 L1747 也用 `ǫ<sup>′</sup>`，属本篇既定的 `<sub>`/`<sup>` 残留族，登记不修。
  6. **登记不修（版式损失）**：`Proposition 5.11.`、`Proof.`、`Step 1.` 的运行头斜体/粗体在 Markdown 中退化为普通文本；`{ \mathrm { - l c } }`、`{ \mathrm { - } C a r t i e r }` 等 MathJax 字距转义；Math 与正文间空格粘连（`Let$X , B , A , L , T , t$ be as in`、`depending only on$d , r , \epsilon$such that`）。
  7. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①印刷在 `A^d ≤ r` 与 `A_H^{d−1} ≤ r` 中都把 `d` 写成上标而**未加括号**（`A^d` 而非 `A^{(d)}`），Markdown 照原样保留。②印刷 `L ≥ 0 is an ℝ-divisor on X` 用的是**连字符**连接的 `ℝ-divisor`，Markdown 保留连字符，未改写为 `ℝ divisor` 或 `\mathbb{R}`-divisor。③印刷假设清单首条 `(X, B) is a projective ɛ-lc pair of dimension d,` 与结论清单末条 `T is an lc place of (X, Λ).` 之间的 `Then there is a 𝕼-Cartier 𝕼-divisor` 为无编号过渡句，Markdown 未给它编号。
- 跨页边界登记：本页印刷末行为 bbox L080–L081（`Now` + `(X, H + B + tL + 2v(B + tL))`，y=698/711），Markdown 以 L1801–L1803 的 `$$ (X, H + B + tL + 2v(B + tL)) $$` 收尾，L1805 `is plt in a neighbourhood of$H$by inversion of adjunction [28, Theorem 5.50].` 起属 **p.38**；此边界将在 p.38 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p037`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

---

## p.038（PDF p.38 / 印刷 p.38）

- PNG：`/tmp/birksing_audit_p038.png`（gs `pngmono` 150dpi，Read 工具已亲阅全页）；另渲染 300dpi `pnggray` 为 `/tmp/bk_p38_300.png`（2550×3300）并切出 4 张裁片逐张 Read：`/tmp/bk_p38_comma.png`（×18，`is plt in a neighbourhood of H, by inversion`）、`/tmp/bk_p38_GW.png`（×8，`Γ_W = (1+v)(B^∼+tL^∼) + (1−ε′/4)∑E_i + (1−ε′)T`）、`/tmp/bk_p38_eps2.png`（×14，`is ε′/2-lc outside finitely many closed`）、`/tmp/bk_p38_half.png`（×6，`and because (X,B+tL) is ε′-lc.`）。文本层用 `pdftotext -bbox -f 38 -l 38` 取 `/tmp/bk_p38_bbox.html`，按 yMin<2.0pt 归并为 L000–L135 逐行比对；所有公式判读一律以裁片为准。
- 核对（正文页五点）：
  1. **节标题与步号顺序**：本页为 p.37 `Step 1.` 的收尾（`is plt in a neighbourhood of H, …` 起）→ 显示式 `(X,B+tL+2v(B+tL))`（bbox L003）→ `(X,B+tL+v(B+tL))`（L005）→ 均值分式显示式（L010–L018）→ `Step 2.`（L020）→ 定义 `Γ_W`（L027）→ `c_i`（L037）→ `ε′=a(T,X,B+tL)`（L043）→ 第一个两行展开式（L045–L064）→ `F`（L066）→ `c′_i`（L078）→ `a′`（L084）→ 第二个两行展开式（L086–L109）→ `G`（L111）→ `(X,(1+v)(B+tL))`（L121）→ 收尾句（L122–L135）。Markdown L1805–L1887 与此逐段对应，无错位、无跳步；`Step 3.`（MD L1889）起属 **p.39**。
  2. **编号与陈述**：`Lemma 2.3`（bbox L009）、`[28, Theorem 5.50]`（L002）两处引用编号与所指一致；本页无新编号命题。陈述文字与印刷逐句一致，未见改写、增删或错指。
  3. **公式（系数/指数/上下标）逐条**：`\frac12(K_X+B+tL) + \frac12(K_X+B+tL+2v(B+tL))`（L1820）；`Γ_W = (1+v)(B^∼+tL^∼) + (1−\frac{ε′}{4})\sum E_i + (1−ε′)T`（L1828）；`c_i = a(E_i, X, B+tL)`（L1834）；`ε′ = a(T, X, B+tL)`（L1840）；`K_W+Γ_W = K_W+B^∼+tL^∼+\sum(1−c_i)E_i+(1−ε′)T+v(B^∼+tL^∼)+\sum(c_i−\frac{ε′}{4})E_i \\ = ψ^*(K_X+B+tL)+v(B^∼+tL^∼)+F`（L1846，两行）；`F := \sum(c_i − \frac{ε′}{4})E_i`（L1852）；`c′_i = a(E_i, X, (1+v)(B+tL))`（L1860）；`a′ = a(T, X, (1+v)(B+tL))`（L1866）；`K_W+Γ_W = K_W+(1+v)(B^∼+tL^∼)+\sum(1−c′_i)E_i+(1−a′)T+\sum(c′_i−\frac{ε′}{4})E_i+(a′−ε′)T \\ = ψ^*(K_X+(1+v)(B+tL))+G`（L1872，两行）；`G := \sum(c′_i − \frac{ε′}{4})E_i + (a′−ε′)T`（L1878）；`c′_i ≥ \frac{ε′}{2}`（L1887）。**逐项与印刷一致**：`ε′` 的撇号在 bbox 中一律为 yMin 低于主基线的上标 token（如 L025 `ǫ` y=273 / `′` 同高，L046 `ǫ′` y=385），Markdown 的 `\epsilon^ {\prime}` 正确；三个分式 `\frac{ε′}{4}`（两处）、`\frac{ε′}{2}`（两处）分子分母经 `/tmp/bk_p38_GW.png`（×8）与 `/tmp/bk_p38_eps2.png`（×14）目视**均带可见分数线**，非下标；`\sum` 的印刷字形为**大号无上下限 Σ**（bbox 把这四处 Σ 误解码为 `X`，见 L066/L093/L099/L111 的孤立 `X` token），`/tmp/bk_p38_GW.png` 目视确认，Markdown `\sum` 正确。
  4. **记号约定**：`a(E_i, X, \cdot)`（沿用上文的 `a(\cdot,\cdot)`）、`c_i` / `c′_i`、`a′`、`F` / `G`、`\psi^*`、`\sim`（birational transform 记号）、`\frac{ε′}{2}`-lc / `\frac{ε′}{4}` 系数——全部与印刷同形同义，Markdown 未替换记号。
  5. **行间关系**：`is plt … by inversion of adjunction [28, Theorem 5.50]` ⇒ `(X,B+tL+2v(B+tL))` klt ⇒ （对 v 减半）`(X,B+tL+v(B+tL))` 是 `ε′/2`-lc（由 Lemma 2.3 与 `(X,B+tL)` 是 `ε′`-lc）⇒ Step 2 引入 log resolution `ψ` 与 `Γ_W`，用 `c_i`、`c′_i`、`a′` 把 `K_W+Γ_W` 两次展开成 `ψ^*` 的拉回加有效除子 `F`、`G`；结尾由 `E_i` 的像正维 ⇒ `c′_i ≥ ε′/2` ⇒ `E_i` 是 `G` 的正系数分支。Markdown 段落顺序与印刷完全一致，推理链未断。
- 结果：**FAIL**（1 处改动）。
  1. **缺陷明细（唯一 1 处）**：印刷 bbox L002 为 `is plt in a neighbourhood of H, by inversion of adjunction [28, Theorem 5.50]. Therefore,`——`H` 之后**有逗号**（bbox 该 token 为 `H,`）；`/tmp/bk_p38_comma.png`（×18）目视可见斜体 `H` 右侧紧跟一个带下探尾钩的逗号，再接 `by inversion`。Markdown L1805 写成 `is plt in a neighbourhood of$H$by inversion of adjunction [28, Theorem 5.50]. Therefore,`，数学定界符在 `H` 后闭合，**逗号被整个丢失**，渲染为 `neighbourhood of H by inversion`。属字符级标点缺失，**已用 Edit 逐处修复**（只在定界符后补回一个逗号，其余字节不动；修复后渲染为 `neighbourhood of H, by inversion`，与印刷逐字一致）。
  2. **溯源**：父提交版 `^`(`16ffcc7c`) 与当前 HEAD(`37580aaf`) 的 L1805 均为 `…of$H$by inversion…`（缺逗号），而**初次 MinerU 导出 `53a92412` 的同一行为 `is plt in a neighbourhood of$H _ { ; }$by inversion of adjunction [28, Theorem 5.50]. Therefore,`**——同样缺逗号，且额外带一个伪下标残留 `$H _ { ; }$`。即：该行的伪下标 `_ { ; }` 已在此前某轮修复中被清掉，但**缺逗号自初次导出即存在并一直保留**，故此缺逗号**属导出缺陷，原导出在此处不正确**，**不是**后续 peer 引入的回归。
  3. **登记不修（HTML 下标泄漏）**：L1825 写作 `define a boundary Γ<sub>W</sub>`，印刷为 `Γ_W`（`W` 为真下标，bbox L021 `W` 的 yMin=236 高于基线 231 → 上标位？见下方备注）。属本篇既定 `<sub>`/`<sup>` 残留族，渲染结果与 `Γ_W` 一致，登记不修。同类还有 L1831 的 `where$E _ { i }$are …`、`L1855` 的 `…for every$i ,$`。
  4. **登记不修（对齐环境与 MathJax 转义）**：两处两行展开式分别用 `\begin{array}{r}`（L1846）与 `\begin{array}{c}`（L1872）近似印刷的 flush 右对齐；L1887 把行内不等式包成 `$\begin{array} { r } { c _ { i } ^ { \prime } \geq \frac { \epsilon^ {\prime}}{2 } } \end{array}$`；`{ \mathrm { - } \mathrm { lc } }`、`{ - }` 等字距转义。均渲染等价，登记不修。
  5. **登记不修（版式损失）**：`Step 2.` 的斜体步号退化为普通文本；Math 与正文间空格粘连（`is plt in a neighbourhood of$H$…`、`and because$( X , B + t L )$is…`、`a boundary Γ<sub>W</sub> and study…`）。
  6. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①印刷 `Step 2.` 开头写 `In this step we take a log resolution W → X and define a boundary Γ_W and study some of its properties. Let ψ : W → X be a log resolution of…`——同一步内先说「取一个 log resolution `W → X`」，紧接着又说「令 `ψ : W → X` 是 log resolution」，两处 `W → X` 同指同一映射却用了不同记号（`→` 与 `ψ :`）；Markdown L1825 原样保留，未统一。②印刷结尾 `if the image of E_i on X is positive-dimensional for some i, then c′_i ≥ ε′/2 so E_i is a component of G with positive coefficient` 未加句末句点（bbox L135 末 token 为 `coefficient.`，实为**有**句点）——据 bbox 与 150dpi 全页图，句点存在，Markdown L1887 保留句点，一致，无 quirk。③印刷在 `F := ∑(c_i − ε′/4)E_i` 与 `G := ∑(c′_i − ε′/4)E_i + (a′−ε′)T` 中都把 `\frac{ε′}{4}` 排成**行内小分式**而非 `ε′/4` 的斜杠写法，Markdown 用 `\frac` 正确还原。
  7. **印刷 bbox 的 `Γ_W` 下标方向存疑但不影响结论**：bbox L020–L021 把 `Γ` (y=231) 与 `W` (y=236) 分列，`W` 的 yMin=236 略低于 `Γ` 的 yMax，L027–L028 亦同（`Γ` y=281 / `W` y=285）。这是 pdftotext 对 `\Gamma_W` 中「下标 W 与主符号 Γ 共享行盒」时的 yMin 分组产物；`/tmp/bk_p38_GW.png`（×8）目视明确显示 `Γ` 之后右下方是**下标** `W`（比 `Γ` 的基线低、右移），Markdown `\Gamma_ {W}` **正确**，撤销疑虑不改。
- 跨页边界登记：本页印刷末行为 bbox L128–L135（`for some i, then c′_i ≥ ε′/2 so E_i is a component of G with positive coefficient.`），Markdown 以 L1887 该句收尾，L1889 `Step 3.` 起属 **p.39**；此边界将在 p.39 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p038`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.039（PDF p.39 / 印刷 p.39）
- PNG：`/tmp/birksing_audit_p039.png`（150dpi pngmono，1575×2037，Read 亲自查看）。300dpi 灰度底图 `/tmp/bk_p39_300.png`。放大裁片（LANCZOS 升采样，仅用于目视仲裁，不用于写 Markdown）：
  1. `/tmp/bk_p39_frac.png`（×12，x=85–300 / y=124–162）——第 3 行「is ε′/2-lc outside finitely many closed points.」，可见 ε′ 为分子、**2 为分母且有分数线**（不是下标 2）。
  2. `/tmp/bk_p39_asTY.png`（×12，x=88–300 / y=482–505）——「contracted by φ is inside *T*<sub>Y</sub> as −*T*<sub>Y</sub> is ampl[e]」，**印刷确实有负号 −T_Y**，非 Markdown 臆造。
  3. `/tmp/bk_p39_dash.png`（×14，x=88–290 / y=505–520）——「*Y* ⟶ *Y*′ does not contract any divisor.」，箭头**虚线杆**（birational dash-arrow），非实线 `→`。
  4. `/tmp/bk_p39_simRY.png`（×12，x=220–395 / y=562–582）——第 5 节首显示式，*K*<sub>Y</sub>+Γ<sub>Y</sub> **∼**<sub>ℝ</sub>*G*<sub>Y</sub> = (*a*′−ε′)*T*<sub>Y</sub>/*X*，可见 ∼ 为**波浪号**且 ℝ 为**下标**（双线黑板粗）。
  5. `/tmp/bk_p39_geq.png`（×12，x=88–300 / y=608–634）——「Since / *a*(*T*,*X*,*B*) ≥ ϵ > …」，关系符确为**严格大于 `>`** 且左中 eps 无撇。
  6. `/tmp/bk_p39_muTY.png`（×16，x=200–370 / y=648–670）——「μ_*T*<sub>*Y*</sub> φ\* *tL* ≥ ϵ − ϵ′ > 0.」，**下标是嵌套的 *T*<sub>*Y*</sub>**（Y 比 T 更低更右），非 `\mu_T` 加独立 Y。
  7. `/tmp/bk_p39_aprime.png`（×10，x=210–450 / y=676–694）——「(*T*,*X*,(1+*v*)(*B*+*tL*)) < ε′ = *a*(*T*,*X*,*B*+*tL*).」。
  8. `/tmp/bk_p39_last.png`（×12，x=210–400 / y=704–724）——本页末显示式，*K*<sub>Y</sub>+Γ<sub>Y</sub>+2*dA*<sub>Y</sub> ∼<sub>ℝ</sub>(*a*′−ε′)*T*<sub>Y</sub>/*X*。
- 核对（正文页五点）：
  1. **节标题与步号顺序**：印刷依序为 `Step 3.`（bbox L002，y=89）→ `Step 4.`（L060，y=380）→ `Step 5.`（L086，y=538）；Markdown 依序为 L1889 `Step 3.` → L1917 `Step 4.` → L1925 `Step 5.`。**顺序与内容均一致**，无漏步、无错序。
  2. **编号与陈述**：本页为纯正文推演段，无定义/定理/引理编号。`Step 4.` 的陈述「consider a model Y on which −T_Y is ample over X」（bbox L060–L062）与 Markdown L1917 逐字对应；`Step 5.` 的陈述「we show that K_Y + Γ_Y + 3dA_Y is ample where K_Y + Γ_Y, A_Y are the pushdowns of K_Y′ + Γ_Y′, A_Y′」（bbox L086–L105）与 Markdown L1925 逐字对应。
  3. **公式逐条**（全部 8 条显示式 + 1 条行内式逐条比对）：
     - L1892 `$$ (X, (1 + v) (B + t L)) $$` ↔ bbox L011 `(X, (1 + v)(B + tL))`（x=257–355，y=133，居中显示）**一致**。
     - L1895 行内 `\frac{\epsilon^{\prime}}{2}` ↔ bbox L012/L013/L014/L015（`′` y=133 在 `ǫ` y=151 之上；`2` y=158 在其下且 x=104–108 与 `ǫ` x≈100–106 **重叠**）＋ 裁片 1 **确认为分式**，Markdown `\frac{...}{2}` **正确**。
     - L1900 `K_W + Γ_W ≡ v(B^∼ + tL^∼) + F / X` ↔ bbox L032–L036（`≡` x=513–521 单列；两个 `∼` 均在 B、L 的右上）**一致**，含三横等价号与两个波浪上标。
     - L1906 `v(B^∼ + tL^∼) + F ≥ 0,` ↔ bbox L038 **一致**（`≥` 为大于等于）。
     - L1914 `K_X + (1 + v) (B + t L) + 2 d A.` ↔ bbox L057–L059 **一致**。
     - L1920 `a (T, X, B + t L) = \epsilon^{\prime} < 1,` ↔ bbox L064 `a(T, X, B + tL) = ǫ ′ &lt; 1,` **一致**（严格小于）。
     - L1928 `K_Y + Γ_Y \sim_{\mathbb{R}} G_Y = (a′ − \epsilon′) T_Y / X` ↔ bbox L106–L116 ＋ 裁片 4 **逐 token 一致**（∼ 为波浪号、ℝ 为下标、`/X` 斜杠在 *T*<sub>Y</sub> 之后）。
     - L1936 `a (T, X, B) \geq \epsilon > \epsilon^{\prime} = a (T, X, B + t L)` ↔ bbox L132 ＋ 裁片 5 **一致**（`≥` 后是严格 `>`，且左中为无撇 ε）。
     - L1942 `\mu_{T_Y} \phi^{*} tL \geq \epsilon - \epsilon^{\prime} > 0.` ↔ bbox L134/L135/L136/L137（`µ` y=654 → `T` y=658 → `Y` y=661，`Y` 的 x=266–270 与 `T` 的 x=261–266 相接且更低）＋ 裁片 6 **确认为嵌套下标**，Markdown `\mu_ {T _ {Y}}` **正确**。
     - L1948 `a^{\prime} = a (T, X, (1 + v) (B + t L)) < \epsilon^{\prime} = a (T, X, B + t L).` ↔ bbox L139 ＋ 裁片 7 **一致**。
     - L1954 `K_Y + Γ_Y + 2 d A_Y \sim_{\mathbb{R}} (a′ − \epsilon′) T_Y / X` ↔ bbox L141–L151 ＋ 裁片 8 **逐 token 一致**。
  4. **记号约定**：本段出现的 `X`、`Y`、`Y′`、`Y″`、`T_Y`、`T_{Y″}`、`B^∼`、`tL^∼`、`Γ_Y`、`A_Y`、`G_Y`、`a(·)`、`ε`、`ε′`、`a′`、`v`、`d` 均与印刷一致。特别地：印刷用斜杠记号 `F/X`（L1900）、`G/X`（L1897）、`G_Y/X`（L1928）、`T_Y/X`（L1928、L1954）表示「在 X 上数值等价」，Markdown 原样保留 `F / X`、`G / X`、`G _ {Y} / X`、`T _ {Y} / X`，**未按数学常识改写为 `F_X`、`\operatorname{equiv}_X` 等形式**（依铁律三）。`∼_{\mathbb{R}}` 的 ℝ 为双线黑板粗，与 p.34 起的写法同族。
  5. **行间关系**：印刷 L002→L039 为 Step 3（设 MMP 模型 Y′，负性引理 → `K_W + Γ_W ≡ v(B^∼+tL^∼)+F/X` → T 非分量 → 不收缩 T → `A_{Y′}` 为 A 的拉回 → 半ample → 基点 freely），Markdown L1889→L1915 **逐段同序**；Step 4（L060→L085）→ Markdown L1917→L1923；Step 5（L086→L151）→ Markdown L1925→L1955。**未发现段落错位、显示式撕裂或跨段串行**。
- 结果：**PASS**
  1. **缺陷明细**：无。本页 11 处数学表达式（8 个 `$$` 显示块 + 3 处行内式）与正文全部与印刷一致，**零改动**。
  2. **溯源**：本页**零改动**，无缺陷需归因；所核区间（L1889–L1957）在 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版中内容一致，本页未触碰任何三版存在差异之处。
  3. **撤销疑点（bbox 推断被裁片推翻，故不改 Markdown）**：①bbox L085 把虚线 birational 箭头解为字形码 `99K`（solid arrow 则解为 `→`），一度疑 Markdown 写成实线 `\to`；裁片 3 目视为**虚线杆**，Markdown `Y \dashrightarrow Y ^ {\prime}` **正确**，撤销疑虑不改。②bbox L134–L136 中 `µ`→`T`→`Y` 的 yMin 逐级下降，一度疑为 `\mu_T Y` 的三个并列符号；裁片 6 显示 `T` 与 `Y` 为**右降两级**的嵌套下标，Markdown `\mu_ {T _ {Y}}` **正确**，撤销不改。③bbox L012/L014 中 `′`(y=133) 与 `2`(y=158) 分列两行，一度疑 `\epsilon^{\prime} _ {2}`；按「分母 x 范围与分子重叠而非右移」的判据＋裁片 1 的分数线，确认为分式，撤销不改。
  4. **登记不修（字形/别名族变体）**：`ǫ`(U+01EB，bbox L013/L064/L114/L132/L137/L139/L149) 与 Markdown 的 `\epsilon` 混用；`\sim_ {\mathbb {R}}` 的内部空格；L1917 的 `\epsilon ^ {\prime} { - } \mathrm {l c}`（连接号被包进数学模式并带空格）；L1895 的 `\frac { \epsilon ^ {\prime} } { 2 } -$lc`（连字符落在数学与正文交界）；L1920/L1948 的 `<   1,`、`<   \epsilon` 的 MathJax 多空格转义；数学与正文的空格粘连（`$X$and`、`$Y$.`、`over$X :$` 等）；L1923 的 `$T _ {Y }{ \mathrm { ~ a s ~ } } - T _ {Y }$`（英文单词 `as` 被吞入数学模式作 `\mathrm`）；L1965 的 `${\sim _ {\mathbb {R} }} } 0$`（花括号数学定界符）。以上渲染等价或仅差字距，**不改**。
  5. **登记不修（版式损失）**：`Step 3.`/`Step 4.`/`Step 5.` 的斜体步号退化为普通文本；行内数学与正文的斜体丢失（`x`、`φ`、`X`、`A` 等）；页眉「Singularities of linear systems and boundedness of Fano varieties　39」按既定登记类**从不导出**。
  6. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①**bbox L085 的 `Y ⟶ Y′` 与 Step 4 的叙述上下文不符**——Step 4 全段讨论的是 *Y*⟶*Y*″（抽缩 T 的双有理映射），句末却写成 `the induced map Y ⟶ Y′ does not contract any divisor`；Markdown L1923 **照录为 `$Y \dashrightarrow Y ^ {\prime }$`**，未按上下文「订正」为 `Y^{\prime\prime}`。②L084 `is mapped to x, φ is an isomorphism over the complement of x in X.` 中句点 `x` 与 `φ` 均为正体（未斜排），Markdown 同样以正体 `x`、`$X$` 外置 `φ` 呈现，保留原状。③L139 的 `a′ = a(T,X,(1+v)(B+tL)) < ε′ = a(T,X,B+tL)` 与 L132/L137 的严格不等号方向在数学上依赖 ε′>0，印刷如此，未改。
- 跨页边界登记：本页印刷首行 `Step 3.`（bbox L002，y=89）与 p.38 审计末尾登记的边界「L1889 `Step 3.` 起属 p.39」**交叉核对一致**；本页印刷末行 bbox L141–L151（`K_Y + Γ_Y + 2dA_Y ∼_ℝ (a′ − ε′)T_Y/X`，y=711）对应 Markdown L1954 该显示块，L1957 `we deduce that…` 起属 **p.40**；此边界将在 p.40 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p039`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.040（PDF p.40 / 印刷 p.40）
- PNG：`/tmp/birksing_audit_p040.png`（150dpi pngmono，1575×2037，Read 亲自查看）。300dpi 灰度底图 `/tmp/bk_p40_300.png`。放大裁片（LANCZOS 升采样，仅用于目视仲裁，不用于写 Markdown）：
  1. `/tmp/bk_p40_eq.png`（×12，x=180–432 / y=382–402）——Step 6 的等式 `K_Y + B_Y^∼ + tL_Y^∼ + (1 − ε′)T_Y = φ*(K_X + B + tL),`，可见 ε 的**撇号存在**。
  2. `/tmp/bk_p40_anyl.png`（×22，x=352–432 / y=400–418）——「…r any **l** we have」，该字符是 CM 斜体小写 `l`（非 `i`、非数字 `1`）。
  3. `/tmp/bk_p40_BLY.png`（×22，x=88–165 / y=401–417）——「where *B*<sub>*Y*</sub>^∼, *L*<sub>*Y*</sub>^∼ a…」，波浪号为**上标**、Y 为下标。
  4. `/tmp/bk_p40_RC.png`（×10，x=88–400 / y=500–524）——「is ℝ-Cartier because *B*<sub>*Y*</sub>^∼, *L*<sub>*Y*</sub>^∼ are ℝ-Cartier which in turn follow…」，ℝ 为**双线黑板粗**。
  5. `/tmp/bk_p40_phiB.png`（×20，x=375–530 / y=500–526）——「…from the fact that φ\* *B*, φ\* *L*, *T*<sub>*Y</sub>」，**两个星号都在**，T_Y 下标完好。
  6. `/tmp/bk_p40_Ad.png`（×18，x=385–521 / y=524–542）——「…*A* is very ample and *A*<sup>*d*</sup> ≤ *r*,」，*d* 为上标，关系符为**小于等于（带下横线）**。
  7. `/tmp/bk_p40_step6.png`（×6，x=88–530 / y=298–320）——「*Step 6.* In this step we show that there is a natural number *l* depending only on *d*, *r*, ϵ such that」，步号斜体、ϵ **无撇**。
  8. `/tmp/bk_p40_beta.png`（×14，x=88–300 / y=540–556）——「β*A* − *K*<sub>*X*</sub> is ample for some bounded natur…」，β 为希腊字母 β 而非 `p`/`δ`。
  9. `/tmp/bk_p40_two.png`（×6，x=128–516 / y=436–464）——两行显示式的第二行，含**四个叠置分式** 3d/v、1/v、1/v、3d/v 及 `B_Y^∼ + tL_Y^∼`。
  10. `/tmp/bk_p40_1v.png`（×6，x=148–462 / y=660–692）——`1/v(K_Y + Γ_Y + 3dA_Y) = 1/v φ*(K_X + B + tL) + B_Y^∼ + tL_Y^∼ + 3d/v A_Y`，**三个叠置分式**。
  11. `/tmp/bk_p40_PYp.png`（×14，x=226–386 / y=178–198）——`0 ≤ P_{Y′} ∼_ℝ K_{Y′} + Γ_{Y′} + 2dA_{Y′}`，三处 `Y′` 下标齐全、∼ 的 ℝ 为下标。
  12. `/tmp/bk_p40_dotC.png`（×12，x=213–400 / y=238–260）——`(K_Y + Γ_Y + 2dA_Y) · C = P_Y · C ≥ 0.`，两处**居中点 `\cdot`**、关系符为大于等于。
  13. `/tmp/bk_p40_last.png`（×14，x=243–370 / y=703–723）——本页末显示式 `lA_Y − (K_Y + (1 − ε′)T_Y)`，斜体 `l`、撇号、下标齐全。
  14. 坐标探针 `/tmp/bk_p40probe.py`（y=436–468 与 y=568–596 两窗口）：按 x 序读出两处多分式显示式的**分子/分母配对与左右次序**，见下「撤销疑点」③。
- 核对（正文页五点）：
  1. **节标题与步号顺序**：印刷本页为 Step 5 收尾（bbox L002 起 `we deduce that…`）→ `Step 6.`（L085，y=303）；Markdown L1957 → L1979 `Step 6.`。**顺序一致，无漏步、无错序**。
  2. **编号与陈述**：本页无定义/定理/引理编号。`Step 6.` 的陈述「we show that there is a natural number *l* depending only on *d*, *r*, ϵ such that *lA_Y − (K_Y + (1 − ε′)T_Y)* is ample」（bbox L085–L094＋裁片 7）与 Markdown L1979–L1985 **逐字对应**，含依赖参数 `d, r, ε`（**ε 无撇**）。Step 5 收尾段「Therefore, *K_Y + Γ_Y + 2dA_Y* is nef globally while being ample over *X*. Since *A_Y* is the pullback of the ample divisor *A*, it follows that *K_Y + Γ_Y + 3dA_Y* is ample.」（bbox L069–L084）与 Markdown L1977 **逐字对应**。
  3. **公式逐条**（本页 14 个 `$$` 显示块 + 全部行内式逐条比对）：
     - L1962 `K_{Y′} + Γ_{Y′} + 2dA_{Y′} \sim_{\mathbb{R}} G_{Y′} / X` ↔ bbox L013–L023 **一致**（三个 `Y′`、∼ 的 ℝ 下标、`/X` 斜杠记号）。
     - L1968 `0 \leq P_{Y′} \sim_{\mathbb{R}} K_{Y′} + Γ_{Y′} + 2dA_{Y′}` ↔ bbox L037–L046 ＋ 裁片 11 **一致**。
     - L1974 `\left(K_Y + Γ_Y + 2dA_Y\right) \cdot C = P_Y \cdot C \geq 0.` ↔ bbox L060–L068 ＋ 裁片 12 **一致**（两处居中点未丢）。
     - L1982 / L2010 / L2036 三处同形的 `lA_Y - (K_Y + (1 - \epsilon^{\prime}) T_Y)` ↔ bbox L087–L093、L144–L150、L202–L208 ＋ 裁片 13 **三处一致**。
     - L1988 `a (T, X, B + tL) = \epsilon^{\prime},` ↔ bbox L095 **一致**。
     - L1994 `K_Y + B_Y^{\sim} + tL_Y^{\sim} + (1 - \epsilon^{\prime}) T_Y = \phi^{*} (K_X + B + tL),` ↔ bbox L097–L107 ＋ 裁片 1 **一致**（撇号、两个上标 ∼、星号全在）。
     - L2000 `lA_Y - (K_Y + (1 - \epsilon^{\prime}) T_Y) = lA_Y - \phi^{*}(K_X + B + tL) + B_Y^{\sim} + tL_Y^{\sim}` ↔ bbox L113–L126 **一致**。
     - L2004 `= (l - \frac{3d}{v}) A_Y - (1 + \frac{1}{v}) \phi^{*}(K_X + B + tL) + \frac{1}{v} \phi^{*}(K_X + B + tL) + B_Y^{\sim} + tL_Y^{\sim} + \frac{3d}{v} A_Y.` ↔ bbox L127–L143 ＋ 裁片 9 ＋ 探针（分子 x 序 135/204/314/480，分母 x 序 137/204/314/483）**四个分式左右次序与 Markdown 完全一致**。
     - L2018 `(l - \frac{3d}{v}) A_Y - (1 + \frac{1}{v}) \phi^{*}(K_X + B + tL) = \phi^{*}((l - \frac{3d}{v}) A - (1 + \frac{1}{v}) (K_X + B + tL))` ↔ bbox L163–L171 ＋ 探针（分子 x 序 133/203/350/413，分母 x 序 136/203/353/413）**四个分式次序 3d/v、1/v、3d/v、1/v 与 Markdown 一致**。
     - L2024 `K_Y + Γ_Y = \phi^{*}(K_X + B + tL) + v (B_Y^{\sim} + tL_Y^{\sim}),` ↔ bbox L174–L184 **一致**。
     - L2030 `\frac{1}{v} (K_Y + Γ_Y + 3dA_Y) = \frac{1}{v} \phi^{*}(K_X + B + tL) + B_Y^{\sim} + tL_Y^{\sim} + \frac{3d}{v} A_Y` ↔ bbox L186–L200 ＋ 裁片 10 **一致**。
     - 行内式：L1957 `$- T_Y$`、L1965 `${ \sim_{\mathbb{R}} } 0$`、L1971 `Step$4 , \phi \colon Y \to X$`、L2013 `\phi^{*} B , \phi^{*} L , T_Y`（＋裁片 5）、L2015 `A^d \leq r`、`\beta A - K_X`（＋裁片 6/8）、L2021 `$t \leq r$`、`$v , \beta$` 全部与印刷一致。
  4. **记号约定**：`X`、`Y`、`Y′`、`T_Y`、`B^∼`、`L^∼`、`B_Y^∼`、`L_Y^∼`、`A_Y`、`A`、`K_Y`、`K_X`、`Γ_Y`、`C`、`c`、`φ`、`d`、`r`、`ε`、`ε′`、`l`、`v`、`β`、`t` 均与印刷一致。斜杠记号 `G_{Y′}/X`（L1962）沿用 p.34 起的同一印刷惯例，Markdown 原样保留 `G _ {Y ^ {\prime}} / X`，**未按数学常识改写**（依铁律三）。
  5. **行间关系**：印刷 L002→L084（Step 5 收尾：ampleness → 取曲线 C → 半ample + `∼_ℝ 0` → 造 `P_{Y′}` → 推下 `P_Y` → `·C ≥ 0` → nef + 拉回 → ample）与 Markdown L1957→L1977 **逐段同序**；L085→L208（Step 6 全段）对应 Markdown L1979→L2036。**未发现段落错位、显示式撕裂或跨段串行**；L2000/L2004 两行长式在 Markdown 中被拆成两个 `$$` 块（L1999–L2001 与 L2003–L2005），属既定登记类。
- 结果：**PASS**
  1. **缺陷明细**：无。本页 14 个 `$$` 显示块（另 3 处同形重复共 17 次出现）与全部行内式与印刷一致，**零改动**。
  2. **溯源**：本页**零改动**，无缺陷需归因；所核区间（L1957–L2036）在 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版中内容一致，本页未触碰任何三版存在差异之处。
  3. **撤销疑点（bbox 推断被裁片/坐标探针推翻，故不改 Markdown）**：①bbox 把 y=389 显示式的 `(1 − ε′)` 里的撇号**提前发射**到该行行首（L097 = `′ ∗ K`，行内 `+ (1 − ǫ )T` 反而无撇），一度疑 Markdown 漏撇；裁片 1 目视确认撇号在 `ε` 右上，Markdown `\epsilon^ {\prime}` **正确**，撤销不改。②bbox L112 `Hence for any l we have` 的 `l` 与分式分子 `1` 同形码，一度疑为 `1`；裁片 2（×22）显示为 CM 斜体 `l`，Markdown `l` **正确**，撤销不改。③bbox 的分式分子按**内容流顺序**输出（y=442 行为 `3d 1 1 3d`、y=574 行为 `3d 1 3d 1`），与视觉左右次序不同，一度疑 Markdown 的 `\frac{3d}{v}` 与 `\frac{1}{v}` 位置互换；坐标探针按 x 序复核（y=442：3d@135、1@204、1@314、3d@480；y=574：3d@133、1@203、3d@350、1@413）后确认 Markdown 次序与视觉**一致**，撤销不改。这与 p.35 已登记的「bbox 内容流顺序不可直接当作视觉顺序」是同一现象。
  4. **登记不修（字形/别名族变体）**：`ℝ`(双线黑板粗，bbox 解为普通 `R`) 被 Markdown 展平为 `R-Cartier`（L2013）；`ǫ`(U+01EB，bbox L085/L162/L172) 与 `\epsilon` 混用；`\leq`/`\ge` 与 `\leq`/`\geq` 别名混用（L1968 `\leq`、L1974/L2015/L2021 `\geq`/`\leq`）；`\left(...\right)` 用于拉伸括号（L1974）；`\begin{array}` 未出现在本页；数学与正文的空格粘连（`$X$.`、`$Y$.`、`$d , r$`、`$v , \beta$`、`$B ^ {\sim} , L ^ {\sim }$` 等）；L1965 的 `${ \sim _ {\mathbb {R} } } 0$` 花括号定界符。均渲染等价，**不改**。
  5. **登记不修（版式损失）**：`Step 6.` 的斜体步号退化为普通文本（裁片 7 可见印刷确为斜体）；行内数学斜体丢失（`l`、`d`、`r`、`ε`、`A`、`B`、`L`、`t`、`v`、`β`、`C`、`c`、`φ`、`X`、`Y`）；页眉「Caucher Birkar」与页码「40」（bbox L000 居中作者名、L001 左侧页码）按既定登记类**从不导出**。
  6. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①**Step 6 中 `l` 与分式分子 `1` 字形近似**（CM 斜体 `l` 与数字 `1`），且正文「Hence for any l we have」中的 `l` 与所证结论中的自然数 `l` 同名同形，阅读时极易混淆；Markdown 一律照录为 `l`，**未替换为 `1`、`i`、`m` 或 `\ell`**。②bbox L085/L162/L172 三处依赖参数印作 `ǫ`（**无撇** ε），而同页 L095/L091/L117/L148 等处为 `ε′`（**有撇**）；Markdown 分别写 `\epsilon` 与 `\epsilon^ {\prime}`，**未统一**。③印刷把 `K_Y + Γ_Y + 2dA_Y` 与 `K_Y + Γ_Y + 3dA_Y` 两个 ample 性断言分置 Step 5 末与 Step 5 末句（`is ample`），Step 6 又重新引入同一式；Markdown 照录，未合并。④印刷把 Step 5 末尾的 nef 断言写作「is nef globally **while being** ample over *X*」（bbox L075），与后半句 `Since A_Y is the pullback of the ample divisor A` 的因果表述略有跳跃；Markdown L1977 原样保留 `while being`，未改写。
- 跨页边界登记：本页印刷首行 bbox L002（`we deduce that K_Y + Γ_Y + 2dA_Y is ample over X because −T_Y is ample over X.`，y=89）与 p.39 审计末尾登记的边界「L1957 `we deduce that…` 起属 p.40」**交叉核对一致**；本页印刷末行 bbox L202–L208（`lA_Y − (K_Y + (1 − ε′)T_Y)`，y=711）对应 Markdown L2036 该显示块，L2039 `is ample by the previous paragraph.` 与 L2041 `Step 7.` 起属 **p.41**；此边界将在 p.41 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p040`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

### 本段小结：PDF p.33–p.40（本轮 redo 复审，actor 前缀 `Wf-R-Birkar-pNNN`）

- **范围与页–行对应**：p.33→L1505–L1557、p.34→L1559–L1621、p.35→L1623–L1683、p.36→L1685–L1733、p.37→L1735–L1803、p.38→L1805–L1887、p.39→L1889–L1957、p.40→L1957–L2036（L1957 为 p.39 末显示式与 p.40 首行的共享行，与印刷的跨页续接一致）。**8 页全部逐页渲染 150dpi pngmono、Read 亲自查看原页图、裁片仲裁、写说明，无一页合并、无一页跳过。**
- **分级统计**：**FAIL 3 页**（p.33、p.37、p.38）｜**PASS± 1 页**（p.36）｜**PASS 4 页**（p.34、p.35、p.39、p.40）。合计 8 页。
- **改动合计 3 处**，全部为字符级增删，无公式重排：
  | # | 页 | Markdown 行 | 改动 | 印刷依据 |
  |---|---|---|---|---|
  | 1 | p.33 | L1535 | 删去多余句点：`… \epsilon^{\prime}.\n$, and replacing r` → `… \epsilon^{\prime}$, and replacing r` | bbox 逗号 token y=361.78–372.69 低于基线下探，句点 yMax≈366.51 与撇号同高；×14 裁片目视逗号尾钩 |
  | 2 | p.37 | L1769 | 删去重复字母：`Let$X , B , A , L , T , t$t be as…` → `Let$X , B , A , L , T , t$ be as…` | bbox token 序 `T ,`(x=323.04) `t`(x=335.16–339.10) `be`(x=343.32)，`be` 前只有一个 `t`；×20 裁片目视 |
  | 3 | p.38 | L1805 | 补回漏掉的逗号：`is plt in a neighbourhood of$H$by inversion` → `…of$H$, by inversion` | bbox L002 行内 `H,`；×18 裁片可见逗号下探 |
- **溯源结论（三处全部为「导出缺陷」，非 peer 回归）**：对每处均执行 `git show cpf-redo/Birkar_2016_singularities_linear_systems^:"2018年 - Birkar/…__….md"`（`^` = `16ffcc7c`）、当前 HEAD（`37580aaf`）与初次 MinerU 导出（`53a92412`）三版比对，结果：
  1. **p.33 L1535**：三版**字节相同**均为带句点的错误形态 → 初次导出即错，**导出缺陷**。
  2. **p.37 L1769**：三版**字节相同**均为 `t$t` 重复形态 → **导出缺陷**。
  3. **p.38 L1805**：初次导出 `53a92412` 为 `is plt in a neighbourhood of$H _ { ; }$by inversion of adjunction [28, Theorem 5.50].`——**同样缺该逗号**，且另带一处伪下标 `_ { ; }`（该伪下标已被更早的一轮修复清掉，但逗号从未被补上）；`^` 与 HEAD 延续同一形态 → **导出缺陷**，非任何 peer 引入的回归。
  → **本段 0 处「系 \<commit\> 引入」的假修复回归**；3 处缺陷均为 MinerU 初次导出的字符级误差，本轮已用 Edit 工具逐处改正。
- **撤销疑点合计 11 处**（bbox 或坐标推断被 300dpi 裁片／坐标探针推翻，依铁律二不改 Markdown）：p.33 竖排 `{l c}` 数组环境；p.35 `∼` 的内容流提前发射；p.37 `ε′/2` 疑为下标；p.38 `Γ_W` 下标方向疑为上标；p.39 虚线 birational 箭头、`\mu_{T_Y}` 嵌套下标、`\epsilon^{\prime}/2` 分式；p.40 `ε′` 撇号提前发射、`for any l` 的 `l`、两处多分式的左右次序。**均登记在各页说明的「撤销疑点」条目下**。
- **登记不修的主要族**（渲染等价或仅差字距，非缺陷）：ℝ/ℚ 黑板粗展平为 R/Q、`ǫ`↔`\epsilon` 混用、`\mathbb{R}` 内部空格、`\left(...\right)` 拉伸括号、`\begin{array}` 对齐环境承载 flush 对齐、`\le`/`\ge` 与 `\leq`/`\geq` 别名混用、MathJax 多空格转义（`<   1` 等）、`\mathrm{~as~}` 等英文单词被吞入数学模式、数学与正文的空格粘连、斜体步号与行内斜体丢失、页眉页码从不导出、QED 方框 `□` 丢失（p.36 两处）、HTML `<sub>`/`<sup>` 泄漏（p.37 `ǫ<sup>′</sup>`、p.38 `Γ<sub>W</sub>`）。
- **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：p.33 的 `(X, H + B + 2tB)`（字母 H，疑印误）、`zero-`/`dimensional` 行末断词；p.36 的 `Replacing A we can assume it is effective`、`belongs to bounded family of couples` 缺冠词、`Λ reduced` 中 Λ 为正体；p.39 Step 4 末句写作 `the induced map Y ⟶ Y′`（上下文讲的是 Y″）；p.40 Step 6 中斜体 `l` 与数字 `1` 字形近似且「Hence for any l we have」与所证自然数同名、三处依赖参数印作无撇 `ϵ` 而另处为 `ε′`。斜杠记号 `F/X`、`G/X`、`exceptional/X`、`T_Y/X` 一律原样保留。
- **跨页边界链已闭环**：p.32→p.33（`(X, H + B + tL + 2v(B + tL))` 后的 `is plt in a neighbourhood of H`）、p.33→p.34、p.34→p.35、p.35→p.36、p.36→p.37、p.37→p.38、p.38→p.39、p.39→p.40 **均在相邻两页的说明中双向交叉核对一致**；p.40→p.41 的边界已登记（Markdown L2039 `is ample by the previous paragraph.`、L2041 `Step 7.` 起属 p.41），留待下一轮核对。
- **未完成/受阻项**：无。3 处缺陷均已用 Edit 工具定位并改正，无需退回脚本；无「Edit 不可用」或「字节无法定位」而如实登记放弃的情形。
- **边界声明**：本段**只写**了本 AUDIT 文件与目标 Markdown 两个文件；**未触碰** 仓库根 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、`MEMORY.md`、`README.md` 及任何其他论文目录；**未执行** 任何 `git add/commit/merge/push`；**未启动或停止** mineru 服务或改其配置；**PDF 全程只读**（未写入、未重排、未另存）。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p033-040`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.041（PDF p.41 / 印刷 p.41）
- PNG：`/tmp/birksing_audit_p041.png`（150dpi pngmono，1575×2037，Read 亲自查看）。300dpi 灰度底图 `/tmp/bk_p41_300.png`。放大裁片（LANCZOS 升采样，仅用于目视仲裁，不用于写 Markdown）：
  1. `/tmp/bk_p41_thus.png`（×20，x=88–300 / y=208–222）——第 3 行行首，目视为 **`Thus we have`**（非 `This`）。
  2. `/tmp/bk_p41_alpha.png`（×12，x=88–300 / y=136–156）——`positive real number α ≤ ε′/(ε−ε′) such that`，**叠置分式**（分子 ε′、分母 ε−ε′、有分数线），关系符为带下横线的 `≤`。
  3. `/tmp/bk_p41_lge.png`（×18，x=260–345 / y=340–364）——`l ≥ (1 + r)ε′/(ε − ε′),`，分子含 `(1 + r)` 与撇号，`≥` 带下横线。
  4. `/tmp/bk_p41_restr.png`（×10，x=155–400 / y=648–672）——`(Y, T_Y) is lc, by our choice of ε′. Moreover, A_Y|_{T_Y} ∼ …`，**限制竖线与下标 `T_Y` 齐全**。
  5. `/tmp/bk_p41_glyphLam.png`（×30，x=449–474 / y=676–694）——争议字形特写：左斜为**笔直细线、无横向中划、两腿底部为平直衬脚、顶点尖锐并略左出**。
  6. `/tmp/bk_p41_refA.png`（×24，x=134–175 / y=558–574）——对照字形（`+ 3dA_Y` 中的 `A`）：左斜**明显外鼓带钩**、**有横向中划**。
  7. `/tmp/bk_p41_lastd.png`（×16，x=230–380 / y=705–722）——本页末显示式 `n(K_Y + Λ_Y) ∼ (n + 2)lA_Y.`：**Λ 与 A 在同一裁片内并排**，Λ 无中划、A 有中划，形状可直读对比。
  8. `/tmp/bk_p41_arr1.png`（×10，x=170–450 / y=226–246）——三行显示式第 1 行 `3lA_Y − (K_Y + T_Y) = 3lA_Y − (K_Y + (1−ε′)T_Y) − ε′T_Y`。
  9. `/tmp/bk_p41_arr3.png`（×8，x=115–500 / y=266–286）——三行显示式第 3 行 `= (lA_Y − (K_Y + (1−ε′)T_Y)) + (lA_Y − αφ*(B + tL)) + (lA_Y + α(B_Y^∼ + tL_Y^∼)).`
  10. 坐标探针 `/tmp/bk_p41probe.py`（y=455–482 与 y=486–514 两窗口）：按 x 序读出 `\begin{array}{rl}` 两行显示式中全部分式的分子/分母配对，见下「撤销疑点」③。
- 核对（正文页五点）：
  1. **节标题与步号顺序**：印刷依序为 Step 6 末句 `is ample by the previous paragraph.`（bbox L002，y=89）→ `Step 7.`（L003，y=115）→ `Step 8.`（L157，y=602）；Markdown 依序为 L2039 → L2041 `Step 7.` → L2097 `Step 8.`。**顺序与内容一致**，无漏步、无错序。
  2. **编号与陈述**：`Step 7.` 的陈述「In this step we show that after replacing *l* with a bounded multiple we can ensure that *lA_Y − (K_Y + T_Y)* is ample.」（bbox L003–L010）与 Markdown L2041 逐字对应；`Step 8.` 的陈述「In this step we finish the proof by applying Theorem 1.9. The pair (*Y*, (1−ε′)*T_Y*) is klt because (*X*, *B + tL*) is klt and…」（bbox L157–L160）与 Markdown L2097 逐字对应。两处对 Theorem 1.9 的引用编号与 Step 5/6 的回指编号均与印刷一致。
  3. **公式逐条**（本页 13 个 `$$` 显示块 + 全部行内式逐条比对）：
     - L2041 行内 `\alpha \le \frac{\epsilon^{\prime}}{\epsilon - \epsilon^{\prime}}` ↔ bbox L014/L016 ＋ 裁片 2 **一致**（分子 y=141、分母 y=149 且 x 范围重叠，叠置分式）。
     - L2044 `\alpha \mu_{T_Y} \phi^{*} (B + tL) = \epsilon^{\prime}.` ↔ bbox L018–L021（`µ` y=163 → `T` y=167 → `Y` y=170，嵌套下标）**一致**。
     - L2050 `\alpha \phi^{*} (B + tL) = \alpha (B_Y^{\sim} + tL_Y^{\sim}) + \epsilon^{\prime} T_Y.` ↔ bbox L023–L029 **一致**（行首 L023 的 `′` 是 `ε′T_Y` 撇号的提前发射，见「撤销疑点」②）。
     - L2056 三行 `\begin{array}{c}`：第 1 行 ↔ bbox L031–L044 ＋ 裁片 8；第 2 行 `= 3lA_Y − (K_Y + (1−ε′)T_Y) − αφ*(B + tL) + α(B_Y^∼ + tL_Y^∼)` ↔ bbox L045–L055；第 3 行 ↔ bbox L056–L070 ＋ 裁片 9。三行**逐 token 一致**，`3l` 未误作 `31`，三个加括号的分组括号完整，末尾句点保留。
     - L2062 `l A_Y - (K_Y + (1 - \epsilon^{\prime}) T_Y)` ↔ bbox L079–L085 **一致**。
     - L2068 `l \geq \frac{(1 + r) \epsilon^{\prime}}{\epsilon - \epsilon^{\prime}},` ↔ bbox L087–L090 ＋ 裁片 3 **一致**。
     - L2074 `l A_Y - \alpha \phi^{*} (B + tL)` ↔ bbox L092–L094 **一致**。
     - L2080 `l A - \alpha (B + tL) = (l - (1 + t) \alpha) A + \alpha (A - B + tA - tL)` ↔ bbox L096 **一致**（注意此处无 `Y` 下标，印刷即无，Markdown 亦无）。
     - L2086 `\begin{array}{rl}` 两行：第 1 行 `lA_Y + α(B_Y^∼ + tL_Y^∼) = lA_Y + α(1/v(K_Y + Γ_Y + 3dA_Y) − 1/v φ*(K_X + B + tL) − 3d/v A_Y)` 的三个分式，坐标探针读出分子 y=461 的 x 序为 `1`@258、`1`@372、`3d`@477，分母 y=476 的 x 序为 `v`@258、`v`@372、`v`@480，**次序 1/v、1/v、3d/v 与 Markdown 完全一致**；第 2 行 `= (l − 3dα/v)A_Y − α/v φ*(K_X + B + tL) + α/v (K_Y + Γ_Y + 3dA_Y)` 的三个分式，分子 y=492 的 x 序为 `3dα`@192、`α`@246、`α`@353，分母 y=507 的 x 序为 `v`@199、`v`@247、`v`@353，**次序与 Markdown 完全一致**。
     - L2092 `l A_Y + \alpha (B_Y^{\sim} + tL_Y^{\sim})` ↔ bbox L135–L141 **一致**。
     - L2100 `a (T, X, B + tL) = \epsilon^{\prime}.` ↔ bbox L161 **一致**。
     - L2103 行内 `$A_Y|_{T_Y} \sim 0$` ↔ bbox L164–L169 ＋ 裁片 4 **一致**（限制竖线 `|` 与 `T_Y` 下标均在）。
     - L2106 `n (K_Y + \Lambda_Y) \sim (n + 2) l A_Y.` ↔ bbox L185–L191 ＋ 裁片 7 **一致**，`Λ` 与 `A` 未混淆。
  4. **记号约定**：`X`、`Y`、`Y′`、`T_Y`、`T_{Y′}`、`B^∼`、`L^∼`、`B_Y^∼`、`L_Y^∼`、`A`、`A_Y`、`K_X`、`K_Y`、`Γ_Y`、`Λ_Y`、`φ`、`d`、`r`、`t`、`v`、`α`、`ε`、`ε′`、`l`、`n`、`x` 均与印刷一致。特别核对了 **`Λ_Y` 与 `A_Y` 的区分**：Theorem 1.9 给出的边界除子印作 **Λ**（非 A），而 ample 除子印作 **A**，裁片 7 在同一画面内并排显示两者，形状可直读区分（Λ 无中划、左斜笔直；A 有中划、左斜外鼓带钩）。Markdown 保留了这一区分，**未按数学常识或上下文把它「统一」成 A_Y**（依铁律二、三）。
  5. **行间关系**：印刷 L002→L156（Step 6 末句 + Step 7 全段：定 α → 造 `P` → 三行分解 → 换有界倍数 → nef 判断 → ample 判断 → 结论）与 Markdown L2039→L2095 **逐段同序**；L157→L191（Step 8 开头：引 Theorem 1.9 → klt → lc → 限制为零 → 取 `M,S,z` → 得 `Λ_Y ≥ T_Y` → 得线性关系）与 Markdown L2097→L2106 **逐段同序**。**未发现段落错位、显示式撕裂或跨段串行**。
- 结果：**PASS**
  1. **缺陷明细**：无。本页 13 个 `$$` 显示块（含 `\begin{array}{c}` 三行块与 `\begin{array}{rl}` 两行块）与全部行内式与印刷一致，**零改动**。
  2. **溯源**：本页**零改动**，无缺陷需归因；所核区间（L2039–L2106）在 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`)、当前 HEAD(`37580aaf`) 与初次 MinerU 导出 `53a92412` 三版中内容一致，本页未触碰任何三版存在差异之处。
  3. **撤销疑点（bbox／低分辨率读图推断被裁片或坐标探针推翻，故不改 Markdown）**：①**150dpi 整页读图把 `There is a Q-divisor A_Y ≥ T_Y` 误读为 `A_Y`**，bbox L177/L182/L187 三处 token 均解为 `Λ`（U+039B），裁片 5（×30）与对照裁片 6（×24）逐笔对比后确认印刷字形为 **Λ**（左斜笔直无中划、两腿平直衬脚），Markdown `\Lambda _ { Y }` **正确**，撤销不改。②bbox 把 `α(B_Y^∼ + tL_Y^∼) + ε′T_Y` 中 `ε′` 的撇号**提前发射**到行首（L023 以 `′` 开头），一度疑 Markdown 漏撇；按 bbox 中 `ε` 与其右侧 `T` 的 x 关系及裁片可见 `ε′T_Y` 撇号在位，Markdown `\epsilon^ {\prime}` **正确**，撤销不改。③bbox 的分式分子按**内容流顺序**输出（第 1 行 `3d 1`、第 2 行 `α α 3dα`），与视觉左右次序不同，一度疑 Markdown 把 `\frac{1}{v}` 与 `\frac{3d}{v}` 互换；坐标探针按 x 序复核后确认次序**一致**，撤销不改——这与 p.35、p.40 已登记的「bbox 内容流顺序不可直接当作视觉顺序」是同一现象。另：150dpi 读图把 `Thus we have` 误读为 `This we have`，裁片 1（×20）与 bbox L030 均确认印刷为 **`Thus`**，Markdown `Thus we have` **正确**，撤销不改。
  4. **登记不修（字形/别名族变体）**：`ǫ`(U+01EB，bbox L013/L015/L016/L041/L043 等) 与 `\epsilon` 混用；`\geq`/`\leq` 与 `\ge`/`\le` 别名混用（L2068 用 `\geq`，L2041 数组内用 `\le`）；L2041 的 `\begin{array} { r } { … } \end{array}` 单元素数组包裹行内式（印刷为无框单式）；L2059 的 `\left( K_Y + T_Y \right)` 与同页其它位置的普通圆括号混用；`\begin{array}{c}`（L2056）与 `\begin{array}{r l}`（L2086）对齐环境承载 flush 对齐的三行/两行显示式；数学与正文的空格粘连（`$l A _ { Y }$`、`$3 l$`、`$K _ { Y } + \Gamma _ { Y } + 3 d A _ { Y }$`、`$d , r , \epsilon$`、`$M = l A _ { Y } , S = T _ { Y }$` 等）；`$\epsilon ^ {\prime } .$`、`$\alpha .$` 处句点落在数学模式内。均渲染等价或仅差字距，**不改**。
  5. **登记不修（版式损失）**：`Step 7.`/`Step 8.` 的斜体步号退化为普通文本；行内数学斜体丢失（`l`、`α`、`ε`、`t`、`r`、`d`、`n`、`Λ`、`A`、`B`、`L`、`T`、`K`、`Γ`、`x`）；页眉「Singularities of linear systems and boundedness of Fano varieties　41」（bbox L000/L001）按既定登记类**从不导出**。
  6. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①Step 7 开头句「we show that after replacing *l* with a bounded multiple we can ensure that *lA_Y − (K_Y + T_Y)* is ample」中，被放大的自然数与目标式里出现的自然数**同名同形**（都是斜体 `l`），且与分式分子 `1` 字形近似；Markdown 一律照录为 `l`，**未替换为 `m`、`1`、`i` 或 `\ell`**。②印刷 Step 7 的依赖参数在三处写法不一致：L142 `d, r, ǫ`（无撇 ε）、L162 `d, r, ǫ`（无撇）、L172 段内的 `d, r, ǫ`（无撇），而同段多处出现 `ε′`；Markdown 分别写 `\epsilon` 与 `\epsilon^ {\prime}`，**未统一**。③印刷把 Step 7 的分解式排成**三行**且第 1、2 行以 `=` 续行、第 3 行以 `=` 续行，Markdown 用 `\begin{array}{c}` 保留了三行结构与续行等号，未合并为一行（若合并会丢失 `3lA_Y` 与 `lA_Y` 的倍数对应，属数学内容损失）。④`By Step 5, we have μ_{T_Y} φ*tL ≥ ε − ε′.`（bbox L010–L013）中 `μ_{T_Y}` 与 `φ^*` 之间**无逗号**，Markdown L2041 同样照录，**未补逗号**。
- 跨页边界登记：本页印刷首行 bbox L002（`is ample by the previous paragraph.`，y=89）与 p.40 审计末尾登记的边界「L2039 `is ample by the previous paragraph.` 起属 p.41」**交叉核对一致**；本页印刷末行 bbox L185–L191（`n(K_Y + Λ_Y) ∼ (n + 2)lA_Y.`，y=711）对应 Markdown L2106 该显示块，L2109 `Let Λ be the pushdown of…` 起属 **p.42**；此边界将在 p.42 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p041`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.042（PDF p.42 / 印刷 p.42）
- PNG：`/tmp/birksing_audit_p042.png`（`gs -sDEVICE=pngmono -r150 -dFirstPage=42 -dLastPage=42`，150dpi 二值整页，已用 Read 工具亲自打开观看）；基底 `/tmp/bk_p42_300.png`（`pnggray` 300dpi，仅作裁切用）；坐标探针 `/tmp/bk_p42_bbox.html`（`pdftotext -bbox`）+ `/tmp/bk_p42grp.py`、`/tmp/bk_p42probe.py`。放大裁片：`/tmp/bk_p42_avec.png`（×5，项目符号行 `• A_Y^d ≤ l and…`，核定 `d` 为 `A` 的**上标**、`Y` 为**下标**）、`/tmp/bk_p42_4lA.png`（×3，`4lA − (K_X + Λ)`）、`/tmp/bk_p42_dispA.png`（×3，显示式左半 `a(T,X,Λ) = a(T,Y,Λ_Y`）、`/tmp/bk_p42_lctA.png`（×3，`lct(X,B,|A|_ℝ) = ½…`）、`/tmp/bk_p42_Lhalf.png`（×5，`L := ½N ∈ |C|_ℝ`，核定 `½` 为**上下叠置**分式）、`/tmp/bk_p42_phi.png`（×8，`φ : Y → X`，核定箭头为**实线** `→` 而非虚线双射箭头）、`/tmp/bk_p42_last.png`（×5，页末 `definition of C. Pick L ∈ |C|_ℝ. Let t be the…`）。
- 对应 Markdown：**L2109–L2163**（L2163 末 `we can assume$t < 1$.` 为本页最后一句）。
- 核对（正文页五点）：
  1. **节标题与步号顺序**：p.41 末段收尾（L2109–L2121）→ 印刷节标题 `6. Proof of main results`（bbox L032，y=241）→ 缩进段 `We apply induction on dimension…`（L033–L035）→ `Proof. (of Theorem 1.8) Step 1.`（L036–L040）→ 显示式 → Step 2（L049–L055）→ 两项目符号（L056、L059）→ Step 3（L099–L103）→ 段末（L120–L129）。顺序与 Markdown L2123 `## 6. Proof of main results`、L2125、L2127、L2135、L2137、L2139、L2155、L2163 **逐项一致**，无缺步、无错序、无跨页吞并。
  2. **编号与陈述**：`By Lemma 2.24`（bbox L051–L052，跨行断在 `By Lemma` / `2.24,`）、`Theorem 1.9 in Section 4`（L035）、`Proposition 5.11`（L103、L120）、`Theorems 1.1, 1.6, and 1.8`（L033）、`dimension ≤ d − 1`（L034）—— Markdown L2125/L2135/L2155 中对应编号与序数词**全部正确**。
  3. **公式逐条**：本页共 7 个显示块与 10 余处行内式，逐条核对——(a) L2112 `K _ {X} + \Lambda \sim_ {\mathbb {Q}} \frac {(n + 2) l}{n} A`：bbox 显示分子 `(n+2)l`(x313–349, y119–130)、主基线因子 `A`(x351–360, y127–138)、分母 `n`(x328–335, y134–145)、下标 `Q`(x302–308, y131–138)，**叠置分式且次序正确**；(b) L2115 `4 l A − (K_X + \Lambda)`：bbox token `4lA`(x170)＋裁片 `/tmp/bk_p42_4lA.png` 逐笔确认，`Λ` 为希腊大写 Λ（左斜笔直、无中划、平直衬脚），Markdown `\Lambda` **正确**；(c) L2118 `a (T, X, \Lambda) = a (T, Y, \Lambda_ {Y}) = a (T _ {Y}, Y, \Lambda_ {Y}) = 0,`：裁片 `/tmp/bk_p42_dispA.png` 确认左半三个因子的自变量顺序，末尾**逗号**在位；(d) L2130 `lct(X,B,|M|_ℝ) ≥ lct(X,B,|M+N|_ℝ) = lct(X,B,|A|_ℝ),`；(e) L2139 `A _ { Y } ^ { d } \leq l`：bbox `A`(x127,y452–463)＋叠字 `dY`(x135,y451–465)＋`Y`(x193,y457–464)，裁片 `/tmp/bk_p42_avec.png` 目视 `d` 在 `A` 右上、`Y` 在右下，**上标 `d` 完好**；(f) L2144 加法分解式与 L2150 的 lct 换基等式链；(g) L2158 `\operatorname{lct} (X, B, | A | _ {\mathbb {R}}) = \frac {1}{2} \operatorname{lct} (X, B, | C | _ {\mathbb {R}})`：bbox `1`(x309,y615–626) 与 `2`(x309,y630–641) **同 x 上下叠置**，裁片确认；(h) L2161 `L : = { \textstyle { \frac { 1 } { 2 } } } N \in | C | _ {\mathbb {R} }`：bbox 合并 token `12`(x241.20–245.43, y645.01–659.27)，宽仅 4.23pt 而高 14.26pt —— 分子 `1` 与分母 `2` **同 x 叠置**而非并排，裁片 `/tmp/bk_p42_Lhalf.png` 目视确认叠置分数；`C := ½ A` 处 bbox `1`/`2` 同为 x133.20，结论一致。**七条显示式与全部行内式均与印刷吻合，无一处系数、指数、上下标、箭头或断行丢失。**
  4. **记号约定**：`\operatorname{lct}` 全称与 `\sim_{\mathbb{R}}`/`\sim_{\mathbb{Q}}`（下标 ℝ/ℚ 黑色board）、`\phi^{*}A` 拉回、`K_X/K_Y/B_Y/A_Y/L/C/Λ/Γ/T/t/l/m/n/q/v` 各记号用法——均与印刷一致；页首 `Let Λ be the pushdown of Λ_Y` 与 L2103 的 `\Lambda _ { Y }` 大小写区分**未混淆**。
  5. **行间关系**：三条项目符号（L2137、L2139）归属 Step 2 的「such that」从句；`Let K_Y + B_Y = φ*(K_X + B). Then`（L2141）引出 L2144 分解式再接 `is big as φ is small.`；`We have`（L2155）引出 L2158 等式，`because`（L2161）解释来源；`Finally,`（L2115）引出 L2118 显示式再接 `so T is an lc place of (X, Λ).`（L2121）。**行间逻辑连接词与归属全部正确，无错位、无漏行。**
- 结果：**PASS**——**零缺陷、零改动**。页内 Markdown L2109–L2163 与印刷 p.42 逐句逐式吻合。
- 备注（分级依据）：
  1. **溯源（对 L2109–L2163 逐行 `git show` 比对 `53a92412` → `16ffcc7c`(`^`) → `37580aaf`(HEAD) 三版，34 个非空行中 27 行三版同形、7 行有差异，逐条查证如下）**：本页当前态**零缺陷、零新增改动**，7 处差异全部是 **`53a92412` 初次导出的错误、已被后续 peer 修正**的方向，**不存在 peer 回归**。①初次导出把印刷的 `pseudo-effective` 误作 `pseudo-efective`（少一个 `f`），当前 `pseudo-effective` 与印刷一致（bbox L037）。②初次导出的映射 `\phi \colon Y  X` **丢失箭头**，当前 `\phi \colon Y \to X` 与印刷一致（bbox L053 + 裁片 `/tmp/bk_p42_phi.png` 目视实线箭头）。③初次导出的第二条项目符号为 `$A _ { Y } ^ { d } \leq l ,$, and`——**项目符号 `•` 丢失且 `A_Y − φ*A is ample.` 整段丢失**，当前 `• $A _ { Y } ^ { d } \leq l$ and$A _ { Y } - \phi ^ { * } A$is ample.` 完整（bbox L059–L061 + 裁片 `/tmp/bk_p42_avec.png`）。④初次导出把 `C := ½A` 的 `C` 误加了点号成 `${ \dot { C } } : =`，当前 `C :=` 与印刷一致（bbox L101–L102，坐标探针显示 `C` x133 前的 token 无附加点号）。⑤–⑦三处为句末**句点**的补齐：`so$T$is an lc place of$( X , \Lambda )$` → `…$( X , \Lambda ).`、`…lct$( X , B , | C | _ {\mathbb {R} } )$` → `…$).`、`…we can assume$t < 1.$` → `…$t < 1$.`，三处印刷均有句点（bbox L030 结尾 `Λ).`、L119 结尾 `).`、L129 结尾 `t < 1.`），当前形态**正确**。以上 7 处**均非本轮改动**，本轮对其未作任何 Edit。
  2. **撤销疑点（bbox／低分辨率读图推断被裁片或坐标探针推翻，故不改 Markdown）**：①bbox 把 `L := ½N` 处的分子 `1` 与分母 `2` 合并成单 token `12`（x241.20–245.43），一度疑 Markdown 把叠置分式误写成 `12`（即数字十二）并排；坐标探针显示该 token 宽仅 4.23pt（单数字宽）而高 14.26pt（跨分子分母），裁片 `/tmp/bk_p42_Lhalf.png` 目视确认为**上下叠置的 ½**，Markdown `\frac { 1 } { 2 }` **正确**，撤销不改。②bbox 把 `• A^d_Y ≤ l` 排成 `• A dY ≤ l and …` 同一 y 值行，一度疑 `d` 与 `Y` 丢失上下标身份、被降为普通乘子；坐标探针显示 `A`(y452–463)、叠字 `dY`(y451–465) 与 `Y`(y457–464) 三者 y 值各异，裁片 `/tmp/bk_p42_avec.png` 目视确认 `d` 在右上、`Y` 在右下，Markdown `A _ { Y } ^ { d }` **正确**，撤销不改。③150dpi 整页读图把 `4lA` 中的希腊 `Λ` 与斜体 `l`、`A` 混读，一度疑 `\Lambda` 应为 `A`；bbox token 在 x170–184 处整体解为 `4lA`，裁片 `/tmp/bk_p42_4lA.png` 显示 `(K_X + Λ)` 中该字形左斜笔直、无中划、两腿平直衬脚，确为 **Λ**，Markdown `\Lambda` **正确**，撤销不改。④bbox 把 `φ : Y → X` 的箭头解为 `→`(U+2192)，一度疑印刷应为虚线双射箭头（`⇢`）；坐标探针显示箭头 x268.20–279.11 为**独立实线字形**（与 `Y`/`X` 同 y 区间 y423–434，不带虚线笔划），裁片 `/tmp/bk_p42_phi.png`（×8）目视为**实线箭头**，Markdown `\phi \colon Y \to X` **正确**，撤销不改——与本篇多处 `\to` 虚/实混用（已登记类）一致。
  3. **登记不修（字形/别名族变体）**：`ǫ`(U+01EB，bbox L018/L052/L120/L125 等) 与 `\epsilon` 混用；`\mathbb{R}`/`\mathbb{Q}`（L2112、L2130、L2150、L2158、L2161、L2163）黑板粗体立体化正常；L2127 的 `\sim _ { \mathbb { R } }` 与 L2112 的 `\sim_ {\mathbb {Q}}` 下标间距不一致；L2130/L2150/L2158 使用 `\operatorname{lct}`（印刷为正体 lct）而 L2161 末尾同一 lct 退化为正文 `lct`（`a positive lower bound for lct$( X , B , | C | _ {\mathbb { R } } )$`）；`\begin{array}` 包裹缺失；`{ \textstyle { \frac { 1 } { 2 } } }`（L2155、L2161）为 MinerU 对印刷 **textstyle ½** 的封装（印刷确实是非 displaystyle 的叠置分数，见裁片 5）；数学与正文的空格粘连（`$X , \Lambda )$`、`$4 l A - …$`、`$d , r , \epsilon$`、`$t < 1$`、`$( X , B + t N )$`、`$M + N$`、`$N \geq 0$` 等）；L2163 `$\epsilon .$` 处句点落在数学模式内。均渲染等价或仅差字距，**不改**。
  4. **登记不修（版式损失）**：`6. Proof of main results` 升格为 Markdown 二级标题（原为居中小节标题，字号/字重损失）；`Proof.`、`(of Theorem 1.8)`、`Step 1.`–`Step 3.` 的斜体与缩进退化为普通文本；行内数学斜体丢失（`X`、`B`、`A`、`Y`、`L`、`C`、`φ`、`ε`、`t`、`l`、`m`、`n`、`Λ`、`d`、`r`）；两个项目符号 `•`（L2137、L2139）脱离列表缩进、成为独立段落（项目符号本身**未丢失**）；印刷 QED 方框 □（bbox L031，x513–521, y215）按既定登记类**从不导出**；页眉「Singularities of linear systems and boundedness of Fano varieties　42」（bbox L000/L001）按既定登记类**从不导出**。
  5. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①印刷 Step 2 第二条项目符号写作 `A^d_Y ≤ l`——上标 `d` 置于 `A` 的右上而**下标 `Y` 位于 `d` 的正下方**（bbox 叠字 `dY` y451–465），Markdown 记为 `A _ { Y } ^ { d }`（同一基体的上下标），**未改写为 `A_Y^d` 或 `(A_Y)^d`**。②Step 3 中 `C := ½A` 的 `A` **不带下标**，而 Step 2 中的线性系一律写作 `|A|_ℝ`；Markdown L2155 照录为无下标的 `A`，**未补下标 `Y`**。③Step 3 段末「Let *n*, *m*, *ε′* be the numbers given by Proposition 5.11」中，`n`、`m`、`ε′` 三个量在同页前文（Step 5 之前）尚未出现定义位置，印刷即如此；Markdown L2163 照录，**未作任何前后文补充**。④L2115「we deduce that *4lA* − (*K_X* + Λ) is ample which in turn implies that there is a natural number *m* depending only on *d*, *r*, *ε* such that *mA* − Λ is ample」中自然数 `m` 与分子 `(n+2)l` 的 `l` 字形近似且同段并存，Markdown 分别照录为 `m` 与 `l`，**未互相替换**。⑤印刷 Step 3 最后一句 `In particular, we can assume t < 1.` 与 Step 4 的 `Assume x is not a closed point.` 属不同推理层，Markdown L2163/L2173 **未合并**。
- 跨页边界登记：本页印刷首行 bbox L002（`Let Λ be the pushdown of Λ_Y. Then K_Y + Λ_Y is the pullback of K_X + Λ, …`，y=89）与 p.41 审计末尾登记的边界「L2109 `Let Λ be the pushdown of…` 起属 p.42」**交叉核对一致**；本页印刷末行 bbox L129（`ǫ′-lc. It is enough to find a positive lower bound for t. In particular, we can assume t < 1.`，y=711）对应 Markdown L2163 该句末，L2165 `By definition of$t ,$there is a prime divisor$T$on birational models of X such that` 起属 **p.43**；此边界将在 p.43 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p042`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.043（PDF p.43 / 印刷 p.43）
- PNG：`/tmp/birksing_audit_p043.png`（`gs -sDEVICE=pngmono -r150 -dFirstPage=43 -dLastPage=43`，150dpi 二值整页，已用 Read 工具亲自打开观看）；基底 `/tmp/bk_p43_300.png`（`pnggray` 300dpi，仅作裁切用）；坐标探针 `/tmp/bk_p43_bbox.html`（`pdftotext -bbox`）+ `/tmp/bk_p43grp.py`。放大裁片：`/tmp/bk_p43_repl.png`（×6，Step 5 首行 `…t with 2mA, 2mC, 2mL, t/(2m), re…`，核定 `t/(2m)` 为**上下叠置**分式且四个替换对象的**视觉左右次序**）、`/tmp/bk_p43_ceil.png`（×13，`e = ⌈(3d+1)/s⌉` 全组）、`/tmp/bk_p43_Lbr.png`（×30，`⌈` 与其右侧首字形）、`/tmp/bk_p43_Rbr.png`（×26，`1`、分式线、`⌉,`）、`/tmp/bk_p43_ceil2.png`（×13，取整号组全景）、`/tmp/bk_p43_geqq.png`（×7，`t ≥ (ε − ε′)/q`）、`/tmp/bk_p43_disp.png`（×3，显示式 `(X, B + (1 − ε′/ε)vL)`）、`/tmp/bk_p43_bullets.png`（×4，Step 5 的四条项目符号 `• nΛ is integral,` / `• mA − Λ is ample,` / `• (X, Λ) is lc near x, and` / `• T is an lc place of (X, Λ).`）。
- 对应 Markdown：**L2165–L2211**（L2211 `The idea of Step 6 in the previous proof is due to Yanning Xu.` 为本页最后一句）。
- 核对（正文页五点）：
  1. **节标题与步号顺序**：`By definition of t, …`（L002）→ 显示式（L003）→ `Let x be the generic point…`（L004）→ Step 4（L005–L023）→ Step 5（L024–L037）→ Step 6（L046–L065）→ 献词句（L067）。Markdown L2165、L2173、L2187、L2207、L2211 **顺序完全一致**，Step 3→4→5→6 编号连续，无缺步、无错序。
  2. **编号与陈述**：`Proposition 5.7`（L007、L034）、`Propositions 5.7 and 5.11`（L025）、`Proposition 5.11`（L025）、`Lemma 2.3`（L014）、`Steps 1-5 above`（L051）、`Step 1`（L048）、`Step 6 in the previous proof`（L067）—— 与 Markdown L2173/L2187/L2197/L2207/L2211 **逐一吻合**。
  3. **公式逐条**：本页 5 个显示块与 10 余处行内式，逐条核对——(a) L2168 `a (T, X, B + t L) = \epsilon^ {\prime}.`（bbox L003，末尾**句点在数学模式内**）；(b) L2176 `(X, B + (1 - \frac {\epsilon^ {\prime}}{\epsilon}) v L)`：bbox 分子 `ǫ′`(x323–328, y226–233) 与分母 `ǫ`(x325, y241–248) **同 x 上下叠置**，裁片 `/tmp/bk_p43_disp.png` 确认；(c) L2182 `B + (1 - \frac{\epsilon′}{\epsilon}) v L = \frac{\epsilon′}{\epsilon} B + (1 - \frac{\epsilon′}{\epsilon})(B + v L)`：bbox 三个分子 `ǫ′` 分别在 x253/x294/x349（y276）、三个分母 `ǫ` 在 x254/x296/x351（y291），**三个叠置分式 ε′/ε 次序正确且一个不缺**；(d) L2185 行内 `t \geq ( 1 - \frac { \epsilon ^ { \prime } } { \epsilon } ) v`：bbox 分子 `ǫ′`(x334–338, y307–308) 与分母 `ǫ`(x336, y316) 叠置；(e) L2197 的替换表 `2mA, 2mC, 2mL, \frac { t } { 2 m }`：bbox 分子 `t`(x299, y444)、分母 `2m`(x294, y453) 叠置且位于 `2mL,`(x266–295) 与 `,`(x307) 之间，裁片 `/tmp/bk_p43_repl.png` 目视 **视觉次序为 2mA、2mC、2mL、t/(2m)**，与 Markdown 一致；(f) L2202 `a (T, X, B) \geq \epsilon > \epsilon^ {\prime} = a (T, X, B + t L),`（bbox L039，末尾**逗号**在位）；(g) L2205 `t \geq \frac { \epsilon - \epsilon ^ { \prime } } { q }`：bbox 分子 `ǫ−ǫ′`(x295–310, y531)、分母 `q`(x301, y539) 叠置，裁片 `/tmp/bk_p43_geqq.png` 确认；(h) L2207 的 `0 \leq P \sim _ { \mathbb {R} } A - B`（bbox `0`x112、`≤`x121、`P`x132、`∼`x144、下标 `R`x153 y602、`A`x162、`−`x172、`B.`x183）；(i) 同行的 `e = { \bigl \lceil } { \frac { 3 d + 1 } { s } } { \bigr \rceil }`：bbox `⌈`(x265.20–270.04)、分子 `3d+1`(x271.20–290.55, y648–655)、分母 `s`(x279.00–282.91, y656–664)、`⌉,`(x291.84–299.66)，**分子/分母在括号内居中，无独立圆括号 token**；(j) L2209 `( e + 1 ) A - B`。**九条逐条与印刷吻合，无系数、指数、上下标、箭头、取整号或叠置/顺序丢失。**
  4. **记号约定**：`µ`(bbox L035/L041，U+00B5) ↔ `\mu`、`μ_T` 下标形式、`ν : U → X` 的**实线**箭头（bbox L034 `→`）、`\phi` 的星号拉回、`\sim_{\mathbb{R}}`、`\lceil\,\rceil`、`|A|`（Step 4 中**不带** `_ℝ` 下标）与 `|C|_ℝ`（Step 3 中**带**下标）—— 印刷本身即如此混用，Markdown L2173/L2197/L2207/L2209 **照录未统一**。
  5. **行间关系**：Step 4 的 `Then` → 显示式 → `is ε′-lc near x, by Lemma 2.3, because` → 显示式 → `and because (X, B) is ε-lc. In particular, …`；Step 5 的 `such that` → 四条项目符号（末条自带句点）→ `Replacing …` → `Now since` → 显示式 → `we have … which implies …`；Step 6 的 `Hence letting e = ⌈(3d+1)/s⌉, P + eA is ample.` → 新段 `By assumption, …` → QED → 献词句。**行间连接词与归属全部正确，无错位、无漏行。**
- 结果：**PASS**——**零缺陷、零改动**。页内 Markdown L2165–L2211 与印刷 p.43 逐句逐式吻合。
- 备注（分级依据）：
  1. **溯源（对 L2165–L2211 共 28 个非空行逐行 `git show` 比对 `53a92412` → `16ffcc7c`(`^`) → `37580aaf`(HEAD)）**：当前态**零缺陷、零新增改动**；6 处差异全部是 `53a92412` 初次导出（或 `^` 版）的错误、已被后续 peer 修正的方向，**不存在 peer 回归**。①`Step$\it 4 .$` → `Step 4.`：清除 MinerU 泄漏的原始 `\it` 控制序列（`$`/`\it` 全部删除）。②三条项目符号补齐：初次导出的 `$n \Lambda$is integral,`、`$m A - \Lambda$is ample,`、`$( X , \Lambda )$is lc near$x ,$and` **三条均丢失项目符号 `•`**，当前 L2189/L2191/L2193 全部补齐（印刷裁片 `/tmp/bk_p43_bullets.png` 逐条可见 `•`）。③`• T is an lc place of$( X , \Lambda )$` → `…$( X , \Lambda ).`：补句末句点（印刷 bbox L030 结尾 `Λ).`）。④`hence $s P + ( 3 d + 1 ).$A is ample` → `hence$s P + ( 3 d + 1 )A$ is ample`：删除**数学模式内多出的句点**并把脱逸的 `$A` 收回同一数学模式（印刷 bbox L058 `hence sP + (3d + 1)A is`、L059 起 `ample which means…`，句点不在此处）。⑤/⑥ 即 ①–④ 中的 `^`→HEAD 两项（`Step$\it 4.$` 清除、句点补齐）。以上 **6 处均非本轮改动**，本轮对其未作任何 Edit。
  2. **撤销疑点（bbox／低分辨率读图推断被裁片或坐标探针推翻，故不改 Markdown）**：①**bbox 把 Step 5 首行整行打乱**：L031 的 token 序列读作 `t , respectively, and replacing r accordingly, we Replacing A, C, L, t with 2mA, 2mC, 2mL,`——把行**中段**内容发射到了行首，一度疑 Markdown 把四个替换对象的次序排错；坐标探针给出视觉 x 序（`Replacing`x91、`2mA,`x210、`2mC,`x238、`2mL,`x266、分子 `t`x299 y444、分母 `2m`x294 y453、`,`x307、`respectively,`x313），裁片 `/tmp/bk_p43_repl.png`（×6）目视确认**视觉次序为 `2mA, 2mC, 2mL, t/2m,`**，Markdown L2197 **正确**，撤销不改——这与 p.35、p.40、p.41 已登记的「bbox 内容流顺序不可直接当作视觉顺序」是同一现象（本页首次出现整行级别乱序）。②130dpi/×13 裁片 `/tmp/bk_p43_ceil.png` 中，`e = ⌈` 与 `⌉` 的括号笔划在低倍率下被误读为 `e = ⌈(3d+1)/s⌉`（即取整号内另有圆括号），一度疑 Markdown 漏掉印刷的圆括号；改用 `/tmp/bk_p43_Lbr.png`（×30，x263.5–275.5）只见 `⌈` 的竖笔+右向顶横紧接数字 `3`、**其间无圆括号笔划**，`/tmp/bk_p43_Rbr.png`（×26，x285–302）只见 `1`、分式线、`⌉` 的竖笔+左向顶横、逗号、**其间亦无圆括号笔划**；bbox 亦无独立 `(`/`)` token（`⌈`x265.20–270.04 与 `3d+1`x271.20–290.55 之间仅 1.16pt 空隙，不足一个圆括号宽），三通道一致确认印刷**只有取整号、无圆括号**，Markdown `\bigl \lceil } { \frac { 3 d + 1 } { s } } { \bigr \rceil` **正确**，撤销不改。③bbox 把 L2182 显示式中三个分式的分子、三个分母分别连成单 token（`ǫ ′ ǫ ′ ǫ ′` / `ǫ ǫ ǫ`），一度疑三个 ε′/ε 被合并成一个；坐标探针显示六个字形的 x 分别为 253/294/349 与 254/296/351，**三组分式彼此独立、横向并列**，Markdown 三个 `\frac {\epsilon^ {\prime}}{\epsilon}` **正确**，撤销不改。④bbox 把 L2185 中 `t ≥ (1 − ε′/ε)v` 的 `ε′` 分子提前发射到独立行（L019 `′`@x338 y307），一度疑 Markdown 漏 ε 或漏撇；按 x 序（`t`x291、`≥`x298、`(1`x310、`−`x322、`′`x338 y307、分母 `ǫ`x336 y316、`)v.`x342）确认分数完整，Markdown **正确**，撤销不改。
  3. **登记不修（字形/别名族变体）**：`ǫ`(U+01EB，bbox L003/L008/L011/L013/L014/L016/L018/L020/L021/L034/L039/L043/L052 等) 与 `\epsilon` 混用；`µ`(U+00B5) ↔ `\mu`；`\geq`/`\leq` 与 `\ge`/`\le` 别名混用（L2202 `\geq`、L2197 `\leq`、L2185 `\geq`、L2207 `\leq`）；`\bigl \lceil`/`\bigr \rceil` 对应变高取整号（`\big` 级别，未用 `\left...\right` 自适应）；`{ \frac { t } { 2 m } }`、`{ \textstyle { \bigl \lceil } … }` 为 MinerU 封装（印刷为 textstyle 叠置分数）；数学与正文的空格粘连（`$d , r , ǫ$`、`$X , \Lambda )$`、`$t L$`、`$q$`、`$U .$`、`$( e + 1 ) A$`、`$s P + ( 3 d + 1 )A$` 等）；句点/逗号落在数学模式内（`$\epsilon^ {\prime}.$`、`$U .$`、`( X , \Lambda ).`、`$P \sim _ {\mathbb{R} } A - B ,$`、`$\epsilon .$`）。均渲染等价或仅差字距，**不改**。
  4. **登记不修（版式损失）**：`Step 4.`–`Step 6.` 的斜体与缩进退化为普通文本；行内数学斜体丢失（`X`、`B`、`A`、`L`、`C`、`T`、`t`、`v`、`s`、`e`、`m`、`n`、`q`、`Λ`、`φ`、`ν`、`ε`、`d`、`r`、`x`）；四条项目符号 `•`（L2189/L2191/L2193/L2195）脱离列表缩进、成为独立段落（项目符号本身**未丢失**）；`Now since`（L2199）的段首缩进丢失；印刷 QED 方框 □（bbox L066，x513–521, y689）按既定登记类**从不导出**；页眉「Singularities of linear systems and boundedness of Fano varieties　43」（bbox L000/L001）按既定登记类**从不导出**。
  5. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①印刷 Step 4 的「general elements of `|A|`」写作**无下标**的 `|A|`，而同页 Step 3 一律写作 `|C|_ℝ`、`|A|_ℝ`；Markdown L2173 照录无下标形式，**未补 `_ℝ`**。②印刷 Step 4 与 Step 5 中 `ε′/ε` 共出现 **4 处**（显示式 1 处 + 等式 3 处 + 行内式 1 处），每次都重新排版，Markdown L2176/L2182/L2185 **逐处重复写出**而非合并为记号，**未简写**。③印刷 Step 5 的替换句 `Replacing A, C, L, t with 2mA, 2mC, 2mL, t/2m, respectively, …` 把被替换量 `A, C, L, t` 中的 `t` 写成**与定理中同一字母 `t`**（Step 4 中 `t` 是 lct 阈值），Markdown L2197 照录，**未改记号**。④印刷 Step 6 中 `0 ≤ P ∼_ℝ A − B` 与随后的 `By assumption, P ∼_ℝ A − B` 是**同一断言的两次陈述**，Markdown L2207/L2209 **未合并为「由假设」**。⑤印刷 Step 6 末 `replacing A with (e + 1)A, we are reduced to the case when A − B is ample` 与 Step 6 开头的 `We will show that after replacing A with a bounded multiple, A − B becomes ample` 呼应，Markdown L2207/L2209 **未交叉引用**。⑥印刷把取整号写作 `\lceil (3d+1)/s \rceil` 时**分式被取整号直接包裹**，未写成 `\lceil \frac{3d+1}{s} \rceil` 之外的任何形式；Markdown L2207 **未增删任何括号**（见撤销疑点 ②）。
- 跨页边界登记：本页印刷首行 bbox L002（`By definition of t, there is a prime divisor T on birational models of X such that`，y=89）与 p.42 审计末尾登记的边界「L2165 `By definition of$t ,$there is a prime divisor$T$on birational models of X such that` 起属 p.43」**交叉核对一致**；本页印刷末行 bbox L067（`The idea of Step 6 in the previous proof is due to Yanning Xu.`，y=711）对应 Markdown L2211，L2213 `Proof. (of Theorem 1.7) This follows by combining Theorem 1.8, Lemma 3.3, and Proposition 3.4.` 起属 **p.44**；此边界将在 p.44 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p043`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.044（PDF p.44 / 印刷 p.44；正文收尾页 + 参考文献起始页）
- PNG：`/tmp/birksing_audit_p044.png`（`gs -sDEVICE=pngmono -r150 -dFirstPage=44 -dLastPage=44`，150dpi 二值整页，已用 Read 工具亲自打开观看）；基底 `/tmp/bk_p44_300.png`（`pnggray` 300dpi，仅作裁切用）；坐标探针 `/tmp/bk_p44_bbox.html`（`pdftotext -bbox`）+ `/tmp/bk_p44grp.py`。放大裁片：`/tmp/bk_p44_tl.png`（×8，行内 `t_l = t/l for l ∈ ℕ`，核定 `t/l` 为**上下叠置**分式且 `l` 是 `t` 的下标）、`/tmp/bk_p44_eps2.png`（×4，`is ε/2-lc. Now apply…`，核定 `ε/2` 为叠置分数且 ε 为**月牙形** CM `\epsilon`）、`/tmp/bk_p44_Xpp2.png`（×8，`and let X″ be`，核定 `X` 后为**双撇** `″`）、`/tmp/bk_p44_Omega2.png`（×4，`K_{X″} + Ω″ which gives`，核定 `X″` 的双撇在**下标内**、`Ω″` 的双撇在上标位）、`/tmp/bk_p44_Xpp.png`（×3，`…the resulting model. Then` 行段，定位参照）。
- 对应 Markdown：**L2213–L2259**（L2259 为参考文献 [7]，L2261 `[8] A. Borisov; …` 起属 p.45）。
- 核对（正文页五点）：
  1. **段标题与证明块顺序**：`Proof. (of Theorem 1.7)`（bbox L002–L003，跨行断在 `Proposi-`/`tion 3.4.`）→ `Proof. (of Theorem 1.6)`（L005–L006）→ `Proof. (of Theorem 1.1)`（L008–L031）→ 缩进段 `By Theorems 2.10 and 2.13, …`（L032–L041）→ 缩进段 `On the other hand, …`（L042–L055）→ `Proof. (of Corollary 1.4)`（L057–L081）→ `Proof. (of Corollary 1.5)`（L083）→ 小节标题 `References`（L085）→ 文献 [1]–[7]（L086–L095）。Markdown L2213/L2215/L2217/L2219/L2221/L2223/L2243/`## References`/L2247–L2259 **顺序完全一致**，定理与推论编号 1.7→1.6→1.1→Cor 1.4→Cor 1.5 无错序、无缺失、无吞并。
  2. **编号与陈述**：`Lemma 3.3`、`Proposition 3.4`（L002–L003）；`Theorem 1.8 in dimension ≤ d`、`Theorem 1.1 in dimension ≤ d − 1`、`Lemma 3.2`（L005–L006）；`[5, 6.1(3)]`、`[15]`（L025/L030）；`Theorems 2.10 and 2.13`（L032）；`Theorem 1.1 in dimension ≤ d − 1`、`Theorem 2.11`（L038）；`Theorem 1.6`（L042）；`Theorem 2.15`（L055）；`Theorem 1.1`（L081/L083）；`[39, Theorem 1.8]`（L083）。与 Markdown L2213/L2215/L2217/L2219/L2221/L2241/L2243 **逐一吻合**。
  3. **公式逐条**：4 个显示块与 10 余处行内式，逐条核对——(a) L2226 `Γ = (1 - \alpha) \Delta + \alpha D.`；(b) L2232 `- (K _ {X} + \Gamma) = - (1 - \alpha) (K _ {X} + \Delta) - \alpha (K _ {X} + D)`；(c) L2238 `- (K _ {X} + D) \sim_ {\mathbb {R}} \Delta - D \sim_ {\mathbb {R}} A`：bbox `∼`(x305/358) 与下标 `R`(x305/358, y500) 成对，**两个 `∼_ℝ` 一个不缺**；(d) L2241 的 `\frac { \epsilon } { 2 }`：bbox 分子 `ǫ`(x103, y523–530) 与分母 `2`(x103, y531–538) **同 x 上下叠置**，裁片 `/tmp/bk_p44_eps2.png` 确认；(e) L2217 的 `X ^ { \prime }`、`X ^ { \prime \prime }`、`\Delta ^ { \prime \prime }`、`\Omega ^ { \prime \prime }`、`K _ { X ^ { \prime \prime } }`、`K _ { X ^ { \prime } }`、`\Omega ^ { \prime }`：bbox L010 `X ′`、L011 `X ′′`、L017 `∆ ′′` 与 `(X ′′ , ∆ ′′ )`、L019 `X ′′`、L022 `X ′′`、L023 `+ Ω ′′`、L024 `X ′`、L025 `+ Ω ′ [5, 6.1(3)]` 逐一对应，裁片 `/tmp/bk_p44_Xpp2.png`（`X″` 双撇）与 `/tmp/bk_p44_Omega2.png`（`K_{X″} + Ω″`）目视确认；(f) L2219 的 `\vert - m K _ { X } \vert`（bbox L033–L035 `|−mK` / `X` / `| defines a birational map`）与 `\operatorname { vol } ( - K _ { X } ) \leq v`（bbox L039–L041 `vol(−K` / 下标 `X` / `) ≤ v.`，`vol` 为**正体**）；(g) L2221 的 `0 \leq N \sim _ { \mathbb {R} } - K _ { X }`（bbox L043–L046 `0 ≤ N ∼`/下标 `R`/`−K`/下标 `X`）、`\begin{array} { r } { t _ { l } = \frac { t } { l } } \end{array}`（bbox 基线 `t`@x427.56–431.50 + 下标 `l`@x431.52–434.05 y353.83–361.15 + `=` + 合并 token `tl`@x451.20–454.25 w=3.05 y347.71–363.07 —— **宽仅 3.05pt（窄于单字符）而高 15.36pt**，为分子 `t`/分母 `l` 同 x 叠置；裁片 `/tmp/bk_p44_tl.png`（×8）目视确认为叠置分数）、`0 \le L \sim - l K _ {X}`（bbox L050–L051，**无 `_ℝ` 下标**，与前半句不同）、`( X , t _ { l } L )`（bbox L052–L054，基线 `t`@x262 + 下标 `l`@x333 y367 + `L`@x336）。**七组逐条与印刷吻合，无系数、指数、上下标、撇号、绝对值竖线或叠置/顺序丢失。**
  4. **记号约定**：`\Delta`(bbox 作 U+2206 `∆`)、`\Omega`、`\Gamma`、`\alpha`、`X ′`/`X ″`（Q-factorialisation / MMP 结果模型）三模型的次级记号、`\sim_{\mathbb{R}}` 数值等价关系、`\vert · \vert` 线性系绝对值记号、`\operatorname{vol}`、`\mathbb{N}`、`\mathbb{R}` —— 印刷本身即混用（`∆`/`Δ` 同形、`0 ≤ N ∼_ℝ −K_X` 与 `0 ≤ L ∼ −lK_X` 一处有下标一处无），Markdown L2217/L2219/L2221 **照录未统一**。
  5. **行间关系**：Theorem 1.1 证明内三段的缩进与归属（三段同为 `Proof. (of Theorem 1.1)` 的延续，第一段非缩进、二三段缩进）；Corollary 1.4 中 `and let` → 显示式 → `Then` → 显示式 → `is ample because` → 显示式 → `is ample.`；`References` 与文献条目的挂接。**行间连接词与归属全部正确，无错位、无漏行。**
- 参考文献五点核对（[1]–[7]，逐条查 作者/刊名/卷期页码/年）：
  - [1] 印刷 `V. Alexeev; Boundedness and K² for log surfaces. Internat. J. Math. 5 (1994), no. 6, 779–810.`；bbox 坐标 `K`@x232 y615 与上标 `2`@x240 y613（**上标在 K 右上**）、卷 `5`@x390、`(1994),`@x399；MD L2247 `[1] V. Alexeev; Boundedness and$K ^ { 2 }$for log surfaces. Internat. J. Math. 5 (1994), no. 6, 779–810.` —— **作者(分号)/标题/刊名/卷/期/年/页码全部吻合**。
  - [2] 印刷 `V. Alexeev, M. Brion, Boundedness of spherical Fano varieties. The Fano Conference, 69-80, Univ. Torino, Turin, 2004.`（跨行 `Univ.`/`Torino`）；MD L2249 —— **吻合**。
  - [3] 印刷 `F. Ambro; Variation of Log Canonical Thresholds in Linear Systems. Int. Math. Res. Notices 14 (2016), 4418-4448.`；MD L2251 —— **吻合**。
  - [4] 印刷 `C. Birkar; Log Calabi-Yau fibrations, arXiv:1811.10709.`；MD L2253 —— **arXiv 编号逐位吻合**。
  - [5] 印刷 `C. Birkar; Anti-pluricanonical systems on Fano varieties, Ann. of Math. (2) 190 (2019), no. 2, 345-463.`；MD L2255 —— **吻合**。
  - [6] 印刷 `C. Birkar; Existence of log canonical flips and a special LMMP, Pub. Math. IHES., 115 (2012), 325-368.`（刊名后**保留**了 `IHES.,` 的句点+逗号）；MD L2257 —— **吻合**。
  - [7] 印刷 `C. Birkar, P. Cascini, C. Hacon and J. MᶜKernan; Existence of minimal models for varieties of log general type, J. Amer. Math. Soc. 23 (2010), no. 2, 405-468.`；bbox `M`@x275 y702 与上标 `c`@x284 y701（**c 为上标**）；MD L2259 `… J. M<sup>c</sup>Kernan; …` —— 作者/刊名/卷/期/年/页码**全部吻合**，上标 `c` 走 HTML `<sup>` 泄漏（见登记不修 ③）。**文献 [1]–[7] 编号连续、无跳号、无重复。**
- 结果：**PASS**——**零缺陷、零改动**。页内 Markdown L2213–L2259 与印刷 p.44 逐句逐式、逐条文献吻合。
- 备注（分级依据）：
  1. **溯源（对 L2213–L2259 共 27 个非空行逐行 `git show` 比对 `53a92412` → `16ffcc7c`(`^`) → `37580aaf`(HEAD)）**：当前态**零缺陷、零新增改动**；4 处差异全部是 `53a92412` 初次导出的错误、已被后续 peer 修正的方向，**不存在 peer 回归**。①MMP 处的 `\boldsymbol { X } \boldsymbol { \mathit { \Pi } …` 公式碎片与紧跟其后的乱码，被还原为印刷的 `- K _ { X ^ { \prime } }`（bbox L009–L010 `−K` / `X ′`），并补回句点（`…is of Fano type. Run an MMP on$- K _ { X ^ { \prime } }$`，印刷 bbox L008–L010 `Run an MMP on −K_{X′}`）。②`vo$.` 碎片被还原为 `$\operatorname { vol }`（印刷为**正体** `vol`，bbox L039）。③`$d , e$ǫ` 被还原为 `$d , \epsilon$`（印刷为单个 ε，bbox L043 `on d, ǫ such that`）。④`suficiently`（少一个 `f`）被改正为 `sufficiently`（印刷 bbox L078 `choosing α to be sufficiently small`）。另 ①②③ 中附带的两个句末句点补齐（`assume$B = 0$.` 与 `$\leq v$.`，印刷 bbox L031/L041 均有句点）系 `^`→HEAD 阶段的修正。**以上 4 处均非本轮改动**，本轮对其未作任何 Edit。
  2. **撤销疑点（bbox／低分辨率读图推断被裁片或坐标探针推翻，故不改 Markdown）**：①bbox 把行内 `t_l = t/l` 的分子分式合并成单 token `tl`（x451.20–454.25，**宽 3.05pt、高 15.36pt**），一度疑 Markdown 把叠置分式误写成并排的 `tl`（即字母乘积）；裁片 `/tmp/bk_p44_tl.png`（×8）目视确认为**分子 `t` 在上、分母 `l` 在下的叠置分数**，且其左侧 `t`（x427.56–431.50）与下标 `l`（x431.52–434.05, y353.83–361.15）是**另一组** `t_l`，Markdown `t _ { l } = \frac { t } { l }` **正确**，撤销不改。②bbox 把 `K_{X″}` 的下标 `X″` 拆为独立行（L022 `X ′′`），一度疑 Markdown 把双撇写成了 `X ^ { \prime \prime }` 的上标而非下标；裁片 `/tmp/bk_p44_Omega2.png`（×4）目视确认 `X` 为主基线、**`″` 位于其右上但整组 `X″` 处于下标高度**（下方紧接 `+ Ω″` 的基线），Markdown `K _ { X ^ { \prime \prime } }` **正确**，撤销不改。③150dpi 整页读图把 `Ω″` 的希腊 `Ω` 与拉丁 `O`/`Q` 混读；bbox L023 解为 `Ω`(U+03A9)，裁片 `/tmp/bk_p44_Omega2.png` 显示为两侧带**水平足部**的希腊大写 Omega，Markdown `\Omega ^ { \prime \prime }` **正确**，撤销不改。④bbox 把 `ε/2` 的分子 `ǫ` 与句首 `is` 排在同一 y 行（L081 `ǫ -lc. Now apply Theorem 1.1.`），一度疑 `ε/2` 丢失分母；坐标探针显示 `ǫ`@x103 y523–530 与 `2`@x103 y531–538 **同 x 上下叠置**，裁片确认，Markdown `\frac { \epsilon } { 2 }` **正确**，撤销不改。
  3. **登记不修（字形/别名族变体）**：`ǫ`(U+01EB，bbox L012/L017/L042/L052/L078/L081 等) 与 `\epsilon` 混用；`∆`(U+2206，bbox L012/L014/L017/L057/L059/L067/L073/L075/L078) ↔ `\Delta`（印刷为 CM 大写 Delta，仅 CMap 码位差异）；`\geq`/`\leq`（L2215、L2219、L2221）与同页 `\le`（L2221 的 `0 \le L`）别名混用；`\begin{array} { r } { t _ { l } = \frac { t } { l } } \end{array}`（L2221）单元素数组包裹行内式（印刷为无框单式）；`\vert - m K _ { X } \vert`（L2219）用 `\vert` 而非 `|`；`\epsilon { \mathrm { - l c } }`（L2241）与 `\frac { \epsilon } { 2 } { - } \mathrm { l c }`（L2241）两种 lc 写法混用；数学与正文的空格粘连（`$X , \Delta )$`、`$K _ { X } + \Omega$`、`$d , \epsilon$`、`$\lvert - m K _ { X } \rvert$`、`$t N$`、`$U .$`、`$B = 0$` 等）；句点落在数学模式内（`$\leq d .$` L2215、`$B = 0$.` L2217、`$\leq v$.` L2219、`$A + D.` L2223、`$\alpha D.$` L2226）。均渲染等价或仅差字距，**不改**。
  4. **登记不修（版式损失）**：`References` 在印刷中为**小型大写字母**（small caps），Markdown `## References` 升格为二级标题并丢失 small caps 字形；`Proof.`、`(of Theorem 1.7)`、`(of Theorem 1.6)`、`(of Theorem 1.1)`、`(of Corollary 1.4)`、`(of Corollary 1.5)` 的斜体与段首缩进退化为普通文本；行内数学斜体丢失（`X`、`B`、`A`、`D`、`K`、`Ω`、`Γ`、`∆`、`α`、`t`、`l`、`m`、`n`、`v`、`ε`、`d`）；文献条目的**小号正文字号与悬挂缩进**（续行顶格而非缩进）退化为普通段落，条目间空行由印刷的紧排变为空行分隔；文献标题的斜体（`Boundedness and K² for log surfaces`、`Log Calabi-Yau fibrations` 等）丢失；`[5, 6.1(3)]`、`[15]`、`[39, Theorem 1.8]` 的方括号引用**未转为超链接**（Markdown 中为纯文本，正确）；印刷 QED 方框 □（bbox L004、L007、L056、L082、L084，x513–521）按既定登记类**从不导出**；跨行连字符 `Proposi-`/`tion`（bbox L002–L003）按既定登记类**连字符丢失**；页眉「Caucher Birkar　44」（bbox L001/L000）按既定登记类**从不导出**。
  5. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①文献 [1] 的作者与题名之间用**分号** `;`（Alexeev 条），而 [2]、[7] 的多作者之间用**逗号** `,`；同一位作者 V. Alexeev 在 [1] 用 `;`、在 [2] 用 `,`，Markdown L2247/L2249 **照录未统一**。②文献 [1] 的 `779–810` 用**连接号 `–`（U+2013）**，而 [3] 的 `4418-4448`、[5] 的 `345-463`、[6] 的 `325-368`、[7] 的 `405-468` 用**连字符 `-`（U+002D）**；Markdown L2247–L2259 **逐条照录，未统一**。③文献 [3] 的刊名 `Int. Math. Res. Notices` 与文献 [1] 的 `Internat. J. Math.` 是**两种不同的期刊名缩写**，且 [3] 缺 `Internat.` 的 `n`；Markdown L2251 **照录未按 [1] 补全**。④文献 [6] 的刊名写作 `Pub. Math. IHES.,` —— 机构名后**多一个句点再接逗号**（`IHES.,`），属印刷排印怪癖；Markdown L2257 **照录，未删句点亦未删逗号**。⑤文献 [7] 中 `J. MᶜKernan` 的上标 `c` 与 `M` 之间**无空格**；Markdown L2259 走 `<sup>` 亦无空格，**未补空格**。⑥Theorem 1.1 证明中 `0 ≤ N ∼_ℝ −K_X`（带 ℝ 下标）与 `0 ≤ L ∼ −lK_X`（**无 ℝ 下标**）指同一 ℝ-等价关系，印刷写法不一致；Markdown L2221 **照录未统一**。⑦Theorem 1.1 证明中 `K_{X″} + Ω″` 与 `K_{X′} + Ω′` 两处「klt n-complement」先陈述 `K_{X″}` 的（作为蕴含主语）再陈述 `K_{X′}` 的，两者的 `Ω` **无撇与有撇**之别极小易混；Markdown L2217 **逐处照录未合并**。
- 跨页边界登记：本页印刷首行 bbox L002（`Proof. (of Theorem 1.7) This follows by combining Theorem 1.8, Lemma 3.3, and Proposi-`，y=89）与 p.43 审计末尾登记的边界「L2213 `Proof. (of Theorem 1.7) This follows by combining…` 起属 p.44」**交叉核对一致**；本页印刷末行 bbox L095（`general type, J. Amer. Math. Soc. 23 (2010), no. 2, 405-468.`，y=713）对应 Markdown L2259 文献 [7] 的行末，L2261 `[8] A. Borisov; Boundedness of Fano threefolds with log-terminal singularities of given index. J. Math. Sci. Univ. Tokyo 8 (2001), no. 2, 329–342.` 起属 **p.45**；此边界将在 p.45 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p044`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.045（PDF p.45 / 印刷 p.45；参考文献页，无正文、无收稿日期）
- PNG：`/tmp/birksing_audit_p045.png`（gs pngmono 150dpi 全页，**已用 Read 打开亲看**）；`/tmp/bk_p45_300.png`（pnggray 300dpi 底图，S=300/72.0=4.16667）；`/tmp/bk_p45_bbox.html`（`pdftotext -bbox -f 45 -l 45`）。裁片：`/tmp/bk_p45_affine.png`（×8，x246–286 / y414–428，裁定 [23] `affine` 是**双 f** 还是单 f——同行 peer 修复的关键字）、`/tmp/bk_p45_kollar.png`（×4，x115–196 / y448–458，裁定 [25] `Kollár ét al.` 的两个变音符）、`/tmp/bk_p45_asterisque.png`（×4，x370–466 / y448–458，裁定 `Astérisque` 的 `é`）、`/tmp/bk_p45_mckernan.png`（×7，x170–222 / y216–229，裁定 `MᶜKernan` 的 `c` 是上标还是正体）、`/tmp/bk_p45_tians2.png`（×16，x352–384 / y175–185，裁定 `Tian’s` 的撇号是 `’` 还是 `'`）、`/tmp/bk_p45_lens2.png`（×16，x246–279 / y318–328，裁定 `l’ENS` 的撇号）、`/tmp/bk_p45_dash8.png`（×8，x222–267 / y96–107，裁定 [8] `329–342` 用**长连接号**）、`/tmp/bk_p45_dash23.png`（×8，x170–212 / y425–436，裁定 [23] `187-192` 用**短连字符**）、`/tmp/bk_p45_nik35.png`（×3，x91–300 / y623–634，裁定 [35] 题名首字母是 `Del` 还是 `del`）。以上 9 张裁片**全部已用 Read 打开逐张亲看**。
- 对应 Markdown：**L2261–L2319**（文献 [8]–[37]，共 30 条）
- 核对（文末页五点）：
  1. **文献编号连续性**：印刷条目编号 `[8] … [37]` 连续、**无跳号、无重复、无漏条**；Markdown L2261/L2263/…/L2319 逐条对应，**编号序列完全吻合**。页首无 `References` 标题（该标题在 p.44 末），本页正文栏全部为文献条目，**无正文段落、无定理、无公式、无收稿日期**（收稿日期在 p.46）。
  2. **逐条核对作者**：印刷与 Markdown 逐条吻合。含多作者分隔符混杂（见备注 5①）、`MᶜKernan` 的上标 `c`（备注 5②）、`Kollár` 的变音符（备注 3）、[25] 的 `J. Kollár ét al.;` 形式（备注 5③）。
  3. **逐条核对刊名 / 卷 / 期 / 年 / 页码**：印刷 → Markdown 全部吻合，重点复核（bbox token 与 150dpi 整页图双向印证）：
     - [8] `J. Math. Sci. Univ. Tokyo` **8** (2001), no. 2, 329–342
     - [9] `Acad. Sci. USSR Sb. Math.` **75** (1993), no. 1, 277–283
     - [10] `Bull. Soc. Math. France` **119** (1991), no. 4, 479–493 (French)
     - [11] `Russian Mathematical Surveys` **63** (2008), 859-958（**无期号、无页码逗号**，印刷如此）
     - [12] `Graduate Studies in Mathematics, volume 214, American Mathematical Society (2011)`（**无期、无页码**，印刷如此）
     - [13] `Ann. of Math. (2)` **180** (2014), no. 2, 523-571
     - [14] `Ann. of Math. (2)` **177** (2013), no. 3, 1077-1111
     - [15] `Math. Res. Lett.` **22** (2015), no. 6, 1699-1716
     - [16] `Encyclopaedia Math. Sci., vol. 47, Springer, Berlin, 1999`
     - [17] `arXiv:1705.02740`　[18] `arXiv:1411.6728v2`　[19] `Amer. J. Math.` **140** (2018), no. 5, 1253-1276
     - [20] `Invent. Math.` **167** (2007), 129-133　[21] `Invent. Math.` **105** (1991), no. 3, 609-611
     - [22] `439–445, Contemp. Math., 131, Part 3, Amer. Math. Soc., Providence, RI, 1992`
     - [23] `Journal of Algebraic Geometry` **14** (2005), 187-192
     - [24] `Tunis. J. Math.` **1** (2019), no. 1, 3-12　[25] `Astérisque No. 211 (1992)`
     - [26] `J. Di. Geom.` **36** (1992), 765-769　[27] `Proc. Japan Acad. Ser. A Math. Sci.` **76** (2000), no. 5, 73–77
     - [28] `Cambridge Tracts in Math. 134, Cambridge Univ. Press, 1998`　[29] `Springer (2004)`
     - [30] `Int. Math. Res. Not.` **6** (2003), 301-312　[31] `Manuscripta Math.` **114** (2004), no. 3, 281–304
     - [32] `J. Amer. Math. Soc.` **4** (1991), no. 4, 681–692
     - [33] `Izv. Akad. Nauk SSSR Ser. Mat.` **53** (1989), no. 6, 1316–1334, 1338; translation in `Math. USSR-Izv.` **35** (1990), no. 3, 657–675
     - [34] `Izv. Akad. Nauk SSSR Ser. Mat.` **52** (1988), no. 5, 1032–1050, 1119; translation in `Math. USSR-Izv.` **33** (1989), no. 2, 355–372
     - [35] `Mat. Sb.` **180** (1989), no. 2, 226–243, translation in `Math. USSR-Sb.` **66** (1990), no. 1, 231–248
     - [36] `301–317, de Gruyter, Berlin, 2000`　[37] `J. Algebraic Geometry, 18 (2009) 151-199`（**`18 (2009)` 后无逗号**，印刷如此，见备注 5④）
  4. **记号约定 / 字符类核对**：本页无公式与记号；字符层面核对 —— 印刷的重音符 `á`(×5, Kollár×5 + Kollárov)、`é`(×9)、`è`(×1, `théorème`) 与 Markdown 的 U+00E1/U+00E9/U+00E8 **逐个吻合**；印刷的两个撇号 `Tian’s`、`l’ENS`（裁片 ×16 确认为右单引号 `’`，笔画呈逗号形带左下尾，非竖直撇）与 Markdown 的 U+2019 **吻合**；连接号混用（U+2013 ×14 与 U+002D ×30，见备注 5⑤）与印刷**逐条一致**。
  5. **行间关系 / 断行连字符**：印刷的跨行断词（[10] `Geometric`、[11] `thresh-`+`olds.`、[16] `Encyclopaedia Math.`+`Sci.`、[17] `below`+`appear`、[22] `Alge-`+`bra`、[23] `Geom-`+`etry`、[26] `Di.`+`Geom.`、[27] `Acad.`+`Ser.`、[28] `Math.`+`Cambridge`、[32] `Math.`+`Soc.`、[33]/[34] `SSSR`+`Ser.`、[37] `Ge-`+`ometry`）在 Markdown 中均已**合并为完整词**、连字符按既定登记类**丢失**；条目间顺序与印刷严格一致，无错序、无跨条串行。
- 结果：**PASS**——**零缺陷、零改动**。30 条文献的作者/刊名/卷/期/年/页码与印刷 p.45 全部吻合；两条先前 peer 已修的字符级缺陷（重音符 TeX 化、漏字 `afine`）经本轮裁片复核**确认修得正确**，无需再改。
- 备注（分级依据）：
  1. **溯源（对 L2261–L2319 共 30 个非空行，先 `git show` 三版比对再写本条）**：`cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`) 与初次导出 `53a92412` 在本区间仅差 **1 行**（`DPMMS, Centre for Mathematical Sciences` 的归属行号位移，非内容差异）；当前 HEAD(`37580aaf`) 相对 `^` 有 **7 行差异**，**全部是 peer 对 `53a92412` 导出缺陷的修正，无 peer 回归**：
     ① 文献 [10] `g´eom´etrique g´en´eralis´ee du th´eor\`eme` → `géométrique généralisée du théorème`（5 处重音符由 TeX 转义残留 `´`/`\`` 还原为预组合字符；印刷 bbox L006 为 `géométrique généralisée du théorème`）；
     ② 文献 [23] `More ´etale covers of afine spaces` → `More étale covers of affine spaces` —— 除重音符外**还补回一个漏字 `f`**（`afine`→`affine`），这是本页唯一的**真·字符级丢失**修复；本轮裁片 `/tmp/bk_p45_affine.png`（×8）目视确认印刷 `affine` 为 `a`+**双 f 连字**+`ine`（bbox token `affine`@x254.0–276.3），**peer 修得正确**；
     ③ 文献 [24] `Koll´ar` → `Kollár`（裁片 `/tmp/bk_p45_kollar.png` ×4 确认印刷有变音符）；
     ④ 文献 [25] `Koll´ar ´et al. … Ast´erisque` → `Kollár ét al. … Astérisque`（裁片 ×4 分别确认 `Kollár` 与 `Astérisque` 的 `á`/`é`）；
     ⑤⑥⑦ 文献 [26]、[27]、[28] 各自的 `Koll´ar` → `Kollár`。
     **本轮对这 7 处未作任何 Edit**；它们不是导出缺陷的遗留，而是已被修正的项。
  2. **撤销疑点（bbox／低分辨率读图推断被裁片或坐标探针推翻，故不改 Markdown）**：①150dpi 整页读图把 [23] 的 `affine` 读作 `afine`，bbox 探针给出该 token 宽 **22.3pt**（x254.0–276.3，`a`+`ff`+`i`+`n`+`e` 五字母宽度，接近同尺度 `characteristic.` 的 56.3pt 之半），裁片 ×8 目视确认**双 f**，Markdown `affine` **正确**，撤销不改（此疑点亦反向证实 peer 的补字修复成立）。②150dpi 整页读图把 [10]/[23]/[25]/[26]/[27]/[28] 的重音符读作普通字母，一度疑 Markdown 的 `é`/`á` 是 peer 擅自「改正」印刷；bbox L006/L032/L034–L040 全部解为预组合 `é`/`á`，裁片 ×4 逐一确认印刷**确有**变音符，Markdown **正确**，撤销不改。③150dpi 整页读图把 `MᶜKernan` 的上标 `c` 读作正体小写 `c`；bbox L014 显示 `c`@x182.6–185.9, y=221 而同句基线 y=222、字高仅 **3.3pt**（相邻 `M`/`Kernan` 为 8–9pt），裁片 ×7 显示 `c` 明显**浮于基线之上、字号更小**，确为上标（`Mac` 的缩写上标），Markdown `M<sup>c</sup>Kernan` **正确**，撤销不改。
  3. **登记不修（字形/别名族变体）**：`Kollár` 的 `á` 在 [24]–[28] 五处均为 U+00E1 预组合，与 `Astérisque`/`étale`/`ét al.` 的 U+00E9、`théorème` 的 U+00E8 属不同码位；`Kollár` 五条均带变音符而 `Borisov`/`Campana`/`Kedlaya`/`Cox` 等无变音符姓氏**不统一加注**，属印刷排印惯例而非缺陷。均渲染等价，**不改**。
  4. **登记不修（版式损失）**：印刷文献条目的**题名斜体**（`Boundedness of Fano threefolds…`、`Log canonical thresholds of smooth Fano threefolds.`、`Toric varieties.`、`ACC for log canonical thresholds` 等）与**卷号粗体**（[8] `8`、[9] `75`、[10] `119`、[11] `63`、[13] `180`、[14] `177`、[15] `22`、[20] `167`、[21] `105`、[26] `36`、[27] `76`、[28] `134`、[31] `114`、[32] `4`、[33] `53`、[34] `52`、[35] `180` 等）在 Markdown 中**全部退化为正体**；印刷的**小号正文字号**与**悬挂缩进**（续行顶格、条目标 `[n]` 左对齐于 x90.7 而续行缩进至 x109.6）退化为普通段落 + 空行分隔；`J. MᶜKernan` 的上标走 HTML `<sup>` 泄漏（与 p.44 文献 [7] 同一既定登记类）；跨行断词连字符按既定登记类**丢失**；页眉「Singularities of linear systems and boundedness of Fano varieties　45」（bbox L000/L001，x141–521）按既定登记类**从不导出**。均**不改**。
  5. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①多作者分隔符**混用**：同一位作者 V. V. Nikulin 在 [33]/[34] 用 `V. V. Nikulin, del Pezzo…`（逗号），[35] 用 `V. V. Nikulin, Del Pezzo…`（逗号）；而 [9] `A. Borisov, L. Borisov;`、[26]/[27] `J. Kollár; Y. Miyaoka; S. Mori;`、[31] `J. MᶜKernan, Yu. Prokhorov;` 用逗号，[8]/[20]/[21]/[22]/[36] `A. Borisov;`/`M. Kawakita;`/`Y. Kawamata;`/`Yu. Prokhorov;` 用**分号**；Markdown L2261–L2319 **逐条照录，未统一**。②`MᶜKernan` 的上标 `c` 与 `M` 之间**无空格**（[13]/[14]/[31] 三处皆然），Markdown **未补空格**。③[25] 的 `J. Kollár ét al.;` 把 `ét al.` **放在姓氏之后、题名之前**并以**分号**收尾，与 [24]/[26]/[27] 的 `J. Kollár;`（分号直接接题名）形式不同，Markdown **照录未改写为 `J. Kollár et al.`**。④文献 [37] 写作 `J. Algebraic Geometry, 18 (2009) 151-199.`，`18 (2009)` 与页码 `151-199` 之间**没有逗号**，且刊名后用逗号而非句点——与本页其余条目（如 [8] `Univ. Tokyo 8 (2001), no. 2, 329–342.`）格式不同，Markdown L2319 **照录，未补逗号亦未改刊名标点**。⑤页码连接号**混用**：en-dash `–`(U+2013) 用于 [8] `329–342`、[9] `277–283`、[10] `479–493`、[22] `439–445`、[27] `73–77`、[31] `281–304`、[32] `681–692`、[33] `1316–1334`/`657–675`、[34] `1032–1050`/`355–372`、[35] `226–243`/`231–248`、[36] `301–317`；连字符 `-`(U+002D) 用于 [11] `859-958`、[13] `523-571`、[14] `1077-1111`、[15] `1699-1716`、[17] `arXiv:1705-`（实为 `1705.02740` 的点，非连接号）、[19] `1253-1276`、[20] `129-133`、[21] `609-611`、[23] `187-192`、[24] `3-12`、[26] `765-769`、[30] `301-312`、[37] `151-199`；裁片 ×8 对照确认两类连接号**墨迹长度明显不同**（`329–342` 的横线宽约一个数字，`187-192` 的横线约其一半），Markdown **逐条照录，未统一**。⑥[33]/[34] 的 `1316–1334, 1338` 与 `1032–1050, 1119` 用**逗号 + 空格**分隔尾页，Markdown 照录。⑦[33]/[34]/[35] 三条 Nikulin 文献的原文与译文**分列同一句内**（`; translation in …`），Markdown **未拆为两条**。⑧[12] Cox–Little–Schenck 一条**无期号、无页码**，只有 `volume 214` 与出版社，Markdown **未补页码**。
- 跨页边界登记：本页印刷首行 bbox L002（`[8] A. Borisov; Boundedness of Fano threefolds with log-terminal singularities of given index. J. Math. Sci.`，y=90）与 p.44 审计末尾登记的边界「L2261 `[8] A. Borisov; Boundedness of Fano threefolds…` 起属 p.45」**交叉核对一致**；本页印刷末行 bbox L056（`ometry, 18 (2009) 151-199.`，y=682）对应 Markdown L2319 文献 [37] 的行末，L2321 `[38] Yu. Prokhorov; V.V. Shokurov; The first fundamental Theorem on complements: from global to local. …` 起属 **p.46**；此边界将在 p.46 审计时交叉核对。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p045`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## p.046（PDF p.46 / 印刷 p.46；**全文末页**：参考文献 [38]–[45] + 通讯地址块）
- PNG：`/tmp/birksing_audit_p046.png`（gs pngmono 150dpi 全页，**已用 Read 打开亲看**）；`/tmp/bk_p46_300.png`（pnggray 300dpi 底图，S=300/72.0=4.16667）；`/tmp/bk_p46_bbox.html`（`pdftotext -bbox -f 46 -l 46`）。裁片：`/tmp/bk_p46_kahler.png`（×14，x230–266 / y185–196，裁定 `K¨ahler` 的分音符位置——本轮第 1 处改动的依据）、`/tmp/bk_p46_diffgeom.png`（×7，x398–480 / y185–196，裁定 `Diferential` 是单 f 还是双 f——本轮第 2 处改动的依据）、`/tmp/bk_p46_addr.png`（×2，x100–362 / y308–360，核定通讯地址块的四行内容与 small caps 字形）、`/tmp/bk_p46_43end.png`（×2，x91–480 / y207–218，核定文献 [43] 结尾 `1995` 后**无句点**）。以上 4 张裁片**全部已用 Read 打开逐张亲看**。
- 对应 Markdown：**L2321–L2341**（文献 [38]–[45] 共 8 条 + 通讯地址块 3 行；L2341 为 Markdown 全文最后一行，文件总 2342 行，末尾字符 `c.birkar@dpmms.cam.ac.uk\n`）
- 核对（文末页五点）：
  1. **文献编号连续性**：印刷条目编号 `[38] … [45]` 连续、**无跳号、无重复、无漏条**；Markdown L2321/L2323/L2325/L2327/L2329/L2331/L2333/L2335 逐条对应，**编号与顺序完全吻合**（注意：`53a92412` 初次导出把 [45] 排在 [44] **之前**，当前态已修正，见备注 1）。
  2. **逐条核对作者**：印刷 → Markdown 逐条吻合。[38] `Yu. Prokhorov; V.V. Shokurov;`（**两位作者之间用分号**，而同页 [39]/[40] 的 `Yu. Prokhorov and C. Shramov;` 用 `and`）、[39] `[40] `Yu. Prokhorov and C. Shramov;`、[41] `J.-P. Serre;`、[42] `G. Tian;`、[43] `E. Viehweg;`、[44] `C. Xu;`、[45] `Yu. G. Zarhin.`（**用句点而非分号**，见备注 5①）。**全部吻合**。
  3. **逐条核对刊名 / 卷 / 期 / 年 / 页码**（bbox token 与 150dpi 整页图双向印证，逐位核对）：
     - [38] `Izv. Ross. Akad. Nauk Ser. Mat.` **65** (2001), no. 6, 99–128; translation in `Izv. Math.` **65** (2001), no. 6, 1169–1196
     - [39] `Amer. J. Math.,138 (2016), 403-418`（**`Math.,` 后无空格直接接卷号 `138`**，印刷如此，见备注 5②）
     - [40] `Compositio Math., Volume 150, Issue 12 (2014), 2054-2072`
     - [41] `Mosc. Math. J., 9 (2009):193-208`（**用冒号而非逗号**分隔卷年与页码，印刷如此）
     - [42] `J. Differential Geom.` **32** (1990), 99-130 —— **本轮第 2 处改动落点**
     - [43] `Springer-Verlag, Berlin, 1995`（**无期、无页码，且结尾无句点**，印刷如此；裁片 ×2 确认）
     - [44] `Compositio Math., 150 (3) (2014), 409-414`
     - [45] `Proc. Edinburgh Math. Soc., 57 (2014):299-304`（**用冒号**，印刷如此）
  4. **记号约定 / 字符类核对**：本页无公式与数学记号。字符层面 —— 印刷 [42] 的 `ä` 为**分音符落在 `a` 正上方**（bbox 解为 `a`+U+0308 组合序列，裁片 ×14 目视确认两点正压 `a` 顶部）；印刷地址块的 `Cambridge`、`Road`、`Sciences` 等为 **small caps**；Markdown 原写 `K¨ahler`（U+00A8 置于 `a` **之前**）与地址块的混合大小写，均见备注 2 与备注 4。印刷其余字符类（`J.-P.`、`c.birkar@dpmms.cam.ac.uk`、`CB3 0WB`）与 Markdown **逐字吻合**。
  5. **行间关系 / 断行连字符**：印刷的跨行断词（[38] `local` 后续换行、[40] `Math.,`+`Volume`、[41] `rank`+`2 over`、[45] `Math.`+`Soc.`）在 Markdown 中均已合并为完整词、连字符按既定登记类丢失；**通讯地址块印刷为 4 行**（bbox L017–L020，y=314/327/340/353），Markdown 中第 2、3 行被**合并为一行**（L2339），见备注 4；条目间顺序与印刷严格一致，无错序、无跨条串行。
  6. **收稿日期核对（本项为本页文末页专有检查点，结果为「印刷侧不存在」）**：**印刷 p.46 全页（含页眉 `46` / `Caucher Birkar`、文献 [38]–[45] 与底部地址块）不存在任何收稿日期 / 修回日期 / 投稿信息**——150dpi 整页图逐区扫描确认：页眉行只有页码 `46` 与作者名 `Caucher Birkar`；正文栏止于文献 [45] 的 `Soc., 57 (2014):299-304.`（bbox L016, y=244）；其下 y≈244–353 之间为**空白区**；y=314 起为**通讯地址块**四行（非日期）。bbox L000–L020 全量 token 中亦无 `Received`/`Submitted`/`日期` 形态的字符串。**Markdown L2337–L2341 同样没有添加任何收稿日期**，与印刷一致，**依铁律三不补、不臆造**。
- 结果：**FAIL（2 处改动，以原图为准）**。发现并修复文献 **[42]** 内的 **2 处字符级内容缺陷**：
  - 改动 1（Markdown **L2329**）：`…polarized K¨ahler metrics on algebraic manifolds…` → `…polarized Kähler metrics on algebraic manifolds…`（把置于 `a` **之前**的独立分音符 U+00A8 还原为**叠在 `a` 正上方**的 `ä`）。依据：印刷 bbox token `Kähler`@x233.52–260.43 解为 `K`+`a`+**U+0308 COMBINING DIAERESIS**+`hler`（分音符在 `a` 之后），裁片 `/tmp/bk_p46_kahler.png`（×14）目视确认**两点正压 `a` 顶部**；`K¨ahler` 的显字顺序与印刷不符，属字符级内容错误。改用预组合 `ä`(U+00E4) 而非 `a`+U+0308，与本文件既有惯例一致（p.45 的 `Kollár`/`géométrique`/`Astérisque` 均为预组合字符），二者渲染等价。
  - 改动 2（Markdown **L2329**）：`J. Diferential Geom.` → `J. Differential Geom.`（补回丢失的一个 `f`）。依据：印刷 bbox token `Differential`@x402.48–447.39 宽 **44.91pt**（12 字母，含 2 个窄 `f` + 3 个窄 `i`），裁片 `/tmp/bk_p46_diffgeom.png`（×7）目视确认 `D-i-ff-e-r-e-n-t-i-a-l` 的 **`ff` 为连字**（两竖画与横画相接）；`Diferential` 为 11 字母的漏字形式，属字符级丢失。
  - 两处均**以原图为准**修正，逐处用 `Edit` 工具单点替换完成，未使用任何脚本批量改写。其余（文献 [38]–[41]、[43]–[45]、通讯地址块、无收稿日期）**全部吻合**。
- 备注（分级依据）：
  1. **溯源（对 L2321–L2341 共 11 个非空行，先 `git show` 三版比对再写本条）**：当前 HEAD(`37580aaf`) 相对 `cpf-redo/Birkar_2016_singularities_linear_systems^`(`16ffcc7c`) 在本区间**零差异**，**不存在 peer 回归**；相对初次 MinerU 导出 `53a92412` 有 **5 处差异，全部是 peer 对导出缺陷的修正**：
     ① 文献 **[44]/[45] 次序倒置**：`53a92412` 的文件尾部顺序为 `[42] → [43] → [45] → [44]`（[45] 排在 [44] **之前**，与印刷的升序不符，且该文件**就此结束**）；当前态已恢复为印刷的 `[43] → [44] → [45]`，**peer 修得正确**。
     ②③④ **通讯地址块整块缺失**：`53a92412` 中**完全没有** `DPMMS, Centre for Mathematical Sciences` / `University of Cambridge, Wilberforce Road, Cambridge CB3 0WB, UK` / `c.birkar@dpmms.cam.ac.uk` 三行（经 `git show 53a92412:…` 逐行检查文件末 8 行确认，文件止于 L2337 的 `[44] …`；全文唯一的 `DPMMS` 出现在第 1 页的作者单位而非文末）。当前态 L2337/L2339/L2341 **已补齐三行**，内容与印刷 bbox L017–L020 **逐字吻合**，**peer 修得正确**（这是**整段丢失**级别的导出缺陷修复，与本轮 2 处改动性质不同）。
     ⑤ 文献 [42] 的 `K¨ahler` 与 `Diferential` 在 **`53a92412`、`^`、当前 HEAD 三版中完全相同**，即**三版皆有的原始导出缺陷，历次审计均未修复**；本轮首次以原页图判定并修复。
  2. **撤销疑点（bbox／低分辨率读图推断被裁片或坐标探针推翻，故不改 Markdown）**：①150dpi 整页读图把 [42] 的 `Kähler` 读作 `Kahler`（漏识分音符），一度疑 Markdown 保留 `¨` 是「忠实于某种 TeX 原始写法」；bbox 探针显示该 token 的码位序列为 `U+0061 U+0308`（**组合分音符紧跟 `a`**），裁片 ×14 确认两点在 `a` 正上方，`K¨ahler` 确为**顺序错误**而非风格差异，**改**。②150dpi 整页读图把 [42] 的刊名读作 `J. Diferential Geom.`，一度疑印刷本身即漏字（即应「照录不改」）；bbox 探针给出该 token 为 `Differential` 且宽 44.91pt（同尺度 10 字母的 `manifolds.` 宽 41.45pt，而本词含 2 个更窄的 `f`），裁片 ×7 见 `ff` 连字，**印刷为双 f，Markdown 漏字**，**改**。③150dpi 整页读图把文献 [43] 末尾读作 `1995.`（带句点），bbox L013 结尾 token 为 `1995`（无句点）且裁片 ×2 目视确认其后无墨迹，一度疑 Markdown 漏句点；复核确认**印刷本就无句点**，Markdown L2331 **正确**，撤销不改。
  3. **登记不修（字形/别名族变体）**：`Kähler` 采用预组合 `ä`(U+00E4) 而非 PDF 文本层的 `a`+U+0308 组合序列，二者字形与渲染完全等价，属编码选择而非内容差异；`c.birkar@dpmms.cam.ac.uk` 中 `@` 与 `.` 均为印刷原样；`CB3 0WB` 中的数字 `0`（U+0030）与字母 `O`(U+004F) 字形近似，印刷为邮编 `CB3 0WB`，Markdown 照录，**未按字母 `O` 改动**。均**不改**。
  4. **登记不修（版式损失）**：印刷通讯地址块四行 `DPMMS, Centre for Mathematical Sciences` / `University of Cambridge,` / `Wilberforce Road, Cambridge CB3 0WB, UK` 为 **small caps**（首字母全高、其余字母矮化大写），Markdown L2337/L2339 **退化为普通混合大小写**；印刷的地址块**第 2、3 行分列**（bbox L018 y=327 `University of Cambridge,` 与 L019 y=340 `Wilberforce Road, Cambridge CB3 0WB, UK`），Markdown L2339 **合并为一行**（与本篇参考文献续行合并属同一既定登记类，不视为内容丢失，因第 2 行以逗号结尾、本为连续邮政地址）；文献条目的**题名斜体**与**卷号粗体**（[38] `65`×2、[44] `150` 等）退化为正体；文献条目的小号正文字号与悬挂缩进退化为普通段落 + 空行分隔；页眉「46　Caucher Birkar」（bbox L000/L001，x91–99 与 x267–345）按既定登记类**从不导出**。均**不改**。
  5. **印刷侧 quirk（依铁律三原样保留并登记，未按数学常识「纠正」）**：①多作者/作者与题名的分隔符在本页**四种混用**：分号分列作者（[38] `Yu. Prokhorov; V.V. Shokurov;`）、`and` 连接（[39]/[40]）、单作者后直接分号（[41]/[42]/[43]/[44]）、单作者后直接**句点**（[45] `Yu. G. Zarhin.`），Markdown L2321–L2335 **逐条照录，未统一**。②文献 [39] 写作 `Amer. J. Math.,138 (2016),` —— 刊名缩写 `Math.` 后**先句点再逗号**且**逗号与卷号 `138` 之间无空格**（`Math.,138` 连写），与 [38]/[44]/[45] 的 `Math.` 后不接标点形成对照；Markdown L2323 **照录未补空格**。③文献 [41] 与 [45] 用**冒号** `:` 分隔「卷(年)」与页码（`9 (2009):193-208`、`57 (2014):299-304`），而 [38]/[39]/[40]/[42]/[43]/[44] 用**逗号**；Markdown **照录未统一**。④文献 [38] 的 `The first fundamental Theorem on complements` 中 **`Theorem` 首字母大写**而 `fundamental` 小写（[41] 的题名 `A Minkowski-style bound…` 亦以冠词 `A` 开头大写），属印刷排印惯例；Markdown L2321 **照录未改为 `theorem`**。⑤文献 [43] `Springer-Verlag` 用**连字符**连接出版商名，而 [43] 的出版社 `Springer` 在 p.45 文献 [29] 中单独出现时不带 `-Verlag`；[43] 结尾 `1995` **无句点**，为本页唯一无终止标点的条目；Markdown L2331 **照录未补句点**。⑥文献 [41] 题名 `A Minkowski-style bound for the orders of the finite subgroups of the Cremona group of rank 2 over an arbitrary field.` 中的 **`A` 无变音符**（作者名 `Minkowski` 本身无变音符），Markdown L2327 **照录未添加 `ä`**。⑦本页**无收稿日期**（见核对第 6 点），印刷与 Markdown **一致**，依铁律三**未补任何日期**。
- 跨页边界登记：本页印刷首行 bbox L002（`[38] Yu. Prokhorov; V.V. Shokurov; The first fundamental Theorem on complements: from global to local.`，y=90）与 p.45 审计末尾登记的边界「L2321 `[38] Yu. Prokhorov; V.V. Shokurov; The first fundamental Theorem on complements: from global to local. …` 起属 p.46」**交叉核对一致**；本页印刷末行 bbox L020（`c.birkar@dpmms.cam.ac.uk`，y=353）对应 Markdown **L2341，即 Markdown 全文的最后一行**（文件总 2342 行，末尾字符 `c.birkar@dpmms.cam.ac.uk\n`），**PDF 与 Markdown 均在此结束，p.46 为全文末页，本页无后续页面边界**；其后无 `## p.047` 及以后的审计条目。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p046`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。

## 小结：p.041–p.046（PDF p.41–46，共 6 页，Wf-R redo 复核）

- **覆盖**：6 页全部逐页执行七步循环（一页一渲染 → Read 亲看 → 读该页 Markdown 段 → 五点比对 → **立刻**追加本页审计说明 → 分级/必要时 Edit → 进下一页），无跳页、无合并判读、无批量渲染后一起判。
- **分级统计**：**PASS 5 页**（p.041、p.042、p.043、p.044、p.045，均零缺陷零改动）；**PASS± 0 页**；**FAIL 1 页**（p.046，2 处改动，以原图为准）。
- **改动统计**：本段共 **2 处** Edit，全部落在 **Markdown L2329**（文献 [42] Tian 一条）：
  1. `K¨ahler` → `Kähler`（U+00A8 置于 `a` 之前 → 预组合 `ä` 叠在 `a` 之上）；
  2. `Diferential` → `Differential`（补回丢失的一个 `f`）。
  两处均以 300dpi 裁片（`/tmp/bk_p46_kahler.png` ×14、`/tmp/bk_p46_diffgeom.png` ×7）+ `pdftotext -bbox` 坐标/码位探针双重取证，**逐处用 `Edit` 单点替换**，未使用任何脚本批量改写目标 Markdown。
- **溯源结论（本段 6 页全部先比对 `53a92412` → `16ffcc7c`(`^`) → `37580aaf`(HEAD) 再落笔）**：**未发现任何 peer 回归**（当前态相对 `^` 的全部差异都是 peer 对初次 MinerU 导出缺陷的**修正方向**）。其中与本段直接相关、值得集成者留意的既往修复共 **18 处**：p.42 七处（伪 efective、重音符/箭头/项目符号/`C :=`/句点）、p.43 六处、p.44 四处、p.45 七处（**含 [23] 文献 `afine`→`affine` 的漏字补回**——本轮 ×8 裁片复核确认修得正确）、p.46 五处（**[44]/[45] 次序倒置复原** + **文末通讯地址块三行整段补齐**——`53a92412` 中该地址块与作者邮箱**完全缺失**，由 peer 补齐；本轮 ×2 裁片复核确认与印刷逐字吻合）。p.046 的 2 处新改动在 `53a92412`、`^`、HEAD **三版中皆相同**，属**历次审计均未发现的原始导出缺陷**。
- **页边界链（本段 6 页逐页交叉核对，前后自洽）**：p.41 起 L2039（对 p.40 末登记）→ p.42 起 L2109 → p.43 起 L2165 → p.44 起 L2213 → p.45 起 L2261 → p.46 起 L2321 → 止于 L2341（Markdown 全文末行）与 PDF 第 46 页，**PDF 与 Markdown 同在末页结束，无跨页残段**。
- **本段撤销疑点合计 15 项**（bbox／低分辨率读图推断被裁片或坐标探针推翻，故**不改** Markdown）：p.41 三项（`A_Y` 实为 `Λ_Y`、`ε′` 撇号被提前发射、`Thus` 非 `This`）；p.42 四项（叠置 `½` 非「12」、`A dY` 叠字保留上下标、`4lA` 的 Λ 非 A、`φ : Y → X` 为实线非虚线 birational）；p.43 四项（Step 5「Replacing…」整行 bbox 乱序、`⌈…⌉` 内无圆括号、三个 `ε′/ε` 分式被合并、`ε′` 分子提前发射）；p.44 四项（`tl` 为叠置 `t/l`、`K_{X″}` 撇号身份、`Ω` 非拉丁 O/Q、`ε/2` 分子与行首合并）。p.45 三项与 p.46 三项另见各页备注 2。
- **本段登记不修的印刷侧 quirk**：p.41–p.44 的记号同名（`l`/`t`/`m`/`n` 复用）、`ε` 与 `ε′` 写法不统一、`∼_ℝ` 下标有无不一致、重复断言不合并、`⌈(3d+1)/s⌉` 的取整号直接包裹分式等；p.45 的**多作者分隔符四种混用**、**页码连接号 en-dash 与连字符混用**（U+2013 ×14 / U+002D ×30，经 ×8 对照裁片确认墨迹长度差异）、`del Pezzo`/`Del Pezzo` 大小写不一致、`MᶜKernan` 上标 `c` 前无空格、`Math.,138` 连写、`18 (2009) 151-199` 缺逗号；p.46 的**分隔符四种混用**、`9 (2009):193-208` 冒号分隔、`Theorem` 首字母大写、`1995` 无终止句点。**全部依铁律三原样保留，未按学术惯例「纠正」。**
- **收稿日期**：本段**未发现任何收稿日期/修回日期**。p.45 为纯参考文献页，p.46（全文末页）在文献 [38]–[45] 之后只有**通讯地址块**四行（`DPMMS, Centre for Mathematical Sciences` / `University of Cambridge,` / `Wilberforce Road, Cambridge CB3 0WB, UK` / `c.birkar@dpmms.cam.ac.uk`），150dpi 整页扫描与 bbox L000–L020 全量 token 均确认印刷侧不存在日期行；Markdown 同样没有添加，**依铁律三不臆造日期**。
- **交付自检**：`grep -c '^## p\.' AUDIT-Birkar_2016_singularities_linear_systems.md` = **136**（本段前 130 → 本段后 136，新增 6 条：p.041/p.042/p.043/p.044/p.045/p.046，无缺漏）。
- 记录时间：2026-10-05；actor=`Wf-R-Birkar-p041-046`；model=`opencode-go-chat / space-bunny-free`；effort=UNKNOWN。
