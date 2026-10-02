# AUDIT — V. G. Drinfeld, “Elliptic Modules”

## 当前状态

- Source PDF：`Drinfeld_1974_elliptic_modules.pdf`，32 个 PDF 页面；Creator 为 ABBYY FineReader。PDF 中每页包含 400dpi 单色整页图像，并另带 OCR 文本层。本篇按扫描件模式执行，OCR/`pdftotext` 仅作定位辅助，原页图像为权威。
- MinerU Markdown：`Drinfeld_1974_elliptic_modules_mineru/Drinfeld_1974_elliptic_modules__Drinfeld_1974_elliptic_modules.md`。
- 逐页审计：32/32 页已于 2026-10-01 完成；汇总 PASS 0、PASS± 3、FAIL 29。各页判定及扫描证据见下列记录；扫描页图为原文权威，PDF OCR 文本仅作定位。
- Markdown 状态：全篇逐页审计结束后，按页图对已确认的差异逐处手工修复；2026-10-01 已全文重读并按页图核验修改。原始 Markdown 与修订提交、逐页修复状态见文末登记。

## p.001（PDF p.1 / 印刷 p.561）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p001.png`（pngmono 150dpi）
- 核对：题名、作者、UDC、摘要、Bibliography 14 items、Introduction 开头、admissible triple 定义与四类、首段记号说明、AMS subject classifications。
- 结果：PASS±。可见正文与现有 Markdown 相符；Markdown 未保留印刷页眉中的 `Mat. Sbornik, Tom 94 (136) (1974), No. 4`、`Math. USSR Sbornik, Vol. 23 (1974), No. 4`，也未保留印刷页码 561。作为扫描件版面的页眉/页码遗漏记录；题名、作者、摘要及正文内容仍可辨认，当前不据此误改正文。
- 依据：本页完整 150dpi 源页 PNG；页级 OCR 文本仅用于定位，未用它覆盖源页判断。

## p.002（PDF p.2 / 印刷 p.562）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p002.png`（pngmono 150dpi）
- 核对：elliptic A-module 定义、level `I` 结构定义、光滑模空间段落、Theorem 1、Theorem 2 两项陈述、四类 triples 的过渡段、B) Outline 开头与 “cusp form” 编辑注。
- 结果：PASS±。现有 Markdown 对应正文和编辑注与源页相符；Markdown 未保留印刷页眉中的作者名和印刷页码 562。复杂公式按源页视觉核对，未根据噪声 OCR 文本替换。
- 依据：本页完整 150dpi 源页 PNG；OCR 文本仅作定位辅助。

## p.003（PDF p.3 / 印刷 p.563）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p003.png`（pngmono 150dpi）
- 核对：B) Outline 的收尾、作者致谢、§1 标题、formal group 定义、加法群例子、特征 `p` 下 Frobenius `τ` 与交换关系、formal O-module 定义及 germ/函子段、Proposition 1.1 开头。
- 结果：PASS±。可见正文与现有 Markdown 相符；Markdown 未保留页眉题名 `ELLIPTIC MODULES` 及印刷页码 563。底部 Proposition 1.1 在本页只出现引入句，后续关系式待下一页继续核对。
- 依据：本页完整 150dpi 源页 PNG；OCR 文本仅作定位辅助。

## p.004（PDF p.4 / 印刷 p.564）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p004.png`（pngmono 150dpi）
- 300dpi 局部证据：`audit/300dpi/Drinfeld_1974_elliptic_modules_p004_relations.png`、`audit/300dpi/Drinfeld_1974_elliptic_modules_p004_proposition.png`、`audit/300dpi/Drinfeld_1974_elliptic_modules_p004_prop13.png`
- 核对：Proposition 1.1 的 (1)–(3) 关系及证明、Proposition 1.2、局部非阿基米德情形开头与 Proposition 1.3。
- 结果：FAIL。印刷 p.564 的 300dpi 原图在 Proposition 1.1 证明、Proposition 1.3 陈述和其证明开头均印作 `h(a)`；现有 Markdown 对应处写作 `b(a)`（当前 MD 第 101、125、129 行），会改变符号。应待全篇审计完成后用 Edit 逐处改为源页 `h(a)`，再复核最终 Markdown；本页签字时尚未修改。
- 源级 quirk：印刷 p.564 的 Proposition 1.2 证明原样出现 “If `O ⊂ F_{p^k}`” 后又给出 `a ∉ F_{p^k}` 的条件，二者表面不相容；留存的 300dpi 源页裁片显示印刷关系符未带否定斜线。按 print 忠实保留，列为原文 quirk，不据数学推断改写。
- 另记：Markdown 未保留页眉作者名与印刷页码 564。

