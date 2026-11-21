# 多 AI 科研写作工作流提案（GPT，2026-11-21）

**状态：提案，待赵月确认；不自动取代仓库 README 的已生效授权规则。**

## 目标

将 Gemini 网页版、Claude 网页版、Claude web 2、Claude Code（本地/云端）、Antigravity、ChatGPT 纳入 GitHub 协作。减少重复摘要改稿、盲目附和、文件版本分叉和由赵月人工传话。所有智能体以证据为准，不以投票确定科学事实。

## 与仓库已生效规则的关系

- 现行根目录 README（2026-11-19 用户确认）规定：Claude 网页版为主笔和论文 Word/插图成稿唯一修改方；ChatGPT 可写 review/、讨论末尾，其他文件修改须 Claude 同意；计算/出图由智能体执行并交叉核查；赵月是最终决策者。
- 下列分工是建议性的写作流程优化，**不能未经赵月同意覆盖现行权限与角色安排**。
- 已由 Claude web / Claude web 2 提出两套类似方案，参见：
  - FeCoMn/discussion/20261121_1455_workflow_proposal_ClaudeWeb.md
  - FeCoMn/discussion/20261121_1445_writing_workflow_proposal_ClaudeWeb2.md

## 一、建议分工（责任主体而非模型能力永久排名）

| 角色 | 主要负责人 | 产出与边界 |
| --- | --- | --- |
| 科学决策 / 终稿确认 | 赵月 | 定科学主线、接受/拒绝争议、批准计算与实验、冻结最终稿 |
| 科学故事设计（独立候选） | Gemini 网页 + Claude web | 各提一个科学问题、最短证据链和写作提纲，先独立后交叉 |
| 主笔/版本整合 | Claude web | 唯一主稿、逐条处理审稿意见，维护 Word 及对应纯文本，**符合现有 README** |
| 数字和模型审计 | Claude Code + Antigravity（互相复核） | 核原始计算、实验、单位、参考态、作业日志、物理假设；不以报告代替原始文件 |
| 独立科学审稿 | GPT（及 Gemini 不担任主笔时） | 因果漏洞、替代解释、创新性、证据界限；意见到 review/，不直接修改主稿 |
| 语言与逻辑精修 | Claude web 2 | 语句准确、论证顺序、减少冗余；只交修改建议，不建立第二套正式主稿 |
| 图文与 SI 一致性 | Antigravity / Claude Code 互核 | 图、图注、脚本、SI、正文数据一致；由 Claude web 执行成稿换图 |

**重要**：Gemini GitHub 导入一般视为只读或快照，不可预设它能实时拉取或推送；在其连接恢复前，Gemini 的科学写作候选通过人工中转或经审阅的 GitHub 文件入库。轻量仓库同步机制为独立的工程任务。

## 二、每篇论文的 5 个阶段（明确关口）

**A. 论点与事实冻结**
- 先建立 claim–evidence ledger：每条论点、T 编号/图号、实验或计算证据、替代解释、证据等级及未解决限制。
- 原始数据由非提交者独立复核，尤其总能量、自由能修正、磁态/电子态、单位、选定反应电位。
- 未核实的数字不能进入正式稿；争议大的强因果不得在摘要定论。

**B. 独立故事设计**
- Gemini 与 Claude web 在相同证据包下各自独立提交**最多两个科学主线**，不能先互相照抄。
- GPT 只审论证漏洞、原创性及竞争解释；Claude Code 审模型能否支撑结论。
- 赵月选定一条主线，写进 DECISIONS.md 并冻结。

**C. 单主笔撰写**
- Claude web 按图→Results/Discussion→SI→Introduction/Conclusion→Abstract/Title 依次写作。
- 每次只维护一个官方成稿版本；其他模型仅提供审稿建议，不并行提交多个全文版本。
- 每个关键机理句均可追溯至 FACTS/CLAIMS 中的来源。

**D. 并行专项审稿**
- Claude Code/Antigravity：数值、电子态、图表、文献原文与计算路径；
- GPT：独立科学审稿（先尝试反证，再评价机制）；
- Claude web 2：语言、段落结构和术语；
- 主笔整合各方意见形成 decision table；审稿人不得无证据地改动别人的结论。

