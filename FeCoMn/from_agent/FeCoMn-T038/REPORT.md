# T038 交付报告：无轴向配体状态下颗粒对相邻 Mn 电子结构的作用

**主查/独立复核方**：Antigravity　**日期**：2026-11-19  
**执行范围**：仅检查并后处理超算已有 DFT 输出；未提交任何新 DFT/优化；未修改 Word 与正文图表。

---

## 0. 对旧版初稿（`6e87500`）的独立复核结论

经穷尽检索 Genkai 与 IMR 全部 `FeCoMn*` 目录，独立复核结论如下：

1. **A（`FCM clean`）与 B（`MnNC clean`）缺失原因确认无误**：两套目录均仅有 `NSW=400` 几何优化，未设 `LORBIT=11` 与 `LAECHG=.TRUE.`，且无颗粒/载体切分静态；全盘无其他 `C174 N4 Fe27 Co32 Mn1` 或 `C174 N4 Mn1` 的无配体静态输出。（注：`20261014` 的 `Near_clean_full` / `Far_clean_full` 组成为 `C174 N4 Fe27 Co32 Mn1 O1 H1`，为颗粒无 O* 而 Mn 带轴向 OH；`MnNC_base_full` 组成为 `C174 N4 Mn1 O1`，为 Mn=O。）
2. **补正旧版遗漏的三项已有关键数据（不需跑新 DFT 即已存在）**：
   - **遗漏 1**：**C 的 MnNC 纯载体切分静态已存在**，位于 IMR `FeCoMn_electronic_20261023/FCM_base_support`（`C 174 N 4 Mn 1`，`ISYM=0, LORBIT=11, LAECHG=.TRUE.`，完整收敛），此前误判为“不存在”。
   - **遗漏 2**：**C 的三片段差分电荷已算完**，位于 IMR `FeCoMn_electronic_20261023/cdd_remaining_20261024_cs001/FCM_interface/`（`FCM_base_full − FCM_base_particle − FCM_base_support`，含 `CHGDIFF.vasp`、`planar_charge_difference.csv`、`validation.json`），此前误判为“不可算”。
   - **遗漏 3**：**C 的 Bader 已在 Genkai 算完**（`FCM_base_full/bader_20261023/ACF.dat` 与 `bader_format_test_v2_20261024/ACF.dat`）；同时基于 IMR `FCM_base_support` 已有 `AECCAR0/2+CHGCAR` 已在 `/tmp` 完成 `bader` 后处理对比（未动原工作目录）。

因此，虽然 A 与独立弛豫态 B 仍缺静态电子结构，但 **C（`FCM 8O*`，Mn 无轴向配体）vs `C_support`（同几何去除颗粒的纯 `Mn–NC` 载体）** 已构成严格同几何单变量对照，可以直接定量回答颗粒在无轴向配体时对相邻 `Mn` 的电子作用。

---

## 1. 全量数据可用性盘点

| 标号 | 对象 | 机器与路径 | 计算类型 / 设置 | `LORBIT=11` | `LAECHG` | PDOS | Bader | Δρ 切分 | 总能量 (eV) | 总磁矩 (μB) | Mn 局域磁矩 (μB) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A** | `FCM clean` | IMR `FeCoMn_ch5_recalc_20261007/S_FeCoMnNC59_clean` | 优化 `NSW=400, ISYM=0` | 否 | 否 | 否 | 否 | 无片段 | −2066.6639 | 139.1098 | 无 |
| **B** | `MnNC clean` | IMR `FeCoMn_ch5_recalc_20261007/MnNC_clean` | 优化 `NSW=400, ISYM=0` | 否 | 否 | 否 | 否 | 无 | −1661.2567 | 3.0306 | 无 |
| **C** | `FCM 8O*`（Mn 无轴向） | Genkai `FeCoMn_electronic_20261023/FCM_base_full` | 静态 `ISYM=0, ENCUT=500` | **是** | **是** | **有** | **有** | **完整三片段** | −2129.3728 | 140.9068 | **+3.116** |
| **C_support** | `Mn–NC` 载体（同 C 几何） | IMR `FeCoMn_electronic_20261023/FCM_base_support` | 静态 `ISYM=0, ENCUT=500` | **是** | **是** | **有** | **有** | **完整三片段** | −1661.0718 | 3.0524 | **+3.126** |
| **C_particle** | `FeCo+8O*` 颗粒（同 C 几何） | Genkai `FeCoMn_electronic_20261023/FCM_base_particle` | 静态 `ISYM=0, ENCUT=500` | 是 | 是 | 有 | — | **完整三片段** | −464.1161 | 139.8634 | — |

说明：A、B、C、C_support 的 `Mn–N` 平均键长分别为 `1.9140`、`1.9154`、`1.9143`、`1.9143 Å`；在 C 中，颗粒最近原子（`Fe185`）距 `Mn238` 为 **`10.130 Å`**。

---

## 2. Bader 电子数与 Mn 局域磁矩对比（C vs C_support）

