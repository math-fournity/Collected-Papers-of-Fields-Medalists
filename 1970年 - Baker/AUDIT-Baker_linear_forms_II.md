# AUDIT — A. Baker《Linear forms in the logarithms of algebraic numbers (II)》（Mathematika 14 (1967), 102–107；Cambridge Core 扫描件，BFO 重打包）

> mineru: standard 档云端解析（OCR），导出 `Baker_1967_linear_forms_II_mineru/`；
> 审计依据 = `audit/baker2_pNNN.png`（pngmono 150dpi）逐页目检为主（文本层 OCR 噪声大，仅作参考）。
> 记号：本篇参数为 κ（与 (I) 俄译件的 х 相对应）。

## p.001（PDF p.1 / 印刷 p.102）
- PNG：audit/baker2_p001.png（pngmono 150dpi）
- 核对：题录（标题/A. BAKER）✓；§1 引言（† 引 (I) Mathematika 13 (1966), 204-216；‡ log z 固定分支
  z^w=e^{w log z}；‡† α₁,…,α_{m+1} 对数认定说明——三脚注文本均以 span 保留且逐字 ✓）；
  **Theorem 1**（iff 线性无关）/**Theorem 2**（transcendental）✓；(I) §5 归纳/Gelfond-Schneider ✓；
  height 定义、n⩾2、**(1) κ > 2n+1** ✓；**Theorem 3** 开头 C=C(n,α₁,…,αₙ,κ,d)>0 ✓
- 结果：**PASS±**（±：①页码 102 与页脚 "[MATHEMATIKA 14 (1967), 102-107]" 未收；②7 个孤立
  page_footnote 碎片/重复 span（z^w、α₁…α_{m+1} 等——碎片化伪影，脚注正文完整）

## p.002（PDF p.2 / 印刷 p.103）
- PNG：audit/baker2_p002.png（pngmono 150dpi）
- 核对：Theorem 3 结论式 |β₁logα₁+…| > Ce^{−(log H)^κ}（κ 指数）与 H 定义 ✓；
  κ>n+1→(1) 限制讨论段 ✓；2πi 排除的重要性/Liouville 1844/Ax 脚注 †（p-adic 类比/Leopoldt 问题、
  Illinois J. Math. 9(1965), 584-589、Brumer to appear）✓；§2 开头记号（c,c₁,c₂…）✓；
  反证假设 **(2)** ✓；ζ=½{1+κ/(2n+1)}、1<ζ<κ/(2n+1) ✓；ε=(1−1/ζ)/(2n)、h=[log H]、
  k=[h^ζ]、D=d^{2n−1} ✓；f_{m₁,…} 偏导定义 ✓
- 结果：**PASS±**（±：①页眉 "LINEAR FORMS…103" 未收；②页脚 † Ax 脚注在 p.2 底——md 中该脚注
  span 位于 §2 前后之间（位置漂移，内容完整））

## p.003（PDF p.3 / 印刷 p.104）
- PNG：audit/baker2_p003.png（pngmono 150dpi）；仲裁：audit/baker2_p003_300dpi.png +
  eq3_zoom4x.png、eq6_zoom4x.png（入库）
- 核对：**LEMMA 1**（p(λ) 整数、e^{2hk} 界、Φ 定义、L=[k^{1−ε}]、γ_r=λ_r+λₙβ_r）——但
  **(3)** md 作 e^{−½hκ}（乘积）——4x 证实**原刊为 e^{−½h^κ}**（κ 为 h 上标）→ FAIL；
  Proof See (I) Lemma 2 + ζ 变更说明 ✓；**LEMMA 2**/(4) e^{4hk}c₁^{L|z|} ✓；**LEMMA 3**/
  τ=2ε^{−1}{(κ−1)ζ^{−1}−1}+1、hk^{½εJ}、k/2^J ✓；**LEMMA 4**/(5) log|φ_j(0)|<−h^κ/log h
  （此处 md h^κ 正确，与 (3)(6) 形成篇内不一致——佐证 (3)(6) 系 md 误）✓；φ(z)=Φ(z,…,z) ✓；
  Proof：X=[½h^{κ−ζ}]、Y=[k/(8κ log h)]、[hk^{½εσ}]⩾X、[k/2^σ]⩾Y、(6)
  |φ_m(r)|<n^k e^{−½h^κ}——**md (6) 亦误作乘积 hκ → FAIL**；Γ/Λ 圆、E(z)={(z−1)…(z−X)}^{Y+1} ✓
