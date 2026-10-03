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

## p.010（PDF p.10 / 印刷 p.439）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 15:05 -0400。
- PNG：`audit/ribet1990_p010.png`（pngmono，150 dpi）；仲裁裁片：`audit/300dpi/ribet1990_p010_curves.png`（pnggray，300 dpi）。
- 核对：§3 续段（𝒞 over Z_q、Deligne-Rapoport [4]/Katz-Mazur [15]、𝒞_Fq 两分支在超奇异点粘合、Frobenius 变换 x^(q)、(loc. cit. 1.18)、𝒯 两元素、𝒮=Σ(M)、j₁(i),j₂(i) 定向、𝒢 两顶点、(2.2) 特化）；Proposition 3.1（C=X₀(Mq)，印刷此处 Mq 与前文 qM 拼排不一，MD 忠实保留）；enhanced elliptic curves 段（H=(End E)⊗_Z Q、End(E) 极大序、End(E) Eichler 序、λ: E→E/B、σ↦λ⁻¹σλ）；oriented/ordered Eichler order 段；Aut 群阶整除 24、{±1}、([4], VI, Th. 6.9)、e(i)=#(Aut E)/2；Proposition 3.2（θ(D)、exponent dividing 12）；[(3.12)–(3.14)] ✓。
- 发现并当场修复：L338 三处 \\mathcal{I}→\\mathcal{S}（"The set 𝒮 is the set Σ(M)"、"For each i∈𝒮"、"we orient the i∈𝒮"），依据 150 dpi 页图（花体 S 与 p.006 300 dpi 裁片同款）。
- 印刷 quirk 登记：300 dpi 裁片确证 "enhanced elliptic curves." 引号内句号存在，MD 一致（150 dpi 初判误读，无修复）。
- 备注：enhanced 曲线粗体 **E** 与椭圆曲线斜体 E 的粗体区分在 "curve E"/"For each E"/"Q-algebra" 处拍平（字母不变，登记不改）；oriented/ordered 斜体拍平同前例。
- 结果：FAIL（3 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.011（PDF p.11 / 印刷 p.440）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 15:12 -0400。
- PNG：`audit/ribet1990_p011.png`（pngmono，150 dpi）；仲裁裁片：`audit/300dpi/ribet1990_p011_phi.png`（pnggray，300 dpi）。
- 核对：𝒮=Σ(M) 与 Deuring [6]（M=1 情形）；T(E)=T_q(E)×∏_{l≠q}T_l(E)；Dieudonné 模、T_q(E)=M(E(q))^t、[23] §3/3.6；enhanced 结构 B⊂T(E)/MT(E)；R=End(E₀)、H=R⊗_Z Q；adelization R_f/H_f/Ẑ；λ∈Hom(E,E₀)⊗_Z Q、V(E₀)、g∈H_f*/R_f*、gT(E)=T(E₀)、g: T(E)/MT(E)≈T(E₀)/MT(E₀)；H*\\H_f*/R_f*；Proposition 3.3（φ_{E₀}，300 dpi 确证粗体小写 φ，MD \\phi 正确）；[22]/[2] §11；Variant 3.4（right ideal classes）；[41], p. 87 ✓。
- 发现并当场修复：L362 一处 \\mathcal{I}→\\mathcal{S}（"the set 𝒮=Σ(M)"），依据 150 dpi 页图（同款花体 S）。
- 备注：\\bar{F}_q、E₀、(E₀,B₀) 等处印刷粗体拍平为普通体（字母不变，登记不改）；Variant/Proposition 标签斜体拍平同前例。
- 结果：FAIL（1 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.012（PDF p.12 / 印刷 p.441）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 15:20 -0400。
- PNG：`audit/ribet1990_p012.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi：括号句 "E≈E′" 粗体、Proof "curve E₀" 粗体、"End(E) to B" 粗体核验；引用判读后未存档）。
- 核对：Remarks 3.5a（E↦Hom(E₀,E)、"(isomorphism classes of enhanced elliptic curves) → (ideal classes)"、Serre [32]）；g⁻¹T(E)=T(E₀) 替代式；Remarks 3.5b（Frobenius 对合 x↦x^(q)、H_f^* 右乘、[22] Theorem 5、R-理想 I′⊂I 指标 q²）；Proposition 3.6 [cf. [42], Theorem 4.5]（S=B∩B′ Eichler 序、κ: (S,B)≈(End(E),End(E))、(E^(q),κ^(q)）；方括号同构定义（ι: End(E)≈End(E′)、κ′ι=κ）；Proof 开头（R=End(E₀)、A=End(E₀)、H=R⊗Q；B⊗Q≈H；κ_λ=λeλ⁻¹、Skolem-Noether）✓。
- 发现并当场修复（粗体 enhanced 对象拍平，字母身份级记号）：①L434 "$E\approx E^{\prime}$"→"$\mathbf{E}\approx\mathbf{E}^{\prime}$"（300 dpi 确证印刷粗体）；②L436 "curve $E_{0}$"→"$\mathbf{E}_{0}$"（300 dpi 确证粗体）。
- 备注：For each **E**、endomorphisms of **E**₀、(E₀,B₀) 等其余粗体拍平处字母不变，登记不改；L444 两处 End(**E**) MD 本即粗体正确（300 dpi 核验）；Hom(E,E₀) 内 E₀ 印刷斜体、MD 一致。
- 结果：FAIL（2 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.013（PDF p.13 / 印刷 p.442）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 15:28 -0400。
- PNG：`audit/ribet1990_p013.png`（pngmono，150 dpi）；仲裁裁片：`audit/300dpi/ribet1990_p013_endE.png`（pnggray，300 dpi）。
- 核对：λ′ 配对同构判据（ι: E→E′、λ′ι、[42] Prop. 3.4）；(E,λ)↦T(E)⊂V(E₀)；H_f*/(R_f*Q*) 与 pairs (E,κ)；gA_fg⁻¹=B_f、gR_fg⁻¹=S_f；局部素点分析（l=q：Lemme 1.5 p. 34、两类、除以 Q_q* 对应 Z/2Z；l 与 qM 互素：M(2,Q_l)、Th. 2.3 p. 38、normalizer）；l|M：Eichler 序 R_l/S_l、A′=End(E′)、树 Δ 与 [33] Ch. II、Elementary Divisor Theorem、Z_le₁⊕lⁿZ_le₂；h⁻¹g∈N(A_l)∩N(B_l)=R_l*Q_l*；全局两类被 Frobenius 交换、Remark 3.5b、□ ✓。
- 发现并当场修复（粗体 enhanced 对象 End(**E**) 拍平，2 处；300 dpi 裁片 ribet1990_p013_endE.png 确证印刷为 End(**E**) (resp. End(E)) / End(**E**) to R and End(E) to A）：L456 "The image of End(E) (resp. End(E))"→"End(𝐄) (resp. End(𝐸))"；"maps End(E) to R and End(E) to A"→"End(𝐄) to R and End(𝐸) to A"。
- 结果：FAIL（2 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.014（PDF p.14 / 印刷 p.443）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 15:38 -0400。
- PNG：`audit/ribet1990_p014.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi：页中斜体 T 与页末正体 T 对比核验，未存档）。
- 核对：h⁻¹g∈N(A_l)∩N(B_l) 链式等式；两类被 Frobenius 交换、Remark 3.5b、□；节标题 "Action of Hecke operators on X"（印刷斜体 run-in，MD 一致）；Hecke 对应定义（[39] Chapter 7、Δ′、det(α)=n、X_SS(α)、page 183）；"modular" 定义（(7.2.4)、Proposition 3.36 of [39]、rational field Q）；J₀(N) 的 two ways（Albanese/Pic）；抽象对应框架（U×V、f/g 投影、A_X/A_U/A_V、f_*,g_*,f*,g*、ξ: A_U→A_V、T: A_V→A_U、[39] §7.2）；φ: U→V 特例段尾 "refer to ξ and T as" 接下页 ✓。
- 印刷 quirk 登记：页末 "refer to ξ and T as" 的 T 印刷为正体（同页它处均斜体 T；300 dpi 对比确证）；MD 该句恰为正体 T，与印刷一致，不修改。
- 备注："in *two* ways" 斜体拍平（登记不改）。
- 结果：PASS。

