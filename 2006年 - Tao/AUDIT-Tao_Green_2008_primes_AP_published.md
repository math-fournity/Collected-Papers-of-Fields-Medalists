# AUDIT — Tao_Green_2008_primes_AP_published

> 论文：Ben Green and Terence Tao, “The primes contain arbitrarily long arithmetic progressions,” *Annals of Mathematics* 167 (2008), 481–547。
> 审计对象：印刷版 PDF 的逐页文字层与同篇 MinerU Markdown 的转录对应；本审计不评价论文定理或证明的数学有效性。
> PDF：`Tao_Green_2008_primes_AP_published.pdf`，67 pages，SHA-256 `967dd6f5bb53d70abdbb07be0afe59e60b2a232e2c3387966013a09960e52c89`。
> MinerU Markdown：`Tao_Green_2008_primes_AP_published__Tao_Green_2008_primes_AP_published.md`；修复前 SHA-256 `79c5b79c7bb4af5103d1b1d540ec9ff9e913ff5ae6cb3c5c34e838b5b736e0af`。
> 模式：born-digital。`pdftotext -layout` 提取 205,041 UTF-8 bytes，67 个非空 PDF 页段，0 个 U+FFFD；归档的 `middle_json.json` 报告 67 页，schema `docvortex.middle` 2.0，producer MinerU 3.4.4。归档 JSON 未提供 `doc_id` 字段，故 doc_id 未知。
> 基线：task base `037602429d3b009f6fc468c732073eb3ddf9875f`；候选分支审计由 `Peer-P28` 执行，配置 `gpt-6-luna/max`。Git author 保持提交环境原值。本候选未经 Master 集成。

## 修复前页级审计（行号对应文件头所列修复前 SHA-256）

## p.001（PDF p.1/67 / 印刷 p.481）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:21:10-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p001.png`（pngmono 150dpi；题录页已目检）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1–15 行；核对题名、作者、期刊卷年页、摘要、引言首段、首个渐近式与作者脚注。PNG 确认原页题录为 “Annals of Mathematics, 167 (2008), 481–547”，首段符号为 `≫`，脚注与 Markdown 对应。
- 结果：FAIL。Markdown 未录入页首期刊卷年页；摘要将印刷 `sufficiently` 录为 `suficiently`，引言将 `difference` 录为 `diference`。均以 PDF p.1 为准，留待全篇审计后逐处手工修复。

## p.002（PDF p.2/67 / 印刷 p.482）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:23:26-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p002.png`（pngmono 150dpi；数值算术级数页已目检）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 17–45 行；核对 Hardy–Littlewood 预测、van der Corput/Heath-Brown/Balog 相关段落、两条例示素数等差数列、Theorem 1.1 与 Theorem 1.2 陈述。150dpi 源页确认两组数列的连续数字写法及公式标点。
- 结果：FAIL。两条例示被拆成逐位空格：印刷 `56211383760397 + 44546738095860k`，Markdown 写成 `5 6 2 1 1 3 8 3 7 6 0 3 9 7 + 4 4 5 4 6 7 3 8 0 9 5 8 6 0 k`；印刷 `11410337850553 + 4609098694200k`，Markdown 同样逐位拆开，改变了数字表达。另印刷 `different` 被录为 `diferent`。留待全篇审计后按源页逐处手工修复；Szemerédi 的重音分解和 `k=3` 后多出的标点另作低影响转录伪影。

## p.003（PDF p.3/67 / 印刷 p.483）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:24:20-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p003.png`（pngmono 150dpi；目检脚注记号与正文交界）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 47–63 行；核对引言后半、致谢、§2 标题、Proposition 2.1 的量词/集合/下界，以及脚注 1 完整说明。PNG 确认印刷脚注中 `Z_N`、`[-N,N]`、除数范围 `2,3,ldots,k` 和 wraparound 说明的顺序。
- 结果：FAIL。脚注 1 被拆成几个漂移的孤立公式块（Markdown 第 57、59、61 行）及被截断正文（第 63 行），造成 `Z_N`、`[-N,N]`、`2,3,ldots,k` 等记号在句中缺失/重复，末句的 `Z_N` 也移到了句尾；另致谢把印刷人名 `Jamie Radcliffe` 录为 `Jamie Radclife`。留待全篇审计后按 PDF p.3 逐处手工修复。

## p.004（PDF p.4/67 / 印刷 p.484）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:27:55-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p004.png`（pngmono 150dpi）；疑字裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p004_Lacey-Laba.png`（源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 65–93 行；核对 Gowers 上界、公式 (2.1)、Rankin 下界、Conjecture 2.2、段落逻辑和脚注 2。150dpi 页图显示主要公式与编号一致；300dpi 裁片确认印刷姓名为 `Lacey-Laba`。
- 结果：FAIL。Markdown 把印刷 `Lacey-Laba` 录为含 U+0004 控制字符的 `Lacey-\x04Laba`；脚注 2 的 `classical` 录成 `classica`，正文的 `sufficiently`、`difference` 分别录成 `suficiently`、`diference`。公式 (2.1) 的 `N_0(δ,k) ≤ 2^{c_k δ^{-1}}` 及其余列出的上下界与印刷相符。待全篇审计后逐处手工修复文字差异。 全篇修复复核补充：正文 W-trick 括注中 common difference 的乘积 `2×3×5×⋯×w(N)` 及相邻说明原被公式碎片污染，现按 PDF p.484 恢复。

## p.005（PDF p.5/67 / 印刷 p.485）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:29:02-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p005.png`（pngmono 150dpi；代表性公式页已目检）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 95–123 行；核对有限/无限系统对照段、Proposition 2.3、条件 (2.2)–(2.3)、进度计数下界及脚注 3。150dpi 页面上两条条件和主计数式与 Markdown 中的标签、记号一致。
- 结果：FAIL。印刷的 `N → ∞` 被 Markdown 写成 `N ∞`，极限箭头丢失；Remark 中 `differences` 被录为 `diferences`，脚注 3 的 `suffice` 被录为 `sufice`。脚注里的等差数列方程另以孤立 `<small>` 块重复一次（第 121 行），随后又在完整脚注中出现；印刷只在脚注句中出现一次。留待全篇审计后按 PDF p.5 修复。

## p.006（PDF p.6/67 / 印刷 p.486）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:30:06-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p006.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 125–145 行；核对 Proposition 2.3 remark、pseudorandom measure 定义 (2.4)、von Mangoldt 函数说明、主段落跨页处，以及脚注 4 和脚注 5 起始。式 (2.4) 及 `\gg N^2`、`c(k,δ)` 下界在文字层/Markdown 对应。
- 结果：FAIL。脚注 4 中印刷的 `Z_N`（“distribution on `Z_N`”）在 Markdown 中被漏掉，另有 `Z_N,` 与 `Vconst` 两个公式碎片游离在脚注块外；正文将 `difference`、`difficulty` 分别录成 `diference`、`dificulty`。脚注 5 在本页以 `4 (mod 6),` 开始并跨页，余下部分转 p.7 继续核对。

