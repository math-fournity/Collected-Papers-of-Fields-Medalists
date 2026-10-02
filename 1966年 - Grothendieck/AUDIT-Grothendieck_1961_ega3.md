# Audit: Grothendieck_1961_ega3

**状态**：`CANDIDATE_NOT_CURRENT`；本地 Peer 候选，待 Master 按 exact OID 复核和集成。
**actor**：Peer-P34
**model**：gpt-6-luna
**effort**：max
**基线**：`037602429d3b009f6fc468c732073eb3ddf9875f`（任务指定快照；本 worktree detached HEAD）
**源 PDF**：`1966年 - Grothendieck/Grothendieck_1961_ega3.pdf`；`pdfinfo` 报告 90 页，Creator `NUMDAM`，Producer `pdfTeX-1.40.16`。
**Markdown**：`1966年 - Grothendieck/Grothendieck_1961_ega3_mineru/Grothendieck_1961_ega3__Grothendieck_1961_ega3.md`。
**审计前 SHA-256**：`98c8a7bd3761a597ebe0007aa69c1c943c553c63fb1d91851c0c7eb231c523ed`。
**源件类别**：born-digital。`pdftotext -layout` 可抽取 252,332 字节，U+FFFD 计数为 0；以完整文本层逐物理页对账，抽取无法判定的字形回到本地 PDF 渲染页图与 300dpi 裁片。PDF 渲染确认题名页及正文页面为可读印刷页。本分类只说明页面有可用文本层，不证明文本层无丢字或公式保真。
**读取记录**：审计前已从头到尾读取目标 Markdown 全部 2,982 行（1–2,982）；后续修复完成后还须从头到尾复读最终文件。
**页面定位**：PDF p.1–3 为前置题录/题名/版权页；正文始于 PDF p.4，页脚印刷号 137。页面顺序定位由 PDF 文本层与 Markdown 文本序列匹配辅助；匹配结果只作定位，逐页签认仍以对应 PDF 页为准。
**身份与证据边界**：每页条目记录 actor、model、effort。页图与裁片只用于转录忠实性判断，不评判文章数学论证的正确性。只审查本篇指定 PDF、Markdown 和本篇短名前缀证据文件；未修改 PDF 或其他 MinerU 资产。根级索引、进度日志与 Master 当前态由 Master 维护。

## 逐页审计

### PDF p.1（题录/版权页；未见印刷页码）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:18 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p001.png`（pngmono 150dpi）；URL 字形终裁：`audit/300dpi/Grothendieck_1961_ega3_p001_url.png`（源页 300dpi 裁片）。
- 核对：作者、论文题名、期刊卷年与页码、版权/使用条款、Numdam 条目 URL。
- 结果：**FAIL**。题录文本与版权条款对应印刷页；但印刷 URL 为 `PMIHES_1963__17__5_0`，Markdown 写作 `PMIHES_1963_17_5_0`：两处双下划线均被压成单下划线。300dpi 裁片可读出印刷 URL，故判为源定位文本差异，待全篇审计完成后逐处手工修复并回核。
- 页内修复状态：未修改 Markdown；修复需以本页 300dpi 原页裁片为依据。

### PDF p.2（题名页；未见印刷页码）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:19 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p002.png`（pngmono 150dpi）；题名页与签名标记目检。
- 核对：机构名、论文题名、作者与合作者、卷册标记 III、分部名、年份、出版系列/卷号及刊行地；Markdown 所引 `images/page_1_image_1.jpg` 与印刷页上的签名图形相符。
- 结果：**PASS±**。可读文字均与题名页相符；作者信息与 “III” 之间的细横线属于版面分隔，Markdown 未表示该线，不改变文字内容。
- 页内修复状态：无需内容修复；未修改 Markdown。

### PDF p.3（版权/法定送存页；未见印刷页码）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:21 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p003.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p003_depot_legal.png`（“DÉPÔT LÉGAL”字形终裁裁片）。
- 核对：法定送存标题、首版季别/年份、版权限制文字及 IHÉS 版权行；MinerU 上下标将 `1re`、`4e` 以公式标记表示。
- 结果：**PASS±**。可读文字对应印刷页；但 Markdown 的 `DÉPOT LÉGAL` 漏掉 `O` 上的 circumflex，300dpi 原页裁片确认印刷为 `DÉPÔT LÉGAL`。这是可定位的单处重音差异，留待全篇审计结束后决定并逐处修复。
- 页内修复状态：尚未修改 Markdown。

### PDF p.4（印刷 p.137）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:23 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p004.png`（pngmono 150dpi；本页正文与主要符号目检）。
- 核对：章/节题名、6.1.1 引言关于换基与上同调函子的正文，以及本页所见的 $\mathbf{X},\mathbf{Y},\mathcal{F},\mathcal{G}$ 和派生函子记号；与 PDF 文本层、原页排版和 Markdown 对应段落核对。
- 结果：**PASS±**。正文与主要符号对应；MinerU Markdown 未保留本页重复章眉 `CHAPITRE III (suite)` 和印刷页码 137，属页眉/页脚排版信息丢失，不改变正文含义。
- 页内修复状态：无内容修复；未修改 Markdown。

### PDF p.5（印刷 p.138）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:25 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p005.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p005_equations.png`（两条 E₂ 谱序列及印刷编号裁片）。
- 核对：§6.1.2 后半、§6.1.3、§6.1.4、§6.2.1 文字和两条 E₂ 公式编号；与 PDF 文本层和公式裁片对照。
- 结果：**FAIL**。印刷页将第一条公式标为 `(6.2.1.1)`、第二条标为 `(6.2.1.2)`；Markdown 在第一条公式上附加 `\tag{6.2.1.2}`，而第二条公式没有对应编号。行 63 的单独 `(6.2.1.1)` 不改变问题：第一条公式仍被错误地标成 `.2`，第二条的 `.2` 标记缺失。另，印刷重复页眉 `A. GROTHENDIECK / Chap. III` 未录入；这属于排版信息。
- 页内修复状态：待全篇审计结束后，用 Edit/apply_patch 逐处调整公式编号，再回看本页裁片核实。
- 补充复核时间：2026-10-01 16:28 EDT。新增页面证据：`audit/300dpi/Grothendieck_1961_ega3_p005_complex_symbols.png`、`audit/300dpi/Grothendieck_1961_ega3_p005_hypercoh_argument.png`。原页记号为 `\mathcal{H}^{n}(f,\mathcal{K}^{\bullet})`，后文同样以 `\mathcal{K}^{\bullet}` 作为超上同调复形参数；Markdown 第 61 行四处写成 `\mathcal{H}^{\bullet}`。这把复形参数 K 改成了 H，改变了数学记号含义，属于同页额外 FAIL，待全文审计后逐处修正。
- 补充复核时间：2026-10-01 16:30 EDT。新增页面证据：`audit/300dpi/Grothendieck_1961_ega3_p005_T_indices.png`。印刷原文为“une composante `\mathcal{T}_{i}` de `\mathcal{T}_{\bullet}`”；Markdown 第 53 行将第二个下标 `\bullet` 误成 `i`。这改变了分量所在的 graded functor 记号，属同页额外 FAIL，待全文审计后逐处修正。

### PDF p.6（印刷 p.139）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:32 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p006.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p006_homotopism.png` 与 `audit/300dpi/Grothendieck_1961_ega3_p006_prop62_symbols.png`（K/H 及上下标终裁裁片）。
- 核对：§6.2.1 的复形/超上同调符号，关于 homotopisme 的段落、Čech 复形项，以及 Proposition (6.2.3) 中 $\mathcal{K}^{i}$ 的上下标。
- 结果：**FAIL**。Markdown 第 83 行把作为复形变量的 `\mathcal{K}^{\bullet}`、`\mathcal{K}'`、`\mathcal{K}''` 多处写成 `\mathcal{H}^{\bullet}`、`\mathcal{H}''` 或 `\mathcal{H}'''`，覆盖 homotopism 的源/目标、超上同调参数和 Čech 双复形参数；原页裁片均印为 K 复形记号。另，第 91 行在 `\mathrm{R}^{q}f_{*}(\mathcal{K}^{i})` 处将上标 `i` 写成下标 `\mathcal{K}_{i}`，300dpi 裁片确认原印为 `\mathcal{K}^{i}`。两类都改变了数学记号含义。Markdown 未保留本页重复页眉及印刷页码 139，属版面信息。
- 页内修复状态：待全篇审计结束后，用 Edit/apply_patch 逐处恢复 K 复形记号及 $i$ 上标，并依本页两张裁片逐项回核。

### PDF p.7（印刷 p.140）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:34 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p007.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p007_KH_top.png`、`audit/300dpi/Grothendieck_1961_ega3_p007_KH_bottom.png`（超上同调函子值、复形参数及 K/H 字形终裁裁片）。
- 核对：Corollary (6.2.4) 同构右端、Proposition (6.2.5) 的复形参数和相干性断言、(6.2.6) 下的同调函子与 Čech 复形说明；与 PDF 页图、文本层及 Markdown 对应行核对。
- 结果：**FAIL**。本页有多处 K/H 记号替换：Corollary (6.2.4) 中 `\Gamma(V,\mathcal{K}^{n}(f,\mathcal{K}^{\bullet}))` 的 `\mathcal{K}^{n}` 应为 `\mathcal{H}^{n}`；Proposition (6.2.5) 的 `\mathcal{H}^{q}(\mathcal{H}^{\bullet})`、`\mathcal{H}^{n}(f,\mathcal{H}^{\bullet})` 和后续 “A fortiori” 复形变量中的 H 应按印刷页恢复为 K。末段 (6.2.6) 中同调函子调用保持 H，但其复形实参、函子源和 Čech 复形实参在 Markdown 多处误作 H；原页裁片显示这些复形均为 K。上述替换混淆了复形 K 与其同调 H，改变数学记号含义。Markdown 未保留重复页眉和印刷页码 140，属版面信息。
- 页内修复状态：待全篇审计结束后逐处按 p.7 原页修正 K/H 记号并复核。

### PDF p.8（印刷 p.141）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:37 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p008.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p008_KH_exact_sequence.png`、`audit/300dpi/Grothendieck_1961_ega3_p008_reindex.png`、`audit/300dpi/Grothendieck_1961_ega3_p008_equation_label.png`。
- 核对：6.2.6 续段中的短正合列与连接态射复形参数、(6.2.7) 的次数重编号、(6.3.1.1) 公式号；对照 PDF 文本层及原页裁片。
- 结果：**FAIL**。Markdown 第 125 行将正合列的复形 `K'' → K' → K'''` 及连接态射参数 `K'''`、`K'` 写成 H 复形记号；原页明确为 K。第 137 行写 `\mathcal{K}^{i}=\mathcal{K}_{-}`，漏掉下标中的 `i`，原页为 `\mathcal{K}^{i}=\mathcal{K}_{-i}`。第 146 行将 `141` 放入公式 `\tag{141}`，但印刷公式号是 `(6.3.1.1)`（Markdown 第 143 行已另列该号）；`141` 是本页印刷页脚号，被错误绑定到公式。
- 页内修复状态：待全篇审计结束后逐处恢复复形参数、重编号下标并移除错误公式 tag，随后按三张裁片复核。

### PDF p.9（印刷 p.142）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:38 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p009.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p009_spectral_labels.png`（(6.3.2.1)/(6.3.2.2) 原页编号裁片）。
- 核对：§6.3.2 两条谱序列的 E₂ 公式及编号，后续 (6.3.4.1)、(6.3.6.1) 公式号；与 PDF 文本层、原页和 Markdown 对应段落核对。
- 结果：**FAIL**。原页分别以 `(6.3.2.1)`、`(6.3.2.2)` 标记两条公式；Markdown 第 156 行将 `.2` 作为第一条公式的 `\tag`，第二条公式则未标号，导致第一条编号错位且第二条编号缺失。裁片确认原页公式号在各自公式左侧。 (6.3.4.1) 与 (6.3.6.1) 号次对应。重复章眉和印刷页码 142 未进入 Markdown，属版面信息。
- 页内修复状态：待全篇审计结束后逐处校正两条公式编号，再按裁片回核。

### PDF p.10（印刷 p.143）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:39 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p010.png`（pngmono 150dpi）。
- 核对：命题 (6.3.6) 证明中的极限步骤、公式 (6.3.6.2)/(6.3.6.3)、命题 (6.3.7) 及公式 (6.3.7.1)；逐页文本层与 Markdown 段落对应，编号与印刷一致。Markdown 行 225 保留印刷页码 143。
- 结果：**PASS±**。所核正文与公式号相符；重复页眉 `11 A. GROTHENDIECK / Chap. III` 未收入 Markdown，属页眉信息。
- 页内修复状态：无内容修复；未修改 Markdown。

### PDF p.11（印刷 p.144）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:40 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p011.png`（pngmono 150dpi）。
- 核对：§6.3.8 的换环态射及复形映射、复合映射的传递性、谱序列态射，以及命题 (6.3.9) 的同调与两条谱序列同构；文本层与本页原图相符。公式编号 (6.3.8.1)、(6.3.9.1)、(6.3.9.2) 对应印刷标记，其中 `.2` 在原页标记两条谱序列公式组成的式组。印刷页码 144 保留在 Markdown 行 265。
- 结果：**PASS±**。核对的正文、符号和公式编号相符；重复页眉 `12 A. GROTHENDIECK / Chap. III` 未收入 Markdown，属版面信息。
- 页内修复状态：无内容修复；未修改 Markdown。

### PDF p.12（印刷 p.145）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:49 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p012.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p012_rho_morphism.png`、`audit/300dpi/Grothendieck_1961_ega3_p012_equation_63111.png`。
- 核对：(6.3.10.1) 的带限制标记复形、命题 (6.3.11) 的公式号及印刷页脚编号；对照 PDF 原页、文本层和 Markdown。
- 结果：**FAIL**。公式 (6.3.10.1) 印刷为 `P'_{[\rho]}`、`Q'_{[\rho]}`，中间项仍各用 `[\rho]`，末项为未带限制下标的 `P'`,`Q'`；Markdown 该式把四个 `\rho` 分别误作 `p/c/p/p`，末项又留下逗号下标。命题 (6.3.11) 的公式号印为 `(6.3.11.1)`，Markdown 写成 `(6.3.II.I)`。300dpi 裁片确认这些符号和数字。另，`pdftotext -layout` 将小号页脚读作 146，但原页印刷页码为 145，Markdown 行 267 的 145 与原页相符；这是文本层误读，不是 Markdown 错误。
- 页内修复状态：待全篇审计结束后逐处修正 (6.3.10.1) 标记、末项和公式号，并以本页两张 300dpi 裁片回核；保留正确的 Markdown 页码 145。

