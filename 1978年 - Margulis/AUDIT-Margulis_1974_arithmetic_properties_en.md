# AUDIT — Margulis_1974_arithmetic_properties_en

- actor: Peer-P19
- model: gpt-6-luna
- effort: max
- base: 037602429d3b009f6fc468c732073eb3ddf9875f
- PDF: `Margulis_1974_arithmetic_properties_en.pdf` (50 pages; print pages 107–156)
- source type: scanned pages with an ABBYY FineReader OCR text layer; `pdfimages -list` reports one full-page 300dpi 1-bit CCITT image on each of 50 pages. The OCR layer is secondary to the printed page.
- initial MinerU Markdown SHA-256: `3821f1d007dd02ad1a4f3894c081d7120bddb675681770a8deb7ea61cc4537f3`
- audit status: in progress; content repairs are deferred until all 50 pages have been audited.

## p.001（PDF p.1 / 印刷 p.107）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:09 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p001.png` (Ghostscript, pngmono, 150dpi)
- 核对：刊物/译本题录、献辞、标题、作者、摘要、目录和题录页脚注；对照 PDF p.1 图像与 OCR 文本层，Markdown L1–L34。
- 结果：FAIL。
- 差异：印刷页顶端两行题录 “Russian Math. Surveys 29:1 (1974), 107–156” 和 “From Uspekhi Mat. Nauk 29:1 (1974), 49–98” 在 MinerU Markdown L1 前缺失。标题、作者、摘要、目录条目和扩展讲稿脚注与印刷页相符。
- 处理：保留本页失败证据；待 50 页初审完成后用 Edit 将缺失题录逐处补入，并记录修复后复核。

## p.002（PDF p.2 / 印刷 p.108）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:11 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p002.png` (Ghostscript, pngmono, 150dpi)
- 核对：Introduction §1 开头至 “simplest”；SL₂(R) 对上半平面的作用公式、紧/非紧有限体积论述、引文 [43]/[41]/[7]/[21] 及页脚注；对照印刷页与 MinerU Markdown L38–L48。
- 结果：PASS。
- 证据说明：印刷页中的 Möbius 作用分式和 2×2 矩阵在 MinerU Markdown 中均保留。PDF 的 ABBYY 文本层漏抽该显示公式的分子和矩阵；150dpi 原页图确认原式，故不将文本层缺失误判为 Markdown 差异。

## p.003（PDF p.3 / 印刷 p.109）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:12 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p003.png` (Ghostscript, pngmono, 150dpi)
- 核对：算术子群定义、格与不可约格定义、Selberg 猜想背景、Weak Rigidity Theorem 起句及本页两条脚注；对照印刷页与 MinerU Markdown L50–L60。
- 结果：PASS。
- 备注：本页正文、公式记号、引文 [7]/[42]/[39]/[40] 与两条脚注在 Markdown 中对应完整；ABBYY 文本层对多个希腊/花体符号识别不稳，判读以 150dpi 印刷页为准。

## p.004（PDF p.4 / 印刷 p.110）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:14 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p004.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p004_footnotes.png`
- 核对：Weak/Strong Rigidity Theorem、非一致格背景、main theorem、对称空间重述开头及本页脚注；对照印刷页与 MinerU Markdown L62–L84。
- 结果：FAIL。
- 差异：印刷脚注 1 为 “... using the ideas of Mostow’s paper [45]”，Markdown L80 误作 “Moscow’s”；L82 又多出不在印刷页的重复碎片 “2. obtained ... Mostow’s paper [45]”。Markdown L78 的独立 “n≥3” 也没有对应印刷脚注，印刷脚注 1 已在其完整句内写作 “n > 3”。300dpi 裁片显示原页仅有脚注 1、2 两条。
- 处理：待全篇 50 页初审完成后，用 Edit 将脚注 1 的姓名改正并移除两个多余片段；修复后回核本页。

## p.005（PDF p.5 / 印刷 p.111）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:15 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p005.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p005_added_in_proof.png`
- 核对：对称空间定理续句、NOTE、Introduction 第 2–3 点、致谢及两条脚注；对照印刷页与 MinerU Markdown L86–L102。
- 结果：FAIL。
- 差异：Markdown L100 将 “rank_Q G > 2” 错排为 “rank Q^G > 2”（Q 上标 G）；300dpi 原页裁片证实印刷为 Q-rank，即 Q 是 rank 的下标、G 为群的主体。
- 处理：待全篇 50 页初审完成后用 Edit 修正该记号，并回核 ADDED IN PROOF 脚注。

## p.006（PDF p.6 / 印刷 p.112）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:16 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p006.png` (Ghostscript, pngmono, 150dpi)
- 核对：§0.1–§0.5 的域/代数群记号、Galois 群、p-adic 符号、unipotent/nilpotent radical 定义、基本群投影、正规化子/中心化子与交换子公式；对照印刷页与 MinerU Markdown L104–L124。
- 结果：PASS。
- 备注：页末集合交换子显示式从 L122 开始并跨页；本页可见内容与 Markdown 相符。PDF OCR 文本层将若干公式字形识别成乱码，未据此判错。

