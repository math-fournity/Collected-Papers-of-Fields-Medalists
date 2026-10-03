<!-- actor=Wf-R-P09; host=zcode; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN） -->
# Serre_1956_gaga 审计重做（Luna 审计不可信 → 全量逐页重检）

## 文件头

- 性质：**Luna 审计重做**。用户 2026-10-02 判定此前 GPT-6 Luna（Peer-P09）对该篇的审计不可信，本 redo 按 AUDIT-SOP 逐页对照 PDF 原页全量重检；Luna 的旧修复（commit `c270a3c2c` 等）一并作为被检对象重核。
- 裁决源：印刷原文 PDF（`1954年 - Serre/Serre_1956_gaga.pdf`）。Luna 旧 AUDIT/旧修复、pdftotext 文本层均只作线索或辅助通道，不作裁决。
- actor=Wf-R-P09；host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）。
- PDF：`1954年 - Serre/Serre_1956_gaga.pdf`，SHA-256 `9898f985dd6932496e26450bfe0beca8655a937032f545b97cebd88d1bc8eb98`，43 页（pdfinfo：Pages: 43）。PDF p.1 为 Numdam 封面（无印刷页码），PDF p.2–43 = 印刷 p.1–42。
- 被检 Markdown 基线：`1954年 - Serre/Serre_1956_gaga_mineru/Serre_1956_gaga__Serre_1956_gaga.md`，重做开始时 SHA-256 `f4ebe12f7a27be038319d2eb23db2f236b6dad7add13c26b9ed8d6224ed19408`（1119 行；该基线已含 Luna 旧修复）。
- 证据图：`1954年 - Serre/audit-redo/`（pngmono 150dpi，本 redo 专用；旧 `audit/` 不动）。
- 文本层判定（2026-10-03）：`pdftotext -f 1 -l 1` 首页返回完整封面文本（Numdam 题录、版权、数字化声明，exit 0）→ **文本层可用，采用双通道主对账**（每页 PNG 视觉检视为主、pdftotext 页文本为辅，二者不一致时以 PNG/原页为准）。
- 日期时间：2026-10-03 12:02 EDT 起。
- print quirk 与印刷错字忠实登记，绝不按数学预期静默改正；看不清的以 300dpi 裁剪仲裁或如实标注，绝不编造。

## 页级记录（重做）

## p.001（PDF p.1 / 印刷封面，无页码）
- PNG：audit-redo/p001.png（pngmono 150dpi）
- 核对：题录（作者/标题/卷期页码/Numdam URL）、版权与使用条款、Numdam 数字化声明、报头。
- 结果：PASS±。MD 行 1–13 与原页逐项吻合（JEAN-PIERRE SERRE / Géométrie algébrique et géométrie analytique / tome 6 (1956), p. 1-42 / item?id=AIF_1956__6__1_0 / © …tous droits réservés / L'accès aux archives… / NUMDAM / 数字化声明三行）。差异：原页顶部灰色网点带上的字距报头「ANNALES DE L'INSTITUT FOURIER」在 MD 无对应行——期刊名已在题录与版权文字中出现，属呈现省略不误导（Luna 旧判同此，重检维持）。Luna 对本页无 md 修复。
- 备注：本页为 born-digital Numdam 封面，pdftotext 辅助通道与 PNG 一致。

## p.002（PDF p.2 / 印刷 p.1）
- PNG：audit-redo/p002.png（pngmono 150dpi）；标题带仲裁裁剪 audit-redo/300dpi/p002_title_300dpi.png（300dpi）
- 核对：文章标题与作者行、Introduction 前三段（至「de façon précise, nous」页末断句）、Chow 定理句。
- 结果：PASS±。标题「GÉOMÉTRIE ALGÉBRIQUE ET GÉOMÉTRIE ANALYTIQUE / par Jean-Pierre SERRE.」与 MD 行 15/17 吻合——150dpi 下首词重音方向存疑，300dpi 仲裁确认为尖音 É（三处一致），MD 无误。正文两段逐词吻合（含 « de première espèce »、kählériennes、non singulière 等）。差异（均不误导）：①印刷以小型大写排「CHOW」，MD 行 23 作「Chow」（Luna 旧修复把 mineru 误识「CNow」改为「Chow」，修复本身正确；大小写规范化连同本页同型：OKA/CARTAN 在 MD 他行保留大写，此处不一致，登记不改）；②印刷斜体（algébrique/analytique/faisceaux cohérents）在 MD 未标——mineru 已知拍平；③印刷「singulière) ; 」分号前细空格被拍平为「singulière);」。
- 备注：Luna 旧判本页 FAIL（CNow）→ 已修复，重检确认修复与原页相符。

