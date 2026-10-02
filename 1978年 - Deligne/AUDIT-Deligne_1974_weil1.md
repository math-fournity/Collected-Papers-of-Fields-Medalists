# AUDIT — Deligne_1974_weil1

## 任务与输入基线

- 状态：候选审计进行中；该文件仅是 Peer-P01 的篇级候选，待 Master-Luna 按精确 source OID 复核和集成。
- 身份：actor=Peer-P01; model=gpt-6-luna; effort=max。
- 共同基线：`e04c4a9603818cfa2d71271942f696115783c33b`；本 worktree 为 detached HEAD。Master-Luna 是唯一 `CANONICAL_INTEGRATOR`。
- PDF：`Deligne_1974_weil1.pdf`；`pdfinfo` 报告 36 页、Creator `NUMDAM`、Producer `pdfTeX-1.40.16`。SHA-256：`8392b345d4854e6dc55fb42cfc0b616d941935983723627237239a87348f42e5`。
- MinerU Markdown：`Deligne_1974_weil1_mineru/Deligne_1974_weil1__Deligne_1974_weil1.md`；修复前 SHA-256：`bc81d9e1dd640c8ed63487fa5db4c1e9b214379b52c2dbe3556f7d2b49ac9e89`；1501 行、109356 字节。执行 `/Users/aurolafly/codex/tools/check_file_baseline.sh` 的结果为 `TRACKED_CLEAN`，HEAD=`e04c4a960381`，无 dirty 状态。
- 输入模式：born-digital；`pdftotext -layout` 得到 89508 字节、36 个非空页段，未发现 U+FFFD。MinerU `structured_content.json` 有 36 页、metadata 标明 MinerU 3.4.4。PDF 与导出目录/Markdown 的命名、题名、作者、期刊卷年页码（IHÉS 43，1974，273–307）和 Numdam item URL 相符；该 MinerU 目录未包含 `origin.pdf`，故输入对应关系由这些来源字段及逐页正文对账建立，不声称存在独立 PDF hash 收据。
- 审计方法：逐页将 PDF 文本层与 Markdown 正文对账；题录页及 1–2 页密集数学内容另做 150dpi 原页抽验。pdftotext 丢失或压平、以及无法从文本层唯一辨认的字形，用原页 300dpi 裁片裁决并纳入 `audit/300dpi/`。正文修复、整份回读及只读终验已完成，详细结果见文末“修复后回读与逐页修复登记”。

## 逐页审计

### p.001（PDF p.1 / 封面，无印刷页码）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 15:48 EDT。
- PNG：`audit/150dpi/Deligne_p001.png`（pngmono 150dpi）。
- 核对：PDF p.1 与 Markdown 开头题录段；作者、题名、期刊/卷年/页码、Numdam URL、版权声明和法律文本逐项相符。依据为 PDF 可搜索文本层与 150dpi 原页图。
- 结果：PASS±。核心题录及法律文字吻合；Markdown 未保留印刷页顶的期刊刊头及页底 Numdam 数字化项目标识/说明，均为封面页装饰/来源标记。

### p.002（PDF p.2 / 印刷 p.273）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 15:52 EDT。
- PNG：`audit/300dpi/Deligne_p002_eq1.1.1.png`（原 PDF p.2 的 300dpi 数学裁片）。
- 核对：PDF p.2 与 Markdown 题名、SOMMAIRE、引言、§1 开头及公式 (1.1.1)；段落文字与目录项目吻合，核心信息完整。依据为逐页 PDF 文本层及公式的 300dpi 原页裁片。
- 结果：FAIL。PDF 印刷式 (1.1.1) 为阿拉伯数字，公式为 `\zeta_X(s)=\prod_{x\in|X|}(1-N(x)^{-s})^{-1}`；Markdown 把公式号写成 `I.I.I`，并把因子中的数字 `1` OCR 成大写 `I`。须在全篇审计后按裁片逐处修正。Markdown 未保留页顶 running title 与页脚印刷页码 273/35。

