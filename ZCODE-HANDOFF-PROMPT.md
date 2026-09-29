# ZCode 接手提示词 —— MinerU 化 + 逐页视觉审计（Collected-Papers-of-Fields-Medalists）

> 把本文件全文作为新 Session 的第一条消息发给 ZCode 的 AI。快照：2026-09-29，git HEAD `4c97d49`。

---

你好，你接手的是 **`/Users/aurolafly/Collected-Papers-of-Fields-Medalists`**（独立 git repo，branch `main`）
的「论文 MinerU 化 + 逐页视觉审计」任务。当前进度 **20/85，暂停中**，请按下面步骤继续。

## 0. 第一件事：读这 5 个文件（按顺序，不要跳过）

1. `README.md` —— 资产地图与目录 schema、审计来源链（唯一真值）；
2. `AUDIT-SOP.md` —— **规范**：最高目标、每页流程、审计后修复、密集提交纪律、图片资产规则；
3. `AUDIT-INDEX.md` —— 篇级进度总账（**唯一进度真值**；一行=一篇，看哪些没有"✅ 完成"）；
4. `HANDOFF-AUDIT.md` —— 交接手册：接力程序、已知坑清单、验收标准、2026-09-29 接力状态更新；
5. `AUDIT-PROGRESS.log` —— 页级进度日志；**读最后 5 行**——你的精确恢复点在那里（哪篇/哪页/最后等级）。

## 1. 最高目标（不可漂移）

本 repo 最终要收录：**全部论文 PDF + 它们的修复后的 Markdown + 修复日志/报告**，使未来第三方能够
**有效审计我们的工作**：每条结论可追到页面/原图/md/提交；每处修复可追到依据（审计记录）与原始 mineru 产出。

## 2. 当前状态（2026-09-29）

- **审计 20/85 完成**（清单与审计文件链接见 `AUDIT-INDEX.md`）；暂停中。
- **mineru 批次 ALL DONE**：84/85 导出成功。**唯一失败**：`2022年 - Huh/Huh_2020_lorentzian_polynomials`
  （云端两次 EXPORT FAIL，待排查——可用 `~/.zcode/skills/mineru/SKILL.md` 的方法重试；重试前先读它）。
- 大件分卷已导出（按片接力，各片独立落签/提交）：Thompson 2 片 / Lafforgue 2 片 / EGA I 2 片 / Schwartz II 2 片
  （md 命名 `<base>__partNN.md`，签名注明对应 PDF 页区间）。
- 已发现 FAIL 已**全部修复并登记**（`git log` 的 `fix(md):` 系列）。
- **下一步队列（按页数升序）**：`1966年 - Atiyah/Atiyah_Singer_1963_index_theorem`（12p）→
  `1970年 - Baker/Baker_1966_linear_forms_ru`（12p）→ `1936年 - Ahlfors/Ahlfors_1930_ueberlagerungsflaechen`（38p）→ …
  （完整候选以 `AUDIT-INDEX.md` 中无"✅"行 + `<base>_mineru/` 已有 md 者为准）

## 3. 每篇的标准接力程序（细节以 `HANDOFF-AUDIT.md` §3 + `AUDIT-SOP.md` 为准）

1. **选下一篇**：`AUDIT-INDEX.md` 无"✅ 完成"行、且 `<base>_mineru/` 已有 md；页数升序优先；
2. **渲染**：先 `mkdir -p <目录>/audit`**（必须先建，否则 gs 静默失败）**，再
   `gs -q -dNOPAUSE -dBATCH -sDEVICE=pngmono -r150 -sOutputFile=<目录>/audit/p%03d.png <pdf>`；
