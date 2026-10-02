# AUDIT-Scholze_2012_perfectoid_published

- actor：Wf-P44
- host/model/effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF：`2018年 - Scholze/Scholze_2012_perfectoid_published.pdf`（69 PDF 页 = 印刷 pp.245–313，Pub. IHÉS 116 (2012)）
- PDF SHA256：`7e7f7a3b6309ead9d8ee376106c92c644f25b22d75ffa6d7382508a36cf7814a`（本次 session 实测复核一致）
- MD 基线 SHA256：`089d58912047de5c0e3439428e48d78b63eda9856562a14fd335a1b5929d7481`（= 原始 mineru 导出 commit d87578ba，本次 session 实测复核一致）
- 日期时间：2026-10-02 13:33 EDT 开工
- 文本层通道判定：**可用**。`pdftotext -f 1 -l 1` 首页抽取干净（标题/摘要/目录/正文完整、公式线性化可读），全程采用「pdftotext 文本层主对账 + pngmono 150dpi PNG 视觉核验」双通道。
- 审计方式：逐页交错（渲染→目检→五点比对→分级→修复→落签→提交），每页一 commit；print quirk 忠实登记不改，MinerU OCR 内容错误按原图证据逐处 Edit 修复。

---
## p.001（PDF p.1 / 印刷 p.245）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：题录（标题 PERFECTOID SPACES / by PETER SCHOLZE、ABSTRACT、CONTENTS 11 条页码 245/252/263/267/272/283/295/303/307/311/312、页脚 DOI 10.1007/s10240-012-0042-x）；§1 Introduction 节标题；Theorem 1.1 陈述（Q_p(p^{1/p^∞}) 与 F_p((t)) 绝对 Galois 群典范同构）；首段与次段公式与上下标
- 结果：**FAIL**（MinerU OCR 数学内容错误，已当页修复，以原图为准）：
  1. 首段 `Q_b`→印刷为 $\mathbf{Q}_p$；`F_{φ}`→$\mathbf{F}_p$；"characteristic$\cdot\cdot\cdot\cdot\cdot$"→"characteristic $p$."；"characteristic$\beta .$."→"characteristic $p$."（p.245 左栏/正文首段）
  2. 首段 "some ofthe"、"is ofcharacteristic"、"ofthis"、"ofFaltings's" 缺空格 → 修正；"weightmonodromy" → "weight-monodromy"（印刷跨行连字符 "weight-/monodromy"）
  3. Theorem 1.1：`$\mathbf{\tilde{Q}}_{\theta}(\theta^{1/p^\infty})$`→$\mathbf{Q}_p(p^{1/p^\infty})$；`$\mathbf{F}_p({\it\Delta\phi}(t))$`→$\mathbf{F}_p((t))$（p.245 定理行原图）
  4. "roots o$\dot{\boldsymbol{p}}$"→"roots of $p$"；`Q_ν(\dot p^{1/p^∞})`→$\mathbf{Q}_p(p^{1/p^\infty})$；`F_p(\r(t))(t^{1/p^∞})`→$\mathbf{F}_p((t))(t^{1/p^\infty})$（p.245 末段）
- 备注：摘要与 CONTENTS 文字、页码全部吻合；印刷版为数字排版，无 print quirk；所有差异均为 MinerU OCR 对 p/𝑝 字形与双括号的系统性误读（p 在下标/正文被读作 b/θ/ν/φ/β/···）。
