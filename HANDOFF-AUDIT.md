# HANDOFF-AUDIT — 逐页视觉审计任务交接文档

> **致接手 AI**：本文件是「Collected-Papers-of-Fields-Medalists 论文 MinerU 化 + 逐页视觉审计」
> 任务的唯一交接手册。不需要任何对话历史，按本文执行即可。
> 上次更新：2026-09-29。交接时进度：**12/85 篇审计完成；mineru 解析 54+/86 在后台运行中**。

---

## 0. 任务是什么（一句话）

把本 repo（`/Users/aurolafly/Collected-Papers-of-Fields-Medalists/`）中 68 位菲尔兹奖得主的
全部 85 个论文 PDF（≈4232 页）逐一：

1. 用 MinerU 处理成 Markdown（含 middle_json/structured_content/images）放入对应子目录；
2. **按 SOP 逐页二值化视觉审计**——每页渲染二值化 PNG、目检原文、与该页 Markdown 比对，
   **看完一页立刻写一条该页的审计说明**（禁止全部加载后批量补写），
   审计文件为各论文目录下的 `AUDIT-<短名>.md`；
3. 全部完成后 `AUDIT-INDEX.md` 全绿。

## 1. 权威文件与路径（全部已存在，勿重建）

| 资产 | 路径 |
|---|---|
| **本 repo（工作对象）** | `/Users/aurolafly/Collected-Papers-of-Fields-Medalists/`（独立 git repo，直接 `git add -A && git commit` 即可，勿 push） |
| **审计 SOP（规范原文）** | `AUDIT-SOP.md`（repo 根）——渲染命令、七步流程、签体格式、PASS/PASS±/FAIL 分级 |
| **进度总账（唯一进度真值）** | `AUDIT-INDEX.md`（repo 根）——每完成一篇加一行 |
| 论文底稿（repo 内镜像） | `/Users/aurolafly/shuxuedashi-glm5.2-worktree/算思系统/tasks/ot-fields68/corpus/papers/` |
| **MinerU CLI / Kit** | `/Volumes/D/toolchain-cache/mineru-venv/bin/mineru` 与 `…/mineru-kit`（v4.0.8，不在 PATH） |
| mineru 使用规范 | ZCode 用户级 skill `mineru`（`~/.zcode/skills/mineru/SKILL.md`，含云端解析/App 导出/输出 schema 的完整说明——**先读它**） |
| 论文获取方法论（如需补文件） | ZCode 用户级 skills：`~/.agents/skills/math-paper-harvest/`（渠道路由+5 个 references：gdz/numdam-eudml/ams-jstor-msp/mathnet-icm/author-sites/validation-assembly）与 `~/.agents/skills/sciverse-direct-api/` |
| 批量解析脚本（可复用/重跑） | `/tmp/mineru_batch.py`（后台运行中；逻辑：按页数升序、跳过已有 md、>200 页先 gs 分 180 页卷、mineru-kit 导出 zip 解压到 `<base>_mineru/`、md 提升为 `<base>__<zip名>.md`） |
| 解析日志 | `/tmp/mineru_batch.log`（`EXPORT OK/FAIL` 计数即进度） |
| 浏览器（付费墙/人机验证时） | BrowserOS（browseros-neo MCP）；JSTOR 一键导出插件在 `~/Downloads/jstor-page-exporter/` |
| 主任务交接（论文收集阶段的历史） | worktree repo `算思系统/tasks/ot-fields68/HANDOFF-CORPUS.md` 与 `MEMORY.md`（只读参考） |

## 2. 当前精确状态（交接时点）

### 已完成逐页审计的 12 篇（勿重做）

