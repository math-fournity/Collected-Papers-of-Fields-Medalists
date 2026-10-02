# Deng 2018 Strichartz — MinerU Markdown 逐页忠实性审计

> 类型：人工维护的审计记录；对象：Deng–Germain–Guth–Myerson, “Strichartz Estimates for the Schrödinger Equation on Non-Rectangular Two-Dimensional Tori”；范围：Yu Deng 目录内 PDF 与既有 MinerU Markdown。
> 状态：34 页来源比对、既有 Markdown 修复与修复后完整回读复核均已完成；基线差异和最终验证分别记录，结论只涉及转录忠实性。

本审计判断的是既有 MinerU Markdown 是否忠实转录这篇 Schrödinger 方程 Strichartz 估计论文的排印内容。原始 PDF 是文字、公式、脚注和参考文献的裁决依据；逐页文本层对账加上题录页与公式密集页的 PNG 抽验、疑难字形的 300dpi 裁片，能够支持转录忠实性的结论，不能代替对论文定理及证明本身的数学审查。

## 范围与方法

- PDF：[Deng_2018_strichartz.pdf](Deng_2018_strichartz.pdf)，34 页；Creator 为 LaTeX with hyperref，Producer 为 dvips + GPL Ghostscript GIT PRERELEASE 9.22；文本层约 79,580 bytes，U+FFFD 计数为 0；SHA-256 为 6987354755fee2b7960f9cf6986d0cebaa4a733f0319230bbc7fd1b9399c1948。
- 既有 MinerU Markdown：[Deng_2018_strichartz__Deng_2018_strichartz.md](Deng_2018_strichartz_mineru/Deng_2018_strichartz__Deng_2018_strichartz.md)；审计基线 HEAD 为 1d124155593a6f61fa92650a7fd930275a29762e，原始 Markdown SHA-256 为 fdf52e47ada42ca6fdd49c21b70d54538bdfe012dfc525a817b8e43107c42203。
- 全文来源通道：逐页运行 pdftotext -enc UTF-8 -layout -f N -l N Deng_2018_strichartz.pdf -，与 Markdown 的连续正文、公式、编号、脚注和文献次序对账；差异以印刷页裁决。
- 150dpi PNG 抽验：题录页与两页数学内容样本分别保存为 [p001](audit/Deng_2018_strichartz_p001.png)、[p008](audit/Deng_2018_strichartz_p008.png)、[p010](audit/Deng_2018_strichartz_p010.png)（pngmono）。样本核对题名/作者/摘要、密集公式以及 (3.3a)–(3.3e) 编号，不代表逐页图像抽验。
- 字形与公式仲裁所需的 300dpi 裁片均在 audit/300dpi/；包括题名重音、\widetilde{\Delta}、\widehat f_k、初始数据、方程编号、证明结束方框、Pall 公式、(6.7) 不等号及作者地址等定位图。
- 未启动、停止或重配 MinerU 服务，未下载模型、未用远程解析；仅使用现有 Markdown。共享进度日志与索引由主集成人维护。

## Claims / Evidence

**Claim.** 基线 Markdown 存在可定位的文字、结构和数学转录差异。修复后以原始印刷页为准，保留源级拼写/语法错误并记录；本文不审查数学定理及证明的正确性。

**Evidence.** 下表列出 34 个 PDF 页的对账范围和基线差异。FAIL 表示原始 Markdown 有需改动的内容；PASS± 表示已核对的现象仅为排印或来源原样，不能据此改写原文。

