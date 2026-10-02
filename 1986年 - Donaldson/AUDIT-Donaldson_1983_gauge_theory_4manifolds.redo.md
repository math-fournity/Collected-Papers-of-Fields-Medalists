# AUDIT-REDO — Donaldson 1983, “An Application of Gauge Theory to Four-Dimensional Topology”

- 性质：**Luna 审计重做**。用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检；Luna 旧修复（`fix(md)` commit `9717b16`，修复后 md SHA `a22812e1…`）一并重核，不再默认其结论正确。
- Actor：`Wf-R-P03`（dynamic-workflow Sub Agent，单篇互斥 worktree `cpf-redo-Donaldson_1983_gauge_theory_4manifolds`，分支 `cpf-redo/Donaldson_1983_gauge_theory_4manifolds`）。
- Host / model / effort：`zcode` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`（run 级配置转述；实际生效 effort **自报 UNKNOWN**，无法从 runtime 直接证明）。
- PDF：`Donaldson_1983_gauge_theory_4manifolds.pdf`，38 页，SHA-256 `5a5201ed38b870ec1ad183b697aa505830c5a35bf03d72614a5bb1667fe65080`（本 worktree 实测）。
- 被检 Markdown 基线：`Donaldson_1983_gauge_theory_4manifolds_mineru/Donaldson_1983_gauge_theory_4manifolds__Donaldson_1983_gauge_theory_4manifolds.md`，1,449 行，SHA-256 `a22812e11e24ebbddde35767b454a47957949df592d97b72a689568b83eb74a5`（= Luna fix 后的基线；原始 mineru 产出见历史 commit `0b0f3dd`）。
- 开工时间：2026-10-02 14:33 EDT；本文头最后更新 2026-10-02 14:51 EDT。
- 文本层判定：`pdftotext -f 1 -l 1` 成功返回首页全文（exit 0；ABBYY FineReader OCR 层，2008 年生成）→ **文本层可用，本篇采用双通道主对账**：150dpi pngmono 页图为印刷原文裁决源，pdftotext 文本层仅作第二通道交叉定位/比对；文本层自身有 OCR quirk（如 `E₈`→`£ 8`、连字符丢失），一律以页图为准。
- 方法：每页 `gs -q -dNOPAUSE -dBATCH -sDEVICE=pngmono -r150` 渲染 `audit-redo/p0NN.png` → Read 目检 → 与 Markdown 对应段五点比对（题录 / 节标题顺序 / 定理编号与陈述 / 公式与上下标 / 记号；文末页逐条参考文献与收稿日期）→ PASS / PASS± / FAIL 分级 → 内容错误用结构化 `Edit` 逐处修复（含修正 Luna 旧修复中的错误；print quirk 忠实登记不改）→ 本文件落签该页条目 → 仅 add 本篇路径后按 `redo(page)` 提交。
- 纪律：PDF 原页为唯一裁决源；不写根级任何文件；不动旧 `audit/` 与旧 `AUDIT-Donaldson_1983_gauge_theory_4manifolds.md`（只读参照）；不碰其他论文目录；不 push。

## 本块进度（Wf-R-P03）

- **p.1–p.9 / 38 已完成**（2026-10-02）：9 页全部 PASS±，无 FAIL。逐页一提交：`51587b6f`(p.001)→`3d799f4e`(p.002)→`12974a11`(p.003)→`ae90de97`(p.004)→`4ef9d908`(p.005)→`95209199`(p.006)→`02c79dd4`(p.007)→`42b69e9d`(p.008)→`498796b0`(p.009)。
- 本块对 md 共 14 处修复（含 1 处 Luna print-quirk 静默改正的复原）：全部见各页「修复登记」；`git diff 8aa00fdd` 复核与登记一一对应，无未登记差异。
- 基线后 md SHA-256（本块结束时）：`755e65dc126cde99ed7f870f8a26a6434ca665199b34951d2f3a62622d4f1f25`。
- 跨页系统性发现（供后续页沿用）：① 逐页 running head/页码省略（登记于 p.002，不逐页补录）；② 同一花体字形在 md 中 H/K 混排（本文定为 harmonic 空间 $\mathcal{H}$，p.7/8/9 已统一，后续页遇 `\mathcal{K}` 同规则）；③ 草书 𝒬/𝒢、Fraktur 𝔤/𝔅 拍平为普通字母是 Luna 基线的高发缺陷（p.3/4/8/9 连续出现，后续页需重点盯）；④ 叠置记号（P↓S⁴ 型三行叠置）易被错位转写（p.6 一例）；⑤ 印刷原样错字已登记两处："so in some base"（p.2）、"complex lie bundles"（p.9）、`F(I_{0,λ})` 分母 `(λ²+|x|)²`（p.7）、式(2) `dμ.` 多余句点（p.6）。
- p.10 起 Theorem 6 一带可见残留普通字母 B/B*（行 329），属下一块范围，届时按本块字形规则处理。

## 页级条目

### p.001（PDF p.1 / 印刷 p.279，首页无单独页码数字）

- PNG：`audit-redo/p001.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（节标题、期刊行，临时中转，结论记于本条）
- 核对：题录（期刊卷期页码行、标题、作者、Received 脚注）；节标题 I.1；正文段落与 cup-square 公式；$E_8$；引用编号 [7][8][11][12][22]
- 结果：**PASS±**。
  - Luna 基线确实缺印刷期刊行 `J. DIFFERENTIAL GEOMETRY 18 (1983) 279–315`（grep 无 `DIFFERENTIAL`/`279` 命中）——**本次已用 Edit 在标题前补入该行**；题录五行余项（标题/作者/脚注日期）逐字吻合。
  - 节标题 300dpi 仲裁：印刷为罗马数字 `I.1 Introduction`（首字符为带衬线大写 I，非阿拉伯 1）；md `I.1` 正确，Luna 未动亦未改错。
  - cup-square 公式 $Q\colon H^2(X;\mathbf{Z})\to H^4(X;\mathbf{Z})\cong\mathbf{Z}$ 与页图一致；`$E_8$` 正确（pdftotext 文本层作 `£ 8`，系 OCR quirk，md 不采纳）。
  - 排版级伪影（登记不改）：印刷斜体 *smooth*、*Rohlin's theorem* 在 md 中拍平为正体；印刷粗体 **Z**/2 在 md 中为正体 `Z/2`。
