# AUDIT — Crandall–Lions, “Viscosity Solutions of Hamilton-Jacobi Equations” (1983)

**状态：Peer 候选审计；尚未由 Master 集成。**

- actor: `Peer-P08`
- model: `gpt-6-luna`
- reasoning effort: `max`
- 起始工作树基线: `e04c4a9603818cfa2d71271942f696115783c33b`
- 开工时观察到的 canonical `main`: `3dfa4a648c3b456057db96c5f6eece204e5bb1dd`；只作集成目标快照，Peer 不更新根级当前态
- PDF: `Crandall_Lions_1983_viscosity_solutions.pdf`，42 页，SHA-256 `e538a4ea97cf96d92e4771bb4e75e24419217c67e597eb7e6111b7a8b79ff8a2`
- MinerU Markdown: `Crandall_Lions_1983_viscosity_solutions_mineru/Crandall_Lions_1983_viscosity_solutions__Crandall_Lions_1983_viscosity_solutions.md`
- Markdown 修复前 SHA-256: `410f4d2c9a4cbf75da636f55056a715b22e52f26281ab209691e916752bc6686`
- 审计模式判定: 扫描件。`pdfimages -list` 显示 42/42 页各有一张 4304×6072、1-bit CCITT 全页图（600 dpi）。`pdftotext` 得到 90,109 字节（88,572 字符）且未发现 U+FFFD，但抽取层将多个印刷字形错误映射（如首屏的 `Ω`、`∂`、下标等）；该层只作定位辅助，页面图像为裁决依据。
- Markdown 页面定位: 导出同时提供按 PDF 页索引的 `structured_content.json`；正文 Markdown 本身没有页分隔符。每页条目记录该页 PDF 印刷内容与对应的 Markdown 正文定位，不能将 JSON/OCR 代替原页。
- 图片规则: 被本报告引用的全页 PNG 和 300 dpi 仲裁裁片均保存在同目录 `audit/` 下并随对应页提交。

## 逐页审计

### p.001（PDF p.1 / 印刷 p.1）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p001.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1–31 行（题名、作者、摘要、引言与方程 (0.1)–(0.2)、本页底部脚注）
- 核对: 题名及脚注标记、作者、摘要首段、(0.1) Dirichlet 方程、(0.2) Cauchy 方程、定义域与梯度记号、页末 “which satisfy” 跨页续接；以原页图核验公式符号和上下标。
- 结果: **PASS±**。已核正文及方程与印刷页相符；Markdown 未收录页眉的期刊/卷期信息、页脚版权行/ISSN/印刷页码（版面元数据遗漏，未作正文修复）。`pdftotext` 对本扫描页出现明显字形错映，不作为定字依据。
- 修复: 无。
- 核验时间: 2026-10-01 15:49 EDT。

### p.002（PDF p.2 / 印刷 p.2）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p002.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p002_footnotes.png`（页底公式余段与脚注 2–3）
- Markdown: 第 33–59 行（引言续段、例子、定义 (0.3) 及脚注）
- 核对: 引言续句；(0.1)、(0.2) 的非唯一解例子及分段函数；黏性解定义 (0.3)；脚注 2–3。公式、指数、绝对值和条件符号按原页图核对。
- 结果: **FAIL**。第 57 行单独出现 `$C_b(\Omega))$`，原页没有这段独立文字；页底脚注 3 已完整印作 `BUC(Ω) (respectively, C_b(Ω)) ...`，300 dpi 图证实该独立片段是多余文本。其余正文和公式与印刷页相符。该项在全篇审计结束后删除并复核。
- 修复: 已删除孤立片段，并按 p.2 原页与 300 dpi 脚注裁图回核；详见文末「全篇修复登记」。
- 核验时间: 2026-10-01 15:53 EDT。

### p.003（PDF p.3 / 印刷 p.3）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p003.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 61–81 行（引言结果概览、说明段落与数值近似讨论开头）
- 核对: 概览结论 (i)–(v) 与引用小节、存在唯一性和正则性说明、§I.5 两个等价判据介绍、分层呈现说明、末段数值近似过渡句；逐条对照本页原文及 (v) 中模连续性界。
- 结果: **PASS±**。所核正文与公式记号吻合；Markdown 未收录页眉 running head 与印刷页码 3。
- 修复: 无。
- 核验时间: 2026-10-01 15:54 EDT。

### p.004（PDF p.4 / 印刷 p.4）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p004.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 83–124 行（引言收尾、§I.1 记号与定义、方程 (1.1) 和 (1.2) 起始分支）
- 核对: 引言末句；§I.1 方程与空间/算子记号；经典解在正极大点的两次微分计算；正、负极值集定义；Definition I.1 与 (1.2) 第一分支。
- 结果: **PASS±**。本页可见正文和公式与印刷页相符；页眉作者名和印刷页码 4 未进入 Markdown。页底 (1.2) 的超解分支延续到下一页，续接在 p.5 逐页核对。
- 修复: 无。
- 核验时间: 2026-10-01 15:55 EDT。

### p.005（PDF p.5 / 印刷 p.5）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p005.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p005_notation.png`；同符号比较：`audit/300dpi/Crandall_Lions_1983_p004_notation.png`
- Markdown: 第 124–153 行（Definition I.1 第二分支、Remark 1.4、§I.2 开头与稳定性定理引入）
- 核对: 方程 (1.3) 与 Definition I.1 总结、F 与 −F 的区别例、Remark 1.4、经典/黏性解一致性说明、§I.2 第一例和 Theorem I.2 引入。
- 结果: **PASS±**。第 141 行的 `\mathfrak{D}(\Omega)^{+}` 字体族与 p.4 定义中的 `\mathcal{D}` 不同，但 300 dpi 原页显示两处印刷字形同形；这是不会误导对象识别的 TeX 字体族转录差异，按逐页审计规范作为 PASS± 保留，不改正文。其余内容与页图相符；页眉与页码 5 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 15:58 EDT。

