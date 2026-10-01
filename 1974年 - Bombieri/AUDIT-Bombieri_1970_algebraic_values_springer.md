# AUDIT — E. Bombieri, "Algebraic Values of Meromorphic Maps"（Inventiones math. 10, 267-287 (1970)；**Springer PageGenie 扫描版**（Producer=PageGenie PDFGenerator, Creator=009042001.TIF，图像型扫描+OCR 文本层））

> mineru: standard 档导出 `Bombieri_1970_algebraic_values_springer_mineru/`；审计依据 = 二值化渲染
> `audit/springer_pNNN.png`（pngmono 150dpi）对照 md；疑点 300dpi（pnggray）终裁。
> **PDF 自带 OCR 文本层严重乱化（数学全部失真），不可作对账通道——按扫描件 SOP 纯 PNG 审计**。
> 同论文 GDZ 600dpi 扫描版已审（AUDIT-Bombieri_1970_algebraic_values.md，22 页含封面）；本版为同一
> 印刷版式的另一数字化件，其已仲裁判例（print 即权威项）作交叉参照，本版仍逐页独立目检。
> print 页码 = PDF p.N + 266（p.001=267 … p.021=287）。

## p.001（print 267：题录 + Theorem A + Remarks 1-2）
- PNG：audit/springer_p001.png（pngmono 150dpi）
- 核对：题录行 Inventiones math. 10, 267-287 (1970)/© Springer-Verlag（**md 缺期刊头，惯例**）；
  标题/ENRICO BOMBIERI (Pisa) ✓；Theorem A：(i) tr deg K(f)≧d+1（print 系 ≧，OCR 层的">"不可信，
  md \geq 正确）✓；(ii) ∂/∂z_α 映 K[f] 入自身 ✓；S⊂代数超曲面 ✓；Remark 1 d(d+1)ρ[K:Q]+2d ✓；
  Remark 2 ∂f_i/∂z_α=P_{iα}(f)Q(f)^{-1}/f_{N+1}=Q(f)^{-1}/f̃=(f_1,…,f_{N+1})/K[f̃]/Q(f(ζ))≠0 ✓；
  Lang [5]/Schneider [10]/cardinality ≦20ρ[K:Q] ✓
- 结果：**PASS±**（期刊头行丢弃；print 页脚"19 Inventiones math., Vol. 10"串入 md 行尾 → 待修）

## p.002（print 268：Lang 高维结果 + 致谢 + II 节开头）
- PNG：audit/springer_p002.png
- 核对：min card S_α≦bρ[K:Q]（print α 下标+≦，md ✓）；historical note 引文全段逐句 ✓；
  C^d/Lelong/Carleman/Andreotti-Vesentini [1]/Hörmander [4] ✓；致谢 Serge Lang/Norberto Kerzman ✓；
  节标题 II. Positive (1,1)-Currents in Cⁿ ✓；D(Ω)/(n-1,n-1)-forms ✓；
  φ=Σφ^{αβ̄}(dz_1∧dz̄_1∧⋯∧dz_n∧dz̄_n)_{α,β̄}^ ✓；comass ‖φ‖=2^{n-1}sup_{α,u}|Σ_{pq}u_{αp}ū_{αq}φ^{pq̄}| ✓；
  |φ|=sup_{p,q}|φ^{pq̄}| ✓；SU(n) ✓
- 结果：**PASS±**（页码/running head "268 E. Bombieri:" 丢弃，惯例；φ 上标 bar 位置 150dpi 不可分辨 → 疑点 A 待 300dpi）

## p.003（print 269：质量范数 + Prop 1 + 密度定义）
- PNG：audit/springer_p003.png
- 核对：‖φ‖_Ω=sup_Ω‖φ‖ ✓；T=Σt_{αβ̄}dz_α∧dz̄_β ✓；‖T‖(f)=sup_φ|T(φ)| ✓；ω=(i/2)Σdz_α∧dz̄_α ✓；
  ω_k=(1/k!)ω^k ✓；‖ω_{n-1}‖=1 ✓；(Σt_{αβ̄}w_αw̄_β)∧ω_n 正性定义 ✓；t_{αβ̄}=t̄_{β̄α} ✓；
  **Prop 1：d‖T‖=iT∧ω_{n-1}=2(Σt_{αᾱ})∧ω_n（print 系数 2 无 i，md 忠实）✓**；[2], p.652 ✓；
  ‖T‖Ω=∫_Ω d‖T‖ ✓