## p.007（PDF p.7/67 / 印刷 p.487）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:31:48-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p007.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p007_W-trick.png`（脚注公式源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 147–173 行；核对 Goldston–Yıldırım 段、式 (2.5)、Gowers uniformity 与 dual-norm 说明，并回核 p.6 起始的脚注 5。裁片确认印刷为 `n ≡ 1 (mod W)`、`W = ∏_{p<w(N)} p`，且 `w(N)` 随 N 缓慢趋于无穷。
- 结果：FAIL。脚注 5 的 `W` 乘积、同余式、`W-trick` 指称和相关句子在 Markdown 第 161–169 行被拆成漂移/乱码碎片，正文留有公式空位；脚注 7 又把印刷 `different` 录为 `diferent`。式 (2.5) 与双对偶范数说明的主记号相符。待全篇审计后依据 PDF p.7 连同跨页脚注逐处修复。

## p.008（PDF p.8/67 / 印刷 p.488）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:32:49-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p008.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 175–197 行；核对 §3 开头、`N=|Z_N|` 记号、极限符号、O/o 记号说明、两种条件期望的定义及脚注 8。页图确认印刷有 `N → ∞`，且脚注表述为投影 `f` 到 Gowers anti-uniform component。
- 结果：FAIL。Markdown 第 179 行把印刷 `N → ∞` 录成 `N ∞`，箭头缺失；脚注 8 中 `projection of f to` 的 `f` 漂移成独立碎片（第 195 行），正文脚注句第 197 行相应变成 `projection of to`。此外 `negligible` 被保留为断词 `neg-ligible`（第 175 行），影响忠实转录。两条期望公式与印刷的平均定义相符；留待全篇审计后逐处手工修复。 全篇修复复核补充：平均公式定义句 `f:A→R` 的映射箭头也缺失，现按 PDF p.488 补回。

## p.009（PDF p.9/67 / 印刷 p.489）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:33:33-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p009.png`（pngmono 150dpi；Definition 3.1 与多线性条件页已目检）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 199–225 行；核对 Definition 3.1 的参数量词/非比例线性型条件、公式 (3.1)–(3.4)、Remarks 对参数取值与 U^d 范数关系的说明。页图确认 (3.4) 后给出的参数为 `(12,5,2)`，且相关求和范围、约束变量与 Markdown 结构相符。
- 结果：FAIL。参数三元组印刷为 `(m_0,t_0,L_0)=(12,5,2)`，Markdown 第 225 行写成 `(1 2, 5, 2)`，将两位整数拆开。此外，(3.1) 线性型公式印刷求和变量为 `j=1,…,t`，原 Markdown 误写为 `i=1,…,t`，现已改正；(3.2)–(3.4) 其余所核主项与变量约束无新差异。待全篇审计后修正该参数表示。

## p.010（PDF p.10/67 / 印刷 p.490）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:34:32-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p010.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 227–249 行；核对线性形式条件到相关条件的转接、Definition 3.2、矩条件 (3.5)、上界 (3.6) 与 Remarks/脚注 9–10。页图确认 (3.5)、(3.6) 的变量范围、求和上下界及 RHS 结构。
- 结果：FAIL。`m_0`-correlation condition 在 Markdown 被写作上标负号形式 `m_0^{-}`；开头关于事件 `ψ_j(x)` 的表述遭到粗体/音调命令碎片污染。脚注 10 的集合 `{1,…,N}` 漂成独立块（第 247 行），正文因此缺少抽样全集；Bernoulli 权重中 `ν(x)`、`log N` 与概率的关系，以及末尾 `1+o(1)` / `O(log^m N)` 两种情形的对应均被打乱。留待全篇审计后据 PDF p.10 逐处修复。

## p.011（PDF p.11/67 / 印刷 p.491）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:35:46-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p011.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 243–265 行；核对 p.490 跨页句的尾部、Definition 3.3 的线性形式/相关条件参数、随机稀疏模型段、Lemma 3.4 的凸组合及证明。页图确认 `(k·2^{k−1},3k−4,k)`、相关条件阶 `2^{k−1}` 和 `ν_{1/2}=(ν+ν_const)/2=(ν+1)/2` 对应。
- 结果：FAIL。两处印刷单词被漏字母：`suffice`→`sufice`（Remarks）及 `different`→`diferent`（Lemma 3.4 说明）。本页核到的参数组、Lemma 3.4 公式及 `2^m` 展开与印刷一致；p.491 正文续句与前一页内容在 Markdown 第 243 行连续合并。

## p.012（PDF p.12/67 / 印刷 p.492）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:36:37-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p012.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 267–297 行；核对 Theorem 3.5 的假设与结论 (3.7)–(3.9)、关于 N 大小与误差项的说明、§4 标题及 L^q 空间引入。定理条件、三式的变量/不等号和界函数与印刷相符；第 267 行承接 p.491 底部未完句。
- 结果：FAIL。§4 首段将印刷 `Throughout` 录为 `Thoughout`，并将 `sufficiently` 录为 `suficiently`。本页未发现定理公式中的额外变量、量词或关系符差异；待全篇审计后逐处修复拼写。

## p.013（PDF p.13/67 / 印刷 p.493）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:37:49-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p013.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 299–323 行；核对 Definition 4.1 的 L^q 范数/内积、指标函数定义、uniform cover 定义与公式 (4.1)、§5 起始段。Definition 5.1 在本页末引入并跨到 PDF p.14，Markdown 第 323 行也跨页，后半在下一页继续核对。
- 结果：FAIL。印刷 `1_Ω: Z_N → R` 在 Markdown 第 311 行丢失 `→`；印刷 `Φ: A → B` 在第 313 行也丢失 `→`，使两个映射类型的 codomain 表达不完整。其余范数、内积与 (4.1) 结构对应。 全篇修复复核补充：脚注 11 的 `d=k−1` 原被拆成游离块且未保留在注释正文，现据 PDF p.493 合并为完整脚注。

## p.014（PDF p.14/67 / 印刷 p.494）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:38:59-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p014.png`（pngmono 150dpi；密集定义/公式页已目检）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 323–370 行；核对 d 维 Gowers inner product 的定义 (5.1)、d=2 例子、正性推导 (5.2)–(5.3)、U^d 范数 (5.4) 及 f_ω 依赖最后坐标时的重写式。主要乘积、平均变量和指数在页图与 Markdown 对应。
- 结果：FAIL。Definition 5.1 将印刷 `{0,1}^d`-tuple 录成 `{0,1}^{d_-}` tuple（第 323 行），引入了不存在的负号/下标并改变索引集合。行 335 的 `When d=2 .` 另有非语义标点伪影；`d=k−1` 脚注属印刷 p.493，按前页页签范围另核。

## p.015（PDF p.15/67 / 印刷 p.495）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:39:50-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p015.png`（pngmono 150dpi；Cauchy–Schwarz 与 U^2 公式页已目检）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 371–431 行；核对 Gowers Cauchy–Schwarz 不等式 (5.5)、三角不等式推导、U^2 例子、傅里叶变换公式及脚注 12。主不等式、指数和求和式结构与源页相符。
- 结果：FAIL。印刷 `h′ variables` 在 Markdown 第 371 行成为带控制字符的 `h<sup>\x08</sup> variables`；傅里叶脚注前另有孤立 `k = 3` 块（第 429 行），而同一短语随后又在完整脚注中出现（第 431 行）。留待全篇审计后修复控制字符与重复碎片。 全篇修复复核补充：脚注 12 的 `rôle` 重音编码已按印刷字形规范化；脚注 11 内容的来源页登记在 p.013。

