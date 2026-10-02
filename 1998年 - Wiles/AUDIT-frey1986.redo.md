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

## p.007（PDF p.7 / 印刷 p.7）
- PNG：audit-redo/p007.png（pngmono 150dpi）
- 核对：2. Multiplicative type 整段（singularity/two tangent lines；typical case 展示式
  $v_l(\lambda)=0, v_l(\mu)>0, v_l(\alpha)>0, v_l(\beta)>0$, $v_l(\gamma)=-v_l(j_E)>0$）；
  DEFINITION（multiplicative type mod $l$，$N_{E(l)}$）；if and only if 句
  （$v_l(j_E)<0$、$Q(\sqrt{\delta_E})$ unramified）；3. Additive type 整段（$N_{E(l)}$、$\mathbb{F}_l$、
  one tangent line）；cases 1./2. 与 stable reduction mod $l$ 定义句；
  "multiplicative type"/"additive type" 词源句至 "torus split by"。
- 结果：PASS±（修复 2 处后）
- 差异与处置：
  1. 【已修复】两处 `$N_{E}(l)$` → `$N_{E(l)}$`（multiplicative DEFINITION 段、Additive type 段）：
     与 p.006 同型——印刷为打字机整行下标（N 下一行 "E(1)"，无逗号），即 $N_{E(l)}$；
     证据：audit-redo/p007.png + 300dpi 裁剪 audit-redo/300dpi/frey1986-p007-NEl-definition-300dpi.png
     （N 下方独立行布局，与 p.6 相同；该裁剪于证据持久化 commit 补齐存档）。
  2. 【150dpi 误读澄清】"the reduction type of E modulo"：300dpi 仲裁印刷为单数 type，MD 忠实
     （150dpi 疑似复数 types 系噪点）。
  3. 【登记不改】印刷下划线强调：case 标号 "1."、"2."、"DEFINITION"、"stable reduction mod l"：
     排版级伪影，MD 拍平。
- 备注：页眉 "Elliptic Curves and Fermat's Equation　7" 未入 MD，正常。本页末行止于
  "torus split by"（跨页句），下一行 "an extension of degree ≤ 2…" 属 p.8 范围。

---

## p.008（PDF p.8 / 印刷 p.8）
- PNG：audit-redo/p008.png（pngmono 150dpi）
- 核对：torus split by 跨页句收尾（degree ≤ 2 / additive group / $\mathbb{F}_l$）；
  Tate 定理段（$Q_l$ l-adic、$\delta_E\in K^{\times2}$、$K/\langle q\rangle$、
  $j_E=\frac{1}{q}+\sum_{i\geq 0}a_iq^i$、Fourier expansion、$q=e^{2\pi i\tau}$、ref [7]）；
  consequence 段（$E_p$、$E(\overline{\mathbb{Q}})$、$K_p$、$K_{p,l}=Q_l(\zeta_p,\sqrt[p]{j_E})$）；
  Hensel's lemma 句（$l$ unramified in $K_p$）。
- 结果：PASS±（修复 2 处后）
- 差异与处置：
  1. 【已修复】`\sum_{i>0}` → `\sum_{i\geq 0}`：350dpi 级放大仲裁印刷下标为 "i≥0"（≥ 字形带底横清晰）。
  2. 【已修复】"good reduction mod $l$. Hensel's" → "good reduction mod $l$ Hensel's"：印刷行尾无标点
     （300% 放大确认），MD 句点系转写添加。
  3. 【核对无误】$K/\langle q\rangle$、$K^{\times2}$、$e^{2\pi i\tau}$、$Q_l(\zeta_p,\sqrt[p]{j_E})$、
     "Let $l$ be a divisor of $l$"（打字机 l/1 同形，语义为素元除 l，MD 读法正确）、ref [7]。
- 备注：页眉 "8　G. Frey" 未入 MD，正常。本页末行止于 "unramified in $K_p$."，后续
  "For brevity's sake…" 属 p.9 范围。

---

## p.009（PDF p.9 / 印刷 p.9）
- PNG：audit-redo/p009.png（pngmono 150dpi）
- 核对：For brevity's sake 引句；DEFINITION（E over Q is stable）；PROPOSITION 1 陈述
  （$K_p$ unramified over $\mathbb{Q}$ in all primes $l\neq p$ with $v_l(j_E)\geq 0$ or
  $v_l(j_E)\equiv 0 \mod p$）；minimal Weierstraß equation 段（principal domain、"one" 强调）；
  展示式 $N_E: Y^2+\lambda XY+\mu Y=X^3+\alpha X^2+\beta X+\gamma$；
  $\alpha,\beta,\gamma,\lambda,\mu\in\mathbb{Z}$ minimal equation 句；discriminant of E = $\Delta_E$ 句；
  The following facts hold: 引句。
- 结果：PASS
- 差异与处置：
  1. 【300dpi 澄清】PROPOSITION 1 同余号印刷为 **≡**（三横清晰），MD `\equiv` 忠实；
     本页 $N_E$ 展示式印刷为 **βX**（与 p.4 一致，反证 p.6 βY 系该页孤立印刷误），MD 忠实。
  2. 【登记不改】印刷下划线强调：DEFINITION、PROPOSITION 1、行内 "one"：排版级伪影。
- 备注：页眉 "Elliptic Curves and Fermat's Equation　9" 未入 MD，正常。本块（p.1–p.9）至此完成；
  本页末行止于 "The following facts hold:"，后续 "Assume that E is stable…" 属 p.10 范围。

---

## 证据持久化附注（p.001–p.009 块收尾）

