# Bourgain · Pointwise ergodic theorems for arithmetic sets

研究对象为 Jean Bourgain 1989 年论文的印刷 PDF 与 MinerU 派生 Markdown。此审计判断 Markdown 是否忠实转录论文陈述、公式与编号；证据来自 born-digital PDF 文本层逐项对账、38 页原页图核验与疑难位置的高分辨率裁片。证据等级支持页面转录忠实度判断，不构成对定理或证明有效性的独立验证。

- actor=Peer-P04; model=gpt-6-luna; effort=max
- 状态：38/38 页逐页核对与逐处 Markdown 修复已完成；修复后的 2,028 行 Markdown 已于 2026-10-02 从头至尾复读，并回核所有修改位置。本文件与对应提交仍是 contributor candidate，须由 Master-Luna 在 canonical target 上复核、集成后才能作为项目当前完成状态。
- 修复后 Markdown SHA-256：ad3fe1901ab87c9f71944726a0fd32fa7eae5040223387d388c7935363d8a79e。独立 fix(md) 候选链：88e02d2c3860ada1916a17e12aa6d5d4c8fe8d58 → 870e01c41593436f2fbc3d6f6c8a21a2457e5942 → d664399e914b228c1fa582b45e6693c5b79755f1 → 2cf4ee2c23fc895779681790c5707be91744f63b。
- 基线：`e04c4a9603818cfa2d71271942f696115783c33b`；本篇 PDF 与 MinerU Markdown 在该基线下均 tracked、clean。
- PDF：`Bourgain_1989_pointwise_ergodic.pdf`，38 页；PDF p.1 为 Numdam 题录/版权封面，PDF p.2–38 对应印刷页 5–41。
- PDF 来源身份：Jean Bourgain, “Pointwise ergodic theorems for arithmetic sets,” *Publications mathématiques de l'I.H.É.S.* 69 (1989), 5–41；封面链接 `PMIHES_1989__69__5_0`。
- Markdown：`Bourgain_1989_pointwise_ergodic_mineru/Bourgain_1989_pointwise_ergodic__Bourgain_1989_pointwise_ergodic.md`；基线 SHA-256 `0a583715b9fad224e16adc0cc9e5a40ea0edbd405948de28cbd9954352643d77`。
- PDF SHA-256：`7890c91e6a54e8867a262430b90f6af7f14a2a3558ac78e5dd56c789c044a9ef`。
- 模式判定：born-digital；`pdfinfo` 报告 `Producer: pdfTeX-1.40.16`、`Pages: 38`；`pdftotext -layout` 得 86,056 字节、0 个 U+FFFD、38 个 form-feed 分隔符。按文本层主对账，PDF 题录页及高密度公式页另做 150dpi PNG 视觉抽验；对文本提取不能裁决的字形回看 PDF 原图。
- MinerU 对应性：现有同名 Markdown 与 `middle_json.json`、`structured_content.json` 均在篇目录；两份 JSON 各有 38 页，producer 为 MinerU 3.4.4。此导出快照未发现显式 `doc_id` 字段。

## 逐页记录

## p.001（PDF p.1 / Numdam 题录封面，无印刷页码）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/Bourgain_1989_pointwise_ergodic_p001.png`（Ghostscript `pngmono`, 150dpi；原 PDF p.1）
- 核对：封面作者 Jean Bourgain、题名、期刊 *Publications mathématiques de l'I.H.É.S.*, tome 69 (1989), p. 5–41、Numdam 条目链接与版权/使用条款；与 PDF 文本层及 MinerU Markdown 开头逐项对照。
- 结果：PASS±。作者、题名、刊卷年页码、链接和版权条款均在 Markdown 开头保留；原页底部另有 “Article numérisé dans le cadre du programme / Numérisation de documents anciens mathématiques / http://www.numdam.org/” Numdam 制作说明，Markdown 未录。此为档案制作署名缺录，不影响论文题录或正文。
- 时间：2026-10-01 15:55:06 EDT

## p.002（PDF p.2 / 印刷 p.5 题名页；页码未印）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/Bourgain_1989_pointwise_ergodic_p002.png`（Ghostscript `pngmono`, 150dpi；原 PDF p.2）
- 核对：论文题名、作者与 appendix 合著者；§1 首段及公式 (1.1)，逐项对照 PDF 原图、PDF 文本层和 MinerU Markdown 对应段。
- 结果：PASS。题名、作者 Jean Bourgain、return-time appendix 合作者 H. Furstenberg、Y. Katznelson、D. S. Ornstein、首段前言与 (1.1) 的 $1/N$、$1\le n\le N$ 求和界及 $T^{p(n)}f$ 均相符。PDF 字体的 pdftotext 输出在专名和显示式处有编码/布局噪声，150dpi 原图已裁决；Markdown 保留了完整显示式，无需修复。
- 时间：2026-10-01 15:57:47 EDT

## p.003（PDF p.3 / 印刷 p.6）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p003_corollary.png`（从原 PDF p.3 以 300dpi 渲染后裁得）
- 核对：§1 后半段、圆周上的平方平均式 (1.2)、极大不等式 (1.3)、边界条件 $f\ge0$；逐项对照 PDF 300dpi 原图、文本层及 Markdown 对应段。
- 结果：PASS±。两式的 $1/N$、求和范围、$n^2\alpha$、$p$ 次方、积分上下限与右侧常数项均与原图一致。文本层将两式压平；300dpi 裁片裁决无 Markdown 错项。Markdown 未保留原页运行页眉 “JEAN BOURGAIN” 与印刷页码 6。源级排印用语 “Let $f$ be and $L^p$-function” 看似语法错误，但原图确为 “and”，Markdown 忠实保留；不修正文。
- 时间：2026-10-01 16:02:53 EDT

## p.004（PDF p.4 / 印刷 p.7）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p004_full.png`（Ghostscript `pnggray`, 300dpi；原 PDF p.4）；`audit/300dpi/Bourgain_1989_pointwise_ergodic_p004_theorem1.png` 为定理 1 局部证据。
- 核对：变差空间定义 (1.4)、指数和 (1.5)–(1.6)、定理 1 与不等式 (1.7)、后续 $L^1$ 说明；与 PDF 原图、PDF 文本层、MinerU 结构化页和 Markdown 对应段对照。
- 结果：FAIL。Markdown 的 (1.7) 把绝对值与上确界的分组次序错置；300dpi 原图为 $\|\sup_{\mathbf N}|A_{\mathbf N}f|\|_r\le C\|f\|_r$。同页把正等距映射的空间写成 `\mathbf{L}^{\prime}(\Omega,\mu)`；印刷为 `L^1(\Omega,\mu)`。两处均是 MinerU 记号误识，待全篇审完后按原图逐处手工修复。式 (1.4)–(1.6) 的上下标、求和界、指数和系数与原图一致。Markdown 未保留原页运行标题与印刷页码 7。
- 源级印刷 quirk：印刷文字确为 “we considerer the variation spaces”、定理 1 中 “by a dynamical system” 以及 “the limit if given by”；均已按 print 忠实保留，不据语法预期改写。
- 时间：2026-10-01 16:08:05 EDT

