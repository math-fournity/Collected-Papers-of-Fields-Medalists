# Deng 2018 Strichartz — Luna 审计重做（逐页视觉重检）

> 性质：Luna 审计重做（用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核）。
> 本文件只登记重做范围（p.1 起）的页级结论；旧 [AUDIT-Deng_2018_strichartz.md](AUDIT-Deng_2018_strichartz.md) 不再作为可信依据，保留仅作对照。
>
> - actor：Wf-R-Deng
> - host / model / effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置，自报 UNKNOWN）
> - PDF：Deng_2018_strichartz.pdf，34 页，SHA-256 = 6987354755fee2b7960f9cf6986d0cebaa4a733f0319230bbc7fd1b9399c1948
> - MD 基线 SHA-256（重做起点，即 Luna 修复后版本）：60f572494701abc6fe95882c753a3b0f86660a98f866cc7767d8a25d8910dd1b
> - 开工时间：2026-10-02 14:28 EDT
> - 文本层判定：`pdftotext -f 1 -l 1` 首页正常输出（arXiv:1810.05630v3 题录完整，exit 0）→ 文本层可用，采用**双通道主对账**（每页 pdftotext 文本层 + 150dpi pngmono PNG 视觉目检，以印刷页图像为最终裁决）。
> - 证据图：`audit-redo/`（pngmono 150dpi，p001–p009 本次）；旧 `audit/` 不动。
> - 纪律：印刷原文为唯一裁决源；Luna 旧修复一并重核；print quirk 与错字忠实保留登记，不按数学预期静默改正；看不清即升级 300dpi 仲裁，不编造。

## p.001（PDF p.1 / 印刷 p.1）
- PNG：audit-redo/p001.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：题录（标题/四位作者/arXiv:1810.05630v3 印记/摘要）、§1.1–1.2 节序、公式 (1.1)(1.2)(1.3) 及 §1.2 无编号式、≲ 与 ≤ 的区分
- 结果：PASS±。题名、作者、摘要（含原刊 "on the other hands" quirk，忠实保留）逐字吻合；(1.1) s = max(0, d/2 − (d+2)/p)、(1.2)、(1.3) 的 ≤、χ(−Δ_M/N²)、O_ε(N^ε T^ε)、s(p) = max(d/4 − d/(2p), d/2 − (d+1)/p) 全部与印刷页一致。瑕疵（均不误导，按 SOP 不改）：display 公式边界句尾标点被吞 3 处——MD L11 "with data v_0" 后缺逗号、L39 O_ε(...) 后缺句号、L41 ‖·‖_{H^s(M)} 后缺句号。
- 备注：Luna 旧修复抽核通过——旧基线的「Schrödinger 重音拆成 sup 标记」「arXiv 印记漏录」在当前 MD 中已不存在（L1/L3 正常）。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：audit-redo/p002.png（pngmono 150dpi）＋ 300dpi 页底仲裁裁片 audit-redo/p002_300dpi_bottom.png ＋ pdftotext 文本层对账
- 核对：s(4)=max(1/8, d/4−1/2)、(1.4) 严格不等号 s(p)>max(0, d/2−(d+2)/p)、§1.3 节标题、环面定义 M=M_{e_1…e_d}、(1.5)、换元 x=y_1e_1+⋯+y_de_d、Fourier 展开 f=Σf̂_k e^{2πik·y}、Δ_M f=−4π²Σ|Ak|²f̂_k e^{2πik·y}、页底 e^{itΔ̃} display
- 结果：PASS±。300dpi 仲裁确认页底印刷确为 e^{it\widetilde{Δ}}（Δ 带波浪）且环面符号为粗体 \mathbf{T}^d（与正文 𝕋^d 混用属原刊自身记号），MD L108 的 `\widetilde{\Delta}`＋`\mathbf{T}^d` 转录忠实。print quirk "the spectrum of Δ_M the torus is rational"（L67）经 PNG 核实为原刊原样，保留。瑕疵（不误导，不改）：L57 "d ≥ 3" 后缺句号；L83 "B(0,N)" 后缺句号；L71 §1.3 run-in 标题被 MinerU 连同尾句 "Define a torus" 整体升级为 `##` 标题（内容与顺序无损）。
- 备注：Luna 旧修复抽核通过——they deduce（L49）、d-dimensional 连字符（L43）、x∈M 的 ∈（L87）、cutoff 拼写（L31）在当前 MD 均已正确。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：audit-redo/p003.png（pngmono 150dpi）＋ 300dpi (1.6) 仲裁裁片 audit-redo/p003_300dpi_eq16.png ＋ pdftotext 文本层对账
- 核对：页顶 Δ̃=(1/2π)Σα_{ij}∂_i∂_j 定义、(1.6) 全式与下标 ≲_{p,(α_{ij}),ε}、Conjecture 1.1 单和式（Σ_{n=0}^d N^{n/2−(n²+2n)/p}）、四分段 piecewise display（含末段 N^{d/2−(d²+2d)/p} 与条件 4n+2<p≤4n+6, n∈{1,…,d−1}）、d=2 四条 bullet 指数
- 结果：PASS±（1 处已修复）。(1.6) 的 e^{it\widetilde{Δ}}、粗体 \mathbf{T}^d、≲ 下标、指数全部经 300dpi 核实与 MD L122 一致；Conjecture 1.1 与分段式的各指数、定义域逐项吻合；四条 bullet 指数（T^{1/p}；T^{1/p}+N^{1−4/p}；T^{1/p}N^{1/2−3/p}+N^{1−4/p}；N^{1−8/p}T^{1/p}+N^{1−4/p}）与印刷一致。原刊 quirk "symmetric, positive definite, matrix" 的双逗号（L114）为印刷原样，保留。**修复 1 处**：L155 原为 `$d = 2 .$,`（数学式内多出原刊没有的句点），印刷为 "dimension d = 2, in which case"——已改为 `$d = 2$`。残余瑕疵（不误导，不改）：L117/L145/L157 公式边界句尾句号缺失 3 处。
- 备注：Luna 旧修复抽核通过——bullet 符号、拆字（10→1 0 类）、cutoff 拼写在当前 MD 均正常。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：audit-redo/p004.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p004_300dpi_thm11.png、p004_300dpi_thm12.png ＋ pdftotext 文本层对账
- 核对：Theorem 1.1（LHS 𝕋²/RHS 𝕋^d 混用、N^{(2/3)(1−4/p)} 缺口因子）、Theorem 1.2 两分支（T^{1/p}N^{1/2−3/p} 与 N^{1−8/p}T^{1/p}）、Remark 1.3（”elliptic”/”hyperbolic” 反向引号、∂_x²±∂_y²、[10]、p≥8/p≤8）、§1.3.1 run-in 标题、(1.7)、K_N 定义
- 结果：PASS±。300dpi 核实定理两式为黑板体 𝕋（与 (1.6) 的粗体 \mathbf T 不同属原刊自身混用），指数、≲_{α,ε}、方括号结构与 MD L170/L180 逐项一致；Remark 1.3 的 ”…” 原刊反向引号（L185）忠实保留；K_N 定义与 (1.7) 完整。瑕疵（不误导，不改）：L167 "p > 4" 后缺逗号；L173 Thm 1.1 "B(0,N)" 后缺句号（印刷有）；L177 "ε > 0" 后缺逗号。注意：Thm 1.2 的 "provided Supp f̂ ⊂ B(0,N)" 印刷本身无句号，MD L183 忠实一致，不属缺失。
- 备注：Luna 旧修复抽核通过——旧基线 If→I f、p=10 拆字、As a 损坏在当前 MD（L167/L180/L185）均已不存在。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：audit-redo/p005.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p005_300dpi_bounds.png、p005_300dpi_levelset.png、p005_300dpi_exponent.png（4x）、p005_300dpi_Sline.png（3x）＋ pdftotext 文本层对账
- 核对：页顶三条 K_N bounds（第一条 ≲ min(N²,1/t)、后两条 ⪯ 与 N^{4/3}(1+t^{1/6})、N⁴T 及 T 条件）、E_λ level-set 定义、|E_λ| 分解式、S 定义、Ĵ₁ 公式、‖Ĵ₁‖≲|S|、TT* 两 bullet、§1.3.2 大求和式（f̂_{k₁}overline{f̂}_{k₂}…、(1−e^{2πiTΩ})/(2πiΩ)）、Ω 定义
- 结果：PASS±。300dpi 核实：三条 bounds 第 1 条为 ≲、第 2/3 条为 ⪯（MD L204 \lesssim/\preceq 区分忠实）；E_λ 行与 bounds 下标为黑板体 𝕋²，而 S 行 sup 下标为粗体 \mathbf{T}²（3x 放大清晰可辨）——MD L212 \mathbb{T}²、L230 \mathbf{T}² 均忠实，混用属原刊自身；E_λ 指数 4x 放大确认为 e^{it\widetilde{Δ}}（波浪清晰）。原刊 quirk 忠实保留：provided λ²>‖J₂‖_{L^∞} 后的多余 ")"（L227）、"The approach which was has been sketched"（L247）、J₁ 的 \widehat{L^∞} 宽帽（L227）。瑕疵（不误导，不改）：L249 bullet 句尾缺句号；L259 "(α_{ij})" 后缺逗号。L209 行内 Δ̃ 用 \tilde 而非 \widetilde，仅帽宽渲染差异，同一符号。
- 备注：Luna 旧修复抽核通过——旧基线 E_λ 的 \bar{Δ}、行首多余 e、bcan、bullet 丢失在当前 MD 均已不存在。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：audit-redo/p006.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：(1.8) 三段式（|Q(k₂)+Q(k₄)+⋯+Q(k_p)−β|<δ、k₂+k₄+⋯+k_p=a、k_i∈ℤ²∩B(0,N)）、[7,19,26] 与 Borel-Cantelli 段、Pall [27] 方程组（k₁²+k₂²+k₃²=A 等）、N_k^{1/k} 简单估计段、§1.4 节、K_N^{(d)} 定义、(1.9) sup/积分式（\mathbf{T}^d 下标、2s 指数、s∈ℕ）、(1.10) I_s(T)≲N^εT(N^{ds+d}+N^{2ds−d(d+1)})
- 结果：PASS±（2 处已修复）。全部公式与正文经 PNG＋文本层逐项吻合；(1.9) 的 sup_{x∈**T**^d, t∈[T,2T]}、|·|^{2s} 与 (1.10) 指数 ds+d、2ds−d(d+1) 无误。print quirk "one in interested principally"（L273）经 PNG 核实为原刊原样，保留。**修复 2 处**（同类：原刊没有的多余句点）：L265 `$k_1,k_3,...$. and`→`$k_1,k_3,...$ and`；L271 `$a,\beta .$.`→`$a,\beta$.`。残余瑕疵（不误导，不改）：L271/L285/L287 公式或段尾缺句号 3 处（δ=1/N 后、p=8 后、d>2 后，印刷均有句号）。
- 备注：Luna 旧修复抽核通过——旧基线 N_k^{1/k} 后多 2、coefficients 误拼、p=16 拆字在当前 MD（L283/L273/L265）均已不存在。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：audit-redo/p007.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：μ₁/μ₂ measure 定义式（t^{−1}m_i^{(j)}、O(γ_j/TN)、O(1/tN)、≲ 条件尾）、y^{(k)} 系统计数段与 Σ_{k=1}^{d+1}y_i^{(k)}y_j^{(k)}=A_{ij}、§1.5 八条 Notation bullet（‖x‖=min|x−k|、≲/∼ 定义、⪯ 定义、≪ 约定、1_E(x)、f̂_k 与 f̂(τ,k) 两个积分式、⟨t⟩=√(1+t²)）、Acknowledgements 四段 grant 号
- 结果：PASS±（1 处已修复）。μ₁/μ₂、求和式、八条 bullet、四个 grant（DMS-1900251；DMS-1501019+Simons+NYUAD；Simons Investigator；EP/M507970/1+ERC 670239+Fields+NSF-DMS 1363013）逐项与印刷一致；\widehat{f}_k（帽只在 f 上）忠实。print quirk 忠实保留：L323 原刊不平衡括号 y^{(d+1)})∈(ℤ^d)^{d+1}（无开括号）。**修复 1 处**：L323 "the number of solution"→"solutions"（印刷与 pdftotext 均为 solutions）。残余瑕疵（不误导，不改）：L333/L335/L339 bullet 尾缺句号 3 处。
- 备注：Luna 旧修复抽核通过——旧基线 ‖x‖ 主语漏录、\widehat{f_k} 帽位错、致谢顺序错/S.M. grant 重复在当前 MD（L333/L346/L357-363）均已不存在。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：audit-redo/p008.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p008_300dpi_rect_display.png ＋ pdftotext 文本层对账
- 核对：§2 节引（比值 ‖e^{itΔ̃}f‖/‖f‖）、启发式 (1)–(3) 全部 display：(1) ∼T^{1/p}；(2) N^{d/2}χ(Nx)、∫_{1/N²}^{1/N}∫_{B(0,tN)}dx dt/(tN)^{dp/2} ≳ N^{dp/2−(d+2)}；(3) N^{−d/2}Σχ̂(k/N)e^{2πi[…]}、∀k 邻式、‖tα_{ij}‖≪1/N²、(d²+d−2)/2、Dirichlet/Khinchin 的 N^{d²+d−2−ε}≲q≲N^{d²+d−2} 与 ‖qα_{ij}‖<1/N²、almost period、末式 N^{d/2−(d+2)/p}[T/N^{d²+d−2−ε}]^{1/p}>N^{d/2−(d²+2d)/p−ε}T^{1/p}；(4) 开头
- 结果：PASS±（3 处已修复）。全部公式逐项吻合。300dpi 裁定两处易误读点均为 MD 忠实：矩形环面句印刷确为**无波浪** e^{itΔ}（与紧邻下一句的 e^{itΔ̃} 形成原刊自身对比，MD L379/L381 分别正确）；表达式 display 内层 Σ 印刷**无** _{ij} 下标（MD L384 一致；∀k 式的 Σ_{ij} 有下标，MD L390 亦一致）。print quirk 忠实保留："close to a integer multiple of 2π"（L393）、"this give examples"（L409）。**修复 3 处**（同类：原刊没有的多余标点）：L367 `$f ,$,`→`$f$,`；L371 `$\chi .$.`→`$\chi$.`；L377 `$f .$.`→`$f$.`。残余瑕疵（不误导，不改）：L369/L403 句尾标点缺失；L371 "initial data f" 后缺逗号。
- 备注：Luna 旧修复抽核通过——旧基线初值误成 f_i 等在当前 MD（L371 为 N^{d/2}χ(Nx)）已不存在；"a integer multiple" 为原刊原样，Luna 亦登记保留，正确。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：audit-redo/p009.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：(4) 后半与 display N^{n/2−(n²+2n)/p−ε}T^{1/p}‖f‖、"Overall, this gives the conjecture (1.1)"、Remark 2.1 全部四式（Parsell–Vinogradov 两条件式、≳N^{pd/2}+ΣN^{(p−1)j+d−j(j+2)}≥…、(N^{d/2}+N^{d−d(d+2)/p})T^{1/p}>max(1,·)T^{1/p}‖f‖、as T→∞ sup 比 ≳ T^{1/p}Σ_{n=0}^d N^{n/2−(n²+2n)/p}）、§3 节标题、§3.1 χ 截断与 K_N 定义、Lemma 3.1（|t|≲1/N ⟹ ∀x∈𝕋², |K_N|≲min(N²,1/t)）、Proof 方框
- 结果：PASS±（1 处已修复）。四条 display 的指数、求和限、≥/＞/≳ 层次、1_{|k|<N} 粗体指示符逐项与印刷一致；Lemma 3.1 与 □ 证明结束符忠实。**修复 1 处**（同类）：L449 `on$\mathbb{R} .$,`→`on$\mathbb{R}$,`（原刊无此句点）。残余瑕疵（不误导，不改）：L455 "(α_{ij})" 后缺句号（印刷有）；L369（p.8 范围已登记）同类的 (1) 句尾缺句号在 L409 区域无新例。
- 备注：Luna 旧修复抽核通过——旧基线 "Similar sums 前多出 e"、"differencing 误识"、证明方框控制字符在当前 MD 均已不存在（方框现为 □）；"this give examples"（L409）与 "focuse" 类原刊拼写保留正确。

