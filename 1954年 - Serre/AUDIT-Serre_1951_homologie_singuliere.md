# AUDIT — Serre_1951_homologie_singuliere

> 逐页视觉审计说明，格式依 `AUDIT-SOP.md`「审计说明格式」。
> 印刷页码换算：印刷页 = PDF 页 + 423（PDF p.1 为 JSTOR 封面，PDF p.2 = 印刷 p.425）。

- actor=Wf-P45
- host/model/effort=zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）
- PDF SHA256=1420abbef07ec179ce1cbad72dec745b05a9f386fe1dbbeeaf98817835f9f69f
- MD 基线 SHA256=cb13117e5f47226c41b61d39cff1b1760463ea47ea772c1b8ee6a2c6f571b6aa（mineru 原始导出 `Serre_1951_homologie_singuliere_mineru/Serre_1951_homologie_singuliere__Serre_1951_homologie_singuliere.md`）
- 审计开始：2026-10-02 13:47
- 审计范围：本文件当前分块审计 p.1–p.9（后续分块由后续 ask 延续）。分块 1（p.001–p.009）已完成：PASS×5、PASS±×3、FAIL×1（p.005，已当场修复）；修复 1 处，见 p.005 条目。分块 2（p.010–p.018）已完成：PASS×2（p.012/016）、PASS±×1（p.014）、FAIL×6（p.010/011/013/015/017/018，均已当场修复）；修复 8 处（图 I λ 箭头、图 II 多余箭头、A\*n→A\*p、II→Π×2、λ^e→λ^ε×2、λ_κ→λ_K），见各页条目。
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

## p.011（PDF p.11 / 印刷 p.434）
- PNG：audit/p011.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p011_pistarmod_600.png、p011_diag2_600.png、p011_diag2top_600.png、p011_diag2end_600.png（600dpi）
- 核对：图 (I) 说明段（suites exactes、commutatif、λ μ biunivoques）；La transgression（H_{p−1}(R) ←∂— H_p(A/R) —π*′→ H_p(S) (p ≧ 2)、L/M/L′/M′ 定义、T: M′ → H_{p−1}(R)/∂(M)、éléments/cycle transgressif、da ∈ R_{p−1} 判据、PROPOSITION 2 全文）；La suspension（Σ 定义、élève les degrés d'une unité、H_p(A) = H_{p−1}(A) = 0 情形、π_*′∘∂^{−1}）；图 (II)；"Dans ce diagramme, d_p est un isomorphisme sur, E_p^{p,0} → H_p(S) est biunivoque…même noyau que Σ" 末行
- 结果：FAIL（已当场修复 1 处）
- 仲裁记录：①初读疑印刷 "égal à π*∘∂^{−1}" 无 prime，600dpi（p011_pistarmod_600.png）确认 π 右上有 prime（π*′∘∂^{−1}），MD \pi_*' 正确；②初读疑末行为 E_∞^{p,0} → H_p(S)，600dpi（p011_diag2_600.png 下部）确认印刷为 **E_p^{p,0}**（下标 p 清晰），MD 正确；③图 (II) 中间斜线：600dpi（p011_diag2top_600.png、p011_diag2end_600.png）确认印刷为**单头 ↖ 斜箭头**（箭头头部仅在上左端，右下端为裸线端、无头部）。
- 差异与修复：
  - **[已修复]** md 行 449 图 (II) 中间斜箭头写作 "\\nwarrow \\searrow"（双头），印刷仅单头 ↖。Edit 修复为 "\\nwarrow"（本页 commit 内 diff 可溯）。
- PASS± 项（不修）：transgression 定义前展示式中 md 作 "\\xrightarrow{\\pi^{\\prime} *}"（π′∗），印刷为 π*′（星号右下标、prime 右上标）且 md 其余处均作 \\pi_{*}^{\\prime}——同一态射的装饰次序排版差异，无数学歧义，不修。
- 备注：md 行 452 起 Note（Chern-Hirsch-Koszul、Eilenberg-MacLane、Koszul [20] deux dernières lignes）与 "## 4. Une suite exacte / Hypothèses." 属印刷 p.435。

## p.012（PDF p.12 / 印刷 p.435）
- PNG：audit/p012.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p012_notE_600.png、p012_ds1_600.png、p012_ds2_600.png、p012_Es1_600.png、p012_Es4_600.png、p012_Es5_600.png（600dpi）
- 核对：Note（proposition 2 due à Koszul [20]）；§4 Une suite exacte；Hypothèses（i < j、ⁿE_s′/ⁿE_s″ 记号约定、a_n < c_n）；两条假设（E_r^{p,q} = 0: p+q = n−1, p ≦ a_n − r；p+q = n+1, p ≧ c_n + r）；PROPOSITION 3 长正合列（ʲE_r′ → H_j(A) → ʲE_r″ → ʲ⁻¹E_r′ → ⋯ → ⁱE_r′ → H_i(A) → ⁱE_r″）；DÉMONSTRATION（D^{p,q}/D^{p−1,q+1} = E_∞^{p,q}、0 → ⁿE_∞′ → H_n(A) → ⁿE_∞″ → 0、d_s nulle sur ⁿE_s′ (s ≧ r)、cible E_s^{a_n−s, b_n+s−1}、ⁿE_∞′ quotient de ⁿE_r′、ⁿE_∞″ sous-groupe de ⁿE_r″、ⁿE_r′ → H_n(A) → ⁿE_r″）；末段（noyau = bords pour d_s (s ≧ r)、deux termes de E_s: ⁿ⁺¹E_s′/ⁿ⁺¹E_s″、d_s-cycles、页尾断句 "…non nulle, celle"）
- 结果：PASS
- 仲裁记录：150dpi 多处疑印刷为 E_r（记号定义句 ⁿE_?′/E_?^{p,q}、d_s 两句、ⁿ⁺¹E_?′/ⁿ⁺¹E_?″、"deux termes de E_?"），600dpi 逐处（p012_notE_600.png、p012_ds1_600.png、p012_ds2_600.png、p012_Es1_600.png、p012_Es5_600.png）确认印刷在这些位置**均为下标 s**，仅 "Ainsi E_r…"、quotient de ⁿE_r′ 等处为 r——印刷本身混用 E_s/E_r，MD 逐处与印刷一致，无需修改。本页我方 150dpi 误读累计八处，全部被仲裁推翻。
- 差异：无。
- 备注：md 行 503 起 "qui applique ⁿ⁺¹E_s″ dans ⁿE_s′…s = c_{n+1} − a_n" 与 ⁿ⁺¹E_r″ → ⁿE_r′ → H_n(A) 展示式属印刷 p.436。

