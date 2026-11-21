# GPT 独立科学审阅：FeCoMn–NC 为什么具有适中的 ORR 中间体吸附（2026-11-20）

审阅依据：`FeCoMn/discussion/20261120_1228_abstract_mechanism_for_review.md`（含 12:30/12:40 更新）；以讨论文件所列 T032/T037 已核实数据为准。本报告独立评价，不默认赞同 Claude web 的现有版本。

## 先给结论
**这不是寻找一句更漂亮的摘要，而是将“可观测的轨道成键—热力学结果”与“导致适中吸附的物理因果”分开。** 当前 FeCoMn–NC 单体系数据明确表明：工作态 Mn–OH；吸附前轴向 Mn–OH 的 dz² 分波 −ICOHP=1.00 eV、dz² 中心 −3.17 eV；吸附 OOH* 时 Mn–OOH 的 dz² 分波 −ICOHP=1.38 eV；在 U=0.78 V 时形成 OOH* 的自由能上坡 <0.01 eV、其余 ORR 步骤下坡、U_L=0.78 V。这些是**相互一致的观测与计算**，但尚未构成“轴向 OH 键较弱，所以 OOH*/OH* 两端都恰好适中”的单向可验证因果定理。

**最值得提出的机制命题：工作态轴向配体确定了 Mn 的局域成键环境，在该环境下 Mn dz² 轨道能够参与 ORR 中间体成键，同时整个四电子 ORR 自由能序列实现近平衡的限制步。** 可将其作为“有证据支持的机制解释”，不能写成已经隔离其他因素的因果证明。

## 1. 对 Claude web 当前英文的逐环审查

原句：
> The axial OH and OOH* bind to the same Mn d orbital from opposite sides. Because the axial OH bonds only weakly with this orbital, Mn binds the ORR intermediates at a strength at which OOH* formation is nearly thermoneutral and OH* removal is downhill at 0.78 V. FeCoMn–NC therefore binds the ORR intermediates moderately and lies near the apex of the activity volcano, which explains its highest measured activity.

- `same Mn d orbital from opposite sides`：若结构明确处于 Mn 的上下两个轴向位、且投影 COHP 支持 dz² 两侧成键，可说 `the Mn dz² orbital contributes to bonding with both the axial OH and OOH*`。不能仅凭两条独立分波 ICOHP 数值就证明二者在同一反应态同时成键、也不应误说它们争夺轨道；需明确哪一组构型/COHP 是吸附前、哪一组是 OOH* 吸附后。
- `because the axial OH bonds only weakly ... Mn binds ... at a strength at which ...`：**关键逻辑跳跃**。弱 Mn–OH 的 dz² 分波本身不唯一决定 Mn–OOH、Mn–OH* 的吸附自由能；COHP 为占据态积分的成键描述符，不直接等于吸附自由能，也不能直接解释 OH* 脱附。同时 “weakly/appropriately” 都是相对于基准的判断，不能依靠单体系绝对 −ICOHP 数值断言。
- `OOH* formation nearly thermoneutral and OH* removal downhill`：这是最扎实、最自洽的**能量层解释**：以反应自由能序列明确何为 `moderate`。但不能误导为“OH* 的脱附完全由 dz² 高能导致”。
- `near apex ... explains highest measured activity`：DFT 自由能趋势与实验相符，但严格上不等于证明实验速率控制/唯一活性中心；最好用 `accounts for the favorable calculated ORR energetics and is consistent with the measured activity`，或 `provides a thermodynamic rationale for its high ORR activity`，避免把理论火山图说成已量化验证了实验动力学。

## 2. 在“不比较 Mn–NC 和 FeCo–NC”的硬约束下，如何解释适中吸附？

