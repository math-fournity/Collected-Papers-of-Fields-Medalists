# AUDIT-REDO — Donaldson 1983, “An Application of Gauge Theory to Four-Dimensional Topology”

- 性质：**Luna 审计重做**。用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检；Luna 旧修复（`fix(md)` commit `9717b16`，修复后 md SHA `a22812e1…`）一并重核，不再默认其结论正确。
- Actor：`Wf-R-P03`（dynamic-workflow Sub Agent，单篇互斥 worktree `cpf-redo-Donaldson_1983_gauge_theory_4manifolds`，分支 `cpf-redo/Donaldson_1983_gauge_theory_4manifolds`）。
- Host / model / effort：`zcode` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`（run 级配置转述；实际生效 effort **自报 UNKNOWN**，无法从 runtime 直接证明）。
- PDF：`Donaldson_1983_gauge_theory_4manifolds.pdf`，38 页，SHA-256 `5a5201ed38b870ec1ad183b697aa505830c5a35bf03d72614a5bb1667fe65080`（本 worktree 实测）。
- 被检 Markdown 基线：`Donaldson_1983_gauge_theory_4manifolds_mineru/Donaldson_1983_gauge_theory_4manifolds__Donaldson_1983_gauge_theory_4manifolds.md`，1,449 行，SHA-256 `a22812e11e24ebbddde35767b454a47957949df592d97b72a689568b83eb74a5`（= Luna fix 后的基线；原始 mineru 产出见历史 commit `0b0f3dd`）。
- 开工时间：2026-10-02 14:33 EDT；本文头最后更新 2026-10-03 21:09 EDT（第三块收尾）。
- 文本层判定：`pdftotext -f 1 -l 1` 成功返回首页全文（exit 0；ABBYY FineReader OCR 层，2008 年生成）→ **文本层可用，本篇采用双通道主对账**：150dpi pngmono 页图为印刷原文裁决源，pdftotext 文本层仅作第二通道交叉定位/比对；文本层自身有 OCR quirk（如 `E₈`→`£ 8`、连字符丢失），一律以页图为准。
- 方法：每页 `gs -q -dNOPAUSE -dBATCH -sDEVICE=pngmono -r150` 渲染 `audit-redo/p0NN.png` → Read 目检 → 与 Markdown 对应段五点比对（题录 / 节标题顺序 / 定理编号与陈述 / 公式与上下标 / 记号；文末页逐条参考文献与收稿日期）→ PASS / PASS± / FAIL 分级 → 内容错误用结构化 `Edit` 逐处修复（含修正 Luna 旧修复中的错误；print quirk 忠实登记不改）→ 本文件落签该页条目 → 仅 add 本篇路径后按 `redo(page)` 提交。
- 纪律：PDF 原页为唯一裁决源；不写根级任何文件；不动旧 `audit/` 与旧 `AUDIT-Donaldson_1983_gauge_theory_4manifolds.md`（只读参照）；不碰其他论文目录；不 push。

## 本块进度（Wf-R-P03）

- **p.1–p.9 / 38 已完成**（2026-10-02）：9 页全部 PASS±，无 FAIL。逐页一提交：`51587b6f`(p.001)→`3d799f4e`(p.002)→`12974a11`(p.003)→`ae90de97`(p.004)→`4ef9d908`(p.005)→`95209199`(p.006)→`02c79dd4`(p.007)→`42b69e9d`(p.008)→`498796b0`(p.009)。
- 本块对 md 共 14 处修复（含 1 处 Luna print-quirk 静默改正的复原）：全部见各页「修复登记」；`git diff 8aa00fdd` 复核与登记一一对应，无未登记差异。
- 基线后 md SHA-256（本块结束时）：`755e65dc126cde99ed7f870f8a26a6434ca665199b34951d2f3a62622d4f1f25`。
- 跨页系统性发现（供后续页沿用）：① 逐页 running head/页码省略（登记于 p.002，不逐页补录）；② 同一花体字形在 md 中 H/K 混排（本文定为 harmonic 空间 $\mathcal{H}$，p.7/8/9 已统一，后续页遇 `\mathcal{K}` 同规则）；③ 草书 𝒬/𝒢、Fraktur 𝔤/𝔅 拍平为普通字母是 Luna 基线的高发缺陷（p.3/4/8/9 连续出现，后续页需重点盯）；④ 叠置记号（P↓S⁴ 型三行叠置）易被错位转写（p.6 一例）；⑤ 印刷原样错字已登记两处："so in some base"（p.2）、"complex lie bundles"（p.9）、`F(I_{0,λ})` 分母 `(λ²+|x|)²`（p.7）、式(2) `dμ.` 多余句点（p.6）。
- p.10 起 Theorem 6 一带可见残留普通字母 B/B*（行 329），属下一块范围，届时按本块字形规则处理。

## 本块进度（Wf-R-P03，第二块）

- **p.10–p.18 / 38 已完成**（2026-10-02）：9 页全部 PASS±，无 FAIL。逐页一提交：`ee2e9dc3`(p.010)→`bff478e6`(p.011)→`a40d85b0`(p.012)→`e941f6e6`(p.013)→`585a0969`(p.014)→`86b74021`(p.015)→`ef60f780`(p.016)→`50e6219a`(p.017)→`353bf995`(p.018)。
- 本块对 md 共 42 处逐字位修复（分布在 27 个改动行；含 2 处 Luna print-quirk 静默改正的复原：intepreted、transυersally；页级分布 p.010=5、p.011=8、p.012=2、p.013=5、p.014=8、p.015=3、p.016=7、p.017=2、p.018=2）；块末 `git diff c1b2d4fc` 复核与登记一一对应，另发现并修正 1 处本块自身修复遗留（行 410 悬挂 `\right.`，见 p.011 条复核补充）。
- 第二块结束时 md SHA-256：`a8387e2c773dfdd878033fdaa1a610a4db98db70e21cec198f63228773a50b48`（行 410 补删 `\right.` 之后；此前中间态 `f7d926ff…` 为补删前快照，已被本块收尾修正取代）。
- 第二块新登记 print quirk：行 335 "principle bundle"、行 356 提位负号 `=⁻d_Agg⁻¹`、行 359 `‖b‖_{L²₃′}` 撇号、行 461 `φ|_{L⁻¹(y₁)}` 与 "dimension K"、行 477 "This position"、行 518 `Φ(ψ⁻¹X)` 大写 X、p.16 μ^σ（μ 系印刷对 𝔐 的误植，Luna 忠实保留）。⇒/↔ 混淆在本块共 4 例（行 488/499/537 及 p.13 丛对），后续页继续盯。
- p.19 起进入 III.2–III.4 与 Appendix，References（行 ~1403 起）属后续块。

## 本块进度（Wf-R-P03，第三块）

- **p.19–p.28 / 38 已完成**（2026-10-03）：10 页全部 PASS±，无 FAIL。p.019 为上块遗留未提交态（条目、行 711 修复与 p019.png 均已在工作区核验一致），本块开工时先归位补提交；逐页一提交：`eeec9b49`(p.019)→`4d8af141`(p.020)→`6acef57b`(p.021)→`f4fed944`(p.022)→`4cec2d23`(p.023)→`b77f696c`(p.024)→`d11ad951`(p.025)→`4b5fe277`(p.026)→`8c9dfb68`(p.027)→`febb35db`(p.028)。
- 本块对 md 共 30 处逐字位修复（页级分布 p.020=3、p.021=0、p.022=3、p.023=1、p.024=7、p.025=8、p.026=5、p.027=3、p.028=0），全部见各页「修复登记」；每页仅 add 本篇三路径后 `redo(page)` 提交。
- 第三块结束时 md SHA-256：`cec20912e81d596dc2b18844da0c70eb3de3792c4580e9001462f8b759763760`。
- 跨页系统性发现（供后续页沿用）：① **草书 ℳ 大流行**：III.3/III.4 印刷的 moduli space 几乎全为圆弧草书 ℳ（`\mathscr{M}`），本块修复 16 处 `M`/`\mathfrak{M}`（p.022×3、p.023×1、p.024×7、p.025×6、p.026×2、p.027×3，其中 p.025 一处兼含 Ω²₋ 上标）；后续页遇 `𝔐`/`M` 一律 300dpi 先仲裁再定；② **跨页字形张力待复核**：p.018 Theorem 11 处已按 `\mathfrak{M}_{\lambda_0}` 提交，而 p.024 同记号印刷为草书 ℳ_{λ₀}——建议后续块以 audit-redo/p018.png 复核一次（本块不改已提交页）；③ Lie 导数印刷为草书 ℒ（p.026 三处修复 `\mathfrak{L}`→`\mathscr{L}`）；④ "flow on ℬ"（p.26）为圆弧草书 ℬ，与 Fraktur 𝔅 并存，勿见 B 即改 Fraktur；⑤ p.008 的 Ω²₋ 上标缺陷在 p.025 再现两处。
- 本块新登记 print quirk（均高倍确认、md 忠实保留）：compatability（p.21）、"strict inequality in (3) above" 交叉引用笔误（p.21）、`[A_i]∈μ` 印刷小写 μ（p.23）、"every possibly subsequence"（p.23）、K/k 混用（p.24）、`|F_-(f_t(A)|` 外层括号漏排（p.26）、`\frac{c}{dt}`（p.26）；另登记 MinerU 图片零基页号命名（p.28）。
- p.29 起 III.4 收尾与 Appendix（行 1103–1403），References（行 ~1403 起）属后续块；p.028 已确认行 1095 的 images 引用即整页插图（零基页号 page_27_image_0.jpg）。

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
- 修复登记：行 381 两处；行 389 三处；行 391/397 各一处；行 410 括号结构（依据 `audit-redo/p011.png` + 300dpi 裁片）。**复核补充**：行 410 首次修复后块末 diff 复核发现 Luna 原行尾悬挂的 `\right.`（与其跨全式的 `\left` 配对）未被清除，产生不配对定界符；已在 p.018 提交后补删（含于块末 commit），现行为 `…\left(\Omega^1(\mathfrak{g})\right)\right) \stackrel{d_A^-}{\rightarrow} L^2_2\left(\Omega^2_-(\mathfrak{g})\right).`，与印刷结构一致。

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

### p.019（PDF p.19 / 印刷 p.297）

- PNG：`audit-redo/p019.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（收敛论证句两个范数记号，结论记于本条）
- 核对：p.18 跨页句收尾（椭圆方程组与先验不等式句）；节标题 III.2（印刷裸标题）；Theorem 13 全文；(i) 显示式 [Ã_i]→[A_∞] in 𝔐⊂𝔅；(ii) ρ_{i′}:K×SU(2)→P|_K 与 ρ*→θ；[15]/[14] 比较句；Lemma 14 全文与 I(α,i′)、I(q,i) 显示式
- 结果：**PASS±**（含一处范数修复）。
  - 与页图一致：`d^-A_i+\frac12[A_i,A_i]_- =0`、Theorem 13 斜体全文（`\tilde{A}_i\in\mathcal{Q}`、`\{i'\}`）、`[\tilde{A}_i]\to[A_\infty]\ in\ \mathfrak{M}\subset\mathfrak{B}`（𝔐⊂𝔅 Fraktur，Luna 本就正确；`i n` 两字母排式系导出排版瑕疵，登记不改）、`\rho_{i'}\colon K\times SU(2)\to P|_K`、`\rho_{i'}^*(\tilde{A}_{i'})\to\theta`、Lemma 14 全文、`\int_X f_i d\mu\leqslant L`、`I(\alpha,i')=\int_{B_\alpha}f_{i'}d\mu`、`I(q,i)=\int_{B_q}f_i d\mu\leqslant L`、`\{B_q\}_{q\in N}`。
  - **修复**：行 711 第二个范数 `$\|A_{i}\|_{L_{p}^{p}}$` → `$\|A_{i}\|_{L_{p}}$`——300dpi 放大确认印刷为 `\|A_i\|_{L_p}`（下标 p，与 p.018 (ii) 行风格一致；同句第一个范数 `\|F(\tilde{A}_i)\|_{L^p}` 印刷确为上标 p，md 原样正确）。Luna 的 `L_{p}^{p}` 系两种风格杂糅的误读。
  - 排版级伪影（登记不改）：Theorem 13/Lemma 14 斜体拍平；"diagonal argument" 等引号。
