# T044 独立复核报告：SI 图 S30、表 S7 与表 S11（Antigravity）

复核人：Antigravity（与制图/撰稿方 Claude web 跨家族独立复核）  
任务单：`FeCoMn/to_agent/FeCoMn-T044_Fig6i_geometry_and_SI_S31.md`（更新至 `1206975`）  
核查基线：
- 待核图件：`FeCoMn/from_agent/FeCoMn-T044/FigS30_ClaudeWeb_draft.png`
- 待核文档：`FeCoMn/manuscript/FeCoMn_SI_revised_20261121_1850.docx`（`71a695a`）及正文 `FeCoMn_Manuscript_revised_20261121_1850_plaintext.txt`
- 原始数据源：`FeCoMn/from_agent/FeCoMn-T042_Mn_position/Antigravity.csv`、`FeCoMn/from_agent/FeCoMn-T041/REPORT.md`、`FeCoMn/from_agent/FeCoMn-T039/REPORT.md`

---

## 总体结论

| 核查对象 | 核查结论 | 数值/公式偏差 | 备注与轻微建议 |
|---|---|---|---|
| **SI 图 S30（`FigS30_ClaudeWeb_draft.png`）** | **通过** | **0 处** | 全部柱位、正负方向、`n/a` 与 0 线及图注文字完全准确；仅建议定稿替换时微调面板字母 `a`/`b` 对齐各自 y 轴标题竖线（见 §1） |
| **SI 表 S7** | **通过** | **0 处** | 5 个单元格数值、单位、小数修约及表注 `Table S12` 口径引用与 `T039/REPORT.md` 逐项一致 |
| **SI 表 S11** | **通过** | **0 处** | 8 个分解值正负号与加和严格闭合（`OH*` `+0.336`、`OOH*` `+0.267`），`0.52 V`/`0.78 V` 与 `T042`/`Table S8` 一致 |

---

## 一、SI 图 S30（`FigS30_ClaudeWeb_draft.png`）逐点数值与视觉核查

### Panel (a)：`Mn height from N4 plane (Å)`（对照 `FeCoMn-T042_Mn_position/Antigravity.csv` `FCM_8O_*`）

| 吸附阶段 | 系列 | 图 S30a 读数（视觉柱位） | `Antigravity.csv` 原值（Å） | 核对结果 |
|---|---|---|---|---|
| `Before` | `With axial OH` | 约 `+0.44`（正值指向轴向 OH） | `+0.4418` | **一致** |
| `Before` | `Without axial OH` | 略低于 `0.0` 线（约 `-0.01`） | `-0.0096` | **一致** |
| `OOH*` | `With axial OH` | 紧贴 `0.0` 线极微正值 | `+0.0026` | **一致** |
| `OOH*` | `Without axial OH` | 无柱，标注 `n/a` | 8O* 模型未算 | **一致** |
| `O*` | `With axial OH` | 约 `-0.10` | `-0.0975` | **一致** |
| `O*` | `Without axial OH` | 略低于 `-0.40` | `-0.4057` | **一致** |
| `OH*` | `With axial OH` | 略低于 `0.0` 线（约 `-0.01`） | `-0.0093` | **一致** |
| `OH*` | `Without axial OH` | 略低于 `-0.45` | `-0.4562` | **一致** |

### Panel (b)：`ΔE vs. Mn without axial OH (eV)`（对照 `FeCoMn-T041/REPORT.md` §3 同参考静态口径）

| 分解项 | 系列 | 图 S30b 读数（视觉柱位） | `T041/REPORT.md` 原值（eV） | 核对结果 |
|---|---|---|---|---|
| `Total` | `OH*` | 约 `+0.336` | `+0.335994`（报 `+0.336`） | **一致** |
| `Total` | `OOH*` | 约 `+0.267` | `+0.267193`（报 `+0.267`） | **一致** |
| `Structural` | `OH*` | 约 `+0.236` | `+0.236229`（报 `+0.236`） | **一致** |
| `Structural` | `OOH*` | 约 `+0.432` | `+0.431726`（报 `+0.432`） | **一致** |
| `Electronic` | `OH*` | 齐平 `+0.10` 刻度线 | `+0.099514`（报 `+0.100`） | **一致** |
| `Electronic` | `OOH*` | 齐平 `-0.10` 刻度线 | `-0.099743`（报 `-0.100`） | **一致** |
| `Adsorbate` | `OH*` | 齐平 `0.0` 线 | `-0.000251`（报 `0.000`） | **一致** |
| `Adsorbate` | `OOH*` | 约 `-0.065` | `-0.064790`（报 `-0.065`） | **一致** |

