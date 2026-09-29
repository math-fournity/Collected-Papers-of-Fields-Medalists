# AUDIT — Bombieri, "Addendum to My Paper 'Algebraic Values of Meromorphic Maps'"（Invent. math. 11 (1970), 163–166）

> mineru: standard 档云端解析，导出 `Bombieri_1970_addendum_mineru/`；审计依据 = 二值化渲染
> `audit/addendum_pNNN.png`（pngmono 150dpi）对照
> `Bombieri_1970_addendum__Bombieri_1970_addendum.md`。逐页审计，一页一签。
> PDF 结构：p.1 = GDZ 数字库封面（PPN356556735_0011 | LOG_0020），p.2–5 = 印刷 pp.163–166。

## p.001（PDF p.1 / GDZ 封面页，无印刷页码）
- PNG：audit/addendum_p001.png
- 核对：
  - 封面题录：Werk / Titel: Inventiones Mathematicae / Verlag: Springer / Jahr: 1970 /
    Kollektion: Mathematica / **Werk Id: PPN356556735_0011** / PURL …**LOG_0020** ✓ 逐字吻合
    （md 以 `\_` 转义下划线，属 Markdown 必要转义）
  - Terms and Conditions 四段 ✓ 逐字吻合；**原文自身的笔误 "must contain there Terms and
    Conditions"（there 应为 these）被 md 忠实保留**——属"忠实≠错误"
  - 页眉 SLUB 馆徽文字（Niedersächsische Staats- und Universitätsbibliothek Göttingen）未转写
- 结果：**PASS±**
  - ±1：`## Contact` 标题下的**馆方联系块整体缺失**（Niedersächsische Staats- und
    Universitätsbibliothek Göttingen / Georg-August-Universität / Platz der Göttinger Sieben 1 /
    37073 Göttingen / Germany / Email: gdz@sub.uni-goettingen.de）——纯图书馆地址信息，
    与论文内容无关，不影响学术使用；
  - ±2：页眉馆徽文字（同 ±1 性质）未转写。
- 备注：本页为 GDZ 数字库封面，非论文正文；下划线转义、原始笔误保留均正确。

## p.002（PDF p.2 / 印刷 p.163）
- PNG：audit/addendum_p002.png
- 核对：
  - 题录：Inventiones math. 11, 163–166 (1970) ✓、© by Springer-Verlag 1970 ✓
  - 标题 Addendum to My Paper "Algebraic Values of Meromorphic Maps" ✓、ENRICO BOMBIERI (Pisa) ✓
  - 节标题 I. Introduction ✓；"In my previous paper [1] the following result is crucial
    (notations are as in [1])" ✓
  - **Existence Theorem**：V 于 C^n 多重次调和 ⟹ 存在 C^n 上全纯且不恒为零的 F(z) 使
    ∫_{C^n} |F|² e^{−V}(1+|z|)^{−3n} ω_n < +∞ ✓ 逐符号吻合（指数 −3n、ω_n 均正确）
  - 论证动机段（e^{−V} 不可和点集在 Ω 内闭且测度零；文献无证明；本短文目的）✓ 逐字吻合
  - (1/π) ∂∂̄V = T ✓
  - Θ(‖T‖; r, a) = T 在球 B(r, a)（半径 r、中心 a）中的平均质量 ✓；对 r < dist(a, ∂Ω) 单调不减 ✓
  - Θ(‖T‖; a) = lim_{r→0} Θ(‖T‖; r, a) ✓；Lelong number 命名 ✓
  - **双边不等式** (1 − |a|/r)^{2n−2} Θ(‖T‖; r − |a|, 0) ≤ Θ(‖T‖; r, a) ≤ (1 + |a|/r)^{2n−2}
    Θ(‖T‖; r + |a|, 0) ✓ 逐符号吻合（指数 2n−2、自变量 r∓|a|、内外系数 1∓|a|/r 全对）
  - "(see [1], Lemma 6)" ✓
  - **页脚 "12 a Inventiones math., Vol. 11" 被保留**，以行内文本形式接在 "…proof of Lemma 1." 之后
    ——与多数件的"页眉页码丢弃"不同，本件页脚反而成为**天然的 p.163/p.164 页界锚点**
