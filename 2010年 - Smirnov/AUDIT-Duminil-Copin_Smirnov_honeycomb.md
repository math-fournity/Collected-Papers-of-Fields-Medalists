# AUDIT — Duminil-Copin & Smirnov, "The connective constant of the honeycomb lattice equals √(2+√2)"（arXiv:1007.0575v2；11 页）

> mineru: standard 档云端解析（**parse_mode=txt**——本 PDF 为 pdfTeX 数字件、含精确文本层），导出
> `Duminil-Copin_Smirnov_2010_honeycomb_mineru/`；审计依据 = 二值化渲染
> `audit/honeycomb_pNNN.png`（pngmono 150dpi）对照 md，并以 `pdftotext` 文本层做**全篇 token 级逐字符复核**。
> **本 PDF 在 `2010年 - Smirnov/` 与 `2022年 - Duminil-Copin/` 各存一份，PDF 与 md 均 byte-identical
> （md5 相同：pdf 9e9c7e1c…、md 50367f5b…）**——本审计对两份同时有效。
> 逐页审计，一页一签。

## p.001（PDF p.1）
- PNG：audit/honeycomb_p001.png（pngmono 150dpi）
- 核对：
  - 题名（两行，含 √(2+√2)）、作者 Hugo Duminil-Copin and Stanislav Smirnov ✓
  - Abstract 全段 ✓；§1 Introduction：Flory [3]、"(i.e. visiting every vertex at most once)"、c_n 定义、
    √2^n ≤ c_n ≤ 3·2^{n−1}、c_{n+m} ≤ c_n c_m、μ := lim c_n^{1/n}、connective constant 命名 ✓
  - "Using Coulomb gas formalism, B. Nienhuis [8, 9]…" 段 ✓（含 O(n) 模型、square lattice 不适用）
  - 左侧 arXiv 戳记（arXiv:1007.0575v2 [math-ph] 27 Jun 2011）、页码 1 未转写（惯例/系统性）
  - **ff→f 伪影（文本层对账）**：正文 "different" ×2 → md "diferent"（见 ±）
- 结果：**PASS±**（±：arXiv 戳记/页码；ff→f "diferent"×2）
- 备注：本件 md 走文本层提取（parse_mode=txt），ff 合字提取缺陷与 Lions 件同类。

## p.002（PDF p.2）
- PNG：audit/honeycomb_p002.png（pngmono 150dpi）
- 核对：
  - **Theorem 1** ✓；μ = √(2+√2) ✓
  - mid-edges 约定（H 记 mid-edge 集）、γ : a → E / γ : a → b、ℓ(γ) 定义 ✓
    —— **md 丢失行内箭头 →（作 "a  E" / "a  b"）**，见 ±；但 Z(x) 的下标 `\gamma : a \to H` 保留了 \to
    （md 内部不一致）
  - Z(x) = Σ_{γ : a→H} x^{ℓ(γ)} ∈ (0,+∞] ✓；μ 的等价表述（x ≷ 1/√(2+√2)）✓
  - 论文结构段、x_c := 1/√(2+√2)、j = e^{i2π/3} ✓
  - **2 Parafermionic observable** ✓；domain 定义（Ω ⊂ H、∂Ω、单连通）✓；winding W_γ(a,b) 定义 ✓
  - **Definition 1**：F(z) = F(a,z,x,σ) = Σ_{γ⊂Ω : a→z} e^{−iσW_γ(a,z)} x^{ℓ(γ)} ✓
  - **Lemma 1**：x = x_c、σ = 5/8 ⟹ (p−v)F(p)+(q−v)F(q)+(r−v)F(r) = 0 ✓（(1)）
    —— md 作 "Lemma 1$I f x = x_c$"（"If" 被切成 "I f"）
  - 页码 2 未转写（系统性）
- 结果：**PASS±**
  - ±1：行内箭头 → 丢失 2 处（"γ : a → E"、"γ : a → b"）；
  - ±2：Lemma 1 前 "If" 被分词为 "I f"；
  - ±3：页码丢弃。
- 备注：Definition 1 与 (1) 逐符号吻合。

