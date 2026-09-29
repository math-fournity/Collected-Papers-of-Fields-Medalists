# AUDIT — Inbo Gottlieb-Fenves《Superrigidity》（Margulis 超刚性讲义/exposition，pdfTeX born-digital，6p）

> mineru: standard 档云端解析；审计依据 = `audit/superrig_pNNN.png`（pngmono 150dpi）逐页目检 +
> 300dpi 抽样（`superrig_p001_300dpi.png` + thm_arrow_zoom / band）。
> **⚠️ 本 PDF 文本层被字体 cmap 损坏**：括号→pq（16 处）、<→ă（9 处）、×→ˆ（18 处）、∈→P、
> 𝔨→ℏ/\mathcal{k}/\mathscr{R}、箭头丢失——mineru 继承了全部乱码，文本层不能作对账真值，
> 审计以 PNG 印刷为准（born-digital 件按 corrupt-text-layer 扫描件处理）。

## p.001
- 核对：题录 ✓；§1（K/𝔨 扩张、𝔨 局部域特征 0、K 代数闭）✓；**Theorem 1.1**（Margulis
  Superrigidity：G⩽SLₙ(ℝ)、ℝ-rk⩾2、无紧因子、Γ 不可约格、H 单非紧 ℝ-代数群、π(Γ) Zariski 稠
  ⇒ π 延拓为有理同态 G **→** H——300dpi 证实实线箭头）✓；§2 + Prop 2.1 + 证明（graph-closure
  𝒵、Borel density、R=Rat(G/P,H/L) 作用、h₁h₂⁻¹ ∈ ⋂hLh⁻¹）✓
- 结果：**FAIL（族）**：①𝔨→\mathscr{R}；②πpΓq（括号 cmap）；③丢箭头 G→H（×2）。
## p.002
- 核对：ρ₂ρ₁:G→H、minimal parabolic P、**Prop 2.2**（Zimmer smoothness/Howe-Moore/H orbit
  Hμ/H/L 同胚）✓；**Prop 2.3** + 降维策略（P-invariant lift、U=unipotent lower）✓；
  **Lemma 2.4**（t₁,U₁,C₁ SL₃(ℝ) 矩阵例）✓；Lemma 2.5 ✓
- 结果：**PASS±**（±：cmap 族伪影见总评）
## p.003
- 核对：Lemma 2.5 证明（Fubini 归纳）✓；**Lemma 2.6**（B/automatic unipotence·rationality/
  ĥ:Cᵢ→N_G(B)/B 同态）✓；**Prop 2.7** + 证明（𝓕(Cᵢ,H/L)/Howe-Moore/essentially constant）✓
- 结果：**PASS±**
## p.004
- 核对：**Thm 3.1** Howe-Moore / **Thm 3.2**(i)(ii) Smoothness / **Thm 3.3** Borel Density /
  **Thm 3.4** Amenability Inheritance / **Thm 3.5** Automatic Rationality + exp/log 证明 ✓；
  "since 𝔞 ∈ 𝔫 is nilpotent"（md "a P n"→∈ cmap）→ FAIL；交换图 U→π→Nₙ/log↓exp↑/𝔲→dπ→𝔫ₙ
  （md 图结构乱）→ FAIL；Prop 3.6 "representaion"——**原刊源级拼写**（print 即如此，忠实）；
  Prop 3.7 ✓
- 结果：**FAIL（两点）**：①a P n→𝔞∈𝔫；②交换图结构重建。H_ℏ→H_𝔨（族）。
## p.005
- 核对：Prop 3.7 证明（Fubini/A_{r,s}/f(x,y) 有理分式/Cramer's rule）✓；§4 +
  **Prop 4.1**（(i) stabilizer compact / (ii) dim L < dim G——print 小于号，md "ă"）→ FAIL；
  **Prop 4.2**（weak mixing/ν×ν——print 乘号，md "ˆ"）→ FAIL
- 结果：**FAIL（族）**：ă→<、ˆ→×（含 H_𝔨 族）。
## p.006
- 核对：E_x={yK∈H/K:(xK,yK)∈𝒪}（print 花体 𝒪，md "θ"）→ FAIL；uKu⁻¹-orbit/compact/BB⁻¹ ✓；
  **Thm 4.3**（𝔨=ℂ 情形，Hausdorff topology——print 双 f，**md 丢 f**）→ FAIL；
  **Thm 4.4**（非阿基米德情形，L_𝔨⊆(H_𝔨)_μ、全不连通论证）✓；"Proposition 2.2.."双句点系
  原刊 quirk（md 单句点，登记不改）
- 结果：**FAIL（两点）**：θ→𝒪；Hausdorf→Hausdorff。

## 总评

- **覆盖声明**：6/6 页逐页目检 + 300dpi 抽样仲裁（p.1 箭头行）。**本文档文本层 cmap 损坏
  （括号/比较号/乘号/∈/𝔨 全部错映射），mineru 产出系统性继承乱码——本篇按 corrupt-text-layer
  流程以 PNG 为唯一真值审计**。
- **FAIL 族清单**：①𝔨 误读（\mathscr{R}/\mathcal{k}/ℏ，全篇 ~10 处）；②括号 pq（πpΓq 等，
  全篇 ~16 处）；③ă→<（1 处语义位）；④ˆ→×（1 处语义位）；⑤丢箭头（Thm 1.1/Prop 2.1/Prop
  2.7 等 4 处）；⑥𝒪→θ；⑦Hausdorff 丢 ff；⑧"a P n"→𝔞∈𝔫；⑨交换图结构。源级 quirk
  （忠实不改）：representaion 拼写、"proceed via"（原刊如此）、"Proposition 2.2.."双句点、
  "we induct" 小写、"the H_𝔨 acts"。
- **可用性结论**：系统性修复后 md 可作该讲义忠实底本；修复以"族"为单位逐一核验。

### 修复登记（2026-09-29）
- 15 组族修复共 33 处：𝔨（\mathscr{R}×1、\mathcal{k}×12、H_\hbar×9 → \mathfrak{k}）；
  丢箭头 ×5（→）；πpΓq→π(Γ)；ă→<；ˆ→×；θ→𝒪；Hausdorf→Hausdorff；a P n→𝔞∈𝔫；
  ∈]R→∈ℝ；交换图重建（U→Nₙ / log↓exp↑ / 𝔲→𝔫ₙ 三行 array）。
- fix commit 见 `git log --grep 'fix(md): Superrigidity'`；修复前 md = 父提交。
- 残留检查：pΓq/ă/ˆ/\hbar/\mathcal{k}/\mathscr{R}/双空格箭头全数清零。

### 登记更正（2026-09-29）
- 前一登记"全数清零"不实：残留核查发现 3 处漏网（Prop 2.1 末尾丢箭头、§2 lift 丢箭头、
  L_𝔨——H_ℏ 替换模式未覆盖 L 开头的同族）——已补修并经 grep 复核为 0。教训：族修复后必须
  以宽松模式全文复核，且替换模式要覆盖同族变体（H_/L_ 前缀）。
