# T034 数据与版式核查报告（Antigravity）

- **读取提交号**：`7448e41`（`FeCoMn/to_agent/FeCoMn-T034_Figure6_3x3.md`）
- **核查对象**：`FeCoMn/from_agent/FeCoMn-T034/`（3×3 九面板 Figure 6 图件、`a–c` 数据表及绘图脚本 `build_t034_v2.py`）
- **核查结论**：**全部通过**。九面板排版与 `Fig6_layout_preview_20261118.png` 一致，`a–c` 新增数据与原始 LOBSTER / VASP `DOSCAR` / `OUTCAR` 精确吻合，`d–i` 原图保留面板数值未发生任何变动。

---

## 1. 第一排新增面板（`a–c`）逐项核查

| 面板 | 核查项 | 原始文件数值 | 图面及 `data/*.csv` 数值 | 结论 |
|---|---|---|---|---|
| **a** (`Axial bond, −ICOHP`) | `FeCoMn–NC` 轴向 `Mn238–O247` (`Mn–OH`) | bond #26, $d = 1.87724\text{ \AA}$, $-\text{ICOHP} = 2.64030\text{ eV}$ | `1.88 Å`, `2.64` (`a_FCM_axial.csv` 301 点一致) | **一致** |
| **a** (`Axial bond, −ICOHP`) | `Mn–NC` 轴向 `Mn179=O180` (`Mn=O`) | bond #25 (`MnNC_axial_COHP_raw_verified_20261118.csv`), $d = 1.57708\text{ \AA}$, $-\text{ICOHP} = 8.03278\text{ eV}$ | `1.58 Å`, `8.03` (`a_MnNC_axial.csv` 301 点一致) | **一致** |
| **b** (`Mn 3d before adsorption`) | `FeCoMn–NC` (`Mn238`) & `Mn–NC` (`Mn179`) 自旋分辨 3d PDOS 与磁矩 | `FCMnew_base_full`: $\mu_{\text{Mn}} = 3.210\ \mu_{\text{B}}$<br>`MnNC_base_full`: $\mu_{\text{Mn}} = 0.289\ \mu_{\text{B}}$ | `3.21 μB`, `0.29 μB`；展宽参数与 `d` 统一（$\sigma = 0.10\text{ eV}$） | **一致** |
| **c** (`Metal 3d before adsorption`) | 三样品吸附前反应位金属 3d 总 PDOS 及占据态 $\varepsilon_{\text{d}}$ (`−8 ~ 0 eV`) | • `FCM` (`Mn238`): $-3.4212\text{ eV}$<br>• `FCN` (`Fe206, Co234, Co235` 均值): $(-2.7944 - 2.1732 - 2.2032)/3 = -2.3903\text{ eV}$<br>• `MnNC` (`Mn179`): $-3.4426\text{ eV}$ | `−3.42`, `−2.39`, `−3.44`（竖虚线位置与数值完全对应） | **一致** |

## 2. 第二、三排沿用面板（`d–i`）及版式核查

- **d–i 数据一致性**：直接复用 `fig6_v6_20261103.py` 的后面板代码与同一批 CSV 输入，曲线、柱高、火山图点位及示意图结构零改动。
- **细节修正核对**：
  - 面板 `e` 内 `"OOH*"` 与 `"OH*"` 已按任务单要求取消粗体（`fontweight='normal'`）。
  - 面板 `b`、`c` 已统一采用与面板 `d` 相同的高斯展宽函数 `broaden(e, y, s=0.10)`。
  - 面板 `c` 中 `FeCoMn–NC` 的 $\varepsilon_{\text{d}}$ 竖虚线高度已调至文字框下方，不与 `"FeCoMn–NC"` 重叠。
  - 面板 `i` 右下角元素图例（`Fe, Co, Mn, O, N, C, H`）已完整收纳在画布右边界之内，无裁切。