## p.007（PDF p.7 / 印刷 p.113）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:17 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p007.png` (Ghostscript, pngmono, 150dpi)
- 核对：§0.5 交换子定义续式、§0.6–§0.12 记号、§1 引言及 Lemma 1.1 陈述/证明开头；对照印刷页与 MinerU Markdown L128–L158。
- 结果：PASS。
- 备注：本页涉及的子群运算、K-structure、无穷远趋向定义、指数和 Lie 代数记号均与印刷页相符；OCR 文本层的符号误识未出现在对应 Markdown 内容中。

## p.008（PDF p.8 / 印刷 p.114）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:18 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p008.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p008_lemma_1_5.png`
- 核对：Lemma 1.1 证明续段、§1.2–§1.5 的引理/Remark/证明；对照印刷页与 MinerU Markdown L158–L186。
- 结果：PASS。
- 备注：本页脚注、引文 [1]–[3]、集合交/正规子群记号及 Lemma 1.5 页末句均与印刷相符；300dpi 裁片核对了 Lemma 1.5 的页末原文。

## p.009（PDF p.9 / 印刷 p.115）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:21 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p009.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p009_hat_H_prime.png`
- 核对：Lemma 1.5 证明续段与 §2.1 的 F-proper/F-compact 定义和引理 2.1.1–2.1.5；对照印刷页与 MinerU Markdown L188–L214。
- 结果：PASS±。
- 印刷原貌：Lemma 1.5 证明的闭包集合中，印刷字形在 H′ 上方可见帽号；Markdown L188 保留该帽号。300dpi 裁片确认后按 print 原貌保留，不作归一化。

