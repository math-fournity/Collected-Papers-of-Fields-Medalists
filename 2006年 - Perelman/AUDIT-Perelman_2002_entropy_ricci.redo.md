# AUDIT-Perelman_2002_entropy_ricci.redo（Luna 审计重做）

- 性质：Luna 审计重做。用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核。
- actor：Wf-R-P05
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF：2006年 - Perelman/Perelman_2002_entropy_ricci.pdf，SHA256 = 945e278613c45ea1ab617b28c3095783d0e68958dc0546dfcfa9b42b9674fbe1
- MD 基线：Perelman_2002_entropy_ricci__Perelman_2002_entropy_ricci.md，SHA256 = ccf3ba4849988c0e5b20e889195e473b8c1aeadde7ebd560f9e9b8df15026883（即含 Luna 修复 67ca87858 的当前态，全部按 PDF 重核）
- 裁决源：印刷原文 PDF；Luna 旧修复仅是被检对象。print quirk 与错字忠实登记，不按数学预期静默改正。
- 开始时间：2026-10-02 14:30 EDT
- 文本层判定：`pdftotext -f 1 -l 1` 首页提取正常（标题/作者/正文/脚注完整可读）→ **文本层可用，双通道主对账**（每页 PNG 视觉核对 + pdftotext 文本对账）。
- 页码对齐：arXiv math/0211159v1 单篇预印本，PDF 页码 = 印刷页码（39 页）。
- 证据：本目录 `audit-redo/p0NN.png`（pngmono 150dpi）；不动旧 `audit/`。

---

（页级条目按 AUDIT-SOP「审计说明格式」逐页追加于下）

