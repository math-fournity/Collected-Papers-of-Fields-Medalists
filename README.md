# Collected Papers of Fields Medalists — 资产地图（README）

> **最高目标**：本 repo 收录 **全部论文 PDF + 修复后的 Markdown + 修复日志/报告**，使未来第三方能
> **有效审计本 repo 的工作**：每条结论可追到页面/原图/md/提交；每处修复可追到依据（审计记录）与原始
> mineru 产出。规范见 [AUDIT-SOP.md](AUDIT-SOP.md)。

## 1. 目录层级 Schema（期望布局）

```
.
├── README.md                  # 本文件：资产地图与目录 schema（唯一真值）
├── AUDIT-SOP.md               # 审计与修复规范（最高目标/流程/提交纪律）
├── AUDIT-INDEX.md             # 篇级进度总账（一行=一篇；审计状态唯一真值）
├── AUDIT-PROGRESS.log         # 页级进度日志（append-only；每页一行；恢复入口）
├── HANDOFF-AUDIT.md           # 交接手册（接力程序、坑清单、当前状态）
├── tools/
│   ├── mineru_batch.py        # 批量解析脚本（已含“跳过已完成”逻辑）
│   └── mineru_batch.log       # 解析日志（ALL DONE = 84/85 导出成功）
└── <NNNN年 - 得主>/            # 65 个论文目录（见 §3 清单）
    ├── <base>.pdf             # 原始 PDF（1..n 个）
    ├── <base>_mineru/         # MinerU 导出（每个 PDF 一套）
    │   ├── <base>__<zip>.md   #   md 正文（分卷件为 <base>__partNN.md）
    │   ├── <base>/            #   解包内容（middle_json.json / structured_content.json / images/）
    │   └── partNN/            #   分卷件的解包目录（>200p 文件）
    ├── audit/                 # 逐页审计渲染与仲裁图（pngmono 150dpi / pnggray 300dpi）
    └── AUDIT-<短名>.md        # 逐页审计报告（逐页签 + 总评 + 修复登记）
```

命名约定：

| 资产 | 约定 |
|---|---|
| 论文目录 | `NNNN年 - 得主`（按获奖年份/得主命名，收集期固定） |
| PDF 基名 | `<FirstAuthor>_<Year>_<topic>`（部分沿用原始文件名，如 `frey1986`） |
| md 正文 | `<base>__<zip名>.md`；分卷 = `<base>__partNN.md` |
| 审计渲染 | `audit/pNNN.png`（或带前缀，如 `icm_pNNN.png`、`honeycomb_pNNN.png`） |
| 300dpi 仲裁图 | `audit/<page>_<topic>_300dpi.png`（证据，必须入库） |

## 2. 审计与来源链（如何审计本 repo）

1. [AUDIT-SOP.md](AUDIT-SOP.md) —— 审计/修复/提交规范与最高目标；
2. [AUDIT-INDEX.md](AUDIT-INDEX.md) —— 逐篇审计状态与审计文件链接；
3. 各目录 `AUDIT-<短名>.md` —— 逐页签、总评、修复登记；
4. `git log` —— 原始 mineru 产出 → `fix(md): …` 修复的每次精确变更
   （修复前 md = 对应 fix commit 的父提交，可 `git show <fix>^:<md path>` 回溯来源）；
5. [AUDIT-PROGRESS.log](AUDIT-PROGRESS.log) —— 页级时间线（会话中断后的恢复入口）；
6. [HANDOFF-AUDIT.md](HANDOFF-AUDIT.md) —— 方法与坑清单。

## 3. 论文目录清单（65 个目录 / 86 个 PDF）

> 计数为当前快照；**审计状态以 [AUDIT-INDEX.md](AUDIT-INDEX.md) 为准**。

| 目录 | PDF | `_mineru` | AUDIT 文件 |
|---|---:|---:|---:|