## p.010（PDF p.10 / 印刷 p.116）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:22 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p010.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p010_lemma_2_1_5.png`
- 核对：Lemma 2.1.5 证明续式、§2.2–§2.4、Zassenhaus 引理、§3 与 Lemma 3.1 开头；对照印刷页与 MinerU Markdown L216–L246。
- 结果：PASS±。
- 印刷原貌：Lemma 2.1.5 的显示式在 “(N∩F)·((K·D∩F) =” 处印有未配对左括号；Markdown 保留该排印。300dpi 裁片确认括号不配对，按原文记录，不擅自补括号。

## p.011（PDF p.11 / 印刷 p.117）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:24 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p011.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p011_3_1_continuation.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p011_3_4_1.png`
- 核对：§3.1 跨页续段、Lemma 3.2.1、§3.3.1–§3.4.3；对照印刷页与 MinerU Markdown L246–L267、L296。
- 结果：FAIL。
- 差异：印刷 p.117 在 §3.1 的 “and” 后有完整续段：ΔΛ 由 Λ 唯一确定；exp: 𝔚→V 与 ln: V→𝔚 是 regular rational maps；Λ 在 V 中 Zariski-dense 蕴含其在 𝔚 中 Zariski-dense；并得出 ΔΛ⊃b(n)lnΛ 是 𝔚_R 中的满维格。Markdown L246 停在 “and”，L248–L267 以多个破碎显示块替代该段，缺少连接文字及完整表达。另，印刷 p.117 的 3.4.1 证明为 “But Λ ⊂ V_Q”，MinerU Markdown L296 误录为 “But A ⊂ V_Q”；300dpi 裁片确认印字为希腊大写 Λ。
- 处理：待全篇初审完成后用 Edit 按 p.117 原文重建 §3.1 跨页段、将 L296 的 A 改为 Λ，并分别回核。

## p.012（PDF p.12 / 印刷 p.118）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:26 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p012.png` (Ghostscript, pngmono, 150dpi)
- 核对：Lemma 3.4.3 证明、§4.1–§4.4 定义/引理/证明及 §4.5 起句；对照印刷页与 MinerU Markdown L302–L330。
- 结果：PASS。
- 备注：Q-rational character、H⁰、unipotent subgroup/horospherical notation、exp-log 公式和引用 [7]/[8]/[9]/[12] 均与印刷页相符；本页 §4.5 语句续至下一页。

## p.013（PDF p.13 / 印刷 p.119）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:28 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p013.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p013_formula_1.png`
- 核对：§4.5 根空间、标准 parabolic 子群定义，显示式 (1)–(4) 与 horospherical 结论；对照印刷页与 MinerU Markdown L332–L362。
- 结果：PASS±。
- 印刷原貌：显示式 (1) 的第二个左端印为 B₀⁻；Markdown 也记录为 B₀⁻。300dpi 裁片确认印字为下标 0，按 print 原貌保留。

## p.014（PDF p.14 / 印刷 p.120）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:31 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p014.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p014_lemmas_451_452.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p014_lemma_4_5_4.png`
- 核对：Lemma 4.5.1–4.5.5 陈述与证明开头；对照印刷页与 MinerU Markdown L364–L392。
- 结果：FAIL。
- 差异：印刷 Lemma 4.5.1(2) 为 `[𝔖,x]=𝔊_α`，Markdown L367 写 `[𝔠,x]`；同项印刷根空间点集下标为 `k`，Markdown L371 写成 `h`。Lemma 4.5.2(1) 印刷第二个群记号为 `B_θ⁻`，Markdown L378 写成 `B_θ′`。Lemma 4.5.4(2) 印刷结论 `V′=V_∅⁻`，Markdown L386 和 L388 两处均写成 `V_∅′`。
- 处理：待全篇初审完成后用 Edit 分别按印刷记号修正；完成后复核三处 300dpi 原文证据与相关陈述/证明。

## p.015（PDF p.15 / 印刷 p.121）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:32 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p015.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p015_lemmas_458_461.png`
- 核对：§4.5.5 证明续段、Lemmas 4.5.6–4.5.8、§4.6.1–§4.7.2；对照印刷页与 MinerU Markdown L394–L422。
- 结果：FAIL。
- 差异：印刷 Lemma 4.6.1 证明写单一 Lie-algebra 参数 “exp ξ, where ξ is an arbitrary element of the open Weyl chamber”; Markdown L412 将其碎裂成 “exp {i,s}, where {i} ...”。300dpi 原页确认是同一单一希腊变量，需按原文修复。
- 印刷原貌：Lemma 4.5.8 陈述印作 $gPg^{-1}=P_\theta$ 且 $gP'g^{-1}=P_\theta$；紧接的证明则使用 $P_\theta^{-}$ 与 $P'$ 为 opposite。Markdown L404 忠实保留陈述中的原印字，按源级内部不一致登记，不代替原文改写。
- 处理：待全篇初审完成后用 Edit 恢复 L412 的参数写法并复核；4.5.8 陈述保留 print 原貌。

## p.016（PDF p.16 / 印刷 p.122）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:35 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p016.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p016_lemma_4_7_1.png`
- 核对：Lemmas 4.7.1–4.7.2、§5 导引图、§5.1 记号和 Remark、§5.2–§5.2.2 开头；对照印刷页与 MinerU Markdown L418–L432。
- 结果：FAIL。
- 差异：Markdown L428 引用 `images/page_15_image_4.jpg`，但相对目标 Markdown 所在目录该路径不存在。对应图像是已跟踪、只读的 `Margulis_1974_arithmetic_properties_en_mineru/Margulis_1974_arithmetic_properties_en/images/page_15_image_4.jpg`；图中节点和箭头与印刷 p.122 导引图一致。修复时只改 Markdown 链接为相对嵌套路径，不改 MinerU 图像。
- 备注：L420 中的 `g^{-1}(P)P_{j(P)}g(P)` 与印刷原页相符，按 print 原貌保留。

## p.017（PDF p.17 / 印刷 p.123）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:36 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p017.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片（补核）：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p017_section_5_4.png`
- 核对：§5.2.2 证明续段、5.2.3–5.5 引理与证明开头；对照印刷页与 MinerU Markdown L442–L474。
- 结果：FAIL（2026-10-02 补核）。
- 差异：§5.4 与 Lemma 5.4.1 的三处 Lie algebra 空间记号在印刷件中为小写 $\mathfrak u_{\mathbf R}$；MinerU Markdown 写成大写 $\mathfrak U_{\mathbf R}$。300dpi 裁片确认小写 $u$ 字形。
- 备注：本页其余初审范围按印刷页核对相符；先前 PASS 判定由本次页内补核修正。
- 处理：待初审修复阶段用 Edit 将 §5.4–§5.4.1 这三处大写字母改为小写，并复核定义与引理。

## p.018（PDF p.18 / 印刷 p.124）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:38 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p018.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p018_lie_algebra_u.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p018_phi_A_gamma.png`
- 核对：§5.5 定义、Lemmas 5.5.1–5.5.5 及证明；对照印刷页与 MinerU Markdown L476–L500。
- 结果：FAIL。
- 差异：印刷 5.5.1 proof 将表示作用空间写作小写 Lie algebra 𝔲；Markdown L480 多处写成大写 𝔘（包括空间定义、成员变量、C(𝔘) 和表示的目标空间）。300dpi 裁片确认字形为小写 𝔲。
- 印刷原貌：p.124 的 5.5.2 proof 印为 “φ(A ∩ Γ)”，Markdown L488 同样保留 A；按源级文字记录，不依据上下文改成 H。
- 处理：待全篇初审结束后用 Edit 将 L480 对应的 𝔘 逐处改为 𝔲，并复核本页。

## p.019（PDF p.19 / 印刷 p.125）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:40 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p019.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p019_lie_algebra_u.png`
- 核对：§6.1–§6.3.3 的引理与证明；对照印刷页与 MinerU Markdown L502–L524。
- 结果：FAIL。
- 差异：印刷 §6.3.1 证明的 Lie 代数记号为小写 𝔲_R；Markdown L516 将该空间及其两处后续引用均写为大写 𝔘_R。300dpi 裁片确认原字形为小写 𝔲。
- 处理：待全篇初审完成后用 Edit 将 L516 对应的大写 𝔘_R 逐处改为小写 𝔲_R，并复核证明。

## p.020（PDF p.20 / 印刷 p.126）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:42 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p020.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p020_theorem_6_4.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p020_DV_subscripts.png`
- 核对：Lemma 6.3.3 证明结尾、Theorem 6.4、§7.1–§7.2.2 陈述及证明开头；对照印刷页与 MinerU Markdown L526–L558。
- 结果：PASS±。
- 印刷原貌：Theorem 6.4 证明印作 “D = R_n(A), V = R_n(A)” 并随后援引 Lemma 6.3.3 得出 D = V；Markdown L536 忠实保留。300dpi 裁片确认印刷两个下标均为 n，按 print 原貌记录。

## p.021（PDF p.21 / 印刷 p.127）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:44 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p021.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p021_ultramaximal.png`
- 核对：Lemma 7.2.2 证明结尾、Definitions 1–2、Lemma 7.2.3 及证明、§7.3.1 引理和本页证明段；对照印刷页与 MinerU Markdown L558–L588。
- 结果：FAIL。
- 差异：印刷 Definition 1 两处均为 \(\bar U\)：`dim A(U)=dim \bar U`，且“\(\bar U\) is a subgroup of finite index in A(U)”。Markdown L562 两处都丢失 overline。印刷 Lemma 7.2.3 结论以及证明首句也均指 \(\bar U\)；Markdown L566 与 L568 均写成 U。300dpi 裁片确认四处印刷上划线。
- 处理：待全篇初审完成后用 Edit 在 L562、L566、L568 补回对应 overline，并逐处回核。

## p.022（PDF p.22 / 印刷 p.128）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:46 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p022.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p022_lemma_7_5_1_statement.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p022_lemma_7_5_1_proof_end.png`
- 核对：Lemma 7.4、Lemma 7.5.1 及其证明、Lemma 7.5.2 陈述/证明开头；对照印刷页与 MinerU Markdown L590–L602（跨页处）。
- 结果：PASS±。
- 印刷原貌：Lemma 7.5.1 陈述印作 “W ⊂ U”，其证明末尾却推得 “W ⊄ U”；两处均被 Markdown 忠实转录。300dpi 裁片确认这是印刷页内部不一致，保留原貌，不替原文协调。

## p.023（PDF p.23 / 印刷 p.129）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:48 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p023.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p023_lemma_7_5_2_7_6.png`
- 核对：Lemma 7.5.2 证明续段、§7.6 split case 证明及 §7.7 起句；对照印刷页与 MinerU Markdown L602–L616。
- 结果：FAIL。
- 差异：印刷 L7.5.2 的后半句为 “\(\bar U \ne \bar W\)”，Markdown L604 写成 “\(\bar U = \bar W\)”。印刷 §7.6 中 “\(\bar U' = V_{\varnothing}^{-}\)”，Markdown L606 写作 “\(\bar U' = V_{\varnothing'}\)”（空集后撇号，漏了负号）。300dpi 裁片确认两处原字形。
- 处理：待全篇初审完成后用 Edit 分别修正 L604 的关系符号与 L606 的负号/下标，并回核证明。

## p.024（PDF p.24 / 印刷 p.130）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:49 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p024.png` (Ghostscript, pngmono, 150dpi)
- 核对：§8.1 Grassmannian 记号/引理、§8.2 假设、§8.3 商空间构造与表示公式 (1)–(2)；对照印刷页与 MinerU Markdown L620–L650。
- 结果：PASS。
- 备注：维数范围、交空间维数 d、Λ-指标与两个表示公式均与印刷页相符；§8.4 从下一页开始。

## p.025（PDF p.25 / 印刷 p.131）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:51 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p025.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p025_lemmas_841_842.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p025_tM_definition.png`
- 核对：§8.4.1 proof、Lemma 8.4.2 陈述/证明、§8.5–Lemma 8.5.1 及线性映射定义；对照印刷页与 MinerU Markdown L660–L690。
- 结果：FAIL。
- 差异：1) 印刷 §8.4.1 proof 结尾为 “Therefore, U_n is non-empty”，Markdown L662 写成 U_x；2) 印刷 Lemma 8.4.2 在 L664、L668 对应的交空间项为 $T_{\lambda_i}N$，Markdown 将 N 并入算子下标，写成 $T_{\lambda_i N}$；3) 印刷 8.5 中 $t_M$ 的定义引导语只出现一次，Markdown L678 多出不完整重复句，随后 L680 又写出完整定义。
- 处理：待全篇初审完成后用 Edit 修正 U_n、两处 $T_{\lambda_i}N$，并移除重复引导句；修复后对照印刷页复核。

