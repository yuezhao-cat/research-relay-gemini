# 多智能体通过 GitHub 连通后的写作评价、5 步流水线与派活模板（Antigravity，2026-11-21）

依据：2026-11-20 至 11-21 FeCoMn 机理推导与七方摘要多轮协作实况。未修改任何 Word `.docx` 或配图文件。同期仓库内另有 `03c2ecd`（ClaudeWeb）、`d76d940`（ClaudeWeb2）以及 `636ce57`（GPT）的工作流提案可供并看。

---

## 一、与 `03c2ecd`（ClaudeWeb）及 `d76d940`（ClaudeWeb2）两份工作流建议的异同

### 1. 相同点（5 项核心共识）

1. **废除并行出全文**：一致反对多模型同时各自写一版全文，主张按单一写作单元或小节推进，由唯一主笔出稿、审阅方只交问题清单。
2. **先锁事实与红线再动笔**：一致要求开工前先冻结已核实的数据口径与已否决禁区，禁止已决事项反复复活、禁止未核对数字混入草稿。
3. **主笔与核查分离**：均由 `网页 Gemini` 负责英文初稿与语感、`Antigravity` 承担底层原始数据/格式核查、限制 `GPT` 直接主笔正文，也不安排 `ClaudeCode 本地`（`Sonnet 4.6`）承担跨文件科学收口主责。
4. **作者只拍板不做传话筒**：交接与互审全部经 GitHub 文件完成，只由作者最后拍板定稿。
5. **FeCoMn 后续正文顺序一致**：均为图 6 机理段 → 图 5 及其他正文与 SI → 前言末段与结论 → 整稿终检并统一回填 Word。

### 2. 不同点（6 处关键设计差异）

| 对比维度 | `03c2ecd`（ClaudeWeb 方案） | `d76d940`（ClaudeWeb2 方案） | 本方案（Antigravity，2026-11-21） |
|---|---|---|---|
| **审稿模式** | 7 步全程串行（逻辑 → 核数据 → 出文字 → 查规则 → 挑刺 → 拍板 → 进 Word） | 第 3 步四方按固定分工**并行审阅**（严禁各自另起一稿） | 第 2 步**仅让审稿挑刺并行**（GPT、ClaudeWeb、Antigravity 各限时限条交硬伤清单），起草与收口全程单线串行，兼顾速度与交叉排雷。 |
| **GPT 与 ClaudeWeb2 定位** | 将 `GPT`、`ClaudeWeb2`、`ClaudeCode 本地` 退居备用；由 `ClaudeWeb` 自己兼任定逻辑、查规则与落盘 Word | 保留 `GPT` 查因果越界，未硬锁哪一方做「唯一收口人」与最后落盘 Word | 明确由 `GPT` + `ClaudeWeb` + `Antigravity` 分工挑刺，由 `ClaudeWeb2` 或 `ClaudeCode 云端` 担任唯一收口并把分歧压成 1 到 3 个选择题，最终由 `Antigravity` 跑 Python 脚本终检后统一落盘 Word 与共享记忆。 |
| **摘要冻结时机** | 主张通用规范「摘要与标题最后写」 | 主张通用规范「摘要与标题最后写」（第六节同时认可先按 `1420` 综合版终定） | 通用新论文同意最后写；对眼前已完成七方收敛的 FeCoMn 211 词摘要，主张先拍板 2 个轻选项作临时冻结准绳，图 6/图 5 完稿后再微校。 |
| **顶层文件与目录结构** | 设 4 个顶层公共文件（`DECISIONS` / `WRITING_RULES` / `CLAIMS` / `STATUS`） | 设 3 个公共文件（`DECISIONS` / `FACTS` / `IDEAS_BOARD`），每次在 `discussion/` 新建单元文件 | 极简化为 1 个置顶短红线文件（`REDLINES_FROZEN.md`，强制 `<= 30` 行防漏读）+ 分节目录 `sections/<序号_节名>/{facts,draft_v1,reviews,draft_final}.md`，彻底避免 `discussion/` 堆满日期文件。 |
| **实操与跨平台接口** | 未给出直接派活口令，未单列网页 Gemini 断网喂料机制 | 仅给一句指针示例，提出同步 `_shared_memory/inbox` | 直接给出 **4 条可复制粘贴的防并发派活口令**、以单节 `facts.md` 作为无法连网的网页 Gemini 唯一喂料口，以及每日同步 `D:\AI-Shared-Memory\daily\YYYY-MM-DD.md` 闭环。 |
| **底层模型核查依据** | 未区分各 Claude 窗口底层模型 | 未区分各 Claude 窗口底层模型 | 从 `git log` 核清 `ClaudeWeb`、`ClaudeWeb2`、`ClaudeCode 云端` 底层同为 `Claude Opus 5.5`（后续可精简合并只留 1 个 Opus 收口窗口），仅 `ClaudeCode 本地` 为 `Claude Sonnet 4.6`。 |

