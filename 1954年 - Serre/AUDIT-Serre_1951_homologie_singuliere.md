# AUDIT — Serre_1951_homologie_singuliere

> 逐页视觉审计说明，格式依 `AUDIT-SOP.md`「审计说明格式」。
> 印刷页码换算：印刷页 = PDF 页 + 423（PDF p.1 为 JSTOR 封面，PDF p.2 = 印刷 p.425）。

- actor=Wf-P45
- host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF SHA256=1420abbef07ec179ce1cbad72dec745b05a9f386fe1dbbeeaf98817835f9f69f
- MD 基线 SHA256=cb13117e5f47226c41b61d39cff1b1760463ea47ea772c1b8ee6a2c6f571b6aa（mineru 原始导出 `Serre_1951_homologie_singuliere_mineru/Serre_1951_homologie_singuliere__Serre_1951_homologie_singuliere.md`）
- 审计开始：2026-10-02 13:47
- 审计范围：本文件当前分块审计 p.1–p.9（后续分块由后续 ask 延续）。分块 1（p.001–p.009）已完成：PASS×5、PASS±×3、FAIL×1（p.005，已当场修复）；修复 1 处，见 p.005 条目。分块 2（p.010–p.018）进行中。
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

## p.006（PDF p.6 / 印刷 p.429）
- PNG：audit/p006.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p006_dCr_600.png、p006_Cinf_600.png、p006_Er_def_600.png、p006_kernel_600.png、p006_display_600.png、p006_display2_600.png（600dpi）
- 核对：C_∞^p/B_∞^p 定义行；包含链 B_0 ⊂ B_1 ⊂ ⋯ ⊂ B_∞ ⊂ C_∞ ⊂ ⋯ ⊂ C_r ⊂ C_{r−1} ⊂ ⋯ ⊂ C_0 = A^p；d(C_r^{p+r}) = B_r^p；DÉFINITION DES E_r^p；E_r^p = C_r^p/(C_{r−1}^{p−1} + B_{r−1}^p)；d 诱导 d_r^p: E_r^p → E_r^{p−r}；noyau (C_{r+1}^p + C_{r−1}^{p−1})/(C_{r−1}^{p−1} + B_{r−1}^p)；image (C_{r−1}^{p−1} + B_r^p)/(C_{r−1}^{p−1} + B_{r−1}^p)；d_r^p∘d_r^{p+r} = 0 与商 = E_{r+1}^p 展示式（两行）；Interprétation 段（E_r = ∑_p E_r^p、degré −r）；H(E_r) = E_{r+1} 链；Le terme E_0 段（E_0^p = A^p/A^{p−1}、d_0 段）
- 结果：PASS
- 仲裁记录：初读 150dpi 曾疑 MD 的 C_{r−1}^{p−1}（上标 p−1）为印刷 C_{r−1}^p 之误读；600dpi 三处裁剪（p006_Er_def_600.png、p006_kernel_600.png、p006_display2_600.png）确认印刷确为 **p−1**（E_r^p = C_r^p/(C_{r−1}^{p−1} + B_{r−1}^p)，展示式尾项 C_r^{p−1} + B_r^p），MD 与印刷逐字一致，无需修改。按数学直觉"改正"该上标反而是错的——print quirk 纪律的正面案例。
- 差异：无。
- 备注：本页公式密度最高，全部逐一核过；"Le terme E_1"起属印刷 p.430。