| 目录 | 论文 | 页数 | 审计文件 | 特别发现 |
|---|---|---|---|---|
| 1990年 - Mori | ample tangent bundles | 14 | （full.md 已核，五点抽查模式） | 首个示范 |
| 1978年 - Fefferman | BMO | 2 | AUDIT-Fefferman.md | running head 丢失 |
| 1982年 - Yau | Calabi 猜想 | 2 | AUDIT-Yau.md | **300dpi 公式仲裁案例**（md 正确，目检误读） |
| 1986年 - Faltings | 勘误 | 1 | AUDIT-Faltings_erratum.md | |
| 1970年 - Baker | Turán 官方报告 | 2 | AUDIT-Baker_work_report.md | **⚠️ md 末尾 mineru 幻觉段落**（"Ground Truth image…"，引用须剔除） |
| 1970年 - Hironaka | Grothendieck 官方报告 | 3 | AUDIT-Hironaka_report.md | 标题 OCR 错 "L'À"（应为 LA）；Grothendieck 著名脚注完整 |
| 1970年 - Novikov | Atiyah 官方报告 | 3 | AUDIT-Novikov_report.md | 全 PASS |
| 1954年 - Kodaira | Analytic stacks | 6 | AUDIT-Kodaira.md | PDF 含 Kodaira-Spencer 短文开头（白赚）；公式 (1)-(10) 逐条 |
| 1966年 - Cohen | 连续统假设 | 6 | AUDIT-Cohen.md | forcing 定义/𝔉₁-𝔉₈/5 个 Lemma 逐字；前后邻文页面自然截断 |
| 1962年 - Milnor | 异纬 7 球面（扫描件） | 7 | AUDIT-Milnor.md | 脚注碎片化；M_k^7→M_k^T 一处 OCR 错；分段函数 tag 拆散 |
| 2006年 - Perelman | Finite extinction | 7 | AUDIT-Perelman_finite_extinction.md | **⚠️ p6 多余 "4"（经 arXiv LaTeX 源码仲裁确认为幻觉）**；作者原始 LaTeX 源码已存档（`…_arxiv_source.tex`） |
| 1990年 - Jones | 结多项式 | 9 | AUDIT-Jones.md | 24 定理+2 表逐条；表格转文本（数据完整、对齐需对照原 PDF） |

### mineru 解析状态

- 后台批次运行中（PID 见 `ps aux | grep mineru_batch`；若已中断，直接重跑
  `python3 /tmp/mineru_batch.py`——脚本自动跳过已完成的）。
- 交接时点 54/86 EXPORT OK，正在处理 ribet1990 (47p)。`EXPORT FAIL` 计数=0。
- 大文件（>200 页）会被脚本自动分 180 页卷：Thompson 282、Lafforgue 241、Schwartz II 210；
  **解析后 md 会按 zip 分片命名**（如 `Thompson_Feit_1963_odd_order__part01.md`）——审计时按
  分片顺序接力即可，签名里注明对应 PDF 页区间。

## 3. 接力执行程序（每篇照此办理）

1. **选取下一篇**：`AUDIT-INDEX.md` 中无 "✅ 完成" 行、且 mineru 已导出（存在
   `<base>_mineru/` 与 md）的 PDF，按页数升序优先（小件快、先建覆盖）；若 mineru 未就绪，
   先做别的或等待/补跑批次。
2. **渲染二值化 PNG**（一次渲整篇，SOP 命令）：
   `gs -q -dNOPAUSE -dBATCH -sDEVICE=pngmono -r150 -sOutputFile=<dir>/audit/p00%d.png <pdf>`
   （**先 `mkdir -p <dir>/audit`**，否则 gs 静默失败）。
3. **逐页循环**（核心纪律）：读第 N 页 PNG → 读 md 中该页对应段 → 五点比对
   （题录/定理陈述/公式上下标/记号/参考文献）→ **立即追加该页签**到 `AUDIT-<短名>.md`
   （格式照 SOP；分级 PASS / PASS± / FAIL）→ 下一页。
4. **疑难仲裁**（md 与二值图不一致时按此顺序取真值）：
   ① 300dpi 灰度渲染局部（`-sDEVICE=pnggray -r300` + sips 裁剪）；
   ② arXiv 论文直接拉 LaTeX 源码（`https://arxiv.org/e-print/<id>`，gunzip 后 grep——
   Perelman "4" 案例即此法）；
   ③ 出版商官方页对照。
5. **收尾**：签体加「## 总评」（覆盖声明+系统性瑕疵+可用性结论）→ 在 `AUDIT-INDEX.md`
   加一行 → collection repo `git add -A && git commit`（信息格式：`audit: <篇名> N页审计完成（累计X/85）`）。

## 4. 已知坑清单（全部踩过，勿再踩）

