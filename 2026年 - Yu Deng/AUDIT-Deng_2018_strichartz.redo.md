# Deng 2018 Strichartz — Luna 审计重做（逐页视觉重检）

> 性质：Luna 审计重做（用户 2026-10-02 判定 Luna 审计不可信，逐页对照 PDF 全量重检，旧修复一并重核）。
> 本文件只登记重做范围（p.1 起）的页级结论；旧 [AUDIT-Deng_2018_strichartz.md](AUDIT-Deng_2018_strichartz.md) 不再作为可信依据，保留仅作对照。
>
> - actor：Wf-R-Deng
> - host / model / effort：zcode / account:zai-individual-coding-plan/GLM-5.3-Flash / max（run 级配置，自报 UNKNOWN）
> - PDF：Deng_2018_strichartz.pdf，34 页，SHA-256 = 6987354755fee2b7960f9cf6986d0cebaa4a733f0319230bbc7fd1b9399c1948
> - MD 基线 SHA-256（重做起点，即 Luna 修复后版本）：60f572494701abc6fe95882c753a3b0f86660a98f866cc7767d8a25d8910dd1b
> - 开工时间：2026-10-02 14:28 EDT
> - 文本层判定：`pdftotext -f 1 -l 1` 首页正常输出（arXiv:1810.05630v3 题录完整，exit 0）→ 文本层可用，采用**双通道主对账**（每页 pdftotext 文本层 + 150dpi pngmono PNG 视觉目检，以印刷页图像为最终裁决）。
> - 证据图：`audit-redo/`（pngmono 150dpi，p001–p009 本次）；旧 `audit/` 不动。
> - 纪律：印刷原文为唯一裁决源；Luna 旧修复一并重核；print quirk 与错字忠实保留登记，不按数学预期静默改正；看不清即升级 300dpi 仲裁，不编造。

## p.001（PDF p.1 / 印刷 p.1）
- PNG：audit-redo/p001.png（pngmono 150dpi）＋ pdftotext 文本层对账
- 核对：题录（标题/四位作者/arXiv:1810.05630v3 印记/摘要）、§1.1–1.2 节序、公式 (1.1)(1.2)(1.3) 及 §1.2 无编号式、≲ 与 ≤ 的区分
- 结果：PASS±。题名、作者、摘要（含原刊 "on the other hands" quirk，忠实保留）逐字吻合；(1.1) s = max(0, d/2 − (d+2)/p)、(1.2)、(1.3) 的 ≤、χ(−Δ_M/N²)、O_ε(N^ε T^ε)、s(p) = max(d/4 − d/(2p), d/2 − (d+1)/p) 全部与印刷页一致。瑕疵（均不误导，按 SOP 不改）：display 公式边界句尾标点被吞 3 处——MD L11 "with data v_0" 后缺逗号、L39 O_ε(...) 后缺句号、L41 ‖·‖_{H^s(M)} 后缺句号。
- 备注：Luna 旧修复抽核通过——旧基线的「Schrödinger 重音拆成 sup 标记」「arXiv 印记漏录」在当前 MD 中已不存在（L1/L3 正常）。