按 AUDIT-SOP「被引用证据不得只存 /tmp」，上列各页条目中引用的 300dpi 仲裁裁剪已持久化至
`audit-redo/300dpi/`（frey1986 短名前缀，避免同目录其他篇目碰撞；150dpi 整页图为本目录 p0NN.png）：

| 页 | 文件 | 裁决内容 |
|---|---|---|
| p.001 | frey1986-p001-conjecture-Fn-300dpi.png | CONJECTURE 下标为 n 非 p |
| p.001 | frey1986-p001-faltings-300dpi.png | 印刷 "Falting's theorem"（print quirk） |
| p.002 | frey1986-p002-implies-Fp-underline-300dpi.png | implies F̲_p 有下划线（已修复项） |
| p.002 | frey1986-p002-theorem-p15-300dpi.png | "the Theorem on p. 15"（无重音） |
| p.002 | frey1986-p002-there-motivation-300dpi.png | "There is our motivation"（print quirk） |
| p.003 | frey1986-p003-fieldcase-300dpi.png | 行首撇号 `'field case"`（print quirk） |
| p.004 | frey1986-p004-EoverC-Pinf-300dpi.png | 印刷 E/C（quirk 保留）+ P_∞ 下标（已修复项） |
| p.005 | frey1986-p005-fromO-300dpi.png / frey1986-p005-delta-eq-300dpi.png | 零字形一致 → O 改 0（已修复项） |
| p.006 | frey1986-p006-NE-display-betaY-300dpi.png | 本页印刷 βY（print quirk 保留） |
| p.006 | frey1986-p006-NEl-display-300dpi.png | N_{E(l)} 整行下标（已修复项） |
| p.006 | frey1986-p006-criterion-300dpi.png / frey1986-p006-criterion-exponents-300dpi.png | β³、γ² 指数确认 |
| p.007 | frey1986-p007-NEl-definition-300dpi.png | N_{E(l)} 整行下标（已修复项证据补齐） |
| p.007 | frey1986-p007-reduction-type-300dpi.png | 单数 type（澄清 150dpi 误读） |
| p.008 | frey1986-p008-sum-index-300dpi.png | Σ_{i≥0}（已修复项） |
| p.008 | frey1986-p008-modl-no-period-300dpi.png | 行尾无句点（已修复项） |
| p.009 | frey1986-p009-congruence-300dpi.png | ≡ 三横确认 |
| p.009 | frey1986-p009-NE-display-betaX-300dpi.png | 本页 βX（反证 p.6 βY 为孤立印刷误） |

块内统计：p.001–p.009 共 9 页 = PASS×3（p.001/p.003/p.009）+ PASS±×6（p.002/p.004–p.008）+ FAIL×0；
MD 修复 8 处（每处对应上表已修复项）；重做起点 MD SHA=dfee1701…，块完成时 MD SHA=81e6b4c1…。

---

## p.010（PDF p.10 / 印刷 p.10）
- PNG：audit-redo/p010.png（pngmono 150dpi）
- 核对：stable 情形 $v_l(\Delta_E)=-\text{Min}(v_l(j_E),0)$ 句；geometric conductor
  $N:=\prod_{v_l(\Delta_E)>0}l$ 展示行；ref [9]；节标题 2. Stable elliptic curves；
  K_p small ramification over $\mathbb{Q}(\zeta_p)$ 句；A ≡ 0 mod $2^5$、B ≡ 1 mod 4、C := A-B 句；
  展示式 $N_E: Y^2=X^3+(A+B)X^2+ABX$；Weierstraß 式 $N_{\widetilde{E}}: \widetilde{Y}^2=\widetilde{X}^3-
  \frac{1}{3}(A^2+B^2-AB)\widetilde{X}+\frac{1}{27}(A+B)(2A^2+2B^2-5AB)$；
  $\Delta=A^2\cdot B^2\cdot C^2$；$j_E=2^8(A^2+B^2-AB)^3\cdot A^{-2}\cdot B^{-2}\cdot C^{-2}$；
  $\delta_E\equiv\frac{1}{2}\cdot\frac{A^2+B^2-AB}{(A+B)(2A^2+2B^2-5AB)} \bmod Q^{*2}$。
- 结果：PASS±（修复 1 处后）
- 差异与处置：
  1. 【已修复】删除伪造展示块 `$$\mathbf{K}_{\mathbf{p}}$$`（原夹于 "rami-" 与 "fication over…" 之间）：
     印刷对应位置为连续句子 "…has only small rami-/fication over Q(ζ_p)."，无任何独立 K_p 展示行；
     系 MinerU 把行内 $K_p$ 下标误提为展示式。删除后按 MD 自身惯例拼合连字符行为
     "…has only small ramification over…"。
  2. 【300dpi 澄清】Weierstraß 式标签确为 $N_{\widetilde{E}}$（E 与变量均有波浪号：$N_{\tilde E}$、
     $\widetilde{Y}^2$、$\widetilde{X}^3$、$\widetilde{X}$），MD 转写忠实（证据
     audit-redo/300dpi/frey1986-p010-NEtilde-display-300dpi.png）；
     $\Delta=A^2\cdot B^2\cdot C^2$ 的 B 指数为 2（150dpi 疑似 3 系噪点；与 $j_E$ 式自洽），MD 忠实
     （audit-redo/300dpi/frey1986-p010-delta-300dpi.png）；δ_E 式 ≡ 忠实。
  3. 【登记不改】节标题 "2. Stable elliptic curves." 印刷有下划线，MD 拍平；
     $\zeta_{\mathbf{p}}$ 粗体 p 为字体伪影（同页内非粗体 $\zeta_p$ 见他页）。
- 备注：页眉 "10　G. Frey" 未入 MD，正常。本页止于 δ_E 展示式，"From those data…" 属 p.11 范围。

---