- **mineru 幻觉**：会把装饰线/分隔线编造成"Ground Truth image…OCR 说明"段落（Baker 案例）、
  或无中生有字符（Perelman "4"）——审计时对 md **末尾段落与孤立字符**保持警惕，必要时
  LaTeX 源码/300dpi 仲裁。
- **running head/页码/版权行**：mineru 系统性丢弃（每篇 PASS± 都会见到）——记录一次即可。
- **脚注碎片化**：脚注常被拆成多个碎片段散置于 md（Milnor 注 ² 5 碎片）——核对完整性而非顺序。
- **PNAS/期刊 PDF 物理边界**：下载件常含前文尾/后文头（Cohen/Kodaira 案例）——转写正常，
  签名注明"自然截断"。
- **arXiv 论文**：md 忠实保留原文拼写错误（Perelman "difeomorphic"、Yau 论文 "latter"）——
  忠实≠错误。侧栏 arXiv 戳记/下载水印列不收（惯例）。
- **`file` 页数误读**：线性化 PDF 首节点页数不可信（Gowers 124 页曾误读为 10）——用 `pdfinfo`。
- **图片转 PDF**：本机 PIL 无 JPEG 编码器（KeyError:'JPEG'）→ 用 img2pdf（已装，
  `--break-system-packages`）；gs 处理图片输入报 /undefined。
- **sips 裁剪**：`--cropOffset a b` 的参数序是 (x, y)（从左上起）——裁剪后必须目检确认位置。
- **gs 渲染前必须 mkdir audit 目录**（否则静默失败 "Could not open the file"）。
- **mathnet.ru**：本机 curl 不可达（000），**用户浏览器可达**（Drinfeld/Baker 俄译均由用户
  下载）——需要时可请用户开 `mathnet.ru/php/getFT.phtml?jrnid=…&paperid=…&what=fullt`。
- **>200 页 PDF** mineru 云端拒绝——脚本已自动分卷，md 分片接力审计。

## 5. 内容缺口（"不留遗憾"遗留项，均已有垫底件，非阻塞）

| 项 | 现状 | 补齐渠道 |
|---|---|---|
| Baker 英文原版（Mathematika 13, 1966, 204-216） | 已有俄译版 | Wiley `10.1112/S0025579300003971`（付费，用户可试） |
| Bombieri 1970 Addendum | ✅ 已收（GDZ vol11 LOG_0020） | — |
| Mirzakhani JAMS 版 | 已有 Stony Brook 全文版 | ams.org jams 2007-20-01（consent 拦截，用户手动点） |
| Serre 1951 Homologie singulière | 已有 GAGA(1956) 代表 | Annals/JSTOR |
| Margulis 英译（RMS 29:4） | 已有俄文原文 | IOP 付费 |
| Novikov 1965 原文 | 已有 1967 英译 86 页 | mathnet（用户浏览器） |

## 6. 验收标准（任务完成的定义）

- [ ] `AUDIT-INDEX.md` 85 行全部带 "✅ 完成（N/N）"；
- [ ] 每篇目录存在 `AUDIT-<短名>.md` 且页数签数 = pdfinfo 页数（分卷论文按分片合计）；
- [ ] 每篇目录存在 `*_mineru/`（md + 附属 JSON/图片）；
- [ ] 全部 PASS 或 PASS±（FAIL 项需有"以原图为准"注记与修复建议）；
- [ ] collection repo git 干净、全部提交（本地即可，**禁止 push**）；
- [ ] worktree repo `MEMORY.md` 有对应的收尾登记（用
  `/Users/aurolafly/codex/tools/check_file_baseline.sh` 检查后再改）。

## 7. 纪律红线（来自全局 AGENTS，审计任务同样适用）

- 集合 repo 可 `git add -A`（个人档案库）；**worktree repo 严禁**——只精确 add 路径；
- 任何 push、-force、tag 移动一律禁止；token/credential 不入 git 不入回答
  （sciverse token 在 gitignored 的 `.zcode/config.json`，勿外传）；
- 不写 ArangoDB/Redis/外部服务；不启动 Solver；不使用 Sub Agent；
- mineru server stop/restart 会干扰用户打开的 MinerU App——禁止执行；
- 审计保持诚实：不确定就写"150dpi 不可分辨，以原 PDF 为准"，绝不脑补 PASS。