## p.013（PDF p.13 / 印刷 p.436）
- PNG：audit/p013.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p013_wx_600.png、p013_wx2_600.png、p013_Cr_600.png（600dpi）
- 核对：s = c_{n+1} − a_n 段与 ⁿ⁺¹E_r″ → ⁿE_r′ → H_n(A) (i ≦ n ≦ j−1)；H_n(A) → ⁿE_r″ → ⁿ⁻¹E_r′ (i+1 ≦ n ≦ j)；COROLLAIRE（E_r^{p,q} = 0 si p+q = n, p ≠ a_n；a_n < a_{n−1} + r；H_n(A) = E_r^{a_n,b_n}）；c_n = a_n + 1, d_n = b_n − 1, i = 0, j = +∞；Note（Chapitre III）；§5 La suite spectrale—Cas de la cohomologie（[20]/[23]；filtration décroissante (1)(2)(3)；w(x) borne supérieure；A*⁰ = A；E_r^{*p,q} = C_r^{*p,q}/(C_{r−1}^{*p+1,q−1} + B_{r−1}^{*p,q}) (r = 0,1,⋯,∞)；E_∞^{*p,q} = D^{*p,q}/D^{*p+1,q−1}；D^{*} 链 0 = D^{*n+1,−1} ⊂ ⋯ ⊂ D^{*0,n} = H^n(A*)；d_r: E_r^{*p,q} → E_r^{*p+r,q−r+1}；H(E_r^*) = E_{r+1}^*）
- 结果：FAIL（已当场修复 1 处）
- 仲裁记录：①md 行 535 "(On a noté w(x)…tels que x ∈ A^{*n})" 的上标 n，600dpi（p013_wx2_600.png）确认印刷为 **A\*p**（斜体 p 带下伸笔清晰），Edit 修复 A^{*n} → A^{*p}；②初读疑 "C_r^{*p,q} est formé des éléments x ∈ A\*p,q"，600dpi（p013_Cr_600.png）确认印刷为 **x ∈ A\*p**（无 ,q），MD 正确。
- 差异：无其他。
- 备注：md 行 557 起 "Les groupes différentiels R\* et S\*." 段属印刷 p.437；该段 "homomorphismes canoniques permis" 表述待 p.014 对照印刷核查。

## p.014（PDF p.14 / 印刷 p.437）
- PNG：audit/p014.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p014_b_600.png、p014_annul_600.png、p014_annul2_600.png、p014_prod_600.png、p014_prop3_600.png、p014_permis3_600.png（600dpi）
- 核对：Les groupes différentiels R\* et S\*.（R\* = A\*/A\*¹、S_p\* = E_1\*^{p,0}、"homomorphismes canoniques permis"、H^p(S\*) → H^p(A\*) → H^p(R\*)、transgression d_p: E_p\*^{0,p−1} → E_p\*^{p,0}、δ 展示式 H^{p−1}(R\*) →δ H^p(A\*¹) ← H^p(S\*)、cocycle transgressif 判据 da ∈ S_p\*）；Exemple（ⁿA\* = Hom(ⁿA, G)、A\* = ∑ⁿA\*、appelons A\*^p l'annulateur de A^{p−1}）；Structure multiplicative（(a) antidérivation d(x·y) = dx·y + (−1)^p x·dy；(b) A\*^i·A\*^j ⊂ A\*^{i+j}；E_r\* 乘积 E_r\*^{p,q}·E_r\*^{p′,q′} ⊂ E_r\*^{p+p′,q+q′}；antidérivations des E_r\*）；Une suite exacte（Prop 3 对偶版）；§6 revêtement universel 开头
- 结果：PASS±
- 仲裁记录：①(b) 行 150dpi 疑为 A\*^p·A\*^q，600dpi（p014_b_600.png）确认印刷为 **A\*^i·A\*^j ⊂ A\*^{i+j}**（印刷自身在 (a) 用 p,q、(b) 用 i,j 的记号切换），MD 忠实；②乘积式首因子 150dpi 疑为 H_r，600dpi（p014_prod_600.png）确认为 **E_r**，MD 正确；③"appelons A\*^p"（p014_annul2_600.png）与 "l'annulateur de A^{p−1}"（p014_annul_600.png）确认，MD 正确；④"canoniques permis" 确为印刷原文（p014_permis3_600.png），MD 忠实于该异常表述。
- PASS± 项（不修）：①印刷 quirk：对偶 Prop 3 展示式中 H^j(**A\**)? 有星号而 H^i(**A**) 无星号（p014_prop3_600.png），印刷自身不一致，MD 逐字保留 "H^{i}(A)"，不改；②md 行 580 "il en est de même des $E_{r}^{*}$" 句尾缺印刷的句点——标点级，不误导，不修。
- 差异：无内容错误。
- 备注：md 行 589 起 "## 6…" 之后 §6 正文（Pontrjagin 引用、Définition du revêtement universel 段）属印刷 p.438。