## p.003（PDF p.3）
- PNG：audit/honeycomb_p003.png（pngmono 150dpi）
- 核对：
  - **Figure 1**（左：domain Ω 与边界 mid-edge/顶点标注；右：W_γ(a,b)=0 与 2π 两条曲线）✓
    图版已随导出（`images/page_2_image_0.jpg`）；图注文字逐字 ✓
  - σ = 5/8 的复权 e^{−iσW_γ(a,z)} 与 λ/λ̄ 解释 ✓；**λ = exp(−i·(5/8)·(π/3)) = exp(−i·5π/24)** ✓
    （md 的 `2 4` 空格为排版级）
  - **Proof** 起（p,q,r 逆时针、c(γ) 展开）✓；c(γ) = (p−v)·e^{−iσW_γ(a,p)} x_c^{ℓ(γ)} ✓
  - 配对/三重组两条 bullet（三 mid-edge 成对 ↔ 一/二 mid-edge 成三）✓ 逐字
    （md 中 "p, q, r." 后接 "," 出现重复标点——排版级）
  - "If one can prove … (1) holds." ✓；"Let γ₁ and γ₂ …" 段首 ✓
  - 页码 3 未转写（系统性）
- 结果：**PASS±**（±：页码；标点微瑕）
- 备注：本页公式与图注逐符号/逐字吻合。

## p.004（PDF p.4）
- PNG：audit/honeycomb_p004.png；仲裁：audit/p004_cos_300dpi.png
- 核对：
  - 承接段（γ₁/γ₂ 反向绕环）✓；ℓ(γ₁)=ℓ(γ₂) 与两行 W_γ 关系式 ✓（含源自身末项写作 W_{γ₁}(a,p)）
  - γ₁ 在 p,q 间绕数论证（a 在边界、Ω 单连通）✓
  - c(γ₁)+c(γ₂) = (q−v)e^{−iσW_{γ₁}(a,q)}x_c^{ℓ(γ₁)} + (r−v)e^{−iσW_{γ₂}(a,r)}x_c^{ℓ(γ₂)}
    = (p−v)e^{−iσW_{γ₁}(a,p)}x_c^{ℓ(γ₁)}(jλ̄⁴ + j̄λ⁴) = 0 ✓；jλ̄⁴ = −i、λ = exp(−i5π/24) ✓
  - 三重组：ℓ(γ₂)=ℓ(γ₃)=ℓ(γ₁)+1 与两行 W_γ 关系式 ✓；
    c(γ₁)+c(γ₂)+c(γ₃) = (p−v)e^{−iσW_{γ₁}(a,p)}x_c^{ℓ(γ₁)}(1 + x_c jλ̄ + x_c j̄λ) = 0 ✓
  - **x_c^{−1} = √(2+√2) = (2 cos π/8)** —— md 作 "(2 cos <sup>π</sup> )"，**丢失分母 8**（300dpi 确认）→ 见 FAIL
  - "The claim of the lemma follows readily …" + QED `□`（原件；md 未录）✓
  - **Figure 2**（左：配对；右：三重组）+ 图注 ✓（"difering" ← differing，ff 伪影）
  - **Remark 1**（(1) 系数为三次单位根乘 (p−v)、discrete dz-integral、discrete holomorphic、Section 4）✓
    （md "Coeficients" ← Coefficients，ff 伪影）
- 结果：**FAIL（单点，公式缺字符）**
  - ✗ md 第 119 行：`= (2 cos <sup>π</sup> )`——**原图为 (2 cos π/8)**（300dpi 确认分母 8）；分母 8 丢失使公式值错
    （2cos π ≠ √(2+√2)）。**以原图为准**；修复建议：`(2 cos <sup>π</sup> )` → `(2 \cos \tfrac{\pi}{8})`。
  - ±：页码；ff 伪影 "difering"、"Coeficients"；QED `□` 未录。
- 备注：除该单点外，本页全部公式逐符号吻合。

## p.005（PDF p.5）
- PNG：audit/honeycomb_p005.png（pngmono 150dpi）
- 核对：
  - **3 Proof of Theorem 1** ✓；strip domain S_T / S_{T,L}（±L、±π/3、C 中 meshsize 1、edge e 使 a=0）✓
  - V(S_T) = {z ∈ V(H) : 0 ≤ Re(z) ≤ (3T+1)/2} ✓；V(S_{T,L}) = {z ∈ V(S_T) : |√3 Im(z) − Re(z)| ≤ 3L} ✓
  - α/β（左右边界）、ε/ε̄（上下边界）✓；三个（正）分割函数 A/B/E 定义（含 a→α∖{a}、a→ε∪ε̄）✓
  - **Figure 3**（S_{T,L} 与边界区间）+ 图注 ✓
  - **Lemma 2**：**1 = c_α A^{x_c}_{T,L} + B^{x_c}_{T,L} + c_ε E^{x_c}_{T,L}**（(2)）✓；
    c_α = cos(3π/8)、c_ε = cos(π/4) ✓（md "coeficients" ← coefficients，ff 伪影）
  - 页码 5 未转写（系统性）
