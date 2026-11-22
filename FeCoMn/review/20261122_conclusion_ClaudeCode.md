# FeCoMn 结论怎么写（Claude Code 本地，2026-11-22）

依据：`discussion/REQUEST_Conclusion_20261122.md`、`discussion/Gemini_brief_Conclusion_20261122.md`。未读其他智能体的回复，独立给出。未改 Word。

## 1. 结论应承担的角色

这篇论文的摘要和前言第三段都已经把整条因果链完整讲了一遍：性能，红外，覆盖计算，Mn–OH 与 Mn=O，成键能力，出平面几何，火山图。读者读到结论时，已经第三次见到这条链。所以结论不该再讲第四遍，它只需要做三件摘要和前言做不到的事：

1. **直接回答前言提出的问题。** 前言第二段的问题是：工作条件下的金属颗粒和表面覆盖，如何影响相邻单原子对中间体的结合。结论要用一句话给出答案：颗粒通过工作条件下的覆盖固定了相邻 Mn 的轴向配体，轴向配体决定中间体结合的强弱。
2. **把机理收成一条规律，不复述过程。** 轴向配体同时管住结合的两端：Mn=O 占掉成键能力，使结合过弱；没有轴向配体时 OH* 结合过强；轴向 OH 用弱键保住成键能力，又用出平面位移让对侧吸附付出部分结合能，从而落在中间。这是赵月所说的价值 (b)，讲规律，不列 0.44 Å、0.34 eV。
3. **意义落在本文独有的内容上，不泛化到多组分体系。** 本文与 Wan 2022 的区别在价值 (a)：配体由工作电位和 pH 下的覆盖决定，颗粒把 Mn–OH 转为 Mn=O 的电位从 0.48 V 推到 0.96 V。所以最后一句的意义应写成：单原子的活性取决于相邻颗粒在多宽的电位范围内为它保住合适的轴向配体。这句只属于本文，不是放之四海而皆准的套话。

数字只保留三组：0.885 V 和 96.5%/238 h（性能），0.48 V 到 0.96 V（价值 a 的唯一证据）。

## 2. 现有各版差在哪里

| 版本 | 主要问题 |
|---|---|
| 导师返回版 | 以方法为主语（accounted for … by combining analyses），写 dispersed Mn species 不写单原子；用 ΔG_OH* 0.85 eV 和 0.78 V 让读者自己比；没有写出颗粒到配体的因果；结尾 should start from 是对读者提要求。导师已批最后再改。 |
| V0（现 Word） | 数字堆积（0.48/0.96、0.44 Å、0.34/0.24/0.10 eV、三个极限电位），像结果部分的缩写；没有稳定性；Relative to overly strong binding … weakens by 0.34 eV 句子别扭；结尾 should be analyzed 是对读者提要求。 |
| C1、C2 | 没有呼应前言的问题（赵月批 C2 一点都不看摘要和前言）；C2 结尾 offers a way to design 偏泛。 |
| C3 | 呼应了前言，但几乎是摘要的逐句复述（Gemini 指出），且缺 0.48 到 0.96 V。 |
| C4、C6、C9、C10（Gemini） | 按摘要顺序再讲一遍因果链；Mn–O 应为 Mn=O；while shifting Mn … 的主语悬空；结尾 clarifies how、is essential to capture 只说能揭示，没说出答案；缺 0.48 到 0.96 V。 |
| C5 | 结构最接近答案先行，但丢了价值 (a) 的电位证据，结尾用 bare single-atom models do not capture 这种否定式收尾。 |
| C7、C8 | 仍是 C6 的复述结构；C8 结尾同样是否定式。 |
| C11 | 结尾拉到 multicomponent electrocatalytic systems，泛化，冲淡本文价值（赵月已批）。 |
| V1 | 即 C11 改结尾后的版本，问题同 C4 一类，并且缺 0.48 到 0.96 V。 |
| C12、V2（80 分） | 三点价值都在，事实正确；但骨架仍是摘要的压缩版（性能、覆盖、两种机理、火山图、意义），读者看不出结论比摘要多给了什么；结尾 not spectators 是否定式修辞；没有一句明确回答前言的问题。 |
| V3（答案先行） | 方向对，但做过了头：删掉了 0.48 到 0.96 V，价值 (a) 失去证据；两端机理压成 through bonding capacity and out-of-plane geometry 一个短语，价值 (b) 读不出来；性能降为 consistent with 的从属成分；结尾 leave out 又是否定式。所以比 V2 差。 |
| V4（Gemini 终稿） | 基本是 C12 的润色版，问题相同；另有 while shifting Mn … forces 主语悬空；结尾 not spectators 否定式。 |

