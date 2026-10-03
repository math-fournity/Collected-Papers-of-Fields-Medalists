# AUDIT-Scholze_2012_perfectoid_published

- actor：Wf-P44
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF：`2018年 - Scholze/Scholze_2012_perfectoid_published.pdf`（69 PDF 页 = 印刷 pp.245–313，Pub. IHÉS 116 (2012)）
- PDF SHA256：`7e7f7a3b6309ead9d8ee376106c92c644f25b22d75ffa6d7382508a36cf7814a`（本次 session 实测复核一致）
- MD 基线 SHA256：`089d58912047de5c0e3439428e48d78b63eda9856562a14fd335a1b5929d7481`（= 原始 mineru 导出 commit d87578ba，本次 session 实测复核一致）
- 日期时间：2026-10-02 13:33 EDT 开工
- 文本层通道判定：**可用**。`pdftotext -f 1 -l 1` 首页抽取干净（标题/摘要/目录/正文完整、公式线性化可读），全程采用「pdftotext 文本层主对账 + pngmono 150dpi PNG 视觉核验」双通道。
- 审计方式：逐页交错（渲染→目检→五点比对→分级→修复→落签→提交），每页一 commit；print quirk 忠实登记不改，MinerU OCR 内容错误按原图证据逐处 Edit 修复。

---
## p.001（PDF p.1 / 印刷 p.245）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：题录（标题 PERFECTOID SPACES / by PETER SCHOLZE、ABSTRACT、CONTENTS 11 条页码 245/252/263/267/272/283/295/303/307/311/312、页脚 DOI 10.1007/s10240-012-0042-x）；§1 Introduction 节标题；Theorem 1.1 陈述（Q_p(p^{1/p^∞}) 与 F_p((t)) 绝对 Galois 群典范同构）；首段与次段公式与上下标
- 结果：**FAIL**（MinerU OCR 数学内容错误，已当页修复，以原图为准）：
  1. 首段 `Q_b`→印刷为 $\mathbf{Q}_p$；`F_{φ}`→$\mathbf{F}_p$；"characteristic$\cdot\cdot\cdot\cdot\cdot$"→"characteristic $p$."；"characteristic$\beta .$."→"characteristic $p$."（p.245 左栏/正文首段）
  2. 首段 "some ofthe"、"is ofcharacteristic"、"ofthis"、"ofFaltings's" 缺空格 → 修正；"weightmonodromy" → "weight-monodromy"（印刷跨行连字符 "weight-/monodromy"）
  3. Theorem 1.1：`$\mathbf{\tilde{Q}}_{\theta}(\theta^{1/p^\infty})$`→$\mathbf{Q}_p(p^{1/p^\infty})$；`$\mathbf{F}_p({\it\Delta\phi}(t))$`→$\mathbf{F}_p((t))$（p.245 定理行原图）
  4. "roots o$\dot{\boldsymbol{p}}$"→"roots of $p$"；`Q_ν(\dot p^{1/p^∞})`→$\mathbf{Q}_p(p^{1/p^\infty})$；`F_p(\r(t))(t^{1/p^∞})`→$\mathbf{F}_p((t))(t^{1/p^\infty})$（p.245 末段）
- 备注：摘要与 CONTENTS 文字、页码全部吻合；印刷版为数字排版，无 print quirk；所有差异均为 MinerU OCR 对 p/𝑝 字形与双括号的系统性误读（p 在下标/正文被读作 b/θ/ν/φ/β/···）。
## p.002（PDF p.2 / 印刷 p.246）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：页眉 246/PETER SCHOLZE；display K°/p = Z_p[p^{1/p^∞}]/p ≅ F_p[t^{1/p^∞}]/t = K^♭°/t；K^♭ = lim_{←x↦x^♯} K 识别式；L^♯ 构造段三个多项式；Definition 1.2（Frobenius Φ 在 K°/p 上满射）；K^♭ = lim_{←x↦x^♭} K；Theorem 1.3；Claim 1.4（A¹_{K^♭} ‘is equal to’ lim_{←T↦T^p} A¹_K）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. "map K^♭  K, x ↦ x^♯."（缺箭头+游离句点）→ "map $\mathrm{K}^\flat \to \mathrm{K}$, $x \mapsto x^\sharp$"；"sends t to$\beta.$"→"sends t to $p$."；$\mathcal{V}_n$→$y_n$；$x^{1/\beta^n}$→$x^{1/p^n}$；$\mathrm{K}^\circ/\boldsymbol{\rho}$→$\mathrm{K}^\circ/p$（p.246 右栏上部）
  2. K^♭ = lim 识别式的极限转移映射 `$x\mapsto x^{\flat}$` → 印刷为 x ↦ x^♯（本页两个极限显示式的转移映射不同：识别式用 ♯、tilt 式用 ♭，MinerU 把前者误成 ♭）（p.246 左栏 display）
  3. L^♯ 构造段：$a_{d-1}^{1/\hat p^n}$ 多出 \hat → $a_{d-1}^{1/p^n}$；"$\mathbf{\partial}\cdot\mathbf{X}^d$"多出 ∂· 且 \mathbf→\mathrm，与同行 X 记号一致；句末补 "∞." 句点（p.246 右栏）
  4. "ofcharacteristic$\beta,$" → "of characteristic $p$,"（Definition 1.2 后首段）
  5. "## Theorem 1.3." 伪标题层级 → 正文行（同页其余定理均为正文行）
  6. Claim 1.4："$‘is equal$t o ^ { \bullet }$"→‘is equal to’；"lim$\mathbf{\Gamma}_{T↦T^p} A^1_K.$"伪 Γ 头+游离句点 → $\varprojlim_{T↦T^p} A^1_K$；句末补句点
  7. "K^{\flat_-};, resp. K𝔭-," → "K^♭-, resp. K-, valued points"（p.246 末段，连字符为 valued-point 记号非下标）
- 备注：第一 display 与 Definition 1.2 本身吻合；印刷 "Frobenius Φ" 的 Φ 在 pdftotext 文本层缺字，经 PNG 确认后与 MD 一致。
## p.003（PDF p.3 / 印刷 p.247）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/247；L^♭ = lim_{←x↦x^♭} L display；adic spaces 段（X^ad、|X^ad|）；Theorem 1.5 陈述与 display |(A¹_{K^♭})^ad| ≅ lim_{←T↦T^p} |(A¹_K)^ad|；Definition 1.6（Frobenius Φ 满射于 R°/p）；Theorem 1.7 tilting equivalence + R^♭ = lim_{←x↦x^♭} R display；R = K⟨T^{1/p^∞}⟩ 例与 tilt R^♭ = K^♭⟨T^{1/p^∞}⟩；(R, R^+) 对与 tilt (R^♭, R^♭+)
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. "L<sup>-</sup> of K^♭" → "$\mathrm{L}^\flat$ of K^♭"（p.247 首行，印刷为 L^♭）
  2. 正文极限下标 "$\varprojlim_{\mathrm{\tiny F\,T^\flat}}$" → $\varprojlim_{\mathrm{T}\mapsto\mathrm{T}^p}$（p.247 左栏 "Looking at the example" 段）
  3. Theorem 1.5 display：$\mathrm{T}\mapsto\mathrm{T}^{\flat}$ → $\mathrm{T}\mapsto\mathrm{T}^{p}$（p.247 display 原图为 T↦T^p）
  4. Definition 1.6："perfectoidfield"、"set ofpowerbounded" 缺空格；"Frobenius \x04 is"（MinerU 丢 Φ 留下 0x04 控制字节）→ "Frobenius$\Phi$is"（p.247 定义行，PNG 确认印刷有 Φ）
  5. Theorem 1.7："ofperfectoid"×2；"K<sup>-</sup>-algebras"×2 → $\mathrm{K}^\flat$-algebras（印刷为 K^♭）
  6. display $\mathrm{R}^{b}=\varprojlim_{x\mapsto x^{b}}$ → $\mathrm{R}^{\flat}=\varprojlim_{x\mapsto x^{\flat}}$（b→♭）
  7. "$\mathbb{R}^\flat\to\mathbb{R}$" → $\mathrm{R}^\flat\to\mathrm{R}$（blackboard R 系 OCR 误字族，印刷为同一字母 R）
  8. tilt 公式 $\mathrm{T}^{1/\flat^\infty}$ → $\mathrm{T}^{1/p^\infty}$（p.247 右栏 "Its tilt is given by"）
  9. "oftopological"、"sheafofcharacteristic"、"rigidanalytic" → of topological / sheaf of characteristic / rigid-analytic（印刷连字符跨行）
- 备注：本页遗留观察——全文件还有 6 行含 0x04 控制字节（行 655/973/983/991/1007/1079，均在 §4–5 后续页范围），留待对应页块审计处理，本块不越界修改。
## p.004（PDF p.4 / 印刷 p.248）
- PNG：audit/p004.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/Scholze_2012_p248_mtorsion.png（300dpi，(iii)/(iv) 与 "Here 𝔪 ⊂ K°" 行）
- 核对：页眉 248/PETER SCHOLZE；Huber [19] Spa(R,R^+) 连续赋值 R→Γ∪{0} 段；Theorem 1.8 (i)–(iv) 全部陈述；𝔪 ⊂ K° 段与 Tate acyclicity 推论；Theorem 1.9；tilting functor X↦X^♭ 段；Theorem 1.10；Remark 1.11 开头 R_0、R_n display 与 R = R̂_∞[1/p]
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. 赋值 "$\mathrm{R}\ \ \Gamma∪\{0\}$" 缺箭头 → $\mathrm{R}\to\Gamma\cup\{0\}$（p.248 首段；目标含值群 Γ，print 原样）
  2. **定理号 "Theorem 1.${\bf 3.}$" → Theorem 1.8.**（MinerU 把 8 误成 3，且 "- L e t" 间距伪影 → "— Let"）（p.248 定理行）
  3. (i) 中 $X^{\mathrm{b}}$、$x^{\mathrm{b}}$、$X^{\mathrm{b}}$（\mathrm{b} 字族）→ $X^\flat$、$x^\flat$、$X^\flat$（同句 |f(x^♭)|=|f^♯(x)| 已是 \flat，MinerU 混排）
  4. (ii) "with tilt $\mathrm{U}^{\mathrm{p}}\subset\mathrm{X}^{\mathrm{p}}$" → $\mathrm{U}^{\flat}\subset\mathrm{X}^{\flat}$（p 偷换 ♭，后半句同一定理内 tilt 用 ♭ 正确）
  5. (iv) "m-torsionfor" → "$\mathfrak{m}$-torsion for"；下段 "Here m⊂K°" → "$\mathfrak{m}\subset K°$"——**300dpi 仲裁**（audit/300dpi/Scholze_2012_p248_mtorsion.png）确认印刷为 fraktur 𝔪
  6. "ofperfectoid"×3、"ofFaltings's" 缺空格 → 修正
  7. Theorem 1.10 句末补句点（印刷 "over R°."）
  8. Remark 1.11：$\mathbf{\tilde{R}}_0$、$\mathbf{\check{K}}^\circ$、$\mathbf{\check{T}}_d$ 的伪 tilde/háček → $\mathrm{R}_0$、$\mathrm{K}^\circ$、$\mathrm{T}_d$（p.248 印刷无重音）
  9. Remark 段（p.248 部分）："finite over$\mathrm{R_0}.$," 游离 ".$" → $\mathrm{R}_0$；"the$\mathrm{R}_{n},$," 游离逗号 → $\mathrm{R}_n$；"$[\frac{1}{\mathit{\Pi}_b}]$" → $[\frac{1}{p}]$（print 为 1/p，Π_b 系 OCR 误字）；"invertingp" → "inverting p"
- 备注：本行 119 自 "R_n-algebra which is étale…" 起属印刷 p.249，留待 p.005 审计；(iii) 无差异；Theorem 1.9/1.10 其余文字吻合。
## p.005（PDF p.5 / 印刷 p.249）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/249；Remark 1.11 收尾（[p^{-1}]、S°=Ŝ_∞）；log-smooth/Gabber–Ramero [14]/[31] 段；almost purity 证明梗概段（R^♭-algebras）；Theorem 1.12（tilting 等价 X_ét ≅ X^♭_ét）；Theorem 1.13（(P^n_{K^♭,ad})_ét^~ ≅ lim_φ (P^n_{K,ad})_ét^~）；φ 坐标映射 (x_0^p:…:x_n^p)；π : P^n_{K^♭} → P^n_K display
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Remark 段："$[{ \boldsymbol{\rho}}^{-1}]$" → $[p^{-1}]$（print 为 p^{-1}）；"$m\geq n_{\because}$" 伪 ∵ → $m\geq n$；"$\hat{\mathrm{S}}_\infty^{\bar{}}.$"（空上标+游离句点）→ $\hat{\mathrm{S}}_\infty$；句末补 "∞."；"inverting${p,}$" → "inverting p"
  2. "ofassumptions"、"ofthe" 缺空格 → 修正
  3. "characteristic$\beta.$" → characteristic $p$.；"R<sup>-</sup>-algebras" → $\mathrm{R}^\flat$-algebras（almost purity 梗概段）
  4. "space$\mathrm{X},$, and" 游离双逗号 → 单逗号（Theorem 1.12 前导段）
  5. Theorem 1.12："over K<sup>-</sup>" → over $\mathrm{K}^\flat$；"ofsites" → "of sites"；句末补句点（print "X_ét ≅ X^♭_ét."）
  6. Theorem 1.13：$\mathrm{K}^{\mathrm{p}}$ → $\mathrm{K}^{\flat}$（第一 topos 下标）；$(P^n_{K,ad})_{\tilde{\mathrm{et}}}^{\sim}$ 的伪 \tilde 下标 → $(P^n_{K,ad})_{\mathrm{et}}^{\sim}$（print tilde 在上标位）；句末补句点
  7. φ 坐标公式 $(x_0^\flat:\ldots:x_n^\flat)$ → $(x_0^p:\ldots:x_n^p)$（print 上标为 p，PNG p.249 右栏确认）；公式后补句点
- 备注：π display（p.005 末）与 print 一致；本页 print 无 quirk；行 139 起（"defined on topological spaces…"）属印刷 p.250，留待 p.006。
## p.006（PDF p.6 / 印刷 p.250）
- PNG：audit/p006.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/Scholze_2012_p250_Qbar.png（Q̄_ℓ-representation + ℓ-adic inertia + Fil/gr 段）、audit/300dpi/Scholze_2012_p250_conj114.png（Conjecture 1.14 全行）
- 核对：页眉 250/PETER SCHOLZE；π 坐标 (x_0^♯:…:x_n^♯) 段；(P^n_{K^♭})^ad 非 perfectoid 而 lim_φ 是段；weight-monodromy 回顾段（G_k=Gal(k̄/k)、Q̄_ℓ-representation、ℓ-adic inertia、Fil^N_i ⊂ V、N(Fil^N_i V) ⊂ Fil^N_{i-2} V(−1)、gr^N_i V ≅ gr^N_{−i} V(−i)）；Conjecture 1.14 (Deligne [9])；Deligne [10]/Terasoma [35]/Ito [27] 段；Rapoport–Zink [30]/de Jong [8]/Ito [26] 段；Harris–Taylor [16]/Taylor–Yoshida [34]/Shin [32]/Caraiani [6]/Boyer [4,5]/Dat [7] 段
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. $(\mathbf{P}_{\mathrm{K}^{\mathrm{p}}}^{n})^{\mathrm{ad}}$ → $(\mathbf{P}_{\mathrm{K}^{\flat}}^{n})^{\mathrm{ad}}$（p.250 第二段首，同句后两个 P^n_{K^♭} 正确，MinerU 混排）
  2. "the${\beta}^{\mathrm{-th}}$power map" → "the $p$-th power map"（φ 为 p-th power map，PNG 确认）；"The orem 1.13" → "Theorem 1.13"
  3. "characteristic$\beta,$let" → "characteristic $p$, let"；"of$k.$." 游离 ".$." → "of$k$. "
  4. "Q<sup>¯</sup> -representation" → $\overline{\mathbf{Q}}_{\ell}$-representation——**300dpi 仲裁**（Scholze_2012_p250_Qbar.png）确认下标为 ℓ
  5. "the \x08-adic inertia subgroup"（MinerU 残留 0x08 退格控制字节、ℓ 丢失）→ "the$\ell$-adic inertia subgroup"（300dpi 确认 ℓ）
  6. "Fil^N_i C V, i∈Z.$characterized" → "$\mathrm{Fil}_i^{\mathrm{N}}\subset\mathrm{V}, i\in\mathbf{Z}$, characterized"（伪 C→⊂，句点→逗号）；"V(\dot{-}1)" → V(−1)（伪点删除）；句末 "i≥0" 补句点
  7. Conjecture 1.14："(Deligne$[9]).-Let" → "(Deligne [9]). — Let"；"V =$H$(X_k̄,…)" → "$\mathrm{V}=\mathrm{H}^{i}(\mathrm{X}_{\bar{k}},\bar{\mathbf{Q}}_{\ell})$"（H 上标 i 丢失；Q̄_ℓ 原本正确，300dpi Scholze_2012_p250_conj114.png 确认）；"andfor"→"and for"；"ofweight"→"of weight"
  8. Deligne 段 "characteristic$\beta,$" → "characteristic $p$,"（同句第二个 characteristic p 原本正确）
  9. "ofvarieties"、"ofDrinfeld's" 缺空格 → 修正
