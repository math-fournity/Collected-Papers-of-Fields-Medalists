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

## p.017（PDF p.17 / 印刷 p.17）
- PNG：audit/p017.png（pngmono 150dpi）
- 核对：FK percolation duality 开篇（wired boundary conditions 情形、dual model 构造）；Proposition 3.3——公式 (3.4) p⋆ = p⋆(p,q) ∶= (1−p)q / ((1−p)q + p)；Proof——∂G 边缘边可忽略的说明、o(ω⋆) = a − o(ω)、f(ω) = k(ω⋆)、Euler formula "# edges + # connected components + 1 = #sites + # faces"、k(ω) = s − 1 + f(ω) − o(ω) = s − 1 + k(ω⋆) − a + o(ω⋆)、φ^1_{G,p,q}(ω) 四行推演至 φ^0_{p⋆,q,G⋆}(ω⋆)、q(1−p)/p = p⋆/(1−p⋆) 收尾（◻）；self-dual point p_sd = p_sd(q) ∶= √q/(1+√q)；p_c(q) = p_sd(q) 的 Kramers-Wannier 式 heuristic 段起头；页脚印刷页码 17。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(3.4) 分母 (1−p)q + p 与 p_sd 的 √q/(1+√q) 根号覆盖 PNG 印刷清晰；φ 的上标 1/0（wired/free）与 p⋆ 上标星号堆叠为对账重点。

## p.018（PDF p.18 / 印刷 p.18）
- PNG：audit/p018.png（pngmono 150dpi）
- 核对：Theorem 3.4 ([BDC10])——FK percolation 于 square lattice 的 p_c(q) = p_sd(q) = √q/(1+√q) 对每个 q ≥ 1；Exercise 3.5（free boundary conditions 的对偶）；Exercise 3.6 (Zhang's argument, [Gri06])——p = p_sd(q)、φ^0_{p_sd,q}、三小问（1−ε、{n}×[−n,n] 外侧触碰概率 > 1−ε^{1/4}、wired 情形与 p_c(q) 讨论）；Exercise 3.7 (Euler's formula)；§3.2 FK-Ising model and Edwards-Sokal coupling——q = 2、[ES88]、cluster 独立赋 ± 自旋概率 1/2；Proposition 3.8——β = −½ ln(1−p) 与 free boundary conditions；Proof 开头 P[(ω,σ)] = (1/Z^0_{p,2,G}) p^{o(ω)}(1−p)^{c(ω)} 2^{k(ω)}·2^{−k(ω)} = (1/Z^0_{p,2,G}) p^{o(ω)}(1−p)^{c(ω)}；P̃ 与 e^{−2β} = 1−p 段起头；页脚印刷页码 18。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：ε^{1/4} 的堆叠分数 1/4 与 β = −½ln(1−p) 的负号+分数 PNG 印刷清晰（文本层拍平）；Theorem 3.4 编号与 p_c=p_sd 等式为重导出对账锚点。

## p.019（PDF p.19 / 印刷 p.19）
- PNG：audit/p019.png（pngmono 150dpi）
- 核对：Edwards-Sokal 证明续——P̃[(ω̃,σ̃)] = e^{−2βr(σ̃)} p^{o(ω̃)}(1−p)^{a−o(ω̃)−r(σ̃)} / Z^f_{β,p} = p^{o(ω̃)}(1−p)^{c(ω̃)} / Z^f_{β,p}（a 为边数、r(σ̃) 为异自旋相邻边数）；P = P̃ 与 marginal 结论（◻）；coupling 双向随机程序段；wired boundary conditions 给 + boundary conditions 段；Corollary 3.9——µ^f_{β,G}[σ_xσ_y] = φ^0_{p,2,G}(x ↔ y)、µ^+_{β,G}[σ_x] = φ^1_{p,2,G}(x ↔ ∂G)、β_c = −½ ln[1−p_c(2)]、"We leave the proof as an exercise."（◻）；φ^1_{p,2}/φ^0_{p,2} extremal 与唯一性论证段（[Wer09]、p_c = p_sd、self-dual point √2/(1+√2)）；Proposition 3.10——p_c = √2/(1+√2) 处唯一 infinite-volume FK-Ising measure 且 a.s. 无 infinite cluster、对应 β_c 处唯一 spin Ising measure；页脚印刷页码 19。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：两处 ½/√2 分数根号 PNG 印刷清晰（文本层拍平为 12、2）；(x ↔ y)/(x ↔ ∂G) 的双箭头记号为对账锚点。

## p.020（PDF p.20 / 印刷 p.20）
- PNG：audit/p020.png（pngmono 150dpi）
- 核对：Proposition 3.10 Proof——φ^0_{p_sd,2} 无 infinite cluster（Exercise 3.6）、star-connected circuit（八邻域）、µ^f_{β_c} restricted to box 随机占优 µ^+_{β_c}、µ^f_{β_c} ≥ µ^+_{β_c}、结论 φ^0_{p_sd,2} = φ^1_{p_sd,2} 与 µ^−_{β_c} = µ^f_{β_c} = µ^+_{β_c}（◻）；Remark 3.11（integer q ≥ 2 与 Potts models、FKG 可用性对比）；§3.3 Loop representation of the FK-Ising model and fermionic observable 标题；FK Dobrushin boundary conditions（wired on ∂_ba、free on ∂_ab、φ^a,b_{Ω_δ,p} 记号）；dual boundary arcs ∂_ba^⋆/∂_ab^⋆ 与 FK-Dobrushin domain (Ω◇_δ, a_δ, b_δ) 两条 bullet；Remark 3.12；loop configuration 构造起头；页脚印刷页码 20。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：印刷错字登记（忠实保留、不改）——FK-Dobrushin domain 第二条 bullet 原文作 "medial sites a_δ, b_δ ∈ Ω◇_δ between arcs ∂_ba an ∂_ab^⋆"，"an" 系 "and" 脱字，文本层与 150dpi PNG 双通道一致，重导出时须按原样保留。∂ 的下标 ab/ba 与上标 ⋆ 堆叠继续为对账重点。

