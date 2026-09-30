# AUDIT — G. Faltings《Endlichkeitssätze für abelsche Varietäten über Zahlkörpern》（Invent. math. 73, 349-366 (1983)，300dpi CCITT 扫描件 + OCR 噪声文本层，18p）

> mineru: standard 档云端解析（自行 OCR，德文转写质量高）。**审计依据 = `audit/faltings1983_pNNN.png`
> （pngmono 150dpi 全 18 页）+ 300dpi 局部放大 20 余处终裁**；pdftotext 文本层系 1983 年 Springer
> OCR 残留（ü→fi、ß→b/g、ö→6、π→rc、v→y），**仅作定位、不作对账依据**（BFO 扫描族 SOP）。
> **伪影族**：fraktur 𝖹→"3"（×17）、Λ^g→A^g（×3）、ℙ→IP/\mathbb{IP}（×7）、𝕫 丢 tilde（Ind 上标）、
> bold ℤ→blackboard ℤ 归一（×15）、V₁→V_l（§6 块 ×8）、𝔖/𝔻 丢 fraktur、A^m→Λ^m、
> besitz/双括号/双$粘连等 ~10 处、**Literatur [4]-[16]+Oblatum 整段丢失（P18）**。

## p.001（print 349：题录 + §1 Einleitung）
- 核对：题名/作者/Wuppertal 地址 ✓；π=Gal(K̄/K)/Tate-Modul 逆极限 ✓；a) T_l⊗_ℤ_l ℚ_l halbeinfach
  （bold ℤ→ℤ 已修）/b) End_K(A)⊗_ℤℤ_l→End_π(T_l(A)) ✓/c) Shafarevich ✓；Tate/Zarhin [15,16]/
  Arakelov [2]/[5] ✓；„alles" hermitesche Metriken ✓
- 结果：**PASS±**（±：bold ℤ 归一；刊头页眉未收）
## p.002（print 350：Gutachter 致谢 + 脚注 + §2 半阿贝尔簇）
- 核对：Gutachter/„Inventiones" 致谢 ✓；Szpiro/Deligne 脚注（小字）✓；§2 Definition ✓；
  Beispiel J=Pic^τ(C/S)→S [4] ✓；Lemma 1（p₁/p₂/φ: A₁/U→A₂/U）✓；Beweis（noethersch/
  exzellent/X⊆A₁×ₛA₂——print 下标 s 即此，忠实/pr₁ 同构/"tausend andere Arten"）✓；
  Definition ω_{A/S} 前置 ✓
- 结果：**PASS**
## p.003（print 351：ω 定义 + Bemerkungen + algebraic stacks + 𝔄_g 事实 a)/b)）
- 核对：ω_{A/S}=s*(Ω^g) ✓；b) 基变换 ✓；c) **Λ^g q_*(ω_{C/S})**（md "A^g" → FAIL 已修）✓；
  d) Γ(A,Ω^g_{A/ℂ})/⟨α,β⟩=(i/2)^g∫α∧β̄ ✓；„universelle Objekt zu 𝔖"（md 丢 fraktur+引号乱 → 已修）✓；
  M̄_g/𝔄_g ✓；a) (ω)^{⊗r} ample/ℙ^N_ℚ、ℙ^N_ℤ（IP→ℙ 已修）✓；b) **"über ℂ"**（md ℂ^s → FAIL 已修）/
  φ: 𝔑→Ā_g/ℂ ✓
- 结果：**FAIL（四点）→已修**
## p.004（print 352：Lemma 2 + Beweis + Korollar 头）
- 核对：**fraktur 𝖹（stack 名）**——300dpi 确认为 fraktur 大写 Z；md 混用 "3"/𝔷 → 统一 \mathfrak{Z}
  （**×17 FAIL 已修**）；𝔘⊂𝔷/ψ̄: 𝔷/ℚ→Ā_g/ℚ ✓；a) q: C→𝔷 ✓；b) **ℒ⊆Λ^g q_*(ω_{C/ℤ})**
  （A^g → FAIL 已修；ω_{C/Z}→ω_{C/ℤ} 已修）✓；c) α/β/α∘β=d·id ✓；d) ℒ^{⊗r}=ψ̄*(ℳ)/
  α*: ψ*(ω_{A/𝔄_g})→Λ^g q_*（md 𝔘_g → FAIL 已修）✓；Beweis（M̄_{g̃}/Kandidaten/Normalisierung/
  𝔷̃/ℂ）✓
