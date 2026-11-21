# FeCoMn-T041：OOH* 吸附的几何形变 / 电子结合拆分报告（Antigravity）

日期：2026-11-20  
任务单：`FeCoMn/to_agent/FeCoMn-T041_OOH_distortion_decomposition.md`（提交 `1a950d9`，赵月 2026-11-20 13:37 批准）  
执行：Antigravity（Genkai）；复核：Claude Code。不改图、不改 Word。

---

## 1. 新补静态计算（Genkai）

* **作业路径**：`/home/pj25000114/ku50002299/FeCoMn_T041_20261120/FCM_OOH_substrate`
* **Genkai 作业号**：`7633024`（`a-pj25000114`，1 节点 120 核）
* **结构来源**：由既有 `/home/pj25000114/ku50002299/FeCoMn_electronic_20261023/FCM_OOH_full/POSCAR` 删除反应侧 `OOH*`（末尾 247 O、248 O、249 H 三原子，坐标未动），保留 246 原子（`C 174, N 4, Fe 27, Co 32, Mn 1, O 8`）。
* **参数口径**：与 `FCM_OH_substrate`、`FCM_OOH_full` 完全一致（`PREC = Accurate`, `ENCUT = 500`, `EDIFF = 1E-6`, `ISMEAR = 0`, `SIGMA = 0.05`, `IVDW = 12`, `ISPIN = 2`, `LMAXMIX = 4`, `ISYM = 0`, `LREAL = .FALSE.`, `Gamma 1×1×1`, `NGXF/Y/ZF = 252/240/352`），`MAGMOM` 沿用原采用分支（`174*0 4*0 27*3 32*2 1*3 8*0.5`），不做自旋扫描。提交前 `preflight_vasp.py --compare` 通过（`FAIL = 0`）。
* **收敛状态**：`Total CPU time used` 正常结束，电子步达到 `EDIFF = 1E-6` 收敛。
* **输出结果**：`energy(sigma->0) = −2129.08855624 eV`，体系总磁矩 `139.3237 μB`，`Mn238` 局域磁矩 `+3.182 μB`。

---

## 2. 原始 `OUTCAR` 能量与几何汇总（Genkai 同口径静态）

| 体系与片段 | Genkai 目录 | `energy(sigma->0)` / eV | `tot_mag` / μB | `Mn` 磁矩 / μB |
|---|---|---:|---:|---:|
| `FCM_base_full` (`8O*`, 无 `OH`) | `FeCoMn_electronic_20261023/FCM_base_full` | `-2129.34174525` | `140.9070` | `+3.116` |
| `FCM_OOH_full` (`noOH + OOH*`) | `FeCoMn_electronic_20261023/FCM_OOH_full` | `-2144.27122470` | `137.1453` | `+2.233` |
| **`FCM_OOH_substrate`**（本任务新算） | `FeCoMn_T041_20261120/FCM_OOH_substrate` | **`-2129.08855624`** | `139.3237` | `+3.182` |
| `FCM_OOH_adsorbate`（`noOH` 终态孤立 `OOH`） | `FeCoMn_electronic_20261023/FCM_OOH_adsorbate` | `-13.00461415` | `1.0000` | — |
| `FCMnew_base_full` (`8O* + 轴向 OH`) | `FeCoMn_MnOH_electronic_v2_20261031/FCMnew_base_full` | `-2140.09673312` | `141.3105` | `+3.206` |
| `FCMnew_OOH_full` (`withOH + OOH*`) | `FeCoMn_MnOH_electronic_v2_20261031/FCMnew_OOH_full` | `-2154.75901952` | `138.0459` | `+2.384` |
| `FCMnew_OOH_substrate` | `FeCoMn_MnOH_electronic_v2_20261031/FCMnew_OOH_substrate` | `-2139.41181770` | `139.4889` | `+3.187` |
| `FCMnew_OOH_adsorbate`（`withOH` 终态孤立 `OOH`） | `FeCoMn_MnOH_electronic_v2_20261031/FCMnew_OOH_adsorbate` | `-13.06940440` | `1.0000` | — |

