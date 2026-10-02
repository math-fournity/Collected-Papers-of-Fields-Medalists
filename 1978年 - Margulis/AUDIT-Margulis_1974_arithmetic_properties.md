# AUDIT — Margulis_1974_arithmetic_properties

- 状态：50 页逐页审计及 Markdown 修复已完成；Peer 候选，尚未集成到 canonical main。
- Actor：Peer-P18；model=`gpt-6-luna`；reasoning effort=`max`。
- Git 基线：审计开始时的 `main` / `037602429d3b009f6fc468c732073eb3ddf9875f`；本 worktree 当时从该 OID detached。
- 原件：`Margulis_1974_arithmetic_properties.pdf`，50 PDF 页；Producer=`ABBYY Hot Folder & Scheduling`。
- 模式：扫描页 + ABBYY OCR 文本层。`pdfimages -list` 显示 50 页各含一张 300 ppi、1-bit 全页图；提取文本层 216743 bytes、无 U+FFFD。按 50 页全页视觉审计；OCR/文本提取只作对照，不作印刷裁决。
- MinerU：`basic` / `ocr`，`middle_json.json` 标记 MinerU 3.4.4；该文件无 `doc_id` 字段。
- 唯一目标 Markdown 的审计前 SHA-256：`7fa7ee59a1c4b3c4fa88254a1ab9aa3d51f3f1b28560e7ccb4e26da2ce8aeec7`。
- 修复后 Markdown SHA-256：`9afd65e79be33a9ec3faf483d61c3bfa3b7271009e80ddcd86b153e4d0ac259f`；Markdown 修复提交：`5a07040e1302967c763dbde61a87d5d77e9c96c1`；审计前最后一页记录提交：`1596ce200170e85fb6c0d8635bae3c85ffe5a8b6`。
- 页签格式：每页记录实际事件时间、actor、model 与 effort；Peer 不更新根 `AUDIT-INDEX.md` 或 `AUDIT-PROGRESS.log`。
- 结果解释：逐页“结果”记录相对审计前 MinerU Markdown 的差异；本文件末尾“Markdown 修复登记”记录当前处置和复读核验。

## p.001（PDF p.1；题名与目录前置页）

- PNG：`audit/Margulis_1974_arithmetic_properties_p001.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p001_toc_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p001_abstract_300dpi.png`。
- 核对：题名、作者、摘要、目录、脚注 1、页脚。
- 结果：FAIL。印刷目录含四项 MinerU Markdown 未录：`§ 16. Группы G Q-ранга 1 (окончание) ... 93`、`§ 17. Некоторые нерешенные задачи теории дискретных подгрупп ... 94`、`Приложение. Свойства корневых разложений ... 95`、`Литература ... 96`；基线 Markdown 的目录在 §15 后即转入脚注。须待 50 页审计完毕后逐处手工补录并复核。
- 源级 quirk：摘要印刷为“...обращением этой теоремы В частности...”——`теоремы` 后无句点；300 dpi 裁片确认，Markdown 忠实保留，不擅改。
- 页面信息：此页是题名/目录前置页；目录把“Введение”标为 50，下一 PDF 页页眉确标印刷页 50。页底印有 `4 Успехи матем. наук, т. XXIX, вып. 1`，保留为原样页底刊物行，不将“4”推作正文页码。
- 签署：2026-10-01 16:14 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.002（PDF p.2 / 印刷 p.50）

- PNG：`audit/Margulis_1974_arithmetic_properties_p002.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p002_formula_300dpi.png`。
- 核对：印刷页眉/页码、§Введение 标题、开篇段落、公式、脚注 1，以及页面末句。
- 结果：FAIL。行间公式末段，印刷为 `..., где g = (...)`；MinerU 基线 Markdown 写作 `..., \text { r   i   n   e } g = (...)`，将“где”误识成无意义字串。300 dpi 裁片确认印刷字为“где”；待逐处手工改正。
- 备注：页眉作者行和印刷页码 50 未收入 Markdown，属非正文页眉/页码省略；本页正文在 `...можно интерпретировать как` 处结束，脚注对应源页例外说明。
- 签署：2026-10-01 16:17 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.003（PDF p.3 / 印刷 p.51）

- PNG：`audit/Margulis_1974_arithmetic_properties_p003.png`（pngmono，150 dpi）。
- 核对：算术子群定义、格点/不可约格定义、Selberg 假设、脚注 1–2 与页面末句。
- 结果：PASS±。逐段目检后，正文与 MinerU Markdown 对应段一致；MinerU 未录页眉运行标题及印刷页码 51（非正文页眉/页码省略）。
- 签署：2026-10-01 16:19 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.004（PDF p.4 / 印刷 p.52）

- PNG：`audit/Margulis_1974_arithmetic_properties_p004.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p004_theorem_note_300dpi.png`。
- 核对：弱/强刚性定理、主定理陈述、段落末尾以及注 1–2。
- 结果：FAIL。主定理中的“связная”被识为“сеязная”；脚注 1 印为“группой движений”，Markdown 写作“грушной движений”。300 dpi 裁片确认源字，均待逐处手工修复。其余核对段落与页面相符。
- 备注：Markdown 未录本页眉作者行与印刷页码 52；属非正文页眉/页码省略。
- 签署：2026-10-01 16:21 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.005（PDF p.5 / 印刷 p.53）

- PNG：`audit/Margulis_1974_arithmetic_properties_p005.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p005_10-1_line_300dpi.png`。
- 核对：主定理结论、对“有理性”定理的证明提纲、引理 10.1 陈述和脚注 1–2。
- 结果：PASS±。对应正文、符号与脚注均与印刷页相符；页眉运行标题和印刷页码 53 未收入 Markdown。源级 quirk：印刷在“лемму 10.1”后有双句点 `10.1..`，Markdown 忠实保留，300 dpi 裁片确认。
- 签署：2026-10-01 16:23 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.006（PDF p.6 / 印刷 p.54）

- PNG：`audit/Margulis_1974_arithmetic_properties_p006.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p006_symbol_defs_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p006_03defs_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p006_0-5_bottom_300dpi.png`。
- 核对：引言收尾与致谢、§0.1–0.5 定义、页面末尾的中心化子定义。
- 结果：FAIL。§0.3 的印刷记号为 `H_{nZ}` 与 `H_Z`；MinerU Markdown 将两个整数环下标都写成小写 `z`（`H_{nz}`、`H_z`），须手工恢复大写 `Z`。其余正文在当前页面范围内对应。
- 源级 quirk 候选：§0.2 的印刷字形见作 `Z_x` 样式，紧接文字却说明“целые p-адические”；MinerU 也记录 `Z_x`。300 dpi 裁片仍显示 x 样小写字形，按印刷原样保留，不推改为 p。
- 签署：2026-10-01 16:26 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.007（PDF p.7 / 印刷 p.55）

- PNG：`audit/Margulis_1974_arithmetic_properties_p007.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p007_definition_top_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p007_commutator_defs_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p007_0-11_300dpi.png`。
- 核对：§0.5 的中心化子定义续句、Lie algebra 交换子记号、§0.6–0.12 定义。
- 结果：FAIL。三处符号/文字失真：①“\(\mathfrak{A}\) в H, т. е.”被写为 `A B H, T. e.`；②§0.5 第二个 Lie algebra 记号，印刷与本节先前定义一致为 \(\mathfrak{S}\)，Markdown 为 `ℊ`；③§0.11 两处印刷 \(\mathfrak{S}\) / \(\mathfrak{S}_{K}\) 被写成男性符号 `♂`。裁片已核印刷原字，待逐处手工改正。
- 源级 quirk：§0.11 印刷“алгебраической h-группы”中小写字形在 300 dpi 仍呈 `h`，Markdown 亦为 h；尽管上下文前文定义了 k-группы，按印刷原样保留并登记。
- 备注：Markdown 未录页眉运行标题和印刷页码 55。
- 签署：2026-10-01 16:30 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.008（PDF p.8 / 印刷 p.56）

