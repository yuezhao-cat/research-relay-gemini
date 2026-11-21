# IMR GPU + AIMD + AI4Science 长期科研档案与计划

## 1. 档案元信息与协作规则

- **档案定位**：未来 6 个月 IMR GPU + AIMD + AI4Science 工作的唯一统一主档案。
- **双端同步路径**：
  - 本地长期记忆：`D:\AI-Shared-Memory\project_imr_gpu_ai4science_20261121.md`
  - GitHub 私有仓库：`yuezhao-cat/research-relay` 路径 `AI4Science/IMR_GPU_RESEARCH_PLAN.md`
  - 本地长期记忆索引：`D:\AI-Shared-Memory\MEMORY.md`
- **核查日期**：`2026-11-21`（北京时间 `20:00–20:50` 只读实查；IMR `jobtime` 更新时间戳 `2026/11/21 21:02 JST`）
- **最后更新时间**：`2026-11-21`
- **使用期限约束**：预计 IMR 超算剩余可用期限**不超过 6 个月**，且存在提前失去访问权限的风险。
- **状态标注约定**（严格区分四态，禁止混淆）：
  - `已完成`：已执行完毕并取得输出/结果。
  - `正在运行`：当前仍在队列运行或排队中（仅代表核查瞬间快照，非永久状态）。
  - `待执行`：已规划或已建目录但尚未提交/运行。
  - `未确认`：暂无直接实测或文件输出予以确认。
  - （对历史崩溃或墙时截断的任务，标明`未完成/已中断`或`失败`。）
- **证据来源分级约定**：
  - `[真实文件/实测命令核实]`：本次直接读取本地文件、GitHub 仓库、Genkai/IMR 原始文件或直接执行只读命令（`qstat`、`pbsnodes`、`qmgr`、`lfs quota`、`jobtime`、`ls`、`OUTCAR/OSZICAR` 解析）取得。
  - `[此前会话汇报，待落盘复核]`：来自共享记忆/日常流水（如 `daily/2026-11-21.md`）中此前会话的口头或屏幕汇报，因交互未落盘而尚未拿到持久化文本输出。
- **后续协作维护铁律**：
  1. 后续任何智能体开展 IMR GPU、MACE 或 ML-MD 相关任务前，**必须先读取本档案**。
  2. 后续完成 GPU 硬件测试、轨迹清洗、MACE 微调或 ML-MD 计算后，**直接在本地记忆与 GitHub 仓库原地更新本档案**并在第 7 节变更日志追加日期记录，禁止反复创建新版本文档或重复档案。

---

## 2. IMR GPU 资源核查（账户 `05926`）

### 2.1 队列、物理 GPU 与限制总表

> 说明：以下所有队列配置、物理节点数、单机规格与限额均来自 `qstat -Qf`、`pbsnodes -a` 与 `qstat -Bf`/`qmgr -c "p s"` 实测输出 `[真实文件/实测命令核实]`。

| 队列 | 物理 GPU（去重计数） | 对应物理节点与单机规格 | 单作业限制 | 时限 | 权限与分配方式 |
|---|---:|---|---|---|---|
| `CA_001` | 48 | 6 台节点（`cgpu001–cgpu006`，每台 8 GPU / 112 CPU / 920 GB） | 最多 4 GPU / 56 CPU / 460 GB / 1 节点（`min ngpus=1`，默认 1 GPU / 1 CPU / 8 GB） | 72 h（默认 24 h） | `acl_user_enable=False`，`pack:shared` |
| `DA_002` | 与 `CA_001` 共用（不重复计） | 同 `CA_001` 6 台节点（`cgpu001–cgpu006`） | 最多 4 GPU / 4 CPU / 32 GB / 2 节点（每用户 `max_run=2`, `max_queued=10`） | 2 h | `acl_user_enable=False`，`scatter:shared` |
| `A_002` | 40 | 5 台节点（`cgpu007–cgpu011`，每台 8 GPU / 112 CPU / 920 GB） | 最多 16 GPU / 224 CPU / 1840 GB / 2 节点，整节点分配 | 24 h | `acl_user_enable=False`，`free:excl`（默认整台 8 GPU / 112 CPU / 920 GB） |
| `A_001` | 16 | 2 台节点（`cgpu012–cgpu013`，每台 8 GPU / 112 CPU / 920 GB） | 最多 8 GPU / 112 CPU / 920 GB / 1 节点，整节点分配 | 24 h | `acl_user_enable=False`，`free:excl`（尚未实测提交） |
| `IA_001` | 2 | 2 台交互节点（`gpu1–gpu2`，每台 1 GPU / 64 CPU / 110 GB） | 单卡交互申请，最多 4 CPU / 8 GB / 1 节点（每用户 `max_run=1`, `max_queued=1`） | 8 h（默认 1 h） | `acl_user_enable=False`，`pack:shared` |

