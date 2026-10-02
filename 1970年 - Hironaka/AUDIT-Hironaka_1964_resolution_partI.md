# Hironaka, Resolution of Singularities, Part I — 逐页审计

## 任务与来源

- 状态：进行中；终审、修复登记与全文复读待完成。
- Actor：Peer-P38；model：gpt-6-luna；reasoning effort：max。
- 角色：CONTRIBUTOR；唯一 canonical integrator：Master-Luna。
- 审计基线：`037602429d3b009f6fc468c732073eb3ddf9875f`（main 的任务基线）。
- 源 PDF：`Hironaka_1964_resolution_partI.pdf`；PDF 物理页数 96；SHA-256 `5827903e8edb78f93660c3ef7fa17fb2c83aa1718ed6b88d9aed2dcc65a63bd7`。
- 唯一审计对象：`Hironaka_1964_resolution_partI_mineru/Hironaka_1964_resolution_partI__Hironaka_1964_resolution_partI.md`；修复前 SHA-256 `15f32017f4527f5e7ec8141804338637459dff4198d9535a69632714da3d21c2`；修复前行数/字节数 `2134 / 314059`。
- 源类型：born-digital。`pdfinfo` 记录 Creator `PDFplus`、Producer `Atypon Systems, Inc.`；UTF-8 `pdftotext` 文本层 232523 字节、U+FFFD 计数 0。以 PDF 文本层逐物理页对账；目检题录页和 1–2 个密集数学页；文本层丢失/压平的符号及其他疑点回到源页 PNG 或 300dpi 裁片裁决。
- 页码映射：PDF p.001 是无印刷页码的 JSTOR 包装页；PDF p.002 印刷页 109，PDF p.096 印刷页 203。README 所列 95 页对应印刷页 109–203；任务索引与 PDF 物理页数均为 96。
- 唯一证据图像名前缀：`audit/Hironaka_1964_resolution_partI_` 与 `audit/300dpi/Hironaka_1964_resolution_partI_`。未引用的临时渲染不保留。
- 本篇页级签认由本文件和逐页 Git commits 保存；根 `AUDIT-PROGRESS.log`、`AUDIT-INDEX.md`、README 与 MEMORY 由 Master 独占维护，本 Peer 不修改。

## 逐页签认

### PDF p.001 / 96（无印刷页码）— PASS±

- 时间：2026-10-01 16:18 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.001 文本层与 MinerU Markdown 第 1–13 行。标题、JSTOR 题录、稳定 URL、访问时间、使用条款和服务说明均对应；MinerU 未保留页底 “Annals of Mathematics is collaborating with JSTOR …” 说明及裸站点 URL。该遗漏属于 JSTOR 包装页平台说明，不改变论文内容或书目信息，记录为非误导性差异，不修正文档。
- 结论：PDF p.001 是 JSTOR 包装页，未发现论文正文内容缺失；仅有上述包装说明省略。

### PDF p.002 / 96（印刷 p.109，题录页）— PASS

- 时间：2026-10-01 16:21 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.002 文本层、入库题录页图 `audit/Hironaka_1964_resolution_partI_p002.png`（pngmono 150dpi）与 MinerU Markdown 第 14–61 行。题名、作者、献词、收稿/修订日期、Part II 说明、参考文献 1–18 与作者资助脚注均相符。图像确认文本层的特殊字符提取失真不是印刷错误；例如参考文献 [1] 的 `p ≠ 0` 在 Markdown 中对应为 `p \neq 0`。
- 结论：本页论文题录及参考文献内容与印刷页相符；未发现需修订项。

### PDF p.003 / 96（印刷 p.110）— FAIL

- 时间：2026-10-01 16:24 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.003 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p003.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p003_refs28_29.png` 与 MinerU Markdown 第 63–83 行。参考文献 [19]–[29] 顺序与主体可对账，但 [28] 在第 81 行停于 `Accad.`；印刷页还含 `Naz. dei Lincei, Roma, 31 (1962), 97-102 (Nota I) pp. 177-180 (Nota II).`，整段书目信息缺失，无法从当前条目定位完整来源。
- 源级 print quirk：参考文献 [29] 印刷为 `Trans,`（逗号）；Markdown 保留该印刷字形，禁止据出版物惯例改成句点。
- 备注：本页还开始目录，印刷内容到 Chapter III §4；Markdown 目录继续到 Chapter IV，后续部分须与 PDF p.004 对账。运行页眉 `HEISUKE HIRONAKA` 与页码 110 未录入 Markdown，属于重复导航元素省略。
- 结论：引用 [28] 后半段确实缺失，列为 FAIL，待全篇审计结束后依据本页原文修复。

### PDF p.004 / 96（印刷 p.111）— PASS±

- 时间：2026-10-01 16:26 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.004 文本层、目检页图 `audit/Hironaka_1964_resolution_partI_p004.png`（pngmono 150dpi）与 MinerU Markdown 第 133–169 行。目录 Chapter III §5–§10、Chapter IV §1–§4 与该页续文吻合；开篇公式映射 `f:\widetilde{X} \to X` 及 `f^{-1}(V) \xrightarrow{\approx} V` 已在图像核验，后者与 Markdown 相符。文本层把这些符号压平，但未造成 Markdown 丢失。
- 备注：印刷运行页眉和页码 111 未录入 Markdown，属不影响正文的导航元素省略。
- 结论：目录续项及 Introduction 起始段无实质差异；因运行页眉/页码省略记为 PASS±。

### PDF p.005 / 96（印刷 p.112）— FAIL

- 时间：2026-10-01 16:28 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.005 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p005.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p005_theorem_I.png` 与 MinerU Markdown 第 169–181 行。印刷多次写作 `Main theorem I`、`I*`、`I(n)`、`I'`、`I'(n)`、`I''(n)`；Markdown 第 177、179 行相应写成数字 `1`（如 `main theorem 1(n)`、`1'(n)`）。300dpi 图确认均为罗马大写 I，非阿拉伯数字 1，属于定理名称误录，待全篇审计后逐处手工修复。该页的映射公式 `f: \widetilde{X} \to X`、`f^{-1}(V) \xrightarrow{\approx} V` 及脚注 1 与原页相符。
- 备注：印刷运行页眉与页码 112 未录入 Markdown，属非误导性导航元素省略。
- 结论：定理编号 I 被误录为 1，列为 FAIL；修复前保留原稿。

### PDF p.006 / 96（印刷 p.113）— PASS±