- PNG：`audit/Margulis_1974_arithmetic_properties_p008.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p008_1-2_wording_300dpi.png`。
- 核对：§1 标题、1.1、1.2.1–1.2.2、1.3.1–1.3.3 与 1.4 引入句。
- 结果：FAIL。基线 Markdown 行 160 将“нильпотентным радикалом”损坏为混合拉丁/西里尔字串 `Hilьпотентным радикалом`；行 162 将印刷“предположения несущественны”写为“предложения несущественны”。300 dpi 裁片确认原文，两处待手工改正。
- 备注：印刷页眉作者行和页码 56 未收入 Markdown；页内 1.4 引入句在本页结束，后续引理从下一页开始。
- 签署：2026-10-01 16:31 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.009（PDF p.9 / 印刷 p.57）

- PNG：`audit/Margulis_1974_arithmetic_properties_p009.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p009_lemma15_proof_300dpi.png`。
- 核对：引理 1.4.1、引理 1.5 及其证明、§2/2.1–2.1.3 开头。
- 结果：PASS±。对应段落、关系符和证明文字与印刷页相符；Markdown 在“algebraическая / algebraическим”保留混合拉丁字母的轻微 OCR 伪影，未改变可读语义。页眉运行标题及页码 57 未收入 Markdown。
- 源级 quirk：引理 1.5 证明先印 `H' ∩ Λ ≠ {e}`，随后又印 `H' ∩ Λ = {e}`；300 dpi 裁片确认两处均为 H′。Markdown 忠实转录。此记录只说明源页文字内部冲突，不据此裁定引理证明的数学有效性。
- 签署：2026-10-01 16:34 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.010（PDF p.10 / 印刷 p.58）

- PNG：`audit/Margulis_1974_arithmetic_properties_p010.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p010_D1_D2_300dpi.png`。
- 核对：引理 2.1.3 的证明、引理 2.1.4–2.1.5、2.2/2.2.1 及 2.3 陈述。
- 结果：PASS±。本页可见正文、公式、下标及编号与 Markdown 对应；页眉作者行和印刷页码 58 未收入 Markdown。
- 源级 quirk：引理 2.1.3 证明中的印刷包含式把 `((K·D₂)∩F)` 连写两次；300 dpi 裁片确认，MinerU Markdown 忠实复制。它与上下文前面的 D₁ 项似不一致，但按印刷原样登记，不改写或宣称已判定证明对错。
- 签署：2026-10-01 16:35 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.011（PDF p.11 / 印刷 p.59）

- PNG：`audit/Margulis_1974_arithmetic_properties_p011.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p011_exp_map_300dpi.png`。
- 核对：2.3 证明结尾、2.4 Zassenhaus 邻域引理、§3 与 3.1–3.3.2。
- 结果：FAIL。§3.1 中映射的印刷名称是 `exp: 𝔚 → V`；基线 Markdown 写作 `expr: 𝔚 → V`，多出 `r`。300 dpi 裁片确认，待手工改正。其他本页对照项相符。
- 备注：页眉运行标题和印刷页码 59 未收入 Markdown。
- 签署：2026-10-01 16:36 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.012（PDF p.12 / 印刷 p.60）

- PNG：`audit/Margulis_1974_arithmetic_properties_p012.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p012_3-4-1_statement_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p012_3-4-1_300dpi.png`。
- 核对：3.3.3、3.4.1–3.4.3、§4 标题与 4.1–4.2.1。
- 结果：FAIL。3.4.1 的命题主语印刷为希腊大写 `Λ`，基线 Markdown 写成西里尔 `А`；同一证明里的映射印为 `exp: 𝔚 → V`，Markdown 写成 `expr: 𝔚 → V`。300 dpi 裁片确认，均待逐处手工改正。
- 源级/轻微 OCR 记录：3.3.3 的“индекса”在基线 Markdown 字母次序错成“индедса”；§4.1 印刷的“связаная”与 Markdown 相同，按印刷原样保留。页眉作者行和印刷页码 60 未收入 Markdown。
- 签署：2026-10-01 16:38 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.013（PDF p.13 / 印刷 p.61）

- PNG：`audit/Margulis_1974_arithmetic_properties_p013.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p013_4-3_formula_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p013_4-5_roots_300dpi.png`。
- 核对：4.3–4.4.1、§4.5 根系统与子群记号的定义，及本页末的闭子集定义。
- 结果：PASS±。本页公式与定义按可辨字形和版面顺序均有对应。4.3.1 的印刷“Лемма”被 Markdown 写作英文 “Lemma”，属轻微词项 OCR 伪影。
- 源级 quirk / 未闭合解释：4.3.1 前印刷式确有双包含号 `⊂ ⊂ H^u`，Markdown 忠实保留。§4.5 的 (G_\psi) 定义可见记作根号标签 `α∈Φ`，但同段还另定义 (G_\psi^*) 并给出关系式；图像字形与 Markdown 一致，是否为原文记号不一致不在本次转录审计中裁断。
- 备注：未见整段漏录；页眉运行标题和印刷页码 61 未收入 Markdown。
- 签署：2026-10-01 16:41 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.014（PDF p.14 / 印刷 p.62）

- PNG：`audit/Margulis_1974_arithmetic_properties_p014.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p014_formula1_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p014_normalizers_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p014_4-5-1_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p014_4-5-4_300dpi.png`。
- 核对：§4.5 定义式 (1)–(4)、4.5.1 的 1)–3)、引理 4.5.2–4.5.4。
- 结果：FAIL。①式 (1) 的印刷为 `B_{\bar\theta}=P_\theta\cap V_{\varnothing}^{-}`，Markdown 写成 `V_\phi`，丢失负根标记并误识空集下标。②印刷式 (3) 是 `N(V_\theta)=P_\theta, V_\theta=R_u(N(V_\theta))`，式 (4) 是对应的负根式；Markdown 将式 (3) 留成孤立行、把第一组公式误标为 (4)，第二组未标 (4)。③引理 4.5.1 把希腊 `\alpha` 记成拉丁 `a`，2) 把下标 `k` 记成 `h`，3) 的整条 Lie bracket 陈述损坏为不可读混合字串。④引理 4.5.4 结论将 `V_{\varnothing}^{-}` 误为带 prime 的 `V_{\varnothing}'`。均以所列 300 dpi 原页裁片为准，待逐处人工修复。
- 备注：页眉运行标题和印刷页码 62 未收入 Markdown。
- 签署：2026-10-01 16:45 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.015（PDF p.15 / 印刷 p.63）

- PNG：`audit/Margulis_1974_arithmetic_properties_p015.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p015_4-5-5_proof_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p015_4-5-6-8_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p015_4-6-1_wording_300dpi.png`。
- 核对：引理 4.5.4 证明、4.5.5–4.5.8、4.6.1 陈述。
- 结果：FAIL。①4.5.4 证明中印刷 `w∈{}_kW(S,G)`，基线 Markdown 下标写成 `h`。②4.5.5 证明中，印刷 `V_θ` 是 `V=V_∅` 的法向子群，Markdown 写成 `V=V_θ`，并把末尾 `P_∅/N(V_∅)` 下标损坏为 `P_0/N(V_φ)`。③4.5.6 论证中印刷的最大幺幂子群 `V_∅` 被记为 `V_φ`。④4.5.8 中印刷 `u∈R_u(P)_k`，Markdown 下标为 `h`。⑤4.6.1 的“унипотентной подгруппе”被写成“унипотентной водгруппе”。裁片显示这些实际差异；经复核，4.5.5 陈述中“F 是 V 的法向子群”原 Markdown 与印刷一致，并非差异。
- 备注：页眉运行标题和印刷页码 63 未收入 Markdown。
- 签署：2026-10-01 16:49 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.016（PDF p.16 / 印刷 p.64）

