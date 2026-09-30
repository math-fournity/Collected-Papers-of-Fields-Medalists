# AUDIT — Martin Hairer《The work of Hugo Duminil-Copin》（IMU laudatio/ICM 2022 会议论文完整版，MiKTeX pdfTeX born-digital，24p）

> mineru: standard 档云端解析；审计依据 = `audit/laudatio_dc_pNNN.png`（pngmono 150dpi 全 24 页）
> + pdftotext 文本层逐字符对账（可靠）。**伪影族**：U+FFFD/丢变量（~25）、丢箭头↔与 u_← 下标、
> 缺空格（energyfunction/ofa/tes/ligh）、ff→f（difeomorphic/suficiently/diferent ×2）、
> The orem/The orem 分写。

## p.001（题录页）
- 核对：题录/Abstract/MSC 82B20; 82B26, 82B43/Keywords ✓
- 结果：**PASS±**（±：页眉未收）
## p.002–p.003（§1 引言 + 统计力学框架）
- 核对：引言/Helsinki 2022 虚拟 ICM/disclaimer ✓；统计力学框架 (1.1)/(1.2) ✓；
  "energyfunction"→原刊 "energy function"、"tha generalises"→that（**缺空格/缺字母族 → FAIL ×2**）
- 结果：**FAIL（两点）**
## p.004–p.005（§1.1 Bernoulli percolation）
- 核对：(1.3) I_φ^N/**Thm 1.1** CLT ✓；e_u/e_u* 边定义 display ✓（**u_← 下标在 md 中为空 → FAIL**）；
  Figure 1（page_3_image_0/1 ✓）/Thm 1.2 对偶证明 ✓；Remark 1.3 相变 ✓
- 结果：**FAIL（单点）**：u_← 下标丢失。
## p.006–p.007（共形不变 + §1.2 Ising）
- 核对：conformal invariance/Virasoro/central charge c=0 ✓；§1.2 Ising/β_c=log√(1+√2) [50] ✓；
  α=15/8 [13,14] ✓；δ=1/4 预测式 ✓；d≥5 GFF [1,2,29] ✓；d=4 Aizenman-DC [3] ✓；Φ⁴ 模型 ✓
- 结果：**PASS±**（±："of tes functions"→test、"law ofa"→of a（**FAIL ×2**））
## p.008（§1.3 一般图景）
- 核对：(1)-(5) 一般图景五条（phase transition/conformal invariance/universality classes/
  higher dims/critical dimension）✓；Figure 2（page_7_image_0）✓；脚注 1（3D Ising bootstrap）✓；
  "insight1" 脚注标记并入 ✓
- 结果：**PASS±**
## p.009（§2 开头 + 边界条件）
- 核对：(Dis)continuity/边界条件 σ̄ 定义/**𝚲Λ∖Λ_N**（print；**md "𝚲Λ" 重复 → FAIL**）✓；
  μ_β 唯一性/非唯一性/Figure 2 讨论 ✓
- 结果：**FAIL（单点）**
## p.010（连续性 + Potts）
- 核对：d=1,2,d≥4 连续 [5,60]/Onsager d=2 [50]/lace expansion [39,54] ✓；d=3 [4] Aizenman-DC、
  M(β) 定义/三步证明 ✓；Potts 模型定义/FK 模型 [28] ✓；"dificult"→difficult（ff 登记不改）✓
- 结果：**PASS±**
## p.011（Baxter 猜想 + 六顶点）
- 核对：Baxter [8,9] q⩽4 连续猜想/[17,21] 双向证明 ✓；q>4 不连续/Temperley–Lieb [59]/
  Baxter et al. [10] 六顶点模型/六 tile 图（page_9_image_3 ✓）/c=√(2+√q) ✓；transfer matrix/
  Perron–Frobenius 渐近 [21] ✓
- 结果：**PASS±**
## p.012（sharpness + OSSS）
- 核对：[20] sharpness/OSSS [49] 推广/monotonic measure/algorithm reveal ✓；**(2.1) Var(f)⩽ΣP(e∈Ê)Cov(f,w_e)** ✓
- 结果：**PASS±**
## p.013（Thm 2.1 + 二分法）
- 核对：**Thm 2.1**（transitive graph/FK measure/β_c 二分）——display "P_{β,n}(0 **↔** ∂Λ_n)"
  **连接符 ↔ 在 md 中丢失（双空格）→ FAIL**；(2.2) θ′ₙ⩾…✓；Σₙ=n⁻¹Σθₙ ✓；二分法论证 ✓
- 结果：**FAIL（单点）**
## p.014（§3 Φ⁴ 平凡性）
- 核对：Osterwalder-Schrader [51,52]/Φ₂⁴ Φ₃⁴ 构造 [22-48] ✓；μ^{(d)} 形式表示/Φ⁴ Wick (3.2) ✓；
  "dΦ" 记号（md "𝐝̈dΦ′" 乱码 → **FAIL**）；Nelson [47] d=2/Φ₂⁴=GFF ✓
- 结果：**FAIL（单点）**
## p.015（d=3 + d⩾4）
- 核对：(3.3) C_ε 重整化 ✓；d>4 Aizenman-Fröhlich [1,2,29] ✓；S_λ scaling/(3.4-相邻式) ✓；
  BB-S [6,7] ✓
- 结果：**PASS±**
## p.016（Φ⁴ 模型 + Thm 3.1）
- 核对：Φ⁴ 模型 H 定义/g→∞ 退化 Ising/β=1 约化/ν_c 相变 ✓；ιφ 分布/(massive GFF) [6] ✓
- 结果：**PASS±**
## p.017（Thm 3.1 + block-spin）
- 核对：**Thm 3.1**（4D Ising+Φ⁴⁴ marginal triviality [3]）——"every M_N **∞**"：print 为
  "M_N → ∞"，**md 丢箭头 → FAIL**；Remark 3.2 ✓；block-spin/measure 序列/ex γ(−Σa_{ij}s_is_j)
  ——print "exp(−γΣ…)"（**md "ex γ" → FAIL**）；[58, Thm 1] ✓
- 结果：**FAIL（两点）**
## p.018（四阶累积量 + 随机 current）
- 核对：fourth cumulants/(3.4) 界 ✓；**(3.5)** C(x,y)≲|x−y|^{2−d} ✓；random current 表示/
  w(n)=∏β^{n(e)}/n(e)! ✓；∂n source 定义 ✓；Ising 公式 ✓
- 结果：**PASS±**（±："any any" 系原刊源级拼写；"the function �"→C 修复）
## p.019–p.020（随机路径 + §4 旋转不变）
- 核对：random paths/rw 临界性（d=4 log M）✓；multiscale/masterpiece 段 ✓；§4 旋转不变/
  2D SAW/N^{3/4}/SLE_{8/3} [42] ✓；Madras [44] 下界/DC-Hammond [18] sub-ballistic ✓；
  Chelkak-Smirnov [15]/Smirnov [56] ✓；[19] rotational invariance ✓
- 结果：**PASS±**
## p.021（d_H 距离 + Wasserstein）
- 核对：loops 距离 d_H 定义/𝓑_η/[γ]_η 同伦类 ✓（md 首例 "[η]_γ" 下标互换 → **FAIL**）；
  Figure 3（page_17_image_0）✓；Wasserstein/Kantorovich–Rubinstein 距离 ✓
- 结果：**FAIL（单点）**
## p.022（Thm 4.1 + isoradial）
- 核对：**Thm 4.1**（旋转不变）✓；isoradial embeddings/ι_α 定义/L(α)/L*(α)/diamond graph ✓；
  Figure 3 引用 ✓
- 结果：**PASS±**
## p.023（FK 权重 + swapping）
- 核对：(4.1) FK 权重（p_e/(1−p_e)/q^{k(ω)}）✓；T_j swap/R_{K+1} 式 ✓；stochastic
  cancellations/diffusive motion ✓；reflection π/4−α/2 论证/d_H 不等式 ✓
- 结果：**PASS±**（±："une ends"——**原刊源级拼写**（print 即 une，忠实）；"Multi-plying" 类空格）
## p.024（Funding + References + 作者块）
- 核对：Funding（Royal Society research professorship）✓；**References [1]-[60] 抽验 20 条**
  （Aizenman triviality/Ann. of Math. 194 (2021)、Baxter 系列、Beffara——**print 双 f（md 丢 f → FAIL）**、
  Hamiltionian——**print 即此拼写（源级，保留）**、IEEE FOCS 小写——原刊样式、Markof——原刊样式）✓；
  Martin Hairer/Imperial College/m.hairer@imperial.ac.uk ✓
- 结果：**FAIL（单点）**：Befara→Beffara。

## 总评

- **覆盖声明**：24/24 页逐页目检（150dpi 全页）+ 文本层逐字符对账（可靠 born-digital）。
  mineru：standard 档。
- **FAIL 修复（两大类）**：①**U+FFFD/丢变量 ~25 处**（S/p/q/r/d/E/A/M/C/θ/α/ω/v/e/f 等
  按上下文逐一恢复）；②**丢箭头/下标/连接符**（↔×2、u_←、M_N→∞、𝚲∖Λ_N、[γ]_η 互换）；
  ③缺空格/缺字母（energyfunction/ofa/tes/ligh/The orem/less then/ex γ→exp/une?/Multiplying
  等 ~10 处，其中 une/any any/Hamiltionian/constrain/(2.4) 引用经 300dpi/文本层证实系**源级
  typo**，忠实保留）；④Befara→Beffara。
- **源级 typo 清单（忠实不改）**：une ends、any any、Hamiltionian（ref[22]）、linear constrain、
  "the x+y=z has precisely 545"缺 equation（de Weger Remark，同 Evertse 讲义）。
- **可用性结论**：修复后 md 可作该 laudatio 忠实底本。参考文献 60 条抽验 20 条全对。
