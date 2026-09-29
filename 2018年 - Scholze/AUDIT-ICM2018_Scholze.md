# AUDIT — Allyn Jackson《The Work of Peter Scholze》（ICM 2018 会议报告，pdfTeX born-digital，5p）

> mineru: standard 档云端解析；审计依据 = `audit/icm18_scholze_pNNN.png`（pngmono 150dpi）+
> pdftotext 文本层逐字符对账。

## p.001
- 核对：题录（The Work of Peter Scholze / Allyn Jackson）✓；开篇评价段（rarely emerges/inchoate/
  shrouded/unifying vision）✓；2011 会议 perfectoid 起源 ✓；solenoid 比喻 ✓；variety 入门
  （x²+y²=3z² 锥面/coeficients/characteristic p clock arithmetic）✓
- 结果：**FAIL（两点）**：①**md 块序错位**——标题块被排到首段之后（原刊标题在最前）；
  ②"thereby **setting of** a revolution"——原刊 "setting **off**"（文本层证实）。修复：标题块
  移至文件头；of→off。
- 备注：± 页眉未收；coeficients ff→f 伪影。

## p.002
- 核对：p-adic 数直观（close together/high power）✓；cohomology 类型（singular/de Rham/Hodge
  定理）✓；Grothendieck 1966 重构/étale cohomology/Galois group ✓；Grothendieck 猜 p-adic
  Hodge 理论 ✓
- 结果：**FAIL（单点）**：md "´etale **co-homology**"——原刊 "étale cohomology"（é 组合符
  游离 + 跨行假连字符；文本层 "étale cohomology"）。修复：´etale→étale（全篇 ×3）、去假连字符。

## p.003
- 核对：Fontaine 新对象/tilting 术语 ✓；Fontaine-Wintenberger 定理 ✓；Tate rigid-analytic/
  Huber adic spaces ✓；perfectoid 定义段（tilt/Étale/p-adic Hodge/n 维推广）✓；
  weight-monodromy（Deligne 1978）/Faltings almost purity（1986）✓
- 结果：**FAIL（两点）**：①"´etale cohomology"（é 游离，随全篇修复）；②"Galois-theoretic"
  被并作 "Galoistheoretic"（跨行连字丢失）。修复：补连字符。

## p.004
- 核对：Tate 1966 猜想/rigid-analytic 局部 perfectoid ✓；Bhatt-Morrow 积分 p-adic Hodge ✓；
  locally symmetric spaces/torsion classes/limit procedure/Langlands program ✓；universal
  cohomology/motives（Grothendieck/Voevodsky 2002）✓；light switch 比喻 ✓
- 结果：**FAIL（单点）**："integral version of **padic** Hodge theory"——原刊 "p-adic"
  （跨行连字丢失，文本层同形系 PDF 断行所致）。修复：padic→p-adic。

## p.005
- 核对：expositions/kind and generous/30 years/inspiring figure 收尾段 ✓
- 结果：**PASS±**（±：页眉未收；"The efect was exhilarating" ff→f 伪影——原刊 effect，
  属 ff 合字家族，随总评登记不单改）

## 总评

- **覆盖声明**：5/5 页逐页目检 + pdftotext 文本层逐字符对账。mineru：standard 档。
- **FAIL 清单（6 点）**：块序错位（标题后置）；setting of→off；´etale→étale ×3 + co-homology
  假连字符；Galoistheoretic→Galois-theoretic；padic→p-adic。
- **系统性伪影（登记不改）**：ff→f 家族（coeficients×3/diferent·diference×4/efect）。
- **可用性结论**：修复后 md 可作该报告忠实底本。

### 登记更正（2026-09-29）
- 前一"修复登记"先行落盘但修复当时未生效（´etale 实为 4 处非 3）；本 fix commit 为实际修复
  （étale ×4 + 其余 5 组）。以此为准。
