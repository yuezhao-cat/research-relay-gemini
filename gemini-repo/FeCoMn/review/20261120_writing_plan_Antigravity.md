# 写作方案评审与图 6 重写中英文初稿（Antigravity，2026-11-20）

针对 `FeCoMn/discussion/20261120_2205_writing_plan_for_review.md`（`93abea1`）提出之 5 个问题逐项答复，并给出可审阅的**图 6 段英文与直译初稿**（未修改 Word 与正文章节）。

---

## 一、对写作方案五个问题的逐项意见

### 1. 正文各处增删是否合理（总体认可，附 3 处数值/措辞补正）
主线“两次去掉、两种失败”（去颗粒 `T039` → `0.96 → 0.48 V`、落回 `Mn=O` 太弱；去轴向 `OH` `T032` → 落回 `0.52 V` 太强；两者都在 → `Mn–OH` `0.78 V` 适中）逻辑闭环完整，且排除 `Cdl/ECSA`、低能分支、Wan 2022 与未经验证的颗粒细节机理，完全赞同。建言补正三处精确细节：

1. **`T041` 精确数值须把 `0.33` 校为 `0.34 eV`，且 `OOH*` 拆分勿写笼统的“全部”**：
   - `OH*` 削弱总量为 **`+0.336 eV`（四舍五入为 `0.34 eV`，不是 `0.33 eV`）**，其中基底形变增量 `+0.236 eV`（`0.24 eV`，占 `70.4%`），冻结电子结合减弱 `+0.100 eV`（`0.10 eV`）。
   - `OOH*` 静态净削弱为 **`+0.267 eV`（`0.27 eV`）**，其中基底形变增量高达 **`+0.432 eV`（`0.43 eV`）**、大于净削弱本身，而冻结几何电子结合反略强 `−0.100 eV`（另加吸附物内能形变差 `−0.065 eV`）。英文正文宜明确写“**extra substrate deformation of 0.43 eV offsets the slightly stronger frozen-geometry electronic interaction (−0.10 eV), yielding the net weakening**”，既准确又无漏洞。
2. **图 5 段首/段末给 `T038` 留 1 句锚点**：
   - 既然 SI 新增 `T038` 表/图，正文图 5 段在放 `T039` 前须有一句交代“在无轴向配体的裸 Mn 位点上，移除 `FeCo(8O*)` 颗粒几乎不改变 Mn 的局域电荷与磁矩（`Δq = +0.006 e`, `Δμ = −0.01 μB`, SI `T038`），而颗粒效应在工作电位表面覆盖下显现在轴向配体选择上（`T039`）”，避免 SI `T038` 在正文无引用落点。
3. **随手清两处已核出的零成本小隐患**（同属删电容句同批次清理）：
   - 将正文 7 处 `adjacent / next to / neighboring`（行 51、61、107、119、363、399、408）改为 `the Mn single atoms in FeCoMn–NC` 等不涉及未测距离依赖的表述（对齐 11-19 定下“不写相邻”口径）；
   - 将第 210–211 行 `reflects the intrinsic activity` 删改为只写 `is corrected for mass transport`（因未做单位点数归一化）。

### 2. 图 6 段五个要点的顺序与第 ④ 条 `dz²` 的取舍
- **顺序**：完全支持按清单 **① → ② → ③ → ④ → ⑤** 顺序推进（去 OH 过强 `0.52 V` → 几何原因 `h: +0.44 → 0.00 Å` → `T041` 形变代价拆解 → `T037` `dz²` 配对成键保留电子通道 → 对照 `Mn–NC` `Mn=O` 双键致自旋猝灭且回不到平面而过弱 → 落回火山图）。
- **第 ④ 条 `dz²` 建议保留在正文（压缩为 1–2 句）**：它正好回答了审稿人看懂 `T041` 后的必然一问——“为什么加上轴向 `OH` 付出形变代价的同时，界面电子结合并没有随之垮掉？”原因在于高自旋 `Mn–OH` 保持了一个靠近费米能级（`−3.17 eV`）的单占 `dz²` 轨道，吸附 `OOH*` 时以 `dz²–O 2pz` 配对形成强反位键（`−ICOHP = 3.12 eV`, `dz² = 1.38 eV`），严格只作成键方式描述、不写轨道竞争（恪守 `T037` 反证 1 与反证 2）。

