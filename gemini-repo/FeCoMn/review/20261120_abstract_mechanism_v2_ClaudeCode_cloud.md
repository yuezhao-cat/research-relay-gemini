# 摘要机理句修改（Claude Code 云端，2026-11-20）

对象：赵月当前最满意版（机理句 = 弱 Mn–OH → dz² 靠近费米能级 → OOH* 能生成 → 后续下坡）。

## 为什么"dz²"机理句不行
1. 与我们自己的数据矛盾：T041 拆分显示，加上轴向 OH 后，冻结几何下 Mn 与中间体的电子相互作用几乎不变（OH* +0.10 eV，OOH* −0.10 eV）；吸附被削弱主要来自形变（OH* +0.24 eV，OOH* +0.43 eV）。用电子结构（dz²）解释，等于说主因是我们数据里最小的那一项。
2. dz² 中心 −3.17 eV，不能叫"靠近费米能级"（Claude web 22:30 已指出）。
3. dz² 上移会同时加强 OOH* 和 OH* 的吸附，推不出"OH* 脱除下坡"，这一半只能靠自由能结果。
4. "weak Mn–OH bond"没有参照，读者会问"比什么弱"。
5. "strongly enough for OOH* to form"只解释第一步；FeCoMn–NC 适中的关键其实是 OH* 不再吸得过牢，这一点没说。

## 建议机理句（不比较其他催化剂，只回答 FeCoMn–NC 自己为什么适中）
The axial OH pulls the Mn atom out of the N4 plane on its own side, and an ORR intermediate binding on the opposite side must pull Mn back into the plane. The energy spent on this deformation offsets part of the Mn–intermediate bonding, so Mn binds OOH* strongly enough for it to form but no longer holds OH* so tightly that it cannot be removed; at 0.78 V, OOH* formation is nearly thermoneutral and all subsequent steps are downhill.

直译：轴向 OH 把 Mn 原子拉到 N4 平面自己这一侧，中间体从另一侧吸附时必须把 Mn 拉回平面。这部分形变消耗的能量抵消了一部分 Mn 与中间体的成键，因此 Mn 对 OOH* 的吸附仍足以让它生成，但对 OH* 不再抓得过牢而无法脱除；在 0.78 V 下，OOH* 生成接近热中性，之后各步都是下坡。

依据：T042（Mn 离面 +0.44 Å，吸附后回到 0.00/−0.10/−0.01 Å）；T041（形变 vs 相互作用拆分）；表 S7 / T032（0.78 V 各步 ΔG，U_L 0.776 V）。

## 末句（去重，不等 T039）
T039 已查明受 Mn=O 电子态分支影响，四方已定不进正文；末句不必等它。建议：
These results show that the ligand formed on single atoms under working conditions, rather than the bare single atom, must be considered to explain the ORR activity of particle-containing M–N–C catalysts.
直译：这些结果表明，要解释含颗粒 M–N–C 催化剂的 ORR 活性，必须考虑工作条件下单原子上形成的配体，而不是裸单原子。
