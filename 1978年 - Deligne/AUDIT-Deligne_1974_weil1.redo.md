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

## p.005（PDF p.5 / 印刷 p.276）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 16:23 EDT。
- PNG：audit-redo/p005.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p005_a_unnum_det-05.png、p005_b_eq154_det-05.png、p005_c_theorem16-05.png、p005_c2_t_dot_1-05.png、p005_d_Pi_det-05.png、p005_e_taylor_t-05.png（均 600dpi）及参照 p005_ref_dimV1-05.png、p005_ref_sont1-05.png、p002_ref_1973-02.png。
- 旧审计对照：Luna p.005 = FAIL→已修复（(1.6) det(t.i—F*)→det(t·I−F*)、P_i(t) 恒等算子 i→I、移除误挂 (1.5.3) 的页脚 275）；本次重核发现 Luna 在同一页自相矛盾：页条目称 P_i 印刷为 det(1−F*t,…)（即数字 1），修复表却写「恒等算子 I」。
- 核对：(1.5.3) 末句（le vérifier pour dim(V)=1）、未编号式 t d/dt log Z=Σ(−1)^i t d/dt log det(1−F*t,H_c^i(X,Q_ℓ))^{-1},、(1.5.4) Z(X_0,t)=Π_i det(1−F*t,H_c^i(X,Q_ℓ))^{(−1)^{i+1}}.、Q_ℓ(t)/Q_ℓ[[t]]/Z[[t]] 段（含 Taylor en t=o quirk）、Théorème (1.6) 全文（含 det(t.1−F*,…)、|α|=q^{i/2}）、Lemme (1.7)、Preuve (1.7)⇒(1.6)（Z[[t]]、Σ a_n t^n、Hankel 行列式 H_k=det((a_{i+j+k})_{0≤i,j≤M})(k>N)、Fatou 引文、P/Q 首一条件）、P_i(t)=det(1−F*t,H^i(X,Q_ℓ)).
- 结果：PASS±（修复 4 处，均涉 Luna 修复方向性错误）。恒等字形形态学终裁（见 p.004 条目③）：本印刷体正体数字 1=窄干+上下小衬线无旗（1973、dim(V)=1 参照），大写 I=宽干重衬线（Il induit 参照）；p.276 全部 det(?) 字形属前者 → 印刷为数字 1。据此：①(1.5.4) Luna 留下的 I 改为 1；②P_i(t) Luna 改的 I 改回 1（其页条目原文即印作 1，修复表为笔误级错误）；③(1.6) Luna 的 t·I 改回 t.1（600dpi 裁片 p005_c2_t_dot_1-05.png 显示分隔点在基线，为句点「t.1」，非居中乘点；Luna 的居中乘点属改写印刷原样）；④行内「Taylor en t =」后印刷为小写字母高度 o（p005_e_taylor_t-05.png；pdftotext 同读 t=o），按零排作 o 的 print quirk 保留为 t=o，md 原 t=0 改回。未编号式 md 本作 1，正确。残留微差异（不改）：Hankel 上标 M 印刷为斜体、md 作 \mathbb{M}，(k>N) 的 N 印刷斜体、md 作 \mathbf{N}，纯字体投影；(1.6)「(= lisse)」md 缺空格。
- 修复：①`\det (I - F ^ {*} t, H _ {c} ^ {i} (X, Q _ {\ell}))`（1.5.4）→ `\det (1 - …)`（md 行 139）；②P_i(t) `\det (\mathrm{I} - …)` → `\det (1 - …)`（md 行 167）；③`det(t·I − F*, …)` → `det(t.1 − F*, …)`（md 行 146）；④`$t=0$` → `$t=o$`（md 行 142）。系统性提示：`\det (\mathrm{I} …)` 模式在全篇多处出现（行 239/247/259/457/509/553/563/993/999/1013/1019/1025/1035/1052/1062 等），后续页块应按同一形态学标准逐页用原页裁决，预计均应为数字 1。