- PNG：`audit/Margulis_1974_arithmetic_properties_p016.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p016_4-6-1_exp_xi_300dpi.png`。
- 核对：4.6.1 证明中的指数映射/分裂锥参数、4.6.2、4.7–4.7.2、§5 引入及依赖图。
- 结果：FAIL。4.6.1 印刷为 `exp ξ`（ξ 为开 Weyl 室中任意元素），基线 Markdown 写作 `exper {`；同段 `V=V_∅` 的空集下标又误录为 `V_φ`。300 dpi 裁片确认，待逐处修复。
- 备注：§5 依赖图在 PDF 中可见，MinerU Markdown 含对应 `images/page_15_image_8.jpg` 引用，所示节点与箭头可对应原页图；页眉作者行、印刷页码 64 未收入 Markdown。
- 签署：2026-10-01 16:52 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.017（PDF p.17 / 印刷 p.65）

- PNG：`audit/Margulis_1974_arithmetic_properties_p017.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p017_5-2_lie_algebra_300dpi.png`。
- 核对：§5 引入、5.1、5.2.1–5.2.5 与 5.3 引入。
- 结果：FAIL。5.2 中“代数群 G 的 Lie algebra”印刷记号为 \(\mathfrak{G}\)，基线 Markdown 写成 `Ⓔ`（行 386），损失了 Lie algebra 变量。300 dpi 裁片确认，待手工恢复。
- 备注：5.2.4 标题中的 “Lemma” 为轻微英文标签替换；5.2.3 证明有额外重复等号 `==`，其余页面内容与原图对应。底部刊物页脚 “5 Успехи матем. наук...” 已录入 Markdown；页眉运行标题及印刷页码 65 未收入。
- 签署：2026-10-01 16:53 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.018（PDF p.18 / 印刷 p.66）

- PNG：`audit/Margulis_1974_arithmetic_properties_p018.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p018_5-3-1_statement_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p018_5-4_scope_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p018_5-5_definition_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p018_5-5-proof_start_300dpi.png`。
- 核对：5.3.1、5.4–5.4.3、5.5 定义和 5.5.1 证明开头。
- 结果：FAIL。5.4 的印刷范围是 `M⊂N_R`，基线 Markdown 多出星号写作 `M⊂N_R^*`；5.5 的印刷交集为 `N(\bar U)∩Γ`，Markdown 多写一个 `∩`。两处均改变公式文本，待手工修复。
- 未闭合/轻微 OCR：5.3.1 中 `G_R` 后有小上标，300 dpi 仍不能唯一辨认；Markdown 记为 H，暂不推定替代字形。5.3.1 末尾 `Γ` 与 `γ_g(V)` 的相邻数学块缺分隔，5.5.1 表示定义的括号也有轻微格式差异；不影响本页已确认的核心符号判读。
- 备注：页眉作者行和印刷页码 66 未收入 Markdown。
- 签署：2026-10-01 16:57 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.019（PDF p.19 / 印刷 p.67）

- PNG：`audit/Margulis_1974_arithmetic_properties_p019.png`（pngmono，150 dpi）。
- 核对：5.5.1 证明结尾、5.5.2–5.5.5、§6/6.1 陈述与证明。
- 结果：PASS±。逐段对照后，论述、索引、符号和证明步骤均对应；6.1 中 `algebraическая` 保留了混合拉丁字母的轻微 OCR 伪影。页眉运行标题、印刷页码 67 及边注 `5*` 未录入正文。
- 签署：2026-10-01 16:59 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.020（PDF p.20 / 印刷 p.68）

- PNG：`audit/Margulis_1974_arithmetic_properties_p020.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p020_6-2-1_Tt_300dpi.png`。
- 核对：6.2–6.2.1、6.3.1–6.3.3 与 6.4 定理/证明开头。
- 结果：PASS±。定义、参数和关系符与印刷相符；300 dpi 确认 6.2.1 印刷使用带帽参数 \(T^{\hat t}\)，Markdown 如实记录。轻微 OCR 字词伪影：6.3.2 的俄文连词“и”成为拉丁 `u`，`подгруппой` 成为 `подгрушной`，不改变命题内容。页眉和印刷页码 68 未收入 Markdown。
- 签署：2026-10-01 17:00 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.021（PDF p.21 / 印刷 p.69）

- PNG：`audit/Margulis_1974_arithmetic_properties_p021.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p021_7-2_symbols_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p021_7-2-2_Ru_300dpi.png`。
- 核对：6.4 结论、§7/7.1.1–7.2.3、定义 1–2。
- 结果：FAIL。①7.2.1 印刷交集为 `N_R∩\overline{U'}_R`，Markdown 丢了 `U'` 上的 prime，写成 `N_R∩\overline U_R`，并将它与“Γ-紧”黏连为 `$$\Gamma`。②7.2.2 证明末尾印刷两处均为 unipotent radical `R_u`，Markdown 写成大写下标 `R_U`。300 dpi 裁片确认，待手工修复。
- 备注：本页其余主张和行间记号对应；标题中的页眉运行标题和印刷页码 69 未收入 Markdown。节标题末尾多出的点号属轻微格式伪影。
- 签署：2026-10-01 17:03 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.022（PDF p.22 / 印刷 p.70）

- PNG：`audit/Margulis_1974_arithmetic_properties_p022.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p022_7-5-1_end_300dpi.png`。
- 核对：6.4 证明结尾、7.3.1–7.5.1 陈述与 7.5.1 证明开头。
- 结果：FAIL。7.5.1 证明初始化中，印刷为 `N=N(\bar U), N'=N(\bar U')`；基线 Markdown 在两项间插入 `\_{\text{总}}`，形成无源对应的字串。300 dpi 裁片确认，待手工删除该多余文本。
- 源级注记（与 p.023 对读）：此页 7.5.1 陈述印作 `W⊂U`，p.023 的证明末尾印作 `W\not\subset U`。两者均按源页转录；此处登记为印刷陈述/证明冲突，不改写任一方。
- 备注：页眉作者行和印刷页码 70 未收入 Markdown。
- 签署：2026-10-01 17:05 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.023（PDF p.23 / 印刷 p.71）

- PNG：`audit/Margulis_1974_arithmetic_properties_p023.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p023_expW_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p023_7-5-2_conclusion_300dpi.png`。
- 核对：7.5.1 证明收尾、7.5.2 陈述与证明开头、7.6 开头。
- 结果：FAIL。7.5.1 证明中印刷映射为 `exp \widetilde W ⊂ V`，基线 Markdown 写成 `expr \widetilde W ⊂ V`；7.5.2 证明印刷为 `V=\bar V∩Γ`，基线 Markdown 多了前置负号，写成 `V=-\bar V∩Γ`。300 dpi 裁片确认，待手工修复。
- 源级 quirk（本页内部）：7.5.2 证明先印 `\bar U=\bar W`，随后称由交集生成的 `\bar V` 满足 `\bar V\ne\bar U`；结合 p.022 的 `\bar V` 定义，这些印刷断言表面不相容。Markdown 按原样转录；此任务记录页面异文，不裁决作者本意或整段证明有效性。
- 备注：页眉运行标题和印刷页码 71 未收入 Markdown。
- 签署：2026-10-01 17:08 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.024（PDF p.24 / 印刷 p.72）

- PNG：`audit/Margulis_1974_arithmetic_properties_p024.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p024_7-6_notation_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p024_7-7_dimension_300dpi.png`。
- 核对：7.6 分情况证明、4.5 定理的调用、维数比较及 7.7 开头。
- 结果：FAIL。①在 7.6 中，印刷对面的根子群记作 `V_{\varnothing}^{-}`，Markdown 写为 `V_{\varnothing}'`。②最后维数链的印刷为 `dim(B_\theta^-\widetilde{\times}V_\theta)=dim(B_\theta\widetilde{\times}V_\theta)`；Markdown 第二项的数学分隔符/括号错位，未把整个半直积括入 `dim`。300 dpi 裁片确认两处，待逐处手工修复。
- 备注：页眉运行标题和印刷页码 72 未收入 Markdown。
- 签署：2026-10-01 17:11 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.025（PDF p.25 / 印刷 p.73）

