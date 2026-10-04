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

## p.009（PDF p.9 / 印刷 p.280）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 17:32 EDT。
- PNG：audit-redo/p009.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p009_caracteristique-09.png、p009_ref_280-09.png（300dpi）。
- 旧审计对照：Luna p.009 = FAIL→已修复（1/4、Tate twist 中 I→1、「caractéristique 0」）；本次重核修复后状态。
- 核对：§2 节标题、(2.1) 起句（langage farfelu）、a) Variétés différentiables 全段（Z′、Tr:H_c^n(X,Z′)→Z、classe fondamentale）、b) Variétés complexes 起句、a) X²=−1/+i、b) R/Z 与 U¹={z∈C||z|=1}、+i est l'image de 1/4、c) exp(±2πix) 与 U¹、Z(1) 定义段（Ker(exp:C→C*)、y=±2πi、c):x↦exp(xy)）、Z(r) 幂句、(2.2) 全段（caractéristique o、Ẑ*/Z*、Z/ℓ^n(1)、système projectif）、σ_{m,n} 转移式、Z_ℓ(1)=lim proj、Q_ℓ(1)=Z_ℓ(1)⊗Q_ℓ、Q_ℓ(r)=Q_ℓ(−r)^∨。
- 结果：PASS±（回退 1 处 Luna 修复）。内容全部吻合；Luna 的 1/4 与 Tate twist (1) 修复生效。①「caractéristique」后字形：300dpi 裁片显示为小写字母高度 o（与同 crop 内 choisir/isomorphismes 的 o 同形同高；页眉粗体 280 参照零远大之），印刷原文为「caractéristique o」——与 p.003 (p=o)、p.004 (dF=o)、p.276 (t=o) 同属本印刷体「零排作 o」的系统性 quirk。Luna 把 md 的 o 改为 0 属按数学预期改写印刷原样，回退为 o 并登记。范围外提示：行 426（印刷 p.283）、844（p.292）、904（p.293，即 Luna 重分类「caractéristique 0」的那处）的同模式实例，应由对应页块按同一 300dpi 比高法重裁——本块证据提示 Luna 的 p.022 判 0 很可能同样有误。
- 修复：`caractéristique 0` → `caractéristique o`（md 行 308；依据 p009_caracteristique-09.png + p009_ref_280-09.png）。

---

## 本块总评（p.001-p.009 / PDF p.1-9 = 封面 + 印刷 pp.273-280）

- **覆盖声明**：9/9 页逐页审计完成（2026-10-02 14:31-17:29 EDT）。每页 pngmono 150dpi 全页目检（audit-redo/p001-p009.png）+ 关键字形 300/600dpi 仲裁裁片共 17 张（audit-redo/300dpi/，含参照裁片）；pdftotext 文本层全程辅助交叉核对（双通道主对账），公式/字形裁决一律以原页图像为准。分级：**PASS± ×9，PASS ×0，FAIL ×0**（分级针对重做时的页面状态；每页瑕疵均当场以 Edit 修复并登记）。
- **修复统计**：本块共改 md 22 处（按各页条目修复计数：p.001×2 + p.003×2 + p.004×3 + p.005×4 + p.006×2 + p.007×3 + p.008×5 + p.009×1；git diff vs 重做前 8aa00fdd：27 insertions / 19 deletions，仅目标 md）。修复后 md SHA-256：`6a2401c4023bc3fb58896535282be2aa078a3ccdfd953ff6db0362a3ba043831`（1504 行）。只读终验：游离三字页码行本块区间 0（行 484+ 的 7 处属后续页块，见下）；`\tag` 共 31 处与印刷公式编号清点相符；本块 det 恒等字形 0 残留 `I`。
- **系统性发现一（print quirk：零排作小写 o）**：本印刷体行内数学的数字 0 多处排为小写字母高度 o（p=o (1.3)、dF=o ×2 (1.5)、t=o (p.276)、caractéristique o (2.2)）；裁决法=与同页同字号已知数字零（年份/页码）比高。**Luna 的 o→0 系列修复属按数学预期改写印刷原样，本块 4 处已全部回退并登记**。范围外同模式待核：md 行 426（印刷 p.283）、844（p.292）、904（p.293）——其中行 904 即 Luna 据以「重分类」p.022 为 FAIL 的那处，本块同型证据提示该判定很可能同样有误，后续页块必须逐处以 300dpi 比高法重裁，不得沿袭。
- **系统性发现二（恒等字形 det(1−Ft) 非大写 I）**：本印刷体正体数字 1=窄干+上下小衬线无旗，大写 I=宽干重衬线（Il induit 参照）；全部 det(?) 字形经 600dpi 形态学比对均为数字 1（Luna 的 P_i 判 I 与其自身页条目矛盾；(1.5.3) 的 I 系漏改）。本块 8 处已改 1。范围外残留 `\det (\mathrm{I}…)`/`\det (I …)` 共 12 处（行 457/509/553/563/993/999/1013/1019/1025/1035/1052/1062），后续页块按同一标准逐页裁决。
- **系统性发现三（MinerU 图片链接悬空）**：md 的 `images/…` 相对路径相对 md 自身位置不存在，实际文件在 `Deligne_1974_weil1/images/` 嵌套目录。本块已修行 210（交换图，图像内容经与印刷图核对一致）；范围外残留行 782（page_18_image_6.jpg），后续页块处置。
- **范围外其他移交项**：裸三字页码行 7 处（行 484=284、712=288、768=289、950=295、1119=298、1171=299、1329=302），与 Luna 已删的 275/279 及本次删除的 277 同类，建议后续页块按页归属删除；Hankel 式 `\mathbb{M}`/`\mathbf{N}` 字体投影（行 155）本块登记不改。
- **Luna 审计质量小结（仅本块 9 页证据）**：Luna 的题录/文字级修复（Identifions、(1.1.2)/(1.1.3) 标量与编号、F_{q^n}、(-1)^i、Q_ℓ/Z_ℓ/𝓕 记号、1/4、dfn 保留等）大部正确；但存在四类方向性错误——按数学预期改正 print quirk（o→0 系）、恒等字形误判（I/1 形态学不辨）、修复表与页条目自相矛盾（P_i）、以及对图链失效/裸页码 277/(1.15.2) dfn 的漏检。用户判定 Luna 审计不可信在本块证据下成立，逐页重检必要。
- **mineru doc_id**：`structured_content.json` 仅含 pages/metadata/extensions/is_full_document 字段，无 doc_id 标识；如实记为缺失。
- **SOP 偏离声明**：本重做未向 repo 根 `AUDIT-PROGRESS.log` 追加行（ask 明令禁止写根级任何文件）；页级进度以本 redo AUDIT 的逐页条目 + 每页独立 commit（5ab03a49 → 61303542）承载，可追溯性由 git 历史保全。修复均以结构化 Edit 逐处手改目标 md，脚本仅用于只读清点；未改 PDF、未动旧 audit/ 与旧 AUDIT、未触碰其他论文目录、未 push。

