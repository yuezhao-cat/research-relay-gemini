# 论文主线复核：与今天拆解的顶刊相比差在哪、能学什么（Antigravity，2026-11-20 20:10）

核查对象：现行正文 `manuscript/FeCoMn_Manuscript_revised_20261119_2255_plaintext.txt`（下文行号均指此文件）。
对照对象：今天从本地 Zotero 读过全文的 Wan NC 2022、Han NC 2021、Liu & McCrory NC 2019、Ishiki NC 2025、Zhao Nat. Catal. 2025、Jin Nat. Catal. 2021、Wang NC 2024、Su Nat. Catal. 2023、Wu Angew 2025、Jin Angew 2026、Zhang JACS 2024/2025、Wang JACS 2019。
原则：只用现有数据；不提 Cdl/ECSA（赵月 2026-09-18 已定）；不改 Word。

---

## 一、现行主线（按正文原样概括）

FeCoMn–NC 活性最高（E1/2 0.885 V，Tafel 40 mV/dec）→ 原位红外显示表面物种随电位变化 → 算覆盖度：0.78 V 下 FeCoMn–NC 为 8O* + Mn–OH，Mn–NC 为 Mn=O，FeCo–NC 为 8O* → 四步自由能 U_L 0.78 / 0.34 / 0.26 V，排序与实测一致 → 图 6：d 带中心解释不了，差别在轴向配体（Mn–OH −ICOHP 2.64 eV，Mn=O 8.03 eV；磁矩差大）→ Mn–OH 上 OOH* 结合更强，处于火山顶 → 结论：颗粒决定邻近 Mn 的轴向配体。

主线骨架是对的（先定工作态，再在工作态上算活性，和 Wang JACS 2019 同一路数）。问题在下面几处。

---

## 二、核查出的问题（按严重程度排）

### 问题 1（新发现，最严重）：Wan NC 2022 已经报道过"团簇让相邻单原子带上轴向 OH"，正文没引

Wan 等 Nat. Commun. 2022, 13, 2963（10.1038/s41467-022-30702-z），本地 PDF 原文：
> "When the iron cluster is introduced, Fe–N4/Fe4–N6 shows strong adsorption to OH to the extent that a permanent OH ligand is grafted on Fe–N4. This OH ligand optimizes the binding strength of the other side of the Fe–N4 site to the ORR intermediates, greatly reducing the limiting energy barrier to 0.35 eV."
> Discussion："The iron cluster introduces an OH ligand on the satellite Fe–N4, thus lowering the ORR energy barrier and increasing the intrinsic activity of the Fe–N4 site by 60%."

这与正文第 118–121 行"FeCo particles cause the adjacent Mn single atoms to be coordinated by an axial OH, and this axial OH gives these Mn single atoms moderate binding"几乎同一句话。正文参考文献 1–29 中没有这篇（已检索 "Wan, X"），只引了 Huang Angew 2022（ref 8，团簇改变电荷分布）。审稿人只要知道 Wan 2022，就会判定核心结论已有先例。

我们和 Wan 2022 的真实区别（都有数据支撑）：
| | Wan NC 2022 | 本文 |
|---|---|---|
| OH 怎么来的 | 静态 DFT，团簇存在时 OH 吸附很强，直接假定挂上 | 电位依赖的覆盖度热力学（图 5），在 0.78 V、pH 13 下比较 OH 与 O 的竞争 |
| 对照态 | 只比裸 Fe–N4 与带 OH 的 Fe–N4 | 三种状态都有：裸 Mn（太强）、Mn–OH（适中）、Mn=O（太弱）；无颗粒时得到的是 Mn=O 而不是裸 Mn |
| 颗粒表面 | 裸 Fe4 团簇 | 颗粒本身被 8 个 O* 覆盖 |
| OH 为什么能调结合 | 只写"optimizes the binding strength" | 有形变/相互作用拆分与 Mn 位置数据（T041、T042），能定量说明为什么调到适中 |

