# 摘要机理部分修改（Claude web 2，22:40）

基础：赵月 22:30 认为最满意的版本。只改机理部分和末句，其余不动。

## 为什么原机理句不行
1. 方向反了。原句说“较弱的 Mn–OH 键让 dz² 靠近费米能级，所以 Mn 对 OOH* 吸附足够强”，意思是轴向 OH 帮 Mn 抓得更牢。但同一 8O* FeCoMn–NC 的计算显示，不带轴向 OH 时 Mn 抓得太牢（U_L 0.52 V，OH* 脱附受限），带上轴向 OH 后结合变弱才到 0.78 V（T032）。轴向 OH 的作用是削弱，不是加强。
2. dz² 不是原因。T041 拆分显示，OH* 结合减弱 0.34 eV 中 0.24 eV 来自形变，冻结几何下的电子结合几乎不变。OOH* 的减弱完全来自形变（形变 0.43 eV 大于总减弱 0.27 eV）。dz² 位置只是成键方式的描述，不能写成“所以”。
3. “weak axial Mn–OH bond” 没有参照物，读者会问比什么弱。

## 修改
位置：摘要机理部分。前一句：At 0.78 V, the FeCo particles are covered by O*, and the adjacent Mn single atoms carry an axial OH.

原文：The ORR intermediates bind to these Mn single atoms opposite the axial OH. The weak axial Mn–OH bond keeps the Mn dz² states close to the Fermi level, so Mn binds OOH* strongly enough for OOH* to form, and the subsequent steps up to OH* removal are all downhill.
直译：ORR 中间体吸附在这些 Mn 单原子上轴向 OH 的对侧。较弱的轴向 Mn–OH 键使 Mn 的 dz² 态保持在靠近费米能级的位置，因此 Mn 对 OOH* 的吸附足够强，OOH* 能够生成，而之后直到 OH* 脱附的各步都是下坡的。

修改：The ORR intermediates bind to these Mn single atoms opposite the axial OH. 「Without the axial OH, Mn binds the intermediates too strongly, and OH* removal is uphill at 0.78 V. The axial OH pulls Mn out of the N4 plane toward itself, so each intermediate must pull Mn back into the plane as it binds. This costs energy and weakens the binding of the intermediates. As a result, OOH* formation is nearly thermoneutral at 0.78 V, and」 the subsequent steps up to OH* removal are all downhill.
直译：ORR 中间体吸附在这些 Mn 单原子上轴向 OH 的对侧。「没有轴向 OH 时，Mn 对中间体结合太强，0.78 V 下 OH* 脱附是上坡的。轴向 OH 把 Mn 从 N4 平面拉向自己一侧，因此每个中间体结合时都必须把 Mn 拉回平面。这需要消耗能量，削弱了中间体的结合。结果是，在 0.78 V 下 OOH* 生成接近热中性，」之后直到 OH* 脱附的各步都是下坡的。

每句依据
- 无 OH 太强、OH* 脱附上坡：T032，8O* FeCoMn–NC 无轴向 OH，ΔG(OH*) 0.51 eV，0.78 V 下 OH* 脱附 +0.27 eV，U_L 0.52 V。
- 拉出平面再拉回：T042，Mn 被 OH 拉出 0.44 Å，吸附后回到平面（0.00–0.10 Å）。
- 形变削弱结合：T041（OH* 0.24/0.34 eV，OOH* 0.43 eV 大于总减弱 0.27 eV）。
- OOH* 近热中性、其余下坡：T032 带 OH，0.78 V 下 OOH* 生成 +0.01 eV，OH* 脱附 −0.07 eV。

## 末句
最后一句与前一句“吸附适中”重复。T039 已经算完，但因电子态不可比，不能用来写颗粒的因果作用（见 GPT-12、[CW2-15]）。建议现在直接删去最后一句，摘要停在 “...which explains its highest measured activity.”。若以后有颗粒因果的证据，再加一句正面回答。

