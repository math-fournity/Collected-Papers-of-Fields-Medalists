# AUDIT — A. Okounkov & N. Reshetikhin《Correlation function of Schur process with application to local geometry of a random 3-dimensional Young diagram》（J. Amer. Math. Soc. 16 (2003), 581-603，born-digital，23p）

> mineru: standard 档云端解析；审计依据 = pdftotext 文本层逐字符对账（可靠 born-digital，0 FFFD）
> + `audit/ok2003_pNNN.png`（150dpi 全 23 页已渲染；p.1/15/17/18 全页目检——含 Figure 4/6 及
> Theorem 2/(35) 关键页）。**本篇 md 为全程最洁净导出**（无 U+FFFD/无中文标点/无连字粘连），
> 修复集中于细节（31 组）。
> **伪影族**：双分号 ";;"、(8) 标签被污染为 \tag{2.2.5.}、overleftarrow-Π/Q 符号混淆并
> "operators Qare" 粘连、"eIt" 粘连、Contours 公式间缺逗号、\bar τ 乱入、<sub> 残留 ×3、
> 丢箭头 → ×9（r→+0 等）、λ₄→λ₃、|ξ|<2 双逗号、𝒜_j^{*s} 乱码、图题逗号缺失、[P]/[W] 型
> 引用完整。

## 逐页签（文本层主通道 + p.1/15/17/18 全页目检）
- **p.001（print 581：题录 + §1.1/1.2/1.3 开头）**：JAMS 刊头/题名/两作者 ✓；Schur measure
  （"weights **a partitions** λ"——print 即此源级 typo，忠实）/Schur process 定义 ✓；
  correlation functions determinantal form ✓；脚注（Received December 8, 2001/MSC 05E05,
  60G55）✓ — **PASS±**（±：AMS 版权行/下载横幅未收）
- **p.002-005（print 582-585：§1.2-2.2.5）**：3D diagrams/plane partitions/q^|π| (1) ✓；
  Vershik [19]/domino tilings [2,4,5,13]/Conjecture 13.5 ✓；quantum dilogarithm (24) 预告 ✓；
  universality ✓；§2.1 partition/Schur process/对角切片 (3)/(4) 交错条件 ✓；**Figure 1**
  （3D diagram）✓；Example (2)↔(2)≺(3,1)≺(5,3,1) ✓；2.1.3 映射 𝔖(λ)（"of the **of the**
  set"——print 即此源级，忠实）✓；2.2.1/2.2.2 φ(z) 条件 ✓；2.2.3 (6)/Wiener-Hopf 分解 ✓；
  Jacobi-Trudy/h_k=φ⁺ ✓；**(8) 标签修复（原 \tag{2.2.5.} 污染）** ✓；Definition 1 (9) ✓ — **PASS**
- **p.006-008（print 586-588：§2.2.6-2.2.12）**：vertex operators Γ±/coeficient（ff 登记）✓；
  (10)(11) ✓；**"$\overleftarrow{Q}$ denotes the time-ordered product"（Π→Q 符号修复 +
  "operators Qare"→"operators are"）** ✓；Definition 2/(12)/Z 计算 ✓；(14) Schur measure ✓；
  2.2.10 restriction/2.2.11 continuous time/2.2.12 φ_3D (15)/McMahon 生成函数 ✓ — **PASS**
