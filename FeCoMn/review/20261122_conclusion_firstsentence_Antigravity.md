# FeCoMn 结论第一句与 S2–S5 配合评估（Antigravity，2026-11-22 12:47）

依据：`FeCoMn/discussion/REQUEST_Conclusion_20261122.md`（12:45 更新：第一句重新讨论）。本次仅提交本文件，未修改 Word 或仓库内其他文件。

---

## 一、第一句候选 A、B、C 评估与推荐版本

### 1. 对 A、B、C 的判断

- **候选 A（三个动词）不推荐**：一句同时承载 `prepared`、`determined`、`revealed`、`which explains` 四个动作，信息过载、结构松散，且末尾 `which explains its high ORR activity` 中 `which` 挂在整句之后、`its` 存在多个前置名词，可读性不及 C。
- **候选 B（只用 `using ... we revealed`）不推荐**：最凝练，但把实验制备降格为工具状语 `using FeCoMn–NC`，弱化了本文实验加理论结合的特征，读起来像纯计算分析。
- **候选 C（`prepared ... and revealed ...`）方向最对，但有两处可优化**：
  1. `which explains why...` 仍属于指代前文整句的松散非限制从句。
  2. 把 `Pt/C, FeCo–NC, and Mn–NC` 提前放进第一句，会让第一句尾部偏重，同时把「性能对比」和 S2 的「关键数值（`0.885 V`、`96.5% / 238 h`）」拆成两处。
  3. 术语宜保持红线要求的 `an FeCoMn–NC catalyst`。

### 2. 推荐第一句（基于 C 精修，记作 C'）

**English**

In summary, we prepared an FeCoMn–NC catalyst combining FeCo alloy particles and Mn single atoms, and revealed how covered particles regulate intermediate binding at adjacent Mn single atoms under working conditions to achieve high ORR activity.

**中文直译**

综上所述，我们制备了一种兼具 FeCo 合金颗粒与 Mn 单原子的 FeCoMn–NC 催化剂，并揭示了工作条件下被覆盖的颗粒如何调控相邻 Mn 单原子上的中间体结合以实现高 ORR 活性。

**理由**：保留实验制备与核心科学问题两条主干（`prepared ... and revealed ...`），首句即正面回应前言第二段（工作条件下被覆盖的颗粒如何影响相邻单原子结合），去掉 `which` 整句指代，并把三个对照样品留给 S2 与实测数字集中呈现。

---

## 二、第一句改动后，S2–S5 的配合建议

1. **S2（性能句）**：
   - 若采纳 **C'**（第一句不列对照样品名）：S2 应把 `surpassing Pt/C, FeCo–NC, and Mn–NC` 与两个实测核心数字合写在一句里，性能证据最完整：
     `In 0.1 M KOH, FeCoMn–NC achieves an ORR half-wave potential of 0.885 V versus RHE, surpassing Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h.`
   - 若沿用原 **C**（第一句已写 `outperforms Pt/C, FeCo–NC, and Mn–NC`）：S2 **必须保留 `0.885 V` 与 `96.5% / 238 h` 两个数字**，直接沿用 12:43 版 S2 即可，不必再重复对照样品名。
2. **S3（证据句）**：
   - 12:43 版 S3 已经很稳。因第一句已出现 `under working conditions`，S3 开头可改为 `At the working potential and pH`，既补齐 pH 维度，又避免连续两句重复同一短语。
3. **S4（机理句）**：
   - 12:43 版 S4 压缩得很好，建议做两处小修：把 `weak binding` / `strong binding` 补回 `overly`（`overly weak binding` / `overly strong binding`）以准确表达「过弱/过强」；末尾 `the ORR activity of FeCoMn–NC lies near the apex of the volcano` 建议改为 `, placing FeCoMn–NC near the apex of the activity volcano`（落在火山图顶点附近的是催化剂而非活性本身）。
4. **S5（意义句）**：
   - 12:43 版 S5 非常扎实，精准落在了「覆盖颗粒通过移动轴向配体转变电位来调控中间体结合」这一本文独有规律，并闭合了裸位点模型局限，且避开了此前「窗口宽度直接决定活性高低」的审稿风险。建议仅将 `the adjacent single atoms` 改为泛指 `adjacent single atoms`，使收尾更具普适性。

---

## 三、配合后的完整 5 句参考（C' + 精修 S2–S5）

### English Conclusions

In summary, we prepared an FeCoMn–NC catalyst combining FeCo alloy particles and Mn single atoms, and revealed how covered particles regulate intermediate binding at adjacent Mn single atoms under working conditions to achieve high ORR activity. In 0.1 M KOH, FeCoMn–NC achieves an ORR half-wave potential of 0.885 V versus RHE, surpassing Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h. At the working potential and pH, the O*-covered FeCo alloy particles shift the Mn–OH to Mn=O transition of adjacent Mn single atoms from 0.48 to 0.96 V versus RHE, so Mn retains an axial OH during the ORR. The axial OH leaves Mn more bonding capacity than an axial Mn=O does and holds Mn out of the N₄ plane, keeping intermediate binding between the overly weak binding of Mn=O and the overly strong binding of ligand-free Mn and placing FeCoMn–NC near the apex of the activity volcano. Covered particles therefore regulate intermediate binding by shifting the potential at which adjacent single atoms change their axial ligand, an effect that extends the understanding of ORR catalysis beyond bare-site models.

### 完整中文直译

综上所述，我们制备了一种兼具 FeCo 合金颗粒与 Mn 单原子的 FeCoMn–NC 催化剂，并揭示了工作条件下被覆盖的颗粒如何调控相邻 Mn 单原子上的中间体结合以实现高 ORR 活性。在 0.1 M KOH 中，FeCoMn–NC 的 ORR 半波电位达到 0.885 V（相对于 RHE），超过 Pt/C、FeCo–NC 和 Mn–NC，并在 238 h 后保持 96.5% 的初始电流。在工作电位和 pH 下，O* 覆盖的 FeCo 合金颗粒将相邻 Mn 单原子由 Mn–OH 向 Mn=O 的转变从 0.48 移至 0.96 V（相对于 RHE），因此 Mn 在 ORR 期间保持轴向 OH。轴向 OH 相比轴向 Mn=O 为 Mn 留出了更多成键能力，并将 Mn 保持在 N₄ 平面之外，使中间体结合处于 Mn=O 的过弱结合与无配体 Mn 的过强结合之间，从而将 FeCoMn–NC 置于活性火山图顶点附近。因此，被覆盖的颗粒通过移动相邻单原子改变轴向配体的电位来调控中间体结合，这一作用将对 ORR 催化的认识拓展到了裸位点模型之外。
