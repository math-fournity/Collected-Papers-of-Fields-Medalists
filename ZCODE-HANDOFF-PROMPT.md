# 交接提示词 —— Collected-Papers-of-Fields-Medalists 逐页视觉审计（2026-10-01 更新）

> 本文件记录工作方法，不是实时仓库状态：篇级进度以 `AUDIT-INDEX.md` 为准，页级断点以 `AUDIT-PROGRESS.log` 为准，当前 branch/HEAD/dirty 状态以实际 `git status` 为准。2026-10-01 核对时索引中有 70 篇完成标记，最新页级记录是 Maynard popular exposition 31/31 DONE（累计 70/140）；接手时仍须重新查询。
> 2026-10-01 已加入用户裁定：剩余篇目 MinerU Markdown 正文修复使用 Edit 逐处手工修改，脚本仅作只读终验清点。此前静态交接数字与本段核对数字不一致时，以 INDEX、PROGRESS 和当前 Git 为准。

你好。你接手 `/Users/aurolafly/Collected-Papers-of-Fields-Medalists`（独立 git repo，branch main）
的「论文 PDF 逐页视觉审计 + mineru md 修复」任务。请把本会话启动在该 repo 根目录（cwd = 该目录），
所有相对路径、git add/commit 都以它为基准。本文件自包含：不需要任何对话历史，按本文执行即可。

## 0. 当前状态（接手时回到实物核对）

- 篇级进度唯一真值是 `AUDIT-INDEX.md`；最近页级断点见 `AUDIT-PROGRESS.log` 末尾。2026-10-01 核对为 **70/140 篇完成**，但此数字仅是本文件此次更新时的快照。
- branch、HEAD、index/working tree 状态和远端是否同步，必须在接手时用 Git 查询；不要把本文件或旧提交说明里的静态状态当作当前状态。
- 身份：`math-fournity <math-fournity@proton.me>`；**push 已获用户常设授权**（直接
  `git push origin main`）；**禁止改写历史 / force push**。
- 远端：`https://github.com/math-fournity/Collected-Papers-of-Fields-Medalists`。
- 最新 DONE 项和中断恢复点一律从 `AUDIT-PROGRESS.log` 实读；不要从本文件的旧候选列表推断下篇。
- 用户总目标（不可漂移）：**按 SOP 处理完所有 140 份文档**。若发生上下文压缩，必须第一时间
  重新恢复 `AGENTS.md`、README/MEMORY/Feature/rulings/docs 路由，再加载本文件、`AUDIT-SOP.md`、
  `AUDIT-INDEX.md` 与 `AUDIT-PROGRESS.log`。

## 1. 接手时恢复认知闭包

1. `AGENTS.md`（项目硬约束，尤其是剩余篇目 Edit 修复和 AI 全文复核要求）
2. `README.md`（72 人 / 70 目录的资产地图）
3. `MEMORY.md`、`feature-list.md`、`rulings.md`（当前状态、需求和原始裁定）
4. `docs/README.md`（稳定知识路由）
5. `AUDIT-SOP.md`（逐页流程、PASS/PASS±/FAIL 分级、print quirk 和图片证据纪律）
6. `AUDIT-INDEX.md`（**篇级总账 = 唯一进度真值**；看哪些篇还没有 "✅ 完成"）
7. `HANDOFF-AUDIT.md`（历史坑点参考；含旧的 20/85 等快照，当前方法冲突时以 SOP、AGENTS 和本文为准）
8. `AUDIT-PROGRESS.log`（只读最后 10 行，恢复正在处理的论文与精确页码）
9. `ZCODE-HANDOFF-PROMPT.md`（本文件，核对本轮接力步骤）

各论文目录内：`AUDIT-<短名>.md`（逐页签 + 总评 + 修复登记）与 `audit/`（150dpi 页图 +
300dpi 仲裁裁片，均为 Git 资产）。

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

并行 worktree 时，使用 `rulings.md#R-002` 和 `AUDIT-SOP.md#AI-身份与并行Worktree日志`：Master 分配唯一 Peer ID；Peer 每页立即在自己的篇级 AUDIT 中记录真实时间、页码、结果、actor/model/effort 并逐页提交，不改根索引/日志；Master 收到精确候选 page commit 后，将原事件时间和 actor 追加到 canonical `AUDIT-PROGRESS.log`。单人串行工作仍由负责工作的 actor 直接追加根日志。不得改写既有 GLM 历史或推断旧身份。

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