- 结果：**FAIL（fraktur 族 ×12+）→已修**
## p.005（print 353：Korollar + Beweis + §3 Höhen 开头）
- 核对：Korollar：p: A→Spec(R)/ρ: Spec(K)→A_g/ℚ/ρ: Spec(R)→Ā_g/ℤ（print 无 bar——**源级，忠实**）✓；
  ρ*(ℳ)≅(ω)^{⊗r}/e·ρ*(ℳ)⊆(ω)^{⊗r}⊆e^{-1}·ρ*(ℳ) ✓；Beweis：ψ̄: 𝔷/ℤ→Ā_g/ℤ/K'⊇K/ρ̃: Spec(R')→𝔷
  （"3"→已修）✓；e₁·ℒ^{⊗r}⊆ψ̄*(ℳ)⊆e₁^{-1}·ℒ^{⊗r} ✓；α∘β=d·id/d^g·ρ̄*(ℒ)⊆ω⊆ρ̄*(ℒ)
  （ρ̄ 此处有 bar——print 如此）✓；**"bestitzt"**——300dpi 确认 print 即此（源级 typo，忠实）✓；
  §3：metrisiertes Geradenbündel/ε_v=1 oder 2 ✓
- 结果：**PASS±**（±：bestitzt 源级；ρ 无 bar 源级）
## p.006（print 354：Grad 公式 + h(A) 定义 + 高度讨论）
- 核对：Grad(P,‖·‖)=log(#(P/R·p))−Σε_v log‖p‖_v ✓；**h(A)=+1/[K:ℚ]·Grad(ω_{A/R})**
  （300dpi 确认**无负号**；md 正确）✓；x∈ℙⁿ(K)/ρ: Spec(R)→ℙⁿ_ℤ/ℙⁿ_ℂ（IP→ℙ、bold ℤ→ℤ 已修）✓；
  **"Untervariatäten"**——300dpi 确认 print 即此（源级，忠实）；mittels ℳ（补 \mathcal）✓；
  Ā_g(ℂ)−A_g(ℂ)/"eine beschränkten Betrag"（源级语法，忠实）✓
- 结果：**FAIL（IP 族 ×4）→已修**
## p.007（print 355：log-Singularitäten Definition + 单位圆盘情形）
- 核对：φ: X̃→X/Sup{‖h‖,‖h‖^{-1}}≤c₁(|log|f||)^{c₂} ✓；Beispiel X=Ā_g(ℂ), Y=Ā_g(ℂ)−A_g(ℂ) ✓；
  "eine Geradenbündel"（print 语法，忠实）✓；p_*(Ω¹_{A/X}) ✓；**单位圆盘 300dpi 确认为 blackboard 𝔻**
  （md 正文 "ID" → FAIL 已修为 $\mathbb{D}$；a) 项 ID→𝔻 已修）✓；Uᵢ 覆盖 a)/b)（z₁z₂=tᵐ）✓；
  α=(holomorph)·dz、dz₁/z₁ ✓
