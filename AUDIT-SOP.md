# AUDIT-SOP — MinerU Markdown 逐页视觉审计规范

> 依据：2026-09-29 Mori 论文审计案例（五点抽查 + 逐页扩展）沉淀。
> 要求：**审计一页，产出一份审计说明**——逐页交错进行（渲染→目检→比对→落签），禁止
> 先全部渲染/全部加载后再批量输出。

## 最高目标（本 repo 的验收定义；先读）

本 repo 最终要收录的是：**全部论文 PDF + 它们的「修复后的 Markdown」+ 修复日志/报告**。

- **修复后的 Markdown** = 以 mineru 原始产出为底，按逐页审计发现的问题**实际修复**（不是只写建议）。
- **修复日志/报告** = 各论文 `AUDIT-<短名>.md`（问题/证据/等级/修复建议/**修复登记**）+ `AUDIT-PROGRESS.log`
  （逐页进度）+ `AUDIT-INDEX.md`（总账）+ **git 历史**（原始 mineru 产出 → 每次修复的精确变更）。
- **目的：让未来第三方能够有效审计本 repo 的工作**——任一条结论都能追到页面、原图、md 行与提交；
  任一处修复都能追到依据（审计记录）与原始 mineru 产出。
- 因此四条不可漂移的纪律：①**审计伴随修复闭环**（FAIL 必改 md、独立 `fix(md): …` commit、总评追加修复登记）；
  ②**提交密集**（每页一提交），保证所有变更细节与初始来源可追踪；③PDF、原始 mineru 产出与修复后 md
  **三者并存于历史**，任何修改不得覆盖来源链（禁止改写历史）；④**审计图片是资产、是 git 追踪目标**——
  所有渲染图（150dpi 页图、300dpi 仲裁裁剪/证据图、图表截图等）必须存放在 repo 的 `audit/`（或论文目录）内
  并随审计提交；**禁止把审计图片只放在 `/tmp`**（`/tmp` 只作瞬时中转，收尾前必须落库）。

## 流程（每页 7 步）

1. **渲染二值化 PNG**（1-bit，`pngmono`，150dpi，页码对齐原文印刷页码）：
   ```bash
   gs -q -dNOPAUSE -dBATCH -sDEVICE=pngmono -r150 \
      -dFirstPage=N -dLastPage=N -sOutputFile=audit/pNNN.png <paper>.pdf
   ```
2. **读取该 PNG**（视觉端逐页查看，一次一页）。
3. **读取 MinerU 输出中该页对应的 Markdown 段**（`full.md` 按页界/内容定位）。
4. **五点比对**（按论文类型裁剪）：
   - 题录页：标题/作者/期刊卷期页码/脚注；
   - 正文页：节标题顺序、定义-定理-引理编号与陈述、公式（系数/指数/上下标）、
     记号约定、行间关系；
   - 文末页：参考文献逐条（作者/刊名/卷页年）、收稿日期。
5. **该页审计说明落签 + 立即记进度**：把该页说明追加写入本目录 `AUDIT-<论文短名>.md`；随后**立即**用
   shell 追加一行到 repo 根 `AUDIT-PROGRESS.log`（见「进度追踪」节）——会话可能随时因 AI 用量上限中断。
6. **发现问题分级**：
   - `PASS` 全部吻合；
   - `PASS±` 有瑕疵但不误导（例：上标拍平 f^*→f*、Fraktur 混排）——列出具体位置；
   - `FAIL` 数学内容错误/整段丢失——记录并注明"以原图为准"。
7. **下一页**。全部页完成后在文件头补「总评 + 抽查覆盖声明 + mineru doc_id」。

## 审计说明格式（一页一条）

```markdown
## p.0NN（PDF p.N / 印刷 p.X）
- PNG：audit/pNNN.png（pngmono 150dpi）
- 核对：[题录|定理X陈述|公式(YY)|参考文献Z-Z|…]
- 结果：PASS｜PASS±（差异列表）｜FAIL（差异列表）
- 备注：（可选：mineru 已知瑕疵类型、建议阅读方式）
```

## 进度追踪（每页；抗中断）

会话可能因 AI 用量上限或其它原因**随时停止**，因此**每页落签后必须立即追加一行进度**到 repo 根
`AUDIT-PROGRESS.log`（append-only）。用最快的方式——shell 追加，不做额外格式化：

```bash
echo "$(date '+%Y-%m-%d %H:%M') | PAGE | <论文短名> | p.N/总页 | <PASS±/FAIL> | <一句话备注>" >> AUDIT-PROGRESS.log
```

- 论文开始时一行 `START`（含 PNG 渲染状态）；全篇审计 + 总评 + 索引完成后一行 `DONE`（含 commit 短 sha）；
  提交后一行 `COMMIT`（sha + 累计数）。历史论文（≤19）在 `AUDIT-INDEX.md` 有纸级记录。
- 目的：任何时刻停止，接力者只读 `AUDIT-PROGRESS.log` 末尾即可精确恢复「哪篇、哪页、最后等级」。
- 该日志是**过程记录**；`AUDIT-INDEX.md` 仍是进度真值（纸级），最终验收以它为准。

## 审计后修复（FAIL 与内容级瑕疵）

- **FAIL 项默认应在该篇审计完成后修复**，依据只有两样：审计记录中的「以原图为准」事实与修复建议。
- 修复规则：(i) 只改 md，不改 PDF，不改其它件；(ii) **独立 commit**：
  `fix(md): <论文> 按审计修复 …（原始 md 见 <raw commit>）`；(iii) 在对应审计文件「总评」末尾追加一行
  **修复登记**：修复内容 + fix commit sha + 原始 md 所在 commit，保持审计—修复可追溯。
- PASS± 的排版级伪影（ff→f、空格合并、重音分解等）**默认不批量改**；仅当妨碍检索/使用时才批量修复并登记。
- 修复不冒充重新审计；修复后如需再验证，另行落签注明。

## 提交纪律（密集提交、可追踪）

- **每页一提交**：每页落签 + `AUDIT-PROGRESS.log` 追加后，**立即**：
  `git add -A && git commit -m "audit(page): <论文> p.N/总页 <等级>"`——保证逐页变更与时间线可追踪。
- **每篇一提交**：总评 + `AUDIT-INDEX.md`（+ 分卷合计）→ `audit: <篇名> N页审计完成（累计X/85…）`；
  修复另做独立 commit（见上节），不与审计混提。
- 大件分卷按分片各自落签、各自提交（信息注明片号与 PDF 页区间）。
- collection repo 允许 `git add -A`；**禁止 push**；历史只在本地。

## mineru 处理约束

- 云端 standard 档：`mineru parse <pdf> --remote --json`；>200 页文件先 gs 分卷；
- kit 导出（App 同款）：`mineru-kit parse <pdf> -o /tmp/exp --format zip --remote -p 1-N`，
  解压后按 `full.md` + `images/` + `middle_json.json` + `structured_content.json` +
  `origin.pdf` 布局放入论文子目录，命名 `<论文短名>_mineru/`；
- 已知系统性瑕疵：上标偶被拍平、Fraktur/𝒪 混排、⊗ 链下标错位、扫描件专名 OCR 噪声。

## 范围与优先级（2026-09-29 盘点）

85 PDF ≈ 4232 页（含 ICM 报告 2-4 页小件与大部头：Thompson 282、Lafforgue 241、
EGA I 227、Schwartz I/II 352、Hironaka 讲义 139、Wiles 270、Hairer 283、Gowers 124）。
小件先行（Fefferman/Yau 2 页 → Cohen/Kodaira/Milnor 6-8 页 → …），大部头殿后；
每完成一篇在 `AUDIT-INDEX.md` 登记。
