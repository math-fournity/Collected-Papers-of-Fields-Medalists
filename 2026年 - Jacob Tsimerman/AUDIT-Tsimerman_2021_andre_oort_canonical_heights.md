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
