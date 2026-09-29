# AUDIT — Kodaira "On a differential-geometric method in the theory of analytic stacks"（PNAS 39 (1953) 1268-1273）
+ 附录：Kodaira-Spencer "On a theorem of Lefschetz and the lemma of Enriques-Severi-Zariski"（同页 1273 起，PDF 随附下载包含其开头）

> 二值化渲染 audit/p001-p006.png（pngmono 150dpi）对照 Kodaira_1953_analytic_stacks_mineru md。逐页一签。
> 注：PNAS 原始 PDF 即含同卷后文（Kodaira-Spencer 短文）开头 1 页——md 一并转写，属白赚内容。

## p.001（印刷 p.1268）
- 核对：脚注 \*（结果将发表于 Acta Mathematica 1954 / Michigan Conference Report）✓；
  系列¹-⁶ 与 Kaplan⁶ 全部文献行 ✓（Ann. Math. Studies No. 30, 111-139；Fund. Math. 39,
  269-287；Acta Mathematica 1954；Am. J. Math. 75, 23-51；Michigan Report；Duke Math. J.
  I,7,154-185 / II,8,11-45 / Am. J. Math. 64,1-35）✓；
  标题 ON A DIFFERENTIAL-GEOMETRIC METHOD IN THE THEORY OF ANALYTIC STACKS* ✓；
  By K. KODAIRA, Princeton ✓；Communicated by S. Lefschetz, September 9, 1953 ✓；
  §1 Introduction（V 紧 Kähler、F 线丛、Ω^p(F)、H^q 消没问题、Bochner 方法）✓；
  §2 开头 ds²=2Σg_αβ(dz^α dz̄^β) ✓、{f_jk} 与 f_jk f_kl f_lj = 1 ✓、(1) a_j/a_k=|f_jk|² ✓
- 结果：**PASS±**（±：页眉 1268 / MATHEMATICS: K. KODAIRA / Proc. N.A.S. 丢失；侧栏水印未收）

## p.002（印刷 p.1269）
- 核对：φ_j = f_jk·φ_k ✓；(∂̄φ)_j 与 (𝔡φ)_j = −*a_j∂(1/a_j *φ_j) ✓；harmonic 定义 ✓；
  (2) H^q(V;Ω^p(F)) ≅ H^{p,q}(F) ✓；φ → φ† = (1/a_j)*φ̄_j 映射 ✓；
  (3) H^q(V;Ω^p(F)) ≅ H^{n−q}(V;Ω^{n−p}(−F)) ✓；§3 (4)₁ (4)₂ 显式方程 ✓；
  ρ_jλ = −∂_λ log a_j ✓；曲率张量 R^σ_{τα*β} = ∂̄_α(Σg^{σν*}∂_β g_{τν*}) ✓
- 结果：**PASS**

## p.003（印刷 p.1270）
- 核对：(5) X_{λα*} = −∂̄_α ρ_jλ = ∂_λ∂̄_α log a_j ✓；(6) 调和形式基本关系式（含
  (σ)_h/(μ*)_m 替换约定）✓；(7) ΣX_{λα*}dz^λdz̄^α = ∂∂̄ log a_j 整体 2-形式 ✓；
  ξ_μ* 与 φ̄ 上指标式 ✓；(8) −δξ = # + …（# ≥ 0）✓；
  (9) 0 ≥ ∫_V{qΣ(δ^σ_τ[X^β*_α*−R^β*_α*]+pR^σβ*_{τα*})·…} ✓
- 结果：**PASS**（长公式转写结构完整，仅个别上下标排布与原文视觉排法不同——语义一致）

## p.004（印刷 p.1271）
- 核对：(p,q)-form 与实 (1,1)-形式 ψ>0 定义 ✓；LEMMA（γ=(i/2π)∂∂̄ log a_j ∈ c(F) 的
  双向刻画）✓；Proof：主丛 F*、ζ_j = f_jk(z)ζ_k、Φ = (1/2πi)(d log ζ_j − ∂ log a_j)、
  −dΦ = (i/2π)∂∂̄ log a_j ✓；Green 算子论证 γ₀ = ΔGγ₀、Λ∂−∂Λ = −i∂ ✓；
  Θ^{p,q}(γ,u;z) Hermite 型 ✓；(10) ∫_V (g/a_j)Θ^{p,q}(γ,φ_j;z)dV ≤ 0 (q≥1) ✓
- 结果：**PASS**

## p.005（印刷 p.1272）
- 核对：THEOREM 1（c(F) 含充分大的 d-闭 (1,1)-形式 γ ⟹ H^q(V,Ω^p(F)) 与
  H^{n−q}(V,Ω^{n−p}(−F)) 消没，1 ≤ q ≤ n）✓ 及 Proof ✓；
  p=n 情形 Θ^{n,q} = n!ΣX^β*_{α*}… ⟺ γ>0 ✓；THEOREM 2 ✓；canonical bundle K 与
  Jacobians J_jk ✓；−c(K)=第一 Chern 类 ✓；Ω⁰(F) ≅ Ωⁿ(F−K) ✓；THEOREM 3 ✓；
  脚注 \*（Office of Ordnance Research 资助）✓、¹（线丛定义+Kodaira-Spencer PNAS
  39, 868-872 引用）✓、²（Bochner Ann. Math. 49, 379-390; 50, 77-93）✓、
  ³（Kodaira PNAS 39, 865-868）✓、⁴（loc. cit.）✓
- 结果：**PASS**

## p.006（印刷 p.1273）
- 核对：脚注 ⁵（Serre 对偶特例）✓、⁶（Garabedian-Spencer Acta Math. 89, 279-331）✓、
  ⁷（de Rham）✓、⁸（loc. cit. p.290）✓；
  第二篇：ON A THEOREM OF LEFSCHETZ AND THE LEMMA OF ENRIQUES-SEVERI-ZARISKI* ✓、
  By K. KODAIRA AND D. C. SPENCER ✓、Communicated October 8, 1953 ✓；
  §1（Lefschetz 定理推广至 Kähler 丛上同调、含 Enriques-Severi-Zariski 引理）✓；
  §2（S 非奇异除子、{S} 线丛、s_jk = s_j/s_k、c({S}) 为 S 同调类之对偶）✓；
  η_j 分解与 η'_j、η''_j ✓
- 结果：**PASS**（第二篇仅开头 1 页，后续页不在本 PDF——属下载自然截断，非遗漏）

## 总评
- 6 页逐页审计完成：**全部 PASS，零数学错误**；
- 系统性瑕疵：页眉/页码丢失、侧栏水印未收、脚注集中到文末且顺序略有重排（全部在）；
- md 的 (4)₁(4)₂ 排版记法 "（4) ( _{1}" 稍怪但语义保真。
- 结论：md 可作为正文引用与检索底本；白赚的 Kodaira-Spencer 短文开头亦已转写。
