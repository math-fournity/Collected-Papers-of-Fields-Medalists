# AUDIT — Lars V. Ahlfors, "Geometrie der Riemannschen Flächen"（ICM 1936 报告；10 页 = 印刷 pp.239–248）

> mineru: standard 档云端解析（parse_mode=ocr），导出 `Ahlfors_1936_riemannschen_flaechen_icm_mineru/`；
> 审计依据 = 二值化渲染 `audit/icm_pNNN.png`（pngmono 150dpi）对照
> `Ahlfors_1936_riemannschen_flaechen_icm__Ahlfors_1936_riemannschen_flaechen_icm.md`。逐页审计，一页一签。
> 仲裁裁剪：`audit/p001_weierstrass_300dpi.png` 等。
> PDF 结构：10 页 = 印刷 pp.239–248（德文报告，含编号公式与脚注）；本 PDF 由 Ghostscript 重制、含文本层
> （但其对 ß 等字符的转写不可靠，仅作辅助）。
> **系统性已知伪影**：ß → "fs"（如 Weierstrafs / heifat / Mafs / Grüfaenordnung / dafs）。

## p.001（PDF p.1 / 印刷 p.239）
- PNG：audit/icm_p001.png（pngmono 150dpi）；仲裁：audit/p001_weierstrass_300dpi.png
- 核对：
  - 题名 `GEOMETRIE DER RIEMANNSCHEN FLÄCHEN`、`Von Lars V. Ahlfors, Helsingfors.` ✓
  - §1 三段逐句 ✓（Riemanns einfache Idee… / Versucht man den Riemannschen Gedanken axiomatisch… /
    Die geometrische Funktionentheorie…）；末段 "zu ihrer vollen" 与下页 "Geltung." 自然续接 ✓
  - **ß→fs 伪影**："Weierstrafs"（Weierstraß）、"Weierstrafs'schen"（Weierstraß'schen）——
    **300dpi 确认原刊为 ß**（含所有格撇号）
  - 页码 239 未转写（系统性）
- 结果：**PASS±**（±：页码；ß→fs）
- 备注：报告 §1 为导论；无内容级差异。

## p.002（PDF p.2 / 印刷 p.240）
- PNG：audit/icm_p002.png（pngmono 150dpi）；仲裁：audit/p002_def1 / p002_heisst_300dpi.png
- 核对：
  - "Geltung. Ich hoffe mit der in diesem Vortrag gegebenen kurzen Zusammenfassung … zu dienen." ✓
  - §2：Fläche / Hausdorff-Raum / Separabilität / Riemannsche Fläche (R. Fl.) im Sinne von Weyl ✓
  - 定义 1./2.（斜体块）：w=TP 映入 |w|=|u+iv|<1；U₁U₂ 非空时 w₂=T₂T₁⁻¹w₁ 为直接共形映射 ✓
  - Radó 注记（三角化可导出，无需公设）✓；Ortsuniformisierende / lokaler Parameter、内蕴量在共形变换下
    不变、函数解析/调和性的定义、两 R. Fl. 等价的含义、"两个单连通开 R. Fl.（单位圆与平面）" ✓
  - §3 Überlagerungsfläche (Ü. Fl.)：W、W₀、P₀=SP、Spurpunkt、innere Transformation（Stoilow）✓
  - 页码 240 未转写（系统性）
- 结果：**PASS±**
  - ±（**ß 字形，全篇系统**）：本页 "heifat"（heißt）、"dafs"（daß）——原刊为标准 ß；md 对 ß 的转写
    前后不一致（同页多处又正确保留 "daß"），不误导德语读者。注：本 PDF 自带文本层对 ß 同样不可靠。
- 备注：本页无内容级差异。

