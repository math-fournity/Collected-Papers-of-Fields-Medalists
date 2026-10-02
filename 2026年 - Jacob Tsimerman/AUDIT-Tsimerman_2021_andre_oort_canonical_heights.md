# Canonical Heights on Shimura Varieties and the André-Oort Conjecture — 逐页审计

- Peer：`Peer-P21`
- Model / reasoning effort：`gpt-6-luna / max`
- 角色：`CONTRIBUTOR`；`Master-Luna` 是唯一 `CANONICAL_INTEGRATOR`
- 任务基线：`037602429d3b009f6fc468c732073eb3ddf9875f`（detached worktree；该候选尚未集成）
- PDF：`Tsimerman_2021_andre_oort_canonical_heights.pdf`，52 页；Creator 为 LaTeX with hyperref；born-digital
- MinerU Markdown：`Tsimerman_2021_andre_oort_canonical_heights__Tsimerman_2021_andre_oort_canonical_heights.md`
- 对账方法：PDF 文本层逐页为主；150dpi pngmono 页图用于版面/字形核验，疑难字形再用 300dpi 裁片。
- 范围：判断 PDF 排印页与 MinerU Markdown 的转录忠实度，不审查论文数学证明有效性。

## p.001（PDF p.1 / 印刷 p.1）
- 时间：2026-10-01 16:12:03 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p001.png`（pngmono 150dpi）
- 核对：题名、作者、附录作者、日期、目录至 §6.4。
- 结果：PASS±。
- 差异与依据：页面左侧排有 `arXiv:2109.08788v4 [math.NT] 17 Dec 2024`，Markdown 未录入；属版本/来源元数据遗漏，不改变正文命题。印刷目录将 §6.4 写作 `Principle bundles`，Markdown 同样保留该拼法；这是印刷原文 quirk，未作校正。PDF 文本层与 150dpi 页图支持以上判断；Markdown 对应第 1–50 行。

## p.002（PDF p.2 / 印刷 p.2）
- 时间：2026-10-01 16:14:01 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p002.png`（pngmono 150dpi）
- 核对：目录 §6.5–附录 §A.3。
- 结果：PASS±。
- 差异与依据：目录附录标题的印刷排版将 `infinity by` 连作 `infinityby`（源级空格 quirk，照录）；Markdown 对应目录项也缺空格，且作者尾部被截成 `Michael C`，但附录正文标题后续列出全名。此为目录元数据的轻微转录缺损，非正文遗漏。页图与 PDF 文本层一致；Markdown 对应第 51–69 行。

## p.003（PDF p.3 / 印刷 p.3）
- 时间：2026-10-01 16:16:36 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p003.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p003_Theorem-1.2.png`
- 核对：§1.1 概述、Theorem 1.1–1.2、§1.2 开头。
- 结果：FAIL（以原图为准）。
- 差异与依据：Theorem 1.2 在印刷页写作 `Let (T,r) ⊂ (G,X)`，结论为高度 `is (M disc E_T)^{o(1)}`；Markdown 第 95 行的包含式丢失 `(G,X)` 的括号，渐近式丢失左括号并把 `E_T` 输出成 `\cal E_T`。300dpi 裁片清楚显示原式为普通斜体 `E_T`，故当前 Markdown 公式结构不完整。第 81 行还将 `different strategy` 误录为 `diferent strategy`；第 101 行本页对应的 `different` 亦少一个 `f`。印刷 PDF 文本层、150dpi 整页图及 300dpi 裁片相互支持；改动留待 52 页审计完成后逐处 Edit。

## p.004（PDF p.4 / 印刷 p.4）
- 时间：2026-10-01 16:18:10 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p004.png`（pngmono 150dpi）
- 核对：§1.2 余段、§1.3、§1.4 开头及页下注 1–3。
- 结果：PASS±。
- 差异与依据：Markdown 第 107 行把 `different ways` 录作 `diferent ways`，第 115 行把 `A difficulty` 录作 `A dificulty`；均为少一个 `f` 的拼写转录瑕疵，不改数学断言。印刷页底三条脚注在 Markdown 中均有对应文本。PDF 文本层及 150dpi 页图支持核对。

## p.005（PDF p.5 / 印刷 p.5）
- 时间：2026-10-01 16:21:43 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p005.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p005_Property-3-morphism.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p005_enow-print-check.png`
- 核对：Definition 1.4 的性质 (1)–(4)、§1.5 组织说明至 §8 起句、脚注 4。
- 结果：FAIL（以原图为准）。
- 差异与依据：Property (3) 印刷页写有态射 `f : (T_1,r_1) → (T_2,r_2)`；Markdown 第 141 行在两组 Shimura datum 之间漏掉箭头，令命题中的态射缺失。300dpi 裁片可见清楚的右箭头。PASS± 瑕疵：Markdown 第 169 行把 `sufficient` 写作 `suficient`；第 171 行另有孤立的 `ET` 脚注碎片，后面仍保留完整脚注 4。印刷页将 §4 句子排作 `enow`，Markdown 忠实保留；300dpi 裁片确认这是原文拼写 quirk，不校正。改动留待全篇审计后逐处 Edit。

## p.006（PDF p.6 / 印刷 p.6）
- 时间：2026-10-01 16:25:45 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p006.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p006_map-arrows.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p006_theta-map.png`
- 核对：§1.5 结尾、致谢与 §2.1 前半定义（至 `Fil^r`）。
- 结果：FAIL（以原图为准）。
- 差异与依据：印刷定义含 étale map `f : V[s_1,s_1^{-1},…,s_n,s_n^{-1}] → R` 及环同态 `θ : A_inf(\bar R) → \hat{\bar R}`；Markdown 第 197、203 行都丢失 `→`。两张 300dpi 裁片确认这两个箭头在印刷页清晰存在。致谢中的印刷姓名 `Fabrizo Andreatta` 按源文保留；Markdown 对应文字相符。改动留待全篇审计后逐处 Edit。