## p.010（PDF p.10 / 印刷 p.281）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 19:00 EDT。
- PNG：audit-redo/p010.png（pngmono 150dpi）。
- 旧审计对照：Luna p.010 = FAIL→已修复（Euler 特征 (-1)^i、Q_t→Q_ℓ、epsilon 标量 1 与 (-1)^N）；本次重核修复后状态。
- 核对：§2.2 末段（Q_ℓ(1)≅Q_ℓ、aut(k) 经 Z_ℓ* 作用、φ:x↦x^q 乘 q）、faisceau d'orientation 段、Tr 两式、Théorème (2.3) dualité de Poincaré（Tr(x∪y) 式与 dual de H^{2n-i}(X,Q_ℓ(n))）、(2.4)（q^n α_j^{-1}）、(2.5) a)-d)、(2.6) χ(X) 定义与函数方程 Z(X_0,t)=ε·q^{−nχ(X)/2}·t^{−χ(X)}·Z(X_0,q^{−n}t^{−1})、ε={1 / (−1)^N} 分段式、Grothendieck formulation 句。pdftotext 交叉核对一致。
- 结果：PASS±（本页无需改 md）。内容全部吻合；Luna 四项修复生效。仅登记：页眉页脚（281/36）未收录（全篇系统性版式省略）；χ(X) 的 X、Tr 内 X 等斜体/粗体字形在 md 中偶有混排（不误导）。
- 修复：无。