## p.015（PDF p.15 / 印刷 p.444）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 15:45 -0400。
- PNG：`audit/ribet1990_p015.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："Prop. 3.54, of [39]" 逗号确证，未存档）。
- 核对：Albanese/Pic maps 段；auto-dual 与 Rosati 对合；T(n)/ξ_n/[39] Chapter 7；式 (3) T_n=ξ_n*、T_n*=ξ_n（Rosati）；Atkin-Lehner w=w_N、X_SS(τ)、[39] §7.5；式 (4) wT_nw=ξ_n、wξ_nw=T_n；page 193 恒等式与 Prop. 3.54（印刷即带逗号 "3.54, of"）；子代数 Ξ=Ξ_N 与 **T**=**T**_N（MD 粗体保留正确）、Ξ≈**T**、S₂(Γ₀(N))、T_n*、faithful/cotangent、free Z-module rank、Th. 3.45；段尾 "Consider now the special situation where" 接下页 ✓。
- 备注：L518 "defined over Q" 印刷粗体 **Q**，MD 正体 Q（字母不变，登记不改）。
- 结果：PASS。

## p.016（PDF p.16 / 印刷 p.445）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 15:55 -0400。
- PNG：`audit/ribet1990_p016.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi：Σ 下标 "C≠D" 确证、"where **E**/C" 粗体+斜体 E/C 对比、"fact that T" 斜体放大、"defined over **Q**" 粗体，未存档）。
- 核对：N=qM、toric part T、X≈H₁(𝒢, Z)（(2.1)）、inclusion (1)；n 与 q 互素情形无 inversion；T_r(E)=Σ_C E/C 与 T_r(E)=Σ_{C≠D} E/C（下标 300 dpi 确证 ≠）；w_q 三重结构 (E, C_M, C_q) 与 (E/C_q, (C_M⊕C_q)/C_q, E[q]/C_q)；w_q 于 J₀(N)/Néron 模/特征 q 纤维；[1] Th. 3、q-new、(3.10)；Proposition 3.7（w_q=−T_q on torus T）；Proof：degeneracy maps α, β（cf. [19]）、w_q+T_q=α*β_*、β_*: J₀(N)→J₀(M)、T→J₀(M)_Fq、torus 消没、□ ✓。
- 发现并当场修复：①L526 三处 \\mathcal{I}→\\mathcal{S}（𝒮=Σ(M)、Z^𝒮、i∈𝒮）；②L536 首个 "E/C"→"$\mathbf{E}/C$"（300 dpi 带状裁片确证印刷首个粗体、第二个斜体）。
- 印刷 quirk 登记：L548 "the fact that *T* pertains" 印刷为斜体 T（与 p.015 子代数粗体 **T** 为印刷自身不一致；300 dpi 放大确证斜体），MD 正体 T 恰与印刷一致，不改。
- 备注：L548/552 "over Q" 印刷粗体 **Q**，MD 正体（登记不改）；其余与本页逐项吻合。
- 结果：FAIL（4 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.017（PDF p.17 / 印刷 p.446）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 16:05 -0400。
- PNG：`audit/ribet1990_p017.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："T-stable" 粗体 **T**、"images of **T**"、"**T**₀ and **T**₁ are the *q-old* and *q-new* quotients of **T**" 全行确证，未存档）。
- 核对：Proposition 3.8 (i)/(ii)（w_q 置换两分支、Frobenius x↦x^(q)、Z^Σ(M)、 restriction=Frobenius）与 Proof（[4] Ch. V §1、(3.7)、𝒢 两顶点反转、X₀(qM)_Fq 有理、[18] Appendix §3、□）；节标题 "Old and new"；**T**=**T**_{M_q} 定义（cotangent space S、S₂(Γ₀(Mq))、[39] Th. 3.45）；q-old subspace（cf. [1]）；S₀=α*(S₂(Γ₀(M)))⊕β*(S₂(Γ₀(M)))；Petersson 正交补 S₁；**T**-stable、**T**₀/**T**₁ images、q-old/q-new quotients；积映射 **T**→**T**₀×**T**₁ finite index；特征 q 纤维 F_q-group、Φ、J、Raynaud [24]/Deligne-Rapoport [4]；正合列 (5) 1→T→J⁰→J₀(M)×J₀(M)→0 ✓。
- 发现并当场修复：①L560 "\\mathcal{I}"→"\\mathcal{S}"（singular points 集，150 dpi 页图，同款花体 S）；②L574 四处 Hecke 代数粗体拍平："T-stable"→"$\mathbf{T}$-stable"、"let $T_0$ and $T_1$"→"$\mathbf{T}_0$/$\mathbf{T}_1$"、"images of T"→"$\mathbf{T}$"、"quotients of T"→"$\mathbf{T}$"（300 dpi 裁片确证全行粗体；MD 下一行显示式本为 \mathbf，修复后页内一致）。
- 备注：J₀(Mq)_C 的下标 C、F_q-group 的 F 印刷粗体，MD 正体（字母不变，登记不改）。
- 结果：FAIL（5 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.018（PDF p.18 / 印刷 p.447）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 16:18 -0400。
- PNG：`audit/ribet1990_p018.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："Hom(X, **G**_m)" 下标正体 m、"T_q∈**T**_M" 粗体、"End_**Q**(Q)" 下标粗体、"t∈**T** … **T**₁" 粗体，未存档）。
- 核对：T=Hom(X, G_m)、(5) 作用分解、ω: J⁰→J₀(M)×J₀(M) 由 Pic 函子性、与 Albanese 函子性退化映射之区分、X₀(M)⇉X₀(Mq) 仅特征 q；Remark 3.9（ρ: J₀(M)×J₀(M)→J₀(Mq)、kernel [28]、ρξ=T_qρ、(x,y)↦(τx+qy,−x)、τ=q-th Hecke、(3.19)）；Theorem 3.10（**T** 作用切出 q-new 商 **T**₁）；Proof（A=im ρ、Q=coker ρ、[19]、0→A→J₀(Mq)→Q→0 对偶、cotangent over C、0→S₀→S→S₁→0、End_Q(Q) faithful、toric reduction）✓。
- 发现并当场修复（粗体 Hecke 代数 **T** 拍平 5 处 + 字形误植 1 处；均据 300 dpi 裁片）：①L588 "$\mathbf{G}_{\mathfrak{m}}$"→"$\mathbf{G}_{\mathrm{m}}$"（印刷下标为正体 m；与 MD p.006 处 G_m 渲染一致）；②L588 "The action of T on T corresponds to the action of T on X"→两处 $\mathbf{T}$；③L588 "The action of T on J₀(M)×J₀(M)"→$\mathbf{T}$；④L588 "$T_q\in T_M$"→"$T_q\in\mathbf{T}_M$"；⑤L620 "$t\in T$ maps to 0 in $T_1$"→"$t\in\mathbf{T}$ / $\mathbf{T}_1$"。
- 备注："defined over Q" 印刷粗体 **Q**，MD 正体（登记不改）；End_**Q** 下标 MD 本即粗体正确。
- 结果：FAIL（6 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.019（PDF p.19 / 印刷 p.448）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 16:30 -0400。
- PNG：`audit/ribet1990_p019.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："**T**-equivariant"、"as a **T**-module"、"Let **Λ** … set **𝒮** … X⊂**Λ**"、"**Φ**≈coker(*ι*)"，未存档）。
- 核对：π: J₀(Mq)→Q 诱导 J⁰→U、π_*η_* 等距、Theorem 3.10 Proof 结尾（□）；Theorem 3.11（**T**-module via (5)、t is 0 in **T**₀）与 Proof（similar to (3.10)、A→J⁰、(5) 复合等距、□）；节标题 "Action of Hecke operators on Φ"；Eisenstein 性（T_r 乘 1+r、[30]/[8]）；Λ/𝒮/X⊂Λ/degree 0、e(i) 对角配对；κ: Λ→Λ*、ι: X→X*；Φ≈coker(ι)（300 dpi 确证为 ι 非 t）；T_n 作用 target/source 之别、ξ_n=w_{qM}T_nw_{qM}；段尾 "because the source" 接下页 ✓。
- 发现并当场修复：①L622 "T-equivariant"→"$\mathbf{T}$-equivariant"（粗体代数拍平，300 dpi 确证）；②L624 "as a T-module"→"as a $\mathbf{T}$-module"（同）；③L632 六处字母/花体：A→Λ ×3（free abelian group、X⊂Λ、subgroup of Λ、pairing on A）、S→𝒮 ×3（supersingular points 集、Note that、i∈𝒮）（300 dpi 确证印刷为 Λ 与花体 S，MD 误作普通 A/S）；④L649 行间式 "coker(t)"→"coker(ι)"（300 dpi 确证印刷为 ι；MD 误作拉丁 t，字母身份错误）。
- 备注：F_q、F̄_q 印刷粗体，MD 正体（登记不改）；两处证明结束符 □ 未收录（惯例）。
- 结果：FAIL（10 处记号/字母错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.020（PDF p.20 / 印刷 p.449）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 16:40 -0400。
- PNG：`audit/ribet1990_p020.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："variety **to** X₀(qM)" 用词确证，未存档）。
- 核对：ι/Θ-polarization/ξ_n 段；T_r=ξ_r、η_r=T_r−(1+r)；Theorem 3.12（Φ annihilated by η_r, (r,qM)=1）与 Theorem 3.22 预告；E↦Σ_H E/H（(r+1) 子群、evident enhancement）；ι/κ 与 T_r 作用交换（T_r=ξ_r）；Φ=X*/X；η_r(X*)⊂X；式 (6) η_r(Λ*)⊂Λ 与式 (7) η_r(Λ*)⊂X；e=(Λ*:Λ) 挠性论证、Λ/X≅Z；基 {i*} 对偶于 𝒮={i}；1/e(i) i·η_r(j)=1/e(i) j·η_r(i)；段尾接下页 ✓。
- 发现并当场修复：①L674 首个 "(The quotient E/H"→"$\mathbf{E}/H$"（印刷粗体 enhanced 商，与后文斜体 E/H 对照，150 dpi 页图）；②L698 两处 "$\mathcal{I}$"→"$\mathcal{S}$"（"basis 𝒮={i}"、"for each j∈𝒮"，150 dpi 页图同款花体 S）。
- 印刷原文 quirk：L654 印刷即 "the reduction of the Albanese variety **to** X₀(qM)"（语义预期为 of；300 dpi 确证 to 为印刷原样），MD 忠实保留不改。
- 结果：FAIL（3 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.021（PDF p.21 / 印刷 p.450）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 16:48 -0400。
- PNG：`audit/ribet1990_p021.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："**E**/*H*≈**F**" 粗体、"α∈Aut(**E**)"、"α∈{±1}"（带 1），未存档）。
- 核对：η_r-等变性、λ=η_r(i)/e(i) 整除论证；E=(E,B)、F=(F,C)、e=e(i)=card(A)、Aut(E)/{±}（印刷 {±} 无 1，MD 忠实；后文 {±1} 带 1，MD 亦忠实）；E/H≈F 整除命题；A 自由作用、α 阶 3/4/6、虚二次域；R=End(E) 由 α 生成、Gaussian integers、Q(√−3)、R/rR-模 E[r]、ideal ℘=(π)、π′=r/π、E/H≈E 矛盾；Remark 3.13（Brandt matrix、i-th column）；Proposition 3.14（η_r: Λ*→X、Φ→X/η_rX）；Φ=X*/X=Λ*/(X⊕X^⊥)、σ、Weil Riemann Hypothesis、η_r 等距；段尾行间式 η_r: Λ*→X ✓。
- 发现并当场修复：L714 "$E/H \approx F$"→"$\mathbf{E}/H \approx \mathbf{F}$"（粗体 enhanced 对象拍平；300 dpi 裁片确证）。
- 结果：FAIL（1 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.022（PDF p.22 / 印刷 p.451）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 16:58 -0400。
- PNG：`audit/ribet1990_p022.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："where **E**₁ and **E**₂"、"Lemma 3.16 Let **E** … of **E** … of *E*"、"For x∈*I*"，未存档）。
- 核对：σ 单射性结尾（□）；节标题 "Comparison with X₀(pqM)"；L 与 pM、proposition (3.1)、p-isogenies E₁→E₂；α,β: X₀(pqM)⇉X₀(qM)、α_*,β_*: L⇒X、[E₁→E₂]↦E₁ 或 E₂；δ: L→(X⊕X)；Theorem 3.15（δ surjective）；Lemma 3.16（odd power of p）与 Proof（reduced norm、R[p⁻¹]、[41] Cor. 5.9 p.90/Th. 4.1 p.80、□）；Lemma 3.17（isogeny、degree a power of p）与 Proof 开头（T=Hom(E₁,E₂)、[T: xR]）✓。
- 发现并当场修复：①L752 "$E_1$ and $E_2$"→"$\mathbf{E}_1$ and $\mathbf{E}_2$"（粗体 enhanced，300 dpi 确证）；②L770 Lemma 3.16 两处："Let E"→"$\mathbf{E}$"、"endomorphism of E"→"$\mathbf{E}$"（括号内 "as an endomorphism of E" 印刷斜体，MD 保留）。
- 印刷原文 quirk：L782 印刷即 "For x ∈ *I*, x ≠ 0"（语义预期为 x∈T；300 dpi 确证 I 为印刷原样），MD 忠实保留不改。
- 备注：F_q 印刷粗体，MD 正体（登记不改）。
- 结果：FAIL（3 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.023（PDF p.23 / 印刷 p.452）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 17:08 -0400。
- PNG：`audit/ribet1990_p023.png`（pngmono，150 dpi）。
- 核对：Lemma 3.17 收尾（Z[p⁻¹]、[41] Th. 5.7 p.89、□）；Theorem 3.15 证明（(E−E′,0)/(0,E−E′)、even power p^{2i}、π_j/θ_j 因子分解、λ=π₀−θ₁+…−θ_{2i−1}、δ(λ) 与 λ′）；Remark 3.18（Ron Livné、Bas Edixhoven）；τ 与 T_p 之区分（p-th Hecke、w_p 相对 divisor p）；正合列 0→Y→L→X⊕X→0；Theorem 3.19（T_p=−w_p on Y、(x,y)↦(τ(x)−y, px)）；αw_p=β、βw_p=α；T_p+w_p 经 α_*/β^* 分解、vanishes on Y；p+1=α_*α*=β_*β*、τ=β_*α*=α_*β*（上下标正确）；(τx,(p+1)x)、 Subtracting w_p、□ ✓ 全部与印刷一致。
- 备注：E/E′ 全页粗体 enhanced 记号 MD 保留正确（块二修复后惯例稳定）；"even" 斜体拍平（登记不改）；□ 惯例不收录。
- 结果：PASS。

