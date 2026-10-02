# Witten 1982 "Supersymmetry and Morse Theory" — Luna 审计重做（逐页对照 PDF 全量重检）

- 性质：**Luna 审计重做**。用户 2026-10-02 判定 Luna 审计不可信；本 redo 对 32 页全部重检（本文件本轮范围 p.1–p.9），Luna 的旧修复一并作为被检对象重新核验，一切以 PDF 原页为唯一裁决源。
- actor：`Wf-R-Witten`（Sub Agent，动态 workflow 单篇重审员）。
- host / model / effort：`zcode` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`（run 级配置，自报 `UNKNOWN`——无独立收据可证实际模型/effort）。
- 日期时间：2026-10-02 14:27 EDT（`date` 实测，本轮开工时刻）。
- PDF SHA-256：`3441cd533a88538dcb858e531fed1d21beb9ba468949814b626d70351f292b1d`（本轮 `shasum -a 256` 实测，与任务书一致）。
- MD 基线 SHA-256：`3a661655f3d797cf2f51cdc40423b53031a1da250d355c081f726303d1a4c4d2`（本轮实测；该基线 = 含 Luna 全部旧修复的当前态，worktree 内该 md 仅两笔历史：原始 `0b0f3dd2` 与 harvest `3429efe70`）。
- 文本层判定：`pdftotext -f 1 -l 1` 成功输出（ABBYY FineReader OCR 层）。判定 = **可用，双通道主对账**：OCR 文本用于逐页内容定位与文字级交叉核对；但 OCR 层含噪声（如首页 "Hubert space"、"Hubert" 类错误），**印刷页图仍是唯一裁决源**，一切内容级判定回到 150dpi/300dpi 页图。
- 证据图：`audit-redo/p0NN.png`（`gs -dNOPAUSE -dBATCH -sDEVICE=pngmono -r150` 逐页渲染，每页随审计提交）。不动旧 `audit/`。
- 纪律：print quirk 与错字忠实登记、绝不按数学预期静默改正；每处 Markdown 修改须溯源本篇页图证据；看不清即升级 300dpi 仲裁或如实记录，绝不编造。

---

## p.001（PDF p.1 / 印刷 p.661）
- PNG：`audit-redo/p001.png`（pngmono 150dpi）
- 核对：期刊页眉/卷页信息；标题、作者、摘要；§1 引言四段；公式 (1)；收稿日期脚注。
- 结果：PASS±。题录、摘要、引言各段（含 [17]/[18]、[22]、§§2 and 3）、公式 (1) `(-1)^F Q_i + Q_i(-1)^F = 0`、脚注（Received March 26, 1982；NSF PHY80-19754；致谢 R. Bott, W. Browder, S. Graffi, J. Milnor, D. Sullivan）逐项与印刷页相符。**Luna 旧修复重核：本页 `\mathscr{H}`/`\mathscr{H}^{\pm}` 共 7 处与印刷 script 𝓗 一致，修复正确**。差异仅：印刷页眉 "J. DIFFERENTIAL GEOMETRY 17 (1982) 661–692" 与页码未入 md（版面信息省略，不误导）。