## p.003（PDF p.3 / 印刷 p.2）
- PNG：audit-redo/p003.png（pngmono 150dpi）
- 核对：Introduction 续三段（对应双范畴句、§1–§4 内容综述、𝒪_x/ℋ_x 局部环句、「couple plat」句）、脚注(1)全文。
- 结果：PASS±。MD 行 27–35 与原页逐段吻合：fibrés 重音、« couple plat »、l'Annexe déf. 4、théorèmes A et B de [3] exp. XVIII-XIX、脚注(1)（…renvoyons à [3], exp. XX.）均一致；印刷花体 𝒪_x、ℋ_x 与 MD $\mathcal{O}_x$/$\mathcal{H}_x$ 对应（150dpi 可辨，Luna 300dpi 旧裁剪同证）。差异（登记不改）：印刷小型大写「BETTI」「CHOW」在 MD 作「Betti」「Chow」（与 p.002 同类大小写规范化）；印刷斜体（normales、espaces fibrés 等）未标。
- 备注：Luna 旧判本页 PASS±，重检维持；本页 Luna 无 md 修复。

## p.004（PDF p.4 / 印刷 p.3）
- PNG：audit-redo/p004.png（pngmono 150dpi）
- 核对：Introduction 末段、§ 1 节标题、n° 1 标题、解析子集定义段（n ⩾ 0、f₁,…,f_k、U ∩ W）、𝒞(X)/ℋ/𝒞(Cⁿ) 记号、限制同态显示式 ε_x、𝒜_x(U) 核与商环句、holomorphe 定义段（C^r/C^s、ℋ_{φ(x),V}）。
- 结果：PASS±。MD 行 37–55 与原页逐项吻合：$\geqslant$ 与印刷斜等号 ⩾ 一致（pdftotext 拍平为「^ 0」，以 PNG 为准）；显示式 ε_x : 𝒞(Cⁿ)_x → 𝒞(U)_x 下标、上标 n 与箭头均正确；𝒜_x(U)、ℋ_{x,U}、f∈ℋ_{φ(x),V} ⟹ f∘φ∈ℋ_{x,U} 全部一致。差异（登记不改）：①印刷显示式末尾句点「(U)_x.」在 MD 显示式未保留；②印刷斜体（analytique、faisceau des germes de fonctions holomorphes sur U、application holomorphe）未标；③印刷正体 U/V/W 与 MD 数学模式 \mathrm{U} 等混排（可辨识）。
- 备注：Luna 旧判本页 PASS±，重检维持；本页 Luna 无 md 修复。

