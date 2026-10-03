# Birkar_2016_singularities_linear_systems — Luna审计重做：PDF/Markdown逐页对账（p.1–p.9 片段）

- 性质：Luna审计重做。用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核。印刷原文（PDF 原页）是唯一裁决源；旧 AUDIT（`AUDIT-Birkar_2016_singularities_linear_systems.md`）只是被检对象之一。
- actor：`Wf-R-P13`
- host / model / effort：`zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max`（run级配置；effort 为自报 UNKNOWN，非运行时实测）
- PDF：`Birkar_2016_singularities_linear_systems.pdf`，46 页；SHA-256 = `c9c73303be3b12c5ca91506ac541c9b9d81764d19bcd7183b7c577f8c0d546fe`
- Markdown 基线：`Birkar_2016_singularities_linear_systems_mineru/Birkar_2016_singularities_linear_systems__Birkar_2016_singularities_linear_systems.md`，重检起始 SHA-256 = `34c398ff3b9347d3d0ef166b1f744eef6d1936f9842a212b284529a03be38249`（即 Luna 修复后状态；本次重检以此基线对照 PDF，Luna 的修复作为被检内容一并重核）
- 重做开始时间：2026-10-03 12:09 EDT
- 文本层判定：`pdftotext -f 1 -l 1` 提取首页成功（题名/摘要/目录/脚注齐全，无乱码），p.1–p.9 合计 27,042 字节 → **文本层可用，采用双通道主对账**：每页 gs pngmono 150dpi PNG 目检（视觉终裁）+ pdftotext 文本层交叉对账。判定命令：`pdftotext -f 1 -l 1 "Birkar_2016_singularities_linear_systems.pdf" -`（exit 0）。
- 证据图：`audit-redo/p0NN.png`（Ghostscript `pngmono`，150dpi，1-bit，新建；旧 `audit/` 不动）。
- 分级与修复纪律：PASS / PASS± / FAIL 按 AUDIT-SOP；Markdown 内容错误用结构化 Edit 逐处修复（含修正 Luna 旧修复中的错误），每处可溯源该页证据；印刷原文的 print quirk 与错字忠实登记、绝不按数学预期静默改正；看不清升级说明，绝不编造。

---

## p.001（PDF p.1 / 印刷 p.1）
- PNG：`audit-redo/p001.png`（pngmono 150dpi；本次重做新渲染并目检整页）。
- 核对：题录（题名/作者/摘要）、目录条目与页码、脚注三行（Date/2010 MSC/Keywords）；与 Markdown 第 1–41 行逐项比对。
- 结果：**PASS±**
  - 题名、作者、摘要全文、目录全部条目（1/2/2.1/2.2/2.4/2.5/2.6/2.8/2.9/2.12/2.14/2.16/2.18/2.19/2.22/2.23/2.25/3/4/5/5.1/5.3/5.6/5.10/6 及页码 2,9,9,10,10,11,12,12,12,13,13,14,15,15,15,16,17,22,27,27,28,31,37,42）与印刷一致；目录缺号子节（2.3、2.7 等）与印刷原样一致，非遗漏。
  - 脚注：`Date: December 2, 2020.`、`2010 MSC: 14J45, 14E30, 14C20.`、`Keywords: … minimal model program.` 与印刷一致——Luna 旧修复「minimal mode program→minimal model program」经原页 PNG 复核为正确，保留。
  - PASS± 项（不修，登记）：①摘要 `different` 被拍平为 `diferent`（ff 连字瑕疵，词义可辨）；②MD 第 41 行脚注后有孤立 `References` 行——印刷原文该行是 p.2 顶部目录续项「References 44」（pdftotext p.2 证实），MinerU 把它错位到题录区且丢页码 44，属结构伪影，不影响数学内容，不批量改；③页边 arXiv 水印（arXiv:1609.05543v2 [math.AG] 1 Dec 2020）未收录，非论文内容，不计差异。
- 备注：Luna p.001 登记的两项差异（minimal model program、diferent）均属实；本次重检未发现其漏报本页其他内容差异。
- 记录时间：2026-10-03 12:12 EDT；actor=`Wf-R-P13`；model=`GLM-5.3-Flash`；effort=max（run级配置，自报UNKNOWN）。
