# FeCoMn-T044：图 6i 示意图更新 + SI 图 S31（Claude web 派单，2026-11-21 17:35）
赵月决定（17:33）：图 6 只改 6i 示意图（方案 A），其他放 SI。
执行：动手池（Codex 额度不足时由 Claude Code 本地或 Antigravity 认领，在 STATUS.md 写明）。复核：另一动手方从源数据核对。不改 Word（由 Claude web 换图）。

## 1. 图 6i 更新（底稿：from_agent/FeCoMn-T034/draft_20261118_v38_axial_parentheses/）
- 版面、配色、字号、其他面板 a–h 一律不动，只改 6i。
- 6i 内容：FeCo 颗粒表面 O*；相邻 Mn 带轴向 OH，Mn 略凸出 N4 平面偏向 OH 一侧；ORR 中间体在另一侧吸附，Mn 被拉回平面，用箭头表示 Mn 的位移；不标数字。
- 交付：600 dpi PNG、可编辑 SVG、源文件与脚本；附与 v38 的像素差异检查（a–h 应为 0 差）。

## 2. SI 图 S31（新）
- (a) Mn 离 N4 平面高度：带 OH 与不带 OH，吸附前与吸附 OOH*、O*、OH* 后（数据：from_agent/FeCoMn-T042_Mn_position/Antigravity.csv、ClaudeCode_cloud.csv；正值指向轴向 OH；8O 模型无"不带 OH + OOH*"，该点取 clean 模型并在图注注明或不画）。可在 Antigravity_Mn_position.png 基础上改。
- (b) 吸附能拆分柱状图（T041，静态 ΔE，相对同模型不带轴向 OH）：OH*：总 +0.336、结构形变 +0.236、电子 +0.100；OOH*：总 +0.267、结构形变 +0.432、电子 −0.100、吸附物形变 −0.065（eV）。数据：from_agent/FeCoMn-T041/REPORT.md。
- 风格与 SI 现有计算图一致。交付 PNG/SVG/脚本/源数据 CSV。

## 3. 表 S11（Claude web 自写进 SI，不需动手池）
吸附能拆分数值与不带 OH 的 U_L 0.52 V。

交付到 from_agent/FeCoMn-T044/，REPORT.md 写明数据来源路径与复核人。


## 更新（18:58，赵月同意）
SI 中该图已由 Claude web 按 T041/T042 数据画好并放入 1850 版 SI，编号为图 S30（不是 S31）：from_agent/FeCoMn-T044/FigS30_ClaudeWeb_draft.png。
本任务改为两件事：
1. 改 6i（要求同上第 1 节）。
2. 复核图 S30：逐个数值对照 from_agent/FeCoMn-T042_Mn_position/Antigravity.csv（8O 模型：带 OH 基态 +0.442，OOH* +0.003，O* −0.098，OH* −0.009；不带 OH 基态 −0.010，O* −0.406，OH* −0.456；不带 OH 的 OOH* 在 8O 模型未算，标 n/a）与 from_agent/FeCoMn-T041/REPORT.md（OH*：+0.336/+0.236/+0.100/0.000；OOH*：+0.267/+0.432/−0.100/−0.065 eV）；同时核 SI 表 S7、表 S11 的数值。结论写入 review/。原第 2 节"SI 图 S31（新）"作废。
