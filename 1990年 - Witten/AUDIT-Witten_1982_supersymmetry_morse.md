# W. Witten, “Supersymmetry and Morse Theory” — 逐页视觉审计

- 源 PDF：`Witten_1982_supersymmetry_morse.pdf`（32 个 PDF 页面；印刷页码 661–692）。
- MinerU Markdown：`Witten_1982_supersymmetry_morse_mineru/Witten_1982_supersymmetry_morse__Witten_1982_supersymmetry_morse.md`。
- 模式：Creator 为 ABBYY FineReader，PDF 含 OCR 文本层（`pdftotext` 77,986 bytes）；按扫描/OCR 件处理。OCR 文本仅用于定位，逐页 150dpi 图像中的印刷页面为裁决依据。
- 本轮范围：仅此 Witten 论文目录；不重跑 MinerU，不改 PDF，不更新共享索引/进度文件。
- 最终状态：32/32 个 PDF 页面已逐页审阅；每页都有 150dpi 全页 PNG 和对应记录。修复后的 MinerU Markdown（761 行、15,004 词、91,153 bytes）已在最终修订后从头到尾复读，并与全页记录核对；未发现尚未处置的差异。
- 证据量：32 张 `pngmono` 150dpi 全页图；24 张用于裁决/补充的 300dpi 局部图。所有引用图均在本目录 `audit/` 下。
- 输入快照：本次使用分支基线 `1d124155593a6f61fa92650a7fd930275a29762e` 中已有的 MinerU Markdown；该 Markdown 源文件最后一次既有提交为 `0b0f3dd2`。未重跑 MinerU。

## p.001（PDF p.1 / 印刷 p.661）
- PNG：`audit/Witten_1982_p001.png`（pngmono，150dpi）；Hilbert 空间记号终裁：`audit/300dpi/Witten_1982_p001_Hilbert_space.png`（300dpi 裁片）。
- 核对：期刊页眉与卷页信息；标题、作者、摘要；引言至公式 (1)；收到日期及致谢脚注。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS±。print 使用 script `\mathscr{H}` 表示 Hilbert 空间及其奇偶子空间；原始 Markdown 将其 11 处识别为普通 `K`，已逐项修为 `\mathscr{H}`。题录、公式 (1) 与脚注内容相符。Markdown 未保留印刷页眉“J. DIFFERENTIAL GEOMETRY 17 (1982) 661–692”。

## p.002（PDF p.2 / 印刷 p.662）
- PNG：`audit/Witten_1982_p002.png`（pngmono，150dpi）；脚注终裁：`audit/300dpi/Witten_1982_p002_footnote.png`（300dpi 裁片）。
- 核对：公式 (2)–(7)、相对论代数段、脚注 1。
- 结果：PASS±。公式、正文及脚注与印刷页相符；Markdown 未保留页眉“662 EDWARD WITTEN”。完整脚注与印刷页一致；另有 4 个 DocVortex 残留片段重复脚注中的局部公式/短语，已逐项移除，未删改完整脚注。

## p.003（PDF p.3 / 印刷 p.663）
- PNG：`audit/Witten_1982_p003.png`（pngmono，150dpi）。
- 核对：引言中真空态讨论、公式 (8)、自发破缺段至末句跨页处。
- 结果：PASS±。正文与公式 (8) 相符；末行在印刷页与 Markdown 中均跨页续接。Markdown 未保留运行页眉及页码。

## p.004（PDF p.4 / 印刷 p.664）
- PNG：`audit/Witten_1982_p004.png`（pngmono，150dpi）；子空间记号终裁：`audit/300dpi/Witten_1982_p004_H0_subspace.png`（300dpi 裁片）。
- 核对：真空态指标讨论、Hilbert 空间奇偶分解、supersymmetry index 解释及引言末段章节路线。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS±。print 使用 `\mathscr{H}_0` 及 `\mathscr{H}_0^{\pm}` 表示零动量子空间及其奇偶部分；原始 Markdown 在该段将相关符号拍平为 `H_0`/`K_0`，13 处已逐项修复。其余正文与印刷页相符；Markdown 未保留页眉“664 EDWARD WITTEN”。