## p.005（PDF p.5 / 印刷 p.8）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p005_full.png`（Ghostscript `pnggray`, 300dpi；原 PDF p.5）
- 核对：定理 2 与式 (1.8) 的整部函数指数和平均范围；§1 摘要、目录 1–9 节页码与 appendix 引用；§2 开头及谱测度恒等式 (2.1)。与 PDF 原图、文本层和 MinerU Markdown 对应段逐项对照。
- 结果：PASS±。式 (1.8) 的 $[p(n)]$、$1\le n\le N$ 与 $T^{[p(n)]}f$，目录页码和附录合作者/文献号均吻合；(2.1) 的内积、$\widehat\nu(n)$、指数 $-2\pi i n\theta$ 及 $[0,1]$ 积分边界也与原图一致。PDF 文本层将公式压平，300dpi 原图已终裁。Markdown 未保留运行页眉 “JEAN BOURGAIN” 与印刷页码 8。
- 时间：2026-10-01 16:10:47 EDT

## p.006（PDF p.6 / 印刷 p.9）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p006_full.png`、`audit/300dpi/Bourgain_1989_pointwise_ergodic_p006_middle.png`、`audit/300dpi/Bourgain_1989_pointwise_ergodic_p006_maximal.png`（均由原 PDF p.6 以 300dpi 渲染/裁切）
- 核对：式 (2.2)、平方序列的无理/有理参数极限、§2B 定义与不等式 (2.3)–(2.4)；对照 PDF 原图、文本层及 Markdown。
- 结果：FAIL。Markdown (2.3)、(2.4) 的 MinerU 左右定界符次序损坏，无法忠实表示原页的双范数不等式；300dpi 裁片显示应为 $\|f^*\|_{L^p(\Omega,\mu)}\le C(p)\|f\|_{L^p(\Omega,\mu)}$ 与 $\|f^*\|_{L^{1,\infty}(\Omega,\mu)}\le C\|f\|_{L^1(\Omega,\mu)}$，待全篇审完后逐处手修。其余式 (2.2) 的归一化、求和条件和 $z^n$ 与原图相符。
- PASS± 记录：Gauss 和式在 Markdown 写作 $e^{2\pi i\alpha r^2}$，印刷写 $e^{2\pi i a r^2/q}$；同段已给 $\alpha=a/q$，两写法等价，故不按内容错误修复。印刷把式 (2.2) 的叙述引用写成 “(4)”，原样保留；页面运行页眉与印刷页码 9 未进入 Markdown。
- 源级版式疑点：§2B 平均符号的印刷下标看作 $A_n$，而显示和式使用 $N$；Markdown 忠实记录可见字形，原图证据保留供复核。
- 时间：2026-10-01 16:18:13 EDT

## p.007（PDF p.7 / 印刷 p.10）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p007_full.png` 与 `audit/300dpi/Bourgain_1989_pointwise_ergodic_p007_inequalities.png`（原 PDF p.7，300dpi）
- 核对：受限极大函数 (2.5)、轨道与截断函数 (2.6)、区间等式 (2.7)、由移位模型推出的 $L^p$ 估计 (2.8) 及弱型集合计数式；逐项对照 PDF 原图、文本层和 Markdown。
- 结果：FAIL（全文复读时发现并已修复）。PDF p.7 的 (2.8) 推导中两个范数下标、对应幂次及 $C(p)$ 的幂次均为普通斜体 $p$；Markdown 曾将这两处写成 Fraktur $\mathfrak{p}$，已按原页恢复。其余范围端点、$J-\bar N$、常数及轨道项与原图一致。初始 page commit 的 PASS± 为历史收据；本条根据原页证据更正当前审计判断。Markdown 未保留原页页眉与印刷页码 10。印刷原样出现 “in the some way” 和限制条件 “$f\le0$”；Markdown 忠实保留，未按语法或预期符号更改。
- 时间：2026-10-01 16:23:01 EDT

## p.008（PDF p.8 / 印刷 p.11）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p008_full.png` 与 `audit/300dpi/Bourgain_1989_pointwise_ergodic_p008_convergence.png`（原 PDF p.8，300dpi）
- 核对：弱型估计 (2.9) 与其积分后界；§2C 几乎处处收敛论证、不等式 (2.10)、上极限结论和一般子集平均 (2.11)；正文关于 $L^2/L^p$ 结果的概括。
- 结果：FAIL。印刷写 “The $L^2$ and $L^p$-inequalities ($p>1$)”，Markdown 将第二个空间误写为 $L^2$。另 (2.10) 及紧随其后的上极限 $L^2$ 界在 Markdown 中错置范数/绝对值/上确界的定界符；300dpi 原图显示分别为 $\|\sup_N |F-A_N(A_{N_\varepsilon}f)|\|_2<C\varepsilon$ 和 $\|\overline{\lim}|F-A_N f|\|_2<C\varepsilon$，待全篇审完后按原图逐处修复。式 (2.9)、(2.11) 的求和集合、归一化与变换指数相符。
- 源级文字 quirk：原页写 “the ergodic means relates to the full set of positive integers”，Markdown 忠实保留。运行页眉和印刷页码 11 未录。
- 时间：2026-10-01 16:24:52 EDT

## p.009（PDF p.9 / 印刷 p.12）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p009_full.png` 与 `audit/300dpi/Bourgain_1989_pointwise_ergodic_p009_variations.png`（原 PDF p.9，300dpi）
- 核对：§2 收尾的子序列极大不等式 (2.12)–(2.14)，§3 变差范数定义 (3.1)–(3.2)；对照 PDF 原图、文本层及 Markdown。
- 结果：FAIL。定义 (3.2) 的 Markdown 把求和上界写成 `s`；印刷原页与相邻离散定义 (3.1) 一致，均为 $J$。该 OCR 上界误认需在全篇审完后手工修复。式 (2.12)–(2.14) 的稀疏尺度、索引范围和 $o(J)$ 项与原图相符。
- 源级索引 quirk：原页 (3.1)、(3.2) 的条件只列到 $n_J/t_J$，求和差分却出现 $n_{j+1}/t_{j+1}$；Markdown 忠实保留，不擅自把 print 改成 $J-1$ 或补一个索引。页面页眉与印刷页码 12 未录。
- 时间：2026-10-01 16:28:21 EDT

