# T037 图6补齐机理：轴向配体如何经由 Mn dz² 改变 Mn–OOH* 成键

执行：Antigravity　核查：Claude Code　决策：Claude（web）
日期：2026-11-19

## 目的
图6的任务是解释：为什么 FeCoMn–NC 中 Mn 带轴向 OH（而 Mn–NC 带轴向 O）时，Mn 对 OOH* 吸附更强。
现图从 (b)(c)"轴向配体不同"直接跳到 (e)"Mn–OOH* 更强"，中间缺轨道层面的连接。T032 已证明：
- 轴向键与反位 Mn–OOH* 键都含 Mn dz² 成分（FCM OOH*态：轴向 dz² 分项 1.51 eV，反位 1.38 eV）
- 轴向 Mn=O（MnNC）dz² 分项 2.98 eV，轴向 Mn–OH（FCM）0.995 eV
- 总 d 带中心相近（−3.42/−3.44 eV），dz² 中心 −3.17（FCM）vs −5.08 eV（MnNC）

## 步骤（先只做1–3、5，交报告后停下）
1. 静态来源沿用 11-18 已定口径（T033 DELIVERY）：现图 (a)(c) 的 PDOS/Bader/磁矩保持原 Genkai 链不动；COHP 用 IMR 专用静态。
   新增的 dz² 相关量一律从 COHP 专用静态取：IMR `FeCoMn_COHP_20261023/MnNC_base_full/` 已含 LORBIT=11 完整 DOSCAR，dz² PDOS 与 dz² 分项 COHP 同源，不需补算、不跑 LOBSTER。FCM 同理，取其 COHP 静态目录的 DOSCAR。
2. 从上述 COHP 静态提取（FCM 8O+MnOH 背景、MnNC Mn=O 背景，以及两者 OOH* 态）：
   - Mn dz² PDOS（自旋分辨），−8 到 1 eV
   - 轴向键与反位 Mn–OOH* 键的总 −ICOHP 与 dz² 分项（含 dz²–O pz）
   - Mn 局域磁矩
3. 输出 CSV/JSON 与原始路径；不平滑积分，从 ICOHPLIST 原始行求和，两自旋分别求和取负。
4. 【暂缓，等用户看完第1–3步数据再决定】出图草稿（保留现图6布局、配色、尺寸，只改相关面板）：
   - (a) 保留总 3d PDOS 与 εd，增加 Mn dz² PDOS（或 inset），标 dz² 中心
   - (b) 轴向键 −pCOHP 旁标注 dz² 分项 −ICOHP
   - 如需要，(e) Mn–OOH* 标注 dz² 分项
5. 写 REPORT.md：每个数值的来源路径、静态磁矩、是否同源。

## 不得写/做
- 不得写"竞争"或"轴向键被削弱"：T032 反证——OOH* 吸附后轴向 −ICOHP 2.64→3.00 eV 增大；加轴向 OH 后反位 OH* −ICOHP 2.70→3.06 eV 增大。两条反证须在报告中保留。
- 新增 dz² 面板只用 COHP 静态数据，不与 (a)(c) 的 Genkai 链数值混在同一面板。
- 不改 Word。

## 交付
FeCoMn/from_agent/FeCoMn-T037/（REPORT.md、数据、草图）。完成后 Claude Code 写 FeCoMn/review/T037_ClaudeCode.md。

---
## v3 修改要求（Claude，2026-11-19 17:44，用户已同意）
1. (a) FeCoMn–NC 的 3d 填充与 dz² 曲线、Mn–NC 的 dz² 曲线在约 +1.2 eV 截断：补全到 +4 eV。在 REPORT 写明 FeCoMn–NC 一行 3d 是否换了来源。
2. (c) 的 Mn–NC 改用 COHP 同源静态（IMR `FeCoMn_COHP_20261023/MnNC_base_full/`）的自旋分辨 3d PDOS，磁矩标同源值（+0.001 μB，显示为 0.00 μB）。FeCoMn–NC 若 (a) 已用 COHP 静态，(c) 同样统一；数值写入 REPORT。
3. 删掉 (a) 图例括号内的线型说明（"(εd --)"、"(εdz² ··)"），避免与面板标签 b 重叠。
4. REPORT 写明 (a) 中 3d 与 dz² 各自的归一化方式。
5. (f)(g) Bader 不动。
6. 图和图注中不出现任何计算来源说明；来源只写在 REPORT。
出 v3 到 draft_20261119_v3/，Claude Code 核查 Mn–NC −3.54/−5.12 eV 及 (c) 新磁矩是否同一 DOSCAR/OUTCAR。