## p.011（PDF p.11 / 印刷 p.282）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 19:10 EDT。
- PNG：audit-redo/p011.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p011_hc0_affine-11.png、p011_eq28_tilde-11.png（300dpi）。
- 旧审计对照：Luna p.011 = FAIL→已修复（§§2.8-2.11 的 script F 记号、Q_ℓ 记号、Tate twist (-1)）；本次重核修复后状态。
- 核对：où ε=±1 句与 ε 分段式、Grothendieck formulation 句、(2.7)（𝓕(r)=𝓕⊗Q_ℓ(r)）、Théorème (2.8)（𝓕~ le dual；四段链 Tr(x∪y):H^i(X,𝓕)⊗H_c^{2n-i}(X,𝓕ˇ(n))→H_c^{2n}(X,𝓕⊗𝓕ˇ(n))→H_c^{2n}(X,Q_ℓ(n))→Q_ℓ）、(2.9)（foncteur 𝓕↦𝓕_x、(2.9.1) H^0≅𝓕_x^{π_1}）、H_c^{2n}=H^0(𝓕∨(n))^∨=((𝓕_x^∨(n))^{π_1})^∨、invariants/coinvariants 句与 (𝓕_x)_{π_1(X,x)}(−n)、n=1 句、Scholie (2.10)（(i) H_c^0=o、(ii) H_c^2=(𝓕_x)_{π_1}（−1)）、support fini 句、(2.11) 起首。
- 结果：PASS±（修复 1 处）。内容全部吻合；Luna 记号修复生效。印刷双重 dual 记号（(2.8) 行文 𝓕~、(2.8) 式内 𝓕ˇ、(2.9) 起 𝓕∨）在 md 中分别以 ^{\sim}/\vee 投影，忠实保留。修复 1 处：Scholie (2.10)(i) 印刷为「H_c^0(X,𝓕)=o si X est affine」，等号后为小写字母高度 o（p011_hc0_affine-11.png，对照同式 (ii) 的数字 1 高度），零排作 o quirk 首次见于显示式；md 原 0 改回 o。
- 修复：`(2.10)(i) = 0` → `= o`（md 行 396；依据 p011_hc0_affine-11.png）。

## p.012（PDF p.12 / 印刷 p.283）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 19:25 EDT。
- PNG：audit-redo/p012.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p012_caract_E-12.png（300dpi）。
- 旧审计对照：Luna p.012 = FAIL→已修复（(2.12) 的 script F dual 对偶与 twist、(2.13) 的 Z/ℓ^n(1)、书目指引 Q_ℓ、H_c^i、特征零）；本次重核修复后状态。
- 核对：(2.11) 末句（monodromie locale）、Théorème (2.12) 双行链（H^i/H^{2-i} 无 c 下标、j_*𝓕ˇ(1)、j_*(𝓕⊗𝓕ˇ)(1)、=H^2(X,Q_ℓ(1))→Q_ℓ）、(2.13)（racines (ℓ^n)^ièmes）、(2.14) A)-E) 全部引注（VII、XVII 5.1、XIV 1/XVII 5.3、X、XVIII；SGA 5 XV §§1,2；[1]；(1.14.3)/(1.12)；SGA 4 XVIII (3.2.5)、S=Spec(k)）、§3 节标题、Rankin [3] 句、(3.1)（P^1、u point fermé、𝓕_0/𝓕）。
- 结果：PASS±（修复 1 处）。内容全部吻合；Luna 的 (2.12)/(2.13) 修复生效；E) 段末「en caractéristique o」300dpi 终裁为小写 o（p012_caract_E-12.png，同句 modérée/relevant 的 o 同高），属零排作 o quirk——此即 block-1 总评预告的行 426 实例，本次回退 Luna 的 0 并登记。
- 修复：行 426 `en caractéristique 0.` → `en caractéristique o.`（依据 p012_caract_E-12.png）。

## p.013（PDF p.13 / 印刷 p.284）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 19:45 EDT。
- PNG：audit-redo/p013.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p013_iii_det-13.png、p013_F_neq-13.png、p013_geq_o-13.png（300dpi）。
- 旧审计对照：Luna p.013 = FAIL→已修复（script F_0/F 记号、Q_ℓ(r)、行列式恒等算子 I、(3.3) 张量幂 2k、(3.4) 两处张量幂指数）；本次重核发现 Luna 的「行列式恒等算子 I」修复方向相反：印刷为数字 1（形态学标准，p013_iii_det-13.png 同 p.004/p.005 终裁）。
- 核对：poids 定义段（q_x^{β/2}、Q_ℓ(r) poids −2r）、Théorème (3.2) (i) ψ:𝓕_0⊗𝓕_0→Q_ℓ(−β)(β∈Z)、(ii) Sp(𝓕_u,ψ_u)、(iii) det(1−F_x t,𝓕_0)、Alors 句、𝓕≠o 句、Lemme (3.3)（⊗^{2k}、(2k)^ième、det(1−F_x t^{deg(x)},⊗^{2k}𝓕_0)^{-1}）、Tr(F_x^n,⊗^{2k}𝓕_0)=Tr(F_x^n,𝓕_0)^{2k}、(1.5.3) 句、Lemme (3.4) 两处 det、≥o 句、Lemme (3.5)（f_i−1→∞、a_{i,n}≤a_n）、Lemme (3.6) inf 式、rayons 句。
- 结果：PASS±（修复 7 处）。全部内容项吻合；Luna 的 2k/记号修复生效，唯「恒等算子 I」系误判（印刷为 1）。修复：①(iii) I→1；②𝓕≠0→𝓕≠o（p013_F_neq-13.png，小写 o）；③(3.3) 式 I→1；④(3.4) I→1；⑤(3.4) 第二处 I→1；⑥同句 ≥0→≥o（p013_geq_o-13.png，小写 o）；⑦删除 MinerU 捕获的裸页码行「284」（本页页脚）。
- 修复：行 446/450/455/468/470/470/484 共 7 处（详见上）。

