# FeCoMn-T045 前言新插参考文献逐字核查与全文重编号审计报告（Antigravity）

- **核查任务单**：`FeCoMn/to_agent/FeCoMn-T045_intro_refs_verify.md`（提交 `ee399e0` / `0b7765d`）
- **核查对象**：
  - 正文 2150 版：`FeCoMn/manuscript/FeCoMn_Manuscript_revised_20261121_2150.txt`
  - 附件文本基准：`FeCoMn/manuscript/FeCoMn_SI_revised_20261121_2040.txt`（及 `0b7765d` 提交说明的 `FeCoMn_SI_revised_20261121_2150.docx`）
  - 图件标签核查：`FeCoMn/manuscript/FeCoMn_Manuscript_revised_20261121_2025.docx` 内嵌 `Figure 3` 原图（`word/media/image3.png`）
- **核查方法**：直接打开本地 Zotero（`D:\Zotero\storage`）归档的原文 PDF 逐字比对支持句、页码与章节；通过 CrossRef API 核对两篇新文献书目信息；用脚本审计 `2055 -> 2150` 全文首次出现顺序、参考文献列表（1–40）以及 SI 中对正文参考文献编号的交叉引用。不修改任何 Word 文件、正文讨论稿和任务单。

---

## 核心结论摘要

1. **前言第二段四处引文核查结论**：
   - **原 [D]（Refs 6–10）**：T036 已核实，本次复核无误。其中 **Ref 8**（Wang 2020 *Adv. Mater.*）为纯碳骨架边缘缺陷控制变量研究，强支持"carbon framework"调控；Ref 7/9/10 均支持，Ref 6 为部分支持（单金属 OH 修饰主要提升 OER，双金属提升 ORR）。
   - **原 [F]（Ref 11：`Wan 2022 Nat. Commun.`）**：**部分支持（存在两处措辞边界）**。原文证明金属含量升高时热解产物可从单原子向颗粒转变，且石墨碳层包覆的 Fe 颗粒可在**酸性介质中留存**；但并未写明"金属原子极易团聚（readily aggregate）"，也未直接写明"酸洗（acid leaching）之后仍留存"（正文写 `"in acids"` 指酸性环境存在，酸洗仅用于制备 CQD 载体）。文末给出了**最小改动补强方案**（不增引可并引已有 `9,11,13`；若增引 1 篇可在 Zotero 加入 `Xia 2016 Nat. Energy`）。
   - **原 [G]（Refs 12–13：`Zitolo 2015 Nat. Mater.`、`Li 2018 Nat. Catal.`）**：**均为部分支持（属于“例证型”，而非直接论证“学界通常只归因于单原子”的“综述/普遍判断型”）**。Zitolo 2015 是高活性含颗粒 Fe–N–C 体系中将颗粒判定为 ORR 无活性、归因于单原子的经典例证；但 **Li 2018 存在风险**：其最终样品不含任何 Mn 颗粒（与前句 `such catalysts` 所指的“颗粒与单原子共存催化剂”不符）。若需直接支撑 `"usually attributed"` 这一全称判断，建议增引 Zotero 已有综述 **`Zhao et al., Angew. Chem., Int. Ed. 2021, 60, 4448–4463`**（DOI: `10.1002/anie.202003917`）。
   - **原 [E]（Refs 14–17：`Wang 2019 JACS`、`Zhao 2025 Nat. Catal.`、`Yang 2023 Chem. Commun.`、`Hansen 2008 PCCP`）**：**整体成立**。Refs 14、15 分别从微动力学理论和原位 XANES 实验强支持单原子在工作条件/电解液下形成轴向 OH 覆盖；Ref 17 强支持金属表面在工作电位与 pH 下形成表面 Pourbaix `O*/OH*` 覆盖（注：计算模型为延展 `(111)` 单晶面而非纳米颗粒，作为金属表面覆蓋奠基工作合理）；Ref 16 主体为双原子催化剂，其引言明确综述了电解液水解物种对金属表面和单原子的电位/pH 依赖表面覆盖（部分支持）。
