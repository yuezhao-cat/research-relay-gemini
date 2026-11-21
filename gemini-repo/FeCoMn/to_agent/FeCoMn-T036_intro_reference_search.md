# FeCoMn-T036：前言文献核查（原有文献为主，必要时补充）

发起：Claude，2026-11-19。负责：Claude Code；核对：ChatGPT（是否真支持）。

## 背景
前言按 discussion/20261119_intro_framework_final.md 逐段重写；文献可增删，不受现有编号限制。每段写好后，“需要文献的论断”列在 discussion/20261119_intro_v2.md 对应段下方，标 [A][B]…。

## 要做（赵月 12:07：以核查原有文献为主，不要整体替换）
1. **默认沿用原有文献**。讨论稿每句后已标注原文献编号的，逐篇核查是否直接支持该句：给出原文支持句（英文原句，注明页码或章节）和判断（支持／部分支持／不支持）。
2. **只有判定为不支持、或句子标 [字母] 尚无文献时**，才检索新文献：每个论断 1–3 篇最直接的原始研究或权威综述，给完整引文（ACS 格式）、DOI、支持原句。
3. 核对 DOI 能打开且与题目一致；不能编造。找不到直接支持的如实写“未找到”。
4. 先做第一段：核查 1、2、5、6，检索 [B]。

## 交付
from_agent/FeCoMn-T036/P1_refs.md（之后 P2_refs.md…）；更新 STATUS.md。不修改 Word 与讨论稿正文。

## 第二段（2026-11-19 13:40）
见 discussion/20261119_intro_v2.md 第二段“需要文献的论断”：核查 7、8 是否支持第二、三句（打开原文，引句逐字，注明页码；不能凭记忆）；为 [D] 检索三类调控方法的代表文献。交付 from_agent/FeCoMn-T036/P2_refs.md，之后由 Antigravity 复核（review/T036_P2_Antigravity.md）。

## 分工调整（2026-11-19 14:03 赵月）
- 第一、二段已由 Claude Code 完成，Antigravity 复核（第二段 P2_refs v2 0842ff4 待 Antigravity 复核，交 review/T036_P2_Antigravity.md）。
- **自第三段起由 Antigravity 主做**（交 from_agent/FeCoMn-T036/P3_refs.md…），**Claude Code 复核**（交 review/T036_P3_ClaudeCode.md…）。要求不变：打开原文，逐字引句并注明页码，不能凭记忆。
- 第三段待核：[E] 原 9–12、15、16；[F] 原 13、14（见 discussion/20261119_intro_v2.md 第三段）。

## 补充任务（2026-11-19 15:10，Antigravity 主做，Claude Code 复核）：第二段 [D] 碳骨架文献
现第二段首句（赵月定保留“碳骨架”）：
“Researchers have tuned the binding of ORR intermediates by modifying the coordinating atoms and carbon framework of M–N–C catalysts or by introducing neighboring metal species.”
- 配位原子：已有 4（Li 2018，MnNxCy 构型比较），可加 14（Zhang 2023 Nano-Micro Lett.，轴向配体）。
- **碳骨架：缺。** 请检索 1–3 篇直接证明“改变 M–N–C 的碳骨架（缺陷、曲率、杂原子掺杂、孔结构等）改变单原子对 ORR 中间体的吸附或 ORR 活性”的原始研究或权威综述。Claude Code 提过的候选：Adv. Mater. 2023, DOI 10.1002/adma.202301477（Zotero 无 PDF）、“Review of Carbon Support Coordination Environments for Single Metal Atom Electrocatalysts”、Cu–N–C “carbon matrix effect”。请先确认能否取得原文；取得的逐字摘录支持句与页码。
- 相邻金属物种：由第二句 7、8 支撑，首句可不重复引。
交付：from_agent/FeCoMn-T036/P2_D_carbon_refs.md；Claude Code 复核写 review/T036_P2D_ClaudeCode.md。
