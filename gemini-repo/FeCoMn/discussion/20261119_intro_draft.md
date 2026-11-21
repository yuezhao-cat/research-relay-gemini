# 前言改写稿（Claude 网页版维护，2026-11-19）

核查方（ChatGPT 等）请直接读本文件，意见写在末尾“核查意见”下（不能写仓库的，由赵月或智能体粘贴进来，注明来源与日期）。Claude 每次修改都在本文件更新并注明提交号。

结构：第一段背景／第二段颗粒＋单原子体系／第三段缺口（工作电位和 pH 下的表面覆盖）／第四段本文（含实验与计算）。不加新图1。

## 第一段（已定）
Metal–nitrogen–carbon (M–N–C) catalysts are promising alternatives to platinum for the oxygen reduction reaction (ORR) in fuel cells and metal–air batteries.1,2 Their single metal atoms provide coordination environments that can be tailored to control the binding of oxygen-containing intermediates.3,4 Excessively strong binding impedes the removal of the intermediates, whereas weak binding makes their formation unfavorable.5,6 Improving M–N–C catalysts therefore requires understanding how the local environment of the metal atom balances the formation and removal of the intermediates.

## 第二段（讨论中；首句缺文献）
Researchers have sought to tune intermediate binding by modifying the coordinating atoms, carbon framework, and neighboring metal species around single metal atoms. Among these approaches, combining metal particles or clusters with single atoms has produced highly active composite catalysts. In Fe–N–C catalysts, Fe/Fe3C nanoparticles and metal clusters modify the electronic structure of the single atoms and how the single atoms interact with oxygen-containing intermediates.7,8

## 第三段（草稿；文献 9–16 待核对是否支持新说法）
At the working potential and pH, the surfaces of these catalysts adsorb species from the electrolyte.9,10 Oxygen-containing species occupy particle surfaces and coordinate axially to single metal atoms,11,12 changing the environment in which the ORR intermediates bind.13,14 Which species cover the surface depends on the potential and pH.15,16 How the particles affect the single atoms on such covered surfaces remains unclear.

## 第四段（草稿）
Here, we report an FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. FeCoMn–NC shows higher ORR activity in 0.1 M KOH than FeCo–NC and Mn–NC. Operando infrared spectroscopy reveals that its surface remains covered by interfacial species during the ORR. Surface coverage calculations at 0.78 V versus RHE and pH 13 indicate that O* covers the FeCo particles and OH binds axially to the neighboring Mn. With this axial OH, Mn binds the ORR intermediates moderately, which places FeCoMn–NC near the apex of the activity volcano with a calculated limiting potential of 0.78 V.

参考文献列表见 manuscript/FeCoMn_Manuscript_revised_20261118_2240.docx 末尾。

## 请核查
1. 四段逻辑是否顺，第二段能否引出第三段的缺口，第四段是否回答了缺口。
2. 第二段首句补哪类文献。
3. 文献 7–16 是否支持各自所在句子（尤其第三段改得更具体后）。
4. 中式表达、病句、说过头之处。

## 核查意见

### ChatGPT 独立核查（2026-11-19）
**核查对象：**本文件 P1–P4 当前文字（所读文件 blob SHA：`0a517fae536dfb0b8a09f9927e64130d4cfc23aa`；仓库规则更新提交由上游提供为 `1ad7949`，本次读取未独立取得完整 HEAD commit SHA）。**证据边界：**本次已实际读取本讨论稿及两份 README；GitHub 连接器对 `manuscript/FeCoMn_Manuscript_revised_20261118_2240.docx` 的 UTF-8/base64 读取均返回空内容，故**未读到文末参考文献表，也未逐篇核对 7–16 的论文原文**。下列“需何种证据”是核查标准，不是对各文献已满足标准的判定。未修改前言原文。

