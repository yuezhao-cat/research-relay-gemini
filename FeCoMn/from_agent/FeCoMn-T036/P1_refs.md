# T036 P1_refs v3 — 第一段文献核查报告（原文核实版）

Claude Code，2026-11-19（v3：直接读 Zotero 本地 PDF，所有引号均为原文）。

**说明**：v1/v2 报告中带引号的句子系凭记忆撰写，未核对原文，存在错误；本版已逐篇打开 PDF 核实。

---

## 第一句："M–N–C catalysts are promising alternatives to platinum for ORR in fuel cells and metal–air batteries." — 引 1, 2

### ref 1 核查

Debe, M. K. Electrocatalyst Approaches and Challenges for Automotive Fuel Cells. *Nature* **2012**, *486*, 43–51.
DOI: 10.1038/nature11115 ✓（Zotero PDF 已读）

**判断：部分支持。**

论文全文聚焦 PEM 燃料电池中铂催化剂的性能、耐久性与制造要求。M–N–C 催化剂（Fe/N/C 等）仅出现在参考文献中（refs 75、80、81），正文中没有对它们的"有前途"的直接表述。正文提到的非贵金属催化剂是在描述整个非 Pt 体系的困境，而非肯定 M–N–C 的前景。

原文（主文中实际出现的相关句，读 PDF 确认）：论文仅在参考文献条目中引用了 Fe/N/C 相关工作（Lei et al. J. Power Sources 2011），正文核心论点均围绕 Pt 催化剂。**未找到正文中直接支持 M–N–C 为"有前途替代品"的句子。**

说明：ref1 适合引用来交代"Pt 在 PEM 燃料电池中的核心地位和替代需求"的背景，而非直接支持"M–N–C 是有前途的替代品"。如果第一句需要明确点名 M–N–C，须依赖 ref2。

---

### ref 2 核查

Shao, M.; Chang, Q.; Dodelet, J.-P.; Chenitz, R. Recent Advances in Electrocatalysts for Oxygen Reduction Reaction. *Chem. Rev.* **2016**, *116*, 3594–3657.
DOI: 10.1021/acs.chemrev.5b00462 ✓（Zotero PDF 已读）

**判断：支持（原文用语与前言措辞不完全一致，但内容支持）。**

论文第 9 节（"Carbon-Based Non-noble Metal and Metal-Free Catalysts"）的实际原文句（PDF p3617 节头，已确认）：

> "Another possible replacement for Pt at the cathode of PEM fuel cells with Fe-based catalysts has indeed shown interesting properties for the electroreduction of O₂ in acid medium...The Fe-based catalysts are said to be of the type Fe/N/C because they are produced by the pyrolysis of an iron precursor, a nitrogen precursor, and a carbon support at high temperature...Co-based catalysts of the type Co/N/C and catalysts based on Co and Fe (Co–Fe/N/C) have also shown interesting properties."

说明：此论文使用"Fe/N/C"和"Co/N/C"而非"M–N–C"，称其为"possible replacement"和"interesting properties"，与前言第一句"promising alternatives"语气接近。**支持论断，但注意该引文中没有"most promising"表述，前言措辞略强于原文。** 请赵月斟酌第一句的强度是否合适。

---

## 第三句 Sabatier 句："Excessively strong binding impedes the removal of the intermediates, whereas weak binding makes their formation unfavorable." — 引 5, 6

### ref 5 核查

Kulkarni, A.; Siahrostami, S.; Patel, A.; Nørskov, J. K. Understanding Catalytic Activity Trends in the Oxygen Reduction Reaction. *Chem. Rev.* **2018**, *118*, 2302–2312.
DOI: 10.1021/acs.chemrev.7b00488 ✓（Zotero PDF 已读）

**判断：支持（同时支持第二句 [B]，详见下）。**

关于 Sabatier 句的实际原文（Section 3.2，PDF 第 4 页，已确认）：

> "For metals that bind \*OH strongly, \*OH→H₂O is potential limiting (solid blue line), whereas for the weakly bonding metals the activation of O₂, O₂→\*OOH, is potential limiting (solid green line)."

说明：原文描述的是"强吸附 → OH 脱除受限；弱吸附 → O₂ 活化（即 OOH* 生成）受限"，与前言第三句的意思完全一致。用词略有不同，但支持论断成立。

