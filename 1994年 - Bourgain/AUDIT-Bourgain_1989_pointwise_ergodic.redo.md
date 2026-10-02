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

## p.012（PDF p.12 / 印刷 p.15）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p012.png`（Ghostscript `pngmono`，150dpi；原 PDF p.12）；`audit-redo/p012_3.21_3.22_300dpi.png`、`audit-redo/p012_averages_300dpi.png`、`audit-redo/p012_corollary_300dpi.png`（原 PDF p.12 300dpi 渲染后裁片，分别裁决 (3.21)/(3.22) 标签挂接、averages 显示式分母、Corollary 3.25 字形）。
- 核对：net $2^k=u_1<\dots<u_N=2^{k+1}$、$N=N_\alpha$ 段；(3.21)/(3.22) 双标签显示式（(3.21) 标 $\|{\cdot}\|_{v_2}\leqslant[\cdots]^{1/2}+$ 两行、(3.22) 标 $\{[\int|\partial_t|\,dt]^2\}^{1/2}$ 行）与 “majorizing $v_2$ by $v_1$”；(3.23) 的 $CN_\alpha^{1/2}2^{-|\alpha|}$ 与 $|\lambda|\sim2^{-\alpha-k}$；(3.24) 三行与 $=CN_\alpha^{-1/2}$；代入 (3.19) 的合并界与 “chosing $N_\alpha=2^{|\alpha|}$”；“Summation of (3.17), (3.18) yields (3.14)”；application 显示式 $A_Nf$；Corollary 3.25 与 (3.26) 的 $c(s)\|f\|_2$；末段。文本层 + 150dpi 原页图 + 300dpi 局部裁片三通道，对 Markdown 第 481–527 行。
- 结果：FAIL（两处，已当场修复）。①(3.21)/(3.22)：原页两个标签分别挂在显示式前两行（$\|\cdot\|_{v_2}\leqslant[\cdots]^{1/2}+$）与第三行（$\{\cdots\}^{1/2}$）上；Markdown 把 “(3.21)” 留成孤立文本行、整个 array 只挂 (3.22)，标签归属错位。已按原页拆分为两个显示式并分别挂 (3.21)、(3.22)。②application 显示式 $A_Nf=\frac{1}{N}\sum_{1\leqslant n\leqslant N}T^nf$：300dpi 裁片证实印刷分母为普通粗体 $N$、无上划线；Markdown 误作 $\frac{1}{\overline{\mathbf N}}$（引入受限平均记号），已改为 $\frac{1}{\mathbf N}$。其余：(3.21) 首行范数下标 $v_2$ 经 300dpi 确认与 Markdown 一致；Corollary 3.25 的 DS 四元组第二位印刷即为粗体 K 字形（$(\Omega,\mathbf K,\mu,\mathbf T)$，原页如此，非 σ-代数记号 $\mathcal B$），Markdown 忠实转录，登记不改（与 Luna 旧审登记一致）；(3.23)–(3.26)、合并界、“chosing” 原样均与原页一致。Markdown 未保留原页运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 15。与 Luna 旧审（p.012 PASS±）结论不同：本页存在两处标签/记号级内容错误（Luna 漏检），均已修复。
- 时间：2026-10-02 17:34 EDT 落签

## p.013（PDF p.13 / 印刷 p.16）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p013.png`（Ghostscript `pngmono`，150dpi；原 PDF p.13）
- 核对：(3.27) 的 $\varphi=-\int_0^\infty\chi_t\cdot\varphi'(t)t\,dt$、$\chi_t=\frac1t\chi_{[0,t]}$；Lemma 3.28 与 (3.29) 的 $\int|\varphi'(x)||x|dx$ 权重；熵数定义段（$\mathrm M_\lambda(\mathbf A)$、$\mathrm M_\lambda=0$ if $\mathrm{diam}\,\mathbf A<\lambda$）；Lemma 3.30 与 (3.31) 的 $c_\varphi(s-2)^{-1}$、$\mathbf C_\varphi=\int|\varphi'(x)||x|dx$；(3.32) 与 $t_j$ min 定义；正交基展开显示式（$[\sum_\alpha\|\{f_\alpha*\varphi_t\}\|^2]^{1/2}$ 链）；Lemma 3.33 与 (3.34) 的 $c'_\varphi(\log K)^2$；证明开头 $f_\alpha^*$ 定义。文本层 + 150dpi 原页图双通道，对 Markdown 第 529–597 行。
- 结果：PASS±。全部公式、常数大小写（(3.31) 的小写 $c_\varphi$ 对 where 行的大写 $\mathbf C_\varphi$）与文字均与原页一致，未发现 Markdown 内容偏差。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 16。与 Luna 旧审（p.013 PASS±）结论一致，无修复。
- 时间：2026-10-02 17:46 EDT 落签

