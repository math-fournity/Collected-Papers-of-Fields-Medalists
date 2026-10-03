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

## p.015（PDF p.15 / 印刷 p.15）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p015.png`（pngmono 150dpi）
- 核对：Def_M 函子对应段（行 673）、四条性质 1)–4)（3.2 等价、自然变换、直和→函子积、linear contractible→平凡）、"Properties 2)-4)…Q.E.D."、super Q-manifold 推广段、§4.6/§4.6.1 节标题、D_poly(X) 定义段与 Hochschild 余链公式、T_poly(X)=Γ(X,∧^{n+1}T_X)、Schouten-Nijenhuis 括号两条公式（含 (−1)^{i+j+k} 与 (−1)^i ξ_i(h)）、De Rham 分叉段（ψ_i 奇变量）、[γ₁,γ₂]=γ₁•γ₂−(−1)^{k₁k₂}γ•γ₁ 与 γ₁•γ₂ 定义式（MD 行 673–734）。
- 结果：`FAIL`→3 处已修复：①行 681 `$Def_{\mathbf{g}_1}\times Def_{\mathbf{g}_2}$，` 全角逗号 U+FF0C→ASCII `,`（杂散字符）；②行 683 `linear contractible L -algebra g`→`$L_{\infty}$-algebra`（∞ 丢失，本块第 2 处同型）；③行 699 `are functions in$(x_i)$`→`$(x^i).$`（印刷上标 x^i+句点，下标错为上标且缺句点）。print quirk 忠实保留：行 728 印刷第二项确为 `γ•γ₁`（无下标 2，应为 γ₂，原文如此）；行 731 `where introduce the following notation:`（原文缺 we）。其余 PASS±：`diferential`×5/`polydiferential`/`coeficients`（ff 拍平，含 §4.6.1 标题）。公式行 696/704/710/714/718/722/734 与印刷逐符号吻合。
- 备注：行 737 起（evident map U₁^{(0)}）为印刷 p.16 内容，在 p.016 核对。

## p.016（PDF p.16 / 印刷 p.16）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p016.png`（pngmono 150dpi）
- 核对：U₁^{(0)}:T_poly(X)⟶D_poly(X) 定义式（Hochschild-Kostant-Rosenberg 型 symmetrization 求和 + h↦(1↦h)）、§4.6.1.1/Theorem（U₁^{(0)} 是复形态射拟同构）、KHR 定理段（⊕_{k≥0}Γ(X,∧^kT_Y)[−k]）、 filtration 论证段与 Gr(U₁^{(0)}):Gr(T_poly)⟶Gr(D_poly) 式、principal symbols 段（Sym(T)⊗…⊗Sym(T)）、𝒞:=C(T)⊕(k·1)* 式、f↦(D(f))(0) 式、coproduct Δ 与纤维微分 d:⊗^{n+1}𝒞⟶⊗^{n+2}𝒞 完整公式（MD 行 737–783）。
- 结果：`FAIL`→2 处已修复：①行 747 `on$Y .$. Analogous` 双句点→`on$Y$.`；②行 777 `coalgebra$\mathcal{C} .$. It` 双句点→`$\mathcal{C}$.`。print quirk 忠实保留：行 765 印刷原文 "It better to identify"（缺 is，原文如此）。其余 PASS±：行 747 `afine`、行 749/751/757/759/771/777 `diferential`/`polydiferential`/`coeficients`（ff 拍平）；行 757 `$A=C^{\infty}(X)$` 后缺句点（登记）。公式行 740/754/762/768/774/780 与印刷逐符号吻合。
- 备注：行 785 起（Lemma. Let be the cofree…）为印刷 p.17 内容，在 p.017 核对。

## p.017（PDF p.17 / 印刷 p.17）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p017.png`（pngmono 150dpi）
- 核对：Lemma（∧^{n+1}T, d=0 ⟶ (⊗^{n+1}𝒞, d as above) 拟同构）、Proof 段（Euler 向量场分解、completed complex、H̄om(A^{⊗(n+1)},k)、Ext^{n+1}_{A-mod}(k,k)=∧^{n+1}T、resolution …⟶A⊗A⟶A⟶0⟶…）、𝒞↦C(T) reduced cochains 旁注、gr(U₁^{(0)}) fiberwise 收尾、§4.6.2 Main theorem（U₁≠bracket 兼容、Theorem U₁=U₁^{(0)}、[Su] formality 命名、MC 解=Poisson 结构 α∈T¹_poly 式、γ(ℏ):=α·ℏ 式、difeomorphism 共轭作用、corollary 1.3 定理回指）（MD 行 785–831）。
- 结果：`FAIL`→6 处已修复：①行 785 `Lemma. Let be the cofree`→`Let$\mathcal{C}$be`（斜体 𝒞 丢失，PNG+文本层确凿）；②行 795 `is true if the analogous`→`iff`（ff 连字吞失）；③行 795 `A^{\diamondsuit(n+1)}`→`A^{\otimes(n+1)}`（◇ 符号错写，印刷为 ⊗，PNG+文本层确凿）；④行 803 `one replaces by$C(T)$`→`one replaces$\mathcal{C}$by$C(T)$`（𝒞 丢失）；⑤行 815 `The quasi-isomorphism in the theorem`→`The quasi-isomorphism$\mathcal{U}$in the theorem`（U 丢失）；⑥行 823 `depending on$\hbar ,$,` 双逗号→`$\hbar$,`。print quirk 忠实保留：行 831 印刷原文 `L∞-morphim`（morphism 拼错缺 s，PNG 确证），MD `\mathrm{-morphim}` 原样；行 811 句末缺句点（登记）。其余 PASS±：`difeomorphism`/`diferential`×3（ff 拍平）；行 829 `¯h` 分解。公式行 788/798/820/826 与印刷逐符号吻合。
- 备注：行 833 起（§4.6.3 Non-uniqueness）为印刷 p.18 内容，在 p.018 核对。

