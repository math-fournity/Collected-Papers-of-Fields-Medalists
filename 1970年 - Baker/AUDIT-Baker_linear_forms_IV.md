# AUDIT — A. Baker《Linear forms in the logarithms of algebraic numbers (IV)》（Mathematika 15 (1968), 204–216；Cambridge Core 扫描件，BFO 重打包）

> mineru: standard 档云端解析（OCR，文本层不可靠）；审计依据 = `audit/baker4_pNNN.png`
> （pngmono 150dpi 全 13 页目检）+ 300dpi 仲裁（p.6/p.13）。参数体系：A/d/δ/H（无 κ）。

## p.001（印刷 p.204）
- 核对：题录（Mathematika 15 (1968)）✓；§1（实用动机/[4,5,6,7]/A⩾4、d⩾4、0<δ⩽1/
  principal values）✓；**Theorem**：(1) 0<|Σbᵢlogαᵢ|<e^{−δH} ⇒ (2) H<(4^{n²}δ^{−1}d^{2n}log A)^{(2n+1)²} ✓；
  Davenport 合作应用（3x²−2=y²、8x²−7=z² → x=1、x=11）✓
- 结果：**PASS±**（±：页眉/页脚未收）
## p.002–p.004（印刷 p.205–207）
- 核对：§2 Preliminaries (3)(4)、|α−1| 界 ✓；条件 (i)(ii)(iii)/k 最小选择/b‴ 构造 ✓；
  (7) H⩾(4^{n′²−½}δ^{−1}d^{2n′}log A)^{(2n+1)²} ✓；(8)(9) ✓；k/h/L 定义 (10)(11)(12) ✓；
  D=dⁿ、f_m 定义 ✓；Lemma 1（See [1]）✓；Lemma 2 (13)(14)(15)、v(λ,s)、U=(2A)^{nLDh}(2LH^{n′})^k ✓
- 结果：**PASS±**（±：页眉/页码未收）
## p.005（印刷 p.208）
- 核对：N>k^{n(2n−1)/(2n+1)}=k^{n−1+1/(2n+1)}⩾h²k^{n−1}>2ⁿD²hk^{n−1}>2M ✓；
  (2A)^{LDh}⩽(2A)^{nDk/h³}<e^{**δhk**}（print δhk；**md "1/40 hk" → FAIL**）；(16)
  (2LH^{n′})^k<(2h)^{(2n′+1)³k}<e^{**⅒?**…}——print (16) 末为 e^{⅒?}（分数形态与 md 19/20 一致，
  150dpi 分辨存疑但与 (16) 家族自洽）✓；19/20 x−(2n′+1)³log(2x) 函数论证/f(y) 及导数 ✓；
  "Since also N<k^n<e^{**δhk**}, NU<e^{hk}"（**md 1/40 → FAIL**）；(14)⇒(13)（P 因子 (17)、
  (4dA)^{2Ll}e^{−δH}、(4dA)^{n(k+Ll)}(2LH^{n′})^k、5hk<5H^{1/2}<½δH）✓
- 结果：**FAIL（两点）**：δhk 误读 ×2。
## p.006（印刷 p.209）
- 核对：Lemma 3 (18)(19)、q(λ,z)、(dA)^{4L|z|}/(dA)^{5L|z|}、|Pq(λ,z)|<(dA)^{(4n+1)L|z|}{4e^{19/20 h}
  log(dA)}^{…}（19/20 与 (16) 自洽 ✓）、k^n<e^{**δhk**}（**md 1/δ → FAIL**）、4log(dA)<e^{**δh**}
  （**md 1/δ → FAIL**）、Q/P′/共轭界 (L+1)^n(dA)^{2nLl}e^{2hk}、|Q|⩾{e^{2hk}(dA)^{2nLl}}^{−D+1}、
  |q(λ,l)−q′(λ,l)|<(4dA)^{(n+2)Ll}e^{hk−δH}、(20) Ll⩽k^{2n(n+1)/(2n+1)}⩽H^{1−1/(2n+1)²}、
  e^{−¾δH}/e^{−⅝δH}、|P′|、|P|⩾(2dA)^{−(d+4)k}>e^{−hk}、|PP′^{−1}Q|、e^{2Dhk} 与 (dA)^{2nDLl}
  不超过 e^{½δH}、2e^{−½δH}、|P|⩽(4log(dA))^k<e^{⅛δH} ✓ 全部逐式吻合
