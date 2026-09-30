# AUDIT — De Philippis & Figalli《Partial regularity for optimal transport maps》（Ann. Inst. Fourier (Grenoble) 65 (2015)，DOI 10.1007/s10240-014-0064-7，2014-07-29 在线发表；arXiv:1209.5640 排版版）

## 审计依据

- PDF：`DePhilippis_Figalli_2015_partial_regularity_published.pdf`（32 页；Acrobat Distiller
  born-digital，文本层 62338 字节、0 U+FFFD——**文本层主对账通道 + PNG 抽验**）。
- mineru：`DePhilippis_Figalli_2015_partial_regularity_published_mineru/…md`（1482 行）。
- 模式：pdftotext 逐条仲裁全部疑点（方程编号、(C1)(C2) 映射变元、det(P)/det(M) 的 ≠、fn1/2/4/5
  原文、文献小型大写作者名等），300dpi 终裁 3 处（det(P),det(M)≠0 与 Taylor 式、fn5 全文恢复；
  `audit/300dpi/defi15_p07_detPM_neq_300.png`、`defi15_p27_fn5_300.png` 等），150dpi 全 32 页渲染
  （`audit/defi15_p001–032.png`），p.1 整页目检。
- 方程编号：修复后 \tag 清单 = {(2.1)–(2.10), (3.1)–(3.10), (4.1)–(4.44), (5.1)–(5.25)} 共
  **89 组，无重复无缺失**（修复前 5 组错位：(4.1) 裸行、(4.8)/(4.9)、(5.5)/(5.6)/(5.7)、
  (5.11)/(5.12)、(5.21)/(5.22)，均已按 print 归位）。

## 伪影族汇总

| 族 | 处数 | 说明 |
|---|---|---|
| 箭头丢失（→ 被 double-space 取代） | 13 | T:X Y、c:X×Y R、u:X R、u^c:Y R、ω:R⁺R⁺ 等 |
| 定理/引理头被吞入数学式 | 5 | Theorem 1.3/2.1/2.2、Proof of Theorem 1.3、Lemma 4.1（"$\_ L e t$" 等） |
| 足注碎裂/乱序 | 5 | fn1（μ,ν 定义被拆出）、fn2（display 落入正文）、fn4（c(x,y)=\|x−y\|^p 拆出）、fn5（三段乱序+HTML 碎片+⑩ 乱码，整体重建） |
| 方程编号错位 | 5 组 | 见上 |
| 内容级 OCR 错 | 8 | det(P),det(M) 丢 ≠、(C2) D_y→"D_v"、(C1) 变元 j、C₉→𝒞₂、Step 6→"Step δ"、X′ 丢撇、ȳ→𝒟、杂散"8"/"小"/"gives 5" |
| 记号乱码 | 12 | \bar C/\dot C、$\cdot_{c∈...}$、\tilde{\b{f}}、c_ρ^{ }、\bar{)}、\setminus\backslash、\tilde{⌈⌉}、\qend+33×\qquad 填充带 ×2、ε_{;}、Z⁺ 乱序、Monge-Ampère 式 B 范数 |
| 空格粘连（斜体边界丢空格） | ~45 | Letf×2、awayfrom×5、mapfrom×2、ofclass×5、ofmeasure、convexfunction×6、thefollowing×2、ofvariables×2、Afirst、Then,for、MTWcondition、Proofof、sendingf、ofthe×2 等 |
| 标点错位（.$ 双周期/.$逗号） | 26 | French 式 "$g .$." / "$X .$," 全部归位 |
| 灰边参考文献小型大写姓丢失 | 3 | [1] L. AMBROSIO, N. GIGLI and G. SAVARÉ、[12] L. C. EVANS and R. F. GARIEPY（姓整体丢失，按文本层恢复）；[14] SIAM J.、[21] Equ.、[26] Ampère、[29] J. Reine、[37] and New |
| 其它 | ~20 | proof.- → □（print 墓碑）×5、15juillet/29juillet 间距、$m_:$、(4.9) bold 引用、det(M) 花体化、(B√{8h₀}) 丢下标/丢括号、𝒬→Ω、Domc-exp ×4、u it is（print 原文保留） |

