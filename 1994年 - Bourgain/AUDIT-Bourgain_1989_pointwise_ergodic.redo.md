# Bourgain · Pointwise ergodic theorems for arithmetic sets — Luna 审计重做

研究对象为 Jean Bourgain 1989 年论文（Publications mathématiques de l'I.H.É.S. 69 (1989), p. 5–41）的印刷 PDF 与 MinerU 派生 Markdown。本次审计判断 Markdown 是否忠实转录论文陈述、公式与编号，并一并重核此前 GPT-6 Luna（Peer-P04）审计所作修复的正确性。裁决源为 PDF 原页：150dpi pngmono 全页图 + pdftotext 文本层双通道对账，疑难位置另作高分辨率裁片。证据等级支持页面转录忠实度与旧修复正确性判断，不构成对定理或证明有效性的独立验证。

- 性质=Luna审计重做（用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- 日期时间起：2026-10-02 14:41:45 EDT
- PDF：`Bourgain_1989_pointwise_ergodic.pdf`，38 页；PDF SHA-256=`7890c91e6a54e8867a262430b90f6af7f14a2a3558ac78e5dd56c789c044a9ef`
- MD 基线 SHA-256=`ad3fe1901ab87c9f71944726a0fd32fa7eae5040223387d388c7935363d8a79e`（2,028 行；即 Luna 修复后基线）
- 页映射：PDF p.1 为 Numdam 题录/版权封面（无印刷页码），PDF p.2–38 对应印刷页 5–41。
- 文本层判定：`pdftotext -f 1 -l 1` 首页提取成功（Numdam 封面题录、版权条款完整可读）→ 文本层可用，采用「文本层主对账 + 150dpi PNG 逐页视觉核验」双通道；文本提取不能裁决的字形回看原页图（必要时高分辨率裁片）。
- 范围：本次运行块只覆盖 p.1–p.9（PDF 页序）；后续页由后续块继续。
- 证据图：`audit-redo/p0NN.png`（Ghostscript `pngmono`，150dpi）；不触碰旧 `audit/` 与旧 `AUDIT-Bourgain_1989_pointwise_ergodic.md`。
- 修复纪律：Markdown 内容错误用结构化 Edit 逐处修复（含纠正 Luna 旧修复中的错误），每处可溯源该页证据；印刷原文的错字与 quirk 忠实保留登记，绝不按数学预期静默改正；看不清的位置升级说明，不编造。

## 逐页记录（redo）

## p.001（PDF p.1 / Numdam 题录封面，无印刷页码）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p001.png`（Ghostscript `pngmono`，150dpi；原 PDF p.1）
- 核对：封面作者 Jean Bourgain、题名、期刊 *Publications mathématiques de l'I.H.É.S.*, tome 69 (1989), p. 5–41、Numdam 条目链接、版权/使用条款；文本层（`pdftotext -f 1 -l 1`）与 150dpi 原页图双通道，对 MinerU Markdown 第 1–11 行。
- 结果：PASS±。MD 开头逐项保留了作者、题名、刊卷年页码、`PMIHES_1989__69__5_0` 链接与全部版权/使用条款文字，与原页一致。原页另有版面件未入 MD：顶部横幅 “PUBLICATIONS MATHÉMATIQUES DE L'I.H.É.S.” 与底部 “Article numérisé dans le cadre du programme / Numérisation de documents anciens mathématiques / http://www.numdam.org/”（Numdam 制作署名）。均属档案封面版面件缺录，不影响论文题录或正文。链接行的尖括号在 MD 中录为 HTML 实体 `&lt;…&gt;`，渲染后与原页一致，登记不改。与 Luna 旧审（p.001 PASS±）结论一致；旧审未提顶部横幅缺录，本次补记。
- 时间：2026-10-02 14:41:45 EDT 落签

