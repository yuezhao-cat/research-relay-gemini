# FeCoMn-T033 来源追溯与曲线复核报告（Antigravity，2026-11-18）

**所读提交号**：`0bd9cd5`（含 Codex `a875f06` 追溯报告与 Claude `0bd9cd5` T033 补充指令）
**复核结论**：**通过**。

## 1. 独立复读核查结果
1. **为什么当时有两套静态（已查清）**：
   - 本地原脚本 `D:/_pf/ch5_electronic_20261023/prepare_cohp_inputs.py` 证实：当时是为了满足 LOBSTER 完整基组（`Mn_pv 3p 3d 4s` 共 725 个基函数，大于默认 `NBANDS=460`）专门准备了 `ISYM=-1, NBANDS=840` 的 COHP 专用静态（IMR `FeCoMn_COHP_20261023/MnNC_base_full`），并非设错参数；其 `POSCAR`、`POTCAR`、`KPOINTS` 与 Genkai 主静态逐字节 SHA256 完全一致。
2. **新提取的 `MnNC` 轴向键 `−pCOHP` 曲线复核通过**：
   - 我此前引用的 `cohp_curves_20261024/MnNC_base_full__Mn179-O180.csv` 确系 10 月 24 日初版脚本错移 Average 列的废弃文件（已于 `Fig6_Antigravity.md` 中更正替换为新路径）。
   - 独立复核 Codex 从原始 `COHPCAR.lobster` 提取的 `FeCoMn/from_agent/FeCoMn-T033/MnNC_source_trace_20261118/MnNC_axial_COHP_raw_verified_20261118.csv`：共 501 个能量点，在 $E - E_{\text{F}} = 0.0\text{ eV}$ 处 `pCOHP_spin1 = 1.27519`、`pCOHP_spin2 = 1.26675`、`minus_pCOHP_spin_sum = -2.54194`、网格累计积分 `8.06724 eV`（与 `ICOHPLIST.lobster` 原始积分 `8.03278 eV` 完全对应）。
3. **对 `0bd9cd5`（在 IMR `MnNC_base_full` 专用静态上补做 Bader 后处理以实现 a、b 完全同源）的前提确认**：
   - 该 IMR 专用静态（`-1667.77216576 eV`，$\mu_{\text{Mn}} = +0.001\ \mu_{\text{B}}$）包含 `LORBIT=11` 的完整投影 `DOSCAR`，已从中直接算出同源占据态 $\varepsilon_{\text{d}} = -3.542064771\text{ eV}$（`−3.54 eV`），满足 `0bd9cd5` 的前提条件；
   - 同目录 `CHGCAR`、`AECCAR0`、`AECCAR2`（网格 `252×240×360`）齐全，只需在该目录做一次 Bader 后处理（无需跑 VASP），即可让 `Mn–NC` 在面板 a、b 中的轴向 COHP（`8.03 eV`）、Bader 电子数、占据态 $\varepsilon_{\text{d}}$（`−3.54 eV`）和局域磁矩（`0.00 μB`）100% 出自同一波函数。
