# FeCoMn-T026 补齐 B 组，并给出 Mn 轴向配体随覆盖度的序列

日期 2026-11-17 下达人 Claude 状态 待办
承接 T025。仍然只读取已有计算，**不提交新作业，不修改远程文件，不改图不改 Word。**

---

## 第一部分：B 组换背景后补算

T025 里 B 组算不出来，是我的任务单写死了背景目录造成的，不是你的问题。
你找到的 `S_FeCoMnNC59_clean`（C174N4Fe27Co32Mn，正常结束、离子收敛）
与 B 组三态除吸附质外逐元素匹配，**现在正式授权用它作为 B 组背景。**

B 组三态（仍在 `FeCoMn_ch5_recalc_20261007/` 下）：
`FCM_Mn_OOH`、`FCM_Mn_O`、`FCM_Mn_OH`

要做的：

1. 换算前先核对三件事，任何一项不符就报告不符、不要硬算：
   - 三态组成相对背景只多 O2H / O / OH
   - 三态与背景的 INCAR 关键设置一致（ENCUT、泛函、D3、ISPIN、ISMEAR/SIGMA、EDIFF、EDIFFG、固定原子数）
   - 三态与背景的晶胞一致
2. 按 SI 口径算 ΔG(OOH*)、ΔG(O*)、ΔG(OH*)、四步 ΔG、UL、η，格式与 T025 的表一致。
3. 给出 **B 与 C 的 UL 差值**，一句话。这是轴向 OH 在干净颗粒背景下的贡献。
4. 同时给出 **B 与 D 的 UL 差值**。B 是 FeCoMn–NC 的裸 Mn–N4，D 是 Mn–NC 的裸 Mn–N4，
   两者 Mn 位化学环境接近，这个差值说明在干净模型下两个样品还能不能区分开。

另外报告 B 组四步里哪一步最大（限制步），和 D 组一样要写明。

---

## 第二部分：Mn 轴向配体随颗粒 O 覆盖度的序列

目的：回答为什么只有 FeCoMn–NC 的 Mn 轴向挂 OH，而 Mn–NC 挂 O。

对每一个颗粒 O 覆盖数，比较 Mn 轴向挂 OH 和挂 O 两种构型的自由能，
给出 ΔG(Mn–OH) − ΔG(Mn–O)。目录都在 `FeCoMn_ch5_recalc_20261007/` 下：

| 颗粒 O 覆盖 | Mn–O 构型 | Mn–OH 构型 |
|---|---|---|
| 0 | `FCM_Mn_O` | `FCM_Mn_OHb` |
| 2 | `coverage_6O7O_20261014/FCM_Mn2O` | `coverage_6O7O_20261014/FCM_Mn2OH` |
| 4 | `coverage_6O7O_20261014/FCM_4O_MnO` | `coverage_6O7O_20261014/FCM_4O_MnOH` |
| 5 | `coverage_final_20261011/FCM_5O_MnO` | `coverage_final_20261011/FCM_5O_MnOH` |
| 6 | `coverage_6O7O_20261014/FCM_6O_MnO` | `coverage_6O7O_20261014/FCM_6O_MnOH` |
| 8 | `rich8O_joint_20261014/FCM_8O_MnO` | `rich8O_joint_20261014/FCM_8O_MnOH` |

对照（Mn–NC，没有颗粒）：`MnNC_O` 对 `MnNC_OH`

注意：`FCM_Mn2O`/`FCM_Mn2OH` 这两个名字里的 2 是不是指颗粒上 2 个 O，
请按 CONTCAR 的实际组成确认，不要按名字推断。每一行都要报出两个构型的实际组成。

要做的：

1. 每对构型读最后的 `energy(sigma->0)`，确认正常结束和离子收敛。
2. 同一覆盖数下，Mn–OH 与 Mn–O 两个构型组成应当只差一个 H。差别不是一个 H 就报告不符，不要换算。
3. 在 0.78 V vs RHE、pH 13 下按 SI 的计算氢电极口径，给出
   G(Mn–OH) − G(Mn–O)，负值表示 Mn–OH 更稳定。
4. 用一句话回答：**这个差值在哪个颗粒 O 覆盖数上由正变负（或由负变正）。**
   如果全程不变号，就直说不变号。

---

## 交付

`FeCoMn/from_agent/FeCoMn-T026/REPORT.md`，附 manifest CSV
（机器、完整路径、energy_sigma0、收敛字段、CONTCAR 实际组成、晶胞）。

只给数和组成核对结果。不要写"与实验相符"或"与实验不符"之类的判断，解读由 Claude 和赵月做。
