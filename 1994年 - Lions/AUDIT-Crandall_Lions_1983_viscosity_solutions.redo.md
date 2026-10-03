# AUDIT（重做）— Crandall–Lions, "Viscosity Solutions of Hamilton-Jacobi Equations" (1983)

- 性质：Luna 审计重做。用户 2026-10-02 判定 Luna 审计不可信，本次逐页对照 PDF 全量重检，
  Luna 旧修复一并重核；印刷原文是唯一裁决源。
- actor：Wf-R-P08
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置，自报 UNKNOWN）
- PDF SHA-256：e538a4ea97cf96d92e4771bb4e75e24419217c67e597eb7e6111b7a8b79ff8a2
- MD 基线 SHA-256（重做起点，含 Luna 旧修复）：52d668de4de28e2578a044b57be69678f12a373a280996aa4d459b98604cf8ce
- 旧审计（被检对象之一，不作裁决源）：`AUDIT-Crandall_Lions_1983_viscosity_solutions.md`（Peer-P08/Luna，
  集成于 111fa4beb）；其 MD 修复 diff 见该 commit。
- 证据图目录：`audit-redo/`（p0NN，pngmono 150dpi；不改动旧 `audit/`）。
- 开工时间：2026-10-03 12:04 EDT
- 页数：42（pdfinfo 直证）。

## 文本层判定（pdftotext 首页试验）

`pdftotext -f 1 -l 1` 输出可用但质量受限：散文大体可读（标题、作者、摘要、引言均可提取），
但存在字形错映与空格丢失，如 `VISCOSITYSOLUTIONS`、`= 0 inö,`（Ω 错映）、`u, + H(...)`（下标 t 拍平）。
**判定：文本层部分可用 → 双通道主对账**：pdftotext 仅作散文/题录辅助对账通道；一切数学字形、
上下标、记号与 print quirk 以 150dpi/300dpi 页图（PNG）为唯一裁决源。

## 分块范围

本块重检 p.1–p.9（PDF p.1–p.9）。其余页由其他重审员分块负责。

## p.001（PDF p.1 / 印刷 p.1）

- PNG：audit-redo/p001.png（pngmono 150dpi）
- 核对：题录（标题/作者/期刊卷期）、摘要全文、(0.1)(0.2)、Introduction 首段与第二段、页底四条脚注（收稿 1981-12-01、1980 MSC 35F20/35F25/35L60、Key words、Army/NSF 资助¹）
- 结果：**PASS±**。正文、题录、两条模型 (0.1)(0.2) 与四条脚注均与印刷页相符。Markdown 未收录页眉「TRANSACTIONS OF THE AMERICAN MATHEMATICAL SOCIETY / Volume 277, Number 1, May 1983」、页脚版权行（©1983 AMS、ISSN/价码行）与印刷页码 1（版面元数据遗漏，不误导正文）。正文 $\mathbf{R}^N$（印刷粗体）在本页多处录为普通 $R^{N}$（如 MD 行 21、35），与后文行 51 的 $\mathbf{R}^N$ 混用；属字体族转录差异，对象可辨，不作正文修复（全篇该差异统一登记于此）。
- 备注：pdftotext 对本页摘要有明显错映（`u, +`、`inö`），不作定字依据；MD 的 $u_t$、$\Omega$ 等以页图为准核实无误。「Cauchy problem HJ equations」（无 for）与印刷一致，照录。

## p.002（PDF p.2 / 印刷 p.2）

- PNG：audit-redo/p002.png（pngmono 150dpi）；仲裁裁片 300dpi：BUC(Ω),³ 行（/tmp 中转，结论已录本条）与页底脚注区
- 核对：开头续句（the equations almost everywhere + 文献列表 Douglis[10]/Kružkov[18,19,20]/Fleming[13,14,15]/Friedman[16]/Benton[4]/Lions[22]）、(0.1) 反例 u(x) 分段式、分段线性 u 例子、min/max 封闭性段、viscosity solutions² 段、special case 段与 (0.3) 全式、页底脚注 ²、³
- 结果：**PASS±**。正文与公式均与印刷页相符。重核 Luna 旧修复：删除独立片段 `$C_b(\Omega))$` ——300dpi 页底裁片证实印刷页只有 ²、³ 两条完整脚注，该删除**正确**，维持。新发现：MD 行 51 `n ∈ BUC(R^N), i.e.` 丢失印刷页行内上标 ³（印刷页 `BUC(R**N**),³ i.e.`，300dpi 裁片直证；行 49 的 ² 行内标记保留，此处属漏拍平）→ 本次修复：补回 `$^{3}$`。页眉作者行与印刷页码 2 未录入 Markdown（版面元数据遗漏）。
- 备注：修复 1 处（行内脚注 ³ 标记），以 p002.png 与 300dpi 裁片为据。

## p.003（PDF p.3 / 印刷 p.3）

- PNG：audit-redo/p003.png（pngmono 150dpi）
- 核对：Under these assumptions 列举 (i)–(v) 全文、"It is of interest here…" 段（含 u_t + Σf_i(u)_{x_i}=0、Hopf[17]/Vol'pert[26]/Kružkov[20]）、"Finally we recall…" 段（convex Hamiltonian、[8]）、"A few words about the presentation…" 段（阅读路线 §§I.1,I.2/Corollary I.6/§II.1/§IV/§§V.1,V.2）、"§I.5 deserves a special remark…" 段（Proposition I.19、[27]）、页末断句 "…convergence theorems"
- 结果：**PASS±**。全部正文与印刷页相符；页眉 running head（VISCOSITY SOLUTIONS OF HAMILTON-JACOBI EQUATIONS）与印刷页码 3 未录入 Markdown（版面元数据遗漏，不误导）。
- 备注：p.3 印刷页末句在 MD 行 79 断开，行 81 起为 p.4 内容，续接正确。
