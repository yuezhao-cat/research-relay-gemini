# Mn–NC背景：COHP/Bader来源追溯

2026-11-18。本轮开工拉到`604e391`；沿用`38b5c49`双向核查规则。按赵月本轮要求，只查现有文件，不新跑DFT、LOBSTER或Bader，不改图/Word。原有报告不覆盖，本文件细化并修正“磁矩不一致”的含义。

## 结论

**不是取错结构，也不是无意把参数写错。** 当时为LOBSTER有意准备了独立COHP专用静态，原Bader/PDOS则来自另一套已完成静态；二者原子结构、PAW与k点一致，但不是同一份自洽输出。局域磁矩0.287/0.001的差异真实存在，尚不能将其单独判为两种物理自旋态或认定某个参数导致错误。

**已找到原来采用的两条来源链，尚未找到一套同时现成包含原Bader分支COHP与Bader的输出。** 若要求一套电子密度统一全部量，COHP专用静态的DOS与Bader原始密度文件已经齐全，可以只做后处理而不重跑DFT；但那不是直接复用原11.507781 e与0.287 μB，不能静默替换。

## 1. 永久记忆与当时准备脚本

本轮查了共享永久记忆的索引和直接相关记录，包括：

- `D:/AI-Shared-Memory/project_fecomn_paper_electronic_20261024.md`：记载独立COHP静态及投影任务、Bader验证，以及旧COHP曲线导出错列后停用并重出v2的经过。
- `project_fecomn_manuscript_latest_20261031.md`：Bader/CDD原始电荷验证与O*波函数追溯，区分后处理数值核查通过与磁态同源。
- `project_fecomn_si_tables_captions_20261104.md`：采用结构轴向距离与Mn出平面核查，不是桥连O。

关键本地原脚本：

`D:/_pf/ch5_electronic_20261023/prepare_cohp_inputs.py`

脚本复制原POSCAR/POTCAR/KPOINTS和INCAR，**明确将ISYM设为−1，并按基组数向上取120的倍数设置NBANDS**，还调用了当时两个输入检查程序。MnNC基组函数数为174×4+4×4+9+4=725，NBANDS设置为840。此设计与现有IMR输入完全对应，并非现阶段臆测调整理由。

不能把不同用途任务中的这种主动调整本身称为“低级错误”。当前需核对的是两个独立自洽结果能否作为一套电子态解释，不是否定当时已做过的输入/后处理检查。

## 2. 完整来源链和数值

| 阶段 | 原采用几何优化 | 原PDOS/Bader静态 | COHP专用静态 |
|---|---|---|---|
| 机器 | IMR | Genkai | IMR |
| 相对根目录 | `FeCoMn_ch5_recalc_20261007/MnNC_O_MnNbri` | `FeCoMn_electronic_20261023/MnNC_base_full` | `FeCoMn_COHP_20261023/MnNC_base_full` |
| sigma→0能量/eV | −1667.74239034 | −1667.77945980 | −1667.77216576 |
| 体系磁矩/μB | +0.0128 | +0.4680 | −0.0004 |
| Mn179局域磁矩/μB | 未打印，不能从总磁矩推算 | +0.287 | +0.001 |
| NBANDS，OUTCAR实际 | 462 | 460 | 840 |
| ISYM，INCAR | 原优化设置 | 0 | −1 |
| 正常结束/EDIFF | 是/是 | 是/是 | 是/是 |
| 同窗口占据d中心/eV | 不从无轨道投影的优化输出强算 | −3.442021813 | **−3.542064771** |
| 已有Bader Mn电子数/e | 未找到配套ACF | **11.507781** | 未找到配套ACF |
| 已有轴向COHP | 未找到配套投影 | 未找到配套投影 | **−ICOHP=8.03278 eV** |

