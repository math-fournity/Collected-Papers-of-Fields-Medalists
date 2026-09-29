# AUDIT — "On the work of Alan Baker"（Turán 撰，ICM 1970 Tome 1, p.5-6）

> 二值化渲染 audit/pNNN.png（pngmono 150dpi）对照 Baker_1970_work_report_mineru md。逐页一签。

## p.001（PDF p.1 / 印刷 p.5-6 上半）
- PNG：audit/p001.png
- 核对：
  - 正文续段：exp(10⁷) 第十个虚二次域判据 ✓、d₀ < exp(10⁷) ✓、Gelfond-Linnik 三项和
    有效下界 ✓、Baker 一般结果给出 d₀ = 10⁵⁰⁰ ✓、Stark 独立证明非存在 ✓
  - Linnik 二次型系数有效化（ergodic theory 思路）✓
  - 结尾两段（hard-analysis type、Baker 本人将在大会报告、"two different ways of doing
    mathematics … peaceful coexistence"）✓ 逐字吻合
  - 署名块：P. TURÁN, Mathematical Institute of the Hungarian Academy of Sciences,
    Budapest, Hungary ✓；Alan BAKER, Trinity College, Cambridge (Grande-Bretagne) ✓
- 结果：**PASS±（含一处必须警示的幻觉段落）**
  - ⚠️ **mineru 幻觉**：md 末尾出现一段 "The Ground Truth image displays a single,
    solid horizontal line… OCR has hallucinated text…"——这是 mineru 视觉模型把页面
    分隔装饰线编造成了"OCR 自检说明"，**原页面无此文字，阅读时必须忽略（建议删除）**。
    除该段外，论文内容转写逐字正确。
  - ±：running head（ON THE WORK OF ALAN BAKER / 页码 5）丢失。

## p.002（PDF p.2）
- PNG：audit/p002.png
- 核对：原文即为空白页（仅版面噪声点），md 无对应内容 ✓
- 结果：**PASS**

## 总评
- 2 页逐页审计完成；论文内容转写正确，但 **md 含一段 mineru 幻觉文本（p.001 末）**，
  使用该 md 时须剔除最后一段。其余同系统性瑕疵（running head 丢失）。

> **修复登记（2026-09-29）**：已按本审计删除 md 末尾 mineru 幻觉段（"The Ground Truth image…" 整段）；修复与本登记同一 commit；修复前 md 见该 commit 父提交。
