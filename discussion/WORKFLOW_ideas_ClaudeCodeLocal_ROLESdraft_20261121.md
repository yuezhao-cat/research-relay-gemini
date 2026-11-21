# AI 协作角色与工作流

本文件定义多模型科研协作的分工、验证规则和交接规范。
每个模型完成一个环节后，必须把状态写入仓库，不能只活在自己的上下文里。

---

## 角色定义

### 动手层（Execution）

| 角色 | 工具 | 主要职责 |
|---|---|---|
| Claude Code | claude-code CLI | 文件读写、脚本执行、git push、Word/图片操作、超算 SSH |
| Codex | OpenAI Codex | 代码生成、脚本调试 |
| Antigravity | Gemini CLI / research-relay agent | 文件读写、git push、VASP 计算投递与监控、数据核查 |

动手层的产物必须落在文件里（md/py/sh/docx/图片），并推到 GitHub，不能只停留在终端输出。

### 思考层（Reasoning）

| 角色 | 工具 | 主要职责 |
|---|---|---|
| Claude | claude.ai 网页 | 推理、拍板、写作润色、跨文件整合判断 |
| GPT | ChatGPT 网页 | 独立验证结论、文献逻辑核查、英文写作 |
| Gemini | gemini.google.com 网页 | 独立验证结论、机理逻辑核查、创新点挖掘 |

思考层不直接修改文件，输出意见后由动手层落地。

---

## 相互验证规则

同一个关键结论，必须经过至少两个不同家族的模型独立得出才算可信：
- Claude 家族（claude.ai / Claude Code / CCC）视为一个家族
- GPT 家族（ChatGPT / Codex）视为一个家族
- Gemini 家族（Gemini 网页 / Antigravity / Gemini CLI）视为一个家族

单家族共识不算交叉验证。

---

## 全流程分工

### 1. 文献调研与阅读

- 主导：思考层（Claude / GPT / Gemini 任一）
- 产物：`discussion/` 下的文献笔记 md 文件
- 验证：另一家族独立评估文献结论

### 2. 新 idea 生成

- 主导：思考层（三家独立提案，取交集或最优）
- 产物：`discussion/YYYYMMDD_idea_*.md`
- 决策：用户拍板后写入 `DECISIONS.md`

### 3. 实验方案与表征设计

- 主导：思考层出方案
- 产物：`to_agent/` 下的任务单
- 执行：动手层按任务单操作

### 4. 实验数据与表征分析

- 主导：动手层（Claude Code / Antigravity）读原始文件跑脚本
- 验证：另一动手层独立复算关键数字
- 产物：`from_agent/` 下的 REPORT.md

### 5. 画图

- 主导：动手层（Claude Code / Antigravity）
- 规则：按画图规则 md 执行，交付前逐面板核对
- 产物：png/svg 文件 + 对应版本 Word

### 6. 计算方案设计

- 主导：思考层（三家验证参数合理性）
- 产物：`to_agent/` 下的计算任务单（含 INCAR/KPOINTS 参数）

### 7. 超算投递与监控

- 主导：动手层（Claude Code / Antigravity，视 SSH 权限）
- 规则：投前过 AICC 检查，提交命令用 `< /dev/null`，place=pack:shared 必填
- 产物：STATUS.md 更新，作业号记录在任务单

### 8. 计算数据分析

- 主导：动手层读 OUTCAR/OSZICAR/LOBSTER
- 验证：另一动手层独立复算 ΔG/ICOHP 等关键数字
- 产物：`review/` 下的核查 md 文件

### 9. 整合数据 / 找创新点

- 主导：思考层（三家独立判断，取最强交集）
- 产物：`discussion/YYYYMMDD_innovations.md`

### 10. 写论文

- 起草：思考层（Claude / GPT / Gemini 各出一版）
- 落地：动手层（Claude Code）写入 Word，推 GitHub
- 验证：三家意见汇总后由用户决策，Claude Code 执行

---

## 交接规范

每个模型结束一个环节后，必须：

1. 把产物文件推到 GitHub（动手层）或告知动手层推送（思考层）
2. 在 `STATUS.md` 对应行更新状态
3. 重要决定写入 `DECISIONS.md`，不可撤销的边界写入共享记忆库

下一个接手的模型，读取顺序：`ROLES.md` → `STATUS.md` → `DECISIONS.md` → 对应任务文件。

---

## 基础设施位置

| 资源 | 位置 |
|---|---|
| 任务看板 | `STATUS.md` |
| 已定结论 | `DECISIONS.md`（待建） |
| 红线规则 | 共享记忆库 `D:\AI-Shared-Memory`（Claude Code 可读）|
| 仓库镜像（Gemini 用） | `github.com/yuezhao-cat/research-relay-gemini` |
| 画图规则 | `D:\OneDrive\1a1数据文档\07_规则与资料\画图规则调研_20260915\` |

---

*初稿：Gemini（2026-11-21 工作流设计），Claude Code 落地，赵月决策。*