## p.003（PDF p.3 / 印刷 p.241）
- PNG：audit/icm_p003.png（pngmono 150dpi）
- 核对：
  - 页脚 `16 — Congrès des mathématiciens 1936.` 与页码 241 未转写（系统性）
  - 定义 1./2./3.（S 连续；开集映为开集；SP=P₀ 的点孤立）✓；"Die dritte Bedingung kann nach Stoilow …" ✓
  - S 局部可逆、例外为孤立分歧点（具 Potenz 特征）、拓扑分类对函数论之重要 ✓
  - W₀ 为 R. Fl. 时角度可转移、Riemannsche Kugel / Ebene、闭 R. Fl. ✓
  - §4 主问题（Ü. Fl. 的内蕴性质）、konform-äquivalent、Typenproblem、hyperbolisch/parabolisch ✓
  - 性质刻画讨论（Darstellungsproblem、ausschöpfen、Überdeckungs-/Verzweigungspunkte 计数与渐近行为）✓
- 结果：**PASS±**（±：页脚/页码）
- 备注：本页无内容级差异。

## p.004（PDF p.4 / 印刷 p.242）
- PNG：audit/icm_p004.png（pngmono 150dpi）
- 核对：
  - "Dies ist offenbar ein ungenaues Verfahren … erwarten darf." ✓
  - §5：方法概览（selbstverständlich ohne auf Einzelkeiten einzugehen.¹——原刊拼写 "Einzelkeiten" 忠实）✓
  - 微分形式 ds=λ|dw| 定义 Riemann 度量（λ 非点函数、与参数平面欧氏度量共形）✓
  - Kurvenlängen / Flächeninhalte；∫ds=∫λ|dw|、∬dω=∬λ²dudv ✓
  - curvatura integra ∬Kdω、geodätisches Krümmungsintegral ∫ds/ϱ_g ✓
  - I. Fundamental 定理：G(w)（负对数极点、双曲→0 / 抛物→∞、eigentlich divergent 序列）、
    W(t)={G≤t}、Normalausschöpfung、Γ(t)={G=t} ✓
  - L(t)=∫_{Γ(t)}ds、A(t)=∬_{W(t)}dω；**A′(t)=∫_{Γ(t)} ds/(∂G/∂n)** ✓ 逐符号（含复合分式）
  - 脚注 ¹（Ahlfors 详述文，Acta Soc. Sci. Fenn. Nov. Ser. T. II, N:o 6）✓
  - 页码 242 未转写（系统性）
- 结果：**PASS±**（±：页码）
- 备注：本页无内容级差异。

## p.005（PDF p.5 / 印刷 p.243）
- PNG：audit/icm_p005.png（pngmono 150dpi）
- 核对：
  - 承接句（Normalableitung 关于 Riemann 度量）✓；Schwarz 不等式：L(t)² ≤ A′(t)∫_{Γ(t)}(∂G/∂n)ds = 2πA′(t) ✓
  - dt ≤ dA(t)/L(t)² ✓；抛物情形 ∫^∞ dA(t)/L(t)² 在任何度量下发散 ✓
  - H(t) = ∫_{Γ(t)} ds/ϱ_g ✓；ΔG=0 ⟹ H(t) = ∫_{Γ(t)}(∂/∂n)log(λ/|grad G|)ds ✓
  - Green 公式长链：∫_{t₀}^t H(t)dt = ∬_{W(t)−W(t₀)}(∂/∂n)log(λ/|grad G|)dsdt
    = ∬(∂/∂n)log(λ/|grad G|)(∂G/∂n)dsdn = D(log(λ/|grad G|),G) = |_{t₀}^t∫_{Γ(t)}log(λ/|grad G|)·(∂G/∂n)ds ✓
  - ∫_{t₀}^t H(t)dt ≤ 2π log L(t) + Konst. ✓
  - 上界量级 log A(t)、下界为重要课题 ✓（"Gröfaenordnung" 应为 Größenordnung——ß 伪影）
  - 页码 243 未转写（系统性）
- 结果：**PASS±**（±：页码；"Gröfaenordnung"）
- 备注：本页无内容级差异。

