# AUDIT-frey1986 — Links between stable elliptic curves and certain Diophantine equations

状态：Peer 候选审计；页级 `FAIL` 记录修复前发现，修复与全文复读见文末登记；仍待 Master-Luna 按 exact commit 独立复核并集成。

- actor=Peer-P06; model=gpt-6-luna; effort=max
- 共同基线：`e04c4a9603818cfa2d71271942f696115783c33b`；当前写入范围仅限 `1998年 - Wiles/`。
- PDF：`frey1986.pdf`，40 页；原件 SHA-256：`0f092a804000ad55d39506015516777fee288a4b8de65bb9e41a738cb6a87ab0`。
- 待审 MinerU Markdown：`frey1986_mineru/frey1986__frey1986.md`；审计前 SHA-256：`b9b5a5a56bba04f9a09f13ca90b88fab214a3c19df1ea4a82b191214ec7f74a6`。
- MinerU 导出：`structured_content.json` 与 `middle_json.json` 均登记 40 页，producer 为 MinerU 3.4.4；现有导出中没有 `doc_id` / `document_id` 字段。
- 页面模式：每个 PDF 页均含一张 795×1200、150 dpi JPEG 全页图，另带 OCR 文本层。虽提取文本为 59,827 bytes 且未见 U+FFFD，生产器为 PDF-XChange，页图与抽取文本均呈现扫描/OCR 特征，因此采用扫描件标准：每页渲染 150 dpi pngmono 后逐页目检；字形疑点用 300 dpi 原图裁片裁决。PDF 文本层仅辅助定位，不作为符号真值。
- 题名核对确认该 Markdown 对应本 PDF；Markdown 首行保留印刷两行题名的第二行，但遗漏第一行，详见 p.1。

## p.001（PDF p.1 / 印刷 p.1）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 15:51:15 EDT。
- PNG：`audit/frey1986_p001.png`（pngmono，150 dpi）；公式字形裁片：`audit/300dpi/frey1986_p001_equation.png`（pnggray，300 dpi）。
- 核对：题名、作者、引言开篇、定义 `C_{F_n}`、非平凡解条件与 Fermat 猜想陈述。
- 结果：FAIL。印刷题名为 “LINKS BETWEEN STABLE ELLIPTIC CURVES AND / CERTAIN DIOPHANTINE EQUATIONS”，Markdown 只保留第二行；印刷方程首符号为大写 `C_{F_n}`（300 dpi 裁片确认），Markdown 写成小写 `c_{F_n}`。二者均需在全篇审计结束后按印刷页逐处手工修复。
- 印刷原文 quirk：该页印为 “Falting's theorem”，Markdown 亦为 “Falting's theorem”；忠实保留，不按现代拼法擅改。

## p.002（PDF p.2 / 印刷 p.2）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 15:59:14 EDT。
- PNG：`audit/frey1986_p002.png`（pngmono，150 dpi）；300 dpi 符号裁片：`audit/300dpi/frey1986_p002_intro_symbols.png`、`audit/300dpi/frey1986_p002_representation_symbols.png`（pnggray）。
- 核对：引言关于素数指数、圆分域、无分歧表示与椭圆曲线的段落，至 “the Theorem on p. 15”。
- 结果：FAIL。印刷 “it follows that F_p is true” 被转成 Markdown `F_D`；印刷 `Gl_1(C)_p` 被转成 `G1_1(C)_p`（小写 `l` 误为数字 `1`）；印刷 `G_Q(ζ_p)` 在 “higher dimensional representations” 句被转成 `G_{\mathbb{G}(\zeta_p)}`。三处依原图修复。
- 排版级差异：印刷页眉 “2, G. Frey” 与页码未收入 Markdown；首次 `F_p` 在印刷中为下划线 F 加普通斜体 p，Markdown 使用粗体 F 与 Fraktur p，标签仍可辨为 `F_p`，暂列 PASS±，不因字体差异改动。

## p.003（PDF p.3 / 印刷 p.3）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:06:42 EDT。
- PNG：`audit/frey1986_p003.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p003_parametrization.png`、`audit/300dpi/frey1986_p003_differential.png`、`audit/300dpi/frey1986_p003_galois_and_equation.png`、`audit/300dpi/frey1986_p003_degree.png`（pnggray）。
- 核对：Taniyama–Shimura 参数化段、椭圆曲线微分与模形式、Galois 表示记号及两类猜想的引入，至句首 “If this conjecture would be true it would”。
- 结果：FAIL。印刷参数化式是 `X_0(N)`，Markdown 写 `X_o(N)`；印刷模形式所在曲线是 `X_0(N)`，Markdown 写 `X(N)`；两处印刷 Galois 记号均为 `G_Q`，Markdown 分别写 `G_0` 与 `G_n`；印刷方程记号 `C_{F_p}` 被写成 `C_F`。按页图恢复这些下标。
- 文字转写差异：印刷行末 `re-` / `corres-` 是 “resulting” / “corresponds” 的断行连字符，Markdown 保留换行后显示为 `re- sulting` / `corresponds- ponds`；收尾时将其逐处人工并回正常拼写。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 3 未收入 Markdown。

## p.004（PDF p.4 / 印刷 p.4）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:09:41 EDT。
- PNG：`audit/frey1986_p004.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p004_intro.png`、`audit/300dpi/frey1986_p004_point.png`、`audit/300dpi/frey1986_p004_weierstrass.png`（pnggray）。
- 核对：引言结尾、Section II / 1. Arithmetic of elliptic curves 的开篇定义，以及第一条 generalized Weierstraß 方程（至 PDF p.4 页底）。
- 结果：FAIL。印刷句为 “one Q-rational point P”，Markdown 写成 `F`；300 dpi 原页与同页 `P_{\infty}` 字形对照确认是 `P`。
- 文字转写差异：印刷 “con- / gruence primes” 是跨行断字；Markdown 当前保留为 `con-` 加下一行 `gruence`，需手工并回 `congruence`。
- 已吻合：`E/C` 与本页底部 `N_E: Y^2 + λXY + μY = X^3 + αX^2 + βX + γ`；未按数学记忆改写原式。
- 排版级差异：印刷页眉 “4, G. Frey” 与页码 4 未收入 Markdown。

## p.005（PDF p.5 / 印刷 p.5）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:13:09 EDT。
- PNG：`audit/frey1986_p005.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p005_polynomial.png`、`audit/300dpi/frey1986_p005_discriminant.png`、`audit/300dpi/frey1986_p005_scaling.png`、`audit/300dpi/frey1986_p005_j_invariant.png`（pnggray）。
- 核对：约化 Weierstraß 方程、判别式、尺度变换与 j-invariant，至 Hasse invariant 公式引入。
- 结果：FAIL。印刷判别式的系数为 `27`，Markdown 写成 `2 7`；印刷 j-invariant 的因子是 `12^3`，Markdown 写成 `1 2^3`；印刷名词 `Weierstraß` 在一处被转成希腊字母 `β`（Markdown `Weierstraβ`）。均按 300 dpi 裁片修复。
- 源字形歧义：非奇异条件和判别式不等式中的末字符均为无斜线圆形字形；150/300 dpi 下不足以可靠区分大写 `O` 与数字 `0`。保持该字形歧义，不按数学预期改写。
- 已吻合：两种 Weierstraß 方程及尺度变换中的 μ²、μ³、μ⁻⁴、μ⁻⁶、μ⁻¹²。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 5 未收入 Markdown。

