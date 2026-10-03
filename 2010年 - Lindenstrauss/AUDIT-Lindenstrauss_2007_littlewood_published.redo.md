# AUDIT-Lindenstrauss_2007_littlewood_published.redo — Luna 审计重做（p.1–p.9 块）

- 性质：**Luna审计重做**（用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核）
- actor：Wf-R-P16
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF SHA-256：`7f26dde3f9b206534584b2b94d4a86e6319e467918efca8b4d00b1b1ae574825`
- MD 基线 SHA-256（重做前 MinerU Markdown）：`e92b0d19bd406e72c798834ac2b52e0660d6be0d143a4cd06ed96e675f7c75f9`
- 日期时间：2026-10-03 12:15 EDT（开工）
- 文本层判定：`pdftotext -f 1 -l 1` 首页成功提取 2082 字节结构化正文（题录/摘要/引言完整可读）
  → **文本层可用，采用双通道主对账**（150dpi pngmono PNG 目检 + pdftotext 文本层互证）。
- 本块范围：p.1 至 p.9（全篇 48 页的 Redo 由多个块完成）。
- 证据图目录：`2010年 - Lindenstrauss/audit-redo/`（p0NN.png，pngmono 150dpi；不触碰旧 `audit/`）。
- 旧 Luna 审计文件 `AUDIT-Lindenstrauss_2007_littlewood_published.md` 只作被检对象，不作裁决源；
  唯一裁决源是印刷原文 PDF 原页。

---

## p.001（PDF p.1 / 印刷 p.513）

- PNG：audit-redo/p001.png（pngmono 150dpi）；题录区终裁另用 300dpi 原页裁片（/tmp 瞬时中转，结论已登记于此）。
- 核对：刊名/卷年/页范围、标题、作者、Abstract、§1/§1.1 节标题顺序、开篇三段文字与脚注。
- 结果：**PASS±**
- 差异列表：
  1. MD 缺印刷页眉运行头「Annals of Mathematics, **164** (2006), 513–560」（300dpi 裁片直证；MinerU
     系统性省略运行头，非内容误导，不改动 MD，事实登记于此）。
  2. 行内 LaTeX 紧排空格瑕疵（如 `on$\operatorname{SL}(k,\mathbb{R})/\operatorname{SL}(k,\mathbb{Z})$which`
     缺空格），排版级，不影响语义。
- 旧 Luna 修复重核：Luna p.001 声称修复摘要 `Hausdorf→Hausdorff`——当前 MD 第 7 行确为
  `has Hausdorff dimension zero`，与印刷字形（含 ﬀ 连字）一致，**该旧修复正确，予以确认**。
- 其余核对：标题/作者行（第 1、3 行）、Abstract（第 7 行）、§1.1 三段（第 11/13/15 行前半）与
  脚注（第 17 行：NSF DMS-007133、DMS-0140497、DMS-0434403、Clay、AIM、DMS-0222452）逐句与
  印刷页吻合。本页 MD 无需修改。

---