- 结果：**PASS**（running head/页脚 19\* 丢弃，惯例）

## p.004（print 270：Θ 定义 + Prop 2 + Stokes 准备）
- PNG：audit/springer_p004.png
- 核对：B(r,a)=|z-a|<r ✓；Θ(‖T‖;r,a)=(n-1)!/π^{n-1}r^{2n-2}·‖T‖B(r,a) ✓；Θ(‖T‖;a)=lim_{r→0} ✓；
  Θ*/Θ_* ✓；∂̄-closed/∂̄T(φ)=-T(∂̄φ)/Ω 版 ✓；Prop 2 单调非降+密度存在有限 ✓；
  [8], p.73 and [2], pp.621 and 652 ✓；(1/2π)∂∂̄log|z| Levi 正定 ✓；
  iT∧((i/2π)∂∂̄log|z|)^{n-1} 正测度 ✓；∫_{B(R,a)∖B(r,a)}…=Θ(R,a)-Θ(r,a) ✓；0<r<R<+∞ ✓
- 结果：**PASS**（running head 丢弃，惯例）

## p.005（print 271：S 构造 + Stokes + III 节开头）
- PNG：audit/springer_p005.png
- 核对：∂̄T=0 ⟹ iT=∂̄S ✓；S(∂̄φ)=-iT(φ) ✓；
  ∂̄S∧((i/2π)∂∂̄log|z|)^{n-1}=∂̄[S∧((i/2π)∂∂̄log|z|)^{n-1}] ✓；
  Stokes 两边界积分差式 ✓；((i/2π)∂∂̄log|z|)^{n-1}=(n-1)!/π^{n-1}r^{2n-2}ω_{n-1} on ∂B(r,a) ✓；
  三行 ∫ 链（∂B→S∧ω_{n-1}→iT∧ω_{n-1}→d‖T‖）✓；
  **"because ∂̄ω=0 hence ∂̄(iT∧ω_{n-1})=S∧ω_{n-1}"——print 原文即此**（按 Stokes 应为
  ∂̄(S∧ω_{n-1})=iT∧ω_{n-1}，print 笔误；GDZ 同版式已判"md 忠实"）→ **源级 quirk 忠实保留**；
  III 节标题/psh 定义/T=∂∂̄V 正 current ✓
- 结果：**PASS±**（print 笔误 1 处忠实保留并登记；running head 丢弃惯例）

## p.006（print 272：Poincaré-Lelong + Prop 3 (i)(ii)）
- PNG：audit/springer_p006.png
- 核对：T=∂∂̄V=(1/π)∂∂̄log|F| ✓；V=(1/π)log|F| ✓；iT(φ)=∫_W φ ✓；F(z)=0/[8], p.72 ✓；
  supp(T)=W ✓；‖T‖(f)=∫_{Cⁿ}fd‖T‖=∫_W fdσ ✓；Prop 3 头 T=(1/π)∂∂̄log|F| ✓；
  (i)"the order of zero of a for F(z)"（print 原文语序即此，md 忠实）✓；F(a)≠0 ⟹ Θ=0 ✓；
  (ii) lim_{r→∞}Θ(‖T‖;r,a)=m ✓
- 结果：**PASS**（running head 丢弃，惯例）

## p.007（print 273：Prop 3(iii) + 切锥 + Prop 4）
- PNG：audit/springer_p007.png
- 核对：(iii) 代数超曲面次数≦m ✓；C_a 切锥/P_m(z)=0 ✓；Γ_a=(1/π)∂∂̄log|P_m(z)| ✓；
  Θ(‖T‖;a)=Θ(‖Γ_a‖;0)=Θ(‖Γ_a‖;r,0) 双行 ✓；[2], Theorems 5.4.3 and 4.3.19 ✓；
  (ii) in [7]/[6], p.397 ✓；(iii) Stoll [11]/(57) of Theorem 5 ✓；Schwartz' lemma ✓；
  经典式 |F(w)|≦(|w|/R)^m max ✓；Prop 4 头（|z|≦R/0<τ<1）✓；
  **|w|<τR/6n 与 log(τR/6n/|w|)——print 即 6n，md 忠实** ✓
