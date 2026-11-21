# 图 5 第一段（T038/T038b）审阅：Claude Code

审阅对象：`FeCoMn/discussion/20261120_1112_Fig5_T038_paragraph_for_review.md`（24c2db6，含 93c689b 的 11:15 更新）
核对依据：`manuscript/FeCoMn_Manuscript_revised_20261119_2255.docx`、`manuscript/FeCoMn_SI_revised_20261119_2255.docx`，直接从 docx 提取全文（python-docx，含表格），未只读 plaintext。
审阅人：Claude Code，2026-11-20

---

## 一、数值核对（打开 SI 表 S10 原表）

| 段中数值 | 表 S10 原值（0.78 V，eV per cell） | 结论 |
|---|---|---|
| FeCoMn–NC：OH 比 O 稳定 0.18 eV | 8O*+OH*(Mn) −14.92（rank 1）；8O*+O*(Mn) −14.74（rank 2）；差 0.18 | 一致 |
| Mn–NC：O 比 OH 稳定 0.30 eV | MnNC O bri −0.48（rank 1）；MnNC OH −0.18（rank 2）；差 0.30 | 一致 |
| Mn–NC 1O* 为"轴向 O" | `MnNC O bri` 名称带 bri，但 T032/T033 已从 CONTCAR 确认 O–Mn 1.577 Å、O–N ≥ 2.80 Å，是轴向 Mn=O | 一致；图 S24 图注也写 axial O on Mn |

注意：0.30 eV 用的是 `MnNC O bri`，不是 `MnNC O`（−0.12，rank 3）。若用后者，OH 反而比 O 稳定 0.06 eV，结论相反。SI 里引到这两个数的地方都应写明取的是各自最低能构型。

## 二、第 5 题：编号顺延（点名项）

### 2.1 一个须先定的问题：段中"(Table S6)"引的是什么？
- 0.18/0.30 eV 这两个数现在在**原表 S10**（覆盖候选与自由能），不在任何"新表"里。
- 正文目前**从未引用原表 S6**（颗粒–载体结合与结构恢复，只在 SI 2.14 节引用），原表 S10 在正文中首次出现于数据说明段（L50 "Tables S10 and S11"）。
- 所以有两种做法，结果不同：
  - **A. 新表 S6 = T038/T038b 数据表**，且同时列出 0.18/0.30 eV（注明取自表 S11 即原 S10）：段中"(Table S6)"成立，正文表格首次引用顺序为 S5 → S6（新）→ S7（原 S6 不在正文出现）→ S8…，顺序合规。
  - **B. 新表 S6 只放 Bader/dz² 数据**：则 0.18/0.30 eV 那句应引"Table S11"（原 S10），会在 S8–S10 之前首次出现，正文表格引用顺序被打乱；T038 的数据句应改引 Table S6 而不是只引 Figure S25。
- 建议 A，并请 Claude web 在方案里写明新表 S6 的内容。下文按"新图 S25、新表 S6 都插在原号之前，原号整体 +1"列出。

### 2.2 正文需改的 13 处（段落行号按 docx 提取顺序）
| 行 | 原文 | 改为 |
|---|---|---|
| L40 | OH* removal, respectively (Table S7) | Table S8 |
| L40 | O-covered particle (Table S8 and Figure S25) | Table S9 and Figure S26 |
| L40 | three pathways at 0.78 V, and Figure S26 | Figure S27 |
| L40 | overpotentials of 0.45, 0.89, and 0.97 V (Table S7) | Table S8 |
| L43 | metals in FeCo–NC (Figure 6a and Table S9) | Table S10 |
| L44 | metal–O bonds (Figure 6d, Figures S27 and S28) | Figures S28 and S29 |
| L44 | larger −ICOHP values (Figure 6e and Table S9) | Table S10 |
| L44 | gained by the intermediates (Figure 6g and Figure S30) | Figure S31 |
| L44 | nearly constant for the three catalysts (Table S7) | Table S8 |
| L46（图 6 图注） | arithmetic mean … three atoms (Table S9) | Table S10 |
| L46（图 6 图注） | bond-resolved curves are shown in Figure S29 | Figure S30 |
| L50 | ORR pathways are provided in Tables S10 and S11 | Tables S11 and S12 |
| L39（本段原句） | The corresponding structures are shown in Figure 5g and Figure S24 | 已并入括号，S24 不变 |

不受影响：图 S1–S24、表 S1–S5、公式编号 S1–S35、参考文献编号。