- 时间：2026-10-01 16:29 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.006 文本层与 MinerU Markdown 第 183–190 行。Introduction 对 Chapter 0 §§1–3、§5 的概述、Levi–Zariski 说明、normal flatness 与代数边界段落逐项相符；本页末尾在“into an”处接续至下一物理页，Markdown 后续行与之衔接。
- 备注：印刷运行页眉与页码 113 未录入 Markdown，属不影响正文的导航元素省略。
- 结论：未发现正文或数学记号差异；因运行页眉/页码省略记为 PASS±。

### PDF p.007 / 96（印刷 p.114）— PASS±

- 时间：2026-10-01 16:29 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.007 文本层、页图 `audit/Hironaka_1964_resolution_partI_p007.png`（pngmono 150dpi）与 MinerU Markdown 第 191–205 行。Introduction 章节概述、脚注 2、以及基本定理标签 `I_{1}^{N,n}`、`I_{2}^{N,n}`、`II_{1}^{N}`、`II_{2}^{N}` 均与印刷页相符；图像校正了文本层在这些下标/上标处的丢失。
- 备注：印刷运行页眉和页码 114 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.008 / 96（印刷 p.115）— PASS±

- 时间：2026-10-01 16:31 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.008 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p008.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p008_nu_tau.png` 与 MinerU Markdown 第 207–209 行。逐项核对 normal-flatness 概述及 Chapter III 内容；300dpi 裁片确认原文的记号为 `ν*` 与 `τ*`，Theorem 3 的比较方向与 Markdown 中 `\nu^{*}`、`\tau^{*}` 相符。Markdown 行 209 在 “those” 处接续到下一物理页。
- 备注：印刷运行页眉和页码 115 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现正文、定理记号或比较关系差异；因运行页眉/页码省略记为 PASS±。

### PDF p.009 / 96（印刷 p.116）— PASS±

- 时间：2026-10-01 16:32 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.009 文本层、页图 `audit/Hironaka_1964_resolution_partI_p009.png`（pngmono 150dpi）与 MinerU Markdown 第 211、213、215–221 行。图像核定本页的符号为 `τ-frame`（文本层误成 `z-frame`）；Markdown 写作 `τ-frame`，并且 local-uniformization/Chapter IV 概述及脚注 3–5 对应原页。印刷作者致谢止于 `Professor`，Markdown 下一行从 `M. Kuranishi` 续接，未漏文。
- 备注：印刷运行页眉和页码 116 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.010 / 96（印刷 p.117）— FAIL

- 时间：2026-10-01 16:35 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.010 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p010.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p010_topology_not_supset.png`、局部态射裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p010_local_map.png` 与 MinerU Markdown 第 227–231 行。拓扑定义的印刷关系为 `P ⊅ I`（素理想 P 不包含理想 I），Markdown 写成 `P \not\cong I`；关系含义错误。局部态射裁片显示印刷为 `O_Y → O_X`，Markdown 写成 `O_Y → O_x`；印刷局部环目标为 `O_{X,x}`，Markdown 仅写 `O_X`，漏掉点下标 `,x`。该页类别花体 `\mathcal{R}` 在 Markdown 中记作普通 `R`，仅属排版差异。
- 结论：拓扑开集条件及 local-ringed-space/sheaf 记号有实质错误，列为 FAIL；待完成全篇审计后逐处核验和手工修复。

### PDF p.011 / 96（印刷 p.118）— PASS±

- 时间：2026-10-01 16:38 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.011 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p011.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p011_products.png` 与 MinerU Markdown 第 235–243 行。文本层压平了基底积、对角映射和 Hom 同构中的符号；图像确认 Markdown 的 `\pi_1`、`\pi_2`、`\Delta` 与同构关系正确。印刷产品符号使用小写下标 `s`（`\times_s`），Markdown 忠实保留，不按对数学记号的预期改成大写。印刷类别符号有独特字形，Markdown 记为普通 `S`，只记录为排版差异。
- 备注：印刷运行页眉和页码 118 未录入 Markdown，属非误导性导航元素省略。
- 结论：该页定义与映射内容相符；仅有类别符号字形和运行页眉/页码省略，记为 PASS±。

### PDF p.012 / 96（印刷 p.119）— PASS±

- 时间：2026-10-01 16:40 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.012 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p012.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p012_structural_morphism_order.png` 与 MinerU Markdown 第 247–251 行。有限型定义、类别路由、结构映射和复/实解析空间定义均与本页对应；文本层丢失了多处类别字形和映射符号，页图支持 Markdown 的 `p: X \to S`、`f: X_1 \to X_2` 与 `X_i` 等记号。
- 源级 print quirk：印刷原页本身写作 `p_1 = f \circ p_2`，虽然前句将 `f` 写成 `X_1 \to X_2`，后句将 `p_i` 写成 `X_i \to S`。该组合顺序在类型上不相容，但 MinerU Markdown 忠实转录原页；按 print 优先原则不修正文档，只在此登记。
- 备注：印刷运行页眉和页码 119 未录入 Markdown；部分花体类别字形简化为普通体。
- 结论：未发现由 Markdown 新增的内容差异；保留已印出的映射次序 quirk，按 PASS± 记录。

### PDF p.013 / 96（印刷 p.120）— FAIL

- 时间：2026-10-01 16:42 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.013 文本层、页图 `audit/Hironaka_1964_resolution_partI_p013.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p013_complexification_symbols.png` 与 MinerU Markdown 第 253–267 行。高分辨率对照确认这些位置的印刷结构层下标为大写空间标识 X，Markdown 第 253、255、261 行写作小写 `O_x`；此前把小号大写 X 误认作小写 x 并降级为 PASS±，现撤回。其余 Hausdorff、Kⁿ-coordination、复化映射、同构条件及脚注 7 相符。
- 备注：印刷运行页眉和页码 120 未录入 Markdown，属不影响正文的导航元素省略。
- 结论：结构层大写空间下标误录为小写，列为 FAIL；运行页眉与页码另未录入 Markdown。

### PDF p.014 / 96（印刷 p.121）— FAIL

- 时间：2026-10-01 16:45 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.014 文本层、页图 `audit/Hironaka_1964_resolution_partI_p014.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p014_sheaf_and_stalk.png` 与 MinerU Markdown 第 273、275 行。高分辨率对照确认印刷结构层为 `O_X`，点处局部环为 `O_{X,x}`；Markdown 分别写为 `O_x` 与 `O_{x,x}`，丢失大写空间标识 X。此前将小号大写 X 误读为小写并降级为 PASS±，现撤回。其余 simple/multiple 点条件、解析坐标、复化及脚注 8–11 相符。
- 备注：页内关于简单/多重点、解析坐标、复化及脚注 8–11 的其余内容与原页相符；印刷运行页眉、页码 121 未录入 Markdown。
- 结论：结构层/局部环下标误录大小写，列为 FAIL；运行页眉与页码另未录入 Markdown。

### PDF p.015 / 96（印刷 p.122）— FAIL

- 时间：2026-10-01 16:46 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.015 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p015.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p015_local_ring_indices.png` 与 MinerU Markdown 第 285–297 行。条件 (1) 印刷为局部环 `O_{X,\lambda(\hat{x})}`，条件 (2) 的 homomorphism source 同样以该局部环为源；Markdown 第 287、289 行均漏掉 `X` 与 `\lambda(\hat{x})` 之间的逗号，损坏局部环下标结构。其余 universal-property/canonical-map 关系及脚注 12 与原页相符。
- 备注：印刷运行页眉与页码 122 未录入 Markdown，属导航元素省略。
- 结论：局部环 index 标点缺失，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.016 / 96（印刷 p.123）— PASS±