## p.014（PDF p.14 / 印刷 p.285）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 20:02 EDT。
- PNG：audit-redo/p014.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p014_hc0_o-14.png、p014_Z_det-14.png、p014_mid_det-14.png（300dpi）、p014_alpha_exp-14.png、p014_ineq_exp-14.png（600dpi）。
- 旧审计对照：Luna p.014 = FAIL→已修复（H_c^2/H_c^0 的张量幂和 Tate twist、极点/倒数/分母标量 1、行列式恒等算子 I 保留）；本次重核：Luna「I 保留」再次方向性错误，印刷为 1。
- 核对：(3.7) 开头与 ψ_P 式、Soit x point fermé de X 句、Zariski-dense 句、H. Weyl 引文（The classical groups, Princeton University Press, chap. VI, § 1）、𝓟′⊂𝓟、同构式 (⊗^{2k}𝓕_u)_{π_1}=(⊗^{2k}𝓕_u)_{Sp}≅Q_ℓ(−kβ)^{𝓟′}、N 句、H_c^2(U,⊗^{2k}𝓕)≅Q_ℓ(−kβ−1)^N、Puisque H_c^0=o 句、Z(U_0,⊗^{2k}𝓕_0,t)=det(1−F*t,H^1(U,⊗^{2k}𝓕))/(1−q^{kβ+1}t)^N、pôle t=1/q^{kβ+1} 句、dans C 句、α^{2k} 句、1/α^{2k/deg(x)} 极点句（600dpi 终裁：印刷指数确含斜杠 2k/deg(x)，md 正确）、两条不等式与 |α|≤q_x^{β/2+1/2k}、Faisant tendre k 句、q_x^β α^{−1} 句、q_x^{β/2}≤|α|、Ceci achève la démonstration.
- 结果：PASS±（修复 3 处）。内容全部吻合；Luna 的标量 1/Tate twist 修复生效。修复：①Puisque 句 H_c^0(U,⊗^{2k}𝓕)=0 → =o（p014_hc0_o-14.png，小写 o）；②Z 式 det(I→1（p014_Z_det-14.png，同式分母标量 1 印刷同形，md 已正确）；③段中 det(I→1（p014_mid_det-14.png）。排除一项 150dpi 误判：α 指数 2k/deg(x) 的斜杠经 600dpi 确认存在，md 无需改。
- 修复：md 行 502/505/508 共 3 处（详见上）。

## p.015（PDF p.15 / 印刷 p.286）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-02 20:14 EDT。
- PNG：audit-redo/p015.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p015_exact_seq_full-15.png、p015_prolong_full-15.png、p015_F_qn-15.png、p015_eq38_det-15.png、p015_det_prod-15.png（300dpi）。
- 旧审计对照：Luna p.015 = FAIL→已修复（行列式恒等算子 I、特征多项式乘积标量 1、rank(script F)、j_!=prolongement par 0）；本次重核：「I」与「par 0」两项均方向相反。
- 核对：Corollaire (3.8) 全段（|α|≤q^{(β+1)/2+1/2}、Z(U_0,𝓕_0,t)=det(1−F*t,H_c^1(U,𝓕))、1/α racine、|t|<q^{−β/2−1}、Soit N le rang、det(1−F_x t,𝓕)=Π_{i=1}^N(1−α_{i,x}t)、|α_{i,x}|=q_x^{β/2}、Σ 系列、|t|=q^{−β/2−1−ε}(ε>0)、=NΣq_x^{−1−ε}、droite affine q^n points（F_{q^n} 经 300dpi 确认印刷即如此，md 正确）、Σ_x q_x^{−1−ε}≤Σ_n q^n·q^{n(−1−ε)}=Σ_n q^{−nε}<∞）、Corollaire (3.9)（P^1_{F_q}/P^1、q^{(β+1)/2−1/2}≤|α|≤q^{(β+1)/2+1/2}）、suite exacte courte o→j_!𝓕→j_*𝓕→j_*𝓕/j_!𝓕→o（第三项为斜线商，md 结构正确）、(j_!=prolongement par o) s'écrit、H_c^1(U,𝓕)→H^1(P^1,j_*𝓕)→o.
- 结果：PASS±（修复 6 处）。修复：①(3.8) 式 det(I→1；②det(1−F_x t,𝓕)=Π 式 I→1（乘积内 (1−α_{i,x}t) 印刷即 1，md 已对）；③正合列两端 0→o ×2（p015_exact_seq_full-15.png：端点为小写字母高度 o，明显低于 j_! 下标的 1；零排作 o quirk 首次见于正合列端点）；④prolongement par 0 → par o（p015_prolong_full-15.png，行文小写 o）；⑤列尾 →0. → →o.（同裁片）。排除一项疑差：F_{q^n} 经 p015_F_qn-15.png 确认印刷如此，md 正确。移交提示：Luna p.029 修复「exact sequences 中的 o 改为 0」与本页同型，该块必须重裁。
- 修复：md 行 549/559/591/594/597 共 6 处（详见上）。

## p.016（PDF p.16 / 印刷 p.287）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-03 19:25 EDT。
- PNG：audit-redo/p016.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p016_dstar_disque-16.png、p016_t_neq_o-16.png、p016_beta_autour-16.png、p016_evanescent-16.png、p016_exact_seq-16.png、p016_table-16.png（300dpi）；p016_evanescent_600dpi-16.png、p016_rfz_underline_600dpi-16.png、p016_x0_finv_600dpi-16.png、p016_x0_subscript_600dpi-16.png（600dpi）。
- 旧审计对照：Luna p.016 = 原逐页 PASS±、closeout 重分类 FAIL（vanishing-cycle 符号表头 I 改为数字 1）；本次重核修复后状态。
- 核对：(3.8)/(3.9) 收尾（H_c^1(U,𝓕) 值 propre、(2.12) 对偶 q^{β+1}α^{-1}、两条 |α|≤q^{(β+1)/2+1/2}. 与 |q^{β+1}α^{-1}|≤q^{(β+1)/2+1/2}、et le corollaire）、§4 节标题、(4.1) 与 D={z||z|<1}/D*=D−{o}/f:X→D、a)-d)（non singulier n+1、propre、X_0=f^{-1}(o)、point quadratique non dégénéré）、t≠o 与 X_t=f^{-1}(t) « la » fibre générale、α) 专化 sp 与左向同构链 H^i(X_0,Z)≃←H^i(X,Z)→H^i(X_t,Z);、β) 单值 T 与 « faire tourner t autour de o »、système local R^i f_* Z̲|D*、π_1(D*,t)、cycle évanescant δ∈H^n(X_t,Z)、(i≠n, n+1) 同构式、正合列 o→H^n(X_0,Z)→H^n(X_t,Z)→^{x↦(x,δ)}Z→H^{n+1}(X_0,Z)→H^{n+1}(X_t,Z)→o.、Tx=x±(x,δ)δ、n mod 4 符号表 4 行 4 列（o ı 2 3 / −−++ / 2 o −2 o / −δ δ −δ δ）。
- 结果：PASS±（修复 9 处）。内容全部吻合；Luna 的表头 I→1 经原页确认正确（本印刷体数字 1 无左旗窄干形态）。零排作 o quirk 本页 6 处确证（300dpi 比高法：与同式/同表数字 2、3 比高）：D*=D−{o}、f^{-1}(o)、t≠o、autour de o、正合列两端、表头与 (δ,δ) 行三零。新发现 3 项漏录：①「cycle évanescant」拼写（600dpi 裁片 p016_evanescent_600dpi-16.png，-scant 非 -scent），MinerU 误规范化为 évanescent，改回印刷原样（行 680/782 同词属 p.017/p.018 块，各自裁决）；②α) et β) 右括号漏录，补录；③R^i f_* Z̲ 的 Z 带下划线（local system 记号），补 \underline{\mathbf{Z}}。登记不改：X_0 下标零为加粗窄椭圆形态（600dpi p016_x0_subscript_600dpi-16.png），与全尺寸圆 o 形态有别且同页无同字号下标参照零，按 p.001-015 惯例保留 0；display 内 X 粗体/正体混排为字体投影不误导；页眉页脚 287 未收录（全篇系统性版式省略）。
- 修复：①`$D^{*}=D-\{0\}$`→`\{o\}`（行 618；p016_dstar_disque-16.png）；②`f^{-1}(0)`→`f^{-1}(o)`（行 624；同上+600dpi p016_x0_finv_600dpi-16.png）；③`$t \neq 0$`→`$t \neq o$`（行 628；p016_t_neq_o-16.png）；④« autour de 0 »→« autour de o »（行 636；p016_rfz_underline_600dpi-16.png）；⑤`f$_{*}$Z|D\*`→`f$_{*}$$\underline{\mathbf{Z}}$|D\*`（行 636；同上）；⑥`décrit $\alpha$ et $\beta$`→`décrit $\alpha$) et $\beta$)`（行 638；p016_evanescent_600dpi-16.png）；⑦`cycle évanescent`→`cycle évanescant`（行 638；同上）；⑧正合列两端 `0`→`o` ×2（行 647；p016_exact_seq-16.png）；⑨表头 `\text {0}`→`\text {o}` 与 (δ,δ) 行 `& 2 & 0 & - 2 & 0`→`& 2 & o & - 2 & o`（行 659；p016_table-16.png）。
- **勘误（2026-10-03 20:20 EDT，p.019 块审计回溯发现）**：本条目修复⑦「évanescent→évanescant」系 600dpi 单倍缩放读图误判，属本次重做引入的错误。600dpi×3 放大终裁（audit-redo/300dpi/p016_evanescent_word_600dpi-16.png）：该词为斜体，第 8 字母为带横杠的斜体 e，与第 3 字母单层斜体 a 形态迥异，印刷为「évanescent」；pdftotext OCR 文本层同读 évanescent。已回退 md 行 638 为 évanescent（erratum commit）。本页其余修复（α)/β) 括号、Z̲ 下划线、六处 o/0 系列、裸页码等）经同批 3x 复核不受影响。方法论修订：斜体/罗马小写 a/e 在 ≤2x 缩放下易混淆，凡据此二字形的拼写裁决必须 ≥3x 放大并附 OCR 交叉核对，方可改动拼写。

