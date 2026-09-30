# AUDIT — McMullen 1991《Cusps are dense》（Ann. of Math. 133 (1991) 217–247）

## 审计依据

- PDF：`McMullen_1991_cusps_dense.pdf`（31 页 = 印刷 pp.217–247；PDF p.N = 印刷 p.216+N；
  Producer: PDFlib Lite / page2pdf——**图像型扫描件，pdftotext 文本层 0 字节**）。
- mineru：`McMullen_1991_cusps_dense_mineru/McMullen_1991_cusps_dense__McMullen_1991_cusps_dense.md`
  （1178 行，云端 standard 档导出）。
- 模式：**扫描件纯 PNG 审计**——31 页全部 150dpi pngmono（`audit/mcm91_p001–031.png`）逐页目检，
  与 md 对应段逐条比对；疑点 7 处做 300dpi pnggray 终裁（`audit/300dpi/` 8 件）。
- 方程编号：print 共 4 组编号公式 (2.1)(2.2)(3.1)(3.2)；修复后 md \tag 清单与之对齐，无重复无缺失。

## 伪影族汇总（mineru 系统性瑕疵，本篇实际命中）

| 族 | 处数 | 说明 |
|---|---|---|
| ∫ 积分号误识为 f | 2（+丢竖线 1） | p.6 Idea of proof：(that is, \|∫μdz²\| ≪ ∫\|μ\|\|dz\|²) |
| 花体拍平（𝓛/ℓ/𝐑/𝒮/𝔅/𝒢） | 16 | §3 定义、§4.2、Examples、§5 Proof of 1.2 等 |
| 引用键 digit 1→l | 1 | [Be1]→"[Bel]"（p.5） |
| Γ 下标 Y→γ | 2 | p.21 §4 开头两处 Γ_γ（应为 Γ_Y） |
| OCR 噪声 Ċ（dot 附加） | 2 | p.16 Prop 3.3、p.22 Prop 4.1 证明（print 纯 C） |
| 乘积降为下标 m𝓛→m_𝓛 | 1 | p.22 r = C + log(1/\|m𝓛\|) |
| 行内文字误排为居中 display | 1 | p.24 "Finally d₀Σ…" 整行 |
| 裸编号行 (3.1) 与 display 分离 | 1 组 | p.17；已归位 \tag{3.1} |
| 文献作者名 OCR 错 | 1 | [Sh] H. SHIGA→"SHICA"（300dpi 2x 终裁） |
| 文献重音丢失 | 1 | [P] H. POINCARÉ→"POINCARE"（300dpi 终裁） |

**合计 31 处 / 17 规则**（详见文末修复登记）。

## 逐页签

> 每页核对：running head/页码、正文逐句、全部行间公式与行内式、图及题注、足注、文献条目。
> 全篇 31 页**无 FAIL**；PASS± 均为 mineru 伪影（已修复）或 running head 丢失（系统性，记一次不逐页重复）。

## p.001–p.005（印刷 217–221：题录、§1、Thm 1.1/1.2、Cor 1.3、Figure 1、Prop 1.4、Cor 1.5、Proof of 1.1）

- PNG：audit/mcm91_p001.png–p005.png（pngmono 150dpi）
- 核对：题录（标题/作者/摘要/NSF 足注/running head "Annals of Mathematics, 133 (1991), 217–247"）、
  ι 嵌入式、Definitions（cusp/totally degenerate/maximal cusp）、Thm 1.1/1.2、Remarks 1–2、
  Cor 1.3 及证明、Figure 1（mineru images/page_3_image_6.jpg 在库）、Prop 1.4+证明、
  "[Sh., Cor. 1]"、Cor 1.5+证明、Proof of 1.1 全段
- 结果：PASS±（running head+页码丢；斜体拍平；作者行 `\*` 为合法 markdown 转义渲染正确）
- 备注：p.3 足注 1 "A **palatable** discussion…" 经 PNG 证实系 print 原文；p.5 "[Bel]"→[Be1]
  为 OCR 错已修复

## p.006–p.010（印刷 222–226：Cor 1.6/1.7、Idea of proof、Figure 2、Outline、§2 至 Thm 2.2、(2.1)(2.2)、Cor 2.3、Q(X)）

- PNG：audit/mcm91_p006.png–p010.png
- 核对：Cor 1.6/1.7+证明、Idea of the proof of Theorem 1.2（含 \|∫μdz²\|≪∫\|μ\|\|dz\|²）、
  Figure 2（题注 "An **invariant** line field" 经 300dpi 证实）、Outline、Acknowledgements
  （print 明写 "proof of Proposition 3.4"）、Bibliographical remarks、Notation（"Jørgenson"
  print 原样）、Schwarzian 定义式、Beltrami 方程、Prop 2.1+核 K(z,w)、(2.1)、分段函数例子、
  §2.1、Thm 2.2 主式+证明、(2.2)、Cor 2.3+证明、Q(X)/配对/Θ 算子