## p.015（PDF p.15 / 印刷 p.438）
- PNG：audit/p015.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p015_Pi1b_600.png、p015_Erq2_600.png、p015_Erq3_600.png、p015_Pi2_600.png（600dpi）
- 核对：Pontrjagin Topological groups n° 46 引用与 Leray-Cartan ([8], [3], [6]) 句；Définition du revêtement universel 全段（e、T、V_U、p: T → X projection、π_i(T) ≅ π_i(X) (i = 2, 3, ⋯)）；Les opérateurs définis par Π sur T（Π opère canoniquement、homéomorphisme sans point fixe、K(T) Π-libre、K(T)_Π ≅ K(X)）；La suite spectrale（[6] Exp. XII）；PROPOSITION 4 全文（Π = π_1(X)、suite (E_r) avec E_2^{p,q} = H_p(Π, H_q(T, G))）；Une suite analogue existe en cohomologie；(Précisons que H_p(Π, H_q(T, G))…Hopf-Eilenberg-MacLane-Eckmann…)；COROLLAIRE 1（Π = Z、H_i(X, k) ≅ H_i(T, k) ⊕ H_{i−1}(T, k)）
- 结果：FAIL（已当场修复 2 处）
- 仲裁记录与修复：
  - **[已修复]** md 行 597 "le groupe fondamental II de X" 的 "II"：600dpi（p015_Pi1b_600.png）确认印刷为希腊字母 **Π**（顶横杠与双脚衬线清晰，非罗马数字 II），Edit 修复为 "$\Pi$"（md 全文其余处均作 $\Pi$，此为孤立误读）。
  - **[已修复]** md 行 615 "COROLLAIRE 1. Si II est le groupe additif Z" 的 "II"：600dpi（p015_Pi2_600.png）确认印刷为 **Π**，Edit 修复为 "$\Pi$"。
  - 150dpi 疑 Prop 4 为 E_r^{p,q}，600dpi（p015_Erq3_600.png）确认印刷为 "(E_r) avec **E_2^{p,q}**"（同行 (E_r) 的 r 与之对照），MD $E_{2}^{p,q}$ 正确。
- 差异：无其他。
- 备注：md 行 619 起 "Si $\Pi$ = Z opère trivialement…"、COROLLAIRE 2、Note 与 "## CHAPITRE II" 开头属印刷 p.439；COROLLAIRE 2 中 "$\pi$ soit un groupe d'ordre fini" 的大小写待 p.016 仲裁。

## p.016（PDF p.16 / 印刷 p.439）
- PNG：audit/p016.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p016_pi2_600.png、p016_pi2b_600.png、p016_sil4_600.png（600dpi）
- 核对：Si Π = Z 段（H_0(Π,G) = H_1(Π,G) = G、H_i(Π,G) = 0 pour i ≧ 2、Hurewicz [18]、homologie d'un cercle、E_2、d_2, d_3, ⋯ nulles、E_∞ ≅ E_2）；展示式 H_0(Π, H_i(T,k)) = H_i(T,k) et H_1(Π, H_{i−1}(T,k)) = H_{i−1}(T,k)；Puisque les coefficients…（non canoniquement）；COROLLAIRE 2 全文（π groupe d'ordre fini、caractéristique ne divise pas l'ordre de Π、H_i(X,k) = H_i(T,k)、"Japanese homomorphism"、corollaire à la Prop. 3）；Note（[6] Exp. XI, XII, XIII）；CHAPITRE II 章标题；§1 Homologie singulière cubique（Eilenberg [10]、simplexes/cubes）；Les cubes singuliers（I = (0,1)、u: I^n → X、dégénéré 定义、si et seulement si il est ponctuel）
- 结果：PASS
- 仲裁记录：①COROLLAIRE 2 印刷确为**小写 π**（"Supposons que π soit un groupe d'ordre fini"，p016_pi2b_600.png）而同段 "l'ordre de Π)" 用大写（p016_pi2_600.png）——印刷自身大小写混用，MD "$\pi$…$\Pi$" 忠实保留，不改；②150dpi 疑页尾为 "s'il est"，600dpi（p016_sil4_600.png）确认印刷为 "**si il** est"（两词分写），MD 忠实，不改。
- 差异：无。
- 备注：md 行 646 起 "On notera $Q_n(X)$…" 与 "## L'opérateur bord." 段属印刷 p.440。

## p.017（PDF p.17 / 印刷 p.440）
- PNG：audit/p017.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p017_lamH_600.png、p017_ydot_600.png、p017_lami2_600.png（600dpi）
- 核对：Q_n(X)/D_n(X)/Q(X)/D(X) 定义；L'opérateur bord（faces、H/K/φ_K、λ_H^ε u 定义式、y_i 规则 "si i ∈ H, ẏ_i = ε / si i ∈ K, y_i = x_{φ_K(i)}"、λ_i^ε 简记 λ_{\{i\}}^ε、λ_i^0/λ_i^1 展开式、du = ∑_{i=1}^n (−1)^i(λ_i^0 u − λ_i^1 u)、λ_i^ε∘λ_j^{ε′} = λ_{j−1}^{ε′}∘λ_i^ε (i < j)、ddu = 0、λ_n^0 u = λ_n^1 u、D(X) sous-groupe permis）；Les groupes d'homologie et cohomologie cubiques（DÉFINITION C(X) = Q(X)/D(X)、chaînes cubiques singulières、C_n(X) = Q_n(X)/D_n(X)、groupe libre/coefficients universels）
- 结果：FAIL（已当场修复 2 处）
- 仲裁记录与修复：
  - **[已修复]** md 行 655 "$\lambda_{H}^{e}u$" 与行 697 "$\lambda_i^e u$" 的上标 e：600dpi（p017_lamH_600.png）确认印刷为 **ε**（"lier λ_H^ε u, de dimension q"；同页定义处同行自身即有 "$\varepsilon = 0$ ou 1"），两处 Edit 修复为 "\varepsilon"。
  - 印刷 quirk 登记（不修）：y_i 规则首行印刷为 "**ẏ_i** = ε"——y 上有实心圆点（p017_ydot_600.png，位置居中、形状规则，为印刷实物，疑原书排版失误），md 的 "\dot{y_i}" 忠实保留。
