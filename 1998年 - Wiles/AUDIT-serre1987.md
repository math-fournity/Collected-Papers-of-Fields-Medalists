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