- 结果：PASS±（p.6 ∫→f ×2 已修复；其余仅 running head/斜体）

## p.011–p.015（印刷 227–231：Thm 2.4、§2.2、Prop 2.5、Cor 2.6、§3 定义、Thm 3.1、Remarks、Figure 3、Prop 3.2）

- PNG：audit/mcm91_p011.png–p015.png
- 核对：Thm 2.4+对偶式、§2.2 L-thin part 定义、L₀=log(3+2√2)、Prop 2.5+证明积分式、
  Cor 2.6+证明、§3 𝓛=ℓ+iθ 定义、模数定义（print "1<\|z\|<**log M**" 源级 quirk 登记）、
  M=4π²Re(1/𝓛)、annulus 构造 4 要素、Thm 3.1 主式、Remarks 1–4、§3.1 Spirals、γ(z)=N(exp𝓛)N⁻¹、
  格点 Λ=Z⊕Zτ、p_Ω/p_T、C(y)、m=4πy、M=2πIm τ、Figure 3、Prop 3.2+Remark
- 结果：PASS±（p.12–13 𝓛/ℓ/𝐑 花体拍平 ×7 已修复）

## p.016–p.020（印刷 232–236：Koebe 论证、Prop 3.3、§3.2、(3.1)、"Prop 2.3"、Prop 3.5、(3.2)、Cor 3.6、Thm 3.1 证明）

- PNG：audit/mcm91_p016.png–p020.png
- 核对：Koebe 1/4 引理、Prop 3.3+证明（常数经 300dpi 裁为纯 C）、§3.2 Descent to the torus、
  φ/Φ/ψ/Ψ 定义、(3.1)（裸编号行已归位 \tag）、**"PROPOSITION 2.3"（print 自身错号，源级登记）**、
  Shishikura 级数、Prop 3.5（a₀=𝓛/6、aₙ 公式）、(3.2)、sinh⁴ 不定积分、平行四边形留数计算、
  Cor 3.6+证明、"Proof of Proposition 3.4"（y′=min(Im s, Im τ−s)) print 笔误登记）、
  Proof of Theorem 3.1 全链、A_n 定义
- 结果：PASS±（p.16 Ċ→C 已修复；两处 print 原文 quirk 忠实保留）

## p.021–p.025（印刷 237–241：Weierstrass 𝔭 remark、§4、Prop 4.1、§4.2、Thm 4.2、Lemma 4.3、Figure 4、Prop 4.4、§4.3、Thm 4.5）

- PNG：audit/mcm91_p021.png–p025.png
- 核对：𝔭(s)/Ψ(s) Weierstrass 式（md \mathfrak{p} 忠实）、§4 开头（Γ_γ×2 已修复为 Γ_Y）、
  Margulis 常数/管、shadow 定义、Prop 4.1（"B(γ,𝓛,m**;p**)" 分号经 300dpi 证实为 print 原样；
  "The shadow of S of τ" 词序 print 原样登记；r=C+log(1/\|m𝓛\|) 经 300dpi 修复）、
  §4.2 α-scattered 定义（𝒮 花体已还原）、Thm 4.2（print 确用 "3α × diam(S₀)"，md 忠实）、
  Lemma 4.3+归纳证明（print "(dᵢ,d_{k+1},…)" 笔误忠实保留）、Examples（𝔅/𝒮 已还原；
  "Finally…" display 误排已复位行内）、Figure 4、visual metric、Prop 4.4+证明、
  §4.3 𝒢 集合、M=inf 4π²Re(1/𝓛ᵢ)、Thm 4.5 陈述
- 结果：PASS±

## p.026–p.031（印刷 242–247：Thm 4.5 证明、§5、Prop 5.1/5.2、Proof of 1.2 完成、Princeton 署名、REFERENCES 31 条、Received）

- PNG：audit/mcm91_p026.png–p031.png
- 核对：Thm 4.5 展式+证明全链（Eᵢ 不变性/嵌套论证，跨页断点与 md 分段一致）、⟨Eⱼ⟩ 角括号、
  §5 定义 γ_X̄/γ_Y、Figure 5、𝓛(γ) 计算（"1∈Λ … along Λ" print 原样）、Prop 5.1/5.2+证明、
  Proof of 1.2（"By **Theorem** 2.6" 与 "m<M for L **large** enough" 两处 print 原文 quirk 登记；
  𝒢 花体已还原；Lemma 5.3+证明；"there exist a γ, 𝓛" 花体已还原；最终不等式链）、
  PRINCETON UNIVERSITY 署名、REFERENCES [Ab1]–[Y] 31 条逐条（作者/题名/卷期页年）、
  (Received May 16, 1989)