- PNG：`audit/Margulis_1974_arithmetic_properties_p025.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p025_8-1_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p025_8-2_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p025_8-3_eqs_300dpi.png`。
- 核对：8.1.1–8.1.3、8.2 假设与 (w^{-1}) 项、8.3 商空间构造和公式 (1)–(2)、8.4 引入。
- 结果：FAIL。①8.1.1 的条件 (0\le l\le\dim A) 与 (1) 的并集公式被断成空白/孤立公式块。②8.1.2 的映射域/陪域写作 `f_1,…,f_l U∈A`，关系与印刷“映射 U 到 A”的表述不符。③8.1.3 将“множество тех”识为 `mex`。④8.2 把 (T_{w^{-1}}M) 写成 (T_{w-1}M)。⑤8.3 公式 (1) 的 α\(_\lambda\) 变成拉丁 `a_\lambda`，并把 (1)/(2) 标签移错：第一式标签为 (2)，第二式无 (2)。⑥在 8.3 后重复插入了 “8.4. Локажем две леммы”，印刷只见一条 “8.4. Докажем две леммы”。所列页级差异待手工修复。
- 备注：页眉运行标题和印刷页码 73 未收入 Markdown。
- 签署：2026-10-01 17:15 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.026（PDF p.26 / 印刷 p.74）

- PNG：`audit/Margulis_1974_arithmetic_properties_p026.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p026_H_action_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p026_intertwining_eq3_300dpi.png`。
- 核对：8.4.1–8.4.2、8.5 构造引入、线性映射与交织公式 (3)。
- 结果：FAIL。①8.4.2 的群作用印刷为 `h(h₁,…,h_m)=(hh₁,…,hh_m)`；Markdown 在等式处多一个 `=`。②8.4.2 结尾并集条件印刷为 `λ⁻¹λᵢ∈W`，项为 `T_{λᵢ}N`；Markdown 缺 `∈` 且写成 `T_{λ i}N`。③公式 (3) 印刷为 `pT_λ^Ψ=T_λp`，Markdown 多出下标 bullet（`p_•`）。300 dpi 裁片确认，待逐处人工修复。
- 备注：页眉作者行和印刷页码 74 未收入 Markdown。
- 签署：2026-10-01 17:18 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.027（PDF p.27 / 印刷 p.75）

- PNG：`audit/Margulis_1974_arithmetic_properties_p027.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p027_8-5-2_1_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p027_8-5-2_2_300dpi.png`。
- 核对：8.5.2 延拓引理及其证明中的交集、基底和公式 (4)。
- 结果：FAIL。公式/变量存在多处实差异：①`T_{v^{-1}\lambda_i}` 被写成 `T_{v-1\lambda_i}`；②公式 (4) 的印刷 `\varphi_{\lambda_{i(k)}}` 被写成 `\varphi_{\mathbb M_{i(k)}}`；③印刷 `\alpha_\lambda` 被写成拉丁 `a_\lambda`；④目标 Markdown 在相应系数处写成 `c_h(v), f_h(v)`，印刷及周边求和索引均为 `k`，应为 `c_k(v), f_k(v)`（求和指标本身并未误作 `h`）；⑤公式末端印刷 `\omega_x(\lambda)`，Markdown 反转为 `\omega_\lambda(x)`；⑥“rational map on (V'')”附近插入了无源 `§` 并破坏数学分隔。300 dpi 裁片确认所列差异。
- 备注：页眉运行标题和印刷页码 75 未收入 Markdown。
- 签署：2026-10-01 17:21 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.028（PDF p.28 / 印刷 p.76）

- PNG：`audit/Margulis_1974_arithmetic_properties_p028.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p028_8-5-3_start_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p028_8-5-3_union_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p028_8-5-3_factor_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p028_8-6_definition_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p028_8-6-2_300dpi.png`。
- 核对：8.5.3 延拓证明后半、因子关系、8.6 定义与 8.6.1–8.6.2。
- 结果：FAIL。①8.5.3 中 zᵢ∈α_{λᵢ}(T_{λᵢ}M) 被写成拉丁 a_{λᵢ}；②λᵢ⁻¹ 被写为 −1/λᵢ；③⋃_{λ∈Λ}T_λM 被写成 ⋃_{λ∈λ}T_λM；④源文称 T 是延拓表示 T̄^Ψ 的因子，Markdown 只写“representation Ψ”；⑤8.6.2 证明在 T̄^Ψ 前插入无源竖线 |。300 dpi 裁片确认，待逐处修复。
- 未闭合/格式差异：8.6 相容条件中扫描字面紧连“λ∈Λ∩W M∩T_λN”，300 dpi 未看见可唯一辨认的分隔标点；Markdown 同样把条件连成一串，暂不猜补标点。8.6.1 中 P(Λ) 与 k-结构的相邻数学块少空隙，另作轻微格式问题记录。
- 备注：页眉运行标题和印刷页码 76 未收入 Markdown。
- 签署：2026-10-01 17:25 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.029（PDF p.29 / 印刷 p.77）

- PNG：`audit/Margulis_1974_arithmetic_properties_p029.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p029_9-1-1_proof_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p029_9-3-1_Ru_300dpi.png`。
- 核对：§9 标题、9.1.1 证明、9.2 引理与 9.3.1 开始。
- 结果：FAIL。①9.1.1 印刷链为 `V⊂C(F)⊂N(F)`，Markdown 重复了第二个 `⊂`。②证明末尾印刷为 `F⊂C(V)` 并使用“C(V) 不包含 G′”的关系符，Markdown 把它损坏为两个 `\nexists`。③9.3.1 中印刷 unipotent radical 记号为 `R_u(N)=R_u(S)`，Markdown 写成大写 `R_U`。300 dpi 裁片确认，待手工修复。
- 备注：页眉运行标题和印刷页码 77 未收入 Markdown。
- 签署：2026-10-01 17:50 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.030（PDF p.30 / 印刷 p.78）

- PNG：`audit/Margulis_1974_arithmetic_properties_p030.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p030_9-3-1_U_intersection_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p030_9-3-3_intersection_300dpi.png`。
- 核对：9.3.1 证明续段、9.3.2 引理及证明、9.3.3 引理及证明、9.3.4 引理与证明开头。
- 结果：FAIL。①9.3.1 证明续段中，印刷为 `U=\overline U_R∩Γ`，Markdown 多出 `\mathbb{I}`，成为 `U=\overline U_R∩\mathbb{I}Γ`。②9.3.3 引理陈述印刷为 `A_0∩Γ` 是 `A_0` 中 Zariski 稠密的算术子群；Markdown 写成 `A_0\cup Γ`。相应 300 dpi 裁片确认两处，待全篇审计完成后逐处手工修复。
- 备注：页眉作者行和印刷页码 78 未收入 Markdown；本页其余已核内容对应印刷页。
- 签署：2026-10-01 19:08 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.031（PDF p.31 / 印刷 p.79）

- PNG：`audit/Margulis_1974_arithmetic_properties_p031.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p031_9-4-1_proof_300dpi.png`。
- 核对：9.3.4 证明续段、9.4 定义、9.4.1 引理及证明、9.5.1 定理与证明开头。
- 结果：FAIL。9.4.1 证明第 2 项中，印刷在换行处为 `A_0∩A'_0∩∩Γ≠{e}`（连续两个交集符号，属原页字面 quirk）；Markdown 写成 `A_0∩A'_0∩Γ∩Γ≠{e}`，把印刷的双 `∩` 变成了重复的 `∩Γ`。待全篇审计完成后按印刷所示逐处手工修复。
- 源级 quirk：式 (1) 首个右端印作 `𝔄'∩Ad γ 𝔄'`，其后维数等式则印作 `𝔄∩Ad γ 𝔄'`；Markdown 保留两处各自的印刷写法，记录为页内记号异文，不据数学预期归一。9.4 定义中 `множество тех` 被粘为 `множествотех`，属轻微空格伪影。
- 备注：页眉运行标题和印刷页码 79 未收入 Markdown。
- 签署：2026-10-01 19:37 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.032（PDF p.32 / 印刷 p.80）