## p.026（PDF p.26 / 印刷 p.132）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:53 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p026.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p026_equation_4.png`
- 核对：Lemma 8.5.2 跨页证明与显示式 (4)、Lemma 8.5.3 陈述；对照印刷页与 MinerU Markdown L690–L710。
- 结果：FAIL。
- 差异：显示式 (4) 的印刷结尾是 $T_{\lambda}^{\Psi}(x)=\omega_x(\lambda)$；Markdown L703 将最终函数记号倒置为 $\omega_{\lambda}(x)$。300dpi 原页裁片确认下标 x、参数 λ 的次序。
- 处理：待全篇初审完成后用 Edit 将 L703 末项改为 $\omega_x(\lambda)$，并回核整条等式链。

## p.027（PDF p.27 / 印刷 p.133）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:54 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p027.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p027_lemma_8_5_3.png`
- 核对：Lemma 8.5.3 证明、§8.6 的 k-structure 引理及 §9 起句；对照印刷页与 MinerU Markdown L708–L734。
- 结果：FAIL。
- 差异：印刷 8.5.3 proof 写 “$\overline{T}^{\Psi}$ is a rational extension of $T^{\Psi}$”；Markdown L718 将被扩张的表示也写成 $\overline{T}^{\Psi}$，多出一条 overline。300dpi 裁片确认印刷 RHS 没有 overline。
- 印刷原貌：同页先选择 $z_i$，随后印作 “the $s_i$ form a basis of $\Psi$”；Markdown L710 忠实记录了这个未在前文引入的 $s_i$，按源级文字保留。
- 处理：待全篇初审完成后用 Edit 移除 L718 RHS 的多余 overline 并回核；L710 按 print 原貌保留。