## p.021（PDF p.21 / 印刷 p.21）
- PNG：audit/p021.png（pngmono 150dpi）
- 核对：整页为 Figure 6——Dobrushin boundary conditions 的 Ω_δ 图（primal 黑点、dual Ω_δ^⋆ 白圈、中间 medial graph Ω_δ^◇；图内标注 ∂_ba、∂_ba^⋆、A、A^⋆、a_δ、b_δ、∂_ab、∂_ab^⋆、Ω_δ^◇ 及注记 "do not belong to Ω_δ^◇"）；长图注——∂_ba 与 ∂_ab^⋆ 为两条最外弧、∂_ba^⋆/∂_ab^⋆ 从内侧毗邻 ∂_ba/∂_ab、solid lines 为 ∂_ab 与 ∂_ba（dashed 为 ∂_ab^⋆ 与 ∂_ba^⋆）；页脚印刷页码 21。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：文本层把图中菱形上标映射为 "!"（"Ω!δ"、"Ω!δ"），属嵌入字体 ToUnicode 缺失的伪影；PNG 为裁决源，重导出时图中标注须逐个按 PNG 核对（含 A/A^⋆ 两点）。

## p.022（PDF p.22 / 印刷 p.22）
- PNG：audit/p022.png（pngmono 150dpi）
- 核对：整页为 Figure 7——Dobrushin domain (Ω_δ, a_δ, b_δ) 中的 FK percolation configuration 及 medial lattice 上的 interfaces（loops 为灰线、exploration path γ 从 a_δ 到 b_δ 为黑线）；图内标注 ∂_ba、a_δ、b_δ、"Ω_δ and Ω_δ^⋆ ∪ ∂_ab^⋆"、γ ∶= γ(ω)、∂_ab^⋆；长图注——exploration path 是 wired arc 侧 open cluster 与 free arc 白面侧 dual-open cluster 之间的 interface；页脚印刷页码 22。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：文本层把 ⋆ 映射为 "#"（"Ω#δ ∪ ∂ab#"），与 p.21 的 "!" 同类字体映射伪影；pngmono 下灰线呈浅网点属正常二值化现象，重导出时图注 grey/black 对应关系按 PNG 与原 PDF 彩色版核对。

## p.023（PDF p.23 / 印刷 p.23）
- PNG：audit/p023.png（pngmono 150dpi）
- 核对：oriented loops 与 exploration path γ = γ(ω) 定义（open cluster 连 ∂_ba 与 dual-open cluster 连 ∂_ab^⋆ 的 interface）；Theorem 3.13 (Conformal invariance of the FK-Ising model, [KS10])——γ_δ 弱收敛于 chordal SLE，κ = 16/3；Definition 3.14——edge FK fermionic observable 公式 (3.5) F_{Ω◇_δ,a_δ,b_δ,p}(e) = E^{a_δ,b_δ}_{Ω_δ,p}[e^{(1/2)·iW_γ(e,b_δ)} 1_{e∈γ}]（指数内堆叠分数 1/2）、vertex observable 公式 (3.6) F(v) = ½ Σ_{e∼v} F(e)；临界时省略 p、简记 F_δ；Theorem 3.15 ([Smi10a])——公式 (3.7) (1/√(2δ)) F_δ(·) → √(φ′(·))，φ 为 Ω 到条带 R×(0,1)、a↦−∞、b↦∞ 的任一共形映射；Theorem 3.16 (RSW-type crossing bounds, [DCHN10])——公式 (3.8) φ^0_{p_sd,2,R}(open path left to right) ≥ c（矩形 4n×n）；页脚印刷页码 23。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(3.5) 指数内 ½·iW 与 (3.7) 的 1/√(2δ)、√(φ′(·)) 根号结构 PNG 印刷可辨（文本层拆散拍平），重导出对账时建议对 (3.5)(3.7) 做 300dpi 抽查；κ = 16/3 与定理编号 3.13/3.15/3.16 为锚点。

## p.024（PDF p.24 / 印刷 p.24）
- PNG：audit/p024.png（pngmono 150dpi）
- 核对：loop representation 分布显式计算段起头；Proposition 3.17——公式 (3.9) φ^{a_δb_δ}_{Ω_δ,p}(ω) = (1/Z) x^{o(ω)} √2^{ℓ(ω)}，x = p/[√2(1−p)]、ℓ(ω) 为 loop 数、o(ω) 为 open 边数；Proof——φ = (1/Z)[p/(1−p)]^{o(ω)} 2^{k(ω)}、Dobrushin boundary conditions 自对偶（dual 为 φ^{b_δa_δ}_{Ω_δ^⋆,p⋆}）、四行根号推演（√(φ^{ab}(ω)φ^{ba}(ω⋆)) 起）、p(1−p⋆)/((1−p)p⋆) = x²、ℓ(ω) = k(ω)+k(ω⋆)−1、Z̃ = √(ZZ⋆)/[√2√(p⋆/(1−p⋆))]^{o(ω)+o(ω⋆)} 与构型无关、◻；§4 Discrete complex analysis on graphs 标题与开篇两段；页脚印刷页码 24。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：本页根号套分数密集（文本层乱码为 ¿ÁÀ 序列），PNG 逐项可辨；φ 的上标 a_δ b_δ / b_δ a_δ 堆叠与 √2 的 ℓ(ω)/k(ω) 指数是重导出对账最高风险点，建议 300dpi 抽查整段证明。

