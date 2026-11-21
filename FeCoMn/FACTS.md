# FeCoMn 数据事实表（只有"已复核"的数可进稿；录入人≠复核人）
口径：CHE，Table S10 约定，energy(sigma→0)，G(H2) = −6.83271509 eV，G(H2O) = −14.32745679 eV，ZPE−TS：OOH 0.403 / O 0.066 / OH 0.343 eV。电位 vs RHE。

| 编号 | 量 | 数值 | 单位 | 来源文件 | 录入人 | 复核人 | 状态 |
|---|---|---|---|---|---|---|---|
| F01 | FeCoMn–NC 半波电位（0.1 M KOH） | 0.885 | V | 正文 L99–101，图 3 | Claude web | | 待复核 |
| F02 | Pt/C、FeCo–NC 半波电位 | 0.864、0.864 | V | 共享记忆 metrics.py 核算 | Claude web | | 待复核 |
| F03 | Mn–NC 半波电位 | | V | 正文图 3 | | | 待录入 |
| F04 | 稳定性：238 h 后电流保留 | 96.5 | % | 正文 | Claude web | | 待复核 |
| F05 | U_L：FCM 8O* 带轴向 OH | 0.776（OOH* 生成限速） | V | from_agent/FeCoMn-T032/original_ligand_free_energies.csv | Claude web | | 待复核 |
| F06 | U_L：FCM 8O* 无轴向 OH | 0.516（OH* 脱附限速） | V | 同上 | Claude web | | 待复核 |
| F07 | U_L：Mn–NC 轴向 O | 0.256 | V | 同上 | Claude web | | 待复核 |
| F08 | 0.78 V 下 OOH* 生成 / OH* 脱附（带 OH） | +0.004 / −0.068 | eV | 由 F05 行 ΔG 计算 | Claude web | | 待复核 |
| F09 | Mn 离面高度：带 OH 基态 → OOH* / OH* / O* 后 | +0.442 → +0.003 / −0.009 / −0.098 | Å | from_agent/FeCoMn-T042_Mn_position/Antigravity.csv | Claude web | | 待复核 |
| F10 | Mn 离面高度：无 OH 基态 → OH* 后 | −0.010 → −0.456 | Å | 同上 | Claude web | | 待复核 |
| F11 | T041 静态 ΔE 拆分 OH*：总削弱 / 形变 / 冻结电子 | +0.336 / +0.236 / +0.100 | eV | from_agent/FeCoMn-T041/REPORT.md | Claude web | | 待复核 |
| F12 | T041 静态 ΔE 拆分 OOH*：总削弱 / 形变 / 冻结电子 / 吸附物形变 | +0.267 / +0.432 / −0.100 / −0.065 | eV | 同上 | Claude web | | 待复核 |
| F13 | FeCo–NC U_L | 0.34 | V | 正文图 5/6 | | | 待核 |
