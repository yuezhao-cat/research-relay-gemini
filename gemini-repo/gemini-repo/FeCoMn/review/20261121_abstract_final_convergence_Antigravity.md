# 七方最终收口定稿摘要与多轮核查备忘（Antigravity，2026-11-21）

综合对象：网页 Gemini 14:28 新版 213 词摘要、`ClaudeWeb`（`22c6f52`）、`ClaudeWeb2`（`0b6cc1a` / `2c2bb14`）、`ClaudeCode` 云端（`5fcbcfc`）、`GPT`（`ab9b579`）、`ClaudeCode` 本地（`3b3cd91` / `3e6ee5c`）、`Antigravity`（`d7a83ac`），以及已闭环的 `CW2-19` 多孔碳双面可及性共识。未修改任何 Word `.docx` 或配图文件，未提交任何计算任务。

---

## 一、七方最终收口定稿摘要（211 词，12 句，最长句 24 词）

### English Abstract

Metal particles commonly coexist with single-atom sites in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet catalytic models often rely on bare single-atom surfaces. How the surface state formed under working conditions governs the binding of oxygen reduction reaction (ORR) intermediates remains unclear. Here, we prepare an FeCoMn–NC catalyst combining FeCo alloy particles with Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches a half-wave potential of 0.885 V versus the reversible hydrogen electrode (RHE), surpassing commercial Pt/C, FeCo–NC, and Mn–NC. It also retains 96.5% of its initial current over 238 h. Operando infrared spectroscopy shows that interfacial species evolve with potential, motivating surface-coverage calculations under working conditions. At 0.78 V versus RHE, these calculations reveal O*-covered FeCo particles and adjacent Mn single atoms carrying an axial OH. Without this axial OH, Mn binds ORR intermediates too strongly, and OH* removal is uphill. The axial OH pulls Mn out of the N₄ plane, and an intermediate adsorbing on the opposite side draws Mn back to the plane. Pulling Mn back consumes part of the binding energy and weakens the excessive adsorption. As a result, OH* removal becomes downhill at 0.78 V while OOH* formation remains nearly thermoneutral. FeCoMn–NC therefore lies near the apex of the calculated activity volcano, consistent with its highest measured activity.

### 中文直译

金属颗粒通常与单原子位点共存于热解金属氮碳（M–N–C）催化剂中，但催化模型往往仍依赖裸露的单原子表面。工作条件下形成的表面状态如何支配氧还原反应（ORR）中间体的结合仍不明确。本文中，我们制备了一种结合 FeCo 合金颗粒与 Mn 单原子的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的半波电位达到 0.885 V（相对于可逆氢电极 RHE），超过商业 Pt/C、FeCo–NC 和 Mn–NC。它在连续运行 238 h 后仍保持 96.5% 的初始电流。原位红外光谱显示界面物种随电位演变，这促使我们在工作条件下开展表面覆盖度计算。在 0.78 V（相对于 RHE）下，这些计算揭示了 O* 覆盖的 FeCo 颗粒以及带有轴向 OH 的相邻 Mn 单原子。没有该轴向 OH 时，Mn 对 ORR 中间体结合过强，OH* 脱附呈上坡。轴向 OH 将 Mn 拉出 N₄ 平面，而从对侧吸附的中间体又将 Mn 拉回平面。拉回 Mn 消耗了部分结合能，从而削弱了过强的吸附。因此，在 0.78 V 下 OH* 脱附转为下坡，同时 OOH* 生成保持接近热中性。FeCoMn–NC 因而位于计算活性火山图顶点附近，与其最高的实测活性一致。

### 配套无 `Determine` / 无 `Operating-State` 标题建议

`Axial OH Formed under Working Conditions Moderates Intermediate Binding on Mn Single Atoms beside FeCo Particles for Oxygen Reduction`

中文：工作条件下形成的轴向 OH 缓和 FeCo 颗粒旁 Mn 单原子上的中间体结合以实现高效氧还原

### 可选 3 词精简接口（待作者拍板）