- 修复登记：md 标题前补期刊行（依据 `audit-redo/p001.png` + 300dpi 期刊行裁片）。

### p.002（PDF p.2 / 印刷 p.280）

- PNG：`audit-redo/p002.png`（pngmono 150dpi）
- 核对：Theorem 1 陈述与对角化公式；2mE₈+n[[0,1],[1,0]] 矩阵式；smoothing 讨论（m=1、n=3/0、CP³）；π₁(X)→SU(2) 条件；Acknowledgement；节标题 I.2；𝔐σ(X) 与 Q(α)=1 设定段
- 结果：**PASS±**。
  - Theorem 1 陈述逐字吻合（含印刷原样 quirk "so in some base"，忠实保留不改）；公式 $Q(u_1,\dots,u_r)=u_1^2+\dots+u_r^2$、矩阵 $2mE_8+n\begin{pmatrix}0&1\\1&0\end{pmatrix}$、$CP^3$、$Q(\alpha)=1,\ \alpha\in H^2(X;\mathbf{Z})$ 全部与页图一致。
  - 排版级伪影（登记不改）：印刷整段斜体的 Theorem 1 在 md 中为正体；粗体 **CP**³ 拍平为 `$CP^{3}$`；**Z**/2 同前。
  - 系统性省略（登记一次，适用于全部正文页）：MinerU 导出无逐页 running head 与页码数字（本页印刷页眉 `280  S. K. DONALDSON`）；不影响正文完整性，不逐页补录。
- 修复登记：无。

### p.003（PDF p.3 / 印刷 p.281）

- PNG：`audit-redo/p003.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（connection 空间草书体记号，结论记于本条）
- 核对：Lemma 2 陈述与 n(Q)⩽rank(Q)；split 公式两行；n(Q|α⊥) 限制记号；σ(CP²) 不等式；节标题 I.3；𝔐σ=𝔐σ(X)；P↓X 记号；A−B∈Ω¹(𝔤)；d_A、d_A*、∇_A 算子行
- 结果：**PASS±**（含一处记号修复）。
  - Lemma 2 斜体陈述、`n(Q)\leqslant\operatorname{rank}(Q)`（印刷斜 slanted ⩽，md `\leqslant` 正确）、split 两式、`Q|_{\alpha^\perp}`、`\operatorname{rank}(Q)\leqslant n(Q).\sigma(\mathbf{CP}^2)=n(Q)` 全部与页图一致。
  - 节标题、引论句、`P\downarrow X`、`A-B\in\Omega^1(\mathfrak{g})`、`d_A\colon\Omega^p(V)\to\Omega^{p+1}(V)`、伴随与协变导数行均吻合；跨页句 "The curvature F(A) of any | connection…" 断点与 md 一致。
  - **修复**：md 行 97（p.1 补题录前行号 95）"so Q is an affine space" 的普通 `Q` 与同段行 91/111 的 `$\mathcal{Q}$` 不一致；300dpi 裁片确认印刷两处同为草书 𝒬 → 已 Edit 改为 `so $\mathcal{Q}$ is an affine space`。
  - 排版级伪影（登记不改）：印刷斜体 *connections*、*signature*、Lemma 2 斜体陈述在 md 中为正体。
- 修复登记：行 95 `Q`→`$\mathcal{Q}$`（依据 `audit-redo/p003.png` + 300dpi 两处草书 𝒬 裁片）。

### p.004（PDF p.4 / 印刷 p.282）

- PNG：`audit-redo/p004.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（Proposition 3 分母与括号内记号，结论记于本条）
- 核对：F(A+a) 曲率公式；𝒢 作用 g(A)=A−(d_A g)g⁻¹；SU(2)/U(1) 分类两行；Proposition 3 全文（含分数系数与括号注记）；c₂(P)=(1/8π²)∫Tr(F∧F)；Tc₂(A)∈R/Z 与带边版本；Self-duality 段与 Ω²=Ω²₊⊕Ω²₋
- 结果：**PASS±**（含一处记号修复）。
  - `F(A+a)=F(A)+d_Aa+\frac12[a,a]`、`g(A)=A-(d_Ag)g^{-1}`、`c_2(P)=\frac{1}{8\pi^2}\int_X Tr(F(A)\wedge F(A))\in\mathbf{Z}`、`Tc_2(A)\in\mathbf{R}/\mathbf{Z}`、带边 `Tc_2(A)=\frac{1}{8\pi^2}\int_Z Tr(F(\tilde A)\wedge F(\tilde A)),\ \mathrm{mod}\ \mathbf{Z}`、`\Omega^2=\Omega^2_+\oplus\Omega^2_-` 全部与页图一致。
  - 300dpi 仲裁：Proposition 3 分数分母印刷为 `2πi`，md `$-\frac{1}{2\pi i}F(A)$` **正确**（150dpi 下曾疑为 4π，以 300dpi 裁片否定）。
  - **修复**：md 行 129 "(g is in this case a trivial bundle)" 的普通 `g`，300dpi 裁片确认印刷为 Fraktur **𝔤**（U(1) 情形伴随李代数丛平凡，非连接空间 𝒬）→ 已 Edit 改为 `($\mathfrak{g}$ is in this case a trivial bundle)`。
  - 排版级伪影（登记不改）：Proposition 3 印刷整段斜体在 md 中为正体；粗体 **Z**、**R** 在行内公式外沿用正体。
- 修复登记：行 129 `g`→`$\mathfrak{g}$`（依据 `audit-redo/p004.png` + 300dpi Proposition 3 裁片）。

### p.005（PDF p.5 / 印刷 p.283）