## p.002（PDF p.2 / 印刷 p.5 题名页；页面未印页码）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p002.png`（Ghostscript `pngmono`，150dpi；原 PDF p.2）
- 核对：论文题名、作者、“With an appendix on return-time sequences” 及 joint 合作者 HARRY FURSTENBERG / YITZHAK KATZNELSON / DONALD S. ORNSTEIN；§1 首段与公式 (1.1)。文本层 + 150dpi 原页图双通道，对 Markdown 第 13–37 行。
- 结果：PASS。题名行、appendix 说明、三位合作者、§1 首段（$[B_1]$、$[B_2]$、$[B_3]$、$(\Omega,\mathcal{B},\mu,T)$、polynomial $p(x)$）及 (1.1) 的 $A_{\mathbf{N}}f=\frac{1}{N}\sum_{1\leqslant n\leqslant N}T^{p(n)}f$ 全部与原页一致；后续段落 $N\to\infty$、$L^2(\Omega,\mu)$、$L^p$-theory ($p<2$) 与 a)/b)/c) 三条方法概述亦吻合。文本层在专名与显示式处有 OCR/布局噪声（如 “BirkhofTs”、(1.1) 拍平），150dpi 原页已裁决，Markdown 无错项。与 Luna 旧审（p.002 PASS）结论一致，无修复。
- 时间：2026-10-02 14:47 EDT 落签

## p.003（PDF p.3 / 印刷 p.6）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p003.png`（Ghostscript `pngmono`，150dpi；原 PDF p.3）
- 核对：§1 后半段（$\Lambda=\{[p(n)]\}$、full $L^p$-range、$L^1$ open）；圆周平方平均 (1.2) 与极大不等式 (1.3)（含积分上下限 0–1、sup 的指数 $p$、$n^2\alpha$、右端 $c\int f^p$、条件 $f\geqslant 0$）；过渡两句。文本层 + 150dpi 原页图双通道，对 Markdown 第 39–65 行。
- 结果：PASS±。全部公式与文字与原页一致；印刷源级语病 “Let $f$ be and $\mathbf{L}^p$-function”（原页如此）与 “straight forward” 在 Markdown 忠实保留，不按语法改正。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 6（版面件缺录，与 Luna 旧审记录一致，不误导）。与 Luna 旧审（p.003 PASS±）结论一致，无修复。
- 时间：2026-10-02 14:53 EDT 落签

## p.004（PDF p.4 / 印刷 p.7）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p004.png`（Ghostscript `pngmono`，150dpi；原 PDF p.4）；`audit-redo/p004_isometries_300dpi.png`（原 PDF p.4 300dpi 渲染后裁片，裁决 “positive isometries” 句的上标）。
- 核对：(1.4) 变差空间定义（含 sup 下标 $s;\,j_1<\dots<j_s$ 与 $x_{j_{s-1}}-x_{j_s}$、指数 $1/p$）；(1.5)–(1.6) 指数和与多项式；定理 1 陈述与 (1.7) 的范数/绝对值/上确界分组；定理后文字（$\mathbf{L}^r(\Omega,\mu)$、$r>1$、“positive isometries” 句、$p(x)=x^2$ 句）。文本层 + 150dpi 原页图 + 300dpi 局部裁片三通道，对 Markdown 第 67–121 行。
- 结果：FAIL（一处，已当场修复）。(1.7) 现为 $\|\sup_{\mathbf N}|A_{\mathbf N}f|\|_r\leqslant C\|f\|_r$，与原页分组一致（Luna 对 (1.7) 的旧修复经核正确）。但 Luna 旧修复把 “positive isometries” 句的空间改成 $\mathbf{L}^{1}(\Omega,\mu)$ 并声称印刷为 $L^1$；本次 300dpi 裁片清晰显示印刷上标为斜体 **r**，原页为 $\mathbf{L}^{r}(\Omega,\mu)$。已用 Edit 将该处改回 `$\mathbf{L}^{r}(\Omega,\mu)$`（Luna 旧修复中的错误，本次纠正）。其余：印刷源级 quirks “we considerer the variation spaces”、定理 1 的 “by a dynamical system”、“the limit if given by” 均忠实保留未改；(1.4)–(1.6) 的下标、求和界与系数与原页一致。Markdown 未保留原页运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 7。与 Luna 旧审（p.004 FAIL→修复）结论部分一致，但其 $L^1$ 判读经 300dpi 复核为误判。
- 时间：2026-10-02 15:01 EDT 落签