**结论**：新意必须从"颗粒使 Mn 带 OH"收窄为"在工作电位覆盖下，颗粒决定 Mn 停在 OH 还是被氧化到 O；OH 通过几何形变代价把结合调到适中"。引言必须引 Wan 2022 和 Ishiki NC 2025 再划边界。

### 问题 2：标题和结论写"颗粒决定"，但因果对照还没做完

- 标题第 1–2 行"FeCo Particles Determine the Axial Ligand"，第 61、118、408 行同样是因果句。
- 现有证据是 FeCoMn–NC 模型（OH 比 O 稳定 0.18 eV）对比 Mn–NC 模型（O 比 OH 稳定 0.30 eV）。T039 任务书第 6 行写明：两者载体几何不同（T038b 中 Mn Bader 差 −0.040 e），所以现在的差别不能只归给颗粒。
- T039（同一几何只删颗粒）尚未交付（`from_agent/` 下无 T039 目录）。
- 顶刊做法：Han 2021 证明三个样品初态结构相同后才比较活性；Ishiki 2025 先用 XRD、Raman 证明加 Pt 前后碳基底一样；Jin 2021 用 10 个间距点。共同点是先锁住其他变量，再把差别归给唯一变量。
- **处理**：T039 出结果前，标题和结论里的 "Determine" 不能定稿。T039 翻转则保留；不翻转则改成"颗粒与 Mn 共存的体系中，Mn 在工作电位下带 OH"这类描述句。

### 问题 3：正文 7 处写"adjacent / next to / neighboring"，但没检验距离

第 51、61、107、119、363、399、408 行。共享记忆中的已定口径是"不写相邻（未检验距离依赖）"，现行稿与此冲突。Jin Nat. Catal. 2021 说明，要说"相邻才起作用"必须有距离依赖数据（他们用 10 个间距、找到约 1.2 nm 阈值）。**处理**：改成 "the Mn single atoms in FeCoMn–NC" 一类写法，零成本。

### 问题 4：图 6 缺"去掉原因、效果消失"这一步，留着最明显的漏洞

- 正文第 332–349 行只比较 Mn–OH 与 Mn=O，结论是"Mn–OH 键弱，所以 Mn 对 OOH* 结合更强"。
- 审稿人会接着问：那没有轴向配体的裸 Mn 不是更强、更好吗？T032 已有答案：同一 8O* 背景去掉 OH，U_L 从 0.78 V 掉到 0.52 V（OH* 太强）。这个数现在不在正文里。
- 顶刊做法：Wan 2022 图 5c 把 Fe–N4、Fe–N4/Fe4–N6、Fe–N4–OH/Fe4–N6 三个态并排；Liu & McCrory 2019 用七组对照逐个剥离一级配位和外层环境；Perutz 体系里断开近端组氨酸后亲和力上升。都是"三态对照"或"去因对照"。
- 我们已有的第二层解释（T041 形变拆分：OH* 减弱 0.34 eV 中约 0.24 eV 来自形变；T042：OH 预先把 Mn 拉出平面约 0.44 Å，吸附时回到平面）也没进正文。
- **处理**：图 6 段改为"裸 Mn 太强 / Mn–OH 适中 / Mn=O 太弱"三态并列，再用 T041、T042 说明 OH 为什么削弱得恰好。数据都已有，零新算。

### 问题 5：原位红外到覆盖度计算的逻辑衔接偏弱

