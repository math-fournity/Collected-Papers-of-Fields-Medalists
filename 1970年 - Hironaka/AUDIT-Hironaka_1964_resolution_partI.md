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
- 证据：源 PDF p.010 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p010.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p010_topology_not_supset.png` 与 MinerU Markdown 第 227–231 行。裁片确认 Zariski 拓扑定义中的原文条件为 `P ⊅ I`（素理想 P 不包含理想 I），Markdown 写成 `P \not\cong I`，关系符含义错误。该页还把层 `O_X`、`O_Y` 与 `O_S` 的下标大小写混写为小写 x/y/s，并把点处局部环 `O_{X,x}` 写成 `O_X`；此处 subscript 区分结构层和 stalk，属数学对象记号错误。印刷使用花体 `\mathcal{R}` 表示 local-ringed spaces 类别，Markdown 多处仅为普通 `R`。
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
- 证据：源 PDF p.013 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p013.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p013_complexification_symbols.png` 与 MinerU Markdown 第 253–267 行。印刷定义中结构层为 `O_X`，条件 (i) 也写作 `O_X|U`，实空间复化为 `O_X \otimes_R C`；Markdown 相应位置写成 `O_x`（第 253、255、261 行），把大写空间标识 X 改成小写点名 x，造成对象/点记号混淆。余下的 Hausdorff、协调、复化映射与同构条件和脚注 7 相符。
- 备注：印刷运行页眉和页码 120 未录入 Markdown，属不影响正文的导航元素省略。
- 结论：结构层下标误录会改变符号所指，列为 FAIL；全篇初审完成后逐处手工修复。

### PDF p.014 / 96（印刷 p.121）— FAIL

- 时间：2026-10-01 16:45 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.014 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p014.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p014_sheaf_and_stalk.png` 与 MinerU Markdown 第 273、275 行。原页定义 `X=(X,O_X)`，并把点 x 处局部环写为 `O_{X,x}`；Markdown 写为 `X=(X,O_x)` 与 `O_{x,x}`，把空间标识 X 改成了点变量 x。第 275 行再次将结构层写为 `O_x`，应与原页的 `O_X` 对应。300dpi 裁片可辨大写空间下标与后接的点下标。
- 备注：页内关于简单/多重点、解析坐标、复化及脚注 8–11 的其余内容与原页相符；印刷运行页眉、页码 121 未录入 Markdown。
- 结论：结构层与 stalk 的数学记号不一致，列为 FAIL，待全篇审计结束后逐处修复。

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

### PDF p.017 / 96（印刷 p.124）— PASS±

- 时间：2026-10-01 17:45 EDT；actor=Peer-P38；model=gpt-6-luna；effort=max。
- 证据：源 PDF p.017 文本层、入库页图 `audit/Hironaka_1964_resolution_partI_p017.png`（pngmono 150dpi）、300dpi 裁片 `audit/300dpi/Hironaka_1964_resolution_partI_p017_proj_and_stalks.png` 与 MinerU Markdown 第 309–319 行。对称张量代数、Proj 构造、齐次理想条件、degree-0/1 结构、态射及脚注 13–14 均对应原页；裁片也确认印刷结构层记号 `O_x` / `O_{x'}` 与 Markdown 逐字一致，不能仅凭常用大写记法改写。
- 备注：印刷运行页眉和页码 124 未录入 Markdown，属不影响正文的导航元素省略。
- 结论：未发现正文差异；因运行页眉/页码省略记为 PASS±。