### 3. 图 6 v3 面板设计（丰富好看 + 讲透主线）
兼顾赵月“主图好看、数据丰富、不精简过头”的要求，建议如下排布（`2×3` 或 `3×3` 均可；以 **2×3 六联图或微调 3×3** 呈现最为饱满）：
- **a（机制示意图）**：三态闭环（左：无 `OH` 裸 `Mn` `8O*`，`h ≈ −0.01 → −0.46/−0.31 Å`, `U_L = 0.52 V`；中：工作态 `8O* + Mn–OH`，`+3.2 μB`, `h: +0.44 → 0.00 Å`, `U_L = 0.78 V`；右：无颗粒 `Mn=O`，`~0.0–0.3 μB`, `h: +0.51 → +0.17 Å`, `U_L = 0.26 V`），两条切换箭头清晰标注 `Remove OH (T032)` 与 `Remove particle (T039)`。
- **b（`T039` 单变量颗粒切换图）**：`ΔG(Mn–OH − Mn–O)` vs `U_RHE`（或对照条形/相线：`FCM 8O*` `U* = 0.96 V` vs `T039 C_support` `U* = 0.48 V` vs `Mn–NC` `U* = 0.48 V`，标注 `0.78 V` 处 `−0.18 eV → +0.30 eV` 翻转）。
- **c（`T042` `Mn` 离面位移与吸附强度关系）**：横轴 `h_after (Å)`（吸附态 `Mn` 相对 4N 平面高度），纵轴 `ΔG_OOH*` / `ΔG_OH*` 与叠加 $U_L$ 火山点（直观展示 `Mn` 压入反侧太强、停在 `0.00 Å` 居中、拉不回来太弱）。
- **d（`T041` 能量拆分柱状图）**：`withOH − noOH` 对 `OH*`（`ΔE_dist = +0.24`, `ΔE_elec = +0.10`, `ΔE_tot = +0.34 eV`）与 `OOH*`（`ΔE_dist = +0.43`, `ΔE_elec+int = −0.16`, `ΔE_tot = +0.27 eV`）的叠堆/对比柱状图，一图看懂几何代价主导削弱。
- **e（`T037` 自旋分辨 `metal 3d + Mn dz²` PDOS 与关键 `−ICOHP`）**：保留同源 COHP 静态的 `3d`（虚线 `εd`）+ 深色叠加 `dz²`（点线 `εdz2`: `−3.17` vs `−5.12 eV`）及磁矩、`−ICOHP(axial / OOH*)` 数值标注（沿用 `FeCoMn-T037 v2` 乙方案高颜值风格）。
- **f（火山图）**：在原有 `FeCo–NC`、`FeCoMn–NC`、`Mn–NC` 三点基础上，**加标 `FCM 8O* (no OH, 0.52 V)` 空心对照点**，使“去 OH 掉左坡、去颗粒掉右坡、工作态居火山顶”全部落在火山同一张图上。

*(若想保留 v38 的 `−pCOHP` 和 Bader 电荷转移以维持 `3×3` 饱满度，可将 `c/d` 保持为紧凑双子图并将 `−pCOHP` 与 Bader 保留为第 7、8 面板，视觉信息量最均衡。)*

### 4. SI 新增与顺延冲突提示
5 项 SI 内容全部与正文新主线一比一挂钩，建议增补顺序与正文引用完全同步：
- 新增结构与编号建议：`Table S6`（`T038` 无配体对照 + 接口差分电荷摘要 / 配套 `Figure S12` 维持与旧表一致）→ `Table S7`（`T039` 颗粒去留配体稳定性、转变电位、磁矩、`Mn–O` 键长、`h_Mn`）→ 原表 `S7–S11` 顺延为 `Table S8–S12`，同时在对应表加入 `T032`（`8O* no OH` 自由能）、`T041`（形变/电子拆分详表）、`T042`（吸附前后 `h_Mn` 坐标全表及关联散点图）。
- **唯一防错重点**：正文和 SI 中目前存在多处硬编码交叉引用（如 `Table S7`、`Table S10`、`Figure S24–S30`、`Section 2.8`），改完插入顺序后必须在定稿前用脚本全篇检索核对一遍全部 `Figure Sxx` 与 `Table Sxx` 编号对应关系，避免错号。