## p.024（PDF p.24 / 印刷 p.453）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 17:18 -0400。
- PNG：`audit/ribet1990_p024.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi：首段 "**T**=**T**_{Mpq}/…quotients of **T**/**T̄** of **T**" 粗体全行确证，未存档）。
- 核对：**T**=**T**_{Mpq}、q-old/q-new quotients of **T**_{Mq}、pq-new quotient **T̄**；S=S₂(Γ₀(Mpq)) 与两个直和子空间；S_{pq-old}/S_{pq-new}（Petersson）；**T**-stable、**T̄**=image of **T** in End(S_{pq-new})；Theorem 3.20（**T**-module Y cuts out **T̄**）与 Proof（R=pq-new quotient、退化映射、purely toric、V=(R_{F_q})⁰、Hom(L,G_m)/Hom(X,G_m)、λ、dim(L)/dim(X)/dim(Y) 三组公式、四 copies of S₂(Γ₀(M))、λη isogeny、□）✓。
- 发现并当场修复：①L828 五处 Hecke 代数粗体拍平（**T**=**T**_{Mpq}、**T**_{Mq}、quotients of **T**、**T̄** of **T**）；②L840 四处（**T**-stable、**T̄**、quotient of **T**、image of **T**）；③L842 四处（**T**-module、**T̄** of **T**、element t of **T**、0 in **T̄**）；④L844 两处（t∈**T**、0 in **T̄**）；⑤L852 四处 "$\mathbf{G}_{\mathfrak{m}}$"→"$\mathbf{G}_{\mathrm{m}}$"（印刷下标正体 m，同 p.018 仲裁）；⑥L868 一处同款 G_m。共 20 个记号点（300 dpi 裁片 + p.017/018 同款花体先例）。
- 结果：FAIL（20 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.025（PDF p.25 / 印刷 p.454）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 17:28 -0400。
- PNG：`audit/ribet1990_p025.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："quotient **T**_{q-new/p-old}" 粗体确证，未存档）。
- 核对：q-new/p-old quotient 定义（S_{q-new}∩S_{p-old}）；Theorem 3.21（Hecke algebra **T** acts through **T**_{q-new/p-old} faithfully，MD 粗体本就正确）与 Proof（□ 惯例不录）；J₀(Mq)_Fq 的 Φ 与 Θ；退化映射 J₀(Mq)×J₀(Mq)→J₀(Mpq)；θ: Φ×Φ→Θ；正合列 (8) 0→K→Φ×Φ→Θ→C→0；Theorem 3.22（antidiagonal embedding f↦(f,−f)）；μ 公式 (x,y)↦((p+1)x+τy, τx+(p+1)y)、τ=p-th Hecke、η_p；Φ=X*/X、Θ=L*/L、pairing ι；θ 由 δ 的对偶与 σ: (X⊕X)→L 诱导；X₀(pqM)⇉X₀(qM)；段尾 "is the endomorphism of" 接下页 ✓。
- 发现并当场修复：L870 两处 Hecke 代数粗体拍平（"quotient of T"→"$\mathbf{T}$"、"$T_{q-new/p-old}$"→"$\mathbf{T}_{q\text{-new}/p\text{-old}}$"；300 dpi 确证；与 L872 Theorem 3.21 既有 \mathbf 写法对齐）。
- 备注：页界跨越——MD L912 前半（"X⊕X given by the 2×2 matrix…"）属印刷 p.454 末至 p.455 首的跨页句，其矩阵部分留待 p.026 核验。
- 结果：FAIL（2 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.026（PDF p.26 / 印刷 p.455）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 17:38 -0400。
- PNG：`audit/ribet1990_p026.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："two **T**-module structures"、"T_n∈**T**"、"isomorphic **T**-modules"、"call'these" 排印杂符，未存档）。
- 核对：跨页句收尾（2×2 矩阵 μ=((p+1,τ),(τ,p+1))、Y→Y*）；Proposition 3.23（0→K→(X⊕X)/μ(X⊕X)→Y*/Y→C→0）与 Proof（交换图 L/Y→L*/Y→Θ、σ/δ*/θ、snake lemma、4-term、□）；Remark 3.24（Hecke compatible、p-th Hecke on J₀(qM)² 非 τ 诱导、Picard/Albanese 双作用、T_n 与 ξ_n、 intertwining w=w_{pqM}）；T=(T_n)*=Hom(T_n, id)；T-模结构同构段；w_{qM}∈Aut(X) 与 (x,y)↦(y,x) 复合 ✓。
- 发现并当场修复：①L928 四处 Hecke 代数粗体拍平（"two T-module structures"→"$\mathbf{T}$-module"、"$T_n\in T$"→"$T_n\in\mathbf{T}$"、"These two T-module structures"→"$\mathbf{T}$-module"、"isomorphic T-modules"→"$\mathbf{T}$-modules"）；②L930 两处（"sequence of T-modules"→"$\mathbf{T}$-modules"、"provided that T acts"→"$\mathbf{T}$ acts"）；③L932 两处（"$\mathbf{T}$-module structures"、"$\mathbf{T}$-modules"）。均据 300 dpi 裁片。
- 印刷原文 quirk：Remark 3.24 印刷 "call'these"（call 后有排印杂符撇号），MD 规范化为 "call these"（噪点级，登记不改）。
- 结果：FAIL（8 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.027（PDF p.27 / 印刷 p.456）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 17:50 -0400。
- PNG：`audit/ribet1990_p027.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："Picard **T**-module"、"A model **𝒞** for C"，未存档）。
- 核对：Remark 3.24 收尾；Proposition 3.25（γ=(T_p)²−1∈**T**、μ(X⊕X)=γ(X⊕X)、λ=(x,y)↦(−x,τx−y)、γ=μλ、□）；节标题 "4. Bad reduction of Shimura curves"；Cerednik-Drinfeld ([3],[7] §4)、[13,14,16]、Jacquet-Langlands、GL₂、[29]；Jordan-Livné 预告；B/𝒪/Γ_∞/M(2,R)/SL(2,R)/H/Γ_∞\H/J=Pic⁰(C)；C_{Q_p}、J_{Q_p}、模型 𝒞（Cerednik [3]/Drinfeld [7]）、purely toric、Z、Ψ=Z*/Z；T̃=Z[...T_n...] 双作用（standard/Albanese）；Theorem 4.1（T̃-isomorphism Z≈Y、bilinear pairing）与 adjoint 论证；T̄ 与 S_{pq-new}；Corollary 4.2（**T̄**→End(J) 注入）；trace_{T/Z}(T_n)；Theorem 4.3（0→K→(X⊕X)/γ(X⊕X)→Ψ→C→0）；Cerednik-Drinfeld 定理模型（GL(2,Q_p)\(℘^unr×X)、K\H_f*/H*、Eichler order R⊂H）；段尾 "arising from R." 接下页 ✓。
- 发现并当场修复（12 个记号点；Hecke 代数粗体系列 + 花体模型 𝒞，依据 300 dpi 裁片与既有同款先例）：①L934 "Picard T-module"→"$\mathbf{T}$-module"；②L954 "A model C for C"→"A model $\mathcal{C}$ for C"（印刷花体 𝒞，§2 同一对象）；③L958 五处（"the T-modules"→"$\mathbf{T}$-modules"、"make T"→"$\mathbf{T}$"、"of $\tilde T$"→"$\tilde{\mathbf{T}}$"、"every T-module"→"$\mathbf{T}$-module"、"$\tilde T$-module"→"$\tilde{\mathbf{T}}$-module"）；④L964 三处（"$\bar T$"→"$\bar{\mathbf{T}}$"、"quotient of T cut out"×2→"$\mathbf{T}$"）；⑤L972 "sequence of T-modules"→"$\mathbf{T}$-modules"；⑥L980 "as a T-module"→"$\mathbf{T}$-module"。
- 备注：GL₂、Q_p/Z_p/F_p/F̄_p 等印刷粗体，MD 正体（weight 拍平，登记不改）；□ 惯例不录。
- 结果：FAIL（12 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.028（PDF p.28 / 印刷 p.457）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 18:00 -0400。
- PNG：`audit/ribet1990_p028.png`（pngmono，150 dpi）。
- 核对：本页内容为 T̃ 形式多项式环段、Theorem 4.1、Corollary 4.2、Theorem 4.3、Cerednik-Drinfeld 摘要与 GL(2,Q_p)\(℘^unr×X)——与 p.027 扫描页（印刷 p.456）后 2/3 完全相同；对应 MD 段 L956–988。逐项复对：**T̃**/**Z**[...T_n...]、**T̃**-isomorphism Z≈Y、End_**Q**(J) faithful、trace_{**T**/**Z**}(T_n)、γ=(T_p)²−1∈**T**、0→K→(X⊕X)/γ(X⊕X)→Ψ→C→0、**T̄** cut out by **T**、GL(2,**Q**_p)\(℘^unr×X)、K\H_**f***/H* ✓（本段记号修复已于 p.027 完成，本页复核一致）。
- 扫描件特性登记：PDF 的印刷 p.456 与 p.457 扫描页内容重叠重复（p.457 前 2/3 重摄 p.456 后 2/3）；MD（mineru 导出）仅含该内容一次（grep "formal polynomial ring"/"arising from R"/"The object of this" 各 1 处，L956/958），无重复输出、无缺文，忠实可用。
- 结果：PASS。

