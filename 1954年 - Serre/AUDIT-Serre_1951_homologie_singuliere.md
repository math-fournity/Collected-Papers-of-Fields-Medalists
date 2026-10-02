# AUDIT — Serre_1951_homologie_singuliere

> 逐页视觉审计说明，格式依 `AUDIT-SOP.md`「审计说明格式」。
> 印刷页码换算：印刷页 = PDF 页 + 423（PDF p.1 为 JSTOR 封面，PDF p.2 = 印刷 p.425）。

- actor=Wf-P45
- host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF SHA256=1420abbef07ec179ce1cbad72dec745b05a9f386fe1dbbeeaf98817835f9f69f
- MD 基线 SHA256=cb13117e5f47226c41b61d39cff1b1760463ea47ea772c1b8ee6a2c6f571b6aa（mineru 原始导出 `Serre_1951_homologie_singuliere_mineru/Serre_1951_homologie_singuliere__Serre_1951_homologie_singuliere.md`）
- 审计开始：2026-10-02 13:47
- 审计范围：本文件当前分块审计 p.1–p.9（后续分块由后续 ask 延续）
- 文本层判定：**可用**（JSTOR OCR 文本层；首页 `pdftotext -f 1 -l 1` 成功输出封面文字，p.2–p.3 数学正文页亦能输出全部段落文本）。但 OCR 噪声明显（例：`L'int6retde`、`getodesiques`、`memoireest` 等粘连/错字），故全程采用「**文本层主对账 + PNG 视觉核验**」双通道：文本层用于定位与文字对账，凡字形、上下标、公式、记号一律以 150dpi PNG（pngmono）视觉核验为最终裁决。
- mineru doc_id：UNKNOWN（导出目录未含 doc_id 元数据，仅 `full.md` 等产物；如需可在 `structured_content.json` 侧另行核查）

---

## p.001（PDF p.1 / JSTOR 封面页）
- PNG：audit/p001.png（pngmono 150dpi）
- 核对：题录页（JSTOR cover）——刊名、标题 "Homologie Singuliere Des Espaces Fibres"、Author(s): Jean-Pierre Serre、Source: The Annals of Mathematics, Second Series, Vol. 54, No. 3 (Nov., 1951), pp. 425-505、Published by、Stable URL、Accessed: 18/05/2012 10:32、两段 JSTOR 条款文字
- 结果：PASS±
- 差异：①md（第 14–15 行后）缺印刷页末句 "Annals of Mathematics is collaborating with JSTOR to digitize, preserve and extend access to The Annals of Mathematics." 及页脚 "http://www.jstor.org"——JSTOR 封面样板，非论文内容，不误导，不修；②印刷页 "available at" 与 URL 分两行，md 合并为一行——排版级，不修。其余题录字段逐项吻合。
- 备注：本页为 JSTOR 自动生成封面；该缺失句建议阅读时忽略。

## p.002（PDF p.2 / 印刷 p.425）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：题录（标题 HOMOLOGIE SINGULIÈRE DES ESPACES FIBRÉS / Applications / PAR JEAN-PIERRE SERRE / Received May 4, 1951）；INTRODUCTION 前三段；章节预告 Ch.I（suite spectrale ([22], [19])、K(π; q)、Cartan-Leray）与 Ch.II 开头（跨页断句 "…consiste à prouver que le"）；脚注 1（Les crochets renvoient à la Bibliographie…）
- 结果：PASS±
- 差异：md 缺印刷页眉块 "ANNALS OF MATHEMATICS / Vol. 54, No. 3, November, 1951 / Printed in U.S.A."（grep "Printed in U.S.A|November" 全文 0 命中，系 mineru 系统性略去运行页眉；卷期信息已见于 p.1 封面行，不误导，不修）。正文文字、脚注标记 $^{1}$ 位置（Marston Morse 之后）、关系式 $\pi_i(\Omega) = \pi_{i+1}(X)$、引用编号 [25]/[18]/[22]/[19]/[24] 顺序均与原图逐项吻合。
- 备注：mineru 已知瑕疵类型"运行页眉略去"在本篇为系统性表现，后续页不再重复登记，除非页眉含正文性信息。