### p.006（PDF p.6 / 印刷 p.6）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p006.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p006_proof.png`；脚注对照：`audit/300dpi/Crandall_Lions_1983_p006_footnotes.png`
- Markdown: 第 155–207 行（Theorem I.2 证明、Theorem I.3、Lemma I.4、脚注 4–6）
- 核对: 收敛论证与 (1.5)、Theorem I.3 的 (1.6)–(1.7)、Lemma I.4 陈述/构造开头、页底脚注 4–6；公式按 300 dpi 原页裁片仲裁。
- 结果: **FAIL**。①第 161 行的 `E_{+}(\varphi(u-\overline{k}))` 在印刷页为 `E_{+}(\varphi(u-k))`，原图中的 k 上无横线。②第 197、199、201、203 行分别是 `B(y_0,r)`、`a\cdot b`、`y_0` 与 `a,b\in\mathbf R^M` 的孤立脚注碎片；印刷页只列完整脚注 4、5、6，且完整脚注已录在第 205、207、195 行。其余本页内容相符；页眉和页码 6 未录入 Markdown。
- 修复: 已去除 k 上横线、删除四个多余脚注片段，并将完整脚注 4–6 按印刷次序排列；按 p.6 两张原页/300 dpi 裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:00 EDT。

### p.007（PDF p.7 / 印刷 p.7）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p007.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p007_eq19.png`（方程 (1.9)）
- Markdown: 第 209–256 行（Lemma I.5、Theorem I.3 证明与函数构造）
- 核对: Lemma I.5、(1.8)–(1.9)、子序列极限论证、Theorem I.3 的辅助函数及导数展开；重点核对 (1.9) 的分母和测试函数导数。
- 结果: **FAIL**。第 224 行 (1.9) 的分母写作 `\varphi(y_l)`，300 dpi 印刷页明确为 `\varphi_l(y_l)`；分子和 `D\varphi_l(y_l)` 与印刷相符。该下标影响正在取极限的测试函数序列，须补回。页眉和印刷页码 7 未录入 Markdown。
- 修复: 已将分母改为 `\varphi_l(y_l)`，并按 p.7 原页/300 dpi 方程裁图回核；详见文末登记。
- 核验时间: 2026-10-01 16:02 EDT。

### p.008（PDF p.8 / 印刷 p.8）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p008.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 259–300 行（Corollary I.6–I.8 与非线性未知量变换证明开头）
- 核对: Corollary I.6 一致性结论与证明、Corollary I.7 的乘法/坐标变换公式、Corollary I.8 的 (1.10) 及证明首个构造式；检视公式次序、逆映射和导数。
- 结果: **PASS±**。所核正文和公式与印刷页相符；页眉作者名与印刷页码 8 未进入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:02 EDT。

### p.009（PDF p.9 / 印刷 p.9）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p009.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p009_eq111.png`（方程 (1.11)）；`audit/300dpi/Crandall_Lions_1983_p009_tilde_u.png`（(1.11) 后续辅助函数）；`audit/300dpi/Crandall_Lions_1983_p009_eq112.png`（方程 (1.12)）
- Markdown: 第 303–333 行（Corollary I.8 证明、估计 (1.11)–(1.12)、Remark 1.13 与 §I.3 开头）
- 核对: 逆映射记号、(1.11) Taylor 估计、辅助函数构造及 (1.12)、Remark 1.13 对一般定义域的解释、§I.3 起始段。
- 结果: **PASS±**。两处 (1.11) 记号经 300 dpi 分别核对：第一行的 `D\varphi(x_0)\cdot(x-x_0)` 与后续辅助函数中的 `D\varphi(x_0)\cdot|x-x_0|` 均与各自印刷形式一致。另，(1.12) 的印刷式本身在两组相邻乘积间未见比较符号，末项按扫描可见字形为 `\tilde\varphi(x_0)(u(x_0)\tilde k)`；MinerU 忠实保留，登记为源级 quirk，不依据数学预期补字或改式。页眉与印刷页码 9 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:05 EDT。