### p.003（PDF p.3 / 印刷 p.274）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 15:53 EDT。
- PNG：`audit/300dpi/Deligne_p003_eq1.1.2-1.1.3.png`、`audit/300dpi/Deligne_p003_Identifions.png`（PDF p.3 的 300dpi 原页裁片）。
- 核对：PDF p.3 与 Markdown 的 §1.1 余段、公式 (1.1.2)–(1.1.3)、§1.2–1.3 及 §1.4 起首；段落主题、引用和次序相符。公式及拼写以两个 300dpi 原页裁片终裁。
- 结果：FAIL。印刷式 (1.1.2) 中 `1 - t^{deg(x)}` 的数字 `1` 在 Markdown 中被写成大写 `I`；印刷式 (1.1.3) 的编号为 `(1.1.3)`，Markdown 写成 `I.I.3`；§1.4 起句印刷为 `Identifions`，Markdown 写成 `Identifons`。待全篇审计后修复。Markdown 未保留 running head 与印刷页码 274。

### p.004（PDF p.4 / 印刷 p.275）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 15:57 EDT。
- PNG：`audit/300dpi/Deligne_p004_fixed_points.png`、`audit/300dpi/Deligne_p004_Lefschetz.png`（PDF p.4 的 300dpi 原页裁片）。
- 核对：PDF p.4 与 Markdown §1.4(a)–(d)、公式 (1.4.1)、§1.5 的 Lefschetz 公式及对数导数公式 (1.5.1)–(1.5.2)；陈述次序相符。所有报告的数字/符号差异均由原页裁片终裁。
- 结果：FAIL。§1.4(b) 印刷为 `F_{q^n}`，Markdown 写作 `F_{\\sigma^n}`；两条交错迹公式 (1.5) 与 (1.5.1) 印刷为 `(-1)^i`，Markdown 均误作 `(-i)^i`；正文的 `dF=0` 两次被写成 `dF=o`；(1.5.2) 的分母 `1-t^{deg(x)}` 中，数字 `1` 被写成大写 `I`。待全篇审计后逐处修复。公式 (1.5.3) 中表示恒等算子的 `I` 与印刷相符，保留。Markdown 未保留 running head 与印刷页码 275。

### p.005（PDF p.5 / 印刷 p.276）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:00 EDT。
- PNG：`audit/300dpi/Deligne_p005_Theorem_1.6.png`、`audit/300dpi/Deligne_p005_formula_1.5.4.png`、`audit/300dpi/Deligne_p005_Pi_definition.png`（PDF p.5 的 300dpi 原页裁片）。
- 核对：PDF p.5 与 Markdown 公式 (1.5.4)、定理 (1.6)、引理 (1.7)、蕴含证明开头、Hankel 行列式定义及 `P_i(t)` 定义；定理陈述、指数 `i/2`、行列式指标与 H_k 的项/范围逐项相符。报告的恒等算子符号依据原页裁片终裁。
- 结果：FAIL。定理 (1.6) 印刷特征多项式为 `det(t·1 − F*, H^i(X,Q_ℓ))`，Markdown 写成 `det(t.i—F*,...)`，将恒等算子符号 OCR 成小写 `i` 并把减号写成 em dash；末尾 `P_i(t)` 的行列式印刷为 `det(1−F*t,...)`，Markdown 将恒等算子误作小写 `i`。全篇审计结束后按原页修正。Markdown 未保留 running head 与印刷页码 276。

### p.006（PDF p.6 / 印刷 p.277）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:02 EDT。
- PNG：`audit/300dpi/Deligne_p006_section1.9.png`（PDF p.6 的 300dpi 原页裁片）。
- 核对：PDF p.6 与 Markdown 中 `P(t)`/`Q(t)` 的奇偶指标乘积、根的模长判据、§1.8–1.10 及可构造层定义。奇偶分组、`q^{-i/2}`、Hankel 证明结尾均相符；记号以 300dpi 原页裁片终裁。

