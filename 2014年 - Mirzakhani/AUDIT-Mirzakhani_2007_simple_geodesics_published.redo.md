# AUDIT-Mirzakhani_2007_simple_geodesics_published.redo — Luna 审计重做（逐页全量重检）

- 性质：Luna 审计重做。用户 2026-10-02 判定 Luna 审计不可信，本文件按 PDF 原页逐页全量重检，
  Luna 旧修复（已并入 MinerU Markdown 基线）一并重核；印刷原文（PDF）是唯一裁决源。
- actor：Wf-R-P11
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- 日期：2026-10-03 12:03 EDT 起
- 原文 PDF：`2014年 - Mirzakhani/Mirzakhani_2007_simple_geodesics_published.pdf`（44 页）
  SHA-256 = `c19a088d97b2b3223481341d059ef7836ea9f575f580d3bf574d0b475e7615cf`
- 被检 Markdown 基线：`2014年 - Mirzakhani/Mirzakhani_2007_simple_geodesics_published_mineru/Mirzakhani_2007_simple_geodesics_published__Mirzakhani_2007_simple_geodesics_published.md`
  SHA-256 = `65320689fcaaa8fcbdc4133f224bfba5e9d298c8f8056362e9770a2b5aa43527`（重做起点）
- 证据图：`2014年 - Mirzakhani/audit-redo/`（pngmono 150dpi，p0NN.png；旧 `audit/` 不动）
- 文本层判定：`pdftotext -f 1 -l 1` 首页输出干净（题录、Contents 全部可读）→ **文本层可用，
  本篇采用双通道主对账**：每页 gs pngmono 150dpi PNG 目检 + pdftotext 该页文本逐句对账；
  两者均以 PDF 原页为准，冲突时以 300dpi 裁剪仲裁（如有）。
- 印刷页码换算：Invent. math. 167, 179–222 (2007)；PDF p.N = 印刷 p.(178+N)。
- 分级：PASS / PASS±（瑕疵但不误导）/ FAIL（数学内容错误或整段丢失）。
- 修复纪律：Markdown 内容错误用结构化 Edit 逐处修复（含修正 Luna 旧修复中的错误），每处可溯源该页
  证据；print quirk 忠实登记不改；每页一提交 `redo(page): …`。

---

## p.001（PDF p.1 / 印刷 p.179）
- PNG：audit-redo/p001.png（pngmono 150dpi）；旁证：pdftotext -f 1 -l 1（文本层干净）。
- 核对：题录（刊名卷期页眉头 Invent. math. 167, 179–222 (2007)、DOI 10.1007/s00222-006-0013-2、标题、
  作者、Princeton 单位与 e-mail、Oblatum 19-VII-2005 & 17-VII-2006、Published online: 12 October 2006 –
  © Springer-Verlag 2006）；Contents 1–8 条目与页码 179/186/190/194/203/206/211/217；§1 Introduction
  首段；首段公式 $V_{g,n}(L_1,\ldots,L_n)$、$\mathcal{M}_{g,n}$、$(\mathbb{R}_{\ge0})^n$、$\mathbf{Mod}_{g,n}$、
  $\mathcal{T}_{g,n}(L)$。
- 结果：**PASS±**。
- 差异（不误导的排版伪影，未改动）：
  - 行内公式前后空格合并：L27 "the volume$V_{g,n}...$of the moduli space"、L29 "Given$L=..." 等；
  - Contents 点线简化为 "....."（L16–23）。
- Luna 旧修复重核：刊眉头补录（MD L3–4）与原页一致；L27 无 $\bar{V}$（原页即 $V_{g,n}$）、
  L29 $(\mathbb{R}_{\ge0})^n$ 与原页下标 ≥0 一致——两处旧修复正确，维持。
- 备注：页断在 "We"（L29 末），其后内容属 p.2。

## p.002（PDF p.2 / 印刷 p.180）
- PNG：audit-redo/p002.png（pngmono 150dpi）；仲裁裁剪：audit-redo/p002_table_300dpi.png、
  audit-redo/p002_theorem11_300dpi.png（300dpi）。
- 核对：页顶承接句与展示式 $\mathcal{M}_{g,n}(L)=\mathcal{T}_{g,n}(L)/\mathrm{Mod}_{g,n}.$；Theorem 1.1
  陈述与 $\operatorname{Vol}_{wp}$、求和式 $V_{g,n}(L)=\sum_{|\alpha|\le 3g-3+n}C_\alpha\cdot L^{2\alpha}$、
  $C_\alpha>0\in\pi^{6g-6+2n-|2\alpha|}\cdot\mathbb{Q}$、多指标约定句；$V_{1,1}=L^2/24+\pi^2/6$；
  Wolpert/[Zog] 两段；Remark 段；Table 1 全部 6 行数值。
- 结果：**PASS±**（3 处标点偏离已修，见下）。
- 修复登记（本 redo）：
  1. MD L37：Theorem 1.1 印刷为 "$L_n^2$; namely"（300dpi 裁剪 + 文本层双证），MinerU 行多出逗号
     "$L_n^2,$;" → 删多余逗号；
  2. MD L45：印刷 "(Z≥0)^n**,** L^α=…"（文本层逗号），MinerU 丢逗号 → 补回；
  3. MD L45：印刷句末 "αᵢ**.**"，MinerU 缺句号 → 补回。