若投稿时性能对比句只保留商业 `Pt/C` 基准，只需删去 `FeCo–NC, and Mn–NC` 并把末句 `highest` 改为 `high` 即可（总词数 208 词）。

---

## 二、七方最新综合版与网页 Gemini 14:28 新版的逐项裁决表

| 讨论条目 | 网页 Gemini 14:28 版写法 | 第二轮各家仓库版本对照 | 最终定稿采纳及依据 |
|---|---|---|---|
| **1. 开篇破题** | 两句铺垫「颗粒与单原子共存且表面演变」 | `ClaudeWeb`、`ClaudeWeb2`、`ClaudeCode` 云端/本地、`GPT`、`Antigravity`（6/6）全用方案二反差破题 | **采纳六方一致的方案二开篇**（`yet catalytic models often rely on bare single-atom surfaces` + `governs the binding of oxygen reduction reaction (ORR) intermediates`），科学对比更鲜明，消除名词堆叠。 |
| **2. 术语与语法统一** | `bcc FeCo`、`Mn–N₄ sites`、`RHE` 未在首次出现时写全称 | `ClaudeWeb`、`ClaudeCode` 云端、`Antigravity` 主张 `an FeCoMn–NC`、去 `bcc`、写 `Mn single atoms`、首次展开 `reversible hydrogen electrode (RHE)` | **采纳 `an FeCoMn–NC`、去 `bcc`、`Mn single atoms` 及首次全称 `reversible hydrogen electrode (RHE)`**，并替换 `ClaudeCode` 本地版 `3b3cd91` 残留的 `bcc` 与含糊词 `favor`。 |
| **3. 原位红外与计算过渡** | 写回 `detects OOH* and potential-dependent interfacial water changes, showing an associative ORR pathway` | `ClaudeWeb`、`ClaudeWeb2`、`GPT`、`ClaudeCode` 云端/本地均不写 `OOH*` 与缔合路径 | **坚决删除 `OOH*` 与 `associative ORR pathway`**。依据 `T043` 实测复核，1215 cm⁻¹ 与 Nafion C–F 重叠且同批双电极信号符号相反；采用 `interfacial species evolve with potential, motivating surface-coverage calculations under working conditions`（吸收 `ClaudeWeb 22c6f52` 与 `GPT ab9b579` 建议），不把红外夸大为覆盖态直接证据。 |
| **4. 无 OH 基线句** | 保留 `Without this axial ligand, Mn binds ORR intermediates too strongly and impedes OH* removal.` | `ClaudeWeb2`、`ClaudeCode` 云端/本地、`GPT`、`Antigravity` 与 Gemini 保留（6/7），仅 `ClaudeWeb 22c6f52` 删去 | **采纳 `ClaudeCode` 云端 `5fcbcfc` 句式**：`Without this axial OH, Mn binds ORR intermediates too strongly, and OH* removal is uphill.`。这是 `T032` 同模型内禀对照（`+0.27 eV → −0.07 eV`），与后句 `becomes downhill` 首尾咬合，并非样品间横比。 |
| **5. 几何拉回与能量抵消** | `whereas ... draws Mn back toward the plane` + `Drawing Mn back consumes part of the binding energy...` | `whereas` 含对比连词瑕疵；`ClaudeWeb2 / ClaudeCode` 云端用 `back to the plane` 与 `Pulling Mn back` | **用 `and` 代替 `whereas`**；采纳 `back to the plane`（覆盖 `T042` 实测 `OOH* +0.003 Å`、`OH* −0.009 Å`、`O* −0.098 Å`），并吸收 Gemini 与 `ClaudeWeb2 / ClaudeCode` 云端更直白的表达 `Pulling Mn back consumes part of the binding energy and weakens the excessive adsorption`，舍弃 `opposing displacement` 与 GPT 的 `associated deformation`。 |
| **6. 结尾火山图与活性落点** | 漏写 `calculated`，结尾为 `high measured activity` | `3b3cd91` 因果顺序倒置；`ClaudeWeb2 / ClaudeCode` 云端 / `GPT` / `Antigravity` 均写 `calculated activity volcano` | **修正 `3b3cd91` 因果倒置并补齐 `calculated`**，采用 `near the apex of the calculated activity volcano, consistent with its highest measured activity`（呼应图 6h 计算火山图，不越界用计算绝对值解释实验）。 |
| **7. 双面可及性（`CW2-19` 已闭环）** | 使用 `opposite side` | 用户已于 `2c2bb14` 确认热解多孔碳为领域共识，不补 BET、不加算翻转构型 | **保留 `opposite side` 不变**，与标准单层双面 `M–N–C` DFT 模型共识完全一致。 |

