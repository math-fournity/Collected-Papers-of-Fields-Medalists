# AUDIT — Atle Selberg, "An Elementary Proof of the Prime-Number Theorem"（Annals of Math. 50 (1949) 305–313；JSTOR 版 10 页 = 封面 + 印刷 pp.305–313）

> mineru: standard 档云端解析（parse_mode=ocr），导出 `Selberg_1949_elementary_pnt_mineru/`；
> 审计依据 = 二值化渲染 `audit/pNNN.png`（pngmono 150dpi）对照
> `Selberg_1949_elementary_pnt__Selberg_1949_elementary_pnt.md`。逐页审计，一页一签。
> 仲裁裁剪：`audit/p002_eq14_*_300dpi.png`（pnggray 300dpi）。
> PDF 结构：p.1 = JSTOR 封面（Stable URL 1969455），p.2–10 = 印刷 pp.305–313。

## p.001（PDF p.1 / JSTOR 封面页）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：
  - 题录：An Elementary Proof of the Prime-Number Theorem / Author(s): Atle Selberg /
    Source: Annals of Mathematics, Second Series, Vol. 50, No. 2 (Apr., 1949), pp. 305-313 /
    Published by: Annals of Mathematics / Stable URL: http://www.jstor.org/stable/1969455 /
    Accessed: 04/02/2014 11:21 ✓ 逐字吻合
  - Terms & Conditions 段、JSTOR not-for-profit 段 ✓ 逐字吻合
- 结果：**PASS±**
  - ±（JSTOR chrome 未转写，均与论文内容无关）：① 页顶 "Annals of Mathematics" 页眉；
    ② 页底 "Annals of Mathematics is collaborating with JSTOR to digitize, preserve and extend
    access to Annals of Mathematics."；③ "http://www.jstor.org"；④ 下载行 "This content
    downloaded from 130.39.169.231 on Tue, 4 Feb 2014 11:21:29 AM / All use subject to JSTOR
    Terms and Conditions"。
- 备注：封面页为 JSTOR 数字库模板，非论文内容。

