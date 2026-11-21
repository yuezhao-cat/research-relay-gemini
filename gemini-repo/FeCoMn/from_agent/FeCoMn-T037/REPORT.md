# T037 阶段一交付报告：COHP 同源静态下 Mn d_z² PDOS、分项 -ICOHP 与局域磁矩提取

- **读取任务单**：`FeCoMn/to_agent/FeCoMn-T037_Figure6_dz2_mechanism.md`（提交 `2ce99c6` / `f5aea13`）
- **执行方**：Antigravity　**核查方**：Claude Code（待复核 `FeCoMn/review/T037_ClaudeCode.md`）
- **执行范围**：严格按任务单执行步骤 **1–3、5**；**步骤 4（出图草稿）暂缓**，待用户看完本报告数据后再决定；未跑新 DFT，未跑 LOBSTER，未改 Word。

---

## 1. 数据来源与同源性核对（全部来自 COHP 专用静态）

| 状态 | 体系与背景 | `DOSCAR` / `OUTCAR` 路径（原始静态） | `ICOHPLIST.lobster` 路径 | 同源性 | `ISYM` | `NBANDS` | 体系总磁矩 ($\mu_{\text{B}}$) | Mn 局域磁矩 ($\mu_{\text{B}}$) |
|---|---|---|---|---|---|---|---|---|
| **FCM_base** | `FeCoMn–NC` (`8O* + Mn–OH`) | G:`FeCoMn_MnOH_electronic_v2_20261031/FCMnew_base_full/` | G:`FeCoMn_MnOH_postprocess_corrected_20261031/cohp/FCMnew_base_full/ICOHPLIST.lobster` | **完全同源**（COHP 目录 `OUTCAR`/`WAVECAR` 软链接同一静态） | `-1` | `1200` | `141.310` | **`+3.206`** |
| **FCM_OOH** | `FeCoMn–NC` (`8O* + Mn–OH + OOH*`) | G:`FeCoMn_MnOH_electronic_v2_20261031/FCMnew_OOH_full/` | G:`FeCoMn_MnOH_postprocess_corrected_20261031/cohp/FCMnew_OOH_full/ICOHPLIST.lobster` | **完全同源**（软链接同一静态） | `-1` | `1200` | `138.046` | **`+2.384`** |
| **MnNC_base** | `Mn–NC` (`Mn=O`) | I:`FeCoMn_COHP_20261023/MnNC_base_full/` | I:`FeCoMn_COHP_20261023/MnNC_base_full/lobster_post_v2_20261024/ICOHPLIST.lobster` | **完全同源**（`LORBIT=11` `DOSCAR` 与 LOBSTER 同源） | `-1` | `840` | `0.000` | **`+0.001`** |
| **MnNC_OOH** | `Mn–NC` (`Mn=O + OOH*`) | G:`FeCoMn_COHP_20261023/MnNC_OOH_full/` | G:`FeCoMn_COHP_20261023/MnNC_OOH_full/lobster_post_v2_20261024/ICOHPLIST.lobster` | **完全同源**（`LORBIT=11` `DOSCAR` 与 LOBSTER 同源） | `-1` | `840` | `0.204` | **`+0.256`** |

- 注：`G` = `/home/pj25000114/ku50002299/`，`I` = `/home/05926/zhaoyue/WORK/`。
- **与现图 6 `(a)(c)` 的来源区隔**：现图 6 `(a)(c)` 的 `Mn–NC` 背景 PDOS 与磁矩（`+0.287 μB`，`3d` 中心 `-3.442 eV`）沿用 Genkai `FeCoMn_electronic_20261023/MnNC_base_full`（`ISYM=2`）；本表新增的 `dz²` PDOS 与 `dz²` 分项 `-ICOHP` **严格全部来自上表 COHP 专用静态**，两者绝不混入同一面板。

---

## 2. 核心提取数值汇总（不平滑积分，原始 `DOSCAR` 网格梯形积分 & `ICOHPLIST` 两自旋直接求和取负）

### 2.1 `Mn dz²` 投影 PDOS 统计（`-8.0 ~ 0.0 eV` 占据态窗口）