注：两个孤立 `OOH_adsorbate` 静态能量差 `-0.06479025 eV`（`noOH` 态下 `O–O = 1.4794 Å, O–H = 0.9801 Å`；`withOH` 态下 `O–O = 1.4585 Å, O–H = 0.9783 Å`）。下文同时列出“按各自冻结 `OOH_adsorbate`”与“统一固定 `OOH` 参考态”两种写法，供核查。

---

## 3. `OOH*` 与 `OH*` 能量拆分及 `Mn` 离面高度并列对比表

定义：
- `E_distort(sub) = E(substrate) − E(base_full)`（基底与颗粒几何形变代价）
- `E_bind_frozen = E(full) − E(substrate) − E(adsorbate)`（冻结在吸附终态几何下的界面电子结合能）
- `E_bind(各自 ads) = E(full) − E(base_full) − E(adsorbate) = E_distort(sub) + E_bind_frozen`
- `ΔE_tot(统一 ads 参考) = E(full) − E(base_full)` 相对无 `OH` 组差值（即 `CHE` 同参考态总吸附削弱；其中 `OOH*` 两个 `adsorbate` 内形变差 `ΔΔE_distort(ads) = −0.064790 eV`，`OH*` 两态 `adsorbate` 差仅 `-0.000251 eV`）。

| 中间体 | 背景 | `E_distort(sub)` / eV | `E_bind_frozen` / eV | `E_bind(各自 ads)` / eV | `Mn` 离面高度变化（base → sub） | `Mn` 位移 / Å | `FeCo` 颗粒 rms / Å |
|---|---|---:|---:|---:|---|---:|---:|
| **`OH*`** | 无轴向 `OH` (`noOH`) | `+0.434949` | `-3.638916` | `-3.203967` | `-0.0096 → -0.4562 Å` | `0.4882` | `0.0111` |
| **`OH*`** | 有轴向 `OH` (`withOH`) | `+0.671179` | `-3.539402` | `-2.868224` | `+0.4418 → -0.0093 Å` | `0.4662` | `0.0050` |
| **`OH*` 差值** | **`withOH − noOH`** | **`+0.236229`** | **`+0.099514`** | **`+0.335743`**（同参考 `+0.335994`） | 压回 `N4` 平面 `0.451 Å` | — | — |
| **`OOH*`** | 无轴向 `OH` (`noOH`) | **`+0.253189`** | **`-2.178054`** | `-1.924865` | `-0.0096 → -0.3105 Å` | `0.3194` | `0.0398` |
| **`OOH*`** | 有轴向 `OH` (`withOH`) | **`+0.684915`** | **`-2.277797`** | `-1.592882` | `+0.4418 → +0.0027 Å` | `0.4487` | `0.0387` |
| **`OOH*` 差值** | **`withOH − noOH`** | **`+0.431726`** | **`-0.099743`** | `+0.331983`（同参考 **`+0.267193`**） | 压回 `N4` 平面 `0.439 Å` | — | — |

说明（纯数值陈述）：
1. 对 **`OH*`**：同参考总吸附削弱 `+0.336 eV` = 基底几何形变增量 **`+0.236 eV`（70.4%）** + 冻结几何电子结合减弱 **`+0.100 eV`（29.6%）**（`adsorbate` 差异 `-0.0003 eV`）。
2. 对 **`OOH*`**：同参考总吸附削弱 **`+0.267 eV`**（`E(full)−E(base)` 差值，静态口径）= 基底几何形变增量 **`+0.432 eV`** + 冻结几何电子结合变化 **`-0.100 eV`** + 吸附物自身形变差 **`-0.065 eV`**（即有 `OH` 组 `OOH` `O–O` 拉伸更小，自身内能更低 `0.065 eV`，而电子结合 `E_bind_frozen` 反略强 `0.100 eV`；基底几何形变增量 `+0.432 eV` 大于总削弱 `+0.267 eV`）。
3. 几何对比：`noOH` 下吸附 `OOH*` 时 `Mn` 仅向下偏移到 `-0.3105 Å`（`E_distort = +0.253 eV`），而 `withOH` 下 `Mn` 被轴向 `OH` 预拉出 `+0.4418 Å`，吸附 `OOH*` 时被迫回拉到 `+0.0027 Å`（`Mn` 总位移 `0.4487 Å`，`E_distort = +0.685 eV`）。