2. **两篇新文献书目信息（Ref 8、Ref 11）**：经原文 PDF 首页与 CrossRef API 交叉核对，作者、标题、期刊、年份、卷号、文章号及 DOI **100% 准确无误**。
3. **正文 1–40 重编号与一致性审计**：正文 `2150` 版首次出现顺序**严格为 `1` 到 `40` 递增**，无跳号、无孤立文献；文末参考文献表 `(1)`–`(40)` 连贯、无重复 DOI（原两处 `(36)` 已修正）；正文结果与方法段所有旧编号向新编号的双射全部正确。
4. **⚠ 重要发现：SI 中仍有 3 处（共 10 个）正文文献编号漏改**（`0b7765d` 仅修正了 Section 2.5 的 `main-text ref. 12 -> ref. 3`）：
   - **Section 1 Characterization（SI L177）**：`Larch²⁵` 应改为 `Larch²⁶`；`σ = 1.²⁶` 应改为 `σ = 1.²⁷`
   - **Section 2.8 Volcano relation（SI L283）**：`about 3.2 eV,^(5,22)` 应改为 `^(4,23)`
   - **Table S4（SI L586–606，共 6 行 `Ref.` 列）**：`18 -> 19`（Fe/N-C）、`19 -> 20`（Fe₁Co₃–NC-1100）、`17 -> 18`（CoMn–NC）、`8 -> 10`（Fe-SA@NC）、`17 -> 18`（Co–NSC）、`18 -> 19`（Mn/N-C）
   - 另确认：`Figure 3e` 原图（`word/media/image3.png`）仅含样品名称，不含文献编号，**无需重新作图**；Section 1 L183 为 `Sun et al. (Nat. Catal. 2023, 6, 1164–1173)` 内联引文，不受影响。

---

## 1. 前言第二段逐句原文 PDF 核查

### 1.1 原 [D]（Refs 6–10，T036 已核，本次复核确认）

- **对应正文句**：
  > "Researchers have tuned the binding of ORR intermediates by modifying the coordinating atoms and carbon framework of M–N–C catalysts or by introducing neighboring metal species.^(6–10)"

| 新编号（旧编号） | 文献 | Zotero 本地 PDF 路径 | 支持判断 | 关键逐字依据与位置 |
|---|---|---|---|---|
| **6**（原 13） | Zhao et al., *J. Mater. Chem. A* 2019 | `S05_Zhao_2019_..._2.pdf`（T036 已核） | **部分支持** | Abstract：HO 轴向修饰单金属主要提升 OER，双金属显著提升 ORR；T036 已注明其局限于 DFT 且单金属对 ORR 提升有限。 |
| **7**（原 14） | Zhang et al., *Nano-Micro Lett.* 2023, 15, 228 | `Zhang2023_NML.pdf`（T036 已核） | **支持** | Abstract（PDF p. 1）：`"intentionally breaking the planar symmetry of SACs by adding ligands in the axial direction of metal single atoms offers a novel approach for the tuning of both geometric and electronic structures, thereby enhancing electrocatalytic performance at active sites."` |
| **8**（新增） | Wang et al., *Adv. Mater.* 2020, 32, 2000966 | `D:\Zotero\storage\659FRH95\Wang 等 - 2020 - Edge-Rich Fe−N4 Active Sites in Defective Carbon for Oxygen Reduction Catalysis.pdf` | **强支持** | 保持 `Fe–N₄` 配位不变，对比边缘缺陷（`e-ND−Fe`）与完整平面（`c-ND−Fe`）：Abstract（p. 1 of 8）`"Density functional theory calculations reveal that local electronic redistribution and bandgap shrinkage for e-ND−Fe endow it with a lower free-energy barrier toward direct four-electron ORR."`；DFT 节（p. 2 of 8）给出 0.58 vs 0.43 eV。 |
| **9**（原 7） | Jiang et al., *J. Am. Chem. Soc.* 2016, 138, 3570–3578 | `D:\Zotero\storage\LEV5ZRZE\Jiang2016_JACS.pdf` | **支持** | Abstract（p. 3570 / PDF p. 1）：`"These facts supported that the high ORR activity of the Fe@C-FeNC electrocatalysts should be ascribed to that Fe/Fe3C nanocrystals boost the activity of Fe–Nx."` 与 `"the interaction between metallic iron and Fe–N4 coordination structure favored the adsorption of oxygen molecule."` |
| **10**（原 8） | Huang et al., *Angew. Chem., Int. Ed.* 2022, 61, e202116068 | `D:\Zotero\storage\HTULCWEB\Huang 等 - 2022 - Clusters Induced Electron Redistribution to Tune Oxygen Reduction Activity of Transition Metal Singl.pdf` | **支持** | Abstract（PDF p. 1）：`"the metal clusters are able to induce electron redistribution and modulate M–N species bond lengths... The performance enhancement is attributed to the optimized intermediates desorption..."`；Theoretical Study（PDF p. 7）给出电荷重分布、Bader 电荷与 $\text{OH*}$ 吸附减弱线性关系。 |

---

### 1.2 原 [F]（Ref 11：Wan 2022 *Nat. Commun.*）

