# AUDIT — S. Smale《Generalized Poincaré's Conjecture in Dimensions Greater Than Four》

> mineru: standard 档云端解析，导出 `Smale_1961_generalized_poincare_mineru/`；
> 审计依据 = 二值化渲染 `audit/pNNN.png`（pngmono 150dpi）对照
> `Smale_1961_generalized_poincare__Smale_1961_generalized_poincare.md`。逐页审计，一页一签。
> PDF 结构：17 页（PDFlib 3.02 生成）。

## p.001（PDF p.1 / JSTOR 封面页）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：JSTOR 封面（题名/作者/Annals 74 (1961), 391-406/Stable URL/使用条款三段）逐字转写 ✓
- 结果：**PASS±**（±：底部 "http://uk.jstor.org/ Fri Mar 17 02:07:43 2006" 下载戳记行未收——戳记惯例）

## p.002（PDF p.2 / 印刷 p.391）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：
  - 题录（标题/作者/Received October 11, 1960/Revised March 27, 1961）✓；引言段（Poincaré 问题、
    generalized conjecture、n ≥ 5）✓
  - **THEOREM A** ✓；announced in [20] ✓
  - **THEOREM B**：原刊即印 "which has the **homotopy** of Sⁿ"（应为 homotopy type，源级笔误）
    ——md 忠实保留，不代改 ✓
  - Stallings [Bull. Amer. Math. Soc., 66 (1960), 485–488] ✓；nice function 定义 ✓
  - **THEOREM C**（(m−1)-connected、n ≥ 2m、(n,m) ≠ (4,2)、M₀ = Mₙ = 1、Mᵢ = 0）✓
  - cellular structure 段 ✓；脚注 *（Alfred P. Sloan Fellow）✓
- 结果：**PASS±**（±：①页眉 "ANNALS OF MATHEMATICS Vol. 74, No. 2, September, 1961 Printed in
  Japan" 与页码 391 未收；②Theorem B 缺 "type" 系原刊实物）

## p.003（PDF p.3 / 印刷 p.392）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：Theorem D（Morse [13]）✓；§1 handlebodies 预告（s-disks, k in number, Heegard）✓；
  **THEOREM F**（M=H∪H′, H∩H′=∂H=∂H′, 𝓗(2m+1,k,m)）✓；**THEOREM G**（type numbers = Betti
  numbers、𝓗(2m,k,m)）✓；Morse relation [12] 注 ✓；**THEOREM H**（一个极大一个极小、
  S^{2m−1} 交）✓；J-equivalence 定义（[25]/[10]、∂V ≅ M₁⊔(−M₂)、deformation retract）✓；
  **THEOREM I**（(m−1)-connected、2m+1 维、J-equivalent、m≠1 ⇒ diffeomorphic）✓
- 结果：**PASS±**（±：页眉 "392 STEPHEN SMALE" 与页码未收）

## p.004（PDF p.4 / 印刷 p.393）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：orientation preserving 段 ✓；[10, Problem 5] + Milnor counter-example 插语（括号相邻系
  原刊排印）✓；Milnor [10, p. 33]/Mazur [7]/[9, p. 440] 段 ✓；𝓗ⁿ 定义段 ✓
  - **THEOREM J** ✓；**微分结构表**：n=3,5,7,9,11,13,15 ↔ 0, 0, 28, 8, 992, 3, 16256——逐格吻合
    （|Θ₉|=8 系原刊实物，忠实保留）✓
  - countable/unique structures 段（[9, p. 442]、Munkres [14]、Milnor [8]）✓；Γⁿ/Aⁿ/i: Γⁿ→Aⁿ、
    p: Aⁿ→𝓗ⁿ 段 ✓
- 结果：**PASS±**（±：页眉 "POINCARÉ CONJECTURE 393" 与页码未收）

