# AUDIT — C. Mouhot & C. Villani《Landau damping》（arXiv:0905.2167v2 note 版，10p；Acta Math. 207 (2011) 长文另件）

> mineru: standard 档云端解析（2026-09-29 从换件后正确 PDF 重导出；此前陈旧 Batenkov-Yomdin
> 错件导出已删并登记）。审计依据 = `audit/landau10_pNNN.png`（pngmono 150dpi，p.1/p.10 全页
> 抽验 + 全篇）+ pdftotext 文本层逐字符对账（born-digital，可靠）。

## p.001
- 核对：题录/摘要/Keywords/§1/(1) Vlasov-Poisson-Landau 方程（logΛ/2πΛ Q_L）/②self-induced
  force/W=1/|x|/Q_L [12]/Λ 从 10² 到 10³⁰ ✓；Landau [6] 预测段 ✓
- 结果：**PASS±**（±：arXiv 侧栏戳未收——惯例；页码未收）
## p.002
- 核对：§2/(3) hybrid 范数 ✓；**Theorem 1**（general interaction）陈述与 𝓛(k,ξ) 定义 ✓；
  假设区：**原文 (4)(5) 为并排双 display**（(4) sup|f̃⁰(η)|e^{2πλ|η|}≤C₀；(5) Σ(λⁿ/n!)‖∇_vⁿf⁰‖≤C₀）、
  (6) inf inf|𝓛(k,ξ)−1|≥κ、无标号 W 衰减条件、(7) δ:=‖f_i−f⁰‖≤ε ✓——
- 结果：**FAIL（结构）**：md 把 (4)(5) 两式**合并为一个 \tag{5} display**（内容双全）且
  "(4)" 标签悬挂为孤行文本。修复：拆分并恢复 \tag{4}/\tag{5}。
## p.003
- 核对：(8)(9) ✓；ρ_∞ 定义 ✓；Futhermore（**源级拼写，忠实**）✓；f_±∞ weak/strong 收敛 ✓；
  Comments on assumptions（Glassey-Schaeffer [4]/Jeans **unstability** length——源级拼写/Newton-
  Coulomb/(6) limit case）✓；Conclusions (1)-(5)（KAM 类比/homoclinic/filamentation/weak
  turbulence/radiation）✓
- 结果：**PASS±**（±：源级拼写 2 处登记）
## p.004
- 核对：§3/(10) 线性化/(11) Volterra/(12) K⁰ 核 ✓；两 bullet（source decay/e^{−λt}-
  Fourier-Laplace）✓；"suficient"（原刊 sufficient——ff→f 登记）✓
- 结果：**PASS±**
## p.005
- 核对：Fourier 反演法/(a)(b) 条件（φ_k marginal 定义）——md "calong" 多一杂 c（原刊 along）
  → **FAIL（单点）**；(a) Ŵ(k)≥0, zφ'_k(z)≤0 ✓；(b) 4π²(max|Ŵ|)(sup|f̃⁰|r dr)<1 ✓
- 结果：**FAIL（单点）**：calong→along。
## p.006
- 核对：§4 hybrid/gliding 范数、**(13)** 𝒵_τ 范数定义 ✓；"injection theorem **66** à la Sobolev"
  ——原刊无 66（乱码上标）→ **FAIL**；"(By default γ=0.)" ✓；**(14)** 𝓕 范数 ✓；Newton scheme
  (15)(16)(17) ✓
- 结果：**FAIL（单点）**：66 乱码清除（à la Sobolev）。
## p.007
- 核对：short-time CK 型估计 (17) ✓；characteristics (X,V)/scattering operators ✓；
  (18)(19)(20) 估计链 ✓；λ_n/μ_n → λ_∞/μ_∞、δ_n → 0 retroaction ✓；"；;" 双分号 ×2（md 伪影）
  → **FAIL（单点）**
- 结果：**FAIL（单点）**：;;→;。
## p.008
- 核对：regularity extortion σ(t,x) 定义与解释 ✓；**(21)** 估计 + 核 K(t,τ) 完整表达式 ✓；
  plasma echoes [7]/stabilizing role ✓
- 结果：**PASS±**（±："efect of plasma echoes" ff→f 登记）
## p.009
- 核对：γ>1 subexponential/ultrafast absorption ✓；γ=1 mode-by-mode/"an **b**infinite system"
  （原刊 an infinite，杂 b）→ **FAIL**；"diferent frequencies" ff→f 登记；dominant echo
  τ=kt/(k+1) ✓；(22) 短时 extortion ✓；"dificulties" ff→f 登记 ✓
- 结果：**FAIL（单点）**：binfinite→infinite。
## p.010
- 核对：**References [1]-[13] 逐条**（含源级拼写 Enlglish/landau damping/electic/On the landau
  damping——均忠实保留；ref [13] 的 "8 <sup>`</sup>" 乱码上标 → **FAIL**）✓；作者块
  （Cl´ement/C´edric/all´ee 重音游离 → **FAIL**；散入的 running head 一行 → **FAIL**）✓
- 结果：**FAIL（三点）**：重音 ×4 修复、杂行删除、ref[13] 乱码上标删除。

## 总评

- **覆盖声明**：10/10 页（p.1/p.10 全页抽验 + 全篇文本层逐字符对账）。mineru：standard 档
  （换件后重导出）。
- **FAIL 清单（9 点）**：(4)(5) 双 display 合并+标签悬挂；calong；66 乱码；;;×2；binfinite；
  重音游离 ×4；running head 杂行；ref[13] 乱码上标；中文逗号 ×3。
- **源级 typo（忠实不改）**：Futhermore/unstability×2/Enlglish/electic/landau damping（小写，
  ref[5][9]）/On the landau damping。
- **系统性伪影（登记不改）**：ff→f（suficient/coeficients/efect/diferent/dificulties）。
- **可用性结论**：修复后 md 可作该 note 忠实底本；与 Acta 长文（`Villani_Mouhot_2011_landau_published`）
  互为短长版本。

### 修复登记（2026-09-29）
- 14 组修复落实：(4)(5) 拆分为双 display（恢复 \tag{4}）；中文逗号 ×2；σ: 乱码；calong；
  66 乱码（→“à la Sobolev”）；binfinite；作者区 Clément/Cédric/allée/CNRS DMA 重音与杂行；
  ref[13] 乱码上标；ref[5]/[10] 游离 ´。
- **更正**：总评原记 ";;×2" 系读档误判（实为 ";$" 跨界形态，非缺陷）——该项撤销。
- ff→f 家族与源级 typo 按总评登记不改。
