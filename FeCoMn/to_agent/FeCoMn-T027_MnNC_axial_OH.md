# FeCoMn-T027 Mn–NC 加轴向 OH 的 ORR 自由能

日期 2026-11-17 下达人 Claude 状态 待办
只读取已有计算，**不提交新作业，不修改远程文件，不改图不改 Word。**

## 目的

填一张 2×2 表的最后一格：

| | 有轴向 OH | 无轴向 OH |
|---|---|---|
| 有颗粒（FeCoMn–NC，8O*） | 0.776 V | 0.515 V |
| 无颗粒（Mn–NC） | **本任务** | 0.583 V（T025 D 组） |

## 要读的目录

IMR，根目录 `/home/05926/zhaoyue/WORK/FeCoMn_ch5_recalc_20261007/`

- 背景：`MnNC_OH`（Mn–N4 加一个轴向 OH）
- OOH*：`MnNC_OOH_OHb`
- O*：`MnNC_O_OH`
- OH*：`MnNC_OH_OH`

T017 报告末尾提到"MnNC 轴向-OH 旧路径曾得到 UL≈0.570 V"，请说明那条旧路径
是否就是上面这四个目录；如果不是，给出旧路径的位置，但**以上面四个目录为准**。

## 要做的

1. 每个目录读最后的 `energy(sigma->0)`，确认正常结束、离子收敛，报 CONTCAR 实际组成。
2. 核对组成：三态相对背景只多 O2H / O / OH；中间体与轴向 OH 分别在 Mn 的两侧
   （按坐标确认，不按目录名推断）。任何一项不符就报告不符，不要换算。
3. 核对 INCAR 关键设置与 T025 D 组一致（ENCUT、泛函、D3、ISPIN、ISMEAR/SIGMA、EDIFF、EDIFFG）。
4. 按 SI 口径算 ΔG(OOH*)、ΔG(O*)、ΔG(OH*)、四步 ΔG、UL、η，表格式同 T025。
5. 写明限制步。

## 交付

`FeCoMn/from_agent/FeCoMn-T027/REPORT.md`，附 manifest CSV。
只给数和核对结果，不做解读。