## p.016（PDF p.16/67 / 印刷 p.496）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:40:36-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p016.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 433–485 行；核对范数单调性 (5.6)–(5.7)、Lemma 5.2 的结论 (5.8)、证明中展开式 (5.9)–(5.10) 及向线性形式条件的化归。指数、求和变量与集合约束在页图/文本层和 Markdown 对应。
- 结果：FAIL。两处 `it suffices` 在 Markdown 第 463 行均录为 `it sufices`；第 455 行将 `Definition` 断成 `Defini- tion` 并逐字母排开。留待全篇审计后按 PDF p.16 修正。

## p.017（PDF p.17/67 / 印刷 p.497）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:41:20-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p017.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 487–511 行；核对 Lemma 5.2 证明收束、(5.9) 的二项式消去、Proposition 5.3 的函数界/系数排列、(5.11) 和证明开头的 (5.12)。命题量词、上界和推论与印刷相符。
- 结果：PASS±。引用 `[19, Th. 3.2]` 周围的 `$` 被切入引用语法（第 505 行），造成轻微数学标记伪影；不改变引用编号或段落含义。

## p.018（PDF p.18/67 / 印刷 p.498）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:42:00-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p018.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 513–570 行；核对 Proposition 5.3 的 infimum 选择、(5.13)、k=3 的算术级数重参数化、(5.14) 及两轮 Cauchy–Schwarz 平均式。主界与 J_0/J_1 公式的变量和平均范围对应。
- 结果：FAIL。印刷将三元组 `(x,x+r,x+2r)` 重参数化为 `(y_1+y_2, y_2/2, -y_1)`；Markdown 第 535 行在前两个坐标间丢失逗号，并把公式分隔符拆开，导致该三元组结构不完整。留待全篇审计后依 PDF p.18 修复。

## p.019（PDF p.19/67 / 印刷 p.499）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:42:41-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p019.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 571–621 行；核对 (5.15)–(5.16)、四点 U^2 cube 重参数化、`W−1` 误差估计、n/q 取值，以及一般情形向量 `y^{(S)}` 定义。页图中各乘积项、撇号变量和指数与 Markdown 对应。
- 结果：FAIL。两处印刷 `it suffices` 被录成 `it sufices`（Markdown 第 595、607 行）；其余本页所列公式、上下界和向量坐标选择未见内容差异。

## p.020（PDF p.20/67 / 印刷 p.500）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:43:32-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p020.png`（pngmono 150dpi；定义 (5.17)–(5.20) 与辅助函数页已目检）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 623–665 行；核对 Lemma 5.4 的假设、J_d/P_d 定义 (5.17)–(5.18)、递推不等式 (5.19)、k=3 例子 (5.20) 以及证明中 G/H 的拆分。求和索引、半次幂、向量分量集合与 PDF 相符。
- 结果：FAIL。Markdown 第 626 行的 (5.17) 数学环境末尾混入孤立 `\qend` 字串，印刷无此内容；第 641 行将 `ν^{1/2}` 在 “in (5.17)” 后重复一次，印刷仅有一处，造成说明句多出一个因子。其余本页所核公式主结构一致。

## p.021（PDF p.21/67 / 印刷 p.501）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:44:44-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p021.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 667–716 行；核对 Lemma 5.4 的 Cauchy–Schwarz 推导、(5.19)、(5.21)–(5.22)、一般情形的 φ_i 定义与映射 Φ。页图确认幂次 `2^{k−1}`、`2^{k−2−d}` 及系数 `1−c_i/c_j` 与 Markdown 对应。
- 结果：FAIL。Markdown 第 667 行把印刷的 `ν^{1/2}` 写成带点的 `\dot{ν}^{1/2}`，在 Cauchy–Schwarz 分解中误添导数记号；其余此页核对的递推、指数和映射公式相符。

## p.022（PDF p.22/67 / 印刷 p.502）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:45:27-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p022.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 717–760 行；核对 (5.23)–(5.25)、W(x,h) 的两种乘积表达、ωh/y 向量定义及 U^{k−1} 范数恒等式。指数、乘积因子和边界在页图中对应。
- 结果：FAIL。印刷向量条件 `ωh ∈ Z_N^{k−1}` 在 Markdown 第 741 行被转成 `ωh ε Z_N^{k−1}`；同一行的 `y ∈ Z_N^{k−1}` 也出现异常双点装饰。另两处 `it suffices`（第 747、753 行）漏写一个 f。留待全篇审计后按 PDF p.22 修复。

## p.023（PDF p.23/67 / 印刷 p.503）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:46:17-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p023.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 761–808 行；核对 Lemma 5.5 的 n/q 取值、三组线性形式条件参数、各组 forms 范围、Lemma 收束/§6 标题及 dual norm 定义 (6.1)。参数组和主要集合索引与印刷相符。
- 结果：FAIL。引理条件后印刷 `n=0,2`，Markdown 第 761 行多出一个孤立 `2`；Proof 的 `it suffices` 在第 767 行漏写一个 f。待全篇审计后清除多余数字并修正拼写。

## p.024（PDF p.24/67 / 印刷 p.504）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:46:52-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p024.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 809–844 行；核对 dual norm 的 Fourier 公式 (6.2)、dual function (6.3)、Lemma 6.1 的内积恒等式 (6.4) 与 dual-norm 恒等式 (6.5)，并核对脚注 13。指数、排除零向量条件及标点次序均相符。
- 结果：PASS。此页未发现会改变印刷陈述的转录差异。

## p.025（PDF p.25/67 / 印刷 p.505）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:48:09-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p025.png`（pngmono 150dpi；dual-function 界与脚注页）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 845–883 行；核对 (6.6) 的 L∞ 界、(6.4)–(6.5) 的证明关系、非齐次线性形式条件说明，以及 Remarks 中多项式相位和脚注 14–15。主指数 `2^{2^{k−1}−1}` 与前述范数恒等式一致。
- 结果：FAIL。`for all` 在 (6.6) 条件中被字母拆散；两处 `it suffices` 漏字母 f；`differences` 被录为 `diferences`。脚注 15 对 `k−2`-step nilfactors 的句子被拆接，出现 `nilfactorsk−2`、`order but can k−2` 等错序片段，妨碍忠实读取。待全篇审计后据 PDF p.25 修复。

## p.026（PDF p.26/67 / 印刷 p.506）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:49:03-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p026.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 879–916 行；核对前页跨页的多项式相位讨论、公式 (6.7)、频率集 S 与 L∞ 误差界、基本 anti-uniform 函数值域，以及 Proposition 6.2 的映射/函数定义和均匀估计。式 (6.7)、ε 阈值和区间端点与页图对应。
- 结果：FAIL。Proposition 6.2 将印刷 `Φ:I^K → R` 录成 `Φ:I^K R`，缺少函数箭头；Remarks 里 `effect`、`sufficiently` 分别录成 `efect`、`suficiently`。本页起始继续 Markdown 第 879 行的跨页长段落。