- 仲裁记录（MD 正确项）：150dpi 疑 "au lieu de λ_i^ε u"（无花括号），600dpi（p017_lami2_600.png）确认印刷为 **λ_{\{i\}}^ε u**（下标花括号清晰），MD "$\lambda_{\{i\}}^{\epsilon}u$" 正确（该处 md 用 \epsilon、他处用 \varepsilon，同一字母变体，排版级不修）。
- 差异：除上述两处 e→ε 外无。
- 备注：md 行 703 起 "Nous noterons $C_n(X, G)$…"、cochaines 段与 "## Multiplication des cochaines." 属印刷 p.441。

## p.018（PDF p.18 / 印刷 p.441）
- PNG：audit/p018.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p018_Hn_600.png、p018_lamK2_600.png、p018_Tx2_600.png（600dpi）
- 核对：C_n(X, G) = C_n(X) ⊗ G 与 H_n(X, G)；C^n(X, G) = Hom(C_n(X), G)、fonction nulle sur les cubes dégénérés、cobord d、H^p(X, G)；Multiplication des cochaines（f·g 定义式 (f·g)(u) = ∑_H ρ_{H,K} f(λ_K^0 u)·g(λ_H^1 u)、ρ_{H,K} = (−1)^ν 与 (i, j)、j < i 计数、d(f·g) = df·g + (−1)^p f·dg、λ_K^0/λ_H^1 引理、élément unité、anneau de cohomologie H\*(X, G) = ∑_n H^n(X, G)）；Coefficients locaux（Steenrod [30]、T_h: G_a → G_b、classe d'homotopie、transitivité、G_a 与 groupe fondamental、premier sommet x = u(0, ⋯, 0)、d(g·u) = ∑_{i=1}^n (−1)^i(T_{u,i,0}(g)·λ_i^0 u − T_{u,i,1}(g)·λ_i^1 u)）
- 结果：FAIL（已当场修复 1 处）
- 仲裁记录与修复：
  - **[已修复]** md 行 725 "$\lambda_{\kappa}^{0} u$" 的下标 κ：600dpi（p018_lamK2_600.png）确认印刷为**大写 K**（λ_K^0，与同句 "K est le complémentaire de H" 一致），Edit 修复为 "\lambda_{K}^{0}"。
  - MD 正确项：①150dpi 疑 "H^n(X, G)"，600dpi（p018_Hn_600.png）确认印刷为 **H^p(X, G)**（印刷在 "dimension n" 语境下仍写 p，print quirk，MD 忠实保留）；②150dpi 疑 T 下标为 x，600dpi（p018_Tx2_600.png）确认印刷为 **T_{u,i,0}/T_{u,i,1}**（下标 u），MD 正确。
- 差异：无其他。
- 备注：md 行 735 起 "où $T_{u,i,\epsilon}$ désigne l'isomorphisme…"、cup-product 段与 χ_{u,H} 路径定义属印刷 p.442，留待下一分块。

## p.019（PDF p.19 / 印刷 p.442）
- PNG：audit/p019.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p019_sum_600.png、p019_sum3_600.png（600dpi）
- 核对：T_{u,i,ε} 说明（t → u(0, ⋯, tε, 0, ⋯, 0)、T_{u,i,0}(g) = g）；cup-product 式 (f·g)(u) = ∑_H ρ_{H,K} f(λ_K^0 u)·τ_{u,H} g(λ_H^1 u)；χ_{u,H}(t) = u(x_1, ⋯, x_{p+q})（x_i = 0 si i ∈ K, x_i = t si i ∈ H）；Comparaison avec la théorie singulière classique（L_n、∑_0^n y_i = 1、y_0 = 1 − x_1 / y_1 = x_1(1 − x_2) / ⋯ / y_n 公式组、θ_n: I^n → L_n、θ homomorphisme、isomorphismes sur、Eilenberg-MacLane en préparation）；f·g = (−1)^{pq} g·f（anticommutativité du cup-produit）；"homologie singulière"命名约定段；§2 Espaces fibrés; définition et premières propriétés 开头
- 结果：PASS
- 仲裁记录：150dpi 疑印刷 ∑ 下限为 i，600dpi（p019_sum3_600.png，4x）确认印刷为 **∑₀**（下限 0，与同行 "(E_r)" 类对照清晰），MD $\sum_{0}^{n}$ 正确。
- 差异：无。
- 备注：md 行 775 起 "Pour établir…le théorème" 的续文属印刷 p.443。

## p.020（PDF p.20 / 印刷 p.443）
- PNG：audit/p020.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p020_triple_600.png、p020_prop1b_600.png、p020_prop1c_600.png、p020_lemme2b_600.png（600dpi）
- 核对：relèvement des homotopies 段；DÉFINITION espace fibré（triple、(R) 性质全式）；Exemples 1–4（fibre-bundles [5] Exp. VIII、fibre-spaces d'Hurewicz-Steenrod、GLG/Gleason [5] Exp. VII + 脚注2（Borel C.R. 230 1950 p.1246-1248；作者 Ibid. p.916-918）、Chapitre IV espaces de chemins）；REMARQUE（p^{-1}(b) fermés、topologie quotient）；PROPOSITION 1 全文；LEMME 1/LEMME 2；Prop. 1 证明开头（Y、j: X → Y ⊂ I^n、r rétraction、x → (r(x), j(x))）
- 结果：FAIL（已当场修复 1 处）
- 仲裁记录与修复：
  - **[已修复]** md 行 779 "le triple $E, p, B$" 缺括号：600dpi（p020_triple_600.png）确认印刷为 "**(E, p, B)**"，Edit 修复为 "$(E, p, B)$"。
- PASS± 项（print quirk 登记，不修）：①Prop 1 印刷作 "A et **K** deux polyèdres finis, contractiles, tels que A ⊂ X"（p020_prop1c_600.png 确认 K；K 在后文未再用，条件句实际用 X）——印刷自身记号不一致，md 忠实保留；②LEMME 2 印刷作 "a → (a, s), **ou** s est un point fixé"（p020_lemme2b_600.png：无重音，对比同行 "où n est" 有重音符）——印刷自身笔误（应为 où），md 忠实保留 "ou"。
- 差异：无内容错误（除已修复项）。
- 备注：md 行 797 起 "D'autre part, X est un rétracte…"、REMARQUE réciproque、APPLICATION（π_i(E mod. F) ≅ π_i(B)）与 suite exacte d'homotopie 展示式属印刷 p.444。