- 结果：**FAIL（两点）→已修**
## p.008（print 356：积分估计 + Lemma 3 + Satz 1 头）
- 核对：(i/2)∫_{C_t∩q^{-1}(t)}α∧ᾱ/‖log|r‖| ✓；‖‖≥(pos. Konst.)‖‖₁ ✓；Lemma 3：X⊆ℙⁿ_ℤ
  （300dpi 确认上标 n；md 正确）/O(1)|(X(ℂ)−Y(ℂ)) ✓；f₁,...,**f_t**（300dpi 确认 **t**——md 正确，
  150dpi 误判 r）∈Γ(X/ℤ,O(s)) ✓；**inf{log(‖log‖fᵢ(z)‖₁‖)}——300dpi 确认双竖线（md 正确）**✓；
  ρ: Spec(R)→X/|h−h₁|≤c₃+c₄log(h₁) ✓；Satz 1 i) ✓
- 结果：**PASS±**（±：早前 150dpi 两处疑点经 300dpi 证伪）
## p.009（print 357：Satz 1 ii)+Beweis + Lemma 4 + §4 Isogenien）
- 核对：ii) h(A)≤c ✓；Beweis（K'⊇K n≥3 n-Teilungspunkte/Galois-Kohomologie）✓；
  Lemma 4 Hermite-Minkowski ✓；§4：p₁/p₂/s/φ/G=Ker(φ) quasiendlich ✓；φ*: ω_{A₂/R}→ω_{A₁/R}/
  #(ω/φ*)=#s*(Ω¹_{A₁/A₂})=#s*(Ω¹_{G/R}) ✓；(Grad(φ))^{1/2} ✓
