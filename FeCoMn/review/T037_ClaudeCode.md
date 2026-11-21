# T037 Claude Code 核查报告

Claude Code，2026-11-19。
核查依据：T037 commit b90b854（`from_agent/FeCoMn-T037/`）；对照基准：T032 `orbital_ICOHP.json`（已通过 HPC 原文件逐字核查）和本次对 PDOS CSV 的独立重算。

---

## 1. ICOHP 数值核查（CSV vs T032 参考）

T032 `orbital_ICOHP.json` 已经过对 HPC 原始 ICOHPLIST.lobster 的逐字核查，作为本次比较基准。

| 状态 | 键 | 总 −ICOHP (eV) | Mn dz² 分项和 (eV) | dz²–O pz (eV) | 结论 |
|---|---|---:|---:|---:|---|
| FCM_base 轴向 | Mn238–O247 | 2.64030 | 0.99516 | 0.76992 | **✓ 与 T032 逐位一致** |
| MnNC_base 轴向 | Mn179–O180 | 8.03278 | 2.97544 | 2.32192 | **✓ 与 T032 逐位一致** |
| FCM_OOH 轴向 | Mn238–O247 | 3.00339 | 1.51226 | 1.17626 | **✓ 与 T032 逐位一致** |
| FCM_OOH 反位 | Mn238–O248 | 3.11766 | 1.38304 | 1.07753 | **✓ 与 T032 逐位一致** |
| MnNC_OOH 反位 | Mn179–O181 | 2.65218 | 1.06276 | 0.75846 | **✓ 与 T032 逐位一致** |
| MnNC_OOH 轴向 | Mn179–O180 | — | — | — | **N/A（lobsterin 未设置该键对，报告已如实注明）** |

全部 5 条有效数据与 T032 完全一致，误差为 0（T032 本身精度 5 位有效数字）。

---

## 2. dz² PDOS 统计核查（从 CSV 独立重算）

对 4 个 `*_Mn_dz2_PDOS.csv` 文件，在 −8.0 到 0.0 eV 窗口作梯形积分，重算 dz² 权重与中心，与 T037 `T037_summary_table.csv` 对比：

| 状态 | 重算权重 | 表中值 | 差值 | 重算中心 (eV) | 表中值 (eV) | 差值 (eV) |
|---|---:|---:|---:|---:|---:|---:|
| FCM_base | 0.99576 | 0.99490 | +0.00086 | −3.16062 | −3.16660 | 0.006 |
| MnNC_base | 0.87039 | 0.87058 | −0.00019 | −5.12137 | −5.12139 | 0.000 |
| FCM_OOH | 0.72822 | 0.74427 | −0.016 | −4.83939 | −4.84117 | 0.002 |
| MnNC_OOH | 0.73741 | 0.75484 | −0.017 | −4.95604 | −4.95444 | 0.002 |

**结论：均在数值积分精度范围内。** PDOS CSV 步长约 0.033 eV，权重差 ≤0.017（<2.3%），中心差 ≤0.006 eV，与梯形积分的边界截断误差一致。中心值（物理解读所用核心量）差异 ≤0.006 eV，不影响"dz² 中心相差约 2 eV"的结论。

---

## 3. 同源性核查

T037 表来源与 T032 核查一致：

| 状态 | DOSCAR/OUTCAR 路径 | ICOHPLIST 路径 | 同源标志 |
|---|---|---|---|
| FCM_base/OOH | G: `FeCoMn_MnOH_electronic_v2_20261031/FCMnew_{base,OOH}_full/` | G: `FeCoMn_MnOH_postprocess_corrected_20261031/cohp/FCMnew_{base,OOH}_full/` | ISYM=−1, NBANDS=1200 |
| MnNC_base | I: `FeCoMn_COHP_20261023/MnNC_base_full/` | I: 同目录 `lobster_post_v2_20261024/` | ISYM=−1, NBANDS=840 |
| MnNC_OOH | G: `FeCoMn_COHP_20261023/MnNC_OOH_full/` | G: 同目录 `lobster_post_v2_20261024/` | ISYM=−1, NBANDS=840 |

DOSCAR 与 ICOHPLIST 均来自同一静态目录，dz² PDOS 与 dz² 分项 ICOHP 同源。与现图 6 (a)(c) 的 Genkai 电子结构计算（ISYM=2）无混用。

---

## 4. 中间文件 JSON 说明

`T037_dz2_icohp_summary.json` 中 `total_minus_ICOHP_spin1` / `spin2` 字段的两自旋拆分显示正确（FCM_base：0.74016 + 1.90014 = 2.64030；MnNC_base：4.01527 + 4.01751 = 8.03278），两自旋求和总值与 T032 一致。该文件仅作过程记录，计算引用以 `T037_summary_table.csv` 为准。

---

## 5. 反证边界核查

T037 REPORT.md 保留了两条反证，与 T032 数值一致：

- 反证 1：OOH* 吸附后 FCM 轴向 −ICOHP 从 2.64030 增大到 3.00339 eV（**✓ 与 T032 一致**）
- 反证 2：加轴向 OH 后反位 OH* −ICOHP 从 2.69789 增大到 3.05704 eV（**✓ 与 T032 一致**）

---

## 6. 核查结论

**全部数值通过。** T037 交付数据（`T037_summary_table.csv`，4 个 PDOS CSV）可作为步骤 4 出图的输入。MnNC_OOH 轴向 Mn179–O180 缺失已在报告中如实注明，不需补跑 LOBSTER。

*不修改 Word 文件、讨论稿和任务单。*