## p.029（PDF p.29 / 印刷 p.458）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 18:08 -0400。
- PNG：`audit/ribet1990_p029.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi：页尾 "different.-" 确证，未存档）。
- 核对：Apologies 段（X/K/C 三重记号辨析）；Cerednik-Drinfeld 定理中 R 与 End(E) 之类比（F̄_p、A、L⊂End(A)、D⊂A[M] 阶 M²、L⊗Z_p-同构 ι、"standard" formal module Φ、R=End_L(A)、End_L(A)∩End_L(A/D)）；R⊗Z_p≈M(2,Z_p)、H⊗Q_p≈M(2,Q_p)；空间 X（isomorphism classes、enhancement D′、T(A′) submodule of V(A)）；T(A′)=g⁻¹T(A)、g∈(H_f)*；GL(2,Q_p)⁺、v: GL(2,Q_p)→Z/2Z、v(γ)=ord_p(det γ) (mod 2)；对偶图 𝒢=GL(2,Q_p)⁺\(Δ×X)、tree Δ、SL(2)、[33] Ch II §1、Kurihara [16]、段尾 "not qualitatively different.-" ✓。
- 印刷原文 quirk：页尾印刷即为 "different.-"（句号后带排印杂符连字符；300 dpi 确证），MD 忠实保留。
- 备注：F̄_p、Z_p、Q_p、Φ 等印刷粗体，MD 正体（weight 拍平，登记不改）。
- 结果：PASS。

## p.030（PDF p.30 / 印刷 p.459）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 18:18 -0400。
- PNG：`audit/ribet1990_p030.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："M(2,**Z**)" 无 _p 下标、"PGL(2,**Z**_v)" 下标 v，均为印刷原样，未存档）。
- 核对：S⊂R Eichler order（M(2,Z_p) 显式矩阵集）；𝒱/ℰ（locally free rank-1 left R/S-modules）；𝒱=R_f*\H_f*/H*、ℰ=S_f*\H_f*/H*；α: ℰ→𝒱、β: ℰ→𝒱（Eichler order T、mRm⁻¹、diag(1,p)、(mR_f*m⁻¹)\H_f*/H*、m⁻¹ 平移）；Proposition 4.4（𝒢 边集=ℰ、顶点集=𝒱×{1,2}、(α(e),1)-(β(e),2)）与 Proof（strong approximation、𝒱_Δ=PGL(2,Q_p)/PGL(2,Z_v)=H_p*/R_p*Q*、两个 orbits、𝒱_{Δ+}=PGL(2,Q_p)⁺/PGL(2,Z_p)、GL(2,Z_p)\X=𝒱、𝒱_{Δ−} 补集、bijection 𝒱→GL(2,Q_p)⁺\(𝒱_{Δ−}×X)、m=diag(1,p)）✓。
- 发现并当场修复：①L1038 OCR 误植 "Eicher order"→"Eichler order"（印刷为 Eichler）；②L1044 两处 "Let V/let E"→"$\mathcal{V}$/$\mathcal{E}$"；③L1062 "from E to"→"from $\mathcal{E}$ to"；④L1072 两处 "vertices of G"→"$\mathcal{G}$"、"$V_{\Delta}$"→"$\mathcal{V}_{\Delta}$"；⑤L1078 "$V_{\Delta}$"→"$\mathcal{V}_{\Delta}$"；⑥L1090 三处 "$V_{\Delta-}/V_{\Delta+}/V_{\Delta}$"→"$\mathcal{V}_{\Delta-}/\mathcal{V}_{\Delta+}/\mathcal{V}_{\Delta}$"。均据 150 dpi 页图（花体同款）。
- 印刷原文 quirk：L1041 印刷即 "∈M(2,**Z**)"（漏 _p 下标；300 dpi 确证）与 L1075 "PGL(2,**Z**_v)"（下标 v 为印刷笔误，预期 p；300 dpi 确证）——MD 均忠实保留不改。
- 结果：FAIL（10 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.031（PDF p.31 / 印刷 p.460）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 18:28 -0400。
- PNG：`audit/ribet1990_p031.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："Let **W** be"（粗斜体无点）确证，未存档）。
- 核对：bijection 𝒱=GL(2,Z_p)\X→GL(2,Q_p)⁺\(𝒱_{Δ−}×X)；𝒢 顶点=两 copies of 𝒱；ℰ_Δ=GL(2,Q_p)⁺/(S_p*Q*)、X→ℰ_Δ×X、S_p*\X；边 (1,x⁻¹)、顶点 (x,1)/(xm,1)→(1,x⁻¹)/(m,x⁻¹)、m⁻¹x⁻¹、□；ω: Z^ℰ→Z^𝒱×Z^𝒱、(4.4)、degree-0；Corollary 4.5（(Z^ℰ)₀→(Z^𝒱)₀×(Z^𝒱)₀、induced by (α,β)）；Cerednik-Drinfeld 模型 𝒞 的 pairing、o(e)、ẽ、Γ stabilizer、PGL(2,Q_p)；ℰ=S_f*\H_f*/H*；Proposition 4.6（o(e)=½card(Aut_S(W))）与 Proof（x=(x_v)、S_v·x_v、sx=xa、S_f* stabilizer）✓。
- 发现并当场修复（6 个记号点，依据 300 dpi 裁片）：①L1122 "$\dot{W}$"→"$\mathbf{W}$"——印刷为粗斜体 W、无点；MD 的点为 mineru 误植（字形身份错误），同时按印刷补粗体；②L1130 Aut_S(W)→Aut_S($\mathbf{W}$)；③L1132 "Take W"→"Take $\mathbf{W}$"、Aut_S(W)×3→Aut_S($\mathbf{W}$)（本页印刷 W 均粗体）。
- 备注：L1125 行间式与 L1134 的 f 下标（S_f*/H_f*）印刷粗体，MD 一处 \mathrm{f}、一处正体 f（weight/字形风格类，登记不改）；页界：L1134 段尾 "of x in" 接 p.032 "X = K\H_f*/H*..."。
- 结果：FAIL（6 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.032（PDF p.32 / 印刷 p.461）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 18:40 -0400。
- PNG：`audit/ribet1990_p032.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："Since R and **ℳ** agree"、"order of level p^{+1}"（加号上标）确证，未存档）。
- 核对：X=K\H_f*/H*、s_p x=κxa、κ/a 唯一性；Γ=Aut_S(W)、Γ∩Q_p*={±1}、prime-to-p 部分、a=±1、□；Z/Y 比较开篇（δ: L→X⊕X、Σ(Mp)/Σ(M)、(3.3)、End(E₀,C_p)=S、End(E₀)=R）；ℳ 引入（maximal order End_L(A)）；Proposition 4.7（κ: End(E₀)→ℳ、R↔End(E₀)、S↔End(E₀,C_p)）与 Proof（(3.6) output、B∩B′、C_p 构造、V_p/T_p Tate modules、Eichler order of level p^{+1}、U/pU、E[p]=T_p/pT_p、S⊗Z_p=End(E₀,C_p)⊗Z_p）✓。
- 发现并当场修复：①L1144 Aut_S(W)→Aut_S($\mathbf{W}$)（W 印刷粗体，p.031 同款）；②L1148 两处 "symbol M"/"orders of M"→"$\mathcal{M}$"（花体，300 dpi 确证）；③L1152 "B taken to be M"→"$\mathcal{M}$"；④L1158 "R and M agree"→"R and $\mathcal{M}$ agree"。
- 印刷原文 quirk：L1158 印刷即 "Eichler order of level p^{+1} (or "level 1," in this local context)"——上标为加号（数学预期 p⁻¹；300 dpi 放大确证 +1 为印刷原样），MD 忠实保留不改。
- 备注：Q_p/Z_p/T_p/V_p 印刷粗体（weight 拍平登记）；页界至 L1161 显示式，其后 L1164 起属 p.033。
- 结果：FAIL（5 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.033（PDF p.33 / 印刷 p.462）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 18:50 -0400。
- PNG：`audit/ribet1990_p033.png`（pngmono，150 dpi）。
- 核对：S=End(E₀,C_p) 结论；双射 ι: Σ(Mp)→ℰ、λ: Σ(M)→𝒱；T′(E)/pM·T(E) cyclic、V(E₀)=T(E₀)⊗Q、T(E)=g⁻¹T(E₀)、T′(E)=g⁻¹T′(E₀)；ℰ=S_f*\H_f*/H*、(3.3)、g⁻¹ vs g^{+1}（印刷原样 +1）、□；α,β: ℰ⇒𝒱 与 Σ(Mp)⇒Σ(M) 对照；Proposition 4.8（λα=αι、λβ=βι）与 Proof（T(F)/T′(E) cyclic of order M、m=diag(1,p) idele、M(2,Z_p)、m⁻¹T′(E₀)/mT(E₀)、x=m⁻¹g、β 兼容、α trivial、□）✓ 全部与印刷一致。
- 备注：F̄_q、H_f* 等印刷粗体（weight 拍平登记）；两处 □ 惯例不录。
- 结果：PASS。

