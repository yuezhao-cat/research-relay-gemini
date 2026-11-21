# FeCoMn-T025 取干净表面 ORR 能量（目录已指明）

日期 2026-11-17 下达人 Claude 状态 待办
取代 T020 的第二部分（干净表面问题）。T020 的 Levich 部分仍然有效，另行回复。

## 背景

T017 扫了两台机器 2431 个计算目录，干净表面的 ORR 中间体在清单里是存在的，
但 T017 只取了覆盖态那几个目录的能量，manifest 里没有干净表面的任何一行。
本任务只做一件事：把下面这些**已有**目录的能量读出来并换算。

**不要提交任何新作业，不要修改或删除远程文件。**

## 要读的目录

全部在 IMR Tohoku，根目录 `/home/05926/zhaoyue/WORK/FeCoMn_ch5_recalc_20261007/`

### A 组 干净背景
- `FeCoMnNC59_clean`
- `FeCoNC59_clean`
- `MnNC_clean`

### B 组 FeCoMn–NC 干净表面、Mn 位、无轴向 OH
- `FCM_Mn_OOH`
- `FCM_Mn_O`
- `FCM_Mn_OH`

### C 组 FeCoMn–NC 干净表面、Mn 位、有轴向 OH
- `FCM_Mn_OHb`（这一组的背景）
- `FCM_Mn_OOH_OHb`
- `FCM_Mn_O_OHb`
- `FCM_Mn_OH_OHb`

### D 组 Mn–NC 干净表面
- `MnNC_OOH`
- `MnNC_O`
- `MnNC_OH`

如果某个目录下有 run1/run2/cont 之类的续算子目录，取最后一个正常结束且离子收敛的。

## 要做的事

1. 每个目录读 OUTCAR 最后的 `energy(sigma->0)`，同时记录 normal termination、
   离子收敛、CONTCAR 原子数与元素组成。

2. 按 SI 2.5–2.7 节的口径算 ΔG(OOH*)、ΔG(O*)、ΔG(OH*) 和四步 ΔG，再算 UL 和 η = 1.23 − UL。
   气相参考和零点加熵校正用 SI 的那组：`G(H2) = −6.833 eV`、`G(H2O) = −14.327 eV`，
   校正 `O +0.066`、`OH +0.343`、`OOH +0.403 eV`。每个模型以它自己的背景为参照。

3. 组成必须对得上才算。B 组相对 A 组的 `FeCoMnNC59_clean`，C 组相对 `FCM_Mn_OHb`，
   D 组相对 `MnNC_clean`。如果原子数或元素组成对不上，**不要换算，直接报告对不上**，
   并给出两边的组成。T017 在 `FCM_cov8O_OOH` 上就是这么处理的，做法正确，这次照做。

4. FeCo–NC 的干净表面 ORR 中间体（FCN 的 OOH/O/OH，无覆盖）在 T017 的全量清单里没有。
   请再确认一次：**存在还是不存在，给一句明确答复。**存在就给路径，不存在就直说，不要替代。

## 报告里要有的三张表

| 模型 | 背景能量 | E(OOH*) | E(O*) | E(OH*) | ΔG(OOH*) | ΔG(O*) | ΔG(OH*) | ΔG1–ΔG4 | 最大一步 | UL | η |

一张给 B 组，一张给 C 组，一张给 D 组。

另外用一句话回答：B 组和 C 组的 UL 差多少（这是轴向 OH 在干净背景下的贡献），
C 组和现有覆盖态主结果（UL = 0.776 V）差多少（这是覆盖度的贡献）。

## 不要做的事

- 不要跑新作业
- 不要用覆盖态的数去补干净表面的空缺
- 不要把结论写成"与实验不符"之类的判断，只给数；解读由 Claude 和赵月做
- 不改 Word、不改图

## 交付

`FeCoMn/from_agent/FeCoMn-T025/REPORT.md`，附 manifest CSV（机器、完整路径、
energy_sigma0、收敛字段、CONTCAR 组成）。
