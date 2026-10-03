# AUDIT-serre1987 — Sur les représentations modulaires de degré 2 de Gal(Q̄/Q)

状态：Wf-P43 分块候选审计（本 worker 负责 p.001-009）；页级发现即时以结构化 Edit 修复并随当页 commit；仍待 Master 按精确 commit 集成复核。

- actor=Wf-P43; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置；实际 effort 自报 UNKNOWN）。
- 开工时间：2026-10-02 13:34 EDT。
- 基线 commit：`8aa00fdde6167c8f6785c00c4feaed84518ad692`（分支 `cpf/serre1987`）；写入范围仅限 `1998年 - Wiles/` 下本篇 Markdown、本 AUDIT 文件与 `audit/serre1987_*` 证据图片。
- PDF：`serre1987.pdf`，52 页（Duke Math. J. 54 (1987)，印刷 p.179-230）；原件 SHA-256：`8048919db24dcb972435aaaa2a74d1168d0fe533af3aa26c6c809b12ddaee038`。
- 待审 MinerU Markdown：`serre1987_mineru/serre1987__serre1987.md`；审计前 SHA-256：`8671749d84b93434d89c346542964c0226ea21073423e1921b0410c95f5e4e61`。
- MinerU 导出：`middle_json.json` 与 `structured_content.json` 均登记 52 页；producer 为 MinerU 3.4.4（tier=basic, parse_mode=ocr）；导出中无 `doc_id` / `document_id` 字段。
- 文本层通道判定（2026-10-02，`pdftotext -f 1 -l 1 serre1987.pdf` 输出正常）：文本层可用 → 全程「文本层主对账 + PNG 视觉核验」双通道；文本层含扫描字符映射噪声（如 `p` 代 ρ、`e` 代 ε、`Fermai` 代 Fermat、`©` 印作 `0`），符号真值一律以 PNG 视觉（疑难字形 300 dpi 裁片）为准。
- 页码映射：PDF p.N = 印刷 p.(178+N)。

## p.001（PDF p.1 / 印刷 p.179）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 13:34 EDT。
- PNG：`audit/serre1987_p001.png`（pngmono，150 dpi）。
- 核对：题录（标题/作者/献词）、期刊页眉、摘要全部九段（含 ρ: G_Q → GL₂(F̄ₚ)、n° 1.2/1.3、n°s 2.2-2.4）、致谢 Tate/Fontaine 两段、页脚收稿日期。
- 结果：FAIL。印刷页脚收稿日期 “Received December 5, 1986.” 在 Markdown 全文缺失（grep 无命中）；已依本页原图在题录区（献词行后）补入。其余文字、公式与记号逐句吻合。
- 备注：期刊页眉 “Vol. 54, No. 1 / DUKE MATHEMATICAL JOURNAL © / 1987” 与页码 179 未收入 Markdown——排版级差异，常规不收，不改。摘要中印刷斜体强调词（conjecture、conducteur d'Artin、poids）在 Markdown 为正体纯文本，排版级，不误导。

