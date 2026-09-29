# AUDIT — Adam J Harper《A version of Baker's theorem on linear forms in logarithms》（2010 讲义/exposition，MiKTeX pdfTeX born-digital，7p）

> mineru: standard 档云端解析；审计依据 = `audit/harper_pNNN.png`（pngmono 150dpi）+
> pdftotext 文本层逐字符对账（本文本层可靠）。

## p.001
- 核对：题录（Adam J Harper/1st December 2010）✓；Abstract ✓；§1（1966/Baker/Fields 1970）✓；
  **Baker's Theorem 1**（weak version，含 2πi 假设）✓；weakness 讨论（2πi 可去/effective 界）✓；
  e 超越性证明提纲（反证/ nice 函数 F 逼近/非零小分母有理数）✓
- 结果：**PASS±**（±：项目符号"•"被并入显示式行（排版级）；页码未收）
## p.002
- 核对：提纲收尾/key work 强调 ✓；反设 β₁logα₁+…=0、WLOG 归约 −logαₙ ✓；φ(z) 构造预告/
  extrapolation 描述（"playing **off**"——原刊 off，**md 丢 f → FAIL**）✓；Gelfond-Schneider 1934/
  [3] Gelfond "analytic-arithmetic continuation" ✓
- 结果：**FAIL（单点）**：playing of→off。
## p.003
- 核对：§2 φ(z) 定义（L=[h^{2−1/(4n)}]、|p(λ)|⩽e^{h³}、vanishing 条件）✓；等价改写（λₙβᵢ 项）✓；
  乘 (a₁⋯aₙ)^{Lz}b₁^{m₁}⋯ 后的线性方程组陈述 ✓
- 结果：**PASS±**（±：页码未收）
## p.004
- 核对：M⩽(h²+1)^{n−1}hd^{2n−1}、(L+1)^n⩾h^{2n−1/4}⩾2M ✓；|a^{(j)}|,|b^{(j)}|⩽C^j ✓；
  乘积界 K^{Lh}/(KL)^{h²} ✓；**Siegel's Lemma**（1+(N max|u_{ij}|)^{M/(N−M)}）✓
- 结果：**PASS±**（±：页码未收）
## p.005
- 核对：§3 估计一（e^{h³}(KL)^{h²}K^{L|z|}）✓；|d^m/dz^m φ(z)|⩽K^{h³+L|z|} ✓；§3 估计二
  （X 代数整 数/degree d^{2n−1}/Tower Law/Liouville 式 |X|⩾K^{−d^{2n−2}(h³+Lz)}）✓；
  f_{m₁,…} 二择一（0 或 ⩾K^{−h³−Lz}）✓
- 结果：**PASS±**（±：页码未收；Liouvilleesque 连字丢失登记）
## p.006
- 核对：§4 extrapolation + **Baker's Lemma 1**（C≫T/(A log A)+UBA^ε、条件(1)(2)、结论
  **e^{−2(T+Uz)}** 因子 2 经 PNG 确证 ✓、C/2 与 [AB]）✓；maximum-modulus 证明（g(z)/(z−1)^{[C/2]}…、
  A^{1+ε}B 圆、e^{−(ε/2)log A[A][C/2]}）✓；"Using the assumption (1), and that AC≫(T/log A)+
  UA^{1+ε}B" ✓；应用段（T=h³logK、U=L logK、B=h^{1/8n}、O(n²) 次迭代）✓
- 结果：**PASS±**（±：页码未收）
## p.007
- 核对：§5 结论（Vandermonde/(L+1)^n×(L+1)^n 行列式/λ 元组相等矛盾）✓；Q.E.D. ✓；"robust"
  讨论 ✓；References [1]-[3]（Mathematika 13, pp 204-216, 1966；CUP Reissue 1990；Dover 1960）✓
- 结果：**PASS±**（±：页码未收）

## 总评

- **覆盖声明**：7/7 页逐页目检 + pdftotext 文本层逐字符对账（可靠文本层）。mineru：standard 档。
- **FAIL 清单（1 点）**：playing of→off（p.2）。
- **系统性伪影（登记不改）**：ff→f 家族（efective/efectively/sufices/coeficient(s)×3/diferent×3/
  efect？——原刊均双 f）；Liouvilleesque 连字丢失；孤立 "z.." 双句点 ×2；项目符号并入显示式。
- **可用性结论**：修复 1 点后 md 可作该讲义忠实底本。本篇为 Baker 主题的现代二次文献，
  与 (I)(II) 原文审计件互为参照。

### 修复登记（2026-09-29）
- playing of→off。fix commit 见 `git log --grep 'fix(md): Harper'`。