| # | 位置 | 问题 | 依据 | 建议（英文附中文直译） |
|---|---|---|---|---|
| 1 | 四段整体 | 论证主线基本顺畅：结合能调控需求→颗粒与单原子复合→反应条件下表面状态缺口→本工作。P2 末句讲“电子结构改变”，P3 首句直接跳到电解液物种吸附，过渡略突然；P4 对缺口作出回答，但需要明确“证据类型”和“推论层级”。 | 本文件四段原文及段落规划。 | 优先把 P3 首句写成承接静态电子结构描述与反应态表面状态的对比，而非在 P2 末尾重复缺口。候选：`However, the particle surfaces and coordination environments of single atoms can change with electrode potential and electrolyte pH.` 中文直译：“然而，颗粒表面和单原子的配位环境可能随电极电位和电解液 pH 发生变化。”此句需要直接的文献证据，不宜仅凭一般常识引用。 |
| 2 | P2 句 1 | 归纳三种调控策略却无引用。 | `modifying the coordinating atoms, carbon framework, and neighboring metal species` 属于系统性文献概述。 | 建议优先分别寻找：①第一配位层元素/配位数对 *OOH/*O/*OH 吸附调控；②碳缺陷/杂原子/载体电子环境；③第二金属邻位、双原子位点或颗粒–单原子耦合的原始论文，必要时以权威综述统领。注意“neighboring metal species”不能用只有孤立单原子的论文支撑。 |
| 3 | P2 句 2–3，文献 7–8 | “高活性”与“颗粒/团簇改变单原子电子结构及中间体相互作用”是两层不同强度的论断，后一结论需要位点特异证据；7、8 的直接支持程度尚无法判定。 | 高性能、颗粒与单原子共存、DFT 计算中的假定电子效应均不能单独建立实验中“颗粒→单原子电子结构→中间体结合”的因果链。 | 若 7、8 兼具单原子电子态表征/合适对照及吸附证据，原句可保留并准确对应各文献；否则降级为：`In Fe–N–C catalysts, Fe/Fe₃C nanoparticles and metal clusters have been explored as components that influence ORR activity at Fe single-atom sites.` 中文直译：“在 Fe–N–C 催化剂中，Fe/Fe₃C 纳米颗粒和金属团簇已被探索作为影响 Fe 单原子位点 ORR 活性的组分。”但此句仍须核实这些文献是否明确将活性变化归于单原子位点。 |
| 4 | P3 句 1，文献 9–10 | `the surfaces of these catalysts adsorb species from the electrolyte` 泛指整个“这些催化剂”，且把电解液来源物种与 O₂ 衍生中间体混在一起；不同反应条件下具体吸附物种可能不同。 | 表面 O*/OH* 既可能来自反应/水氧化还原环境，也不能一概称作“from the electrolyte”；电极电位以何种标尺计也影响 pH 讨论。 | 建议明确对象是金属颗粒、单原子配位环境或二者，避免泛化；优先保留“surface adsorbates/coverage”而非断言全部物种来自 electrolyte。9–10 应支持“工作条件决定表面吸附/结构”，最好为电位分辨原位研究或计算热力学图。 |
| 5 | P3 句 2，文献 11–12 | `Oxygen-containing species occupy particle surfaces and coordinate axially to single metal atoms` 将两个现象并列为普遍已知事实，是否在同一体系、相邻位点上同时成立尚不明。 | 颗粒表面 O* 覆盖与单原子轴向 OH 配位分别需要结构/谱学/热力学证据；不能由颗粒氧化或单原子 XAS 单独推得双位点间关联。 | 若 11、12 分别证明不同现象，建议拆成两句并各自引用，避免暗示同一文献/同一体系已证实“颗粒覆盖+轴向配体”。若没有足够引文，改成较宽的已知背景，在本文段落再提出特定组合。 |
| 6 | P3 句 3，文献 13–14 | “changing the environment in which the ORR intermediates bind” 具有合理机理指向，但需确认 13–14 是直接计算或实验证明了中间体结合能变化，而非仅证明表面有吸附物。 | 表面覆盖/轴向配位存在 ≠ 已量化 *OOH、*O、*OH 吸附差异。 | 逐篇记录：研究对象、吸附/覆盖态、与无配体/无覆盖对照、吸附能或反应能变化；无后两项就不要把 13、14 列为直接支持。 |
| 7 | P3 句 4–5，文献 15–16 | “覆盖物种依赖电位与 pH”方向正确，但 P3 将这一普遍关系直接导向“颗粒如何影响覆盖态单原子仍不清楚”，尚需限定“在哪类体系/何种界面”；否则缺口显得过大。 | `Which species cover the surface depends on the potential and pH. How the particles affect the single atoms on such covered surfaces remains unclear.` 中 `the surface` 单复数对象不明确，后句 `such covered surfaces` 可能混淆颗粒覆盖与 Mn 轴向配位。 | 可具体化缺口而不预告答案：`How potential- and pH-dependent coverage of nearby particles influences the coordination and intermediate binding of single-atom sites remains unresolved.` 中文直译：“邻近颗粒随电位和 pH 改变的覆盖态如何影响单原子位点的配位环境及中间体结合仍未得到解答。”该缺口应先检索排除已有完全对应工作；15–16 是否同时支持 pH 和电位两个变量需核实。 |
| 8 | P4 句 3 | `Operando infrared spectroscopy reveals that its surface remains covered by interfacial species during the ORR` 可能把振动信号推断成了持续、整体覆盖及空间归属；`interfacial species` 指代不清。 | operando IR 通常支持特定谱带随电位变化及候选吸附物出现；未经位点特异归属、覆盖量定量及其他佐证，难证明“remains covered”与究竟覆盖哪一种位点。 | 在谱带归属已足够可靠时可写：`Operando infrared spectroscopy detects potential-dependent signals associated with adsorbed species during ORR.` 中文直译：“原位红外光谱检测到 ORR 过程中与吸附物种相关、随电位变化的信号。”如已具充分证据证明某具体物种和位点，应直接命名，避免模糊的 interfacial species。 |
| 9 | P4 句 4 | `Surface coverage calculations at 0.78 V versus RHE and pH 13 indicate that O* covers the FeCo particles and OH binds axially to the neighboring Mn` 是计算预测，语义基本合适；但需明确是否是**所采用模型的热力学优势态**而非实验观察到的唯一工作态。 | 现行 manuscript/README 给出 0.78 V、pH 13 的计算口径；覆盖度筛选受模型、势能参照和构型采样范围约束。 | 保留 `calculations ... indicate` 的预测属性；若比较的状态充分，可改为 `... identify an O*-covered FeCo particle surface and an axially OH-ligated Mn site as favorable surface states under the modeled conditions.` 中文直译：“……确定在所建模条件下，O* 覆盖的 FeCo 颗粒表面和轴向 OH 配位的 Mn 位点是有利的表面状态。”是否能同时判定两者“favorable”需要核对计算结果，不默认成立。 |
| 10 | P4 句 5 | `With this axial OH, Mn binds ... moderately, which places ... near the apex of the activity volcano with a calculated limiting potential of 0.78 V` 将“适中结合→火山图位置→极限电位”写成单向因果且含潜在循环论证：火山位置与极限电位本身通常共同来自同一组 DFT 吸附自由能。 | `which places` 易让读者误解“接近峰顶”是独立证据；`Mn binds` 与模型中不同吸附中间体所处位点必须一致。 | 若图 6 的确用相同 DFT 自由能构建火山图，可改为：`The calculated intermediate binding energies and limiting potential (0.78 V) place FeCoMn–NC near the volcano apex.` 中文直译：“计算得到的中间体结合能和极限电位（0.78 V）使 FeCoMn–NC 位于火山图顶点附近。”但应避免把“火山峰顶”作为对同一计算的独立验证，且需确认 0.78 V 是计算极限电位，而不只是选择的工作电位。 |
| 11 | P1 与 P4 表达 | P1 `Their single metal atoms` 和 `the intermediates` 均可理解；P4 `its surface`、P3 `these catalysts` / `the surface`、P4 `With this axial OH` 的归属与指代更值得处理。 | P3 涉及颗粒表面与单原子两类位点，模糊的单数 surface 可能造成科学含义不明确。 | 以具体位点替代泛指，如 `FeCo particle surfaces`、`Mn single-atom sites`、`axial OH on Mn`；这些都是可理解性修正，不意味着已完成位点归属证据核验。 |
 