| 1936年 - Ahlfors | 2 | 2 | 1 |
| 1936年 - Douglas | 1 | 1 | 0 |
| 1950年 - Schwartz | 2 | 2 | 0 |
| 1950年 - Selberg | 1 | 1 | 1 |
| 1954年 - Kodaira | 1 | 1 | 1 |
| 1954年 - Serre | 1 | 1 | 0 |
| 1958年 - Roth | 1 | 1 | 0 |
| 1958年 - Thom | 1 | 1 | 0 |
| 1962年 - Hörmander | 1 | 1 | 0 |
| 1962年 - Milnor | 1 | 1 | 1 |
| 1966年 - Atiyah | 1 | 1 | 0 |
| 1966年 - Cohen | 1 | 1 | 1 |
| 1966年 - Grothendieck | 2 | 2 | 0 |
| 1966年 - Smale | 1 | 1 | 0 |
| 1970年 - Baker | 2 | 2 | 1 |
| 1970年 - Hironaka | 2 | 2 | 1 |
| 1970年 - Novikov | 2 | 2 | 1 |
| 1970年 - Thompson | 1 | 1 | 0 |
| 1974年 - Bombieri | 3 | 3 | 2 |
| 1974年 - Mumford | 1 | 1 | 0 |
| 1978年 - Deligne | 1 | 1 | 0 |
| 1978年 - Fefferman | 1 | 1 | 1 |
| 1978年 - Margulis | 2 | 2 | 1 |
| 1978年 - Quillen | 1 | 1 | 0 |
| 1982年 - Connes | 1 | 1 | 0 |
| 1982年 - Thurston | 1 | 1 | 0 |
| 1982年 - Yau | 1 | 1 | 1 |
| 1986年 - Donaldson | 1 | 1 | 0 |
| 1986年 - Faltings | 2 | 2 | 1 |
| 1986年 - Freedman | 1 | 1 | 0 |
| 1990年 - Drinfeld | 1 | 1 | 0 |
| 1990年 - Jones | 1 | 1 | 1 |
| 1990年 - Mori | 1 | 0 | 0 |
| 1990年 - Witten | 1 | 1 | 0 |
| 1994年 - Bourgain | 1 | 1 | 0 |
| 1994年 - Lions | 1 | 1 | 1 |
| 1994年 - Yoccoz | 1 | 1 | 0 |
| 1994年 - Zelmanov | 1 | 1 | 1 |
| 1998年 - Borcherds | 1 | 1 | 0 |
| 1998年 - Gowers | 1 | 1 | 0 |
| 1998年 - Kontsevich | 1 | 1 | 0 |
| 1998年 - McMullen | 1 | 1 | 0 |
| 1998年 - Wiles | 5 | 5 | 0 |
| 2002年 - Lafforgue | 1 | 1 | 0 |
| 2002年 - Voevodsky | 1 | 1 | 0 |
| 2006年 - Okounkov | 1 | 1 | 0 |
| 2006年 - Perelman | 3 | 3 | 1 |
| 2006年 - Tao | 1 | 1 | 0 |
| 2006年 - Werner | 1 | 1 | 0 |
| 2010年 - Lindenstrauss | 1 | 1 | 0 |
| 2010年 - Ngô | 1 | 1 | 0 |
| 2010年 - Smirnov | 2 | 2 | 1 |
| 2010年 - Villani | 1 | 1 | 0 |
| 2014年 - Avila | 1 | 1 | 0 |
| 2014年 - Bhargava | 1 | 1 | 0 |
| 2014年 - Hairer | 2 | 2 | 0 |
| 2014年 - Mirzakhani | 1 | 1 | 0 |
| 2018年 - Birkar | 2 | 2 | 0 |
| 2018年 - Figalli | 1 | 1 | 0 |
| 2018年 - Scholze | 1 | 1 | 0 |
| 2018年 - Venkatesh | 1 | 1 | 0 |
| 2022年 - Duminil-Copin | 1 | 1 | 1 |
| 2022年 - Huh | 2 | 1 | 0 |
| 2022年 - Maynard | 1 | 1 | 0 |
| 2022年 - Viazovska | 2 | 2 | 0 |

> 注：`1990年 - Mori` 使用库藏 `full.md`（未经 batch 导出）；`2022年 - Huh` 的
> `Huh_2020_lorentzian_polynomials` 云端解析两次失败（待排查），其余 84/85 导出成功。

## 4. 维护规则

- 结构/文件变化（新增论文目录、PDF、`_mineru/`、`AUDIT-<短名>.md`）时，
  **同一批提交**更新本 README 的清单与计数；
- 审计进度只更新 `AUDIT-INDEX.md`（篇级真值）与 `AUDIT-PROGRESS.log`（页级日志），
  并按上一行规则同步本表该行的 AUDIT 计数；
- 本文件是资产地图与 schema 的唯一真值；细节以 `AUDIT-SOP.md` 为准。