## p.017（PDF p.17 / 印刷 p.288）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-03 19:40 EDT。
- PNG：audit-redo/p017.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p017_eq421_sp_iso-17.png、p017_evanescent-17.png、p017_eq432_iso-17.png、p017_eq433_seq-17.png、p017_atell_action-17.png、p017_xmapsto_action-17.png（300dpi）；p017_faisceaux_600dpi-17.png（600dpi）。
- 旧审计对照：Luna p.017 = FAIL→已修复（专化映射改左向同构箭头；Z_ℓ(1)）；本次重核修复后状态。
- 核对：页首单值 T 保交叉形式段（Tr(x∪y)、transvection symplectique/symétrie orthogonale）、(4.2) 全段（disque D→hensélien A、S/η/s、η̄）、Soit f:X→S 段（X_s、ℓ≠p、X_η̄）、(4.2.1) sp:H^i(X_s,Q_ℓ)≃←H^i(X,Q_ℓ)→H^i(X_η̄,Q_ℓ).、inertie I=Gal(η̄/η) 段、(4.2.2) I→GL(H^i(X_η̄,Q_ℓ)).、Les données 段（faisceaux R^i f_*Q_ℓ sur S）、(4.3)（n=2m/2m+1、cycle évanescant）、(4.3.1) δ∈H^n(X_η̄,Q_ℓ)(m).、(4.3.2) H^i(X_s,Q_ℓ)≃→H^i(X_η̄,Q_ℓ)(i≠n,n+1).、(4.3.3) 正合列 o→…→Q_ℓ(m−n)→…→o.（x↦Tr(x∪δ)）、L'action (4.2.2) 段、A) n impair（t_ℓ:I→Z_ℓ(1),、σ∈I、x↦x±t_ℓ(σ)(x,δ)δ.）。
- 结果：PASS±（修复 3 处）。内容全部吻合；Luna 两项修复经原页确认正确（(4.2.1) 同构箭头确为左向，300dpi 裁片；Z_ℓ(1) 无误）。新发现：①(4.3) 行「cycle évanescant」拼写（p017_evanescent-17.png，-scant），与 p.016 同型误规范化，改回；②(4.3.3) 正合列两端印刷为小写 o（p017_eq433_seq-17.png，与 H 比高），md 0 改回 o；③MinerU 捕获的裸页码行「288」（本页页脚）夹在「et l'action de σ∈I est」与其 display 之间，按 275/277/279/284 同类处置删除。登记不改：faisceaux R^i f_*Q_ℓ 的 R 正体/Q 粗体在 md 作斜体（600dpi p017_faisceaux_600dpi-17.png 确认印刷无下划线，纯字体投影）；页内竖直细线为扫描划痕非印刷内容（见 p017_atell_action-17.png 的 I 处）；页眉 PIERRE DELIGNE/288 未收录（系统性版式省略）。
- 修复：①`cycle évanescent`→`cycle évanescant`（行 680；p017_evanescent-17.png）；②(4.3.3) 两端 `0`→`o` ×2（行 697；p017_eq433_seq-17.png）；③删裸行「288」（原行 710；与 277/284 同类版式家具）。
- **勘误（2026-10-03 20:20 EDT，p.019 块审计回溯发现）**：本条目修复①系与 p.016 同源的读图误判（300dpi 单倍）。600dpi×3 放大终裁（audit-redo/300dpi/p017_evanescent_word_600dpi-17.png）：罗马体下第 8 字母为带横杠的 e，与第 3 字母双层 a 迥异，印刷为「évanescent」；OCR 层同读。已回退 md 行 680 为 évanescent（erratum commit）。本页其余修复（(4.3.3) 两端 o、裸页码 288）不受影响。

