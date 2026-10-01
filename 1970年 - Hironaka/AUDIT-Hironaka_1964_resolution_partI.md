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
