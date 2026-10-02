# AUDIT-REDO — Donaldson 1983, “An Application of Gauge Theory to Four-Dimensional Topology”

- 性质：**Luna 审计重做**。用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检；Luna 旧修复（`fix(md)` commit `9717b16`，修复后 md SHA `a22812e1…`）一并重核，不再默认其结论正确。
- Actor：`Wf-R-P03`（dynamic-workflow Sub Agent，单篇互斥 worktree `cpf-redo-Donaldson_1983_gauge_theory_4manifolds`，分支 `cpf-redo/Donaldson_1983_gauge_theory_4manifolds`）。
- Host / model / effort：`zcode` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`（run 级配置转述；实际生效 effort **自报 UNKNOWN**，无法从 runtime 直接证明）。
- PDF：`Donaldson_1983_gauge_theory_4manifolds.pdf`，38 页，SHA-256 `5a5201ed38b870ec1ad183b697aa505830c5a35bf03d72614a5bb1667fe65080`（本 worktree 实测）。
- 被检 Markdown 基线：`Donaldson_1983_gauge_theory_4manifolds_mineru/Donaldson_1983_gauge_theory_4manifolds__Donaldson_1983_gauge_theory_4manifolds.md`，1,449 行，SHA-256 `a22812e11e24ebbddde35767b454a47957949df592d97b72a689568b83eb74a5`（= Luna fix 后的基线；原始 mineru 产出见历史 commit `0b0f3dd`）。
- 开工时间：2026-10-02 14:33 EDT；本文头最后更新 2026-10-02 14:51 EDT。
- 文本层判定：`pdftotext -f 1 -l 1` 成功返回首页全文（exit 0；ABBYY FineReader OCR 层，2008 年生成）→ **文本层可用，本篇采用双通道主对账**：150dpi pngmono 页图为印刷原文裁决源，pdftotext 文本层仅作第二通道交叉定位/比对；文本层自身有 OCR quirk（如 `E₈`→`£ 8`、连字符丢失），一律以页图为准。
- 方法：每页 `gs -q -dNOPAUSE -dBATCH -sDEVICE=pngmono -r150` 渲染 `audit-redo/p0NN.png` → Read 目检 → 与 Markdown 对应段五点比对（题录 / 节标题顺序 / 定理编号与陈述 / 公式与上下标 / 记号；文末页逐条参考文献与收稿日期）→ PASS / PASS± / FAIL 分级 → 内容错误用结构化 `Edit` 逐处修复（含修正 Luna 旧修复中的错误；print quirk 忠实登记不改）→ 本文件落签该页条目 → 仅 add 本篇路径后按 `redo(page)` 提交。
- 纪律：PDF 原页为唯一裁决源；不写根级任何文件；不动旧 `audit/` 与旧 `AUDIT-Donaldson_1983_gauge_theory_4manifolds.md`（只读参照）；不碰其他论文目录；不 push。

## 页级条目

### p.001（PDF p.1 / 印刷 p.279，首页无单独页码数字）

- PNG：`audit-redo/p001.png`（pngmono 150dpi）；字形仲裁：300dpi 裁片（节标题、期刊行，临时中转，结论记于本条）
- 核对：题录（期刊卷期页码行、标题、作者、Received 脚注）；节标题 I.1；正文段落与 cup-square 公式；$E_8$；引用编号 [7][8][11][12][22]
- 结果：**PASS±**。
  - Luna 基线确实缺印刷期刊行 `J. DIFFERENTIAL GEOMETRY 18 (1983) 279–315`（grep 无 `DIFFERENTIAL`/`279` 命中）——**本次已用 Edit 在标题前补入该行**；题录五行余项（标题/作者/脚注日期）逐字吻合。
  - 节标题 300dpi 仲裁：印刷为罗马数字 `I.1 Introduction`（首字符为带衬线大写 I，非阿拉伯 1）；md `I.1` 正确，Luna 未动亦未改错。
  - cup-square 公式 $Q\colon H^2(X;\mathbf{Z})\to H^4(X;\mathbf{Z})\cong\mathbf{Z}$ 与页图一致；`$E_8$` 正确（pdftotext 文本层作 `£ 8`，系 OCR quirk，md 不采纳）。
  - 排版级伪影（登记不改）：印刷斜体 *smooth*、*Rohlin's theorem* 在 md 中拍平为正体；印刷粗体 **Z**/2 在 md 中为正体 `Z/2`。
- 修复登记：md 标题前补期刊行（依据 `audit-redo/p001.png` + 300dpi 期刊行裁片）。
