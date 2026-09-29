# AUDIT — Allyn Jackson《The Work of Caucher Birkar》（ICM 2018 会议报告，pdfTeX born-digital，5p）

> mineru: standard 档云端解析；审计依据 = `audit/icm18_birkar_pNNN.png`（pngmono 150dpi）+
> pdftotext 文本层逐字符对账。

## p.001
- 核对：Jackson 署名 ✓；代数几何入门（algebraic variety/x²+y²=z² 三种数域/Pythagorean triples）✓；
  birational geometry 与 MMP 目标 ✓
- 结果：**PASS±**（±：页码未收；diferent ff→f 伪影）

## p.002
- 核对：Riemann 一维分类（三种曲率/donut 孔数）✓；意大利学派二维/(-1)-curve blow up-down ✓；
  三分类（**Mori-Fano** fiber spaces——原刊此处用 Mori-Fano 序，md 忠实）/Calabi-Yau/general type ✓；
  Mori 三维 flip/1990 Fields ✓
- 结果：**FAIL（单点）**：md "entirely new **blowingdown** procedure"——原刊 "blowing-down"
  （文本层证实）。修复：补连字符。

## p.003
- 核对：三维粗分类（**Fano-Mori** fiber spaces——原刊此处倒序 Fano-Mori，两页两种序并存系原刊
  原样，md 忠实）✓；log MMP/Shokurov ✓；2003 四维 flips/新哲学 ✓；Birkar-BCHM 缘起 ✓
- 结果：**FAIL（单点）**：md "BCHM answered **afirmatively**"——原刊 "affirmatively"（ff→f）。
  修复：补 ff。

## p.004
- 核对：canonical bundle/ring、flips 全维存在、general type 极小模型 ✓；2016 两论文/
  Borisov-Alexeev-Borisov 猜想/mild singularities 有限参数 ✓；seminars worldwide ✓；
  higher-dim Calabi-Yau mystery ✓；characteristic p frontier（{0,1,…,p−1} clock arithmetic）✓
- 结果：**FAIL（单点）**：md "open-ing areas previously thought"——原刊 "opening"（连字符系
  mineru 误留跨行残迹；文本层无 open-ing）。修复：open-ing→opening。

## p.005
- 核对：Hacon-Xu 基础上三维 log flips/log minimal models（p>5）✓；收尾评价段（facility/
  fearlessness/poised）✓——
- 结果：**FAIL（单点）**：md "when $p > 5$" 丢句号——原刊 "when p > 5**.**"（文本层证实）。
  修复：补句号。

## 总评
- 5/5 页逐页目检+文本层对账；FAIL 4 点（blowingdown/afirmatively/open-ing/丢句号——均
  ff 合字与跨行残迹类伪影）修复后可作忠实底本；原刊 quirk 1 项（Mori-Fano 与 Fano-Mori
  两序并存）忠实保留。

### 修复登记（2026-09-29）
- blowingdown→blowing-down；afirmatively→affirmatively；open-ing→opening；p>5 补句号。
  fix commit 见 `git log --grep 'fix(md): ICM2018 Birkar'`。