## p.027（PDF p.27/67 / 印刷 p.507）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:49:57-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p027.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 917–959 行；核对 polynomial phase functions 的 Remark、(6.8)、Lemma 6.3 的范数上界、线性化为单项式的步骤及 dual-function 积的展开。页图确认 (6.8) 的绝对值界与展开中的频率变量。
- 结果：FAIL。`coefficients` 在 Markdown 第 931 行录成 `coeficients`，`it suffices` 在第 939 行录成 `it sufices`；同一 Lemma 6.3 行还把 `independent of N` 断成 `independent o f N`。本页公式与源页主要索引/界相符。 全篇修复复核补充：另修复了本页第二处 `it suffices` 漏字母 f 的问题。

## p.028（PDF p.28/67 / 印刷 p.508）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:50:33-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p028.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 961–1022 行；核对 Gowers 内积展开、函数 g 定义 (6.9)、多次 Hölder/Cauchy–Schwarz 界、均匀覆盖变量代换，以及最后归约到线性形式条件的表达。组指标、H 的取值域及产品项均相符。
- 结果：FAIL。三处印刷 `suffice/suffices` 被录为 `sufice/sufices`（Markdown 第 979、985、993 行）；其余本页所核代换与上界没有发现内容差异。

## p.029（PDF p.29/67 / 印刷 p.509）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:51:14-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p029.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1023–1068 行；核对 correlation-condition 收尾、τ 的矩界、均匀覆盖变量代换、Weierstrass 逼近误差以及 Proposition 6.2 证明终结。各期望的范围、K 次幂和误差系数均对应。
- 结果：FAIL。Markdown 第 1035 行将 `it thus suffices` 写为 `sufices`，第 1061 行将 `sufficiently` 写为 `suficiently`；主要公式和上界与 PDF p.29 相符。

## p.030（PDF p.30/67 / 印刷 p.510）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:52:07-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p030.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1069–1082 行；核对 Wiener-algebra 范数比较、Proposition 6.2 后的 Remark、基本 anti-uniform 函数范围和 Definition 7.1 的有限 σ-代数定义。主范数关系、区间端点及集合/原子定义相符。
- 结果：FAIL。第 1071 行 “and” 后插入印刷中不存在的 U+0011 控制字符；第 1073 行将 `difficult` 录为 `dificult`。印刷原文在同页首处写 `Wiener norm`、后处写 `Weiner norm`；Markdown 跟随这处源级拼写差异，按 print 原文保留。

## p.031（PDF p.31/67 / 印刷 p.511）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:52:47-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p031.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1083–1117 行；核对 conditional expectation、σ-algebra join、Proposition 7.2 的区间 I、性质 (7.1)–(7.2) 及证明首个 Fubini 平均。条件期望、join、界 ε 和积分被积函数与印刷对应。
- 结果：FAIL。印刷的连续映射 `Ψ_A:I → [0,1]` 在 Markdown 第 1105 行写成 `Ψ_A:I [0,1]`，函数箭头遗漏。留待全篇审计后手工补回。

## p.032（PDF p.32/67 / 印刷 p.512）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:53:27-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p032.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1119–1150 行；核对 (7.3) 的 pigeonhole 界、B_{ε,η}(G) 的 interval partition、cutoff 函数 Ψ_A 定义及 Proposition 7.3 的 (7.4)–(7.6)。误差阶 η^{1/2}、集合 Ω 与界 ε 相符。
- 结果：FAIL。Markdown 第 1125 行在生成原子区间的两个端点之间漏掉逗号；第 1127 行的映射 `ψη:R→[0,1]` 丢失 `→`，并将印刷 `cutoff` 拼成 `cutof`；第 1131 行 `sufficiently` 漏 f。留待全篇审计后据 PDF p.512 修复。

## p.033（PDF p.33/67 / 印刷 p.513）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:54:33-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p033.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1151–1195 行；核对 Proposition 7.3 证明的 (7.7)–(7.8)、Ψ_A 逼近、误差界与 §8 起始/Proposition 8.1 题头。前述公式和 η 阶对应；Proposition 8.1 的题头在源印刷页可见时已无左括号，Markdown 忠实照录，登记为 print quirk，不能替原文补括号。
- 结果：FAIL。Markdown 第 1151、1163 行将 `suffices` 漏 f；第 1169 行映射 `Ψ_A:I^K → [0,1]` 丢 `→`；第 1187 行 η 参数后出现异常分号；Proposition 8.1 首段还将 `sufficiently` 写成 `suficiently`。第 1195 行的命题句跨到下一页，余下接页继续核对。 全篇修复复核补充：另修复 Proposition 7.3 证明中的 `sufficiently` 漏字母 f。

## p.034（PDF p.34/67 / 印刷 p.514）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:55:42-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p034.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1195–1225 行；核对 Proposition 8.1 的 (8.1)–(8.3)、Koopman–von Neumann 类比、Theorem 3.5 证明开头及 f_{U⊥} 的密度下界。ε 指数、Ω 因子和 δ−o_ε(1) 结论相符。
- 结果：FAIL。连续的 `sufficiently` 在第 1195 行录为 `suficiently`；`Fourier coefficients` 在第 1217 行录为 `Fourier coeficients`。此外 “outside of Ω” 在第 1203 行被切成 `outside o f Ω`，产生明显字间碎片。留待全篇审计后逐处修复。

## p.035（PDF p.35/67 / 印刷 p.515）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:56:46-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p035.png`（pngmono 150dpi；脚注 16 与误差项页已目检）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1225–1255 行；核对 Proposition 2.3 的应用、(8.3) 的 U^{k−1} 小范数界、误差合并及 Theorem 3.5 证明的结构迭代描述。三处主估计的指数 `1/2^k` 与 Ω 截断项对应。
- 结果：FAIL。脚注 16 在 Markdown 第 1255 行碎片化并漏掉关键量：源页给出 `f_{U⊥} ≤ 1+o_ε(1)`、密度下界 `δ−o_ε(1)`，以及将 `f_{U⊥}` 调整 `o_ε(1)` 的办法；Markdown 留下 `not U⊥ bounded above by 1 but by` 等残缺句。另第 1249 行两处 `sufficiently` 漏 f，第 1251 行 `suffices` 也错拼。留待全篇审计后逐处修复。

## p.036（PDF p.36/67 / 印刷 p.516）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T16:59:36-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p036.png`（pngmono 150dpi；Proposition 8.2 起始与脚注 17 页）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1257–1297 行；核对迭代步数上界、Lemma/Proposition 8.2 的参数与条件、(8.4)–(8.7) 以及 Zorn 引理脚注 17。四条 displayed bounds 的对象、Ω 截断和 η^{1/2} 阶相符。
- 结果：FAIL。Markdown 第 1257 行在 `L^2-increment` 中插入无源句点；第 1263 行把 `0<η≪ε≪1` 后再添一个孤立 `1`，并将两处 `sufficiently` 录为 `suficiently`；第 1259 行 `different` 漏 f。脚注 17 的 `depending on k` 丢失 k，孤立 `k,` 碎片另见第 1293、1295 行。留待全篇审计后据 PDF p.36 手工修复。 全篇修复复核补充：另将 (8.4) 条件后的 `for all ...` 碎片按 p.516 原句重组；脚注 17 的完整说明已保留。

