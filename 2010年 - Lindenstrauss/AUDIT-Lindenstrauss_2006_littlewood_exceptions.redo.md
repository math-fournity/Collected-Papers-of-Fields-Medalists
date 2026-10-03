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
