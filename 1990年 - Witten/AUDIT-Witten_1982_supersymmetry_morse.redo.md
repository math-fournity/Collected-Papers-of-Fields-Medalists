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

## p.010（PDF p.10 / 印刷 p.670）
- PNG：`audit-redo/p010.png`（pngmono 150dpi）；脚注 3 下标终裁：`audit-redo/300dpi/p010_footnote3.png`（300dpi 裁片）。
- 核对：路径 Γ 取向定义两段；(21) `n(a,b) = Σ_Γ n_Γ`；(22) `δ|a⟩ = Σ_b n(a,b)|b⟩`；`δδ* + δ*δ` 谱与 `Y_p` 上界段；脚注 3。
- 结果：PASS±。正文、(21)–(22)、`Y_p` 论证及跨页断点（line 259 末 "but also in"）逐项与印刷页相符。**Luna 旧修复重核：11 个 DocVortex 脚注碎片清除后无残留，完整脚注 3 保留，正确**。print quirk：脚注 3 印刷原句 "As **V_s** interpolates smoothly from Ṽ_B to V_A … via V_x"（300dpi 确认下标为 `s`，与同句 `V_x` 不一致系原刊排版如此）被 md line 261 忠实保留，不按上下文改为 `V_x`。差异仅：页眉 "670 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.011（PDF p.11 / 印刷 p.671）
- PNG：`audit-redo/p011.png`（pngmono 150dpi）；ℒ 字形终裁：`audit-redo/300dpi/p011_L23.png`（式 23）、`p011_L24.png`（式 24）、`p011_L25.png`（式 25）、`p011_L_prose_zoom.png`（散文处）。
- 核对：(23) 拉格朗日量逐项（动能 + ψ̄i Dψ/Dλ + ¼R_ijkl ψ̄ψψ̄ψ − t²γ∂h∂h − t Hessian ψ̄ψ）；(24) 欧氏作用量；(25) 配方恒等式；脚注 4–5。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。(23)–(25) 各项系数、指标、∫dλ 结构及前后正文（含 `Y_p = B_p`、[13]、`integral cohomology`）逐项与印刷页相符；脚注 4–5 全文相符。**发现 Luna 漏检 2 处记号错误**：(24)(25) 左端印刷为 cursive ℒ 加顶杠（与 (23) 的 ℒ 同字形），md 误作 `\bar{\mathfrak{L}}`（Fraktur）；300dpi 裁片确认后已用结构化 Edit 修为 `\bar{\mathcal{L}}`（md 原 line 278/284）。散文处 "extrema of ℒ"（无杠，line 281）与 (26) 的 `\bar{\mathcal{L}}`（p.012 复核）本就与印刷一致。**Luna 旧修复重核：重复孤立 ψ^i 碎片已清除、完整脚注 5 保留，正确**。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 671" 未入 md（版面信息省略）。