- **p.009-011（print 589-591：§2.3 correlation functions）**：Definition 3/(16) ✓；
  2.3.2 R_U/(17) ✓；2.3.3 Ψ_x(t)/**Lemma 1 (Wick formula) (18)** ✓；kernel K 定义 ✓；
  2.3.4 (19)/Ψ(t,z)/Φ(t,z) (20) ✓；**"Ad(Γ±)·ψ*(z)=φ^{∓}(z^{-1})^{-1}ψ(z)"——print 即写
  ψ(z)（源级，忠实不改；据 (42) 应为 ψ*(z) 的符号性笔误）** ✓；Theorem 1/(21)(22) ✓ — **PASS**
- **p.012-014（print 592-594：§2.3.5-3.1.4）**：Φ_3D (23)/quantum dilogarithm (24) ✓；
  2.3.6 rhombi tilings/(25)/**Figure 3** ✓；Corollary 1/(26) ✓；§3.1/(27) saddle-point 原理 ✓；
  3.1.2 **Lemma 2**（r³|π|→2ζ(3)）✓；3.1.3-3.1.4 (28) dilog ✓ — **PASS**
- **p.015（print 595：S 函数 + 临界点 + Figure 4）**：S(z;τ,χ) 定义/critical points 二次式/
  (30)(31) ✓；3.1.5 对称性质/Re S 常值/(32) 交点 ✓；**Figure 4**（gradient 场）✓；
  3.1.6 contours γ>,γ<,γ± 定义/**Figure 5 题注缺逗号修复** ✓；∫⁽¹⁾+∫⁽²⁾ ✓ — **PASS**
- **p.016-017（print 596-597：§3.1.7-3.1.10 + Theorem 2）**：3.1.7 incomplete beta 积分 ✓；
  **Definition 4** B± ✓；3.1.8/3.1.9 (33)(34) z_* ✓；**Theorem 2**（incomplete beta kernel
  行列式）✓；Remark 1/2 ✓；3.1.10 **Corollary 2** ρ*=θ*/π/**(35)**（**θ*=arg z_* 修复**）✓ — **PASS**
- **p.018-019（print 598-599：Figure 6 + Corollary 3 + 3.1.12-3.1.14）**：**Figure 6**（level
  sets）✓；**Corollary 3** discrete sine kernel ✓；(36) 双积分 ✓；3.1.13 (37)(38) z(τ,χ) ✓；
  (39) x,y ✓；**Figure 7**（limit shape）✓；3.1.14 [3] 参数化/f(A,B,C) ✓ — **PASS**
- **p.020-021（print 600-601：§3.2 Universality）**：3.2.1 principle/3.2.2 anisotropic ✓；
  3.2.3 equal time/3.2.4 poissonized Plancherel/K_Planch ✓；3.2.5 α→∞ asymptotics
  （|ξ|<2 修复/θ=arccos(ξ/2)/sin θΔ/πΔ）✓；3.2.6/3.2.7 **(40)**/Airy kernel ✓；3.2.8 [7]
  Airy process ✓ — **PASS**
- **p.022（print 602：Appendix 无限楔公式）**：Λ^{∞/2}V/v_S/【**v_λ 中 λ₄→λ₃ 修复**】/ψ_k/
  ψ_k^*/anticommutation/(41) ✓；α_n/Heisenberg/"see the formula."（print 即此，忠实）✓；
  (42)(43) ✓ — **PASS**
- **p.023（print 603：Acknowledgments + References + 地址）**：NSF DMS-0096246/DMS-0070931/
  CRDF RM1-2244 ✓；References [1]-[19] 逐条抽验 12 条全对（[5] math.CO/0008220/
  [8] math.CO/9906120 空格 print 即此）✓；Berkeley 地址/okounkov@math.berkeley.edu ✓ — **PASS**

## 总评

- **覆盖声明**：23/23 页经可靠文本层逐字符对账 + md 全文交叉核对；150dpi 全 23 页渲染，
  p.1/15/17/18 全页目检（含 Figure 4/6 与 Theorem 2 页）。
- **FAIL 修复（31 组）**：①(8) 标签去污染（原 \tag{2.2.5.}）；②$\overleftarrow{Q}$ 符号
  修复 + "operators Qare"→"operators are"；③Contours 图题公式间补逗号（$$ 粘连）；④
  θ*=arg z_* 修复（<sub> 残留）；⑤λ₄→λ₃（Appendix v_λ）；⑥丢箭头 → ×9（r→+0 等）；
  ⑦\bar τ 乱入；⑧|ξ|<2 双逗号；⑨A_j^{*s} 乱码；⑩"eIt"/stray paren/句号等细节 ~8。
- **源级 quirk 清单（忠实不改）**："weights a partitions λ"；"bijection of the of the set"；
  "probablistic"；"(6) in unambiguous"；"variety of specialization."；"how suitable the
  formula (22) is"；"see the formula."；"with the same integrand in as in (26)"；
  "Ad(Γ±)·ψ*(z)=φ^{∓}(z^{-1})^{-1}ψ(z)"（末位 ψ(z)——print 即此；据 (42) 应为 ψ*(z) 的
  原文符号性笔误）；ff→f 连字族（diferent/coeficient/sufices）。
- **可用性结论**：修复后 md 可作该 JAMS 论文忠实底本；(1)-(43) 编号公式（含对 Appendix (41)-(43)
  的前向引用）逐一核对全对；Figure 1-7 全部在位且引用一致；参考文献 19 条抽验 12 条全对。
  本篇 23/23 页完成，无未决项。

### 修复登记（2026-09-30）
- **31 组替换全部命中**（三轮；含 (8) 标签去污染、$\overleftarrow{Q}$、λ₃、θ*=arg z_*、
  r→+0 ×9 等）。fix commit 见父提交链。本篇 23/23 页完成，无未决项。