### PDF p.13（印刷 p.146）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:55 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p013.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p013_hypertor_notation.png`、`audit/300dpi/Grothendieck_1961_ega3_p013_tor_module_notation.png`、`audit/300dpi/Grothendieck_1961_ega3_p013_spectral_notation.png`。
- 核对：6.4.1–6.4.3 中本地 hypertor 名称、定义和公式 (6.4.1.1)/(6.4.3.1)–(6.4.3.3)；逐项对照原页专名/运算符及 Markdown 行 322–345。
- 结果：**FAIL**。原页的 hypertor 运算符是 Tor：Markdown 第 325 行写 `\mathfrak{Vor}`，第 327 行两处写 `\mathcal{Gor}`，第 337 行写 `\mathfrak{Gor}`，均把首字母 T 错成 V/G。第 331、334 行关于模情形的系数环记号，原页为 `\mathcal{O}_{S}`，Markdown 写成 `\mathrm{C}_{s}` / `\mathfrak{C}_{s}`；这两处改变了定义底环。另，(6.4.3.2)/(6.4.3.3) 的复形 hypertor 项印为 `\mathfrak{Tor}`，Markdown 写成 `\mathcal{T}or`，与本页所定义的符号不一致。原页印刷页脚 146 未保留在 Markdown，属页码信息。
- 页内修复状态：待全篇审计结束后逐处按本页裁片修正 Tor 首字母、系数环及复形 hypertor 记号，并回核公式 (6.4.1.1)–(6.4.3.3)。

### PDF p.14（印刷 p.147）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 16:57 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p014.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p014_tor_Q_symbols.png`、`audit/300dpi/Grothendieck_1961_ega3_p014_equation_label.png`。
- 核对：(6.4.4.1)/(6.4.4.2)、引理 (6.4.5) 中 (6.4.5.1)/(6.4.5.2) 与 (6.4.5.3) 的 Tor 映射、Q 复形参数和公式号。
- 结果：**FAIL**。印刷的 hypertor 映射运算符为 `\mathfrak{Tor}`；Markdown 第 363、369 行将其写成 `\mathfrak{Cor}`，第 381、387 行写成 `\mathcal{Cor}`。第 348、392 行把 `\mathcal{Q}_{\bullet}` 误录为 `2_{\bullet}`。此外，原页 (6.4.5.3) 公式号在左侧，印刷页脚 `147` 在右下角；Markdown 第 397 行错误地把页脚号写为该公式的 `\tag{147}`（第 394 行另列的公式号才对应原文）。300dpi 裁片确认上述差异。
- 页内修复状态：待全篇审计结束后逐处恢复 Tor/Q 记号并修正公式标签，之后按两张裁片回核；未修改 Markdown。

### PDF p.15（印刷 p.148）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 17:53 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p015.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p015_Tor_Q_notation.png`（hypertor/Tor 与 Q 记号裁片）。
- 核对：§6.4.6 公式组与 §6.5.1–6.5.2 对 hypertor、复形 Q 及局部粘合模的定义；逐处对照原页和 Markdown 行 400–422。
- 结果：**FAIL**。在 §6.5.1，原页为 `\mathfrak{Tor}` 并称其为 P、Q 的局部 hypertor；Markdown 第 418 行写成 `\mathfrak{Gor}`，且把第二复形 `Q` 写成数字 `2`。模块情形中原页写 `\mathcal{Tor}_{n}^{S}(F,G)` 作为替代记号，并以 `\mathfrak{Tor}` 表示复形 hypertor；Markdown 第 420 行将后者写成 `\mathcal{Cor}`。§6.5.2 的粘合构造及限制处原页使用 `\mathfrak{Tor}`，Markdown 行 422 将局部对象写成 `\mathcal{Cor}`。这些替换改变或混淆了 Tor 函子与复形参数。
- 页内修复状态：待全篇审计结束后逐处修正 Tor 符号及 Q 复形参数，并按本页裁片回核。Markdown 未保留本页印刷页码 148 和重复页眉，属页眉/页脚信息。

### PDF p.16（印刷 p.149）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 20:42 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p016.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p016_local_hypertor.png`（局部 hypertor/Tor/Q 记号裁片）。
- 核对：§6.5.2 粘合论证的续段、§6.5.3 局部 hypertor 定义、§6.5.4 两条谱序列；对照印刷原页中的 Tor 运算符及复形参数。
- 结果：**FAIL**。原页在 (6.5.3) 和 (6.5.4) 中反复使用 `\mathfrak{Tor}`；Markdown 第 424、426、430 行出现 `\mathcal{Cor}` / `\mathcal{Gor}` / `\mathfrak{Gor}`，把 Tor 的 T 错成 C/G。第 426、428 行还把第二个复形 Q 写成数字 `2`。第 428、435 行的复形 hypertor 符号也由原页 `\mathfrak{Tor}` 变成 `\mathcal{T}or`，与前页定义的局部复形符号不一致。原页印刷页码 149 未在 Markdown 中保留，属页码信息。
- 页内修复状态：待全篇审计结束后逐处恢复本页 Tor/Q 记号，并按 300dpi 裁片回核；未修改 Markdown。

### PDF p.17（印刷 p.150）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-01 21:44 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p017.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p017_Tor_Q.png`（hypertor/Tor/Q 字形裁片）。
- 核对：§6.5.5 续段，命题 (6.5.6)、备注 (6.5.7)、命题 (6.5.8) 及 Corollary (6.5.9) 在本页出现的部分；对照原页 hypertor 运算符和复形参数。
- 结果：**FAIL**。本页的复形局部 hypertor 原文使用 `\mathfrak{Tor}`：Markdown 第 449、457 行写为 `\mathcal{Cor}` / `\mathfrak{Cor}`，第 454、461 行的对象名称亦有 `Cor` 替代 `Tor`。第 449、454、467 行把复形 `Q` 写成数字 `2`。这些字母替换改变了函数符号或复形参数。原页印刷页码 150 与重复页眉未保留在 Markdown，属页眉/页脚信息。
- 页内修复状态：待全篇审计结束后逐处恢复 Tor 与 Q，并以本页裁片复核；未修改 Markdown。

### PDF p.18（印刷 p.151）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 00:11 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p018.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p018_Tor_Q.png`（Tor、Q 与态射记号裁片）。
- 核对：Corollary (6.5.9)、Corollary (6.5.10)、Proposition (6.5.11)、Remark (6.5.12) 的 Tor 运算符、Q 复形及 (6.5.12.1) 的态射下标。
- 结果：**FAIL**。印刷 hypertor 运算符为 `\mathfrak{Tor}`；Markdown 第 472、484、492 行写成 `\mathfrak{Cor}`，T 被误成 C。Markdown 第 477、489 行把复形 `Q` 写成数字 `2`。公式 (6.5.12.1) 原页为 `(i\times_{S}1)_{*}`；Markdown 将 `1` 并入乘积下标写作 `(i\times_{SI})_{*}`，改变了态射记号。300dpi 裁片确认以上差异。原页页脚 151 未在 Markdown 中保留，属页码信息。
- 页内修复状态：待全篇审计结束后逐处修正 Tor/Q 和 (6.5.12.1) 下标，再按裁片回核；未修改 Markdown。

### PDF p.19（印刷 p.152）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 00:15 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p019.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p019_tor_coherence.png`、`audit/300dpi/Grothendieck_1961_ega3_p019_multi_tor.png`。
- 核对：Proposition (6.5.13)、Corollary (6.5.14) 及其 (ii) 证明、(6.5.15) 多复形 hypertor 定义；对照原页中 Tor、复形像和态射的符号。
- 结果：**FAIL**。Proposition (6.5.13) 的 hypertor 记号原印为 `\mathfrak{Tor}`，Markdown 第 505 行写作 `\operatorname{Cor}`；(6.5.15) 原印多复形记号为 `\mathfrak{Tor}`，Markdown 第 517 行写作 `\mathcal{Cor}`。在 (6.5.14)(ii) 的证明中，Markdown 第 515 行将原页的 `\mathfrak{Tor}_{n}^{S}(\mathcal{F},\mathcal{G})` 损坏成 `Torn(S(F,G)`，并把原页态射 `i\times j` 写成 `1\times j`。这些替换破坏了运算符和态射记号。Markdown 未记录本页印刷页码 152。
- 页内修复状态：待全篇审计结束后逐处恢复 Tor 运算符与 `i\times j`，并依本页裁片回核；未修改 Markdown。

### PDF p.20（印刷 p.153）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 00:22 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p020.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p020_complex_degrees.png`（(6.5.15.1) hypertor 记号及次数符号裁片）。
- 核对：(6.5.15.1) 的多复形 hypertor 记号；§6.6.1 中复形微分次数、移位后的次数，以及 §6.6.2 的索引条件 `(i=1,2)`。
- 结果：**FAIL**。原页 (6.5.15.1) 用 `\mathfrak{Tor}`，Markdown 第 522 行写成 `\mathcal{T}or`。原页 §6.6.1 的次数分别印作 `-1`、`-1`（两个微分）与 `+1`；Markdown 把相应数字 1 写成大写罗马 `I`。§6.6.2 行 534 的条件原为 `(i=1,2)`，Markdown 写成 `(i=I,2)`。这些是数学符号/指标转录差异；Markdown 行 519 保留印刷页码 153。
- 页内修复状态：待全篇审计结束后逐处恢复 Tor 字体记号和数字 1，并按 300dpi 裁片回核；未修改 Markdown。

### PDF p.21（印刷 p.154）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 00:41 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p021.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p021_local_tor.png`（(6.6.4.1) 局部 Tor 记号裁片）。
- 核对：§6.6.3–6.6.4 的首批 E₂ 项及基于 affine intersections 的局部公式 (6.4.1.1)；核对 Markdown 保留的印刷页码 154。
- 结果：**FAIL**。原页 (6.4.1.1) 的右端局部运算符为 `\mathfrak{Tor}_{q}^{S}`；Markdown 第 596 行写成 `\mathfrak{Cor}_{q}^{S}`，把运算符首字母 T 误成 C。Markdown 行 599 的印刷页码 154 正确保留；重复页眉未录入，属版面信息。
- 页内修复状态：待全篇审计结束后将该处 `Cor` 逐处恢复为印刷 `Tor`，并以 300dpi 裁片回核；未修改 Markdown。

