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

<!-- redo-tail -->