## p.005（PDF p.5 / 印刷 p.565）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p005.png`（pngmono 150dpi）
- 300dpi 局部证据：`audit/300dpi/Drinfeld_1974_elliptic_modules_p005_h.png`、`audit/300dpi/Drinfeld_1974_elliptic_modules_p005_q.png`
- 核对：Proposition 1.3 证明续段、映射与商模生成元、Proposition 1.4、Corollary、Proposition 1.5(a) 条件及公式。
- 结果：FAIL。留存的 300dpi 源页裁片确认现有 Markdown 多处把印刷 `h` 误成 `b`：p.5 对应 MD 第 131、133、135 行（含 `h(b)`/`h(a)`、映射 `h(a)` 与生成元 `h(π)`、`h(πb)=πh(b)=π^n h(b)` 及其带横线记号）；第 133 行另将印刷 `α ↦ p/π` 写成 `a ↦ f/π`。Proposition 1.5(a) 印刷写 `n` 不是 `q` 的幂，MD 第 147 行误成 `g`。这些都待全篇审计后用 Edit 逐处修复和复核；本页签字时未改 Markdown。
- 另记：Markdown 未保留页眉题名及印刷页码 565。

## p.006（PDF p.6 / 印刷 p.566）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p006.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p006.png`
- 核对：formal-module homomorphism 定义、height 定义与 O′-module remark、Proposition 1.6 三项及证明、Proposition 1.7 两项及 normal-module 定义和 a)–c) 证明开头、跨页段落止于 “Therefore”。逐项将页图与 Markdown 对应正文/公式对读；PDF OCR 文本仅用于定位。
- 结果：FAIL。印刷 p.566 的 300dpi 页图确认，Markdown 在 Proposition 1.6 证明将 `Λ_O` 误作 `Λ_0`；Proposition 1.7 的 normal-module 证明多处把 height `h` 读作 `b`，把 `q^h` 读作 `q^b`，将系数域 `F_{q^h}` 读作 `F_{ab}`/`F_{q^b}`，并把 `f_a` 读作 `f_α`。这些是内容级符号差异，待全部页审计结束后逐处按原页修复。其余本页核对项与页图相符。
- 备注：页眉作者名与印刷页码 566 未收入 Markdown；本页 300dpi 图像已保存为仲裁证据。

## p.007（PDF p.7 / 印刷 p.567）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p007.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p007.png`
- 核对：Proposition 1.7(c) 收尾与中心除代数结论、§2 标题、Definitions and notation（τ 环与 D/ε）、k/ν/A 记号、elliptic A-module 定义、degree 映射、Proposition 2.1 与证明、rank 定义和 A=F_q[x] 例子、Proposition 2.2 开头。页图对照 Markdown；PDF OCR 文本只作导航。
- 结果：FAIL。印刷 p.567 与 Markdown 有多处内容级差异：Prop. 1.7(c) 的 `h²`/`1/h` 在 Markdown 中为 `b²`/`1/b`，且 `log_p q` 的下标排写被误成 `log p^q`；§2 degree 映射中印刷 `τ^i` 被写成 `r^i`；Prop. 2.1(b) 证明首式多出 `\dot{}`；例子把 `φ(x)` 写成 `(x)`，把 `τ^{j log_p q}` 写成 `r^{j log p q}`。待全篇审计完成后逐处按印刷页修复。其余本页核对项与页图相符。
- 备注：页眉题名与印刷页码 567 未收入 Markdown；本页 300dpi 图像用于公式字形对读。

## p.008（PDF p.8 / 印刷 p.568）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p008.png`（pngmono 150dpi）
- 核对：Proposition 2.2 结论、torsion-module 直和与证明、rank corollary、formal A-module remark、§2C isogeny 定义、Proposition 2.3 条件与证明、isogeny corollary、Proposition 2.4 陈述及证明开头。以整页图像逐项对读对应 Markdown；PDF OCR 仅作定位。
- 结果：FAIL。Markdown 的 Proposition 2.2 torsion-module 直和将指数 `j_ν` 拍平成 `jν`，其证明又将 `j_ν` 误成 `1ν`；印刷 Proposition 2.3(b) 的 `t^{q^b}` 被写为 `t^{qb}`，均改变记号/幂次，待全篇审计后逐处修复。其余本页核对项与源页相符。
- 备注：页眉作者名与印刷页码 568 未收入 Markdown。

## p.009（PDF p.9 / 印刷 p.569）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p009.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p009.png`
- 核对：Proposition 2.4 证明收尾与 corollary、§3 标题及 lattice/morphism 定义、Proposition 3.1、Weierstrass product、Lemma 与证明、proof 1) 收尾、proof 2) 递归式。300dpi 源页与 Markdown 对应段落逐项核对，PDF OCR 只作定位。
- 结果：FAIL。印刷 proof 2) 中 formal-series 自变量使用 `τ`，包括 `f = 1 + Σ b_i τ^i`、`φ(a) = a + Σ a_j τ^j`；Markdown 将这些 `τ` 误读为 `r`。递归式右侧指数印作 `p^j`，Markdown 写作 `p j`。这些符号差异待全篇审计结束后手工修复。其余本页核对项相符。
- 备注：页眉题名与印刷页码 569 未收入 Markdown；本页 300dpi 图像核实递归式上标。