## p.028（PDF p.28 / 印刷 p.134）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:56 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p028.png` (Ghostscript, pngmono, 150dpi)
- 核对：Lemma 9.1.1 证明续段、Lemma 9.2、Lemmas 9.3.1–9.3.2 陈述及 Lemma 9.3.2 证明开头；对照印刷页与 MinerU Markdown L742–L758 及 L760 的页内开头。
- 结果：PASS。
- 备注：本页可见的半直积/作用、有限指数结论和 $A_0\cap A_0'$ 记号与印刷页相符；L760 的证明续文从本页末尾 “Since” 后开始，后续部分在下一印刷页复核。

## p.029（PDF p.29 / 印刷 p.135）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 16:58 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p029.png` (Ghostscript, pngmono, 150dpi)
- 核对：Lemma 9.3.2 proof continuation、Lemmas 9.3.3–9.3.4、§9.4 notation/definition and Lemma 9.4.1 setup; 对照印刷页与 MinerU Markdown L758–L778。
- 结果：PASS±。
- 格式备注：MinerU Markdown L760 将连续证明段落包在单个数学分隔符中；逐句核对了其文字与本页印刷内容，未发现缺句或符号差异。此记法造成的呈现问题与内容忠实性分别记录。

## p.030（PDF p.30 / 印刷 p.136）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 17:00 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p030.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p030_lemma_9_4_1_9_5_1.png`
- 核对：Lemma 9.4.1 proof 余段、显示式 (1)、Theorem 9.5.1 陈述及 proof 开头、§9.6 起句；对照印刷页与 MinerU Markdown L792–L813。
- 结果：FAIL。
- 差异：印刷 Lemma 9.4.1 proof 写 “Γ is dense in G”，Markdown L798 写成 Γ′；印刷 Theorem 9.5.1 陈述写 Γ ⊂ G_Q，Markdown L805 将 Q 误作 0。300dpi 裁片确认两处印字。
- 印刷原貌：同页 Theorem 9.5.1 proof 的交叉引用印作 “Theorem 7.11”；Markdown L807 忠实保留该编号，按源级引用原貌记录。
- 处理：待全篇初审完成后用 Edit 将 L798 的 Γ′ 改为 Γ、L805 的 G_0 改为 G_Q，并逐项回核。

## p.031（PDF p.31 / 印刷 p.137）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 17:48 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p031.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p031_lemma_9_6_2_continuation.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p031_lie_algebra_u.png`
- 核对：Lemma 9.6.2 跨页陈述续句与证明、式 (2)、Lemma 9.6.3 陈述/证明开头；对照印刷页与 MinerU Markdown L812–L850。
- 结果：FAIL。
- 差异：印刷 Lemma 9.6.2 的续句为 “$R_u(P')$, then the subgroups $P_{\mathbf Z}=P\cap G_{\mathbf Z}$ and $P\cap\Gamma$ are commensurable”。Markdown L812 停在 “and”，L814–L824 将符号拆成孤立 display 块，遗漏了连接文字和 “are commensurable” 结论。另，印刷 proof L838 对 Lie algebra 𝔲 的数个引用为小写 𝔲，Markdown 写作大写 𝔘；300dpi 裁片确认字形。
- 处理：待全篇初审完成后用 Edit 恢复 Lemma 9.6.2 的完整续句并逐处将 L838 的 𝔘 改为 𝔲；回核完整陈述、证明和式 (2)。

## p.032（PDF p.32 / 印刷 p.138）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 18:38 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p032.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p032_lemma_9_6_3_statement.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p032_lemma_9_6_3_proof.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p032_lemma_9_6_3.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p032_lemma_9_6_3_roots.png`
- 核对：Lemma 9.6.3 proof 续段、Lemma 9.6.4、Theorem 9.7.1 与 §10 起句；对照印刷页与 MinerU Markdown L840–L867。
- 结果：FAIL。
- 差异：印刷 9.6.3 proof 写 $V_\theta \subset P_{\varnothing} \subset P_{\theta'}$；Markdown L852 写成 $V_\theta \subset P_{\varnothing'} \subset P_{\theta'}$，空集下标后多了撇号。300dpi 裁片确认原页为 $P_{\varnothing}$。
- 处理：待全篇初审完成后用 Edit 移除 L852 空集下标后的撇号，并回核相邻包含关系。

## p.033（PDF p.33 / 印刷 p.139）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 19:39 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p033.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p033_lemma_10_3.png`
- 核对：Lemma 10.2.1 proof 续段、Lemma 10.3 与 proof、§10.4 主定理证明和 §11.1 起句；对照印刷页与 MinerU Markdown L875–L893。
- 结果：PASS±。
- 印刷原貌：Lemma 10.3 proof 印作 “$P_1,\ldots,P_j$” 后接 “$1\leq j\leq i$”；Markdown L879 忠实转录这一编号不一致，按 print 原貌保留。

## p.034（PDF p.34 / 印刷 p.140）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 20:08 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p034.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p034_lemmas_1133_1134.png`
- 核对：§11.1 题注续段、§11.2 定义/引理、§11.3.1–§11.3.5 陈述和当页证明；对照印刷页与 MinerU Markdown L891–L923。
- 结果：FAIL。
- 差异：印刷 Lemma 11.3.3 写群指数 $|F'/F|$ 为 p 的幂；Markdown L913 写作 $|F'|/F|$，绝对值符号未包住商 $F'/F$。300dpi 裁片确认原式的竖线包围整个商。
- 印刷原貌：Lemma 11.3.4 proof 在定义 $M_k$ 后印作 “Then: 1) $M_s\supset V_Z$; 2) $M_s$ is a normal subgroup ...”; Markdown L919 忠实保留该原文记号，按 print 原貌记录。
- 处理：待全篇初审完成后用 Edit 将 L913 改为 $|F'/F|$ 并回核；L919 保留印刷所见 $M_s$。

