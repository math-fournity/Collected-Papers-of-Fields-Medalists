# AUDIT — Enrico Bombieri《Algebraic Values of Meromorphic Maps》（Invent. math. 10, 267-287 (1970)，GDZ 600dpi CCITT 扫描件 + GDZ 封面页，22p）

> mineru: standard 档云端解析（自行 OCR，英文转写质量高）。**审计依据 = `audit/bom1970_pNNN.png`
> （pngmono 150dpi 全 22 页：p.001=GDZ 封面，p.002-022=print 267-287）**；pdftotext 文本层仅含
> GDZ 元数据（1393 字节），**按扫描件 SOP 纯 PNG 审计**。
> **伪影族**：印刷页脚/装订签名串入正文（"19 Inventiones math., Vol. 10"/"19\*"/"20 …"/"20\*"）×4、
> 脚注 1 幽灵碎片 ×4、**References [6]-[11]+作者块+Received 整段丢失**、"polynomial" 应为
> print 之 "polinomial"（源级拼写被 mineru 纠正——还原）。

## p.001（GDZ 封面）
- 核对：GDZ 元数据（Inventiones Mathematicae/Springer/1970/PPN356556735_0010/LOG_0031/PURL）+
  Terms and Conditions ✓（md 保留原文）
- 结果：**PASS**（非论文内容）
## p.002（print 267：题录 + §I Theorem A + Remark 1/2）
- 核对：刊头 Invent. math. 10, 267-287 (1970)/© Springer-Verlag ✓；题名/ENRICO BOMBIERI (Pisa) ✓；
  Theorem A (i) tr.deg K(f)≥d+1 (ii) ∂/∂z_α ✓；Remark 1 界 d(d+1)ρ[K:Q]+2d ✓；
  Remark 2 ∂f_i/∂z_α=P_iα(f)Q(f)^{-1}/f_{N+1}=Q(f)^{-1}/K[f̃] ✓；Lang [5]/Schneider [10]/
  ≤20ρ[K:Q] ✓
- 结果：**PASS**
## p.003（print 268：Lang 乘积集 + Nagata 引文 + §II 正 (1,1)-流）
- 核对：S₁×⋯×S_d/min card S_α≤bρ[K:Q] ✓；historical note 引文全段 ✓；Lelong/currents/
  Carleman/Andreotti-Vesentini [1]/Hörmander [4] ✓；致谢 Lang/Kerzman ✓；§II 𝒟(Ω)/φ 展开/
  comass ‖φ‖=2^{n−1}sup/SU(n) ✓
- 结果：**PASS**
## p.004（print 269：‖φ‖_Ω + Proposition 1）
- 核对：‖φ‖_Ω ✓；T=Σt_αβ̄dz∧dz̄ ✓；‖T‖(f)=sup|T(φ)| ✓；Radon measure ✓；ω=i/2 Σdz∧dz̄ ✓；
  ω_k=1/k! ω^k/‖ω_{n−1}‖=1 ✓；hermitian ✓；**Proposition 1 d‖T‖=iT∧ω_{n−1}=2(Σt_αα)∧ω_n** ✓；
  [2], p.652 ✓；‖T‖Ω=∫d‖T‖ ✓
- 结果：**PASS**
## p.005（print 270：质量/密度 + Proposition 2 + 证明开头）
- 核对：Θ(‖T‖;r,a)=(n−1)!/π^{n−1}r^{2n−2}‖T‖B(r,a) ✓；Θ*/Θ_* ✓；∂̄-closed/∂̄T(φ)=−T(∂̄φ) ✓；
  Proposition 2 单调 ✓；[8], p.73 and [2], pp.621 and 652 ✓；(i/2π)∂∂̄log|z| Levi ✓；
  B(R,a)∖B(r,a) 积分式 ✓
- 结果：**PASS**
## p.006（print 271：Proposition 2 证明 + §III 开头）
- 核对：iT=∂̄S/S(∂̄φ)=−iT(φ) ✓；∂̄S∧(…)ⁿ⁻¹=∂̄[S∧(…)ⁿ⁻¹]/Stokes ✓；
  (i/2π∂∂̄log|z|)^{n−1}=(n−1)!/π^{n−1}r^{2n−2}ω_{n−1} on ∂B ✓；三行 ∫ 链 ✓；
  ∂̄ω=0/∂̄(iT∧ω_{n−1})=S∧ω_{n−1} ✓；III 节 T=∂∂̄V ✓