## p.019（PDF p.19 / 印刷 p.290）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-03 20:55 EDT。
- PNG：audit-redo/p019.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p019_ces_lacets-19.png、p019_diagram-19.png、p019_theoreme54-19.png、p019_rfz_tight_600dpi-19.png、p019_evanescent_word_600dpi-19.png（后者已在 erratum commit 提交）。
- 旧审计对照：Luna p.019 = PASS±，未改正文，称环路图与 PDF 原图相符；本次重核确认其图核对结论，但发现图链悬空与其未检的 3 处问题。
- 核对：Fixons X 段、A) transverse/éclatement、B) partie finie S 与 x_s∈X_s、C) points critiques non dégénérés、(4.1) 应用句（D_s、f^{-1}(D_s)）、(5.2)（U=D−S、lacets disjoints (γ_s)、autour de s）、环路图（三环路自基点 u、两环内 ×、一环内 ×_s、标 γ_s；MinerU 图 page_18_image_6.jpg 与印刷图逐元素一致）、Ces lacets 段（π_1(U,u)、R^i f_* Z|U 无下划线、cycle évanescent δ_s∈H^n(X_u,Z)）、(5.2.1) γ_s x=x±(x,δ_s)δ_s.、Soit E 段（H^n(X_u,Q)、partie évanescente）、Proposition (5.3)（全句斜体、E^⊥、Tr(x∪y)、invariants）、Les γ_s 句、Théorème (5.4)（全句斜体、évanescents 复数、±δ_s、π₁(U,u)）、Soit X̌⊂P̌ 段至 « La variété X̌ est irré- »（跨页连字符，续 p.291）。
- 结果：PASS±（修复 3 处）。①行 776 图链悬空 `images/page_18_image_6.jpg` → `Deligne_1974_weil1/images/page_18_image_6.jpg`（p.007 同类修复；图内容经与本页印刷环路图逐元素核对一致后修复）。②行 778 `\mathbb{R}^{i}f_{*}\mathbf{Z}|\mathbf{U}` → `\mathrm{R}^{i}…`：600dpi×3（p019_rfz_tight_600dpi-19.png）确证印刷为正体衬线 R 且 Z 无下划线（与 p.016 行 636 的 Z̲ 带下划线成对照），黑板体属字形类错误，按 Luna p.018 double-struck D→D 修复方向处置。③行 790 `±δs` → `$\pm\delta_{s}$`：MinerU 下标拉平伪影，按 p.008 dfn 下标结构恢复先例修复。**évanescant 勘误与本案**：本页行 778 单数与行 790 复数印刷均为 évanescent/évanescents（600dpi×3 p019_evanescent_word_600dpi-19.png + p019_theoreme54-19.png；OCR 层一致），md 原文正确、未改动——并据此推翻本 redo p.016/p.017 的 évanescant 修复（见各条目勘误与 erratum commit 02c470de）。登记不改：Prop (5.3)/Théorème (5.4) 印刷整句斜体、md 正文体（斜体排版投影）；(5.3) 内 π₁(U,u)/H^n(X_u,Q) 的粗体在 md 作斜体（混排不误导）；行 790 的 π₁ 用 Unicode 下标 ₁（渲染正确，保留）；页眉 290/PIERRE DELIGNE 与页脚 290 未收录（系统性版式省略）。
- 修复：①图链补嵌套目录前缀（行 776；audit-redo/300dpi/p019_diagram-19.png + MinerU page_18_image_6.jpg 内容比对）；②`\mathbb{R}`→`\mathrm{R}`（行 778；p019_rfz_tight_600dpi-19.png）；③`±δs`→`$\pm\delta_{s}$`（行 790；p019_theoreme54-19.png）。