## p.034（PDF p.34 / 印刷 p.463）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 19:00 -0400。
- PNG：`audit/ribet1990_p034.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："employing **E**"（无下划线）、"commutant of ***W*** / End_S(***W***)" 粗体确证，未存档）。
- 核对：(4.8)⇒ι: Y≈Z；pairings（Z^{Σ(Mp)}、E̲=(E,C)、½card(Aut(E̲))、E̲ 专用于 pM-enhancement、E̲₀=(E₀,C_p)、W=Hom(E̲,E̲₀)、End(E̲) 为 W 的 commutant、Tate 定理 [40]、Aut(E̲)=Aut_S(W)、o(e)、Z^ℰ）；Hecke 作用（T_p、[3]、GL(2,Q_p)\(℘^unr×X)、D*、1×π、Fr⁻¹、C_{F_p}、[13] Th. 4.4、𝒢=GL(2,Q_p)⁺\(Δ×X)、w_p/τ(p)、m）；τ 在 ℰ 上（(m·1,mx)、u、umx、n=um、normalizer、矩阵 (0 −1; p 0)、w_p、ι carries τ to w_p、Z⊂Z^ℰ 取负、orientation）✓。
- 发现并当场修复（5 个记号点；依据 300 dpi 裁片）：①L1190 括号句 "we have been employing $\underline{\mathbf{E}}$"→"$\mathbf{E}$"（印刷此处的 E 为粗体无下划线，与前句 pM-enhancement 专用符号 E̲ 区分；MD 误加下划线）；②L1190 四处 W 粗体："W=Hom(...)"→"$\mathbf{W}=..."、"commutant of W"→"of $\mathbf{W}$"、"End_S(W)"→"End_S($\mathbf{W}$)"、"Aut_S(W)"→"Aut_S($\mathbf{W}$)"。
- 结果：FAIL（5 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.035（PDF p.35 / 印刷 p.464）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 19:12 -0400。
- PNG：`audit/ribet1990_p035.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："the set **ϑ**"（vartheta）与显示式 "ϑ=⊔ᵢ₌₁^{r+1}R_r*a_i" 确证，未存档）。
- 核对：w_p 于 X₀(Mpq)_F_q、L⊂Z^{Σ(Mp)}、τ 取负、T_p↔−w_p、(3.19)；T_r（r≠p 素）经 X 作用、K\H_f*、ζ_r 命名、T(A′)=ΠT_l(A′)、r+1/r 项；ζ_r 保两 copies、Z^ℰ 上限制；ζ_q（L⊗Z_q-stable、q²=(T′:T)、H_q=End_{L⊗Q_q}(V_q(A))、T′=g⁻¹π⁻¹T_q、Frobenius、(3.5b)、(3.8)、T_q）；ζ_r（r⊥pqM、(T′:T)=r²、ϑ=⊔R_r*a_i、ζ_r(T)=Σg⁻¹a_i⁻¹T_r(A)、Σa_i g）；段尾 "(Here the a_i are" 接下页 ✓。
- 发现并当场修复（7 个记号点）：①L1196 "first copy of V"→"$\mathcal{V}$"；②L1200 "graph G"→"$\mathcal{G}$"；③L1202 三处 "vertices of G"→"$\mathcal{G}$"、"two copies of V"→"$\mathcal{V}$"、"$Z^{E}$"→"$\mathbf{Z}^{\mathcal{E}}$"（印刷粗体 Z 花体 ℰ 上标）；④L1212 "the set 9"→"the set $\vartheta$"（300 dpi 确证印刷为希腊 ϑ，mineru 误读为数字 9；L1215 显示式 \vartheta 本即正确）。
- 备注：H_f*/Z_r/V_r 印刷粗体或字重（weight 类，登记不改）。
- 结果：FAIL（7 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.036（PDF p.36 / 印刷 p.465）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 19:25 -0400。
- PNG：`audit/ribet1990_p036.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi：两处显示式 "ρ_**m**: G→GL(2,**T**/**m**)" 与 "trace(ρ_**m**(Frob_r))=T_r (mod **m**)" 的下标均为粗正体 m（非 fraktur 𝔪）确证，未存档）。
- 核对：ℰ 段收尾、ζ_r on ℰ、节标题 "5. Modular representations"；**T**=**T**_N、maximal ideal **m**、[5] Th. 6.7；Proposition 5.1（ρ_**m**: G→GL(2,**T**/**m**)、trace/det 关系、unramified、attached to **m**）；Théorème 6.7 关系（ℒ、Z[[q]]、ℒ 与 **T** 自由 **Z**-模同秩、S₂(Γ₀(N))、residue field **T**/**m**）；式 (9) ℒ→Z[[q]]、ℒ⊗_Zk→k[[q]]、torsion free；pairing (ℒ⊗_Zk)×(**T**⊗_Zk)→k、f|T、式 (10) ℒ⊗_Zk→Hom_Z(**T**,k)、dimension d、[39] Ch. 3、[27] Th. 2.2 ✓。
- 发现并当场修复（14 个记号点）：①L1226/L1228 两处 "E"→"$\mathcal{E}$"（花体，同款）；②L1232 三处 "Let $T=T_N$"→"$\mathbf{T}=\mathbf{T}_{N}$"、"Let m be"→"Let $\mathbf{m}$ be"、"ideal of T"→"of $\mathbf{T}$"；③L1237 显示式两处 "\mathfrak{m}"→"\mathbf{m}"；④L1243 显示式四处 "\rho_{\mathrm{m}}"×2→"\rho_{\mathbf{m}}"、"\mathrm{mod}\,\mathrm{m}"×2→"\mathrm{mod}\,\mathbf{m}"；⑤L1246 三处 "$\rho_m$"×2→"$\rho_{\mathbf{m}}$"、"attached to m"→"to $\mathbf{m}$"；⑥L1248 "\mathfrak{m}"→"\mathbf{m}"。依据：300 dpi 两处显示式放大确证印刷的最大理想符号为粗正体 m；MD 本页 \mathfrak/\mathrm/普通 m 三种混排，统一按印刷改为 \mathbf{m}。
- 后续页提示：p.037+ 各页同一符号请按印刷 \mathbf{m} 处理（L1281 起的 "\bmod m" 属 p.037 块范围）。
- 结果：FAIL（14 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.037（PDF p.37 / 印刷 p.466）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 19:40 -0400。
- PNG：`audit/ribet1990_p037.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："attached to **m**"、"det(ρ_**m**)"、"action of **T**"、"field **T**/**m**"×2 粗体确证，未存档）。
- 核对：(10) 单射性论证、t_n=(T_n mod m)、eigenform；Théorème 6.7 应用（cusp form mod l、Σt_nq^n、K⊂C、λ|l、k↪F、Lift f、𝒪 valuation ring）；ρ_m 的 det 为 mod l cyclotomic character、self Cartier-dual；W=J₀(N)[m] 定义；Theorem 5.2（(a) semisimplification V×…×V、(b) l⊥2N ⇒ W≈V、(c) η_r=1+r−T_r 与 m 互素）与 Proof (a)（faithful、Cartier dual Hom(W,μ_l)、(x²−T_rx+r)ⁿ、Cebotarev/Brauer-Nesbitt、Vⁿ）✓。
- 发现并当场修复（20 个记号点，全部为最大理想 **m**/Hecke 代数 **T** 粗体系——延续 p.036 印刷裁定，300 dpi 裁片确证）：①L1278 "T↦(T mod m)"→"\mathbf{m}"；②L1281 显示式同款；③L1288 七处（let m/of T/ρ_m×3/attached to m/characteristic of m）；④L1290 "(T/m)[G]"→"($\mathbf{T}/\mathbf{m}$)[G]"；⑤L1293 显示式 "\mathfrak{m}"→"\mathbf{m}"；⑥L1296 三处；⑦L1298 三处；⑧L1300 三处（\mathfrak{m}×2、ρ_m）；⑨L1304 一处；⑩L1308 三处（action of T、field T/m×2）。
- 备注：页界——印刷 p.466 止于 "This gives (a)."，MD L1310 起（To prove (b)、H⁰(X,Ω¹)、Néron model 段与编号表）属 p.038 范围（其中 L1326 "model model" 重复词与剩余 \mathfrak{m} 将在 p.038 条目处理）。
- 结果：FAIL（20 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。

