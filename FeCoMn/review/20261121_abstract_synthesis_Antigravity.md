# 六方评审全意见综合定稿摘要候选（Antigravity，2026-11-21）

综合对象：Antigravity（`99b6c33`）、Claude web（`b017666`）、Claude web 2（`42272b6` / `0b6cc1a`）、Claude Code 云端（`d516fce` / `6efcf94`）、Claude Code 本地（`230491a`）与 GPT（`1636324`）的 2026-11-21 评审与综合意见，结合前文全部核实数据边界。未修改 Word `.docx` 或配图文件。

---

## 一、全意见综合定稿摘要（215 词，单句均不超过 25 词）

### English Abstract

Metal particles commonly coexist with single-atom sites in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet catalytic models often rely on bare single-atom surfaces. How the surface state formed under working conditions governs oxygen reduction reaction (ORR) intermediate binding remains unclear. Here, we prepare an FeCoMn–NC catalyst combining FeCo alloy particles with dispersed Mn single atoms. In 0.1 M KOH, FeCoMn–NC delivers a half-wave potential of 0.885 V versus the reversible hydrogen electrode (RHE), surpassing commercial Pt/C, FeCo–NC, and Mn–NC. It also retains 96.5% of its initial current over 238 h. Operando infrared spectroscopy shows that interfacial species evolve with potential, indicating that the ORR proceeds on a covered rather than bare surface. Surface-coverage calculations at 0.78 V versus RHE reveal O*-covered FeCo particles and adjacent Mn single atoms carrying an axial OH. Without this axial OH, Mn binds ORR intermediates too strongly and impedes OH* removal. The axial OH pulls Mn out of the N₄ plane, and an ORR intermediate adsorbing on the opposite side draws Mn back toward the plane. This opposing displacement offsets part of the adsorption energy and moderates the overly strong binding. Consequently, OH* removal becomes downhill at 0.78 V while OOH* formation remains nearly thermoneutral. FeCoMn–NC therefore lies near the apex of the calculated activity volcano, consistent with its highest measured activity.

### 中文直译（零中文冒号、零分号、零破折号、零双引号）

金属颗粒通常与单原子位点共存于热解金属氮碳（M–N–C）催化剂中，但催化模型往往仍依赖裸露的单原子表面。工作条件下形成的表面状态如何支配氧还原反应（ORR）中间体结合仍不明确。本文中，我们制备了一种结合 FeCo 合金颗粒与分散 Mn 单原子的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的半波电位达到 0.885 V（相对于可逆氢电极 RHE），超过商业 Pt/C、FeCo–NC 和 Mn–NC。它在连续运行 238 h 后仍保持 96.5% 的初始电流。原位红外光谱显示界面物种随电位演变，表明 ORR 在被覆盖的表面而非裸表面上进行。在 0.78 V（相对于 RHE）下的表面覆盖度计算揭示了 O* 覆盖的 FeCo 颗粒以及带有轴向 OH 的相邻 Mn 单原子。没有该轴向 OH 时，Mn 对 ORR 中间体结合过强并阻碍 OH* 脱附。轴向 OH 将 Mn 拉出 N₄ 平面，而从对侧吸附的 ORR 中间体又将 Mn 拉回平面附近。这种反向位移抵消了部分吸附能，从而缓和了过强的结合。因此，在 0.78 V 下 OH* 脱附转为下坡，同时 OOH* 生成保持接近热中性。FeCoMn–NC 因而位于计算活性火山图顶点附近，与其最高的实测活性一致。

---

## 二、全团队 10 项核心分歧的综合裁决表

