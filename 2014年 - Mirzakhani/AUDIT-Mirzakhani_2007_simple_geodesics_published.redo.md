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

