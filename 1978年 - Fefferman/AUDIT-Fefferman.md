# AUDIT — Fefferman "Characterizations of bounded mean oscillation" (Bull. AMS 77 (1971), 587-588)

> mineru: standard 档云端解析，导出 `Fefferman_1971_bmo_mineru/`；审计依据 = 二值化渲染
> `audit/pNNN.png`（pngmono 150dpi）对照 `Fefferman_1971_bmo__Fefferman_1971_bmo.md`。
> 逐页审计，一页一签。

## p.001（PDF p.1 / 印刷 p.587）
- PNG：audit/p001.png
- 核对：
  - 题录：标题 CHARACTERIZATIONS OF BOUNDED MEAN OSCILLATION ✓、作者 BY CHARLES FEFFERMAN ✓、
    Communicated by M. H. Protter, December 14, 1970 ✓
  - BMO 定义式 ‖f‖_BMO = sup_Q (1/|Q|)∫_Q |f(x) − av_Q f| dx < ∞ ✓（含 av_Q 说明、[5] 引用、
    f 与 f′ 模常数同一约定）
  - Theorem 1（BMO = (H¹)*，配对 ⟨f,g⟩=∫fg，g 属 H¹ 中 C^∞ 速降稠密子空间）✓ 逐字吻合
  - Theorem 2（f = g₀ + Σ_{j=1}^n R_j(g_j)，g_i ∈ L^∞）✓
  - R_j 常规定义式（lim_{ε→0; M→∞} ∫_{ε<|x−y|<M} K_j(x−y)f(y)dy）✓、
    K_j(y)=cy_j/|y|^{n+1} ✓、sgn(x) 反例 ✓
  - 修正定义式（含 K_j^0 截断，|y|>1 / |y|≤1）✓、See [3, p.105] ✓
  - 脚注三条：AMS 1969 subject classifications. Primary 3067, 4635 ✓；Key words ✓；
    Copyright © 1971 AMS ✓
- 结果：**PASS±**
  - ±1：mineru 丢失页眉（BULLETIN OF THE AMS, Volume 77, Number 4, July 1971）与页码 587
    （running head 级丢失，不影响正文）；
  - ±2：md 中脚注块之后紧跟 (∗) 式与 Theorem 3——该部分实属印刷 p.588（见 p.002 签），
    mineru 未打页界导致两页内容连排；内容本身无损。
- 备注：数学内容零错误。

## p.002（PDF p.2 / 印刷 p.588）
- PNG：audit/p002.png
- 核对：
  - (∗) 式 ∫_{Rⁿ} |f(x)|/(|x|+1)^{n+1} dx < ∞ ✓（与 p.001 末句"any function f satisfying"衔接正确）
  - Poisson 积分 u(x,t)=P.I.(f) 定义于 R₊^{n+1}=Rⁿ×(0,∞) ✓
  - Theorem 3（BMO ⟺ (∗) 且 ∬_{|x−x₀|<δ; 0<t<δ} t|∇u|² dxdt ≤ Cδⁿ）✓ 逐字吻合
  - Theorem 4（(n+1)-元组调和函数 F、[7] 的 Cauchy-Riemann 方程、非切向极大函数
    u₀*(x)=sup_{|x'|<t;t>0}|u₀(x−x′,t)| ∈ L¹ ⟹ F∈H¹）✓
  - L^p/H^p 推广段（0<p<∞，Burkholder-Gundy-Silverstein [1][2]）✓
  - 应用指引 [4][6] ✓（[4] 含详细证明）
  - REFERENCES 1–7 逐条核对：Burkholder-Gundy, Acta Math. 124 (1970), 249-304 ✓；
    B-G-S (to appear) ✓；Calderón-Zygmund, Acta Math. 88 (1952), 85-139, MR 14,637 ✓；
    Fefferman-Stein (in prep.) ✓；John-Nirenberg, CPAM 14 (1961), 785-799 ✓；
    Stein, Bull. AMS 77 (1971), 404-405 ✓；Stein-Weiss, Princeton 1971 ✓
  - 署名 UNIVERSITY OF CHICAGO, CHICAGO, ILLINOIS 60637 ✓
- 结果：**PASS±**
  - ±：仅 running head（588 / CHARLES FEFFERMAN）被 mineru 丢弃（同 p.001 ±1）。

## 总评
- 全文 2 页逐页审计完成：**全部 PASS，零数学错误**。
- 系统性瑕疵 2 项（均不误导）：①running head/页码丢失；②两页内容连排无页界标记。
- 结论：该 Markdown 可放心作为正文引用与检索底本；页界请以原 PDF 为准。