## p.007（PDF p.7 / 印刷 p.7）
- 时间：2026-10-01 16:30:09 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p007.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p007_Acris-inverse-limit.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p007_Bcris-embeddings.png`
- 核对：§2.1 中 A_cris / B_cris / B_dR 定义、自然嵌入、t 的性质，以及 §2.2 Theorem 2.1 和脚注 6。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 211 行将 `A_cris` 的逆极限对象误录成 `Ω_m^{A_cris,m}`；印刷原式是 `lim_m A_cris,m`。第 217 行把印刷中不同的 `B_cris` 与 `\mathcal B_cris`（及对应 A_cris 项）压成同一字形，失去对象区分。第 233 行两项自然嵌入均漏箭头。300dpi 裁片显示逆极限项、两种 B 符号和两个映射箭头。PASS± 瑕疵：第 241 行 `with equality` 漏录为 `wth equality`；脚注 6 的 `Q_p` 被拆成第 243 行独立碎片，而第 245 行留下 `finite extensions of .`。改动留待全篇审计后逐处 Edit。

## p.008（PDF p.8 / 印刷 p.8）
- 时间：2026-10-01 16:31:35 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p008.png`（pngmono 150dpi）
- 核对：§2.2 Theorem 2.1 的证明、§2.3 Tsuji 范畴条件 (1)–(5)、对应滤过公式、Tsuji 关联对象及 Remark 2.2(1)。
- 结果：PASS±。
- 差异与依据：检查到 Markdown 第 247 行将 `compatibility` 写作 `compatiblity`，第 263 行将 `Griffiths` 写作 `Grifiths`（少一个 `f`）；均为不改变定义内容的文本拼写瑕疵。滤过关系、加权和公式、Φ 条件 (a)–(c) 与 Tsuji 对象的同构在 PDF 文本层、页图和 Markdown 中对应。

## p.009（PDF p.9 / 印刷 p.9）
- 时间：2026-10-01 16:34:23 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p009.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p009_TAinf-mod-pi.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p009_Lemma2.3-maps.png`
- 核对：Remark 2.2(2)–(3)、§2.3.1 复原公式、Lemma 2.3 及证明至第二部分结论。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 311 行把印刷的商 `A_inf/π` 录成 `A_inf/\ddot{π}`；第 313 行将 `M ≅ (… )^G` 破坏为 `M – ´…¯^G`。Lemma 2.3 第 319 行把第二权重区间 `[0,b]` 写成 `0,b`；第 325 行把普通张量积 `⊗` 误录为 `\ddot{\otimes}`，并漏掉单射等源 `f : T_cris(M) → L_1 ⊗ L_2` 的映射箭头。两张 300dpi 裁片确认 π、同构、权重区间、普通张量积和箭头。PASS± 瑕疵：脚注 7 在 Markdown 中被拆成 `T A_inf pMq`、`cris` 等孤立片段，脚注正文也缺失所指对象名。修复留待全篇审计后逐处 Edit。

## p.010（PDF p.10 / 印刷 p.10）
- 时间：2026-10-01 16:36:14 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p010.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p010_Lemma2.4-weights.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p010_fiber-maps.png`
- 核对：Lemma 2.4、(2.3.1)–(2.3.4)、对偶定义与证明、§2.4 纤维映射及 Lemma 2.5 陈述。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 349 行将 Lemma 2.4 的权重区间 `[0,a]`、`[0,b]` 都录成无括号的 `0,a`、`0,b`；第 362 行在 (2.3.2) 末尾多出一个右括号，第 385 行在印刷的 `T_cris` 前多出点号。§2.4 第 389 行的 `i : R → V` 漏箭头；第 391 行表示 `G_V → G_R` 的第二处箭头也缺失；第 393 行把 `G_R`-stable 误并成 `G_{R^{-Stable}}`。300dpi 裁片确认区间括号、两处映射箭头及 `G_R`-stable 排版。修复留待全篇审计后逐处 Edit。

## p.011（PDF p.11 / 印刷 p.11）
- 时间：2026-10-01 16:40:02 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p011.png`（pngmono 150dpi）
- 核对：Lemma 2.5 证明、Theorem 2.6 及证明、Lemma 2.7 的权重/扭曲范围、脚注 8。
- 结果：PASS±。
- 差异与依据：Markdown 第 445 行把 `character` 拆为 `charact$e r^{8}$`，并把结果句中的 `for` 拆作 `$f o r …$`；这是局部词形/数学排版边界瑕疵。Theorem 2.6 的张量基变换同构、Lemma 2.7 的 `-a ≤ n ≤ p-2-b` 界及扭曲幂与印刷页一致；脚注 8 的 cyclotomic character 权重约定也保留。

## p.012（PDF p.12 / 印刷 p.12）
- 时间：2026-10-01 16:42:22 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p012.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p012_Theorem2.9-maps.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p012_Divided-power-formula.png`
- 核对：Theorem 2.9、证明中的映射与同构、Tsuji 展开算子 `∇_N`、(2.5.1) 及 divided-power 注释、log toric chart 与 Φ。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 467 行的 Theorem 2.9 结果两侧没有印刷的映射箭头 `→`；第 469、473、475 行分别漏掉 `A_cris → O B_dR`、`β : R → A_cris`、`R → O B_dR` 的箭头。第 479 行把算子中的 `s_i d/ds_i` 丢成 `s d/ds_i`；第 485 行将 divided power `X_i'^{N_i}/N_i!` 错成分母 `N_i`；第 487 行漏掉 toric chart `V[s_1,…,s_n] → R` 的箭头。两张 300dpi 裁片确认箭头、变量下标和阶乘。修复留待全篇审计后逐处 Edit。

## p.013（PDF p.13 / 印刷 p.13）
- 时间：2026-10-01 16:45:19 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p013.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p013_Psi-map.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p013_Lemma3.3-iff.png`
- 核对：Theorem 2.9 的 log-crystalline 证明结尾、§3 Definition 3.1、Lemma 3.2–3.3 与 Definition 3.4 前三项。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 493 行的自然映射 `Ψ : M ⊗_β A_cris,log → L ⊗ A_cris,log` 漏掉 `→`；第 517 行将 Lemma 3.3 印刷的双向条件 `acceptable iff acceptable on a finite affinoid cover` 缩成单向 `if`，丢失必要方向。两张 300dpi 裁片确认原页有该箭头和 `iff`。另有 `affinoid` 写作 `afinoid` 的拼写瑕疵，不影响以上分级。

## p.014（PDF p.14 / 印刷 p.14）
- 时间：2026-10-01 16:50:08 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p014.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p014_admissible-restrictions.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p014_Height-domain.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p014_Corollary-domain.png`
- 核对：Definition 3.4 条目 (4)–(5)、Lemma 3.5–3.6、§3.1 高度定义与 Corollary 3.7。
- 结果：FAIL（以原图为准）。
- 差异与依据：Definition 3.4 第 (5) 项 Markdown 第 535 行把限制域 `\mathcal Y_v^{rig}` 错录为 `\mathcal V_v^{rig}`。§3.1 第 553、559、563 行把高度定义及 Corollary 3.7 的点集从印刷的 `\mathcal Y(\mathcal O_F[N^{-1}])`（及其代数闭包版本）写成 `\mathcal V`/`\dot{\mathcal V}`，并在第 553 行另加入 `\bar{\mathcal O}_F`；这把定义域从基空间换成了向量丛的总空间。300dpi 裁片确认限制域和高度点集均为 `\mathcal Y`。PASS± 瑕疵：`differ`、`sufficient`、`affinoid` 等拼写有少字母伪影，不改变本页分级。

