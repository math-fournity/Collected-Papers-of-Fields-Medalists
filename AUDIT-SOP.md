# AUDIT-SOP — MinerU Markdown 逐页视觉审计规范

> 依据：2026-09-29 Mori 论文审计案例（五点抽查 + 逐页扩展）沉淀。
> 要求：**审计一页，产出一份审计说明**——逐页交错进行（渲染→目检→比对→落签），禁止
> 先全部渲染/全部加载后再批量输出。

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
