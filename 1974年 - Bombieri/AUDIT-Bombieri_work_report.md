# AUDIT — Chandrasekharan, "The Work of Enrico Bombieri"（ICM 1974 官方工作报告，印刷 pp.5-8）

> mineru: standard 档云端解析，导出 `Bombieri_1974_work_report_chandrasekharan_mineru/`；
> 审计依据 = 二值化渲染 `audit/report_pNNN.png`（pngmono 150dpi）对照
> `Bombieri_1974_work_report_chandrasekharan__Bombieri_1974_work_report_chandrasekharan.md`。
> 逐页审计，一页一签。
> ⚠️ 本 PDF 是 4 页摘录：**起点即印刷 p.5 中段**（首句 "made in later years by H. Rademacher…"
> 承接 p.4 未完句），非 mineru 截断。

## p.005（PDF p.1 / 印刷 p.5）
- PNG：audit/report_p001.png
- 核对：
  - 题录/running head：THE WORK OF ENRICO BOMBIERI + 页码 5（图中有）
  - 筛法史首句（Rademacher、Estermann、Ricci、Buchstab → Selberg 1946-1951 筛法）✓ 逐字吻合
    （原文 "Buch-stab" 跨行断词，md 正确还原为 Buchstab）
  - Linnik 1941 大筛法起源、Vinogradov 猜想 h₂(p)（最小二次非剩余）✓、h₂(p) < cp^ε ✓
  - exceptional prime 定义（未被表示的剩余类数 > τp，0<τ<1）✓
  - Linnik 界 c₁N/τ²Z（c₁ 为绝对常数）✓
  - "≪ log log X" 结论 ✓
  - sieving set {Ω_p}、p ≤ N^{1/2}、"more than τp elements" ✓
  - Rényi 步：Z(p,a) 定义（n_j ≡ a mod p 的元素数）✓
  - S_X = Σ_{p≤X} p Σ_{a=0}^{p−1} (Z(p,a) − Z/p)² ✓ 逐符号吻合
  - (2) S_X ≤ 2NZ，for X = (N/12)^{1/3} ✓（**300dpi 复核：此式确带编号 (2)**；
    其上方 c₁N/τ²Z 一式**确无编号**，md 不编号亦正确）
  - S_X ≥ Σ_{p≤X} (|Ω_p|/p) Z² ✓（Ω_p 下标正确，非 ⊗ 链）
- 结果：**PASS±**
  - ±：mineru 丢弃 running head（THE WORK OF ENRICO BOMBIERI）与页码 5/S，正文无影响。
- 备注：数学内容零错误；\epsilon/\varepsilon 混用一处（原文均为 ε），不影响语义。

## p.006（PDF p.2 / 印刷 p.6）
- PNG：audit/report_p002.png
- 核对：
  - 承接句 "which, when combined with (2), gives an upper bound for Z—and also Linnik's result
    provided that X = N^{1/2}" ✓
  - Rényi 应用（充分大偶数 = 素数 + 殆素数）✓ 逐字吻合
  - Rényi 不等式适用范围 p ≪ N^{1/3} vs Linnik p ≪ N^{1/2} ✓
  - Roth/Bombieri 1965：Mathematika 12 (1965), 1–9 与 201–225 ✓（卷号/页码/年份逐字）
  - Roth: X = (N/log N)^{1/2}；Bombieri: X = N^{1/2} ✓
  - Bombieri 三角双和不等式前提：x_1,…,x_R δ-well-spaced（‖x_k − x_l‖ ≥ δ > 0，
    ‖θ‖ = 到最近整数距离）、T(x) = Σ_{n=M+1}^{M+N} a_n e^{2πinx} ✓
  - **(3) Σ_{k=1}^{R} |T(x_k)|² ≤ (N + 2/δ) Σ_{n=M+1}^{M+N} |a_n|²** ✓ 逐符号吻合（含编号 (3)）
  - 出处 Acta Arith. 18 (1971), 401–404；Proc. Internat. Conf. Number Theory, Moscow, 1971 ✓；
    "Bessel's inequality in a Hilbert space" 比喻 ✓
  - 取 x_k = a/q 有理、(a,q)=1、q ≤ Q 时回收 Rényi (2)（q 素）与 Selberg 上界筛型（q 合）✓
  - Gauss 和 G(χ) = Σ_{a=1}^{q} χ(a) exp(2πia/q) ✓
  - Σ_χ |G(χ)|² χ(m)χ̄(n) = φ(q)·S_{m−n,q}（若 (mn,q)=0）、= 0（若 (mn,q)>1）✓
  - S_{m,q} = Σ_{a=1;(a,q)=1}^{q} exp(2πiam/q) ✓
