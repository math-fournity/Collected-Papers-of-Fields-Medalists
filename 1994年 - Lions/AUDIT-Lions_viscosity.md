# AUDIT — Crandall–Ishii–Lions, "User's guide to viscosity solutions of second order partial differential equations"（BAMS 27 (1992) 1–67 的 **MathSciNet 评审记录打印件**：评论 + 文献 1–162）

> mineru: standard 档云端解析，导出 `Lions_1992_viscosity_users_guide_mineru/`；审计依据 = 二值化渲染
> `audit/pNNN.png`（pngmono 150dpi）对照
> `Lions_1992_viscosity_users_guide__Lions_1992_viscosity_users_guide.md`。逐页审计，一页一签。
> 仲裁裁剪：`audit/p001_*_300dpi.png`（pnggray 300dpi）。
> PDF 结构：9 页 = MathSciNet 记录打印件（MR1118699 评论正文 + 参考文献 1–162 + AMS 版权行），
> 非原论文扫描；评论撰写人签名 P. Szeptycki。
> **重要**：本 PDF 为 pdfTeX 数字打印件、**含精确文本层**——对账以 150dpi 目检为主，
> 辅以 `pdftotext` 文本层逐字符复核（300dpi 裁剪仅用于早期疑点，均已复核）。

## p.001（PDF p.1）
- PNG：audit/p001.png（pngmono 150dpi）；仲裁裁剪：p001_header/authors/ineq/ucsc/sig_300dpi.png
- 核对：
  - MathSciNet 界面区：`Citations | From References: 2192 | From Reviews: 31`、`Previous Up Next`、
    `MR1118699 (92j:35050) 35J60 35B05 35D05 35G20` ✓
    （**300dpi 仲裁**：From Reviews=31、分类号 35B05 均正确；150dpi 疑似 21/35B65 系目检误差）
  - 作者行：Crandall, Michael G. **(1-UCSB)**；Ishii, Hitoshi (J-CHUO)；Lions, Pierre-Louis (F-PARIS9-A) ✓
    （**忠实保留**：打印件确为 1-UCSB，勿"纠正"为 UCSC）
  - 题录：User's guide … second order partial differential equations. /
    Bull. Amer. Math. Soc. (N.S.) **27** (1992), no. 1, 1–67 ✓
  - 评论正文（P. Szeptycki）：viscosity solutions 概念、单调性条件、superjet/subjet、Perron 方法、
    "161 references" ✓
  - 公式：F(x,u,Du,D²u)=0；F(x,r,p,X) ≤ F(x,s,p,Y)；x,p ∈ R^N；N×N 对称矩阵；J^{2,+}(u,x)/J^{2,−}；
    **u(y) ≤ u(x)+⟨p,y−x⟩+⟨X(y−x),y−x⟩+o(|y−x|²)**（末尾 = 小写 o，300dpi 确认）✓
  - 文献 1–9（Aleksandrov ×3 / Alziary de Roquefort / Aizawa–Tomita / Bakelman / Barbu ×3）✓
- 结果：**PASS±**
  - **±0（符号缺失 1 处，须留意）**："provided that for **y → x** we have the inequality" 的箭头在 md
    中丢失（md 第 14 行 `provided that for$y  x$we have the inequality`）——**300dpi 仲裁 + pdfTeX
    文本层（"for y → x"）双重确认**。缺口可见、不误导，但引用 superjet 定义时须补；
    建议修复：`for$y  x$` → `for $y \to x$`。
  - ±（系统性 OCR 伪影，全篇性）：① ff 合字丢失（diferential→differential、dificult→difficult）；
    ② 词间空格合并（"existence ofthe"、"diferential ofa"）；③ 行内公式与正文间空格缺失（`form$F(...)$`）。
  - ±（UI chrome）：`Previous Up Next` 行与 Citations 表为 MathSciNet 界面元素，非论文内容。
- 备注：150dpi 两处"疑似错读"（From Reviews、分类号）经 300dpi 复核判 **md 正确**；审稿人签名
  "P. Szeptycki" 转写正确。本 PDF 为评审记录打印件，非论文原扫描（文献列表见后续页）。

