# AUDIT — Quillen handwritten notes (Hikes, 66 pages)

## 元数据与范围

- Actor：`Peer-P27`
- Model / effort：`gpt-6-luna / max`
- 角色：`CONTRIBUTOR`；唯一 canonical integrator：`Master-Luna`
- 基线：`037602429d3b009f6fc468c732073eb3ddf9875f`（worktree 初始 HEAD；detached）
- PDF（只读）：`Quillen_handwritten_notes_Hikes_66p.pdf`；`pdfinfo` 页数 66；SHA-256 `fd6b4642c6f93d47fd789bdd1924e5a8a8b97aa39ecd1b23d9673d934f015786`
- MinerU Markdown（初始快照）：`Quillen_handwritten_notes_Hikes_66p_mineru/Quillen_handwritten_notes_Hikes_66p__Quillen_handwritten_notes_Hikes_66p.md`；2418 行、84498 bytes；SHA-256 `7cf936373447fd016ac6b94ec87b5fcba4092df74d5c3399ea52dda4b140047d`
- PDF 类型：扫描件。`pdftotext -layout` 输出仅 66 个分页符、无正文文字；因此按全页图模式逐页检查。
- MinerU 来源元数据：`middle_json.json` 显示 MinerU 3.4.4、tier `basic`、parse_mode `ocr`，66 页；所检查的 `middle_json.json` 与 `structured_content.json` 均未提供 `doc_id` 字段，故记录为 `UNKNOWN / NOT EXPOSED IN SOURCE BUNDLE`。
- 方法：逐页以 Ghostscript `pngmono` 150dpi 渲染、目检原图并对照 Markdown；字形无法由 150dpi 唯一判定时另存本篇前缀 300dpi 裁片。PDF 与其余 MinerU 导出资产保持只读。
- 状态：逐页审计进行中；本文件与图片属于候选证据，尚未集成至 canonical `main`。

## 逐页审计