## 修改后摘要全文
Metal particles are very common in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet the catalytic activity is usually attributed to the metal single atoms alone. How the particles affect the catalytic activity therefore remains unclear. Here, we prepare a new FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. FeCoMn–NC reaches an oxygen reduction reaction (ORR) half-wave potential of 0.885 V versus RHE. Operando infrared spectroscopy shows that the species adsorbed on the catalyst surface change with potential, so the ORR takes place on a covered surface rather than a bare one. We therefore calculated the surface coverage at different potentials. At 0.78 V, the FeCo particles are covered by O*, and the adjacent Mn single atoms carry an axial OH. The ORR intermediates bind to these Mn single atoms opposite the axial OH. Without the axial OH, Mn binds the intermediates too strongly, and OH* removal is uphill at 0.78 V. The axial OH pulls Mn out of the N4 plane toward itself, so each intermediate must pull Mn back into the plane as it binds. This costs energy and weakens the binding of the intermediates. As a result, OOH* formation is nearly thermoneutral at 0.78 V, and the subsequent steps up to OH* removal are all downhill. FeCoMn–NC therefore binds the ORR intermediates moderately and lies near the apex of the activity volcano, which explains its highest measured activity.

---

## 22:35 补：摘要怎样回答“颗粒怎么影响”

现有数据能回答到什么程度，取决于赵月对低能分支的决定（13:36 决定不考虑）。

### 方案一（与“不考虑低能分支”的决定一致，能正面回答）
按统一的原采用分支（Mn 初始磁矩均为 +3），T039 就是颗粒作用的直接对照：载体几何不变，去掉颗粒，Mn–OH → Mn=O 的转变电位从 0.96 V 降到 0.49 V。同样的初始磁矩下，无颗粒时 Mn=O 猝灭为闭壳层的正常双键，有颗粒时不猝灭、键更长。在火山图那句之后加：

「Removing the FeCo particles while keeping the support structure fixed lowers the potential at which Mn–OH is oxidized to Mn=O from 0.96 to 0.49 V. The FeCo particles thus keep the adjacent Mn single atoms in the Mn–OH state at the working potential, whereas in particle-free Mn–NC the Mn single atoms are oxidized to Mn=O and bind OOH* too weakly.」

直译：「在保持载体结构不变的情况下去掉 FeCo 颗粒，Mn–OH 被氧化为 Mn=O 的电位从 0.96 V 降到 0.49 V。因此，FeCo 颗粒使相邻 Mn 单原子在工作电位下保持 Mn–OH 状态，而在不含颗粒的 Mn–NC 中，Mn 单原子被氧化为 Mn=O，对 OOH* 结合太弱。」

前提：0.96 V 按 T039 同一算式从 FCM 能量直接重算确认；SI 中给出两分支对照表（Antigravity 已补），如实披露。风险：审稿人对有颗粒的 Mn=O 换初始磁矩重算会得到低 0.45 eV 的态，GPT 和 Claude Code 据此认为 T039 有电子态混杂。

### 方案二（不用 T039，只陈述结果）
「In particle-free Mn–NC, the Mn single atoms are instead oxidized to Mn=O at 0.78 V and bind OOH* too weakly. The FeCo particles thus keep the adjacent Mn single atoms in the Mn–OH state that binds the ORR intermediates moderately.」

直译：「而在不含颗粒的 Mn–NC 中，Mn 单原子在 0.78 V 下被氧化为 Mn=O，对 OOH* 结合太弱。因此，FeCo 颗粒使相邻 Mn 单原子保持在对 ORR 中间体结合适中的 Mn–OH 状态。」

这是两种材料覆盖度计算的直接结果，不依赖 T039，但只说明“有颗粒和没颗粒时 Mn 戴的配体不同”，没有排除载体几何的影响。

### 我的判断
如果坚持不考虑低能分支，方案一在逻辑上是自洽的，并且真正回答了开头的问题，我建议用方案一，同时在 SI 如实给出两分支对照。如果担心审稿风险，至少用方案二，否则开头提的问题在摘要里没有答案。