- 结果：**PASS±**
  - ±1：原页眉行（Inventiones math. 11, 163–166 (1970) / © by Springer-Verlag 1970）md 未单独转写；
  - ±2："non-decreasing" 跨行连字符在 md 中合并为 "nondecreasing"（正常去连字符，不影响语义）。
- 备注：数学内容零错误；页脚内联是检索时的注意点（勿把 "12 a" 当作正文）。

## p.003（PDF p.3 / 印刷 p.164）
- PNG：audit/addendum_p003.png
- 核对：
  - **Theorem 1**：存在仅依赖维数 n 的常数 γ(n) > 0，使 Θ(‖T‖; a) < γ(n) ⟹ e^{−V(z)} 在
    z = a 某邻域可和 ✓ 逐字吻合
  - 说明段：Θ(‖T‖; a) = 0 几乎处处 ⟹ e^{−V} 在 Ω 内闭且测度零的集外局部可和（呼应 [1]）✓
  - **Theorem 2**：V 于 C^n 多重次调和 ⟹ e^{−V} 在 C^n 某复解析超曲面外局部可和 ✓
  - Θ(‖T‖; a) > 2n 时 e^{−V} 处处不可和：用 [1] 之 Lemma 7 (ii) + V 局部表为 Newton 位势
    模调和函数 ✓
  - **Structure Theorem**：对每个 c > 0，{Θ(‖T‖; a) > c} 局部含于复解析超曲面内；
    特别地该集具局部有限 (2n−2) 维 Hausdorff 测度 ✓
  - **Theorem 2A**（Theorem 2 的局部版）：V 于开集 Ω 多重次调和 ⟹ e^{−V} 在 Ω∖N 局部可和，
    N 在 Ω 中闭且局部含于复解析超曲面 ✓
  - 节标题 **II. Proof of Theorem 1** ✓
  - T = (1/π) ∂∂̄V、d‖T‖ = iT ∧ ω_n（相伴正 Radon 测度）✓
  - 局部化说明：在原点考察 e^{−V} 可和性，可设 V 定义于 |z| < 1 ✓
  - **Newton 位势 P_ε(z) = −((n−2)!/(4π^{n−1})) ∫_{|ζ|<ε} (1/|z−ζ|^{2n−2}) d‖T‖(ζ)** ✓
    （**300dpi 复核**：下标确为 ε、自变量确为 z——150dpi 初读疑似 "P_z(ζ)" 系目检误差，
    md 正确；此式下标/自变量若互换会改变数学含义，故此处仲裁必要）
- 结果：**PASS±**
  - ±：mineru 丢弃 running head（164 / E. Bombieri:）。
- 备注：数学内容零错误。本页再次出现"低分辨率目检疑似错、300dpi 仲裁判 md 正确"的案例
  （本 PDF 至此已 3 次：ε_{2m}、Schaefer、P_ε(z)）。