不靠其他催化剂也能给出**操作性而非绝对的定义**：
- 适中 = 以 U=0.78 V 为例，OOH* 形成接近热中性（ΔG<+0.01 eV），其余三步在该电位下有利；其对应的 ORR limiting potential 约 0.78 V。这个结论来自 **FeCoMn–NC 自身完整自由能序列**，无需参照对照样品。
- 轴向 OH 的角色 = Mn–OH 工作态存在；COHP/PDOS 表明 Mn dz² 有可辨成键参与（Mn–OH dz² −ICOHP 1.00 eV，Mn–OOH dz² 1.38 eV）。这可以解释 Mn 不是“已经被轴向配体完全钝化”的位点，但这还只是对轨道参与的描述，不自动证明该 OH 造成所有中间体能量的最优化。
- `weak` 无单体系客观绝对阈值。可说 `an axial Mn–OH bond with modest dz² bonding contribution`（需文中明确定义参照）或直接给出 `Mn dz² contributes to both bonds`，避免先验“弱→强”因果。
- 注意 OH* 在 ORR 图上的步骤通常是 `OH* + (H+ + e−) → H₂O + *`（碱性等效水反应）。摘要可写 `OH* removal is downhill`，但完整正文需准确按 CHE/碱性反应式表示。OOH* 吸附后的轴向 Mn–OH 是否还保持、ICOHP 如何变化，要核对结构与数据。

## 3. 摘要应该写到哪里？

**摘要推荐为“工作态局域配位 → 中间体成键（轨道证据一句） → 四步能量的定量结果”**，不在摘要展开 dz² 中心 −3.17、−ICOHP 1.00/1.38 和过度简化的 d-band 理论。

### 可用摘要机制句（推荐）
> On the OH-ligated Mn sites, the Mn dz² orbital participates in OOH* bonding, enabling nearly thermoneutral OOH* formation while subsequent ORR steps remain downhill at 0.78 V versus RHE. This favorable free-energy profile places FeCoMn–NC near the apex of the ORR activity volcano.

直译：在轴向 OH 配位的 Mn 位点上，Mn 的 dz² 轨道参与 OOH* 成键，使 OOH* 的生成接近热中性，同时在相对于 RHE 的 0.78 V 下后续 ORR 步骤仍为自由能下坡。这一有利的自由能分布使 FeCoMn–NC 位于 ORR 活性火山图顶点附近。

**证据定位：**
- 第一句前半：工作态覆盖（Figure 5，8O*+Mn–OH）；OOH* 的 Mn dz² 分波 ICOHP=1.38 eV；
- 第一句后半：T032 U=0.78 V 下 OOH* ΔG<+0.01 eV、其余步骤 ΔG<0；
- 第二句：活性火山图、U_L=0.78 V。
- **保留限定**：这里的 `enabling` 是模型内轨道和热力学结果的合理联系，但若要用更严格的不施加因果说法，可改为 `... participates in OOH* bonding; OOH* formation is nearly thermoneutral ...`（更符合证据，不要用 `thereby`）。

### 直接保守且精确版本（优先科学严谨）
> On the OH-ligated Mn sites, the Mn dz² orbital contributes to OOH* bonding. At 0.78 V versus RHE, OOH* formation is nearly thermoneutral and the remaining ORR steps are downhill, placing FeCoMn–NC near the apex of the ORR activity volcano.

直译：在轴向 OH 配位的 Mn 位点上，Mn 的 dz² 轨道参与 OOH* 成键。在相对于 RHE 的 0.78 V 下，OOH* 生成接近热中性，其余 ORR 步骤为自由能下坡，使 FeCoMn–NC 位于 ORR 活性火山图顶点附近。

**备注：这版解释了“适中表现为什么”，但没有伪装成从 ICOHP 必然推出 ΔG 的微观因果证明；如作者坚持摘要必须写“为何如此”，则需要下文的可检验机制对照来支撑更强因果语言。**

## 4. 图 6 正文的建议结构（先建立机制，再比较）