- 备注：π 坐标公式本就为 ♯ 正确；print "non-/degenerate" 跨行连字符，MD 作 "non-degenerate" 保留（软连字符歧义，不擅改）；"Deligne [10], proved" 的逗号为 print 原样，保留。
## p.007（PDF p.7 / 印刷 p.251）
- PNG：audit/p007.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/251；Theorem 1.15 全文；π : P^n_{K^♭} → P^n_K display；H^i(X)→H^i(π^{-1}(X)) 段；X = {x_0+x_1+x_2=0} ⊂ (P²_K)^ad display；|(P²_{K^♭})^ad| ≅ lim_φ |(P²_K)^ad| display；X_n = {x_0^{p^n}+x_1^{p^n}+x_2^{p^n}=0} ⊂ (P²_K)^ad display；Lemma 1.16；Huber 结果段 H^i(X)=H^i(X̃)→H^i(Y)；Kedlaya–Liu [28] 段开头
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Theorem 1.15："localfield ofcharacteristic"、"truefor" → "local field of characteristic"、"true for"
  2. "injective map$\mathrm{H}^i(\mathrm{X})\ \mathrm{H}^i(\pi^{-1}(\mathrm{X}))$" 缺箭头 → $\mathrm{H}^i(\mathrm{X}) \to \mathrm{H}^i(\pi^{-1}(\mathrm{X}))$（p.251 左栏）
  3. Lemma 1.16 头 "Lemma 1.$\mathbf{16.}\mathrm{~\_~}Let"（编号进 math、伪下划线）→ "Lemma 1.16. — Let"；句末补句点
  4. "a map$\mathrm{H}^i(\mathrm{X})=\mathrm{H}^i(\tilde{\mathrm{X}})\ \mathrm{H}^i(\mathrm{Y})$)." 缺箭头+游离右括号 → "$\mathrm{H}^i(\mathrm{X})=\mathrm{H}^i(\tilde{\mathrm{X}}) \to \mathrm{H}^i(\mathrm{Y})$."
  5. Kedlaya–Liu 段 "finite étale R<sup>-</sup>-algebras" → $\mathrm{R}^\flat$-algebras
- 备注：三个 display（X 例、homeomorphism、X_n）与 print 逐字符吻合（含 p^n 上标）；本行 187 自 "application to the weight-monodromy conjecture…" 起属印刷 p.252，留待 p.008。
## p.008（PDF p.8 / 印刷 p.252）
- PNG：audit/p008.png（pngmono 150dpi）
- 核对：页眉 252/PETER SCHOLZE；Kedlaya–Liu 段收尾（"Theorem 1.3 was proved…for fields, proved in [15], Chapter 6"——print 自身为 1.3，MD 一致，不改）；§2. Adic spaces 节标题；§2 首段 [22][20][19]；Definition 2.1；norm |·|:k→R_≥0 与 automorphisms x↦x^α 段；functor {varieties/k}→{adic spaces/k} display 与 {|f(x)|≤1} display；Γ(X,O_X)→k′ 赋值段至 "inducing"
- 结果：**PASS±**（排版级伪影，已修 4 处，无数学内容错误）：
  1. Definition 2.1："nonarchimedeanfield"、"topologicalfield"、"ofrank" 缺空格 → 修正
  2. "0<α<∞.$, of R_≥0" 游离 ".$" → "0<α<∞, of$\mathbf{R}_{\geq 0}$."（句点移到句末，print 原样）
  3. "subspaces of$\mathrm{\Delta X^{ad}}$" 伪 Δ → $\mathrm{X}^{\mathrm{ad}}$（p.252 右栏 "define subspaces of X^ad"）
  4. "scheme$\mathrm{X}.$."、"Each ofthem"、"of$\mathrm{\nabla}k;\mathrm{\nabla}$composing" → "scheme X."、"Each of them"、"of$k$; composing"（∇ 系 MinerU 伪字，print 为分号）
- 备注：Kedlaya 段中 "Theorem 1.3" 与 print 一致（指 §1 的 Galois 群定理，非编号错误）；两个 display 逐字符吻合；本行 211 自 "a fixed norm map on k.…" 起属印刷 p.253，留待 p.009。
## p.009（PDF p.9 / 印刷 p.253）
- PNG：audit/p009.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/253；rank 1 赋值段收尾；Definition 2.2（|·|: R → Γ∪{0}，Γ 全序交换群，|0|=0,|1|=1，|x+y|≤max）；连续性段（{x | |x|<γ} ⊂ R 开）；Remark 2.3（Γ=R_{>0} seminorm 讨论）；Remark 2.4（valuation ring、Γ=K^×/R^×）；supp(|·|)/R(|·|) 段；Definition 2.5 (i)–(iii)
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Definition 2.2："$| \cdot | : \mathbb{R} \to \Gamma∪\{0\}$" 定义域黑板 ℝ → $\mathrm{R}$（print 为环 R，两次：Def 2.2 与 supp 段）；"where \x05 is some totally ordered abelian group"（Γ 丢失、残留 0x05 控制字节）→ "where$\Gamma$is some"（p.253 定义行 PNG 确认 Γ）；句末补句点
  2. "IfR"、"iffor"、"ofR"、"ofx" 缺空格 → 修正（连续性段与 Remark 2.4）
  3. Remark 2.3："$\mathbf{R}_{>0},,$" 双逗号 → "$\mathbf{R}_{>0}$, then"
  4. "rank 1 on$\Gamma(\mathbf{X},\mathcal{O}_X)$ In Huber's theory" 补句点；"i.e.$\mathrm{R}(|\cdot|)=\{x∈\mathrm{K}\,|\,|x|≤1\}$" 补句点（print 原有）
  5. Definition 2.5(i)："$|\cdot|'{=}\alpha∘|\cdot|$" 游离花括号等号 → "$|\cdot|'=\alpha\circ|\cdot|$"+句末补句点
  6. Definition 2.5(iii)："if and only${jf|a|'\geq|b|'}$"（if 塞进 math 花括号）→ "if and only if$|a|'\geq|b|'$."；"for all$a,b∈\mathbf{R}, |a|\geq|b|$" 逗号后补空格
- 备注：本页 Γ 大量为 pdftotext/MinerU 双重丢字（print 的哥特/希腊 Γ 字形不进文本层），全部经 PNG 确认；行 233 起（Definition 2.6）属印刷 p.254，留待下一块。
## p.010（PDF p.10 / 印刷 p.254）
- PNG：audit/p010.png（pngmono 150dpi）
- 核对：页眉 254/PETER SCHOLZE；Definition 2.6 (i)–(iii)（Tate k-algebra/bounded/power-bounded/R°；affinoid 对 (R,R^+)；tft 定义 k⟨T_1,…,T_n⟩ 商）；收敛幂级环 display；R^+=R° 两点理由段（Proposition 2.27、height 1、rational subdomain）；完备化 R̂/(R̂,R̂^+) 段；Definition 2.7 Spa(R,R^+) 定义 display（Γ∪{0} continuous valuation | ∀f∈R^+|f|≤1 /≅）；rational subsets U(f_1,…,f_n/g) display 与 basis 段
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Def 2.6(i)："aR${\sf\Phi}_{\sf(0)}$"（R_0 被打成花体 Φ 乱码）→ a$\mathrm{R}_0$；"bounded$i f M⊂aR_0.$for some"（if 入 math+内部伪句点）→ "bounded if$M⊂aR_0$for some"；"calledpower-bounded"、"ofpowerbounded" 补空格（p.254 (i) 行）
  2. (ii)(iii) 句末补句点（print 原有 "R^+⊂R°."）
  3. (iii) "quotient o$^{c}k⟨…⟩"→"quotient of$k⟨…⟩"（of 被拆成 o+上标 c）
  4. "take R^+=R^∘，but"（全角逗号）→", but"（p.254 右栏首段）
  5. 完备化 "$( \hat{\textmd R},\hat{\textmd R}^+)$" 非法宏 \textmd→\mathrm（print (R̂,R̂^+)）
  6. Definition 2.7 头 "$- \angle e t ({\bf R},{\bf R}^+)$"（—Let 乱码为 \angle et）→ "— Let$(\mathrm{R},\mathrm{R}^+)$"
  7. "write$f↦|f(x)| f o r$the"（for 入 math）→"$|f(x)|$for"
  8. "as basisfor"、"f_1,…,f_n∈\mathbb{R}"、"$g∈\mathbb{R}$"→basis for、∈\mathrm{R} 两处（print 为环 R）、句末补句点
- 备注：Spa 定义 display 的 Γ 本页未丢（\Gamma 在 MD 中存在）；收敛幂级 display 与 print 一致。
## p.011（PDF p.11 / 印刷 p.255）
- PNG：audit/p011.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/255；Remark 2.8（ϖ^N 添加引理、Σh_i f_i=1、|ϖ^N(x)| display）；Spa 特殊性质段（Hochster [18]）；Definition/Proposition 2.9 spectral (i)–(iii)；qc/qs 缩写段；Proposition 2.10 [19, Thm 3.5]；Proposition 2.11 [19, Prop 3.9]（Spa(R,R^+)≅Spa(R̂,R̂^+)）；Proposition 2.12 (i)–(iii)
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Remark 2.8："$\mathrm{to}f_1$"（to 入 math）→ to$f_1$；"$\operatorname{U}({\frac{f_1,\ldots{}{}\mathcal{f}_n}{g}})$" 乱码（\ldots{}{}+\mathcal f_n）→ U(f_1,…,f_n/g)（p.255 Remark 行）
  2. "ofthe/ifit/thefollowing/offinite/ofquasicompact/underfinite×2/ifthe/ofany" 缺空格 → 修正（p.255 各段）
  3. Def/Prop 2.9(i) 句末补句点（print "Spec(A)."）
  4. Proposition 2.11 头 "[19, Proposition$3.97.\mathrm{~-~}Let"（3.9]. — Let 乱码为 3.97）→ "[19, Proposition 3.9]. — Let"；$\hat{\textmd R}$×2→\hat{\mathrm{R}}；"$\mathrm{Spa}(\mathrm{R},\bar{\mathrm{R}^+})\cong\mathrm{Spa}(\hat{\mathrm{R}},\hat{\mathrm{R}^+})$)（伪 \bar、伪花括号嵌套、尾部游离右括号）→$\mathrm{Spa}(\mathrm{R},\mathrm{R}^+)\cong\mathrm{Spa}(\hat{\mathrm{R}},\hat{\mathrm{R}}^+)$,（p.255 Proposition 2.11 行原图）
  5. Proposition$2.12.-Let 乱码头→Proposition 2.12. — Let、句末 X=Spa(R,R^+) 补句点
  6. Prop 2.12(ii)(iii)：$Let f∈\mathbb{R}$→Let f∈R（\mathbb 系误字族+Let 入 math）、"≠0 f o r"→"≠0 for"、"X.$."→"X."、"IfR/thenf"→If R/then f、(iii) Then f∈\mathbb{R}^+→\mathrm{R}^+ 并补句点（p.255 (ii)(iii) 行）
- 备注：|ϖ^N(x)| display 与 print 逐字符一致；(i) 的 \begin{array} 包装为排版伪影、内容正确，未动。
## p.012（PDF p.12 / 印刷 p.256）
- PNG：audit/p012.png（pngmono 150dpi）
- 核对：页眉 256/PETER SCHOLZE；Prop 2.12 证明（[19] Prop 3.6(i)/[20] Lemma 1.4/[19] Lemma 3.3(i)+QED □）；structure sheaf 引入段；Definition 2.13（R[f_i/g]、R[g^{-1}]、aR_0[f_i/g] 基、B 积分闭包、(R⟨f_i/g⟩,B̂)）；Obviously display Spa(R⟨f_i/g⟩,B̂)→Spa(R,R^+)；Proposition 2.14 [20, Prop 1.3] 泛性质（两处箭头）；(O_X(U),O_X^+(U)) 定义 display；For example 完备化句；f_i/g∈S^+ 段；O_X(W)=lim_{U⊂W rational} display
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Proof 行末 ".-"（QED 墓碑乱码）→ "□"（p.256 首行右缘 print 有 tombstone 方块）
  2. Definition 2.13：积分闭包目标 "$\mathrm{R}^+[\frac{\bar f_1}{g},…]$" 伪 \bar 删除；"in$\mathbb{R}[f_i/g…]$"→\mathrm{R}（p.256 定义行）
  3. Proposition 2.14 头 "[20, Proposition$I.3].-In"（罗马 I+乱码）→ "[20, Proposition 1.3]. — In"（print 阿拉伯 1.3）；"(R,R^+)␣(S,S^+)" 缺箭头→→；"Spa(S,S^+)␣Spa(R,R^+)" 缺箭头→→（p.256 Prop 2.14 行原图）
  4. "In particular,$(\mathrm{\bar R}⟨…⟩, B<sup>ˆ</sup> )"（伪 \bar R、B̂ 误为上标 ˆ）→$(\mathrm{R}⟨…⟩,\hat{\mathrm{B}})$（p.256 In particular 行）
  5. "is the completion$\varrho f(\mathrm{R},\mathrm{R}^+)$"（of 误成 ρ f）→"completion of$(\mathrm{R},\mathrm{R}^+)$."+补句点（p.256 For example 行）
  6. "f_i/g∈S^+" 句末补句点（print 原有）
  7. lim 下标 "U⊂Wrational"→"U⊂W rational"（缺空格）；"and similarly for O_X^+"句末补句点
- 备注：Definition 2.13 中 a$\mathsf{R}_0$[f_i/g] 的 \mathsf 字族与 print 粗斜体不同但记号无歧义，按排版伪影保留；三个 display 与 print 一致。
## p.013（PDF p.13 / 印刷 p.257）
- PNG：audit/p013.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/257；Proposition 2.15 [20, Lemma 1.5, Proposition 1.6]（stalk 赋值扩张 + O_{X,x}^+ display）；O_{X,x}/O_{X,x}^+ 局部环极大理想段 + O_X^+(U) display；U≅Spa(O_X(U),O_X^+(U)) 段；"not in general known¹" 段；Definition 2.16 strongly noetherian display（x∈R̂）；tft 例句；Theorem 2.17 [20, Theorem 2.2]；perfectoid k-algebra 预告段；category (V) 定义段；affinoid adic space 段；脚注 1 "And probably not true."
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Proposition 2.15 头 "[20, Lemma 1.5, Proposition$I.6J.-For\any\x∈\mathrm{X}.$"（罗马 I.6、J.-For 乱码、句点错位）→ "[20, Lemma 1.5, Proposition 1.6]. — For any$x∈X$,"；"valuation f \x06→"（0x06 控制字节+Unicode 箭头残骸）→"$f\mapsto|f(x)|$"；"stalk O_{X,x},,"双逗号→单（p.257 Prop 2.15 行原图）
  2. "The ring O_{X,} is a local ring"（丢 x 下标）→ O_{X,x}；"Moreover,for"→"Moreover, for"；"U C X"（C 代 ⊂）→$\mathrm{U}\subset\mathrm{X}$（p.257 局部环段）
  3. "If U⊂X is rational"的伪 H 头（"$H\mathrm{U}\subset\mathrm{X}$"）→"If$\mathrm{U}\subset\mathrm{X}$"、句末补句点（p.257 If U⊂X is rational 行）
  4. Def 2.16 后 "noetherianfor all n≥0"→"noetherian for all$n≥0$."+补句点（p.257 display 后）
  5. Theorem 2.17 头 "[20, Theorem$2.2].-If({\bf R},{\bf R}^+)$"→"[20, Theorem 2.2]. — If$(\mathrm{R},\mathrm{R}^+)$"（p.257 定理行）
  6. category (V) 段：triples 后游离右括号")"删除、"sheafofcomplete"→"sheaf of complete"、"on O_X,,"双逗号→单（p.257 Finally 段）
  7. affinoid adic space 段：triple 后游离右括号")"删除（p.257 Any affinoid 段）
- 备注：Def 2.16 display 的 x∈R̂（带 hat）与 print 一致；脚注 1 以 MinerU HTML 包装保留（内容与 print 逐字符一致）；本页起 0x 控制字节首次成片出现（行 343 已清），后续行见 notes。
## p.014（PDF p.14 / 印刷 p.258）
- PNG：audit/p014.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/Scholze_2012_p258_classical.png（item (1) "x∈k" 行）
- 核对：页眉 258/PETER SCHOLZE；Definition 2.18；Proposition 2.19 [20, Prop 2.1(ii)] + Hom display + R̂→O_Y(Y) 段；例 2.20 引言（R=k⟨T⟩, R^+=R°=k°⟨T⟩、|·|:k→R_≥0、5 types）；树状图（MinerU 抽为图片 page_13_image_7.jpg，print 原图带 (1)–(5) 标注）；(1) classical points（x∈k°，R→k, f=Σa_nT^n↦Σa_nx^n）；(2),(3) rays（f↦sup|a_n|r^n=sup|f(y)|、D(x,r)）
- 结果：**FAIL**（OCR/导出缺陷，已当页修复，以原图为准）：
  1. Proposition 2.19 头 "[20, Proposition$2.I(ii)].-$"（罗马 I）→"[20, Proposition 2.1(ii)]. —"（p.258 Prop 行原图）
  2. "morphisms$\hat R␣\mathcal{O}_Y(Y)$" 缺箭头→$\hat{\mathrm{R}}\to\mathcal{O}_Y(Y)$；"$\hat R^+\mathrm{\Delta}_{is}$ mapped"（is 变 Δ 下标）→"$\hat R^+$is mapped"；句末补句点（p.258 Here, the latter set 行）
  3. 例 2.20："k°⟨T⟩the"补空格、"X=Spa(R,R^+)␣For"补句点（p.258 Example 行）
  4. **图片引用路径断裂**：`![](images/page_13_image_7.jpg)`→`![](Scholze_2012_perfectoid_published/images/page_13_image_7.jpg)`（mineru 导出 images/ 嵌套在同名子目录内，MD 相对路径原本解析不到；目标文件 30.9K 实测存在）——p.258 树状图
  5. (1) 段："evaluatef"→"evaluate f"；"map$\mathrm{R}␣k$（缺箭头）"→$\mathrm{R}\to k$；"$k,$"内伪逗号删除；句末补句点（p.258 (1) 行；"i.e. x∈k"经 300dpi 仲裁确认 print 无 bar，MD 本正确，不改）
  6. (2),(3) 段（p.258 部分）：f∈\mathbb{R}^+→\mathrm{R}^+；D(x,r) 中 "\lfloor y-x \vert"→"|y-x|"；"\}. \mathrm{If} r=0"→"\}$. If$r=0$"（p.258 末段原图）
