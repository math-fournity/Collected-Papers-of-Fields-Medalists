# 逐页审计：Zur Theorie der Überlagerungsflächen（Lars Ahlfors，1930）

## 任务与来源

- actor=Peer-P02；model=gpt-6-luna；effort=max。
- 角色：CONTRIBUTOR；Master-Luna 是唯一 canonical integrator。
- 候选基线：`e04c4a9603818cfa2d71271942f696115783c33b`（main 指向同一提交；本 worktree 为 detached HEAD）。
- PDF：`Ahlfors_1930_ueberlagerungsflaechen.pdf`；38 页；SHA-256 `46674f287f4b9a085ccea11f10dfa22f168cf84d6e69e5cdac27b9945f5ddb28`。
- MinerU Markdown：`Ahlfors_1930_ueberlagerungsflaechen_mineru/Ahlfors_1930_ueberlagerungsflaechen__Ahlfors_1930_ueberlagerungsflaechen.md`；原始提交 `0b0f3dd237016302793972607504146adcf38004`；审计前 SHA-256 `b16665f158adf0b3e9666f0f2537bbb86891c59f0db4d15c1374beac44f8a7c7`。
- 页面类型：扫描件（38 页均含 2550×3225、300dpi、1-bit 整页图像；PDF 另有约 85.8KB 的可提取 OCR 文本层）。按原页图逐页核对；文本层仅辅助定位，不作为印刷内容的最终依据。
- MinerU 导出元数据：producer `mineru` 3.4.4，记录 38 页；未发现独立 `doc_id` 字段。
- PDF 页码与印刷页码分别记录；首页未见印刷页码。疑点若需字形仲裁，将把 300dpi 裁片存入本篇 `audit/` 并随对应提交保全。

## 总评与复核

- 覆盖：扫描 PDF 共 38 页；逐页查看 38 张 pngmono 150dpi 全页图，并按疑点使用 25 张留存的 300dpi 裁片。PDF 另含约 85.8KB OCR 文本层，仅供定位，判定以页图为准。
- MinerU：3.4.4；元数据记录 38 页，未发现独立 doc_id 字段。
- 原始 Markdown 对照等级（修复前快照）：PASS 1 页、PASS± 18 页、FAIL 19 页。以下逐页等级记录原始导出与印刷页的对照结果；修复后核查另见本节修复登记。
- FAIL 内容项均在独立修复提交中按印刷页逐处更正。修复后 AI 从头复读最终 Markdown 全文，共 1,106 行；确认本次修复已落入且未见由修复引入的新差异。该复读不构成第二次 38 页视觉审计。
- 保留为原刊字样/编号的例子：p.15 “Die Charakter eines Ausnahmefalls”、p.17 末式中 2 后的 comma-like 标点（glyph 类别 UNKNOWN）、p.19 “Rückkerschnitt”、p.21 的 »Insel» / »Zunge»、p.29 的 E dy² 项，以及 p.35–36 重复印刷的编号 28。其余 PASS± 项主要是页眉/页码遗漏、重复或游离脚注片段、出版行横线形式和页末装饰符号；逐项见页级记录。

### 修复登记

修复提交：abde327e5ce3b55b4eef7db7bc72226bd11a6128（父提交含原始 Markdown，raw commit 0b0f3dd237016302793972607504146adcf38004）。原始 Markdown SHA-256：b16665f158adf0b3e9666f0f2537bbb86891c59f0db4d15c1374beac44f8a7c7；修复后 SHA-256：6659c161768323e7bbfca17ce5bfe4e1e5516e97837b8a73c410f0af681b75f4。

