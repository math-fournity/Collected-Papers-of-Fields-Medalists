# AUDIT — Atiyah & Singer, "The Index of Elliptic Operators on Compact Manifolds"（Bull. Amer. Math. Soc. 69 (1963), 422–433）

> mineru: standard 档云端解析，导出 `Atiyah_Singer_1963_index_theorem_mineru/`；
> 审计依据 = 二值化渲染 `audit/pNNN.png`（pngmono 150dpi）对照
> `Atiyah_Singer_1963_index_theorem__Atiyah_Singer_1963_index_theorem.md`。逐页审计，一页一签。
> PDF 结构：12 页 = 印刷 pp.422–433；ABBYY FineReader 生成（2007，含文本层）；
> **PDF 首页上半为前一篇论文（半群论文，UC Davis）的结尾**——md 如实转写（Cohen/Kodaira 案例同类"自然截断"）。

## p.001（PDF p.1 / 印刷 p.422）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：
  - 前篇尾巴（T_p 半群段、REFERENCES 1-4 Clifford/Hölder/Tamura、UNIVERSITY OF CALIFORNIA, DAVIS）
    逐字转写 ✓（j/p^i、completely exclusive direct product、各卷页年数字均吻合）
  - 题录：标题/作者/Communicated by Raoul Bott, February 1, 1963 ✓
  - 引言：Gel'fand [16] 问题、Agranovic [2;3]/Dynin [3;14;15]/Seeley [20;21]/Vol'pert [22]、
    Theorem 1 一般公式、Hirzebruch-Riemann-Roch（Theorem 3）"previously known only for
    projective algebraic manifolds"、§3 预告 ✓ 逐字
  - 致谢 Calderon/Nirenberg/Seeley ✓；§1 开头 "compact oriented smooth mani-"（跨页连字）✓
  - 脚注 1（NSF/Sloan Fellowship）✓ 以 page_footnote span 保留
- 结果：**PASS±**（±：页眉 "422 M. F. ATIYAH AND I. M. SINGER [May" 与页码未收；前篇尾巴混入——系 PDF 实物如此，转写忠实）
- 备注：文献 4 条卷页全对。

## p.002（PDF p.2 / 印刷 p.423）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：
  - D: Γ(E)→Γ(F) 定义、"geometrically interesting operators operate on vector bundles (cf. §3)" ✓
  - T*(X)/S(X)/π、σ(D): π*E→π*F、symbol 定义（∂/∂x_j→iξ_j）、elliptic ⇔ σ(D) isomorphism ✓
  - Ker D/Coker D=Γ(F)/DΓ(E) 有限维、γ(D)=dim Ker D−dim Coker D、伴随 D*: Γ(F)→Γ(E)、
    Coker D≅Ker D*、γ(D)=dim Ker D−dim Ker D* ✓
  - ch(D) 问题陈述 ✓；§2 开头 GL(m, C)、Bott periodicity [8]、Grothendieck groups K(X) [5](cf. [4]) ✓
  - 脚注 2 "E, F have the same dimension" ✓
- 结果：**PASS±**（±：页眉 "1963₁ THE INDEX OF ELLIPTIC OPERATORS 423" 未收）
- 备注："Grothen-dieck" 连字为原文跨行断字，md 忠实保留。

## p.003（PDF p.3 / 印刷 p.424）
- PNG：audit/p003.png（pngmono 150dpi）
- 核对：
  - Chern character ch: K(X)→H*(X; ℚ)、difference element [6, §3]、d(E,F,σ)∈K(Y/Y₀) ✓
  - B(X) 单位球丛、d(p*E,p*F,σ(D))∈K(B(X)/S(X))、ch d(...)∈H*(B(X)/S(X); ℚ) ✓
  - Thom isomorphism φ*: H^k(X;ℚ)≅H^{n+k}(B(X)/S(X);ℚ) (n=dim X)、φ*⁻¹ ch d(...)、ch σ(D)/ch(D) ✓
  - Todd class 定义 𝕀(ξ)=∏ x_i/(1−e^{−x_i})、ch ξ=Σ e^{x_i}、x_i 次数 2、c_i(ξ) ✓；𝕀(η)=𝕀(η⊗_R C) ✓
  - 脚注 3/4 文本在 md 中以 page_footnote span 保留，但——
