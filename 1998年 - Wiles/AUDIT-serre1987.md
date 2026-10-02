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
