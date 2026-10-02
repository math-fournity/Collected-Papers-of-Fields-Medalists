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