## p.020（PDF p.20 / 印刷 p.291）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-03 21:15 EDT。
- PNG：audit-redo/p020.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p020_gamma_x-20.png、p020_f_eoplus_c-20.png、p020_x_delta_neq-20.png、p020_s_dcap_xcheck-20.png、p020_xt_xcheck-20.png（300dpi）。
- 旧审计对照：Luna p.020 = FAIL→已修复（incidence variety 改 X×dual P；(5.4) dual 记号改 dual P/dual X；(5.6) 参数线 double-struck D 改 D）；本次重核修复后状态。
- 核对：«ductible.» 跨页续接（p.019 «irré-»）、Soit Y⊂X×P̌ 段、g-图（X←Y、g↓、P̌）、La fibre de g 段、On retrouve 段（S=D∩X̌ 300dpi 确证 caron）、π₁(D−S,u)→π₁(P̌−X̌,u)、est surjective 段、Pour x dans le lieu lisse 全段（ch、γ_x、« En particulier, les γ_s sont conjugués entre eux »——300dpi 确证印刷即下标 s，与同句 γ_x 并存，MD 正确）、Corollaire (5.5)（整句斜体投影）、Soit F⊂E⊗C 段（两处 ⊗ 经 300dpi 确证为圈乘、⊄、(x,δ_s)≠o 小写 o）、γ_s x−x=±(x,δ_s)δ_s∈F,、et δ_s∈F 段、(5.6)、Soient P 段（(H_t)_{t∈D}、« les X_t, X̃ et le diagramme (5.1.1) »——300dpi 确证独立 X 上为波浪号 X̃（指 (5.1) 的 incidence 空间），MD \widetilde{\mathbf{X}} 正确）、A) L'axe 段（X̃）。
- 结果：PASS±（修复 1 处）。内容全部吻合；Luna 的 incidence/dual 记号修复方向经本页上下文确认成立。零排作 o quirk 本页 1 处：(x, δ_s)≠o（p020_x_delta_neq-20.png，与括号高度比）。登记不改：Corollaire (5.5) 与 « pinceau de Lefschetz » 印刷斜体、md 正文体；π₁(U,u) 的粗体 U；行 808 句点前多一空格「`$ .`」（排版微瑕，按 p.005 残留微差异惯例登记不改）；页眉/页脚 291 与页内竖直扫描划痕未收录。
- 修复：`$(x, \delta_s) \neq 0$`→`$(x, \delta_s) \neq o$`（行 814；p020_x_delta_neq-20.png）。