- 结果：**PASS**
## p.007（print 272：除子 + Proposition 3 (i)(ii)）
- 核对：T=1/π∂∂̄log|F|/V=1/πlog|F| ✓；iT(φ)=∫_W φ/F(z)=0/[8], p.72 ✓；supp(T)=W ✓；
  ‖T‖(f)=∫f d‖T‖=∫_W f dσ ✓；Proposition 3 (i)(ii) ✓
- 结果：**PASS**
## p.008（print 273：(iii) + Schwartz 引理 + Proposition 4）
- 核对：(iii) 代数超曲面次数 ≤m ✓；tangent cone C_a/P_m(z)=0/Γ_a ✓；Θ 两行 ✓；
  [2], Theorems 5.4.3 and 4.3.19/[7]/[6], p.397/Stoll [11]/(57) of Theorem 5 ✓；
  Schwartz' lemma 经典式 ✓；Proposition 4 |w|<τR/6n/log|F(w)|≤max−(1−τ)Θ log(τR/6n/|w|) ✓
- 结果：**PASS**
## p.009（print 274：Proposition 4 证明前半）
- 核对：d‖T‖=1/2πΔlog|F|∧ω_n ✓；U(z) 势 ✓；1/2πΔU 分段 ✓；Δ[log|F|−U]∧ω_n≥0 ✓；
  max/min 式 ✓；下界积分链五段逐行 ✓
- 结果：**PASS**
## p.010（print 275：useful inequality + §IV Existence Theorem）
- 核对：log|F(w)| 两行 ✓；Θ 非降/if t≥|w| ✓；三行链 ✓；(1−τ)log(τx/2n) ✓；
  IV 节/Existence Theorem ∫|F|²e^{−V}(1+|z|²)^{−3n}ω_n<+∞ ✓；Remarks（−∞/3n/L²/[3]/[4]
  Theorem 4.4.4/pp.116-117）✓
- 结果：**PASS**
## p.011（print 276：Hörmander 定理 + Ω₀/Ω_k）
- 核对：L²_{(p,q)}(Ω,V)/weighted norm/loc ✓；**Hörmander's Theorem 全文**（∃U∈L²_{(p,q−1)}(Ω,
  V+2log(1+|z|²)), ∂̄U=f, ∫|U|²e^{−V}(1+|z|²)^{−2}ω_n≤∫|f|²e^{−V}ω_n）✓；
  [3], Theorem 2.2.1′/[4], Theorem 4.4.2 ✓；Ω₀/Ω_k=Ω₀⊂Ω₁⊂⋯⊂Ωₙ=Cⁿ/W=log(1+|z|²) ✓
- 结果：**PASS**
## p.012（print 277：F_k 归纳构造 + Martineau）
- 核对：F_k(0)=1/‖F_k‖_{Ω_k,V+3kW}<+∞ ✓；F₀=1 ✓；∂̄F_k=0/‖F_k‖/F_k=F_{k−1} on {z_k=0} ✓；
  **Martineau [9]** ✓；ψ(ζ)（1 in |ζ|<½, 0 in |ζ|>1, C¹, |∂̄ψ|≤4）✓；ψ_k ✓；
  supp ψ_k⊂Ω_{k−1}/z_k^{-1}∂̄ψ_k∈C_{(0,1)}(Ω_k) ✓；f/|f|≤8|F_{k−1}| ✓；∃v/‖v‖ 链 ✓
- 结果：**PASS**
## p.013（print 278：F_k 验证 + §V 记号）
- 核对：F_k(z)=ψ_kF_{k−1}−z_kv/∂̄F_k=0/连续性/‖F_k‖ 链 ✓；V 节 den(α)/‖α‖=max|σα|/
  size(α)=max(log d, log|σα|) ✓；−2[K:Q]size(α)≤log|σα| ✓；
  −[K:Q]log den(α)−([K:Q]−1)size(α)≤log|σα| ✓；‖P‖/|P|/size(P) ✓
