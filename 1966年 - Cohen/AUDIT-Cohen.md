# AUDIT — Cohen "The independence of the continuum hypothesis" (PNAS 50 (1963), 1143-1148)

> 二值化渲染 audit/p001-p006.png（pngmono 150dpi）对照 Cohen_1963_continuum_hypothesis_mineru md。逐页一签。
> 注：PNAS 页面物理上前后各带邻文（前：生化论文参考文献尾；后：Black et al. SV40 病毒学论文开头）——PDF 下载自然截断，md 一并转写，属正常现象非错误。

## p.001（印刷 p.1143）
- 核对：前文参考文献尾 ¹⁹-³² 逐条 ✓（Gardner/Khorana/Ames/…/Krakow-Ochoa，全部生化文献）；
  标题 THE INDEPENDENCE OF THE CONTINUUM HYPOTHESIS ✓；By Paul J. Cohen* ✓；
  Stanford ✓；**Communicated by Kurt Gödel, September 30, 1963** ✓（历史性细节）；
  引言（Z-F、Axiom of Regularity、model 定义、Gödel 一致性结果）✓；
  THEOREM 1 四部分：(1) 非 constructible 的 a⊆ω 而 AC 与 GCH 成立 ✓；
  (2) 连续统 P(ω) 无良序 ✓；(3) AC 成立但 ℵ₁ ≠ 2^{ℵ₀} ✓；(4) 可数对选择公理失败 ✓；
  "Only part 3 will be discussed in this paper" ✓
- 结果：**PASS±**（±：页眉 1143 / MATHEMATICS: P. J. COHEN / Proc. N.A.S. 丢失）

## p.002（印刷 p.1144）
- 核对：直观思路段（Löwenheim-Skolem 可数模型 𝔐、a_δ ⊆ ω、V={⟨a_δ,a_δ′⟩}、
  generic 子集、"each a_δ contains infinitely many primes, has no asymptotic density"）✓；
  𝔐 满足 V=L 且 x∈𝔐⟹x⊂𝔐 的归约（Ψ 超限归纳）✓；
  LEMMA 1（j, K₁, K₂, N 唯一性，(1)-(5) 全部条件含 j(0)=3ℵ_τ+1、序保持三元组编码）✓；
  Definition 1 (1)-(4)（F_α 归纳定义，α=3ℵ_τ 时 F_α=V）✓
- 结果：**PASS**

## p.003（印刷 p.1145）
- 核对：𝔉₁-𝔉₈（Gödel 八个初等运算）逐条 ✓；N=9 情形与 T_α ✓；𝔐⊆𝔑 ✓；
  Definition 2（formulas 归纳定义）✓；Definition 3（Limited/Unlimited Statement）✓；
  Definition 4（rank=(α,r) 与序）✓；Definition 5（finite conditions P）✓；
  type 𝔯 定义与 limited statements 排序修改 ✓
- 结果：**PASS**

## p.004（印刷 p.1146）
- 核对：**Definition 6（forcing 定义——全文关键点）** I/II/III + (i)-(v) 逐条 ✓：
  (i) α,β ≤ 3ℵ_τ 时形式后承 ✓；(ii) ¬F_α∈F_α 恒被 force ✓；(iii) ψᵢ limited statement
  表达 F_β 定义（ψ₀-ψ₈ 列表）✓；(iv) N(β)=9 情形 ✓；(v) α>β 归约 ✓；
  "The most important part of Definition 6 is I" ✓；Definition 7（unlimited statements）✓；
  LEMMA 2（P 不可能同时 force a 与 ¬a）✓ 及 Proof 开头 ✓
- 结果：**PASS**

## p.005（印刷 p.1147）
- 核对：Lemma 2 证明续（parts (iv)/(v) 归纳收尾）✓；LEMMA 3（P′ ⊃ P 单调性）✓；
  LEMMA 4（可扩至 force a 或 ¬a）✓ 及 Proof ✓；Definition 8（P₂ₙ 枚举）✓；
  **LEMMA 5（被 force 的语句在 𝔑 中为真，反之亦然——forcing 合法性核心）** ✓ 及 Proof ✓；
  "Lemma 5 is the justification of the definition of forcing" ✓
- 结果：**PASS**

## p.006（印刷 p.1148）
- 核对：结尾句 "In the next paper, we shall prove that 𝔑 is a model for Z-F in which
  part 3 of Theorem 1 holds." ✓；脚注 \*（Alfred P. Sloan Foundation fellow）✓；
  References 1-5 逐条：Cohen, Bull. Amer. Math. Soc., 69, 537-540 (1963) ✓；
  Fraenkel-Bar-Hillel, Foundations of Set Theory (1958) ✓；Gödel, Princeton 1940 ✓；
  Shepherdson, J. Symbolic Logic, 17, 225-237 (1957) ✓；Sierpinski, Fund. Math., 34,
  1-5 (1947) ✓；后文（Black et al. SV40）自然截断 ✓
- 结果：**PASS±**（±：本页兼含后文开头，属 PDF 物理边界）

## 总评
- 6 页逐页审计完成：**全部 PASS，零数学错误**——forcing 定义、𝔉₁-𝔉₈、五个 Lemma、
  Gödel 通信人信息等关键内容逐字保真；
- 系统性瑕疵：页眉/页码丢失、邻文页面一并转写（物理边界，非错误）。
- 结论：md 可作为正文引用与检索底本。
