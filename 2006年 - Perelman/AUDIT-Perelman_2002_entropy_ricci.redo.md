# AUDIT-Perelman_2002_entropy_ricci.redo（Luna 审计重做）

- 性质：Luna 审计重做。用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核。
- actor：Wf-R-P05
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF：2006年 - Perelman/Perelman_2002_entropy_ricci.pdf，SHA256 = 945e278613c45ea1ab617b28c3095783d0e68958dc0546dfcfa9b42b9674fbe1
- MD 基线：Perelman_2002_entropy_ricci__Perelman_2002_entropy_ricci.md，SHA256 = ccf3ba4849988c0e5b20e889195e473b8c1aeadde7ebd560f9e9b8df15026883（即含 Luna 修复 67ca87858 的当前态，全部按 PDF 重核）
- 裁决源：印刷原文 PDF；Luna 旧修复仅是被检对象。print quirk 与错字忠实登记，不按数学预期静默改正。
- 开始时间：2026-10-02 14:30 EDT
- 文本层判定：`pdftotext -f 1 -l 1` 首页提取正常（标题/作者/正文/脚注完整可读）→ **文本层可用，双通道主对账**（每页 PNG 视觉核对 + pdftotext 文本对账）。
- 页码对齐：arXiv math/0211159v1 单篇预印本，PDF 页码 = 印刷页码（39 页）。
- 证据：本目录 `audit-redo/p0NN.png`（pngmono 150dpi）；不动旧 `audit/`。

---

（页级条目按 AUDIT-SOP「审计说明格式」逐页追加于下）

## p.001（PDF p.1 / 印刷 p.1）
- PNG：audit-redo/p001.png（pngmono 150dpi）
- 核对：题录（标题/作者/日期行/arXiv 侧标）、Introduction 节标题、§1 段公式 d/dt g_ij(t)=−2R_ij、Rm_t=△Rm+Q、R_t=△R+2|Ric|²、引文 [H 1]/[H 1,H 2]、脚注全文
- 结果：PASS
- 备注：印刷日期行为 "November 26, 2024"（本 PDF 为 2024-11-26 重编译件，arXiv 侧标仍为 11 Nov 2002）——print quirk 忠实保留，MD 同文，不改。跨页断句（"positive curvature operator"→p.2 "in dimension four converge…"）在 MD 中合并为同段，文本逐字一致，属 MinerU 页流合并，非内容错误。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：audit-redo/p002.png（pngmono 150dpi）
- 核对： blow-up/ancient solution 段（[H 9]、(−∞,T)、[I]、[H 4]、[H 3]、[H 4,§26]）、surgery 段（[H 5]、$\tilde{Rm}(x,t)=tRm(x,t)$、$t\to\infty$、[H 6]）
- 结果：PASS
- 备注：印刷原样错字 "a priory"（应为 a priori）与 "a convergence theorem ," 逗号前空格均为 print quirk，MD 忠实保留未改。