### p.007（PDF p.7 / 印刷 p.278）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:09 EDT。
- PNG：`audit/300dpi/Deligne_p007_diagram.png`、`audit/300dpi/Deligne_p007_Lefschetz.png`（PDF p.7 的 300dpi 原页裁片）。
- 核对：PDF p.7 与 Markdown §1.10 结尾、§1.11 的交换图和文字、§1.12 的 Lefschetz 公式及迭代公式，以及 §1.13 起首。Markdown 内嵌交换图与印刷图相符；文字/公式以原页裁片终裁。

### p.008（PDF p.8 / 印刷 p.279）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:13 EDT。
- PNG：`audit/300dpi/Deligne_p008_Zeta_L.png`、`audit/300dpi/Deligne_p008_Frobenius_dictionary.png`（PDF p.8 的 300dpi 原页裁片）。
- 核对：PDF p.8 与 Markdown 公式 (1.14.1)–(1.14.3)、§1.15 的 Frobenius 字典、关系 (1.15.1)–(1.15.2) 及末尾 Galois 记号公式。公式中的固定点集合和编号以裁片终裁。

### p.009（PDF p.9 / 印刷 p.280）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:16 EDT。
- PNG：`audit/300dpi/Deligne_p009_orientation.png`、`audit/300dpi/Deligne_p009_tate_twist.png`（PDF p.9 的 300dpi 原页裁片）。
- 核对：PDF p.9 与 Markdown §2.1(a)–(c)、定向层和 §2.2 的 Tate twist、转移映射及其定义。两类已报告字形差异以原页裁片终裁。

### p.010（PDF p.10 / 印刷 p.281）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:19 EDT。
- PNG：`audit/150dpi/Deligne_p010.png`（题名页与密集数学页抽验中的一页，pngmono 150dpi）；`audit/300dpi/Deligne_p010_twist.png`、`audit/300dpi/Deligne_p010_euler.png`（原页裁片）。
- 核对：PDF p.10 与 Markdown §2.2 结尾、定理 (2.3)、(2.4)、(2.5)、公式 (2.6) 及其函数方程；维数、Frobenius 特征值关系和函数方程指数均吻合，具体符号以全页图及 300dpi 裁片核验。

### p.011（PDF p.11 / 印刷 p.282）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:22 EDT。
- PNG：`audit/300dpi/Deligne_p011_epsilon.png`、`audit/300dpi/Deligne_p011_duality.png`、`audit/300dpi/Deligne_p011_functor.png`（PDF p.11 的 300dpi 原页裁片）。
- 核对：PDF p.11 与 Markdown §2.6 的 ε 分段定义、§2.7–2.10 的带扭结对偶公式、以及 §2.11 起首；裁片覆盖 ε、层记号、表示函子和轨道余不变量公式。

### p.012（PDF p.12 / 印刷 p.283）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:25 EDT。
- PNG：`audit/300dpi/Deligne_p012_duality_twist.png`、`audit/300dpi/Deligne_p012_bibliography_3.1.png`（PDF p.12 的 300dpi 原页裁片）。
- 核对：PDF p.12 与 §2.11 余句、定理 (2.12)、Tate twist 定义 (2.13)、文献说明 (2.14) 和 §3.1 起首。裁片逐项核验了对偶、twist、引文编号和层记号。

### p.013（PDF p.13 / 印刷 p.284）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:27 EDT。
- PNG：`audit/300dpi/Deligne_p013_weight_lemmas.png`（PDF p.13 的 300dpi 原页裁片）。
- 核对：PDF p.13 与 Markdown §3.1 的权重示例、定理 (3.2)、引理 (3.3)–(3.6)；权重指数 β/2、正迹幂 2k、正系数结论及收敛半径不等式相符。差异以公式裁片终裁。

### p.014（PDF p.14 / 印刷 p.285）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:29 EDT。
- PNG：`audit/300dpi/Deligne_p014_weight_bound.png`（PDF p.14 的 300dpi 原页裁片）。
- 核对：PDF p.14 与 Markdown 的 (3.7) 配对映射、coinvariants 同构、H_c^2/U 和有理函数分母、极点位置及后续权重不等式；分区、2k 张量幂和所有指数以原页裁片终裁。