### 2.2 平台总量去重、账户全局配额与磁盘现状

- **全平台物理 GPU 总量（跨队列节点去重）**`[真实文件/实测命令核实]`：共 **15 台 GPU 节点、106 张物理 GPU**（`48 + 40 + 16 + 2 = 106`；注：`HA_011`/`TA_004` 与上述节点共享同一物理机器池，不重复计数）。
- **账户同时运行硬上限**`[真实文件/实测命令核实]`：由 `qstat -Bf` 与 `qmgr -c "p s"` 确认，`max_run_res.ngpus = 24`（用户同一时刻在运行作业占用的 GPU 总和上限为 **24 张**），`max_run = 100`，`max_run_res.ncpus = 5166`。
- **账户机时余额**`[真实文件/实测命令核实]`：`/work/app/cmds/bin/jobtime`（更新时间 `2026/11/21 21:02 JST`）显示总额 `60400.00 H`，已用 `19541.63 H`，剩余 **`40858.37 H`**（此前 20:00 会话汇报约 `40861 h`）。
- **磁盘空间配额**`[真实文件/实测命令核实]`：`lfs quota -h -p 22868 /home` 显示 `/home` 已用 **`1.836 T / 2 T` 软配额**（`2.2 T` 硬上限，`1,116,857` 个文件），距离软配额红线不足 `170 GB`。

### 2.3 硬件验证证据与待确认项

1. **`A_002`（`cgpu011`）8 卡整节点实测**：`[已完成 · 真实文件核实]`
   - 作业 `622685.cmspbs1`（`topo_check`，耗时 `00:01:49`，`Exit_status = 0`），脚本与输出在 `/home/05926/gpucheck/topo_check.sh` 与 `/home/05926/gpucheck/topo_check.o622685`。
   - 实测配置：8 × `NVIDIA H100 80GB HBM3`（单卡 `81559 MiB`），驱动 `580.105.08`，NVLink `NV18` 全互联（18 条链路各 `26.562 GB/s`），InfiniBand `mlx5_0`（Active，速率 `200 Gb/s`），`p2p 0->1 True`，`bf16` 矩阵乘实测吞吐 `23 TFLOPS`（含循环同步开销的简单基准），8 卡 `allreduce 256MB` 实测总线带宽 **`421.7 GB/s busbw`**，`torch 2.11.0+cu128` + `cuda 12.8` + `mace 0.3.15` 加载通过。
2. **`A_002` 整节点资源扣减实测**：`[已完成 · 真实文件核实]`
   - 作业 `622490.cmspbs1`（`gpu_check`，`Exit_status = 0`，耗时 `3 s`）最初仅按测试请求 `mem=4gb`，但 `qstat -x -f 622490` 显示实际分配与计费资源被队列策略调整为整节点 **`112 ncpus / 8 ngpus / place=free:excl`**（执行节点 `cgpu011`）。因此提交到 `A_002` 哪怕跑轻量脚本也会直接消耗 8 GPU 并发额度。
3. **`CA_001` 早期单卡 LAMMPS 实测**：`[已完成 · 真实文件核实]`
   - 目录 `/home/05926/zhaoyue/WORK/lammps_test/`（`lammps_test.o327421`、`log.lammps`，`2026-06-28`）实测分配到 `Device 0: NVIDIA H100 80GB HBM3`（`132 CUs`, `79/79 GB`），跑通 GPU 版 `LAMMPS 22 Jul 2025`（4000 原子 LJ 熔体，NVE 250 步，总 wall time 1 s）。
4. **`IA_001`（`gpu1`）单卡交互实测**：`[已完成 · PBS 作业与历史命令核实，卡型来自此前汇报]`
   - `qstat -x -f 622636` 与 `qstat -x -f 622684` 核实两次均分配在 `IA_001`（`gpu1/0`），`Exit_status = 0`（分别运行 `1m51s` 与 `31s`），`/home/05926/.bash_history_gpu` 记录执行了 `nvidia-smi -L` 与 `nvidia-smi --query-gpu=name,memory.total --format=csv,noheader`。交互窗口终端输出未重定向至文件；`gpu1` 卡型为 **`H100 PCIe 80GB`** 来自 `2026-11-21` Claude Code 本地会话实时汇报 `[此前会话汇报，待落盘复核]`。
