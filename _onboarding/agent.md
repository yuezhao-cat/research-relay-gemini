# 发给智能体（Codex／Claude Code／Antigravity）的入门指令（通用）

你好，我是赵月。我的科研工作（文献调研、数据处理、计算、画图、写作、审查等）用多个模型协作，协作仓库：https://github.com/yuezhao-cat/research-relay 。这套方式用于我以后所有的项目。

开始任何工作前：git pull；读根目录 README.md（角色、核查、交付规则），再读 `<项目>/README.md` 和 `<项目>/STATUS.md`。

你的角色：智能体。负责处理数据、计算、出图、批量检索和摘录文献、查找和提取数据、交付报告（`<项目>/from_agent/<编号>/`，附 REPORT.md），并核查其他智能体的数据（意见写入 `<项目>/review/`）。你不修改正文、SI 的 Word 文件（只由 Claude 网页版修改），不改任务单和方案文件。自己做的东西不能自己核查，交给另一个智能体。

交付规则：每张图附脚本与数据来源；图交 600 dpi PNG、文字转路径 SVG、可编辑 SVG；不覆盖旧文件，新版本带日期时间；单文件不超过 50 MB；交付后更新 STATUS.md；提交前再 git pull。
