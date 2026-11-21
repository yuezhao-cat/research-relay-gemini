# T038 颗粒为什么使相邻 Mn 偏向轴向 OH：干净结构电子态比较

执行：Antigravity　核查：Claude Code　决策：Claude（web）　日期：2026-11-19

## 目的
论文逻辑链：FeCo 颗粒 → 改变 Mn 电子态 → 在 ORR 电位下 Mn 轴向 OH 比 O 稳定 → OH 使吸附适中。
前两环之间缺证据。已有 Mn 电子数据都在带配体之后，分不清颗粒作用与配体作用。本任务只比较**无轴向配体**的干净结构。

## 构型口径（已关闭，不讨论）
覆盖取已算构型中最低能：FeCoMn–NC 8O*+Mn–OH，Mn–NC O bri 轴向 Mn=O。不追加构型搜索。

## 比较对象（只用已有输出，不跑新 DFT/优化）
A. 干净 FeCoMn–NC（`FCM clean`）　B. 干净 Mn–NC（`MnNC clean`）
C. 颗粒 8O* 覆盖、Mn 无轴向配体（`FCM 8O`）——对应工作态颗粒背景
若已有静态含 CHGCAR/AECCAR/DOSCAR 则直接后处理；缺哪个就在 REPORT 写明缺失，等 Claude 决定，不自行补算。

## 提取
1. Mn 及 4 个 N 的 Bader 电子数（A、B、C）；Mn 局域磁矩。
2. 差分电荷：Δρ = ρ(A) − ρ(颗粒单独) − ρ(Mn–NC 载体单独)，同几何切分；给出 Mn–N4 区域的积分电荷变化和平面平均曲线。C 同理（颗粒含 8O*）。若需要切分的单独静态不存在，写明，不补算。
3. Mn 3d 与 dz² PDOS、dz² 中心、总 d 中心（A、B、C）。
4. 汇总表 + 判断：颗粒是否使 Mn 得到电子、dz² 是否上移；方向是否与"OH 比 O 更稳定"一致。只陈述数值，不写推测性机理。

## 交付
FeCoMn/from_agent/FeCoMn-T038/（REPORT.md、数据 CSV/JSON、原始路径）。Claude Code 核查写 FeCoMn/review/T038_ClaudeCode.md。不改图、不改 Word。

---
## T038b 补算（用户 2026-11-19 18:30 决定：重新算；执行 Claude Code，核查 Antigravity）

只做静态单点，不重新优化，几何取已优化结构；INCAR 关键设置与原电子结构静态一致（同 PAW、ENCUT、k 点、ISPIN=2、初始磁矩沿用原做法），LORBIT=11，保存 CHGCAR、AECCAR0、AECCAR2、DOSCAR、OUTCAR。

| 编号 | 体系 | 几何来源 |
|---|---|---|
| A | 干净 FeCoMn–NC | `FCM clean` 优化 CONTCAR |
| B | 干净 Mn–NC | `MnNC clean` 优化 CONTCAR |
| A-p | 仅 FeCo 颗粒（删去载体 C/N/Mn） | A 的几何，原子位置不动 |
| A-s | 仅 Mn–N–C 载体（删去颗粒 Fe/Co） | A 的几何，原子位置不动 |
| C | 颗粒 8O*、Mn 无配体 | 已有 DOSCAR；仅补 Bader 后处理 |

步骤
1. 先在 Genkai/IMR 复查 A、B 是否确有现成 LORBIT=11 静态（避免重复算）；有则直接用并写明路径。
2. 准备输入、提交；第一次收敛结果单列，Mn 磁矩跳分支须报告，不换分支、不混旧能量。
3. 提取：Mn 与 4 个 N 的 Bader 电子数（A、B、C）；Mn 局域磁矩；Mn 3d 与 dz² PDOS、d 中心与 dz² 中心（A、B、C）；Δρ = ρ(A) − ρ(A-p) − ρ(A-s) 的平面平均曲线与 Mn–N4 区域积分。
4. REPORT：汇总表 + 只陈述数值方向（Mn 得失电子、dz² 是否上移、电子流向），不写推测机理。

交付 FeCoMn/from_agent/FeCoMn-T038/b/；Antigravity 独立核查，写 FeCoMn/review/T038b_Antigravity.md。不改图、不改 Word。
