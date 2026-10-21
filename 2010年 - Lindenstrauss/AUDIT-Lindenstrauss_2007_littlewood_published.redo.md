# AUDIT-Lindenstrauss_2007_littlewood_published.redo — Luna 审计重做（p.1–p.9 块）

- 性质：**Luna审计重做**（用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核）
- actor：Wf-R-P16
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF SHA-256：`7f26dde3f9b206534584b2b94d4a86e6319e467918efca8b4d00b1b1ae574825`
- MD 基线 SHA-256（重做前 MinerU Markdown）：`e92b0d19bd406e72c798834ac2b52e0660d6be0d143a4cd06ed96e675f7c75f9`
- 日期时间：2026-10-03 12:15 EDT（开工）
- 文本层判定：`pdftotext -f 1 -l 1` 首页成功提取 2082 字节结构化正文（题录/摘要/引言完整可读）
  → **文本层可用，采用双通道主对账**（150dpi pngmono PNG 目检 + pdftotext 文本层互证）。
- 本块范围：p.1 至 p.9（全篇 48 页的 Redo 由多个块完成）。
- 证据图目录：`2010年 - Lindenstrauss/audit-redo/`（p0NN.png，pngmono 150dpi；不触碰旧 `audit/`）。
- 旧 Luna 审计文件 `AUDIT-Lindenstrauss_2007_littlewood_published.md` 只作被检对象，不作裁决源；
  唯一裁决源是印刷原文 PDF 原页。

---

## p.001（PDF p.1 / 印刷 p.513）

- PNG：audit-redo/p001.png（pngmono 150dpi）；题录区终裁另用 300dpi 原页裁片（/tmp 瞬时中转，结论已登记于此）。
- 核对：刊名/卷年/页范围、标题、作者、Abstract、§1/§1.1 节标题顺序、开篇三段文字与脚注。
- 结果：**PASS±**
- 差异列表：
  1. MD 缺印刷页眉运行头「Annals of Mathematics, **164** (2006), 513–560」（300dpi 裁片直证；MinerU
     系统性省略运行头，非内容误导，不改动 MD，事实登记于此）。
  2. 行内 LaTeX 紧排空格瑕疵（如 `on$\operatorname{SL}(k,\mathbb{R})/\operatorname{SL}(k,\mathbb{Z})$which`
     缺空格），排版级，不影响语义。
- 旧 Luna 修复重核：Luna p.001 声称修复摘要 `Hausdorf→Hausdorff`——当前 MD 第 7 行确为
  `has Hausdorff dimension zero`，与印刷字形（含 ﬀ 连字）一致，**该旧修复正确，予以确认**。
- 其余核对：标题/作者行（第 1、3 行）、Abstract（第 7 行）、§1.1 三段（第 11/13/15 行前半）与
  脚注（第 17 行：NSF DMS-007133、DMS-0140497、DMS-0434403、Clay、AIM、DMS-0222452）逐句与
  印刷页吻合。本页 MD 无需修改。

---

## p.002（PDF p.2 / 印刷 p.514）

- PNG：audit-redo/p002.png（pngmono 150dpi）；`where n, m` 终裁裁片 300dpi（/tmp 瞬时中转，结论登记于此）。
- 核对：跨页段落延续（unipotents groups→Ratner 段）、§1.2 节标题与段落、Conjecture 1.1 (Margulis)
  陈述、Furstenberg 半群段落前半、运行头。
- 结果：**PASS±**（1 处文字偏离已修复）
- 差异列表：
  1. MD 原作「where $n$ and $m$ are two multiplicatively independent integers」，印刷原文（300dpi 裁片
     + pdftotext 双证）为「where *n, m* are two multi-plicatively independent integers」。已用结构化
     Edit 修复为 `where $n, m$ are two multiplicatively independent integers`（MD 第 25 行）。
  2. 缺运行头「514 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（MinerU 系统性
     伪影，登记不改）。
