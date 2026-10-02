# AUDIT-frey1986.redo — Luna 审计重做（逐页对照 PDF 全量重检）

- 性质：Luna 审计重做（用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核）
- actor：Wf-R-P06
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF SHA256：0f092a804000ad55d39506015516777fee288a4b8de65bb9e41a738cb6a87ab0
- MD 基线 SHA256（重做起点，frey1986_mineru/frey1986__frey1986.md）：dfee1701475ac1593bb55affe56e397537db988b9cf2788d22971602d481835f
- 日期时间：2026-10-02 16:11 EDT 起
- 范围：本文件块只覆盖 p.1–p.9（共 40 页，后续块由其他 worker 接续）
- 证据图：`1998年 - Wiles/audit-redo/p0NN.png`（gs pngmono 150dpi；旧 `audit/` 不动）
- 文本层判定：`pdftotext -f 1 -l 1` 输出散文大体可读但数学区域严重 OCR 失真
  （例：`z_1·z_2·z_3 ≠ 0` → `21-22-23 + O`、`C_{F_n}` → `CF`），
  **判定=部分可用（仅散文/结构旁证，公式不可用）**；主裁决 = 150dpi PNG 视觉逐页核对。
- 分级与纪律：按 AUDIT-SOP；print quirk/错字忠实登记不改正；修复用结构化 Edit 逐处修改并逐页 commit；
  禁止写根级文件，进度以本文件页条目 + 逐页 commit 承载（AUDIT-PROGRESS.log 属根级，本块不写）。

---

## p.001（PDF p.1 / 印刷 p.1）
- PNG：audit-redo/p001.png（pngmono 150dpi）
- 核对：题录（标题两行下划线/By/Gerhard Frey）；I. Introduction 开篇；式 $C_{F_n}: z_1^n - z_2^n = z_3^n$；
  解的定义句（$(z_1,z_2,z_3)\in\mathbb{Z}^3$、$z_1\cdot z_2\cdot z_3\neq 0$、$\gcd=1$）；
  $n=1,2$ 无穷多解 / $n=3$ 无解 / $n>3$ 有限多解句；CONJECTURE F_n 陈述（$n\geq 3$ 无解）。
- 结果：PASS
- 备注：①300dpi 仲裁（/tmp 裁剪比对）：印刷 CONJECTURE 后下标为 **n**（非 p），MD line 21 `$F_{n}$` 忠实；
  ②印刷把 Faltings 印作 **"Falting's theorem"**（300dpi 仲裁确认，专名少 s），MD 忠实保留，属 print quirk 不改；
  ③文本层 pdftotext 该页数学区失真（`21-22-23 + O` 等），未作裁决依据。本次无 MD 修改。

---

## p.002（PDF p.2 / 印刷 p.2）
- PNG：audit-redo/p002.png（pngmono 150dpi）
- 核对：n=p 素数句；cyclotomic field $\mathbb{Q}(\zeta_p)$ 句；Kummer/regular case 句（cf. [1]）；
  Galois group $G_{\mathbb{Q}(\zeta_p)}$、$\mathrm{Gl}_1(C)_p$ implies F̲_p 句；
  ρ dimension 2 / points of order p 句；"Fermat type"（see II）、stable over Q（cf. [2]）、Theorem on p. 15 句。
- 结果：PASS±（修复 1 处后）
- 差异与处置：
  1. 【已修复】MD line 49 `$F_{p}$` → `$\underline{F}_{p}$`：300dpi 仲裁印刷为 "implies **F̲**_p."（F 有下划线，
     与 line 27 的 F̲_p 同指猜想；下划线丢失会误为普通符号）。证据：audit-redo/p002.png + 300dpi 裁剪比对。
  2. 【登记不改】line 67 "stable" 印刷有下划线（强调关键词），MD 拍平为 "stable"：排版级伪影，按 SOP 默认不改。
  3. 【登记不改】同一页 $\zeta_{\mathrm{p}}$（line 29）/$\zeta_{\mathfrak{p}}$（line 39）/$\zeta_{p}$（line 47）字体变体混排，
     同指同一对象：MinerU 已知 Fraktur 混排瑕疵，不影响数学内容。
  4. 【print quirk】印刷作 "There is our motivation to relate…"（300dpi 仲裁确认，语法疑为 This 之误但系印刷原文），
     MD 忠实保留。
  5. 【150dpi 误读澄清】末行经 300dpi 仲裁为 "the Theorem on p. 15)."（无重音），MD 忠实；150dpi 下疑似
     "Théorème" 系噪点误读。
- 备注：页眉 "2　G. Frey" 为页件未入 MD，正常。本次修复后五点比对无内容错误。

---

## p.003（PDF p.3 / 印刷 p.3）
- PNG：audit-redo/p003.png（pngmono 150dpi）
- 核对：Taniyama–Shimura 句；展示式 $\varphi: X_0(N) \longrightarrow E$；geometric conductor 句；
  $\varphi^{*}\omega$→weight 2 modular form 句；$G_{\mathbb{Q}} := \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$
  与 torsion points 句；III. 预告句（Serre 型 / Szpiro 型猜想，$C_{F_p}$、polynomial bound in N）。
- 结果：PASS
- 差异与处置：
  1. 【print quirk】印刷行首作 `'field case".`（300dpi 仲裁：撇号系印刷本身痕迹，"function field case" 引号对
     完整）；MD line 121 忠实保留，不改。
  2. MD line 93 将印刷跨行连字符 "corres-/ponds" 正常拼合为 "corresponds"，无损。
- 备注：页眉 "Elliptic Curves and Fermat's Equation　3" 未入 MD，正常。无 MD 修改。

---
