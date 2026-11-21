# FeCoMn-T005 文献核对报告

日期：2026-11-14。按更新后的7项逐条核对；Fe、Co、Mn分别检索，不预设Fe优先。只查资料，没有修改任何论文图或Word。金属详细证据表见 [METALS_EVIDENCE.md](METALS_EVIDENCE.md)。

## 先说与本样有关的结论

1. 三个谷739、818、882 cm⁻¹，与天然单晶硅多声子吸收739.1、819、约888 cm⁻¹组成的整组位置十分接近。这是值得优先核查的光学来源线索，**不是本样已经证实的归属**；只凭峰位不能宣布三个谷都是硅。
2. 低于1000 cm⁻¹不是统一禁区。薄硅片/Au方法确实测到约730 cm⁻¹水摆动带；具体可用性取决于棱镜厚度、光路、探测器及单光束透过率。
3. 金属候选确实存在：α-FeOOH约887–895及795；β-FeOOH ATR 845；γ-FeOOH ATR 750/895；MnO₂特定相FTIR 740；Co–OH弯曲798。它们不能仅凭“接近”就套到本样三个谷，也不能用OER氧化区的Co证据代替本样ORR证据。
4. 1215–1230有多篇原始论文归OOH，也有原始论文通过空白对照归1220为Si–O。**文献两种说法都真实存在，不能靠多数票定归属。**
5. 赵月说明采背景时已装好样品膜，包含Nafion；这一事实应保留。静态Nafion贡献在背景比值中通常抵消，不能因为1210附近有C–F峰就说当前信号一定来自Nafion。同样，仅这一背景步骤也不能证明所有电位响应、膜水合/取向或棱镜界面变化完全为零。本次不据此重新处理数据或改归属。

本报告采用“原始出处已读/仅摘要已核/未取得原表”的分级；未取得图号、半峰宽、参比电位等信息时明确写缺，不推测补齐。候选峰接近不等于相鉴定、反应中间体鉴定或对当前负谷的因果解释。

## 1. 单晶Si多声子吸收