## p.005（PDF p.5 / 印刷 p.665）
- PNG：`audit/Witten_1982_p005.png`（pngmono，150dpi）。
- 核对：§2 开始；公式 (9)–(12)；Betti 数随 t 不变的解释，末段跨页续接。
- 结果：PASS±。公式 (9)–(12) 及正文与印刷页相符；末段在 “We will be” 后跨页续接。Markdown 未保留运行页眉及页码。

## p.006（PDF p.6 / 印刷 p.666）
- PNG：`audit/Witten_1982_p006.png`（pngmono，150dpi）；局部 Morse 模型与 Hessian 算子裁片：`audit/300dpi/Witten_1982_p006_Morse_setup.png`、`audit/300dpi/Witten_1982_p006_hessian_expansion.png`。
- 核对：式 (13) 中 Hessian/creation-annihilation 项；弱 Morse 不等式论证；渐近展开 (14)。
- 结果：PASS±。式 (13)、(14) 的项、指标与正文相符；“This shows” 后的论证在 Markdown 中跨页续接。Markdown 未保留页眉“666 EDWARD WITTEN”。

## p.007（PDF p.7 / 印刷 p.667）
- PNG：`audit/Witten_1982_p007.png`（pngmono，150dpi）；Taylor 展开余项终裁：`audit/300dpi/Witten_1982_p007_Taylor_expansion.png`（300dpi 裁片）。
- 核对：Taylor 展开余项、局部谐振子近似式 (15)–(18)，谱与 p-形式的条件，Morse 指数对应零模的结论。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。原始 Markdown 将 Taylor 余项的 `O(φ^3)` 识别为数字 `0(φ^3)`，现已更正。式 (15)–(18) 的算符项、符号与指标及其解释均与印刷页相符。Markdown 未保留运行页眉及页码。

## p.008（PDF p.8 / 印刷 p.668）
- PNG：`audit/Witten_1982_p008.png`（pngmono，150dpi）。
- 核对：零能态计数、强 Morse 不等式公式 (19)、余边界算子解释、脚注 2。
- 结果：PASS±。式 (19)、正文与脚注 2 均与印刷页相符；段末 “we can go” 后跨页续接。Markdown 未保留页眉“668 EDWARD WITTEN”。

## p.009（PDF p.9 / 印刷 p.669）
- PNG：`audit/Witten_1982_p009.png`（pngmono，150dpi）。
- 核对：微扰论与 tunneling 讨论、instantons 路径方程 (20)、Morse 指数相差 1 的条件。
- 结果：PASS±。公式 (20) 与印刷页相符；ABBYY 的提取文本漏出该显示公式，但 MinerU Markdown 有公式且由页面图核实。页末取向解释续至负特征向量段。

## p.010（PDF p.10 / 印刷 p.670）
- PNG：`audit/Witten_1982_p010.png`（pngmono，150dpi）；脚注终裁：`audit/300dpi/Witten_1982_p010_footnote3.png`（300dpi 裁片）。
- 核对：路径取向定义、公式 (21)–(22)、instantons 对 Morse 复形的说明、脚注 3。
- 结果：PASS±。公式 (21)–(22)、正文与完整脚注 3 均与印刷页相符；Markdown 原有 11 个 DocVortex 残留片段重复脚注局部符号，已逐项移除，完整脚注保留。Markdown 未保留页眉“670 EDWARD WITTEN”。

## p.011（PDF p.11 / 印刷 p.671）
- PNG：`audit/Witten_1982_p011.png`（pngmono，150dpi）；脚注终裁：`audit/300dpi/Witten_1982_p011_footnotes4_5.png`（300dpi 裁片）。
- 核对：拉格朗日量 (23)、欧几里得作用量 (24)–(25)、脚注 4–5。
- 结果：PASS±。公式 (23)–(25)、正文及脚注 4–5 与印刷页相符；完整脚注 5 保留，另一个重复的孤立 `ψ^i` 片段已移除。Markdown 未保留页眉及页码。

