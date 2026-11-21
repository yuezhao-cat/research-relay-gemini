# T045 前言新插参考文献核查（Claude Code 本地，2026-11-21）

说明：赵月指示由 Claude Code 直接核（Antigravity 慢）。插入方 Claude web 与本核查方同属 Claude 家族，不属跨家族核查。依据：正文 `manuscript/FeCoMn_Manuscript_revised_20261121_2150.txt`；原文 PDF 取自 D:\Zotero\storage（按 DOI 从 Zotero 数据库定位）。页码为期刊页码，括号内为 PDF 页序。未改 Word。

## 结论一览
| 位置 | 引文 | 结论 |
|---|---|---|
| [D] 新增 Wang 2020 | 8 | 支持 |
| [F] 颗粒团聚、包碳颗粒耐酸、颗粒与单原子共存 | 11 | **部分支持**：共存与耐酸有原句；高金属含量时团聚这一方向 Wan 2022 没有明说 |
| [G] 活性通常只归给单原子 | 12、13 | 支持 |
| [E] 工作条件下颗粒和单原子都被电解液物种覆盖 | 14–17 | 支持；颗粒一侧仅 Hansen 2008 的单晶面计算 |
| 书目信息（8、11） | | 正确 |
| 正文引用顺序 1–40 | | 正确 |
| SI 表 S4 中的正文文献编号 | | **需改 6 处**（见第 4 节） |

## 1. 逐句原文

**[D] ref 8 Wang 2020 Adv. Mater. 32, 2000966**（第 1 页，PDF p1，摘要）
> "Density functional theory calculations reveal that local electronic redistribution and bandgap shrinkage for e-ND−Fe endow it with a lower free-energy barrier toward direct four-electron ORR. Inspired by this, a series of atomic Fe catalysts with adjustable ND−Fe coordination are synthesized"

调整缺陷碳中 Fe–N4 的边缘配位来改变 ORR 能垒，对应 modifying the coordinating atoms and carbon framework，支持。

**[F] ref 11 Wan 2022 Nat. Commun. 13, 2963**（第 2 页，PDF p2，引言）
> "Fe–N–C catalysts may contain multiscale metal phases from single atoms (SAs), atomic clusters (ACs) to nanoparticles (NPs) depending on the metal contents and the synthesis methods33–35."
> "Fe NPs can be present in acids when they are encapsulated by a few layers of graphitic carbon (L > 3)43,44."

- 颗粒与单原子共存、包碳颗粒酸洗后残留：有原句支持。
- 不足 1：原文是 may contain，以及 depending on the metal contents，没有写 readily aggregate，也没有写 especially at high metal contents 这个方向。
- 不足 2：这两句在 Wan 原文中本身是引用他人（33–35、43、44），属于二手表述。
- 可补的原句（都已在本文列表中）：
  - Li 2018（ref 13，第 936 页，PDF p2）："Mn atoms tend to form unstable and inactive metallic compounds, oxides and carbides during the heat treatment when simply increasing the amount of Mn precursors"
  - Zitolo 2015（ref 12，第 938 页，PDF p2）："The Fe content and catalyst precursor preparation were modified for Fe0.5 to avoid the formation of metal particles."
- 处理建议，二选一（由 Claude web 和赵月定）：
  - (a) 第一句句末加引 Zitolo 和 Li。但这样 12、13 会先于 11 出现，需要重新编号。
  - (b) 把 especially at high metal contents 改为 depending on the metal content，与 Wan 原句一致，编号不动。

**[G] ref 12 Zitolo 2015 Nat. Mater. 14, 937**（第 937 页，PDF p1，摘要）
> "Here, we synthesized Fe–N–C materials quasi-free of crystallographic iron structures … The present study then identifies the structure of two candidate active sites having a porphyrinic planar architecture with a FeN4C12 core"

第 938 页（PDF p2）还写到："The Fe content and catalyst precursor preparation were modified … to avoid the formation of metal particles."

**[G] ref 13 Li 2018 Nat. Catal. 1, 935**（第 936 页，PDF p2）
> "synthesis of Mn-N-C catalysts with atomic dispersion of MnN4 active sites"

第 942 页（PDF p8，图 6 注）："Atomistic structure of MnN4C12 active site in the 20MnNC-second catalyst."

两篇都刻意排除颗粒，并把活性归于 MN4 单原子位点，支持 attributed to the single atoms alone。