## p.003（PDF p.3 / 印刷 p.426）
- PNG：audit/p003.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p003_pi_formula.png、p003_distinct.png、p003_distinct_word.png、p003_donne_zoom.png（300dpi，sips 裁剪/放大）
- 核对：Ch.II 续段（terme E₁ de la suite spectrale…définition des espaces fibrés）；Ch.III（Prop. 5、Prop. 3、Leray [24]、Čech）；Ch.IV（th. de Hopf、n°7/n°8、Riemann compact connexe、infinité de géodésiques）；Ch.V（π_i(S_n) finis sauf π_n(S_n) et π_{4n−1}(S_{2n})；caractéristique p：π_{n+2p−3}(S_n)，n impair）；Ch.VI（Eilenberg-MacLane）；Comptes-Rendus [28]；致谢 H. Cartan / J-L Koszul 段
- 结果：PASS±
- 仲裁记录：①初读 150dpi 疑 MD 行 45 "π_{n+2p−3}" 与印刷 "π_{n+2p−2}" 不符 → 300dpi 裁剪（p003_pi_formula.png）确认印刷确为 **n+2p−3**，MD 正确，我方初读有误；②印刷原句为 "deux points **distinct** donnés"（p003_distinct_word.png/p003_donne_zoom.png：distinct 无尾 s；donnés 拼写确认）——印刷语法 quirk（应为 distincts），**md 忠实保留 "distinct"，不改**。
- 差异：md "dont on connaît les groupes" 对印刷 "dont on connait les groupes"——重音符号现代化（排版级），不误导，不修。
- 备注：本页无内容错误需修复；引用 [22][19][24][25][28] 与数学式全部逐项吻合。

## p.004（PDF p.4 / 印刷 p.427）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：致谢结尾段（Borel/Bourbaki/Eilenberg/Leray/Denjoy）；TABLE DES MATIÈRES：CHAPITRE I（n°1–6）、CHAPITRE II（n°1–13，含 n°4 "Filtration du complexe singulier de E"、n°5/n°6 "Calcul du terme E₁/E₂"、Lemmes 4/5/3 顺序）、CHAPITRE III（n°1–7，Gysin/Wang/Leray-Hirsch）、CHAPITRE IV（n°1–4）
- 结果：PASS
- 差异：无。目录各条目文字、编号、顺序、标点（Ch.II 标题无句点、其余章标题有句点；n°5 "suite spectrale—Cas" em-dash；斜体 E₁/E₂ → $E_{1}$/$E_{2}$）逐项吻合。
- 备注：md 行 112 起的 Ch.IV n°5 条目属印刷 p.428 内容，跨页顺序正常。

## p.005（PDF p.5 / 印刷 p.428）
- PNG：audit/p005.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p005_Cr.png、p005_Cr_left.png、p005_Cr_600.png（本页记号行）、p006_dCr_600.png（p.6 同记号对照）
- 核对：目录续（Ch.IV n°5–9、Ch.V n°1–6、Ch.VI n°1–3、APPENDICE、BIBLIOGRAPHIE）；正文开头（CHAPITRE I 标题、§1 标题、DÉFINITION 段、 filtration 三条件 ∪_p A^p = A; A^p ⊂ A^{p+1}; d(A^p) ⊂ A^p、A^{−∞}=0/A^{+∞}=A、w(x) 定义、w(a−b) ≦ Sup(w(a), w(b)); w(da) ≦ w(a)、Réciproquement 段、Notations C/B 定义）
- 结果：FAIL（已当场修复 1 处）
- 差异与修复：
  - **[已修复]** md 行 181 记号定义 "$C_{-}^{p}$ : ensemble des éléments de A^p dont le bord est dans A^{p−r}" 的下标误为减号。证据链：本行印刷自证 "dans A^{p−r}" 用斜体 r（p005_Cr.png）；p.5 该 C 下标字形退化呈短横（p005_Cr_left.png、p005_Cr_600.png），与同行 B_r 的清晰 r 不同；p.6 同一记号印刷清晰为 C_r^{p+r} = B_r^p 及包含链 C_∞ ⊃ C_r（p006_dCr_600.png、audit/p006.png）。据此判定 p.5 印刷字形为退化 r、mineru 误读为 "-"，Edit 修复为 "$C_{r}^{p}$"（本页 commit 内，diff 可溯）。
- PASS± 项（不修）：目录 CHAPITRE V、CHAPITRE VI 两行缺 `##` 标题前缀（md 行 129/139；Ch.I–IV 均有），mineru 结构伪影，内容忠实，仅影响标题导航。
- 备注：目录与正文其余文字、公式逐项吻合。
