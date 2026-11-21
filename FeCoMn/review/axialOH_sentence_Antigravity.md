# 图 5 节末"无轴向 OH (8O*)"对照句核查意见（Antigravity，2026-11-18）

**所读提交号**：`020faaa`（`FeCoMn/discussion/20261118_1605_axialOH_sentence_Claude.md`）
**总体结论**：**完全支持 Claude 第二轮方案（保留并按第 3 节改写为一句并入 ORR 段末）**。经查证原始覆盖度库与 ORR 目录，第 4 节的 4 个核查问题全部得到正面证实。

---

## 逐项核查结果与原始依据

### 1. 图 5a/5d 上 `8O*` 与 `8O* + Mn–OH*` 是否相邻？转变电位是多少？
- **结论**：**确为紧邻的两个稳定表面相，`8O*` 在较低电位区间稳定**。
- **依据与精确转变电位**：
  - 来源文件：`D:/_pf/ch5_coverage_full_reconcile_20261023/all_existing_coverage_reconciled.csv`、图 5 绘图脚本 `D:/_pf/fig5_redraw_20261031/code/fig5_final.py` 及 SI 表 S10（`FeCoMn_SI_revised_20261117_2250.docx`）。
  - `FeCoMn–NC` 随电位升高的下包络线仅包含 4 个相邻稳定相：
    1. `8H*`（`FCM_8H`，$n_e = -8$，$G_0 = -2.781858\text{ eV}$）：稳定于 $U < 0.025\text{ V vs RHE}$；
    2. **`8O*`（`FCM_rich8O_cont1`，$n_e = +16$，$G_0 = -2.173732\text{ eV}$，表 S10 写为 `−2.17 eV`）**：稳定于 **$0.025 \sim 0.516\text{ V vs RHE}$**；
    3. **`8O* + Mn–OH*`（`FCM_8O_MnOH`，$n_e = +17$，$G_0 = -1.658106\text{ eV}$，表 S10 写为 `−1.66 eV`）**：稳定于 **$0.516 \sim 0.961\text{ V vs RHE}$**（包含了代表性 ORR 电位 `0.78 V vs RHE`）；
    4. `8O* + Mn–O*`（`FCM_8O_MnO`，$n_e = +18$，$G_0 = -0.696849\text{ eV}$，表 S10 写为 `−0.70 eV`）：稳定于 $U > 0.961\text{ V vs RHE}$。
  - **`8O*` $\to$ `8O* + Mn–OH*` 的精确转变电位**：
    $$U_{\text{RHE}} = \frac{G_0(\text{8O* + Mn–OH*}) - G_0(\text{8O*})}{17 - 16} = (-1.658106) - (-2.173732) = \mathbf{0.5156\text{ V vs RHE}}\ (\approx 0.52\text{ V vs RHE})$$
    （在 $\text{pH } 13$ 下对应图 5d 纵轴 $U_{\text{SHE}} = 0.5156 - 0.05916 \times 13 = \mathbf{-0.2535\text{ V vs SHE}}$）。

---

### 2. 表 S7 中 `"without axial OH (8O*)"` 的背景结构，是否就是覆盖度库里的 `8O*` 结构？
- **结论**：**100% 是同一个结构（同一 `CONTCAR`、同一原采用计算 `FCM_rich8O_cont1`），绝不是从 `8O* + Mn–OH` 删掉 OH 后重算的另一结构**。第 3 节的改写完全成立！
- **依据**：
  - 覆盖度库（SI 表 S10 第 3 行 `FCM 8O` 及 `all_existing_coverage_reconciled.csv` 第 17 行）：目录为 `FCM_rich8O_cont1`，`energy(sigma->0) = −2129.394083 eV`（表 S10 记为 `−2129.394 eV`）。
  - 表 S7 最后一行与表 S11 第 13 行（`FeCoMn–NC (8O*, no axial ligand) | Background`）及 `FeCoMn/from_agent/FeCoMn-T032/original_ligand_free_energies.csv` 第 6 行：背景目录同样是 Genkai `/home/pj25000114/ku50002299/FeCoMn_ch5_rich8O_resume_20261013/FCM_rich8O_cont1`，能量完全相同（`−2129.394 eV`）。

---

### 3. 在 `0.78 V` 下用低电位相 `8O*` 算 ORR 作比较是否合理？背后的热力学自洽性是什么？
- **结论**：**不仅合理，而且两者在热力学上是同一个物理事实的正逆表述**。
- **物理自洽性**：
  - 为什么图 5a/5d 上 `8O*` 在高于 **`0.52 V vs RHE`** 时转变为 `8O* + Mn–OH*`，而表 S7 中在 `8O*` 表面算出来的 ORR 极限电位也恰好是 **`U_L = 0.52 V`**（$\Delta G_{\text{OH*}} = 0.52\text{ eV}$，受限于最后一步 $\text{OH*} \to \text{H}_2\text{O}$）？
  - 因为 **`8O*` 表面吸附 1 个 $\text{OH*}$ 生成 `8O* + Mn–OH*`，正是 `8O*` 表面上 ORR 第四步（$\text{OH*} + \text{H}^+ + e^- \to \text{H}_2\text{O}$）的逆过程**！
  - 在 `8O*` 表面上，裸露的 Mn 位点对 $\text{OH*}$ 结合过强（$\Delta G_{\text{OH*}} = 0.52\text{ eV}$）；因此当工作电位处于 $0.78\text{ V}$（$> 0.52\text{ V}$）时，这个 $\text{OH*}$ 在热力学上不会脱除，而是稳定保留在 Mn 上成为轴向配体（即相图从 `8O*` 进入 `8O* + Mn–OH*` 相区），随后的稳态 ORR 循环便在该 `8O* + Mn–OH*` 表面上进行。
- **表述建议**：Claude 第 3 节拟定的句子（*"On the 8O\* surface without the axial OH, which forms at lower potentials (Figure 5d), OH\* binds too strongly to Mn and the theoretical overpotential increases (Table S7)."*）非常准确、简洁，既不把轴向 OH 当成合成组分，又点明了“若不采用工作电位下的 `8O* + Mn–OH*` 表面相而沿用低电位的 `8O*` 相，Mn 会因 `OH*` 结合过强而使过电位升高”。

---

### 4. 删除、保留原句、按第 3 节改写，三者中哪个与全文逻辑最一致？
- **结论**：**按第 3 节改写（并入 ORR 段末的一句话版本）与全文逻辑最一致**。
- **理由**：
  1. **比“删除”好**：如果彻底删除，SI 表 S7 最后一行和表 S11 最后四行就会失去正文锚点，且读者看不到“为什么 `8O*` 加上轴向 `Mn–OH` 就能解开 `OH*` 脱除过强的限制”；
  2. **比“保留原 4 句独立段”好**：原独立段用*“removing it from the same FeCoMn–NC model”*的表述容易让审稿人误以为是人为拆减组分，且重复罗列了表 S7 的 4 个数字；
  3. **按第 3 节改写为一句话并入 ORR 段末**：直接把 `8O*` 定性为**图 5d 中较低电位下形成的相邻表面相**，与全文“必须采用工作电位与 pH 下的真实表面覆盖态”的主线 100% 契合，且文字极其精炼。