## p.002（PDF p.2 / 印刷 p.180）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p002.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p002_toc_section5.png`、`audit/300dpi/serre1987_p002_epsilon_target.png`、`audit/300dpi/serre1987_p002_extension_Qbar.png`（pnggray）。
- 核对：致谢续（Frey/Mestre 段）、目录六行（§1-§5+Bibliographie 页码 180/182/192/199/217/228）、§1 标题、1.1 Notations 全段（ρ: G_Q → GL(V)、GL₂(F_q)、ε: (Z/NZ)* → F̄ₚ*）、1.2 Définition de N 开头（G₀ ⊃ G₁ ⊃ ⋯ ⊃ Gᵢ ⊃ ⋯）、脚注 1。
- 结果：FAIL。印刷 “Choisissons une extension à **Q̄** de la valuation l-adique de Q”（300 dpi 裁片确认首 Q 带 bar）在 Markdown 丢 bar 写成 “à Q”，数学对象改变；已依裁片修复为 $\overline{\mathbf{Q}}$。其余文字与公式吻合。
- 印刷原文 quirk：目录 §5 行印刷作 “Exemp**i**es”（300 dpi 裁片确认 i 无上升部带点，非 l；Duke 排字错误），Markdown 亦作 “Exempies”，忠实保留不改（PDF 电子文本层的 “Exemples” 是隐性修正，以印刷页为准）。
- 备注：ε 值域 300 dpi 确认为 F̄ₚ*（F 带 bar），Markdown $\overline{\mathbf{F}}_{p}^{*}$ 正确；印刷 “Weil + epsilon¹ ⇒ Fermat” 中 epsilon 为拼写式，Markdown “epsilon$^{1}$” 忠实；页眉 “180 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级；脚注 1 在 Markdown 中按页界插于 “([38],” 之后，位置与印刷页底一致。

## p.003（PDF p.3 / 印刷 p.181）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p003.png`（pngmono，150 dpi）。
- 核对：n(l,ρ) 定义 (1.2.1)、改写 (1.2.2)、“invariant sauvage” b(V) 句、性质 (a)(b)(c)、(1.2.3) N = ∏ l^{n(l,ρ)}、conducteur 句、1.3 节标题、det ρ: G_Q → F̄ₚ*、(1.3.1)/(1.3.2)/(1.3.3)。
- 结果：PASS。公式系数、上下标、编号、括号 (G₀:Gᵢ)、∏_{l≠p}、Z/pNZ 与 Z/NZ 的区分、ε/φ 记号全部与印刷吻合。
- 备注：页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 181” 未收入 Markdown，排版级；(c) 条末 “en l”、(1.2.3) 前后正文里个别斜体数学字母（N、ρ、p−1）在 Markdown 为纯文本，排版级不误导。

## p.004（PDF p.4 / 印刷 p.182）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p004.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p004_rho_p_glV.png`（pnggray）。
- 核对：(1.3.4) φ = χ^h、cyclotomique 句（χ: G_Q → Fₚ* 无 bar）、(1.3.5)/(1.3.6) Frob 式、Remarque（复共轭 c）、(1.3.7)/(1.3.8)/(1.3.9)、p=2 段与矩阵 (1 0; 0 −1)、§2 引言、2.1 Préliminaires、ρ_p: G_p → GL(V) ≃ GL₂(F̄ₚ)、où G_p = Gal(Q̄_p/Q_p)。
- 结果：PASS±。Markdown 在 “où G_p = Gal(Q̄_p/Q_p)” 处把法语 où 写成数学环境内的 $\mathrm{ou}$（丢 grave accent，300 dpi 裁片确认印刷为 “où”）；已修复为正体文本 “où” + 数学式。其余公式、上下标（l^{k−1}、(−1)^{k−1}、(−1)^k）、记号全部吻合。
- 备注：ρ_p 式连接号 300 dpi 确认为 ≃（simeq），Markdown \simeq 正确——150 dpi 初观似 “=”，以裁片为准，不改。χ 值域 Fₚ* 无 bar 与印刷一致。页眉 “182 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。

## p.005（PDF p.5 / 印刷 p.183）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p005.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p005_projlime.png`、`audit/300dpi/serre1987_p005_restriction_It.png`（pnggray）；600 dpi 放大：`audit/300dpi/serre1987_p005_projlime_600dpi.png`。
- 核对：I/I_p/I_t 惯性群定义句、I_t ≅ lim← Fₚₙ* 句、V^ss 半简化段、φ, φ′: I_t → F̄ₚ*、PROPOSITION 1 全陈述、Frobenius s 共轭句（sus⁻¹ ≡ u^p mod I_p）、情形 (a)/(b)、2.2 节标题与正文（ψ, ψ′ = ψ^p、F_{p²} 嵌入）、(2.2.1)/(2.2.2)/(2.2.3)。
- 结果：PASS。公式与陈述全部吻合。
- 印刷原文 quirk：① 印刷将逆向极限排作 “lim”（其下一行 “←”）加基线圆点 “·” 再接 F*ₚₙ（600 dpi 裁片确认无下标 n），Markdown 作 $\varprojlim$. $\mathbf{F}_{p^{n}}^{*}$，与印刷视觉一致，忠实保留、不按数学预期补下标；② (2.2.1) 后正文印刷作 “sa restriction à I”（300 dpi 裁片确认 I 无下标 t），Markdown 亦作 $I$，忠实保留。
- 备注：页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 183” 未收入 Markdown，排版级。

## p.006（PDF p.6 / 印刷 p.184）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p006.png`（pngmono，150 dpi）。
- 核对：(2.2.4) k = 1 + pa + b、Remarques (1)(2)（含无编号式 k = 1 + b, d'où 2 ⩽ k ⩽ p）、“torsion” 段与 ρ_p = χ^a ⊗ ρ′_p、(a,b) ↦ (0, b−a)、k′ = 1 + b − a、(2.2.5) k = k′ + a(p+1)、[24],[42] 比较句、2.3 节标题与 ρ_p|I 对角矩阵、mod(p−1) 正规化句、(2.3.1)、(2.3.2) 分段定义。
- 结果：PASS。公式、不等号方向（⩽）、分段括号、编号全部与印刷吻合；印刷中 k = 1 + b 一式无编号，Markdown 亦无编号，一致。
- 备注：页眉 “184 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级；Remarques (2) 式内 “d'où” 在 Markdown 为 \mathrm{d}′+\text{où} 拼合，渲染可读，排版级不改。

## p.007（PDF p.7 / 印刷 p.185）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p007.png`（pngmono，150 dpi）。
- 核对：2.3 节后 Remarques (1)(2)(3)（k=2、非分歧 “décaler” k by p−1、cycle de Tate [21],[22]）、2.4 节标题与正文（droite D、θ₁/θ₂）、(2.4.1) 上三角矩阵、(2.4.2) θ = χ^α ε₁/χ^β ε₂ 与 Z/(p−1)Z、e₁/e₂ 非分歧句、ρ_p|I = (χ^β *; 0 χ^α)、(2.4.3) 正规化、对称性提醒句、(2.4.4) Inf/Sup、情形 (i) 与 (2.4.5)。
- 结果：PASS。矩阵 (*, 0) 位置、χ 上标 α/β 分配、不等号端点（0 ⩽ α ⩽ p−2；1 ⩽ β ⩽ p−1）、Inf/Sup、编号全部吻合。
- 备注：页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 185” 未收入 Markdown，排版级。印刷页止于 (2.4.5)；其后的 “(Noter le cas …)” 与情形 (ii) 属印刷 p.186，在下一页核对。

## p.008（PDF p.8 / 印刷 p.186）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p008.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p008_xi_elements.png`、`audit/300dpi/serre1987_p008_remark2_KKt.png`（pnggray）。
- 核对：(2.4.5) 后 “Noter le cas” 句（χ^α = χ^β = 1、p ⩾ 3、α = 0、β = p − 1、k = p）、情形 (ii) β = α + 1、peu/très ramifié 定义、K₀ = Q_{p,nr} 句、域塔图 K | K_t | K₀、Gal(K_t/K₀) = (Z/pZ)*、Kummer 段（矩阵 (1 *; 0 1)）、(2.4.6)、x_i ∈ K₀*/K₀*^p 句、(2.4.7)、très ramifiées 句、Remarques (1)(2) 首句。
- 结果：FAIL。(2.4.6) 中印刷 “où” 在 Markdown 被拆成 “o u”（丢 accent、字符间插空格）；(2.4.6) 后正文印刷 “les x_i étant”（300 dpi 裁片确认下标为 i，与 (2.4.7) ν_p(x_i) 同形）在 Markdown 写成 $x_{t}$。两处均已依原图修复。
- 备注：域塔图 K | K_t | K₀ 在 Markdown 以 `![](images/page_7_image_4.jpg)` 保留，位置与印刷一致（“contenue dans K.” 与 “Du fait que” 两段之间）；Remarques (2) 印刷为 “Si K/K_t est peu ramifiée”（300 dpi 裁片确认），Markdown 一致，150 dpi 初观似 “K_t/K₀” 系误读；页眉 “186 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。

## p.009（PDF p.9 / 印刷 p.187）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p009.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p009_epsilon_p_target.png`（pnggray）。
- 核对：conducteur (π²)/(π^{p+1})=(pπ²) 句、(ii₁) peu ramifié 与 (2.4.8) k = 1+pa+b = 2+α(p+1)、(ii₂) très ramifié 与 (2.4.9) 分段（(α+1)(p+1) / 4）、五公式汇总句、2.5 节标题、PROPOSITION 2、(2.5.1)、χ d'ordre p−1 括注、hauteur 2 验证链 (ψ^a ψ′^b)(ψ^b ψ′^a) = (ψψ′)^{a+b} = χ^{a+b} = χ^{k−1}、puisque k−1 = pa+b ≡ a+b mod(p−1)、(2.5.2)、ε_p 非分歧句、(2.5.3) ε_p(Frob_p) = ε(p)。
- 结果：FAIL。印刷 “à valeurs dans **Fₚ***”（300 dpi 裁片确认 F 无 bar）在 Markdown 写成 $\overline{\mathbf{F}}_{p}^{*}$（多 bar，ε_p 值域改变）；已依裁片修复为 $\mathbf{F}_{p}^{*}$。其余公式与推导链逐项吻合。
- 备注：PROPOSITION 2 的法语动词 “a” 在 Markdown 被放入数学环境写作 “On $a$.”（斜体化），语义可辨、不误导，排版级不改；印刷页止于 “où Frob_p est un élément de Frobenius de G_p.”，其后 2.6 节属印刷 p.188；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 187” 未收入 Markdown，排版级。

## p.010（PDF p.10 / 印刷 p.188）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p010.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p010_rem1_matrix.png`、`audit/300dpi/serre1987_p010_281_sign.png`（pnggray）。
- 核对：2.6 节（k = 1 + a₀ + pa₁、a₁ ⩽ a₀ + 1、p=3 例 k=2,3,4,5,6,8、p=2 句）、Exemple（u: G₂ → Z/2Z、ρ₂ 矩阵 (1 u(s); 0 1)）、K/Q₂ 三行判据（√5；discr=(4): √−1/√−5；discr=(8): √2/√−2/√10/√−10）、2.7 节标题与 (2.7.1)/(2.7.2)、Remarques (1)(2)（矩阵 (x *; 0 1)、χ^m ⊗ ρ_p、[44] th.3）、2.8 节标题、PROPOSITION 3、(2.8.1) ρ_p|I ≃ (ψ′ 0; 0 ψ)。
- 结果：PASS。公式、矩阵、根式内容、编号全部与印刷吻合。
- 备注：Remarques (1) 矩阵左上元素 300 dpi 确认为斜体 x（非 χ），Markdown 一致；(2.8.1) 连接号 300 dpi 确认为 ≃（simeq），Markdown \simeq 一致——150 dpi 初观似 “=” 系分辨率不足；\sqrt{1 0} 数字间空格与判据首行的行内公式形式为排版级，渲染可读不改；页眉 “188 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。(2.8.2) 印于下一页，随 p.011 核对。

## p.011（PDF p.11 / 印刷 p.189）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p011.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p011_282_sign.png`、`audit/300dpi/serre1987_p011_psi_exponents.png`（pnggray）。
- 核对：(2.8.2) ρ_p|I ≃ (χ 0; 0 1) ou (χ *; 0 1)、schémas en groupes de type (p,p) 段（Raynaud [35]、finie en p 定义）、PROPOSITION 4、(2.8.3) det ρ_p|I = χ、(2.8.4) ρ_p est finie en p、(2.8.5) k ≡ 2 mod(p−1)、[35] cor. 3.4.4 段、ψ^n ψ′^{n′}（0 ⩽ n, n′ ⩽ 1）、四可能性 1, ψ, ψ′, ψψ′ = χ、p=2 归三句、情形 (i) {ψ, ψ′} 与 (ii) {1, χ}。
- 结果：FAIL。三处已依原图修复：① 正文 “prend ses valeurs **dan** GL₂(F_p)” 丢 s，修为 “dans”；② (2.8.2) 式内连接词 “ou” 被拆成 “o u”（300 dpi 裁片确认印刷为斜体正字 ou），修为 “ou”；③ (2.8.3)/(2.8.4) 编号错位——Markdown 把 “(2.8.3)” 写成文本行且第一式挂 \tag{2.8.4}、第二式无编号，修为第一式 \tag{2.8.3}、第二式 \tag{2.8.4}。
- 备注：(2.8.2) 连接号 300 dpi 确认为 ≃，Markdown \simeq 一致；ψ^n ψ′^{n′} 上标与 0 ⩽ n, n′ ⩽ 1 经裁片确认一致；同段 Q_p、Z_p、F_q 在 Markdown 为非粗体而印刷为粗体（与全文 \mathbf 体例不一），数学对象同一、不误导，登记排版级不改；情形 (i)/(ii) 在 Markdown 以 \tag{i}/\tag{ii} 表达左侧标号，渲染等效；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 189” 未收入 Markdown，排版级。印刷页止于 “(ii) {φ, φ′} = {1, χ}.”，其后段属印刷 p.190。

## p.012（PDF p.12 / 印刷 p.190）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p012.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p012_b_matrix.png`（pnggray）。
- 核对：cas (i)/(ii) 衔接句、J 在 Z_p 上延拓句（[35] prop. 3.3.2）、(2.8.6) 0 → A → J → B → 0、A/B étale 与 multiplicatif 句、R 上两条正合列（0 → Z/pZ → J → μ_p → 0 与 0 → μ_p → J → Z/pZ → 0）、scindée 句（Z/pZ ⊕ μ_p）、Kummer 类 u ∈ R*/R*^p、ρ_p|I ~ (χ *; 0 1)、K_t(u^{1/p}) 句与 Fontaine [15] th. 1、prop. 3 两情形 (a)（Raynaud [35] th. 2.4.3）/(b)。
- 结果：FAIL。两处已依原图修复：① “des racines **p-èmes** de l'unité” 修为印刷的 “p-ièmes”（丢 i）；② (b) 情形矩阵印刷为 (χ *; 0 1)（300 dpi 裁片确认左上为 χ 带波浪尾，与 p.188 Remarques (1) 的斜体 x 不同），Markdown 写成 x，修为 χ。其余公式与序列方向全部吻合。
- 备注：该段 Q_p/Z_p 在 Markdown 部分为非粗体（$Q_{p}$、$Z_{p}$），与印刷粗体体例不一，对象同一，排版级不改（p.011 已登记同类差异）；页眉 “190 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 (b) 段句末，2.9 节属印刷 p.191。

## p.013（PDF p.13 / 印刷 p.191）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p013.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p013_rhoI_sign.png`、`audit/300dpi/serre1987_p013_nu_valuation.png`（pnggray）。
- 核对：2.9 节标题（E semi-stable、j_E、E_p）、ρ_p: G_p → Aut(E_p) ≃ GL₂(F_p)、(2.9.1) k ≡ 2 mod(p−1)、semi-stable 限定句、PROPOSITION 5 (i)(ii) 与 k 分段（v_p(j_E) divisible par p / sinon）、v_p 正规化括注、bonne réduction 句、Tate 模型段与正合列 0 → μ_p → E_p → Z/pZ → 0、ρ_p|I ≃ (χ *; 0 1)、q_E 恒等式 j_E = q_E^{-1} + 744 + 196884 q_E + …、K = K_t(q_E^{1/p}) 与 v_p(q_E) = −v_p(j_E) 句、Remarques (1) 首句至 “Posons m =”。
- 结果：PASS。公式、分段、正合列、q_E 展开系数（744、196884）全部与印刷吻合。
- 备注：d'où 后 ρ_p|I 连接号 300 dpi 确认为 ≃，Markdown \simeq 一致；valuation 记号 300 dpi 确认印刷为拉丁 v_p（非希腊 ν），Markdown $v_{p}$ 一致（p.012 条目中核对栏写 “ν_p” 系签认笔误，本页起统一以 v_p 为准，md 无需改动）；印刷 “i.e. a, soit bonne réduction…” 的 “a,” 为印刷原文 quirk，Markdown 忠实保留；196884 在 Markdown 为 “1 9 6 8 8 4” 数字带空格，渲染可读，排版级不改；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 191” 未收入 Markdown，排版级。印刷页止于 “Posons m =”，Remarques (1) 余部属印刷 p.192。

## p.014（PDF p.14 / 印刷 p.192）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p014.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p014_pieme_ab.png`（pnggray）。
- 核对：−v_p(j_E)/p 与 u = p^{pm}j_E 句、(a) u^{p−1} ≡ 1 (mod p²) ⇒ K = K_t、ρ_p|I ≃ (χ 0; 0 1)、(b) u^{p−1} ≢ 1 (mod p²) ⇒ [K:K_t] = p、ρ_p|I ≃ (χ *; 0 1)、[6] prop. 5.1.(3)(d) 反驳句、(2) 类型 additif 段（p ≡ 1 mod 3、y² = x³ + Ax + B、v_p(A) ⩾ 1、v_p(B) = 1、type c₁ de Néron）、ρ_p|I ≃ (χ^β 0; 0 χ^α) ou (χ^β *; 0 χ^α)、α = (p−1)/6、β = (5p+1)/6、p > 7 与 p = 7（k = 14 / k = 2、v_p(A) ⩾ 2）、§3 标题、3.1 段（N、k、ε）、(3.1.1)、formes paraboliques 引言与 Identifions Q̄ 句。
- 结果：FAIL。一处已依原图修复：Remarques (1)(a) 中矩阵印刷为 (χ 0; 0 1)（300 dpi 裁片确认左上 χ 带弯尾），Markdown 写成 x，修为 χ。
- 印刷原文 quirk：本页 “la puissance p-ème” 印刷确为 p-ème（无 i；300 dpi 裁片确认），与 p.190 页的 “p-ièmes” 排印不一致属印刷原文自身差异，Markdown 两处各自忠实保留。
- 备注：(a)(b) 连接号 300 dpi 确认为 ≃，Markdown 一致；“à coefficients dans F̄ₚ” 处 Markdown 用非粗体 \overline{F}_p，体例差异排版级不改（同 p.011 登记）；页眉 “192 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “le choix de la place en question définit”，ε₀ 式属印刷 p.193。

## p.015（PDF p.15 / 印刷 p.193）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p015.png`（pngmono，150 dpi）。
- 核对：z ↦ z̃ 同态句、ε₀: (Z/NZ)* → Z̄* 定义式、relèvement multiplicatif 句、ε₀(x)˜ = ε(x)、ε₀(−1) = (−1)^k 句、Γ₀(N) 上 formes paraboliques 引言、(3.1.2) F = Σ A_n q^n（q = e^{2πiz}）、收敛半平面句、条件 (a)（ε₀(d)(cz+d)^k F(z)、Γ₀(N)）、条件 (b)（SL₂(Z)、z ↦ (cz+d)^{−k}F((az+b)/(cz+d))、q 换 q^{1/N}）、type (N,k,ε₀) 缩写句、DÉFINITION（f = Σ aₙqⁿ、aₙ ∈ F̄ₚ、F = Σ Aₙqⁿ、Aₙ ∈ Z̄、F̃ = f、Ãₙ = aₙ）、anneau local 括注。
- 结果：PASS。公式、矩阵、群记号（Γ₀(N)、SL₂(Z)）、上下标全部与印刷吻合。
- 备注：印刷将约化记号 ~ 排在 ε₀(x) 正上方，Markdown 作上标 \varepsilon_0(x)^{\sim}，语义同一（mod p 约化），排版级不改；“à coefficients dans F̄ₚ” 处 \overline{F}_p 非粗体体例同前登记；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 193” 未收入 Markdown，排版级。印刷页止于 “Cela ne changerait rien.)”，S(N,k,ε) 句属印刷 p.194。

