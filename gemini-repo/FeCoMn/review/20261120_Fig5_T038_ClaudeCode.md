# Fig 5 段落修订审阅：Claude Code

审阅人：Claude Code  
日期：2026-11-20  
审阅对象：`FeCoMn/discussion/20261120_1112_Fig5_T038_paragraph_for_review.md`，当前版本（Claude web 11:10）

---

## 问题 1：逻辑顺序与末句是否超出数据

逻辑链：**现象**（FeCoMn–NC 中 OH 比 O 稳定 0.18 eV，Mn–NC 中 O 比 OH 稳定 0.30 eV）→ **提问**（是否因颗粒直接改变 Mn 的电子结构）→ **检验**（删颗粒、几何不动）→ **结果**（电荷分布和 3d 电子态几乎不变）→ **结论**（颗粒的影响体现在轴向配体上，而不是裸 Mn 上）。

逻辑顺序成立。

末句（11:15 更新版）：
> "The effect of the FeCo particles on the Mn single atoms therefore appears in the axial ligand rather than in the bare Mn single atoms."

这句话从两条证据出发：(1) 裸 Mn（T038b）几乎不受颗粒影响；(2) 带配体的 Mn（T032/论文主线）受影响。从这两条可以推断"颗粒的影响体现在配体上"，结论和数据匹配，不超出证据范围。

**无异议。**

---

## 问题 2：原段末结构句移入括号后，与下一段衔接是否还在

原末句改为插入式："… and 1O* (an axial O on Mn) for Mn–NC (Figure 5g and Figure S24)."

下一段开头仍是 "On these covered surfaces…"，它指称的是这三种催化剂的覆盖态。结构句现在变成括号里的附属信息，不再是段落的收尾，但"这些覆盖表面"的指代仍可追溯到同一句中的"8O* + Mn–OH*"、"8O*"和"1O*"。读者能找到指代对象，衔接逻辑未断裂。

有一点值得注意：括号内 "(Figure 5g and Figure S24)" 原本是独立的强调句，现在变成附属括号，视觉上弱化了。是否需要在新加内容结束后单独恢复这个参考提示（例如在结论句末加 "(Figure S25)"之后再加一行跳转），可供赵月酌情决定。

**目前不阻塞，建议赵月决定是否保留视觉强调。**

---

## 问题 3："and pH 13, which corresponds to the 0.1 M KOH electrolyte"

RHE 电位已经把 pH 折算进去，表面覆盖度在 RHE 标度下确实不依赖 pH（Pourbaix 图横轴是 V vs SHE，纵轴是 pH，0.78 V vs RHE 对应的覆盖态在 pH 13 下取的就是这一行）。从科学角度，这个 pH 注释对覆盖结论没有必要。

但这句话同时出现在正文第 4 段末尾（"At 0.78 V versus RHE… and pH 13… the surface coverage is…"）。**正文中另一处（Figure 6i 末尾，第 362 行）也有"At the ORR working potential and pH 13"**，风格一致。两处都删或都留，不建议只删一处。

**建议赵月在与其他审阅人汇总后统一决定，不单独影响本段通过。**

---

## 问题 4：中式表达、长句、指代不清

逐句检查新加部分：

1. "Axial OH is more stable than axial O by 0.18 eV in FeCoMn–NC, whereas axial O is more stable than axial OH by 0.30 eV in Mn–NC (Table S6)."  
   表达清晰，无中式痕迹。"axial OH / axial O"出现 4 次，重复略重，但对于技术准确性是必要的。

2. "To test whether this difference arises because the FeCo particles directly change the electronic structure of the Mn single atoms, we removed the particles from the FeCoMn–NC model without changing the other atomic positions."  
   句子较长但结构清楚，主从逻辑顺畅，英文无误。"without changing the other atomic positions"精确交代了控制条件（符合"已否定写法"第 2 条的精神，不用 "models with and without"）。

3. "After this removal, the charge distribution and 3d electronic states of the Mn single atoms without axial ligands barely change (Figure S25)."  
   "After this removal"指代清晰。"without axial ligands"是限定语（T038b 算的正是无配体情况），准确。"barely change"相对于什么而变化？隐含的参照是保留颗粒的情况——读者能推断，但如果改成 "barely change relative to those in the full model" 会更严格。可选择性修改。

4. "The effect of the FeCo particles on the Mn single atoms therefore appears in the axial ligand rather than in the bare Mn single atoms."  
   无问题。

**整体通过。可选修订："barely change" → "barely change relative to those in the full model"。**

---

## 问题 5：编号核查（主任务）

插入两个新条目：
- **新图 S25**（T038b Mn 电子态不变的图）→ 现有 S25 起后移 1
- **新表 S6**（轴向配体稳定性：OH vs O 在两种催化剂中）→ 现有 S6 起后移 1

> 注意：SI 中的**方程编号**（S4、S6、S24–S33 等）使用独立序号，与图/表编号不共享，**不受影响，不需要修改**。

### 正文中受影响的引用（逐行列出）

