# 交接提示词 —— Collected-Papers-of-Fields-Medalists 逐页视觉审计（2026-09-30 深夜快照 · 第七轮）

> 把本文件全文作为新 Session 的第一条消息发给 ZCode 的 AI。快照：2026-09-30 深夜，git HEAD `6e34e140`，
> 进度 **63/140**，working tree 干净，已推送 origin/main。旧 09-29 版（20/85 快照）已被本版取代，
> 旧内容在 git 历史中可查。

你好。你接手 `/Users/aurolafly/Collected-Papers-of-Fields-Medalists`（独立 git repo，branch main）
的「论文 PDF 逐页视觉审计 + mineru md 修复」任务。请把本会话启动在该 repo 根目录（cwd = 该目录），
所有相对路径、git add/commit 都以它为基准。本文件自包含：不需要任何对话历史，按本文执行即可。

## 0. 当前状态（权威快照，先信这里）

- 进度：**63/140 篇完成**（`AUDIT-INDEX.md` 含 63 个 "✅ 完成" 行），HEAD = `6e34e140`，
  working tree 干净，**已推送** origin/main。
- 身份：`math-fournity <math-fournity@proton.me>`；**push 已获用户常设授权**（直接
  `git push origin main`）；**禁止改写历史 / force push**。
- 远端：`https://github.com/math-fournity/Collected-Papers-of-Fields-Medalists`。
- 上一会话（2026-09-30 晚—深夜，第七轮）闭环 4 篇共 129 页：
  McMullen 1991 Cusps（60，`016dc296`）、Maynard 2015 published（61，`6f189700`）、
  DePhilippis–Figalli 2015 published（62，`b5c63fe7`）、Bhargava–Shankar 2015 published
  （63，`6e34e140`）。
- **账实已对齐**：第六轮曾报 "累计 60/140" 系虚高（INDEX 中 Mori 1979 重复两行 + Okounkov
  2003 JAMS 闭环件漏登）。本会话已修正：Okounkov 补行、Mori 并行，`AUDIT-INDEX.md` 现有
  63 行全部带 "✅ 完成"，与 git 历史逐一对账相符。**进度唯一真值 = `AUDIT-INDEX.md`**，
  交接词与口头数字一律以其为准。
- 用户总目标（不可漂移）：**按 SOP 处理完所有 140 份文档**。若发生上下文压缩，必须第一时间
  重新完整加载本文件 + `AUDIT-SOP.md` + `AUDIT-INDEX.md`。

## 1. 第一件事：按顺序读 6 个文件

1. `README.md`（资产地图：72 人 / 70 目录 / 140 PDF 的分节索引）
2. `AUDIT-SOP.md`（规范：逐页流程、PASS/PASS±/FAIL 分级、FAIL 必修、图片资产纪律）
3. `AUDIT-INDEX.md`（**篇级总账 = 唯一进度真值**；看哪些篇还没有 "✅ 完成"）
4. `HANDOFF-AUDIT.md`（接力手册与坑清单；其 "20/85" 计数是旧快照，以本文件和 INDEX 为准）
5. `AUDIT-PROGRESS.log`（**只读最后 10 行** = 你的精确恢复点；末行 = Bhargava 2015 published
   DONE/COMMIT，63/140）
6. `ZCODE-HANDOFF-PROMPT.md`（本文件）

各论文目录内：`AUDIT-<短名>.md`（逐页签 + 总评 + 修复登记）与 `audit/`（150dpi 页图 +
300dpi 仲裁裁片，均为 git 资产）。

## 2. 单篇工作循环

### 2.0 选篇

`AUDIT-INDEX.md` 中无 "✅ 完成" 行、且 mineru 已导出（存在 `<base>_mineru/`）的 PDF，
**按页数升序**。若 mineru 未导出：跑 `python3 /tmp/mineru_batch.py`（自动跳过已完成；
运行时脚本若丢失可按 `tools/mineru_batch.py` 重建）。大件（>200p）已被分卷为
`<base>__partNN.md`，按分片接力审计。

### 2.1 判定模式（每篇第一分钟）

```bash
pdfinfo <paper>.pdf | grep -E "Pages|Producer|Creator"
pdftotext <paper>.pdf /tmp/<短名>.txt && wc -c /tmp/<短名>.txt   # 并查 U+FFFD、中文标点
```