- 结果：**FAIL（两点）**：(3) 与 (6) 指数 hκ 应为 h^{\kappa}（300dpi×2 证实）。
- 备注：± ①页眉 "104 A. BAKER" 未收；②(3)(6) 的 md 乘积形与 (5) 的幂形不一致——修复以幂形统一。

## p.004（PDF p.4 / 印刷 p.105）
- PNG：audit/baker2_p004.png（pngmono 150dpi）；仲裁：audit/baker2_p004_300dpi.png + ast_zoom.png（入库）
- 核对：**(7)** Cauchy/Γ_r/8^{Y+1} ✓；双和界 X(Y+1)8^{Y+2}n^k e^{−½h^κ}<(8n)^{k+2}h^κ e^{−½h^κ}
  <e^{−¼h^κ}（PNG 三处均 h^κ；md 首末两处误作乘积 hκ，中处正确——同行不一致佐证误识）→ FAIL；
  ξ/Ξ 上下界、(¼X log h)^{X(Y+1)}、ξ⩽e^{4hk}c₁^{LX log h} ✓；
  |φ(w)|⩽2e^{4hk}c₁^{LX log h}(¼ log h)^{−X(Y+1)}+(2X)^{2XY}e^{−¼h^κ}——md 末指数作
  **e^{−¼h\*}（κ 丢失成孤立星号）**→ FAIL（300dpi 证实 h^κ）；2XY log(2X)⩽{(κ−ζ)/(8κ)}h^κ⩽⅛h^κ
  （md 此处 h^κ 正确）✓；X(Y+1)⩾h^κ/(64κ log h)、(log h)^{−½X(Y+1)}、j!4^j⩽k^{kn+1}、
  ½X(Y+1)loglog h⩾2k^{n+1}log k、|φ_j(0)|⩽(log h)^{−¼X(Y+1)} ⇒ (5) ✓
- 结果：**FAIL（四点）**：三处 hκ→h^{\kappa}（双和界首末、|φ(w)| 花括号指数）+ 一处孤立星号
  h\*→h^{\kappa}。
- 备注：± 页眉 "…105" 未收。

### 修复登记（2026-09-29，阶段）
- p.3/p.4 的 5 处指数误识全部修复：(3)、(6)、双和界（3 连式 2 处）、|φ(w)| 花括号（hκ→h^κ ×4）、
  孤立星号 h*→h^κ（×1）。fix commit 见 `git log --grep 'fix(md): Baker linear forms II'`；
  修复前 md = 对应 fix commit 父提交。
- **状态**：p.1–p.4 已签；p.5–p.6 审计待续（§3 证明的 e^{−hκ} 两处待 p.5 目检后裁定）。

### 修复登记（2026-09-29，阶段·更正版）
- 更正：commit 627db85 实际包含 (3) 与孤立星号两处修复（此前登记表述有误）；本 fix commit
  包含 (6)、双和界两处、|φ(w)| 花括号三处。p.3/p.4 的 5 处 hκ→h^κ 至此全部完成。
- 剩余 e^{−hκ}×2（md 行 324/330，§3 证明）属 p.5 审计域，待 p.5 目检裁定。
- 状态：p.1–p.4 已签，p.5–p.6 待续（本篇审计中）。

## p.005（PDF p.5 / 印刷 p.106）
- PNG：audit/baker2_p005.png（pngmono 150dpi）；仲裁：audit/baker2_p005_300dpi.png +
  exp_zoom8x.png、bottom_band.png（入库）