## p.018（PDF p.18 / 印刷 p.18）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p018.png`（pngmono 150dpi）；仲裁裁剪 `audit/300dpi/Kontsevich_1997_deformation_quantization_p018_U.png`、`..._p018_Lmorphism.png`（300dpi）
- 核对：§4.6.3 Non-uniqueness（异型拟同构、homotopy 定义、R^× 缩放自同构与 const^k、[Ko2] exotic L∞-自同构、演化方程 ∂³α^{ij}/∂x^k∂x^l∂x^m·∂α^{kk'}/∂x^{l'}·∂α^{ll'}/∂x^{m'}·∂α^{mm'}/∂x^{k'}(∂_i∧∂_j)、aff(1,R) 作用、cup-product 回指 section 8）、§5/§5.1 节标题、Conf_{n,m} 定义式、G^{(1)} 群与 G^{(1)}={z↦az+b|a,b∈R,a>0} 式、C_{n,m}:=Conf_{n,m}/G^{(1)} 段、Conf_n/C_n 两式（MD 行 833–874）。
- 结果：`FAIL`→5 处已修复（花体 𝒰/∞ 丢失，PNG/300dpi 确凿）：①行 835 `quasi-isomorphism$u ,$i.e.`→`$\mathcal{U}$, i.e.`（小写 u 错写+逗号粘连）；②行 835 `in a natural sense to .`→`to$\mathcal{U}$.`（𝒰 丢失）；③行 837 `Composing these automorphisms with  one get`→`with$\mathcal{U}$ one get`（𝒰 丢失，300dpi 确证）；④行 847 `why our quasi-isomorphism is better`→`quasi-isomorphism$\mathcal{U}$is better` 与 `is that only (up to homotopy) preserves`→`only$\mathcal{U}$(up to homotopy)`（𝒰 丢失×2）；⑤行 859 `and the point , acts on`→`and the point$\infty$, acts on`（∞ 丢失，与 p.006 同型）。print quirk 忠实保留：行 835 `Mimicking constructions and definitions form 4.5.2`（原文 form 误于 from，300dpi 确证）；行 835 `on the set of L-morphisms`（印刷无 ∞，300dpi 确证）；行 837 `one get`（原文如此）。其余 PASS±：`difer`/`difeomorphism`/`afine`（ff 拍平）；行 845 `realanalytic` 行连字丢 `-`；行 843/856/865 句末缺句点；行 847 `${\bf{}}aff(1,{\bf{R}})$` 空 `\bf{}` 组（登记）。公式行 840/856/862/870/874 与印刷逐符号吻合。
- 备注：行 877 起（where$G^{(2)}$is a 3-dimensional Lie group）为印刷 p.19 内容，属下一块 p.019 审计。

## p.019（PDF p.19 / 印刷 p.19）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p019.png`（pngmono 150dpi）
- 核对：G^{(2)}={z↦az+b|a∈R,b∈C,a>0} 式、C̄_{n,m}/C̄_n 紧化引言、manifold with corners 段（(R_{≥0})^d、[0,1]^d）、angle 集合 (Arg(p_i−p_j),Arg(p_i−p̄_j),Arg(p_i−q_j)) 式、torus 嵌入段、open strata 段、Σ_n/Σ_n×Σ_m 作用与 C_A/C_{A,B} 纤维化段、§5.2 节标题、[FM] 引用段、H∪R⊂C 显微镜段、standard position 定义 1)–2)（diameter=1、center=0）、s^cont 截面段、stable configuration 段、oriented tree T 引言（MD 行 877–917）。
- 结果：`FAIL`→5 处已修复：①行 887 `$n\geq 1$ With`→`$n\geq 1$. With`（缺句点，PNG 确凿）；②行 893 `The space$\overline{{C}}_{r}$,m is defined`→`$\overline{{C}}_{n,m}$ is defined`（下标错写 r, 应为 n,m，PNG 确凿）；③行 897 `$C_n .$,` 双句点→`$C_n$,`；④行 905 `$\mathbf{R}^2\simeq\mathbf{C}.$, i.e.` 双句点→`$\mathbf{C}$, i.e.`；⑤行 905 `standard position if`→`iff`（印刷 iff，PNG+文本层确凿，ff 吞失）。print quirk 忠实保留：行 915 `(i.e.the number`（印刷粘排缺空格）；行 883 `( and`（印刷空格原貌）。其余 PASS±：行 885 `diference`、行 903 `diferent`（ff 拍平）；行 903 Euclidean 斜体拍平；行 909/911/897 句末缺句点（登记）。公式行 880/890/883 与印刷逐符号吻合。
- 备注：行 919 起（$^2\bullet…$ 配置图、tree、Star(v)、a)/b) 数据）为印刷 p.20 内容，在 p.020 核对；行 931 全角逗号为上块移交线索，届时处理。