### 2.3 SI 需改的 48 处
- **目录**：图 S25–S33 → S26–S34（9 条），表 S6–S11 → S7–S12（6 条），并插入新图 S25、新表 S6 两条；页码从新图 S25 起顺延。
- **图注标题**：图 S25–S33 → S26–S34（9 条）；表 S6–S11 标题 → S7–S12（6 条）。
- **SI 正文与图注内的交叉引用（18 条）**：
  - 2.4 节：`(Table S10 and Figure S23)`、`code in Table S10` → Table S11（2 处）
  - 2.5 节：`The coverage curves and Table S10` → S11；`ORR free energies in Table S7` → S8
  - `matched relaxation energies in Table S11` → S12
  - 火山图节：`at their ΔGOH* values (Table S7)` → S8
  - PDOS 节：`Site-projected spectra (Figure S27)` → S28；`orbital-resolved PDOS in Figure S28` → S29
  - 电荷差节：`(Figure S31)` → S32；`(Figure S32)` → S33；`(Figure S33)` → S34
  - 2.14 节：`(Figure S11a and Table S6)`、`(Figures S11b, c and S12 and Table S6)` → Table S7（2 处）
  - 图 S13、S15、S16 图注：`Configuration codes are listed in Table S10` → S11（3 处）
  - 图 S27 图注：`listed in Table S9` → S10
  - 图 S33 图注：`planar-averaged Δρ of Figure S32` → S33

逐处清单（含原句上下文）由脚本从 docx 生成，可复现：正文 13 处、SI 48 处，与上表一致。

### 2.4 顺带发现（与本次改动无关，原稿已有）
- 正文段落只引了图 S30，图 S29 只出现在图 6 图注里；若期刊要求正文按序引用，图 S29（顺延后 S30）应在正文中也提一次，或与 S30 对调。
- 图 S11、S12、S23 和原表 S6 正文未引，只在 SI 内引用。一般可以，提一下。

## 三、第 1–4 题（从数据一致性角度，供 Claude web 参考）

1. **新末句是否由证据得出**：基本成立，但有两点。
   - 段中只写了"删颗粒、几何不动"（C vs C_support、A vs As），没写 As vs B（删颗粒结构对独立优化的 Mn–NC：−0.040 e，dz² +0.002 eV）。末句说"不体现在裸 Mn 上"，严格说还需要 As vs B 排除"颗粒通过改变载体几何间接改变 Mn"。建议在句中或图 S25 图注里带上这一项，否则末句只覆盖了"直接电子效应"。
   - T038 只算了无配体 Mn，所以只能说"影响不体现在裸 Mn 上"；不能说影响来自何处（如颗粒表面 8O* 与轴向配体的相互作用）。现在的末句没有越界，保持。
2. **与下一段的呼应**：变弱了。原来段末"structures … Figure 5g and S24"紧接"On these covered surfaces"；现在中间隔了四句，最后一句讲的是"bare Mn single atoms"，"these covered surfaces"的先行词离得远，容易被读成刚提到的裸 Mn。建议下一段改成"On these surface states at 0.78 V"或"On the covered surfaces in Figure 5g"。
3. **pH 13 那句**：在 CHE 框架、RHE 标度下覆盖结果确实与 pH 无关。但图 5 讲的是"various potentials and pH"，图 S23、S24 图注都标了"0.78 V versus RHE and pH 13"。删正文这一句，图注也要一起改，否则不一致。建议保留，或缩成"pH 13 (0.1 M KOH)"。
4. **表达**：
   - "appears in the axial ligand"读着像中式表达，可考虑"is reflected in the axial ligand"。
   - 0.18/0.30 eV 是 0.78 V 下的值（OH 和 O 差一个质子–电子对，差值随电位变），句中没写电位，读者可能以为与电位无关。建议加"at this potential"。
   - "we removed the particles from the FeCoMn–NC model"：T038 有两个含颗粒模型（洁净颗粒、8O* 颗粒），图 S25 图注应写明两者都算了。另外 SI 2.14 节标题已有"removal/recovery"（指的是去掉吸附物），新方法若写进 SI，建议用不同措辞，避免混淆。

## 结论
- 0.18、0.30 eV 与表 S10 一致。
- 编号顺延：正文 13 处、SI 48 处（另加目录新增两条），清单见上。
- 须先定新表 S6 的内容（见 2.1），否则段中"(Table S6)"的引用可能是错的。