## p.006（PDF p.6 / 印刷 p.6）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:17:31 EDT。
- PNG：`audit/frey1986_p006.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p006_reduction_equation.png`、`audit/300dpi/frey1986_p006_good_reduction_criterion.png`、`audit/300dpi/frey1986_p006_definition.png`（pnggray）。
- 核对：Hasse invariant 公式、generalized Weierstraß 模型、素数约化记号与 good reduction 定义。
- 结果：FAIL。印刷在本页以小写素数变量 `l` 贯穿 “Let l be a prime”、`F_l = Z/l`、`N_E(l)`、`E^{(l)}`、`l ≠ 2,3`、各个 `v_l` 与 “mod l”；Markdown 相应位置多处写成数字 `1`（例如 `F_1 = Z/1`、`E^{(1)}`、`v_1`、`N_E(1)`）。300 dpi 页图确认这组重复记号是同一个变量 `l`，须逐处修复。
- 印刷原文 quirk：本页 reduction-theory 方程印为 `… + βY + γ`，Markdown 与原图一致；p.4 的 generalized Weierstraß 方程相应项印为 `βX`。保留这一处印刷差异，不按前页公式改成本页 `βX`。
- 已吻合：Hasse invariant 与 good-reduction 判据的其他已核系数和项。
- 排版级差异：印刷页眉 “6, G. Frey” 与页码 6 未收入 Markdown。

## p.007（PDF p.7 / 印刷 p.7）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:20:44 EDT。
- PNG：`audit/frey1986_p007.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p007_multiplicative.png`、`audit/300dpi/frey1986_p007_stable_reduction.png`（pnggray）。
- 核对：multiplicative / additive reduction 分类、Tate 型条件、stable reduction 定义及非奇异点说明，至页末 “split by”。
- 结果：FAIL。印刷的素数变量为小写 `l`；Markdown 多处写成数字 `1`，包括 `E^{(1)}`、`v_1`、`N_E(1)`、`mod 1` 和 “unramified in 1”。逐处恢复为 `l`，但 case labels `1.` / `2.` / `3.` 保留数字。印刷为 `Q(√δ_E)` 的根式，Markdown 写成 `Q(√δ)_E`，下标 `E` 应留在根号内。印刷断行词 `singu- / larity` 与 `differ- / ent` 在 Markdown 中形成断开的词，须在复核阶段合并为 `singularity` 与 `different`。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 7 未收入 Markdown。

## p.008（PDF p.8 / 印刷 p.8）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:26:22 EDT。
- PNG：`audit/frey1986_p008.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p008_tate.png`、`audit/300dpi/frey1986_p008_radical_and_primes.png`、`audit/300dpi/frey1986_p008_divisor_glyph.png`（pnggray）。
- 核对：Tate uniformization 陈述、从稳定乘法约化得到的局部域结论与 good-reduction 非分歧结论。
- 结果：FAIL。印刷的域为 `Q_l`，Markdown 多处写 `Q_1`；素数变量 `l` 在 “mod l”、“Let l be a divisor of l”、“l ≠ p” 与 “l is unramified” 等位置被识别成数字 `1`；`K_p` 是由扭点坐标添入 `Q` 得到，Markdown 写成添入 `G`。印刷末式是 `K_{p,l}=Q_l(ζ_p, √[p]{j_E})`，Markdown `Q(ζ_p, P ∨ j_E)` 未保留 `Q_l` 下标与 p 次根，依 300 dpi 裁片恢复。
- 排版级差异：印刷页眉 “8, G. Frey” 与页码 8 未收入 Markdown。

## p.009（PDF p.9 / 印刷 p.9）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:29:31 EDT。
- PNG：`audit/frey1986_p009.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p009_definition_proposition.png`、`audit/300dpi/frey1986_p009_prime_criterion.png`、`audit/300dpi/frey1986_p009_minimal_equation.png`（pnggray）。
- 核对：稳定椭圆曲线定义、Proposition 1 的非分歧条件、minimal Weierstraß equation 的引入与方程。
- 结果：FAIL。印刷稳定性定义、Proposition 1 与 “unramified over Q” 均写 `Q`，Markdown 相应位置写成 `G`；素数变量 `l` 在 “all primes l”、“mod l”、“l ≠ p” 与 `v_l(j_E)` 中写成数字 `1`；`Weierstraß` 两处被转成 `Weierstraβ`。依据 300 dpi 原页逐处恢复。
- 已吻合：页底 minimal equation 的 `βX` 项与判别式记号，未套用前页印刷方程的 `βY`。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 9 未收入 Markdown。

## p.010（PDF p.10 / 印刷 p.10）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:32:41 EDT。
- PNG：`audit/frey1986_p010.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p010_conductor.png`、`audit/300dpi/frey1986_p010_kp.png`、`audit/300dpi/frey1986_p010_weierstrass.png`、`audit/300dpi/frey1986_p010_hasse.png`（pnggray）。
- 核对：稳定曲线的判别式/导体关系、Section 2 的 Frey 曲线构造、Weierstraß 变换与 Hasse invariant。
- 结果：FAIL。印刷 `l` 素数变量在判别式/导体公式中被转成 `1`；对应域印为 `K_p`，Markdown 正文一处写成 `K_n`；Weierstraß 变换系数印为 `1/27`，Markdown 拆成 `1/2 7`；Hasse invariant 的剩余类域印为 `Q^{*2}`，Markdown 写成 `G^{*2}`。按裁片逐处修复。
- 已吻合：曲线 `Y^2 = X^3 + (A+B)X^2 + ABX`、判别式 `A^2B^2C^2` 与 j-invariant 因子。
- 排版级差异：印刷页眉 “10, G. Frey” 与页码 10 未收入 Markdown。

## p.011（PDF p.11 / 印刷 p.11）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:35:15 EDT。
- PNG：`audit/frey1986_p011.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p011_divisibility.png`、`audit/300dpi/frey1986_p011_radical.png`、`audit/300dpi/frey1986_p011_prime_criterion.png`（pnggray）。
- 核对：Frey 曲线性质 i–ii、模 3 的约化情形、一般素数 `l` 的约化判据，至 conductor 公式引出。
- 结果：FAIL。印刷 `3 ∤ A·B·C` 被写成 `3/A·B·C`；印刷 `A ≠ B (mod 3)` 被写成 `A \nmid B`；`Q(√δ_E)` 的根号被转成字母 `V`；`B mod Q_2^{*2}` 粘成 `Bmod Q_2^{*2}`；一般素数 `l` 在多处被写成数字 `1`（`If 1 is a prime`、`mod 1`、`v_1`、`1|A^2B^2C^2`）。均由页图确认，待全篇结束后按位置逐处修复。
- 已吻合：`A-B=C ≠ 0 (mod 3)`、`v_3(j_E)=-v_3(Δ)<0` 与同页各有明文数字 2、3 的位置。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 11 未收入 Markdown。