- 时间：2026-10-01 16:48 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.016 文本层、页图 `audit/Hironaka_1964_resolution_partI_p016.png`（pngmono 150dpi）与 MinerU Markdown 第 299–307 行。模块、态射对、同调映射、blowing-up 的 universal mapping property 及存在定理段落均与该页相符；文本层多处损失 `\mathcal{R}`、`\mathcal{M}`、`\Phi` 等符号，已对照页图确认 Markdown 保留这些记号。
- 备注：印刷运行页眉和页码 123 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.017 / 96（印刷 p.124）— FAIL

- 时间：2026-10-01 17:45 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.017 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p017.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p017_proj_and_stalks.png` 与 MinerU Markdown 第 317、319 行。对称张量代数和 Proj 构造均与原页对应；高分辨率对照显示印刷结构层写作 `O_X`/`O_{X'}`，Markdown 第 317 行误作 `O_x`/`O_{x'}`，第 319 行的结构层 `O_X` 也误作 `O_x`。局部点处的 `O_x` 在 line 319 保持原样，不与结构层混淆。
- 备注：印刷运行页眉和页码 124 未录入 Markdown，属不影响正文的导航元素省略。
- 结论：结构层空间下标大小写误录，列为 FAIL；运行页眉与页码 124 另未录入 Markdown。

### PDF p.018 / 96（印刷 p.125）— FAIL

- 时间：2026-10-01 23:24 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.018 文本层、页图 `audit/Hironaka_1964_resolution_partI_p018.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p018_Px_sheaf.png` 与 MinerU Markdown 第 325、327 行。印刷定义为 `P^x=(P^x,O_{P^x})`，Markdown 第 325 行写成 `O_{Px}`，漏掉结构层下标中 P 的上标 x；裁片确认原页上下标。对称张量代数、开集基和脚注 13–14 的其余部分逐项对应。
- 备注：印刷运行页眉和页码 125 未录入 Markdown，属导航元素省略。
- 结论：结构层下标丢失上标，列为 FAIL，待全篇审计完成后逐处修复。

### PDF p.019 / 96（印刷 p.126）— PASS±

- 时间：2026-10-02 00:12 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.019 文本层、页图 `audit/Hironaka_1964_resolution_partI_p019.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p019_analytic_projective.png` 与 MinerU Markdown 第 329–335 行。解析 K-cover、`\lambda^{*}(I)`、`\Psi=(f\circ\lambda,\psi\circ\varphi)` 和 projective 映射定义逐项核对相符。
- 源级 print quirk：印刷给出的 `\tilde{f}` 同构目标写为 `X|h^{-1}(T)`（未带波浪），即使此前定义 `N=(\tilde{X},\tilde{J})` 且 `\Phi=(h,\alpha)`；Markdown 忠实保留该页字面式，不按图式预期补波浪。
- 备注：印刷运行页眉和页码 126 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现 Markdown 与印刷页的内容差异；登记源页式样 quirk，并因页眉/页码省略记为 PASS±。

### PDF p.020 / 96（印刷 p.127）— PASS±

- 时间：2026-10-02 00:15 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.020 文本层、页图 `audit/Hironaka_1964_resolution_partI_p020.png`（pngmono 150dpi）与 MinerU Markdown 第 339–343 行。Chow 定理段落续文、`(\mathcal{R}/S)`-ideal 定义、映射对与 sheaf homomorphism 条件、annihilator 构造及 footnote 14″ 均相符；页图确认文本层压平的 `\theta`、`\varphi` 和结构 sheaf 下标按 Markdown 当前写法保留。
- 备注：印刷运行页眉与页码 127 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.021 / 96（印刷 p.128）— PASS±

- 时间：2026-10-02 00:19 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.021 文本层、页图 `audit/Hironaka_1964_resolution_partI_p021.png`（pngmono 150dpi）与 MinerU Markdown 第 345–349 行。coherent ideal categories、(S_A^*(J))/(I_1^*) 的 Proj 构造、从局部 ringed spaces 态射诱导 sheaf-ideal 映射及逆像记号均与印刷页相符；页图核验了文本层丢失的上/下标和范畴符号。
- 备注：印刷运行页眉和页码 128 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.022 / 96（印刷 p.129）— FAIL

- 时间：2026-10-02 00:24 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.022 文本层、页图 `audit/Hironaka_1964_resolution_partI_p022.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p022_ideal_morphism.png` 与 MinerU Markdown 第 357 行。印刷定义的局部环结构层商为 `O_X/J`，限制到 D；Markdown 写作 `O_x/J`，把空间下标 X 变成小写 x。裁片核准该字形不是局部点变量。其余 universal property、理想/子空间对应及 footnote 15 对应。
- 备注：印刷运行页眉和页码 129 未录入 Markdown，属导航元素省略。
- 结论：结构层下标大小写误录，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.023 / 96（印刷 p.130）— FAIL

- 时间：2026-10-02 00:42 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.023 文本层、页图 `audit/Hironaka_1964_resolution_partI_p023.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p023_generic_local_ring.png` 与 MinerU Markdown 第 363–369 行。本页印刷给出 generic point 处局部环 `O_{X,\bar{x}}`；Markdown 第 367 行写为 `O_{x,\bar{x}}`，把空间标识 X 误为小写 x。章节题名中的 `Main theorem I`、generic point 横线及其余域扩张记号与原页相符。
- 备注：印刷运行页眉和页码 130 未录入 Markdown，属导航元素省略。
- 结论：局部环空间下标误录大小写，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.024 / 96（印刷 p.131）— FAIL

- 时间：2026-10-02 00:47 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.024 文本层、页图 `audit/Hironaka_1964_resolution_partI_p024.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p024_references.png` 与 MinerU Markdown 第 369、373 行。脚注 [16] 印刷书名为 `Faisceaux algébriques cohérents`，Markdown 第 373 行写成 `Faisceaux algebrigues cohérents`，重音和字母次序均不符；需按此页书名修复。方程/域扩张段的符号对应原页。
- 源级 print quirk：同一页正文印刷拼作 `conicides`；Markdown 忠实保留此拼法，不按英语惯用拼法订正。
- 备注：印刷运行页眉和页码 131 未录入 Markdown，属导航元素省略。
- 结论：参考文献 [16] 书名发生 OCR 误录，列为 FAIL；源级正文拼写 quirk 保留。

### PDF p.025 / 96（印刷 p.132）— FAIL

- 时间：2026-10-02 00:53 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.025 文本层、页图 `audit/Hironaka_1964_resolution_partI_p025.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p025_theorem_I.png` 与 MinerU Markdown 第 375–399 行。印刷在第 381、383 行关联段落和本页强形式起句反复使用罗马大写 `I`；Markdown 将其误录为阿拉伯 `1`（行 381、383）或小写 `i`，并在第 391 行把 `theorem` 拼成 `therem`。裁片确认这不是印刷写法差异，待全篇初审结束后逐处修复。
- 备注：印刷运行页眉与页码 132 未录入 Markdown，属导航元素省略。
- 结论：定理编号与术语有 OCR 误录，列为 FAIL。

### PDF p.026 / 96（印刷 p.133）— FAIL

- 时间：2026-10-02 01:00 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.026 文本层、页图 `audit/Hironaka_1964_resolution_partI_p026.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p026_multiplicity_stalk.png` 与 MinerU Markdown 第 399–409 行。印刷 multiplicity 定义中的局部环为 `O_{x,x}`；Markdown 第 409 行写成 `O_{Xx}`（无分隔逗号），随后将 multiplicity 写作 `e(O_{X,x})`，下标与印刷的两级小写索引不一致。其他 (gr_m^p(A))、ν_M(J) 及 theorem I* 记号与本页相符。
- 备注：印刷运行页眉和页码 133 未录入 Markdown，属导航元素省略。
- 结论：局部环 stalk 下标误录，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.027 / 96（印刷 p.134）— FAIL

- 时间：2026-10-02 01:06 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.027 文本层、页图 `audit/Hironaka_1964_resolution_partI_p027.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p027_multiplicity_bounds.png` 与 MinerU Markdown 第 411–433 行。Statements (A)–(C)、Question (D) 的 multiplicity 阈值 `≥ d`、`< d` 与前后映射均对应原页；但原文两处写作罗马大写 `Main theorem I`，Markdown 第 431 行写成数字 `1`，属于定理编号误录。
- 备注：印刷运行页眉和页码 134 未录入 Markdown，属导航元素省略。
- 结论：定理编号 I/1 不符，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.028 / 96（印刷 p.135）— FAIL

- 时间：2026-10-02 01:12 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.028 文本层、页图 `audit/Hironaka_1964_resolution_partI_p028.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p028_main_theorem_I.png` 与 MinerU Markdown 第 435–453 行。印刷页写作 `main theorem I`（强形式引用），Markdown 第 451 行写成 `main theorem 1`；300dpi 图确认是罗马大写 I。Definition 1 关于 `gr_D^p(X)` 与 `J^p/J^{p+1}` 的记号与原页一致。
- 备注：印刷运行页眉和页码 135 未录入 Markdown，属导航元素省略。
- 结论：定理编号 I 误录为 1，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.029 / 96（印刷 p.136）— FAIL

- 时间：2026-10-02 01:17 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.029 文本层、页图 `audit/Hironaka_1964_resolution_partI_p029.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p029_theorem_I.png` 与 MinerU Markdown 第 455–469 行。normal-flatness 定义中的 `gr_D^p(X)`、`J^p/J^{p+1}`、`O_{D,x}` 及命题 (I)、(II) 与原页相符；第 467 行的 `main theorem 1` 对应印刷的罗马大写 `main theorem I`，属定理编号误录。
- 备注：印刷运行页眉和页码 136 未录入 Markdown，属导航元素省略。
- 结论：定理编号 I/1 不符，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.030 / 96（印刷 p.137）— PASS±

- 时间：2026-10-02 01:23 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.030 文本层、页图 `audit/Hironaka_1964_resolution_partI_p030.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p030_stability_and_I.png` 与 MinerU Markdown 第 469–485 行。脚注 18–19、singularity character `s_x(X/Y)`、性质 (1) 的比较关系、性质 (2) 的 `i ≥ r` 等号方向及 Question (D*) 起始段逐项对应；图像确认文本层丢失的上/下标和不等号方向未进入 Markdown。
- 备注：印刷运行页眉和页码 137 未录入 Markdown，属导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.031 / 96（印刷 p.138）— FAIL

- 时间：2026-10-02 01:30 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.031 文本层、页图 `audit/Hironaka_1964_resolution_partI_p031.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p031_theorem_I_star.png` 与 MinerU Markdown 第 485–515 行。印刷 `main theorem I`（上一节定理的引用）为罗马大写 I，Markdown 第 493 行写成数字 `1`。Question (D*) 的映射、限制及严格下降式与本页对应。
- 源级 print quirk：MAIN THEOREM I* 的条件 (b) 在印刷中写成 `X_r`，虽周围索引为 `i`；Markdown 同样写 `X_r`，忠实保留原页，不擅自改成 `X_i`。
- 备注：印刷运行页眉与页码 138 未录入 Markdown，属导航元素省略。
- 结论：定理编号误录列为 FAIL；条件 (b) 的 X_r 保留并列入源级 quirk。

### PDF p.032 / 96（印刷 p.139）— FAIL

- 时间：2026-10-02 01:35 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.032 文本层、页图 `audit/Hironaka_1964_resolution_partI_p032.png`（pngmono 150dpi）与 MinerU Markdown 第 515–519 行。proper rational application 的图像投影条件、domain of definition、复合条件及 elimination-of-indeterminacy 问题均相符；但 Markdown 第 517 行写作 `these exists a unique morphism`，印刷为 `there exists a unique morphism`，是可见正文转录错误，待全文审完后手工修复。
- 备注：印刷运行页眉与页码 139 未录入 Markdown，属导航元素省略。
- 结论：正文出现词汇误录，列为 FAIL。

### PDF p.033 / 96（印刷 p.140）— PASS±

- 时间：2026-10-02 01:39 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.033 文本层、页图 `audit/Hironaka_1964_resolution_partI_p033.png`（pngmono 150dpi）与 MinerU Markdown 第 515、517–535 行。Question (E) 的三项条件、proper rational application 与 graph projection 说明、trivialization 段落及脚注 22 对应印刷页；图像确认文本层显示的 `propar` 是提取失真，印刷实际拼作 `proper`，Markdown 保留正确印字。
- 备注：印刷运行页眉和页码 140 未录入 Markdown，属导航元素省略。
- 结论：未发现 Markdown 内容差异；因运行页眉/页码省略记为 PASS±。

### PDF p.034 / 96（印刷 p.141）— FAIL

- 时间：2026-10-02 01:46 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.034 文本层、页图 `audit/Hironaka_1964_resolution_partI_p034.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p034_ideal_indices.png`、`audit/300dpi/Hironaka_1964_resolution_partI_p034_normal_crossings.png` 与 MinerU Markdown 第 539、545 行。性质 (*) 原文条件中残余理想的点 index 写为 `J'_{i,x}=O_{X',x}`；Markdown 写成 `J_{ix}'`，丢失 i 与 x 之间的逗号。normal-crossings 定义里的 `O_{x,x}` 参数环与原页相符。
- 备注：印刷运行页眉和页码 141 未录入 Markdown，属导航元素省略。
- 结论：局部理想 index 分隔符误录，列为 FAIL；待全篇审计完成后逐处修复。

