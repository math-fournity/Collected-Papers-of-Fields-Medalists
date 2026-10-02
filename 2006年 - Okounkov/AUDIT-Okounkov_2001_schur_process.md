# AUDIT — Okounkov_2001_schur_process

> 论文：A. Okounkov, N. Reshetikhin, *Correlation function of Schur process with application to local geometry of a random 3-dimensional Young diagram*（arXiv:math/0107056v3，2003-01-31 版，35 页）。
> actor=Wf-P10；host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）。
> PDF SHA-256 = 83bd21a169bc03393390b95428324eec8a9511cefa1df7968bd48c4fa5bde4f1。
> MD 基线 SHA-256 = ad6a88a9e361adf0407b097ab68b5c4f158506460d0a4c245fc7b1ab623a846d。
> 审计开始：2026-10-02 13:39 EDT。
> 文本层判定：`pdftotext -f 1 -l 1` 首页输出完整可读 → **文本层可用**，全程采用「文本层主对账 + PNG 视觉核验」双通道。
> 分级与格式遵循 worktree 根 `AUDIT-SOP.md`「流程（每页 7 步）」「审计说明格式」「审计后修复」三节；本篇审计 p.1–p.35，本块覆盖 p.1–p.9。

---

## p.001（PDF p.1 / 印刷 p.1）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：题录（标题/作者/脚注邮箱）、Abstract 全文、§1、§1.1、§1.1.1 首句
- 结果：PASS。标题、作者 "Andrei Okounkov and Nikolai Reshetikhin∗"、Abstract 逐句、节标题顺序、§1.1.1 首句与脚注全部吻合。印刷原样 quirk 忠实保留于 md：错字 "weights a partitions λ"、邮箱 "reshetik@math.berkeley.edu"（印刷即如此，非 md 错）。
- 备注：mineru 把该页脚注排版为 docvortex-page-footnote 样式块，属导出格式非内容错误；相邻处 "where$s _ { \lambda }$" 缺空格为 mineru 排版级伪影，不妨碍阅读，不按 quirk 改。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：§1.1.1 续（Schur process 序列式与 Prob∝∏𝕊^(t) 式）、§1.1.2 全节、𝔖({λ(t)}) 定义式、行列式式 det(K(u_i,u_j))
- 结果：PASS±（两处 mineru 伪影已修复，见下）。正文与公式全部吻合：𝕊^(t)(λ(t),λ(t+1)) 无 ∏ 下标（印刷如此）、𝔖 定义式 t,i∈Z（斜体 Z，印刷如此）、U⊂ℤ×(ℤ+½) 黑体 Z 均与 md 一致。
- 修复：① md 行 19 `{<sup>λ(t)</sup>} <sup>such</sup> <sup>that</sup>` → `{λ(t)} such that`——p.002.png 显示 "such that" 为正常正文字号，非上标；② md 行 39 `$U \subset \mathbb { Z } \times ( \mathbb { Z } + { \frac { 1 } { 2 } } )$` 句末补印刷原页的句号。
- 备注：印刷 quirk 忠实保留不改：语法瑕疵 "This determinants can be also interpreted"、"Our main interest in this paper are"。
