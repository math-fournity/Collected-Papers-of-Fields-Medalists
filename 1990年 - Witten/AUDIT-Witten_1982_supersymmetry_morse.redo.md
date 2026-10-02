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

## p.005（PDF p.5 / 印刷 p.665）
- PNG：`audit-redo/p005.png`（pngmono 150dpi）
- 核对：§2 标题；公式 (9)–(12)；Betti 数 `B_p(t)` 不变性段；跨页断点 "We will be"。
- 结果：PASS±。(9) `Q_1 = d + d*, Q_2 = i(d - d*), H = dd* + d*d`、(10) `Q_1^2 = Q_2^2 = H, Q_1Q_2 + Q_2Q_1 = 0`、(11) `d_t = e^{-ht}de^{ht}, d_t^* = e^{ht}d^*e^{-ht}`、(12) `Q_{1t}, Q_{2t}, H_t` 各项及前后正文逐项与印刷页相符；`d^2 = d^{*2} = 0`、`e^{th}`、`B_p(t)` 记号一致；跨页断点与印刷页一致（line 139 末 "We will be"）。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 665" 未入 md（版面信息省略）。

## p.006（PDF p.6 / 印刷 p.666）
- PNG：`audit-redo/p006.png`（pngmono 150dpi）
- 核对：`a^k`/`a^{k*}` 记号段；式 (13)（Hessian 项与 `[a^{*i}, a^j]`）；`(dh)^2 = γ^{ij}(∂h/∂φ^i)(∂h/∂φ^j)`；弱 Morse 不等式论证；渐近展开 (14)；跨页断点 "This shows"。
- 结果：PASS±。(13) `H_t = dd* + d*d + t^2(dh)^2 + Σ_{i,j} t(D^2h/Dφ^iDφ^j)[a^{*i}, a^j]`、(14) `λ_p^{(n)}(t) = t(A_p^{(n)} + B_p^{(n)}/t + C_p^{(n)}/t^2 + ···)` 及正文逐项与印刷页相符；`M_p ⩾ B_p`、`D^2h/Dφ^iDφ^j`、`p^a` 记号一致。print quirk：印刷原句 "the number of $A_{p}^{(n)}$ vanish is equal to the Morse number"（"vanish" 非标准搭配）被 md 忠实保留，不改。跨页断点一致（line 163 末 "This shows"）。差异仅：页眉 "666 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.007（PDF p.7 / 印刷 p.667）
- PNG：`audit-redo/p007.png`（pngmono 150dpi）
- 核对：跨页续段 `M_p ⩾ B_p`；局部坐标与 Taylor 展开 `h(φ_i) = h(0) + ½Σλ_iφ_i² + O(φ³)`；式 (15)–(18)（谐振子谱与 `K_i` 本征值 ±1）；p-形式限制与零模对应段。
- 结果：PASS±。(15) `H̄_t = Σ_i(−∂²/∂φ_i² + t²λ_i²φ_i² + tλ_i[a^{i*}, a^i])`、(16) `H̄_t = Σ(H_i + tλ_iK_i)`、(17) `H_i = −∂²/∂φ_i² + t²λ_i²φ_i², K_j = [a^{j*}, a^j]`、(18) `tΣ_i(|λ_i|(1+2N_i) + λ_i n_i), N_i = 0,1,2,···, n_i = ±1` 及正文逐项与印刷页相符；`|λ_iφ_i| ≫ 1/√t`、`t|λ_i|(1+2N_i)` 一致。**Luna 旧修复重核：Taylor 余项 `O(φ^3)`（md line 167）与印刷一致，修复正确**。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 667" 未入 md（版面信息省略）。

## p.008（PDF p.8 / 印刷 p.668）
- PNG：`audit-redo/p008.png`（pngmono 150dpi）
- 核对：零能态计数与弱形式结论段；强 Morse 不等式 (19)；`X_p`/`δ: X_p → X_{p+1}` 上同调模型段；脚注 2（Reed–Simon [16]，pp. 34–38）。
- 结果：PASS±。(19) `Σ M_p t^p − Σ B_p t^p = (1 + t) Σ Q_p t^p` 及正文逐项与印刷页相符；`δ² = 0`、`Q_p` 非负整数陈述一致；脚注 2 全文（含 "pp. 34–38"、"double well potential"）相符；跨页断点一致（line 213 末 "we can go"）。差异仅：页眉 "668 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.009（PDF p.9 / 印刷 p.669）
- PNG：`audit-redo/p009.png`（pngmono 150dpi）；(20) 后关键词终裁：`audit-redo/300dpi/p009_correct_word.png`（300dpi 裁片）。
- 核对：微扰论各阶项消失段；tunneling/WKB/instantons 段；最陡下降方程 (20)；Morse 指数相差 1 条件段；路径 Λ 与 `V_A` 取向段。
- 结果：PASS±。(20) `dφ_i/dλ = γ^{ij} ∂h/∂φ_j` 及正文逐项与印刷页相符；`V(φ) = t^2(dh)^2`、`V_A`、`D^2h/Dφ^iDφ^j`、`[14]` 引用一致；跨页断点一致（line 213 末 "we can go" 续至本页 "further and attempt to refine"）。print quirk：印刷原句 "the ones which **correct** two critical points whose Morse indices differ by one"（300dpi 裁片确认为 "correct"，非 "connect"；原刊用词如此）被 md line 233 忠实保留，不按数学预期改动。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 669" 未入 md（版面信息省略）。
