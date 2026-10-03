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

## p.003（PDF p.3 / 印刷 p.3）
- PNG：audit-redo/ICM2022_proceedings_Duminil-Copin_p003.png（pngmono 150dpi）
- 核对：p.2 跨页续句（"field is applied to it…ferromagnetic phase below it"）、Curie's law/Weiss 段、Lenz 两段、Ernst Ising 段、Ising 假设两引语段、末段至 "irrespective of the tempera-" 跨页断点
- 结果：**PASS±**
  - 正文与印刷逐句吻合：`[101]`、`[80]`、`[70]` 引用号正确；`mean-field approximation`、`Curie-Weiss model` 术语正确；Ising 两处直接引语（"decay rapidly with distance…"、"of all the possible positions…"）逐字一致；1900/1924/1925 年份正确；页界断词 `tempera-`/`ture` 跨页衔接正确。
  - 残留伪影（登记不改）：MD 行 35 `eficient`——印刷为 `efficient`（ff 拍平 OCR 伪影，非 print quirk）；印刷 running foot `3 100 Years of the Ising Model` 未入 MD。
- 备注：Luna 旧审计 p.003 判 PASS± 并登记同一 `eficient` 伪影，本次重核结论一致；无内容错误、无新修复。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：audit-redo/ICM2022_proceedings_Duminil-Copin_p004.png（pngmono 150dpi）
- 核对：p.3 跨页续段（Ising conjecture + Stephen Brush 引语）、§2.2 形式定义段符号、公式 (2.1)(2.2)(2.3) 与编号、n.n.f. 术语
- 结果：**PASS±**
  - 数学定义逐项吻合：`G = (V, E)`、`Z^d`、`e = {x,y}`、`σ_x ∈ {−1,+1}`、`(σ_x : x ∈ V) ∈ {−1,1}^V`；打印文本的 `{−1,+1}`（自旋取值）与 `{−1,1}^V`（构型空间）差异在 MD 中忠实保留。
  - 公式：(2.1) `H_{G,h}(σ) := −Σ_{{x,y}∈E} σ_x σ_y − h Σ_{x∈V} σ_x`；(2.2) `H_{G,h,(J_{x,y})}(σ) := −Σ_{x,y∈V} J_{x,y} σ_x σ_y − h Σ_{x∈V} σ_x`；(2.3) `Z(G,β,h) := Σ_{σ∈{−1,1}^V} exp[−βH_{G,h}(σ)]`——求和域、下标、编号与印刷一致；`h ∈ R`、`(J_{x,y} : x,y ∈ V)`、`n.n.f.` 正确。
  - Luna 旧修复重核**全部成立**：Brush 引语中 `Dr. Wolfgang Pauli`（旧 MD 曾作 `$D r$Wolfgang Pauli`）、`model`（曾作 `mode`）、定义段符号 `V/E/x/y/G`（曾作 `�`）现均与印刷一致。
  - 残留伪影（登记不改）：MD 行 51 `ofthe`、行 59 `magneticfield`、行 65 `neighbourferromagnetic`——均为印刷含空格而 MD 空格合并（SOP PASS± 类）；行内公式与相邻词的空格合并（如 `subgraph$G = ( V , E )$of`）；running foot `4 Hugo Duminil-Copin` 未入 MD。
- 备注：本页公式编号 (2.1)–(2.3) 完整；p.5 将核对 (2.4) 的 print quirk（印刷在定义 `H_{G,h}` 之后 (2.4) 即使用 `H_{G,β,h}`）。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：audit-redo/ICM2022_proceedings_Duminil-Copin_p005.png（pngmono 150dpi）
- 核对：公式 (2.4)(2.5)(2.6)(2.7) 与编号、自由能/磁化强度 prose、§2.3 节标题、§2.3 前两段（至 "violating the latest developments of" 跨页断点）
- 结果：**PASS±**
  - 公式逐项吻合：(2.4) `⟨X⟩_{G,β,h} := (1/Z(G,β,h)) Σ_{σ∈{−1,1}^V} X(σ) exp[−βH_{G,β,h}(σ)].`；**print quirk 忠实保留**——印刷 (2.4) 指数内作 `H_{G,β,h}`（前置定义是 `H_{G,h}`，Z(G,β,h) 内亦然），MD 行 78 原样照录，**不得按数学预期改回 `H_{G,h}`**（150dpi 图与 born-digital 文本层双证一致）；(2.5) 无句尾句号（印刷如此，MD 同）；(2.6) 尾逗号保留；(2.7) `lim_{h↘0}`（`\searrow`）正确。
  - 记号：`Λ_n := [−n,n]^d ∩ Z^d`、`f(β,h) := −(1/β) lim_{n→∞} (1/|Λ_n|) ln Z(Λ_n,β,h)`、`m(β,h) := −∂/∂h f(β,h)`、`m*(β) := lim_{h↘0} m(β,h)` 全部与印刷一致；`[63]` 引用号正确；"a semi-classical version of Heisenberg model"（印刷即无 the）忠实保留。
  - 残留伪影（登记不改）：MD 行 81 `called thefree energy`、`define thefree energy`（两处空格合并，印刷为 "the free energy"）；行 101 `$m ^ { * } ( \beta ) =$ 0` 行内空格排版；running foot `5 100 Years of the Ising Model` 未入 MD。
