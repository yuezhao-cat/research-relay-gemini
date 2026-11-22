# 意义部分改为两句（Claude web 2，2026-11-22 14:10）
赵月要求：意义部分分成两句，既要呼应摘要开头两句，也要扩大适用的反应，把意义提高一层。S1–S4 不动，只改最后部分。

## 先说一个必须面对的问题：扩大到其他反应，正文里有没有依据
- 正文现在只讨论 ORR。前言里唯一与反应无关的普适前提是"工作条件下颗粒和单原子都被电解液物种覆盖"（文献 14–17）。文献 6 的标题提到 OER，文献 7 是轴向配位在能源电催化中的综述，但正文没有用它们来说其他反应。
- 写作规则第 7 条是"结论不引入正文没有的内容"。所以扩大适用范围要么只靠那个普适前提、不点名具体反应，要么在前言第二段补半句话并引用文献 6、7，结论才能点名其他反应。
- 点名哪种反应要小心，我们自己的数据就会对其中一些不利。
  - OER 的电位高于 1.23 V。按本文结果，即使有颗粒，Mn 在 0.96 V 以上也会变成 Mn=O，所以"保住轴向 OH"在 OER 下并不成立。点名 OER，审稿人可以直接用我们的图 5 反驳。
  - 硝酸根和 CO2 还原在负电位下进行，覆盖物种主要是 H* 等，轴向配体是什么本文没有算过。
  - 与本文最接近的是二电子 ORR（产 H₂O₂）。它的中间体相同（OOH*），电位范围也相近，但本文同样没有算过。
- 我的建议是不点名具体反应，只写"其他电催化反应"，依据就是普适前提：配体来自电解液、随电位变化。这样意义能提高一层，又不会被本文数据反驳。

## 两句（推荐版）
S5（回到摘要第 1、2 句）：Because metal particles commonly coexist with single atoms in pyrolyzed M–N–C catalysts, the ORR activity of such catalysts thus also depends on the particles, whose surface coverage under working conditions determines the axial ligand of the neighboring single atoms.
直译：由于热解 M–N–C 催化剂中金属颗粒普遍与单原子共存，此类催化剂的 ORR 活性因此也取决于颗粒，颗粒在工作条件下的表面覆盖决定了相邻单原子的轴向配体。

S6（扩大到其他反应）：Electrolyte species cover the particles and the single atoms in other electrocatalytic reactions as well, so the surface coverage of coexisting particles under working conditions also sets the axial ligands that tune single atoms in these reactions.
直译：在其他电催化反应中，电解液物种同样覆盖颗粒和单原子，因此共存颗粒在工作条件下的表面覆盖同样决定着调节这些反应中单原子的轴向配体。

**呼应：**
- S5 前半句对应摘要第 1 句"颗粒与单原子常共存"，也对应前言的 commonly coexist。
- S5 后半句对应摘要第 2 句的 surface coverage under working conditions。
- S5 的 also depends on the particles 正面回应前言中"活性常只归给单原子"的说法。

**提高一层：**
- S5 从 FeCoMn–NC 上升到"此类催化剂"。
- S6 从 ORR 上升到"电催化反应"。
- 两步都有明确依据：S5 依据颗粒普遍共存，S6 依据电解液覆盖普遍存在，都是前言已经写过、并有文献支持的前提，不是凭空推广。

**规则自查：**
- 没有数字，没有冒号、分号、破折号。
- 没有 should、can、beyond，也没有否定句。
- 没有 generalizable design principle 一类套话，S6 的推广写了理由。
- whose、these 的指代都紧跟所指对象。
- 如果 REDLINES 禁止 these reactions，可以改成 in such reactions。

## 如果赵月坚持点名具体反应
条件是在前言第二段第一句后补半句话，例如 "Axial ligands on single atoms also tune other electrocatalytic reactions.^(6,7)"。点名的对象只用二电子 ORR，不用 OER：

S6'：Electrolyte species cover the particles and the single atoms in other electrocatalytic reactions as well, such as the two-electron reduction of O₂ to H₂O₂, so the surface coverage of coexisting particles under working conditions also sets the axial ligands that tune single atoms in these reactions.
直译：在其他电催化反应中，例如 O₂ 二电子还原生成 H₂O₂，电解液物种同样覆盖颗粒和单原子，因此共存颗粒在工作条件下的表面覆盖同样决定着调节这些反应中单原子的轴向配体。

## 完整结论（S1–S4 不变，加推荐的 S5、S6）
In summary, we determined the surface coverage of FeCoMn–NC, a catalyst combining FeCo alloy particles and Mn single atoms, under working conditions and thereby revealed how the FeCo alloy particles affect intermediate binding at the adjacent Mn single atoms. Experimentally, FeCoMn–NC reaches an ORR half-wave potential of 0.885 V versus RHE in 0.1 M KOH, outperforming Pt/C, FeCo–NC, and Mn–NC. Calculations show that the O*-covered FeCo alloy particles keep an axial OH on the adjacent Mn single atoms at the working potential. The axial OH moderates the binding of ORR intermediates through electronic and geometric effects, placing FeCoMn–NC near the apex of the activity volcano. Because metal particles commonly coexist with single atoms in pyrolyzed M–N–C catalysts, the ORR activity of such catalysts thus also depends on the particles, whose surface coverage under working conditions determines the axial ligand of the neighboring single atoms. Electrolyte species cover the particles and the single atoms in other electrocatalytic reactions as well, so the surface coverage of coexisting particles under working conditions also sets the axial ligands that tune single atoms in these reactions.

直译：总之，我们确定了兼具 FeCo 合金颗粒与 Mn 单原子的催化剂 FeCoMn–NC 在工作条件下的表面覆盖，并由此揭示了 FeCo 合金颗粒如何影响相邻 Mn 单原子上的中间体结合。实验上，FeCoMn–NC 在 0.1 M KOH 中的 ORR 半波电位达到 0.885 V（相对 RHE），优于 Pt/C、FeCo–NC 和 Mn–NC。计算表明，被 O* 覆盖的 FeCo 合金颗粒在工作电位下使相邻 Mn 单原子保持轴向 OH。轴向 OH 通过电子和几何作用使 ORR 中间体的结合适中，从而使 FeCoMn–NC 位于活性火山图顶点附近。由于热解 M–N–C 催化剂中金属颗粒普遍与单原子共存，此类催化剂的 ORR 活性因此也取决于颗粒，颗粒在工作条件下的表面覆盖决定了相邻单原子的轴向配体。在其他电催化反应中，电解液物种同样覆盖颗粒和单原子，因此共存颗粒在工作条件下的表面覆盖同样决定着调节这些反应中单原子的轴向配体。

通读提醒：S5 和 S6 都写了 surface coverage under working conditions。这是有意保留的，用来把 ORR 的结论接到其他反应上。如果赵月嫌重复，S6 可以改成 the same surface coverage。