5. **`CA_001` 逐节点卡型探测作业（快照状态）**：`[正在运行/排队快照 · 真实命令核实，非永久事实]`
   - 作业号 **`622515–622520`**（`chk_cgpu001` 至 `chk_cgpu006`，工作目录 `/home/05926/gpucheck`，各申请 `1 CPU / 1 GPU / 4 GB / 5 min`，指定不同 `host`）。
   - 截至 `2026-11-21 20:45 CST`（`21:45 JST`）`qstat -u 05926 -w` 与 `qstat -f 622515` 显示 6 个作业**全部处于 `Q` 排队状态**（`comment = Not Running: Insufficient amount of resource: Qlist`）。严禁把该排队快照写成永久结论，待这批作业完成后须回写各节点实际型号。
6. **尚未确认的硬件与性能项**：`[未确认]`
   - `CA_001`（`cgpu001–cgpu006`）近期各节点卡型、`A_002` 其余 4 台节点（`cgpu007–cgpu010`）、`A_001` 2 台节点（`cgpu012–cgpu013`）及 `IA_001` 另 1 台节点（`gpu2`）的具体 GPU 型号均尚未实测确认。
   - GPU 队列对 `jobtime` 剩余机时的具体计费换算比例尚未确认。
   - 跨节点（如 `A_002` 上 2 节点 16 GPU）的实际多机分布式训练扩展效率尚未实测。

### 2.4 IMR GPU 常用只读查询命令

- 查询 GPU 队列规则与限制：`qstat -Qf CA_001 DA_002 A_002 A_001 IA_001`
- 查询各节点状态、空闲 GPU/CPU/内存与归属队列：
  ```bash
  pbsnodes -a | awk '/^[a-zA-Z0-9_-]+$/{if(n&&g>0)print n,"state="s,"ngpus="g,"ncpus="c,"mem="m,"qlist="q;n=$1;s="";g=0;c="";m="";q=""} /state =/{s=$3} /resources_available.ngpus =/{g=$3} /resources_available.ncpus =/{c=$3} /resources_available.mem =/{m=$3} /resources_available.Qlist =/{q=$3} END{if(n&&g>0)print n,"state="s,"ngpus="g,"ncpus="c,"mem="m,"qlist="q}'
  ```
- 查询服务器级硬上限：`qstat -Bf` 或 `qmgr -c "p s" | grep -iE "ngpus|max_run"`
- 查询账号作业及已完成作业详情：`qstat -u 05926 -w`、`qstat -x -f <jobid>`
- 查询机时余额：`/work/app/cmds/bin/jobtime`
- 查询 `/home` 空间配额：`lfs quota -h -p 22868 /home`

---

## 3. 已有 AIMD 与分子动力学计算盘点

> **重要事实声明**：截至 `2026-11-21`，课题组已完成并取得物理轨迹的分子动力学**全部为传统 VASP AIMD**；**尚未完成任何真正的 MACE / ML-MD 或 ReaxFF 生产计算**。当前 Genkai（`pjstat -v` 空）与 IMR（`qstat -u 05926` 仅有静态任务与 GPU 探测任务）**均无任何正在运行或排队的 AIMD / MD 作业** `[真实文件/实测命令核实]`。

### 3.1 FeCo-NC / FeCo-NC(H) 项目（博论第 4 章 / FeCo 小论文）

已完成 **7 条 VASP AIMD 轨迹**，有效模拟时长合计 **`75.0 ps`（`75,000` 帧）** `[真实文件/实测命令核实]`。

#### A. 计算软件与方法参数

- **软件与计算资源**：`VASP 6.3.2`（Genkai `a-pj25000114` 队列，1 节点 120 核，`NCORE=12`）。
- **电子结构设置**：PAW-PBE（`GGA=PE`）+ DFT-D3(BJ)（`IVDW=12`），`ISPIN=2`，`ENCUT=400 eV`，`PREC=Normal`，`EDIFF=1E-4`，`ALGO=Fast`，`LREAL=Auto`，`ISMEAR=1`，`SIGMA=0.10`，Gamma 点（`1×1×1`），`ISYM=0`，`LDIPOL=.TRUE., IDIPOL=3`。
  - 显式水额外设置：`c = 30.50 Å`，`DIPOL = 0.5 0.5 0.66`，`POMASS(H) = 2.000`（氘质量以保证 1 fs 步长积分稳定）。
  - 后期续算统一设置 `LCHARG = .FALSE.`（2026-10-08 因 `LCHARG=.TRUE.` 追加 `CHG` 写满 Genkai 组配额 `11263/11264 GB` 致作业中断，此后修正）。