- 结果：**FAIL（单点）**：脚注 3 编号被误识为 8——md 作 "$^{8}$ We assume Y₀ a 'reasonable' subspace…"，
  原文页脚清楚为 "³ We assume …"（150dpi 可辨，无需 300dpi 仲裁）；与后文真脚注 8（K̃）形成重复编号、
  脚注 3 缺号。修复建议：将该 "$^{8}$" 改回 "$^{3}$"。
- 备注：±项（不误导）：①行 121-125 五个孤立 page_footnote 碎片 span（"E, F"/"$Y_0$"/"T(Y)"/"X"/
  "T(X)⊗_R C"——正文片段重复检出，碎片化伪影）；②ℚ 转写为 \mathcal{Q}（Zelmanov 篇同类）。

## p.004（PDF p.4 / 印刷 p.425）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：
  - 𝕀(X)=𝕀(T(X))、y_j² 初等对称函数、𝕀(X)=∏_j y_j/(1−e^{−y_j})·(−y_j)/(1−e^{y_j}) ✓
  - α[X] 定义 ✓
  - **THEOREM 1**：γ(D)={ch(D)·𝕀(X)}[X] ✓（逐字，含黑体 [X]）
  - REMARKS 1-3（singular integral operators cf. §4 / γ(D)=0 cf. (3.5) / rational→integer）✓
  - §3 G-structure：G-模 V、principal G-bundle P、(A) P×_G V≅T(X)、(B) P×_G M≅E, P×_G N≅F、
    G-map V*→Hom(M,N) polynomial degree k ✓
- 结果：**PASS**（±：页眉 "1963₁ … 425" 未收）
- 备注：本页无内容级差异；定理公式逐字符吻合。

## p.005（PDF p.5 / 印刷 p.426）
- PNG：audit/p005.png（pngmono 150dpi）
- 核对：
  - **THEOREM 2**：dim V=2l、rank l、universal class (ch M − ch N)∏_{i=1}^l ω_i⁻¹ ∈ H**(B_G; ℚ)、
    negative⁵ weights、Borel-Hirzebruch [7] ✓
  - 脚注 5（"negative" weights / orientation）✓
  - (3.1) RIEMANNIAN STRUCTURE G=SO(2l)：Λ=ΣΛ^p、*: Λ^p→Λ^{2l-p}、(*)²=(−1)^p、α²=1、
    M(N) ±1 eigenspace、(i) ρ=(*)² (ii) ρ=α、D=d+δ、ρω=ω⇒ρ(Dω)=−Dω ✓
  - 结论 (i) Σ(−1)^p h^p=χ[X]（Gauss-Bonnet）/(ii) h_+^l−h_−^l=L(X)（l even）✓
- 结果：**PASS±**
- 备注：± ①页眉未收；②α 定义上标辖域合并：md 作 `i^{p(p+1)-l *}`（* 被并入指数），
  原文为 `i^{p(p+1)-l} *`（i 的幂乘以 * 算子）——排版级伪影，不误导（α²=1 仍成立）。

## p.006（PDF p.6 / 印刷 p.427）
- PNG：audit/p006.png（pngmono 150dpi）
- 核对：
  - Hirzebruch index theorem [17, §8] 承接、d+δ self-adjoint REMARK ✓
  - (3.2) HERMITIAN STRUCTURE G=U(l)×U(m)：M=(Σ_k Λ^{2k})⊗C^m、N=(Σ_k Λ^{2k+1})⊗C^m ✓
  - V≅V̄*、D=∂̄+𝔡、γ(D)=Σ(−1)^p h^{0,p}(W)、Laplacian、Dolbeault isomorphism [17, §15]、
    H^{0,p}(W)≅H^p(X,W) ✓
  - **THEOREM 3**（HRR）：Σ(−1)^p dim H^p(X,W)={ch(W)𝕀(X)}[X] ✓；Hirzebruch [17]/Kodaira [18] Kahler surfaces ✓
- 结果：**PASS±**
- 备注：± ①页眉未收；②伴随算子字形（原刊花体 𝔡）混并：md 行 "D=∂̄+d … and d is its formal adjoint"
  把 𝔡 转写为普通 d，而同段 Laplacian 行又作 \mathfrak{d}——同篇内前后不一致（Fraktur 混排家族伪影，
  数学内容可由上下文唯一确定，不误导）；③Todd 类字形 \Im 与 \mathfrak{I} 混用（同上）。