## p.012（PDF p.12 / 印刷 p.12）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:38:04 EDT。
- PNG：`audit/frey1986_p012.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p012_conductor.png`、`audit/300dpi/frey1986_p012_minimal_equation.png`、`audit/300dpi/frey1986_p012_radical_field.png`、`audit/300dpi/frey1986_p012_fermat_type.png`（pnggray）。
- 核对：导体乘积、Frey 曲线 iii–iv、p 次根式局部域扩张、Fermat-type 方程定义与所得曲线判别式，至 “and conductor”。
- 结果：FAIL。导体乘积中的素数 `l` 被转成数字 `1`；minimal equation 的系数印为 `AB/16`，Markdown 拆成 `AB/(1 6)`；印刷扩张商的底域为 `Q(√[p]{2^4 ABC})`，Markdown 写成 `G(\underline{p}√{2^4 ABC})`，并未保留 `Q` 与清楚的 p 次根式。按原页修复。印刷行末 `corres- / ponding` 在 Markdown 中造成断词，须合并为 `corresponding`。
- 已吻合：Fermat-type 方程的指数、整数互素条件及由 `A,B,C` 导出的判别式幂次。
- 排版级差异：印刷页眉 “12, G. Frey” 与页码 12 未收入 Markdown。

## p.013（PDF p.13 / 印刷 p.13）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:40:53 EDT。
- PNG：`audit/frey1986_p013.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p013_conductor.png`、`audit/300dpi/frey1986_p013_equation.png`、`audit/300dpi/frey1986_p013_proposition2.png`（pnggray）。
- 核对：导体乘积与不等式、Fermat 方程下的 Proposition 2、最小方程、判别式与命题脚注。
- 结果：FAIL。印刷导体乘积中用小写 `l` 表示素数，Markdown 两处均写数字 `1`；最小方程乘积系数印为 `z_1^p z_2^p / 16`，Markdown 拆成 `/ (1 6)`。按原页逐处修复。
- 已吻合：Proposition 2 的 `2|z_1`、`z_2 ≡ 1 (mod 4)`、Frey 判别式幂次及脚注 1 内容。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 13 未收入 Markdown。

## p.014（PDF p.14 / 印刷 p.14）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:44:07 EDT。
- PNG：`audit/frey1986_p014.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p014_kummer_local.png`、`audit/300dpi/frey1986_p014_converse_assumptions.png`、`audit/300dpi/frey1986_p014_curve_and_discriminant.png`（pnggray）。
- 核对：Proposition 2 的 Kummer 局部结论、Fermat 曲线/稳定曲线的“逆向”假设、Weierstraß 模型与判别式因式分解，至 `gcd(B,A^2-4B)=1`。
- 结果：FAIL。印刷假设中 `K_p` 在 Markdown 一处写成 `K_n`；300 dpi 假设行确认该下标为 `p`，依图修复。
- 未闭合字形：局部结论里的 `p|p` 以及 completion “with respect to p” 所指的 prime divisor，300 dpi 图呈现较重的首 glyph，但不足以可靠断定是否印为 Fraktur 𝔭；修复稿保留其 prime-divisor 语义，具体字体形态仍登记为未知，不从语境断言原印字字体。
- 已吻合：本页 `N_E: Y^2=X^3+AX^2+BX`、`B^2(A^2-4B)=u^{2p}` 与有理域假设。
- 排版级差异：印刷页眉 “14, G. Frey” 与页码 14 未收入 Markdown。

## p.015（PDF p.15 / 印刷 p.15）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:47:40 EDT。
- PNG：`audit/frey1986_p015.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p015_power_equations.png`、`audit/300dpi/frey1986_p015_theorem.png`（pnggray）。
- 核对：`A^2-4B` 与 `B` 的幂分解、`z_1,z_2` 的构造、Fermat 方程与椭圆曲线条件等价定理，至 theorem 条件 ii 的分歧陈述。
- 结果：FAIL。印刷 `B=w^P`，Markdown 写成格式损坏的 `B = w$^{p}`；多处显示幂在印刷中为大写 `P`（如 `(A−v^P)(A+v^P)=4B=4w^P`、`2v^P` 与定理 1 的 `Z_1^P−Z_2^P=Z_3^P`），Markdown 的部分对应项使用小写 `p`。按印刷大小写逐处恢复；相邻正文中的小写 prime `p` 保持不变，登记为源页大小写差异，不做数学规范化。
- 已吻合：`A^2−4B=v^{2p}`、`z_1^p z_2^p=B` 及定理条件中的 `p≥5`。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 15 未收入 Markdown。

## p.016（PDF p.16 / 印刷 p.16）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:50:06 EDT。
- PNG：`audit/frey1986_p016.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p016_theorem_first_case.png`、`audit/300dpi/frey1986_p016_modular_curve.png`（pnggray）。
- 核对：等价定理第三条件、Fermat “first case” 备注、Section III 的 `X_0(N)`、`Γ_0(N)` 与上半平面商定义，至页末 “…is equal to H*/Γ_0(N) as”。
- 结果：FAIL。印刷 `2^8 Δ_E ∈ Z^{2p}` 的变量是大写 `Z`，Markdown 写小写 `z`；印刷 `p ∤ z_1z_2z_3` 与 `p ∤ Δ_E` 被转成普通斜杠；印刷 `X_0(N)` / `Γ_0(N)` / `SL(2,Z)` 在 Markdown 对应位置出现 `X_o(N)` / `Γ_o(N)` / `S1(2,Z)`；印刷扩充上半平面集合含 `i·∞`，Markdown 写为分离的 `i, ∞`。据裁片逐处恢复。
- 已吻合：定理条件 iii 的 `Min(0,v_p(j_E)) ≡ 0 ≡ v_2(j_E)-8 (mod p)`，以及模曲线的 `N`、`Z` 域字段。
- 排版级差异：印刷页眉 “16, G. Frey” 与页码 16 未收入 Markdown。

## p.017（PDF p.17 / 印刷 p.17）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 16:53:42 EDT。
- PNG：`audit/frey1986_p017.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p017_transformation.png`、`audit/300dpi/frey1986_p017_cusps.png`、`audit/300dpi/frey1986_p017_differential.png`、`audit/300dpi/frey1986_p017_endomorphisms.png`（pnggray）。
- 核对：模形式的变换规则、尖点集合、Fourier 展开、微分与 cusp form 的对应关系，以及 Ribet 的 endomorphism 等式。
- 结果：FAIL。印刷变换规则的群是 `Γ_0(N)`，Markdown 写 `Γ_o(N)`；印刷 cusp 集合含 `q ∈ Q`，Markdown 写 `q ∈ G`；印刷微分式为 `ω = f dq/q`，Markdown 将 `ω` 写成 Latin `w`；Endomorphism 等式中的 `J_0(N)` 在 Markdown 写作 `J_o(N)`。按 300 dpi 裁片恢复。
- 已吻合：变换因子 `(cz+d)^2`、Fourier 参数 `q=e^{2πiz}`、归一化条件 `a_1=1` 与权重 2。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 17 未收入 Markdown。