- **对应正文句**：
  > "In pyrolyzed M–N–C catalysts, metal atoms readily aggregate into particles, especially at high metal contents. Carbon-encapsulated particles also remain after acid leaching, so metal particles commonly coexist with single metal atoms.¹¹"

- **Ref 11 核查**：Wan, X.; Liu, Q.; Liu, J.; Liu, S.; Liu, X.; Zheng, L.; Shang, J.; Yu, R.; Shui, J. *Nat. Commun.* **2022**, *13*, 2963. DOI: `10.1038/s41467-022-30702-z`
  - **Zotero PDF**：`D:\Zotero\storage\HZ489V2P\s41467-022-30702-z.pdf`（全文 11 页）
  - **判断**：**部分支持（有两处措辞边界）**
  - **逐字原文支持句与位置**：
    1. **PDF p. 2（Introduction 第 2 段）**——支持“随金属含量改变形成单原子到纳米颗粒的多尺度共存相”：
       > "Fe–N–C catalysts may contain multiscale metal phases from single atoms (SAs), atomic clusters (ACs) to nanoparticles (NPs) depending on the metal contents and the synthesis methods33–35."
    2. **PDF p. 2（Introduction 第 2 段）**——支持“石墨碳层包覆的 Fe 颗粒能在酸中留存”：
       > "Fe NPs can be present in acids when they are encapsulated by a few layers of graphitic carbon (L > 3)43,44."
    3. **PDF p. 3（Results 第 2 节 `Active site structure analysis of FeSA/FeAC−2DNPC`）**——实验证明提高前驱体 Fe 含量从单原子演变为石墨碳层包覆颗粒与单原子共存（总 Fe 含量由 0.59 增至 1.16 和 1.56 wt%）：
       > "By varying the ratio of TPI in the precursor (5%, 15% and 30% of the CQD mass), the existing form of iron could be gradually tuned from SAs, to SAs/ACs, and then to SAs/NPs. ... FeSA−2DNPC shows atomic iron only, while FeSA/FeNP−2DNPC has atomic iron and iron NPs encapsulated by graphitic layers. According to inductively coupled plasma optical emission spectroscopy analysis, the overall iron contents are 0.59, 1.16, and 1.56 wt% for FeSA−2DNPC, FeSA/FeAC−2DNPC, and FeSA/FeNP−2DNPC, respectively."
  - **边界与核查细节说明**：
    1. 原文并未直接出现 `"readily aggregate"`（易团聚）表述，而是陈述 `"contain multiscale metal phases ... depending on the metal contents"` 及前驱体比例升高从 SAs 变为 SAs/NPs。而热解易团聚的表述其实在**正文已有的 Ref 9（Jiang 2016）和 Ref 13（Li 2018）**中都有直接原句：
       - Ref 9（Jiang 2016 *JACS*，p. 3571 / PDF p. 2）：`"the pyrolysis process not only created the Fe−Nx configurations, but also aggregated iron atoms to form graphene-encapsulated metallic Fe/Fe3C nanocrystals around Fe−Nx species."`（同一页下文亦写 `"formed by the random aggregation of iron atoms at high temperature during pyrolysis"`）
       - Ref 13（Li 2018 *Nat. Catal.*，p. 936 / PDF p. 2）：`"Mn atoms tend to form unstable and inactive metallic compounds, oxides and carbides during the heat treatment when simply increasing the amount of Mn precursors13,27."` 与 `"Mn aggregates easily form during the high-temperature carbonization even at a low content."`
    2. 原文写的是 `"present in acids"`（存在于酸性介质中），而非专门测试“热解后**酸洗（acid leaching）**前后颗粒残留”（Wan 2022 中的酸蚀仅在制备 CQD 载体步骤用浓盐酸刻蚀半碳化 ZIF-8，见 PDF p. 2 与 Methods p. 8）。若审稿人严格对照“acid leaching”原词，本地 Zotero 另有高影响力原始文献直接写到**酸洗后石墨碳壳包覆颗粒依然完整留存**：
       - **可选增引（无需另找 PDF，Zotero 已有）**：Xia, B. Y.; Yan, Y.; Li, N.; Wu, H. B.; Lou, X. W.; Wang, X. A Metal–Organic Framework-Derived Bifunctional Oxygen Electrocatalyst. *Nat. Energy* **2016**, *1*, 15006. DOI: `10.1038/nenergy.2015.6`（Zotero: `D:\Zotero\storage\N8LXXNE4\...`），**PDF p. 2**：
         > "H2SO4 for 6 h to remove the accessible Co nanoparticles. ... the carbon-encased Co nanoparticles are inaccessible to reactants as they remain completely encapsulated within the graphitic carbon shell even after acid leaching."

