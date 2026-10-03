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

## p.002（PDF p.2 / 印刷 p.2）
- PNG：`audit-redo/p002.png`（pngmono 150dpi；本次重做新渲染并目检整页）。
- 核对：目录续项（References…44）、§1 开头三段、Theorem 1.1 完整陈述（含两条 bullet 假设）、ǫ=0 反例段、已知部分情形列表前两条；与 Markdown 第 43–71 行逐项比对，辅以 `pdftotext -f 2 -l 2`。
- 结果：**PASS±**
  - 目录续项：印刷为「References …… 44」；MD 中该行在题录区（见 p.001 登记②）且缺页码 44，结构伪影不修。
  - 正文、Theorem 1.1 陈述（(X,B) ǫ-lc / −(K_X+B) nef and big 两条 bullet）、两条已知情形（[22]、[27]）与印刷一致；两处 `Y → Z` 箭头（Mori fibre space structure 及 general fibre）MD 均为 `$Y \to Z$`——Luna 旧修复经原页 PNG 复核为正确，保留。
  - PASS± 项（不修，登记）：`that`→`tha`（p.2 中段，丢 t）；`differential`→`diferential`、`pseudo-effective`→`pseudo-efective`（ff 拍平）；若干 `$…$` 与后续单词间空格丢失（如 `$-K_X$is`），词界仍可辨，均不改变数学陈述。
- 备注：Luna p.002 登记的箭头丢失与 bullet 缺失两项修复均属实且已正确落地；`tha` 登记属实。本次重检未发现 Luna 漏报的本页内容差异。
- 记录时间：2026-10-03 12:16 EDT；actor=`Wf-R-P13`；model=`GLM-5.3-Flash`；effort=max（run级配置，自报UNKNOWN）。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：`audit-redo/p003.png`（pngmono 150dpi；本次重做新渲染并目检整页）。
- 核对：已知情形列表后三条（[2]/[8]/[13] 及 DCC 边界条）、Example 1.2（含 $K_{W_n}+\frac{n-2}{n}E=f^*K_{X_n}$）、Example 1.3（爆破链 $V_1\to\mathbb{P}^2$、$V_2\to V_1$、$V_n\to V_{n-1}$、$X'_n\to X_n$）、Corollary 1.4 陈述（两条 bullet + $K_X+\Delta\sim_{\mathbb{R}}0$）；与 Markdown 第 73–111 行逐项比对，辅以 `pdftotext -f 3 -l 3`。
- 结果：**PASS±**
  - Luna 旧修复逐项复核为正确：四处箭头（$V_1\to\mathbb{P}^2$、$V_2\to V_1$、$V_n\to V_{n-1}$、$X'_n\to X_n$ 及 $n\to\infty$、$f\colon W_n\to X_n$）均已恢复；`n ≥ 2` 为普通 `\geq` 无伪双点；[8] 后无多余 `2`；Corollary 1.4 边界为 `$\Delta$` 无伪下标，且 `K_X+Δ∼_R 0`、两条 bullet 均与印刷一致。
  - PASS± 项（不修，登记）：①MD 第 83 行 `$n \geq 2 ,$,` 双逗点（印刷单个逗号）；②MD 第 91 行 `## Example 1.3. Consider the pair` 与第 107 行 `## form a bounded family.` 被 MinerU 提升为二级标题（印刷均为普通段落行；内容完整、不改变数学，属结构伪影——Luna p.003 登记未含此两项，本次补记）；③$S^{\sim}$：印刷为 S 上方波浪（$\tilde S$ 式），MD 写成上标波浪 `S ^ { \sim }`，记号可辨属排版扁平；④`coefficients`→`coeficients` 三处 ff 拍平；⑤数学式与正文间若干空格粘连。
  - 公式 $K_{W_n}+\frac{n-2}{n}E=f^*K_{X_n}$、$\frac{2}{n}$-lc、$(\mathbb{P}^2,\Delta=S+T+R)$、$x_0:=S\cap T$、$x_1:=S^{\sim}\cap E_1$ 等均与印刷一致。
