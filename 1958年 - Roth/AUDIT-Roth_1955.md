# AUDIT — K. F. Roth《Rational approximations to algebraic numbers》（Mathematika 2 (1955), 1-20，300dpi CCITT 扫描件 + Cambridge Core OCR 文本层，20p）

> mineru: standard 档云端解析（自行 OCR，质量高）。**审计依据 = `audit/roth1955_pNNN.png`
> （pngmono 150dpi 全 20 页）+ 300dpi 局部放大 5 处终裁**；pdftotext 文本层 prose 可靠、
> 数学式系统性乱码（仅作 prose 对账与定位，数学式以 PNG 为准）。
> **伪影族**：指数 κ→n、δ²→δ³、½δr₁→(1/δ)δr₁、1+2δ→1+2⁵、k^{p−1}→k^p−1 ×2、幽灵页脚注 ×4、
> Lemma 8 版式乱序、页尾 catchword "Q" 误入正文、Dyson 脚注标记 †→‡。

## p.001（print 1：刊头 + §1 引言）
- 核对：MATHEMATIKA 刊头/Vol. 2 Part 1 June 1955 No. 3 ✓；Liouville 1844/|α−h/q|>A/qⁿ ✓；
  Thue ½n+1/Siegel s+n/(s+1)/Dyson κ⩽√(2n) ✓；Siegel 猜想 κ⩽2 ✓；脚注 † Davenport The Higher
  Arithmetic 165-167 ✓、**‡** Acta Mathematica 79 (1947) 225-240（md "†" → FAIL 已修）✓；
  [MATHEMATIKA 2 (1955), 1-20] 页脚（惯例未收）；Cambridge Core 下载横幅（非内容）
- 结果：**PASS±**（±：脚注标记已修；页脚未收）
## p.002（print 2：THEOREM + 丢番图方程应用 + 推广）
- 核对：THEOREM κ⩽2 ✓；κ=2 最佳 ✓；**|f(x,y)|<(|x|+|y|)^{n−κ}**（md "n−n" → FAIL 已修）✓；
  g 全次数 ⩽n−3/f=g 有限解 ✓；Thue-Siegel-Dyson/Siegel 基本memoir ✓；推广 |α−β|<(H(β))^{-κ}
  次数 g/κ⩽2g/H(β) 定义 ✓；Davenport 致谢 ✓；脚注 † Skolem/‡ Math. Zeitschrift ✓
- 结果：**FAIL（单点）→已修**
## p.003（print 3：Schneider 引 + §2 Wronskian）
- 核对：Lemma 8 归功 Davenport ✓；Wronskian det(1/μ! d^μ/dx^μ φ_ν) ✓；线性相关判据 ✓；
  Δ=(1/i₁!…i_p!)(∂/∂x₁)^{i₁}…(2) ✓；广义 Wronskian G=det(Δ_μφ_ν) ✓；converse§ ✓；
  脚注 † Crelle 175 (1936) 182-192/‡ Siegel Math. Annalen 84 + Kellogg/§ It should perhaps... ✓；
  **md 幽灵脚注 "κ⩽2"（print 无）→ 已删**
- 结果：**FAIL（幽灵脚注）→已修**
## p.004（print 4：Lemma 1 + 证明前半）
- 核对：Lemma 1 ✓；(3) φ_ν(t,t^k,…,t^{k^{p−1}}) ✓；b^{(ν)} 展开/唯一性 ✓；恒等式链条 ✓；
  W(t) det (4) ✓；d/dt 展开 ✓；**"replaced by t,…,t^{k^{p−1}}"**（md k^p−1 → FAIL 已修）✓；
  (d/dt)^μ=f₁Δ^{(1)}+… ✓