### p.015（PDF p.15 / 印刷 p.286）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:32 EDT。
- PNG：`audit/300dpi/Deligne_p015_rank_product.png`、`audit/300dpi/Deligne_p015_exact_sequence.png`（PDF p.15 的 300dpi 原页裁片）。
- 核对：PDF p.15 与 Markdown 推论 (3.8) 的函数方程特征值界、收敛估计，以及推论 (3.9) 的谱界和长正合列片段；幂 `β/2`、`1/2` 和点数估计相符。

### p.016（PDF p.16 / 印刷 p.287）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:33 EDT。
- PNG：`audit/300dpi/Deligne_p016_vanishing_cycle_table.png`（PDF p.16 的 300dpi 原页裁片）。
- 核对：PDF p.16 与推论 (3.9) 的上下界、§4.1 的局部 Lefschetz 条件、特化映射/单值变换、vanishing-cycle exact sequence 和 (n\bmod 4) 符号表。公式、映射和表内各行数值吻合。

### p.017（PDF p.17 / 印刷 p.288）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:35 EDT。
- PNG：`audit/300dpi/Deligne_p017_specialization.png`、`audit/300dpi/Deligne_p017_vanishing_cycle.png`（PDF p.17 的 300dpi 原页裁片）。
- 核对：PDF p.17 与 §4.2 的专化映射及惯性群表示、§4.3 vanishing-cycle 上同调等式、exact sequence、奇维情形的惯性群作用。印刷映射的箭头方向和符号以裁片终裁。

### p.018（PDF p.18 / 印刷 p.289）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:38 EDT。
- PNG：`audit/300dpi/Deligne_p018_inertia_signs.png`、`audit/300dpi/Deligne_p018_pencil.png`（PDF p.18 的 300dpi 原页裁片）。
- 核对：PDF p.18 与 (4.3)(B) 的二次情形惯性作用、(4.4) 的常值层/短正合列结论及 (5.1) 的 Lefschetz pencil 参数和图式；短正合列对象与图式方向相符。

### p.019（PDF p.19 / 印刷 p.290）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:39 EDT。
- PNG：`audit/300dpi/Deligne_p019_loops.png`（PDF p.19 的 300dpi 原页裁片）。
- 核对：PDF p.19 与 §5.1 泛型 pencil 的 A/B/C 条件、§5.2 的互不相交环路/monodromy 作用、命题 (5.3) 和定理 (5.4) 起首；Markdown 内嵌环路图与 PDF 原图核对相符，公式 (5.2.1) 记号一致。

### p.020（PDF p.20 / 印刷 p.291）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:41 EDT。
- PNG：`audit/300dpi/Deligne_p020_dual_variety.png`、`audit/300dpi/Deligne_p020_abstract_pencil.png`（PDF p.20 的 300dpi 原页裁片）。
- 核对：PDF p.20 与定理 (5.4) 的 dual variety 论证、推论 (5.5) 的不变子空间论证，以及 §5.6 抽象 Lefschetz pencil 的起首条件。monodromy、正合列和图式方向相符。

### p.021（PDF p.21 / 印刷 p.292）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:43 EDT。
- PNG：`audit/300dpi/Deligne_p021_monodromy.png`（PDF p.21 的 300dpi 原页裁片）。
- 核对：PDF p.21 与 (5.7) Veronese embedding 维数/次数、(5.8) 的 tame ramification 前提及非零 vanishing-cycle 分支 a)(1)–(3)；整数参数和不变子空间等式吻合。

### p.022（PDF p.22 / 印刷 p.293）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:45 EDT。
- PNG：`audit/300dpi/Deligne_p022_Margulis.png`（PDF p.22 的 300dpi 原页裁片）。
- 核对：PDF p.22 与零 vanishing-cycle 情形的短正合列、(5.9) 的 symplectic form、Kajdan-Margulis 论证和 Lemma (5.11) 的生成条件/指数公式；上同调次数、twist 和符号关系均相符。