1. **工作态明确**：基于 Fig.5，在 0.78 V、pH13，Mn–OH + 8O* FeCo；ORR 中间体与 Mn 单原子结合（结构/吸附位置）。
2. **轨道如何参与**：Mn dz² 占有态中心 E−E_F=−3.17 eV；轴向 Mn–OH dz² 分波 −ICOHP=1.00 eV、Mn–OOH 分波 −ICOHP=1.38 eV。说明两者涉及同一轨道对称性的成键通道；小心 COHP 是否在同一构型中核对。
3. **真正量化“适中”**：引用 FeCoMn–NC 完整四步 ΔG 图，U=0.78 V 下 OOH* 生成 ΔG<0.01 eV、其余步为下坡。不要假设“dz² 高→OOH 强、OH 自动易脱附”。
4. **性能联系**：该自由能分布→ U_L=0.78 V、火山图靠近顶点，与实验 E1/2=0.885 V 的较优趋势一致（不同量纲/物理意义，不应数值等同）。
5. **最后才对照**：在 Mn–NC 中轴向 Mn=O 的 dz² 成键更强（2.98 eV）、dz² 轨道中心更低（−5.12 eV）、Mn–OOH dz² 分波较小（1.06 eV），配合其 OOH* 形成自由能更不利；这是对提出机制的对比佐证，不应反过来替代本体系解释。此处允许对照，摘要解释中不用。
6. **图文衔接**：避免连续列多个术语；每个数字解释其作用，不让 COHP→能量关联跳步。

### 示范 Fig.6 核心英文段（需与图和原稿上下文整合）
> At the ORR-relevant surface state, FeCoMn–NC contains an axial OH ligand on Mn, while the FeCo particles are covered by O*. The occupied Mn dz² states are centered at −3.17 eV relative to the Fermi level. Orbital-resolved COHP analysis identifies contributions from Mn dz² to the axial Mn–OH bond (−ICOHP = 1.00 eV) and to Mn–OOH* bonding (−ICOHP = 1.38 eV), establishing that this orbital participates in both types of bonding. The resulting ORR free-energy profile provides a direct measure of the adsorption balance: at 0.78 V versus RHE, OOH* formation is nearly thermoneutral (ΔG < 0.01 eV) and the remaining three steps are downhill. The calculated limiting potential is therefore 0.78 V, placing FeCoMn–NC near the top of the activity volcano and providing a thermodynamic rationale for its high ORR activity.

直译：在与 ORR 相关的表面状态下，FeCoMn–NC 中 Mn 带轴向 OH 配体，而 FeCo 颗粒表面被 O* 覆盖。Mn dz² 占有态中心位于相对于费米能级的 −3.17 eV。轨道分辨 COHP 分析表明，Mn dz² 对轴向 Mn–OH 键（−ICOHP=1.00 eV）以及 Mn–OOH* 成键（−ICOHP=1.38 eV）均有贡献，说明该轨道参与两类成键。得到的 ORR 自由能分布直接量化了吸附平衡：在 0.78 V vs RHE 下，OOH* 形成几乎热中性（ΔG < 0.01 eV），其余三个步骤均为下坡。因此，计算的限制电位为 0.78 V，使 FeCoMn–NC 位于活性火山图顶端附近，并为其较高 ORR 活性提供热力学解释。

**注意**：这段不是完整“为何 OH 引起适中”的因果证明，是安全的、最清楚的证据层级叙事；更强归因需检验配体变化的受控反事实。

## 5. 自由思考：最有希望的机制突破口（不限是否新计算）

**突破口 A（首选）：把 T039 发展为“同几何配体选择—中间体吸附耦合”的闭合自由能循环。**
- T039 原任务：在 C_support 载体上分别 Mn–OH/Mn–O，检验去掉 8O*+FeCo 颗粒是否反转配体选择。这检验“颗粒 → 配体偏好”。
- 但摘要需要的是另一半：“配体状态 → ORR 中间体吸附为何合适”。最有辨识力的不是更多 Bader/d带中心，而是**控制同一表面几何下分别保持 Mn–OH、Mn–O，计算两态的 OOH*（以及 OH*）吸附/对应 ORR 反应自由能**，并在相同电位/pH、化学势修正及磁态口径比较。
- 这样可构建两条可审查箭头：
  (i) `FeCo 颗粒/颗粒覆盖 → 轴向 OH 与 O 相对稳定性`（T039）
  (ii) `轴向 OH vs 轴向 O → OOH* / OH* 相对反应自由能`（配体受控比较）。
