# FeCoMn 论文结论角色评估与改写方案（Antigravity，2026-11-22）

依据文件：`FeCoMn/discussion/REQUEST_Conclusion_20261122.md`、`FeCoMn/discussion/Gemini_brief_Conclusion_20261122.md`、`FeCoMn/manuscript/FeCoMn_Manuscript_revised_20261121_2200.txt`（全文含摘要、前言 P1–P3、图 5/6 正文与现行结论）、`FeCoMn/DECISIONS.md` 与 `FeCoMn/REDLINES_FROZEN.md`。本次只提交本评审文件，未修改 Word 或仓库内其他文件。

---

## 一、这篇论文的结论应承担什么角色

把定稿摘要、前言 P1–P3 与现行所有结论草稿并排对照后，可以看到现有版本集体卡壳的根本原因。摘要和前言第三段已经完整讲了两遍「从制备、性能、原位红外、工作条件表面覆盖到 0.78 V 反应步骤与火山图」的全流程故事，而结论在全篇中的分工应当与二者明确区隔。

1. **摘要的角色是独立内容提要**，面向尚未读正文的人，按研究顺序压缩交代背景缺口、实验、原位红外引出覆盖计算、0.78 V 下的表面态与反应步骤、火山图落点。
2. **前言的角色是立题与预告**。前言 P1 提出领域基本矛盾（M–N–C 活性受限于中间体结合过强阻碍脱附、过弱阻碍生成，需找到有效调控手段），前言 P2 抛出本文核心科学问题（热解 M–N–C 中颗粒与单原子常共存，现有分析只归功于单原子或仅停留在裸单原子模型上讨论颗粒电子效应，未考虑工作条件下颗粒与单原子都被电解液物种覆盖，颗粒与表面覆盖如何影响相邻单原子结合尚不明确），前言 P3 预告研究结果。
3. **结论的角色不是第三遍复述流程，也不是脱离机制的空泛拔高，而是「闭环定论与机制结晶」**。面向已经读完图 1–6 证据的读者，本文的结论需要精准完成四项任务。
   - **任务一（实验锚点，克制收束）**：以 `In summary` 开篇，简明交代制备了 FeCo 合金颗粒与 Mn 单原子共存的 FeCoMn–NC，只给核心实测锚点（0.1 M KOH 中 0.885 V 优于 Pt/C、FeCo–NC、Mn–NC，238 h 保持 96.5% 初始电流），不再复述表征与原位红外过程。
   - **任务二（正面闭合前言 P2，并标出相对 Wan 2022 的核心差异）**：直接落到工作电位和 pH 下的表面覆盖定论，交代 O* 覆盖的 FeCo 颗粒将 `Mn–OH` 向 `Mn=O` 转变从 `0.48 V` 移至 `0.96 V versus RHE`，从而在 ORR 期间为相邻 Mn 单原子守住轴向 OH，而无颗粒 Mn 形成 `Mn=O`。这是本文区别于 Wan 2022（未以工作电位/pH 覆盖相图界定氧化窗口，且体系为 Fe 团簇与 Fe–N4）的关键硬核贡献。
   - **任务三（结晶图 5–6 的双效机制，正面闭合前言 P1 的过强/过弱两难）**：去掉 0.44 Å、0.34/0.24/0.10 eV、0.78/0.34/0.26 V 等微观计算数字堆砌，用对称、直白的因果链讲清三态对照，即 `Mn=O` 双键占用成键能力导致 `OOH*` 过弱、无轴向配体导致 `OH*` 过强，而 FeCoMn–NC 中较弱的 `Mn–OH` 键留出 `OOH*` 成键能力，同时轴向 OH 将 Mn 拉出 N₄ 平面、对侧中间体吸附拉回平面并消耗部分结合能，最终平衡 `OOH*` 生成与 `OH*` 脱附并落于火山图顶点附近。
   - **任务四（立住属于本文独有的科学认识与设计意义，不空泛、不说教）**：收官句必须把「FeCoMn–NC 的具体结果」与「对同类 M–N–C 催化剂的普适机制认识」分开，直接给出前言 P2 的答案，即在颗粒与单原子共存的 M–N–C 催化剂中，工作条件下被覆盖的颗粒决定相邻单原子的轴向配体并由此调控中间体结合，该表面覆盖机制超越了裸位点模型对 ORR 催化的认识并指导催化剂设计。既不写 `should` 教训读者，也不泛化到「多组分电催化体系」冲淡本文价值，也不用 `clarifies how` 式的空壳元话语回避答案。