## p.038（PDF p.38 / 印刷 p.467）
- actor=Wf-P42; model=account:zai-individual-coding-plan/GLM-5.3-Flash; effort=max（run级配置，自报UNKNOWN）；签认时间：2026-10-02 19:52 -0400。
- PNG：`audit/ribet1990_p038.png`（pngmono，150 dpi）；仲裁裁片：/tmp（300 dpi："Let **𝒟** be the contravariant Dieudonné-module functor…denoted M…"（𝒟 花体、M 普通斜体）确证，未存档）。
- 核对：To prove (b)（minimal submodule、V⊂W、X₀(N) over F_l）；H⁰(X,Ω¹)→F_l[[q]]、H⁰(X,Ω¹)[m] dimension ≤1；H¹(J,𝒪)/mH¹(J,𝒪)、pp.116–117 [18]；Néron model 段（𝒯 abelian scheme、Zariski closures 𝒱/𝒲、T[l]、e<(l−1)、[25] §3/3.3.2/3.3.6）；等价条件表 1. V=W / 2. 𝒱=𝒲 / 3. 𝒱_s=W_s；𝒱_s/𝒲_s special fibers；auto Cartier-dual 段；𝒟 Dieudonné functor（Oda [23]、(l,…,l)、φ/v、φv=vφ=0、Frob/Ver 约定）✓。
- 印刷原文 quirk：印刷即为 "Let 𝒯 be the Néron model **model** of J over Q_l"——"model model" 重复词为原刊 typo，MD 忠实保留不改（300 dpi 页图核验）。
- 发现并当场修复（16 个记号点）：①L1310 "(**T**/𝔪)[G]-submodule"→"\mathbf{m}"；②L1316 两处；③L1321 显示式 H¹(J,𝒪)/mH¹(J,𝒪)；④L1324 一处；⑤L1326 一处（**T**/**m**-vector space schemes）；⑥L1336 五处（𝒱_s/𝒲_s/special fibers of 𝒱 and 𝒲/T/**m**-vector space schemes）；⑦L1338 六处（𝒱_s⊂𝒲_s、𝒲_s/𝒱_s×2、copies of 𝒱_s、𝒱_s auto Cartier-dual）；⑧L1340 两处 "D"→"$\mathcal{D}$"（300 dpi 确证花体；"denoted M" 印刷普通斜体，MD 一致不改）。均据 150 dpi 页图花体 + 300 dpi 裁片。
- 备注：印刷编号表 "2. 𝒱=𝒲" 的序号 "2." 被 mineru 从显示式中略去（结构性微瑕，登记不改）；F_l weight 拍平照例登记；页界至 L1340，L1342 起属 p.039。
- 结果：FAIL（16 处记号错误）→ 本页当场修复闭环，修复后与原图逐项吻合。