## p.016（PDF p.16 / 印刷 p.194）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p016.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p016_euler_product.png`、`audit/300dpi/serre1987_p016_316_Z.png`、`audit/300dpi/serre1987_p016_nmid_glyphs.png`（pnggray）。
- 核对：S(N,k,ε) 引言、(3.1.3)（Shimura [51] th. 3.52、[11] prop. 2.7）、(3.1.4) T_l/U_l 作用式（ε(l)l^{k−1}、l∤pN、l|pN）、U_p 为 T_p (ε₀(p)p^{k−1}) 的 mod p 约化句、k ⩾ 2、(3.1.5)（f ≠ 0、a₁ = 1 正规化、T_l(f) = a_l f / U_l(f) = a_l f）、L_f(s) = Σ aₙn^{−s}、Euler 积、f 由 a_l 决定句、(3.1.6)（F de type (N,k,ε₀)、à coefficients dans Z̄、A₁ = 1、F̃ = f）。
- 结果：FAIL。两处已依原图修复：① (3.1.5) 中 “T_l(f) = a_l f pour **l ⊬ pN**”（Duke 字体不整除符 ⊬ 呈 + 样，与 (3.1.4) 的 l∤pN 同字形，见裁片 nmid_glyphs）在 Markdown 写成真加号 “l + pN”，修为 l \nmid pN；② (3.1.6) 中 “T_l(**l ⊬ N**)” 同样被写成 “l + N”，修为 l \nmid N。
- 备注：Euler 积因子-下标配对经 300 dpi 裁片确认与 Markdown 一致（∏_{l|pN}(1−a_l l^{−s})^{−1}·∏_{l∤pN}(1−a_l l^{−s}+ε(l)l^{k−1}l^{−2s})^{−1}），且与 T_l/U_l 定义及经典好/坏素数因子结构吻合，150 dpi 阶段的 “颠倒” 怀疑系误读；(3.1.6) “à coefficients dans Z̄” 的 Z 带 bar（裁片确认），Markdown \overline{\mathbf{Z}} 一致；页眉 “194 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “A₁ = 1; F̃ = f.”。

## p.017（PDF p.17 / 印刷 p.195）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p017.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p017_Al_line.png`、`audit/300dpi/serre1987_p017_reecrite.png`、`audit/300dpi/serre1987_p017_rho_simeq.png`（pnggray）。
- 核对：En effet 提升句（[11] lemme 6.11、Ã_l = a_l、F̃ = f）、(Bien entendu…) 非唯一性括注、(3.1.7) Deligne 定理与 ρ_f: G_Q → GL₂(F̄ₚ)、(D) 性质（Frob_l 非分歧）、(3.1.8) Tr ρ_f(Frob_l) = a_l、(3.1.9) det ρ_f(Frob_l) = ε(l)l^{k−1}、(3.1.10) det ρ_f = ε·χ^{k−1}、Compte tenu 段（det ρ_f(c) = −1、caractère impair）、Remarque（niveau p^mN、poids 2/niveau p ⇔ poids p+1/niveau 1、[43] th. 11）、3.2 节标题与 ρ: G_Q → GL(V) ≃ GL₂(F̄ₚ)、F̄ₚ-espace vectoriel 句。
- 结果：PASS。全部文字与公式吻合。
- 备注：三处 150 dpi 疑点经 300 dpi 裁片全部排除——① 印刷确为 “Ã_l = a_l”（A 带 tilde，Markdown \tilde{A}_l 一致）；② 印刷确为 “récrite”（单 e，Markdown 一致）；③ 3.2 节 ρ 式连接号确为 ≃（Markdown \simeq 一致）。(D) 段 “et, si l'on note” 的逗号为 Markdown 增益标点，语义无差，排版级不改；Remarque 段 \overline{F}_p 非粗体体例同前登记；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 195” 未收入 Markdown，排版级。印刷页止于 “V étant un F̄ₚ-espace vectoriel de dimension 2. On”。