## p.025（PDF p.25 / 印刷 p.25）
- PNG：audit/p025.png（pngmono 150dpi）
- 核对：§4.1 Preharmonic functions、§4.1.1 Definition and connection with random walks——Laplacian Δ ∶= ¼(∂²_{xx} + ∂²_{yy})、Δ_δ f(u) = ¼ Σ_{v∼u}(f(v) − f(u))；Definition 4.1——preharmonic (resp. pre-superharmonic, pre-subharmonic) 若 Δ_δh(x) = 0 (resp. ≤ 0, ≥ 0)；斜体随机游走刻画（(h(X_n)) is a martingale ⟺ preharmonic）；[Law91]、复向量空间与最大最小值原理段；§4.1.2 Derivative estimates and compactness criteria；Proposition 4.2——公式 (4.1) ∣h(x) − h(y)∣ ≤ Cδ · sup_{z∈Ω_δ}∣h(z)∣ / d(x,Ω^c)；Proof——公式 (4.2) h(x) − h(y) = E[h(X_τ) − h(Y_{τ′})]、2r = d(x,Ω^c)、U = x + [−r,r]²、X/Y coupling 两条 bullet（σ 为 [X_1,y] 垂直平分线 ℓ 的 orthogonal symmetry）；页脚印刷页码 25。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：垂直平分线记号在 PNG 中为花体 ℓ，文本层映射为反引号 `，属字体映射伪影；¼ 分数与 ∂² 上下标 PNG 印刷清晰。

## p.026（PDF p.26 / 印刷 p.26）
- PNG：audit/p026.png（pngmono 150dpi）；疑难字形仲裁件 audit/p026_item2_300dpi.png / audit/p026_item2_crop300.png（300dpi 裁切）
- 核对：Proposition 4.2 Proof 收尾——∣h(x)−h(y)∣ ≤ E[∣h(X_τ)−h(Y_{τ′})∣1_{X_τ≠Y_{τ′}}] ≤ 2(sup_{z∈∂U_δ}∣h(z)∣)P(X_τ≠Y_{τ′})、touch ℓ before exiting 概率 ≤ (C′/r)δ、两层 sup 递推（◻）；Proposition 4.3——(h_δ)_{δ>0} precompact 两条件：(1) 任意紧子集一致有界，or (2) 对任意紧 K 存在 M=M(K)>0 使 δ² Σ_{x∈K_δ}∣h_δ(x)∣² ≤ M；Proof——Arzelà-Ascoli、uniformly Lipschitz、C_K = C·sup_{δ>0}sup_{x∈Ω:d(x,K)≤r/2}∣h_δ(x)∣ / d(K,Ω^c)、∣h_δ(x)−h_δ(y)∣ ≤ 2C_K∣x−y∣；第二条件⟹第一条件段——2r = d(K,Ω^c)、(2δ/r) ≤ k ≤ (r/δ)、公式 (4.3) δ Σ_{y∈∂U_{k_δ}}∣h_δ(y)∣² ≤ 2M/r、U_{k_δ} = x + [−δk,δk]²、公式 (4.4) h_δ(x) = Σ_{y∈∂U_{k_δ}} h_δ(y)H_{U_{k_δ}}(x,y)；页脚印刷页码 26。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：疑难字形仲裁——150dpi PNG 中 Proposition 4.3 条件 (2) 的数字疑似带圈 "②"，经 300dpi 裁切（audit/p026_item2_crop300.png）确认为数学斜体 "(2)"，属字体式样而非 print quirk。ℓ 花体、1_{X_τ≠Y_{τ′}} 下标堆叠为对账重点。

## p.027（PDF p.27 / 印刷 p.27）
- PNG：audit/p027.png（pngmono 150dpi）
- 核对：Proposition 4.3 Proof 收尾——Cauchy-Schwarz：h_δ(x)² = (Σ_{y∈∂U_{k_δ}} h_δ(y)H_{U_{k_δ}}(x,y))² ≤ (δ·Σ∣h_δ(y)∣²)(¼·Σ H_{U_{k_δ}}(x,y)²) ≤ 2M/r·C（Exercise 4.5 给 H_{U_{k_δ}}(x,y) ≤ Cδ，◻）；Exercise 4.4——discrete harmonic measure H_{Ω_δ}(·,y) 定义与 h = Σ_{y∈∂Ω_δ} h(y)H_{Ω_δ}(·,y)；Exercise 4.5——H_{Q_δ}(0,y) ≤ Cδ（Q = [−1,1]²）；§4.1.3 Discrete Dirichlet problem and convergence in the scaling limit——早期文献 [PW23, Bou26, Lus26]、[CFL28]；Proposition 4.6——preharmonic 一致极限为 harmonic；Proof——(1/δ)[h_δ(·+δ)−h_δ] precompact、(1/(√2δ))[h_δ(·+δ)−h_δ] 收敛、0 = (1/(2δ²))Δ_δh_δ → ¼[∂²_{xx}h + ∂²_{yy}h]（◻）；Theorem 4.7 陈述起头（f_δ 一致有界且 away from a,b 收敛于 f、h_δ 为唯一 preharmonic 延拓）与页底展示式 h_δ ⟶ h when δ → 0；页脚印刷页码 27。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：文本层把长箭头映射为 "Ð"（"hδ Ð→ h"），PNG 为长箭头 ⟶，属字体映射伪影；1/(√2δ)、1/(2δ²)、¼[∂²xx+∂²yy] 的分数根号 PNG 印刷清晰。

## p.028（PDF p.28 / 印刷 p.28）
- PNG：audit/p028.png（pngmono 150dpi）
- 核对：Theorem 4.7 陈述收尾（uniformly on compact subsets、h 为 ∂Ω 上取值 f 的唯一 harmonic extension）与 Proof——(h_δ) 界 M、precompact (Prop 4.3)、h̃ harmonic (Prop 4.6)、边界连续延拓论证：∣f_δ(x′)−f_δ(x)∣ < ε for x′ ∈ ∂Ω∩Q(x,R)、Q(x,R)=x+[−R,R]²、∣h_δ(y)−f_δ(x)∣ = E_y[f_δ(X_τ)−f_δ(x)]、≤ ε + 2M P_y[X_τ ∉ Q(x,R)]、Exercise 4.8 给 P_y ≤ (r/R)^α、取 r = R(ε/2M)^{1/α} 得 ∣h̃(y)−f(x)∣ ≤ 2ε（◻）；Exercise 4.8 完整陈述（D = {z∶∣z∣<1}、C = {∣z∣=1}、annulus {x ≤ ∣z∣ ≤ 2x}、概率 < r^α）；§4.1.4 Discrete Green functions——G_{Ω_δ}(·,y) 定义两 bullet（Laplacian 仅在 y 处为 1、边界取 0）；−G 的 visit 计数解释；Proposition 4.9 (Riesz representation formula)——f = Σ_{y∈Ω_δ} Δ_δf(y) G_{Ω_δ}(·,y)；页脚印刷页码 28。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(r/R)^α、(ε/2M)^{1/α} 指数与 𝔻 花体 D 的 PNG 印刷清晰；G_{Ω_δ}(·,y) 中点记号 · 为对账锚点。

## p.029（PDF p.29 / 印刷 p.29）
- PNG：audit/p029.png（pngmono 150dpi）；疑难字形仲裁件 audit/p029_boxq_300dpi.png / audit/p029_boxq_crop300.png（300dpi 裁切）
- 核对：Proposition 4.9 Proof（harmonic + 边界为零 ⟹ 恒零，◻）；aQ_δ = [−a,a]² ∩ L_δ 与 ∇_x f(x) = (f(x+δ)−f(x), f(x+iδ)−f(x)) 记号；Proposition 4.10——Σ_{x∈Q_δ}∣∇_x G_{9Q_δ}(x,y)∣ ≤ Cδ Σ_{x∈Q_δ} G_{9Q_δ}(x,y)（y ∈ 9Q_δ）；Proof——C_1,…,C_7 universal constants、y ∈ 9Q_δ∖3Q_δ 情形（Harnack 特例 (1/C_1)G(x,y) ≤ G(x′,y) ≤ C_1G(x,y)、Prop 4.2 推 C_1C_2δ 上界）、y ∈ 3Q_δ 情形（Σ G ≥ C_3/δ²、需证 ≤ C_4/δ、全平面 Green function G_{L_δ}、[MW40] 渐近式 G_{L_δ}(x,y) = (1/π)ln(∣x−y∣/δ) + C_5 + o(δ/∣x−y∣)、两不等式相加，◻）；页脚印刷页码 29。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：疑难字形仲裁——150dpi 下 "9Q_δ" 的数字 9 疑似空心方块，300dpi 裁切（audit/p029_boxq_crop300.png）确认为数字 9（与 aQ_δ 缩放记号一致），非 quirk；ln 分式与 o(δ/∣x−y∣) 以 PNG 为准。

## p.030（PDF p.30 / 印刷 p.30）
- PNG：audit/p030.png（pngmono 150dpi）
- 核对：§4.2 Preholomorphic functions、§4.2.1 Historical introduction——Kirchhoff [Kir47] 电网络模型、两条定律公式 (4.5) Σ_{v∼u}F(uv) = 0 与 (4.6) Σ_{[uv]∈γ}F(uv) = 0、[BSST40] 方形铺砌、Isaacs [Isa41, Isa52]（mono-diffric、Cauchy-Riemann 离散版 ∂_{iα}F = i∂_α F / z̄-导数为 0）、第一定义 i[f(E)−f(S)] = f(W)−f(S)、第二定义 i[f(E)−f(W)] = f(N)−f(S)（N/E/S/W 为面四角）、Ferrand [Fer44, LF55]、Duffin [Duf56]；§4.3 Isaacs's definition of preholomorphic functions——∂̄ = ∂_x + i∂_y 的离散化 ∂̄_δ f(x) = ½[f(E)−f(W)] + (i/2)[f(N)−f(S)]（x ∈ L⋆_δ）；页脚印刷页码 30。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：Cauchy-Riemann 行的下标 iα/α 堆叠与 ∂̄_δ 的 bar 记号以 PNG 为准；(4.5)/(4.6) 编号齐全。

## p.031（PDF p.31 / 印刷 p.31）
- PNG：audit/p031.png（pngmono 150dpi）
- 核对：Remark 4.11（derivation 用图-对偶图对偶、二阶导回原图、primitive 在 G⋆）；Definition 4.12——preholomorphic 即 ∂̄_δ f(x) = 0 ∀x ∈ Ω⋆_δ、discrete Cauchy-Riemann equation；preholomorphic 理论起步段（gradient of preharmonic is preholomorphic）；Exercise 4.13（O(δ³)）；Exercise 4.14（√2δ modified Laplacian、gradient 性质、极限 holomorphic）；Exercise 4.15（contour integral/primitive/differential）；Exercise 4.16——(1/√(2δ))∂̄_δ 与 (1/(2δ²))Δ_δ 依分布收敛于 ∂, ∂̄, Δ；§4.4 s-holomorphic functions 引入段；§4.4.1——line ℓ(e) 过原点与 √ē（ℝ, e^{iπ/4}ℝ, iℝ, e^{3iπ/4}ℝ，Fig. 8）；Definition 4.17——P_{ℓ(e)}[f(x)] = P_{ℓ(e)}[f(y)]（P_ℓ 为正交投影）；页脚印刷页码 31。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：1/(√2δ) 与 1/(2δ²) 分数、e^{iπ/4}ℝ 指数、P_{ℓ(e)} 花体 ℓ 下标以 PNG 为准；Fig. 8 在下一页，跨页引用登记。

## p.032（PDF p.32 / 印刷 p.32）
- PNG：audit/p032.png（pngmono 150dpi）
- 核对：Figure 8——white face 周围 medial edges 的 lines ℓ(e)（图内标注 NW/NE/SW/SE、1、e^{−iπ/4}、e^{iπ/4}、i、v）及图注 "Lines ℓ(e) for medial edges around a white face."；s-holomorphicity 非旋转不变段（e^{iπ/4}f(i·)、if(−·) 仍 s-holomorphic）；Proposition 4.18——s-holomorphic ⟹ preholomorphic；Proof——v ∈ L_δ∪L⋆_δ、四条投影关系（P_ℝ[f(NW)] = P_ℝ[f(NE)] 起、含共轭 f̄ 的四行恒等式）、第二/三/四条分别乘 −i/−1/i 后相加得 0 = (1−i)[f(NW)−f(SE)+if(SW)−if(NE)] = 2(1−i)∂̄_δf(v)（◻）；§4.4.2 Discrete primitive of F²——½Im(∫^z f̄²) 的离散化引语（150dpi 下 f 上 bar 可辨度有限，重导出时 300dpi 抽查）；Theorem 4.19——唯一 H ∶ Ω_δ∪Ω⋆_δ → C 使 H(b_0) = 1 且 H(b)−H(w) = δ∣P_{ℓ(e)}[f(x)]∣² (= δ∣P_{ℓ(e)}[f(y)]∣²)，e=[xy] 为 black face b 与 white face w 夹边；页脚印刷页码 32。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：共轭 bar（f(NW) 等）与 overline 结构密集，150dpi 部分可辨，建议重导出后对本页公式群 300dpi 抽查；(1−i)/2(1−i) 系数为对账锚点。

## p.033（PDF p.33 / 印刷 p.33）
- PNG：audit/p033.png（pngmono 150dpi）
- 核对：Figure 9（2ΔH● 的 arrows contributions 图，黑白点与箭头）及图注（black→white 箭头贡献为负、white→black 为正）；H(b_1)−H(b_2) = ½Im[f(v)²·(b_1−b_2)]（v 为 [b_1b_2] 中心 medial vertex，Ω⋆_δ 同式）；H 为 ½Im(∫^z f̄²) 的离散类似（f̄ 的 bar 在 150dpi 可辨度有限，同 p.32 登记）；Theorem 4.19 Proof——唯一性（单连通）、存在性（沿路径求和、second Kirchhoff's law、elementary square contours）、公式 (4.7) ∣P_{ℓ(n)}[f(v)]∣² − ∣P_{ℓ(e)}[f(v)]∣² + ∣P_{ℓ(s)}[f(v)]∣² − ∣P_{ℓ(w)}[f(v)]∣² = 0 与公式 (4.8) ∣P_{ℓ(n)}∣²+∣P_{ℓ(s)}∣² = ∣f(v)∣² = ∣P_{ℓ(e)}∣²+∣P_{ℓ(w)}∣²（◻）；H●/H○ 记号（Ω_δ 黑面/Ω⋆_δ 白面限制）；Proposition 4.20——H● subharmonic、H○ superharmonic；脚注 5 "H is roughly (the imaginary part of) the primitive of the square of f."；页脚印刷页码 33。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(4.7)/(4.8) 编号齐全；ℓ(n)/ℓ(e)/ℓ(s)/ℓ(w) 与正交关系为重导出对账锚点；脚注 5 上标与正文分隔正常。

## p.034（PDF p.34 / 印刷 p.34）
- PNG：audit/p034.png（pngmono 150dpi）
- 核对：Figure 10（isoradial graph 黑图 + dual 灰顶点）及图注（所有面可内切于半径 r 的圆、dual 顶点为圆心）；Proposition 4.20 Proof——B ∈ Ω_δ∖∂Ω_δ、Fig. 9 十六条 arrows、a,b,c,d = √δP_{ℓ(e)}[f(y)] 四值、八个 interior increments −a²,−b²,−c²,−d²（各两次）、八个 exterior increments (a√2−b)², (b√2−a)², (b√2−c)², (c√2−b)², (c√2−d)², (d√2−c)², (d√2+a)², (a√2+d)²、S = 4(a²+b²+c²+d²) − 4√2(ab+bc+cd−da) (4.9) = 4∣e^{−iπ/4}a − b + e^{i3π/4}c − id∣² ≥ 0 (4.10)、H○ 同理（◻）；Remark 4.21——subharmonic ≤ harmonic 同边界、H●/H○ sandwich 论证；§4.5 Isoradial graphs and circle packings——Duffin [Duf68] 扩展定义；页脚印刷页码 34。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(4.9)/(4.10) 编号齐全；e^{i3π/4} 指数（非 e^{3iπ/4} 排法差异按 PNG 原样）与 √2 因子的括号结构为重导出对账锚点。

## p.035（PDF p.35 / 印刷 p.35）
- PNG：audit/p035.png（pngmono 150dpi）
- 核对：isoradial embedding 续段——circumcircle 同半径 r、Kenyon-Schlenker [KS05] 拓扑充要条件、Baxter [Bax89] Z-invariant graphs 与 eight-vertex/Ising、Mercat [Mer01]、Boutilier-de Tilière [BdT11, BdT10]、Chelkak-Smirnov [CS08]、dimer/UST [Ken02]、star-triangle relation、Cauchy-Riemann 算子离散化高阶成立；circle packings 段——Thurston [Thu86]、Rodin-Sullivan [RS87]（Riemann uniformization 新证）、He-Schramm [HS93]（Koebe conjecture、可数边界分支情形）、Stephenson [Ste05]、non-linear Cauchy-Riemann [BMS05]；§5 Convergence of fermionic observables 标题（at criticality、Theorems 2.11 与 3.15）；§5.1 Convergence of the FK fermionic observable——固定 (Ω,a,b)、F_δ = F_{Ω◇_δ,a_δ,b_δ,p_sd}、三步证明（第一条 bullet：prove the s-holomorphicity of the observable）；页脚印刷页码 35。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：本页为文献密集段（15 个引文键），重导出对账时逐键核对；F_δ 记号的上标 p_sd 堆叠以 PNG 为准。

## p.036（PDF p.36 / 印刷 p.36）
- PNG：audit/p036.png（pngmono 150dpi）
- 核对：三步证明续——Second：H_δ 与 s-holomorphic functions F_δ/√(2δ) 的收敛；Third：F_δ/√(2δ) → √φ′；§5.1.1 s-holomorphicity of the (vertex) fermionic observable for FK-Ising 标题；Lemma 5.1——F_δ(e) ∈ ℓ(e)；Proof——winding 取值 W + 2πZ、权重 ∝ e^{iW/2}、b_δ southeast corner、末边向右（◻）；parenthetical remark（FK Dobrushin domain 定义非旋转不变、southeast 条件不影响收敛结果）；Lemma 5.2——公式 (5.1) F_δ(N) − F_δ(S) = i[F_δ(E) − F_δ(W)]（N/E/S/W 为顺时针相邻边）；Proof——v 对应 SE→NW primal edge（NE→SW 类似，Fig. 11）、involution s 切换 v 对应 primal 边开闭、ê_ω ∶= φ_{Ω◇_δ,a_δ,b_δ,p_sd}(ω) e^{(1/2)W_γ(e,b_δ)} 1_{e∈γ}（e 上方是否有 hat 记号在 150dpi 不可确证，该行建议 300dpi 抽查）、F_δ(e) = ½Σ_ω[ê_ω + ê_{s(ω)}]、公式 (5.2) N_ω + N_{s(ω)} − S_ω − S_{s(ω)} = i[E_ω + E_{s(ω)} − W_ω − W_{s(ω)}]、Case 1（γ 不经邻边，(5.2) 平凡成立）与 Case 2 起头；页脚印刷页码 36。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(5.1)/(5.2) 编号齐全；W + 2πZ 的花体 Z、1_{e∈γ} 指示函数下标以 PNG 为准；Fig. 11 在下一页，跨页引用登记。

## p.037（PDF p.37 / 印刷 p.37）
- PNG：audit/p037.png（pngmono 150dpi）
- 核对：Figure 11（两个 associated configurations：一条 exploration path + 一个 loop / 无 loop，标注 N/W/E/S、v、b_δ）及图注（switching the state of the edge 互相转换）；Lemma 5.2 Proof Case 2 续——γ(ω) 经 W 入 S 出（primal edge open）、P(s(ω)) = (1/√2)P(ω)（self-dual point、少一条 open edge 权 1、少一个 loop 权 √2，Proposition 3.17）、winding 用 W_ω 表出（N 的 winding = W − π/2）；贡献表两行——ω 行：W_ω、0、0、e^{iπ/4}W_ω；s(ω) 行：W_ω/√2、e^{iπ/2}W_ω/√2、e^{−iπ/4}W_ω/√2、e^{iπ/4}W_ω/√2；恒等式 e^{iπ/4} − e^{−iπ/4} = i√2 与 (5.2) 求和推证；Case 3（γ 过四边时 s(ω) 只过两边，化归 Case 2）；结论 (5.2) 恒成立（◻）；vertex observable 过渡段；页脚印刷页码 37。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：表格中 e^{iπ/2}/e^{−iπ/4}/e^{iπ/4} 指数与 √2 分母以 PNG 为准；表格结构与 W/E/N/S 列序为重导出对账锚点。

## p.038（PDF p.38 / 印刷 p.38）
- PNG：audit/p038.png（pngmono 150dpi）
- 核对：Proposition 5.3——vertex fermionic observable F_δ 是 s-holomorphic；Proof——(5.1) 取共轭改写为 F_δ(N)+F_δ(S) = F_δ(E)+F_δ(W)、由 (3.6) 得 F_δ(v) ∶= ½Σ_{e adjacent}F_δ(e) = F_δ(N)+F_δ(S) = F_δ(E)+F_δ(W)、F_δ(N)⊥F_δ(S)（Lemma 5.1）⟹ F_δ(N) 为 F_δ(v) 在 ℓ(N) 上的投影（◻）；F_δ/√(2δ) preholomorphic 与 discrete Riemann-Hilbert boundary value problem 段、离散类比 Im(∫^z [F_δ(z)/√(2δ)]² dz)；§5.1.2 Convergence of (H_δ)_{δ>0} 标题——A 为 bordering a_δ 的 black face（Fig. 6）、Theorem 4.19 定义 H_δ ∶ Ω_δ∪Ω⋆_δ → R，H_δ(A) = 1 且 H_δ(B)−H_δ(W) = ∣P_{ℓ(e)}[F_δ(x)]∣² = ∣P_{ℓ(e)}[F_δ(y)]∣²；H_δ● subharmonic / H_δ○ superharmonic；Lemma 5.4——H_δ● ≡ 1 on ∂_ba、H_δ○ ≡ 0 on ∂_ab^⋆；Proof 起头——公式 (5.3) H_δ●(B)−H_δ●(B′) = ∣F_δ(e)∣² − ∣F_δ(e′)∣² = 0（因 ∣F_δ(e)∣² = φ^{a_δb_δ}_{Ω◇_δ,p_sd}(W ↔ ∂_ab^⋆)，见 Lemma 7.3）、H_δ●(A) = 1 收尾；页脚印刷页码 38。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：∣·∣² 的 ‖ 双竖线排法（PNG 中 ∣P_{ℓ(e)}[F_δ(x)]∣² 用双竖线）与 φ 上标 a_δb_δ 堆叠为对账锚点；(5.3) 编号齐全。

## p.039（PDF p.39 / 印刷 p.39）
- PNG：audit/p039.png（pngmono 150dpi）
- 核对：Figure 12（∂_ba 上相邻两点 B、B′ 与 W、e、e′ 记号图）及图注；Lemma 5.4 Proof 收尾——H_δ○ 在 ∂_ab^⋆ 上常值、dual white face A⋆ ∈ ∂_ab^⋆ bordering a_δ 满足公式 (5.4) H_δ○(A⋆) = H_δ●(A) − ∣F_δ(e)∣² = 1 − 1 = 0（e 为分离 A 与 A⋆ 的边、必属 γ，◻）；Lemma 5.5——H_δ● → 0 on ∂_ab、H_δ○ → 1 on ∂_ba^⋆（uniformly away from a and b）；Proof——B ∈ ∂_ab 距 ∂_ba 为 r、W 为 B 在 ∂_ab^⋆ 上邻点、H_δ•(B) = H_δ○(W) + ∣P_{ℓ(e)}[F_δ(e)]∣² = φ^{a_δb_δ}_{Ω_δ,p_sd}(e ∈ γ)²、e∈γ ⟺ B 连通 wired arc、free boundary conditions 比较 ⟹ ≤ φ^1_{U_δ,p_sd}(B ↔ ∂U_δ)²（U_δ = (B+[−r,r]²)∩L_δ）、Proposition 3.10 ⟹ 收敛于 0（◻）；两引理边界条件 0/1 过渡段；页脚印刷页码 39。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(5.4) 编号齐全；φ 上标 a_δb_δ 与 φ^1_{U_δ,p_sd} 的堆叠下标为对账锚点；e∈γ 平方（(e ∈ γ)²）排法以 PNG 为准。

## p.040（PDF p.40 / 印刷 p.40）
- PNG：audit/p040.png（pngmono 150dpi）
- 核对：Proposition 5.6——(H_δ)_{δ>0} 收敛于 Im(φ)（compact subsets 一致），φ 为 Ω 到条带 T = ℝ×(0,1)（PNG 花体 T）、a↦−∞、b↦∞ 的任一共形映射；Im(φ) 为边界条件 1 on ∂_ba / 0 on ∂_ab 的 Dirichlet 解；Proof——H_δ● subharmonic、h_δ●/h_δ○ 为同边界 preharmonic 函数、三明治公式 (5.5) h_δ○(w_δ) ≤ H_δ○(w_δ) ≤ H_δ●(b_δ) ≤ h_δ●(b_δ)、Theorem 4.7 应用（◻）；§5.1.3 Convergence of FK fermionic observables (F_δ/√(2δ))_{δ>0} 标题；Proof of Theorem 3.15——precompactness 假设下取收敛子列 (F_{δ_n}/√(2δ_n))、f holomorphic、H_{δ_n}(y)−H_{δ_n}(x) = ½Im(∫_x^y (1/δ_n)F²_{δ_n}(z)dz)、右端收敛 Im(∫_x^y f(z)²dz)、左端收敛 Im(φ(y)−φ(x))、φ(y)−φ(x) = C + ∫_x^y f(z)²dz ⟹ f = √φ′；precompactness 化归与 9Q（同中心更大方形）策略；公式 (5.6) δ²Σ_{v∈Q◇_δ}∣F_δ(v)/√(2δ)∣² = δΣ_{x∈Q_δ}∣∇H_δ●(x)∣ + δΣ_{x∈Q⋆_δ}∣∇H_δ○(x)∣ 与 ∇H_δ● 定义；页脚印刷页码 40。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(5.5)/(5.6) 编号齐全；𝕋 花体 T、∫_x^y 上下限、δ_n 下标堆叠以 PNG 为准。

## p.041（PDF p.41 / 印刷 p.41）
- PNG：audit/p041.png（pngmono 150dpi）
- 核对：Theorem 3.15 precompactness Proof 主体——H_δ● = S_δ + R_δ 分解（S_δ 为 ∂9Q_δ 上同边界的 harmonic、R_δ ≤ 0 subharmonic）；S_δ 梯度链式估计 Σ_{x∈Q_δ}∣∇S_δ(x)∣ ≤ (C_1/δ²)·C_2δ(sup_{x∈∂Q_δ}∣S_δ(x)∣) ≤ (C_3/δ)(sup_{x∈9Q_δ}∣H_δ●(x)∣) ≤ C_4/δ（Prop 4.2 + maximum principle）；公式 (5.7) R_δ(x) = Σ_{y∈9Q_δ} ΔR_δ(y)G_{9Q_δ}(x,y)（Prop 4.9）；∇R_δ 六行推演至 C_6/δ（ΔR_δ ≥ 0、Prop 4.10、Prop 4.9、Q_δ 含 1/δ² 量级点、R_δ 一致有界）；(F_δ/√(2δ))_{δ>0} precompact 结论（◻）；§5.2 Convergence of the spin fermionic observable 标题——固定 (Ω,a,b)、F_δ = F_{Ω◇_δ,a_δ,b_δ}、三步同前（后两步仅 sketch，[CS09]）；Proposition 5.7——对 δ > 0，F_δ s-holomorphic on Ω◇_δ；页脚印刷页码 41。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：(5.7) 编号齐全；C_1/δ² 与 C_2δ 的分数乘积排法、9Q_δ 记号（p.29 已仲裁为数字 9）为对账锚点。

## p.042（PDF p.42 / 印刷 p.42）
- PNG：audit/p042.png（pngmono 150dpi）
- 核对：Figure 13——Proposition 5.7 证明中各情形图（上排 ω、下排 ω′，六列标注 1(a)、1(b)、2、3(a)、3(b)、4，图内 x、y、e、v 记号）及图注；Proposition 5.7 Proof——相邻 medial vertices x、y 与 e=[xy]、v 为 bordering e 的 Ω_δ 顶点、x_ω/y_ω 贡献记号、公式 (5.8) Σ_ω P_{ℓ(e)}(x_ω) = Σ_ω P_{ℓ(e)}(y_ω)、γ(ω) 只终于 x_ω 或 y_ω 之一、配置成对 (ω,ω′) 分割；e 指向 southeast ⟹ ℓ(e) = ℝ；x_ω = (1/Z) e^{−(1/2)i[W_{γ(ω)}(a_δ,x_δ) − W_{γ′}(a_δ,b_δ)]} (√2−1)^{∣ω∣}（Z 为不依赖构型的归一化实数）；六种 pairs、Case 1（interface 达 x/y 后一步达另一点）、Case 2（γ 先达 v 再一步至 x/y）、Case 3（loop 阻止延伸）、Case 4（离开 v 又回来）、curve always goes to the left、cases 1(a)/1(b)/2 中 loop 或 past of γ 不改变计算；表格预告段（x_ω 与 y_{ω′}、argument modulo π、投影到 ℝ 收尾）；页脚印刷页码 42。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：印刷 quirk 登记（忠实保留）——页末句原文作 "When upon projecting on ℝ, the result follows."，"When upon" 连用为原文式样（双通道一致），不作"改正"；(5.8) 编号齐全。

## p.043（PDF p.43 / 印刷 p.43）
- PNG：audit/p043.png（pngmono 150dpi）
- 核对：Lemma 5.2/5.5 证明用贡献表（列：configuration、Case 1(a)、1(b)、2、3(a)、3(b)、4；x_ω 行全为 x_ω；y_{ω′} 行：(√2−1)e^{iπ/4}x_ω、(e^{iπ/4}/(√2−1))x_ω、e^{−iπ/4}x_ω、e^{3π/4}x_ω、e^{5π/4}x_ω、e^{−5π/4}x_ω；arg. x_ω mod π 行：5π/8、π/8、π/8、5π/8、5π/8、5π/8）；◻ 收尾；Proof of Theorem 2.11 (Sketch)——[CS09] 完整证明引用、H_δ 定义（white face adjacent to b 处为 0）、H_δ○ 边界恒 0、H_δ 在 a 附近不应有界（superharmonic 非 harmonic）、unboundedness near a_δ 阻碍 Prop 4.3 直接使用、boundary modification trick（[DCHN10] FK 情形、[CS09] Ising 原始情形）、precompactness、(f,H) 极限、H=0 on ∂Ω∖{a}、H ≥ 0、one-parameter family of positive harmonic functions（= Ω 到上半平面 ℍ、a↦∞ 的共形映射虚部）、ψ 固定 b↦0、H = λImψ、Im(∫^z f̄²) = H（f̄ 的 bar 以 PNG 为准）⟹ f² = λψ′、f(b) = 1 ⟹ λ = 1/ψ′(b)、结论 f(z) = √(ψ′(z)/ψ′(b))（◻）；边界 b 附近光滑性正则性假设说明段；§6 Convergence to chordal SLE(3) and chordal SLE(16/3) 标题与三步策略第一条 bullet；页脚印刷页码 43。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：表中 (e^{iπ/4}/(√2−1)) 为堆叠分数、e^{5π/4}/e^{−5π/4} 指数以 PNG 为准；√(ψ′(z)/ψ′(b)) 根号套分数为对账锚点；本页 §6 标题与 p.1 目录 §6 页码 43 呼应。

## p.044（PDF p.44 / 印刷 p.44）
- PNG：audit/p044.png（pngmono 150dpi）
- 核对：§6 三步策略续两条 bullet——time-changed Loewner chain with continuous driving process（Beffara's course 引用）、唯一可能 driving process 为 √κB_t（B_t standard Brownian motion）；Lévy's theorem 段——X_t 与 X_t² − at 均为 martingale 的连续实值过程必为 √aB_t；§6.1 Tightness of interfaces for the FK-Ising model 标题；Theorem 6.1——(γ_δ)_{δ>0} 对 curve distance 拓扑 tight；[AB99] annuli crossed back and forth 论述；S_{r,R}(x) = (x+[−R,R]²) ∖ (x+[−r,r]²) 与 A_k(x;r,R)（k crossings）记号；Theorem 6.2 (Aizenman-Burchard [AB99])——P_δ(A_k(x;r,R)) ≤ C_k(r/R)^{Δ_k}（k ∈ N、C_k < ∞、Δ_k > 2）⟹ (γ̃_δ) tight；Lemma 6.3 (Circuits in annuli)——φ^1_{p_sd,S_{n,2n}(x)}(E(x;n,2n)) ≤ c（c < 1）；wired boundary conditions 与 decouple 论述；页脚印刷页码 44。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：S_{r,R}(x) 下标 r,R、(r/R)^{Δ_k} 指数、φ 上标 1 与 p_sd,S_{n,2n}(x) 堆叠以 PNG 为准；𝔼 概率记号未见（本页无）。

## p.045（PDF p.45 / 印刷 p.45）
- PNG：audit/p045.png（pngmono 150dpi）
- 核对：Figure 14（左：event A_6(x,r,R) 与 alternating open/closed paths；右：矩形 R_T、R_R、R_B、R_L 被 closed paths 沿长边穿过，标注 [−n,n]² 与 [−2n,2n]²）及图注；Lemma 6.3 Proof——四矩形 R_B = [−2n,2n]×[−n,−2n]、R_L = [−2n,−n]×[−2n,2n]、R_T = [−2n,2n]×[n,2n]、R_R = [n,2n]×[−2n,2n]（Theorem 3.16，Section 7.2 预引）、aspect ratio 4、closed path 概率 ≥ c_1、FKG inequality (3.2) ⟹ circuit 概率 ≥ c_1⁴、crossing 概率 ≤ c = 1 − c_1⁴ < 1（◻）；Proof of Theorem 6.1——公式 (6.1) φ^{a_δb_δ}_{Ω_δ,p_sd}(A_{2k}(x; r, 2r)) ≤ c^k（c < 1 一致）、alternating open/dual paths 论证、 successive conditionings、≤ [φ^1_{p_sd,S_{r,2r}(x)}(E(x; r, 2r))]^k、固定 k 使 c^k < 1/8、annulus 分解为 ln_2(R/r) 个 S_{r,2r}、公式 (6.2) φ(A_{2k}(x; r, R)) ≤ (r/R)³；页脚印刷页码 45。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：印刷错字登记（忠实保留、不改）——"Using Lemma 6.3, φ… ≤ c < 1 and and (6.1) follows." 中 "and and" 连写为原文重复（文本层与 PNG 双通道一致）；(6.1)/(6.2) 编号齐全；R_B/R_L/R_T/R_R 与 [−2n,2n] 记号为对账锚点。

## p.046（PDF p.46 / 印刷 p.46）
- PNG：audit/p046.png（pngmono 150dpi）
- 核对：Theorem 6.1 Proof 收尾（Theorem 6.2 ⟹ (γ_δ) tight，◻）；§6.2 sub-sequential limits of FK-Ising interfaces are Loewner chains 标题（行首小写 sub-sequential，与 p.1 目录 quirk 同源，正文证实）；h-capacity / time-changed Loewner chain 定义段（Beffara's course 引用）；Theorem 6.4——(γ_δ)_{δ>0} 的任一 sub-sequential limit 是 time-changed Loewner chain；非自交曲线三条件刻画（h-capacity 连续、严格递增、curve grows locally seen from infinity——g_s 为 Ω_s 到 ℳ hydrodynamical renormalization 的共形映射，PNG 花体 ℳ）；six arm event Δ_6 > 2、universal exponents、5-arm exponent = 2、Δ_6 > Δ_5 = 2 论述；Kemppainen-第二作者结构定理引出；Condition (⋆) 完整陈述（C > 1、Δ > 0、0 < δ < r < R/C、stopping time τ、annulus S_{r,R}(x) 不含 γ_τ、概率 < C(r/R)^Δ，Fig. 15 引用）；页脚印刷页码 46。
- 结果：FAIL——MD 无任何对应段（整文档错源），以原图为准。
- 备注：印刷 quirk 登记——§6.2 节标题行首 "sub-sequential" 小写（p.1 目录已登记，本页正文节标题同式样）；(⋆) 星号条件记号与斜体强调 "while it is not forced to enter S_{r,R}(x) again" 为对账锚点。