## p.018（PDF p.18 / 印刷 p.18）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 17:49:19 EDT。
- PNG：`audit/frey1986_p018.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p018_hecke.png`、`audit/300dpi/frey1986_p018_z_structure.png`、`audit/300dpi/frey1986_p018_modular_curve.png`、`audit/300dpi/frey1986_p018_restriction.png`（pnggray）。
- 核对：Hecke/Fricke endomorphisms 与 Jacobian、Z-structure/cusp forms、modular elliptic curve 定义及参数化映射。
- 结果：FAIL。印刷等式中的 `J_0(N)` 在 Markdown 写为 `J_o(N)`；定义与参数化映射中的 `J_0(N)` / `X_0(N)` 也出现 `o` 代替数字 `0`；印刷微分系数是 Greek `ω`，Markdown 写成 Latin `w`。按裁片恢复。
- 未闭合字形：印刷 `ω|Z` 中竖线后的 `Z` 是否为下标无法从当前 300 dpi 裁片可靠区分；先保留 Markdown 现状，不擅自更改层级。
- 排版级差异：印刷页眉 “18, G. Frey” 与页码 18 未收入 Markdown。

## p.019（PDF p.19 / 印刷 p.19）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 20:27:45 EDT。
- PNG：`audit/frey1986_p019.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p019_parametrization.png`、`audit/300dpi/frey1986_p019_differential.png`、`audit/300dpi/frey1986_p019_hecke.png`（pnggray）。
- 核对：strong parametrization 定义、Néron differential、cusp form Fourier 展开与 Hecke eigenvalue 事实，至页末 “and”。
- 结果：FAIL。印刷两处参数化映射为 `X_0(N)→E`，Markdown 写 `X_o(N)`；印刷 differential 字形为 `ω`，对应公式中的 `φ^*ω`，转写误作 `w`；印刷 “primes l ∤ N”、系数 `a_l` 与 Hecke operator `T_l` 被转写为 `1/N`、`a_i` 与 `T_1`。按 300 dpi 页图恢复。
- 已吻合：Néron differential `dX/(2Y+λX+μ)`、Fourier 因子 `dq/q`、`c=1 or 4`。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 19 未收入 Markdown。

## p.020（PDF p.20 / 印刷 p.20）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 21:27:37 EDT。
- PNG：`audit/frey1986_p020.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p020_eichler_shimura.png`、`audit/300dpi/frey1986_p020_representation.png`（pnggray）。
- 核对：Eichler–Shimura 特征值公式、Taniyama–Shimura conjecture、Serre modular representation 定义及 Frobenius trace 判据，含脚注 2。
- 结果：FAIL。印刷的特征值公式为 `a_l=1+l−#E^{(l)}(F_l)`，Markdown 写成 `a_1=1+1−#E^{(1)}(IF_1)`；定义表示的 Galois 群底域为 `Q`，Markdown 写成 `G`；印刷有限域为 `F_p`，Markdown 加了 Fraktur 下标；Frobenius 判据中的素数变量为 `l`，特定特征值为 `b_l`，Markdown 写 `1` / `b_1`。依 300 dpi 裁片逐处恢复。
- 已吻合：表示维数 2、级别 M、权重 k、Hecke eigenform 条件及脚注 2 的内容。
- 排版级差异：Markdown 将印刷页眉中的 “G. Frey” 保留为孤立行，但未收入页码 20。

## p.021（PDF p.21 / 印刷 p.21）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 22:39:40 EDT。
- PNG：`audit/frey1986_p021.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p021_representation.png`、`audit/300dpi/frey1986_p021_criterion.png`、`audit/300dpi/frey1986_p021_conjecture_s.png`（pnggray）。
- 核对：representation unramified 定义、Serre 的 finite-in-p 条件与 Kummer 判据、Conjecture S 的前半。
- 结果：FAIL。印刷 Galois 群为 `Gal(Q̄/Q)`，Markdown 分母为 `G`；印刷在素数 `l` 上 unramified，Markdown 写为 `1`；Definition 中印刷主体为 `ρ`，Markdown 写成 `p`；Criterion 中 kernel 属于 `ρ`，Markdown 写成 `p`，局部域下标在印刷中为 p-like prime symbol，Markdown 写 `K_h`，且 Kummer 字段式印 `Q_p(ζ_p, √[p]{a})`、Markdown 写成 `G_p(ζ_p, P ∀ a)`；Conjecture S 第 1 条印 `ρ` 和 `p ∤ M`，Markdown 写成 Fraktur `p` 与 `p/M`。依页图逐处修复。修复稿以 `K_{\mathfrak p}` 表示 prime-ideal role；局部域下标是否为 Fraktur 的字形层级仍未知。
- 已吻合：群方案类型 `(p,p)`、`v_p(a) ≡ 0 (mod p)`、权重 2 及 Conjecture S 第 2 条起始。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 21 未收入 Markdown。

## p.022（PDF p.22 / 印刷 p.22）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-01 23:48:17 EDT。
- PNG：`audit/frey1986_p022.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p022_serre_and_fermat.png`、`audit/300dpi/frey1986_p022_first_case.png`（pnggray）。
- 核对：Conjecture S 第 2 条结尾、Fermat 方程经 Frey 曲线导出的不可约性论证、RESULT 与第一种情形备注，并核对第二种 Fermat-type 方程开头。
- 结果：FAIL。印刷 “Then ρ is a modular representation” 被转成 `Then p`；“Conjecture S implies ρ_E” 被转成 `ρ_F`；第一种情形的 `p ∤ z_1z_2z_3` 被写成普通斜杠；第二种方程的显示指数在原页为大写 `P`，Markdown 写成小写 `p`。按裁片保留原页大小写并逐处修复。
- 已吻合：不可约性结论、`X_0(2)` 的 genus 0、RESULT 的逻辑文字及第二种方程系数结构。
- 排版级差异：印刷页眉 “22, G. Frey” 与页码 22 未收入 Markdown。