## p.015（PDF p.15 / 印刷 p.15）
- 时间：2026-10-01 16:53:51 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p015.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p015_Definition4.1-GK.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p015_Gr-map.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p015_lattice-powers.png`
- 核对：Definition 4.1 的 Galois 群与分级空间、Gr map、Lemma 4.2 两种 lattice 及比较证明。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 582 行把定义中的 `G_K`-representation 写成 `G`-representation，且在 `V_n^\circ` 不变量处用小写 `G_k`。第 589 行的 `Gr S_cris(V) → Gr D_dR(V)` 漏掉箭头。第 595 行把系数域写为 `W(\bar{\mathbb F}_p)[1/\bar p]`，源文是 `[1/p]`；第 597 行又将 `t^n` 录为 `t^{\bar n}`。300dpi 裁片确认群标记、映射箭头和指数/分母。PASS± 拼写瑕疵未改变以上分级。

## p.016（PDF p.16 / 印刷 p.16）
- 时间：2026-10-01 16:58:34 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p016.png`（pngmono 150dpi）
- 核对：Definition 4.3–4.4、Theorem 4.5 与完整证明、§4.2 开头。
- 结果：PASS±。
- 差异与依据：Definition 4.4 第 605 行把 `S-b_1\dim V` 的 TeX 数学式边界拆成 `$S-b_1$dim$V$`，但乘积因子仍可读。脚注 9 的 `V(-b_1)` 被单独抽成前一段孤立 span，第 629 行脚注正文则留下 “weights of …” 空缺；页图原文为 “weights of V(-b_1)”。Theorem 4.5 的规范化权重和界、lattice 夹逼与行列式估计在 PDF 与 Markdown 中对应。

## p.017（PDF p.17 / 印刷 p.17）
- 时间：2026-10-01 17:02:57 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p017.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p017_Theorem4.6-range.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p017_Theorem4.6-part2.png`
- 核对：§4.2 的结构层、(4.2.1)–(4.2.2)、Theorem 4.6 两条、证明起始部分及 α 展开式。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 651 行把权重假设 `[0,m]` 写成 `0,m`，丢失区间括号。第 657 行 Theorem 4.6(2) 的范围 `0 ≤ s < r` 被损坏成带多余 `i`、`p` 的 `r_i p`，并在后文加入残留 `p the identification`；这破坏了结论对指标 s 的范围。300dpi 裁片确认印刷式为 `[0,m]` 与 `0 ≤ s < r`。修复留待全篇审计后逐处 Edit。

## p.018（PDF p.18 / 印刷 p.18）
- 时间：2026-10-01 17:07:31 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p018.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p018_L-less-r.png`
- 核对：Theorem 4.6(2) 证明余段、定义 \bar L_{<r}、(4.2.3)、Proposition 4.7 与 Definition 4.8。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 691 行定义 `\bar L_{<r}` 时将范围 `for s < r` 录成 `for s r`，漏掉 `<`，使过滤项集合条件不完整；300dpi 裁片可见 `s < r`，并由 (4.2.3) 的 `\bigoplus_{s<r}` 复核。第 687 行在 `0 ≤ s < r-1` 后还残留数字 `2`。Definition 4.8 处的独立 `p` 是局部 OCR 碎片，列为 PASS±。

## p.019（PDF p.19 / 印刷 p.19）
- 时间：2026-10-01 17:16:02 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p019.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p019_Lemma4.9-domains.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p019_phi-map.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p019_Theorem4.11-map.png`
- 核对：Lemma 4.9、Proposition 4.10、§4.3 主映射与 Lemma 4.11 开头。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 731 行把 Lemma 4.9 的第一个对象写成 `ν_*(L̂⊗OC)(n)`，将 `n` 移出系数层；第二个 `ν_{ket,*}` 又被破坏成含 `Ω_*` 的字串。第 741 行的 `φ : Y → X` 和第 759 行的 `S_cris(L) → D^0_dR(L)` 都漏掉映射箭头。三张 300dpi 裁片核实印刷对象次序及两个箭头；本页所列差异均为数学对象/映射的转录问题。

## p.020（PDF p.20 / 印刷 p.20）
- 时间：2026-10-01 17:19:28 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p020.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p020_Theorem4.14-bound.png`
- 核对：Lemma 4.11 余段、Lemma 4.12、Definition 4.13、Theorem 4.14 陈述及证明开头。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 789 行 Theorem 4.14 的比较因子 `p^{b(dim L-1)/(p-1)}` 被破坏成 `b…` 后接 `p^{\longrightarrow\not\longrightarrow}`；该界是本定理的核心定量结论。300dpi 裁片清楚显示指数 `b(dim L-1)/(p-1)`。第 791 行的证明标签还把 `Theorem 4.5` 录成 `Theorem 4.1%`，作为交叉引用瑕疵另记。

## p.021（PDF p.21 / 印刷 p.21）
- 时间：2026-10-01 18:27:04 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p021.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p021_Theorem4.14-scaling.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p021_quadratic-field-print.png`
- 核对：Theorem 4.14 证明收尾与 §5.1 题材、平方关系、二次域定义、CM 模与 A/B 元素。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 807 行把缩放因子 `1/π^i` 写成 `1/π^2`，改变了按权重 i 缩放的公式；300dpi 裁片确认上标为 i。印刷页还保留一个源级数学排印冲突：同页先称 `\mathfrak p^2=-p`，随后定义 `M=\mathbb Q[x]/(x^2-p)`；Markdown 忠实保留两处原文，未按预期更正。相邻的 A、B 公式与来源字形一致。

## p.022（PDF p.22 / 印刷 p.22）
- 时间：2026-10-01 20:27:23 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p022.png`（pngmono 150dpi）
- 核对：§5.1.1 intrinsic valuation 余段、§5.1.2 crystalline valuations、§5.2 开头至 intrinsic norm 与 crystalline norm 分节。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 853 行在正文把 degree-p isogeny 写成 `E E'`，漏掉映射箭头；第 863 行同一 isogeny 再次出现时则有 `E → E'`。150dpi 页图与 PDF 文本层均显示第一处印刷原文为 `E → E'`，故这是单处转录漏符号。其余本页 valuation 公式与印刷排版相符。

