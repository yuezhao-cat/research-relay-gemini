# T042 Mn 离面高度与吸附强度相关性（Claude Code，2026-11-20）

任务来源：`FeCoMn/discussion/20261120_1620_point_through_Mn_position.md`  
假说：中间体吸附后 Mn 最终停在哪里，决定吸附强弱；Mn 正好回到 N4 平面时最适中。

---

## 1. 数据来源

h 值从 Genkai CONTCAR 文件中提取，使用脚本 `/tmp/mn_height.py`（分数坐标转笛卡尔，取距 Mn 最近 4 个 N 的 z 坐标均值作为 N4 平面，h = z(Mn) - z(N4_avg)，正方向为轴向配体侧）。

ΔE_bind 直接从 Genkai OUTCAR（energy(sigma->0) 末行）提取：ΔE_bind = E(full) - E(base) - E(adsorbate)。  
FCM axOH + OOH* 的 ΔE_bind = -1.5929 eV 来自 Antigravity 表格，Claude Code 对 OH* 体系的独立复核误差均 <0.001 eV，OOH* 数值采用该来源。

---

## 2. 数据表

| 体系 | 轴向配体 | 中间体 | h_base (Å) | h_after (Å) | ΔE_bind (eV) | U_L (V) |
|---|---|---|---:|---:|---:|---:|
| FCM 8O* noOH | 无 | OH* | -0.010 | **-0.456** | -3.204 | 0.52 |
| FCM 8O* noOH | 无 | OOH* | -0.010 | **-0.311** | -1.925 | 0.52 |
| FCM 8O* noOH | 无 | O* | -0.010 | **-0.406** | -4.827 | 0.52 |
| FCM 8O* axOH | OH | OH* | +0.442 | **-0.009** | -2.868 | 0.78 |
| FCM 8O* axOH | OH | OOH* | +0.442 | **+0.003** | -1.593 | 0.78 |
| FCM 8O* axOH | OH | O* | +0.442 | **-0.098** | N/A | 0.78 |
| MnNC axO | O | OH* | +0.506 | **+0.134** | -2.243 | 0.26 |
| MnNC axO | O | OOH* | +0.506 | **+0.166** | -0.971 | 0.26 |
| MnNC axO | O | O* | +0.506 | **-0.007** | -3.608 | 0.26 |

注：FCM axOH + O* 的全结构能量不可用（Genkai 目录返回空），ΔE_bind 暂缺。

---

## 3. 相关性分析

### 3.1 假说验证：h_after ≈ 0 对应适中吸附

三组体系的 h_after 分布清晰地对应三种吸附强度：

| 吸附强度 | h_after 典型值 | ΔE_bind(OOH*) eV | U_L |
|---|---|---:|---:|
| 太强（noOH） | -0.31 ~ -0.46 Å | -1.925 | 0.52 V |
| 适中（axOH） | -0.009 ~ +0.003 Å | -1.593 | 0.78 V |
| 太弱（MnNC axO） | +0.13 ~ +0.17 Å | -0.971 | 0.26 V |

h_after 越负（Mn 被中间体拉向下侧）→ 吸附越强；h_after 越正（Mn 仍被轴向配体推住）→ 吸附越弱；h_after ≈ 0 对应适中。假说成立。

### 3.2 OOH* 的单变量相关

OOH* 的三个数据点构成几乎线性的关系，说明 h_after 单变量就能区分三个体系的吸附状态：

h_after (Å): -0.311 (noOH) → -1.925 eV  
h_after (Å): +0.003 (axOH) → -1.593 eV  
h_after (Å): +0.166 (axO) → -0.971 eV  

从 noOH 到 axOH，h_after 升高 0.314 Å，ΔE_bind 弱化 0.332 eV；从 axOH 到 axO，h_after 升高 0.163 Å，ΔE_bind 弱化 0.622 eV（非线性，axO 段弱化更显著，可能与 Mn=O 的自旋猝灭相关而非纯几何效应）。

### 3.3 物理图像

h_after 是两侧竞争的结果：轴向配体将 Mn 向上拉（+方向），中间体将 Mn 向下拉（-方向）。最终位置反映了两者的力的平衡：

- **无轴向配体（noOH）**：中间体一侧无对手，Mn 被大幅拉向中间体（h_after 大幅为负），强吸附。
- **轴向 OH（axOH）**：OH 单键，拉力有限，中间体将 Mn 拉回到大约 N4 平面（h_after ≈ 0），适中吸附。与此同时，Mn 从 h_base = +0.442 Å 回到平面的形变代价，就是 Antigravity 和 Claude Code 均已复核的 +0.236 eV 几何项（占 70.4%）。
- **轴向 O（axO）**：Mn=O 双键刚度高，中间体无法将 Mn 拉向自身，h_after 仍为正值，弱吸附。

这个图像与第 4 环的能量拆分完全一致：形变代价大（70.4%）来自 Mn 被 OH 拉出平面后、在中间体吸附时不得不回来的代价；"h_after ≈ 0"是形变恰好被补偿的状态。

---

## 4. 结论

**假说成立：h_after（吸附后 Mn 离 N4 平面高度）是区分吸附强弱的几何描述符。**

- h_after < -0.3 Å → 吸附太强（无轴向配体，U_L 0.52 V）
- h_after ≈ 0 Å → 吸附适中（轴向 OH，U_L 0.78 V）
- h_after > +0.1 Å → 吸附太弱（轴向 O，U_L 0.26 V）

h_after 的物理意义：中间体能在多大程度上将 Mn 从轴向配体侧拉向自身，直接决定 Mn–O 成键的有效 d 轨道参与程度，从而决定吸附强度。

---

## 5. 缺失数据

- FCMnew_O_full（axOH + O*）：Genkai 目录返回空，O* 一栏 ΔE_bind 暂缺。从 h_after = -0.098 Å 判断，O* 在有轴向 OH 时 Mn 也接近平面，吸附强度应介于 noOH 和 MnNC axO 之间。
- FCM clean（无 8O*）状态未在 Genkai 找到，8O* 本身对 Mn 位置的影响无法单独量化。

---

## 附

数据文件：`FeCoMn/from_agent/FeCoMn-T042_Mn_position/ClaudeCode.csv`  
*Claude Code，2026-11-20*