## p.035（PDF p.35 / 印刷 p.141）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 20:27 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p035.png` (Ghostscript, pngmono, 150dpi)
- 核对：Lemma 11.3.5 proof 续段、Lemmas 11.3.6–11.5.1 陈述/证明开头；对照印刷页与 MinerU Markdown L923–L949。
- 结果：PASS。
- 备注：p-adic 指数/闭包记号、Newton 二项式论证、强逼近定理陈述和 11.5.1 数据均与印刷页相符；11.5.1 证明续至下一页。

## p.036（PDF p.36 / 印刷 p.142）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 20:46 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p036.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p036_section_13_1.png`
- 核对：11.5.1 proof 续段、§12 的引理与 Lemma 10.1 回代、§13.1 记号及 Lemma 13.2.1 陈述；对照印刷页与 MinerU Markdown L947–L977。
- 结果：FAIL。
- 差异：印刷 §13.1 的 $U'=R_u(P')$ 后记号为 $V_{\varnothing}$，Markdown L971 写成 $V_{\varnothing'}$；印刷 Lie 代数为小写 $\mathfrak u'$、$\mathfrak u''$，Markdown L971 写成大写 $\mathfrak U'$、$\mathfrak U''$。Lemma 13.2.1(2) 印刷子代数由 $\mathfrak u'\cup\mathfrak u''$ 生成，Markdown L973 写成 $\mathfrak A'\cup\mathfrak A''$。300dpi 裁片确认这些字形。
- 处理：待全篇初审完成后用 Edit 分别修正 L971、L973 的三个记号，并回核 §13.1 定义与 Lemma 13.2.1。

## p.037（PDF p.37 / 印刷 p.143）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 21:08 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p037.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p037_lemma_13_5_1.png`
- 核对：Lemma 13.2.1 proof 结尾、Lemmas 13.2.2–13.2.3、§13.3–§13.6.1；对照印刷页与 MinerU Markdown L975–L1001。
- 结果：FAIL。
- 差异：印刷页 §13.2.2 只有一条 Lemma，主张 $G_{\mathbf Z}\cap\Gamma$ 在 $G$ 中 Zariski-dense；其后直接进入该 Lemma 的 PROOF。Markdown L979 已记录该 Lemma，L981 又重复编号为 13.2.2，并新增一条印刷页上不存在的 “$U_{\mathbf Z}'\cap\Gamma$ is Zariski-dense in $G$” 作为第二条陈述，导致原证明没有正确挂接到唯一 Lemma。另，印刷 L13.5.1 的有限集为 $M$ 和 $\widetilde M$；Markdown L997 两处均写成 $M$，第二集漏波浪号。
- 处理：待全篇初审完成后用 Edit 删除重复 Lemma 头及错误新增陈述、将第二个 $M$ 补为 $\widetilde M$，并逐句核对。

## p.038（PDF p.38 / 印刷 p.144）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 22:34 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p038.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p038_xi_definition.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p038_xi_notation.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p038_lemma_13_8_1.png`
- 核对：§13.6–§13.7.1 的函数符号与界、§13.8.1 陈述及 proof 开头；对照印刷页与 MinerU Markdown L999–L1031。
- 结果：FAIL。
- 差异：印刷 §13.7 在 ψ(h)、ω(h) 定义及其不等式中重复同一个函数符号；Markdown L1010、L1013、L1023 分别以 𝔵、ξ、χ/ξ 混用，未忠实保留统一的印刷记号。300dpi 裁片显示这些位置为同一符号字形。
- 印刷原貌：§13.8.1 陈述的共轭式印刷为 “γ_{U,p}Uγ_{U,p}^{-1}p = uU''u^{-1}”，含有其所见的尾随 p；Markdown L1027 保留该字形，按原貌记录。
- 处理：待全篇初审完成后用 Edit 将 §13.7 对应函数记号统一为印刷所见符号并回核；§13.8.1 的尾随 p 不按数学预期改写。

## p.039（PDF p.39 / 印刷 p.145）[Peer-P19 | gpt-6-luna/max] · 2026-10-01 23:13 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p039.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p039_lemma_14_2_1.png`
- 核对：§14.1 定义/引理与 Lemma 14.2.1 陈述、证明开头及显示式 (1)；对照印刷页与 MinerU Markdown L1033–L1055。
- 结果：FAIL。
- 差异：印刷 Lemma 14.2.1 下界中的模数为 $p(t(rp^{2l}))p^{2l}\mathbf Z$；Markdown L1049 写为 $p(t(rp^2l))_p^{2l}\mathbf Z$，将指数 $2l$ 拆开，并把相乘的第二个 $p^{2l}$ 变成下标结构。300dpi 裁片确认印刷的指数和因子位置。
- 处理：待全篇初审完成后用 Edit 按原式重排 L1049 模数并复核定义域/指数。

## p.040（PDF p.40 / 印刷 p.146）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:11 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p040.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p040_lemma_14_3.png`
- 核对：§14.2.1 显示式 (2)–(3)、§14.3 推导与显示式 (4)、§15.1 起始记号/定义；对照印刷页与 MinerU Markdown L1057–L1101。
- 结果：PASS±。
- 印刷原貌：本页 14.3 写 $u\in U_{\mathbf Q}$，并写 $\gamma_{U,p}U\gamma_{U,p}^{-1}=uU''u^{-1}$；p.144 的 13.8.1 陈述则印作 $u\in U'_{\mathbf Q}$ 且共轭式在逆元后多一个 p。Markdown 分页保留两处各自的印刷原貌，不作跨页归一化；本页显示式与对应 Markdown 相符。

## p.041（PDF p.41 / 印刷 p.147）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:13 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p041.png` (Ghostscript, pngmono, 150dpi)
- 核对：§15.1.2、§15.2 引理/证明、§15.3.1 陈述及式 (1)–(2)；对照印刷页与 MinerU Markdown L1097–L1129。
- 结果：PASS。
- 备注：root-space 直和、交换子记号、p-adic 邻域条件和两个指数界均与印刷页相符；15.3.1 的证明续至下一页。

## p.042（PDF p.42 / 印刷 p.148）[Peer-P19 | gpt-6-luna/max] · 2026-10-02
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p042.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p042_equations_3_5.png`
- 300dpi 页尾裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p042_lemma_15_3_2_tail.png`
- 核对：§15.3.1 的证明续段、显示式 (3)–(5)、§15.3.2 Lemma 与 proof 开头；对照印刷页与 MinerU Markdown L1119–L1169。页尾补核 L1171–L1183。
- 结果：FAIL。
- 差异：印刷显示式 $(U'\cap\Lambda)_{\mathbf Q_p}\supset a_1\{V',a_1^{-1}a_2\}a_1^{-1}$ 带有编号 (4)，Markdown L1148 保留该公式但无标签；Markdown L1131 则将孤立的 `(4)` 放在前一段 (2) 后、公式前。300dpi 裁片确认 (4) 与公式同一行组，且后文 “From this and from (4)” 引用该式。
- 补充差异（页尾，2026-10-02 00:41 EDT）：印刷续写 $gP_{a\mathbf Z}''g^{-1}\supset (gP''g^{-1})_{a^2\mathbf Z}$ 后，接有 “hence ... is of index at most $k$ in $(gP''g^{-1})_{\mathbf Z}$” 的有限指数结论；Markdown L1171–L1175 保留前两项关系，L1177–L1183 却拆出两个无关系的公式碎片，漏掉结论句。300dpi 页尾裁片确认印刷关系与结论连续排印。
- 处理：待全篇初审完成后用 Edit 将 (4) 移到 L1148 的公式；并在同次复核中修复页尾有限指数句，移除 L1177–L1183 的孤立重复碎片。回核公式、结论及后续引用。

## p.043（PDF p.43 / 印刷 p.149）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:40 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p043.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p043_equations_6_8.png`
- 核对：§15.3.2 proof 续段、显示式 (6)–(8)、强非紧群的 Lemma 12.2.1 proof 与 §15.4 起始；对照印刷页与 MinerU Markdown L1185–L1215。
- 结果：FAIL。
- 差异：显示式 (6) 印刷为 $(U_{\mathbf Z}'\cap g_0\Gamma g_0^{-1})_{\mathbf Q_p}\supset V(K(g_0),T)$，其中整数环指标是大写 $Z$；Markdown L1194 写为 $U_{\mathbf z}'$，误作小写 $z$。300dpi 裁片确认印刷为大写字形。
- 处理：待全篇初审完成后用 Edit 将 L1194 的小写指标改为大写 $Z$，并回核显示式 (6)。

## p.044（PDF p.44 / 印刷 p.150）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:42 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p044.png` (Ghostscript, pngmono, 150dpi)
- 核对：§15.4.1 分类引理及推论、§15.4.2 引理与 proof、§15.4.3–§15.5、§16.1–16.1.1；对照印刷页与 MinerU Markdown L1213–L1243。
- 结果：PASS。
- 备注：分类类型、域限制/秩条件、显示式 (9)、证明的 restriction-of-scalars 记号及 §16.1.1 引理陈述均与印刷页相符。

## p.045（PDF p.45 / 印刷 p.151）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:43 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p045.png` (Ghostscript, pngmono, 150dpi)
- 核对：§16.2–§16.4.3 的定义、两条引理及证明，特别是 Lemma 16.2.1(1)–(3)、有限生成结论和 Lemma 12.1.1 proof 末段；对照印刷页与 MinerU Markdown L1245–L1265。
- 结果：PASS。
- 备注：整数点群、紧商、共轭类有限性、素因子集构造及其记号均与印刷页相符。

## p.046（PDF p.46 / 印刷 p.152）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:46 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p046.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p046_problem_17_1_full.png`
- 核对：§17.1–§17.4 的问题陈述、Appendix 开头至首段续页；对照印刷页与 MinerU Markdown L1267–L1281。
- 结果：PASS±。
- 印刷原貌：§17.1 括号内印刷作 “$x\in X'$” 后换行接 “$\lambda\ne e$”，X 后带撇且两条件间缺逗号；Markdown L1270 保留该印刷形态。按 print 原貌记录，不依数学预期补逗号或删撇。

## p.047（PDF p.47 / 印刷 p.153）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:47 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p047.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p047_equation_1.png`、`audit/300dpi/Margulis_1974_arithmetic_properties_en_p047_appendix_lemma.png`
- 核对：Appendix Lemma 4.5.1 证明续段、显示式 (1)、该 Lemma 与 references [1]–[5]；对照印刷页与 MinerU Markdown L1281–L1306。
- 结果：FAIL。
- 差异：显示式 (1) 印刷为 $[\mathfrak G_0,x]\not\ni x$（$x$ 不属于该括号像）；Markdown L1281 写成 $[\mathfrak{G}_0,x]\nmid x$（“不整除”）。另，印刷 proof 写 “representation of $\mathfrak A$ ... in $\mathfrak G$”，Markdown L1287 将两处 fraktur 字母写成普通 $A$、$G$。300dpi 裁片确认运算符与字体字形。
- 处理：待全篇初审完成后用 Edit 将 L1281 运算符还原为 $\not\ni$，并将 L1287 的 $A,G$ 改为 $\mathfrak A,\mathfrak G$；回核公式及该句。

## p.048（PDF p.48 / 印刷 p.154）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:49 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p048.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p048_reference_15.png`
- 核对：References [6]–[21]；对照印刷页与 MinerU Markdown L1308–L1348。
- 结果：FAIL。
- 差异：印刷参考文献 [15] 在 MR 41 #8595 后还列有俄译刊载信息 “= Matematika 16 (1972), no. 4, 74–91.”；Markdown L1332 在 MR 号后直接结束该条并进入 [16]，漏掉此行。300dpi 裁片确认该续行位于 [15] 条目内。
- 处理：待全篇初审完成后用 Edit 将该刊载信息补入 [15]，并复核 [15] 与 [16] 的条目边界。

## p.049（PDF p.49 / 印刷 p.155）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:51 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p049.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p049_reference_29.png`
- 核对：References [22]–[35]；对照印刷页与 MinerU Markdown L1350–L1387。
- 结果：PASS±。
- 印刷原貌：[29] 标题原印作 “Non-uniform latticee in semisimple algebraic groups”；300dpi 裁片确认双写 e 是印刷原貌，Markdown L1371 忠实保留，不改为预期拼法。

## p.050（PDF p.50 / 印刷 p.156）[Peer-P19 | gpt-6-luna/max] · 2026-10-02 00:52 EDT
- PNG: `audit/Margulis_1974_arithmetic_properties_en_p050.png` (Ghostscript, pngmono, 150dpi)
- 300dpi 裁片：`audit/300dpi/Margulis_1974_arithmetic_properties_en_p050_publication_footer.png`
- 核对：References [36]–[49] 及论文末尾刊务信息；对照印刷页与 MinerU Markdown L1389–L1422。
- 结果：FAIL。
- 差异：印刷页在参考文献 [49] 后另列 “Received by the Editors 16 July 1973” 和 “Translated by J. S. Joel”；Markdown 在 L1422 的 [49] 条目后即结束，缺少收稿日期和译者署名。300dpi 页尾裁片确认两行均在该印刷页上。
- 处理：待全篇初审完成后用 Edit 在 [49] 后补入两行刊务信息，并复核文末位置及字样。