## p.002（PDF p.2 / 印刷 p.305）
- PNG：audit/p002.png；仲裁：audit/p002_eq14_denom_zoom6x / _frac_zoom3x / _pxs_zoom8x_300dpi.png
- 核对：
  - 页眉 `ANNALS OF MATHEMATICS / Vol. 50, No. 2, April, 1949`、页码 305 未转写（系统性）
  - 题名 / ATLE SELBERG / (Received October 14, 1948) ✓
  - §1. Introduction 两段 ✓；"We shall prove the prime-number theorem in the form" ✓
  - (1.1) lim_{x→∞} ϑ(x)/x = 1 ✓；(1.2) ϑ(x) = Σ_{p≤x} log p ✓；
    (1.3) ϑ(x) log x + Σ_{p≤x} log p ϑ(x/p) = 2x log x + O(x) ✓ 逐符号吻合
  - Erdős 结果段（δ、K(δ)、x₀ = x₀(δ)、K(δ)x/log x、x 到 x+δx）✓；
    上下极限记法 lim/lim‾ = a/A ✓
  - 脚注 ¹（避免上下极限概念；"of course (1.1) would then have to be stated differently."）✓ 逐字
  - **(1.4) ⚠️ 源级笔误（非 md 缺陷）**：原件印刷即作 Σ_{p≤x} (log p)/**x** = log x + O(1)——
    **300dpi 6×/8× 放大确认分母字形为 x（无降部），与分子 p（有降部）不同形**；md 照录 x，忠实。
    数学上应为分母 p（Mertens 型；本页 (1.5) a+A=2 的推导依赖 Σ log p/p）。此系 1949 原刊
    已知笔误（外部核对：MathOverflow Q491837, 2025-04 专帖；Zbl 0036.30604 评论亦记 p^{-1}log p 形式）。
    **引用 (1.4) 时须用修正形式 Σ_{p≤x}(log p)/p。**
- 结果：**PASS±**（±：页眉/页码丢弃；唯一注意点 = 源级笔误 (1.4)，md 转写忠实）
- 备注：本页为正文首页；正文其余公式零错误。

## p.003（PDF p.3 / 印刷 p.306）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：
  - 页眉 `306 / ATLE SELBERG`、JSTOR 下载页脚未转写（系统性）
  - (1.5) a + A = 2 ✓；"Next, taking a large x, with" ✓；ϑ(x) = ax + o(x) ✓
  - (1.6) (ϑ(x) − ax) log x + Σ_{p≤x} log p (ϑ(x/p) − A x/p) = O(x) ✓ 逐符号
  - (1.7) ϑ(x/p) > (A − δ) x/p ✓；例外集 Σ (log p)/p = o(log x) ✓（两处，分母均 p）
  - √x < x′ < x；ϑ(x′) = Ax′ + o(x′) ✓；行末 "wit"（原文断行截断、md 同——非缺陷）
  - (1.8) ϑ(x′/p) < (a + δ) x′/p ✓；Erdős 段（原拼法 "chose"）✓
  - x/p < x′/p′ < (1+δ) x/p ✓；四重不等式链 ✓；A − δ < (a + δ)(1 + δ) ✓；A ≤ a ✓
- 结果：**PASS±**（±：页眉/页码/JSTOR 页脚丢弃）
- 备注：本页无内容级差异。

## p.004（PDF p.4 / 印刷 p.307）
- PNG：audit/p004.png；仲裁：audit/p004_eq22_300dpi / p004_eq22_sub_zoom8x_300dpi.png
- 核对：
  - 页眉 `THE PRIME-NUMBER THEOREM / 307`、JSTOR 页脚未转写（系统性）
  - "Hence since also A ≥ a and a + A = 2 we have a = A = 1…" ✓；Erdős 段 ✓；
    Beurling/算术级数段（脚注 ²/³）✓
  - (1.9) ϑ(x) = O(x). ✓；"Of known results…" ✓
  - 记号段（p,q,r 素数；μ(n) Möbius 函数；τ(n) 除数个数；c/K 为常数）✓
  - **2. Proof of the basic formulas** ✓；(2.1) λ_d = λ_{d,x} = μ(d) log²(x/d) ✓
  - (2.2) θ_n = θ_{n,x} = Σ_{d/n} λ_d ✓——下标经 7× 放大确认为**斜线 "d/n"**（语义即 d|n 求和；
    原件写法如此，md 忠实）
  - (2.3) 分段四行逐符号 ✓（log²x ／ log p log x²/p ／ 2 log p log q ／ 0）
  - 归纳说明段 ✓；θ_{n,x} = θ_{n/p_k,x} − θ_{n/p_k,x/p_k} ✓；"From this the remaining part of (2.3) follows." ✓
  - 脚注 ² Beurling（Acta Math. 68, 255–291, 1937）、³（These Annals this issue, pp. 297–304）✓
- 结果：**PASS±**（±：页眉/页码/页脚丢弃；下标 "d/n" 为原件写法）
- 备注：本页无内容级差异。

## p.005（PDF p.5 / 印刷 p.308）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：
  - 页眉 `308 / ATLE SELBERG`、JSTOR 页脚未转写（系统性）
  - "Now consider the expression" ✓；**(2.4)** 完整链：Σ_{n≤x}θ_n = ΣΣ_{d/n}λ_d = Σ_{d≤x}λ_d[x/d] =
    xΣ λ_d/d + O(Σ|λ_d|) = xΣ μ(d)/d log²(x/d) + O(Σ log²(x/d)) = … + O(x) ✓（含 floor 括号 [x/d]）
  - "This on the other hand … by (2.3)" ✓；**(2.5)** 六行链：log²x + Σ_{p^α≤x} log p log x²/p +
    2Σ_{p^αq^β≤x, p<q} log p log q = Σ_{p≤x}log²p + Σ_{pq≤x}log p log q + O(Σ log p log(x/p))
    + O(Σ_{α>1} log²x) + O(Σ_{α>1} log p log q) + log²x ✓
  - "remainder term … (1.4) and (1.9)" ✓；**(2.6)** Σ_{p≤x}log²p + Σ_{pq≤x}log p log q =
    xΣ_{d≤x} μ(d)/d log²(x/d) + O(x) ✓
  - **(2.7)** Σ_{ν≤z} 1/ν = log z + c₁ + O(z^{−¼}) ✓；**(2.7′)** Σ τ(ν)/ν = ½log²z + c₂log z + c₃
    + O(z^{−¼}) ✓；Σ_{ν≤z} τ(ν) = z log z + c₄z + O(√z) ✓；
    log²z = 2Σ τ(ν)/ν + c₅Σ 1/ν + c₆ + O(z^{−¼}) ✓ —— 逐符号吻合
- 结果：**PASS±**（±：页眉/页码/页脚；下标 "d/n" 同 p.307）
- 备注：本页公式密集但零内容级差异。

## p.006（PDF p.6 / 印刷 p.309）
- PNG：audit/p006.png；仲裁：audit/p006_oterm / p006_dexp_zoom8x_300dpi.png
- 核对：
  - 页眉 `THE PRIME-NUMBER THEOREM / 309`、JSTOR 页脚未转写（系统性）
  - "By taking here z = x/d, we get" ✓；长链 2ΣΣ + c₅ΣΣ + c₆Σ + O(…) = 2Σ_{dν}μτ/dν + c₅Σ μ/dν
    + c₆Σ μ/d + O(1) = 2Σ 1/n Σ_{d/n} μτ + c₅Σ 1/n Σμ + O(1) = 2Σ1/n + c₅ + O(1) = 2 log x + O(1) ✓
  - "We used here that Σ_{d/n} μ(d)τ(n/d) = 1 …" ✓；"Now (2.6) yields" ✓
  - **(2.8)** Σlog²p + Σlog p log q = 2x log x + O(x) ✓
  - **(2.9)** ϑ(x)log x + Σ log p ϑ(x/p) = 2x log x + O(x) ✓；Σ log²p = ϑ(x)log x + O(x) ✓
  - **(2.10)** Σlog p + Σ (log p log q)/log pq = 2x + O(x/log x) ✓
  - "This gives" 链 ✓；**(2.11)** ϑ(x)log x = Σ (log p log q)/log pq · ϑ(x/pq) + O(x log log x) ✓
- 结果：**FAIL（单点，指数级）**
  - ✗ md 第 227 行：`O (x ^ {- \frac {1}{4}} \sum_ {d \leq x} d ^ {- \frac {4}{3}})`——**原图为 d^{−3/4}**
    （300dpi 8× 放大：分子 3、分母 4；且由 z=x/d 代入 (2.7′) 的 O(z^{−1/4}) 再乘 1/d 亦应得 d^{−3/4}）。
    md 将指数分数**转置**为 −4/3，属内容级错误。**以原图为准**；
    修复建议：`d ^ {- \frac {4}{3}}` → `d ^ {- \frac {3}{4}}`。
  - ±：页眉/页码/页脚丢弃；下标 d/n 同前。
- 备注：除该单点外，本页其余公式与 (2.8)–(2.11) 全部逐符号吻合。

## p.007（PDF p.7 / 印刷 p.310）
- PNG：audit/p007.png；仲裁：audit/p007_since_300dpi.png
- 核对：
  - 页眉 `310 / ATLE SELBERG`、JSTOR 页脚未转写（系统性）
  - "Writing now / ϑ(x) = x + R(x) , (2.9) easily gives" ✓
  - **(2.12)** R(x) log x = −Σ_{p≤x} log p R(x/p) + O(x) ✓
  - **(2.13)** R(x) log x = Σ_{pq≤x} (log p log q)/(log pq) R(x/pq) + O(x log log x) ✓
  - "since" 式：Σ_{**pq≤x**} (log p log q)/(pq log pq) = log x + O(log log x)——**300dpi 确认下标为 pq≤x**
    （双字母 pq 清晰；与紧随其后的 Σ_{pq≤x} (log p log q)/pq 定义域一致）→ 见 FAIL
  - Σ_{pq≤x} (log p log q)/pq = ½log²x + O(log x) ✓；"which again follows easily from (1.4)." ✓
  - "The (2.12) and (2.13) yield" ✓；2|R|log x ≤ Σ_{p≤x} log p|R(x/p)| + Σ_{pq≤x}(…) + O(x log log x) ✓
  - "From this, by partial summation," 与 "or by (2.10)" 两条长链 ✓ 逐项吻合（含 Σ n/(1+log n)、
    Σ 1/(n(1+log n))、Σ 1/(1+log n)ϑ(x/n)）
- 结果：**FAIL（单点，求和域错误）**
  - ✗ md 第 291 行：`\sum_ {p \geq x}`——**原图为 Σ_{pq≤x}**。**以原图为准**；
    修复建议：`\sum_ {p \geq x}` → `\sum_ {pq \leq x}`。
  - ±：页眉/页码/页脚丢弃。
- 备注：除该单点外，本页 (2.12)–(2.13) 与两条部分求和长链逐符号吻合。

## p.008（PDF p.8 / 印刷 p.311）
- PNG：audit/p008.png（pngmono 150dpi）
- 核对：
  - 页眉 `THE PRIME-NUMBER THEOREM / 311`、JSTOR 页脚未转写（系统性）
  - **(2.14)** |R(x)| ≤ (1/log x)Σ_{n≤x}|R(x/n)| + O(x log log x / log x) ✓；"which is the result we will use…⁴" ✓
  - **3. Some properties of R(x)** ✓；"From (1.4) we get by partial summation that" ✓；
    Σ_{n≤x} ϑ(n)/n² = log x + O(1) ✓；Σ_{n≤x} R(n)/n² = O(1) ✓
  - "This means there exists an absolute positive constant K₁…（x > 4, x′ > x）" ✓；
    **(3.1)** |Σ_{x≤n≤x′} R(n)/n²| < K₁ ✓
  - "Accordingly we have…（x ≤ y ≤ x′）" ✓；**(3.2)** |R(y)/y| < K₂/log(x′/x)、K₂ ≥ 1 ✓
  - "…changes the sign also.⁵" ✓；**(3.3)** |R(y)| < δy（δ < 1, x ≤ y ≤ e^{K₂/δ}x）✓
  - "From (2.10) we see that for y < y′" ✓；0 ≤ Σ_{y<p≤y′} log p ≤ 2(y′−y) + O(y′/log y′) ✓；
    |R(y′)−R(y)| ≤ y′−y + O(y′/log y′) ✓
  - 脚注 ⁴（2.14 余项说明 + 替代不等式 |R(x)| ≤ (2/log²x)Σ (log n/n)|R(x/n)| + O(x/log x)）✓；
    脚注 ⁵（Because there will then be a |R(y)| < log y.）✓
- 结果：**PASS±**（±：页眉/页码/页脚丢弃；脚注 ⁴ 在 md 中被拆为三个片段 span——内容完整）
- 备注：本页无内容级差异。

## p.009（PDF p.9 / 印刷 p.312）
- PNG：audit/p009.png（pngmono 150dpi）
- 核对：
  - 页眉 `312 / ATLE SELBERG`、JSTOR 页脚未转写（系统性）
  - "Hence, if y/2 ≤ y′ ≤ 2y, y > 4," ✓；|R(y′)−R(y)| ≤ |y′−y| + O(y′/log y′) ✓
  - "or" ✓；|R(y′)| ≤ |R(y)| + |y′−y) + O(y′/log y′) ✓——**原件此式自带笔误**（y′−y 前多一竖线、
    括号不配对），md **忠实保留**（勿"纠正"）
  - "Now consider an interval (x, e^{K₂/δ}x)…" ✓；|R(y)| < δy ✓；"Thus for any y′…" ✓
  - |R(y′)| ≤ δy + |y′−y| + K₃y′/log x ✓；|R(y′)/y′| < 2δ + |1−y′/y| + K₃/log x ✓
  - "Hence if x > e^{K₃/δ} and e^{−δ/2} ≤ y′/y ≤ e^{δ/2}…" ✓；< 2δ + (e^{δ/2}−1) + δ < 4δ ✓
  - "Thus for x > e^{K₂/δ} …sub-interval (y₁, e^{δ/2}y₁)…|R(z)| < 4δz" ✓
  - **4. Proof of the prime-number theorem** ✓；THEOREM：lim ϑ(x)/x = 1 ✓；(4.1) lim R(x)/x = 0 ✓
  - "We know that for x > 1," ✓；(4.2) |R(x)| < K₄x ✓；"Now assume…α < 8," ✓；(4.3) |R(x)| < αx ✓；
    "holds for all x > x₀. Taking δ = α/8…" ✓
- 结果：**PASS±**（±：页眉/页码/页脚丢弃）
- 备注：本页无内容级差异；"|y′−y)" 系原件笔误的忠实转写。

## p.010（PDF p.10 / 印刷 p.313，**末页**）
- PNG：audit/p010.png；仲裁：audit/p010_substack_300dpi.png
- 核对：
  - 页眉 `THE PRIME-NUMBER THEOREM / 313`、JSTOR 页脚未转写（系统性）
  - "section (since we may assume that x₀ > e^{K₃/δ})…" ✓；(4.4) |R(z)| < αz/2（y ≤ z ≤ e^{δ/2}y）✓
  - "The inequality (2.14) then gives, using (4.2)," ✓；两条不等式链（Σ_{(x/x₀)<n≤x} 1/n 与
    Σ_{n≤(x/x₀)} (1/n)|(n/x)R(x/n)|）✓
  - "writing now ρ = e^{K₂/δ}…" ✓；主链：αx − (αx/(2log x))Σ_{1≤ν≤…}δ/2 + O(x/√log x) =
    αx − (αδ/(4log ρ))x + O(x/√log x) = α(1 − α²/(256K₂))x + O(x/√log x) < α(1 − α²/(300K₂))x ✓
  - **substack 求和域**：原图为 Σ_{y_ν ≤ n ≤ y_ν e^{δ/2}；ρ^{ν−1}<y_ν≤ρ^ν e^{−δ/2}}（**两处均 y_ν**）
    ——md 首处作 `y _ {n}` → 见 FAIL
  - "for x > x₁. Since the iteration-process" ✓；α_{n+1} = α_n(1 − α_n²/(300K₂)) ✓；
    "obviously converges … α₁ = 4（α_n < K₅/√n）" ✓
  - FINAL REMARK 全段 ✓（o(x log x) 代 O(x)、o(log x)、ϑ(x) > Kx、§3 需调整）
  - 署名 "THE INSTITUTE FOR ADVANCED STUDY / AND / SYRACUSE UNIVERSITY" ✓
- 结果：**FAIL（单点，下标误识）**
  - ✗ md 第 469 行：substack 首条件 `y _ {n} \leq n`——**原图为 y_ν**（300dpi 确认；且 md 同式后两处
    均作 `y _ {\nu}`，内部不一致）。**以原图为准**；修复建议：`y _ {n}` → `y _ {\nu}`。
- 备注：除该单点外，本页（含 FINAL REMARK 与署名）逐字吻合。

## 总评
- **覆盖声明**：10 页全部逐页审计（audit/p001–p010.png，pngmono 150dpi；p.2/4/6/7/10 附 300dpi 仲裁裁剪）。
- 结论分布：**PASS± ×7 + FAIL ×3（均为单点、内容级）**：
  ① p.309 `d^{-4/3}` 应为 `d^{-3/4}`（指数分数转置，8× 放大 + 推导双重确认）；
  ② p.310 `\sum_{p \geq x}` 应为 `\sum_{pq \leq x}`（求和域错误，300dpi 确认）；
  ③ p.313 `y_{n}` 应为 `y_{\nu}`（下标误识，300dpi 确认且 md 内部不一致）。
  **使用建议：以上三处修复前，涉及 (2.4) 余项界、§3 部分求和式与 §4 迭代论证的引用须以原 PDF 为准。**
- 源级问题（**非 md 缺陷**）：① (1.4) 分母 "x" 系 1949 原刊印刷笔误（应为 p；外部核对
  MathOverflow Q491837 / Zbl 0036.30604）；② p.312 "|y′−y)"（多余竖线、括号不配对）系原件笔误，
  md 忠实；③ 整除记号原件即作 "d/n"（非 d|n）。
- 系统性瑕疵：页眉/页码/JSTOR 页脚全部丢弃；脚注以 page_footnote span 保留（⁴ 被拆三段）。
- 可用性：文本、文献与绝大多数公式可引用；**3 处 FAIL 单点须按上表修复或以原图为准**。
- mineru 解析信息：mineru 3.4.4 / tier=basic / parse_mode=ocr。

> **修复登记（2026-09-29）**：已按本审计修复 3 处单点 FAIL（d^(-4/3)→d^(-3/4)、Σ_{p≥x}→Σ_{pq≤x}、y_n→y_ν）；修复与本登记同一 commit；修复前 md 见该 commit 父提交。