- 结果：**PASS**（running head 丢弃，惯例）

## p.008（print 274：Prop 4 证明前半 + 分部积分长链）
- PNG：audit/springer_p008.png
- 核对：d‖T‖=(1/2π)Δlog|F(z)|∧ω_n ✓；n≧2 假设 ✓；U(z)=-(n-2)!/2π^{n-1}∫_{|ζ|<R/3}d‖T‖/|ζ-z|^{2n-2} ✓；
  (1/2π)ΔU∧ω_n={d‖T‖/0} 分段 ✓；Δ[log|F|-U]∧ω_n≧0 ✓；log|F(w)|≦max-min∫ 两行 ✓；
  五行长链（≧∫[1/(|ζ|+|w|)^{2n-2}-…]=∫₀^{R/3}…=[…R/3,0]‖T‖B(R/3,0)+(2n-2)∫[…+…]‖T‖B(t,0)dt）
  逐行 ✓；
  **末行 print 原文即 ≧(2n-2)∫₀^{R/3}‖T‖B(t,0)/(t-|w|)^{2n-1}dt**（下一行有用不等式走 (t+|w|)，
  此行疑似 print 笔误但 GDZ 同版式同文同"✓"判例）→ **源级忠实保留 + 登记**
- 结果：**PASS±**（print 疑似笔误 1 处忠实保留；running head 丢弃惯例）

## p.009（print 275：有用不等式 + Prop 4 证毕 + IV 节 Existence Theorem）
- PNG：audit/springer_p009.png
- 核对：log|F(w)|≦max-∫₀^{R/3}(t/(t+|w|))^{2n-2}Θ(‖T‖;t,0)/(t+|w|)dt ✓（此行 print 系 t+|w|，
  与 p.274 末行 t-|w| 不自洽——登记见 p.008）；
  Θ(‖T‖;t,0)≧Θ(‖T‖;|w|,0) if t≧|w| ✓；三行链（∫₀^{R/3}≧Θ(|w|)∫_{|w|}^{R/3}=Θ(|w|)∫₁^{R/3|w|}(t/(t+1))^{2n-2}dt/t）✓；
  ∫₁^x(t/(t+1))^{2n-2}dt/t≧(1-τ)log(τx/2n)——**print 即 2n，与 Prop 4 陈述的 6n 差 3 倍系
  R/3 积分上限自带因子，两者自洽** ✓；IV 节标题 ✓；Existence Theorem ∫|F|²e^{-V}(1+|z|²)^{-3n}ω_n<+∞ ✓；
  Remarks（V 可取 -∞/V=const 例/3n 不能低于 n）✓；Hörmander [3]/[4] Thm 4.4.4/pp.116-117 ✓
- 结果：**PASS**（running head 丢弃，惯例）

## p.010（print 276：Hörmander 定理 + 多圆柱构造）
- PNG：audit/springer_p010.png
- 核对：L²_{(p,q)}(Ω,V) 定义/f=Σf_{I,J}dz_I∧dz̄_J/加权范数 ✓；L²(Ω,loc) Fréchet ✓；
  Hörmander's Theorem 全文（pseudoconvex/q≧1/∂̄f=0/U∈L²(V+2log(1+|z|²))/∂̄U=f/
  ∫|U|²e^{-V}(1+|z|²)^{-2}ω_n≦∫|f|²e^{-V}ω_n）✓；[3] Thm 2.2.1'/[4] Thm 4.4.2 ✓；
  Ω_0 polycilinder（print 拼法 polycilinder，md 忠实）✓；Ω_k={|z_{k+1}|<1,…} ✓；
  Ω_0⊂Ω_1⊂⋯⊂Ω_n=Cⁿ ✓；W=log(1+|z|²) psh ✓
- 结果：**PASS**（running head 丢弃，惯例）