- print quirk 忠实保留：印刷原文确实拼作「**Raghunatan's** conjecture」（Raghunathan 漏 h，印刷自身
  错拼）；MD 第 15 行同样拼 `Raghunatan's`，与印刷一致，**不改正**。印刷「one–parameter subgroups」
  用 en-dash，MD 保留 en-dash，一致。
- 其余核对：第 15 行后半（[41]/[42]/[40]/[43]/[28] 引文串、parabolic behavior、[8]）、第 19 行 §1.2
  （split Cartan、Weyl chamber flow [16]）、第 21 行（k=2 Anosov、k>2 R^{k-1}-action、e.g. [16],[15]、
  partially hyperbolic）、第 23 行 Conjecture 1.1（X=SL(k,R)/SL(k,Z)、k≥3、closed connected L>A、
  single closed L-orbit）逐句与印刷吻合。

---

## p.003（PDF p.3 / 印刷 p.515）

- PNG：audit-redo/p003.png（pngmono 150dpi）；双通道：pdftotext 文本层互证。
- 核对：Furstenberg 段落收尾、Rees 非代数测度段、Conjecture 1.2 (Littlewood (c. 1930)) 与公式 (1.1)、
  Theorem 1.3 陈述、Corollary 1.4 陈述、过渡句。
- 结果：**PASS±**
- 差异列表：
  1. 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 515」（MinerU 系统性伪影，登记不改）。
  2. MD 第 45 行 Corollary 1.4 内一处用字面字符「µ」（U+00B5）而非 `$\mu$`（「if k is prime, µ is the
     unique」），字形混排伪影，不误导，登记不改。
  3. 定理头格式：印刷小型大写「THEOREM 1.3 / COROLLARY 1.4」，MD 作普通文字「Theorem 1.3. /
     Corollary 1.4.」，排版级，全篇一致，不改。
- print quirk 忠实保留：印刷作「come from A invariant homogeneous subspaces」（A 后无连字），
  MD 第 27 行同为 `A invariant homogeneous subspaces`，与印刷一致，不改。
- 其余核对：Rees 段引文串（[44]、[3, §9]、[21]、[25]、[48]）、Γ<SL(k,ℝ) 与 X=SL(k,ℝ)/Γ、
  公式 (1.1) `liminf_{n→∞} n⟨nu⟩⟨nv⟩ = 0`、⟨w⟩=min_{n∈ℤ}|w−n| 定义、Theorem 1.3 全部条件
  （A-invariant and ergodic、k≥3、one-parameter subgroup of A、positive entropy）与结论
  （μ is algebraic）、Corollary 1.4（not compactly supported、if k is prime、unique SL(k,ℝ)-invariant
  measure on X）逐项与印刷吻合。本页 MD 无需修改。

---

## p.004（PDF p.4 / 印刷 p.516）

- PNG：audit-redo/p004.png（pngmono 150dpi）；「a.e. (u,v)」与「[K:ℚ]=3).」终裁裁片 300dpi
  （/tmp 瞬时中转，结论登记于此）；双通道：pdftotext 文本层互证。
- 核对：Theorem 1.5 陈述与 Ξ 定义、Cassels–Swinnerton-Dyer [1] 段、badly approximable 段、
  公式 (1.2)、k 线性型 f_m 定义式、Theorem 1.6 陈述与公式 (1.3)、Hee Oh [32] 过渡句。