- 两步都有同几何/相容的计算基准后，才有条件在摘要写 `FeCo particles shift the preferred axial ligand toward OH, which tunes intermediate binding ...`。若只有数值现象，避免声称已解释微观通道。
- 可操作性约束：若 Mn–O 与 Mn–OH 改变 H/O 原子数，必须用相同 H+/e−/H₂O 化学势作 grand-canonical/CHE 对齐，不能简单拿裸总能量或独立自由能差冒充配体选择能。

**突破口 B：检验“一个 dz² 通道连接两类键”到底是不是微观因果。**
- 针对 Mn–OH 与 Mn–OOH* 的 projected COHP/PDOS，在*同一 OOH* 吸附构型中*计算轴向 Mn–OH 及 ORR 端 Mn–OOH* 的 dz² 分波，配合吸附前后的变化、占据态与反键态贡献。检测两侧键是否同时存在、是否存在电荷重排；避免断言“轨道竞争”。
- 因轴向 Mn–OH 的总 ICOHP 吸附 OOH* 后由 2.64→3.00 eV（用户已指出），这至少说明“两侧键此消彼长”的简单竞争模型不成立，可能存在协同成键/自洽重排，但**仅凭增强不能断言协同机制**。
- 若吸附前后 dz² 投影的变化与反应自由能一致，再尝试从轨道杂化/反键态占据构建不循环论证的解释；重点应是 OOH*、OH* 两端都核实，而不是只解释 OOH* 成键增强。

**突破口 C：从“单个吸附能最佳”换为“整个自由能窗口内的平衡”。**
- 已有 T032 能说明 ΔG_OOH*、ΔG_OH* 受近似通用 scaling 约束（讨论文件称 ΔG_OOH*−ΔG_OH* 近似恒定）；因此对四电子 ORR，“适中”往往是中间体结合强度将瓶颈从 OOH* 形成与 OH* 去除之间取得较好的折衷，表现为 volcano apex。**不是**轴向 OH 需要分别独立地把 OOH* 吸牢同时使 OH* 变弱。
- 建议正文根据 Fig. 6 的同一 ΔG_OH* 描述符、各步自由能，明确示出关键支配的两个边界（OOH* 形成与 OH* 去除）；不能从单一 dz² 带心推断两者朝相反方向调节。
- 这可能是当前最有解释力的理论框架：**配体改变的是 Mn 位点在 scaling-constrained adsorption-energy landscape 中的位置**，而不是打破 scaling。若稿件数据确实支持 FeCoMn–NC 位于近最优点，可在 Fig.6 以数值展示“自由能窗口匹配”。

**突破口 D：严格区分“OH 作为固定工作态配体”和“OH* 作为 ORR 中间体”。**
- 文章中的轴向 `Mn–OH`（工作态）与 ORR 的 `OH*`（反应性吸附中间体）分属不同配位位置/角色。任何“OH* 脱附下坡”的自由能参照必须明确保留轴向配体或检查配体是否在反应过程中变化；否则“弱轴向 Mn–OH → OH* 易脱附”的推论尤其危险。
- 如拟打通图 5→图 6 的反应过程，可核对四步中轴向 OH 是否始终保留、是否存在工作态覆盖互变；必要时才构建自洽比较。

## 建议的决策顺序
1. 不急于在摘要写“弱轴向键使所有中间体适中”的因果句。
2. 优先核对已有 Fig.6 四步的明确反应式、工作态配体是否固定、轨道分波 ICOHP 是否同态比较，以及 ΔG_OOH*−ΔG_OH* scaling。
3. 等 T039 检验“颗粒 → 配体”后，若要强化“配体 → 适中吸附”，优先做**相容几何下改变轴向配体的受控自由能比较**，而非继续单点 Bader/d带心堆积。
4. 在没有这些额外数据前，采用“轨道参与 + ΔG定量定义适中 + 热力学火山图”的严谨叙事；有反事实支持后再升级因果句。