## 本块小结（p.001–p.009 重做完成；非全篇总评）

- 覆盖：PDF p.1–p.9（印刷页码同），逐页 150dpi pngmono PNG 全览＋逐页 pdftotext 文本层对账（双通道主对账，文本层可用），9 处疑难字形/符号升级 300dpi 仲裁（p002 底式、p003 (1.6)、p004 定理两式、p005 bounds/level-set/exponent 4x/S-line 3x、p008 矩形环面句＋表达式 display）。
- 页级结论：9 页全部 **PASS±**，0 FAIL。无一处数学内容错误（公式、指数、编号、陈述全与印刷页一致）；登记不修改的 PASS± 瑕疵共 25 处，其中 display 公式边界句尾标点缺失 23 处（p.1×3、p.2×2、p.3×3、p.4×3、p.5×2、p.6×3、p.7×3、p.8×3、p.9×1，详见各页条目），另 2 处为 §1.3 run-in 标题被 MinerU 升级为 `##`（L71）与行内 Δ̃ 的 \tilde/\widetilde 帽宽渲染差（L209）。print quirk 忠实保留共 9 处（"on the other hands"、"the spectrum of Δ_M the torus is rational"、"symmetric, positive definite, matrix" 双逗号、provided 后多余 ")"、"which was has been sketched"、\widehat{L^∞} 宽帽、不平衡括号 y^{(d+1)})、"close to a integer multiple"、"this give examples"；另有 𝕋/\mathbf{T} 与 e^{itΔ}/e^{itΔ̃} 的原刊自身混用经 300dpi 逐处核实为印刷原样）。
- 本次修复（8 处，均为原刊没有的多余标点或词级误录，逐处对应页证据；git diff 全量核对恰为 8+/8−，无其他行变动）：
  1. L155（p.3）`$d = 2 .$,`→`$d = 2$,`
  2. L265（p.6）`$k _ { 1 } , k _ { 3 } , . . .$. and`→`$…$ and`
  3. L271（p.6）`$a , \beta .$.`→`$a , \beta$.`
  4. L323（p.7）"the number of solution"→"solutions"
  5. L367（p.8）`functions$f ,$,`→`functions$f$,`
  6. L371（p.8）`function$\chi .$.`→`function$\chi$.`
  7. L377（p.8）`the same$f .$.`→`the same$f$.`
  8. L449（p.9）`on$\mathbb { R } .$,`→`on$\mathbb { R }$,`