## p.018（PDF p.18 / 印刷 p.196）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p018.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p018_323eps.png`、`audit/300dpi/serre1987_p018_323eps_600dpi.png`、`audit/300dpi/serre1987_p018_placeQ.png`（pnggray）。
- 核对：(3.2.1) ρ est irréductible、(3.2.2) det ρ est impair cf. (1.3.8)、conjecture 句、(3.2.3?) 定义、Il convient de préciser 句、(3.2.4?) 与 (3.2.3?) 引用、f normalisée 句、(3.2.5) Tr(Frob_{l,ρ}) = a_l et det(Frob_{l,ρ}) = ε(l)l^{k−1}、densité 1 括注、(3.2.6?) 与 (a)/(b)（droite D、V/D、quotient étale、a_l 特征值句）、Remarques sur (3.2.6?) (1)（droite 唯一性、conducteur N）至 “v_l(cond.ε)” 段首。
- 结果：FAIL。两处已依原图修复：(3.2.4) 定义处 Markdown 写成 “(3.2.4.)” 且引用写成 “de (3.2.3.)”（丢下标 ?），而印刷为 (3.2.4_?)/(3.2.3_?)（600 dpi 裁片确认编号下标为问号字形），且 Markdown 自己的引用处 “satisfasse à (3.2.3?) et (3.2.4?)” 带 ?；已统一修复为 “(3.2.4?)”/“(3.2.3?)”。
- 印刷原文 quirk：编号 (3.2.3?)/(3.2.4?)/(3.2.6?) 的下标经 600 dpi 放大确认为问号 “?” 字形（上弯钩带点，非 ε 月牙形）——Duke 排印原样，Markdown 以平排 “(3.2.3?)” 忠实保留，不按数学预期改成 ε。
- 备注：“une place l-adique donnée de Q̄” 的 Q 带 bar（300 dpi 裁片确认），Markdown $\overline{\mathbf{Q}}$ 一致；(3.2.5) 用 Frob_{l,ρ} 记号与 p.182 (1.3.5) 一致；页眉 “196 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “…valeur propre λ de la substitution de Frobenius en l opérant sur V/D est telle”，Remarques (1) 余部属印刷 p.197。

## p.019（PDF p.19 / 印刷 p.197）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p019.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p019_footnote_line.png`（pnggray）。
- 核对：Remarques (1) 余部（λ² = ε_prim(l)l^{k−2}、a_l² = ε_prim(l)l^{k−2} 无编号式、[27] th. 3 (iii)）、(2) l=p ramifiée 句（a_p 唯一、corps de rationalité、F_p）、(3) l=p non ramifiée 句（λ、μ、λμ = ε(p)、ρ_f ~ ρ、corps de définition、n° 5.1）、(4) Atkin-Lehner-Li W_l (l|N)、constantes locales（Deligne [9], §6）、Remarques sur (3.2.4?) (5)（N、k minimaux、F̃、forme primitive newform [11],[27]）、(6) Katz [23] 定义、a priori、脚注 ² 全文。
- 结果：FAIL。脚注 ² 在 Markdown 被解析成 4 个碎片 span（“$^{2}$ La”、“$p = 2$”、“$k + p - 1$”、“$p \geqslant 5,$”）加 1 个完整 span 的重复伪影；已删除 4 个碎片、保留完整版。其余文字与公式逐项吻合。
- 印刷原文 quirk：脚注中 “Avec la définiton adoptée ici” 印刷确为 “définiton”（300 dpi 裁片确认丢 i），Markdown 忠实保留。
- 备注：正文末行印刷为 “d'étudier de ce”（300 dpi 裁片确认，跨页接 “point de vue”），Markdown “d'étudier de ce” 一致，150 dpi 阶段的 “多 de” 怀疑系误读；编号 (3.2.4?)/(3.2.6?) 沿用 p.018 的问号下标 quirk；“un espace $a$ priori” 的 a 单独数学环境，排版级不改；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 197” 未收入 Markdown，排版级。印刷页止于 “d'étudier de ce”，其余属印刷 p.198。

