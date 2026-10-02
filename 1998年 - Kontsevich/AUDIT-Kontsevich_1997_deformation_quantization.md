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

## p.006（PDF p.6 / 印刷 p.6）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p006.png`（pngmono 150dpi）
- 核对：weight W_Γ 引言段、Lobachevsky 上半平面构造段（𝓗={z∈C|Im(z)>0}、φ^h(p,q)∈R/2πZ、l(p,q)/l(p,∞) 两线夹角、counterclockwise 方向、h=harmonic）、角度示意图（MD 行 235 引 `images/page_5_image_2.jpg`，文件存在）、Arg/Log 公式 φ^h=(1/2i)Log((q−p)(q̄−p)/((q−p̄)(q̄−p̄)))、𝓗_n 配置空间定义式与定向段、图的几何实现段（L↦0、R↦1）、权公式 w_Γ:=1/(n!(2π)^{2n})∫_{𝓗ₙ}⋀_{i=1}^n(dφ^h_{e¹ₖ}∧dφ^h_{e²ₖ})、Lemma、Theorem f⋆g:=ΣℏⁿΣ_{Γ∈Gₙ}w_ΓB_{Γ,α}(f,g)（MD 行 231–268）。
- 结果：`FAIL`→2 处已修复：①行 233 `through p and the point  on the absolute` 印刷为 `the point ∞ on the absolute`（PNG+文本层确凿），已补 `$\infty$`；②行 253 `to the vertex$L ,$, and point` 印刷为 `to the vertex L, and point`，双逗号已删。print quirk 忠实保留：权公式⋀ 指标 `i=1..n` 与 φ 下标 `e^1_k/e^2_k` 混用为印刷原貌（MD 行 258 逐符号一致）。其余 PASS±：行 240 `A r g`/`L o g` 字距拆分；行 233 `I m ( z )` 同类；行 253 句末缺句点；行 281 起属印刷 p.7。
- 备注：行 271「defines an associative product.」起为印刷 p.7 内容，在 p.007 核对。

## p.007（PDF p.7 / 印刷 p.7）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p007.png`（pngmono 150dpi）；仲裁裁剪 `audit/300dpi/Kontsevich_1997_deformation_quantization_p007_zgrading.png`、`..._p007_shift_functor.png`（300dpi）
- 核对：Theorem 收尾两句、§3/§3.1/§3.2 节标题顺序、Super^k 段（ΠV=V⊗k^{0|1}、Koszul 符号规则、Vect^k）、Graded^k 段（Ẽ^{(n)} 奇偶、ℰ=⊕Π^n(ℰ^n)）、shift functor 段（k[1]^{-1}≃k、k[1]^{≠-1}=0）、ℰ=⊕_{n∈Z}ℰ^n[−n] 式、dgLie 公理三式（d²=0、Leibniz、反交换、Jacobi 恒等式，含 (−1)^{γ̄₁·γ̄₂} 等指标）与 γ̄_i 说明句（MD 行 271–317）。
- 结果：`FAIL`→3 处幻影字符已修复（300dpi 裁剪确凿）：①行 285 `$\mathbf{Z}\mathbf{\cdot}$-grading` 印刷为 `Z-grading`，删幻影 `·`；②行 289 `k[1]^{≠-1}=\dot{0}` 印刷为 `= 0`（0 上无点），删 `\dot{}`；③行 289 `denoted by [n],$\mathbf{\psi}_n\in\mathbf{Z}$` 印刷为 `[n], n ∈ Z`（无 ψ），删幻影 ψ。另修 1 处重复标点：行 315 `$\gamma_i.$, i.e.` 印刷为 `γ_i, i.e.`。其余 PASS±：行 275/297/301/317 `diferential`/`diferential`/`diferential`（含两处节标题 ff 拍平，登记不改）；行 285 `Graded^k$` 后缺句点（登记）；行 289 `(acting from the$\mathrm{right})` 正体拍平。公式行 304/308/312 与印刷逐符号吻合。
- 备注：行 319 起（Def_g 函子）为印刷 p.8 内容，在 p.008 核对。

