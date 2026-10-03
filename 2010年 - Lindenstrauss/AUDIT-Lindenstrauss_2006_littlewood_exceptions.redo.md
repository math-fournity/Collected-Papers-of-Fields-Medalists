# Page-by-page redo audit — Lindenstrauss_2006_littlewood_exceptions

- 性质：**Luna 审计重做**。用户 2026-10-02 判定 Luna（Peer-P15, gpt-6-luna/max）对该篇的审计不可信，本文件对其全部页面逐页对照 PDF 原页全量重检，Luna 的旧修复（`AUDIT-Lindenstrauss_2006_littlewood_exceptions.md` 所登记者）一并重新核实；印刷原文（PDF 原页）是唯一裁决源，Luna 旧修复仅是被检对象之一。
- Actor：`Wf-R-P15`（Luna 审计重做 worker）
- Host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置；模型自报 UNKNOWN，按 SOP 身份纪律如实登记）
- PDF：`Lindenstrauss_2006_littlewood_exceptions.pdf`，48 页（印刷页 513–560），SHA-256 `8f32c468132cc9cb3441beed933fb31a3dd2799a6ab46cc79c5050492b198a36`
- 被检 Markdown：`Lindenstrauss_2006_littlewood_exceptions_mineru/Lindenstrauss_2006_littlewood_exceptions__Lindenstrauss_2006_littlewood_exceptions.md`，基线 SHA-256 `aca45d5a32ad8846a41ffa9f5c781715f5827a8a200f52ae3dd39230fff5dd5f`（重做开始时点）
- 日期：2026-10-03 12:08 EDT 开工
- 文本层判定：`pdftotext -f 1 -l 1` 于首页返回清晰完整文本（arXiv 头、刊名卷期页码、标题、作者、摘要、§1 开头、脚注均可读）→ **文本层可用，本重做采用双通道主对账**：pdftotext 逐页提取与 PNG（pngmono 150dpi）视觉核对互证；字形疑难再按需 300dpi 仲裁。
- 证据图：`audit-redo/Lindenstrauss_2006_littlewood_exceptions_p0NN.png`（pngmono 150dpi；本目录与同父目录另一篇的重做证据以短名前缀互斥）。旧 `audit/` 与旧 AUDIT 文件不动。
- 本块范围：p.1–p.9（PDF p.1–9 / 印刷 p.513–521）。

## Page entries

### p.001（PDF p.1 / 印刷 p.513）

- 证据 PNG：`audit-redo/Lindenstrauss_2006_littlewood_exceptions_p001.png`（pngmono 150dpi）；双通道辅证 `pdftotext -f 1 -l 1 -layout`（文本层可用）。
- 核对：题录（期刊卷期页码行、标题、作者行、arXiv 直印水印）、摘要、§1 与 §1.1 标题、§1.1 前三段正文、脚注（NSF 号 DMS-007133 / DMS-0140497 / DMS-0434403 / DMS-0222452、Clay fellow、AIM）。
- 结果：**PASS±**
  - 标题、作者行、摘要（含 "Hausdorff dimension zero"）、§1.1 三段、脚注全文与印刷页逐项吻合。
  - **Luna 旧修复复核**：摘要 `Hausdorf→Hausdorff`（旧 AUDIT p.001 登记）与印刷一致，修复正确，保留。
  - 登记非保留伪影（按 Witten 篇先例，不修）：①印刷页眉期刊行 "Annals of Mathematics, 164 (2006), 513–560" 未保留（MinerU 系统性丢页眉）；②左侧竖排 arXiv 水印 `arXiv:math/0612721v1 [math.DS] 22 Dec 2006` 未保留；③MD 行 11 印刷 `\mathbb{R}^k` 拍平为 `R<sup>k</sup>`（黑体拍平，不误导）。
  - 印刷原文 "unimodular lattices in three space" 与 MD 一致，忠实保留（不作数学预期改写）。
- 备注：本页无需 Edit；MD 段落跨页续接属 MinerU 页流合并（行 15 延入 p.2 内容，p.2 复核）。

### p.002（PDF p.2 / 印刷 p.514）