| PDF 页 | 按印刷原页完成的 Markdown 修复 | 修复提交 |
|---|---|---|
| 3 | 两处 ∂/2 误识为 δ/2 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 7 | 还原 S(Δ) / S_n(Δ)、三个数字 1，并删除绝对值式中的重复负号 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 8 | 两处 S(Δ) 被识作 S(𝒜) | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 9 | 还原 S(Δ) / S_n(Δ) 与五个数字 1 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 12 | 将点号误识还原为 ρ⁺，并将字母 o 改为数字 0 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 15 | 重建 Ω / σ 四列对应表 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 17 | 两处 𝒜′/𝒜″ 还原为 Δ′/Δ″ | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 18 | 补回 n(σ̄) 横线，并将 zasammenhängende 改为 zusammenhängende | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 20 | 还原数字 1、希腊字母 α、ρ⁺ 位置及式号 (II. 2′) | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 22 | 两处 𝒜 还原为 Δ | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 24 | 将 w(𝒜)、n(𝒜ᵥ)、w(𝒜ᵥ) 还原为 Δ 记号 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 25 | 将 Defekt 句的 o/i 还原为 0/1，并修正 (B₁) 标签 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 26 | 三处罗马字母 I 还原为数字 1 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 27 | 修正 Δ_ν 下标，按印刷顺序重排脚注并移除游离重复片段 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 28 | 还原数字 1，并补全 zusammenhängende 词尾 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 29 | 恢复两处根号；保留原刊 E dy² 项 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 34 | 两处罗马字母 I 还原为数字 1 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 35 | 两处 ∘ 误识还原为数字 0 | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |
| 37 | 三处 O(I) 还原为 O(1)，两处 κ(r) 还原为 x(r) | abde327e5ce3b55b4eef7db7bc72226bd11a6128 |

## 逐页记录

### p.001（PDF p.1 / 印刷页码未见）

- audited_at=2026-10-01 15:49 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p001.png`（pngmono，150dpi）。
- 核对：题名、作者 Lars Ahlfors、地点 Helsingfors、引言前三段及页底断句。扫描页可见末句止于“als Erweiterung”；Markdown 保留该处断句，下一页续文仍按顺序出现。可见印刷内容与 Markdown 对应内容吻合。
- 结果：PASS。

### p.002（PDF p.2 / 印刷 p.158）

- audited_at=2026-10-01 15:52 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p002.png`（pngmono，150dpi）。300dpi 局部核对：`audit/300dpi/ueberlagerungsflaechen_p002_distance.png`。
- 核对：引言末句续文；第一部与 §1 标题；定义 1 中有限三角剖分、闭/有边界曲面、长度/面积/距离条件及脚注 1。印刷正文与 Markdown 对应内容一致；裁片中的 ε 符号与 Markdown 一致。
- 差异：印刷页眉“158 Lars Ahlfors.”未收入 Markdown；完整脚注正文之后另有单独的 `131-163` `docvortex-page-footnote` 碎片，而原页只在脚注句末出现一次该页码范围。
- 结果：PASS±（缺失页眉页码与重复脚注碎片均不改变正文含义）。

### p.003（PDF p.3 / 印刷 p.159）

- audited_at=2026-10-01 15:54 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p003.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p003_delta_over2.png`。
- 核对：Regularitätsbedingung 与 `d` 的定义、Hilfssatz 1 的假设和公式 (1)、其两种情形的证明、编号 3 的起始段及脚注 1。除下述符号外，所见陈述和公式与印刷页相符。
- 结果：FAIL。Markdown 两处写作 `\frac{\partial}{2}`；印刷原页及 300dpi 裁片在“Abstand kleiner als …”和“Zahlen …”两处均清楚印为希腊小写 δ/2。修复建议：全篇审计结束后仅在这两个位置逐处用 Edit 将 `\partial` 改为 `\delta`，并记录原页 p.159 为依据。印刷页眉“Zur Theorie der Überlagerungsflächen. 159”未收入 Markdown；脚注前的独立 `k^{\prime}` 页脚片段在完整脚注外多出现一次。

### p.004（PDF p.4 / 印刷 p.160）

- audited_at=2026-10-01 15:55 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p004.png`（pngmono，150dpi）。
- 核对：编号 3 的延续与 Hilfssatz 2 陈述/不等式；证明简述；编号 4 的双化论证、相对闭曲线定义及边界曲面推论，含末尾不等式。页内文字、λ/λ′/λ″、k′、W₀ 与公式关系均与印刷页吻合。
- 差异：印刷页眉“160 Lars Ahlfors.”未收入 Markdown。
- 结果：PASS±（缺失页眉页码，不影响正文）。

### p.005（PDF p.5 / 印刷 p.161）