- **born-digital**（文本层 >20KB、0 FFFD；Producer 常见 pdfTeX/LaTeX）→ **文本层主对账
  通道 + PNG 抽验**（题录页 + 1–2 页密集数学页整页目检即可；快，约 30–45 分钟/篇）。
  注意：pdftotext 会**丢弃 ≠、∫、Ш、∑ 等字形**（输出里缺失≠print 没有），这类必须 300dpi
  PNG 终裁。
- **扫描件**（文本层空/极短）→ **纯 PNG 审计模式**：全部页面 150dpi pngmono 逐页目检，
  疑点 300dpi 终裁（慢，约 60–90 分钟/篇）。

```bash
mkdir -p audit && gs -q -dNOPAUSE -dBATCH -dSAFER -sDEVICE=pngmono -r150 \
  -sOutputFile="audit/<短名>_p%03d.png" <paper>.pdf
# 300dpi 终裁：-sDEVICE=pnggray -r300 -dFirstPage=N -dLastPage=N，再用 PIL 按比例坐标裁剪
```

被引用为证据的裁片必须 `cp` 进 `audit/300dpi/` 随审计提交；**禁止只留 /tmp**。
每篇开工先记进度：`echo "$(date '+%F %H:%M') | PAGE | <短名> | p.1-N/N | <模式> | 累计M+1篇进行中" >> AUDIT-PROGRESS.log`。

### 2.2 通读 md + 伪影族 grep

完整读一遍 mineru md（长文分段 Read，行要读全），同时 grep 伪影族：
丢箭头（`$X  Y$` 双空格 = → 丢失）、变音拆裂（´e、¨、ˇ）、ff 连字（diferent/coeficient/
suficient/efective/unafected…）、数字逐位拆分（`2 7 B`、`1 0 5`、`1 . 1 7`、`1 4 1 7 2 5 5`）、
双分号、`",$"`、幽灵下标、docvortex 足注碎片、`\x03`（**born-digital 里常为 print 墓碑 □ 的
私有编码字形，应还原为 □ 而非删除**）、`~~`、裸编号行 `(N.M)`、letter-spaced 操作符
（`\operatorname*{l i m i n f}`、`{m a x}`、`{s u p}`）、smart-quote 乱码（`^{66}`、
`\mathfrak{s}`、`^{7,}`、`^{2,}`）、`\dag`（应 → ∤）、`\mathsf{\Omega}^{1}_{16}`（应 → 1/16）、
HTML sub/sup 残留、重音拆裂（`´e`、`¨`、`ˇ`）、小型大写作者姓丢失（参考文献 "L. A , N. G"）、
斜体边界丢空格（Letf/awayfrom/ofclass/convexfunction/Then,for）、French 式标点错位
（`$g .$.`、`$X .$,`）。

### 2.3 文本层仲裁 + 300dpi 终裁

每个疑点先查文本层（born-digital 可逐字符对账）；字形级疑点（ℓ vs l、重音有无、≠ 有无、
G vs C、分号/逗号、矩阵形状）必须 300dpi 裁片终裁。**print 即权威**：疑似 print 错拼/错号/
笔误（实例：McMullen "PROPOSITION 2.3"、"Bierberbach"、"an ternary"、"possesess"、
Maynard "X^{9/12}"、DeFigalli "R_V^+(X)"、Bhargava "M_p(U₁,F)"、"[0,1]∈ℝ"）一律终裁后
**忠实保留 + AUDIT「源级 quirk 清单」登记**（注明证据 PNG/300dpi/文本层），禁止顺手改正。
注意 pdftotext 的系统性盲区：**丢弃 ≠ ∫ Ш ∑ 等字形**（输出缺失≠print 没有）、重音字符
拆解（à → \`a）、下标上标扁平化。

### 2.4 修复脚本：收敛式（第七轮沉淀，务必照做）

用 Write 工具落盘 `/tmp/<短名>_pub/fix_md.py` 再执行。**禁止多轮 heredoc 内联补丁**
（第七轮在 Bhargava 篇因转义补丁浪费大量轮次——不要重蹈）。已验证可靠的脚本结构：

```python
t = io.open(MD, encoding='utf-8').read()
applied, missed, skipped = [], [], []
def sub(old, new, n):            # 精确规则：计数断言，失败仅记录不中止
    global t
    c = t.count(old)
    if c != n: missed.append((old[:56], n, c)); return
    t = t.replace(old, new)