- 备注：本页含插图（print p.258 中部的树状图），MD 以图片引用承载；其余 5 处同类断裂引用（行 473、1701、1721、1995、2119）按页归属留待对应块处理，本块只修行内所属页。
## p.015（PDF p.15 / 印刷 p.259）
- PNG：audit/p015.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/Scholze_2012_p259_A1k.png（A^1_κ 行）
- 核对：页眉 PERFECTOID SPACES/259；Gaußpoint 收尾；type (2)/(3) 判据（r∈|k^×|、branching）；(4) Dead ends（D_1⊃D_2⊃⋯、⋂D_i=∅、k=C_p、f↦inf_i sup|f(x)| display）；(5) rank 2 赋值（Γ=R_{>0}×γ^Z、f↦max|a_n|γ^n、D(x,<1)）；Γ_{?r} 变体段；D(x,<r)/D(x,r) 段；branching 等价段；A^1_κ/P^1_κ 段；case (5) 反例（f↦max|a_n|γ^n、r>γ>1、T∈R^+）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. type (2)/(3) 判据段：$\dot{\boldsymbol r}$ 伪点删、\boldsymbol{k}→k（print 斜体）；"$Ḋ\mathrm{Ḋ(}x,r)ḌḌ$"Unicode 组合点乱码→$\mathrm{D}(x,r)$（p.259 第二段）
  2. (4) 段："ofthe/ofdisks"补空格、"$\emptyset$ Such"补句点、**"$\mathbf{C}_{\rho}$"→"$\mathbf{C}_p$"**（print 为 C_p，Completed algebraic closure；ρ 系 p 误读，PNG 确认）（p.259 (4) 行）
  3. (4) display 后：f∈\mathbb{R}^+→\mathrm{R}^+、句末补句点
  4. (5) 段："$\mathrm{D}(x,<$ $1)$ 跨 math run 断裂→$\mathrm{D}(x,<1)=\{y∈k^\circ\mid|y-x|<1\}$"+补句点（print "disc D(x,< 1)"，disc 拼写保留）
  5. Γ_{?r} 段：两处 "$\mathrm{if}?=</>$"（if 塞入 math）→"if$? = <$""if$? = >$"（p.259 Similarly 段）
  6. D(x,<r) 段："$\operatorname{If}^{?}=>$"乱码头→"If$? = >$"、尾部 $Ḋ…Ḍ$ 乱码→$\mathrm{D}(x,r)$+补句点；mid 处 \vert 闭合一并统一为 |（p.259 defines a rank 2-valuation 段）
  7. "ifr∉"→"if$r∉"、oftype×2→of type（p.259 One checks 段）
  8. **A^1_κ 段：$\dot{\mathbf{A}^1_\kappa}$ 伪 \dot 删除→$\mathbf{A}^1_\kappa$——300dpi 仲裁（audit/300dpi/Scholze_2012_p259_A1k.png）确认 print 无 dot**；P^1_κ 句末补句点
  9. case (5) 反例段：f∈\mathbb{R}^+→\mathrm{R}^+
- 备注：Γ=R_{>0}×γ^Z 与 Γ_{?r} 的 Γ 在 MD 中完好；三个 max/inf display 与 print 一致；(5) 段 "disc" 拼写为 print 原样保留。
## p.016（PDF p.16 / 印刷 p.260）
- PNG：audit/p016.png（pngmono 150dpi）
- 核对：页眉 260/PETER SCHOLZE；Theorem 2.21 [22, (1.1.11)]（fully faithful functor r display）；Sp(R)→Spa(R,R^+) 段；{qs…}≅{qs…} 等价式；locally of finite type 定义段（X⊂X^ad、U↦U∩X 双射）；{qc admissible opens in X}≅{qc opens in X^ad}；U↦Ũ、admissible cover 段；topos of sheaves 段；sober topological space 段；non-admissible cover 例 + {x||x|≤1}={x||x|=1}∪⋃_{r<1}{x||x|≤r} display；type (5) 解释段；小树状图（page_15_image_12.jpg）；formal models 段
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Theorem 2.21 "afullyfaithfulfunctor"→"a fully faithful functor"；display \text 内 "rigid - analytic"→"rigid-analytic"（print 无空格连字符）（p.260 定理行+display）
  2. "{qs…}<sup>∼</sup>="（≅ 拆成上标）→$\cong$（p.260 等价式行原图）
  3. "locally offinite/ifit/oftheform"→补空格；"$\mathrm{\Delta X\subset X^{ad}}$"伪 Δ 删除；"$\mathrm{U}\subset\mathrm{X}^{\mathrm{ad}} t o\mathrm{U}\cap\mathrm{X}$"（to 入 math）→"to"出 math（p.260 where an adic space 段）
  4. 双射式 "{qc admissible opens in$\mathrm{X}\mathrm{\cong\{qc\opens\in\mathrm{X^ad}\}}$"花括号结构错乱→"{qc admissible opens in$\mathrm{X}\}\cong\{$qc opens in$\mathrm{X}^{\mathrm{ad}}\}$,"+补尾逗号（p.260 双射行原图）
  5. "the inverse ofwhich…U→U<sup>ˆ</sup> ."→"of which…$\mathrm{U}\mapsto\tilde{\mathrm{U}}$."（↦ 印刷原样）；"afamily ofquasicompact"补空格；"$\mathrm{U}_i\subset\mathrm{X}.$forms"伪句点删除；"$\tilde{\mathrm{U}}_i\subset\bar{\mathrm{X}}^{\mathrm{ad}} cover\mathrm{X}^{\mathrm{ad}}$"伪 \bar 删、"cover"出 math、句末补句点（p.260 the inverse of which 段）
  6. "In particular,for/ofsheaves×2"补空格、句末补句点（p.260 In particular 段）
  7. "⟩discussed"补空格（p.260 In the example 行）
  8. "any$r<1$"句末补句点（print 原有）；**图片引用路径断裂**第二处：`![](images/page_15_image_12.jpg)`→`![](Scholze_2012_perfectoid_published/images/page_15_image_12.jpg)`（p.260 小树状图；目标文件 7.4K 实测存在）
- 备注：⋃_{r<1} display 与 print 一致含尾句点；Theorem 2.22 起（行 477）属印刷 p.261，留待 p.017。
## p.017（PDF p.17 / 印刷 p.261）
- PNG：audit/p017.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/261；Theorem 2.22（**𝔛** admissible formal scheme vs X generic fibre 的 fraktur 区分；sp : X^ad → 𝔛 display；(X^ad,O_{X^ad}^+)→(𝔛,O_𝔛)；X≅lim_{←𝔛}𝔛 display；(X,O_X^+)≅lim_{←𝔛}(𝔛,O_𝔛)）；Proof（[3]/[20] Section 4、X→lim_{←𝔛}𝔛 display、Tychonoff、𝔘=Spf R⊂𝔛、U=Spa(R[1/p],R)、O_X^+(U)=R=O_𝔛(𝔘)、QED □）；Spf(k°⟨T⟩) 例与 A^1_κ/P^1_κ's；nonstrict equalities 段；Berkovich 对比预告
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. **Theorem 2.22 首 "Let X be some admissibleformal scheme" 的形式概形丢 fraktur → "Let$\mathfrak{X}$be…"**（print 用 𝔛/X 区分形式概形与其 generic fibre，PNG 确认）；"admissibleformal/genericfibre/ofRaynaud"补空格
  2. "(X^ad,O_{X^ad}^+)␣(𝔛,O_𝔛)" 缺箭头→→、句末补句点；"oflocally"→of locally（p.261 extending to a morphism 行）
  3. "afixed/offinite"补空格、"over$k.$"句点出 math、"formal models X for X"首 X→$\mathfrak{X}$（print "there exist formal models 𝔛 for X"）（p.261 Now assume 段）
  4. "runs overformal models ofX"补空格、"oflocally"×2 补空格（p.261 where 𝔛 runs 段）
  5. Proof："of[3]"、"proofofthe"补空格（p.261 Proof 行）
  6. display X→lim 下标 $\mathfrak{x}$（小写）→$\mathfrak{X}$（print 为大写 𝔛）
  7. Proof 中段："$\mathrm{X,}$one may"/"of$\mathrm{X,}$"逗号出 math；"${\mathfrak{X}}.$. "伪'.$.'；"(as X is$\mathrm{T}_0)_{\mathrm{:}}$"乱码→"(as X is$\mathrm{T}_0$)"；**"$\mathrm{U}=\mathrm{Spa}(\mathrm{R}[\frac{1}{\rho}],R)$"→"$\mathrm{Spa}(\mathrm{R}[\frac{1}{p}],\mathrm{R})$"（print 为 1/p，ρ 系 p 误读）**；"$\mathcal{\bar O}_\mathfrak{X}(\mathfrak{U})$"伪 \bar 删；"assertion.-"→"assertion.□"（QED，print 有 tombstone）（p.261 Proof 中段原图）
  8. "Spf(k°⟨T⟩))"游离右括号删除；"additional$\mathbf{p}^1_\kappa\mathrm{\tilde{s};}$"（小写 p+乱码 's;）→"additional$\mathbf{P}^1_\kappa$'s;"（print 𝐏¹_κ's）（p.261 In the example 段）
- 备注：sp display 与 X≅lim display 本身完好；Definition 2.23 起（行 507）属印刷 p.262，留待 p.018。
## p.018（PDF p.18 / 印刷 p.262）
- PNG：audit/p018.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/Scholze_2012_p262_closure.png（Def 2.23 closure 行）
- 核对：页眉 262/PETER SCHOLZE；Definition 2.23 taut（closure 行）；Most natural adic spaces 段（Hellmann [17]、nontaut）；taut rigid-analytic varieties 段；Theorem 2.24 [22, Prop 8.3.1, Lemma 8.1.8]（Berkovich ≅ taut adic spaces、M(R)↦Spa(R,R^+)）；X^Berk→X^ad 注入映射段（rank-1-valuations、retraction、Hausdorff quotient）；type (1)–(4)/(2)+(5) 收缩段；fibres 段；(R,R^+) affinoid 段（k(x)、k(x)^+）；Proposition 2.25（ϖ-adic completion）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；一处遗留见第 6 条，以原图为准）：
  1. Definition 2.23："ifit/andfor/ofU"补空格；"$\mathrm{~U~C~X~}$"伪 C→$\mathrm{U}\subset\mathrm{X}$；"the closure U of U"——**300dpi 仲裁（audit/300dpi/Scholze_2012_p262_closure.png）确认 print 两个 U 均无 overline**，print quirk 原样保留不改
  2. Theorem 2.24 头："[22, Proposition 8.3.1, Lemma$\delta.l.\delta].-\tilde{T}here"（8.1.8 误为 δ.l.δ、There 加伪 tilde）→"[22, Proposition 8.3.1, Lemma 8.1.8]. — There"；"ofcategories"补空格（p.262 定理行原图）
  3. "{taut adic spaces…}"前的"<sup>∼</sup>="→$\cong$（p.262 等价式）
  4. X^Berk 段："$Let"出 math、"ofsets"→of sets、"$\mathrm{X^{Berk}␣}\ \mathrm{X^{ad}}$"缺箭头→→；"quotient$\mathrm{\Gamma_{\it 0}f X^{ad}}$"（of 乱码为 Γ₀f）→"quotient of$\mathrm{X}^{\mathrm{ad}}$."+补句点（p.262 Let X^Berk map 段）
  5. fibres 段："$\mathrm{X^{ad}␣}\ \mathrm{X^{Berk}}$"缺箭头→→；"$k{\mathrm{-algebra}}.$,"乱码→"$k$-algebra,"；"$\mathcal{O}_{\mathrm{X},x},,$"双逗号→单（p.262 Let (R,R^+) 段）
  6. **Proposition 2.25（部分修复+登记）**：陈述含两处 0x0b 控制字节（ϖ 丢失，print 为 "ϖ-adic completion"×2，PNG 确认）与尾部"\ o f"乱码。尾部已修："$\widehat{k(x)}^{+} \ o f k(x)^{+}$"→"$\widehat{k(x)}^{+}$of$k(x)^{+}$."+补句点。**两处 \x0b 字节本 Edit 通道无法表达（转义在匹配前被剥离，多次尝试失败），按修复协议不转用脚本，登记待后续字节级修复**：行 529 现为 "Then the \x0b-adic completion of$\mathcal{O}_{X,x}^{+}$is equal to the \x0b-adic completion…"，修复方案=将 \x0b 替换为 "$\varpi$"。