## p.008（PDF p.8 / 印刷 p.8）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p008.png`（pngmono 150dpi）；仲裁裁剪 `audit/300dpi/Kontsevich_1997_deformation_quantization_p008_degree_minus1.png`（300dpi）
- 核对：Def_g 函子定义段、MC(g)={γ∈g¹|dγ+½[γ,γ]=0}/Γ⁰ 式、Γ⁰ 仿射作用与无穷小作用 α∈g⁰↦(γ̇=dα+[α,γ]) 式、无单位代数 m^{dim(m)+1}=0 与 Def_g(m)=MC(g⊗m)、Artin 代数 m′=m⊕k·1、线性拓扑 m:=ℏR[[ℏ]]=lim←(ℏR[ℏ]/ℏ^kR[ℏ])、§3.3 Remark 全段、§3.4/§3.4.1 节标题、切复形定义式 g=⊕g^k[−k]; g^k=Γ(X,Ω^{0,k}_X⊗T^{1,0}_X)（MD 行 319–364）。
- 结果：`FAIL`→2 处已修复：①行 353 `non-trivial component in degree 1` 印刷为 `degree −1`（300dpi 裁剪确凿，负号丢失，数学内容错误），已补 `−1`；②同 行 `$\mathbf{g}^{<0}=0 .$.` 双句点已删。其余 PASS±：行 353/357 `diferential`×3（ff 拍平）；行 325 `afine`。公式行 322/328/334/340/348/364 与印刷逐符号吻合。
- 备注：印刷 p.8 止于 ⊕ 公式（页码 8）；MD 行 367 起「with the diferential equal to ∂̄…」为印刷 p.9 内容，其中 `$\overline{\partial}.$forms` 疑似幻影句点、`X$eof` 杂散 e 在 p.009 处理。

## p.009（PDF p.9 / 印刷 p.9）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p009.png`（pngmono 150dpi）；仲裁裁剪 `audit/300dpi/Kontsevich_1997_deformation_quantization_p009_dbar_forms.png`、`..._p009_mA.png`、`..._p009_Atilde.png`（300dpi）
- 核对：p.8 跨页句（∂̄-forms、holomorphic vector fields）、形变函子段（X̃/Spec(m′)/fibert identification i）、§3.4.2 Hochschild complex：C^•(A,A) 定义式、g:=C^•(A,A)[1] 与 g=⊕g^k[−k]; g^k:=Hom(A^{⊗(k+1)},A)（k≥−1, g^{<(−1)}=0）、Hochschild 微分显式公式（三项和）、Gerstenhaber 括号式、∘ 积显式公式、余代数 F=⊕_{n≥1}⊗^n(A[1])、coderivation 段（m_A∈g¹、[m_A,m_A]=0、d=ad(m_A)）、Def_g(m)≅pairs(Ã,i) 段与 Ã⊗_{m′}k≃A 式（MD 行 367–411）。
- 结果：`FAIL`→6 处已修复：①行 367 `cup-product on$\overline{\partial}.$forms` 印刷为 `∂̄-forms`（300dpi 确证连字符），幻影句点改 `-forms`；②行 369 `≃X$eof the special fiber` 印刷为 `≃ X of`，删杂散 e；③行 397 `(non-associative) product is defined` 印刷为 `product ◦ is defined`（PNG+文本层确凿），补 `$\circ$`；④行 409 `element m$A\in{\bf g}^1$, m$\mathbf{\delta}_A:` 印刷为 `m_A∈g¹, m_A:`（下标错裂+幻影 δ，300dpi 确证），改 `$m_A\in{\bf g}^1$, $m_A:`；⑤行 411 `$\widetilde{A}$e eis free` 印刷为 `Ã is free`，删杂散 `e e`；⑥行 411 `$\overset{\triangledown}{\boldsymbol{A}}\otimes…\simeq\boldsymbol{A}$` 印刷重音为波浪号 Ã（300dpi 确证非 ∇），改 `$\widetilde{\boldsymbol{A}}\otimes_{\mathbf{m}^{\prime}}\mathbf{k}\simeq\boldsymbol{A}$`。print quirk 忠实保留：印刷本行 `Maurer- Cartan` 连字符后确有空格（300dpi 确证），MD 原样。其余 PASS±：`diferential`×5、`coeficients`（ff 拍平）；行 369 `$X$` 后缺句点、行 409 `=0$` 后缺句点与句末缺句点（标点遗漏登记）；`\widetilde`/`\tilde` 混用、m′-module 粗体拍平。公式行 376/382/388/394/400/406 与印刷逐符号吻合。
- 备注：行 413 起（HH^k=Ext…）为印刷 p.10 内容，属下一块 p.010 审计。