## p.002（PDF p.2）
- PNG：audit/p002.png（pngmono 150dpi）
- 核对：**文献 10–32 逐条**（作者/题名/刊名/卷年页/MR 号）——
  10. Barbu–Da Prato（Research Notes 86, Pitman 1983）✓；11. Bardi（Pisa 4(4) 1987, 569-612）✓；
  12. Bardi–Evans（Nonlinear Anal. 8 (1984), 1373-1381）✓；13. Bardi–Perthame（Comm. PDE 15 (1990), 1649-1669）✓；
  14. Barles（Poincaré 1 (1984), 325-340）✓；15.（Poincaré 2 (1985), 21-33）✓；16.（INRIA no. 464, 1985）✓；
  17.（DIE 4 (1991), 263-275）✓；18.（DIE 4 (1991), 241-262）✓；19.（Indiana Univ. Math. J. 39 (1990), 443-466）✓；
  20.（DIE 3 (1990), 103-125）✓；21.（JDE to appear）✓；22.（Analyse Non Linéaire to appear）✓；
  23.（Duke Univ. Math. J. 61 (1990), 835-858）✓；24.（Nonlinear Anal. 16 (1991), 143-153）✓；
  25.（Modél. Math. Anal. Num. 21 (1987), 557-579）✓；26.（SIAM J. Control Optim. 26 (1988), 1133-1148）✓；
  27.（Appl. Math. Optim. 21 (1990), 21-44）✓；28.（Asymp. Anal. 4 (1991), 271-283）✓；
  29.（Nonlinear Anal. 14 (1990), 971-989）✓；30.（Nonlinear Anal. 13 (1989), 1067-1090）✓；
  31.（Trans. Amer. Math. Soc. 298 (1986), 635-641）✓；32.（JDE 68 (1987), 10-21）✓
  - MR 号（0704182/0963490/0764917/1080616/…/0885811）全部逐位吻合 ✓
- 结果：**PASS±**
  - **文本层精确对账**（md↔pdfTeX 源，归一化后）：仅 **ff→f 伪影 10 处词位**（refs 13/17/18/20/21/22/23/29/31/32：
    Comm. PDE、DIE、JDE、reaction-difusion、Diferential games、partial diferential equations 等），
    其余逐字符一致。**更正**：ref 13 "B. Perthame Exponential" 无逗号**系源本身写法**（文本层同）——
    非 md 缺陷；`Mod\`el.` 为 LaTeX 转义，等价。
- 备注：本页无页眉页码（打印件正文页无 running head）；文献流与 p.1 自然续接（9→10）。

## p.003（PDF p.3）
- PNG：audit/p003.png（pngmono 150dpi）；仲裁裁剪：p003_caffarelli / p003_capuzzo_300dpi.png
- 核对：**文献 33–53 逐条**——
  33.（Comm. PDE 15 (1990), 1713-1742）✓；34.（PAMS 113 (1991), 397-402）✓；35.（Math. Operations Research 15 (1990), 49-79）✓；
  36. Benton（Academic Press 1977）✓；37. Bony（C. R. Acad. Sci. Paris Ser. A 265 (1967), 333-336）✓；
  38. Brezis（North Holland 1973）✓；39. **Caffarelli**（Ann. of Math. (2) 130 (1989), 180-213）✓；
  40.（Indiana 46 (1987), 501-524）✓；41.（Nonlinear Anal. 13 (1989), 305-323）✓；42.（Appl. Math. Opt. 24 (1991), 197-220）✓；
  43.（SIAM J. Optim. Control 22 (1988), 1133-1148）✓；44.（TAMS 318 (1990), 643-683）✓；
  45. Chen–Giga–Goto（J. Differential Geom. 33 (1991), 749-786）✓；46.（Poincaré 6 (1989), 419-435）✓；
  47.（TAMS 282 (1984), 487-502）✓；48.（DIE 3 (1990), 1001-1014）✓；49.（J. Math. Soc. Japan 39 (1987), 581-596）✓；
  50.（C. R. Acad. Sci. Paris Sér. I Math. 292 (1981), 183-186）✓；51.（TAMS 277 (1983), 1-42）✓；
  52.（Math. Comp. 43 (1984), 1-19）✓；53.（Nonlin. Anal. 10 (1986), 353-370）✓
  - MR 号逐位吻合 ✓；**300dpi 仲裁**：39 原文 C**aff**arelli（md 作 "Cafarelli"，ff→f 伪影）；
    43/44 原文 C**app**uzzo-Dolcetta（md 同形，**忠实保留**——勿"纠正"）
- 结果：**PASS±**
  - **文本层精确对账**：仅 **ff→f 伪影 6 处词位**（refs 33/39/43/45/46/48——含专名 Caffarelli→Cafarelli）；
    其余逐字符一致（Cappuzzo-Dolcetta 的 "pp" 系源本身写法，忠实）。
  - ±：系统性 ff 伪影 + 空格合并（"singularities ofthe"、"singularities ofviscosity"）。
