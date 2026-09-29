# AUDIT — J. Tits, "The Work of Gregorii Aleksandrovitch Margulis"（Helsinki 1978 会议工作报告；`Margulis_1978_work_report_tits`，印刷 pp.60–64 摘录）

> mineru: standard 档云端解析，导出 `Margulis_1978_work_report_tits_mineru/`；审计依据 = 二值化渲染
> `audit/report_pNNN.png`（pngmono 150dpi）对照
> `Margulis_1978_work_report_tits__Margulis_1978_work_report_tits.md`。逐页审计，一页一签。
> PDF 结构：p.1–5 = 印刷 pp.60–64（p.64 空白）；报告开头与 §1–§3 不在本件内，
> p.60 起于句中 "destroying the algebraicity"；作者 J. Tits（页眉题名与文末 Collège de France 地址）。

## p.001（PDF p.1 / 印刷 p.60）
- PNG：audit/report_p001.png（pngmono 150dpi）
- 核对：
  - 页眉 `60 — J. Tits` 未转写（系统性丢弃，见坑清单）
  - 承接段 "destroying the algebraicity … vast generalization of Weil's and Mostow's rigidity
    theorems:" ✓ 逐字吻合
  - **超刚性主定理**（斜体段）：rk_R G ⩾ 2、F 局部紧非离散、ϱ: Γ→GL_n(F)、ϱ(Γ) 不相对紧且
    Zariski 闭包连通 ⟹ F = R 或 C 且 ϱ 可延拓为 𝒢 的有理表示 ✓（LaTeX 表达 rk/\geqslant/\varrho/\to 对应无误）
  - 论证评述段（ergodic theory、unitary representations、functional spaces、algebraic geometry、
    structure theory…）；1975–1976 Collège de France 课程；"a summary … is given in [27]" ✓
  - Furstenberg [20] 段 ✓
  - **4. Other results.**、**4.1 S-arithmetic groups**：K/S/o 定义、ℋ⊂𝒢𝔏_n、ℋ(o)=ℋ∩GL_n(o)、
    ℋ(o) 单射为有限余体积离散子群、乘积 H=∏_{v∈S} ℋ(K_v) ✓（见 ±3 记号拍平）
  - 例（分母为 2 的幂的 o、SL_n(R)×SL_n(Q_2)）✓；S-算术定义（K,S,ℋ、α: H→G 紧核、commensurable）✓；
    [18] 一般框架 ✓；段末 "he shows that if the" 与下页自然续接 ✓
- 结果：**PASS±**
  - ±1：running head `60 — J. Tits` 被丢弃（系统性，不误导）；
  - ±2：`Zariski-closure` → md `Zariskiclosure`（丢连字符，md 第 3 行）；
  - ±3：记号拍平 2 处——正文 "algebraic group 𝒢" → `G`（md 第 1 行）、首次 ℋ⊂𝒢𝔏_n → `H \subset GL_n`
    （md 第 11 行）；后者使首处 `H` 与同段乘积群 `H = ∏ ℋ(K_v)` 同形，属可自愈的小瑕
    （紧随的 ℋ(o)=ℋ∩GL_n(o) 还原了记号）。
- 备注：本件为工作报告摘录，无标题页信息；`\prod_{v \in s}`（小写 s）为行内大小写排印差异。

## p.002（PDF p.2 / 印刷 p.61）
- PNG：audit/report_p002.png（pngmono 150dpi）
- 核对：
  - 页眉 `The Work of Gregorii Aleksandrovitch Margulis — 61` 未转写（系统性；**该页眉给出报告标题**，
    与目录命名 "work_report_tits" 相符）
  - S-算术结论段 "… then Γ is S-arithmetic." ✓（rk≥2、irreducible、n°2 引用）
  - **4.2 "Abstract" isomorphisms**（Dieudonné / O'Meara / A. Borel 历史与"beyond"结论）✓
  - **4.3 Normal subgroups**：rk G ⩾ 2 ⟹ 一切非中心正规子群有限指数；一般化条件（局部紧局部域、
    有限特征）；Mennicke/Bass/Milnor/Serre/Raghunathan 对照 ✓
  - **4.4 Action on trees**：Serre LNM no 372、Chevalley 群概形秩 ≥2、非 amalgam 说明；Margulis
    最广一般性定理（G 如 4.1、秩≥2、不可约有限余体积 ⟹ 不能无不动点作用在树上）✓
  - **5. Conclusion** 全段 ✓
  - 末行 "I wish to conclude … However, I cannot but express" 与下页自然续接 ✓
- 结果：**PASS±**
  - ±1：running head（报告标题 + 页码 61）被丢弃（系统性，不误导）。
- 备注：本页无内容级差异；页眉标题为报告全名提供旁证。