- 结果：PASS±（[Sh] H. **SHIGA**、[P] H. Poincaré**É** 经 300dpi 修复；"The **Bierberbach**
  Conjecture" [T2] 系 print 原文拼写，忠实保留）

## 总评

- **覆盖声明**：31/31 页全览（150dpi pngmono 逐页目检，无抽样）；行间公式与行内式逐条比对；
  文献 31 条逐条核对；足注 2 条核对；图 5 幅全部在 mineru images/ 且位置正确。
  300dpi 终裁 8 件入库 `audit/300dpi/`（Figure 2 题注 / Prop 3.3 常数 / Prop 4.1 分号与词序 /
  r 式 / Prop 5.2 B′ 式逗号 / [Sh] SHIGA / [P] POINCARÉ）。
- **修复统计**：31 处 / 17 规则（rep 断言一次通过，无手工补刀）；方程编号 \tag{2.1}{2.2}{3.1}{3.2}
  与 print 对齐，无重复无缺失。
- **无 FAIL**：全部数学内容级差异均为 OCR 伪影且已修复；print 原貌差异按下表忠实保留。

### 源级 quirk 清单（print 原貌，md 忠实保留，禁止"顺手改正"）

1. **"PROPOSITION 2.3"**（p.233，§3.2 主估计）——应为 3.4：print 自身错号（同页 print 后文
   "Proof of Proposition 3.4"、p.223 Acknowledgements 均用 3.4）。证据：mcm91_p017.png。
2. **"1 < |z| < log M"**（p.229，模数定义括注）——按 print 自身柱高约定应为 e^M；print 原文如此。
   证据：mcm91_p013.png。
3. **"y′ = min(Im s, Im τ − s))"**（p.236，Prop 3.4 证明）——应为 Im τ − Im s，且 print 有双右
   括号（md 归一化括号数，数学内容保留 print 原样）。证据：mcm91_p020.png。
4. **"(dᵢ, d_{k+1}, …, d_{n+1})"**（p.240，Lemma 4.3 归纳）——应为 d_{i+1}；print 原文。
   证据：mcm91_p023.png。
5. **"By Theorem 2.6"**（p.244，Proof of 1.2）——所引条目实为 Corollary 2.6；print 原文。
   证据：mcm91_p028.png。
6. **"Then m < M for L large enough"**（p.244）——按数学应为 small（下句 "this already holds
   under our assumption that L < 1/2" 自释意图）；print 原文。证据：mcm91_p028.png。
7. **"at 'distance O(exp(r))"**（p.238，Prop 4.1 证明 2）——杂散撇号；print 原样（md 保留）。
8. **"The shadow of S of τ from p"**（p.238，Prop 4.1 结论 1）——词序应为 "The shadow S of τ"；
   print 原样（300dpi 证实，audit/300dpi/mcm91_p22_shadowS_300.png）。
9. **"The Bierberbach Conjecture"**（p.247，[T2] 书名）——应为 Bieberbach；print 拼写原样。
   证据：mcm91_p031.png。
10. **"Jørgenson"**（p.224）——print 拼法（通称 Jørgensen）；md 忠实。
11. **文献缩写/大小写不一致**：[Ab1] "Acta. Math." vs [Be2] "Acta Math."；[KT] "Inv. Math." vs
    [Mc] "Invent. Math."；[Be3]/[Mas1] 标题内 "kleinian" 小写——print 自身不一致，md 忠实。
12. **"1 ∈ Λ … along Λ"**（p.243，𝓛(γ) 计算）——记号 Λ 复用（§3.1 格点）；print 原样。
13. **Prop 4.1 "B(γ,𝓛,m;p)" 分号** vs 全篇他处逗号（含 p.244 "B(γᵢ,𝓛ᵢ,m′,p)" 逗号，300dpi
    分别证实）——print 自身不一致。
14. **"(For m small, no pair of nested Eᵢ's…)"**（p.243）——print 原样（md 忠实）。

- **可用性结论**：修复后 md 可作本论文全文可靠对读本；图 5 幅、足注 2 条、文献 31 条完整；
  唯 print 自身错号/笔误（上表）在 md 中原样保留，引用 Proposition 3.4 时请注意 print/md
  均作 "PROPOSITION 2.3"。

## 修复登记

（fix(md) commit 后追加）