- Luna 旧修复重核：9 页逐页抽样全部通过——旧基线登记的 FAIL 项（题名重音、arXiv 印记、deduce/the、连字符、∈、bullet、widetilde/barΔ、N_k^{1/k} 后多 2、致谢顺序、f_i 初值、方框控制字符等）在当前 MD 中均确已修复；Luna 登记的 print quirk 保留项（hands、was has been、a integer、one in interested、this give 等）均被正确保留、未被误改。
- 收尾只读清点：`$$` 定界行 490（偶）；`\tag` 51；C0 控制字符 0；1,783 行 / 124,488 bytes。MD SHA-256 由基线 60f572494701…dd1b 变为 a6ff2f6080b91693e03e58e3fcf962a26c5e2c0a174185abaf445ae86c36e796（差异 = 上列 8 处修复，见 git diff 8d10e4f6..HEAD）。
- 范围声明：本块只覆盖 p.1–p.9；p.10–p.34 的重检与全篇总评、根级索引/进度由后续块与集成方负责，本文件不对其作任何结论。证据图 18 张（p001–p009 全页 + 9 张 300dpi 裁片）均已随页提交入库。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：audit-redo/p010.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：Proposition 3.2 假设与 (3.1)、(i)(ii) 两式（≼ N^{4/3}⟨t⟩^{1/6}、≼ N⁴T）、§3.2 节引、Lemma 3.3 差分式（ΣΣΠ min(N, 1/‖2tL_j(r)‖)）、#E^N_{m₁,m₂} 求和式与定义、(3.2)、Minkowski minima 引理（N²/(M₁^tM₂^t)、F(n,m)=max(|n_i/N|, N|tL_i(n)−m_i|)、M_k^t 定义）、t∼T∈2^ℤ、dyadic 条件 (3.3a)–(3.3e)
- 结果：PASS±（1 处已修复；另 1 处曾误判已即时回滚）。(3.1)–(3.3e) 编号与内容逐项与印刷一致（Luna 旧基线的编号错位/空标签已不存在；(3.3a)-(3.3e) 标签齐全且与印刷对位）。**修复 1 处**：L489 句尾全角逗号 "，"→半角 ","（印刷为半角）。**误判回滚登记**：初审时将 (3.3c) 闭合 `$$` + 空行 + (3.3d) 开启 `$$`（L539-541）误判为"空 display 块"并删除，随后只读清点发现 `$$` 行数变为 489（奇数、失配），当即恢复原结构并复核 `$$` 行数回到 490（偶）、(3.3a)–(3.3e) 各 display 定界配对完整——该序列是合法的逐式 display 分隔，不是空公式。残余瑕疵（不误导，不改）：L481 "(ii) For any T ≥ 1" 后缺逗号。
- 备注：Luna 旧修复抽核通过——本页公式链（Lemma 3.3 → E 集合 → (3.2) → Minkowski → (3.3a-e)）与印刷逐式一致，旧基线的编号问题已修复且未引入新错位。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：audit-redo/p011.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：(3.4a)–(3.4d) 四条兼容性条件（β/N、γ/βN 右端与编号顺序）、regime 句 1/N<β<√γ≪1、(3.5) β≳1/(NT) 及反证段、E^{n,n′}_{β,γ,N,T} 定义、Lemma 3.4 (i)(ii)（∅ 与 γ²N/|n×n′|(1+TγN·gcd/β|n₂′|)min(β/|n|, γ/β|n′|)）、Σ 分割 display（两 substack 条件 + "= Σ₁+Σ₂"）、Bound for Σ₁ 与 γ³TN²Σgcd/(|n₂′||n×n′||n₁|)
- 结果：PASS±。四条 (3.4x) 编号依次对位无误（Luna 旧基线的"四标签整体错后一位"已修复且现与印刷一致）；Lemma 3.4 (ii)、(3.5)、Σ 分割多行 display 逐项吻合。print quirk 忠实保留："The cases where one of n₁,n₂,n₁′,n₂′ is zero is easier to deal with"（L589，原刊语法原样）。残余瑕疵（不误导，不改）：L577 "= 0" 后缺逗号、L583 "n₂′ ≠ 0" 后缺逗号、L589 句尾缺句号（印刷均有）；L599 印刷对 "Bound for Σ₁" 整词组加下划线而 MD 仅对 Σ₁ 加下划线（排版级，语义无损）。
- 备注：Luna 旧修复抽核通过——旧基线登记的 (3.4a) 孤立标签/末式漏标在当前 MD（L549-563）已不存在；标签-公式配对与 p.11 印刷逐一对齐。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：audit-redo/p012.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p012_300dpi_conclusion.png（1.5x 与 4x）＋ pdftotext 文本层对账
- 核对：gcd 分式分解 display（Σ_λ、三重 substack、≼1）、Σ₁≼γ³TN²、Bound for Σ₂ 与 γ³N/(β|n×n′||n₂′|)、Σ_{n,n′}1/(|n×n′||n₂′|) 链式 ≼ βN、Σ₂≼γ³N²、"Proposition (3.2)" 结论段两式（γ³N²(1+T)）、两 regime bullet（T^{−1/3−δ}N^{−2/3−δ} / T^{−δ}N^{−2/3−δ}）、ΣΣ|E|<∞、Borel-Cantelli 后 M₁^tM₂^t≽γ(t,N)、末式 ∀t>1/N, x∈𝕋^d, |K_N|≼N^{4/3}⟨T⟩^{1/6}
- 结果：PASS±（3 处已修复）。全部公式与印刷逐项一致；末式环面记号经 4x 放大确认为**黑板体 𝕋^d**（上标 d 为原刊原样——Proposition 3.2 主体系 𝕋² 而此结论行写 𝕋^d，MD L668 `\mathbb{T}^d` 忠实）。print quirk 忠实保留："We can now conclude the proof of Proposition (3.2)"（L635，带括号系原刊原样）。**修复 3 处**：L649/L651 两条 regime 设置补回 bullet 符号 "- "（印刷有 •，Luna 旧基线已登记项目符号丢失但未修复）；L659 "(α_{ij})" 后全角逗号 "，"→半角 ","。残余瑕疵（不误导，不改）：L617/L599 "Bound for Σ₂/Σ₁" 印刷整词组下划线而 MD 仅对 Σ 加下划线。
- 备注：Luna 旧修复抽核部分未完成——p.12 两条 bullet 在 Luna 修复后仍缺失（本次补上），其余本页旧修复无新问题。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：audit-redo/p013.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：§3.3 节引与首 display（Π min(N,1/‖tL_j(n)‖)，此处无因子 2 与 p.10 Lemma 3.3 的 2tL_j(r) 不同，均与印刷一致）、P(t) 定义、(3.6) 两行积分＋=ΣS₁S₂、(3.7) S₁≼N/(|p₁|+|p₁′|)、平方积分链 (Σ N/(|p₁|+|p₁′|) Σ_k 1)²≲N⁴(...)²≼N⁴、∬∫sup|K_N|⁴≼N⁴T、ν/δ 整数-分数分解（−1/2≤δ,δ′<1/2）、ε,ε′∈2^ℤ∩[1/N,1/2] 定义、S₁≲Σ∫(1/εε′)dα₁₁
- 结果：PASS±。本页（至 "We now argue as follows:"，MD L727）全部公式与陈述逐项与印刷一致；页界判明：L729 起的 "For ε,ε′ fixed…" 段属 p.14 印刷内容，留待下页核对。print quirk 忠实保留："we focuse on the former"（L689，原刊拼写）。
- 备注：Luna 旧修复抽核通过——Luna 对 p.13 的判断（focuse 为原刊原样、仅 PASS±）与本页重检结论一致；未发现 Luna 引入的错误。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：audit-redo/p014.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：两条 • bullet（ν/ν′ 约束计数与 α₁₁ 测度）、|νp₁′−ν′p₁−C|<ε|p₁′|+ε′|p₁|、≼tk(ε|p₁′|+ε′|p₁|+1)、tk 论证段、≲min(ε/t|n₁|, ε′/t|n₁′|)、|S₁(t)| 汇总链（≼Σ(1/εε′)tk(…)min(…)≲Σ1+1/(ε′|p₁|)≼N/|p₁|）、§3.4 节、K_N 平方展开与 r=n−n′/s=n+n′ 换元 display（Σ* 奇偶限制）、s₁ 子和、Abel 求和 ≲min(N,1/‖2tΣα₁jr_j‖)、总体 ΣΣΠ min(N,1/‖2tL_j(r)‖)
- 结果：PASS±（3 处已修复）。全部公式与印刷逐项一致；print quirk "a constant dedending on"（L735）、"restricted to these s"（L769）忠实保留。**修复 3 处**：L741 `ε′|\stackrel{\sim}{p}_1|`→`ε′|p_1|`（**Luna 基线已登记"带波浪的 p₁"但未修复的遗留错误**，印刷为无波浪 p₁）；L729/L743 补回两条 bullet "- "（印刷有 •）。残余瑕疵（不误导，不改）：L741 句尾缺句号；L757 §3.4 run-in 标题被 MinerU 升级为 `##`（与 §1.3 同类，内容无损）；L787 "L_j(r)=Σα_{ij}r_i" 后缺句号。
- 备注：Luna 旧修复抽核**发现遗留缺陷**——其 p.14 条目登记的"ε′|p₁| 误排为带波浪 p₁"在修复后版本中仍存在（本次修正）；bullet 缺失同样登记未修（本次补上）。除此外本页无其他问题。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：audit-redo/p015.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：§3.5 (i) n×n′=0 反证（n=kp, n′=kp′、四条代入不等式 β/(N|p|) 与 γ/(βN|p′|)、binom 向量差的 ≲/≥ 夹逼、1≲β|p′|/N+γ|p|/βN、矛盾式 ≲γ≪1）、(ii) 开头、• First freezing t bullet、两条 α₁₂ 求解 display（±O(γ/T|n×n′|)）、(3.8) 兼容性条件、"staisfying" 计数段与 ≲γ(TN)²、≲1+TγN·gcd/(β|n₂′|)
- 结果：PASS±（2 处已修复）。全部公式与印刷逐项一致。print quirk 忠实保留："staisfying"（L855，原刊拼写）。**修复 2 处**：L789 `The case $n×n′=0 .$$.` 双句点（印刷单句点）；L839 "First freezing t…" 补回 bullet "- "（印刷有 •）。残余瑕疵（不误导，不改）：印刷对 "(ii) The case n×n′≠0" 加下划线而 MD 无下划线（与 p.11 "Bound for Σ" 同类排版级差异，语义无损）。
- 备注：Luna 旧修复抽核通过——本页公式链与印刷逐式一致，未见 Luna 引入的错误。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：audit-redo/p016.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：(3.8) 解数汇总 ≲γ(TN)²(1+…)、• With t still frozen bullet（三个测度 ∼γ/N²T²·1/|n×n′|、β/NT·1/|n₂|、γ/βNT·1/|n₂′| 及 ≲γ/(N³T³|n×n′|)min(…)）、• dt≪1/N² 离散时间 bullet（O(N²T)）、Lemma 3.4(ii) 汇总式、§4 节标题、Step 1 kernel 分解（φ、φ̂≥0、A∈(0,1/N)、J₁/J₂/J₃ underbrace display）、‖Ĵ₁‖≲A、‖J₂‖≲1/A、‖J₃‖≼N^{4/3}T^{1/6}、S_μ 定义（无绝对值）、|S_μ|≼N⁴T/μ⁴、J₃=J₃1_{S_μ}+J₃(1−1_{S_μ})=J₃′+J₃″
- 结果：PASS±（1 处已修复）。全部公式与印刷逐项一致。print quirk 忠实保留：S_μ 定义中 sup K_N 无绝对值（Luna 登记为原刊原样，PNG 复核确认）；p.16 印刷在 ≲γ(TN)² display 后 bullet 前有一行游离句点（原刊排印噪声），MD 未转录该噪声行，属合理省略。**修复 1 处**：L867 "solve for α<sub>22</sub>" HTML 下标残留→`$\alpha _ { 2 2 }$`（全文一致性，印刷为 α₂₂）。残余瑕疵（不误导，不改）："Step 1: decompositions of the kernel" 印刷有下划线、MD 无（排版级）。
- 备注：Luna 旧修复抽核通过——本页未见 Luna 登记项之外的问题；S_μ 无绝对值的保留判断正确。

