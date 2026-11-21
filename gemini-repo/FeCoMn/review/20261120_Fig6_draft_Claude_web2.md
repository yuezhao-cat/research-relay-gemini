# 图 6 段草稿与主线审阅（Claude web 2，2026-11-20 16:10）

审阅对象：discussion/20261120_1550_mechanism_mainline_current.md（3ed8338）。全部数据为原采用分支，来自 T032 `selected_descriptors.csv`（Mn_height_signed_A，按各组自身轴向取符号，下面只看大小和方向）以及 Antigravity 和 Claude Code 复核过的 OH* 拆分（T041_ClaudeCode.md）。

## 一、第 4 环：可以用“拔河”一条线讲清楚，并且能贯通到第 6 环

Mn 位于 N4 平面中央。哪一侧的配体与它结合，就会把 Mn 往哪一侧拉出平面。中间体结合得好，需要 Mn 能够朝它移过来。

| Mn 背面的轴向配体 | 吸附前 Mn 离面（朝轴向配体一侧） | 中间体吸附后 Mn 的位置 | 中间体结合 | U_L |
|---|---|---|---|---|
| 无（FeCoMn–NC，8O*） | 0.01 Å，在平面内 | 朝中间体一侧拉出 0.31（OOH*）、0.41（O*）、0.46 Å（OH*） | 太强 | 0.52 V |
| OH（FeCoMn–NC，8O*） | 0.44 Å | 回到平面，0.00（OOH*）、0.10（O*）、0.01 Å（OH*），不再越过平面 | 适中 | 0.78 V |
| O（Mn–NC） | 0.51 Å | OOH* 吸附后仍留在 O 一侧 0.17 Å | 太弱 | 0.26 V |

一句话：轴向配体把 Mn 拉向自己，中间体在另一侧就拉不动 Mn。没有轴向配体时，Mn 可以向中间体靠过去，所以结合太强。轴向 OH 把 Mn 拉住，中间体只能把它拉回平面，结合减弱，落到适中。轴向 O 是双键，拉得更紧，中间体连平面都拉不回来，所以结合太弱。

**能量上的证据（已由两方复核）。**OH* 结合减弱 0.336 eV，其中 0.236 eV（70%）来自形变代价的增加。无 OH 时，形变代价是 0.435 eV（Mn 向 OH* 移动 0.46 Å）。有 OH 时，形变代价是 0.671 eV（Mn 从 OH 一侧被拉回平面，移动 0.44 Å）。Mn 移动的距离差不多，但有 OH 时代价多出 0.24 eV，多出来的就是和轴向 OH“拔河”的代价。剩下的 0.10 eV 是成键本身的变化，用 dz² 单占态配对来描述就可以。

**这也解释了 −ICOHP 的反例。**OH* 与 Mn 的键本身并没有变弱（−ICOHP 2.70 → 3.06 eV），变的是“把 Mn 拉过来”的代价。

**它和第 6 环是同一条线，不是另一个故事。**Mn–NC 的 Mn=O 拉得更紧，这条线自然地推出“太弱”。所以第 6 环可以从“验证”升级为同一原理的第三个点。注意这一行用的是 Mn–NC 实际的工作态（Mn=O），不是被撤回的 Mn–NC+OH 假设态。

**待补的一项（不跑新 DFT）。**OOH* 的形变与电子拆分，T041 正在算。如果 OOH* 也主要来自形变，第 4 环就完整了。

## 二、第 2 环：颗粒让 OH 更稳定，现有数据已经能把范围缩小一半

Antigravity 的 `FCMnew_base_support`（几何冻结、去掉颗粒、保留轴向 OH）显示，去掉颗粒后 Mn–OH 态几乎不变：Mn Bader −0.0007 e，Mn 磁矩 −0.022 μB，轴向 OH −0.0043 e。

所以，如果 T039 显示去掉颗粒后偏好翻成 O，颗粒的作用就不在 Mn–OH 一侧，而在 Mn=O 一侧。也就是说，颗粒不是稳住了 OH，而是让 Mn=O 变得不稳定。这样第 2 环的问题就缩小成：颗粒为什么让 Mn=O 不稳定？

**只需后处理的下一步（T039 交付后）。**比较 T039 的 S-O（去颗粒，Mn=O）和原采用的 FeCoMn–NC 8O* + Mn=O 两个态，看四个量：Mn 离面高度、Mn–O 键长、Mn 磁矩、Bader（Mn、轴向 O、颗粒 ΣFe+Co）。哪个量变化最大，颗粒就是通过它起作用。例如，如果 Mn=O 有颗粒时 Mn 拉出得更少或键更长，就和第一节的拔河图像接上了，即颗粒让 O 这根绳拉不紧，从而偏向 OH。所有比较都在原采用分支内进行。

## 三、对图 6 段草稿的修改建议

### 修改 1
位置：草稿第 3 句。前一句：To understand why the Mn single atoms in FeCoMn–NC bind the ORR intermediates moderately, we compared the same 8O*-covered FeCoMn–NC model with and without the axial OH.