## p.014（PDF p.14 / 印刷 p.17）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p014.png`（Ghostscript `pngmono`，150dpi；原 PDF p.14）
- 核对：(3.35) 的 $c_\varphi\|f_\alpha\|_2$；(3.36) 的 $\mathrm F=[\Sigma(f_\alpha^*)^2]^{1/2}$；min$(\mathrm K,\mathrm M_\lambda(x))^{1/2}$ 两行估计（积分限 $K^{-1/s}F(x)$ 至 $F(x)$、$K^{1/2-1/s}$、$\sup_{\lambda>0}\lambda\cdot M_\lambda(x)^{1/s}$）；“(3.34) follows … letting $\frac12-\frac1s=(\log K)^{-1}$”；§4 标题与开头两段；$\Pi=\mathbf R/\mathbf Z$ 约定；Lemma 4.1 与 (4.2) 的 $\min_{1\leqslant k\leqslant K}|\lambda-\lambda_k|\leqslant2^{-j}$、Then、(4.3) 的 $\ell^2(\mathbf Z)$ 范数与 $C(\log K)^2$；Remark；$\mathcal F$ 约定段。文本层 + 150dpi 原页图双通道，对 Markdown 第 599–635 行。
- 结果：PASS±。全部公式与文字与原页一致；Markdown 中的粗体/罗马 $\mathrm K$ 与原页 K 字形风格差异不误导（Luna 旧审已登记同类字形注记）。原页右下角有一孤立印刷数字 3（页边杂标），与运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS”、印刷页码 17 一同未入 Markdown，属版面件缺录。与 Luna 旧审（p.014 PASS±）结论一致，无修复。
- 时间：2026-10-02 17:58 EDT 落签

## p.015（PDF p.15 / 印刷 p.18）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p015.png`（Ghostscript `pngmono`，150dpi；原 PDF p.15）；`audit-redo/p015_4.7_4.8_300dpi.png`（原 PDF p.15 300dpi 渲染后裁片，裁决 (4.7)/(4.8) 标签挂接）。
- 核对：Lemma 4.4 与 (4.5)（$\mathrm L^2(\mathbf R)$ 乘子极大不等式）、Then、(4.6)（$\ell^2(\mathbf Z)$、$CB$）；$B_1$、$u\in[0,\rho]$ 分解式；(4.7)/(4.8) 两加项（(4.7) 标 $\rho^{-1/2}\|\sup_\varphi\cdots\|_{L^2(\mathbf R)}+$ 行、(4.8) 标 $\sup_{0<u<\rho}\cdots$ 行）；(4.9) 的 $\rho^{-1/2}B\|\mathscr Ff\|_{L^2[0,1]}$；(4.10) 三行链；$B_1\leqslant\rho^{-1/2}B+C\rho B_1$；Lemma 4.11 陈述与 (4.12)；Lemma 4.13 条件与 (4.14)。文本层 + 150dpi 原页图 + 300dpi 局部裁片三通道，对 Markdown 第 637–693 行。
- 结果：FAIL（一处，已当场修复）。(4.7)/(4.8)：原页 (4.7) 挂在显示式第二行（$\rho^{-1/2}\|\sup_\varphi|\mathcal F^{-1}[\varphi\mathcal Ff]|\|_{L^2(\mathbf R)}+$）、(4.8) 挂在第三行（$\sup_{0<u<\rho}\cdots$），与下文 “By (4.5), (4.7) is clearly bounded by”/“By definition of $B_1$, (4.8) is bounded by” 的分别引用对应；Markdown 把 “(4.7)” 留成孤立文本行、整个 array 只挂 (4.8)。已按原页拆分为两个显示式并分别挂 (4.7)、(4.8)（与 p.12 (3.21)/(3.22) 同类 MinerU 标签错挂，Luna 旧审对本页只记录了 (4.5)/Then 错位、漏检此处）。其余：Luna 对 (4.5)/Then/(4.6) 顺序的旧修复经原页核验正确；(4.9)–(4.14) 的常数、范数与 supp 条件均与原页一致。字形注记：Lemma 4.11 陈述在 Markdown 用黑板体 $\mathbb K$、$\mathbb R_j$、$\mathbb Z$，原页为普通斜体/罗马字母，属字体映射伪影、不误导，登记不改。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 18。
- 时间：2026-10-02 18:16 EDT 落签

