# AUDIT-Deligne_1974_weil1.redo — Luna 审计重做（Deligne 1974, La conjecture de Weil I）

- **性质**：Luna 审计重做。用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核。印刷原文（PDF 原页）为唯一裁决源；Luna 旧修复只是被检对象之一。print quirk 与错字忠实保留登记，绝不按数学预期静默改正；看不清即升级说明，绝不编造。
- **actor**：Wf-R-P01
- **host/model/effort**：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置，自报 UNKNOWN）
- **日期时间**：2026-10-02 14:31 EDT 开工
- **PDF SHA-256**：`8392b345d4854e6dc55fb42cfc0b616d941935983723627237239a87348f42e5`（36 页；PDF p.1 为 Numdam 数字化封面页，PDF p.2-36 = 印刷 pp.273-307）
- **MD 基线 SHA-256**：`fdada5f38196e5f3b46feca4a0a94ef912ffe7b4bda03c4081ab47b8ece3c6e4`（`Deligne_1974_weil1__Deligne_1974_weil1.md`，重做起点）
- **文本层判定**：`pdftotext -f 1 -l 1` 与 `-f 5 -l 5` 均成功输出文本（封面为原生文本层，正文页为 OCR 文本层，公式噪声大）。→ **可用，采用双通道主对账**：pngmono 150dpi 视觉逐页为主裁决通道，pdftotext 文本仅作辅助交叉核对，不作为公式/上下标依据。
- **证据目录**：`audit-redo/`（p001.png … pNNN.png，pngmono 150dpi；不触碰旧 `audit/`）
- **旧 AUDIT**：`AUDIT-Deligne_1974_weil1.md`（Luna 原审计，只读对照，不修改）

---
## p.001（PDF p.1 / Numdam 数字化封面，无印刷页码）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 14:50 EDT。
- PNG：audit-redo/p001.png（pngmono 150dpi）。
- 旧审计对照：Luna p.001 = PASS±，未修复正文，称刊头与 Numdam 数字化标识属页面布局信息。
- 核对：封面题录——刊头、作者 PIERRE DELIGNE、题名 La conjecture de Weil : I、期刊卷年页码（tome 43, 1974, p. 273-307）、Numdam item URL、版权段全文、页脚 NUMDAM 块。
- 结果：PASS±。作者/题名/期刊卷年页码/URL/版权法律文本与 md 逐项吻合（撇号排为直引号，不误导）。差异：md 缺印刷页顶部刊头横幅「PUBLICATIONS MATHÉMATIQUES DE L'I.H.É.S.」与页脚「NUMDAM / Article numérisé dans le cadre du programme / Numérisation de documents anciens mathématiques / http://www.numdam.org/」整块。均为来源/版式信息，不误导检索与使用，不构成 FAIL。
- 修复：补录上述两块缺失文本（依据 audit-redo/p001.png；NUMDAM 图形标志本身不录，只录其下文字行）。Luna「不修」的处置本次改为补全，属增补非改正。