- 核对：**LEMMA 5**（t₁,…,tₙ 整数界 T、|Σtᵢlogαᵢ| > c₂^{−T}）+ 证明（ω=a₁^{t₁}⋯aₙ^{tₙ}
  (α₁^{t₁}⋯αₙ^{tₙ}−1)、Norm ⩾ 1、2πi 非零倍数二择、|ω|⩾c₃^{−(D−1)T}、|e^z−1|⩽2|z|）✓
  - §3 开头：R=(L+1)^n−1、r 的 (L+1) 进制展开、p_r/p(λ₁,…,λₙ)、ψ_r=λ₁logα₁+…+λₙlogαₙ、
    Ψ_j=Σp_rψ_r^j (0⩽j⩽R) ✓；φ_j(0) 展开式 ✓；|ψ_r|<c₅L、j⩽R、由 (2) 得
    |(γ₁logα₁+…+γ_{n−1}logα_{n−1})^j − ψ_r^j| < (c₆L)^R **e^{−h^κ}**——8x 证实 κ 为上标，
    **md 作 e^{−h\kappa}（乘积）→ FAIL**（md 行 324；行 330 的同形待 p.6 裁定）
- 结果：**FAIL（单点）**：e^{−hκ}→e^{−h^{\kappa}}。
- 备注：± 页眉 "106 A. BAKER" 未收。

## p.006（PDF p.6 / 印刷 p.107）
- PNG：audit/baker2_p006.png（pngmono 150dpi；指数形态与 p.5 8x 裁定同族一致）
- 核对：|φ_j(0)−Ψ_j|⩽(R+1)e^{2hk}(c₆L)^R e^{−h^κ}（PNG κ 上标；md 乘积 → FAIL①）；
  L⩽h^{ζ(1−ε)}/R⩽h^{nζ}/κ>ζ(2n+1)、"at most e^{−½h^κ}"（PNG 上标；md 乘积 → FAIL②）；
  **(8)** log|Ψ_j|<−½h^κ/log h ✓（md 幂形正确）；Vandermonde Δ 定义与 ∏(ψ_s−ψ_r) ✓；
  |ψ_s−ψ_r|>c₂^{−L}、(L+1)^{2n} 对、log|Δ|⩾−c₇k^{2n+1}⩾−c₈h^{ζ(2n+1)} ✓；p₀≠0、行变换
  行列式展示 ✓；log|Δ|⩽log((R+1)!)+R²log(c₉k)−½h^κ/log h、R²⩽k^{2n}、(R+1)!⩽k^{nk^n} ✓；
  log|Δ|⩽−¼h^κ/log h、矛盾收尾 ✓；Trinity College, Cambridge ✓
- 结果：**FAIL（三点）**：①②两处乘积 hκ→h^{\kappa}；③**(Received on the 21st of March, 1967.)**
  收稿行整行丢失（页脚右下，md 未收）。修复：两处指数 + 补收稿行。
- 备注：± 页眉 "…107" 未收。

---

## 总评

- **覆盖声明**：6/6 页逐页目检（pngmono 150dpi）+ 300dpi 仲裁 6 件（含 4x/6x/8x 放大 5 件）。
  扫描件文本层噪声大，未作对账依据。mineru：standard 档云端解析（OCR）。
- **数学内容可信度**：Theorems 1-3、(1)-(8)、Lemmas 1-5 及证明的公式链逐式核对；**κ 指数被
  mineru 系统性识成乘积或 `*` 共 8 处**（(3)/(6)/双和界×2/|φ(w)| 花括号/星号/e^{−hκ}×2——
  全部按 300dpi 修复为 h^{κ} 幂形），是本篇最主要伪影家族（已录入 HANDOFF §4 坑清单）。
- **原刊排印 quirk（md 忠实，不代改）**：①"pseudo efective"（Baker II 无此词——该项属 citation
  篇，此处略）；本篇未发现源级笔误；脚注 †（Ax/Leopoldt）完整保留。
- **可用性结论**：修复后 md 可作该文忠实底本；阅读时应知：页眉/页码未收、脚注位置漂移、
  7 个孤立碎片 span（p.1）。本篇与 (I) 俄译件（AUDIT-Baker_linear_forms_ru.md）配套阅读。

### 修复登记（2026-09-29）
- 全篇 κ 指数误识 8 处修复完成（p.3-p.6）；补 Received on the 21st of March, 1967. 收稿行。
  fix commits 见 `git log --grep 'fix(md): Baker linear forms II'`；修复前 md = 各 fix 父提交。
- 本篇 6/6 页审计完成，无未决项。