- 结果：**PASS±**（4 处偏离已修复）
- 差异列表（均已用结构化 Edit 修复）：
  1. **Theorem 1.5 结论被意译**：MD 原作「Then the Hausdorff dimension of $\Xi$ is zero.」，印刷原文
     为「Then the Hausdorff dimension *dim*<sub>H</sub> Ξ = 0.」（150dpi 图 + pdftotext 双证）。定理
     陈述的符号形式不得意译，已修复为 `Then the Hausdorff dimension $\dim _ { H } \Xi = 0$.`
     （MD 第 55 行）。
  2. Cassels–Swinnerton-Dyer 段末缺句点：印刷「degree [K : ℚ] = 3).」；MD 原作 `= 3 )$` 收尾，
     已补 `.`（MD 第 57 行）。
  3. 「for a.e. $(u,v)$, equation (1.1) holds」的逗号为 MD 添加：印刷（300dpi 裁片）作
     「for a.e. (u, v) equation (1.1) holds」，无逗号；已删（MD 第 59 行）。
  4. §1.6 前导段末缺句点：印刷「evaluated on ℤ^k∖{0}.」；MD 原作 `$\mathbb { Z } ^ { k } \setminus \{ 0 \}$`
     收尾，已补 `.`（MD 第 83 行）。
- 缺运行头「516 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（系统性，登记不改）；
  Theorem 1.6 行末印刷逗号（`∖ Ξ_k,` 后接展示式）MD 未保留，排版级，不改。
- 其余核对：Ξ 定义（(u,v)∈ℝ²、liminf n⟨nu⟩⟨nv⟩>0）、(1.1) 引用、Hausdorff dimension 1 的 badly
  approximable 集、Pollington and Velani [35]、(1.2) 集合、f_m = Π_{i=1}^k m_i、m=(m_ij) 行说明、
  Theorem 1.6（Ξ_k ⊂ SL(k,ℝ)、维数 k−1、m ∈ SL(k,ℝ)∖Ξ_k、inf_{x∈ℤ^k∖{0}}|f_m(x)|=0、A-invariant、
  transversally zero）逐项与印刷吻合。

---

## p.005（PDF p.5 / 印刷 p.517）

- PNG：audit-redo/p005.png（pngmono 150dpi）；双通道：pdftotext 文本层互证。
- 核对：Conjecture 1.7 (Margulis, 1993) 全陈述（G、U_1、U_2、格条件、结论）、Hee Oh [33]/[32] 段、
  §1.3 Measure rigidity 两段、脚注 1。
- 结果：**PASS±**（2 处偏离已修复）
- 差异列表：
  1. **print quirk 被静默改正（已恢复）**：印刷原文（pdftotext 行 44 直证）作「Hausdorff dimension and
     **tranversals**」（漏 s，印刷自身错拼）；MD 原作 `transversals`，属对印刷错字的静默改正。已恢复
     为 `tranversals`（MD 第 101 行），并在此登记为 print quirk——同一句后文「transversally to the
     orbit」印刷拼写正常，两处均按印刷原样保留。
  2. Conjecture 1.7 结论行缺句点：印刷「…× GL(2,ℝ).」；MD 原作 `$\mathrm { G L } ( 2 , \mathbb { R } )$`
     收尾，已补 `.`（MD 第 99 行）。
- print quirk 忠实保留（无需修，登记）：印刷 Conjecture 1.7 结论作「up to **conjunction** in
  GL(2,ℝ)×⋯×GL(2,ℝ)」（conjugation 之错拼，印刷原文如此）；MD 第 99 行同为 `conjunction`，
  **与印刷一致，不改正**。
- 其余登记（排版级意译，不误导，不改）：MD 第 101 行两处「the set 𝒟」简化为 `$D$`；
  「Section 7 and Section 10」作「Sections 7 and 10」；「(or more precisely Theorem 10.2 which…)」
  添加两枚逗号；脚注标记 `$\boldsymbol{lattice^1}$` 加粗拍平。
- 其余核对：Conjecture 1.7 头（n≥2 copies of SL(2,ℝ)）、U_1/U_2 上三角/下三角 unipotent 矩阵.display
  （含 U_2 句点、U_1 无句点）、格条件（i=1 and 2、proper connected normal N<G、Γ∩N∩U_i trivial）、
  Hee Oh 段引文串（[33]、[32]、[33, Thm. 1.5]、§10、Theorem 10.2）、§1.3（Furstenberg problem:
  [22],[45],[12]、Rudolph [45]、Johnson [12]、×m,×n、positive entropy→Lebesgue）、脚注 1（[33]）逐项
  与印刷吻合。