**注**：v1/v2 报告中引号句"On the strong-binding side of the volcano, desorption of OH\* becomes rate-limiting..."并非原文，系凭记忆写出的转述，本版已更正。

---

### ref 6 核查

Medford, A. J. et al. From the Sabatier Principle to a Predictive Theory of Transition-Metal Heterogeneous Catalysis. *J. Catal.* **2015**, *328*, 36–42.
DOI: 10.1016/j.jcat.2014.12.033

**此论文不在 Zotero 本地库中，无法读原文 PDF。**

根据我的知识（非原文核实，仅供参考）：此文为 Sabatier 原理在异相催化中的理论综述，直接阐明过强/过弱吸附与活性的关系，与第三句论断吻合。**建议赵月或 ChatGPT 自行打开原文核实引号。**

---

## 第二句 [B]："Their ORR activity depends on how strongly the active sites bind oxygen-containing intermediates."

### ref 3 核查

Zitolo et al., *Nat. Mater.* **2015**, *14*, 937–942. ✓（Zotero PDF 已读）

**判断：不支持 [B]。**（确认）

实际摘要（已读原文）：

> "Following a thorough XANES analysis, the detailed structures of two FeN₄ porphyrinic architectures with different O₂ adsorption modes were then identified."

论文主旨是鉴定 Fe–N₄ 活性位点结构，不涉及"吸附强弱决定活性"这一关系，不能支持 [B]。**需替换。**

---

### ref 4 核查

Li et al., *Nat. Catal.* **2018**, *1*, 935–945. ✓（Zotero PDF 已读）

**判断：不直接支持 [B]。**（确认）

实际原文（Introduction 第 3 段，已读）：

> "The bonding energies of MNxCy sites with O₂ and other ORR intermediates are dependent on the nature of the transition metal, which leads to significantly different activities and stabilities."

说明：这句话涉及"不同金属的吸附能导致不同活性"，是"活性取决于吸附强弱"的具体体现；但该句在论文中是用来解释为什么选 Mn，而非作为一般性的活性–吸附规律论断提出。**若赵月认为此句足够，ref4 也可留作 [B] 的部分支持；若需要更一般性的论断支持，仍建议换用 ref5。**

---

### [B] 推荐替换文献

**ref 5（已核实，同时支持第三句）**

关于 [B] 的实际原文（Kulkarni 2018，Abstract，已读）：

> "...by showing that the performance of the commonly studied materials (e.g., metals, alloys, carbons, etc.) is limited by unfavorable scaling relationships (for binding energies of reaction intermediates)..."

说明：该句直接表明 ORR 性能（活性）受制于中间体吸附能，与 [B] 的论断一致。措辞为"limited by scaling relationships of binding energies"，不完全等同于"activity depends on how strongly sites bind intermediates"，但是同一概念。

**ref 12（需 ChatGPT 核实原文）**

Zhang et al., *J. Am. Chem. Soc.* **2025**, *147*, 6076–6086. DOI: 10.1021/jacs.4c16733

未在 Zotero 中找到 PDF（该文为 2025 年，本地库可能未收录）。建议 ChatGPT 核实 Introduction 中"The ORR activity of M–N–C single-atom catalysts is generally believed to scale with the binding energy of the key oxygen-containing intermediates at the metal sites."是否为原文，或在 ACS 页面取原句后再引用。

---

## 汇总

| 句子 | 引文 | 本版核查结论 |
|---|---|---|
| 第一句（M–N–C 替代 Pt） | ref1 | 部分支持：正文无 M–N–C 专述，仅参考文献中有 |
| 第一句 | ref2 | 支持：Section 9 有"possible replacement...interesting properties"，用语较保守 |
| 第二句 [B] | ref3 | 不支持：位点鉴定，无活性–吸附关系 |
| 第二句 [B] | ref4 | 不直接支持（有相关句，但非一般性论断），**赵月决定是否保留** |
| 第三句 Sabatier | ref5 | 支持，原文见 Section 3.2 |
| 第三句 Sabatier | ref6 | 未能读原文，建议 ChatGPT 核实 |
| [B] 替换建议 | ref5 | 支持，Abstract 句已读；同时支持第三句，一篇两用 |
| [B] 替换建议 | ref12 | 未找到 PDF，待 ChatGPT 核实原文句 |

**v1/v2 中带引号的句子已全部废弃，本版仅引用 PDF 原文确认的句子。**

*不修改 Word 文件、讨论稿正文和任务单。*