- 结果：**PASS**
## p.014（print 279：Lemma 1 + Lemma 2 + 有限阶脚注 1）
- 核对：Lemma 1 全文（(r+|k|)^{|k|} 代替 r^{|k|}|k|!；[5] Chapter IV §2 p.34/p.23）✓；
  Lemma 2（Siegel/Dirichlet box principle）‖X‖≤C₂(C_{2n}‖A‖)^{r/(n−r)} ✓；
  有限阶设定 + **脚注 1 全文**（"An entire function h(z) is of finite order ≤ρ if
  max log|h(z)|=O(R^{ρ+ε}); a quotient of two entire functions of order ≤ρ is meromorphic
  of order ≤ρ."）——md 碎成 4 个幽灵块 → 删除碎片（真脚注 md 本已完整）✓
- 结果：**FAIL（幽灵脚注 ×4）→已修**
## p.015（print 280：辅助函数 F + Lemma 3）
- 核对：F(z)=Σ_{(j)<J}a_{(j)}f₁^{j₁}…f_{d+1}^{j_{d+1}}/(j)<J ✓；D^λF(ζ)=0/‖a_{(j)}‖ ✓；
  ≪/O(⋯)/o(⋯) 记号 ✓；Lemma 3 J^{d+1}=[mL^d log L]/size(a_{(j)})≪L ✓；
  证明全链（((d+1)J+L)^L C₁^{…}/Δ/线性方程组/C₁^{2(d+1)J+2L}/r=m(L+d choose d)/
  n=J^{d+1}/r/(n−r)≪1/log L）✓
- 结果：**PASS**
## p.016（print 281：s=s(L) + Lemma 4 + §VI 开头）
- 核对：D^σF(ζ)=0 for |σ|<s/L≤s<+∞ ✓；g entire of order ≤ρ/G_s(z)=g(z)^{(d+1)J}F(z) ✓；
  Lemma 4 log|D^{σ′}G_s(ζ′)|≥−([K:Q]−1)s log s+O(s) ✓；证明 ξ∈K/两行不等式 ✓；
  VI 节 T_s=1/πs∂∂̄log|G_s|/Cauchy inequality ✓
- 结果：**PASS**
## p.017（print 282：Proposition 4 应用 + Lemma 5 + 弱极限）
- 核对：Θ(‖sT_s‖;r,0)=Θ·s ✓；两行上界 ✓；O(JR^{ρ+ε})/R=s^κ/κ<1/((d+1)ρ) ✓；
  Lemma 5 (i) ≤[(d+1)ρ+o(1)][K:Q] (ii) ≥1 ✓；Alaoglu-Bourbaki/弱极限 T ✓；
  ‖T_s‖Ω→‖T‖Ω/iT_s(φ_Ωω_{n−1}) ✓
- 结果：**PASS**
## p.018（print 283：Lemma 6 + Theorem A 策略 + 势 V(z)）
- 核对：Θ(‖T_s‖;r,a)→Θ(‖T‖;r,a)/lim̄ 两行 ✓；Lemma 6 (i)(ii) ✓；
  B(r−|a|,0)⊆B(r,a)⊆B(r+|a|,0) 两行 ✓；degree ≤d(d+1)ρ[K:Q]+2d ✓；
  1/r Θ(‖T‖;r,0) summable ✓；V(z)=(n−2)!/2π^{n−1}∫(1/|ζ|^{2n−2}−1/|ζ−z|^{2n−2})d‖T‖ ✓
- 结果：**PASS**
## p.019（print 284：V(z) 性质 + Lemma 7 证明前半）
- 核对：[6], Theorem 1, pp. 380-381 ✓；1/2πΔV∧ω_n=d‖T‖ ✓；Lelong [6], Theorem 3, p. 387 ✓；
  1/π∂∂̄V(z)=T ✓；Lemma 7 (i)(ii) ✓；≪|z|/|ζ|^{2n−1} ✓；V(z)≤ 两段 ✓；∫ 链三行 ✓；
  ‖T‖B(t,0)≤π^{n−1}/(n−1)!t^{2n−2}Θ(∞) ✓
