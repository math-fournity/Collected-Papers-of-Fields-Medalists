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