## p.016（PDF p.16 / 印刷 p.19）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p016.png`（Ghostscript `pngmono`，150dpi；原 PDF p.16）；`audit-redo/p016_4.21_4.22_300dpi.png`（原 PDF p.16 300dpi 渲染后裁片，裁决 (4.21) 的 “2.2^s” 点符与 (4.22) 下标括号）。
- 核对：(4.15) 的 $\mathrm L^2[0,\tau^{-1}]$、上界 $K$ 与 $\mathrm C\tau^{-1/2}$；$\overline a=(a_k)$ 段；(4.16) supp $\hat f_k\subset[-\tau,\tau]$；$\sigma_u$ 平移算子；(4.17) 的 $\frac12\|f_k\|_2$ 与 $\frac{1}{100}\tau^{-1}$；$B$ 与 $CK^{1/2}$ 括注；(4.18) 两显示（LHS $\leqslant$ + 带 $\sigma_u$ 的 sup 范数 $+\frac12B(\sum\|f_k\|_2^2)^{1/2}$）；“Integrating (4.18) in $u$ on $[0,\tau^{-1}/100]$”；(4.19) 双重 $L^2$ 范数；目标 $\mathrm C(\log K)^2(\sum\|f_k\|_2^2)^{1/2}$；(4.20) $A=A_x$；(4.21) $|\bar b|\leqslant 2.2^s$；(4.22) $\#\mathbf B_s\leqslant\mathbf M_{(2^s)}$；(4.23) 分解与 “cardinality” 括注。文本层 + 150dpi 原页图 + 300dpi 局部裁片三通道，对 Markdown 第 695–757 行。
- 结果：PASS±。全部公式与文字与原页一致；Luna 旧修复三处经原页核验正确——(4.15) 的 $L^2$ 范数与上界 $K$、(4.17) 的 $\frac{1}{100}$、(4.21)/(4.22) 标签归位。300dpi 裁片裁决两点：①(4.21) 两处 2 之间的点符印刷即为**基线句点** “2.2^s”（非中点 $\cdot$，原页排印如此），Markdown 的 “2. 2^s” 忠实对应，不改为 $\cdot$、登记为 print quirk（Luna 旧审修复登记把它描述为 $2\cdot2^s$，与原页点符位置不符，仅更正记录）；②(4.22) 下标印刷确带括号 $\mathbf M_{(2^s)}$，Markdown 一致。另：Luna 修复登记把 (4.24) 的范数修复列在 PDF p.16 名下，但本页止于 (4.23) 及其括注，(4.24) 实在下一页（见 p.017 记录），属登记页码误挂、不影响修复本身。Markdown 未保留原页运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 19。与 Luna 旧审（p.016 FAIL→修复）已修复项一致，本页无新差异、无修复。
- 时间：2026-10-02 18:34 EDT 落签