- **对 [F] 的最小改动建议**（供 Claude web / 赵月决策）：
  - 若保持现有 40 篇文献不增加条目：可将句尾上标由 `11` 改为 **`9,11,13`**（或分句标注：第一分句“热解时随金属含量升高易团聚成颗粒”引 `9,11,13`，第二分句“碳包覆颗粒在酸处理后留存并与单原子共存”引 `11`，甚至将两句合为一个引文注在句末）；
  - 若希望连 `"acid leaching"` 也达到 100% 字面精确覆盖，可在第二分句增引 `Xia 2016 Nat. Energy`（`10.1038/nenergy.2015.6`）配 `Wan 2022`（需随之顺延编号）。

---

### 1.3 原 [G]（Refs 12–13：Zitolo 2015 *Nat. Mater.* 与 Li 2018 *Nat. Catal.*）

- **对应正文句**：
  > "The activity of such catalysts is usually attributed to the single atoms alone.^(12,13)"
  （注：前句 `such catalysts` 指代“金属颗粒与单原子共存的 M–N–C 催化剂”）

1. **Ref 12 核查**：Zitolo, A. et al. *Nat. Mater.* **2015**, *14*, 937–942. DOI: `10.1038/nmat4367`
   - **Zotero PDF**：`D:\Zotero\storage\6P3L79HI\nmat4367.pdf`（全文 8 页）
   - **判断**：**部分支持（强例证型，而非阐述“学界普遍/通常归因”的综述句）**
   - **逐字原文支持句与位置**：
     - **p. 938（PDF p. 2，讨论 `Fe0.5` 无颗粒 vs `Fe1.0` 含零价 Fe / FeCx 颗粒）**：
       > "The equal activity of Fe0.5 and Fe1.0 indicates that the Fe-based particles present in Fe1.0 are ORR inactive, in contrast with recent reports on the ORR activity of carbon-encapsulated iron particles36,37."
     - **p. 937（PDF p. 1，Abstract）**：
       > "Here, we synthesized Fe–N–C materials quasi-free of crystallographic iron structures after argon or ammonia pyrolysis. ... Following a thorough XANES analysis, the detailed structures of two FeN4 porphyrinic architectures with different O2 adsorption modes were then identified."
   - **评价**：Zitolo 2015 确实对同时含铁颗粒与 `Fe–Nₓ` 的 `Fe1.0` 样品做出了“颗粒对 ORR 无活性，催化活性来自单核 Fe–Nₓ 位点”的经典结论，是 `"usually attributed to the single atoms alone"` 极佳的代表性**实证研究例证**；但它本身是具体案例论证（同时正文明确写出与当时包碳铁颗粒报道相反 `"in contrast with..."`），并非综述“学界通常如此认为”。

2. **Ref 13 核查**：Li, J. et al. *Nat. Catal.* **2018**, *1*, 935–945. DOI: `10.1038/s41929-018-0164-8`
   - **Zotero PDF**：`D:\Zotero\storage\FCMVMY9M\Li 等 - 2018 - Atomically dispersed manganese catalysts for oxyge.pdf`（全文 11 页）
   - **判断**：**部分支持（且与前句 `such catalysts` 主语存在一定张力）**
   - **逐字原文支持句与位置**：
     - **p. 935（PDF p. 1，Introduction 第 1 段）**：
       > "The MNxCy moieties themselves are also believed to be acting as the active sites to directly adsorb O2 and catalyse the subsequent O–O bond breaking in acidic media, therefore significantly improving the ORR catalytic activity6,10,11."
     - **p. 936（PDF p. 2，Introduction 第 2 段）**：
       > "However, a grand challenge is to increase the density of MnN4 active sites in catalysts because Mn atoms tend to form unstable and inactive metallic compounds, oxides and carbides during the heat treatment when simply increasing the amount of Mn precursors13,27."
     - **p. 936（PDF p. 2，Results 第 1 段）**：
       > "Both XRD patterns and STEM images verified the absence of any crystalline Mn-containing phases or clusters in the catalyst."
     - **p. 937（PDF p. 3，XPS 讨论）**：
       > "It was reported that the interaction between metallic clusters and MNx could change the charge density of the central metal ions and lead to a shift in the binding energy12."
   - **风险提示**：Li 2018 虽然在引言将非单原子金属/氧化物/碳化物称为 `"unstable and inactive"` 并将 Mn–N–C 活性归因于 `MnN4`，但**其高活性最终催化剂（`20Mn-NC-second`）通过两步掺杂+酸洗清除了所有 Mn 团簇/颗粒**，并不是前句所说的“颗粒与单原子共存催化剂（`such catalysts`）”。单引 Refs 12, 13 在审稿人眼里可能显得缺少直接综述该领域传统认知的文献。

