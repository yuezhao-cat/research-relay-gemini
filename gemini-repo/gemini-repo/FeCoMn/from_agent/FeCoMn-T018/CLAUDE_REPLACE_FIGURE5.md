# 给Claude：只替换已确认的Figure 5，并同步0.78 V

用户已确认2026-11-16最终PNG，并在2026-11-17再次明确指定：
`C:/Users/46775/Documents/Codex/2026-11-13/gu/outputs/Figure5_078_remove_white_trace_20261116/Figure_5_078V_白痕清理_高清.png`。

## 图文件

请使用 [20261117_Figure5_078V_final/Figure_5_078V_白痕清理_高清.png](20261117_Figure5_078V_final/Figure_5_078V_白痕清理_高清.png) 替换正文图5。它与用户指定本地PNG同字节，详情及SHA256见同目录CHECKS.json。不要用SVG重新渲染替代确认PNG。两份SVG用于保留编辑/出版源。

## 正文和图注

以 `FeCoMn/manuscript/FeCoMn_Manuscript_revised_20261116_2240.docx` 为基稿。图4保持浅紫底无框版，不改。

- 摘要、引言、覆盖度/自由能段及Figure5图注中，指向本次代表性ORR电位的0.87 V，统一为0.78 V vs RHE。不可盲目全局替换其他实测电位。
- Figure5 a–c虚线代表0.78 V vs RHE；d–f星号为pH13下的同一工作点，纵轴为V vs SHE，不能误写成RHE。
- h为0.78 V自由能。FeCoMn–NC五态为1.800000、1.804263375、0.673081970、0.068485085、0 eV；四步依次+0.004263375、−1.131181405、−0.604596885、−0.068485085 eV。
- 当前正文仍有0.87 V下的+0.09、−1.04、−0.51、+0.02 eV，不能只改电位数字而保留旧能量。随本次电位同步更新这些直接相关的数值。OH*脱除在0.78 V为下坡约0.07 eV，不能沿用nearly thermoneutral。
- 三样品最大上坡0.004、0.44、0.52 eV；限制电位0.78、0.34、0.26 V不变。
- 0.78 V的出处和写作规则依 `_shared_memory/inbox/20261116_2245_FeCoMn_图4图5正文修改与写作规则.md` 及最新manuscript/README。

保留修订和导师批注。除图5替换、对应代表性电位及其直接相连的能量表述以外，不自行润色或改动其他内容。存新的带日期时间Word版本，更新manuscript/README。SI本次不修改。