## p.012（PDF p.12 / 印刷 p.672）
- PNG：`audit/Witten_1982_p012.png`（pngmono，150dpi）。
- 核对：作用量下界与等号条件 (26)–(27)、瞬子作用量 (28)、费米子零模说明。
- 结果：PASS±。公式 (26)–(28) 的不等号、绝对值、符号与正文均与印刷页相符；末句在 “determine the sign from the” 后跨页续接。Markdown 未保留页眉“672 EDWARD WITTEN”。

## p.013（PDF p.13 / 印刷 p.673）
- PNG：`audit/Witten_1982_p013.png`（pngmono，150dpi）；300dpi 终裁：`audit/300dpi/Witten_1982_p013_footnotes6_7.png`（脚注）、`audit/300dpi/Witten_1982_p013_redefinition.png`（状态重定义行）。
- 核对：WKB 符号讨论、边界算子公式 (29)、脚注 6–7。
- 结果：PASS±。公式 (29)、正文及完整脚注 6–7 与印刷页相符；4 个 DocVortex 片段重复脚注 7 的末尾内容，已逐项移除，完整脚注保留。状态重定义行的印刷本在 `|a⟩` 与箭头间另有一个形似大写 `Z` 的字符；MinerU 的 `Z\to` 忠实保留，无法仅据该印刷判断其意图，不予改写。Markdown 未保留运行页眉及页码。

## p.014（PDF p.14 / 印刷 p.674）
- PNG：`audit/Witten_1982_p014.png`（pngmono，150dpi）。
- 核对：退化 Morse 情形、负特征向量丛、临界子流形邻域上的算符分解公式 (30)。
- 结果：PASS±。公式 (30) 的 Laplacian 分解及关联文字与印刷页相符；末段在“large energy associated”后跨页续接。Markdown 未保留页眉“674 EDWARD WITTEN”。

## p.015（PDF p.15 / 印刷 p.675）
- PNG：`audit/Witten_1982_p015.png`（pngmono，150dpi）；多项式指数终裁：`audit/300dpi/Witten_1982_p015_morse_exponent.png`、`audit/300dpi/Witten_1982_p015_morse_polynomial.png`（300dpi 裁片）。
- 核对：低能态张量分解 (31)、横向 Laplacian (32)、twisted cohomology 与退化 Morse 不等式。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。Morse 多项式项的上标印刷为小写 `p`，原始 Markdown 作大写 `P`；300dpi 裁片确认后已更正。公式 (31)–(32) 与取向丛条件相符。Markdown 未保留运行页眉及页码。

## p.016（PDF p.16 / 印刷 p.676）
- PNG：`audit/Witten_1982_p016.png`（pngmono，150dpi）。
- 核对：§3 标题；Killing 向量场变形微分 (33)–(34)、Hamiltonian (35)、Betti 数界。
- 结果：PASS±。公式 (33)–(35)、Lie 导数记号与零特征值结论和印刷页相符；末段在 “each connected” 后跨页续接。Markdown 未保留页眉“676 EDWARD WITTEN”。

## p.017（PDF p.17 / 印刷 p.677）
- PNG：`audit/Witten_1982_p017.png`（pngmono，150dpi）；记号终裁：`audit/300dpi/Witten_1982_p017_conjugation.png`（300dpi，度数算子）、`audit/300dpi/Witten_1982_p017_Lie_derivative.png`（300dpi，Lie 导数记号）。
- 核对：零态与 de Rham 商空间的关系、度数算子共轭、偶/奇零态及 Euler 特征数关系。
- 结果：PASS±。正文与 Markdown 相符；共轭算子上标印刷为大写 `P`，紧接文字定义其在 p-形式上的作用，Markdown 保留 `P` 符合页面证据。两处原本被压平为普通 `L_K` 的 Lie 导数记号按 300dpi 裁片改为 `\mathscr{L}_K`。末句在 “large s behavior of” 后跨页续接；Markdown 未保留运行页眉及页码。