## p.004（PDF p.4 / 印刷 p.165）
- PNG：audit/addendum_p004.png
- 核对（逐式）：
  - 承接句 "differs from V(z) in |z|<ε only by a harmonic function … summability of P_ε(z)
    at the origin" ✓
  - **Lemma 1**：|a| < ε、r < ε 时 ∫_{|z−a|<r} |∇P_ε(z)| ω_n(z) ≤ c₁Θ(‖T‖; 3ε, 0) r^{2n−1} ✓
  - Proof 首式 |∇P_ε(z)| ≤ c₂ ∫_{|ζ|<ε} (1/|z−ζ|^{2n−1}) d‖T‖(ζ)（因 d‖T‖ 为正测度）✓
  - "Next, one checks easily that" ∫_{|z−a|<r} ω_n(z)/|z−ζ|^{2n−1} ≤ c₃ r (t+1)^{−2n+1}，
    t = (1/r)|ζ−a| ✓；t ≥ 2 ⟹ |z−ζ| ≥ r(t−1)、t < 2 ⟹ |z−a|<r ⊂ |z−ζ|<3r 的论证 ✓
  - I 的首两行：I ≤ c₃r ∫_{|ζ−a|<2ε} (1 + (1/r)|ζ−a|)^{−2n+1} d‖T‖(ζ) = c₃r ∫_0^{2ε/r}
    (1+t)^{−2n+1} d‖T‖B(rt, a) ✓
  - "Finally" 链：‖T‖B(rt,a) = (π^{n−1}/(n−1)!)(rt)^{2n−2}Θ(‖T‖; rt, a) ≤ …Θ(‖T‖; 2ε, a)
    ≤ c₄(rt)^{2n−2}Θ(‖T‖; 3ε, 0) ✓ 逐符号吻合
  - 页脚 "12 b Inventiones math., Vol. 11" 保留（内联，同 p.163 惯例）✓
  - "the last inequality being one noted earlier. Combining this estimate with the bound already
    obtained for I, Lemma 1 follows." ✓；Lemma 2（John and Nirenberg）开头 ✓
- 结果：**FAIL（3 处，内容级）**
  - ✗1 **∇ 被误识为 V**：md 中 "Hence" 链首行写作 `| V P _ {\varepsilon} (z) |`，
    原文为 **|∇P_ε(z)|**（同页上文与 Lemma 1 陈述均正确用 `\nabla`）。∇P 与 VP 数学含义不同。
    修复建议：`| V P _ {\varepsilon} (z) |` → `| \nabla P _ {\varepsilon} (z) |`。
  - ✗2 **整行丢失 + LaTeX 损坏**：该 "Hence" 三行链中，**第 2、3 行被空 `\qquad` 填充而丢失**，
    数组以**非法命令 `\qend{array}`** 收尾（无法编译）。丢失内容为
    "≤ c₂ ∫_{|z−a|<r} ∫_{|ζ−a|<2ε} (1/|z−ζ|^{2n−1}) d‖T‖(ζ) ω_n(z) = c₂ I."
    ——**其中 "= c₂ I" 是后文"bound already obtained for I"的指代对象**，丢失影响阅读连贯。
    修复建议：以完整三行链替换该数组（积分域 |ζ|<ε → |ζ−a|<2ε 的一步 + `= c_2 I`）。
  - ✗3 **负号丢失**：md 写作 `= \frac{c_3 r}{(1+2\varepsilon/r)^{2n-1}} \|T\| B(2\varepsilon, a) + …`，
    原文为 **"= − c₃r/(1+2ε/r)^{2n−1} ‖T‖B(2ε,a) + …"**（300dpi 复核：行首确为减号）——
    分部积分项符号，属数学内容错误。修复建议：该分式前补 `-`。
  - ±：running head（Addendum to My Paper "Algebraic Values of Meromorphic Maps" / 165）被丢弃。
- 备注：本页是本 PDF 中**唯一 FAIL 页**，且三处缺陷均集中在同一处推导链；除该链外其余公式零错误。
  引用该页结论（Lemma 1 的界）时**以原 PDF 为准**。