## p.012（PDF p.12 / 印刷 p.672）
- PNG：`audit-redo/p012.png`（pngmono 150dpi）
- 核对：(26) 作用量下界（ℒ̄ ⩾ t|h(+∞) − h(−∞)|）；(27) 等号条件；(28) `I = t|h(B) − h(A)|`；瞬子贡献 exp−I / exp−2I 段；Dirac 零模与归一化抵消段；跨页断点 "determine the sign from the"。
- 结果：PASS±。(26) 左端印刷 ℒ̄ 与 md `\bar{\mathcal{L}}` 一致；`⩾`、`±`/`∓`、绝对值与指数（exp − I、exp − 2I、exp − t|h(B) − h(A)|）逐项相符；`⟨b, d_t a⟩`、`L^2 norm`、`λ → λ + constant` 记号一致。print quirk：印刷原句 "The instantons contributions to matrix elements"（"instantons" 复数作定语）被 md 忠实保留。跨页断点一致（line 319 末）。差异仅：页眉 "672 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.013（PDF p.13 / 印刷 p.673）
- PNG：`audit-redo/p013.png`（pngmono 150dpi）；`Z→` quirk 独立终裁：`audit-redo/300dpi/p013_redefinition.png`（300dpi 裁片，本轮自摄）。
- 核对：WKB 符号确定两段；(29) `δ̃|a⟩ = Σ_b e^{−t(h(B)−h(A))} n(a,b)|b⟩`；`e^{th}` 共轭消除与状态重定义行；脚注 6–7。
- 结果：PASS±。(29)、正文（含 "the |a⟩ falls off like exp − th(φ)"——印刷 "the" 作引导词被 md 忠实保留）及脚注 6（[13, 171–178]、[19]）、脚注 7（绝对值可去条件、h(B) > h(A)）逐项与印刷页相符。print quirk：状态重定义行印刷原样为 "e^{−th(A)}|a⟩**Z**→|a⟩"，本轮 300dpi 裁片独立复核确认 `Z` 字形确实见于印刷（Luna 保留决定正确），md line 335 的 `Z\to` 忠实保留，不按数学预期删除。**Luna 旧修复重核：4 个 DocVortex 脚注碎片清除后无残留，完整脚注 7 保留，正确**。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 673" 未入 md（版面信息省略）。

## p.014（PDF p.14 / 印刷 p.674）
- PNG：`audit-redo/p014.png`（pngmono 150dpi）
- 核对：退化 Morse 情形设定段（`N_i`、Morse index `p_i`、负丛 `Λ(N_i)`）；`V(φ) = t²(dh)²` 段；`M(N_0)` 纤维丛邻域与 `d̃` 段；(30) `H_t = (d̃d̃* + d̃*d̃) + H′`；`|α(m;n)⟩` 段；Born–Oppenheimer 段开头。
- 结果：PASS±。(30) 各项、`D^2h/Dφ^iDφ^j`、`Λ(N_0)`、`p_i`-维负丛及正文逐项与印刷页相符。排版级伪影：印刷破折号 "state |α(m; n)⟩—n denoting…" 在 md 拍平为 "⟩ - n denoting"（line 359），不误导，登记不改。跨页断点一致（line 361 末 "large energy associated"）。差异仅：页眉 "674 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.015（PDF p.15 / 印刷 p.675）
- PNG：`audit-redo/p015.png`（pngmono 150dpi）
- 核对：(31) `|ψ(n,m)⟩ = |χ(n)⟩ ⊗ |α(m;n)⟩`；`|χ⟩` 全局条件与 twisted cohomology 段；(32) `(d̃d̃* + d̃*d̃)|χ⟩ = λ|χ⟩`；退化 Morse 不等式与 Morse 多项式 `t^p P̄_t(N_0)` 段；双原子分子类比段。
- 结果：PASS±。(31)–(32)、`Λ(N_0)` 可定向性条件、`H_t|ψ⟩ = λ|ψ⟩` 及正文逐项与印刷页相符。**Luna 旧修复重核：Morse 多项式指数 `t^p`（小写 p，md line 383）与印刷一致，修复正确**；`$\overline{P}$` 记号一致。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 675" 未入 md（版面信息省略）。