## p.017（PDF p.17 / 印刷 p.17）
- PNG：audit-redo/p017.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：The bounds 段（‖Ĵ₃′‖≼N⁴T/μ⁴ 与 ‖J₃″‖≤μ 的 ≼/≤ 区分、provided μ>N^{4/3}）、Step 2（F=e^{itΔ̃}f 的波浪号、E_λ 定义、F̃=(F/|F|)1_{E_λ}、Q(k)）、Plancherel–Cauchy-Schwarz 五行链（χ(k_i/N)^{1/2}、overline、卷积归并）、⟨(J₁+J₂+J₃)*F̃, F̃⟩ 三行链、(4.1) 与 (4.2)、Step 3 引（‖F‖_{L^∞(ℝ×𝕋^d)}≲N）、• If λ>N^{2/3+δ}T^{1/12} bullet 与 |E_λ|≼N^δλ^{−4}
- 结果：PASS±（1 处已修复）。本页（至 |E_λ|≼N^δλ^{−4}，MD L963）全部公式与印刷逐项一致；≲/≤/≼ 层次、上标 1/2、共轭线均忠实。print quirk 忠实保留：Step 3 的 ‖F‖ 定义域 ℝ×𝕋^d（上标 d 非本篇主体 2，原刊原样，MD L957 忠实）；"Step 2/Step 3" 印刷下划线、MD 无（排版级）。**修复 1 处**：L959 "If λ>N^{2/3+δ}T^{1/12}…" 补回 bullet "- "（印刷有 •）。
- 备注：Luna 旧修复抽核通过——旧基线的"Cauchy–Schwarz 前多余 e""distinguished 拆字"在当前 MD 已不存在；F=e^{itΔ̃}f 波浪号正确。

## p.018（PDF p.18 / 印刷 p.18）
- PNG：audit-redo/p018.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：三情况后两条 • bullet（A=N^δ/λ², μ=λ²N^{−δ/4} 与 Chebyshev+‖F‖_{L⁴}≲T^{1/4}）、|E_λ| 两式、4<p<10 积分链（三段积分限与 λ^{p−5}/λ^{p−11} 指数、≼T(N^{2/3})^{p−4}+N^{p−4+δ}）、§5 节标题（ℓ² decoupling: p=14）、dyadic 归约 f=Σf̂_k**1**_S(k)e^{2πik·y}、S⊂B(0,N)∩ℤ²、Theorem 5.1（≼(N⁴+T)N^{p−8}|S|^{p/2}, if p=14）、矩阵记法 (α₁₁ α₁₂; α₁₂ α₂₂)=(1 β; β α)、(5.1) 五条交替和、[9] 界 ≼N^{2p−10}|S|、(5.2) ≼N^{p−8}|S|^{p/2}
- 结果：PASS±（2 处已修复）。本页（至 (5.2)，MD L1037）全部公式与印刷逐项一致。**修复 2 处**：L965/L971 两条 bullet 补回 "- "（印刷有 •；连同 p.17 的 L959，Step 3 三情况 bullet 现齐全）。残余瑕疵（不误导，不改）：L1005 "f̂_k ∼ 1" 后缺句号；L1009 "(α_{ij})" 后缺逗号；L971 "≲ T^{1/4}" 被 MD 拆为两个相邻数学串（印刷为同一行内公式，渲染等价）。
- 备注：Luna 旧修复抽核通过——旧基线 p.18 的"12、10、14 等数字被拆字""Our aim 前多余 b"在当前 MD（L977/L1007）均已不存在。

## 本块小结（p.010–p.018 重做完成；非全篇总评）

- 覆盖：PDF p.10–p.18（印刷页码同），逐页 150dpi pngmono PNG 全览＋逐页 pdftotext 文本层对账（双通道主对账），1 处升级 300dpi 仲裁（p012 末式 𝕋^d 字形，1.5x 初读误似粗体、4x 放大确认为黑板体，避免了一次误改）。页界：p.10 起 Proposition 3.2，p.18 止 (5.2)；L729 起属 p.14、L861/L915 起分属 p.16/p.17 的跨页内容按印刷页界归属登记。
- 页级结论：9 页全部 **PASS±**，0 FAIL。无数学内容错误；Lemma 3.3/3.4、Proposition 3.2、(3.1)–(3.8)、(4.1)(4.2)、Theorem 5.1、(5.1)(5.2) 及各推导链与印刷逐式一致；≲/≤/≼ 与 ≳/≥/⪯ 层次、bold **1** 指示符、binom/underbrace 结构均忠实。
- 本次净修复 **13 处**（每处可溯源对应页 PNG/文本层证据；git 净 diff 恰为 13+/13−，与下表逐行对应）：
  1. L489（p.10）全角逗号 "，"→","
  2. L649/L651（p.12）两条 regime bullet 补 "- "（印刷有 •，Luna 基线登记未修）
  3. L659（p.12）全角逗号 "，"→","
  4. L729/L743（p.14）两条 bullet 补 "- "
  5. L741（p.14）`ε′|\stackrel{\sim}{p}_1|`→`ε′|p_1|`（Luna 基线登记未修的遗留错误）
  6. L789（p.15）`$=0 .$.` 双句点→单句点
  7. L839（p.15）"First freezing t" bullet 补 "- "
  8. L867（p.16）HTML 残留 `α<sub>22</sub>`→`$\alpha_{22}$`（该行 bullet 原本就在，仅替换记号）
  9. L959（p.17）/L965、L971（p.18）三条 bullet 补 "- "（Step 3 三情况至此齐全）
  （上表按行号分组共 9 组、按修复处数计 13：1+2+1+2+1+1+1+1+3。）

