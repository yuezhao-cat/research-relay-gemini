# FeCoMn-T012 在 Zotero 中查找"用实验大数据引出问题"的论文

- 发起方：Claude
- 日期：2026-11-15
- 目的：赵月拿到一份 ORR 实验数据库（`ORR.xlsx`，1484 行 M–N–C 数据，列结构与 DigCat 平台一致），想把它用到 FeCoMn 论文的图 1 来引出问题。需要参考别人怎么用大数据。

## 已读的 5 篇（不用重复找）
- Zhang 2025 JACS, Why Do Weak-Binding M–N–C SACs Possess Anomalously High ORR Activity（图 1：按金属分组的半波电位箱线图，碱性/酸性）
- Liu 2026 Angew, Dual-Sabatier Optima…Dual-Atom Catalysts（图 1：实验活性 vs ΔG(OH*) 火山图，单原子 vs 双原子）
- Jiang 2025 JACS, Pyrrolic vs Pyridinic M–N–C in NO3RR（图 1：>60 个 M–N–C 的产率–法拉第效率–电位三维散点）
- Wang 2025, Divalent Hydride Electrolytes…Data-Driven Framework with LLM（图 1：数据库中全部 SSE 的电导率与活化能）
- Jia 2025, Closed-Loop Framework…Bifunctional Metal Oxide Catalysts（DigCat 闭环）

## 要做的
1. 在赵月的 Zotero 库中检索（全文与标题、摘要、标签）：DigCat、Digital Catalysis Platform、data-driven、big data、data mining、database、high-throughput experiment、literature mining、machine learning + ORR/OER/M–N–C/single-atom/dual-atom 等。
2. 找出**用已报道实验数据（数据库或文献汇总）做统计图来引出科学问题**的论文，优先：ORR、M–N–C、单原子/双原子/多金属、颗粒与单原子协同、表面覆盖度或工况表面。
3. 对每篇列出：作者、年份、期刊、DOI；数据来源（哪个数据库、多少条数据）；**图 1（或用到大数据的那张图）的画法**（箱线图/火山图/散点/热图/周期表等，横纵轴是什么）；这张图引出了什么问题；后文如何回答这个问题（理论、实验验证）。
4. 特别留意 Hao Li 课题组（东北大学）使用 DigCat 的论文，以及 DigCat 平台本身的引用文献（平台介绍论文）。
5. 把最有参考价值的 3–5 篇的图 1 截图放到 `FeCoMn/refs/big_data_examples/`（只放截图，不放全文 PDF）。

## 交付（`FeCoMn/from_agent/FeCoMn-T012/`）
- REPORT.md：表格汇总，按"与本文相关度"排序，并总结常见的几种大数据引出问题的套路。
- 更新 STATUS.md。