## p.007（PDF p.7 / 印刷 p.430）
- PNG：audit/p007.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p007_phi_600.png（A^{p,q} 定义行）、p007_phi2_600.png（Eilenberg 引用行）
- 核对：Le terme E_1（E_1^p = H(A^p/A^{p−1})、∂: H(A^p/A^{p−1}) → H(A^{p−1}/A^{p−2})、"triple" (A^p, A^{p−1}, A^{p−2})）；Le terme E_∞（E_∞^p = C_∞^p/(C_∞^{p−1} + B_∞^p)）；D^p = C_∞^p/B_∞^p；D^p/D^{p−1} = E_∞^p；∩_p A^p = 0 与 ∩_p D^p remark；Note（J. Leray [23]、J-L. Koszul [20]、remplacer p par −p）；Eilenberg ([6], Exp. VIII)；§2 Cas d'un groupe gradué（ⁿA、d(ⁿA) ⊂ ⁿ⁻¹A、A^{p,q} = ⁽ᵖ⁺ᑫ⁾A ∩ A^p、H_n(A)）；Graduation des termes…开头（Nous noterons C_r^{p,q}, B_r^{p,q}, C_∞^{p,q}, B_∞^{p,q},）
- 结果：PASS
- 仲裁记录：①150dpi 初读 Eilenberg 引用疑为 [16]，600dpi（p007_phi2_600.png）+JSTOR 文本层双证为 **([6], Exp. VIII)**，MD 正确；②600dpi 确认印刷 "Nous poserons A^{p,q} = ⁽ᵖ⁺ᑫ⁾A ∩ A^p" 与 MD 逐字一致；③印刷本页作 "vis a vis"（a 无重音），MD 行 277 同样保留 "vis a vis"，忠实。
- 差异：md "J.-L. Koszul" 对印刷 "J-L. Koszul"——标点规范化（排版级），不误导，不修。
- 备注：md 中 D^{p,q} 定义句、E_r^{p,q} 商式、d_r 次数性质、(Φ) 假设、"Conséquences de l'hypothèse (Φ)" 均属印刷 p.431，留待 p.008 核对。

## p.008（PDF p.8 / 印刷 p.431）
- PNG：audit/p008.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p008_E0_600.png、p008_Eps_600.png（600dpi）
- 核对：D^{p,q} 求和直解句；On pose de même: E_r^{p,q} = C_r^{p,q}/(C_{r−1}^{p−1,q+1} + B_{r−1}^{p,q}) (0 ≦ r ≦ +∞)；bigraduation 段（degré filtrant/complémentaire/total）；d_r 三条次数性质；Une hypothèse supplémentaire；(Φ) 假设（0 ≦ w(x) ≦ deg. x；A^{n,0} = ⁿA；A^{p,q} = 0 si p < 0）；Conséquences de l'hypothèse (Φ)；E_∞^{p,q} = D^{p,q}/D^{p−1,q+1}；suite de composition 0 = D^{−1,n+1} ⊂ ⋯ ⊂ D^{n,0} = H_n(A)；∩_p D^p = 0；PROPOSITION 1（E_r^{p,q} = ⋯ = E_∞^{p,q} pour r > Sup(p, q+1)）；证明段；C_r^{p,q} = C_∞^{p,q}; B_r^{p,q} = B_∞^{p,q}；limite 段；Le groupe différentiel R 开头（R = A^0、R_q = A^{0,q}、E_1^{0,q} = H_q(R)）
- 结果：PASS
- 仲裁记录：①150dpi 初读疑首句为 E_r^{p,q}（MD 作 E_0^{p,q}），600dpi（p008_E0_600.png）确认印刷为 **E_0^{p,q}**（下标 0 清晰、与同行 E_r 的 r 对比明确），MD 正确；②150dpi 初读疑 "E_r^{p,s} = 0"，600dpi（p008_Eps_600.png）确认印刷为 **E_r^{s,t} = 0 pour s < 0**，与 MD 一致。
- PASS± 项（不修）：md 将斜体小节引导句 "Conséquences de l'hypothèse (Φ)." 与前段合并在同一行（印刷中为独立一行），mineru 分段伪影，内容无缺损。
- 备注：本页证明段、Prop. 1 陈述逐项吻合；"(r ≧ 1)" 处 md 作 "(r \geq 1)"，符号等价。

## p.009（PDF p.9 / 印刷 p.432）
- PNG：audit/p009.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p009_E3_600.png、p009_E1_600.png（600dpi）
- 核对：R 组续（"cycles pour d_r…degré filtrant minimum"段、H_q(R) = E_1^{0,q} → E_2^{0,q} → ⋯、isomorphismes sur dès que r > q+1、E_∞^{0,q} = E_{q+2}^{0,q}、H_q(R) → E_∞^{0,q} → H_q(A)、injection R → A）；Le groupe différentiel S（E_1^{p,0} = S_p、S = ∑_p S_p、H_p(S) = E_2^{p,0}、d_r (r ≧ 2) 无 bord、⋯ → E_3^{p,0} → E_2^{p,0} = H_p(S)、E_{p+1}^{p,0} = E_∞^{p,0}、E_∞^{p,0} = D^{p,0}/D^{p−1,1} = H_p(A)/D^{p−1,1}、H_p(A) → E_∞^{p,0} → H_p(S)、E_1^{p,0} = C_1^{p,0}/(C_0^{p−1,1} + B_0^{p,0})、C_1^{p,0} = ᵖA、π: A → S、π_* image = E_∞^{p,0} noyau = D^{p−1,1}）；Note（groupes d'opérateurs、extensions de groupes discrets、Morse）
- 结果：PASS
- 仲裁记录：①150dpi 初读展示式为 "⋯ → E_r^{p,0} → E_2^{p,0}"，600dpi（p009_E3_600.png）确认印刷为 **E_3^{p,0}**，MD 正确；②150dpi 初读 "rappelons" 句为 "E_2^{p,0} = C_2^p/(C_1^{p−1,1} + B_2^{p,0})"，600dpi（p009_E1_600.png）确认印刷为 **E_1^{p,0} = C_1^{p,0}/(C_0^{p−1,1} + B_0^{p,0})**，与 MD 逐字一致。
- 差异：无。
- 备注：md 行 371 起 "Dans le cas d'un espace fibré…" 属印刷 p.433，留待下一分块。

