# Antigravity面板a、b数据清单复核

2026-11-18。核对 `Fig6_Antigravity.md`（a5a80c1）及原始文件，仅只读，无新计算、无改图/Word。

**结论：主要数值可复现；文件路径有一处错误，εd所报精确值有小出入，跨面板电子态来源不一致尚未解决，不能无条件标“全部通过”。**

## 1. 可复现的数值

| 项目 | 主样品Mn238 | Mn–NC Mn179 | 原始依据 |
|---|---:|---:|---|
| 轴向键长 / Å | 1.87724 | 1.57708 | 轴向ICOHPLIST总键行，且CONTCAR距离复核一致 |
| 轴向−ICOHP / eV | 2.64030 | 8.03278 | −(−0.74016−1.90014)；−(−4.01527−4.01751) |
| Bader电子数 / e | 11.457649 | 11.507781 | ACF.dat；MnNC本地验证JSON也一致 |
| 按ZVAL=13换算净电荷 / e | +1.542351 | +1.492219 | 13减Bader电子数，不是形式氧化态 |
| 主静态Mn局域磁矩 / μB | +3.206 | +0.287 | 各自PDOS/Bader主静态OUTCAR |

主样品本地 `电子结构后处理核查_20261031/fig6_data/ICOHPLIST_base.lobster` 第26号总键确为Mn238–O247；MnNC IMR第1号总键确为Mn179–O180。不能把含轨道下标的分项再次加到总键上。MnNC导出CSV路径存在，列为 `energy_eV,cohp_spin1,cohp_spin2`；画−pCOHP需将两个自旋求和后取负号。

## 2. 必须更正的路径

清单给主样品Bader的Genkai路径：

`/home/pj25000114/ku50002299/FeCoMn_MnOH_postprocess_corrected_20261031/bader/FCMnew_base_full/ACF.dat`

**该路径不存在。正确路径是：**

`/home/pj25000114/ku50002299/FeCoMn_MnOH_postprocess_20261031/bader/FCMnew_base_full/ACF.dat`

`corrected_20261031`适用于此处的COHP/修正PDOS来源，不能机械加到Bader路径。MnNC完整原始Bader路径为Genkai：

`/home/pj25000114/ku50002299/FeCoMn_electronic_20261023/MnNC_base_full/bader_validated_20261024/ACF.dat`

清单给出的本地 `D:/_pf/ch5_electronic_20261023/bader_results_v3/genkai.json` 存在，`name=MnNC_base_full`、`atoms.index=179`的电子数确为11.507781，验证标记为true。

## 3. εd精确值不符合清单引用的那张表

实际读取清单引用的：

`D:/OneDrive/Desktop/知识库/papers/FeCoMn/ACS_Catalysis_第三轮投稿/单图汇总_journal_20261025/92_电子结构统一原参考态_20261029/atom_resolved_occupied_d_centers.csv`

| 行选择 | 表内实际值 / eV | 清单所写 / eV |
|---|---:|---:|
| FCM, base, Mn238 | −3.416298530970028 | −3.416341 |
| MnNC, base, Mn179 | −3.442021812954855 | −3.442146 |

差分别约0.000042和0.000124 eV，不影响−3.42/−3.44的图上显示，但“精确值”需按实际来源修正，或另列真正产生该数的文件。

## 4. 路径齐不等于跨面板同源

MnNC背景PDOS/Bader来源静态为：

`/home/pj25000114/ku50002299/FeCoMn_electronic_20261023/MnNC_base_full/OUTCAR`

Mn局域磁矩+0.287 μB，energy(sigma->0)=−1667.77945980 eV。

轴向COHP来源静态为：

`/home/05926/zhaoyue/WORK/FeCoMn_COHP_20261023/MnNC_base_full/lobster_post_v2_20261024/OUTCAR`

Mn局域磁矩+0.001 μB，energy(sigma->0)=−1667.77216576 eV。组成C174N4MnO、Mn–O距离相同，电子态输出却不同。Antigravity已经在磁矩单元格括号中列出这个差异，但总体“通过”仍应限定：数值来源已找到，不能声称a中的8.03与b中的0.29来自同一波函数。

主样品背景COHP与其主静态则同为Mn +3.206 μB、energy(sigma->0)=−2140.09673312 eV。

## 5. 清单附带的c面板路径

六个本地反应侧COHP CSV均存在。不过主样品O* CSV注释写 `−IpCOHP(EF)=6.501 eV`，所列ICOHPLIST值为6.45840 eV。曲线数值积分、离散EF截断与LOBSTER原始积分输出不可未经说明混称为一个“精确值”；最终标注应明确采用原始ICOHPLIST口径，曲线另核对总键列与分支。

主样品O*现有图用静态与自由能磁态不同，单凭路径存在还未解决这个问题。已找到原优化波函数延续的既有静态 `FeCoMn_MnOH_O_magnetic_wavecheck_20261031`，正在T032分别核对，不在本复核中替换数据。

## 6. 可采用的状态

- 路径清单：**需更正一处Bader路径**。
- 轴向键长、原始−ICOHP、Bader电子数：**数值复现**。
- εd：**两位小数正确，精确数值需更正来源**。
- a/b跨面板电子态一致性：**未通过同源性确认**。
- 不将−ICOHP三倍写成结合自由能三倍，不据局域磁矩直接宣称“自旋猝灭”。

远程只读采集数值见 `Fig6_Codex_data/combined.json`、`background_source_checks.json`；未改Antigravity原报告，保留独立复核记录。