### 5. 标题是否保留 `Determine`
**建议保留 `Determine`**。`T039` 已经在固定同载体几何下去除颗粒证实转变电位从 `0.96 V` 回落到 `0.48 V`、`0.78 V` 下偏好净翻转 `+0.48 eV`，严格单变量确立了颗粒对工作态轴向配体的因果作用。若希望主谓读起来更流畅，也可微调语序为 *FeCo Alloy Particles Determine the Working-State Axial Ligand of Mn Single Atoms for Oxygen Reduction*，否则沿用 22:19 含 `Determine` 的标题亦完全站得住。

---

## 二、图 6 段重写初稿（英文 + 中文直译，待审阅，未动 Word）

> **写法自查**：按 ① 去 `OH` 太强（`T032` `0.52 V`）→ ② `OH` 拉出 `0.44 Å` 吸附回平面（`T042`）→ ③ 形变代价拆解（`T041` `OH*` `0.24 / 0.34 eV`，`OOH*` `+0.43 eV`）→ ④ `dz²` 单占配对保住电子成键（`T037`）→ ⑤ `Mn–NC` `Mn=O` 双键自旋猝灭且回不到平面（`0.26 V`）→ ⑥ 落到火山图与实验 `Tafel / RRDE` 收口。全文避免任何防御性语句，中文直译零中文冒号、零中文分号。

### 英文正文草稿（Draft for Figure 6 Narrative）

To understand why the working-state axial OH places FeCoMn–NC near the top of the ORR volcano, we first examined the same `8O*`-covered FeCoMn–NC model without the axial OH (Table Sxx). Removing the axial OH causes the Mn site to bind the intermediates too strongly (`ΔG_OH* = 0.52 eV`), lowering the limiting potential from `0.78` to `0.52 V` because `OH*` removal becomes sluggish. Before the reaction, the occupied d-band centers of Mn in FeCoMn–NC (`−3.42 eV`) and Mn–NC (`−3.54 eV`) are nearly identical (Figure 6a), so the overall d-band position alone cannot explain this difference. Instead, geometric and energy-decomposition analyses reveal that the axial OH regulates binding mainly through structural relaxation (Figure 6x–y and Tables Sxx). In working FeCoMn–NC, the axial OH initially pulls Mn `+0.44 Å` out of the `N4` plane toward the ligand, and adsorption of `OH*` or `OOH*` on the opposite face pulls Mn back into the `N4` plane (`h = −0.01` and `0.00 Å`), whereas bare Mn without axial OH relaxes freely toward the reacting intermediate (`h = −0.46` and `−0.31 Å`). Decomposing the adsorption energy into substrate distortion and frozen-geometry electronic interaction confirms that this return-to-plane deformation accounts for `0.24 eV` (`70%`) of the `0.34 eV` total weakening of `OH*` binding, while for `OOH*` the extra substrate deformation penalty (`0.43 eV`) even outweighs the slight strengthening (`−0.10 eV`) of the frozen-geometry electronic interaction to yield the net weakening (`0.27 eV`). Meanwhile, the axial `Mn–OH` single bond (`−ICOHP = 2.64 eV`, `Mn–O = 1.88 Å`) keeps Mn in a high-spin state (`3.21 μB`) with a singly occupied, high-lying `dz²` orbital (`ε_dz2 = −3.17 eV`, Figure 6x). During `OOH*` adsorption, this `dz²` state pairs with the O `2p` orbitals (`Mn–OOH*` `−ICOHP = 3.12 eV`, `dz²` contribution `1.38 eV`), preserving a strong covalent bonding channel despite the deformation cost. By contrast, in particle-free Mn–NC, the strong axial `Mn=O` double bond (`−ICOHP = 8.03 eV`, `Mn–O = 1.58 Å`) quenches the Mn spin moment (`0.001 μB` in the COHP static), pushes the `dz²` states deep below the Fermi level (`−5.12 eV`), and holds Mn `+0.13` to `+0.17 Å` out of the `N4` plane even after intermediate adsorption. As a result, `OOH*` bonding is overly weakened (`−ICOHP = 2.65 eV`, `ΔG_OOH* = 4.66 eV`, `U_L = 0.26 V`), making `O2` activation rate-limiting. Overall, the FeCo particles prevent over-oxidation to `Mn=O`, while the axial OH introduces a controlled out-of-plane deformation penalty without closing the `dz²` bonding channel, placing FeCoMn–NC near the apex of the ORR activity volcano (Figure 6f), in line with its lowest Tafel slope (`40.2 mV dec⁻¹`) and high four-electron selectivity (`n = 3.83`, `8.3% H2O2`).

