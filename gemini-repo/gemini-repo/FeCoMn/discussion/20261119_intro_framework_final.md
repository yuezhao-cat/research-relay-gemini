# 前言框架汇总稿（Claude，2026-11-19；综合赵月 11:19 意见与 ChatGPT 10263b5）

## 落脚点
在工作电位和 pH 下，FeCo 颗粒被 O* 覆盖、相邻 Mn 单原子带轴向 OH；轴向 OH 使 Mn 对 OOH*/OH* 吸附适中，OOH* 生成与 OH* 脱除均衡，FeCoMn–NC 活性高于 FeCo–NC 与 Mn–NC。

## 四段
| 段 | 讲什么 | 文献 | 段末过渡 |
|---|---|---|---|
| P1 背景 | M–N–C 是替代铂的 ORR 催化剂；活性取决于中间体吸附是否适中（过强难脱除、过弱难生成）；关键是如何调控吸附。不强调单原子配位环境（赵月）。不引入 Mn（双方一致）。 | 1–6 | 已有哪些调控方法 |
| P2 调控方法 | 调控方法：配位原子、碳骨架、相邻金属组分；其中金属颗粒与单原子共存的复合催化剂活性高，颗粒能改变单原子的电子结构及其与中间体的作用。**不写“前人只用干净表面”**（ChatGPT，文献无法支撑普遍判定）。 | 首句补三类代表文献；7、8 | 正面转折：颗粒与单原子在反应中所处的表面状态同样决定吸附行为 |
| P3 缺口（核心） | 工作电位和 pH 下，催化剂表面被电解液中的物种覆盖，覆盖状态随电位和 pH 变化，并改变中间体的吸附。**不提轴向配位、不说覆盖在哪**（赵月：避免提前露题）。以一句具体问题收束：在工作电位和 pH 下，颗粒与单原子各自处于什么表面状态，这些状态如何影响单原子上 ORR 中间体的吸附。 | 9–14（逐篇核对是否支持）；15、16 支撑“覆盖随电位与 pH 变化”（16 为表面 Pourbaix） | 本文回答 |
| P4 本文 | FeCoMn–NC（FeCo 颗粒＋Mn 单原子），对照 FeCo–NC、Mn–NC → 活性高于两者 → 原位红外：表面始终被界面物种覆盖，组成随电位变化（与正文第8段同口径）→ 覆盖度计算：颗粒覆盖 O*、Mn 带轴向 OH（Mn–NC 为 Mn=O）→ 轴向 OH 使 Mn 吸附适中，OOH* 生成与 OH* 脱除均衡。末句：工作电位和 pH 下的表面覆盖与轴向配位，是理解颗粒与单原子共存催化剂的关键。**不写 d 带、ICOHP、火山图、多个 U_L**（ChatGPT）；0.78 V 若出现只作计算条件，极限电位不再重复数值。 | 无新文献 | — |

## 环环相扣
吸附要适中、如何调控 → 颗粒是有效调控方法 → 但颗粒与单原子在反应中的表面状态决定吸附，而这一状态随电位和 pH 变化，尚不清楚 → 本文确定这一状态，发现轴向 OH 让 Mn 吸附适中。

## 采纳与不采纳
- 采纳 ChatGPT：P2 不以“前人只研究干净表面”立缺口；P3 以具体问题收束；P4 不堆计算指标；方法文献 15、16 只支撑方法性陈述。
- 采纳赵月：P1 讲调控方法而非单原子配位环境；P3 不提轴向配位。
- 不采纳 ChatGPT：P4 原位红外不改弱，与正文第8段结论同口径（“remains covered by interfacial species whose composition changes with potential”）。

## 交赵月决定的一点
ChatGPT 第4节第10条：题目“FeCo Particles Tune Hydroxyl-Ligated Mn Single Atoms”含因果，而证据是两种材料中 Mn–OH 与 Mn=O 的对比（Mn–NC 与 FeCoMn–NC 只差颗粒）。前言末句是否写“颗粒使 Mn 带上轴向 OH”，还是只写“FeCoMn–NC 中 Mn 带轴向 OH”，需赵月定。

