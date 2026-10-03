# AUDIT-ICM2022_proceedings_Duminil-Copin.redo — Luna 审计重做

- 性质：**Luna 审计重做**。用户 2026-10-02 判定 Luna（Peer-P14, gpt-6-luna）对本篇的审计不可信，本次逐页对照 PDF 原页全量重检，Luna 旧修复一并重核。印刷原文（PDF 原页）是唯一裁决源；Luna 旧审计（`AUDIT-ICM2022_Duminil-Copin.md`）只是被检对象之一，不作证据。
- 本块范围：p.1 – p.9（PDF p.1–9 / 印刷 p.1–9，46 页中的前 9 页）。
- Actor：`Wf-R-P14`（重审员，单篇单 worker）。
- Host / model / effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置；模型在自身输出内的自报为 UNKNOWN，不据文本风格推断）。
- Source PDF：`2022年 - Duminil-Copin/ICM2022_proceedings_Duminil-Copin.pdf`（46 页，`pdfinfo` 实测 Pages: 46）。
- PDF SHA-256：`f4ff23ff0a69474a84260b2e949ee850eb42c202e12f5d42a3af20168932ded6`（本 worktree 实算，与派发给定一致）。
- MD 基线 SHA-256（重做开始前被检 Markdown）：`45dc4fbe37b30e01f57a7b288688b1803f4e97a8c9dad37102ae3a0f6a919898`（本 worktree 实算，含 Luna 修复后的当前态）。
- 文本层判定：`pdftotext` 首页提取成功且与版面逐行对应（born-digital，pdfTeX 产物）→ **文本层可用，双通道主对账**（pdftotext 全页文本 + 150dpi pngmono 页图互证；符号/图存疑处 300dpi 裁剪仲裁）。判定与返回字段一致。
- 证据图：`audit-redo/ICM2022_proceedings_Duminil-Copin_p0NN.png`（pngmono 150dpi，逐页渲染）；仲裁裁剪在 `audit-redo/300dpi/`。旧 `audit/` 不动、不复用。
- 纪律：print quirk 与印刷错字忠实保留登记，绝不按数学预期静默改正；看不清升级说明，不编造。本 worker 不写根级文件（`AUDIT-PROGRESS.log`/`AUDIT-INDEX.md` 由 Master 集成侧负责）；每页一提交，subject 格式 `redo(page): [Wf-R-P14 | zcode/GLM-5.3-Flash/max配置] ICM2022_proceedings_Duminil-Copin p.0NN/46 <等级>`。
- 开工时间：2026-10-03 12:02 EDT（`date` 实取）。

## 逐页审计

## p.001（PDF p.1 / 印刷封面页）
- PNG：audit-redo/ICM2022_proceedings_Duminil-Copin_p001.png（pngmono 150dpi）；仲裁裁剪 audit-redo/300dpi/ICM2022_proceedings_Duminil-Copin_p001_footer_300dpi.png（页脚 DOI 区）
- 核对：题录（标题/作者/ dedication/摘要/MSC 2020/Keywords/页脚版权与 DOI）
- 结果：**PASS±**
  - MD 第 1–19 行与印刷页逐项吻合：标题、作者、dedication（`Dmitry Ioffe` 拼写正确——Luna 旧审计称其修复过 `Iofe`，当前态正确）、摘要全文、MSC `Primary 82B20; Secondary 60K35`、Keywords、页脚 `© 2022 International Mathematical Union`、`Preliminary version, to appear in Proc. Int. Cong. Math. 2022, Vol. 1.`、`DOI 10.4171/ICM2022/204`（300dpi 仲裁确认印刷即为 `ICM2022/204`，斜杠+204，非连字符）。
  - 差异（不误导）：页脚左下 ICM 会徽内的文字 "INTERNATIONAL CONGRESS OF MATHEMATICIANS 2022 JULY 6–14" 未入 MD——属图形徽标文字，非正文内容，不影响检索与语义。
- 备注：Luna 旧审计将 p.001 判 FAIL（称 MD 缺页脚/DOI、`Iofe` 拼写错）。当前 MD 基线已含页脚与 DOI、Ioffe 拼写正确，旧修复结果与 PDF 一致；本次无新修复。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：audit-redo/ICM2022_proceedings_Duminil-Copin_p002.png（pngmono 150dpi）
- 核对：§1 全部三段（含 breakthroughs 列举与引用 [20, 86]/[48]）、§2 与 §2.1 节标题顺序、§2.1 Curie 段前半（至 "only when an external" 跨页断点）
- 结果：**PASS±**
  - 节标题顺序与编号（`1. Short motivation` → `2. The first twenty years: a laborious start` → `2.1. Ising model's prehistory`）与印刷一致；三段正文逐句吻合；`769.85 degrees Celsius`、引用 `[30]`、`[20, 86]`、`[48]` 数值一致。
  - `Kadanoff's`（MD 行 27）当前拼写与印刷一致——Luna 旧修复（`Kadanof's`→`Kadanoff's`）经原页重核**成立**。
  - 残留伪影（登记不改，SOP PASS± 默认）：MD 行 27 `diferent`、`diferential`——印刷与文本层均为 `different`、`differential`（ff 连字被拍平成单 f，OCR 伪影，非 print quirk）；`[20,86]` 印刷为 `[20, 86]`（空格合并）；印刷页脚 running foot `2 Hugo Duminil-Copin` 未入 MD。
- 备注：ff 拍平词会妨碍精确字符串检索，按 SOP 未批量修复；如后续统一批量处理须整篇登记。