**合计约 160 处 / 75 规则**（脚本逐规则计数断言通过）。

## 逐页签（文本层全篇对账 + 关键页 PNG/300dpi 目检）

- **p.001（题录）**：标题/作者/摘要/Thm 1.1/1.2/DOI/CrossMark ✓。PASS±。
- **p.002–p.006**：§1 续（MTW 讨论、(C0)–(C3)、Thm 1.3/1.4 重构）、§2 (2.1)–(2.10)、§3 开头。
  PASS±（箭头/编号/头格式已修复）。
- **p.007–p.011**：Proof of Thm 1.3 全链（c-共轭、(3.1)–(3.10)、重标化、fn1 重建）。PASS±。
- **p.012–p.013**：Proof of Thm 1.4、§4 开头、Lemma 4.1（(4.1) 归位）+证明、Lemma 4.2（K′ 撇恢复）。PASS±。
- **p.014–p.018**：Theorem 4.3 陈述（(4.8)–(4.10) 归位）、Steps 1–3（(4.11)–(4.20)）、Lemma 4.2 应用。PASS±。
- **p.019–p.024**：Steps 4–6（(4.33)–(4.43)、(4.36) \qend 修复）、Remark 4.4、Cor 4.5/4.6。PASS±。
- **p.025–p.031**：§5、Lemma 5.1、Prop 5.2+证明（(5.1)–(5.10) 归位）、Theorem 5.3+证明
  （(5.11)–(5.25)、fn5 整体重建）。PASS±。
- **p.032**：Acknowledgements、REFERENCES [1]–[37] 逐条（姓氏恢复、MR/DOI/卷页全部保留）、
  双机构署名（G. P. / A. F. print 原样）、Manuscrit reçu/accepté/publié 行。PASS±。

## 总评

- **覆盖声明**：文本层全篇逐式对账；300dpi 终裁 3 处入库；150dpi 32 页渲染入库；p.1 整页
  目检；文献 37 条逐条核对；足注 5 条全部重建核对；\tag 89 组与 print 逐一对应。
- **修复统计**：约 160 处 / 75 规则。
- **无 FAIL**：内容级错误（det(P),det(M) 丢 ≠、(C2) D_y 误 D_v、C₉、Step δ、fn5 碎裂）全部修复；
  参考文献作者姓整体丢失（[1][12]）按 print 文本层恢复。

### 源级 quirk 清单（print 原貌，md 忠实保留）

1. **"at every point x where u it is twice differentiable"**（§2，(2.10) 后）——print 原文多 "u"。
2. **"depending only K"**（Lemma 4.1，缺 on）——print 原文。
3. **"to show regularity optimal transport maps for the cost |x−y|^p"**（§4 开头，缺 of）——print 原文。
4. **(4.4) 中 Σ_{j=1}^k J_k^{(m)}(F₁)**——j/m 指标错配；print 原文（文本层证实）。
5. **"In addition, thanks (5.7) and (5.2)"**（缺 to）——print 原文（文本层证实）。
6. **"interior estimates for solution of the Monge-Ampère equation"**（solution 单数）——print 原文。
7. **"consider his c-subdifferential"**（fn3，his）——print 原文。
8. **[7] "M. M. GONZALES"**（通常拼 González）与 **[19]/[20] "R.J. MCCANN"/"R. J. MCCANN" 不统一**、
   **[20] "J. Eur. Math. Soc. (JEMS), 5 (2013)"**（该文实际卷号非 5）——print 原文。
9. **[26] "Progress in … Applications, vol. 440"**（Gutiérrez 书实为 vol. 44）——print 原文（文本层证实）。
10. **[28] "Art. ID rnn120"** 与 **[15] "Exposés 997–1011. Astérisque No. 332 (2010), Exp. No. 1009,
    ix, 341–368."** 的卷期排印均为 print 原样。
11. **μ := f(x)dx / ν := g(y)dy（fn1，无积分号）**——print 原文简写（300dpi 证实）。

- **可用性结论**：修复后 md 与 print 逐式对齐（\tag 89 组），可作可靠对读本；足注 5 条完整重建；
  文献 37 条含 MR/Zbl/DOI 全信息。

## 修复登记

（fix(md) commit 后追加）