- audited_at=2026-10-01 15:56 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p005.png`（pngmono，150dpi）。
- 核对：§2、编号 5 的 Überlagerungsfläche 定义、三角形/Spurdreieck 对应关系、相对边界与 Verzweigungspunkt 定义、曲线长度和区域面积的诱导度量；页底出版 imprint 行保留 21—34686、卷 65 和印刷日期。
- 差异：页眉“Zur Theorie der Überlagerungsflächen. 161”未收入 Markdown；imprint 号中印刷长横线被 Markdown 记为普通连字符。
- 结果：PASS±（页眉与出版行标点差异，不影响数学正文）。

### p.006（PDF p.6 / 印刷 p.162）

- audited_at=2026-10-01 15:57 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p006.png`（pngmono，150dpi）。
- 核对：编号 6 的 n-叶定义、单调性和最大叶数 N；面积加和公式 (2)；相对边界及其长度加和；编号 7 的平均叶数 S 与 `S=S₁+…+S_N`。可见文字、下标和公式均与印刷页相符。
- 差异：印刷页眉“162 Lars Ahlfors.”未收入 Markdown。
- 结果：PASS±（缺失页眉页码，不影响正文）。

### p.007（PDF p.7 / 印刷 p.163）

- audited_at=2026-10-01 15:58 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p007.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p007_Delta_equations.png`。
- 核对：局部平均叶数 `S(Δ)` 的定义、求和恒等式、补集不等式、绝对值与 Min/Max 估计以及第一 Hilfssatz 的边界长度估计。300dpi 裁片逐式核验。
- 结果：FAIL，均为可定位的 MinerU 符号差异：①该页 14 处 `S(Δ)`/`S_n(Δ)` 实际写成 `S(\mathcal A)`/`S_n(\mathcal A)`；②补集估计中的 3 个数字 1 写成 `\mathrm{I}`；③一处 `|S_n - S_n(Δ)|` 多出负号，Markdown 为 `|S_n - - S_n(Δ)|`。全篇审计结束后按这些位置逐处 Edit 修正，依据为原页 p.163 及所链 300dpi 裁片。印刷页眉“Zur Theorie der Überlagerungsflächen. 163”未收入 Markdown。

### p.008（PDF p.8 / 印刷 p.164）

- audited_at=2026-10-01 16:00 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p008.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p008_Delta_formula.png`。
- 核对：由逐叶估计求和得到的全局边界估计、Überdeckungssatz 1 陈述及式 (I. I)，均匀性说明，编号 8 的曲线平均叶数定义、加和式、Teilbogen 估计及其文字解释。300dpi 裁片核对了 Δ 记号。
- 结果：FAIL。两处全局估计式（求和后结论与 Überdeckungssatz 1 公式）中的印刷 `S(Δ)` 被 Markdown 写成 `S(\mathcal A)`；依据为印刷 p.164 及所链裁片。印刷页眉“164 Lars Ahlfors.”未收入 Markdown。

### p.009（PDF p.9 / 印刷 p.165）

- audited_at=2026-10-01 16:02 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p009.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p009_Delta_equations.png`。
- 核对：由 Δ 分割曲面导出的各叶估计、Max/Min 界、对 n 求和后的结论、Überdeckungssatz 2 及其边界曲面说明。原页裁片核对了三角形 Δ 与数字 1。
- 结果：FAIL。①8 处 `S_n(Δ)`/`S(Δ)` 被写成 `S_n(\mathcal A)`/`S(\mathcal A)`；②5 处印刷数字 1 被写为大/小写罗马字母 `\mathrm{I}`/`\mathrm{i}`（补集不等式与 Max 估计）。全篇审计后逐处 Edit 修正，依据为印刷 p.165 和所链裁片。印刷页眉“Zur Theorie der Überlagerungsflächen. 165”未收入 Markdown。

### p.010（PDF p.10 / 印刷 p.166）

- audited_at=2026-10-01 16:04 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p010.png`（pngmono，150dpi）。
- 核对：§3 与编号 9 的有限曲面特征数定义 `ρ=-E+K-P`，公式 (3) 的区域分解关系、细分不变性论证开头以及曲线/Querschnitt 对特征数贡献的解释直至页底。可见陈述与公式相符。
- 差异：印刷页眉“166 Lars Ahlfors.”未收入 Markdown。
- 结果：PASS±（缺失页眉页码，不影响正文）。

### p.011（PDF p.11 / 印刷 p.167）

