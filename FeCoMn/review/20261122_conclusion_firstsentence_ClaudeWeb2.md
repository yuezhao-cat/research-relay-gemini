# 结论第一句（Claude web 2，2026-11-22 12:50）
依据：REQUEST_Conclusion_20261122.md 的"12:45 更新"。未读其他方回复。未改 Word。

## 1. 第一句：A、B、C 都不直接用，我给一个 A 的修改版

**三个候选的问题**
- **A**：三个动词并列，读起来是三件平行的事。可它们其实有先后因果：先确定表面状态，才揭示了颗粒的作用，再由此解释了活性。另外，句尾 which explains its high ORR activity 里的 which，指代的是前面哪个动作并不清楚，违反主语明确的规则。
- **B**：去掉了"制备"，把 FeCoMn–NC 当成研究对象，这个立意很好。但它只用了"揭示"一个动词，"确定了工作条件下的表面状态"这个独有价值 (a) 就丢了。而颗粒作用的依据正是表面状态。
- **C**：仍有 which explains 指代不清的问题。而且 outperforms Pt/C, FeCo–NC, and Mn–NC 和 S2 的性能句重复，第一句因此变得很长。

**我的版本：两个动词，用 thereby 连成因果。解释活性的部分留给 S4，等机理讲完再说。**

In summary, we determined the surface state of FeCoMn–NC, a catalyst combining FeCo alloy particles and Mn single atoms, under working conditions and thereby revealed how the FeCo particles affect intermediate binding at the adjacent Mn single atoms.

直译：总之，我们确定了兼具 FeCo 合金颗粒与 Mn 单原子的催化剂 FeCoMn–NC 在工作条件下的表面状态，并由此揭示了 FeCo 颗粒如何影响相邻 Mn 单原子上的中间体结合。

理由有三条。
- 第一句直接回答前言的问题："颗粒和工作条件下的表面覆盖如何影响相邻单原子的中间体结合"。
- "确定"是手段，"揭示"是结果，thereby 交代两者的关系，不是平铺三件事。
- 不写 prepared，制备只是前提，不是本文解决的问题。不写"解释活性"，这一点到 S4 讲完机理以后才站得住。

## 2. S2–S5 怎么配合

**S2 性能：保留对照比较，第一句已经不再写"优于"。**
In 0.1 M KOH, FeCoMn–NC reaches an ORR half-wave potential of 0.885 V versus RHE, outperforming Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h.
直译：在 0.1 M KOH 中，FeCoMn–NC 的 ORR 半波电位达到 0.885 V（相对于 RHE），优于 Pt/C、FeCo–NC 和 Mn–NC，并在 238 h 后保持其初始电流的 96.5%。

**S3 证据（对应"确定了"）：把 Under working conditions 换掉，和第一句不重复，同时写出完整的表面状态。**
At the working potential and pH, the FeCo particles are covered by O* and raise the Mn–OH to Mn=O transition of the adjacent Mn single atoms from 0.48 to 0.96 V versus RHE, so the Mn single atoms keep an axial OH during the ORR.
直译：在工作电位和 pH 下，FeCo 颗粒被 O* 覆盖，并把相邻 Mn 单原子由 Mn–OH 转变为 Mn=O 的电位从 0.48 V 提高到 0.96 V（相对于 RHE），因此 Mn 单原子在 ORR 过程中保持轴向 OH。

**S4 机理与活性（对应"解释了"）：拆成两句。** 原句末尾写 the ORR activity of FeCoMn–NC lies near the apex，可是"活性位于火山顶"在语义上不通，位于火山顶附近的应该是催化剂本身。
The axial OH leaves Mn more bonding capacity than an axial Mn=O does and holds Mn out of the N₄ plane, so intermediate binding falls between the weak binding of Mn=O and the strong binding of ligand-free Mn. FeCoMn–NC therefore lies near the apex of the activity volcano, consistent with its highest measured ORR activity.
直译：轴向 OH 比轴向 Mn=O 为 Mn 留下更多成键能力，并使 Mn 保持在 N₄ 平面之外，因此中间体结合处于 Mn=O 的过弱结合与无配体 Mn 的过强结合之间。因此，FeCoMn–NC 位于活性火山图顶点附近，与其实测最高的 ORR 活性一致。