---

## 第二轮（2026-11-20）：对第一轮汇总及四个问题的独立回答

审阅源：`FeCoMn/discussion/20261120_1310_mechanism_synthesis_round2.md` (commit 102e917)、`FeCoMn/from_agent/FeCoMn-T026/REPORT.md`、Claude Code 与 Antigravity 的第一轮审阅，以及 T040 任务单。

### 1. T026 B→C 是否是“为什么适中”的核心解释？

**是，这是迄今最有力的“同一催化剂内部”的定量反事实；应成为 Fig. 6 的主要机制之一。但必须准确限定体系。**

我独立重读 T026/REPORT：B、C 都是**干净 FeCo 颗粒**背景，不是 8O* 工作态颗粒。B（Mn 无轴向 OH）的 ΔG(OOH*/O*/OH*) = **3.8738/1.4291/0.4669 eV**；C（Mn 有轴向 OH）= **4.1235/1.9382/0.8076 eV**。加入轴向 OH 后吸附自由能分别升高 **0.2497/0.5091/0.3407 eV**，即相对于无轴向 OH 的同一 FeCoMn–NC 模型，ORR 中间体总体吸附减弱；U_L **0.4669→0.7965 V**，瓶颈由 OH* 去除转为 OOH* 生成。这是定量“合适吸附”的真正解释，不需要拿 Mn–NC 或 FeCo–NC 来定义“适中”。

对 ORR 自由能的可复核描述（采用 T026 ΔG 和常规 ORR CHE）：在 **0.78 V** 时，B 的 OH* 去除为 **+0.3131 eV**（不利），C 的 OH* 去除为 **−0.0276 eV**（有利）；C 的 OOH* 形成为 **−0.0165 eV**（近热中性）。这比不带参照的“Mn–OH 键弱，所以恰当”逻辑明显更硬。

**关键限制**：
- B/C 颗粒都未覆盖 O*；实际 0.78 V 工作态是**颗粒 8O*** + Mn–OH，主结果 U_L≈0.78 V。C 的 0.7965 V 与工作态 0.78 V 数值接近是**外推一致性**，不是证明颗粒覆盖无影响。不得把 B/C 写成“同一 8O* 背景”的对照。要避免把“Mn 自发吸附 OH”说成由 B→C 算出；OH 优选是 Fig. 5 的独立热力学结论，且需结合 T039 的颗粒因果。
- B/C 中不同表面原子数（增加 OH）和电化学参照必须按相同 CHE 公式分别确定各自背景及各步 ΔG；T026 已按相同校正核对，但不能以 B/C 总能量直接作吸附差。
- **最值得先做的零新增计算检查**：从现有计算目录核对是否已有**8O* 背景下，Mn 裸位与 Mn–OH 位点的相容 ORR 三中间体**。只有齐备才能把这一关键结果严格升级到工作态。没有齐备也可以在正文明确写“for the clean-particle model, introducing axial OH ...; the actual O*-covered surface exhibits a similar limiting potential”，不装作已完成工作态单变量测试。
- 需要注意单次 DFT/局域构型可能不完整，并非动力学实测速率或“OH 中毒”的直接实验观察。

### 2. 自旋思路应放在什么位置？

**建议放在“支持成键和电子重排”的次级证据，不用作“配体为何将吸附变得适中”的主因，更不进入摘要。**