- 结果：**PASS±**（±：页码；ff "coeficients"）
- 备注：本页公式逐符号吻合。

## p.006（PDF p.6）
- PNG：audit/honeycomb_p006.png（pngmono 150dpi）
- 核对：
  - **Proof（Lemma 2）**：对 V(S_{T,L}) 求和、内部 mid-edge 相消 ✓
  - **(3)** 0 = −Σ_{z∈α}F + Σ_{z∈β}F + jΣ_{z∈ε}F + j̄Σ_{z∈ε̄}F ✓
  - 对称性 F(z̄)=F̄(z)；绕数 −π/π；Σ_{z∈α}F = 1 + (e^{−iσπ}+e^{iσπ})/2·A_{T,L}^x = 1 − cos(3π/8)A = 1 − c_α A ✓
  - F(a)=1；β/ε/ε̄ 绕数 0 / 2π/3 / −2π/3；Σ_β F = B、jΣ_ε F + j̄Σ_ε̄ F = cos(π/4)E = c_ε E ✓
  - QED `□`（原件；md 未录）；"formulæ" 原拼法 ✓
  - 单调有界 ⟹ A_T/B_T 极限（Σ_{γ⊂S_T : a→α∖{a}} / a→β）✓；E_{T,L}^{x_c} 递减 → E_T^{x_c} ✓
  - **(4)** 1 = c_α A_T^{x_c} + B_T^{x_c} + c_ε E_T^{x_c} ✓
  - **Proof of Theorem 1**：Z(x_c) ≥ Σ_{L>0}E_{T,L}^{x_c} ≥ Σ_{L>0}E_T^{x_c} = +∞（若某 T 有 E_T>0）✓；
    反之 **E_T^{x_c}=0 ∀T** ⟹ **(5)** 1 = c_α A_T^{x_c} + B_T^{x_c} ✓
  - 页码 6 未转写（系统性）
- 结果：**PASS±**（±：页码；QED `□` 未录）
- 备注：本页公式逐符号吻合。

## p.007（PDF p.7）
- PNG：audit/honeycomb_p007.png（pngmono 150dpi）
- 核对：
  - 桥分解论证（A_{T+1}^x 计数差、切割首点、半边缘补给、比 γ 长一步）✓；
    **(6)** A_{T+1}^{x_c} − A_T^{x_c} ≤ x_c(B_{T+1}^{x_c})² ✓
  - (5)+(6) 组合链（0=1−1 起始、c_α 拆分、≤ 估值）✓；c_αx_c(B_{T+1}^{x_c})² + B_{T+1}^{x_c} ≥ B_T^{x_c} ✓
  - 归纳界 B_T^{x_c} ≥ min[B₁^{x_c}, 1/(c_αx_c)]/T ✓；Z(x_c) ≥ Σ_{T>0}B_T^{x_c} = +∞ ⟹ μ ≥ x_c^{−1} = √(2+√2) ✓
  - 反向不等式：bridge 定义（宽 T、S_T 两侧间、垂直平移等价）、B_T^x ≤ 1（由 (4)）、长度 ≥ T ⟹
    **B_T^x ≤ (x/x_c)^T B_T^{x_c} ≤ (x/x_c)^T** ✓；级数 Σ_{T>0}B_T^x 与乘积 ∏(1+B_T^x) 收敛 ✓
  - 桥分解事实（宽 T_{−i}<⋯<T_{−1}、T₀>⋯>T_j；固定起点 mid-edge 与首顶点 ⟹ 唯一）✓；
    Hammersley–Welsh [5]、Section 3.1 of [4] ✓
  - **Z(x) ≤ 2Σ_{T_{−i}<⋯<T₀}(∏_{k=−i}^{j}B_{T_k}^x) = 2∏_{T>0}(1+B_T^x)² < ∞** ✓；因子 2 说明 ✓；μ ≤ x_c^{−1} ✓
  - 页码 7 未转写（系统性）
- 结果：**PASS±**（±：页码）
- 备注：本页公式逐符号吻合。