### p.023（PDF p.23 / 印刷 p.294）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 16:47 EDT。
- PNG：`audit/300dpi/Deligne_p023_hypersurface_zeta.png`、`audit/300dpi/Deligne_p023_start_6.1.png`（PDF p.23 的 300dpi 原页裁片）。
- 核对：PDF p.23 与 Remark (5.12) 的 hypersurface zeta 公式、§5.13 引文及 §6.1 开头；上同调次数、Tate twist、行列式及 page transition 均对账。

### p.024（PDF p.24 / 印刷 p.295）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 17:00 EDT。
- PNG：`audit/300dpi/Deligne_p024_rationality_6.1-6.4.png`（PDF p.24 的 300dpi 原页裁片）。
- 核对：PDF p.24 与 diagram (6.1.1)、§6.1 的 Lefschetz pencil 假设、exceptional local system pairing、定理 (6.2)、corollary (6.3) 及 lemma (6.4) 的 determinant 分解；数值界与配对指数相符。

### p.025（PDF p.25 / 印刷 p.296）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-01 20:59 EDT。
- PNG：`audit/300dpi/Deligne_p025_rational_factors.png`（PDF p.25 的 300dpi 原页裁片）。
- 核对：PDF p.25 与 (6.4) 的局部 Euler factors、(6.5) 的分子/分母多项式、Proposition (6.6) 与公式 (6.6.1) 的不可约分母陈述；系数域与各指数按原页终裁。

### p.026（PDF p.26 / 印刷 p.297）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 00:13 EDT。
- PNG：`audit/150dpi/Deligne_p026.png`（密集数学页全页抽验，pngmono 150dpi）；`audit/300dpi/Deligne_p026_Proposition_6.8.png`、`audit/300dpi/Deligne_p026_Proposition_6.9_6.10.png`（原页裁片）。
- 核对：PDF p.26 与 Lemma (6.7)、Proposition (6.8)、论证 (6.9) 及 (6.10) 开头；指数、family sizes 和 rationality 结论逐项核对。

### p.027（PDF p.27 / 印刷 p.298）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 00:17 EDT。
- PNG：`audit/300dpi/Deligne_p027_theorem_7.1.png`（PDF p.27 的 300dpi 原页裁片）。
- 核对：PDF p.27 与 (6.10)–(6.13) 的 similitude subgroup、measure-zero argument 和 Čebotarev 推论，以及 Lemma (7.1) 的范围与界；幂指数和不等式相符。

### p.028（PDF p.28 / 印刷 p.299）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 00:21 EDT。
- PNG：`audit/300dpi/Deligne_p028_blowup_leray.png`（PDF p.28 的 300dpi 原页裁片）。
- 核对：PDF p.28 与 Lemma (7.1) 归纳步骤、blow-up 上同调分解、Leray spectral sequence 及其项 A/B；次数、谱序列指标和映射均相符。

### p.029（PDF p.29 / 印刷 p.300）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 00:41 EDT。
- PNG：`audit/300dpi/Deligne_p029_exact_sequences.png`、`audit/300dpi/Deligne_p029_lemma_7.2.png`（PDF p.29 的 300dpi 原页裁片）。
- 核对：PDF p.29 与归纳证明中的 Gysin/无 vanishing-cycle 两种分支、(7.1.2′)–(7.1.5′) 长正合列、Lemma (7.2) 的绝对值等式；对象、次数与 q 指数对账。

### p.030（PDF p.30 / 印刷 p.301）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 00:46 EDT。
- PNG：`audit/300dpi/Deligne_p030_W_and_bound.png`、`audit/300dpi/Deligne_p030_Theorem_8.1.png`（PDF p.30 的原页裁片）。
- 核对：PDF p.30 与证明 (7.2)⇒(1.7) 的 W 归约、(7.3) 的 tensor-power bounds 及定理 (8.1) 陈述；定理的点数界和上同调分解起首相符。

