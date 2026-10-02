# AUDIT — Kontsevich_1997_deformation_quantization

- actor: `Wf-P12`
- host / model / effort: `zcode` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`（run 级配置，自报 UNKNOWN，未独立核验）
- PDF: `Kontsevich_1997_deformation_quantization.pdf` — 46 页；SHA-256 `8baf650d86c5b8ab0a8b6a70f0f04b0d66e16dca69846247c8869b864180d9e8`；arXiv q-alg/9709040v1 (1997-09-29) LaTeX 排版 born-digital。
- MinerU Markdown: `Kontsevich_1997_deformation_quantization_mineru/Kontsevich_1997_deformation_quantization__Kontsevich_1997_deformation_quantization.md`。
- Original Markdown SHA-256（基线）: `a6912cc51d1587aacf8c4f271dfe7d6206afad09e5b19ffc09a42df5a681d5bd`。
- `doc_id`: `UNKNOWN`。
- 文本层判定：`pdftotext -f 1 -l 1` 首页输出完整清晰（标题/作者/arXiv 戳/§0 全文可读）→ 文本层可用；全程采用「文本层主对账 + 150dpi PNG 视觉核验」双通道；疑难字形回到 PNG/300dpi 裁剪仲裁。
- Method: 逐页（每页 7 步交错）：gs pngmono 150dpi 渲染 `audit/p0NN.png` → Read 看图 → pdftotext 该页文本与 Markdown 对应段五点比对（题录/节标题顺序/定理编号与陈述/公式与上下标/记号；文末页逐条参考文献与收稿日期）→ 分级 → 内容错误结构化 Edit 逐处修复 → 本文件落签 → 每页一提交。print quirk 忠实保留不改。
- 日期时间起点：2026-10-02 13:33 EDT。

## p.001（PDF p.1 / 印刷 p.1）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p001.png`（pngmono 150dpi）
- 核对：题录（标题 DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I / 作者 Maxim Kontsevich / 页边 arXiv:q-alg/9709040v1 29 Sep 1997 竖排戳）、§0 Introduction 与 §0.1 Content of the paper 节标题顺序、Section 1–8 逐段陈述（MD 行 1–27）。
- 结果：`PASS±`。文本逐段与印刷吻合；差异仅为排版级伪影：MD 行 7 `difeomorphisms`、行 17/19/21 `diferential`（印刷均 `differential`/`diffeomorphisms`，ff 连字拍平）；行 19 `an$L _ { \infty }$-morphism` 中 `an` 与公式间空格丢失（印刷 `an L∞-morphism`，内容正确）；行 23/25 `afine`（印刷 `affine`）。按 SOP「PASS± 排版级伪影默认不批量改」，本页不修复。print quirk：印刷原文 `uses in a essential way`（行 9）MD 忠实保留，不改。
- 备注：arXiv 竖排时间戳按惯例不入正文 MD，不视为缺漏。Section 8 段跨页续行（`rigid tensor` → p.2 `categories`）在 p.002 核对。

## p.002（PDF p.2 / 印刷 p.2）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p002.png`（pngmono 150dpi）；仲裁裁剪 `audit/300dpi/Kontsevich_1997_deformation_quantization_p002_sum_m1.png`、`..._p002_gauge_formula.png`（300dpi）
- 核对：Section 8 跨页续行、§0.2 Plans 条目 1)–5)（引 [DL][F][EK][Ko4][AKSZ]）、§0.3 Acknowledgements、§1/§1.1 节标题、星积定义式 $(f,g)\mapsto f\star g=fg+\hbar B_1+\hbar^2B_2+\dots$、两条 $\hbar$-adic 求积式、gauge 群自同构两式与共轭作用式（MD 行 27–79）。
- 结果：`FAIL`→已修复 1 处：MD 行 75 `D(\hbar)=1+\sum_{m>1}D_m\hbar^m`，印刷为 `m\geq 1`（300dpi 裁剪确凿），已 Edit 改为 `\sum _ { m \geq 1 }`。其余 PASS±：行 37 `coeficients`、行 59 `bidiferential`/`diferential`、行 75 `diferential`（印刷 `coefficients`/`bidifferential`/`differential`，ff 连字拍平）；行 53/65 `Let$`、`an$` 等公式前空格粘连；行 59/65 散文 `¯h` 为 `ℏ` 重音分解；行 53 印刷粗体 `\mathbf R` 在「over R」处拍平为正体。print quirk：p.2 末式印刷外层括号本身未闭合 `D(\hbar)\big(D(\hbar)^{-1}(f(\hbar))\star D(\hbar)^{-1}(g(\hbar)),`（300dpi 裁剪 `_p002_gauge_formula.png` 确认无配对高括号），MD 行 78 忠实保留，不改。
- 备注：修复随本页 audit(page) 提交（Master 指令的分页提交纪律）。行 81「We are interested in star-products up to gauge equivalence.」属印刷 p.3 内容，在 p.003 核对。