---

## p.006（PDF p.6 / 印刷 p.518）

- PNG：audit-redo/p006.png（pngmono 150dpi）；双通道：pdftotext 文本层互证。
- 核对：conditional measures 段、positive entropy/δ-measure 段、Weyl chamber 附加假设段（weak\*
  limits）、two new methods 过渡、first method [3] 段（ℝ-split、all one-parameter groups、Haar、
  nonsplit [4]、Hausdorff dimension at most 1）、third author [20]/Host [9] 段。
- 结果：**PASS±**
- 差异列表（均排版级，登记不改）：
  1. 缺运行头「518 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（系统性）。
  2. 黑板体拍平：印刷「general **ℝ**-split semisimple Lie groups」与页末「Let A be an **ℝ**-split」，
     MD 两处作 `R-split`（第 117、119 行）；MinerU 已知伪影，语义不变。
  3. 行内数学紧排（如 `$m ,$n` 跨字合并），排版级。
- print quirk 忠实保留：印刷作「two commuting hyperbolic automorphisms of the **three torus**」
  （非 three-dimensional torus），MD 第 111 行同为 `the three torus`，一致。
- 其余核对：Lyapunov exponents、δ-measure supported on a single point、if the flow along every
  singular direction … is ergodic、entropies of μ with respect to all one-parameter groups → Haar
  measure、Γ=SL(k,ℤ)/every discrete subgroup Γ、[4]、quantum unique ergodicity conjecture [20]、
  Host [9] 逐句与印刷吻合。本页 MD 无需修改。

---

## p.007（PDF p.7 / 印刷 p.519）

- PNG：audit-redo/p007.png（pngmono 150dpi）；双通道：pdftotext 文本层互证。
- 核对：[20] 方法补段收尾（SL(2,ℝ)×SL(2,ℝ)/Γ A-ergodic 陈述）、complementary 段（"high"/"low"
  entropy、Theorem 2.1 预告）、[20] proof 段（Ratner [39],[38]、H-property、[28] §1.5、a priori）、
  Ledrappier-Young [19] 段（Tomanov–Margulis [26]）、Acknowledgment 全段、Part I 标题、§2 起始段。
- 结果：**PASS±**
- 差异列表（均排版级，登记不改）：
  1. 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 519」（系统性）。
  2. 印刷斜体「*Acknowledgment.*」在 MD 作普通文字「Acknowledgment.」（第 129 行），格式伪影。
- print quirk 忠实保留：印刷作「many one-parameter **subgroup** have positive entropy」（subgroup
  单数配 many），MD 第 123 行同为 `many one-parameter subgroup have`，一致不改。
- 其余核对：第 121 行（irreducible lattice、do commute、[3] not applicable）、第 125 行（unipotent
  trajectories、[39],[38]、Section 1.5 of [28]、quasi-invariant）、第 127 行（Ledrappier-Young [19]、
  G. Tomanov and Margulis' alternative proof of Ratner's theorem [26]）、第 129 行致谢全段（Dave
  Morris Witte、nonisotropic tori、Barak Weiss、Sanju Velani、M. Ratner、referees、Newton Institute、
  spring of 2000、ETH Zurich、University of Washington、Center for Dynamical Systems at the
  Pennsylvania State University、Stanford University）、第 131 行「## Part I. Measure rigidity」与第 133
  行 G=SL(k,ℝ)/k≥3/X=G/Γ/A<G/k×k 对角群定义逐句与印刷吻合。本页 MD 无需修改。

---

## p.008（PDF p.8 / 印刷 p.520）