## p.037（PDF p.37/67 / 印刷 p.517）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:01:08-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p037.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1299–1355 行；核对 (8.8)–(8.15)、能量增量指数、迭代步数上界 `2^{2^k}/ε+2`，以及 Proposition 8.1 的 K_0/η 启动参数。各 bounds 的 Ω、σ-代数与范数对象对应。
- 结果：FAIL。`sufficiently` 在 Markdown 第 1353 行录为 `suficiently`；本页核到的迭代指数、能量增量项及 (8.8)–(8.15) 主公式与印刷一致。

## p.038（PDF p.38/67 / 印刷 p.518）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:02:01-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p038.png`（pngmono 150dpi；迭代步骤与脚注页）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1357–1381 行；核对算法 Step 0–4、(8.8)–(8.9)、K_0 终止条件、成功/失败状态，以及脚注 18 对 O() 常数的说明。步序、阈值和脚注所述边界相符。
- 结果：FAIL。脚注 18 在 Markdown 第 1381 行漏掉 “these constants to depend on K” 中的 `K`，并将 `different` 录为 `diferent`。脚注 remainder 与 Step 0–4 记录均对上印刷页。 全篇修复复核补充：脚注 18 的断裂文本已重组，游离 `00` 与 `K,` 碎片已清除，并恢复其关于常数依赖 K 的句子。

## p.039（PDF p.39/67 / 印刷 p.519）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:03:19-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p039.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1375–1428 行；核对算法成功/错误终止排除、能量递增 (8.16)、E_K 的上界、Proposition 8.2 的基本函数范数界 (8.17) 及本页末 Ω 估计。指数、K_0 阈值和 Ω/能量对象与印刷相符。
- 结果：FAIL。跨页段落 (Markdown 第 1375 行) 中 `sufficiently` 漏 f；第 1383、1401 行分别把 `suffices`、`sufficiently` 错拼。第 1411 行把 `F_{K+1}` 和误差常数 `O_{K,ε}` 误录为带额外下标的 `F_{K_1+1}`、`O_{K_1,ε}`；第 1413 行再多出一个孤立 `1`。留待全篇审计后依 PDF p.519 修复。

## p.040（PDF p.40/67 / 印刷 p.520）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:04:13-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p040.png`（pngmono 150dpi；能量增量推导页）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1424–1478 行；核对 (8.18)、Cauchy–Schwarz 内积拆分、(8.19) 的 ε^{1/2} 下界和 Pythagoras 说明。主指数与误差项在页图中相符。
- 结果：FAIL。(8.14) 中源页使用 `Ω_{K+1}`，Markdown 第 1430 行误写为 `Ω`，改变了异常集标识；后经复核 p.520 页图确认第 1465 行内积列举逗号与印刷一致，原逗号差异系误报，不列为差异。

## p.041（PDF p.41/67 / 印刷 p.521）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:05:00-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p041.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1478–1533 行；核对 (8.18) 的目标能量界、余项吸收、cosine rule 展开、近似正交性与逐步改写的内积。各异常集索引和 `O(ε^{3/2})` 项与源页对应。
- 结果：FAIL。第 1479 行把印刷 `sufficiently small` 录为 `suficiently small`；本页主公式未见符号或指数差异。

## p.042（PDF p.42/67 / 印刷 p.522）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:06:05-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p042.png`（pngmono 150dpi；§9 开篇及脚注 19 页）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1535–1557 行；核对 Proposition 8.2 收尾、§9 标题、von Mangoldt 函数与 residue-class obstructions 的说明，以及 W-trick 引入段和脚注 19。Theorem 3.5 收尾与主论述内容对应；W-trick 长句在 Markdown 一行内跨到下一印刷页，下一页继续核其余部分。
- 结果：FAIL。Markdown 第 1555 行将印刷 `W-trick` 写为 `Wtrick`，`effectively` 写成 `efectively`；脚注 19 第 1557 行把 `our argument ...` 与 `K=0` 粘成 `argumentK = 0`，并把 `difficult` 写为 `dificult`。行 1551 在 `p^3, …` 后额外插入句点。待全篇审计后依据印刷 p.522 修复。 全篇修复复核补充：另修复 §9 起始段中的 `suffices`、`effectively` 与 `sufficiently` 拼写碎片；脚注 19 的 K=0 说明一并重组。

## p.043（PDF p.43/67 / 印刷 p.523）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:07:08-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p043.png`（pngmono 150dpi；W 乘积、分段定义及两条文献脚注页）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1555–1579 行；核对 W 的素数乘积、修正后的 von Mangoldt 函数定义、Dirichlet 定理推论、ε_k 和 Proposition 9.1 的 majorant 范围，以及脚注 20/21。W 与 ~Λ 的表达和 majorant 下界相符。
- 结果：FAIL。Markdown 第 1567 行把印刷 `ε_k=1/(2^k(k+4)!)` 写成 `1/2^k (k+4)!`，分母结构改变；第 1577 行脚注把 `≫ N` 写成单个 `> N`。脚注 20（第 1575 行）漏掉 “independent of N” 的 N 且多处文本粘连；脚注 21（第 1579 行）把求和范围、`Λ(n)≫N` 与替换 `n≡b (mod W)` 的叙述拆散。正文另有 `suffices/effecting/sufficiently` 多处漏字母。待全篇审计后依据 p.523 逐处修复。

## p.044（PDF p.44/67 / 印刷 p.524）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:22:26-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p044.png`（pngmono 150dpi；平均值、Λ 与截断除数和公式页）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1581–1618 行；核对 E(f) 渐近式、Theorem 3.5 得出的等差数列下界、r=0 退化情形、von Mangoldt 恒等式、Λ_R 定义及 R/ε_k 参数。主要系数、求和范围和截断公式结构对应。
- 结果：FAIL。Markdown 第 1593、1595 行的 `sufficiently/suffice` 漏字母 f；其余 p.524 上述公式结构与印刷相符。 全篇修复复核补充：另删除 `is sufficiently slowly growing` 前的 U+0014 控制字符。

## p.045（PDF p.45/67 / 印刷 p.525）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:32:47-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p045.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1613–1637 行；核对 Lemma 9.4 的 majorant 常数、Proposition 9.5 的线性形式系数/区间长度假设及截断除数和主渐近式。页图确认 Proposition 9.5 右端幂次 m 与 `R^{10m}` 区间长度条件。
- 结果：FAIL。`sufficiently` 在 Markdown 第 1623、1629 行录为 `suficiently`；`coefficients` 第 1629 行录为 `coeficients`。式前 Proposition 9.5 对 `ψ_i` 的定义后多出逗号，影响句法阅读；主公式因子结构与印刷相符。 全篇修复复核补充：另修复本页 prose 中 `difficulty`、`different` 的 OCR 漏字母，并把 Definition 9.3 的 ε_k 分母恢复为 `2^k(k+4)!`。

## p.046（PDF p.46/67 / 印刷 p.526）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:43:16-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p046.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1639–1676 行；核对 Proposition 9.6 的 m/h_i/Δ 假设、(9.1) 的 Euler-product 上界、Lemma 9.7 的测度归一化及 Proposition 9.8 起始参数。(9.1) 的幂次 m 和 p|Δ 乘积结构相符。
- 结果：FAIL。Proposition 9.6 的印刷条件为 `m≥1`，Markdown 第 1641 行写成 `m - 1`，改坏参数下界；第 1647 行 `sufficiently` 漏 f。其余本页核到的渐近式与上界因子对应。

