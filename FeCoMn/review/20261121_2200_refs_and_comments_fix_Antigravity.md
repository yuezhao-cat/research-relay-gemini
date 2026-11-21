# FeCoMn 2200 版参考文献与批注嵌套回复修复说明（Antigravity）

- **完成时间**：2026-11-21 21:46–21:51
- **依据任务与核查报告**：`FeCoMn/to_agent/FeCoMn-T045_intro_refs_verify.md` 及 `FeCoMn/review/20261121_T045_intro_refs_verify_Antigravity.md`（`901a22a`）
- **生成桌面 2200 版 Word 文件（原 2155 版未改）**：
  - `D:\OneDrive\Desktop\FeCoMn_Manuscript_revised_20261121_2200.docx`（黄标保留，批注修复）
  - `D:\OneDrive\Desktop\FeCoMn_Manuscript_revised_20261121_2200_clean.docx`（无黄标，批注同步修复）
  - `D:\OneDrive\Desktop\FeCoMn_SI_revised_20261121_2200.docx`（黄标保留，SI 编号补齐）
  - `D:\OneDrive\Desktop\FeCoMn_SI_revised_20261121_2200_clean.docx`（无黄标，SI 编号补齐）
- **同步纯文本**：`FeCoMn/manuscript/FeCoMn_Manuscript_revised_20261121_2200.txt`

---

## 1. 正文批注嵌套回复修复（OOXML 根因与全量校验）

- **现象与根因**：检查 `2155.docx`（含 `_clean` 版）全部 61 条批注（30 条 `admin` 批注、30 条 `Yue Zhao` 回复、1 条 `Author` 自注 `id=348`）发现：`commentsExtended.xml` 中全部 30 条 `Yue Zhao` 回复虽均已写入 `w15:paraIdParent`，但在 `word/document.xml` 中结构分裂：
  - 早期回复 `349–362`（含第 1 条 `0 -> 362`）将 `<w:commentReference w:id="child"/>` 与父批注 `<w:commentReference w:id="parent"/>` 放在**同一个 `<w:r>`** 内，且 `<w:commentRangeEnd w:id="child"/>` 紧挨着放在 `<w:commentRangeEnd w:id="parent"/>` 之前；
  - 后续插入的 **16 条**回复 `363–378`（含 `1 -> 367`、`52 -> 368`、`53 -> 376`、`73 -> 377`、`93 -> 375`、`131 -> 369`、`141 -> 370`、`147 -> 371`、`154 -> 372`、`197 -> 373`、`272 -> 366`、`276 -> 374`、`345 -> 365`、`310 -> 363`、`334 -> 364`、`347 -> 378`）把子批注的 `<w:commentReference>` 拆到了单独 `<w:r>` 中（其中 `363–377` 还排在父批注 `commentRangeEnd` 和 `commentReference` 之前），导致 Word/WPS 将其显示为另起的新批注。
- **修复与校验**：将全部 16 条异常回复（`363–378`）并入各自父批注的同一 `<w:r>` 内（`parent` 在前、`child` 在后），并清理空 `<w:r>`。在 `Manuscript_2200.docx` 与 `Manuscript_2200_clean.docx` 上脚本逐条断言：**30/30** 老师批注的嵌套回复结构完全一致（`same_<w:r>` 且 `c_ce < p_ce < p_r` 无异常，作者自注 `id=348` 保留原样）。

---

## 2. 正文前言 [F] / [G] 边界与文献编号修复

在 `Introduction` 第 2 段做最小改动，**保持 1–40 文献首次出现顺序严格 `[1..40]` 不变**：
1. **热解团聚句**：在 `...especially at high metal contents.` 后补上标 **`9,11`**（Jiang 2016 + Wan 2022 共同支撑）。
2. **`[F]` 精确对应 Wan 2022 原文**：`Carbon-encapsulated particles also remain after acid leaching...` 改为 `Carbon-encapsulated particles can also survive acidic conditions, so metal particles commonly coexist with single metal atoms.¹¹`。
3. **`[G]` 证据边界收敛**：`The activity of such catalysts is usually attributed to the single atoms alone.^(12,13)` 改为 `The activity of such catalysts is often attributed to the single atoms alone.^(12,13)`。

---

## 3. SI 遗漏的正文参考文献编号补齐

在保留 `Section 2.5`（`main-text ref. 3`）的前提下，于 `SI_2200.docx`（新增修改均标黄）与 `SI_2200_clean.docx`（0 高亮）中补齐 3 处共 10 个漏改编号：

| SI 位置 | 修改前（2155） | 修改后（2200） |
|---|---|---|
| Section 1 Characterization | `Larch²⁵` / `σ = 1.²⁶` | **`Larch²⁶`** / **`σ = 1.²⁷`** |
| Section 2.8 Volcano relation | `about 3.2 eV,^(5,22)` | **`^(4,23)`** |
| Table S4 `Ref.` 列（6 行） | `18 / 19 / 17 / 8 / 17 / 18` | **`19 / 20 / 18 / 10 / 18 / 19`** |
