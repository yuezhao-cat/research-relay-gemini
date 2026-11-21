# T036 补充任务：第二段 [D] 碳骨架文献检索报告（Antigravity）

- **读取任务单提交号**：`9e27a19`（`FeCoMn/to_agent/FeCoMn-T036_intro_reference_search.md` 补充任务，对应第二段首句 `"Researchers have tuned the binding of ORR intermediates by modifying the coordinating atoms and carbon framework of M–N–C catalysts or by introducing neighboring metal species."`）
- **检索与核查方法**：直接在本地 Zotero（`D:\Zotero\storage`）检索并打开原文 PDF，逐字摘录英文支持句并核对页码与 DOI，不需用户另行下载 PDF。

---

## 1. 推荐文献（均已有 Zotero 原文 PDF 并逐字核实）

### 候选 1（首选，纯“碳骨架边缘缺陷”控制变量，配位原子同为 Fe–N₄）

- **引文（ACS 格式）**：
  Wang, X.; Jia, Y.; Mao, X.; Liu, D.; He, W.; Li, J.; Liu, J.; Yan, X.; Chen, J.; Song, L.; Du, A.; Yao, X. Edge-Rich Fe−N4 Active Sites in Defective Carbon for Oxygen Reduction Catalysis. *Adv. Mater.* **2020**, *32*, 2000966.
- **DOI**：`10.1002/adma.202000966`
- **本地原文 PDF**：`D:\Zotero\storage\659FRH95\Wang 等 - 2020 - Edge-Rich Fe−N4 Active Sites in Defective Carbon for Oxygen Reduction Catalysis.pdf`
- **支持判断**：**强支持**（在不改变 $\text{Fe–N}_4$ 第一配位层的前提下，仅比较碳基底边缘缺陷 `e-ND−Fe` 与完整碳平面中心 `c-ND−Fe`，用 DFT + 实验直接证明碳骨架缺陷环境改变电子分布、ORR 自由能垒与催化活性）。
- **逐字原文支持句与位置**：
  - **p. 1（`2000966 (1 of 8)`, Abstract）**：
    > "Herein, a fundamental investigation of unfolding intrinsically superior edge-ND trapped atomic Fe motifs (e-ND−Fe) relative to an intact center model (c-ND−Fe) in ORR electrocatalysis is reported. Density functional theory calculations reveal that local electronic redistribution and bandgap shrinkage for e-ND−Fe endow it with a lower free-energy barrier toward direct four-electron ORR. Inspired by this, a series of atomic Fe catalysts with adjustable ND−Fe coordination are synthesized, which verify that ORR performance highly depends on the concentration of e-ND−Fe species."
  - **p. 2（`2000966 (2 of 8)`, 正文 DFT 节）**：
    > "As seen clearly, the electron redistribution of e-ND−Fe is more obvious than c-ND−Fe, leading to higher electron density around Fe−N4 active sites... Gibbs free energy diagrams at different equilibrium potential (U) are further calculated to theoretically predict the ORR activity difference between c-ND−Fe and e-ND−Fe (Figure 1c,d)... However, at U = 1.23 V (reversible hydrogen electrode (RHE) at T = 298.15 K), both of them have their own largest energy barrier toward ORR, 0.58 eV for c-ND−Fe versus 0.43 eV for e-ND−Fe... The predictive onset potential is further offered to reflect the practical performance of ORR (0.65 V for c-ND−Fe and 0.8 V for e-ND−Fe)."

---

### 候选 2（备选/并引，碳基底空位缺陷诱导效应调控中间体吸附平衡）

- **引文（ACS 格式）**：
  Zhao, Y.; Chen, H.-C.; Ma, X.; Li, J.; Yuan, Q.; Zhang, P.; Wang, M.; Li, J.; Li, M.; Wang, S.; Guo, H.; Hu, R.; Tu, K.-H.; Zhu, W.; Li, X.; Yang, X.; Pan, Y. Vacancy Defects Inductive Effect of Asymmetrically Coordinated Single-Atom Fe─N3S1 Active Sites for Robust Electrocatalytic Oxygen Reduction with High Turnover Frequency and Mass Activity. *Adv. Mater.* **2024**, *36*, 2308243.
- **DOI**：`10.1002/adma.202308243`
- **本地原文 PDF**：`D:\Zotero\storage\4246GFQ8\Vacancy Defects Inductive Effect of Asymmetrically Coordinated Single‐Atom Fe─N3S1 Active Sites for.pdf`
- **支持判断**：**支持**（研究碳基底空位缺陷的诱导效应对单原子中心 `d` 带中心与中间体吸附 `OOH*` / `*OH` 平衡的调控，且文中对比了有空位与无空位碳基底模型 `Fe SAs/NSC-vd` vs `Fe SAs/NSC`）。
- **逐字原文支持句与位置**：
  - **p. 1（`2308243 (1 of 14)`, Abstract）**：
    > "Theoretical calculation reveals the upshifted d band center of Fe─N3S1 active sites facilitates the adsorption of O2 and accelerates the kinetics process of *OH reduction. The abundant vacancy defects around the Fe─N3S1 active sites balance the OOH* formation and *OH reduction, thus synergistically promoting the electrocatalytic ORR process."
  - **p. 11（`2308243 (11 of 14)`, DFT 节）**：
    > "which suggests the presence of sulfur atoms is beneficial to OH* reduction, and the inductive effect of the vacancy and the coordinated sulfur atom plays a key role in the balance between OOH* formation and *OH reduction."

---

## 2. 建议引用方案

- 若仅需 **1 篇** 代表“碳骨架（缺陷/边缘拓扑）调控”，**首选 `Wang et al., Adv. Mater. 2020, 32, 2000966`（DOI: `10.1002/adma.202000966`）**，因为其第一配位层保持 `Fe–N4` 不变，纯以碳骨架边缘缺陷（`e-ND−Fe` vs `c-ND−Fe`）控制变量，逻辑最干净。
- 若需 **2 篇**（覆盖碳边缘缺陷 + 碳基底空位诱导效应），可同时引 `Wang 2020` 与 `Zhao 2024`（DOI: `10.1002/adma.202308243`）。
- 交由 Claude Code 复核并写入 `review/T036_P2D_ClaudeCode.md`。