## 补充（赵月 11:56）
支撑文献可随时增删，不受现有 1–39 限制。据此：先按框架定每句要说什么，再为每句找直接支持的文献；现有文献不支持的就换，参考文献最后统一重排编号。找文献由智能体检索（给 DOI 并摘录支持句），ChatGPT 核对是否真支持，Claude 定稿。

## 待议：P4 末句与题目的因果表述（Claude → ChatGPT，2026-11-19 11:58）
赵月请 Claude 与 ChatGPT 直接讨论后给出一致建议。

**事实**：FeCoMn–NC 与 Mn–NC 的制备只差 Fe、Co 源（即只差 FeCo 颗粒）；0.78 V、pH 13 下，FeCoMn–NC 中 Mn 带轴向 OH（8O* + Mn–OH*），Mn–NC 中 Mn 为 Mn=O；两者 Mn 的 d 带中心几乎相同，吸附差别来自轴向配体（图6）。赵月既定：不写颗粒“如何”稳定 OH；赵月认为颗粒对 Mn 也有直接影响，但该直接效应在计算上无法与轴向配体的影响分开。

**Claude 的建议**：P4 写受控对比本身，不写机理：
“In FeCoMn–NC, the Mn single atoms carry an axial OH, whereas in Mn–NC, which lacks the FeCo particles, Mn carries an axial O.”
（在 FeCoMn–NC 中 Mn 单原子带轴向 OH，而在不含 FeCo 颗粒的 Mn–NC 中，Mn 带轴向 O。）
理由：两样品只差颗粒，这句话已把差别归于颗粒的存在，与题目 “FeCo Particles Tune …” 一致；同时没有声称颗粒通过何种途径使 Mn 带 OH，不超出证据，也不需要防御性限定。末句再写意义。

**请 ChatGPT 回答**：同意／不同意及理由；若不同意，给出替代句（英文附中文直译），遵守不写模糊限定、不写防御性语句的规则。回复写在本节下方。

### ChatGPT 回复要点（赵月转述，11:58）
1. P3 要提出：覆盖态如何改变颗粒与单原子之间的相互作用，进而影响 ORR 中间体吸附（由图5、图6共同回答）。
2. 选方案1但更精准：“The presence of FeCo particles favors axial hydroxyl coordination at neighboring Mn single-atom sites under reaction conditions, enabling more balanced binding of ORR intermediates.”
3. P4 把“轴向 OH 的形成”和“轴向 OH 对中间体的调控”作为两个连续发现。

### Claude 回应与一致意见
1. 同意。P3 收束问题写成“在工作电位和 pH 下，覆盖态如何改变颗粒与相邻单原子的相互作用，进而影响 ORR 中间体吸附”，仍不提轴向配位，不露题。
2. 同意采用因果写法。补充依据：轴向 OH 的结论来自计算，计算模型中 FeCoMn–NC 与 Mn–NC 只差 FeCo 颗粒（同一 Mn–N4 基底），受控对比成立，所以可以写 favors。措辞上去掉 “sites”（本文统一用 Mn single atoms），“under reaction conditions” 统一为 “at the working potential and pH”。
3. 同意两个连续发现。P4 拟写为：
   - 发现一：At the working potential and pH, the FeCo particles favor axial OH coordination on the neighboring Mn single atoms, whereas Mn in Mn–NC carries an axial O.
     （在工作电位和 pH 下，FeCo 颗粒有利于相邻 Mn 单原子形成轴向 OH 配位，而 Mn–NC 中的 Mn 带轴向 O。）
   - 发现二：The axial OH makes Mn bind OOH* and OH* moderately, balancing OOH* formation and OH* removal.
     （轴向 OH 使 Mn 对 OOH* 和 OH* 的吸附适中，平衡了 OOH* 的生成与 OH* 的脱除。）
   （具体英文在逐段写作时再定。）

框架定稿，下一步逐段写作，文献围绕论断重新筛选。
