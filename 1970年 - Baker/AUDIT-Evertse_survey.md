# AUDIT — J.-H. Evertse《Linear forms in logarithms》（2011 讲义/Master Course notes，pdfTeX born-digital，13p）

> mineru: standard 档云端解析；审计依据 = `audit/evertse_pNNN.png`（pngmono 150dpi）+
> pdftotext 文本层逐字符对账（born-digital，可靠）。衍生阅读件（Baker 主题现代综述）。

## p.001
- 核对：题录（LINEAR FORMS IN LOGARITHMS/JAN-HENDRIK EVERTSE/April 2011）✓；Literature
  （Shorey-Tijdeman CUP 1986/reprinted 2008）✓；§1/Thm 1.1（Gel'fond-Schneider 1934）✓；
  Cor 1.2（e^{πβ}）✓
- 结果：**PASS±**（±：页眉未收）
## p.002
- 核对：Cor 1.3 + 证明 ✓；线性无关定义 ✓；**Thm 1.4**（Baker 1966）✓；**Thm 1.5**（Baker 1975，
  (eB)^{−C}）✓；Cor 1.6 陈述 ✓
- 结果：**PASS±**
## p.003
- 核对：Cor 1.6 证明（|log(1+w)|⩽2|w|、2kπi 加模 2πi、|k|⩽C₂B）✓；**Thm 1.7**（Matveev 2000，
  C′=½e·m^{4.5}30^{m+3}∏max(1,logH(a_j))）✓；**Cor 1.8** + 证明 ✓；Catalan 猜想史
  （Tijdeman 1976/Mihailescu 2000 代数方法）✓；Thm 1.9（Tijdeman 1974，S-smooth 数列）✓
- 结果：**PASS±**（±：Mihailescu 拼写系原刊；数字列表空格排版）
## p.004
- 核对：Thm 1.9 证明（B⩽2log aₙ/log 2、(2e log aₙ/log 2)^{−C}）✓；p-adic 类比引言 ✓；
  **Thm 1.10**（Yu 1986）✓；§2 SML 定理：Γ 有限生成/(2.1) ax+by=1/**Gy˝ory 1979** Thm 2.1 ✓
- 结果：**FAIL（单点）**：Gy˝ory→Győry（人名重音，文本层 Gy̋ory 证实 ő；全篇 ×4）。
## p.005
- 核对：S-unit 归约 (2.2)/u+v=w/(2.3)/重排素数/Theorem 1.10 应用 p_t^{−B}、(eB)^{−C₂}⩽p_t^{−B} ✓；
  **Thm 2.2** ✓；Remark de Weger 1988 LLL/**545 solutions** ✓
- 结果：**FAIL（单点）**：随 p.4 族（Gy˝ory 不在本页）；"the x + y = z has precisely" 缺
  "equation" 一词——**文本层证实原刊即如此（源级笔误），忠实保留**。其余吻合。
## p.006
- 核对：**Thm 2.3**（(2.4) O_K* 单位方程）✓；**Cor 2.4**（二元形式 F(x,y)=m，三不同根）✓；
  **Cor 2.5**（yⁿ=f(x)）✓；单位论预备（embeddings/r₁+2r₂=d/Lemma 2.6 Norm=±1）✓
- 结果：**PASS±**
## p.007
- 核对：共轭绝对值积=1 ✓；**Lemma 2.7**（Dirichlet 单位定理精化版，L 映射/核=U_K/像为格）✓；
  (2.5) 唯一表示 ✓；(2.6) 矩阵 M 可逆 ✓
- 结果：**PASS±**
## p.008
- 核对：**Lemma 2.8**（max|bᵢ|⩽C·max log|σᵢ(ε)|）+ 证明（M⁻¹=L(ε)/三角不等式）✓；
  **Thm 2.3 证明**开头（ζ₁ζ₂ 单位表示/B=|b_r|）✓
- 结果：**PASS±**
## p.009
- 核对：Λᵢ 定义（=|σᵢ(b)σᵢ(y)|）✓；|σᵢ(y)|^{d−1}|σⱼ(y)|⩽1/|σᵢ(y)|⩽|σⱼ(y)|^{−1/(d−1)}⩽
  e^{−B/C(d−1)} ✓；Λᵢ⩽|σᵢ(β)|e^{−B/C(d−1)}——**σᵢ(β) 系原刊符号用法**（本证明无 β 定义，
  应为 b；源级 quirk，文本层证实，忠实保留）；脚注片段 "defined by (2.4)"——原刊交叉引用
  即印 (2.4)（应预期 (2.5)，源级引用笔误，忠实保留）
- 结果：**FAIL（块序，跨 p.009/p.010）**：见 p.010。
## p.010
- 核对：(eB)^{−C′}⩽|σᵢ(a)|e^{−B/C(d−1)} display ✓；"By Corollary 1.6 we have |Λᵢ|⩾(eB)^{−C′}…
  We infer / [display] and this leads to an effectively computable upper bound for B." ✓；
  Remark Wildanger 2000（K=ℚ(cos(2π/19))、degree 9、rank 8）✓；§3 Exercises 1(a)(b) ✓
- 结果：**FAIL（块序）**：md 将 (eB) display 提至 "By Corollary 1.6…We infer" 句之前——原刊
  顺序为 "…We infer / [display] / and this leads to…"（文本层证实跨页原序）。修复：复位。
## p.011–p.013
- 核对：Exercise 1-6 全部（二次/S-unit/Laurent-Mignotte-Nesterenko 2000 显式估计、
  97^m−89^n=8 上界计算题、xⁿ−2yⁿ=1 n>10000、Catalan 型/Exercise 6(a) p-adic |(1+a)^b−1|_p=|ab|_p、
  p^x−2^y=1 无解）逐条 ✓；p.13 尾 "y ⩾ 2." 收尾 ✓
- 结果：**PASS±**（±：Exercise 4 估计式中 −22 系数与 0.06/21 结构逐字 ✓）

## 总评

- **覆盖声明**：13/13 页逐页对账（born-digital 文本层可靠，逐字符核对 + p.1 PNG 抽验）。
  mineru：standard 档。
- **FAIL 清单（两点）**：Gy˝ory→Győry（×4，人名重音）；(eB) display 块序复位（跨 p.9/p.10）。
- **源级 quirk（忠实不改）**：①"the x + y = z has precisely 545 solutions" 缺 "equation"；
  ②"defined by (2.4)" 交叉引用（应预期 (2.5)）；③σᵢ(β) 符号（应预期 b）。
- **系统性伪影（登记不改）**：ff→f 家族（efectively ~15/diferent ~6/dificult ×2/coeficients）。
- **可用性结论**：修复后 md 可作该讲义忠实底本；作为 Baker 主题综述与 (I)-(IV) 审计链互补。

### 修复登记（2026-09-29）
- Gy˝ory→Győry ×3（全文复核确为 3 处，总评"×4"系计数笔误）；(eB) display 复位至 "We infer" 之后（原刊跨页原序）；Multi-plying→Multiplying。
  源级 quirk ×3 与 ff 家族按总评登记不改。fix commit 见 `git log --grep 'fix(md): Evertse'`。
- 本篇 13/13 页完成，无未决项。