### 2.4 逐处手工修复与 AI 全面确认（2026-10-01 用户裁定）

本条适用于尚未完成篇目的 MinerU Markdown 正文纠错和内容级修复。每篇以负责工作的 AI 使用 `Edit` 工具逐处手改为主；修复脚本不再负责写入或替换文本。

1. **先核实问题和证据**：结合 §2.1–2.3 确认疑点所在 PDF 页、Markdown 上下文及印刷原文。字形或公式不能由文本提取唯一确定时，用本提示词要求的 PNG/300dpi 原图仲裁。print 里的拼写或编号即使看似错误，也按 §2.3 忠实保留并在 AUDIT 中登记。
2. **通过 Edit 逐处修改**：每个实际出现位置单独判断并编辑；不得将一组查找/替换规则写成 Python、正则、`sed`、Perl、heredoc 或其它可批量改写 Markdown 的脚本。若 `Edit` 工具不可用，暂停该篇并报告，不切换到写文件脚本。
3. **留下可追溯记录**：每条修复在 `AUDIT-<短名>.md` 中记录 PDF 页码、原文证据、改动内容和修改后的核对结果；不要只写脚本 applied 数量。
4. **全面复核最终文件**：手工编辑后重新从头阅读最终 Markdown 全文，并按本篇的 born-digital/扫描件模式回核相应页面。逐条验证预期修复已正确落入、没有漏改/重复误改，也没有因编辑引入的新差异；按 SOP 为所有页给出签名和完成声明。
5. **脚本仅作只读终验与清点**：此时可用脚本统计 `\tag`、编号缺失/重复、剩余伪影、待查候选及修复清单覆盖率。脚本不得写回、格式化或自动修复目标 Markdown；脚本 PASS 只证明对应机械检查通过，不能替代 AI 的原文判断和全文复核。终验发现问题时，返回 `Edit` 逐处手改并重跑只读清点。

“AI 全面确认”只可在可见证据覆盖上述步骤时声称；处理速度放慢是用户明确接受的取舍。此规则不要求重做已完成篇目，也不改变 MinerU 初始导出、PDF/PNG 只读检查、逐页签、AUDIT 登记或 Git 来源链纪律。

### 2.5 收尾三段提交（顺序固定）+ push

```bash
git add "<论文目录>/AUDIT-<短名>.md" "<论文目录>/audit"
git commit -m "audit(page): <短名> p.N/N <等级> [<actor> | <model>/<effort>]"
git add "<论文目录>/<base>_mineru/<base>__<base>.md"
git commit -m "fix(md): <短名> <细节> [<actor> | <model>/<effort>]（修复前 md = 父提交；<证据链>；<源级登记>）"
# AUDIT 文件追加「### 修复登记」+ AUDIT-INDEX.md 追加一行 + AUDIT-PROGRESS.log 追加 DONE/COMMIT
git add "<论文目录>/AUDIT-<短名>.md" AUDIT-INDEX.md AUDIT-PROGRESS.log
git commit -m "audit: <篇名> N页审计完成 [<actor> | <model>/<effort>]（累计M/140）"
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

先将 `README.md` 的论文资产地图与当前 PDF 文件清单对账，再检查 `AUDIT-INDEX.md`。索引里的已有行不是待办全集：若 README/磁盘中存在尚无索引行的 PDF，先确认其确为独立篇目、读取 `pdfinfo` 页数并确认对应 MinerU 输出已存在；然后在 `AUDIT-INDEX.md` 新增唯一一行，状态记为“审计中”，再开始该篇。不得因为 INDEX 当前只有已完成行就漏掉未登记 PDF，也不得把未完成项计作完成。

从所有尚未完成且 MinerU 文件已可用的篇目中，按实际 PDF 页数升序选择；同页数按 README 中的顺序稳定择一。不要使用早期接力提示里固定或重复的候选清单，因为它会随审计进度过期。

接到用户开始或继续审计的指令后，先核对 `AUDIT-PROGRESS.log` 末行；若恢复的是未登记篇目，先补 INDEX 行；随后按 §2.1 记录 START/PAGE 行再逐页工作。会话中断后仍以该日志和 INDEX 作为恢复入口。

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