## p.010（PDF p.10 / 印刷 p.570）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p010.png`（pngmono 150dpi）
- 核对：Proposition 3.1 proof 2) 收尾与 proof 3)、corollary、§4A zero-level deformations 的设置、Proposition 4.1 与证明、deformation-isomorphism 定义、Proposition 4.2 陈述和证明开头。逐项按源页对读 Markdown；PDF OCR 文本仅用于定位。
- 结果：FAIL。递归估计中的印刷幂次 `p^{-i}` 在 Markdown 两处写成 `p-i`；Proposition 4.2 的有限 height 参数印作 `h`，表示环参数数为 `h-1`，并在证明开头使用 `q^h-1`，而 Markdown 对应写作 `b-1` 和 `q^b-1`。待全篇审计后按印刷页逐处修复。
- 备注：页眉作者名与印刷页码 570 未收入 Markdown。

## p.011（PDF p.11 / 印刷 p.571）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p011.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p011.png`
- 核对：Proposition 4.2 proof opening（level-0 parameters）、2-dimensional cocycle 定义及四组关系、coboundary、Lemma 1 两项与证明、Proposition 4.2 同构构造、`(Δ_i, δ_i)` 的 degree bounds、subsection a) 两条 coboundary congruence。300dpi 页图用于核对上标及 m-adic 幂次；OCR 仅供定位。
- 结果：FAIL。Proposition 4.2 延续处的印刷 `h-1`、`q^h-1`、`j<q^h-1` 与 `Σ_{i=1}^{h-1}` 在 Markdown 多处误作 `b`；Lemma 1 proof 将印刷 `mod m^r` 两处读为 `mod m'`。待全篇审计后逐处按印刷页修复。
- 源级 quirk：印刷句为 “The exists a one-to-one correspondence”；Markdown 忠实保留，不作语法润色。另记：页眉题名与印刷页码 571 未收入 Markdown。

## p.012（PDF p.12 / 印刷 p.572）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p012.png`（pngmono 150dpi）
- 核对：Proposition 4.2(b) 两个 cocycle congruence、§4B arbitrary-level 设置与 level-n 结构定义、divisor relation、唯一结构说明、Proposition 4.3 陈述及 proof a)/`Φ_r` lemma 开头和 local parameters。以完整页图对读 Markdown；OCR 仅供导航。
- 结果：FAIL。Prop. 4.2(b) 第一项的集合/分量括号在 Markdown 中错位，且把第二分量的 `v` 并入第一分量。§4B 中印刷高度 `h` 被多处写作 `b`；level-n 结构的 source map 指数 `h` 被写作 `b`；印刷 `f_{π^n}` 与点集 `((1/π^n)O/O)^h` 被写作 `f_π` 与 `((1/π)O/O)^b`。此外 `\hat O^{nr}` 在两处被写作 `\hat O^{nτ}`，有限高度 `h` 被写作 `b`，`Φ_r` lemma 的 `t_r,…,t_{h-1}` 被写作 `t_r,…,t_{b-1}`。以上待全篇审计后逐处按源页修复。
- 备注：页眉作者名与印刷页码 572 未收入 Markdown。

## p.013（PDF p.13 / 印刷 p.573）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p013.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p013.png`
- 核对：`Φ_r` construction 与 parameter quotient、injectivity proof、`r=h` specialization、Proposition 4.3(b) basis and power-series presentation、Proposition 4.4 statement through proof opening. 300dpi 页图用于核对变量上下标；PDF OCR 仅作定位。
- 结果：FAIL。印刷多处高度/维数 `h` 在 Markdown 写成 `b`，包括 local parameters `t_r,…,t_{h-1}`、`r=h`、`e_i (1≤i≤h)`、`D_{n+1}` 的变量 `y_1,…,y_h` 和 `P⊂((1/π^n)O/O)^h`；另有对应 level-m homomorphism 的指数 `h` 误作 `b`。一处乘积中的 `((1/π)O/O)^r` 被写为 `((1/π)!O/O)^r`。待全篇审计后逐处按源页修复。
- 备注：页眉题名与印刷页码 573 未收入 Markdown；结构映射记号对读证据还包括 `audit/300dpi/Drinfeld_1974_elliptic_modules_p013_phi_crop.png`。

