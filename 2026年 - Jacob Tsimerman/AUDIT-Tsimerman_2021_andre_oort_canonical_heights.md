# Canonical Heights on Shimura Varieties and the André-Oort Conjecture — 逐页审计

- Peer：`Peer-P21`
- Model / reasoning effort：`gpt-6-luna / max`
- 角色：`CONTRIBUTOR`；`Master-Luna` 是唯一 `CANONICAL_INTEGRATOR`
- 任务基线：`037602429d3b009f6fc468c732073eb3ddf9875f`（detached worktree；该候选尚未集成）
- PDF：`Tsimerman_2021_andre_oort_canonical_heights.pdf`，52 页；Creator 为 LaTeX with hyperref；born-digital
- MinerU Markdown：`Tsimerman_2021_andre_oort_canonical_heights__Tsimerman_2021_andre_oort_canonical_heights.md`
- 对账方法：PDF 文本层逐页为主；150dpi pngmono 页图用于版面/字形核验，疑难字形再用 300dpi 裁片。
- 范围：判断 PDF 排印页与 MinerU Markdown 的转录忠实度，不审查论文数学证明有效性。

## p.001（PDF p.1 / 印刷 p.1）
- 时间：2026-10-01 16:12:03 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p001.png`（pngmono 150dpi）
- 核对：题名、作者、附录作者、日期、目录至 §6.4。
- 结果：PASS±。
- 差异与依据：页面左侧排有 `arXiv:2109.08788v4 [math.NT] 17 Dec 2024`，Markdown 未录入；属版本/来源元数据遗漏，不改变正文命题。印刷目录将 §6.4 写作 `Principle bundles`，Markdown 同样保留该拼法；这是印刷原文 quirk，未作校正。PDF 文本层与 150dpi 页图支持以上判断；Markdown 对应第 1–50 行。

## p.002（PDF p.2 / 印刷 p.2）
- 时间：2026-10-01 16:14:01 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p002.png`（pngmono 150dpi）
- 核对：目录 §6.5–附录 §A.3。
- 结果：PASS±。
- 差异与依据：目录附录标题的印刷排版将 `infinity by` 连作 `infinityby`（源级空格 quirk，照录）；Markdown 对应目录项也缺空格，且作者尾部被截成 `Michael C`，但附录正文标题后续列出全名。此为目录元数据的轻微转录缺损，非正文遗漏。页图与 PDF 文本层一致；Markdown 对应第 51–69 行。

## p.003（PDF p.3 / 印刷 p.3）
- 时间：2026-10-01 16:16:36 EDT (-0400)
- actor=Peer-P21；model=gpt-6-luna；effort=max
- PNG：`audit/Tsimerman_2021_andre_oort_canonical_heights_p003.png`（pngmono 150dpi）
- 300dpi 仲裁图：`audit/300dpi/Tsimerman_2021_andre_oort_canonical_heights_p003_Theorem-1.2.png`
- 核对：§1.1 概述、Theorem 1.1–1.2、§1.2 开头。
- 结果：FAIL（以原图为准）。
- 差异与依据：Theorem 1.2 在印刷页写作 `Let (T,r) ⊂ (G,X)`，结论为高度 `is (M disc E_T)^{o(1)}`；Markdown 第 95 行的包含式丢失 `(G,X)` 的括号，渐近式丢失左括号并把 `E_T` 输出成 `\cal E_T`。300dpi 裁片清楚显示原式为普通斜体 `E_T`，故当前 Markdown 公式结构不完整。第 81 行还将 `different strategy` 误录为 `diferent strategy`；第 101 行本页对应的 `different` 亦少一个 `f`。印刷 PDF 文本层、150dpi 整页图及 300dpi 裁片相互支持；改动留待 52 页审计完成后逐处 Edit。