- 8O* 工作态无配体 Mn ≈3.116 μB、带轴向 OH ≈3.206 μB；两者磁矩接近，但轴向 OH 对吸附自由能的调节很大，故自旋大小**不能解释 B→C 初态的主要区别**。
- 若 T037 的 Mn–OOH* 从 3.206→2.384 μB 及 dz² 自旋投影从 +0.519→+0.106 复核无误，这只能说明 OOH* 吸附伴随显著**局域自旋极化重排**。不能依据局域磁矩下降 0.8 μB 宣称恰有“一个自旋配对”、交换能代价的正负、某个 β 空轨道充填或实验 ORR 电子转移动力学被加速；总磁矩和吸附物种的自旋密度亦需检查。
- `dz² occupied weight = 0.995` 是**指定能窗内的投影积分**，并不能直接等同于整数单占的精确原子轨道构型 `dz²¹`；“α 在下、β 低能空态”需要自旋分辨 PDOS 的费米能级上下连续谱证据。Antigravity 应独立复核 Claude Code 分析脚本的列索引、上下自旋符号、能窗、费米能对齐及对应的结构态。
- **特别的轨道物理纠错：** Claude Code 提出“Mn=O 的额外 π 通道直接走 dz²”不正确。在近轴向几何中 dz² 对称性主要参与 σ 相互作用，典型金属–氧 π 相互作用涉及 **dxz/dyz** 与氧 px/py。不能借这一错误解释 dz² −ICOHP(OH)=1.00 与 Mn=O 的 2.98 eV。
- Antigravity 第一轮用“高自旋保留→保证 OOH*、五配位单齿→自动防止过强吸附”也不构成充分证明：单齿配位不必然弱吸附，局域 Bader 电荷与总吸附能亦不能直接等同。
- 轴向 Mn–OH 的 −ICOHP 在吸附 OOH* 后 **2.64→3.00 eV**，本身反对简单“相反两侧争抢 dz² 所以削弱轴向键”的直观；不宜急用 `trans influence` 或“自旋配对解除了交换排斥”等尚未算出的解释。

### 3. “颗粒效应在配体存在时才显现”值得追吗？

**值得追，但目前不能写成已证实。** 它有可能真正区别于传统“颗粒直接向裸 Mn 电子调控”的机制。

- T038/C_support 与 T038b/A/As 显示裸 Mn 电荷与 dz² 中心变化极小，但这只是**局域态电子描述符**；T030、T032 的带配体吸附自由能变化若较大，存在“配体依赖的能量响应”线索，尚不能单靠这两类不同的指标推出明确的因果协同。
- 现有 Mn–NC 与 FeCoMn–NC 背景几何不同；Mn–NC+OH 属**强加的亚稳/假设配体态**，且所谓 ΔG_OOH*−ΔG_OH* =2.70 eV 偏离其他约 3.2–3.4 eV，首先要做数值与自旋/参考态审计，防止把不相容数据当机制发现。
- 我主张优先用已有的**完整双差自由能循环**（如能由现有数据补齐）分离因果：同一 Mn–N4 支撑几何、同类约束、同一电化学参照，分别比较“颗粒有/无 × 轴向配体有/无”下**OOH* 与 OH* 反应自由能**的差异。定义对某一 ORR 中间体 X 的颗粒-配体耦合项
  `J_X = [ΔG_X(P,OH)−ΔG_X(P,bare)]−[ΔG_X(noP,OH)−ΔG_X(noP,bare)]`。
  只有 `J_X` 显著非零，才支持“颗粒影响取决于轴向配体”的能量非加性；并通过误差/收敛性检查判断幅度。这里 P 应注明是否 `FeCo+8O*`，否则不能分辨颗粒本体与覆盖层作用。
- T039 检验的是**颗粒存在与否对 OH/O 配体偏好**（另一自由能双差），不能独自证明上述对 OOH*/OH* 的非加性。因此 T039 是必要但不充分的部分。

### 4. 对第二节摘要候选的意见

候选：`Under working conditions, an OH binds to the Mn single atom on the side opposite to the reaction site. This axial OH weakens the binding of the ORR intermediates to Mn, so that OOH* formation is nearly thermoneutral and all other steps are downhill at 0.78 V.`

**方向比上一轮“弱 Mn–OH 键使 OOH* 强吸附”正确，并抓到了 T026 B→C。建议进一步压缩并对真实工作态严格措辞：**

> At the ORR-relevant potential, Mn single atoms in FeCoMn–NC are coordinated by an axial OH. Comparisons within FeCoMn–NC show that this ligand moderates the binding of ORR intermediates, yielding nearly thermoneutral OOH* formation and downhill subsequent steps at 0.78 V versus RHE.