## p.014（PDF p.14 / 印刷 p.574）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p014.png`（pngmono 150dpi）
- 核对：Proposition 4.4 proof 收尾、§4C divisible-module definition 与 level-n structure、Proposition 4.5 陈述及 proof、Remark on O′-module deformation bases。
- 结果：FAIL。Proposition 4.4 proof 的 level-m homomorphism 印作 `((1/π^m)O/O)^h`，Markdown 写成指数 `b`；§4C divisible-module level structure 的 source rank 印作 `j+h`，Markdown 写成 `j+b`；Proposition 4.5 表示环维数印作 `j+h`，Markdown 写成 `j+b`。均为此前出现的 `h→b` 记号误读，待全篇审计后按原页修复。
- 备注：页眉作者名与印刷页码 574 未收入 Markdown。

## p.015（PDF p.15 / 印刷 p.575）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p015.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p015.png`
- 核对：§5A Proposition 5.1 与证明、Proposition 5.2 statement/conjugation/degree-lowering proof、§5B elliptic A-module definition and standard-module remark、`X_I` finite-flat/étale assertion。
- 结果：FAIL。Proposition 5.1 中印刷操作元 `h` 在 Markdown 多处写作 `b`；其证明的 coefficient comparison 用印刷 `τ^{d+n}`，Markdown 写作 `r^{d+n}`，并把 `d=d_1=d_2` 写成 `d=d_2=d`。Proposition 5.2 conjugation 左因子将印刷 `Σ α_i τ^i` 错排为 `Σ α_i τ^j`；存在性构造分母的印刷指数为 `a_d^{p^{n-d}}`，Markdown 写成 `a_d^{p^{n-1}}`。以上待全篇审计后逐处修复。
- 备注：页眉题名与印刷页码 575 未收入 Markdown；300dpi 页图核实了末项幂指数。

## p.016（PDF p.16 / 印刷 p.576）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p016.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p016.png`
- 核对：level-I structure definition/remark、Proposition 5.3 and proof, §5C deformation functor setup, Proposition 5.4(a)–(b) through the localization action opening.
- 结果：FAIL。印刷 level-I remark 的 target 为 `X_I`，Markdown 写成 `X_r`；structure lift 的 level 为 `Iν^n`，Markdown 写成 `lv^n`。Proposition 5.4(b) 开头的 place notation `ν` 在 Markdown 写作 `v`（`v=(x)`、`x∈v`），改变了已定义符号。待全篇审计后按原页修复。
- 备注：页眉作者名与印刷页码 576 未收入 Markdown；300dpi 页图用于确认 `Iν^n` 和下标记号。

## p.017（PDF p.17 / 印刷 p.577）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p017.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p017.png`
- 核对：Proposition 5.4(b) localization-action proof close, part c) tangent-space deformation calculation, Proposition 5.3 corollary, §5D group-action setup through the commutative diagram introduction. 300dpi 页图用于核对 (h/b)、系数索引及 adèle notation。
- 结果：FAIL。Proposition 5.4(b) 延续处印刷 `A_ν^*`，Markdown 写作 `A_v^*`。Part c) 的 fixed height/index `h` 多处写成 `b`（起始指数 `a_h≠0`、`β_i=0` for `i≤h-1`、求和下限 `h`、点数 `p^{d-h}`）；universal deformation 的参数印作 `α_i`，Markdown 写作 `a_i`。Proposition 5.3 corollary 的有限平坦映射印作 `M_J^d→M_I^d`，Markdown 两端写成 `M_I^d`。待全篇审计后逐处按印刷页修复。
- 备注：页眉题名与印刷页码 577 未收入 Markdown。

## p.018（PDF p.18 / 印刷 p.578）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p018.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p018.png`
- 核对：§5D commutative diagram completion, adelic group actions and finite-level quotient identity, §5E induced-ring definition, fiber `M^d_(ν)`/height-1 subset, Proposition 5.5 statements and proof opening.
- 结果：FAIL。印刷 subgroup action 使用 `GL(d,𝔄_f)`，Markdown 在两处误作 `GL(d,𝔘_f)`；Proposition 5.5 的 `B'` preimage and scheme action 也将 `𝔄_f` 写作 `𝔘_j`/`𝔘_f`。印刷 quotient identity 为 `M_I^d=U_I\backslash M^d`，Markdown 末式把右侧改成 `U_I\backslash M_I^d`。本页多处 local-field place `ν` 被写作 `v`（含 `k_v`、`A_v`）；矩阵左下项印作 `1`，Markdown 写入 `1.`。这些待全篇审计后逐处按源页修复。
- 备注：页眉作者名与印刷页码 578 未收入 Markdown；300dpi 页图用于核对 adèle fraktur 与矩阵项。