## p.008（PDF p.8）
- PNG：audit/honeycomb_p008.png（pngmono 150dpi）
- 核对：
  - **Figure 4**（左：半平面 walk 分解为宽 8>3>1>0 四桥、含宽 0 桥；右：逆过程）+ 图注 ✓
  - 桥分解存在性证明：γ̃ 半平面 walk（起点极值实部）、对 T₀ 归纳、末次访问最大实部顶点、
    n 个顶点成桥 γ̃₁（T₀）、跳过无歧义的 (n+1)-th 顶点、后续成 γ̃₂（T₁<T₀）、归纳 T₁>⋯>T_j、
    在 γ̃₂ 分解前加 γ̃₁ ✓（md "$( n + 1 )$)-th" 多一右括号——排版级）
  - 反向/平面情形（γ₁/γ₂ 切分；宽 T_{−i}<⋯<T_{−1} 与 T₀>⋯>T_j）✓；QED `□`（原件；md 未录）
  - **Remark 2** 首句 ✓
  - 页码 8 未转写（系统性）
- 结果：**PASS±**（±：页码；QED `□` 未录）
- 备注：本页逐字吻合（图版已随导出）。

## p.009（PDF p.9）
- PNG：audit/honeycomb_p009.png（pngmono 150dpi）
- 核对：
  - **Remark 2** 续：c/T ≤ B_T^{x_c} ≤ 1 ✓
  - [6] 3.3.3/3.4.3 节猜想行为 ⟹ **Σ_{γ⊂S_T : 0→T+iyT} x_c^{ℓ(γ)} ≈ T^{−5/4}H(0,1+iy)^{5/4}** ✓；
    H 为 Poisson 核的边界导数；对 y 积分 ⟹ B_T^{x_c} ~ T^{−1/4}；S_T 内 0→iyT 的类似猜想 ✓
  - **4 Conjectures** ✓；Nienhuis [8, 9] 更精确渐近 ✓
  - **(7)** c_n ∼ A n^{γ−1}√(2+√2)^n，γ = 43/32 ✓；∼ 的含义（比值 n^{o(1)} 阶或趋常）✓
  - Flory 预测：**⟨|γ(n)|²⟩ = (1/c_n)Σ_{γ n-step SAW}|γ(n)|² = n^{2ν+o(1)}**，ν = 3/4 ✓（(8)）
  - "Despite the precision …" 段 ✓；Lawler–Schramm–Werner [6]（共形不变极限 ⟹ γ、ν 可算）✓
  - 离散逼近设定（Ω ≠ C、Ω_δ ⊂ Ω、a_δ/b_δ 最近顶点、P_{x,δ} 权重 ∝ x^{ℓ(γ)}、γ_δ 随机曲线）✓
  - **Conjecture 1**（x = x_c 时 γ_δ 的 law → chordal SLE κ = 8/3，δ→0）✓ —— "posses" 系源拼写（忠实）
  - 页码 9 未转写（系统性）
- 结果：**PASS±**（±：页码）
- 备注：本页公式逐符号吻合。

## p.010（PDF p.10）
- PNG：audit/honeycomb_p010.png（pngmono 150dpi）
- 核对：
  - SLE 收敛判据 [7, 10]；F_δ 归一化版共形不变极限（全纯 + 预定边界值）✓
  - [11] 界面绕数唯一；**Riemann BVP**：**Im(F(z)·(tangent to ∂Ω)^{5/8}) = 0, z ∈ ∂Ω**（(9)）✓
    （md "tangentto" 空格合并——排版级）；奇点于 a；(dz)^{5/8}-forms、fractal 边界仍良定义 ✓
  - Remark 1 续（离散围道积分消失、次列极限全纯）；仅 relation (1) 不足（≈(2/3)E 关系 vs E 值，
    无法由边界值重构）；divergence-free 向量场、curl 极限消失 ✓（源拼写 "vertice"、"unsufficient" 忠实）
  - **Conjecture 2**（Ω、z、a/b、b 处光滑、F_δ 与 z_δ 最近点）✓；
    **(10)** lim_{δ→0}F_δ(z_δ)/F_δ(b_δ) = (φ′(z)/φ′(b))^{5/8} ✓
  - Φ 为 Ω→上半平面、a→∞、b→0 的共形映射；(10) 右侧良定义（φ 唯一至实因子）✓
  - **Acknowledgements** 全段（Slade、Lawler、EU Marie-Curie RTN CODY、ERC AG CONFRA、Swiss FNS、
    Chebyshev Laboratory、RF governement grant 11.G34.31.0026——源拼写 "governement" 忠实）✓
  - 页码 10 未转写（系统性）
