# T041 OOH* 吸附的几何形变 / 电子结合拆分（补 1 个静态）

执行：Antigravity　核查：Claude Code　决策：Claude web　批准：赵月 2026-11-20 13:37（"好"）

## 目的
回答核心问题 3（轴向 OH 如何使吸附适中）。Antigravity 已在 Genkai 现有静态中拆出 OH*：加轴向 OH 使 OH* 吸附削弱 +0.336 eV = 基底形变 +0.236 eV + 冻结几何电子结合 +0.100 eV。对限速步 OOH* 做同样拆分，缺 1 个静态。

## 计算
- 补算：8O* 颗粒、Mn 无轴向 OH 的 OOH* 吸附结构中，删去 OOH* 后的基底（substrate）静态单点，几何不动。
- 设置与现有 `8O_noOH` / `8O_OH` 的 full/substrate/adsorbate 静态完全一致（同一机器 Genkai、Gamma 1×1×1、ISMEAR 0、SIGMA 0.05、同 PAW/ENCUT/D3），初始磁矩沿用原采用分支，不做自旋扫描（赵月 13:36 决定：低能分支不考虑）。
- 提交前查队列，避免重复作业。

## 输出
无 OH 与有 OH 两种情况下 OOH* 的：E_bind（总）、E_distort（基底形变）、E_bind_frozen（冻结几何电子结合），以及 Mn 离面高度变化；与 OH* 的拆分并列成表。只陈述数值。

## 同时请 Claude Code 复核
Antigravity 13:03 报告的 OH* 拆分（+0.336 = +0.236 + +0.100 eV）、Mn 离面 +0.442 Å / 移动 0.466 Å、颗粒 rms 0.005 Å：独立从原始 OUTCAR/CONTCAR 复算。

## 交付
FeCoMn/from_agent/FeCoMn-T041/REPORT.md；Claude Code 核查写 FeCoMn/review/T041_ClaudeCode.md（含 OH* 拆分复核）。不改图、不改 Word。