- PNG：`audit/Margulis_1974_arithmetic_properties_p032.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p032_9-5-1_continuation_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p032_9-6-2_defs_300dpi.png`。
- 核对：9.5.1 证明续段、§9.6 引入、9.6.1 引理、9.6.2 引理及证明至本页末。
- 结果：FAIL。①9.5.1 证明在“`𝔄∩Ad γ𝔄'` 是 Q-子空间”处，印刷仅有一个交集符号，Markdown 写成 `\mathfrak{A}∩∩Ad γ\mathfrak{A}'`。②9.6.2 证明的记号设定中，印刷为 `N'=N(\overline U')`，Markdown 写成 `N'=N(\overline U)`。③定义 `D'_Z` 和 `D''_Z` 时，印刷分别写作 `(Ad d)Δ=Δ` 与 `(Ad d)\overlineΔ=\overlineΔ`；Markdown 将作用记号与变量合并为普通文本 `\text{Add}`，未保留印刷中的算子/变量区分。三处均由 300 dpi 裁片确认，待全篇审计完成后逐处手工修复。
- 备注：页眉作者行和印刷页码 80 未收入 Markdown。
- 签署：2026-10-01 20:01 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.033（PDF p.33 / 印刷 p.81）

- PNG：`audit/Margulis_1974_arithmetic_properties_p033.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p033_9-6-3_intro_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p033_9-6-3_proof_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p033_9-6-4_9-7_300dpi.png`。
- 核对：9.6.2 证明收尾、9.6.3 引理及证明、9.6.4 引理及证明、9.7.1 定理陈述。
- 结果：FAIL。①9.6.3 引理陈述中，印刷首项为 `P_θ∩G_Z`，Markdown 给 `G_Z` 增加了 `^{\bar ε}`；印刷第二项为 `P_{\bar θ}^{-}∩G_Z`，Markdown 写成 `P_θ^{-}∩∩G_Z`，丢失 θ 上的横线并多出 `∩`。②9.6.3 证明中，印刷记号为 `\bar V_θ`（横线在 V 上）；Markdown 将横线移至下标，写作 `V_{\bar θ}`，并在后续相应交集/稠密关系处另添 `^{-}`。③9.6.4 证明由 3.3.3 和 3.3.1 得出的稠密关系，印刷为 `U'∩Γ` 在 `U'` 中稠密；Markdown 把目标群误作 `U''`。④9.7.1 第 3 项印刷为 `Δ={}_{Q}Δ(S,G)`，Markdown 在 Q 下标前多了负号；9.6.4 的 `rank_Q G` 记号也被 Markdown 数学分隔符拆成 `rank$_{Q}$$G`。所列差异均由 300 dpi 裁片确认，待全篇审计完成后逐处手工修复。
- 源级 quirk：9.6.2 证明收尾印刷将引文与后随式子连排为 `([7], 6.4(D_Z·\bar U_Z ...`；300 dpi 未见两者间的闭合标点，Markdown 保留该印刷连排。页末印刷行 `6 Успехи матем. наук, т. XXIX, вып. 1` 是刊物页脚，Markdown 将其排成 `##` 标题。
- 备注：页眉运行标题和印刷页码 81 未收入 Markdown。
- 签署：2026-10-01 20:26 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.034（PDF p.34 / 印刷 p.82）

- PNG：`audit/Margulis_1974_arithmetic_properties_p034.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p034_10-2-1_indices_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p034_10-3_end_300dpi.png`。
- 核对：§10 引入、10.1–10.2.1 引理与 10.2.1 证明、10.3 引理及证明续段至本页末。
- 结果：FAIL。①10.1 中印刷为 `Найдется такое n`，Markdown 误作 `Найдемся такое n`。②10.2.1 假设中印刷为 `дискретная подгруппа в G_R`；Markdown 把 `дискретная` 误成 `дискремная`，并将介词 `в` 损坏为 `B$$`。③10.2.1 的条件与证明均把撇号从印刷的 `U'_{nZ}` 移到整个下标之后，写成 `U_{nZ}'`。④10.3 证明中，Markdown 插入了原页没有的乱码短句 `Hence реконшти показатентство леммы...` 及孤立 `$<N(n)$`，并重复了后面的“Чтобы закончить доказательство леммы…”起句；印刷只有该证明文字一次，接续选择 `m=N(n)!`。300 dpi 裁片确认第③项符号位置及第④项页面内容，待全篇审计完成后逐处手工修复。
- 备注：页眉作者行和印刷页码 82 未收入 Markdown。
- 签署：2026-10-01 20:43 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.035（PDF p.35 / 印刷 p.83）

- PNG：`audit/Margulis_1974_arithmetic_properties_p035.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p035_10-3_unipotent_term_300dpi.png`。
- 核对：10.3 证明续段、10.4 主定理证明、§11 标题、11.1、11.2 及公式、11.2.1 引理与证明、11.3 和 11.3.1。
- 结果：PASS±。10.3 证明续段中，印刷为 `унипотентный элемент`，Markdown 将 `н` 误为 `п`，写成 `упипотентный элемент`；300 dpi 裁片确认词形，属于可恢复的轻微字词伪影。本页其余已核内容与记号对应。页眉运行标题、印刷页码 83 和页脚标记 `6*` 未收入 Markdown。
- 签署：2026-10-01 21:03 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.036（PDF p.36 / 印刷 p.84）

- PNG：`audit/Margulis_1974_arithmetic_properties_p036.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p036_11-3-4_11-3-6_300dpi.png`。
- 核对：11.3.2–11.3.7 引理及证明、11.4 引理与证明。
- 结果：FAIL。11.3.6 印刷结论为 `то M⊃U_{nZ}, где v_p(n)≤k`；Markdown 把 `то` 写成 `mo`，把 `где` 破坏为 `e \partial e`，致使引理结论句不可正确读取。300 dpi 裁片确认两处。
- 源级 quirk：11.3.4 证明先定义 `M_k` 为由 `kM` 生成的子群，随后第 1、2 项却写 `M_s`，第 3 项又写 `M_h`；Markdown 忠实保留这些印刷下标，不按推理预期统一。
- 备注：页眉作者行和印刷页码 84 未收入 Markdown。
- 签署：2026-10-01 21:34 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.037（PDF p.37 / 印刷 p.85）

- PNG：`audit/Margulis_1974_arithmetic_properties_p037.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p037_11-5-1_proof_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p037_12-heading_300dpi.png`。
- 核对：11.5–11.5.1 定理及证明、§12 标题、12.1.1 和 12.2.1 引理陈述。
- 结果：FAIL。①11.5.1 证明中印刷为 `индекс Λ в H_{mZ}`，Markdown 误写成 `индекс Λ в H_{nZ}`，与本引理的 `m` 参数不符。②12.2.1 末句印刷把 `U` 与 `G` 分开排作 `U G`，其间未见可辨认介词；Markdown 合并为 `$UG$`。应保留印刷空格，不补猜原页未显示的介词。另，11.5.1 证明有轻微字词伪影：印刷 `групп H'` 被写成 `групи H'`。
- 源级 quirk：11.5.1 陈述对指数写“не больше n”（不大于 n），其证明稍后写成“меньше n”（小于 n）；两处均按印刷记录，不在本任务中裁决证明。§12 标题印作 `G_z`（下标为小写 z），Markdown 保留该字形。
- 备注：页眉运行标题和印刷页码 85 未收入 Markdown。
- 签署：2026-10-01 22:24 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.038（PDF p.38 / 印刷 p.86）

- PNG：`audit/Margulis_1974_arithmetic_properties_p038.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p038_13-2_13-4_300dpi.png`。
- 核对：12.3 证明结尾、§13 引入、13.1、13.2.1–13.2.3 引理及证明、13.3.1 引理、13.4 引理与证明开头。
- 结果：FAIL。①13.2.1 第 2 项印刷为“由 `𝔘'∪𝔘''` 生成的 Lie 子代数等于 `𝔊`”；Markdown 将它误作第一项的群生成式 `U'∪U''=G`。②13.2.2 证明结论印刷为 `G_Z∩Γ` 在 `G` 中 Zariski 稠密；Markdown 多出 `G_Z` 上的撇号。③13.2.3 证明中，印刷说 `U_Z''∩Γ` 在 `U_Z''` 中有有限指数；Markdown 将该关系截成 `U_Z''∩Γ — в U''`，丢失“有限指数”并删去目标群的 `Z` 下标。④13.3.1 的第二个包含式印刷为 `Γ⊃((P_{\bar θ}^{-})_{rZ})^u`；Markdown 漏了抛物子群上的 `−`。300 dpi 裁片确认所列公式和关系，待全篇审计完成后逐处手工修复。
- 备注：页眉作者行和印刷页码 86 未收入 Markdown。
- 签署：2026-10-01 22:49 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.039（PDF p.39 / 印刷 p.87）

