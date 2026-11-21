# 正文"去掉轴向 OH"对照句：删除还是改写（Claude，2026-11-18 16:05）

请 Codex、Antigravity 一起思考，意见写入 review/axialOH_sentence_<名字>.md，注明所读提交号与依据。由赵月决定。

## 1. 现状
该对照原为图 5 节末单独一段（4 句，含 ΔGOH* 0.85→0.52、η 0.45→0.71，引表 S7 最后一行 "FeCoMn–NC without axial OH (8O*)"）。赵月认为数值都在 SI、写得太多，要求压缩并入上一段（ORR 段），并进一步问能否删除。

ORR 段（已定稿）结尾：
"...The order of the limiting potentials agrees with that of the measured half-wave potentials (Figure 3b), and the moderate intermediate binding of FeCoMn–NC accounts for its higher activity than FeCo–NC and Mn–NC."
其后紧接图 6 第一段（两个 Mn 的轴向配体不同：Mn–OH vs Mn=O）。

## 2. Claude 的两轮思考
**第一轮（倾向删除）**：认为"去掉轴向 OH"是人为加减吸附物，与已定原则"颗粒、Mn 是组分，8O*、轴向 OH 是吸附物，不能当组分加减"冲突，与撤销 2×2 同理；图 6 已用两个真实工作表面对比解释适中结合。代价：失去全文唯一的单变量证据（图 6 中两个 Mn 同时差轴向配体与有无颗粒）。

**第二轮（改为保留并改写）**：第一轮判断有误。图 5 中 FeCoMn–NC 覆盖随电位变化为 8H* → 8O* → 8O* + Mn–OH → 8O* + Mn–O。"8O*（无轴向 OH）"是覆盖度计算中真实存在的表面状态，只是出现在较低电位，不是虚构表面。2×2 中"Mn–NC 加 OH""干净颗粒"在任何电位都不出现，二者性质不同。
因此该句的意义是：若表面状态取错（用低电位的 8O*），OH* 结合过强、过电位增大；只有取 0.78 V 下的 8O* + Mn–OH，计算活性才与实验一致。这正体现覆盖度计算的意义，且位于图 5 节，符合"表面状态之间的对比放图 5"。

## 3. 改写方案（一句，无数字，并入 ORR 段末）
"On the 8O* surface without the axial OH, which forms at lower potentials (Figure 5d), OH* binds too strongly to Mn and the theoretical overpotential increases (Table S7)."
直译：在较低电位下形成的、没有轴向 OH 的 8O* 表面上（图 5d），OH* 与 Mn 结合过强，理论过电位增加（表 S7）。
表 S7 最后一行保留，行名改为 "FeCoMn–NC (8O*)"。

## 4. 请重点核查
1. 0.78 V、pH 13 下，8O* 与 8O* + Mn–OH 在图 5d（FeCoMn–NC Pourbaix）上是否确为相邻、8O* 在较低电位稳定。给出转变电位（来源文件）。
2. 表 S7 中 "without axial OH (8O*)" 那组 ORR 的背景结构，是否就是覆盖度库里 8O* 那个结构（同一 CONTCAR、原采用分支），而不是从 8O* + Mn–OH 中删掉 OH 后重新优化的另一结构。若不同，第 3 节的改写不成立。
3. 在一个非稳定电位（0.78 V 下 8O* 已非最稳）的表面上算 ORR 作比较，作为"表面状态取错的后果"是否合理；有无更好的表述。
4. 删除、保留原句、按第 3 节改写，三者中哪个与全文逻辑最一致，理由。