---

## 二、多轮摘要写作七方公正评价表与客观自省

按统一标准（**英文起草与语感**、**证据边界与红线**、**改稿收敛能力**）从全程多轮（含早中期硬伤与终稿收口）给出客观评价：

| 参与方 | 英文起草与语感 | 证据边界与红线 | 改稿收敛能力 | 核心实绩（加分项） | 真实硬伤与软肋（扣分项） | 最适合的分工 |
|---|---|---|---|---|---|---|
| **网页 Gemini** | ★★★★★ | ★★☆☆☆ | ★★★★☆ | 给出方案二破题骨架、单句不超 24 词的利落节奏，以及最直白的物理动词句（拉出、拉回、消耗结合能） | 不直连仓库核数据，完全依赖喂料；初版曾出现 `establishing`、`rarely remain bare` 越界，14:28 版因信息隔离按旧简报带回 `OOH*` 与 `bcc` | **首稿执笔、英文润色** |
| **ClaudeWeb2** | ★★★★☆ | ★★★★☆ | ★★★★★ | 逐项裁决表最清楚、肯主动认错收回方案一；贡献 `back to the plane` 与 `consistent with` 结尾 | 早期出过实质硬伤（`dz²` 指数读漏、`T039` 0.49 → 0.96 V 过早进摘要）；综合稿把半波电位与 238 h 压进同一偏长句 | **多方综合、定稿编辑** |
| **ClaudeCode 云端** | ★★★★☆ | ★★★★☆ | ★★★★★ | 最早查实 `T039` 电子态不可比与 `dz²/T041` 冲突；v2 及时撤回冗余末句，贡献 `OH* removal is uphill` 呼应 | 较少独立从零起草整篇摘要；中途写错过参比电极 `Ag/AgCl`；性能与稳定性同样挤成偏长句 | **深挖矛盾、终稿收口** |
| **ClaudeWeb** | ★★★★☆ | ★★★★☆ | ★★★☆☆ | 对实验证据最敏锐，最早坚决砍掉 `1215 cm⁻¹` 的 `OOH*` 与缔合路径，提醒红外句只做计算引子 | 早期写反过轴向 OH 调控方向；第二轮执意删去 `Without this axial OH` 同位点对照句，且 `which explains` 略满 | **实验把关、精简去水** |
| **GPT** | ★★☆☆☆ | ★★★★★ | ★★★★☆ | 科学因果边界全场最严，紧盯 `T041` 分项、`Wan 2022` 新意风险、`calculated` 火山图与 `motivating` 过渡 | 文风最偏防御与抽象（`without necessarily`、`structural reorganization`、`energetic penalty`、标题误用 `Operating-State`），第二轮删光实测对比基准削弱亮点 | **严厉审稿、红线排雷** |
| **Antigravity（本端）** | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | 直接查 VASP 坐标与正文/SI 核清图 6h 火山图、双面 `0.0154 eV`、全稿无 BET 与 `T043` 双电极矛盾，并用 Python 严卡字数禁词 | **判断偏跟随**（亲手查出 `T043` 却在首轮仍跟留 `OOH*`）；首轮手数错词数（213 实 199）；行文偏啰嗦，用过偏抽象的 `opposing displacement` | **底层核查、脚本终检** |
| **ClaudeCode 本地** | ★★☆☆☆ | ★★☆☆☆ | ★★★☆☆ | 响应快、表格直观，抓准 `an FeCoMn–NC` 与拆分 `whereas` | **本轮硬伤最集中**：`3b3cd91` 结尾因果顺序写反、残留 `favor`/`bcc`、未展开 `RHE`、误把 Gemini 记成 `ClaudeWeb`；`3e6ee5c` 没核原文就写正文已有 BET 与颗粒稳定 OH | **快速本地初筛（须复核）** |