3. **强力补充建议（Zotero 已有 PDF，直接支撑“通常归因于单原子、颗粒常被认为惰性/被避免或酸洗去除”）**：
   - **引文**：Zhao, C.-X.; Li, B.-Q.; Liu, J.-N.; Zhang, Q. Intrinsic Electrocatalytic Activity Regulation of M–N–C Single-Atom Catalysts for the Oxygen Reduction Reaction. *Angew. Chem., Int. Ed.* **2021**, *60*, 4448–4463. DOI: `10.1002/anie.202003917`
   - **Zotero PDF**：`D:\Zotero\storage\TKGR4J5I\Zhao 等 - 2021 - Intrinsic Electrocatalytic Activity Regulation of M–N–C Single-Atom Catalysts for the Oxygen Reducti.pdf`（全文 16 页）
   - **逐字原文支持句与位置**：
     - **p. 4458（PDF p. 11，Section 5.5 `Inorganic Nanoparticles`）**：
       > "Indeed, metal-based nanoparticles (usually metals, nitrides, or carbides) can be easily formed during the widely used pyrolysis synthetic process.[93] At first glance, these nanoparticles are catalytically inert for ORR and mark a failure in SAC fabrication. For this reason, the formation of nanoparticles in SAC synthesis is usually avoided or they are removed by acid washing after pyrolysis.[94]"
     - **p. 4451（PDF p. 4，Section 2 `Center Metal Atoms`）**：
       > "The center metal atoms are usually regarded as the actual ORR active sites.[30]"
   - **说明**：这段综述原文精准覆盖了“[F] 热解易生成颗粒、通常需酸洗去除”与“[G] 这类颗粒在传统 SAC 视角下被视为 ORR 惰性（不活跃），催化活性归于中心单原子”两重背景！若在此处或 [G] 处加入 `Zhao 2021 Angew.`（与经典例证 `Zitolo 2015` 搭配，甚至代替与“共存体系”略有张力的 `Li 2018`），逻辑和证据硬度会显著提升。

---

### 1.4 原 [E]（Refs 14–17）

- **对应正文句**：
  > "Under working conditions, however, both metal particles and single atoms are covered by species from the electrolyte.^(14–17)"