- 证据 PNG：`audit-redo/Lindenstrauss_2006_littlewood_exceptions_p002.png`（pngmono 150dpi）；双通道辅证 `pdftotext -f 2 -l 2 -layout`。
- 核对：§1.1 末段（Ratner 定理引文 [41]/[42]/[40]/[43]/[28]/[8]）、§1.2 标题与前两段、Conjecture 1.1 (Margulis) 全句、Furstenberg §Σ_{m,n} 段前半、页眉（514 作者行）。
- 结果：**PASS±**（发现并修复 MD 对印刷的 4 处偏差；登记 2 处 print quirk）
  - **print quirk 忠实保留（不改，PNG 视觉确认印刷如此）**：①印刷 "of general unipotents groups"（多 s），MD 一致；②印刷 "Raghunatan's conjecture"（少 h，与 p.1 "Raghunathan" 拼写不一致系印刷本身），MD 一致。
  - **修复（Edit，逐处溯源 p.2 PNG/文本层）**：
    1. 行 19 `a diferent homogeneous action` → `a different`（印刷双 f）；
    2. 行 21 `very diferent from Anosov flows` → `very different`（印刷双 f）；
    3. 行 21 `For$k > 2 .$the` → `For$k > 2,$the`（印刷为逗号，MinerU 误作句点）；
    4. 行 25 `where$n ,$, m are two multi-plicatively` → `where$n , m$are two multiplicatively`（印刷 "n, m"，MinerU 产生双逗号伪影；"multi-plicatively" 系印刷断行连字符并入 MD 应还原）；同句 `multi-plicative semigroup` → `multiplicative semigroup`（同理）。
  - **Luna 旧判定复核**：Luna 将上述 diferent 类仅登记未修、且未发现 `n ,$, m` 双逗号与 `k > 2 .` 逗号误码；重做按 redo 授予「MD 对印刷偏差即修」口径补齐。
  - 登记非保留伪影（不修）：页眉 "514 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS" 未保留；"isomorphic to ℝ" 印刷黑体拍平为 MD 行 21 `isomorphic to R`。
  - Conjecture 1.1 陈述、[16]/[15]/[6]/[17]/[25] 引用号、ℝ^{k−1}-action 与印刷逐项吻合。

### p.003（PDF p.3 / 印刷 p.515）

- 证据 PNG：`audit-redo/Lindenstrauss_2006_littlewood_exceptions_p003.png`（pngmono 150dpi）；双通道辅证 `pdftotext -f 3 -l 3 -layout`。
- 核对：Furstenberg 段后半（ℝ/ℤ 不变集）、"intrinsic difference" 段（M. Rees [44]、[3, §9]、Γ=SL(k,ℤ) 例外 [21]/[25]/[48]）、Conjecture 1.2 (Littlewood (c. 1930)) 与式 (1.1)、⟨w⟩ 最近整距离定义、Theorem 1.3 全句、Corollary 1.4 全句、页眉。
- 结果：**PASS±**（1 处修复）
  - **修复（Edit，溯源 p.3 PNG/文本层）**：行 27 `intrinsic diference` → `intrinsic difference`（印刷双 f，PNG 与文本层一致）。
  - Conjecture 1.2、式 (1.1) `liminf_{n→∞} n⟨nu⟩⟨nv⟩ = 0`、⟨w⟩ 定义、Theorem 1.3（k ≥ 3、one-parameter subgroup positive entropy → algebraic）、Corollary 1.4（not compactly supported；k prime → unique SL(k,ℝ)-invariant）与印刷逐项吻合；[24, §2]、[21] 引用号一致。
  - 印刷 "come from A invariant homogeneous subspaces"（A 后无连字符）MD 忠实保留。
  - 登记非保留伪影：页眉 "THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 515" 未保留。
  - **Luna 旧判定复核**：Luna 登记 `diference` 为 PASS± 未修；重做口径下已修。

### p.004（PDF p.4 / 印刷 p.516）

- 证据 PNG：`audit-redo/Lindenstrauss_2006_littlewood_exceptions_p004.png`（pngmono 150dpi）；双通道辅证 `pdftotext -f 4 -l 4 -layout` / `-raw`；300dpi 仲裁裁片 `audit-redo/300dpi/Lindenstrauss_2006_littlewood_exceptions_p004_theorem-1-5_300dpi.png`、`..._p004_theorem-1-6_300dpi.png`、`..._p004_dim-k-zoom_600dpi.png`、`..._p004_eq-1-3_300dpi.png`。
- 核对：Theorem 1.5（Ξ 定义 + dim 结论）、Cassels–Swinnerton-Dyer [1] 段、badly approximable 段与式 (1.2)、Pollington–Velani [35] 段、线性形式 f_m 定义与乘积display、Theorem 1.6 全句与式 (1.3)、Hee Oh [32] 引出行、页眉。
- 结果：**FAIL（以原图为准）→ 修复后复核 PASS**
  - **FAIL 主项（redo 发现，Luna 未处理）**：Theorem 1.5 结论在 MD 中被伪影损坏为 `dim$. \boldsymbol { H } \boldsymbol { \Xi } = 0$. In$f a c t , \Xi$is…`（下标结构丢失、H/Ξ 误加粗、In fact 误入数学模式）；印刷（300dpi 裁片）为 `dim_H Ξ = 0. In fact, Ξ is…`。已修为 `Then the Hausdorff dimension$\dim _ { H } \Xi = 0$. In fact,$\Xi$is…`。
  - **Luna 旧修复重核（关键）**：Luna 曾删除 Theorem 1.6 句尾游离 `2`（原 MinerU 输出 `…\setminus \Xi _ { k }$2`）。600dpi 终裁（`..._dim-k-zoom_600dpi.png`）确认**印刷即为 "Hausdorff dimension k−1"，k 后无上标 2**（本 PDF 为 arXiv v1 版式；pdftotext -raw 同证 "dimension k−1"，而 p.2 印刷 ℝ^{k−1} 在同一提取中显式带 2，证明文本层不丢上标），该 `2` 无印刷来源，**Luna 的删除正确**，initial suspicion（疑其为 k² 的错位上标）不成立。
  - **其余修复（Edit，逐处溯源）**：
    1. 行 57 段末补句点：`= 3 )` → `= 3 ).`（印刷 "[K : Q] = 3)."）；
    2. 行 59 两处 `lim in$\operatorname { f } …$` 跨界伪影 → `$\liminf …$`（印刷 liminf）；
    3. 行 62 `\text` 内 `(1. 1)` → `(1.1)`（印刷 (1.1)）；
    4. 行 65 `efective` → `effective`（印刷双 f）；
    5. 行 75 Theorem 1.6 句 `…\setminus \Xi _ { k }$` 补回印刷逗号 → `…\setminus \Xi _ { k }$,`（Luna 删 2 时原句无逗号，印刷 "…∖Ξ_k,"）；
    6. 行 83 段末补句点（印刷 "…evaluated on Z^k∖{0}."）。
  - **核实证真**：式 (1.3) 印刷 x、0 为粗体（300dpi 裁片 `..._eq-1-3_300dpi.png`），MD `\mathbf { x }`/`\mathbf { 0 }` 正确保留。
  - 登记非保留伪影：页眉 "516 MANFRED EINSIEDLER, …" 未保留。
  - 线性形式定义 Σ_{j=1}^k m_ij x_j、f_m 乘积 display、[1]/[35]/[32] 引用号与印刷一致。