共同问题：所有版本都在**按摘要的顺序复述过程**，没有一版把结论当作回答问题、收成规律、落到本文独有意义的地方。V3 想做答案先行，却丢了证据和两端机理。

## 3. 我的版本

### 英文
In summary, we prepared an FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. FeCoMn–NC reaches an ORR half-wave potential of 0.885 V versus RHE in 0.1 M KOH, higher than those of Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h. Under working conditions, the FeCo particles affect the adjacent Mn single atoms by fixing their axial ligand. Surface coverage calculations at the working potential and pH show that the O*-covered particles raise the potential at which the axial OH on Mn turns into an axial O from 0.48 to 0.96 V versus RHE, so Mn keeps the axial OH at the ORR working potential. The axial ligand sets both limits of intermediate binding at Mn. An axial O forms an Mn=O double bond that takes up most of the bonding capacity of Mn, so Mn binds OOH* too weakly, whereas Mn without an axial ligand binds OH* too strongly. The axial OH avoids both limits, because its weak bond leaves Mn enough bonding capacity for OOH* and its pull on Mn out of the N4 plane makes opposite-side adsorption spend part of the binding energy to draw Mn back. FeCoMn–NC therefore binds the ORR intermediates moderately and lies near the apex of the activity volcano. The activity of single atoms next to metal particles thus depends on the potential range over which the covered particles keep a suitable axial ligand on these single atoms.

### 中文直译
总之，我们制备了一种 FeCo 合金颗粒与 Mn 单原子共存的 FeCoMn–NC 催化剂。FeCoMn–NC 在 0.1 M KOH 中的 ORR 半波电位达到 0.885 V（相对 RHE），高于 Pt/C、FeCo–NC 和 Mn–NC，并在 238 h 后保持初始电流的 96.5%。在工作条件下，FeCo 颗粒通过固定相邻 Mn 单原子的轴向配体来影响这些单原子。在工作电位和 pH 下的表面覆盖计算表明，被 O* 覆盖的颗粒把 Mn 上轴向 OH 转变为轴向 O 的电位从 0.48 V 提高到 0.96 V（相对 RHE），因此 Mn 在 ORR 工作电位下保持轴向 OH。轴向配体决定了 Mn 上中间体结合的两个极限。轴向 O 与 Mn 形成 Mn=O 双键，占去 Mn 的大部分成键能力，因此 Mn 对 OOH* 结合过弱，而没有轴向配体的 Mn 对 OH* 结合过强。轴向 OH 避开了这两个极限，因为它的弱键为 Mn 留下足够的成键能力来结合 OOH*，而它把 Mn 拉出 N4 平面，使对侧吸附要消耗部分结合能把 Mn 拉回。因此，FeCoMn–NC 对 ORR 中间体的结合适中，位于活性火山图的顶点附近。由此，位于金属颗粒旁的单原子的活性，取决于被覆盖的颗粒能在多宽的电位范围内为这些单原子保持合适的轴向配体。

### 逐句对应
1. 做了什么。
2. 性能，只给半波电位和稳定性。
3. 直接回答前言的问题（价值 c）。
4. 证据：工作条件覆盖，0.48 V 到 0.96 V（价值 a）。
5. 规律：轴向配体管两端。
6. 两端各是什么（过弱和过强）。
7. 轴向 OH 为何落在中间（价值 b，电子和几何各一句，不列数字）。
8. 落到火山图。
9. 意义：只属于本文的电位范围这一结论，与 Wan 2022 的永久轴向 OH 区分开。

### 规则自查
- 无 first、novel，无 should，无防御性限定词，无破折号。
- 主语均为具体名词，没有用 It 或 This 作主语。
- 句 7 的 avoids both limits 后面紧跟正面原因，不是纯否定句。
- 机理部分只有 0.48 V 和 0.96 V 两个数，它们是价值 (a) 的证据。0.44 Å、0.34/0.24/0.10 eV、三个极限电位都没有进结论。
- 所有内容都能在正文图 5 末段（Table S7）和图 6 第二段中找到。

## 4. 一个需要赵月确认的事实口径
0.48 V 到 0.96 V 来自 Table S7，按 11-18 定下的首次分支口径。T039（11-20）的两分支对照显示：若比较同一电子态分支，有无颗粒的转变电位差只有约 0.03 V。结论把 0.48 V 到 0.96 V 作为价值 (a) 的唯一证据写入，前提是正文和 SI 继续采用首次分支口径。如果口径有变，第 4 句和第 9 句要一起改。