| 编号 | 文献 | Zotero 本地 PDF 路径 | 支持判断 | 逐字原文支持句与位置 |
|---|---|---|---|---|
| **14** | Wang, Y.; Tang, Y.-J.; Zhou, K. *J. Am. Chem. Soc.* **2019**, *141*, 14115–14119. DOI: `10.1021/jacs.9b07712` | `D:\Zotero\storage\QE9PVQJH\He2019_JACS.pdf`（及 `7C2JHE2J`） | **强支持（单原子端）** | • **p. 14115（PDF p. 1，Abstract）**：`"The modeling results show that the single-atom Fe site of the FeN4 center of Fe−N−C is covered with an intermediate OH* from 0.28 to 1.00 V. Remarkably, such OH* becomes part of the active moiety, Fe(OH)N4..."`<br>• **p. 14116（PDF p. 2）**：`"Above 1.00 V the Fe site is dominated by O*Fe. With the decrease of electrode potential (U), the covered O*Fe is gradually replaced by OH*Fe, which covers the Fe site over a wide range of U from 0.28 to 1.00 V."`<br>• **p. 14117（PDF p. 3）**：`"We extend our modeling into ORR on Mn−N−C and Co−N−C SACs and find that Mn−N−C possesses a similar self-adjusting mechanism as Fe−N−C (Figure 5a and Figure S11)."` |
| **15** | Zhao, K.-M. et al. *Nat. Catal.* **2025**, *8*, 422–435. DOI: `10.1038/s41929-025-01324-7` | `D:\Zotero\storage\5FRDI5MA\s41929-025-01324-7.pdf` | **强支持（单原子端，原位实验+理论）** | • **p. 422（PDF p. 1，Abstract）**：`"A high-spin trivalent FeN4 with an axial hydroxyl ligand, denoted as OH–Fe3+N4 (S = 5/2), is identified as the active state."`<br>• **p. 423（PDF p. 2）**：`"In situ Fe K-edge XANES was further used to probe the ligand presence at Fe3+N4 sites under a 0.1 M perchloric acid environment saturated with N2. As the potential was decreased from 0.9 to 0.5 V, there was a noticeable decrement in the Fe oxidation state, illustrated in Fig. 1g. ... This observation aligns with the inferred gradual disassociation of ligands from the Fe sites36. ... Extended X-ray absorption fine structure (EXAFS), in situ Fe K-edge XANES and mass spectrometry identified an axial OH ligand at the FeN4 site."` |
| **16** | Yang, W. et al. *Chem. Commun.* **2023**, *59*, 10761–10764. DOI: `10.1039/d3cc03208f` | `D:\Zotero\storage\4Y3FWCXT\Yang 等 - 2023 - Effects of intermetal distance on the electrochemistry-induced surface coverage of M–N–C dual-atom c.pdf` | **部分支持（引言综述涵盖金属与单原子；正文主体是双原子 DACs）** | • **p. 10761（PDF p. 1，Introduction 第 1 段）**：`"Understanding the surface coverages of an electrocatalyst under electrochemical conditions is crucial because the potential-dependent surface coverages determine properties of the initial reaction surface.1 Owing to the occurrence of electrochemical reactions at the electrolyte-electrode interface, cations or anions from hydrolysis have the potential to occupy the catalytic sites... Hansen et al.6 observed that alterations in the electrolyte pH and applied potentials induce modifications in surface coverages of some metal catalysts (e.g., Pt, Ag, and Ni). Dobrota et al.7 developed surface Pourbaix diagrams for some single-atom catalysts (SACs), revealing that the presence of H*, O*, and HO* species under certain reaction potentials could impede the accessibility of active sites."` |
| **17** | Hansen, H. A.; Rossmeisl, J.; Nørskov, J. K. *Phys. Chem. Chem. Phys.* **2008**, *10*, 3722–3730. DOI: `10.1039/b803956a` | `D:\Zotero\storage\GGQ6LY7X\Hansen2008_PCCP.pdf` | **强支持（金属表面端）** | • **p. 3722（PDF p. 3，Abstract & Intro）**：`"Based on density functional theory calculations we investigate the electrochemically most stable surface structures as a function of pH and electrostatic potential for Pt(111), Ag(111) and Ni(111), and we construct surface Pourbaix diagrams."` 与 `"It is obvious that the molecular structures on the surface is dependent on the metal, potential and pH of the electrolyte."`<br>• **p. 3723（PDF p. 4，Section 2.1）**：`"It is assumed the surface is in equilibrium with protons and liquid water at 298 K, so that oxygen and hydroxyl may be exchanged between the surface and a reference electrolyte through the following steps H2O(l) + * ⇌ HO* + H+(aq) + e− (1) and HO* ⇌ O* + H+(aq) + e− (2)"`<br>• **注**：该经典文献研究的是延展 `(111)` 金属单晶表面而非纳米颗粒本身，但作为电化学工作条件下金属表面受电解液 `O*/HO*` 物种覆盖的奠基方法文献（且本文亦用于 `FeCo(110)` 覆盖分析，Methods ref. 17），引用完全恰当。 |

---

## 2. 两篇新文献书目信息核查（PDF + CrossRef API）

### 2.1 Ref 8：Wang et al., *Adv. Mater.* 2020
- **2150 列表条目**：
  `(8) Wang, X.; Jia, Y.; Mao, X.; Liu, D.; He, W.; Li, J.; Liu, J.; Yan, X.; Chen, J.; Song, L.; Du, A.; Yao, X. Edge-Rich Fe–N₄ Active Sites in Defective Carbon for Oxygen Reduction Catalysis. Adv. Mater. 2020, 32, 2000966. DOI: 10.1002/adma.202000966.`
- **CrossRef API 与 PDF 首页核对结果**：
  - 12 位作者姓名、顺序及缩写：**一致**（Xin Wang, Yi Jia, Xin Mao, Daobin Liu, Wenxiang He, Jia Li, Jianguo Liu, Xuecheng Yan, Jun Chen, Li Song, Aijun Du, Xiangdong Yao）
  - 标题：`Edge‐Rich Fe−N4 Active Sites in Defective Carbon for Oxygen Reduction Catalysis`：**一致**
  - 期刊/年份/卷/文章号/DOI：`Advanced Materials`, `2020`, Vol. `32` (Issue 16), Article `2000966`, DOI `10.1002/adma.202000966`：**全部一致**。

### 2.2 Ref 11：Wan et al., *Nat. Commun.* 2022
- **2150 列表条目**：
  `(11) Wan, X.; Liu, Q.; Liu, J.; Liu, S.; Liu, X.; Zheng, L.; Shang, J.; Yu, R.; Shui, J. Iron Atom–Cluster Interactions Increase Activity and Improve Durability in Fe–N–C Fuel Cells. Nat. Commun. 2022, 13, 2963. DOI: 10.1038/s41467-022-30702-z.`