## p.021（PDF p.21 / 印刷 p.444）
- PNG：audit/p021.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p021_homol_600.png、p021_cond2b_600.png、p021_SCdef2_600.png、p021_Sc_600.png（600dpi）
- 核对：Prop.1 证明结尾与 REMARQUE réciproque；APPLICATION（F = p^{-1}(b)、π_i(E mod. F) ≅ π_i(B)）；suite exacte d'homotopie ⋯ → π_i(F) → π_i(E) → π_i(B) → π_{i−1}(F) → π_{i−1}(E) → ⋯；§3 Le système local formé par l'homologie de la fibre（F = p^{-1}(b)、B et F connexes par arcs、cubes sommets en x (ou b)、"l'homologie de F, E, E mod. F, B"）；DÉFINITION construction subordonnée à v（条件 1 λ_1^0 C(u) = u；条件 2 (p∘C(u))(t, t_1, ⋯, t_n) = v(t)；条件 3 C(λ_i^ε u) = λ_{i+1}^ε C(u)；条件 4 dégénéré）；S_c 定义（(S_c u)(t_1, ⋯, t_n) = C(u)(1, t_1, ⋯, t_n)）与 S_c(λ_i^ε u) = λ_i^ε(S_c u)
- 结果：PASS
- 仲裁记录（MD 正确项）：①150dpi 疑印刷为 "l'homologie de E, E mod. F, B"（无 F），600dpi（p021_homol_600.png）确认行首为 **F**，即 "de F, E, E mod. F, B"，MD 四项正确；②条件 2 参数表 150dpi 疑无前导 t，600dpi（p021_cond2b_600.png）确认印刷为 **(t, t_1, ⋯, t_n)**，MD 正确；③S 下标 2x 下疑为资本 C，4x（p021_Sc_600.png）确认定义行与条件行均为**小写斜体 c**（S_c），MD 一致。
- 差异：无。
- 备注：md 行 845 起 "nombre d'éléments de H…"、LEMME 3、PROPOSITION 2 与 (C u)(t, t_1, ⋯, t_n) 展示式属印刷 p.445。

## p.022（PDF p.22 / 印刷 p.445）
- PNG：audit/p022.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p022_SCline1_600.png、p022_SClemme_600.png、p022_SCpermis_600.png、p022_SCtoutu_600.png、p022_SCdou_600.png、p022_SCdisp_600.png、p022_SCfin_600.png、p022_cqfd_600.png（600dpi；p022_SC1/SC2/SC3_600.png 为前次中断会话遗留同页裁剪，经我复核内容后一并引用）
- 核对：LEMME 3 全文（S_{c_1}/S_{c_2} homotopiquement équivalents）与 "(La démonstration sera donnée au n°13)"；T_α 定义段（S_c endomorphisme permis、ne dépend que de α）；PROPOSITION 2 全文（représentation de π₁(B) dans … automorphismes de H(F)）+ (Rappelons … Chap. IV, n°1) 括注；T_e = 1 与 T_α∘T_β = T_{α∗β} 两处；展示式 (Cu)(t, t₁, ⋯, t_n) = u(t₁, ⋯, t_n)；构造 C″ 分段定义（si t ≤ 1/2 / si t ≥ 1/2 两情形）；展示式 (S_{c″}u)(t₁, ⋯) = (C(S_{c′}u))(1, ⋯) = (S_c∘S_{c′}u)(⋯)；"D'où S_{c″} = S_c∘S_{c′} … cqfd"；π₁(B) opérait 段与 systèmes locaux；PROPOSITION 3 全文（groupe structural G、connexe par arcs、opère trivialement sur H(F) et H*(F)）；S_cu = u 段；Soit T 段（0 et 1 de I、v′: T → B、image réciproque，跨页断句 "par l'application"）
- 结果：FAIL（已当场修复 3 处）
- 仲裁记录与修复：
  - **[已修复]** md 行 866 展示式第二情形 "$C (S _ {C ^ {\prime}} u)$" 的下标大写 C′：600dpi（p022_SCdou_600.png）确认印刷为小写 **c′**，即 (C(S_{c′}u))(2t − 1, t₁, ⋯, t_n)；Edit 修复为 "$S _ {c ^ {\prime}}$"。本页印刷 S 下标全程为小写斜体 c（p022_SCline1_600.png：S_c(λ_H^ε u) = λ_H^ε(S_c u)；p022_SCpermis_600.png：S_c … S_c；p022_SC2/p022_SClemme_600.png：S_{c₁}、S_{c₂}；p022_SCdisp_600.png：S_{c″}、S_{c′}、S_c∘S_{c′}），md 行 866 为孤立大写误读。
  - **[已修复]** md 行 875 "$S_{c','}$"（下标 c',' ）为 OCR 伪迹：600dpi（p022_cqfd_600.png、p022_SCdisp_600.png）确认印刷为 **S_{c″}**（c 加双 prime），与 md 行 872 展示式自身的 "$S _ {c ^ {\prime \prime}}$" 一致；Edit 修复为 "$S_{c''}$"。
  - **[已修复]** md 行 875 "$T_\alpha *_\beta$"（∗ 带下标 β 且游离在 T 下标之外）：600dpi（p022_cqfd_600.png、p022_SC3_600.png）确认印刷为 **T_{α∗β}**（α、∗、β 同处 T 的下标层，β 的下伸仅为希腊 beta 自带笔形）；Edit 修复为 "$T_{\alpha* \beta}$"，与 md 行 855/863 自身写法一致。