## p.005（PDF p.5 / 印刷 p.394）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：**THEOREM K**（(a) Aⁿ→𝓗ⁿ→0, n≠3,4；(b) Γⁿ→Aⁿ→0, n even≠4；(c) 0→Aⁿ→𝓗ⁿ, n odd≠3；
  Γⁿ=Aⁿ/Aⁿ=𝓗ⁿ 推论）✓；(a)/(b)/(c) 来源句 ✓；Kervaire [4] ✓；**THEOREM L** ✓
  - W₀ 论证：Theorem 4.1 [10] k=3、∂W₀→S¹¹、12-disk、H⁶(M, π₅(SO(12)))=0、index 8、
    Lemma 3.7 [10]、Bott [1] ✓ 逐字
  - **THEOREM M** ✓；Schoenflies/Mazur [7] 段 ✓；Poincaré duality 论证段（∂C homotopy sphere、
    attach 2m-disk、Theorem H）✓
- 结果：**PASS±**（±：页眉 "394 STEPHEN SMALE" 与页码未收）

## p.006（PDF p.6 / 印刷 p.395）
- PNG：audit/p006.png（pngmono 150dpi）
- 核对：Palais [17] 承接段 ✓；Theorem B 证明段（[Munkres 15]、double W、Mazur [7]）✓；
  **THEOREM N**（Hauptvermutung for closed cells）✓；Hirsch [3]/Whitehead [27] 论证 ✓；
  **THEOREM O**（Hauptvermutung for spheres）✓；Gluck [2] 段 ✓；program 段（[21]、F/G）✓；
  proofs similar 段 ✓
- 结果：**PASS±**（±：页眉 "POINCARÉ CONJECTURE 395" 与页码未收）

## p.007（PDF p.7 / 印刷 p.396）
- PNG：audit/p007.png（pngmono 150dpi）；仲裁：audit/p007_300dpi.png + p007_dks_zoom3x.png（入库）
- 核对：mimeographed/Stallings gap 段 ✓；C^∞ 约定段 ✓；Eⁿ/Dⁿ/∂Dⁿ=S^{n−1}/D_iⁿ 定义式 ✓；
  Wallace [26] ✓；§1 χ(M,Q;f₁,…,f_k;s) 定义段 ✓——"the D_i^s × **D_i^{k−s}**"——3x 放大证实
  **原刊即印 k−s**（应为 n−s，同页 "handle" 与 corners 处均作 n−s；源级笔误）——md 忠实保留 ✓；
  straightening the angle/Milnor [10] 段 ✓；(1.1) LEMMA (a)(b)(c) ✓；presentation 定义 ✓
- 结果：**PASS±**（±：①页眉 "396 STEPHEN SMALE" 与页码未收；②D_i^{k−s} 系原刊笔误）

## p.008（PDF p.8 / 印刷 p.397）
- PNG：audit/p008.png（pngmono 150dpi）
- 核对：presentation 句 ✓；handlebody 定义（𝓗(n,k,0)、𝓗(2,1,1)=S¹×I+Möbius、𝓗(3,k,1)
  Henkelkörper [19]）✓；**(1.2) HANDLEBODY THEOREM**（n≥2s+2、s=1 时 n≥5、
  π₁(χ(H;f₁,…,f_{r−k};2))=1 附加假设、V∈𝓗(n,r−k,s+1)、括号注）✓
  - §2 记号（G_r 自由/自由交换、f_σ(D_i)=φ_i、f̄_i: ∂D^{s+1}×0→Q、x₀/y₀/U 基点处理）✓
  - realizes F 定义 ✓；**(2.1) THEOREM**（automorphism α、V realizes f_σ α）✓；**(2.2) LEMMA** ✓
- 结果：**PASS±**（±：页眉 "POINCARÉ CONJECTURE 397" 与页码未收）

