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
