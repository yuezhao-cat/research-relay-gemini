# FeCoMn-T022 图 5h 删箭头，η 并入图例

日期 2026-11-17 下达人 Claude 状态 待办

底图用 T021 的交付件 `FeCoMn/from_agent/FeCoMn-T021/Figure_5_T021_20261117_1750_editable.svg`。

## 背景

T021 把 0.004/0.44/0.52 eV 换成了 η 标注，但箭头是 T018 画底图时就有的，
三个箭头里只有橙（Mn–NC）和蓝（FeCo–NC）是按真实落差画的，
红（FeCoMn–NC）那一步真实落差不到 0.01 eV，箭头却画了约 0.5 eV 长，
读者会把三条里唯一一条几乎全程下坡的路径读成有半个 eV 的上坡。

落差本来就由能级高度画出来了，箭头不必再表示大小，因此全部删掉。

## 要做的事

只改 5h，a–g 一律不动。

1. 删掉 h 里的三个箭头（红、橙、蓝），连同箭头相关的全部图形对象。
   能级横线、虚线连接、结构图圆圈、坐标轴、台阶位置一律不动。

2. 删掉 T021 加的那个独立 η 标注块（图例左侧那三行带色的 η = … V）。

3. 把 η 并进图例，每条曲线的样品名后面直接跟 η，同一行：

   | 图例行 |
   |---|
   | FeCoMn–NC, η = 0.45 V |
   | FeCo–NC, η = 0.89 V |
   | Mn–NC, η = 0.97 V |

   η 用 Arial 斜体，数值和单位 Arial 正体，其余文字沿用图例原有字体字号。
   图例位置和框线沿用现状，行宽变长可适当左移，不要压到能级线或结构图圆圈。

4. 图里不要出现 1.23 V，不要改坐标轴范围。

## 交付

- 600 dpi PNG
- 可编辑 SVG
- Arial 文字转路径 SVG
- 生成程序
- REPORT.md 写明删了哪些对象、改了哪些文字、哪些没动

放在 `FeCoMn/from_agent/FeCoMn-T022/`。

## 对应正文改动（Claude 负责）

图 5 图注末句由
`Arrows mark the largest uphill step of each pathway, and η is the theoretical overpotential.`
改为
`η is the theoretical overpotential.`