- print quirk 登记不改：Table 1 (0,4) 行印刷系数 **1/2**、(1,2) 行印刷 **1/192** 且第二因子为
  **12π²+L₁²+L₂²**（300dpi 裁剪直证；通行 arXiv 版数值不同，但本印刷原文如此，即裁决源；
  MD 与印刷一致，不动）。页顶眉头 "180 / M. Mirzakhani" MinerU 未收录（全篇通例，登记一次）。
- Luna 旧修复重核：本页 Table 1 与 Theorem 陈述当前值与印刷一致，未见旧修复引入新错误。
- 备注：行内公式前后空格合并伪影同 p.1，通例登记。

## p.003（PDF p.3 / 印刷 p.181）
- PNG：audit-redo/p003.png（pngmono 150dpi）。
- 核对：页顶承接段（We approach… [M]）；McShane identity 引导句；Theorem 1.2 (McShane) 陈述与
  展示式 (1.1) $\sum_\gamma(1+e^{\ell_\gamma(X)})^{-1}=1/2$ 及求和说明；Calculation of Vol(M_{1,1}) 段；
  $\mathcal{M}_{1,1}^*$ 定义式；$\pi:\mathcal{M}_{1,1}^*\to\mathcal{M}_{1,1}$、$\ell(X,\gamma)=\ell_\gamma(X)$；
  (1.2) 式与 $f(x)=(1+e^x)^{-1}$；$\mathcal{M}_{1,1}^*=\mathcal{T}_{1,1}/\mathrm{Stab}(\alpha)$ 段与
  Fenchel–Nielsen 坐标句；$\mathcal{M}_{1,1}^*\cong\{(\ell,\tau)\mid 0\le\ell\le\tau\}/(x,0)\sim(x,x)$。
- 结果：**PASS±**（5 处偏离已修，见下）。
- 修复登记（本 redo，证据=p.3 PNG + pdftotext 文本层）：
  1. MD L84：印刷词为 "McShane's"（原页行末换行连字符 "Mc-/Shane's"），MinerU 误留 "Mc-Shane's" →
     改 "McShane's"；
  2. MD L84：印刷 "the case $g=n=1$**.** Consider"，缺句号 → 补 "."；
  3. MD L96：印刷 "define ℓ : M*₁,₁ → **ℝ** by"（PNG 黑板粗体直证），MinerU 拍平为裸 "R" →
     改 $\mathbb{R}$；
  4. MD L108：印刷 "$f(x)=(1+e^x)^{-1}$**.**"，缺句号 → 补 "."；
  5. MD L110：印刷 "determined by the pair $(\ell,\tau)$**,** the length"，缺逗号 → 补 ","；
     同行 MinerU 双句号 "around$\gamma .$. Note"（印刷单句号）→ 改 "around$\gamma$. Note"。
- print quirk 登记不改：无（本页印刷无异常 quirk）。
- Luna 旧修复重核：Theorem 1.2、(1.1)/(1.2) 展示式与记号当前与印刷一致。
- 备注：页断在 ≅ 式后，p.4 起于 "On the other hand"（MD L116）；眉头缺失与空格合并通例照登。

## p.004（PDF p.4 / 印刷 p.182）
- PNG：audit-redo/p004.png（pngmono 150dpi）；仲裁裁剪：audit-redo/p004_Mod_DR_300dpi.png（300dpi）。
- 核对：Weil–Petersson 辛形式句 $\pi^*(\omega_{wp})=d\ell\wedge d\tau$；三重积分展示式；
  $\mathrm{Vol}(\mathcal{M}_{1,1})=2\int_0^\infty\ell f(\ell)\,d\ell=\cdots=\pi^2/6$；Calculation of V_{g,n}
  引导与 (I)/(II) 两条；"(I): Generalized McShane's identity" 段；辅助函数 𝒟, ℛ : ℝ₊³ → ℝ₊；
  Theorem 1.3 陈述与展示式 (1.3)；两个和的说明句；cusp 允许句（页末 "geodesic of length 0."）。
- 结果：**PASS±**（4 处偏离已修，见下）。
- 修复登记（本 redo）：
  1. MD L116：印刷 $d\ell\wedge d\tau$ 均为数学斜体，MinerU 把 "dτ" 拍平为正体外文 → 并回公式；
  2. MD L136：印刷正文 "each orbit of Mod_{g,n}"（300dpi 直证**正体**），MinerU 作 $\mathbf{Mod}$
     （粗体）→ 改 $\mathrm{Mod}_{g,n}$（Luna 旧遗留错误修正）；
  3. MD L136：印刷两辅助函数为花体 **𝒟**, **ℛ**（300dpi 直证），MinerU 把 𝒟 拍平为平文 "D," →
     改 $\mathcal{D}$（ℛ 原已正确）；
  4. MD L144：MinerU "pair ofpants" 丢空格 → "pair of pants"；同行平文 γ → $\gamma$。
