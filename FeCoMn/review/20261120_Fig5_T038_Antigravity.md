# Fig 5 第一段（加入 T038/T038b）Antigravity 独立审阅报告

**审阅方**：Antigravity  
**日期**：2026-11-20  
**审阅对象**：`FeCoMn/discussion/20261120_1112_Fig5_T038_paragraph_for_review.md`（commit `24c2db6` 及 `11:15` 更新 `93c689b`）  
**对照基准**：现行正文 `FeCoMn/manuscript/FeCoMn_Manuscript_revised_20261119_2255_plaintext.txt`（第 278–335 行）、现行 SI `FeCoMn_SI_revised_20261119_2255_plaintext.txt`（第 839–870 行、第 1039–1430 行）、`FeCoMn/discussion/20261119_core_claims.md`（第十二节）。

---

## 对 5 个重点问题的逐项审阅结论

### 问题 1：逻辑顺序是否成立；新末句 `"The effect of the FeCo particles on the Mn single atoms therefore appears in the axial ligand rather than in the bare Mn single atoms."` 是否严格由前两条证据得出？

1. **逻辑骨架成立**：现象（0.78 V 下 FeCoMn–NC 中 OH 比 O 稳 0.18 eV，Mn–NC 相反）→ 问题（是否因颗粒直接改变裸 Mn 电子态）→ 检验（保持其余原子坐标不变去除颗粒）→ 结果（无配体 Mn 电荷分布与 3d 态几乎不变）→ 结论。这一对比只涉及无轴向配体 Mn，与图 6 中带配体（Mn–OH vs Mn=O）的机制拆分开，避免了混用风险。
2. **新末句边界评估（需微调措辞以免微弱越界与搭配生硬）**：
   - T038/T038b 实际证伪的是“无轴向配体条件下颗粒直接显著改变 Mn 静态电子结构”（`Δq(Mn) = +0.006–0.007 e`，`Δdz² = +0.013–0.032 eV`，磁矩同为 `~3.1 μB`）。它**并没有直接观测“含轴向配体形成过程中颗粒到底通过何种动态/间接路径起作用”**，只能严谨得出：**该颗粒效应并不体现在无轴向配体的裸 Mn 基态上，而是体现在有轴向配体（配位态）的情况下**。
   - 原句 `"appears in the axial ligand"` 在英文语义上易被理解成“影响出现在配体自身内部（而非 Mn–配体态或配体选择性上）”，与前面 `"electronic structure of the Mn single atoms"` 衔接稍显跳跃。建议改为 **`"manifests in the axial-ligand state (or axial coordination) rather than in the ligand-free Mn site"`**。

---

### 问题 2：原段末结构句并入括号后，与下一段 `"On these covered surfaces"` 的呼应是否还在？

- **判定：存在明显“话题断档”，建议微调新末句尾词或第 2 段首词加以桥接。**
  - 原文段末是 `8O* + Mn–OH* ... 8O* ... 1O* ... (Figure 5g and Figure S24)`，下一段紧接 `On these covered surfaces`，`these` 自然回指刚说完的三种覆盖表面。
  - 修改版在括号后插入了 4 句关于“**去掉颗粒后的无配体裸 Mn**（`bare Mn single atoms`, `Figure S25`）”的讨论，导致段末焦点停留在“裸 Mn”上；下一段一开头突然写 `On these covered surfaces`，读者需要向前跨越四行才能找回 `these` 的先行词。
- **最小改动修复**：在新末句末尾顺带点回覆盖表面（不改变已定的结构句位置），例如写成：
  `"...manifests in the axial-ligand state on the covered surfaces rather than in the ligand-free Mn site."`
  这样下一段开头的 `On these covered surfaces` 即可直接无缝承接。

---

### 问题 3：`"and pH 13, which corresponds to the 0.1 M KOH electrolyte"` 要不要删？

- **判定：不建议整句删除，建议收紧为 `"in 0.1 M KOH (pH 13; Figure 5d–f)"`。**
  - **不能一删了之的原因**：图 5d–f 纵轴为 `V versus SHE`，其图注明确标注 `"Stars mark 0.78 V versus RHE at pH 13"`（正文第 320–321 行）；第 2 段首句也写了 `"On these covered surfaces, obtained with the actual potential and solution pH taken into account..."`（正文第 295–296 行）；SI Figure S24 图注同样写明 `"at 0.78 V versus RHE and pH 13"`（SI 第 839–840 行）。若正文第 1 段完全删去 `pH 13` 和 `0.1 M KOH`，图 5d–f 的五角星和第 2 段的 `solution pH` 会在正文中失去上下文交代。
  - **收紧理由**：在 CHE 框架下，RHE 标度内表面覆盖度的热力学排序与 pH 无关（pH 13 仅用于把 0.78 V vs RHE 换算到图 5d–f 的 SHE 纵轴并对应 0.1 M KOH 实验体系）。原句 `At 0.78 V versus RHE ... and pH 13, which corresponds to the 0.1 M KOH electrolyte` 并列作条件状语略冗余，改为 **`At 0.78 V versus RHE (a representative ORR potential)¹¹ in 0.1 M KOH (pH 13; Figure 5d–f), ...`** 既保留对应关系又消除物理误解。

---

### 问题 4：中式表达、长句与指代问题

