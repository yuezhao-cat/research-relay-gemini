# FeCoMn–NC T017：ORR 原始计算全量核查

日期：2026-11-17。仅读取 IMR Tohoku（`/home/05926/zhaoyue/WORK`）与 Genkai Kyushu（`/home/pj25000114/ku50002299`）已有目录；没有提交、修改或删除远程作业，也没有改图或 Word。

## 检索与覆盖

- Genkai 全目录检索：1835 个含 OUTCAR/OSZICAR 的计算目录，169 个名称与 FeCoMn/FCM/FCN/MnNC 相关的目录进入候选清单，0 个读取错误。
- IMR 全目录检索：353 个候选计算目录（工作区内相关目录均纳入），0 个读取错误。
- 原始清单：`genkai_inventory_raw.json`、`imr_inventory_raw.json`；筛选清单：`*_selected_paths.json`；远程解析结果：`*_parsed.json`。清单保存了完整远程路径和 CONTCAR/INCAR SHA256。
- 本报告的定量 ORR 主表优先采用 S7/S11 对应的、结构组成一致且正常结束并达到离子收敛的 0 V ORR relax；同一结构的 IMR/Genkai 或 Lobster 后处理副本不当作独立构型。

## 现行可比计算

主表采用 SI 表 S11 的最终构型，并用远程原始 OUTCAR 的最后 `energy(sigma->0)` 交叉核对。关键 Genkai 路径的正常结束和离子收敛均为 True：

| 模型 | 背景 | OOH* | O* | OH* |
|---|---:|---:|---:|---:|
| FeCoMn–NC, 8O*+Mn–OH* | −2140.147857 | **S11 −2154.812** | **S11 −2145.476** | **S11 −2150.553** |
| FeCo–NC, 8O* | −2143.215（S11） | −2158.351411 | −2150.084936 | −2154.121223 |
| Mn–NC, Mn=O | −1667.742（S11） | −1681.887464 | −1672.909045 | −1677.546576 |
| FeCoMn–NC, 8O*（无轴向 Mn–OH） | −2129.394（S11） | −2144.264599 | −2135.516288 | −2140.132460 |

注：第一行背景的完整精确值来自同批 `FCM_8O_MnOH` relax（−2140.14785718）；表 S11 采用 −2140.148 的三位小数。重要核查结果：远程目录 `FCM_cov8O_OOH` 的 CONTCAR 是 C174N4Fe27Co32MnO10H（248 原子），最后 sigma→0 为 −2144.264599，**与 S11 的 −2154.812 相差约 10.55 eV，不能当作同一构型**；因此 FCM 的定量自由能仍按 S7/S11 的配对数据报告，并将该原始目录列为不兼容/待追溯，而不是替换或挑选它。表中最后一行是“无轴向”对照，不能与轴向 Mn–OH 背景混用；其余 S11 精确值以 SI 表为准。完整路径和 SHA256 在 `energy_structure_manifest.csv`。

## ORR 自由能计算

严格使用 SI 口径：`G(H2)=−6.833 eV`、`G(H2O)=−14.327 eV`，修正 `O +0.066`、`OH +0.343`、`OOH +0.403 eV`。结果（eV）：

| 模型 | ΔG(OOH*) | ΔG(O*) | ΔG(OH*) | 四步 ΔG（O2→OOH, OOH→O, O→OH, OH→H2O） | PDS | UL | η=1.23−UL |
|---|---:|---:|---:|---|---|---:|---:|
| FeCoMn–NC 8O*+Mn–OH* | 4.144 | 2.232 | 0.849 | −0.776, −1.912, −1.383, −0.849 | O2→OOH* | 0.776 | 0.454 |
| FeCo–NC 8O* | 3.672 | 0.690 | 0.348 | −1.248, −2.981, −0.343, −0.348 | O2→OOH* | 0.343 | 0.887 |
| Mn–NC Mn=O | 4.663 | 2.393 | 1.448 | −0.257, −2.270, −0.944, −1.448 | O2→OOH* | 0.257 | 0.973 |
| FeCoMn–NC 8O*（无轴向） | 3.936 | 1.438 | 0.515 | −0.984, −2.499, −0.922, −0.515 | O2→OOH* | 0.515 | 0.715 |

这些数值与现行 S7 基准一致（四舍五入差异来自 S11 三位小数）。清洁表面的实验顺序为 FeCoMn–NC (0.885 V) > FeCo–NC (0.864 V) > Mn–NC (0.840 V)，与计算中轴向 8O*+Mn–OH*、FeCo–NC、Mn–NC 的趋势并不按同一绝对 UL 排列；因此不能把计算 UL 直接当作实验半波电位的定量替代。

## 结构、收敛和参数审计

- 关键 ORR relax 的 OUTCAR 均有 `energy(sigma->0)`、正常结束标志、`EDIFF is reached` 和离子收敛标志；未采用仅有静态单点或 Lobster 后处理副本替代 relax。
- CONTCAR 原子数与现行 SI 模型一致：FCM 反应态 248、FCN 247、MnNC 180；FCM/FCN 粒子模型固定 15 个内部原子，MnNC 按 SI 为全自由。每个关键目录保留 CONTCAR/INCAR SHA256。
- 现行 S7 设置：VASP 6.6 PAW-PBE、ENCUT 500 eV、Gamma 1×1×1、IVDW12(D3BJ)、ISPIN=2、PREC=Normal、LREAL=Auto、ISMEAR=0/SIGMA=0.05、IBRION=2、ISIF=2、EDIFF=1e−5、EDIFFG=−0.02。关键目录均按此组读取；NCORE=12/14 是机器并行差异，不视为物理方法差异。电子静态 `PREC=Accurate/LREAL=F/EDIFF=1e−6` 目录未与 relax 能量混用。
- 结构审计：CONTCAR 存在且构型名称与 OOH/O/OH 状态对应；未发现关键 ORR 路径目录名称提示 OOH/OH 解离。对粒子是否发生微小重构、Mn 是否保持严格 Mn–N4，报告只把它们标作“需按坐标逐原子复核”，没有用名称臆断为已证明；因此不把不兼容的 partial-coverage、电子结构静态和不同原子数模型纳入主表。
- 全量候选中存在多种 partial-coverage、MnNC 轴向 OH、以及不同初始磁矩/重启分支。它们不与 S7 原子数、背景和固定原子定义兼容，已作为候选记录保留，未挑选替代主结果。MnNC 轴向-OH 旧路径曾得到 UL≈0.570 V；本次只报告其存在，不把它改写成现行结论。

## 交付文件

- `energy_structure_manifest.csv`：关键结果的机器、完整路径、最后 sigma→0 能量、收敛字段、CONTCAR/INCAR SHA256。
- `*_inventory_raw.json`、`*_selected_paths.json`、`*_parsed.json`：两台机器的检索/解析证据。
- `remote_inventory.py`、`remote_parse.py`、`run_inventory.py`、`run_parse.py`、`make_manifest.py`：可复核脚本；均为只读检索和本地整理。