## p.047（PDF p.47/67 / 印刷 p.527）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T17:57:25-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p047.png`（pngmono 150dpi）；疑点裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p047_footnote22.png`（footnote 22 源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1677–1722 行；核对 Proposition 9.8 的线性形式声明、(9.2)、整数系数界、Q-box 切分、nice box 条件、non-nice 比例以及脚注 22 的模 N 修正。裁片确认脚注中的 `ψ_i(x)`、区间 `[ε_kN,2ε_kN]` 与从 affine-linear form 减去常数倍 N 的完整叙述。
- 结果：FAIL。结尾的非 nice box 误差在 Markdown 第 1711 行把印刷 `O_{m,t}(1/Q)` 录成带点号 `\dot O_{m,t}(1/Q)`。脚注 22（第 1721 行）丢失 `ψ_i(x)` 和区间端点符号、将“subtract ... from ψ_i”拆散，且 `affine-linear` 漏 f；print crop 已将正确符号逐项终裁。 全篇修复复核补充：另修复本页 `sufficiently` 拼写；脚注 22 的完整说明已恢复。

## p.048（PDF p.48/67 / 印刷 p.528）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T18:45:29-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p048.png`（pngmono 150dpi）；疑点裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p048_tau.png`（Lemma 9.9 的 τ 定义源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1723–1772 行；核对 nonnice box 计数、Lemma 9.9 的参数、质因子乘积上界、τ_m 构造及其 q-矩条件。裁片确认源页 τ_m 中使用普通 `O_m(1)` 与 `(1+p^{-1/2})^{O_m(1)}`，无 overline。
- 结果：FAIL。Lemma 9.9 条件 `m≥1` 在 Markdown 第 1745 行写成 `m−1`；第 1759 行的 τ_m 定义将源页普通 `O_m(1)` 和 `1` 误加 overline；同一行 `it suffices` 漏 f。300dpi 裁片已终裁这组公式差异。 全篇修复复核补充：另删除 Lemma 9.9 区间 `[ε_kN,2ε_kN]` 后的游离 `2`。页图同时确认印刷确为 `h_1,…,h_j`，此记号原样保留为 print quirk。

## p.049（PDF p.49/67 / 印刷 p.529）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T19:00:03-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p049.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1773–1818 行；核对 Lemma 9.9 的矩估计收束、整除和上界、Proposition 9.10 的相关条件范围、(9.3) 权函数 bound 与重复 h_i 情形。主要变量范围、求和索引和 τ(0) 取值与印刷对应。
- 结果：PASS。p.48 起始的 Lemma 9.9 证明跨页续完；本页对应段落未发现新的转录差异。

## p.050（PDF p.50/67 / 印刷 p.530）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T19:08:49-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p050.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1803–1840 行；核对 ν 由 1+g 支配的展开、各 A 子集求和、Lemma 9.9 的 τ 控制、Proposition 9.1 收束及 §10 开始处的线性形式条件参数。g(n) 和 R、W 因子与源页对应。
- 结果：FAIL。Markdown 第 1835 行将印刷 `coefficients` 录为 `coeficients`；其余本页核对的乘积展开、τ 上界和 section transition 相符。 全篇修复复核补充：§10 开头线性型定义原将求和指标误作 `i=1,…,t`，已据 p.530 改为印刷的 `j=1,…,t`。

## p.051（PDF p.51/67 / 印刷 p.531）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T19:33:00-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p051.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1837–1870 行；核对 Proposition 9.5 的 B 区间长度条件、(10.1)–(10.2) 的 Möbius 展开与误差界，以及 Chinese remainder theorem 后的局部平均分解。求和范围、平方自由条件和模 p 约束对应。
- 结果：PASS±。Markdown 第 1837 行把印刷 `I_j, each ...` 的逗号解析成 `I_j.` 句点，产生轻微标点/MathJax 伪影，但区间定义及长度条件仍可确定；本页未见主公式内容差异。

## p.052（PDF p.52/67 / 印刷 p.532）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T20:15:21-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p052.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p052-omega-sets.png`（(10.2) 局部因子下标）与 `audit/300dpi/Tao_Green_2008_primes_AP_published_p052-local-factors.png`（(10.5)–(10.6) contour/F(z,z′) 定义，均为源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1873–1915 行；核对局部因子 ω_X(p)、CRT 分解、(10.2) 和式中的乘积/对数、contour 参数 (10.4)、反演积分、(10.5)–(10.6) 及 z/z′ 变量组。裁片确认目标下标是 `X_{d_1,…,d_m}(p) ∪ X_{d'_1,…,d'_m}(p)`。
- 结果：FAIL。Markdown 第 1888 行在 (10.2) 展开中把该集合索引的括号/下标边界拆错，呈现为 `X_{d_1}, …, d_m(p)` 与 `X_{d'_1}, …, d'_m(p)`，不等于印刷的两个完整 X 集合。其余本页所核 contour 和积分公式相符。

## p.053（PDF p.53/67 / 印刷 p.533）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T20:31:25-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p053.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p053_linear-forms.png`（local-factor proof 疑词，源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1917–1937 行；核对 Euler product E_p、收敛区域、Lemma 10.1 的局部因子估计及 (10.8) 的展开。裁片确认印刷原句为 “none of the s pure linear forms”；Markdown 照录该字母，作为源级 wording quirk 保留。
- 结果：FAIL。Markdown 第 1929 行将 `affine` 录成 `afine`；第 1931 行将 `comparison` 录成 `comparision`；第 1927 行把 `If` 断成 `I f`。局部因子主公式和 `p>w(N)` 条件与印刷对应；源页中 `s` 的表述保持原样，不擅改为其他词。

## p.054（PDF p.54/67 / 印刷 p.534）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T20:43:13-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p054.png`（pngmono 150dpi；Euler factor/ζ-function 页已目检）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1939–1971 行；核对 E_p^(1),(2),(3) 分解、G_3 与 ζ 的关系 (10.9)、复域 D_σ^m、C^k 导数范数及 Lemma 10.3 的一致收敛/点值估计。
- 结果：FAIL。E_p^(3) 在 Markdown 第 1940 行写成 `\prod_{i=1}^m`，但乘积因子仍使用自由下标 j；印刷与前两个 Euler factors 一样以 j 为乘积索引，当前式因此存在变量索引错误。另第 1971 行 `suffice` 漏 f；本页其余 ζ 比值和范数定义与印刷相符。 全篇修复复核补充：另修复 Definition 10.2 中端点 `100` 的数字拆分，按印刷连写。

## p.055（PDF p.55/67 / 印刷 p.535）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T20:46:54-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p055.png`（pngmono 150dpi；Euler product/contour lemma 页）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 1973–2010 行；核对 G_1/G_2 收敛与 φ(W)/W 乘积、Lemma 10.4 的 contour integral/error term、Proposition 9.5 收尾和 Proposition 9.6 的过渡。积分核、ζ 比值和 `e^{-δ√log R}` 余项相符。
- 结果：FAIL。Markdown 第 1973 行把乘积范围写为 `p<w(n)`，印刷为 `p<w(N)`；第 1999 行 `sufficiently` 漏 f，且第 2001 行两处 `differences` 漏 f。Lemma 10.4 的主积分结构与误差项一致。 全篇修复复核补充：另修复本页 `sufficiently` 拼写碎片。

