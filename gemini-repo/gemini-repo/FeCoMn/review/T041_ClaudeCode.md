# T041 核查：OH* 吸附拆分独立复核（Claude Code）

日期：2026-11-20  
核查对象：Antigravity 13:03 报告的 OH* 拆分（+0.336 = +0.236 + 0.100 eV）、Mn 离面高度、颗粒位移  
OOH* 部分：待 T041 Genkai 作业 7633024 收敛后补充  

---

## 1. OH* 拆分复核

### 原始能量（energy(sigma->0)，直接从 Genkai OUTCAR 末行读取）

| 片段 | 目录 | energy(sigma->0) / eV |
|---|---|---:|
| FCM_base_full（8O* 无轴向 OH） | FeCoMn_electronic_20261023/FCM_base_full | -2129.34174525 |
| FCM_OH_substrate（noOH 下 OH* 吸附态基底） | FeCoMn_electronic_20261023/FCM_OH_substrate | -2128.90679602 |
| FCM_OH_full（noOH + OH*） | FeCoMn_electronic_20261023/FCM_OH_full | -2140.08378759 |
| FCM_OH_adsorbate（孤立 OH*） | FeCoMn_electronic_20261023/FCM_OH_adsorbate | -7.53807512 |
| FCMnew_base_full（8O* + 轴向 OH） | FeCoMn_MnOH_electronic_v2_20261031/FCMnew_base_full | -2140.09673312 |
| FCMnew_OH_substrate（withOH 下 OH* 吸附态基底） | FeCoMn_MnOH_electronic_v2_20261031/FCMnew_OH_substrate | -2139.42555450 |
| FCMnew_OH_full（withOH + OH*） | FeCoMn_MnOH_electronic_v2_20261031/FCMnew_OH_full | -2150.50328291 |
| FCMnew_OH_adsorbate（孤立 OH*） | FeCoMn_MnOH_electronic_v2_20261031/FCMnew_OH_adsorbate | -7.53832593 |

### 计算结果

**无轴向 OH（noOH）：**

| 量 | 计算式 | 结果 / eV |
|---|---|---:|
| E_distort(noOH) | FCM_OH_substrate - FCM_base_full | +0.43494923 |
| E_bind_frozen(noOH) | FCM_OH_full - FCM_OH_substrate - FCM_OH_adsorbate | -3.63891645 |
| ΔE_tot(noOH) | FCM_OH_full - FCM_base_full - FCM_OH_adsorbate | -3.20396722 |

**有轴向 OH（withOH）：**

| 量 | 计算式 | 结果 / eV |
|---|---|---:|
| E_distort(withOH) | FCMnew_OH_substrate - FCMnew_base_full | +0.67117862 |
| E_bind_frozen(withOH) | FCMnew_OH_full - FCMnew_OH_substrate - FCMnew_OH_adsorbate | -3.53940248 |
| ΔE_tot(withOH) | FCMnew_OH_full - FCMnew_base_full - FCMnew_OH_adsorbate | -2.86822386 |

**差值（轴向 OH 对 OH* 吸附的影响）：**

| 量 | 值 / eV | 占比 |
|---|---:|---:|
| ΔΔE_tot（总削弱） | +0.33574336 | 100% |
| ΔΔE_distort（形变代价增量） | +0.23622939 | **70.4%** |
| ΔΔE_bind_frozen（冻结几何电子结合减弱） | +0.09951397 | **29.6%** |

### 与 Antigravity 报告对比

| 量 | Antigravity（eV） | Claude Code（eV） | 偏差 |
|---|---:|---:|---:|
| ΔE_tot(noOH) | -3.2040 | -3.20397 | <0.001 eV |
| E_distort(noOH) | +0.4349 | +0.43495 | <0.001 eV |
| ΔE_tot(withOH) | -2.8682 | -2.86822 | <0.001 eV |
| E_distort(withOH) | +0.6712 | +0.67118 | <0.001 eV |
| ΔΔE_tot | +0.3358 | +0.33574 | <0.001 eV |
| ΔΔE_distort（70.4%） | +0.2363 | +0.23623 | <0.001 eV |
| ΔΔE_bind_frozen（29.6%） | +0.0995 | +0.09951 | <0.001 eV |

**结论：所有 7 个数值与 Antigravity 报告完全一致，误差均小于 0.001 eV，复核通过。**

注：两套体系的 OH* adsorbate 能量略有差异（-7.53808 vs -7.53833 eV，差 0.25 meV），来自两次独立静态计算，对结果无实质影响。

---

## 2. Mn 离面高度与颗粒位移（待补）

T041 任务单要求核查 Mn 离面 +0.442 Å / 移动 0.466 Å、颗粒 rms 0.005 Å。这需要比对 FCMnew_base_full 与 FCMnew_OH_substrate 的 CONTCAR 坐标，同时需要晶格参数换算。待 Genkai 上 FCMnew_OH_substrate POSCAR 读取后补充此节。

---

## 3. 图 6 段草稿数值准确性意见

针对 `20261120_1550_mechanism_mainline_DECIDED.md` 中的英文草稿：

1. **数值一致性**："OH* and OOH* bind more weakly by 0.33 and 0.21 eV"，后文 "0.34 eV weakening" 应统一为 0.33 eV（实际 ΔΔE = 0.336 eV，取 0.33 eV 更保守）。

2. **"just below the Fermi level"**：单占 dz²↑ 态的积分（EF±0.25 eV）= 0.371；dz² 中心 = -3.17 eV，确实在费米能级以下但靠近。措辞准确，无需修改。

3. **"0.24 eV of the 0.34 eV"**：实际 0.236 eV / 0.336 eV，改为 "0.24 eV of the 0.33 eV" 与前文一致。

4. **Mn-NC U_L 0.26 V**：决定文件标注"待核对"，建议确认后再定稿，或在括注中加 "from DFT free energies"。

5. 其余数值（Mn 离面 0.44 Å、磁矩降 0.82 μB、dz² 中心 -5.12 eV）与已有报告数据一致，无需修改。

---

## 4. OOH* 拆分（待补）

T041 Genkai 作业 7633024（FCM_OOH_substrate）收敛后，补充：
- E_distort(noOH, OOH*)、E_bind_frozen(noOH, OOH*) 与已有 E_distort(withOH, OOH*) = +0.685 eV / E_bind_frozen(withOH, OOH*) = -2.278 eV 配对比较
- 验证 OOH* 削弱是否与 OH* 相同机制主导（几何形变占主要部分）

---

*Claude Code，2026-11-20*