## p.016（PDF p.16 / 印刷 p.676）
- PNG：`audit-redo/p016.png`（pngmono 150dpi）；Lie 导数记号终裁：`audit-redo/300dpi/p016_Lie_derivative.png`（300dpi 裁片）。
- 核对：§3 标题；Killing 场设定两段；(33) `d_s = d + s i(K)`；`V_±` 分解段；(34) `d_s² = −d_s*² = s𝓛_K`；(35) `H_s = d_s d_s* + d_s* d_s`；[8] 界与 Hirzebruch signature 引段。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。(33)–(35)、`i(K)`、`V_±` 映射方向、`d_s*² = −d_s²` 及正文逐项与印刷页相符。**发现 Luna 漏检 1 处记号错误**：(34) 后散文 "and 𝓛_K is the Lie derivative" 印刷为 script 𝓛_K（300dpi 裁片确认，与式 (34) 内同形），md line 405 误作 `$\mathcal{L}_K$`；已用结构化 Edit 修为 `$\mathscr{L}_K$`（与 Luna 自己在 p.017/p.021/p.022 的同类修复标准一致）。**移交备注**：md line 539（p.022 redo 范围）`$I(\theta) = \operatorname{Tr} * \exp\theta\mathcal{L}_{K}$` 仍含 `\mathcal{L}_{K}`，且 `Tr * exp` 的 `*` 需该页仲裁。跨页断点一致（line 417 末 "each connected"）。差异仅：页眉 "676 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.017（PDF p.17 / 印刷 p.677）
- PNG：`audit-redo/p017.png`（pngmono 150dpi）
- 核对：Hopf 定理与 [6],[7],[5] 引段；`V̄` 子空间与 `𝓛_K` 零化段；(ker d_s/im d_s) 维数段；`e^{λP}` 共轭段（`e^{−λP} d_s e^{λP} = e^{−λ} d_s`、`s′ = se^{2λ}`）；`n_±`/`N_±` 与 Euler 特征段。
- 结果：PASS±。正文逐项与印刷页相符：`d_s² = s𝓛_K`、`χ(M)`、`n₊ − n₋ = N₊ − N₋ = χ(M)`、`n₊ ⩾ N₊`、`s ≠ 0` 条件一致。**Luna 旧修复重核：本页 2 处 Lie 导数 `\mathscr{L}_K`（md line 421）与印刷 script 记号一致，修复正确；共轭算子上标印刷为大写 `P`（`e^{λP}`，后续文字定义其在 p-形式上的作用），md 保留 `P` 符合页面证据**。跨页断点一致（line 431 末 "large s behavior of"）。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 677" 未入 md（版面信息省略）。

## p.018（PDF p.18 / 印刷 p.678）
- PNG：`audit-redo/p018.png`（pngmono 150dpi）
- 核对：`N_0`/`ψ̄` 策略段；`M(N_0)` 邻域与 `ψ̃`/`d_sψ̃ = 0` 段；`K² = (K,K)`、`M_ε`、截断函数 `φ(x)`；`K̃` 与 `i(K)(dK̃) = −d(K²)`；(36) σ 级数（系数 1/s、1/2s²、1/3s³ 与楔积次数）；(37) `χ = ψ̃ ∧ σ`。
- 结果：PASS±。(36) 各项导数阶、系数、楔积次数及 (37) 均与印刷页逐项相符；`K^2 ⩽ ε`、`x ⩾ ε`、`i(K)(d\tilde{K}) = -d(K^2)`、`d_sχ = 0`、`χ = d_sα` 一致；本页 Luna 无修复登记，redo 亦未发现需修复项。差异仅：页眉 "678 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.019（PDF p.19 / 印刷 p.679）
- PNG：`audit-redo/p019.png`（pngmono 150dpi）
- 核对：(38) `H_s = dd* + d*d + s²K² + s((dK̃)∧ + i(dK̃))`；(39) Killing 场局部标准形；(40) 近似 Hamiltonian；`n₊ ⩽ N₊` 论证段。
- 结果：PASS±。(38)–(40) 及正文逐项与印刷页相符。print quirks 忠实保留（Luna 已 300dpi 仲裁，本轮 150dpi 复核一致，不改）：(40) 势能项印刷排作 `((x_{2r-1})^2 + x_{2r})^2`（md line 484 原样）；(40) 末项求和上限印刷排作 `n`（λ_r 定义域至 n/2，md 原样）；正文 "As in §3 this makes it possible to obtain detailed information about the spectrum for large s"（上下文指向 §2 方法，印刷作 §3，md line 471 原样）。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 679" 未入 md（版面信息省略）。

