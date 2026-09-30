# AUDIT — Grisha Perelman《Ricci flow with surgery on three-manifolds》（arXiv:math/0303109v1，LaTeX born-digital，22p）

> mineru: standard 档云端解析；审计依据 = pdftotext 文本层逐字符对账（可靠 born-digital，0 FFFD）
> + `audit/per2003b_pNNN.png`（pngmono 150dpi 全 22 页已渲染；**重公式页 p.2/5/8 全页目检 +
> 关键疑点 300dpi 放大 3 处**——本篇以可靠文本层为主通道、PNG 抽验为辅，与纯扫描篇的
> 全页目检流程不同，特此如实登记）。
> **伪影族**：引用 § 丢失 ×15（[I,§11]/[H 5,§4,5]/[H 2,§17]/[H 4,§4]/[I,§4]/[H 2,§13]/
> [H 5,§4]/[I,§7]/[H 4,§2,7]/[H 4,§8-12]/[H 4,§8-10]/[H 4,§11,12]/[P,§2]/[I,§1,2]/[I,§13.2]）、
> 丢箭头 → ×8、`\vec t`/`\dot Q`/`\top(A)`/`\Xi`/`\natural`/`\check S` 乱码 ×8、缺空格/句号 ~15、
> 页码串入 ×3、Hamilton 引语标点、L√(−t₀) 乱码、𝓛-exponential 丢 𝓛、M_can→M_cap、
> References 末两条丢 [P]/[W] 标签。

## 逐页签（文本层主通道；PNG 抽验页全页目检）
- **p.001-002**：arXiv 边条/题录/Grisha Perelman 脚注（St.Petersburg/emails）✓；§0 前言
  （[I,§13] 两例外/R_MAX=Γ Hamilton 引语标点修复/两 scale bounds h,r）✓；Notation and
  terminology（B/P/ε-neck/strong ε-neck/ε-tube/ε-horn/double ǫ-horn/ε-cap/capped ǫ-horn）✓；
  **p.2 全页目检** ✓ — **PASS±**（±：arXiv 边条未收）
- **p.003-004（§1.1-1.5）**：ancient κ-solutions/I.11.7 冗余假设/I.11.2 渐近 soliton 分类 ✓；
  **Lemma 1.2**（无非compact soliton）证明：式(1.1)(1.2)/第二变分/level surfaces 凸性/
  Gauss-Bonnet 反证 ✓；1.3 分类/1.4 Example（S³ 长圆柱+双帽；Harnack [H 3]；距离变化估计
  [H 2,§17]；**"less than L√(−t₀)"** 300dpi 终裁修复）✓；1.5 κ₀/η/式(1.3)/四类 canonical
  neighborhoods ✓ — **PASS**
- **p.005-007（§2 standard solution）**：Claims 1-5 全部（旋转对称 Killing/唯一性线性化方程组/
  延拓到 [0,1)/blow-up 反证/Claim 5 + R_min 估计）✓；**p.5 全页目检**（"T≤1."/"≪"/"B(p,0,
  ε⁻¹), t<3/4" 修复生效）✓ — **PASS**
- **p.008-009（§3 第一奇异时刻拓扑 + §4 Ricci flow with cutoff）**：Ω/Ω_ρ/五种 subset 类型
  (a)-(e)/M 拓扑重构 ✓；4.1 两个 a priori 假设（pinching/canonical neighborhood）✓；
  4.2 Claims 1-2（R≤8Q/dist ≥ AQ₀^{-1/2} 修复）✓；4.3 Lemma（δ-neck 收缩反证/Toponogov
  分裂 S²×ℝ）✓；**p.8 全页目检**（[−1,0]/[−2,0]/δ-cutoff 修复生效）✓ — **PASS**
- **p.010-012（§4.4-4.7 + §5 命题 + 5.2/5.3）**：surgery 定义（Hamilton [H 5,§4] 共形因子
  e^{−f}/pinching 改善）✓；4.5 Lemma (a)(b) ✓；4.6 Corollary（∫>l）✓；4.7 Corollary
  （T_x≤T₀+θh²）✓；5.1 normalized/(5.1)/Proposition（r_j/κ_j/δ̄_j 序列归纳）✓；
  5.2 κ-noncollapsing/barely admissible curves/𝓛₊ ✓；5.3 Lemma（△t=εr₀⁴𝓛^{-2}）✓ — **PASS**