## p.023（PDF p.23 / 印刷 p.23）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 00:13:30 EDT。
- PNG：`audit/frey1986_p023.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p023_index_products.png`、`audit/300dpi/frey1986_p023_sprime_conductors.png`、`audit/300dpi/frey1986_p023_modular_form_trace.png`（pnggray）。
- 核对：Fermat-type 方程对应的 `N'`、genus 条件、S' 的 conductor 与模形式/Hecke 系数条件，至下一节 “Conditions on the degree…” 的开头不等式。
- 结果：FAIL。印刷素数变量 `l` 在两个乘积定义和 “almost all primes” 中被转成 `1`；`X_0(N')` 被写作 `X_o(N')`；S' 的 `N'` 乘积条件是 `Min{0,v_l(j_E)} ≢ 0 (mod p)` 且每项乘 `l`，Markdown 既写 `v_1` / `≠ 0` 又漏掉乘积项 `l`；印刷底域为 `Q`，Markdown 写 `G`，有限域是 `F_p`，Markdown 写 `IF_p`；印刷 Hecke 系数条件含点数符号 `#E^{(l)}` 且系数为 `a_l`，Markdown 写成 `1/n·E^{(1)}` 与 `a_i`。均据 300 dpi 裁片逐处修复。
- 已吻合：较一般 Fermat-type 方程的三组系数/指数结构及本页底部 `2^8Δ_E ≥ N^{2p}`。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 23 未收入 Markdown。

## p.024（PDF p.24 / 印刷 p.24）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 00:18:08 EDT。
- PNG：`audit/frey1986_p024.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p024_hyperbolic_set.png`（pnggray）。
- 核对：Szpiro conjecture 陈述及其 function-field 背景、由参数化估计导入的 `N_E` 方程和 `H` 定义。
- 结果：FAIL。页底 `N_E` 方程中印刷 `z_1^P`, `z_2^P` 的显示指数为大写 `P`，Markdown 使用小写 `p`；依 300 dpi 原页保留印刷大小写，不依据相邻小写 p 统一。
- 已吻合：Szpiro 的 `|Δ_{\widetilde E}| ≤ N^c`、`c=6` 的 function-field 说明及本页的 `X_0(N)` 参数化语句。
- 排版级差异：印刷页眉 “24, G. Frey” 与页码 24 未收入 Markdown。

## p.025（PDF p.25 / 印刷 p.25）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 00:23:55 EDT。
- PNG：`audit/frey1986_p025.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p025_integral_volume.png`、`audit/300dpi/frey1986_p025_g2_volume.png`、`audit/300dpi/frey1986_p025_conjecture_d.png`（pnggray）。
- 核对：参数化积分恒等式、Vol(E) 与判别式的比较、degree 下界及 Conjecture D 的开头。
- 结果：FAIL。印刷 `g_2` 展开中的显示指数为大写 `P`（`z_1^{2P}+z_2^{2P}-z_1^Pz_2^P`），Markdown 对应处用小写 `p`，按本页印刷大小写恢复。
- 排版级差异：积分等式中的 `Vol(E)` 在 Markdown 写成 `V o l (E)`；该断裂妨碍检索，待修复时手工并回 `Vol(E)`。
- 已吻合：`2^δ` 积分等式的系数、`Δ_E^{-1/6}` 估计与 Conjecture D 的 morphism 声明。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 25 未收入 Markdown。

## p.026（PDF p.26 / 印刷 p.26）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 00:42:47 EDT。
- PNG：`audit/frey1986_p026.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p026_diagram.png`、`audit/300dpi/frey1986_p026_isogeny_and_level.png`、`audit/300dpi/frey1986_p026_degree_bound.png`（pnggray）。
- 核对：Conjecture D 的因子分解映射与度数界、任意 stable elliptic curve 的推论及 Remarks 1。
- 结果：FAIL。印刷图中的底曲线为 `X_0(N)`，Markdown 写 `X_o(N)`；随后参数化 map `X_0(N)→\widetilde E` 被写为 `X_α(N)→\widetilde E`；印刷 `isogenous` 被转成 `isogenou:`；行末断词 `parame- / trized` 在 Markdown 形成断开的词，需恢复 `parametrized`。
- 已吻合：`ψ_2∘ψ_1=φ`、`deg(ψ_2)≤N^d`、Hurwitz bound 与 degree estimate。
- 页眉文字：此页印刷页眉为 “G. Frey”，Markdown 保留为孤立行；页码 26 未收入正文。

## p.027（PDF p.27 / 印刷 p.27）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 00:48:57 EDT。
- PNG：`audit/frey1986_p027.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p027_general_fermat.png`、`audit/300dpi/frey1986_p027_serre_cancellation.png`、`audit/300dpi/frey1986_p027_congruence_prime.png`（pnggray）。
- 核对：SZ/(D+TS) 对 Fermat-type 方程的推论、Conjecture S 的 level cancellation 及 congruence-prime 弱形式，至 Remark 2 的方程。
- 结果：FAIL。印刷 Galois 群底域是 `Q`，Markdown 写成 `C`；Conjecture S 中素数 `l` 的 `l ∤ p`、`l || M` 与 “l can be cancelled” 多处写成数字 `1`；弱形式印为 cusp form `g ≠ f`，Markdown 写成 `g 1/f`。依 300 dpi 原图逐处修复。
- 已吻合：单调指数函数 `α_i(n)` 与三项 Fermat-type 方程结构、`f ≡ g (mod p)` 及结尾 “p is a congruence prime”。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 27 未收入 Markdown。

## p.028（PDF p.28 / 印刷 p.28）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 00:54:10 EDT。
- PNG：`audit/frey1986_p028.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p028_parametrization.png`（pnggray）。
- 核对：congruence number `r` 的定义与等价刻画、Petersson pairing 关系，以及 strong modular parametrization 的引入，至映射 `φ:X_0(N)→E`。
- 结果：FAIL。印刷底曲线为 `X_0(N)`，Markdown 该映射写成 `X_o(N)`；300 dpi 裁片确认下标是数字 `0`。
- 已吻合：`L=⟨f⟩^⊥`、congruence number 的定义和 `r` 的两种代数刻画。
- 排版级差异：印刷页眉 “28, G. Frey” 与页码 28 未收入 Markdown。

## p.029（PDF p.29 / 印刷 p.29）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 01:00:25 EDT。
- PNG：`audit/frey1986_p029.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p029_first_step.png`、`audit/300dpi/frey1986_p029_isogeny_split.png`、`audit/300dpi/frey1986_p029_hecke_algebra.png`（pnggray）。
- 核对：Proposition 3 (Hida) 的 first/second/third steps，含 dual map、isogeny splitting、Ribet 的 Hecke algebra 关系，至 denominator `n|m`。
- 结果：FAIL。印刷 `A:=ker(φ_*)`，Markdown 漏掉下标星号；isogeny 映射印为 `β(b,a)=φ^*(b)−a`，Markdown 数学片段破损；端同态分解中的 `J_0(N)` 被写为 `J_Q(N)`；Ribet 关系 `T⊗Q` 被识别为 `T 2 Q`；参数化映射中的 `X_0(N)` 写成 `X_o(N)`。依 300 dpi 原页修复。
- 已吻合：Proposition 3 的命题 “deg φ divides r”、`A∩φ^*(E)=E_n` 及 denominator `n|m`。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 29 未收入 Markdown。