### p.005（PDF p.5 / 印刷 p.517）

- 证据 PNG：`audit-redo/Lindenstrauss_2006_littlewood_exceptions_p005.png`（pngmono 150dpi）；双通道辅证 `pdftotext -f 5 -l 5 -layout`；300dpi 仲裁裁片 `audit-redo/300dpi/Lindenstrauss_2006_littlewood_exceptions_p005_conjunction_300dpi.png`、`..._p005_tranversals_300dpi.png`。
- 核对：Conjecture 1.7 (Margulis, 1993) 全句、U₁/U₂ 矩阵 display、Hee Oh [33]/[32] 段、§1.3 Measure rigidity 前两段、脚注 1、页眉。
- 结果：**PASS±**（3 处修复；2 处 print quirk 300dpi 确证保留）
  - **修复（Edit，溯源）**：
    1. 行 99 `$\boldsymbol { l a t t i c e ^ { 1 } }$`（整词误入粗体数学模式）→ `lattice$^ { 1 }$`（印刷为斜体正文 lattice 加脚注上标 1）；
    2. 行 99 句末补句点（印刷 "…× GL(2,ℝ)."）；
    3. 行 101 `true for$n \geq 3$ As explained` 补句点 → `$n \geq 3$. As explained`（印刷 "n ≥ 3. As explained"）。
  - **print quirk 300dpi 确证忠实保留（不改）**：①印刷即 "up to **conjunction** in GL(2,ℝ)×⋯×GL(2,ℝ)"（按数学预期应为 conjugation，但印刷如此，MD 一致）；②印刷即 "regarding Hausdorff dimension and **tranversals**"（缺 s，MD 一致）。
  - **Luna 旧判定复核**：Luna 对 conjunction/tranversals 的 print quirk 登记经 300dpi 复核**正确**；但 Luna 修复时把本页两处 Hausdorf→Hausdorff 之外的三处句读/词入数学伪影全部漏掉，重做补齐。
  - 登记非保留伪影（不修）：页眉 "THE SET OF EXCEPTIONS… 517" 未保留；印刷花体 𝒟（set D）拍平为 MD 行 101 斜体 `D`（语义无歧义）。
  - U₁/U₂ 矩阵、[22]/[45]/[12]/[17]/[13] 引用号、×m,×n 半群记法、脚注 1 全文与印刷一致。

### p.006（PDF p.6 / 印刷 p.518）

- 证据 PNG：`audit-redo/Lindenstrauss_2006_littlewood_exceptions_p006.png`（pngmono 150dpi）；双通道辅证 `pdftotext -f 6 -l 6 -layout`。
- 核对：条件测度/foliations 段、positive entropy 例外段（δ-measure、three torus、[17]）、[17] 证明附加假设段（singular direction、weak* limits）、"two new methods" 过渡句、first method 段（[3]、[4]、Haar measure、dim ≤ 1）、third author 段开头（[20]、Host [9]）、页眉。
- 结果：**PASS±**（4 处修复）
  - **修复（Edit，溯源 p.6 PNG/文本层）**：
    1. 行 111 `about$\mu .$. Hence`（双句点伪影）→ `about$\mu$. Hence`（印刷单句点）；
    2. 行 113 `suficient` → `sufficient`（印刷双 f）；
    3. 行 115 `dificulty` → `difficulty`（印刷双 f）；
    4. 行 119 `A diferent approach` → `A different`（印刷双 f）。
  - 登记非保留伪影（不修）：页眉 "518 MANFRED…" 未保留；印刷 ℝ-split（两处）黑体拍平为 MD `R-split`。
  - weak<sup>∗</sup> limits 上标星保留正确；[3]/[4]/[17]/[20]/[9] 引用号与 "Hausdorff dimension at most 1" 结论与印刷一致。