- audited_at=2026-10-01 16:05 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p011.png`（pngmono，150dpi）。
- 核对：公式 (4) 与一般分解公式；q/q′ Konturen 的特征数；闭/有边界曲面的特征数下界；公式 (5)、(5′) 及编号 10 的开头。公式内容与印刷页相符，核对延伸至页底“Für die Teilung”。
- 差异：印刷页眉“Zur Theorie der Überlagerungsflächen. 167”未收入 Markdown；公式 (5′) 的 Markdown `\tag` 参数含多余的 `\(`/`\)`，印刷标签为 `(5′)`，这是标签排版差异，不改变不等式内容。
- 结果：PASS±。

### p.012（PDF p.12 / 印刷 p.168）

- audited_at=2026-10-01 16:07 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p012.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p012_rho_plus.png`。
- 核对：曲面分支特征数公式 (6)、Hurwitz 关系推论、§4 主定理及 (II. 1) 不等式，至全篇论证的开头。裁片显示主定理定义符号为 rho 上标 `+`，公式中的相应记号也一致。
- 结果：FAIL。主定理文字中印刷的 `ρ⁺` 被写作 `\dot{\varrho}`，且“grössere der Zahlen ρ und 0”中的数字 `0` 被写成字母 `o`；300dpi 裁片确认两处原字形。两处均已按 p.168 用 Edit 修正。印刷页眉“168 Lars Ahlfors.”未收入 Markdown。

### p.013（PDF p.13 / 印刷 p.169）

- audited_at=2026-10-01 16:08 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p013.png`（pngmono，150dpi）。
- 核对：主定理动机与 q>2 简连基面分割的构造、横截曲线假设、提升至 W 的 σ 分割，以及不等式 (5)；可见陈述和公式均与原页相符。
- 差异：印刷页眉“Zur Theorie der Überlagerungsflächen. 169”未收入 Markdown；页底期刊 imprint 的 `22—34686` 在 Markdown 中用普通连字符记录。
- 结果：PASS±（页眉与出版行标点差异，不影响数学内容）。

### p.014（PDF p.14 / 印刷 p.170）

- audited_at=2026-10-01 16:09 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p014.png`（pngmono，150dpi）。
- 核对：编号 13 的 Ωₙ/σₙ 类构造与归纳论证；文本截至“und auch dann”，后续句子在下一页。可见记号、类关系与陈述顺序均与印刷页相符。
- 差异：印刷页眉“170 Lars Ahlfors.”未收入 Markdown。
- 结果：PASS±（缺失页眉页码，不影响正文）。

### p.015（PDF p.15 / 印刷 p.171）

- audited_at=2026-10-01 16:11 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p015.png`（pngmono，150dpi）。300dpi 局部核对：`audit/300dpi/ueberlagerungsflaechen_p015_classes.png`。
- 核对：编号 13 例外情形的收尾；编号 14 的 Ω′/Ω* 与 σ′/σ″/σ* 分类规则；类对应关系表与其下三条性质。300dpi 裁片核验表格列关系与印刷字形。
- 结果：FAIL。类对应关系表未正确保留：印刷为四类并列、两行对齐的表格 `((Ω₁)…(Ωₚ), Ω′, Ω*) / ((σ₁)…(σₚ), σ′与σ″, σ*)`；Markdown 只声明两列，把 `Ω*` 错置为数组 `\tag`，并将 `σ*` 移到数组之外，破坏类的列对应关系。全篇结束后按原表逐处手工修复。另，原刊此页印作“Die Charakter eines Ausnahmefalls”；Markdown 忠实保留该源级语法 quirk，不按语法预期改写。印刷页眉“171”未收入 Markdown。

### p.016（PDF p.16 / 印刷 p.172）

- audited_at=2026-10-01 16:12 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p016.png`（pngmono，150dpi）。
- 核对：公式 (7)、(8) 与 σ*/Ω* 类的计数界；λ*、λ′、λ″、λa 定义；覆盖定理估计以及导出的 rho 下界，至页底句中断处。可见变量、系数、分式和不等式方向均与印刷页一致。
- 差异：印刷页眉“172 Lars Ahlfors.”未收入 Markdown；正文在页底连字符处续至下一页。
- 结果：PASS±（缺失页眉页码，不影响正文）。

### p.017（PDF p.17 / 印刷 p.173）