## p.009（PDF p.9 / 印刷 p.398）
- PNG：audit/p009.png（pngmono 150dpi）
- 核对：(2.2) PROOF（covering homotopy property、Thom [23] + Palais CMH 34 (1960)、
  F_t/G_t、hf₂ = G₂^{-1}F₂ = F₁F₂^{-1}F₂ = f₁——原刊即如此）✓；**(2.3) THEOREM
  (H. Whitney, W.T. Wu)**（n ≥ max(2k+1,4)）✓；Whitney [29]/Wu [30] 注 ✓；
  **(2.4) LEMMA** + PROOF ✓；See [16] ✓；**(2.5) LEMMA (Nielson)** 生成元阵列
  R/T_i/S 及条件（i>1、j≠1,j≠i,i=2,⋯,r）✓；free abelian case ✓；𝓐 生成元归约句 ✓；
  α=R 开头 h: D^{s+1}×D^{n−s−1} 定义句 ✓
- 结果：**PASS±**（±：页眉 "398 STEPHEN SMALE" 与页码未收）

## p.010（PDF p.10 / 印刷 p.399）
- PNG：audit/p010.png（pngmono 150dpi）；仲裁：audit/p010_300dpi.png + hxy_zoom2x.png、
  gammag_zoom.png、gline2_300dpi.png、h32_300dpi.png（入库）
- 核对：
  - α=R 情形：h(x,y)=(r,x,y)——300dpi 证实**原刊即印 "(r,x,y)"**（数学上应预期 (rx,y)；源级笔误）
    ——md 忠实 ✓；f_i′=f₁h、χ(σ′) realizes f_σ′=f_σ α ✓；α=T_i/(1.1) ✓
  - V₁/Q₁ 定义、γ/β 同态 ✓；**(2.6) LEMMA**（φ₂ ∈ γ Ker β）+ PROOF（ψ̄、γψ̄=φ₂、βψ̄=0、
    g=y+ψ̄（s=1 时 yψ̄））✓；n=2s+2 情形 (2.4) 应用 ✓
  - "Since γg=g₁+g₂, f_σα(D₁)=f_σ(D₁+D₂)=g₁+g₂, f_σ′(D₁)=gD₁=g₁+g₂, f_σα=f_σ′"——300dpi 证实
    **原刊即用 g₁+g₂/gD₁**（未先行定义，应预期 φ₁+φ₂/γḡ——源级行文瑕疵）——md 忠实 ✓
  - §3/(3.1) THEOREM ✓；**(3.2) LEMMA**——300dpi 证实**原刊即缺 "H ∈"**（"If 𝓗(n,k,s) then
    π_s(H) is"；源级笔误）——md 忠实 ✓；(a)(b)(c) +Furthermore ✓；PROOF 开头 ✓
- 结果：**PASS±**（±：①页眉 "POINCARÉ CONJECTURE 399" 与页码未收；②(r,x,y)/g₁+g₂/缺 "H ∈"
  三处均系原刊实物）

## p.011（PDF p.11 / 印刷 p.400）
- PNG：audit/p011.png（pngmono 150dpi）
- 核对：(3.2) PROOF（wedge of k s-spheres、π_i(H,∂H)=0 归零构造 f₁→f₄、D_i^s×0）✓；
  H_β cell bundle 定义 ✓；**(3.3) LEMMA**（V=χ(H_β;f;s+1)≅Dⁿ）✓；PROOF（zero-cross-section、
  regular homotopy [29]、β=0、S^s×D^{n−s} 乘积）✓；σ₁/f̄ 同伦段（orientation reversing 注）✓；
  f_ε/g_ε/r_ε/k_ε/p_x 构造段（D_ε^{n−s−1}、(x, εy)、F_x fibre、σ^{-1}g_ε(x,0)）✓
- 结果：**PASS±**（±：页眉 "400 STEPHEN SMALE" 与页码未收）

## p.012（PDF p.12 / 印刷 p.401）
- PNG：audit/p012.png（pngmono 150dpi）；仲裁：audit/p012_300dpi.png + keps_zoom6x.png、
  pis_zoom2x.png、dni_300dpi.png、gammabar_zoom.png（入库）