- PNG：`audit-redo/p005.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（d_A⁻ 算子行、Laplacian 行、椭圆复行，结论记于本条）
- 核对：式(1) 自偶/反自偶性质；F(A)=F₊(A)+F₋(A) 分解；Yang-Mills 作用量两个积分式；−8π²c₂(P) 等式链；flat connection/θ 段；d⁻ 复合算子；d_A⁻ 与三个 Laplacian 公式；椭圆复；本篇约定段（c₂(P)=−1）
- 结果：**PASS±**。
  - 式(1)（含 `\tag{1}` 与印刷同位的 `.vol.`）、`\Omega^2=\Omega^2_+\oplus\Omega^2_-`、`\|F(A)\|^2_{L^2}` 两个积分式、`-8\pi^2c_2(P)=\int_X-Tr(F\wedge F)=\int_X|F_+|^2-|F_-|^2d\mu`、`d^-\colon\Omega^1\to\Omega^2_-` 复合式逐字吻合。
  - 300dpi 仲裁三处均确认 md 正确：① `d_A^-\colon\Omega^1(V)\to\Omega_-^2(V)` 目标确有下标减号；② Laplacians 印刷为 `d_A^*d_A,\ d_Ad_A^*+d_A^*d_A^-,\ d_A^-d_A^*`，md（行 195）连中项的上标减号都一致；③ 椭圆复箭头标签印刷为 `d_A` 与 `d_A^-`（无数字上标），md 行 198 一致。
  - 排版级伪影（登记不改）：印刷斜体 *self-dual connection*、*Yang-Mills action*、*flat*、*if A is self-dual* 在 md 中为正体。
- 修复登记：无。

### p.006（PDF p.6 / 印刷 p.284）

- PNG：`audit-redo/p006.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（叠置丛记号 P↓S⁴ 与 S⁷↓S⁴，结论记于本条）
- 核对：节标题 I.4；∫_U|F|²dμ 与共形不变段；式(2)；Proposition 4 [20, Theorem 4.1] 全文与有限作用积分；moduli space 𝔐(S⁴)=SO(5,1)⁺/SO(5)=B⁵ 段；P↓S⁴ 与 S⁷↓S⁴ 叠置记号
- 结果：**PASS±**（含两处叠置记号错位修复）。
  - I.4 标题、`c_2(P)=-1`、`\int_U|F|^2d\mu`、式(2) `\int_{\mathbf{R}^4}|F|^2d\mu . = -8\pi^2c_2`（印刷原样 quirk：`d\mu` 后多一句点，md 忠实保留）、Proposition 4 斜体全文、`\int_{B^4\setminus\{0\}}|F(A)|^2d\mu<\infty`、`g\colon B^4\setminus\{0\}\to SU(2)`、总作用 `8\pi^2`、`\mathfrak{M}(S^4)=SO(5,1)^+/SO(5)=B^5`、centre/scale 段与 `4\pi^2` 全部与页图一致。
  - **修复**：印刷把 `P\downarrow S^4` 排成 P/↓/S⁴ 三行叠置，Luna 转写丢了下位 S⁴（行 231 作 `$P\downarrow$`），又把版面重叠的同一 S⁴ 误挂成 `SO(5)` 的上标（`$SO(5)^{S^4}$`）。300dpi 裁片确认：SO(5) 无上标，S⁴ 是箭头叠置的下位 → 已 Edit 改为 `on $P\downarrow S^4$ form a single orbit … a single $SO(5)$ invariant class`；第二处叠置 `$S^7\downarrow S^4$` Luna 转写正确，不动。
  - 排版级伪影（登记不改）：印刷斜体 *moduli space*、*centre*、*scale*、Proposition 4 整段斜体在 md 中为正体；粗体 **R⁴** 拍平。
- 修复登记：行 231 `$P\downarrow$`→`$P\downarrow S^4$`、`$SO(5)^{S^4}$`→`$SO(5)$`（依据 `audit-redo/p006.png` + 300dpi 叠置记号裁片）。

### p.007（PDF p.7 / 印刷 p.285）

- PNG：`audit-redo/p007.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（F(I₀,λ) 分母、谐和空间花体字母、Proposition 5 叠置记号，结论记于本条）
- 核对：dilations/quaternionic 段；I₀,λ 与 F(I₀,λ) 两式；B̄⁵=𝔐(S⁴)∪S⁴ 段；节标题 I.5；ℋ²=ℋ²₊⊕ℋ²₋ 分解；Q_R(α)=∫α∧α；[9, §52.2] 段；Taubes 引入段；Proposition 5 开头（P↓X 叠置）
- 结果：**PASS±**（含一处记号一致性修复）。
  - `I_{0,\lambda}(x)=\mathrm{Im}(xd\bar{x}/(\lambda^2+|x|^2))` 与页图一致；`\overline{B}^5=\mathfrak{M}(S^4)\cup S^4`、`Q_{\mathbf{R}}(\alpha)=\int_X\alpha\wedge\alpha,\ \alpha\in H^2(X;\mathbf{R})`、`[9,\ \S52.2]`（印刷原样 quirk，忠实保留）均吻合。
  - **印刷 quirk 登记（不改）**：`F(I_{0,\lambda})=\lambda^2\,dx\,d\bar{x}/(\lambda^2+|x|)^2` —— 300dpi 确认印刷分母即无 `|x|^2` 的 `(\lambda^2+|x|)^2`，与上一式自相矛盾，系原刊排印笔误；md 忠实保留。
  - 300dpi 确认 Proposition 5 叠置记号 `P\downarrow X`（行 261）Luna 转写正确。
  - **修复**：同一印刷花体字形，md 行 251 作 `$\mathcal{H}^2=\mathcal{H}^2_+\oplus\mathcal{H}^2_-$`，行 257 却作 `$\mathcal{K}^2_-(X)$`；300dpi 裁片确认两处为同一字形（字形本身 H/K 形难分，但语境为 harmonic forms 空间，且全文无其它 script-K 用法）→ 已 Edit 统一为 `\mathcal{H}`。行 277 的 `$\mathcal{K}^2_-(X)=0$` 属 p.8 内容，届时同规则修复。
  - 排版级伪影（登记不改）：印刷斜体 *moduli space* 等在 md 中为正体。
- 修复登记：行 257 `$\mathcal{K}^2_-(X)$`→`$\mathcal{H}^2_-(X)$`（依据 `audit-redo/p007.png` + 300dpi 两处花体字形对比裁片）。

### p.008（PDF p.8 / 印刷 p.286）

- PNG：`audit-redo/p008.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（Ω²₋(𝔤) 两处、Sobolev 范数下标、𝔅=𝒬/𝔤 商空间行、𝔐 与 ℳ 两种 M 字形，结论记于本条）
- 核对：Proposition 5 正文（δ(A₀) 判据、结论 (i)(ii)）；Taubes 应用段；U(1) 唯一性观察；节标题 II.1（含 $\mathfrak{B}$）；Sobolev 空间定义与范数示例式；widening 段；moduli space 定义与商空间、记号行
- 结果：**PASS±**（含五处记号修复）。
  - `\delta(A_0)=\|F_-(A_0)\|_{L^2}+\|F(A_0)\|_{L^4}\|F_-(A_0)\|_{L^{4/3}}<\varepsilon_0`、`(i)\ \|\nabla_{A_0}a\|_{L^2}\leqslant C.\delta(A_0)`、`(ii)\ \|a\|_{L^2}\leqslant C.\|F_-(A_0)\|_{L^{4/3}}`、范数示例式 `\|s\|^2_{L^2_1(A)}=\|\nabla_A s\|^2_{L^2}+\|s\|^2_{L^2}=\int_X(|\nabla_A s|^2+|s|^2)d\mu`（300dpi 确认印刷下标即 `L^2_1`，md 正确）、`L^2_3(\Omega^1(\mathfrak{g}))` 与 `\|\ \|_{L^2_k(A)}`、`k\leqslant3`（300dpi 确认 md 正确）均吻合。
  - **修复×5**（均 300dpi 裁片裁决）：① 行 263 与 ② 行 269 印刷均为 `Ω²₋(𝔤)`，md `\Omega_-(\mathfrak{g})` 丢上标 ² → 补 `\Omega^2_-`；③ 行 277 同字形花体 K → `\mathcal{H}`（同 p.7 规则）；④ 行 294 商空间印刷为 `𝔅 = 𝒬/𝔤`（分子草书 𝒬 同 p.3 字形、分母 Fraktur 𝔤 与 Ω(𝔤) 中一致），md `\mathscr{A}/\mathfrak{g}` 分子误作草书 A → 改 `\mathcal{Q}`；⑤ 行 297 记号行印刷 `p: 𝒬 → 𝔅`，md `\mathcal{A}\to\mathcal{B}` 两字形皆误 → 改 `\mathcal{Q}\to\mathfrak{B}`；同行 "the moduli space **ℳ**"（印刷圆弧草书 M，与行 291 定义处 Fraktur 𝔐 不同字形）md 拍平为 M → 改 `$\mathscr{M}$`，"the ambient space **𝔅**" 拍平为 B → 改 `$\mathfrak{B}$`。
  - 排版级伪影（登记不改）：Proposition 5 结论行斜体、*moduli space* 斜体在 md 中为正体。
