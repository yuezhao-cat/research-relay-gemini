# 结论怎么写（Claude web 2，2026-11-22 12:35）
依据：`discussion/REQUEST_Conclusion_20261122.md`、`discussion/Gemini_brief_Conclusion_20261122.md`。未读其他方的回复，独立写。未改 Word 和其他文件。

## 1. 结论应承担的角色

**诊断：所有版本都是摘要的第三遍复述。** 摘要和前言第三段已经把完整机理按同一顺序讲了两遍，顺序是：制备、性能、红外、覆盖计算、轴向 OH、三种结合强度、火山图、颗粒决定配体。现有结论几乎都沿用这个顺序，只是压缩一下，所以无论怎么改都显得重复。V3 换成答案先行，却把因果链也一起删了，于是更差。

**我认为结论要做三件事，摘要和前言都没替它做：**
1. **回答前言提出的问题，并用一句话说清"颗粒通过什么起作用"。** 前言的问题是：颗粒和工作条件下的表面覆盖如何影响相邻单原子的中间体结合。答案是：颗粒通过 Mn 在工作条件下从电解液得到的轴向配体起作用。这句要单独成句，不能埋在长句里。
2. **用一条因果链收束三种情况，只保留独有价值的那一个数。** 唯一保留的计算数是 0.48→0.96 V，因为它就是颗粒作用的量化证据，对应独有价值 (a)。三种结合强度（Mn=O 过弱，无配体过强，Mn–OH 适中）各一句，不出现 eV、Å 和极限电位。
3. **最后一句写本文独有的规律，不写放之四海皆准的套话。** 这句话要和 Wan 2022 区分开。Wan 的轴向 OH 是永久配体，本文有三点不同：颗粒改变的是"Mn 在什么电位换配体"；轴向 OH 通过成键能力和 Mn 出平面位置两条途径调节结合；颗粒本身被 O* 覆盖。最后一句要把 (a)(b)(c) 三点都落到具体对象上。

**措辞上也和摘要拉开。** 摘要说的是 keep an axial OH，结论改说"把 Mn–OH 被氧化成 Mn=O 的电位从 0.48 V 提高到 0.96 V"。这样讲的是颗粒改变了一个电位，读者读到的是规律，不是又一次描述状态。

## 2. 各版本差在哪里
| 版本 | 主要问题 |
|---|---|
| 导师返回版 | 用 dispersed Mn species，与正文"单原子"不一致；没写颗粒的作用；ΔG_OH* 0.85 eV 是堆数字；结尾 should 是对读者提要求 |
| V0（现 Word） | 数字堆砌（0.44 Å、0.34/0.24/0.10 eV、三个极限电位），像结果部分的缩写；没写稳定性；Relative to... weakens by 0.34 eV 别扭；结尾 should |
| C1 | 写 axial O，不是 Mn=O；没写 0.48→0.96 V；结尾 tune intermediate binding 泛泛 |
| C2 | 没回应前言问题；结尾 offers a way to design 是套话 |
| C3 | 和摘要几乎逐句对应；instead of using bare single-atom models 带防御意味；最后一句用了冒号 |
| C4、C6、C9、C10、C11、V1（Gemini 系列） | 键写成 Mn–O，应为 Mn=O；while shifting Mn... allows/forces 主语悬空；C4 用 It 开头；V1、C11 用冒号；都没写 0.48→0.96 V；C11、V1 结尾泛泛 |
| C5 | rather than on bare single atoms 和 do not capture 是防御加否定；写 axial O |
| C7、C8 | 修好了 Mn=O 和几何半句；C8 结尾 do not capture 是否定句 |
| C12 | 内容最全，三点价值都有。但和摘要同序复述；结尾 not spectators 是纯否定，还用了冒号 |
| V2（80 分） | 因果链清楚。但没有单独一句回答"颗粒通过什么起作用"；最后一句和摘要最后一句几乎相同；也没写出与 Wan 的区别（电位、两条途径） |
| V3（更差） | 开头没交代做了什么；三种结合强度压成一句 through bonding capacity and out-of-plane geometry，因果链丢了；写 axial O；结尾 leave out 有指责别人的防御味 |
| V4（Gemini 终稿） | 键名已改对，0.48→0.96 V 也写了。但 while shifting Mn... forces 主语悬空；结尾 not spectators 是否定加冒号加分号；整体仍是摘要同序复述 |