## p.056（PDF p.56/67 / 印刷 p.536）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T21:09:23-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p056.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p056-delta-index.png`（Lemma 10.5 的 Δ 索引，源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2011–2040 行；核对高阶相关性的 ω_X 定义、Lemma 10.5 条件、(10.11) 的局部因子和 λ_p 误差项、E_p^(0)–E_p^(3) 分解。裁片确认印刷 Δ 公式的上限字母。
- 结果：PASS±。印刷 Proposition/Lemma 10.5 的 Δ 乘积上限确实写为 `s`，尽管邻近 h_i 列表及 Lemma9.6 中用 `m`；Markdown 照原文写 `s`，记录为源级 notation tension，不擅自改成 m。正文中 `If` 被轻微拆字，但未见另一处与印刷不符的公式内容。

## p.057（PDF p.57/67 / 印刷 p.537）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T21:34:08-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p057.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2041–2084 行；核对 Lemma 10.6 的 G_0–G_3 分解、(10.12)–(10.15)、G_0(0,0) 的局部因子积和导数界。主幂次、Euler factor 和 Δ 上界与页图对应。
- 结果：FAIL。源页把 (10.14) 标在 `G_0(0,0)=∏_{p|Δ}(1+O_m(p^{-1/2}))` 前；Markdown 将 `(10.14)` 放到上方 `G_2` 的 C^m 范数估计（第 2060 行），导致公式引用错位。另第 2075、2083 行分别把 `difficulties`、`differentiating` 漏掉一个 f。 全篇修复复核补充：另修复本页证明段 `suffices` 漏字母 f。

## p.058（PDF p.58/67 / 印刷 p.538）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T21:37:57-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p058.png`（pngmono 150dpi）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2084–2121 行；核对 (10.13) 推导、(10.14) 的 G_0 点值估计、Lemma 10.4 应用的导数界/主渐近与误差项，以及 Proposition 9.6 收尾。Euler-product 乘积、R 的对数幂和指数误差对应。
- 结果：FAIL。`it suffices` 在 Markdown 第 2085 行漏 f，`sufficiently` 在第 2119 行漏 f；本页主估计与积分误差的结构未见其他差异。

## p.059（PDF p.59/67 / 印刷 p.539）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T22:02:19-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p059.png`（pngmono 150dpi；§11、四项平方和公式与脚注 23 页）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2123–2135 行；核对 k-term 素数等差数列上下界、W-trick 与 Theorem 1.2 的推广说明、Heath-Brown 的四项平方和例子，以及 footnote 23 的 N_j 处理。
- 结果：FAIL。四项平方和例子在 Markdown 第 2129 行把第二与第三项之间的分隔符转成孤立 `2`，破坏了四项列举；脚注 23 的 `N_1,N_2,…→∞` 与 `N_j` 漂成第 2131、2133 行的孤立块，完整脚注第 2135 行又缺 `N_j` 与 O(1) 放弃因子的衔接。另第 2125 行 `off`→`of`、第 2127 行 `affect`→`afect`。待全篇审计后依 PDF p.539 修复。

## p.060（PDF p.60/67 / 印刷 p.540）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T22:24:27-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p060.png`（pngmono 150dpi）；脚注裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p060_footnote24.png`（源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2137–2155 行；核对 Chen 定理延伸、Transference principle 段、F_i 的多项式函数型、footnote 24 的双 Λ_R 主项与互素条件，以及 press notes 25–26。裁片确认 footnote 24 的完整源表达。
- 结果：FAIL。第 2139 行丢失 `F_i: N→N` 的箭头，`affine` 漏 f，且 `transference principle` 被字母/标记拆坏。脚注 24 在第 2141–2151 行把 `1≤b<W`、`b,b+2` 互素条件及 `Λ_R(Wn+b)Λ_R(Wn+b+2)` 拆成游离片段，完整注释句缺少关键 majorant 公式。p.540 开头还继续 p.539 Markdown 第 2129 行四项平方和段。 全篇修复复核补充：另把 §11 中 Chen 定理介绍语的印刷短语 `to the effect` 从拆字碎片恢复。

## p.061（PDF p.61/67 / 印刷 p.541）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T22:51:29-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p061.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p061-zero-free.png` 与 `audit/300dpi/Tao_Green_2008_primes_AP_published_p061-upper-bound.png`（源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2157–2187 行；核对 Appendix A 开头、Lemma A.1 的零点自由区域、ζ 与 1/ζ 界、区域边界和 Γ_0、Γ_2 的参数化。两张裁片确认印刷本身将零点自由区域上界印为 `10 ≥ Re(s)`，后文区域上界印为 `Re(s)<101`；Markdown 照录这两个源页字面记号，作为原文 notation quirk 保留，不归为 OCR 错误。
- 结果：FAIL。Markdown 第 2169 行把 `sufficiently` 录成 `suficiently`。本页其余核对的区域与轮廓公式对应印刷内容。

## p.062（PDF p.62/67 / 印刷 p.542）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T23:00:23-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p062.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p062-integral-tags.png`（(A.2)–(A.3) 公式标签，源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2189–2234 行；核对 Lemma A.2 的两条轮廓积分界、参数 T 的选择、证明中的尾积分估计及 Lemma A.3 的假设和主积分渐近式。裁片确认源页依次将两条积分界标为 (A.2) 与 (A.3)。
- 结果：FAIL。Markdown 第 2196 行把第一条积分界标成 `\tag{A.3}`，应为 (A.2)；第二条积分界在第 2200 行漏掉 (A.3) 标签。公式正文与源页相符。第 2235 行开始的证明句跨到下一 PDF 页，继续在 p.63 核对。

## p.063（PDF p.63/67 / 印刷 p.543）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T23:06:47-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p063.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p063-residue-derivative.png`（残数导数，源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2235–2267 行；核对上一页续入的移 contour 说明、I_1/I_2 分解、双极点残数、两个简单极点的贡献及 (A.4) 新轮廓积分。裁片确认印刷残数为 `∂f/∂z′(0,0)`，f 上无横线。
- 结果：FAIL。第 2235 行把 `difficulties` 写成 `dificulties`，并在 `Im(z), Im(z′)→∞` 处漏掉趋于符号；第 2241 行残数导数中的 f 多出横线；第 2249 行又把 `sufficient` 写成 `suficient`，且漏掉 `|Im(z′)|→∞` 的箭头。其余本页核对的极点位置、残数积分、衰减项和 (A.4) 公式对应源页。

## p.064（PDF p.64/67 / 印刷 p.544）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T23:13:25-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p064.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p064-imaginary-parts.png` 与 `audit/300dpi/Tao_Green_2008_primes_AP_published_p064-product-limit.png`（源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2269–2305 行；核对 (A.5) 的 ζ 增长界、I_1/I_2 误差收束、Lemma 10.4 的积分与归纳起步、(A.6) 绝对积分界及进入 m+1 的过渡。页中印刷公式的乘积上限字面为 `s`，虽前后以 m 参数化，Markdown 同样记作 s；按源页原样保留，作为原文 notation quirk。
- 结果：FAIL。Markdown 第 2275 行把印刷的虚部符号 `Im` 录成 `\mathbb{S}`，并在 (A.4) 的衰减结论前多出帽号 `\hat O_m`；同段 `1/10`、`1/100` 的数字又被空格拆开。第 2303 行在 C^1 范数表达式后多出游离 `σ`。源页裁片确认虚部记号与乘积上限 s 的印刷字形/位置；本页其余核对的主积分、增长指数与 (A.6) 积分内容对应。