## p.010（PDF p.10 / 印刷 p.13）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p010_full.png`（原 PDF p.10，300dpi）
- 核对：Lemma 3.3 与不等式 (3.4)–(3.8)，Fourier 变换定义 (3.9)–(3.10)；与 PDF 原图、文本层及 Markdown 对应段对照。
- 结果：FAIL。Markdown 的 Lorentz 空间说明把普通斜体 $p$ 误成 Fraktur $\mathfrak{p}$；式 (3.7) 中序列集合的右侧定界符误为竖线，且 (3.7)、(3.8) 的跳跃计数下标把 $2^{-k}$ 误录为 $2-k$。三类差异均已按 PDF 原图逐处恢复。其余参数范围和 Fourier 核心指数与原图相符。Markdown 未保留原页运行标题与印刷页码 13。
- 时间：2026-10-01 16:30:09 EDT

## p.011（PDF p.11 / 印刷 p.14）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p011_full.png`（原 PDF p.11，300dpi）
- 核对：Lemma 3.11 及估计 (3.12)–(3.20)，重点核对 Poisson 半群 Fourier 乘子、$K=\chi-P_1$、频率分块与 $2^{-|\alpha|}$ 衰减。
- 结果：FAIL。Markdown 把 Poisson 半群乘子写成 $e^{-i|\lambda|}$；300dpi 原页明确为 $\widehat P_t(\lambda)=e^{-t|\lambda|}$，误把尺度参数 $t$ 识别成虚数单位 $i$。此差异改变半群乘子，待全篇审完后手工修复。其余式 (3.12)–(3.20) 的主要范围、指数和频率条件与原页相符。Markdown 未保留原页运行页眉与印刷页码 14。
- 时间：2026-10-01 16:31:30 EDT

## p.012（PDF p.12 / 印刷 p.15）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p012_full.png` 与 `audit/300dpi/Bourgain_1989_pointwise_ergodic_p012_corollary.png`（原 PDF p.12，300dpi）
- 核对：估计 (3.21)–(3.24)、$N_\alpha=2^{|\alpha|}$ 的选择、求和后界及 Corollary 3.25 / (3.26)；逐项对照原图、PDF 文本层与 Markdown。
- 结果：PASS±。级数权重、频率环带 $|\lambda|\sim2^{-k-\alpha}$、网格增量、$N_\alpha$ 选择和 (3.26) 的 $n\le N$ 均与原页相符。Corollary 3.25 的印刷字形为 K 形书写符号，Markdown 以粗体 K 表示，记为字形风格差异。PDF 文本层在公式处大幅失真，已由 300dpi 页图裁决。
- 源级文字 quirk：原页拼作 “chosing $N_\alpha=2^{|\alpha|}$”，Markdown 忠实保留。Markdown 未保留运行页眉与印刷页码 15。
- 时间：2026-10-01 16:34:25 EDT

## p.013（PDF p.13 / 印刷 p.16）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p013_full.png`（原 PDF p.13，300dpi）
- 核对：表示式 (3.27)、Lemma 3.28 / (3.29)、熵数界 Lemma 3.30 / (3.31)–(3.32)、Lemma 3.33 / (3.34) 与其证明开头；与 PDF 原图、文本层和 Markdown 对应段逐项比对。
- 结果：PASS±。$\chi_t=t^{-1}\chi_{[0,t]}$、$\varphi'(t)t$ 权重、$M_\lambda^{1/s}$、$\log K$ 因子及 Hilbert 空间范数与原图相符，未发现 Markdown 内容偏差。文本提取公式较多扁平化，已由 300dpi 原页裁决。Markdown 未保留原页运行页眉与印刷页码 16。
- 时间：2026-10-01 16:36:18 EDT

## p.014（PDF p.14 / 印刷 p.17）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p014_full.png`（原 PDF p.14，300dpi）
- 核对：Lemma 3.33 证明中的 (3.35)–(3.36) 与积分界收束；§4 开头及 Lemma 4.1 的条件、邻域 $R_j$、估计 (4.3) 和文字说明。
- 结果：PASS±。公式中的 $f_\alpha^*$、$F$、$K^{-1/s}F(x)$ 端点、$1/2-1/s=(\log K)^{-1}$、频率邻域 $2^{-j}$ 和 $(\log K)^2$ 常数均与 300dpi 原图相符。部分 $K$ 在 Markdown 用粗体字形表示，印刷为常规数学大写体；仅属字体差异。全文结构/页眉未保留，未见内容丢失。
- 时间：2026-10-01 16:37:48 EDT

## p.015（PDF p.15 / 印刷 p.18）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p015_full.png`（原 PDF p.15，300dpi）
- 核对：Lemma 4.4 的 (4.5)–(4.6) 及证明 (4.7)–(4.10)；Lemma 4.11、Lemma 4.13 与估计 (4.14)，逐项对照 PDF 原图、文本层、MinerU JSON 和 Markdown。
- 结果：FAIL。(4.5) 印刷为 $L^2(\mathbf R)$ 乘子极大不等式，Markdown 把标签独立留在前一行，却把显示式的 tag 误录为 `Then`；印刷在 (4.5) 公式后另有正文 “Then”，再引出 (4.6)。因此 (4.5) 的公式归属和过渡文字在 Markdown 中均错位，待全篇审完后用 Edit 逐处复原。(4.6)、(4.14) 的函数、参数和常数项核对相符。Markdown 未保留原页运行页眉与印刷页码 18。
- 时间：2026-10-01 16:40:39 EDT

