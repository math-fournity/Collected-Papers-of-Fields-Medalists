# AUDIT-ribet1990 — 逐页视觉审计记录

> 依据 `AUDIT-SOP.md`「流程（每页 7 步）」「审计说明格式」「审计后修复」执行；一页一条，逐页交错落签。

- 论文：K.A. Ribet, *On modular representations of Gal(Q̄/Q) arising from modular forms*, Inventiones mathematicae **100** (1990), 431–476。
- PDF：`1998年 - Wiles/ribet1990.pdf`（47 页；p.1 为 Göttingen 数字化收藏封面/条款页，p.2–47 为正文扫描页，对应印刷 p.431–476，即 PDF p.N（N≥2）↔ 印刷 p.429+N）。
- 待审 Markdown：`1998年 - Wiles/ribet1990_mineru/ribet1990__ribet1990.md`（mineru 3.4.4 导出；`middle_json.json` 47 页；导出 metadata 未含独立 doc_id，记 UNKNOWN）。
- actor = Wf-P42；host/model/effort = zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run级配置，自报UNKNOWN）。
- PDF SHA-256 = `08f8ebfda40855d0f6d9e90e1dc352eb6576ecc44cc7c6e6ca3d448d724503b4`（开工实测与任务给定一致）。
- MD 基线 SHA-256 = `8fa0375dd53408c63acd0170755d4457643c365c0fdd652e542e772d612c68bf`（开工实测与任务给定一致）。
- 文本层判定：**不可用**——`pdftotext -f 1 -l 1` 仅得收藏封面 3 行题录；p.2/3/5/10/20/47 抽测均无文本层（0–1 字符）。全程采用**纯 PNG 逐页视觉审计**（gs pngmono 150dpi 单页渲染 → 目检 → 与 Markdown 比对）。
- 审计开始：2026-10-02 13:58 -0400（date 实取）。
- 本文件按页序追加；全部页完成后在文末补「总评 + 抽查覆盖声明 + mineru doc_id」。

## p.001（PDF p.1 / 收藏封面页，无印刷页码）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 13:58 -0400。
- PNG：`audit/ribet1990_p001.png`（pngmono，150 dpi）；仲裁裁片：`audit/300dpi/ribet1990_p001_header.png`、`audit/300dpi/ribet1990_p001_contact.png`、`audit/300dpi/ribet1990_p001_terms_line.png`（pnggray，300 dpi）。
- 核对：封面题录块（题名/作者/刊名/卷页）、Terms and Conditions 全文、Purchase a CD-ROM 全文、两处 Contact 地址块、图片引用 `images/page_0_image_15.jpg`（存在 ✓）。
- 发现（修复前）：①mineru 丢封面左上题录块（"On modular representations of Gal (.../Q) arising from modular forms. / by Ribet, K.A. / in Inventiones mathematicae / volume 100; pp. 431 - 476"）；②MD "Niedersaechssische" 为 OCR 拼写误，300 dpi 裁片确认印刷为 "Niedersaechsische"（单 s；CD-ROM 块处 MD 本即正确）；③印刷原样 "Conditions.With the usage"（句号后无空格），mineru 规范化为 "Conditions. With"。
- 修复（本页 commit，依据上述 300 dpi 裁片）：①在文件首补入题录块五段；②Niedersaechssische→Niedersaechsische；③还原 "Conditions.With"。
- 印刷原文 quirk：封面题录写 "Gal (.../Q)"（GDZ 生成器无法排 Q̄ 上划线，字面三点省略）——修复①按印刷原样保留，不改为 Gal(Q̄/Q)。
- 结果：PASS±（三项瑕疵均已当场修复闭环；修复后与原图逐项吻合）。

## p.002（PDF p.2 / 印刷 p.431）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:05 -0400。
- PNG：`audit/ribet1990_p002.png`（pngmono，150 dpi）；仲裁裁片：`audit/300dpi/ribet1990_p002_assume.png`（pnggray，300 dpi）。
- 核对：题录（题名/K.A. Ribet/地址）、节标题顺序（1. Introduction → The Main Theorem）、表示 ρ: G → GL(2, F)、l ≥ 3、odd/eigenvalues +1, −1、trace(ρ)、finite at p 定义（[34]/[35], §2.8）、p ≢ 1 (mod l) 行间公式、段尾 "Our new" 接下页 ✓。
- 印刷原文 quirk：印刷首行即 "Assume that **ρ** is a prime which exactly divides N (we write p ∥ N)"——主语排成 ρ（数学预期为 p），300 dpi 裁片确证为印刷原样；MD 与印刷一致，忠实保留不改。
- 备注：页眉 "Invent. math. 100, 431–476 (1990) / Inventiones mathematicae © Springer-Verlag 1990" 为 mineru 惯例不收录；完整题录信息已在本 MD 文章题名块与 p.001 封面补录块中。
- 结果：PASS。