- 备注：Luna 总评登记的 (2.4) print quirk 经本页双通道重核属实且 MD 处置正确；无内容错误、无新修复。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：audit-redo/ICM2022_proceedings_Duminil-Copin_p006.png（pngmono 150dpi）
- 核对：§2.3 续段（Heisenberg 对比结尾、Tamman/Bragg-Williams/Bethe、Fowler、Peierls 三段）、§2.4 节标题、§2.4 首段与 Peierls argument 开头（至 "one may draw" 跨页断点）
- 结果：**PASS±**
  - 正文逐句吻合：1919/1935/1936 年份、`[19]`/`[90]` 引用号、`Gustav Tamman`、`Bragg-Williams model`、`cooperative phenomena` 正确；印刷 "a statistical mechanics's argument"（原作者笔法）忠实保留。
  - 记号：`σ ∈ Z²` 构型、`E(σ)`、`{x,y}`、`σ_x ≠ σ_y` 与印刷一致。
  - 残留伪影（登记不改）：MD 行 115 `diferent`×2（印刷 `different`，ff 拍平）；行 121 `ofthe`、`ofmathematical`（空格合并，印刷 "of the physics community"、"of mathematical interest"）；行 123 `dual graph1`——印刷为脚注上标 `graph¹`（上标拍平；脚注正文不在 p.6 页面，p.007 续查）；running foot `6 Hugo Duminil-Copin` 未入 MD。
- 备注：跨页断词 "draw" 处 MD 与印刷衔接一致；无内容错误、无新修复。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：audit-redo/ICM2022_proceedings_Duminil-Copin_p007.png（pngmono 150dpi）
- 核对：p.6 跨页续段、公式 (2.8)(2.9)、无编号不等式 `⟨I(C=C)⟩ ≤ e^{−2β|∂_e C|}`、Frame 1 标题与正文两段、脚注 1（对偶图定义）
- 结果：**PASS±（含 2 处修复，见下）**
  - 公式逐项吻合：(2.8) `Z(G,β,0) = Σ_{σ∈{−1,1}^V} e^{−βH_{G,h}(σ)} = e^{β|E(G)|} Σ_{F∈Even(G*)} e^{−2β|F|}.`——**print quirk 忠实保留**：左端取 h=0 而指数内印刷作 `H_{G,h}`（非 `H_{G,β,0}`），MD 原样照录不改；(2.9) `⟨σ_0σ_g⟩_{Λ_n^+,β,0} = 1 − 2 Σ_{g∉C∈Even((Λ_n^+)*)} ⟨I(C=C)⟩_{Λ_n^+,β,0}.`——随机 `C`（粗体 C）与固定 `C`（斜体）在印刷与 MD 中均有区分；`Flip_C(σ)`、`∂_e C`、`R² \ {e* : e ∈ E(σ)}` 正确。
  - Frame 1 正文：`⟨σ_0σ_g⟩_{Λ_n^+,β,0}`、`Λ_n^+`、Griffiths "ghost" vertex、`m*(β)` 极限表述与印刷一致；印刷美式拼写 "magnetization" 忠实保留；**print quirk 忠实保留**："the fact that β large renders"（印刷原句如此）。
  - 脚注 1（对偶图 `G* = (V*, E*)` 定义、`e ↦ e*` 双射、(1/2,1/2) 平移）完整且逐句吻合；MD 以 `<small>` 段落承载，位置在 Frame 不等式之后（对应印刷页脚位置），属布局级差异不误导。
  - **修复 1（本页证据：PNG 中 "for large values of β, see Frame 1" 为单逗号，born-digital 文本层同）**：MD 行 129 `$\beta ,$,` → `$\beta$,`（转写时重复逗号；印刷干净，非 print quirk）。
  - **修复 2（本页证据：PNG 中 "with exactly one endpoint in C." 为单句点，文本层同）**：MD 行 143 `$C .$.` → `$C$.`（转写时重复句点；印刷干净，非 print quirk）。
  - 残留伪影（登记不改）：行 131 `diferent`、行 135 `suficient`、行 143 `efectively`（均 ff 拍平，印刷 `different/sufficient/effectively`）；行 135 `uniformly in$n .$`、行 137 数学跨行拆分 `{ e ^ { * } : e \in$ $E ( \sigma ) \}`（排版级）；行 123 `dual graph1` 脚注上标拍平（脚注正文已入 MD 行 149）；running foot `7 100 Years of the Ising Model` 未入 MD。
- 备注：Luna 总评登记的 p.7 "the fact that β large renders" print quirk 重核属实；本次修复仅消除双标点转写错误，未触碰任何 print quirk。