## p.003（PDF p.3 / 印刷 p.62）
- PNG：audit/report_p003.png（pngmono 150dpi）
- 核对：
  - 页眉 `62 — J. Tits` 未转写（系统性）
  - 结论末段 "my deep disappointment—no doubt shared by many people here—in the absence of
    Margulis from this ceremony. In view of the symbolic meaning of this city of Helsinki,¹ …" ✓ 逐字吻合
  - **References** 标题、`Published work of G. A. Margulis` ✓
  - **文献 1–20 逐条核对**（作者/刊名/卷(年)/页）：
    - 1. Dokl. 166 (1966), 1054—1057 ✓；2. Mat. Sb. 75 (1968), 163—168 ✓；
    - 3. Uspehi Mat. Nauk 22 (1967), 169–171 ✓；4. Mat. Sb. 80 (1960), 600–615 ✓；
    - 5. Funkcional. Anal. i Priložen, 3 (4) (1969), 89–90 ✓；6. Dokl. 187 (1969), 518–520 ✓；
    - 7. Funkcional. Anal. i Priložen 4 (1) (1970), 62–76 ✓；8. Dokl. 192 (1970), 736–737 ✓；
    - 9. Mat. Sb. 86 (1971), 552–556 ✓；10. Budapest 1971 / Akademiai Kiado 1975 ✓；
    - 11. Tezis … (1971) ✓；12. Devyataya Letnyaya Mat. Škola … 1972, pp. 342–348 ✓；
    - 13. Funkcional. Anal. i Priložen 7 (3) (1973), 88—89 ✓；14. Probl. Peredači Informacii 9 (4) (1973), 71—80 ✓；
    - 15. Uspehi Mat. Nauk S.S.S.R. 29 (1974), 49—98 ✓；16. Funkcional. Anal. Priložen 8 (3) (1974), 77–78 ✓；
    - 17. Probl. Peredači Informacii 10 (2) (1974), 101—108 ✓；18. Proc. Internat. Congr. Math. (Vancouver, 1974), vol. 2, 1975, pp. 21–34 ✓；
    - 19. Funkcional. Anal. Priložen 9 (1) (1975), 35–44 ✓；20. Moscow 1977, pp. 277—313 ✓
  - **脚注 ¹**（Finlandia Hall / 1975 Helsinki Agreements）内容逐字保留 ✓
- 结果：**PASS±**
  - ±1：running head `62 — J. Tits` 被丢弃（系统性，不误导）。
- 备注：脚注在 md 中被排入文献流（20 与 21 之间，即本页页脚原位），文本正确、上标锚点 ¹ 完好，
  阅读时勿误当文献条目；"U-flows"、"Každan"、"Peredači" 等专名 diacritics 全对。

## p.004（PDF p.4 / 印刷 p.63）
- PNG：audit/report_p004.png（pngmono 150dpi）
- 核对：
  - 页眉 `The Work of Gregorii Aleksandrovitch Margulis — 63` 未转写（系统性）
  - **文献 21–25**：
    - 21. (with G. A. Soifer), Dokl. Akad. Nauk S.S.S.R. 234 (1977), 1261—1264 ✓；
    - 22. Funkcional. Anal. i Priložen 11 (1977), 45—57 ✓；23. Funkcional. Anal. i Priložen 12 (4) (1978), 64—76 ✓；
    - 24. Dokl. Akad. Nauk S.S.S.R. 242 (1978) 533—536（原文无逗号，md 同）✓；
    - 25. Funkcional. Anal. i Priložen (to appear) ✓
  - **Other references**（斜体节标题）✓；26. A. Borel, Sém. Bourbaki, 1969, LNM vol. 179, pp. 199—215 ✓；
    27. J. Tits, Sém. Bourbaki, 1976, LNM vol. 567, pp. 174—190 ✓
  - 文末地址块：`COLLÈGE DE FRANCE` / `75231 PARIS CEDEX 05, FRANCE` ✓
  - 忠实保留原刊笔误：26 条 "Sous-groupes discrets de **groups** semi-simples"（法语应为 groupes）✓
- 结果：**PASS±**
  - ±1：running head（标题 + 页码 63）被丢弃（系统性，不误导）；
  - ±2：`Other references` 在 md 中出现两次——行尾粘入 ref 25 段末（md 第 83 行）＋ 独立标题
    （md 第 85 行 `## Other references`）；内容不误导，检索时注意去重。
- 备注：本页下半为空白（报告正文至此结束）；跨行连字符 "Mar-goulis" 正常合并为 "Margoulis"。

## p.005（PDF p.5 / 印刷 p.64，**末页**）
- PNG：audit/report_p005.png（pngmono 150dpi）
- 核对：目检整页**空白**（无文字、无图）；`pdftotext` 输出仅换页符；md 无对应内容 （一致）。
- 结果：**PASS**（空白页，无可比内容）。
- 备注：报告正文止于 p.63；本页为空白尾页。

## 总评
- **覆盖声明**：本 PDF 共 5 页（pdfinfo 5p），**逐页 5/5 完成审计**（audit/report_p001–p005.png）；
  无跳页、无抽查替代。对应印刷 pp.60–64（p.64 空白页）。
- 结论分布：**PASS± ×4**（p.60/61/62/63）+ **PASS ×1**（p.64 空白）；**无 FAIL**。
- 系统性瑕疵（均不误导）：①running head 全数丢弃（`60 — J. Tits`、`The Work of Gregorii
  Aleksandrovitch Margulis — 61/63`、`62 — J. Tits`）；②记号拍平（𝒢→G、ℋ/𝒢𝔏_n→H/GL_n，
  首处 `H` 与乘积群 `H = ∏ℋ(K_v)` 同形）；③`Zariski-closure` 连字符丢失；④`Other references`
  标题在 md 中重复一次（ref 25 行尾 + `## Other references`）。
- 忠实性正面案例（勿误判为错误）：ref 26 原刊法语笔误 "groups"（应为 groupes）被保留；
  脚注 ¹ 全文保留且上标锚点完好；U-flows / Každan / Peredači / Dieudonné / Raghunathan 等
  专名 diacritics 全对；文献 1–27 作者/卷页年逐条准确。
- 结构提示：本件为**摘录**（报告起始页与标题页不在内），引用全文须回会议录原件；脚注 ¹ 在 md 中
  位于文献流 ref 20/21 之间（原位页脚）。
- 可用性：全部 5 页文本可放心引用（p.64 无内容）；若需严格区分 ℋ 与乘积群 H，对照原 PDF pp.60–61。
- mineru 解析信息：mineru 3.4.4 / tier=basic / parse_mode=ocr（导出件无 doc_id 字段）。