- 核对：
  - "It can be proved k_ε and g_ε are differentiably isotopic"——6x 证实原刊下标为 **ε**，
    **md 作 k_e/g_e → FAIL**（修复：e→\varepsilon）；referee/tubular neighborhood theorem 注 ✓
  - (3.3) 证明收尾：V′=χ(H_β;f′;s+1)、**π_ε(V′)=0**——300dpi 证实原刊即印 **ε 下标**
    （数学上应预期 π_s；源级笔误）——md 忠实 ✓；replace f/f′ by k_ε/k_ε′、hf=f′、image f∩F_x ✓
  - M₁ⁿ/M₂ⁿ 段：**f_i: D^{n−1}×i → ∂M_i**——300dpi 证实原刊即印小写 i（应预期 ×{i}/×I；
    源级笔误）——md 忠实 ✓；M₁+M₂ 定义 ✓；**(3.4)** ✓；**(3.5)** + PROOF（φ(D^s)、T cell、
    H_β、V∈M+H_β）✓
  - (3.1) 证明开头：H=χ(Dⁿ;f₁,⋯,f_k;s)、γ̄_i ∈ π_s(H,Dⁿ)、"Let γ_i ∈ π_s(∂H) be the image of
    **γ_i**"——300dpi 证实原刊第二个 γ_i **无横杠**（应预期 γ̄_i；源级笔误）——md 忠实 ✓；
    gD_i=γ_i (i≤k)、gD_i=0 (i>k) ✓；**(3.6)** ✓
- 结果：**FAIL（单点）**：k_e/g_e → k_ε/g_ε（6x 仲裁）。
- 备注：± ①页眉 "POINCARÉ CONJECTURE 401" 与页码未收；②π_ε(V′)/D^{n−1}×i/γ_i 缺横杠
  三处均系原刊实物。

## p.013（PDF p.13 / 印刷 p.402）
- PNG：audit/p013.png（pngmono 150dpi）
- 核对：g₁′/(3.5) and f₁ 承接 ✓；§4 s=0（permutation i₁,…,i_r、Y=χ(H;f_{i₁},…,f_{i_k};1)、
  V=χ(Y;f_{i_{k+1}},…,f_{i_r};1) ∈ 𝓗(n,r−k,1)）✓；s=1（g: G_k→π₁(∂H)、ḡ_i、(2.4)、
  χ(Y,g₁,…,g_k)=χ(H;…)=χ(Dⁿ,f₁,…,f_{r−k}) ∈ 𝓗(n,r−k,2)）✓；**(4.1) LEMMA** + PROOF
  （rank G − rank G′、p: G′+G″→G′、0→f^{-1}(0)→G→G′→0 splits、α = f+kh）✓；
  Grusko [6] REMARK ✓；f_σα=g 归结段 ✓；§5 开头 ✓
- 结果：**PASS±**（±：页眉 "402 STEPHEN SMALE" 与页码未收）

## p.014（PDF p.14 / 印刷 p.403）
- PNG：audit/p014.png（pngmono 150dpi）
- 核对：**(5.1) THEOREM**（𝓗_M(n,k,s)、Q=∂H−M×0、π_s(M×0)→π_s(V) isomorphism、
  s=1 附加假设、V∈𝓗_M(n,r−k,s+1)）✓；(1.2) 归约句 ✓；**(5.2)** ✓；p₁/p₂ 投影 ✓；**(5.3)** ✓
  - (5.1) 证明（p₁f_σ trivial、p₂f_σ epimorphism、(4.1)、p₂f_σα=p₂g）✓——σ=(H,Q;g₁,⋯,g_r,s+1)
    逗号系原刊 ✓
  - §6 开头 ✓；**(6.1) THEOREM**（f^{-1}[−∞,ε] presentation）✓；**(6.2) THEOREM**（k new critical
    points index s）✓；SKETCH OF PROOF（Morse [13] 坐标式 f(x)=−Σ_{i=1}^λ x_i²+Σ_{i=λ+1}^n x_i²、
    E₁/E₂ 平面、D^λ）✓
