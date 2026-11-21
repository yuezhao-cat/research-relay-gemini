# FeCoMn-T044 第 1 项：图 6i 示意图更新（Claude Code 本地，2026-11-21）

执行：Claude Code 本地（Codex 无额度替补）。复核：Antigravity（待）。未改 Word。

## 交付文件（Fig6_T044_final/）
- `Figure6_T044_600dpi.png`：600 dpi，4200 × 4228 px，与 v38 尺寸相同
- `Figure6_T044_editable.svg`（文字可编辑）、`Figure6_T044_Arial_paths.svg`（文字转路径）、`Figure6_T044.pdf`
- `preview_6i_T044.png` 与 `preview_6i_v38.png`：6i 改前改后对照截图
- `pixel_diff_vs_v38.txt`：像素差记录

## 6i 改了什么
1. Mn 从 N4 平面向轴向 OH 一侧抬起（示意位移 DZ = 0.22 个图内单位，为看清有夸大，不代表真实比例）；OH 和 O–H 键随 Mn 一起上移，Mn–N4–OH 标签同步上移。
2. Mn 在平面内的原位置画虚线圆，表示 Mn 被拉回平面后的位置。
3. Mn 右侧加向下箭头（深灰 0.3，与 ORR 循环箭头同色同线宽），表示 Mn 向平面方向的位移。
4. 下方连到 ORR 循环的虚线保留，表示中间体在 OH 的另一侧吸附。
5. FeCo 颗粒表面 O*、颗粒标签、ORR 循环、原子图例、字号、配色均不变；图中不标数字。

## a–h 不变的核对
- 方法：以 Codex 本地工作区的 v38 脚本 `build_t034_v38_axial_parentheses.py` 为底本。先原样复现，复现 PNG 与仓库 v38 定稿 `FeCoMn-T034/draft_20261118_v38_axial_parentheses/Figure6_T034_600dpi.png` 逐像素比较为 0 差，再在此基础上只替换原始 v6 脚本中画 Mn、OH、标签的 4 行，以及 v38 补画 O–H 键的 1 行。
- 结果：与 v38 相比变化 13773 像素，全部位于 x 3715–4049、y 3060–3297（6i 内 Mn 位点附近）；6i 单元格以外（a–h）变化像素 **0**。
- 脚本自检：文字重叠 0 处；出界 4 处，与 v38 相同（v38 原有）。

## 脚本与数据来源
- `build_t044.py`：本任务出图脚本（由 v38 脚本改路径并加 6i 替换）。
- `build_v38_repro.py`：v38 原样复现脚本（用于 0 差验证）。
- 原始示意图代码：`D:/OneDrive/Desktop/知识库/papers/FeCoMn/ACS_Catalysis_第三轮投稿/ACS_投稿拼图_Claude重绘_20261027/Figure_6_三样品OOH_OH_20261103/v6_工作版/fig6_v6_20261103.py`（第 248–261 行）。
- a–h 数据沿用 v38：`FeCoMn-T034/data/`、`FeCoMn-T033/draft_20261118_v1/data/`，以及原始 v6 脚本读取的本地计算目录；本任务未改任何数据。
- `Fig6_T044_final/data/`：脚本运行时重新导出的面板 CSV，与 v38 相同来源。

## 请 Antigravity 复核
1. 打开 `preview_6i_T044.png` 和 `preview_6i_v38.png` 对照，确认 6i 内容符合任务单第 1 节。
2. 用 `pixel_diff_vs_v38.txt` 的方法独立比较两张 600 dpi PNG，确认 a–h 为 0 差。
3. 结论写入 `review/`。