## p.006（PDF p.6 / 印刷 p.277）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 16:35 EDT。
- PNG：audit-redo/p006.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p006_mapsTo_arrow-06.png（300dpi）。
- 旧审计对照：Luna p.006 = FAIL→已修复（六处 Q_t→Q_ℓ、一处 Z_t→Z_ℓ、§1.9(b) 两处 sheaf F→𝓕），页条目无结果行（原文缺「结果」字段，仅描述性）；本次重核修复后状态。
- 核对：P_i 互素段与 (1.5.4) 不可约性、P(t)=Π_{i impair}P_i(t)/Q(t)=Π_{i pair}P_i(t).、K 与 R(t)=P(t)Q(t) 段（q^{-i/2}、Gal(K/Q)、lemme de Gauss、inverses d'entiers algébriques、indépendant de ℓ）、(1.8)、(1.9) 起句（SGA 5 VI）、a)（constant tordu）、b)（π_1(X,x̄)、 fibre 𝓕_x̄、双箭头行、quotient fini）、c)（X^{an}、Z_ℓ-Modules 大写 M quirk、𝓕|X_i=𝓕_i⊗_{Z_ℓ}Q_ℓ.）、(1.10)（H^i/H_c^i、i>2 dim(X)）。
- 结果：PASS±（修复 2 处）。内容全部吻合；Luna 的 Q_ℓ/Z_ℓ/𝓕 修复生效。①MinerU 捕获的裸页码行「277」残留在 P_i(t) 式与下段之间——Luna 已删同类页码 275/279 却漏删此行，本次补删（与 Luna 既有处置对齐；页码属版式家具非正文）。②b) 末尾印刷为「…constants tordus sur X)↦」且次行以「↦ (représentations…」起（300dpi 裁片 p006_mapsTo_arrow-06.png 确认两处均带竖杠的 maps-to），md 首箭头投影为「→」，改回「↦」；次行 \mapsto 本已正确。print quirk 保留：Z_ℓ-Modules 的大写 M、(1.9)b) 印刷在行尾/行首重复 ↦ 的折行方式。
- 修复：①删裸行「277」（原 md 行 170）；②`sur X)→` → `sur X)↦`（md 行 192）。

## p.007（PDF p.7 / 印刷 p.278）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 17:10 EDT。
- PNG：audit-redo/p007.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p007_fiber_product_subscript-07.png、p007_eq113_det-07.png（300dpi）；对照物证 Deligne_1974_weil1_mineru/Deligne_1974_weil1/images/page_6_image_2.jpg（MinerU 交换图截图）。
- 旧审计对照：Luna p.007 = FAIL→已修复（§1.12 的 script F_0/F 记号、𝓕_{F^n(x)}、(1.12) 与 (1.12.1) 两个 (-1)^i）；页条目无结果行；本次重核修复后状态。
- 核对：(1.10) 末句（X^{an}）、(1.11) 全段（F*:F*𝓕≅𝓕、[𝓕_0] espace étalé、f:[𝓕_0]→X_0 étale、sections locales）、交换图（上 [𝓕]–F→[𝓕]，两侧 f↓，下 X–F→X；MinerU 截图与印刷图一致）、d'où un morphisme [𝓕]→X×_{(F,X,f)}[𝓕]=[F*𝓕]、F*𝓕≅𝓕 cherché、(1.12) 全段与三段链 F*:H_c^i(X,𝓕)→H_c^i(X,F*𝓕)→H_c^i(X,𝓕)、F*_x:𝓕_{F(x)}→𝓕_x、Lefschetz 公式 Σ_{x∈X^F}Tr(F*_x,𝓕_x)=Σ_i(−1)^iTr(F*,H_c^i(X,𝓕)).、n^ième itéré 句（𝓕_{F^n(x)}）、(1.12.1)、(1.13) 全段与 det(1−F*_{x_0}t,𝓕_0)=det(1−F*_{x_0}t,𝓕_x).（300dpi 确认两个下标均为 x_0，第二处 sheaf 为 𝓕_x）、A isomorphisme près 句。
- 结果：PASS±（修复 3 处）。内容与图全部吻合；Luna 的记号与 (-1)^i 修复生效。①交换图引用路径悬空：md 写 `images/page_6_image_2.jpg`，实际文件在 `Deligne_1974_weil1/images/page_6_image_2.jpg`（mineru kit 嵌套目录；md 被上移一层导致相对路径失效），改为正确相对路径，图得以渲染（Luna 未察觉链接失效）。②X×_{(…)} 纤维积下标：md 作 (\mathbb{F},\mathbf{X},f)，300dpi 裁片显示印刷为斜体 (F, X, f)，改回。③(1.13) 两处恒等字形按 p.004/p.005 确立的形态学终裁为数字 1，`\mathrm{I}`→`1`（300dpi 裁片 p007_eq113_det-07.png）。
- 修复：①`![](images/page_6_image_2.jpg)` → `![](Deligne_1974_weil1/images/page_6_image_2.jpg)`（md 行 210）；②`_{(\mathbb{F},\mathbf{X},f)}` → `_{(F,X,f)}`（md 行 212）；③(1.13) 两处 `\mathrm{I}` → `1`（md 行 237）。范围外提示：行 782 的 `images/page_18_image_6.jpg` 同样悬空，属后续页块（印刷 p.287 邻域）处置。