- **动力学系综**：NVT，Nosé–Hoover 热浴（`IBRION=0, ISIF=2, MDALGO=2, SMASS=0`），时间步长 `POTIM = 1.0 fs`。

#### B. 7 条已完成轨迹与续算/作废分段明细

| 序号 | 体系与条件 | 模型与原子数 | 晶胞尺寸 (Å) | 温度 / 步长 / 有效总时长 | 有效分段与步数 | 显式水 / 吸附物 / 界面 | 状态与作废/未投段说明 |
|---|---|---|---|---|---|---|---|
| 1 | `A1_OH_aimd_300K` | FeCo-NC(H)（团簇+空位），154 原子（C129 N6 Fe6 Co11 O1 H1，底部固定 12） | `17.22 × 21.30 × 27.00` | 300 K / 1.0 fs / **12.0 ps** | 原 `3000` + `cont1 3161` + `cont2r 5839`（共 12000 帧） | 真空；Fe 顶 `OH*`；无电位 | **已完成**。注：`cont2`（5839 步）因沿用 3 ps 旧 `WAVECAR` 导致总磁矩翻至 `-10.03 μB` 且能量高约 `1.3 eV`，**已作废**，由 `cont2r` 替代 |
| 2 | `A2_OH_aimd_300K` | FeCo-NC_DA(H)（无团簇有空位），139 原子（C129 N6 Fe1 Co1 O1 H1，固定 0） | `17.22 × 21.30 × 27.00` | 300 K / 1.0 fs / **12.0 ps** | 原 `3181` + `cont1 8819`（共 12000 帧） | 真空；Fe 顶 `OH*`；无电位 | **已完成** |
| 3 | `A3_OH_aimd_300K` | FeCo-NC_DA（无团簇无空位），140 原子（C130 N6 Fe1 Co1 O1 H1，固定 0） | `17.22 × 21.30 × 27.00` | 300 K / 1.0 fs / **12.0 ps** | 原 `3861` + `cont1 8139`（共 12000 帧） | 真空；Fe 顶 `OH*`；无电位 | **已完成** |
| 4 | `A4_OH_aimd_300K` | FeCo-NC（有团簇无空位），155 原子（C130 N6 Fe6 Co11 O1 H1，底部固定 12） | `17.22 × 21.30 × 27.00` | 300 K / 1.0 fs / **12.0 ps** | 原 `3000` + `cont1 3081` + `cont2b 5919`（共 12000 帧） | 真空；Fe 顶 `OH*`；无电位 | **已完成**。注：`cont2`（17 步）因旧 `WAVECAR` 首步发散至 `12501 K` 并报 `FEXCF` 退出，**已作废**，由 `cont2b`（从头 SCF）替代 |
| 5 | `A1_OH_aimd_500K` | FeCo-NC(H)，154 原子（固定 12） | `17.22 × 21.30 × 27.00` | **500 K** / 1.0 fs / **12.0 ps** | 原 `3000` + `cont1 762` + `cont2 8238`（共 12000 帧） | 真空；Fe 顶 `OH*`；无电位 | **已完成** |
| 6 | `A1_ObriOOH_aimd_300K` | FeCo-NC(H)，156 原子（C129 N6 Fe6 Co11 O3 H1，固定 12） | `17.22 × 21.30 × 27.00` | 300 K / 1.0 fs / **12.0 ps** | 原 `3000` + `cont1 623` + `cont2 8377`（共 12000 帧） | 真空；桥位 `O*` + Fe 顶 `OOH*`；无电位 | **已完成** |
| 7 | `A1_OH_water_aimd_300K` | FeCo-NC(H) + 40 H2O，274 原子（C129 N6 Fe6 Co11 O41 H81，固定 12） | `17.22 × 21.30 × 30.50` | 300 K / 1.0 fs / **3.0 ps** | 单段 `3000` 帧 | **显式水（40 H2O）** + Fe 顶 `OH*`；电中性无离子无电位 | **已完成**。`A1_OH_water_aimd_300K_cont1` 目录（含 `2.18 GB` `WAVECAR`）仅建目录从未提交，因末帧 2 个水分子穿 PBC 到晶胞底部且已定稿不续（`待执行/已搁置`） |

#### C. 数值收敛、自旋变化与能量漂移问题（训练 MLP 前必看）