## p.003（PDF p.3 / 印刷 p.3）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p003.png`（pngmono 150dpi）
- 核对：p.2 跨页句、§1.2 First approximation 全节（Hochschild 2-cocycle 等式、B₁ 对称/反对称分解式、gauge 变换式、B₁⁻=⟨α,df⊗dg⟩ 双矢量式、Poisson/Jacobi 恒等式、{f,g}:=（f⋆g−g⋆f)/ℏ|_{ℏ=0} 式、Schouten-Nijenhuis [α,α]=0）、§1.3 Theorem 陈述与 α(ℏ) 公式、α_{(0)} 路径句（MD 行 81–139）。
- 结果：`PASS±`→含 1 处已修复：MD 行 91 `in the e ecohomological Hochschild complex`，印刷为 `in the cohomological Hochschild complex`（杂散 `e` 为提取故障，PNG 与文本层一致确凿），已 Edit 修复。其余 PASS± 伪影：行 105 `diferential`/`afect`、行 113 `afine`、行 137 `difeomorphism`×2（印刷 `differential`/`affect`/`affine`/`diffeomorphism`，ff 连字拍平）；行 107 `$g .$` 空格错位；行 131 `¯h` 重音分解；行 127 印刷斜体 *A priori* 拍平为正体。全部公式（行 88/96/102/110/118/122/125/134/139）与印刷逐符号吻合。
- 备注：本页无数学内容错误；「e ecohomological」修复随本页提交。

## p.004（PDF p.4 / 印刷 p.4）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p004.png`（pngmono 150dpi）
- 核对：§1.4/§1.4.1/§1.4.2/§1.5/§2 节标题顺序；常系数 Poisson 结构式 α=Σα^{ij}∂_i∧∂_j；Moyal 公式两行（含 Π α^{i_k j_k}(Π∂_{i_k})(f)×(Π∂_{j_k})(g)，Σ 下标 `i₁,…,iₙ;j₁,…jₙ` 的印刷不对称标点忠实保留）；二阶近似公式两行（含 ℏ²/3 项系数）；结合性 O(ℏ³) 式；§1.5 两段；§2 首两段（MD 行 141–183）。
- 结果：`FAIL`→3 处已修复：①行 157 `Here and later symbol denotes the usual product.` 印刷为 `symbol × denotes`（× 为数学符号，PNG 与文本层确凿），已补 `$\times$`；②行 161 `modulo$O ( \hbar ^ { 3 } )$):` 印刷为单闭括号+冒号，多余 `)` 已删；③行 181 `to functions$f , g .$. All` 印刷为 `f, g. All`，重复句点已删。其余 PASS±：行 145/161/175/181 `coeficients`/`bidiferential`/`polydiferential`（ff 拍平）；行 161 `( \mathrm { i . e }` 缩写缺句点、行 181 句末缺句点（标点遗漏伪影，登记不改）；行 175/181 印刷粗体 `\mathbf R` 拍平为正体 R。公式行 148/154/164/170/183 与印刷逐符号吻合（含 `j _ { 1 } , \ldots j _ { n }` 无逗号 quirk）。
- 备注：行 185 起为印刷 p.5 内容（Definition. An (oriented) graph…），在 p.005 核对。

## p.005（PDF p.5 / 印刷 p.5）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p005.png`（pngmono 150dpi）
- 核对：Definition（有向图 Γ=(V_Γ,E_Γ)）、G_n 归属条件 1)–5)（顶点 {1,…,n}⊔{L,R}、边标号 e^1_1…e^2_n、无环 (v,v)、2n 条边）、|G_n|=(n(n+1))^n（PNG 确证上标 n，文本层拍平为 `n(n + 1)`；MD `\left( n ( n + 1 ) \right) ^ { n }` 与印刷一致）、B_{Γ,α} 定义式、n=3 边表 ((1,L),(1,R),(2,R),(2,3),(3,L),(3,R))、图 PNG（顶点 1/2/3→L/R、边标 i₁–i₆，MD 行 217 引 `images/page_4_image_14.jpg`，文件存在于 `_mineru/Kontsevich_1997_deformation_quantization/images/`）、示例算子 (f,g)↦Σα^{i₁i₂}α^{i₃i₄}∂_{i₄}(α^{i₅i₆})∂_{i₁}∂_{i₅}(f)∂_{i₂}∂_{i₃}∂_{i₆}(g)（与图逐边自洽：L 入边 i₁,i₅→f；R 入边 i₂,i₃,i₆→g；i₄ 终点为顶点 3 作用于 α^{i₅i₆}）、一般公式两行（MD 行 185–229）。
- 结果：`PASS±`。无内容错误。伪影登记：行 185 句末缺句点、行 197 列表尾缺逗号、行 203 句末缺句点（标点遗漏）；行 205 `bidiferential`（ff 拍平）；行 187/199 句点/逗号包进数学式（`$v_2 .$`、`$k,$`）。公式行 208/214/222/228 与印刷逐符号吻合。
- 备注：行 231 起（weight W_Γ）为印刷 p.6 内容，在 p.006 核对。mineru 图引用相对路径 `images/…` 为全 repo 统一导出布局，不按内容错误处理。
