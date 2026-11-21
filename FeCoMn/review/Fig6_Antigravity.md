# 图 6 定稿方案面板 a、b 数据路径核查清单（Antigravity，2026-11-18）

**所读提交号**：`0bd9cd5`（含 `a875f06` Codex 追溯报告与新提取曲线核验）
**核查结论**：**面板 a、b 全部 5 项主要数值 100% 交叉复现一致**；`Mn–NC` 轴向键曲线路径已更新为 Codex 从原始 `COHPCAR.lobster` 提取并经我复核通过的 `FeCoMn/from_agent/FeCoMn-T033/MnNC_source_trace_20261118/MnNC_axial_COHP_raw_verified_20261118.csv`（替代此前引用的已停用初版错列 CSV）。

---

## 一、面板 a：吸附前工作表面两根轴向键（`Mn–OH` vs `Mn=O`）

| 指标 | `FeCoMn–NC` 工作表面（`8O* + Mn–OH`，`Mn238–O247`） | `Mn–NC` 工作表面（`Mn=O`，`Mn179=O180`） |
| :--- | :--- | :--- |
| **轴向键长** | **`1.88 Å`**（精确值 `1.87724 Å`） | **`1.58 Å`**（精确值 `1.57708 Å`） |
| **轴向键 `−ICOHP`** | **`2.64 eV`**（精确值 `2.64030 eV` = `0.74016 + 1.90014`） | **`8.03 eV`**（精确值 `8.03278 eV` = `4.01527 + 4.01751`） |
| **`ICOHPLIST` 文件路径** | • 本地：`D:/OneDrive/Desktop/知识库/papers/FeCoMn/ACS_Catalysis_第三轮投稿/电子结构后处理核查_20261031/fig6_data/ICOHPLIST_base.lobster`（`COHP# 26: Mn238–O247`）<br>• Genkai：`/home/pj25000114/ku50002299/FeCoMn_MnOH_postprocess_corrected_20261031/cohp/FCMnew_base_full/ICOHPLIST.lobster` | • IMR：`/home/05926/zhaoyue/WORK/FeCoMn_COHP_20261023/MnNC_base_full/lobster_post_v2_20261024/ICOHPLIST.lobster`（`COHP# 1: Mn179–O180`） |
| **`−pCOHP(E)` 曲线文件路径** | • 本地：`D:/OneDrive/Desktop/知识库/papers/FeCoMn/ACS_Catalysis_第三轮投稿/电子结构后处理核查_20261031/fig6_data/COHPCAR_base.lobster`（第 26 号总键 `Mn238–O247`）<br>• Genkai：`/home/pj25000114/ku50002299/FeCoMn_MnOH_postprocess_corrected_20261031/cohp/FCMnew_base_full/COHPCAR.lobster` | • 仓库已核验完整 501 点 CSV：`FeCoMn/from_agent/FeCoMn-T033/MnNC_source_trace_20261118/MnNC_axial_COHP_raw_verified_20261118.csv`（从原始 `COHPCAR.lobster` 列组 1 提取，勿用旧 `cohp_curves_20261024` 错列文件）<br>• IMR 原始 LOBSTER：`/home/05926/zhaoyue/WORK/FeCoMn_COHP_20261023/MnNC_base_full/lobster_post_v2_20261024/COHPCAR.lobster`（第 1 号总键 `Mn179–O180`） |

---

## 二、面板 b：吸附前两个 Mn 位点的分组柱状图（Bader 电子数、占据态 $\varepsilon_{\text{d}}$、局域磁矩）

| 指标 | `FeCoMn–NC`（`Mn238`） | `Mn–NC`（`Mn179`） | 精确文件路径（经 Codex `79351a0` 交叉验证） |
| :--- | :--- | :--- | :--- |
| **1. Mn Bader 电子数** | **`11.46 e`**（精确值 `11.457649 e`；按 `ZVAL=13` 换算净电荷 `+1.542351 e`） | **`11.51 e`**（精确值 `11.507781 e`；按 `ZVAL=13` 换算净电荷 `+1.492219 e`） | • `FeCoMn–NC`：Genkai `/home/pj25000114/ku50002299/FeCoMn_MnOH_postprocess_20261031/bader/FCMnew_base_full/ACF.dat`（已修正文件夹名为 `postprocess_20261031`）；仓库 `FeCoMn/from_agent/Figure6_mechanism_audit_20261118/supplement_genkai.json`<br>• `Mn–NC`：本地 `D:/_pf/ch5_electronic_20261023/bader_results_v3/genkai.json`（`name: "MnNC_base_full"`, `atoms.index=179`）；Genkai `/home/pj25000114/ku50002299/FeCoMn_electronic_20261023/MnNC_base_full/bader_validated_20261024/ACF.dat` |
| **2. 吸附前 Mn 占据态 $\varepsilon_{\text{d}}$** | **`−3.42 eV`**（表内原始值 `−3.416298530970028 eV`） | **`−3.44 eV`**（表内原始值 `−3.442021812954855 eV`） | • 本地统一表：`D:/OneDrive/Desktop/知识库/papers/FeCoMn/ACS_Catalysis_第三轮投稿/单图汇总_journal_20261025/92_电子结构统一原参考态_20261029/atom_resolved_occupied_d_centers.csv`（`sample=FCM, state=base, atom_1based=238` 与 `sample=MnNC, state=base, atom_1based=179`） |
| **3. Mn 局域磁矩** | **`3.21 μB`**（精确值 `+3.206 μB`） | **`0.29 μB`**（Genkai 主静态 `+0.287 μB`；IMR COHP 静态为 `+0.001 μB`） | • 仓库已收录：`FeCoMn/from_agent/FeCoMn-T031/branch_inventory.csv`（第 51 行 `FCMnew_base_full: 3.206`；第 49 行 Genkai `MnNC_base_full: 0.287`；第 2 行 IMR `MnNC_base_full: 0.001`） |

### 关于 `MnNC_base_full` 两套静态的同源性说明
- `FeCoMn–NC` 的 `FCMnew_base_full` 中，轴向 COHP 与 PDOS/Bader/磁矩来自**完全同一个波函数**（$E_0 = -2140.09673312\text{ eV}$，$\mu_{\text{Mn}} = +3.206\ \mu_{\text{B}}$）。
- `Mn–NC` 的 `MnNC_base_full` 中，坐标 `CONTCAR` 完全相同（`Mn=O` 距离均为 `1.57708 Å`），但 PDOS/Bader 主静态（Genkai `ISYM=0`，`-1667.77945980 eV`，$\mu_{\text{Mn}} = +0.287\ \mu_{\text{B}}$）与 COHP 专用静态（IMR `ISYM=-1, NBANDS=840`，`-1667.77216576 eV`，$\mu_{\text{Mn}} = +0.001\ \mu_{\text{B}}$）能量差 `0.0073 eV`，两者均属于低自旋近零磁矩分支（与 `FeCoMn–NC` 的 `+3.206 μB` 对比悬殊）。在报告与图注中如实记录来源即可。