- 结果：**FAIL（两点）**：1/δ→δ ×2。
## p.007–p.008（印刷 p.210–211）
- 核对：Lemma 4（J<½n(4n−1)、R₀=Dh、S₀=k、R_J/S_J、(21)(22)、f_m(r) 求值说明完整、
  F(z)、Γ 半径 R_{K+1}h、(23)）✓；(24) k^{(4n²+3n+1)/(4n+2)}⩽H^{1−n/(2n+1)²} ✓；
  双和界 <H(8n)^ke^{−½δH}<e^{−¼δH} ✓；(25) ✓；R_{K+1}⩽k^{(4n²−n+1)/(4n+2)} ✓；
  (26) |F(l)|<H^{R_K(S_{K+1}+1)}<e^{⅛δH} ✓；(27) H^{n/(2n+1)²}>8δ^{−1}logH ✓；
  h>8δ^{−1}、H^{1/(2n+1)²}⩾h>logH ✓；e^{2Dhk}/(dA)^{4nDLl} 不超 e^{1/16δH}、
  |f(l)|>2e^{−⅛δH}、|f(l)/F(l)|>2e^{−¼δH} ✓；θ=upper|f|/Θ=lower|F|、(28) 4θ|F(l)|>Θ|f(l)| ✓；
  Θ⩾(½R_{K+1}h)^{…}、θ⩽e^{2hk}(dA)^{5nLR_{K+1}h}、Θ|F(l)|^{−1}⩾(½h)^{…}、
  θ|f(l)|^{−1}⩽{e^{2hk}(dA)^{5nLR_{K+1}h}}^{D+1} ✓
- 结果：**PASS±**（±：R_{**K**} 粗体 K 一处（p.8 底段 print 正体）→ **FAIL（单点，minor）**）
## p.009–p.010（印刷 p.212–213）
- 核对：(28) 推出 log4+(D+1){2hk+5nLR_{K+1}h log(dA)}⩾R_K(S_{K+1}+1)log(½h) ✓；K=0/K>0
  两情形（log(½h)>log(2⁵d⁴)>9、2^{−(K+1)}kR_K log(½h)、R_K⩾8/9·k^{(2K+1)/(4n+2)}、
  2^{−K+2}hk^{1+K/(2n+1)}>4D²k^{1+K/(2n+1)}logA、log4+2hk(D+1)<4Dhk⩽¼D²k^{1+K/(2n+1)}、
  5n(D+1)log(dA)⩽5×17/16·nD(logd+logA)⩽6D²(½+⅛logA)<15/4·D²logA）✓；**Lemma 5** (29)
  −2^{−½n(4n−1)}k^{n(4n+3)/(4n+2)} ✓；X/Y 定义、(30)、E(z)、(31)(32)、ξ/Ξ、
  |φ(w)|⩽2e^{2hk}(dA)^{5nLXh}(¼h)^{−X(Y+1)}+(2X)^{2XY}e^{−¼δH} ✓；2XY log(2X)<⅛δH ✓；
  L⩽kh^{−4}/X>k/Y+1>…、e^{½X(Y+1)} ✓；|φ(w)|<(1/16·h)^{−X(Y+1)}+e^{−⅛δH}、
  h^{X(Y+1)}<e^{½δH}、h^½>32 ✓；φ_j(0)=j!/2πi∫、|φ_j(0)|<j!4^jh^{−½X(Y+1)} ✓；
  **j!4^j⩽(4j)^j⩽(4k)^{nkn}⩽e^{2nkn log k}**——print 指数 "nk^n"（j⩽kⁿ 代入），
  **md "nkn" 漏幂 → FAIL ×2**