## p.003（PDF p.3 / 印刷 p.432）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:10 -0400。
- PNG：`audit/ribet1990_p003.png`（pngmono，150 dpi）。
- 核对：Theorem 1.1 (Main Theorem) 陈述与条件 1. p ≢ 1 (mod l)、2. N is prime to l；Corollary 1.2；Fermat 方程 a^l+b^l+c^l=0；Frey 曲线 y²=x(x−a^l)(x+b^l)；V=E[l]；(4.1.9)/(4.1.12)；证明结尾 "we have a contradiction." ✓ 全部与印刷一致。
- 备注：定理与推论陈述的斜体排版未保留（如条件 2 印刷为斜体 "*N* is *prime to l*"，MD 为正体）——mineru 惯例排版级伪影，不误导，按 SOP 默认不批量修；证明结束符 □ 未收录（惯例）。
- 结果：PASS±。

## p.004（PDF p.4 / 印刷 p.433）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:14 -0400。
- PNG：`audit/ribet1990_p004.png`（pngmono，150 dpi）。
- 核对：Summary 节前半——§2 Raynaud [24]/Grothendieck [11]/Mazur-Rapoport ([18], Appendix)；Deligne-Rapoport [4]、Cerednik-Drinfeld ([3], [7])；Theorem 4.1 与 Eichler [9]/Shimizu [36]/Jacquet-Langlands [12] 对应；Z[...T_n...]-module Z、fiber over F_p、J_0(pqM)_{F_q} 与 J_0(pqM)_{F_p} 的 p/q 互换方向；§5/§6 路线图、p ≢ 1 (mod l)、q ≡ −1 (mod l)、段尾 "and the image" 接下页 ✓ 全部与印刷一致。
- 结果：PASS。

## p.005（PDF p.5 / 印刷 p.434）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:18 -0400。
- PNG：`audit/ribet1990_p005.png`（pngmono，150 dpi）。
- 核对：Summary 后半（Cebotarev Density Theorem——印刷原拼无重音，MD 一致忠实保留；§8 Mpq→Mq 路线；MSRI 致谢、Lemma 6.2/Fontaine/Messing；Henniart、Oesterlé、Livné 重音正确；NSF/Vaughn Foundation）；Contents 全部 16 条节名与页码（1.Introduction 431/The Main Theorem 431/Summary 433/2.Picard-Lefschetz 435/Admissible Curves 437/3. 438/X 443/Old and new 446/Φ 448/X_0(pqM) 451/4. 456/5. 465/6. 469/A variant 471/7. 471/8. 473）✓ 与印刷逐条一致。
- 结果：PASS。