- 结果：**PASS±**（±：页码；"tangentto" 空格合并）
- 备注：本页公式逐符号吻合。

## p.011（PDF p.11，**末页**）
- PNG：audit/honeycomb_p011.png（pngmono 150dpi）
- 核对：**References [1]–[11] 逐条**（作者/题名/期刊卷页年/出版信息）——全部吻合：
  [1] Cardy–Ikhlef（J. Phys. A 42(10), 102001, 2009）；[2] Chelkak–Smirnov（Invent. Math. to appear; arXiv:0910.2045, 2009）；
  [3] Flory（Cornell, ISBN 0-8014-0134-8, 1953）；[4] Madras–Slade（Birkhäuser, 1993）；[5] Hammersley–Welsh（Quart. J. Math. Oxford Ser. (2) 13 108–110, 1962）；
  [6] Lawler–Schramm–Werner（Fractal Geometry … Part 2, 339–364; Proc. Sympos. Pure. Math. 72, 2004）；
  [7] ——（Ann. Probab. 32(1B) 939–995, 2004）；[8] Nienhuis（Phys. Rev. Lett. 49 1062–1065, 1982）；
  [9] Nienhuis（J. Stat. Phys. 34 731–761, 1984）；[10] Smirnov（ICM Eur. Math. Soc. Zürich, Vol. II 1421–1451, 2006）；
  [11] Smirnov（ICM Hyderabad 2010, Plenary lectures, World Scientific, 2010）
  - **md 遗漏作者单位/邮箱块**（页底右栏 "DÉPARTEMENT DE MATHÉMATIQUES / UNIVERSITÉ DE GENÈVE /
    GENÈVE, SWITZERLAND / E-MAIL: hugo.duminil@unige.ch ; stanislav.smirnov@unige.ch"）——见 ±
  - 重音修饰符伪影："Birkh¨auser"、"Benoˆıt"、"Z¨urich"；页码 11 未转写（系统性）
- 结果：**PASS±**（±：页码；作者单位/邮箱块遗漏；重音伪影）
- 备注：文献 11 条逐条吻合。

## 总评
- **覆盖声明**：11 页全部逐页审计（audit/honeycomb_p001–p011.png，pngmono 150dpi）；因本件为 pdfTeX 数字件
  （parse_mode=txt），另以 `pdftotext` 做**全篇 token 级逐字符复核**。
- 结论分布：**PASS± ×10 + FAIL ×1（单点）**。
- **FAIL（1 处，单点，公式缺字符）**：p.4（md 第 119 行）`(2 cos <sup>π</sup> )` 应为 **(2 cos π/8)**——
  分母 8 丢失（300dpi 确认）。**以原图为准**；修复建议：`(2 \cos \tfrac{\pi}{8})`。
- 系统性瑕疵：①页码（1–11）与 arXiv 侧栏戳记未转写（惯例）；②**ff→f 伪影 8 处词位**（different→diferent×2、
  differing→difering、Coefficients→Coeficients×2、sufficient→suficient、suffice→sufice、unsufficient→unsuficient）；
  ③行内箭头 **→** 丢失（p.2 "γ : a → E"/"γ : a → b"）；④重音字符修饰符分解（Birkh¨auser / Benoˆıt / Z¨urich）；
  ⑤空格合并（tangentto、forthanks、ofthe 等）；⑥**p.11 作者单位/邮箱块遗漏**；⑦QED `□` 未录（p.4/p.6/p.8）。
- 忠实性正面案例（勿改）：源拼写 "posses"、"unsufficient"、"vertice"、"governement"。
- **双副本**：`2022年 - Duminil-Copin/` 的 PDF 与 md 均与本目录 byte-identical（md5 同）；该目录 AUDIT 文件互指本审计。
- 可用性：全部文本/公式/文献可引用；**唯 p.4 的 cos π/8 须按修复建议处理或以原图为准**。
- mineru 解析信息：mineru 3.4.4 / tier=basic / **parse_mode=txt**。

> **修复登记（2026-09-29）**：已按本审计修复 p.4 `(2 cos <sup>π</sup> )` → `(2 \cos \tfrac{\pi}{8})`；**双副本同步**（2022年 - Duminil-Copin 目录 md 同改）；修复与本登记同一 commit；修复前 md 见该 commit 父提交。
