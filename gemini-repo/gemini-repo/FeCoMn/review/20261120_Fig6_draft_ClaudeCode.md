# 图 6 段草稿审阅（Claude Code，2026-11-20）

审阅对象：`20261120_1550_mechanism_mainline_current.md` 图 6 段英文草稿  

---

## 一、数值与证据准确性

| 位置 | 草稿写法 | 核查结果 | 建议 |
|---|---|---|---|
| "OH* and OOH* bind more weakly by 0.33 and 0.21 eV" | 0.33 和 0.21 eV | Antigravity 报告 +0.333 eV / +0.206 eV（T032）；Claude Code 独立核查 ΔΔE(OH*)=0.336 eV。**两处一致，0.33 和 0.21 是合理取整** | 保留 |
| "0.34 eV weakening" | 0.34 eV | 与前文 0.33 eV 不一致；实际 0.336 eV | 改为 0.33 eV |
| "0.24 eV of the 0.34 eV weakening" | 0.24/0.34 | 实际 0.236/0.336；与上一处同样不一致 | 改为 "0.24 eV of the 0.33 eV weakening" |
| "Mn retains a high spin state, and a singly occupied spin-up dz² state appears just below the Fermi level" | — | Genkai DOSCAR 实读：dz²↑ 在 EF±0.25 eV 积分 = 0.371（从几乎为零升起），dz² 中心 −3.17 eV；"just below the Fermi level"准确 | 保留；可加"in the Mn-projected PDOS"以防歧义 |
| "lowers the Mn magnetic moment by 0.82 μB" | 0.82 μB | Bader 序列：μ_Mn 从 +3.206（base+OH）降至 +2.384（+OOH*），差 −0.822 μB | 保留，可取整为 0.82 μB |
| "limiting potential is only 0.26 V" | 0.26 V（Mn–NC） | 决定文件注"与 T032 静态 0.24 V 待核对"；尚未独立确认 | 加注待核对，或改为"0.24–0.26 V" |
| "lowers the dz² states to −5.12 eV" | −5.12 eV | 来自 T037，Mn–NC + Mn=O 的 dz² 中心；已有报告数据 | 保留 |

---

## 二、逻辑完整性

**第 4 环（OH 为什么削弱吸附）的两步叙事：**

草稿将原因分成几何（0.24 eV）和电子（0.10 eV）两部分，并以 dz² 单占态说明为什么不会削弱过头。这个结构是完整的，读者可以跟住。

一处潜在逻辑缺口：草稿说"The deformation costs energy"，但没有解释**为什么轴向 OH 存在时形变代价更高**。读者会问：Mn 在有 OH 时已经被拉离平面，对侧吸附为什么还要付出更多？

建议在"The axial OH pulls the Mn single atom 0.44 Å out of the N4 plane"之后加一句：Without the axial OH, the Mn single atom sits in the N4 plane and can move freely to accommodate the intermediate. With the axial OH, Mn is displaced to one side, and adsorbing an intermediate from the other side requires Mn to move back toward the plane, which costs additional reorganization energy.（约 25 词，说明清楚）

这样读者就能理解 0.24 eV 的物理起源，不只是数字。

**Mn–NC 验证句：**

"The Mn=O double bond quenches the Mn spin and lowers the dz² states to −5.12 eV, so OOH* binds too weakly."

有一处隐含逻辑：为什么 dz² 在 −5.12 eV 就导致 OOH* 太弱？读者需要知道 dz² 要靠近费米能级才能与 OOH* 有效成键。建议加"leaving fewer unoccupied dz² states available for bonding with OOH*"，使前后对称（有 OH 时 dz²↑ 态可用，有 O 时 dz² 状态被压低、几乎全部占据）。或直接对照："whereas in FeCoMn–NC the singly occupied dz²↑ state is accessible to OOH*."

---

## 三、第 2 环的一个结构观察（待各方评估）

关于"颗粒为什么让 OH 更稳定"，现有结构数据有一个值得注意的不对称性：

- FCM_8O_MnOH：Mn–O = 1.877 Å，与无颗粒 MnNC_OH（1.879 Å）几乎完全相同（差 0.001 Å）。颗粒几乎不影响 Mn–OH 键长。
- FCM_8O_MnO：Mn–O = 1.655 Å，而无颗粒 MnNC_O_bri = 1.577 Å，键长拉长 0.078 Å；同时系统保持高总磁矩（139.8 μB），而无颗粒的 MnNC_O 自旋接近猝灭（μ_Mn = +0.287 μB）。

初步解读：颗粒（及 8O* 覆盖态）对 Mn–OH 态几乎无影响，但对 Mn=O 态有明显影响——它阻止了 Mn=O 状态下的自旋猝灭（保持高磁矩），而猝灭通常使 Mn=O 更加稳定。颗粒通过维持高自旋，使 Mn=O 比在 MnNC 上更不稳定，从而相对使 OH 更稳定。

这是一个基于已有数据的假说，不需要新计算（Mn 局域磁矩从 FCM_8O_MnO 和 MnNC_O OUTCAR 即可核实），供各方参考。如果 T039 显示去颗粒后 O 比 OH 更稳定，这个逻辑就有了间接支持。

---

## 四、草稿语言意见（次要）

1. "pairs with this state to form a Mn–O single bond" — 物理上准确（σ 配对），但对不熟悉配位化学的读者可能生疏。可考虑替换为"forms a σ-bond with the singly occupied dz² orbital"，更直接。
2. 末句"the limiting potential is only 0.26 V"与前文"0.78 V"对比已经很鲜明，不需要额外强调词。保持现有简洁度即可。

---

*Claude Code，2026-11-20*