- PNG：audit-redo/p008.png（pngmono 150dpi）；双通道：pdftotext 文本层互证。
- 核对：Σ 定义式、α^t/diag 约定、unipotent/normalized/normalizer/centralizer 定义段、foliation
  invariance 与 expands U 定义、M_∞(Y) 与 weak\* 拓扑、ν_1∝ν_2 比例记号、球 B_ε 记号、
  d(·,·) 度量约定、§2 标题、§2.1 起始段。
- 结果：**PASS±**（1 处偏离已修复）
- 差异列表：
  1. 重复句点：MD 原作「continuous$f .$. For two Radon measures」，印刷（文本层行 23）为单句点
     「continuous f. For two Radon」。已修复为 `continuous$f.$ For two Radon measures`
     （MD 第 147 行）。
  2. 缺运行头「520 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS」（系统性，不改）。
  3. 行内紧排伪影：`normalized$b y \ g \in G$`（by 拆成 b y）、`$g \in U , \ g - \mathrm{I}_k$` 等，排版级，不改。
- 其余核对：Σ={t∈ℝ^k: t_1+⋯+t_k=0}、(t_1,…,t_k)↦diag、α^t=diag(e^{t_1},…,e^{t_k})∈A、
  ℝ^{k−1} flow、g−I_k 幂零、gHg^{−1}=H、N(H)/C(H)、a(Ux)=Uax、Ad(a) 特征值>1、
  ρ↦∫_Y f(y)dρ(y)、ν_1∝ν_2 若 ν_1=Cν_2（C>0）、B_ε^Y(y)/B_ε^H(I)/B_ε^H·x、
  right-invariant Riemannian metric、H⊂G、X=G/Γ、§2 双行标题、[17, §4]/[45]/[20, §3] 逐项
  与印刷吻合。

---

## p.009（PDF p.9 / 印刷 p.521）

- PNG：audit-redo/p009.png（pngmono 150dpi）；双通道：pdftotext 文本层互证。
- 核对：conditional measures 系统引入句、性质 (1)–(7) 全部陈述、normalization 段（B_1^U=1）、
  atomic/trivial 段（Poincaré recurrence、A-ergodic 二择一、[26, §9]/[17]）、positive entropy 收尾段、
  脚注 2 全文。
- 结果：**PASS±**（4 处标点偏离已修复）
- 差异列表（均已用结构化 Edit 修复）：
  1. 性质 (3)：印刷「∝ (μ_{ux,U})u**, **where …」为逗号，MD 原作 `u .$ where`（句点替代逗号）；
     且行末「map v ↦ vu**.**」句点缺失。已修复为 `( \mu _ { u x , U } ) u$, where … $v \mapsto v u$.`
     （MD 第 169 行）。
  2. 性质 (4) 行末缺句点：印刷「α^t(μ_{x,U})α^{−t}.」；已补 `.`（MD 第 171 行）。
  3. 性质 (5) 行末缺句点：印刷「whenever x, α^t x ∈ X′.」；已补 `.`（MD 第 175 行）。
  4. 缺运行头「THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 521」（系统性，不改）。
- 排版级伪影（登记不改）：`Poincar´e`（重音分解，第 179 行）；性质 (6) 用字面「µ」而非 `$\mu$`；
  (7) 中 `\mathsf{h}_\mu` 替代印刷斜体 h_μ。
- print quirk 备注：印刷行 15「µx,U (B1U ) = 1」正常；印刷 (2) B_ε^U 与 MD 一致。MD 第 187 行
  的性质 (8) 属印刷 p.522 内容，留待 p.010 块核对。
- 其余核对：(1) measurable、(2) μ_{x,U}(B_ε^U)>0、normalization 段、atomic→identity I_k∈U→trivial、
  Poincaré recurrence/unstable manifolds、A-ergodic ⇒ trivial a.s. or nonatomic a.s.、
  (7) stable manifold/h_μ(α^t)/nonatomic a.e.、脚注 2（[20] conventions、[17]、[13]、not a Radon
  measure on X）逐项与印刷吻合。

---