**P. G. Sennikov等，Semiconductors 39 (2005) 300–307，DOI [10.1134/1.1882791](https://doi.org/10.1134/1.1882791)**。已读作者英文稿/俄刊版：*Fizika i Tekhnika Poluprovodnikov* 39，320–326；**Table 2，印刷p322，PDF第3页**。两版页码不可混用。[原始PDF](http://journals.ioffe.ru/articles/viewPDF/5752)。表头短引：“Spectral positions ... of phonon modes in IR spectrum of silicon”。

|天然Si模式|原表引用值 / 本文测得，cm⁻¹|与本样近似谷的关系|
|---|---|---|
|LO + TA|566 / 566.4|本次三谷范围之外|
|TO + TA|610 / 610.8|范围外|
|LO + LA|739 / 739.1|对应约739，接近0.1|
|TO + LA|819 / 819|对应约818，接近1|
|TO + LO|886 / 约888|对应约882，差约4–6；不可称完全重合|
|TO + TO|960 / 约959|额外可查位置，本次未重新分析样品|

这是**Si晶格多声子组合**，不是Si–O化学键振动。原表为300 K天然同位素Si；不同同位素样品列不能误当普通ATR棱镜数据。

交叉证据：**Topsil，2013年10月，HiTran应用说明，Table 1，p3**，[厂商原始技术说明](https://www.topsil.com/wp-content/uploads/2023/05/hitran_application_note_october2013.pdf)，无DOI。给740、819、896 cm⁻¹，吸收系数约3.0、2.1、2.4 cm⁻¹。它支持该区域存在Si多声子吸收，同时也显示高频一带文献数值并不全相同；不能人为把896改成888。

**对本样的界限：**静态棱镜吸收若参比/样品光学状态完全相同，应在比值中抵消。当前负谷不能仅凭“硅有吸收”解释其电位依赖；还需要本体系单光束/空白等信息。本轮未做该实验验证，也未自动删点或扣掉这些谷。

## 2. Au/Si ATR-SEIRAS低波数可用下限

**Tyler A. Morhart、Bipinlal Unni、Michael J. Lardner、Ian J. Burgess，Analytical Chemistry 89 (2017) 11818–11824，DOI [10.1021/acs.analchem.7b03509](https://doi.org/10.1021/acs.analchem.7b03509)**。期刊原始摘要已核：[PubMed](https://pubmed.ncbi.nlm.nih.gov/29019249/)。作者使用厚500 μm、沟槽角35°的微加工Si片，比较传统半径25 mm Si半球；优化入射角50–55°，在低波数获得更好的信噪比，观察到置换水约730 cm⁻¹摆动振动。原始摘要短引：“water libration bands at ca. 730 cm−1”。本轮未取得期刊正文图版，**不编造期刊图号**。

同作者完整一手资料：**Tyler A. Morhart，2021年博士论文，Surface-Enhanced Spectroelectrochemistry using Synchrotron Infrared Radiation，University of Saskatchewan**，[机构原文](https://harvest.usask.ca/server/api/core/bitstreams/d6aa7e44-af26-48bd-91f7-37e870799e90/content)，无DOI。**Fig. 4.8，印刷p64/PDF第81页；解释印刷p66/PDF第83页**。文中约725 cm⁻¹负带与1625 cm⁻¹水弯曲同向，说明SEIRAS增强可延伸到1000以下；采集下限还受MCT/A探测器限制。这是学位论文图号，**不是Anal. Chem. Fig. 4.8**。

结论：不能给所有Au/Si系统规定一个共同的1000 cm⁻¹下限；也不能反过来因为别人的薄片可测730，就认定本样传统棱镜在739的定量可靠。针对咱们仪器的具体截止仍未核定。

## 3. 水的摆动振动与电位响应

|原始出处与定位|原文位置/带宽/条件|能说明什么|
|---|---|---|
|Morhart 2017及2021论文，见第2项|期刊摘要约730；论文解释约725，**宽的向下带**；比较−700 mV参比与+200 mV样品，电位标尺按原论文，此处不自行换算RHE；伴随1625水弯曲带|吸附有机单层置换界面水，能产生低波数负带；不是本样金属氧化物证据|
|Hongna Zhang、Boqiang Chen、Tianying Liu、Gary W. Brudvig、Dunwei Wang、Matthias M. Waegele，JACS **146 (2024) 878–883**，DOI [10.1021/jacs.3c11206](https://doi.org/10.1021/jacs.3c11206)，**Fig. 3A，机构作者稿PDF p2**，[一手作者稿](https://www.osti.gov/servlets/purl/2274729)|Au/Si、1.25 mM Ir二聚体、0.1 M HClO₄；1.4–1.7 V RHE周期调制，OCV为单光束参比。700–950宽背景随电位响应，作者解释为水的摆动振动；未报FWHM|确有**电位依赖的水摆动振动**，非只在吸附置换实验出现；但体系为酸性Ir析氧，不能移植为本样ORR曲线|

Zhang作者原句短引：“potential-dependent changes in the librational band of water”。期刊卷期年为2024，在线日期2023-12-28，不能因在线年份写成JACS 2023卷146。

本次已核一手资料呈现的是宽带/背景，**没有给液态水一个统一FWHM**；不编造半峰宽。水可能贡献739附近的宽负谷，但不能据此把739/818/882三个较固定的位置全部认成三个独立水摆动模式。精确三峰组合的Si证据和宽带水证据需分别考虑。

## 4. Fe、Co、Mn与混合物的低波数IR

完整作者、DOI、峰位、图表号和短引见 [METALS_EVIDENCE.md](METALS_EVIDENCE.md) 第4项。核心分组如下；下表为导航，不替代详细证据表。

|组别|本轮查实的主要IR资料|没有查实的部分|
|---|---|---|
|Fe|α-FeOOH OH变形887–895/795附近；β-FeOOH ATR 642/845/980；γ-FeOOH ATR 750/895及1020/1156；固态Fe₃O₄ FTIR 570|δ-FeOOH与固态Fe(OH)₂所需原表未取得；不以基质隔离Fe(OH)₂的737.3补位|
|Co|Co–OH弯曲798→活化后CoOOH 568；Co₃O₄ IR伸缩600/682；CoOOH宽500–650|α/β样品阴离子不同导致模式差异；863等可能是插层硝酸根，不可直接当Co–OH|
|Mn|ramsdellite MnO₂ FTIR 740/687；Mn₃O₄约632/530等；MnOOH相关OH弯曲1085/1118/1151|固态Mn(OH)₂及Mn–N₄位点Mn–O/OH的600–1000原始IR未核实；不把孤立分子或Raman值套用|
|混合|CoFe₂O₄ FTIR 600/417|FeCo-LDH与FeCo羟基氧化物缺可核的所需逐峰原表，不能由CoFe₂O₄替代|

**模式必须区分：**FeOOH约890/795是OH变形；Co–OH 798作者称弯曲；许多氧化物M–O晶格伸缩在约400–700。不存在一个对所有Fe/Co/Mn材料通用的“金属–氧800–900”标签。光谱方法也必须分开：Glotch与Kraft同文的发射谱和ATR数值不同，不在本报告混抄。

## 5. 原位电化学IR中的M–O/OH生成和还原

最直接核实的碱性例子为 **Yangming Lin等，ACS Catalysis 12 (2022) 5345–5355，DOI [10.1021/acscatal.1c05598](https://doi.org/10.1021/acscatal.1c05598)**，**Fig. 5 p5350，解释p5351；Fig. 6 p5351**。[机构原文](https://pure.mpg.de/pubman/item/item_3379099_7/component/file_3383764/acscatal.1c05598.pdf)。详细短引/条件在金属证据表第5项，此处不重复引用。

0.1 M KOH，Ar气氛：835 cm⁻¹自约1.3 V RHE出现，作者谨慎归O–CoIII–O⁻；845自约1.4 V出现，作者谨慎归CoIV=O，1.6 V较强。作者使用H/D及¹⁸O检验，并观察可逆电位响应。**这是OER氧化区，不能直接解释本样ORR的1.21→0.81 V。**

Fe和Ni：本轮已检索但未取得符合“低波数M–O/OH原位IR、逐电位、可核原图”的可靠实例；NiOOH常见475/555多为Raman，本报告不冒充红外。此为明确的证据缺口，不是宣称Fe/Ni不存在此类研究。

## 6. 800–900 cm⁻¹过氧物种

|物种/谱学|作者、出处、定位|原始峰位与验证|对本样的限制|
|---|---|---|---|
|表面Ir–OOH，快速扫描ATR-FTIR|Narayanappa Sivasankar、Walter W. Weare、Heinz Frei，JACS **133 (2011) 12976–12979**，DOI [10.1021/ja205300a](https://doi.org/10.1021/ja205300a)，**原始摘要已核，正文图号本轮未取得**；[PubMed](https://pubmed.ncbi.nlm.nih.gov/21770440/)|ν(O–O) **830**；D₂O到800（−30）；进一步¹⁸O位移24/46。短引：“OO vibrational mode at 830 cm−1”。光敏Ru激发Ir氧化物纳米簇氧化水|证明M–OOH确有800–900的IR先例；不是FeCoMn ORR，也不是自由HO₂⁻|
|H₂O₂分子红外|Paul A. Giguère，J. Chem. Phys. **18 (1950) 88–92**，DOI [10.1063/1.1747464](https://doi.org/10.1063/1.1747464)，**原始摘要**；[Caltech原文及摘要](https://authors.library.caltech.edu/records/2wrvk-hv005)|气相877，液相约880。PDF为扫描图，本轮未完成原图编号核实|与882接近，但中性H₂O₂不能冒充HO₂⁻或吸附M–OOH|
|自由HO₂⁻，水溶液IR|本轮未取得符合条件的原始IR逐峰证据|850附近检索结果大量是**Raman**；未纳入IR赋值|不能据此把818/882标HO₂⁻|

另外检索到过氧桥Fe配合物831及¹⁸O位移46的原始论文（DOI10.1038/s41467-022-28894-5），但原图IR与rR混合展示，本轮没有完成逐面板独立核对，**不纳入已核实IR赋值表**。同样不使用HO₂自由基气相数值替代HO₂⁻。

结论：金属过氧O–O确实可能落在这一区域，但仅位置相似不能从三个负谷推断其被还原或消耗。M–OOH的800–900 O–O与部分电催化论文1225的OOH标签并非可以简单互相替代的“同一个通用峰”；需核对具体模式和同位素证据。

## 7. 1215–1230 cm⁻¹：OOH、Si–O与Nafion

### 7.1 至少三篇原始ORR论文的OOH归属

|原始论文|体系、原文位置与峰位|采谱电位/参比|原文短引与核对等级|
|---|---|---|---|
|**Yuhui Tian等**，JACS **148 (2026) 5574–5584**，DOI [10.1021/jacs.5c20189](https://doi.org/10.1021/jacs.5c20189)，*Machine Learning-Guided Coordination Engineering…*|CuSA/N–C，0.1 M KOH；**Fig. 5f**，本地ASAP PDF p8图/p9解释，**1228**|图示1.1→0.4 V RHE；正文及已读SI未明确单光束背景电位，**未查明，不能默认OCV或1.21 V**|“characteristic peak at approximately 1228 cm−1”；正文+SI已读|
|**Long-Ji Yuan等**，Nat. Commun. **16 (2025) 7198**，DOI [10.1038/s41467-025-62728-4](https://doi.org/10.1038/s41467-025-62728-4)，*Janus effect of FeCo dual atom catalyst…*|T-FeCo-N-C/R-FeCo-N-C，酸性ORR；**Fig. 4b,c，PDF p7**；T样一带**1225.9→1206.4**红移|图示0.9→0.1 V RHE；**Methods PDF p10明确工作电极OCV背景**|“red shift from 1225.9 cm−1 to 1206.4 cm−1”；全文已读。图纵轴Transmission，作者还作基线处理，不能据图外观宣称未经处理吸收|
|**Haiyuan Zou等**，Nat. Commun. **15 (2024) 10818**，DOI [10.1038/s41467-024-55116-x](https://doi.org/10.1038/s41467-024-55116-x)，*Steering acidic oxygen reduction selectivity…*|Co-N₄-NP与Co-N₄，O₂饱和0.10 M HClO₄；**SI Fig. 29a,b，SI PDF p27；正文PDF p7**，约**1225**归表面OOH；1392另归H₂O₂弯曲|0.80→0.10 V RHE；**Methods PDF p9明确OCV背景**|“O−O stretching mode of surface-adsorbed *OOH”；全文+SI图已核|

上表是“原作者如此归属”的事实记录，不表示三篇均完成排除Si–O、Nafion的全部验证。OCV作背景不等于没有参比；不要把吸收/透过率的纵轴名称直接等同于仪器是否作过背景比值。Tian背景未交代的缺口已保留。

### 7.2 同一区域的Si–O直接反例

**Kai Sun、Juncai Dong、Hao Sun、Xingdong Wang、Jinjie Fang、Zhongbin Zhuang、Shubo Tian、Xiaoming Sun，Nature Catalysis 6 (2023) 1164–1173**，DOI [10.1038/s41929-023-01047-7](https://doi.org/10.1038/s41929-023-01047-7)，*Co(CN)₃ catalysts with well-defined coordination structure for the oxygen reduction reaction*。

**Main Fig. 4c，p1169/PDF p6；SI Fig. 23，SI PDF p26**。原作者把**1220 cm⁻¹**归为ATR硅棱镜Si–O，用**无催化剂空白电极**验证；SI图为O₂饱和0.1 M KOH、25°C，显示1.0、0.7、0.4、0.1 V RHE。原句短引：“associated with a Si–O vibration from the silicon prism used in the ATR tests”。本轮已打开正文和SI图，不是只见转述。

[原始SI](https://media.springernature.com/full/springer-static/esm/art%3A10.1038%2Fs41929-023-01047-7/MediaObjects/41929_2023_1047_MOESM1_ESM.pdf)。约45 MB不重复上传仓库，保存URL和本地审阅记录。该篇1094/1062为作者另外讨论的OH相关带，不能改写成1220为OOH。

### 7.3 Nafion的实际C–F位置

**J. Zamudio-García、M. V. Martínez de Yuso、A. L. Cuevas、D. Marrero-López、J. Benavente，Polymers 15 (2023) 2527**，DOI [10.3390/polym15112527](https://doi.org/10.3390/polym15112527)，*Modification of the Physical Properties of a Nafion Film…*。**§3.1，PDF p4，SI Fig. S1**；[原始正文](https://www.mdpi.com/2073-4360/15/11/2527)。原文列纯Nafion **1210/1140 cm⁻¹**为CF₂非对称/对称伸缩，1050为SO₃，980/970为C–O–C。短引：“characteristic bands at 1210 and 1140 cm−1”。

这是固体膜材料的直接FTIR位置证据，**不是“本样差谱1215一定为Nafion”证据**。当前样品已装膜采背景，静态背景的情况必须与未扣背景的粉末IR区分。本报告未查到能直接证明本样该电位响应为Nafion的原始对照，因此不作这项结论。

### 7.4 原文如何区分来源

- Sun 2023：同一光学体系下无催化剂空白，直接暴露1220 Si–O。这是最切题的一手对照先例。
- Sivasankar 2011：D/H及¹⁸O位移支持OOH/O–O，且响应跟随激发；说明结构赋值可以超出“峰位吻合”。
- Lin 2022：KOH/KOD、H₂¹⁸O和电位可逆性相结合，区分835/845金属氧及1054/1108含氧中间体；其1054不能改写成本样1215。
- 三篇ORR论文的OOH标签，不能单独排除咱们仪器的棱镜或膜；别人的空白也不能替代本样空白。文献证据允许保留OOH相关候选，尚不足以宣布唯一来源。

## 三个谷逐项证据评估

“强/中/弱”指**文献匹配强度**，不表示本样归属置信概率。

|本样近似位置|文献支持的候选与匹配强度|仍不能排除/不能直接使用|
|---|---|---|
|882|Si TO+LO约886–888，且与819/739成组，**整组匹配强**；α-FeOOH OH变形887–895，单峰接近**中**；液H₂O₂约880但物种不同，**弱**|水宽带/光学背景可能叠加；不能标成已证实FeOOH或HO₂⁻；Co插层硝酸根863不是CoOH的直接证据|
|818|Si TO+LA819，**强峰位匹配**；CoOH弯曲798相差20，**弱**|IrOOH830为不同体系，仅说明范围可能；βFeOOH发射823不能冒充其ATR峰；本轮无唯一金属IR归属|
|739|Si LO+LA739.1，**强峰位匹配**；MnO₂-ramsdellite FTIR740，**强位置/弱本样相证据**；水摆动725–730宽带，**中**；γFeOOH ATR750，**中**|可为多来源叠加；不能把ramsdellite740等同所有MnO₂；不能用Fe(OH)₂孤立分子737.3作固态证明|

## 本轮未解决事项与文件

已完成7项检索与报告，但**未完成样品物种确证**。明确缺口：δ-FeOOH、固态Fe/Mn氢氧化物部分原表；Mn–N₄–O/OH低频IR；Fe/Ni逐电位低频IR；自由水溶HO₂⁻原始IR；部分论文背景电位和正文图号；本体系光学截止及空白。未取得不是不存在，报告不据此否定这些物种。

- 本报告：`REPORT.md`。
- 金属详细出处与检索式：`METALS_EVIDENCE.md`。
- 一手资料核查与SHA：`SOURCE_AUDIT.json`（仅记录实际本地已打开文件；PDF不在仓库重复保存）。
- 没有新增拟合、扣背景、重画或修改Word，也未自动调整Figure 4的谱带名称。