- PASS± 项（print quirk 登记，不修）：印刷行 "π₁(B) **opérait** canoniquement sur H(F)"（p022_SCdisp_600.png 底缘清晰可读；按语法应为 opère）——印刷自身笔误，md 行 877 忠实保留 "opérait"，不改。
- 差异：除上述 3 处外无。文本层对账（pdftotext -f 22 -l 22）与正文逐句一致（OCR 噪声 "Sc"、"T,,*B" 等不构成差异）。
- 备注：mineru 将两展示式线性化为 array/cases，与印刷版式等价；md 行 885 起 "v' (Voir [5], VII et VIII)…" 属印刷 p.446，留待 p.023。

## p.023（PDF p.23 / 印刷 p.446）
- PNG：audit/p023.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p023_Scu_600.png、p023_lam_600.png、p023_lam2_600.png（600dpi）
- 核对：跨页续句 "v′ (Voir [5], VII et VIII)；E′ … diagramme commutatif"；交换图（E′ —h→ E；p′↓ p↓.；T —v′→ B，含 p 箭头后句点）；"Comme G est connexe par arcs…S_cu = u" 段（C(u) = h∘(I × u)、u: Iⁿ → F）；Note 段（sans hypothèses de connexion、systèmes locaux sur B）；§4 标题 "4. Filtration du complexe singulier de E"；(Rappelons …) 括注；"Nous allons filtrer…" 段（suite spectrale (E_r)、Voir Th. 2、E_∞、groupe gradué associé au groupe filtré H(E)）；Définition de la filtration 行；T^p ⊂ T^{p+1} 链、T^{p,q} ⊂ Q_{p+q}(E) 定义两句、p(u(t₁, ⋯, t_{p+q})) 与 t_{p+1}, ⋯, t_{p+q}；On pose: T^p = Σ_q T^{p,q}；(Φ) 0 ≦ w(x) ≦ deg. x；lorsque x ≠ 0 est homogène；En outre 稳定段（λ_i^ε u ∈ T^p、λ_i^ε u ∈ T^{p−1}、stables、n°1 et 2 du Chap. I）
- 结果：PASS
- 仲裁记录：①150dpi 初读末段 λ 下标上疑无上标 ε，600dpi（p023_lam2_600.png、p023_lam_600.png）确认两处印刷均为 **λ_i^ε u**（ε 上标清晰），MD "$\lambda_i^\epsilon u$" 正确；②600dpi（p023_Scu_600.png）确认 "telle que **S_cu** = u" 下标为小写斜体 c，与 p.022 全页 S 下标约定一致，MD 正确。
- 差异：无。
- 备注：交换图线性化为 array（p′↓ 与 p↓. 同行、句点保留），节点/箭头/标记逐项吻合；md 行 923 起 "Etude du terme E_0." 属印刷 p.447，留待 p.024。

## p.024（PDF p.24 / 印刷 p.447）
- PNG：audit/p024.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p024_d0u_600.png、p024_prop3_600.png（600dpi）
- 核对：Etude du terme E_0 行；Rappelons 段（E_0^p = A^p/A^{p−1}、E_0 = Σ_p E_0^p、d_0、combinaisons linéaires … w(u) ≦ p−1）；Si u est un cube 段与展示式 d_0u = Σ_{i>p} (−1)^i(λ_i^0 u − λ_i^1 u) dans E_0^p；puisque λ_i^ε u ∈ T^{p−1} si i ≦ p；Définissons … opérations B et F 段；Bu/Fu 两定义式（含 (y_i quelconques)）；(Pour un cube u donné …) 括注（Fu, Bu 顺序、w(u) ≦ p ≦ deg. u）；propriétés 1) 2) 3)（Bλ_i^ε u = Bu、Fλ_i^ε u = λ_{i−p}^ε Fu si i > p, ε = 0, 1）；J_p = C_p(B) ⊗ C(F) 与 d_F(b ⊗ f) = (−1)^p b ⊗ df；φ: E_0^p → J_p 与 (1) φ(u) = Bu ⊗ Fu；compatibilité 段（d_F∘φ = φ∘d_0、homomorphisme permis）；§5 标题 "5. Calcul du terme E₁"；PROPOSITION 4 全文（équivalence de chaînes）；末行 ψ: J_p → E_0^p 起句（跨页）
- 结果：PASS
- 仲裁记录：①600dpi（p024_d0u_600.png）确认展示式下限 **i > p**、λ_i^0/λ_i^1 两上标、随句 **dans E_0^p,** 与 "puisque λ_i^ε u ∈ T^{p−1} si i ≦ p."（含 ε 上标与句点）均与 MD 一致；②600dpi（p024_prop3_600.png）确认性质 3) 印刷为 **Bλ_i^ε u = Bu, Fλ_i^ε u = λ_{i−p}^ε Fu si i > p, ε = 0, 1.**（下标 i−p 清晰），MD 逐项吻合。
- PASS± 项（排版级，不修）：①md 行 930 展示式内 "dans" 被 mineru 拆成 "d a n s"（字母间空格）；②md 行 938 的 "(y_i quelconques)" 附于 array 之后（渲染时贴 Fu 行），印刷中与 Bu 行对齐——线性化排版差异，内容无损；③md 行 933 句尾缺印刷句点；④md 行 949 "\mathrm{si}" 直立体对印刷斜体 si。
- 差异：无内容错误。
- 备注：md 行 973 起 "φ∘ψ = 1 …" 与 Construction de ψ、LEMME 4 属印刷 p.448，留待 p.025。