| 状态 | `Mn` 原子索引 | `dz²` 占据态权重 | `dz²` 自旋权重差 ($\uparrow - \downarrow$) | `dz²` 占据态中心 (eV) | 总 `3d` 占据态中心 (eV，同源静态) | 自旋分辨曲线 CSV（`-8.2 ~ 1.2 eV`） |
|---|---|---:|---:|---:|---:|---|
| **FCM_base** | `Mn238` | `0.99490` | `+0.51915` | **`−3.16660`** | `−3.41630` | `data/FCM_base_Mn_dz2_PDOS.csv` |
| **MnNC_base** | `Mn179` | `0.87058` | `+0.00007` | **`−5.12139`** | `−3.54206` | `data/MnNC_base_Mn_dz2_PDOS.csv` |
| **FCM_OOH** | `Mn238` | `0.74427` | `+0.10610` | **`−4.84117`** | `−3.40121` | `data/FCM_OOH_Mn_dz2_PDOS.csv` |
| **MnNC_OOH** | `Mn179` | `0.75484` | `+0.00527` | **`−4.95444`** | `−2.95262` | `data/MnNC_OOH_Mn_dz2_PDOS.csv` |

### 2.2 轴向键与反位 `Mn–OOH*` 键总 `-ICOHP` 及 `dz²` 分项（单位：eV）

| 状态 | 键类型与编号 | 键长 (Å) | 总 `-ICOHP` | `Mn dz²` 对该 O 全轨道 `-ICOHP` 和 | 其中 `Mn dz² – O 2pz` | 其中 `Mn dz² – O 2s` |
|---|---|---:|---:|---:|---:|---:|
| **FCM_base** | 轴向 `Mn238–O247` | `1.87724` | **`2.64030`** | **`0.99516`** | **`0.76992`** | `0.21944` |
| **MnNC_base** | 轴向 `Mn179–O180` | `1.57708` | **`8.03278`** | **`2.97544`** | **`2.32192`** | `0.65400` |
| **FCM_OOH** | 轴向 `Mn238–O247` | `1.87283` | **`3.00339`** | **`1.51226`** | **`1.17626`** | `0.33519` |
| **FCM_OOH** | 反位 `Mn238–O248` | `1.89484` | **`3.11766`** | **`1.38304`** | **`1.07753`** | `0.30121` |
| **MnNC_OOH** | 轴向 `Mn179–O180` | — | `N/A`（现有 `lobsterin` 未投影该键） | `N/A` | `N/A` | `N/A` |
| **MnNC_OOH** | 反位 `Mn179–O181` | `1.93616` | **`2.65218`** | **`1.06276`** | **`0.75846`** | `0.26095` |

- 说明：`MnNC_OOH_full/lobster_post_v2_20261024/lobsterin` 仅设置了 `cohpbetween atom 179 and atom 181 orbitalwise`，未输出轴向 `Mn179–O180`；按本任务单要求不重跑 LOBSTER，如实记为 `N/A`。

---

## 3. 物理图景与必须保留的反证边界

1. **为什么总 `3d` 中心相近，而反位 `Mn–OOH*` 结合更强**：
   - 吸附前两者的总 `3d` 占据态中心相近（`FCM`: `−3.42 eV`, `MnNC`: `−3.54 eV` 同源 / `−3.44 eV` Genkai），但 **`Mn dz²` 中心相差近 `2.0 eV`**（`FCM`: **`−3.17 eV`**，高能且明显自旋极化；`MnNC`: **`−5.12 eV`**，受强 `Mn=O` 键推深）。
   - 在 `Mn–OOH*` 态下，两者反位键的总 `-ICOHP`（`3.12` vs `2.65 eV`，差 `0.47 eV`）和 `Mn dz² – O 2pz` 分项（`1.08` vs `0.76 eV`，差 `0.32 eV`）清晰表明：**`FeCoMn–NC` 的 `Mn dz²` 轨道能级更高、未受强 `Mn=O` 束缚，因此能与反位 `OOH*` 的 `O 2pz` 形成更强的 `dz²–pz` $\sigma$ 键**。
2. **必须保留的反证边界（严禁写“竞争”或“轴向键被削弱”）**：
   - 反证 1：`OOH*` 吸附后，`FeCoMn–NC` 轴向 `Mn238–O247` 总 `-ICOHP` 反而从 `2.64030 eV` **增大**到 `3.00339 eV`（`dz²` 分项从 `0.995` 增至 `1.512 eV`），未发生削弱。
   - 反证 2：`FeCoMn–NC` 在同一 `8O*` 颗粒背景下加入轴向 `OH` 后，反位 `OH*` 的 `-ICOHP` 从 `2.69789` **增大**到 `3.05704 eV`。

---