### PDF p.035 / 96（印刷 p.142）— FAIL

- 时间：2026-10-02 01:56 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.035 文本层、页图 `audit/Hironaka_1964_resolution_partI_p035.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p035_J_index.png` 与 MinerU Markdown 第 553–567 行。Main theorem II 条件 (ii) 印刷为 `\nu(J_{i,x(i)})`；Markdown 第 561 行写作 `\nu(J_{ix(i)})`，丢失 sheaf index i 与 point x(i) 之间的逗号，裁片确认该分隔符。
- 备注：印刷运行页眉和页码 142 未录入 Markdown；其余 weak-transform 与 E_{i+1} 公式相符。
- 结论：局部 sheaf-index 结构误录，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.036 / 96（印刷 p.143）— FAIL

- 时间：2026-10-02 02:02 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.036 文本层、页图 `audit/Hironaka_1964_resolution_partI_p036.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p036_transform_indices.png` 与 MinerU Markdown 第 561、575、577 行。Main theorem II 条件 (iv) 印刷为 `\nu(J_{r,y})<d`，Markdown 第 575 行写成 `\nu(J_{ry})<d`；由 (ii) 推出的 `\nu(J_{i,x(i)})=d` 在第 577 行也丢失 i 与点 x(i) 间的逗号。300dpi 裁片核准这两个索引分隔符。
- 备注：B* 比较方向、e≥1 与两项 corollary 条件相符；印刷运行页眉和页码 143 未录入 Markdown。
- 结论：两个局部 sheaf/stalk index 逗号缺失，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.037 / 96（印刷 p.144）— FAIL

