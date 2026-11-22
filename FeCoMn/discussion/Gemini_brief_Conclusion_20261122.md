# FeCoMn–NC 论文结论改写资料包（给 Gemini）

整理：Claude web，2026-11-22 12:00。正文最新版本：FeCoMn_Manuscript_revised_20261122_1140。

## 1. 任务

请重写论文的 CONCLUSIONS 一段（英文），并给出完整的中文直译。要求见第 2 节。可以参考第 6 节 Claude 的草稿，但不必沿用。

## 2. 写作要求（作者定下的规则，必须遵守）

1. 结构参照高水平论文（见第 7 节）：第一句交代做了什么；性能只给最关键的一两个数；机理用因果链讲，分别说明结合过强、过弱和适中三种情况；最后一句写这项工作的意义。
2. 机理部分不堆计算数值（导师批注过：不要把数字列出来让读者自己比，直接写规律）。0.44 Å、0.34/0.24/0.10 eV 这类数字不进结论。
3. 不写防御性语句：不写局限性，不用 tentatively、within the sampled models 这类限定词，不写纯否定或自我辩护的句子。
4. 不写 first、for the first time、novel 一类表述（原因见第 8 节）。
5. 每句话主语明确，不用指代不清的 it、this、this step。用词平实，不故作深奥。
6. 不用破折号（—），不用中文双引号。
7. 结论内容必须与正文一致，机理以正文图 5 末尾和图 6 两段为准（第 5 节）。不要引入正文没有的内容。
8. 不要写成对读者提要求的句子（例如 should be analyzed）。

## 3. 现在的结论（作者和 Claude 都认为不好）

An FeCoMn–NC catalyst with FeCo alloy particles and Mn single atoms reaches an ORR half-wave potential of 0.885 V versus RHE, surpassing Pt/C, FeCo–NC, and Mn–NC. At pH 13, O*-covered FeCo alloy particles shift the Mn–OH to Mn=O transition from 0.48 to 0.96 V versus RHE. Adjacent Mn single atoms thus keep an axial OH at 0.78 V versus RHE, whereas Mn–NC forms Mn=O. Compared with Mn=O, the weaker axial Mn–OH bond lets Mn bind OOH* more firmly. Meanwhile, the axial OH pulls Mn 0.44 Å out of the N₄ plane, and opposite-side adsorption draws Mn back. Relative to overly strong binding without the axial OH, OH* adsorption weakens by 0.34 eV (0.24 eV from structural deformation and 0.10 eV from weaker electronic interaction). FeCoMn–NC thus achieves a limiting potential of 0.78 V versus RHE near the volcano apex, exceeding FeCo–NC (0.34 V) and Mn–NC (0.26 V). Coexisting particle and single-atom catalysts should be analyzed on covered surfaces under reaction conditions, where particles determine the axial ligand that balances intermediate binding through electronic structure and geometry.

问题：
- 数字太多：0.48/0.96 V、0.44 Å、0.34/0.24/0.10 eV、三个极限电位，读起来像结果部分的缩写版。
- 句子别扭，例如 Relative to overly strong binding without the axial OH, OH* adsorption weakens by 0.34 eV。
- 没有提稳定性。
- 最后一句 should be analyzed 是对别人提要求，没有落到这项工作说明了什么。

## 4. 导师返回版的结论（导师批注：最后再改）

We prepared an FeCoMn–NC catalyst in which FeCo alloy particles coexist with dispersed Mn species and accounted for its favorable ORR performance by combining surface coverage, reaction free-energy, and electronic-structure analyses. At the operating potential and pH, the coverage calculations give O* coverage on the FeCo particle surface and axial OH coordination at the Mn site, and the corresponding limiting potential reaches 0.78 V. Bonding and charge analyses show that FeCoMn–NC stabilizes OOH* more strongly than Mn–NC while avoiding the overly strong OH* binding at the multimetal sites of FeCo–NC, thereby facilitating the initial intermediate formation and final hydroxyl removal. Its ΔG_OH* of 0.85 eV lies close to the volcano optimum, corresponding to moderate intermediate binding. These results show that activity analysis of catalysts in which particles and dispersed metal sites coexist should start from the surface coverage and coordination formed under operating conditions and connect specific bonding interactions with the reaction steps.