### PDF p.22（印刷 p.155）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 00:46 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p022.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p022_b_terms.png`、`audit/300dpi/Grothendieck_1961_ega3_p022_bprime_terms.png`。
- 核对：谱序列 (b)、(b') 的 E₂ 项、系数系统与末端超上同调公式；同时确认页码 155。
- 结果：**FAIL**。原页的局部 hypertor 运算符为 `\mathfrak{Tor}`；Markdown 第 606、612、618 行记作 `\mathfrak{Cor}`，T 被误成 C；第 630、636、642、648 行用 `\mathcal{T}or` 代替原页的 `\mathfrak{Tor}`。这些记号位于相同的局部 hypertor 系数项，需按原页恢复。另，Markdown 第 615 行将变量 U 写为转义美元符包住的 `\mathfrak{U}`（`\$...\$`），源页为普通变量 U，属于额外的数学标记渲染差异。Markdown 行 601 保留印刷页码 155。
- 页内修复状态：待全篇审计结束后逐处修正 Tor 字形标记与 U 的行内数学定界，并按两张裁片回核；未修改 Markdown。

### PDF p.23（印刷 p.156）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 00:51 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p023.png`（pngmono 150dpi）。
- 核对：§6.6.5 的 (c)/(d) 初始项、(6.6.6.1) 双复形等价、(6.6.7,t) 覆盖细化同构及页尾局部 hypertor 公式；印刷页码 156 未录入 Markdown。
- 结果：**PASS±**。本页所核公式、指标和系数项与 PDF 文本层/原页相符。印刷页眉与页码未写入 Markdown，属版面信息。另，原页在 6.6.7 的文字用 `\mathfrak{B}` 指较细覆盖，显示的同构公式用 `\mathfrak{V}`；Markdown 同样保留这处 B/V 切换，按印刷原样记录，不作语义性归一。
- 页内修复状态：无内容修复；未修改 Markdown。

### PDF p.24（印刷 p.157）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 00:56 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p024.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p024_global_tor.png`（global hypertor 记号裁片）。
- 核对：§6.6.7 全局 hypertor 的定义、§6.6.8 由两个态射诱导的全局谱序列对象，以及 §6.7.1 开篇定义。
- 结果：**FAIL**。原页 (6.6.8) 的全局 hypertor 对象及 (6.7.1) 的局部化对象均为 `\mathfrak{Tor}`；Markdown 第 707 行写为 `\mathcal{Gor}`、第 711 行写为 `\mathfrak{Gor}`，把首字母 T 错成 G。300dpi 裁片确认原页 Tor 记号。原页印刷页码 157 未在 Markdown 中记录，属页码信息。
- 页内修复状态：待全篇审计结束后逐处恢复 Tor 运算符，并以本页裁片回核；未修改 Markdown。

### PDF p.25（印刷 p.158）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 01:04 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p025.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p025_theorem_673.png`（Theorem (6.7.3) 运算符及复形参数裁片）。
- 核对：(6.7.1.1)、(6.7.2.1) 两个谱序列同构，以及 Theorem (6.7.3) 开头对全局 hypertor 双函子的命名。
- 结果：**FAIL**。Theorem (6.7.3) 原页将新定义的双函子写为 `\mathfrak{Tor}_{\bullet}^{S}(f_{1},f_{2};\mathcal{P}^{(1)},\mathcal{P}^{(2)})`；Markdown 第 749 行写成 `\mathcal{Gor}_{\bullet}^{S}`，把 Tor 的首字母 T 误为 G。300dpi 裁片确认印刷符号。原页印刷页码 158 未写入 Markdown，属页码信息。
- 页内修复状态：待全篇审计结束后按本页裁片恢复双函子 Tor 记号；未修改 Markdown。

### PDF p.26（印刷 p.159）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 01:20 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p026.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p026_local_tor.png`（Theorem (6.7.3) Hypertor 符号裁片）。
- 核对：Theorem (6.7.3) 的全局双函子记号；其余页面文字至 §6.7.4 开始与 Markdown 对应。
- 结果：**FAIL**。原页 Theorem (6.7.3) 将新定义的双函子写为 `\mathfrak{Tor}_{\bullet}^{S}`；Markdown 第 749 行写成 `\mathcal{Gor}_{\bullet}^{S}`，把首字母 T 误为 G。150dpi 页图与 300dpi 裁片均确认该字形。原页印刷页码 159 未在 Markdown 中保留。
- 页内修复状态：待全篇审计结束后按本页裁片恢复 Tor 记号；未修改 Markdown。

### PDF p.27（印刷 p.160）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 01:25 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p027.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p027_theorem_E2.png`、`audit/300dpi/Grothendieck_1961_ega3_p027_hypercoh_tensor.png`、`audit/300dpi/Grothendieck_1961_ega3_p027_kunneth_formula.png`。
- 核对：Theorem (6.7.3) 的限制公式和 E₂ 项，(6.7.4.1)/(6.7.4.2)，Propositions (6.7.5)/(6.7.6)，以及 Künneth 同构标签。
- 结果：**FAIL**。本页多处局部 hypertor 印刷为 `\mathfrak{Tor}`，Markdown 却写成 `\mathfrak{Cor}`：包括第 754、770、774、798、806、827、834 行。式 (6.7.6.1) 原页编号为 `.1`，Markdown 第 834 行写为 `.x`。此外，第 801 行将印刷的 `\otimes_Y` 转成 `\otimes_{\mathbb{Y}}`。原页 p.160 页脚号未录入。裁片核实了 `.1` 公式号及 Tor/T 字形。
- 页内修复状态：待全篇审计结束后逐处恢复 Tor 记号、公式号与张量下标；未修改 Markdown。
- 补充复核时间：2026-10-02 01:29 EDT。使用同页 `audit/300dpi/Grothendieck_1961_ega3_p027_theorem_E2.png` 回查 E₂ 公式的字形：印刷在 (a)、(b')、(c)、(d) 项中均用 `\mathfrak{Tor}`；Markdown 第 766、778、782、786 行改用 `\mathcal{T}or`。这是本页同一 local-hypertor 符号的附加字体/记号差异，纳入同页复核与修复登记。

### PDF p.28（印刷 p.161）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 01:37 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p028.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p028_Q_Tor_labels.png`。
- 核对：Proposition (6.7.7) 中的 local hypertor 双函子、复形参数及公式号；并检查 Proposition (6.7.6) 的公式 (6.7.6.3) 与 Theorem (6.7.8) 在本页的起始处。
- 结果：**FAIL**。第 845 行将印刷的 `\mathcal{Q}_{\bullet}` 误录为 `2_{\bullet}`。Proposition (6.7.7) 的公式左端印为 `\mathfrak{Tor}_{n}^{S}`，Markdown 第 862 行写作 `\mathcal{Cor}_{n}^{S}`，同时误录了首字母和运算符字体；同一行公式号印为 `(6.7.7.1)`，Markdown 写成 `(6.7.7.I)`。300dpi 裁片确认 Q、Tor 及数字 1。公式 (6.7.6.3) 的编号和其余核对符号与原页相符。Theorem (6.7.8) 在本页只开始列出假设，后续部分留待 PDF p.29 核对。印刷页脚 161 未录入 Markdown，属版面信息。
- 页内修复状态：待全篇审计结束后逐处修复 Q、local hypertor 记号和公式号，并按裁片回核；未修改 Markdown。

### PDF p.29（印刷 p.162）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 01:40 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p029.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p029_kunneth_tor_labels.png`、`audit/300dpi/Grothendieck_1961_ega3_p029_local_tor.png`。
- 核对：Theorem (6.7.8) 的 Künneth 公式号与表达式；Proposition (6.7.9) 的三项假设和结论中的局部 hypertor 记号；并检查 (6.7.10) 开头及图示。
- 结果：**FAIL**。Theorem (6.7.8) 的 Künneth 公式印为 `(6.7.8.1)`，Markdown 第 872 行将末位数字 1 写成字母 `i`。Proposition (6.7.9) 第一项条件印为 `1°`，Markdown 第 889 行写成 `$^{10}$`，漏掉了基位数字 1。结论及证明中的局部 hypertor 均印为 `\mathfrak{Tor}`；Markdown 第 895 行写作 `\mathcal{Cor}`、第 897 行写作 `\mathcal{Eor}`，分别误录首字母并改变了运算符字体。300dpi 裁片确认公式标签和 Tor 字形。本页其余核对的 theorem/proposition 正文、(6.7.10.1)/(6.7.10.2) 与图示相符。印刷页脚 162 未录入 Markdown，属版面信息。
- 页内修复状态：待全篇审计结束后逐处修复公式号、条件标号和两处 local hypertor 记号，并以两张裁片回核；未修改 Markdown。

### PDF p.30（印刷 p.163）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 01:43 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p030.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p030_refinement_diagram.png`、`audit/300dpi/Grothendieck_1961_ega3_p030_P_bullet.png`。
- 核对：Proposition (6.7.10) 的细化覆盖构造、(6.7.10.3)–(6.7.10.5) 映射和交换图；检查由 (6.7.10.4) 推出模块同态的文字说明。
- 结果：**FAIL**。交换图印为 `\mathfrak{B}^{(i)}` 与 `\mathfrak{B}'^{(i)}`，Markdown 第 922 行却把图中两个 `\mathfrak{B}` 都录成 `\mathfrak{V}`。第 931 行的 `u_i^*(\mathcal{P}^{(i)}_i)` 漏掉印刷记号 `\mathcal{P}^{(i)}_{\bullet}` 的 bullet。300dpi 裁片确认图中字母及缺失的复形指标。其余核对的 (6.7.10.3)–(6.7.10.5)、正文和末段局部化同构与原页相符；印刷页脚 163 未录入 Markdown，属版面信息。
- 页内修复状态：待全篇审计结束后逐处恢复两个覆盖符号并补入 bullet，再按裁片回核；未修改 Markdown。

### PDF p.31（印刷 p.164）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 01:47 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p031.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p031_general_hypertor.png`、`audit/300dpi/Grothendieck_1961_ega3_p031_global_tor.png`、`audit/300dpi/Grothendieck_1961_ega3_p031_proposition_6712.png`、`audit/300dpi/Grothendieck_1961_ega3_p031_symmetry_associativity.png`。
- 核对：(6.7.11) 的多变量 global hypertor 定义和记号缩写；Proposition (6.7.12) 的 Tor 同构及 degree-zero 情形；Remark (6.7.13) 的交换因子同构；§6.8/(6.8.1) 的结合谱序列记号。
- 结果：**FAIL**。印刷的 global/local hypertor 运算符均为 `\mathfrak{Tor}`：Markdown 第 943 行写成 `\mathcal{C}\sigma r`；第 946 行的两个简写均写成 `\mathfrak{Cor}`；第 952 行同构两端也均写成 `\mathfrak{Cor}`；第 957 行两处写成 `\mathcal{E}\mathsf{or}`；第 961 行写成 `\mathcal{Cor}`；第 964 行写成 `\mathfrak{Cor}`。Remark (6.7.13) 的底环印作 `S`，Markdown 第 957 行误作 `\mathbb{S}`。Proposition (6.7.12) 假设印为 degree `0`，Markdown 第 949、955 行分别写成字母 `o` 和 `(o,o)`，应为数字 `0` 与 `(0,0)`。300dpi 裁片确认 Tor、底环和度数记号；印刷页脚 164 在 Markdown 第 967 行保留。
- 页内修复状态：待全篇审计结束后逐处恢复 Tor 与底环记号、degree-zero 数字，并按四张裁片回核；未修改 Markdown。

### PDF p.32（印刷 p.165）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 01:50 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p032.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p032_associativity_E2.png`、`audit/300dpi/Grothendieck_1961_ega3_p032_corollary_E2.png`。
- 核对：Proposition (6.8.2) 的结合谱序列、共同 abutment 和 E₂ 项；Corollary (6.8.3) 的结论与 E₂ 公式；并检查该推论证明中的三复形乘积、两个分块复形和有界性论证。
- 结果：**FAIL**。Proposition (6.8.2) 的共同 abutment 印为 `\mathfrak{Tor}_{\bullet}^{S}`，Markdown 第 975 行误录为 `\mathfrak{Gor}_{\bullet}^{S}`。同一行 E₂ 项的两个分块 hypertor 均印为 `\mathfrak{Tor}^{S}`，Markdown 将两者都写成 `\mathfrak{Gor}^{S}`。300dpi 裁片确认 Tor 首字母。Corollary (6.8.3) 中核对的粗体 Tor 记号、E₂ 项、双分块 tensor product 和证明文字与原页相符。印刷页脚 165 未录入 Markdown，属版面信息。
- 页内修复状态：待全篇审计结束后恢复第 975 行的三个 Tor 首字母，并以 associativity E₂ 裁片回核；未修改 Markdown。

### PDF p.33（印刷 p.166）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 01:53 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p033.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p033_base_change_proof.png`、`audit/300dpi/Grothendieck_1961_ega3_p033_complex_Q.png`。
- 核对：§6.9.1 的换基记号和 (6.9.2.1) 同构；Proposition (6.9.2) 的仿射情形证明与单指标说明；复形 Q′ 的引入及 Proposition (6.9.3) 的起始声明。
- 结果：**FAIL**。§6.9.1 中两处 global hypertor 运算符印为 `\mathfrak{Tor}`，Markdown 第 1001 行均写成 `\mathcal{Cor}`；(6.9.2.1) 两端也均印为 `\mathfrak{Tor}`，Markdown 第 1006 行写成 `\mathfrak{Cor}`。第 1009 行把印刷的 `\mathbf{C}^{\bullet}(\mathfrak{U}^{(i)},\mathcal{P}_{\bullet}^{(i)})` 在 tensor 公式及紧接着定义 `L^{(i)}` 的位置均误写成 `\mathcal{P}_{\bullet}^{'(i)}`。第 1011 行将单指标 `i` 写成大写 `I`，并把 degree `0` 两处误作字母 `o`。原文的新复形记作 `\mathcal{Q}'`；Markdown 第 1013 行写成 `2'`，第 1019 行也将谱序列的复形参数写作 `2'`；第 1016 行的 hypertor 运算符误作 `\mathfrak{Cor}`，第 1019 行共同 abutment 的 `\mathfrak{Tor}` 误作 `\mathcal{Gor}`。两张 300dpi 裁片确认 P/P′、Q′ 和 Tor 字形。印刷页脚 166 未录入 Markdown，属版面信息。
- 页内修复状态：待全篇审计结束后修正换基 proof 的复形、下标、degree-zero、Q′ 和 hypertor 记号，并按裁片回核；未修改 Markdown。

### PDF p.34（印刷 p.167）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:00 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p034.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p034_693_E2.png`、`audit/300dpi/Grothendieck_1961_ega3_p034_694_E2.png`、`audit/300dpi/Grothendieck_1961_ega3_p034_proof_E2.png`、`audit/300dpi/Grothendieck_1961_ega3_p034_final_E2_modules.png`。
- 核对：Proposition (6.9.3) 三条谱序列的 E₂ 公式；Corollary (6.9.4) 的对象设定、共同 abutment 和三条 E₂ 公式；证明中 Cartan–Eilenberg 复形、张量积与最终 E₂ 项。
- 结果：**FAIL**。Proposition (6.9.3) 的 (e) 公式第 1022 行把印刷 `\mathfrak{Tor}` 写为 `\mathfrak{Cor}`，并把 `\mathcal{Q}'_{\bullet}` 写为 `\mathcal{Z}'_{\bullet}`。(f) 公式第 1026 行同样把首个 `\mathfrak{Tor}` 写成 `\mathfrak{Cor}`；整条公式在首个分块后即被截断，缺少余下分块 hypertor 和 `\mathcal{H}_{q_{m+1}}(\mathcal{Q}'_{\bullet})`，末尾还留有与原文不符的残缺 `\tag{...}`。 (f′) 公式第 1030 行的序列标记丢失 `f`，印刷 `(f′)` 被写成仅带 prime 的标记；其 global hypertor `\mathfrak{Tor}` 变成 `\mathfrak{Cor}`，末项 `\mathcal{Q}'_{\bullet}` 变成 `\mathcal{Z}'_{\bullet}`，求和条件也把 `q_1+\dots+q_m=q` 录成省略号后缺少加号。Corollary (6.9.4) 第 1035 行把 `1\leq i\leq m` 写成 `I\leq i\leq m`，把 `\mathbf{X}'^{(i)}=\mathbf{X}^{(i)}_{(S')}` 缩成 `X^{(i)}=X_{(S')}`，把复形 `\mathcal{P}_{\bullet}^{(i)}` 写成 `P_i`，并漏掉 `\mathcal{Q}'_{\bullet}` 的 bullet。证明第 1055 行把 global hypertor `\mathfrak{Tor}` 写作 `\mathcal{Gor}`，将印刷 `\mathbf{C}^{\bullet}` 记成 `\mathbf{C}^{*}`，并把 tricomplex 的两个 degree-zero 记成字母 `o`。300dpi 裁片核实上述公式、Q′、复形指标和符号。最终 E₂ 公式中两处 M/M′ 的印刷写法与 Markdown 一致；印刷页脚 167 未录入 Markdown，属版面信息。
- 页内修复状态：待全篇审计结束后修复三条 E₂ 公式、Corollary 输入记号及证明中的 Tor/cochain/degree-zero 记号；按四张裁片逐处回核。Markdown 未修改。

### PDF p.35（印刷 p.168）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:06 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p035.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p035_global_hyperhomology.png`、`audit/300dpi/Grothendieck_1961_ega3_p035_hyperhomology_E2.png`、`audit/300dpi/Grothendieck_1961_ega3_p035_j_plus_one.png`、`audit/300dpi/Grothendieck_1961_ega3_p035_remark_corollary_footer.png`。
- 核对：Proposition (6.9.3) 的 (f) 续证、两个双复形 E₂ 表达式和局部化公式；Remark (6.9.5) 的同伦替换与谱序列同构；Corollary (6.9.6) 两项假设及其页内页码。
- 结果：**FAIL**。第 1061 行第二个同调等式的原文为 `H_{q_i}(M^{(i)}\otimes_A A')`，Markdown 又写成 `M'^{(i)}\otimes_A A'`；同一行 `\mathcal{P}^{(i)}` 漏掉印刷复形下标 `\bullet`。第 1067 行将关于 Q′ 双复形的三个数字 `0`（degree-zero 与 `n\ne0`）均写成字母 `o`。第 1073 行将 affine intersection 的数量 `j+1` 写成 `j+i`。Remark (6.9.5) 第 1087 行漏录 `\mathcal{Q}'_{\bullet}` 的 bullet，且谱序列右端将印刷的参数分隔符 `;` 写成冒号。Corollary (6.9.6) 第一项条件标记印为 `1°`，Markdown 第 1091 行写成 `$^{10}$`；第 1094 行的 global hypertor `\mathfrak{Tor}_{n}^{S}` 写成 `\mathcal{Cor}_{n}^{S}`；第 1099 行将复形 `\mathcal{Q}'` 写成 `2'`。本页印刷页脚 168 未录入 Markdown；第 1101 行的 169 与 PDF p.36 的印刷页脚相符，虽出现在该页正文前。300dpi 裁片确认复形指标、数字、`j+1`、分隔符及页码边界。
- 页内修复状态：待全篇审计结束后逐处恢复同调输入、complex bullet、degree-zero、交集数、Remark 参数分隔符及 Corollary 记号/页码，按四张裁片回核；未修改 Markdown。

### PDF p.36（印刷 p.169）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:14 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p036.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p036_696_formulas.png`、`audit/300dpi/Grothendieck_1961_ega3_p036_697_estimate.png`。
- 核对：Corollary (6.9.6) 的函子性同构、两条 edge homomorphism 及证明；Corollary (6.9.7) 的有限度数估计、条件 (3°) 和公式 (6.9.7.1)。
- 结果：**FAIL**。第 1103 行将印刷的 `\mathcal{P}_{\bullet}^{\prime(i)}=\mathcal{P}_{\bullet}^{(i)}\otimes_{\mathcal{O}_{S}}\mathcal{O}_{S'}` 写成 `\mathcal{P}^{\prime(i)}=\mathcal{P}^{\prime(i)}\otimes_{\mathcal{O}_{\mathfrak{s}}}\mathcal{O}_{S'}`，左右两边都漏掉 complex bullet，右端还多出一个 prime。公式 (6.9.6.1) 第 1106 行把两处 `\mathfrak{Tor}` 写为 `\mathfrak{Cor}`，并将 `\otimes_{\mathcal{O}_{S}}` 写为 `\otimes_{S}`；(6.9.6.2) 第 1112 行两端的 `\mathfrak{Tor}` 也均变成 `\mathfrak{Cor}`。(6.9.6.3) 第 1118 行两处印刷 `\mathfrak{Tor}` 被误作 `\mathfrak{Gor}`。第 1124 行 edge homomorphism 两端分别将 `\mathfrak{Tor}^{S}`、`\mathfrak{Tor}^{S'}` 写成 `\mathfrak{Cor}`；第 1130 行同一 global hypertor 写为 `\mathcal{Cor}`；第 1136 行 edge homomorphism 起点和直和项中的 `\mathfrak{Tor}` 均写作 `\mathfrak{Cor}`。第 1139 行把复形 `\mathcal{Q}'` 两次写作 `2'`，把两个数字 `0` 写成字母 `o`，并将 `\mathcal{F}'=\mathcal{O}_{S'}` 的底空间下标写成 `S`。Corollary (6.9.7) 条件 (3°) 第 1141 行将 `\mathfrak{Tor}_{q}^{S}` 写成 `\mathcal{Gor}_{q}^{S}`；公式 (6.9.7.1) 第 1146 行将 `\mathfrak{Tor}_{p}^{S'}` 写成 `\mathfrak{Cor}_{p}^{S'}`。300dpi 裁片核实 Tor/Q、张量底环和页内公式。Markdown 第 1101 行的单独页码 169 与本页印刷页脚相符，虽出现在本页正文前。
- 页内修复状态：待全篇审计结束后逐处恢复换基对象、`Tor`、张量底环、`Q'` 与零度记号，再按两张裁片回核；未修改 Markdown。

### PDF p.37（印刷 p.170）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:19 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p037.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p037_estimate_proof.png`、`audit/300dpi/Grothendieck_1961_ega3_p037_698_formulas.png`、`audit/300dpi/Grothendieck_1961_ega3_p037_699_footnote.png`。
- 核对：Corollary (6.9.7) 估计证明的谱序列标记与 Tor 记号；Proposition (6.9.8) 的共同 abutment、两条 E₂ 公式、两种特化情形及公式编号；Corollary (6.9.9) 与页下注。
- 结果：**FAIL**。第 1149 行关于 Corollary (6.9.7) 的平坦 hypertor 被写作 `\mathcal{Gor}_{q}^{S}`，原页为 `\mathfrak{Tor}_{q}^{S}`；同一行两处谱序列标记原为 `(f')`，Markdown 均写成 `(l')`。Proposition (6.9.8) 第 1153 行共同 abutment 的 `\mathfrak{Tor}_{\bullet}^{S}` 写成 `\mathfrak{Cor}_{\bullet}^{S}`。其 E₂ 公式编号也错置：第 1155 行孤立的 `(6.9.8.1)` 原应附于第一条公式；第 1158 行将整组两公式统一标为 `(6.9.8.2)`，而原页分别标作 `(6.9.8.1)`、`(6.9.8.2)`。后面的特化公式同样将编号错移：第 1165 行孤立输出 `(6.9.8.3)`，第 1168 行却给第一条公式加 `(6.9.8.4)`，第 1172 行第二条公式未带编号；原页第一、第二条分别为 `(6.9.8.3)`、`(6.9.8.4)`。第 1179 行多出不见于原页的 HTML 页下注片段 `(6.9.8),`；紧接着的真正脚注 (1) 与原页相符。印刷页脚 170 未录入 Markdown。300dpi 裁片确认 `(f')` 字形、Tor 运算符、编号归属及脚注内容。
- 页内修复状态：待全篇审计结束后恢复 hypertor/谱序列标记和四个公式号的归属，并删除无原文依据的页下注残片；按三张裁片回核。Markdown 未修改。

### PDF p.38（印刷 p.171）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:24 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p038.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p038_699_610_formulas.png`、`audit/300dpi/Grothendieck_1961_ega3_p038_6101_contract_diagram.png`。
- 核对：Corollary (6.9.9) 的两条基变换同构；Corollary (6.9.10) 的纤维记号和公式 (6.9.10.1)；§6.10 Proposition (6.10.1) 的对象范围、同构 (6.10.1.1) 与交换图 (6.10.1.2)。
- 结果：**FAIL**。(6.9.9.1) 第 1186 行把 `\mathfrak{Tor}` 写成 `\mathfrak{Cor}`，并将 `\mathcal{H}^{-n}` 写成 `\mathscr{H}^{-n}`、把张量底环 `\mathcal{O}_{S}` 写成 `\mathcal{O}_{\mathfrak{s}}`；(6.9.9.2) 第 1192 行的张量底环同样把大写 `S` 写成小写 `s`。第 1195 行的特例为 `m=1`，Markdown 写成字母 `i`。Corollary (6.9.10) 第 1197 行将 `s\in S` 及各处 `\otimes_{S}` 改成 `s\in\mathbb{S}` / `\otimes_{\mathbb{S}}`，把纤维态射 `f\times_{S}1` 记为 `f\times_{\mathbb{S}}\mathbf{I}`，并把 `\mathcal{P}_{\bullet}\otimes_{\mathcal{O}_{S}}k(s)` 的底环写成 `\mathcal{O}_{\mathbb{S}}`；公式 (6.9.10.1) 第 1200 行又把 `\mathcal{O}_{S}` 写成 `\mathcal{O}_{s}`。Proposition (6.10.1) 第 1207 行把指标范围 `1\leq i\leq n` 的首位数字 1 写成字母 i，且没有保留 `\mathcal{R}_{\bullet}`、`\mathcal{Q}'_{\bullet}` 的复杂指标。公式 (6.10.1.1) 第 1210 行把 `\mathfrak{Tor}_{\bullet}^{S}` 写成 `\mathfrak{Cor}_{\bullet}^{S}`，把 `\mathcal{Q}'_{\bullet}` 写成 `2'_{\bullet}`；同时将印刷的 `\mathcal{H}`、`\mathcal{R}`、`\mathcal{O}_{S}` 的字体分别改作 `\mathscr{H}`、`\mathscr{R}`、`\mathscr{O}_{S}`。第 1213 行把函子变量 `\mathcal{Q}'` 记为 `2'`。交换图 (6.10.1.2) 第 1216 行两处 hypertor 运算符也都把 `\mathfrak{Tor}` 写成 `\mathfrak{Cor}`。300dpi 裁片确认字母、复形指标、张量底环及 Tor。印刷页脚 171 未录入 Markdown。
- 页内修复状态：待全篇审计结束后逐处修正 Tor、S/1/Q′、complex bullets、同构下标和交换图，再按两张裁片回核；未修改 Markdown。

### PDF p.39（印刷 p.172）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:29 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p039.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p039_proof_6103.png`、`audit/300dpi/Grothendieck_1961_ega3_p039_remarks_6103.png`。
- 核对：Proposition (6.10.1) 仿射证明的 Cartan–Eilenberg 复形构造；Corollary (6.10.2) 的有界性陈述；Remark (6.10.3)(i) 的谱序列及 (ii) 的同伦复形同构和交换图。
- 结果：**FAIL**。Proposition (6.10.1) 证明第 1221 行将 `\mathcal{Q}'=\widetilde{\mathcal{Q}}'` 的左端写成 `2'`。Corollary (6.10.2) 第 1223 行的 `\mathcal{P}_{\bullet}^{(i)}` 与 `\mathcal{R}_{\bullet}` 分别写成不带 bullet 的 `\mathcal{P}^{(i)}` 和 `R.`。Remark (6.10.3)(i) 第 1227 行把 hypertor `\mathfrak{Tor}_{\bullet}(\mathcal{R}_{\bullet},\mathcal{Q}')` 写为 `\mathcal{Eor}_{\bullet}(\mathcal{R}_{\bullet},2')`；同段第 1230 行谱序列项将 `\mathcal{Q}'_{\bullet}` 写为 `2'_{\bullet}`。Remark (ii) 第 1235 行把复形 `\mathcal{R}'_{\bullet}`、`\mathcal{R}_{\bullet}` 写成不带 bullet 的 `\mathcal{R}'`、`\mathcal{R}.`，并将 isomorphism 的右端错误地重复成 `\mathcal{H}_{\bullet}(\mathcal{R}'\otimes_S\mathcal{Q}')`；原页右端是 `\mathcal{H}_{\bullet}(\mathcal{R}_{\bullet}\otimes_S\mathcal{Q}')`。图 (6.10.3)(ii) 第 1238 行的四个张量底环印为大写 `S`，Markdown 均录为小写 `s`。300dpi 裁片确认 Q/Tor、复形指标、右端复形和大写底环。印刷页脚 172 保留在 Markdown 第 1241 行。
- 页内修复状态：待全篇审计结束后恢复 Q′、Tor、complex bullets、R/R′ 同构两端及张量底环，并按两张裁片回核；未修改 Markdown。

### PDF p.40（印刷 p.173）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:36 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p040.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p040_scholie_bases.png`、`audit/300dpi/Grothendieck_1961_ega3_p040_theorem_6105.png`。
- 核对：Remark (6.10.3)(iii) 的 exact sequence 与 functoriality；Scholie (6.10.4) 的 base-change data；Theorem (6.10.5) 的 complex objects、函子同构及其 base-change 定义。
- 结果：**FAIL**。Remark (iii) 第 1245 行把印刷 exact sequence 两端的数字 `0` 录成字母 `o`。Scholie (6.10.4) 第 1247 行把 homological functor 的变量 `\mathcal{Q}'_{\bullet}` 写成 `\mathcal{Z}'_{\bullet}`，同一行后面的 `\mathcal{Q}'_{\bullet}` 又写成 `2'`。第 1250 行定义 `X,f,\mathcal{P}` 及 `X',Y',f'` 时，印刷的各个张量/乘积基环 `S` 均被写作小写 `s`；第 1253 行把印刷 `\mathcal{H}^{\bullet}_{f'}`、`\mathcal{H}^{\bullet}_{f}` 都写成 `\mathcal{H}^{\bullet}_{j'}`，并将 `\mathcal{O}_{S'}`、`\mathcal{O}_{S}` 写成 `\mathcal{O}_{s'}`、`\mathcal{O}_{s}`。第 1255 行把 `\mathcal{P}_{\bullet}` 写为 `\mathcal{P}.`。Theorem (6.10.5) 第 1257 行的输入复形 `\mathcal{P}_{\bullet}` 和输出复形 `\mathcal{L}_{\bullet}` 均记成句点 `P.` / `L.` 而漏掉 bullet；公式 (6.10.5.1) 第 1260 行的 `\mathcal{Q}_{\bullet}` 误写为 `2_{\bullet}`。第 1266 行把页脚 `173` 当作该定义显示式的 `\tag{173}`；原页无此公式标签，173 是本页页码。300dpi 裁片确认零、Q′、复形指标、base `S` 与页码位置。
- 页内修复状态：待全篇审计结束后逐处修正 0/Q′、base `S`、函子下标、complex bullets 与页码标签，并按两张裁片回核；未修改 Markdown。

### PDF p.41（印刷 p.174）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:41 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p041.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p041_6105_4_Q.png`。
- 核对：Theorem (6.10.5) 的 (6.10.5.2)/(6.10.5.3) 同构、(6.10.5.4) 及证明；Remark (6.10.6) 的同调/导出函子对应和上界结论；并确认页尾跨页句子的切分。
- 结果：**FAIL**。第 1286 行 (6.10.5.4) 两处印刷的复形 `\mathcal{Q}_{\bullet}` 均被写成 `2_{\bullet}`。本页余下核对的同构、交换图和 Remark (6.10.6) 内容与原页相符。印刷页脚 174 未录入 Markdown；句子 “Le complexe ... ne paraît posséder aucune” 在 Markdown 第 1293 行保留，后续接在第 1295 行，符合跨页边界。
- 页内修复状态：待全篇审计结束后将 (6.10.5.4) 的两个 `2_{\bullet}` 恢复为 `\mathcal{Q}_{\bullet}`，并按 300dpi 裁片回核；Markdown 未修改。

### PDF p.42（印刷 p.175）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:47 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p042.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p042_Q_complex.png`。
- 核对：Remark (6.10.6) 跨页末句；§7 标题、§7.1 的起始说明及 (7.1.1)/(7.1.2) 的函子和环作用公式；检查 (7.1.3) 在本页出现的开头。
- 结果：**FAIL**。Remark (6.10.6) 的续句第 1295 行把复形 `\mathcal{L}_{\bullet}` 写成 `\mathcal{L}.`，把公式两处 `\mathcal{Q}_{\bullet}` 均写成 `2.`，并在结尾把函子变量 `\mathcal{Q}_{\bullet}` 截成 `\mathcal{Q}`。300dpi 裁片确认印刷字形为 Q。其余在本页核对的 §7/§7.1 标题、(7.1.1)/(7.1.2) 和 (7.1.3) 开头文字相符；印刷页脚 175 未录入 Markdown。
- 页内修复状态：待全篇审计结束后修复复形 L/Q 的下标和公式中的两处 Q，并按 300dpi 裁片回核；Markdown 未修改。

### PDF p.43（印刷 p.176）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:51 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p043.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p043_localization_labels.png`、`audit/300dpi/Grothendieck_1961_ega3_p043_tensor_product_opening.png`。
- 核对：§7.1.3 的标量扩张续段；(7.1.4.1)/(7.1.4.2) 的局部化同构、证明与引用号；Proposition (7.1.5)；§7.2 与 (7.2.1) 在页尾的开头。
- 结果：**FAIL**。第 1321 行的定位引用应为 `(0_{I},1.6.1)`、`(0_{I},1.4.5)` 和公式 `(7.1.4.1)`；Markdown 分别把数字 1 写成字母 `i`，包括重复引用处的 `(7.i.4.i)`。本页其余核对的 (7.1.3) 续文、(7.1.4.1)/(7.1.4.2) 公式与证明、Proposition (7.1.5) 及 (7.2.1) 页尾内容相符。印刷页脚 176 未录入 Markdown。
- 页内修复状态：待全篇审计结束后恢复 `1.6.1`、`1.4.5` 和两处 `(7.1.4.1)` 引用中的数字 1，并按定位裁片回核；未修改 Markdown。

### PDF p.44（印刷 p.177）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 02:56 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p044.png`（pngmono 150dpi）。
- 核对：§7.2.1 的双线性映射表征续段、(7.2.2.1)/(7.2.2.2) 的自然同态与交换图，以及 (7.2.3)/(7.2.3.1) 的一般化同态。
- 结果：**PASS±**。本页核对的正文、映射条件、公式和交换图均与 PDF 原页相符。印刷页脚 177 未录入 Markdown，属版面信息；Markdown 随后的嵌入图位于该页正文之后，留到对应后续 PDF 页核对。
- 页内修复状态：无内容修复；未修改 Markdown。

### PDF p.45（印刷 p.178）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 03:05 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p045.png`（pngmono 150dpi）；Markdown 嵌入图 `Grothendieck_1961_ega3_mineru/Grothendieck_1961_ega3/images/page_44_image_5.jpg`（diagram (7.2.3.3)）。
- 核对：(7.2.3.2) 标量扩张映射；交换图 (7.2.3.3) 的箭头、端点和标签；Lemma (7.2.4)、Proposition (7.2.5) 的条件列表与证明开头。
- 结果：**PASS±**。本页所核的正文、公式、条件和 (7.2.3.3) 图示均与 PDF 印刷原页相符；Markdown 中嵌入的 `page_44_image_5.jpg` 与原页图示一致。印刷页脚 178 未录入 Markdown，属版面信息。
- 页内修复状态：无内容修复；未修改 Markdown。

### PDF p.46（印刷 p.179）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 03:11 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p046.png`（pngmono 150dpi）。
- 核对：Proposition (7.2.5) 证明中自由分解的自然图；Lemma (7.2.5.1) 的 epimorphism 论证；Remark (7.2.6) 的右模识别；Proposition (7.2.7) 的假设和条件 (d)。
- 结果：**FAIL**。第 1413 行条件 (b′) 的同态印为 `t_M`，Markdown 写成 `t_{\mathbb{M}}`；第 1425 行“lemma of five”结论中的 `t_M` 也写成 `t_{\mathbb{M}}`。PDF p.46 原页图确认这里是普通变量 M，不是 double-struck M。其余本页核对的证明文字、交换图、对象记号和 Proposition (7.2.7)(d) 条件与原页相符。印刷页脚 179 未录入 Markdown，属版面信息。
- 页内修复状态：待全篇审计结束后恢复两处 `t_M` 的变量字形；未修改 Markdown。

### PDF p.47（印刷 p.180）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 03:20 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p047.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p047_first_exact_sequence.png`、`audit/300dpi/Grothendieck_1961_ega3_p047_second_exact_sequence.png`。
- 核对：Proposition (7.2.7) 归纳证明中的两条 exact sequence、比较图和 epimorphism 结论；§7.3 Proposition (7.3.1) 的开头及其条件 (a)/(b)。
- 结果：**FAIL**。第 1446 行 exact sequence 两端的数字 `0` 都写成字母 `o`；第 1455 行另一 exact sequence 两端也都误录为 `o`；第 1458 行 diagram 首行的末端 `0` 同样写成 `o`。第 1461 行三个 homomorphism 下标原为普通变量 `M`、`M''`，Markdown 写成 double-struck `\mathbb{M}`、`\mathbb{M}''`。第 1465 行的 homological functor 印为 `T_{\bullet}`，Markdown 写成 `T.`，丢失了复形下标 bullet。页码 180 保留在 Markdown 第 1471 行；其后才接 PDF p.48 的 (7.3.1) 后续条件，符合页边界和抽取顺序。
- 页内修复状态：待全篇审计结束后逐处恢复五个零、homomorphism 下标变量字形和 `T_{\bullet}`，按两张裁片回核；未修改 Markdown。

### PDF p.48（印刷 p.181）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 03:28 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p048.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p048_exact_sequences.png`、`audit/300dpi/Grothendieck_1961_ega3_p048_7331_label.png`、`audit/300dpi/Grothendieck_1961_ega3_p048_7351_formula.png`。
- 核对：Proposition (7.3.1) 的后续条件与推论；Corollary (7.3.2) 的非零元断言；Proposition (7.3.3) 条件清单、公式 (7.3.3.1)、等价性论证；Corollary (7.3.4) 与 Proposition (7.3.5) 在本页的部分。
- 结果：**FAIL**。第 1489 行 exact sequence 两端的数字 `0` 均录成字母 `o`；Corollary (7.3.2) 第 1491 行两处非零判据也把 `\ne0` 写成 `\neq o`。Proposition (7.3.3) 第 1495 行的 homological functor 原印为 `T_{\bullet}`，Markdown 写成 `T.`，漏掉了 bullet。公式 (7.3.3.1) 的编号在第 1508 行作为独立 display `(7\cdot3\cdot3\cdot\mathbf{1})` 脱离公式呈现，而原页将 `(7.3.3.1)` 作为下一条同态公式的标签。印刷页脚 181 未录入 Markdown。300dpi 裁片确认数字零和公式编号/位置。
- 页内修复状态：待全篇审计结束后恢复 exact-sequence/非零判据的数字零，补回 `T_{\bullet}` 并将 (7.3.3.1) 标签与公式正确对应，按三张裁片回核；未修改 Markdown。

### PDF p.49（印刷 p.182）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 03:34 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p049.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p049_7352_label.png`、`audit/300dpi/Grothendieck_1961_ega3_p049_exact_zeroes.png`。
- 核对：Corollary (7.3.4) 与 Proposition (7.3.5) 的条件和 length 公式；Lemma (7.3.5.3) 的 exact-sequence inequality、equality criterion 与 proof estimate.
- 结果：**FAIL**。Proposition (7.3.5)(j) 的公式号印为 `(7.3.5.2)` 并标在 `long(T_p(A))=d\cdot long(A)` 前；Markdown 第 1546 行把编号单独排成 `(7\cdot3\cdot5\cdot2)`，与后面的未编号公式分离。Lemma (7.3.5.3) 第 1555 行 exact sequence 两端的数字 `0` 都被写成字母 `o`；第 1564 行 equality criterion 的序列两端也都将 `0` 写成 `o`。300dpi 裁片确认公式编号、零和序列边界。印刷页脚 182 在 Markdown 第 1575 行保留。
- 页内修复状态：待全篇审计结束后将 (7.3.5.2) 标签与公式相连，并恢复 Lemma 两条序列中的四个数字零，按两张裁片回核；未修改 Markdown。

### PDF p.50（印刷 p.183）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 03:40 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p050.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p050_exact_sequence_zero.png`、`audit/300dpi/Grothendieck_1961_ega3_p050_T_homological.png`。
- 核对：Lemma (7.3.5.3) 等号成立条件、(7.3.5.7)/(7.3.5.8) 的证明；Lemma (7.3.6) 的 exactness criterion；Proposition (7.3.7) 的开头及等价条件。
- 结果：**FAIL**。Lemma (7.3.5.7) 第 1589 行 exact sequence 两端印为数字 `0`，Markdown 写成字母 `o`；第 1598 行的 (7.3.5.8) 两端也同样误作 `o`；第 1601 行将 `\operatorname{Tor}_{1}^{A}(N,k)=0` 写成 `=o`。Lemma (7.3.6) 第 1603 行及 Proposition (7.3.7) 第 1611 行都将印刷复形函子 `T_{\bullet}` 记成 `T.`，漏掉 bullet。300dpi 裁片确认五处零及两个 bullet。印刷页脚 183 未录入 Markdown；接在其后第 1621 行的 (7.3.8) 属 PDF p.51。
- 页内修复状态：待全篇审计结束后恢复五个数字零和两个 `T_{\bullet}` 记号，并按两张裁片回核；未修改 Markdown。

### PDF p.51（印刷 p.184）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 03:47 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p051.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p051_739_zeros.png`、`audit/300dpi/Grothendieck_1961_ega3_p051_7310_recurrence.png`。
- 核对：§7.3.8 的 homological functor 延拓；Corollaries (7.3.9)/(7.3.10) 的 localization 与 generic-point 论证至本页边界；检验基环参数、非零条件、recurrence indices 和 exact sequence。
- 结果：**FAIL**。第 1621 行的 functor 印为 `T_{\bullet}`，Markdown 记成 `T.`；第 1623 行同一 functor 也漏掉 bullet。第 1627 行把 `T_i\ne0` 及 `A-\{0\}` 中的两个零写成 `o`。Corollary (7.3.10) 证明第 1631 行又将 `f_p\in B-\{0\}` 写成 `B-\{o\}`，把递归初值 `f_p=1` 写成 `f_p=I`，把 `N=p+1` 写成 `N=p+I`，并将 exact sequence `0\to p\to A\to A/p\to0` 两端录成字母 `o`；同一行后面 `f_N\in B-\{0\}` 也将零写成 `o`。页底印刷页码 184 未录入 Markdown。第 1631 行末尾的 “Si la proposition est” 是 p.51 的截断边界，后续证明留待 PDF p.52 核对。300dpi 裁片确认零、1/I 与 T-bullet 字形。
- 页内修复状态：待全篇审计结束后恢复 `T_{\bullet}`、六个数字零、`f_p=1` 与 `N=p+1`；按两张裁片回核。Markdown 未修改。

### PDF p.52（印刷 p.185）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 03:53 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p052.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p052_7311_rank.png`、`audit/300dpi/Grothendieck_1961_ega3_p052_7411_footer.png`。
- 核对：Corollary (7.3.10) 证明越过页界后的结论；Proposition (7.3.11) 条件 d/d′ 与归纳证明；§7.4 标题、(7.4.1) 的复形假设及首个同态公式。
- 结果：**FAIL**。第 1635 行 Proposition (7.3.11) 的 homological functor 印为 `T_{\bullet}`，Markdown 写成 `T.`。第 1655 行 §7.4 标题的 `\mathcal{H}_{\bullet}(\mathcal{P}_{\bullet}\otimes_A M)` 被缩成 `H.(P.\otimes A M)`；第 1657 行同样将输入复形 `\mathcal{P}_{\bullet}` 写为 `P.`。公式 (7.4.1.1) 原标号是 `(7.4.1.1)`，Markdown 第 1659 行写成 `(7.4.I.I)`，将数字 1 转成字母 I；第 1662 行又把印刷页脚 185 当作公式 `\tag{185}`，而本页原式没有该 tag。300dpi 裁片确认 T/P 复形标记、公式号和页码的位置。第 1633 行起承接 p.51 的 Corollary (7.3.10) 证明，本页结束于 (7.4.1.1)。
- 页内修复状态：待全篇审计结束后恢复 T/P 下标、(7.4.1.1) 公式号并移除误作公式标签的页脚 185，按两张裁片回核；未修改 Markdown。

### PDF p.53（印刷 p.186）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 03:59 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p053.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p053_7412_13.png`、`audit/300dpi/Grothendieck_1961_ega3_p053_7421_diagram.png`。
- 核对：Proposition (7.4.2) 条件 (a)–(c)；自然 exact sequence 与比较图 (7.4.2.1)；证明中由 `c)` 推出 `a)` 的 homology boundary argument。
- 结果：**FAIL**。第 1685 行把印刷的复形 `\mathbf{P}'_{\bullet}` 写成 `\mathbf{P}'.`，漏掉 bullet。第 1696 行自然 exact sequence 的首项数字 `0` 写成 `o`；第 1702 行比较图上下两行开头的两个 `0` 也均写成 `o`；第 1705 行 `0\to M'\to M\to M''\to0` 两端再将数字 `0` 误作 `o`。此外，第 1702 行的图 (7.4.2.1) 漏掉印刷在右侧 `P_{p-1}\otimes M\to P_{p-1}\otimes N` 上的竖直映射 `w`。300dpi 裁片确认五个零、复形下标及缺失的第三条竖箭头。印刷页脚 186 在 Markdown 第 1711 行保留。
- 页内修复状态：待全篇审计结束后补回 `P'_{\bullet}`、五个数字零和 comparison diagram 的 `w` 箭头，按两张裁片回核；未修改 Markdown。

### PDF p.54（印刷 p.187）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 04:05 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p054.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p054_exact_sequence_zeros.png`、`audit/300dpi/Grothendieck_1961_ega3_p054_7414_start.png`。
- 核对：Proposition (7.4.2)(b)→(c) 的复形重构与 cycle/boundary identifications；Corollary (7.4.3) 两种平坦性判据；Proposition (7.4.4) 开头的复形假设。
- 结果：**FAIL**。第 1716 行短 exact sequence 两端的数字 `0` 均写成 `o`；第 1725 行零微分 `0` 也写成 `o`；第 1733、1742 行两条 exact sequence 的四个端点数字 `0` 均写成 `o`；第 1749 行 `\mathrm{H}_{i}(\mathcal{P}_{\bullet})=0` 的零写成字母 `o`。Proposition (7.4.4) 第 1749 行将输入复形 `\mathcal{P}_{\bullet}` 写成 `P.`，第 1751 行再次将 `\mathcal{P}_{\bullet}` 写成 `P.`。300dpi 裁片确认这些零和复形 bullet。印刷页脚 187 未录入 Markdown。
- 页内修复状态：待全篇审计结束后恢复八个数字零和 Proposition (7.4.4) 的复形 bullet，并按两张裁片回核；未修改 Markdown。

### PDF p.55（印刷 p.188）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 04:11 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p055.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p055_representing_sequences.png`。
- 核对：Proposition (7.4.6) 的 Hom 表示构造，尤其是由 (d_{p+1}=0) 得到的 exact sequences (0\to T_p(M)\to P_p\otimes M\to P_{p-1}\otimes M)、(0\to Q'\to P_p\to P_{p-1}) 与其对偶序列。
- 结果：**FAIL**。第 1772 行同调列首的数字 `0` 被写成 `o`。第 1775 行两个相邻 exact sequences 中，首/末端数字 `0` 共两处写成 `o`/`\mathtt{o}`。第 1778 行 Hom exact sequence 的首端数字 `0` 又写成 `o`。300dpi 裁片确认四处均为数字零；印刷页脚 188 未录入 Markdown，后续叙述从第 1781 行接续到下一 PDF 页。
- 页内修复状态：待全篇审计结束后将四处 `o`/`\mathtt{o}` 改为数字 `0`，按裁片回核；未修改 Markdown。

### PDF p.56（印刷 p.189）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 04:20 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p056.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p056_identity_dual.png`、`audit/300dpi/Grothendieck_1961_ega3_p056_remark_748_symbols.png`。
- 核对：Proposition (7.4.6) 的 Hom 表示构造结尾；Proposition (7.4.7) 完备化同构及其核/余核引理；Remark (7.4.8) 的 Tor 谱序列和未定性说明。
- 结果：**FAIL**。第 1781 行将两处印刷恒等映射 `I` 写为 `\mathfrak{i}`。Remark (7.4.8) 第 1805 行把 `\mathcal{Q}'` 多处写成 `2'`，将 hypertor `\mathfrak{Tor}_{\bullet}` 写成 `\mathcal{Eor}_{\bullet}`，并把张量底环大写 `S` 录成小写 `s`；谱序列 E₂ 项中的 `\mathcal{H}_{q''}(\mathcal{Q}'_{\bullet})` 也把 Q 写为 2。该行结尾把 `\mathcal{P}'_{\bullet}` 写成 `P'_{\otimes}`，丢失了 complex bullet 并把它并入 tensor 符号。印刷页脚 189 在 Markdown 第 1807 行保留。
- 页内修复状态：待全篇审计结束后恢复恒等映射 `I`、Tor/Q′、大写 `S` 和复杂指标 `P'_{\bullet}`，按两张裁片回核；Markdown 未修改。

### PDF p.57（印刷 p.190）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 04:27 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p057.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p057_corollary_7353_zero.png`。
- 核对：§7.5.1 完备化与 (7.5.1.1)；Proposition (7.5.2) 的判别条件及精确性证明；Corollary (7.5.3) 的零函子结论。
- 结果：**FAIL**。Corollary (7.5.3) 第 1837 行把原文两处 `T(k)=0`、`T(M)=0` 的数字零都录成了字母 `o`。300dpi 裁片确认原页为 0。印刷页脚 190 未录入 Markdown。
- 页内修复状态：待全篇审计结束后将第 1837 行的两个 `o` 恢复为 0，并按裁片回核；Markdown 未修改。

### PDF p.58（印刷 p.191）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 04:38 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p058.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p058_corollary_755_zeros.png`。
- 核对：Corollary (7.5.3) 的证明续段；Proposition (7.5.4) 的等价条件；Corollaries (7.5.5)/(7.5.6) 的零函子、张量同构与平坦性判据。
- 结果：**FAIL**。Corollary (7.5.5) 第 1856 行 `T_p(k)=0` 把数字零写成字母 `o`；第 1858 行 `T_{p-1}(k)=T_{p+1}(k)=0` 两处零也都写成 `o`。其余本页核对的完备化同构、判据正文及公式与原页相符。印刷页脚 191 未录入 Markdown。
- 页内修复状态：待全篇审计结束后修复 Corollary (7.5.5) 的三个数字零，并按裁片回核；Markdown 未修改。

### PDF p.59（印刷 p.192）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 04:47 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p059.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p059_exact_sequence_751.png`、`audit/300dpi/Grothendieck_1961_ega3_p059_7611_label.png`。
- 核对：Corollary (7.5.6) 的 uniformizer exact sequence 与 induced homology sequence；Remark (7.5.7) 对 homological functor 的引用；§7.6 Proposition (7.6.1)/(7.6.2) 的 base-change exactness 及其首公式。
- 结果：**FAIL**。Corollary (7.5.6) 第 1874 行 exact sequence 的两个端点数字 `0` 均被录成字母 `o`。Remark (7.5.7) 第 1882 行的 printed homological complex `T_{\bullet}` 被写成 `T.`，漏掉 bullet。Proposition (7.6.1) 公式第 1891 行标签原为 `(7.6.1.1)`，Markdown 写成 `(7.6.x.x)`。300dpi 裁片确认 exact sequence 的零及公式标签。印刷页脚 192 未录入 Markdown；本页末尾的 (7.6.2) 证明继续到 PDF p.60。
- 页内修复状态：待全篇审计结束后恢复两个数字零、`T_{\bullet}` 和 (7.6.1.1) 标签，再按两张裁片回核；未修改 Markdown。

### PDF p.60（印刷 p.193）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 04:55 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p060.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p060_reference.png`、`audit/300dpi/Grothendieck_1961_ega3_p060_exact_sequences.png`、`audit/300dpi/Grothendieck_1961_ega3_p060_identity.png`、`audit/300dpi/Grothendieck_1961_ega3_p060_footer.png`。
- 核对：Proposition (7.6.3) 的 Tor 精确列、三条张量化精确序列及证明；Remark (7.6.4)(i) 的谱序列首项公式。
- 结果：**FAIL**。第 1904 行交叉引用 `(0_I, 6.2.I)` 的末位应为数字 `1`。第 1911、1917、1925、1929、1933、1945 行共有 14 个数字 `0` 被录成小写字母 `o`。第 1922–1933 行的三个精确序列标签错位：空置的 `(7.6.3.2)` 应标在第一个序列，现标作 `(7.6.3.3)`；第二个现标作 `(7.6.3.4)`；第三个序列漏标，正确标签依次为 `(7.6.3.2)`、`(7.6.3.3)`、`(7.6.3.4)`。第 1936 行四处印刷恒等映射 `I` 被录成小写 `i`。第 1953 行把印刷页脚 `193` 错并入未编号的谱序列公式，形成伪 `\tag{193}`。300dpi 裁片分别确认引文、标签与零、恒等映射、公式及页脚；第 1956 行起属于下一 PDF 页，不纳入本页。
- 页内修复状态：待全篇审计结束后更正引文末位、14 个数字零、三条序列标签、四处恒等映射，并从谱序列公式移除伪标签；Markdown 未修改。

### PDF p.61（印刷 p.194）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:02 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p061.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p061_spectral_sequence.png`、`audit/300dpi/Grothendieck_1961_ega3_p061_label_7651.png`、`audit/300dpi/Grothendieck_1961_ega3_p061_ordinals.png`、`audit/300dpi/Grothendieck_1961_ega3_p061_footer.png`。
- 核对：Remark (7.6.4)(i) 的退化谱序列短正合列；Corollary (7.6.5) 两个秩公式及等号条件；(7.6.6) 的秩函数定义和 Lemma (7.6.7) 的基变换公式。
- 结果：**FAIL**。第 1959 行短正合列两个端点的数字 `0` 均录成字母 `o`。第 1969 行不等式公式的标签被写成 `(7.6.5.i)`，原文是 `(7.6.5.1)`。第 1986 行把条件序号中的法文序数标记 `1°`、`2°` 录成 `1^{0}`、`2^{0}`。第 2004 行将印刷页脚 `194` 当作正文插在标签 `(7.6.7.1)` 与公式之间；原页中公式完整排在页脚之前，页码在页面左下方。裁片确认两个零、公式标签、序数标记及页脚位置；第 2010 行起为下一 PDF 页内容。
- 页内修复状态：待全篇审计结束后把两个 `o` 改为数字零、将标签末位改为 `1`、恢复 `1^\circ` 与 `2^\circ`，并从正文删除页脚 `194`；Markdown 未修改。

### PDF p.62（印刷 p.195）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:06 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p062.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p062_theorem.png`、`audit/300dpi/Grothendieck_1961_ega3_p062_corollary.png`。
- 核对：Lemma (7.6.7) 证明续段、Lemma (7.6.8)、Theorem (7.6.9) 及 Corollary (7.6.10)(i) 的两条秩不等式。
- 结果：**FAIL**。第 2024 行 Theorem (7.6.9) 定义中，`T_\bullet`、`H_\bullet` 和 `P_\bullet` 的复形指标 bullet 均被简化为句点。第 2034 行两处范围均把初始数字 `1` 误录为字母 `i`：`(i \leqslant i \leqslant r)` 应为 `(1 \leqslant i \leqslant r)`。第 2010 行的标签 `(7.6.10.2)` 被提前放在 Lemma (7.6.7) 证明之前；它实际属于第 2045 行 Corollary (7.6.10)(i) 中 “En particulier” 后的第二条不等式，故该公式当前漏标。印刷页脚 195 未录入正文；第 2052 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后恢复三个 `_\bullet` 指标、两处范围中的数字 `1`，并把 `(7.6.10.2)` 移至第二条不等式；Markdown 未修改。

### PDF p.63（印刷 p.196）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:09 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p063.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p063_conditions.png`、`audit/300dpi/Grothendieck_1961_ega3_p063_sequence_footer.png`、`audit/300dpi/Grothendieck_1961_ega3_p063_transpose_map.png`。
- 核对：Corollary (7.6.10)(ii) 的秩条件；Remark (7.6.11) 的不等式与等价条件 (a)–(c)；Lemma (7.6.11.6) 的精确列。
- 结果：**FAIL**。第 2059 行条件范围把数字 `1` 写成大写字母 `I`。第 2103 行 Lemma (7.6.11.6) 精确列的首尾两个数字 `0` 均录成字母 `o`。第 2098 行将转置映射 `^{t}d` 写成 `t_d`，把原文上标的转置记号 `t` 错置为下标 `d`。第 2106 行将印刷页脚 `196` 当作正文置于精确列之后；原页页码在页面左下方。300dpi 裁片确认范围首位、零端点、转置映射及页脚位置；第 2108 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后将范围首位恢复为 `1`、修复两个数字零、恢复转置映射 `^{t}d`，并从正文删除页脚 `196`；Markdown 未修改。

### PDF p.64（印刷 p.197）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:16 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p064.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p064_exact_sequence.png`、`audit/300dpi/Grothendieck_1961_ega3_p064_reference.png`、`audit/300dpi/Grothendieck_1961_ega3_p064_exterior_power.png`。
- 核对：Lemma (7.6.11.6) 证明及 (7.6.11.7) 精确列；等价条件 (a)–(c) 的证明；正则局部环反例说明；§7.7 开始与 (7.7.1) 假设。
- 结果：**FAIL**。第 2108 行六个 exact-sequence 端点数字 `0` 均录成字母 `o`；同一行两处恒等映射 `I` 被写成数字 `1`。第 2110 行 exact sequence 末端的数字 `0` 也写成了 `o`。第 2122 行交叉引用 `(7.6.II.2)` 中的两个数字 `1` 被录成大写 `I`，应为 `(7.6.11.2)`。第 2124 行把印刷标点 “dimension n; on sait alors” 录成 “dimension n'y on sait alors”。第 2126 行外幂 `\wedge(\mathfrak{m}/\mathfrak{m}^{2})` 漏掉上标外幂次数 `i`。印刷页脚 197 未插入正文；第 2134 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后修复七个数字零、两处恒等映射 `I`、交叉引用、标点，并在外幂符号上恢复上标 `i`；Markdown 未修改。

### PDF p.65（印刷 p.198）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:20 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p065.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p065_functor_formula.png`、`audit/300dpi/Grothendieck_1961_ega3_p065_base_change.png`。
- 核对：函子 `\mathcal{T}_{\bullet}` 的定义与次数约定；基变换下的复形及函子 (7.7.2.1)；(7.7.2.2) 与 (7.7.3.1) 的限制和自然映射。
- 结果：**FAIL**。第 2141 行把公式右侧的定义域说明 “pour n∈Z” 错排为独立伪公式 `\mathbf{z}`，并把说明放入 `\tag{pour n∈Z,}`。第 2146 行新复形 `\mathcal P_*` 的复形指标将印刷 bullet 录成星号，应为 `\mathcal P_{\bullet}`。第 2149 行 (7.7.2.1) 左侧张量项把基变换后的复形 `\mathcal P'^{\bullet}` 漏录 prime，写成 `\mathcal P^{\bullet}`；等式右侧无 prime 与原文相符。页脚 198 未录入正文；第 2169 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后移除伪公式并将 “pour n∈Z” 恢复为定义域说明、把 `P_*` 改为 `P_{\bullet}`，并在 (7.7.2.1) 左侧复形补回 prime；Markdown 未修改。

### PDF p.66（印刷 p.199）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:24 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p066.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p066_7732_zero_degree.png`、`audit/300dpi/Grothendieck_1961_ega3_p066_theorem_bullets.png`。
- 核对：自然变换 (7.7.3.1) 的限制交换图与基变换映射 (7.7.3.2)；§7.7.4 的复形表示；Theorem (7.7.5) 的半连续性命题与公式 (7.7.5.1)。
- 结果：**FAIL**。第 2180 行将 degree-zero term 的数字 `0` 录成字母 `o`。第 2190 行把复形 `\mathcal{P}_{\bullet}` 写成 `\mathcal{P}.`；第 2192 行的定理假设也把 `\mathcal{P}_{\bullet}` 写成 `P.`，并在同一行将 homological functor `\mathcal{T}_{\bullet}(\mathcal{M})` 写成无 bullet 的 `\mathcal{T}(\mathcal{M})`。裁片确认 degree 0 和两处复形/函子 bullet；页脚 199 未录入正文，第 2204 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后恢复 degree `0`，并在第 2190、2192 行的复形和同调函子中补回 bullet；Markdown 未修改。

### PDF p.67（印刷 p.200）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:28 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p067.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p067_exchange_conditions.png`、`audit/300dpi/Grothendieck_1961_ega3_p067_exact_sequences.png`、`audit/300dpi/Grothendieck_1961_ega3_p067_basechange.png`。
- 核对：Theorem (7.7.5) 的交换性质等价条件 (a)–(d) 与 (7.7.5.2)/(7.7.5.3)；由 a) 推出 c) 的延拓证明；b') 的表示对象；a) 与 d) 的仿射情形证明起始。
- 结果：**FAIL**。第 2214 行 b') 条件将表示对象 `\mathcal{Q}` 写成数字 `2`；第 2217 行 (7.7.5.2) 的 Hom 首个自变量也写成 `2`，应为 `\mathcal{Q}`。第 2225 行把公式标签 `(7.7.5.3)` 展开为独立的乘法式 `(7 \cdot 7 \cdot 5 \cdot 3)`；原页是公式左侧标签，后续行已另给该公式正确标签。第 2234 行两条 exact sequence 的四个端点数字 `0` 均录成字母 `o`。第 2238 行仿射情形的基变换函子写为 `T_{\bullet}^{A}`，原文为 `T_{\bullet}^{A'}`，漏掉 A' 的 prime。印刷页脚 200 未录入正文；第 2240 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后恢复两个 `\mathcal{Q}`、移除伪乘法标签、修复四个数字零，并将第 2238 行函子补为 `T_{\bullet}^{A'}`；Markdown 未修改。

### PDF p.68（印刷 p.201）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:32 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p068.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p068_theorem_Q.png`、`audit/300dpi/Grothendieck_1961_ega3_p068_corollary_Q_labels.png`、`audit/300dpi/Grothendieck_1961_ega3_p068_footer_tag.png`。
- 核对：Theorem (7.7.6) 的表示对象与两个自然同构；Corollary (7.7.7) 的表示对象、两个同构标签及其证明开头的函子映射。
- 结果：**FAIL**。Theorem (7.7.6) 第 2248、2251、2257 行三处表示对象 `\mathcal{Q}` 均被录成数字 `2`。Corollary (7.7.7) 证明第 2278、2281 行的 `Q`/`Q'` 共四处也被录成 `2`/`2'`。第 2271 行把同构标签 `(7.7.7.1)` 的末位数字 `1` 写成 `I`，并把第二个标签 `(7.7.7.2)` 错并入这一独立伪公式；原页分别把 (7.7.7.1)、(7.7.7.2) 标在两个同构关系左侧。第 2287 行的 `\tag{201}` 来自印刷页脚 201；该页末公式为未编号函子映射，页码在原页右下角。裁片确认 Q、标签和页脚位置；第 2290 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后修复七处 `Q/Q'`、将两个标签分别归回对应同构，并从第 2287 行函子映射移除伪页脚标签；Markdown 未修改。

### PDF p.69（印刷 p.202）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:36 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p069.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p069_q_representation.png`、`audit/300dpi/Grothendieck_1961_ega3_p069_corollary_hom.png`、`audit/300dpi/Grothendieck_1961_ega3_p069_kernel_hom.png`。
- 核对：Corollary (7.7.7) 证明中从自然变换构造表示对象的交换图；Corollary (7.7.8) 两个函子的定义、表示同构及其由有限自由表示导出的证明。
- 结果：**FAIL**。第 2290 行将表示对象箭头 `v:Q′→Q` 写成 `v:2′→2`。第 2299 行首个 Hom 项的结构层写成 `O_Y`，原文应为 `O_X`；同一行另一个 Hom 项以及第 2319、2325 行多处把大写 `X` 写成小写 `x`，结构层下标均应为 `O_X`。300dpi 裁片核实 Q/Q' 与 X/Y 层指标；印刷页脚 202 未录入正文，第 2330 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后将第 2290 行的 `2′→2` 恢复为 `Q′→Q`，更正第 2299 行 Hom 的层为 `O_X`，并将第 2299、2319、2325 行相关小写 `x` 改为大写 `X`；Markdown 未修改。

### PDF p.70（印刷 p.203）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:41 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p070.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p070_q_reference.png`、`audit/300dpi/Grothendieck_1961_ega3_p070_local_functors.png`。
- 核对：Remarques (7.7.9)(i) 的表示对象基变换公式与仿射伴随 Hom 同构；(7.7.9)(ii)/(iii)；Proposition (7.7.10) 的局部正合性判据；Corollary (7.7.11) 的平坦基变换陈述。
- 结果：**FAIL**。第 2330 行对象列表中的 `Q` 被录成数字 `2`；第 2339 行 Hom 同构两侧的 `Q` 与 `g^*(Q)` 也分别被录成 `2` 与 `g^*(2)`。第 2342 行引用末位将数字 `1` 录成大写字母 `I`：原文为 `(0_I, 4.4.3.1)`。第 2350、2352、2354、2358 行共七处函子上标把 `O_y` 写成 `O y`，漏掉 O 的 y 下标；应为 `T_p^{O_y}`。300dpi 裁片核实 Q、引用末位与系数环下标。印刷页脚 203 未录入正文；第 2362 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后恢复三处 `Q`、将引用末位改为数字 `1`，并在七处函子系数环记号中补回 `O_y` 的下标；Markdown 未修改。

### PDF p.71（印刷 p.204）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:45 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p071.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p071_corollary_functor.png`、`audit/300dpi/Grothendieck_1961_ega3_p071_complex_equalities.png`、`audit/300dpi/Grothendieck_1961_ega3_p071_truncation_formula.png`。
- 核对：Corollary (7.7.11) 证明续段；Remarques (7.7.12)(i)/(ii) 的有限复形截断与替代函子定义；§7.8 开始及 Definition (7.8.1) 首段。
- 结果：**FAIL**。第 2362 行把函子系数环 `O_y` 写成 `c_y`。第 2364 行复形 `P_\bullet` 的指标 bullet 被写成句点；同一行同调等式两侧均写为 `L'_\bullet`，而原文右侧是未截断复形 `L_\bullet`。第 2364 行不等式范围末项写为大写 `I`，应为数字 `1`，即 `i_1-I` 应为 `i_1-1`。第 2366 行把单一非零项的 degree `0` 写成字母 `o`，并漏掉复形指标 bullet。第 2374 行仿射情形同调公式把 `L_\bullet` 录成 `L_\otimes`，丢失复形指标并与后续张量符号混淆。300dpi 裁片核实函子系数环、两处截断复形表达式、范围数字、degree 0 与张量公式；页脚 204 未录入正文，第 2380 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后将 `c_y` 恢复为 `O_y`、补回复形 bullet、把右侧同调复形改为未截断的 `L_\bullet`、将 `i_1-I` 改为 `i_1-1`、把 degree `o` 改为数字零，并恢复 `L_\bullet\otimes`；Markdown 未修改。

### PDF p.72（印刷 p.205）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:50 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p072.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p072_propositions.png`、`audit/300dpi/Grothendieck_1961_ega3_p072_prop784_formulas.png`。
- 核对：Definition (7.8.1) 的续文；(7.8.2)/(7.8.3) 对同调平坦性的局部判据；Proposition (7.8.4)(a)–(d) 及其长度和基变换公式。
- 结果：**FAIL**。第 2380、2382、2384、2388、2398、2400 行多处复形或同调函子指标把印刷 bullet 简化成逗点、句点或省略，涉及 `P_•` 与 `T_•`。第 2402 行系数环写成 `O y`，漏掉 y 下标，应为 `O_y`。第 2413 行将标签 (7.8.4.2) 拆成独立伪公式；原页将它作为左侧编号标在第 2417 行映射旁。第 2417 行该映射左端的上同调对象写成 `K^{-p}`，原文是 `H^{-p}`，且在限制符号 `|U` 后多出一个右括号。裁片核实函子下标、标签及 H/K 记号；印刷页脚 205 未录入正文，第 2428 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后恢复遗漏的 bullet、补回 `O_y` 下标、将标签 (7.8.4.2) 接回映射左侧、将 `K^{-p}` 改为 `H^{-p}` 并删除限制符号后的多余右括号；Markdown 未修改。

### PDF p.73（印刷 p.206）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 05:55 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p073.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p073_proposition_786_zeros.png`。
- 核对：Proposition (7.8.4) 的等价条件证明；Propositions (7.8.5) 与 (7.8.6)；Lemma (7.8.6.1) 的陈述开头。
- 结果：**FAIL**。第 2442 行 Proposition (7.8.6) 结论的维数把数字 `0` 录成字母 `o`；第 2444 行证明中由平坦性得到的 `T_{-1}=0` 也把末端零录成字母 `o`。300dpi 裁片核实命题的维数零与证明中的零函子值。印刷页脚 206 未录入正文；第 2448 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后将第 2442 行维数和第 2444 行函子值中的两个 `o` 改为数字 `0`；Markdown 未修改。

### PDF p.74（印刷 p.207）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 06:00 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p074.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p074_lemma_numbers.png`、`audit/300dpi/Grothendieck_1961_ega3_p074_corollary_Q.png`、`audit/300dpi/Grothendieck_1961_ega3_p074_corollary_789_proof.png`。
- 核对：Lemma (7.8.6.1) 的幂等元判据及连通分支论证；Corollaries (7.8.7)–(7.8.9)；Remarque (7.8.10)(i) 的 Stein 分解开头。
- 结果：**FAIL**。第 2448 行将“非零”中的数字 `0` 写成 `o`。第 2450 行幂等元判据另有五处数字 `0`/`1` 被写成字母 `o`/`i`；同一行引文末位把 volume 标记 `I` 写成数字 `1`，应为 `(0_I, 5.5.2)`。第 2476 行剩余域写成 `k(\mathcal{y})`，原文为 `k(y)`。第 2480、2483 行表示对象 `Q` 均写成数字 `2`。第 2486 行复形 bullet 被写成句点，degree `0` 被写成 `o`，而结构层 `O_X` 被写成小写 `O_x`。300dpi 裁片确认数字/字母字形、Q、剩余域与结构层；印刷页脚 207 未录入正文，第 2494 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后恢复 Lemma (7.8.6.1) 中六个零/一数字和 `(0_I, 5.5.2)` 引文，将 `k(\mathcal{y})` 改为 `k(y)`，把两处 `2` 改回 `Q`，并恢复第 2486 行复形 bullet、degree `0` 和大写 `O_X`；Markdown 未修改。

### PDF p.75（印刷 p.208）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 06:06 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p075.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p075_remark_Q_reference.png`、`audit/300dpi/Grothendieck_1961_ega3_p075_euler_formulas.png`。
- 核对：Remarques (7.8.10)(i)/(ii) 的 Stein factorization 与表示对象；(7.9.1.1)、Proposition (7.9.2) 的 Euler–Poincaré 等式、Corollary (7.9.3) 的局部常值函数；Theorem (7.9.4) 的开头。
- 结果：**FAIL**。第 2494 行 Bourbaki 引文把数值版本号中的数字写成字母 `I`：应为 `(II, 1.5.1)`，Markdown 为 `(II, I.5.I)`。第 2496 行表示对象 `Q` 两处均录成数字 `2`。第 2506 行 Proposition (7.9.2) 将 `P_\bullet`、`T_\bullet`、`H_\bullet` 等复形/同调族指标 bullet 平化成句点。第 2509 行 Euler 特征式两处 `(-1)^i` 中的数字 `1` 均写成大写 `I`。第 2517 行函数映射符号 `\mapsto` 被写成 `\sim`，且交错和符号 `(-1)^i` 中的数字 1 被写成小写字母 `r`。印刷页脚 208 未录入正文；第 2525 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后恢复引文中的两个数字 `1`、两处表示对象 `Q`、复形/同调族 bullet、两个交错和中的 `1`，并将函数定义符号改回 `\mapsto`；Markdown 未修改。

### PDF p.76（印刷 p.209）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 06:13 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p076.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p076_794_function.png`、`audit/300dpi/Grothendieck_1961_ega3_p076_796_additivity.png`、`audit/300dpi/Grothendieck_1961_ega3_p076_796_alternating_sum.png`。
- 核对：Theorem (7.9.4) 的局部常值函数；(7.9.5) 的 Euler–Poincaré 记号；(7.9.6) 短正合列下的可加性与复形长度归纳。
- 结果：**FAIL**。第 2525 行把 (7.9.4.1) 标签末位数字 `1` 写成大写 `I`，并拆成与第 2529 行函数公式分离的伪标签。第 2529 行函数对应符号写成 `\sim`，原文是指向值的函数箭头（`\rightsquigarrow`）。第 2536、2544 行中 `P_\bullet`、`T_\bullet` 等复形/同调函子的 bullet 被简化为句点。第 2553 行可加性公式标签末位把数字 `1` 写成字母 `r`。第 2565 行有限复形 Euler 特征公式把 `(-1)^i` 的底数数字 1 写成小写字母 `i`。裁片核实公式标签、箭头、复形 bullet、可加性标签及交错符号；印刷页脚 209 未录入正文，第 2568 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后把分离标签接回公式并恢复末位 `1`、将 `\sim` 换成函数箭头、恢复复形/同调函子 bullet、将 (7.9.6.1) 标签末位改为 `1`，并把 Euler 特征公式中的 `i` 改为 `1`；Markdown 未修改。

### PDF p.77（印刷 p.210）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 06:18 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p077.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p077_q_reference.png`、`audit/300dpi/Grothendieck_1961_ega3_p077_local_functor_tail.png`。
- 核对：Proposition (7.9.7) 基变换下的 Euler–Poincaré 函数；Proposition (7.9.8) 的唯一非零同调维数条件；Corollaries (7.9.9)/(7.9.10) 与其消失引理。
- 结果：**FAIL**。第 2576 行 Bourbaki 引文体号写成 `(0_1, 6.2.1)`，原文为 `(0_I, 6.2.1)`，将罗马卷号 I 误作数字 1。第 2580 行两处函子上标 `O_y` 写成 `O y`，漏掉 y 下标。第 2586 行末句将剩余域变量 `y` 写成花体大写 `Y`。第 2592 行把 `R^i f_*(F)=0` 的数字零录成字母 `o`。第 2598 行把复形 `P_\bullet` 的 bullet 平化为句点，把 degree `0` 写成 `o`，并将结构层 `O_X` 写成小写 `O_x`。300dpi 裁片确认引文、系数环下标、剩余域变量和零端点。印刷页脚 210 未录入正文；第 2602 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后恢复 `(0_I,6.2.1)` 引文、两处 `O_y` 系数环、普通小写 `y`、数字零、复形 bullet 和大写 `O_X`；Markdown 未修改。

### PDF p.78（印刷 p.211）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 06:24 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p078.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p078_label_7911.png`、`audit/300dpi/Grothendieck_1961_ega3_p078_degree_zero.png`。
- 核对：Proposition (7.9.11) 的 Hilbert 多项式标签与函数；(7.9.11) 证明及 (7.9.12.1)–(7.9.12.3) 的多项式性质；Corollary (7.9.13) 的陈述与证明开头。
- 结果：**FAIL**。第 2605 行 Proposition (7.9.11) 的公式标签把 (7.9.11.1) 中三个数字 `1` 均录成大写 `I`，写为 `(7.9.II.I)`。第 2610 行把单一非零项所在的 degree `0` 写成字母 `o`。300dpi 裁片核实标签的末两段和度数零。印刷页脚 211 未录入正文；第 2638 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后将第 2605 行标签的三处 `I` 恢复为数字 `1`，并将第 2610 行 degree `o` 改为数字 `0`；Markdown 未修改。

### PDF p.79（印刷 p.212）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 06:29 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p079.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p079_Rif.png`、`audit/300dpi/Grothendieck_1961_ega3_p079_degree_one.png`。
- 核对：Corollary (7.9.13) 的 vanishing criterion；Proposition (7.9.14) 的局部自由推出平坦性证明。
- 结果：**FAIL**。第 2638 行将直接像消失条件 `R^i f_*(\mathcal{F}(n))=0` 错写为 `R^{if}_*(\mathcal{F}(n))=0`，把 `f_*` 误并入上标。第 2642 行把生成次数“degree 1”中的数字 `1` 写成大写字母 `I`。300dpi 裁片确认直接像上标/算子及生成次数。印刷页脚 212 未录入正文；第 2644 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后将上标/函子写回 `R^i f_*(\mathcal{F}(n))`，并把 degree `I` 改成数字 `1`；Markdown 未修改。

### PDF p.80（索引页；印刷页脚 p.213）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 06:58 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p080.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p080_notations_index.png`。
- 核对：Index des notations 中第 6.3–7.9 节的 hypertor、Cor、Ab、T、EP 与 PH 符号条目及其章节定位。
- 结果：**FAIL**。第 2651 行将印刷 fraktur `\mathfrak{Cor}` 写成 calligraphic `\mathcal{Cor}`，并把第二个复形自变量印刷 Q 录成 Z。第 2655、2671 行把印刷 fraktur `\mathfrak{Tor}` 录成 calligraphic `\mathcal{Tor}`；第 2667 行第二个 S-base hypertor 条目又把 fraktur `\mathfrak{Tor}` 写成粗体 `\mathbf{Tor}`。第 2667 行两个 A-complex 的下标各录成双 bullet `L_{\bullet\bullet}`，原文每个复形各有一个 bullet。章节定位第 2651、2655 行的 (6.4.1)、(6.5.1) 和第 2683、2695 行的 (7.1.1)、(7.1.4) 把数字 1 写成大写 I。300dpi 裁片核实字体、Q/Z 字形、复形下标与编号；印刷页脚 213 未录入正文，第 2710 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后按原字形将 `\mathcal{Cor/Tor}` 改回 `\mathfrak{Cor/Tor}`、将 Z 形复形变量改回 Q、每个 A-complex 保留单一 bullet，并把列出的章节定位末位 I 改成数字 1；Markdown 未修改。

### PDF p.81（Index terminologique；印刷页脚 p.214）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 07:04 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p081.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p081_terminology.png`。
- 核对：术语索引中关于 cohomological flatness、Ext/Tor、Euler–Poincaré 与 Hilbert polynomial 的词条和交叉引用。
- 结果：**FAIL**。第 2714 行把结构层 `O_X` 转录为字母 `c_X`；第 2726 行同一术语的结构层被写成 fraktur `\mathfrak{O}_X`，原文均为 calligraphic `\mathcal{O}_X`。第 2736 行将法文术语 `Künneth` 拼成 `Künneh`。300dpi 裁片核实两处结构层符号和 Künneth 拼写。印刷页脚 214 未录入正文；第 2738 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后将第 2714、2726 行结构层统一写为 `O_X`，并将第 2736 行 `Künneh` 改为 `Künneth`；Markdown 未修改。

### PDF p.82（目录页；印刷页脚 p.215）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 07:10 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p082.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p082_contents.png`。
- 核对：Table des matières 中 §6 与 §7 的篇章标题、编号及原页码列。
- 结果：**FAIL**。第 2741、2747、2748 行把法文术语 `Künneth` 错拼为 `Künneith`。第 2756 行目录项中的 `H_\bullet(P_\bullet)` 将复形/同调指标 bullet 都平化成句点。原页把目录页码逐项放在右侧；Markdown 将 18 个页码移到全部目录条目之后的独立行（2762–2779），使页码与条目脱离，并漏掉 §6 的页码 5、6.2 的页码 6 和 6.3 的页码 9。第 2781 行另有一段讨论 Ground Truth/OCR 规则的英文说明；该段不见于本页原始目录，是多出的异文，不作为指令。300dpi 裁片核实题名、指标与页码列；印刷页脚 215 未录入正文，第 2783 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后更正三处 `Künneith` 拼写、恢复 `H_\bullet(P_\bullet)` 指标、将各页码归回目录条目并补回缺失的 5/6/9，删除与原页无关的第 2781 行异文；Markdown 未修改。

### PDF p.83（空白扫描页；未见印刷页码）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 07:14 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p083.png`（pngmono 150dpi）。
- 核对：本页整页视觉内容及对应 Markdown 页边界。
- 结果：**PASS±**。原页没有正文，只有零散扫描尘点；Markdown 未为本页录入正文，和原页相符。PDF 文本抽取仅返回孤立字母 `s`，但图像上没有可辨认的印刷字符，因此不作为应转录内容。目录后的第 2781 行异文已在 PDF p.82 项下记录；本页图像不支持该文本。
- 页内修复状态：无正文修复；不把图像尘点或无图像依据的文本抽取 `s` 写入 Markdown。

### PDF p.84（印刷 p.217）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 07:20 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p084.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p084_early_errata.png`、`audit/300dpi/Grothendieck_1961_ega3_p084_later_errata.png`。
- 核对：Errata et Addenda (Liste 2), A) Erreurs typographiques 中从 (0_I, 3.2.1) 到 (I, 10.12.2) 的更正条目。
- 结果：**FAIL**。volume-I 引文中的大写罗马 `I` 多处转成数字 `1`：第 2789、2793、2799 行的 `(0_I,...)` 均写成 `(0_1,...)`。第 2801 行引文由 `(0_I, 7.6.9)` 漏成 `(0, 7.6.9)`；该条订正记号还把印刷的 `J_\lambda \mapsto \widetilde{J}_\lambda` 简化为 `Jλ / ℑλ`。第 2803 行把数字引用 `(I, 1.1.15)` 写成 `(I, i.i.15)`；第 2805 行把 `(I, 1.4.1)` 写成 `(I, I.4.I)`；第 2809 行将行号 11 写成 `II`。300dpi 裁片确认 I/1、J 的订正符号及行号。印刷页脚 217 未录入正文；第 2843 行起属于下一 PDF 页。
- 页内修复状态：待全篇审计结束后修正 0_I 引文、补齐第 2801 行 citation 和 J 标记，并恢复 1.1.15、1.4.1、行号 11 中误识的数字；Markdown 未修改。