## p.020（PDF p.20 / 印刷 p.20）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p020.png`（pngmono 150dpi）
- 核对：6 点配置图与 tree 图（行 919–925，树图引 `images/page_19_image_2.jpg` 文件存在）、Star(v) 定义段、a)/b) 参数化数据、(z↦s_v z+p_v)∈G^{(2)}、s_v 缩放与 C̄_n 紧化段、strata C_T 与 ⊔_{trees T}∏_{v∈V_T\{leaves}}C_{Star(v)} 式、s^smooth 截面段、H∪R 情形过渡句（MD 行 919–947）。
- 结果：`FAIL`→4 处已修复：①行 931 `$Star(v)$，` 全角逗号 U+FF0C→ASCII `,`（上块移交线索落实）；②行 945 `$v \in V_T \mathrm{~}\backslash$leaves`→`$v \in V_T \backslash \{\text{leaves}\}$`（集合差记号括号丢失，PNG 确凿）；③行 947 `points on   R is not much harder`→`points on$\mathcal{H}\cup\mathbf{R}$ is not much harder`（𝓗∪ 丢失，PNG+文本层确凿）；④行 947 `standard position if`→`iff`（印刷 iff，PNG+文本层确凿）。`FAIL` 另登记 1 项不可修复：行 919–921 6 点配置图被 MinerU 损毁为 `$^2\bullet\quad^3_4$` 数学残片且 images/ 无源图（仅 page_19_equation_* 与 page_19_image_2），图内容以 PDF p.20 原图为准，不虚构重建。其余 PASS±：行 933/935/945 句末缺句点（登记）。公式行 942 与印刷逐符号吻合。
- 备注：行 949 起（standard position 条件 1)/2)）为印刷 p.21 内容，在 p.021 核对。

## p.021（PDF p.21 / 印刷 p.21）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p021.png`（pngmono 150dpi）
- 核对：standard position 条件 1)/2)（convex hull 投影、{0}、diameter=1）、stable case 唯一放置段（G^{(1)}）、两类放大域段、C̄_{n'} 归约段、低维空间 C_{1,0}/C_{0,2}/C_{1,1} 段、半圆图（行 961 引 page_20_image_6.jpg 存在）、C_{2,0}≃𝓗\{0+1·i} 段与 i=√−1、C̄_{2,0} 两图（行 965/969 引 page_20_image_8/10.jpg 存在）、The Eye 图题、forgetting maps 段（MD 行 949–973）。
- 结果：`FAIL`→6 处已修复（PNG/文本层确凿）：①行 949 `one-point set 0 ,`→`one-point set$\{0\}$,`（花括号丢失）；②行 953 `n points on and m points on R`→补 `$\mathcal{H}$`（𝓗 丢失）；③行 953 `$G^{\breve{(1)}}$`→`$G^{(1)}$`（幻影 \breve 重音，印刷为干净 G^{(1)}）；④行 955 `a point on comes too close to R`→补 `$\mathcal{H}$`；⑤行 955 `on  or on R.`→`on$\mathcal{H}$ or on R.`（𝓗 丢失）；⑥行 963 `$\in{\mathcal{H}}.$.` 双句点已删。其余 PASS±：行 957 `$\mathcal{H},$` 逗号入式、行 953/957 句末缺句点（登记）；行 963 `difeomorphic`（ff 拍平）。图文对应逐项吻合（三张 Eye 系列图与印刷三图对应）。
- 备注：行 975 起（§5.2.1 Boundary strata、S1)/S2) 层）为印刷 p.22 内容，在 p.022 核对。