## 5. 正文核心内容（结论必须与这些一致）

### 5.1 摘要（已定稿）
Metal particles often coexist with single atoms in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet models usually treat bare single atoms as the only active sites. How particles and surface coverage under working conditions affect intermediate binding at adjacent single atoms remains unclear. Here, we prepare an FeCoMn–NC catalyst combining FeCo alloy particles and Mn single atoms. In 0.1 M KOH, FeCoMn–NC achieves an oxygen reduction reaction (ORR) half-wave potential of 0.885 V versus RHE, outperforming Pt/C, FeCo–NC, and Mn–NC. FeCoMn–NC also retains 96.5% of its initial current after 238 h. Operando infrared spectroscopy shows that surface species change with potential, so we calculated surface coverage under working conditions. At 0.78 V versus RHE, O*-covered FeCo alloy particles keep an axial OH on adjacent Mn single atoms, whereas Mn without particles forms Mn=O. Compared with Mn=O, the much weaker axial Mn–OH bond lets Mn bind OOH* firmly enough for OOH* formation. Without the axial OH, Mn binds ORR intermediates too strongly. The axial OH pulls Mn out of the N₄ plane toward itself, and opposite-side intermediate adsorption draws Mn back. Drawing Mn back consumes part of the binding energy and weakens excessive adsorption. At 0.78 V versus RHE, OH* removal turns downhill and OOH* formation stays nearly thermoneutral, placing FeCoMn–NC near the volcano apex. FeCo alloy particles thus determine the axial ligand of adjacent Mn single atoms, keeping intermediate binding neither too strong nor too weak.

### 5.2 前言第三段（已定稿）
Here, we report an FeCoMn–NC catalyst combining FeCo alloy particles and Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches a half-wave potential of 0.885 V versus RHE, outperforming commercial Pt/C, FeCo–NC, and Mn–NC. FeCoMn–NC also retains 96.5% of its initial current after 238 h. Operando infrared spectroscopy shows that surface species change with potential, so we calculated surface coverage under working conditions. At pH 13, O*-covered FeCo alloy particles shift the Mn–OH to Mn=O transition from 0.48 to 0.96 V versus RHE. At 0.78 V versus RHE, adjacent Mn single atoms thus keep an axial OH, whereas particle-free Mn–NC forms Mn=O. In Mn–NC, the axial O forms a strong Mn=O double bond that takes up most of the bonding capacity of Mn, so Mn binds OOH* on the opposite side too weakly and OOH* formation is hindered. The much weaker axial Mn–OH bond in FeCoMn–NC leaves more bonding capacity for OOH*, so OOH* forms readily. Without the axial OH, Mn binds ORR intermediates too strongly, so that OH* removal limits the ORR. The axial OH pulls Mn out of the N₄ plane, and opposite-side intermediate adsorption draws Mn back. Drawing Mn back consumes part of the binding energy and weakens excessive adsorption. In FeCo–NC, by contrast, O*-covered FeCo alloy particles bind O* too strongly and hinder O* conversion to OH*. At 0.78 V versus RHE, OH* removal on FeCoMn–NC is downhill and OOH* formation stays nearly thermoneutral. FeCoMn–NC therefore lies near the activity volcano apex, accounting for the highest measured ORR activity. FeCo alloy particles thus determine the axial ligand of adjacent Mn single atoms, keeping intermediate binding neither too strong nor too weak.