## p.030（PDF p.30 / 印刷 p.30）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 01:07:50 EDT。
- PNG：`audit/frey1986_p030.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p030_conductor.png`、`audit/300dpi/frey1986_p030_parametrization.png`、`audit/300dpi/frey1986_p030_proposition4.png`（pnggray）。
- 核对：Zagier pairing/remark、stable modular elliptic curve 的参数化与 conductor、Proposition 4 的前半假设，至页末 “E (and”.
- 结果：FAIL。印刷 `X_0(N)`、`J_0(N)` 两处被转成 `X_o(N)` / `J_o(N)`；conductor 乘积中的 `l` 与 `v_l` 被写成 `1` / `v_1`；Proposition 4 的 odd prime `l` 与 `l^{p^k} | Δ_E` 也被转成数字 `1`。由 300 dpi 原页逐处修复。
- 已吻合：pairing 把 Hecke operator 作用的 first Fourier coefficient 送到 `Z`、Zagier 结论 `deg φ | r` 及 `E^* = φ^*(E)` 的包含关系。
- 排版级差异：印刷页眉 “30, G. Frey” 与页码 30 未收入 Markdown。

## p.031（PDF p.31 / 印刷 p.31）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 01:14:03 EDT。
- PNG：`audit/frey1986_p031.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p031_proposition4.png`、`audit/300dpi/frey1986_p031_neron_components.png`、`audit/300dpi/frey1986_p031_local_components.png`（pnggray）。
- 核对：Proposition 4 的 kernel 结论与 Deligne–Rapoport/Mazur Néron component 论证，直至本页脚注 3。
- 结果：FAIL。印刷的有理域/有理点记号 `Q`、`Q̄` 被转成 `G`、`Ḡ`；素数 `l` 与 residue field `F_l` 多处变成 `1` / `F_1`；Jacobian 下标 `0` 转为 `o`，component indices `C_i^0,C_0^0` 也有 `o/0` 混淆；印刷 prime-divisor 标记在 “divisor … of Q(P)” 被转成 `!|1 of G(P)`。据 300 dpi 裁片修复其 prime-divisor 角色与 `l`；修复稿以 `\mathfrak{l} \mid l` 转写，但首 glyph 的确切字体仍无法判定，故字形状态保留未知。
- 已吻合：cusp divisor `c=(0)-(∞)`、order ratio `order(c)/3` 与脚注 3 的原文内容。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 31 未收入 Markdown。

## p.032（PDF p.32 / 印刷 p.32）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 01:21:32 EDT。
- PNG：`audit/frey1986_p032.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p032_local_components.png`、`audit/300dpi/frey1986_p032_corollary.png`、`audit/300dpi/frey1986_p032_remark_and_example.png`（pnggray）。
- 核对：Proposition 4 proof 的 local-component 推论、Corollary、p=2 remark、congruence-number 条件，及例子首句。
- 结果：FAIL。印刷 `P mod l` 在 Markdown 写成 `P mod I`；印刷 “no Q-rational isogeny” 在 Corollary proof 里写成 `G-rational`；印刷 `l^{p^k}|A·B·C` 被写成 `1^{p^k}|A·B·C`。按原页裁片恢复。
- 已吻合：Corollary 中 `f ≠ g`、`f ≡ g (mod p^k)`，p=2 remark 的 `A-B=C` 条件与 example 首句。
- 排版级差异：印刷页眉 “32, G. Frey” 与页码 32 未收入 Markdown。

## p.033（PDF p.33 / 印刷 p.33）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 01:28:13 EDT。
- PNG：`audit/frey1986_p033.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p033_example.png`、`audit/300dpi/frey1986_p033_prop4prime.png`、`audit/300dpi/frey1986_p033_footnote.png`（pnggray）。
- 核对：Frey curve 78B 例子、Proposition 4′ 的对象和条件 i–iii、脚注 4。
- 结果：FAIL。印刷开头为 `For l ≠ p`，Markdown 写成损坏的 `For 1 1/4 p`；条件 ii 印 `Q(C^*)=Q(C)`，Markdown 混写为 `Q(C^*)=G(C)`；印刷 prime divisor 是 `l|N`，条件 iii 是 reduction `mod l`，Markdown 写为 `I|1` / `mod I`；印刷 `A(\overline{Q})_{p^k}` 被转成 `A(\overline{C})`。示例方程 `Y^2=X^3+269X^2+2^8·13X` 的 `269` 与 `13` 分别被拆成 `2 6 9`、`1 3`。据裁片逐处修复。
- 印刷原文 quirks：本页 example 对曲线 78B 使用拼法 “isogeneous”，修复稿保留；脚注 4 的英文原文重复 “for for”，修复稿也忠实保留。
- 已吻合：78B 的导体与 5 为 congruence prime 的说明、条件 i `C^*≥C≥(Z/p^k)^2`。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 33 未收入 Markdown。

## p.034（PDF p.34 / 印刷 p.34）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 01:35:06 EDT。
- PNG：`audit/frey1986_p034.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p034_consequence.png`、`audit/300dpi/frey1986_p034_proposition5.png`、`audit/300dpi/frey1986_p034_quotient_map.png`（pnggray）。
- 核对：Proposition 4 推出的 abelian subvarieties、norm-map kernel、Proposition 5 条件与 quotient map。
- 结果：FAIL。印刷多处 `J_0(N)`、component superscript `0` 与 prime `l` 在 Markdown 分别写成下标 `o`、字母 `o` 或数字 `1`；Proposition 5 条件印为 `l ≠ 1 (mod p)`，Markdown 两侧都写 `1`；Néron model 中 `mod l` 与 `N/l` 被写作 `mod 1` / `N/1`。依据 300 dpi 裁片逐处恢复。
- 已吻合：`A_1,…,A_t` 的排序、`t<k` 与商 `J_0(N)/K=A/K×B/K` 的结构。
- 排版级差异：印刷页眉 “34, G. Frey” 与页码 34 未收入 Markdown。

## p.035（PDF p.35 / 印刷 p.35）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 01:43:10 EDT。
- PNG：`audit/frey1986_p035.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p035_connected_components.png`、`audit/300dpi/frey1986_p035_local_fields.png`（pnggray）。
- 核对：Proposition 5 归约到 totally degenerated reduction 的 setup、isogeny `α`、unramified extension `K/Q_l` 与 uniformization lattices，至 `G_m^d/Γ`。
- 结果：FAIL。印刷的 Jacobian 下标与 component superscript 使用数字 `0`，Markdown 多处写小写 `o`；素数 `l` / completion `Q_l` 在约化条件、component map 与 Galois base 中多次被转成 `1` / `Q_1`；`E'/Q` 与 `B/Q` 在 Markdown 写为 `G`；`v_l(j_{E'})` 被写成 `v_1`。按页图逐处恢复。
- 已吻合：isogeny `α(Ẽ)=E'`、`Ker(α)∩Ẽ={0}` 与 lattice/uniformization 的主要结构。
- 印刷原文 quirk：本页两处将 “isogenous” 印为 “isogeneous”；正文保留印刷拼法，并保留印刷语法 “There are an elliptic curve”。
- 字形未知：local-field prime divisor 的首 glyph 以 `l` 转写；它承担 prime-divisor 角色，但当前裁片不足以确认原印字是否 Fraktur。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 35 未收入 Markdown。

## p.036（PDF p.36 / 印刷 p.36）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 01:50:08 EDT。
- PNG：`audit/frey1986_p036.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p036_fields_isogeny.png`、`audit/300dpi/frey1986_p036_galois_maps.png`（pnggray）。
- 核对：uniformization-isogeny lattice map、Gal-equivariance identities、Tate/non-Tate sign ε(σ) 与 p-torsion roots-of-unity tuple，至页末 “unity”。
- 结果：FAIL。印刷的 residue/local field is `Q_l`，Markdown 多处写 `Q_1`；相应的 Galois groups 应以 `Q_l` 为底，Markdown 写 `G_1`（如 `G(K_p·K/Q_l)`）。据 300 dpi 页图恢复。注意 `Γ_1` 是 lattice 的编号 1，不随 prime `l` 改写。
- 已吻合：`γ_2∘α=\tilde α∘γ_1`、ε(σ) 的 Tate/非 Tate 分段与 p 次单位根 tuple 的论证结构。
- 排版级差异：印刷页眉 “36, G. Frey” 与页码 36 未收入 Markdown。

## p.037（PDF p.37 / 印刷 p.37）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 01:57:52 EDT。
- PNG：`audit/frey1986_p037.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p037_tate_case.png`、`audit/300dpi/frey1986_p037_non_tate_case.png`、`audit/300dpi/frey1986_p037_corollary_start.png`（pnggray）。
- 核对：Tate/non-Tate 两种情形的 contradiction argument、Proposition 4 remark 与 Corollary 的表示开头。
- 结果：FAIL。印刷局部域中的 `Q_l` / `l` 在 Markdown 多处写成 `Q_1` / `1`；假设 `l ≡ -1 (mod p)` 被写成 `1 ≡ -1`；Tate 情形印为 `σ(γ_2(Q)) ≠ γ_2(Q)`，Markdown 误为 `σ(Y_2(Q)) ∤ Y_2(Q)`；Corollary 表示下标印为 `ρ_E`，Markdown 写 `p_E`。按裁片修复。
- 已吻合：非 Tate 情形的 `γ_2(σQ)=-σ(γ_2(Q))=γ_2(Q)`、单位根逆像关系与 footnote 5。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 37 未收入 Markdown。

## p.038（PDF p.38 / 印刷 p.38）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 02:05:26 EDT。
- PNG：`audit/frey1986_p038.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p038_corollary.png`、`audit/300dpi/frey1986_p038_remark1.png`、`audit/300dpi/frey1986_p038_remarks2_3.png`（pnggray）。
- 核对：Corollary 的 modular representation 条件、remarks 1–3 中 level cancellation 的推广与 Weil/Mestre 度数估计引入。
- 结果：FAIL。印刷参数化映射为 `X_0(N)`，Markdown 写 `X_o(N)`；`2·l^p|Δ_E` 和 `l≠1 (mod p)` 在 Markdown 变成 `2·1^p|Δ_E` 与 `1≠1`；备注 1 的 `l=p` 被写成 `1=p`；Galois 群底域 `Q` 被写成 `G`；Remarks 2 的 `l` 与 `l^{p^k}` 条件中多处写成 `1`，且 “l can be cancelled” 写成 `I`。按 300 dpi 页图逐处恢复。
- 已吻合：`ρ_E` 的不可约性假设、S1 level N/l 结论、Weil eigenvalue 估计的叙述及其后接 Mestre result。
- 排版级差异：印刷页眉 “38, G. Frey” 与页码 38 未收入 Markdown。

## p.039（PDF p.39 / 印刷 p.39）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 02:16:52 EDT。
- PNG：`audit/frey1986_p039.png`（pngmono，150 dpi）；300 dpi 裁片：`audit/300dpi/frey1986_p039_conclusion.png`、`audit/300dpi/frey1986_p039_closing_group.png`、`audit/300dpi/frey1986_p039_references_1_8.png`、`audit/300dpi/frey1986_p039_reference1.png`（pnggray）。
- 核对：文章结语、Frobenius/Tate module 概述及印刷参考文献 [1]–[8]。
- 结果：FAIL。印刷 Galois 群是 `Gal(Q̄/Q)`，Markdown 用 `Ḡ/Q`；印刷群写作 `Gl_2(Z/p)`，Markdown 将模数下标写为 Fraktur `p`；参考文献 [1] 的印刷姓氏带 caron（`SHAFAREVIČ`），Markdown 写成无附加符号的 `SHAFAREVIC`。根据原图恢复，不按现代姓名拼写替换。
- 已吻合：degree bound 中的常数 `c` 与 [2]–[8] 的作者/题名/刊名/卷页/年份核对结果。
- 排版级差异：印刷页眉 “Elliptic Curves and Fermat's Equation” 与页码 39 未收入 Markdown。

## p.040（PDF p.40 / 印刷 p.40）

- actor=Peer-P06; model=gpt-6-luna; effort=max；签认时间：2026-10-02 02:20:56 EDT。
- PNG：`audit/frey1986_p040.png`（pngmono，150 dpi）；本页可见的 references 与 Received 日期字样足够清晰，未另作 300 dpi 裁片。
- 核对：References [9]、[10]、作者单位地址与 received date。
- 结果：FAIL（修复前）。References [9]、[10] 和作者地址与原页相符；印刷页底 `received 16.12.1985` 修复前缺失，已由后续 fix commit 补录，见修复登记。
- 排版级差异：印刷页眉 “40, G. Frey” 与页码 40 未收入 Markdown。

## 修复登记

- 修复执行者：Peer-P06；模型/effort：`gpt-6-luna/max`。
- 原始 MinerU Markdown commit：`4e5d9aabe1bc05fbb69fe4f77c0e692470fd9935`；修复前 SHA-256：`b9b5a5a56bba04f9a09f13ca90b88fab214a3c19df1ea4a82b191214ec7f74a6`。
- 独立 Markdown 修复 commit：`c21075d3909f13069859611e45a88c0a91c7f975`；修复后 SHA-256：`dfee1701475ac1593bb55affe56e397537db988b9cf2788d22971602d481835f`。
- 对照原件：`frey1986.pdf` SHA-256 `0f092a804000ad55d39506015516777fee288a4b8de65bb9e41a738cb6a87ab0`；审计证据使用仓库中的 40 张 150dpi 页图与逐页登记的 300dpi 裁片。
- 手工修订方法：所有目标 Markdown 改动均通过 `apply_patch` 按具体上下文逐处完成；没有运行脚本写入、批量替换或格式化目标文件。

| PDF 页 | 修复后的正文核对 |
|---|---|
| 1 | 补全两行题名并更正方程首字母为大写 `C`。 |
| 2 | 恢复 `F_p`、`Gl_1(C)_p` 与 `G_{Q(ζ_p)}` 记号。 |
| 3 | 恢复 `X_0(N)`、`G_Q`、`C_{F_p}`，并合并 `resulting`、`corresponds` 的跨行断词。 |
| 4 | 将有理点 `F` 更为 `P`，合并 `congruence` 断词。 |
| 5 | 恢复 `27`、`12^3` 与 `Weierstraß`；印刷圆形字形仍不确定是 `O` 还是 `0`，未推断改写。 |
| 6 | 恢复有限域/赋值中的素数 `l`；保留印刷 reduction 方程项 `βY`。 |
| 7 | 恢复 `E^{(l)}`、`v_l` 与 `Q(√δ_E)`，并合并 `singularity`、`different` 断词。 |
| 8 | 恢复 `Q_l`、素数 `l`、`K_p` 的有理域底域及 `√[p]{j_E}`。 |
| 9 | 恢复有理底域 `Q`、局部素数 `l` 和 `Weierstraß` 拼写。 |
| 10 | 恢复 `K_p`、`1/27`、`Q^{*2}` 与导体公式的素数 `l`。 |
| 11 | 恢复 `3∤ABC`、模 3 的不等式、`Q(√δ_E)` 与导体/赋值中的 `l`。 |
| 12 | 恢复 `16`、p 次 Kummer 根式及其 `Q` 底域，合并 `corresponding`。 |
| 13 | 恢复导体乘积中的 `l` 与 minimal equation 的分母 `16`。 |
| 14 | 将假设中的 `K_n` 改为 `K_p`；`p|p` 的首 glyph/Fraktur 字形保留未知。 |
| 15 | 恢复印刷大写指数 `P`，包括 `B=w^P`、`2v^P` 与定理方程中的 `Z_i^P`。 |
| 16 | 恢复大写 `Z`、`p∤`、`X_0(N)`、`Γ_0(N)`、`SL(2,Z)` 与 cusp `i·∞`。 |
| 17 | 恢复 `Γ_0(N)`、`q∈Q`、微分 `ω` 与 `J_0(N)`。 |
| 18 | 恢复 `J_0(N)` 与 `ω`；`ω|Z` 中竖线后的 `Z` 是否为下标仍未知。 |
| 19 | 恢复 `X_0(N)`、`ω`、`l∤N`、`a_l`、`T_l` 及公式中的 `with`。 |
| 20 | 恢复 `a_l` 公式、`F_l`、Galois 底域 `Q`、`F_p`、`b_l`；Markdown 保留孤立页眉 `G. Frey`，页码仍省略。 |
| 21 | 恢复 `ρ`、`Q_p(ζ_p,√[p]{a})`、kernel 归属及 `p∤M`；局部理想 glyph 的 Fraktur 字形仍未知。 |
| 22 | 恢复 `ρ_E`、`p∤` 关系，并保留原页方程显示的大写 `P`。 |
| 23 | 恢复 `N` / `N'` 的 `l` 乘积、`\not\equiv`、`F_p`、点数 `#E^{(l)}(F_l)` 与 `a_l`。 |
| 24 | 按本页印刷保留显示公式中的大写指数 `P`。 |
| 25 | 恢复 `g_2` 公式的大写 `P`、`Vol(E)` 与显示公式中的 `with`。 |
| 26 | 恢复 `X_0(N)`、印刷词 `isogenous` 与 `parametrized`；Markdown 保留孤立页眉 `G. Frey`，页码仍省略。 |
| 27 | 恢复 `Gal(Q̄/Q)`、`Z/p`、`l∤p`、`l∥M`、level cancellation 的 `l` 与 `g≠f`。 |
| 28 | 恢复参数化映射的底曲线 `X_0(N)`。 |
| 29 | 恢复 `A=ker(φ_*)`、isogeny `β(b,a)=φ^*(b)-a`、`J_0(N)` 与 `T⊗Q` 分解。 |
| 30 | 恢复 `X_0/J_0` 记号及导体乘积中的 `l`。 |
| 31 | 恢复 `Q/Q̄`、`F_l`、`J_0(N)` 与分量 `C_i^0,C_0^0`；prime-divisor 首 glyph 以 `𝔩|l` 暂作语义转写，确切字体未知。 |
| 32 | 恢复 `P mod l`、`Q`-rational 与 `l^{p^k}`。 |
| 33 | 恢复示例系数 `269` / `13`、`For l≠p`、`A(\bar Q)_{p^k}`、`Q(C^*)=Q(C)` 与条件中的 `l`；保留印刷 `isogeneous` 及脚注重复 `for for`。 |
| 34 | 恢复 `J_0(N)`、`N/l`、`X_0(N)`、`A_i^0`、`mod l` 与 `l≠1 (mod p)`。 |
| 35 | 恢复 `Q_l` / `l`、`Q` 底域、`v_l` 与分量 `0`；原印刷 `isogeneous`、`totally degenerated` 和 “There are an elliptic curve” 均保留。 |
| 36 | 恢复局部域/伽罗瓦底域 `Q_l`；保留 `Γ_1` 中代表 lattice index 1 的数字。 |
| 37 | 恢复 `Q_l`、`v_l`、`l≡-1 (mod p)` 与 `σ(γ_2(Q))≠γ_2(Q)`。 |
| 38 | 恢复 `ρ_E`、`X_0(N)`、`2·l^p`、`l≠1`、`N/l`、`S_l`、`l^{p^k}` 与 cancellation 的 `l`。 |
| 39 | 恢复 `Gal(Q̄/Q)`、`Gl_2(Z/p)` 与参考文献姓名印刷 caron `SHAFAREVIČ`。 |
| 40 | 补录印刷页底日期 `received 16.12.1985`。 |

### 最终复读与边界

- Markdown 修复后从第 1 行至第 1545 行完整复读：最终文件为 1,545 行、54,946 bytes，SHA-256 如上。逐页修复项对照对应 PDF 页图/裁片与本文件该页的审计发现核验；`git diff --check` 通过。未运行测试；这项工作验证转写忠实性，不证明论文中的数学命题。
- 40 个页级 commit 的 `FAIL` 是修复前审计等级，均保留为原始逐页审计证据；修复后的核对结果和未闭合字形列于本节，不把旧签级静默改成 PASS。
- 未修复为确定字形的项目：p.5 的 `O/0` 圆形字形；p.14 的 prime-divisor glyph；p.18 `ω|Z` 中 `Z` 的下标状态；p.21 与 p.31 prime-ideal glyph 的准确 Fraktur 字形。涉及符号的语义转写不应被当作原印刷字形的确定判读。
- print quirks 继续忠实保留：p.1 “Falting's theorem”、p.6 的 `βY`、p.15/p.22/p.24/p.25 的大写指数 `P`、p.33 脚注 “for for”、p.33/p.35 印刷拼法 “isogeneous” 及 p.35 的原印刷语法。
- 本 Peer 候选只改 `1998年 - Wiles/`；按用户边界未修改根级 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、`README.md` 或 `MEMORY.md`，未 push。候选状态仍待 Master-Luna 独立复核与集成。