## p.019（PDF p.19 / 印刷 p.19）
- PNG：audit-redo/p019.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：|S|^{p/2−1} 计数论证段（含原刊不平衡括号 "(ie i ≥ p/2,"）、"We can write" 三行 display（f̂ 与 overline{f̂}、1_S(k,ℓ)、(1−e^{2πiT(A+Bα+Cβ)})/(2πi(A+Bα+Cβ))）、Σ1≲N⁴2^j+1、(N⁴+2^{−j})N^{p−8}|S|^{p/2}≼(N⁴+T)…、证明结束方框、§6 节标题、Theorem 6.1（≲|S⁴|(N⁴+NT)）、(6.1) 两条 meas 估计、B 集合与 meas_R3(B)、A_z 定义 display
- 结果：PASS±（3 处已修复）。全部公式与印刷逐项一致；print quirk 忠实保留："(ie i ≥ p/2," 无闭括号（L1041，原刊原样）。**修复 3 处**：L1049 `$\beta _ { i }$`→`$\beta$` 并补逗号（印刷为 "genericity of α and β,"，无下标 i）；L1067 Theorem 6.1 句尾全角逗号 "，"→","；L1060 补 "□" 证明结束框（印刷在 Theorem 5.1 证明末尾右侧有空心方框，MD 缺失——Luna 基线的"方框存为控制字符"实际被整体删除而非替换）。**误报登记**：初审曾将 L1039 的 `$$` 误判为孤儿开启符，经与 git HEAD 逐行对照确认它是 (5.2) display 的闭合定界符（其后直接接正文属合法结构），未做修改——p.010 教训再次强调 display 定界符必须查配对上下文。
- 备注：Luna 旧修复抽核通过——旧基线 p.19 的"证明结束方框存为控制字符"已不在（但方框本身也被删了，本次补回 □）；其余无新问题。

## p.020（PDF p.20 / 印刷 p.20）
- PNG：audit-redo/p020.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p020_300dpi_delta.png（2.2x）＋ pdftotext 文本层对账
- 核对：zA⊂A_z 句、§6.1 Pall's formula 引（φ(x,y)=A′x²+B′y²+2C′xy、公式 (43)/(44)、[27] p.358）、Lemma 6.2 求和式（24·2^ν∏_{p|2kΔ}χ(p)）、χ 定义段（p^{u₁}/p^{u₂−u₁}/δ₁=⌊(u₁+1)/2⌋）、κ₁/κ₂ 四行表、(6.2)、Corollary 6.3（≤h、h²|gcd）、Proof 的 χ(p)≤{…} 与 Πχ(p)≤2^ν(…)(…)＝2^ν d(Δ)h、□ 结束框
- 结果：PASS±（2 处已修复，1 处还原印刷错字）。κ 表四行、(6.2)、Corollary 及证明链逐项与印刷一致。**还原 1 处（印刷错字忠实化）**：L1111 印刷为 **Δ=(A′B′−C′)/k²**（C′ 上无平方；300dpi 2.2x 与同行 k² 的清晰上标 2 对照确认，pdftotext 亦无该 2）——原刊排版错字（数学上应为 C′²），MD 原作 `(C′)²` 属静默数学改正，已按印刷原形还原并在此登记；同页 Lemma 6.2 条件 "A′B′−C′²>0" 印刷有平方、MD 忠实，两处对照佐证 Δ 行确为原刊漏排。**修复 1 处**：L1101 `meas<sub>R</sub>3`/`meas<sub>R</sub>2` HTML 下标残留→`$\mathrm{meas}_{\mathbb{R}^3}$`/`$\mathrm{meas}_{\mathbb{R}^2}$`。残余瑕疵（不误导，不改）：L1103 "C′ ∈ Z" 的 Z 为数学环境外裸字符（印刷为黑板体 ℤ）；L1131 "gcd(A′,B′,C′)" 后缺句号。
- 备注：Luna 旧修复抽核**发现偏离**——Δ=(A′B′−C′)/k² 的印刷错字被此前的修复链静默改正为 (C′)²，本次已按纪律还原；其余本页无新问题。

## p.021（PDF p.21 / 印刷 p.21）
- PNG：audit-redo/p021.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：§6.2 Ω^{p,N} 与 Ω^{q,N,+} 两定义、"Recall that" 链、(6.3) 三行（substack 条件 a,b≲N、A_i,B_i,C_i≲N²、|(A₁−A₂)+(B₁−B₂)α+(C₁−C₂)β|≲2^j、sup_{a,b≲N;τ≲N²}）、k′_i=4k_i−a 换元、(6.4) 五和⟺四和（16A₁−4a²、16B₁−4b²、16C₁−4ab）、(6.5) k″/ℓ″/A′B′C′ 定义、(6.6) 注入 ↪（含 "C′.}" 句点位置）
- 结果：PASS。本页全部定义与公式逐项与印刷一致，无标点缺失、无拆字、无记号偏差——本篇重做以来首个无瑕疵页。(6.4)/(6.5) 的 16 系数完整（Luna 旧基线的"16 拆成 1 6"已修复且未复发）。
- 备注：Luna 旧修复抽核通过——本页旧修复无遗留、无新错。

## p.022（PDF p.22 / 印刷 p.22）
- PNG：audit-redo/p022.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：(6.7) 两段式（(1+2^j)N 分离项与 A′B′≠0 substack）、§6.3 退化情形引（A′B′=(C′)²、三平方和等式条件）、k″_i=pz_i/ℓ″_i=qz_i、(6.8) 双段链（p,q≲N/√m 与 mp²,mq²≲N²、√m）、Lemma 6.4（satisying 原刊拼写、⪰_{α,β}N^{−2}）、Proof 的 E 集合与 |E|≤N^{−2−τ}min(1/(mq²−m′(q′)²), 1/(mp²−m′(p′)²))、Σ|E|∼N^{−2−τ}Σ(1/d)Σ、p′-bounds display（√max(mp²−d,0)/√m′ ≤ p′ ≤ √(mp²+d)/√m′）
- 结果：PASS±。本页（至 p′-bounds display，MD L1233）全部公式与印刷逐项一致；⪰ 方向与下标 α,β 忠实（Luna 旧基线的"符号方向转成 \succeq"实为正确转录，印刷即 ⪰）。print quirk 忠实保留："satisying"（L1211，原刊拼写）。残余瑕疵（不误导，不改）：L1195 "k″ = 0 or ℓ″ = 0" 后缺句号。
- 备注：Luna 旧修复抽核通过——旧基线 p.22 的"判别式条件拆乱"在当前 MD 已不存在；(6.7)(6.8) 结构完整对位。

## p.023（PDF p.23 / 印刷 p.23）
- PNG：audit-redo/p023.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：p′ 计数 display（1+d/√(m′(mp²+d))）、(p,p′) 求和 ≼N/√m+d/√(mm′)、d 定义链 ≼N²、"there are most O(N^ε)" divisor 段及 1/d² 链 ≼N²、Σ|E|<∞ 与 Borel-Cantelli 收尾（□）、(6.9) ≼(2^jN²+1)N、§6.4 节引（U=h^{−2}A′ 等）、(6.10)、|U+Vα+Wβ|⪰_{α,β}h⁴/N⁴、h≤N^{1/2} 求和 ≲2^jN⁴+N、"this should heuristically" 段首
- 结果：PASS±。本页（至 "this should heuristically"，段落在 MD L1287 跨页延续）全部公式与印刷逐项一致；□ 结束框在位。print quirk 忠实保留："there are most O(N^ε)"（L1253，原刊漏 "at"）。残余瑕疵（不误导，不改）：L1275 "W=h^{-2}C′" 后 MD 添有原刊没有的逗号（印刷 "W = h−2C′ we deduce"，无逗号）。
- 备注：Luna 旧修复抽核通过——旧基线 p.23 的"mq²/d 带点横线变量""h,U,V 定义多出点横线""方框控制字符"在当前 MD 均已不存在。

