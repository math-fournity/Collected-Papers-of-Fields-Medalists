# 重做逐页审计：Zur Theorie der Überlagerungsflächen（Lars Ahlfors，1930）— redo

## 任务与来源

- 性质=Luna审计重做（用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核）。
- actor=Wf-R-P02；host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）。
- 开工时间：2026-10-02 14:29 EDT（`date` 实取）。
- worktree：`/Users/aurolafly/.zcode/worktrees/cpf-redo-Ahlfors_1930_ueberlagerungsflaechen`（分支 `cpf-redo/Ahlfors_1930_ueberlagerungsflaechen`）；主 checkout 只读禁触。
- PDF：`1936年 - Ahlfors/Ahlfors_1930_ueberlagerungsflaechen.pdf`；`pdfinfo` 实测 Pages: 38；SHA-256 `46674f287f4b9a085ccea11f10dfa22f168cf84d6e69e5cdac27b9945f5ddb28`（开工实测，与任务书一致）。
- 被检 Markdown：`1936年 - Ahlfors/Ahlfors_1930_ueberlagerungsflaechen_mineru/Ahlfors_1930_ueberlagerungsflaechen__Ahlfors_1930_ueberlagerungsflaechen.md`；重做起点基线 SHA-256 `6659c161768323e7bbfca17ce5bfe4e1e5516e97837b8a73c410f0af681b75f4`（= Luna 修复后快照；其全部修复作为被检对象一并按原页重核）。
- 裁决源：印刷原文（PNG 页图）。旧审计 `AUDIT-Ahlfors_1930_ueberlagerungsflaechen.md`（actor=Peer-P02，gpt-6-luna）只作被检对象与交叉参照，不作依据。
- 文本层判定（2026-10-02，`pdftotext -f 1 -l 1` 首页实测）：文本层存在且可提取，但为低质量 OCR（Ö→0、ä→~、von→yon、NEVANLINNA 打碎为 BTEVA~LIN~A 等）。判定：**文本层可用（低质量），采用双通道主对账**——pdftotext 仅用于定位与粗交叉核对，一切字形/内容判定以 150dpi pngmono 页图为准，疑点升 300dpi 裁片仲裁。
- 证据图：`1936年 - Ahlfors/audit-redo/ueberlagerungsflaechen_pNNN.png`（pngmono 150dpi；带本篇短名前缀，避免与同目录另一篇 Ahlfors ICM 论文的图片命名空间冲突；旧 `audit/` 目录不动）。
- 边界：本次只写本篇路径（`audit-redo/` 图、本 redo AUDIT、被检 Markdown）；不写根级任何文件（SOP 的根 `AUDIT-PROGRESS.log` 进度行由每页 redo commit 的时间线代替），不动旧 `audit/`、旧 AUDIT 文件与其他论文目录，不 push。
- 分级沿用 `AUDIT-SOP.md`：PASS / PASS± / FAIL。Markdown 修复一律用结构化 Edit 逐处完成，每处可溯源该页证据；印刷原文的错字与 print quirk 忠实保留、只登记不改正。

## 逐页记录

### p.001（PDF p.1 / 印刷页码未见）

- audited_at=2026-10-02 14:45 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p001.png`（pngmono 150dpi）。
- 核对：题录（题名 ZUR THEORIE DER ÜBERLAGERUNGSFLÄCHEN. / VON / LARS AHLFORS / in HELSINGFORS.）、节标题 Einleitung.、引言前三段逐词（含 „Teil vom analytischen Charakter der Abbildung abhängen“、„als Überlagerungsfläche einer geschlossenen Grundfläche.“、„…anzusehen sind.“）、页末断句 „als Erweiterung“（MD 行 15 同点断开，续句在次页，顺序衔接正确）。
- 与 Luna 旧记录交叉：旧 p.001 判 PASS；本次独立按页图重核，同样未见差异，旧判维持。
- 结果：PASS。

### p.002（PDF p.2 / 印刷 p.158）

- audited_at=2026-10-02 14:55 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p002.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p002_kerekjarto_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p002_gebietes_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p002_gebiets_zoom8x.png`。
- 核对：页眉（158 / Lars Ahlfors.）、Einleitung 末句续文（HURWITZ-RIEMANNschen Relation…endgültige Erklärung.）、节标题顺序（I. Endliche Überlagerungsflächen. → § 1. Die Metrik der Grundfläche.）、定义段 1（geschlossen/berandet 判据）、Metrik 定义段（1°/2° 性质、ε、P）、W₀/U_P/I<kL 记号、脚注 1（Kérékjártó: Vorl. über Topologie, S. 131—163）。
- 发现并修复（MD 结构化 Edit，各 1 处，同块完成）：
  1. 脚注人名 `KERÉKJÁRTÓ` → `KÉRÉKJÁRTÓ`——300dpi 裁片显示首 É 带尖音符（印刷小体大写 KÉRÉKJÁRTÓ）。
  2. 删除游离重复脚注碎片块「131-163」（半角连字符）——印刷该页仅一条脚注，页码范围已完整含于正式脚注「S. 131—163.」，该碎片为 mineru 重复伪影，非印刷内容。
- 仲裁否决（登记不改）：150dpi 初读疑「Gebiets」应为「Gebietes」，300dpi 单词 4x 放大（`…p002_gebiets_zoom8x.png`）确证印刷即为 **Gebiets,**，MD 原文正确，不动。
- 保留登记（PASS± 排版级，不修）：印刷定义术语 geschlossen/berandet/Metrik 及书名 Vorl. über Topologie 为斜体，MD 全篇统一丢失斜体（mineru 系统性伪影，按 SOP 默认不逐处改）。
- 与 Luna 旧记录交叉：旧 p.002 判 PASS±（列 distance/300dpi 局部核对、游离片段类伪影）；本次重核另发现人名缺音与游离碎片两项内容级问题并已修复，其余吻合。
- 结果：PASS±（两处内容级修复后与印刷一致；斜体缺失登记保留）。

### p.003（PDF p.3 / 印刷 p.159）