## p.010（PDF p.10 / 印刷 p.433）
- PNG：audit/p010.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p010_HpAR_600.png、p010_imDis_600.png、p010_diag1_600.png、p010_lamMu_600.png、p010_lamMu2_600.png（600dpi）
- 核对：espace fibré E/F/B 段（R→A→S 与 F→E→B）；§3 标题 "La transgression et la suspension"；Le groupe A/R（π、π′: A^{p,0}/A^{0,p} → S_p、π_*′: H_p(A/R) → H_p(S)）；H_p(A/R) = C_p^{p,0}/(C_0^{0,p} + B_1^{p,0}) 与 H_p(B) = C_2^{p,0}/(C_1^{p−1,1} + B_1^{p,0})；π_*′ 的核（C_{p−1}^{p−1,1} → H_p(A/R) 的像）与像（C_p^{p,0}/[C_1^{p,0} ∩ (C_1^{p−1,1} + B_1^{p,0})] = C_p^{p,0}/(C_{p−1}^{p−1,1} + B_1^{p,0}) = E_p^{p,0}）；正合列 C_{p−1}^{p−1,1} → H_p(A/R) → E_p^{p,0} → 0；composé 段；Un diagramme + 图 (I)（三行三列/五行结构、(p ≥ 2)、suites exactes/commutatif/λ μ biunivoques 段）；La transgression 开头
- 结果：FAIL（已当场修复 1 处）
- 仲裁记录：①初读疑 H_p(A/R) 公式为 C_1^{p,0}/(C_0^{p,0}+…)（MD 作 C_p^{p,0}/(C_0^{0,p}+B_1^{p,0})），600dpi（p010_HpAR_600.png）确认印刷为 **C_p^{p,0}/(C_0^{0,p} + B_1^{p,0})**，MD 正确；②初读疑 π_*′ 像展示式首项为 C_1^{p,0}，600dpi（p010_imDis_600.png）确认印刷为 **C_p^{p,0}**，MD 正确；③图 (I) 第一行 600dpi（p010_diag1_600.png）确证 C_∞^{p−1,1} → C_{p−1}^{p−1,1} —d→ B_{p−1}^{0,p−1}，MD 一致。
- 差异与修复：
  - **[已修复]** md 行 410 图 (I) 的线性化 array 把 λ 画在第一列竖箭头上（"\\Bigg \\downarrow \\lambda"），使 λ 的目标呈现为底行的 0；印刷（p010_lamMu_600.png、p010_lamMu2_600.png）中第一列竖箭头无标签（E_∞^{p,0} ↓ 0），λ 是从 E_∞^{p,0} 指向 H_p(S) 的右下斜箭头（箭头头部在 H_p(S) 端），μ 是从 E_p^{p,0} 指向 H_p(S) 的左下斜箭头。MD 原状与同页 "les homomorphismes λ et μ … sont biunivoques" 相矛盾。Edit 修复为 "\\Bigg \\downarrow & \\searrow \\lambda \\quad \\swarrow \\mu & …"（两斜箭头汇入 H_p(S)，竖箭头去 λ 标签），本页 commit 内 diff 可溯。
- PASS± 项（不修）：mineru 将二维交换图线性化为 array，列间部分竖箭头（如 B_{p−1}^{0,p−1} ↓ H_{p−1}(R) 列的排布）与原图几何有出入，属图线性化固有近似，其余节点/标签逐项吻合。
- 备注：md 行 413 起 "La transgression." 段的正文部分属印刷 p.434。