## p.019（PDF p.19 / 印刷 p.579）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p019.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p019.png`
- 核对：Proposition 5.5 proof 收尾、§6A analytic/homogeneous/topological analog definitions, simplicial metric, norm classification, barycentric construction, metric `ρ` formula and λ-map, Proposition 6.1 opening.
- 结果：FAIL。印刷 metric `ρ({ν_1},{ν_2})` 使用两项 `sup_{K^d}`（`ν_1/ν_2` 与 `ν_2/ν_1`）；Markdown 将 `ν_1,ν_2` 写成粗体 `v_1,v_2`，并将第二个 `sup` 识别成乱码 `s_{llp}`，破坏了该公式。其余本页主要定义与关系式和源页相符。
- 备注：页眉题名与印刷页码 579 未收入 Markdown；300dpi 页图核实 metric 公式。

## p.020（PDF p.20 / 印刷 p.580）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p020.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p020.png`
- 核对：Proposition 6.1 statements and proof, norm `ψ`/`ν` definitions and boundedness estimate, barycentric subdivision definition, Proposition 6.2 set and covering statement/proof opening.
- 结果：FAIL。印刷 boundedness estimate 的 ball radius 为 `log_q ε`，Markdown 写作 `log_a ε`；印刷单位 norm `ν(a_1,…,a_d)=max|a_i|` 被写作 `v(...)`，且 ∑ formula `Σ_{i=1}^d a_i z_i` 在 Markdown 丢失 `i=` 并写作 capital `Σ_1^d`。Proposition 6.2 proof 的 nerve 为 `\bar S^d`，Markdown 写作 `\widetilde S^d`；set definition 中印刷连接词 “for” 被拆成未格式化的 `f o r`。其余本页主要条件与陈述相符。
- 备注：页眉作者名与印刷页码 580 未收入 Markdown；300dpi 页图核实了对数底、范数符号与 bar/tilde。

## p.021（PDF p.21 / 印刷 p.581）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p021.png`（pngmono 150dpi）
- 核对：Proposition 6.2 proof covering/nerve argument and barycentric-coordinate inequalities, Proposition 6.3 invariant Tate algebra, Proposition 6.4 quotient open-embedding assertion/proof, finite-group quotient universal property through the affine-covering setup.
- 结果：FAIL。印刷交集点的 coordinates 为 `(α_1,…,α_d)`，Markdown 末项误作 `α_2`；印刷 simplex coordinate condition `Σ_{i=1}^d α_i=1` 被写成 `Σ_1^d α_i=1`，遗漏求和指标 `i=`。其余本页主要证明结构与陈述相符。
- 备注：页眉题名与印刷页码 581 未收入 Markdown。

## p.022（PDF p.22 / 印刷 p.582）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p022.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p022.png`
- 核对：finite-group quotient argument close, discrete-action definition/conditions 1–4 and quotient property, §6C uniformization spaces, metrized A-module similarity and level-structure definitions, induced norm and Proposition 6.5 statement/proof opening.
- 结果：FAIL。Discrete-action condition 3 印作 `X_j∩X_{γ(i)}`，Markdown 写作 `X_(j)∩X_{γ(i)}`。相似 metrized modules 的印刷同构为 `f:P_1→P_2`，Markdown 写作 `f:P\preceq P_2`。本节的 level-structure similarity space 与 Proposition 6.5 所用空间均印作 `U_I\backslash \tilde S^d(R)`；Markdown 两处省略了 tilde，写成 `U_I\backslash S^d(R)`。这些是记号/对象范围差异，待全篇审计后按原页修复。
- 备注：页眉作者名与印刷页码 582 未收入 Markdown；300dpi 页图确认 (\tilde S^d(R)) 和 (P_1\to P_2) 记号。

## p.023（PDF p.23 / 印刷 p.583）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p023.png`（pngmono 150dpi）
- 核对：Proposition 6.5 proof close, Proposition 6.6 statement and proof a)/b), formal-isomorphism construction, bounded-affine-open lemma and proof through its product estimate.
- 结果：FAIL。Prop. 6.6 印刷目标 `U_I\backslash \tilde Ω^d` 在 Markdown 写成 `U_I\backslash Ω^d`；proof b) 的 `x` source set 同样漏掉 tilde。例子中 lattice `Σ_{i=1}^{d} A z_i` 丢失 `i=`，level `I` 写成 `l`；level-structure map `ψ` 与 `I^{-1}Γ/Γ` 之间的印刷 isomorphism sign 被写作 `\mathfrak S`。proof b) 的 local ring quotient 印作 `O_y/m_y^n`，Markdown 写作 `O_y/M_y^n`。待全篇审计后逐处按源页修复。
- 备注：页眉题名与印刷页码 583 未收入 Markdown。

