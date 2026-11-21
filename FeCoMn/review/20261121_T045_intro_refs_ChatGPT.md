# FeCoMn-T045 独立文献核查（ChatGPT，2026-11-21）

## 核查范围与方法
只读审查 GitHub `FeCoMn/manuscript/FeCoMn_Manuscript_revised_20261121_2150.txt`、`FeCoMn/to_agent/FeCoMn-T045_intro_refs_verify.md`；独立检索 DOI 与出版社/PMC 原文。**未修改 Word/SI；不能把当前网络可访问的全文/摘要核验冒充全部 PDF 逐页核验。** 原文页码仅对能确认的页面提供。结论按已证实/部分支持/待独立复核区分。

## 1. [D] 6–10
**支持。** 新增 Wang X. 等，*Adv. Mater.* 2020, **32**, 2000966，DOI 10.1002/adma.202000966。出版社/作者版本首页证实题名、作者、期刊、年份、文章号；第1页摘要介绍氮修饰双空位中 Fe–N4 位点与边缘碳缺陷对 ORR 性能的调控。可支持 carbon framework。来源：https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202000966；可读作者/出版社预览：https://www.researchgate.net/publication/339731875_Edge-Rich_Fe-N_4_Active_Sites_in_Defective_Carbon_for_Oxygen_Reduction_Catalysis 。

## 2. [F] 11
**部分支持，建议微调文字。** Wan X. et al., *Nat. Commun.* 2022, **13**, 2963，DOI 10.1038/s41467-022-30702-z；作者、题名、卷、文章号核实无误。原论文第2页 Introduction（PDF 排印页码 2）明确金属物种形态随含量与合成方法在单原子、团簇、纳米粒子之间变化，以及多层石墨碳包覆 Fe NP 在酸环境中可能存留；正文也有与单原子共存的含颗粒样品。它**不直接量化/证明所有热解 M–N–C “readily aggregate” 或“commonly coexist” 的普遍频率**，也并非直接报告“酸洗前后所有此类颗粒”的系统比较。建议改成 `Depending on metal loading and synthesis, pyrolyzed M–N–C catalysts can contain both single atoms and particles; graphitic-carbon-encapsulated particles can survive acidic treatment.` 避免泛化。
原文：https://pmc.ncbi.nlm.nih.gov/articles/PMC9135695/，PDF：https://www.nature.com/articles/s41467-022-30702-z.pdf 。

**高度重要的创新性先例：** Wan 2022 原文第7页 Discussion 及第5图展示 Fe 团簇诱导邻近 Fe–N4 形成轴向 OH 配体并改善 ORR。**不能声称首次发现颗粒诱导邻位单原子轴向 OH**。本稿区别应聚焦于 FeCo 颗粒对 Mn–OH/Mn=O 电位稳定性、0.48→0.96 V 变换、Mn 离面形变和吸附能分解的具体机制；应评估是否需要在前言显式区分 Wan 先例。

## 3. [G] 12–13
**作为两个代表性单原子活性中心实例成立；对 usually/alone 普遍性断言不足。**
Zitolo et al. *Nat. Mater.* 2015, 14, 937–942（DOI 10.1038/nmat4367）识别 FeN4 位点；Li et al. *Nat. Catal.* 2018, 1, 935–945（DOI 10.1038/s41929-018-0164-8）研究 MnN4 活性位。后二文突出原子级金属位，但不能代表所有文献把活性“solely”归于单原子。建议 `Many studies have focused on atomically dispersed metal–N sites as the principal ORR centers.` 并保持引用 12–13。
来源：https://pubmed.ncbi.nlm.nih.gov/26259106/；https://www.ornl.gov/publication/atomically-dispersed-manganese-catalysts-oxygen-reduction-proton-exchange-membrane-2 。

## 4. [E] 14–17
**当前原句证据不充分，建议修改。** 
- #14 Wang et al. *JACS* 2019, DOI 10.1021/jacs.9b07712：Fe–N–C 单原子位点反应中间体引起自调节，支持吸附物作用，不支持每种颗粒表面均有覆盖。
- #15 Zhao et al. *Nat. Catal.* 2025, DOI 10.1038/s41929-025-01324-7：高自旋 OH–FeN4 轴向羟基工作态，支持 M–N–C 单原子配体。
- #16 Yang et al. *Chem. Commun.* 2023, DOI 10.1039/d3cc03208f：DAC 电位依赖的预覆盖/表面覆盖度理论，支持单/双原子位表面态分析。
- #17 Hansen et al. *PCCP* 2008, DOI 10.1039/b803956a：Pt/Ag/Ni(111) 金属表面 Pourbaix/覆盖度，支持金属表面可被吸附物覆盖，不是 FeCo 纳米颗粒原位实证。

四篇合起来可以支持**表面覆盖需考虑且会受电位、pH 影响**，但不足以推出 `Under working conditions ... both metal particles and single atoms are covered by species from the electrolyte` 这个无条件断言。建议 `Under electrochemical conditions, adsorbates from the electrolyte can alter the surface states of both metal surfaces and atomically dispersed sites, depending on potential and pH.` 仍保留 14–17，避免把理论可能说成已实测本体系两处表面全部覆盖。
来源：https://pubmed.ncbi.nlm.nih.gov/31468961/ ; https://www.nature.com/articles/s41929-025-01324-7 ; https://pubmed.ncbi.nlm.nih.gov/37589047/ ; https://pubmed.ncbi.nlm.nih.gov/18563233/ 。

## 5. 引用完整性
按 GitHub 2150 纯文本编程检查：主文（含 Methods）中各参考文献首次出现顺序恰为 **1,2,...,40**；无缺号；文末参考列表有 **40** 个唯一编号。这里的检查是文本中的明确编号解析，**不代表 PDF/Word 域代码、图表题注或所有引文科学正确性均已核查。** SI 2150 原文未能在仓库取到，不能独立核验 `main-text ref. 12 → 3`，仅与 GitHub 的版本说明一致。

## 建议处理顺序
P0：明确 Wan 2022 既是 [F] 共存证据，也为“颗粒诱导 FeN4–OH”**相关先例**，避免创新性绝对化。
P1：改弱 [E] 两种位点 `are covered` 的全称断言。
P1：改弱 [G] 的 `usually ... alone`。
P2：把 [F] 泛化句收紧为 can coexist。
P2：待独立智能体逐页核查余下 PDF 和 SI Word（本报告不宣称全部完成）。

报告作者：ChatGPT，独立意见；请 Claude web 决定是否应用，遵守 ROOT ROLES.md，**本报告不直接改动任何成稿**。