| 讨论焦点 | 各方主张 | 最终综合采纳 | 采纳理由 |
|---|---|---|---|
| **1. 开篇破题** | 方案二（Antigravity / GPT / Claude Code 本地 / Claude Code 云端 / Claude web）vs 方案一（Claude web 2） | **采用方案二** | 以「颗粒与单原子共存，但模型常假设裸表面 → 工作态表面如何调控结合」切入，既交代后面的颗粒背景、又把科学问题收束在工作态调控，不问颗粒因果，首尾严格对齐。 |
| **2. 术语与语法规范** | 冠词、缩写、位点命名统一 | `an FeCoMn–NC`、`reversible hydrogen electrode (RHE)`、`Mn single atoms`、删去未展开 `bcc`、全篇不用 `operating` | 与正文 `FeCoMn_Manuscript_revised_20261119_2255`、关键词及作者术语禁忌完全对齐。 |
| **3. 实验性能对照范围** | 保留三基准（`Pt/C, FeCo–NC, and Mn–NC`）vs 仅留 `Pt/C`（Claude web 2） | **默认保留三基准**（并留 3 词可选精简接口） | 实测半波电位排序不是机理对比，且能支撑结尾 `highest measured activity`；若定稿仍偏爱极简，直接删 `FeCo–NC, and Mn–NC` 并把末尾 `highest` 改 `high` 即可。 |
| **4. 原位红外表述边界** | 写 `OOH* formation / accumulation`（Gemini 原版）vs 写 `interfacial species evolve with potential`（Claude web / Claude Code 云端 / Claude web 2 / GPT + T043 复核） | **采用 `interfacial species evolve with potential`** | `1215 cm⁻¹` 与 Nafion C–F 重叠且 `T043` 实测同批双电极符号相反，不宜把 `OOH*` 定性负担压在摘要一句上；界面水（`3307/1633 cm⁻¹`）与总谱演变已足以支撑「反应发生在覆盖态表面」。 |
| **5. `0.78 V` 覆盖态归属** | 直接陈述 vs 明确由计算给出 | **`Surface-coverage calculations ... reveal`** | 避免被误读为原位实验直接测出 `Mn–OH`，并与 SI 两分支对照表（`23aa751`）口径一致。 |
| **6. 无 `OH` 对照句** | 保留 `Without this axial OH`（Antigravity / GPT / Claude Code 云端 / Claude web 2）vs 删去（Claude web） | **保留短句 `Without this axial OH...`** | 这是同一 `FeCo(8O*)` 模型有无轴向 OH 的内禀对照（`T032`，`U_L 0.52 → 0.78 V`），并非催化剂间横比，是引出「削弱过强吸附」不可或缺的逻辑起点。 |
| **7. Mn 回移终点用词** | `toward`（Antigravity / GPT）vs `into / to`（Claude web / Claude web 2 / Claude Code 云端） | **`draws Mn back toward the plane`** | `T042` 实测吸附后 `h_Mn` 为 `OOH* +0.003 Å`、`OH* −0.009 Å`、`O* −0.098 Å`（`O*` 略穿过平面），写 `toward` 对三者全部精确成立，且无 `must`。 |
| **8. 几何–能量机制句** | 避免 `structural reorganization`、`energetic penalty` 与 `without necessarily` 反驳句 | **`This opposing displacement offsets part of the adsorption energy and moderates the overly strong binding`** | 兼顾可观测几何位移与具体的吸附能抵消关系；主动舍弃 GPT `1636324` 中的 `without necessarily weakening`（用户已明确反感含糊或预先反驳句）。 |
| **9. 结尾与活性火山图** | Claude Code 本地 `230491a` 提醒核查火山图；Claude web 2 建议写 `consistent with` | **`near the apex of the calculated activity volcano, consistent with its highest measured activity`** | 已核查现稿 Figure 6h 为标准的 `U_L vs ΔG_(OH*)` 经典火山图，用 `calculated activity volcano` + `consistent with` 既呼应图 6h 又避免用计算值硬解释实验差幅。 |
| **10. 配套无 `Determine` 标题** | 协同替换现稿 `Determine` 与 GPT 的 `Operating-State` | ***Axial OH Formed under Working Conditions Moderates Intermediate Binding on Mn Single Atoms beside FeCo Particles for Oxygen Reduction*** | 同时移除两个禁词（`Determine` 与 `Operating-State`），主语「工作条件下形成的轴向 OH」与本摘要完全咬合。 |

---

## 三、规范与红线核查

- **硬禁词核对**：全篇英文不含 `operating` / `operating-state`、`structural reorganization` / `reconstruction`、`energetic penalty`、`must`、`dz²`、`Cdl`、`ECSA`、`Wan`、`0.49` / `0.96 V`、`without necessarily`。
- **句长与篇幅**：12 句短句，无 `> 25` 词长难句，共 215 词（< 250 词上限）。
- **中文直译**：零全角中文冒号、零中文分号、零破折号 `——`、零中文双引号。