- PNG：`audit/Margulis_1974_arithmetic_properties_p039.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p039_13-5_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p039_13-6-1_proof_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p039_13-7_300dpi.png`。
- 核对：13.5–13.5.1、13.6–13.6.1、13.7 定义及 13.7.1 引理和证明到本页末。
- 结果：FAIL。①13.5 印刷为 `P''=P_{\bar θ}^{-}`；Markdown 将负号排在下标后作 `P_{\bar θ} -`，丢失了上标位置。②13.7 定义行印刷为俄文连词 `и` 后接 `ω(h)=𝔵(v_h,H_z)`，Markdown 写成 `\pi\omega(h)=...`，把连词变成了公式中的 `\pi`。③13.7/13.7.1 的定义域与证明多次以印刷的 `H_z·M` 表示；Markdown 在相关位置交替写成 `H_Z·M`、`H_Z^1·M`、`H_Z''·M`、`H_Z^\bullet M`，并增添数字/双撇号/项目符号、改变乘积点或下标字形。具体位置包括 D 的 ambient group、任意 h 的定义域、13.7.1 的函数定义域、证明中的 h 范围及式 (1) 上确界指标。300 dpi 裁片确认上述标点、上标和公式分隔差异，待全篇审计完成后逐处手工修复。
- 源级 quirk：13.6.1 证明先定义对偶空间 `L'_R`，下一句随即写 `M⊂L'` 而未带 `R` 下标；Markdown 按印刷保留该写法，不补猜下标。
- 备注：页眉运行标题和印刷页码 87 未收入 Markdown。
- 签署：2026-10-01 23:53 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.040（PDF p.40 / 印刷 p.88）

- PNG：`audit/Margulis_1974_arithmetic_properties_p040.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p040_13-7-1_end_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p040_13-8-1_proof_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p040_14-1_start_300dpi.png`。
- 核对：13.7.1 证明续段、13.8.1 引理及证明、§14 引入、14.1 与 14.1.1。
- 结果：FAIL。①13.7.1 收尾印刷为 `ψ(h)=𝔵(v_h,D)<k𝔵(v_h,H_z)=kω(h)`；Markdown 把两处 `𝔵` 误作 `\underline{\chi}`。②13.8.1 中，印刷先设 `γ_{U,p}=γ(g_U,p)`，再用 `f(γ_{U,p}·g_U)=u`、`q(γ_{U,p}·g_U)=s`；Markdown 把这些实参拆写成 `f(γ_U,p·g_U)` / `q(γ_U,p·g_U)`。同一段共轭式将 `γ_{U,p}^{-1}` 损坏为 `γ_U^1,p` 等碎片，末尾赋值估计也丢失 `y(γ_{U,p}·g_U)` 的闭括号。③14.1 中生成 `Ω_k` 的并集印刷为 `⋃_{θ≠Δ}(B_{\bar θ}^{-})_{kZ}`；Markdown 漏了 (B_{\bar θ}) 上的上标 `−`。上述记号差异由 300 dpi 裁片确认，待全篇审计完成后逐处手工修复。
- 源级 quirk：13.8.1 前文先对 `g∈G_Z·M` 说明 `γ(g,p)` 的存在，随后有一处印作 `для любого g∈G_Q`；Markdown 保留该原文范围写法，本记录不将其升级为证明正确性结论。
- 备注：页眉作者行和印刷页码 88 未收入 Markdown。
- 签署：2026-10-02 00:12 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.041（PDF p.41 / 印刷 p.89）
- 复核补记：14.1.2 证明中的下标应读作 `U_{t(k)Z}^{\prime\prime}`（不是 `U_{i(k)Z}^{\prime\prime}`），并有一处 `rank_Q G` 的 `$` 分隔符损坏；两项均已依同页 300 dpi 裁片修复。

- PNG：`audit/Margulis_1974_arithmetic_properties_p041.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p041_14-1_14-2-1_start_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p041_14-2-1_proof_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p041_14-3_300dpi.png`。
- 核对：14.1.2 证明、14.2 与 14.2.1 引理/证明及式 (1)–(3)、14.3 证明和式 (4)。
- 结果：FAIL。①14.1.2 中印刷的生成集使用 `B_{\bar θ}^{-}`，其生成群记为 `U''=V_{\varnothing}^{-}`；Markdown 漏掉根子群上的 `−`，并将 `V_{\varnothing}^{-}` 误作 `V_{\bar\varphi}'`，后续 `((B_{\bar θ}^{-})_{kZ})` 还被拆成 `$B_{\bar θ}$` 与乱码 `\$\_{kZ}\$`。②14.2.1 假设中印刷为 `p — простое` 和 `l — целое неотрицательное число`；Markdown 将两处俄语条件损坏为 `p - n rho c m o e`、`a$$l - y \epsilon l o e`，并把 `p^{2l}` 分拆成 `p^{2}l`。③证明的前提/式 (1) 左端及后续 s-包含式印刷使用 `B_{\bar θ}^{-}`，Markdown 对这些位置漏掉 `−` 或横线，并将范围 `θ⊂Δ` 写成 `θ⊂Λ`；式 (1) 右端按印刷本身为未加横线的 `B_θ`。④式 (3) 印刷的格子下标为 `p(ba)Z`，Markdown 写成小写 `p(ba)z`。⑤14.3 首个数组式中，印刷有 `m^2`，Markdown 拍平成 `m 2`，且单独插入一个 `\cdot` 行。300 dpi 裁片确认所列公式，待全篇审计完成后逐处手工修复。
- 源级 quirk：14.2.1 式 (1) 印刷首项为 `B_{\bar θ}^{-}`、右项为 `B_θ`（未加横线/负号）；Markdown 保留右项的这一源页异文，本记录不据前文推理归一。
- 备注：页眉运行标题和印刷页码 89 未收入 Markdown。
- 签署：2026-10-02 00:19 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.042（PDF p.42 / 印刷 p.90）

- PNG：`audit/Margulis_1974_arithmetic_properties_p042.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p042_15-1_15-2_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p042_15-3-1_proof_300dpi.png`。
- 核对：§15 引入、15.1–15.1.2、15.2–15.2.2 引理及证明、15.3.1 引理及证明开头。
- 结果：FAIL。①15.1 印刷为 `rank_Q G=1`，Markdown 将 Q 误作 `0`。②15.2 将 Lie 代数记号拍平：印刷分别使用 `\mathfrak{R}`、`\mathfrak{M}` 指代 N 的 Lie 代数和生成子代数，Markdown 多处写成普通 `R/M`；15.2.1 陈述同样把 `\mathfrak{G}_{\alpha}` 扁平为 `G_α`，并把俄语 `то` 损坏为 `mo`。其证明中 Lie 括号两侧还被嵌入了多余的 `$` 分隔符。③15.2.2 陈述将 `Если`、`то` 损坏为拉丁串 `Ecau`、`mo`。300 dpi 裁片确认这三处所在的印刷页内容，待全篇审计完成后逐处手工修复。
- 备注：页眉作者行和印刷页码 90 未收入 Markdown。
- 签署：2026-10-02 00:25 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.043（PDF p.43 / 印刷 p.91）

- PNG：`audit/Margulis_1974_arithmetic_properties_p043.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p043_15-3-1_equations_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p043_15-3-2_start_300dpi.png`。
- 核对：15.3.1 证明续段及式 (1)–(5)、15.3.2 引理及证明开头。
- 结果：FAIL。①15.3.1 证明定义 `𝔐` 时，印刷括号为 `[𝔑,𝔘']`；Markdown 将首个 Lie 代数拍平成普通 `N`。②交换子恒等式印刷末项为 `a_1^{-1}`，Markdown 写成 `a_i^{-1}`。③15.3.2 引理条件印刷为 `...⊃V(E) для любого g∈E·G_Z`；Markdown 在 `V(E)` 后插入无源乱码 `\partial_\lambda \lambda_0 \delta_{020}`。300 dpi 裁片确认所列差异。
- 备注：页眉运行标题和印刷页码 91 未收入 Markdown。
- 签署：2026-10-02 00:51 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.044（PDF p.44 / 印刷 p.92）