## p.065（PDF p.65/67 / 印刷 p.545）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T23:19:24-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p065.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p065-induction-integral.png`（归纳步双重积分与 H 的定义域，源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2305–2347 行；核对 Lemma 10.4 归纳步的两个积分项、误差项、H 的导数和轮廓积分定义、C^j 范数估计及最终归纳收束。裁片确认第二个积分分母为 `z_j^2 z_j′^2`，且印刷 `H:D_σ^m→C` 含映射箭头。
- 结果：FAIL。Markdown 第 2308 行第二个积分项把 `z_j′^2` 错录为嵌套下标 `z_{j′^2}`；第 2311 行 H 的定义漏掉 `D_σ^m` 到 `C` 的映射箭头。其余核对的归纳表达式、导数与误差项对应源页。

## p.066（PDF p.66/67 / 印刷 p.546）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T23:29:24-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p066.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p066-reference-dashes-diacritics.png`（参考文献 3、9、12 等处，源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2349–2395 行；核对两处作者单位及邮箱、References [1]–[21] 的条目顺序、重复作者标识、姓名、题名、刊名、卷页和年份。裁片确认 [3]、[12] 等处的长横线是沿用前一条作者名的印刷标识，并能辨认 Erdős、Turán 的重音位置。
- 结果：FAIL。Markdown 第 2359、2377、2387 行分别漏掉源页表示重复作者的长横线；第 2371 行把 `Erdős`、`Turán` 写成重音位置错误的 `Erdos˝`、`Turan´`。第 2361 行及本页多条 Szemerédi 引文中的急音符也以独立符号插在字母间，而非落在印刷的 e 上。其余本页核对的条目顺序及主要书目字段对应源页。 全篇修复复核补充：另补回参考文献 [16] 前的重复作者长横线；[20] 的长横线也已恢复。两处单位地址中的逗号原被包入 `<sub>` 标签，现按 p.546 还原为普通逗号。

## p.067（PDF p.67/67 / 印刷 p.547）
- actor：Peer-P28；model：gpt-6-luna；effort：max；审阅时间：2026-10-01T23:35:18-0400。
- PNG：`audit/Tao_Green_2008_primes_AP_published_p067.png`（pngmono 150dpi）；裁片：`audit/300dpi/Tao_Green_2008_primes_AP_published_p067-references-ending.png`（参考文献 [29]–[45]、重音姓名与文末日期，源页 300dpi 灰度裁片）。
- 对账：PDF 原生文字层与 MinerU Markdown 第 2397–2443 行；核对参考文献 [22]–[45] 的作者、题名、期刊和出版信息，以及收稿/修订日期。裁片确认重复作者长横线、Ł/Rödl/Ramaré/Über 等印刷字形，以及文末 `(Received April 9, 2004)`、`(Revised June 2, 2005)`。
- 结果：FAIL。Markdown 第 2409、2429、2431、2443 行缺少 [28]、[38]、[39]、[45] 的重复作者长横线；第 2413、2415 行把 Łuczak、Łaba 中的 Ł 损坏为连字符形式，并把 Rödl 的重音错置；Szemerédi、Théor、Ramaré 等多处重音也未按印刷位置记录，第 2437 行把 `Über` 拆成 `Uber` 加游离上标分音符。Markdown 末尾还漏掉收稿日期 April 9, 2004 与修订日期 June 2, 2005。其余本页核对的参考文献顺序与主要出版字段对应源页。

## 修复登记

- 修复身份：`Peer-P28 | gpt-6-luna/max`；修复提交：`7df95cbce15504eac315c2c423bcbf3be65413dd`；其父提交/修复前快照：`71d12263fa7a4052933a229db9f2b1f14ae1eaca`；原始 MinerU Markdown 所在提交：`ce11d92fd5c5a412de2d8f31c1415b9f9f8951ac`。
- 修复前 Markdown SHA-256：`79c5b79c7bb4af5103d1b1d540ec9ff9e913ff5ae6cb3c5c34e838b5b736e0af`。修复后 Markdown SHA-256：`9031f2f94437405abe67b1df58c3f289356a3aed79ba1eb855409e0623b7ec8c`；最终文件为 2,391 行。
- 初始逐页分级保持为修复前评级：PASS 2、PASS± 3、FAIL 62。上述 62 个 FAIL 结果行记录逐页修复对象与原页证据；修复后未重评级，也未批量改写 PASS± 项。
- 复核：在最后一次 Markdown 修改后，从首行至末行重新人工复读完整文件；按各页结果行对应的 PDF 页图/裁片逐项核验修复，印刷版仍是文字与数学记号的权威。`git diff --check` 通过，目标文件未发现禁止的 C0 控制字符。未运行软件测试；本次验收针对 PDF 原页与 MinerU 转录的对应关系，不评价论文证明的数学有效性。

### 全文件复核期间追加的修复

| PDF 页 | 追加发现与修复 |
|---|---|
| 4 | W-trick 括注中的共同差乘积与相邻说明恢复。 |
| 8 | 补回 `f:A→R` 映射箭头。 |
| 9 | (3.1) 求和指标由误录的 i 更正为印刷的 j。 |
| 13 | 脚注 11 的 `d=k−1` 说明并回完整注释。 |
| 15 | 脚注 12 的 `rôle` 重音规范化。 |
| 27, 33, 36, 38 | 修复第二处拼写错误、Proposition 7.3 的 `sufficiently`、(8.4) 后碎裂的 `for all`，以及脚注 18/孤立 `00`、`K,` 碎片。 |
| 42–45 | 补齐 §9 起始段拼写、清除 U+0014、修复 difficulty/different，并把 Definition 9.3 的 ε_k 分母恢复为 `2^k(k+4)!`。 |
| 47–48 | 修复 `sufficiently`、清除 Lemma 9.9 区间后的孤立 `2`。 |
| 50 | §10 线性型公式的求和指标由 i 改为 j。 |
| 54–57 | 修复 Definition 10.2 数字 `100` 的拆分、`sufficiently` 和 `suffices` 拼写。 |
| 60 | 恢复 `to the effect`。 |
| 66 | 恢复 [16]、[20] 的重复作者横线，修复两处地址行的逗号标签。 |

### 保留的印刷原貌

p.030 的 `Weiner norm`、p.033 Proposition 8.1 题头缺左括号、p.048 条件中的 `h_1,…,h_j`、p.053 的 “s pure linear forms”、p.056 的 `s` 乘积上限、p.061 的 `10 ≥ Re(s)`/`Re(s)<101`、p.064 的 `s` 乘积上限均由印刷页确认，未按推测修正。

### 候选工作树状态

本修复仍是 Peer 候选，未集成到 `main`、未推送。候选共同 base/merge-base 为 `037602429d3b009f6fc468c732073eb3ddf9875f`；记录时观察到 main 为 `42ad5ffc8481b31e1ea640c8182a4ef1c19efbec`。根级 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、README 与 MEMORY 未改；须由 Master 在其当前目标上复核 exact candidate OID 后处理集成。