## p.024（PDF p.24 / 印刷 p.24）
- PNG：audit-redo/p024.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对："make no difference" 段、Lemma 6.5（Φ 定义三重 substack、≼_{α,β}2^jN⁴/K+N/K）、(6.11)、(6.12) ⪰_{α,β}ρ、optimistic bound 段（⪯_{α,β}2^j/ρ、≲_ε N^{−4+ε}、⪰_ε 2^jKN^{4−ε}、KN^{−ε}）、Σ(α,β,τ′) 定义（h²(U,V,W)≠h′²(U′,V′,W′)）、(6.13) 平方链、对角贡献段与 Σ′(α,β) 定义
- 结果：PASS±（2 处已修复）。全部公式与印刷逐项一致。**修复 2 处**：L1287 "diference"→"difference"（印刷与 pdftotext 均为双 f；注意 Luna 在 p.24 登记的少 f quirk 指 "sufficient"，与本词无关，本词印刷拼写正确而 MD 少 f，属转录错字）；L1307 `$U,\dot{U′},\dot{V},V′,W,W′\stackrel{-}{\sim}N²/h²`→`$U,U′,V,V′,W,W′\lesssim N²/h²` 并补 K 后逗号（印刷为干净 ≲，无点无横线——Luna 基线登记的"点/横线"类缺陷在本行残留，本次清除）。残余瑕疵（不误导，不改）：L1321 "KN^{−ε}" 后缺句号。
- 备注：Luna 旧修复抽核部分未完成——"点/横线"类缺陷在其登记后仍有一处残留于 L1307（本次修复）；其余本页无新问题。

## p.025（PDF p.25 / 印刷 p.25）
- PNG：audit-redo/p025.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：Borel-Cantelli 积分链 display（Σ′≼_{α,β}∫Σ′dα′dβ′）、"Consquently" 段与 Σ′≼_{α,β}2^jN^{12}/K^{10}、2^{j/2}N⁶/K⁴ 反例段（K=N^{1/2}、2^j=N^{−3}、N^{5/2}、≲_{α,ε}N^{1+ε}）、"split off" 段、Proof of Lemma 6.5（2^j≥N^{−3} 归约、立方 display 三重 substack 带 (i=0,1,2)）、"collinear iff" 段、(6.14) 叉积、(6.15) 三项分裂（λ_i∈ℚ 共线项 / (U₀,V₀,W₀)^T×(U₁,V₁,W₁)^T≠0 且 Δ=0 项 / Δ≠0 项）
- 结果：PASS±（3 处已修复）。全部公式与印刷逐项一致；print quirk 忠实保留："Consquently"（L1347，原刊拼写）。**修复 3 处**：L1355 "split of"→"split off"（印刷与 pdftotext 均为 split off；Luna 把此句记在 p.24 名下但实际印刷位置在 p.25）；L1363 "collinear if"→"collinear iff"（印刷 iff）；L1347 省略号后多余句点 `$. . .$. this`→`$. . .$ this`。残余瑕疵（不误导，不改）：L1353 "N^{1+ε}" 后缺句号。
- 备注：Luna 旧修复抽核**发现遗留缺陷**——"split of" 与 "collinear if" 两处少 f/少 f 均在 Luna 登记类似问题（p.24 名下）后仍残留（本次修复）。

## p.026（PDF p.26 / 印刷 p.26）
- PNG：audit-redo/p026.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：对角贡献段与 Û₀,Ŵ̂₀ 约化、双和 display（(Σ_{|y(Û₀+V̂₀α+Ŵ̂₀β)−τ′|<2^j, y∈ℤ} 1)² ≤ ΣΣ((2^{j+1}/|·|)²+1)）、|Û₀+V̂₀α+Ŵ̂₀β|⪰_{α,β}K⁴/N⁴、(6.16)、"This will suffice"、Lemma 6.6（m^T×c^T≠0 条件与 ≼_{α,β}2^jN⁴/K²+1）、Lemma 6.7 Σ₀ 定义与 ≼1+2^{3j}N^{12}/K³、"Inserting (6.16)" 链与 "from which we obtain" 链、"This proves the lemma."□
- 结果：PASS±（4 处已修复）。全部公式与印刷逐项一致。**修复 4 处**：L1378 第二 substack `(0.0,0)`→`(0,0,0)`（印刷为逗号，MD 句点笔误）；L1381 损毁的 ⪰ 构造（`\stackrel{}{\underset{}{ et{}{^-}}}` 等）→`\succeq_{\alpha,\beta} K^4/N^4`（印刷正常，此处为转录乱码）；L1387 "sufice"→"suffice"（印刷双 f）；L1421 "This proves the lemma." 后补 □（印刷右缘有结束方框，MD 缺失）。残余瑕疵：无新增。
- 备注：Luna 旧修复抽核通过——本页公式链（对角项、Lemma 6.6/6.7、两条插入链）与印刷逐式一致；乱码 ⪰ 为 Luna 链未清理的转录缺陷（本次修复）。

## p.027（PDF p.27 / 印刷 p.27）
- PNG：audit-redo/p027.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：§6.5 节标题、Lemma 6.6 证明（两结论、gcd 链、max_{h₂∼K} 求和、x₀/x′/c′ 归约、2^j/|h₂²(m₁+m₂α+m₃β)|+1、≼_{α,β}2^j|m|^{2+ε}/K²+1、□）、Lemma 6.7 证明（Borel-Cantelli 积分 display、(6.17) 2^{2j}|Δ|^{−1}、(6.18) H/G/T 定义、(6.19) gcd 比值 =H/G 与 T-bounds 行）
- 结果：PASS±（2 处已修复）。全部公式与印刷逐项一致。**修复 2 处**：L1459 "from which the claim follows." 后补 □（印刷右缘有结束方框）；L1464 Lemma 6.7 证明 display 中 `(i=0,1,2)` 原被放在 substack 之外成为求和后的孤立因子（印刷中它是下标条件 "U_i,V_i,W_i≲N²/K² (i=0,1,2)" 的组成部分）——已移入 substack，消除结构拆乱。残余瑕疵（不误导，不改）：L1425 "Suppose mx" 与 L1477 "and W" 的个别符号在数学环境外（印刷为同一行内公式，渲染等价）；L1437 "up to ≼ 1" 的 "to" 在数学环境内带空格（`\mathrm{t o}`，渲染近拟）。
- 备注：Luna 旧修复抽核通过——旧基线 p.27 无专项登记；本页 (i=0,1,2) 拆乱为 Luna 链未修复的结构缺陷（本次修复）。

## 本块小结（p.019–p.027 重做完成；非全篇总评）

- 覆盖：PDF p.19–p.27（印刷页码同），逐页 150dpi pngmono PNG 全览＋逐页 pdftotext 文本层对账（双通道主对账），1 处升级 300dpi 仲裁（p020 Δ=(A′B′−C′)/k² 印刷错字确认）。页界：p.19 起 |S|^{p/2−1} 计数论证，p.27 止 (6.19) 与 T-bounds 行；跨页段落按印刷页界归属（"heuristically" 段跨 p.23/24、三情况 bullet 跨 p.17/18 已在前块处理）。
- 页级结论：9 页全部 **PASS±**，0 FAIL。Theorem 5.1/6.1、Lemma 6.2–6.7、(6.1)–(6.19)、(6.16) 及各证明链与印刷逐式一致。
- 本次净修复 **21 处**（git 净 diff 19+/13−：13 行逐行修复 + 3 处 □ 各 +2 行；每处可溯源对应页 PNG/文本层证据）：
  - 词级/记号级（8）：L1049 β_i→β+逗号；L1111 **还原印刷错字** Δ=(A′B′−C′)/k²（原 MD 静默改正为 (C′)²）；L1287 diference→difference；L1355 split of→split off；L1363 collinear if→iff；L1387 sufice→suffice；L1378 (0.0,0)→(0,0,0)；L1307 \dot{U′}/\dot{V}/\stackrel{-}{\sim}→干净 ≲ 并补逗号。
  - 标点/定界（2）：L1067 全角逗号→半角；L1347 省略号后多余句点。
  - 乱码/结构（3）：L1381 损毁 ⪰ 构造→\succeq_{α,β}K⁴/N⁴；L1464 (i=0,1,2) 移回 substack；L1039 区 **误报核销**（(5.2) 闭合符被误判孤儿，经 HEAD 对照未做任何修改）。
  - 证明结束框（3 处补 □）：Theorem 5.1 证明末（L1061）、Lemma 6.6 证明末（L1423）、Lemma 6.7 前一证明末（L1459）——印刷均有右缘空心方框而 MD 缺失（Luna 链曾把方框存为控制字符，修复时整体删除而非替换）。
