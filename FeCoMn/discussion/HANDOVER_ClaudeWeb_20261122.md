# 交接：Claude web 卸任主写与主改（2026-11-22 13:52）

赵月决定：Claude web 不再担任主要写作和修改角色。接任者由赵月指定后，在 ROLES.md 中更新。

## 结论当前状态（详见 discussion/REQUEST_Conclusion_20261122.md）
- S1（定稿）：In summary, we determined the surface coverage of FeCoMn–NC, a catalyst combining FeCo alloy particles and Mn single atoms, under working conditions and thereby revealed how the FeCo alloy particles affect intermediate binding at the adjacent Mn single atoms.
- S2（四家选 A）：Experimentally, FeCoMn–NC reaches an ORR half-wave potential of 0.885 V versus RHE in 0.1 M KOH, outperforming Pt/C, FeCo–NC, and Mn–NC.（不写稳定性，赵月定。）
- S3（待改）：Calculations show that the O*-covered FeCo alloy particles keep an axial OH on the adjacent Mn single atoms at the working potential.
  赵月意见：keep（保持）不对；应体现 OH 主动吸附；要看正文怎么写；改动不要大。
  正文相关原句：图 6 段末 "O* and OH from the electrolyte adsorb on the FeCo particles and on the neighboring Mn, respectively, with the OH bound axially."；图 5 末 "The FeCo particles thus determine the surface coverage of FeCoMn–NC under reaction conditions, namely O* on the particles and an axial OH on the adjacent Mn single atoms."
- S4（定稿，乙）：The axial OH moderates the binding of ORR intermediates through electronic and geometric effects, placing FeCoMn–NC near the apex of the activity volcano.
- S5（多数采用 Claude Code 版，去掉 adjacent；范围待赵月最终确认）：The ORR activity of single atoms beside metal particles thus also depends on the particles, whose surface coverage under working conditions determines the axial ligand of the single atoms.
- 相关问题：摘要与前言第三段也用 keep an axial OH，是否同步改由赵月定。

## 文件版本
- 最新 Word：正文、SI 1140 版（标黄 / _clean / _for_HaoLi），在 Claude web 会话中生成并已发给赵月；未上传 GitHub。纯文本见 manuscript/。
- 1140 内容：Antigravity 2200 基础上标黄按词重核；图 4 去顶部空白；图注单倍行距；图注分图标号加粗；图 3g 去掉计时电流电压；图 6 图注精简、SI 2.13 补归一化句；30 条批注回复为一句话式（#310 展开）。
- 结论尚未放入 Word。

## 未完成事项
1. 结论 S3 改写并最终定稿，放入 Word，出新版（标黄、干净、给李昊老师三版）。
2. 前言 "These analyses considered only bare single-atom sites." 与 Wan 2022（ref 11）的轴向 OH 先例冲突，需改写。
3. SI 方法与图 S10 仍写 0.516 V，是否删除待定。
4. GitHub 历史中误传的 4 个 Word 文件（约 64 MB）是否清理，需赵月同意。
5. IMR 重复 T040 作业（622207、622219、622220、622221）是否取消，需赵月同意。

## 规则
- 写作规则与红线：REDLINES_FROZEN.md；DECISIONS.md；Gemini_brief_Conclusion_20261122.md 第 2 节。
- 赵月偏好：每次改 Word 存新版本；标黄只标改动的词且叠加保留；英文必附中文直译；修改给原文和改后版并用「」标出；批注回复口语、一句话说怎么改；结论和图注不讲细节、不列数字；动手前先问清楚，不自行扩大改动范围。