### 5.3 图 5 末尾：覆盖与颗粒作用
The free energies of many different coverage configurations were therefore compared to determine the surface states of the three catalysts at various potentials and pH (Figure 5 and Table S5). As shown in Figure 5a–c, the surfaces of all three catalysts are covered by H* at negative potentials, and adsorbed O-containing species become more stable as the potential increases. As shown in Figure 5d–f, the surface coverage of FeCoMn–NC changes from 8H* to 8O* with increasing potential, then to 8O* + Mn–OH*, and finally to 8O* + Mn–O*. The surface coverage of FeCo–NC changes only from 8H* to 8O*, whereas that of Mn–NC changes from 3H* to the clean surface and then to 1O* and 2O*. Figures S13–S16 and S17–S22 give the corresponding free-energy data and structures, respectively. At 0.78 V versus RHE (a representative ORR potential)¹⁶ and pH 13, which corresponds to the 0.1 M KOH electrolyte, the surface coverage is 8O* + Mn–OH* for FeCoMn–NC, 8O* for FeCo–NC, and 1O* for Mn–NC. The corresponding structures are shown in Figure 5g and Figure S24. To identify the role of the FeCo particles, we removed the particle from the FeCoMn–NC model and kept all other atoms and calculation settings unchanged. Without the particle, the axial ligand on Mn changes from OH to O at 0.48 V, whereas with the particle this change occurs only at 0.96 V (Table S7). The FeCo particles therefore keep the adjacent Mn single atoms in the Mn–OH state at the representative ORR potential of 0.78 V, whereas without the particles Mn is oxidized to Mn=O. The FeCo particles thus determine the surface coverage of FeCoMn–NC under reaction conditions, namely O* on the particles and an axial OH on the adjacent Mn single atoms.

### 5.4 ORR 自由能段
On these covered surfaces, obtained with the actual potential and solution pH taken into account, the free energies of the four-step associative pathway of O₂ → OOH* → O* → OH* → H₂O were then calculated. Here, ΔG₁, ΔG₂, ΔG₃, and ΔG₄ refer to the reaction free energies of OOH* formation, OOH* conversion to O*, O* conversion to OH*, and OH* removal, respectively (Table S8). On FeCoMn–NC and Mn–NC, the intermediates bind to Mn, and on FeCo–NC to the O-covered particle (Table S9 and Figure S25). Figure 5h compares the three pathways at 0.78 V, and Figure S26 shows them at 0 V. On FeCo–NC, O* binds too strongly, so its conversion to OH* is uphill by 0.44 eV. On Mn–NC, OOH* binds too weakly, so its formation is uphill by 0.52 eV. On FeCoMn–NC, the largest step is OOH* formation, which is uphill by less than 0.01 eV, and the other three steps are downhill. The limiting potentials of FeCoMn–NC, FeCo–NC, and Mn–NC are therefore 0.78, 0.34, and 0.26 V, corresponding to theoretical overpotentials of 0.45, 0.89, and 0.97 V (Table S8). The order of the limiting potentials agrees with that of the measured half-wave potentials (Figure 3b), and the moderate intermediate binding of FeCoMn–NC accounts for its higher activity than FeCo–NC and Mn–NC.

### 5.5 图 6 第一段（反应前）
To understand the origin of this moderate binding, we analyzed the electronic structure of the reaction sites before and after the intermediates adsorb, together with the bonding and charge transfer between the sites and the intermediates (Figure 6). Before the reaction, the Mn atoms in FeCoMn–NC and Mn–NC have nearly the same occupied d-band center, and both are lower than that of the bonded metals in FeCo–NC (Figure 6a and Table S10). The d-band center therefore cannot explain why the two Mn atoms bind the intermediates differently. In contrast, the axial Mn–OH bond in FeCoMn–NC is much weaker than the axial Mn=O bond in Mn–NC, with negative integrated crystal orbital Hamilton population (−ICOHP) values of 2.64 and 8.03 eV (Figure 6b). The Mn atom in FeCoMn–NC also has a much larger local magnetic moment (Figure 6c). Its spin-up and spin-down 3d states are strongly unbalanced, whereas those of Mn in Mn–NC are nearly balanced, with almost all 3d electrons paired. The difference between the Mn atoms in FeCoMn–NC and Mn–NC therefore lies in the axial ligand adsorbed from the electrolyte before the reaction, and this ligand is set by the FeCo particles (Table S7).