### p.001（PDF p.1 / 纸面圈号 1）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p001.png`（pngmono 150dpi）
- 核对：课程标题、讲者与笔记署名、环设定、`K_0 A` / `K_1 A` 定义、acyclic/aspherical 定义及 Whitehead 相关陈述。
- 结果：**FAIL**。
- 印刷证据与差异：原图在标题与定义之间写有 `A ring.`，MinerU 正文漏录；原图明确写 `X acyclic ⇒ π_1(X) is perfect (by Poincaré)`，MinerU 基线第 25 行写为 `X cyclic`，改变了断言。末句 `X acyclic and simply connected ⇒ X ~ * (by Whitehead.` 另有未闭合括号；待修复阶段据原文统一标点。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；修复后按该页原图复核。
- 记录：2026-10-01 16:22:31 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.002（PDF p.2 / 纸面圈号 2）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p002.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p002_pullback.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p002_lower-right.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p002_hofiber-notation.png`。
- 核对：简单非交换群与有限无环多面体问题；acyclic map 的等价条件；路径空间构造及同伦纤维；局部系数同调映射；普遍覆盖的拉回与证明开头。
- 结果：**FAIL**。
- 印刷证据与差异：300dpi 裁片确认证明开头是 `(i) ⇒ (ii)`，而 Markdown 基线第 57 行为 `(ii) ⇒ (ii)`。纸面公式为 `(p_2)_*: H_*(X ×_Y \widetilde Y) → H_*(\widetilde Y)`，Markdown 基线第 53 行省略 `×` 的下标 `Y`，把纤维积写成普通积。纸面路径空间构造为 `X ×_Y Y^I`，并将固定 `y` 的同伦纤维写为 `X ×_Y Y^I_y`；Markdown 基线第 38、40 行丢失/错置该纤维积与路径端点记号，并带入噪声 `y.3`。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；修复后回看上述 150dpi 页图与 300dpi 原图裁片。
- 记录：2026-10-01 16:28:39 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.003（PDF p.3 / 纸面圈号 3）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p003.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p003_spectral-sequence.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p003_covering-homology.png`。
- 核对：Serre 谱序列、通用系数公式、局部系数限制、普遍覆盖上的同调映射、覆盖空间图及证明衔接。
- 结果：**FAIL**。
- 印刷证据与差异：原图的谱序列为 `E^2_{p,q}=H_p(Y,H_q(F;i^*L')) ⇒ H_{p+q}(X,L')`，Markdown 基线第 67 行把两个指标错写成 `i,g` / `g,g`，并将总次数写成 `p+g`。原图的通用系数项为 `Tor_1(H_{q-1}(F),A)` 且条件是 `F` acyclic；基线第 72 行把 `A` 塞入 `H_{g-1}(F,A)` 并写成 `F ≥ cyclic`。原图第 90 行所对应的图包含 `π=π_1Y`、`H_*(X×_Y \widetilde Y)→H_*(\widetilde Y)` 及覆盖映射，Markdown 将这些记号和映射压成无法按原图读取的表达。基线第 103–108 行又把交换图/同调与同伦序列衔接压平，并把纸面 `p_2` 误识为 `β r_2`、`same fiber` 误成 `some fiber`；这些差异影响本页证明的对象和推理关系。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；按上述 150dpi 与 300dpi 原图证据回核。
- 记录：2026-10-01 16:30:55 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.004（PDF p.4 / 纸面圈号 4）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p004.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p004_fibration.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p004_pullback.png`。
- 核对：以普遍覆盖拉回替换 `f` 的论证；`(ii) ⇒ (i)` 的路径空间同伦纤维与两条 Serre 谱序列；无环映射的复合与拉回性质。
- 结果：**FAIL**。
- 印刷证据与差异：原图第 110 行的 `p_2` 定义包含 `X×_Y \widetilde Y`，Markdown 基线行 110 写成 `X_x \widetilde Y`，丢失乘积与基底下标。原图的同伦纤维为 `PY_y×_Y X`，基线行 112、114 丢失拉回下标 `Y`。原图第二个谱序列的系数空间是 `\Omega Y`，基线行 120 误为 `RY`。本页拉回方块原图也是 `Y'×_Y X`，基线行 133 漏掉 `×_Y`；这些符号决定所用空间/映射，不能作为纯排版差异处理。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；修复后按 150dpi 页图与 300dpi 裁片复核。
- 记录：2026-10-01 16:33:00 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.005（PDF p.5 / 纸面圈号 5）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p005.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p005_pushout.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p005_relative-homology.png`。
- 核对：沿 cofibration 的推前保持 acyclic 的方块与相对同调证明；局部系数 Whitehead 定理；闭流形同调球的定向与基本类例子。
- 结果：**FAIL**。
- 印刷证据与差异：原图推前目标为 `Z∪_X Y`，基线第 139 行把该 pushout 写成不可读的 `Z U(Y)/X L`；第 143–149 行的局部系数/相对同调交换图也被识别成 `f(y)`、`z_i f_i` 等不对应原式的文本。原图 Whitehead 定理要求 `π_1(f):π_1X→π_1Y` 为同构，基线第 151 行把下标 1 识别为逗号；基线第 153–155 行的普遍覆盖、`H_*` 同构和 Whitehead 拼写均有错误。原图将基本类 `μ` 送到 canonical generator，基线第 160 行只留残缺 `genera`；第 162 行把 `acyclic map` 写成 `cyclic map`，改变映射性质。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；按 150dpi 页图及两张 300dpi 原图裁片复核。
- 记录：2026-10-01 16:35:05 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.006（PDF p.6 / 纸面圈号 6）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p006.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p006_poincare-sphere.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p006_classification.png`。
- 核对：Poincaré 同调 3-球面的两个群商表示；固定源的 acyclic map 分类；perfect normal subgroup 的实现；`π_1` kernel 的加强命题。
- 结果：**FAIL**。
- 印刷证据与差异：原图把 `SO(3)` 的商标为 icosahedron symmetry group，并将 `S^3` 的商标为 binary icosahedral group；Markdown 基线第 164 行把分母写成 `icosahedral_1`，且没有保留这两个群的对应记号。原图定理 (ii) 明写存在 `acyclic map f:X→Y`，基线第 176 行将其误成 `on 24c map`。原图 Remark 5 说 acyclic `f` 的 `π_1(f)` 满射且 kernel perfect，基线第 178 行误为 `cyclic` 并损坏了 `π_1` 下标。基线第 191 行又把 “maps over Z” 误成 “crops over Z”。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；对群商、性质名及 `π_1` 记号按 300dpi 裁片复核。
- 记录：2026-10-01 16:37:07 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.007（PDF p.7 / 纸面圈号 7）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p007.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p007_van-kampen.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p007_mapping-cone.png`。
- 核对：pushout 方块上的 Van Kampen 计算；acyclic map 分类证明中由 `π_1X` 生成元构造 mapping cone；附带的 mapping-cone 同调序列。
- 结果：**FAIL**。
- 印刷证据与差异：原图 pushout 是 `Z∪_X Y`，Van Kampen 给出 `π_1(Z∪_X Y)=π_1(Z)*_{π_1X}π_1(Y)`，并在 kernel 假设下化为 `π_1(Z)`；Markdown 基线第 193、195 行的商空间记号无法还原原式，并把 amalgamated free product 误成直接积 `×`。构造使用生成 `π_1X` 的映射 `f_i:S^1→X`，基线第 205、208 行把 `S^1` 写成 `S'`。第 210、212 行的 attaching-map / mapping-cone 与 `π_1X'=0` 记号也有损坏，需按本页裁片修复。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；修复后核对 pushout、自由积粘合下标、`S^1` 与长正合序列。
- 记录：2026-10-01 16:39:13 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.008（PDF p.8 / 纸面圈号 8）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p008.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p008_hurewicz-cones.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p008_general-case.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p008-general-pushout-group.png`。
- 核对：Hurewicz 后的二维同调分解、用 3-胞腔杀去 `H_2` 的 mapping-cone 构造、相应长正合序列，以及一般 perfect normal subgroup 的覆盖空间/推前构造。
- 结果：**FAIL**。
- 印刷证据与差异：原图给出 `H_2X' ≅ H_2X ⊕ ⊕_{i∈I} Z`，再沿映射 `∨g_i:∨S^2→X'` 附着 3-胞腔；基线第 224、226 行把下标、直和项、球面楔和 attaching map 损坏成无法按原图读取的符号。原图第 230 行收束为 `ker(π_1(f))=N`，基线丢失 `π_1` 下标。一般情形原图第 232 行写覆盖空间 `X_0'` 且 `π_1(X_0')=N`，基线截断/错置其下标；第 234 行把带粘合子群的 Van Kampen 表达式识别为直接积。纸面该等式右端清晰写作 `N`，其数学含义在此不作推测性改写，作为源级 print quirk 保留。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；源级 print quirk 保留原样并在总评列明。
- 记录：2026-10-01 16:42:14 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.009（PDF p.9 / 纸面圈号 9）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p009.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p009_plus-product.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p009_examples.png`。
- 核对：`X⁺` 的定义与函子/积性质；`π_1` 商群计算；acyclic 空间与同调球例子；Poincaré 同调 3-球面的 `G` 与 `\widetilde G` 记号。
- 结果：**FAIL**。
- 印刷证据与差异：原图 `X⁺` 定义杀去 `π_1X` 中最大 perfect subgroup；基线第 244 行把 `π_1X` 的下标识别为逗号。原图同调球例子给出 collapsing map `X→S^n` 后 `X⁺≃S^n`，基线第 285 行把这个结论损成 `${S}_0${X}^+∼S^n`。Poincaré 例子原图明确区分 `G`（icosahedron symmetries，`A_5`，阶 60）与 `\widetilde G`（binary icosahedral group，阶 120）；基线第 287–289 行把商群名称和符号混在一起。基线第 283 行也把原图 `H_*(X)=H_*(S^n)` 的星号识别为 `x`。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；群商与同调球例子按 300dpi 裁片复核。
- 记录：2026-10-01 16:44:22 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.010（PDF p.10 / 纸面圈号 10）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p010.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p010_BG-fibration.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p010_eilenberg-maclane.png`。
- 核对：`B\widetilde G≃K(\widetilde G,1)` 的起点及纤维图；同伦群与同调群的 Eilenberg–MacLane 空间公式；`[X,K(A,n)]≅H^n(X,A)` 及 Hurewicz 映射引出的 Hom/Ext 短正合序列起始。
- 结果：**FAIL**。
- 印刷证据与差异：原图对象是 `B\widetilde G≃K(\widetilde G,1)`，基线第 293–294 行丢了 `B` 上的波浪号并把 `,1` 错成下标。原图使用 `K(A,n)`（Eilenberg–MacLane space），基线第 308、311、317、320、323 行反复写成 `H(A,n)`；这改变了后续 `π_q`、`[X,K(A,n)]` 与 Hurewicz 断言的对象。基线第 304 行也把原图的 `H_*(α)` / `H_*(β)` 误作 `H_x` / `H_y`，第 306 行把 `(B\widetilde G)^+` 的波浪号位置错置。第 314 行 `H_{n+1}` 的下标另被误识为 `H_{k+1}`。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；按两张 300dpi 裁片核对群对象、空间符号和上下标。
- 记录：2026-10-01 16:46:17 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。

