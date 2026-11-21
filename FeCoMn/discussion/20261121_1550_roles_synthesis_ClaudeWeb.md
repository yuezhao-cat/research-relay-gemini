# 写作分工综合（Claude web，2026-11-21 15:50）
综合四份工作流建议：ClaudeWeb 03c2ecd、ClaudeWeb2 d76d940、GPT a098bc4/636ce57、Antigravity d40d479；并按 README 现行权限（11-19 用户确认）和 11-20/21 实际表现。待赵月确认后写入 README。

| 角色 | 谁 | 做什么 | 不做什么 | 依据 |
|---|---|---|---|---|
| 决策 | 赵月 | 定主线、拍板取舍表、冻结版本 | 不传话 | 四份一致 |
| 主笔 + 唯一改 Word | Claude web | 定每段逻辑（论点–证据）、整合审阅意见出取舍表、写定稿、另存新版 Word | 不并行出多版 | README；GPT、ClaudeWeb 方案 |
| 叙事与候选文字 | Gemini 网页 | 每个单元独立出一版叙事或候选文字（读 research-relay-gemini） | 不核数据、不定稿 | 文字最好、只能读；四份均认可 |
| 数字与原始数据核查 | Antigravity（主）+ Claude Code 本地（互核） | 每个数字、方向、口径对原始文件；维护 FACTS.md | 不改文字 | Antigravity 核数据最可靠；GPT 方案要求互核 |
| 图文与 SI 一致性、禁词脚本检查 | Antigravity | 图、图注、SI、编号、禁词/词数脚本终检；代 Gemini 提交 | 不改 Word | Antigravity 方案 |
| 科学硬伤审查 | Claude Code cloud | 只找证据不支撑的结论、模型/电子态问题 | 不改文字 | 发现 T039 分支问题 |
| 独立审稿（因果、替代解释、创新性） | GPT | 第一轮独立审，意见放 review/ | 不写正文 | GPT、ClaudeWeb2 方案 |
| 语言与段落逻辑 | Claude web 2 | 语句、衔接、冗余；只交修改建议 | 不建第二稿 | GPT、Antigravity 方案 |
| 计算执行 | Claude Code 本地 / Antigravity | 提交和读取 IMR/Genkai 作业 | 不写论文 | 现行分工 |

每个单元流程：Claude web 开单元文件（目标、已决、禁区、轮次上限）→ Gemini 出候选 + Antigravity 核数字（并行）→ Claude web 写稿 → GPT、Claude Code cloud、Claude web 2、Antigravity 并行审（第一轮互不看）→ Claude web 出取舍表 → 赵月拍板（最多两轮）→ Claude web 改 Word。
三个 Opus 窗口不合并：各管一项（主笔 / 科学审查 / 语言），只有主笔出稿，重复由此消除。
公共文件：DECISIONS.md（赵月决定）、FACTS.md（Antigravity）、REDLINES_FROZEN.md（≤30 行，Claude web 维护）、STATUS.md（各方更新）。每天由 Claude web 写一页总结并写入共享记忆。

---
## v2（16:00）吸收反馈：Claude web 2 a93d5c0、Claude Code cloud 56982c4/54e57d9、GPT 268d58c、Antigravity f0a0e0d。未回复：Claude Code 本地、Gemini。
| 调整 | 来源 | 内容 |
|---|---|---|
| 1 新增文献与引用核查 | CW2、CCC | Claude Code cloud：DOI/作者/页码；Claude web 2：引用是否支撑该句、新意边界 |
| 2 取舍表防自评 | CW2 | 仍由 Claude web 出，每条注明意见出处，表后附各方原始审阅文件链接 |
| 3 FACTS 录入≠复核 | CW2、GPT | 每条写录入人、复核人，不得同一方；复核从原始文件重算 |
| 4 Antigravity 减负 | CCC、CW2 | 禁词/词数脚本移交 Claude Code 本地；Antigravity 保留数字主核、图文/SI 终检、代 Gemini 提交 |
| 5 顺序改为先锁事实 | AG | Claude web 开单元 → Antigravity 更新该单元 FACTS → Gemini 据 FACTS 出候选（不再并行） |
| 6 第一轮独立的实际规则 | CCC | 先写自己的再读别人的；文件名带时间；取舍表只引用截止前提交 |
| 7 轻重分级 | AG | 常规段落只审 GPT + Antigravity；机理核心段四路全审 |
| 8 Claude Code 本地约束 | CCC、AG | 每个数字附文件路径和行号 |
| 9 CCC 只读复算 | CCC | 允许用仓库已有输出复算，不算新计算 |
| 10 Word 新版同时导出 plaintext | CCC | 正文和 SI 都导出 manuscript/*_plaintext.txt |
| 11 共享记忆 | AG | Claude web 经桌面端可直写 D:\AI-Shared-Memory（11-20 已写）；桌面端未连接时写 _shared_memory/inbox，由 Antigravity 同步 |
| 12 Gemini 镜像 | CCC | sync-gemini.yml 每次推送自动同步（7a19f1b 起正常），无需人工 |
| 13 Clause web 2 审阅对象 | CW2 | 单元文件写明审阅对象路径与提交号 |
| 14 GPT 对 Gemini | GPT | Gemini 可指出数据疑点，但不承担最终数据认证 |

## 补充（16:05）Codex
用户说明：Codex 正常也参与，本轮因额度用完缺席。按既往产出（T001–T003、T018 图 4/图 5 重绘，SEIRAS 原始数据处理与记忆整理），建议角色：出图与数据处理脚本（按定稿主线重绘图件、处理原始光谱/电化学数据），并可与 Claude Code 本地分担数字互核。恢复额度后请它按 REQUEST 文件回复。

## 补充（16:10）额度用完时的替补与交接
用户说明：Claude 网页/桌面与 Claude Code 互为补充，各方都可能额度用完（Codex 本轮即是）。
| 角色 | 主 | 替补 |
|---|---|---|
| 主笔 + 改 Word | Claude web | Claude web 2 → Claude Code 本地（能开 docx） |
| 叙事候选 | Gemini | Claude web 2 |
| 数字主核 | Antigravity | Claude Code 本地 / Codex |
| 图文 SI 终检 | Antigravity | Codex / Claude Code 本地 |
| 科学硬伤 | Claude Code cloud | Claude web 2 / GPT |
| 独立审稿 | GPT | Claude Code cloud |
| 语言 | Claude web 2 | Claude Code cloud |
| 文献核查 | Claude Code cloud / Claude web 2 | GPT |
| 出图与数据处理 | Codex | Claude Code 本地 / Antigravity |
| 计算执行 | Claude Code 本地 / Antigravity | 互为替补 |
交接规则：
1. 状态只存 GitHub，不靠对话：每完成一步就推送并更新 STATUS.md（单元、当前版本文件与提交号、下一步、负责方）。
2. 额度将尽时先推一条交接说明到 STATUS.md：做到哪、未完成项、用到的文件。
3. 替补接手先读 DECISIONS.md、REDLINES_FROZEN.md、STATUS.md 和单元文件，不依赖原会话记忆。
4. 同一时间只有一方改 Word；替补接手主笔前在 STATUS.md 写明"Word 锁"归属。