## p.006（PDF p.6 / 印刷 p.435）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:28 -0400。
- PNG：`audit/ribet1990_p006.png`（pngmono，150 dpi）；仲裁裁片：`audit/300dpi/ribet1990_p006_suppose.png`、`audit/300dpi/ribet1990_p006_bullets.png`、`audit/300dpi/ribet1990_p006_foreach.png`（pnggray，300 dpi）。
- 核对：§2 节标题；¶1（p-adic 域 K/剩余域 k/P=Pic⁰(C)/[24],[11] §12,[18] 附录）；P⁰≈Pic⁰(𝒞_k)（(12.1.12)）；半阿贝尔扩张与归一化 surjection（[EGA IV], 21.8.5）；对偶图三要点；Proposition 2.1（cf. [11], (12.3.7)）T ≈ H¹(𝒢, Z) ⊗ G_m；X ≈ H₁(𝒢, Z)；段尾接下页 ✓。
- 发现并当场修复（Fraktur 拍平/误植，均为记号级内容错误；依据 300 dpi 裁片与 150 dpi 页图）：①L156 "C is the regular minimal model of C"→"𝒞 is the regular minimal model of C"，同行 C_k→𝒞_k；②L164 曲线 𝒞_k 两处、𝒟_j、映射 ∪𝒟_j→𝒞_k；③L167 行间公式 Pic⁰(D_j)→Pic⁰(𝒟_j)；④L172 对偶图 G→𝒢、C_k→𝒞_k；⑤L176/178/200 奇异点集合 \mathcal{I}→𝒮（300 dpi 确证印刷为花体 S）；⑥L194 bouquet G→𝒢̄、G→𝒢、映射 G→G→𝒢→𝒢̄；⑦L200 边所属 G→𝒢。
- 印刷原文 quirk：归一化映射印刷即为 "∪ 𝒟_j"（用 ∪ 表不相交并），MD 原有 \cup 忠实保留，不改为 ⨿/⊔。
- 备注：P_k、P⁰ 印刷为粗斜体，MD 拍平为普通斜体（字母正确，排版级，登记不改）；𝒞_k 在 L161 作 \mathcal{C}_k、L167 作 \mathscr{C}_k，为 mineru 既有混排（均指同一花体字形，不误导，保留现状）。
- 结果：FAIL（8 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.007（PDF p.7 / 印刷 p.436）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:35 -0400。
- PNG：`audit/ribet1990_p007.png`（pngmono，150 dpi）。
- 核对：H₁(𝒢̄, Z) ≈ Z^𝒮；非典范包含 X ⊂ Z^𝒮（式 (1)）；度映射 Z^𝒯 → Z；Proposition 2.2（α: Z^𝒮 → D，α(i)=j₁(i)−j₂(i)，[11] §12.4）；Φ=连通分支群、Albanese、monodromy pairing (11.5.2b)、Y → X*、Φ ≈ coker(u) [loc. cit.]；Picard-Lefschetz 公式引入与 Θ-polarization P ≈ Alb(C)；Theorem 2.3 陈述与 Proof（Théorème 12.5 of [11]，□）✓。
- 发现并当场修复（均据 150 dpi 页图，上标集合字形 𝒮 与 p.006 300 dpi 裁片同款花体 S）：①L202 𝒢̄ 拍平为 $\bar{G}$；②L205/211/214/223 四处上标 \mathcal{I}→\mathcal{S}；③L254 "edges of G"→𝒢、"$Z^{J}$"→$\mathbf{Z}^{\mathcal{S}}$；④L256 Theorem 2.3 三处 "$Z^{I}$"→$\mathbf{Z}^{\mathcal{S}}$。
- 备注：Proposition 2.2 前后印刷 D 为粗斜体、正文 X/Y/P/Φ 斜粗体拍平为普通体（字母与结构正确，排版级，登记不改）。
- 结果：FAIL（7 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.008（PDF p.8 / 印刷 p.437）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:45 -0400。
- PNG：`audit/ribet1990_p008.png`（pngmono，150 dpi）；仲裁裁片：`/tmp` 核验后未引用（"kernel is the group X" 无上杠、𝒮̃/𝒯̃ 字形，与 p.006 裁片同款花体）。
- 核对：节标题 "Admissible curves"（印刷斜体小写 c，MD 一致）；admissible curve/Jordan-Livné [13] §3；e(i) 链替换与 P¹；surjection 𝒮̃→𝒮；τ: Z^𝒮→Z^𝒮̃；Z^𝒯→Z^𝒯̃；ι: D→D̃；α̃ kernel=X（300 dpi 确证无杠）；四图交换方 α,α̃,ι,τ；蛇图引理论证；段尾 "we can continue to" 接下页 ✓。
- 发现并当场修复（记号级；依据 150 dpi 页图 + 300 dpi 裁片）：①L262 三处 \mathcal{I}→\mathcal{S}（sets 𝒮/𝒯、i∈𝒮 ×2）；②L264 "$C_k$"→$\mathcal{C}_k$、"sets I and T"→$\mathcal{S}$/$\mathcal{T}$、"$\tilde I/\tilde T$"→$\tilde{\mathcal{S}}/\tilde{\mathcal{T}}$；③L267 行间式 𝒮̃→𝒮；④L273 τ 式上下标；⑤L276 i∈𝒮、𝒮̃、"set T"、𝒯̃；⑥L282 "$Z^T$"→$\mathbf{Z}^{\mathcal{T}}$；⑦L290/292 两处 sets 𝒮̃/𝒯̃；⑧L295 交换图 (2) 上/下行 Z 上标 \mathcal{I}→\mathcal{S}、\tilde{\mathcal{I}}→\tilde{\mathcal{S}}。
- 备注：D、D̃、P_k 等印刷粗斜体拍平（字母正确，登记不改）；印刷 ∪ 记号沿用前页 quirk。
- 结果：FAIL（10 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.009（PDF p.9 / 印刷 p.438）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 14:55 -0400。
- PNG：`audit/ribet1990_p009.png`（pngmono，150 dpi）；仲裁裁片（/tmp 核验，未引用存档）：同款花体 S 上标、"map y" 字形、"cokernel of γ" 字形（与 p.006 300 dpi 裁片同款花体）。
- 核对：同伦图替换注；Φ=coker(y: Y→Hom(Y,Z))、对角矩阵 e(i) 配对、[11] 12.10.1；Theorem 2.4（θ: D→Φ，Hom(Z^𝒮,Z)/Z^𝒮 ≈ ⊕(Z/e(i)Z)）；Proof（γ、Y^⊥、Φ ≈ Hom(Z^𝒮,Z)/(Y^⊥⊕Y)、Φ₀=Z^𝒮/(M⊕Y)、M=Y^⊥∩Z^𝒮、□）；Remark 2.5（Jordan-Livné [14]、prime-to-6、(2.4)、Theorem 4.3）；节标题 "3. Quaternions and modular curves" 与首段（X₀(qM)，段尾接下页）✓。
- 发现并当场修复（13 个 \mathcal{I}/C_k 上标与记号点，依据 150 dpi 页图 + 300 dpi 同款花体确证）：①L300 𝒞_k ×2；②L302 Z^𝒮 ×3；③L304 Theorem 2.4 Z^𝒮 ×2 + over 𝒮；④L309/315/321/327 四个行间式 Z^𝒮；⑤L312 "linear forms on $Z^I$"→Z^𝒮；⑥L318 Hom(Z^𝒮,Z)；⑦L330 Z^𝒮 ×4。
- 印刷原文 quirk：正文称 "the map y: Y → Hom(Y, Z)"（斜体 y），同页 Proof 却作 "cokernel of γ"——印刷自身记号不一致；MD 两处各按印刷保留（y 与 γ），不统一。
- 备注：M、Y、D 等印刷粗斜体拍平（字母正确，登记不改）。
- 结果：FAIL（13 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。