- 结果：**FAIL（单点，符号级）**
  - ✗ md 第 39 行：「(with $\leqslant$ in place of $\leqslant$)」——原文实为 **"(with ≪ in place of ≤)"**
    （300dpi 灰度 5× 放大复核：前者为双尖括号 ≪ 无下横，后者为 ≤）。md 输出成同符号重复，
    该括注因此自相矛盾、语义反转（原意为"常数不再固定为 2"）。
    **以原图为准**。修复建议：首个 `$\leqslant$` 改为 `$\ll$`。
  - 说明：本 md 其余 13 处 `\ll` 均识别正确（如 p ≪ N^{1/3}），故此为**孤立误识**，非系统性。
  - ±：running head（6 / K. CHANDRASEKHARAN）被丢弃。
- 备注：除此单符号外，本页正文、公式、文献出处零错误。

## p.007（PDF p.3 / 印刷 p.7）
- PNG：audit/report_p003.png
- 核对：
  - "is the well-known Ramanujan sum (not to be confused with S_X in (2))" ✓
  - **(4) Σ_{q∈Q} (1/φ(q)) Σ_χ |G(χ)|²·|Σ_{X<n≤Y} χ(n)a_n|² ≤ 7D·max(Y−X, M²)·Σ_{X<n≤Y} d(n)|a_n|²** ✓
    逐符号吻合（含编号 (4)；系数 7D、max(Y−X,M²)、d(n) 除数函数）
  - Σ_χ 记号：**300dpi 3× 复核确认原文为无星号的 Σ_χ**（"Here Σ_χ denotes summation over
    *all* characters χ modulo q"），md 的 `\sum_{\chi}` 正确——150dpi 初看疑似"Σ*_χ"，经仲裁否定
  - **D = D(q) = max_{q∈Q} d(q)、M = M(Q) = max_{q∈Q} q** ✓ 逐字吻合，且**忠实保留了原文自身的
    大小写不一致**（D 写小写 q、M 写大写 Q）——系原刊笔误，非 mineru 之误
  - 密度定理求和式 Σ_{q∈Q} (1/φ(q)) Σ_χ |G(χ)|² N(α,T;χ) ✓
  - "uniform with respect to Q, for ½ ≤ α ≤ 1, T ≥ 2" ✓
  - N(α,T;χ) 定义（L(s,χ) 在矩形 α ≤ Re s ≤ 1 内零点数、|Im s| ≤ T）✓；**原文此处自身重复
    出现 "½ ≤ α ≤ 1"（300dpi 确认），md 亦照录**——原刊衍字，非解析错误
  - Siegel-Walfisz 定理引用 ✓
  - 三大应用逐条：Vinogradov (1937) 充分大奇数 = 三素数 ✓、Linnik (1961) 充分大整数 = 素数+两平方 ✓、
    Chen (1967) 充分大偶数 = 素数 + 至多两素因子之积 ✓
  - "It has not put an end to any one question; rather it has led to many new ones." ✓
  - 推广：χ(n)n^{it} 型乘性特征、"δ-well-spaced" ✓
  - 素数间隙 p_{n+1} − p_n ≪ p_n^{7/12+ε} ✓、RH 蕴含指数 1/2 说明 ✓
  - 密度假设 N(α,T;χ₀) ≪ T^{2(1−α)+ε} 对 α > 13/16 ✓、χ₀ 主特征 ✓
  - 学者名单 Davenport / Halberstam / Gallagher / Montgomery ✓（续页接 Halász 等）
- 结果：**PASS±**
  - ±：running head（THE WORK OF ENRICO BOMBIERI）与页码 7 被丢弃。
- 备注：数学内容零错误；两处"看似异常"（D(q) 大小写、½≤α≤1 重复）经 300dpi 仲裁均系原刊自身，
  md 忠实无误——本页是"忠实≠错误"的典型案例。