1. **术语风险：`bare Mn single atoms` 易与“失去 N₄ 配位”混淆**：Mn 在所有模型中始终与 4 个平面 N 配位（`Mn–N₄`），只是没有**轴向 O/OH 配体**。且同一段中先用 `Mn single atoms without axial ligands`，后用 `bare Mn single atoms`，指代不统一。建议全文统一为 **`ligand-free Mn sites`（或 `Mn sites without axial ligands`）**。
2. **模型颗粒单复数不一致**：前文在三催化剂并列对比时用复数 `FeCo particles` 合理，但执行计算动作 `we removed the particles from the FeCoMn–NC model` 时，`FeCoMn–NC` 周期单胞中仅含 **1 个** 59 原子 FeCo 颗粒；用复数 `the particles` 易让读者误解为一个超胞里有多个颗粒。建议该句用单数 **`removed the FeCo particle from the FeCoMn–NC model`**（或在并列包含 clean 和 8O* 两套对比时明确写 `models` 并补充说明包含两种颗粒覆盖）。
3. **中式/非典型学术表达两处**：
   - `without changing the other atomic positions` → 建议改为 **`while keeping all remaining atomic coordinates fixed`**（或 **`at fixed support geometry`**）；
   - `the charge distribution and 3d electronic states ... barely change` → `barely change` 口语感偏强，且本文实际统计的是 Bader 电荷/局域积分电荷与 3d/$d_{z^2}$ 中心，建议改为 **`both the local charge and 3d electronic states ... remain essentially unchanged`**。
4. **能量差缺失电位限定**：`Axial OH is more stable than axial O by 0.18 eV ...` 中该自由能差随电位变化（含 1 个质子-电子对），应加上 **`At this potential,`**（或 **`At 0.78 V versus RHE,`**）。

---

### 问题 5：编号顺延、表号对应与数据口径核查（供 Claude Code 与作者核实）

在核对现行正文与 SI 纯文本时发现以下 **2 处表号/口径隐患**：

1. **草稿中的 `(Table S6)` 与现有 `Table S10` 指向冲突**：
   - 现行 SI 中，`Table S6` 原为颗粒结合能与结构恢复（`−3.73 eV`），而 **`0.18 eV`（`−14.92 vs −14.74 eV`）和 `0.30 eV`（`−0.48 vs −0.18 eV`）的数据源自现行 `Table S10`**！
   - 草稿第 43 行规划 `新表 S6（原 S6 起顺延）`，但新表 `Table S6` 在草稿正文中被挂在了 `0.18 eV / 0.30 eV` 这句话末，而 **T038/T038b 本身的数据却只引了 `(Figure S25)`，未引 `Table S6`**。
   - **处理建议**：
     - 若新 `Table S6` 打算专门汇总 **T038/T038b 受控比较数据**（Bader、磁矩、3d/dz² 中心、Δq）+ 配体差值，则应把 `0.18 / 0.30 eV` 的引用指向原 `Table S10` 顺延后的 **`Table S11`**（或双引 `Tables S6 and S11`），并在 T038/T038b 结论句加上 **`(Figure S25 and Table S6)`**。
2. **现行 `Table S10` 中 `0.30 eV` 对应的 `Mn–NC` 构型名称需在内部确认一致性**：
   - 现行 `Table S10` 第 1321–1325 行显示：`MnNC O bri`（`−0.48 eV`）比 `MnNC OH`（`−0.18 eV`）稳 **`0.30 eV`**，而表中另有一项 `MnNC O`（`−0.12 eV`）。`20261119_core_claims.md` 第 152 行曾提示 `MnNC O` 并非全局最稳、`MnNC O bri` 低 0.36 eV；但 `Figure S24` 与 `Table S5` 已统一标注 `Mn–NC` 反应态为 `Axial O* on Mn (Mn=O, 1.58 Å)`。请 Claude Code 在核对编号与 SI 时同步确认 `MnNC O bri` 与正文/图 S24 口径无冲突。
3. **现行稿件受顺延影响的已知引用位置（供 Claude Code 核查补充）**：
   - 正文第 299、301、302、309 行（`Table S7`, `Table S8`, `Figure S25`, `Figure S26`）及第 331 行起图 6 段落的 `Table S9`；
   - SI 目录页（第 125–165 行）及正文交叉引用（第 403、437、660、764、784、792、850–870、1060–1168 行）中所有 `Table S6–S10` 与 `Figure S25–S28+`。

---

## 综合修改建议（可直接替换当前版本）

> At 0.78 V versus RHE (a representative ORR potential)¹¹ in 0.1 M KOH (pH 13; Figure 5d–f), the surface coverage is 8O* + Mn–OH* for FeCoMn–NC, 8O* for FeCo–NC, and 1O* (an axial O on Mn) for Mn–NC (Figure 5g and Figure S24). At this potential, axial OH is more stable than axial O by 0.18 eV in FeCoMn–NC, whereas axial O is more stable than axial OH by 0.30 eV in Mn–NC (Table S11). To test whether this difference arises because the FeCo particle directly alters the electronic structure of the Mn site, we removed the FeCo particle from the FeCoMn–NC model while keeping all remaining atomic coordinates fixed. After this removal, both the local charge and the 3d electronic states of the ligand-free Mn site remain essentially unchanged (Figure S25 and Table S6). The influence of the FeCo particle on the Mn site therefore manifests in the axial-ligand state on the covered surfaces rather than in the ligand-free Mn site itself.