## p.011（print 277：F_k 归纳构造 + Martineau + ψ 截断）
- PNG：audit/springer_p011.png
- 核对：F_k(0)=1/‖F_k‖_{Ω_k,V+3kW}<+∞ ✓；F_0=1 in Ω_0/e^{-V} 可积 ✓；
  ∂̄F_k=0/‖F_k‖<+∞/F_k=F_{k-1} on Ω_k∩{z_k=0} ✓；Martineau [9] ✓；
  ψ（1 in |ζ|<½，0 in |ζ|>1，C¹，|∂̄ψ|≦4）✓；ψ_k(z)=ψ(z_k) ✓；supp ψ_k⊂Ω_{k-1} ✓；
  z_k^{-1}∂̄ψ_k∈C_{(0,1)}(Ω_k) ✓；f=z_k^{-1}F_{k-1}∂̄ψ_k/supp f⊂Ω_{k-1}/∂̄f=0 ✓；|f|≦8|F_{k-1}| ✓；
  ‖f‖_{Ω_k,V+3(k-1)W}<+∞ ✓；∂̄v=f/‖v‖_{Ω_k,V+(3k-1)W}≦‖f‖_{Ω_k,V+3(k-1)W}<+∞ ✓
- 结果：**PASS**（running head 丢弃，惯例）

## p.012（print 278：F_k 证毕 + V 节记号与基本不等式）
- PNG：audit/springer_p012.png
- 核对：[4] Theorem 4.2.5/v 连续 ✓；F_k=ψ_kF_{k-1}-z_kv ✓；∂̄F_k=F_{k-1}∂̄ψ_k-z_k∂̄v=0 ✓；
  F_k=F_{k-1} on Ω_k∩{z_k=0} ✓；范数两行归纳链 ✓；V. Auxiliary Lemmas ✓；den(α) ✓；
  ‖α‖=max_σ|σα| ✓；size(α)=max(log d, log|σα|) ✓；
  -2[K:Q]size(α)≦log|σα| ✓；-[K:Q]log den(α)-([K:Q]-1)size(α)≦log|σα| ✓；
  P=Σa_jT^j/T^j ✓；‖P‖/|P|/size(P)=max(deg P, log‖P‖) ✓
- 结果：**PASS**（running head 丢弃，惯例）

