# AUDIT — A. Baker《Linear forms in the logarithms of algebraic numbers (I)》（Mathematika 13 (1966), 204–216；Cambridge Core 扫描件，BFO 重打包）

> mineru: standard 档云端解析（OCR，文本层不可靠——同 (II)(III)）；审计依据 = `audit/baker1_pNNN.png`
> （pngmono 150dpi 全 13 页目检）+ 300dpi 仲裁（`baker1_p005_300dpi.png` + eq7/eq8）。
> **交叉参照**：本篇为 (II) 俄译件（`AUDIT-Baker_linear_forms_ru.md`）之原文，数学内容互为对照。

## p.001（印刷 p.204）
- 核对：题录 ✓；§1 引言（Gelfond [2]/Schneider [6]/七问题、Gelfond [3] β₁logα₁+β₂logα₂ 下界、
  Thue-Siegel-Roth、[4; p.177] 预言）✓；height 定义、†‡ 脚注（z^w=e^{w log z}、2πi 排除更强）、
  § 脚注（κ>2 suffices n=2）✓；**(1) κ>n+1** ✓；**Theorem** C=C(n,α₁,…,αₙ,κ,d)>0 ✓
- 结果：**FAIL（单点）**：脚注 † "z^w means e^w log z"——原刊 "e^{w log z}"（上标丢失）。
## p.002（印刷 p.205）
- 核对：**(2)** e^{−(log H)^κ} ✓；**Corollary 1/2** ✓；Diophantine f(x,y)=1/[4; p.176]、
  Gelfond-Linnik [5]/九个类数 1 虚二次域/Stark 脚注 † ✓；Davenport 致谢 ✓；§2 开头 ✓
- 结果：**PASS±**（±：页眉/页码未收）
## p.003（印刷 p.206）
- 核对：修改版定理（⩾ e^{−(log H)^κ}）✓；|α|⩽dH/(a₀α)^j/递推式/αβ 次数 d² 高度 H′/
  (ab)^{d²}∏(x−α^{(i)}β^{(j)}) ✓；β′ᵣ=−βᵣ/βₙ ✓；脚注 †‡ ✓
- 结果：**PASS±**
## p.004（印刷 p.207）
- 核对：κ′=½(κ+n+1)、κ>κ′>n+1 ✓；修改版结论 |β′₁logα₁+…−logαₙ| > e^{−(log H″)^{κ′}}——
  **md 乘积 (log H″)κ′ → FAIL**；|βₙ|⩾(dH)^{−1}、(dH)^{−1}e^{−(log H″)^{κ′}}（**md 乘积 → FAIL**）、
  Ce^{−(\log H)^{κ}}（**md 乘积 → FAIL**）✓；§3 记号 ✓；**(3)**/**|e^z−1|⩽|z|e^{|z|}**/**(4)**/
  **(5)** ζ=½{1+κ/(n+1)}、ε=(1−1/ζ)/(2n) ✓；h/k/D/f_m 定义 ✓
- 结果：**FAIL（三点）**：κ′/κ 指数乘积化 ×3。
## p.005（印刷 p.208）
- PNG+仲裁：baker1_p005_300dpi.png + eq7（2x）/eq8
- 核对：**Lemma 1**（B=[(NU)^{M/(N−M)}]、(B+1)^N/(NUB+1)^M）✓；**Lemma 2**：Φ 定义 ✓；
  **(7) |Φ_m(l,…,l)|<e^{−½h^κ}**——2x 证实 κ 上标，**md 乘积 → FAIL**；**(8)** Σp(λ)α₁^{λ₁l}…αₙ^{λₙl}
  γ₁^{m₁}…=0（300dpi 证实 α^{λl} 形）✓；(9) ✓