- 修复登记：行 263/269 `\Omega_-`→`\Omega^2_-`；行 277 `\mathcal{K}`→`\mathcal{H}`；行 294 `\mathscr{A}`→`\mathcal{Q}`；行 297 `\mathcal{A}\to\mathcal{B}`→`\mathcal{Q}\to\mathfrak{B}`、`M`→`$\mathscr{M}$`、`B`→`$\mathfrak{B}$`（依据 `audit-redo/p008.png` + 300dpi 裁片）。

### p.009（PDF p.9 / 印刷 p.287）

- PNG：`audit-redo/p009.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（"complex lie bundles" 用词、§I.2/§I.5 引用、fixes-A-in 字形、Ω^p(L²) 上标、stabiliser 行字形，结论记于本条）
- 核对：reducible connections 讨论段；E=L⊕L⁻¹ 分解；c₂(L⊕L⁻¹)=−c₁(L)²；n(Q)=½|{α∈H²(X;Z)|Q(α)=1}|；§I.2/§I.5 引用；γ 固定 A 与 stabiliser Γ_A≅S¹ 段；H¹(X;R)=ℋ²₋(X)=0 式；Ω^p(L²) 段；Conversely 段
- 结果：**PASS±**（含一处 print quirk 复原 + 六处字形拍平修复）。
  - 公式全部吻合：`E=L\oplus L^{-1}`、`c_2(L\oplus L^{-1})=-c_1(L)^2`、`n(Q)=\frac12|\{\alpha\in H^2(X;\mathbf{Z})\mid Q(\alpha)=1\}|`、`H^1(X;\mathbf{R})=\mathcal{H}^2_-(X)=0`（修复后）。
  - 300dpi 仲裁：印刷 "the complex **lie** bundles"（"line" 之排印误植）→ **Luna 静默改正为 "line"，违背 print quirk 忠实原则，本次 Edit 复原为 "lie" 并在此登记**；同页后文 "trivial line bundle / complex line bundle L²" 印刷确为 line，不动。
  - 印刷 §I.2、§I.5 为罗马 I，md 原本即正确；印刷 `Ω^p(L²)` 上标确为斜体 p（非 0/2），md `$\Omega^p(L^2)$` 正确（语义存疑但忠实保留）。
  - **修复×6**（同页字形拍平，均 300dpi 裁片裁决）：行 319 "automorphisms G"→`$\mathcal{G}$`；"fixes A in Q"→`$\mathcal{Q}$`（印刷确为草书 𝒬，γ 固定的是连接本身，语义亦通）；"of A in Q"→`$\mathcal{Q}$`；"the g valued forms"与"The bundle g splits"→`$\mathfrak{g}$`；行 327 "in G"→`$\mathcal{G}$`、"sections of g"→`$\mathfrak{g}$`。行 322 display 中 `\mathcal{K}`→`\mathcal{H}`（同 p.7/p.8 同字形规则）。
  - 排版级伪影（登记不改）：*reducible connections* 斜体等在 md 中为正体。
- 修复登记：行 305 "line"→"lie"（print quirk 复原）；行 319 G→`$\mathcal{G}$`、两处 Q→`$\mathcal{Q}$`、两处 g→`$\mathfrak{g}$`；行 322 `\mathcal{K}`→`\mathcal{H}`；行 327 G→`$\mathcal{G}$`、g→`$\mathfrak{g}$`（依据 `audit-redo/p009.png` + 300dpi 裁片）。

### p.010（PDF p.10 / 印刷 p.288）

- PNG：`audit-redo/p010.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（𝔤⊗C 的 C、b 式提位负号、‖b‖ 下标撇号、S 映射目标字形，结论记于本条）
- 核对：Theorem 6 (i)(ii) 全文与 slice 定义式；"principle bundle" 句；Proof 段（Lie 群拓扑、分解 g=γg̃、H⁰_A/H^{0⊥}_A、⩾ 不等式、b 式与 d_Ag₂ 式、‖b‖‖a‖<ε 段、g=γg̃ 两行式）；Hausdorff 论证段；(i) 开集论证与 S 映射定义
- 结果：**PASS±**（含四处 Fraktur/商式修复）。
  - slice 式 `T_{A,\varepsilon}=\{A+a\mid d_A^*a=0,\ \|a\|_{L^2_3}<\varepsilon\}`、`L^2_4(\Omega^0(\mathfrak{g}\otimes\mathbf{C}))`（300dpi 确认印刷为粗体 **C**，md `\mathbf{C}` 正确）、`H_A^0/H_A^{0\perp}`、`\|d_Ag_2\|_{L^2_k}\geqslant\mathrm{const.}\|g_2\|_{L^2_{k+1}}`、`g=\gamma\tilde g` 两行式全部与页图一致。
  - **修复×4**：① 行 329 Theorem 6 开头 `B`/`$B^{*}$` → `$\mathfrak{B}$`/`$\mathfrak{B}^{*}$`（印刷 Fraktur 𝔅/𝔅*，同侧行 369 前两处 Luna 已用 `\mathfrak{B}`，同一行内自相矛盾）；② 行 337 `$T_{A,\varepsilon/\Gamma_A}$` → `$T_{A,\varepsilon}/\Gamma_A$`（印刷商号在 T 之外，Luna 把 /Γ_A 塞进了下标）；③ 行 365 `so $\mathcal{B}$ is Hausdorff` → `$\mathfrak{B}$`；④ 行 369 `$p^{-1}(B^*)$` → `$p^{-1}(\mathfrak{B}^*)$`。
  - **印刷 quirk 登记（不改，300dpi 逐一确认确系印刷原样）**：① "is a **principle** 𝒢/±1 bundle"（principal 之误植，Luna 忠实保留）；② b 式中提位负号 "=⁻d_Agg⁻¹"（负号位于上标高度，md `= ^{-} d_A g g^{-1}` 忠实保留空底上标形式）；③ "Thus from ‖b‖_{L²₃′}‖a‖_{L²₃} < ε" 首个下标带撇号（印刷确有 prime，md `L_3^2'` 忠实保留）。
  - 排版级伪影（登记不改）：Theorem 6 整段斜体拍平为正体；行 362 印刷内层括号转写为花括号 `\{\ldots\}`。