## p.006（PDF p.6 / 印刷 p.244）
- PNG：audit/icm_p006.png（pngmono 150dpi）
- 核对：
  - II. 任意 Ausschöpfung Φ(w)=τ（Φ 满足一般条件）→ 平行 Niveaukurven 的度量 ds=|grad Φ|·|dw| ✓
  - A′(τ)=L(τ), L′(τ)=H(τ) ✓；∫_{Γ(τ)}(∂G/∂n)ds = 2π ✓
  - 4π² ≤ L(τ)∫_{Γ(τ)}(∂G/∂n)²ds ✓；4π²∫_{τ₀}^{τ} dτ/L(τ) ≤ ∫∫(∂G/∂n)²dsdt = ∫∫|grad G|²dudv ✓
  - 双曲情形最后积分有界：∬|grad G|²dudv = |_a^b∫ G(∂G/∂n)ds = (b−a)2π ✓
  - **Wenn W hyperbolisch ist …**：∫_0^∞ dτ/L(τ) < ∞ ✓（斜体强调句）
  - 页码 244 未转写（系统性）
- 结果：**PASS±**（±：页码）
- 备注：本页无内容级差异。

## p.007（PDF p.7 / 印刷 p.245）
- PNG：audit/icm_p007.png（pngmono 150dpi）
- 核对：
  - "Die eben angeführten Resultate liefern …"（度量-共形 / 拓扑-度量两部分之划分至关重要）✓
  - §6：拓扑-度量任务的另一途径（与微分几何联系更显；metrisch/konform 划分不彻底之瑕）✓；
    脚注 ¹（Acta Mathematica, t. 65, 1935）✓
  - 第一 Hauptsatz 讨论：μ(Ω) 全加性、有界变差、μ(W₀)=1；多重覆盖区域 W̄ 上的定义 ✓
  - μ(W̄) = ∫_{W₀} n(a)dμ(a) ✓；n(a) 覆盖点数；"mittlere Blätteranzahl"（平均叶数）✓
  - 两个 Belegungen μ₁,μ₂、μ₀=μ₁−μ₂、χ(w,a,b)（对数极点、留数 1 与 −1）✓
  - p(w) = ∫_{W₀} χ(w,a,b)dμ(a) ✓
  - 页码 245 未转写（系统性）
- 结果：**PASS±**（±：页码；"Mafs"）
- 备注：本页无内容级差异。

## p.008（PDF p.8 / 印刷 p.246）
- PNG：audit/icm_p008.png（pngmono 150dpi）
- 核对：
  - χ 的 b-归一化、"p(w) 仅表观依赖 b" ✓
  - S(t)（W(t) 的平均叶数）；**(1)** ∫_{t₀}^{t}(S₁−S₂)dt = |∫_{t₀}^{t}∫_{Γ(t)} p(w)(∂G/∂n)ds. ✓（原件绝对值竖线为单侧，
    md 以 `\left| … \right.` 忠实记录）
  - 第一 Hauptsatz 之最一般形式与最重要应用（μ₀ 的势有界性 ⟹ S₁/S₂ 的渐近不等式或等式）✓
  - 连续面密度 Belegung、S(t) 作为 Ü. Fl. 的特征量、∫S dt = ∫S̄ dt + O(1) ✓
  - §7：第二 Hauptsatz 与 Gauss-Bonnet 的联系（与本性拓扑-度量性质相合）✓
  - 正则度量 ds=λ|dw|；**(I)** −(1/2π)∬_{W̄}Kdω = E + (1/2π)∫_Γ ds/ϱ_g ✓
  - **(2)** −(1/2π)∬_{W₀}Kdω = E₀ ✓
  - 页码 246 未转写（系统性）
- 结果：**PASS±**（±：页码）
- 备注：本页无内容级差异。