## p.017（PDF p.17 / 印刷 p.20）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p017.png`（Ghostscript `pngmono`，150dpi；原 PDF p.17）；`audit-redo/p017_4.24_300dpi.png`（(4.24) 范数下标放大裁片）、`audit-redo/p017_4.28_4.29_300dpi.png`（(4.28)/(4.29) 标签挂接裁片；原 PDF p.17 300dpi 渲染后裁切）。
- 核对：Estimate 无编号式（$\sup_{t>0}$ 对 $\sum_{s\in\mathbf Z}\max_{\bar b\in\mathbf B_s}$）；(4.24) 的求和与范数；“For given $s$” 的 min{2^{s+1}K^{1/2}, […]} 界；(4.25) 两行与 $\sim\mathrm C\tau^{-1/2}\int_0^\infty\min(K,M_\lambda(x))^{1/2}d\lambda$；“Taking the $L^2(dx)$-norm … This proves (4.14)”；Lemma 4.26 与 (4.27)；$\hat\varphi=1$ on $[-\frac12,\frac12]$；(4.28)/(4.29) 分解（(4.28) 标前两行、(4.29) 标第三行）；$g*\varphi_{2^j}=(g*\varphi_{2^{s-1}})*\varphi_{2^j}$ 段与 “f.e^{-2πiλ_k x}” 基线点排布；(4.30)；(4.31) 两行。文本层 + 150dpi 原页图 + 300dpi 局部裁片三通道，对 Markdown 第 759–815 行（本页止于 (4.31)；MD 813/815 两句在下一页核对）。
- 结果：FAIL（两处，已当场修复）。①(4.24)：300dpi 放大裁片显示印刷范数下标为 $\mathrm L^2([0,\tau^{-1}])$——**无 “,du”**；Luna 旧修复在此式补入的 “, du” 为原页所无（正文行 “the $L^2([0,\tau^{-1}],du)$-norm” 的 du 为原文所有、保留），已删去。②(4.28)/(4.29)：原页 (4.28) 挂显示式前两行（$\sup_{j\geqslant s}|\cdots|\leqslant$ 与 sup 加项行）、(4.29) 挂第三行（$+\{\sum_{j\geqslant s}|\cdots|^2\}^{1/2}$），与下文 “bound on (4.28)”/“(4.29) is bounded by” 分别引用对应；Markdown 把 “(4.28)” 留成孤立文本行、整个 array 只挂 (4.29)。已按原页拆分并分别挂标签（与 p.12、p.15 同类 MinerU 错挂，Luna 漏检）。其余：(4.25)、(4.27)、(4.30)、(4.31) 与 Lemma 4.26 陈述均与原页一致。Luna 旧修复登记两处勘误：其把 (4.24) 的范数修复列在 PDF p.16 名下（实在本页），且该修复把下标写成 $L^2([0,\tau^{-1}],du)$ 与原页不符（见上）。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 20。
- 时间：2026-10-02 19:18 EDT 落签

## p.019（PDF p.19 / 印刷 p.22）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p019.png`（Ghostscript `pngmono`，150dpi；原 PDF p.19）
- 核对：$\widetilde g_j=\mathcal F^{-1}[\chi_{\mathrm R_j}\mathcal Fg_j]$ 与 (4.35)；Hölder 四行链（$S_{c,0}/S_{c,1}$ 分解、$(1+2Bs)$ 收尾）与 “proving (4.33)”；Proof of (4.12) 的 S 定义（$K^{-1}2^{-j}<|\lambda_k-\lambda_{k'}|<K2^{-j}$）；(4.36) 的 $|S|\leqslant K^3$；$Z_r$ 定义与 (4.37) 的 $Z_1\prec Z_2\prec\dots\prec Z_K$；$j_r=\min Z_r$、$\Lambda_r$；(4.38) 分离条件与 (4.39) 内外包络；对偶 B 式；$\mathbf G_r/\widetilde{\mathbf G}_r$ 设定及 $\|\sum_j\widetilde g_j\|_2$ 链；$Z_r\prec Z_{r'}$ 段、$\langle\widetilde g_j,\widetilde g_{j'}\rangle$、$\langle\widetilde G_r,\widetilde G_{r'}\rangle$ 与 $\|\Sigma\widetilde G_r\|_2^2$ 展开式。文本层 + 150dpi 原页图双通道，对 Markdown 第 864–942 行（现行号）。
- 结果：PASS±。全部公式与文字与原页一致；Luna 对 (4.38)/(4.39) 的标签修复经原页核验正确——(4.38) 现挂分离条件、(4.39) 现挂包络式，与原页一一对应。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 22。与 Luna 旧审（p.019 FAIL→修复）已修复项一致，无新差异、无修复。
- 时间：2026-10-02 19:12 EDT 落签

