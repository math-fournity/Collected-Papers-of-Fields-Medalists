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
