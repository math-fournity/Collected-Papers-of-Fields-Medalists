# AUDIT（重做）— Borcherds_1992_monstrous_moonshine

- 性质：**Luna 审计重做**。用户 2026-10-02 判定 Luna（Peer-P07, gpt-6-luna）审计不可信，本次按 PDF 原页对全部 41 页逐页全量重检；Luna 的旧修复（fix commit `01fe4a35f8075d3a8a30a56c159660e51045f0d2` 后的 Markdown）也是被检对象，一并以 PDF 原页为准重核。
- Actor：`Wf-R-P07`。
- Host / model / effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置，自报 UNKNOWN：模型自述无法独立核实）。
- 开工时间：2026-10-03 12:17 EDT。
- 工作区：worktree `/Users/aurolafly/.zcode/worktrees/cpf-redo-Borcherds_1992_monstrous_moonshine`（分支 `cpf-redo/Borcherds_1992_monstrous_moonshine`）；只写本篇目录。
- PDF：`Borcherds_1992_monstrous_moonshine.pdf`，41 页，SHA-256 `dee2cb9c3121cf1bf8bddce952d952e0f478a39e497df8946e220e9ceffab501`（本机 shasum -a 256 实测，2026-10-03）。
- 被检 Markdown：`Borcherds_1992_monstrous_moonshine_mineru/Borcherds_1992_monstrous_moonshine__Borcherds_1992_monstrous_moonshine.md`；重做开工基线 SHA-256 `b09bb557b3f70e02088f4a542d370fd530749b086fc6c3773151f897a639cbb1`（= Luna 修复后的最终版；原始 MinerU 产出 SHA-256 `2d89f26db76e7e2187a916d82120cb40f2296092f636fc830c03f8373ea75b18`，commit `4e5d9aabe`，可由 Git 恢复）。
- 文本层判定：`pdftotext -f 1 -l 1`（poppler，/opt/homebrew/bin/pdftotext）首页提取成功、全文可读 → **文本层可用**，采用「PDF 文本层 + 150dpi PNG 目检」**双通道主对账**；印刷原文仍是唯一裁决源，文本层仅作对照通道，文本层自身伪影（如断词、上标拍平）不作为判定依据。
- 渲染证据：本篇 `audit-redo/`（`pngmono` 150dpi，`p001.png`–`p041.png`，本块先做 p.001–p.009）；不动旧 `audit/`。
- 分级：PASS / PASS±（瑕疵但不误导）/ FAIL（数学内容错误或整段丢失，登记"以原图为准"并修复）。
- print quirk 纪律：印刷原文的错字/排版 quirk 忠实保留登记，绝不按数学预期静默改正。
- 全局备注（一次登记，不再逐页重复）：MinerU 导出在行文与行内公式衔接处普遍缺空格（如 `Suppose that$V = …`）、数字/系数被拆成带空格的 TeX 片段（如 `2 ^ { 46 }`）、引用以纯文本形式出现。这些是全文件性的排版风格伪影，不妨碍语义；除非页面特有或误导，不计入分级。
- 进度口径：按任务边界，本块不写 repo 根 `AUDIT-PROGRESS.log`；重做进度以本文件逐页条目与本块逐页 commit 为准。
- 本块范围：p.001–p.009（全篇 41 页重检的后续块另行分派）。

## p.001（PDF p.1 / 印刷 p.1）

- PNG：audit-redo/p001.png（pngmono 150dpi，本块实渲染实读）。
- 核对：题录（标题/期刊卷期页码/作者地址）、摘要全文、目录 1–15 条顺序与措辞、节标题「1 Introduction.」、Theorem 1.1 开头（V=⊕_{n∈Z}V_n、[16,17]、T_g(q)=Σ_{n∈Z}Tr(g|V_n)q^n）。
- 文本层通道：pdftotext 首页与 PNG 一致。
- 结果：**PASS**。
- 备注：MD 行文/地址把印刷断行连字 `Cam-bridge` 并为 `Cambridge`（跨行连字符合并，属正确修复，非内容变更）。Luna 旧修复逐项对印刷复核：摘要 `Co_1`（印刷 Co₁ ✓）、`affine`（印刷 affine ✓）、引文 `[16,17]`（✓）均正确；旧审计所列 `Cam bridge`/`repre sentation`/`afine`/`C o _ { 1 }`/`\lceil 1 6 , 1 7 \rceil` 在当前 MD 已不存在。Theorem 1.1 在印刷页尾断于 `…q^n is`，MD 相应断句位置一致（续文归 p.002 核对）。无修复动作。

## p.002（PDF p.2 / 印刷 p.2）

- PNG：audit-redo/p002.png（pngmono 150dpi，本块实渲染实读）。
- 核对：Theorem 1.1 续句（a Hauptmodul … paper [13]）、Z²-graded monster Lie algebra 段、论文组织段、Fischer-Griess 群阶 2^{46}3^{20}5^97^6 11^213^3·17·19·23·29·31·41·47·59·71、V^♮/V^♮_{-n} 记号、j(τ)−744 展开式（q^{-1}+196884q+21493760q²+…）、Thompson series 定义式、Hauptmodul 定义（SL₂(Z) 在上半平面的作用、(a b;c d)(τ)=(aτ+b)/(cτ+d)、level 1）。
- 文本层通道：pdftotext 第 2 页与 PNG 一致。
- 结果：**PASS±**。
- 差异与处理：
  1. 印刷 "on each space V_n**.** The best way…" 的句点在 MD 中缺失（`…on each space$V _ { n }$ The best way`）。以原图为准，已用 Edit 补回句点（本页 commit）。
  2. Luna 旧修复对印刷复核：`j(\tau)-744`（印刷 j(τ)−744 ✓，旧 MinerU 误为 `j(\dot{\tau})`）、`level 1` 措辞无多余上标（✓）、`The Fischer-Griess` 分词（✓）均正确。旧审计列于本页的 `coeficient` 拼写：本页印刷确有 "the coefficient c(n)"，当前 MD 拼写 `coefficient` 正确，已修复；`dificulty`/`dificult` 两词印刷在本页未出现（属 p.3 正文），归 p.3 核对。