- 时间：2026-10-02 02:11 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.037 文本层、页图 `audit/Hironaka_1964_resolution_partI_p037.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p037_ideal_index.png` 与 MinerU Markdown 第 589–599 行。印刷 T/S 集合定义在条件项中使用 local ring `O_{X,x}`；Markdown 第 589 行写为 `O_X_x`，第 591 行写为 `O_{x,x}`，均未保留大写空间下标 X 与点 x 的逗号/区分。裁片核实了上下文中两者是不同 index。
- 备注：Corollary 1 的闭子集构造及函数域对的 (1)/(2) 叙述其余部分与原页相符；印刷运行页眉和页码 144 未录入 Markdown。
- 结论：局部环下标误录，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.038 / 96（印刷 p.145）— FAIL

- 时间：2026-10-02 02:17 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.038 文本层、页图 `audit/Hironaka_1964_resolution_partI_p038.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p038_sheaf_indices.png` 与 MinerU Markdown 第 595–609 行。印刷第 601 行引用 `main theorem I`，Markdown 写作 `main theorem 1`；Corollary 2 证明第 607 行印作 `O_x`-modules，Markdown 写为 `O_X`-modules。300dpi 裁片确认此处是小写 x。其余 direct-image 和 quotient-sheaf 语句与原页对应。
- 备注：印刷运行页眉与页码 145 未录入 Markdown，属导航元素省略。
- 结论：定理编号和结构层下标各有误录，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.039 / 96（印刷 p.146）— PASS±

- 时间：2026-10-02 02:21 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.039 文本层、页图 `audit/Hironaka_1964_resolution_partI_p039.png`（pngmono 150dpi）与 MinerU Markdown 第 609–630 行。Corollary 3 的复合中心、约化总变换和法向交叉条件，以及 Zariski space 的定义/两条相容性质与原页对应；页图核验了文本层丢失的上划线和函子符号。
- 源级 print quirk：Corollary 3 后的段落写“assumption of Corollary 2”；Markdown 保留该交叉引用，不按上一段推改为 Corollary 3。
- 备注：印刷运行页眉和页码 146 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现 Markdown 内容差异；记录印刷交叉引用 quirk，并因页眉/页码省略记为 PASS±。

### PDF p.040 / 96（印刷 p.147）— FAIL

- 时间：2026-10-02 02:28 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.040 文本层、页图 `audit/Hironaka_1964_resolution_partI_p040.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p040_zariski_space.png` 与 `audit/300dpi/Hironaka_1964_resolution_partI_p040_zariski_restriction.png`，以及 MinerU Markdown 第 641–665 行。原页反复以花体 Zariski-space 记号 `\mathfrak{Z}` 书写 `\mathfrak{Z}(X)`、`\mathfrak{Z}(g)` 等；Markdown 多处转成数字 `3`（例如第 643、659、661、663、665 行），改变了专名对象的记号。
- 备注：印刷运行页眉和页码 147 未录入 Markdown，属导航元素省略。
- 结论：Zariski-space 标识符误录为数字，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.041 / 96（印刷 p.148）— FAIL

- 时间：2026-10-02 02:34 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.041 文本层、页图 `audit/Hironaka_1964_resolution_partI_p041.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p041_zariski_symbol.png` 与 MinerU Markdown 第 647–663 行。原页 Theorem / Question (F) 使用花体 Zariski-space 标识 `\mathfrak{Z}`，Markdown 第 659、661、663 行及后续关联式将其写成数字 `3`，包括 `\mathfrak{Z}(X_1)`、`\mathfrak{Z}(X_2)`、`h_i:\mathfrak{Z}\to X_i`。`dim(X)\leq 3` 的边界与原页相符。
- 备注：印刷运行页眉和页码 148 未录入 Markdown，属导航元素省略。
- 结论：Zariski-space 标识符误录为数字，列为 FAIL；待全篇审计结束后逐处手工修复。

### PDF p.042 / 96（印刷 p.149）— FAIL