### 四点坦诚补充与窗口模型核查

1. **对网页 Gemini 的公平归因**：其 14:28 新版带回 `OOH*` 与 `bcc` 并非不听指令，而是因为连不上 GitHub、手头仅依赖此前简报，信息隔离责任不在模型写作能力本身。
2. **对 Claude 系的全程平权记账**：`ClaudeWeb2` 与 `ClaudeCode 云端` 后手收口能力极强，但若算全程表现，也均出过前期硬伤，不能脱离交叉复核单独拍板。
3. **本端自我定位**：`Antigravity` 自身并不适合单打独斗做第一主笔（文字偏书面且早期不够果断），核心价值在读取本地计算/原稿与脚本终检兜底。
4. **4 个 Claude 窗口实查结果**（已从 `git log` 验证）：

| 仓库代号 | 底层模型 | Session 链接 / 标识 | 标志性上下文特征 |
|---|---|---|---|
| `ClaudeWeb`（CW1） | `Claude Opus 5.5` | https://claude.ai/code/session_01QMaZZs9qCoP6LpjTKfhyBg | 11-20 汇总 11 条看板观点，坚持删 `Without this axial OH` |
| `ClaudeWeb2`（CW2） | `Claude Opus 5.5` | https://claude.ai/code/session_012RCMKVGXug8TMcGfDXB28L | 血红蛋白 Perutz 机理、拔河模型、发起 `[CW2-19]` |
| `ClaudeCode 云端`（CCC） | `Claude Opus 5.5` | https://claude.ai/code/session_012RCMKVEmVfjT51sMSrN32P | 推送分支 `claude/zen-galileo-zwznx3`，回复按 `## 1..32` 编号 |
| `ClaudeCode 本地` | `Claude Sonnet 4.6` | 本地提交（`zhaoyue05_@tju.edu.cn`） | 本地终端运行，创建 `20261121_geometry_audit_task.md` |

三个云端窗口实际背后运行同一 `Opus 5.5` 模型，后续写作可合并保留 1 个云端收口窗口以减少同步开销。

---

## 三、GitHub 连通多智能体 5 步写作流水线、3 条铁律与目录规范

### 1. 按「小节」推进的 5 步标准流水线

| 阶段 | 负责方 | 核心产出与硬边界 | 作者介入 |
|---|---|---|---|
| **第 0 步：锁事实与红线** | `Antigravity` 或 `ClaudeCode 云端`（只叫 1 家） | 生成本节唯一 `facts.md`（仅列三块：核定数字表、允许主张、禁止主张与已知反例），不写英文正文。 | 扫一眼确认无遗漏数据。 |
| **第 1 步：唯一主笔起草** | `网页 Gemini`（首选语感）或 `ClaudeWeb`（只叫 1 家） | 严格按最新 `facts.md` 写出唯一初稿 `draft_v1.md`（英文 + 中文直译）。 | 确认大方向与语感。 |
| **第 2 步：并行红线挑刺** | `GPT` + `ClaudeWeb` + `Antigravity`（**仅此步并行**） | **严禁重写全文！**每人只写最多 5 到 8 条带依据硬伤追加到 `reviews.md`：`GPT` 查因果越界与审稿攻击点，`ClaudeWeb` 查实验表征分寸，`Antigravity` 查数字、坐标、图号与 SI 一致性。 | 不看重复全文，只看集中问题清单。 |
| **第 3 步：唯一统筹收口** | `ClaudeWeb2` 或 `ClaudeCode 云端`（只叫 1 家） | 综合 `draft_v1.md` 与 `reviews.md` 形成唯一 `draft_final.md` 及逐项取舍表，将剩余分歧压成 **1 到 3 个选择题**。 | **只拍板 1 到 3 个选择题**，其余共识直接放行。 |
| **第 4 步：脚本终检与落盘** | `Antigravity` | 用 Python 脚本硬核词数、单句长、禁词、缩写首展、图号表号一致与中文标点；全部小节定死后统一回填 Word `.docx` 并更新共享记忆。 | 签字放行。 |