### PDF p.85（印刷 p.218）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 07:29 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p085.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p085_early_errata.png`、`audit/300dpi/Grothendieck_1961_ega3_p085_III_and_zeros.png`、`audit/300dpi/Grothendieck_1961_ega3_p085_footnote.png`。
- 核对：Errata et Addenda (Liste 2) 的 (II)/(III) typographic entries；(Err_III,1–2) 文字修改开头及脚注。
- 结果：**FAIL**。第 2849 行把 X-prime 写成上标 f（`X^f`），原文为 `X'`。第 2865 行引用 (0_III,11.1.1) 中连续数字 11.1.1 被录成 `II.I.I`。第 2877 行两个页码 111 均写成罗马字母序列 `III`；同一行两条不等式中的四个数字零都录成字母 `o`。第 2889 行 Err_III 条目序号 1 写成小写 `i`，并将 volume-I 引用 `(0_I,5.1.3)` 写成 `(0_1,5.1.3)`。第 2895 行单独插入了脚注词项 `Err_N`；原页只在页底脚注正文中定义它，没有独立正文块。300dpi 裁片确认 X-prime、序号、页码及脚注；印刷页脚 218 未录入正文，第 2899 行起的 Err_III,2 引文续至下一 PDF 页。
- 页内修复状态：待全篇审计结束后修复 X-prime、连续数字 11.1.1、页码 111 与四个数字零、Err_III 的数字 1 和 (0_I,5.1.3) 引文，并删除孤立的 `Err_N` 块；Markdown 未修改。

