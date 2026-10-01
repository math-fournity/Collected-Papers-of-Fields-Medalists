# AUDIT — V. G. Drinfeld, “Elliptic Modules”

## 当前状态

- Source PDF：`Drinfeld_1974_elliptic_modules.pdf`，32 个 PDF 页面；Creator 为 ABBYY FineReader。PDF 中每页包含 400dpi 单色整页图像，并另带 OCR 文本层。本篇按扫描件模式执行，OCR/`pdftotext` 仅作定位辅助，原页图像为权威。
- MinerU Markdown：`Drinfeld_1974_elliptic_modules_mineru/Drinfeld_1974_elliptic_modules__Drinfeld_1974_elliptic_modules.md`。
- 已完成：1/32 页目检与对照；尚未修复 Markdown。其余 31 页未审。

## p.001（PDF p.1 / 印刷 p.561）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p001.png`（pngmono 150dpi）
- 核对：题名、作者、UDC、摘要、Bibliography 14 items、Introduction 开头、admissible triple 定义与四类、首段记号说明、AMS subject classifications。
- 结果：PASS±。可见正文与现有 Markdown 相符；Markdown 未保留印刷页眉中的 `Mat. Sbornik, Tom 94 (136) (1974), No. 4`、`Math. USSR Sbornik, Vol. 23 (1974), No. 4`，也未保留印刷页码 561。作为扫描件版面的页眉/页码遗漏记录；题名、作者、摘要及正文内容仍可辨认，当前不据此误改正文。
- 依据：本页完整 150dpi 源页 PNG；页级 OCR 文本仅用于定位，未用它覆盖源页判断。

## p.002（PDF p.2 / 印刷 p.562）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p002.png`（pngmono 150dpi）
- 核对：elliptic A-module 定义、level `I` 结构定义、光滑模空间段落、Theorem 1、Theorem 2 两项陈述、四类 triples 的过渡段、B) Outline 开头与 “cusp form” 编辑注。
- 结果：PASS±。现有 Markdown 对应正文和编辑注与源页相符；Markdown 未保留印刷页眉中的作者名和印刷页码 562。复杂公式按源页视觉核对，未根据噪声 OCR 文本替换。
- 依据：本页完整 150dpi 源页 PNG；OCR 文本仅作定位辅助。

## p.003（PDF p.3 / 印刷 p.563）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p003.png`（pngmono 150dpi）
- 核对：B) Outline 的收尾、作者致谢、§1 标题、formal group 定义、加法群例子、特征 `p` 下 Frobenius `τ` 与交换关系、formal O-module 定义及 germ/函子段、Proposition 1.1 开头。
- 结果：PASS±。可见正文与现有 Markdown 相符；Markdown 未保留页眉题名 `ELLIPTIC MODULES` 及印刷页码 563。底部 Proposition 1.1 在本页只出现引入句，后续关系式待下一页继续核对。
- 依据：本页完整 150dpi 源页 PNG；OCR 文本仅作定位辅助。

## p.004（PDF p.4 / 印刷 p.564）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p004.png`（pngmono 150dpi）
- 300dpi 局部证据：`audit/300dpi/Drinfeld_1974_elliptic_modules_p004_relations.png`、`audit/300dpi/Drinfeld_1974_elliptic_modules_p004_proposition.png`、`audit/300dpi/Drinfeld_1974_elliptic_modules_p004_prop13.png`
- 核对：Proposition 1.1 的 (1)–(3) 关系及证明、Proposition 1.2、局部非阿基米德情形开头与 Proposition 1.3。
- 结果：FAIL。印刷 p.564 的 300dpi 原图在 Proposition 1.1 证明、Proposition 1.3 陈述和其证明开头均印作 `h(a)`；现有 Markdown 对应处写作 `b(a)`（当前 MD 第 101、125、129 行），会改变符号。应待全篇审计完成后用 Edit 逐处改为源页 `h(a)`，再复核最终 Markdown；本页签字时尚未修改。
- 源级 quirk：印刷 p.564 的 Proposition 1.2 证明原样出现 “If `O ⊂ F_{p^k}`” 后又给出 `a ∉ F_{p^k}` 的条件，二者表面不相容；留存的 300dpi 源页裁片显示印刷关系符未带否定斜线。按 print 忠实保留，列为原文 quirk，不据数学推断改写。
- 另记：Markdown 未保留页眉作者名与印刷页码 564。

## p.005（PDF p.5 / 印刷 p.565）

- PNG：`audit/Drinfeld_1974_elliptic_modules_p005.png`（pngmono 150dpi）
- 300dpi 局部证据：`audit/300dpi/Drinfeld_1974_elliptic_modules_p005_h.png`、`audit/300dpi/Drinfeld_1974_elliptic_modules_p005_q.png`
- 核对：Proposition 1.3 证明续段、映射与商模生成元、Proposition 1.4、Corollary、Proposition 1.5(a) 条件及公式。
- 结果：FAIL。留存的 300dpi 源页裁片确认现有 Markdown 多处把印刷 `h` 误成 `b`：p.5 对应 MD 第 131、133、135 行（含 `h(b)`/`h(a)`、映射 `h(a)` 与生成元 `h(π)`、`h(πb)=πh(b)=π^n h(b)` 及其带横线记号）；第 133 行另将印刷 `α ↦ p/π` 写成 `a ↦ f/π`。Proposition 1.5(a) 印刷写 `n` 不是 `q` 的幂，MD 第 147 行误成 `g`。这些都待全篇审计后用 Edit 逐处修复和复核；本页签字时未改 Markdown。
- 另记：Markdown 未保留页眉题名及印刷页码 565。