根目录：Genkai `/home/pj25000114/ku50002299/`；IMR `/home/05926/zhaoyue/WORK/`。DOS中心均从原始DOSCAR对Mn179五个d轨道、自旋求和，EF为零，−8到0 eV同窗口积分，不是从图读数。计算过程在上级 `trace_MnNC_sources.py`，元数据在本目录 `genkai_provenance.json`、`imr_provenance.json`。

### 不要混入未完成的IMR电子结构任务

IMR `FeCoMn_electronic_20261023/MnNC_base_full`是未完成的早期任务，CONTCAR和WAVECAR为空，没有正常结束；其OUTCAR中间能量不作为结果。Genkai同名任务`7158551`的`migration.json`记录从IMR迁移并保留原目录，输入哈希可核对。不能因两个目录同名就把IMR中间输出当成另一个已收敛分支。

COHP专用任务是IMR `497505.cmspbs1`，投影输出在其下`lobster_post_v2_20261024`；该投影目录的OUTCAR/WAVECAR映射到专用静态父目录，不是另一份独立VASP计算。

## 3. 确认相同和不同的项目

原PDOS/Bader与COHP静态的POSCAR、POTCAR、KPOINTS逐字节SHA256分别一致：

- POSCAR：`b01683e4a7529462e678c30f3dadb0bc48f7f50a0171734ac448895c393f41d3`
- POTCAR：`aa97bffe0ebf269afcf4d641832e2a3686e4885722aed9e10fc73b7812e2a5ae`
- KPOINTS：`eb5458194ab7121b0491b77381659e7dfe887a47d2aa6dde49eb1a55c7a01036`

与原优化CONTCAR逐原子比较已通过；Mn179–O180为1.577085 Å。ENCUT500、PREC Accurate、EDIFF1e−6、ISPIN2、ISMEAR0、SIGMA0.05、IVDW12、LREAL False、LORBIT11、NEDOS2000、MAGMOM初始`174*0 4*0 1*3 1*0.5`以及ISTART0/ICHARG2均相同。

输入仅见三项差异：NCORE12/8（机器并行布局）、ISYM0/−1、默认NBANDS/显式840。**初始磁矩并没有被擅自换掉，也没有几何或赝势混用。** 两静态能量差0.00729404 eV，不能在未做隔离对照时全归因于ISYM、NBANDS或“磁态跳变”。局域磁矩差约0.286 μB，不能只凭该差就指定高/低自旋量子数。

原优化体系磁矩接近0，而COHP静态也接近0，只是描述事实；由于优化与静态精度设置不同、原优化未打印Mn局域磁矩，不能仅凭“哪个总磁矩更近”自动宣布哪个是唯一原磁态。

## 4. 原采用分支有没有另一份现成COHP/Bader

检索两机根目录至9层内MnNC相关ACF.dat与ICOHPLIST.lobster，结合目录名、原采用几何、局域/总磁矩、迁移记录及本地`D:/_pf/ch5_electronic_20261023`归档核对：

- 原Bader链：Genkai上述目录`bader_validated_20261024/ACF.dat`；旧`bader_20261023`格式处理结果不替代验证版。验证版盆编号179读得11.507781，全体盆电子和734.999956与NELECT735对应。
- 原COHP链：IMR上述专用静态下`lobster_post_v2_20261024/ICOHPLIST.lobster`总键Mn179–O180，两个自旋−4.01527/−4.01751 eV，合计−8.03278。
- 在本轮检索到的这些已采用背景来源中，**未找到局域Mn=0.287这份自洽输出对应的现成ICOHPLIST/COHPCAR，也未找到COHP静态0.001对应的现成Bader ACF**。不把其他组成、OH*反应态或旧模型的LOBSTER结果拿来凑。

原Bader静态460条带少于当时完整基组725个函数，不是把现有460带文件直接拷进现有840带投影目录就能声称相同基组投影完成。不能通过改文件名或换另一套更小基组规避对应要求。

这里的“原采用”有两个层级：原稿PDOS/Bader采用的是Genkai链，原稿COHP采用的是IMR专用链，二者各自是当时保留的原结果；但不存在一个已经证实统一二者的单一波函数来源。不能事后将其中一条称为“后来低能搜索”而删除，也不能假定所有独立静态应逐字相同。