- audited_at=2026-10-01 16:13 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p017.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p017_Delta_bounds.png`；`audit/300dpi/ueberlagerungsflaechen_p017_lambda_bound.png`。
- 核对：编号 15 的相对边界估计、对 Ωₙ/σₙ 求和得到的 λa 界，以及 p.16 末尾证明句的续文。300dpi 裁片核对 Δ′/Δ″ 两个基面区域。
- 结果：FAIL。定义 `L(Ω)` 的位置，印刷原文指 Ω 相对于 `Δ′` 或 `Δ″` 的相对边界长度；Markdown 两处写成 `\mathcal A'`、`\mathcal A''`。已按 p.173 裁片逐处修正，见修复登记。同页后部不等式中，印刷在系数 2 后有 comma-like 标点；300dpi 裁片确认该印刷形状，Markdown 保留为 `2, λ_a`。其具体 glyph 分类（comma 或 multiplication dot）为 UNKNOWN，不按代数预期规范化。印刷页眉“Zur Theorie der Überlagerungsflächen. 173”未收入 Markdown。

### p.018（PDF p.18 / 印刷 p.174）

- audited_at=2026-10-01 16:15 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p018.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p018_covering_count.png`。
- 核对：多连通基面割开后的曲面分解、公式 (9)、以正部特征数与 `N₁` 表达的改写、以及横截曲线分割连通曲面的拓扑论证开头。裁片核验了式中 `\bar{\sigma}` 与“zusammenhängende”的印刷字形。
- 结果：FAIL。①`\varrho=\sum^+\varrho(\bar W)-N_1+n(\bar\sigma)` 中末项应为 `n(\bar\sigma)`，Markdown 漏掉 σ 上方的横线；②印刷为 `zusammenhängende Fläche`，Markdown 误作 `zasammenhängende Fläche`。页眉“174 Lars Ahlfors.”未收入 Markdown。OCR 另将该页脚注符号 `Ω′`、`σ′` 单独拆出，完整脚注正文仍在其后；该重复碎片不替代正文脚注。

### p.019（PDF p.19 / 印刷 p.175）

- audited_at=2026-10-01 16:17 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p019.png`（pngmono，150dpi）。300dpi 原文局部核对：`audit/300dpi/ueberlagerungsflaechen_p019_Rueckker.png`。
- 核对：第 16 节特征数正部比较及其证明、全篇不等式 (II. 1) 的回收、§5 与编号 17 的开头。可见公式、横线和系数与原页相符。
- 源级字形/拼写：PDF 印作 `Rückkerschnitt`，Markdown 保留相同拼写；仅作原刊记录，不据术语预期擅改。
- 差异：印刷页眉“Zur Theorie der Überlagerungsflächen. 175”未收入 Markdown。
- 结果：PASS±。

### p.020（PDF p.20 / 印刷 p.176）

- audited_at=2026-10-01 16:21 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p020.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p020_double_ineq.png`。
- 核对：补集特征数关系、双边不等式 (II. 2) 及 ρ₀≥0 时的简化式 (II. 2′)。300dpi 裁片核验了 1/α/ρ⁺ 的印刷位置和标签。
- 结果：FAIL。①式 (II. 2) 下界中印刷数字 `1` 被写成 `\mathrm{i}`；②定理陈述中的闭合轮廓数印刷为 `α`，Markdown 写成普通字母 `a`；③简化式 (II. 2′) 中印刷为 `ρ⁺`，Markdown 将 `+` 错置到 `≤` 上；④式号印刷为 `(II. 2′)`，Markdown 标签成 `II. z′`。全篇审计后逐处 Edit 修正。印刷页眉“176 Lars Ahlfors.”未收入 Markdown。

### p.021（PDF p.21 / 印刷 p.177）

- audited_at=2026-10-01 16:23 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p021.png`（pngmono，150dpi）。300dpi 局部核对：`audit/300dpi/ueberlagerungsflaechen_p021_quotes_imprint.png`。
- 核对：§II 开放覆盖定义、正则穷尽条件，编号 19 的 `S(Δ)` 覆盖估计与 Insel/Zunge 分类，直至页底“Multiplizität der betref-”。正文与公式均相符。
- 差异：印刷页眉“Zur Theorie der Überlagerungsflächen. 177”未收入 Markdown；页底期刊 imprint 分隔线在 Markdown 中简化为短横线。印刷中的术语引号为 `»Insel»`、`»Zunge»`，Markdown 保留同样的原刊排印。
- 结果：PASS±。