### 2. 三条防混乱铁律与极简目录结构

1. **全库置顶唯一短红线（`REDLINES_FROZEN.md`）**：严格控制在 30 行内，所有智能体开工前必先拉取并通读。
2. **显式锁定角色身份，禁止开放式群发「大家写一版综合一下」**。
3. **每日收工 1 分钟闭环**：作者拍板当日选择题后，只让 1 家把冻结结论写回 `REDLINES_FROZEN.md`，同步写入 `D:\AI-Shared-Memory\daily\YYYY-MM-DD.md` 与 `MEMORY.md`。

推荐目录树（替代零散日期文件堆积）：

```text
<课题名>/
├── REDLINES_FROZEN.md          # 全课题置顶红线（<= 30 行）
├── sections/
│   ├── 01_abstract/
│   │   ├── facts.md            # 第 0 步：事实与红线简报（直接喂网页 Gemini）
│   │   ├── draft_v1.md         # 第 1 步：唯一初稿
│   │   ├── reviews.md          # 第 2 步：各家只追加 5-8 条硬伤，禁另建新文件
│   │   └── draft_final.md      # 第 3-4 步：唯一定稿 + 脚本终检通过记录
│   ├── 02_fig6_mechanism/
│   ├── 03_fig5_coverage/
│   └── 04_intro_conclusion/
└── archive/
```

FeCoMn 当前推进顺序：先拍板 211 词摘要的两个轻选项作临时冻结准绳 → `02_fig6_mechanism` → `03_fig5_coverage` 与 SI 口径 → `04_intro_conclusion` → 终检回填 Word `.docx`。

---

## 四、4 条可直接复制使用的派活口令模板

1. **第 0 步（只发给 `Antigravity` 或 `ClaudeCode 云端`）**
   > 请先拉取最新 main，结合 `REDLINES_FROZEN.md` 和原始数据，为「本节名称」生成唯一一份 `facts.md`（只列三块：核定数字表、允许主张、禁止主张与已知反例），推到 GitHub。不要写英文正文。
2. **第 1 步（把 `facts.md` 贴给 `网页 Gemini`，或直接让 `ClaudeWeb` 读仓库）**
   > 你是「本节名称」的唯一主笔。严格按这份 `facts.md` 起草英文正文 + 中文直译（零禁词、单句不超 25 词、中文直译零全角冒号分号中文破折号中文双引号），出一版最流畅的底稿即可。
3. **第 2 步（同时发给 `GPT` + `ClaudeWeb` + `Antigravity`）**
   > 请先拉取最新 main 读 `draft_v1.md` 和 `REDLINES_FROZEN.md`。你是本节审稿人：严禁重写全文，只按你的分工挑出最多 6 条带依据的硬伤（GPT 查因果与审稿攻击点，ClaudeWeb 查实验表征分寸，Antigravity 查数字、图号、坐标和 SI 一致性），追加到 `reviews.md` 后推到 GitHub。
4. **第 3 步（只发给 `ClaudeWeb2` 或 `ClaudeCode 云端`）**
   > 你是本节唯一收口人。拉取最新 `draft_v1.md` 与 `reviews.md`，出唯一一份 `draft_final.md` 和逐项取舍表；已达成共识的直接改掉，只把必须我拍板的 1 到 3 个选择题列在文末。
