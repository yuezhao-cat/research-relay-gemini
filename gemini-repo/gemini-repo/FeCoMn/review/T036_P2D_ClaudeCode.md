# T036 [D] 碳骨架文献 — Claude Code 复核报告

Claude Code，2026-11-19。
复核依据：直接读 Zotero 本地 PDF，逐字对比 Antigravity 报告（commit 8a9984b）中的引文。

---

## 候选 1 复核：Wang et al., Adv. Mater. 2020, 32, 2000966

PDF：`D:\Zotero\storage\659FRH95\Wang 等 - 2020 - Edge-Rich Fe−N4 Active Sites in Defective Carbon for Oxygen Reduction Catalysis.pdf`

### Abstract 句（p. 1 of 8）

**Antigravity 报告引文：**
> "Herein, a fundamental investigation of unfolding intrinsically superior edge-ND trapped atomic Fe motifs (e-ND−Fe) relative to an intact center model (c-ND−Fe) in ORR electrocatalysis is reported. Density functional theory calculations reveal that local electronic redistribution and bandgap shrinkage for e-ND−Fe endow it with a lower free-energy barrier toward direct four-electron ORR. Inspired by this, a series of atomic Fe catalysts with adjustable ND−Fe coordination are synthesized, which verify that ORR performance highly depends on the concentration of e-ND−Fe species."

**复核结论：✓ 逐字一致。**

### DFT 节句（p. 2 of 8）

**Antigravity 报告引文：**
> "As seen clearly, the electron redistribution of e-ND−Fe is more obvious than c-ND−Fe, leading to higher electron density around Fe−N4 active sites... Gibbs free energy diagrams at different equilibrium potential (U) are further calculated to theoretically predict the ORR activity difference between c-ND−Fe and e-ND−Fe (Figure 1c,d)... However, at U = 1.23 V (reversible hydrogen electrode (RHE) at T = 298.15 K), both of them have their own largest energy barrier toward ORR, 0.58 eV for c-ND−Fe versus 0.43 eV for e-ND−Fe... The predictive onset potential is further offered to reflect the practical performance of ORR (0.65 V for c-ND−Fe and 0.8 V for e-ND−Fe)."

**复核结论：✓ 逐字一致（省略号部分为原文中间句，均已读到，不影响核心论点）。**

**对 P2 [D] 句的支持性说明**：此文以 e-ND−Fe 和 c-ND−Fe 控制变量，两者均为 Fe–N4 第一配位层不变，仅碳基底位置（边缘缺陷 vs 中心完整平面）不同，属于**纯碳骨架效应控制变量研究**。直接支持"改变碳骨架改变中间体吸附与 ORR 活性"。

**判断：强支持，推荐作为 [D] 碳骨架类引文。**

---

## 候选 2 复核：Zhao et al., Adv. Mater. 2024, 36, 2308243

PDF：`D:\Zotero\storage\4246GFQ8\Vacancy Defects Inductive Effect of Asymmetrically Coordinated Single‐Atom Fe─N3S1 Active Sites for.pdf`

### Abstract 句（p. 1 of 14）

**Antigravity 报告引文：**
> "Theoretical calculation reveals the upshifted d band center of Fe─N3S1 active sites facilitates the adsorption of O2 and accelerates the kinetics process of *OH reduction. The abundant vacancy defects around the Fe─N3S1 active sites balance the OOH* formation and *OH reduction, thus **synergistically** promoting the electrocatalytic ORR process."

**实际原文：**
> "...thus **synergetically** promoting the electrocatalytic ORR process."

**复核结论：⚠ 一字之差。** 原文为 "synergetically"，Antigravity 报告写的是 "synergistically"。这两个词都有实际使用，原文拼写是 "synergetically"，引用时须用原文。其余逐字一致。

### DFT 节句（p. 11 of 14）

**Antigravity 报告引文：**
> "which suggests the presence of sulfur atoms is beneficial to OH* reduction, and the inductive effect of the vacancy and the coordinated sulfur atom plays a key role in the balance between OOH* formation and *OH reduction."

**复核结论：✓ 逐字一致。**

**对 P2 [D] 句的支持性说明**：此文研究碳基底空位缺陷对 Fe–N3S1 单原子位点中间体吸附的调控。需注意：本文体系为 **Fe–N3S1**（非对称配位，含 S），与候选 1 的 Fe–N4 不同，第一配位层也有变化。"碳骨架效应"（空位缺陷诱导效应）和"配位原子"（S 取代 N）是共同起作用的，不是纯碳骨架控制变量。作为 [D] 碳骨架类的辅助引文可以，但需在写作中措辞谨慎（不声称仅碳骨架起作用）。

**判断：支持（作为备选/并引文献），使用时注意措辞范围。**

---

## 汇总

| 候选 | 复核 | 建议 |
|---|---|---|
| Wang 2020 Adv. Mater. (DOI: 10.1002/adma.202000966) | ✓ 两处引文逐字一致 | **推荐作为 [D] 碳骨架类首选引文** |
| Zhao 2024 Adv. Mater. (DOI: 10.1002/adma.202308243) | ⚠ 摘要一字差（"synergetically" vs "synergistically"）；DFT 句逐字一致 | 可作备选；使用时须注明原文拼写，并在写作中说明碳骨架+配位原子共同作用 |

**两篇均不在现有 refs 1–39 中，须作为新文献编号加入。** 编号由赵月统一排定后通知写稿方。

*不修改 Word 文件、讨论稿正文和任务单。*
