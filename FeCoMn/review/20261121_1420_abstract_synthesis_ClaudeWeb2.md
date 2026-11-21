# 摘要综合版（Claude web 2，2026-11-21 14:20）

综合：Claude web 1405 版、Claude Code 云端审阅（230491a/d516fce）、GPT 1636324、Antigravity 99b6c33，以及我 42272b6 的意见。

## 逐项取舍
| 问题 | 各方意见 | 采用 | 理由 |
|---|---|---|---|
| 开头 | Claude Code、Antigravity、GPT 选方案二开头（颗粒与单原子共存，模型却用裸表面）；我选方案一；Claude web 用方案三 | 方案二开头 | 三方一致。它交代了颗粒，后文“颗粒被 O* 覆盖”正是工作态表面的一部分，问题与回答对得上。我收回方案一的主张 |
| 红外 | Claude web 指出 1215 cm⁻¹ 与 Nafion C–F 重叠、两片电极趋势相反，不写 OOH* 和缔合路径；Claude Code 认为 “accumulation” 过强；GPT 只写界面物种变化 | 只写界面水随电位变化 | 界面水 3307、1633 cm⁻¹ 有正文依据，OOH* 归属有争议，摘要不写有争议的指认 |
| 无轴向 OH 一句 | Claude Code、Antigravity、GPT 保留为两短句；Claude web 删去 | 保留 | 这是同一位点有无 OH 的对照（T032），回答“为什么适中”的起点，不是与其他催化剂比较 |
| 拉回平面 | 我主张 into，Antigravity 指出 O* 略越过平面（−0.10 Å），主张 toward | back to the plane | OOH* 0.00、OH* −0.01、O* −0.10 Å，回到平面附近，to 覆盖三者 |
| Mn–N₄ sites 还是 Mn single atoms | Claude Code、Claude web 主张 Mn single atoms | Mn single atoms | 与正文、关键词一致 |
| 冠词 | Claude Code、Antigravity | an FeCoMn–NC | 读作 eff |
| RHE | Antigravity 补全称 | 首次写全称 | 规范 |
| bcc | Antigravity 删，Claude web 保留 | 删 | 摘要不展开晶体结构，正文图 1 交代 |
| 性能对比 | 四方草稿都列 FeCo–NC、Mn–NC；我曾建议只留 Pt/C | 保留三者 | 多数意见，且是实测性能而非机理对比。若赵月仍要只留 Pt/C，删去 “FeCo–NC, and Mn–NC” 即可 |
| 结尾落点 | Claude Code 要加回“解释最高实测活性” | consistent with its highest measured activity | 计算与实测量级不同（正文用背景位点解释），用 consistent 表示排序一致，不写成 explains |
| GPT 的 “favor”“without necessarily” | 含糊词 | 不采用 | 违反不写含糊措辞的规则 |
| 标题 | 均去掉 Determine；GPT 用 Operating-State（列为禁用词） | 见文末 | |

## 综合版全文
Metal particles commonly coexist with single-atom sites in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet catalytic models often rely on bare single-atom surfaces. How the surface state formed under working conditions governs the binding of oxygen reduction reaction (ORR) intermediates remains unclear. Here, we prepare an FeCoMn–NC catalyst combining FeCo alloy particles with Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches a half-wave potential of 0.885 V versus the reversible hydrogen electrode (RHE), surpassing commercial Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current over 238 h. Operando infrared spectroscopy shows that the interfacial water changes with potential, so we calculated the surface coverage under working conditions. At 0.78 V versus RHE, the FeCo particles are covered by O*, and the adjacent Mn single atoms carry an axial OH. Without this axial OH, Mn binds the ORR intermediates too strongly and impedes OH* removal. The axial OH pulls Mn out of the N₄ plane, and an intermediate adsorbing on the opposite side pulls Mn back to the plane. Pulling Mn back consumes part of the binding energy and moderates the overly strong binding. As a result, OH* removal becomes downhill at 0.78 V while OOH* formation remains nearly thermoneutral, placing FeCoMn–NC near the apex of the activity volcano, consistent with its highest measured activity.

直译：金属颗粒通常与单原子位点共存于热解金属–氮–碳（M–N–C）催化剂中，但催化模型往往仍以裸露的单原子表面为基础。工作条件下形成的表面状态如何支配氧还原反应（ORR）中间体的结合仍不清楚。本文制备了一种 FeCo 合金颗粒与 Mn 单原子结合的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的半波电位达到 0.885 V（相对于可逆氢电极 RHE），超过商业 Pt/C、FeCo–NC 和 Mn–NC，并在 238 h 后保持初始电流的 96.5%。原位红外光谱显示界面水随电位变化，因此我们计算了工作条件下的表面覆盖。在 0.78 V（相对于 RHE）下，FeCo 颗粒被 O* 覆盖，相邻的 Mn 单原子带一个轴向 OH。没有这个轴向 OH 时，Mn 对 ORR 中间体结合过强，阻碍 OH* 脱附。轴向 OH 把 Mn 拉出 N₄ 平面，在对侧吸附的中间体又把 Mn 拉回平面。拉回 Mn 消耗了部分结合能，缓和了过强的结合。结果是，在 0.78 V 下 OH* 脱附变为下坡，而 OOH* 生成保持接近热中性，使 FeCoMn–NC 位于活性火山图顶点附近，与其最高的实测活性一致。

约 205 词，无冒号和分号，无含糊词。

## 每句依据
- 界面水随电位变化：正文图 4，3307、1633 cm⁻¹。
- 0.78 V 覆盖：图 5、表 S10。
- 无 OH 过强：T032，U_L 0.52 V，0.78 V 下 OH* 脱附 +0.27 eV。
- 拉出与拉回：T042，+0.44 Å 到 0.00、−0.01、−0.10 Å。
- 消耗结合能：T041，OH* 0.236/0.336 eV，OOH* 形变 0.432 eV 大于总减弱 0.267 eV。
- 下坡与近热中性：T032 带 OH，OH* 脱附 −0.07 eV，OOH* 生成 +0.004 eV。
- 最高实测活性：图 3、表 S3。

## 标题建议（去掉 Determine，不用 Operating）
Axial OH Formed under Working Conditions Moderates Intermediate Binding on Mn Single Atoms beside FeCo Particles for Oxygen Reduction
直译：工作条件下形成的轴向 OH 缓和 FeCo 颗粒旁 Mn 单原子对中间体的结合，用于氧还原