### p.031（PDF p.31 / 印刷 p.302）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 00:50 EDT。
- PNG：`audit/300dpi/Deligne_p031_theorem_8.1.png`、`audit/300dpi/Deligne_p031_modular_8.2.png`（PDF p.31 的 300dpi 原页裁片）。
- 核对：PDF p.31 与计数公式 (8.1)、模形式定理 (8.2) 的变换律/Hecke bound/特征方程、以及定理 (8.4) 的初始条件；指数和不等式界逐项核对。

### p.032（PDF p.32 / 印刷 p.303）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 00:57 EDT。
- PNG：`audit/300dpi/Deligne_p032_equation_8.4.1.png`、`audit/300dpi/Deligne_p032_equation_8.4.3_lemma8.5.png`（PDF p.32 的 300dpi 原页裁片）。
- 核对：PDF p.32 与 Theorem (8.4) 的 additive character、Artin–Schreier 覆盖、Frobenius trace 计算、公式 (8.4.2)–(8.4.3) 及 Lemma (8.5) 的非退化 pairing。

### p.033（PDF p.33 / 印刷 p.304）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 01:03 EDT。
- PNG：`audit/300dpi/Deligne_p033_trace.png`（PDF p.33 的 300dpi 原页裁片）。
- 核对：PDF p.33 与 (8.4) 的 injectivity argument、trace identity、diagram (8.6.1) 及 Lemmas (8.7)–(8.9) 的 local equations/resolution argument；图中投影箭头、divisor equation 和局部幂次相符。

### p.034（PDF p.34 / 印刷 p.305）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 01:09 EDT。
- PNG：`audit/300dpi/Deligne_p034_relative_compactification.png`（PDF p.34 的 300dpi 原页裁片）。
- 核对：PDF p.34 与 §8.10 的 relative compactification 图、locally constant higher direct images 及 Künneth reduction；diagram endpoints/arrows 和 sheaf image decomposition 以裁片终裁。

### p.035（PDF p.35 / 印刷 p.306）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 01:15 EDT。
- PNG：`audit/300dpi/Deligne_p035_Kunneth_conductor.png`（PDF p.35 的 300dpi 原页裁片）。
- 核对：PDF p.35 与 (8.11) 的 n=1 降维和 extension-by-zero/direct-image 性质、Euler characteristic 和 Swan conductor (8.12)–(8.13)；分数幂/导数身份与参考文献条目相符。

### p.036（PDF p.36 / 印刷 p.307）
- 身份/时间：actor=Peer-P01; model=gpt-6-luna; effort=max; 2026-10-02 01:22 EDT。
- PNG：`audit/300dpi/Deligne_p036_bibliography.png`（PDF p.36 的 300dpi 题录/收稿信息裁片）。
- 核对：PDF p.36 与参考文献 [4]、SGA 4/5/7 条目及 manuscript received date；作者名、刊物、卷页、出版年和日期相符。
- 结果：PASS±。SGA 5 题名中印刷的符号为 script ell `ℓ`，Markdown 写作 plain `l-adique`，记录为符号字体差异，便于检索时可规范为 `ℓ-adique`；参考文献作者小型大写被排成普通大小写，不改变姓名。Markdown 未保留 running head 与印刷页码 307。

## 修复后回读与逐页修复登记