## p.001（PDF p.1 / 印刷 p.1）
- PNG：audit-redo/p001.png（pngmono 150dpi）
- 核对：题录（标题/作者/日期行/arXiv 侧标）、Introduction 节标题、§1 段公式 d/dt g_ij(t)=−2R_ij、Rm_t=△Rm+Q、R_t=△R+2|Ric|²、引文 [H 1]/[H 1,H 2]、脚注全文
- 结果：PASS
- 备注：印刷日期行为 "November 26, 2024"（本 PDF 为 2024-11-26 重编译件，arXiv 侧标仍为 11 Nov 2002）——print quirk 忠实保留，MD 同文，不改。跨页断句（"positive curvature operator"→p.2 "in dimension four converge…"）在 MD 中合并为同段，文本逐字一致，属 MinerU 页流合并，非内容错误。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：audit-redo/p002.png（pngmono 150dpi）
- 核对： blow-up/ancient solution 段（[H 9]、(−∞,T)、[I]、[H 4]、[H 3]、[H 4,§26]）、surgery 段（[H 5]、$\tilde{Rm}(x,t)=tRm(x,t)$、$t\to\infty$、[H 6]）
- 结果：PASS
- 备注：印刷原样错字 "a priory"（应为 a priori）与 "a convergence theorem ," 逗号前空格均为 print quirk，MD 忠实保留未改。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：audit-redo/p003.png（pngmono 150dpi）
- 核对：Hamilton program 收束段、Hamilton-Tian 段、Introduction §2（RG flow、[Gaw,§3]）、Introduction §3（论文组织段）
- 结果：FAIL（一处公式片段丢失）——已按原图修复
- 差异：印刷 "confirm Hamilton's hope that the solution that exists for all time **t → ∞** necessarily has bounded normalized curvature"，MD 原文缺 "→ ∞"（"for all time t necessarily…"）。PNG（p003.png 第 4 行）与 pdftotext p.3 双证。以原图为准，已 Edit 补为 "$t \to \infty$"。
- 备注：其余文本（含 "an hierarchy" print 原样）逐字一致。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：audit-redo/p004.png（pngmono 150dpi）
- 核对：Introduction §3 组织段（§2/§3/(3.4)/L.Gross/§4–§10、[Cao-C]）、§11–§13 概述段、historical remarks 段
- 结果：PASS
- 备注：print quirk 忠实保留——"formal expressions ," 逗号前空格、"( they must satisfy" 括号内空格、"can not" 分写、"three manifolds" 无连字符，MD 与印刷一致。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：audit-redo/p005.png（pngmono 150dpi）
- 核对：节标题 "1 Ricci flow as a gradient flow"、1.1 泛函 F=∫(R+|∇f|²)e^{−f}dV、一阶变分 display 公式逐项、1.2 Proposition（F^m ≤ n/2T ∫dm）、(1.1)/(1.2)/(1.3)
- 结果：FAIL（一处逻辑词丢失）——已按原图修复
- 差异：印刷 "Notice that v/2−h vanishes identically **iff** the measure dm=e^{−f}dV is kept fixed"，MD 原文作 "if"（丢 ff，改变逻辑强度）。PNG（p005.png 第 5 段）与 pdftotext p.5 双证 "iff"。以原图为准，已 Edit 补为 "iff"。
- 备注：其余（变分公式三行逐项、(1.1)–(1.3) 编号与内容、Proposition 陈述无句号 print 原样）一致。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：audit-redo/p006.png（pngmono 150dpi）；仲裁图 audit-redo/p006_bianchi_300dpi.png、p006_period_300dpi.png、p006_barline_600dpi.png
- 核对：(1.4)、F_t ≥ (2/n)∫(R+△f)²e^{−f}dV ≥ (2/n)(∫(R+△f)e^{−f}dV)² = (2/n)F²、1.3 Remark 全部 Bochner-Lichnerovicz 公式（含 R^m 系列定义与 Bianchi 恒等式）、1.4* DeTurck 段、dilaton 段 [D,§6]、Bakry-Emery [B-Em]/[Lott]、节标题 "2 No breathers theorem I"、2.1 breather 定义开头
- 结果：PASS±（两处排版级差异，登记不改）
- 差异：(a) Bianchi 恒等式中间项印刷为 ∇_i R̄^m_ij（R 上有短横，原 PDF 印刷 quirk；600dpi p006_barline_600dpi.png 证实）——MD 以 `\bar { R _ { i j } ^ { m } }` 忠实保留，一致；(b) 印刷 "= 1/2∇_jR^m**.**" 行尾句点存在（p006_period_300dpi.png），MD 该句点缺失（丢字符类排版伪影，不误导数学内容，按 SOP 默认不批量改，仅登记）。
- 备注：其余公式（(1.4)、F_t 链、∇*∇u_i/∇*∇ψ、∇*m 系列、δ^mψ、R^m=2△f−|∇f|²+R、g^ijR^m_ij=R+△f≠R^m）与文本逐项一致。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：audit-redo/p007.png（pngmono 150dpi）；仲裁图 audit-redo/p007_trivial_300dpi.png
- 核对：2.1 soliton 定义段（R_ij+cg_ij+∇_ib_j+∇_jb_i=0、b_i=½∇_ia、Gaussian soliton a=−|x|²/2）、§2 导语段、2.2 λ 定义与单调性、2.3 λ̄ 与 Claim、Indeed 括注（−d/dt logV = (1/V)∫RdV ≥ λ(t)）、Proof of the claim 三行不等式链
- 结果：PASS±（两处词/标点级偏差，已按原图修复；一处行尾句点缺失登记不改）
- 差异与修复：(a) 印刷 "differ only by **diffeomorphism** and scaling"，MD 多出冠词 "a"（300dpi 仲裁）→ 已删；(b) 印刷 "for each pair of t_1 and t_2, are called"，MD 作 "$t_2,$,"（math 逗号+文本逗号双写）→ 已改为 "$t_2$, are called"。
- 登记不改：印刷行尾 "a = −|x|²/2**.**" 句点存在（PNG/pdftotext 双证），MD 缺失——丢字符类排版伪影，不误导，按 SOP 默认不批量改。
- 备注：Claim 斜体段、"can not"、"t∈[t₁,t₂]" 紧排、三行不等式链（含 λ∫−RdV）逐项一致。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：audit-redo/p008.png（pngmono 150dpi）；仲裁图 audit-redo/p008_eq34_300dpi.png
- 核对：2.4 无 soliton 论证（R+△f const、Euler-Lagrange 2△f−|∇f|²+R=const、∫(△f−|∇f|²)e^{−f}dV=0）、2.5* [H 6,§2] RV^{2/n}、节标题 "3 No breathers theorem II"、3.1 引语、(3.1) W 定义、(3.2)、τ>0 段、(3.3)（含 τ_t=−1）、□* 共轭热算子段、(3.4)
- 结果：PASS±（一处双句点已修；一处逗点缺失登记不改）
- 差异与修复：(a) MD 行 115 "${ \mathcal F } .$." 双句点（印刷为 "F ." 单句点带空格 quirk）→ 已删多余句点，保留 "F ." quirk。
- 登记不改：印刷 "= const = 0**,** because"（150dpi PNG 与 pdftotext 双证有逗点），MD 缺失——丢标点类排版伪影，不误导，按 SOP 默认不批量改。
- 备注：(3.4) 300dpi 仲裁：积分号前无 1/(2τ) 系数，1/(2τ) 仅出现于绝对值内被减项 g_ij/(2τ)，MD 与印刷逐项一致；(3.3) τ_t=−1 与印刷一致；□* 用 \Box 表示与印刷空心方框一致。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：audit-redo/p009.png（pngmono 150dpi）
- 核对：μ/ν 定义段（lim_{τ→∞}μ=+∞）、Claim（μ 负小 τ、τ→0 趋零）、Proof of the Claim (sketch)（u=(4πτ)^{−n/2}e^{−f}、τ(t)=τ̄−t、μ(g_ij,τ̄)≤W(g_ij(0),f(0),τ(0))<0 by (3.4)）、W(½τ^{−1}g_ij,f^τ,½)=W(g_ij,f^τ,τ)=μ≤c<0、∫_{ℝⁿ}[½|∇f|²+f−n](2π)^{−n/2}e^{−f}dx<0、L.Gross 段（f=|x|²/2−2logφ）、3.2 Remark（R_ij−g_ij−∇_ib_j−∇_jb_i=0、(1−2t)g_ij(0)、μ(g_ij(t),½−t)=μ(g_ij(0),½)）
- 结果：PASS±（一处双标点已修）
- 差异与修复：印刷 "tends to zero as t tends to τ̄**,** and therefore"（仅逗点），MD 作 "$\bar{\tau}.$,"（math 内句点+文本逗点双写）→ 已改为 "$\bar{\tau}$, and therefore"。
- 备注：印刷 ”converge”（两枚右引号）为 print quirk，MD 忠实保留未改；其余逐项一致。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：audit-redo/p010.png（pngmono 150dpi）
- 核对：3.2 Remark 收尾、3.3* [I]、Log-Sobolev 段 [G]/[B-Em]/[E 1]、节标题 "4 No local collapsing theorem I"、4.1 locally collapsing 定义与 Theorem、Proof（f_k=−logφ(dist+…)、μ(g_ij(0),t_k+r_k²)→−∞）、4.2 κ-noncollapsed Definition、ρ 尺度稳定性段（α²g_ij/αρ）
- 结果：PASS±（一处双句点已修；五处丢/换标点登记不改）
- 差异与修复：印刷 "…on the scale ρ**.** The theorem above…"（单句点），MD 作 "$\rho .$. The theorem"（math 句点+文本句点双写）→ 已改为 "$\rho$. The theorem"。
- 登记不改（丢/换标点，印刷侧均有 PNG+pdftotext 双证）：(a) 4.1 "on [0, T)**.** We say" 句点缺失；(b) "at times t_k**,** such that" 印刷逗点被 MD 作 "$t_k.$" 句点；(c) Proof "…→ −∞**.** However" 句点缺失；(d) Definition "has volume at least κr^n**.**" 句点缺失；(e) 页末 "for all t ∈ [0,T)**,**" 逗点缺失。均不误导数学内容，按 SOP 默认不批量改。
- 备注：Definition 斜体段 MD 拍平为正体，属 MinerU 已知排版伪影；其余文本逐字一致。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：audit-redo/p011.png（pngmono 150dpi）
- 核对：§4 Corollary（t_k→T、Q_k=|Rm|(p_k,t_k)→∞、(a subsequence of )、κ-noncollapsed on all scales）、节标题 "5 A statistical analogy"、5.1 partition function 段（Z=∫exp(−βE)dω(E)、⟨E⟩=−∂/∂β log Z、S=β⟨E⟩+log Z、σ=⟨(E−⟨E⟩)²⟩=∂²/(∂β)² log Z、dm=udV、log Z=∫(−f+n/2)dm）、⟨E⟩/S/σ 三条 display 公式、(3.3 ) 替换段、σ 非负段开头
- 结果：PASS±（一处双逗点已修；一处句点缺失登记不改）
- 差异与修复：印刷 "the entropy S = β⟨E⟩ + log Z**,** and the fluctuation"（单逗点），MD 作 "+\log Z ,$, and"（math 逗号+文本逗号双写）→ 已改为 "+\log Z$, and"。
- 登记不改：Corollary 行尾 "for some κ > 0**.**" 句点印刷存在（PNG/pdftotext 双证），MD 缺失——丢标点不误导，默认不批量改。
- 备注：印刷 quirk 忠实保留——"(a subsequence of )"、"(3.3 ) ," 括号内空格、”density of states” 双右引号。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：audit-redo/p012.png（pngmono 150dpi）
- 核对：σ 非负段续（(a)/(b) δ-function 极限、case (a)/(b)）、ancient solution 段（τ→∞、S bounded）、5.2 Remark、5.3* [C]、Black Hole Thermodynamics 段、节标题 "6 Riemannian formalism in potentially infinite dimensions"、§6 引语、6.1 M̃=M×S^N×R^+ 与度规分量式（g̃_ij=g_ij、g̃_αβ=τg_αβ、g̃_00=N/2τ+R、其余为 0）
- 结果：PASS±（一处双标点已修）
- 差异与修复：印刷 "a limit of a sequence of functions u_i**,** such that each u_i"（仅逗点），MD 作 "$u_i.$,"（math 句点+文本逗号双写）→ 已改为 "$u_i$, such that"。
- 备注：印刷原样错字 "Rimannian geometry"（应为 Riemannian）为 print quirk，MD 忠实保留未改；其余逐字一致。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：audit-redo/p013.png（pngmono 150dpi）
- 核对：6.1 续（Ricci 张量为零 mod N^{−1}、热方程/共轭热方程经 M̃ 上 Laplace 方程解释、ũ*=τ^{−(N−1)/2}ũ）、6.2 g^m 构造（τ(1−2f/N) 微分同胚、g̃^m 分量式、g^m_αβ/g^m_00=(1/τ)(N/2−[τ(2△f−|∇f|²+R)+f−n])、g^m_i0=g^m_α0=g^m_iα=0）、τ=const 超曲面体积形式与标量曲率段、6.3 Bishop-Gromov 引语与测地线长度第一积分
- 结果：FAIL（两处 iff 丢失）——已按原图修复；另两处双标点已修
- 差异与修复：(a) 印刷 "u satisfies the heat equation on M **iff** ũ…" 与 "similarly, u satisfies the conjugate heat equation on M **iff** ũ*=τ^{−(N−1)/2}ũ…"（PNG 与 pdftotext p.13 双证），MD 两处均作 "if"（丢 ff，改变逻辑强度）→ 两处均已 Edit 补为 "iff"；(b) 6.2 开头印刷 "Starting from g̃**,** we can also construct a metric g^m on M̃**,** isometric…"（单逗点），MD 作 "${\tilde g}._$," 与 "$\tilde M,$," 双标点 → 均已改为单逗点。
- 备注："( given by equations (1.1)" 括号内空格、"τ =const" 空格为 print quirk，MD 忠实保留；度规分量两条 display 式逐项一致。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：audit-redo/p014.png（pngmono 150dpi）；仲裁图 audit-redo/p014_accents_300dpi.png、p014_Sring_600dpi.png、p014_Ldot2_600dpi.png
- 核对：测地线长度第二行 display（=√(2Nτ(q))+…+O(N^{−3/2})）、L(γ) 极小化段与 L(q_M)、度量球体积式 V(𝕊^N)∫_M(√τ(q)−(1/2N)L(x)+O(N^{−2}))^N dx、reduced volume 定义段、6.4* [C-Chu 1,2]/[Hu]、节标题 "7 A comparison geometry approach to the Ricci flow"、7.1 引语、L(γ) 定义式
- 结果：PASS±（两处伪影 accent 已修）
- 差异与修复：(a) 印刷 "Let **L**(*q_M*) denote"（600dpi p014_Ldot2_600dpi.png 证实 L 上方净空、无点），MD 作 "$\overset{\cdot}{L}(q_M)$"（伪影点 accent）→ 已改为 "$L(q_M)$"；(b) 印刷 "V(**𝕊**^N)"（600dpi p014_Sring_600dpi.png 证实为无 ring 的黑板粗体 S），MD 作 "\mathring{\mathbb{S}}^N"（伪影 ring）→ 已改为 "\mathbb{S}^N"。
- 备注：MD "M<sup>˜</sup>"（M̃ 的上标式波浪号）为 MinerU 排版伪影，语义不变，登记不改；O(N^{−3/2}) 上标 pdftotext 拍平为 "N − 2" 属文本层伪影，以 PNG 为准与 MD 一致；其余逐项一致。