- **能量与力标签完整性**`[真实文件核实]`：上述 18 个有效分段 `OUTCAR` 与 `vasprun.xml` 均完整写出每步 `TOTAL-FORCE (eV/Angst)` 与能量，全部 **75,000 有效帧**可提取构型、能量、原子力。
- **SCF 收敛**：18 个有效分段累计仅 **36 步**触及 `NELM=120` 上限（`A1_OH_aimd_300K` 首段 29 步、`A1_OH_500K_cont2` 3 步、`A2_OH` 首段 2 步、`A1_ObriOOH` 与 `A4_OH` 首段各 1 步），其余步 SCF 均收敛。
- **扩展能量漂移**：1–6 ps 专项诊断显示，四模型 Nosé–Hoover 扩展守恒量 `E` 均存在系统性向下漂移（A1 `-0.326`、A4 `-0.346`、A2 `-0.287`、A3 `-0.239 eV/ps`），不能声称严格能量守恒（推测与 `EDIFF=1E-4`、`LREAL=Auto` 等集成设置有关）。
- **总磁矩漂移与跳变**：`A2_OH` 总磁矩在 `+1.97 -> -1.95 -> ~0.00 μB` 间切换；`A3_OH` 由 `+2.03` 降至 `~0.03 μB`；`A1_ObriOOH` 由 `37.9` 降至 `29.2 μB`；`A1_OH_300K_cont2r` 总磁矩保持正值并在 `+33.09 ~ +38.37 μB` 间波动。**因此 75,000 帧不可未经自旋分组与异常帧过滤直接用于训练单一势函数**。

#### D. 已获得的科学分析结果

1. **位点配位与 OH* 顶位/桥位动态迁移**：
   - `A1_OH_300K` 前 3 ps 已计算 `FeCoN6` 位点核心 Kabsch RMSD，均值 **`0.193 ± 0.073 Å`**（最大 `0.359 Å`），并观察到 15 原子团簇在碳层下方横向滑移约 `2.1–2.5 Å` 到活性位正下方（`plot_aimd_rich.py`）。注：12 ps 全程 RMSD 尚未更新重算。
   - 1–6 ps 专项诊断（`AIMD_four_models_6ps`）：四模型 6 根 `M–N` 键 2.5 Å 阈值几何配位数保持 `3.00`；团簇几何回转半径 `Rg ≈ 2.573 ± 0.010 Å`（未解体）。真空 300 K 下，A1 约在 `1.2 ps` 后 `OH*` 由 Fe 顶位滑向 Fe–Co 桥位，并在 `2.216–2.475 ps` 短暂转向 Co 配位（最大 `Fe–O = 3.274 Å` 时 `O–Co = 1.864 Å`）；A4 在 `1.521–1.584 ps` 亦出现短时转向 Co（最大 `Fe–O = 2.630 Å`，`O–Co = 1.869 Å`），说明该动态配位并非 A1 独有。
   - 12 ps 有效轨迹统计（`AIMD_对比_四模型_12ps_有效A1_统计_20261107_141928.csv`）：四模型 `OH*` 均未脱附，`O–H` 均值 `0.977–0.980 Å`；`Fe–Co` 均值分别为 A1 `2.480`、A4 `2.488`、A2 `2.540`、A3 `2.547 Å`；`M–N` 均值分别为 `1.962 / 1.935 / 1.922 / 1.913 Å`。
   - 12 ps 新现象：`A1_ObriOOH_300K` 中 `O–O` 平均 `1.48 Å`（最大 `1.67 Å`）不断裂，`Fe–Co` 均距拉宽至 `2.807 Å`，且 **3 ps 后 `Fe–N130` 键在 59% 的时间里拉长至 `2.6–2.75 Å`（>2.4 Å）**；`A1_OH_500K` 后半程均温 `497 K`，仅 `Co–N133` 在约 6% 时间里短暂拉长（最长 `0.4 ps`），整体骨架完整。
2. **显式水氢键与界面稳定化（`A1_OH_water_aimd_300K`，3 ps）**：
   - 氢键统计（`data\aimd_water_water_geom.csv`）：`OH*` 氧原子平均**接受 `1.584 ± 0.667` 条氢键**（范围 `0–3`），氢原子平均**供出 `0.536 ± 0.515` 条氢键**（范围 `0–2`）；`O(H)–O_water` 最近距离均值 `2.820 ± 0.255 Å`。
   - 水膜密度分布（`AIMD_A1_OH_显式水_密度_20260923_052443.csv`）：第一水层 O 峰位于金属面上方 **`2.875 Å`**（峰值 `0.05141 mol cm^-3`，接近体相水 `0.055`），H 峰位于 **`3.375 Å`**（`0.08396 mol cm^-3`）；全程 **`water_on_metal = 0`**（无水分子直接配位金属位点）。
   - 界面效应对照：与真空 300 K 滑向桥位不同，显式水氢键网把 `OH*` **全程稳定锚定在 Fe 顶位**（`Fe–O = 1.929 ± 0.072 Å`，`Fe–Co = 2.323 ± 0.096 Å`）。缺陷：3 ps 末帧已有 2 个水分子穿过 `z` 向周期边界到达晶胞底部（O 位于 `z = 2.9, 3.4 Å`）。