### PDF p.86（印刷 p.219）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 07:37 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p086.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p086_erratum_OX.png`。
- 核对：Errata (Err_III, 3)–(Err_III, 8) 与 (Err_III, 2) 替代正文续段。
- 结果：**FAIL**。第 2903 行把结构层 `O_X` 中的大写方案指标 `X` 写成小写 `x`；原页的下标是大写 X。其余本页核对的 errata 条目及替代文字首段和印刷内容相符。页脚 219 未录入正文；PDF p.86 在 Err_III, 8 替代文字的 “mais” 处结束，Markdown 后续行 2919 延续到下一 PDF 页。
- 页内修复状态：待全篇审计结束后将第 2903 行 `O_x` 恢复为 `O_X`；Markdown 未修改。

### PDF p.87（印刷 p.220）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 07:42 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p087.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p087_errata_ids.png`。
- 核对：Errata (Err_III, 9)–(Err_III, 18) 条目与对应引用编号、修订对象。
- 结果：**FAIL**。第 2925 行把 errata 条目号 11 转录为罗马字母 `II`，破坏了 (Err_III, 1)–(Err_III, 18) 的十进制顺序。第 2931 行引用 `(II, I.7.8)` 把节号首位数字 `1` 写成大写 `I`；原文为 `(II, 1.7.8)`。300dpi 裁片核实条目号和引用首位。印刷页脚 220 未录入正文；PDF p.87 在 Err_III, 18 条目中的 “si g est” 处结束，Markdown 的第 2945 行续至下一 PDF 页。
- 页内修复状态：待全篇审计结束后将第 2925 行 `Err_{III}, II` 改回条目号 `Err_{III}, 11`，并将第 2931 行引用首位 `I` 改为数字 `1`；Markdown 未修改。