- print quirk 忠实保留："(ie i ≥ p/2," 无闭括号、Proposition (3.2) 带括号（前块）、"there are most O(N^ε)"、"Consquently"、"satisying"、L1275 原刊无逗号处（MD 添逗号已登记不改）、L1103 裸 Z、L1437 \mathrm{t o}。
- Luna 旧修复重核：9 页抽核通过，另发现其登记后仍残留的缺陷 5 处（p.19 □ 被删、p.24 点/横线残留、p.25 split of/collinear if、p.26 乱码 ⪰、p.27 (i=0,1,2) 拆乱）及 1 处静默改正（p.20 Δ），均已按纪律处理。
- 收尾只读清点：`$$` 定界行 490（偶）；`\tag` 51；C0 控制字符 0；HTML sub/sup 残留 0；1,789 行。MD SHA-256 = 83516511bf2493964979b79f88a8081857d2bcecab7f0fb2f633e2529d479138。git diff 40526b93..HEAD 逐行核对无计划外变更。
- 范围声明：本块只覆盖 p.19–p.27；p.28–p.34（含参考文献逐条与收稿日期）由后续块负责，本文件不对其作任何结论。证据图 10 张（p019–p027 全页 + p020 300dpi 裁片）已随页提交入库。
- **误判回滚登记**：p.010 初审曾把 (3.3c) 闭合 `$$`+空行+(3.3d) 开启 `$$` 误判为空 display 块删除，只读清点发现 `$$` 行数 489（奇）后当即恢复；该序列是逐式 display 的合法分隔。此误判与回滚均记录于 p.010 条目，最终 MD 不含该变更。
- Luna 旧修复重核：9 页逐页抽样全部通过，另发现两处 Luna 登记了但未修复的遗留缺陷（p.12 bullet、p.14 带波浪 p₁），均已在本次修复；Luna 的 print quirk 保留判断（Proposition (3.2) 带括号、focuse、dedending、staisfying、these s、S_μ 无绝对值、𝕋^d 上标）经 PNG 复核全部正确。
- print quirk 忠实保留：Proposition (3.2)（带括号）、we focuse、dedending、staisfying、restricted to these s、S_μ 无绝对值、p.12 末式 𝕋^d 与 Step 3 ‖F‖ 定义域 ℝ×𝕋^d（原刊自身 d/2 混用）、p.16 游离句点行（排印噪声，MD 合理省略）、"The cases … is zero is easier"。
- 收尾只读清点：`$$` 定界行 490（偶，回滚后复核）；`\tag` 51；C0 控制字符 0；1,783 行。git diff b9c67fc5..32829b97 基础上仅叠加本回滚（净变更 = 12 处修复行），无其他行变动。MD SHA-256 以最终提交为准（见本块末次 commit）。
- 范围声明：本块只覆盖 p.10–p.18；p.19–p.34 的重检与全篇总评、根级索引/进度由后续块与集成方负责，本文件不对其作任何结论。证据图 10 张（p010–p018 全页 + p012 300dpi 裁片）已随页提交入库。

## p.028（PDF p.28 / 印刷 p.28）
- PNG：audit-redo/p028.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p028_300dpi_delta.png ＋ pdftotext 文本层对账
- 核对：页顶 "In particular, if Δ≠0 then it follows from this that T>0 and H>0. Observe that"、Δ 展开大式（h₂² 因子＋括号内行栈＋Q(h₀,h₁,U₀,U₁,V₀,V₁,W₀,W₁)）、"for some triple of forms Q" 与 (6.18)(6.19) 满足假设句、三重 substack 计数式 ≲ 1+N²H/K²T+M/K²+N²HM/K⁴T+M²N²/T²K⁶、M/TK²≳1 段与 N²/K²(M/TK²)²=M²N²/T²K⁶、choices、M/TK²≪1 段、(h₁²V₁−h₀²V₀)U₂+(h₀²U₀−h₁²U₁)V₂ 式（尾逗号）、U₂ (mod ξ), ξ:= (h₀²U₀−h₁²U₁)/gcd(h₁²V₁−h₀²V₀, h₀²U₀−h₁²U₁) 式（尾句号）、|ξ|∼T/H 段、(M/K²+1)(N²H/K²T+1)≲1+N²H/K²T+M/K²+N²HM/K⁴T 链（尾句号）
- 结果：PASS±（1 处已修复）。Δ 展开式经 300dpi 仲裁（1x 裁片）确认印刷为 h₂² 后**三行**括号栈，MD 原 `\binom` 仅两行、漏第三行——**修复 1 处**：L1492 `\binom{两行}`→`\left(\begin{array}{c}三行\end{array}\right)`，补回 `(h_1^2 V_1 - h_0^2 V_0)U_2 + (h_0^2 U_0 - h_1^2 U_1)V_2`；栈内前两行、h₂² 因子与 Q(...) 实参逐项与印刷一致。计数式、假设句、ξ 残式与末端链全部逐项吻合，display 尾标点（，．）在位。print quirk 忠实保留："there is at most M/TK² choices"（is/are 原刊语法原样，MD 忠实）。残余瑕疵：无新增。
- 备注：Luna 旧修复抽核通过——Luna 基线登记的 "U₂ 的数字误设为罗马体" 在当前 MD（L1495/L1501 等 `U_2` 均为斜体数学环境）已不存在；Δ 展开式漏行属 Luna 登记范围之外的新发现缺陷（本次修复）。

## p.029（PDF p.29 / 印刷 p.29）
- PNG：audit-redo/p029.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p029_300dpi_sumattrib.png、p029_300dpi_preceq.png、p029_300dpi_v1line.png、p029_300dpi_endbox.png ＋ pdftotext 文本层对账
- 核对：页顶 "Clearly the same bound holds if we permute U,V and W in (6.18), and also if we put ∼ in place of the equalities in (6.18). Inserting this into (6.17) we find"、Σ₀(α,β) 大 display 全部七个 Σ 及其条件栈、2^{2j}M^{-1} 因子与尾句号、"Here we will explain the bound in the summation in (V₁,W₁)" 段（四个 gcd 的 ⪯1 choices）、ξ/gcd(ξ,h₁²)∼H/G 定义式、V₁ 残数论证段（at most GT/HK²+1）、η/gcd(η,h₁²) 定义式（η:=... 尾逗号）、"which is not less than H/G"、Maximising over G and M 两级 display（T²/(H^{1/2}K(H+K²)^{3/2}) 与 N²T^{3/2}/((T^{3/2}+K³)K³)+TN²/K⁵+T²/K⁴+N⁶/K^{10}+N²/K²+N⁶/T²K⁶）、T∈{1,K²,N²} 分情形、(N^{12}/K⁹+N^{14}/K^{15})2^{2j}≲N^{12}/K⁹2^{2j}≲N^{12}/K³2^{3j}、using the fact 行（含行尾句号与右缘 □）
- 结果：PASS±（4 处已修复）。**结构修复 2 处（同一 display 内条件归属，经 300dpi 裁片 sumattrib/preceq 确证）**：L1530 印刷中范围条件 1≤T≤N²; 1≤M≤T²; 1≤G≤K²; G≤H≤T 属于**第一个 Σ**（T,M,G,H∈2^ℤ 之下）而 MD 误挂到第二个 Σ（h₀,h₂∼K）名下——已归位；U₀≲N²/K² 印刷属第二个 Σ、gcd(h₁²,h₀²U₀)≳G 印刷属第三个 Σ（h₁∼K），MD 分别误挂到第三/第四个 Σ——已各归其位；同一 display 的 ≼-侧 Σ（N²K/G^{1/2}... 前）印刷同样带全部四条范围条件而 MD 漏挂——已补。**标点/结束框修复 2 处**：L1539 "at most$GT/HK²+1$" 后补句号（300dpi 裁片 v1line 确认印刷有）；L1565 "N^{1/2}≤K≤N" 后补句号并补行尾 □（Lemma 6.7 证明结束框，300dpi 裁片 endbox 确认印刷句号＋右缘空心方框）。其余公式、指数（12/14/15 均完整）、≻/≲/∼ 层次与文本逐项与印刷一致。print quirk 忠实保留："∼" 记号（put ∼ in place of the equalities）为原刊原样。残余瑕疵：无新增。
- 备注：Luna 旧修复抽核通过——Luna 基线登记的 "h₁²V₁ 上多出横线""12/14/15 指数拆字""(6.18) equalities 前的 ∼ 漏录" 三项在当前 MD（L1539/L1556–1562/L1527）均已不存在；Σ 条件错挂属 Luna 登记范围之外的新发现结构缺陷（本次修复）。