## p.008（PDF p.4 / 印刷 p.8，**扫描件末页**）
- PNG：audit/report_p004.png
- 核对：
  - 承上页名单续：G. Halász, M. N. Huxley, M. Jutila，及较近的 M. Forti, C. Viola ✓
    "There is little doubt that Bombieri's theorems have inspired that development." ✓
  - 节标题 **2. Univalent functions and the local Bieberbach conjecture** ✓
  - S 族定义 f(z)=z+a₂z²+a₃z³+…，单位圆盘 |z|<1 内归一化全纯单叶 ✓
  - Bieberbach 猜想陈述：Re a_n ≤ n，等号仅当 f(z)=z/(1−ρz)² 且 ρ^{n−1}=1 ✓（逐字）
  - 已知范围 2 ≤ n ≤ 6 及大量子族 ✓
  - 1965 Garabedian–Schiffer 局部有效性提问（2 − Re a₂ 小 ⟹ n − Re a_n ≥ 0？n 偶时肯定）✓
  - **ε_{2m} 陈述**：正数 ε_{2m} 使 |2 − a₂| < ε_{2m} ⟹ Re a_{2m} ≤ 2m；等号 ⟺ Koebe 函数
    f(z) = z(1−z)^{−2} = Σ_{n=1}^{∞} nz^n ✓（**300dpi 复核**：ε 下标与右端确为 2m，非 2n；
    150dpi 初读疑似"2n"系目检误差，md 正确）
  - Bombieri 1967 对一切 n 证明（n 奇更难）Invent. Math. 4 (1967), 26–67 ✓
  - 两个 lim inf 陈述：n 偶用 (n−Re a_n)/(2−Re a₂)、a₂→2；n 奇用 (n−Re a_n)/(3−Re a₃)、a₃→3 ✓
    逐符号吻合；lim inf 取遍 S 族全部函数 ✓
  - Garabedian–Schiffer 独立证明 Arch. Rational Mech. Anal. 26 (1967), 1–32 ✓
  - 证明构成：Löwner 参数法 + Duren–Schiffer"第二变分"理论 ✓；用 A. C. **Schaefer** 与
    D. C. Spencer 的 Löwner 曲线结果 ✓（**300dpi 复核：原刊此处即写作单 f 的 "Schaefer"**——
    数学史通行拼法为 Schaeffer，但 md 与原文逐字一致，属"忠实≠错误"，不得据通行拼法改写）
  - 二次型 (Q_n)（无穷多变元）两条性质：(a) 不定 ⟹ 该 n 猜想不成立；(b) 正定 ⟹ Koebe 函数的
    一切解析变分使 Re a_n 减小 ✓
  - Duren–Schiffer (1962/63) 证 Q_n 对 n=2,…,9 正定、计算机验至 n ≤ 100 ✓
  - Bombieri 证 Q_n 对**一切 n** 正定，Boll. Un. Mat. Ital. (3) 22 (1967), 25–32 ✓
  - 节标题 **3. Several complex variables** + 引文 Invent. Math. 10 (1970), 267–287; 11 (1970),
    163–166，正文止于断词 "moti-" ✓（扫描件自然截断，md 忠实）
- 结果：**PASS±**
  - ±：mineru 丢弃 running head（8 / K. CHANDRASEKHARAN）。
- 备注：数学内容零错误；本页两处 150dpi 目检疑点经 300dpi 仲裁均判 md 正确，再次印证
  "低分辨率目检不得压过 md，须仲裁后定案"。

## 总评
- **覆盖声明**：本 PDF 共 4 页（pdfinfo 4p），**逐页 4/4 完成审计**（audit/report_p001–p004.png），
  无跳页、无抽查替代。本件为 ICM-1974 工作报告的 4 页摘录，起于印刷 p.5、止于印刷 p.8 中段断词。
- 结论分布：PASS± ×3（p.5/p.6 除下述符号外/p.7/p.8）+ FAIL ×1（p.6 单符号级）。
- 系统性瑕疵：①running head 与页码全部丢弃（每页均见，不误导）；
  ②**孤立符号误识 1 处**：p.6 "≪" 被解析为 `\leqslant`，致 "(with ≤ in place of ≤)" 自相矛盾。
- 修复建议（若要把该 md 用作引用底本）：将 md 第 39 行首个 `$\leqslant$` 改为 `$\ll$`；
  其余无需改动。
- 忠实性正面案例（勿误判为错误）：p.7 的 `D = D(q)` 大小写不一致、p.7 "½ ≤ α ≤ 1" 重复、
  p.8 "Schaefer"（单 f）——三者均为原刊自身写法，md 逐字忠实。
- 可用性：除上述 1 处符号外，可放心作为正文引用与检索底本；页界以原 PDF 为准。
- mineru 解析信息：mineru 3.4.4 / tier=basic / parse_mode=ocr（本目录导出件无 doc_id 字段）。

> **修复登记（2026-09-29）**：已按本审计将 "(with ≪ in place of ≤)" 中误识的首个 \leqslant 修回 \ll；修复与本登记同一 commit；修复前 md 见该 commit 父提交。
