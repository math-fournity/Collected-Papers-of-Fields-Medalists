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