## p.023（PDF p.23 / 印刷 p.23）
- 时间：2026-10-01 23:14:46 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p023.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p023_Faltings-height.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p023_Shimura-map.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p023_Res-field.png`
- 核对：§5.2 crystalline norm 的 Faltings-height 算式及 §6.1 Basic definitions。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 867 行把 Faltings 高度增量分母 `2p` 写成 `2\upsilon`。第 881 行 Shimura datum 的 homomorphism `f : S → G_R` 漏掉箭头。第 893 行把 `Res_{F/\mathbb Q}` 误录为 `Res_{F/\mathbb 0}`，并省略 `G_R` 与 Hermitian domain 两个乘积的下标范围（源文分别为 `σ:F→R` 与 `σ∈I_nc`）。300dpi 裁片逐项确认分母、箭头、基域和索引集合。

## p.024（PDF p.24 / 印刷 p.24）
- 时间：2026-10-02 00:14:07 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p024.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p024_Special-maps.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p024_Prop6.2-maps.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p024_Prop6.3-maps.png`
- 核对：§6.2 special points、Lemma 6.1、Proposition 6.2 的映射与群覆盖构造、Proposition 6.3 开头。
- 结果：FAIL（以原图为准）。
- 差异与依据：多处数学映射在 Markdown 中丢失箭头：第 897 行 `h : S → G`；第 911 行 `f : (G',X') → (G,X)`；第 913 行 `G' → G`；第 919 行 `G^s → G^{der}` 与 `μ : S → G`；第 923 行 `((G_2,X_2) → (G_0,X_0))`。300dpi 裁片显示这些箭头在印刷页均清楚存在，关系语义因此无法由 Markdown 原文完整恢复。

## p.025（PDF p.25 / 印刷 p.25）
- 时间：2026-10-02 00:22:11 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p025.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p025_principal-bundle-maps.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p025_Rational-representation-maps.png`
- 核对：§6.4 principal bundle 的商类映射与作用、§6.5 automorphic vector bundles、§6.6 Betti/étale local systems 及 Proposition 6.4。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 949 行把 étale local system 的标签写成 `\Pi_{et}`，随后又把同一标签写成 `\Omega_{et}`；第 953 行把 Betti local system `{}_B V_{\mathbb Q}`误录成 `\Sigma_B V_{\mathbb Q}`。300dpi 文本裁片确认来源仅为下标 `et` 与 `B`，无 Π、Ω、Σ 这些额外符号。PASS± 瑕疵：principal-bundle 第二个 quotient representative 在 Markdown 用 ceiling brackets `\lceil\rceil`，印刷为 square brackets `[ ]`；其两个映射箭头和对象相符。

## p.026（PDF p.26 / 印刷 p.26）
- 时间：2026-10-02 00:26:29 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p026.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p026_CM-character-lattice.png`
- 核对：§6.7 canonical metrics、§6.8 torus representation lemma、§6.9 torus lattices/partial CM type 与 `r_Φ`、`χ_Φ` 定义。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 977 行 character lattice 生成元写作 `e_σ^* - e_σ^*`，丢失第二个基向量的复共轭横线；印刷为 `e_σ^* - e_{\bar σ}^*`，缺横线会把所列生成元退化为零。该行的 embedding `σ : K → C` 也漏掉箭头。300dpi 裁片确认横线与 `K → C` 映射。

## p.027（PDF p.27 / 印刷 p.27）
- 时间：2026-10-02 00:47:38 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p027.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p027_Theorem6.6-products.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p027_character-beta-map.png`
- 核对：Theorem 6.6 陈述、Step 1 product splitting/character maps、Step 2 partial CM type construction 与 identity 起始式。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 1003 行定理中的 `a_i : (T_x,h_x) → (R_K,r_{Φ_i})` 漏箭头。第 1015 行将 `G_R ≅ \prod_{j∈J}G_j` 写成索引 `i∈J` 却仍用 `G_j`。第 1021 行的 character-lattice map `X^*(R_{K_x}) → X^*(T_x)` 漏箭头，且生成元 `e^*_{τ_0}-e^*_{\bar τ_0}` 丢失复共轭横线；同一行又把 `f_β:T_x→R_{K_x}` 写成无箭头且目标 `R_{K_β}`。两张 300dpi 裁片确认原文的箭头、指标与目标域。

## p.028（PDF p.28 / 印刷 p.28）
- 时间：2026-10-02 00:56:09 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p028.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p028_Tannakian-maps.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p028_Motives-definitions.png`
- 核对：Theorem 6.6 identity 收尾、Definition 6.7、Theorem 6.8、Proposition 6.9 及其 Tannakian reduction。
- 结果：FAIL（以原图为准）。
- 差异与依据：Markdown 第 1073 行把 Proposition 6.9 上下文中的 rational representation `V` 属于 `T` 误录成 `T_i`，并把 lattice `\mathbb V ⊂ V` 写成 `\mathbb V ⊂ V'`。第 1085 行把 source 中的 `A` 写成含 `\mathscr A` 的异形记号。第 1087 行的 projection `W → V` 和 quotient/surjection `T' → T` 均漏箭头。300dpi 裁片核实变量与箭头。

