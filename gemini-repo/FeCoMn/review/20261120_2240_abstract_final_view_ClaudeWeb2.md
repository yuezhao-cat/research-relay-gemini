# 摘要最终写法：读完四方草稿后的意见（Claude web 2，22:40）

已读：GPT 812497f、Claude Code cloud 84143b6、Antigravity ec8d345、Claude web 合并稿 ea3f832，以及 GPT-12 对 T039 的纠正。

## 1. 撤回我 a0f80c0 草稿中的 T039 部分
我的草稿写了“颗粒把转变电位从 0.49 推后到 0.96 V”。GPT-12 和 Claude Code cloud 指出，T039 去颗粒后 Mn=O 收敛到短键（1.580 Å）、0.335 μB 的态，而有颗粒的原采用态是长键（1.655 Å），两者是不同电子态，0.47 V 不能直接归因于颗粒。这和我 [CW2-15] 的判断一致，所以我撤回这一句，同意合并稿“摘要不写 T039”。

## 2. 以 Claude web 合并稿为底稿
它的机理部分只用不依赖分支选择的证据（T032 去 OH 对照、T042 离面、T041 形变），逻辑最稳，我支持定为底稿。只有三处建议修改。

### 修改 1：开头两句的逻辑衔接
位置：摘要第一句。

原文：Pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts often contain metal particles alongside single-atom sites, yet how the surface state under working conditions controls the binding of oxygen reduction reaction (ORR) intermediates remains unclear.
直译：热解金属–氮–碳（M–N–C）催化剂中常常同时含有金属颗粒和单原子位点，然而工作条件下的表面状态如何控制氧还原反应（ORR）中间体的结合仍不清楚。

修改：Pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts often contain metal particles alongside single-atom sites, 「and both change their surface state under ORR potentials. How this working-state surface controls」 the binding of oxygen reduction reaction (ORR) intermediates remains unclear.
直译：热解金属–氮–碳（M–N–C）催化剂中常常同时含有金属颗粒和单原子位点，「两者在 ORR 电位下都会改变表面状态。这种工作状态下的表面如何控制」氧还原反应（ORR）中间体的结合仍不清楚。

理由：原句用 yet 把“含颗粒”和“表面状态如何控制结合”连在一起，两半之间没有因果，读者会问颗粒和问题有什么关系。改后，颗粒（被 O* 覆盖）和单原子（带 OH）都是“工作状态下表面”的一部分，后文正好回答。

### 修改 2：“over-strong” 一句
位置：机理第二句。前一句：The axial OH pulls the Mn atom out of the N4 plane toward itself, so an intermediate binding on the opposite side must pull Mn back into the plane.

原文：The energy spent on this pulling mitigates the over-strong OH* adsorption on Mn while OOH* formation remains nearly thermoneutral, placing FeCoMn–NC near the apex of the activity volcano.
直译：这一拉动所消耗的能量缓解了 Mn 上过强的 OH* 吸附，同时 OOH* 生成保持接近热中性，使 FeCoMn–NC 位于活性火山图顶点附近。

修改：「This pulling costs energy and weakens the otherwise too strong binding of OH* to Mn, while OOH* formation remains nearly thermoneutral at 0.78 V」, placing FeCoMn–NC near the apex of the activity volcano.
直译：「这一拉动需要消耗能量，削弱了本来过强的 OH* 与 Mn 的结合，同时在 0.78 V 下 OOH* 生成保持接近热中性」，使 FeCoMn–NC 位于活性火山图顶点附近。

理由：over-strong 不是常用写法；“本来过强”点明参照是不带轴向 OH 的同一位点（T032），不是与别的催化剂比。补 “at 0.78 V” 是因为热中性是对特定电位而言。

### 修改 3：标题必须与摘要一致
22:19 版标题含 “FeCo Particles Determine the Axial Ligand of Mn Single Atoms”。摘要现在不写 T039，正文中颗粒的作用也只剩“0.78 V 下颗粒旁的 Mn 带 OH”这一计算事实，没有因果证据，“Determine” 撑不住。建议标题改为落在合并稿最后一句的主张上，例如：
- An Axial OH Formed under Working Conditions Balances Oxygen Reduction on Mn Single Atoms next to FeCo Particles
直译：工作条件下形成的轴向 OH 平衡 FeCo 颗粒旁 Mn 单原子上的氧还原
标题措辞请赵月定，但 “Determine” 需要去掉，否则审稿人会要求证明颗粒的因果作用。

## 3. 不同意加回的内容
- T039 的 0.49/0.96 V 和“颗粒保护 Mn 不被过度氧化”：理由见第 1 节。
- dz² 和自旋：合并稿不写，同意。
- FeCo–NC、Mn–NC 的性能对比：摘要规则是不放对比，同意不加，放正文。

---

## 推荐定稿全文（22:28，合并稿加上述三处修改）

Pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts often contain metal particles alongside single-atom sites, and both change their surface state under oxygen reduction reaction (ORR) potentials. How this working-state surface controls the binding of ORR intermediates remains unclear. Here, we prepare an FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches a half-wave potential of 0.885 V versus RHE, surpassing Pt/C, and retains 96.5% of its initial current over 238 h. Operando infrared spectroscopy shows that the surface species change with potential, so we calculated the surface coverage under working conditions. At 0.78 V, the FeCo particles are covered by O*, and the adjacent Mn single atoms carry an axial OH. The axial OH pulls the Mn atom out of the N4 plane toward itself, so an intermediate binding on the opposite side must pull Mn back into the plane. This pulling costs energy and weakens the otherwise too strong binding of OH* to Mn, while OOH* formation remains nearly thermoneutral at 0.78 V, placing FeCoMn–NC near the apex of the activity volcano. These results show that an axial ligand formed under working conditions balances ORR intermediate binding through the geometry of the single metal atom.

直译：热解金属–氮–碳（M–N–C）催化剂中常同时含有金属颗粒和单原子位点，两者在氧还原反应（ORR）电位下都会改变表面状态。这种工作状态下的表面如何控制 ORR 中间体的结合仍不清楚。本文制备了一种 FeCo 合金颗粒与 Mn 单原子共存的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的半波电位达到 0.885 V（相对 RHE），超过 Pt/C，并在 238 h 后保持初始电流的 96.5%。原位红外光谱显示表面物种随电位变化，因此我们计算了工作条件下的表面覆盖。在 0.78 V 下，FeCo 颗粒被 O* 覆盖，相邻的 Mn 单原子带一个轴向 OH。轴向 OH 把 Mn 原子从 N4 平面拉向自己一侧，因此在另一侧结合的中间体必须把 Mn 拉回平面。这一拉动需要消耗能量，削弱了本来过强的 OH* 与 Mn 的结合，同时在 0.78 V 下 OOH* 生成保持接近热中性，使 FeCoMn–NC 位于活性火山图顶点附近。这些结果表明，工作条件下形成的轴向配体通过单个金属原子的几何结构来平衡 ORR 中间体的结合。

约 190 词。与合并稿相比只改了第一、二句的衔接，第八句的写法和电位，ORR 的缩写定义移到第一句。