- 摘要第 47–49 行、正文第 103–105 行："红外显示表面物种随电位变化，所以我们计算了覆盖度"。红外看到的是界面水和 1215 cm⁻¹ 的 OOH*，没有看到 Mn–OH（今天按 −0.084 V 重新扣参比，995–1080 cm⁻¹ 和 3520–3750 cm⁻¹ 都没有孤立峰）。
- 1215 cm⁻¹ 附近与 Nafion 的 C–F 区重叠；1.116 V、1.016 V 已有响应。目前正文把它直接定为 OOH*（第 259–260 行，引 ref 20、21）。
- 顶刊做法：Zhao 2025 用 CO 探针红外比较五个分子的结合；Jin Angew 2026 用 H/D 同位素、界面水高斯分峰和对照样（无颗粒样品中峰缺失）来证明红外信号归属。都有对照或探针排除干扰。
- **处理（零成本）**：红外只用于两件确定的事：OOH* 支持缔合路径、界面物种随电位变化；不暗示红外看到了 Mn 的配体。若有 Nafion 空白或无催化剂空白谱，可在 SI 补一张对照排除 C–F 干扰（需查是否有原始文件）。

### 问题 6：计算与实验只对上了排序，量级差没交代

- 第 309–312 行只说 U_L 排序与 E1/2 排序一致。U_L 差约 0.5 V，E1/2 只差 21–45 mV，审稿人会看到。
- 顶刊做法：Wang JACS 2019 用微动力学把工作态自由能转成理论半波电位（约 0.88 V）再和实验比；Zhang JACS 2024/2025 把模拟 jK/TOF 和实验并排，并比较新旧模型谁更吻合。
- **处理**：两种选一。(a) 零机时微动力学，用已有自由能给出理论 jk(U) 与 Tafel，和实测比；(b) 至少加一句说明：对照样品还有氮掺杂碳本底的贡献，计算比较的是金属位点本身。不写成防御段。

### 问题 7：第 210–211 行"kinetic current ... reflects the intrinsic activity"说过头

几何面积归一的 jk 只扣除了传质，没有按活性位数量归一（没有可靠 ICP，也没有位点密度测量）。Wan 2022 用亚硝酸根吸附剥离测位点密度 SD 和 TOF，Jin 2021、Wu 2025 用 SI-SECM，才敢说 intrinsic。**处理**：改成 "is corrected for mass transport"，删 "therefore reflects the intrinsic activity"。不涉及 Cdl。

### 问题 8：已定要删的一句

第 225–227 行"larger capacitive current ... larger electrochemically accessible surface area"，按 20:15 决定删除，图 S8 保留作 O2/N2 对比。

### 附：不要用作证据的一处

第 186–188 行 Mn 第一壳层配位数 4.9 ± 0.6。数值上可容纳 N4 + 1 个轴向 O，但这是非原位测试、误差 ±0.6，CW2-16 已撤回把它当轴向 OH 证据的说法，共享记忆也明确不能为目标配位数挑 σ²。保持现在的中性写法。

---

## 三、六步证据链对照（✓ 有，△ 部分，✗ 没有）

| 步骤 | 顶刊做法（例） | 本文现状 | 差距 |
|---|---|---|---|
| 1 指出静态模型不行 | Wang 2019、Jia 2015：裸位点算出的结果与实验不符 | △ 有 T038（初始结构中颗粒几乎不改变 Mn），但正文没用 | 把 T038 放进图 5 段开头，零成本 |
| 2 确定工作态 | Zhao 2025：原位 XANES + 三种磁测；Han 2021：原位 EXAFS 键长对上 DFT | △ 只有计算覆盖度；实验无 Mn 状态测量 | 现有数据补不了；T043 若无收获，正文不写成已证 |
| 3 单变量对照 / 去因 | Wan 2022 三态并列；Liu 2019 七组对照；Ishiki 2025 先证明基底相同 | △ 有 T032（去 OH），正文未用；颗粒的单变量对照 T039 未完成 | 去 OH 写进正文；等 T039 |
| 4 测出中介物理量 | Wang 2024 Stark 测电场；Ishiki 2025 穆斯堡尔测 D1 存量；Zhao 2025 测自旋 | ✗ Mn 价态、自旋、离面都没有实验值 | 最大缺口，现有数据补不了，只能收窄声明 |
| 5 定量关联 / 连续变量 | Jin 2021 十个间距；Wang 2024 四个曲率；Zhao 2025 TOF 对 S=5/2 含量线性 | ✗ 三个样品三类状态 | 可用的计算连续量：电位（覆盖度随电位）、颗粒 0/5/8 O*（T026）；不写普适描述符 |
| 6 排除其他解释 | Ishiki 2025 用 HPRR 排除"Pt 只是分解 H2O2"；Wan 2022 排除团簇本身是活性位 | △ T038 排除"颗粒向 Mn 大量转移电荷"；FeCo–NC 活性低说明颗粒本身不是主活性位 | 正文写清这两条排除；对照样无 RRDE，不能说已排除 H2O2 差异 |

