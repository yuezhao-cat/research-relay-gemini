# 摘要草稿（Antigravity，2026-11-20）

基于现稿 `FeCoMn_Manuscript_revised_20261117_1845.docx` 及已核实实验/计算数据，严格按当前四方对齐的稳健主线（不写颗粒推迟过氧化 `0.49 → 0.96 V` 强因果，突出 `T032 + T042 + T041` 轴向 `OH` 离面形变代价机理）撰写，约 237 词。未修改 Word 或配图。

## 英文正文

Pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts often contain metal particles alongside dispersed single-atom sites, yet how operating-state surface coverage controls intermediate binding remains unclear. Here, we prepare an FeCoMn–NC catalyst combining FeCo alloy particles with dispersed Mn–N4 sites for the alkaline oxygen reduction reaction (ORR). In 0.1 M KOH, FeCoMn–NC reaches a half-wave potential of 0.885 V versus the reversible hydrogen electrode (RHE), surpassing Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current over 238 h. Operando infrared spectroscopy reveals potential-dependent surface species, motivating coverage calculations at 0.78 V versus RHE (pH 13). These calculations identify O*-covered FeCo particles and an axial OH-ligated Mn site in FeCoMn–NC, whereas particle-free Mn–NC forms an axial oxo (Mn=O) site. Without the axial OH, the Mn site binds ORR intermediates too strongly and is limited by OH* removal (limiting potential 0.52 V). The axial OH pulls Mn out of the N4 plane by 0.44 Å, so adsorbing an intermediate on the opposite side must pull Mn back into the plane. This deformation penalty weakens the overly strong OH* binding while keeping OOH* formation nearly thermoneutral, raising the limiting potential to 0.78 V. By contrast, oxo-ligated Mn–NC binds OOH* too weakly (0.26 V), and O*-covered FeCo–NC binds oxygenated intermediates too strongly (0.34 V). These results show how operating-state axial OH ligation balances ORR intermediate binding through a geometric distortion penalty in composite M–N–C catalysts.

## 中文直译（已禁用中文冒号与分号）

热解制备的金属–氮–碳（M–N–C）催化剂常同时含有金属颗粒和分散的单原子位点，但在工作状态下表面覆盖如何调控中间体结合尚不清楚。本文制备了一种将 FeCo 合金颗粒与分散的 Mn–N4 位点结合的 FeCoMn–NC 催化剂，用于碱性氧还原反应（ORR）。在 0.1 M KOH 中，FeCoMn–NC 的半波电位达到 0.885 V（相对可逆氢电极 RHE），优于商业 Pt/C、FeCo–NC 和 Mn–NC，且在 238 h 运行后仍保持初始电流的 96.5%。原位红外光谱揭示了催化剂表面物种随电位演变，因此我们计算了 0.78 V（相对 RHE，pH 13）工作条件下的表面覆盖。计算结果表明，FeCoMn–NC 中 FeCo 颗粒表面被 O* 覆盖且 Mn 位点带有轴向 OH 配体，而无颗粒的 Mn–NC 形成轴向氧配位（Mn=O）位点。去掉该轴向 OH 后，Mn 位点对 ORR 中间体结合过强，反应受限于 OH* 脱除（极限电位 0.52 V）。轴向 OH 将 Mn 原子拉出 N4 平面 0.44 Å，因此中间体在对侧吸附时必须把 Mn 拉回平面内。由此产生的形变代价削弱了过强的 OH* 结合，同时保持 OOH* 生成接近热中性，使极限电位提升至 0.78 V。相比之下，带轴向氧配体的 Mn–NC 对 OOH* 结合过弱（0.26 V），而被 O* 覆盖的 FeCo–NC 对含氧中间体结合过强（0.34 V）。这些结果阐明了工作态轴向 OH 配位如何通过几何畸变代价平衡复合 M–N–C 催化剂中的 ORR 中间体结合。

## 数值与口径依据

| 要素 | 来源 |
|---|---|
| `0.885 V vs RHE`、`0.1 M KOH`、优于 `Pt/C` / `FeCo–NC` / `Mn–NC`、`238 h` 保持 `96.5%` | 正文现稿（`FeCoMn_Manuscript_revised_20261117_1845.docx`）与 `05_ORR` 稳定性数据 |
| 原位红外表面物种随电位演变 | 图 4 定稿版（`FeCoMn-T015/20261116_A_single_bend1_V2`，`E(RHE)=E(SCE)+1.016 V`，`1.2 → 0 V`） |
| `0.78 V`（pH 13）表面覆盖：`8O*` 颗粒、`FeCoMn–NC` `Mn–OH`、`Mn–NC` `Mn=O` | 图 5 / 表 S5（基于所采用 `Mn=O` 电子态分支，见 SI 两分支对照表 `23aa751`） |
| 无轴向 `OH` 过强且 `OH*` 脱除限速（`0.52 V`） | `T032`（同 `8O*` 背景） |
| 轴向 `OH` 将 `Mn` 拉出 `N4` 平面 `0.44 Å`，吸附时拉回平面产生形变代价并保留 `OOH*` 近热中性（`0.78 V`） | `T042` + `T041` |
| 对照极限电位 `Mn–NC` `0.26 V`、`FeCo–NC` `0.34 V` | 正文现稿与图 6 |