- 时间：2026-10-02 02:41 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.042 文本层、页图 `audit/Hironaka_1964_resolution_partI_p042.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p042_zariski_questions.png` 与 MinerU Markdown 第 659–677 行。Question (F) 和后续定理里的 Zariski space 印刷为花体 `\mathfrak{Z}`，Markdown 相应多处写成数字 `3`，包括全局空间、`h_i` 的定义域及定理假设中的对象；维数关系 `\dim(X_1)=\dim(X_2)\geq 3` 与问题 (F′) 复合映射其余部分相符。
- 备注：印刷运行页眉和页码 149 未录入 Markdown，属导航元素省略。
- 结论：Zariski-space 标识符误录为数字，列为 FAIL。

### PDF p.043 / 96（印刷 p.150）— FAIL

- 时间：2026-10-02 02:46 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.043 文本层、页图 `audit/Hironaka_1964_resolution_partI_p043.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p043_zariski_space.png` 与 MinerU Markdown 第 681–693 行。Question (F) 结尾和 Theorem (a) 中 canonical map 的定义域在印刷中是花体 Zariski-space 符号 `\mathfrak{Z}`；Markdown 第 681、687 行写成数字 `3`，复用 p.40–42 的系统性符号误录。维数界、归一化/monoidal transformation 序列和 compact-window 结论均相符。
- 备注：印刷运行页眉与页码 150 未录入 Markdown，属导航元素省略。
- 结论：Zariski-space 标识符误录为数字，列为 FAIL；待全篇审计结束后统一逐处修复。

### PDF p.044 / 96（印刷 p.151）— PASS±

- 时间：2026-10-02 02:50 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.044 文本层、页图 `audit/Hironaka_1964_resolution_partI_p044.png`（pngmono 150dpi）与 MinerU Markdown 第 697–709 行。维数 2/3 对比、analytic C-space 覆盖范围、局部环类 `\mathcal B`、Strong Theorem I 与 Theorem I′ 起始陈述均与原页相符。
- 备注：印刷运行页眉和页码 151 未录入 Markdown，属导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.045 / 96（印刷 p.152）— FAIL

- 时间：2026-10-02 02:56 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.045 文本层、页图 `audit/Hironaka_1964_resolution_partI_p045.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p045_theorem_II_prime.png` 与 MinerU Markdown 第 709–735 行。印刷 Main theorem II′ 引用的是 `main theorem I′`，Markdown 第 721 行写作 `main theorem 1′`；条件 (ii) 印刷为 `\nu(I_{i,y})`，Markdown 第 725 行写成 `\nu(I_{iy})`，丢失 i/y 下标分隔逗号。其余弱变换和 (E_{i+1}) 条件相符。
- 备注：印刷运行页眉和页码 152 未录入 Markdown，属导航元素省略。
- 结论：定理标号及局部 ideal index 有两处误录，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.046 / 96（印刷 p.153）— PASS±

- 时间：2026-10-02 03:02 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.046 文本层、页图 `audit/Hironaka_1964_resolution_partI_p046.png`（pngmono 150dpi）与 MinerU Markdown 第 737–767 行。Local Chow lemma 两项、Corollary 1 的四项、higher-direct-image vanishing 与 Corollary 3 起始句的映射/下标方向均对照原页一致。
- 备注：印刷运行页眉和页码 153 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.047 / 96（印刷 p.154）— PASS±

- 时间：2026-10-02 03:06 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.047 文本层、页图 `audit/Hironaka_1964_resolution_partI_p047.png`（pngmono 150dpi）与 MinerU Markdown 第 769–777 行。Corollary 3 的局部拼接构造、投影映射、应用 Theorem I′、及关于 I′/II′ 推广的说明均与印刷页相符；图像核对了文本层丢失的帽记、限制符号和映射箭头。
- 备注：印刷运行页眉和页码 154 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.048 / 96（印刷 p.155）— FAIL

- 时间：2026-10-02 03:13 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.048 文本层、页图 `audit/Hironaka_1964_resolution_partI_p048.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p048_theorem_names.png` 与 MinerU Markdown 第 777 行。印刷写作 `I′(n)`、`II′(N)`，并分别称为主定理 `I(n)`、`II(N)`；Markdown 第 777 行把 I 写成花体 `\mathfrak{I}`，又把 II 写成希腊大写 Pi `\Pi`，均改变定理标识。
- 备注：印刷运行页眉和页码 155 未录入 Markdown，属导航元素省略。
- 结论：主定理符号 I/II 被转录为其他字形，列为 FAIL；待全文审计后逐处手工修复。

### PDF p.049 / 96（印刷 p.156）— FAIL

- 时间：2026-10-02 03:22 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.049 文本层、页图 `audit/Hironaka_1964_resolution_partI_p049.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p049_theorem_IIprime_indices.png` 与 `audit/300dpi/Hironaka_1964_resolution_partI_p049_local_rings.png`，并比对 MinerU Markdown 第 797–809 行。Main theorem II′ 的名称、well-ordered sequence 和局部环事实对应原页；但条件 (ii) 印刷写作 `\nu(J_{\lambda,y})`，Markdown 第 801 行为 `\nu(J_{\lambda y})`，遗漏 index λ 与点 y 之间的逗号。
- 备注：印刷运行页眉和页码 156 未录入 Markdown，属导航元素省略。
- 结论：局部理想下标分隔符误录，列为 FAIL；待全篇审计结束后逐处修复。

### PDF p.050 / 96（印刷 p.157）— PASS±

- 时间：2026-10-02 03:27 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.050 文本层、页图 `audit/Hironaka_1964_resolution_partI_p050.png`（pngmono 150dpi）与 MinerU Markdown 第 811–815 行。`n' ≤ n` 的界、Theorem I′(n) 归纳链、基础变换诱导的闭子空间和临时重变换过程与原页对应；图像确认文本层压平的帽记和不等号。
- 备注：印刷运行页眉和页码 157 未录入 Markdown，属非误导性导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.051 / 96（印刷 p.158）— FAIL

- 时间：2026-10-02 03:36 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.051 文本层、页图 `audit/Hironaka_1964_resolution_partI_p051.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p051_theorem_II_notation.png` 与 MinerU Markdown 第 815–825 行。印刷将第二主定理记为罗马数字 `II′(N)`/`II(N)`；Markdown 第 817 行将同段的 `II′(N)` 和两处 `II(N)` 都录为希腊字母 `\Pi`，第 819 行再次将 `II′(N)` 录为 `\Pi′(N)`。另印刷第 158 页 `\Gamma(X, O_X)` 与 `X=(X,O_X)` 的 sheaf 符号均为大写下标 `X`，Markdown 第 821 行两处均写作 `O_x`。相邻定理 I′/II″ 标识、基础定理 `I_2^{N,n}`、解析类比 `III(N,n)`、态射与变换链的其余对应文本已对照页图。
- 备注：印刷运行页眉和页码 158 未录入 Markdown，属导航元素省略。
- 结论：主定理 II/II′ 被误录为 Pi/Π，且结构层符号 `O_X` 的下标大小写错误，列为 FAIL；待全篇审计结束后逐处手工修复。

