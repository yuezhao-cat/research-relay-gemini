# 结论里的数字（Claude web 2，2026-11-22 13:20）
依据：REQUEST_Conclusion_20261122.md 的"13:14 第二步新问题"。写之前未读他方意见，未改 Word。

## 1. 0.48→0.96 V：结论里不保留。我修正此前的意见
- 我之前主张保留，理由是它是区别于 Wan 2022 的唯一定量证据。重新想过后，区别的实质是定性的，不需要靠这个数字。Wan 的轴向 OH 是永久配体；本文的轴向 OH 由颗粒在工作电位下维持，没有颗粒时 Mn 形成 Mn=O。无数字版 S3 的 whereas 对比已经把这一点说全了。
- 这个数字已经在摘要、前言第三段、图 5 末尾和表 S7 出现过四次。读者读到结论时早已见过它，结论再列一遍只会让句子变成结果复述。
- 高水平论文的习惯也是这样。资料包第 7 节归纳的 10 篇里，机理部分几乎都不出现计算数值，Zhao 2025 的机理句一个数也没有。

## 2. S2：只保留半波电位，稳定性写定性加时长，去掉 96.5%
- 我不建议全改成定性。maintains stable operation 太空，读者无法判断稳定到什么程度。资料包归纳的高水平论文性能只给一两个关键数，例如 Jiang 2016 只给了 E1/2。
- 建议保留 0.885 V 一个数字。238 h 作为时长保留，因为它说明的是"稳定多久"，读者一看就懂，不需要再拿别的数去比。96.5% 去掉。

Experimentally, FeCoMn–NC reaches an ORR half-wave potential of 0.885 V versus RHE in 0.1 M KOH, outperforming Pt/C, FeCo–NC, and Mn–NC, and operates stably for 238 h.
直译：实验上，FeCoMn–NC 在 0.1 M KOH 中的 ORR 半波电位达到 0.885 V（相对 RHE），优于 Pt/C、FeCo–NC 和 Mn–NC，并稳定运行 238 h。

如果赵月要求性能句一个数字都不留，原候选的定性句也可以用，只把 maintains stable operation 改为 operates stably for over 200 h。这样读者至少知道稳定的量级，"over 200 h"是概数，不算列数字。

## 3. 无数字版 S3、S4
**S3：合适，只改一处。** pH 13 也是一个数字。把它换成 at the working potential and pH，同时和 S1 的 under working conditions 拉开说法。现在 S3 不再讲转变电位的推移，"在工作电位下"修饰的就是保持轴向 OH 这件事，13:08 指出的逻辑问题已经不存在了。

Calculations show that, at the working potential and pH, the O*-covered FeCo alloy particles keep an axial OH on the adjacent Mn single atoms, whereas Mn without the particles forms Mn=O.
直译：计算表明，在工作电位和 pH 下，被 O* 覆盖的 FeCo 合金颗粒使相邻 Mn 单原子保持轴向 OH，而没有颗粒的 Mn 形成 Mn=O。

**S4：改两处，长度基本不变。**
- leaves Mn bonding capacity for OOH* 少了比较对象，读者会问"比谁留得多"。紧接 S3 的 Mn=O，补 than Mn=O does 三个词，电子途径就自然成立了。
- consume part of its binding energy 里的 its 指代不清，可以指 OH*，也可以指轴向 OH，违反主语明确的规则。改为 the binding energy。

The axial OH leaves Mn more bonding capacity for OOH* than Mn=O does and, by pulling Mn toward itself, makes OH* adsorption consume part of the binding energy, placing FeCoMn–NC near the volcano apex.
直译：轴向 OH 比 Mn=O 为 Mn 留下更多结合 OOH* 的成键能力，又通过把 Mn 拉向自身，使 OH* 吸附消耗一部分结合能，从而使 FeCoMn–NC 位于火山图顶点附近。

**是否还能更短。** 不建议再删。这一句已经只剩两条途径各一个短语，再加一个结果。再删掉其中一条，就会退回 V3 的问题，也就是只说"适中"，不说靠什么做到的。

## 4. 第二步全文（S3–S4，无计算数字）
Calculations show that, at the working potential and pH, the O*-covered FeCo alloy particles keep an axial OH on the adjacent Mn single atoms, whereas Mn without the particles forms Mn=O. The axial OH leaves Mn more bonding capacity for OOH* than Mn=O does and, by pulling Mn toward itself, makes OH* adsorption consume part of the binding energy, placing FeCoMn–NC near the volcano apex.
直译：计算表明，在工作电位和 pH 下，被 O* 覆盖的 FeCo 合金颗粒使相邻 Mn 单原子保持轴向 OH，而没有颗粒的 Mn 形成 Mn=O。轴向 OH 比 Mn=O 为 Mn 留下更多结合 OOH* 的成键能力，又通过把 Mn 拉向自身，使 OH* 吸附消耗一部分结合能，从而使 FeCoMn–NC 位于火山图顶点附近。

规则自查：没有冒号、分号、破折号，没有计算数字，没有 cost 或 penalty（遵守 REDLINES 第 8 条），每句主语明确，没有否定判断句。内容与正文一致：轴向 OH 对 Mn=O 对应表 S7 和图 5 末尾，成键能力对应图 6 第二段，拉回消耗结合能对应图 6 第二段和图 S30。