## 4. 交付数据文件清单（`FeCoMn/from_agent/FeCoMn-T037/data/`）

- `T037_summary_table.csv`（总表：含全部数值、中心、磁矩、`ISYM`/`NBANDS`）
- `T037_dz2_icohp_summary.json`（含原始真实路径与 `dz²` 逐轨道分解明细）
- `FCM_base_Mn_dz2_PDOS.csv`、`MnNC_base_Mn_dz2_PDOS.csv`、`FCM_OOH_Mn_dz2_PDOS.csv`、`MnNC_OOH_Mn_dz2_PDOS.csv`（`-8.2 ~ 1.2 eV` 自旋分辨 `dz²` 与总 `3d` 原始 PDOS）


---

## 5. 步骤 4 出图草稿（`draft_20261119_v1/`，2026-11-19）

严格保持图 6 定稿（v38）的 `3×3` 布局、配色、尺寸（`177.8 × 179.0 mm`）与 `8 pt Arial` 排版，仅作最小化机理补充：

- **面板 (a)**：保留原 Genkai 链总 `3d` PDOS 与 $\varepsilon_{\text{d}}$（`−3.42 / −2.39 / −3.44 eV`）不动；在顶部新增与 `(d)` 对称的 `metal 3d  — Mn dz²` 图例；叠加同源 COHP 静态的 `Mn dz²` 曲线（深灰实线，与对应总 `3d` 同比例缩放）并标出 $\varepsilon_{\text{d}_{z^2}}$（`FeCoMn–NC` `−3.17 eV` vs `Mn–NC` `−5.12 eV`，黑色点线）。（注：`Mn–NC` 行总 `3d` 来自 Genkai `ISYM=2` 静态、`dz²` 来自 IMR COHP `ISYM=-1` 静态，图注中应予注明）。
- **面板 (b)**：在轴向键总 `−ICOHP`（`2.64`、`8.03`）下方标注 `dz²` 分项（`dz² 1.00`、`dz² 2.98`）。
- **面板 (e)**：在 `OOH*` 列左下角总 `−ICOHP` 旁标注 `dz²` 分项：`3.12 (dz² 1.38)` 与 `2.65 (dz² 1.06)`；`OH*` 列及 `(c)(d)(f)(g)(h)(i)` 保持 v38 原貌不变。

导出文件：
- `draft_20261119_v1/Figure6_T037_preview.png`（300 dpi 预览）
- `draft_20261119_v1/Figure6_T037_600dpi.png`（600 dpi 印刷版）
- `draft_20261119_v1/Figure6_T037.pdf`、`Figure6_T037_editable.svg`
- 脚本：`build_t037_draft.py`


---

## 6. 步骤 4 出图草稿 v2（采用乙方案，`draft_20261119_v2/`，2026-11-19）

按用户与审阅意见完成三项改进（推荐 **乙方案**）：
1. **面板 `(a)` 同源性修正（乙方案）**：`Mn–NC` 行的总 `3d` PDOS 与 $\varepsilon_{\text{d}}$ 同步切换为 COHP 专用静态数据（$\varepsilon_{\text{d}} = -3.54\text{ eV}$），确保 `(a)` 中 `FeCoMn–NC`（`-3.42` / `-3.17 eV`）与 `Mn–NC`（`-3.54` / `-5.12 eV`）各自的 `3d` 与 `dz²` **100% 来自同一波函数**（`FeCo–NC` 为 `-2.39 eV` 不变）。
2. **`dz²` 曲线单独归一化并采用深色同色系**：`FeCoMn–NC` 用深砖红 `#8b1e34`、`Mn–NC` 用深棕橙 `#9c4328`（线宽 `1.15 pt`），独立归一化至行高 `0.85`，使 `dz²` 分布差异一目了然。
3. **区分两种竖线与图例**：$\varepsilon_{\text{d}}$ 沿用虚线（`--`），$\varepsilon_{\text{d}_{z^2}}$ 采用对应深色同色系点线（`··`）；顶部图例标明 `metal 3d (εd --)` 与 `Mn dz² (εdz² ··)`。

导出文件：
- `draft_20261119_v2/Figure6_T037_v2_preview.png`（300 dpi 预览）
- `draft_20261119_v2/Figure6_T037_v2_600dpi.png`（600 dpi 印刷版）
- `draft_20261119_v2/Figure6_T037_v2.pdf`、`Figure6_T037_v2_editable.svg`
- 脚本：`build_t037_draft_v2.py`