**S5 意义（对应"揭示了"的落脚点）：删掉 extends the understanding of ORR catalysis beyond bare-site models。** 这半句是赵月已经否定过的套话，而且 beyond bare-site models 还带一点防御意味。改为写出本文独有的规律，并和 Wan 2022 区分开：Wan 的轴向 OH 是永久配体，本文的轴向配体是随电位变化、由颗粒控制的状态。
The O*-covered FeCo particles therefore regulate intermediate binding at the adjacent Mn single atoms by raising the potential at which Mn changes its axial ligand, so the axial ligand of a single atom beside a metal particle is a working-condition state controlled by the particle.
直译：因此，被 O* 覆盖的 FeCo 颗粒通过提高 Mn 更换轴向配体的电位来调控相邻 Mn 单原子上的中间体结合，所以金属颗粒旁单原子的轴向配体是由颗粒控制的、工作条件下的状态。

## 3. 全段（6 句，供拼合）
In summary, we determined the surface state of FeCoMn–NC, a catalyst combining FeCo alloy particles and Mn single atoms, under working conditions and thereby revealed how the FeCo particles affect intermediate binding at the adjacent Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches an ORR half-wave potential of 0.885 V versus RHE, outperforming Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h. At the working potential and pH, the FeCo particles are covered by O* and raise the Mn–OH to Mn=O transition of the adjacent Mn single atoms from 0.48 to 0.96 V versus RHE, so the Mn single atoms keep an axial OH during the ORR. The axial OH leaves Mn more bonding capacity than an axial Mn=O does and holds Mn out of the N₄ plane, so intermediate binding falls between the weak binding of Mn=O and the strong binding of ligand-free Mn. FeCoMn–NC therefore lies near the apex of the activity volcano, consistent with its highest measured ORR activity. The O*-covered FeCo particles therefore regulate intermediate binding at the adjacent Mn single atoms by raising the potential at which Mn changes its axial ligand, so the axial ligand of a single atom beside a metal particle is a working-condition state controlled by the particle.

直译：总之，我们确定了兼具 FeCo 合金颗粒与 Mn 单原子的催化剂 FeCoMn–NC 在工作条件下的表面状态，并由此揭示了 FeCo 颗粒如何影响相邻 Mn 单原子上的中间体结合。在 0.1 M KOH 中，FeCoMn–NC 的 ORR 半波电位达到 0.885 V（相对于 RHE），优于 Pt/C、FeCo–NC 和 Mn–NC，并在 238 h 后保持其初始电流的 96.5%。在工作电位和 pH 下，FeCo 颗粒被 O* 覆盖，并把相邻 Mn 单原子由 Mn–OH 转变为 Mn=O 的电位从 0.48 V 提高到 0.96 V（相对于 RHE），因此 Mn 单原子在 ORR 过程中保持轴向 OH。轴向 OH 比轴向 Mn=O 为 Mn 留下更多成键能力，并使 Mn 保持在 N₄ 平面之外，因此中间体结合处于 Mn=O 的过弱结合与无配体 Mn 的过强结合之间。因此，FeCoMn–NC 位于活性火山图顶点附近，与其实测最高的 ORR 活性一致。因此，被 O* 覆盖的 FeCo 颗粒通过提高 Mn 更换轴向配体的电位来调控相邻 Mn 单原子上的中间体结合，所以金属颗粒旁单原子的轴向配体是由颗粒控制的、工作条件下的状态。

注：第 5、6 句都用 therefore。拼合时建议第 6 句改用 thus 开头，或写成 Coexisting metal particles thus...（直译"由此可见，共存的金属颗粒……"）。

## 4. 规则自查
- 英文中没有冒号、分号和破折号。
- 没有 should、first、novel，也没有纯否定句。
- 计算数字只有 0.48 和 0.96 V。
- 每句主语都明确，没有 which 指代不清的从句。
- 内容与正文一致：
  - 0.48/0.96 V 与表 S7 和图 5 末尾一致。
  - 成键能力和出平面与图 6 第二段一致。
  - 无配体 Mn 结合过强与表 S11 一致。
  - 火山顶点与图 6h 一致。