## p.005（PDF p.5 / 印刷 p.8）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p005.png`（Ghostscript `pngmono`，150dpi；原 PDF p.5）
- 核对：定理 2 陈述与 (1.8) 的 $T^{[p(n)]}f$、$1\leqslant n\leqslant N$；$L^r$-results ($r>1$) 句；CONTENTS 目录 1–9 条及页码 1/4/8/13/19/21/25/34/36；appendix 合作者与 $[B_4]$、$[B_6]$；§2 开头一段与谱测度 (2.1)。文本层 + 150dpi 原页图双通道，对 Markdown 第 111–149 行。
- 结果：PASS±。全部公式、目录条目、页码与合作者均与原页一致；(2.1) 的内积、$\widehat\nu(n)\equiv\int_0^1 e^{-2\pi i n\theta}\nu(d\theta)$ 与原页相符。微小字形注记：正文 “positive Radon measure v” 处印刷为斜体希腊 ν，Markdown 文字层用拉丁 v（下一行公式内为 $\nu$），不影响辨识。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 8。与 Luna 旧审（p.005 PASS±）结论一致，无修复。
- 时间：2026-10-02 15:09 EDT 落签

## p.006（PDF p.6 / 印刷 p.9）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p006.png`（Ghostscript `pngmono`，150dpi；原 PDF p.6）；`audit-redo/p006_gauss_300dpi.png`、`audit-redo/p006_arithsets_300dpi.png`（原 PDF p.6 300dpi 渲染后裁片，分别裁决 Gauss 和式指数与 “arithmetic sets” 拼写）。
- 核对：(2.2) 的归一化 $|\Lambda\cap[1,N]|^{-1}$ 与求和条件 $1\leqslant n\leqslant N,\ n\in\Lambda$；平方序列的极限两式（irrational → 0；Gauss-sums 定义 $S(q,a)$）；§2B 开头 $A_n f$、$f^*$ 定义；(2.3)、(2.4) 双范数不等式与 $L^{1,\infty}$ 定义行。文本层 + 150dpi 原页图 + 300dpi 局部裁片三通道，对 Markdown 第 151–207 行。
- 结果：PASS±。(2.3) 现为 $\|f^*\|_{L^p(\Omega,\mu)}\leqslant C(p)\|f\|_{L^p(\Omega,\mu)}$、(2.4) 现为 $\|f^*\|_{L^{1,\infty}(\Omega,\mu)}\leqslant C\|f\|_{L^1(\Omega,\mu)}$，均与原页一致——Luna 对 (2.3)/(2.4) 定界符的旧修复经核正确。Gauss 和式：300dpi 裁片显示印刷为 $e^{2\pi i\alpha r^2}$（希腊 α，无 /q），与 Markdown 现文完全一致；Luna 旧审备注称印刷为 $e^{2\pi iar^2/q}$ 属对原页的误述，但未导致 Markdown 错误，本次不修复、只更正记录。印刷源级 quirk “given by (4)” 忠实保留；“arithmetic sets” 拼写与原页一致（150dpi 下疑似的 “arithmetics” 经 300dpi 否定），该行闭引号后原页有一墨迹微点，非字符。§2B 的 $A_n f=\frac{1}{N}\sum_{n=1}^{N}T^nf$ 下标混用（$A_n$ 对 $1/N$）为原页排印原样，Markdown 忠实保留。Markdown 未保留运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS”、印刷页码 9 及右下角孤立数字 2。与 Luna 旧审（p.006 FAIL→修复）差异已修复的说法一致，但其等价性备注表述有误。
- 时间：2026-10-02 15:22 EDT 落签

## p.007（PDF p.7 / 印刷 p.10）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p007.png`（Ghostscript `pngmono`，150dpi；原 PDF p.7）；`audit-redo/p007_2.8_300dpi.png`（(2.8) 裁片）、`audit-redo/p007_ell_300dpi.png`（shift 不等式范数下标裁片；原 PDF p.7 300dpi 渲染后裁切）。
- 核对：(2.5) 受限极大函数（含源级 “$(f\leqslant 0)$” 条件）；轨道与截断 (2.6)；(2.7)；ℓ^p 链不等式；(2.8) 及其积分后的 $\|T^j\bar f\|_p^p$ 不等式（含 $C(p)^p$）；收尾 $\|\bar f\|_p\leqslant C(p)\frac{J}{J-\bar N}\|f\|_p$、$\|f^*\|_p$；弱型推导起点与集合计数式。文本层 + 150dpi 原页图 + 300dpi 局部裁片三通道，对 Markdown 第 203–275 行。
- 结果：PASS±。全部公式、求和界（(2.8) 右端 $0\leqslant j\leqslant J$ 对积分后右端 $0\leqslant j<J$ 的差别）与文字均与原页一致；Luna 对积分后不等式两处 Fraktur $\mathfrak p\to p$ 的旧修复经核正确（现为普通斜体 $p$，与原页相符）。两处原页排印原样在 Markdown 中忠实保留，本次补记：①(2.8) 左端 $\bar f(T^jx)$ 前印刷为双竖线、闭侧单竖线（300dpi 裁片证实为原页排印，非 MinerU 伪影）；②shift 不等式左范数下标印刷排为 $\ell^{1}\,\infty_{(\mathbf Z)}$（“1” 作 ℓ 下标、“$(\mathbf Z)$” 挂于 ∞ 下），Markdown 逐字对应，不按数学预期改写。源级语病 “in the some way” 忠实保留。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 10。与 Luna 旧审（p.007 FAIL→修复）已修复项一致；其未登记上述两条印刷 quirk。
- 时间：2026-10-02 15:35 EDT 落签