- audited_at=2026-10-02 15:05 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p003.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p003_hilfssatz_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p003_nu_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p003_nu_zoom8x.png`。
- 核对：页眉（Zur Theorie der Überlagerungsflächen. / 159）、Regularitätsbedingung 段（δ、δ/2、U_P、U′_P、d、L<d、I<kL）、编号段 2 与 Hilfssatz 1 陈述、公式 (1) `Min(I′,I″)≦kL`（含 \tag{1}）、证明两段（Σ I^{(ν)} < kΣL^{(ν)} = kL、k=I₀/2d、Min(I′,I″)≦I₀/2）、编号段 3 起始、页末断句「von der Länge L」、脚注 1（k 或 k′ 为常数但不必相同）。
- 发现并修复（MD 结构化 Edit，2 处）：
  1. 上标曲线索引 `(v)` → `(\nu)`（一行内 6 个字形：L^{(ν)}、I^{(ν)}<kL^{(ν)}、ΣI^{(ν)}<kΣL^{(ν)}=kL）。依据：印刷字形为斜体，v/ν 在该字体下几乎同形（8x 放大 `…p003_nu_zoom8x.png` 不能单凭字形判别；OCR 文本层此处为 `L(')`，无旁证），但 MD 其余 7 行（γ_ν、Δ_ν、a_ν 等）对同一印刷字形均转写 `\nu`，本行是唯一 `v` 转写——按转写一致性统一为 `\nu` 并在此留痕，非按数学预期静默改正。
  2. 删除游离脚注碎片块 `$k^{\prime}$`——印刷正文与脚注均无独立 k′ 块，该碎片为脚注中「k 或 k′」的 mineru 重复伪影。
- 仲裁否决（登记不改）：①150dpi 疑 Hilfssatz 1 中「geschlossenen」；300dpi 裁片确证印刷即为 **geschlossene**，MD 正确。②旧审计修复表 p.3 行「两处 ∂/2 误识为 δ/2」措辞方向写反——`git show abde327` 实际 diff 为 mineru 的 `\partial/2` 被改回印刷的 `\delta/2`（修复内容正确，仅表格描述颠倒；登记为旧审计记录瑕疵，不改旧文件）。
- 保留登记（PASS± 排版级，不修）：Hilfssatz 1 陈述整段印刷为斜体，MD 丢失斜体（系统性伪影）；公式 (1) 印刷关系号 ≦ 转写为 \leq，等价。
- 与 Luna 旧记录交叉：旧 p.3 修复（δ/2、S(Δ)、数字 1、重复负号）经本次原页重核均与印刷一致；本次新发现并修复上标索引与游离碎片两项。
- 结果：PASS±（两处内容级修复后与印刷一致）。

### p.004（PDF p.4 / 印刷 p.160）

- audited_at=2026-10-02 15:15 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p004.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p004_formel_300dpi.png`。
- 核对：页眉（160 / Lars Ahlfors.）、页首续句（gezogen.…λ<k′L…U_P abhängt.）、Hilfssatz 2 陈述与公式 `Min(λ′,λ″)≦k′L,`、beweis 一句、编号段 4（Verdoppelung、relativ zu W₀ geschlossen）、Randkurve C 段、页末 formuliert 结果（…der Bedingung / Min(λ′,λ″)≦k′L / genügen.）。
- 发现并修复（MD 结构化 Edit，1 处）：**公式错位**——印刷顺序「…deren Längen λ′ und λ″ der Bedingung / [公式 Min(λ′,λ″)≦k′L] / genügen.」，MD 原把整段 display 公式放在「genügen.」之后（原行 73→75→77-79），已按印刷顺序移回 Bedingung 与 genügen. 之间。
- 看不清登记（不改）：页末公式 k′L 之后有一极淡的低位小点，300dpi 裁片不能判定为句号还是印刷污点（glyph 类别 UNKNOWN）；MD 现无句号，维持原状，待后续更高分辨率仲裁。
- 保留登记（PASS± 排版级，不修）：Hilfssatz 2 陈述、relativ zu、页末结果整段及 Randkurve C 的斜体在 MD 中系统性丢失。
- 与 Luna 旧记录交叉：Luna 修复表无 p.4 行，本页公式错位系旧审计遗留未检出的结构缺陷，本次修复。
- 结果：PASS±（公式语序修复后与印刷一致；斜体缺失与公式末存疑小点登记保留）。

### p.005（PDF p.5 / 印刷 p.161）

- audited_at=2026-10-02 15:22 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p005.png`（pngmono 150dpi）；本页无需 300dpi 仲裁。
- 核对：页眉（Zur Theorie der Überlagerungsflächen. / 161）、节标题 § 2. Metrische Eigenschaften der Überlagerungsfläche.、编号段 5 及 Spurdreieck 对应公设、D₀^(1)/D₀^(2)/D^(1)/D^(2) 全部上下标、Spurpunkt 段（P₀ über P₀）、Der relative Rand 段、Verzweigungspunkt 段（h>1、Vielfachheit、h−1 Verzweigungsordnung）、Metrik 转移段、页底 imprint 行（21—34686. Acta mathematica. 65. Imprimé le 8 février 1935.）。
- 结果：PASS±。内容逐词与印刷一致，无修复项。保留登记（排版级，不修）：印刷斜体术语 Der relative Rand / relativ unberandet / unbegrenzt 及刊名 Acta mathematica 在 MD 中丢失（系统性）；imprint 行「21—34686」长划转写为半角连字符「21-34686」；「h − 1」转写为带连字符的纯文本「h - 1」（语义等价）。
- 与 Luna 旧记录交叉：旧 p.5 未列入修复表；本次重核与旧判（PASS± 类排版伪影）精神一致，未发现旧修复错误。
- 备注：imprint 行证实本篇刊于 Acta Mathematica 65（Imprimé le 8 février 1935）；文件名年份 1930 与印刷年不符属篇目命名既有事实，不属于本页 Markdown 审计范围，仅登记。

### p.006（PDF p.6 / 印刷 p.162）

- audited_at=2026-10-02 15:30 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p006.png`（pngmono 150dpi）；本页无需 300dpi 仲裁。
- 核对：页眉（162 / Lars Ahlfors.）、编号段 6（Blätterfolge W₁,W₂,…,Wₙ,…、das n:te Blatt、maximale Blätteranzahl N）、äquivalent 段（P₀、n₀、Iₙ）、公式 (2) `I=I₁+I₂+⋯+I_N.`（\tag{2}，句点在）、relativer Rand der Blätter 段（n₀ Kanten）、无号公式 `L=L₁+L₂+⋯+L_N,`（逗号在）、「wobei die Länge einer doppelten Kante zweifach zu zählen ist.」、编号段 7（mittlere Blätteranzahl S、Nach (2) gilt）、公式 `S=S₁+S₂+⋯+S_N,`、「wo Sₙ die mittlere Blätteranzahl von Wₙ ist.」。
- 结果：PASS±。内容、公式与编号逐项与印刷一致，无修复项。保留登记（排版级，不修）：印刷斜体 das n:te Blatt / mittlere Blätteranzahl 丢失（系统性）。
- 与 Luna 旧记录交叉：Luna 修复表无 p.6 行；本次独立重核未发现内容差异，旧状态维持。
- 页界：本页印刷内容止于「…von $W_{n}$ ist.」，MD 行 119 吻合；下一行（Betrachten wir ein Teilgebiet Δ…）属 p.007，待次页核。

### p.007（PDF p.7 / 印刷 p.163）

- audited_at=2026-10-02 15:40 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p007.png`（pngmono 150dpi）；本页五点比对无需新增 300dpi 仲裁（S(Δ)/δ 记号沿用 Luna 已修复并与原页图直接吻合）。
- 核对：页眉（Zur Theorie der Überlagerungsflächen. / 163）、Teilgebiet Δ 段（S(Δ)、Inhalt δ）、公式 `S(Δ)=S₁(Δ)+⋯+S_N(Δ)`（无标点）、「und folglich」、`S−S(Δ)=Σ₁^N(Sₙ−Sₙ(Δ)).`（句点在）、Abschätzung 段、`Sₙ(Δ)≦I₀/δ Sₙ.`、Komplementärmenge 段、`1−Sₙ(Δ)≦I₀/δ(1−Sₙ).`、「Man hat nun einerseits」、`|Sₙ−Sₙ(Δ)|≦Max(Sₙ,Sₙ(Δ))≦I₀/δ Sₙ`（无标点）、「und andererseits」、`|Sₙ−Sₙ(Δ)|=|(1−Sₙ)−(1−Sₙ(Δ))|≦Max(1−Sₙ,1−Sₙ(Δ))≦I₀/δ(1−Sₙ).`（句点在）、「Diese Ungleichungen…」、`|Sₙ−Sₙ(Δ)|≦I₀/δ Min(Sₙ,1−Sₙ)`（无标点）、zusammenfassen 段、`|Sₙ−Sₙ(Δ)|≦k/δ Lₙ,`（逗号在）。
- 发现并修复（MD 结构化 Edit，1 处）：行内 `$\varDelta$` → `$\Delta$`（「des in Δ gelegenen Teils」）——印刷全篇同一 Δ 字形，mineru 转写混用 `\Delta`/`\varDelta`，本页为 p.1–9 内唯一 `\varDelta`，按同字形同转写统一。
- 移交登记（超出本段页范围，不改）：MD 行 603 另有一处 `\varDelta`（`p(\varDelta_{v})`，属后续页），且其下标 `v` 与本篇 ν 转写问题同类，留待该页重检处理。
- 与 Luna 旧记录交叉：旧修复表 p.7 行（还原 S(Δ)/Sₙ(Δ)、三个数字 1、删除绝对值式重复负号）经原页重核全部与印刷一致，`git show abde327` 的对应 diff 亦确认；本次新发现并修复 `\varDelta` 混写一处。
- 结果：PASS±（记号统一修复后与印刷一致）。

### p.008（PDF p.8 / 印刷 p.164）

- audited_at=2026-10-02 15:55 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p008.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p008_tag_zoom3x.png`、`audit-redo/ueberlagerungsflaechen_p008_L0_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p008_lambda0_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p008_l0_first_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p008_l0_zoom2x.png`。
- 核对：页眉（164 / Lars Ahlfors.）、「woraus durch Addition」+ 公式 `|S−S(Δ)|≦k/δ Σ₁^N Lₙ = k/δ L.`（句点在）、Überdeckungssatz 1 引言句与整段陈述、公式 (I. 1) `|S−S(Δ)|≦kL`、Das Wesentliche 段（k 只依赖 W₀ 与 Δ；Ist L=0 句）、编号段 8（λ₀、s(γ) 定义）、Zerlegung 公式 `s(γ)=s₁(γ)+⋯+s_N(γ).`（句点在）、γ′ Teilbogen 段、`|s(γ)−s(γ′)|≦k′/λ′ L,`（逗号在）、「wo λ′ die Länge von γ′ bedeutet…aufgefasst werden.」。
- 发现并修复（MD 结构化 Edit，1 处）：公式编号 `\tag{I. I}` → `\tag{I. 1}`——3x 裁片显示编号括号内第二字形为短杆带旗头的旧式数字 **1**（首字形为高衬线罗马 I），印刷为 **(I. 1)**；编号制度=章号（罗马）+公式号（阿拉伯），与 Luna 旧表 p.20 还原的 (II. 2′) 同制。
- 仲裁否决（登记不改）：①「Ist L = 0」印刷字形为小圆 o 形，旧式数字 0 与字母 o 在本字体同形不可辨（`…p008_L0_300dpi.png`）；按语义（相对边界长为零⇒Blätteranzahl 常值）与 Luna 全篇同类字形读 0 的先例维持 MD 的 0，登记同形异写。②行 185 两处 `$\lambda_{0}$`：低分辨率初读第二处疑为 l₀，2x 宽幅裁片确证两处字形相同、均为 **λ₀**，MD 正确。
- 保留登记（PASS± 排版级，不修）：Überdeckungssatz 1 陈述整段与 Überdeckungssatzes 斜体丢失（系统性）。
- 与 Luna 旧记录交叉：旧修复表 p.8 行（两处 S(𝒜)→S(Δ)）经原页重核与印刷一致；公式编号 (I. 1) 的 I/1 混写系旧审计未检出项，本次修复。
- 结果：PASS±（编号修复后与印刷一致）。

### p.009（PDF p.9 / 印刷 p.165）

- audited_at=2026-10-02 16:05 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p009.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p009_formel1_300dpi.png`。
- 核对：页眉（Zur Theorie der Überlagerungsflächen. / 165）、Wir wollen noch zeigen 段（Δ = kleinere Teilgebiet）、Hilfssatz-Anwendung 段与公式 `Sₙ(Δ)≦k/δ(λ₀sₙ(γ)+Lₙ).`、Ebenso 段与 `1−Sₙ(Δ)≦k/δ(λ₀(1−sₙ(γ))+Lₙ).`、δ≦kλ₀ 段与两条 Max 估计（前者无标点、后者句点）、zweiter Hilfssatz 段与 `…≦k/δ(λ₀k′+1)Lₙ=\bar{k}Lₙ.`、Durch Addition 段 + 旁注「und mit Hilfe von (I. 1)」+ 双式 `|S(Δ)−s(γ)|≦\bar{k}L,` / `|S−s(γ)|≦(k+\bar{k})L.`、Die neue Konstante 段、Überdeckungssatz 2 陈述与公式 `\tag{I. 2}`、末段（Teilbogen des Randes…sehr wichtig.）。
- 仲裁否决（登记不改）：150dpi 疑首式末为逗号；300dpi 裁片显示低圆点无下伸尾，为**句点**，MD 的「.」正确。
- 保留登记（PASS± 排版级，不修）：①旁注「und mit Hilfe von (I. 1)」在印刷中位于第二式左侧，MD 置为独立段落置于双式 array 之前——阅读顺序仍通顺，内容无缺，不重构；②Überdeckungssatz 2 陈述整段斜体丢失（系统性）。
- 加分核验：本页多处印刷新常数记号 **k̄**（k 上划线）在 MD 中均正确保留为 `\bar{k}`；旁注 (I. 1) 与 Überdeckungssatz 2 的 (I. 2) 编号交叉印证 p.008 的 `\tag{I. 1}` 修复方向正确。
- 与 Luna 旧记录交叉：旧修复表 p.9 行（还原 S(Δ)/Sₙ(Δ) 与五个数字 1）经原页重核与印刷一致（本页 1 的字形为旧式数字，均转写正确）。
- 结果：PASS±（无内容修复项；旁注位置与斜体缺失登记保留）。
- 页界：本页印刷止于「…sehr wichtig.」（MD 行 247 吻合）；「## § 3. Die Charakteristik.」起为 p.010 内容。

## p.001–p.009 段内复核与移交登记（Wf-R-P02）

- 复核范围声明：本次 redo 只覆盖 p.001–p.009；以下「移交登记」来自修复后的整份 Markdown 全文复读（1,103 行全部过目），只登记、不改动——均属 p.010–p.038 的重检范围，留给后续页的重审员按原页仲裁。
- 公式编号类（与本次 `\tag{I. I}`→`\tag{I. 1}` 同类，需按原页核对正文引用）：
  - MD 行 319：正文引用「(II. I)」「(I. I)」——字母 I 疑应为数字 1（位于 §4，约 PDF p.17–18）。
- 希腊字母转写类（与本次 `(v)`→`(\nu)` 同类）：
  - 行 390 `s(\gamma_{v})`；行 603 `p(\varDelta_{v})`（兼 `\varDelta` 混写）；行 725 `p(a_{v})`；行 901 `p(r,\Delta_{v})`；行 907、929、1065、1071、1077 各处 `a_{v}`/`a_v` 下标——逐一按原页核对 v/ν。
- 游离/错位片段类（与本次删除的两处同型，需按原页仲裁后处置）：
  - 行 458、460：游离 `$\Omega^{\prime}$`、`$\sigma^{\prime}$` 块（在真实脚注前）；
  - 行 910–916：四个游离块 `$W_{r}$`×2、`$|z|<r$`、`$|z|=r$`（在 p.33 脚注 1 前）；
  - 行 1008：游离 `$a=f(0)$` 块（紧邻真实脚注 ¹，脚注内为 `a=f(o)`——o/0 同形问题再现，需仲裁）；
  - 行 548：imprint 行「23–34686. Acta mathematica…」**嵌入段内词中**（「betref-23–34686」），页界合并伪影；
  - 行 1012：运行页眉「Zur Theorie der Überlagerungsflächen.」游离为独立行。
- 编号重复：行 968 与 970 两段均编号「28.」——与 Luna 旧总评所述 p.35–36 重复印刷编号 28 一致，属 print quirk 候选，按原页忠实核验后保留或登记。
- 文末结构：MD 止于行 1103（正文末句「…in wichtiger Weise komplettiert.」），**未含参考文献表与收稿日期**；PDF p.36–38 是否有 Literatur/Zusammenfassung 及其是否被 mineru 整体遗漏，必须由后续页重检对照原页定论（SOP 文末页五点含参考文献逐条与收稿日期）。
- 本段（p.001–p.009）修复后的 MD 终态 SHA-256：`b4e48563b5e3233c4d14fd3ca3ae2902ae48117a5f383b111a52277d4256f017`（基线 `6659c161…` + 本段 6 处结构化 Edit）。

### p.010（PDF p.10 / 印刷 p.166）

- audited_at=2026-10-02 17:45 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p010.png`（pngmono 150dpi）；本页无需 300dpi 仲裁。
- 核对：页眉（166 / Lars Ahlfors.）、节标题 § 3. Die Charakteristik.、编号段 9（E/K/P 定义、Dreiecke (Polygone)）、无号公式 `ϱ=−E+K−P,`（逗号在）、Charakteristik 定义句、Ω/σ/ϱ(Ω)/Ē/K̄ 段、公式 (3) `ϱ=Σϱ(Ω)−Ē+K̄.`（句点在、\tag{3}）、Oberteilung 段（Ē,K̄,P̄、−Ē+K̄−P̄）、Die Bedeutung 段页末断句「punktfremde Rück-」。
- print quirk 保留核验：印刷「die zur **Oberteilung** gehörigen Anzahlen」（语义应为 Unterteilung）——MD 行 265 忠实保留「Oberteilung」，不改正 ✓。
- 结果：PASS±。内容逐词与印刷一致，无修复项。保留登记（排版级，不修）：Charakteristik 斜体丢失（系统性）；页眉/印刷页码 mineru 全篇未收（系统性，旧审计已登记）。
- 与 Luna 旧记录交叉：Luna 修复表无 p.10 行；本次独立重核未见内容差异，旧状态维持。
- 页界：本页止于「…punktfremde Rück-」（断词跨页），MD 连写为「Rückkehrschnitte」并衔接 (4) 公式，顺序正确。

### p.011（PDF p.11 / 印刷 p.167）

- audited_at=2026-10-02 17:55 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p011.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p011_formel5p_300dpi.png`。
- 核对：页眉（Zur Theorie der Überlagerungsflächen. / 167）、公式 (4) `ϱ=Σϱ(Ω)+n(σ),`（逗号在、\tag{4}）、allgemeine Zerlegungsformel 句、topologische Typen 段（q−1、q−2、q′、q+2q′−2）、Geschlecht Null 段（ϱ=−2、−1）、公式 (5) `ϱ≧n(σ)−N(Ω),`（\tag{5}）、Gleichheitszeichen 句、公式 (5′) `ϱ≧n(σ)−N₁(Ω),`、N₁(Ω) 句、编号段 10 起始、Der Betrachtung 段（Eₙ,Kₙ,Pₙ、ϱₙ=−Eₙ+Kₙ−Pₙ）页末断句「Für die Teilung」。
- 发现并修复（MD 结构化 Edit，1 处）：公式编号 `\tag{(5')}` → `\tag{5'}`——印刷编号为单层括号「(5′)」，mineru 把编号括号并入 tag 内容造成双层；本篇其余编号 tag 均为单层惯例（如 `\tag{5}` 对应印刷 (5)）。
- 仲裁否决（登记不改）：150dpi 疑 (5′) 式末为句点；300dpi 裁片显示末标记带下伸尾，为**逗号**，MD 逗号正确。
- 结果：PASS±（编号修复后与印刷一致；斜体/页眉系统性伪影同前，不重复展开）。
- 与 Luna 旧记录交叉：Luna 修复表无 p.11 行；本次发现的 (5′) 双层括号系旧审计未检出项。
- 页界：本页止于「Für die Teilung」，次页续「der Fläche W gilt…」，衔接正确。

### p.012（PDF p.12 / 印刷 p.168）

- audited_at=2026-10-02 18:05 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p012.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p012_rho0_300dpi.png`。
- 核对：页眉（168 / Lars Ahlfors.）、页首续句（P=ΣPₙ、K=ΣKₙ、E≦ΣEₙ、E=ΣEₙ−w、Verzweigungszahl）、公式 (6) `ϱ=Σϱₙ+w.`（句点在、\tag{6}）、斜体定理句（Charakteristik einer Überlagerungsfläche…）、Hurwitzsche Relation 段（ϱ=Nϱ₀+w）、节标题 § 4. Der metrisch-topologische Hauptsatz.、编号段 11、引言两段、Metrisch-topologischer Hauptsatz 陈述（ϱ₀、ϱ⁺=grössere der Zahlen ϱ und 0）、公式 (II. 1) `ϱ⁺≧ϱ₀S−kL,`（逗号在、\tag{II. 1} 印刷数字 1 ✓）、wo S… 句。
- print quirk/同形登记（不改）：印刷「die grössere der Zahlen ϱ und **o**.」末字形为小圆 o 形（300dpi 裁片 `…p012_rho0_300dpi.png`），旧式数字 0 与字母 o 在本字体同形（与 p.008「L = o」同类）；MD「0」为 Luna p.12 修复结果，语义（ϱ 与 0 取大）与全篇读法支持，维持 0 并登记同形异写。
- Luna 旧修复重核：本页旧表行「点号误识还原为 ρ⁺、字母 o 改为数字 0」——$\stackrel{+}{\varrho}$ 与「0」经原页重核均与印刷判定一致，维持。
- 结果：PASS±。无内容修复项；定理句斜体丢失登记（系统性）。
- 与 Luna 旧记录交叉：旧修复内容正确；本次另核 (II. 1) 编号数字 1 正确（p.008 同类问题在本页不存在）。

### p.013（PDF p.13 / 印刷 p.169）

- audited_at=2026-10-02 18:15 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p013.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p013_formelref_300dpi.png`。
- 核对：页眉（Zur Theorie der Überlagerungsflächen. / 169）、Es soll zunächst 段（ϱ=Nϱ₀+w、ϱ≧Nϱ₀、mittlere Blätterzahl S、(II. 1) 引用、ϱ>0、(I. 1)/(I. 2) 引用、ϱ=−1、Null schreiben）、Wir bemerken 段（ϱ₀≦0）、编号段 12（q>2、ϱ₀=q−2、γ₁,…,γ_q、Δ′/Δ″）、Die Überlagerungsfläche W ist definiert 段、Die folgenden Betrachtungen 段、公式 (5) 重复 `ϱ≧n(σ)−N(Ω).`（句点在、\tag{5}）、页底 imprint 行「22—34686. Acta mathematica. 65. Imprimé le 8 février 1935.」（位置：印刷在 (5) 式下方页底，MD 行 333 同位独立行 ✓）。
- 发现并修复（MD 结构化 Edit，1 处含 2 字形）：行 319 正文公式引用「(II. I)」→「(II. 1)」、「(I. I)」→「(I. 1)」——300dpi 裁片显示两处均为旗头短杆旧式数字 **1**（段内移交项核销）；同段 (I. 2) 原本正确。
- 同形登记（不改）：印刷「ϱ > o」与「ϱ₀ ≦ o」的 o 形字符（0/o 同形，同 p.008/p.012 类）；MD 维持 0。
- 结果：PASS±（引用编号修复后与印刷一致）。
- 与 Luna 旧记录交叉：Luna 修复表无 p.13 行；本次修复的两处引用编号 I/1 系旧审计未检出项。
- 备注：本页印刷将 (5) 式原样重排一次（编号同为 (5)），MD 忠实保留重排与同号，✓。

### p.014（PDF p.14 / 印刷 p.170）

- audited_at=2026-10-02 18:25 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p014.png`（pngmono 150dpi）；本页无需 300dpi 仲裁。
- 核对：页眉（170 / Lars Ahlfors.）、Aus dieser Ungleichung 段（正文引用 (II. 1) 数字 1 ✓，MD 行 335 本就正确）、编号段 13（Gebietsklassen (Ω₁)…(Ω_p)、Querschnittsklassen (σ₁)…(σ_p)）、Zur der ersten Klasse 段（(Ω₂)/(σ₂)、(σ₁)…(σ_{n−1})）、Aus der Definition 段（斜体 Eigenschaft 陈述：Jeder Querschnitt σₙ zerlegt…）、Für n = 1 归纳段、Wenn es vorkommt 段页末断句「und auch dann」。
- 结果：PASS±。内容逐词与印刷一致，无修复项。保留登记（排版级，不修）：Eigenschaft 陈述句印刷斜体丢失（系统性）。
- 与 Luna 旧记录交叉：Luna 修复表无 p.14 行；本次独立重核未见内容差异。
- 页界：本页止于「…und auch dann」，次页续「nur für den einzigen Querschnitt der höchsten Klasse」，衔接正确。

### p.015（PDF p.15 / 印刷 p.171）

- audited_at=2026-10-02 18:35 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p015.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p015_1grad_300dpi.png`。
- 核对：页眉（Zur Theorie der Überlagerungsflächen. / 171）、页首续句（nur für den einzigen Querschnitt…umkehrbar eindeutig.）、Die übriggebliebenen Gebiete 段（**print quirk「Die Charakter eines Ausnahmefalls」忠实保留 ✓**，印刷原文如此）、编号段 14（(Ω′)/(Ω*) 分类、Jenachdem…kleiner als q oder wenigstens gleich q）、drei Klassen 段（(σ*)/(σ′)/(σ″) 对应关系）、Damit ist 段、**Ω/σ 四列对应表**（印刷两行：(Ω₁)…(Ω_p) | (Ω′) | (Ω*) 与 (σ₁)…(σ_p) | (σ′)(σ″)（上有横线相连）| (σ*)；Luna 重建的 `\begin{array}{cccc}`+`\multicolumn{2}{c}{(Ω′)}` 结构与印刷对应关系一致 ✓）、und es gilt:、条目 1°/2°/3°（ein-eindeutig 连字符 ✓、q−1、σ′ oder σ″、wenigstens q）、Die obige Einteilung 段页末断句「genügen」。
- 发现并修复（MD 结构化 Edit，1 处）：条目一编号 `$^{1}$`（上标脚注 1）→ `$1^{\circ}$`——300dpi 裁片显示印刷为「**1°** Die Ωₙ und σₙ…」（度数符号枚举），mineru 把 1° 误作上标脚注标记；2°/3° 两条格式本就正确，修复后三条一致。
- 与 Luna 旧记录交叉：旧表 p.15 行「重建 Ω/σ 四列对应表」经原页重核与印刷结构一致，维持；游离 `$^{1}$` 系旧审计未检出项。
- 结果：PASS±（1° 修复后与印刷一致；表格上方横线连接记号以 \multicolumn 分组近似表达，登记为排版级近似）。

### p.016（PDF p.16 / 印刷 p.172）

- audited_at=2026-10-02 18:45 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p016.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p016_gamma_nu_300dpi.png`。
- 核对：页眉（172 / Lars Ahlfors.）、页首续句（…auf diesen Fall nicht näher einzugehen.）、编号段 **14.（第二次）**「Wir kehren zur Ungleichung (5) zurück…」、Aufspaltung 段、公式 (7) `ϱ≧[n(σ″)+½n(σ′)−N(Ω′)]+[n(σ*)+½n(σ′)−N(Ω*)].`（句点在、\tag{7}）、Wenn man ausdrückt 段（n(σ′)+2n(σ″)≧2N(Ω′)、n(σ′)+2n(σ*)≧qN(Ω*)）、公式 (8) `ϱ≧(q−2)/q(n(σ*)+½n(σ′))≧(q−2)/q n(σ*).`（句点在、\tag{8}）、Es gilt jetzt 段（γ_ν、λ(σ)、λ*、λ′、λ″、λ_a、n(σ*)≧λ*、Σ₁^q s(γ_ν)=λ*+λ′+λ″+λ_a）、Σ₁^q s(γ_ν)≧qS−kL 行、无号公式 `ϱ≧(q−2)S−kL−(λ′+λ″+λ_a).`（句点在、印刷无编号 ✓）、Um den Beweis 段页末断词「Kon-」。
- print quirk 保留核验（不改）：①印刷第二次出现编号「**14.**」（前页已有 14.，此段逻辑上应为后续编号）——MD 行 376 忠实保留重复编号 ✓（与 Luna 总评所述 p.35–36 重复「28.」同类印刷现象）；②「der erste Klammer」（语法性 print quirk）MD 行 382 忠实保留 ✓；③「gleich der entsprechenden Summe erstreckt über…」措辞照排 ✓。
- 发现并修复（MD 结构化 Edit，1 处）：行 390 `$s(\gamma_{v})$` → `$s(\gamma_{\nu})$`——同页行 388 对同一印刷记号已转写 `\gamma_{\nu}`，300dpi 裁片显示两处下标字形完全相同（v/ν 同形，p.003 已证不可辨），属 mineru 转写不一致，统一为 `\nu`（段内移交项核销）。
- 结果：PASS±（γ_ν 转写统一后与印刷一致）。
- 与 Luna 旧记录交叉：Luna 修复表无 p.16 行；重复编号 14. 与「der erste Klammer」为 Luna 总评未点名但属忠实保留项，本次补登记。

### p.017（PDF p.17 / 印刷 p.173）

- audited_at=2026-10-02 18:55 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p017.png`（pngmono 150dpi，两处修复均在该页图直接可辨，无需新增 300dpi）。
- 核对：页眉（Zur Theorie der Überlagerungsflaechen 印刷作 Überlagerungsflächen / 173）、页首续句（stante.…(II. 1) ist erfüllt…）、编号段 15（**print quirk「Zuendeführung」忠实保留 ✓**，印刷原文如此）、Δ′/Δ″ Teilgebiete、feste Zahl k 段、公式 `|s(γ_μ)−s(γ_ν)|≦(q−2)/(q−1) kL(Ω)`（无标点 ✓）、erfüllt sein 段（L(Ω)、Δ′ bzw. Δ″）、Für Ω wählen wir 段（ν=2,…,q）、公式 `λ(σₙ)≦s(γ₁)≦s(γ_ν)+(q−2)/(q−1) kL(Ωₙ).`（句点在）、Diese Ungleichungen 段、公式 `qλ(σₙ)≦Σ_{Ωₙ}λ(σ)+(q−2)kL(Ωₙ),`（逗号在）、wo die Summe 段（ein-eindeutig ✓、2λ_a、(q−2)kL）、公式 `qλ_a≦2λ_a+(q−2)kL,`、woraus sofort 句。
- 发现并修复（MD 结构化 Edit，2 处）：
  1. 行 398 正文引用「(II. I)」→「(II. 1)」——本页印刷第四行清晰为数字 1（与 p.013 同类 I/1 转写残留，段内移交项再核销一处）。
  2. 行 423 公式内多余逗号 `2, \lambda_{a}` → `2 \lambda_{a}`——印刷为「q λ_a ≦ 2 λ_a + (q−2) kL,」，2 与 λ_a 间无标点；数学恒等式亦唯一支持此读法。
- print quirk 保留核验（不改）：「Die Zuendeführung des Beweises」（印刷原文如此）MD 行 400 忠实保留 ✓。
- 结果：PASS±（两处修复后与印刷一致）。
- 与 Luna 旧记录交叉：Luna 修复表 p.17 行为「两处 𝒜′/𝒜″ 还原为 Δ′/Δ″」——本页 Δ′/Δ″ 均正确（该修复对象应在 p.018 内容，待次页核）；本次 (II. I) 与多余逗号系旧审计未检出项。
- 页界：本页止于「woraus sofort λ_a ≦ kL folgt.」，衔接正确。

### p.018（PDF p.18 / 印刷 p.174）

- audited_at=2026-10-02 19:10 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p018.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p018_zusammen_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p018_zasammen_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p018_zusammenhang2_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p018_sumplus_300dpi.png`。
- 核对：页眉（174 / Lars Ahlfors.）、Die Grössen λ′ und λ″ 段（γ_μ、σ′/σ″）、公式 `Σ_{Ω′}λ(σ′)+Σ_{Ω′}λ(σ″)≦Σ_{ν≠μ}s(γ_ν)≦(q−1)s(γ_μ)+(q−2)kL(Ω′).¹`（脚注标 ¹ 在 ✓）、Wenn wir diese 段（λ′+2λ″）、公式 `λ′+2λ″≦(q−1)λ_a+(q−2)kL≦(2q−3)kL.`（句点在）、Hiermit 段、编号段 16（Rückkehrschnitte γ̄、W̄₀、σ̄、Zerlegungsgesetz (4)）、公式 (9) `ϱ=Σϱ(W̄)+n(σ̄),`（逗号在、\tag{9}、n(σ̄) 横线 ✓——Luna p.18「补回 n(σ̄) 横线」经原页核验正确）、wo n(σ̄) 段、第二式 `ϱ=Σϱ⁺(W̄)−N₁+n(σ̄)`（无标点）、schreiben 段（N₁）、Nach einem grundlegenden Satz 段、页末断词「mehr-」、脚注 ¹「Die linksstehenden Summen…」。
- 发现并修复（MD 结构化 Edit，4 处）：
  1. 行 431 `Σ_{v≠μ}s(γ_v)` → `Σ_{ν≠μ}s(γ_ν)`——同一公式链在 p.017 侧均已转写 `\gamma_{\mu}/\gamma_{\nu}`，印刷下标同形（v/ν 不可辨，p.003 已证），统一转写（段内移交项核销）。
  2. 行 451 `Σ⁺ϱ(W̄)` → `Σϱ⁺(W̄)`（`\sum^{+}` → `\sum \stackrel{+}{\varrho}`）——300dpi 裁片显示加号在 **ϱ 上方**而非 Σ 上方；与 Luna p.20「ρ⁺ 位置」修复同类的加号归位。
  3. 行 456 还原印刷误植「zusammenhängende」→「**zasammenhängende**」——300dpi 裁片（`…p018_zasammen_300dpi.png`）确证印刷原文为 z-a-s；Luna 旧修复「zasammenhängende→zusammenhängende」违反 print quirk 忠实原则，本次撤销并还原；同段第二处「zusammenhängend」经裁片核验印刷拼写正确、维持不动。
  4. 删除两块游离脚注碎片 `$\Omega^{\prime}$`、`$\sigma^{\prime}$`（真实脚注 ¹ 完整含此二记号，碎片为 mineru 重复伪影；段内移交项核销）。
- 结果：PASS±（4 处修复后与印刷一致）。
- 与 Luna 旧记录交叉：旧表 p.18 行两项中「补回 n(σ̄) 横线」正确维持；「zasammenhängende→zusammenhängende」经原页仲裁判定为对印刷误植的不忠实改正，已撤销还原——本段发现的首例 Luna 旧修复方向性错误。
- 页界：本页止于「…Wenn die gegebene Fläche mehr-」（断词跨页，次页续「fach zusammenhängend ist…」），脚注 ¹ 位置与印刷一致。

## p.010–p.018 段内复核与移交登记（Wf-R-P02，续）

- 复核范围声明：本段 redo 覆盖 p.010–p.018（印刷 p.166–p.174，§ 3 全部、§ 4 全部、§ 5 至 Doppelungleichung (II. 2′) 止）。修复后重读本段全部编辑区（MD 行 315–460），无修复引入的新差异。
- 本段修复汇总（MD 结构化 Edit，8 处编辑动作）：
  1. p.011 `\tag{(5')}`→`\tag{5'}`（编号双层括号）；p.013 行 319 `(II. I)`/`(I. I)`→`(II. 1)`/`(I. 1)`（300dpi 证旧式数字 1）；p.015 条目 `$^{1}$`→`$1^{\circ}$`（度数符号误作脚注标）；p.016 行 390 `γ_v`→`γ_ν`；p.017 行 398 `(II. I)`→`(II. 1)`、行 423 删公式内多余逗号 `2, λ_a`→`2 λ_a`；p.018 行 431 `Σ_{v≠μ}s(γ_v)`→`Σ_{ν≠μ}s(γ_ν)`、行 451 `Σ⁺ϱ`→`Σϱ⁺`（300dpi 证加号在 ϱ 上）、行 456 还原印刷误植「zasammenhängende」（撤销 Luna 不忠实改正）、删 2 块游离碎片。
- Luna 旧修复重核结论（本段）：p.12（ρ⁺/o→0）、p.15（Ω/σ 表重建）、p.18「补回 n(σ̄) 横线」均与印刷一致维持；**p.18「zasammenhängende→zusammenhängende」判定为方向性错误并已撤销还原**（300dpi 裁片证印刷误植原文如此；同段第二处 zusammenhängend 印刷正确、未动）。
- print quirk 保留登记（本段新增）：重复编号「14.」（p.016，印刷确重新编号）、「Die Charakter eines Ausnahmefalls」（p.015）、「der erste Klammer」（p.016）、「Zuendeführung」（p.017）、「zur Oberteilung」（p.010）、「Summe erstreckt über」（p.016）——均忠实保留。
- 同形异写登记（本段）：「ϱ > o」「ϱ₀ ≦ o」「Zahlen ϱ und o」（p.013/p.012，旧式 0/o 同形；MD 维持 0）。
- 段内移交项核销情况：行 319 (II.I)/(I.I) ✓已修；行 390 γ_v ✓已修；行 458/460 碎片 ✓已删；重复 14. ✓判定为 print quirk 保留；行 333 imprint 位置 ✓与印刷一致（页底独立行）。
- 新发现移交项（属 p.019+）：MD 行 657 `\tag{(B_1)}` 双层括号（同 p.011 (5') 类，位于 Ungleichung (B₁)，约 PDF p.21）；行 599 `\varDelta_v`（兼 v/ν）；行 704 起后续页 `a_v` 类下标与游离块（行 828/910–916/1008 等）仍待对应页重检。
- 本段修复后的 MD 终态 SHA-256：`10e6cfe205aef4e4be162d93475f4d73a4f594293a45b88075a4a4695f04e198`（上段末 `b4e48563…` + 本段 8 处结构化 Edit）。
- 分级汇总（本段 9 页）：PASS 0、PASS± 9、FAIL 0。

### p.019（PDF p.19 / 印刷 p.175）

- audited_at=2026-10-02 20:00 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p019.png`（pngmono 150dpi，ϱ⁺ 三处加号位置在该页图直接可辨，无需新增 300dpi）。
- 核对：页眉（Zur Theorie der Überlagerungsflächen. / 175）、页首续句（fach zusammenhängend…N₁≦n(σ̄)）、Rückkerschnitt 句、公式 `ϱ⁺≧Σϱ⁺(W̄).`（句点在）、Wenn andererseits 段（ϱ=−1、N₁≦n(σ̄)+1）、公式 `ϱ⁺≧Σϱ⁺(W̄)`（无标点）、in jedem Falle 句、Die Grössen 段（(II. 1) 引用数字 1 ✓）、节标题 § 5. Die Umkehrung.、编号段 17（ϱ=Nϱ₀、ϱ=Sϱ₀、(II. 1) 引用）、Die Fläche W sei 段页末断句「Das Komplement von」。
- print quirk 保留核验（不改）：「Rückkerschnitt」（印刷原文如此，Luna 总评已登记）MD 行 464 忠实保留 ✓。
- 发现并修复（MD 结构化 Edit，3 处）——ϱ⁺ 加号转写不一致统一（印刷三处均为加号在 ϱ 上方；行内既有的 `\stackrel {+} {\varrho}` 惯例为准）：
  1. 行 463 display 式浮动 `{ } ^ { + } \varrho` ×2 → `\stackrel {+} {\varrho}` ×2；
  2. 行 466 行内 `$\varrho^{+}(\overline{W})$` → `$\stackrel {+} {\varrho}(\overline{W})$`；
  3. 行 473 「Die Grössen $\varrho(\overline{W})$」→「$\stackrel {+} {\varrho}(\overline{W})$」（印刷有 ϱ⁺，MD 漏加号）。
- 结果：PASS±（ϱ⁺ 统一后与印刷一致）。
- 与 Luna 旧记录交叉：Luna 修复表无 p.19 行；行 473（次页首式）为其 p.20「ρ⁺ 位置」修复对象、写法正确，本页三处系旧审计未检出项。
- 页界：本页止于「Das Komplement von」，次页续「W in Bezug auf F…」，衔接正确。

### p.020（PDF p.20 / 印刷 p.176）

- audited_at=2026-10-02 20:10 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p020.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p020_formeln_300dpi.png`。
- 核对：页眉（176 / Lars Ahlfors.）、页首续句（W in Bezug auf F zerfällt…Zerlegungsgesetz (4)）、公式 `Nϱ₀=ϱ+Σϱ(W′)+n(Γ),`（逗号在）、wo n(Γ) 段、Setzen wir N₁ 段、公式 `Nϱ₀=ϱ+Σϱ⁺(W′)−N₁+n(Γ).`（句点在、ϱ⁺ 加号在 ϱ 上）、Auf die Gebiete W′ 段（(II. 1) ✓）、公式 `Nϱ₀≧ϱ+(N−S)ϱ₀−N₁+n(Γ)−kL`（300dpi 证无句点，MD 无句点 ✓）、oder、公式 `ϱ≦Sϱ₀+N₁−n(Γ)+kL.`（句点在）、Wenn der ganze Rand Γ 段（α、N₁≦n(Γ)+α）、公式 `ϱ≦Sϱ₀+kL+α.`（句点在）、Diese Ungleichung 段（ϱ≧ϱ⁺−1，\stackrel ✓）、Metrisch-topologische Doppelungleichung 陈述（斜体整段，系统性丢失登记）、公式 (II. 2) `Sϱ₀−kL−1≦ϱ≦Sϱ₀+kL+α.`（\tag{II. 2} ✓）、Ist ϱ₀≧0 句（o/0 同形维持 0）、公式 (II. 2′) `Sϱ₀−kL≦ϱ⁺≦Sϱ₀+kL+α,`（逗号在、\tag{II. 2′} ✓、\stackrel ✓）、denn die zweite Hälfte 句。
- 发现并修复（MD 结构化 Edit，1 处）：行 497 `\sum^{+}\varrho(W′)` → `\sum \stackrel{+}{\varrho}(W′)`——300dpi 裁片证印刷加号在 ϱ 上方（ϱ⁺），非 Σ 上方。
- 仲裁否决（登记不改）：行 505 式（Nϱ₀≧…−kL）150dpi 疑有句点，300dpi 裁片显示无句点，MD 现状正确。
- Luna 旧修复重核（p.20 行「还原数字 1、希腊字母 α、ρ⁺ 位置及式号 (II. 2′)」）：(II. 2′) tag ✓、α ✓、本页各 ϱ⁺ \stackrel 写法 ✓，全部与印刷一致维持；本次 \sum^{+} 残留一处系该修复未覆盖到位。
- 结果：PASS±（加号归位后与印刷一致）。
- 页界：本页止于「…trivial für ϱ = −1.」，衔接正确。

### p.021（PDF p.21 / 印刷 p.177）

- audited_at=2026-10-02 20:20 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p021.png`（pngmono 150dpi；imprint 拆分依据即本页图底部版式，无需 300dpi）。
- 核对：节标题 II. Offene Überlagerungsflächen.、编号段 18（Spurpunkt、abzählbare Folge、W*、Ausschöpfung、umgekehrt）、Eine Folge 段（(I) und (II) 公式组引用 ✓）、regulär 定义句（斜体整段丢失登记；lim L/S = 0 的 o/0 同形维持 0）、In den folgenden 段、编号段 19、公式 `|S−S(Δ)|≦kL,`（逗号在）、gleichmässig 段（»Insel« / »Zunge« 尖引号 ✓ 忠实保留）、页末断词「betref-」、页底 imprint 行「23—34686. Acta mathematica. 65. Imprimé le 8 février 1935.」。
- 发现并修复（MD 结构化 Edit，1 处）：**imprint 行嵌入段内词中**——MD 原为「…die Multiplizität der betref-23–34686. Acta mathematica.…」连写；印刷中段落止于页底「betref-」（断词跨页），imprint 为页底独立行。已拆分为段落断词 + 独立 imprint 行（段内移交项核销；短横形式沿用本篇 imprint 既有 MD 惯例，长划差异同前登记为排版级）。
- 同形登记（不改）：lim L/S = o 的 o 形字符（0/o 同形，同 p.008/p.012/p.013 类）。
- 结果：PASS±（imprint 拆分后与印刷版式一致）。
- 与 Luna 旧记录交叉：旧总评已登记 p.21 »Insel«/»Zunge« 保留 ✓；imprint 嵌入词中系旧审计未检出的结构缺陷。
- 页界：本页止于「…der betref-」（次页续「fenden Insel.」），imprint 在段落后、页底，MD 顺序已按印刷恢复。

### p.022（PDF p.22 / 印刷 p.178）

- audited_at=2026-10-02 20:30 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p022.png`（pngmono 150dpi）；本页无需 300dpi 仲裁。
- 核对：页眉（178 / Lars Ahlfors.）、页首续句（fenden Insel.…vollständig überdeckt wird.）、Den von den Zungen 段（μ(Δ)）、**Gleichung (A)** 标题（印刷黑体，MD 黑体丢失登记）、公式 `n(Δ)+μ(Δ)=S+O(L)`（无标点 ✓）、schreiben 段（Landauische Bezeichnungsweise、(A) 引用）、公式 `\overline{\lim} n(Δ)/S≦1.`（lim 上横线 ✓、句点在）、Wenn man das Gebiet 段（n(a)、Multiplizitäten、(A) 引用、Konstante k）、编号段 20、Als Grundfläche 段（Geschlecht Null、q≧2、Δ₁,…,Δ_q）、Ausser der 段页末断句「definieren,」。
- 结果：PASS±。内容、公式与记号逐项与印刷一致，无修复项。保留登记（排版级）：Gleichung (A) 黑体丢失；regulär 定义句斜体丢失（系统性）。
- Luna 旧修复重核（p.22 行「两处 𝒜 还原为 Δ」）：本页 Δ 记号全部正确，与印刷一致，维持。
- 与 Luna 旧记录交叉：无新差异。
- 页界：本页止于「…eine zweite Multiplizität definieren,」，次页续，衔接正确。

### p.023（PDF p.23 / 印刷 p.179）

- audited_at=2026-10-03 19:25 EDT；actor=Wf-R-P02；model=account:zai-individual-coding-plan/GLM-5.3-Flash；effort=max（run级配置，自报UNKNOWN）。
- PNG：`audit-redo/ueberlagerungsflaechen_p023.png`（pngmono 150dpi）；300dpi 仲裁裁片：`audit-redo/ueberlagerungsflaechen_p023_gegeben_300dpi.png`、`audit-redo/ueberlagerungsflaechen_p023_zerlegung_300dpi.png`。
- 核对：页眉（Zur Theorie der Überlagerungsflächen. / 179）、页首续句（einfache Multiplizität 定义…nur für einfach zusammenhängende Gebiete Δ bilden）、p(Δ) 定义段（n(Δ)、p(Δ_ν)、Σ₁^q p(Δ_ν) 上下限 1/q、上界 qS+kL、无第二个脚注标）、Wir betrachten 段（Ω_i/Ω_z、W′、W̄、W̄₀、脚注标 ¹ 在「besitzen.」后 ✓、Hurwitzsche Relation 特征数不少于 q−2 的倍数）、Die Zerlegung 段（Σϱ(W̄)+Σϱ(Ω_i)=Σϱ(W′),、p=−Σϱ(Ω_i)=Σϱ(W̄)+N(W′)、N₁(W̄)、p=Σϱ⁺(W̄)+N(W′)−N₁(W̄)、「Nach dem was oben gezeigt wurde」措辞照排 ✓）、页末断句「Hieraus folgt dass」、脚注 ¹（»Binnenseen« 尖引号 ✓）。
- 发现并修复（MD 结构化 Edit，3 处含 4 字形）：
  1. 行 574 两处 `p(\Delta_v)` → `p(\Delta_{\nu})`、行 576 一处 `\Delta_{v}` → `\Delta_{\nu}`——印刷下标 v/ν 同形不可辨（p.003 已证）；全篇 `\nu` 转写 20 处为既有主流（行 45/388/390/400/403/411/431/629/659/700 等），本段 v 为 mineru 转写不一致，按转写一致性统一为 `\nu` 并留痕，非按数学预期静默改正。
  2. 行 578 `\varrho^+(\overline{W})` → `\stackrel {+} {\varrho}(\overline{W})`——300dpi 裁片确证加号在 ϱ 上方而非上标；与 p.018/p.019/p.020 同类加号归位，沿用全篇 `\stackrel {+} {\varrho}` 惯例（行 451/474/493）。
- 仲裁否决（登记不改）：150dpi 初读疑「gegeben.」后有上标脚注标；300dpi 裁片显示其后无任何标记（扫描尘点），MD 无标正确。
- 保留登记（PASS± 排版级，不修）：行 572 prose 内 Δ 以裸 Unicode 转写（非 `$\Delta$`，语义同形、转写风格差异）；Rückkehrschnitt/Insel/Zunge 等斜体丢失（系统性）；页眉未收（系统性，旧审计已登记）；脚注 ¹ 在 MD 中置于 Zerlegung 段后独立小块（mineru 既有布局惯例，非页底位置）。
- 与 Luna 旧记录交叉：旧 p.023 判 PASS±（仅页眉缺失）；本次另发现 ϱ⁺ 加号位置与 v/ν 转写不一致两项内容级问题并已修复，其余吻合。
- 结果：PASS±（3 处修复后与印刷一致）。
- 页界：本页止于「…Hieraus folgt dass」（MD 行 578 吻合）+ 页底脚注 ¹；「β = N(W′)…」起为 p.024 内容。

<!-- redo-tail -->