- 修复对象：仅 Deligne_1974_weil1_mineru/Deligne_1974_weil1__Deligne_1974_weil1.md；PDF 原件和其它篇目未改。
- 修复前 Markdown SHA-256：bc81d9e1dd640c8ed63487fa5db4c1e9b214379b52c2dbe3556f7d2b49ac9e89。
- 修复后 Markdown SHA-256：fdada5f38196e5f3b46feca4a0a94ef912ffe7b4bda03c4081ab47b8ece3c6e4；1496 行、108998 字节。
- 正文修复 commit：c97236172626cdead2500704020fda71e2e67df2；Git 统计为 127 insertions / 133 deletions，仅含目标 Markdown。
- 原逐页 commit subject 记录为 31 个 FAIL、5 个 PASS±。最终复核发现 p.016 表头的 I 是数字 1，p.022 的 “caractéristique o” 是数字 0；两页原 PASS± 分级据原页证据重分类为 FAIL。故修复前分级在复核后为 33 FAIL / 3 PASS±。历史 page commit 不改写。
- 修复覆盖：36 页均已逐页核查；34 页的正文有手工修订，p.001 和 p.019 未发现需改正文的内容错误。以下分级指修复前逐页结果（含上述两项重分类）。

| PDF 页 | 修复前复核分级 | 修订与原页复核点 |
|---|---|---|
| p.001 | PASS± | 未改正文；封面刊头、数字化项目标识属于页面布局信息。 |
| p.002 | FAIL | 公式号 (1.1.1)；zeta 因子的标量 1。 |
| p.003 | FAIL | (1.1.2) 因子的标量 1；公式号 (1.1.3)；“Identifions” 拼写。 |
| p.004 | FAIL | F(q^n)；两处 Lefschetz 符号 (-1)^i；两处 dF=0；(1.5.2) 分母标量 1。恒等算子 I 保留。 |
| p.005 | FAIL | 定理 (1.6) 的特征多项式符号 t·I−F*；P_i(t) 中的恒等算子 I；移除误挂在 (1.5.3) 的页脚 275。 |
| p.006 | FAIL | 六处 Q_t 改为 Q_ell、一处 Z_t 改为 Z_ell；§1.9(b) 两处 sheaf F 改为 script F。 |
| p.007 | FAIL | §1.12 的 script F_0/F 记号；script F_{F^n(x)}；(1.12) 与 (1.12.1) 两个 Lefschetz 符号 (-1)^i。 |
| p.008 | FAIL | 公式号 (1.14.1)；(1.14.2) 分式结构和集合 X^(F^n)；交叉引用 (1.15.1)；移除误挂在末式的页脚 279。PDF 印刷分母中可见的 dfn 按源文保留。 |
| p.009 | FAIL | 1/4；Tate twist 中误录为 I 的数字 1；“caractéristique 0”。 |
| p.010 | FAIL | Euler 特征的 (-1)^i；Q_t 改为 Q_ell；epsilon 中的标量 1 与 (-1)^N。 |
| p.011 | FAIL | §§2.8–2.11 的 script F 记号、Q_ell 记号和 Tate twist (-1)。 |
| p.012 | FAIL | (2.12) 的 script F dual(1) 对偶和 twist；(2.13) 的 Z/ell^n(1)；书目指引 Q_ell、H_c^i；特征零。 |
| p.013 | FAIL | script F_0/F 记号、Q_ell(r)；行列式恒等算子 I；(3.3) 张量幂 2k；(3.4) 两处张量幂指数。 |
| p.014 | FAIL | H_c^2/H_c^0 的张量幂和 Tate twist；极点、倒数及分母中的标量 1；行列式中的恒等算子 I 保留。 |
| p.015 | FAIL | 行列式恒等算子 I；特征多项式乘积的标量 1；rank(script F)；j_! = prolongement par 0。 |
| p.016 | FAIL（重分类） | vanishing-cycle 符号表头 I 改为数字 1；原逐页 commit 的 PASS± 是漏判。 |
| p.017 | FAIL | 专化映射改为左向同构箭头；Z_ell(1)。 |
| p.018 | FAIL | inertia character 的值域和值改为 {±1}, 1, -1；“around 0”；pencil 参数线 double-struck D 改为 D。 |
| p.019 | PASS± | 未改正文；环路图与 PDF 原图相符。 |
| p.020 | FAIL | incidence variety 改为 X×dual P；5.4 的 dual projective/dual variety 记号改为 dual P/dual X；5.6 的参数线 double-struck D 改为 D。 |
| p.021 | FAIL | Q_t 改为 Q_ell；“caractéristique 0”。 |
| p.022 | FAIL（重分类） | Lemma 5.11 的 “caractéristique o” 改为数字 0；原逐页 commit 的 PASS± 是漏判。 |
| p.023 | FAIL | zeta 分母 (1−q^i t)；E∩E-perp={0}；dim P_0≥1。 |
| p.024 | FAIL | P_0 维数下界改为 1；参数线 D；五处 Q_t 改为 Q_ell；“Soiert” 改为 “Soient”；Lemma 6.4 两个多项式因子的标量 1。 |
| p.025 | FAIL | Qbar_t 改为 Qbar_ell；6.5–6.6 局部因子的标量 1；移除混入句中的页脚 296 及续页浮入正文的 297。命题 6.8 印刷前提中的 delta_i 按源文保留。 |
| p.026 | FAIL | 命题 6.8 的界改为 1≤i,j，R/S 与除式中的标量 1；6.10 的 F_u 改为 script F_u；measure/density 中的零值写为 0。命题 6.8 的 delta_i 指标按印刷原文保留。 |
| p.027 | FAIL | Lemma 7.1 公式号改为 (7.1.1)。 |
| p.028 | FAIL | Q_t 改为 Q_ell；Tate twist 中的标量 1。 |
| p.029 | FAIL | exact sequences 中的 o 改为 0；script E/F sheaf 记号及 H^1(D,R^n f_*Q_ell)；长正合列编号恢复为 (7.1.2')–(7.1.5')。 |
| p.030 | FAIL | W(X_0,i)；Q_ell；0≤i≤n；(7.3) 第一条界右端指数从 −1/2 改为 +1/2。 |
| p.031 | FAIL | (-1)^n；点数式中的 P^n；c congruent 0 mod N；维数 k−1。 |
| p.032 | FAIL | 加法特征公式号改为 (8.4.1)；张量基域改为 Q_ell。 |
| p.033 | FAIL | trace 恒等式系数 I/p 改为 1/p。 |
| p.034 | FAIL | sheaf F_{j,s} 改为 script F_{j,s}；direct-image functor 下标 1 改为 !。图式 X_S→Z_S 与印刷原页一致，未添 tilde。 |
| p.035 | FAIL | n=i 改为 1；u_i 改为 u_!；Euler characteristic 改为 1−d。 |
| p.036 | PASS± | SGA 5 题名中的 l-adique 改为 ℓ-adique；作者小型大写未模拟，running head/页码仍未收录。 |