- 修复登记：行 329 `B`/`$B^{*}$`→`$\mathfrak{B}$`/`$\mathfrak{B}^{*}$`；行 337 `$T_{A,\varepsilon/\Gamma_A}$`→`$T_{A,\varepsilon}/\Gamma_A$`；行 365 `$\mathcal{B}$`→`$\mathfrak{B}$`；行 369 `$p^{-1}(B^*)$`→`$p^{-1}(\mathfrak{B}^*)$`（依据 `audit-redo/p010.png` + 300dpi 四张裁片）。

### p.011（PDF p.11 / 印刷 p.289）

- PNG：`audit-redo/p011.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（p⁻¹(𝔅*) 行、T_{A,ε}/Γ_A 行、Φ 映射显示式、DΦ 显示式，结论记于本条）
- 核对：DS 导数式与同构论证段；(ii) 限制式 S: T_{A,ε}×exp(H^{0⊥}_A)→𝒬；Γ_A 分裂与 T_{A,ε}/Γ_A 局部模型；T_{A,ε}/Γ_A ⊂ Ω¹(L²)/S¹×Ω¹_X 显示式；quotient singularity 段；节标题 II.2；Φ 零点定义与两行显示式；DΦ Fredholm 段
- 结果：**PASS±**（含六处 Fraktur/括号结构修复）。
  - `DS\colon\operatorname{Ker}d_A^*\times\Omega^0(\mathfrak{g})\to\Omega^1(\mathfrak{g})`、`T_{A,\varepsilon}/\Gamma_A\subset\Omega^1(L^2)/S^1\times\Omega_X^1`（此行商号位置 Luna 本就正确）、`\Omega^1_X` 下标、Φ 两行显示式（含 `L^2_2(\Omega^2_-(\mathfrak{g}))` 目标与 `d_A^-a+\frac12[a,a]`）全部与页图一致（300dpi 确认目标 Sobolev 下标为 2）。
  - **修复×6**：① 行 381 `\Omega^1(g)`→`\Omega^1(\mathfrak{g})`；② 行 381 `$p^{-1}(\mathcal{B}^*)\to\mathcal{B}^*$`→`$\mathfrak{B}^*$`（300dpi 确认印刷 Fraktur）；③ 行 389 `in $\mathcal{B}$`→`$\mathfrak{B}$`；④ 行 389 `$T_{A,\varepsilon/\Gamma_{A}}$`→`$T_{A,\varepsilon}/\Gamma_{A}$`（300dpi 确认商号在 T 外，与 p.010 行 337 同型错误）；⑤ 行 389 `$\mathcal{B}^{*}$`→`$\mathfrak{B}^{*}$`；⑥ 行 391/397 两处普通 `B`→`$\mathfrak{B}$`；⑦ 行 410 DΦ 显示式补闭大括号——印刷为 `(Ker d_A^* ⊂ L²₃(Ω¹(𝔤))) →^{d_A⁻} L²₂(Ω²₋(𝔤))`（大括号在 Ω¹(𝔤) 后即闭合，目标在括号外），md 原 `\left(` 未闭合且跨含目标，结构错误 → 已 Edit 改为 `\left(\operatorname{Ker}\ldots\left(\Omega^1(\mathfrak{g})\right)\right)\stackrel{d_A^-}{\rightarrow}L^2_2(\ldots)`。
  - 记号宏不一致（登记不改）：行 386 目标 `$\mathscr{Q}$` 与全文 `\mathcal{Q}$` 为同一印刷字形（草书 𝒬），MinerU 宏混用，语义无损。
- 修复登记：行 381 两处；行 389 三处；行 391/397 各一处；行 410 括号结构（依据 `audit-redo/p011.png` + 300dpi 裁片）。

### p.012（PDF p.12 / 印刷 p.290）

- PNG：`audit-redo/p012.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（index 公式分数、"intepreted" 用词，结论记于本条）
- 核对：Index(DΦ)_A 两行显示式；Atiyah-Singer index 公式（8|c₂(P)|−3/2(χ−τ)=5）；χ=2+b₂、τ=b₂ 段与 [A]∈𝔅 句；Kuranishi/Smale 引言；Lemma 7 全文（斜体）；E=kerL⊕E′、F=ImL⊕F′；Proof（L|_{E′}、L̃、ψ 三行式、f∘ψ⁻¹ 式）；regular value 段
- 结果：**PASS±**（含一处 print quirk 复原 + 一处草书拍平修复）。
  - Index 显示式（`\operatorname{Index}(D\Phi)_A=\dim\operatorname{Ker}-\dim\operatorname{coker}`，目标 `\Omega^0(\mathfrak{g})\oplus\Omega^2_-(\mathfrak{g})`）、index 公式 300dpi 确认分数为 **3/2**（md `\frac{3}{2}` 正确；与 χ−τ=2 时结果 5 自洽）、行 427 `in $\mathfrak{B}$`（此处 Luna 本就正确）、Lemma 7 全部公式（`\ker L`/`\operatorname{Ker} L` 大小写混排系印刷原样）、Proof 三行式与 f(ψ⁻¹(x)) 式均与页图一致。
  - **修复×2**：① 行 421 `$A \in Q$` → `$A \in \mathcal{Q}$`（印刷草书 𝒬）；② 行 429 "interpreted" → "intepreted"（300dpi 确认印刷即漏字母 r 的 **intepreted**，系原刊排印错误；Luna 曾静默改正，按 print quirk 忠实原则复原并登记）。
  - 排版级伪影（登记不改）：Lemma 7 斜体陈述、*regular value* 斜体拍平；"(c.f. [16])" 印刷原样保留。
- 修复登记：行 421 `Q`→`$\mathcal{Q}$`；行 429 "interpreted"→"intepreted"（依据 `audit-redo/p012.png` + 300dpi 裁片）。

### p.013（PDF p.13 / 印刷 p.291）

- PNG：`audit-redo/p013.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（φ|_{L⁻¹(y₁)} 与 dimension K、H²_A 补空间句、§I.2、Banach 显示式、ℰ³⇒ℰ² 丛对，结论记于本条）
- 核对：Lemma 7 收尾句；Proposition 8 全文与两个显示式（Z(φ)、Z(φ)/Γ_A≅Z(φ)/S¹、dim_R=6）；"This position" 段；H⁰_A/H²_A 段与 K⊂𝔐 句；节标题 II.3；§I.2 引用句；𝒢/±1 作用与 Banach 显示式；ℰ³⇒ℰ² 丛对句
- 结果：**PASS±**（含三处修复）。
  - Proposition 8 两个显示式（含 `dim_{\mathbf{R}}` 与实维数 5/6）、"This position follows straight from the lemma"（印刷原样 quirk，忠实保留）、"Taubes implicit function theorem"（印刷无所有格 's，忠实保留）、`H_A^1\cong C^3`、`\Delta_{A_0}=d_{A_0}^-d_{A_0}^*`、`\Omega^2_-(\mathfrak{g})`、`§I.2`（300dpi 确认罗马 I）均与页图一致。
  - **印刷 quirk 登记（不改，300dpi 确认）**：① 行 461 `φ|_{L^{-1}(y_1)}`（语义应为 f⁻¹，印刷确为 L）与 "of dimension $K$"（语义应为小写 k，印刷确为大写 K）——均系原刊排印疏忽，md 忠实保留；② 行 477 "This position"（语义疑为 This proposition/result，印刷原样）。
  - 300dpi 否决两处初读怀疑：行 463 "harmonic space $H_A^2$ as the complement of Im $d_A^-$" 印刷确为上标 2（md 正确，未改）；行 488 Banach 显示式两侧 Sobolev 下标印刷确为 3 与 2、两目标同为 Ω²₋(𝔤)（md 正确，未改）。
  - **修复×3**：① 行 479 `$K \subset M$` → `$K \subset \mathfrak{M}$`（印刷 Fraktur 𝔐）；② 行 488 显示式箭头 `\leftrightarrow` → `\Rightarrow`（300dpi 确认印刷为双线 ⇒）；③ 行 491 丛对 `$\mathfrak{E}^3\to\mathfrak{E}^2$` → `$\mathscr{E}^3 \Rightarrow \mathscr{E}^2$`，及 "section $\Phi$ of $\mathfrak{E}^2$" → `$\mathscr{E}^2$`（300dpi 确认为草书 ℰ 与双箭头 ⇒，Luna 误作 Fraktur E + 单箭头）。
  - 排版级伪影（登记不改）：Proposition 8 整段斜体拍平；`C^3` 印刷粗体拍平为正体。
- 修复登记：行 479 `M`→`$\mathfrak{M}$`；行 488 箭头→`\Rightarrow`；行 491 `\mathfrak{E}`→`\mathscr{E}` 与箭头→`\Rightarrow`（依据 `audit-redo/p013.png` + 300dpi 裁片）。

### p.014（PDF p.14 / 印刷 p.292）

- PNG：`audit-redo/p014.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（ℰ 系列字形、L²₃⇒L²₂ 箭头、H¹_A→φ→H²_A 箭头标、(Dφ)₀、Φ(ψ⁻¹X) 大写 X、"transυersally" 希腊 υ，结论记于本条）
- 核对：∇σ 定义显示式与 ℰ³ 纤维范数段；"in effect the slices" 段与 L²₃⇒L²₂ compact；Γ_A symmetry 拓扑段；reducible 处理段（H²_A≅C^p、H¹_A≅C^{3+p}→^φ H²_A≅C^p、(Dφ)₀=0、α 上同调、φ̃(z) 式、φ̃⁻¹(0)/S¹≅C³/S¹ cone on CP²）；Φ/Φ̃ 替换两显示式；K⊂𝔅* 段；Lemma 9 全文
- 结果：**PASS±**（含八处修复）。
  - 与页图一致：`(∇σ)_{[A]}` 显示式结构（`(T\mathfrak{B}^*)_{[A]}` Fraktur 正确）、`H_A^1\cong\mathbf{C}^{3+p}\xrightarrow{\phi}H_A^2\cong\mathbf{C}^p`（300dpi 确认箭头标为**无 tilde 的 φ**，md 正确）、`(\mathbf{D}\phi)_0=0`（300dpi 确认**无 tilde**，md 正确）、φ̃(z) 式、`L^2_2(\Omega^2_-(\mathfrak{g}))`（300dpi 确认下标 2）、`Φ(ψ^{-1}X)` 印刷确为**大写 X**（与同式小写 x 并存系原刊疏忽，md 忠实保留）、Lemma 9 的 `V\subset\subset U` 与 `K\subset U_1\subset\subset U_2\subset\subset U_3`。
  - **修复×8**：① 行 493 `\mathfrak{S}^3` → `$\mathscr{E}^3$`（印刷草书 ℰ³，Luna 此处误作 Fraktur S——同一字形在 p.13 又被它作 Fraktur E，三页三种写法）；② 行 496 `\mathfrak{E}_A^3` → `$\mathscr{E}_A^3$`；③④ 行 499 `\mathfrak{E}^k`/`\mathfrak{E}^2` → `\mathscr{E}`；⑤ 行 499 `L_3^2 \Leftrightarrow L_2^2` → `L_3^2 \Rightarrow L_2^2`（300dpi 确认双线 ⇒，与 p.13 行 488 同型）；⑥⑦ 行 529 两处 `$B^{*}$` → `$\mathfrak{B}^{*}$`（印刷 Fraktur）；⑧ 行 531 "cut out transversally" → "cut out transυersally"（300dpi 放大对比同段斜体 *covered* 的尖底 v：印刷此处为**圆底希腊 υ**，ABBYY 文本层亦作 transυersally；Luna 曾静默改正，按 print quirk 原则复原并登记）。
  - 排版级伪影（登记不改）：Lemma 9 整段斜体拍平；`C^p`（行 503）印刷粗体、md 正体，而同行 506/515 又用 `\mathbf{C}`——粗体处理不一致系 Luna 基线遗留，语义无损。
- 修复登记：行 493/496/499（×3）草书 ℰ 统一为 `\mathscr{E}`；行 499 箭头→`\Rightarrow`；行 529 两处 `B*`→`$\mathfrak{B}^{*}$`；行 531 "transversally"→"transυersally"（依据 `audit-redo/p014.png` + 300dpi 裁片）。

### p.015（PDF p.15 / 印刷 p.293）

- PNG：`audit-redo/p015.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（Proof 首句两个 Sobolev 上标与紧性箭头、f=Φ+σ 显示式、Ṽ/W̃ tilde、KO(T) 字形、脚注尾词，结论记于本条）
- 核对：Lemma 9 应用句（𝔐^σ=Z(Φ+σ)、n(Q) 奇点）；Proof of Lemma 9（covering¹ 脚注标、L²₄/L²₃/L²₄ 界链、L²₄⇒L²₃ 紧性）；G 开性段；f=Φ+σ 显示式；Sard 引理与 bump function β(‖a‖) 段；节标题 II.4（$\mathfrak{M}^{\sigma}$）；Fredholm 族 setup（Ṽ,W̃ over M×T、Ṽ_t|≅V、ind{L_t}∈KO(T)）；页脚注¹全文
- 结果：**PASS±**（含三处修复）。
  - 与页图一致：`f=\Phi+\sigma\colon E=\operatorname{Ker}d_A^*\cap L^2_3\to L^2_2=F`（300dpi 确认印刷无 Ω¹(𝔤)、单箭头，md 原样正确）；`\tilde{V},\tilde{W}` over M×T 与 `\tilde{V}_t=\tilde{V}|_{M\times\{t\}}\cong V`（300dpi 确认 tilde 在上）；`\operatorname{ind}\{L_t\}\in KO(T)`（300dpi 确认为**基线 KO**，实 K 论，非 K⁰）；`0\leqslant R<\infty`、`\|(\Phi+\sigma)(A)\|_{L^2_3(A)}\leqslant R`、Sard 句与 `\beta(\|a\|)`。
  - **修复×3**：① 行 537 "an $L_3^2$ bound on Φ+σ" → `$L_4^2$`（300dpi 确认印刷为 L²₄；界链为 L²₄→给 L²₃→得 L²₄）；② 行 537 `$L_4^2 \Leftrightarrow L_3^2$` → `\Rightarrow`（300dpi 确认双线 ⇒，本块第 4 例同型错误）；③ 行 563 脚注尾 "dense in Q" → `$\mathcal{Q}$`（300dpi 确认草书 𝒬）。
  - 印刷 quirk 登记（不改）：脚注标 ¹ 与 "covering¹ U" 原位保留（md `covering$^1$$U$`）；行 537 `$T_{A,\epsilon}$` 用 `\epsilon` 而全文他处用 `\varepsilon`——同一印刷字形，MinerU 宏不一致，语义无损。
- 修复登记：行 537 `L_3^2`→`L_4^2`（首个界）、`\Leftrightarrow`→`\Rightarrow`；行 563 `Q`→`$\mathcal{Q}$`（依据 `audit-redo/p015.png` + 300dpi 裁片）。

### p.016（PDF p.16 / 印刷 p.294）

- PNG：`audit-redo/p016.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（乘积商空间行、𝔅̂→π𝔅 显示式、μσ 字形、𝔅̂(M,n,k) 帽号，结论记于本条）
- 核对：(*) 显示式与 coKer/CoKer 大小写；KO 增广句；𝒢₀⊂𝒢 与 "on P_{x₀}. Then" 段；Ṽ/W̃ 显示式（整体宽 tilde）；𝒬/𝒢₀×X=𝔅̂×X；L_[A] 显示式；𝔅̂→π𝔅 投影；μ^σ∩𝔅* 可定向段；π*(Tμ^σ)=Ind{L_[A]} 式；w₁=0∈H¹(𝔅̂;Z/2)；柱面族 Ind{L_[A]}=Ind{d_A*+d_A⁻}∈KO(𝔅̂)；Lemma 10 全文
- 结果：**PASS±**（含四处花体/Fraktur 修复）。
  - 与页图一致：`ind\{L_t\}|_S=\operatorname{Ker}\{L_t\}-\operatorname{CoKer}\{L_t\}\in KO(S)`（正文 coKer 小写 co、显示式 CoKer 大写 C 系印刷原样，md 两处分别正确）；KO(T)→**Z**；Ṽ/W̃ 显示式的整体宽 tilde（`\widetilde{(T^*X)\otimes\mathfrak{g}}` 等）；`L_{[A]}` 显示式；`d_A^*+d_A^-+t(\nabla\sigma)_A\colon L_3^2\to L_2^2`；`Ind\{d_A^*+d_A^-\}\in KO(\hat{\mathfrak{B}})`；Lemma 10 的 `P_k`/`SU(n)`/`c_2=k`；μ^σ 系印刷原样（300dpi 确认为小写希腊 μ，非 Fraktur 𝔐——语义上应为 moduli space 的笔误，但 Luna 忠实保留 μ，本次不改并在此登记）；`\hat{\mathfrak{B}}(M,n,k)` 帽号（300dpi 确认印刷有 hat，md 正确）。
  - **修复×4**：① 行 577 `over the product $\mathcal{A}/\mathcal{G}_0\times X$` → `$\mathcal{Q}/\mathcal{G}_0\times X$`（300dpi 放大确认印刷为草书 𝒬，即连接空间 𝒬 对受限规范群 𝒢₀ 的商，Luna 误作 𝒜）；② 行 577 `= \hat{\mathcal{B}}\times X` → `\hat{\mathfrak{B}}`；③ 行 586 投影显示式 `\hat{\mathcal{B}}\to\mathcal{B}` → `\hat{\mathfrak{B}}\to\mathfrak{B}`（300dpi 确认首个 B 带 hat、均为 Fraktur）；④ 行 589 `$\mathcal{B}^*\subset\mathcal{B}$` 与同句 `$\mu^\sigma\cap\mathcal{B}^*$` 两处 → `\mathfrak{B}`（同段行 594/597 Luna 又用 `\mathfrak{B}`，同段自相矛盾）。
- 修复登记：行 577 两处；行 586 两处；行 589 三处 `𝔅` 字形（依据 `audit-redo/p016.png` + 300dpi 裁片）。

### p.017（PDF p.17 / 印刷 p.295）

- PNG：`audit-redo/p017.png`（pngmono 150dpi）
- 核对：Proof 开头（stable range n⩾3）；伴随表示分解 𝔰𝔲(2)⊕R⊕V；𝔅̂(M,2,k)/𝔅̂(M,3,k) 归纳段与三个 ind 显示式；w₁ 限制句（H¹(𝔅̂(M,3,k),Z/2)、H¹(𝔅̂(M,2,k);Z/2)）；𝒢₀=𝒢₀(M,n,k) 单连通论证；2-skeleton/wedge of 2-spheres 段；π₄(SU(n)) 显示式；Notes (i)(ii)(iii)
- 结果：**PASS±**（含两处字形拍平修复）。
  - 与页图一致：`\mathfrak{su}(3)`、`\mathfrak{su}(2)\oplus\mathbf{R}\oplus V`、全部 `\hat{\mathfrak{B}}(M,n,k)`（含帽号）、三个 ind 显示式、`w_1` 限制句、`n\geqslant 3`（印刷 slanted ⩾）、`\pi_2(SU(n))=0`、`M=S^4`、`\pi_4(SU(n))`、`$\mathfrak{B}=\hat{\mathfrak{B}}/SO(3)$`、`Sp(n)`。
  - **修复×2**：① 行 655 "any element of $G_{0}$" → `$\mathcal{G}_{0}$`（印刷草书 𝒢₀；同行末 `$\mathcal{G}_{0}(S^{4},n,0)$` Luna 本就正确，行内自相矛盾）；② 行 663 "noncompact space $\hat{\mathcal{B}}$" → `$\hat{\mathfrak{B}}$`（印刷 Fraktur 带帽；行 665 同段又用 `\hat{\mathfrak{B}}`，同段自相矛盾）。
  - 排版级伪影（登记不改）：Proof 斜体、*Notes.* 粗体拍平；行 651 第一个 H¹(…) 分隔符逗号/分号依印刷原样（第二个为分号）。
- 修复登记：行 655 `G_{0}`→`$\mathcal{G}_{0}$`；行 663 `\hat{\mathcal{B}}`→`\hat{\mathfrak{B}}`（依据 `audit-redo/p017.png`）。

### p.018（PDF p.18 / 印刷 p.296）

- PNG：`audit-redo/p018.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（Theorem 11 的 λ₀ 上下标、(ii) 行范数记号，结论记于本条）
- 核对：Notes (iii) 收尾句；节标题 III（独行）；Theorem 11 全文；§II 回顾段；Taubes/Uhlenbeck 引言与四部分列表；节标题 III.1.（印刷即为无标题裸标题）；Proposition 12 全文与 ∫|F(Ã_i)|²dμ⩽C；(i)(ii) 两行
- 结果：**PASS±**（含两处上下标修复）。
  - 与页图一致：`\mathfrak{M}_{\lambda_0}`（300dpi 确认 Theorem 11 中 λ₀ 为**下标**，md 正确；III.3 列表中同为下标）、`\mathfrak{M}^{\sigma}`、`K.K. Uhlenbeck`、四部分列表（III.3 含 `\xrightarrow{p}`）、裸标题 `III.1.`、`C^{\infty}(\overline{B}^4)`、`m_{\infty}`、`\int_{B^4}|F(\tilde{A}_i)|^2 d\mu\leqslant C`、`{i'}\subset\{i\}`、`\frac{1}{2}B^4=\{X\in\mathbb{R}^4||X|<\frac{1}{2}\}`、`(i) d^*A_i=0`、`p\geqslant 2`。
  - 印刷 quirk 登记（不改）：Proposition 12 陈述中 "a limiting $m_{\infty}$ ; and if"（分号）、显示式后 "Then" 大写、"such that $A_i$, converge"（多余逗号）、"$A_\infty$; self-dual"（分号）——均系原刊排印原样，md 忠实保留。
  - **修复**：行 703 (ii) 行两处 `$L^p$` → `$L_p$`——300dpi 放大确认印刷两个范数的 p 均在下标位（与 p.8 定义的 `L^p_k` 上标 p 风格不同，此处印刷即为 `L_p`）；同 zoom 亦确认 `A_i` 无 prime，md 原样正确。
- 修复登记：行 703 两处 `L^p`→`L_p`（依据 `audit-redo/p018.png` + 300dpi 裁片）。