- 结果：**FAIL（单点）→已修**
## p.005（print 5：W 分解 + §3 Lemma 2）
- 核对：W(t)=g₁G^{(1)}+…+g_sG^{(s)} ✓；**G^{(i)}(t,t^k,…,t^{k^{p−1}})**（md k^p−1 → FAIL 已修）✓；
  a fortiori ✓；Lemma 2 全文（(5)(6)(7)/U 次数 lrⱼ/V 次数 lr_p）✓；证明：表示选取/least l/φ 线性无关/
  d₀..d_{l−2} ✓
- 结果：**FAIL（单点）→已修**
## p.006（print 6：Lemma 2 证明后半）
- 核对：ψ 线性无关/1⩽l⩽r_p+1 ✓；W(x_p)/G 行乘行列式 GW=…=F ✓；F=WG ✓；有理数 g/U=gG/V=g^{-1}W ✓；
  次数论证 ✓；脚注 † Perron Algebra I Satz 88（"between G and W"——print 即 G）✓
- 结果：**PASS**
## p.007（print 7：Lemma 3 + §4 index 定义）
- 核对：Lemma 3 界 ((r₁+1)…(r_p+1))^l l!B^l 2^{(r₁+…+r_p)l} ✓；证明（展开/binom 系数/A⩽2^{s}）✓；
  index θ 定义/展开/θ=min(j/r) ✓
- 结果：**PASS**
## p.008（print 8：index 性质 + Lemma 4 + §5 𝓡ₘ）
- 核对：导数条件/θ⩾0/导多项式 index 下界 ✓；Lemma 4 (8)(9)+末句 ✓；§5 (a)(b)(c)/𝓡_m ✓；
  (hⱼ,qⱼ)=1/θ(R)/(10) Θ_m 上界 ✓
- 结果：**PASS**
## p.009（print 9：double significance + Lemma 5 + Lemma 6 头）
- 核对：m=1 简单情形 ✓；Lemma 5 (11) log B/(r₁log q₁) ✓；证明 (q₁x₁−h₁)^{θr₁}/Gauss/q₁^{θr₁}⩽B ✓；
  [It may be noted…] ✓；**脚注 † The exponent θr₁ is of course…**（md 幽灵 "θr₁" 条目 → 已删）✓；
  Lemma 6 (12)(13)(14) ✓
- 结果：**FAIL（幽灵脚注）→已修**
## p.010（print 10：(15)(16) + Lemma 6 证明前半）
- 核对：Φ/M 定义 ✓；Lemma 3 界 <M/r₁>r₂>…>r_p ✓；F=UV/系数 <M ✓；𝓡_{p−1}/Θ_{p−1}/lΘ/lΘ₁ ✓；
  (17) index F⩽lΦ ✓
- 结果：**PASS**
## p.011（print 11：Lemma 6 证明后半）
- 核对：Δ 算子/index 下界 θ−…/w/r_{p−1}<δ ✓；max(0,θ−ν/r_p)−δ ✓；典型项 ±(Δ_{μ₀}R)… ✓；
  Σmax−lδ ✓；θr_p>10/θ⩽10r_p^{-1}<δ<2δ^{1/2} ✓；θr_p<l 与 ⩾l 两情形（½[θr_p]²/⅓r_pθ²、½lθ）✓
- 结果：**PASS**
## p.012（print 12：(18) + Lemma 7 (19)-(23) + 证明开头）
- 核对：(18)/min⩽l(Φ+δ)/两分支/r_p+1<4/3r_p/θ<2(Φ^{1/2}+δ^{1/2}) ✓；(19)-(23) ✓；
  m=1 情形 δ⩽10δ^{1/2} ✓；归纳设定 ✓；M 估计链（2^{(2p+1)r₁}/e^{…}）✓