## p.018（PDF p.18 / 印刷 p.678）
- PNG：`audit/Witten_1982_p018.png`（pngmono，150dpi）。
- 核对：固定点集邻域构造、截断函数、1-形式 `\tilde K`、级数形式 (36) 与闭形式 (37)。
- 结果：PASS±。式 (36) 的导数阶、系数、楔积次数及式 (37) 均与印刷页相符；正文无需修复。Markdown 未保留页眉“678 EDWARD WITTEN”。

## p.019（PDF p.19 / 印刷 p.679）
- PNG：`audit/Witten_1982_p019.png`（pngmono，150dpi）；公式终裁：`audit/300dpi/Witten_1982_p019_equations39_40.png`（300dpi 裁片）。
- 核对：H_s 的展开式 (38)、孤立零点附近 Killing 场模型 (39)、近似 Hamiltonian (40)。
- 结果：PASS±。公式 (38)–(40) 与 MinerU Markdown 忠实一致。式 (40) 的印刷文本在势能项排作 `((x_{2r-1})^2 + x_{2r})^2`，且末项的求和上限排作 `n`（而 (39) 的 λ_i 范围至 `n/2`）；这些可见排式原貌予以保留，不推断或改正。Markdown 未保留页眉“679 EDWARD WITTEN”。

## p.020（PDF p.20 / 印刷 p.680）
- PNG：`audit/Witten_1982_p020.png`（pngmono，150dpi）；Hamiltonian 终裁：`audit/300dpi/Witten_1982_p020_hamiltonian.png`（300dpi 裁片）。
- 核对：一般固定点集谱界、Euler 特征数论证与公式 (41)、任意向量场推广段开头。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。原始 Markdown 将 `H_s` 写成 `d_s d_s^* + d_s d_s^*`，重复第一项；印刷式为 `d_s d_s^* + d_s^* d_s`，已更正第二项。公式 (41) 与其余段落相符。Markdown 未保留页眉“680 EDWARD WITTEN”。

## p.021（PDF p.21 / 印刷 p.681）
- PNG：`audit/Witten_1982_p021.png`（pngmono，150dpi）；共轭恒等式终裁：`audit/300dpi/Witten_1982_p021_Qs_squared.png`（300dpi 裁片）。
- 核对：任意向量场的 Euler 特征数表达、signature 算子及其平方与 Lie 导数的关系。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。原始 Markdown 在 (Q_s^2) 公式中丢失 `2is\mathscr{L}_K`，并把 Lie 导数记号识别残缺；现已按印刷页补回。其余偶/奇分解与 signature 计数文字相符。Markdown 未保留运行页眉及页码。

## p.022（PDF p.22 / 印刷 p.682）
- PNG：`audit/Witten_1982_p022.png`（pngmono，150dpi）；Lie 导数记号终裁：`audit/300dpi/Witten_1982_p022_lie_character.png`、`audit/300dpi/Witten_1982_p022_Fourier_component.png`（300dpi 裁片）。
- 核对：孤立零点 signature 公式 (42)、固定集 signature (43)、character 值 (44)–(45)。
- 结果：PASS±。公式 (42)–(45) 与正文相符；300dpi 裁片确认 print 在 Lie 导数和其 Fourier 特征值处使用 script `\mathscr{L}_K` 记号，Markdown 中两处纯 `L_K` 已按印刷记号修订。页眉“682 EDWARD WITTEN”未收入 Markdown。

## p.023（PDF p.23 / 印刷 p.683）
- PNG：`audit/Witten_1982_p023.png`（pngmono，150dpi）。
- 核对：量子力学超对称代数 (46)–(48)，非紧情形谱条件与共轭不变性说明。
- 结果：PASS±。公式 (46)–(48) 的下标、算子组合及正文相符；Markdown 未保留运行页眉及页码。