## p.013（print 279：Lemma 1 + Lemma 2 + 正文 setup + 足注 1）
- PNG：audit/springer_p013.png
- 核对：Lemma 1 全文（K[f] 映入自身/f(ζ)∈K^N/deg Q≦r/D^k=∏D_i^{k_i}/
  ‖D^k(Q(f))(ζ)‖≦‖Q‖(r+|k|)^{|k|}C_1^{|k|+r}/den≦C_1^{|k|+r}）✓；
  Proof：[5] Ch IV §2 p.34/**"instead of r^{|k|}|k|!"（print 有 "！"）——md L647 无 "！" → 疑点 B**；
  [5] Ch IV §2 p.23/d=1 ✓；Lemma 2（AX=0/r×n/O_K/n>r/
  ‖X‖≦C_2(C_{2n}‖A‖)^{r/(n-r)}）✓；Siegel/Dirichlet/[5] Ch I §2 Lemma 2 ✓；
  setup：finite order¹≦ρ/tr deg K(f)≧d+1/f_1,…,f_{d+1} 代数无关 ✓；S={ζ_i}, i=1,…,m ✓；
  足注 1 全文（max_{|z|=R}log|h(z)|=O(R^{ρ+ε})/quotient…meromorphic）✓（md 足注 span 文本吻合）
- 结果：**PASS±→疑点 B 待 300dpi 终裁**（若证实 print 带 "！" 则 FAIL 修复补入）

## p.014（print 280：F(z) 辅助函数 + Lemma 3 全文）
- PNG：audit/springer_p014.png
- 核对：F(z)=Σ_{(j)<J}a_{(j)}f_1^{j_1}…f_{d+1}^{j_{d+1}} ✓；(j)<J 定义 ✓；D^λF(ζ)=0, |λ|<L ✓；
  ≪/O(·)/o(·) 约定 ✓；**Lemma 3：J^{d+1}=[mL^d log L]/size(a_{(j)})≪L** ✓；
  ‖D^λf_1^{j_1}…f_{d+1}^{j_{d+1}}(ζ)‖≦((d+1)J+L)^L C_1^{(d+1)J+L} ✓；Δ≦C_1^{(d+1)J+L} ✓；
  m(L+d∥d) 线性方程组 ✓；
  **Σa_{(j)}(Δ·D^λf_1^{j_1}…f_{d+1}^{j_{d+1}}(ζ))=0——print 上标小写 j_{d+1}，md L728 误作大写
  f_{d+1}^{Jd+1} → 疑点 C 待修**；‖Δ·D^λ…‖≦((d+1)J+L)^L C_1^{2(d+1)J+2L} ✓；
  size=log‖‖≪(r/(n-r)){L log(L+J)+J} ✓；r=m(L+d∥d)/n=J^{d+1} ✓；
  J^{d+1}=[mL^d log L]/r/(n-r)≪1/log L ✓
- 结果：**PASS±→疑点 C 待修**（j_{d+1} 大小写错，内容级）

## p.015（print 281：s(L) 定义 + Lemma 4 + VI 节开头）
- PNG：audit/springer_p015.png
- 核对：s=s(L) 定义（D^σF(ζ)=0, |σ|<s；∃σ',|σ'|=s 使 D^{σ'}F(ζ')≠0）✓；L≦s<+∞ ✓；
  s=+∞ ⟹ F≡0 与代数独立矛盾 ✓；g 整函数 order≦ρ/gf_j 整 ✓；G_s=g^{(d+1)J}F ✓；
  Lemma 4（log|D^{σ'}G_s(ζ')|≧-([K:Q]-1)s log s+O(s)）✓；
  Proof（=g^{(d+1)J}D^{σ'}F/ξ∈K≠0/≧O(J)-([K:Q]-1)size(ξ)+O(log den(ξ))）✓；
  由 Lemma 1,3 得 ✓；VI 节标题 ✓；T_s=(1/πs)∂∂̄log|G_s(z)| ✓；Cauchy 不等式 + r>|ζ'| ✓
- 结果：**PASS**（running head 丢弃，惯例）

## p.016（print 282：Prop 4 应用 + κ 取法 + Lemma 5）
- PNG：audit/springer_p016.png
- 核对：Θ(‖sT_s‖;r,0)=Θ(‖T_s‖;r,0)·s ✓；
  log|D^{σ'}G_s(ζ')|≦s log s+O(s)+max-（1-τ)Θ(‖T_s‖;r,0)s·**log(τR/2nr)——print 即 2nr，md 忠实**
  （print 自身 Prop 4 陈述用 6n、此处用 2n，print 内部差异照实登记）；
  O(JR^{ρ+ε}) ✓；R=s^κ/κ<1/(d+1)ρ ✓；max=o(s log s) for large R ✓；
  界：≦s log s+o(s log s)-(1-τ)κΘ(‖T_s‖;r,0)[s log s+O(s)] ✓；
  **Lemma 5：(i) Θ(‖T_s‖;r,0)≦[(d+1)ρ+o(1)][K:Q]（print 即此）✓；(ii) Θ(‖T_s‖;ζ)≧1** ✓；
  Θ(‖sT_s‖;ζ)≧s/Prop 3,(i) ✓；Alaoglu-Bourbaki/弱极限 T 正且 ∂、∂̄-closed ✓；
  ‖T_s‖Ω→‖T‖Ω ✓；‖T_s‖Ω=iT_s(φ_Ω ω_{n-1})/φ_Ω 特征函数 ✓
- 结果：**PASS**（running head 丢弃，惯例）

## p.017（print 283：弱极限细节 + Lemma 6 + Theorem A 归约）
- PNG：audit/springer_p017.png
- 核对：φ_Ω 与 s 无关 ✓；Θ(‖T_s‖;r,a)→Θ(‖T‖;r,a) ✓；
  limsup Θ(‖T_s‖;ζ)≦Θ(‖T‖;ζ) 及两行依据 ✓；Prop 2 复用 ✓；
  **Lemma 6：(i) Θ(‖T‖;r,a)≦(d+1)ρ[K:Q]（print 无 o(1)）✓；(ii) Θ(‖T‖;ζ)≧1** ✓；
  B(r-|a|,0)⊆B(r,a)⊆B(r+|a|,0) ✓；(1∓|a|/r)^{2n-2}Θ 双向 ✓；r→+∞/Prop 2 ✓；
  **"S lies in a algebraic hypersurface"——print 原文即 "a algebraic"（语法 quirk，md 忠实）**，
  degree≦d(d+1)ρ[K:Q]+2d ✓；
  (1/r)Θ(‖T‖;r,0) summable at the origin（print 即此，md 忠实）✓；
  V(z)=(n-2)!/2π^{n-1}∫_{ζ∈Cⁿ}(1/|ζ|^{2n-2}-1/|ζ-z|^{2n-2})d‖T‖ ✓
- 结果：**PASS±**（print 页脚"20 Inventiones math., Vol. 10"串入 md 行尾 → 待修；print 语法 quirk 忠实）

## p.018（print 284：V(z) 性质 + Lemma 7 (i) 证明）
- PNG：audit/springer_p018.png
- 核对：[6] Theorem 1, pp.380-381/(1/r)Θ summable at r=0 ✓；(1/2π)ΔV∧ω_n=d‖T‖ ✓；
  subharmonic in C^d/Lelong [6] Thm 3 p.387/supp(T) 条件与弱条件 ✓；(1/π)∂∂̄V=T ✓；plurisubharmonic ✓；
  **Lemma 7：(i) V(z)≦[1+o(1)]Θ(‖T‖;∞,0)log|z| ✓；(ii) V(z)≦-[1+o(1)]Θ(‖T‖;ζ)log(1/|z-ζ|)** ✓；
  Θ(∞)=Θ(‖T‖;∞,0) ✓；≪|z|/|ζ|^{2n-1}, |ζ|>|z| ✓；
  V(z)≦(n-2)!/2π^{n-1}∫_{|ζ|<|z|}+O(|z|∫_{|ζ|>|z|}) ✓；
  四行链：∫_{|ζ|>|z|}|ζ|^{-(2n-1)}=∫_{|z|}^∞t^{-(2n-1)}d‖T‖B(t,0)=-(1/|z|^{2n-1})‖T‖B(|z|,0)
  +(2n-1)∫_{|z|}^∞**‖T‖B(t,0)/t^?dt**——**print 指数 150dpi 难辨（疑点 D：t^n vs t^{2n}，
  由分部积分与末行 t^{-2} 收尾推应为 2n）→ 300dpi 终裁**；
  ‖T‖B(t,0)≦π^{n-1}/(n-1)!·t^{2n-2}Θ(∞)/∫t^{-2}dt=O(1/|z|) ✓
- 结果：**PASS±→疑点 D 待 300dpi 终裁**

## p.019（print 285：Lemma 7 证明 (i) 收尾 + (ii) 证明）
- PNG：audit/springer_p019.png
- 核对：四行 ∫ 链（∫₀^{|z|}t^{-(2n-2)}=≦‖T‖B(|z|,0)/|z|^{2n-2}+(2n-2)∫₀^{|z|}‖T‖B(t,0)/**t^{2n-1}**dt
  =O(1)+(2n-2)∫₁^{|z|}π^{n-1}/(n-1)!·Θ(‖T‖;t,0)/t dt≦(2n-2)π^{n-1}/(n-1)!·Θ(∞)log|z|+O(1)）
  ✓（此处 print 分母清晰为 t^{2n-1}——佐证疑点 D 的 p.284 行应为 t^{2n}）；
  "prove statement (1)"（print 原文即数字 (1)，指 (i)，md 忠实）✓；
  V(z)=-(n-2)!/2π^{n-1}∫_{|ζ-ζ_0|<1}+O(1) ✓；1/|ζ-z|^{2n-2}≧1/(|ζ-ζ_0|+|z-ζ_0|)^{2n-2} ✓；
  下界三行链（=O(1)+(2n-2)∫‖T‖B(t,ζ_0)/(t+|z-ζ_0|)^{2n-1}dt≧O(1)+2π^{n-1}/(n-2)!·Θ(‖T‖;ζ_0)∫t^{2n-2}/(t+|z-ζ_0|)^{2n-1}dt）✓；
  Finally：∫₀¹t^{2n-2}/(t+α)^{2n-1}dt=∫_α^{1+α}(t-α)^{2n-2}/t^{2n-1}dt=∫dt/t+O(α∫dt/t²)=log(1/α)+O(1) ✓；
  (ii) of Lemma 7 proved ✓
- 结果：**PASS**（print 页脚 20\* 串入 md → 待修；running head 丢弃惯例）

## p.020（print 286：Theorem A 完成 + References [1]-[5]）
- PNG：audit/springer_p020.png
- 核对：κV/κ>2d ✓；∫_{C^d}|F|²e^{-κV}(1+|z|²)^{-3d}ω_d<+∞ ✓；e^{-κV} not summable/Θ≧1/F 零点 ✓；
  |F|²|z|^{-κΘ(∞)-6d-ε} ✓；∫(1+|z|)^{-κΘ(∞)-6d-ε}ω_d<+∞ ✓；
  **"F is a polinomial of degree at most"——print 确为 polinomial（md 被 mineru 纠正为 polynomial
  → FAIL 修复：还原 polinomial；同 GDZ 版判例）**；½[κΘ(∞)+6d+ε]-d ✓；
  Liouville/ε→0/κ→2d/Lemma 6 ✓；第二个实例 print 即 "poly-nomial"（正常连字换行，md polynomial 不改）✓；
  **degree≦d(d+1)ρ[k:Q]+2d——print 小写 k，源级（md 忠实）** ✓；|P|=1 ✓；
  finiteness removed/compact/bound 不依赖 S ✓；References [1]-[5] 逐条与 md 一致 ✓
- 结果：**FAIL（polinomial 还原）→待修**

## p.021（print 287：References [6]-[11] + 作者块 + Received）
- PNG：audit/springer_p021.png
- 核对：**md 止于 [5]——[6]-[11]+作者块+Received 整段丢失 → FAIL**；print 逐条：
  [6] Lelong, P.: Fonctions entières (n variables) et fonctions plurisousharmoniques d'ordre
  fini dans Cⁿ. J. d'Analyse Math. 12, 365-407 (1964)；[7] — Propriétés métriques des variétés
  analytiques complexes définies par une équation. Ann. E.N.S. 67, 393-419 (1950)；
  [8] — Fonctions plurisousharmoniques et formes différentielles positives. New York:
  Gordon and Breach 1968；[9] Martineau, A.: Indicatrices de croissance des fonctions entières
  de N-variables. Inventiones Math. 2, 81-86 (1966), and Corrections. Inventiones Math. 3,
  16-19 (1967)；[10] Schneider: Ein Satz über ganzwertige Funktionen als Prinzip für
  Transzendenzbeweise. Math. Annalen 121, 131-140 (1949-1950)（**无人名缩写，print 即此**）；
  [11] Stoll, W.: The growth of the area of a transcendental analytic set. Math. Annalen 156,
  47-78 and 144-170 (1964)；Enrico Bombieri/Università di Pisa/Istituto Matematico
  "Leonida Tonelli"/Pisa, Italia；(Received June 29, 1970)
- 结果：**FAIL（整段丢失）→按 print 转录补入**

## 总评

- **覆盖声明**：21/21 页逐页目检（150dpi pngmono 全览 + 4 处 300dpi 仲裁裁片）；PDF 自带 OCR
  文本层数学严重失真，不可作对账通道，按扫描件 SOP 纯 PNG 审计；同印刷版式的 GDZ 600dpi 版
  （AUDIT-Bombieri_1970_algebraic_values.md）已审，其 print 即权威判例作交叉参照（本版独立逐页
  目检，未照搬其结论——(t-|w|) 长链、6n/2n、"a algebraic"、statement (1)、ρ[k:Q] 小写 k 等均在本版
  页面上重新证实）。
- **FAIL 修复（3 类）**：①"F is a polynomial"→还原 print 拼写 "polinomial"（p.286，mineru 误纠正）；
  ②References [6]-[11]+作者块+(Received June 29, 1970) 整段按 print 转录补入；③页脚/装订签名串入
  正文 ×3（"19 Inventiones math., Vol. 10"/"20 Inventiones math, Vol. 10"/"20\*" 删除）+
  docvortex 足注幽灵碎片 ×5 删除（真足注 1 保留）。
- **内容级修复（300dpi 终裁后定）**：疑点 A（comass φ 上标 bar 位置）、疑点 B（r^{|k|}|k|! 的 "！"）、
  疑点 C（f^{Jd+1}→f^{j_{d+1}}）、疑点 D（t^n→t^{2n}）。
- **源级 quirk 清单（忠实不改）**：p.271 "∂̄(iT∧ω_{n-1})=S∧ω_{n-1}"（print 笔误，按 Stokes 应为
  ∂̄(S∧ω_{n-1})=iT∧ω_{n-1}）；p.274 长链末行 (t-|w|)^{2n-1}（与 p.275 有用不等式的 (t+|w|) 不自洽，
  疑 print 笔误）；Prop 4 用 τR/6n 而应用式用 τR/2nr（print 内部差异）；p.272 Prop 3(i) "the order
  of zero of a for F(z)"（print 语序）；p.283 "a algebraic hypersurface"（print 语法）；
  "prove statement (1)"（print 以数字指 (i)）；"ρ[k:Q]" 小写 k（定理 A 结论句）；"polinomial"
  （定理 A 结论）；[10] Schneider 无人名缩写；[7][8] dash 起首（Lelong 续条）；"polycilinder"（print 拼法）。
- **可用性结论**：修复后 md 可作该文忠实底本；正文 I-VI 全部公式逐行核对；参考文献 11 条齐全。
  本篇 21/21 页完成；与 GDZ 版（已审 ✅）、Addendum（已审 ✅）、1974 work report（已审 ✅）构成闭环。

### 300dpi 终裁记录（audit/300dpi/ 入库）

- **疑点 A（p.002 comass）**：p002_comass_zoom_300dpi.png（3x）证实 print 指数为 **φ^{p̄q}**（bar 在 p）；
  同页定义式 φ^{αβ̄}（bar 在 β）与 ‖φ‖=sup 行 φ^{pq̄}（bar 在 q）经 p002_phidef/supzoom_300dpi.png
  证实均 md 原样正确——**print 自身 bar 位置不一致**（comass 式 vs 同页另两处），照 print 修 comass 式
  并登记 quirk。
- **疑点 B（p.013）**：p013_insteadof_300dpi.png 证实 print 为 "instead of **r^{|k|}|k|!**"（带 ！）
  → md 补 "！"（FAIL 修复）。
- **疑点 C（p.014）**：p014_sigma_zoom_300dpi.png（3x）证实 Σ 式上标为小写 **j_{d+1}**（与 f_1^{j_1}
  同形；次行 "J^{d+1} unknowns" 的大写 J 明显异形）→ md f^{Jd+1} 改 f^{j_{d+1}}（FAIL 修复）。
- **疑点 D（p.018）**：p018_chain_300dpi.png 证实 print 分母即 **t^n**（与 p.285 平行式的 t^{2n-1}
  不一致，且与末行 t^{-2} 收尾在数学上不自洽，疑 print 应为 t^{2n}）——**print 即权威，md t^n
  忠实不改**，源级登记（GDZ 版 md 同位置亦 t^n，两 md 一致）。

### 修复登记（2026-09-30）

- **11 组规则全部命中（applied 11 / missed 0 / skipped 0），终验 19/19 PASS**：
  ①页脚/装订签名串入 ×3 删除（"19 Inventiones math., Vol. 10"/"20 Inventiones math, Vol. 10"/"20\*"）；
  ②docvortex 幽灵碎片 ×5 删除（真足注 $^{1}$ span 保留）；③r^{|k|}|k|! 补 ！；④f^{Jd+1}→f^{j_{d+1}}；
  ⑤comass 指数 φ^{pq̄}→φ^{p̄q}（bar 归位）；⑥polynomial→polinomial（print 拼写还原）；
  ⑦References [6]-[11]+作者块+Università di Pisa/(Received June 29, 1970) 整段按 print 转录补入。
- fix(md) commit 的父提交 = 修复前 md 原貌（audit(page) 提交不含 md 改动）。
- **源级 quirk 新增登记**：comass φ^{p̄q} vs 同页 φ^{pq̄}（print 自身不一致）；t^n（p.284）vs
  t^{2n-1}（p.285 平行式）（print 自身不一致）。
- 本篇 21/21 页完成，无未决项；修复脚本 /tmp/bombieri_springer_pub/fix_md.py（收敛式，转义三铁律遵守）。
