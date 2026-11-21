# T033 出图前结构与数据核查

2026-11-18。**暂不出图**。按任务“对不上先报告”执行，仅核查，无新计算、无改图/Word。

## 已通过：背景结构及轴向键身份

将原优化CONTCAR与电子结构POSCAR逐元素、逐坐标比较，采用周期最短位移：

| 材料 | 原优化工作背景 | 静态输入 | 最大逐原子差 / Å |
|---|---|---|---:|
| FeCoMn–NC | IMR `FeCoMn_ch5_recalc_20261007/rich8O_joint_20261014/FCM_8O_MnOH/CONTCAR` | Genkai `FeCoMn_MnOH_electronic_v2_20261031/FCMnew_base_full/POSCAR` | 3.63×10⁻¹⁵ |
| Mn–NC | IMR `FeCoMn_ch5_recalc_20261007/MnNC_O_MnNbri/CONTCAR` | Genkai `FeCoMn_electronic_20261023/MnNC_base_full/POSCAR` | 4.34×10⁻¹⁵ |

两组各自组成、元素顺序、晶胞一致。各自COHP专用静态POSCAR也对应同一原优化CONTCAR，误差相同。这里是几何对应通过，不等于磁态一致通过。

反应侧OOH*/O*/OH*也逐态核对了两材料原优化CONTCAR与PDOS/Bader静态POSCAR，六对元素顺序与晶胞均一致，最大逐原子差为3.63～4.34×10⁻¹⁵ Å。见 `../FeCoMn-T032/reaction_geometry_matches.json`。此结论同样不能消除主样品O*的已知静态磁态差异。

MnNC O bri最终结构：O180最近的原子是Mn179，距离1.577085 Å；四个N175–178距离2.80156、2.80273、2.81234、2.81239 Å；最近C约3.40035 Å。O位于Mn–N4平面之外，Mn出平面约0.50628 Å。**最终是轴向Mn–O，不是仍连接Mn/N或C的桥位；原目录名不能当最终几何标签。**

## 已通过：LOBSTER基组与谱设置的对应

主样品：Genkai `FeCoMn_MnOH_postprocess_corrected_20261031/cohp/FCMnew_base_full/lobsterin`。

MnNC：IMR `FeCoMn_COHP_20261023/MnNC_base_full/lobster_post_v2_20261024/lobsterin`。

两者均 `basisSet pbeVaspFit2015`、Mn `3p 3d 4s`、O `2s 2p`、C/N `2s 2p`、`COHPstartEnergy -15`、`COHPendEnergy 10`、`gaussianSmearingWidth 0.1`。主样品额外Fe/Co/H基组对应其实际组成，不是Mn/O投影口径不同。负pCOHP比较应使用未各自归一化的自旋求和总键曲线。

LOBSTER两者正常结束，绝对charge spilling主样品1.39%/2.57%，MnNC为1.04%/1.04%。两者均存在band-overlap正交化警告，不能声称输出完全无警告；如解释细小谱差，还需检查bandOverlaps，不以spilling单项代替全部投影质量验收。

## 未通过：跨面板同一电子态，以及路径/精确值问题

详见 `../../review/Fig6_Antigravity_data_check_Codex_20261118.md`：

1. 主样品Bader远程路径错误，应为 `FeCoMn_MnOH_postprocess_20261031/bader/...`，不是不存在的 `postprocess_corrected_20261031/bader/...`。
2. εd引用表实际−3.41629853/−3.44202181 eV，清单所列精确小数有微小出入；−3.42/−3.44显示值不变。
3. MnNC背景的COHP来源Mn磁矩+0.001 μB，Bader/PDOS来源+0.287 μB。几何相同，但a的8.03278与b的0.287不能被称为同一电子态输出。
4. 主样品反应O*现行COHP来源静态Mn +0.374 μB；已找到原优化波函数延续的现有静态Mn +2.085 μB、体系139.6017 μB、εd=−3.385513 eV。路径Genkai `FeCoMn_MnOH_O_magnetic_wavecheck_20261031/`，来源文件明确记载原优化WAVECAR，不需补算。但现成COHP并非自动变成该延续分支；需查该分支已有LOBSTER投影是否存在，不能只替换标签。T032保留两者区分。

## 当前处置

T033停在出图前核查，不生成草图、不改SI。数据数值多数可复现，但“几何、原子和基组正确”不能替代“电子态与自由能来源对应”。不擅自更换磁态或补算。原始结构、INCAR、LOBSTER输入与警告摘录保存在 `../FeCoMn-T032/structure_basis_sources.json`；数值复读记录在 `../../review/Fig6_Codex_data/`。

机器根目录：Genkai `/home/pj25000114/ku50002299/`；IMR `/home/05926/zhaoyue/WORK/`。以上相对远程路径均相对于各自根目录。
