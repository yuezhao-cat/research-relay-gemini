# 图 5 第一段：加入 T038/T038b 对照计算（征求意见）

发起：Claude web，2026-11-20 11:12
请 ChatGPT、Antigravity、Claude Code 各自独立审阅，结果写到 FeCoMn/review/20261120_Fig5_T038_<名字>.md。最终由赵月决定。

## 已定事项（赵月 2026-11-20 确认）
- T038/T038b 写进正文一句加 SI 完整数据，不只放附件。
- 放在图 5 覆盖度讨论中，不放图 6。图 6a–c 比较的是带配体的 Mn（Mn–OH、Mn=O），T038 算的是无配体 Mn，放进去会混。
- 不能放在段末：原段末句"The corresponding structures are shown in Figure 5g and Figure S24"和下一段开头"On these covered surfaces"相互呼应。
- 摘要、前言、题目暂不调整。T032 推导值核实前不写进正文。

## T038/T038b 数据（Antigravity 已核实，6f47d72）
| 比较 | 含颗粒 | 不含颗粒 | Mn Bader 差 | dz² 中心差 |
|---|---|---|---|---|
| C vs C_support | FeCoMn–NC 模型（颗粒 8O*） | 同一结构删去颗粒，几何不动 | +0.006 e | +0.032 eV |
| A vs As | FeCoMn–NC 模型（洁净颗粒） | 同一结构删去颗粒，几何不动 | +0.007 e | +0.013 eV |
| As vs B | 删去颗粒的结构 | Mn–NC（独立优化） | −0.040 e | +0.002 eV |

Mn 都是无轴向配体、约 3.1 μB 的高自旋，磁矩变化约 −0.01 μB。配体相对稳定性（0.78 V，原表 S10）：FeCoMn–NC 中 OH 比 O 稳定 0.18 eV；Mn–NC 中 O 比 OH 稳定 0.30 eV。

## 原文（Manuscript_revised_20261119_2255，图 5 第一段）
The free energies of many different coverage configurations were therefore compared to determine the surface states of the three catalysts at various potentials and pH (Figure 5 and Table S5). As shown in Figure 5a–c, the surfaces of all three catalysts are covered by H* at negative potentials, and adsorbed O-containing species become more stable as the potential increases. As shown in Figure 5d–f, the surface coverage of FeCoMn–NC changes from 8H* to 8O* with increasing potential, then to 8O* + Mn–OH*, and finally to 8O* + Mn–O*. The surface coverage of FeCo–NC changes only from 8H* to 8O*, whereas that of Mn–NC changes from 3H* to the clean surface and then to 1O* and 2O*. Figures S13–S16 and S17–S22 give the corresponding free-energy data and structures, respectively. At 0.78 V versus RHE (a representative ORR potential)¹¹ and pH 13, which corresponds to the 0.1 M KOH electrolyte, the surface coverage is 8O* + Mn–OH* for FeCoMn–NC, 8O* for FeCo–NC, and 1O* for Mn–NC. The corresponding structures are shown in Figure 5g and Figure S24.

## 当前版本（Claude web 11:10，「」为改动）
The free energies of many different coverage configurations were therefore compared to determine the surface states of the three catalysts at various potentials and pH (Figure 5 and Table S5). As shown in Figure 5a–c, the surfaces of all three catalysts are covered by H* at negative potentials, and adsorbed O-containing species become more stable as the potential increases. As shown in Figure 5d–f, the surface coverage of FeCoMn–NC changes from 8H* to 8O* with increasing potential, then to 8O* + Mn–OH*, and finally to 8O* + Mn–O*. The surface coverage of FeCo–NC changes only from 8H* to 8O*, whereas that of Mn–NC changes from 3H* to the clean surface and then to 1O* and 2O*. Figures S13–S16 and S17–S22 give the corresponding free-energy data and structures, respectively. At 0.78 V versus RHE (a representative ORR potential)¹¹ and pH 13, which corresponds to the 0.1 M KOH electrolyte, the surface coverage is 8O* + Mn–OH* for FeCoMn–NC, 8O* for FeCo–NC, and 1O* 「(an axial O on Mn)」 for Mn–NC 「(Figure 5g and Figure S24). Axial OH is more stable than axial O by 0.18 eV in FeCoMn–NC, whereas axial O is more stable than axial OH by 0.30 eV in Mn–NC (Table S6). To test whether this difference arises because the FeCo particles directly change the electronic structure of the Mn single atoms, we removed the particles from the FeCoMn–NC model without changing the other atomic positions. After this removal, the charge distribution and 3d electronic states of the Mn single atoms without axial ligands barely change (Figure S25). The effect of the FeCo particles on the Mn single atoms therefore appears in the axial ligand rather than in the bare Mn single atoms.」

直译：……（前同原文）……在 0.78 V 相对于 RHE（一个代表性的 ORR 电位）¹¹ 和 pH 13（对应 0.1 M KOH 电解液）下，FeCoMn–NC 的表面覆盖为 8O* + Mn–OH*，FeCo–NC 为 8O*，Mn–NC 为 1O*「（Mn 上的一个轴向 O）（图 5g 和图 S24）。在 FeCoMn–NC 中，轴向 OH 比轴向 O 稳定 0.18 eV，而在 Mn–NC 中，轴向 O 比轴向 OH 稳定 0.30 eV（表 S6）。为了检验这一差别是否因为 FeCo 颗粒直接改变了 Mn 单原子的电子结构，我们从 FeCoMn–NC 模型中去掉颗粒，其他原子位置不变。去掉颗粒后，无轴向配体 Mn 单原子的电荷分布和 3d 电子态几乎不变（图 S25）。因此，FeCo 颗粒对 Mn 单原子的影响体现在轴向配体上，而不是体现在裸 Mn 单原子上。」

逻辑：现象（OH 对 O 及稳定性差）→ 提问（是否因颗粒直接改变 Mn）→ 检验（删颗粒、几何不动）→ 结果（几乎不变）→ 结论（颗粒的影响体现在轴向配体上，而不是裸 Mn 上）→ 下一段"On these covered surfaces…"。

## 讨论中已否定的写法（避免重复）
- "Controlled calculations show…"：读者不知道控制了什么。
- "models with and without the FeCo particles"：读者会以为不含颗粒就是 Mn–NC。
- "the two catalysts differ…"：段中有三种催化剂，指代不清；而且 T038 比较的是同一模型加或不加颗粒。
- 主动方：是电解液中的物种（OH/O）吸附到 Mn 上，不是 Mn 吸附配体。
- 不用 only / emerges only。

## 请重点审
1. 逻辑顺序是否成立；"therefore act … through the axial ligand"是否超出数据（T038 只算了无配体 Mn）。
2. 原段末结构句并入括号后，与下一段"On these covered surfaces"的呼应是否还在。
3. "and pH 13, which corresponds to the 0.1 M KOH electrolyte"：覆盖度在 RHE 标度下与 pH 无关，是否删除。
4. 中式表达、长句、指代不清。
5. 编号：新图 S25（原 S25 起顺延），新表 S6（原 S6 起顺延）。请 Claude Code 核对正文和 SI 中受影响的全部引用。

## 11:15 更新（赵月指出）
原末句 "therefore act on the Mn single atoms through the axial ligand" 推导不出：证据只说明影响体现在配体上，没有说明颗粒如何改变配体偏好。已改为 "The effect of the FeCo particles on the Mn single atoms therefore appears in the axial ligand rather than in the bare Mn single atoms." 第 1 个审阅问题相应改为：新末句是否严格由前两条证据得出。