## p.020（PDF p.20 / 印刷 p.680）
- PNG：`audit-redo/p020.png`（pngmono 150dpi）
- 核对：非孤立零点段（`H_N = dd* + d*d`）；`n₊ ⩽ N₊, n₋ ⩽ N₋` 上界段；Euler 特征框架段（`H_s = d_s d_s* + d_s* d_s = (d_s + d_s*)²`、`D_s = d_s + d_s*`）；(41) `χ(M) = χ(N)`；任意向量场推广段开头。
- 结果：PASS±。正文与 (41) 逐项与印刷页相符。**Luna 旧修复重核：`H_s` 第二项 `d_s^* d_s`（md line 499，Luna 曾修复原始 md 的重复 `d_s d_s^*`）与印刷一致，修复正确**；`d_s² + d_s*² = 0`、`D_{s±}`、`N₊ − N₋` 一致；跨页断点一致（line 509 末 "it is no"）。差异仅：页眉 "680 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.021（PDF p.21 / 印刷 p.681）
- PNG：`audit-redo/p021.png`（pngmono 150dpi）
- 核对：任意向量场 Euler 特征表达段（`α(N_i) = α₊ − α₋`、`χ(M) = Σ_i α(N_i)`）；signature 算子 `Q_s = i^{1/2}d_s + i^{−1/2}d_s*` 与 `Q̃_{s±}` 段；`𝓛_K` 零化段；`Q_s² = H_s + 2is𝓛_K` 段；(40) 与 `dx₁∧dx₂∧···dx_n` 取向段。
- 结果：PASS±。正文逐项与印刷页相符。**Luna 旧修复重核：`Q_s^2 = H_s + 2is\mathscr{L}_K`（md line 521，Luna 补回丢失项）与印刷一致，修复正确；本页 `\mathscr{L}_K` 系列记号与印刷 script 字形一致**；`i^{±1/2}`、`Ṽ₊/Ṽ₋`、`A_i`、`n_i = ±1` 一致；`dx_1∧dx_2∧⋯dx_n`（末项无 ∧）忠实保留。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 681" 未入 md（版面信息省略）。

## p.022（PDF p.22 / 印刷 p.682）
- PNG：`audit-redo/p022.png`（pngmono 150dpi）；`I(θ)` 定义行终裁：`audit-redo/300dpi/p022_Itheta.png`（300dpi 裁片）。
- 核对：(42) `sign(M) = Σ_i n_i`；τ 取向与 (43) `sign M = sign N`；`I(θ) = Tr * exp θ𝓛_K` 特征讨论；(44) `I_i(θ) = n_i Π_r (1+e^{iθλ_ir})/(1−e^{iθλ_ir})`；Fourier 分量段；(45) `sign M = Σ_i I_i(θ)` 与 Atiyah–Bott 引文。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。(42)–(45) 及正文逐项与印刷页相符。**上块移交仲裁完毕**：印刷原句确为 "I(θ) = Tr * exp θ𝓛_K"（`Tr * exp` 中的 `*` 是前文定义的 duality 算子，印刷如此，md 忠实保留）；但 `exp` 后的 Lie 导数印刷为 script `𝓛_K`（300dpi 裁片确认），md line 539 误作 `\mathcal{L}_{K}`（**Luna 漏检第 4 处**），已用结构化 Edit 修为 `\mathscr{L}_{K}`。**Luna 旧修复重核：本页其余 `\mathscr{L}_K`/`i\mathscr{L}_K` 与印刷一致，修复正确**。差异仅：页眉 "682 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.023（PDF p.23 / 印刷 p.683）
- PNG：`audit-redo/p023.png`（pngmono 150dpi）；(46) 字形终裁：`audit-redo/300dpi/p023_formula46.png`（300dpi 裁片）。
- 核对：twisted signature complex 与 [4]/[20] 引段；(46) `Q_{1s}, Q_{2s}, H_s, P = 2is𝓛_K`；(47) `Q_1² = H + P` 等；`d_{s,t} = e^{−ht}d_s e^{ht}` 与 (48) 四行定义；非紧情形两段。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。(46)–(48) 各行、下标 `s,t` 结构及正文逐项与印刷页相符。**发现 Luna 漏检 1 处记号错误**：(46) 末行印刷 `P = 2is𝓛_K`（script，300dpi 裁片确认），md line 562 误作 `\mathcal {L} _ {K}`（此前 grep 用无空格模式漏检，本轮宽松模式补获）；已用结构化 Edit 修为 `\mathscr {L} _ {K}`（(48) 内同位置本就是 `\mathscr`）。print quirk：印刷原句 "A slight generalizations is possible"（原刊语法 quirk）被 md line 573 忠实保留。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 683" 未入 md（版面信息省略）。

