# 结论第二步：S3–S5（Claude Code 本地，2026-11-22）

依据：`discussion/REQUEST_Conclusion_20261122.md` 的 13:01 定稿（S1、S2）与 13:02 讨论稿。只讨论第二步，未改 Word。

## 1. S3–S5 是否合适

### S3 证据：需要小改
问题：
- At the working potential and pH 修饰 shift … from 0.48 to 0.96 V，逻辑上不通。转变电位的推移是在不同电位之间比较，不发生在工作电位这一点上。工作电位只和后半句有关，即 Mn 在工作电位下保持轴向 OH。
- 0.48 V 是去掉颗粒后的值，原句没有交代，读者不知道从 0.48 V 推到 0.96 V 是和什么相比。
- during the ORR 比正文的说法宽。正文的结论是在代表电位 0.78 V 下 Mn 保持轴向 OH。

修改：
At pH 13, the O*-covered FeCo alloy particles raise the Mn–OH to Mn=O transition of the adjacent Mn single atoms from 0.48 V without the particles to 0.96 V versus RHE, so the Mn single atoms keep an axial OH at the working potential.

直译：在 pH 13 下，被 O* 覆盖的 FeCo 合金颗粒把相邻 Mn 单原子由 Mn–OH 向 Mn=O 的转变电位，从无颗粒时的 0.48 V 提高到 0.96 V（相对 RHE），因此 Mn 单原子在工作电位下保持轴向 OH。

### S4 机理：需要改（同时回答待判断一条）
问题：
- 两条途径和两个极限没有一一对应。电子效应避免的是 Mn=O 的过弱结合，几何效应避免的是无配体 Mn 的过强结合。原句把两条途径并列放在前面，把两个极限并列放在后面，读者要自己去配对。
- holding Mn out of the N4 plane 单独出现会误导，见第 3 节。

修改（仍为一句，每条途径紧跟它避免的那个极限）：
The axial OH moderates intermediate binding in two ways, as its weak bond leaves Mn more bonding capacity than an axial Mn=O does and thus avoids the overly weak binding of Mn=O, and its pull on Mn out of the N4 plane toward itself makes opposite-side adsorption spend part of the binding energy to draw Mn back and thus avoids the overly strong binding of ligand-free Mn.

直译：轴向 OH 通过两条途径使中间体结合适中，它的弱键比轴向 Mn=O 为 Mn 留下更多成键能力，从而避免了 Mn=O 的过弱结合，它把 Mn 向自身一侧拉出 N4 平面，使对侧吸附要消耗部分结合能把 Mn 拉回，从而避免了无配体 Mn 的过强结合。

这一句偏长（约 70 词）。如果赵月允许机理用两句，可以拆成：
The axial OH moderates intermediate binding in two ways. Its weak bond leaves Mn more bonding capacity than an axial Mn=O does, which avoids the overly weak binding of Mn=O, and its pull on Mn out of the N4 plane toward itself makes opposite-side adsorption spend part of the binding energy to draw Mn back, which avoids the overly strong binding of ligand-free Mn.
（拆开后第二句的两个 which 都紧跟各自的分句，指代清楚。）

### S5 火山图：合适，不改
FeCoMn–NC therefore lies near the apex of the activity volcano.
therefore 承接 S4 的结合适中。计算得到的火山图位置和 S2 的实测性能各说各的，没有写成计算导致实测，因果是对的。

## 2. 与 S1、S2 的衔接
- S1 说确定了工作条件下的表面覆盖，并揭示了颗粒如何影响相邻单原子的结合；S3 给覆盖结果和颗粒作用的证据，S4、S5 给结合如何被调到适中。顺序与 S1 的承诺一致，衔接顺。
- 重复：13:02 稿的 S3 以 At the working potential and pH 开头，紧接 S1 的 under working conditions，意思重复。改成 At pH 13 后，工作电位只在句末出现一次，与 S1 不再重复。
- S2 以 Experimentally 开头讲实测性能，S3 回到计算结果，中间没有转折词。由于 S1 已经说明表面覆盖是确定出来的，S3 的内容一看就是计算结果，不必再加 Calculations show（Claude web 去掉这一开头是对的，否则与 S1 重复）。
- adjacent Mn single atoms 在 S1 和 S3 各出现一次，是指同一对象，属于必要的重复，不用改。
- S4 和 S5 都没有再出现 0.885 V 或对照样品，与 S2 不重复。

## 3. 待判断一条：holding Mn out of the N4 plane 能否看懂
看不懂，而且容易被误解。正文写明，没有轴向 OH 时，Mn 也会离开 N4 平面，向被吸附的 OH* 一侧移动 0.46 Å，结果 OH* 结合过强。所以 Mn 出平面本身不是削弱结合的原因。真正起作用的有两点：
1. Mn 被拉向轴向 OH 一侧，也就是远离中间体的一侧；
2. 中间体在对侧吸附时，要先把 Mn 拉回平面，这会消耗一部分结合能。

只写 holding Mn out of the N4 plane，读者如果联想到无配体时 Mn 向 OH* 凸出，会得出相反的结论。因此至少要保留 toward itself（拉向自身一侧）和 opposite-side adsorption … draw Mn back 这两个要素。这不算讲过程，而是讲清几何途径的方向。第 1 节的 S4 修改稿已经包含这两点，没有数字。
