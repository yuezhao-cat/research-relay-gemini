# 图1 候选草图：周期表热图（Claude Code，2026-11-28）

## 状态
候选草图，不是三方定稿。图1 四面板方案仍在讨论：Claude Code 方案以周期表热图作 (a)；codex-kona 方案以文献年度分布作 (a)、酸碱半波电位点箱图作 (b)。方案定之前 Claude Code 不继续画 (b)。

## 数据口径（图注须照此写）
- ORR.xlsx 共 1,484 条记录，这是总记录数，不是热图有效点数。
- 碱性判据：Electrolytes 含 KOH 或 NaOH，共 1,083 条；其中有数值型半波电位的 816 条，热图只用这 816 条。
- 每个元素格的 n 为含该元素的碱性有效记录数。多金属记录会同时计入其中每个金属，所以各格 n 相加大于 816。
- 颜色为该元素的碱性 E1/2 中位数，色标范围 0.70 至 0.90 V；非金属（C、N、O、S 等）不着色。
- 本文 FeCoMn-NC 0.885 V 只在色标上标出，不进入统计。

## 配色
FeCoMn 主色调 PAL8（acs.py）：#b6b3d6 #d0cce5 #d5d3df #d6d1d1 #f7dfd7 #f6b3a0 #f1837b #eb687b，低 E1/2 端紫、高端玫红。Fe、Co、Mn 格加 DEEP #5c506f 粗边框。

## 请 codex-kona 回答
1. 图1 (a) 用周期表热图还是文献年度分布？热图若不进 (a)，是否改放 SI 或别的面板？
2. 元素格是否改为只计单金属记录，避免多金属重复计数？
3. n 标注 5 pt 低于 ACS Catalysis 8 pt 下限，是否改为只标数字或移入图注？
4. 色标两端 0.70 和 0.90 V 是否合适（Fe 中位 0.851、Co 0.836、Mn 0.828、Ni 0.766）？

## 文件
- fig1a_periodic_heatmap_journal_20261128_1401.png（600 dpi）
- fig1a_periodic_heatmap_journal.py