## p.024（PDF p.24 / 印刷 p.684）
- PNG：`audit-redo/p024.png`（pngmono 150dpi）
- 核对：N 非紧段（`(dh)^2` 有界条件）；`d_t = e^{−ht}de^{ht}`、`H_t = d_t d_t* + d_t* d_t` 谱重合段；§4 标题；Ω(B; S) 与内积 `(δσ, δτ) = ∫dx⟨δσ(x), δτ(x)⟩` 段；loop space de Rham 局限段。
- 结果：PASS±。正文与小节标题顺序逐项与印刷页相符；`Tr(−1)^F`、`V = V₊ ⊕ V₋`、`L → ∞` 一致；跨页断点一致（line 603 末 "Indeed, the group"）。差异仅：页眉 "684 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.025（PDF p.25 / 印刷 p.685）
- PNG：`audit-redo/p025.png`（pngmono 150dpi）
- 核对：U(1) circle action 段；(49) `d_s = d + si(K), H_s = d_s d_s* + d_s* d_s`；renormalization/asymptotically free 段；`S^N`/`CP^N` 大 N 谱段；`H = −∇² + V` 类比段。
- 结果：PASS±。(49) 及正文逐项与印刷页相符；`[1], [10], [19]`、`S^N`/`CP^N`、`(46) and (47)` 引用一致。print quirks 忠实保留（不改）：circle action 行 "$\sigma(x) + \sigma(x + a)$"（Luna 300dpi 已证为加号，本轮 150dpi 复核一致；数学意图未知）；"the supersymmetric nonlinear sigma is mathematically well-defined"（原刊漏 "model"，md line 617 原样）。跨页断点一致（line 619 末 "potential energy function"）。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 685" 未入 md（版面信息省略）。

## p.026（PDF p.26 / 印刷 p.686）
- PNG：`audit-redo/p026.png`（pngmono 150dpi）
- 核对：QFT 即无穷维量子力学段；de Rham 算子为 Laplace–Beltrami 平方根段（[22] 引文）；真空态问题段；`Ω(B)` 零点空间识别为 B 段；`H_s` 零模数等于 Betti 数之和段；`1/N` 展开段。
- 结果：PASS±。正文逐项与印刷页相符；`[1], [11], [19], [22]`、`§3` 引用及跨页断点（line 635 末 "drawn on the"）一致。差异仅：页眉 "686 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.027（PDF p.27 / 印刷 p.687）
- PNG：`audit-redo/p027.png`（pngmono 150dpi）；𝓗 字形终裁：`audit-redo/300dpi/p027_Hdecomp.png`（𝓗 = 𝓗₊ ⊕ 𝓗₋ 行）、`audit-redo/300dpi/p027_Q5decomp.png`（𝓗 = 𝓗̃₊ ⊕ 𝓗̃₋ 行）。
- 核对：index 定理引入段；`𝓗 = 𝓗₊ ⊕ 𝓗₋` 分解与 `Tr(−1)^F` 段；duality/`½N` 近似段；`Q₅` 对称与 `𝓗 = 𝓗̃₊ ⊕ 𝓗̃₋` 分解段；(50) `Tr(−1)^F = χ(B), Tr Q₅ = sign(B)`。
- 结果：FAIL（以原图为准）→ 修复后复核 PASS。正文与 (50) 逐项与印刷页相符。**上块移交仲裁完毕（发现 Luna 修复的字体变体错误）**：两处 300dpi 裁片确认印刷 Hilbert 空间字形为 script `𝓗`/`𝓗̃`（与 p.001 判定的 `\mathscr{H}` 同形），md line 639/643 共 18 处 `\mathcal{H}`/`\tilde{\mathcal{H}}`（Luna 从 K 恢复 H 时选错 \mathcal 变体，与其自身 p.001/p.004 修复标准不一致）已用结构化 Edit（replace_all，`mathcal{H}` 全文清零验证）修为 `\mathscr{H}`/`\tilde{\mathscr{H}}`。**Luna 旧修复其余部分重核：Q₅（从 Q_s 恢复，md line 643 ×3）与印刷一致，正确**。记号备注：md line 645 `$TrQ_{5}$` 与 `$\operatorname{Tr}(-1)^{F}$` 混排（印刷均作 Tr，排版级不一致，不误导，登记不改）。跨页断点一致（line 651 末 "it is enough"）。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 687" 未入 md（版面信息省略）。