- **CrossRef API 与 PDF 首页核对结果**：
  - 9 位作者姓名、顺序及缩写：**一致**（Xin Wan, Qingtao Liu, Jieyuan Liu, Shiyuan Liu, Xiaofang Liu, Lirong Zheng, Jiaxiang Shang, Ronghai Yu, Jianglan Shui）
  - 标题：`Iron atom–cluster interactions increase activity and improve durability in Fe–N–C fuel cells`：**一致**
  - 期刊/年份/卷/文章号/DOI：`Nat. Commun.`, `2022`, Vol. `13` (Issue 1), Article `2963`, DOI `10.1038/s41467-022-30702-z`：**全部一致**。

---

## 3. 全文引用顺序（1–40）与重编号双射核查

对 `FeCoMn_Manuscript_revised_20261121_2150.txt` 进行脚本化解析核验：
1. **首次出现顺序**：正文首次出现编号序列严格为 `[1, 2, 3, ..., 40]`，**逐一递增，无跳号、无倒序、无未被引用的孤立文献**。
2. **文末列表连续性**：文末 `REFERENCES` 共 40 条 `(1)`–`(40)`，无重复编号（2055 版中原有两处重复标号为 `(36)` 的错误已在 2150 版中修复为 `(37)`–`(40)`）、无重复 DOI。
3. **跨版本映射核验（2055 版共 38 篇 -> 2150 版共 40 篇）**：

| 正文位置 | 2055 原引用 | 2150 新引用 | 对应文献 | 审计结论 |
|---|---|---|---|---|
| Intro P1 句 1（替代 Pt） | `1, 2, 12` | `1–3` | Debe 2012, Shao 2016, Zhang 2025 | **正确** |
| Intro P1 句 2（吸附强度决定活性） | `5, 12` | `3, 4` | Zhang 2025, Kulkarni 2018 | **正确** |
| Intro P1 句 3（过强/过弱 Sabatier） | `5, 6` | `4, 5` | Kulkarni 2018, Medford 2015 | **正确** |
| Intro P2 句 1 [D]（三类调控） | 占位 `[D]` | `6–10` | Zhao 2019, Zhang 2023, Wang 2020(新), Jiang 2016, Huang 2022 | 编号递增 **正确**（科学边界见 1.1） |
| Intro P2 句 2–3 [F]（团聚+包碳酸留存共存） | 占位 `[F]` | `11` | Wan 2022(新) | 编号递增 **正确**（科学边界见 1.2） |
| Intro P2 句 4 [G]（通常归于单原子） | 占位 `[G]` | `12, 13` | Zitolo 2015, Li 2018 | 编号递增 **正确**（科学边界见 1.3） |
| Intro P2 句 5（颗粒/团簇+单原子高活性） | `7, 8` | `9, 10` | Jiang 2016, Huang 2022 | **正确** |
| Intro P2 句 6（Fe 团簇例子） | `8` | `10` | Huang 2022 | **正确** |
| Intro P2 句 8 [E]（工作条件表面覆盖） | 占位 `[E]` | `14–17` | Wang 2019, Zhao 2025, Yang 2023, Hansen 2008 | 编号递增 **正确**（科学细节见 1.4） |
| Results L61（Fig 3e E₁/₂ 对比） | `8, 17–19` | `10, 18–20` | Huang 2022, Zhao 2025 AFM, Cai 2022, He 2022 | **正确** |
| Results L67（SEIRAS 1215 cm⁻¹ OOH*） | `20, 21` | `21, 22` | Zhou 2024 Nat. Commun., Wu 2025 Angew. | **正确** |
| Results L73（0.78 V 代表性电位） | `11` | `16` | Yang 2023 Chem. Commun. | **正确** |
| Results L83（scaling relation） | `5, 22, 23` | `4, 23, 24` | Kulkarni 2018, Viswanathan 2012, Zhou 2022 | **正确** |
| Results L83（activity volcano） | `6, 24` | `5, 25` | Medford 2015, Huang 2024 | **正确** |
| Methods L95（XAS Larch + WT） | `25, 26` | `26, 27` | Newville 2013, Funke 2005 | **正确** |
| Methods L95（VASP + PAW + PBE + D3） | `27–32` | `28–33` | Kresse 1996 .. Grimme 2011 | **正确** |
| Methods L95（Bader + COHP/LOBSTER） | `33–38` | `34–39` | Henkelman 2006 .. Nelson 2020 | **正确** |
| Methods L95（CHE 覆盖与自由能） | `15, 16` | `17, 40` | Hansen 2008, Nørskov 2004 | **正确** |

---

## 4. ⚠ 重要发现：Supporting Information（SI）中遗漏的文献交叉引用修改清单

对最新可见 SI 文本（`FeCoMn/manuscript/FeCoMn_SI_revised_20261121_2040.txt`，共 1035 行）及 `0b7765d` 提交日志进行了全文件逐行检查。