def try_sub(key, old, new):      # 条件规则：在场才替换（幂等收敛，重跑安全）
    global t
    if old in t: t = t.replace(old, new, 1); applied.append(key)
    else: skipped.append(key)
def rsub(pat, repl, n):          # regex 规则：repl 一律 lambda 化（见铁律2）
    rr = repl if callable(repl) else (lambda m, r=repl: r)
    t2, c = re.subn(pat, rr, t)
    if c != n: missed.append((pat[:56], n, c)); return
    t = t2
# …全部规则…
io.open(MD, 'w', encoding='utf-8').write(t)   # 始终写盘 + 打印 applied/missed/skipped 报告
```

- **转义三条铁律**（第七轮踩遍，勿重蹈）：
  1) regex **pattern** 里匹配 md 的字面反斜杠必须双写（`r'\\frac'` 匹配 `\frac`）；
     `\f \b \t \n \m` 等在 pattern 里是合法转义但含义错误（`\f`=换页）——匹配字面
     反斜杠+字母必须 `\\`；
  2) re.subn 的 **replacement 模板**同样解析转义——凡 repl 含反斜杠一律传
     `lambda m: r'\frac …'`（callable 直通）；
  3) **不要用带反斜杠的字符串去 patch 脚本自身**（双层转义必错，第七轮多次浪费轮次）——
     要改脚本就整文件 Write 重写。
- 规则失败时**禁止盲改**：先对 md 跑探针（`t.count(锚点)` / repr 上下文）拿真实字节再修。
- 规则失败不中止（missed 记录），**写盘后必做终验**：\tag 全量清单（Counter 查重/缺失，
  与 print 逐号对齐——第七轮三篇分别对齐到 106/89/40 组）、**每条意图修复的实际存在性
  检查**（防"部分写盘丢失/前轮覆盖"事故）、残余伪影 grep 全零。

### 2.5 收尾三段提交（顺序固定）+ push

```bash
git add "<论文目录>/AUDIT-<短名>.md" "<论文目录>/audit"
git commit -m "audit(page): <短名> N页签（<模式与伪影族摘要>，K处修复清单）"
git add "<论文目录>/<base>_mineru/<base>__<base>.md"
git commit -m "fix(md): <短名> <细节> 共K处/R规则（修复前 md = 父提交；<证据链>；<源级登记>）"
# AUDIT 文件追加「### 修复登记」+ AUDIT-INDEX.md 追加一行 + AUDIT-PROGRESS.log 追加 DONE/COMMIT
git add "<论文目录>/AUDIT-<短名>.md" AUDIT-INDEX.md AUDIT-PROGRESS.log
git commit -m "audit: <篇名> N页审计完成（累计M/140）"
git push origin main
```

路径含空格与中文，必须引号；**禁止 git add -A**（精确路径）。INDEX 行格式照抄现有行
（含 "✅ 完成（N/N；⚠️<伪影与修复摘要>；<print 原文 quirk> 源级登记）" 与 AUDIT 文件链接）。

## 3. 判例纪律（七轮沉淀，务必遵守）

- **print 即权威**：print 错拼/错号/笔误一律忠实保留 + AUDIT「源级 quirk 清单」登记，
  禁止顺手改正。已有判例：McMullen "PROPOSITION 2.3"（应为 3.4）、"Bierberbach"、
  "H. SHICA"（300dpi 证实 print 实为 SHIGA → 修复）；Maynard "that that"、"an ternary"、
  "possesess"、X^{9/12}、M_p(U₁,F)、[0,1]∈ℝ、[28] "Zbl 06261655" 缺点号；DeFigalli
  "u it is"、(4.4) j/m 指标错配、[26] vol.440、[1][12] 姓丢失（修复）；Bhargava
  R_V^+(X)、"i.e,"、Prop 15 杂散 grave、J. of Math. of Kyoto Univ. 等。
- **方程编号以 print 为准**：裸编号行与 \tag 错位时按 print 重排（mineru 常把编号错后一格，
  或把 print 分立的 (30)/(31) 合并成一个数组）；完成后 \tag 全量清单必须无重复无缺失。
- **足注/文献修复**：足注碎片按 print 重构完整句子（第七轮：Maynard Received/Revised 两行
  整丢已补、DeFigalli fn1/fn2/fn4/fn5 重建、Bhargava fn1 六碎片重建）；参考文献小型大写姓
  被整丢时按文本层恢复（L. AMBROSIO, N. GIGLI and G. SAVARÉ；L. C. EVANS and R. F. GARIEPY）；
  MR/Zbl/DOI 原样保留（含 print 自身笔误）。
- **\x03 处理**：born-digital 里 \x03 通常是墓碑 □（Maynard）或撇号/prime（DeFigalli K′/X′）
  的私有编码字形 → 按上下文还原为 □ / ′，不要删除。
- **journal 事实以 PDF 页眉/DOI 为准**：DePhilippis–Figalli 2015 实为 Ann. Inst. Fourier
  （DOI 10.1007/s10240-014-0064-7）；McMullen 1991 为 Ann. 133 (1991) 217–247；Bhargava
  2015 为 Ann. 181 (2015) 587–621。不凭记忆。
- 不确定的历史结论不复活：只信 AUDIT-INDEX / AUDIT-PROGRESS.log / git。

## 4. 硬纪律（违反即事故）

- push 已授权；**禁止 force push / 改写历史**；三段提交顺序不可乱（fix(md) 的父提交 = 修复前 md）。
- git add 只加精确路径（目录名含空格与中文，必须引号）；提交前可用
  `/Users/aurolafly/codex/tools/check_file_baseline.sh <path>` 核对。
- token/credential 不入 git 不入回答；**mineru server 的 stop/restart 禁止**（会杀用户打开的
  App）；不使用 Sub Agent；不写 ArangoDB/Redis/外部服务。
- 被引用为证据的 PNG 必须在 `audit/`（建议 `audit/300dpi/`）内随审计提交，禁止只留 /tmp。
- mineru 已知系统性瑕疵（判例速查）：上标拍平、花体拍平（𝓛𝓢𝒮𝓖𝔅→普通字母）、Fraktur 混排、
  running head/页码丢弃、脚注碎片化、letter-spaced 操作符、数字逐位拆分、ff 连字、
  斜体边界丢空格、French 式 "$g .$." 标点错位、积分/求和/箭头/关系符丢失（双空格或 f 代替 ∫）、
  Γ 下标错置（Γ_Y→Γ_γ）、\dot/\tilde/\overset 噪声、docvortex 足注 span 碎片。

## 5. 你的第一项任务与队列

按 `AUDIT-INDEX.md` 未勾选行、**页数升序**接力。参考队列（以 INDEX 实时为准，含但不止）：
中小件先行——Borcherds 44p、Mirzakhani simple geodesics published 44p、Tsimerman 52p、
Douglas 59p、Kontsevich published 60p、Quillen 63p、Tao–Green published 67p、Thom 70p、
Smirnov conformal 70p、Scholze published 70p、Huh 2020 lorentzian 60p、Birkar singularities
46p、Okounkov arXiv、Serre GAGA、Avila schrodinger 30p（arXiv 版，published 版已审）、
Lindenstrauss published 79p、Yoccoz 91p、Venkatesh 91p、Birkar fano flips 93p、Gowers 124p、
Wang–Zahl 127p；**大部头殿后**——Mirzakhani simple geodesics 49p、Hironaka I 95p/II 122p/
讲义 139p、Schwartz I 142p/II 209p、Hairer published 236p、Lafforgue 241p、EGA 227p、
Deng 34p/138p/192p、Wiles 270p、Thompson 282p，及 ICM/citation/laudatio 零散小件。

每篇开工先记 PAGE 行（见 2.1），会话可能随时中断，恢复只看 `AUDIT-PROGRESS.log` 末行。

## 6. 汇报格式

每篇闭环后向用户一句话汇报（篇名/页数/修复量/推送 commit）；每 5-10 篇给一次小结
（进度 n/140、本批修复统计、源级登记要点、剩余队列）。遇到无法自主裁决的问题
（如 print 严重自相矛盾且 PNG 不可读），停下向用户说明，不要猜。

## 7. 验收标准（任务完成的定义）

- [ ] `AUDIT-INDEX.md` 140 行全部带 "✅ 完成（N/N）"；
- [ ] 每篇目录存在 `AUDIT-<短名>.md` 且页数签数 = pdfinfo 页数（分卷按分片合计）；
- [ ] 每篇目录存在 `*_mineru/` 与 `audit/`（证据图入库）；
- [ ] 全部 PASS 或 PASS±（FAIL 项需"以原图为准"注记与修复，并登记）；
- [ ] repo git 干净、全部提交并推送 origin/main。