---

## 二、现有全部版本（导师返回版、V0–V4、C1–C12）分别差在哪里

### 整体诊断：为何所有版本都在「摘要重播」与「抽空失焦」两端摇摆

现有 18 个版本可以清晰归为四类偏差。第一类（导师返回版、V0）停留在旧稿或结果数字清单阶段，缺提炼且对读者说教。第二类（C1–C10、V1、C11）在试图去掉数字和去重时，反复丢掉 `0.48 → 0.96 V`、丢掉无轴向配体过强端、把 `Mn=O` 错写为 `Mn–O`，或结尾退回空壳句/泛化套话。第三类（C12、V2、V4）把三点独有价值装齐了，但骨架依然是按时间线把摘要再讲一遍，同时结尾要么把样品结果和一般认识揉成一团（V2），要么踩了 `This`、`must`、纯否定句 `not spectators` 与语法主语错位（C12、V4）。第四类（V3）为了避免复述摘要而矫枉过正，把实测稳定性和具体电子/几何因果抽成空洞名词短语，反而丢失了结论应有的证据分量。

### 逐版本核查明细

| 版本 | 核心长处 | 主要问题与差距 |
| :--- | :--- | :--- |
| **导师返回版（1116_2010）** | 篇幅紧凑，尝试从覆盖度、自由能、电子结构总括 | 已与最新定稿正文严重脱节。术语过时且踩红线（`dispersed Mn species`、`operating potential/conditions`、`should start from`）。机理对照写错（把避免过强结合归到 `FeCo–NC` 的 `OH*` 过强，而正文图 5h 中 `FeCo–NC` 是 `O*` 过强阻碍 `O*→OH*`），完全缺失颗粒推迟 `Mn–OH→Mn=O` 转变与 Mn 离面回拉机理，漏掉半波电位与稳定性却保留孤立计算数 `0.78 V` 与 `0.85 eV`。 |
| **V0（现 Word 1140）** | 事实准确，涵盖 `0.48→0.96 V` 与几何拉回 | 最像结果段压缩数字表，违背不堆计算数值原则（`0.48/0.96 V`、两次 `0.78 V`、`0.44 Å`、`0.34/0.24/0.10 eV`、`0.34/0.26 V`）。漏掉 238 h 稳定性与 0.1 M KOH。缺 `Mn=O` 占成键能力的过弱端解释，`Relative to overly strong binding...` 别扭。结尾 `should be analyzed` 对读者提要求。 |
| **C1（11:45 Claude）** | 首次去掉微观数字和 `should`，节奏变清爽 | 漏掉 `96.5%` 及与 Pt/C、FeCo–NC、Mn–NC 的对比。漏掉 `0.48→0.96 V` 转变电位（抹平与 Wan 2022 的核心边界）。未明写过弱端（`Mn=O` 占成键能力）与过强端（无轴向配体 `OH*` 过强）。踩红线：`must draw Mn back`、`These results`、`axial O` 未点出 `Mn=O` 双键。未呼应前言裸位点问题。 |
| **C2（11:50 Claude）** | 引入 `In summary` 与三态对比，补齐性能与稳定性 | 如赵月指出，完全未呼应前言问题且结构同构于摘要。漏掉 `0.48→0.96 V`。几何机理过简（`the shift of Mn toward the axial OH weakens OH* binding` 跳过对侧拉回消耗结合能的关键因果）。踩 `This work`，结尾 `offers a way to design...` 略空泛。 |
| **C3（11:58 Claude）** | 尝试通过对比裸单原子模型回应前言 | 把研究动机与计算过程（`To determine... we calculated...`）搬进结论，变成第三遍摘要。漏掉 `0.48→0.96 V` 与 `Mn=O` 占成键能力机制，仍带结果叙事腔（`At 0.78 V`），末尾用冒号拉长句。 |
| **C4（12:01 Gemini）** | 敏锐指出 C3 与摘要重复 | 自身仍沿用摘要流水账骨架，并引入硬伤。化学式笔误（`Mn–O bonding` 应为 `Mn=O`）。连用三处含糊指代（`It reaches`、`this balance`、`These results`）。漏 `0.48→0.96 V` 与对照组性能对比。结尾 `show how...` 为空壳元话语。 |
| **C5（12:02 Claude）** | 尝试首尾呼应裸单原子模型 | 漏掉 0.1 M KOH、与 Pt/C 等的对比、`O*-covered` 颗粒特征、`0.48→0.96 V` 以及火山图落点。写 `An axial O` 未写 `Mn=O` 双键，几何机理再次丢掉对侧拉回消耗结合能。踩 `These results`、冒号，且结尾 `do not capture` 带否定尾巴。 |
| **C6（12:04 Gemini，V1 前身）** | 语言较 C4 顺畅，补回 0.1 M KOH | 保留 `Mn–O` 笔误。`while shifting Mn...` 逻辑主语错误地挂在 `a weaker axial Mn–OH bond` 上而非 `the axial OH`。漏掉无轴向配体过强端参照、漏 `0.48→0.96 V`、漏对照组性能比较。踩 `This moderate binding`、`These results`，结尾 `clarify how...` 未给出实质结论。 |
| **C7（12:05 Claude）** | 修正了 C6 的 `Mn=O`、几何主语和 `This moderate binding` | 仍继承 C6 的结构短板。缺 `0.48→0.96 V`、缺无轴向配体过强端参照、缺对照组性能对比，保留空壳尾句 `These results clarify how...`，整体仍像摘要复述。 |
| **C8（12:08 Claude）** | 在 C7 基础上改掉了空壳尾句，开始落回裸位点对比 | 仍未补回 `0.48→0.96 V`、无轴向配体过强端和对照组性能对比。结尾仍落回否定从句 `that models of bare single atoms do not capture`，且前半段依旧按摘要顺叙。 |
| **C9 / C10（12:07 Gemini A/B）** | 调整了前两句衔接与紧凑度 | 完整继承 C6 全部硬伤，即 `Mn–O` 笔误、`while shifting` 主语错位、缺 `0.48→0.96 V`、缺无轴向配体过强端、缺对照组性能对比。C9 尾句 `is essential to capture how...` 既空壳又含变相说教，C10 用 `This balance` 且以空壳 `clarifies how...` 作结。 |
| **C11（12:12 Gemini）** | 尝试给结论增加层次收尾 | 保留 `Mn–O` 笔误、`while shifting` 主语错位、缺 `0.48→0.96 V` 与无轴向配体参照，还新增 `Examining... shows` 悬垂感、冒号和 `This difference / these findings`。最大败笔是结尾拔高到 `across multicomponent electrocatalytic systems`，变成放之四海而皆准的套话，冲淡本文独有价值，且 `requires moving beyond` 变相向读者提要求。 |
| **V1（Gemini 修订最新版）** | 删去了 C11 末尾的多组分泛化套话 | C11 其余问题几乎全部残留，即 `Mn–O` 笔误、`Examining... shows`、`while shifting` 主语不清、`This difference` 与冒号、漏 `0.48→0.96 V`、漏无轴向配体参照、漏对照组性能对比。结尾 `demonstrates that accounting for... reveals how...` 叠了两层元话语，依然没说出结论答案本身。 |
| **C12（12:13 Claude，80 分）** | 首次完整装齐赵月强调的三点独有价值，无微观数字堆砌 | 共 9 句偏碎，结构仍是加长版摘要重播。第 4 句 `This axial ligand prevents...` 为空壳过渡句。踩多条红线，包括 `This axial ligand`、`must pull Mn back`、纯否定修辞与冒号 `are thus not spectators:`。未提优于 Pt/C 等对照组，也未闭合前言裸位点模型问题。 |
| **V2（Claude 版 B，80 分）** | 压缩到 6 句，去除了 `must` 和 `not spectators`，三点价值均在 | 依然未完成结论角色切换。开篇缺结语标识且漏对照组对比，第 2 句仍是计算汇报腔，第 3 句 `balances... in two ways` 仍是教科书空壳过渡句。机制对照顺序倒置（先讲 `Mn–OH` 再反衬 `Mn=O` 和无轴向配体），`consumes binding energy to pull Mn back` 语意略别扭。最关键的是没有回应前言的裸位点局限，且把一般性结论和单个样品火山图顶点粘在末句里，缺少真正独立站起来的意义收尾。 |
| **V3（Claude 答案先行版）** | 意识到不能逐句复述摘要，试图直接回答前言问题 | 矫枉过正导致论证失重。开篇抛弃研究体系锚点直接悬空断言。删掉了 238 h 稳定性与 `0.48→0.96 V` 关键边界。把电子与几何核心机制压缩成空洞词组 `Through bonding capacity and out-of-plane geometry`，审稿人看不到具体物理因果。踩红线 `consistent with`，用 `axial O` 未写 `Mn=O`，尾句 `leave out` 偏否定且生硬。 |
| **V4（12:16 Gemini 终稿）** | 保留了 C12 的三点价值与 `0.48→0.96 V` | 本质上是 C12 照搬加局部改坏。原样保留了 C12 的 `This axial ligand`、空壳过渡句、纯否定 `are thus not spectators`（仅把冒号换成分号）及 8 句摘要重播感。第 6 句改回逻辑主语不清的 `while shifting Mn...` 并用了拟人强迫词 `forces`。第 3 句多塞回孤立的 `0.78 V`，第 2 句仍缺对照组性能对比。 |