3. **逐页循环**（核心纪律，禁止批量补写）：读第 N 页 PNG → 读 md 中该页对应段 → 五点比对
   （题录/定理陈述/公式上下标/记号/参考文献）→ **立即**追加该页签到 `<目录>/AUDIT-<短名>.md` →
   **立即 `echo "$(date '+%F %H:%M') | PAGE | <论文> | p.N/总页 | <等级> | <备注>" >> AUDIT-PROGRESS.log`** →
   **立即 `git add -A && git commit -m "audit(page): <论文> p.N/总页 <等级>"`**；
4. **疑难仲裁**（顺序）：① 300dpi 灰度局部（`-sDEVICE=pnggray -r300` + 裁剪，裁剪后必须目检位置）；
   ② **数字件（pdfTeX 等）先用 `pdftotext` 逐字符对账**（本 repo 已有 Lions/honeycomb 多例）；
   ③ arXiv 论文拉 LaTeX 源码（`https://arxiv.org/e-print/<id>`）；④ 出版商官方页。
   **仲裁图片必须存入该篇 `audit/` 并随审计提交——禁止只放在 `/tmp`**；
5. **收尾**：签体加「## 总评」（覆盖声明+系统性瑕疵+可用性结论）→ `AUDIT-INDEX.md` 加一行 →
   更新 `README.md` 中该目录行的 AUDIT 计数 → 如有 FAIL，按审计中的修复建议**实际修复 md**
   （独立 `fix(md): …` commit，并在总评追加「修复登记」；修复前 md = 该 fix commit 的父提交）→
   `git add -A && git commit -m "audit: <篇名> N页审计完成（累计X/85…）"`。

## 4. 纪律红线

- collection repo 允许 `git add -A`；**禁止 push、禁止改写历史**；只提交本地历史；
- 不使用 Sub Agent；不写 ArangoDB/Redis/外部服务；不启动 Solver/资格实验；
- mineru server stop/restart 会干扰用户打开的 MinerU App —— **禁止**；
- token/credential 不入 git、不入回答；
- 审计保持诚实：不确定就写"150dpi 不可分辨，以原 PDF 为准"，绝不脑补 PASS。

## 5. 已知坑（完整清单见 `HANDOFF-AUDIT.md` §4）

- **ff→f 伪影**（pdfTeX 数字件文本层：diferent/suficient/Coeficients…；`pdftotext` 能还原是仲裁真值）；
- **ß→fs/fa**（德文老印刷件，如 Ahlfors；原刊为标准 ß）；
- arXiv 侧栏戳记、页眉/页码/水印通常被 mineru 丢弃（记 PASS±）；脚注常被拆成碎片段；
- **`file` 页数不可信**，一律用 `pdfinfo`；
- 批次脚本已 ALL DONE；若需重跑：canonical 副本 `tools/mineru_batch.py`（已含"跳过已完成"逻辑），
  运行：`nohup python3 /tmp/mineru_batch.py >> /tmp/mineru_batch.log 2>&1 < /dev/null &`；
- >200 页文件按 gs 分卷导出；EGA I 分卷时 gs 曾报 page-range 警告，审计其分片时核对完整性。

## 6. 完成判据（验收）

- `AUDIT-INDEX.md` 85 行全部带"✅ 完成（N/N）"；
- 每个论文目录有 `AUDIT-<短名>.md`，且页数签数 = `pdfinfo` 页数（分卷按片合计）；
- 每个论文目录有 `*_mineru/`（md + JSON/images）；全部 PASS/PASS±；FAIL 已修复（或有"以原图为准"注记+修复登记）；
- repo git 干净、全部提交（本地即可）；`README.md` 计数与实物一致；
- （可选项）worktree repo `shuxuedashi-glm5.2-worktree` 的 `MEMORY.md` 收尾登记（先跑
  `/Users/aurolafly/codex/tools/check_file_baseline.sh` 再改）。

**任何时刻中断，恢复点 = `AUDIT-PROGRESS.log` 末行 + `HANDOFF-AUDIT.md`「下一步队列」。**
先读 §0 的 5 个文件，然后从 §3 继续。