## p.024（PDF p.24 / 印刷 p.684）
- PNG：`audit/Witten_1982_p024.png`（pngmono，150dpi）。
- 核对：非紧固定点集情形的离散谱条件与低能谱约化；§4 开始至 loop-space de Rham 算子局限。
- 结果：PASS±。文字、记号和小节标题顺序与印刷页相符。Markdown 未保留页眉“684 EDWARD WITTEN”。

## p.025（PDF p.25 / 印刷 p.685）
- PNG：`audit/Witten_1982_p025.png`（pngmono，150dpi）；作用定义终裁：`audit/300dpi/Witten_1982_p025_U1_action.png`（300dpi 裁片）。
- 核对：U(1) circle action 文字、超对称非线性 sigma 模型公式 (49)、大 s/N 谱讨论与普通量子力学比较。
- 结果：PASS±。公式 (49) 和其余正文与印刷页相符。源级 quirk：印刷的 circle-action 说明原样写作 “σ(x) + σ(x + a)”；300dpi 证实为加号，Markdown 忠实保留。其数学意图未知，不予改写。Markdown 未保留页眉及页码。

## p.026（PDF p.26 / 印刷 p.686）
- PNG：`audit/Witten_1982_p026.png`（pngmono，150dpi）。
- 核对：loop-space 与有限维固定点集的关系、超对称真空态计数、量子场论论述至正则化适用边界。
- 结果：PASS±。正文与 MinerU Markdown 对应内容相符；末段在“which can be drawn on the”后跨页续接。Markdown 未保留页眉“686 EDWARD WITTEN”。

## p.027（PDF p.27 / 印刷 p.687）
- PNG：`audit/Witten_1982_p027.png`（pngmono，150dpi）；记号终裁：`audit/300dpi/Witten_1982_p027_Q5_decomposition.png`（300dpi 裁片）。
- 核对：Hilbert 空间的 `Q_5` 偶/奇分解、与 `Q_5` 的反对易关系、Euler/signature 指标公式 (50)。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。MinerU 将 Hilbert 空间 `\mathcal{H}` 及其 `\tilde{\mathcal{H}}_{\pm}` 子空间误识为 `K`，并把反对易关系中的 `Q_5` 误识为 `Q_s`；9 处逐项修复。公式 (50) 与印刷页相符。Markdown 未保留运行页眉及页码。

## p.028（PDF p.28 / 印刷 p.688）
- PNG：`audit/Witten_1982_p028.png`（pngmono，150dpi）；公式终裁：`audit/300dpi/Witten_1982_p028_formula51.png`（300dpi 裁片）。
- 核对：迹不变量的渐近论证、任意等距变换及公式 (51)。
- 结果：PASS±。公式 (51) 与印刷页相同。源级 quirk：前句写 `t:B→B`，但公式 (51) 印刷为 `Lef(f)`；300dpi 确认此字形为 `f`，MinerU 忠实保留，原刊意图未知，未改写。Markdown 未保留页眉“688 EDWARD WITTEN”。

## p.029（PDF p.29 / 印刷 p.689）
- PNG：`audit/Witten_1982_p029.png`（pngmono，150dpi）；Hamiltonian 终裁：`audit/300dpi/Witten_1982_p029_Hst_definition.png`（300dpi 裁片）。
- 核对：标量场泛函 (52)、约化一维算子 (53)、`H_{s,t}` 的定义段与非紧指标讨论。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。原始 Markdown 在 prose 的 `H_{s,t}` 公式中把第二个乘积 `d_{s,t}^{*}d_{s,t}` 误成逗号分隔；300dpi 确认印刷为乘积，已修正。公式 (52)、(53) 与余文相符。Markdown 未保留运行页眉及页码。

## p.030（PDF p.30 / 印刷 p.690）
- PNG：`audit/Witten_1982_p030.png`（pngmono，150dpi）。
- 核对：超对称破缺的有限/无限体积极限说明、结论 §5。
- 结果：PASS±。论证、例子 `W=φ^3+bφ`、有限 `L` 与 `L→∞` 的区分及结论段均与印刷页相符。Markdown 未保留页眉“690 EDWARD WITTEN”。

