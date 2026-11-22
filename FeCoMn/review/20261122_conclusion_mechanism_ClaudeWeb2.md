# 结论第二步：S3–S5（Claude web 2，2026-11-22 13:08）
依据：REQUEST_Conclusion_20261122.md 中的"13:01 第一步最终定稿"和"13:02 第二步讨论稿更新"。只讨论第二步，未改 Word，写之前没有读其他方的意见。

## 1. S3–S5 是否合适

**S3：要改，但改法和 13:02 的思路相反，建议把"计算"加回句首。**
13:02 版删掉 Surface-coverage calculations show 的理由是和 S1 重复。可是 S1 写的是 determined the surface coverage，并没有出现"计算"。真正的问题在 S2：它以 Experimentally 开头，S3 却没有交代自己是计算结果，读者会顺着 S2 把 S3 也当成实验结论，以为颗粒推迟 Mn=O 转变是实测出来的。所以 S3 必须标明来源，而且不能重复 S1 的 surface coverage 一词。
另有一处小问题：shift the transition from 0.48 to 0.96 V 的宾语应是转变的电位，不是转变本身。

改为：
Calculations at the working potential and pH show that the O*-covered FeCo alloy particles shift the potential of the Mn–OH to Mn=O transition at the adjacent Mn single atoms from 0.48 to 0.96 V versus RHE, so the Mn single atoms keep an axial OH during the ORR.
直译：在工作电位和 pH 下的计算表明，被 O* 覆盖的 FeCo 合金颗粒把相邻 Mn 单原子上 Mn–OH 向 Mn=O 转变的电位从 0.48 V 推移到 0.96 V（相对 RHE），因此 Mn 单原子在 ORR 过程中保持轴向 OH。

**S4：结构好，有两处要改。**
- **the overly weak binding of Mn=O 字面不通。** 结合中间体的是 Mn，不是 Mn=O 这个键。前半句也有同样问题：than an axial Mn=O does 说的是 Mn=O 在留成键能力，宾语对不上。建议改为 Mn with an axial O，与后面的 ligand-free Mn 对称。
- **几何途径的写法太简。** 见第 3 节。

改为：
The axial OH moderates intermediate binding electronically by leaving Mn more bonding capacity than an axial O does and geometrically by holding Mn out of the N₄ plane, which costs each adsorbing intermediate part of its binding energy, so that Mn binds the intermediates neither as weakly as Mn with an axial O nor as strongly as ligand-free Mn.
直译：轴向 OH 通过两种途径使中间体结合适中。在电子上，它比轴向 O 为 Mn 留下更多成键能力。在几何上，它使 Mn 保持在 N₄ 平面之外，这让每个吸附的中间体都要付出一部分结合能。因此 Mn 对中间体的结合既不像带轴向 O 的 Mn 那样弱，也不像无配体的 Mn 那样强。

这样写还去掉了 avoiding both ...，改成 neither ... nor 的比较句。比较句是肯定的说法，不是否定判断。如果赵月觉得句子太长，可以拆成两句，从 so that 处断开，后半句改为 Mn therefore binds the intermediates ...。

**S5：合适，不用改。** 13:02 删掉"实测最高"是对的，计算不能作为实测的原因，而且那句也和 S2 重复。

## 2. 与 S1、S2 的衔接
- S1 说"揭示了颗粒如何影响中间体结合"，S3 回答颗粒通过轴向 OH 起作用，S4 回答轴向 OH 如何调节结合，S5 给出结果，链条完整。
- 唯一的断点就是第 1 节说的 S2 到 S3：Experimentally 之后需要一个计算标记，否则读者分不清实验和计算的边界。改成 Calculations ... show that 之后，S2 和 S3 一实验、一计算，正好对照。
- 没有其他重复。
  - S1 用 under working conditions，S3 用 at the working potential and pH，说法不同，而且 S3 更具体。
  - S2 写 Pt/C 等对照，S3–S5 都没有再提，不重复。

## 3. 待判断：holding Mn out of the N₄ plane 不讲拉回，读者看不看得懂
**看不懂，而且可能读反。** 只说"Mn 被保持在平面外"，读者容易理解成 Mn 被轴向 OH 拉走，离对侧中间体更远，于是结合变弱。这和正文的机理不同。正文说的是中间体吸附时要把 Mn 拉回平面，拉回这个形变要消耗结合能。

不需要讲拉回的过程，只要补一个原理层面的短语，说明"形变要付出代价"，也就是 which costs each adsorbing intermediate part of its binding energy，大约 8 个词。这句话讲的是"为什么会削弱"，不是"Mn 怎么动"，所以仍然符合赵月 12:42 定下的"只写本质，不写过程"。这个说法与正文图 6 第二段（Drawing Mn back consumes part of the binding energy）和图 S30 一致。

## 4. 第二步建议稿（S3–S5）
Calculations at the working potential and pH show that the O*-covered FeCo alloy particles shift the potential of the Mn–OH to Mn=O transition at the adjacent Mn single atoms from 0.48 to 0.96 V versus RHE, so the Mn single atoms keep an axial OH during the ORR. The axial OH moderates intermediate binding electronically by leaving Mn more bonding capacity than an axial O does and geometrically by holding Mn out of the N₄ plane, which costs each adsorbing intermediate part of its binding energy, so that Mn binds the intermediates neither as weakly as Mn with an axial O nor as strongly as ligand-free Mn. FeCoMn–NC therefore lies near the apex of the activity volcano.

直译：在工作电位和 pH 下的计算表明，被 O* 覆盖的 FeCo 合金颗粒把相邻 Mn 单原子上 Mn–OH 向 Mn=O 转变的电位从 0.48 V 推移到 0.96 V（相对 RHE），因此 Mn 单原子在 ORR 过程中保持轴向 OH。轴向 OH 通过两种途径使中间体结合适中。在电子上，它比轴向 O 为 Mn 留下更多成键能力。在几何上，它使 Mn 保持在 N₄ 平面之外，这让每个吸附的中间体都要付出一部分结合能。因此 Mn 对中间体的结合既不像带轴向 O 的 Mn 那样弱，也不像无配体的 Mn 那样强。因此，FeCoMn–NC 位于活性火山图顶点附近。

规则自查：英文没有冒号、分号和破折号，没有 should、first，没有否定判断句。计算数字只有 0.48 和 0.96 V。每句主语明确。内容与正文一致，对应关系如下：
- 0.48→0.96 V 对应表 S7。
- 成键能力对应图 6 第二段。
- 结合能代价对应图 6 第二段和图 S30。
- 无配体 Mn 结合过强对应表 S11。
- 火山图对应图 6h。
