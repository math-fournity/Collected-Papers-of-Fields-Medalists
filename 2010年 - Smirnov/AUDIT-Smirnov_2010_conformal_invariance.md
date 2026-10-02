# AUDIT — Smirnov_2010_conformal_invariance（Duminil-Copin & Smirnov, "Conformal invariance of lattice models"，70 页）

- actor：Wf-P30
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置，自报 UNKNOWN）
- PDF：Smirnov_2010_conformal_invariance.pdf，SHA-256 = dfc298f2b1b7bd5b26bb5dfa2a3ed3c25e27248924c2703711c69cbd19194cc5（70 页，pdfinfo 核实）
- MD 基线：Smirnov_2010_conformal_invariance_mineru/Smirnov_2010_conformal_invariance__Smirnov_2010_conformal_invariance.md，SHA-256 = b4b2cd09c397fbcb0449c4ec8f457439a85c2a91a5d4975515fa10e0272d95b8（1743 行）
- 通道判定：`pdftotext -f 1 -l 1` 首页输出完整可读（标题/作者/摘要/目录）→ **文本层可用**，全程「文本层主对账 + PNG 视觉核验」双通道。
- 审计开始：2026-10-02 13:34 EDT

## ⚠️ 开工即发现的全局异常（阻断逐页内容对账与修复）

**MinerU 导出与 PDF 是两篇不同的论文，MD 中不存在本篇任何对应段。**

证据（2026-10-02，本 worktree 内实际读取）：

1. PDF p.1（pdftotext + PNG p001.png 双通道）：标题 "Conformal invariance of lattice models"，作者 Hugo Duminil-Copin and Stanislav Smirnov，arXiv:1109.1549v4 [math.PR] 21 Jun 2012。
2. MD 第 1–2 行（`head -60`）：标题 "MULTI LINEAR FORMULATION OF DIFFERENTIAL GEOMETRY AND MATRIX REGULARIZATIONS"，作者 "JOAKIM ARNLIND, JENS HOPPE, AND GERHARD HUISKEN"。
3. `grep -in "conformal invariance|Smirnov|Ising|Duminil"` 全 MD 仅命中 1 行，且为 "sur**prisingly**" 含 "ising" 的假阳性；MD 内无任何 Ising/SLE/fermionic observable/Smirnov 内容。
4. MinerU 原始导出 `Smirnov_2010_conformal_invariance_mineru/Smirnov_2010_conformal_invariance/structured_content.json`：`is_full_document: true`，33 页，page 0 首块即 Arnlind–Hoppe–Huisken 标题；同目录 images/ 共 248 个公式图，页号仅覆盖 page_1–page_31（33 页论文），与本篇 70 页规模不符。

结论：整个 MinerU 导出（MD + structured_content.json + images）属于 Arnlind–Hoppe–Huisken "Multi linear formulation of differential geometry and matrix regularizations"（约 33 页），对本篇 PDF 是**整文档错源**，不是逐页转写瑕疵。按 `REMAINING_PAPER_MARKDOWN_EDIT_V1` 与 AUDIT-SOP，这不是可用逐处 Edit 修复的内容级错误，也不允许把人工重打的文本冒充 MinerU 导出；正确处置是**对本篇 PDF 重新执行 MinerU 初始导出**后重审。该处置超出本块（p.1–9 审计）授权范围，本块按指示「先完成能完成的页」：逐页渲染 PNG、双通道核对 PDF 原文、逐页落签；因 MD 无对应段，p.1–9 全部记 **FAIL（对应段整文档缺失，以原图为准）**，不做任何 MD 修复（fixes = 空）。

---

