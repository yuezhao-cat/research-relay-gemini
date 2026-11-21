# 摘要综合版 v2（Claude Code 云端，2026-11-21）

在 v1（6efcf94）之后，又读了各方的第二轮综合：Claude web b017666、Claude web 2 0b6cc1a、Antigravity d7a83ac、Claude Code 本地 3b3cd91，以及几何可及性讨论（CW2-19，赵月已定：多孔碳两面可接液，沿用现模型）。各方已基本收敛，本版按多数意见定稿，只在仍有分歧处给出理由。

## English Abstract（约 205 词）

Metal particles commonly coexist with single-atom sites in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet catalytic models often rely on bare single-atom surfaces. How the surface state formed under working conditions governs the binding of oxygen reduction reaction (ORR) intermediates remains unclear. Here, we prepare an FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches a half-wave potential of 0.885 V versus the reversible hydrogen electrode (RHE), higher than those of commercial Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h. Operando infrared spectroscopy shows that the interfacial species change with potential, so the ORR takes place on a covered surface. Surface-coverage calculations show that at 0.78 V versus RHE, the FeCo particles are covered by O*, and the adjacent Mn single atoms carry an axial OH. Without this axial OH, Mn binds the ORR intermediates too strongly, and OH* removal is uphill. The axial OH pulls Mn out of the N4 plane, and an intermediate binding on the opposite side pulls Mn back to the plane. Pulling Mn back consumes part of the binding energy and moderates the overly strong binding. As a result, OH* removal becomes downhill at 0.78 V while OOH* formation remains nearly thermoneutral, placing FeCoMn–NC near the apex of the calculated activity volcano, consistent with its highest measured activity.

## 中文直译

热解金属–氮–碳（M–N–C）催化剂中金属颗粒常与单原子位点共存，但催化模型往往仍以裸露的单原子表面为基础。工作条件下形成的表面状态如何控制氧还原反应（ORR）中间体的吸附，目前仍不清楚。本文制备了 FeCo 合金颗粒与 Mn 单原子共存的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的半波电位达到 0.885 V（相对可逆氢电极 RHE），高于商业 Pt/C、FeCo–NC 和 Mn–NC，运行 238 h 后仍保持初始电流的 96.5%。原位红外光谱表明界面物种随电位变化，因此 ORR 发生在被覆盖的表面上。表面覆盖计算表明，在 0.78 V（相对 RHE）下，FeCo 颗粒被 O* 覆盖，相邻 Mn 单原子带轴向 OH。没有这个轴向 OH 时，Mn 对 ORR 中间体吸附过强，OH* 脱除为上坡。轴向 OH 把 Mn 拉出 N4 平面，而从对侧吸附的中间体又把 Mn 拉回平面。拉回 Mn 消耗了部分结合能，缓和了过强的吸附。因此，在 0.78 V 下 OH* 脱除转为下坡，而 OOH* 生成仍接近热中性，使 FeCoMn–NC 位于计算火山图顶点附近，与其最高的实测活性一致。

## 收敛情况与本版取舍

| 问题 | 第二轮各方 | 本版 |
|---|---|---|
| 开头 | 五方都用方案二开头（Claude web 2 收回方案一） | 方案二开头 |
| 红外 | 五方都不写 OOH*/缔合路径 | "interfacial species change with potential, so the ORR takes place on a covered surface"（赵月原句的意思 + 各方措辞） |
| 覆盖态主语 | Antigravity：须写明是计算结果 | "Surface-coverage calculations show that…" |
| 无 OH 一句 | 四方保留，Claude web 删 | 保留。同一 8O* 模型有无 OH（T032），是"适中"的起点，不是催化剂间比较。末尾用"OH* removal is uphill"（T032：0.78 V 下 +0.27 eV），与后句"becomes downhill"呼应 |
| 拉回 | into / toward / to 三种 | back to the plane（Claude web、Claude web 2）：OOH* 0.00、OH* −0.01、O* −0.10 Å，to 对三者都成立 |
| 性能对比 | 第二轮四方保留三者；Claude web 2 也改为保留 | 保留三者。它是实测数据，且结尾"highest measured activity"需要参照。赵月若只留 Pt/C：删"FeCo–NC, and Mn–NC"，并把"highest"改为"high" |
| 结尾 | 四方收敛到"calculated activity volcano, consistent with its highest measured activity" | 采用。不用 explains（计算与实测之间有背景位点等因素） |
| 我 v1 的末句归纳 | 他方均未采用 | 撤回，篇幅留给机理 |
| Claude Code 本地版 | 把"explains the highest activity"放在 Consequently 之前，且用"favor" | 不采用：顺序颠倒、favor 含糊 |
| 用词 | an FeCoMn–NC；RHE 首次写全称；删 bcc；Mn single atoms；不用 must/operating | 全部采用 |
| 两面可及 | 赵月已定：多孔碳两面接液，沿用模型 | 摘要"opposite side"不改 |

## 依据
T032（8O* 背景：无 OH U_L 0.52 V，0.78 V 下 OH* 脱除 +0.27 eV；有 OH U_L 0.78 V，OOH* 生成 +0.004 eV、OH* 脱除 −0.07 eV）；T042（Mn +0.44 Å → OOH* 0.00、OH* −0.01、O* −0.10 Å）；T041（OH* 削弱 0.34 eV 中形变 0.24 eV；OOH* 形变 0.43 eV）；图 3/表 S3（实测活性），图 4（界面水 3307、1633 cm⁻¹），图 6h（火山图）。

## 标题
Axial OH Formed under Working Conditions Moderates Intermediate Binding on Mn Single Atoms beside FeCo Particles for Oxygen Reduction
（Claude web 2、Antigravity 一致；去掉 Determine，不用 Operating）

## 仍待赵月拍板
1. 性能句保留三者还是只留 Pt/C。
2. 标题措辞。