## p.010（PDF p.10 / 印刷 p.10）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p010.png`（pngmono 150dpi）
- 核对：HH^k(A,A)=Ext^k_{A-mod-A}(A,A) 式、§4/§4.1 节标题、余自由余代数 C(V)=⊕_{n≥1}(⊗^nV)^{Σ_n}⊂⊕_{n≥1}(⊗^nV) 式、(V_formal, base point) 定义式、C(V)^* 幂级数说明、formal pointed manifold Definition、coalgebra 同构段、f_*:C(V₁)⟶C(V₂) 与线性映射 C(V₁)⟶V₂、齐次分量 f^{(n)} 式、Taylor 系数 ∂^n f 定义式、Sym^n(V₁) 商空间式（MD 行 413–472）。
- 结果：`FAIL`→3 处独立斜体 `C` 被 MinerU 丢失，已补（PNG+文本层确凿）：①行 441 `a coalgebra which is isomorphic`→`a coalgebra$C$which is isomorphic`；②行 443 `between and$C(V)$`→`between$C$and$C(V)$`；③行 443 `primitive elements in coalgebra .`→`in coalgebra$C$.`。另修 1 处：行 463 `of$f .$.` 双句点已删。其余 PASS±：行 423 `diferential`、行 443 `afine`、行 463/475 `coeficients`（ff 拍平）；行 477 句末缺句点（登记）；行 466 偏导分式与下标 `|_{t₁=…=tₙ=0}` 位置逐符号吻合。
- 备注：印刷 p.10 止于 Sym^n 公式（页码 10）；MD 行 475 起（inverse mapping theorem）为印刷 p.11 内容，在 p.011 核对。

## p.011（PDF p.11 / 印刷 p.11）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p011.png`（pngmono 150dpi）
- 核对：inverse mapping theorem 段、§4.2/§4.3 节标题、pre-L∞-morphism Definition 与 𝓕:((g₁[1])_formal,0)⟶((g₂[1])_formal,0) 式、∂¹F/∂²F/∂³F 三行、Sym^n(g₁[1])≃(∧^n(g₁))[n]、F_{(k₁,…,kₙ)} 定义式与 symmetry property（含 (−1)^{k_i k_{i+1}} 与参数置换）、∂^nF(γ₁∧…∧γₙ)=F_{(k₁,…,kₙ)}(γ₁⊗…⊗γₙ)、Q-流形段（Q₁ 线性映射、Q₂:∧²g⟶g、[Q,Q]=0↔dgLa、[AKSZ]）（MD 行 475–533）。
- 结果：`FAIL`→3 处已修复（PNG 确凿）：①行 475 `is invertible if its first`→`iff its first`（印刷 iff，ff 连字吞失致词义改变）；②行 485 Definition `$A \ p r e - L _ { \infty } . _ {\mathit{morphism}} \mathcal{F}$from g to g`→`A pre-$L_\infty$-morphism$\mathcal{F}$from$\mathbf{g}_1$to$\mathbf{g}_2$`（幻影句点还原为连字符 + 补丢失的 g₁/g₂ 下标）；③行 529 `The second coeficien$Q^{2}:`→`coefficient$Q_{2}:`（丢 t + 印刷下标 Q₂ 错为上标 Q²，PNG 确证；与后文 "the bracket Q₂" 一致）。其余 PASS±：`coeficients`/`coeficient`/`diferential`×2（ff 拍平）；行 477 句末缺句点；行 481/527 标题 `L<sub>∞</sub>` HTML 残留（格式级）。公式行 488/494/498/502/505/508/514/520 与印刷逐符号吻合。
- 备注：行 533 为印刷 p.11 末段（页码 11）；MD 行 535 起属印刷 p.12，在 p.012 核对。