- PNG：`audit/Margulis_1974_arithmetic_properties_p044.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p044_15-3-2_proof_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p044_12-2-1_eq7_8_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p044_15-4_300dpi.png`。
- 核对：15.3.2 证明续段、12.2.1 弱不紧群证明及式 (7)–(8)、§15.4 引入和 15.4.1 陈述/证明开头。
- 结果：FAIL。①15.3.2 证明中，印刷一次指称子群 `((gP''g^{-1})_Z∩gΓg^{-1})`，Markdown 重复整项并插入等号。②12.2.1 证明多处印刷 `Q_p`，Markdown 误成 `Q_ρ`/`Q_P`；式 (8) 格子下标印刷为 `Z`，Markdown 插入额外 `\Sigma`，写成 `\Sigma_Z`。300 dpi 裁片确认上述公式差异。
- 源级 quirk：15.3.2 证明在 p.43 页尾和本页开头的接续中，印刷连续出现两个 `⊃`；Markdown 保留该跨页字面。该证明还印作 `P''_Z∩Γ=(P_{\varnothing})_Z∩Γ`，Markdown 如实转录，不按邻近符号归一。
- 备注：页眉作者行和印刷页码 92 未收入 Markdown。
- 签署：2026-10-02 01:00 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.045（PDF p.45 / 印刷 p.93）

- PNG：`audit/Margulis_1974_arithmetic_properties_p045.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p045_15-4_terminology_300dpi.png`。
- 核对：15.4.1 续段、15.4.2 引理及证明开头、15.4.3–15.5、§16 引入、16.1–16.2.1 陈述及证明开头。
- 结果：FAIL。①15.4.1 域限制段印刷为 `G=R_{k/Q}H`、`R_{k/k'}`；Markdown 将 `k` 误识成 `h`，两处写成 `R_{h/Q}H`、`R_{h/k'}`。②15.4.3 再次印作 `G=R_{k/Q}H`，Markdown 仍写 `R_{h/Q}H`。300 dpi 裁片确认 k/h 字形差异。
- 备注：页眉运行标题和印刷页码 93 未收入 Markdown；p.45 印刷 `и их описания` 与 Markdown 相同，按源文保留。
- 签署：2026-10-02 01:07 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.046（PDF p.46 / 印刷 p.94）

- PNG：`audit/Margulis_1974_arithmetic_properties_p046.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p046_16-2-rank_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p046_16-4_17-1_300dpi.png`。
- 核对：16.2.1 证明续段、16.3–16.4.3 引理及证明、§17 标题和 17.1 陈述至本页末。
- 结果：FAIL。16.2.1 证明中的两处 `rank_Q G=1` 被 Markdown 拆成 `rank$_{Q}$$G=1`，插入/错置 `$` 分隔符，破坏秩公式的数学排版；另有 `rank_Q S^0=0` 一处同样把分隔符拆坏。300 dpi 裁片确认印刷秩式分别为两处 `rank_Q G=1` 和一处 `rank_Q S^0=0`。
- 源级 quirk：17.1 的无不动点条件印作 `λ∈λ'`（小写 lambda）；Markdown 按印刷照录，不改成大写群符号。页末句在印刷页 94 以 `произ-` 断开，余下续于下一页，故本页仅核至该断页处。
- 备注：页眉作者行和印刷页码 94 未收入 Markdown。
- 签署：2026-10-02 01:12 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.047（PDF p.47 / 印刷 p.95）