## p.022（PDF p.22 / 印刷 p.22）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p022.png`（pngmono 150dpi）；仲裁裁剪 `audit/300dpi/Kontsevich_1997_deformation_quantization_p022_starting_from_s.png`（300dpi）
- 核对：§5.2.1 S1)/S2) 余维 1 层清单（#S≥2、2#S+#S′≥2、#S+#S′≤#A+#B−1）、∂_S C̄_{A,B}≃C_S×C_{(A\\S)⊔{pt},B} 与 ∂_{S,S'} 两式、§6/§6.1 节标题、admissible graph Definition 1)–4)（顶点 {1..n}⊔{1̄..m̄}、2n+2−m≥0、无环、Star(k) 标号 e¹_k…e^{#Star(k)}_k）、§2 图=_identifications L=1̄,R=2̄ 段、§6.2 节标题、Eye 同伦 S¹ 段、angle map Definition、φ([(x,y)]) 记号段、φ^h 段、weight 引言（MD 行 975–1027）。
- 结果：`FAIL`→3 处已修复：①行 989 `of points in . Analogously`→`of points in$\mathcal{H}$. Analogously`（𝓗 丢失，PNG+文本层确凿）；②行 1001 `$\mathbf{Z}_{>0}$`→`$\mathbf{Z}_{\geq 0}$`：印刷为 Z_{≥0}（PNG+文本层确凿，数学内容错误——定义允许 m=0）；③行 1023 `$\phi([(x,y)])$) simply` 幻影闭括号已删。print quirk 忠实保留：行 1013 `starting from$s ,$`（300dpi 确证印刷原文为 s，语义应为 k，原文如此）；行 1001 `{1̄,…,m̄}` 带杠记号原样。其余 PASS±：行 1017 §6.2 标题 `Diferential`（ff 拍平）；行 981/1003/1021 句末缺逗号/句点；行 1021 `of the$Eye,$` 逗号入式（登记）。公式行 986/992/1010 与印刷逐符号吻合。
- 备注：行 1029 起（W_Γ weight 公式）为印刷 p.23 内容，在 p.023 核对。

## p.023（PDF p.23 / 印刷 p.23）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p023.png`（pngmono 150dpi）
- 核对：W_Γ weight 公式（∏1/(#Star(k))!·1/(2π)^{2n+m−2}∫_{C̄⁺_{n,m}}⋀_{e∈E_G}dφ_e，E_G 下标为印刷原貌）、C̄⁺_{n,m} 增序定向段（q₁<…<q_m）、Conf_{n,m} 定向段、forgetting map/φ_e 拉回段、wedge 序段、积分良定义段、§6.3 节标题、U_Γ 线性映射段（⊗^n T_poly⟶D_poly[1+l−n]、k_i=#Star(i)−1、anti-symmetrization）、Φ 定义式、Σ_{I:E_Γ→{1..d}}Φ_I 式、ψ_i=⟨γ_i,dx^{I(e_i^1)}⊗…⟩ 式、polyvector↔skew-tensor 标识式、ψ_j̄=f_j 段、顶点偏导 ∏∂_{I(e)}ψ_v 式（MD 行 1029–1082）。
- 结果：`FAIL`→6 处已修复：①行 1039 `on complex manifold . Thus,`→`on complex manifold$\mathcal{H}$. Thus,`（𝓗 丢失，PNG+文本层确凿）；②行 1047 §6.3 标题 `Pre-$L_{\infty}.$-morphisms` 杂散句点已删；③行 1049 `a linear map$I_{\Gamma}:`→`$\mathcal{U}_{\Gamma}:`（字母错写 I，印刷/文本层均为花体 U_Γ）；④行 1049 `$l\in\mathbf{Z}.$,` 双句点已删；⑤行 1049 `i = 1,\dots,n.$.` 双句点已删；⑥行 1049 `then from <sub>Γ</sub> after`→`then from$\mathcal{U}_{\Gamma}$ after`（𝒰_Γ 丢失）。print quirk 忠实保留：行 1030 ⋀ 下标 `E_G`（印刷原貌，全篇他处为 E_Γ）；行 1063 印刷 `functions$g_j$`（通篇函数记号为 f_j，原文如此）；行 1030 `∫` 下标 C̄⁺_{n,m} 原样。其余 PASS±：行 1045 `diferential`、行 1063/1065 `coeficients`（ff 拍平）；行 1039/1041 句末缺句点；行 1057 逗号入式（登记）。公式行 1030/1036/1054/1060/1068/1074/1082 与印刷逐符号吻合。
- 备注：行 1085 起（and then take the product…）为印刷 p.24 内容，在 p.024 核对。

## p.024（PDF p.24 / 印刷 p.24）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p024.png`（pngmono 150dpi）
- 核对：Φ_I 收尾、affine 不变性段、§6.4 节标题、𝒰 定义句（𝒰:T_poly(R^d)⟶D_poly(R^d)、𝒰_n, n≥1）、𝒰_n=Σ_{m≥0}Σ_{Γ∈G_{n,m}}W_Γ×𝒰_Γ 式、G_{n,m} 说明、Theorem（𝒰 是 L∞-态射且拟同构）、Proof（skew-symmetric、6.5 引）、L∞-morhism 显式条件两大式（f₁·𝒰_n 项、Σ_{i=1}^{m−1}(f_i f_{i+1}) 项、Σ_{i≠j}[γ_i,γ_j] 项、½Σ 1/k!l![𝒰_k,𝒰_l] 项）、𝒰₀/m_A 段（mA:f₁⊗f₂↦f₁f₂）、第二条件两式（γ_i•γ_j、∘ 复合）、(F) 记号段、𝒰+𝒰₀ Q-equivariant 段、Γ₀ 唯一图段（MD 行 1085–1129）。
- 结果：`FAIL`→11 处已修复（PNG/文本层确凿）：①行 1091 `-morphism :$T_{poly}`→补 `$\mathcal{U}$`（𝒰 丢失）；②行 1099 `Theorem. is an$L_{\infty}–morphism,$$,`（𝒰 丢失+数学mush）→`Theorem.$\mathcal{U}$is an$L_{\infty}$-morphism,`；③行 1101 `i.e. that is a pre-`→补 `$\mathcal{U}$`；④行 1103 `The condition that is an`→补 `$\mathcal{U}$`；⑤行 1113 `homogeneous components of  (see 4.1)`→补 `$\mathcal{U}$`；⑥行 1115 `for  to be an`→补 `$\mathcal{U}$`；⑦行 1125 `via operations  (see 3.4.2) and  (see 4.6.1)`→补 `$\circ$`/`$\bullet$`（两运算符号丢失）；⑧行 1127 `pre-$L_{\infty}.$-morphism` 杂散句点；⑨行 1127 `$T_{poly}(\mathbf{R}^d)[1])_{formal}$` 多余 `)`（印刷 [1]_{formal}）；⑩行 1129 `definition of . Namely,`→补 `$\mathcal{U}$`；⑪同句 `second$\mathrm{type}$` 直立体保留。print quirk 忠实保留：行 1103 `-morhism`（原文拼写缺 p，PNG 确证）。其余 PASS±：行 1087 `afine`、行 1113/1127 `bidiferential`/`diferential`（ff 拍平）；行 1085/1097/1113 附近句末缺句点（登记）。公式行 1094/1106/1110/1118/1122 与印刷逐符号吻合。
- 备注：行 1131 起（We consider the expression (F)…）为印刷 p.25 内容，在 p.025 核对。

## p.025（PDF p.25 / 印刷 p.25）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p025.png`（pngmono 150dpi）
- 核对：(F) 线性组合段与 Σ_Γ c_Γ·𝒰_Γ(γ₁⊗…⊗γₙ))(f₁⊗…⊗f_m) 式（印刷括号本身不配对 `))(f`，MD 忠实保留）、2n+m−3 边条件段（c_Γ=±c_{Γ′}、relabeling）、Coeficients 段（𝒲_{Γ′} 权、operads 段）、c_Γ vanishes 段、Stokes 公式 ∫_{∂C̄}⋀dφ_e=∫_{C̄}d(⋀dφ_e)=0 式、boundary strata 分解 0=Σ_S∫_{∂_S}+Σ_{S,S'}∫_{∂_{S,S'}} 式、§6.4.1 Case S1（n₂=#S、n₁=n−n₂+1、2n₂−3 边数条件）、§6.4.1.1 n₂=2 子情形（𝒰 收缩、• 运算）（MD 行 1131–1163）。
- 结果：`FAIL`→5 处已修复：①行 1137 `$c_{\Gamma'}$′ if` 幻影 ′ 已删（印刷 prime 在下标内）；②行 1139 `numbers c do not depend`→`numbers$c_{\Gamma}$ do not depend`（下标 Γ 丢失，PNG+文本层确凿）；③行 1157 `$\#S \geq 2 .$,` 双句点→`$\#S \geq 2$,`；④行 1163 `gives number 1`→`gives number$\pm 1$`（± 丢失，PNG 确凿）；⑤行 1163 `the operation on polyvector fields`→`the operation$\bullet$ on polyvector fields`（• 丢失，PNG+文本层确凿）。print quirk 忠实保留：行 1134 公式 `𝒰_Γ(γ₁⊗…⊗γₙ))(f₁⊗…)` 印刷括号本身不配对；行 1163 `coming from the of the formula`（原文重复 the of the）；行 1163 `$e .$` 句点入式。其余 PASS±：行 1139 `Coeficients`、行 1143 `diferential`（ff 拍平）。公式行 1146/1152 与印刷逐符号吻合。
- 备注：行 1165 起（图 page_25_image_0.jpg、§6.4.1.2 n₂≥3）为印刷 p.26 内容，在 p.026 核对。

