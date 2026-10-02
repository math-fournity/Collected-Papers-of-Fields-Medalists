# 逐页审计：Yoccoz_1995_siegel_bruno

- actor：Peer-P35
- model：gpt-6-luna
- reasoning effort：max
- 角色：CONTRIBUTOR；canonical integrator：Master-Luna
- 审计基线：`037602429d3b009f6fc468c732073eb3ddf9875f`（任务基线 main HEAD）
- PDF：`Yoccoz_1995_siegel_bruno.pdf`，91 页；Creator=`NUMDAM`；Producer=`pdfTeX-1.40.16`
- 审计模式：born-digital；`pdftotext -layout` 全文 214,249 bytes、91 个 PDF 页、未发现 U+FFFD。MinerU Markdown 为 192,927 bytes。复杂公式按文本层可读性及疑点回到对应原页图核验。
- MinerU 导出：`MinerU 3.4.4`；`structured_content.json` 与 `middle_json.json` 各含 91 个按 PDF 顺序的 0-based `page_idx`。现存导出元数据未提供 `doc_id` 字段，故 `doc_id=UNKNOWN`。
- 唯一修订对象：`Yoccoz_1995_siegel_bruno__Yoccoz_1995_siegel_bruno.md`。原始 SHA-256：`d759402aa8951c595188350424cd206df0bc40c3d088b26247bc754873856de2`。
- 本文件只记录 Peer-P35 的本篇候选证据；根级 AUDIT-INDEX.md、AUDIT-PROGRESS.log、README.md、MEMORY.md 由 Master-Luna 独占维护。

## 逐页记录

