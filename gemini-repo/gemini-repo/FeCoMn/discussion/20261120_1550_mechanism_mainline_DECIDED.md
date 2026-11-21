# 机理主线（已定）与图 6 段草稿

发起：Claude web，2026-11-20 15:50。四方 13:41–13:46 的版本已收敛到这条线。**后续所有分析、计算、写作都只服务于这条线，不再开新线。**

## 已定决定（不再讨论）
- 低能分支不考虑（赵月 13:36）：沿用原采用分支；P0、M3、自旋扫描都不做。
- 不再提新问题、不再追加新计算（赵月 13:39）。在跑的 T039、T040、T041 只用于确认或调整措辞；结果不理想就改写法，不加计算。
- 颗粒"为什么"让 OH 更稳定：不追，正文只写结果。
- Mn–NC+OH 假设态不作论据。

## 主线
1. 工作态：0.78 V 下 FeCo 颗粒被 8O* 覆盖，Mn 带轴向 OH；Mn–NC 带轴向 O（图 5）。已证。
2. 颗粒决定 Mn 带 OH：颗粒不改变裸 Mn（T038/T038b）；OH 比 O 稳 0.18 eV（表 S10）。只写结果，等 T039 确认。T039 不翻转则改为"FeCoMn–NC 中 Mn 带 OH"，不归因颗粒。
3. 轴向 OH 把过强吸附调到适中：同一 8O* FeCoMn–NC，无 OH U_L 0.52 V（OH* 脱附受限）→ 有 OH 0.78 V；OH* +0.33、OOH* +0.21 eV（T032）。已证，全文核心。
4. 原因（几何）：轴向 OH 把 Mn 拉出 N4 平面 0.44 Å；中间体在对侧吸附时 Mn 回到平面，形变耗能。OH* 减弱 0.34 eV 中 0.24 eV 来自形变、0.10 eV 来自电子结合（Antigravity，Genkai 现有静态）。待 Claude Code 复核；OOH* 等 T041。
   成键方式（只作描述）：中间体经 Mn dz² 成键；带 OH 时 Mn 保持高自旋，费米能级**下方**出现**单占** dz²↑ 态，OOH* 与之配对形成 Mn–O 单键（磁矩 −0.82 μB）。待 Antigravity 复核 Claude Code 数据。
5. 吸附适中、近火山顶点、活性最高（图 5h、火山图）。已证。
6. 验证：Mn–NC 的 Mn=O 双键使自旋猝灭、dz² 降至 −5.12 eV，OOH* 太弱，U_L 0.26 V（与 T032 静态 0.24 V 待核对）。

## 不再使用的说法
- "OH 成键弱，所以留下强吸附"（方向反了）。
- "OH 把 dz² 推上去、留下空 dz² 轨道"（实际是单占态，且 dz² 中心下移）。
- "Mn=O 的 π 走 dz²"（π 用 dxz/dyz）。
- "OH 移走费米能级附近 dz² 态"（读数漏指数，已纠正）。
- "颗粒与 OH 缺一不可""颗粒在带 OH 时还调吸附"（依据已撤回）。
- 用 Mn–O 键长 1.655 vs 1.577 Å 说明颗粒作用（取决于自旋分支）。

## 图 6 段草稿（面板编号待图 6 v3）
To understand why the Mn single atoms in FeCoMn–NC bind the ORR intermediates moderately, we compared the same 8O*-covered FeCoMn–NC model with and without the axial OH. Without the axial OH, the Mn single atom binds the intermediates too strongly. OH* removal is the limiting step, and the limiting potential is only 0.52 V [Table SX]. With the axial OH, OH* and OOH* bind more weakly by 0.33 and 0.21 eV, respectively, and the limiting potential rises to 0.78 V. The axial OH pulls the Mn single atom 0.44 Å out of the N4 plane [Figure 6a]. When an intermediate adsorbs on the opposite side, the Mn single atom returns to the N4 plane, and this deformation costs energy. For OH*, the deformation accounts for 0.24 eV of the 0.34 eV weakening, and the change in electronic binding accounts for the remaining 0.10 eV [Figure 6b, Table SX]. The intermediates bond to the Mn single atom through its dz² orbital. With the axial OH, Mn retains a high spin state, and a singly occupied spin-up dz² state appears just below the Fermi level [Figure 6c]. OOH* pairs with this state to form a Mn–O single bond, which lowers the Mn magnetic moment by 0.82 μB [Figure 6d, e]. The axial OH therefore weakens the binding of the intermediates without making it too weak, and FeCoMn–NC lies near the apex of the activity volcano [Figure 6f]. In Mn–NC, by contrast, the Mn single atoms carry an axial O. The Mn=O double bond quenches the Mn spin and lowers the dz² states to −5.12 eV, so OOH* binds too weakly and the limiting potential is only 0.26 V [Figure 6g].

直译：为了理解 FeCoMn–NC 中的 Mn 单原子为什么对 ORR 中间体吸附适中，我们比较了同一个 8O* 覆盖的 FeCoMn–NC 模型在有和没有轴向 OH 时的情况。没有轴向 OH 时，Mn 单原子对中间体的吸附太强，OH* 脱附是限制步，极限电位只有 0.52 V。有轴向 OH 时，OH* 和 OOH* 的吸附分别减弱 0.33 和 0.21 eV，极限电位升到 0.78 V。轴向 OH 把 Mn 单原子从 N4 平面拉出 0.44 Å。中间体在另一侧吸附时，Mn 单原子回到 N4 平面，这一形变需要付出能量。对 OH* 而言，0.34 eV 的减弱中，0.24 eV 来自形变，其余 0.10 eV 来自电子结合的变化。中间体通过 Mn 单原子的 dz² 轨道成键。有轴向 OH 时，Mn 保持高自旋态，费米能级下方出现一个单占的自旋向上 dz² 态。OOH* 与这个态配对形成 Mn–O 单键，使 Mn 磁矩降低 0.82 μB。因此，轴向 OH 减弱了中间体的吸附，又不会使其过弱，FeCoMn–NC 位于活性火山图顶点附近。相比之下，Mn–NC 中的 Mn 单原子带轴向 O。Mn=O 双键使 Mn 的自旋猝灭，并把 dz² 态压低到 −5.12 eV，因此 OOH* 吸附太弱，极限电位只有 0.26 V。

建议图 6 v3 面板顺序：a 几何（Mn 离面）、b 能量拆分、c–e 成键（dz² 自旋 PDOS、OOH* 配对）、f 火山图、g Mn–NC 验证。

## 各方当前任务
- Claude Code：T040 LOBSTER（618088）；复核 OH* 拆分；T041 结果核查。
- Antigravity：T039（617431/617433）、T041（Genkai 7633024）；复核 Claude Code 的磁矩与 dz² 态密度数据。
- GPT / Claude web 2：审阅图 6 段草稿的语言与证据边界，只提措辞和准确性意见，不提新机理。
回复写到 FeCoMn/review/20261120_Fig6_draft_<名字>.md。