直译：在与 ORR 相关的电位下，FeCoMn–NC 中的 Mn 单原子由轴向 OH 配位。FeCoMn–NC 内部的比较表明，这一配体调节了 ORR 中间体的吸附强度，使得在 0.78 V（vs RHE）下 OOH* 的生成接近热中性，后续步骤为自由能下坡。

**措辞证据提示：** “within FeCoMn–NC”依据 B/C 都是干净颗粒模型；“0.78 V 工作态”的自由能来自另一个 8O* 覆盖模型，全文正文必须把两种模型的相容性说清，不能让读者误以为两者是同一覆盖构型的直接差值。在完成 8O* 背景受控对照前，最严谨的摘要是：

> Under ORR conditions, Mn single atoms in FeCoMn–NC preferentially coordinate an axial OH, which moderates intermediate binding in model comparisons. On the calculated O*-covered working surface, OOH* formation is nearly thermoneutral and the remaining steps are downhill at 0.78 V versus RHE.

直译：在 ORR 条件下，FeCoMn–NC 的 Mn 单原子优先形成轴向 OH 配位，模型对照表明这一配体能够调节中间体吸附强度。在计算得到的 O* 覆盖工作表面上，OOH* 的生成接近热中性，而其余反应步骤在 0.78 V（vs RHE）下均为自由能下坡。

摘要最好最终压缩为一句机制 + 一句 ΔG；用 `moderates` 避免把所有三种中间体变化压成“弱键导致合适”的单一化学定理。不要写“OH 与 OOH* 同一轨道抢占”。

### 5. 建议图 6 的真正核心结构

1. **第一层：先提出受控反事实**——为何 OH* 不再束缚 Mn：引用 T026 干净 FeCoMn–NC，无轴向 OH 时 ΔG_OH*=0.4669 eV、U_L=0.4669 V、限制步 OH* 去除；加入轴向 OH 后 ΔG_OH*=0.8076 eV、U_L=0.7965 V、限制步 OOH* 形成；三中间体 ΔG 分别升高 0.2497/0.5091/0.3407 eV。说明 axial OH 不只是“工作态标识”，而是**可直接改变完整 ORR 自由能分布的配位变量**。
2. **第二层：确认真实工作态**——Fig.5 的 8O* 颗粒+Mn–OH，工作态 UL≈0.78 V；0.78 V 时第 1 步近平衡，其余下坡；注意 C 模型的 0.7965 V 非工作态实测。
3. **第三层：解释局域成键（辅助）**——Mn dz² 对 axial OH 与 OOH* 均有投影贡献，COHP 描述各键与吸附后的电子重排；自旋改变可作为支持，但不作“量子配对机理”的实证。
4. **第四层：其他催化剂作为边界验证**——Mn–NC axial O 导致 OOH* 形成困难；FeCo–NC O* 过强。火山图按既有 scaling 给出热力学折衷，而不是打破 scaling。
5. **第五层：颗粒归因**——T039 若发生翻转，可说明在固定几何条件下颗粒/其 O* 覆盖促进 axial OH 相对于 O；若不翻转则需相应降低 `determine` 的因果语气。

**最后再提醒一个有价值的反例**：T026 B→C 中 `ΔG(O*)` 上移最大（+0.5091 eV），而 `ΔG(OOH*)` 只上移 +0.2497 eV，说明 OH 引起的并非所有吸附物“均匀上移”。若 Fig.6 要讲 orbital-specific mechanism，需要分别解释各物种响应；不能把 0.25–0.51 eV 的不同变化都归结于相同的 dz² 占用程度。

### 推荐下一步
**优先核实有无 8O* 工作态无轴向 OH 的 ORR 全套既有数据，再决定是否补算；T040 的 LOBSTER 可以辅助成键描述，但即使得到 dz² −ICOHP 差值，也不能单独证明吸附能变化的原因。** 不推荐将“π 通道经 dz²”“一个自旋电子配对导致反位增强”“五配位自动防止过强吸附”等推断直接写进摘要。