### PDF p.052 / 96（印刷 p.159）— FAIL

- 时间：2026-10-02 03:41 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.052 文本层、页图 `audit/Hironaka_1964_resolution_partI_p052.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p052_theorem_IIprime.png` 与 `audit/300dpi/Hironaka_1964_resolution_partI_p052_Zariski_notation.png`，并比对 MinerU Markdown 第 827、829–837 行。页首印刷写作 `II′(N)`，Markdown 第 827 行误录为希腊字母 `\Pi′(N)`。本页关于解析情形的限制、维数界、Question (M)、Zariski 空间及其规范态射、下标 0 和脚注 27 的正文均与印刷页对应；300dpi 裁片确认字体化 Z 及其下标，Markdown 对应使用 `\mathfrak{Z}`/`\mathfrak{Z}_0`。
- 备注：印刷运行页眉和页码 159 未录入 Markdown，属导航元素省略。
- 结论：定理 II′ 标识误录为 Pi′，列为 FAIL；待全篇审计结束后逐处手工修复。

### PDF p.053 / 96（印刷 p.160）— FAIL

- 时间：2026-10-02 03:45 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.053 文本层、页图 `audit/Hironaka_1964_resolution_partI_p053.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p053_IIprime_and_note28.png`、`audit/300dpi/Hironaka_1964_resolution_partI_p053_G_and_footnote.png` 与 MinerU Markdown 第 839、845 行。印刷称 `main theorem II′(3)`，Markdown 第 839 行误录为 `\Pi′(3)`；并且印刷在 `n=dim(X)` 后有脚注标记 28，Markdown 第 839 行漏掉该锚点，虽然脚注 28 的正文保留在第 845 行。图像还确认印刷写作 `g: X_i \to X`（此处确为小写下标 i），以及例中关于 $X_i$、$h_1$、$h_2$、变换序列、维数界与局部图的其余记号/叙述均与 Markdown 对应。
- 备注：印刷运行页眉和页码 160 未录入 Markdown，属导航元素省略。
- 结论：主定理 II′ 标识误录为 Pi′，且正文遗漏脚注 28 锚点（脚注本身仍在）；列为 FAIL，待全篇审计后逐处手工修复。

### PDF p.054 / 96（印刷 p.161）— FAIL

- 时间：2026-10-02 03:48 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.054 文本层、页图 `audit/Hironaka_1964_resolution_partI_p054.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p054_footnote_numbers_and_Inst.png` 与 MinerU Markdown 第 847、849–873 行。印刷脚注 30 的正文在 Markdown 第 871 行误标为 `^{80}`；同一注释中的期刊出版机构缩写印刷为 `de l'Inst.`，Markdown 第 871 行将小写字母 `l` 录成数字 `1`。正文条件 (i)–(iii)、性质 (a)–(c) 与脚注 29、31 的内容相符；另印刷在 Markdown 第 849、859 行写作花体 `\mathcal{B}` 的 class 名称为普通 `B`，而同页的 membership 公式仍保留花体，属于不改变指代的正/花体混排（PASS±）。
- 备注：Markdown 第 845 行的脚注 28 正文属于上一印刷页 p.160 的页脚，不计作本页内容；本页印刷运行页眉和页码 161 未录入 Markdown，属导航元素省略。
- 结论：脚注 30 号误录为 80，刊名缩写小写 `l` 误录为数字 `1`，列为 FAIL；待全篇审计后逐处手工修复。

### PDF p.055 / 96（印刷 p.162）— PASS±

- 时间：2026-10-02 03:51 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.055 文本层、页图 `audit/Hironaka_1964_resolution_partI_p055.png`（pngmono 150dpi）与 MinerU Markdown 第 875、877、879、881 行。关于代数 scheme 的定义和结构态射、local-ring class B 在代数/解析几何中的范围、选择较小 B 类的说明及脚注 32 均对应印刷页。印刷多处以花体 `\mathcal{B}` 表示已定义的 class，Markdown 第 875、877、879 行使用普通 `B`；上下文中的 class 指代明确，属不改变意义的正/花体混排（PASS±）。
- 备注：印刷运行页眉和页码 162 未录入 Markdown，属导航元素省略。
- 结论：未发现正文内容差异；class B 的字体样式混排及运行页眉/页码省略记为 PASS±。

### PDF p.056 / 96（印刷 p.163）— PASS±

- 时间：2026-10-02 03:52 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.056 文本层、页图 `audit/Hironaka_1964_resolution_partI_p056.png`（pngmono 150dpi）与 MinerU Markdown 第 883、885–887 行。scheme、simple/multiple/singular、singular locus、结构层与 stalk、维数和空子概形余维约定，以及“Resolution data and permissible transformations”节首均与印刷页对应。
- 备注：印刷运行页眉和页码 163 未录入 Markdown，属导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.057 / 96（印刷 p.164）— PASS±

- 时间：2026-10-02 03:54 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.057 文本层、页图 `audit/Hironaka_1964_resolution_partI_p057.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p057_data_types.png` 与 `audit/300dpi/Hironaka_1964_resolution_partI_p057_definition3_formulas.png`，及 MinerU Markdown 第 887–917 行。四种 resolution data 标识与 (F)/(U) 配对、Definition 3 的 `\mathfrak{R}_{\mathrm{I}}^{N,n}` 数据形式及条件 (i)–(iv)、`\mathfrak{R}_{\mathrm{II}}^N` 矩阵数据形式，连同 permissible transformation 术语说明均与原页相符。
- 备注：印刷运行页眉和页码 164 未录入 Markdown，属导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。

### PDF p.058 / 96（印刷 p.165）— FAIL

