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

## 14:05 精简版（赵月：太啰嗦）
S5：In pyrolyzed M–N–C catalysts, coexisting metal particles thus shape the activity of single atoms through the axial ligand that their surface coverage sets under working conditions.
直译：由此可见，在热解 M–N–C 催化剂中，共存的金属颗粒通过其表面覆盖在工作条件下决定的轴向配体，影响单原子的活性。
S6：Because electrolyte species cover both particles and single atoms in any electrocatalytic reaction, this effect extends to other reactions on M–N–C catalysts.
直译：由于在任何电催化反应中，电解液物种都会覆盖颗粒和单原子，这一作用也适用于 M–N–C 催化剂上的其他反应。
（两句分别为 26 词和 22 词。不点名具体反应，理由同上：OER 电位下 Mn 已经是 Mn=O。）

## 14:08 对赵月第二句（中文稿）的意见
赵月稿：将共存金属颗粒与表面覆盖纳入考量，为理解和设计用于各类受中间体结合支配的电催化反应的 M–N–C 催化剂提供了更广阔的依据。

**好的地方**：适用范围定为"受中间体结合支配的电催化反应"，比我写的"其他反应"更准确，也有依据。前言第一段写的正是活性取决于中间体结合（文献 3–5），这一点对多数电催化反应都成立。我采纳。

**两处建议**
1. 删去"更广阔"。这是比较级，却没有比较对象，读者会问比什么更广，只能理解为"比裸单原子模型更广"，又回到防御的写法。去掉以后意思不变。
2. "设计"可以保留，但要知道它离赵月否定过的 design principle 很近。本文只提出了理解，没有给出设计规则。若想更稳，只写"理解"。

**英文**
Accounting for coexisting metal particles and their surface coverage thus provides a basis for understanding and designing M–N–C catalysts for electrocatalytic reactions governed by intermediate binding.
直译：由此可见，将共存金属颗粒及其表面覆盖纳入考量，为理解和设计用于受中间体结合支配的电催化反应的 M–N–C 催化剂提供了依据。

（只写"理解"的版本：把 understanding and designing M–N–C catalysts 改为 understanding M–N–C catalysts。）

**与第一句连读**
In pyrolyzed M–N–C catalysts, coexisting metal particles thus shape the activity of single atoms through the axial ligand that their surface coverage sets under working conditions. Accounting for coexisting metal particles and their surface coverage therefore provides a basis for understanding and designing M–N–C catalysts for electrocatalytic reactions governed by intermediate binding.
两句的连接词改为一个 thus、一个 therefore，避免重复。第二句第二次出现 coexisting metal particles，可以改成 Accounting for these particles and their surface coverage，以免重复。

## 14:10 合成一句（赵月：结尾就一句）
Because coexisting metal particles set the axial ligand of adjacent single atoms through their surface coverage under working conditions, accounting for these particles provides a basis for understanding M–N–C catalysts in electrocatalytic reactions governed by intermediate binding.
直译：由于共存的金属颗粒通过其在工作条件下的表面覆盖决定相邻单原子的轴向配体，将这些颗粒纳入考量，为理解受中间体结合支配的电催化反应中的 M–N–C 催化剂提供了依据。
- 前半句回应摘要第 1、2 句（颗粒共存、工作条件下的表面覆盖），并落在本文独有价值上：颗粒决定轴向配体。
- 后半句把适用范围扩大到受中间体结合支配的电催化反应，这一点依据前言第一段。
- 后半句只写"理解"，不写"设计"。若要加上，改为 understanding and designing。