- 结果：**PASS**
## p.013（print 13：Lemma 7 证明后半 + §6 Lemma 8 陈述）
- 核对：(24) δ₁=δ(1+p^{-1})/(25)(26) ✓；log(q₁^{δ₁lr₁})/(lr_p log q_p)⩽δ₁ ✓；δ₁<(p−1)^{-1} ✓；
  Φ<3(10^{p−1}δ^{(1/2)^{p−1}}) ✓；(13) 三行链 <10^pδ^{(1/2)^p} ✓；Lemma 8：**不等式行与
  "does not exceed 2m^{1/2}λ^{-1}(r₁+1)…(rₘ+1)." 版式**（md 乱序+"xceed" 断词 → FAIL 已修）✓
- 结果：**FAIL（版式）→已修**
## p.014（print 14：Lemma 8 证明 + §7 开头）
- 核对：m=1 ✓；λ⩽2m^{1/2} 平凡/λ'=λ−1+2jₘ/rₘ/λ'>0 ✓；归纳和 ✓；j 归一和 ✓；r 偶数替换
  （λ+2k/r）^{-1} 三行链 ⩽(r+1)λ^{-1}(1−λ^{-2})^{-1} ✓；1−λ^{-2}>1−¼m^{-1}>(1−m^{-1})^{1/2} ✓；
  脚注 † The case of even r…in §8…（md 幽灵 "§8"、"$r₁,…,rₘ$" 条目 → 已删）✓；
  |Mα−h'/q|<M/q^κ ✓
- 结果：**FAIL（幽灵脚注 ×2）→已修**
## p.015（print 15：(27)(28) + 条件 (29)-(33) + λ γ η B₁ + Lemma 9 头）
- 核对：(27) f(x)=xⁿ+a₁x^{n−1}+…+aₙ/(28) A ✓；(29)-(33) 全部 ✓（(30)(31)(32)(33) 逐项）✓；
  (29)+(32)⇒δlog q₁>m(2m+1) ✓；(34)-(37) ✓；(38) η<γ ✓；
  **"r₁>10 and q₁^{δ²}>e^{2m+1}⩾e³. Thus, in particular, q₁^{½δr₁}<B₁."**
  （300dpi 终裁：δ² 非 δ³（FAIL 已修）；**½**δr₁ 非 (1/δ)δr₁（FAIL 已修）；"<" 方向与 "r₁>10"
  print 即此，忠实）✓；Lemma 9 (i)(ii) ✓
- 结果：**FAIL（两点）→已修**
## p.016（print 16：Lemma 9 (iii) + 证明前半）
- 核对：(iii) Q_{i₁…i_m}/(39) <B₁^{1+3δ} ✓；(40)-(43) N=(B₁+1)^r/r=(r₁+1)…(rₘ+1) ✓；
  (44)(45) D⩽2m^{1/2}λ^{-1}r ✓；W_j(x,…,x)/T_j(W;x)/次数 n−1 ✓；2^{r₁+…+r_m}B₁<B₁^{1+δ} ✓
- 结果：**PASS**
## p.017（print 17：系数估计 + 抽屉原理 + W* 构造）
- 核对：mr₁log2<½δ²r₁log q₁ ✓；rB₁^{1+δ}<B₁^{1+2δ} ✓；除法步骤 w_v−a_{s−v}w_s ✓；
  **(1+A)B₁^{1+2δ}**（md "1+2⁵" → FAIL 已修）✓；(1+A)^{s−n+1}B₁^{1+2δ}/(1+A)^{mr₁}B₁^{1+2δ}<B₁^{1+3δ} ✓；
  (1+2B₁^{1+3δ})^{nD}/(1+3δ)nD=½r/(2+2B₁)^{r/2}<(1+B₁)^r ✓；W'/W''/W*=W'−W''/index⩾γ/系数⩽B₁ ✓；
  **页尾 catchword 小字符**（print 装订标记，非正文；md 误入独立段 "Q" → 已删）