## p.028（PDF p.28 / 印刷 p.688）
- PNG：`audit-redo/p028.png`（pngmono 150dpi）；`Lef(f)` quirk 独立终裁：`audit-redo/300dpi/p028_formula51.png`（300dpi 裁片，本轮自摄）。
- 核对：渐近展开论证段（[22] 引文）；`t: B → B` 与 `T: Ω → Ω` 定义段；(51) `Tr(−1)^F T = Lef(f), Tr Q₅T = sign(t)`；重要性段与总结段；`φ⁴` 理论过渡段开头。
- 结果：PASS±。正文与 (51) 逐项与印刷页相符。print quirk：印刷 (51) 原样为 "Lef(**f**)"（前句映射记作 t: B → B，300dpi 裁片独立复核确认字形为斜体 `f`，原刊符号不一致如此），md line 660 `\operatorname{Lef} (f)` 忠实保留，不按上下文改为 `Lef(t)`。跨页断点一致（line 669 末 "We"）。差异仅：页眉 "688 EDWARD WITTEN" 未入 md（版面信息省略）。

## p.029（PDF p.29 / 印刷 p.689）
- PNG：`audit-redo/p029.png`（pngmono 150dpi）
- 核对：`d_{s,t} = e^{−ht}d_s e^{ht}` 与 `H_{s,t}` 定义段；`φ: S → R` 与 (52) `h(φ) = ∫_S dx W(φ(x))`；`W(φ) = mφ²`/`aφ³ + bφ` 段；`d_t` 限制到 R 段；(53) `D = d/dφ + tL dW/dφ`；Atiyah–Singer 指数段。
- 结果：PASS±。(52)–(53) 及正文逐项与印刷页相符。**Luna 旧修复重核：`H_{s,t} = d_{s,t}d_{s,t}^* + d_{s,t}^* d_{s,t}`（md line 673，Luna 修复原始 md 的逗号误识为乘积）与印刷一致，修复正确**；`d_t = e^{-ht}de^{ht}`、`+φ^n`、`1,0, or -1` 一致；跨页断点一致（line 695 末 "In particular,"）。差异仅：页眉 "SUPERSYMMETRY AND MORSE THEORY 689" 未入 md（版面信息省略）。

## p.030（PDF p.30 / 印刷 p.690）
- PNG：`audit-redo/p030.png`（pngmono 150dpi）
- 核对：偶数阶多项式 `Tr(−1)^F = 1` 段；奇数阶/零指数段（`H_t` 与 `H_{s,t}` 谱收敛）；有限 `L` 与 `L → ∞` 体积极限两段；`W = φ³ + bφ` 的 b 正负区分段；§5 标题与首段。
- 结果：PASS±。正文与小节标题逐项与印刷页相符；`[22]`、`L → ∞`、`L = ∞` 一致；印刷斜体 "not"（md line 705 平排）为排版级拍平，登记不改。差异仅：页眉 "690 EDWARD WITTEN" 未入 md（版面信息省略）。