### p.022（PDF p.22 / 印刷 p.178）

- audited_at=2026-10-01 16:24 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p022.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p022_delta_multiplicity.png`。
- 核对：Insel/Zunge 解释、岛的普通重数与公式 (A)、正则穷尽中的上极限估计、点极限说明及编号 20 的特殊情形起始。裁片确认公式使用三角形 Δ。
- 结果：FAIL。定义 Zunge 贡献时，印刷为 `S(Δ)` 与 `μ(Δ)`；Markdown 两处写为 `S(\mathcal A)` 与 `μ(\mathcal A)`。审计完成后逐处 Edit 修复，并回读全文。页眉“178 Lars Ahlfors.”未收入 Markdown；页底出版行分隔符也与印刷短横线样式不同。

### p.023（PDF p.23 / 印刷 p.179）

- audited_at=2026-10-01 16:25 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p023.png`（pngmono，150dpi）。
- 核对：简单 Insel 重数定义、p(Δᵥ) 总和与上界、去除 Zungen/Inseln 后余下 ̅W 分解、特征数关系与 N₁ 修正，至 p.23 末句“Hieraus folgt dass”。可见定义、下标和公式与原页一致。
- 差异：印刷页眉“Zur Theorie der Überlagerungsflächen. 179”未收入 Markdown。
- 结果：PASS±（缺失页眉页码，不影响正文）。

### p.024（PDF p.24 / 印刷 p.180）

- audited_at=2026-10-01 16:27 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p024.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p024_delta_beta.png`。
- 核对：β 的定义及其导出下界，覆盖不等式 (10)、(B)，q=2 的说明，以及编号 21 的 Hurwitz 关系和两种等价不等式。裁片核验其中三角形 Δ 记号。
- 结果：FAIL。第 21 节中定义岛分支点总数的文字 `w(Δ)` 被写成 `w(\mathcal A)`；推导 (B) 的后一种表达式还将两处 `n(Δᵥ)`/`w(Δᵥ)` 写成 `n(\mathcal A_v)`/`w(\mathcal A_v)`，共 3 处。全篇审计后逐处 Edit 修复。印刷页眉“180 Lars Ahlfors.”未收入 Markdown。

### p.025（PDF p.25 / 印刷 p.181）

- audited_at=2026-10-01 16:29 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p025.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p025_defect.png`。
- 核对：不等式 (B′)、缺陷 δ 与分支指数 ε 的极限定义、Defektrelation、由区域退化为点所得 (B₁)。裁片核验边界数值。
- 结果：FAIL。印刷句“Der Defekt zwischen 0 und 1”使用数字 `0`、`1`；Markdown 写成字母 `o`、`i`，两处需分别用 Edit 修正。公式 (B₁) 的 MinerU `\tag` 还带有嵌套 `\(` 标记；正文不等式仍在，作为标签排版瑕疵另行登记。印刷页眉“Zur Theorie der Überlagerungsflächen. 181”未收入 Markdown。

### p.026（PDF p.26 / 印刷 p.182）

- audited_at=2026-10-01 16:30 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p026.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p026_muinverse.png`。
- 核对：编号 22 的必要条件、(II) 对 μᵢ 的限制、五组最小整数系统及点退化推论开头。裁片逐字符核验了系数中的倒数数字。
- 结果：FAIL。①系数 `q−2−Σ 1/μᵢ` 中分子数字 1 被写成 `\mathrm{I}`；②条件 `Σ(1−1/μᵢ)>2` 中两个数字 1 都写成 `\mathrm{I}`；两项公式中共 3 个数字 1 需改回 `1`。p.25 的“Defekt zwischen 0 und 1”两字母误识已在 p.025 记录。印刷页眉“182 Lars Ahlfors.”未收入 Markdown。

### p.027（PDF p.27 / 印刷 p.183）

- audited_at=2026-10-01 16:32 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p027.png`（pngmono，150dpi）。300dpi 脚注裁片：`audit/300dpi/ueberlagerungsflaechen_p027_footnotes.png`。
- 核对：不正则穷尽的三个点推论、编号 23 对开放覆盖的定义与 Insel 条件、补集覆盖 F 的构造，以及脚注 1、2 的引文内容。
- 结果：FAIL。脚注 1 印作 `\bar W_0` 为区域 `Δ_ν` 的补集；Markdown 把 `ν` 写成与 Δ 同行的 `\Delta\nu`，丢失下标，见 300dpi 裁片。Markdown 还将脚注 2 排在脚注 1 前，并在脚注全文外留有独立 `\bar W_0` 碎片；脚注语句均存在但顺序/碎片化另作修复核对。印刷页眉“Zur Theorie der Überlagerungsflächen. 183”未收入 Markdown。

