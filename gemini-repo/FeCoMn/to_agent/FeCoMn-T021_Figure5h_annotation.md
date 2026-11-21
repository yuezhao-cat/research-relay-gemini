# FeCoMn-T021 图 5h 标注改为过电位

日期 2026-11-17 下达人 Claude 状态 待办

## 背景

图 5h 现在是 0.78 V vs RHE 下三个催化剂的 ORR 自由能台阶图，
箭头旁标了 0.004 eV、0.44 eV、0.52 eV。

这三个数是 0.78 − 极限电位，不是任何有名字的物理量；
而且对 FeCoMn–NC，0.78 − 0.776 = 0.004 完全是凑整噪声。
改为标注理论过电位 η，和表 S7 一致。

## 要做的事

只改 5h 这一个分图的文字标注，曲线、配色、坐标轴、台阶位置、
其余分图（a–g）全部不动。

1. 删掉箭头旁的三个数值 `0.004 eV`、`0.44 eV`、`0.52 eV`。
   箭头本身保留，仍然指向每条路径上坡最大的那一步。

2. 在每条路径旁（建议放在各自曲线的图例或末端附近，位置以不压线为准）
   标出理论过电位：

   | 样品 | 标注 |
   |---|---|
   | FeCoMn–NC | η = 0.45 V |
   | FeCo–NC   | η = 0.89 V |
   | Mn–NC     | η = 0.97 V |

   η 用斜体希腊字母 eta，数值和单位正体。字号与图中其他标注一致。

3. 图里不要出现 1.23 V 字样，也不要改横轴或纵轴范围。

## 交付

- 600 dpi PNG
- 可编辑 SVG
- Arial 文字转路径 SVG
- 生成程序
- REPORT.md 写明改了什么、没改什么

放在 `FeCoMn/from_agent/FeCoMn-T021/`。

## 对应正文改动（Claude 已做，供核对）

- 图注：Arrows mark the largest uphill step of each pathway, and η is the theoretical overpotential.
- 正文：uphill by only 0.004 eV → uphill by less than 0.01 eV
- 正文保留 0.44 eV 和 0.52 eV 的描述，它们是对图上落差的文字描述，不是图上标注。