- 备注：本页其余文字（Hellmann 段、type 收缩段）与 print 逐句吻合；Proposition 2.25 的 Proof 起于行 531（印刷 p.263），留待下一块。
## p.019（PDF p.19 / 印刷 p.263）
- PNG：audit/p019.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/263；Prop 2.25 证明（O_{X,x}^+→k(x)^+、ϖ-divisible、QED □）；Definition 2.26 affinoid field（print "is pair" 无冠词，print quirk 保留）；In other words 段；Proposition 2.27（points 与 affinoid fields 双射）；Definition 2.28（x ≻ y / y ≺ x specializes、closure {x}‾）；Proposition 2.29 [22, (1.1.6)–(1.1.10)]（x≻y ⟺ K≅L 且 L^+⊂K^+）；generalizations 链段；x_0 段；§3 Perfectoid fields 节标题；Definition 3.1（residue characteristic p>0、Frobenius 满射）；Q_p 排除段；Lemma 3.2（|·|:K→Γ∪{0}、Γ=|K^×| minimal、Γ p-divisible）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 9 条，以原图为准）：
  1. Prop 2.25 证明："map$\mathcal{O}_{X,x}␣k(x)$"缺箭头→$\to$；QED ".-"→"□"（print 有 tombstone）（p.263 首行）
  2. Def 2.26 句末补句点；"is pair"无冠词为 print 原样，保留不改
  3. Prop 2.27 头 "Proposition$2.2.7.\_{Let}$"乱码→"Proposition 2.27. — Let"；"points$gf\mathrm{Spa}$"（of 误为 gf）→"points of$\mathrm{Spa}$"；"affinoidfields"→affinoid fields；maps 缺箭头→→（p.263 Prop 2.27 行原图）
  4. Def 2.28：$\mathrm{X,}$逗号出 math、specializes toy (ory→to y (or y、"$x\succ y ( o r y \prec x ) .$,"乱包→$x\succ y$(or$y\prec x$), if、ify→if y、closure 乱包头清理（p.263 Def 2.28 行；≻/≺ 两符号 MD 本正确）
  5. Prop 2.29 头 "$[22,(\cal I.\cal I.\delta)-(\cal I.\cal I.\cal I 0)].-\cal Let\ (\bf R,\bf R^+)$"（罗马/δ 乱码）→"[22, (1.1.6)–(1.1.10)]. — Let$(\mathrm R,\mathrm R^+)$"；maps 两处缺箭头→→、resp. 后补逗号、"only$i f$"→only if、句末补句点（p.263 Prop 2.29 行原图）
  6. generalizations 段：X,,、ofgeneralizations ofy、oflength/ofthe 补空格、"$t o\:y$"→to$y$+补句点（p.263）
  7. Definition 3.1："perfectoidfield/nonarchimedeanfield/ofresidue"补空格；**"characteristic $/ > 0$"→"$p > 0$"（/ 系 p 误读，PNG 确认）**；句末补句点（p.263 Def 3.1 行）
  8. "unramified extensions of$\mathbf{Q}_b$"→"$\mathbf{Q}_p$"（p.263 We note 段；Q_b 系 Q_p 误读）
  9. Lemma 3.2：头"Lemma 3.2.$-Let"→"— Let"、|·|:K→Γ∪{0} 缺箭头→→、"$|\mathrm K^\times|\ i s$chosen"→"$|\mathrm K^\times|$is chosen"；**"Then \x05 is p-divisible"含 0x05 控制字节（Γ 丢失，print "Then Γ is p-divisible."，PNG 确认）——Edit 通道无法表达该字节，登记待字节级修复（方案：\x05→$\Gamma$）**（p.263 Lemma 3.2 行原图）
- 备注：Def 2.28 的 ≻/≺ 与 Prop 2.29 的 ≅ MD 本正确；"affinoid field is pair"为 print 原样。
## p.020（PDF p.20 / 印刷 p.264）
- PNG：audit/p020.png（pngmono 150dpi）
- 核对：页眉 264/PETER SCHOLZE；Lemma 3.2 证明（Γ≠|p|^Z、|p|<|x|≤1、|y|^p=|y^p|=|x|、QED □）；char 0/char p 分离段；Remark 3.3 deeply ramified [15] Prop 6.6.6；tilting functor 段；ϖ∈K^× 选择段；lim_{←Φ}K°/ϖ display；Φ Frobenius x↦x^p 段；Lemma 3.4 (i)（lim_{←x↦x^♯}K°≅lim_{←Φ}K°/ϖ display、independent of ϖ、lim K°/ϖ→K°: x↦x^♯ display）；(ii)（ϖ^♭、K^♭=(lim K°/ϖ)[(ϖ^♭)^{-1}] display）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 1 条，以原图为准）：
  1. Lemma 3.2 证明："the group \x05 is generated"（Γ 丢失，print "the group Γ is generated"，PNG 确认）——0x05 控制字节 Edit 通道无法表达，登记待字节级修复（\x05→$\Gamma$）；同句其余已修
  2. 同证明："|μ|<|x|≤1"→"$|p|<|x|≤1$"（μ 系 p 误读）；"For such$x,$"→"$x$,"；choose somey→some y；"as desired.-"→"as desired.□"（QED）
  3. char 分离段与 tilting 段："characteristic$\beta.$"×3→"$p$. "（p.264 两段）
  4. ϖ 选择段："$|\rho|≤|\varpi|<1$"→"$|p|≤|\varpi|<1$"（ρ 系 p 误读）+补句点（p.264 For its first description 行）
  5. Φ 段："Frobenius morphism$x↦x^{ρ}$"→"$x↦x^{p}$"（print 为 x^p）；characteristic$\beta.$→$p$.（p.264 where Φ 行）
  6. "## Lemma 3.4."伪标题层级→正文行（同页 Lemma 版式）
  7. Lemma 3.4(i) display：左极限转移 "$x\mapsto x^{\flat}$"→"$x\mapsto x^{\sharp}$"（print 下标为 x↦x^♯，PNG 确认；与 p.246 K^♭=lim_{←x↦x^♯}K 一致）；"independent of$\dot{}_{\varpi}$"乱码→"independent of$\varpi$"（p.264 (i) display 与 given by projection 行）
- 备注：(ii) 的 ϖ^♭、|(ϖ^♭)^♯|=|ϖ|、K^♭ display 均与 print 一致；行 591 (iii) 起属印刷 p.265，留待 p.021。
## p.021（PDF p.21 / 印刷 p.265）
- PNG：audit/p021.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/265；Lemma 3.4 (iii)（K^♭=lim_{←x↦x^♭}K，此处为 ♭ 正确）；In particular 段（K^♭→K、char p）；K^♭° display；|x|_{K^♭}=|x^♯|_K 与 |K^{♭×}|=|K^×|；K^♭°/ϖ^♭≅K°/ϖ、K^♭°/𝔪^♭=K°/𝔪 display；𝔪/𝔪^♭ maximal ideal 段；(iv)；We call K^♭ the tilt；Remark 3.5（ϖ=（ϖ^♭)^♯、ϖ^{1/p^n}=((ϖ^♭)^{1/p^n})^♯ display、K^♭=lim display）；Proof (i)（lim K°/ϖ→K° display、(x̄_0,x̄_1,…)、x^♯=lim x_n^{p^n} display、well-defined、telescoping display (x_n′)^{p^i}−…）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. "perfectoidfield ofcharacteristic$\rho,$"→"perfectoid field of characteristic$p$,"（ρ 系 p 误读；p.265 In particular 段）
  2. "$|\mathrm{K}^{\mathrm{p}\times}|=|\mathrm{K}^{\times}|$"→"$|\mathrm{K}^{\flat\times}|=|\mathrm{K}^{\times}|$"（♭× 误为 p×，print |K^{♭×}|）+句末补句点（p.265 We have 行）
  3. "where m, resp.𝔪^♭.$,"→"where$\mathfrak m$, resp.$\mathfrak m^\flat$,"（首 m 补 fraktur、伪'.$,'删）、"ideal$o f\mathrm K^\circ$"（of 入 math）→of 出 math（p.265 where 行；𝔪 为 fraktur，PNG 确认）
  4. (iv)：IfK/ofcharacteristic 补空格、$\beta,→p,、句末补句点（p.265 (iv) 行）
  5. Remark 3.5："to replace with"丢 ϖ→"to replace$\varpi$with"（print 有 ϖ，文本层整体丢字无残骸）（p.265 Remark 行）
  6. "of$\beta^n\mathrm{^{-th}}$roots"→"of$p^n$-th roots"（β→p）；"choice ofp<sup>n</sup>-th"→"choice of$p^n$-th"（p.265 of p^n-th roots 行）
  7. "lift$x_n∈K^\circ$of$\cdot_{\overline{x}_n}$"伪 \cdot 前缀→"of$\overline{x}_n$"（p.265 Let (x̄_0,…) 行）
- 备注：(iii) display 与 Proof 的 telescoping display（x_n′ 带 prime）均与 print 一致；K^♭=lim_{←x↦x^♭}K 此处 ♭ 正确（与 p.264 (i) display 的 x↦x^♯ 不同，两处 print 本就不同，均已按原图处理）。
## p.022（PDF p.22 / 印刷 p.266）
- PNG：audit/p022.png（pngmono 150dpi）
- 核对：页眉 266/PETER SCHOLZE；well-defined/ϖ|p 段；x↦x^♯ multiplicative 段（lim_Φ→lim_{x↦x^p} 逆映射）；(ii)（ϖ_1、ϖ^♭=(0,ϖ_1,…) display、surjectivity of Φ、|(ϖ^♭)^♯−ϖ_1^♯|≤|ϖ|²）；(iii)（K^♭→lim_{←x↦x^♭}K display、topology 段）；(iv)+QED □；continuous valuations 段；Proposition 3.6（|x|^♭=|x^♯|）；Proof（|x+y|^♭ 双行 display）；K^+/K°/𝔪=K^♭°/𝔪^♭ 段+QED □
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 3 条，以原图为准）：
  1. "using that$\varpi|\boldsymbol p.$"→"$\varpi|p$."（bold p→p、句点出 math）（p.266 首行）
  2. "map$\varprojlim_\Phi K^\circ/\varpi␣\varprojlim_{x↦x^\beta}K^\circ$"缺箭头+β→p→$\to\varprojlim_{x\mapsto x^p}$；"$(x^\sharp,(x^{1/\hbar})^\sharp,…)$"（1/ℏ 系 1/p 误读）→$(x^{1/p})^\sharp$（p.266 It is clear 段）
  3. "surjectivity of \x04 on$K^\circ/\varpi$"（Φ 丢失，print "surjectivity of Φ on K°/ϖ"，PNG 确认）——0x04 字节 Edit 无法表达，登记待字节级修复（\x04→$\Phi$）；(ii) 后段"|(ϖ^♭)^♯−ϖ_1^{\boldsymbol p}|"→"ϖ_1^\sharp"（print 指数为 ♯ 非 p）+中间游离 "$-" 拆分合并（p.266 (ii) 段）
  4. (iii) 段"characteristic$\beta.$."→"$p$. "（β→p+伪'.$.'删）（p.266 (iii) 段）
  5. Proposition 3.6："perfectoidfield/ofK"补空格、"$|\cdot|^\flat gf\mathbf K^\flat$"（of 乱码为 gf）→"$|\cdot|^\flat$of$\mathrm K^\flat$"、句末补句点（p.266 Prop 3.6 行原图）
  6. 末段："nilpotent elements m"→$\mathfrak m$（fraktur，PNG 确认）、$\dot{\mathrm K}^+$伪点删、"$\mathrm{K^\circ/m}=\mathrm{K^\circ/m^\flat}$"→"$\mathrm K^\circ/\mathfrak m=\mathrm K^{\flat\circ}/\mathfrak m^\flat$"（print 右侧为 K^♭°/𝔪^♭，MD 丢 ♭）、"described.-"→"described.□"（QED）（p.266 末段原图）
- 备注：|ϖ_1|^p（(ii) 首行）print 即为上标 p，MD 正确；双行 |x+y|^♭ display 与 print 一致；行 681 起（Theorem 3.7 前 seed 段）属印刷 p.267，留待 p.023。
## p.023（PDF p.23 / 印刷 p.267）
- PNG：audit/p023.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/267；Fontaine-Wintenberger 段；Theorem 3.7 (i)(ii)（tilting functor L↦L^♭、preserves degrees）；defer 段；Proposition 3.8（K^♭ 代数闭 ⇒ K 代数闭）；Proof（P(X) monic irreducible、Newton polygon 线、|a_0|=1、|K^×|=|K^{♭×}| Q-向量空间、Q(X)∈K^{♭°}[X]、K°/ϖ[X]=K^{♭°}/ϖ^♭[X]、P(X+y^♯)、P_1(X)=c^{-d}P(cX+y^♯)、|c|^d≤|ϖ|、QED □）；Theorem 3.7 预告段；§4 Almost mathematics 节标题；Gabber-Ramero [15] 段；𝔪=K^{°∘} 段；Definition 4.1 almost zero
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 5 条，以原图为准）：
  1. Theorem 3.7/(i)/Prop 3.8："perfectoidfield"×3 → perfectoid field（p.267 三行）
  2. (ii)："K<sup>-</sup>"×2 →$\mathrm{K}^\flat$（tilt 记号，print K^♭）（p.267 (ii) 行）
  3. "proofofthis"→proof of this（p.267 defer 段）；"IfK"→If K
  4. Proof 头 "$Proof\mathrm{-}\mathrm{Let}$"→"Proof. — Let"；"$=1,\mathrm{as}|…|$"（as 入 math）→"$=1$, as$|…|$"；"Qhave"→Q have；"$\mathrm{K}^{\mathrm{bo}}[\mathrm X]$"→"$\mathrm K^{\flat\circ}[\mathrm X]$"（b°→♭°）；"root of$\mathrm{\Delta Q}$"伪 Δ→$\mathrm Q$+补句点（p.267 Proof 两行原图）
  5. "constant term P(y^♯) is divisible by \x0b. As"（ϖ 丢失，print "divisible by ϖ."，PNG 确认）——0x0b 字节登记待字节级修复（\x0b→$\varpi$）；同段 "P.-"→"P.□"（QED）
  6. §4 导语段："neglects m-torsion"→"neglects$\mathfrak m$-torsion"（fraktur，PNG 确认）
  7. Definition 4.1："almost zero$i f\mathfrak m x=0$"（if 入 math）→if 出 math；"ifall ofits"→if all of its；"equivalently, m$\mathbf M=0$"→"equivalently,$\mathfrak m\mathbf M=0$"（m→𝔪）+补句点（p.267 Def 4.1 行）
- 备注：P/Q 多项式 display 与 K°/ϖ[X]=K^{♭°}/ϖ^♭[X] 均与 print 一致；Lemma 4.2 起行 709 属印刷 p.268，留待 p.024。
## p.024（PDF p.24 / 印刷 p.268）
- PNG：audit/p024.png（pngmono 150dpi）
- 核对：页眉 268/PETER SCHOLZE；Lemma 4.2 thick + Proof（0→M′→M→M″→0 display、𝔪M′=𝔪M″=0、𝔪²=𝔪、QED □）；localization functors display（K°-mod→K°-mod/(𝔪-torsion)→K-mod）；slightly generic fibre 段（ϖ^N/ϖ^{N/p}/ϖ^{N/p^m}-torsion）；fét 约定段；K_fét≅K^{°a}_fét≅(K^{°a}/ϖ)_fét=(K^{♭°a}/ϖ^♭)_fét≅K^{♭°a}_fét≅K^♭_fét display；Definition 4.3 K^{°a}-mod display；M↦M^a 段；Proposition 4.4 [15, §2.2.2]（Hom_{K^{°a}}(M^a,N^a)=Hom_{K°}(𝔪⊗M,N) display）；alHom 定义
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Lemma 4.2："Thefull/ofalmost"补空格（p.268 Lemma 行）
  2. Proof："with$\mathrm{\ mM′=mM″=0}$"的 m 补 fraktur→$\mathfrak m$（print 𝔪M′=𝔪M″）；"almost zero.-"→".□"（QED）（p.268 Proof 段）
  3. ϖ^N-torsion 段："characteristic$\beta,$"→"$p$,"；"$\dot\varpi^{\mathrm{N}/\dot{p^m}}$"伪点×2→"$\varpi^{\mathrm{N}/p^m}$"；"for all$m,$"→"$m$,"（p.268 右栏）
  4. fét 段："subscript fet"→"subscript fét"、句末游离 "´" 删除（p.268 Following these ideas 段）
  5. Def 4.3 "ofalmost"、M↦M^a 段"ofalmost"补空格（p.268 两行）
  6. Prop 4.4："two$\mathrm{K}^\circ.$-modules"伪'.$'→$\mathrm{K}^\circ$-modules；"-modulefor"→-module for（p.268 Prop 4.4 行）
  7. alHom 句：",$we"补空格、句末补句点（p.268 末行）
- 备注：六个范畴的 display 链与 print 逐字符一致（含 f-acute）；其余段落无差异。
## p.025（PDF p.25 / 印刷 p.269）
- PNG：audit/p025.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/269；Proposition 4.5 [15, §2.2.6, §2.2.12]（abelian tensor category、M^a⊗N^a=(M⊗N)^a display、Hom(L,alHom(M,N))=Hom(L⊗M,N) display）；K^{°a}-algebra 抽象定义段；Proposition 4.6 [15, Prop 2.2.14]（right adjoint K^{°a}-mod→K°-mod: M↦M_* display、M_*=Hom_{K^{°a}}(K^{°a},M) display、(M_*)^a≅M、(M^a)_*=Hom(𝔪,M)）；A_* K°-algebra 段；Definition/Proposition 4.7 (i)（flat、Tor_i^R(N,X) almost zero）
- 结果：**FAIL**（OCR 排版级伪影为主，1 处符号差异已修，以原图为准）：
  1. Prop 4.5 头 "[15,$\\{2.2.6,\\S2.2.12\\}.-\\T$he"→"[15, §2.2.6, §2.2.12]. — The"；"$e.g.$"出 math→e.g.（p.269 Prop 4.5 行原图）
  2. "afunctorial"→a functorial（p.269 for any two 段）
  3. "$\mathrm{K}^{\circ a}.$-algebra"×2 伪'.$'→$\mathrm{K}^{\circ a}$-algebra；"ofan"→of an；"$\mathrm{R}^{a},$, as"→"$\mathrm{R}^{a}$, as"（p.269 This means 段）
  4. Prop 4.6 头 "2.2.$I4].-T$here"→"2.2.14]. — There"（I4 系 14 误读）；"localizationfunctor"→localization functor、"$\mathbf{M}\mapsto\mathbf{M}^a.$,"→"$\mathbf{M}\mapsto\mathbf{M}^a$,"（p.269 Prop 4.6 行）
  5. "then$(\mathbf{M}^a)_*=$ Hom(m, M)"拆分 run→"$(\mathbf{M}^a)_*=\operatorname{Hom}(\mathfrak m,\mathrm M)$"（𝔪 fraktur，PNG 确认）（p.269 adjunction 段）
  6. "$\mathrm{K}^{\circ a}-{\acute c}$algebra"（连字符乱码为 acute-c）→"$\mathrm{K}^{\circ a}$-algebra"；"$\mathrm A_*^a=\mathrm A$"与"$\mathrm A\to\mathrm B$"句末补句点×2；"$\mathrm{K}^{\circ a}.$-modules"伪'.$'（p.269 If A is 段）
  7. (i)：isflat/ifthefunctor/isflat ifand only iffor 补空格、"$H\mathrm R$"→If R、"$i>0_i$"伪下标删（p.269 Def/Prop 4.7 (i) 行）
- 备注：M^a⊗N^a 与 Hom 两个 display 与 print 一致（print 的 Hom 无 K^{°a} 下标，MD 亦无，不添加）；(ii)(iii) 与 Proof 属印刷 p.270，留待 p.026。
## p.026（PDF p.26 / 印刷 p.270）
- PNG：audit/p026.png（pngmono 150dpi）
- 核对：页眉 270/PETER SCHOLZE；Def/Prop 4.7 (ii)（almost projective、Ext^i_R）；(iii)（almost finitely generated/presented、N_ε、f_ε、annihilated by ε、uniformly）；Proof [15] 引用+QED □；Remark 4.8（K°=Hom(K^{°a},K^{°a})→Hom(K^{°a},K^{°a}/ϖ)=Hom(𝔪,K°/ϖ) display、Σϖ^{1−1/p^i}x_i display）；Example 4.9（Q_p(p^{1/p^∞})、p≠2、L=K(p^{1/2})、K°⊕p^{1/2p^n}K°→L° display、killed by p^{1/2p^n}）；Proposition 4.10 [15, Prop 2.4.18]；finite projective 术语段；rank 预告
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. (ii)/(iii)：IfR/isflat/ifand only iffor/almostfinitely×2/off 补空格与出 math（p.270 (ii)(iii) 行）
  2. (iii) 两处丢 ε："annihilated by ."→"annihilated by$\epsilon$"；"for all ."→"for all$\epsilon$"（print 有 ε，PNG 确认；文本层无残骸直接丢字）；"cokernel off"→"cokernel of$f_\epsilon$"（print f_ε）
  3. Proof 行末".-"→"□"（QED，print 有 tombstone）（p.270 Proof 行）
  4. Remark 4.8："$\mathbf{R}^a.$-module"伪'.$'→$\mathbf{R}^a$-module（p.270 Remark 行）
  5. "for arbitrary$x_i∈K^\circ/\varpi$"句末补句点（print 原有）（p.270 sums 段后）
  6. Example 4.9："$\mathbf{Q}_{\mathcal{P}}(\boldsymbol{\phi}^{1/\mathcal{P}^\infty}),\boldsymbol{\mathscr{p}}\neq 2$"→"$\mathbf{Q}_p(p^{1/p^\infty})$, $p\neq 2$"（花体/希腊字族系 p 误读，PNG 确认）；"$\mathrm{K}(\boldsymbol{\mu}^{1/2})$"→"$\mathrm{K}(p^{1/2})$"（μ→p）（p.270 Example 行原图）
  7. Prop 4.10：isflat/almostfinitely×2/ifand only ifit 补空格（p.270 Prop 4.10 行）
- 备注：Hom/Σ 两个 display 与 print 一致；Theorem 4.11 起行 823 属印刷 p.271，留待 p.027。
## p.027（PDF p.27 / 印刷 p.271）
- PNG：audit/p027.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/271；Theorem 4.11 [15, Prop 4.3.27, Remark 4.3.10(i)]（A=A_0×⋯×A_k 分解、∧^i M_i invertible、∧^{i+1}M_i=0、invertible if L⊗_A alHom_A(L,A)=A）；étale morphisms 段；Definition 4.12（μ:B⊗_A B→B）；(i) unramified（e∈(B⊗_A B)_*、ker(μ)_*）；(ii) étale；diagonal closed immersion 段；almost finitely presented étale maps 段；Definition 4.13 finite étale（A_fét）；trace morphisms 段（P_*=alHom(P,A)、P_{**}≅P、End(P)^a=P⊗_A P_* display、tr_{P/A}:End(P)^a→A）；Definition 4.14 trace form（t_{B/A}:B⊗_A B→A display、b′↦bb′ of B）；Remark 4.15 开头（至 "There is no"）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Theorem 4.11 头 "Remark$4.3.IO(i)]$"→"Remark 4.3.10(i)]."（IO 系 10 误读）；such thatfor→such that for；"$\Lambda^{i\breve{+}1}\mathbf M_i$"伪 \breve+Λ→$\bigwedge^{i+1}\mathbf M_i$；"invertible ifL$\otimes_A$$\mathrm{{lHom}_A(L,A)=A}$"→"invertible if$\mathrm L\otimes_{\mathrm A}\operatorname{alHom}_{\mathrm A}(\mathrm L,\mathrm A)=\mathrm A$."（lHom→alHom、跨 math run 合并、补句点）（p.271 定理行原图）
  2. Definition 4.12："Let A be$\iota \ K ^ { \circ a } - a l g e b r a ,$"（ι 系冠词 a 误读+连字符散入 math）→"Let A be a$\mathrm K^{\circ a}$-algebra"（p.271 Def 4.12 行原图）
  3. (i)：**"(B⊗_A B)"与"ker(μ)"补 _* 下标**（print 为几乎元素 (B⊗_A B)_*、ker(μ)_*，PNG 确认）；ifthere→if there；游离 ",$."→"_{*}$."（p.271 (i) 行）
  4. (ii)：ifit→if it、aflat→a flat（p.271 (ii) 行）
  5. Definition 4.13：almostfinitely→almost finitely、offinite→of finite、$\mathrm{\bf A}_{fet}$→$\mathrm{\bf A}_{f\acute et}$（fét 带尖音符，与 p.268 display 一致）（p.271 Def 4.13 行）
  6. trace 段："$\mathrm{K}^{\circ a}\mathrm{-algebra}.$"→$\mathrm K^{\circ a}$-algebra（散字合并）；**"$\mathrm P^*=\mathrm{alHom}(\mathrm P,\mathrm A)$"→"$\mathrm P_*=\operatorname{alHom}(\mathrm P,\mathrm A)$"、"$\mathrm P^{**}\cong\mathrm P$"→"$\mathrm P_{**}\cong\mathrm P$"、display "P⊗_A P^*"→"P⊗_A P_*"（print 三处均为下标 _*，上标系误读）**（p.271 trace 段与 display 原图）
  7. tr_{P/A} 行：End(P)^a␣A 缺箭头→→+补句点（p.271 In particular 行）
  8. Definition 4.14：afinite→a finite、traceform/bilinearform→trace form/bilinear form（p.271 Def 4.14 行）
  9. "composition of${\bf{\dot\mu}}$"伪点删、"$\mathrm B␣\mathrm A$"缺箭头→→、"$bb′ \ g f{\bf B}$"（of 乱码为 \ gf）→"of$\mathbf B$"+补句点（p.271 given by 段）
- 备注：Theorem 4.11 的 ∧^i/∧^{i+1} 上标经 PNG 确认为同一 i 指标；Remark 4.15 起（行 857）跨印刷 p.271/272，其 p.271 部分无差异；行 859（Theorem 4.16）属印刷 p.272，留待下一块。
## p.028（PDF p.28 / 印刷 p.272）
- PNG：audit/p028.png（pngmono 150dpi）
- 核对：页眉 272/PETER SCHOLZE；Remark 4.15 收尾（B_*→End_{A_*}(B_*)、End_{A_*}(B_*)^a=End_A(B)^a）；Theorem 4.16 [15, Thm 4.1.14]（B≅B_*）；nilpotent lift 段；Theorem 4.17（A≅lim A/ϖ^n display、A_fét≅(A/ϖ)_fét、B⊗_A A/ϖ、uniformly finite projective）；Proof [15] Thm 5.3.27+QED □；string of equivalences display（K_fét≅K^{°a}_fét≅(K^{°a}/ϖ)_fét=(K^{♭°a}/ϖ^♭)_fét≅K^{♭°a}_fét≅K^♭_fét）；tautological 段；§5 Perfectoid algebras 节标题；Definition 5.1 (i)(ii)（Φ:R°/ϖ→R°/ϖ 满射；Φ:A/ϖ^{1/p}≅A/ϖ display）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；3 处控制字节遗留见第 4 条，以原图为准）：
  1. Remark 4.15 收尾："map$\mathrm B_*␣\mathrm{End}_{\mathrm A_*}(\mathrm B_*)$"与"almost objects$\mathbf B␣\mathrm{End…}$"两处缺箭头→→、句末补句点（p.272 首段）
  2. Theorem 4.16 头"[I 5,→[15,、ofthe/isfinite/ifand only ifthe补空格；**"isomorphism$\mathrm B\cong\mathrm B^{\ast}$"→"$\mathrm B\cong\mathrm B_*$"（print 为下标星 B_*，PNG 确认）**+补句点（p.272 定理行原图）
  3. Theorem 4.17："$\mathrm K^{\circ a}-algebra.$"散字合并+伪'.$'→$\mathrm K^{\circ a}$-algebra、isflat→is flat；Then 段 thefunctor/ofcategories/againflat/uniformlyfinite×2 补空格；**"$3\otimes_A\mathrm A/\varpi$"→"$\mathbf B\otimes_A\mathrm A/\varpi$"（B 误为数字 3，PNG 确认）**（p.272 定理两行原图）
  4. **控制字节登记**：行 863 "and \x0b-adically"、行 869 "and \x0b-adically"与"A/\x0b-module"、行 889 "is a \x0b-adically"——共 4 处 \x0b（ϖ 丢失，print "ϖ-adically"×3、"A/ϖ-module"，PNG 确认），Edit 通道无法表达，登记待字节级修复（\x0b→$\varpi$）
  5. Proof "easy. -"→"easy.□"（QED，print 有 tombstone）（p.272 Proof 行）
  6. Def 5.1(i)：Frobenius$\Phi:R^\circ/\varpi␣R^\circ/\varpi$缺箭头→→、"ofKalgebras"→of K-algebras（p.272 (i) 行）
  7. Def 5.1(ii)：completeflat→complete flat；末段"$\mathrm K^{\circ a}.$-algebras"伪'.$'删、"ofK^{◦a}"补空格（p.272 (ii) 行与末行）
- 备注：string of equivalences display 与 print 逐字符一致；Def 5.1(iii) 起行 897 属印刷 p.273，留待 p.029。
## p.029（PDF p.29 / 印刷 p.273）
- PNG：audit/p029.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/Scholze_2012_p273_thm52.png（Theorem 5.2 范畴链 display）
- 核对：页眉 PERFECTOID SPACES/273；Def 5.1(iii)（承接 p.028 修毕）；K-Perf/K^{°a}-Perf 命名段；Theorem 5.2（等价 + K-Perf≅K^{°a}-Perf≅(K^{°a}/ϖ)-Perf=(K^{♭°a}/ϖ^♭)-Perf≅K^{♭°a}-Perf≅K^♭-Perf display）；In other words 段；Lemma 5.3 (i)–(iv)（flat 判据、M_*={x∈N[1/ϖ]|∀ε∈𝔪:xε∈N}、(xM)_*=xM_*、M_*/xM_*⊂(M/x𝔪M)_*、ϖ-adic complete）；Remark 5.4；Proof (i)（Tor_i^{K^{°a}}、N=K°/ϖ、M_*=Hom_{K^{°a}}(K^{°a},M)=Hom_{K°}(𝔪,M_*) display）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；2 处控制字节遗留见第 6 条，以原图为准）：
  1. K-Perf 命名段："$\mathrm K^{\circ a}{\ –}\mathrm{Perf},\ \dots$"散字乱码→"$\mathrm K^{\circ a}$-Perf, ...."（p.273 Let K-Perf 段）
  2. Theorem 5.2：ofperfectoid/andperfectoid/thefollowing/ofequivalences 补空格、"$In fact,$"出 math（p.273 定理行）
  3. In other words 段："$\mathrm K^{\circ a}.$-algebras"伪'.$'删、modulo ϖ 后补句点；Lemma 引导段"$\mathrm K^{\circ a.}$ algebra"→$\mathrm K^{\circ a}$-algebra（p.273 两段）
  4. Lemma 5.3(i)："isflat/ifand only/only$if M_*$（\\ast 变体）"修正、**"if and only if M has no -torsion"→"if and only if$\mathrm M_*$has no$\varpi$-torsion"（丢 M_* 下标与 ϖ，print "M_* has no ϖ-torsion"，PNG 确认）**（p.273 (i) 行）
  5. Lemma 5.3(ii)：**"$\mathbf N[\frac1\pi]$"→"$\mathbf N[\frac1\varpi]$"（π 系 ϖ 误读）**；"∀ε∈𝔪: εx∈N"→"∀ε∈𝔪: xε∈N"（print 顺序 xε，PNG 确认）+补句点（p.273 (ii) 行）
  6. Lemma 5.3(iii)：**"(M/xM)_*"漏 𝔪→"(M/x𝔪M)_*"**（print M/x𝔪M，PNG 确认）；"(M/xϵM))in(M/xM)∗"（游离右括号、∗ 散落 math 外且丢 _*）→"$(\mathrm M/x\epsilon\mathrm M)_*$in$(\mathrm M/x\mathrm M)_*$"；句末补句点（p.273 (iii) 行原图）
  7. **控制字节登记**：行 925 两处 \x0b（"M is \x0b-adically complete…"×2，ϖ 丢失）、行 929 一处 \x0b（"multiplication by \x0b on M_*"，print "by ϖ on"）——登记待字节级修复（\x0b→$\varpi$）
  8. Proof (i)："ifand only ifall To$\mathrm r_i^{\mathrm K^\circ}$"→"if and only if all$\operatorname{Tor}_i^{\mathrm K^{\circ a}}$"（To r 拆字+上标漏 a，print Tor_i^{K^{°a}}）（p.273 Proof 行原图）
- 备注：Theorem 5.2 display 经 300dpi 仲裁（audit/300dpi/Scholze_2012_p273_thm52.png）确认第 4 项为 (K^{♭∘a}/ϖ^♭)-Perf，与 MD 一致无需改；M_*=Hom… display 与 print 一致；Proof 行 935 起属印刷 p.274，留待 p.030。
## p.030（PDF p.30 / 印刷 p.274）
- PNG：audit/p030.png（pngmono 150dpi）
- 核对：页眉 274/PETER SCHOLZE；Lemma 5.3(ii)(iii)(iv) 证明（x∈Hom_K(K,N[1/ϖ])=N[1/ϖ] display、(xM)_*=Hom(𝔪,xM_*)={y∈M_*[1/ϖ]|∀ε∈𝔪:εy∈xM_*}=xM_* display、left-exact 包含、m̃/n/ñ/δñ 论证、m_1=ñ/ε、(iv) M_*=(lim M/ϖ^nM)_*=… 三连 display、M=(M_*)^a=… display+QED □）；Proposition 5.5（Φ:R°/ϖ^{1/p}≅R°/ϖ）；Proof（x^p/ϖ powerbounded、x/ϖ^{1/p}、R° ϖ-adic complete flat、QED □）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；5 处控制字节遗留见第 6 条，以原图为准）：
  1. (iii) 首行："$=x\mathbf M_{\mathrm\Omega}$"乱码（Ω）→"$=x\mathbf M$"；"and xM is a flat"→"and$x\mathrm M_*$is a flat"（print xM_*）（p.274 (iii) 行）
  2. (ii) 末句补句点（print "εx ∈ N."）
  3. left-exact 段（p.274 右栏原图多处）："using that is left-exact"→"using that$_*$is left-exact"；"inclusion$\mathrm M_*/x\mathrm M_*⊂(\mathrm M/x\mathrm M),$$(,)$→$_*$"（逗号系星标误读）；"If$m∈(\mathrm M/x\mathrm M)$lifts"补 _*；"evaluate …on ."丢 ε→"on$\epsilon$"；"n˜"组合字符→"$\tilde n$"×2（δn˜ 同）；"divisible by for any"丢 ε→"divisible by$\epsilon$for any"
  4. m_1 段："lift of$m∈(\mathrm M/x\mathrm M),$:"逗号→$_*$（p.274 Then 段）
  5. Prop 5.5/Proof："$\mathrm K^\circ{}_{;};$"伪"_{;};"→"$\mathrm K^\circ$;"；末行"-$"→".□"（QED）
  6. **控制字节登记（7 字节）**：行 935 两处 \x0b（"no \x0b-torsion"×2，print "no ϖ-torsion"）；行 961 \x17+\x0b（"if M is \x17-adically"，print ϖ-adic）；行 967 一处 \x0b（"M_* is \x0b-adically"）；行 973 一处 \x04（"Then \x04 induces"，print "Then Φ induces"）；行 975 一处 \x14 与两处 \x0b（"By assumption, \x14 is surjective"=Φ、"R° is \x0b-adically"×2）——Edit 无法表达，登记待字节级修复（\x0b/\x17→$\varpi$，\x04/\x14→$\Phi$）
- 备注：(ii)(iii) 三个 display 与 print 逐字符一致；Prop 5.5 的 R°/ϖ^{1/p}≅R°/ϖ 正确；Lemma 5.6 起行 977 属印刷 p.275，留待 p.031。
## p.031（PDF p.31 / 印刷 p.275）
- PNG：audit/p031.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/275；Lemma 5.6（R=A_*[ϖ^{-1}]、A_*=R°、Φ:A_*/ϖ^{1/p}≅A_*/ϖ display）；Proof 5.6（almost isomorphism A_*/ϖ^{1/p}→A_*/ϖ、x^p∈ϖA_*、εx∈ϖ^{1/p}A_*）；Lemma 5.7（x^♭∈A_*）；Proof 5.7（y^♭∈ϖA_*、y=ϖ^{k/p}x、ϖ^{(k−1)/p}x、induction、QED □）；power-bounded 段（(εx)^{p^N}∈A_*）；surjectivity 段（A_*/ϖ^{1/p}→A_*/ϖ→A_*/𝔪、z=y/ϖ^{1/p²}、z^p≡x mod ϖ^{(p−1)/p}A_*、𝔪A_*）；Finally 段；K^{°a}-Perf≅K-Perf 段+QED □；Proposition 5.8 reduced+Proof+QED □；char p 段；Proposition 5.9（R perfectoid ⟺ R perfect）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；3 处控制字节遗留见第 6 条，以原图为准）：
  1. Proof 5.6：段首 "By definition, \x04 is an isomorphism"（Φ 丢失）登记待字节级修复；"almost isomorphism$\mathrm A_*/\varpi^{1/p}␣\mathrm A_*/\varpi$"缺箭头→→；句末"A_* = ϖ^{1/p}A_*"补句点（p.275 Proof 5.6 行原图）
  2. **Lemma 5.7："satisfies$x^p∈\mathrm A_*$"→"$x^\flat∈\mathrm A_*$"（print 为 x^♭，PNG 确认）**+补句点（p.275 Lemma 5.7 行）
  3. Proof 5.7："satisfies$y^{\boldsymbol p}∈\varpi\mathrm A_*$"→"$y^\flat∈\varpi\mathrm A_*$"（♭ 系 p 误读）；"$y∈\varpi^{1/\beta}A_*$"→"$\varpi^{1/p}$"；"$\varpi^{(k-1)/\beta}\boldsymbol x$"→"$\varpi^{(k-1)/p}$"；"$\in\mathrm A_*.\mathrm{By}$induction"→". By induction"；"result.-"→"result.□"（p.275 Proof 5.7 行原图）
  4. power-bounded 段："Then x is topologically nilpotent"→"Then$\epsilon x$is topologically nilpotent"（print εx，PNG 确认）；"for all ε∈𝔪 so that"补逗号（p.275 Obviously 段）
  5. surjectivity 段：段首"Next, \x14 is surjective"（Φ 丢失）登记；composition 两处缺箭头→→；"$\varpi^{(p-1)/P}$"×2→"$\varpi^{(p-1)/p}$"（P→p）；"in particular$\tilde z^p$"与"As$x≡\tilde{\mathcal Z}^p$"→plain"$z^p$"（print 无 tilde/花体）；"modulo m$\mathrm A_*$,"→"modulo$\mathfrak m\mathrm A_*$,"（fraktur）（p.275 Next 段原图）
  6. **控制字节登记**：行 983（\x04，"By definition, Φ is"）、行 987（\x0b，"A_* has no ϖ-torsion"）、行 991（\x04，"Next, Φ is surjective"）——登记待字节级修复
  7. K^{°a}-Perf≅K-Perf 段"propositions.-"→".□"；Prop 5.8 Proof"bounded.-"→".□"（QED，print 有 tombstone）（p.275 两行）
- 备注：Lemma 5.6 display 与 Proof 主体、z 构造段均与 print 一致；Prop 5.9 陈述正确；行 1003 起（Prop 5.9 证明）属印刷 p.276，留待 p.032。
## p.032（PDF p.32 / 印刷 p.276）
- PNG：audit/p032.png（pngmono 150dpi）
- 核对：页眉 276/PETER SCHOLZE；Prop 5.9 证明（x^♭ powerbounded、Φ:R°/ϖ→R°/ϖ 满射、R°/ϖ^{1/p}≅R°/ϖ、successive approximation、QED □）；Theorem 5.2 收尾段；Theorem 5.10（A↦Ā=A/ϖ 等价）；cotangent complex 回顾（Quillen [29]、Illusie [23,24]、L_{S/R}∈D^{≤0}(S)、Ω¹_{S/R}、triangle display、short exact sequence display、Dold-Kan、S_• resolution、Ω¹_{S•/R}⊗_{S•}S、smooth 情形）；I²=0 变形问题设定
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 4 条，以原图为准）：
  1. char p 段与 Prop 5.9："characteristic$\beta,$"×2→"$p$,；ofcharacteristic/set ofpowerbounded/ifand only ifR"补空格（p.276 两行）
  2. Prop 5.9 证明："as an element x is powerbounded if and only if$\chi^{\boldsymbol\rho}$is powerbounded"→"if and only if$x^\flat$is powerbounded"（print 为 x^♭，χ/ρ 系 x/♭ 误读，PNG 确认）；"Φ:R°/ϖ␣R°/ϖ"缺箭头→→（p.276 Proof 行原图）
  3. "$\mathrm R^\circ/\varpi^{1/\beta}$"→"$\varpi^{1/p}$"；"that R is perfect.-"→".□"（p.276 Proof 段）
  4. **控制字节登记**：行 1007 一处 \x04（"by Proposition 5.5, \x04 induces"=Φ 丢失）——登记待字节级修复（\x04→$\Phi$）
  5. Dold-Kan 段："resolution S_• ofthe R-algebra"→of the；"simplicial S-module Ω¹_{S•/R}⊗_{S•} S"句末补句点（p.276 Let us briefly recall 段）
  6. smooth 段："if$\mathrm R␣\mathrm S$is a smooth morphism"缺箭头→→（p.276 Just as 段）
  7. I²=0 段："$\mathrm{~I~C~R~}$"伪 C→$\mathrm I\subset\mathrm R$；"flat$\mathrm R_0=\mathrm R/\mathrm I\mathrm{-algebra}$$\mathrm S_0$"散字合并→"flat$\mathrm R_0=\mathrm R/\mathrm I$-algebra$\mathrm S_0$"（p.276 Specifically 段原图）
- 备注：triangle/short exact sequence 两个 display 与 print 一致；Theorem 5.11 起行 1033 属印刷 p.277，留待 p.033。
## p.033（PDF p.33 / 印刷 p.277）
- PNG：audit/p033.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/277；Theorem 5.11 [23, III.2.1.2.3]/[15, 3.2.9]（Ext² obstruction、torsor、automorphism group）；deformation isomorphism 段；S,S′ lifting 段；Theorem 5.12 [23, III.2.2.2]/[15, 3.2.16]（Ext¹ obstruction）；cotangent vanishing 引导段；Proposition 5.13 (i)(ii)（F_p-algebra、R_{(Φ)}/S_{(Φ)}、R_{(Φ)}⊗^L_R S→S_{(Φ)} display、L_{S/R}≅0）；Remark 5.14（Witt vectors W(R)、Ω¹_{R/F_p}=0、dx=dy^p=py^{p−1}dy）；Proof（S• simplicial resolution、Φ_{S•/R}:R_{(Φ)}⊗_R S•→S•_{(Φ)} display、S^k polynomial、X_i↦X_i^p）
- 结果：**FAIL**（OCR 排版级+符号错误，已当页修复，以原图为准）：
  1. Thm 5.11："deformationsforms"→deformations forms；automorphism group 句末补句点（p.277 定理行）
  2. deformation 段句末补句点（print "= S_0."）（p.277 Here 段）
  3. S,S′ 段："S, S<sup>\\x10</sup>"（S′ 丢失、sup 内 0x10 控制字节）——\x10 字节登记待字节级修复（建议整段改写为 "S, $\mathrm S′$"）；"morphism f:S→S′"句末补句点（p.277 Now assume 行原图）
  4. Thm 5.12："extension off$t o f"→"extension of$f_0$to$f"；Ifthere/set ofall/liftsforms 补空格；句末补句点（p.277 定理行）
  5. Prop 5.13(i)："perfect F -algebra"丢 p、"L_{R/F_b}"→"L_{R/F_p}"（b 系 p 误读）+补句点；(ii)："R␣S be a morphism"缺箭头→→、"via$\Phi:R␣R\\.$"乱码→"$\Phi:R\to R$, and"（p.277 Prop 5.13 两行原图）
  6. "in D(R). Then L_{S/R}≅0"补句点；Remark 5.14：**"$\Omega^1_{R/\mathbf F_\phi}$"→"$\Omega^1_{R/\mathbf F_p}$"（φ 系 p 误读）**、"written as$y^\flat,$"→"$y^p$, and"（print y^p，PNG 确认）（p.277 Remark 行）
  7. Proof 段："$\mathrm R_{(\Phi)}\mathrm{-algebra}$"散字合并→$\mathrm R_{(\Phi)}$-algebra；"sending$\mathrm X_i\mapsto\mathrm X_i^p$"补句点（p.277 Proof 段）
- 备注：display（⊗^L 与 Φ_{S•/R}）与 print 一致；行 1065 起（"The assumption says…"）属印刷 p.278，留待 p.034。
## p.034（PDF p.34 / 印刷 p.278）
- PNG：audit/p034.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/Scholze_2012_p278_dX.png（dX_i^p 指数行）
- 核对：页眉 278/PETER SCHOLZE；Φ_{S•/R} quasiisomorphism 段（R_{(Φ)}⊗^L_R L_{S/R}≅L_{S_{(Φ)}/R_{(Φ)}} display、dX_i↦dX_i^p=0）；Gabber-Ramero almost 扩张段；Remark 5.15；Corollary 5.16（L^a_{Ā/(K^{°a}/ϖ)}≅0）；Proof（B=(Ā×K^{°a}/ϖ)_{!!}、B/ϖ^{1/p}≅B via Φ、C↦C_{!!}、§2.2.25、QED □）；Now we can prove Theorem 5.10；Proof of Theorem 5.10（Ā_n 提升、0→Ā^{ϖ^{n−1}}→Ā_n→Ā_{n−1}→0 display、L^a 三角 display）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；2 处控制字节遗留见第 5 条，以原图为准）：
  1. dX 段：句末"with$\mathbf L_{S/R}$-"→".□"（QED）——"dX_i^p"指数经 **300dpi 仲裁**（audit/300dpi/Scholze_2012_p278_dX.png）确认为单独 p（非 p^i），MD 原本正确未改（p.278 On the other hand 段）
  2. Gabber-Ramero 段："$\mathrm K^\circ\cdot$ algebras"（断行连字符伪 \cdot）→$\mathrm K^\circ$-algebras；"$\mathrm{\Delta S^{\it a}}$-modules"伪 Δ→$\mathrm S^a$-modules；"$\mathrm A␣\mathrm B$"缺箭头→→；**"depends only the morphism"缺 on 为 print 原样，保留不改**（p.278 In their book 段原图）
  3. Corollary 5.16 句末补句点；Proof："argue with$(\overline{\Lambda}×…)$"→"$(\overline{\mathrm A}×…)$"（Λ 系 Ā 误读，print 为 Ā）；"$\mathrm K^\circ/\varpi\mathrm{-algebra}$"散字合并→-algebra；"§2.2.25.-"→".□"（p.277 Corollary/Proof 行）
  4. Proof of Theorem 5.10：头"ProofofTheorem${5.}I{0.}-\mathrm{{Let}}$"→"Proof of Theorem 5.10. — Let"；"$(\mathrm K^\circ/\varpi^n)^a{\mathrm{-algebra~}}$"→"-algebra"（p.278 Proof 行原图）
  5. **短正合列 display 结构修正**："$0\to\overline A\stackrel{\varpi^{n-1}}{\to}\overline A_n→…"（把 ϖ^{n−1} 误作映射标号）→"$0\to\overline A^{\varpi^{n-1}}\to\overline A_n\to\overline A_{n-1}\to 0$"（print 首项为带上标 ϖ^{n−1} 的对象 Ā^{ϖ^{n−1}}，PNG 确认）；tensoring 段 L 补上标 ^a；**triangle display 三项 "$\mathrm A/\mathrm A_n/\mathrm A_{n-1}$"→"$\overline{\mathrm A}/\overline{\mathrm A}_n/\overline{\mathrm A}_{n-1}$"（print 均为 Ā-bar）**（p.278 两 display 原图）
  6. **控制字节登记**：行 1077 一处 \x0b（"K^{◦a}/\x0b-algebra"=ϖ 丢失）、行 1079 一处 \x04（"B/ϖ^{1/p}≅B via \x04."=Φ 丢失）——登记待字节级修复
- 备注：R_{(Φ)}⊗^L_R display 与 print 一致；行 1097 起（"This gives a unique system…"）属印刷 p.279，留待 p.035。
## p.035（PDF p.35 / 印刷 p.279）
- PNG：audit/p035.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/279；unique system 段（Ā_n/ϖ^{n−1}≅Ā_{n−1} display，承接 p.034 修毕）；Let A 段+QED □；tilting equivalence K-Perf≅K^♭-Perf 段；A^♭=lim_Φ A/ϖ display；K^{♭°a}=(lim K°/ϖ)^a=… display；R^♭=A^♭_*[(ϖ^♭)^{-1}]；Proposition 5.17（R^♭=lim_{←x↦x^♭}R、A^♭_*=lim A_*、A^♭_*/ϖ^♭≅A_*/ϖ display、R^♭→R x↦x^♯）；Remark 5.18；Proof（A^♭_*=(lim A/ϖ)_*=… display、because _* commutes、image of Φ 段、lim_Φ A_*/ϖ=lim_{←x↦x^♭}A_* display）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 1 条，以原图为准）：
  1. Let A 段："Then A is \x0b-adically complete"（ϖ 丢失）登记待字节级修复；"$\mathrm K^{\circ a}/\varpi\mathrm{-algebras.}$,"散字+伪'.$,'→-algebras,；"as desired.-"→".□"（p.279 Let A 段）
  2. tilting 段："$\mathrm K\cdot\mathrm{Perf}\cong\mathrm K^\flat\cdot\mathrm{Perf}.$."（\\cdot 断行伪影+伪'.$.'）→"$\mathrm K$\text{-Perf}$\cong\mathrm K^\flat$\text{-Perf}."（p.279 In particular 段原图）
  3. "$\mathrm K^{\mathsf{bo}a}$"→"$\mathrm K^{\flat\circ a}$"（bo 系 ♭∘ 误读）（p.279 which we regard 行）
  4. "and set R^♭=A^♭_*[(ϖ^♭)^{-1}]"补句点；Prop 5.17："K<sup>-</sup>"→$\mathrm K^\flat$、"K<sup>-◦a</sup>"→$\mathrm K^{\flat\circ a}$、"$\mathrm A_{~i}^\flat$"（A^♭ 乱码为 A_{~i}）→$\mathrm A^\flat$、$\sf R→\mathrm R$（p.279 Prop 5.17 行原图）
  5. In particular 段：$\mathbb R^\flat→\mathbb R$→$\mathrm R^\flat→\mathrm R$（blackboard 系误字族）+补句点（p.275 In particular 行）
  6. Proof：**"because commutes"丢 _*→"because$_*$commutes"（print "_* commutes"，PNG 确认）**；"image of$\Phi:(A/\varpi)_*\to(A/\varpi)$"目标丢 _*→$(A/\varpi)_*$；"projection$(A/\varpi^{1/p})$)"游离右括号+丢 _*→$(A/\varpi^{1/p})_*$（p.279 Proof 段原图）
  7. **display "lim_{←x↦x^p}A_*"→"lim_{←x↦x^\flat}A_*"（print 转移映射为 x↦x^♭，PNG 确认）**（p.279 But display）
- 备注：A^♭/K^{♭°a} 两个 display 与 print 逐字符一致；行 1141 起（"as in the proof of Lemma 3.4(i)"）属印刷 p.280，留待 p.036。
## p.036（PDF p.36 / 印刷 p.280）
- PNG：audit/p036.png（pngmono 150dpi）
- 核对：页眉 280/PETER SCHOLZE；Lemma 3.4(i) 引用句；A^♭_* ϖ^♭-adic complete 段（A^♭_*/ϖ^♭≅A_*/ϖ display、K^{♭°a}）；tilt 验证段（K^{°a}/ϖ→K^{♭°a}/ϖ^♭→K^{♭°a}→R^♭ 链+QED □）；Remark 5.19（W(R^{♭°})⊗_{W(K^{♭°})}K、θ:W(K^{♭°})→K、[28]）；prototypical example 段；Proposition 5.20（R=K⟨T_i^{1/p^∞}⟩=K°[T̂_i^{1/p^∞}][ϖ^{-1}] display 带宽帽、tilt 为 K^♭⟨T_i^{1/p^∞}⟩）；Proof（R°=K°[T̂_i^{1/p^∞}]、reduces to R°/ϖ、tilt check+QED □）；tilting 下 perfectoid fields 段；Lemma 5.21；Proof 开头（spectral norm ‖x‖_R=inf{|t|^{-1}|t∈K^×,tx∈R°} display）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 4 条，以原图为准）：
  1. "as in the proof of Lemma 3.4(i)"补句点（print 原有）（p.280 首行）
  2. "$\mathrm K^{\mathsf{bo}a}$"→"$\mathrm K^{\flat\circ a}$"（p.280 Therefore 段）；tilt 验证段："$\mathrm K^{\circ a}/\varpi\mathrm{-algebra}\ \mathrm A/\varpi$"散字合并、"$\mathrm K^{\flat\circ a}/\varpi^\flat.$-algebra"伪'.$'删、链尾"$\mathrm R^\flat-$"→".□"（p.280 To see that 段原图）
  3. Remark 5.19："characteristic$\beta,$"→"$p$,"；"$\theta:\mathrm W(\mathrm K^{\flat\circ})␣\mathrm K$"缺箭头+句末补句点；"in our proofwe"→proof we（p.280 Remark 行）
  4. **控制字节登记**：行 1165 一处 \x0b（"which is \x0b-adically complete"，print "ϖ-adically complete"，PNG 确认）——登记待字节级修复（\x0b→$\varpi$）
  5. Prop 5.20 后句与 Proof：**"$\mathrm T_i^{1/\flat^\infty}$"×2→"$\mathrm T_i^{1/p^\infty}$"（tilt 的 T 指数为 p^∞ 非 ♭^∞，PNG 确认）+补句点；"$\mathbf T_i^{1/\rho^\infty}$"×2→"$\mathbf T_i^{1/p^\infty}$"（ρ 系 p 误读）；"$]_{:}$"伪下标冒号删；"$\boldsymbol{\mathrm T}_i^{1/\boldsymbol\beta^\infty}$"×2→"$\mathrm T_i^{1/p^\infty}$"（β 系 p 误读）**（p.280 Prop 5.20 与 Proof 行原图）
  6. "But this is obvious.-"→".□"（QED，print 有 tombstone）（p.280 To see that 段）
  7. Lemma 5.21："R<sup>-</sup>"→$\mathrm R^\flat$、perfectoidfield→perfectoid field、only$if$出 math（p.280 Lemma 行）
- 备注：Prop 5.20 display 的宽帽（K°[\widehat{T_1^{1/p^∞},…,T_n^{1/p^∞}}][ϖ^{-1}]）与 print 一致；spectral norm display 与 print 一致；行 1179 起（"on R, and it is a rank-1-valuation…"）属印刷 p.281，留待下一块。
## p.037（PDF p.37 / 印刷 p.281）
- PNG：audit/p037.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/281；Lemma 5.21 证明（‖x‖_{R^♭}=‖x^♯‖_R、R^♭=lim_{←x↦x^p}R as multiplicative monoids、ϖ^{1/p}R°、x^♭,y^♭∈R^{♭°}、x/(x^♭)^♯ invertible、QED □）；finite étale covers 段；Proposition 5.22（Ā perfectoid K^{°a}/ϖ-algebra、B̄ finite étale）；Proof+QED □；commutative diagram（R_fét←A_fét≅Ā_fét≅A^♭_fét→R^♭_fét / K-Perf←K^{°a}-Perf≅(K^{°a}/ϖ)-Perf≅K^{♭°a}-Perf≅K^♭-Perf）；fully faithful 段；Proposition 5.23；Remark 5.24 开头
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. "$\operatorname{if}\parallel\cdot\parallel_R$"（if 入 math+双竖线变体）→"if$\|\cdot\|_{\mathrm R}$"；"$\Vert\cdot\Vert_{R^\flat}$ Also"补句点；**"$\mathbb R^\flat=\varprojlim_{x\mapsto x^\flat}\mathbb R$"→"$\mathrm R^\flat=\varprojlim_{x\mapsto x^p}\mathrm R$"（blackboard 误字族+转移映射 print 为 x↦x^p，PNG 确认；与 p.279 display 的 ♭ 并存均为 print 原样）**；句末补句点（p.281 首段）
  2. Conversely 段："$\varpi^{1/\ d p}\mathrm R^\circ$"乱码→"$\varpi^{1/p}\mathrm R^\circ$"；"$x^{\mathrm b},y^{\mathrm p}\in\mathbb R^{\mathrm{bo}}$"→"$x^\flat,y^\flat\in\mathrm R^{\flat\circ}$"（b/p/bo 系 ♭/♭/♭∘ 误读）（p.281 Conversely 段原图）
  3. Finally 段："$x^{\mathrm b}$"→"$x^\flat$"；"also x.-"→".□"（QED）（p.281 Finally 行）
  4. Prop 5.22："$\mathrm K^{\circ a}/\varpi-algebra.$,"散字+伪'.$,'→-algebra,；句尾"$K^{\circ a}/\varpi-algebra$"补句点（p.281 Prop 行原图）；Proof 头"$Proof.-\mathrm{Obviously,\ }\mathbf{\overline B}$"→"Proof. — Obviously, $\mathbf{\overline B$"、"[15].-"→".□"
  5. fully faithful 段：ofthem→of them、characteristic$\beta.$→$p$.；Prop 5.23：ofcharacteristic$\beta,$→of characteristic$p$、befinite/isfinite/uniformlyfinite补空格（p.281两段）
- 备注：commutative diagram（array 双行）与 print 方向/≅ 标注格局一致（个别 ≅ 标签在上/下行的微差为排版伪影，内容无歧义，未改）；Remark 5.24 主体属印刷 p.282，留待 p.038。
## p.038（PDF p.38 / 印刷 p.282）
- PNG：audit/p038.png（pngmono 150dpi）
- 核对：页眉 282/PETER SCHOLZE；Remark 5.24 收尾（topology 段）；Prop 5.23 证明（S_0⊂S、S_0^⊥、t_{S/R}:S⊗_R S→R; display、Y integral closure、S^{°a}=Y^a）；uniformly finite projective 段（S°→R^{°n}、R^{°n}→S°、ϖ^N e=Σx_i⊗y_i、ϖ^{N/p^m}e、εe=Σa_i⊗b_i）；s↦(t_{S/R}(s,b_i)) display；(r_1,…,r_n)↦Σa_ir_i display；unramified R^{°a}-algebra 段+QED □；extended commutative diagram
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. Remark 5.24 尾："{\mathrm{-module~M}}carries"散字→-module M carries、"morphism offinitely"→of finitely（p.282 首段/上页边界行）
  2. uniformly finite 段："$\mathbf S^\circ␣\mathbf R^{\circ n}$and"缺箭头→→、composite is multiplication by .丢ε→by$\epsilon$.（p.282 Next 段）
  3. idempotent 段：**"${\varpi^N}_\ell$"→"$\varpi^N e$"（ℓ 系 e 误读，print ϖ^N e，PNG 确认）**；"$\mathrm{\Delta S^\circ\otimes_{R^\circ}S^\circ}$伪 Δ删；"${\bf\Phi}^N e=\sum$"→"$\varpi^N e=\sum$"（Φ 系 ϖ 误读，print ϖ^N e）；"depending on ."丢ε→on$\epsilon$；"We get the map$\mathbf S^\circ␣\mathbf R^{\circ n}$"缺箭头→→（p.282 Let e 段原图）
  4. composite 段："multiplication by , giving"丢ε→by$\epsilon$；"desired properties.-"→".□"（p.282 两行）
  5. extended diagram：$A_{\text{fét}}^b/R_{\text{fét}}^b$→$^\flat$（b→♭）；$K^{\flat oa}→K^{\flat\circ a}$（p.282 末 display）
- 备注：t_{S/R} display 与 (r_1,…,r_n) display 与 print 一致；行 1237 起（"Moreover, using Theorem 4.17…"）属印刷 p.283，留待 p.039。
## p.039（PDF p.39 / 印刷 p.283）
- PNG：audit/p039.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/283；Theorem 5.2 收尾段；Theorem 5.25（fully faithful functor R^♭_fét→R_fét、essential image、uniformly finite projective）；preserves degrees 段；Proof of Theorem 3.7；ramification theory 证明（[15] Prop 6.6.2/6.6.6/6.3.6）；Proof reducing to K^♭ algebraically closed（M=K̄^♭、M^♯、N=∪_L L^♯⊂M̄^♯ dense、Krasner、F^♭=L^H、(F^♭)^♯⊂(L^♯)^H=F、QED □）；§6 Perfectoid spaces: analytic topology 节标题；Definition 6.1；𝔪R°⊂R^+⊂R° 段
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；3 处控制字节遗留见第 5 条，以原图为准）：
  1. "Proofreducing to the case"→Proof reducing、completion ofan→of an（p.283 Proof reducing 行）
  2. **"Any finite extension L ⊂ M of K^♭"→"L ⊂$\overline{\mathrm M}$of K^♭"（print 为 M̄ 带上横线，PNG 确认）**；"union$\mathrm{N}=\mathrm{U}_{I},\mathrm{L}^\sharp\subset\mathrm M^\sharp$"乱码→"$\mathrm N=\bigcup_{\mathrm L}\mathrm L^\sharp\subset\overline{\mathrm M}^\sharp$"（∪_L 误为 U_I，M̄ 丢横线）（p.283 Conversely 段原图）
  3. "Galois extension L of K<sup>-</sup>"→$\mathrm K^\flat$；"$\mathrm F^{\mathrm b}=\mathrm L^{\mathrm H}$"→"$\mathrm F^\flat=\mathrm L^{\mathrm H}$"（b→♭）；"=F.$and"伪'.$'→", and"；"equal.-"→".□"（p.283 Proof reducing 行）
  4. **控制字节登记**：行 1247 三处 \x03（"Let M<sup>\x03</sup>"、"contained in L<sup>\x03</sup>"、"Note that L<sup>\x03</sup>"——♯ 丢失，print M^♯/L^♯，PNG 确认）——登记待字节级修复（\x03→$^{\sharp}$，即 sup 内容替换）
- 备注：Theorem 5.25 与 ramification 段文字与 print 一致；Definition 6.1 与 𝔪R°⊂R^+ 段行 1253/1255 属印刷 p.283 尾与 p.284 交界，其"m$\\mathbb R^\\circ$"缺 fraktur 留待 p.040 一并处理。
## p.040（PDF p.40 / 印刷 p.284）
- PNG：audit/p040.png（pngmono 150dpi）
- 核对：页眉 284/PETER SCHOLZE；Lemma 6.2（R^{♭+}/ϖ^♭≅R^+/ϖ、R^{♭+}=lim_{←x↦x^p}R^+）；Proof+QED □；Theorem 6.3 (i)–(iv)（x^♭∈X^♭、U^♭⊂X^♭、O_X/O_{X^♭} sheaves、𝔪-torsion）；R^+ 非 K°-algebra 备注；outline 段
- 结果：**FAIL**（OCR 数学内容错误，已当页修复，以原图为准）：
  1. （上块边界承接）Def 6.1 后段："m$\\mathbb R^\\circ\\subset\\mathbb R^+\\subset\\mathbb R^\\circ$"→"$\\mathfrak m\\mathrm R^\\circ\\subset\\mathrm R^+\\subset\\mathrm R^circ$"（𝔪 fraktur+blackboard 系误字族，print 𝔪R°⊂R^+⊂R°）+补句点（p.283 末行，本页一并修正）
  2. Lemma 6.2：ofperfectoid补空格、"$\\mathrm K^\\flat.$-algebras"伪'.$'→$\\mathrm K^\\flat$-algebras、"$H(\\mathbb R,\\mathbb R^+)$) maps to"（If 乱码为 H+游离右括号）→"If$(\\mathrm R,\\mathrm R^+)$maps to"；**"Also$\\mathbb R^+=\\varprojlim_{x\\mapsto x^\\rho}\\mathbb R^+$"→"Also$\\mathrm R^{\\flat+}=\\varprojlim_{x\\mapsto x^p}\\mathrm R^+$."（ρ 系 p 误读+blackboard 误字族，print R^{♭+}=lim_{←x↦x^p}R^+，PNG 确认）**（p.284 Lemma 6.2 行原图）
  3. Proof 6.2 "last identities.-"→".□"（p.284 Proof 行）
  4. Theorem 6.3(i)："$\\mathrm X^{\\mathrm b}.$,"伪'.$'与 \\mathrm b→$\\mathrm X^\\flat$、"$x^{\\mathrm p}∈\\mathrm X^{\\mathrm b}$"→"$x^\\flat∈\\mathrm X^\\flat$"（p 系 ♭ 误读，print x^♭∈X^♭）；(ii)"tilt$\\mathrm U^{\\mathrm p}\\subset\\mathrm X^{\\mathrm p}$"→"$\\mathrm U^\\flat\\subset\\mathrm X^\\flat$"（同上）；(iv)"is m-torsion"→"$\\mathfrak m$-torsion"（fraktur，PNG 确认）+补句点（p.284 (i)(ii)(iv) 行原图）
  5. outline 段："$\\mathrm K^{\\circ a}{-}\\mathrm al$gebra"散字→$\\mathrm K^{\\circ a}$-algebra、ofthe→of the、"part$(\\mathrm i)_{-}$and"伪"_{-}"→"part (i), and"（p.284 Let us give 段）
  6. proof outline 段：characteristic$\\boldsymbol p$×2→$p$（p.284 It remains 段）
- 备注：Theorem 6.3 (iii) 与 R^+ 备注段与 print 一致；行 1277 自"as the completed direct limit ofalgebras ofthe previous form"起属印刷 p.285（其中 ofalgebras/ofthe 两处缺空格一并留给 p.041），留待 p.041。
## p.041（PDF p.41 / 印刷 p.285）
- PNG：audit/p041.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/285；proof outline 收尾（char 0 由 char p 推出）；Proof 6.3 开头（well-defined/continuous）；preimage U(f^♯/g^♯) 段；Lemma 6.4（U(f_i/ϖ)、f_i,g∈R^{♭°}、f_n=ϖ^{♭N}）；(i) ϖ-adic completion display R°⟨(f_i^♯/g^♯)^{1/p^∞}⟩ 与 subring display；(ii) O_X(U^♯)^{∘a} display；(iii)；Proof (i) char p 段（R°⟨(f_i/g)^{1/p^∞}⟩ display、flat + ϖ-adic complete）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 5 条，以原图为准）：
  1. outline 收尾："ofalgebras ofthe"→of algebras of the、"the result in characteristic$\beta,$"→"characteristic$p$,"（p.285 首段）
  2. Lemma 6.4：**"$\operatorname U(\frac{f_1,\dots,f_n}{\rho})$"→"$\frac{f_1,\dots,f_n}{\varpi}$"（ρ 系 ϖ 误读，print U(f_1,…,f_n/ϖ)，PNG 确认）**；"$f_i,g\in\mathbb R^{\mathrm{bo}}$"→"$\in\mathrm R^{\flat\circ}$"（bo 系 ♭∘ 误读）；"$f_n=\varpi^{\mathrm{bN}}$"→"$\varpi^{\flat\mathrm N}$"（p.285 Lemma 行原图）
  3. (iii)"The tilt$o f\mathcal O_X(U^\sharp)$"（of 入 math）→of 出 math+补句点；Proof 头"$Proof.-\mathrm{(i)}$(K of characteristic$p)$."→"Proof. — (i) (K of characteristic p)."、段内"characteristic$\beta,$"→"$p$,"（p.285 (iii)/Proof 行）
  4. **控制字节登记**：行 1287 一处 \x0b（"(i) Consider the \x0b-adic completion"，print "ϖ-adic completion"，PNG 确认）；行 1315 一处 \x0b（"and \x0b-adically complete"）——登记待字节级修复（\x0b→$\varpi$）
- 备注：R°⟨(f_i^♯/g^♯)^{1/p^∞}⟩ 两个 display 与 print 一致；行 1317 起（"We want to show that modulo ϖ…"）属印刷 p.286，留待 p.042。
## p.042（PDF p.42 / 印刷 p.286）
- PNG：audit/p042.png（pngmono 150dpi）
- 核对：页眉 286/PETER SCHOLZE；surjection display R°[T_i^{1/p^∞}]→R°[(f_i/g)^{1/p^∞}]；ideal I 段（T_i^{1/p^m}g^{1/p^m}−f_i^{1/p^m}）；/I→R°[…] display；almost isomorphism 段（inverting ϖ、ϖ^k f∈I、(ϖ^{k/p^m}f)^{p^m}∈I）；Reducing display /(I,ϖ)→⟨…⟩/ϖ；Frobenius display /(I,ϖ^{1/p})≅/(I,ϖ)；This finally shows display ⟨…⟩^a；char p 结论；(i)⇒(ii) General K 段（R_0=R°、inclusions display、ϖ^{nN} claim display、1/g^♯=ϖ^{−nN}f_n^♯/g^♯）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 4 条，以原图为准）：
  1. "modulo$\varpi_{:}$"伪"_{:"→$\varpi$（p.286 首段）
  2. almost isomorphism 段："Iff lies"→If f lies、"some k with$^ k f∈I$"（ϖ 丢失）→"some k with$\varpi^k f∈I$"（print ϖ^k f，PNG 确认）（p.286 右栏原图）
  3. "From the definition of$^{\mathrm{~I~},}$"（I 乱码为上标块）→"From the definition of I,"；"characteristic$\beta.$"→"$p$."（p.286 From 段与 char p 结论行）
  4. **控制字节登记**：行 1329 一处 \x0b（"after inverting \x0b, because this also inverts g"=ϖ 丢失）——登记待字节级修复（\x0b→$\varpi$）
  5. Indeed 段："$\varpi^{-\mathrm N}\frac{f_n^\sharp}{g^\sharp}$"→"$\varpi^{-n\mathrm N}\frac{f_n^\sharp}{g^\sharp}$"（print 指数 −nN，PNG 确认）；句末补句点（p.286 Indeed 行原图）
- 备注：surjection//I/(I,ϖ)/(I,ϖ^{1/p})/⟨…⟩^a 五个 display 与 inclusions/ϖ^{nN} claim 两个 display 均与 print 一致；行 1365 起（"Now we prove (iii)…"）属印刷 p.287，留待 p.043。
## p.043（PDF p.43 / 印刷 p.287）
- PNG：audit/p043.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/287；ϖ-adic completion 后 inclusions display（R°{f^♯/g^♯}⊂R°⟨(f^♯/g^♯)^{1/p^∞}⟩⊂R[f^♯/g^♯,…]=O_X(U)）；Thus 段 O_X(U)=R°⟨(f^♯/g^♯)^{1/p^∞}⟩[ϖ^{-1}] display；(i),(iii) General K 段 display；ϖ^{1/p} kernel 段；R°[T]/I→R°[…] display；I 生成段；tilted 段（Spa(S,S^+)→X factors over U^♯）；composite map display（R°⟨T⟩^a→R°⟨(f^♯/g^♯)^{1/p^∞}⟩^a→O_X(U^♯)^{∘a}→S^{∘a}）；tilt composite display；Note that display（R^{♭°}⟨T⟩/(I^♭,ϖ^♭)=R°[T]/(I,ϖ)）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 5 条，以原图为准）：
  1. **inclusions display 首项 "$\mathrm R^\circ\langle f^\sharp/g^\sharp\rangle$"→"$\mathrm R^\circ\{f^\sharp/g^\sharp\}$"（print 首项为花括号 {}，与第二项尖括号 ⟨⟩ 不同，PNG 确认）**；第三项 "$\subset \mathrm R\langle f^\sharp/g^\sharp,\ldots\rangle=\mathcal O_X(\mathrm U)$"→方括号 "$\subset \mathrm R[\ldots]=\mathcal O_X(\mathrm U)$"（print 方括号；右端 =O_X(U) 本正确）（p.287 首 display 原图）
  2. (i),(iii) 段："kernel almost generated by$\varpi^{1/\rho}$"→"$\varpi^{1/p}$"（ρ 系 p 误读）（p.287 is flat over 段）
  3. tilted 段："$\mathrm{Spa}(\mathrm S,\mathrm S^+)␣\bar{\mathrm X}$"缺箭头+伪 bar→"$\mathrm{Spa}(\mathrm S,\mathrm S^+)\to\mathrm X$"（print Spa(S,S^+)→X 无 bar，PNG 确认）（p.287 Let (S,S^+) 段原图）
  4. "where$\Gamma^\flat$is the corresponding ideal"→"$\mathrm I^\flat$is the corresponding ideal"（Γ^♭ 系 I^♭ 误读，print/上文 I^♭）；Note that display 右端 "$\mathrm R^\circ\langle T_i^{1/p^\infty}\rangle/(\mathrm I,\varpi)$"→方括号 "$\mathrm R^\circ[T_i^{1/p^\infty}]/(\mathrm I,\varpi)$"（print 方括号，PNG 确认）（p.287 where/Note that 段原图）
  5. **控制字节登记**：行 1365 一处 \x0b（"pass to the \x0b-adic completion"=ϖ 丢失）——登记待字节级修复（\x0b→$\varpi$）
- 备注：Thus display（O_X(U)=R°⟨…⟩[ϖ^{-1}]）与 composite/tilt composite 两个多行 display 与 print 一致；行 1419 起（"is an isomorphism, so is the composite map…"）属印刷 p.288，留待 p.044。
## p.044（PDF p.44 / 印刷 p.288）
- PNG：audit/p044.png（pngmono 150dpi）
- 核对：页眉 288/PETER SCHOLZE；composite map display（R°⟨T⟩^a/(I,ϖ)→R°⟨(f^♯/g^♯)^{1/p^∞}⟩^a/ϖ→S^{∘a}/ϖ,）；In particular display（≅S^{∘a}/ϖ）；part (i)(ii)(iii) 结论+QED □；approximation lemma 引导；Lemma 6.5（R=K⟨T_i^{1/p^∞}⟩、d∈Z[1/p]、g_{c,ε}∈R^{♭°}、|f(x)−g_{c,ε}^♯(x)|≤|ϖ|^{1−ε}max display）；Remark 6.6 display；Proof（ε(c) 归纳、g_c display、|f(x)−g_c^♯(x)|≤|ϖ|^{1−ε+ε(c)}max display、c′=c+a、ε(0)=ε、ε(c)≤ε−a）
- 结果：**FAIL**（OCR 排版级+记号错误，已当页修复，以原图为准）：
  1. "gives part (iii). -"→".□"（QED，print 有 tombstone）（p.288 结论行）
  2. Lemma 6.5：**"$d∈\mathbf Z[\frac1\rho]$"→"$\frac1p$"（ρ 系 p 误读，print d∈Z[1/p]，PNG 确认）**、"Thenfor"→Then for（p.288 Lemma 行原图）
  3. "homogeneous ofdegree d such thatfor all"→of degree/such that for（p.288 homogeneous 行）
  4. Proof："ε∈Z[1/ρ]"→Z[1/p]；"We also fix$f .$Then"→"fix$f$. Then"（p.288 Proof 行）
  5. Proof 尾：Z[1/ρ]→Z[1/p]×2（p.288 末段）
- 备注：composite/In particular/Remark 6.6/|f−g_c^♯| 四个 display 与 print 逐字符一致（ε 记号在文本层完好）；行 1467 起（"Let$\Delta X=\mathrm{Spa}(R,R^+)…$"）属印刷 p.289，留待 p.045。
## p.045（PDF p.45 / 印刷 p.289）
- PNG：audit/p045.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/Scholze_2012_p289_OXU.png（O_X(U_c^♯) display）
- 核对：页眉 PERFECTOID SPACES/289；U_c⊂X^♭ 段（R^+=R°=K°⟨T_i^{1/p^∞}⟩、|g_c(x)|≤|ϖ^♭|^c、h=f−g_c^♯∈ϖ^{c+1−ε+ε(c)}O_X^+(U_c^♯) display）；previous lemma display（O_X(U_c^♯)^{∘a}=R°⟨(g_c^♯/ϖ^c)^{1/p^∞}⟩^a）；ϖ-adic completion ⊕ display；r_i 段与 h=Σϖ^{c+1−ε+ε(c′)}(g_c^♯/ϖ^c)^i r_i display；ε(c′) 段与 s_i 段；g_{c′} display；claim display（|f(x)−g_{c′}^♯(x)|≤|ϖ|^{1−ε+ε(c′)}max）；|f(x)|>|ϖ|^c 情形 display；Neglecting 段；|f(x)|≤|ϖ|^c 情形 display
- 结果：**FAIL**（OCR 记号错误，已当页修复；1 处控制字节遗留见第 3 条，以原图为准）：
  1. "Let$\mathrm{\Delta X=\mathrm{Spa}(R,R^+)}$"伪 Δ→$\mathrm X$；"$\mathbf K^\circ\langle\mathbf T_0^{1/\rho^\infty},\ldots,\mathbf T_n^{1/\rho^\infty}\rangle$"→"$1/p^\infty$"×2（ρ 系 p 误读）；"$\mathrm U_c\subset\mathrm X^{\mathrm p}$"→"$\mathrm X^\flat$"（p 系 ♭ 误读，print U_c⊂X^♭）（p.289 首段原图）
  2. ε(c′) 段："$\epsilon(c′)\in\mathbf Z[\frac{1}{\it\Delta\phi}]$"（Δφ 系 p 乱码）→"$\mathbf Z[\frac 1p]$"；"Choose$s_i∈\mathbb R^{\flat+}$"→\\mathrm；"$s_i␣0$"缺箭头→"$s_i\to 0$"（p.289 where 段原图）
  3. **控制字节登记**：行 1479 一处 \x0b（"h lies almost in the \x0b-adic completion"=ϖ 丢失）——登记待字节级修复（\x0b→$\varpi$）
  4. O_X(U_c^♯) display：**经 300dpi 仲裁（audit/300dpi/Scholze_2012_p289_OXU.png）确认为 "$\mathrm R^\circ\langle(g_c^\sharp/\varpi^c)^{1/p^\infty}\rangle^a$"（分母 ϖ^c、指数 1/p^∞），MD 原本一致未改**（150dpi 下曾疑分母为 ϖ^♯）
- 备注：h=Σ、g_{c′}、claim、两种情形 estimate 共五个 display 与 print 逐字符一致；行 1517 起（display 之后的正文）属印刷 p.290，留待下一块。
## p.046（PDF p.46 / 印刷 p.290）
- PNG：audit/p046.png（pngmono 150dpi）
- 核对：页眉 290/PETER SCHOLZE；g_{c′} 恒等式两 display（g_{c′}/(ϖ^♭)^c=…+Σ(ϖ^♭)^{1−ε+ε(c′)}(…)^i s_i；g_{c′}^♯/ϖ^c=…+Σϖ^{1−ε+ε(c′)}(…)^i r_i）；f−g_c^♯=f−g_c^♯−h=0 display+QED □；Corollary 6.7 (i)–(iii)（g_{c,ε}∈R^♭、k(x)̂ perfectoid field、X→X^♭ homeomorphism）；Proof (i)（maximal points、f=g_0^♯+ϖg_1^♯+⋯+ϖ^c g_c^♯+ϖ^{c+1}f_{c+1}、K⟨T^{1/p^∞}⟩→R display）；(ii) char p 段；(iii) 段
- 结果：**FAIL**（OCR 排版级+记号错误，已当页修复；1 处控制字节遗留见第 6 条，以原图为准）：
  1. "desired estimate."补 QED □（print 有 tombstone）（p.290 modulo ϖ^{c+1} 段）
  2. Corollary 6.7 头"Corollary${\bf 6.7.\_}Let"乱码→"Corollary 6.7. — Let"；"$\mathrm{Spa}(\mathrm R^\flat,\mathrm R^{\flat}+)$"→$\mathrm R^{\flat+}$；(i)"any$c\geq 0,\epsilon>0.$,"游离'.$,、such thatfor→such that for、$g_{c,\epsilon}∈\mathbb R^\flat→\mathrm R^\flat$（p.290 Corollary 行原图）
  3. (ii)"$x∈\mathrm X,$,"双逗号→单、residuefield→residue field、perfectoidfield→perfectoid field（p.290 (ii) 行）
  4. Proof (i)："after increasing slightly"丢ε→"increasing$\epsilon$slightly"（print "increasing ε slightly"，PNG 确认）；"enlarging$^{c,}$"伪上标→"enlarging c, we"；"$\bar f=g_0^\sharp+…$"伪 \bar 删（print 无 bar）；"$f_{c+1}∈\mathbb R^\circ→\mathrm R^\circ$"（p.290 Proof 行原图）
  5. sending 段："$\mathrm T_i^{1/p^m}$"→"$1/p^\infty$"、"$g_i^{1/\boldsymbol p^m}$"→"$g_i^{1/p^\infty}$"（m 系 ∞ 误读，print T_i^{1/p^∞}/g_i^{1/p^∞}）、"andf"→and f（p.290 sending 行原图）
  6. (ii) 段："$\mathrm K^{\circ a}.$-algebra"伪'.$'→-algebra；**控制字节登记：行1557 一处 \x0b（"the \x0b-adic completion"=ϖ 丢失）——登记待字节级修复（\x0b→$\varpi$）**（p.290 (ii) 行）
  7. (iii) 段："$\mathrm{\Delta X^\flat}$"伪 Δ→$\mathrm X^\flat$、"$\mathrm T_0.$,"→"$\mathrm T_0$"（p.290 (iii) 行）
- 备注：g_{c′} 两个恒等式 display 与 f−g_c^♯=0 display 与 print 逐字符一致；行 1561 起（"For any subset M⊂X…"）属印刷 p.291，留待 p.047。
## p.047（PDF p.47 / 印刷 p.291）
- PNG：audit/p047.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/291；Lemma 5.21 证明收尾（R^♭→k(x)̂→Γ∪{0}、untilt、QED □）；M^♭ 记号段；Corollary 6.8；Proof+QED □；parts (i)(ii) proved 段；char p 段；Definition 6.9 p-finite（R^+ 为 lim_{←Φ}S^+ 的 ϖ-adic completion、R=R^+[ϖ^{−1}]）；Proposition 6.10 (i)–(iii)（S^+=S°、reduced、cohomology 复形 display 0→O_X(X)°→∏O_X(U_i)°→∏_{i,j}→⋯ 被 ϖ 某幂零化）
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 5 条，以原图为准）：
  1. M^♭ 记号段："$\mathrm M\subset\mathrm X.$,"伪'.$,、"$\mathrm M^{\mathrm p}\subset\mathrm X^{\mathrm b}$"→"$\mathrm M^\flat\subset\mathrm X^\flat$"（p/b 系 ♭ 误读）（p.291 For any subset 行）
  2. Corollary 6.8 头"Corollary${\bf 6.8.\mathcal-}Let"乱码→"Corollary 6.8. — Let"、"$\mathrm R^{\flat}+$"→$\mathrm R^{\flat+}$、"Thenfor/rational$\mathrm U\subset\mathrm X.$,"修正（p.291 Corollary行原图）
  3. Proof 段：") among"游离右括号删、"$\mathrm K^{\mathrm b}\mathrm{-algebras.}-$"→"$\mathrm K^\flat$-algebras.□"（QED）（p.291 Proof行）
  4. char p 段与 Def 6.9："characteristic$\beta,$/$\beta.$"×2→"$p$"；"completed perfection${\cal O}f(\mathrm S,\mathrm S^+)$"（of 乱码为 𝒪f）→"perfection of$(\mathrm S,\mathrm S^+)$"；"$gf\underline{\mathrm{lim}}_\Phi$"→"of$\varprojlim_\Phi$"；"$\boldsymbol\varpi^{-1}→\varpi^{-1}$"；句末补句点（p.291 Def 6.9行原图）
  5. **控制字节登记**：行1571 一处 \x0b（"is the \x0b-adic completion"=ϖ 丢失）——登记待字节级修复（\x0b→$\varpi$）
  6. Prop 6.10：oftopologically→of topologically；"(ii)$\mathrm{~U~C~X~}_\mathfrak i$"（C系⊂、伪下标i）→"$\mathrm U\subset\mathrm X$,"；"(O_X(U),O_X^+(U)))"游离右括号删；(iii)"$\mathrm X=\cup\mathrm U_i$"→$\bigcup$、"byfinitely/ofthe"补空格；"power of$\cdot_\varpi$"伪\cdot删（p.291 Prop 6.10各行原图）
- 备注：cohomology 复形 display 与 print 一致；行 1589 起（Proof of Prop 6.10）属印刷 p.292，留待 p.048。
## p.048（PDF p.48 / 印刷 p.292）
- PNG：audit/p048.png（pngmono 150dpi）
- 核对：页眉 292/PETER SCHOLZE；Prop 6.10 证明（[20]/[19]/[2] BGR 引用）；Tate acyclicity display（d_0/d_1/d_2 复形）；ker d_i Banach 段；°-复形 display；ϖ^n im d_{i-1}° 基段+QED □；Proposition 6.11 (i)–(iii)（X≅Y、completed perfection、0→O_X(X)^{°a}→∏→∏_{i,j}→⋯ exact display、H^i=0）；Remark 6.12（annihilated by 𝔪）；Proof (i)(ii)(iii)+QED □
- 结果：**FAIL**（OCR 排版级错误，已当页修复，以原图为准）：
  1. ϖ^n 基段："By parts (i) and$(\ddot{\mathrm{1i}})$"（(ii) 乱码）→"(ii)"；"$\varpi^n$im$d_{i-1}^\circ, n\in\mathbf Z.$,"×2 伪'.$,'→", n∈\mathbf Z$,"；"of$\varpi$.-"→".□"（p.292 By parts 段原图）
  2. Prop 6.11：ofcharacteristic$\rho,→$of characteristic$p$,（ρ系p误读）、completedperfection ofa/oftopologicallyfinite补空格（p.292 Prop行原图）
  3. (ii)："${\mathrm{~V~C~Y~}}_3$"（C系⊂、伪下标3）→"$\mathrm V\subset\mathrm Y$,"；句末补句点（p.292 (ii)行）
  4. (iii)："$\mathrm X=\mathrm U_i\mathrm U_i$"（并集符号丢失）→"$\mathrm X=\bigcup_i\mathrm U_i$"（p.292 (iii)行原图）
  5. "H$^i(...)= 0 f o r i > 0.$"→"$\mathrm H^i(...)=0$ for$i>0$"（for散字出math）（p.292 is exact行）；Remark 6.12 annihilated by m→$\\mathfrak m$（fraktur，PNG确认）；(ii) Proof"affinoid$\\mathrm K\\cdot$-algebra"伪\\cdot→-algebra；(iii) Proof"after completion. -"→".□"（p.292四处）
- 备注：两个 Tate 复形 display 与 print 一致；行 1627 起（Lemma 6.13）属印刷 p.293，留待 p.049。
## p.049（PDF p.49 / 印刷 p.293）
- PNG：audit/p049.png（pngmono 150dpi）
- 核对：页眉 PERFECTOID SPACES/293；Lemma 6.13 (i)–(iv)（filtered direct limit、Spa(R,R^+)≅lim Spa(R_i,R_i^+)、U_j preimage of U_i、quasicompact）；Proof (i)（S_I⊂R、K⟨T_i|i∈I⟩→R、S_I^+ power-bounded/integral、ϖ-adic completion of lim_Φ S_I^+、R_I=R_I^+[ϖ^{−1}]、R^+/ϖ^n=lim_I R_I^+/ϖ^n、f_1−f_2=ϖ^n g、J⊃I）；(ii)（(L,L^+) direct limit、ϖ-adic topology、Spa(L,L^+)≅lim Spa(R_i,R_i^+)）；(iii)（O_{X_j}(U_j)）；(iv)（A_i closed complement、spectral、constructible topology）+QED □；Proposition 6.14 头
- 结果：**FAIL**（OCR 数学内容错误，已当页修复；1 处控制字节遗留见第 5 条，以原图为准）：
  1. Lemma 6.13 (i)(ii) 句末补句点×2（print 原有）；(iii)"(O_{X_i}^+(U_j))"下标 i→j（print O_{X_j}^+(U_j)）、"))"游离右括号删、"$\mathrm{\Delta T}_i$"伪Δ且 T 系 U 误读→"$\mathrm U_i$"、"$f o r j\ge i.$"for散字出math+补句点（p.293 (iii)行原图）
  2. (iv)："${If\mathbf U}_i\subset\mathbf X_i$"→"If$\mathrm U_i\subset\mathrm X_i$"；"image ofX"×2→image of X；句末补句点（p.293 (iv)行）
  3. Proof (i)："K⟨T_i|i∈I⟩␣R"缺箭头→→；"S_I^+⊂R^+ We caution"补句点；"$\varpi\cdot$-adic"→"$\varpi$-adic"；"$\lim_\Phi^{\tiny S_I^+}$"→"$\varprojlim_\Phi\mathrm S_I^+$"；"$(R_I,R_I^+)␣(R,R^+)$"缺箭头→→；"$\varinjlim_{\tiny}$"补下标 I；"$g∈\mathbb R^+$"→\mathrm R^+；completed direct limit of the$(R_I,R_I^+)$句末补句点（p.293 Proof (i)各行原图）
  4. (ii)段："$\operatorname*{lim}_{}$"→$\varprojlim$（p.293 (ii)行）
  5. (iii)段："(O_{X_i}^+(U_j))"下标 i→j（同上）（p.293 (iii)行）
  6. (iv)段："$\mathrm U_{i:}$"伪':'删、"the$\operatorname A_j$are"补空格、"has to be zero.-"→".□"（p.293 (iv)行）
  7. Prop 6.14 头："ofany"→of any、"${\mathrm K}\cdot-algebra, \mathrm X=…"散字→"$\mathrm K$-algebra, $\mathrm X=\mathrm{Spa}(\mathrm R,\mathrm R^+)$"、"$\mathrm X=\mathrm U_i\mathrm U_i$"（并集丢失）→"$\mathrm X=\bigcup_i\mathrm U_i$"（p.293 Prop 6.14行原图）
  8. **控制字节登记**：行1641 一处 \x0b（"equipped with the \x0b-adic topology"=ϖ 丢失）——登记待字节级修复（\x0b→$\varpi$）
- 备注：°-复形 display 已在 p.048 修毕；行 1649 起（"sequence"+exact display）属印刷 p.294，留待 p.050。