- 备注：本页无页眉页码；文献流 32→33 自然续接。

## p.004（PDF p.4）
- PNG：audit/p004.png（pngmono 150dpi）
- 核对：**文献 54–73 逐条**——
  54.（Illinois J. Math. 31 (1987), 665-688）✓；55. HJ in infinite dimensions Part I–V（J. Func. Anal. 62/65/68/90/97、417-465）✓；
  56.（DIE 3 (1990), 601-616）✓；57.（Arch. Rat. Mech. Anal. 105 (1989), 163-190）✓；
  58.（PAMS 94 (1985), 283-290）✓；59.（Appl. Anal. 34 (1989), 1-23）✓；60.（Nonlinear Anal. 12 (1991), 1123-1138）✓；
  61.（Hokkaido Math. J. 20 (1991), 135-164）✓；62.（Ann. Probab. 18 (1990), 226-255）✓；
  63.（Proc. London Math. Soc. 63 (1991), 212-240）✓；64.（Indiana 27 (1978), 875-887）✓；65.（Israel J. Math. 36 (1980), 225-247）✓；
  66.（Proc. Roy. Soc. Edinburgh A 111 (1989), 359-375）✓；67. Evans–Gariepy（CRC Press 1992）✓；
  68.（Poincaré 2 (1985), 1-20）✓；69.（preprint）✓；70.（Indiana 33 (1984), 773-797）✓；
  71.（Indiana 38 (1989), 141-172）✓；72.（J. Differential Geom. 33 (1991), 635-681）✓；73.（Appl. Math. Optim. 15 (1987), 1-13）✓
  - MR 号逐位吻合 ✓
- 结果：**PASS±**
  - **文本层精确对账**：仅 **ff→f 伪影 6 处词位**（refs 56/65/66/68/70/72）；另 ref 59 的 ℝ^n 在 md 作
    `\mathbb{R}^n`（pdf 文本层作 "R"，判 **md 表示更佳**）；其余逐字符一致。
  - ±1：系统性伪影（ff；空格合并："fine properties offunctions"）。
  - ±2：ref 56 的 ℝ^n 写成 HTML 形式 `R<sup>n</sup>`（与同页 ref 59 的 `\mathbb{R}^n` 不一致——
    表示级小瑕，不影响书目使用）。
- 备注：本页无页眉页码；文献流 53→54 自然续接。

## p.005（PDF p.5）
- PNG：audit/p005.png（pngmono 150dpi）；仲裁裁剪：p005_fleming / p005_ishii91_300dpi.png
- 核对：**文献 74–97 逐条**——
  74. Federer（Springer 1969）✓；75. Fleming–Rishel（Springer 1975）✓；76.（Pisa 13 (1986), 171-192）✓；
  77.（Indiana 38 (1989), 293-314）✓；78. Frankowska（Nonlin. Anal. 10 (1986), 1477-1483）✓；
  79. Giga–Goto–Ishii–Sato（Indiana U. Math. J. 40 (1991), 443-470）✓；80.（SIAM J. Math. Anal, to appear）✓；
  81. Gilbarg–Trudinger（2nd Ed. 1983）✓；82.（Chuo Univ. 26 (1983), 5-24）✓；83.（Indiana 33 (1984), 721-748）✓；
  84.（Chuo Univ. 28 (1985), 33-77）✓；85.（Funkcial. Ekvac. 29 (1986), 167-188）✓；86.（Duke 55 (1987), 369-384）✓；
  87.（PAMS 100 (1987), 247-251）✓；88.（Nonlin. Anal. 12 (1988), 121-146）✓；89.（CPAM 42 (1989), 14-45）✓；
  90.（Pisa 16 (1989), 105-135）✓；91.（Duke 62 (1991), **663-661**）✓；92.（Dif. Integral Equations 5 (1992), 1-24）✓；
  93.（Appl. Math. Optim. 23 (1991), 1-15）✓；94.（Funkcial. Ekvac. 34 (1991), 143-155）✓；
  95.（Comm. PDE 16 (1991), 1095-1128）✓；96.（JDE 83 (1990), 26-78）✓；97.（Nonlinear Anal. 13 (1989), 1295-1301）✓
  - MR 号逐位吻合 ✓
  - **文本层精确对账**：仅 **ff→f 伪影 6 处词位**（refs 77/80/81/92/95/96）；其余逐字符一致。
  - **源本身笔误 2 处，md 忠实保留（勿改）**：ref 75 "Determinisitic"（deriv. of 原记录镌录错误）、
    ref 91 页码 "663-661"——经 pdfTeX 文本层与 300dpi 双重确认属源文件写法。