- 结果：**FAIL（两点）**：(4k)^{nkn}→(4k)^{nk^{n}}、e^{2nkn log k}→e^{2nk^{n} log k}。
## p.011–p.012（印刷 p.214–215）
- 核对：8n(2n+1)kⁿ log h、X(Y+1)>2^{−½n(4n−1)−1}k^{n(4n+3)/(4n+2)}、X(Y+1)>8hkⁿ、
  h>(2n+1)³log h、j!4^j<e^{¼X(Y+1)}、|φ_j(0)|<h^{−¼X(Y+1)}、log h>9 ✓；**Lemma 6**
  （W=0 或 |W|>(dA)^{−4nDT}、α_j^{−1} 替换、|ω|⩽|W|e^{|W|}A^{nT}）✓；§4 Proof（R=(L+1)ⁿ−1、
  r 的 (L+1) 进制、p_r/ψ_r/Ψ_j、φ_j(0) 展开、|ψ_r|<4nL log(dA)、(16nL log(dA))^R e^{−δH}、
  k^R e^{−δH}、(R+1)k^R⩽(2k)^R⩽e^{2kn log k}、H⩾k^{n+½}、k^½⩾h^{2n+1}、|φ_j(0)−Ψ_j|<e^{−½δH}、
  **(33)** log|Ψ_j|<−2^{−½n(4n−1)−1}k^{n(4n+3)/(4n+2)} ✓、**(34)** p_rΔ_r(ψ_r)=Σσ_{r,j}Ψ_j、
  Δ_r(x)=∏(x−ψ_s)=σ_{r,0}+…、L⩽k^{1−ε}<H、|ψ_r−ψ_s|>(dA)^{−4nDL}、R<(2L)ⁿ、
  **(35)** log|Δ_r(ψ_r)|>−2^{2n+2}Dk^{(n+1)(2n−1)/(2n+1)}log(dA) ✓、|σ_{r,j}|⩽∏(1+|ψ_s|)、
  (2k)^R、log|p_rΔ_r(ψ_r)|⩽… ✓
- 结果：**PASS±**（±：页眉/页码未收）
## p.013（印刷 p.216）
- 核对：log|Δ_r(ψ_r)|⩽−2^{−½n(4n−1)−2}…、(35)⇒k^{(n+2)/(4n+2)}<2^{2n²+3n/2+4}D log(dA)、
  与 (12) 矛盾收尾 ✓；**References [1]-[7] 逐条**（(I)(II)(III)/Phil. Trans. 263 (1968) 两篇/
  J. London Math. Soc. 43 (1968)（Mordell 80th birthday 献词）/Proc. Cambridge Phil. Soc. To appear）
  ✓；Trinity College, Cambridge ✓
- 结果：**FAIL（单点）**：**(Received on the 12th of June, 1968.)** 收稿行丢失。

## 总评

- **覆盖声明**：13/13 页逐页目检（150dpi 全页）+ 300dpi 抽样（p.6/p.13）。本篇 md 质量显著
  优于 (II)(III)（OCR 噪声低），伪影集中为 **δ 字形误读族**（δ→"1/40"/"1/δ" ×4）与一处漏幂。
- **FAIL 清单（8 点）**：δhk 误读 ×4（e^{1/40hk}×2、e^{1/δhk}、e^{1/δh}）；(4k)^{nkn}→(4k)^{nkⁿ}
  与 e^{2nkn log k}→e^{2nkⁿ log k}（同式两处）；R_{**K**}→R_K；Received 行丢失。
- **源级 quirk（忠实不改）**：无新发现（"rôle" 等拼写正常）。
- **可用性结论**：修复后 md 可作该文忠实底本。(I)–(IV) 四篇正文审计链完整。
