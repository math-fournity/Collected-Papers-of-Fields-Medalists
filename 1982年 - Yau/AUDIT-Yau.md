# AUDIT — Yau "Calabi's conjecture and some new results in algebraic geometry" (PNAS 74 (1977), 1798-1799)

> mineru standard 档；审计依据 = 二值化渲染 audit/pNNN.png（pngmono 150dpi）对照
> Yau_1977_calabi_conjecture__Yau_1977_calabi_conjecture.md。逐页审计，一页一签。

## p.001（PDF p.1 / 印刷 p.1798）
- PNG：audit/p001.png
- 核对：
  - 题录：标题 ✓、关键词行（Kähler manifold/Chern class/Ricci tensor/complex structure）✓、
    SHING-TUNG YAU ✓、Stanford 地址 ✓、Communicated by S. S. Chern, January 31, 1977 ✓
  - ABSTRACT ✓（Calabi 猜想证明预告 + CPⁿ 上 Kähler 结构唯一性）
  - 正文前半：Chern (ref.1) 第一 Chern 类表示 ✓、Calabi(ref.2,3) 提问与部分结果 ✓、
    Calabi 猜想陈述 ✓
  - 公式 [1]（∂∂̄ log det 复鞍方程）✓、[2]（det(g+φ)det(g)^{-1}=exp F）✓、
    [3]（∫exp F = Vol(M)）✓、[4]（exp(cφ+F)，c=+1,0,−1）✓——双栏布局被正确拍平
  - Nakano 定理引述 ✓、Kähler-Einstein 讨论与 c₁ 三情形 ✓
  - THEOREM 1（c≥0 时 eqs.2,4 可解；c₁≤0 时 Kähler-Einstein 存在，c₁<0 且 Ricci=−1 时唯一）✓
  - Aubin (ref.4,5) 相关评注 ✓
  - THEOREM 2（Ricci≡0 而曲率张量非平凡的紧单连通例；度 n+2 超曲面）✓ 及 Proof ✓
  - THEOREM 3（Ricci 处处为负的紧单连通例；度 > n+2）✓ 及 Proof ✓
  - THEOREM 4（陈述：ample canonical bundle ⟹ 3c₂ ≥ c₁²，等号 ⟺ 球覆盖）✓ 及
    Proof 开头（Chern 定理、曲率张量函数）✓——页末断句 "…be a uni-" 与 p.002 正确衔接
- 结果：**PASS±**
  - ±1：mineru 丢失页眉（Proc. Natl. Acad. Sci. USA, Vol. 74, No. 5, pp. 1798-1799,
    May 1977, Mathematics）与页码 1798；
  - ±2：侧栏 "Downloaded from ... IP address" 水印列未收录（无害）；
  - ±3：双栏连排无页界标记（内容无损，页界以原 PDF 为准）。
- 备注：数学内容零错误；md 忠实保留了原文 "latter occasion" 用词。

## p.002（PDF p.2 / 印刷 p.1799）
- PNG：audit/p002.png（150dpi 二值）；关键公式区另做 300dpi 灰度裁决图
  audit/p002_hi300.png + audit/p002_formula_crop.png
- 核对：
  - Theorem 4 Proof 续：曲率公式 ¼π²{[R₁₂₁₂−2(R₁₃₁₃+R₁₄₁₄)]² + 3(R₁₃₁₃−R₁₄₁₄)² +
    6(R²₁₃₁₂+R²₁₄₁₂+R²₁₄₁₃)} —— **300dpi 裁决：md 与原文逐字一致**（初轮 150dpi 二值图
    曾疑似 π⁴/下标差异，高清复核确认系目检误读，md 无误）；
    3c₂(M) ≥ c₁²(M) 与等号条件 ✓；Ricci 负常数 ⟹ 球覆盖 ✓
  - Remarks (i)：Van de Ven 8c₂≥c₁² ✓、Bogomolv 4c₂≥c₁² ✓（**原文即排印 "Bogomolv"**，
    为 Bogomolov 之刊误，md 忠实保留）、Miyaoka 3c₂≥c₁² ✓
  - Remarks (ii)：Guggenheimer (ref.7) 20 年前已在 Kähler-Einstein 假设下得到该不等式 ✓
  - Remarks (iii)：高维推广 (−1)ⁿc₁^{n−2}c₂ ≥ (−1)ⁿ n/2(n+1) c₁ⁿ ✓
  - Severi 猜想（ref.8）的解决引言 ✓
  - THEOREM 5（同伦于 CP² ⟹ 双全纯于 CP²）✓ 及 Proof（示性数 ¼[c₁²−2c₂]=±1、c₂=3、
    Kodaira ref.9 代数性）✓
  - 正合列 [5] 1→Z→𝒪→𝒪*→1 ✓、长正合列 [6] ✓、H¹(M,Z)=0 与 H²(M,Z)=Z 推导 ✓、
    Hirzebruch–Kodaira (ref.9) c₁²=9 ✓
  - THEOREM 6（球覆盖曲面 N 的同伦类唯一性；Miyaoka ref.10、K-3 排除、K(π,1)、
    Mostow 刚性 ref.11）✓
  - 致谢（Sloan fellowship）+ PNAS 页资费 "advertisement" 18 U.S.C. §1734 声明 ✓
  - REFERENCES 1–11 逐条：Chern 1946 Ann. Math. 47, 85-121 ✓；Calabi 1954 ✓；
    Calabi 1955 ✓；Aubin 1970 J. Diff. Geom. 4, 383-424 ✓；Aubin 1976 C.R. 283, 119-121 ✓；
    Van de Ven Invent. Math. 36, 285-293 ✓；Guggenheimer Experientia 8, 420-421 ✓；
    Severi MR 16, p.397 ✓；Kodaira Collected Works ✓；Miyaoka Proc. Jpn. Acad. Sci. 50 ✓；
    Mostow 1973 ✓
- 结果：**PASS±**
  - ±1：running head（Mathematics: Yau / PNAS 74 (1977) 1799）丢失；
  - ±2：侧栏下载水印列未收录（无害）；
  - ±3：双栏连排无页界标记。
- 备注：**关键曲率公式经 300dpi 高清裁决确认 md 正确**；原文刊误（Bogomolv、C₂、
  "latter occasion"）均被 md 忠实保留——OCR 保真度极高。

## 总评
- 全文 2 页逐页审计完成：**全部 PASS，零数学错误**；一处公式经高清仲裁后确认 md 正确。
- 系统性瑕疵 2 项（同 Fefferman 案例）：running head/页码丢失、无页界标记。
- 结论：md 可作为正文引用与检索底本。