### 全篇复读与检查

- 正文最后一次手工复读范围：目标 Markdown 第 1–1496 行，完整覆盖首行题录至 manuscript-received 末行；复读时逐页回看 PDF 文本层、150dpi 抽样页及 300dpi 原页裁片。确定的字形裁决图仍位于本篇 audit/300dpi/；未使用外部 PDF 或 MinerU 解析结果替代原件。
- PDF SHA-256：8392b345d4854e6dc55fb42cfc0b616d941935983723627237239a87348f42e5；最终 Markdown SHA-256：fdada5f38196e5f3b46feca4a0a94ef912ffe7b4bda03c4081ab47b8ece3c6e4。
- 只读终验：git diff --check PASS；针对已识别 OCR 模式的只读残余扫描无未处置项。扫描中保留的 dfn（p.008）和命题 6.8 的 delta_i（p.026）均经原页确认，是印刷源文 quirk。
- 修改遵守本项目 Markdown 修复 SOP：差异逐处对照 PDF 页/裁片并用 apply_patch 手工编辑目标 Markdown；脚本只用于只读清点。未运行 MinerU、未改 PDF、未改根级索引/进度/其它论文，也未运行与本项无关的 tests。
- 修复后未发现未解决的正文内容差异。已披露的剩余投影差异是非内容版式信息；原文 dfn 和 delta_i 保留为 source quirk。SOP 偏离：无。
- Candidate 仍待 Master-Luna 按精确 source commit 复核并集成；Peer-P01 未修改 root-level current truth、未 push。
