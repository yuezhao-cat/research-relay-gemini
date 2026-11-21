# 摘要综合版（Claude Code 云端，2026-11-21）

综合：Antigravity 99b6c33（方案二融合 199 词）、Claude web 2 42272b6（方案一 + 4 处）、Claude web ba373e9（方案三改）、GPT 1636324、Claude Code 本地 230491a、本人 d516fce；以及赵月定的规则（先解释 FeCoMn–NC 自己为什么适中再下结论；Mn–NC、FeCo–NC 对比不进摘要；不写颗粒推后过氧化/颗粒决定配体/dz²）。

## English Abstract（约 215 词）

Metal particles commonly coexist with single-atom sites in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet the catalytic activity is usually attributed to bare single atoms. How the surface state formed under working conditions controls the binding of oxygen reduction reaction (ORR) intermediates remains unclear. Here, we prepare an FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches a half-wave potential of 0.885 V versus RHE, outperforming commercial Pt/C, and retains 96.5% of its initial current after 238 h. Operando infrared spectroscopy shows that the species adsorbed on the catalyst surface change with potential, so the ORR takes place on a covered surface. We therefore calculated the surface coverage at different potentials. At 0.78 V, the FeCo particles are covered by O*, and the adjacent Mn single atoms carry an axial OH. Without this OH, Mn binds the ORR intermediates too strongly, and OH* removal limits the reaction. The axial OH pulls Mn out of the N4 plane toward itself, and an intermediate binding on the opposite side pulls Mn back into the plane. Pulling Mn back consumes part of the binding energy and weakens the binding. As a result, OH* removal becomes downhill at 0.78 V while OOH* formation remains nearly thermoneutral, placing FeCoMn–NC near the apex of the calculated activity volcano. These results show that an axial OH formed under working conditions can balance ORR intermediate binding through the geometry of the Mn single atom.

## 中文直译

热解金属–氮–碳（M–N–C）催化剂中金属颗粒常与单原子位点共存，但催化活性通常只归因于裸露的单原子。工作条件下形成的表面状态如何控制氧还原反应（ORR）中间体的吸附，目前仍不清楚。本文制备了 FeCo 合金颗粒与 Mn 单原子共存的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的半波电位达到 0.885 V（相对 RHE），优于商业 Pt/C，运行 238 h 后仍保持初始电流的 96.5%。原位红外光谱表明，吸附在催化剂表面的物种随电位变化，因此 ORR 发生在被覆盖的表面上。于是我们计算了不同电位下的表面覆盖。在 0.78 V 下，FeCo 颗粒被 O* 覆盖，相邻的 Mn 单原子带轴向 OH。没有这个 OH 时，Mn 对 ORR 中间体吸附过强，OH* 脱除限速。轴向 OH 把 Mn 拉出 N4 平面、偏向自己一侧，而从对侧吸附的中间体又把 Mn 拉回平面。拉回 Mn 消耗了部分结合能，削弱了吸附。因此，在 0.78 V 下 OH* 脱除转为下坡，而 OOH* 生成仍接近热中性，使 FeCoMn–NC 位于计算火山图顶点附近。这些结果表明，工作条件下形成的轴向 OH 可以通过 Mn 单原子的几何位置平衡 ORR 中间体的吸附。

## 分歧点与取舍

| 分歧 | 各方 | 取舍及理由 |
|---|---|---|
| 开头 | 颗粒共存起句（Antigravity、GPT、CC 本地、本人）vs 表面随电位演变起句（Claude web 2、Claude web） | 颗粒共存起句，但第二句把问题收到"工作态表面状态如何控制吸附"，结尾正好回答。保留赵月最满意版的开头，否则后文 FeCo 颗粒没有来由。Claude web 2 担心"开头提颗粒、后文不答颗粒作用"，所以第一句只陈述共存与"活性只归因于裸单原子"，不问"颗粒如何影响"。 |
| 性能句是否列 FeCo–NC、Mn–NC | 列（Antigravity、GPT、Claude web）vs 只留 Pt/C（Claude web 2） | 只留 Pt/C。符合赵月"对比不进摘要"；摘要不解释两个对照为何差，列出来读者会追问。正文保留对比。 |
| 红外写到哪一步 | 写 OOH*/缔合路径（Antigravity、方案一）vs 只写表面物种随电位变化（Claude web、GPT） | 只写物种随电位变化 + 表面被覆盖。1215 cm⁻¹ 与 Nafion C–F 重叠、双电极趋势相反（Antigravity T043），摘要不承载 OOH* 归属。用赵月版原句。 |
| "没有 OH 时过强"是否保留 | 保留（Antigravity、GPT、Claude web 2）vs 删（Claude web） | 保留。这是同一体系内部的起点，不是与其他催化剂比较；没有它，"削弱"无从说起，"适中"也解释不出来。 |
| 拉回位置 | toward（Antigravity、GPT）vs into（Claude web、Claude web 2） | into。T042：OOH* 0.00、OH* −0.01、O* −0.10 Å，即回到平面内。 |
| GPT"不一定削弱局部成键" | 仅 GPT | 不进摘要，放正文 T041 段。对摘要读者过细。 |
| 火山图 | CC 本地问图 6 是否有火山图 | 图 6h 是火山图；按 GPT 加 "calculated"，避免读者以为是实验火山图。 |
| 末句 | 无末句（多数）vs 赵月版"explains its highest measured activity" | 加一句归纳：轴向 OH 通过 Mn 几何平衡吸附。不写"解释实测最高活性"，因计算与实测之间还有背景位点等因素（Claude web 2 已提）。 |
| 用词 | Mn–N4 sites（方案一/二）vs Mn single atoms | Mn single atoms，与正文、赵月版一致；删 bcc（正文图 1 展开）；an FeCoMn–NC；不用 must、operating。 |

## 依据
T032（8O* 背景：无 OH U_L 0.516 V，OH* 脱除限速；有 OH U_L 0.776 V，OOH* 生成 +0.004 eV，OH* 脱除 −0.07 eV）；T042（Mn +0.44 Å → 吸附后约 0）；T041（OH* 削弱 0.34 eV 中形变 0.24 eV；OOH* 形变 0.43 eV）；正文第 99–101、235–236 行（0.885 V、Pt/C、238 h、96.5%）。

## 标题（配套，去 Determine）
Axial OH Formed under Working Conditions Balances Oxygen Reduction on Mn Single Atoms beside FeCo Particles
直译：工作条件下形成的轴向 OH 平衡 FeCo 颗粒旁 Mn 单原子上的氧还原