## p.026（PDF p.26 / 印刷 p.26）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p026.png`（pngmono 150dpi）
- 核对：收缩图 e 与直线图（行 1165 引 page_25_image_0.jpg 存在）、§6.4.1.2 n₂≥3 heading、2n₂−3 angle forms 消没段（"corresponding to the corresponding" 为印刷原句忠实保留）、第二张图（行 1171 引 page_25_image_3.jpg 存在）、§6.4.2 Case S2（j̄∈S₂⊂{1̄,…,m̄}、2n₂+m₂−2≥0、n₂+m₂≤n+m−1、C_{n₁,m₁}×C_{n₂,m₂}）、§6.4.2.1 no bad edges、W_{Γ₁}×W_{Γ₂} 段（MD 行 1165–1181）。
- 结果：`FAIL`→1 处已修复：行 1181 `where the product  on polydiferential operators appears`→补 `$\circ$`（印刷为 product ◦，PNG+文本层确凿）。其余 PASS±：行 1175/1179 句末缺句点（登记）；行 1181 `polydiferential`（ff 拍平）。行 1183 图 page_26_image_0.jpg 属印刷 p.27 版式（p.26 印刷止于 ◦ 句+页码 26），归 p.027 核对。
- 备注：行 1185 起（§6.4.2.2 bad edge）为印刷 p.27 内容，在 p.027 核对。