## p.008（PDF p.8 / 印刷 p.11）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p008.png`（Ghostscript `pngmono`，150dpi；原 PDF p.8）
- 核对：(2.9) 集合计数式与求和界；积分后 $\lambda\mu(\Omega_\lambda)\leqslant C\frac{J}{J-\bar N}\|f\|_1$；“The $L^2$ and $L^p$-inequalities ($p>1$)” 句；§2C 开头、$\|F-A_{N_\varepsilon}f\|_2<\varepsilon$；(2.10) 的 $\|\sup_{\mathbf N}|F-A_N(A_{N_\varepsilon}f)|\|_2<C\varepsilon$；$\frac{N_\varepsilon}{N}\|f\|_\infty$ 式；上极限结论行（首个 $\overline{\lim}$ 无下标、第二个带 $_N$）；(2.11) 一般子集平均；页末 “If the eigenfunctions …” 半句。文本层 + 150dpi 原页图双通道，对 Markdown 第 269–315 行。
- 结果：PASS±。全部公式与文字与原页一致；Luna 旧修复两处经核正确——“The $L^2$ and $L^p$” 第二空间恢复为 $L^p$ 与原页相符；(2.10) 的范数/绝对值/上确界定界符分组与原页相符。原页首个 $\overline{\lim}$ 确无下标 N、第二个带 $_N$，Markdown 逐字保留该字形差异，不补写。源级语病 “the ergodic means relates to the full set” 忠实保留。Markdown 未保留原页运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 11。与 Luna 旧审（p.008 FAIL→修复）已修复项一致，无新差异。
- 时间：2026-10-02 15:47 EDT 落签