**[E] ref 14 Wang 2019 JACS 141, 14115**（第 14115 页，PDF p1）
> "the SA Fe site of FeN4 of Fe−N−C SACs is preferentially covered with an intrinsic intermediate OH*. Such OH* becomes part of the Fe center with the formation of Fe(OH)N4"

注：Zotero 中该条目的附件文件名为 He2019_JACS.pdf，但内容确为本文，建议改名。

**[E] ref 15 Zhao 2025 Nat. Catal. 8, 422**（第 422 页，PDF p1，摘要）
> "A high-spin trivalent FeN4 with an axial hydroxyl ligand, denoted as OH–Fe3+N4 (S = 5/2), is identified as the active state."

**[E] ref 16 Yang 2023 Chem. Commun. 59, 10761**（第 10761 页，PDF p1，摘要）
> "based on surface Pourbaix analysis, we identified a significant change in the electrochemistry-induced surface coverages of DACs … the type of pre-covered adsorbate"

**[E] ref 17 Hansen 2008 PCCP 10, 3722**（第 3722 页，PDF p3，摘要）
> "The reason for this difference is the oxidation of the reactive surface. Oxygen absorbed on the surface shifts the reactivity towards the weak binding region"

第 3723 页图 1 注："The hydroxyl coverage increases to 1/3 ML at 1.11 V"（Ag(111)）。

14–16 支持单原子被覆盖。17 支持金属表面被 O/OH 覆盖，但对象是 Pt、Ag、Ni(111) 单晶面，不是负载颗粒。作为颗粒一侧的依据可以接受；如需更贴近，可另找负载合金颗粒的覆盖文献。

## 2. 新文献书目信息（对照 PDF 首页与 OpenAlex）
- ref 8：Wang, X.; Jia, Y.; Mao, X.; Liu, D.; He, W.; Li, J.; Liu, J.; Yan, X.; Chen, J.; Song, L.; Du, A.; Yao, X. Edge-Rich Fe–N4 Active Sites in Defective Carbon for Oxygen Reduction Catalysis. Adv. Mater. 2020, 32, 2000966。12 位作者及顺序、题名、DOI 均一致（OpenAlex 作者名为 Yi Alec Jia，缩写 Jia, Y. 无误）。
- ref 11：Wan, X.; Liu, Q.; Liu, J.; Liu, S.; Liu, X.; Zheng, L.; Shang, J.; Yu, R.; Shui, J. Iron Atom–Cluster Interactions Increase Activity and Improve Durability in Fe–N–C Fuel Cells. Nat. Commun. 2022, 13, 2963。9 位作者、题名、卷号、文章号（PDF 页脚 (2022)13:2963）、DOI 均一致。

## 3. 正文引用顺序
解析正文中 ^(…) 与 Unicode 上标两种引用格式，共 25 处引用、40 个编号，首次出现顺序为 1, 2, …, 40，无跳号；参考文献列表 40 条，无缺号、无重号。按 DOI 对照 2040 版与 2150 版：旧 38 条全部保留，新增 8、11 两条；旧 ref 15（Nørskov 2004）首次出现位置后移，现为 ref 40。

## 4. SI 中的正文文献编号（需要改）
本机没有 2150 版 SI，只有仓库中的 2040 版 SI 文本。2040 版 SI 中有两处引用正文编号：
1. 第 2.x 节 main-text ref. 12（Zhang 2025 JACS）应改为 ref. 3。Claude web 说已改。
2. **表 S4（图 3e 半波电位对照）的 Ref. 列**：表注写明 reference numbers refer to the main-text reference list，但该列仍是旧编号。Claude web 的说明中没有提到这一处。按 DOI 换算应改为：

| 行 | 旧 | 新 | 文献 |
|---|---|---|---|
| Fe/N-C | 18 | 19 | Cai 2022 Small |
| Fe₁Co₃–NC-1100 | 19 | 20 | He 2022 ACS Catal. |
| CoMn–NC | 17 | 18 | Zhao 2025 Adv. Funct. Mater. |
| Fe-SA@NC | 8 | 10 | Huang 2022 Angew. |
| Co–NSC | 17 | 18 | Zhao 2025 Adv. Funct. Mater. |
| Mn/N-C | 18 | 19 | Cai 2022 Small |

请 Claude web 在 2150 版 SI 中确认是否已改；未改则按上表修改。