### p.011（PDF p.11 / 纸面圈号 11）

- PNG：`audit/Quillen_handwritten_notes_Hikes_66p_p011.png`（pngmono 150dpi）
- 300dpi 终裁裁片：`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p011_UCT-map.png`、`audit/300dpi/Quillen_handwritten_notes_Hikes_66p_p011_Dror-tower.png`。
- 核对：UCT 的 `Ext^1→H^n→Hom` 序列；`K(A,n)` 的表示性质与 Hurewicz 映射；Dror tower 的覆盖空间、低维约化同调条件、纤维和下一阶段的诱导映射。
- 结果：**FAIL**。
- 印刷证据与差异：UCT 原图写 `Ext^1(H_{n-1}X,A)`，基线第 335 行将上标 1 识别为 prime。原图整页均使用 Eilenberg–MacLane 空间 `K(A,n)`，而基线第 338、340、365 行写 `H(A,n)`，第 343 行又把自然映射 `ρ` 识别成 `H''`。塔构造原图明确给出 `\widetilde H_qX_n=0`（`q<n`），基线第 355 行漏掉该条件；原图令 `A=H_n(X_n)` 并构造 `X_n→K(H_nX_n,n)`，基线第 368 行写成 `H_n(X_0)` 和 `H(H,X_0,n)`，其后第 371 行也把 `K` 错成 `H`。
- 修复状态：待全篇审计完成后，使用 Edit/apply_patch 逐处修复；按两张 300dpi 裁片回核上下标、K/H 字形和塔的 stage index。
- 记录：2026-10-01 16:48:10 -0400；actor=`Peer-P27`；model=`gpt-6-luna`；effort=`max`。