---

## 三、推荐版本（英文 + 完整中文直译）

### English Conclusions

In summary, we prepared an FeCoMn–NC catalyst in which FeCo alloy particles coexist with Mn single atoms. In 0.1 M KOH, FeCoMn–NC reaches a higher ORR half-wave potential (0.885 V versus RHE) than Pt/C, FeCo–NC, and Mn–NC, and retains 96.5% of its initial current after 238 h. Surface-coverage analysis at the working potential and pH shows that O*-covered FeCo particles shift the Mn–OH to Mn=O transition from 0.48 to 0.96 V versus RHE, so adjacent Mn single atoms retain an axial OH during the ORR whereas Mn without particles forms Mn=O. In Mn–NC, the strong axial Mn=O double bond occupies most of the bonding capacity of Mn and makes OOH* binding too weak, whereas Mn without an axial ligand binds OH* too strongly. In FeCoMn–NC, the weaker axial Mn–OH bond leaves Mn enough bonding capacity for OOH* formation. Meanwhile, the axial OH pulls Mn out of the N₄ plane, so opposite-side intermediate adsorption draws Mn back toward the plane and consumes part of the binding energy. The axial OH therefore balances OOH* formation and OH* removal, placing FeCoMn–NC near the apex of the activity volcano. In M–N–C catalysts where metal particles coexist with single atoms, covered particles under working conditions determine the axial ligand of adjacent single atoms and thereby regulate intermediate binding, a surface-coverage mechanism that extends understanding of ORR catalysis beyond bare-site models and guides catalyst design.