| PDF 页 | 页级比对内容与基线发现 | 基线结果 |
|---:|---|---|
| 1 | 题名、作者、摘要、(1.1) 开头；题名 Schrödinger 重音被拆成 sup 标记，页边 arXiv 版本印记漏录，正文有拼写误识。 | FAIL |
| 2 | (1.1)–(1.6) 背景与环面设定；they deduce 误成 the deduce，d-dimensional 漏连字符，x∈M 的 ∈ 丢失，cutoff 等拼写误识。 | FAIL |
| 3 | Conjecture 1.1 与二维分段估计；分段列表项目符号/For 标记损坏，10 被拆字，cutoff 误识。 | FAIL |
| 4 | Theorems 1.1–1.2 与 Remark 1.3；If 被拆成 I f，p=10 拆字，As a 与行内文字标记损坏。 | FAIL |
| 5 | (1.7)、Weyl 核和 level-set 定义；Eλ 中的 \widetilde{\Delta} 被转成 \bar{\Delta}，出现行首多余 e、bcan，两个小节要点丢项目符号。 | FAIL |
| 6 | 计数论证与 (1.8) 后的加权计数估计；Nₖ^(1/k) 后多出 2，coefficients 拼写错误及 p=16 拆字。 | FAIL |
| 7 | 高维展望、Notation 与 acknowledgements；‖x‖ 的主语符号漏录，特征函数集合误加下标，\widehat f_k 被误排为 \widehat{f_k}，项目符号丢失；P.G./L.G./S.M. 致谢顺序错且 S.M. grant 重复。 | FAIL |
| 8 | §2 启发式 (1)–(3)；初值被误成 f_i，其余关键大小公式由印刷页确认，a integer multiple 是原刊原样。 | FAIL |
| 9 | §2 结尾与 Lemma 3.1；Similar sums 前多出 e，differencing 误识；证明结束方框被编码为控制字符。 | FAIL |
| 10 | Proposition 3.2 与 Minkowski minima 条件；(3.3a)–(3.3e) 编号错位/空标签。 | FAIL |
| 11 | (3.4a)–(3.4d)、Lemma 3.4；基线四个公式标签整体错后一位，(3.4a) 孤立在首式前、末式漏标；另有标签引用需与 (3.3b)–(3.3e) 对齐，n′₂≠0 后多余 2。 | FAIL |
| 12 | Lemma 3.4 估计汇总、两种 dyadic regime 与 Proposition 3.2 结论；源文两项项目符号丢失，different 拼写误识。 | FAIL |
| 13 | Proposition 3.2(ii) 平均值证明与 S₁ 分解；focuse on the former 是原刊拼写，保留。 | PASS± |
| 14 | Lemma 3.3 的平方差分展开；ε′|p₁| 被误排为带波浪的 p₁，项目符号缺失。 | FAIL |
| 15 | Lemma 3.4 的兼容性条件 (3.8)；1 误成 i，measure 上界排版被拆成不完整的 array/min 片段。 | FAIL |
| 16 | 三组 measure 界与 §4 kernel decomposition；第三组分子 1 误成 i，最终 min 上界结构损坏；Sμ 印刷定义确实没有绝对值符号，保留并登记。 | FAIL |
| 17 | J₃ 分解及 (4.1)–(4.2) level-set 推导；Cauchy–Schwarz 前多余 e，distinguished 被拆字，\widetilde{\Delta} 页图核实。 | FAIL |
| 18 | §4 尾部积分与 §5 起始；12、10、14 等数字被拆字；Our aim 前多余 b。 | FAIL |
| 19 | Theorem 5.1、(5.1)–(5.2) 和 Pall 工具引入；证明结束方框存为控制字符。 | FAIL |
| 20 | Pall 公式 (6.2) 前置条件；Δ 漏掉 C′² 中平方，二次型加号出现伪点，δ₁ 的 +1 误成重音符号，Corollary 6.3 证明方框为控制字符。 | FAIL |
| 21 | §6.2 preliminaries 与 (6.3)–(6.6)；三处 16 被拆成 1 6。 | FAIL |
| 22 | (6.7) 与退化条件；第二个比较符号方向被转成 \succeq，判别式条件的正文和公式结构被拆乱。 | FAIL |
| 23 | Lemma 6.4 收尾及 (6.10)；m q²/d 被识成带点/横线变量，h,U,V 定义多出点/横线，证明结束方框编码为控制字符。 | FAIL |
| 24 | Lemma 6.5 与 optimistic bound；∼ 漏录，split off 误成 split of，sufficient 少 f，12/10 指数拆字。 | FAIL |
| 25 | (6.14)–(6.16) 三类求和分割；Write × 的运算符漏录，W 分量多横线，12 指数拆字。 | FAIL |
| 26 | Lemmas 6.6–6.7 与 Φ³ 界；12 指数被拆字。 | FAIL |
| 27 | Lemma 6.7 的算术估计；只涉及 U₂,V₂,W₂ 的求和多出 (i=0,1,2)。 | FAIL |
| 28 | (6.18)–(6.19)、Δ 展开及 H,G,T 估计；U₂ 的数字误设为罗马体。 | FAIL |
| 29 | 对 G、M 最大化后的最终上界；h₁²V₁ 上多出横线，12/14/15 指数拆字，(6.18) “equalities” 前的 ∼ 漏录。 | FAIL |
| 30 | Theorem 6.1 收尾与 Theorem 7.1；p=10 数字拆字；后续推导中的 L^p([0,T]) 记法按 PDF 印刷原样保留。 | FAIL |
| 31 | §7 退化项与 Pell 计数；Σzᵢ²=m 损坏，β 多出帽，if/is/get 标记损坏。 | FAIL |
| 32 | Appendix A 的 (A.1)–(A.3) 推导；dim V 后多出冒号；exponenetial、intepret 是印刷原样，保留。 | FAIL |
| 33 | References [1]–[27]；Götze、Gérard、Müller、Schrödinger 的重音误识，Reference [3] nonlinear 漏 r。 | FAIL |
| 34 | 四位作者地址；Rydin Myerson 的 Universität/Göttingen/Bunsenstraße 重音字符和空格错位。 | FAIL |

## 印刷原文差异与保留项

以下可疑词句在 PDF 文本层或页图中与印刷品一致，按来源保留，不作为 MinerU 错误修正：

- p.1 “on the other hands”；p.2 谱条件句中 “the spectrum of Δ_M the torus is rational”；
- p.5 “The approach which was has been sketched”；p.6 “one in interested”；
- p.8 “a integer multiple”；p.9 “this give examples”；
- p.13 “focuse on the former”；p.14 “dedending”；p.15 “staisfying”；p.22 “satisying”；
- p.25 “Consquently”；p.27 “there are most O(N^ε)”；
- p.32 “exponenetial” 与 “intepret”；
- p.4 Remark 1.3 的原刊引号形状；p.16 Sμ 定义内对 K_N 的无绝对值写法。