### p.028（PDF p.28 / 印刷 p.184）

- audited_at=2026-10-01 16:34 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p028.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p028_one_and_word.png`。
- 核对：式 (C)、(C′) 及点覆盖推论，§III 与编号 24 的开头。裁片核验式 (C) 常数项和 “zusammenhängende” 拼写。
- 结果：FAIL。①式 (C) 右端印刷数字 `1`，Markdown 写成 `\mathrm I`；②印刷为 `einfach zusammenhängende Fläche`，Markdown 漏写词尾 `nde`，成为 `einfach zusammenhänge Fläche`。审计结束后在这两个位置分别用 Edit 修正。印刷页眉“184 Lars Ahlfors.”未收入 Markdown。

### p.029（PDF p.29 / 印刷 p.185）

- audited_at=2026-10-01 16:37 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p029.png`（pngmono，150dpi）。300dpi 裁片：`audit/300dpi/ueberlagerungsflaechen_p029_radicals.png`；`audit/300dpi/ueberlagerungsflaechen_p029_L_integral.png`。
- 核对：正定度量公式、长度/面积积分、拟共形条件 (12)、I(r)/L(r) 定义与 I′(r) 关系。两张裁片核验根号和微分符号。
- 结果：FAIL。①式 (12) 印刷为 `E+G≤2K√(EG−F²)`，Markdown 丢失根号，输出成 `2K V E G−F²`；②L(r) 印刷积分的整个被积二次型有根号，Markdown 同样把根号识别成 `V`。另一个源级印刷 quirk：L(r) 被积式首项印为 `E dy²`（300dpi 已确认）；Markdown 按印刷保留，不依照标准度量形式改成 `E dx²`。印刷页眉“Zur Theorie der Überlagerungsflächen. 185”未收入 Markdown。

### p.030（PDF p.30 / 印刷 p.186）

- audited_at=2026-10-01 16:38 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p030.png`（pngmono，150dpi）。
- 核对：Schwarz 不等式估计 (13)、导出的微分不等式 (14)、积分条件 (15) 与后续辅助函数引入。可见系数、指数、积分区域及公式关系与印刷页相符。
- 差异：印刷页眉“186 Lars Ahlfors.”未收入 Markdown。
- 结果：PASS±（缺失页眉页码，不影响正文）。

### p.031（PDF p.31 / 印刷 p.187）

- audited_at=2026-10-01 16:39 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p031.png`（pngmono，150dpi）。
- 核对：关于满足特定 Φ 条件的区间列与 L(r) 界、有限圆盘情形的微分不等式和面积增长估计、Abbildungssatz 及等周准则。可见根号、指数、积分限、(13)–(15) 与不等式方向均相符。
- 差异：印刷页眉“Zur Theorie der Überlagerungsflächen. 187”未收入 Markdown。
- 结果：PASS±（缺失页眉页码，不影响正文）。

### p.032（PDF p.32 / 印刷 p.188）

- audited_at=2026-10-01 16:40 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p032.png`（pngmono，150dpi）。
- 核对：Typenproblem 说明、等周判据、section IV 与编号 26 的 meromorphic function 部分开头，至页底“endliche Über-”断句。可见文本与符号均与印刷页相符。
- 差异：印刷页眉“188 Lars Ahlfors.”未收入 Markdown。
- 结果：PASS±（缺失页眉页码，不影响正文）。

### p.033（PDF p.33 / 印刷 p.189）

- audited_at=2026-10-01 16:41 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p033.png`（pngmono，150dpi）。
- 核对：球面覆盖下的 S(r)、L(r) 积分表示，式 (a)、(b)、(b₁) 及对应的 meromorphic function 条件。数学表达、积分限、系数和公式标签均与印刷页相符；脚注 1 的三角剖分说明也保留。
- 差异：印刷页眉“Zur Theorie der Überlagerungsflächen. 189”未收入 Markdown；脚注全文之前另有 `W_r` 两次及 `|z|<r`、`|z|=r` 两个单独 `page_footnote` 碎片，原页只有其后的完整脚注说明。
- 结果：PASS±（页眉与重复脚注碎片，不影响公式内容）。

