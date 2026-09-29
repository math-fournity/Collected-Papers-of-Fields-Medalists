# AUDIT — IMU Citation, Akshay Venkatesh（Fields Medal 2018 官方颁奖词，short + long citation，IMU 件）

> mineru: standard 档云端解析；审计依据 = `audit/citation_venkatesh_pNNN.png`（pngmono 150dpi）+
> born-digital 文本层。2 页（short 1 页 + long 1 页）。

## p.001（short citation）
- 核对：颂词一句（analytic number theory/homogeneous dynamics/topology/representation theory、
  equidistribution of arithmetic objects、long-standing 带连字符）逐字 ✓
- 结果：**PASS±**（±：页码未收）

## p.002（long citation）
- 核对：六段结构逐字 ✓——subconvexity for GL(2)/Michel、local-global/Ellenberg、
  Einsiedler-Lindenstrauss-Michel 周期环面轨道、Einsiedler-Margulis-Mohammadi、
  Cohen-Lenstra/Ellenberg-Westerland 函数域——但两处：
- 结果：**FAIL（两点）**：①"established **efective** equidistribution"——原刊 **effective**（双 f，
  150dpi 清晰）；②"periodic torus orbits in SL(3, Z) **SL(3, R)**"——原刊为
  **SL(3, Z)\SL(3, R)**（差集反斜杠被丢）。修复：efective→effective；补 \。

## 总评
- 2/2 页逐页目检+文本层对账；2 点 FAIL 修复后 md 可作忠实底本。

### 修复登记（2026-09-29）
- efective→effective；SL(3,Z)\SL(3,R) 补 \backslash。fix commit 见 `git log --grep 'fix(md): IMU citation Venkatesh'`。