## p.027（PDF p.27 / 印刷 p.27）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p027.png`（pngmono 150dpi）
- 核对：p.26 末无 bad edge 收缩图（行 1183 引 page_26_image_0.jpg，与印刷 p.27 顶部图对应）、§6.4.2.2 bad edge heading、dφ(x,y)=0 消没段、bad edge 图（行 1189 引 page_26_image_3.jpg 存在）、multiple edges/ingore 段、c_Γ=0 收尾段、§6.4.3 heading、𝒰₁=𝒰₁^{(0)} 检查段、n=1 树图（行 1199 引 page_26_image_8.jpg 存在，p₁→q₁…q_m）（MD 行 1183–1199）。
- 结果：`FAIL`→2 处已修复：①行 1193 `and that  is an$L_{\infty}.$-morphism.`→`and that$\mathcal{U}$ is an$L_{\infty}$-morphism.`（𝒰 丢失+杂散句点，PNG+文本层确凿）；②行 1197 `check that it is a quasi-isomorphism`→`check that$\mathcal{U}$ it is a quasi-isomorphism`（𝒰 丢失；印刷原文冗余 "𝒰 it is" 忠实保留）。print quirk 忠实保留：行 1191 `we ingore them`（原文拼写）；`diferential form`（ff 拍平）。
- 备注：行 1201 起（(2π)^m/m!、ξ₁∧…∧ξ_m 映射式、Theorem is proven. Q.E.D.、§6.4.4）为印刷 p.28 内容，属下一块 p.028 审计。

## p.028（PDF p.28 / 印刷 p.28）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p028.png`（pngmono 150dpi）；仲裁裁剪 `audit/300dpi/Kontsevich_1997_deformation_quantization_p028_is_final_formula.png`、`..._p028_put_quotes.png`（300dpi）
- 核对：(2π)^m/m! 与 Ũ_Γ 映射式（sgn(σ)·ξ_{σ₁}⊗…）、Theorem is proven. Q.E.D.、§6.4.4 Comparison 段（w_Γ 与 W_Γ 差 2^n/n! 因子、B_{Γ,α}=2^{−n}𝒰_Γ(α∧…∧α)）、§6.5 节标题、(E) 分次空间映射式（Sym^n((⊕Γ(∧^kT)[−k])[2])⟶(Hom(A[1]^{⊗m},A[1]))[1]）、shift 记账段、三重符号来源 1)–3)、skew-symmetric 推断、inverse factorials 段、Stokes 无丢号讨论段与 Φ 表达式、§6.6 heading 与 C_n/G^{(2)} 段（MD 行 1201–1245）。
- 结果：`FAIL`→7 处已修复：①行 1215 `Homogeneous components of  are maps`→补 `$\mathcal{U}$`（𝒰 丢失）；②行 1221 `In our formula for the same`→补 `$\mathcal{U}$`；③行 1221 `$\bar{G}^{(1)}$`→`$G^{(1)}$`（幻影杠，PNG 确证无 bar）；④行 1221 `our formula for is compatible`→补 `$\mathcal{U}$`；⑤行 1225 `1) the orientation of$\overline{{C}}_{n,m} .$7`→`…_{n,m}$,`（幻影 7+印刷为逗号，PNG 确凿）；⑥行 1235 `the fact that is an`→补 `$\mathcal{U}$`；⑦行 1235 `$\mathrm{\Delta^{66}\ put^{,93}}$` 引号损毁→`"put"`（300dpi `_p028_put_quotes.png` 确证正规引号）。print quirk 忠实保留：行 1233 `1/n! is the final formula does not appear`（300dpi `_p028_is_final_formula.png` 确证印刷为 is 非 in，原文笔误）；行 1211 印刷 `differ`（MD `difer` 为 ff 拍平伪影，登记不改）。其余 PASS±：行 1211 `bidiferential`、行 1235 `loose`（原文如此）/`diferential` 拍平；行 1227 列表尾缺逗号、行 1245 句末缺句点、行 1235 bold C 拍平（登记）。公式行 1204/1218/1238 与印刷逐符号吻合。
- 备注：行 1247 起（Lemma. Let n≥3…）为印刷 p.29 内容，在 p.029 核对。

## p.029（PDF p.29 / 印刷 p.29）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p029.png`（pngmono 150dpi）
- 核对：Lemma（2n−3=dim(C_n) 个闭 1-form 积分为零）、Proof（C_n↪C_n'、p_{i₁}=0、p_{j₁}∈S¹、wedge 分解式、C_n'' 旋转归一、±2π 关系式）、∫_{C_n''}∏dArg(Z_α) 式、§6.6.1 heading、Theorem（dim N≥1、Z₁…Z_{2N} 有理函数、Zariski 开集、∫_{U(C)}⋀d(Arg Z_α) 绝对收敛且为零）、Goncharov 段、dLog|Z_α| trick、(1/2i)(d(Log Z_α)−d(Log Z̄_α)) 式、holomorphic/anti-holomorphic 分解段与 ⋀(1/2)(d+d) 式、Ū 正规交叉紧化段（MD 行 1247–1291）。
- 结果：`FAIL`→2 处已修复：①行 1255 `is equal to 2π times`→`is equal to$\pm 2\pi$ times`（± 丢失，PNG+文本层确凿，与 p.025 ±1 同类）；②行 1267 `non-vanishing on$U_i$and`→`on$U$, and`（幻影下标 i，印刷为 U,，PNG 确凿）。print quirk 忠实保留：行 1279 `of a holomorphic an anti-holomorphic form`（原文 an 误于 and）；行 1267 `ofdimension`/`ofX` 粘排。其余 PASS±：行 1263 `diferences`、行 1277/1279/1291 `diferential`/`diference`/`coeficients`（ff 拍平）；行 1267 粘排空格；行 1277 `\Lambda` 代 ⋀ 样式（登记）。公式行 1252/1260/1270/1282/1288 与印刷逐符号吻合。
- 备注：行 1293 起（Lemma. Let$\omega$…）为印刷 p.30 内容，在 p.030 核对。

