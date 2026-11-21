# FeCoMn-T042 文献调研：轴向配体为什么削弱吸附，颗粒为什么决定轴向配体

下达：Claude web 2，2026-11-20 16:15，赵月指示（“让智能体去读文章”）。
分工：Antigravity 主做检索与摘录，Claude Code 抽查引用和数值。GPT 查结论是否准确、有无遗漏。
交付：`FeCoMn/from_agent/FeCoMn-T042/REPORT.md`，以及 `papers.csv`（每篇一行）。

## 目的

全文机理主线是“颗粒 → Mn 带轴向 OH 而不是 O → 轴向 OH 把过强吸附调到适中 → 活性最高”。现在有两环讲不出内在原因，需要看文献里别人是怎样解释的，有没有现成的理论框架可以直接借用，避免我们自己凭空编解释。

- **问题 A（第 4 环）**：在 M–N4 单原子（尤其 Mn、Fe、Co）上，轴向配体为什么会削弱对位 ORR 中间体的吸附？文献用什么解释，例如反位影响（trans influence）、dz² 被两侧共用、金属离面位移与形变能、d 带中心、自旋态。有没有人做过形变能与电子结合的能量拆分？
- **问题 B（第 2 环）**：邻近的金属颗粒或团簇怎样影响单原子位点的轴向配体？颗粒会不会决定单原子带 OH 还是 O（或带不带配体）？文献给出的机理是什么，例如电子转移、费米能级钉扎、磁耦合、静电场、载体形变？
- **问题 C（对照）**：轴向 –OH 与 =O 的比较。有没有文献在同一个 M–N4 上同时算过轴向 OH 和轴向 O，并解释为什么 O 削弱得更多？

我们已有的数据（供对照，不必重复检索）：同一 FeCoMn–NC，无轴向 OH 时 U_L 0.52 V，有轴向 OH 时 0.78 V；OH* 削弱 0.34 eV 中 0.24 eV 来自 Mn 被拉回 N4 平面的形变；轴向 OH 把 Mn 拉出平面 0.44 Å，Mn–NC 的 Mn=O 拉出 0.51 Å。

## 检索规程

1. 数据库：Web of Science、Google Scholar、ACS、RSC、Wiley、Elsevier。优先 2018–2026 年，经典理论文献（反位影响、卟啉金属离面）不限年份。
2. 关键词组合（中英文结果都看英文原文）：
   - axial ligand / axial coordination / fifth coordination + M–N4 / single-atom + ORR / OH adsorption
   - trans influence / trans effect + metalloporphyrin / M–N4 + oxygen
   - metal out-of-plane displacement / doming + porphyrin / single-atom + adsorption energy
   - deformation energy / distortion–interaction / energy decomposition + single-atom catalyst
   - nanoparticle / cluster + adjacent single atom + axial / electronic interaction + ORR
   - Mn–N–C + axial OH / Mn=O / oxo + ORR
3. 每个问题至少 8 篇，总数 25–40 篇。必须读到原文（正文加 SI），只看摘要的不算。
4. 下面是 Claude web 2 初检得到的起点，请核实并读原文：
   - Luo et al., Impact of Halogen Axial Coordination on the Electronic and Magnetic Properties of MN4 SACs for ORR, PCCP 2025（d5cp04404a）。用金属离面位移 h1、h2 作为轴向配体效应的指标，与我们的几何图像直接相关。
   - Zhang et al., Strategy to weaken the oxygen adsorption on single-atom catalysts towards oxygen-involved reactions, Mater. Today Adv. 16, 100280 (2022)。在多种 SAC 上比较轴向 –OH、=O、≡N，报告吸附随轴向键增强而减弱，与问题 C 直接相关。
   - Boosting the catalytic activity of water splitting and ORR through axial coordination to MN4–C model catalysts, J. Mater. Chem. A 13, 24948 (2025)（d5ta01464f）。
   - Mou et al., Axial Coordination Engineering on Fe−N−C Materials for ORR, Chem. Eur. J. 30 (2024)。
   - Wei et al., MnN4-doped graphene with axial halogen ligands, Molecules 29, 3517 (2024)。
   - Axial traction（Ni–N4–O），Angew. Chem. Int. Ed. 60, 4192 (2021)。
   - 轴向 Fe 团簇作用于 Fe1–N–C 的 ORR，Angew. Chem. 2025（PMC12304842，含有轴向与非轴向团簇的 PCOHP 对比），与问题 B 直接相关。
   - Iron atom–cluster interactions increase activity and durability in Fe–N–C fuel cells, Nat. Commun. 13, 2963 (2022)。
   - Electronically and Geometrically Modified Single-Atom Fe Sites by Adjacent Fe Nanoparticles for Enhanced Oxygen Reduction（Fe 纳米颗粒同时改变 Fe–N–C 的电子与几何结构）。
   - 二级配位效应选择性稳定 OOH*（ChemRxiv 65eebf809138d23161320412，相邻 M–N4 位点的轴向配体）。

## 每篇摘录字段（papers.csv）

DOI、期刊年份、体系（金属、配位、载体、有无颗粒）、方法（DFT 泛函、U 值、溶剂化、是否考虑自旋）、轴向配体种类、受影响的中间体及能量变化（eV）、是否报告金属离面位移（数值）、是否做能量拆分（形变与电子各多少）、作者给出的机理解释（用自己的话写一句，不超过 40 字，必要的原文短语不超过 15 词并注页码或图号）、与我们哪一环相关（A、B、C）、可借用程度（直接可引、部分支持、矛盾）。

## REPORT.md 结构

1. 问题 A、B、C 各自的结论：文献主流解释是什么，有几篇支持，有没有相互矛盾的说法。
2. 与我们数据的对照：哪些文献的数据或解释和我们一致（例如离面位移、形变能占比、OH 与 O 的差别），哪些不一致。
3. 可以直接写进正文或 SI 的引用建议，每条注明支撑哪一句。
4. 若文献中有我们没想到、但能用已有数据检验的解释，单独列出，并写明用哪项已有数据检验。

## 注意

- 不下载或上传有版权限制的全文到仓库，只放 DOI、摘录和自己的总结。
- 不写主观判断“我们的结果新颖”之类的话，只报告文献说了什么。
- 本任务不涉及新计算。

## 17:00 合并说明（Claude web）
本任务与 Claude web 16:30 的 `FeCoMn/discussion/20261120_1630_literature_survey_ALL.md` 重叠。为避免重复劳动，以后者为准：四方按其中分工各查各的方向，并在汇总里回答本文件的问题 A、B、C。交付统一写到 `FeCoMn/review/20261120_literature_<名字>.md`，不再单独写 from_agent/FeCoMn-T042/REPORT.md。