### p.034（PDF p.34 / 印刷 p.190）

- audited_at=2026-10-01 16:43 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p034.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p034_scheiben.png`。
- 核对：式 (c)、(c′)、Scheibensatz 条件及结论 `S(r)=O(1/(R-r))`，连同其脚注和五组极小整数参数例。
- 结果：FAIL。Scheibensatz 条件中印刷为 `Σ(1−1/μᵢ)>2`；Markdown 将两个数字 1 都写成 `\mathrm{I}`。300dpi 裁片确认字形。全篇审计后逐处 Edit 修正。印刷页眉“190 Lars Ahlfors.”未收入 Markdown。

### p.035（PDF p.35 / 印刷 p.191）

- audited_at=2026-10-01 16:45 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p035.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p035_zero.png`。
- 核对：Scheibensatz 的 Picard/Valiron 特例、编号 28 的正 genus 代数关系命题、由函数映射诱导的覆盖对应及该反证的前半段。
- 结果：FAIL。代数关系定义和禁止恒等成立的主张中共两处印刷数字 `0` 被 Markdown 写成 `\circ`；300dpi 裁片确认原页均为数字零。全篇审计后逐处 Edit 修复。印刷页眉“Zur Theorie der Überlagerungsflächen. 191”未收入 Markdown。

### p.036（PDF p.36 / 印刷 p.192）

- audited_at=2026-10-01 16:47 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p036.png`（pngmono，150dpi）。300dpi 复核裁片：`audit/300dpi/ueberlagerungsflaechen_p036_one_zero.png`。
- 核对：编号 28 的代数关系结论收尾；Nevanlinna 的 N(r,a)、m(r,a)、m(r,∞)、T(r) 定义及第一主定理 (16)。符号、积分域、绝对值和等式均与印刷页相符。脚注 `a=f(o)` 按原刊字形保留。
- 源级编号：本页又出现印刷编号“28.”，与 p.35 的编号重复；依原页保留，不重编号。
- 差异：印刷页眉“192 Lars Ahlfors.”未收入 Markdown。
- 结果：PASS±。

### p.037（PDF p.37 / 印刷 p.193）

- audited_at=2026-10-01 16:48 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p037.png`（pngmono，150dpi）。300dpi 仲裁裁片：`audit/300dpi/ueberlagerungsflaechen_p037_O_one.png`。
- 核对：Nevenlinna 主公式积分后的两条平均值关系、`x(r)=S(r)-S(r,Δ)` 定义、界 `|x(r)|≤kL(r)` 及幂次估计。裁片核验数字 1 与变量 x。
- 结果：FAIL。①三处余项印刷为 `O(1)`，Markdown 写成 `O(\mathrm{I})`；②积分式与末尾绝对值界中两处印刷变量 `x(r)` 被写成 `\varkappa(r)`。审计结束后逐处 Edit 修正。印刷页眉“Zur Theorie der Überlagerungsflächen. 193”未收入 Markdown；页底出版行另见原页。

### p.038（PDF p.38 / 印刷 p.194）

- audited_at=2026-10-01 16:50 EDT；actor=Peer-P02；model=gpt-6-luna；effort=max。
- PNG：`audit/ueberlagerungsflaechen_p038.png`（pngmono，150dpi）。
- 核对：Nevanlinna 第二主定理估计式 (17)/(17′)、重数一计数函数定义、积分残差关系、λ(r) 界与全文结论。公式、下标、交叉引用和页末收束相符；PDF 末尾另有装饰性收尾符号。
- 差异：印刷页眉“194 Lars Ahlfors.”未收入 Markdown；页末装饰符号未转写。
- 结果：PASS±（缺失页眉与装饰性收尾符号，不影响正文）。