- 时间：2026-10-02 03:58 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.058 文本层、页图 `audit/Hironaka_1964_resolution_partI_p058.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p058_definition4_symbols.png` 与 `audit/300dpi/Hironaka_1964_resolution_partI_p058_resolution_sets.png`，并比对 MinerU Markdown 第 919–969 行。Definition 4(I) 印刷写作 `\mathfrak{R}_{\mathrm{I}}^{N,n}`，Markdown 第 933 行将罗马大写 I 误录成数字 1（`\mathfrak{R}_1^{N,n}`）。其余 Definition 3(II) 的参数/normal-crossings 条件、`\nu_{\mathbf M}(\mathbf J)` 与 `M^\nu \supseteq J`、Definition 4 的 resolved 条件和解析度集 $S,\nu,S_\nu,S_*$ 对应印刷页。另 Definition 4(II) 的数据符号在印刷中为花体 `\mathfrak{R}_{\mathrm{II}}^N`，Markdown 第 941 行写普通 `R_{II}^N`，属于不改变上下文指代的正/花体混排（PASS±）。
- 备注：印刷运行页眉和页码 165 未录入 Markdown，属导航元素省略。
- 结论：Definition 4(I) 的 datum 类型标签将罗马 I 误录为数字 1，列为 FAIL；待全篇审计后逐处手工修复。

### PDF p.059 / 96（印刷 p.166）— PASS±

- 时间：2026-10-02 03:59 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.059 文本层、页图 `audit/Hironaka_1964_resolution_partI_p059.png`（pngmono 150dpi）与 MinerU Markdown 第 969–1009 行。Definition 5 中 (I.1)、(I.2)、(II.1) 三种带 restriction 的 datum、闭/开 restriction 条件及四类 datum 的归纳角色说明，与单项变换的 universal mapping property、`\operatorname{Proj}(S(I))` 及直和 `\sum_{m=0}^{\infty} I^m` 构造、脚注 33 均对应印刷页。正文叙述处 Markdown 第 977、989、997 行将印刷的 `\mathfrak{R}` 写作普通 `R`；上下文中的 datum 指代明确，属不改变意义的正/花体混排（PASS±）。
- 备注：印刷运行页眉和页码 166 未录入 Markdown，属导航元素省略。
- 结论：未发现正文内容差异；datum 标识的字体混排及运行页眉/页码省略记为 PASS±。

### PDF p.060 / 96（印刷 p.167）— PASS±

- 时间：2026-10-02 04:01 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.060 文本层、页图 `audit/Hironaka_1964_resolution_partI_p060.png`（pngmono 150dpi）与 MinerU Markdown 第 1011–1033 行。嵌入概形的 strict transform 图、strict-transform 定义、中心与变换的配对约定、Definition 6 的 permissible 数据条件及脚注 34 均对应印刷页。Definition 6 的叙述行 1025 在印刷中使用 `\mathfrak{R}_{\mathrm{I}}^{N,n}`/`\mathfrak{R}_{\mathrm{II}}^N`，Markdown 使用普通 `R`；紧邻的数学式仍使用花体标识，属不改变指代的正/花体混排（PASS±）。
- 备注：印刷定义 strict transform 时先写 `X' - g^{-1}(B)`，后在括号中写 `X' - f^{-1}(B)`；Markdown 原样保留此印刷用法。运行页眉和页码 167 未录入 Markdown。
- 结论：未发现正文内容差异；datum 标识字体混排及运行页眉/页码省略记为 PASS±。

### PDF p.061 / 96（印刷 p.168）— FAIL

- 时间：2026-10-02 04:04 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.061 文本层、页图 `audit/Hironaka_1964_resolution_partI_p061.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p061_definition7_formulas.png` 与 MinerU Markdown 第 1035–1091 行。Definition 6 restrictions、Definition 7 的 datum 变换、矩阵中新增系数、`a_{\alpha+1}=(\sum_{B\subseteq E_i}a_i)+\nu-b` 及脚注 35 正文均与印刷页相符。但 Markdown 第 1081–1089 行在完整脚注 35（第 1091 行）之外另含 5 个脚注式碎片：独立的 `f:X'\to X`、`X'`、`X' (or, by f)` 与 `f^{-1}(B)` 等；这些片段在印刷页无对应独立内容，是脚注 35 的重复/截片伪影。
- 备注：正文在印刷页末以断词 `permis-` 续至下一页，Markdown 同样在第 1079 行保留断词；页脚 35 的完整内容仍在第 1091 行。印刷运行页眉和页码 168 未录入 Markdown。
- 结论：MinerU Markdown 多出 5 条脚注式变量碎片，列为 FAIL；待全篇审计结束后以 Edit 逐处清理，保留完整脚注 35。

### PDF p.062 / 96（印刷 p.169）— FAIL

- 时间：2026-10-02 04:07 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.062 文本层、页图 `audit/Hironaka_1964_resolution_partI_p062.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p062_type_I_labels.png` 与 `audit/300dpi/Hironaka_1964_resolution_partI_p062_parameters_and_Definition8.png`，并比对 MinerU Markdown 第 1093–1115 行。印刷在 Remark 1 连续 4 次写作 datum 类型 `\mathfrak{R}_{\mathrm{I}}^{N,n}`（其中末次为 `\mathfrak{R}_{\mathrm{I}}^{N,n'}`）；Markdown 第 1093 行 4 处均将罗马大写 I 误录成数字 1。其余维数与变换后 datum 论述、normal-crossings 参数证明，以及 Definition 8 的 permissible succession 定义和条件 (i)–(iii) 均与原页相符。
- 备注：印刷运行页眉和页码 169 未录入 Markdown，属导航元素省略。
- 结论：四处 datum 类型标签把罗马 I 误录为数字 1，列为 FAIL；待全篇审计后逐处手工修复。

### PDF p.063 / 96（印刷 p.170）— FAIL

- 时间：2026-10-02 04:10 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.063 文本层、页图 `audit/Hironaka_1964_resolution_partI_p063.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p063_theorem_labels.png` 与 `audit/300dpi/Hironaka_1964_resolution_partI_p063_theorem_II2_label.png`，并比对 MinerU Markdown 第 1117–1129 行。印刷的 resolution-datum 类型 `\mathfrak{R}_{\mathrm{I}}^{N,n}` 在第 1123、1125 行的定理 I₁/I₂陈述中共 9 处被 Markdown 误录为 `\mathfrak{R}_1^{N,n}`。另印刷的主定理标签为 `II_1^N`、`II_2^N`，Markdown 第 1127、1129 行分别录为希腊字母 `\Pi_1^N`、`\Pi_2^N`。section heading 中 I₁/I₂/II₁/II₂编号、维数范围、定理陈述及因子化约定的其余部分已对照原页。
- 备注：引言叙述中 Markdown 第 1121 行用普通 `R` 表示印刷的 Fraktur datum label，属不改变指代的正/花体混排（PASS±）；印刷运行页眉和页码 170 未录入 Markdown。
- 结论：9 处 datum 标签把罗马 I 误录为数字 1，另有 2 个主定理 II 标签误录为 Pi，列为 FAIL；待全篇审计后逐处手工修复。
