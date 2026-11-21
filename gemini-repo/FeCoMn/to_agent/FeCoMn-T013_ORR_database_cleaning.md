# FeCoMn-T013 整理 ORR 数据库（尽量用全部 1484 条）

- 发起方：Claude
- 日期：2026-11-15
- 原始文件：`FeCoMn/data/ORR_database/ORR_raw_20261115.xlsx`（赵月提供，1484 行 × 46 列；列结构与 DigCat 平台一致，SHA256 见同目录）
- 原则：**不删行，不按电解液或任何条件预先筛掉数据**。所有清洗都以"新增标准化列"的方式完成，原始列原样保留，任何判断都留下依据。

## 1. 标识与去重标记（不删除）
- 每行加 `row_id`。
- 加 `catalyst_id`：同一 DOI + 同一 Formula 视为同一催化剂（目前约 898 个）。DOI 去掉首尾空格、统一小写后再比较。
- 加 `dup_flag`：标出同一催化剂的重复行，并写明重复原因（稳定性条目不同、电解液不同、完全相同等）。

## 2. 金属与元素
- `metals`：从 Elements 与 Formula 中识别金属元素，排序后用 "-" 连接；`n_metals`：金属种数。
- 逐条人工核对自动识别的易错情况：电解液或前驱体中的 K、Na、Li；Formula 中的缩写（如 "Co/NC" 中的 N、C 不是金属）；"Pc"、"COF"、"MOF" 等缩写。无法确定的标 `metal_uncertain=1` 并写原因。
- 原 Elements 为空或无金属（约 116 个催化剂）的，标 `metal_free_or_unknown`，并尽量从 Formula 判断是否为无金属 N–C。

## 3. 电解液（作为分组维度，不用于删数据）
- `medium`：alkaline / acidic / neutral / other。
- `electrolyte_std`：统一写法，如 "0.1 M KOH"、"1 M KOH"、"0.1 M HClO4"、"0.5 M H2SO4"、"0.1 M PBS"。
- `pH_est`：有 pH 列用 pH 列；没有的按电解液估算并标 `pH_estimated=1`。

## 4. 性能数据解析（把"数值@电位"拆成两列）
- 半波电位：数值化；非数值或单位可疑（如注明 vs Ag/AgCl、>1.2 V、<0.3 V）的标 `E12_flag` 并写原因，不删。
- 起始电位、圆盘电流密度、环电流、H₂O₂ 产率、TOF、质量活性、比活性：拆成 `value` 与 `at_potential`（V vs RHE）两列，统一正负号与单位；无法解析的保留原文并标记。
- 稳定性：拆成循环数、时长（h）、电位、衰减量与衰减指标；"10000S"之类的写法换算为小时并标注。

## 5. 结构类别（尽量全覆盖）
- `structure_class`：single-atom / dual-atom / particle-or-cluster / particle+single-atom / metal-free / unclear。依据 subType、Structural Property、Formula、Content 中的关键词（single atom, SAC, dual atom, DAC, nanoparticle, NP, cluster, alloy, @, encapsulated, carbide 等）。
- 每条写 `structure_evidence`（命中的原文片段）。`unclear` 的比例要报告；对 unclear 中涉及 Fe、Co、Mn 的条目，尽量用 DOI 对应论文的标题或摘要判断（只读题目和摘要，不必全文），并注明来源。

## 6. 年份、来源
- 年份数值化；统计每年条目数。
- Name / Institute 列不做处理，但统计提交者分布（用于说明数据来源）。

## 交付（`FeCoMn/from_agent/FeCoMn-T013/`，数据放 `FeCoMn/data/ORR_database/`）
- `ORR_clean_20261115.csv`：全部 1484 行，原始列 + 新增标准化列。
- `ORR_catalyst_level_20261115.csv`：每个催化剂一行（约 898 行），汇总其金属、结构类别、各电解液下的半波电位等。
- `cleaning_log.csv`：每一处人工修改或判断的行号、原值、新值、依据。
- REPORT.md：各字段可用条数（清洗前后）、金属/组合/结构类别/电解液的分布表、发现的数据问题；并查明 DigCat 平台的引用文献（平台介绍论文的作者、期刊、DOI）与数据使用条款。
- 更新 STATUS.md。