### PDF p.88（印刷 p.221）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 07:48 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p088.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p088_errata_24.png`。
- 核对：Errata (Err_III, 19)–(Err_III, 26) 的订正条目；尤其是 Err_III, 24 中 (0_III, 13.7.7) 的导出函子记号。
- 结果：**FAIL**。第 2955 行 Err_III, 24 的两处 “R^nT(A)” 与一处 “R^{n+1}T(A)” 都多出 prime，Markdown 写成 `R^{\prime n}` / `R^{\prime n+1}`；原文是 `R^n` / `R^{n+1}`。300dpi 裁片确认该三处上标无 prime。印刷页脚 221 未录入正文；第 2961 行起为替代正文，续至下一 PDF 页。
- 页内修复状态：待全篇审计结束后从第 2955 行三个 derived-functor 符号中删除多余 prime；Markdown 未修改。

### PDF p.89（印刷 p.222）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 07:56 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p089.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p089_errata_27_and_29.png`。
- 核对：Errata (Err_III, 18) 的论证结尾、(Err_III, 19)–(Err_III, 29) 条目及 Err_III, 26 替代证明的开头。
- 结果：**FAIL**。第 2971 行 Err_III, 27 中三处直接像项把印刷的 `R^i f_*(−)` 写成 `R^{if}_*(−)`：既把 `f_*` 并入上标，也使上标 i 与函子记号错位。300dpi 裁片核实该条陈述中 vanishing term 及 induced map 的两端均使用 `R^i f_*`。页脚 222 未录入正文；第 2977 行的 Err_III, 29 更正文本续到下一 PDF 页。
- 页内修复状态：待全篇审计结束后将第 2971 行三个 `R^{if}_*` 改为 `R^i f_*`；Markdown 未修改。

