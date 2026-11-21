# 摘要草稿（Claude web 2，22:15）

按当前主线改写：颗粒阻止相邻 Mn 单原子被过度氧化，使 Mn 停在 Mn–OH，轴向 OH 通过离面形变把过强的吸附调到适中。前五句（背景、样品、活性、原位红外、覆盖度计算）保持原文不变，从第六句起改写。改动处用「」标出。

## 不变的前五句

Metal particles are very common in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet the catalytic activity is usually attributed to the metal single atoms alone. How the particles affect the catalytic activity therefore remains unclear. Here, we prepare a new FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. FeCoMn–NC reaches an oxygen reduction reaction (ORR) half-wave potential of 0.885 V versus RHE. Operando infrared spectroscopy shows that the species at the catalyst surface change with potential, so we calculated the surface coverage before the ORR takes place.

## 原文（第六句起）

The calculations show that, on the surfaces formed under working conditions at 0.78 V, the FeCo particles are covered by O* and the Mn single atoms next to them are coordinated by an axial OH. On these covered surfaces, the axial Mn–OH bond allows the Mn single atoms in FeCoMn–NC to bind OOH* strongly enough to facilitate OOH* formation, whereas the much stronger axial Mn=O bond in particle-free Mn–NC leaves the Mn single atoms binding OOH* too weakly, which hinders OOH* formation. In FeCo–NC, which contains only the particles, the particles bind O* too strongly, which hinders the conversion of O* to OH*. FeCoMn–NC therefore binds the ORR intermediates moderately and lies near the apex of the activity volcano, which explains its highest measured activity. FeCo particles thus determine the axial ligand of the adjacent Mn single atoms under working conditions and thereby their binding of the ORR intermediates.

直译：计算表明，在 0.78 V 工作条件下形成的表面上，FeCo 颗粒被 O* 覆盖，与其相邻的 Mn 单原子由一个轴向 OH 配位。在这些覆盖表面上，轴向 Mn–OH 键使 FeCoMn–NC 中的 Mn 单原子对 OOH* 的结合足够强，从而促进 OOH* 生成，而在不含颗粒的 Mn–NC 中，强得多的轴向 Mn=O 键使 Mn 单原子对 OOH* 结合太弱，阻碍 OOH* 生成。在只含颗粒的 FeCo–NC 中，颗粒对 O* 结合太强，阻碍 O* 转化为 OH*。因此 FeCoMn–NC 对 ORR 中间体结合适中，位于活性火山图顶点附近，这解释了它最高的实测活性。由此，FeCo 颗粒在工作条件下决定了相邻 Mn 单原子的轴向配体，进而决定了它们对 ORR 中间体的结合。

## 修改稿（第六句起）

The calculations show that, 「as the potential rises, the Mn single atoms are coordinated first by an axial OH and then by an axial O. The FeCo particles shift this Mn–OH to Mn=O transition from 0.49 to 0.96 V versus RHE. At 0.78 V, the Mn single atoms next to the particles therefore remain in the Mn–OH state, whereas those in particle-free Mn–NC are oxidized to Mn=O. Without the axial OH, the Mn single atoms bind the ORR intermediates too strongly. The axial OH pulls the Mn single atom out of the N4 plane, and an adsorbing intermediate must pull it back into the plane. This deformation weakens the binding of the intermediates, so that OOH* formation becomes nearly thermoneutral at 0.78 V and FeCoMn–NC lies near the apex of the activity volcano. The Mn=O sites in Mn–NC instead bind OOH* too weakly. FeCo particles thus protect the adjacent Mn single atoms from over-oxidation under working conditions, and the resulting axial OH tunes their binding of the ORR intermediates to the optimum.」

直译：计算表明，「随着电位升高，Mn 单原子先由一个轴向 OH 配位，再由一个轴向 O 配位。FeCo 颗粒把这一 Mn–OH 到 Mn=O 的转变电位从 0.49 V 推后到 0.96 V（相对 RHE）。因此在 0.78 V 下，与颗粒相邻的 Mn 单原子保持在 Mn–OH 状态，而不含颗粒的 Mn–NC 中的 Mn 单原子被氧化为 Mn=O。没有轴向 OH 时，Mn 单原子对 ORR 中间体结合太强。轴向 OH 把 Mn 单原子拉出 N4 平面，吸附的中间体必须把它拉回平面。这一形变削弱了中间体的结合，使 OOH* 生成在 0.78 V 下接近热中性，FeCoMn–NC 位于活性火山图顶点附近。Mn–NC 中的 Mn=O 位点则对 OOH* 结合太弱。由此，FeCo 颗粒在工作条件下保护相邻 Mn 单原子不被过度氧化，由此保留的轴向 OH 把它们对 ORR 中间体的结合调到最佳。」

## 每句依据
- 先 OH 后 O：图 5 覆盖度序列 8O* → 8O* + Mn–OH* → 8O* + Mn–O*。
- 0.49 与 0.96 V：T039（去颗粒，载体几何冻结）与 FeCoMn–NC。0.96 V 需按 T039 同一算式从 FCM 能量直接重算确认，T039 待 Antigravity 复算。
- 0.78 V 下两种状态：图 5、表 S10。
- 无轴向 OH 吸附太强：T032，同一 8O* FeCoMn–NC，U_L 0.52 V。
- 离面与拉回：T042（Mn 被拉出 0.44 Å，吸附后回到平面）。
- 形变削弱结合：T041（OH* 0.236/0.336 eV，OOH* 形变 0.432 eV 超过总减弱 0.267 eV）。
- OOH* 生成近热中性、火山顶：图 5h、图 6h。
- Mn=O 结合太弱：Mn–NC U_L 0.26 V。

## 取舍说明
- 删去了 FeCo–NC 一句，把篇幅留给主线。若需保留对照，可在 “The Mn=O sites in Mn–NC instead bind OOH* too weakly.” 后加 “and the particles in FeCo–NC bind O* too strongly.”
- 没有写颗粒“为什么”能推后转变，也没有写自旋，按清单不进摘要。
- 原文最后一句 “which explains its highest measured activity” 去掉了，因为实测与计算的差距需要在正文中说明背景位点，摘要不宜把计算火山图直接等同于实测最高。
- 全文共约 210 词，比原文少约 10 词。