## p.008（PDF p.8 / 印刷 p.279）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 17:24 EDT。
- PNG：audit-redo/p008.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p008_eq1141_det-08.png、p008_eq1152_dfn-08.png（300dpi）。
- 旧审计对照：Luna p.008 = FAIL→已修复（公式号 (1.14.1)、(1.14.2) 分式结构与集合 X^{F^n}、交叉引用 (1.15.1)、移除误挂末式的页脚 279；(1.14.2) 分母 dfn 按印刷保留）；本次重核修复后状态。
- 核对：(1.14) 定义句、(1.14.1) Z(X_0,𝓕_0,t)=Π_{x∈|X_0|}det(1−F*_x t^{deg(x)},𝓕_0)^{-1}.、faisceau constant 句、(1.14.2)（含分母 dfn 印刷 quirk 与 Σ_{n}Σ_{x∈X^{F^n}=X_0(F_{q^n})}）、Substituant 句、(1.14.3)、identité dans Q_ℓ[[t]] 句、(1.15) 字典段（F̄_q^1/F̄_q^2、σ:F̄_q^1→F̄_q^2、H_c^*(X_1,𝓕_1)≅H_c^*(X_2,𝓕_2).、F*=φ^{-1}(dans End(H_c^*(X,𝓕)))、(1.15.1) F*=F 的编号投影、Gal(k(x)/k(x_0)) 句）、(1.15.2)、En notations galoisiennes 句与末式。
- 结果：PASS±（修复 5 处）。Luna 的修复与 dfn 保留（(1.14.2)）均确认；md 无游离页码。①(1.14.1)、(1.14.3)、末式共 4 处 det 恒等字形：按 p.004/p.005 确立的形态学标准（本页证据 p008_eq1141_det-08.png：窄干小衬线无旗=数字 1），`\mathrm{I}`/`I` 全部改 1。②(1.15.2) 印刷在首个 F* 的下标 x_0 下方另有小字定义标记「dfn」（p008_eq1152_dfn-08.png），md 完全漏录；Luna 只在 (1.14.2) 保留了 dfn、此处的 dfn 未处置。按印刷原样补录为下标堆叠 \substack{x_0 \\ dfn}。
- 修复：①(1.14.1) `\det (\mathrm{I} …)`→`\det (1 …)`；②(1.14.3) 同；③④末式两处 `\det (I …)`→`\det (1 …)`；⑤(1.15.2) 首项 `\mathrm{F} _ {x _ {0}} ^ {*}`→`\mathrm{F} _ {\substack{x _ {0} \\ \mathrm{dfn}}} ^ {*}`。