- 结果：**FAIL（两点）→已修**
## p.018（print 18：Lemma 9 证明收尾 + §8 Completion 开头）
- 核对：(a)(b)(c) of §5/𝓡ₘ(q₁^{δr₁};…)/Lemma 7 index<η ✓；Q 定义/k₁/r₁+…<η/Q(h/q)≠0 ✓；
  index⩾γ−η/(i)(ii) ✓；2^{mr₁}B₁^{1+δ}<B₁^{1+2δ}/|Q_i(α)|<B₁^{1+2δ}(1+|α|)^{Σr}/(1+|α|)^{mr₁}<B₁^δ ✓；
  §8：(46)/(h,q)=1/m>4nm^{1/2}/(47) ✓；m−4(1+3δ)nm^{1/2}−2η>0 ✓
- 结果：**PASS**
## p.019（print 19：(48)-(53) + 矛盾比较开头）
- 核对：(48)/(49) 等价 ✓；(50) log qⱼ/log q_{j−1}>2/δ ✓；(51)(52)(53) ✓；(31) 验证 ✓；
  Lemma 9 应用/(54) |Q|⩾q₁^{-r₁}…>q₁^{-mr₁(1+δ)} ✓；Taylor 展开式 ✓
- 结果：**PASS**
## p.020（print 20：矛盾完成 + 收尾）
- 核对：(i) 零化/|(h/q−α)^{i}|<1/(q^{i})^κ⩽q₁^{-r₁(γ−η)κ}/qⱼ⩾q₁^{r₁/rⱼ} ✓；三行链
  <q₁^{(1+4δ)δr₁−r₁(γ−η)κ} ✓；与 (54) 比较/κ<[m(1+δ)+δ(1+4δ)]/(γ−η)<m(1+4δ)/(γ−η) contra (49) ✓；
  University College, London ✓；**(Received 26th January, 1955. ; §1 revised 20th May, 1955)**
  （300dpi 终裁：**26th**——md 正确，150dpi 误读 20th）✓
- 结果：**PASS±**（±：Received 行 md 已有且正确）

## 总评

- **覆盖声明**：20/20 页逐页目检（150dpi 全页）+ 300dpi 局部放大 5 处终裁；Cambridge Core OCR
  文本层 prose 可靠（用于逐句 prose 对账），数学式以 PNG 为准。
- **FAIL 修复（11 组）**：①指数 κ 丢字：(|x|+|y|)^{n−κ}（"n−n"）；②B₁ 段 q₁^{δ²}（δ³）与
  q₁^{½δr₁}（(1/δ)δr₁）；③除法段 B₁^{1+2δ}（"1+2⁵"）；④t^{k^{p−1}} ×2（k^p−1）；
  ⑤Lemma 8 版式乱序（"xceed" 断词+does not exceed 错位）重组；⑥幽灵页脚注 ×4（κ⩽2/θr₁/§8/
  r₁,…,rₘ——print 脚注区均无此四条）；⑦p.17 页尾 catchword "Q" 误入正文段（删除）；
  ⑧Dyson 脚注标记 †→‡。fix commit 见 `git log --grep 'fix(md): Roth 1955'`。
- **源级 quirk 清单（忠实不改）**：Korollar…"r₁>10"（非 10δ^{-1}，300dpi 确认）；q₁^{½δr₁}<B₁
  的 "<" 方向（print 即此）；Received 26th January（300dpi 确认，md 正确）；⟨x 与 OCR 层的
  "xceed" 系 mineru 断词而非 print。
- **150dpi 证伪记录**：Received "20th"→实为 26th；p17 catchword 并非正文 Q。
- **可用性结论**：修复后 md 可作 Roth 定理忠实底本；(1)-(54) 编号公式逐一核对全对；
  本篇 20/20 页完成，无未决项。

### 修复登记（2026-09-29）
- **11 组替换全部命中**（指数 κ/δ²/½δr₁/1+2δ/k^{p−1}×2/Lemma 8 版式/幽灵脚注×4/catchword Q/‡）；
  fix commit 见父提交链（audit(page) 即修复前 md 原貌）。
- 本篇 20/20 页完成，无未决项。
