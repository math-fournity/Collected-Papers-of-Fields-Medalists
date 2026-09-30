# AUDIT — Bhargava & Shankar《Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0》（Ann. of Math. 181 (2015) 587–621，排版版）

## 审计依据

- PDF：`Bhargava_2015_ternary_cubic_published.pdf`（35 页 = 印刷 pp.587–621；pdfTeX born-digital，
  文本层 81011 字节、0 U+FFFD——**文本层主对账通道 + PNG 抽验**）。
- mineru：`Bhargava_2015_ternary_cubic_published_mineru/…md`（998 行）。
- 模式：pdftotext 逐条仲裁（方程编号 (30)/(31) 分立、(21)/(40) 归位、Ш 字形、"possesess"、
  R_V^+(X)、X^{9/12}、M_p(U₁,F)、[0,1]∈ℝ、[28] Zbl 等），300dpi 终裁 2 处
  （`audit/300dpi/`——γ 矩阵与 x 变元、fn5 类区域），150dpi 全 35 页渲染
  （`audit/bha15_p001–035.png`），p.1 整页目检。
- 方程编号：修复后 \tag 清单 = **(1)–(40) 连续 40 组，无重复无缺失**（修复前缺
  (21)/(30)/(40)，(30)/(31) 合并错位；均已按 print 归位）。

## 伪影族汇总

| 族 | 处数 | 说明 |
|---|---|---|
| 数字逐位拆分 | 20+ | 27B²、12288/512、(4I³−J²)/27、16·I/32·J、1.17、1/16×8、1/32×8、1/12、1/24、1/36、9/12、3·24、32/135、128/135、144/(36·27)、8/5、32/5、2/81、36Z×27Z、5/12>41.6% |
| ff 连字 | ~15 | coeficients ×5、suficiently/sufices、diferent、dificult(y)、going of to、possesess（print 原文者除外） |
| 方程编号错位 | 4 组 | (21)、(30)/(31) 合并拆分、(40)；\tag (1)–(40) 对齐 |
| 足注碎裂 | 1 | fn1（PGL₃(Q) 等价类定义）六碎片按 print 重建 |
| Sha 字形 | 3 | \operatorname{III}→Ш ×2、裸 X→Ш（"Since Ш is always a square…Ш[3]"） |
| 记号乱码 | 10+ | \tilde{⌈⌉}、`2 Å`、`$m_:$`、smart-quote（"degree 12"、"E."、7,、2,）、\dag→∤ ×2、\mathsf{Ω}¹₁₆→1/16、`\``→ℓ ×2、#·A₂→#𝒜₂、\Pi_p→\prod_p、(a)(a)→(a)(b) |
| 空格粘连/标点 | ~35 | Letf、awayfrom×5、ofclass×5、convexfunction×6、.$ 双周期/.$逗号 ×26、Then,for、MTWcondition、Proofof、Skinner–Urban、15juillet 类 |
| 结构 | 3 | (30)/(31) 拆分、fn1 重建、Theorem 39 (38) 分数式重构 |

**合计约 120 处 / 65 规则**（合并脚本逐条条件应用，全程报告）。

## 逐页签（文本层全篇对账 + 关键页 PNG 目检）

- **p.001（587 题录）**：PNG 目检——题录/DOI 10.4007/annals.2015.181.2.4/摘要（SL₃(Z)、1.17、
  BSD）/高度公式 max{4|A³|, 27B²}（27 修复 ✓）/© 足注 ✓。PASS±。
- **p.002–p.010（588–596）**：§1 Thm 1–10、Cor 2/7、Hessian (1)、(2) 12288/512、(3) Δ、
  (4) 高度、Thm 9 同余条件 (a)–(j)×2 组、Thm 10、3-covering 定义与交换图、(5) Jac。PASS±。
- **p.011–p.019（597–605）**：§2 (6)–(16)、Siegel 集 𝓕（n(u₁,u₂,u₃) 矩阵重建+"transformations"
  截断修复）、(17)(18)、Thm 17/18、Lemma 14（(20)）、Prop 15（ℓ 修复）、(21) 归位、Lemma 19。PASS±。