## p.001（PDF p.1 / 印刷 p.1）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：题录页——标题 "Conformal invariance of lattice models"；作者 Hugo Duminil-Copin and Stanislav Smirnov；日期 November 27, 2024（arXiv v4 编译日期）；Abstract 全文；Contents §1–§6.4 与页码；左缘 arXiv:1109.1549v4 [math.PR] 21 Jun 2012 竖排水印；页脚印刷页码 1。
- 结果：FAIL——MD（b4b2cd0… 基线）为 Arnlind–Hoppe–Huisken 另一篇论文，本页对应段（标题/摘要/目录）整文档缺失，以原图为准。
- 备注：印刷 quirk 登记——目录 §6.2 原文作 "sub-sequential limits of FK-Ising interfaces are Loewner chains"（行首小写 s），p.43 正文节标题同式样；后续 MinerU 重导出后仍须忠实保留，不得按数学惯例改写。文本层（pdftotext -layout）与 PNG 视觉逐项一致。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：目录续 §7（7.1–7.3）、§8（8.1–8.5）及页码；§1 Introduction 开篇（Lenz-Ising 史、[Len20]/[Isi25]/[Hei28]/[Pei36]/[KW41a, KW41b]）；公式 Hamiltonian E_Λ(σ) ∶= −∑_{x∼y} σ_x σ_y、µ_{β,Λ}(σ) ∶= e^{−βE_Λ(σ)}/Z_{β,Λ}、Z_{β,Λ} ∶= ∑_{σ̃∈{−1,1}^Λ} e^{−βE_Λ(σ̃)}；页脚印刷页码 2。
- 结果：FAIL——MD 无任何对应段（整文档错源为 Arnlind 等），以原图为准。
- 备注：文本层与 PNG 双通道一致；公式中 ∶= 冒号等号、下标 β,Λ 与指数 −βE_Λ(σ) 印刷清晰，后续重导出时按此对账。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：Figure 1（三幅 Ising 构型图，pngmono 下呈半调网纹）及图注 "Ising configurations at β < β_c, at β = β_c, and β > β_c respectively."；Onsager/Yang/McCoy-Wu/Lieb-Baxter/Fisher-Kasteleyn/Kac-Ward 历史段；脚注 1（"This result represented a shock for the community…"）；引文 [Ons44][KO50][Yan52][MW73][Pal07][Lie67, Bax89][Fis66, Kas61][KW52][She60][Vdo65][DZM+99, Cim10][Fis98]；页脚印刷页码 3。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：Figure 1 为位图插图，pngmono 150dpi 下仅见网纹属正常二值化现象；后续 MinerU 重导出需保留该图并抽 300dpi 复核图注 β 关系方向。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：universality/CFT 段与引文 [PP66, Kad66][BPZ84b, BPZ84a][ISZ88][Sch00]；Dobrushin boundary conditions 段（Ω_δ ⊂ δZ²，arcs ∂_ab/∂_ba，+1/−1 自旋固定）；斜体预测展示式 "For any (Ω,a,b) and any conformal map ψ ∶ Ω → C, the random curve ψ ○ γ_(Ω,a,b) has the same law as γ_(ψ(Ω),ψ(a),ψ(b))"；SLE(κ) 定义（driving process √κ B_t，(B_t) standard Brownian motion）；脚注 2 "i.e. one-to-one holomorphic maps"、脚注 3 "In fact the interface is not unique…"；页脚印刷页码 4。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：印刷 quirk 登记——脚注 3 末 "the closest interface to ∂_ab" 的下标 ab 排印位置偏高（近乎上标位），文本层提取为 "to ∂\nab"；重导出对账时按此原样登记，不作"改正"。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：Figure 2 及图注 "An interface between + and − in the Ising model."；Main result 1 (Theorem 2.10) critical Ising → SLE(κ=3)；Main result 2 (Theorem 3.13) critical FK-Ising → SLE(κ=16/3)；[LPSA94] 数值实验段、Cardy's formula [Car92]、Smirnov [Smi01]；crossing probability 记号 C_δ(Ω,A,B,C,D)；页脚印刷页码 5。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：两条 Main result 的定理编号（2.10/3.13）与 κ 值（3 与 16/3）为后续重导出对账的关键锚点；文本层与 PNG 双通道一致。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：audit/p006.png（pngmono 150dpi）
- 核对：fermionic observable 段（Definition 2.9、Theorem 2.11）；discrete complex analysis 应用段及引文 [Ken00][Lov04][Ste05][Mer01][BS08]；Acknowledgments 整段（Búzios, Brazil, August 2010 Clay Mathematics Institute Summer School；致谢 Sidoravicius/Benoist/Cimasoni/Hammond；资助 EU Marie-Curie RTN CODY、ERC AG CONFRA、Swiss FNS、RF Government grant 11.G34.31.0026）；§1.1 Organization of the notes 开篇（Section 2/3 概述）；页脚印刷页码 6。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：Acknowledgments 为重导出对账的高风险段（人名地名带重音：Búzios、Stéphane；长资助编号 11.G34.31.0026），文本层与 PNG 双通道逐项一致。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：audit/p007.png（pngmono 150dpi）
- 核对：§1.1 续（Section 4–8 概述，含 s-holomorphic/spin-holomorphic 与 Loewner chains 表述）；§1.2 Notations；§1.2.1 Primal, dual and medial graphs——rotated square lattice L 顶点集 e^{iπ/4}Z²、边 [xy]、x ∼ y、primal graphs、boundary ∂G（<4 邻居）、dual graph G⋆ 与 L⋆（无限面不对应对偶点）、medial lattice L◇ 与 medial graph G◇、L◇ 为 L 旋转 1/√2 缩放、black/white faces、L◇ 边绕 black faces 逆时针定向；§1.2.2 Approximations of domains——√2δL 记 L_δ（mesh-size √2δ）、L◇_δ（mesh-size δ）、Ω_δ = Ω ∩ L_δ；页脚印刷页码 7。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：印刷 quirk 登记——"Note that L◇ is" 处菱形上标基线略下沉（PNG 与文本层断行 "vertices of L ◇ / √ corresponding…" 均可见）；√2δ 的根号覆盖范围以 PNG 为准（只盖 2）。重导出对账时 L/L⋆/L◇ 的星号与菱形记号需逐个核对。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：audit/p008.png（pngmono 150dpi）
- 核对：§1.2.2 续（分段线性延拓 f）；§1.2.3 Distances and convergence——公式 (1.1) d(z,F) ∶= inf_{y∈F} ∣z−y∣、公式 (1.2) d(γ1,γ2) = inf_φ sup_{u∈[0,1]} ∣γ1(u) − γ2(φ(u))∣（重参数化 φ(0)=0, φ(1)=1），编号 (1.1)/(1.2) 齐全；§2 Two-dimensional Ising model；§2.1 Boundary conditions, infinite-volume measures and phase transition——b ∈ {−1,+1}^{∂G}、公式 (2.1) Z^b_{β,G} = Σ_{σ∈{−1,1}^G ∶ σ=b on ∂G} exp[β Σ_{x∼y} σ_x σ_y]、公式 (2.2) µ^b_{β,G}(σ) = (1/Z^b_{β,G}) exp[β Σ_{x∼y} σ_x σ_y]、free boundary conditions 记号 µ^f_{β,G}；页脚印刷页码 8。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(2.1)/(2.2) 中 β 符号为正（exp[+β∑σ_xσ_y]），下标 σ=b on ∂G 排于求和条件下方；公式编号 (1.1)(1.2)(2.1)(2.2) 为重导出对账锚点。文本层与 PNG 双通道一致。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：audit/p009.png（pngmono 150dpi）
- 核对：Theorem 2.1 (Positive association at every temperature)——FKG inequality 公式 (2.3) µ^b_{β,G}(A∩B) ≥ µ^b_{β,G}(A)µ^b_{β,G}(B)、Comparison between boundary conditions 公式 (2.4) µ^{b1}_{β,G}(A) ≤ µ^{b2}_{β,G}(A)；stochastic domination µ^{b1} ≤ µ^{b2} 与 extremal +/− boundary conditions；Λ_n = [−n,n]² 递增盒子序列与 infinite-volume 极限 µ^+_β、µ^−_β；Theorem 2.2——β_c = ½ ln(1+√2)，magnetization µ^+_β[σ_0] 在 β>β_c 严格正、β<β_c 等于 0；引文 [FKG71][Pei36][KW41a, KW41b][Yan52]；脚注 4；页脚印刷页码 9。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：文本层把 ½ 拍平为 "12"、√2 的根号丢失（"ln(1 + 2)"），属 pdftotext 已知伪影；PNG 为裁决源，分数与根号印刷清晰。上标 b/b1/b2/+/- 与下标 β,G 的堆叠记号是重导出对账重点。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：audit/p010.png（pngmono 150dpi）
- 核对：Gibbs measures 段与引文 [ABF87][Aiz80, Hig81][CV10][Dob72]；幂律 µ^+_{βc}[σ_0σ_x] ≈ ∣x∣^{−1/4}（[Ons44]）；Theorem 2.3（[MW73]）——τ_β(a) = lim_{n→∞} −(1/n) ln µ^+_β[σ_0σ_[na]] = x arcsinh(s_x) + y arcsinh(s_y)，s 的方程 √(1+s²x²) + √(1+s²y²) = sinh(2β) + (sinh(2β))^{−1}；Theorem 2.4 (see e.g. [Mes06]) 公式 (2.5) lim_{β↗β_c} τ_β(z)/(β_c−β) = 4∣z∣；§2.2 Low and high temperature expansions 标题；低温展开 partition function 公式 (2.6) Z^+_{β,G} = e^{β# edges in G⋆} Σ_{ω∈E_{G⋆}} (e^{−2β})^{∣ω∣}；页脚印刷页码 10。
- 结果：FAIL——MD 无任何对应段（整文档错源为 Arnlind–Hoppe–Huisken），以原图为准。
- 备注：文本层与 PNG 双通道一致；(2.6) 中 e 的指数 "β# edges in G⋆" 与 G⋆ 的 ⋆ 上标位置印刷紧凑，重导出对账时按 PNG 为准。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：audit/p011.png（pngmono 150dpi）
- 核对：high temperature expansion 段；恒等式 (2.7) e^{βσ_xσ_y} = cosh(β) + σ_xσ_y sinh(β) = cosh(β)[1 + tanh(β)σ_xσ_y]；Proposition 2.5——公式 (2.8) Z^f_{β,G} = 2^{# vertices G} cosh(β)^{# edges in G} Σ_{ω∈Ɛ_G} tanh(β)^{∣ω∣}、公式 (2.9) µ^f_{β,G}[σ_aσ_b] = Σ_{ω∈Ɛ_G(a,b)} tanh(β)^{∣ω∣} / Σ_{ω∈Ɛ_G} tanh(β)^{∣ω∣}；Ɛ_G 与 Ɛ_{G⋆} 记号衔接句；Proof——(2.10) µ^f 定义式、(2.11) Σ_σ σ_aσ_b e^{−βH(σ)} = 2^{# vertices G} cosh(β)^{# edges in G} Σ_{ω∈Ɛ_G(a,b)} tanh(β)^{∣ω∣}；页底两行推导收尾；页脚印刷页码 11。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：PNG 中边族集合用花体 Ɛ（\mathcal{E} 类），pdftotext 拍平为 "EG"，重导出时须保留花体记号；公式编号 (2.7)–(2.11) 连续齐全。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：audit/p012.png（pngmono 150dpi）
- 核对：Figure 3（两幅菱形网格图）及长图注（low-temperature expansion 的 contour 不含 G 边界点间边、对应 Ɛ_{G⋆}、即 G⋆ 上 free boundary conditions 高温展开）；Proposition 2.5 证明结尾（◻ 收尾）；Ɛ_G 为 loop collections、Ɛ_G(a,b) 附一条 a→b 曲线的说明段；Proposition 2.6 (Kramers-Wannier duality)——tanh(β⋆) = e^{−2β}、公式 (2.12) 2^{# vertices G⋆} cosh(β⋆)^{# edges in G⋆} Z^+_{β,G} = (e^β)^{# edges in G⋆} Z^f_{β⋆,G⋆}；Proof 与 Kramers-Wannier 奇点论证（β_c = β_c⋆ ⟹ β_c = ½ln(1+√2)）；Exercise 2.7、Exercise 2.8 (Peierls argument)；页脚印刷页码 12。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：β_c = ½ln(1+√2) 的分数与根号 PNG 印刷清晰（文本层拍平为 "21 ln(1 + 2)"）；◻ 结尾符、β⋆ 上标星号为对账锚点。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：audit/p013.png（pngmono 150dpi）
- 核对：Figure 4（medial lattice 图，标注 a_δ、z_δ、b_δ）及图注 "An example of collection of contours in Ɛ(a_δ, z_δ) on the lattice Ω◇."；§2.3 Spin-Dobrushin domain, fermionic observable and results on the Ising model 标题；spin-Dobrushin domain (Ω◇_δ, a_δ, b_δ) 定义（b_δ 为 black face 东南角）；E(a_δ,z_δ)/γ(ω) 左转约定；Definition 2.9——spin-Ising fermionic observable F_{Ω_δ,a_δ,b_δ}(z_δ) = Σ_{ω∈Ɛ(a_δ,z_δ)} e^{−(1/√2) iW_{γ(ω)}(a_δ,z_δ)} (√2−1)^{∣ω∣} / Σ_{ω∈Ɛ(a_δ,b_δ)} e^{−(1/√2) iW_{γ(ω)}(a_δ,b_δ)} (√2−1)^{∣ω∣}；winding W_γ 定义句；分母与 conditioned critical Ising partition function 的联系段（(2.11) 回引）；页脚印刷页码 13。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：指数内堆叠分数 1/√2 在 150dpi 下字形较小，文本层被拆散为 "e− 2 iW…/1/√" 三段，属 pdftotext 伪影；PNG 可辨分数结构，重导出对账时以 300dpi 抽查该公式再定案。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：audit/p014.png（pngmono 150dpi）
- 核对：Figure 5（primal/dual lattice 高温展开与对偶构型图，含 +/− 自旋圈码与 a_δ、b_δ 标注）及长图注（a_δ 连 b_δ 的约束对应 +/− boundary conditions partition function）；分母对应 free boundary conditions 条件于 σ_a=σ_b 同自旋的 partition function 段、disorder operators 一句；临界性 √2−1 = e^{−2β_c} 与 Kramers-Wannier duality 解释段（dual graph 加一层 dual vertices、Fig. 5 引用）；spin Dobrushin domain 上的临界 Ising 模型约定段（interface γ_δ 从 a_δ 到 b_δ、左转约定、∂_{ab}^⋆/∂_{ba}^⋆ 弧、Figures 1/2 回引）；Theorem 2.10——(γ_δ)_{δ>0} 弱收敛于 chordal Schramm-Loewner Evolution κ = 3；页脚印刷页码 14。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：∂_{ab}^⋆ 的下标 ab 与上标 ⋆ 堆叠排印（PNG 中 ab 偏高），与 p.4 脚注 3 同类 print quirk，登记不改；κ = 3 与 Theorem 2.10 编号为重导出对账锚点。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：audit/p015.png（pngmono 150dpi）；疑难字形仲裁件 audit/p015_cetail_300dpi.png（300dpi 裁切）
- 核对：Theorem 2.10 证明程序四条 bullet——tightness、M_t^z_δ = F_{Ω◇_δ∖γ_δ[0,t],γ_δ(t),b_δ}(z_δ) 为 discrete curve γ_δ 的 martingale、martingales 收敛给出 sub-sequential limit 的 (M_t^z)_t、用 martingales 识别唯一可能极限 chordal SLE(κ=3)；Theorem 2.11 ([CS09])——公式 (2.13) F_{Ω_δ,a_δ,b_δ}(·) → √( ψ′(·) / ψ′(b) )，根号覆盖分数（pdftotext 把该根号-分数结构乱码为 "¿ Á À"，PNG 为裁决源），在 Ω 每一紧子集上一致收敛，ψ 为 Ω 到上半平面 ℍ 的任一共形映射（a↦∞、b↦0）；Theorem 2.12 ([HS10])——µ^f_{β_c,Ω∩δZ²}[σ_xσ_y] = (√2/2) − (φ′_a(a)/π)δ + o(δ)，φ_a 为 Ω 到圆盘 𝔻、a↦0、φ′_a(a)>0 的唯一共形映射；§3 Two-dimensional FK-Ising model 标题；§3.1 FK percolation 开篇（[Gri06][FK72]、configuration ω、open/closed、x ↔ y、clusters）；页脚印刷页码 15。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：疑难字形仲裁——150dpi PNG 中 "will be explained in … Section 6" 一行的 d 字形升部缺损疑似 "cetail"，经 300dpi 裁切复核（audit/p015_cetail_crop300.png）确认为 "detail"，属渲染伪影而非 print quirk，不登记为原文错字。(2.13) 的根号套分数结构是重导出对账高风险点。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：audit/p016.png（pngmono 150dpi）
- 核对：boundary conditions ξ = ∂G 的 partition、o(ω)/c(ω)/k(ω,ξ)（wiring）定义；FK percolation 定义公式 (3.1) φ^ξ_{p,q,G}(ω) ∶= p^{o(ω)}(1−p)^{c(ω)} q^{k(ω,ξ)} / Z^ξ_{p,q,G}；q ≥ 1 positively correlated 段；Theorem 3.1——FKG 公式 (3.2) φ^ξ_{p,q,G}(A∩B) ≥ φ^ξ_{p,q,G}(A)φ^ξ_{p,q,G}(B)、Comparison 公式 (3.3) φ^ψ_{p,q,G}(A) ≥ φ^ξ_{p,q,G}(A)（ξ 为 ψ 的 refinement）；wired ξ=1 / free ξ=0 及 extremal 性质；Theorem 3.2——p_c(q) ∈ (0,1)、p<p_c 无 infinite cluster、p>p_c 唯一 infinite cluster；q=1 即 bond percolation 与 coupling 论证段（[Gri06]）；页脚印刷页码 16。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(3.3) 的 φ 上标 ψ/ξ 方向（ξ refinement of ψ ⟹ φ^ψ ≥ φ^ξ）以 PNG 为准核对无误；公式编号 (3.1)–(3.3) 齐全，为重导出对账锚点。