- 结果：**FAIL（单点）**：(7) 补 ^。
## p.006（印刷 p.209）
- 核对：(9) 代入/γ_r^{m_r}/A(s,t) 方程/v(λ)/w(λ,μ) ✓；|v|⩽c₂^{Lh}、|w|⩽(4HL)^k、
  U=c₂^{Lh}(8HL)^k ✓；M⩽D(k+1)^{n−1}h、N=(L+1)^n、N>k^{n−nε}>2M ✓
- 结果：**PASS±**
## p.007（印刷 p.210）
- 核对：NU⩽kⁿc₂^{Lh}(8ke^{(3/2)h})^k⩽e^{2hk} ✓；(8)⇒(7)（P 因子、代换 αₙ、脚注 †
  |x^λ−y^λ| 界、c₃^{Ll}e^{−(log H)^κ}⩽c₃^{Lh}**e^{−h^κ}**——**md 乘积 → FAIL**）✓；
  |γ_r|⩽2dLH、c₄^{k+Ll}(2dLH)^k<e^{2hk}、(L+1)^ne^{4hk}c₃^{Lh}**e^{−h^κ}**（**md 乘积 → FAIL**）✓；
  **Lemma 3** (10)(11) ✓；P/q(λ,z) ✓；footnote † ✓
- 结果：**FAIL（两点）**：e^{−hκ}×2 补 ^。
## p.008（印刷 p.211）
- 核对：|Pq(λ,z)|⩽c₅^{L|z|}(2c₈dLH)^k、(L+1)^ne^{2hk}c₅^{L|z|}(2c₈dLH)^k⩽e^{4hk}c₅^{L|z|} ✓；
  Q/P′/q′、共轭界 (L+1)^ne^{2hk}c₉^{Ll}(2dLH)^{2k}⩽e^{6hk}c₉^{Ll}、|Norm Q|⩾1、
  |Q|⩾(e^{6hk}c₉^{Ll})^{−D+1} ✓；|q(λ,l)−q′(λ,l)|⩽c₁₀^{Ll}(2dLH)^k**e^{−h^κ}**（**md 乘积 → FAIL**）、
  e^{−½h^κ}（✓）、(L+1)^ne^{2hk−¾h^κ}<e^{−⅝h^κ}（**md 乘积 ×2 → FAIL**）✓；
  |P/P′|>c₁₁^{−Ll−k}H^{−k}、|P|<c₁₂^k ✓；**Lemma 4** (12) τ ✓
- 结果：**FAIL（四点）**：e^{−hκ}+e^{−¾hκ}+e^{−⅝hκ} 补 ^（另一 e^{−½h^κ} md 本正确）。
## p.009（印刷 p.212）
- 核对：R_J/S_J ✓；(13)(14) ✓；f_m(r) 定义 + "evaluated at the point z₁=…=z_{n−1}=r" ✓
  （(II) 中丢失误此处的求值说明，本篇 md 完整）；(15) Cauchy/留数/Γ_r ✓
- 结果：**PASS±**
## p.010（印刷 p.213）
- 核对：双和界 R_K(S_{K+1}+1)8^{S_{K+1}+1}n^k e^{−½**h^κ**}⩽h^κ(8n)^k e^{−½**h^κ**}<e^{−¼**h^κ**}
  ——print κ 上标 ×2 + ¼；**md 三处全误**（乘积 ×2 + ½）→ **FAIL**；(16)(17)(18) ✓；
  **|F(l)|⩽e^{¼h^κ}、|f(l)|>2e^{−¼h^κ}**——print ¼；**md 1/5 → FAIL ×2**；
  **|f(l)/F(l)|>2e^{−¼h^κ}**——print ¼；**md ½ 乘积 → FAIL**；θ=upper|f|/Θ=lower|F| 定义 ✓；
  4θ|F(l)|>Θ|f(l)| ✓；(19) ✓；θ⩽e^{4hk}**c₅^{LR_K+1 log h}**——print R_{K+1}；**md R_R+1 → FAIL**；
  Θ|F(l)|^{−1}、θ|f(l)|^{−1}⩽(e^{6hk}c₅^{LR_{K+1} log h})^{D+1} ✓；脚注 †（…⩽k^{½ε(K+1−τ)}**h^κ**}
  ——print κ；**md h^K → FAIL**）