- 备注：Luna p.003 登记的差异与修复全部属实；漏报的两处标题提升与上标波浪已补记。本次重检未发现本页数学内容错误。
- 记录时间：2026-10-03 12:22 EDT；actor=`Wf-R-P13`；model=`GLM-5.3-Flash`；effort=max（run级配置，自报UNKNOWN）。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：`audit-redo/p004.png`（pngmono 150dpi；本次重做新渲染并目检整页）。
- 核对：McKernan–Prokhorov 猜想段（含 M<sup>c</sup>Kernan 上标 c）、Jordan property 段与 Corollary 1.5 全文、Cremona group $\mathrm{Cr}_d(k):=\mathrm{Bir}(\mathbb{P}^d_k)$、Bir(X) 非 Jordan 段（[45]/[40]）、`lct(X,B,L)`、`|A|_R` 定义及四个行间公式（inf/sup 两条等价式）；与 Markdown 第 113–153 行逐项比对，辅以 `pdftotext -f 4 -l 4`。
- 结果：**PASS±**
  - 正文、Corollary 1.5、`[39, Theorem 1.8]`、`[41, 6.1]`、四条行间公式及 `|A|`、`|A|_Q` 句均与印刷一致；`M<sup>c</sup>Kernan` 与印刷的上标 c 排印一致（Luna 判定忠实，维持）。
  - PASS± 项（不修，登记）：①`Kähler-Einstein` 被编码为 `K¨ahler-Einstein`（变音符脱离元音，可辨；与 Luna 登记一致）；②行末 `$A = - K _ { X }$` 后缺句点（印刷句末有点，属下页跨行末尾，标点扁平）；③若干数学式与单词空格粘连。
- 备注：Luna p.004 登记属实、无过度或遗漏修复。本页无数学内容错误。
- 记录时间：2026-10-03 12:27 EDT；actor=`Wf-R-P13`；model=`GLM-5.3-Flash`；effort=max（run级配置，自报UNKNOWN）。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：`audit-redo/p005.png`（pngmono 150dpi；本次重做新渲染并目检整页）。
- 核对：anti-log canonical 引入段、Theorem 1.6 全文（两条 bullet 假设 + `lct(X,B,|A|_R) ≥ t`）、Theorem 1.7 全文（含 `0 ≤ D ∼_R A`、`D ∼_Q A`、三条行间公式）、Cheltsov/Shokurov 段、Theorem 1.8 开头三条假设（重点 `A^d ≤ r` 无下标）；与 Markdown 第 153–203 行逐项比对，辅以 `pdftotext -f 5 -l 5`。
- 结果：**PASS±**
  - Luna 旧修复逐项复核为正确：Theorem 1.8 第二条假设为 `$A ^ { d } \leq r$` 无下标 i（印刷无下标，PNG 直接可辨）；Theorem 1.6 两条假设与 Theorem 1.8 三条假设的 bullet 均已恢复，与印刷列表一致。
  - 阈值公式 `lct(X,B,|A|_R) ≥ t`、`lct ≤ 1`、`lct(…|A|_R)=lct(…,D)`、`lct < 1` 及 `[42, Question 1]`、`[11, Conjecture 1.12]`、`[19][18]`、`[3]`、`[13]`、`[5]` 引用均与印刷一致。
  - PASS± 项（不修，登记）：①`different`→`diferent` 两处（第 155、169 行，ff 拍平）；②MD 第 185 行 `$i f B$` 把 if 排进数学斜体；③第 201 行 `$A ^ { d } \leq r$` 后缺印刷的逗号；④若干数学式与单词空格粘连。
- 备注：Luna p.005 登记的 `A^d ≤ r_i→r` 与 bullet 恢复均属实且已正确落地；`diferent` 登记属实。本次重检未发现本页数学内容错误。
- 记录时间：2026-10-03 12:33 EDT；actor=`Wf-R-P13`；model=`GLM-5.3-Flash`；effort=max（run级配置，自报UNKNOWN）。