## p.016（PDF p.16 / 印刷 p.19）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p016_full.png`（原 PDF p.16，300dpi）
- 核对：Lemma 4.13 证明的三角和估计 (4.15)–(4.20)；覆盖集合分解 (4.21)–(4.23)，逐式对照 PDF 原图与 Markdown。
- 结果：FAIL。式 (4.15) 的印刷范数为 $L^2[0,\tau^{-1}]$、平方和上界为 $K$；Markdown 曾录为 $L^3$ 且上界为小写 $k$。(4.17) 的 $1/100$ 分母还被拆成 `1 0 0`；该式亦已恢复。另 (4.21) 印刷对应 $|\bar b|\le2\cdot2^s$，(4.22) 对应 $\#B_s\le M_{2^s}$；Markdown 将首个标签留作独立文本、把后一个标签挂到了 (4.21) 公式，并使计数界失去原页编号。上述位置均在全篇审毕后按原图逐处修复。
- Markdown 未保留原页运行标题与印刷页码 19。
- 时间：2026-10-01 16:42:04 EDT

## p.017（PDF p.17 / 印刷 p.20）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p017_full.png`（原 PDF p.17，300dpi）
- 核对：熵分解估计 (4.24)–(4.25)、Lemma 4.26 / (4.27)、平方函数分解 (4.28)–(4.31)；按 PDF 原图检查区间范数与系数。
- 结果：FAIL。(4.24) 的区间范数在印刷中是 $L^2([0,\tau^{-1}],du)$；Markdown 错识为 $L^3$。其余 (4.25)–(4.31) 的主系数、频率项和求和范围与原图相符，待全篇审毕后单独修正该范数。
- 时间：2026-10-01 16:43:58 EDT

## p.018（PDF p.18 / 印刷 p.21）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p018_full.png`（原 PDF p.18，300dpi）；`audit/Bourgain_1989_pointwise_ergodic_p018_mineru_tree.jpg`（MinerU Markdown 所引用 tree 图的本篇审计副本）
- 核对：Lemma 4.32 的 $R_j$ 定义、有限集合 $S$ 的极大不等式 (4.33)、双重化估计 (4.34)，以及 Markdown 内嵌二叉/diadic 分割图；与 PDF 原图、导出 Markdown 和所引用 MinerU 图像对照。
- 结果：FAIL。原页先给 $R_j$ 定义，随后 “Then” 引出编号 (4.33) 的极大不等式；Markdown 将 “Then” 放到定义之前，把 (4.33) 标给 $R_j$ 定义，并让真正的极大不等式无编号。全篇审完后需手工调整该处段落顺序和标签。PDF p.18 的分割树与 Markdown 引用的 `images/page_17_image_16.jpg` 四个叶结点/标签吻合；其本篇审计副本哈希与 MinerU 源图一致。
- Markdown 未保留原页运行页眉与印刷页码 21。
- 时间：2026-10-01 16:46:33 EDT

## p.019（PDF p.19 / 印刷 p.22）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p019_full.png`（原 PDF p.19，300dpi）
- 核对：内积与分块求和、(4.36)–(4.39) 的尺度集合/分离集/邻域包络及后续双对偶估计开头；与 PDF 原图、文本层及 Markdown 比较。
- 结果：FAIL。(4.38)–(4.39) 标签发生错位：原页 (4.38) 标注 $|\lambda-\lambda'|>2^{-j_r}$ 的分离条件，(4.39) 标注 $\Lambda_r$ 邻域并集对 $R_j$ 的内外包络；Markdown 将 (4.38) 留成孤立文本，把 (4.39) 挂到分离条件上，并使包络式无原页标签。全篇审完后按原页逐处恢复标签。
- Markdown 未保留原页运行页眉与印刷页码 22。
- 时间：2026-10-01 16:47:49 EDT

## p.020（PDF p.20 / 印刷 p.23）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p020_full.png`（原 PDF p.20，300dpi）
- 核对：结束 Lemma 4.12 的估计 (4.40)–(4.41)；§5 开头、指数和定义 (5.1)–(5.2)、Weyl 引理 (5.4)、major box (5.5) 和离箱界 (5.7)。与 PDF 原图、文本层及 Markdown 对照。
- 结果：FAIL。印刷 (4.41) 左侧是 $L^2$ 范数 $\|\sup_{j\in Z_r}|\mathcal F^{-1}[\chi_{R_j}\mathcal F f]|\|_2$；Markdown 的开左范数符号缺失/错置，不能正确包围上确界及绝对值，待全篇审后修复。Weyl 指数 $\rho=2^{-(d-1)}$、误差幂与 major-box 宽度其余均与原图相符。
- 源级文字 quirk：原页印 “The same argument as in (4.32) than shows that”，Markdown 保留 “than”；运行页眉与印刷页码 23 未录。
- 时间：2026-10-01 16:49:53 EDT

## p.021（PDF p.21 / 印刷 p.24）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p021_full.png`（原 PDF p.21，300dpi）
- 核对：major-box 近似 (5.8)–(5.16)、Gauss sum / continuous integral 定义及 Lemma 5.17 两个振荡积分估计；与 PDF 原图、文本层和 Markdown 对照。
- 结果：FAIL。Lemma 5.17 的 (5.18)、(5.19) 标签在 Markdown 错位：`(5.18)` 孤立，首个 $|1-V_N(\bar\beta)|$ 估计被标成 (5.19)，第二个 $|V_N(\bar\beta)|$ 界无编号；原页编号与两个不等式一一对应相反。式 (5.8)–(5.16) 的有理盒条件、指数和及误差阶与原图相符。原页作者名为 “A. Weil”，Markdown 也相符。
- Markdown 未保留原页运行页眉与印刷页码 24。
- 时间：2026-10-01 16:54:06 EDT

## p.022（PDF p.22 / 印刷 p.25）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p022_full.png`（原 PDF p.22，300dpi）
- 核对：§6 起始多项式平均 (6.1)–(6.6)、平滑截断定义 (6.7)、S / $w_N$ 记号 (6.8)–(6.9)、逼近式 (6.10) 与有理权重界 (6.11)。
- 结果：FAIL。三项 OCR 偏差：标签 (6.1)/(6.2) 错位（平均式误挂 (6.2)，多项式式失去 (6.2)）；(6.7) 的尺度 $10^s$ 在 Markdown 中被字距拆为 `1 0^s`；(6.8)/(6.9) 标签也错位（$S(\theta)$ 的定义误挂 (6.9)，$w_N$ 定义无编号）。300dpi 原图确认了全部应有顺序，待全篇审毕后逐条修复。
- 源级语句 quirk：印刷原文确为 “where reduced to proving certain inequalities…”，Markdown 忠实保留，不按语法预期补写主语。运行页眉与印刷页码 25 未录。
- 时间：2026-10-01 16:57:20 EDT