- 结果：**PASS**
## p.010（print 358：Lemma 5 + Bemerkung + Satz 2 + Beweis 开头 + Lemma 6）
- 核对：**Lemma 5 h(A₂)=h(A₁)+½log Grad(φ)−1/[K:ℚ]·log(#s*(Ω¹_{G/R}))** ✓；exp(2[K:ℚ](h(A₂)−h(A₁))) ✓；
  Satz 2 h(Aₙ)=h(A) ✓；Beweis：v₁..v_r/"Stellen von **k**"（print 小写 k，源级，忠实）/mᵢ=[Kᵢ:ℚ_l]/m=Σmᵢ ✓；
  Â über Spf(Rᵢ)/0→T_s→A_s→B_s→0 ✓；Ĥᵢ=Â[l^∞]/T_l(T)⊆T_l(Hᵢ)⊆T_l(A) ✓；Lemma 6 Iᵢ trivial/
  Dᵢ/Iᵢ≅**Ẑ**（300dpi 确认 blackboard ℤ̂；widehat bold→\hat\mathbb 已修）✓；⟨,⟩: T_l(A)**x**T_l(A)
  （**300dpi 确认 print 本身用 x**——源级记号，忠实不改）→ℤ_l(1)=T_l(𝔾_m) ✓
- 结果：**PASS±**（±：Ẑ 归一；x 源级）
## p.011（print 359：Lemma 6 证明 + Gᵢ 构造 + 全局化 + Ṽ 定义）
- 核对：SGA VII₁ Exp IX §7/⟨T_l(T),T_l(Hᵢ)⟩=0 ✓；T_l(Hᵢ)=T_l(T)^⊥/Hom_{ℤ_l} ↪ ✓；**K⊆Kᵢ**
  （300dpi 确认 ⊆；md 正确）✓；Gᵢ=G∩Hᵢ/**#(s*Ω¹_{A/Aₙ}⊗_R Rᵢ)=#s*(Ω¹_{(Gᵢ)ₙ/Rᵢ})**
  （300dpi 确认 ⊗_R 与 (Gᵢ)ₙ——md 正确，150dpi 误判）✓；[13] Prop 2：l^{n·mᵢ·dᵢ} ✓；
  T_l(Gᵢ)⊗Cᵢ≅Cᵢ^{hᵢ−dᵢ}⊕Cᵢ^{dᵢ}(+1)/„(+1)"=Tate-Twist（md ,,…″ 忠实转写）/Dᵢ-**Moduln** ✓；
  Cᵢ(**χ₀^{dᵢ}**)=Cᵢ(dᵢ)（md d₁ → FAIL 已修）✓；#s*Ω¹=l^{nΣmᵢdᵢ}/h(Aₙ)−h(A) 公式 ✓；
  **Ṽ=Ind_π^{π̃}(T_l(A))**（300dpi 确认上标 π̃ 带 tilde；md 丢 → FAIL 已修）(π=Gal(K̄/K)) ✓
- 结果：**FAIL（两点）→已修**
## p.012（print 360：W̃/χ + 有限阶 + mh/2 + §5 Satz 3/4）
- 核对：W̃=Ind_π^{π̃}(T_l(G))/L=Λ^{mh}(W̃)⊆Λ^{mh}(Ṽ) ✓；χ: π̃→ℤ_l^* ✓；χ=(l-adische Potenz von
  χ₀)·(Charakter endlicher Ordnung) ✓；**D≅Gal(ℚ̄_l/ℚ_l)⊆π̃**（300dpi 确认 ⊆、tilde；md 正确，
  150dpi 误判 ≅π̂）✓；L⊗_{**ℤ_l**}C（md bold ℤ_i → FAIL 已修）≅C(+Σmᵢdᵢ) ✓；χ·χ₀^{−Σmᵢdᵢ} ✓；
  p^{mh/2}/Σmᵢdᵢ=mh/2 ✓；Satz 3/4（End bold K→K、⊗_ℤ 归一已修）✓；弱化命题 bijektiv ✓
- 结果：**FAIL（bold ℤ 族 ×4）→已修**
## p.013（print 361：Satz 4 证明纲要 + 四元数 + Korollar 1/2）
- 核对：**"Dann besitzt"**（md "besitz" 丢 t → FAIL 已修）✓；W⊆T_l⊗ℚ_l/π-不变极大迷向 ✓；
  Satz 2+Satz 1 推论 ✓；[16] 幂等 ✓；a²+b²+c²+d²=−1 四元数矩阵 v ✓；v·ᵗv=−1 ✓；
  W₁={(x,vx)|x∈W⁴}⊕{(y,−vy)|y∈(W^⊥)⁴}⊆T_l(A)⁸⊗ℤ_lℚ_l（bold 归一已修）✓；
  Korollar 1/Beweis Satz 4 für A₁×A₂/L-Reihe ✓；Korollar 2 i)-iv)（⊗_ℤ 归一已修）✓
- 结果：**FAIL（多点）→已修**
## p.014（print 362：Korollar 3 + §6 Satz 5 + Beweis 开头）
- 核对：Korollar 3 T_l(A)≅T_l(B) ✓；Beweis："Wir dürfen **weiter**"（300dpi 确认 weiter；md 正确）✓；
  **Grad √d**（300dpi 4x 确认**无 n 次根指数**；md \sqrt{d} 正确，150dpi 误判）✓；a) semistabile
  b) prinzipal polarisiert（300dpi 确认 prinzipal）c) größte l-Potenz in Grad(φ) N teilt（varphi→phi 归一）✓；
  **exp(2[K:ℚ](h(B)−h(A)))**——md 少一个右括号 → FAIL 已修 ✓；Satz 5 ✓；Beweis：L_v(A,s)/
  v₁..v_r/K'⊇K ≤l^{8g²} ✓；G=Gal(K'/K)/Čebotarev ✓；M⊆End_{ℤ_l}(T_l(A₁))×End_{ℤ_l}(T_l(A₂))
  （300dpi 确认下标 ℤ_l；bold→\mathbb 已修）✓；"die ℤ_l-Unteralgebra"（italic Z→blackboard 已修）✓
- 结果：**FAIL（括号+归一）→已修**
## p.015（print 363：Nakayama 论证 + Satz 6 + N 的选取）
- 核对：ρ: π→(M/lM)*=Einheiten/#(M/lM)*≤l^{8g²}/因子化过 G ✓；Satz 6 (Shafarevich) ✓；
  Beweis（d=1/exp 式平衡已核）✓；B₁/B₂ 同构→Isogenie Grad prim zu l ✓；π-不变 Gitter/
  **M_l**（300dpi 确认下标 **l**；md 正确，150dpi 误判 Mᵢ）⊗_{ℤ_l}ℚ_l halbeinfach（Satz 3）✓；
  n=Primzahlen 乘积/**K⊇ℚ**（md 斜体 Q → FAIL 已修 blackboard）✓；π̃=Gal(ℚ̄/ℚ)⊇π ✓；
  **P_h(T)=det[T−F_p|Λ^h(Ind_π̃^π(T_l(A)))]**（300dpi 确认 sub π̃/sup π——**print 即此与 §4 相反**，
  md 忠实不改，quirk 登记）✓
- 结果：**FAIL（单点）→已修**
## p.016（print 364：P_h 性质 + N 选取 + V₁ 块 + Raynaud）
- 核对：l zu pn prime/F_p ✓；**p^{+h/2}**（300dpi 确认带 +；md 正确）/Koeffizienten in ℤ（补 \mathbb）✓；
  P_h(±p^j)/0≤h≤2gm、0≤j≤gm、j≠½h ✓；N≥np ✓；φ: B₁→B₂/l annuliert G ✓；
  **V₁/Ṽ₁/W₁/W̃₁ 块**——300dpi 确认 print 全部下标 **1**（md 误 V_l → FAIL 已修 ×8）且
  Ind 上标为 π̃（md 丢 → FAIL 已修 ×2）；(V)→(V₁) 已修 ✓；L=Λ^{mh}(W̃₁)⊆Λ^{mh}(Ṽ₁) 已修 ✓；
  γ: π̃→(ℤ/lℤ)* ✓；**Λ^m Ind_π^{π̃}(ℤ)**（md "A^m" → FAIL 已修）✓；γ·εʰ unverzweigt/unipotent
  auf **V₁**（已修）✓；l^d=#s*(Ω¹_{G/R})（300dpi 确认 G/R；md 正确）/0≤d≤gm ✓；
  **χ·εʰ=χ₀^{+d}**（300dpi 确认带 +；md 正确）/χ₀^d(F_p)=±p^d/P_{mh}(T) mod l/d=hm/2 ✓；
  h(B₂)−h(B₁)=log(l)(h/2−d/m) ✓
- 结果：**FAIL（V₁ 块 ×11+Λ^m）→已修**
## p.017（print 365：Satz 7 Mordell + Bemerkungen + Literatur [1]-[3]）
- 核对：Korollar 1（Torelli）✓；Satz 7 X(K) endlich ✓；Beweis [9]：φ: X₁→X/K₁/φ^{-1}(x)/
  **y∈φ^{-1}(x)**（md 误 p^{-1} → FAIL 已修）/D=φ^{-1}(x)−{y}/verallgemeinerte Jacobische (X₁,D) ✓；
  Multiplikation mit 2/Y(x)→X₁/a) v teilt 2 b) schlechte Reduktion c) φ verzweigt ✓；
  **"Es folgt die Behauptung"**（300dpi 确认 Es；md 正确，150dpi 噪点误判 It`s）✓；
  Bemerkungen 1. Siegelscher Satz 2. [16] Kommutator ✓；Literatur [1] Arakelov 5, 1277-1302 (1971)/
  [2] 8, 1167-1180 (1974)/[3] Baily-Borel 84, 442-528 (1966) ✓
- 结果：**FAIL（单点）→已修**
## p.018（print 366：Literatur [4]-[16] + Oblatum + Zusatz bei der Korrektur）
- 核对：**md Literatur 只有 [1]-[3]——[4]-[16] 与 "Oblatum 8-VI & 10-VII-1983" 整段丢失 → FAIL**
  （与 Maynard [49] 同族 mineru 掉页尾缺陷）；已按 PNG 逐条转录补入 13 条
  （[4] Deligne-Mumford Publ. math. I.H.E.S. 36/[5] Calculus Eingereicht/[6] Invent. 73, 337-347/
  [7] Moret-Bailly "267-270: 1983"——print 即此标点/[8] Namikawa LN 812/[9] Parshin/[10] Raynaud
  (p,...,p) 102/[11] Szpiro "de **Parsin**"——print 即此拼写/[12] Astérisque 86/[13] Tate Driebergen/
  [14] Tate Invent. 2/[15] Zarhin Sbornik 24/[16] Zarhin Izvestija 8, 477-480）✓；
  Zusatz：**Gabber 指出 Satz 2 证明不完全正确，只可得 h(Aₙ) stationär**（与 1984 勘误呼应）✓
- 结果：**FAIL（整段）→已修**

## 总评

- **覆盖声明**：18/18 页逐页目检（150dpi 全页）+ 300dpi 局部放大 22 处终裁；pdftotext 文本层为
  1983 Springer OCR 残留（系统损坏），按扫描件 SOP 不作对账依据，mineru 自行 OCR 质量高。
- **FAIL 修复（七大类，共 72 组替换）**：①fraktur 𝖹 误读 "3" ×17 统一为 \mathfrak{Z}（含 𝔷̃）；
  ②Λ^g 误读 A^g ×3；③ℙ 误读 IP/\mathbb{IP} ×7、bold ℤ/blackboard 归一 ×15、italic Z_l→ℤ_l ×3、
  斜体 Q→ℚ；④𝔖/𝔻 丢 fraktur ×4、Ind 上标丢 tilde ×3、A^m→Λ^m、χ₀^{d₁}→dᵢ、bold End K→K；
  ⑤§6 V₁ 块下标 l→1 ×8；⑥缺字/括号/粘连 ~10 处（besitz→besitzt、exp 补右括号、$..$$..$ 拆分、
  Satz 4/5/6 空格、y∈p^{-1}→φ^{-1}）；⑦**Literatur [4]-[16]+Oblatum 整段按 PNG 转录补入（13 条）**。
- **源级 quirk 清单（忠实不改）**："bestitzt"（Korollar，300dpi 确认）；Korollar 中两处 ρ 无 bar
  （Beweis 内 ρ̄ 有 bar——print 自相不一致）；×ₛA₂ 下标小 s；"Untervariatäten"；"eine Geradenbündel"；
  "eine beschränkten Betrag"；"Stellen von k" 小写；⟨,⟩ 用 "x" 不用 ×；„(+1)" 引号 md ,,…″ 转写；
  ref[7] "267-270: 1983"；ref[11] "de Parsin"；P_h 的 Ind_π̃^π 与 §4 Ind_π^{π̃} 方向相反（print 即此）；
  "Wir dürfen weiter"（150dpi 误 wiede，300dpi 定谳 weiter）。
- **300dpi 证伪记录（150dpi 疑点未改）**：h(A) 无负号；f_t（非 f_r）；inf 公式双竖线；K⊆Kᵢ；
  ⊗_R 与 (Gᵢ)ₙ；p^{+h/2}；χ₀^{+d}；Ω¹_{G/R}；√d 无根指数；Es folgt；D≅Gal(ℚ̄_l/ℚ_l)⊆π̃；
  M_l（非 Mᵢ）；P_h Ind 上下标 print 即 Ind_π̃^π。
- **可用性结论**：修复后 md 可作该文忠实德文底本；与 Faltings_1984_erratum（已审 ✅）构成完整闭环。
  参考文献 16 条现已齐全（抽验 8 条全对）。

### 修复登记（2026-09-29）
- **72 组替换全部命中**（fraktur 𝖹 ×17、Λ^g ×3、ℙ/IP ×7、blackboard ℤ 归一 ×18、V₁ 块 ×8、
  Ind/Λ^m 记号 ×5、缺字/括号/粘连 ~10、Literatur [4]-[16]+Oblatum 整段补入）；fix commit `2dd63866`
  （父 `86a988e4` 即修复前 md 原貌）。
- 本篇 18/18 页完成，无未决项；与 1984 勘误（a84086d2 已审）构成闭环。