### 完整中文直译

综上所述，我们制备了一种 FeCo 合金颗粒与 Mn 单原子共存的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 达到了高于 Pt/C、FeCo–NC 和 Mn–NC 的 ORR 半波电位（0.885 V，相对于 RHE），并在 238 h 后保持 96.5% 的初始电流。工作电位和 pH 下的表面覆盖分析表明，O* 覆盖的 FeCo 颗粒将 Mn–OH 向 Mn=O 的转变从 0.48 移至 0.96 V（相对于 RHE），因此相邻 Mn 单原子在 ORR 期间保持轴向 OH，而无颗粒的 Mn 则形成 Mn=O。在 Mn–NC 中，强轴向 Mn=O 双键占用了 Mn 大部分成键能力，使 OOH* 结合过弱，而无轴向配体的 Mn 对 OH* 结合过强。在 FeCoMn–NC 中，较弱的轴向 Mn–OH 键为 Mn 留出了足够的成键能力以生成 OOH*。同时，轴向 OH 将 Mn 拉出 N₄ 平面，因此对侧的中间体吸附将 Mn 拉回平面方向并消耗部分结合能。轴向 OH 因而平衡了 OOH* 生成与 OH* 脱附，使 FeCoMn–NC 位于活性火山图顶点附近。在金属颗粒与单原子共存的 M–N–C 催化剂中，工作条件下被覆盖的颗粒决定相邻单原子的轴向配体，进而调控中间体结合，该表面覆盖机制超越了裸位点模型对 ORR 催化的认识，并指导催化剂设计。