## p.023（PDF p.23 / 印刷 p.26）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p023_full.png`（原 PDF p.23，300dpi）
- 核对：由 $w_N$ 得到的界 (6.12)–(6.13)、乘子逼近 Lemma 6.14 / (6.15)、major-arc 两种情形与误差界 (6.16)–(6.18)。
- 结果：FAIL。与上一页相同的连续编号偏移出现在 (6.12)/(6.13)：原页 (6.12) 是 $|1-w_N(\beta)|$ 界、(6.13) 是 $|w_N(\beta)|$ 界；Markdown 把 (6.12) 独立留行、将 (6.13) 挂到第一个不等式，并使第二个界无编号。另 (6.17) 的截断函数自变量在 Markdown 中写作 `1 0^{s_0}(\alpha-\theta_0)`，原图为 $10^{s_0}(\alpha-\theta_0)$；空格拆开数字会改变该参数，待全篇审后修复。
- Markdown 未保留原页运行页眉与印刷页码 26。
- 时间：2026-10-01 16:59:35 EDT

## p.024（PDF p.24 / 印刷 p.27）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p024_full.png`（原 PDF p.24，300dpi）
- 核对：Lemma 6.14 的 Case 2 收尾、极大不等式 (6.19)–(6.21)、截断乘子定义 (6.22)–(6.23)、主导比较 (6.24)–(6.28)。
- 结果：FAIL。(6.19) 印刷为 $L^2(\mathbf Z)$ 范数 $\|\sup_N|f*K_N|\|_2$，Markdown 少了左侧一条范数竖线。 (6.22) 的截断宽度印刷为 $\zeta(10^s(\alpha-\theta))$，Markdown 把 `10` 拆成 `1 0`。另 (6.25)–(6.26) 标签错位：印刷 (6.25) 属于 $\mathcal F[g_s]$ 定义，(6.26) 属于 $\widetilde\psi_{s,N}\mathcal Ff=\mathcal F[g_s]\chi_{R_j}$；Markdown 把 (6.25) 留在独立行、把 (6.26) 标到前一个公式，后一个无编号。三项待全篇审后单独修复。
- Markdown 未保留原页运行页眉与印刷页码 27。
- 时间：2026-10-01 17:02:21 EDT

## p.025（PDF p.25 / 印刷 p.28）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p025_full.png`（原 PDF p.25，300dpi）
- 核对：$L^2$ 极大估计 (6.29)–(6.30)、稀疏子序列和条件 (6.31)–(6.32)、误差界 (6.33)、替代定义 (6.34)–(6.35) 与变差控制 (6.36)。
- 结果：FAIL。印刷 (6.30) 是 $\|\sup_N|A_N f|\|_2\le C\|f\|_2$；Markdown 该式在上确界前缺少外范数左竖线，未忠实表达 $L^2$ 范数。300dpi 原页确认，待全篇审完后修复。其他求和范围、$N_j$ 间隔、$J^{1/4}$ 因子与原图相符。
- 源级文字 quirk：原页写 “is follows from (6.36) and (3.26)”，Markdown 忠实保留。运行页眉及印刷页码 28 未录。
- 时间：2026-10-01 17:04:17 EDT

## p.026（PDF p.26 / 印刷 p.29）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p026_full.png`（原 PDF p.26，300dpi）
- 核对：Theorem 1 的 maximal / a.s. 收尾、不等式 (6.37)–(6.40)，弱混合结论及 §7 开头的 (7.1)–(7.3)。
- 结果：PASS±。$\hat\chi(N^d\alpha)$ 误差项、$J^{1/2}$、$J^{3/4}$ 因子和 $z^{p(n)}$ 的弱混合极限与 300dpi 原图及 Markdown 相符。原页印字 “goods bounds on $L^p$” 按 print 原样保留；Markdown 未录运行页眉与印刷页码 29。
- 时间：2026-10-01 17:06:16 EDT

## p.027（PDF p.27 / 印刷 p.30）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p027_full.png`（原 PDF p.27，300dpi）；`audit/600dpi/Bourgain_1989_pointwise_ergodic_p027_full.png` 与 `audit/600dpi/Bourgain_1989_pointwise_ergodic_p027_7_8_7_9_detail.png`（(7.8)–(7.9) 的高分辨率原页/裁片复核）。
- 核对：Lemma 7.4 的 $L^p/\ell^p$ 比较与证明 (7.5)–(7.9)，Lemma 7.10 的和式 (7.11)–(7.12)。
- 结果：FAIL。正文把 $L^p(\mathbb R)$、$\ell^p(\mathbb Z)$ 误录为 $L^\nu$、$\ell^\nu$；已恢复为普通 $p$。高分辨率 PDF p.27 原页确认 (7.8) 中首两项的范数对象在印刷本本身留空，Markdown 保留该源级缺项，不补写推测公式。(7.9) 左侧两处指数应为 $q$ 而非 $\alpha$，右侧积分号在 Markdown 缺失；均已依原页补正。和式 (7.11) 的上界在印刷本确为 $a\leq q$，虽含端点，按 print 忠实保留。
- Markdown 未保留原页运行页眉与印刷页码 30。
- 时间：2026-10-01 17:08:16 EDT

## p.028（PDF p.28 / 印刷 p.31）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p028_full.png`（原 PDF p.28，300dpi）
- 核对：Lemma 7.10–7.13 的 Fourier 系数/积分估计 (7.11)–(7.15)，实变量 maximal inequality (7.17)–(7.19)。
- 结果：FAIL。式 (7.18) 印刷截断区间为 $[0,N^d]$，Markdown 写为 $[0,Nd]$，丢失了幂次；(7.18) 与 (7.19) 的 $L^p$ 范数索引在 Markdown 误写成 `\mathcal{P}`，四处都需逐位恢复为 $p$。300dpi 原页确认。源级端点 quirk：Lemma 7.10 的 (7.11) 印作 $0\le a\le q$，紧接证明按 $0\le a<q$ 求和；两处均忠实保留。Markdown 未录页眉与印刷页码 31。
- 时间：2026-10-01 17:12:55 EDT