- print quirk 登记不改：无。注：本页正文 Mod 为正体而 p.1 正文为粗体，系原文自身的混用，各自如实
  对应，不作统一。
- Luna 旧修复重核：Theorem 1.3 与 (1.3) 展示式（\mathcal{D}/\mathcal{R}、求和限、=L₁）当前与印刷一致。
- 备注：页界 L116–L146；(1.4) 及其后属 p.5。

## p.005（PDF p.5 / 印刷 p.183）
- PNG：audit-redo/p005.png（pngmono 150dpi）；仲裁裁剪：audit-redo/p005_Mod_300dpi.png（300dpi）。
- 核对：特例句与 (1.4) $\sum_\gamma\mathcal{D}(L,\ell_\gamma(X),\ell_\gamma(X))=L$；non-peripheral 说明；
  $\mathcal{D}(x,y,y)\sim 2x/(1+e^y)$ 与 "implies the original McShane identity (1.1) when L → 0"；
  "(II): Integration over the moduli space" 段；$S_{g,n}$/$\mathcal{T}_{g,n}$/同调类句；
  $\mathcal{O}_\gamma=\{[\alpha]\mid\alpha\in\mathrm{Mod}_{g,n}\cdot\gamma\}$；$\mathrm{Mod}_{g,n}$-orbit 句；
  $f_\gamma(X)=\sum_{[\alpha]\in\mathcal{O}_\gamma}f(\ell_\alpha(X))$ 与 $f_\gamma:\mathcal{M}_{g,n}\to\mathbb{R}_+$；
  Our goal 段；covering space 定义 $\pi^\gamma:\mathcal{M}_{g,n}^\gamma=\{(X,\alpha)\mid X\in\mathcal{M}_{g,n},$
  and $\alpha\in\mathcal{O}_\gamma$ is a geodesic on X$\}\to\mathcal{M}_{g,n}$；页末 $\ell:\mathcal{M}_{g,n}^\gamma\to\mathbb{R}_+$。
- 结果：**PASS±**（6 处偏离已修，见下）。
- 修复登记（本 redo，证据=p.5 PNG + 300dpi 裁剪 + 文本层）：
  1. MD L160：印刷 "when L → 0**.**"，缺句号 → 补 "."；
  2. MD L162：印刷 "over $\mathcal{M}_{g,n}(L)$**.**"，缺句号 → 补 "."；
  3. MD L164：印刷 "homotopy class of γ**,** and let"，MinerU 作 "$\gamma.$, "（多句号）→ 删多余句号；
  4. MD L172：印刷 "$\mathrm{Mod}_{g,n}$-orbit"（300dpi 直证**正体**），MinerU 作 $\mathbf{Mod}$
     （粗体；Luna 旧遗留）→ 改正体；
  5. MD L172：印刷 "For any function f : ℝ₊ → ℝ₊**,**"，缺逗号 → 补 ","；
  6. MD L188：印刷集合定义含 "**and** α ∈ 𝒪_γ is a geodesic on X}" 且 "$\to\mathcal{M}_{g,n}$**,** where"，
     MinerU 丢 "and" 与逗号 → 补回。
- print quirk 登记不改：无。
- Luna 旧修复重核：(1.4)、𝒟 记号、$\mathcal{O}_\gamma$ 定义（\operatorname{Mod} 正体）当前与印刷一致。
- 备注：页界 L148–L192；L194 起（defined by…）属 p.6。

## p.006（PDF p.6 / 印刷 p.184）
- PNG：audit-redo/p006.png（pngmono 150dpi）。
- 核对：defined by ℓ(X,η)=ℓ_η(X) 句；$\int f_\gamma dX=\int f\circ\ell\,dY$；level set 句与
  $\int f\circ\ell\,dY=\int_0^\infty f(t)\mathrm{Vol}(\ell^{-1}(t))dt$；main idea 段；$S_{g,n}(\gamma)$
  切割段（≅、$\gamma\times(0,1)$、n+2 边界、$\mathcal{M}(S_{g,n}(\gamma),\ell_\gamma=t)$ 定义）；
  circle bundle 箭头图；$S^1$-action 段；$\ell^{-1}(t)/S^1\cong\mathcal{M}(S_{g,n}(\gamma),\ell_\gamma=t)$；
  Vol 展望式；页末 "…at a point"（句跨页）。
- 结果：**PASS±**（2 处偏离已修）。
- 修复登记（本 redo，证据=p.6 PNG + 文本层）：
  1. MD L206：印刷 "induced on $\ell^{-1}(t)$**.**"，缺句号 → 补 "."；
  2. MD L216：MinerU 双句号 "along$\gamma .$. The"（印刷单句号）→ 改 "along$\gamma$. The"。
- print quirk 登记不改：L210 "along$\gamma ;$"（math 内多余空格+分号）为 MinerU 空格类伪影，
  语义无歧义，按通例不逐处改。
- Luna 旧修复重核：本页公式（含箭头图 array、≅ 式、Vol 式句号）当前与印刷一致。
- 备注：页界 L194–L228（L228 止于 "at a point"，"is in fact t/2…" 属 p.7）。