## p.029（PDF p.29 / 印刷 p.29）
- 时间：2026-10-02 01:06:03 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p029.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p029_Theorem7.1-fields.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p029_Corollary7.2-labels.png`
- 核对：§7 开头、Theorem 7.1 与 Corollary 7.2 陈述，以及证明中导出的有限 étale 映射。
- 结果：FAIL（以原图为准）。
- 差异与依据：§7 首段将 rigid flat vector bundles 的 rank 条件 `≤ m` 录为 `m`。Theorem 7.1 将 `G^c` 污染为含 `;` 的下标，将整数 `N'` 的第一次出现录为 HTML 上标 `1`，并把结论中的 `et V_p` 写成 `\Pi_{et}V_p`、底域下标 `E_v` 写成 `E_\tau`；300dpi 裁片确认印刷分别为 `G^c`、`N'`、`et V_p` 和 `E_v`。Corollary 7.2 的 `et V_{p^f}^{\oplus n}` 在 Markdown 中丢失 `t`；对应裁片确认印刷有完整的 `et` 标签。证明中有限 étale 映射 `S_{K'}(G',X') → S(G,X)` 在 Markdown 漏掉箭头。上述差异会改变量词范围、局部系统标签或映射关系。

## p.030（PDF p.30 / 印刷 p.30）
- 时间：2026-10-02 01:10:01 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p030.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p030-product-formulas.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p030-Hodge-and-local-systems.png`
- 核对：Corollary 7.2 证明余段（乘积 Shimura 数据与局部系统）、Theorem 7.1 证明，以及 §8 开头。
- 结果：FAIL（以原图为准）。
- 差异与依据：Corollary 7.2 证明将诱导有限 étale 映射 `S_K(G,X) → ∏_i S_{K_i}(G^{(i)},X_i)` 的箭头漏录；张量表示中给 `V_2` 多加点号，并把 isotypic component 中的 `V_1` 多加复共轭横线。Hodge-weight 对象的 `d_R(V_1 ⊠ … ⊠ V_k)` 被录成 `\bigcap(V_1 ⊠ … ⊠ V_k)`；其后 `⊠_{i,et}V_{i,p^f}` 被误录为带黑体 `S` 的 `\mathbb S_{i,et}\mathbb V_{i,p^f}`，另一个局部系统项又多出 `\breve{}` 标记。两张 300dpi 裁片核实原文的 `d_R`、`⊠`、局部系统标签和普通表示因子。PASS± 拼写伪影：`diference`、`sufices`；§8 标题与问题陈述和印刷相符。

## p.031（PDF p.31 / 印刷 p.31）
- 时间：2026-10-02 01:12:51 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p031.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p031-Theorem8.1-Lemma8.2.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p031-Lemma8.2-proof.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p031-setup-Lemma8.3.png`
- 核对：Theorem 8.1；Lemma 8.2 陈述及证明；§8.2 模型与 CM 点设定、Lemma 8.3 陈述和式 (8.2.1) 之前的基本群分解。
- 结果：FAIL（以原图为准）。
- 差异与依据：Lemma 8.2 证明中印刷变量为 `η_j`，Markdown 将 localization 的素理想写成 `\mathfrak h_{\mathcal j}`，随后又将其上方的素理想写成 `\mathfrak p_j`；印刷两处均为 `η_j`。同一证明把 `R[[x_1,…,x_n,…]]` 的首变量写成 `x_i`，并将 localization 下标误留为 HTML `<sub>j</sub>`。§8.2 的 `G_\mathbb Q`-representation 漏了 `\mathbb Q`，integral point 的 `\mathcal S` 误成小写 `s`，Lemma 8.3 的 `et V_2` 局部系统标记被破坏成空下标形式。300dpi 裁片核实了这些对象和下标；Theorem 8.1 中 `S(\overline{\mathbb Q})` 和 `S(\overline{\mathbb Z}[N^{-1}])` 则与印刷相符。

## p.032（PDF p.32 / 印刷 p.32）
- 时间：2026-10-02 01:16:24 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p032.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p032-Lemma8.4-parameters.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p032-Lemma8.4-monodromy.png`
- 核对：Lemma 8.3 证明余段、Lemma 8.4 及其反证构造、§9 开头。
- 结果：FAIL（以原图为准）。
- 差异与依据：Lemma 8.3 证明把延拓至积分模型的点 `\mathcal S` 录成小写 `s`，局部系统 `et V_2` 又误录为 `\Pi_{et}\mathbb V_2`。Lemma 8.4 反证假设和完成局部环中，印刷的 residue field `\overline{\mathbb F}_p` 被写成 `\overline{\mathbb F}_n`，且 `\widehat{\mathcal O}_{\overline S, y_{0,\overline{\mathbb F}_p}}` 漏掉紧化符号 `\overline S`。300dpi 裁片确认 residue-field 下标和环所在的紧化空间；构造中的 `t_i` 分母、`M=E_w'^{\mathrm{ur}}` 与后续映射指数则与印刷相符。PASS± 拼写伪影：页首 `in actually exact` 对应印刷 `in fact exact`，并有 `ppull` 重复字母。

## p.033（PDF p.33 / 印刷 p.33）
- 时间：2026-10-02 01:19:22 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p033.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p033-norm-bound-Prop9.2.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p033-Shimura-product-reductions.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p033-dR-model-identification.png`
- 核对：§9 两个有限处范数约定、Theorem 9.1、Proposition 9.2 陈述及其关于 Shimura 数据乘积与 de Rham 模型的归约。
- 结果：FAIL（以原图为准）。
- 差异与依据：第一条非 Archimedean 范数条件中的界 `p > rng_V · dim V + 2` 漏掉乘号。Proposition 9.2 把 `d_R V_{E_v}` 误作 `d_R V_{E_i}`，其证明的覆盖 `f:(G',X') → (G,X)` 漏掉箭头；末段的 `\mathcal V_v` 误作希腊字母 `\nu_v`，并把 `d_R V` 写成 `\operatorname{der}V`。300dpi 裁片逐项确认乘号、映射、`\mathcal V_v` 与 `d_R`。另有 `Q.`-simple 的多余句点属于内容级符号噪声，列入本页 FAIL。PASS± 拼写/措辞伪影：`is is`、`comes form`、`suficiently` 与 `based change base`；其余本页已核公式和命题结构按印刷为准。

## p.034（PDF p.34 / 印刷 p.34）
- 时间：2026-10-02 01:26:26 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p034.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p034-comparison-and-height.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p034-Definitions9.4-10.2.png`
- 核对：§9 p-adic comparison isomorphism、Corollary 9.3、Definition 9.4；§10.1 notation 与 Definition 10.1–10.2。
- 结果：FAIL（以原图为准）。
- 差异与依据：p-adic comparison isomorphism 两端 `p-d_R V_0` 与 `d_R V_0` 在 Markdown 被破坏为含 `\nabla_0`、`\mathbf\Omega` 的不同对象，且括号内的 `D_{dR}(et V_{0,p}[1/p])` 也出现额外上下标。Corollary 9.3 的 `L = det(Gr^a_{F^\cdot} d_R V)` 漏掉等号，首个 Schmid 引用的 `Thm 6.6'` 被录为 `Thm 6.67`。§10.1 用于参数依赖的向量 `\vec{x}` 被录为 `\~x`；Definition 10.2 将 filtration 对象 `V_{\chi,\mathbb C}` 写成 `V_{x,\mathbb C}`，并漏掉 `Fil^\cdot` 的点。300dpi 裁片确认这些字形与上下标。PASS±：正文拼写 `Rieman Hilbert` 是印刷原文，Markdown 忠实保留；另有 `diference` 拼写伪影。

## p.035（PDF p.35 / 印刷 p.35）
- 时间：2026-10-02 01:30:56 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p035.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p035-Lemmas10.3-10.5.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p035-Definition10.6-properties.png`
- 核对：Lemma 10.3；Definitions 10.4、10.6；Lemma 10.5 的 cocharacter、homomorphism 与权空间；Definition 10.6 的性质 (1)–(4) 和 Theorem 10.7。
- 结果：FAIL（以原图为准）。
- 差异与依据：Lemma 10.3 的 Shimura-data map `f:(T_1,r_1) → (T_2,r_2)` 在 Markdown 漏箭头；Lemma 10.5 的 `h:Res_{E/\mathbb Q}\mathbb G_m → Res_{E/\mathbb Q}\mathbb G_m` 同样漏箭头；Definition 10.6 性质 (3) 再次将 `f:(T_1,r_1) → (T_2,r_2)` 写成相邻对象而无箭头。300dpi 裁片确认三处箭头。印刷在 `V'_{-1}=\bigoplus_{\sigma\in\bar\Phi}` 后未印出 summand `\mathbb C_\sigma`，Markdown 忠实保留该源级公式缺项；Lemma 10.3 的印刷拼写 `vaieties` 也保留。PASS±：`heighest` 拼写伪影及 Definition 10.6 性质 (2) 中被拆开的 `Given` 与脚注 13 标记。

## p.036（PDF p.36 / 印刷 p.36）
- 时间：2026-10-02 01:34:53 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p036.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p036-Proposition10.8-norm-map.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p036-Zarhin-height-formulas.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p036-Theorem10.9.png`
- 核对：Proposition 10.8 陈述和范数映射归约、Zarhin trick/height 估计，以及 Theorem 10.9 陈述。
- 结果：FAIL（以原图为准）。
- 差异与依据：Proposition 10.8 证明的 quotient map `i:(S_E,s_\Phi) → (R_E,r_\Phi)` 漏箭头，所得 height bound 的 `O_g` 被录为 `O_q`；实点分解中 `Res_{E/\mathbb Q}\mathbb G_m(\mathbb R)` 的域/群记号遭 HTML 与字体噪声破坏。Character identity `\chi_{Std}^2=i^*\chi_\Phi\cdot Nm` 的 `Nm` 被写成含下标 `l` 的 `N_lm`；后续 Shimura morphism `Nm_{E/\mathbb Q}:(S_E,s_\Phi) → (\mathbb G_m,Nm_{E/\mathbb Q})` 既多出 `\Sigma` 又漏箭头。Zarhin 表示 `Std^{\oplus 8}` 被转录成注册商标样式 `Std^{\textregistered 8}`，高度界 `h_A(x)=O_g((\operatorname{Disc}E)^{o_g(1)})` 也被破坏。Theorem 10.9 的量词点条件 `x\in S_K(G,X)(\mathbb Q)` 则变成 `x\equiv S_K(G,X)(\overline{\mathbb Q})`。300dpi 裁片确认这些映射、符号、底域和指数。PASS±：印刷中的 `its a rational character` 与 `The completes the proof` 原样保留，属源级语法瑕疵。

## p.037（PDF p.37 / 印刷 p.37）
- 时间：2026-10-02 01:40:08 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p037.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p037-Theorem10.9proof-maps.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p037-Theorem10.10-reduction.png`
- 核对：Theorem 10.9 证明的 adjoint filtration、Theorem 6.6 的 partial-CM-type maps 与 height sum；Theorem 10.10 Step 1–3 及 Galois-closure reduction。
- 结果：FAIL（以原图为准）。
- 差异与依据：Theorem 10.9 证明中的 `L := det Fil^1_{dR}V` 被录成含波浪号的 `Fil^{\tilde 1}`。由 Theorem 6.6 给出的 map `a_i:(T_x,h_x) → (R_{E_T},r_{\Phi_i})` 漏箭头；Step 2 的 norm map `Nm_{E'/E}:R_{E'} → R_E` 和诱导 Shimura-data map 两处也漏箭头。Step 3 标题 `|\Phi|=1` 的编号 `3` 被录成 `\mathcal B`。300dpi 裁片确认其上标、映射与步骤编号。PASS± 源级印刷瑕疵：`By Theorem 6.6 there there are` 的重复 `there` 被忠实保留；另有 `suficient` 拼写伪影。

## p.038（PDF p.38 / 印刷 p.38）
- 时间：2026-10-02 01:44:54 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p038.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p038-Step3-combination.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p038-Step4-Theorem10.11.png`
- 核对：Theorem 10.10 Step 3 的复合域/partial CM type 公式与高度组合；Step 4 的全 CM type 归约和式 (10.4.1)；Theorem 10.11 与式 (10.5.1)。
- 结果：FAIL（以原图为准）。
- 差异与依据：Step 3 的 Shimura-data map 应由范数 `Nm_{E^{(j)}/E_i}` 诱导，Markdown 写成了 `Nm_{E'/E_i}`，并漏掉 map `(R_{E^{(j)}},\rho_{\Phi^{(j)}}) → (R_{E_i},\rho_{\Phi_i}^{2^{d-1}})` 的箭头。300dpi 裁片确认复合域上标及箭头。式 (10.4.1)、式 (10.5.1) 的表达式与编号均相符。PASS± 源级排印：Theorem 10.11 印作 `S_K(G,x)`（末字母为小写 `x`），MinerU 忠实保留。

## p.039（PDF p.39 / 印刷 p.39）
- 时间：2026-10-02 01:50:12 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p039.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p039-Definition11.1-norms.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p039-Lemma11.2-footnotes.png`
- 核对：Definition 11.1 的 norm-label、Fontaine–Laffaille range 条件及局部比较对象；Lemma 11.2 的 constancy domain、twisted-lattice identity 和脚注 14–15。
- 结果：FAIL（以原图为准）。
- 差异与依据：Definition 11.1 的 norm-label `\mathcal K_{K,\mathbb V,q}|\cdot|` 被破坏为近似 `|K,\mathbb V,q|\cdot|` 的字串；界 `p ≥ rng_V · dim V + 2` 漏乘号。crystalline 条件下的比较对象把 `E_v` 误录成 `E_{\imath}`，另一分支的 `p-d_RV_{E_v}` 也出现额外粗体/上标噪声。Lemma 11.2 的 constancy domain 应为 `S_K(T,X)(\mathbb Q)`，Markdown 写成 `S_K(T,X)(\overline{\mathbb Q})`；证明末行的 `t^{-1}\mathbb V` 又将 `\mathbb V` 错并入指数。300dpi 裁片核实 norm-label、域下标、局部系统对象和结尾变量。脚注 15 的 `\mathbb Z_p` 从句中脱落成独立 footnote 碎片；其尾部 `GSp_{2g}` 又在 Markdown 重复一次。

## p.040（PDF p.40 / 印刷 p.40）
- 时间：2026-10-02 01:54:59 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p040.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p040-Definition11.2-polarization.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p040-Property1-3.png`
- 核对：Definition 11.2 的 endomorphism algebra、trace polarization 与 discriminant；Lemma 11.3；§11.3 Property (1) 的 projection/index/polarization 比较及 Property (3) 开头。
- 结果：FAIL（以原图为准）。
- 差异与依据：Definition 11.2 应定义 `\mathbb Q_\chi=\operatorname{End}_T(V_\chi)`，Markdown 的 End 对象丢了下标 `\chi`；同段 trace 与 norm 域 `\mathbb Q_\chi` 多次误成 `\mathbb Q_x`。Property (1) 中系数环映射 `R_{\chi_1}\otimes R_{\chi_2} → R_{\chi_3}` 漏箭头，`\mathbb V_{\chi_i}, i=1,2,3` 的定义行也把枚举变量混入下标。Property (3) 的 Shimura-data map `f:(T_1,r_1) → (T_2,r_2)` 漏箭头，其 Archimedean error bound 的维数/range 下标被拆坏。300dpi 裁片核实 endomorphism 对象、`\mathbb Q_\chi`、映射及误差下标。PASS± 源级瑕疵：印刷原文的 `odd of even` 被保留；`fix a sign` 在 Markdown 中有字母拆裂。

## p.041（PDF p.41 / 印刷 p.41）
- 时间：2026-10-02 02:00:00 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p041.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p041-property4-characters.png`
- 核对：Property (3) 的高度与范数界余段；§11.4 Property (4) 的 character、restriction level、pullback norm collection 与格子分解。
- 结果：FAIL（以原图为准）。
- 差异与依据：Property (4) 中取点范围应为 `x ∈ S_{K'}(T,r)(\mathbb Q)`，Markdown 改成 `x ∈ S_K(T,r)(\overline{\mathbb Q})`，同时丢失 `K'=i^*K` 的 level。紧接着的 norm collection `\mathcal N_0|\cdot|` 被写成无名称的 `_0|\cdot|`。同页后半将 direct-summand 表示/lattice `\mathbb V_\chi` 多次误录为 `\mathbb V_x` 或 `\mathbb V_{\mathcal X}`，改变了 subscript 中的 character 身份。300dpi 裁片确认点集的 level/base field、collection 名称和 `\chi` 字形。PASS±：`morphisms`、`diferent` 与 `suficient` 拼写/词形伪影。

## p.042（PDF p.42 / 印刷 p.42）
- 时间：2026-10-02 02:05:15 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p042.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p042-references1-18.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p042-references19-30.png`
- 核对：§11.4 证明收尾；参考文献 [1]–[30] 的作者、题名、刊物/出版信息、页码与 URL。
- 结果：FAIL（以原图为准）。
- 差异与依据：参考文献 [13] 的印刷 URL 含 `~conrad`，Markdown 将波浪号转为 `„`，破坏链接。参考文献 [9] 的印刷 URL 本身未印出 `~`，MinerU 忠实沿用该源级缺字，故不计作转录差异。Markdown 将 [30] 的 arXiv URL 末尾 `v3` 与下一条 `[31]` 连成同一行，失去条目分隔。两张 300dpi 裁片确认 [13] URL 字符和页面末尾 [30] 的边界。PASS± 源级印刷瑕疵忠实保留：[9] URL 中缺少 `~`；[16] 的 `info Sémin. Bourbaki`、[19] 的作者标点 `A, Yafaev`、[23] 的 `Andrè-Oort` 重音、[29] 的 `Japac Acad.`；其余已对照的题录和页码相符。

## p.043（PDF p.43 / 印刷 p.43）
- 时间：2026-10-02 02:14:06 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p043.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p043-references31-40.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p043-references47-62.png`
- 核对：参考文献 [31]–[62] 的作者、题名、刊物/出版信息、卷页年及 URL。
- 结果：FAIL（以原图为准）。
- 差异与依据：参考文献 [34] 的印刷 URL 在行末为 `intro-`、下一行续 `sh-ex.pdf`，构成 `intro-sh-ex.pdf`；Markdown 将连接号变成空格 (`intro sh-ex.pdf`)，改变链接路径。300dpi 裁片核实该连接号。PASS±：Refs [47]、[58] 的 `A_g` 与 [49] 的 `C^n` 上下标被拍平为 `Ag`、`Cn`；[59] 的 `\mathbb Z_p`、`A_{\inf}` 亦拍平。源级印刷 URL [34] 在主机目录分隔符后没有可见 `~`，MinerU 忠实保留；其余本页核过的参考文献条目与印刷相符。

## p.044（PDF p.44 / 印刷 p.44）
- 时间：2026-10-02 02:19:09 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p044.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p044-base-divisor-residue.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p044-DefinitionsA1-A2.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p044-DefinitionA3.png`
- 核对：Appendix A 开头；定义边界 divisor 与 residue map；Definitions A.1(a)–(d)、Remark A.2(a)–(b) 和 Definition A.3 arithmetic-model data。
- 结果：FAIL（以原图为准）。
- 差异与依据：边界 divisor `D_S=\bigcup_{\mu=1}^{c}D_S^\mu` 多出 brevé；residue map `res_\mu:\Omega^1_{\bar X_S/S}\langle D\rangle → \mathcal O_{D_S^\mu/S}` 在 Markdown 丢失映射箭头。Remark A.2(a) 的 `End(E_{C,an})^{End(\nabla_C)}` 被拆成 HTML sub/sup 标签及乱码 `Endp∇Cq`。Definition A.3 首个 triple 中 `\mathcal O_{\bar X_C}(1)` 漏掉基底下标 `C`；(b) 的相应 tuple 又将 `C` 误成 `r`。三张 300dpi 裁片确认 union、箭头、cohomology invariant 与 scheme 下标。PASS± 拼写伪影：`affine` 被录成 `afine`，`differentials` 也有漏字母。

## p.045（PDF p.45 / 印刷 p.45）
- 时间：2026-10-02 02:22:44 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p045.png`（pngmono 150dpi）
- 核对：Theorem A.4；Remark A.5；§A.1 的 Theorem A.6、Corollary A.7、Theorem A.8 及 associated-graded 与 Kodaira–Spencer maps。
- 结果：PASS±。
- 差异与依据：数学陈述、Hilbert polynomial `P_0(n)`、étale gluing、torsionfree Fontaine–Laffaille conclusion 和 maps 均与印刷相符。PASS± 字面噪声：`Griffiths` 转成 `Grifiths`；Corollary A.7 中 `U_i`-family 被插入额外的数学点号。

## p.046（PDF p.46 / 印刷 p.46）
- 时间：2026-10-02 02:26:59 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p046.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p046-PropositionA10-contract.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p046-arithmetic-model-proof.png`
- 核对：Remark A.9、Proposition A.10 (a)–(g)、证明中选取 arithmetic model 与 moduli-space base change。
- 结果：FAIL（以原图为准）。
- 差异与依据：Proposition A.10 所述 model 应以 `(S,\bar X_S,D_S,\mathcal O_{\bar X_S}(1))` 为源、以 `(\bar X_C,D_C,\mathcal O_{\bar X_C}(1))` 为目标；Markdown 两个 tuple 都丢失了紧化横线。性质 (e) 的 geometric-point map `s:\operatorname{Spec}\bar k → S` 漏箭头，性质 (g) 的 `S → \operatorname{Spec}\mathbb Z` 也漏箭头。证明中 `\mathbb P^N_{\tilde S}` 后多出 `r`，并在 `\bar X_{\tilde S}` 的 smooth 断言前多出 `r`。300dpi 裁片确认 scheme、bar、箭头及多余字符。

## p.047（PDF p.47 / 印刷 p.47）
- 时间：2026-10-02 02:32:27 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p047.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p047-sections-A1.1-A2.1.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p047-Higgs-de-Rham-maps.png`
- 核对：Proposition A.10 证明中的 sections 与有限平坦 structural morphism；§A.2 Definition A.11、periodicity definition、restricted Higgs-de Rham correspondence (A.2.1)。
- 结果：FAIL（以原图为准）。
- 差异与依据：式 (A.1.1) 的 sections `[(E_S^i,\nabla_S^i)]_{i\in I}` 从 `S` 到模空间的箭头在 Markdown 写成冒号；随后的 structural morphism `\mathcal M_{log-dR}(\bar X_{\tilde S}/\tilde S) → S` 也漏箭头。§A.2 中 geometric-point map `s:\operatorname{Spec}\bar k → S` 再次漏箭头；定义 `R_{dR}(s)` 时印刷为 nilpotent residues **of** level `≤p-1`，Markdown 写成 **or**。式 (A.2.1) 印刷有两条相反方向的 correspondence（上方 `C^{-1}` 向右、下方 `gr` 向左），Markdown 只保留单一向右箭头，并把 `gr` 挂在它下面。300dpi 裁片核实 sections、morphism 和两条流向。PASS± 拼写伪影：`Griffiths` 变成 `Grifiths`；“are jointly surjective” 另有 `r rare` 噪声。

## p.048（PDF p.48 / 印刷 p.48）
- 时间：2026-10-02 02:37:32 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p048.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p048-LemmasA12-A14.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p048-LemmaA15-injectivity.png`
- 核对：Lemmas A.12–A.15 的 category equivalence、Ext/rigidity 及 injectivity arguments。
- 结果：FAIL（以原图为准）。
- 差异与依据：Lemma A.12 的 `gr:R_{dR}(s) → R_{Dol}(s)` 漏箭头；Definition A.15 Artin–Rees family 中 `t:\mathbb A_s^1 → \mathbb A_s^1` 也漏箭头。Grothendieck-existence conclusion 的 `\operatorname{Spec}\bar k[[t]]` 被缩成 `\operatorname{Spec}\bar k t`，丢失 formal power series ring；Lemma A.13 的 target category `\mathsf{MIC}_{p-1}` 被录成 `\mathsf{MlC}_{p-1}`。两张 300dpi 裁片核实箭头、环和 category 字形。

## p.049（PDF p.49 / 印刷 p.49）
- 时间：2026-10-02 02:43:53 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p049.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p049-LemmasA15-A17.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p049-DefinitionA18-TheoremA19.png`
- 核对：Lemma A.15 injectivity continuation、Propositions A.16–A.17；§A.3 geometric-point setup、Definition A.18 的 periodic tuple 与 φ-map；Theorem A.19。
- 结果：FAIL（以原图为准）。
- 差异与依据：Proposition A.17 的 printed formula 是 `\sigma^{f'}([(E,\nabla)])=[(E,\nabla)]`，Markdown 在 `\sigma` 上多出圆圈。§A.3 geometric-point map `s:\operatorname{Spec}\bar k → S` 漏箭头；Definition A.18 的 `\phi_i` 对象 `C_1^{-1}(\operatorname{gr}_F E_{W_n}^i,\mathrm{KS}_i)` 被加上额外 `\cdot` 上标，且 prose 中 `\mathsf{MIC}_{p-1}` 被录成 `\mathsf{MlC}_{p-1}`。300dpi 裁片核实 `\sigma`、`\mathrm{KS}_i`、point map 与 MIC identifier。PASS± 拼写伪影：`Grifithstransverse` 与 reference/citation spacing noise。

## p.050（PDF p.50 / 印刷 p.50）
- 时间：2026-10-02 02:53:30 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p050.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p050-TheoremA20-periodic-identity.png`、`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p050-Betti-TheoremA22.png`
- 核对：Theorem A.20 periodic lift identity; Remark A.21; Betti representations, their extension to the étale fundamental group, and Theorem A.22.
- 结果：FAIL（以原图为准）。
- 差异与依据：Theorem A.20 的 periodic identity 应将 `C_n^{-1}\circ\overline{gr}` 作用后的 connection 指标写为 `\nabla_{W_n}^{\sigma(i)}`；Markdown 保留了 `\nabla_{W_n}^{i}`。Betti moduli passage 两处把表示数上界 `n_r` 错作 `n`、`n_i`；embedding `\mathcal O_F → W(\overline{\mathbb F}_p)` 漏箭头。Remark A.21 的 `End(E_{\mathbb C,an})^{End(\nabla_{\mathbb C})}` invariant group 又被拆成 HTML sub/sup 标签与乱码。两张 300dpi 裁片核实 connection index、rank-count indices、embedding arrow 与 cohomology invariant。

## p.051（PDF p.51 / 印刷 p.51）
- 时间：2026-10-02 02:58:29 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p051.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p051-residual-representations.png`
- 核对：Theorem A.22 proof 的 residual irreducibility、pairwise non-isomorphism 与 pigeonhole descent；附录参考文献 [Del70]–[EV86]。
- 结果：FAIL（以原图为准）。
- 差异与依据：pairwise-isomorphism contradiction 中右侧 residual coefficient field 应为 `\overline{\mathbb F}_p`，Markdown 将 p 错录成粗体 `\boldsymbol\pi`；结尾 pigeonhole argument 的 local-system coefficient ring 应为 `W(\overline{\mathbb F}_p)`，Markdown 将下标 p 移到 (W(\overline{\mathbb F})_p) 之后。300dpi 裁片确认这两处的 p 都属于有限域下标。