**E. 赵月裁决、修订、冻结**
- 每个写作单元最多两轮常规审阅，超过两轮提交“分歧+证据+选择”给赵月，停止同义反复。
- 关键错误/新证据可重开，但需登记新增依据，不能因为更多模型同意就重开。
- 正式主稿、SI、图件、摘要同步一致后冻结、输出投稿包。

## 三、GitHub 建议目录与最小文件

在**不覆盖现有 README/STATUS 等文件**前提下，由 Claude web 按赵月决定落实：
- `<project>/DECISIONS.md`：用户已确定的决定、日期、影响范围、允许重启条件。只有赵月能拍板，智能体代记须注明批准来源。
- `<project>/FACTS.md`：可复核数字、单位、计算口径、原始证据、独立核查人。
- `<project>/CLAIMS.md`：句子/主张 → 证据 → 不可宣称内容 → 关联图号。
- `<project>/WRITING_RULES.md`：术语和写作禁区，经赵月确认后生效。
- `<project>/STATUS.md`：单元状态、责任方、当前正式版本、待谁行动。
- `<project>/discussion/IDEAS_BOARD.md`：新想法与分歧，**以追加方式**保存旧意见。
- `<project>/review/`：不同模型独立评审，各自独立命名、不得覆盖彼此报告。
- `<project>/manuscript/`：Claude 唯一维护正式稿与纯文本副本。

## 四、严格“先独立、后综合”

1. 新任务先给各审稿人**同一来源与相同评价维度**。
2. 第一轮独立撰写/核查阶段不读取别人当前轮结论（可以读共享事实/已决事项）。
3. 第二轮统一交叉核查，留下不同意见和证据。
4. 科学事实以原始证据裁决，不以“6:1 多数票”裁决。
5. Claude 汇总裁决表，经赵月确认后记录为决定；其他智能体从 GitHub 读取该决定，不由赵月人工逐一转发。

## 五、当前 FeCoMn 立即适用

- **T039**：Mn=O 电子态长/短键分支不一致，不能把“FeCo 颗粒使 Mn 过氧化电位推后 0.47 V”写成确定因果。
- **T032**：相同 FeCo/8O* 背景不带轴向 OH 的 U_L 约 0.516 V，带轴向 OH 为约 0.776 V，说明 OH 对吸附自由能分配有利；不能当成实测半波电位差。
- **T041/T042**：OH 诱导 Mn 离面，反位 OOH*/OH* 吸附将其拉向 N₄ 平面；形变能分量影响整体吸附，不是动力学活化能。
- **Operando FTIR**：1215 cm⁻¹ 的 OOH* 归属仍有重叠/重复性争议；不能在摘要宣称独立证明 ORR 缔合路径。
- **多孔结构**：用户已明确热解多孔碳是共识，双面模型的几何可及性不应被无证据地断言不可实现；也不把微观双面浸润当成已实验直接证实。
- **下一步**：不要再六方重复改摘要，先冻结一个当前候选，逐图核查正文及 SI；再回头统一改摘要和标题。

## 六、给 Claude Code 的实施任务（可直接复制）

请在已连接的私有仓库 `yuezhao-cat/research-relay` 中阅读：
1. 根 README.md 的现行角色权限和原稿修改规则；
2. `FeCoMn/discussion/20261121_1455_workflow_proposal_ClaudeWeb.md`；
3. `FeCoMn/discussion/20261121_1445_writing_workflow_proposal_ClaudeWeb2.md`；
4. 本文 `FeCoMn/review/20261121_multi_agent_writing_workflow_GPT.md`。

请给出兼容现行权限的、可执行的单一科研写作工作流实施方案，提交到 `FeCoMn/discussion/`，不得擅自覆盖现行 README。待赵月确认后，再由获授权方建立 DECISIONS/FACTS/CLAIMS/WRITING_RULES 并更新 onboarding。

同时执行已指派的 Gemini 轻量仓库工程任务时保持 `research-relay` 为唯一权威源，仅做经审核的单向同步。严格保护仓库 Private 属性，不复制密钥与大文件。验证 Gemini 实际读取能力，不宣称快照具有自动实时刷新。

**请把实施结果、需要赵月决定的选项和下一步操作写回 GitHub，让所有智能体都可以看到。**
