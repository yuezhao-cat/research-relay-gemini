# Zotero 文献交叉核对（Claude Code，2026-11-20）

Zotero 本地库中与 IDEAS_BOARD 各方向直接相关的文献。逐条对应 IDEAS_BOARD 条目，标注是否已在文献调研中使用。

---

## 一、直接支持 [6] 抗过氧化门控的文献

### Cao 2022 Nat Commun — 氧化态 vs 活性火山型关系
- **标题：** Volcano-type relationship between oxidation states and catalytic activity of single-atom catalysts towards hydrogen evolution
- **DOI：** 10.1038/s41467-022-33589-y
- **核心：** Os SAC，氧化态从 +0.9 到 +2.9，HER 活性呈火山型；最优氧化态在中间（+1.9）。配位环境（N/S/C 比例）调控氧化态，从而决定活性。
- **与我们的关系：** 直接类比。颗粒调控 Mn 的氧化态（Mn(III)–OH vs Mn(IV)=O），活性随之变化。可引用支持"氧化态决定活性"这一框架，把"颗粒推后 Mn 过氧化"落到已有文献的火山图框架里。
- **引用位置：** 图 6 讨论，[6] 主线支撑。

---

## 二、直接支持 [5]/[7] 高自旋活性态的文献

### Zhao 2025 Nat Catal — 高自旋 Fe(III)–OH–N4 是酸性 ORR 活性中心
- **标题：** Identifying high-spin hydroxyl-coordinated Fe3+N4 as the active centre for acidic oxygen reduction using molecular model catalysts
- **DOI：** 10.1038/s41929-025-01324-7
- **核心：** 用分子模型催化剂（卟啉 Fe）明确鉴定：酸性 ORR 的活性中心是高自旋 OH–Fe³⁺N4，而非低自旋 Fe²⁺N4。高自旋态由 OH 配体维持。这与我们的 Mn(III)–OH 高自旋（3.2 μB）vs Mn(IV)=O 自旋猝灭（0.3 μB）完全对应。
- **与我们的关系：** FeCoMn–NC 中的 Mn 情况与本文 Fe 情况高度同构：OH 配体 → 高自旋 → 活性，而非低自旋失活态。这篇文章已在 [CC-5]（审稿应对）中提到，但应该放到主线支撑。
- **注意：** [9] 指出"高自旋 M–OH 是活性态"已有顶刊报道，本文是证据。要在引言中指出我们的贡献不在于"发现 Mn–OH 高自旋活性"，而在于"颗粒如何使 Mn 维持这一状态"。
- **引用位置：** 引言 P2/P3，图 6 自旋态讨论。

---

## 三、直接支持 [1]/[CC-1] 形变能拆分的文献

### Zhang 2025 JACS — 弱结合 M-N-C 的反常高 ORR 活性
- **标题：** Why Do Weak-Binding M–N–C Single-Atom Catalysts Possess Anomalously High Oxygen Reduction Activity?
- **DOI：** 10.1021/jacs.4c16733
- **核心：** 经典 Sabatier 认为最优催化剂（Fe/Co–N–C）因"适中结合"活性最高；但一些"弱结合"M–N–C 也表现出异常高活性。本文解释该异常的机制。
- **与我们的关系：** 对我们是**潜在挑战**：若弱结合 M–N–C 可以高活性，为什么 Mn=O（也是弱结合）活性低？我们的答案是：Mn=O 自旋猝灭（0.3 μB），限制成键，不是简单的弱结合低活性。需在讨论中明确区分"弱结合但自旋正常"vs"弱结合且自旋猝灭"。[CC-5] 已提及本文，但该应对逻辑应写进来。
- **引用位置：** 讨论，作为对比和审稿应对。

---

## 四、支持工作态/原位表征框架的文献

### Deng 2023 JACS — 原位光谱分析轴向 O 配位 Sn 单原子
- **标题：** Operando Spectroscopic Analysis of Axial Oxygen-Coordinated Single-Sn-Atom Sites for Electrochemical CO2 Reduction
- **DOI：** 10.1021/jacs.2c12952
- **核心：** 用原位 XAS 鉴定工作条件下 Sn 单原子的轴向 O 配位状态；轴向 O 是电化学工作条件下形成的，不是静态结构中的配体。
- **与我们的关系：** 方法论先例。我们的"工作条件下 Mn 带轴向 OH"与本文"工作条件下 Sn 带轴向 O"同构；证明"工作态 = 电位+电流下的真实配位"是已有框架，可引用。
- **引用位置：** 图 5 覆盖度/工作态讨论，引言关于工作态重要性。

### Yuan 2025 Nat Commun — FeCo 双原子催化剂 Co 为活性中心
- **标题：** Janus effect of FeCo dual atom catalyst with Co as active center in acidic oxygen reduction
- **DOI：** 10.1038/s41467-025-62728-4
- **核心：** FeCo DAC 中 Fe–Co 键强，原位光谱显示 Co 为 ORR 活性中心，Fe 通过电子调控 Co；动态结构演变使机理复杂。
- **与我们的关系：** FeCo 组合已有报道，原位光谱是关键方法；但我们的体系是**颗粒 FeCo + 单原子 Mn**（非双原子），作用机理不同（FeCo 决定 Mn 配体，非直接成键）。可引用作为 FeCo 活性调控的文献背景，说明我们体系的不同之处。
- **引用位置：** 引言 P2 颗粒与单原子协同背景。

---

## 五、尚未在 Zotero 中找到的关键文献（需补充）

| 文献 | 在哪里提到 | 是否在 Zotero |
|---|---|---|
| Kim JACS 2024 (Mn ORR spin, 10.1021/jacs.4c13137) | 上下文/[7] | 未找到 |
| Yang Nat Commun 2021 (single eg electron, 10.1038/s41467-021-21919-5) | [5] 相关 | 未找到 |
| Zagal & Koper Angew 2016 (10.1002/anie.201604311) | [CC-6]/[6] | 未找到 |
| Ramaswamy, Mukerjee JACS 2013 (10.1021/ja405149m) | [CC-6] | 未找到 |
| Perutz Nature 1970 (10.1038/228726a0) | [CC-1] | 未找到 |
| Nat Catal 2025 Zhao operando (另一篇?) | [10] | 已有（上面第二条） |

建议把以上文献加入 Zotero，或直接在文中引用 DOI。

---

## 六、总结：Zotero 中与各观点对应的引用路线

| IDEAS_BOARD 条目 | Zotero 现有文献 | 建议用途 |
|---|---|---|
| [6] 抗过氧化门控 | Cao 2022 Nat Commun | 氧化态-活性火山，支持框架 |
| [5]/[7] 高自旋活性 | Zhao 2025 Nat Catal | 高自旋 OH–FeN4 = 活性中心，同构支撑 |
| [1]/[CC-1] 形变拆分 | Zhang 2025 JACS | 对比：弱结合异常活性，需区分自旋猝灭 |
| 工作态方法 | Deng 2023 JACS | 原位轴向配位方法先例 |
| FeCo 背景 | Yuan 2025 Nat Commun | FeCo 协同背景，区分我们体系 |

---

*Claude Code，2026-11-20。从本地 Zotero 检索（pyzotero local 模式），仅含数据库中已有文献。*