- 结果：**PASS±**（仅 ff 伪影；无内容级差异）。
- 备注：本页无页眉页码；文献流 73→74 自然续接。

## p.006（PDF p.6）
- PNG：audit/p006.png（pngmono 150dpi）
- 核对：**文献 98–120（120 起于页底，续 p.7）**——
  98. Ivanov（Steklov 1 (1984), 1-287）✓；99.（J. Math. Anal. Appl. 157 (1991), 277-292）✓；
  100.（Nonlinear Anal. 11 (1987), 429-436）✓；101. Jensen 最大值原理（Arch. Rat. Mech. Anal. 101 (1988), 1-27）✓；
  102.（Indiana 38 (1989), 629-667）✓；103.（preprint）✓；104.（PAMS 102 (1988), 975-978）✓；
  105. Jensen–Souganidis（TAMS 301 (1987), 137-147）✓；106. Kohn–Nirenberg（CPAM 20 (1967), 797-872）✓；
  107. Kruzkov（Math. USSR-Sb. 10 (1970), 217-243）✓；108. Krylov（Springer 1980）✓；109.（Reidel 1987）✓；
  110.（Israel J. Math 55 (1986), 257-266）✓；111.（Math. Ann. 283 (1989), 583-630）✓；
  112.（Appl. Math. Optim. 9 (1982), 177-191）✓；113.（J. Math. Anal. Appl. 131 (1988), 180-193）✓；
  114.（Funkcial. Ekvac. to appear）✓；115.（preprint）✓；116.（Pitman 1982）✓；117.（Acta Appl. 1 (1983), 17-41）✓；
  118.（Taniguchi 1984）✓；119.（Comm. PDE 8 (1983), 1101-1174 and 1229-1276）✓；120 头部（…Soc. 88）✓
  - MR 号逐位吻合 ✓；**文本层精确对账**：仅 ff→f 伪影 9 处词位（refs 101/102/104/108/112×2/118/119×2）。
- 结果：**PASS±**
- 备注：ref 120 跨页（p.6 页底 "Proc. Amer. Math. Soc. 88" → p.7 "(1983), 503-508"）；md 将其拆为两段（排版级）。

## p.007（PDF p.7）
- PNG：audit/p007.png（pngmono 150dpi）
- 核对：**ref 120 尾部 + 文献 121–139**——
  120 尾（"(1983), 503-508. MR0699422"）✓；121.（Duke 52 (1985), 793-820）✓；122.（Appl. Anal. 20 (1985), 283-308）✓；
  123.（Colloque De Giorgi, Pitman 1985）✓；124.（Nonlinear Differential Equations and Applications, Pitman 1988）✓；
  125.（Acta Math. 161 (1988), 243-278）✓；126.（LNM 1390, Springer 1989；Trento 1988）✓；127.（J. Funct. Anal. 86 (1989), 1-18）✓；
  128. Lions–Papanicolau–Varadhan（preprint）✓；129.（Nonlinear Anal. 11 (1987), 613-622）✓；
  130. Lions–Nisio（Proc. Japan Acad. 58 (1982), 273-276）✓；131. Lions–Rochet（PAMS 90 (1980), 79-84）✓；
  132.（IMA vol. 10, Springer 1988）✓；133.（C. R. Acad. Sci. 311 (1990), 259-264）✓；
  134.（Rev. Math. Ibero. 3 (1987), 275-310）✓；135. Mignot（J. Funct. Anal. 22 (1976), 130-185）✓；
  136. Newcomb（Univ. of Wisconsin-Madison 1988）✓；137.（DIE 3 (1990), 77-91）✓；138.（preprint）✓；
  139 头部（…nonnegative charac-）✓
  - MR 号逐位吻合 ✓；**文本层精确对账**：ff→f 伪影 6 处（refs 122/124/126×2/132×2）+ 重音修饰符
    伪影（Contrˆole、in´equations、Ole˘ınik）——排版级。
  - **源自身特征，md 忠实（勿改）**：ref 124/128 的 MR 号（0667669、0909709）与 ref 116/123 重复（源数据如此）；
    ref 128 "G. Papanicolau"、ref 131 仅 "Rochet"、ref 136 "equations Univ." 无逗号——均系源写法。
- 结果：**PASS±**
- 备注：ref 139 跨页（"charac-" → p.8 "teristic form"）。

