# AUDIT — Andrei Okounkov, "Rhymes in primes"（ICM 2022 popular exposition，DOI 10.4171/ICM2022/206 卷内；born-digital，pdfTeX + hyperref）

> mineru: standard 档导出 `ICM2022_popular_exposition_Maynard_mineru/`；**born-digital 文本层主对账通道**
> （pdftotext 68.5KB/0 FFFD 逐点仲裁）+ PNG 抽验（题录页整页目检；150dpi 全 31 页入库）。

## 逐页签（31/31；文本层全对账）

- **p.1**：标题 "Rhymes in primes"/作者 Andrei Okounkov/Abstract/MSC/Keywords/ICM ©+DOI ✓
  （© 块按惯例未收）— PASS±
- **p.2-4**（§1 古筛法 + §2 末位数）：乘法表 (1)、Eratosthenes、(3) 素数表、twin primes、
  **足注 1 重构**（print "Can you prove that **p + 2 and p − 2** cannot both be prime, except for
  **p = 5**?"——碎片 "p = 5"/"lik" 归位）、足注 2（n!+1）✓ — PASS（修复后）
- **p.5-7**（§2 余数 + §3 CRT）：mod 记号、(4) 二进制、(5) 211i+j、CRT (6)-(9)、
  **足注 3 重构**（print 原文 "It is **fact of life** that **it** takes a while…like **q = 211**…
  for either some fixed **q** and **a** or averaged over **a**."——碎片 q=211/andq 归位；
  "fact of life" 缺冠词系 print 原文）✓ — PASS（修复后）
- **p.8-10**（§4 极限与级数）：(10)-(15)、**足注 4 重构**（print "namely (e^x)′ = e^x and
  (ln y)′ = 1/y … the rule (x^n)′ = nx^{n−1}"——碎片 "(ln y)′=1/y"/"ex"/幂法则归位）✓ — PASS（修复后）
- **p.11-13**（§5 密度 + (16)-(26)）：Euler 常数 (14)、ζ(2)=π²/6、**"whethe"→whether** ✓ — PASS（修复后）
- **p.14-16**（§6 PNT + 表 (29)）：(27)(28)、**表 (29) 按 print 补全至 22 行**（md 原截断于 10^14
  且末行 mineru 乱串 "\text{.}."×29；print 第三列 22 值逐行转录：.98e-7/.35e-7/.12e-7/.30e-8/.89e-8/
  .43e-8/.10e-8/.28e-9/.96e-9）✓ — **PASS（表格补全，内容级修复）**
- **p.17-19**（§7 容斥 + (30)-(43)）：**(30) 双 tag 清理（mineru 残留 "\tag{2}\tag{30}"→(30)）**、
  μ_P(d)、(37)-(43) ✓ — PASS（修复后）
- **p.20-22**（§7 续 + §8 sieve 首难 + §9 patterns 开头）：Dirichlet L-function (44)-(47)、
  (48)-(52)（C₂=1.32…）、**"f₁/f₂  1" 丢箭头→→1** ✓ — PASS（修复后）
- **p.23-25**（§9 续 + (53)-(59) + C_{2m}/C₂ + 图 55/56）：**足注 6 包 span**、
  "aprime"/"occurfor"/"ifone"/"woud" 等 ✓ — PASS（修复后）
- **p.26-28**（§10 Closing the gap + (60)-(64)）：GPY、Zhang、Maynard-Tao、246/35410/433992、
  **足注 7/8**（fn8 print 原文 "check **than** any **k**-tuples of primes larger than **k** are
  admissible"——than/are 系 print 原文，k 字形恢复）✓ — PASS（修复后）
- **p.29-31**（§12 证明一瞥 + (65)-(81) + 附录 A/B + (82)-(93) + References [1]-[31] + 作者块）：
  **"limi"→limit、"argumen"→argument 截断修**、**"real par 𝔅s=1/2"→real part**、
  Mellin transform (83)-(93)、胶水 ×14（Boundedintervals/manyprimes/ofprime/ofbounded/ProofSettles/
  Publi cations/Internationa/Inter national/Collo quium/Ency 类/concentration ofmeasure/ofGoldston/
  andprimes/Digits ofprimes）、[29] Dirichet **L**-series（� 恢复）✓ — PASS（修复后）

## 总评

- **覆盖声明**：31/31 页文本层全对账 + PNG 抽验（p.001 整页）+ 150dpi 全 31 页入库；born-digital 通道。
- **系统性修复**：丢字形 � ×31（n/m/p/b/a/N/x/J/k/F/E/W/s/y/γ/μ/L/ζ 按上下文）；足注碎片重构 5 组
  （fn1/fn3/fn4/fn5 公式与人名碎片归位；**fn6 补 span**）——足注 1-8 共 8 个全真；**表 (29) 按 print
  补全 9 行（10^14-10^22，第三列 9 值）并清除 29 个 \text{.} 乱串**；(30) 双 tag 清理；丢箭头 ×2；
  smart-quote 无；ff ×12；胶水断词 ×20；mash ×8；HTML sub ×2。**共约 200 处/90 规则**。
- **源级 quirk 清单（忠实不改）**："Let **is** call a pattern J"；"**if has** a nonzero chance"；
  "**one expect** that"（未复数）；"It is **fact of life**"（缺冠词）；"All newcomers we wish some
  patience"；"Such **considerations of** are both very basic"（语法悬空）；"there is **lot** of
  questions"；"for arguments in **(0, 2)**"；"this project **have lead** to"式 "have lead"；
  "**the the** following description"；"check **than** any k-tuples … **are** admissible"；
  "punch trough"（print 原文 trough）；作者 email okounkov@math.columbia.edu（伯克利地址配哥大邮箱，
  print 原文）；©/DOI 块未收（惯例）。
- **可用性结论**：修复后 md 可作该文忠实底本；(1)-(93) 编号齐全，11 节 + 附录 A/B、8 足注、
  31 条 References（含 Quanta 链接与 ↑ 页码回标）、作者块完整。与 Maynard arXiv/published/ICM/
  laudatio（均已审 ✅）构成 Maynard 目录闭环（尚余 ICM proceedings 主文等已审）。

### 修复登记（2026-09-30）

- pass-1 约 88 规则 applied（脚本结构错 4 处按铁律 3 整文件重写纠正，md 未被半成品污染）+
  pass-2 28 规则 + 表格切片法补全 1 + 内联终清 8。
- fix(md) commit 父提交 = 修复前 md 原貌；脚本 /tmp/maynard_pop_fix/fix_md.py + 内联 pass。
- 本篇 31/31 页完成，无未决项。
