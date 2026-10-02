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
  - **修复**：md 行 95 "so Q is an affine space" 的普通 `Q` 与同段行 89/109 的 `$\mathcal{Q}$` 不一致；300dpi 裁片确认印刷两处同为草书 𝒬 → 已 Edit 改为 `so $\mathcal{Q}$ is an affine space`。
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