## p.024（PDF p.24 / 印刷 p.584）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p024.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p024.png`
- 核对：Proposition 6.6 proof close, §7 Tate uniformization definitions, stable/good reduction conditions, Proposition 7.1 valuation formula, lattice definition, Proposition 7.2 pair classification, and the `(ψ,u)` relation at proof opening.
- 结果：FAIL。印刷 valuation definition is `w(Σa_iτ^i) = -inf_{i>0}{v(a_i)/(p^i-1)}`；Markdown 写作 `= = inf`，漏掉负号。Proposition 7.2 的 `X` rank 印作 `d_1`，Markdown 写成 `d`；the intertwining equation 印作 `uψ(a)=φ(a)u`，Markdown 写成 `uψ(a)=\varphi(a)u`；系数条件 `a_i→0` 被写成 `a_i→O`。均为可由 300dpi 页图确认的内容差异，待全篇审计后修复。
- 备注：页眉作者名与印刷页码 584 未收入 Markdown；300dpi 页图核实 valuation 符号和指数。

## p.025（PDF p.25 / 印刷 p.585）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p025.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p025.png`
- 核对：Proposition 7.2 proof 2) analytic-homomorphism recurrence/lattice conclusion and proof 3), §8 Theorem 1/proof/corollary, §9 compactification setup through the boundary group definition.
- 结果：FAIL。Lemma recurrence 中印刷 `d_i=c_i^{p^{-i}}` 与 `d_{i-j}^{p^k}` 在 Markdown 写成 `c_i^{p-i}` 与 `d_{i-j}^{p,k}`；印刷 `a_i→0` 被写为 `a_i→O`。§8 Theorem 1 and proof 中印刷 adèle factor `𝔄_f^*` 多处写作 `𝔘_f^*`，并把 place `ν` 写作 `v`（`v∈Spec A`, `A_v`, `A_v/(π)`）。待全篇审计后按源页修复。
- 备注：页眉题名与印刷页码 585 未收入 Markdown；300dpi 页图核实了递归上标。

## p.026（PDF p.26 / 印刷 p.586）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p026.png`（pngmono 150dpi）
- 核对：§9A boundary-group construction and completions, Proposition 9.1 and proof/corollary, Proposition 9.2 and proof, Proposition 9.3 statement.
- 结果：FAIL。印刷 `V_I` 为上三角矩阵 `\begin{pmatrix}x&y\\0&1\end{pmatrix}`，Markdown 写作 `\binom{x}{0}`，丢失矩阵的上右/下右项。印刷 `N_I^1=V_I\backslash N^1`、`M_I^2=U_I\backslash\widetilde M^2` 与 `\hat M_I^2=U_I\backslash M^2` 在 Markdown 都使用 `\setminus`，把商空间符号改成了集合差。Corollary 的 place `ν` 也写作 `v`。待全篇审计后按原页修复。
- 备注：页眉作者名与印刷页码 586 未收入 Markdown。

## p.027（PDF p.27 / 印刷 p.587）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p027.png`（pngmono 150dpi）
- 核对：Proposition 9.3 proof morphism `σ`/sheaf lemma and its six steps, §10 heading and étale-cohomology introduction.
- 结果：FAIL。印刷 composition begins at `\hat M_I^2` with arrow labelled `π'`; Markdown fuses these into `\hat M_I^{2π'}`. The open-set list in the sheaf lemma begins with `∅`, but Markdown writes `φ`. Proof step 6 uses `H^0(X,G_1)=0`; Markdown drops the superscript and writes `H_0(X,G_1)=0`. 待全篇审计后逐处按源页修复。
- 备注：页眉题名与印刷页码 587 未收入 Markdown。

## p.028（PDF p.28 / 印刷 p.588）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p028.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p028.png`
- 核对：§10A étale-cohomology definitions 1–4, four stated properties, Proposition 10.1 statement and proof a)/b) opening.
- 结果：FAIL。Definition 1 的 invertible-sheaf trivialization 印作 `φ: O_X ≅ L^n`；Markdown 写作 `O_x ≅ L^n`，将 `X` 改成小写 `x`。其余本页主要定义、序列与 Proposition 10.1 条件和页图相符。
- 备注：页眉作者名与印刷页码 588 未收入 Markdown；300dpi 图像确认 `O_X` 的大写下标。

## p.029（PDF p.29 / 印刷 p.589）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p029.png`（pngmono 150dpi）
- 核对：Proposition 10.1 proof b), resulting exact sequence and cohomology group, §10B cochain definition, Proposition 10.2 statement and proof through the harmonic-function criteria, Proposition 10.3 opening.
- 结果：FAIL。印刷条件为 “`n ∤ m`” in the assertion that `z^m` is not an `n`th power in `K{z,z^{-1}}`; Markdown renders this as `n + m`, changing the divisibility condition. The remaining checked statement and proof formulas on this page match the scan.
- 备注：页眉题名与印刷页码 589 未收入 Markdown。