`0b7765d` 已在 `FeCoMn_SI_revised_20261121_2150.docx` 中将 Section 2.5（L239）的 `"main-text ref. 12"` 更新为 `"main-text ref. 3"`（Zhang 2025 JACS）；但**SI 中还有以下 3 处（共 10 个编号）同样引用正文文献列表（Section 2.1 L189 明确声明 `"Reference numbers in this section follow the main-text bibliography."`，Table S4 L606 明确声明 `"reference numbers refer to the main-text reference list."`），在 `2040` 版中仍为旧编号，需要 Claude web 在 SI Word 中补改**：

| SI 位置（行号） | 现文本（旧编号） | 对应文献 | 应改为（2150 新编号） |
|---|---|---|---|
| **Section 1 Characterization（L177）** | `Larch²⁵ was used for background removal...` | Newville 2013 *J. Phys.: Conf. Ser.* | **`Larch²⁶`** |
| **Section 1 Characterization（L177）** | `Morlet wavelet transforms used η = 10 and σ = 1.²⁶` | Funke 2005 *Phys. Rev. B* | **`σ = 1.²⁷`** |
| **Section 2.8 Volcano relation（L283）** | `With the commonly used scaling constant of about 3.2 eV,^(5,22) the apex shifts...` | Kulkarni 2018 (旧 5) & Viswanathan 2012 (旧 22) | **`^(4,23)`** |
| **Table S4 第 2 行（L593）** | `Fe/N-C \| single-metal control \| 0.88 \| 18` | Cai 2022 *Small* | **`19`** |
| **Table S4 第 3 行（L595）** | `Fe₁Co₃–NC-1100 \| bimetallic \| 0.877 \| 19` | He 2022 *ACS Catal.* | **`20`** |
| **Table S4 第 4 行（L597）** | `CoMn–NC (atomically dispersed) \| bimetallic control \| 0.85 \| 17` | Zhao 2025 *Adv. Funct. Mater.* | **`18`** |
| **Table S4 第 5 行（L599）** | `Fe-SA@NC \| single-atom \| 0.84 \| 8` | Huang 2022 *Angew. Chem., Int. Ed.* | **`10`** |
| **Table S4 第 6 行（L601）** | `Co–NSC \| single-metal control \| 0.82 \| 17` | Zhao 2025 *Adv. Funct. Mater.* | **`18`** |
| **Table S4 第 7 行（L603）** | `Mn/N-C \| single-metal control \| 0.76 \| 18` | Cai 2022 *Small* | **`19`** |

### 无需修改的 SI / 图件项确认
- **Section 1 ATR-SEIRAS（L183）**：`Sun et al. (Nat. Catal. 2023, 6, 1164–1173)` 为完整内联作者/期刊信息，不在正文参考文献 1–40 列表中，**无需改动**。
- **Figure 3e 原图（`word/media/image3.png`）**：经直接查看图像确认，图内仅标注催化剂名称（`Fe/N-C`, `Pt/C`, `CoMn–NC`, `Mn–NC`, `Fe₁Co₃-NC`, `FeCo–NC`, `Fe-SA@NC`, `Co-NSC`, `Mn/N-C`），**不含文献编号**，无需重新制图。

---

## 5. 给写稿方与作者的后续行动清单

1. **必须执行**：在 `FeCoMn_SI_revised_20261121_2150.docx` 中同步更新上述 **Section 1（2 处）、Section 2.8（1 处）和 Table S4（6 处）**的正文参考文献编号（若之后因增补 [F]/[G] 再次变更正文编号，需一并更新 SI 这几处与 `main-text ref. 3`）。
2. **强烈建议酌定（是否补强 [F] 与 [G]）**：
   - **[F]**：目前单引 `11`（Wan 2022）缺少 `"readily aggregate"` 与 `"acid leaching"` 原词（实际是 `"in acids"`）；最轻量化做法是改为 **`9,11,13`**（用正文已有的 Jiang 2016 + Li 2018 补齐热解团聚），或增引 `Xia 2016 Nat. Energy`（`10.1038/nenergy.2015.6`）补齐 `"even after acid leaching"`；
   - **[G]**：目前 `12,13` 缺少针对“学界通常只把共存体系活性归因于单原子”的综述型表述（且 `13` Li 2018 自身产物无颗粒）；建议在 [G] 处增引 `Zhao et al., Angew. Chem., Int. Ed. 2021, 60, 4448–4463`（`10.1002/anie.202003917`，p. 4458 直述 `"At first glance, these nanoparticles are catalytically inert for ORR... usually avoided or they are removed by acid washing after pyrolysis"`）。