## 与另两版草稿（`a0f80c0` / `84143b6` / `ClaudeWeb_replies` 22:20）的主要区别

1. 不含 `a0f80c0` 的 `0.49 → 0.96 V` 颗粒推后过氧化强因果句，也不使用「颗粒决定轴向配体」，与 `23aa751` 两分支对照表边界严格一致。
2. 修正了 `ClaudeWeb_replies_20261120.md` 22:20 中「`axial OH holds the Mn atom in the N4 plane`」的方向性笔误，明确写清 `0.44 Å` 离面 → 对侧吸附拉回平面 → 几何形变代价（较 `84143b6` 的「更大畸变」更准确具体）。
3. 保留现稿 `238 h / 96.5%` 与各对照极限电位（`0.52 / 0.78 / 0.26 / 0.34 V`），直接匹配现稿标题 *Operating-State Axial Hydroxyl Ligation Balances Intermediate Binding at Mn Sites for Oxygen Reduction*。


---

## 定稿迭代 v2（去抽象词版，2026-11-20 22:48）

按用户反馈拿掉 `structural reorganization`（结构重组）与 `energetic penalty`（能量代价）两个抽象词，保留全套具体几何位移与能量收支表述（主选写法 A，另附写法 B 备选），全篇约 225 词。

### 英文正文（写法 A 主选）

Metal particles are common in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet activity is usually attributed to bare single-atom sites alone. What surface state these composite catalysts adopt under working conditions, and how it regulates intermediate binding, remains unclear. Here, we prepare an FeCoMn–NC catalyst in which FeCo alloy particles coexist with dispersed Mn–N₄ sites. In 0.1 M KOH, FeCoMn–NC achieves an oxygen reduction reaction (ORR) half-wave potential of 0.885 V versus the reversible hydrogen electrode (RHE) and retains 96.5% of its initial current over 238 h. Operando infrared spectroscopy shows that surface species evolve with potential, indicating that the ORR proceeds on a covered rather than bare surface. Potential-dependent surface coverage calculations identify O*-covered FeCo particles and axially OH-ligated Mn single atoms at 0.78 V versus RHE. The axial OH pulls Mn out of the N₄ plane, while adsorption of ORR intermediates on the opposite side pulls Mn back toward the plane. Pulling Mn back against the axial OH consumes part of the binding energy without substantially weakening the local Mn–adsorbate bond, thereby alleviating the overly strong intermediate binding of the unligated Mn site. Consequently, OH* removal becomes downhill while OOH* formation remains nearly thermoneutral at 0.78 V, yielding a balanced ORR free-energy profile that places FeCoMn–NC near the apex of the activity volcano and accounts for its high measured activity.

### 中文直译（写法 A 主选，无中文冒号与分号）

热解金属–氮–碳（M–N–C）催化剂中金属颗粒十分常见，但催化活性通常只归因于裸露的单原子位点。这类复合催化剂在工作条件下会呈现怎样的表面状态，以及它如何调控中间体结合，目前仍不清楚。在此，我们制备了一种 FeCo 合金颗粒与分散 Mn–N₄ 位点共存的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的氧还原反应（ORR）半波电位达到 0.885 V（相对于可逆氢电极 RHE），并在 238 h 运行后保持初始电流的 96.5%。原位红外光谱表明，表面物种随电位演变，说明 ORR 发生在被覆盖的表面而非裸表面上。电位依赖的表面覆盖计算在 0.78 V（相对于 RHE）下识别出被 O* 覆盖的 FeCo 颗粒以及带轴向 OH 配体的 Mn 单原子。轴向 OH 将 Mn 拉出 N₄ 平面，而 ORR 中间体在对侧的吸附又将 Mn 拉回平面附近。逆着轴向 OH 拉回 Mn 会消耗一部分结合能，而并未显著削弱局域的 Mn–吸附物成键，从而缓解了无轴向配体 Mn 位点过强的中间体结合。结果是，在 0.78 V 下 OH* 脱附变为下坡过程，同时 OOH* 生成保持接近热中性，形成了平衡的 ORR 自由能分布，使 FeCoMn–NC 位于活性火山图顶点附近并解释了其较高的实测活性。

### 写法 B 机理句备选（学术书面语）

- **英文**：The axial OH displaces Mn from the N₄ coordination plane, while adsorption of ORR intermediates on the opposite side drives Mn back toward the plane. Restoring Mn toward the plane offsets part of the adsorption energy while leaving local Mn–adsorbate interactions nearly unchanged, thereby alleviating the excessively strong intermediate binding of the unligated Mn site.
- **中文直译**：轴向 OH 使 Mn 偏离 N₄ 配位平面，而 ORR 中间体在对侧的吸附又促使 Mn 向平面内回移。使 Mn 向平面回移抵消了一部分吸附能，同时局域 Mn–吸附物相互作用几乎保持不变，从而缓解了无轴向配体 Mn 位点过强的中间体结合。

### 口径自查清单

- 禁用 `"structural reorganization"` / `"energetic penalty"` / `"operating"` / `"must"`：已全部剔除；
- 不越过 `T039` 电子态边界（不写 `0.48/0.49 → 0.96 V` 强因果），不把 `dz²` 写成原因；
- 符合个人写作标点规范（直译段零中文冒号、零中文分号）。