- 结果：**PASS**
## p.020（print 285：Lemma 7 证明后半）
- 核对：∫_{|ζ|<|z|} 链四行 ✓；statement (1) ✓；(ii) 证明/ζ₀≠0/V(z)=−…+O(1) ✓；
  ≥(a+b)^{−2n−2} ✓；lower bound 三行链 ✓；Finally log 1/α+O(1) ✓；"(ii) of Lemma 7 is
  proved." ✓（md 句末句号齐全）
- 结果：**PASS**
## p.021（print 286：Theorem A 完成 + References [1]-[5]）
- 核对：κV/κ>2d/∫|F|²e^{−κV}(1+|z|²)^{−3d}ω_d<+∞ ✓；e^{−κV} not summable/Θ≥1 ✓；
  |F|²|z|^{−κΘ(∞)−6d−ε}/∫(1+|z|)^{−κΘ(∞)−6d−ε} ✓；**"polinomial of degree at most"**
  ——print 即此源级拼写（md 被 mineru 纠正为 polynomial → 还原 polinomial）✓；
  ½[κΘ(∞)+6d+ε]−d/Liouville/κ→2d ✓；**"degree ≤d(d+1)ρ[k:Q]+2d"——print 小写 k，源级
  （md 忠实）**✓；|P|=1/finiteness removed/compact ✓；References [1]-[5] 与 md 一致 ✓
- 结果：**FAIL（polinomial 还原）→已修**
## p.022（print 287：References [6]-[11] + 作者块 + Received）
- 核对：**md 止于 [5]——[6]-[11]+作者块+Received 整段丢失 → FAIL**；已按 print 逐条转录补入：
  [6] Lelong, J. d'Analyse Math. 12, 365-407 (1964)；[7] — Propriétés métriques, Ann. E.N.S.
  67, 393-419 (1950)；[8] — Fonctions plurisousharmoniques…, Gordon and Breach 1968；
  [9] Martineau, Inventiones Math. 2, 81-86 (1966), and Corrections, Inventiones Math. 3,
  16-19 (1967)；[10] Schneider, Math. Annalen 121, 131-140 (1949-1950)；[11] Stoll,
  Math. Annalen 156, 47-78 and 144-170 (1964)；Enrico Bombieri/Università di Pisa/
  Istituto Matematico "Leonida Tonelli"/Pisa, Italia；(Received June 29, 1970) ✓
- 结果：**FAIL（整段）→已修**

## 总评

- **覆盖声明**：22/22 页逐页目检（150dpi 全页；p.001 为 GDZ 封面非论文内容）；pdftotext 文本层
  仅 GDZ 元数据，按扫描件 SOP 纯 PNG 审计；600dpi 原扫描可按需放大复核。
- **FAIL 修复（4 类）**：①印刷页脚/装订签名串入正文 ×4（"19 Inventiones math., Vol. 10"/
  "19\*"/"20 Inventiones math., Vol. 10"/"20\*" 删除）；②脚注 1 幽灵碎片 ×4 删除（真脚注完整）；
  ③"polinomial" 源级拼写还原（mineru 误纠正为 polynomial）；④**References [6]-[11]+作者块+
  (Received June 29, 1970) 按 print 逐条转录补入**。
- **源级 quirk 清单（忠实不改）**："polinomial"；"ρ[k:Q]" 小写 k（定理 A 结论句）；
  Schneider 条目无人名缩写（print 即此）；[7][8] 的 dash 起首（Hörmander? 不——系 Lelong 续条）。
- **可用性结论**：修复后 md 可作该文忠实底本；正文 I-VI 全部公式逐行核对全对；参考文献 11 条
  现已齐全（[1]-[5] 原有 + [6]-[11] 补入）。本篇 22/22 页完成，无未决项；与
  Bombieri_1970_addendum（已审 ✅）及 1974 work report（已审 ✅）构成闭环。

### 修复登记（2026-09-30）
- **9 组替换全部命中**（页脚/签名 ×4、脚注碎片 ×4、polinomial 还原）+ References [6]-[11]+
  作者块+Received 整段转录补入；fix commit 见父提交链（audit(page) 即修复前 md 原貌）。
- 本篇 22/22 页完成，无未决项。