| 位置 | 现在的写法 | 应改为 |
|------|-----------|--------|
| 正文第 300 行 | Table S7 | Table S8 |
| 正文第 301 行 | Table S8 and Figure S25 | Table S9 and Figure S26 |
| 正文第 302 行 | Figure S26 | Figure S27 |
| 正文第 309 行 | Table S7 | Table S8 |
| 正文第 331 行 | Table S9 | Table S10 |
| 正文第 345 行 | Figures S27 and S28 | Figures S28 and S29 |
| 正文第 347 行 | Table S9 | Table S10 |
| 正文第 353 行 | Figure S30 | Figure S31 |
| 正文第 357–358 行 | Table S7 | Table S8 |
| 正文第 383 行（Figure 6 题注）| Figure S29 | Figure S30 |

### SI 中受影响的引用

**目录（Table of Contents）：**

| 现在 | 应改为 |
|------|--------|
| Figure S25. Optimized ORR intermediates | Figure S26 |
| Figure S26. ORR free-energy diagrams at 0 V versus RHE | Figure S27 |
| Figure S27. Site-projected DOS of the intermediates | Figure S28 |
| Figure S28. Orbital-resolved PDOS… | Figure S29 |
| Figure S29. Bond-resolved metal–O −pCOHP… | Figure S30 |
| Figure S30. Adsorbate electron gain… | Figure S31 |
| Figure S31. Three-dimensional Δρ upon OH* adsorption | Figure S32 |
| Figure S32. Planar-averaged Δρ… | Figure S33 |
| Figure S33. Cumulative ΔN(z)… | Figure S34 |
| Table S6. Particle–support binding and structural recovery | Table S7 |
| Table S7. ORR free energies at 0 V versus RHE | Table S8 |
| Table S8. Metal–O distances of the intermediates | Table S9 |
| Table S9. Electronic descriptors… | Table S10 |
| Table S10. Coverage candidates and their free energies | Table S11 |
| Table S11. Relaxation-stage σ → 0 energies… | Table S12 |

**SI 正文内容（逐行）：**

| 行号 | 现在的写法 | 应改为 |
|------|-----------|--------|
| SI 403 | Table S10 and Figure S23 | Table S11 and Figure S23 |
| SI 407 | Table S10 | Table S11 |
| SI 437 | Table S7 | Table S8 |
| SI 472 | Table S11 | Table S12 |
| SI 533 | Figure S27 | Figure S28 |
| SI 535 | Figure S28 | Figure S29 |
| SI 595 | Figure S31 | Figure S32 |
| SI 600 | Figure S32 | Figure S33 |
| SI 603 | Figure S33 | Figure S34 |
| SI 660 | Table S6 | Table S7 |
| SI 664 | Table S6 | Table S7 |
| SI 764 | Table S10 | Table S11 |
| SI 784 | Table S10 | Table S11 |
| SI 792 | Table S10 | Table S11 |
| SI 907 | Figure S32 | Figure S33 |

**SI 图/表标题行（caption heading，作为标号本身）：**

| 现在 | 应改为 |
|------|--------|
| Figure S25. Optimized OOH*… | Figure S26 |
| Figure S26. ORR free-energy diagrams… | Figure S27 |
| Figure S27. Site-projected DOS… | Figure S28 |
| Figure S28. Orbital-resolved PDOS… | Figure S29 |
| Figure S29. Bond-resolved metal–O… | Figure S30 |
| Figure S30. Electron gain… | Figure S31 |
| Figure S31. Three-dimensional charge-density difference… | Figure S32 |
| Figure S32. Planar-averaged charge-density difference… | Figure S33 |
| Figure S33. Cumulative charge ΔN(z)… | Figure S34 |
| Table S6. Particle–support binding… | Table S7 |
| Table S7. ORR free energies… | Table S8 |
| Table S8. Metal–O distances… | Table S9 |
| Table S9. Site-resolved electronic descriptors… | Table S10 |
| Table S10. Coverage candidates… | Table S11 |
| Table S11. Relaxation-stage σ → 0 energies… | Table S12 |

### 不受影响的编号（确认）

- 方程 S6、S24–S33：独立序号，**不改**。
- Figure S6（Morlet wavelet transforms）：图 S6，**不改**（新增的是表 S6，不是图）。
- Table S5（coverage formation free energies，正文第一段已引用）：**不改**。
- Figure S24（ORR surface structures，新段落括号中明确保留）：**不改**。
- Figures S1–S24：均在 S25 之前，**不改**。
- Tables S1–S5：均在 S6 之前，**不改**。

### 总计需要修改的位置

| 类别 | 正文中 | SI 中 | 合计 |
|------|--------|-------|------|
| Figure 编号 | 10 处 | ~20 处（含 ToC、题注标题、正文引用）| ~30 处 |
| Table 编号 | 6 处 | ~18 处（含 ToC、表格标题、正文引用）| ~24 处 |

**建议赵月在 Word 中用"查找替换"操作，从最大编号往小编号顺序替换（先 S33→S34，再 S32→S33，依此类推；先 S11→S12，再 S10→S11，依此类推），防止连锁错误。**

---

## 综合意见

新段落内容准确，与已核验的 T038b 数据一致。结论"颗粒的影响体现在轴向配体上而非裸 Mn 上"严格由数据支撑。**主要工作是编号更新**，共约 54 处，建议批量替换而非逐一手动修改。