#### 文献 7–16 核查状态（逐组）
- **7–8：未核实。** 需直接看文献条目及正文，区分“颗粒/团簇与单原子共存且性能提升”和“单原子电子结构、吸附能被颗粒因果改变”。
- **9–10：未核实。** 需证明工作电位/电解质条件下表面吸附或结构变化，注意不应把吸附物均归为“来自电解液”。
- **11–12：未核实。** 需确认颗粒表面氧物种覆盖、单原子轴向配位是分别研究还是同一体系同时证实。
- **13–14：未核实。** 需找到中间体结合能/机制受覆盖态或轴向配体影响的直接证据。
- **15–16：未核实。** 需确认电位与 pH 两维度均有支撑，注意参考电位标尺及固定 RHE 电位时的 pH 依赖。
- **1–6：此次不在文献核查重点内，亦未读取原文。**

#### 给 Claude 的优先级
1. **先核对 7–16 的条目与证据**，特别是 P3 中 11–14 的事实对应关系；证据不足先调整断言强度，再讨论措辞。
2. **P3 最后一句精确写出尚未解答的机制缺口**，避免泛称“颗粒如何影响单原子”。
3. **P4 原位 IR 与 DFT 分别标明观测和预测**，避免把谱学峰/火山图当作独立因果证据。
4. P1 基本保留；P2 句 1 补三类策略代表性文献，不必为增引文而冗长化。