## p.018（PDF p.18 / 印刷 p.289）
- 身份/时间：actor=Wf-R-P01; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）; 2026-10-03 19:55 EDT。
- PNG：audit-redo/p018.png（pngmono 150dpi）；仲裁裁片 audit-redo/300dpi/p018_a_si_delta-18.png、p018_b_si_delta-18.png、p018_seq_ql-18.png（300dpi）；p018_ou_faisceau_600dpi-18.png（600dpi）。
- 旧审计对照：Luna p.018 = FAIL→已修复（inertia character 值域与值 {±1}/1/−1；pencil 参数线 double-struck D 改 D）；本次重核修复后状态。
- 核对：B) n pair 全段（p≠2、caractère d'ordre deux、ε:I→{±1},、σx=x si ε(σ)=1 / σx=x±(x,δ)δ si ε(σ)=−1.）、Les signes ± 句、(4.4) a) Si δ≠o（1) i≠n 常值、2) j:η↪S 与 Rⁿf_*Q_ℓ=j_*j*Rⁿf_*Q_ℓ.）、b) Si δ=o（cas exceptionnel、(δ,δ)=±2、1) i≠n+1 常值、2) Q_ℓ(m−n)_s 与正合列 o→Q_ℓ(m−n)_s→R^{n+1}f_*Q_ℓ→j_*j*R^{n+1}f_*Q_ℓ→o,）、où 句、§5 节标题、(5.1) 全段（P/P̌、H_t、D⊂P̌、pinceau d'axe A）、Soit X⊂P 段、(5.1.1) 交换图（X←^{π}X̃、f↓、D）、La fibre 段（X_t=X∩H_t）。
- 结果：PASS±（修复 5 处）。内容全部吻合；Luna 的 ε 值域修复确认生效。零排作 o quirk 本页 3 处确证（300dpi 比高法）：Si δ≠o、Si δ=o、正合列两端（p018_seq_ql-18.png 与 H/R 比高）。新发现文本错误 1 处：行内「où j_*j*…」md 作 `\mathrm{ou}`（漏抑音符，600dpi p018_ou_faisceau_600dpi-18.png 确证印刷为 où），「or/where」语义有别，移出 math 并补为 où。登记不改：ε display 的 I、R^i f_*Q_ℓ 的 R/Q 在印刷为粗体、md 作 \mathrm{I}/斜体（字体投影）；(5.1.1) 图 md 以 array 投影、结构与印刷一致（π 左箭头、f 下箭头）；页脚绑定号 37 与页眉页脚 289 未收录（系统性版式省略，与 p.002 装订号 35 同）。移交澄清：行 778 悬空图链 `images/page_18_image_6.jpg` 位于 (5.2) 段，该段属印刷 p.290（PDF p.19）内容，归 p.019 块修复；MinerU 图名为 0 基页号（page_18=PDF p.19），与 p.007 的 page_6=PDF p.7 一致。
- 修复：①`$Si \delta \neq 0$`→`$Si \delta \neq o$`（行 730；p018_a_si_delta-18.png）；②`$\delta = 0$`→`$\delta = o$`（行 740；p018_b_si_delta-18.png）；③正合列两端 `0`→`o` ×2（行 747；p018_seq_ql-18.png）；④`$\mathrm{ou} j_{*}j^{*}…$`→`où $j_{*}j^{*}…$`（行 750；p018_ou_faisceau_600dpi-18.png）；⑤删裸行「289」（原行 764；同类版式家具）。
