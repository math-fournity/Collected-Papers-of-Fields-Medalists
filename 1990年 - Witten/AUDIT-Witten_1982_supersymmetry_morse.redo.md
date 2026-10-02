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

## p.002（PDF p.2 / 印刷 p.662）
- PNG：`audit-redo/p002.png`（pngmono 150dpi）
- 核对：公式 (2)–(7)；相对论推广段；末段 H、P 偶性陈述；脚注 1（Lorentz 生成元 M 的对易关系）。
- 结果：PASS±。(2) `Q_iH - HQ_i = 0`、(3) `Q_i^2 = H`、(4) `Q_iQ_j + Q_jQ_i = 0`、(5) `Q_1^2 = H + P, Q_2^2 = H - P, Q_1Q_2 + Q_2Q_1 = 0`、(6) `[Q_i,H] = [Q_i,P] = 0`、(7) `H = ½(Q_1^2 + Q_2^2)` 及前后正文逐项与印刷页相符；脚注 1 全文（含 `[M,H] = P`、`[M,P] = H`、`[M,Q_1] = ½Q_1`、`[M,Q_2] = −½Q_2`）相符。**Luna 旧修复重核：DocVortex 脚注碎片清除后无残留，完整脚注保留，正确**。差异仅：页眉 "662 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.003（PDF p.3 / 印刷 p.663）
- PNG：`audit-redo/p003.png`（pngmono 150dpi）；Hilbert 记号终裁：`audit-redo/300dpi/p003_Hilbert_space.png`（300dpi 裁片）。
- 核对：真空态讨论五段、公式 (8)、[21] 段至跨页句 "It may be shown that a solution does"。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。正文与公式 (8) `Q_i|\Omega\rangle = 0` 及跨页断点均与印刷页相符。**发现 Luna 漏检 1 处记号错误**：md 将 "Hilbert space 𝓗 a state |Ω⟩" 的 script 𝓗 误作 `\mathcal{H}`（md line 73）；300dpi 裁片确认印刷字形与 p.001 判定的 `\mathscr{H}` 同形，已用结构化 Edit 修为 `$\mathscr{H}$`。**移交备注**：md line 639/643（§4，属 p.027/p.028 redo 复检范围）仍有 `\mathcal{H}`/`\tilde{\mathcal{H}}`，其印刷字形应由该两页 redo 仲裁，本轮不动。差异：页眉 "SUPERSYMMETRY AND MORSE THEORY 663" 未入 md（版面信息省略）。

## p.004（PDF p.4 / 印刷 p.664）
- PNG：`audit-redo/p004.png`（pngmono 150dpi）
- 核对：mass gap 续段、index 方法段、`𝓗₀ = 𝓗₀⁺ ⊕ 𝓗₀⁻` 分解段、`Q₊ + Q₋` 与 `Tr(−1)^F` 段、[21] 与 φ⁴ 段、章节路线段。
- 结果：PASS±。正文逐段与印刷页相符，含 `Q_i^2 = Q_j^2 = H`、`Tr(-1)^F`、`$\phi^{4}$`、(1)-(4)/(5) 引用及跨页断点（"can usefully be applied to supersymmetry." 起本页）。**Luna 旧修复重核：本页 `\mathscr{H}_0`/`\mathscr{H}_0^{\pm}`/`\mathscr{H}` 系列（md line 93/95/97）与印刷 script 记号一致，13 处修复正确**。差异仅：页眉 "664 EDWARD WITTEN" 未入 md（版面信息省略）。