## p.030（PDF p.30 / 印刷 p.590）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p030.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p030.png`
- 核对：Proposition 10.3 statement, proof a) exact sequence and harmonic-cochain identification, proof b) inertia action, proof c) archimedean-curve cohomology and covering formula through the compactified-cohomology conclusion.
- 结果：FAIL。Proposition 10.3 定义 `V` 使用印刷大写 `Π`，Markdown 写成小写 `π`；其 `H^0` function-space/Galois-action parenthetical 被 Markdown 粘连进值域。Proof a) 中印刷的 quotient `U_I\backslash\widetilde S^2(R)` 被写成 `U_I\setminus\widetilde S^2(R)`，且 ~Ω 项丢失维数上标 `2`；下一句 `H^1(Ω^2⊗k_∞^s,μ_n)` 被写成 `H^1(Ω⊗\widetilde{k}_∞^s,μ_n)`。Proof c) 在 complete archimedean field `K` 下印作 `K^s`，Markdown 多处沿用了 `k_∞^s`。均为内容级变量/对象差异，待全篇审计后逐处修复。
- 备注：页眉作者名与印刷页码 590 未收入 Markdown；300dpi 页图用于核对表示符号、维数上标与 Galois-field 标记。

## p.031（PDF p.31 / 印刷 p.591）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p031.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p031.png`
- 核对：Proposition 10.3 proof d)/e), harmonic-cochain and distribution construction, §11 representation/Galois setup, Theorem 2 statements, proof 1) map and proof 2) opening.
- 结果：FAIL。印刷 d) 的 quotient `U_I\backslash\widetilde S_0^2(R)` 被写成 `U_I\setminus\widetilde S_0^2(R)`；`V_I` 是 harmonic cochains on `\widetilde S^2`，Markdown 漏掉 tilde，且印刷 `\bar V=\varprojlim_I V_I` 被写成 `\vec V=\varinjlim_I V_I`。§11 开头与 `W_i` 的 Galois group/space 使用局部 `Gal(k_∞^s/k_∞)` 和 `k_∞^s`，Markdown 多处换成全局 `Gal(k^s/k)`/`k^s`；Theorem 2 的印刷层级是标题 “Theorem 2.” 加 numbered clauses `1)`、`2)`，Markdown 合并为 `Theorem 2.1)`。Theorem 2(2) 中 place `ν` 写成 `v`；proof 1) 的 `B⊂GL(2,𝔄_f)` 写成 `B⊂GL(2,𝔘_f)`。待全篇审计后逐处按源页修复。
- 备注：页眉题名与印刷页码 591 未收入 Markdown；300dpi 页图与裁片 `audit/300dpi/Drinfeld_1974_elliptic_modules_p031_limit_crop.png`、`audit/300dpi/Drinfeld_1974_elliptic_modules_p031_theorem_crop.png` 核对了 limit direction 与 Theorem 2 的编号层级。

## p.032（PDF p.32 / 印刷 p.592）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p032.png`（pngmono 150dpi）；300dpi 对读：`audit/300dpi/Drinfeld_1974_elliptic_modules_p032.png`
- 核对：Theorem 2 proof continuation through the Frobenius eigenvalue conclusion, final remark, received date, all 14 bibliography entries, and translator credit.
- 结果：FAIL。Theorem 2 proof prints `s ∈ H^0(\bar M^2 ⊗ k_∞^s, \bar Q_l)`; Markdown uses `k^s` in that occurrence. Bibliography items 1, 4, and 14 print author spelling `Pjateckii-Šapiro`; Markdown omits the accent in item 1 and relocates it as `Pjateckiš-Sapiro` in items 4 and 14. Markdown also omits the printed `Received 17/DEC/73` line and final `Translated by M. B. NATHANSON` credit.
- 备注：300dpi 页图核实了 bibliography spelling, received date, and translator line。

## 修复登记（2026-10-01）

- 原始 MinerU Markdown：Drinfeld_1974_elliptic_modules_mineru/Drinfeld_1974_elliptic_modules__Drinfeld_1974_elliptic_modules.md，原始提交 0b0f3dd237016302793972607504146adcf38004。
- 修订 Markdown：同一文件；手工修订提交 145706440e02f1e1d2b5793a2f70367421cc108e。
- 修订方式：在 32 页扫描件审计全部结束后，逐处使用 structured apply_patch 手工修改；未运行批量替换脚本。修订后重新从头至尾读取完整 Markdown（1136 行），对照已保存页图核验改动；git diff --check 通过。
- 下表“初审”状态针对原始 MinerU Markdown；“修复后”仅表示已核实差异按扫描件修订，不改变原始逐页审计签字。PASS± 表示正文可辨认，记录了页眉/页码未收入 Markdown。