## p.020（PDF p.20 / 印刷 p.23）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p020.png`（Ghostscript `pngmono`，150dpi；原 PDF p.20）
- 核对：“The same argument as in (4.32) than shows that”（源级 “than” quirk）；(4.40) 的 $\mathrm B^2\leqslant(\log\mathrm K)^2+\mathrm B_1^2+\mathrm B(\log\mathrm K)$；(4.41) 的 $\|\sup_{j\in\mathbf Z_r}|\mathcal F^{-1}[\chi_{\mathrm R_j}\mathcal Ff]|\|_2\leqslant\mathrm B_1\|f\|_2$ 双范数+内层绝对值；$B_1$ 估计段（apply (4.26) with $\Lambda=\Lambda_r$, $s=j_r$）与 “Lemma's 4.11 and 4.1”；§5 标题与开头；(5.1) 的 $\frac1N\sum_{n=1}^N$；(5.2) 多项式；Lemma 5.3 条件 $|\alpha_d-(a/q)|<1/q^2$ 与 (5.4) 的 $[q^{-1}+n^{-1}+qn^{-d}]^\rho$、$\rho=1/2^{d-1}$；[Vaug]/[Vin]；$\mathbf Q$、$\delta=\delta(d)$、$\theta_j\in[0,1]\cap\mathbf Q$；(5.5) major box 的 $N^{-j+\delta}$；Lemma 5.6 与 (5.7) 的 $\mathrm{CN}^{-\delta'}$。文本层 + 150dpi 原页图双通道，对 Markdown 第 944–1001 行（现行号）。
- 结果：PASS±。全部公式与文字与原页一致；Luna 对 (4.41) 双范数及内层绝对值的旧修复经原页核验正确；源级语病 “than shows”、“Lemma's 4.11” 忠实保留。微小排版注记：(5.4) 的 “where” 在 Markdown 中为数学模式散排字母 `w h e r e`，渲染为斜体连排、可辨识，登记不改。Markdown 未保留原页运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 23。与 Luna 旧审（p.020 FAIL→修复）已修复项一致，无新差异、无修复。
- 时间：2026-10-02 19:24 EDT 落签