## p.030（PDF p.30 / 印刷 p.30）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p030.png`（pngmono 150dpi）
- 核对：𝓘(ω) Lemma（L^1 系数、𝓘(dω)=d(𝓘(ω))、∫ 对应关系）、elementary exercise 段、Stokes 四重链式 ∫𝒰(C)⋀dArg=…=∫_{Ū(C)}d(𝓘(...))=0. Q.E.D. 式、§6.6.2 Remark（Chern-Simons 维 3、≥4、involution）、§7 heading、R^d_formal 形式完备段、W_d:=Vect 段、m_T/m_D 两态射式、P1)–P4) 性质与 𝒰₁(m_T(ξ))=m_D(𝒰₁(ξ))、𝒰_k(m_T⊗…⊗m_T)=0 两式（MD 行 1293–1340）。
- 结果：`FAIL`→3 处已修复（PNG+文本层确凿）：①行 1325 `properties of the quasi-isomorphism from 6.4`→补 `$\mathcal{U}$`；②行 1327 `P1) can be defined for`→`P1)$\mathcal{U}$ can be defined for`；③行 1335 `P3)  is$GL(d,\mathbf{R})$-equivariant`→`P3)$\mathcal{U}$ is…`（三处 𝒰 丢失）。其余 PASS±：行 1317 `diferential`×3（ff 拍平）；行 1293–1298 印刷中 ∫_{Ū(C)}𝓘(ω) 显示式在 MD 中后置（版式重排登记）；行 1317 `$T_{poly}(...)$` 后缺句点；行 1341 印刷页末逗号（P4 式后）MD 无对应（p.31 续行核对）。print quirk 忠实保留：行 1315 `that that`（原文重复）。公式行 1298/1306/1320/1332/1340 与印刷逐符号吻合。
- 备注：行 1343 起（P5) for any k≥2, ξ∈gl(d,R)…）为印刷 p.31 内容，在 p.031 核对；P5 行已见 η 下标疑似重复，届时仲裁。

## p.031（PDF p.31 / 印刷 p.31）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p031.png`（pngmono 150dpi）；仲裁裁剪 `audit/300dpi/Kontsevich_1997_deformation_quantization_p031_P5_eta.png`（300dpi）
- 核对：P5) 性质与 𝒰_k(m_T(ξ)⊗η₂⊗…⊗η_k)=0 式、P1-P4 使用段、𝒯/𝒟/𝒲 三 Q-流形段、§7.1 formal geometry heading（Gelfand-Kazhdan、X^coor/X^aff、G_d 主丛、Lie(G_d) 余维 d、se [GK]）、§7.2 heading、ΠTM Q-流形段（T[1]M）、flat connection ∇ 提升段与 [Q_E,Q_E]=0（MD 行 1343–1381）。
- 结果：`FAIL`→6 处已修复：①行 1343 P5 的 η 列表 `$\eta_2,\mathbf{\eta}_2,\mathbf{\eta}_3,\mathbf{\eta}_4,\eta_k$`→`$\eta_2,\ldots,\eta_k$`（garbled 重复，300dpi `_p031_P5_eta.png` 确证印刷为 η₂,…,η_k）；②行 1349 `of the map . Properties`→补 `$\mathcal{U}$`（𝒰 丢失，PNG+文本层确凿）；③行 1351 `d$\mathbf{\Xi}\in\mathbf{N}$` 幻影 Ξ 已删（印刷 d∈N）；④行 1369 `$X^{coor}\longrightarrow\dot{X}$` 幻影点已删（印刷 X）；⑤行 1381 `flat connection . Denote`→补 `$\nabla$`；⑥行 1381 `The connection gives a lift`→补 `$\nabla$`（∇ 丢失×2，PNG+文本层确凿）。print quirk 忠实保留：行 1359 `which will used in 7.3`（原文缺 be）；行 1375 `(se [GK])`（原文拼写）。其余 PASS±：行 1357/1359/1369/1371/1373/1375/1379 `diferential`/`difeomorphisms`/`afine`/`Diferential`/`diference`（ff 拍平）；行 1373 `infinitedimensional` 行连字丢-；行 1359/1373 句末缺句点（登记）。公式行 1347 残缺显示式（P4 式收尾逗号在 p.30 页末，MD 空显示式）登记为版式伪影。公式行 1354/1366 与印刷逐符号吻合。
- 备注：行 1383 起（Q-equivariant bundle、superconnection [Q]）为印刷 p.32 内容，在 p.032 核对。