- **p.013-015（5.4 反证 + §6 Long time behavior I）**：5.4 反证框架（t̄/κ-noncollapsing/伸缩
  极限/Q₀/Q₁/Alaoglu-Bourbaki→Lemma 6）/h≪r 修复 ✓；6.1 摘要/正标量曲率情形（Schoen-Yau/
  Gromov-Lawson [G-L]）✓；6.2 **Correction to Theorem I.12.2**（原 I.12.2 不正确）✓；
  6.3 Proposition (a)(b)(c) + (6.1)(6.2)(6.3) ✓；"right hand side×2"（print 即此重复，忠实）✓；
  "apply Lemma 5.3."（杂散 C 删除）✓ — **PASS**
- **p.016-018（§6.4-6.8 + §7 开头）**：6.4 Proposition（2C₁h≤r₀/r(t₀) 情形）✓；6.5 Lemma
  （K₀τ^{-1}/体积 1/10）✓；6.6 Lemma（Aleksandrov/θ₀）✓；6.7 归纳（τ=min/K=max/△t=
  C(A)^{-1}r²/θ₀(1/10)r₀/4 修复）✓；6.8 Corollary（θ^{-1}(w)h/−r₀^{-2} 修复）✓；
  §7/[H 4,§2,7]/(7.1)(7.2) ✓；"the long tome behavior"——**print 即此源级 typo，忠实** ✓ —
  **PASS±**（±：tome/chose/then 三处源级）
- **p.019-021（§7.2-7.4 + §8 + References）**：7.2 Lemma (a)(b)(c)（(7.5)|2tR_ij+g_ij|<ξ）✓；
  7.3 thin part M⁻(w,t)/(7.6)/hyperbolic limits/standard truncation H₁(w′) ✓；7.4 collapsing
  theorem 三假设/**"−r^{−2}"** ✓；exceptional case（flat manifold）✓；[P,§2] ✓；
  graph manifolds [W] ✓；8.1 第一特征值/λ 梯度流/Lemma（λ⁺−λ⁻≥ξ(V⁺−V⁻)）✓；
  (8.1)(8.2)/"Clearly is satisfies"——**print 即此源级 typo，忠实** ✓；M_cap 修复 ✓；
  8.2 (a)(b)(c)（λ>0/λ̄=0/λ̄<0 几何化描述）✓ — **PASS**
- **p.022（References [I]-[W]）**：11 条文献逐条核对 ✓；**末两条 [P]/[W] 标签补入**（md 原缺）✓
- 结果：**FAIL（单点）→已修**

## 总评

- **覆盖声明**：22/22 页经可靠文本层逐字符对账 + md 全文交叉核对；150dpi 全 22 页渲染，
  重公式页 p.2/5/8 全页目检 + 300dpi 疑点放大 3 处（L√(−t₀)/R̄^{-1/2}/[I,§11]）。
  **本篇验证方式与扫描篇不同（文本层为主通道），如实登记。**
- **FAIL 修复（100 组，三轮）**：①§ 丢失 ×15；②丢箭头 → ×8（R→R̄/R(x)→1/L→∞/t→T/
  α→∞/δ̄→0/τ→0⁺ 等）；③乱码记号 ×8（\vec t/\dot Q₀/\top(A)/\bar ξ/\natural_t/\check S̄/
  \tilde θ₀/\dot Q）；④中文逗号 ×2/双逗号/页码串入 ×3/幽灵 "$$1" 粘连；⑤Hamilton 引语
  "(R_MAX = Γ," 标点；⑥L√(−t₀) 乱码 + 𝓛-exponential/𝓛-length 补 𝓛；⑦M_cap（M_can 误读）；
  ⑧6.8 "−r₀^{-2}"/定理(3) "−r^{−2}" 指数；⑨句号/逗号/粘连 ~15；⑩References [P]/[W] 标签补入。
- **源级 quirk 清单（忠实不改）**："the long tome behavior"、"one can chose δ(t)"、
  "greater then log h"、"Clearly is satisfies the equation"（四处均 print 即此）；ff→f 连字族
  （diferent/Diferentiating/difeomorphic/coeficients/suficiently/cutof/efectively/unafected
  等）；"right hand side" 重复（print 即此）；Lemma 29 式 "e_i(m|I)"（无此篇——略）。
- **可用性结论**：修复后 md 可作该 arXiv 论文忠实底本；(1.1)-(8.2) 编号公式逐一核对全对；
  参考文献 11 条现已带齐全标签。本篇 22/22 页完成，无未决项；与 entropy（39p，待审）、
  finite extinction（7p，已审 ✅）构成 Perelman 三部曲。

### 修复登记（2026-09-30）
- **三轮共 100 组替换全部命中**（§×15、箭头×8、乱码记号×8、标点/粘连/页码 ~25、M_cap、
  [P]/[W] 标签）；L√(−t₀)/−r₀^{-2} 等经 300dpi/文本层双证。
- 本篇 22/22 页完成，无未决项。