### 中文直译（零中文冒号、零中文分号）

为了理解工作态轴向 OH 为何使 FeCoMn–NC 处于 ORR 火山图顶部附近，我们首先检验了同一 `8O*` 覆盖的 FeCoMn–NC 模型在去掉轴向 OH 后的情况（Table Sxx）。去掉轴向 OH 会使 Mn 位点与中间体结合过强（`ΔG_OH* = 0.52 eV`），`OH*` 脱附受阻，从而使极限电位从 `0.78 V` 降至 `0.52 V`。反应前，FeCoMn–NC 中 Mn 的占据 d 带中心（`−3.42 eV`）与 Mn–NC（`−3.54 eV`）几乎相同（Figure 6a），因此仅靠整体 d 带位置无法解释这一差异。几何分析与能量拆分进一步表明，轴向 OH 主要通过结构弛豫代价来调控吸附强度（Figure 6x–y 与 Tables Sxx）。在工作态 FeCoMn–NC 中，轴向 OH 预先将 Mn 向配体一侧拉出 `N4` 平面 `+0.44 Å`，当 `OH*` 或 `OOH*` 在对位吸附时，必须将 Mn 拉回 `N4` 平面（`h = −0.01` 与 `0.00 Å`），而在没有轴向 OH 的裸 Mn 上，Mn 会毫无阻滞地朝向反应中间体一侧偏移（`h = −0.46` 与 `−0.31 Å`）。将吸附能拆分为基底形变能与冻结几何电子相互作用的结果证实，这种回平面形变在 `OH*` 总结合减弱量（`0.34 eV`）中占 `0.24 eV`（`70%`），而对于 `OOH*`，额外的基底形变代价（`0.43 eV`）甚至超过冻结几何电子结合略微增强的部分（`−0.10 eV`），从而带来净削弱效果（`0.27 eV`）。与此同时，轴向 `Mn–OH` 单键（`−ICOHP = 2.64 eV`，`Mn–O = 1.88 Å`）使 Mn 保持在高自旋态（`3.21 μB`），并保留了一个能量较高的单占 `dz²` 轨道（`ε_dz2 = −3.17 eV`，Figure 6x）。吸附 `OOH*` 时，该 `dz²` 态与氧 `2p` 轨道配对成键（`Mn–OOH*` `−ICOHP = 3.12 eV`，其中 `dz²` 贡献 `1.38 eV`），从而在付出形变代价的同时仍维持了有效的电子成键通道。相比之下，在不含颗粒的 Mn–NC 中，强轴向 `Mn=O` 双键（`−ICOHP = 8.03 eV`，`Mn–O = 1.58 Å`）不仅猝灭了 Mn 的局域磁矩（COHP 静态为 `0.001 μB`）并将 `dz²` 态推至费米能级深处（`−5.12 eV`），还在中间体吸附后仍将 Mn 拉留在 `N4` 平面外 `+0.13` 至 `+0.17 Å`。这使得对位 `OOH*` 成键被过度削弱（`−ICOHP = 2.65 eV`，`ΔG_OOH* = 4.66 eV`，`U_L = 0.26 V`），导致 `O2` 活化受阻。综上，FeCo 颗粒阻止了 Mn 过度氧化为 `Mn=O`，而轴向 OH 在保留 `dz²` 成键通道的同时引入了受控的离面回平面形变代价，使 FeCoMn–NC 位于 ORR 活性火山顶部附近（Figure 6f），这与其最低的 Tafel 斜率（`40.2 mV dec⁻¹`）和较高的四电子选择性（`n = 3.83`，`H2O2` 产率 `8.3%`）相一致。

*(注：若图 6 确定沿用 COHP 同源静态展示磁矩，`0.001 μB` 与 `−3.54 eV` 可直接对齐正文，并在图注注明其来自 COHP 非对称化静态；若保留原 Genkai `ISYM=2` 静态磁矩 `0.29 μB` 与 `−3.44 eV`，可在写图注时对应统一，两者绝不混用。)*
