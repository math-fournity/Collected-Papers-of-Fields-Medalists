# Bourgain · Pointwise ergodic theorems for arithmetic sets — Luna 审计重做

研究对象为 Jean Bourgain 1989 年论文（Publications mathématiques de l'I.H.É.S. 69 (1989), p. 5–41）的印刷 PDF 与 MinerU 派生 Markdown。本次审计判断 Markdown 是否忠实转录论文陈述、公式与编号，并一并重核此前 GPT-6 Luna（Peer-P04）审计所作修复的正确性。裁决源为 PDF 原页：150dpi pngmono 全页图 + pdftotext 文本层双通道对账，疑难位置另作高分辨率裁片。证据等级支持页面转录忠实度与旧修复正确性判断，不构成对定理或证明有效性的独立验证。

- 性质=Luna审计重做（用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- 日期时间起：2026-10-02 14:41:45 EDT
- PDF：`Bourgain_1989_pointwise_ergodic.pdf`，38 页；PDF SHA-256=`7890c91e6a54e8867a262430b90f6af7f14a2a3558ac78e5dd56c789c044a9ef`
- MD 基线 SHA-256=`ad3fe1901ab87c9f71944726a0fd32fa7eae5040223387d388c7935363d8a79e`（2,028 行；即 Luna 修复后基线）
- 页映射：PDF p.1 为 Numdam 题录/版权封面（无印刷页码），PDF p.2–38 对应印刷页 5–41。
- 文本层判定：`pdftotext -f 1 -l 1` 首页提取成功（Numdam 封面题录、版权条款完整可读）→ 文本层可用，采用「文本层主对账 + 150dpi PNG 逐页视觉核验」双通道；文本提取不能裁决的字形回看原页图（必要时高分辨率裁片）。
- 范围：本次运行块只覆盖 p.1–p.9（PDF 页序）；后续页由后续块继续。
- 证据图：`audit-redo/p0NN.png`（Ghostscript `pngmono`，150dpi）；不触碰旧 `audit/` 与旧 `AUDIT-Bourgain_1989_pointwise_ergodic.md`。
- 修复纪律：Markdown 内容错误用结构化 Edit 逐处修复（含纠正 Luna 旧修复中的错误），每处可溯源该页证据；印刷原文的错字与 quirk 忠实保留登记，绝不按数学预期静默改正；看不清的位置升级说明，不编造。

## 逐页记录（redo）

## p.001（PDF p.1 / Numdam 题录封面，无印刷页码）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p001.png`（Ghostscript `pngmono`，150dpi；原 PDF p.1）
- 核对：封面作者 Jean Bourgain、题名、期刊 *Publications mathématiques de l'I.H.É.S.*, tome 69 (1989), p. 5–41、Numdam 条目链接、版权/使用条款；文本层（`pdftotext -f 1 -l 1`）与 150dpi 原页图双通道，对 MinerU Markdown 第 1–11 行。
- 结果：PASS±。MD 开头逐项保留了作者、题名、刊卷年页码、`PMIHES_1989__69__5_0` 链接与全部版权/使用条款文字，与原页一致。原页另有版面件未入 MD：顶部横幅 “PUBLICATIONS MATHÉMATIQUES DE L'I.H.É.S.” 与底部 “Article numérisé dans le cadre du programme / Numérisation de documents anciens mathématiques / http://www.numdam.org/”（Numdam 制作署名）。均属档案封面版面件缺录，不影响论文题录或正文。链接行的尖括号在 MD 中录为 HTML 实体 `&lt;…&gt;`，渲染后与原页一致，登记不改。与 Luna 旧审（p.001 PASS±）结论一致；旧审未提顶部横幅缺录，本次补记。
- 时间：2026-10-02 14:41:45 EDT 落签

## p.002（PDF p.2 / 印刷 p.5 题名页；页面未印页码）
- actor=Wf-R-P04; host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（自报UNKNOWN）
- PNG：`audit-redo/p002.png`（Ghostscript `pngmono`，150dpi；原 PDF p.2）
- 核对：论文题名、作者、“With an appendix on return-time sequences” 及 joint 合作者 HARRY FURSTENBERG / YITZHAK KATZNELSON / DONALD S. ORNSTEIN；§1 首段与公式 (1.1)。文本层 + 150dpi 原页图双通道，对 Markdown 第 13–37 行。
- 结果：PASS。题名行、appendix 说明、三位合作者、§1 首段（$[B_1]$、$[B_2]$、$[B_3]$、$(\Omega,\mathcal{B},\mu,T)$、polynomial $p(x)$）及 (1.1) 的 $A_{\mathbf{N}}f=\frac{1}{N}\sum_{1\leqslant n\leqslant N}T^{p(n)}f$ 全部与原页一致；后续段落 $N\to\infty$、$L^2(\Omega,\mu)$、$L^p$-theory ($p<2$) 与 a)/b)/c) 三条方法概述亦吻合。文本层在专名与显示式处有 OCR/布局噪声（如 “BirkhofTs”、(1.1) 拍平），150dpi 原页已裁决，Markdown 无错项。与 Luna 旧审（p.002 PASS）结论一致，无修复。
- 时间：2026-10-02 14:47 EDT 落签