## p.012（PDF p.12 / 印刷 p.12）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p012.png`（pngmono 150dpi）
- 核对：L∞-algebra Definition（(g,Q)、Sugawara 别名 [HS2]）、Q₁/Q₂/Q₃ 三行、Q₂=0 二次约束段（dgLa↔Q₃=Q₄=…=0）、L∞-morphism Definition（𝓕_*:C(g₁[1])⟶C(g₂[1])）、dgLa 情形主方程（dFₙ−Σ±Fₙ=½Σ1/k!l!Σ_σ±[F_k,F_l]+Σ_{i<j}±F_{n−1}）、前两条显式式（dF₁、dF₂−(−1)^{γ̄₁}F₂=F₁[γ₁,γ₂]−[F₁γ₁,F₁γ₂]）、g=k[−1]⊗切空间段、MC 解转移公式 dγ+½[γ,γ]=0⟹dγ̃+½[γ̃,γ̃]=0, γ̃=Σ(1/n!)Fₙ(γ∧…∧γ)∈g₂¹⊗m（MD 行 535–580）。
- 结果：`FAIL`→10 处已修复（全部 PNG 确凿）：①行 551 `$Q^{2}=0$`→`$Q_{2}=0$`（下标错为上标）；②行 551 `$\mathbf{g}.$. 双句点；③行 551 `$L_{\infty}{-}\mathrm{a}$lgebra` 拆词→`$L_{\infty}$-algebra`；④/⑤行 555/559 `pre-$. L_{\infty}$` 幻影句点×2→`pre-$L_{\infty}$`；⑥行 559 `-morphism if it satisfies`→`iff`（ff 连字吞失，词义改变）；⑦行 559 `$n=1,2\dots$. and` 多余句点；⑧行 575 `$L_{\infty}\mathrm{-algebras.}$.` 句点重复→`$L_{\infty}$-algebras.`；⑨行 577 `from g<sub>1</sub> to g .`→`to g<sub>2</sub>.`（下标丢失）；⑩行 577 `$\gamma\in{\bf g}_1$m of`→`$\gamma\in{\bf g}_1\otimes\mathbf{m}$ of`（⊗ 丢失，PNG+文本层确凿）。其余 PASS±：`diferential`×5/`codiferentials`/`coeficients`（ff 拍平）；行 535 句末缺句点、行 551 `=0$` 后缺句点（登记）。公式行 544/548/562/568/572/580 与印刷逐符号吻合。
- 备注：行 583 起（formally on parameter ℏ）为印刷 p.13 内容，在 p.013 核对；行 583 已见 `$\hbar\mathrm{:}$:` 双冒号伪影，届时处理。

## p.013（PDF p.13 / 印刷 p.13）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p013.png`（pngmono 150dpi）
- 核对：ℏ 形式参数 MC 解转移式（γ(ℏ)=γ₁ℏ+γ₂ℏ²+…∈g₁¹[[ℏ]]⟹dγ̃(ℏ)+½[γ̃(ℏ),γ̃(ℏ)]=0）、Q-流形 zero 子概形段、§4.4 Quasi-isomorphisms（Q₁^{(g_i)} 复形态射、quasi-isomorphism Definition、Theorem：拟同构⟹存在逆 L∞-态射+形变函子同构、等价关系段、[GM][HS1][SS]）、§4.5/§4.5.1 节标题、minimal/linear contractible 两个 Definition、contractible iff 段、direct sum Lemma（MD 行 583–621）。
- 结果：`FAIL`→11 处已修复：①行 583 `parameter$\hbar\mathrm{:}$:` 双冒号→`$\hbar$:`；②行 589 `$\mathbf{g}[1]_{formal}$$L_{\infty}\mathrm{{-morphisms}}$map` 缺句号+空数学+直立体→`$…_{formal}$. $L_{\infty}$-morphisms map`；③行 589 同行 `that$L_{\infty}\mathrm{{-morphisms}}$induce`→`that$L_{\infty}$-morphisms induce`；④行 593 `L -morphisms generalize`→`$L_{\infty}$-morphisms`（印刷 L∞，∞ 丢失）；⑤行 599 `an$L_{\infty}.$-morphism` 杂散句点→删除；⑥行 599 `i = 1,2$Also,`→`i = 1,2$. Also,`（缺句号）；⑦行 613/⑧行 617/⑨行 621 `L_{\infty}{\mathrm{-}alg}\mathrm{e}bra(…) ` 拆词 mush×3→`$L_{\infty}$-algebra$(\mathbf{g},Q)$`（印刷 An L∞-algebra (g, Q)）；⑩行 619 `$Q{\mathrm{-manifold}}$contractible if`→`$Q$-manifold contractible iff`（ff 连字吞失致词义改变，PNG+文本层确凿）；⑪行 621 `ofa minimal and ofa` 缺空格×2+`alg\mathrm{e}bras` 拆词+句末缺句点→`of a minimal and of a linear contractible$L_{\infty}$-algebras.`。其余 PASS±：`diferential`×4/`coeficients`×2（ff 拍平）；行 599 末 `$L_{\infty}{\mathrm{-}}morphism~\mathcal{F}$` 直立连字符样式与 `associated with$\mathbf{g}_i$` 句末缺句点（登记）；行 609 标题 `\bf-algebras` 粗体样式（登记）。公式行 586 与印刷逐符号吻合。
- 备注：行 623 起（This lemma says…This affine）为印刷 p.13 末段跨页续行+印刷 p.14 内容，在 p.014 核对。