---

## 四、每篇能直接学的东西

| 文献 | 学什么 | 用在本文哪里 |
|---|---|---|
| Wan NC 2022 | ① 必须引用并划边界；② 三态并列的自由能图（裸 / 团簇 / 团簇+OH）；③ 一句话写法："This OH ligand optimizes the binding strength of the other side of the site" | 引言第 2 段；图 6 第一步 |
| Han NC 2021 | 适中的解释写成"两个相反效应的平衡"：形变既加强新的 Cu–O 键、又削弱原有 Cu–N 键，最优点在中间。正好对应我们"保住成键、付出形变代价" | 图 6 机理段的句式 |
| Liu & McCrory NC 2019 | 把"一级配位（轴向配体）效应"和"外层环境效应"分开论证，并用一个动力学量（KIE）判断决速步是否变了 | 写作上把"颗粒的作用"与"轴向 OH 的作用"分两层，不混在一句里 |
| Ishiki NC 2025 | ① 先证明加颗粒前后基底相同；② 主动排除最容易想到的替代解释；③ 坦白模型局限（"More theoretical work is however desirable..."）；④ 新意边界：他们的 Pt 基本不改变 OOH 与 Fe 的结合，作用在稳定性 | 引言边界；讨论段写局限 |
| Zhao Nat. Catal. 2025 | 高自旋 OH 配位是活性态已有先例（正文已引 ref 10），我们的贡献不能放在"发现 Mn–OH 高自旋有利" | 引言，避免撞车 |
| Wang JACS 2019 | 工作态自由能 → 微动力学 → 理论半波电位，和实验比数值而不只比排序 | 问题 6 |
| Jin Nat. Catal. 2021 | 要说"相邻"必须有距离依赖 | 问题 3 的依据 |
| Zhang JACS 2025（李昊组，ref 12） | 弱结合金属上 O 可能在 M–N 桥位；我们已核查 Mn–NC 的 O 优化后回到顶位，可在 SI 写一句 | SI，预防审稿问题 |

---

## 五、建议的执行顺序

**现在就能做（零成本，只改文字，需赵月同意后再动 Word）**
1. 引言第 2 段补引 Wan NC 2022、Ishiki NC 2025，按第二节问题 1 的表格划边界。
2. 7 处 adjacent / next to / neighboring 改掉。
3. 图 6 段改为三态并列（T032 的 0.52 V 进正文），接 T041、T042 的形变解释。
4. 图 5 段开头放 T038。
5. 第 210–211 行 intrinsic 删去；第 225–227 行电容句删去。
6. 红外段只保留两条确定结论。
7. 计算与实验量级差：加一句说明，或做零机时微动力学。

**等 T039**
- 翻转：标题和结论保留 "Determine"，补一句"同一载体几何下去掉颗粒，Mn 改为偏好 O"。
- 不翻转：标题改为描述句，颗粒写成工作态环境的组成部分，不写因果。

**现有数据补不了、正文不能写成已证的**
- Mn 价态、自旋、离面位移的实验测量；
- 活性随某个量连续变化的定量关系；
- 颗粒通过电场、刚度还是电子起作用。