## 5. 只靠现有文件能统一到什么程度

### 可立即完成，无需新计算

1. 用原始COHPCAR重新读取轴向总键曲线，见第6节与本目录新CSV；没有动旧CSV。
2. 原PDOS/Bader链的电荷、DOS和磁矩内部统一，继续保留原值并注明来源。
3. COHP专用链内部也有DOSCAR、OUTCAR、WAVECAR和完整电荷文件，已能从该DOSCAR读出同源εd=−3.542064771 eV和磁矩0.001，而不是挪用另一链−3.442/0.287。

### 能不跑DFT统一，但尚需后处理

COHP专用静态父目录保留CHGCAR、AECCAR0、AECCAR2，三者网格均252×240×360，文件均非空；WAVECAR与DOSCAR也在。可以用**这套现有密度重新做一次Bader后处理**，把COHP、Bader、PDOS、磁矩统一到同一静态；无需优化、无需VASP、无需磁态搜索。但新Bader数值目前未知，不能填原11.507781，也不能声称已经做完。

若坚持全部保留原Genkai PDOS/Bader自洽解，则本轮未找到可直接给出其完整基组COHP的现成输出。不能在“先不补算”的要求下承诺现有文件已经完全统一。是否将主图改用专用静态整套来源，须由赵月决定，而不是因为这条路线更方便就自动更换原数据。

本轮仅解析已有DOS与COHP表，**未运行Bader/LOBSTER或任何DFT作业**。

## 6. 永久记忆定位出的旧CSV问题

记忆`project_fecomn_paper_electronic_20261024.md`明确记载：初版`extract_cohp_curves.py`错读Average表头，旧`cohp_curves_20261024`停用，后改`export_cohp_curves_v2.py`；base态在v2批量导出默认跳过，所以后来仍能找到一个名字像正确总键的旧base CSV。

Antigravity当前引用：

I:`FeCoMn_COHP_20261023/cohp_curves_20261024/MnNC_base_full__Mn179-O180.csv`

本轮逐点复读确认：原COHPCAR有501行，旧CSV只有500行，漏掉第0行；在共有能量点，两自旋曲线与原始总键最大绝对偏差**8.31707**，不是小数舍入误差，不能使用。

原COHPCAR元数据声明38个列组、2自旋；包含Average列组0，完整Mn179→O180总键为列组1。对应零起始数组索引为pCOHP列3/79、积分列4/80；不要按ICOHPLIST里的键编号直接推曲线列，更不要取轨道分项当总键。

已只从现有原始文件提取完整501点，另存本目录：

`MnNC_axial_COHP_raw_verified_20261118.csv`

含能量、自旋1/2原pCOHP、自旋求和后−pCOHP、原始累计积分。EF恰为0的网格积分合计8.06724 eV，ICOHPLIST原积分8.03278 eV；二者相差0.03446 eV（约0.43%），沿用当时“网格累计积分与原积分值分开”的口径，图内标签应以原ICOHPLIST为准，不从有限窗口曲线重积分伪造8.03。

**这说明当前复用时引用到了当时已经停用的旧导出文件，不是当时没有检查出该问题。** 正确原始LOBSTER输出保留完整，修正只需提取，不需要补算。

## 7. 对前一轮措辞的修正

前一轮说“跨面板电子态来源未统一”作为文件来源判断仍成立；但若理解为“已证明不同磁态分支、当时设置错误或全部原数据不可用”，则超出了证据。本轮纠正为：**有意独立准备的两套静态，输出不同，差异的单一物理原因尚未隔离；原数据各自有有效来源，当前不能冒称同一套波函数。**

图和Word继续不动。T033是否可恢复应在数据来源口径确定并经Antigravity独立复读后由赵月决定，不能凭本次重新提取曲线就自动宣称Bader也已统一。
