# T040 轴向 OH 是否削弱对位 OOH* 的 dz² 成键（LOBSTER 后处理）

执行：Claude Code　核查：Antigravity　决策：Claude web　状态：**已批准**，赵月 2026-11-20 12:42："跑 提交到IMR"

## 目的
检验摘要候选句"轴向 OH 削弱对位中间体结合"在轨道层面的直接证据：同一 FeCoMn–NC，Mn–OOH* 的 dz² 成键在对位有无 OH 时是否不同。

## 对象
1. 无轴向 OH：T032 第 3 节已有 "FCM 8O*，Mn 无轴向 OH" 的 OOH* 静态（Mn 约 +2.233 μB）。
2. 有轴向 OH：T037 已有结果，Mn–OOH* dz² 分波 −ICOHP 1.38 eV。

## 步骤
1. 先确认对象 1 的静态是否有 WAVECAR 与 LOBSTER 所需输出；有则直接跑 LOBSTER，设置与 T037 完全一致（同基组、同能量窗口、同 COHP 对定义）。
2. 缺 WAVECAR 则需对该几何重跑静态单点（与 T037 同 INCAR）：赵月已批准在 IMR 上跑，按同 INCAR 重跑静态单点后再做 LOBSTER，REPORT 写明是重跑。
3. 输出 Mn–O(OOH*) 的总 −ICOHP 与 dz² 分波 −ICOHP，与 1.38 eV 并列成表；同时给出 Mn 磁矩。

## 交付
FeCoMn/from_agent/FeCoMn-T040/REPORT.md；Antigravity 核查写 FeCoMn/review/T040_Antigravity.md。只陈述数值，不写机理推测。不改图、不改 Word。

## 计算平台
IMR。提交前先查队列，确认没有同名或重复作业。