- 备注：印刷 `V^♮`（moonshine 模块记号，上标 natural 号）MD 作 `\natural`，与印刷及 [16] 惯用记号一致；150dpi 下字形与 pdftotext 的怪映射（`\`）互证。印刷页首行 "The / Fischer-Griess" 为跨行排版，MD 合并为正常行文，非内容变更。

## p.003（PDF p.3 / 印刷 p.3）

- PNG：audit-redo/p003.png（pngmono 150dpi，本块实渲染实读）。
- 核对：平移矩阵 (1 1;0 1)∈SL₂(Z)、j(τ) 无穷积公式 (1+240Σσ₃(n)q^n)³/(qΠ(1−q^n)^24)、σ₃(n)=Σ_{d|n}d³、[30]、H/SL₂(Z) 与 Riemann sphere、genus 0 group/Hauptmodul/normalized Hauptmodul 定义、j(τ)−744=e^{−2πiτ}+0+196884e^{2πiτ}+…、Γ₀(2) 与 Γ₀(N)={…|c≡0 mod N}、T₂₋(q)=24+q^{-1}Π_{n>0}(1−q^{2n+1})^{24}=q^{-1}+276q−2048q²+…（2B, atlas [14]）、Thompson [31] 有限性、V⁺/V⁻ 与阶 2 元、"The difficulty…"、印刷 quirk "to to work out"、T_g(τ)（此处印刷用 τ）、monster Lie algebra M 的 Z²=Z⊕Z 分次与 V_{mn}/R²。
- 文本层通道：pdftotext 第 3 页与 PNG 一致（含 "to to work out"）。
- 结果：**PASS±**。
- 差异与处理：
  1. 印刷 "…normalized Hauptmodul for the genus 0 group SL₂(Z)**.**"（段末句点，后接 "Another example…"）在 MD 中缺失。以原图为准，已用 Edit 补回句点（本页 commit）。
  2. Luna 旧修复对印刷复核：平移矩阵 `\begin{pmatrix}1&1\\0&1\end{pmatrix}`（印刷 2×2 ✓，旧 MinerU 误为 `\binom{1}{0}1` 丢列）、`difficulty`（印刷 difficulty ✓）、`+a function`（印刷 "+ a function" ✓，旧 MinerU 误作 `\mathrm{a} function`）均正确；旧审计所列 `dificulty`/`dificult`/系数拆分（240/24/276/2048）在当前 MD 已为正常连写。
- 备注：**print quirk 保留**：印刷原文重复 "it is not difficult **to to** work out"，MD 忠实保留，不改。印刷此处 Thompson series 记号确为 T_g(τ)（与它处 T_g(q) 不同），MD 忠实保留 `$T _ { g } ( \tau )$`。Γ₀(N) 定义中印刷竖线后 "c ≡ 0 mod N" 的 mod 为行文，MD 拆为 `$c \equiv 0$mod$N \}$`，语义一致，属全局排版风格。

## p.004（PDF p.4 / 印刷 p.4）

- PNG：audit-redo/p004.png（pngmono 150dpi，本块实渲染实读）。
- 核对：Z²=Z⊕Z 分次度数表（8 列×9 行，含 R² 行行尾 "⋯." 句点；各 V₃/V₆/V₉/V₂/V₄/V₁/V₋₁ 位置）、Z₂-orbifold of a 26-dimensional torus 段、[3,16,18]/[21] 引文、generalized Kac-Moody 定义段（sl₂ per Dynkin point、sl₂'s 可粘合、Heisenberg、实根 ⟨(α,α)>0 vs 虚根 (α,α)≤0、simple roots must be real、**may also have imaginary simple roots**）、affine sl₂(R[z,z^{-1}]) Jacobi triple product、正根 (m,n),m>0,n>0 与 (1,−1)、multiplicity c(mn)、Weyl group order 2 maps (m,n)→(n,m)。
- 文本层通道：pdftotext 第 4 页与 PNG 一致。
- 结果：**PASS**。
- 仲裁记录：初读 150dpi 曾疑 MD "may also have" 多出 "may"；经 pdftotext + 300dpi 裁剪双证（audit-redo/300dpi/p004-may-also.png，pdftoppm 渲染；gs 300dpi 整页对本页报 Page drawing error，故用 poppler），印刷确为 "may also have"，MD 正确，不改。
- Luna 旧修复对印刷复核：`$\mathbf{Z}_2$-orbifold`（印刷 Z₂-orbifold ✓，旧 MinerU 误为 `Z _ { \mathrm { 2 ^ { - O r b i f o l d } } }`）、`$sl_2$`/`$sl_2's$`（印刷 sl₂/sl₂'s ✓）、`difference`（✓）、`affine`（✓）均正确。旧审计所列 `diference`/`afine`/`s l _ { 2 }` 碎片在当前 MD 已不存在。
- 备注：度数表 MD 与印刷逐格一致（含 R² 所在行行尾印刷的 "⋯."，MD 作 `\dots .` 忠实保留）。`$sl_2’s$` 中撇号以 Unicode 右单引号置于数学内，属 MinerU 全局排版风格，不改。无修复动作。