## p.025（PDF p.25 / 印刷 p.448）
- PNG：audit/p025.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p025_lemme4_600.png、p025_lemme5_600.png、p025_disp_600.png（600dpi）
- 核对：φ∘ψ = 1 段；Construction de ψ 行；LEMME 4 全文与条件 1–3（B·K(u,v) = u et F·K(u,v) = v；K(u, λ_i^ε v) = λ_{i+p}^ε K(u, v) (ε = 0, 1)；Si v est dégénéré…）与 "(La démonstration sera donnée au n°11)"；Posons ψ(u ⊗ v) = K(u, v) 段（filtration ≦ p − 1 d'après 1.）；La propriété 2. 段（h = ψ∘φ opérateur d'homotopie sur E_0^p）；LEMME 5 全文与条件 1–5（B·Su = Bu；Su(0, ⋯, 0, t, x₁, ⋯, x_q) = u(0, ⋯, 0, x₁, ⋯, x_q)；λ_{p+1}^0 Su = u et λ_{p+1}^1 Su = K(Bu, Fu)；Sλ_i^ε u = λ_{i+1}^ε Su；Si q > 0…）与 n°12 括注；Posons k(u) = (−1)^p Su 段与三条 "si …(Propriété …)" 判据；Calculons alors d_0ku + kd_0u 与两展示式（Σ_{i=p+1}^{n+1} (−1)^{i+p}(λ_i^0 Su − λ_i^1 Su)；kd_0u = Σ_{i=p+1}^{n+1} (−1)^{i+p}(Sλ_i^0 u − Sλ_i^1 u) = Σ_{i=p+2}^{n+1} (−1)^{i+p+1}(λ_i^0 Su − λ_i^1 Su),）；d'après la Propriété 4.
- 结果：PASS±（已当场修复 3 处编码伪迹）
- 仲裁记录与修复：
  - **[已修复]** md 行 997/998/1004 的 HTML 实体 "$i &gt; p$"、"$q &gt; 0$"（×2）：600dpi（p025_lemme5_600.png）确认印刷为数学关系号 **>**（"Pour tout i > p"、"Si q > 0"），Edit 修复为 ">"。该实体在 math 内会妨碍 LaTeX 渲染，按 SOP「妨碍使用时修复并登记」处理。
  - 仲裁记录（MD 正确项）：①LEMME 4 条件 2 的 λ_{i+p}^ε 下标（p025_lemme4_600.png 清晰）；②LEMME 5 条件 3 的 λ_{p+1}^0/λ_{p+1}^1 与条件 4 的 Sλ_i^ε u = λ_{i+1}^ε Su（p025_lemme5_600.png）；③两展示式的求和限 i = p+1/i = p+2、上限 n+1、指数 i+p/i+p+1 与末尾逗号（p025_disp_600.png）均与 MD 逐项一致。
- PASS± 项（登记，不修）：①md 行 993–1010 被 mineru 包裹在 `<div class="docvortex-algorithm" style="white-space: pre-wrap; …">` 内——印刷并无算法框，此为导出结构伪迹；但 pre-wrap 渲染恰好按印刷行式呈现 LEMME 5 条件与三条判据，内容完整有序，不修（与已登记的 page-footnote span 同类处理；文件内 L1682/L1686/L1690 还有三处同类 div，属后续分块页域，不在本页处置）；②md 行 1008 将印刷的两行展示式压平为同一行内联 math（内容两式俱全、逗号保留）——线性化伪迹；③md 行 1005 "(Propriété 1)." 缺印刷句末句点（印刷作 "(Propriété 1.)."）——标点级；④三条 "si…" 判据保留 4 空格缩进（依赖 ① 的 pre-wrap 呈现）。
- 差异：无数学内容错误。
- 备注：md 行 1012 起 "On a done/donc: d_0ku + kd_0u = …" 展示式与 Th. 1 属印刷 p.449，留待 p.026（"done/donc" 之辨待该页仲裁）。

## p.026（PDF p.26 / 印刷 p.449）
- PNG：audit/p026.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p026_donc_600.png（600dpi）
- 核对：On a donc 行；展示式 d_0ku + kd_0u = (−1)^{2p+1}(λ_{p+1}^0 Su − λ_{p+1}^1 Su) = K(Bu, Fu) − u = h(u) − u,；ce qui montre que h … achève la démonstration de la Proposition 4；Soit maintenant G un groupe abélien 段（A ⊗ G、facteurs directs、homotopiquement équivalent à C_p(B) ⊗ C(F) ⊗ G = C_p(B) ⊗ C(F, G)）；Puisque C_p(B) est un groupe libre 段；THÉORÈME 1 全文（E_1^{p,q}、chaînes singulières de dimension p、q-ème groupe d'homologie singulière）；(2) E₁ = C(B, H(F))；REMARQUE（degré filtrant = degré-base、complémentaire = degré-fibre、total）；§6 标题 "6. Calcul du terme E₂"；Nous venons de voir 段（d₁、E₂ = H(E₁)）；Soit x = b ⊗ h 段；Soit y … d₁x 计划段（ψ(y) ∈ E_0^{p,q}、z ∈ A^p、dz ∈ A^{p−1}、t ∈ C_{p−1}(B) ⊗ C_q(F, G)）；(Avant de donner … B^p u, K^p(u, v), etc.) 括注
- 结果：FAIL（已当场修复 1 处）
- 仲裁记录与修复：
  - **[已修复]** md 行 1013 "\text {On a done:}"：600dpi（p026_donc_600.png）确认印刷为 **"On a donc:"**（d-o-n-c 清晰；done 非法语词），Edit 修复为 "donc"。
  - MD 正确项：同裁剪确证展示式指数 **2p+1**、λ_{p+1}^0/λ_{p+1}^1 下标与末尾逗号，与 MD 逐项一致。
- 差异：除上述 1 处外无。
- 备注：本页 THÉORÈME 1 为全篇核心定理之一，陈述全文逐句核对无差；md 行 1042 起 "Ecrivons d'abord un cycle m …" 与 z、dz 两展示式属印刷 p.450，留待 p.027。