- 结果：**FAIL（八点）**：1/5→¼×2、½hκ→¼h^κ、乘积×2、R_R→R_{K+1}、h^K→h^κ。
## p.011（印刷 p.214）
- 核对：**(20)** ✓；c₁₄ 两形/K=0 或 K>0 ✓；R_K(S_{K+1}+1)⩾½hk^{½εK}(k/2^{K+1})、
  c₁₅^{−1}h^{½εζK+1+ζ}log log h ✓；§4 **(21)** e^{−½h^κ} ✓；½h^{κ−ζ} ✓；Ψ(l) 定义 ✓；
  c₁₆^L、c₁₇^{Ll}**e^{−h^κ}**（**md 乘积 → FAIL**）、|Φ−**Ψ(l)**|（**md Ψ^* → FAIL**）✓；
  "at most **e^{−h^κ}**"（**md e^{−1hκ} → FAIL**）；Ll⩽…<2^nh^{κ(1−ε)} ✓；**(22)** |**Ψ(l)**|<2e^{−½h^κ}
  （**md Ψ^* → FAIL**）✓
- 结果：**FAIL（四点）**：e^{−hκ}、e^{−1hκ}、Ψ^*×2。
## p.012（印刷 p.215）
- 核对：ω=(a₁⋯aₙ)^{Ll}**Ψ(l)**（**md Ψ′ → FAIL**）；共轭界 (L+1)^ne^{2hk}c₁₈^{Ll}<c₁₉^{h^{κ(1−ε)}} ✓
  （md hκ(1−ε) 乘积 → **FAIL**）；|Norm ω|<1、ω/Ψ(l)=0† ✓；Vandermonde ✓；§5 Corollary 2
  证明开头（α_{m+1}=1 不可能/γ_j/β_{m+1}=−1）✓；脚注 †‡ ✓
- 结果：**FAIL（两点）**：Ψ′→Ψ；hκ(1−ε)→h^{κ(1−ε)}。
## p.013（印刷 p.216）
- 核对：β₁,…,β_{m+1} 线性无关/Corollary 1/ρ_{m+1}≠0/δ_j/ε_j 归纳矛盾 ✓；"footnote on page 204" ✓；
  **References [1]-[8] 逐条**（Feldman/Gelfond×3/Gelfond-Linnik/Schneider×2/Siegel——卷页全对，
  与俄译件文献表一致）✓；Trinity College, Cambridge ✓
- 结果：**FAIL（单点）**：**(Received on the 17th of October, 1966.)** 收稿行丢失（同 (II)）。

## 总评

- **覆盖声明**：13/13 页逐页目检（150dpi 全页）+ 300dpi 仲裁（p.5 (7)(8) 两帧）。文本层不可靠
  （BFO），以 PNG 为准；与 (II) 俄译件交叉参照（俄译审计已核的数学内容在此全部得到英文原文印证）。
- **FAIL 清单（20 点，两大家族）**：①**κ/κ′ 指数乘积化或漏幂 ×17**（p.4×3、p.5×1、p.7×2、
  p.8×4、p.10×3、p.11×2、p.12×1、含 ℏκ×1、e^{−1hκ}×1、h^K×1）；②杂码/缺失（Ψ^*×2、Ψ′×1、
  R_R+1、Received 行、脚注 † 上标）。
- **源级/排印 quirk（忠实不改）**：θ=upper|f| 与 Θ=lower|F| 的定义方向（与俄译件相反——俄译
  藏了 swap，英文原刊如此）；"4θ|F(l)|" 原刊即基线 4θ（俄译排版为上标 4^θ——译文排印 quirk）。
- **可用性结论**：修复后 md 为 (I) 原文忠实底本；(I)(II)(III)+Harper 四件构成 Baker 主题完整
  审计链。本篇 13/13 页完成，无未决项。
