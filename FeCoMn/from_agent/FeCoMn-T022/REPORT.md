# FeCoMn-T022 交付

底图为 T021 可编辑 SVG：`FeCoMn/from_agent/FeCoMn-T021/Figure_5_T021_20261117_1750_editable.svg`（SHA256：`bfc0b5bdbbccf3c8e2ddc3e4cf297327b8c8f1b1edddc0f2e443a4ce3657f300`）。

仅修改图 5h：

- 删除红、橙、紫三支箭头的 SVG 对象 `patch_46`、`patch_44`、`patch_45`。
- 删除 T021 图例左侧独立的三组 η 标注 `t021_eta_1` 至 `t021_eta_3`。
- 原图例的色线、样品名和字号沿用；三行整体左移以腾出位置。样品名后加逗号，并紧跟彩色的 `η = 0.45 V`、`η = 0.89 V`、`η = 0.97 V`。η 用 Arial 斜体，数字和单位用 Arial 正体。

未改 a–g、h 能级横线、虚线连接、结构图圆圈、坐标轴、台阶位置及范围。XML 比对确认 `axes_1` 至 `axes_14` 与 T021 底图逐字节一致。图中未加入 1.23 V。

交付：`Figure_5_T022_20261117_1740_600dpi.png`（4200 × 4308 px，600 dpi）、可编辑 SVG、Arial 转路径 SVG、生成脚本 `build_t022.py`；转路径 SVG 无 `text`/`tspan` 残留。PNG 由 T022 矢量源导出，浏览器的抗锯齿可能与 T018 用户确认的旧 PNG 有细微差异。

供 Claude：待赵月确认后替换正文 Figure 5，并将图注末句改为 `η is the theoretical overpotential.`；本任务没有修改 Word。