## p.005（PDF p.5 / 印刷 p.166，**末页**）
- PNG：audit/addendum_p005.png
- 核对：
  - 承接句 "the last inequality being one noted earlier. Combining this estimate with the bound
    already obtained for I, Lemma 1 follows." ✓
  - **Lemma 2 (John and Nirenberg)**：U(z) 在 |z| < 2R 可和、∫_{|z−a|<r} |∇U(z)| ω_n(z) ≤ γ r^{2n−1}
    （对一切 |a| < R, r < R）✓
  - 结论式 min_k ∫_{|z|<½R} exp(c₅ γ^{−1}|U(z) − k|) ω_n(z) ≤ c₆ R^{2n}，c₅,c₆ 仅依赖 n ✓
    逐符号吻合（含 ½R 限、绝对值、γ^{−1}）
  - Proof：John–Nirenberg [2] 特例；Trudinger [3] 给出简证 ✓
  - 合并 Lemma 1、2：exp(−c₅γ^{−1}P_ε(z))、从而 exp(−c₅γ^{−1}V(z)) 在 |z| < ε/2 可和，
    γ = c₁Θ(‖T‖; 3ε, 0) ✓
  - 末段：Θ(‖T‖; 0) < c₅/c₁ = γ(n) ⟹ 存在 ε > 0 使 Θ(‖T‖; 3ε, 0) < c₅/c₁ 且 exp(−V(z))
    在原点邻域可和，Theorem 1 证毕 ✓
  - **References 逐条**：
    1. Bombieri, E.: Algebraic values of meromorphic maps. Inventiones Math. **10, 267–287 (1970)** ✓
    2. John, F., Nirenberg, L.: On functions of bounded mean oscillation. Comm. Pure Appl. Math.
       **14, 415–426 (1961)** ✓
    3. Trudinger, N.S.: On embeddings into Orlicz spaces and some applications. J. Math. Mech.
       **17, 473–483 (1967)** ✓
  - 署名地址：E. Bombieri / Istituto Matematico "Leonida Tonelli" / Università di Pisa /
    Via Derna 1 / I-56100 Pisa ✓
- 结果：**PASS±**
  - ±1：**收稿日期行 "(Received September 7, 1970)" 整行丢失**（grep "received" 无命中）——
    属书目信息，不影响数学内容，但引用时若需投稿/收稿日期须查原 PDF；
  - ±2：running head（166 / E. Bombieri: Addendum to My Paper …）被丢弃。
- 备注：数学内容零错误；文献三条卷页年逐字准确。

## 总评
- **覆盖声明**：本 PDF 共 5 页（pdfinfo 5p），**逐页 5/5 完成审计**（audit/addendum_p001–p005.png），
  含 GDZ 封面页；无跳页、无抽查替代。正文对应印刷 pp.163–166（Invent. math. 11）。
- 结论分布：PASS± ×4（p.1 封面 / p.2 / p.3 / p.5）+ **FAIL ×1（p.4，三处内容级缺陷）**。
- FAIL 汇总（均在 p.165 的 I 界推导链，附修复建议）：
  ① `| V P_{\varepsilon}(z) |` 应为 `| \nabla P_{\varepsilon}(z) |`（∇→V 误识）；
  ② 三行链的第 2、3 行丢失（积分域 |ζ|<ε → |ζ−a|<2ε 一步 + `= c_2 I`），数组以非法 `\qend{array}` 收尾；
  ③ `= \frac{c_3 r}{(1+2\varepsilon/r)^{2n-1}}` 前丢失负号（分部积分项符号）。
- 系统性瑕疵：①running head/页码全丢（不误导）；②封面 Contact 联系块丢失；
  ③末页收稿日期行丢失；④**页脚 "12 a / 12 b Inventiones math., Vol. 11" 反被保留为行内文本**
  （可作页界锚点，但检索时勿当正文）。
- 忠实性正面案例（勿误判为错误）：封面 "must contain **there** Terms and Conditions"（原刊笔误）、
  p.163 页脚内联、p.165 页脚内联。
- 仲裁记录：本 PDF 有 3 处 150dpi 目检疑似错误经 300dpi 复核判 **md 正确**——ε_{2m} 下标、
  "Schaefer"（原刊单 f 拼法）、P_ε(z) 下标/自变量。教训：低分辨率目检不得直接压过 md，须仲裁定案。
- 可用性：p.163/p.164/p.166 可放心引用；**p.165 的 I 界推导链须以原 PDF 为准**（或先按上述三条修复 md）。
- mineru 解析信息：mineru 3.4.4 / tier=basic / parse_mode=ocr（本目录导出件无 doc_id 字段）。