## p.021（PDF p.21 / 印刷 p.24）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p021.png`（Ghostscript `pngmono`，150dpi；原 PDF p.21）
- 核对：$\varphi_{\mathbf N}(\bar\alpha)$ 形状段（$\theta_j=a_j/q$、$\alpha_j=\theta_j+\beta_j$、$n=qs+r$）；(5.8) 的 $o(N^{-1+2\delta})$；(5.9) 双因子分解与 $o(N^{-1/2})$；(5.10) Gauss 和定义；(5.11) 的 $V_N(\bar\beta)$；Lemma 5.12 与 (5.13) 的 $O(N^{-1/2})$、where $\theta_j=a_j/q$；Lemma 5.14 与 (5.15) 的 $cq^{-\delta'}$；“consequence of (5.3)”；A. Weil 句；(5.16)；Lemma 5.17 的 (5.18)（$|1-V_N|<C\sum|\beta_j|N^j$）与 (5.19)（$|V_N|<C[1+\sum|\beta_j|N^j]^{-1/d}$）、where $\mathbf C=c(d)$；van der Corput 收尾句。文本层 + 150dpi 原页图双通道，对 Markdown 第 1004–1070 行（现行号）。
- 结果：PASS±。全部公式与文字与原页一致；Luna 对 (5.18)/(5.19) 标签的旧修复经原页核验正确——(5.18) 现挂 $|1-V_N(\bar\beta)|$ 界、(5.19) 现挂 $|V_N(\bar\beta)|$ 界，与原页一致；A. Weil's estimate 句与原页相符。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 24。与 Luna 旧审（p.021 FAIL→修复）已修复项一致，无新差异、无修复。
- 时间：2026-10-02 19:36 EDT 落签

## p.022（PDF p.22 / 印刷 p.25）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p022.png`（Ghostscript `pngmono`，150dpi；原 PDF p.22）
- 核对：§6 标题与开头（$[B_1]$、uses less structure）；(6.1) 平均式与 (6.2) 多项式（$b_j\in\mathbf Z$、$b_d>0$）标签归位；源级 “where reduced to proving…” quirk；(6.3) 的 $A_N\mathcal F=f*K_N$（原页 LHS 即 $\mathcal F$）与 $K_N=\frac1N\sum\delta_{p(n)}$；(6.4)；(6.5) 的 $\varphi_N(-b_1\alpha,\dots)\equiv\varphi_N(-\alpha.\bar b)$；(6.6) 的 $2^s\leqslant q<2^{s+1}$ 与 $\mathcal R_0=\{0\equiv1\}$；ζ 定义段（$\pm\frac{1}{10}$、$\pm\frac{1}{5}$、$r<2$）；(6.7) 的 $\zeta(10^s(\alpha-\theta))$；(6.8) $S(\theta)$ 定义与 (6.9) $w_N(\beta)$ 标签；(6.10) 的 $O(N^{-1/2})$、$|\alpha-\theta|<N^{-d+\delta}$；(6.11) 的 $C2^{-s\delta'}$。文本层 + 150dpi 原页图双通道，对 Markdown 第 1072–1136 行（现行号）。
- 结果：PASS±。全部公式与文字与原页一致；Luna 三处旧修复经原页核验正确——(6.1)/(6.2) 标签归位、(6.7) 的 $10^s$ 完整、(6.8)/(6.9) 标签归位；源级 “where reduced…” 与 (6.3) 左端 $A_N\mathcal F$（原页原样）忠实保留。原页右下角有孤立印刷数字 4（页边杂标），与运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS”、印刷页码 25 一同未入 Markdown，属版面件缺录。与 Luna 旧审（p.022 FAIL→修复）已修复项一致，无新差异、无修复。
- 时间：2026-10-02 19:48 EDT 落签

## p.023（PDF p.23 / 印刷 p.26）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p023.png`（Ghostscript `pngmono`，150dpi；原 PDF p.23）
- 核对：(6.12) 的 $|1-w_N(\beta)|<C|\beta|N^d$ 与 (6.13) 的 $[1+|\beta|N^d]^{-1/d}$ 标签归位；disjointly supported 句；Lemma 6.14 与 (6.15) 的 $CN^{-\delta_1}$；replacement 句；Proof of (6.14) 与 (6.16) 的 $N^{-d+\delta}$；Case 1 与 (6.17) 的 $\zeta(10^{s_0}(\alpha-\theta_0))$；$10^{s_0}<N^{4\delta}$ 段；$|\alpha-\theta|\geqslant|\theta-\theta_0|-|\alpha-\theta_0|$、$|\theta-\theta_0|>\frac12q^{-1}2^{-s_1}\geqslant\frac14N^{-2\delta}$ 无编号式；$(\log N).N^{-1+(2\delta/d)}$ 收尾；Case 2 与 (6.18) 的 $C2^{-s_1\delta'}$。文本层 + 150dpi 原页图双通道，对 Markdown 第 1140–1194 行（现行号）。
- 结果：PASS±。全部公式与文字与原页一致；Luna 两处旧修复经原页核验正确——(6.12)/(6.13) 标签归位（(6.12) 挂 $|1-w_N|$ 界、(6.13) 挂 $|w_N|$ 界）、(6.17) 的尺度 $10^{s_0}$ 完整。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 26。与 Luna 旧审（p.023 FAIL→修复）已修复项一致，无新差异、无修复。
- 时间：2026-10-02 20:00 EDT 落签

## p.024（PDF p.24 / 印刷 p.27）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p024.png`（Ghostscript `pngmono`，150dpi；原 PDF p.24）
- 核对：Case 2 收尾（$CN^{-\delta/d}$、“This proves Lemma (6.14).” 括号原样）；(6.19) 的 $\|\sup_N|f*K_N|\|_{\ell^2(\mathbf Z)}\leqslant C\|f\|_{\ell^2(\mathbf Z)}$；$Z_1=\{2^k\}$；(6.20)；(6.21) 三行（含 $\psi_N$ 与 $\Sigma_{s=0}^\infty$ 行）；(6.22) 的 $\chi(N^d(\alpha-\theta))\zeta(10^s(\alpha-\theta))$；$\chi=\chi_{[-1,1]}$；(6.23)；(6.24)；$N^d=2^j$ 段；(6.25) $\mathcal F[g_s]$ 定义与 (6.26) $\widetilde\psi_{s,N}\mathcal Ff=\mathcal F[g_s]\chi_{\mathrm R_j}$ 标签；(6.27) 两行；$|\mathcal R_s|<4^s$、$\|g_s\|_2$ 界；(6.28) 的 $C.s^22^{-s\delta'}$。文本层 + 150dpi 原页图双通道，对 Markdown 第 1196–1259 行（现行号）。
- 结果：PASS±。全部公式与文字与原页一致；Luna 三处旧修复经原页核验正确——(6.19) 的 $\ell^2(\mathbf Z)$ 双范数完整、(6.22) 的 $10^s$ 完整、(6.25)/(6.26) 标签归位且 (6.26) 变量为小写 $\widetilde\psi$；源级 “This proves Lemma (6.14).” 的括号排布忠实保留。Markdown 未保留原页运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 27。与 Luna 旧审（p.024 FAIL→修复）已修复项一致，无新差异、无修复。
- 时间：2026-10-02 20:12 EDT 落签

## p.025（PDF p.25 / 印刷 p.28）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p025.png`（Ghostscript `pngmono`，150dpi；原 PDF p.25）；`audit-redo/p025_6.36_v4_300dpi.png`（原 PDF p.25 300dpi 渲染后放大裁片，裁决 (6.36) 变差范数下标）。
- 核对：(6.29) 的 $C(\sum_{s=0}^\infty s^22^{-s\delta'})\|f\|_2$；(6.30) 的 $\|\sup_N|A_Nf|\|_2\leqslant C\|f\|_2$ 外层双范数；(6.31) 的 $o(J)\|f\|_2$；(6.32) 的 $\mathcal M_j$ 定义（严格不等号 $N_j<N<N_{j+1}$、$N\in Z_\varepsilon$）；$Z_\varepsilon$ 与 rapidly increasing 句；(6.33) 的 $C\varepsilon^{-1}2^{-\delta''s_0}$；(6.34)；$w_N$ 与 additional factor 句；(6.35) 的 $\widetilde{\mathcal M}_j f$ 与 $\chi_{(N^d)}$；$\chi_t$ 定义；(6.36) 的 $J^{1/4}$ 与右端 $v_4$ 下标；源级 “is follows from (6.36) and (3.26)” quirk；$\sum\|\widetilde{\mathcal M}_jf\|_2^2\leqslant CJ^{1/2}\|f\|_2^2$ 无编号式。文本层 + 150dpi 原页图 + 300dpi 放大裁片三通道，对 Markdown 第 1262–1318 行（现行号）。
- 结果：PASS±。全部公式与文字与原页一致；Luna 对 (6.30) 外层 $L^2$ 极大范数的旧修复经原页核验正确；源级语病 “is follows” 忠实保留。(6.36) 右端范数下标经 300dpi 放大裁决为粗体 $v_4$（非 $v_s$），与 Markdown 一致、无需修复。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 28。与 Luna 旧审（p.025 FAIL→修复）已修复项一致，无新差异、无修复。
- 时间：2026-10-02 20:26 EDT 落签

## p.018（PDF p.18 / 印刷 p.21）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p018.png`（Ghostscript `pngmono`，150dpi；原 PDF p.18）；`audit-redo/p018_tree_print_300dpi.png`（原页二叉分割树 300dpi 裁片）、`audit-redo/p018_tree_mineru_source.jpg`（Markdown 所引 MinerU 源图 `images/page_17_image_16.jpg` 的本篇审计副本，SHA-256=`56b9ebd4824c8c914b3e42f7fc1d81cf5d68c435138e0c786e1f40d4a2739d43`）。
- 核对：p.017 收尾两句（$\chi_{\mathbf R_j}$ 差的 vanishing 条件 $\mathrm{dist}(\lambda,\Lambda)<2^{-j-1}$ / $>2^{-j}$；“Now, (4.27) is implied by (4.30), (4.31)”）；Remark（$a/q$、$(a,q)=1$、$q\leqslant Q$、neighborhoods $\ll Q^{-2}$）；Lemma 4.32 的 $R_j$ 定义（无编号显示式）→ Then → (4.33) 的 $\sup_{j\in\mathbb S}$ 与 $(\log|S|)\|f\|_2$；“for S a finite subset of Z”；BDG-Stein 证明开头；$R_{j+1}\subset R_j$、$s\sim\log|S|$；B 最优常数式；(4.34) 对偶式；“diadic partitioning of S” 与二叉树图。文本层 + 150dpi 原页图 + 300dpi 局部裁片 + MinerU 源图对照，对 Markdown 第 813–855 行。
- 结果：PASS±。全部文字与公式与原页一致；Luna 对本页的旧修复（分离 $R_j$ 定义与 “Then”、把 (4.33) 标签移到极大不等式上）经原页核验正确——现行顺序 $R_j$ 定义（无编号）→ “Then” → (4.33) 与原页相符。树图：Markdown 所引 `images/page_17_image_16.jpg` 与原页二叉分割树逐结点吻合（根 $S_0=S$，第二层 $S_0$、$S_1$，四叶 $S_{0,0}$、$S_{0,1}$、$S_{1,0}$、$S_{1,1}$），源图哈希已登记。字形注记同前：MD 的 $\mathbb K$、$\mathbb R_j$、$\mathbb S$、$\mathbb Z$ 黑板体对应原页普通字形，不误导、不改。Markdown 未保留原页运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 21。与 Luna 旧审（p.018 FAIL→修复）已修复项一致，无新差异、无修复。
- 时间：2026-10-02 19:18 EDT 落签