#### E. 原始数据、分析脚本与图件路径

- **Genkai 原始 20 个 AIMD 分段目录**：`/home/pj25000114/ku50002299/FeCo_v2_genkai_20260916/`
- **Genkai 拼接轨集**：
  - 最新有效 A1（已接入 `cont2r`）：`/home/pj25000114/ku50002299/FeCo_v2_genkai_20260916/_aimd12ps_valid_cont2r_20261107/`
  - 其余 5 条 12 ps 拼接目录：`/home/pj25000114/ku50002299/FeCo_v2_genkai_20260916/_aimd12ps_20261015/`（注意该目录下 `A1_OH_300K_*` 含作废 `cont2`，**严禁再用**）
- **本地任务模板备份**：`D:\OneDrive\1a1数据文档\03_第4章_FeCo\FeCo_DFT_jobs_v2_20260911\_genkai_20260916\`
- **本地分析数据、脚本与成品图**：`D:\OneDrive\1a1数据文档\03_第4章_FeCo\FeCo_DFT_figures\FeCo_supp_figs_20260918\`
  - 数据：`data\aimd12ps_valid_20261107\`、`data\aimd12ps_20261015\`、`data\aimd_water_water_geom.csv`、`AIMD_对比_四模型_12ps_有效A1_统计_20261107_141928.csv`、`AIMD_A1_OH_显式水_密度_20260923_052443.csv`、`AIMD_A1_OH_丰富版_统计_20260920_120939.csv`
  - 脚本：`plot_aimd_rich.py`、`plot_aimd_water_v4.py`、`plot_aimd_compare_12ps_valid_20261107.py`
- **本地 1–6 ps 诊断档案**：`D:\Codex工作归档\2026-10-10\ni\outputs\AIMD_four_models_6ps\`（`初步分析.md`、`analysis_summary.json`、`comparison_summary.csv`）
- **FeCo 小论文扩展模拟规划单**：`D:\OneDrive\Desktop\博士毕业论文撰写\小论文_FeCo_20261105\FeCo小论文_补充模拟任务单_交其他智能体_v4_20261107.md`（其中 `T5/T14/T15动态/T16/T17/T24` 均处计划/暂缓状态）

### 3.2 FeCoMn-NC、NO3RR 及其他项目

- **FeCoMn-NC（博论第 5 章 / ACS 投稿）**：
  - `FCM_aimd_300K`（裸 clean 表面 `S_FeCoMnNC59_clean`，`C174 N4 Fe27 Co32 Mn1` 共 238 原子，固定 15，300 K，1.0 fs，目标 12 ps，PBE+D3-BJ，`ENCUT=400 eV`，`LCHARG=.FALSE.`）：
    - Genkai 副本（`/home/pj25000114/ku50002299/stability_from_imr_20261016/FCM_aimd_300K`，`VASP 6.6.0`，Job `7090640`）因墙时设 `24:00:00` 触发 `ELAPSE LIMIT EXCEEDED`（`PJM CODE 11`），**仅完成 `1007` 步（`1.007 ps`）即中断** `[真实文件核实]`。未进行任何 RMSD/配位/能量分析，也未续算。
    - IMR 副本（`/home/05926/zhaoyue/WORK/FeCoMn_ch5_recalc_20261007/stability_20261015/FCM_aimd_300K`，`VASP 6.3.2`，Job `481228/481405`）仅跑 `106` 步（`0.106 ps`）后因跨超算去重被终止 `[真实文件核实]`。
    - 对照组 `FCN_aimd_300K`（`S_FeCoNC59_clean`）从未建目录与提交（`待执行/未启动`）。
  - **已定项目策略**：FeCoMn-NC 当前以尽快投稿为第一优先，**不安排重复或续算裸表面 AIMD**。
- **NO3RR（投 Angew）**：
  - Genkai `~/NO3RR_anneal_20260731/` 下 2 条 1000 K 退火（`CO2H_slab_anneal1000K` 231 原子 Job `6343951`、`NH21_slab_anneal1000K` 227 原子 Job `6343952`）均在第 0/1 步因 `ZHEGV`/SCF 发散崩溃（`失败`，0 有效轨迹） `[真实文件核实]`。
- **CoMn-NSC（博论第 3 章，已发 AFM）/ WaterSplitting / Pseudocapacitance**：
  - 本地磁盘、GitHub 与 Genkai/IMR 均未检出任何 MD/AIMD/MACE 文件或运行记录（`未确认/无记录`）。

---

## 4. 未来 6 个月 IMR GPU + AI4Science 科研计划与原则

- **整体目标**：在 IMR GPU 剩余访问期内（预计 ≤ 6 个月，可能提前终止）最大化实际科研产出，直接服务核心论文的机理论证与投稿，**不用于单纯学习 GPU 或训练通用大语言模型**。

### 4.1 优先级路线图（全部标为 `待执行`）

| 优先级 | 任务阶段 | 核心内容与交付标准 | 当前状态 |
|---|---|---|---|
| **P0** | 已有资产安全备份 | 完整备份已有 DFT 静态/覆盖度、75 ps FeCo AIMD 关键输出（含 `OUTCAR`/`vasprun.xml`/`CONTCAR`）、分析脚本与 conda 环境清单至本地与异地存储，防范 IMR 权限提前到期 | `待执行` |
| **P0** | AIMD 轨迹清洗与标定准备 | 清洗 75,000 帧 FeCo AIMD 轨迹：剔除 `A1 cont2`、`A4 cont2` 与 36 个撞 `NELM` 步，按总磁矩平台分段，校验能量/受力标签连续性，生成去相关结构元数据表 | `待执行` |
| **P1** | MACE 预训练评估与微调 | 在清洗验证集上测试 MACE 预训练基座模型（如 `MACE-MP-0`）对 FeCo-NC 的能量/力零样本误差；若偏差超标，先对抽帧子集做**统一高精度 DFT 口径（如 `ENCUT=500 eV`）**单点重标，再在 GPU 队列微调并完成严格留出测试 | `待执行` |
| **P1** | 显式水界面 ML-MD | 经 P1 精度严格验证后，在 `CA_001`/`A_002` 跑足 `c` 轴防穿底的 FeCo-NC（A1/A4/A2）显式水百皮秒至纳秒级 ML-MD，定量解析 `OH*` 顶/桥动态吸附、氢键网络寿命与局部配位切换 | `待执行` |
| **P2** | OOH* 采样与增强采样自由能 | 根据 P1 显式水结果评估是否开展 `OOH*` 构型空间采样、增强采样（Umbrella Sampling / Metadynamics）及 `O2 -> *OOH` 质子转移自由能垒计算 | `待执行` |
| **P3** | 大规模含离子电化学界面 | 若 P1–P2 模型可靠且仍有额外 GPU 机时，对接 GPU 版 LAMMPS 探索含 `K+` / `OH-` 显式电解液电双层大体系界面动力学 | `待执行` |

### 4.2 不可违背的 7 条科研原则

1. **不重复**已经完成的干态 12 ps AIMD（6 条轨迹已齐全）。
2. **不混训**：严禁将不同 DFT 精度（如 400 eV AIMD 与 500 eV 静态）、不同自旋/磁态的数据直接混合训练同一 ML 势。
3. **不替代**：不将 MACE 预测结果直接等同于 DFT 能量或几何。
4. **不越界表述**：不将电中性显式水模拟直接描述成恒电位电化学模拟。
5. **DFT 复核底线**：任何由 ML-MD 发现的关键构型、过渡态和科学结论，必须回代统一口径的 DFT 计算验证。
6. **FeCoMn-NC 投稿优先**：FeCoMn-NC 当前以尽快修改定稿并投稿为最高优先，不因任何 AI4Science / GPU 新计算推迟投稿节奏。
7. **问题导向选题**：新 GPU 任务优先选择能够实质性补强核心论文机理论证与审稿防御的科学问题。

---

## 5. 软件环境与资源风险登记

### 5.1 已核查软件栈版本 `[真实文件/实测命令核实]`

| 类别 | 安装路径 / 位置 | 已核实版本与组件 |
|---|---|---|
| **PyTorch & CUDA (Conda)** | `/home/05926/anaconda3/envs/mace` | `torch 2.11.0+cu128`、`torchvision 0.26.0+cu128`、`CUDA 12.8`（节点实测 NVIDIA Driver `580.105.08`；系统 `/work/app/cuda` 另有 `9.2/10.2/11.8/12.8/12.9/13.0`） |
| **MACE 生态** | `/home/05926/anaconda3/envs/mace` | `mace-torch 0.3.15`（含 `e3nn 0.4.4`、`torch_ema 0.3`、`torchmetrics 1.9.0`，CLI 含 `mace_run_train`、`mace_finetuning_select`、`mace_active_learning_md`、`mace_eval_configs`、`mace_create_lammps_model`） |
| **ASE** | `/home/05926/anaconda3/envs/mace` | `ase 3.28.0` |
| **NCCL** | `/home/05926/anaconda3/envs/mace` | `nvidia-nccl-cu12 2.28.9`（`A_002` 8 卡 H100 allreduce 256MB 实测 `421.7 GB/s busbw`） |
| **LAMMPS** | `/work/app/LAMMPS/` | `lammps-22Jul2025_gpu`（已在 `CA_001` 跑通单卡 H100）、`lammps-22Jul2025_Update5_gpu`、`lammps-22Jul2025kokkos_gpu`、`lammps-22Jul2025_cpu` 及 `29Aug2024` 系列 |
| **Singularity & 容器** | `/usr/bin/singularity`、`/work/app/PyTorch/` | `singularity-ce version 4.2.2-1.el9`（无 `apptainer`）；含 `pythorch_gpu.sif`、`pythorch.sif` |

### 5.2 风险标记与应对规程

1. **MACE 训练与精度未验证（红线）**：`mace 0.3.15` 已确认可在 H100 GPU 上正常导入加载，但**正式训练脚本吞吐速度、显存占用及对 FeCo-N-C 含磁体系的能量/力误差尚未经过任何实测验证**。
2. **`/home` 配额紧迫（红线）**：账号 `/home` 已使用 **`1.836 T / 2 T` 软配额**（硬上限 `2.2 T`），剩余安全空间不足 `170 GB`。开展 ML 数据集生成、模型权重保存与 ns 级轨迹输出前，必须先规划清理陈旧波函数/临时轨迹并设置输出轮转。
3. **访问终止与异地容灾**：由于 IMR 使用期预期 ≤ 6 个月，所有模型训练**必须实行阶段性 checkpoint 保存（按 epoch 定期落盘）并同步做本地/异地备份**，同时保留 `conda env export` 与训练配置脚本，确保随时可迁移复现。

---

## 6. 与既有长期记忆的差异对账

本档案保持已有历史记录原文不变，仅在此明确新旧衔接口径：
1. **相对 `reference_imr_queue_reality_20260915.md`**：
   - `A_001` 权限更新：2026-09-18 曾记录 `A_001` 有白名单限制不可用；2026-11-21 `qstat -Qf A_001` 实测 `acl_user_enable = False`（但尚未实测提交）。
   - GPU 节点总量澄清：2026-09-23 记录了 `cgpu001–011`（11 台）；2026-11-21 全量 `pbsnodes -a` 补齐了 `A_001`（`cgpu012–013`）和 `IA_001`（`gpu1–gpu2`），确认全平台跨队列去重总计 **15 台节点、106 张 GPU**。
2. **相对 `project_md_ml_pipeline.md` / `projects/project_md_ml_pipeline_20260606.md`**：
   - 更新 `lammps_test` 状态：`2026-06-06` 记录 `323861` 仍在排队，现已核实 `lammps_test` 后续作业 `327421` 于 `2026-06-28` 在 `CA_001` 单卡 H100 成功跑通。
   - 本档案正式接替 `2026-06-06` 早期版图规划，作为未来半年 IMR GPU + AI4Science 执行与状态追踪的唯一统一参考。
3. **相对 `aimd12ps_20261015` 拼接目录**：
   - 重申 `A1_OH_300K` 有效 12 ps 轨迹必须采用 `aimd12ps_valid_20261107`（Genkai `_aimd12ps_valid_cont2r_20261107`），`aimd12ps_20261015` 中的 A1 轨迹含作废 `cont2`，严禁用于 MACE 训练或力学统计。

---

## 7. 原地更新变更日志

- **2026-11-21**：首版建档。完成 IMR GPU 队列/节点/配额/软件栈全量只读核查、Genkai/IMR 全部 AIMD 与 MD 历史成果逐文件审计，并确立未来 6 个月 P0–P3 科研路线与 7 条科研原则。本地档案 `D:\AI-Shared-Memory\project_imr_gpu_ai4science_20261121.md` 与 GitHub `yuezhao-cat/research-relay` 的 `AI4Science/IMR_GPU_RESEARCH_PLAN.md` 保持同步。