## p.031（PDF p.31 / 印刷 p.691）
- PNG：`audit/Witten_1982_p031.png`（pngmono，150dpi）；参考文献终裁：`audit/300dpi/Witten_1982_p031_references_1_17.png`（300dpi 裁片）。
- 核对：结论段末尾与参考文献 [1]–[17] 的作者、标题、刊名、卷页、年份。
- 结果：PASS±。参考文献逐条与印刷页相符；[2] 标题印刷为 “elliptic complexes. I”，Markdown 原作冒号，已据 300dpi 图改为句点。其他本页书目条目未发现差异。Markdown 未保留运行页眉及页码。

## p.032（PDF p.32 / 印刷 p.692）
- PNG：`audit/Witten_1982_p032.png`（pngmono，150dpi）。
- 核对：参考文献 [18]–[22]、文末单位署名。
- 结果：PASS±。作者占位线、书目信息与文末 “PRINCETON UNIVERSITY” 均与印刷页相符；Markdown 未保留页眉“692 EDWARD WITTEN”。

## 总评、打印原貌与修复登记

- 32/32 页均已核对。最终结果为 PASS 或 PASS±；8 页的初始内容级 FAIL（p.1、p.4、p.7、p.15、p.20、p.21、p.27、p.29）均已按印刷页修复并复核。页眉/页码未收入 MinerU Markdown 属版面信息省略，已在逐页记录中说明。
- 保留的印刷原貌/未决解释：p.13 状态重定义中的 `Z→`；p.19 式 (40) 的势能项和末项求和上限；p.25 circle-action 行的 `σ(x) + σ(x+a)`；p.28 式 (51) 的 `Lef(f)`（前句映射记作 `t:B→B`）。各项均已由页面图核验并忠实保留；其作者意图未知。

### 修复登记

修复前 Markdown 快照为上述基线 `1d124155`（源文件既有提交 `0b0f3dd2`）。每项均有独立 `fix(md):` 提交；页面图和审计记录另行提交。

| PDF 页 | 修复 | `fix(md):` 提交 |
|---|---|---|
| 2 | 移除 4 个重复的 DocVortex 脚注碎片，保留完整脚注 | `395e4971` |
| 10 | 移除 11 个重复的 DocVortex 脚注碎片，保留完整脚注 3 | `77667553` |
| 11 | 移除重复的孤立 `ψ^i` 脚注碎片 | `7b4bd27c` |
| 13 | 移除 4 个重复的 DocVortex 脚注碎片，保留完整脚注 7 | `dc5abaa5` |
| 1、4 | 将被 OCR 误识的 Hilbert 空间 `\mathscr{H}` / `\mathscr{H}_0^{\pm}` 符号逐项恢复 | `8219e7a9` |
| 7、15 | 恢复 Taylor 余项 `O(φ^3)` 与 Morse 多项式指数 `t^p` | `fb35a3ec` |
| 17、21、22 | 恢复 6 处被拍平的 Lie 导数 script `\mathscr{L}_K` 记号 | `bf47a65d` |
| 20 | 将 `H_s` 的第二项从重复的 `d_s d_s^*` 修为 `d_s^* d_s` | `a13340fc` |
| 21 | 恢复 `Q_s^2 = H_s + 2is\mathscr{L}_K` | `f12a22d5` |
| 27 | 将 8 处 Hilbert 空间 `\mathcal{H}` 符号及 1 处 `Q_5` 逐项从 `K`/`Q_s` OCR 误识中恢复 | `2fbf673c` |
| 29 | 将 `H_{s,t}` 定义中的逗号误识修为乘积 `d_{s,t}^*d_{s,t}` | `7931f092` |
| 31 | 将参考文献 [2] 标题中的冒号修为印刷句点 | `57aa3d00` |