| 电子结构量 | **C_support**（无颗粒纯 `Mn–NC`） | **C**（`FCM 8O*`，Mn 无轴向） | 差值 Δ（C − C_support） | 数据来源 |
|---|---:|---:|---:|---|
| 体系总电子数（Bader 校验） | 729.0000 | 1281.0000 | — | `VACUUM CHARGE = 0.0000` |
| **Mn Bader 电子数 (e)** | **11.6258** (`11.625768`) | **11.6319** (`11.631851`) | **+0.0061** (`+0.006083`) | `ACF.dat`（ZVAL=13） |
| **N175 Bader (e)** | 6.2841 | 6.2846 | +0.0005 | `ACF.dat` |
| **N176 Bader (e)** | 6.2852 | 6.2872 | +0.0019 | `ACF.dat` |
| **N177 Bader (e)** | 6.3327 | 6.3319 | −0.0008 | `ACF.dat` |
| **N178 Bader (e)** | 6.3324 | 6.3337 | +0.0013 | `ACF.dat` |
| **4N Bader 总和 (e)** | **25.2344** (`25.234449`) | **25.2373** (`25.237300`) | **+0.0029** (`+0.002851`) | `ACF.dat` |
| **Mn + 4N Bader 总和 (e)** | **36.8602** | **36.8692** | **+0.0089** | `ACF.dat` |
| **Mn 局域磁矩 tot / d (μB)** | **+3.126** / 3.033 | **+3.116** / 3.024 | **−0.010** / −0.009 | `OUTCAR magnetization (x)` |

---

## 3. 差分电荷密度 Δρ（`FCM_interface` = `FCM_base_full − FCM_base_particle − FCM_base_support`）

- 原始目录：IMR `/home/05926/zhaoyue/WORK/FeCoMn_electronic_20261023/cdd_remaining_20261024_cs001/FCM_interface/`
- 网格验证：`[252, 240, 360]`（`max_coordinate_error_fractional = 0.0`，全晶胞净电荷守恒残差 `1.63 × 10⁻⁷ e`）
- 三片段结合能：$E_{\text{bind}} = -2129.3728 - (-464.1161 - 1661.0718) = -4.1849\ \text{eV}$

### 3.1 `Mn–N4` 局域三维空间积分 Δq（由 `CHGDIFF.vasp` 直接积分）

| 积分区域 | Δq (e) | 说明 |
|---|---:|---|
| `Mn` 球积分 $r \le 1.2\ \text{Å}$ | **+0.0028** | `+0.002788 e` |
| `Mn` 球积分 $r \le 1.5\ \text{Å}$ | **+0.0030** | `+0.003002 e` |
| `Mn` 球积分 $r \le 2.0\ \text{Å}$ | **+0.0034** | `+0.003354 e` |
| `Mn` 球积分 $r \le 2.5\ \text{Å}$ | **+0.0029** | `+0.002863 e` |
| `Mn` 球积分 $r \le 3.0\ \text{Å}$ | **+0.0011** | `+0.001101 e` |
| `Mn (r ≤ 1.8 Å) ∪ 4N (r ≤ 1.5 Å)` 并集 | **+0.0027** | `+0.002711 e` |

### 3.2 平面平均差分电荷曲线 Δρ(z) 与沿 z 轴积分（`FCM_8O_interface_planar_cdd.csv`）

- 碳氮基底位于 $z \approx 6.06\ \text{Å}$（`z_Mn = 6.0645 Å`，`z_4N_mean = 6.0741 Å`），颗粒最近原子位于 $z = 12.1653\ \text{Å}$。
- 按整层截面（含颗粒正下方碳载体界面区）对 `z` 积分：
  - `z_Mn ± 1.0 Å` (`5.07–7.07 Å`)：`-0.0118 e`（碳片层内部极化再分配）
  - `z_Mn ± 1.5 Å` (`4.53–7.53 Å`)：`+0.1640 e`（主要包含颗粒正下方界面碳区域向上凸起/成键极化区域）
  - `z_Mn ± 2.0 Å` (`4.07–8.07 Å`)：`-0.0035 e`（跨碳层与近界面过渡层净值接近中性）
  - `z = 8.07–16.00 Å`：净积分 `+0.000004 e`（整个颗粒+界面偶极过渡区总净电荷守恒为零）
- 完整 360 点 `planar_charge_difference.csv` 已保存在本目录 `FCM_8O_interface_planar_cdd.csv`。

---

## 4. Mn `3d` 与 `dz²` 占有态中心（`−8 ~ 0 eV` vs $E_F$）

PDOS 原始曲线已提取保存至 `FCM_8O_Mn_pdos.csv`（`FCM_base_full` `Mn238`）与 `FCM_base_support_Mn_pdos.csv`（`FCM_base_support` `Mn179`）。

