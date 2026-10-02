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
## p.002（PDF p.2 / 印刷 p.273）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 15:00 EDT。
- PNG：audit-redo/p002.png（pngmono 150dpi）。
- 旧审计对照：Luna p.002 = FAIL→已修复（公式号 I.I.I→(1.1.1)、zeta 因子 I→1）；本次重核修复后状态。
- 核对：题名页（LA CONJECTURE DE WEIL. I / par PIERRE DELIGNE）、SOMMAIRE 全 8 条及页码 273/280/283/287/289/294/298/301、引言三段（含 « difficile »、§§ 3, 6, 7 et 8、Cambridge juillet 1973、N. Katz）、§1 节标题、(1.1) 定义段、公式 (1.1.1) ζ_X(s)=Π_{x∈|X|}(1−N(x)^{-s})^{-1}、ℜ(s) 与 Spec(Z) 句。
- 结果：PASS±。全部内容项与印刷页吻合；Luna 的两处修复（公式号、标量 1）经原页确认正确且已生效。差异：①md 无页脚印刷页码 273 与装订号 35（全篇系统性版式省略，不误导）；②(1.1.1) 公式号在 md 中为独立 display 块置于公式前（排版投影差异，编号存在且正确）；③N、X 等罗马/粗体字形在 md 中混用（不误导）。
- 修复：无（本页无需改 md）。
## p.003（PDF p.3 / 印刷 p.274）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 15:07 EDT。
- PNG：audit-redo/p003.png（pngmono 150dpi）。
- 旧审计对照：Luna p.003 = FAIL→已修复（(1.1.2) 标量 I→1、公式号 I.I.3→(1.1.3)、Identifons→Identifions）；本次重核修复后状态。
- 核对：(1.1) 末段（q_x、deg(x)=[k(x):F_q]、t=q^{-s}）、公式 (1.1.2) Z(X;t)=Π(1−t^{deg(x)})^{-1};（含尾分号）、(1.1.3) ζ_X(s)=Z(X;q^{-s}).（含尾句号）、(1.2) Dwork 引文（Amer. J. Math., 82, 1960, p. 631-648）与 Grothendieck [1] et SGA 5、ℓ-adique/p-adiques/cristalline/Washnitzer/Lubkin 段（Ann. of Math., 87, 1968, p. 105-255）、(1.3) 全段（H^i、H_c^i、i>2 dim(X)）、(1.4) 起句至 Identifions。
- 结果：PASS±（修复 1 处）。内容全部与印刷页吻合；Luna 三处修复经原页确认正确生效。新发现残留伪影 1 处：公式 (1.1.2) 的编号 tag 在 md 中为损坏的 `\tag{\( (1.1.2) \}`（含游离 `\( ` 与 `\}`，可破坏公式渲染），编号本身正确。
- 修复：`\tag{\( (1.1.2) \}` → `\tag{1.1.2}`（依据 audit-redo/p003.png 左侧编号 (1.1.2)；md 行 61）。这是 Luna 修复不彻底处（改了编号文字但未清掉包裹伪影）。
- 增补（300dpi 仲裁后追加，回溯计入本页）：`On n'exclut pas le cas $p=0$.` → `$p=o$.`（md 行 76）。300dpi 裁片 audit-redo/300dpi/p003_p_eq_zero-03.png 显示印刷在 `p =` 后为小写字母高度的圆形字形；与同页同字号参照数字零（`1960`、`631-648`，裁片 audit-redo/300dpi/p003_ref_zeros_1960-03.png）高度差明显，判定印刷原文此处以字母 o 排数字零，属 print quirk。按「印刷 quirk 忠实保留」改回 o 并登记。此项针对 MinerU 原始导出即有的 $p=0$（非 Luna 改动，Luna p.003 修复单未含此项）。
- 300dpi 仲裁方法论（适用后续各页）：本印刷体行内数学的「0」存在被排成小写 o 的系统性 quirk；裁决标准 = 与同页同字号已知数字零（年份/页码区间）比高度，高度同小写 o 者按字母 o 录入并登记，不按数学预期改正。
## p.004（PDF p.4 / 印刷 p.275）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 15:26 EDT。
- PNG：audit-redo/p004.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p004_dF_zero-04.png、p004_eq153_identity-04.png、p004_eq153_identity_600dpi-04.png、p004_Il_induit_600dpi-04.png、p004_num_1_600dpi-04.png。
- 旧审计对照：Luna p.004 = FAIL→已修复（F_{σ^n}→F_{q^n}、两处 (-i)^i→(-1)^i、两处 dF=o→dF=0、(1.5.2) 分母标量 I→1；(1.5.3) 恒等算子 I 保留）；本次重核修复后状态。
- 核对：(1.4) 末句 φ∈Gal(F̄_q/F_q)、a)-d) 全部（X^F、X^{F^n}、|X|_F 轨道、deg）、公式 (1.4.1)、(1.5) 应用 F*:H_c^i→H_c^i、Lefschetz 公式 #X^F=Σ(-1)^i Tr(F*,H_c^i(X,Q_ℓ));（含尾分号）、dF 句、(1.5.1)（含尾句号）、(1.5.2) 双行（含 −(−deg(x)t^{deg(x)})/(1−t^{deg(x)}) 的印刷原样与 Σ_{(1.4.1) n} 下标 quirk）、(1.5.3) t d/dt log(det(I−Ft,V)^{-1})=Σ_{n>0}Tr(F^n,V)t^n。
- 结果：PASS±（回退 Luna 旧修复 3 处）。F_{q^n}、两处 (-1)^i、(1.5.2) 标量 1 等 Luna 修复经原页确认正确；Σ_{(1.4.1) n} 下标与 −(−⋯) 双负号均为印刷原样，md 忠实保留。三处问题：①②两处 `dF =` 后印刷为小写字母高度 o（300dpi 裁片 p004_dF_zero-04.png，同页参照零比对法同 p.003 增补），印刷原文即 `dF = o`；Luna 把 md 的 dF=o 改为 dF=0 属按数学预期改正印刷 quirk，回退。③(1.5.3) 恒等算子：初裁曾判大写 I（对照 p004_Il_induit_600dpi-04.png 与粗体 (1.5.1) 数字 1），后发现该字体正体数字 1 本无左旗（600dpi 参照 audit-redo/300dpi/p002_ref_1973-02.png 的「1973」、p005_ref_dimV1-05.png 的 dim(V)=1），其形态=窄干+上下小衬线，与 (1.5.3) 处 det(?) 字形完全一致；大写 I（Il induit 参照）为宽干重衬线，形态迥异。终裁：印刷为数字 1。Luna「保留 I」与其修复表中「(1.5.2) 分母标量 1」的同类判定自相矛盾，本页 (1.5.3) 的 I 系 Luna 漏改，改判 I→1。此判定同时推翻本条目初稿的第②小点裁定，以本段为准。
- 修复：两处 `dF=0` → `dF=o`（md 行 108；依据 p004_dF_zero-04.png）；(1.5.3) `\det (\mathrm{I} - \mathrm{F} t, \mathrm{V})` → `\det (1 - \mathrm{F} t, \mathrm{V})`（md 行 127；依据 p004_eq153_identity_600dpi-04.png + p002_ref_1973-02.png 形态比对）。print quirk（零排作 o）忠实保留并登记。
