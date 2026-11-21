# T039 去掉颗粒后 Mn 轴向 OH 与 O 的相对稳定性（IMR）

执行：Antigravity　核查：Claude Code（独立复算 ΔG，不用执行方的中间数）　决策：Claude web　批准：赵月 2026-11-20 11:19（"算 提交到IMR"）

## 目的
正文要写"FeCo 颗粒决定 Mn 的轴向配体"，现有证据不够：0.78 V 下 FeCoMn–NC 中 OH 比 O 稳定 0.18 eV，Mn–NC 中 O 比 OH 稳定 0.30 eV，但两者载体几何不同（T038b：As vs B 的 Mn Bader 差 −0.040 e）。本任务在同一几何下只去掉颗粒，看配体偏好是否翻转。只算这一组，不扩展构型和自旋搜索。

## 体系（共 2 个优化）
几何来源：T038 的 C_support，即 FeCoMn–NC "8O*、Mn 无配体" 优化结构删去颗粒（Fe、Co 及颗粒上的 8 个 O），其余原子不动。

| 编号 | 体系 | 起始结构 |
|---|---|---|
| S-OH | C_support + Mn 轴向 OH | OH 位置取自 FCM 8O*+Mn–OH 优化结构中的 Mn–OH 坐标 |
| S-O | C_support + Mn 轴向 O | O 位置取自 FCM 8O*+Mn–O 优化结构中的 Mn–O 坐标 |

约束：只放开 Mn、配体原子（O/H）和与 Mn 成键的 4 个 N，其余原子固定（选择性动力学）。这样载体几何与 FeCoMn–NC 相同，唯一变量是有没有颗粒。

## 计算设置
- 与 Table S10（覆盖候选，现行 SI）完全一致：同 PAW（Mn_pv）、ENCUT、k 点、泛函、D3(BJ)、ISPIN=2、收敛标准。直接复制原 FCM 8O*+Mn–OH 任务的 INCAR/KPOINTS，只改 POSCAR 和选择性动力学。
- 初始磁矩：沿用对应 FCM 结构（Mn–OH / Mn–O）原先采用的分支，不换分支。第一次收敛结果单列；若 Mn 磁矩跳到其他分支，如实报告，不另行搜索。
- 自由能：用 SI 式 S3/S8 的同一套 CHE 公式和同一套 ZPE−TS 修正（Mn–OH、Mn–O 各自沿用 Table S10 所用值），给出 0.78 V vs RHE 下 G_form，以及 ΔG = G(Mn–OH) − G(Mn–O)。
- 提交到 IMR。IMR 上重复的 T038b 作业 617153–617156 不要动（删除或取消需赵月同意）。

## 交付
FeCoMn/from_agent/FeCoMn-T039/：REPORT.md（两体系能量、Mn 磁矩、Mn–O 键长、G_form 和 ΔG，与 FCM 的 −0.18 eV、Mn–NC 的 +0.30 eV 并列成表）；原始路径；INCAR 与原任务的 diff。
REPORT 只陈述数值和方向（OH 比 O 稳定多少，或反之），不写机理推测。
Claude Code 核查写 FeCoMn/review/T039_ClaudeCode.md：核对几何确实只删颗粒、INCAR 一致、磁矩分支、ΔG 独立复算。
不改图、不改 Word。

## 2026-11-20 12:42 更新（赵月）
S-OH 作业 617432 是重复作业，被终止属正常，不续投。以另一份 S-OH 作业为准；S-O（617433）继续跑。