## p.008（PDF p.8）
- PNG：audit/p008.png（pngmono 150dpi）
- 核对：**ref 139 尾部 + 文献 140–162（162 起于页底，续 p.9）**——
  139 尾（"teristic form … MR0457908"）✓；140. Osher–Sethian（J. Comp. Physics 79 (1988), 12-49）✓；
  141.（TAMS 317 (1990), 723-747）✓；142.（SIAM J. Math. Anal. 19 (1988), 295-311）✓；
  143. Pucci（Boll. Un. Mat. Ital. (6) 21 (1966), 228-233）✓；144. Rouy–Tourin（preprint）✓；145. Rudin（McGraw-Hill 1987）✓；
  146. M. Sato（Proc. Japan Acad. 66 (1990), 252-256）✓；147. Yamada（Funkcial. Ekvac. 30 (1987), 417-425）✓；
  148. Sayah（Comm. PDE 16 (1991), 1057-1221）✓；149.（SICON 24 (1986), 552-562）✓；150.（SICON 24 (1986), 1110-1122）✓；
  151.（JOTA 57 (1988), 121-141）✓；152.（preprint）✓；153. Souganidis（Nonlin. Anal. 9 (1985), 217-257）✓；
  154.（JDE 56 (1985), 345-390）✓；155.（JDE 59 (1985), 1-43）✓；156.（PAMS 96 (1986), 323-330）✓；
  157. Tataru（J. Math. Anal. Appl. 163 (1992), 345-392）✓；158.（Rev. Mat. Ibero. 4 (1988), 453-468）✓；
  159. Trudinger（Proc. Roy. Soc. Edinburgh A 108 (1988), 57-65）✓；160.（Bull. Austral. Math. Soc. 39 (1989), 443-447）✓；
  161. Vila–Zariphopolou（preprint）✓；162 头部（…Markov-）✓
  - MR 号逐位吻合 ✓；**文本层精确对账**：ff→f 伪影 6 处（refs 148×2/153/154/155/160）+ H¨older 重音伪影。
  - **"Partres I and II"（ref 148）经文本层确认系源自身拼写**——md 忠实（勿改）。
- 结果：**PASS±**
- 备注：ref 162 跨页；139/162 在 md 中均为分段表示（排版级）。

## p.009（PDF p.9，**末页**）
- PNG：audit/p009.png（pngmono 150dpi）
- 核对：
  - ref 162 尾："Chain parameters, SIAM J. Control Optim. 30 (to appear, 1992). MR1160145" ✓
  - 尾注："Note: This list reflects references listed in the original paper as accurately as possible with
    no attempt to correct errors." ✓
  - 版权行："© Copyright American Mathematical Society 2021" → md 作 "c Copyright …"（**©→c** 1 处）
- 结果：**PASS±**（±：©→c 单符号，非误导）
- 备注：本页其余空白。

## 总评
- **覆盖声明**：9 页全部逐页审计（audit/p001–p009.png，pngmono 150dpi）；另因本件为 pdfTeX 数字打印件
  （含精确文本层），对全部 9 页做了 `pdftotext` 逐字符复核（见各页"文本层精确对账"）。
- 结论分布：**PASS± ×9；FAIL ×0**。
- 内容级缺陷（仅 1 处）：p.1 "provided that for **y → x**" 的箭头丢失（300dpi + 文本层双重确认）——
  引用 superjet 定义时须补 `\to`。
- 系统性瑕疵：①**ff 合字提取丢失 53 处词位**（p.1×4 / p.2×10 / p.3×6 / p.4×6 / p.5×6 / p.6×9 / p.7×6 / p.8×6：
  Differential→Diferential、diffusion→difusion、effects→efects、Caffarelli→Cafarelli 等）——检索时需宽匹配；
  ②重音字符以修饰符分解（Contrˆole、in´equations、H¨older、Ole˘ınik、Poincar´e）；③空格/换行合并（"ofthe" 等）；
  ④标记表示混用（ref 56 `R<sup>n</sup>` vs ref 59 `\mathbb{R}^n`）；⑤UI chrome（p.1）与 ©→c（p.9）。
- 忠实性正面案例（勿改）：1-UCSB；Cappuzzo-Dolcetta；Determinisitic；页码 663-661；Partres I and II；
  重复 MR 号（0667669/0909709）；Papanicolau；Rochet；无逗号的 "B. Perthame Exponential"。
- 可用性：9 页文本与 162 条文献可放心引用；唯一须手工修复的是 p.1 的 "→"。
- mineru 解析信息：mineru 3.4.4 / tier=basic / **parse_mode=txt**（本 PDF 含文本层；ff→f 系该字体
  ff 合字在 mineru 文本提取路径未还原，而 `pdftotext` 可还原）。