## p.027（PDF p.27 / 印刷 p.450）
- PNG：audit/p027.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p027_dz_600.png、p027_deux_600.png、p027_Sc_600.png、p027_Sc2_600.png、p027_Sc3_600.png、p027_Sc4_600.png、p027_donc2_600.png（600dpi）
- 核对：Ecrivons d'abord un cycle m 段（m = Σ_α g_α u_α、y = b ⊗ m）；z = Σ_α g_α K^p(b, u_α)；dz = Σ_{α,i=1}^{n} (−1)^i g_α[λ_i^0 K^p(b, u_α) − λ_i^1 K^p(b, u_α)]；décomposer 段（Σ_{i≦p} + Σ_{i>p}、λ_i^ε K^p(b, u_α) = K^p(b, λ_{i−p}^ε u_α)、Σ_{α,i=1}^{q} g_α(−1)^i(λ_i^0 u_α − λ_i^1 u_α)、nulle dans C(E)）；dz = Σ_{α,i=1}^{p} …；filtration ≦ p − 1 与 φ^{p−1} 段（φ^{p−1}(u) = B^{p−1}u ⊗ F^{p−1}u）；B^{p−1}λ_i^ε K^p(b, u_α) et F^{p−1}λ_i^ε K^p(b, u_α) (i ≦ p)；Le premier … λ_i^ε b 段与 (F^{p−1}λ_i^ε K^p(b, u_α))(x₁, ⋯, x_q) = K^p(b, u_α)(0, ⋯, 0, ε, 0, ⋯, 0, x₁, ⋯, x_q)；où ε est à la i-ème place；construction u → C(u) 定义式 C(u)(t, x₁, ⋯, x_q) = K^p(b, u)(0, ⋯, 0, tε, ⋯)；On vérifie 段（v(t) = b(0, ⋯, 0, tε, 0, ⋯, 0)、S_{c,b,i,ε} l'endomorphisme、on a donc;）；S_{c,b,i,ε} u_α = F^{p−1}λ_i^ε K^p(b, u_α),；t = Σ_{α,i=1}^{p} (−1)^i g_α[(λ_i^0 b) ⊗ S_{c,b,i,0} u_α − (λ_i^1 b) ⊗ S_{c,b,i,1} u_α]；Notons T_{b,i,ε} 段；(3) d₁x = Σ_{i=1}^{p} (−1)^i(λ_i^0 b ⊗ T_{b,i,0}h − λ_i^1 b ⊗ T_{b,i,1}h)
- 结果：FAIL（已当场修复 1 处）
- 仲裁记录与修复：
  - **[已修复]** md 行 1084 "$S_{c,b,i,e}$" 的下标末位罗马字母 e：600dpi（p027_Sc4_600.png）确认印刷为希腊 **ε**（两弧开口字形），与 md 行 1087 展示式及行 1096 自身的 "$S_{c,b,i,\varepsilon}$" 一致；Edit 修复为 "$S_{c,b,i,\varepsilon}$"（同 p.017 λ^e→λ^ε 类误读）。
- 仲裁记录（MD 正确项）：①行 1054 "l'expression Σ_{α,i=1}^{q}…" 上限 600dpi（p027_deux_600.png）确认印刷为 **q**（u_α 为 F 的 q 维立方），MD 正确；②同裁剪确认 λ_{i−p}^ε 下标 i−p；③dz 首展示式上限 n（p027_dz_600.png）；④t 展示式两 S_{c,b,i,0}/S_{c,b,i,1} 下标与 λ_i^0 b/λ_i^1 b 括号（p027_Sc_600.png）；⑤(3) 式结构与 \tag{3} 对应印刷左侧编号。
- PASS± 项（print quirk 登记，不修）：①印刷行 14 句末作 "on a **donc;**"（分号，按文意应为冒号；p027_donc2_600.png 清晰）——印刷自身标点笔误，md 行 1084 忠实保留 "donc;"；②行 1054 同行内 \epsilon 与 \varepsilon 混用（λ_i^{\epsilon} vs \varepsilon=0,1）——字母变体排版级；③md 行 1062–1068 把 "(i ≦ p)" 拆成独立展示式——线性化伪影。
- 差异：除已修复 1 处外无。
- 备注：md 行 1102 起 "Si le système local … (3′) d₁x = (db) ⊗ h" 与 PROPOSITION 5、THÉORÈME 2 属印刷 p.451，留待 p.028。

## p.028（PDF p.28 / 印刷 p.451）
- PNG：audit/p028.png（pngmono 150dpi）；仲裁裁剪 audit/300dpi/p028_ref_600.png、p028_Rq_600.png、p028_Rq2_600.png、p028_disp_600.png（600dpi）
- 核对：Si le système local … 段与 (3′) d₁x = (db) ⊗ h；PROPOSITION 5 全文（opérateur de bord naturel、coefficients locaux）；On tire tout de suite 段；THÉORÈME 2 全文（H_p(B, H_q(F, G))、système local）；(4) E₂ = H(B, H(F))；Note 段（Leray [24] n°6, b、Čech à supports compacts、[6] Exp. IX、les trois cas）；Signalons 段（sans supposer B, ni F, connexes、E mod. F、groupes d'homotopie）；§7 标题 "7. Propriétés de la suite spectrale d'homologie"；Commençons 段（R 的刻画、R_q ≅ C_q(F, G)）；Le groupe différentiel S = Σ S_p 段（E_1^{p,0} ≅ C_p(B) ⊗ H_0(F, G) = C_p(B, G)、π: A → S、p: E → B）；On peut alors 段与两行展示式 H_i(F, G) → E_∞^{0,i} → H_i(E, G) / H_i(E, G) → E_∞^{i,0} → H_i(B, G),
- 结果：PASS
- 仲裁记录：①150dpi 初读 Note 引用疑为 "[8]， Exp. IX"，600dpi（p028_ref_600.png）确认印刷为 **[6]**（单碗带升干字形，非双层 8），MD 行 1122 "[6]， Exp. IX" 正确——我方初读有误；②600dpi（p028_Rq2_600.png）确认 "le groupe **R_q** est isomorphe à C_q(F, G)" 下标为斜体 q（非 0），MD 正确；③600dpi（p028_disp_600.png）确认两行展示式上标 **E_∞^{0,i}** 与 **E_∞^{i,0}**，MD 逐项一致。
- PASS± 项（排版级，不修）：md 行 1134–1140 将印刷的两行同组展示式拆为两个独立 $$ 块——线性化伪影，内容无缺损。
- 差异：无。
- 备注：本页含 THÉORÈME 2（Leray-Serre 经典定理），全文逐句核对无差。md 行 1142 起 "les premiers étant sur…" 属印刷 p.452，留待 p.029。
