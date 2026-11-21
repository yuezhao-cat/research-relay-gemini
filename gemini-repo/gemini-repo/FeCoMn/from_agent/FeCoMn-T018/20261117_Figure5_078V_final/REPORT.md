# FeCoMn-T018：Figure 5，0.78 V 定稿交付

## 必须使用的正文插图

`Figure_5_078V_白痕清理_高清.png` 是用户最后明确指定的文件。直接从原路径复制，SHA256 完全相同，不重画、不缩放、不重新导出。4200 × 4305 px，600 dpi，原生宽度177.8 mm。

`Figure_5_078V_final_preview.png` 是同版预览。

## SVG 源文件

- `Figure_5_078V_final_editable.svg`：原矢量源整理，文字保留 Arial，曲线、标记、图框、图例均为可编辑矢量；结构球棍图沿用嵌入图像。不是把整张 PNG 封进 SVG。
- `Figure_5_078V_final_Arial_paths.svg`：使用 Arial/Arial Italic/Arial Bold 的实际字体文件转路径，不含 text/tspan。
- 这两份是对应矢量源的交付。浏览器、SVG 渲染器与既有 PNG 的抗锯齿和字形采样可有差异，不能声称逐像素相同。正文必须使用用户指定 PNG，不能擅自改用 SVG 渲染结果。
- 整理时曾发现旧源把橘色、深红色曲线画成实线，已按定稿恢复点虚线和虚线。该中间实线版不交付。

## 已定的内容

- a–f 的代表性工作点为0.78 V vs RHE，d–f 的星号在pH13；相图纵轴依旧 V vs SHE。
- a–c 的候选数说明删除；图内吸附物靠近对应代表线并用对应颜色；图例文字同色；样品名与纵轴、分图字母保留已确认对齐。
- d–f 样品名浅灰底；g 为 FeCoMn–NC (8O* + Mn–OH*)。
- h 为0.78 V，0.52 eV标签避线，三个结构图距台阶间距统一；0.004 eV采用与其他两处统一样式的竖直指示箭头。注释箭头不作为按比例量取能量差的标尺。
- h 三样品最大上坡显示0.004、0.44、0.52 eV；完整数值见 Figure5h_078V_energies.csv。

## 可追溯与检查

- `source_078V.svg`为前次0.78 V矢量源快照，`build_vector.py`整理可编辑SVG，`outline_text.py`转路径。
- `H_legend_atom.png`沿用确认PNG中的H图例原子局部。原子结构图本身仍为原有图像，不声称它们是可编辑的原子模型。
- `CHECKS.json`记录PNG同字节核验、SVG字体/路径/引用检查和数值。`SHA256SUMS.json`记录文件校验值。
- 原始 DFT 吸附能、结构、热修正与限制电位未修改。本次不改任何Word/SI。

## Claude交接

见上一级 `CLAUDE_REPLACE_FIGURE5.md`。当前基稿正文 `FeCoMn_Manuscript_revised_20261116_2240.docx`，SI `FeCoMn_SI_revised_20261116_2250.docx`。按用户授权只替换正文图5，统一对应代表性电压及直接受影响的图5h能量表述，其余内容保持原样，存新版本。