## p.005（PDF p.5 / 印刷 p.4）
- PNG：audit-redo/p005.png（pngmono 150dpi）；仲裁裁剪 audit-redo/300dpi/p005_def1-axioms_300dpi.png（300dpi，公理标号与 ℋ 下标）
- 核对：同构判据句（ℋ_U→ℋ_V）、积空间段与显示式 φ×φ′、n° 2 标题、DÉFINITION 1、公理 (H_I)/(H_II)、morphismes 段（ℋ_{φ(x),Y}、ℋ_{x,X}）。
- 结果：FAIL（两处下标内容错误，已当场修复，见下）。①Déf.1 与 morphismes 段中印刷为 $\mathcal{H}_{X}$（大写斜体 X，指空间；300dpi 确认），MD 两处（行 71、77）作小写 $\mathcal{H}_{\mathrm{x}}$ → 已改 $\mathcal{H}_{\mathrm{X}}$；②公理标号印刷为罗马数字 (H_I)/(H_II)（300dpi：下标为带衬线罗马 I，与同段「n° 1.」的阿拉伯 1 字形明显不同），MD 行 73 作 $(\mathrm{H}_{1})$ → 已改 $(\mathrm{H}_{\mathrm{I}})$。其余各项吻合：Luna 旧修复「$\mathcal{H}_{U}$ en le faisceau $\mathcal{H}_{V}$」与原页相符（旧 mineru 为 $\mathcal{H}_{\backslash}$，已正确修为 V）；显示式 φ×φ′: U×U′→V×V′ 及 C^{r+r'} 等一致。print quirk 忠实保留：印刷原文即作「sera dite holomorphe **si elle continue**」（无 est，印刷脱漏），MD 行 77 原样保留，不按语法预期补词。差异（登记不改）：印刷显示式末尾句点未保留；印刷斜体（isomorphisme analytique、espace affine 等）未标。
- 修复登记：本页 3 处 md 修复（行 71 x→X、行 73 1→I、行 77 x→X），依据 audit-redo/300dpi/p005_def1-axioms_300dpi.png，随 p.005 页级 commit 提交；修复前 md 基线见 SHA f4ebe12f（重做起点）。
- 备注：Luna 旧判本页 FAIL（仅 ℋ_{\backslash}→ℋ_V 一项）→ 该修复正确；但 Luna 未发现上述 x/X 与 1/I 两处下标错误，本次重检补修。

## p.006（PDF p.6 / 印刷 p.5）
- PNG：audit-redo/p006.png（pngmono 150dpi）；仲裁裁剪 audit-redo/300dpi/p006_axiome-ref_300dpi.png（公理引用下标）、audit-redo/300dpi/p006_AxY_300dpi.png（𝒜_x(Y)/ℋ_{x,X} 行）
- 核对：carte 定义段、(H_?) 交叉引用、Y analytique 段、积空间段（φ×φ′: V×V′→U×U′）、[18] nos 34-35 句、n° 3 标题、faisceau analytique 定义（ℋ_X-modules）、𝒜_x(Y)/𝒜(Y)/商束 ℋ_X/𝒜(Y) 段、PROPOSITION 1 a) b)。
- 结果：PASS±。全部条目与原页吻合：Luna 旧修复「$f \in H_{x,X}$」（行 87，旧 mineru 作 H_{x,Y}）经 300dpi 复核与印刷一致；Prop.1 陈述、ℋ_X/𝒜(Y)、ℋ_Y、[18] n° 15/12/5/6、nos 34-35 均正确。**print quirk 忠实登记**：印刷原文交叉引用即作「L'axiome (H_II) signifie qu'il est possible de recouvrir X par des ouverts possédant des cartes」——300dpi 确认下标为罗马 II（两个衬线 I），语义上此处应指覆盖公理 (H_I)，属印刷原文自身引用 quirk；MD 行 79 作 (H$_{II}$) 忠实保留，不按数学预期改正。差异（登记不改）：①行 87/89 段内 MD 的 $H_{x,X}$、$H_{X}$、$H_{Y}$ 用正体 H 而同段 $\mathcal{H}_X/\mathcal{A}(Y)$ 用花体——印刷一律花体 ℋ，属 mineru 花体拍平/混排，全文性伪影，不妨碍辨识，按 SOP 不批量改；②印刷斜体（carte、induite、produit 等）未标。
- 备注：Luna 旧判本页 FAIL（H_{x,Y}）→ 修复正确；Luna 未登记 (H_II) 交叉引用 quirk，本次补登。

## p.007（PDF p.7 / 印刷 p.6）
- PNG：audit-redo/p007.png（pngmono 150dpi）；仲裁裁剪 audit-redo/300dpi/p007_series_300dpi.png（两处 C{z₁,…,z_n}）
- 核对：Prop.1 证明段（ℋ_X=ℋ_U/𝒜(X)、[18] n° 16）、相干解析束例段、n° 4 标题、局部环 ℋ_x/𝔪 段、C{z₁,…,z_n} 两处、正则局部判据段（点 simple、variété analytique）、最小素理想显示式 0=∩𝔭_i。
- 结果：PASS±。MD 行 93–107 与原页逐项吻合。Luna 旧修复复核：行 99 两处 $C\{z_{1}, \ldots, z_{n}\}$（旧 mineru 作 z_i）经 300dpi 裁剪确认与印刷一致（首下标为阿拉伯 1，末下标斜体 n）；显示式 $0 = \cap \mathfrak{p}_{i}$（含尾逗号）与印刷一致；ℋ_x=ℋ_U/𝒜(X)、[3] ths. 1 et 2、[15] chap. iv § 2、[16] 等引用均正确。差异（登记不改）：①行 99 的 $H_{x}$、$H_{x}/m$ 及 $X=C^{n}$、$C^{n}$、$C\{z\}$ 用正体 H/双线体 C，印刷为花体 ℋ、粗体 C——全文性花体/粗体拍平类伪影（同类已见于 p.006），不妨碍辨识；②行 99 商理想 "/a" 印刷为花体 𝔞，MD 作正体 a——fraktur 拍平，登记不改；③印刷斜体（algèbre locale、anneau noethérien、anneau analytique、régulier、simple、variété）未标。
- 备注：Luna 旧判本页 FAIL（z_i 两处）→ 修复正确，重检维持 PASS±；本页无新增修复。