### 5.6 图 6 第二段（吸附后、几何机理、电荷、火山图）
After the intermediates adsorb, the metal 3d states overlap with the O 2p states of the intermediates below the Fermi level in each catalyst, forming metal–O bonds (Figure 6d, Figures S27 and S28). The Mn–O bonds formed with OOH* and OH* are stronger in FeCoMn–NC than in Mn–NC, as shown by their larger −ICOHP values (Figure 6e, Figure S29 and Table S10). In Mn–NC, the strong axial Mn=O double bond (Figure 6b) takes up most of the bonding capacity of Mn, which also pairs nearly all of its 3d electrons (Figure 6c), so Mn binds the intermediates on the opposite side weakly. The much weaker axial Mn–OH bond in FeCoMn–NC leaves more bonding capacity for the intermediates. Mn in FeCoMn–NC therefore holds OOH* more firmly, which makes OOH* formation easier than on Mn–NC, where this step limits the ORR. At the same time, the axial OH prevents Mn from binding the ORR intermediates too strongly. Without the axial OH, Mn shifts 0.46 Å out of the N₄ plane toward adsorbed OH*. OH* therefore binds so strongly that its removal limits the ORR at 0.52 V (Table S11). By contrast, the axial OH pulls Mn 0.44 Å out of the N₄ plane toward the axial OH. An ORR intermediate adsorbing on the opposite side then draws Mn back toward the N₄ plane (Figure S30a). Drawing Mn back consumes part of the binding energy. Relative to Mn without the axial OH, OH* adsorption weakens by 0.34 eV, of which 0.24 eV arises from the structural deformation and 0.10 eV from the weaker electronic interaction between Mn and OH* (Figure S30b and Table S11). Upon adsorption, electrons move from the catalyst to the intermediates, and the amount transferred reflects how strongly they interact. Both the electrons lost by the bonded metals (Figure 6f) and those gained by the intermediates (Figure 6g and Figure S31) increase from Mn–NC to FeCoMn–NC to FeCo–NC. FeCoMn–NC thus binds the intermediates moderately. This moderate binding places FeCoMn–NC near the apex of the activity volcano (Figure 6h), where OOH* formation and OH* removal are relatively balanced. Because ΔG_(OOH*) − ΔG_(OH*) is nearly constant for the three catalysts (Table S8), the limiting potential can be approximated as a function of ΔG_(OH*) alone,^(4,23,24) which gives the volcano in Figure 6h.^(5,25) The construction of this volcano is described in Section 2.8 of the Supporting Information. Figure 6i summarizes the mechanism. At the ORR working potential and pH 13, O* and OH from the electrolyte adsorb on the FeCo particles and on the neighboring Mn, respectively, with the OH bound axially. The FeCo particles keep this axial OH on Mn, and the axial OH pulls Mn out of the N₄ plane, so that Mn binds the intermediates neither too strongly nor too weakly. The ORR proceeds on this Mn single atom.