## p.029（PDF p.29 / 印刷 p.32）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p029_full.png`；`audit/300dpi/Bourgain_1989_pointwise_ergodic_p029_upper.png`；`audit/300dpi/Bourgain_1989_pointwise_ergodic_p029_lower.png`（原 PDF p.29，300dpi）
- 核对：born-digital 文本层逐式核对 Lemma 7.20 与其证明 (7.21)–(7.28)，并用原页 300dpi 图裁决范数和绝对值竖线结构、求和/积分边界及指数项。
- 结果：FAIL。(7.22) 的序列范数中 `sup_N`、积分绝对值与外层 $\ell^p$ 范数在 Markdown 的竖线配对/层次错乱；(7.24) 左侧极大表达式与右侧积分范数的竖线结构也未对应印刷的 $\ell^p$ 范数；(7.26) 第一项 $q^{-1/p}\|\sup_N|\mathcal F^{-1}[w_NF\zeta(D\cdot)]|\|_{L^p}$ 的内外范数分隔符错乱。需逐处按原页恢复。其余 (7.21)、(7.23)、(7.25)、(7.27)、(7.28) 的主要项、条件和编号与原图相符。源级 quirk：印刷 (7.26) 第二个比较项确实写作 $e^{2\pi i qy}$，少于前一积分中的 $e^{2\pi i\beta qy}$；正文 “Apply consecutively (7.5), (7.6, (7.5)” 的括号也如印刷缺失。Markdown 均忠实保留，不能擅改。Markdown 未录运行页眉 “JEAN BOURGAIN” 与印刷页码 32。
- 时间：2026-10-01 17:25:05 EDT

## p.030（PDF p.30 / 印刷 p.33）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p030_full.png`（原 PDF p.30，300dpi）
- 核对：Lemma 7.29 的估计 (7.30)–(7.31)，Lemma 7.32 的受限极大不等式 (7.33) 及有限循环群改写 (7.34)–(7.35)；逐式核对范数、幂次、区间和编号。
- 结果：FAIL。(7.30) 的 $\ell^p$ 范数竖线分组在 Markdown 中错乱；(7.33) 的 $\ell^p$ 范数下标被误录为 `\mathfrak{p}`；(7.34) 的核 $K_{2^k}$ 被误录为 $K_{2k}$，丢失指数。待全篇审毕后按原图逐处修复。其余 (7.31)、(7.35)、求和区间与群记号在原图和 Markdown 中相符。源级 quirk：印刷原文写 “The following lemma in an important new ingredient in proving (7.1)”；Markdown 忠实保留语法异常，不改写。Markdown 未录页眉 “POINT-WISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 33。
- 时间：2026-10-01 17:29:16 EDT

## p.031（PDF p.31 / 印刷 p.34）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p031_full.png`（原 PDF p.31，300dpi）
- 核对：对偶估计 (7.36)–(7.39)，展开 $q$ 次幂得到的 (7.40)–(7.41)，乘积卷积逼近 (7.42) 及代入估计 (7.43)；与 300dpi 原页核对变量、编号、范数和区间。
- 结果：FAIL。印刷定义 $L_k=K_{2^{Mk}}$，Markdown 将 $M$ 误成 $u$；(7.40)–(7.41) 的公式/标签错位，Markdown 把 (7.40) 留成空编号、把首个展开估计挂在 (7.41)，并使其后的加项无标签；(7.42) 的 $L^2(G)$ 范数少一条左侧竖线。以上需全篇审毕后依原图修复。(7.36)–(7.39) 的对偶条件、常数依赖与主区间，及 (7.43) 的积分项和求和范围与印刷相符。Markdown 未录运行页眉 “JEAN BOURGAIN” 与印刷页码 34。
- 时间：2026-10-01 17:44:07 EDT

## p.032（PDF p.32 / 印刷 p.35）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p032_full.png`（原 PDF p.32，300dpi）
- 核对：证明 (7.42) 的 Fourier 截断定义 (7.44)–(7.48)、频谱支撑及误差分解 (7.49)–(7.50)、逐因子估计 (7.51)–(7.53)；重点核对尺度、求和下标、标签与常数。
- 结果：FAIL。(7.44) 的尺度 $10^s$ 在 Markdown 拆成 `1 0^s`；(7.49)–(7.50) 标签错位：原页 (7.49) 是逐因子的误差和，(7.50) 是乘积与 $L_{k_1}-L_{k_0}$ 的卷积项，Markdown 将乘积的末个逐因子误差挂为 (7.50)，而真正的卷积项无编号；两处表达式也有分隔符/闭合符损坏。(7.51) 指数起始项应为 $s_2$，Markdown 写成 $s_3$；(7.52) 的 $1/10$ 被拆为 `1 0`。待全文审毕后逐处照原页修复。(7.45)–(7.48) 的误差阶、$4^{s_r}$ 界及 $L^2(G)$ 目标范数，以及 (7.53) 的支撑集上确界结构与原页相符。Markdown 未录页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 35。
- 时间：2026-10-01 18:01:33 EDT

## p.033（PDF p.33 / 印刷 p.36）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p033_full.png`（原 PDF p.33，300dpi）
- 核对：估计 (7.54)–(7.56) 与 Lemma 7.32 收尾；§7 证明 (7.2) 的定义 (7.57)–(7.59)、乘子逼近 (7.60)–(7.61) 和极大范数界 (7.62)。
- 结果：FAIL。合并估计的 $1/10$ 在 Markdown 拆为 `1 0`，且两处 $k_0^{-q}$ 被录成 $k_0^{-a}$；(7.57)/(7.58) 标签错位：原页 (7.57) 标 $Q_s=2^s!$、(7.58) 标 $\mathcal K_s$ 定义，Markdown 把 (7.57) 留空、将 (7.58) 挂在 $Q_s$ 上并使集合定义无编号；(7.59)、(7.60) 中 $2^k$ 的幂次分别在 $w_{2^k}$、$K_{2^k}$ 丢失；(7.62) 的极大算子 $p_0$ 范数竖线层次损坏。证明 (7.2) 的分解式中，$f*K_{2^k}$ 在首项与末项均失去指数，也已恢复。以上均依 PDF 原图逐处修复。(7.54)–(7.56) 的误差项与尺度相符。源级 quirk：印刷用语 “the left number of (7.42)” 在 Markdown 中忠实保留。Markdown 未录运行页眉 “JEAN BOURGAIN” 与印刷页码 36。
- 时间：2026-10-01 18:27:18 EDT

## p.034（PDF p.34 / 印刷 p.37）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p034_full.png`（原 PDF p.34，300dpi）；`audit/300dpi/Bourgain_1989_pointwise_ergodic_p034_7_63_7_65_detail.png`（(7.63)–(7.65) 标签、阈值和下标裁片）。
- 核对：极大函数分解 (7.63)–(7.66)、乘子差分分解 (7.67)–(7.68)、高频估计 (7.69) 与插值前的 $L^2$ 界 (7.70)–(7.71)。
- 结果：FAIL。(7.63) 的标签未连到公式，Markdown 将 “By (7.62)” 错并成公式 tag；该式 $K_{2^k}$ 两处指数均丢失，阈值 $4^{s'}$ 拆成 $4s'$，且分块集 $\mathcal{K}_s$ 被录作 $\mathcal{X}_s$；已恢复并把 “By (7.62)” 放回 (7.64) 前。(7.64) 的极大范数竖线分组损坏。(7.65)–(7.66) 与 (7.70)–(7.71) 的范数/内层绝对值竖线层次损坏；(7.65) 的 $p_0$ 范数另误录为 Fraktur $\mathfrak{p}_0$；(7.66) 的 $K_{2^k}$ 与 $\psi_{r,2^k}$ 指数丢失；均已依原页恢复。(7.67)/(7.68) 标签错位，且两处乘子 $w_{2^k}$ 指数遗失及 (7.68) 起始加号缺失，已恢复；(7.69) 的 $w_{2^k}$ 指数与 (7.71) 的 $K_{2^k}$、$\Omega_{k,s}$ 逗号也已更正。Markdown 未录页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 37。
- 时间：2026-10-01 18:56:56 EDT

## p.035（PDF p.35 / 印刷 p.38）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p035_full.png`；`audit/300dpi/Bourgain_1989_pointwise_ergodic_p035_middle.png`（原 PDF p.35，300dpi）；另核对 Markdown 所引 `images/page_34_image_14.jpg` 与原页示意图。
- 核对：§7 插值结论及 §8 开头的整数部分多项式平均 (8.1)–(8.3)，系数条件、整数分解、uniform distribution 句、图像与平滑平均定义。
- 结果：FAIL。§7 收尾的极大平均核在印刷中为 $K_{2^k}$，Markdown 写成 $K_{2k}$，丢失指数。其余 (8.1)–(8.3) 的公式与所引梯形函数图均与原图相符。源级 quirks：原文明确写系数分母条件 $(1\le j\le q)$，尽管此前多项式次数记为 $d$；又写 “Fix $\varepsilon<0$”，而同页图将 $\varepsilon$ 置于 $(0,1)$ 内、下一页文字将其取为正。PDF 原页证实这些文字确实如此，Markdown 忠实保留，不自行改正。Markdown 未录运行页眉 “JEAN BOURGAIN” 与印刷页码 38。
- 时间：2026-10-01 19:49:09 EDT

## p.036（PDF p.36 / 印刷 p.39）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/Bourgain_1989_pointwise_ergodic_p036.png`（150dpi）；`audit/300dpi/Bourgain_1989_pointwise_ergodic_p036_full.png`（300dpi）。
- 核对：整数部分平均的点态误差 (8.4)、核的 Fourier 表示 (8.5)–(8.8)、有理共振集 (8.9)、$S(\theta)$ 与 $w_N$ 定义 (8.10)–(8.11)、乘子定义 (8.12)–(8.13)。
- 结果：FAIL。(8.9) 在原页由共振同余条件、$(q,a_1,\dots,a_d)=1$ 与 $2^s\le q\le2^{s+1}$ 共同定义 $\mathcal R_{s,k}$；Markdown 将标签放在第一行后，把后两项拆出公式，未完整绑定定义。(8.12)/(8.13) 标签移位：Markdown 将 (8.12) 留为空行、把 $\psi_{s,k,N}$ 定义误标为 (8.13)，而 $\psi_{s,N}$ 求和式无标签；且 (8.12) 中 $10^s$ 被拆成 `1 0^s`。其余 (8.4)–(8.8)、(8.10)–(8.11) 的系数、指数、范围和公式与原页相符。Markdown 未录页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS” 与印刷页码 39。
- 时间：2026-10-01 20:08:26 EDT

## p.037（PDF p.37 / 印刷 p.40）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p037_full.png`（原 PDF p.37，300dpi）
- 核对：整数部分平均极大估计 (8.14)–(8.16)、Theorem 2 收尾及 Remark；§9 素数平均和 Fourier 渐近式 (9.1)–(9.3) 与参数范围。
- 结果：FAIL。(8.15) 印刷为 $\|\sup_{N\in\mathbf Z_1}|\mathcal F^{-1}[\psi_{s,k,N}\mathcal Ff]|\|_2$；Markdown 的范数/绝对值竖线配对错乱，缺少对 Fourier 逆变换项的内层绝对值边界。需按原页修复。(8.14)、(8.16)、(9.1)–(9.3) 的编号、主要项及渐近误差与原图相符。Markdown 未录运行页眉 “JEAN BOURGAIN” 与印刷页码 40。
- 时间：2026-10-01 20:35:39 EDT

## p.038（PDF p.38 / 印刷 p.41）
- actor=Peer-P04; model=gpt-6-luna; effort=max
- PNG：`audit/300dpi/Bourgain_1989_pointwise_ergodic_p038_full.png`（原 PDF p.38，300dpi）
- 核对：§9 末三条评论、素数平均定理后续讨论、正等距算子推广与熵数必要条件 (9.4)，以及结尾说明文字。
- 结果：PASS±。所核正文、公式 (9.4)、不等式方向、索引集合和引文标记与印刷原页相符；Markdown 未录运行页眉 “POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS”、印刷页码 41 及右下角孤立页边数字 6，均属版面信息遗漏。源级 quirk：原文结尾写 “the previous criterion if often effective”，Markdown 忠实保留该印刷用词。
- 时间：2026-10-01 20:46:54 EDT

## 总体验收与修复后复核

- 38/38 个 PDF 页均有独立页级记录与可追溯 PDF 图像证据；其中 29 页含 MinerU 转录/编号差异并在审毕后修复，其他页的 PASS/PASS± 依据见对应页记录。
- 页级记录中的 PASS/PASS±/FAIL 保留首轮逐页比对判断；P7 在修复后全篇复读中发现额外的普通斜体 $p$ → Fraktur $\mathfrak p$ 误识，因此将当前页记录由历史 page-commit 的 PASS± 更正为 FAIL。没有改写已有提交历史；此记录说明修正依据。
- 修复前 Markdown SHA-256 为 0a583715b9fad224e16adc0cc9e5a40ea0edbd405948de28cbd9954352643d77；修复后为 ad3fe1901ab87c9f71944726a0fd32fa7eae5040223387d388c7935363d8a79e。修复后全文共 2,028 行，2026-10-02 从头至尾复读；修复项逐项回核对应 PDF 页原图，P27 的 (7.8)–(7.9) 使用 600dpi 原页/裁片，P34 的 (7.63)–(7.65) 下标、阈值和标签使用独立局部裁片。
- 手工修改均位于独立 fix(md) 提交链：88e02d2c3860ada1916a17e12aa6d5d4c8fe8d58（首批逐处修复）、870e01c41593436f2fbc3d6f6c8a21a2457e5942（全文复读后补正 P10 式 (3.8) 的 $2^{-k}$）、d664399e914b228c1fa582b45e6693c5b79755f1（全文复读后补正 P15 的 (4.5)/Then 顺序）、2cf4ee2c23fc895779681790c5707be91744f63b（全文复读后补正 P7 的 $p$ 范数指数）。actor 均为 Peer-P04，model/effort 均为 gpt-6-luna/max；Git author 沿用真实环境配置。

### 逐页修复登记

- PDF p.4：恢复 (1.7) 的外层 $L^r$ 范数与内层绝对值/上确界分组；L′ 误识恢复为印刷的 $L^1$。
- PDF p.6：重排 (2.3)、(2.4) 的双范数定界符。
- PDF p.7：将积分后不等式及其范数中的两处 Fraktur $\mathfrak p$ 恢复为普通 $p$。
- PDF p.8：将“The $L^2$ and $L^2$”第二项恢复为 $L^p$；修正 (2.10) 与上极限界的范数、绝对值和定界符，同时保留原页首个 $\overline{\lim}$ 无下标这一字形。
- PDF p.9：将 (3.2) 的求和上界从 $s$ 恢复为 $J$。
- PDF p.10：恢复 Lorentz 空间中的普通 $p$、(3.7) 的闭右花括号，以及 (3.7)、(3.8) 跳跃计数下标 $N_{2^{-k}}$。
- PDF p.11：将 Poisson 半群乘子 $e^{-i|\lambda|}$ 恢复为 $e^{-t|\lambda|}$。
- PDF p.15：恢复 (4.5) 标签，并把印刷正文 “Then” 放回 (4.5) 与 (4.6) 之间。
- PDF p.16：恢复 (4.15) 的 $L^2$ 范数与上界 $K$；(4.17) 的 $1/100$；(4.21)、(4.22) 标签；(4.24) 的 $L^2([0,\tau^{-1}],du)$ 范数。
- PDF p.17：将 (4.24) 中第二处区间范数 $L^3$ 恢复为 $L^2$。
- PDF p.18：分离 $R_j$ 定义与 “Then”，并把 (4.33) 标签移到极大不等式。
- PDF p.19：将分离条件与邻域并集分别标为 (4.38)、(4.39)。
- PDF p.20：恢复 (4.41) 的双范数及内层绝对值界线。
- PDF p.21：将第一、第二个振荡积分估计分别恢复为 (5.18)、(5.19)。
- PDF p.22：恢复 (6.1)/(6.2)、(6.8)/(6.9) 标签顺序，并把 (6.7) 的尺度恢复为 $10^s$。
- PDF p.23：恢复 (6.12)/(6.13) 标签，并将 (6.17) 的尺度恢复为 $10^{s_0}$。
- PDF p.24：恢复 (6.19) 的 $L^2(\mathbf Z)$ 范数、(6.22) 的 $10^s$ 及 (6.25)/(6.26) 标签；将 (6.26) 的变量符号恢复为小写 $\widetilde\psi$。
- PDF p.25：恢复 (6.30) 的 $L^2$ 极大范数边界。
- PDF p.27：恢复 $L^p/\ell^p$ 中的普通 $p$、(7.9) 的两个 $q$ 指数及右端积分号。原页 (7.8) 前两项的范数对象在印刷本本身留空，故按原页保留而没有推补。
- PDF p.28：将 (7.18) 截断区间恢复为 $[0,N^d]$，并将 (7.18)、(7.19) 四处 Fraktur $\mathcal P$ 范数索引恢复为普通 $p$。
- PDF p.29：恢复 (7.22)、(7.24)、(7.26) 的外层 $\ell^p/L^p$ 范数与内层绝对值竖线分组。
- PDF p.30：恢复 (7.30) 范数边界、(7.33) 的 $\ell^p$ 下标及 (7.34) 的 $K_{2^k}$。
- PDF p.31：将 $L_k=K_{2^{Mk}}$ 中误识变量恢复为 $M$；重排 (7.40)/(7.41) 的公式与编号；恢复 (7.42) 的 $L^2(G)$ 外范数。
- PDF p.32：恢复 (7.44) 的 $10^s$；重组并重标 (7.49)/(7.50) 的逐因子误差和与乘积卷积项；恢复 (7.51) 起始指数 $s_2$ 和 (7.52) 的 $1/10$。
- PDF p.33：恢复合并估计的 $1/10$ 与两处 $k_0^{-q}$；重排 (7.57)/(7.58)；恢复 (7.59)/(7.60) 中 $2^k$；修正 (7.62) 范数；恢复证明 (7.2) 分解式首尾两处 $K_{2^k}$。
- PDF p.34：重标 (7.63) 并恢复其 $K_{2^k}$、$4^{s'}$、$\mathcal K_s$，将 “By (7.62)” 放回 (7.64) 前；恢复 (7.64)–(7.66)、(7.70)–(7.71) 的范数/绝对值分组、$p_0$、$K_{2^k}$ 与 $\psi_{r,2^k}$；拆分并重标 (7.67)/(7.68)，恢复两处 $w_{2^k}$ 指数、(7.68) 的续接加号和 (7.71) 的 $\Omega_{k,s}$ 下标逗号。
- PDF p.35：恢复 §7 收尾极大平均中的 $K_{2^k}$。
- PDF p.36：合并并完整标注 (8.9) 的共振集条件；恢复 (8.12)/(8.13) 标签与 $10^s$。
- PDF p.37：恢复 (8.15) 极大算子中的外范数及内层绝对值定界符。

印刷原文的拼写、编号或内部条件疑点未按记忆或数学预期擅改；逐项例子与原页证据保留在相应页记录中。P7 原 page-commit 的 PASS±、本文件现行 FAIL 更正、后续 fix(md) OID 与以上修复登记共同保留候选的历史及当前结论。该候选尚未由 Master-Luna 集成，不更新根索引或共享进度日志。