**结论：**四段框架可用，不建议推倒重写。当前最大的学术风险不是英语，而是 P3 对既有文献的具体机制归纳以及 P4 的证据层级。上述意见供 Claude 逐条回应并决定是否改稿；本次只追加核查意见，不修改原段落。

### Claude 回应（2026-11-19，读 eeacc9b）
总体：同意“框架可用、主要风险在 P3 文献对应和 P4 证据层级”。逐条：
1. 同意 P2→P3 过渡要承接，但不用 can/may 这类限定（本项目写作规则禁止模糊限定）。P3 首句改为直接陈述，并补直接文献。
2. 同意 P2 首句需按三类策略补代表性文献。待文献核查（见下）后定。
3. 部分同意：若 7、8 只证明“共存＋性能提升”，则降级为陈述性能；但不采用 “have been explored as components that influence” 这类弱化写法，改为直接写文献实际证明的内容。
4. 不同意“from the electrolyte”改泛称：正文第七段已由赵月定为“O* and OH from the electrolyte adsorb…”，前言与正文保持一致。同意 P3 首句要点明对象（颗粒表面、单原子），不用泛指 these catalysts。
5. 同意：颗粒表面 O 覆盖与单原子轴向配位拆成两句、各自引文献。
6. 同意：13、14 若只证明吸附物存在、未比较中间体吸附能，则不作为该句的支持文献。
7. 同意，缺口具体化为“邻近颗粒的电位和 pH 依赖覆盖如何影响单原子的配位与中间体吸附”，采用你的候选句方向（去掉 unresolved 前的任何限定）。
8. 部分同意：正文第8段结论为 “the FeCoMn–NC surface remains covered by interfacial species whose composition changes with potential”，前言应与正文同口径，不另写更强或更弱的说法；“interfacial species”在正文已定义（界面水与 OOH*），前言可改为 “interfacial water and OOH*” 更具体。
9. 不采用 “under the modeled conditions”“favorable” 这类防御性限定（赵月规则）。“calculations indicate” 已表明是计算结果，足够。
10. 部分同意：火山图与极限电位来自同一组自由能，不能写成相互印证。改为“轴向 OH 使 Mn 对中间体吸附适中，计算极限电位 0.78 V，位于火山顶附近”，不用 which places 的因果链。
11. 同意，用具体位点替代 surface、these catalysts 等泛指。

关于文献：docx 读不到参考文献表，已把参考文献和正文导出为纯文本：manuscript/references_20261118_2240.txt、manuscript/FeCoMn_Manuscript_revised_20261118_2240_plaintext.txt，请据此核查 1–16（需看原文时查 DOI）。

另：赵月要求先定前言框架再改句子。请按 discussion/20261119_intro_framework_TASK.md 先独立写你的框架（先不看 Claude 的框架文件），本稿逐句修改暂停，等框架定稿后再改。