## p.009（PDF p.9 / 印刷 p.12）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p009.png`（Ghostscript `pngmono`，150dpi；原 PDF p.9）；`audit-redo/p009_norm_notation_300dpi.png`（原 PDF p.9 300dpi 渲染后裁片，裁决 $v_s$ 记号行的两竖线间是否有圆点）。
- 核对：§2 收尾——密本征函数段的极大不等式 $\|f^*\|_p\leqslant C\|f\|_p$、模型 $(\mathbf T,\mathbf R_a)$；(2.12) 的 $Z_\varepsilon=\{[(1+\varepsilon)^n]\}$、$|A_Nf-A_{N'}f|\leqslant 2\varepsilon$；(2.13) 的 $\mathcal M_j$ 定义（sup 范围 $N_j\leqslant N\leqslant N_{j+1},\ N\in Z_\varepsilon$）；(2.14) 的 $o(J)\|f\|_2$；§3 开头 (3.1)、(3.2) 变差范数定义（求和上界 $J$、指标链 $n_1<\dots<n_J$ / $t_1<\dots<t_J$）；Lépingle [Lé]、[P-X] 引用句。文本层 + 150dpi 原页图 + 300dpi 局部裁片三通道，对 Markdown 第 313–365 行。
- 结果：PASS±。全部公式与文字与原页一致；Luna 对 (3.2) 求和上界 $s\to J$ 的旧修复经核正确（现与 (3.1) 同为 $J$，与原页相符）。原页排印原样在 Markdown 中忠实保留，本次登记：①$v_s$ 记号行印刷即两竖线间空心（无 $\cdot$），300dpi 裁片证实，Markdown 的 `$||\|_{v_s}$` 逐字对应，不按预期补点；②(3.1)、(3.2) 的条件只列到 $n_J/t_J$ 而差分出现 $n_{j+1}/t_{j+1}$，为原页自身的索引排布，Markdown 忠实保留（与 Luna 旧审登记一致）；③(2.13) 的 `where` 与 $\mathcal M_j$ 之间 Markdown 无空格（`\text{where}\mathcal{M}_jf`），MinerU 间距伪影，渲染稍挤但不误导，登记不改。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 12。与 Luna 旧审（p.009 FAIL→修复）已修复项一致，无新差异。
- 时间：2026-10-02 16:02 EDT 落签

## p.010（PDF p.10 / 印刷 p.13）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p010.png`（Ghostscript `pngmono`，150dpi；原 PDF p.10）
- 核对：Lemma 3.3 陈述与 (3.4)；Doob 振荡引理 (3.5)；Lorentz 空间 (3.6)（范围 $3/2\leqslant p\leqslant s<5/2$）；$\chi_{\mathbf A}$、$\mu(\mathbf A)=\varepsilon$、$\|f\|_{p,1}=\varepsilon^{1/p}$ 段；(3.7) 的 $2^{-ks}$、$N_{2^{-k}}$ 与闭括号；(3.8) 的 $2^{-kp}$、$(N_{2^{-k}})^{p/s}$、$2^{-kp(1-2/s)}$、$\|f\|_r^r$；$r=2p/s$、$6/5\leqslant r<2$ 段；(3.9)–(3.10) Fourier 定义。文本层 + 150dpi 原页图双通道，对 Markdown 第 367–413 行。
- 结果：PASS±。全部公式与文字与原页一致；Luna 旧修复三处经原页核验正确——(3.6) Lorentz 空间为普通斜体 $p$（非 Fraktur）、(3.7) 右端闭括号恢复、(3.7)/(3.8) 跳跃计数下标为 $N_{2^{-k}}$（非 $2^{-k}$ 误录为 $2-k$ 后的残形）。Markdown 未保留原页运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 13。与 Luna 旧审（p.010 FAIL→修复）已修复项一致，无新差异、无修复。
- 时间：2026-10-02 16:52 EDT 落签

## p.011（PDF p.11 / 印刷 p.14）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p011.png`（Ghostscript `pngmono`，150dpi；原 PDF p.11）；`audit-redo/p011_3.14_norm_300dpi.png`、`audit-redo/p011_3.16_rhs_300dpi.png`、`audit-redo/p011_3.19_300dpi.png`（原 PDF p.11 300dpi 渲染后裁片，裁决 (3.14)/(3.16)/(3.18)/(3.19) 的 $v$ 下标）。
- 核对：Lemma 3.11 与 (3.12)；Poisson 半群乘子 $\widehat P_t(\lambda)$；(3.13)；(3.14) 与 $K=\chi-P_1$；(3.15) 两条 Fourier 估计；(3.16) 点态估计两项；(3.17) Parseval；(3.18)；$\eta$ 分解与 $\sum_\alpha\eta(2^\alpha\lambda)=1$；(3.19)；(3.20) 的 $2^{-|\alpha|}$。文本层 + 150dpi 原页图 + 300dpi 局部裁片三通道，对 Markdown 第 415–479 行。
- 结果：FAIL（四处 $v$ 下标误读，已当场逐处修复）。300dpi 放大裁片裁决：印刷 (3.14) 为 $\mathrm{L}^2_{v_s}$（Markdown 误作 $v_2$）；(3.16) 右端范数为 $v_2$（Markdown 误作 $v_3$；左端 $v_2$ 本就正确）；(3.18) 为 $\mathrm{L}^2_{v_s}$（误作 $v_3$）；(3.19) 为 $\mathrm{L}^2_{v_s}$（误作 $v_3$）。已用 Edit 按原页改正四处。此页 $v_2/v_3/v_s$ 混排为 Luna 旧审未发现的残留 MinerU 下标误读。其余：Luna 对 Poisson 乘子 $e^{-i|\lambda|}\to e^{-t|\lambda|}$ 的旧修复经原页核验正确；(3.12)、(3.13)、(3.15)、(3.17)、(3.20) 的指数、常数与范围均与原页一致。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 14。与 Luna 旧审（p.011 FAIL→修复）结论部分一致，但漏检上述四处下标。
- 时间：2026-10-02 17:12 EDT 落签