### 5.7 关键事实（如需数字，只能用这些）
- 半波电位 0.885 V vs RHE，优于 Pt/C、FeCo–NC、Mn–NC；238 h 后保持 96.5% 初始电流（结论中不写测试电压）。
- 0.78 V vs RHE、pH 13 下：FeCoMn–NC 为 8O*（颗粒）+ Mn 上轴向 OH；Mn–NC 为 Mn=O；FeCo–NC 为 8O*。
- 有颗粒时 Mn–OH 变为 Mn=O 的电位是 0.96 V，去掉颗粒是 0.48 V（同一设置对比）。
- 极限电位：FeCoMn–NC 0.78 V，FeCo–NC 0.34 V，Mn–NC 0.26 V；去掉轴向 OH 的 FeCoMn–NC 0.52 V（OH* 脱附受限）。
- Mn–NC：Mn=O 键很强（−ICOHP 8.03 eV，Mn–OH 为 2.64 eV），占掉 Mn 大部分成键能力，3d 电子几乎全配对，对侧 OOH* 结合过弱，OOH* 生成受限。
- 轴向 OH 把 Mn 拉出 N4 平面约 0.44 Å，对侧吸附中间体把 Mn 拉回平面；拉回消耗部分结合能，使 OH* 吸附减弱 0.34 eV（结构 0.24 + 电子 0.10）。
- FeCo–NC：颗粒结合 O* 过强，O* 转化为 OH* 受限。

## 6. Claude 的草稿（供参考）

In summary, we prepared an FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. FeCoMn–NC reaches an ORR half-wave potential of 0.885 V versus RHE, higher than those of Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h. Surface coverage calculations under working conditions show that O*-covered FeCo particles keep an axial OH on the adjacent Mn single atoms at the ORR potential, whereas Mn single atoms without particles are oxidized to Mn=O. The axial ligand determines how strongly Mn binds the ORR intermediates. In Mn–NC, the strong Mn=O bond makes Mn bind OOH* too weakly, and without an axial ligand, Mn binds OH* too strongly. In FeCoMn–NC, the weaker Mn–OH bond leaves Mn enough bonding capacity for OOH*, and the shift of Mn toward the axial OH weakens OH* binding, so that FeCoMn–NC lies near the apex of the activity volcano. This work shows that metal particles can tune adjacent single atoms by setting their axial ligand under working conditions, which offers a way to design catalysts that combine particles and single atoms.

## 7. 10 篇同领域高水平论文结论的写法（Claude 从 Zotero 原文读取后归纳）

论文：Wan 2022 Nat. Commun.；Zhao 2025 Nat. Catal.；Zhang 2025 JACS；Li 2018 Nat. Catal.；Zitolo 2015 Nat. Mater.；Jiang 2016 JACS；Huang 2022 Angew.；Wang 2019 JACS；Xu 2023；Luo 2019 Nature。

共同模式：
1. 开头一句交代制备了什么，多数以 In summary 开头。
2. 性能只给一两个关键数字。例如 Jiang 2016 只给 E1/2 和比 Pt/C 高多少；机理部分几乎不出现计算数值。
3. 机理用因果链，并做对比。Zhao 2025 最典型：分别描述吸附适中、过强、偏弱的三类 Fe 位点，再用一句话收束，大意是过强和过弱的吸附都阻碍 ORR。
4. 最后一句写意义：加深了对某类活性位点的理解，或方法可推广到其他体系；不对读者提要求。
5. 长度一般 5–8 句。

## 8. 必须注意的文献：Wan 2022 Nat. Commun.（正文 ref 11）

Wan 等人（Nat. Commun. 2022, 13, 2963）用 DFT 提出 Fe 团簇使相邻 Fe–N4 结合一个永久的轴向 OH 配体，该 OH 优化了另一侧对 ORR 中间体的结合。因此“颗粒或团簇诱导单原子轴向 OH”本身不是本文首创。本文的区别在于：
1. 用工作电位和 pH 下的表面覆盖计算确定配体，颗粒把 Mn–OH 变为 Mn=O 的电位从 0.48 V 推到 0.96 V；
2. 解释了轴向配体为何使结合适中：Mn=O 与 Mn–OH 对成键能力的不同占用，以及轴向 OH 使 Mn 出平面、吸附时被拉回的几何效应；
3. 体系是 FeCo 合金颗粒加 Mn 单原子，颗粒本身被 O* 覆盖。
结论应突出这些区别，不写 first。