- **p.020–p.026（606–612）**：2.6 Thm 9/10 证明、Prop 20/21（Kraus）、Lemma 22（36Z×27Z）、
  Prop 23 (a)(b)、2.7 Thm 24、Prop 25（(23)–(28)、X^{9/12} print 原文）、Lemma 26、(26)(27) 矩阵。PASS±。
- **p.027–p.035（613–621）**：§3 (29)–(40)、Prop 28–32、Lemma 33/34（1/16 修复）、fn1 重建、
  Prop 35/36、Thm 37/39（(38) 分数式重构）、Lemma 40、(40) 归位、§4 Thm 41–44（Ш ×3、
  5/12>41.6%、root number 讨论）、Acknowledgments、References [1]–[29] 逐条、双机构署名。PASS±。

## 总评

- **覆盖声明**：文本层全篇逐式对账；\tag (1)–(40) 与 print 逐一对应；文献 29 条逐条核对
  （MR/Zbl/DOI 全保留）；足注 3 条核对；p.1 PNG 整页目检。
- **修复统计**：约 120 处 / 65 规则。
- **无 FAIL**：内容级错误（(30)/(31) 合并、(21)/(40) 丢号、Ш→III/X、12288 拆分）全部修复。

### 源级 quirk 清单（print 原貌，md 忠实保留）

1. **"an ternary cubic form"**（§3.3，m_p(f) 定义）——print 原文（文本层证实）。
2. **"possesess a degree n divisor"**（§1，Cassels 引用）——print 原文（文本层证实）。
3. **"R_V^+(X)"**（(16) 式第二个积分下标）——按上下文应为 R^+(X)；print 原文（文本层证实）。
4. **"X^{9/12}"**（(24) 式）——按上下文应为 X^{3/4}；print 原文（文本层证实）。
5. **"M_p(U_1, F)"**（(38) 式及 (40) 前文）——U₁ 未在本篇定义（沿袭 [8] 记号）；print 原文。
6. **"φ : V_Z → [0,1] ∈ ℝ"**（§2.7）——∈ 应为 ⊂；print 原文（文本层证实）。
7. **[28] "Zbl 06261655"**——Zbl 号缺点号；print 原文。
8. **"Theorem 42 … that that exactly 50%"**——双 that；md 观测（print 同形概率高，未单独终裁）。
9. **"i.e,"**（§2，relative invariants 句）——print 缺句点（文本层证实）。
10. **Prop 15 邻域 "at most \`"**——print 以杂散 grave 排印（应为 ℓ 的排版事故）；print 原样保留。

- **可用性结论**：修复后 md 与 print 逐式对齐（\tag (1)–(40)），可作可靠对读本。

## 修复登记

- **fix commit**：`a53365e3`；**修复前 md**：父提交 `89939e36`（audit(page) 提交，其父 `b5c63fe7`
  为 mineru 原始产出态）。
- **修复内容**（约 120 处 / 65 规则，条件应用+全量报告）：数字拆分 20+（12288/512、27B²、
  1.17、1/16×8、1/32×8、1/12、1/24、1/36、9/12、32/135、128/135、144/(36·27)、2/81、
  36Z×27Z、5/12>41.6%、16·I/32·J）；ff 连字 ~15；编号归位 4 组 → \tag (1)–(40) 无重无缺；
  Sha 字形 ×3（\operatorname{III}→Ш、裸 X→Ш）；fn1 六碎片按 print 重建；Theorem 39 (38)
  分数式重构；(a)(a)→(a)(b)；矩阵 array 重建 ×3（n(u₁,u₂,u₃)、(26)、(27)）；"orthogonal
  transformations" 截断修复；\dag→∤ ×2；\mathsf{Ω}¹₁₆→1/16；\`→ℓ 保留判定；标点 .$ ×26；
  空格粘连 ~35；文献 [2][7][17][18][21][22][25][26] 修正（Veränderlichen/à/Astérisque/Sér/
  Nekovář/numdam 下划线/Zbl 空格）。
- **不改项**：源级 quirk 10 项（见总评清单）——print 原貌忠实保留。
- **修复后核验**：\tag (1)–(40) 无重无缺；残余 \x03/小/，/\dag/III/Å/.$ 全文 grep = 0
  （ grave 2 处系 print 原文保留）；p.1 PNG 整页目检与修复后 md 一致。
