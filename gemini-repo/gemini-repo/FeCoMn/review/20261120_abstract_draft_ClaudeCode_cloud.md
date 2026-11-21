# 摘要草稿（Claude Code 云端，2026-11-20）

依据：四方对齐的兜底主线（91e3176 / 本人 §22、§24）——正文不写"颗粒推后过氧化 0.48 V"；颗粒作用只作观察陈述；主线 = 工作电位下 Mn 带轴向 OH，把吸附调到适中。

## 英文

Metal particles are very common in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet the catalytic activity is usually attributed to the metal single atoms alone. Here, we prepare an FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches an oxygen reduction reaction (ORR) half-wave potential of 0.885 V versus RHE, higher than those of commercial Pt/C, FeCo–NC, and Mn–NC. Operando infrared spectroscopy shows that the species at the catalyst surface change with potential, so we calculated the surface coverage under working conditions. At 0.78 V, the FeCo particles are covered by O*, and the Mn single atoms in FeCoMn–NC carry an axial OH, whereas those in particle-free Mn–NC carry an axial O. Without an axial ligand, Mn binds the ORR intermediates too strongly, so the removal of OH* limits the reaction. An axial O weakens the binding so much that OOH* formation becomes difficult. The axial OH lies between these two cases: it weakens the binding mainly because the Mn site must distort more when an intermediate adsorbs, so that at 0.78 V OOH* formation is nearly thermoneutral and OH* removal is downhill. In FeCo–NC, the particles bind O* too strongly, which hinders the conversion of O* to OH*. FeCoMn–NC therefore binds the ORR intermediates moderately and lies near the apex of the activity volcano, which explains its highest measured activity.

## 中文直译

热解得到的金属–氮–碳（M–N–C）催化剂中金属颗粒非常常见，但催化活性通常只归因于金属单原子。本文制备了 FeCo 合金颗粒与 Mn 单原子共存的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的 ORR 半波电位达到 0.885 V vs RHE，高于商业 Pt/C、FeCo–NC 和 Mn–NC。原位红外光谱显示催化剂表面物种随电位变化，因此我们计算了工作条件下的表面覆盖。在 0.78 V 下，FeCo 颗粒被 O* 覆盖，FeCoMn–NC 中的 Mn 单原子带轴向 OH，而无颗粒的 Mn–NC 中 Mn 带轴向 O。没有轴向配体时，Mn 对 ORR 中间体吸附过强，OH* 脱除限速；轴向 O 把吸附削弱过多，OOH* 难以生成。轴向 OH 介于两者之间：它削弱吸附主要是因为中间体吸附时 Mn 位点需要更大的畸变，使 0.78 V 下 OOH* 生成接近热中性、OH* 脱除下坡。在 FeCo–NC 中，颗粒对 O* 吸附过强，阻碍 O* 向 OH* 转化。因此 FeCoMn–NC 对 ORR 中间体吸附适中，位于活性火山顶附近，解释了其最高的实测活性。

## 每句依据
| 句 | 依据 |
|---|---|
| 0.885 V，高于 Pt/C、FeCo–NC、Mn–NC | 正文第 99–101 行、图 3 |
| 原位红外表面物种随电位变化 | 图 4（定稿版，E(SCE)+1.016 V） |
| 0.78 V：颗粒 8O*，FCM Mn–OH，Mn–NC Mn=O | 覆盖计算，表 S5、图 5（基于所采用的 Mn=O 电子态，SI 分支表） |
| 无配体过强、OH* 脱除限速 | 同一 8O* 模型裸 Mn，U_L 0.52 V |
| 轴向 O 过弱、OOH* 难生成 | Mn–NC Mn=O，U_L 0.26 V，OOH* 生成上坡 |
| OH 削弱主要来自畸变代价 | T041：冻结几何相互作用几乎不变（OH* +0.10、OOH* −0.10 eV），额外畸变 OH* +0.24、OOH* +0.43 eV |
| OOH* 近热中性、OH* 下坡 | 表 S7，U_L 0.78 V |
| FeCo–NC O* 过强 | 原摘要，图 5/6 |
| 火山顶 | 图 6h |

## 与现稿相比的改动
1. 删去"FeCo particles determine the axial ligand…"末句：T038b 显示颗粒不改变裸 Mn 电子结构，且 FCM/Mn–NC 配体差异依赖 Mn=O 电子态分支，"determine"超出数据。颗粒只保留观察陈述（"the Mn single atoms in FeCoMn–NC carry an axial OH, whereas those in particle-free Mn–NC carry an axial O"）。
2. 把"适中"讲成三档：无配体（过强）→ OH（适中）→ O（过弱），并点出 OH 削弱的来源（畸变代价，T041）。
3. 现稿"Mn–OH allows Mn to bind OOH* strongly enough"改为从"削弱过强吸附"角度叙述，与图 6 段主线一致。

## 标题需同步
现标题"…Reveals That FeCo Particles Determine the Axial Ligand of Mn Single Atoms…"与上面第 1 点冲突。建议候选：
- Surface Coverage under Working Conditions Shows That an Axial OH Moderates the Binding of Mn Single Atoms Next to FeCo Particles for Oxygen Reduction
- Working-Condition Surface Coverage Reveals an Axial OH That Tunes Mn Single Atoms beside FeCo Particles for Oxygen Reduction