**最接近的是 C12 和 V2。** 我的版本以 V2 的因果链为骨架，补上三处：单独一句回答问题；把 0.48→0.96 V 改写成"电位"的说法；最后一句写出与 Wan 的区别。

## 3. 我的版本

In summary, we prepared an FeCoMn–NC catalyst combining FeCo alloy particles and Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches an ORR half-wave potential of 0.885 V versus RHE, outperforming Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h. The FeCo particles act on the adjacent Mn single atoms through the axial ligand that Mn takes up from the electrolyte under working conditions. Surface coverage calculations at the working potential and pH show that the O*-covered FeCo particles raise the potential at which the axial OH on Mn is oxidized to Mn=O from 0.48 to 0.96 V versus RHE, so Mn keeps an axial OH during the ORR. The axial ligand sets how strongly Mn binds the ORR intermediates. An axial Mn=O double bond occupies most of the bonding capacity of Mn and leaves OOH* bound too weakly, and Mn without an axial ligand binds OH* too strongly. The weaker axial Mn–OH bond leaves Mn enough bonding capacity for OOH*, and the axial OH pulls Mn out of the N₄ plane, so each intermediate adsorbing on the opposite side spends part of its binding energy drawing Mn back. FeCoMn–NC therefore binds the intermediates moderately and lies near the apex of the activity volcano. Coexisting metal particles thus tune adjacent single atoms by shifting the potential at which the single atoms change their axial ligand, and the axial OH kept by the particles moderates intermediate binding through both the bonding capacity and the out-of-plane position of Mn.

**中文直译：**
总之，我们制备了一种结合 FeCo 合金颗粒和 Mn 单原子的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的 ORR 半波电位达到 0.885 V（相对于 RHE），优于 Pt/C、FeCo–NC 和 Mn–NC，并在 238 h 后保持其初始电流的 96.5%。FeCo 颗粒通过 Mn 在工作条件下从电解液中获得的轴向配体作用于相邻的 Mn 单原子。在工作电位和 pH 下的表面覆盖计算表明，被 O* 覆盖的 FeCo 颗粒把 Mn 上轴向 OH 被氧化为 Mn=O 的电位从 0.48 V 提高到 0.96 V（相对于 RHE），因此 Mn 在 ORR 过程中保持轴向 OH。轴向配体决定 Mn 结合 ORR 中间体的强弱。轴向 Mn=O 双键占用了 Mn 的大部分成键能力，使 OOH* 结合过弱；而没有轴向配体的 Mn 结合 OH* 过强。较弱的轴向 Mn–OH 键为 OOH* 留下了足够的成键能力，同时轴向 OH 把 Mn 拉出 N₄ 平面，因此每个在对侧吸附的中间体都要消耗一部分结合能把 Mn 拉回。因此，FeCoMn–NC 对中间体的结合适中，位于活性火山图顶点附近。由此可见，共存的金属颗粒通过改变单原子更换轴向配体的电位来调控相邻单原子，而颗粒保持住的轴向 OH 又同时通过 Mn 的成键能力和 Mn 的出平面位置使中间体结合变得适中。

（直译中的分号只用于中文断句，英文原文没有分号或冒号。）

## 4. 规则自查
- 计算数字：只有 0.48 和 0.96 V，对应独有价值 (a)。没有 eV、Å，也没有极限电位。
- 没有 first 或 novel，没有 should，没有防御句。
- 没有纯否定句：结尾不用 not spectators、do not capture。
- 每句主语明确，没有用 It 或 This 开头。
- 英文没有破折号，没有冒号，也没有分号。
- 内容与正文一致，逐句对照如下：
  - 0.48/0.96 V 对应图 5 末尾和表 S7。
  - Mn=O 占成键能力、OOH* 过弱，对应图 6 第二段和前言第三段。
  - 无配体时 OH* 过强，对应表 S11。
  - 出平面后被拉回、消耗结合能，对应图 6 第二段和图 S30。
  - 火山图顶点，对应图 6h。
- 和 Wan 2022 的区别写在最后一句：颗粒改变的是更换配体的电位，结合通过两条途径调节。

## 5. 结论之外的一点提醒
结论难写，根源在前言第三段。它和摘要几乎逐句相同，连 0.48→0.96 V 和三种结合强度都写全了。这样结论无论怎么写，都是同一内容的第三遍。如果以后允许改已定稿的前言，可以把第三段压缩为"做了什么、发现了什么"两三句，机理细节留给正文和结论。这一条只是提醒，本次不要求改动。