## p.008（PDF p.8 / 印刷 p.7）
- PNG：audit-redo/p008.png（pngmono 150dpi）；仲裁裁剪 audit-redo/300dpi/p008_series-zr_300dpi.png（C{z₁,…,z_r} 三处）
- 核对：不可约分量段（𝔭_i=𝒜_x(X_i)、ℋ_x/𝔭_i=ℋ_{x,X_i}）、Krull 维数比对段（[14] § 4、[3] exp. VIII、[16] p. 18）、§ 2 节标题、Z-拓扑约定段、n° 5 标题、LEMME 1 a)–d)。
- 结果：PASS±（含 1 处结构修复）。Luna 旧修复复核：行 109 三处 $\mathbb{C}\{z_{1},\dots,z_r\}$/$\mathbb{C}[[z_{1},\dots,z_r]]$（旧 mineru 作 z_i）经 300dpi 裁剪确认与印刷一致（首下标 1、末下标 r）；𝔭_i=𝒜_x(X_i)、anneau d'intégrité、[15]/[16] 引用一致；LEMME 1 四项陈述（Z-topologie moins fine、Z-localement fermé、application régulière ⟹ holomorphe、isomorphisme birégulier ⟹ isomorphisme analytique）与印刷逐词吻合。**结构修复**：行 115「5. Définition de l'espace analytique associé à une variété algébrique.」印刷为与 n° 1–4 同式的粗体节标题，MD 原为普通段落 → 已升为「## 5. …」（mineru 结构性漏标；n° 6/7/20 疑似同类，留待对应页核处）。差异（登记不改）：①行 109 的 $\mathcal{H}_{x,\mathrm{X}_i}$ 用正体 X，印刷为斜体 X_i；②C 的 \mathbb/\mathbf 混排与花体 ℋ 拍平（全文性伪影）；③印刷斜体（dimension、coïncide、Z-topologie 等词条内斜体）未标。
- 修复登记：本页 1 处 md 结构修复（行 115 升 ## 标题），随 p.008 页级 commit 提交。
- 备注：Luna 旧判本页 FAIL（z_i）→ 修复正确；Luna 未发现 n° 5 标题漏标，本次补修。

## p.009（PDF p.9 / 印刷 p.8）
- PNG：audit-redo/p009.png（pngmono 150dpi）；仲裁裁剪 audit-redo/300dpi/p009_Vprime-colon_300dpi.png（V′ 后冒号行）、audit-redo/300dpi/p009_axiomes-VA_300dpi.png（(H_I)/(H_II)/(VA′_II) 公理标号）
- 核对：LEMME 1 证明段（a/b/c/d 引用、f⁻¹）、X 上解析结构设置段、carte 显示式 φ : V → U（含尾逗号）、PROPOSITION 2 全陈述、「Plus brièvement」句、唯一性/存在性段（φ⁻¹ 运输、V ∩ V′、recollement、ℋ_X、(H_I)、(VA′_II)、T_ij、U_i × U_j、a fortiori、séparé）、Remarque 首句。
- 结果：PASS±。MD 行 127–143 与原页逐项吻合；无 md 修复。**print quirk 忠实保留（Luna 旧登记复核维持）**：印刷原文即作「Si $\varphi': V': \to U'$」——V′ 与箭头之间多一个冒号（300dpi 确认），MD 行 141 原样保留不改正。公理标号印刷为 (H_I)/(H_II)（罗马数字，300dpi 确认，与 p.005 修复一致），MD 行 141 ($H_I$)/($H_{II}$) 相符；($VA_{II}'$) 与印刷 VA′_II（A 右上撇、II 下标）对应无误；显示式 φ : V → U , 的尾逗号与 \quad 间距均保留。差异（登记不改）：印刷斜体（Prop.2 陈述整段斜体、a fortiori、Remarque）未标。
- 备注：Luna 旧判本页 PASS±（登记 V′ 冒号 quirk）→ 重检维持；本页 Luna 无 md 修复。








