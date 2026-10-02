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

<!-- redo-tail -->