### p.001（PDF p.1 / 印刷页无页码）
- PNG：`audit/Yoccoz_1995_siegel_bruno_p001.png`（pngmono 150dpi）
- 核对：卷名、作者、论文题名、Astérisque 卷页、Numdam URL、版权和数字化来源。
- 结果：PASS。
- 证据与复核：PDF 第 1 页文本层和 150dpi 原页图一致；MinerU 文本包含同一题名页信息。PDF 文本层将作者姓名拆成字距字符，原页图确认印刷为 “JEAN-CHRISTOPHE YOCCOZ”；MinerU Markdown 已正确恢复。题名在 Markdown 中合并了印刷换行，字符和词序一致。
- 时间：2026-10-01 16:29 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.002（PDF p.2 / 印刷页无页码）
- 核对：卷号与期刊页眉、年份、卷名、作者、出版机构和 CNRS 资助页脚。
- 结果：PASS±（内容无误；重复卷名页眉和出版机构/CNRS 页脚未进入 MinerU Markdown）。
- 证据与复核：PDF 第 2 页文本层与 `structured_content.json` 的 `page_idx=1` 相符；Markdown 收录 1995、`PETITS DIVISEURS EN DIMENSION 1` 和作者，未保留印刷的 `231 ASTÉRISQUE` 页眉及出版机构页脚。缺项均属页眉/页脚，不影响题名或作者识别。
- 时间：2026-10-01 16:30 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.003（PDF p.3 / 印刷页无页码）
- 核对：AMS 分类编号。
- 结果：PASS±（一行出版分类元数据缺失；文章正文、定理或公式未受影响）。
- 证据与复核：PDF p.3 文本层印有 `Classification A.M.S. : 30C10, 30C62, 58F03, 58F23, 58F27.`；该行未见于相应 MinerU Markdown。按其题名页元数据性质记作轻微遗漏，不作正文错误判断。
- 时间：2026-10-01 16:33 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.004（PDF p.4 / 印刷 p.1）
- 核对：卷级目录的两个篇名及起始页码。
- 结果：PASS±（目录内容吻合；印刷页脚数字 `1` 未保留）。
- 证据与复核：PDF p.4 文本层列出 Yoccoz 篇起始页 `3` 和下一篇起始页 `89`；Markdown 对应目录条目及页码一致。仅遗漏印刷 folio。
- 时间：2026-10-01 16:34 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.005（PDF p.5 / 空白页）
- 核对：页内容与 MinerU 页映射。
- 结果：PASS。
- 证据与复核：PDF 文本层为空；`structured_content.json` 的 `page_idx=4` 没有 blocks；该页没有对应正文内容，符合空白页。
- 时间：2026-10-01 16:34 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.006（PDF p.6 / 印刷 p.3）
- PNG：`audit/Yoccoz_1995_siegel_bruno_p006.png`（pngmono 150dpi）
- 核对：论文法文题名、作者、目录章节顺序及内部页码。
- 结果：PASS±（题名与目录吻合；印刷 folio `3` 未保留，换行合并）。
- 证据与复核：150dpi 原页确认题名 `THÉORÈME DE SIEGEL, NOMBRES DE BRUNO ET POLYNÔMES QUADRATIQUES`、`Jean-Christophe YOCCOZ` 及目录各节页码；MinerU Markdown 的题名、作者、章节顺序和页码一致。PDF 文本层将目录中的 `R(α)` 字形映射为 `R(a)`，原页和 Markdown 均确认此处为 `R(α)`。仅有排版换行和印刷页脚省略。
- 时间：2026-10-01 16:35 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.007（PDF p.7 / 空白页）
- 核对：页内容与 MinerU 页映射。
- 结果：PASS。
- 证据与复核：PDF 文本层为空；`structured_content.json` 的 `page_idx=6` 没有 blocks；Markdown 在题名页目录与 `INTRODUCTION` 之间没有对应正文内容，符合空白页。
- 时间：2026-10-01 16:36 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.008（PDF p.8 / 印刷 p.5）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p008_300dpi.png`（pnggray 300dpi）
- 核对：Introduction 首页、形式共轭记号、单位根条件及公式 `f_{n,a}(z)`。
- 结果：PASS±（正文和公式与印刷相符；印刷 folio `5` 未保留；PDF 文本层对数学字形映射有损）。
- 证据与复核：300dpi 原页逐项确认 `\widehat{G}`、`p\wedge q=1`、`q\geq1` 以及 `f_{n,a}(z)=\lambda z(1+z^{nq}+az^{2nq})`；MinerU Markdown 对应项一致。PDF 文本层将这些字形压平或错映射，未据此判为 Markdown 错误。
- 时间：2026-10-01 16:37 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.009（PDF p.9 / 印刷 p.6）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p009_300dpi.png`（pnggray 300dpi）
- 核对：Cremer 条件 `(Cr)`、Siegel 条件 `(S)`、Bruno 条件 `(B)` 及主定理陈述。
- 结果：PASS±（关键公式与定理吻合；页眉/folio 未保留；记录源级印刷拼写 quirk）。
- 证据与复核：300dpi 原页确认 `(Cr)` 为 `\sup_{n\geq0}(\operatorname{Log}q_{n+1})/q_n=+\infty`，`(S)` 为 `\operatorname{Log}q_{n+1}=\mathcal{O}(\operatorname{Log}q_n)`，`(B)` 为 `\sum (\operatorname{Log}q_{n+1})/q_n<+\infty`，其后的主定理必要充分条件也与 Markdown 一致。PDF 文本层对 Greek/Fraktur/算符映射有损，未将抽取字形误差归为 Markdown 差异。
- 源级 quirk：印刷正文为 `elle-mêmes`（PDF p.9 / 印刷 p.6）；Markdown 忠实保留，不更正。
- 时间：2026-10-01 16:39 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.010（PDF p.10 / 印刷 p.7）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p010_300dpi.png`（pnggray 300dpi）
- 核对：Cherry/Siegel/Bruno 相关段落、函数 `\Phi` 的定义与函数方程、定理 I.2.6 的半径估计。
- 结果：PASS±（内容与数学表达相符；印刷 folio `7` 未保留，PDF 文本层符号映射有损）。
- 证据与复核：300dpi 原页确认 `\Phi(\alpha)=\operatorname{Log}\alpha^{-1}+\alpha\Phi(1/\alpha)`（`0<\alpha<1/2`）及 `|\operatorname{Log}R_\alpha^{-1}-\Phi(\alpha)|\leq C`；Markdown 对应式一致。正文中 “l’énoncé” 原页清楚可辨，Markdown 亦正确；文本层的 `Pénoncé` 为抽取错映射，不是印刷或 Markdown 错误。
- 时间：2026-10-01 16:40 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.011（PDF p.11 / 印刷 p.8）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p011_300dpi.png`（pnggray 300dpi）
- 核对：PSL₂(ℤ) 变换、`0<α<1/2` 与 `α>2` 的两种情形、收敛半径估计及第 II 章概述。
- 结果：PASS±（数学记号和论述吻合；页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `$\alpha \gg 2$` 为印刷双大于号，Markdown 的 `>>` 忠实保留；另核对 `\operatorname{Log}d_f^{-1}`、`\operatorname{Log}d_g^{-1}`、`P_\lambda(z)=\lambda z(1-z)`、`(B)` 与定理 I.6.5 引用，Markdown 表达与印刷一致。PDF 文本层把箭头/帽子/希腊字母拆平，本页图像已终裁。
- 时间：2026-10-01 16:41 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.012（PDF p.12 / 印刷 p.9）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p012_300dpi.png`（pnggray 300dpi）
- 核对：关于函数 `U` 的未证性质、附录概述及致谢。
- 结果：FAIL（1 处正文单词误识）。
- 差异：印刷原文为 `démontrer (ou d’infirmer)`；MinerU Markdown 为 `démontrer (ou d’infirmier)`。
- 修复建议：将唯一对应位置的 `infirmier` 改为 `infirmer`。依任务约束，待 91 页审计结束后用 Edit 逐处修复。
- 补充引文核对：2026-10-02 04:01 EDT；actor=Peer-P35；model=gpt-6-luna/max。600dpi 原页裁片将附录引文标签读为 `[Il]`，与 MinerU Markdown 第 150 行一致；`pdftotext` 派生文本读成 `[II]`，该字形以页面图像为准，此处无需修正文稿。
- 证据与复核：300dpi 原页清楚显示动词 `infirmer`；PDF 文本层也读作 `infirmer`。Markdown `infirmier` 改变该句词义，属实质性正文差异。
- 时间：2026-10-01 16:42 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.013（PDF p.13 / 空白页）
- 核对：页内容与 MinerU 页映射。
- 结果：PASS。
- 证据与复核：PDF p.13 文本层为空；`structured_content.json` 的 `page_idx=12` 为 0 blocks；该页无对应正文内容，符合空白页。
- 时间：2026-10-01 16:44 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.014（PDF p.14 / 印刷 p.11）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p014_300dpi.png`（pnggray 300dpi）
- 核对：第一章标题、整数部分/小数部分/最近整数记号、`\tilde A` 定义及连分数递推初值。
- 结果：PASS±（定义与公式一致；页眉/folio 未保留，PDF 文本层有字形映射损失）。
- 证据与复核：300dpi 原页确认 `\|x\|=\min(\{x\},1-\{x\})`、`\langle x\rangle` 的半整数约定、`\tilde A(x)=\{x^{-1}\}`、`\tilde a_n=[\tilde\alpha_{n-1}^{-1}]` 及 `p_{-2}=q_{-1}=0, p_{-1}=q_{-2}=1`；MinerU Markdown 对应项一致。抽取文本中的符号错映射未进入 Markdown。
- 时间：2026-10-01 16:45 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.015（PDF p.15 / 印刷 p.12）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p015_300dpi.png`（pnggray 300dpi）
- 核对：通常连分数公式、`\tilde\beta_n` 递推及估计、改进连分数映射 `A` 和 `\epsilon_n` 关系。
- 结果：PASS±（公式与文字相符；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页逐项核验 `\alpha=(p_n+p_{n-1}\tilde\alpha_n)/(q_n+q_{n-1}\tilde\alpha_n)`、行列式关系、两项 `\tilde\beta` 恒等式、`(q_{n+1}+q_n)^{-1}<\tilde\beta_n<(q_{n+1})^{-1}`，以及 `A(x)=\|x^{-1}\|` 与改进递推；MinerU Markdown 对应内容一致。文本层公式字符映射损坏，原页图为终裁依据。
- 时间：2026-10-01 16:46 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.016（PDF p.16 / 印刷 p.13）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p016_300dpi.png`（pnggray 300dpi）
- 核对：映射 `k` 的递推、`\tilde\beta_n=\tilde\beta_{k(n)}`、`\Phi` 定义/性质及其与经典 Bruno 级数的关系。
- 结果：PASS±（记号和等式均吻合；印刷页眉/folio 未保留，文本层对公式映射有损）。
- 证据与复核：300dpi 原页确认 `k(n+1)` 按 `\epsilon_{n+1}` 分两支、`\tilde\beta_{k(n)+1}=\beta_n-\beta_{n+1}`、`\Phi(\alpha)=\sum_{i\geq0}\beta_{i-1}\operatorname{Log}\alpha_i^{-1}`，两项对称性及函数方程，及 `\sum q_i^{-1}\operatorname{Log}q_{i+1}<+\infty` 的经典定义；Markdown 与印刷一致。
- 时间：2026-10-01 16:47 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.017（PDF p.17 / 印刷 p.14）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p017_300dpi.png`（pnggray 300dpi）
- 核对：两种 Bruno 和式的有界差估计及推导式 (1)–(3)。
- 结果：PASS±（公式内容与原页一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页逐项核对首个总估计、`q_i^{-1}=\tilde\beta_{i-1}+q_{i-1}q_i^{-1}\tilde\beta_i`、`1/2\leq q_{i+1}\tilde\beta_i\leq1`，以及 (1)、(2)、(3) 的求和范围、正负号和误差项；MinerU Markdown 对应式一致。PDF 文本层对上下标和算符映射严重失真，未以该抽取结果作终裁。
- 时间：2026-10-01 16:48 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.018（PDF p.18 / 印刷 p.15）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p018_300dpi.png`（pnggray 300dpi）
- 核对：辅助量 `B_{k,i}` 定义、集合 `\mathcal I/\mathcal J`、引理四项与估计式 (4)。
- 结果：PASS±（公式、条件与引理陈述一致；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `B_{k,k+1}=0`、递推及其求和表达、`\mathcal I(\alpha)`/`\mathcal J(\alpha)` 的下标范围、引理 1–4 的结论和 (4) 的两侧严格不等号；MinerU Markdown 对应符号和范围一致。PDF 文本抽取破坏了公式字形，原页图终裁通过。
- 时间：2026-10-01 16:49 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.019（PDF p.19 / 印刷 p.16）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p019_300dpi.png`；裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p019_index_crop_300dpi.png`（均源自 pnggray 300dpi）
- 核对：技术引理证明中有限非空 `\mathcal I` 情形的分段递增整数列条件与后续估计。
- 结果：FAIL（1 处公式下标错误）。
- 差异：印刷条件为 `B_{k_\ell,k_{\ell-1}+1}\leq0`；MinerU Markdown 行 426 为 `B_{k_\ell,k_\ell-1+1}\leq0`，第二下标将前一项 `k_{\ell-1}` 错写为 `k_\ell-1`。
- 修复建议：把该位置第二下标改为 `k_{\ell-1}+1`；待全篇审计完成后通过 Edit 单独修复并回读。
- 证据与复核：PDF p.19 原页和放大裁片清楚显示 `k_{\ell-1}+1`；这一项控制后续递增分段的范围，当前 Markdown 下标改变了该条件。
- 时间：2026-10-01 16:52 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.020（PDF p.20 / 印刷 p.17）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p020_300dpi.png`（pnggray 300dpi）
- 核对：§2.1 形式线性化方程与归一化缩放；§2.2 单叶函数空间和上半平面提升定义。
- 结果：PASS±（定义及等式吻合；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `DH_f(0)=1`、`H_f(\lambda z)=f(H_f(z))`、`f_t(z)=t^{-1}f(tz)`、`R(f_t)=t^{-1}R(f)`，及 `FT=TF` 与 `\lim_{\operatorname{Im}z\to+\infty}(F(z)-z)=\alpha`；Markdown 的符号、方向和缩放指数一致。
- 时间：2026-10-01 16:53 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.021（PDF p.21 / 印刷 p.18）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p021_300dpi.png`（pnggray 300dpi）
- 核对：上半平面提升像、共形容量定义、单调性与距离界、Siegel 圆盘集合关系。
- 结果：PASS±（公式与定义一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `\Pi^{-1}(S_{E(\alpha)})=\bigcup_{n\in\mathbb Z}\widehat S_{\alpha+n}`、`C(U,x_0)=|Dk(0)|`、`C(V,x_0)\leq C(U,x_0)`、`d\leq C(U,x_0)\leq4d`，以及 `f(K_f)\subset K_f`、`f(U_f)\subset U_f` 和 `C(f)\leq1`；MinerU Markdown 对应项一致。
- 时间：2026-10-01 16:54 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.022（PDF p.22 / 印刷 p.19）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p022_300dpi.png`（pnggray 300dpi）
- 核对：共形表示与线性化共轭式、`R(f)\geq C(f)`，以及半连续性证明和 Proposition 2 条件。
- 结果：PASS±（等式、包含关系和条件吻合；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `\widetilde H_f^{-1}\circ f\circ\widetilde H_f(z)=Df(0)z`、`R(f)\geq C(f)>0`、`C(f)=0\Rightarrow R(f)=0`，半连续性证明中的 `H(Df(0)z)=f(H(z))`，以及 Proposition 2 的两项边界条件；Markdown 与印刷一致。
- 时间：2026-10-01 16:56 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.023（PDF p.23 / 印刷 p.20）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p023_300dpi.png`（pnggray 300dpi）
- 核对：Proposition 2 三种边界情形、共轭延拓公式、Corollary 中的下确界等式及 §2.6 定义。
- 结果：PASS±（包含关系、公式和下确界符号一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认三种 `\mathcal C` 情形及边界条件，`\widetilde f(z)=\widetilde H_f(\lambda\widetilde H_f^{-1}(z))`，`\inf_{f\in S_\lambda}C(f)=\inf_{f\in S_\lambda}R(f)`，以及 `R(\alpha)=\inf R(f)=\inf C(f)`；Markdown 符号方向和集合下标相符。
- 时间：2026-10-01 16:57 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.024（PDF p.24 / 印刷 p.21）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p024_300dpi.png`（pnggray 300dpi）
- 核对：Theorem I.2.6、Bruno/Siegel 半径估计、数值界及周期轨道判据。
- 结果：PASS±（定理与公式正确；两个数值常数有数字间空格；页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认定理条件和 `|\operatorname{Log}R(\alpha)+\Phi(\alpha)|\leq C`（为 `\leq`，不是 `<`）、估计 `\operatorname{Log}R(\alpha)\geq-C'\Phi(\alpha)-C''`、常数 `-15.24` 与 `139.75`，以及 `\sum_{n\geq0}q_n^{-1}\operatorname{LogLog}q_{n+1}<+\infty`。Markdown 对应数学内容一致；常数目前写作分隔数字 `- 1 5. 2 4`、`1 3 9. 7 5`，登记为可读性/检索候选，不据此判为错误数值。
- 时间：2026-10-01 16:59 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.025（PDF p.25 / 印刷 p.22）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p025_300dpi.png`（pnggray 300dpi）
- 核对：关于 `P_\alpha` 收敛半径的上界、`K_F`/`d_F` 定义及 2.8 的归约估计。
- 结果：PASS±（公式方向和指标范围正确；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `\log R(P_\alpha)<-(1-\varepsilon)\Phi(\alpha)+C'(\varepsilon)`、`K_F=E^{-1}(K_f)` 中迭代指标 `n\geq0`、`d_F=-(2\pi)^{-1}\log d(0,\mathbb C-K_f)`、`e^{-2\pi d_F}\leq C(f)\leq4e^{-2\pi d_F}` 及上确界误差 `\leq C_0`；Markdown 与印刷一致。
- 时间：2026-10-01 17:01 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.026（PDF p.26 / 印刷 p.23）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p026_300dpi.png`（pnggray 300dpi）
- 核对：2.9 中 Douady–Ghys 构造说明、Figure 1、回返映射段落及提升方程。
- 结果：FAIL（Figure 1 的 Markdown 图片链接失效）。
- 差异：PDF 原页含三角形 Figure 1，图中标记 `0`、`\ell`、`z_0`、`f(z_0)`、`f(\ell)` 和角 `2\pi\beta`。Markdown 第 754 行引用 `![](images/page_25_image_7.jpg)`，相对 Markdown 所在目录不存在；现存只读导出图片位于 `Yoccoz_1995_siegel_bruno/images/page_25_image_7.jpg`。
- 修复建议：将 Markdown 图片链接改为 `![](Yoccoz_1995_siegel_bruno/images/page_25_image_7.jpg)`；不移动或改写 MinerU 图片。待全篇审计后通过 Edit 修复。
- 证据与复核：PDF p.26 的 300dpi 原页显示 Figure 1；只读 `test -e` 检查确认当前链接目标缺失、上述导出内路径存在。该错链会使 Markdown 阅读者看不到原文图示。
- 时间：2026-10-01 17:03 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.027（PDF p.27 / 印刷 p.24）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p027_300dpi.png`（pnggray 300dpi）
- 核对：提升函数 `K` 的边界等式、首返映射 `G` 与 `T` 的交换式、极限及后续归约论证。
- 结果：PASS±（所有记号、指数和正负号吻合；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `\lim(F(z)-z)=\beta`、`\Im K(z)=0`、`K(F(z))=K(z)+1`、`G\circ T=T\circ G`、`\lim(G(z)-z)=-1/\beta` 及 `K(z)=\beta^{-1}z+c+o(1)`；Markdown 对应式一致。
- 时间：2026-10-01 17:05 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.028（PDF p.28 / 印刷 p.25）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p028_300dpi.png`（pnggray 300dpi）
- 核对：逆向构造所用的 `F^*` 共轭公式、§3 标题/范围及 `F(z)=z+\alpha+\varphi(z)` 表达。
- 结果：PASS±（共轭、符号和递推说明吻合；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `F^*(z)=-\overline{F(-\bar z)}`，以及 §3.2 的 `F(z)=z+\alpha+\varphi(z)`、`\varphi` 的周期性与上半平面极限；MinerU Markdown 对应项一致。PDF 文本层丢失复共轭字形，未将其误判为 Markdown 差异。
- 时间：2026-10-01 17:06 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.029（PDF p.29 / 印刷 p.26）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p029_300dpi.png`（pnggray 300dpi）
- 核对：Lemma 3.2 的 `D\varphi` 与 `\varphi` 界、诱导映射公式及畸变估计证明。
- 结果：PASS±（不等号、指数、分母和常数吻合；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `|D\varphi(z)|\leq 2e^{-2\pi\operatorname{Im}z}/(1-e^{-2\pi\operatorname{Im}z})`、`|\varphi(z)|\leq-\pi^{-1}\operatorname{Log}(1-e^{-2\pi\operatorname{Im}z})`、`D\varphi(z)=E(z)f'(E(z))/f(E(z))-1` 以及 `|u f'(u)/f(u)-1|\leq2|u|/(1-|u|)`；Markdown 表达一致。
- 时间：2026-10-01 17:07 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.030（PDF p.30 / 印刷 p.27）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p030_300dpi.png`（pnggray 300dpi）
- 核对：常数 `c_0`–`c_4`、估计 (1)/(2)、领域 `\mathcal U_F` 拼接定义及均匀化映射条件。
- 结果：PASS±（系数、分母、上下界及边界关系一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `c_1=e^{-2\pi c_0}<1/23`、`c_2=2c_1(1-c_1)^{-1}<1/11`、`c_3=\pi^{-1}\operatorname{Log}(1-c_1)^{-1}<1/71`，(1)/(2) 的指数及 `\min(1,\alpha)` 因子，均匀化关系 `K(F(z))=K(z)+1`，以及 §3.3 领域界；MinerU Markdown 对应一致。
- 时间：2026-10-01 17:10 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.031（PDF p.31 / 印刷 p.28）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p031_300dpi.png`（pnggray 300dpi）
- 核对：Proposition 3.3 的扩展范围、`K(F(z))=K(z)+1`，边界不等式 (2)、半平面分割及 `K_-`/`K_+` 递推。
- 结果：PASS±（包含关系、方向和上下界与原页一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `\Im F(z)\pm c_4\Re F(z)` 的两个方向、`\mathcal V_-`/`\mathcal V_+` 的定义与像包含式、`\Re F(z)\geq\Re z+(1-c_3)\alpha`，以及 `K_-(z)=K(F^{n(z)}(z))-n(z)`、`K_+(z)=K(F^{-m(z)}(z))+m(z)` 和扩展恒等式；Markdown 对应公式一致。
- 时间：2026-10-01 17:11 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.032（PDF p.32 / 印刷 p.29）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p032_300dpi.png`（pnggray 300dpi）
- 核对：注入性论证、3.4 的奇项系数估计，以及 Lemma 2 的点 `z_1` 存在性和误差界。
- 结果：PASS±（指数、系数、区间和不等号方向一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认畸变式右端为 `2|Dg(0)||z|^3(3-|z|^2)/(1-|z|^2)^2`；Lemma 2 条件含 `\Im z_1\geq\Im z_0-c_3/2`、`F(z_1)+z_1=2z_0`，误差项为 `c_3\min(1,\alpha)e^{-2\pi s}`，其中 `s=\Im z_0-t_0-c_0-c_3/2`；Markdown 逐项一致。
- 时间：2026-10-01 17:13 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.033（PDF p.33 / 印刷 p.30）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p033_300dpi.png`（pnggray 300dpi）
- 核对：Proposition 3.4 的半径/导数估计、插值函数 `g`、`u` 的界及推出的不等式。
- 结果：PASS±（等式结构与不等号一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `r_1\leq(1+c_3)\alpha/2`、`r_0\geq(1+c_3)\alpha`、`|u|=r_1/r_0\leq1/2`，畸变余项中的 `r_1^3r_0^{-2}`，以及 `s=\Im z_0-t_0-c_0-c_3/2`；Markdown 对应式一致。
- 时间：2026-10-01 17:15 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.034（PDF p.34 / 印刷 p.31）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p034_300dpi.png`（pnggray 300dpi）
- 核对：估计 (3)、`c(\alpha)` 定义、两个 `\alpha` 区间的假设与常数 `c_6,c_7,c'_6,c'_7`，Proposition 1 界。
- 结果：PASS±（分段、系数与不等号均一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `\theta=c_3\min(1,\alpha)e^{-2\pi s}+\frac54c_5^2(1+c_3)^3w^{-2}\alpha^3`、`c(\alpha)\leq c_6^2\alpha` 与 `c_6<0.58`、第二段 `c(\alpha)\leq(c'_6)^2\alpha^3`、`c'_6<1.15`，以及 Proposition 1 的分母 `w^2-c_6^2`；Markdown 对应项一致。
- 时间：2026-10-01 17:16 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.035（PDF p.35 / 印刷 p.32）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p035_300dpi.png`（pnggray 300dpi）
- 核对：Proposition 2 的导数界、Remark、§3.5 的 `t_1` 与 `\mathcal W/\mathcal W_1` 定义、估计 (4)–(6)。
- 结果：PASS±（数学公式与原页一致；印刷原文拼写 quirk 保留；页眉/folio 未保留）。
- 源级 quirk：300dpi 原页印刷字样为 `Pout`，MinerU Markdown 忠实保留；不得依据法语语义更正原文。
- 记录更正：2026-10-02 00:19 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。复核 PDF p.35 原页后，撤回先前将 `Pout` 判为 MinerU OCR 差异的记录；印刷与 Markdown 均为 `Pout`，只作为源级 quirk 登记。
- 证据与复核：300dpi 原页确认 `|\alpha DK(z_0)-1|\leq(c'_6)^2\alpha^2/(w^2-(c'_6)^2\alpha^2)`、`t_1=(2\pi)^{-1}\operatorname{Log}\alpha^{-1}+c_7+c_6+c_3`、`\alpha D K(z)` 的 (4) 界和常数 `c_8<2.43`，均与 Markdown 一致；原页与 Markdown 的句首均为 `Pout`。
- 时间：2026-10-01 17:18 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.036（PDF p.36 / 印刷 p.33）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p036_300dpi.png`（pnggray 300dpi）
- 核对：`G(L(z))=L(z-1)` 的定义、交换关系、`G` 的上半平面渐近及单射性推证。
- 结果：PASS±（等式和集合条件吻合；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `G\circ T=T\circ G`、`\lim_{\Im z\to+\infty}(G(z)-z)=-\alpha^{-1}`、单射证明中 `G(z')-G(z)\in\mathbb N` 与 `z'=z+1`，以及 p.33 底部 3.6 命题 `0\leq m<n`；Markdown 对应关系与符号方向一致。
- 时间：2026-10-01 17:19 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.037（PDF p.37 / 印刷 p.34）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p037_300dpi.png`（pnggray 300dpi）
- 核对：3.6 轨道构造中的 `0\leq m\leq p<n`，3.7 主估计、反证假设和变换归一化。
- 结果：PASS±（不等式方向、迭代范围及主估计吻合；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认首返指数 `0\leq m\leq p<n`，并确认 `d_F\leq(2\pi)^{-1}\Phi(\alpha)+2c_8`、反证条件 `\Im F^n(z)\leq0` 与 `\Im z\geq(2\pi)^{-1}\Phi(\alpha)+2c_8`，以及反射 `F(z)\mapsto-\overline{F(-\bar z)}`；Markdown 对应关系一致。
- 时间：2026-10-01 17:21 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.038（PDF p.38 / 印刷 p.35）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p038_300dpi.png`（pnggray 300dpi）
- 核对：主定理证明收尾、构造参数 `A,c_{14},c_9`、截断函数 `\eta` 的端点条件、`J_1` 复共轭与 `\chi` 定义。
- 结果：PASS±（公式、端点不等号和共轭关系与印刷相符；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `\alpha> A`、`A=c_{14}<100`，`\eta(t)=0` 对 `t\leq-1/2`、`\eta(t)=1` 对 `t\geq1/2`、`0\leq D\eta\leq2`，`|\Delta\alpha|\leq c_9=1/100`，`J_1(z)=\overline{J_0(\bar z)}`，以及 `\chi(is)=\eta(s)F_0(is)+(1-\eta(s))J_1(is)`；Markdown 对应式一致。
- 时间：2026-10-01 17:53 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.039（PDF p.39 / 印刷 p.36）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p039_300dpi.png`（pnggray 300dpi）
- 核对：`\mathcal X` 拼接后的 `K_0` 条件、矩形 `R`、分段 `G_0` 定义、`G_1` 共轭与 Möbius 变换 `k`。
- 结果：PASS±（区域界、分段定义和映射公式与原页相符；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `K_0(\chi(is))=K_0(is)`、`\lim_{s\to+\infty}K_0(is)=0`、`K_0(0)=1`，`G_0` 的三个分段区域（`\Re z\geq1`、`0\leq\Re z<1` 且 `\Im z\geq1/2` 或 `\Im z\leq-1/2`），`G_1(K_0(z))=K_0(G_0(z))` 及 `k(z)=tz/(z-1)`；Markdown 一致。
- 时间：2026-10-01 18:52 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.040（PDF p.40 / 印刷 p.37）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p040_300dpi.png`（pnggray 300dpi）
- 核对：`t=c_{15}\alpha^{-1}` 关系，4.3 中 `F_0/J_1` 误差界、`\chi` 渐近式及导数公式。
- 结果：PASS±（指数方向、平移量与导数项吻合；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `F_0(z)-z-\alpha` 与 `DF_0(z)-1` 的指数 `-2\pi(s+1/2)`，`J_1(z)-z-\alpha'` 与 `DJ_1(z)-1` 的指数 `2\pi(s-1/2)`，以及 `d\chi(is)/ds=D\eta(s)(F_0-J_1)+i\eta DF_0+i(1-\eta)DJ_1`；Markdown 对应相同。
- 时间：2026-10-01 19:52 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.041（PDF p.41 / 印刷 p.38）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p041_300dpi.png`；公式裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p041_v_defs_crop_300dpi.png`、`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p041_derivative_crop_300dpi.png`、`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p041_v_equations_crop_300dpi.png`（均源自 pnggray 300dpi）
- 核对：`\chi` 导数界、`v^\pm(s)` 的定义、解析表达式、导数及估计 (1)–(3)。
- 结果：PASS±（Markdown 忠实对应印刷；两处印刷括号 quirk 原样保留）。
- 源级 quirk：印刷的 `v^-(s)` 定义在 `J_1(-ie^s)` 后多一个右括号；导数式末项 `1+D\varphi((1+e^s)i)` 后缺少闭合右括号。原页图确认这两处为印刷本身的括号瑕疵，MinerU Markdown 予以忠实转录，不能按数学预期更正。
- 证据与复核：300dpi 全页及放大裁片确认 `|d\chi(is)/ds-i|<c_2+4c_3+2c_9<0.17`、`\exp v^-(s)+(\alpha+\alpha')/2=J_1(-ie^s))`、(1) 的 `v^\pm-(s+i\pi)\pm i\pi/2`（此处原文确未写 `(s)`）、(2) 的 `v^+(s)-v^-(s)+i\pi` 和 (3) 的导数界；Markdown 与原印刷字形相符。
- 补充证据：2026-10-02 03:48 EDT；Peer-P35 / gpt-6-luna/max。新加入的 `p041_v_equations_crop_300dpi.png` 再次覆盖 `\exp v^\pm` 定义、(1)–(3) 与导数界，没有新增转写差异，等级仍为 PASS±。
- 时间：2026-10-01 19:52 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.042（PDF p.42 / 印刷 p.39）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p042_300dpi.png`（pnggray 300dpi）
- 核对：环域模估计目标、两个 annuli 的内外半径/中心、密度 `\rho`、面积/长度泛函及模下界。
- 结果：PASS±（区域参数与不等号吻合；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `|K_0(z)-1|<C\alpha^{-1}` 与导数版本、外半径 `|\alpha+\alpha'|/4`、`|\alpha-\alpha'|\leq1/100`、两 annuli 的中心、`\rho=1/|z|` 和 `\rho=1/|z-(\alpha+\alpha')/2|`，以及 `M\geq L^2S^{-1}`；Markdown 对应式一致。
- 时间：2026-10-01 21:27 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.043（PDF p.43 / 印刷 p.40）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p043_300dpi.png`（pnggray 300dpi）
- 核对：变量 `\sigma^{\pm}` 及其反函数、矩形 `\widetilde{\mathcal A}_2`、面积上界 `S` 与界 (4)。
- 结果：PASS±（矩形边界、积分范围及不等式方向一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `\widetilde{\mathcal A}_2` 中 `\Im v^-(\sigma^-(\Re v))\geq\Im v\geq\Im v^+(\sigma^+(\Re v))`，`S\leq2\pi\operatorname{Log}|(\alpha+\alpha')/6|+2c_{10}` 及 `\sigma(v)` 的分段定义；Markdown 对应一致。
- 时间：2026-10-01 22:22 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.044（PDF p.44 / 印刷 p.41）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p044_300dpi.png`（pnggray 300dpi）
- 核对：`|dv|` 下界 (5)、路径长度积分、`\sigma_0/\sigma_1`、`L` 下界和模下界 `M`。
- 结果：PASS±（系数、上下限和不等号方向一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 `c_{12}=c_{11}+\frac13c_{10}^2<1/98`、`\int_\gamma\rho|dz|\geq\int_{\sigma_0}^{\sigma_1}(1-c_{12}e^{-\sigma})d\sigma`、`L\geq\operatorname{Log}|(\alpha+\alpha')/6|-2c_{10}-\frac23c_{12}`、`M\geq(2\pi)^{-1}(\operatorname{Log}|(\alpha+\alpha')/6|-c_{13})` 和 `c_{13}=(4+\pi^{-1})c_{10}+\frac43c_{12}<1/28`；Markdown 表达一致。
- 时间：2026-10-01 22:46 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.045（PDF p.45 / 印刷 p.42）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p045_300dpi.png`（pnggray 300dpi）
- 核对：Teichmüller 的环域界、`K_0(R)` 距离上界、常数 `c_{14},c_{15}` 与 4.6 区域定义。
- 结果：PASS±（内容与原页一致；raw Markdown 的部分常数数字间有空格，作为检索候选；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页确认 Teichmüller 常数为 `16`、`|K_0(z)-1|` 的两步上界、`\alpha>c_{14}=\frac12c_9+96e^{c_{13}}`、`c_{15}=96e^{c_{13}}<100`、`t=c_{15}\alpha^{-1}` 和 `t/(1+t)` 界；对应 Markdown 的 `1 6`、`9 6` 数字分隔不改变印刷数值，公式关系一致。
- 时间：2026-10-01 23:24 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.046（PDF p.46 / 印刷 p.43）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p046_300dpi.png`（pnggray 300dpi）；公式 (6) 裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p046_eq6_crop_300dpi.png`；600dpi 放大裁片：`audit/Yoccoz_1995_siegel_bruno_p046_eq6_crop_600dpi.png`。
- 核对：§4.6 的估计 (6)、积分所得 (7)，以及 §4.7 开头的命题 1 条件与两项结论。
- 结果：PASS±（正文、公式及不等式与印刷一致；印刷页眉/folio 未保留）。
- 源级 quirk：PDF p.46 印作 `Pout`，MinerU Markdown 忠实保留；式 (6) 印作 `c_6^2`（无撇号），尽管前一行的界含 `c'_6`。高分辨率原页裁片确认印刷确无撇号，Markdown 也对应保留，均不得按语义或预期推改。
- 证据与复核：300dpi 全页及局部裁片核对 `w\geq2c'_6\alpha`、式 (6) 的 `\frac43c_6^2\alpha^2w^{-2}\leq1/3`、式 (7) 的 `c'_8<4.76`，并核对 4.7 中 `G(K(z))=K(z-1)`、命题 1 的 `0<m<2\alpha n` 与下界；对应 Markdown 第 1831–1875 行内容与字形一致。PDF 文本层对公式字形映射有损，相关判断以页面图像为据。
- 时间：2026-10-02 00:25 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.047（PDF p.47 / 印刷 p.44）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p047_300dpi.png`（pnggray 300dpi）。
- 核对：§4.7 命题 1 的证明、命题 2 的界及证明、§5 开始处的标题与参数范围。
- 结果：PASS±（正文、变量关系、求和界与命题结论相符；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对最小 `p` 的条件、`z'_j` 的定义、`m=\sum_{j=0}^{p-1}n_j\leq p(\alpha+1+c_3)<2n\alpha`、`|E(G^m(z_1))|\geq1`，以及命题 2 的 `\Im z_1\geq(2\pi)^{-1}(\operatorname{Log}\alpha-\operatorname{Log}c_{15})` 和 `0\leq m\leq2\alpha`；对应 Markdown 第 1878–1938 行吻合。PDF 文本层对复杂公式有损，裁定依据为原页图。
- 时间：2026-10-02 00:41 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.048（PDF p.48 / 印刷 p.45）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p048_300dpi.png`（pnggray 300dpi）。
- 核对：§5 开篇、§5.1–5.2 的参数范围、`L` 定义、估计 (1)–(2)、`G(L(z))` 定义及命题陈述。
- 结果：PASS±（数学内容和不等式与印刷相符；一处印刷标点间距与 Markdown 排版不同；页眉/folio 未保留）。
- 差异：印刷将 `précédent,à` 连排，Markdown 写作 `précédent, à`；这是空格/排版差异，不影响语义。
- 证据与复核：300dpi 原页核对 `2<\alpha\leq c_{14}`、`\max_{|s|\leq\alpha}\Im K(s+it'_1)`、关系 (1)–(2) 及 `c''_8=\frac53c'_6+c'_7+\frac23+\frac12c_3<4.03`；命题的 `0<m<2\alpha n` 与 `\Im z_1\geq\alpha^{-1}\Im z_0-c''_8` 也与 Markdown 第 1940–1990 行一致。
- 时间：2026-10-02 00:43 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.049（PDF p.49 / 印刷 p.46）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p049_300dpi.png`（pnggray 300dpi）；第 2 步符号裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p049_step2_crop_300dpi.png`。
- 核对：§5.3 的 `T_{n,\varepsilon}` 定义、`(\alpha_n)` 递推、`F_{n,\ell}` 归纳构造与 §5.4 起始处。
- 结果：PASS±（定义、符号和归纳关系与印刷相符；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 全页及裁片核对 `T_{n,+1}(F)=F+n`、`T_{n,-1}(F)=-\overline{F(-\bar z)}+n`、`\alpha_n=(a_{n+1}+\varepsilon_{n+1}\alpha_{n+1})^{-1}`、第 2 步的 `\widehat S_{\alpha_\ell^{-1}}` 和随后 `G_{n,\ell}\in\widehat S_{-\alpha_\ell}`、`F_{n,\ell}=T_{0,-1}(G_{n,\ell})`；对应 Markdown 第 1992–2026 行一致。公式上下标与符号以原页图像裁定。
- 时间：2026-10-02 00:46 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.050（PDF p.50 / 印刷 p.47）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p050_300dpi.png`（pnggray 300dpi）。
- 核对：§5.4.1 的空集情形、§5.4.2 的 `B_{n,\ell}` 递推及引理陈述、反向归纳第一情形。
- 结果：PASS±（不等式与证明关系吻合；一处法文单词 OCR 差异、常数数字间距伪影及页眉/folio 缺失）。
- 差异：Markdown 第 2066 行写 `tells qu'on ait`，印刷为 `tels qu'on ait`；第 2063 行常数 `34.59` 被拆成 `3 4. 5 9`。前者计划在全篇审计后逐处修正，后者仅作检索/排版伪影记录。
- 证据与复核：300dpi 原页核对 `\Phi(\alpha)\leq4B`、`\sup_{F\in\widehat S_\alpha}d_F\geq(2\pi)^{-1}\Phi(\alpha)-2B/\pi`、`B_{n,\ell}=\alpha_\ell B_{n,\ell+1}+\operatorname{Log}\alpha_\ell^{-1}-B`、引理中的 `c_{16}<34.59`，以及第一归纳情形所得下界；Markdown 第 2028–2082 行数学内容一致。
- 时间：2026-10-02 00:48 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.051（PDF p.51 / 印刷 p.48）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p051_300dpi.png`（pnggray 300dpi）；引理裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p051_lemma_crop_300dpi.png`。
- 核对：5.4.2 反向归纳余下两种情形与结论、§5.4.3 的无限情形及引理四项条件。
- 结果：PASS±（递推估计、指标范围和结论相符；Markdown 一处集合符号字体被拍平，印刷页眉/folio 未保留）。
- 差异：Markdown 第 2120 行写 `n', n \in I`，原页为 `n', n \in \mathcal{I}`；计划在全篇审计后逐处恢复花体记号。
- 证据与复核：300dpi 全页与引理裁片核对第二种情形 `B_{n,\ell+1}\leq2\pi(c'_8\alpha_\ell^{-1}+1)`、第三种情形 `\alpha_\ell\geq c_{14}^{-1}` 的估计、有限情形结论，以及无限情形引理中 `m(n',n',n)<2\alpha_{n'}^{-1}`、`m(\ell,n',n)<2\alpha_\ell^{-1}m(\ell+1,n',n)`、`F_{n,\ell}^m(z)\notin\mathbb H` 和 `0\leq\Re z<1`；对应 Markdown 第 2084–2134 行一致，除上述花体字体差异。
- 时间：2026-10-02 00:51 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.052（PDF p.52 / 印刷 p.49）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p052_300dpi.png`（pnggray 300dpi）。
- 核对：§5.4.3 的收敛子列论证、Bruno/非 Bruno 两种结论、半径估计及 §6.1 开头。
- 结果：PASS±（论证、和式、结论与印刷相符；常数数字间距伪影、一个标点间距差异及页眉/folio 缺失）。
- 差异：Markdown 第 2157 行把 `139.75` 拆成 `1 3 9. 7 5`；原页在 `théorème.On obtient` 之间无空格，而 Markdown 加了常规句间空格。均不改变数学内容。
- 证据与复核：300dpi 原页核对 `B_{n',0}>\sum_{j=0}^{n'}\beta_{j-1}\operatorname{Log}\alpha_j^{-1}-2B`、非 Bruno 时 `d_F=+\infty`、Bruno 时 `d_F\geq(2\pi)^{-1}\Phi(\alpha)-B/\pi`，以及 `\operatorname{Log}R(\alpha)\leq-\Phi(\alpha)+4B+\operatorname{Log}4` 和 `4B+\operatorname{Log}4<139.75`；§6.1 两段说明亦对应 Markdown 第 2136–2166 行。
- 时间：2026-10-02 00:54 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.053（PDF p.53 / 印刷 p.50）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p053_300dpi.png`（pnggray 300dpi）；求和式裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p053_sum_crop_300dpi.png`。
- 核对：§6.2 的区域与 `L/G` 关系、周期点假设、引理下界及证明中 `n_j` 的定义与 `m_s` 求和。
- 结果：PASS±（内容和字形与印刷一致；保留一处源级求和指标 quirk；页眉/folio 未保留）。
- 源级 quirk：印刷本身写作 `m_s=\sum_{r=1}^{s}n_j`，求和指标为 `r` 但被加项下标为 `j`；Markdown 忠实转录。不得仅按预期将 `n_j` 改成 `n_r`。
- 证据与复核：300dpi 原页及求和式裁片核对 `\mathcal{D}` 的边界、`L(F(z))=L(z)+1`、`G(L(z))=L(z-1)`、周期关系 `F^q(z)=z+p`、`G^p(z')=z'-q`、最小虚部界及 `F(z_j)=z_{j+1}+n_{j+1}`；对应 Markdown 第 2170–2222 行与印刷一致，包括原印刷的 `\sum_{r=1}^{s}n_j`。
- 时间：2026-10-02 00:57 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.054（PDF p.54 / 印刷 p.51）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p054_300dpi.png`（pnggray 300dpi）。
- 核对：6.2 引理证明余下的递推定义、6.3 集合 `\mathcal{J}(\alpha)`、`p,q` 构造的两个起始条件及向下归纳开头。
- 结果：PASS±（符号、上下标、递推和参数范围与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `y_0=z_0`、`y_{m_s+1}=F(y_{m_s})-1`、`y_{j+1}=y_j-1`（`j\ne m_s`）、两类 `z'_{j+1}` 递推，并核对 `B_{n,\ell}\geq B\alpha_{\ell-1}^{-1}`、`F_{n,\ell}^{q}(z)=z+p`、`\Im F_{n,\ell}^{j}(z)\geq(2\pi)^{-1}B_{m,\ell}` 与 `\ell=m` 初值；对应 Markdown 第 2225–2276 行一致。
- 时间：2026-10-02 01:00 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.055（PDF p.55 / 印刷 p.52）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p055_300dpi.png`（pnggray 300dpi）。
- 核对：§6.3 向下归纳构造的收尾、轨道周期与虚部下界命题、§6.4 共轭类及导数约束。
- 结果：PASS±（各递推式、区间和估计与印刷一致；印刷页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `G_{n,\ell}^{\tilde p}(z')=z'-q`、`p(m)=p_{k(m)}`、`q(m)=q_{k(m)}`、命题中的 `F^{q_{k(m)}}(z_m)=z_m+p_{k(m)}` 与虚部和式下界，以及 `|\alpha_m'^{-1}-\alpha_m^{-1}|\leq c_9`；对应 Markdown 第 2278–2320 行一致。公式以页面图像核对，PDF 文本层的专用数学字形映射有损。
- 时间：2026-10-02 01:02 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.056（PDF p.56 / 印刷 p.53）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p056_300dpi.png`（pnggray 300dpi）；`\Lambda(f)` 定义裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p056_lambda_crop_300dpi.png`。
- 核对：§6.4 的共轭类定理、`f_\theta` 三项性质、`\Lambda(f)` 参数定义，以及 §6.5 开头的 `\mathcal W`。
- 结果：FAIL（`\Lambda(f)` 定义中的参数关系漏掉逆指数，改变公式含义）。
- 差异：Markdown 第 2348 行写 `\alpha'_m(t)-\alpha_m^{-1}=c_9t`；300dpi 原页明确为 `\alpha'_m(t)^{-1}-\alpha_m^{-1}=c_9t`。全篇审计结束后须依据此原页逐处补回 `^{-1}`。
- 证据与复核：300dpi 全页与定义裁片确认参数方程；同时核对 `\mathcal J=\mathcal J_1\cup\mathcal J_2`、条件 (i)–(iii)、非 Bruno 假设、可数性论证、`F^{q_{k(m)}}(z_m)=z_m+p_{k(m)}`、下界和式，以及 §6.5 的 `\mathcal W` 定义；其余对应 Markdown 第 2320–2359 行。
- 时间：2026-10-02 01:05 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.057（PDF p.57 / 印刷 p.54）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p057_300dpi.png`（pnggray 300dpi）；常数裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p057_constant_crop_300dpi.png`。
- 核对：§6.5 的周期轨道引理与证明、§6.6 命题的假设、结论及常数 `c_{17}`。
- 结果：PASS±（公式和命题结论与印刷相符；`10^{-13}` 数字间距伪影；页眉/folio 未保留）。
- 差异：Markdown 第 2417 行把 `10^{-13}` 拆成 `1 0 ^ {- 1 3}`；印刷值清楚为 `10^{-13}`，不影响该公式的读数。
- 证据与复核：300dpi 原页及常数裁片核对 `G^p(z')=z'-q`、最小虚部估计、`q\geq q_{k(m)}`、`|p|\geq|p_{k(m)}|`、等号判据及 `c_{17}=c_3\exp(-2\pi(2c_8-\frac12))<10^{-13}`；对应 Markdown 第 2362–2420 行内容一致。
- 时间：2026-10-02 01:09 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.058（PDF p.58 / 印刷 p.55）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p058_300dpi.png`（pnggray 300dpi）；归纳步骤裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p058_induction_crop_300dpi.png`。
- 核对：§6.6 命题的归纳证明基例、应用 6.5 后的虚部估计、带帽参数关系与命题结尾。
- 结果：PASS±（归纳估计与参数关系相符；保留一处源级拼写 quirk；页眉/folio 未保留）。
- 源级 quirk：印刷和 Markdown 都写作 `Suppposons`（多一个 `p`）；这是原文拼写，忠实保留。
- 证据与复核：300dpi 全页及裁片核对 `q_{k(0)}=1`、`|p_{k(0)}-\alpha|=\alpha_0<1/2`、变换后 `G^p(z')=z'-q`、两级虚部下界、`\hat\alpha_\ell=\alpha_{\ell+1}`、`\hat\beta_\ell=\alpha^{-1}\beta_{\ell+1}` 及 `\hat p_{k(m-1)}=-q_{k(m)}`、`\hat q_{k(m-1)}=p_{k(m)}`；对应 Markdown 第 2422–2446 行一致。
- 时间：2026-10-02 01:12 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.059（PDF p.59 / 空白页）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p059_300dpi.png`（pnggray 300dpi）。
- 核对：空白页及其对应 MinerU 页块。
- 结果：FAIL（Markdown 含不属于论文的整段英文生成文本）。
- 差异：Markdown 第 2448 行含一段 564 字符英文指令式说明；300dpi PDF 原页为空白，`pdftotext` 第 59 页仅输出分页符，`structured_content.json` 的 `page_idx=58` 却包含一个同文 `text` block。该段是 MinerU 衍生文本的错误插入，不应当作论文内容或执行指令；待全篇审计后从 Markdown 逐处删除。
- 证据与复核：300dpi 空白页图、PDF 页文本输出长度 1 byte（仅 form-feed）及 `structured_content.json` page_idx/block 结构共同证明该差异；审计按 PDF p.59 与 Markdown 第 2448 行对齐。
- 时间：2026-10-02 01:16 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.060（PDF p.60 / 印刷 p.57）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p060_300dpi.png`（pnggray 300dpi）。
- 核对：第二章标题、§1.1 的 `P_\lambda`、§1.2 的形式共轭方程及 `K_\lambda` 展开起始式。
- 结果：PASS±（正文、变量和公式与印刷一致；页眉/folio 未保留）。
- 源级 quirk：印刷和 Markdown 均写作 `Ecrivons`（无首字母重音）；照原文保留。
- 证据与复核：300dpi 原页核对 `P_\lambda(z)=\lambda(z-z^2)`、`H_\lambda(\lambda z)=P_\lambda(H_\lambda(z))`、`H_\lambda(z)=zK_\lambda(z)=z\sum_{n\geq0}H_n(\lambda)z^n` 与 `H_0(\lambda)=1`，以及最后的 `\lambda zK_\lambda(\lambda z)=\lambda zK_\lambda(z)-\lambda z^2K_\lambda^2(z)`；对应 Markdown 第 2450–2481 行一致。
- 时间：2026-10-02 01:19 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.061（PDF p.61 / 印刷 p.58）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p061_300dpi.png`（pnggray 300dpi）。
- 核对：递推式 `H_n(\lambda)`、§1.3.1 的整函数类型证明和临界点描述、§1.3.2 命题陈述。
- 结果：PASS±（递推、增长界与命题条件相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `H_n(\lambda)=(1-\lambda^n)^{-1}\sum_{i+j=n-1}H_i(\lambda)H_j(\lambda)`、`\gamma=\operatorname{Log}2/\operatorname{Log}|\lambda|`、`m_n=2|\lambda|^{2^n-1}`、`M_n=2(3|\lambda|)^{2^n-1}`、临界点 `\lambda^n z_0` 及 `H_\lambda(z_0)=1/2`，并核对 `|\lambda|<1` 时 `R_2(\lambda)` 与唯一边界奇点 `U(\lambda)` 的命题；对应 Markdown 第 2484–2520 行一致。
- 时间：2026-10-02 01:21 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.062（PDF p.62 / 印刷 p.59）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p062_300dpi.png`（pnggray 300dpi）。
- 核对：§1.3.2 证明、Riemann 曲面分歧描述、§1.3.3 单位模情形、§1.4 初始扰动定义与引理。
- 结果：PASS±（命题、方程和指数关系与印刷相符；保留一处源级重音拼写；页眉/folio 未保留）。
- 源级 quirk：印刷与 Markdown 均写作 `Ecrivons`，未在首字母 `E` 上标重音；照原文保留。
- 证据与复核：300dpi 原页核对 `H_\lambda(\lambda U(\lambda))=\lambda/4`、上覆点 `\lambda^{-n}U(\lambda)` 的 `2^n` 个二阶分歧点、`|\lambda|=1` 的陈述、`f_b(z)=f(z)+bz^2`、`H_b(z)=z(1+\sum_{n\geq1}H_n^*(b)z^n)`，以及 `H_n^*(b)` 的次数与最高次项；对应 Markdown 第 2522–2550 行一致。
- 时间：2026-10-02 01:25 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.063（PDF p.63 / 印刷 p.60）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p063_300dpi.png`（pnggray 300dpi）。
- 核对：§1.4 中多项式型映射的边界估计、Rouché 引理应用、`\Gamma` 和 `\eta` 的定义，以及 `\tilde f_{a,b}` 公式。
- 结果：PASS±（开集、界和公式均与印刷一致；一处分数数字间距伪影及页眉/folio 缺失）。
- 差异：Markdown 第 2571 行将 `10/9`、`13/36` 的数字拆开排写；300dpi 原页数值清楚为 `10/9=13/36+3/4`，关系本身一致。
- 证据与复核：300dpi 原页核对 `\mathcal W=\{|z|<13/36\}`、`\mathcal W_b=\{|z|\leq1/3, f_b(z)\in\mathcal W\}`、`|f(z)|\leq3/4`、`|bz^2|\geq10/9=13/36+3/4`、Rouché 后的 proper degree 2、`\eta` 的两个端区间及 `\tilde f_{a,b}` 拼接公式；对应 Markdown 第 2560–2594 行内容一致。
- 时间：2026-10-02 01:28 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.064（PDF p.64 / 印刷 p.61）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p064_300dpi.png`（pnggray 300dpi）。
- 核对：1.5 末尾的导数界、Beltrami 拉回公式、`\mu` 支撑与范数界、规范化准共形映射和共轭多项式引理。
- 结果：PASS±（公式、作用域与归一化条件与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `|\partial_{\bar z}\tilde f_{a,b}|\leq k(a)|\partial_z\tilde f_{a,b}|`、`f^*\mu` 的分式、`\operatorname{supp}\mu\subset\mathcal W`、`\|\mu_{f,a,b}\|_{L^\infty}\leq k(a)`、`\partial_{\bar z}\phi=\mu\partial_z\phi`、`\phi(0)=0`、`\phi(z)-z` 有界及 `\phi\circ\tilde f_{a,b}\circ\phi^{-1}(z)=\lambda z+bz^2`；对应 Markdown 第 2596–2638 行一致。
- 时间：2026-10-02 01:31 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.065（PDF p.65 / 印刷 p.62）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p065_300dpi.png`（pnggray 300dpi）；1.8 引理裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p065_lemma_crop_300dpi.png`。
- 核对：§1.6 证明 `\lambda=\lambda'`、§1.7 Hölder 界、§1.8 Siegel 圆盘引理与线性化系数界。
- 结果：PASS±（方程、常数和幂次与印刷相符；页眉/folio 未保留）。
- 记号复核：印刷的 1.8 引理第 1 项写 `f_{a,b}`（无波浪号），Markdown 一致；此处未按邻近的 `\tilde f_{a,b}` 定义推改。
- 证据与复核：300dpi 全页及引理裁片核对 `\phi_t\circ\tilde f_t\circ\phi_t^{-1}(z)=\lambda'z+bTz^2`、`K(a)=(1+k(a))/(1-k(a))`、Hölder 指数 `1/K(a)`、`D'_{\lambda}` 中的半径 `[R_2(\lambda)/(40C(a))]^{K(a)}`、`D'_{\lambda}\subset\mathcal W_b`，以及 `|H_n^*(a,b)|\leq\frac13R_a^{-n-1}`；对应 Markdown 第 2638–2672 行一致。
- 时间：2026-10-02 01:35 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.066（PDF p.66 / 印刷 p.63）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p066_300dpi.png`（pnggray 300dpi）。
- 核对：1.8 估计推导、线性化主定理两项、1.9 对最优收敛半径的讨论与开放问题。
- 结果：PASS±（不等式、量词和参数集合与印刷一致；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `R(f)\geq aR_a`、`\alpha\notin\mathcal B` 时 `P_\lambda` 不可线性化、Bruno 情形下 `(1-\varepsilon)\Phi(\alpha)-C(\varepsilon)\leq-\operatorname{Log}R_2(\lambda)\leq\Phi(\alpha)+C_1`，以及关于 `\Phi(\alpha)+\operatorname{Log}R_2(\lambda)` 有界性的提问；对应 Markdown 第 2674–2692 行一致。
- 时间：2026-10-02 01:38 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.067（PDF p.67 / 印刷 p.64）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p067_300dpi.png`（pnggray 300dpi）。
- 核对：§2.1 函数 `U` 的定义、`U_n` 递推与有界性、紧集上一致收敛及极限识别。
- 结果：PASS±（递推、初值、界和极限公式与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `U_n(\lambda)=\lambda^{-n}P_\lambda^n(1/2)`、`U_{n+1}=U_n-\lambda^nU_n^2`、`U_0=1/2`、`|P_\lambda(z)|\geq|z|(|z|-1)`、`|U_n(\lambda)|\leq2` 及 `\lambda^{-n}H_\lambda(\lambda^nU(\lambda))\to U(\lambda)`；对应 Markdown 第 2694–2732 行一致。
- 时间：2026-10-02 01:41 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.068（PDF p.68 / 印刷 p.65）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p068_300dpi.png`（pnggray 300dpi）。
- 核对：§2.2 的 `R_2` 界和 `U` 的级数、§2.3 的 Fatou 边界结论与命题、§2.4 的边界极限定理及根单位备注。
- 结果：PASS±（估计、幂级数系数及极限结论与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `R_2(\lambda)=|U(\lambda)|\leq2`、`R_2(\lambda)\leq1`、Herman 界 `|U(\lambda)|\leq4/7`、`U(\lambda)=1/4-\lambda/16-\lambda^2/16-\lambda^3/32+\cdots`，以及非根单位点的 `R_2(\lambda_0)\geq\limsup|U(\lambda)|`、边界模的非切向极限等于 `R_2(\lambda_0)` 和根单位时 `R_2(\lambda_0)=0`；对应 Markdown 第 2734–2764 行一致。
- 时间：2026-10-02 01:44 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.069（PDF p.69 / 印刷 p.66）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p069_300dpi.png`（pnggray 300dpi）；递推指标裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p069_recurrence_crop_300dpi.png`。
- 核对：§2.4 容量比较与两个命题、§2.5 命题 1 的起始构造和导数递推。
- 结果：PASS±（内容吻合；原文递推的指标范围 quirk 保留；页眉/folio 未保留）。
- 源级 quirk：印刷与 Markdown 均将 `y_n(t)=P_\lambda^n(y_0)=P_\lambda(y_{n-1}(t))` 标为 `n\geq0`；代入 `n=0` 时末项出现 `y_{-1}`，但这是原文明确的指标范围，不按推测改写。文本层抽取成 `n>0`，裁片确认印刷符号为 `\geq`。
- 证据与复核：300dpi 全页及裁片核对 `R_2(\lambda)=|U(\lambda)|=C(\mathcal V_\lambda)\leq C(\mathcal U_\lambda)`、两项容量命题、`\lambda=(1-t)\lambda_0`、`y_n/x_n` 定义、`x_n(0)=\lambda_0^n x_0` 和 `Dy_n(0)=-y_n(0)+DP_{\lambda_0}(y_{n-1}(0))Dy_{n-1}(0)`；对应 Markdown 第 2766–2813 行内容一致。
- 时间：2026-10-02 01:48 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.070（PDF p.70 / 印刷 p.67）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p070_300dpi.png`（pnggray 300dpi）。
- 核对：§2.5 命题 1 的导数公式、Birkhoff 和界、紧集上一致控制及前向不变域结论。
- 结果：PASS±（递推、求和界和半径关系与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `Dx_n(0)=-\lambda_0^n x_0\sum_{i=1}^{n}k(\lambda_0^ix_0)`、`k(z)=H_{\lambda_0}(z)/(zDH_{\lambda_0}(z))`、Birkhoff 和的均匀收敛、`|x_N(t)/x_N(0)-1+tN|` 界，以及域 `H_{\lambda_0}(\{|z|\leq(1-\varepsilon)R_2\})` 在 `P_\lambda^N` 下不变并落入吸引盆的结论；对应 Markdown 第 2816–2866 行一致。
- 时间：2026-10-02 01:52 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.071（PDF p.71 / 印刷 p.68）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p071_300dpi.png`（pnggray 300dpi）。
- 核对：§2.6 的 Blaschke 共轭 `Q_\lambda`、线性化与容量关系、商式估计，以及 `\widetilde R_\lambda` 不趋于零的引理陈述。
- 结果：PASS±（归一化、商式不等式和引理与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `Q_\lambda(z)=e^{2\pi i\alpha}z\frac{|\lambda|-z}{1-|\lambda|z}`、`\widetilde H_\lambda=K_\lambda^{-1}H_\lambda(DK_\lambda(0)z)`、`\widetilde R_\lambda=C(\widetilde{\mathcal V}_\lambda,0)=C(\mathcal V_\lambda,0)[C(\mathcal U_\lambda,0)]^{-1}`、上/下商式界和 `|\lambda|^b\leq|Q_\lambda(z)/z|\leq|\lambda|^a`；对应 Markdown 第 2868–2916 行一致。
- 时间：2026-10-02 01:56 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.072（PDF p.72 / 印刷 p.69）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p072_300dpi.png`（pnggray 300dpi）；`\theta` 项 300dpi 裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p072_theta_crop_300dpi.png`、`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p072_theta_term_crop_300dpi.png`；600dpi 裁片：`audit/Yoccoz_1995_siegel_bruno_pdf_p072_theta_crop_600dpi.png`。
- 核对：§2.6 引理不趋于零的证明、极限函数与均匀收敛论证、最后的矛盾及 Proposition 2 结尾。
- 结果：PASS±（证明不等式与印刷相符；保留一处源级参数记号 quirk；页眉/folio 未保留）。
- 源级 quirk：选择整数 `N` 处原印刷写作 `\theta < \lambda_n^{2Nb} < \theta'`，未在 `\lambda_n` 周围写模长符号；Markdown 忠实转录。300dpi 与 600dpi 原页裁片均确认无模长竖线，未按推测增补。
- 证据与复核：300dpi 全页及裁片核对第一个引理中的迭代模下界、`H(\lambda_0 z)=\lambda_0H(z)`、`\theta=R/r` 与 `\theta'=(1+\theta)/2`、迭代轨道下界以及由收敛到恒等映射导出的矛盾；对应 Markdown 第 2918–2952 行内容和符号一致。
- 时间：2026-10-02 02:04 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.073（PDF p.73 / 印刷 p.70）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p073_300dpi.png`（pnggray 300dpi）。
- 核对：§3.1 中 `U_n` 递推、`A(s,k)` 定义、差分式 (2)、递归式 (3) 与展开式 (4)。
- 结果：PASS±（求和范围、二项式指标及指数与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `U_0=1/2`、`U_{n+1}=U_n-\lambda^nU_n^2`、`A(s,k)=\sum_{n\geq1}U_n^{-s}\lambda^{kn}`、`\binom{s+k-1}{k}`、式 (3) 的 `A(s-k_1+k,k_1)` 递归项，以及式 (4) 中 `k=k_0<k_1<\cdots<k_\ell` 和乘积项；对应 Markdown 第 2954–2990 行一致。
- 时间：2026-10-02 02:09 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.074（PDF p.74 / 印刷 p.71）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p074_300dpi.png`（pnggray 300dpi）。
- 核对：式 (5) 对 `(4U)^{-s}` 的展开、`-Log 4U` 的乘积/双和/式 (6)，以及两个二项式不消失条件。
- 结果：PASS±（幂次、求和范围和二项式指标与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `U^{-s}=4^s+\sum_{k\geq1}A(s-k,k)\binom{s+k-1}{k}`、式 (5) 中 `0=k_0<k_1<\cdots<k_\ell`、`4U=\prod_{n\geq1}(1-\lambda^nU_n)`、式 (6) 的两个乘积范围，以及备注中的 `k_i\leq2k_{i-1}-s` 或 `k_{i-1}\leq s-1` 条件；对应 Markdown 第 2992–3026 行一致。
- 时间：2026-10-02 02:13 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.075（PDF p.75 / 印刷 p.72）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p075_300dpi.png`（pnggray 300dpi）。
- 核对：§3.2 的非切向极限问题、单位圆边界问题与 `BMO(S^1)` 定义。
- 结果：PASS±（问题陈述、集合条件与平均振荡定义相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 Question 1–3 对 `U` 的边界值、Question 4 对 `\operatorname{Log}|U\circ E|+\Phi\in L^\infty(\mathbb T^1)`、Question 5–7，以及 `\sup_I |I|^{-1}\int_I|\varphi-\varphi_I|dt<+\infty`；对应 Markdown 第 3028–3070 行内容一致。
- 时间：2026-10-02 02:16 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.076（PDF p.76 / 印刷 p.73）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p076_300dpi.png`（pnggray 300dpi）。
- 核对：§3.3.1 的 `H_n` 与高斯多项式递推、`P_n` 的正系数和次数、§3.3.2 在单位根处的高斯多项式取值公式。
- 结果：PASS±（递推、次数、条件和组合系数与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `H_n(\lambda)=(1-\lambda^n)^{-1}\sum_{i+j=n-1}H_iH_j`、`\Pi_{i,j}(X)` 的乘积定义、`P_n=\sum_{i+j=n-1}\Pi_{i,j}P_iP_j`、`\deg P_n=n(n+1)/2-\delta_n` 及 `\delta_n` 分段式，并核对 `\Pi_{i,j}(\zeta)=0` 的 floor 条件和 `\binom{m+n}{m}\Pi_{r,s}(\zeta)` 公式；对应 Markdown 第 3072–3124 行一致。
- 时间：2026-10-02 02:19 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.077（PDF p.77 / 印刷 p.74）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p077_300dpi.png`（pnggray 300dpi）。
- 核对：§3.3.2 在单位根处的 `B_k` 生成函数、递推和 Gamma 公式；§3.3.3 中 `h_\lambda` 的函数方程及系数极限命题开头。
- 结果：PASS±（指标、阶数和 Gamma 参数与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `B_k(z)=\sum_{m\geq0}b_k(m)z^m/m!`、`B_k=P_k(\zeta)B_0^{k+1}`、`DB_0=P_q(\zeta)B_0^{q+1}`、`P_{mq+r}(\zeta)` 的 Gamma 商、`h_\lambda(z)=H_\lambda(U(\lambda)z)`、函数方程及 `n^{3/2}h_n(\lambda)` 极限；对应 Markdown 第 3126–3185 行一致。
- 时间：2026-10-02 02:22 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.078（PDF p.78 / 印刷 p.75）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p078_300dpi.png`（pnggray 300dpi）。
- 核对：§3.3.3 的平方根展开、`h_n(\lambda)` 渐近式和导数乘积，至 §3.4 的开头。
- 结果：PASS±（渐近系数、Gamma 参数、乘积项和范围与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `\varphi(1)=4Dh_\lambda(\lambda)`、`a=2(Dh_\lambda(\lambda))^{1/2}`、`2h_n(\lambda)` 的 Gamma 渐近式、Remark 1 的一般展开、`Dh_\lambda(\lambda)=\frac14\prod_{n\geq1}\frac{1-\lambda^nU_n(\lambda)}{1-2\lambda^nU_n(\lambda)}`，以及 `P_q(\zeta)\neq0` 所在段落起点；对应 Markdown 第 3182–3248 行一致。
- 时间：2026-10-02 02:24 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.079（PDF p.79 / 印刷 p.76）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p079_300dpi.png`（pnggray 300dpi）；极限命题裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p079_prop_crop_300dpi.png`。
- 核对：§3.4 的 `P_q(\zeta)\neq0`、乘积极限、`Q_\lambda` 重标度与估计、极限命题及 `K_\lambda` 定义。
- 结果：PASS±（阶数、集合范围及极限表达与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 全页及命题裁片核对 Lemma 2 的两种剩余类情形、`P_\lambda^q` 的迭代展开、`Q_\lambda(z)` 的缩放、Lemma 3 两侧模估计，以及 `\lim_{\lambda\to\zeta,\lambda\in V}[U(\lambda)]^q/(1-\lambda^q)=P_q(\zeta)^{-1}`；原页分子为方括号 `[U(\lambda)]^q`，表示普通 q 次幂，Markdown 一致。对应 Markdown 第 3250–3304 行内容相符。
- 时间：2026-10-02 02:28 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.080（PDF p.80 / 印刷 p.77）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p080_300dpi.png`（pnggray 300dpi）。
- 核对：§3.4 证明中 `K_\lambda` 系数、根单位极限、候选极限函数、半径 limsup 界与 `\rho_n` 子列设置。
- 结果：PASS±（幂次、Gamma 商和极限关系与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `K_\lambda` 的 `z^{n+1}` 系数、`n=kq` 时的 `\Gamma(k+1/q)/(k!\Gamma(1/q))(P_q(\zeta))^k`、`K(z)=z(1-P_q(\zeta)z^q)^{-1/q}`、`\limsup |U(\lambda)||1-\lambda^q|^{-1/q}\leq|P_q(\zeta)|^{-1/q}`，以及 `\rho_n=U(\lambda_n)(1-\lambda_n^q)^{-1/q}` 的归一化；对应 Markdown 第 3306–3346 行一致。
- 时间：2026-10-02 02:31 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.081（PDF p.81 / 印刷 p.78）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p081_300dpi.png`（pnggray 300dpi）；迭代界裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p081_iterate_bound_crop_300dpi.png`、`audit/Yoccoz_1995_siegel_bruno_pdf_p081_iterate_bound_crop_600dpi.png`。
- 核对：§3.4 反证论证中最小模点的选择、迭代后 `K_{\lambda_n}` 下界及最终矛盾。
- 结果：PASS±（推演中的条件、模界和结论与印刷相符；保留一处源级指标 quirk；页眉/folio 未保留）。
- 源级 quirk：Markdown 与印刷第 3370 行均写作 `|\rho_n\mu_n^{k}-\rho|\leq\theta`，而前面为定义 `\mu_n` 使用 `\rho_n\mu_n^{q}`。原页清楚印成指数 `k`，故保留，不按证明预期改成 `q`。
- 证据与复核：300dpi 全页、300dpi 与 600dpi 裁片确认条件 (iii)、`\mu_n` 的最小模选择、`|K_{\lambda_n}(\rho_n\mu_n^q\lambda_n^{kq})|\geq|\lambda_n|^{bkq}B`、后续 `3B/4=3A/2` 矛盾及结尾条件；对应 Markdown 第 3348–3376 行一致。
- 时间：2026-10-02 02:36 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.082（PDF p.82 / 印刷 p.79）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p082_300dpi.png`（pnggray 300dpi）。
- 核对：附录 1.1–1.2 的算子 `A_{\lambda,t}`、齐次项展开、对称幂矩阵及系数向量关系。
- 结果：PASS±（定义域、求和指标和矩阵元素与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `A_{\lambda,t}g=g(\lambda(z_1+tz_2),\lambda z_2)-\lambda g`、`g^{(n)}` 的分量次序、复合式中的 `t^{j-k}\binom{j}{k}`、`M_{ij}^{(n)}=0`（`j<i`）与 `\binom{j}{i}t^{j-i}`（`i\leq j`），以及 `w^{(n)}=(\lambda^nM^{(n)}-\lambda)g^{(n)}`；对应 Markdown 第 3378–3427 行一致。
- 时间：2026-10-02 02:39 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.083（PDF p.83 / 印刷 p.80）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p083_300dpi.png`（pnggray 300dpi）。
- 核对：附录 1.3–1.4 的矩阵逆展开、矩阵幂、系数 `A_{k,m}`、多项式 `Q_k` 及插值恒等式证明。
- 结果：PASS±（矩阵指标、二项式系数与求和范围和印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对根单位情形 `q\mid n-1` 的非可逆性、`P^{(n)}=c_n^{-1}\sum_{k=0}^{n}(-b_n)^k\sum_{r=0}^{k}(-1)^{k-r}\binom{k}{r}(M^{(n)})^r`、`(M^{(n)})^r_{ij}=\binom{j}{i}(rt)^{j-i}`（`j\geq i`）、`P^{(n)}_{ij}` 的 `A_{k,j-i}` 形式，以及 `X^m=\sum_{k=0}^{m}A_{k,m}Q_k`；对应 Markdown 第 3430–3463 行一致。
- 时间：2026-10-02 02:42 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.084（PDF p.84 / 印刷 p.81）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p084_300dpi.png`（pnggray 300dpi）；§1.6 下界与下标裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p084_section16_crop_300dpi.png`。
- 核对：`A_{k,m}` 递推与上界、`P_{0m}^{(n)}` 的下界估计，以及 §1.6 的 `n_r,m_r,w` 定义。
- 结果：PASS±（系数估计与边界指标相符；文本层将一处 `\geq` 映射为 `>`，印刷图像已裁定）。
- 证据与复核：300dpi 原页核对 `A_{m,m}=m!`、`A_{m-1,m}=m!(m-1)/2`、`0\leq A_{k,m}\leq\frac{m-1}{2}A_{k+1,m}`、`|P_{0m}^{(n)}|\geq\frac13 t^m m!((n-1)/(2\pi))^{m+1}`，并确认 §1.6 印刷和 Markdown 均为 `r\geq0`（`pdftotext` 派生文本显示为 `r>0`）；对应 Markdown 第 3466–3520 行一致。
- 时间：2026-10-02 02:46 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.085（PDF p.85 / 印刷 p.82）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p085_300dpi.png`（pnggray 300dpi）；引文标签 600dpi 裁片：`audit/Yoccoz_1995_siegel_bruno_pdf_p085_reference_key_crop_600dpi.png`。
- 核对：附录 1.6 的非可解方程级数结论、矩阵值 proposition 及线性化障碍论证。
- 结果：PASS±（幂指标、矩阵和非线性化结论与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `g(0,z_2)=\sum_{r\geq0}P_{0,m_r}^{(n_r)}z_2^{n_r}`、矩阵 `A=\begin{pmatrix}\lambda&\lambda\\0&\lambda\end{pmatrix}`、算子 `B(g)=g\circ A-A\circ g`、其第二分量为 `A_{\lambda,1}(g_2)`，以及不在线性化像中的 `w` 导致 `F_t=A+tw` 对几乎处处 `t\in\mathbb C` 不可线性化；对应 Markdown 第 3522–3542 行一致。
- 后续引文核对：2026-10-02 04:01 EDT；actor=Peer-P35；model=gpt-6-luna/max。600dpi 原页裁片显示该处标记为 `[Il]`，Markdown 第 3542 行写作 `[II]`；`pdftotext` 派生文本也读成 `[II]`，但同页裁片与 p.12 引文裁片均支持小写 `l`。待全篇修复时逐处改为 `[Il]`。
- 时间：2026-10-02 02:48 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.086（PDF p.86 / 印刷 p.83）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p086_300dpi.png`（pnggray 300dpi）。
- 核对：附录 2 的 `H_n/h_n` 递推、Bruno 与非 Bruno 状态、收敛分母集合 `A` 及其外部项和界。
- 结果：PASS±（递推、定义和不等式与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `H_0=1` 与 `H_n=(1-\lambda^n)^{-1}\sum_{i+j=n-1}H_iH_j`、`h_n` 的绝对值主项递推、`|H_n|\leq h_n`、集合 `A=\{q_n:q_{n+1}\geq(q_n+1)^2\}`，以及 `\sum_{q_n\notin A}q_n^{-1}\operatorname{Log}\sigma(q_n)<+\infty`；对应 Markdown 第 3544–3582 行一致。
- 时间：2026-10-02 02:51 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.087（PDF p.87 / 印刷 p.84）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p087_300dpi.png`（pnggray 300dpi）。
- 核对：附录 2 中集合 `A` 的发散和、`n_r` 定义、`h_n` 单调性及递推下界、`\alpha_r` 乘积控制。
- 结果：PASS±（指标、范围和乘积不等式与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `\sum q_n'^{-1}\operatorname{Log}\sigma(q_n')=+\infty`、`n_r=\lfloor q'_{r+1}/(q'_r+1)\rfloor`、`h_{q'_{r+1}}\geq\sigma(q'_{r+1})h_{q'_r}^{n_r}`、`1\geq\alpha_r\geq(1-1/(q'_r+1))^2` 与 `\prod\alpha_r` 收敛后得到的对数递推；对应 Markdown 第 3584–3636 行一致。
- 时间：2026-10-02 02:54 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.088（PDF p.88 / 印刷 p.85）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p088_300dpi.png`（pnggray 300dpi）。
- 核对：附录 2 递推所得对数下界、乘积 `\prod\alpha_r` 控制及 `\limsup` 发散结论。
- 结果：PASS±（求和指标、乘积与极限结论均与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页核对 `q_{r+1}'^{-1}\operatorname{Log}h_{q_{r+1}'}\geq q_{r+1}'^{-1}\operatorname{Log}\sigma(q_{r+1}')+\alpha_r q_r'^{-1}\operatorname{Log}h_{q_r'}`、对部分和的 `\prod_{r\geq0}\alpha_r` 下界，以及 `\limsup_{n\to+\infty}n^{-1}\operatorname{Log}h_n=+\infty`；对应 Markdown 第 3635–3642 行一致。
- 时间：2026-10-02 02:57 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.089（PDF p.89 / 空白页）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p089_300dpi.png`（pnggray 300dpi）。
- 核对：空白页与相邻参考文献起始位置的 MinerU 页映射。
- 结果：FAIL（Markdown 含不属于论文的整段英文生成文本）。
- 差异：Markdown 第 3644 行含 564 字符英文说明；PDF p.89 原页为空白，`pdftotext` 第 89 页仅输出分页符，`structured_content.json` 的 `page_idx=88` 有一个同文 `text` block。该块是 MinerU 衍生文本的错误插入，不属于论文，且不作为指令；待全篇审计后逐处删除该行。
- 证据与复核：300dpi 空白页图、单个分页符的 PDF 文本输出与 MinerU page_idx/block 结构相互印证；记录位置为 PDF p.89 与 Markdown 第 3644 行。
- 时间：2026-10-02 03:00 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

### p.090（PDF p.90 / 印刷 p.87）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p090_300dpi.png`（pnggray 300dpi）；Il'yashenko 条目标记局部图：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p090_il_label_crop_300dpi.png`、`audit/Yoccoz_1995_siegel_bruno_p090_ref_Il_crop_600dpi.png`。
- 核对：参考文献 `[Ah]` 至 `[PM1]` 的作者、题名、出版信息、卷页、年份与条目标签。
- 结果：PASS±（其余书目条目与印刷相符；Il'yashenko 条目标签存在一处确定的 MinerU 转写差异）。
- 差异：PDF p.90 的书目标签为 `[Il]`，Markdown 第 3664 行为 `[II]`；600dpi 裁片与 p.12、p.85 的标签裁片并置后显示为大写 `I` 加小写 `l`。全篇审计结束后逐处改正书目标签。
- 证据与复核：300dpi 全页逐项核对 `[Ah]` Ahlfors 至 `[PM1]` Pérez-Marco，正文内容一致；600dpi 字形对照裁片确认 p.12、p.85 正文及 p.90 书目均印为 `[Il]`。文本层在 p.12/p.85 将小写 `l` 映射为大写 `I`，故以原页图像裁定。
- 时间：2026-10-02 03:33 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。
- 后续复核时间：2026-10-02 04:01 EDT；actor=Peer-P35；model=gpt-6-luna/max。

### p.091（PDF p.91 / 印刷 p.88）
- PNG：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p091_300dpi.png`（pnggray 300dpi）；末页书目裁片：`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p091_biblio_crop_300dpi.png`。
- 核对：最后三条参考文献 `[Po]`、`[Si]`、`[Vo]` 的作者、题名和出版项。
- 结果：PASS±（书目信息与印刷相符；页眉/folio 未保留）。
- 证据与复核：300dpi 原页与书目裁片确认 Poincaré《Oeuvres》卷号/出版者/年份、Siegel 论文刊名/卷页/年份，以及 Voronin 题名中的 `(\mathbb C,0)\to(\mathbb C,0)` 箭头和期刊信息；对应 Markdown 第 3672–3676 行一致。PDF 文本层未保留 Voronin 题名中的映射箭头，页面图像与 Markdown 均显示该箭头。
- 时间：2026-10-02 03:40 EDT；actor=Peer-P35；model=gpt-6-luna；effort=max。

## 修复登记

### 2026-10-02 · 审计后逐处修复

- 原始 MinerU Markdown：SHA-256 `d759402aa8951c595188350424cd206df0bc40c3d088b26247bc754873856de2`；原始文件提交 `e2ecf051043c2683576c8c19c6cdf66d7e05c6af`。
- 本登记写入前的 AUDIT 文件：SHA-256 `5034d1402262a9fe7126ad52f3bd21a35a55c257e360fd1e8c49f035b11a6fc8`。
- 修复后 MinerU Markdown：SHA-256 `08a2579371bdbe74d13b7489cfcab5906081207f04a1f44e0c3ef728f25dded5`。
- 独立正文修复提交：`0d9b384103757cdf6f9f2e78f5c92cb76e1bd9ff` (`fix(md): Yoccoz 按审计修复10处（原始 md 见 e2ecf051） [Peer-P35 | gpt-6-luna/max]`)。

| PDF 页 | 逐处修复 | 原页证据 |
|---|---|---|
| 12 | `démontrer (ou d'infirmier)` → `démontrer (ou d’infirmer)`。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p012_300dpi.png` |
| 19 | `B_{k_\ell,k_\ell-1+1}` → `B_{k_\ell,k_{\ell-1}+1}`。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p019_index_crop_300dpi.png` |
| 26 | 修正 Figure 1 图片相对路径，使其指向现存 MinerU 导出图片。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p026_300dpi.png`；目标图片 `Yoccoz_1995_siegel_bruno_mineru/Yoccoz_1995_siegel_bruno/images/page_25_image_7.jpg` |
| 50 | `tells qu'on ait` → `tels qu'on ait`。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p050_300dpi.png` |
| 51 | `n', n \in I` → `n', n \in \mathcal{I}`。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p051_300dpi.png`、`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p051_lemma_crop_300dpi.png` |
| 56 | 在 `\alpha'_m(t)` 上补回逆指数：`\alpha'_m(t)^{-1} - \alpha_m^{-1} = c_9t`。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p056_300dpi.png`、`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p056_lambda_crop_300dpi.png` |
| 59 | 删除空白 PDF 页对应 MinerU Markdown 中 564 字符英文生成文本。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p059_300dpi.png` |
| 85 | 正文引文标签 `[II]` → `[Il]`（末字母为小写 `l`）。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p085_300dpi.png`、`audit/Yoccoz_1995_siegel_bruno_pdf_p085_reference_key_crop_600dpi.png` |
| 89 | 删除空白 PDF 页对应 MinerU Markdown 中 564 字符英文生成文本。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p089_300dpi.png` |
| 90 | 参考文献标签 `[II]` → `[Il]`（末字母为小写 `l`）。 | `audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p090_300dpi.png`、`audit/300dpi/Yoccoz_1995_siegel_bruno_pdf_p090_il_label_crop_300dpi.png`、`audit/Yoccoz_1995_siegel_bruno_p090_ref_Il_crop_600dpi.png` |

- 最终复核：修复后从首行至末行完整复读 Markdown 全部 3672 行，并将上述十处分别与表列 PDF 原页图/裁片核对；两段空白页注入文本均已移除，Figure 1 图片目标存在。只读断言全部通过；AUDIT 仍有 91 条唯一页记录、无缺页或重复页，等级计数保持 PASS=4、PASS±=81、FAIL=6。`git diff --check` 在正文提交前通过。
- 这些修复不改写逐页审计原始等级；该候选仍待 Master-Luna 按 exact commit 集成，不能据此更新根级索引或进度。