### PDF p.90（印刷 p.223；页眉 p.91）

- actor=Peer-P34；model=gpt-6-luna；effort=max。
- 时间：2026-10-02 08:05 EDT。
- 页面证据：`audit/Grothendieck_1961_ega3_p090.png`（pngmono 150dpi）；`audit/300dpi/Grothendieck_1961_ega3_p090_erratum29_notation.png`、`audit/300dpi/Grothendieck_1961_ega3_p090_generators.png`。
- 核对：Errata (Err_III, 29) 更正说明的末段，以及 (Err_III, 30) Proposition (9.3.5) 与拟证明其理想层拟凝聚性的段落。
- 结果：**FAIL**。第 2977 行把原页的 `\mathcal{F}=\widetilde{M}` 和带波浪号的理想层记号简化成 `F=M`、`J=J`，漏掉波浪号并抹平层/理想的字形区别。第 2981–2983 行多处把原页的 calligraphic `\mathcal{F}`、`\mathcal{G}`、`\mathcal{O}_X`、`\mathcal{J}` 写成普通 `F`、`G`、`O_X`、`J`；相邻的 `\mathcal{O}_X/\mathcal{J}` 和 `\mathcal{G}=j^*(\mathcal{F})` 虽保留了相应字形，不能抵消其它位置的漏识。第 2983 行有限生成元指标范围写成 `(i\leqslant i\leqslant r)`，原页为 `(1\leqslant i\leqslant r)`，把数字 1 识成字母 i。300dpi 裁片核实第 2977 行层化/波浪号记号及生成元下界。印刷页脚 223 未录入正文；这是本 PDF 的最后一页。
- 页内修复状态：待全篇审计结束后恢复第 2977 行的层/理想记号和波浪号，统一第 2981–2983 行漏失的 calligraphic 符号，并将第 2983 行生成元范围首项改为数字 `1`；Markdown 未修改。
