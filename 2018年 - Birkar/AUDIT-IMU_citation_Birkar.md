# AUDIT — IMU Citation, Caucher Birkar（Fields Medal 2018 官方颁奖词，short + long citation，IMU 件）

> mineru: standard 档云端解析，导出 `IMU_citation_Birkar_2018_mineru/`；
> 审计依据 = `audit/citation_birkar_pNNN.png`（pngmono 150dpi）+ born-digital 文本层（dvipdfmx）。
> PDF 结构：2 页（short citation 1 页 + long citation 1 页）。

## p.001（short citation）
- PNG：audit/citation_birkar_p001.png
- 核对："— Birkar short citation —" 标题 + 一句颂词（"For the proof of the boundedness of Fano
  varieties and for contributions to the minimal model program."）逐字 ✓
- 结果：**PASS±**（±：页码 1 未收）

## p.002（long citation）
- PNG：audit/citation_birkar_p002.png
- 核对：long citation 三段逐字 ✓——MMP/Fano fibering 定义、Cascini-Hacon-M^cKernan 合作
  （M<sup>c</sup>Kernan 上标 c 系原刊排印，md 忠实）、canonical rings 有限生成、Borisov-Alexeev-Borisov
  猜想、Hacon-McKernan-Xu ✓
- 结果：**PASS±**（±：①页码 2 未收；②"pseudo efective" 系原刊原样（单 f，无连字符），md 忠实）

## 总评

- **覆盖声明**：2/2 页逐页目检 + 文本层对账。mineru standard 档。
- **可信度**：颂词全文逐字吻合；无 FAIL。
- **可用性结论**：md 可作为该 citation 的忠实底本。