## Conflicts / Unknowns

- 无需求/实现冲突；PDF 是唯一排印裁决源。本次只判断转录忠实性，没有判断 Strichartz 定理的真伪或证明有效性。
- MinerU doc_id 未从任务允许读取的 Markdown 中获得；没有启动或重跑 MinerU，因此不声称新解析结果。
- 150dpi 图像仅覆盖规定的题录页与两页数学样本；其他页面通过 born-digital 文本层全篇对账。疑难符号采用所列 300dpi 裁片仲裁。
- 主集成目标工作树在审计期间为 HEAD 1e65cbafe0346988fdb0a932be2b2a451004ed39 且有其他根级未提交资产；本候选仍绑定本工作树基线 1d124155593a6f61fa92650a7fd930275a29762e。根进度/索引及集成状态由主集成人处理。

## Mutations

- 新增此页级审计记录及 audit/ 内的规定样本/仲裁图；source PDF 保持只读。
- 修复后的 MinerU Markdown 已作为独立 fix 提交 `89626f5b0d57ceddef0b8ba12a8fc42519bf8c8c`，仅触及本目录内的单个 Markdown 文件；页级差异表保留的是修复前基线发现。

## Verification

- pdfinfo：34 页；pdftotext born-digital 文本层 79,580 bytes，U+FFFD 为 0。
- 题录/数学样图：[p001](audit/Deng_2018_strichartz_p001.png)、[p008](audit/Deng_2018_strichartz_p008.png)、[p010](audit/Deng_2018_strichartz_p010.png)，均为 pngmono 150dpi。
- 300dpi 仲裁图：题名 [p001](audit/300dpi/Deng_2018_strichartz_p001_title.png)，公式 [p004](audit/300dpi/Deng_2018_strichartz_p004_formula.png)、[p005](audit/300dpi/Deng_2018_strichartz_p005_kernel-symbol.png)、[p007](audit/300dpi/Deng_2018_strichartz_p007_fourier-coefficient.png)、[p008](audit/300dpi/Deng_2018_strichartz_p008_initial-data.png)、证明方框 [p009](audit/300dpi/Deng_2018_strichartz_p009_proof-marker.png)、编号 [p010](audit/300dpi/Deng_2018_strichartz_p010_equation-tags.png)、[p016](audit/300dpi/Deng_2018_strichartz_p016_S-mu.png)、[p016](audit/300dpi/Deng_2018_strichartz_p016_measure-factors.png)、[p017](audit/300dpi/Deng_2018_strichartz_p017_level-set.png)、Pall 公式 [p020](audit/300dpi/Deng_2018_strichartz_p020_pall-formula.png)、证明方框 [p020](audit/300dpi/Deng_2018_strichartz_p020_proof-marker.png)、不等号 [p022](audit/300dpi/Deng_2018_strichartz_p022_inequality-67.png)、[p023](audit/300dpi/Deng_2018_strichartz_p023_scaling-variables.png)、证明方框 [p023](audit/300dpi/Deng_2018_strichartz_p023_lemma64-proof.png)、[p030](audit/300dpi/Deng_2018_strichartz_p030_l10-bound.png)、[p030](audit/300dpi/Deng_2018_strichartz_p030_level-domain.png)、[p031](audit/300dpi/Deng_2018_strichartz_p031_degenerate-sum.png)、[p031](audit/300dpi/Deng_2018_strichartz_p031_pall-sum.png)、[p033](audit/300dpi/Deng_2018_strichartz_p033_references.png)、[p034](audit/300dpi/Deng_2018_strichartz_p034_address.png)。
- 修复后完整回读覆盖 Markdown 全部 1,783 行；回读发现并补修第 11 页四个公式标签的整体错位：清除首式前孤立 `(3.4a)`，依次将四条不等式标为 `(3.4a)`–`(3.4d)`。以 PDF 第 11 页视觉核验和 `pdftotext` 结果复核编号与不等式，随后再次完成全文回读。
- 修复后转录复核结论：`PASS`。34 页基线差异均已修复或作为原刊原样项目明确保留；完整回读中未发现额外转录差异。此结论不评价论文定理或证明的数学正确性。
- 最终 Markdown SHA-256：`60f572494701abc6fe95882c753a3b0f86660a98f866cc7767d8a25d8910dd1b`；UTF-8 内容 124,500 bytes、1,783 行，禁用控制字符为 0。
- `git diff --check` 与修复提交前的 `git diff --cached --check` 均通过；fix commit `89626f5b0d57ceddef0b8ba12a8fc42519bf8c8c` 的净差异为 128 行新增、126 行删除。该行数是 Git diff 统计，不等同于独立语义修复数。

## Recommendation

本目录的页级审计、手工修订及完整回读复核已完成。由主集成者核对候选基线与目标 HEAD 后，维护根级 `AUDIT-INDEX.md` 和 `AUDIT-PROGRESS.log` 并决定集成；本候选没有修改这些根级文件，也没有 push。