### p.010（PDF p.10 / 印刷 p.10）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p010.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p010_footnote7.png`（页底脚注 7）
- Markdown: 第 335–371 行（§I.3 引入、Proposition I.9、跨界面导数关系及脚注 7）
- 核对: 分片光滑解设置、Proposition I.9 的局部性、界面法向/切向记号及两侧方向导数不等式、脚注 7。
- 结果: **FAIL**。第 367 行 `$^{7}u|_{\theta'}$` 与第 369 行 `O'.` 是原页没有的脚注碎片；300 dpi 页底只印有一条完整脚注“\(u|_{\mathcal O'}\) 表示 u 在 \(\mathcal O'\) 上的限制”，完整内容已录在第 371 行。第 337–339、371 行的 `\mathfrak O` 字体族与文中 `\mathcal O` 混用属样式差异，内容仍可辨，不列入本次正文修复。页眉作者名与印刷页码 10 未录入 Markdown。
- 修复: 已删除两处孤立脚注碎片并保留完整脚注；按 p.10 原页/300 dpi 脚注裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:07 EDT。

### p.011（PDF p.11 / 印刷 p.11）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p011.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 376–420 行（界面导数的可取值范围、(1.14)–(1.15)、Theorem I.10 必要性证明）
- 核对: 切向/法向分解与可取法向分量区间；粘性 subsolution/supersolution 条件 (1.14)、(1.15)；Theorem I.10 的必要性论证及局部坐标化开头。
- 结果: **PASS±**。本页所核公式、区间端点和不等号方向均与印刷页相符；页眉 running head 与印刷页码 11 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:07 EDT。

### p.012（PDF p.12 / 印刷 p.12）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p012.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p012_construction.png`（界面上方构造）；`audit/300dpi/Crandall_Lions_1983_p012_example.png`（应用例）；`audit/300dpi/Crandall_Lions_1983_p012_proof_corollary.png`（证明与 (1.20)–(1.21)）
- Markdown: 第 423–474 行（界面上函数构造、黏性条件失败例、Proposition I.11、Remark 1.19 与 Corollary I.12）
- 核对: 首段 \(\psi_0\) 的边界取值/切向导数条件及 \(\psi=\psi_0+\xi y_1\) 定义；分片线性解的例子；Proposition I.11 的 (1.16)–(1.18)；末段 (1.20)–(1.21) 的编号和 “Then” 位置。
- 结果: **FAIL**。①第 423 行把导数等式破坏性地拼成 `= $$\partial...`，并把两个构造式拼在同一行，未忠实保存原页清晰的 \(\partial\psi_0/\partial y_i=\partial u_\pm/\partial y_i\) 及 \(\psi(y)=\psi_0(y_2,\ldots,y_m)+\xi y_1\)。②Corollary I.12 的 (1.20) 在第 467 行被孤立成普通文本，而第 470 行误用 `\tag{Then}`；原页将 (1.20) 标在 \(g'+\gamma g\le h\) 旁，随后另起正文 “Then”。③(1.17) 和 (1.21) 的条件词 “for” 被录成 `f o r`，原页连续排印为普通词。需恢复公式段落、两个标签及这两处文字。
- 源级 quirk: 原页的例句确实印作 `F(p_Tu_{\pm}(0,t)+\xi\vec n(0,t))`，此处没有 D；证明句也印作 `\psi'(t_0)=h(t_0)<h(t_0)`。Markdown 忠实复制了这两处印刷形式，不按推导预期改动。
- 修复: 已重录 \(\psi_0\) 条件与 \(\psi\) 定义，恢复 (1.20) 标签和独立正文 “Then”，并将 (1.17)、(1.21) 的 letter-spaced `f o r` 改为 `for`；两处源级 quirk 保留。按 p.12 三张原页/300 dpi 裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:10 EDT。

### p.013（PDF p.13 / 印刷 p.13）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p013.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p013_prop13.png`；`audit/300dpi/Crandall_Lions_1983_p013_thm14.png`；字形比较 `audit/300dpi/Crandall_Lions_1983_p002_v_reference.png`；跨页复核 Theorem I.14 的同一向量场 `audit/Crandall_Lions_1983_p014.png`
- Markdown: 第 477–526 行（Proposition I.13 的两条等价条件、Theorem I.14 及 (1.22)–(1.28)）
- 核对: (1.22)、Proposition I.13 两个条件及其编号、证明式 (1.25)、Theorem I.14 的向量场与流方程 (1.26)、微分不等式 (1.27) 和沿流估计 (1.28)。
- 结果: **FAIL**。①第 492 行把第一条件的 `\mathcal{O}_z` 误成 `\vartheta_z`。②第一条条件的编号在第 489 行另列为普通 `(1.23)`，却又在第 492 行错误标成 `(1.24)`；第二条条件（第 495–497 行）没有 (1.24) 标号。原页分别给第一、第二条件标 (1.23)、(1.24)。③第 520 行将 Theorem I.14 已定义并在 (1.26) 使用的 Greek vector field `\nu` 误录为 Latin `v`。④方程 (1.27) 中 “in” 被录为 `i n`。p.14 对该定理的延续在证明中继续以 Greek `\nu` 指称同一向量场；p.2 的 Latin `v` 图仅为字形比较，不能决定本处字母身份。第 511、514 行的 `\nu` 编码保留。页眉和印刷页码 13 未录入 Markdown。
- 修复: 已将 `\vartheta_z` 改为 `\mathcal{O}_z`，把 (1.23)、(1.24) 标签放到对应条件，将 (1.27) 的 Latin `v` 改为 Greek `\nu`，并把 `i n` 改为 `in`。按 p.13 原页、两张 300 dpi 裁图及 p.14 跨页同一向量场复核，详见文末登记。
- 核验时间: 2026-10-01 16:15 EDT。

### p.014（PDF p.14 / 印刷 p.14）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p014.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p014_flow.png`；`audit/300dpi/Crandall_Lions_1983_p014_corollary.png`
- Markdown: 第 529–585 行（Theorem I.14 证明、Corollary I.15 与 §I.5 开头）
- 核对: 坐标变换及向量场流的估计、局部到区间的延拓、Corollary I.15 的 Lipschitz 估计、§I.5 条件。
- 结果: **FAIL**。第 571、574 行把 Corollary I.15 证明中定义并沿用的 Latin 向量 `v` 写成希腊 `\nu`；同页第 577 行及 300 dpi 原页对应处均为 Latin `v`。另，第 550 行 (1.29) 的 “on” 被录成 `o n`。来源页在流估计式中首项可见地印作 `u(I(t,0))`，其后同式为 `u(Y(s,0))`；Markdown 保留此印刷字形，列为源级 quirk，不按上下文改为 Y。页眉作者名和印刷页码 14 未录入 Markdown。
- 修复: 已将证明中两处 Greek `\nu` 改为 Latin `v`，并把 (1.29) 的 `o n` 改为 `on`；原页首项 `I(t,0)` 保留。按 p.14 两张 300 dpi 裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:18 EDT。

### p.015（PDF p.15 / 印刷 p.15）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p015.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p015_Aplus_proof.png`（Corollary I.17 与证明）
- Markdown: 第 589–635 行（Theorem I.16、Remark 1.31、Corollary I.17 与 Remark 1.32）
- 核对: (1.30) 的可实现性条件、必要性上界、Remark 1.31 的极限刻画、稠密集 \(A_+\) 的定义与证明。
- 结果: **FAIL**。①第 626 行把普通英文 “and”“near” 录成数学字母串 `a n d`、`n e a r`；原页是正常词组。②第 631 行的 \(E_+\) 项漏掉 \(\varphi\)，且闭合括号位置与原页不符；原页明确为 \(E_+(\varphi(u-(u(y_0)-1)))\)。页眉 running head 与印刷页码 15 未录入 Markdown。
- 修复: 已将 “and”“near” 还原为普通正文，并按原页补入 \(\varphi\) 和正确括号。按 p.15 原页/300 dpi 裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:21 EDT。

### p.016（PDF p.16 / 印刷 p.16）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p016.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p016_domain.png`（定义域符号）；`audit/300dpi/Crandall_Lions_1983_p016_footnote8.png`（脚注 8）
- Markdown: 第 637–707 行（D⁺u/D⁻u 定义、Proposition I.18、唯一性章节开头与脚注 8）
- 核对: 上/下微分的极限定义、(1.33)–(1.34)、(2.1)–(2.5)、脚注 8。
- 结果: **FAIL**。①第 649 行声称每个集合对稠密的 \(y_0\in\varnothing\) 非空，原页是 \(y_0\in\mathcal{O}\)；300 dpi 原图确认此处为领域符号 \(\mathcal O\)。②第 705 行 `$^{8}r^{+}(r^{-})$` 是原页没有的独立脚注碎片；完整脚注已在第 707 行，300 dpi 页底只印一条完整脚注。页眉作者名和印刷页码 16 未录入 Markdown。
- 修复: 已将 `\varnothing` 改为 `\mathcal{O}`，删除多余脚注片段并保留完整脚注。按 p.16 两张 300 dpi 裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:22 EDT。

### p.017（PDF p.17 / 印刷 p.17）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p017.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 709–776 行（Theorem II.1 的衰减情形证明及一般情形开头）
- 核对: (2.7)–(2.12)、最大值 \(M\) 的定义、接触点 \(x_0,y_0\)、两条比较不等式、模连续性 \(\rho_n\) 及一般情形的截断估计。
- 结果: **PASS±**。所核证明脉络、公式和不等号与印刷页相符；页眉及印刷页码 17 未录入 Markdown。结论行的 \(u,v\) 在 Markdown 中加粗而原页为普通斜体，属不改变函数标识的字形样式差异。
- 修复: 无。
- 核验时间: 2026-10-01 16:23 EDT。

### p.018（PDF p.18 / 印刷 p.18）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p018.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 779–824 行（Theorem II.1 一般情形证明开头与 (2.7)–(2.15)）
- 核对: added-in-proof remark、\(M_\varepsilon\) 定义、极限 \(M_\varepsilon\to M\) 的上/下界、(2.13)–(2.14) 估计及 (2.15) 的测试点条件。
- 结果: **PASS±**。所核内容和公式与原页相符；页眉作者名与印刷页码 18 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:24 EDT。

### p.019（PDF p.19 / 印刷 p.19）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p019.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 830–860 行（(2.15) 第二不等式、(2.16) 参数、(2.14) 后续估计与 §II.2 条件）
- 核对: 第二条 (2.15)′ 的符号与 \(k_2\)、(2.16) 的 \(\lambda_\varepsilon,\delta_\varepsilon,\tilde\delta_\varepsilon\)、两条不等式相减后的界、Remark 2.17–2.18 与 §II.2 开头的条件 (2.19)–(2.20)。
- 结果: **PASS±**。本页续接公式、参数符号和 (2.15)′ 标记均与印刷页相符；页眉和印刷页码 19 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:24 EDT。

### p.020（PDF p.20 / 印刷 p.20）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p020.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 863–924 行（条件 (2.21)、(2.21*)、Theorem II.2 与证明起始）
- 核对: 两个关于 H 的连续性条件及参数范围；Theorem II.2 三种假设下的结论 (2.22)；Remark 2.23–2.24；比较不等式 (2.25)–(2.27) 的输入和项次。
- 结果: **PASS±**。公式、条件范围、(2.21*) 星号和各结论与印刷页相符；页眉作者名与印刷页码 20 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:26 EDT。

### p.021（PDF p.21 / 印刷 p.21）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p021.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p021_Aestimate.png`（\(A_\varepsilon\) 连续性界）
- Markdown: 第 927–966 行（对 \(A_\varepsilon\) 的模连续性估计、(ii) 情形的选择及 Lemma II.3 开头）
- 核对: \(\lambda_\varepsilon+\delta_\varepsilon\) 有界性、\(A_\varepsilon\) 的上界集合、\(\Lambda(\alpha)\to0\)、\(v\in\mathrm{BUC}\) 下的距离估计，以及 Lemma II.3。
- 结果: **PASS±**。正文公式与原页吻合；300 dpi 原图中条件集最后 \(K\) 后确有一个额外竖线，Markdown 同样保留，登记为源级 quirk。页眉和印刷页码 21 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:26 EDT。

### p.022（PDF p.22 / 印刷 p.22）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p022.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p022_contact.png`（\(x_\varepsilon\) 的极大集条件及相邻估计）
- Markdown: 第 972–1030 行（Lemma II.3 估计、Theorem II.2 收尾及 §III 方程 (3.1) 开头）
- 核对: \(\rho_{D\Phi}\) 与 (2.28)–(2.29) 型估计、Lemma II.3 证明、\(\lambda_\varepsilon+\delta_\varepsilon\) 展开、(2.26)–(2.27)、§III 边值问题 (3.1) 起始。
- 结果: **FAIL**。第 993 行写成 `x_\varepsilon\in E_+(u-\psi_1)\Phi)`，括号把 \(\Phi\) 错置在极大集之外；300 dpi 原页明确为 `E_+((u-\psi_1)\Phi)`。须修复包围关系。
- 修复: 已将接触点条件改为 `x_\varepsilon\in E_+((u-\psi_1)\Phi)`，按 p.22 原页/300 dpi 接触点裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:29 EDT。

### p.023（PDF p.23 / 印刷 p.23）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p023.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1033–1086 行（Theorem III.1 陈述、(3.2) 及有界区域证明开头）
- 核对: 定理对边界一致连续性的假设与三种结论；(3.2) 中边界范数及 \(m^-\)；证明中 \(M_\alpha\) 的选取、(3.4) 和内点接触点导出的两条不等式。
- 结果: **PASS±**。所核假设、公式、范数域和不等号均与印刷页相符；页眉作者名与印刷页码 23 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:31 EDT。

### p.024（PDF p.24 / 印刷 p.24）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p024.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p024_propIII2.png`；对照 Theorem III.1 (3.2)：`audit/300dpi/Crandall_Lions_1983_p023_theorem32.png`；导数计算：`audit/300dpi/Crandall_Lions_1983_p024_derivative.png`
- Markdown: 第 1089–1146 行（Theorem III.1 证明收尾、Proposition III.2、变换后 Hamiltonian 导数估计）
- 核对: (3.2) 的内部/边界范数关系、(3.6)–(3.8)、Proposition III.2 的结论、\(\partial_r\tilde H\) 计算与凸性推论。
- 结果: **PASS±**。Markdown 忠实呈现页上数学文本。源级 quirk：p.24 Proposition III.2 的印刷式两侧均显示为 \(L^\infty(\partial\Omega)\)，而前一页 Theorem III.1 (3.2) 的左侧是 \(L^\infty(\Omega)\)；300 dpi 两页裁片核实该差异，按印刷保留，不依后续结论改写。页眉作者名与印刷页码 24 未录入 Markdown。
- 修复: 无；源级 quirk 保持原样。
- 核验时间: 2026-10-01 16:34 EDT。

### p.025（PDF p.25 / 印刷 p.25）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p025.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p025_theta.png`（\(\Psi_\theta\) 定义）
- Markdown: 第 1149–1191 行（Proposition III.2 证明收尾、Remark 3.9、反例、Proposition III.3）
- 核对: \(\Psi_\theta\) 与 \(\Phi_\theta\) 的定义和边界范数推论；(3.10) 假设；两个解的构造；凸 Hamiltonian 下的 semiconcavity 说明与 Proposition III.3。
- 结果: **FAIL**。第 1149 行把 \(\Psi_\theta(r)=\theta\Psi(r)+(1-\theta)r\) 的第二个 \(\theta\) 误录为 `\mathcal O`；300 dpi 原图清楚显示为同一个希腊 \(\theta\)。
- 修复: 已将 `(1 - \mathcal{O})r` 改为 `(1 - \theta)r`，按 p.25 原页/300 dpi 裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:35 EDT。

### p.026（PDF p.26 / 印刷 p.26）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p026.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1193–1225 行（Proposition III.3 证明与 §IV 开头）
- 核对: 凸 Hamiltonian 下局部 Lipschitz subsolution 的 mollification 论证、semiconcave supersolution 的切触/可微点论证及 §IV 章节引入。
- 结果: **PASS±**。所核方程、卷积核记号和证明顺序与印刷页相符；(ii) 的不等式中 `in` letter-spacing 为 `i n`，保留原文判断不变并修复为可读单词。页眉作者名与印刷页码 26 未录入 Markdown。
- 修复: 已将该不等式中的 `i n` 改为 `in`，按 p.26 原页回核，详见文末登记。
- 核验时间: 2026-10-01 16:36 EDT。

### p.027（PDF p.27 / 印刷 p.27）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p027.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p027_identity.png`（(4.1)\(_\varepsilon\) 与 Proposition IV.1 证明恒等式）
- Markdown: 第 1227–1263 行（§IV.1、(4.1)\(_\varepsilon\)、Proposition IV.1 的证明开头）
- 核对: vanishing-viscosity 近似问题及编号；解收敛命题；最大点处对 \(-\varepsilon\Delta u_\varepsilon+H\) 的恒等变形；超/下解极限论证。
- 结果: **FAIL**。①第 1236 行的 equation tag 被破坏为 `\tag{4.1) \(_{\varepsilon}\}`；原页标记清楚为 \((4.1)_\varepsilon\)。②第 1246 行混用 `\phi` 和 `\varphi` 表示同一测试函数；300 dpi 原页公式中这些位置均为与上文相同的 \(\varphi\)，应统一为 \(\varphi\)。源级 quirk：第 1243 行 `k\in\mathbf R^N` 与印刷页一致，照录保留。
- 修复: 已重录 (4.1)\(_\varepsilon\) 标签，并将恒等式中误录的 `\phi` 改为印刷所用 `\varphi`；印刷页的 `k\in\mathbf R^N` 保留。按 p.27 原页/300 dpi 恒等式裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:38 EDT。

### p.028（PDF p.28 / 印刷 p.28）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p028.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1265–1313 行（Remark 4.3–4.4、§IV.2 条件及 Lemma IV.2）
- 核对: 假设组 (4.5)、模型方程 (4.6)–(4.8)、Lemma IV.2 的条件 (4.9)、两项先验估计 (4.10) 与 (4.11) 及证明草图。
- 结果: **FAIL**。第 1310 行把原页独立标在公式左侧的 `(4.11)` 错放进 `array` 内容，录作 `\text{4.11)}`，导致编号缺少左括号且进入公式正文；应恢复为独立方程标签。公式右端与集合范围和原页相符。页眉作者名与印刷页码 28 未录入 Markdown。
- 修复: 已将 (4.11) 编号移出公式正文并还原为独立标签，按 p.28 原页回核，详见文末登记。
- 核验时间: 2026-10-01 16:39 EDT。

### p.029（PDF p.29 / 印刷 p.29）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p029.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p029_411.png`（Lemma IV.2 的 (4.11) 推导）
- Markdown: 第 1315–1370 行（Lemma IV.2 证明、Proposition IV.3 及存在性逼近）
- 核对: (4.11) 的推导与两种模项、Proposition IV.3 的 (4.12)–(4.14)、\(\bar H\) 的单调性计算、逼近条件 (4.15) 和近似方程 (4.16)。
- 结果: **PASS±**。所核公式与印刷页相符；特别是 (4.11) 中 `But then` 后的范数未带正部，而上一步含正部，原页与 Markdown 一致。页眉与印刷页码 29 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:40 EDT。

### p.030（PDF p.30 / 印刷 p.30）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p030.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p030_414.png`（估计 (4.14) 的范围端点）
- Markdown: 第 1373–1404 行（存在性证明收尾、(4.13)–(4.16)、Cauchy 问题开头）
- 核对: \(u_\varepsilon\) 的紧性与模连续估计、(4.13) 的逆函数上确界范围、模连续估计 (4.14)、(4.15)–(4.16) 的逼近假设与方程、(5.1) 首个初边值系统。
- 结果: **FAIL**。第 1396 行的 `\max` 参数中，\(\|m\|\) 与 \(\|n\|\) 之间漏了逗号；300 dpi 原图清楚印有分隔逗号。
- 修复: 已在两个范数之间补入逗号，按 p.30 原页/300 dpi 裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:41 EDT。

### p.031（PDF p.31 / 印刷 p.31）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p031.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1407–1435 行（Cauchy 问题记号、Definition 5.3、(5.4)–(5.5)、Proposition V.1 开头）
- 核对: \(Q_T,Q_T^0\) 定义；时间变量导数项 \(\varphi_t\) 与空间梯度项；(5.4)、(5.5) 的 sub/supersolution 不等式方向；Proposition V.1 的边界延拓陈述与证明开头。
- 结果: **PASS±**。所核定义和符号均与原页相符；原页中 “respectively (5.4) and (5.5))” 的双右括号也被忠实保留。页眉作者名和印刷页码 31 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:42 EDT。

### p.032（PDF p.32 / 印刷 p.32）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p032.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p032_remark56.png`；`audit/300dpi/Crandall_Lions_1983_p032_assumptions.png`；`audit/300dpi/Crandall_Lions_1983_p032_theoremV2.png`
- Markdown: 第 1437–1485 行（Proposition V.1 证明收尾、Remark 5.6、假设 (5.7)–(5.9*) 与 Theorem V.2 开头）
- 核对: (5.4) 边界极限论证；Remark 5.6 的域关系与外法向条件；(5.7)–(5.9*) 的闭包、向量维度及参数范围；Theorem V.2 的定义域闭包记号。
- 结果: **FAIL**。第 1485 行把原页的 \(\overline{Q}_T\) 错录为 \(\overline{Q}_{\overline T}\)，给 \(T\) 多加一条横线；300 dpi 原页显示横线仅盖在 Q 上。源级 quirk：Remark 5.6 的集合关系印作 `\mathcal O\subset\mathcal O_1\cap\mathcal O\cup\partial\mathcal O`，且 (5.8) 末尾维数印作 \(\mathbb R^n\)；Markdown 与原页一致，均按印刷保留。
- 修复: 已删除 Theorem V.2 中 `v`、`g` 定义域指标 T 上多出的横线，恢复 `\overline Q_T`；按 p.32 原页/300 dpi 定理裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:45 EDT。

### p.033（PDF p.33 / 印刷 p.33）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p033.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1491–1551 行（Theorem V.3 条件、(5.10)、模型问题假设与极大值定义）
- 核对: \(\partial_0Q_T\) 定义；边界连续性条件和估计 (5.10)；模型假设 (5.12)–(5.13)；\(m_0\)、\(M_\alpha\) 及极大点 (5.14)–(5.18)。
- 结果: **PASS±**。条件域、指数权重、积分项与极值定义均与印刷页相符；页眉和印刷页码 33 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:46 EDT。

### p.034（PDF p.34 / 印刷 p.34）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p034.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p034_horizon.png`（\(\eta\) 的时间支集范围）
- Markdown: 第 1560–1606 行（测试函数乘积、(5.20) 极限估计、推论积分界及 §V.3 开始）
- 核对: 两条测试函数的支集；sub/supersolution 不等式相加；(5.20) 和由 Corollary I.12 得出的指数积分估计；\(\eta\) 的时间区间上限与 (5.21) 开头。
- 结果: **PASS±**。公式和估计与印刷页一致；300 dpi 图确认此处印刷为 \(\eta\in\mathcal D(]0,t[)\)（小写 \(t\)），Markdown 如实记录。页眉作者名与印刷页码 34 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:47 EDT。

### p.035（PDF p.35 / 印刷 p.35）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p035.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1609–1674 行（Theorem V.3 assumptions/results, Proposition V.4 and cone estimate proof）
- 核对: initial condition (5.23), constants (5.24), Lipschitz condition (5.25), cone conclusion (5.26), cutoff hypothesis (5.27), support geometry and (5.28).
- 结果: **FAIL**。①原页在常数定义 `C=... , m=...` 前标号 (5.24)，Markdown 第 1624 行漏掉该标签。②(5.24) 与 (5.26) 的 “on”、(5.25) 的 “for”“and”、(5.27) 的 “in” 和 “the interior of” 均被拆成逐字母空格串；原页是普通连词/说明文字。这些位于公式条件中，须恢复为可读文本，而不保留成数学变量。
- 修复: 已恢复 (5.23)、(5.24) 的正确编号，并将 (5.24)–(5.27) 中 letter-spaced “on”, “for”, “and”, “in”, “the interior of” 改回普通文字。按 p.35 原页回核，详见文末登记。
- 核验时间: 2026-10-01 16:48 EDT。

### p.036（PDF p.36 / 印刷 p.36）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p036.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p036_subtract.png`（相减不等式中的时间偏导）
- Markdown: 第 1680–1720 行（(5.29) 后的光滑截断选择及 Proposition V.4 证明开头）
- 核对: \(\Lambda\) 的空间/时间导数与 (5.29)；参数区间；最大值 \(M_\alpha\)；接触点在 \(\operatorname{supp}\Lambda\) 内部的条件；两条 viscosity inequalities 及相减式中两个偏导。
- 结果: **PASS±**。公式、偏导变量（相减式两项均印作 \(\partial_t\)）和不等号方向与页图吻合；页眉作者名与印刷页码 36 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:50 EDT。

### p.037（PDF p.37 / 印刷 p.37）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p037.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1723–1757 行（cone comparison 收尾、Remarks 5.30–5.32、§V.4 例子开头）
- 核对: 连续极限中的两条梯度界、(5.20) 矛盾式、Remark 5.30–5.32、常微分方程 (5.33)、输运问题 (5.34) 与 flow 假设开头。
- 结果: **PASS±**。符号、梯度项、不等号及编号与原页相符；页眉作者名和印刷页码 37 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:51 EDT。

### p.038（PDF p.38 / 印刷 p.38）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p038.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1763–1807 行（flow 表示的非唯一性论证、Remarks 5.30–5.32、§VI 开头）
- 核对: (5.35) 的 flow 代入、时间函数极值条件、特征公式、非唯一 flow 例、变换 \(v=e^{-\gamma t}u\) 及 (6.1) 引入。
- 结果: **PASS±**。所核公式与原页一致；页眉作者名和印刷页码 38 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:52 EDT。

### p.039（PDF p.39 / 印刷 p.39）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p039.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p039_eq68.png`（(6.8) 及条件行）
- Markdown: 第 1809–1867 行（Proposition VI.1、Theorem VI.2、(6.6)–(6.8) 与 §VI.3 开头）
- 核对: vanishing-viscosity 极限及边值；模型问题假设、(6.5)–(6.8)、半群陈述和翻译不变性公式。
- 结果: **FAIL**。第 1790、1798、1804 行的方程 (6.1)–(6.3) 把 “in”/“on” 错录为 `i n`/`o n`；第 1854 行又将普通词 “for” 拆成 `f o r`。p.39 原页图显示这些均为连续排印的英语介词。(6.8) 条件在原页印作 `for u_0 v_0 ∈ BUC`，两变量间未见逗号，Markdown 忠实保留；Theorem VI.2 句中原页亦印作 “and Q”，均列为源级 quirk，不补写。补充核验（2026-10-02 00:42 EDT）：(6.2) 原页明确印作 u_t + H(x,t,u,Du)=0，旧 Markdown 为减号；扫描全页 `audit/Crandall_Lions_1983_p039.png` 清楚显示加号，本项一并修复。
- 修复: 已将 (6.1)–(6.3) 中 `i n`/`o n` 与 (6.8) 前的 `f o r` 改为 `in`/`on`/`for`，并将 (6.2) 中 -H 改为原页的 +H；不增补源文未印出的逗号，也不改写 “and Q”。按 p.39 扫描全页及 300 dpi (6.8) 裁图回核，详见文末登记。
- 核验时间: 2026-10-01 16:54 EDT。

### p.040（PDF p.40 / 印刷 p.40）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p040.png`（扫描页，pngmono 150 dpi）
- Markdown: 第 1869–1908 行（m-accretive resolvent estimates、Crandall–Liggett approximation 与 (6.11)–(6.13)）
- 核对: (6.9) 的正部与全范数收缩；离散演化式 (6.10) 与极限指数；最大点关系 (6.11)、差分式 (6.12)、分解 (6.13) 及其代入后的不等式。
- 结果: **PASS±**。公式次序、符号和不等号方向与印刷页相符；页眉作者名与印刷页码 40 未录入 Markdown。
- 修复: 无。
- 核验时间: 2026-10-01 16:55 EDT。

### p.041（PDF p.41 / 印刷 p.41）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p041.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p041_eq617.png`（(6.15)–(6.17) 与偏导字形）
- Markdown: 第 1911–1963 行（粘性 supersolution 判据、(6.14)–(6.18) 与参考文献 [1]–[5]）
- 核对: (6.14)–(6.18) 的 test-function 梯度符号和集合域；检查参考文献前五条与本页印刷内容的对应。
- 结果: **PASS±**。Markdown 与原页的定义及参考文献相符。源级 quirk：印刷式 (6.17) 明确写作 `D(x)`，没有 `D\psi(x)`，尽管紧邻的 (6.15)、(6.16) 含 `D\psi`；300 dpi 原图核实此字形，Markdown 照录保留。页眉作者名及印刷页码 41 未录入 Markdown。
- 修复: 无；(6.17) 的印刷形式不推断改写。
- 核验时间: 2026-10-01 16:57 EDT。

### p.042（PDF p.42 / 印刷 p.42）
- actor/model/effort: `Peer-P08 / gpt-6-luna / max`
- PNG: `audit/Crandall_Lions_1983_p042.png`（扫描页，pngmono 150 dpi）
- 300 dpi 仲裁图: `audit/300dpi/Crandall_Lions_1983_p042_refs_06_16.png`；`audit/300dpi/Crandall_Lions_1983_p042_refs_17_27_affiliations.png`
- Markdown: 第 1963–2011 行（参考文献 [5]–[27] 与作者单位；[1]–[4] 从上一页承接）
- 核对: 参考文献编号、作者/占位横线、题名、期刊/丛书、卷期/页码/年份和语言说明；核对两处作者单位。
- 结果: **PASS±**。本页参考文献 [6]–[27] 与单位均对应印刷原文；页眉与印刷页码 42 未写入 Markdown。源级 quirk：正文 p.2 对 [10] 作者印作 “A. Douglis”，本页参考文献 [10] 印作 “A. Douglas”；两种原文写法均保留，并由对应页图支持。
- 修复: 无；文献作者的源内拼写差异保持原样。
- 核验时间: 2026-10-01 17:01 EDT。

## 全篇修复登记

- 原始 MinerU Markdown commit：`d351abbff700768968605937fac5c051de31bb0a`。
- 修复前 Markdown SHA-256：`410f4d2c9a4cbf75da636f55056a715b22e52f26281ab209691e916752bc6686`。
- 独立正文修复 commit：`813c07a6948f1a861ab600eb107d73ba200d881e` (`fix(md)`；父提交为审计/修订候选 `a2b2feb12a5b329ff9abf1469f3bf6fd8f43a485`)。
- 修复后 Markdown SHA-256：`52d668de4de28e2578a044b57be69678f12a373a280996aa4d459b98604cf8ce`。
- PDF SHA-256：`e538a4ea97cf96d92e4771bb4e75e24419217c67e597eb7e6111b7a8b79ff8a2`；PDF 与原始 MinerU 导出均未修改。
- 实际修复页：PDF p.2、6–7、10、12–16、22、25–28、30、32、35、39；共 18 页。具体原页证据和裁片 locator 见对应逐页条目。

| PDF 页 | 修复内容 |
|---|---|
| 2 | 删除印刷页上不存在的孤立脚注片段 `$C_b(\Omega))$`。 |
| 6 | 去除 k 上误加的横线；删除四个残缺脚注片段；完整脚注 4、5、6 保留并按印刷次序排列。 |
| 7 | 在 (1.9) 分母恢复序列下标 `\varphi_l(y_l)`。 |
| 10 | 删除两段重复/残缺脚注片段，保留完整脚注。 |
| 12 | 重录损坏的 \(\psi_0\) 条件与 \(\psi\) 定义；将 (1.20) 标签放回公式并把 “Then” 还原为正文；修复 (1.17)、(1.21) 中 `f o r` 的字距。 |
| 13 | 恢复 \(\mathcal O_z\)；将 (1.23)、(1.24) 标签放回对应条件；将 (1.27) 的向量场改为 \(\nu\)，并恢复 “in”。 |
| 14 | 将 Corollary I.15 中两处 \(\nu\) 改为原页 Latin `v`；恢复 (1.29) 的 “on”；保留原页 `I(t,0)`。 |
| 15 | 将 “and”“near” 还原为普通正文；在 \(E_+\) 项补回 \(\varphi\) 并修复括号。 |
| 16 | 将误录空集符号改为 \(\mathcal O\)；删除多余脚注片段，保留完整脚注。 |
| 22 | 将接触点条件改为 \(E_+((u-\psi_1)\Phi)\) 的原页括号结构。 |
| 25 | 将 \((1-\mathcal O)r\) 改为原页 \((1-\theta)r\)。 |
| 26 | 将不等式中的 letter-spaced `i n` 还原为 “in”。 |
| 27 | 重录 \((4.1)_\varepsilon\) 标签；将恒等式中的误录 `\phi` 改为原页 \(\varphi\)，保留原页 \(k\in\mathbf R^N\)。 |
| 28 | 将 (4.11) 编号移出公式内容，恢复为独立标签。 |
| 30 | 在 (4.14) 两个范数参数之间补回原页逗号。 |
| 32 | 去掉 Theorem V.2 中 `v`、`g` 定义域指标 T 上多出的横线。 |
| 35 | 恢复 (5.23)、(5.24) 标签；将 (5.24)–(5.27) 中 letter-spaced 的 “on/for/and/in/the interior of” 还原为普通文字。 |
| 39 | 将 (6.1)–(6.3) 的 `in/on` 和 (6.8) 前的 `for` 还原；把 (6.2) 的 `-H` 改为扫描页清楚印出的 `+H`。 |

- p.5 的 \(\mathfrak D/\mathcal D\) 差异经 300 dpi 并置裁片复核为不误导的字体族转录差异（PASS±），正文保持原样；p.9 的两处不同表达式分别符合印刷页（PASS±），未作修改。源级印刷 quirk 按逐页条目保留，未依数学预期改写。
- 最终 Markdown 修复后从第 1 行至第 1993 行完成全文复读；所有登记修复均按对应原页图/裁片逐项回核。只读伪影检索对 `~~`、`\x03`、`\dag`、letter-spaced `liminf/max/sup/for/and/near/on/in/the interior of` 及拆裂变音候选均无命中；统计到 115 个 `\tag{` 标记。`git diff --check` 通过。未运行软件测试。
- 逐页总评：42 页签认；p.5、p.9 从初次 FAIL 候选经原页图像证据在独立审计修订提交中改判 PASS±；最终等级为 17 页 FAIL、25 页 PASS±、0 页 PASS。17 个 FAIL 页的问题已在上述独立 `fix(md)` commit 中修复。
- 审计修订 commits：`0860eef2af7f7b2bf3efe9d5d6d982d9d639498d`（p.13 字形）、`dd9d2592a6e1eb7d8964ae3809089ce7a17614e8`（p.5/p.9 评级）、`a2b2feb12a5b329ff9abf1469f3bf6fd8f43a485`（word-spacing 修复登记）。
- 审计角色：`Peer-P08 / gpt-6-luna / max`；本分支为候选，尚未由 `Master-Luna` 集成。
