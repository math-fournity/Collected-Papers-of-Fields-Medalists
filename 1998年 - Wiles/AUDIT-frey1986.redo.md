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

## p.004（PDF p.4 / 印刷 p.4）
- PNG：audit-redo/p004.png（pngmono 150dpi）
- 核对："Fermat type" 后果句；congruence primes（cf. [6]）/Deligne–Rapoport–Mazur/Néron model of
  $J_0(N)$ over Z 句；节标题 II. Construction of stable elliptic curves；1. Arithmetic of elliptic curves
  开头（ref [9]）；椭圆曲线定义句与 Riemann–Roch/models 句；The generalized Weierstraß normal form 标引；
  展示式 $N_E: Y^2+\lambda XY+\mu Y = X^3+\alpha X^2+\beta X+\gamma$。
- 结果：PASS±（修复 1 处后）
- 差异与处置：
  1. 【已修复】MD line 149 `one Q-rational point P.` → `one Q-rational point $P_{\infty}$.`：300dpi 仲裁
     印刷 "point P_∞"（∞ 下标清晰，且本页后文 "such that $P_{\infty}$ is the only..." 同记号）。
  2. 【print quirk 登记不改】印刷作 "**E/C** is a projective irreducible curve"：300dpi 高倍仲裁该字形为开口 C
     （与同页 "over Q"、"Q-rational" 两处闭合金尾 Q 明确不同），数学上应为 E/Q，但系印刷错字，
     按纪律忠实保留（MD line 147 `E/C`）。
  3. 【登记不改】三处印刷下划线强调（节标题 II.、小节 1. Arithmetic...、The generalized Weierstraß normal form:
     及行内 "normal forms"）在 MD 中拍平：排版级伪影。
  4. 【字形澄清】印刷 "Weierstraß" 的 ß 为打字机 ß 字形（形似 3），MD `Weierstraß` 忠实。
- 备注：页眉 "4　G. Frey" 未入 MD，正常。展示式逐项（系数/指数/希腊字母）核对无误。

---

## p.005（PDF p.5 / 印刷 p.5）
- PNG：audit-redo/p005.png（pngmono 150dpi）
- 核对：$\alpha,\beta,\gamma,\lambda,\mu\in\mathbb{Z}$ 句；$\mathbb{Z}[1/2]$ biregular transformation 句；
  展示式 $N'_E: Y^2=X^3+AX^2+BX+C$；discriminant 句（different from 0）；
  $X\to X'+\frac{1}{3}A$ 句与 $N''_E: Y^2=X^3-g_2X-g_3$；$g_i\in Z$ 句；
  展示式 $\Delta:=4g_2^3-27g_3^2\neq 0$；$\mu^2X/\mu^3Y$ 变换段（$\mu^{-4}g_2$、$\mu^{-6}g_3$、$\mu^{-12}\Delta$）；
  绝对不变量 $j_E:=12^3\cdot 4g_2^3\cdot\Delta^{-1}$；Hasse invariant $\delta_E$ 引句。
- 结果：PASS±（修复 1 处后）
- 差异与处置：
  1. 【已修复】"is different from **O**." → "is different from **0**."：300dpi 仲裁该字形为无斜杠椭圆零，
     与同页 Δ 展示式 "≠ 0" 处零字形相同（MD 在 Δ 式已作 `0`）；判别式 ≠ 0 语境下字母 O 为转写错误。
  2. 【150dpi 误读澄清】"g₃ to μ⁻⁶g₃" 行首 150dpi 疑似 z₂，300dpi 仲裁确为 **g₃**，MD 忠实。
  3. 【登记不改】印刷下划线："Weierstraß normal form"、"the invariants" 的 "the"：排版级伪影。
  4. 【登记不改】"μ⁻¹².Δ" 以打字机句点充当乘号，MD 忠实保留。
- 备注：页眉 "Elliptic Curves and Fermat's Equation　5" 未入 MD，正常。四个展示式逐项核对无误。

---

## p.006（PDF p.6 / 印刷 p.6）
- PNG：audit-redo/p006.png（pngmono 150dpi）
- 核对：$\delta_E$ 展示式（mod $Q^{*2}$，if $j_E\neq 0,12^3$）；$j_E\notin\mathbb{Z}$ 括注；reduction theory 引入句；
  展示式 $N_E: Y^2+\lambda XY+\mu Y=X^3+\alpha X^2+\beta Y+\gamma$；residue classes
  $\overline{\alpha},\overline{\beta},\overline{\gamma},\overline{\lambda},\overline{\mu}\in\mathbb{F}_l=Z/l$ 句；
  展示式 $N_{E(l)}$（带杠系数）；plane affine curve / projective closure $E^{(l)}$ 句；
  1. Good reduction case 整段（$l\neq 2,3$；$v_l(j_E)\geq 0$；$v_l(4\beta^3-27\gamma^2)=v_l(\Delta)=0$）；
  DEFINITION（good reduction mod $l$）。
- 结果：PASS±（修复 1 处后）
- 差异与处置：
  1. 【已修复】展示式 `\mathrm{N}_{\mathrm{E}}(l)` → `\mathrm{N}_{\mathrm{E}(l)}`：印刷为打字机整行下标布局
     （N 下一行左缘 "E(1)"，无逗号，两处出现一致），即 $N_{E(l)}$；与 MD 中 DEFINITION 段的 `$N_{E(l)}$`
     原本一致，展示式系转写错位。
  2. 【print quirk 登记不改】本页 $N_E$ 展示式印刷作 "$\beta Y+\gamma$"（300dpi 高倍确认字形为 Y），
     与 p.4 同一正规式的 "$\beta X+\gamma$" 印刷不一致（p.6 打字误）；MD 按本页忠实保留 βY。
  3. 【300dpi 澄清】判据式指数确认：$4\beta^3-27\gamma^2$（β 有下降部双环=β 非 δ；指数 3、2 清晰）；
     β、γ 为无杠整系数，与印刷一致。
  4. 【登记不改】"over $\mathbf{Q}$"（reduction theory 句）印刷为普通打字机 Q，MD 作粗体 `\mathbf{Q}`：字体伪影。
  5. 【登记不改】DEFINITION 一词印刷有下划线，MD 拍平：排版级伪影。
- 备注：页眉 "6　G. Frey" 未入 MD，正常。展示式逐项核对无误（含杠线位置）。

---