- PNG：`audit/Margulis_1974_arithmetic_properties_p047.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p047_17-3_projection_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p047_appendix_300dpi.png`。
- 核对：17.1 续段、17.2–17.4、附录标题及引理 4.5.1 证明开头至页末。
- 结果：FAIL。①附录证明中，印刷为 `x∈(𝔊_α)_k`，Markdown 下标误写成 `h`。②同段定义 \(\alpha(s)\) 的全称范围印刷为 `s∈𝔖`，Markdown 写成 `s∈𝔊`。③式 (1) 印刷为 `[\mathfrak{C}_0,x]\not\ni x`，Markdown 把关系损坏为 `\nexists x`。三处数学差异由 300 dpi 裁片确认。另，17.3 中投影符号 `\varphi` 的两个行文位置被录作西里尔字母 `ф`，属于轻微字符伪影。
- 备注：页眉运行标题和印刷页码 95 未收入 Markdown；17.1 段落在源页末以断词 `произ-` 续接下一页。
- 签署：2026-10-02 01:26 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.048（PDF p.48 / 印刷 p.96）
- 复核更正：本页初核对差异的计数有误：印刷只有一处 `\mathfrak{G}_{-\alpha}` 根空间下标；另一处将 Latin `a` 误作根字母的位置是标量表达式 `(-\alpha-\beta)(h)`。修复登记按这两个不同表达式记录。
- 300 dpi 补充证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p048_appendix_end_300dpi.png`，核对根空间/标量根表达式和括号。

- PNG：`audit/Margulis_1974_arithmetic_properties_p048.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p048_appendix_4-5-1_300dpi.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_p048_references_300dpi.png`。
- 核对：附录引理 4.5.1 证明续段及参考文献 [1]–[10]。
- 结果：FAIL。①4.5.1 证明中印刷两处为 `\mathfrak{G}_{-\alpha}`，Markdown 均误作 `\mathfrak{G}_{-a}`（希腊字母 α 被 Latin `a` 代替）。②同一证明结论处，印刷为 `[\mathfrak{G}_\alpha,\mathfrak{G}_\beta]=\mathfrak{G}_{\alpha+\beta}`；Markdown 首次写成 `[\mathfrak{G}_\alpha,\mathfrak{G}_\beta=...`，遗漏右方括号。③参考文献 [8] 标题印刷 `унипотентных`，Markdown 写成 `унипотеятных`。300 dpi 裁片确认相关数学符号与文献字词。
- 源级 quirk：参考文献 [2] 印作 `Homogenous spaces`；Markdown 忠实保留该拼写，不改成别的词形。
- 备注：页眉作者行和印刷页码 96 未收入 Markdown。
- 签署：2026-10-02 01:33 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.049（PDF p.49 / 印刷 p.97）

- PNG：`audit/Margulis_1974_arithmetic_properties_p049.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p049_footer_300dpi.png`。
- 核对：参考文献 [11]–[36] 与页脚刊名行。
- 结果：PASS±。参考文献 [11]–[36] 已对照印刷页核验。页脚印作 `Успехи матем. наук, т. XXIX, вып. 1`；Markdown 写成 `Усехи матем. наук. т. XXIX, вып. 1`，少了 `п` 并把逗号误成句点；300 dpi 裁片确认。该差异限于页脚行。
- 备注：页眉运行标题和印刷页码 97 未收入 Markdown。
- 签署：2026-10-02 01:39 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## p.050（PDF p.50 / 印刷 p.98）

- PNG：`audit/Margulis_1974_arithmetic_properties_p050.png`（pngmono，150 dpi）。
- 300 dpi 证据：`audit/300dpi/Margulis_1974_arithmetic_properties_p050_refs_300dpi.png`。
- 核对：参考文献 [37]–[49] 与收稿日期行。
- 结果：FAIL。印刷页包含完整参考文献 [37]–[49] 共 13 条，以及 `Поступило в редакцию 16 июля 1973 г.`；MinerU Markdown 全文在参考文献 [36] 和 p.49 页脚后结束，没有这 13 条及收稿日期。对完整 Markdown 搜索 bibliography anchor `^[37]`–`^[49]` 与 `Поступило в редакцию` 均无匹配。
- 源级 quirk：参考文献 [49] 的刊名在印刷中显示为 `Enventicnes Math.`；按页图保留该字面拼写，不用题录常识替换。
- 备注：页眉作者行和印刷页码 98 未收入 Markdown。
- 签署：2026-10-02 01:47 EDT；actor=Peer-P18；model=gpt-6-luna；effort=max。

## MinerU Markdown 修复登记（Peer 候选，未集成）

- 原始 Markdown：`a33f22f3b0bcf430149ea06d98e65076266acc9e`；审计前 SHA-256：`7fa7ee59a1c4b3c4fa88254a1ab9aa3d51f3f1b28560e7ccb4e26da2ce8aeec7`。
- 修复提交：`5a07040e1302967c763dbde61a87d5d77e9c96c1`；目标 Markdown 修复后 SHA-256：`9afd65e79be33a9ec3faf483d61c3bfa3b7271009e80ddcd86b153e4d0ac259f`。
- 以下 PDF 页号对应上方同页审计项中的全页 PNG 与列明的 300 dpi 原页裁片；每项均由印刷页图支持。修复按项目要求使用当前 Host 的 Edit 工具逐处人工修改，未用脚本写入 MinerU Markdown。
- 50 页已逐页核对。原始差异中 41 个 FAIL 页已修复；9 个 PASS± 页保留了记录所述轻微 OCR 伪影、印刷 quirk 或非正文省略，没有把它们升级为内容修复。完成修复后已从头复读整份 Markdown，并逐项核对本次改动、页图依据和残余差异；未发现未落实的 FAIL 项或新增转录差异。

### 审计记录的复核修订

- p.015：曾把引理 4.5.5 陈述中 `F` 在 `V` 内正规误报为差异。300 dpi 页图复核确认印刷为“F 是 V 的法向子群，由 V∩V′ 生成”，原 Markdown 的该句与印刷一致；已从差异项撤回。p.015 其余实际差异仍按本页记录修复。
- p.027：原审计把求和指标 `k` 误称为 `h`。PDF p.27 的求和式和公式 (4) 均印作 `k`；实际需要改正的是目标 Markdown 中 `c_h(v), f_h(v)`，已改为 `c_k(v), f_k(v)`。
- p.041：补记 14.1.2 证明的 `U_{t(k)Z}^{\prime\prime}` 下标（原 Markdown 写成 `U_{i(k)Z}^{\prime\prime}`）及一处 `rank_Q G` 分隔符损坏，两处均已修复。
- p.046：补记并修复第三处秩式损坏 `rank_Q S^0=0`；本页实际修复两处 `rank_Q G=1` 和一处 `rank_Q S^0=0`。
- p.048：修订原审计中“有两处 `\mathfrak{G}_{-\alpha}`”的错误计数。实际上只有一处根空间下标 `\mathfrak{G}_{-\alpha}`，另一处是标量根表达式 `(-\alpha-\beta)(h)`；两处 Latin `a` 误识均已修复。新增裁片 `audit/300dpi/Margulis_1974_arithmetic_properties_p048_appendix_end_300dpi.png` 直接支持这两处和缺失括号的核对。

### 按 PDF 页码登记的正文修复

- p.001：补齐目录遗漏的 §16、§17、附录和参考文献四项。
- p.002：恢复行间公式中的 `где g=...`。
- p.004：修正 `связная` 和脚注中的 `группой движений`。
- p.006：恢复 `H_{nZ}` 与 `H_Z` 的大写 Z 下标。
- p.007：修复 `𝔄`、`𝔖` 和 `𝔖_K` 的 Lie 代数记号。
- p.008：修正 `нильпотентным` 与 `предположения`。
- p.011：把映射名 `expr` 修为 `exp`。
- p.012：恢复希腊大写 `Λ`，并把映射名改为 `exp`。
- p.014：恢复式 (1) 的负根和空集下标、式 (3)/(4) 标签、引理 4.5.1 的 α/k/括号式，以及 4.5.4 的 `V_∅⁻`。
- p.015：修正 Weyl 群的 k 下标、4.5.5 证明中的正规子群和 `P_∅/N(V_∅)` 下标、4.5.6/4.5.8 记号及 `подгруппе`；4.5.5 陈述中与印刷相同的 `F` 项保持不改。
- p.016：修复 `exp ξ` 和 `V_∅`。
- p.017：恢复 `𝔊` 记号。
- p.018：移除无源的 `N_R^*` 星号及多出的交集符号。
- p.021：恢复 `\overline{U'}_R`、公式分隔和 `R_u`。
- p.022：移除 OCR 总量标记，并恢复 `N'=N(\bar U')`。
- p.023：修复 `exp \widetilde W` 及 `V=\bar V∩Γ`。
- p.024：恢复 `V_∅⁻` 和完整维数公式分隔符。
- p.025：重建 8.1.1；修正 8.1.2 映射、8.1.3 文字、`T_{w^{-1}}`、8.3 的 α/公式标签，并移除重复 8.4 标题。
- p.026：修正作用等式、并集成员关系与 `T_{λ_i}`，移除公式 (3) 中的无源项目符号。
- p.027：修复 `T_{v^{-1}λ_i}`、`φ_{λ_{i(k)}}`、`α_λ`、`ω_x(λ)`、系数下标 `c_k(v), f_k(v)`、无源 §，并恢复 `V'` 的并集构造。
- p.028：恢复根 α 与 `λ_i^{-1}`，修正对 Λ 的并集、`\bar T^Ψ` 因子和无源竖线。
- p.029：修复包含链、`C(V)\not\supset G'` 和 `R_u`。
- p.030：恢复 `U=\bar U_R∩Γ` 及 `A_0∩Γ`。
- p.031：按原页保留并恢复印刷中的双交记号 `∩∩Γ`。
- p.032：移除多余交集，修复 `N'=N(\bar U')` 和 `(Ad d)Δ`。
- p.033：恢复 `P_{\bar θ}^-`、`\bar V_θ`、`U'`，并修复秩分隔符与 Δ 的 Q 下标。
- p.034：修正 `Найдется`、`дискретная в G_R`、`U'` 下标；移除无源英文 OCR、重复句和孤立公式片段。
- p.036：恢复 11.3.6 结论中的俄文 `то` 与 `где`。
- p.037：修正 `H_{mZ}` 下标，并按印刷保留 `$U$ $G$` 之间的空格。
- p.038：恢复 Lie 子代数 `𝔘'∪𝔘''=𝔊`、删除 `G_Z` 上的无源 prime、补齐有限指数/open 关系，并给 `P_{\bar θ}^-` 加回负号。
- p.039：修正 `P''=P_{\bar θ}^-`。
- p.040：恢复 `𝔵`、`H_z` 下标/定义域、`γ_{U,p}` 及其证明记号，并给 14.1 生成集补回负根。
- p.041：修复负根生成集、`V_∅^-`、14.2.1 条件与 `p^{2l}`、式 (1) 的保留异文、`p(ba)Z`、14.3 的 `m²`；另修正 `U_{t(k)Z}^{\prime\prime}` 和损坏的 `rank_Q G`。
- p.042：恢复 `rank_Q G=1`、`\mathfrak{R}`/`\mathfrak{M}`/`\mathfrak{G}_α` 的 Lie 代数字体、俄语 `Если/то` 和括号公式。
- p.043：恢复 Lie 括号中的 `𝔑`、`a_1^{-1}`，并删除无源乱码。
- p.044：移除重复子群项，修复 `Q_p` 并去掉格子下标中多出的 `Σ`。
- p.045：将限制标量的域 `h` 修正为 `k`。
- p.046：修复两处 `rank_Q G=1` 与一处 `rank_Q S^0=0`。
- p.047：修正 `(𝔊_α)_k`、`s∈𝔖` 和 `\not\ni` 关系。
- p.048：修复一处 `𝔊_{-α}`、标量根 `(-α-β)(h)`、缺失右括号及参考文献 [8] 的 `унипотентных`。
- p.050：补录参考文献 [37]–[49] 和收稿日期；按原印刷保留 [49] 的 `Enventicnes Math.`。

- 复读结论限于转录忠实性与页面覆盖；未据此评判论文的数学证明有效性。