原文：Without the axial OH, the Mn single atom binds the intermediates too strongly. OH* removal is the limiting step, and the limiting potential is only 0.52 V [Table SX].
直译：没有轴向 OH 时，Mn 单原子对中间体吸附太强。OH* 脱附是限制步，极限电位只有 0.52 V。

修改：Without the axial OH, the Mn single atom binds the intermediates too strongly. OH* removal is the limiting step, and the limiting potential is 0.52 V [Table SX].
直译：没有轴向 OH 时，Mn 单原子对中间体吸附太强。OH* 脱附是限制步，极限电位为 0.52 V。

理由：讨论中已定不用 only。

### 修改 2
位置：几何两句。前一句：With the axial OH, OH* and OOH* bind more weakly by 0.33 and 0.21 eV, respectively, and the limiting potential rises to 0.78 V.

原文：The axial OH pulls the Mn single atom 0.44 Å out of the N4 plane [Figure 6a]. When an intermediate adsorbs on the opposite side, the Mn single atom returns to the N4 plane, and this deformation costs energy. For OH*, the deformation accounts for 0.24 eV of the 0.34 eV weakening, and the change in electronic binding accounts for the remaining 0.10 eV [Figure 6b, Table SX].
直译：轴向 OH 把 Mn 单原子从 N4 平面拉出 0.44 Å。中间体在另一侧吸附时，Mn 单原子回到 N4 平面，这一形变需要付出能量。对 OH* 而言，0.34 eV 的减弱中，0.24 eV 来自形变，其余 0.10 eV 来自电子结合的变化。

修改：The axial OH pulls the Mn single atom 0.44 Å out of the N4 plane 「toward itself」 [Figure 6a]. 「Without the axial OH, an adsorbing intermediate pulls the Mn single atom 0.31–0.46 Å out of the plane toward the intermediate. With the axial OH, the intermediate brings the Mn single atom back to the N4 plane and no further, and dragging the Mn single atom away from the axial OH costs energy. For OH*, this deformation accounts for 0.24 eV of the weakening, and the change in electronic binding accounts for 0.10 eV」 [Figure 6b, Table SX].
直译：轴向 OH 把 Mn 单原子从 N4 平面「朝它自己一侧」拉出 0.44 Å。「没有轴向 OH 时，吸附的中间体把 Mn 单原子朝中间体一侧拉出平面 0.31–0.46 Å。有轴向 OH 时，中间体只能把 Mn 单原子拉回 N4 平面，不能再越过平面，而把 Mn 单原子从轴向 OH 一侧拉开需要付出能量。对 OH* 而言，这一形变贡献了 0.24 eV 的减弱，电子结合的变化贡献了 0.10 eV」。

理由：补上“无 OH 时 Mn 朝中间体移动”这一半，读者才看得出为什么拉回平面就意味着变弱。去掉 “of the 0.34 eV”，避免与前一句自由能的 0.33 eV 并列造成数值不一致（0.336 是 ΔE，0.33 是 ΔG）。

### 修改 3
位置：最后一句。前一句：In Mn–NC, by contrast, the Mn single atoms carry an axial O.

原文：The Mn=O double bond quenches the Mn spin and lowers the dz² states to −5.12 eV, so OOH* binds too weakly and the limiting potential is only 0.26 V [Figure 6g].
直译：Mn=O 双键使 Mn 的自旋猝灭，并把 dz² 态压低到 −5.12 eV，因此 OOH* 吸附太弱，极限电位只有 0.26 V。

修改：The Mn=O double bond quenches the Mn spin and lowers the dz² states to −5.12 eV. 「It also pulls the Mn single atom 0.51 Å out of the N4 plane, and after OOH* adsorption the Mn single atom stays 0.17 Å on the side of the axial O. OOH* therefore binds too weakly, and the limiting potential is 0.26 V」 [Figure 6g].
直译：Mn=O 双键使 Mn 的自旋猝灭，并把 dz² 态压低到 −5.12 eV。「它还把 Mn 单原子从 N4 平面拉出 0.51 Å，OOH* 吸附后 Mn 单原子仍留在轴向 O 一侧 0.17 Å。因此 OOH* 吸附太弱，极限电位为 0.26 V」。

理由：让 Mn–NC 与前文使用同一个几何原理，并去掉 only。

## 四、图 6 面板建议

图 6a 建议画成三栏示意加数值：无配体、轴向 OH、轴向 O，每栏画出吸附前和 OOH* 吸附后 Mn 相对 N4 平面的位置，箭头标出轴向配体和中间体各自的拉力方向。这一张图就能让读者一眼看懂“太强、适中、太弱”。图 6b 放能量拆分（形变 0.24、电子 0.10 eV）。

## 五、需要复核的数据

- Mn 离面高度来自 T032 `selected_descriptors.csv`，各组的符号约定不同（按各自轴向）。建议 Claude Code 用 CONTCAR 统一以 N4 平面法向、朝轴向配体为正，重新给出上表的 9 个数。
- Mn–NC 的 U_L 0.26 V（正文）和 0.24 V（T032 静态）仍待统一。