## p.030（PDF p.30 / 印刷 p.30）
- PNG：audit-redo/p030.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p030_300dpi_thm71.png、p030_300dpi_omega.png ＋ pdftotext 文本层对账
- 核对：§6.6 run-in 标题（黑体 "6.6." ＋斜体 "Completing the case p = 8."）与 (6.7)+(6.9)+(6.11) 组合式 ‖e^{itΔ̃}f‖⁸_{L⁸([0,T]×𝕋²)} ≲ |S⁴|((NT+N)+(N³+NT)+(N⁴+NT))、"which proves the case p = 8 of Theorem 6.1."、§7 节标题（p = 10）、Theorem 7.1 引言行与 ‖·‖¹⁰_{L¹⁰([0,T]×𝕋²)} ≲ |S⁵|(N⁶+TN²) 式、"This implies Theorem 1.2 for p = 10."、(6.3) 引入句、‖·‖¹⁰_{L^p([0,T])} ≲ Σ2^{-j}|S⁵|sup Σ |Ω^{5,N,+}_{a,b,A₁,B₁,C₁}| display、Ω 定义句、五方程组 display（Σ_{i=1}^5 k_i=a 等，尾句号）、Over ℚ 等价句与平方配凑 display（= (x₁+x₂+x₄/2)²+(x₂+x₃+x₄/2)²+(x₁+x₃+x₄/2)²+5(x₄/2)²，尾句号）、Σk²+5k₄²=A′ 三方程 display、两级 ≲/≼ display（内层 Σμ²+5μ₄²=A′ 与 Σμ²=A′−5x² 两套 substack、末尾 "1."）、首个退化情形段与 Σ_{(m,x,y)}Σ_{(μ_i)}1 ≼ (2^jN⁴+1)N 式（尾逗号）
- 结果：PASS±（2 处已修复）。**修复 2 处**：L1579 Theorem 7.1 引言行 "Generically in$(α_{ij})$" 后补逗号（300dpi 裁片 thm71 确认印刷为 "Generically in (α_{ij}),"）；L1590 display 末 |\Omega_{a,b,A₁,B₁,C₁}^{5,N,+} 补闭合竖线 "|"（300dpi 裁片 omega 确认印刷竖线成对）。其余全部公式、指数、编号与文本逐项与印刷一致。print quirk 忠实保留：**L^p([0,T]) 记号**——该 display（L1590）印刷 norms 下标确为 L^p（而 Theorem 7.1 式与下式均为 L^{10}），系原刊自身混用（Luna 亦登记为印刷原样），MD 忠实保留不改；MD L1570 的 \tilde（他处 \widetilde）帽宽渲染差异同 p.5 L209 先例登记不改。残余瑕疵（不误导，不改）：L1599 行内长式被 MD 拆为两个相邻数学串（印刷为同一行内公式，渲染等价）；§6.6 run-in 标题未如 §1.3/§3.4 被 MinerU 升级为 `##`（本次内容无损，仅记录 MinerU 行为不一致）。
- 备注：Luna 旧修复抽核通过——Luna 基线登记的 "p=10 数字拆字" 在当前 MD（L1575/L1585）已不存在；其对 L^p([0,T]) "按 PDF 印刷原样保留" 的判断经页图复核正确；Theorem 7.1 尾逗号与 |Ω| 闭合竖线属 Luna 登记范围之外的新发现缺陷（本次修复）。

## p.031（PDF p.31 / 印刷 p.31）
- PNG：audit-redo/p031.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p031_300dpi_neq0.png、p031_300dpi_gzintegral.png ＋ pdftotext 文本层对账
- 核对：Diophantine 条件句（|i+jα+kβ| ≳ N⁻⁴ if i,j,k ≲ N², with (i,j,k)≠(0,0,0). This is more than satisfactory.）、"Next we consider" 段（(Σµ²)(Σλ²)=(Σµλ)²≠0. In this case…µᵢ=pzᵢ, λᵢ=qzᵢ）、三重 Σ 计数 display（Σ_{A′,B′,C′}Σ_{mp²+5x²=A′,…}Σ_{Σzᵢ²=m}1 ≲ (2^jN⁴+1)N sup|{(m,p,q,x,y):…}|，尾句号）、"We claim the last supremum is ≲ N" 段（choose x arbitrarily、divisor bound、(q,y) ellipse∩line、≲ (2^jN⁴+1)N² as desired）、"Finally we treat the case 0≠(Σµ²)(Σλ²)≠(Σµλ)². By Pall" 句、Pall 贡献 display（内层条件为**无撇 A,B,C**——印刷原样，MD 忠实）、"We get" 与 |{(U,V,W,x,y):…}| ≼ N²/h² display、"by choosing the values of W and xy" 段（xy=0, x=0 → (U,W) uniquely fixed）、Σ…h ≼ (2^jN⁴+1)N² display、"and we're done."、Appendix A 节标题、Guo–Zhang 定理引入句与大 display、right-hand side 句（≲ N^ε(N^{ds}+N^{2ds−d(d+2)})）、Z(M) 定义 display（尾逗号）
- 结果：PASS±（2 处已修复）。**修复 2 处**：L1625 `\ne 0 .$.` 双句点→`\ne 0$.`（300dpi 裁片 neq0 确认印刷为单句点 "≠ 0. In this case"）；**L1658 结构修复**——印刷中 "0≤βᵢ≤1; 0≤αᵢⱼ≤1" 是 ∫⋯∫ 的下标（左下）而 MD 误将其挂为外层 Σ 的下标并多出一道 `\Big|` 竖线（300dpi 裁片 gzintegral 确证：∫⋯∫ 带条件下标、Σ 下标为 x∈ℤ^d/|x|≤M、|·|^{2s} 单对竖线）——已改为 `\int_{\substack{0\leq\beta_i\leq1\\0\leq\alpha_{ij}\leq1}}\dots\int\bigg|\sum_{\substack{x\in\mathbb{Z}^d\\|x|\leq M}}e(...)\bigg|^{2s}…`，多余 `\Big|` 一并清除。其余公式、指数、编号与文本逐项与印刷一致。print quirk 忠实保留：Pall 贡献 display 内层条件用无撇 A,B,C（外层求和为 A′,B′,C′），系原刊记号原样，MD 与印刷一致不改。残余瑕疵：无新增。
- 备注：Luna 旧修复抽核通过——Luna 基线登记的 "Σzᵢ²=m 损坏、β 多出帽、if/is/get 标记损坏" 在当前 MD（L1628/L1623/L1631）均已不存在；∫ 下标错挂属 Luna 登记范围之外的新发现结构缺陷（本次修复）。

## p.032（PDF p.32 / 印刷 p.32）
- PNG：audit-redo/p032.png（pngmono 150dpi）＋ 300dpi 仲裁裁片 audit-redo/p032_300dpi_xiline.png、p032_300dpi_A2.png、p032_300dpi_A3.png、p032_300dpi_Asub.png ＋ pdftotext 文本层对账
- 核对："then we have"、(A.1)（Z(M) ≲_ε M^{ds+d+ε}+M^{2ds−d(d+1)+ε}.，尾句号与标签）、"Indeed this follows…values of Σ^{2s}_{i=1}(−1)^i x^{(i)}." 行、(A.2)（I_s(T) ≲_α N^εT^ε ∫_{1≤αij≤2}⋯∫ I_s(T) dα₁₁⋯dα_{dd}，尾逗号）、"by estimating the measure…form 2^k. For T≥2" 句、(A.3)（≍ N^εT^{1+ε} ∫_{0≤αij≤1}⋯∫ sup_{x∈**T**^d}|K_N^{(d)}(1,x)|^{2s} dα…，尾逗号）、"1-periodic in each α_{ij}" 句、|K_N^{(d)}(1,x)|² ≼ N^d[#\{n∈[−4N,4N]^d s.t. ‖L_j(n)‖<2/N\}+1] display、exponenetial 段（|K_N^{(d)}(0,0)|²、(3.2)）、≲ N^d Σ_{w,n} e^{−2/N²|n|²−N²/8|w−4(αij)n|²} display、Poisson summation 句与 = 2^d Σ_{n,m} e^{−…}e(−4Σαij n_im_j) display、换元 x=n−m,y=n+m 句、sup_{x∈**T**^d}|K_N^{(d)}(1,x)|² ≼ Σ_{x≡y (2)} e^{−…}e(Σαij x_ix_j−Σαij y_iy_j) display、"Substituting this into (A.3)" 与 I_s(T) ≼_α T Σ_{两行 substack}e^{−Σ…} ≲ TΣ_{M∈2^ℤ;M>N}e^{−M²/N²}Z(M) display、"This together with (A.1) proves (1.10)."、末段（ds+d→ds、square-root cancellation heuristic、intepret、ȳ^{(i)} 超曲面、dim V、Franke-Manin-Tschinkel [17]）
- 结果：PASS±（2 处已修复）。**修复 2 处**：L1673 行内式 `$x^{(i)}$` 后补句号（300dpi 裁片 xiline 确认印刷为 "x^{(i)}. We will deduce"）；**L1684 (A.3) 结构修复**——印刷中 "x∈**T**^d" 只是 sup 的下标、积分 ∫⋯∫ 组仅带 "0≤αij≤1" 条件（300dpi 裁片 A3 确证），MD 在末 ∫ 上多出 `_{x \in \mathbf{T}^d}` 下标——已删除，现为 `\int_{0\leq\alpha_{ij}\leq1}\dots\int\sup_{x\in\mathbf{T}^d}`。其余公式、指数、(A.1)(A.2)(A.3) 标签与文本逐项与印刷一致。print quirk 忠实保留：**(A.2) 被积项印为 I_s(T)**（300dpi 裁片 A2 确认印刷即如此，疑原刊笔误但按纪律原样保留；同一式内 ≲_α 与积分下标 1≤αij≤2 位置经同裁片核对与 MD 一致）；"exponenetial"（L1693）与 "intepret"（L1719）为原刊拼写原样（Luna 同判，页图复核确认）；\mathbf{T}^d 与全文 𝕋/\mathbf{T} 混用同前块登记。残余瑕疵：无新增。
- 备注：Luna 旧修复抽核通过——Luna 基线登记的 "dim V 后多出冒号" 在当前 MD（L1719 "Given dim$V$, we can count"）已不存在；其 "exponenetial、intepret 是印刷原样" 的判断经页图复核正确；末 ∫ 多余下标与 x^{(i)} 后缺句号属 Luna 登记范围之外的新发现缺陷（本次修复）。
