# AUDIT — Allyn Jackson《The Work of Alessio Figalli》（ICM 2018 会议报告，pdfTeX born-digital，4p）

> mineru: standard 档云端解析；审计依据 = `audit/icm18_figalli_pNNN.png`（pngmono 150dpi）+
> pdftotext 文本层逐字符对账。

## p.001
- 核对：作者署名 Allyn Jackson ✓；开篇评价段（~150 publications/at 34）✓；书籍搬运最优传输比喻
  （n books/cost n moves）✓；Monge 250 年前/Kantorovich 1940s 复兴/1975 Nobel ✓；
  1980s 理论进展与应用列表 ✓
- 结果：**PASS±**（±：页码未收；diferent/cofee ff→f 伪影）

## p.002
- 核对：等周问题（fencing/circle/soap bubbles）✓；晶体形变/能量 E/√E 平均位移结果 ✓；
  semi-geostrophic equations（1990s 气象学、velocity/pressure/geostrophic wind）✓；
  存在唯一性困难段 ✓
- 结果：**PASS±**（±：页码未收；diferential ff→f 伪影）

## p.003
- 核对：Monge-Ampère 方程段（differential geometry/kinetic energy/water droplets）✓；
  De Philippis 合作突破、Ambrosio-Colombo 三维凸域全解 ✓；free boundary 开头
  （ice/obstacle problem/membrane-ball）✓——"could **possesses** singularities" 与
  "membrane **bounded on** a wire"：文本层证实**原刊即印此形**（源级语法笔误，md 忠实保留）
- 结果：**FAIL（两点）**：①md 5 处作字面 "Monge-Amp\`ere"——原刊为 **Monge-Ampère**（è，
  文本层证实）；②"allow **opti mal** transport"——mineru 拆词（原刊 optimal，跨行连字）。
  修复：Amp\`ere→Ampère；opti mal→optimal。

## p.004
- 核对：Caffarelli 1977 自由边界光滑性（singular points 几何描述）✓；二维局限 40 年 ✓；
  Figalli-Serra 2017 完整描述（3D isolated singularities/any dimension sharp result）✓；
  收尾评价段（expositions/friendliness/ideal leader）✓——
- 结果：**FAIL（单点）**：md "Luis **Cafarelli**"——原刊 **Caffarelli**（双 f，ff→f 伪影入人名，
  妨碍检索）。修复：Cafarelli→Caffarelli。

## 总评
- 4/4 页逐页目检+文本层对账；FAIL 3 点（Ampère×5、opti mal、Caffarelli）修复后可作忠实底本；
  原刊 quirk 2 项（possesses、bounded on）忠实保留。