## p.009（PDF p.9 / 印刷 p.247）
- PNG：audit/icm_p009.png（pngmono 150dpi）
- 核对：
  - (1) 对 Ü. Fl. 的子区域不成立（Windungspunkte 处转移度量奇异）；分片证明广义公式 ✓
  - **(3)** −(1/2π)∬_{W̄}Kdω = E − n₁ + (1/2π)∫_Γ ds/ϱ_g ✓；n₁ 定义（按分歧阶计数的 Windungspunkte）✓
  - 更一般情形：度量在 a₁,⋯,a_q 奇异；测地零圆排除条件；r(∂/∂r)log λ → 1（r=|w−a_ν|→0）✓
  - 打孔后连通数增加 q 与 Σ₁^q n̄(a_r)；**(4)** E + Σ₁^q n(a_ν) − n₁ + (1/2π)∫_Γ ds/ϱ_g ✓
  - **(5)** −(1/2π)∬_{W₀}Kdω = q + E₀ ✓；**(II)** (q+E₀)S(t) = Σ₁^q n(a_ν,t) − n₁(t) − 1 + H(t) + β(t) ✓
  - β(t) 说明、λ 的选取、H/β 的估计、第二 Hauptsatz 最一般形式 ✓（"dergestellten" 原刊拼写忠实）
  - 页码 247 未转写（系统性）
- 结果：**PASS±**
  - ±1：奇异点下标 md 转写不一致（a_{v} / a_r / a_{\nu} 混用；原件为同一记号）——非误导；
  - ±2：式 (5) 的积分域 md 作 `\int_ {w _ {0}}`（原图 W₀；大小写误差，非误导）；
  - ±3：式 (5) 的编号与公式在 md 中被 "über." 分隔（版面顺序伪影，内容完整）。
- 备注：本页无内容级差异。

## p.010（PDF p.10 / 印刷 p.248，**末页**）
- PNG：audit/icm_p010.png（pngmono 150dpi）
- 核对：
  - Kugel E₀=−2 ⟹ Nevanlinna 定理及亚纯函数值分布推论；Torus χ=0 ⟹ 抛物情形缺陷与分歧指数消失 ✓
  - E₀>0 且 q=0 时的矛盾（t 可无限增大）⟹ zweiter Satz von Picard：亏格 >0 的闭曲面的一切
    覆盖曲面必双曲 ✓（斜体强调句逐字）
  - §8：Nr. 5 unter II 的推测（抛物情形的充分条件）、理论尚未建立、Gauss-Bonnet 亦重要、
    Kobayashi¹ 的个别结果 ✓
  - 脚注 ¹：Sci. Rep. Tokyo Bunrika Daigaku, sect. A Nr. 39 (1935) ✓
  - 页码 248 未转写（系统性）；本页其余空白
- 结果：**PASS±**（±：页码；"dafs"）
- 备注：报告至 §8 结束。

## 总评
- **覆盖声明**：10 页全部逐页审计（audit/icm_p001–p010.png，pngmono 150dpi；p.1/p.2 附 300dpi 仲裁裁剪）。
- 结论分布：**PASS± ×10；FAIL ×0**——无内容级数学错误。
- 系统性瑕疵：①**ß 字形转写不稳定**：原刊为标准 ß，md 或作 "fs"（Weierstrafs / Mafs / dafs）、
  或作 "fa"（heifat←heißt）、或正确保留 "ß"（daß、Größen 多处）；检索时须宽匹配，不误导德语读者。
  注：本 PDF 自带文本层对 ß 同样不可靠（"Weierstrafe"）。②页脚 `16 — Congrès des mathématiciens 1936.`
  与页码 239–248 全部未转写。③记号层面小瑕：奇异点下标 a_{v}/a_r/a_{\nu} 混用；式 (5) 积分域 W₀→`w_0`；
  式 (5) 编号与公式被 "über." 分隔。
- 忠实性正面案例（勿改）：原刊拼写 "Einzelkeiten"（p.242）、"dergestellten"（p.247）；1930 年代 ß 排印。
- 可用性：全 10 页文本与公式可放心引用；**无需要"以原图为准"的内容级修复项**。
- mineru 解析信息：mineru 3.4.4 / tier=basic / parse_mode=ocr。
