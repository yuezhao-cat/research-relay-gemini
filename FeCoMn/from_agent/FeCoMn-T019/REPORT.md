# FeCoMn-T019 交付（2026-11-17）

## 请 Claude 替换

- 正文 Figure 3：`Figure_3_20261117_1650_600dpi.png`。对应可编辑源文件和 Arial 文字转路径文件均在本目录。
- SI Figure S10：`Figure_S10_20261117_1650_600dpi.png`。S10 现为单图，图注应去掉 `(a)`；原 S10b 的 LSV 已放入 Figure 3h。
- 此处只交图，未修改 Word 或图注。图 S7 未动。

## 本版内容

- Figure 3 a–f 的数据、曲线、配色、图框未改。按赵月后续要求，分图字母与对应 y 轴标题调整到同一竖线。
- g 占左侧两格；保留 238 h 原曲线、96.5% 终点和阴影；移除放大插图。按后续要求纵轴改为 0–135%，粉色带加宽，标出 FeCoMn–NC，测试条件移到右下角。
- h 占右侧一格，沿用 S10b 的 31.6 h 测试前后 LSV 和半波点；图例为 Before / After。按赵月最终要求删除 ΔE₁/₂ 数值标注。
- 图 3 外部宽度等比例设为 177.8 mm。PNG 为 4200 × 3824 px、600 dpi。S10 PNG 为 2666 × 1208 px、600 dpi。
- 两份转路径 SVG 已检查：无 `<text>` 或 `<tspan>` 残留；使用系统 Arial 字形。

## 数据来源与限制

- a–f 底图：本机 `outputs/图3_ef交换_20261114/Figure_3_e标号对齐_Arial_可编辑.svg`。
- g 数据：本机 `outputs/图3_稳定性改版_20261113/Figure3g_沿用数据.csv`；复用同目录 `figure3_equal.py` 的绘图设置。
- h 与 S10 源图：本机 `outputs/图S10_仅31.6h_20261114/Figure_S10_仅31.6h_Arial_可编辑.svg`；SHA256 见 `h_source_sha256.txt`。
- 因分图字母及 y 轴标题对齐、g 纵轴/飘带和 h 标注均按后续用户要求变化，a–f 与旧版“逐像素一致”、g “只删插图”的任务单原句已被后续要求取代。没有重新计算 h 的 LSV。

生成程序：`Figure_3_20261117_1650_source.py`；Arial 转路径与 600 dpi 打包程序在本机 `work/package_t019.py`。