### 图注与版面核查
- `1850` 版 SI `P@242` 图注已准确说明 8O* 背景、正方向指向轴向 OH、`OOH*` 无轴向 OH 标 `n/a`、正值表示吸附减弱及数值见 `Table S11`。
- 正文 `1850` 版（L364、L368）对应引用 `Figure S30a` 与 `Figure S30b` 均已同步正确。
- **轻微版面建议（非硬错）**：目前 `a`/`b` 字母略在各自 y 轴标题竖线左侧；按赵月出图规则，若后续重绘定稿版本，建议把 `a`/`b` 水平对齐到各自 y 轴标题中心/竖线上。

---

## 二、SI 表 S7 逐格核查（`FeCoMn_SI_revised_20261121_1850.docx` `TABLE@274`）

对照源数据：`FeCoMn/from_agent/FeCoMn-T039/REPORT.md` §5–§6（`Table S10`/`Table S12` 覆盖度参考态口径 `G(H₂) = −6.834 eV`）。

| 行 | 字段 | SI 表 S7 数值 | `T039/REPORT.md` 源数据 | 核对结果 |
|---|---|---|---|---|
| `FeCoMn–NC (8O* particle and support)` | `E(Mn–OH) (eV)` | `−2140.14786` | `−2140.14786` | **一致** |
| 同上 | `E(Mn=O) (eV)` | `−2135.49370` | `−2135.49370` | **一致** |
| 同上 | `Mn=O length (Å)` | `1.655` | `1.655` | **一致** |
| 同上 | `U* (V)` | `0.96` | `0.960`（两位小数 `0.96`） | **一致** |
| `Particle removed (same support atoms and geometry)` | `E(Mn–OH) (eV)` | `−1671.76397` | `−1671.76396918` | **一致** |
| 同上 | `E(Mn=O) (eV)` | `−1667.58789` | `−1667.58789271` | **一致** |
| 同上 | `Mn=O length (Å)` | `1.580` | `1.5798` | **一致** |
| 同上 | `U* (V)` | `0.48` | `0.482`（两位小数 `0.48`） | **一致** |

- 表注（`P@275`）明确说明采用 `σ → 0` 能量、固定载体坐标、保持 `Mn` 初始磁矩 `3 μB` 及按 `Table S12` 覆盖度参考态计算 `U*`，无隐瞒或口径混用；正文 L297、L350 引用 `Table S7` 无误。

---

## 三、SI 表 S11 逐格核查（`FeCoMn_SI_revised_20261121_1850.docx` `TABLE@285`）

对照源数据：`FeCoMn/from_agent/FeCoMn-T041/REPORT.md` §3 及 `FeCoMn-T042_Mn_position/Antigravity.csv`。

| 中间体 | 字段 | SI 表 S11 数值 | 源数据原值 | 核对结果 |
|---|---|---|---|---|
| `OH*` | `Total (eV)` | `+0.336` | `+0.335994`（`+0.336`） | **一致** |
| `OH*` | `Structural (eV)` | `+0.236` | `+0.236229`（`+0.236`） | **一致** |
| `OH*` | `Electronic (eV)` | `+0.100` | `+0.099514`（`+0.100`） | **一致** |
| `OH*` | `Adsorbate (eV)` | `0.000` | `-0.000251`（`0.000`） | **一致** |
| `OOH*` | `Total (eV)` | `+0.267` | `+0.267193`（`+0.267`） | **一致** |
| `OOH*` | `Structural (eV)` | `+0.432` | `+0.431726`（`+0.432`） | **一致** |
| `OOH*` | `Electronic (eV)` | `−0.100` | `-0.099743`（`−0.100`） | **一致** |
| `OOH*` | `Adsorbate (eV)` | `−0.065` | `-0.064790`（`−0.065`） | **一致** |

- 加和校验：`OH*`: `+0.236 + 0.100 + 0.000 = +0.336`；`OOH*`: `+0.432 − 0.100 − 0.065 = +0.267`，均严格闭合。
- 表注（`P@286`）`0.52 V`（`FCM_8O_bare` `U_L = 0.5157 V`、`OH*` 脱附限速）与 `0.78 V (Table S8)`（`0.7757 V`）核对无误；正文 L362、L368 引用 `Table S11` 无误。

---

## 四、后续待办

- **图 6i 复核待接力**：待 Claude Code 本地按 `FeCoMn-T044` 第 1 项改完图 6i 并交付到 `FeCoMn/from_agent/FeCoMn-T044/` 后，再由 Antigravity 做像素差分与构型/标注独立复核。