| PDF页 | 初审 | 修复后 |
|---:|---|---|
| 1 | PASS± | 无内容修订 |
| 2 | PASS± | 无内容修订 |
| 3 | PASS± | 无内容修订 |
| 4 | FAIL | h(a) 符号差异已修订 |
| 5 | FAIL | h、映射 α ↦ p/π、q 与 Λ_O 差异已修订 |
| 6 | FAIL | Λ_O、height h、有限域与 f_a 差异已修订 |
| 7 | FAIL | h、τ、log_p q、degree/例子中的符号差异已修订 |
| 8 | FAIL | j_ν、q^b 差异及条件行数学定界已修订 |
| 9 | FAIL | τ、p^j 与递推等式左侧符号差异已修订 |
| 10 | FAIL | p^{-i}、height h 差异已修订 |
| 11 | FAIL | height h 与 m^r 差异已修订 |
| 12 | FAIL | 分量括号、h、π^n、\hat O^{nr} 等差异已修订 |
| 13 | FAIL | height/rank h、参数及点集差异已修订 |
| 14 | FAIL | rank 指数 j+h 差异已修订 |
| 15 | FAIL | intertwiner h、degree 指数、τ、系数下标差异已修订 |
| 16 | FAIL | X_I、Iν^n、place 符号差异已修订 |
| 17 | FAIL | place、系数、通用形变与层级对象差异已修订 |
| 18 | FAIL | 𝔄_f、商记号、矩阵及商空间差异已修订 |
| 19 | FAIL | 范数 ν_1,ν_2 与两个 supremum 记号差异已修订 |
| 20 | FAIL | log_q、范数 ν、求和指标、\bar S^d 与 “for” 差异已修订 |
| 21 | FAIL | α_d 与求和指标差异已修订 |
| 22 | FAIL | P_1 \xrightarrow{\sim} P_2 与带 tilde 的 S^d 差异已修订；X_{(j)} 原本符合印刷，未作最终改动 |
| 23 | FAIL | 带 tilde 的 Ω^d、求和/level 指标、同构符号、m_y 差异已修订 |
| 24 | FAIL | valuation 负号、rank d_1、φ 与 0 差异已修订 |
| 25 | FAIL | p^{-i}、p^k、𝔄_f、place ν 差异已修订 |
| 26 | FAIL | 矩阵、商记号与 place ν 差异已修订 |
| 27 | FAIL | 映射记号、空集与 H^0 差异已修订 |
| 28 | FAIL | O_X 下标差异已修订 |
| 29 | FAIL | divisibility 条件 n ∤ m 已修订 |
| 30 | FAIL | Π、H^0 作用说明、商记号、维数及 K^s 差异已修订 |
| 31 | FAIL | 商记号、\widetilde S^2、Theorem 2 编号、ν 与 𝔄_f 差异已修订 |
| 32 | FAIL | 参考文献作者拼写与译者行已修订 |

### 对初审记录的后续澄清

- p.005：全页审计完成后，使用已保存的 p.005 300dpi 裁片又确认 Proposition 1.4 proof 的 Λ_0 ⊗ K 应为印刷的 Λ_O ⊗ K；该处已在修订 Markdown 中改正。
- p.008：除 j_ν 和 q^b 外，Proposition 2.3(b) 条件行还修复了损坏的行内数学定界；公式内容按 p.008 页图保留。
- p.009：扫描原式为 (a^i-a)b_i = Σ a_j b_{i-j}^{p^j}。修订同时移除了原 Markdown 左侧多出的负号，并恢复 p^j 上标；两项均以 p.009 的 300dpi 页图核验。
- p.022：初审把 X_j/X_{(j)} 记为差异。300dpi 页图实际印作 X_{(j)}，与原始 Markdown 一致；修复过程中曾改动该处，全文复核时已恢复。该项不计为修订。相似同构与带 tilde 的 S^d 差异仍属真实错误并已修订。
- p.031：初审关于 d) 中 limit direction 的记录有误。扫描页印作 \bar V = \varinjlim_I V_I，原始 Markdown 也是该式；该行最终未作改动。初审所述 §11 Galois 作用误差也为 false positive：扫描页和原始 Markdown 的 §11 开头、W_i 的整体表示空间均使用全局 k^s/k，并在 W_i^ν 的限制处使用局部 k_ν^s/k_ν。真正差异（商记号、tilde、Theorem 2 编号、ν、𝔄_f）已修订。
- p.032：初审所述 Theorem 2 proof 中 k^s 差异不成立：扫描页和原始 Markdown 都印/写作 k^s，未作改动。Received 17/DEC/73 在原始 Markdown 中已经存在，也未改动。三条参考文献作者拼写差异及缺失的 Translated by M. B. NATHANSON 确认属实并已修订。