---

## 四、与摘要/前言的区分及写作规则逐条自检

1. **与摘要、前言的角色区分**
   - **去流程化**：删去摘要和前言 P3 中的原位红外过渡、0.78 V 逐步骤 ΔG 展开等研究过程叙述，直接呈现定论。
   - **双闭环回应前言**：第 4–7 句以「过弱（Mn=O）与过强（无轴向配体）对比 → 轴向 Mn–OH 双效化解 → 平衡 OOH* 生成与 OH* 脱附」直接闭合前言 P1 的吸附强弱两难。第 3 句与第 8 句以「工作电位和 pH 下表面覆盖（0.48 → 0.96 V）」和「工作条件下被覆盖颗粒决定轴向配体，超越裸位点模型认识」直接闭合前言 P2 的核心科学问题。
   - **样品结果与普适意义分离**：第 7 句把 `FeCoMn–NC` 落在火山图顶点收住，第 8 句专门上升到「颗粒与单原子共存的 M–N–C 催化剂」并紧扣表面覆盖与轴向配体调控，既不落回单样品汇报（修正 V2），也不空泛拉高到「多组分电催化体系」（修正 C11）。
2. **三点独有价值与 Wan 2022 区别核验**
   - 覆盖相图窗口（0.48 → 0.96 V versus RHE，工作电位与 pH）、O* 覆盖的 FeCo 颗粒加 Mn 单原子、Mn=O vs Mn–OH 成键能力分配与 Mn 离面/拉回几何消耗结合能三点全部完整落位。
3. **规则与红线零违规自检**
   - **句数与篇幅**：共 8 句（落在 10 篇顶刊结论 5–8 句规范内），每句主语均为具体实体（`we`、`FeCoMn–NC`、`Surface-coverage analysis`、`O*-covered FeCo particles`、`the strong axial Mn=O double bond`、`Mn without an axial ligand`、`the weaker axial Mn–OH bond`、`the axial OH`、`opposite-side intermediate adsorption`、`The axial OH`、`covered particles under working conditions`、`a surface-coverage mechanism`）。
   - **零计算数字堆砌**：正文仅保留实测锚点（`0.1 M KOH`、`0.885 V`、`96.5%`、`238 h`）与核心相变电位窗（`0.48 to 0.96 V versus RHE`），未引入 `0.44 Å`、`0.34/0.24/0.10 eV`、`0.78/0.34/0.26 V`、`0.52 V`、`0.85 eV`、`0.516 V` 或 ICOHP 数值。
   - **零禁词与零违规标点**：无 `first/novel`、无防御性措辞（无 `consistent with/tentatively`）、无纯否定句（全文零 `not/no/never`）、无 `should/must/forces/requires`、无 `operating/reorganization/energetic penalty/dz²`、无裸 `It/This/These` 指代、无 `Mn–O` 笔误、Mn 回移严格写 `back toward the plane`、英文无冒号分号与破折号、中文直译零全角冒号/分号/破折号/中文双引号。
