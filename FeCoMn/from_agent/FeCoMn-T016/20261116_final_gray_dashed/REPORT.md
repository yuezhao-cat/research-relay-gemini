# FeCoMn-T016 最终交付：灰色虚线框版

2026-11-16 用户确认：采用白底、灰色虚线外框版本，其余不动，上传 GitHub 供 Claude 插图。Word 未修改。

## 最终文件
- Figure_4_20261116_final_gray_dashed_preview.png：合并预览。
- Figure_4_20261116_final_gray_dashed_600dpi.png：600 dpi，4200 × 5032 px。
- Figure_4_20261116_final_gray_dashed_editable.svg：Arial 可编辑文字。
- Figure_4_20261116_final_gray_dashed_Arial_paths.svg：文字全部转路径。
- Figure_4c_20261116_final_gray_dashed_*：c 单独预览与两份 SVG。

## 现行版式
- 总宽 177.8 mm；a 保留定稿源图，原始数据不变。
- b 高 54 mm，三个谱图区之间 4 mm；第三段左端 1300 cm⁻¹，右端保持原值，虚线仍在 1215 cm⁻¹。仅显示范围及用户授权版式改变，谱线数据不变。
- a、b 的 ν 为希腊字母 U+03BD。
- c 高 36 mm，白底；灰色外框 #808080、0.6 pt、虚线 3/2.5 pt；左右边界 13/161 mm 与 b 外框对齐。
- c 反应箭头 1.575 pt；原子放大；OOH* 标签黑色，14 × 14 mm 正方形浅红强调框；不含 1215 注字；O/H 图例合并至右上；O2 无吸附表面。
- 用户选择的是简化机理示意图：共同 O2 起点、分两路、最终汇入 H2O；未展开碱性反应的电子/水/OH− 配平，不应将图中箭头作为配平的基元反应式。

## 核验与可追溯
- 两份 SVG 的 ID 唯一、引用完整；转路径版无 text/tspan 元素。
- 已用支持虚线和裁切的 resvg 渲染并目视核对；600 dpi PNG 为向量渲染，不是预览放大。
- source/ 保存本次确认的 a/b 向量及预览快照；它们来自 T015 定稿以及本轮用户授权的 b 调整，不含原始数据修改。
- 原始数据唯一位置：FeCoMn/data/SEIRAS_20241021_1-2/。
- generate_panel_c.py 生成 c；compose_final.py 合成两份完整 SVG、预览及 600 dpi PNG。所需 Python：matplotlib、numpy、Pillow、resvg-py。
- SHA256SUMS.json 保存本交付所有文件校验值。

本交付取代此前水分子/电位双卡、树状图、左右两框及各颜色试版。任务原文的早期版式已由用户本次连续明确修改取代。