| 轨道 / 指标 | **C_support**（无颗粒纯 `Mn–NC`） | **C**（`FCM 8O*`，Mn 无轴向） | 差值 Δ（C − C_support） |
|---|---:|---:|---:|
| $E_F$ (eV) | −2.9965 | −2.2044 | +0.7920 |
| **Mn `dz²` 占有态中心 (eV)** | **−3.0450** | **−3.0135** | **+0.0315** |
| **Mn 总 `3d` 占有态中心 (eV)** | **−3.1147** | **−3.0830** | **+0.0317** |
| `dz²` 占有态权重 (`−8 ~ 0 eV`) | 0.8817 | 0.8865 | +0.0048 |
| 总 `3d` 占有态权重 (`−8 ~ 0 eV`) | 4.7907 | 4.7925 | +0.0018 |
| `dz²` 自旋净差（↑ − ↓） | 0.7898 | 0.7929 | +0.0031 |

---

## 5. 汇总判断（只陈述数值，不写推测性机理）

1. **颗粒是否使相邻 Mn 得电子、dz² 是否上移（基于已有完整同几何对照 `C` vs `C_support`）**：
   - **Mn 得电子**：Bader 电荷显示 Mn 得电子 **`+0.0061 e`**，4 个 N 合计得电子 **`+0.0029 e`**；`CHGDIFF.vasp` 三维体积积分显示 Mn 周围得电子 **`+0.0028 ~ +0.0034 e`**、`Mn+4N` 区域得电子 **`+0.0027 e`**。方向为**微弱得电子**，但幅度不足 `0.01 e`。
   - **dz² 上移**：`dz²` 占有态中心由 `−3.0450 eV` 上移至 `−3.0135 eV`（**`+0.0315 eV`**）；总 `3d` 中心由 `−3.1147 eV` 上移至 `−3.0830 eV`（**`+0.0317 eV`**）；Mn 局域磁矩几乎不变（`3.126 → 3.116 μB`）。
2. **数值与“OH 比 O 更稳定”方向一致性**：
   - 得电子与 `dz²` 上移的**代数符号（正向）**与“d/dz² 升高、削弱强双键配体或更利于 OH”的方向一致；
   - 但从**量级**上看，当 FeCo 颗粒距离 Mn `10.130 Å` 且颗粒带 `8O*` 时，无轴向配体状态下颗粒直接引起的 Mn 静态电荷转移（`< 0.01 e`）和 `dz²` 偏移（`+0.032 eV`）非常微弱；先前带轴向配体态下 `FCM(OH)` 与 `MnNC(O)` 之间 `~2 eV` 的 `dz²` 差距和 `~3 μB` 的磁矩差距主要发生在带轴向配体之后（无配体的 `Mn–NC` 载体本身即处于 `3.126 μB`、`dz² = −3.045 eV` 状态）。
3. **如若仍需补齐 A（干净无 `8O*` 颗粒）与独立弛豫态 B，建议的最小静态单点清单**：
   - ① `S_FeCoMnNC59_clean`（A）静态单点（`NSW=0, LORBIT=11, LAECHG=.TRUE.`）；
   - ② `MnNC_clean`（B）静态单点（同上，用于检验独立弛豫态是否与同几何 `FCM_base_support` 一致）；
   - ③ A 的几何切分颗粒单独静态 + ④ A 的几何切分载体单独静态（若需在无 `8O*` 状态下计算 A 的 $\Delta\rho$；`C` 的 Bader 与 $\Delta\rho$ 已完整存在，**无需补算**）。

---

## 6. 交付文件与原始路径索引

- 本目录交付：
  - [REPORT.md](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T038/REPORT.md)
  - [T038_available_summary.csv](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T038/data/T038_available_summary.csv)
  - [T038_bader_cdd_pdos.json](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T038/data/T038_bader_cdd_pdos.json)
  - [FCM_8O_Mn_pdos.csv](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T038/FCM_8O_Mn_pdos.csv)
  - [FCM_base_support_Mn_pdos.csv](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T038/FCM_base_support_Mn_pdos.csv)
  - [FCM_8O_interface_planar_cdd.csv](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T038/FCM_8O_interface_planar_cdd.csv)
  - [FCM_8O_interface_cdd_validation.json](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T038/FCM_8O_interface_cdd_validation.json)
- 远端原始路径：
  - A (`FCM clean`): `imr:/home/05926/zhaoyue/WORK/FeCoMn_ch5_recalc_20261007/S_FeCoMnNC59_clean`
  - B (`MnNC clean`): `imr:/home/05926/zhaoyue/WORK/FeCoMn_ch5_recalc_20261007/MnNC_clean`
  - C (`FCM 8O*`): `genkai:/home/pj25000114/ku50002299/FeCoMn_electronic_20261023/FCM_base_full`
  - C 切分颗粒: `genkai:/home/pj25000114/ku50002299/FeCoMn_electronic_20261023/FCM_base_particle`
  - C 切分载体: `imr:/home/05926/zhaoyue/WORK/FeCoMn_electronic_20261023/FCM_base_support`
  - C 差分电荷: `imr:/home/05926/zhaoyue/WORK/FeCoMn_electronic_20261023/cdd_remaining_20261024_cs001/FCM_interface/`
