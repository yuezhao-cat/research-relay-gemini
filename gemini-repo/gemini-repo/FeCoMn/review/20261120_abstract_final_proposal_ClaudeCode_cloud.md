# 摘要定稿建议（Claude Code 云端，2026-11-20）

读过：Claude web 合并稿 ea3f832、Antigravity ec8d345、GPT 812497f、Claude web 2 a0f80c0、本人 84143b6。
结论：以 Claude web 合并稿为底（已吸收各家），做 3 处改动。

## 建议定稿

Pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts often contain metal particles alongside single-atom sites, yet how the surface state under working conditions controls the binding of oxygen reduction reaction (ORR) intermediates remains unclear. Here, we prepare an FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches a half-wave potential of 0.885 V versus RHE, surpassing Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h. Operando infrared spectroscopy shows that the surface species change with potential, so we calculated the surface coverage under working conditions. At 0.78 V, the FeCo particles are covered by O*, and the adjacent Mn single atoms carry an axial OH. Without this OH, ORR intermediates pull the Mn atom out of the N4 plane toward themselves and bind too strongly. The axial OH holds Mn on the opposite side of the plane, so an intermediate can only pull it back into the plane. The energy spent on this deformation weakens the over-strong OH* binding while OOH* formation remains nearly thermoneutral, placing FeCoMn–NC near the apex of the activity volcano. These results show that an axial OH formed under working conditions can balance ORR intermediate binding through the geometry of the Mn single atom.

## 直译
热解 M–N–C 催化剂常同时含金属颗粒和单原子位点，但工作条件下的表面状态如何控制 ORR 中间体的吸附尚不清楚。本文制备了 FeCo 合金颗粒与 Mn 单原子共存的 FeCoMn–NC。在 0.1 M KOH 中，其半波电位 0.885 V vs RHE，优于 Pt/C、FeCo–NC 和 Mn–NC，238 h 后保持 96.5% 初始电流。原位红外显示表面物种随电位变化，因此我们计算了工作条件下的表面覆盖。0.78 V 下，FeCo 颗粒被 O* 覆盖，相邻 Mn 单原子带轴向 OH。没有这个 OH 时，中间体把 Mn 从 N4 平面拉向自己一侧，吸附过强。轴向 OH 把 Mn 留在平面另一侧，中间体只能把它拉回平面。这部分形变耗费的能量削弱了过强的 OH* 吸附，同时 OOH* 生成仍接近热中性，使 FeCoMn–NC 位于火山顶附近。结果表明，工作条件下形成的轴向 OH 可以通过 Mn 单原子的几何位置平衡 ORR 中间体的吸附。

## 相对合并稿的 3 处改动及理由
1. **机理句补上"没有 OH 时 Mn 往哪走"**（T042，本人 CSV）：裸 Mn 吸附 OOH*/O*/OH* 时 Mn 被拉到吸附物一侧 −0.31/−0.41/−0.46 Å；带轴向 OH 时 Mn 从 +0.44 Å 只回到 0.00/−0.10/−0.01 Å。读者因此看清"形变代价"的来源：OH 让 Mn 无法向中间体靠拢。这正是 Claude web 读 Zotero 20 篇摘要总结的"结构特征 + 物理原因 → 具体中间体能量"句式。
2. **性能句加回 FeCo–NC、Mn–NC**：是实测数据，正文第 99–101 行已有，不属于机理比较；合并稿留作"待用户定"，我建议加。
3. **末句收窄**："an axial ligand … balances" → "an axial OH … can balance … through the geometry of the Mn single atom"。理由见下"风险 1"。

## 摘要里坚持不写的
- 颗粒推后过氧化 0.48/0.96 V（T039 电子态分支未定）。
- "颗粒决定轴向配体"（同上；T038b 裸 Mn 不受颗粒影响）。
- dz²、自旋、ICOHP。

## 风险（写正文时必须处理，摘要已按此收窄）
1. **轴向 OH 本身不足以给出 0.78 V。** 同一 OH 放在无颗粒 Mn–NC 上（假设构型，T042 表 MnNC_axOH_hypo）U_L 只有 0.57 V；FeCoMn–NC 干净表面 0.80 V、8O* 表面 0.78 V。所以摘要只能说"颗粒旁的 Mn 带 OH → 几何平衡吸附"，不能说"任何 Mn 带 OH 都行"。审稿人若问，正文需一句交代：Mn–OH 的吸附还受周围环境影响，本文只解释 FeCoMn–NC 工作态。
2. **Wan et al., Nat. Commun. 2022（10.1038/s41467-022-30702-z）已报道团簇诱导轴向 OH、对侧吸附优化**（GPT 提示）。本文的新意要落在"工作电位覆盖计算 + 形变代价（几何）而非电子成键"上，前言须引用并区分；摘要末句已突出 geometry。
3. **"carry an axial OH"基于所采用的 Mn=O 电子态**，SI 两分支表（23aa751）交代即可，摘要不加限定词。
4. 标题须与"颗粒决定配体"脱钩；Antigravity 提到的 *Operating-State Axial Hydroxyl Ligation Balances Intermediate Binding at Mn Sites for Oxygen Reduction* 与本摘要一致，可用。