- 结果：**PASS±**（±：页眉 "POINCARÉ CONJECTURE 403" 与页码未收）

## p.015（PDF p.15 / 印刷 p.404）
- PNG：audit/p015.png（pngmono 150dpi）；仲裁：audit/p015_300dpi.png + exists_zoom.png、
  cap_zoom2x.png（入库）
- 核对：T′ = T∩f^{−1}[−ε₁,ε₁] ≅ D^λ×D^{n−λ} 段 ✓；(6.1) 证明收尾（ε₁→ε 替换）✓；
  (6.2) converse 句 ✓；§7 开头 ✓；**(7.1) THEOREM**（f(V₁)=−(1/2)、f(V₂)=n+(1/2)、
  f(β)=index β）✓；nice functions 命名 ✓；X_s = f^{−1}[0, s+(1/2)] ✓；**(7.2)** ✓；**(7.3)**——
  "then there **exists—a** C^∞ non-degenerate function"：300dpi 证实**原刊即有长横线**
  （源级标点 quirk）——md 忠实 ✓
  - Theorem C 证明开头：X₀ ∈ 𝓗(n,q,0)、π₁(M)=1 & n≥6、Samelson 论证、X₂′ = X₂ + k copies
    D^{n−2}×S²、X₂′ ∈ 𝓗(n,r,2)、f_i: ∂D³×D^{n−3}→∂H_i **∩** ∂X₂′（inline 原刊 ∩，md 忠实）✓；
    显示式 π₂(∂D³×D^{n−3}) → π₂(**∂H_i × ∂X₂′**) → π₂(∂H_i)——300dpi 证实显示式中间项原刊即 **×**
    （与 inline 的 ∩ 不一致系原刊排印自身；md 逐处忠实）✓
- 结果：**PASS±**（±：①页眉 "404 STEPHEN SMALE" 与页码未收；②exists—a 长横线与
  inline∩/display× 不一致均系原刊实物）

## p.016（PDF p.16 / 印刷 p.405）
- PNG：audit/p016.png（pngmono 150dpi）
- 核对：χ(X₂′,f₁,…,f_k;3)≅X₂、X₃=χ(X₂′,f₁,…,f_k,g₁,…,g_l;3) ∈ **H**(n,k+l−r,3)（原刊此处
  即印斜体 H 而非花体 𝓗——排印不一致，md 逐处忠实）✓；X_m′ ∈ 𝓗(n,r,m)、h^{-1}[n−m−(1/2),n]
  =X_m^* ∈ 𝓗(n,k₁,m)、modify h by (7.3) ✓；Theorem I 证明（∂V=V₁−V₂、n=2m+2、(5.1) 替换、
  index m+1）✓；**(7.4) LEMMA**（χ_v = Σ(−1)^q M_q + χ_{v₁}；χ_V/χ_v 大小写原刊混用，md 忠实）✓；
  §8（M_m = M_{m+1}、f^{-1}[0,m+(1/2)] ∈ 𝓗(2m+1,M_m,m)）✓；Theorem G 收尾 ✓；
  UNIVERSITY OF CALIFORNIA, BERKELEY ✓；REFERENCES + Ref 1 (Bott, Ann. of Math., 70 (1959),
  313-337) ✓
- 结果：**PASS±**（±：页眉 "POINCARÉ CONJECTURE 405" 与页码未收）

## p.017（PDF p.17 / 印刷 p.406）
- PNG：audit/p017.png（pngmono 150dpi）；仲裁：audit/p017_300dpi.png + ref16b_zoom.png、
  ref30_zoom.png（入库）