- 修复登记：行 711 `L_{p}^{p}`→`L_{p}`（依据 `audit-redo/p019.png` + 300dpi 裁片）。

### p.020（PDF p.20 / 印刷 p.298）

- PNG：`audit-redo/p020.png`（pngmono 150dpi）；字形仲裁：600dpi 裁片（ds² 显示式、行内度量式与 `0(r²)` 三处 O/0 字形，结论记于本条）
- 核对：Lemma 14 证明收尾（对角线论证句、δ-函数点集段、∫_{B_j}f_{i'}dμ>c/2 与 L⩾Σ⩾½lc 两式、l⩽2L/c 收尾）；Proof of Theorem 13 开头（测地球与测地坐标 ds² 式、伸缩映射 χ_B、诱导度量共形等价句、作用量密度 f_i 式与 §I.3 引用、Proposition 12 假设段、χ_α 图卡、共形不变推论句）
- 结果：**PASS±**（含三处 print quirk 复原）。
  - 与页图一致：`I(q,i')\to I(q)` 对角线论证句（引号原样）、`\int_{B_j}f_{i'}d\mu>c/2`、`L\geqslant\int_X f_{i'}d\mu\geqslant\sum_{j=1}^{l}\int_{B_j}f_{i'}d\mu\geqslant\frac12 lc`、`\chi_B\colon B^4\to B,\ y^i\to ry^i=x^i`、`f_i=|F(\tilde A_i)|^2,\ \int_X f_i d\mu=8\pi^2`、300dpi 确认 `by §I.3` 为罗马 I（沿用 p.1 规则，md 正确）、`\chi_\alpha\colon B^4\to B_\alpha`、`\chi_\alpha^*(A_{i'})`、`½B^4`。
  - **修复×3（print quirk 复原）**：行 774 `\delta_{ij}+O|x|^{2}` 与行 783 `r^{2}O|y|^{2}`、`O(r^{2})` 三处——600dpi 放大确认印刷均为**窄长直边数字 0**（非大写 O；同页 §I.3 的 I 与之对照清晰），数学上应为 big-O 系原刊排印用零；Luna 曾按数学预期静默作 O，按 print quirk 忠实原则复原为 0 并在此登记。ABBYY 文本层第二通道：一行作 `0(r2)`、另一行作 `θ`（OCR 自身不定），以 600dpi 页图为准。
  - 排版级伪影（登记不改）：*Proof of Theorem 13.* 斜体拍平；行 797 末句 "diagonal argument" 印刷无引号（md 亦无，一致；与行 755 带引号用法并存系印刷原样）。
- 修复登记：行 774 `O|x|^{2}`→`0|x|^{2}`；行 783 `r^{2}O|y|^{2}`→`r^{2}0|y|^{2}`、`O(r^{2})`→`0(r^{2})`（依据 `audit-redo/p020.png` + 600dpi 裁片）。

### p.021（PDF p.21 / 印刷 p.299）

- PNG：`audit-redo/p021.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（"compatability" 拼写、"(3) above" 交叉引用，结论记于本条）
- 核对：III.2 证明收尾（连接矩阵 A_{i'}(α)→A_∞(α) 式、转移函数与 compatability 句、式(1)、g_{i'} 有界与子序列收敛段、(A_∞(α),g_∞(α,β)) 数据段、式(2)、Uhlenbeck 可去奇点段、式(3)、κ₁⋯κ_l 紧集段、ρ_{i'}:Q|_K→P|_K、归纳构造句、Tc₂ 极限式、l=0/1 分类 (i)(ii)）
- 结果：**PASS±**（无修复，两条新 print quirk 登记）。
  - 与页图一致：`A_{i'}(\alpha)\to A_\infty(\alpha)\ in\ C^\infty(\frac12 B_\alpha)`、式(1) 全式（含 `dg_{i'}(\alpha,\beta)g_{i'}(\alpha,\beta)^{-1}` 前置负号与 `\tag{1}`）、式(2)（含 `\lim` 与 `\tag{2}`）、式(3) `\frac{1}{8\pi^2}\int_{B_j}|F(\tilde A_i)|^2d\mu=\frac{1}{8\pi^2}\int_{B_j}Tr(F\wedge F)=-Tc_2(\tilde A_i|_{\partial B_j}),\ \mod\mathbf{Z}`（300dpi 确认粗体 **Z**）、`K\subset X\setminus\{\kappa_1,\cdots,\kappa_l\}`（300dpi 确认印刷为 kappa 字形，md `\kappa` 忠实；与本页他处 `x_j` 用字不一系印刷原样）、`\rho_{i'}\colon Q|_K\to P|_K`、`Tc_2(A_\infty|_{\partial B_j})=\lim_{i'}Tc_2(\tilde A_{i'}|_{\partial B_j})`、`[21,\ \S3]`、`A_{i'}\ in\ \mathcal{Q}`（草书 𝒬，md 本就正确）、`§I.3` 罗马 I。
  - **印刷 quirk 登记（不改，300dpi 确认）**：① 行 805 "compatability condition"（compatibility 之排印误植，印刷连字符断词 com-/patability，md 忠实保留）；② 行 819 "strict inequality in (3) above"——数学上应指式(2)，印刷确作 (3)，系原刊交叉引用笔误，md 忠实保留。
  - 排版级伪影（登记不改）：行 837 *either* 斜体拍平为正体。
- 修复登记：无。

### p.022（PDF p.22 / 印刷 p.300）

- PNG：`audit-redo/p022.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（三处 moduli space 的 M 字形，结论记于本条）
- 核对：节标题 III.3；开篇段（紧化句、§I.4、Taubes 映射 X×(0,λ₀)→ℳ 显示式、[19] 微分同胚句、p 映射定义段、"radius"/"smooth" 引号句）；β bump function 段与 χ_{[-1,1]}；β_s(x,y)=β(d(x,y)/s) 式；f=|F(I_{0,1})|² on R⁴ 式；R_I:R⁴×R→R 与 R_I(x,s)=∫β_s(x,y)f(y)dμ_y 式；性质 (i)(ii)；open property 句；Definition 15 (a)(b)
- 结果：**PASS±**（含三处草书 ℳ 拍平/误作 Fraktur 修复）。
  - 与页图一致：`\lambda_0>\lambda>0`、`\beta_s(x,y)=\beta(d(x,y)/s)`、`f=|F(I_{0,1})|^2` on `\mathbf{R}^4`、`R_I\colon\mathbf{R}^4\times\mathbf{R}\to\mathbf{R}`、`R_I(x,s)=\int_{\mathbf{R}^4}\beta_s(x,y)f(y)d\mu_y`、`\partial R_I/\partial s\neq0`、`R_I(x,s(x))=4\pi^2`、minimum value K、`\beta` dominated by `\chi_{[-1,1]}`、Definition 15 (a) `R_A(x,s)=\int\beta_s(x,y)|F(A)_y|^2d\mu_y` 与 (b) `\lambda(A)=K^{-1}\min\{s\mid\exists x,\ R_A(x,s)=4\pi^2\}`；`§I.4` 罗马 I（300dpi 确认）。
  - **修复×3**：行 845 "the moduli space M"、行 848 显示式目标 `\mathfrak{M}`、行 851 "an open subset of M"——300dpi 裁片确认三处印刷均为**圆弧草书 ℳ**（同 p.008 行 297 "the moduli space ℳ" 字形；非本文 Fraktur 𝔐_{λ₀} 的角状字形）→ 分别 Edit 为 `$\mathscr{M}$`、`\mathscr{M}`、`$\mathscr{M}$`（行 848 的 Fraktur 系 Luna 误标，另两处系拍平）。后文 X×(0,λ₀)→ℳ 语境继续沿用此规则。
  - 排版级伪影（登记不改）：**Definition 15.** 粗体与斜体引言拍平；"Taubes construction" 印刷无所有格 's，md 忠实保留。
- 修复登记：行 845 `M`→`$\mathscr{M}$`；行 848 `\mathfrak{M}`→`\mathscr{M}`；行 851 `M`→`$\mathscr{M}$`（依据 `audit-redo/p022.png` + 300dpi 三字形裁片）。

### p.023（PDF p.23 / 印刷 p.301）

- PNG：`audit-redo/p023.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（Theorem 16(i) 的 M 字形、行 887 的 μ、行 915 "possibly"，结论记于本条）
- 核对：λ(A) 释义段（含 [A_i]∈μ 句）；conformal chart 段与 χ_λ:(r/λ)B⁴⊂R⁴→B(x,r)⊂X 式；Â=χ*_λ(A) 与 λ²m̂ 段；Theorem 16 (i)(ii) 全文与曲率界显示式 |F(Â(y))|⩽const.|y|^{-4+δ}；Note 段；Proof (i)（∫_{R⁴}|F(Â)|²dμ⩽8π² 式、m̂_i 收敛论证段、λ(Â_i)=1 正规化句、§I.4 引用）；possibly 句；(ii) Appendix 引导句
- 结果：**PASS±**（含一处草书 ℳ 误作 Fraktur 修复）。
  - 与页图一致：`\chi_\lambda\colon(r/\lambda)B^4\subset\mathbf{R}^4\to B(x,r)\subset X`、`\hat A=\chi_\lambda^*(A)`、`\lambda^2\hat m`（hat 在 m 上）、`|F(\hat A(y))|\leqslant\mathrm{const.}|y|^{-4+\delta},\ y\in\mathbf{R}^4,\ |y|\leqslant\frac12 r\lambda^{-1}`、`\int_{\mathbf{R}^4}|F(\hat A)|^2d\mu\leqslant 8\pi^2`、`\lambda(\hat A_i)=1`、`§I.4`/`§III.4` 罗马 I。
  - **修复×1**：行 897 Theorem 16(i) `$[A]\in\mathfrak{M}$` → `$\mathscr{M}$`——300dpi 确认印刷为圆弧草书 ℳ（同 p.022 字形规则）。
  - **印刷 quirk 登记（不改，300dpi 确认）**：① 行 887 `[A_{i}]\in\mu`——印刷确为小写希腊 μ（语义应为 𝔐，同 p.16 μ^σ 类误植），md 忠实保留；② 行 915 "for every possibly subsequence"（possible 之排印笔误，印刷原样），md 忠实保留。
  - 排版级伪影（登记不改）：**Theorem 16.**/**Note.**/*Proof.* 粗斜体拍平。
- 修复登记：行 897 `\mathfrak{M}`→`\mathscr{M}`（依据 `audit-redo/p023.png` + 300dpi 裁片）。

### p.024（PDF p.24 / 印刷 p.302）

- PNG：`audit-redo/p024.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片×3（Corollary 17 显示式与延伸句、invariant 拼写、末段 𝔐_{λ₀}/𝔐∖𝔐_{λ₀}，结论记于本条）
- 核对：Corollary 17 全文与 p:ℳ_{λ₀}={...}→X×(0,λ₀) 两行显示式、extends 句与 bound 显示式；Proof（2λ 分离句、conformally invariant 句、|F(Â)|²_{m̂} 收敛段、Likewise 段、dλ(Â)/dt 三行显示式、Similarly 与 ‖d/dt x(Â)‖=H^{-1}{...} 显示式、Hessian 句）；rechoose λ₀ 段与 ℳ∖ℳ_{λ₀} 紧性句
- 结果：**PASS±**（含七处草书 ℳ 误作 Fraktur 修复）。
  - 与页图一致：`|\frac{d}{dt}p(A_t)|\leqslant\mathrm{const.}\lambda(A_0)\|\frac{d}{dt}F(A_t)\|_{L^2}`、`\frac12` 作用量句、`|F(\hat A)|^2_{\hat m}`、`f=|F(I_{0,1})|^2`、`\frac{d\lambda(\hat A)}{dt}\Big|_{t=0}=k^{-1}\int_{\mathbf{R}^4}\beta_k(0,y)\dot f_t(y)|_{t=0}d\mu_y` 三行链（⩽ const.∫|\dot f_t|dμ_y ⩽ const.‖F(Â)‖_{L²}‖d/dt F(Â_t)‖_{L²}）、`\|\frac{d}{dt}x(\hat A)\|_{t=0}=H^{-1}\{\int_{\mathbf{R}^4}[\operatorname{grad}_y\beta_k(0,y)]\dot f_t(y)|_{t=0}d\mu_y\}`、300dpi 确认 "conformally invariant" 拼写正确。
  - **修复×7**：行 922 显示式两处、行 925 两处、行 951 三处 `\mathfrak{M}`/`\mathfrak{M}_{\lambda_0}` → `\mathscr{M}`/`\mathscr{M}_{\lambda_0}`——300dpi 裁片确认本页七处印刷均为圆弧草书 ℳ；同裁片内 `𝔅` 为角状 Fraktur 提供页内字形对照，故 `\mathfrak{B}` 不动。
  - **印刷 quirk 登记（不改）**：① Definition 15(b) 印刷作大写 K⁻¹ 而本页 Proof 印刷作小写 k^{-1}、β_k——K/k 混用系印刷原样，md 两处均忠实；② 行 887 类 μ 字形本页无。
  - **跨页字形张力（登记待后续页留意）**：p.018 Theorem 11 处已按 `\mathfrak{M}_{\lambda_0}` 提交（当时 300dpi 仲裁记录为下标 λ₀ 正确）；本页同记号印刷为草书 ℳ_{λ₀}。两页证据图（p018.png/p024.png）均在档；本块不对已提交页改判，III.3 后续页遇 `𝔐_{λ₀}` 一律先 300dpi 仲裁再定 Fraktur/草书。
  - 排版级伪影（登记不改）：**Corollary 17.**/*Proof.* 粗斜体拍平；斜体陈述段拍平。
- 修复登记：行 922 两处 `\mathfrak{M}`→`\mathscr{M}`；行 925 两处 `\mathfrak{M}_{\lambda_0}`→`\mathscr{M}_{\lambda_0}`；行 951 三处 `\mathfrak{M}`/`\mathfrak{M}_{\lambda_0}`→`\mathscr{M}`/`\mathscr{M}_{\lambda_0}`（依据 `audit-redo/p024.png` + 300dpi 裁片×3）。

### p.025（PDF p.25 / 印刷 p.303）

- PNG：`audit-redo/p025.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片×3（Prop 18 首句、(ii) 句 Ω²₋ 与 ℳ_{λ₀}、Theorem 19/Proof 的四个显示式，结论记于本条）
- 核对：Proposition 18 (i)(ii)(iii) 全文；Proof (i)(ii)(iii)（re-statement 句、ω/ω′ 比较段含 ‖d*_Aω‖²_{L²}=μ(A) 与 ‖d*_θω′‖²_{L²}⩾μ₁‖ω′‖²_{L²}、[18, Proposition 8.8] 句、L⁴-norm 变换句、(1/|y|^{[4−δ(r)]}) 显示式）；Theorem 19 与 p 显示式、is a covering map 句；Proof 开头与 dp:(T𝔐)_{[A]}→(TX)_{x(A)}×R、§II.2 句、α:(TX)_{x(A)}×R→(T𝔐)_{[A]}、dp∘α invertible 句、式(1)（\tag{1}，III.3 节内重新编号系印刷原样）、α 定义段与 V=β_{r/2}(v^i+φx^i)∂/∂x^i 显示式
- 结果：**PASS±**（含八处修复：6 处草书 ℳ 误作 Fraktur + 2 处 Ω²₋ 上标/伴生 (𝔤) 修复）。
  - 与页图一致：`[A]\to\theta` in `C^\infty(X\setminus B(x(A),r))`、`\|F(A)\|_{L^4}\leqslant\mathrm{const.}\lambda(A)^{-1}`、`\omega'=(1-\beta_r)\omega`、`B(x(A),r)`、`(1/|y|^{[4-\delta(r)]})`、`p\colon\mathscr{M}_{\lambda_0}\to X\times(0,\lambda_0)`（修复后）、`(T\mathscr{M})_{[A]}`（修复后）、`§II`/`§II.2` 罗马 II、`|(dp\circ\alpha)\xi-\xi|<|\xi|` for all `\xi\in TX\times\mathbf{R}`（\tag{1}）、`\delta(r)<1`、`V=\beta_{r/2}(v^i+\phi x^i)\frac{\partial}{\partial x^i}`。
  - **修复×8**：① 行 953 `[A]\in\mathfrak{M}_{\lambda_0}`→`\mathscr{M}_{\lambda_0}`；② 行 957 第一处 `\Omega_-(\mathfrak{g})`→`\Omega^2_-(\mathfrak{g})`（300dpi 确认印刷有上标 ²，同 p.008 行 263/269 缺陷类）；③ 行 957 第二处 `\Omega_-(\mathfrak{g})`→`\Omega^2_-`（300dpi 确认印刷**无** (𝔤)，Δ on Ω²₋ 后直接接 as）；④ 行 957 `\mathfrak{M}_{\lambda_0}`→`\mathscr{M}_{\lambda_0}`；⑤ 行 976 显示式 `\mathfrak{M}_{\lambda_0}`→`\mathscr{M}_{\lambda_0}`；⑥ 行 984 `(T\mathfrak{M})_{[A]}`→`(T\mathscr{M})_{[A]}`；⑦ 行 987 `[A]\in\mathfrak{M}`→`\mathscr{M}`；⑧ 行 990 `(T\mathfrak{M})_{[A]}`→`(T\mathscr{M})_{[A]}`（均 300dpi 圆弧草书裁决）。
  - 排版级伪影（登记不改）：*Let*/*covering map*/*Proof.* 斜体拍平；**Proposition 18.**/**Theorem 19.** 粗体拍平。
- 修复登记：行 953、957、976、984、987、990（详见上，共 8 处；依据 `audit-redo/p025.png` + 300dpi 裁片×3）。

### p.026（PDF p.26 / 印刷 p.304）

- PNG：`audit-redo/p026.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片×4 + 600dpi 终裁（ℬ/𝔅、ℳ、ℒ、P/p 指数、c/dt、括号闭合，结论记于本条）
- 核对：α 定义句与 [A_t]=q(f_t(A))∈ℳ 段（flow on ℬ、Taubes' map、Proposition 5）；α(ξ)=d/dt[A_t]|_{t=0}∈(T𝔐)_{[A]} 句与 property (1) 检查段（m_t 路径、ω∈Λ²R⁴）；d/dt|ω−*_{m_t}ω|⩽const.|ω||π(dm/dt)| 式；"trace free" 句；d/dt|F₋(f_t(A)|⩽const.|F(A)||πℒ_V m| 式；All derivatives 括注（ℒ_V Lie derivative）；|πℒ_V m|⩽const.ρ|ξ| 式；left-hand side 句；|F(A)| 两行界式（λ^{-2} 与 λρ^{-3}）；So 段与 d/dt‖F₋(f_t(A))‖_{L^p} 积分式；which gives 段与 L²/L^{4/3} 两范数式；each bounded 句；‖d/dt(A_t−f_t(A))‖_{L²₁(A)} 三行式
- 结果：**PASS±**（含五处草书字形修复）。
  - 与页图一致：`f_t=1` outside `B(x(A),r/2)`、`\alpha(\xi)=\frac{d}{dt}[A_t]|_{t=0}`、`\omega\in\Lambda^2\mathbf{R}^4`、`*_{m_t}\omega`、两行界式 `\text{const}\lambda^{-2}|\xi|`/`\text{const}\lambda\rho^{-3}|\xi|`（const 后无句点，印刷原样）、积分式全部小写 p（300dpi 否决初读疑 P：`(\rho\lambda^{-2})^p`、`(\lambda\rho^{-3})^p`、`^{1/p}`、`L^p` 均小写，md 正确）、`L^2_1(A)` 下标、`+\lambda^{-1}\frac{d}{dt}\|F_-(f_t(A))\|_{L^{4/3}}`。
  - **修复×5**：① 行 1005 `[A_t]=q(f_t(A))\in\mathfrak{M}`→`\mathscr{M}`；② 行 1007 `(T\mathfrak{M})_{[A]}`→`(T\mathscr{M})_{[A]}`；③④⑤ 行 1016/1019/1022 三处 Lie 导数 `\mathfrak{L}_V`→`\mathscr{L}_V`（300/600dpi 确认印刷为圆弧草书 ℒ，非 Fraktur 角状 L）。
  - **印刷 quirk 登记（不改，高倍确认）**：① 行 1005 "a flow on $\mathcal{B}$"——印刷为**圆弧草书 ℬ**，与本文他处角状 Fraktur 𝔅 并存（p.024 裁片页内对照），md `\mathcal{B}` 忠实；② 行 1016 显示式印刷即为 `|F_-(f_t(A)|`——外层右括号漏排（内层 `(A)` 闭合后直接范数直杠；同页行 1034/1046 的 `‖F_-(f_t(A))‖` 双括号齐全提供对照），600dpi 确认，md `\left(f_{t}(A)\right|` 忠实；③ 行 1046 首项印刷为 `\frac{c}{dt}`（第二行 `\frac{d}{dt}` 提供页内 d 字形对照，c 系 d 之排印误植），md `\frac {c}{d t}` 忠实。
  - 排版级伪影（登记不改）：斜体陈述段拍平。
- 修复登记：行 1005 `\mathfrak{M}`→`\mathscr{M}`；行 1007 `(T\mathfrak{M})_{[A]}`→`(T\mathscr{M})_{[A]}`；行 1016/1019/1022 `\mathfrak{L}_V`→`\mathscr{L}_V`×3（依据 `audit-redo/p026.png` + 300dpi 裁片×4 + 600dpi 裁片）。

### p.027（PDF p.27 / 印刷 p.305）

- PNG：`audit-redo/p027.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（III.4 开头三处 M 字形，结论记于本条）
- 核对：Lemma 23 证明第一段收尾（since by Proposition 18 句、|d/dt p(A_t)−d/dt p f_t(A)|⩽const.λ|ξ| 式、i.e. 句、|(dp∘α)ξ−d/dt p f_t(A)|⩽const.λ|ξ| 式、flat 度量句、|(dp∘α)ξ−ξ|⩽const.λ.|ξ| 式、property (1) satisfied 句）；节标题 III.4.（印刷带标题粗体）；III.4 开篇段（diffeomorphism 归约句、x(A)=x(B)=x₀, λ(A)=λ(B)=λ 显示式、short path in 𝔐 句、flat in B(x₀,r) 括注、small lemma 句）；Lemma 20 全文（annulus {x∈R⁴|R/2<|x|<2R} 显示式、‖F(A)‖_{C⁰}⩽K/R² 句、2RB⁴、‖F(Ã)‖_{C⁰}⩽C.‖F(A)‖_{C⁰} 式）；Proof（conformal re-scaling 句）
- 结果：**PASS±**（含三处草书 ℳ 拍平/误作 Fraktur 修复）。
  - 与页图一致：`\|F(A)\|_{L^4}\leqslant\text{const.}\lambda^{-1}`、`\|\frac{d}{dt}(F(A_t)-F(f_t(A)))\|_{L^2}\leqslant\text{const.}|\xi|`、两处 dp∘α 显示式、`x(A)=x(B)=x_0,\ \lambda(A)=\lambda(B)=\lambda`、`B(x_0,r)`、`\{x\in\mathbf{R}^4\mid R/2<|x|<2R\}`、`\|F(A)\|_{C^0}\leqslant K/R^2`、`2RB^4`、`\|F(\tilde A)\|_{C^0}\leqslant C.\|F(A)\|_{C^0}`、`R^{-1}`/`R^2`。
  - **修复×3**：①② 行 1071 `p\colon\mathfrak{M}_{\lambda_0}`→`\mathscr{M}_{\lambda_0}` 与 `[A],[B]\in\mathfrak{M}_{\lambda_0}`→`\mathscr{M}_{\lambda_0}`；③ 行 1077 "a short path in M"→`in $\mathscr{M}$`（本处 Luna 拍平为普通 M）——300dpi 裁片确认三处印刷均为圆弧草书 ℳ。
  - 行 1095 的 `![](images/page_27_image_0.jpg)` 图引用为 MinerU 导出伪影（印刷该页无插图），维持原样不删。
  - 排版级伪影（登记不改）：**III.4.**/**Lemma 20.**/*Proof.* 粗斜体拍平。
- 修复登记：行 1071 两处、行 1077 一处 `\mathfrak{M}`/`M`→`\mathscr{M}`（依据 `audit-redo/p027.png` + 300dpi 裁片）。

### p.028（PDF p.28 / 印刷 p.306）

- PNG：`audit-redo/p028.png`（pngmono 150dpi）；本页为整页插图页，无字形仲裁需求
- 核对：整页示意图（印刷 p.306）与 md 行 1095 `![](images/page_27_image_0.jpg)` 的对应；图下正文段 "Thus once K is small enough … exponential gauge … [20, §2] … satisfies"（行 1097）；显示式 `\|A\|_{C^0}\leqslant\text{const.}\|F(A)\|_{C^0}.`（行 1100）
- 结果：**PASS±**（无修复）。
  - 插图核验：已 Read `mineru/Donaldson_1983_gauge_theory_4manifolds/images/page_27_image_0.jpg` 与页图对照——三层示意图完全一致（S⁴ 带影线帽 C_λ 与 "Connections A′, B′ over S⁴"；R⁴ 平面带 rλ^{-1}、λ^{-1/2} 标注与 "Connections Ã, B̂ close to the basic instanton I_{0,1}"；X 带点 W、B(x₀,r) 与 "Connections A₁, B₁ on the trivial bundle."）；图注文字在图片内、md 未抽为正文，系 MinerU 表示方式，无内容缺失。**登记**：MinerU 图片命名为零基页号（`page_27_*` 对应 PDF p.28/印刷 p.306），后续按图定位勿按名字面页号。
  - 与页图一致："exponential gauge" 引号、`[20, §2]`、`\|A\|_{C^0}\leqslant\text{const.}\|F(A)\|_{C^0}.` 逐字吻合。
  - 本页 md 范围为行 1095–1101；行 1103 起（Then set Ã=(1−β)A）属 p.29。
- 修复登记：无。