---

## 三、实测坐标核查与 `3e6ee5c` 两处笔误更正备忘

针对 `CW2-19` 期间的坐标核查请求，本端已核对本地 [imr_branches.json](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T031/imr_branches.json)、[genkai_branches.json](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T031/genkai_branches.json)、[reaction_geometry_matches.json](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T032/reaction_geometry_matches.json) 与 [Antigravity.csv](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T042_Mn_position/Antigravity.csv) 中的精确原子坐标（无需再在超算复跑或另查 POSCAR）：

1. **三项精确几何实测**：
   - 超胞尺寸为 `22.20 × 21.36 × 24.00 Å³`，单层 `N` 掺杂石墨烯（`174 C + 4 N`）位于 `z = 5.96–6.45 Å`（`N₄` 均值约 `6.10 Å`），无第二层碳，上下真空跨度 `10.24–12.59 Å`。
   - `FeCo` 合金颗粒（`z = 8.26–16.37 Å`，含表面 `8O*` 至 `17.38 Å`）与主背景态 `FCM_8O_MnOH` 的轴向 `OH`（`O` 位于 `z = 8.43 Å`，`N₄` 上方 `+2.32 Å`）同在 **`+z` 上表面一侧**；主路径 `FCM_bg8O_MnOH_{OOH, O, OH}` 与无 `OH` 对照组 `FCM_cov8O_{OOH, O, OH}` 的 ORR 中间体全在 **`−z` 下表面一侧**。
   - `Mn` 原子距 `FeCo` 颗粒最近水平投影距离 `min_xy(Mn–FeCo) = 8.09–8.10 Å`（并未贴近颗粒缝隙）；仅放单个轴向 `OH` 在颗粒同侧（`+z`，`FCM_8O_MnOH`，`E = −2140.1479 eV`）与对侧（`−z`，`FCM_cov8O_OH`，`E = −2140.1325 eV`）能量仅差 **`0.0154 eV`**。
2. **对 `20261121_geometry_audit_task.md`（`3e6ee5c`）两处笔误的公开提醒**：
   - **没有 BET 表征**：检索正文 [FeCoMn_Manuscript_revised_20261119_2255_plaintext.txt](file:///C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/manuscript/FeCoMn_Manuscript_revised_20261119_2255_plaintext.txt) 与 SI 全文均未见 BET 或 N₂ 吸脱附测试数据，后续正文或审稿回复中不可宣称引用已有 BET 数据。
   - **不可写颗粒稳定了轴向 OH**：`3e6ee5c` 记录中出现过「由 O*-covered FeCo 颗粒稳定」的表述；根据 `T039` 双分支电子态不可比边界（以及双面 `OH` 仅差 `0.0154 eV` 的结果），正文、SI 与图注不得将该表达写成已证明因果，仅陈述计算给出 0.78 V 下两者共存即可。

---

## 四、Python 自动化核验记录

- **英文摘要总词数**：`211` 词（上限 `< 250` 词）
- **英文句子数与句长**：`12` 句，最长句 `24` 词（`<= 25` 词）
- **英文禁词命中**：`[]`（`0` 命中，已排查 `operating`、`reorganization`、`reconstruction`、`penalty`、`must`、`dz`、`cdl`、`ecsa`、`wan `、`0.49`、`0.96`、`favor`、`without necessarily`、`bcc`、`determine`、`whereas`、`associative`）
- **中文直译禁标点命中**：`[]`（`0` 命中，零全角冒号、零全角分号、零中文破折号、零中文双引号）
- **全文件共享记忆禁用符号检查**：`0` 命中（全文零中文破折号、零中文双引号）