## p.032（PDF p.32 / 印刷 p.32）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p032.png`（pngmono 150dpi）
- 核对：Q-equivariant bundle 段（Quillen superconnection [Q]）、flat family Definition、{point} 段、apologize 段、[Ko3] 段、§7.3/§7.3.1 headings、𝒯×𝒲⟶𝒲 与 𝒟×𝒲⟶𝒲 两平凡丛式、σ_𝒯/σ_𝒟 截面段（m_T/m_D 同态）、𝒰:𝒯⟶𝒟、Lemma（𝒰×id_𝒲 是 flat families 态射）、Proof 与 (𝒰×id_𝒲)∘σ_𝒯=σ_𝒟∈Maps(𝒲,𝒟×𝒲) 式、Taylor 系数比较段（P2/P4、T⁰(R^d)=Γ(R^d,T)）、§7.3.1.1 heading、2k+m−2=k 式（MD 行 1383–1432）。
- 结果：`FAIL`→6 处已修复（PNG/文本层确凿）：①行 1399 §7.3.1 标题 `Flat families over`→补 `$\mathcal{W}$`（𝒲 丢失）；②行 1401 `The first bundle over  is trivial`→补 `$\mathcal{W}$`；③行 1417 `flat families over .`→补 `$\mathcal{W}$`；④行 1419 `$id\mathcal{w}$`（小写 w 错排）→`$id_{\mathcal{W}}$`；⑤行 1425 `part$\mathcal{U}_1$of maps`→补 `$\mathcal{U}$`（𝒰 丢失）；⑥行 1425 `$T^0(\dot{\mathbf{R}}^d)$` 幻影点已删（印刷 T⁰(R^d)）。print quirk 忠实保留：行 1383 `introduced Quillen`（原文缺 by）；行 1387 `the same a formal`（原文缺 as）；行 1435 `intersting`（原文拼写）。其余 PASS±：行 1407/1413/1415/1435 句末缺句点；行 1422 `\sigma_D` 正体 vs 印刷 σ_𝒟 花体（样式登记）；行 1425 `coeficients`/`diferential`（ff 拍平）。公式行 1404/1410/1422/1432 与印刷逐符号吻合。
- 备注：行 1437 起（𝒰₂ 二次映射 ξ↦Σ∂_i(ξ^j)∂_j(ξ^i)）为印刷 p.33 内容，在 p.033 核对。

## p.033（PDF p.33 / 印刷 p.33）
- actor / model / effort：`Wf-P12` / `account:zai-individual-coding-plan/GLM-5.3-Flash` / `max`
- PNG：`audit/p033.png`（pngmono 150dpi）
- 核对：p₁↔p₂ 双箭头图（p.32 末 "The graph is looking as" 的配图，MD 行 1435 后无图引用，图内容以 PDF 为准——已登记为图缺失伪影）、𝒰₂ 二次映射式、weight 公式 ∫_{C_{2,0}}dφ_{(12)}dφ_{(21)}=∫_{𝓗\{z₀\}}dφ(z,z₀)∧dφ(z₀,z)、Lemma（angle map 积分为零）、Proof（C̄_{2,0}⟶S¹×S¹、involution (φ₁,φ₂)↦(φ₂,φ₁)、z↦−z̄）、§7.3.2 heading、Maurer-Cartan ΠT(X^coor)⟶𝒲 式、ΠTG/G=Πg 段与 ΠTG⟶Πg 式、pullback families 两平凡丛式、σ_𝒯/σ_𝒟 拉回段（MD 行 1437–1477）。
- 结果：`FAIL`→4 处已修复：①行 1453 `$\phi:\overline{{C}}_{2,0}\mathrm{-}\varDelta S^1$`（箭头 mangling −Δ）→`$\longrightarrow S^1$`（PNG 确凿）；②行 1453 `reverses the orientation of and preserves`→补 `$\mathcal{H}$`（𝓗 丢失，PNG+文本层确凿）；③行 1463 `Q-manifold Π$\mathrm{?}G/G$`→`$\Pi TG/G$`（T 错写为 ?，PNG+文本层确凿）；④行 1477 `$\mathcal{U}\times id\boldsymbol{\omega}$`→`$\mathcal{U}\times id_{\mathcal{W}}$`（ω 应为 𝒲，PNG 确凿）。另登记：行 1435 后 p.32 配图（p₁/p₂ 图）在 MD 无引用无源图，以 PDF p.33 顶部原图为准（与 p.020 图丢失同类）。其余 PASS±：行 1469 句末缺句点（登记）；行 1453 `$z\mapsto-\overline{{z}}$` 前空格（登记）。公式行 1440/1446/1460/1466/1474 与印刷逐符号吻合。
- 备注：行 1479 起（§7.3.3 Flat families over ΠT(X^aff)）为印刷 p.34 内容，在 p.034 核对。