## p.020（PDF p.20 / 印刷 p.198）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p020.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p020_331eps.png`（pnggray）。
- 核对：point de vue 段（k=1、Katz 定义反问句）、3.3 Exemple k=2（ρ: G_Q → GL₂(F_p) 无 bar）、条件 (a) det ρ = χ、(b) absolument irréductible（F̄ₚ）、(c) finie en p n° 2.8、[p ≠ 2 时 (b′) 替代条件括注（ρ(c) 特征值 ±1、rationnelle sur F_p、contredirait (b′)）、N/k/ε 句（ε = 1、k = 2、prop. 4 du n° 2.8）、(3.3.1?)、(3.2.6?) 系数句（F_p、p = 2 例外）、J₀(N)/X₀(N)/Γ₀(N) 句、(3.3.2?)、3.4 Questions (1)(2)（Ash-Stevens [2]、GL₂/GL_N/其他整体域列表）。
- 结果：FAIL。两处已依原图修复：(3.3.1) 与 (3.3.2) 定义处 Markdown 写成 “(3.3.1.)”/“(3.3.2.)”（丢下标 ?），印刷为 (3.3.1_?)/(3.3.2_?)（300 dpi 裁片确认问号字形，与 p.196 同款印刷 quirk），修为 “(3.3.1?)”/“(3.3.2?)”。
- 备注：ρ 式 F_p 无 bar 与印刷一致（与 (b) 的 F̄ₚ 形成对照，Markdown 正确区分）；GL₂/GL_N/Q 在 (2) 列表中为非粗体，体例差异排版级不改；页眉 “198 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “de remplacer Q par d'autres corps globaux.”，§4 标题属印刷 p.199。

## p.021（PDF p.21 / 印刷 p.199）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p021.png`（pngmono，150 dpi）。
- 核对：§4 标题与应用列表五项（n°s 4.1-4.3、4.4、(p,p) sur Z 4.5、Taniyama-Weil + variétés abéliennes 4.6-4.7、cohomologie/Betti 4.8）、Excepté la dernière 句（(3.2.4?)、ε = 1, k = 2、n° 3.3）、4.1 节（A,B,C 两两互素、A+B+C=0）、x₁,x₂,x₃ 选择式、y² = (x−x₁)(x−x₂)(x−x₃)、x₁=A/x₂=0/x₃=−B、(4.1.1) y² = x(x−A)(x+B)、E_{A,B,C}、Remarque（signature ±1、tordue Q(√−1)/Q）、(4.1.2)（l|ABC、type multiplicatif、modèle minimal、Tate [4] p.47）、(4.1.3)、(4.1.4) A ≡ −1 (mod 4), B ≡ 0 (mod 32)。
- 结果：FAIL。一处已依原图修复：§4 标题印刷为 “Ces applications concernent:”，Markdown 写成 “concern”（缺 “ent”），已补全。其余文字与公式逐项吻合。
- 备注：Taniyama-Weil 拼法与印刷一致；“(mod 3 2)” 数字带空格渲染为 32，排版级；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 199” 未收入 Markdown，排版级。印刷页止于 (4.1.4)，变量替换式属印刷 p.200。

## p.022（PDF p.22 / 印刷 p.200）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p022.png`（pngmono，150 dpi）。
- 核对：变量替换 x = 4X, y = 8Y + 4X、(4.1.5) Y² + XY = X³ + cX² + dX（c = (B−1−A)/4、d = −AB/16）、(mod 2) 分段（A ≡ 7 / A ≡ 3 mod 8）、cubique sur F₂ 段（point double (0,0)、tangentes rationnelles、Tate loc. cit.、équation minimale、Spec(Z)）、(4.1.6) Δ = 2^{−8}A²B²C²、semi-stable/conducteur 句、(4.1.7) cond(E) = rad(ABC)、rad(X) 定义句、(4.1.8) j_E = 2⁸(C²−AB)³/A²B²C²、(4.1.9) 分段（−2v_l(ABC) / 8−2v₂(ABC)）、Points de p-division 段（p ⩾ 5、ρ_p^E: G_Q → GL₂(F_p)）。
- 结果：PASS。公式、分段条件、上下标（2^{−8}、2⁸、³、v_l/v₂）全部与印刷吻合。
- 备注：F₂/F_p 在 Markdown 部分为非粗体（$F_{2}$），与印刷粗体体例不一，排版级不改（同前登记）；“−AB/1 6” 数字带空格渲染 16，排版级；valuation 记号与 p.013 裁片实证一致为拉丁 v；页眉 “200 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 ρ_p^E 式，“fournie par…” 句属印刷 p.201。

## p.023（PDF p.23 / 印刷 p.201）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p023.png`（pngmono，150 dpi）。
- 核对：PROPOSITION 6（ρ_p^E irréductible、absolument irréductible 括注）、réductible 反证段（sous-groupe X、caractère unité/χ、[41] p.307、torsion ⩾ 4p ⩾ 20、Mazur [28] th. 8、E′ = E/X）、Remarque（Mazur [29]）、invariants 引言、(4.1.10) ε = 1、(4.1.11) k = 2 / k = p + 1（v_p(Δ)、prop. 5 du n° 2.9）、(4.1.12) conducteur N（l ≠ p、v_l(Δ)）、Tate 模型 “G_m/q^Z” 句、Remarque（v_l(Δ) 条件）、(4.1.13) v_l(ABC) ≢ {0; 4} (mod p) 分段、4.2 节标题、THÉORÈME 1（Admettons (3.3.1?)、a^p + b^p + c^p = 0、a,b,c ∈ Z、abc ≠ 0）、homothétie 段（b ≡ 0 mod 2、a ≡ −1 mod 4）、A = a^p, B = b^p, C = c^p。
- 结果：FAIL。一处已依原图修复：Remarque 段 Markdown 把 “v_l(Δ)” 的下标写成大写 I（$v_{I}(\Delta)$），印刷为小写 l（同段 (4.1.12)/(4.1.13) 均为小写 l），修为 $v_{l}$。其余逐项吻合。
- 备注：“Admettons (3.3.1?)” 引用带 ? 与印刷一致；“G_m/q^Z” 粗体一致；页眉 “201 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 A = a^p, B = b^p, C = c^p 式。

## p.024（PDF p.24 / 印刷 p.202）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p024.png`（pngmono，150 dpi）。
- 核对：(4.1.4) 条件满足句、v_l(ABC) ≡ 0 (mod p) 式、(4.1.11)+(4.1.13) ⇒ k = N = 2 段（prop. 6、X₀(2) genre 0、D'où le théorème）、Remarque（Hurwitz [20] 1886）、Hellegouarch [19]/Vélu [54]/Frey [16],[17] 段、4.3 节标题（p ⩾ 11）、THÉORÈME 2（Admettons (3.3.1?)、L ≠ p）、S = {3,5,7,11,13,17,19,23,29,53,59}、(4.3.1) a^p + b^p + L^α c^p = 0、abc ≠ 0 句、证明开头（0 < α < p、B pair、2^p、a fortiori 32、A ≡ −1 mod 4、k = 2、N = 2L）、f = q + a₂(f)q² + ⋯ + a_n(f)q^n + ⋯、F̄ₚ/2L 句。
- 结果：PASS。公式、集合元素、引用编号（[19]/[54]/[16]/[17]/[20]）、上下标全部与印刷吻合。
- 备注：S 集合内 “1 1, 1 3…” 数字带空格渲染正常，排版级；印刷 “avec a, b, c ∈ Z et abc ≠ 0” 的 “et” 与 Markdown 一致（th. 1 处印刷无 “et”，Markdown 同样无——两处各自忠实）；页眉 “202 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “soit isomorphe à ρ_p^E. Nous”，其后 “allons voir…” 段与 LEMME 1 属印刷 p.203。

## p.025（PDF p.25 / 印刷 p.203）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p025.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p025_b1_neq.png`、`audit/300dpi/serre1987_p025_b2_mu3.png`、`audit/300dpi/serre1987_p025_table.png`（pnggray）。
- 核对：allons voir 段（L = 3,5、X₀(6)/X₀(10) genre 0、L ⩾ 7）、LEMME 1 (a)(b)(c)（a₃(f) = 0 ou ±4、a₅(f) = ±2 ou ±6）、(3.1.6) f = F̃ 段（niveau L 反证、conducteur 2L）、(b₁) bonne réduction en 3（ABC ≠ 0 mod 3、Ě、点数被 4 整除、1 ± 3 ± 2√3、trace 0、a₃(f) = 0 (dans F_p)、(3.1.8)）、(b₂) mauvaise réduction en 3（déployée/Tate、G_{Q₃}-module E_p extension de Z/pZ par μ_p、特征值 1 et 3、a₃(f) = 4 / −4）、(c) 类推段、LEMME 2（F、Aₙ ∈ Z̄、A₃ = ±1, ±2 ou ±3 si L ≠ 23、A₅ = 4 si L = 23）、A₃ 数值表（L = 7/13/17/19/29/53/59）。
- 结果：PASS。文字、公式与表格逐项吻合。
- 印刷原文 quirk：(b₂) 段印刷作 “E_p est extension de Z/pZ par μ_p”（300 dpi 裁片确认 p 系下标），但该处 Frobenius 特征值 “1 et 3” 在数学上对应 3-division——疑为原文笔误，print 原文优先，Markdown 同作 E_p/Z/pZ/μ_p 忠实保留。
- 备注：三处 150 dpi 疑点经 300 dpi 裁片全部排除——① (b₁) 印刷确为 “ABC ≠ 0 (mod 3)”（单斜杠）；② (b₂) 确为 p 系下标（见上）；③ 表格 L=59 列印刷确为 “−1, −1, 2, 2”，Markdown 表格逐格一致。LEMME 1 (b)(c) 的法语动词 a 在 Markdown 入数学环境（“On $a$…”），同 p.009 quirk，排版级；“2 3” 数字空格排版级；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 203” 未收入 Markdown，排版级。印刷页止于 A₃ 数值表，“L = 11 ne figure pas…” 句属印刷 p.204。

## p.026（PDF p.26 / 印刷 p.204）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p026.png`（pngmono，150 dpi）。
- 核对：(L = 11) 括注、th. 2 证明收尾（L = 23：±2 ou ±6 ≡ 4 mod p、p ⩾ 7；L ≠ 23：0 ou ±4 ≡ ±1, ±2 ou ±3 mod p、p ⩾ 11）、Remarques (1)（p = L 时 k = p + 1、N = 2、(3.2.4?)）、(2)（p = 5/7、Dénes [12]）、(3)（L = 31 Mersenne、ρ_p^E、F = q + q² + q⁴ − 2q⁵ + q⁸ + … niveau 62、a⁵ + b⁵ + 31c⁵ = 0 解 (1, −2, 1)、y² = x(x+1)(x−32)、courbe de Weil）、15c^p 与 3b^p + 5c^p 方程（N = 30）、(4) Mazur 结果开头（L 非 Fermat 非 Mersenne、2^n ± 1 跨页）。
- 结果：FAIL。一处已依原图修复：Mazur 结果的引用 Markdown 写成 “(3.3.1$_{2}$)”（下标 2），印刷为 (3.3.1_?)（问号下标，同 p.196 quirk），修为 (3.3.1$_{?}$)。
- 备注：本段引用 Markdown 用 $_{?}$ 下标形式、他处用平排 “(3.2.4?)”，形式不一但语义同为问号下标，排版级；“Mersenne–cf.” 印刷为 en-dash 连接，Markdown 用连字符，排版级；“1 5 c^p” 数字空格排版级；页眉 “204 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “…ne peut pas s'écrire sous la forme”，“2^n ± 1)” 句属印刷 p.205。

## p.027（PDF p.27 / 印刷 p.205）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p027.png`（pngmono，150 dpi）。
- 核对：Mazur 结果余部（C_L、a^p + b^p + L^α c^p = 0、abc ≠ 0、conducteur 2L 段）、4.4 节标题（Brumer-Kramer [6] §9）、PROPOSITION 7（|Δ| p-ème 幂、p ⩽ 7）、p = 2 段（𝔖₃/𝔄₃、[6] prop. 9.2、Mazur [29] th. 4、(N,k,ε) = (1,2,1)、niveau 1 矛盾）、PROPOSITION 8（Δ = ±P^m、Setzer-Neumann、P = 11,17,19,37）、m > 1 段（[33],[50]、P = 17、Miyawaki [32]、P = 11 / 19 ou 37）、4.5 节标题（p ⩾ 3）、THÉORÈME 3 与三选项式（Z/pZ ⊕ Z/pZ、Z/pZ ⊕ μ_p、μ_p ⊕ μ_p）。
- 结果：PASS±。一处已依原图修复：THÉORÈME 3 引用处 Markdown 写成 “Admettons (3.3.1?), Tout schéma…”（句号误作逗号、逗号后大写），印刷为 “(3.3.1_?). Tout schéma…”，修为句号。其余文字、引用与公式逐项吻合。
- 备注：引用编号 (3.3.1_?) 的问号下标沿用已登记 quirk；𝔖₃/𝔄₃ Fraktur 记号 Markdown 一致；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 205” 未收入 Markdown，排版级。印刷页止于三选项式，“Soit J un schéma…” 段属印刷 p.206。

## p.028（PDF p.28 / 印刷 p.206）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p028.png`（pngmono，150 dpi）。
- 核对：Soit J 段（Spec(Z) − {p}、ρ: G_Q → GL₂(F_p)、Raynaud [35] prop. 3.3.2）、LEMME 3（三选项 Z/pZ ⊕ Z/pZ、Z/pZ ⊕ μ_p、μ_p ⊕ μ_p）、0 → A → J → B → 0、Oort-Tate [34] 句、Fontaine [15] n° 3.4.3、LEMME 4（det ρ = χ、χ^i、0 ⩽ i ⩽ p−2、i = 0,1,2、Minkowski、i = 1）、th. 3 证明收尾（(1,2,1)、(3.3.1?)、prop. 7）、Remarques (1)（p = 3…17、(p,…,p)、Fontaine [15]）、(2)（Z/2Z 组合、extension non scindée、ρ = (1 u; 0 1)）。
- 结果：PASS。公式、引用编号、记号（⊕、μ_p、χ^i）全部与印刷吻合。
- 备注：Markdown 将 “LEMME 4” 行标记为 ## 标题（其余 LEMME 为正文段落），渲染样式差异不改变内容，排版级不改；F_p/G_Q 等粗体一致；页眉 “206 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 ρ = (1 u; 0 1) 式，“où u: G_Q → Z/2Z…” 句属印刷 p.207。

## p.029（PDF p.29 / 印刷 p.207）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p029.png`（pngmono，150 dpi）。
- 核对：u 核 Gal(Q̄/Q(i)) 句、2-division 曲线 y² + xy + y = x³ − x² − x − 14（conducteur 17、discriminant −17⁴）、4.6 节标题（j_E、N）、THÉORÈME 4（Admettons (3.3.1?)、courbe de Weil de niveau N）、J₀(N)/X₀(N) 括注、ρ_p^E 定义、(4.6.1) det ρ_p^E = χ、LEMME 5（C_E）、(4.6.2)/(4.6.3)、Mazur [29] p > 163 句、[18],[40],[49]、N_p divise N、p ⩾ 5 条件句、(a) p∤N、(b) v_l(N) = 1 ⇒ p∤v_l(j_E)、Noter 括注（v_l(j_E) < 0）、Bornons-nous 段（ρ_{f_p}、f_p = Σa_{n,p}qⁿ、F̄ₚ）、(3.1.6) relève 句。
- 结果：PASS。公式、引用编号、上下标（−17⁴、a_{n,p}）全部与印刷吻合。
- 备注：“− 1 4” 数字带空格渲染 14，排版级；valuation 记号 v_l 与印刷一致；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 207” 未收入 Markdown，排版级。印刷页止于 “il existe une forme parabolique de poids 2 et de niveau N”，F = ΣAₙqⁿ 式属印刷 p.208。

## p.030（PDF p.30 / 印刷 p.208）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p030.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p030_464_nmid.png`（pnggray）。
- 核对：F̃ = f_p 有限性论证段、a_l ≡ a_{l,p} (mod p) 式、A_l − a_l image 段、(4.6.4) A_l = a_l pour tout l ⊬ N、courbe de Weil E_F 段（Faltings [13],[14]、isogènes sur Q、D'où le th. 4）、Remarques (1)（Colmez、Colloque de Luminy 1986）、(2)（primitive、Carayol [8]）、(3) Shimura 例子（K = Q(√D)、σ、E^σ、λ^σ∘λ = −c、[52] p.184、(N,2,ε)、(3.2.4?)、Q(√−c)）、n°s 4.7 et 4.8 句、4.7 节标题首句。
- 结果：FAIL。一处已依原图修复：(4.6.4) 式印刷 “pour tout l ⊬ N”（300 dpi 裁片确认不整除符 + 样字形，同 p.194 已裁决字形），Markdown 写成 “l + N”（真加号），修为 l \nmid N。其余逐项吻合。
- 备注：F̄ₚ/Z̄/Q 粗体一致；(3.2.4$_{?}$) 下标问号沿用 quirk；页眉 “208 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 4.7 节首句 “(cf. Ribet”，其后属印刷 p.209。

## p.031（PDF p.31 / 印刷 p.209）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p031.png`（pngmono，150 dpi）。
- 核对：K_X = Q ⊗ End_Q(X) 定义句、Shimura [51] §7.5 句、THÉORÈME 5（Admettons (3.3.1?)、racine n-ème du conducteur）、th. 4 类比句、(4.7.1) λ-adiques 系统句、Ribet [36]、a_l trace 句、(4.7.2) N^n 句、[18] exposé IX §4 / [40] n° 2.1 段、Fixons 段（λ_p、F_p、ρ_p^X: G_Q → GL₂(F_p)）、(4.7.3) det ρ_p^X = χ、(4.7.4)（Faltings [14] p. 204、th. 6）、(4.7.5)。
- 结果：FAIL。两处已依原图修复：① THÉORÈME 5 引用 Markdown 写成 “(3.3.1)”（丢下标 ?），印刷为 (3.3.1_?)，修为 “(3.3.1?)”；② “c'est un entier du corps K_X” 处 Markdown 下标写成小写 x（$K_{x}$），印刷为大写 X，修为 $K_{X}$。其余逐项吻合。
- 备注：K_X 大小写在 Markdown 全文他处均正确为大写，仅此一处笔误；(4.7.2)-(4.7.5) 编号连续一致；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 209” 未收入 Markdown，排版级。印刷页止于 (4.7.5)，其后 Néron 模型句属印刷 p.210。

## p.032（PDF p.32 / 印刷 p.210）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p032.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p032_nmid_x2.png`（pnggray）。
- 核对：Néron 模型句（diviseur de N）、(4.7.6) k = 2、prop. 4 du n° 2.8、(4.7.3)…(4.7.6) 汇总句与 (3.3.1?)、f_p = Σa_{n,p}qⁿ、ρ_p^X ≃ ρ_{f_p}、a_{l,p} = ã_l pour tout l ⊬ N, l ≠ p、F = ΣAₙqⁿ、Z̄/P 无限/K_X 段、Ã_l = a_{l,p} = ã_l 式、Faltings [13]、Remarque（primitive、Carayol [8]）、4.8 节标题与四个定义项（X、X_C、m impair、H^m(X_C, C)）、(4.8.1)/(4.8.2) Hodge 分解、Choisissons S 句。
- 结果：FAIL。两处已依原图修复：Markdown 两处把不整除符写成真加号——“a_{l,p} = ã_l pour tout **l + N**, l ≠ p” 与 “Si **l + N**, on a donc”，300 dpi 裁片确认印刷均为 l ⊬ N（+ 样字形，同 p.194/p.208 已裁决字形），均修为 l \nmid N。其余逐项吻合。
- 备注：(4.8.1) 与 (4.8.2) 在 Markdown 合并为一行，印刷分两行，内容一致，排版级不改；页眉 “210 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “on peut définir une réduction”，modulo l 段属印刷 p.211。

## p.033（PDF p.33 / 印刷 p.211）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p033.png`（pngmono，150 dpi）。
- 核对：modulo l 段（X̃_l、π_l/π′_l、Deligne、corps quadratique imaginaire）、(4.8.3) π′_l = π̄_l et π_lπ̄_l = l^m、(4.8.4) a_l(X) = π_l + π̄_l、|a_l(X)| ⩽ 2l^{m/2}、unicité 括注（[40] n° 1.2）、THÉORÈME 6（Admettons (3.2.4?)）、(a) N ⩾ 1、(b) (N, m+1, 1)、F = q + ⋯ + Aₙqⁿ + …、(4.8.5) A_l = a_l(X) pour l ∉ S、En d'autres termes 括注、galoisiennes 重述段（X̄、H^m_et(X̄, Q_p)、H_p、Z_p*、arithmétiques/géométriques、k = m + 1）、Démonstration 开头（T 有限、p ∉ T、dim H^m_et = 2）。
- 结果：PASS。公式、编号、上下标（l^m、2l^{m/2}、H^{m+1}_et）全部与印刷吻合。
- 备注：页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 211” 未收入 Markdown，排版级。印刷页止于 “définit alors une”，ρ_p 式及其后内容属印刷 p.212。

## p.034（PDF p.34 / 印刷 p.212）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p034.png`（pngmono，150 dpi）。
- 核对：ρ_p: G_Q → GL₂(F_p) 式、non ramifiée hors S et p 段（det ρ_p = χ^m、J-M. Fontaine、W. Messing）、(4.8.6) (Fontaine—non publié)（k = m + 1）、Hodge 括注、N_p = ∏_{l∈S} l^{n(l,p)}（n(l,p) ⩾ 0）、C₃ de [40] 段（bornés、formule (11)）、(4.8.7) 同余式组（mod 2³ / mod 3² / mod l，si 2 ∈ S / si 3 ∈ S / pour tout l ∈ S, l ⩾ 5）、(4.8.8)（n(l,p) ⩽ 9 pour l = 2；⩽ 5 pour l = 3；⩽ 2 pour l ⩾ 5）、En effet 句首（I_{l,p}、SL₂(F_p)、diviseur de）。
- 结果：PASS。公式、同余条件、不等式界全部与印刷吻合。
- 备注：页眉 “212 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “…et son ordre est un diviseur de”，p(p²−1) 段属印刷 p.213。

## p.035（PDF p.35 / 印刷 p.213）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p035.png`（pngmono，150 dpi）。
- 核对：p(p²−1) 段（l ⩾ 5 modérée、n(l,p) ⩽ 2、Sylow cycliques d'ordre 3 / quaternioniens d'ordre 8、n° 4.9、n(3,p) ⩽ 5、n(2,p) ⩽ 9）、Notons P 段、(4.8.9)、P′/semi-simplification 段（α, β: G_Q → Fₚ*、αβ = χ^m）、(4.8.10) a_l(X) ≡ α(l) + α(l)^{−1}l^m (mod p)、α₀ relèvement 段（(Z/N_pZ)* → Z̄*、P″）、b_l 式、a_l(X) = b_l 段、{π_l, π̄_l} = {α₀(l), α₀(l)^{−1}l^m}、absurde 句、P₁/∏_{l∈S}l^{n(l)} 段、(a)(b)(c)（χ^m、N、m + 1）。
- 结果：PASS。公式、引用编号、上下标（α(l)^{−1}l^m、χ^m、P″）全部与印刷吻合。
- 备注：页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 213” 未收入 Markdown，排版级。印刷页止于 “(c) l'invariant k de ρ_p est égal à m + 1.”，“Comme m est impair…” 段属印刷 p.214。

## p.036（PDF p.36 / 印刷 p.214）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p036.png`（pngmono，150 dpi）。
- 核对：Comme m est impair 段（(3.2.4?)、k = m + 1、f_p = Σa_{n,p}qⁿ、ρ_p ≃ ρ_{f_p}）、th. 4 类比收尾句、Remarques (1)（Schoen [37]、m = dim X = 3、k = 4、S = {5}、N = 5²、P₄ 五次超曲面 X₀⁵ + … − 5X₀X₁X₂X₃X₄ = 0、Faltings [13] p. 362-363、[47]）、(2)（S. Bloch [5]、archimédiennes、motifs、Deligne [10]、Weil [55]、(2π)^{−s}Γ(s)）、(3)（(m−r, r) + (r, m−r)、0 ⩽ r < m/2、(3.2.4?)、m − 2r、a_l(X) = l^rA_l、torsion de Tate）、4.9 节标题与记号区（K complet、v_K: K* → Z、K̄、G_K = Gal(K̄/K)）。
- 结果：PASS。公式、引用编号、上下标（5²、(2π)^{−s}、l^rAₗ）全部与印刷吻合。
- 备注：v_K 式中目标域 “Z” 在 Markdown 为非粗体，印刷粗体，体例差异排版级不改（同前登记）；页眉 “214 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “…le groupe de Galois de K̄ sur K.”，“On suppose que K…” 段属印刷 p.215。

## p.037（PDF p.37 / 印刷 p.215）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p037.png`（pngmono，150 dpi）。
- 核对：On suppose 段（e_K = ν_K(p)、indice de ramification absolu、changement de notation 括注）、Soit maintenant V 段（Ω、ρ: G_K → GL(V)、exposant du conducteur n(ρ) ⩾ 0、(G_i)_{i⩾0}）、(4.9.1) n(ρ) = Σ_{i⩾0}(g_i/g₀)dim V/V_i、g_i/V_i 句、(4.9.2) n(ρ) = dim V/V₀ + b(ρ)、b(ρ) = Σ_{i⩾1}…、invariant sauvage 句（[39] §19.3）、PROPOSITION 9（p^c、G₁、N sur Ω）、(4.9.3) b(ρ) ⩽ N e_K(c + 1/(p−1))、stricte 句、COROLLAIRE、(4.9.4) n(ρ) ⩽ N(1 + e_K c + e_K/(p−1))。
- 结果：PASS。公式、量词（Σ 端点 i⩾0/i⩾1）、不等式方向与端点全部与印刷吻合。
- 备注：(4.9.3) 左端 Markdown 为 b(ρ) 与印刷一致；b(ρ) 式内 \mathrm{dim} 与他处 \dim 混用，渲染等效，排版级；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 215” 未收入 Markdown，排版级。印刷页止于 (4.9.4) 后 stricte 句，“Démonstration de la prop. 9” 属印刷 p.216。

## p.038（PDF p.38 / 印刷 p.216）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p038.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p038_d_sum.png`（pnggray）。
- 核对：Démonstration de la prop. 9（I 最大指标、dim V/V_i majoration）、(4.9.5) b(ρ) ⩽ N/g₀(g₁+⋯+g_I) ⩽ N/g₀(I + Σ_{i⩾1}(g_i−1))、[38] p. 79 exerc. 3 句、(4.9.6) I ⩽ g₀e_K/(p−1)、stricte 句、d = Σ(g_i−1) 定义（différente、[38] p. 72、Hensel [38] p. 67）、d ⩽ g₀ − 1 + g₀e_K c、(4.9.7) Σ_{i⩾1}(g_i−1) ⩽ g₀e_K c、En combinant 段、Remarque（abélien d'exposant p^h、b(ρ) ⩽ Ne_K(h + 1/(p−1))、h ⩽ c）、Application à (4.8.8)（(a) p=3/N=2/e_K=1/c⩽1/n(ρ)⩽5/conducteur 3⁵；(b) p=2/N=2/e_K=1/c⩽3/G₁ non cyclique si c=3/n(ρ)⩽9/même n(ρ)⩽8/conducteur 2⁸）。
- 结果：PASS。公式、不等式、界（⩽ 9/5/2）、引用页码全部与印刷吻合。
- 印刷原文 quirk：d 的定义式印刷为 Σ_{i⩾0}(g_i − 1)（300 dpi 裁片确认下标含等号；数学上 différente 的 valuation 应为 i>0，疑原文笔误），print 原文优先，Markdown 同作 i ⩾ 0 忠实保留。
- 备注：150 dpi 阶段 “i>0” 判读经裁片排除；“3⁵”/“2⁸” Unicode 上标渲染等效，排版级；页眉 “216 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “…courbes elliptiques de conducteur 2⁸.”，§5 开头属印刷 p.217。

## p.039（PDF p.39 / 印刷 p.217）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p039.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p039_s3_title.png`（pnggray）。
- 核对：§5 开头（J-F. Mestre、p = 2/3/7 与 n°s 5.1-5.5 列表）、5.1 标题（GL₂(F₂) ≃ 𝔖₃）、K^gal/Gal(K^gal/Q) 段、ρ^K: G_Q → GL₂(F₂) 式、(N, k, ε) 判定段（D = ±2^m N、m = 0, 2 où 3、conducteur N、ε = 1、k = 2 (resp. 4)）、(3.2.4?) 预测段（F₂/F₄、(N, k, 1)）、A₃/U₂ 数值表（−23/2/23、−31/2/31、−44/2/11、−59/2/59、−76/2/19、−104/4/13、148/2/37、229/2/229、257/2/257、316/2/79）、(D = −23, −31, 257) 括注（F₄ − F₂、(3.2.6?)）。
- 结果：FAIL。两处已依原图修复：① 正文 “le groupe symétrique 𝔖₃” 在 Markdown 写成普通斜体 $S_{3}$（300 dpi 裁片确认 Fraktur 花体，与 5.1 标题同字形），修为 $\mathfrak{S}_{3}$；② “La conjecture (3.2.4.)” 丢下标 ?，印刷为 (3.2.4_?)，修为 “(3.2.4?)”。其余文字与表格逐格吻合。
- 备注：Markdown 表格为 markdown table 格式，表头 “D<0” 以 HTML 转义呈现，渲染正常，排版级；5.1 标题同构符号与全文 \simeq 字形一致，不改；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 217” 未收入 Markdown，排版级。印刷页止于 “…appartiennent à F₂.)”，PROPOSITION 10 段属印刷 p.218。

## p.040（PDF p.40 / 印刷 p.218）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p040.png`（pngmono，150 dpi）。
- 核对：Dans le cas général 句（(3.2.4?)）、PROPOSITION 10、(3.2.3?) 括注、Démonstration（𝔖₃ → GL₂(Z)、ρ₀^K: G_Q → GL₂(C)、ε_D: G_Q → 𝔖₃ →^{sgn} {±1}、Q(√D)）、情形 (i)（ε_D impair、𝔖₃ diédral、[11],[45]、F₁ poids 1 niveau |D|、thêta、E_D Eisenstein、F = F₁·E_D、f = F̃₁、Ẽ_D = 1、(2^m N, 2, 1)）、k′ 括注（m = 0、D = −N、k′ = 2）、情形 (ii)（ψ d'ordre 3、α auxiliaire、(ii₁)/(ii₂)/(ii₃)）、L'existence 括注、ρ₀′ = Ind(ψα) 句首。
- 结果：FAIL。一处已依原图修复：Markdown 在 “D'après (ii₁), sa” 处把下标写成错误转义 “(ii$\_{1}$)”（渲染为字面反斜杠），修为 “(ii$_{1}$)”。其余文字与公式逐项吻合。
- 备注：印刷 “f = F̃₁” 的 tilde 与 Markdown \tilde{F}_1 一致；(ii₁)/(ii₂)/(ii₃) 列表下标其余处正常，仅此引用处转义损坏；页眉 “218 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “D'après (ii₁), sa”，réduction 段属印刷 p.219。

## p.041（PDF p.41 / 印刷 p.219）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p041.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p041_indpsi.png`（pnggray）。
- 核对：réduction en caractéristique 2 段（Ind(ψ) ≃ ρ^K、(ii₂)/(ii₃)、2^M N、F′ poids 1、thêta indéfinies 括注）、Remarque（ρ_p: G_Q → GL₂(F̄ₚ), p ≠ 2、PGL₂(F̄ₚ)、diédral、(3.2.3?)）、5.2 节标题（SL₂(F₄) ≃ 𝔄₅）、𝔄₅/SL₂(F₄) 段、ρ^K: G_Q → GL₂(F₄) 式、det ρ^K = 1、“méthode des graphes” ([30],[31]) 句、D 定义句、数值表（−2083/2083、−2707/2707、−3203/3203、−3547/3547、−4027/4027、2³887/887、8311/8311、2²8447/8447、13613/13613、2²24077/24077）、Buhler [7] p. 136-141 与 [31] n° 4.2 句、Remarques (1) 句首（F₄/F₁₆、U₂, T₃, T₅）。
- 结果：FAIL。两处已依原图修复：正文 “le groupe alterné 𝔄₅. Comme 𝔄₅ est isomorphe…” 在 Markdown 两处写成普通斜体 $A_{5}$（与 5.2 标题的 \mathfrak{A}_5 体例不一；同 p.039 𝔖₃ 类问题），修为 $\mathfrak{A}_{5}$。其余文字与表格逐格吻合。
- 备注：印刷 “Ind(ψ) ≃ ρ^K” 的连接号经 300 dpi 裁片确认为 ≃，Markdown \simeq 一致（150 dpi “=” 判读排除）；表格 markdown 格式逐格一致；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 219” 未收入 Markdown，排版级。印刷页止于 “…que la représenta-”，Remarques (1) 余部属印刷 p.220。

## p.042（PDF p.42 / 印刷 p.220）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p042.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p042_tet_glyph.png`（pnggray）。
- 核对：Remarques (1) 余部（ρ_f ≃ ρ^K、travail considérable）、(2)（𝔄₅ 中心扩张、PGL₂(C)、Tate [45] §6、Artin conjecture、F poids 1、ρ_f ≃ ρ^K、(3.2.3?)）、D > 0 句、5.3 节标题与正文（PGL₂(F₃)/P₁(F₃)、{±1} noyau、extension centrale degré 2、[46] n° 1.5、GL₂(Z[√−2]) plongement、ρ: G_Q → GL₂(F₃)、ρ₀: G_Q → GL₂(Z[√−2]) ⊂ GL₂(C)、Langlands [26]/Tunnell [53]、3^m N₀、N₀ premier à 3）、PROPOSITION 11、ε 括注、(3.2.3?)、Remarque（N = ∏_{l≠3} l^{n(l)}、N₀ = ∏_{l≠3} l^{n₀(l)}）。
- 结果：FAIL。六处已依原图修复：5.3 节群记号印刷为 fraktur 𝔗̃₄（300 dpi 裁片确认花体 T 带 tilde，标题与正文各处均带 tilde），Markdown 全部写成 fraktur S 系（\tilde{\mathfrak{S}}_{4}/\mathfrak{S}_{4}/\widetilde{\mathfrak{S}}_{4}），已统一修为 \tilde{\mathfrak{T}}_{4}/\widetilde{\mathfrak{T}}_{4}。其余文字与公式逐项吻合。
- 备注：Remarques (2) 的 \mathfrak{A}_5 与印刷一致；同构号均为 ≃ 与全文一致；页眉 “220 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “…l^{n₀(l)},” 式，(5.3.1) 属印刷 p.221。

## p.043（PDF p.43 / 印刷 p.221）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p043.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p043_121B.png`（pnggray）。
- 核对：(5.3.1)（ρ(G_Q) ≃ ρ₀(G_Q) 惯性、n(l) = 1、n₀(l) = 2）、(5.3.2)、N divise N₀ 段与 (3.2.4?) 引用、Exemples tirés de courbes elliptiques 段（c₃/c₆、Néron、IV/IV* Kodaira、[41] n° 5.6、Φ_l）、ρ^E: G_Q → GL₂(F₃) 式、Exemple (5.3.3)（y² + xy = x³ + x² − 2x − 7、N₀ = 11²、N = 11、E′ y² + y = x³ − x²）、a_l ≡ a′_l (mod 3) 式、a_l/a′_l 数值表（l < 50，13 列逐格）。
- 结果：FAIL。一处已依原图修复：“La conjecture (3.2.4.)” 丢下标 ?，印刷为 (3.2.4_?)，修为 “(3.2.4?)”。其余文字、公式与表格逐格吻合。
- 备注：Exemple (5.3.3) 曲线标签印刷为 121_F（300 dpi 裁片确认斜体 F），Markdown $121_{F}$ 一致——150 dpi “121_B” 判读排除；“IV\*” 转义渲染为 IV*，排版级；“3, 1 1”/“1 17–119” 数字空格排版级；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 221” 未收入 Markdown，排版级。印刷页止于 a′_l 表行，Exemple (5.3.4) 属印刷 p.222。

## p.044（PDF p.44 / 印刷 p.222）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p044.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p044_54_glyph.png`（pnggray）。
- 核对：Exemple (5.3.4)（147_I、y² + y = x³ + x² − 114x + 473、147 = 3.7²、type multiplicatif en 3、c₆ en 7、N₀ = 7²、N = 7、très ramifiée en 3、k = 4）、F = q + Σ_{n⩾2}Aₙqⁿ 展开式（q − q² − 2q³ − 7q⁴ + 16q⁵ + 2q⁶ − 7q⁷ + 15q⁸ + …）、calcul 括注、a_l ≡ A_l (mod 3) 式、a_l/A_l 数值表（l < 50，13 列逐格）、Calcul de F 段（Q(√−7)、f₁ = Σ q^{zz̄}、f₂ = (1/2)Σ z²q^{zz̄}、poids 1 et 3、Legendre mod 7）、5.4 节标题（SL₂(F₉) ≅ 𝔄̃₆）、G = {±1, ±i}·SL₂(F₉) 式、F₉* 句。
- 结果：FAIL。一处已依原图修复：5.4 节标题印刷为 SL₂(F₉) ≅ 𝔄̃₆（300 dpi 裁片确认 fraktur A 带 tilde），Markdown 写成无 tilde 的 \mathfrak{A}_{6}，修为 \tilde{\mathfrak{A}}_{6}。其余文字、公式与表格逐格吻合。
- 备注：147_I 下标与印刷一致（罗马 I）；表格 markdown 格式逐格一致；页眉 “222 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 “…dans PGL₂(F₉)”，PSL₂(F₉)/A₆ 段属印刷 p.223。

## p.045（PDF p.45 / 印刷 p.223）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p045.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p045_A6_lines.png`（pnggray）。
- 核对：PSL₂(F₉)/𝔄₆ 段、projection φ: G → 𝔄₆、(φ, det) 同态句、(*) 正合列 {1} → {±1} → G → 𝔄₆ × {±1} → {1}、Donnons-nous 段（Gal(K^gal/Q) ≅ 𝔄₆、Q(√D)）、α^K/ε_D 与 α 式、Cherchons à relever 段、obs(α) ∈ H²(G_Q, {±1}) ≅ Br₂(Q)、[46] n° 1.1、LEMME 6（Witt invariant、Tr_{K/Q}(x²)）、(5.4.1) obs(α) = w + (−1)(D)、quaternions 括注、th. 1 de [46] 段（α^K: G_Q → 𝔄₆ ≃ PSL₂(F₉)、G_Q → 𝔄̃₆ ≃ SL₂(F₉)）、ε_D/{±1, ±i} 式、Le lemme résulte 句。
- 结果：FAIL。三处已依原图修复：正文 “groupe alterné 𝔄₆”、“projection φ: G → 𝔄₆”、“G → 𝔄₆ × {±1}” 在 Markdown 均写成普通斜体 $A_{6}$（同页 (*) 式与 α^K 式的 \mathfrak{A}_6 体例正确），统一修为 $\mathfrak{A}_{6}$。其余逐项吻合。
- 备注：α^K 式与 𝔄̃₆ 式的连接号经 300 dpi 裁片确认均为 ≃，Markdown \simeq 一致；两式 Fraktur 记号一致；页眉 “SUR LES REPRÉSENTATIONS MODULAIRES… / 223” 未收入 Markdown，排版级。印刷页止于 “…par un argument facile.”，“Fixons maintenant…” 段属印刷 p.224。

## p.046（PDF p.46 / 印刷 p.224）

- actor=Wf-P43; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run 级配置，自报 UNKNOWN）；签认时间：2026-10-02 14:22 EDT。
- PNG：`audit/serre1987_p046.png`（pngmono，150 dpi）；300 dpi 仲裁裁片：`audit/300dpi/serre1987_p046_l3N.png`（pnggray）。
- 核对：Fixons 段（D = −3、K corps sextique、X⁶ + aX + b = 0、𝔄₆）、Mestre 七组 (a,b) 列表、[46] n° 3.3 段（w = (3)(−d) + (−1)(−1)、d discriminant、d est un carré、w = (3)(−1) + (−1)(−1) = (−1)(−3)）、obs(α) = 0、ρ: G_Q → G ⊂ GL₂(F₉)、torsion quadratique 段（[45] §6、k = 2 ou 4、l = 2 et 5）、f = Σaₙqⁿ/(N,k,1)/F₉/ρ ≃ ρ_f、ord(l) 定义句、四情形判据（ord = 1 ou 3 ⇔ a_l² = (l/3)；= 2 ⇔ a_l = 0；= 4 ⇔ a_l² = −(l/3)；= 5 ⇔ a_l⁴ = −1）、F₉ 括注。
- 结果：FAIL。两处已依原图修复：① “de groupe de Galois 𝔄₆” 在 Markdown 写成普通斜体 $A_{6}$（同段 Gal(K^gal/Q) ≅ \mathfrak{A}_6 体例正确），修为 $\mathfrak{A}_{6}$；② “(pour l ∤ 3N)” 在 Markdown 写成 “l + 3N”（300 dpi 裁片确认 + 样不整除符，同前已登记字形），修为 l \nmid 3N。其余文字与公式逐项吻合。
- 备注：Legendre 符号 (l/3) 与 ⇔ 记号一致；Mestre 列表七组数对逐项核对无误；页眉 “224 / JEAN-PIERRE SERRE” 未收入 Markdown，排版级。印刷页止于 F₉ 括注，“En particulier, si l ≠ 3…” 段属印刷 p.225。