- 核对：参考文献 2-30 逐条（作者/题名/刊名/卷页年）：2. Gluck (66 (1960), 282-284) ✓；
  3. Hirsch to appear ✓；4. Kervaire (CMH 34 (1960), 304-312) ✓；5. Kervaire-Milnor to appear ✓；
  6. Kurosh ✓；7. Mazur (65 (1959), 59-65) ✓；8. Milnor (AJM 81 (1959), 962-972) ✓；
  9. Milnor (BSMF 87 (1959), 439-444) ✓；10. Milnor mimeographed ✓；11. Moise ✓；12. Morse ✓；
  13. Morse (Ann. 71 (1960), 352-383) ✓；14/15. Munkres ✓；**16. Nielsen——300dpi 证实原刊即印
  "Math. Ann., 9 (1919), 269-272"**（实刊为 Math. Ann. 91 (1924), 269-272——原刊卷/年双误，
  md 忠实）✓；17. Palais ✓；18. Papakyriakopoulos ✓；**19. "THRELLFALL"**（原刊拼写，实为
  Threlfall——源级笔误，md 忠实）✓；20/21. Smale ✓；22-25. Thom ✓（25 "caracteristiques"
  无重音系原刊）✓；26. Wallace ✓；27/28. Whitehead ✓；29. Whitney ✓；
  **30. Wu——300dpi 证实原刊即印 "Now Ser."**（应为 New Ser.，源级笔误，md 忠实）✓
- 结果：**PASS±**（±：①页眉 "406 STEPHEN SMALE" 与页码未收；②Ref 16/19/30 三处系原刊实物）

---

## 总评

- **覆盖声明**：17/17 页逐页目检（pngmono 150dpi，`audit/p001-p017.png`），每页五点比对后即时
  落签并提交；300dpi 灰度仲裁 17 件入库（含 2x/3x/6x 放大 5 件）。mineru：standard 档云端解析
  （JSTOR 扫描件）。
- **数学内容可信度**：Theorems A-O（含微分结构表逐格）、(1.1)-(1.2) Handlebody Theorem、
  (2.1)-(2.6)、(3.1)-(3.6)、(4.1)、(5.1)-(5.3)、(6.1)-(6.2)、(7.1)-(7.4) 及各证明的公式链逐式
  核对全部吻合；30 条参考文献逐条对原刊核实。
- **系统性瑕疵（PASS± 家族）**：①页眉/页码全篇未收；②JSTOR 封面页下载戳记未收；③原刊
  𝓗/H 花体与斜体混用（md 逐处忠实）；④χ_V/χ_v 大小写混用（同上）。
- **FAIL 清单（1 项）**：p.012 "k_e/g_e" → 原刊为 "k_ε/g_ε"（6x 放大仲裁）。
- **原刊排印 quirk（md 忠实，不代改）**：①Theorem B 缺 "type"；②D_i^s×D_i^{k−s}（应 n−s）；
  ③(h(x,y)=(r,x,y)（应 (rx,y)）；④γg=g₁+g₂/f_σ′(D₁)=gD₁ 未定义记号（应 φ₁+φ₂）；⑤(3.2) 缺
  "H ∈"；⑥π_ε(V′)（应 π_s）；⑦D^{n−1}×i（应 ×{i}）；⑧"image of γ_i" 缺横杠（应 γ̄_i）；
  ⑨(7.3) "exists—a" 长横线；⑩inline ∩/display × 不一致（∂H_i 与 ∂X₂′）；⑪Ref 16 "9 (1919)"
  （实为 91 (1924)）；⑫Ref 19 "THRELLFALL"；⑬Ref 30 "Now Ser."。
- **可用性结论**：修复 1 项 FAIL 后，本 md 可作为该文的忠实检索/阅读底本；定理陈述与公式链
  逐字可信；阅读时应知：JSTOR 封面混入（实物如此）、页眉未收、上列 13 项原刊 quirk。