## p.014（PDF p.14 / 印刷 p.14）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p014.png`（pngmono 150dpi）
- 核对：Lemma 证明收尾（归纳构造、Q.E.D.）、奇点理论旁注（[AGV] 11.1、f=constant+Q₂(x)+Q_{≥3}(y)）、g/g^min 投影-包含两态射式、拟同构传递式、g₁^min⟶g₂^min 式、minimal 拟同构可逆段（含印刷原缺 of 的 "the set equivalence classes" print quirk 忠实保留）、§4.5.2 节标题、Maps(Spec(m⊕k·1)…)⊂Maps(…(M,0)) 式、余代数 C 同态段、gauge equivalent 定义与 dp(t)/dt=[Q,ξ(t)]_{|p(t)} 式、g¹⊗m⊗k[t] 段、Hom_{Graded^k} 公式（MD 行 623–671）。
- 结果：`FAIL`→6 处已修复（PNG/文本层确凿）：①行 627 `an$L_{\infty}.$-algebra` 杂散句点；②行 645 `$L_{\infty}{-}\mathrm{a}$lgebras` 拆词→`$L_{\infty}$-algebras`；③行 655 `the coalgebra  corresponding`→`the coalgebra$C$corresponding`（斜体 C 丢失，与 p.010 同类）；④行 655 `base point to$(M,0)$`→`base point ) to$(M,0)$`（闭括号丢失）；⑤行 657 `gauge equivalent if`→`iff`（ff 连字吞失）；⑥行 657 `of degree 1`→`of degree −1`（负号丢失，数学内容错误）。print quirk 忠实保留：行 645 印刷原文缺 "of"（"the set equivalence classes of L∞-algebras"），MD 原样。其余 PASS±：行 623 `afine`×2/`diferential`、行 649 `coeficients`（ff 拍平）；行 645/665 句末缺句点、行 645/665 直立体样式（登记）。公式行 630/636/642/652/660/668 与印刷逐符号吻合。
- 备注：行 671 句子跨页（"solutions of the"→p.15），在 p.015 核对。
