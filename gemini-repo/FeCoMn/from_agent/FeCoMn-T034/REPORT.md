# FeCoMn-T034 交付报告：Figure 6（3×3 九面板）

- **读取任务单提交号**：`7448e41`（`FeCoMn/to_agent/FeCoMn-T034_Figure6_3x3.md` 及预览图 `FeCoMn/to_agent/Fig6_layout_preview_20261118.png`）
- **出图与核查执行方**：Antigravity（基于原 `fig6_v6_20261103.py` 沿用下两排 d–i，新增第一排 a–c 并统一高斯展宽与版式对齐）
- **范围确认**：未提交任何新 DFT 计算，未修改任何 Word 文档（`.docx`）。

---

## 1. 交付文件清单

1. **汇总草图与印刷级图件**：
   - `FeCoMn/from_agent/FeCoMn-T034/Figure6_draft.png`（300 dpi 预览主入口）
   - `FeCoMn/from_agent/FeCoMn-T034/draft_20261118_v2/Figure6_T034_preview.png`（300 dpi 预览）
   - `FeCoMn/from_agent/FeCoMn-T034/draft_20261118_v2/Figure6_T034_600dpi.png`（600 dpi 印刷版 PNG）
   - `FeCoMn/from_agent/FeCoMn-T034/draft_20261118_v2/Figure6_T034.pdf`（矢量 PDF）
   - `FeCoMn/from_agent/FeCoMn-T034/draft_20261118_v2/Figure6_T034_editable.svg`（可编辑字体 SVG）
   - `FeCoMn/from_agent/FeCoMn-T034/draft_20261118_v2/Figure6_T034_Arial_paths.svg`（转曲 SVG）
   - `FeCoMn/from_agent/FeCoMn-T034/build_t034_v2.py`（绘图脚本）
2. **新增第一排 `a–c` 曲线及数值表（`FeCoMn/from_agent/FeCoMn-T034/data/`）**：
   - `a_FCM_axial.csv`、`a_MnNC_axial.csv`、`a_display_scale.csv`
   - `b_FCM_Mn_spin.csv`、`b_MnNC_Mn_spin.csv`
   - `c_FCM_metal_d.csv`、`c_FCN_metal_d.csv`、`c_MnNC_metal_d.csv`、`c_centroids.csv`

---

## 2. 九面板布局与数据源说明

### 第一排：吸附前背景态（Before adsorption）

| 面板 | 内容 | 原始数据路径 | 原子/键编号与图内标注核对 |
|---|---|---|---|
| **a** | 轴向键 `−pCOHP`（`Axial bond, −ICOHP (eV)`） | • `FeCoMn–NC`: `电子结构后处理核查_20261031/fig6_data/COHPCAR_base.lobster` (bond #26) 及 `ICOHPLIST_base.lobster`<br>• `Mn–NC`: `FeCoMn-T033/MnNC_source_trace_20261118/MnNC_axial_COHP_raw_verified_20261118.csv` (bond #25) | • 上：`FeCoMn–NC  Mn–OH`（`Mn238–O247`，键长 `1.88 Å`，`−ICOHP = 2.64 eV`）<br>• 下：`Mn–NC  Mn=O`（`Mn179=O180`，键长 `1.58 Å`，`−ICOHP = 8.03 eV`）<br>• 能量范围 `−8 ~ 1 eV`，填充 $E < E_{\text{F}}$ 的成键正值区 |
| **b** | 吸附前 Mn 3d 自旋分辨 PDOS（`Mn 3d before adsorption`） | • `Genkai`: `fcm_static_20261029/FCMnew_base_full/DOSCAR` & `OUTCAR`<br>• `Genkai`: `fcm_static_20261029/MnNC_base_full/DOSCAR` & `OUTCAR`<br>（提取缓存于 `data/background_spin_PDOS.json`） | • 上：`FeCoMn–NC`（`Mn238`，$\mu_{\text{Mn}} = 3.21\ \mu_{\text{B}}$）<br>• 下：`Mn–NC`（`Mn179`，$\mu_{\text{Mn}} = 0.29\ \mu_{\text{B}}$）<br>• 采用与面板 `d` 相同的高斯展宽 $\sigma = 0.10\text{ eV}$，上正下负，标灰 `↑`/`↓` |
| **c** | 吸附前反应位金属 3d 总 PDOS（`Metal 3d before adsorption`） | • `FeCoMn–NC` (`Mn238`) & `Mn–NC` (`Mn179`): 同 **b**（`d_up + d_down`）<br>• `FeCo–NC` (`Fe206, Co234, Co235`): `单图汇总_journal_20261025/10_计算_第三轮/calc_PDOS_FCN_base_journal_20261025.csv` & `atom_resolved_occupied_d_centers.csv` | • `FeCoMn–NC`: $\varepsilon_{\text{d}} = -3.42\text{ eV}$<br>• `FeCo–NC`: $\varepsilon_{\text{d}} = -2.39\text{ eV}$（三接触金属 `Fe206 = −2.794`、`Co234 = −2.173`、`Co235 = −2.203 eV` 均值）<br>• `Mn–NC`: $\varepsilon_{\text{d}} = -3.44\text{ eV}$<br>• 高斯展宽 $\sigma = 0.10\text{ eV}$，竖虚线标出占据态 $\varepsilon_{\text{d}}$ |

### 第二、三排：完全沿用原 `fig6_v6_20261103.py` 面板（位置与字母更新为 `d–i`）

- **d**（原 6c）：三样品 `OOH*` 吸附态金属 3d 与 O 2p PDOS（$\varepsilon_{\text{d}} = -3.40,\ -2.40,\ -2.96\text{ eV}$）。
- **e**（原 6d）：三样品 `OOH*`（`3.12, Σ 3.11, 2.65 eV`）与 `OH*`（`3.06, Σ 3.19, 2.72 eV`）金属–O 键 `−pCOHP`，已按任务单去掉图内 `"OOH*"` 与 `"OH*"` 粗体。
- **f**（原 6e）：三样品成键金属 Bader 电荷变化 `Bonded-metal |ΣΔN| (e)`。
- **g**（原 6f）：三样品吸附物电子富集 `Adsorbate electron excess (e)`。
- **h**（原 6g）：火山图 $U_{\text{L}}$ vs $\Delta G_{\text{OH*}}$。
- **i**（原 6h）：`FeCo (8O*)` + `Mn–N4–OH` 活性位结构与四电子 ORR 循环示意图（底部七元素图例已完整收纳于第三列画布内，无右侧裁切）。
