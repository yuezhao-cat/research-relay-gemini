# FeCoMn 任务看板

## 写作单元（按 ROLES.md v3；每步结束更新本表）
Word 锁：Claude web　当前正式稿：manuscript/FeCoMn_Manuscript_revised_20261119_2255.docx、FeCoMn_SI_revised_20261119_2255.docx（8dc699c）

| 单元 | 负责 | 当前版本（文件 / 提交） | 下一步 | 待谁 | 额度水位 |
|---|---|---|---|---|---|
| 摘要 | Claude web | review/20261121_1430b_abstract_synthesis2_ClaudeWeb.md（22c6f52） | 先冻结，图 6/图 5 后回改 | 赵月定 DECISIONS 待定项 | |
| 图 6 段 | Claude web | 未开 | 开单元文件 | Claude web | |
| 图 4 电位标签 | Codex / Antigravity | 现图 4 末条标 −0.08 V | 改 0 V（标签格式待赵月定） | 赵月 | |
| FACTS 复核 | Antigravity（复核）、Claude Code 本地（互核） | FeCoMn/FACTS.md | 逐条复核打"已复核" | Antigravity | |


协作规则见 README.md（Claude 写作与任务单，Codex 计算出图，Antigravity 核查，赵月决定）。

| 编号 | 标题 | 负责方 | 状态 | 日期 | 对应文件 |
|---|---|---|---|---|---|
| FeCoMn-T018 | 图5定稿0.78 V交付及Claude替换说明 | 智能体 | 已交付（用户指定PNG同字节，待Claude替换） | 2026-11-17 | from_agent/FeCoMn-T018/CLAUDE_REPLACE_FIGURE5.md |
| FeCoMn-T001 | Figure 4 重画 | 智能体 | 已确认（主版作为T002底版，蓝移只写正文） | 2026-11-14 | from_agent/FeCoMn-T001/REPORT.md |
| FeCoMn-T002 | Figure 4 精简标注（含补充1：a 配色出 C 紫、D 红两版） | 智能体 | 已确认（选 D 红色版，见 T003） | 2026-11-14 | from_agent/FeCoMn-T002/REPORT.md |
| FeCoMn-T003 | Figure 4 下排改三张色图与上排对齐（a 用 D 原配色） | 智能体 | 已确认（作为 T008 底版） | 2026-11-14 | from_agent/FeCoMn-T003/REPORT.md |
| FeCoMn-T004 | 查找 FeCoMn–NC 全部原位红外原始数据 | 智能体 | 已确认 | 2026-11-14 | from_agent/FeCoMn-T004/REPORT.md |
| FeCoMn-T005 | 文献核对：1000 以下三个谷和 1215 归属 | 智能体 | 已确认 | 2026-11-14 | from_agent/FeCoMn-T005/REPORT.md |
| FeCoMn-T006 | 导出赵月旧 Origin 工程（4 个 .opju）并与原始数据配对 | 智能体 | 已确认 | 2026-11-14 | from_agent/FeCoMn-T006/REPORT.md |
| FeCoMn-T007 | 收集 ATR-SEIRAS 方法综述并整理数据处理要点 | 智能体 | 已确认 | 2026-11-15 | from_agent/FeCoMn-T007/REPORT.md |
| FeCoMn-T008 | Figure 4 加全景三维图、三层版面、统一美化 | 智能体 | 已确认（view2 作为 T009 底版） | 2026-11-15 | from_agent/FeCoMn-T008/REPORT.md |
| FeCoMn-T009 | 修改 T008：本文主色调、b 改错开堆叠（参考 v3）、范围与字母位置 | 智能体 | 已确认（选 view2） | 2026-11-15 | from_agent/FeCoMn-T009/REPORT.md |
| FeCoMn-T010 | Figure 4 最后修改：a 电位轴拉深、刻度重排，b 比例尺加粗 | 智能体 | 已交付 | 2026-11-15 | from_agent/FeCoMn-T010/REPORT.md |
| FeCoMn-T011 | 查清 2024-10-21 两片电极的测量顺序、预处理和同步电流 | 智能体 | 已交付 | 2026-11-15 | from_agent/FeCoMn-T011/REPORT.md |
| FeCoMn-T012 | Zotero 中查找用实验大数据引出问题的论文 | 智能体 | 待办 | 2026-11-15 | to_agent/FeCoMn-T012_zotero_big_data_papers.md |
| FeCoMn-T013 | 整理 ORR 数据库（全部 1484 条，不预筛） | 智能体 | 已交付 | 2026-11-15 | from_agent/FeCoMn-T013/REPORT.md |
| FeCoMn-T014 | 图 4a 改为全谱原始三维（1000–4000，白底红紫配色），b–e 不动 | 智能体 | 被 T015 取代 | 2026-11-15 | to_agent/FeCoMn-T014_Figure4_panel_a_full_spectrum.md |
| FeCoMn-T015 | 图 4 改两层（a 差谱三维 + b 差谱堆叠），四点基线，去 c/d/e，SI 原始谱 | 智能体 | 已确认（A版54mm定稿，待Claude插入Word） | 2026-11-16 | from_agent/FeCoMn-T015/20261116_A_single_bend1/REPORT.md |
| FeCoMn-T016 | Figure 4c 简化反应路径与完整图4交付 | 智能体 | 已确认（灰色虚线框白底版，Claude 已插入 Word） | 2026-11-16 | from_agent/FeCoMn-T016/20261116_final_gray_dashed/REPORT.md |
| FeCoMn-T017 | 在超算上查找干净表面 ORR 数据，与反应条件下表面状态对比 | 智能体 | 待办 | 2026-11-17 | to_agent/FeCoMn-T017_clean_surface_ORR_data_search.md |
| FeCoMn-T019 | 图 3 改版：g 占两格去插图，新增 h 为 31.6 h 前后 LSV；同步改 SI 图 S10 | 智能体 | 已完成，图已入正文与 SI（20261117_1710） | 2026-11-17 | from_agent/FeCoMn-T019/REPORT.md |
| FeCoMn-T020 | Levich 检查（极限电流偏高）与干净表面 ORR 数据明确答复 | 智能体 | Levich 部分赵月确认已解决；干净表面部分由 T025 取代 | 2026-11-17 | to_agent/FeCoMn-T020_Levich_check_and_clean_surface.md |
| FeCoMn-T021 | 图 5h 标注改为过电位 η，删掉 0.004/0.44/0.52 eV | 智能体 | 已交付，未入正文（箭头不按比例，见 T022） | 2026-11-17 | from_agent/FeCoMn-T021/REPORT.md |
| FeCoMn-T022 | 图 5h 删掉三个箭头，η 并入图例（样品名后） | 智能体 | 已完成，图已入正文（20261117_1755） | 2026-11-17 | from_agent/FeCoMn-T022/REPORT.md |
| FeCoMn-T023 | 导师批注中属于图的三条：#53 XRD 标相和晶面去卡片、#73 HRTEM 标碳层与颗粒、#197 S17–S22 图例配色与逐图核对 | 智能体 | #53、#73 已完成（图1d/1e 已入正文）；#197 未做，转 T035 | 2026-11-17 | to_agent/FeCoMn-T023_figure_comments.md |
| FeCoMn-T024 | 李昊老师单位全称（加作者用，回导师 #1） | 智能体 | 已完成，作者行已加（20261117_1830） | 2026-11-17 | from_agent/FeCoMn-T024/REPORT.md |
| FeCoMn-T025 | 取干净表面 ORR 能量（目录已指明，取代 T020 的干净表面部分） | 智能体 | 已交付；B 组指定背景不匹配，见报告 | 2026-11-17 | from_agent/FeCoMn-T025/REPORT.md |
| FeCoMn-T026 | 换背景补算 B 组，并给出 Mn 轴向配体随颗粒 O 覆盖度 0–8 的序列 | 智能体 | 已交付；2/4/6 点不满足核查条件，见报告 | 2026-11-17 | from_agent/FeCoMn-T026/REPORT.md |
| FeCoMn-T027 | Mn–NC 加轴向 OH 的 ORR 自由能（2×2 表最后一格） | 智能体 | 取消：当前主线不再需要（未开工，任务单保留作记录） | 2026-11-17 | to_agent/FeCoMn-T027_MnNC_axial_OH.md |
| FeCoMn-T028 | 图 6a 每面板单独标元素、统一行高、缺失原子留白（朱老师指出 FeCo–NC 看似有 Mn） | 智能体 | 取消：被 T029 取代（三面板统一行高使 Mn–NC 成空框，设计错误） | 2026-11-18 | from_agent/FeCoMn-T028/REPORT.md |
| FeCoMn-T029 | 图 6 改为六面板（OH 稳定性、2×2 结构、2×2 自由能、各步 ΔG、火山图、示意），旧两面板方案作废 | 智能体 | 取消：被 T033 取代 | 2026-11-18 | from_agent/FeCoMn-T029/REPORT.md |
| FeCoMn-T030 | 核实 Mn–NC 加轴向 OH 的 ORR 自由能，与 C 组比较以拆分颗粒与轴向 OH 的贡献 | 智能体 | 已确认（ΔGOH* 1.332，U_L 0.570，O*→OH*） | 2026-11-18 | from_agent/FeCoMn-T030/REPORT.md |
| FeCoMn-T031 | 统一 ISYM/NBANDS 静态取 PDOS/Bader/COHP；不考虑低能分支，全部用原采用结果 | 智能体 | 取消：数据均已有，不新算 | 2026-11-18 | from_agent/FeCoMn-T031/ |
| FeCoMn-T032 | 从现有计算中找"轴向配体 → 反位结合"证据（只查不算） | 智能体 | 已交付：五方向证据及最小补算清单，待交叉核查 | 2026-11-18 | from_agent/FeCoMn-T032/REPORT.md |
| FeCoMn-T033 | 图 6 六面板出图 a–e（先核对结构与 ORR 背景一致），f 待 T032 | 智能体 | 取消：被 T034 取代（六面板方案作废） | 2026-11-18 | from_agent/FeCoMn-T033/ |
| FeCoMn-T034 | 图 6 按 3×3 九面板预览出图（a 轴向键 COHP、b Mn 自旋 PDOS、c 吸附前 3d PDOS 为新；其余为原图） | 智能体 | 已交付（v2 九面板定稿及数据表，已通过核查） | 2026-11-18 | from_agent/FeCoMn-T034/REPORT.md |
| FeCoMn-T035 | SI 图 S17–S22 重新配色 C 与 H 图例并逐张核对（导师 #197） | 智能体 | v3 已交付（Claude Code 修正 S21/S22 PBC 显示问题：H–Fe 距离 1.552 Å 确认正常吸附，启用 wrap=True 修正边界折回；S22 第 1 格标签去括号；待 Antigravity 复核 S21 "1H* @ short bridge" 右侧 Co 球） | 2026-11-19 | from_agent/FeCoMn-T035/v3_20261119/REPORT.md |
| FeCoMn-T036 | 前言文献核查（P1–P2 及 [D] 碳骨架） | Antigravity 主查 / Claude Code 复核 | P1、P2 原文复核完成；[D] 碳骨架文献已由 Antigravity 从 Zotero 原文检索交付（Wang 2020 AM, Zhao 2024 AM），待 Claude Code 复核；待 P3 | 2026-11-19 | from_agent/FeCoMn-T036/P2_D_carbon_refs.md |
| FeCoMn-T037 | 图 6 补齐机理：轴向配体经 Mn dz² 改变 Mn–OOH* 成键（步骤 1–5） | Antigravity 主查 / Claude Code 复核 | 数据及步骤 4 图 6 草图 v2（乙方案，panel a 同源、dz² 独立归一化深色同色系）已交付，待 Claude Code 复核及用户定稿 | 2026-11-19 | from_agent/FeCoMn-T037/REPORT.md |
| FeCoMn-T038 | 无轴向配体状态下颗粒对相邻 Mn 电子结构的作用 | Antigravity 主查 / Claude Code 核查 | 独立复核并交付：确认 A/B 缺 LORBIT=11 静态；同时补齐此前遗漏的 `FCM_base_support`、`FCM_base_full/ACF.dat` 及 `FCM_interface` 差分电荷与区域积分，给出 C vs C_support 完整定量对比 | 2026-11-19 | from_agent/FeCoMn-T038/REPORT.md |
| FeCoMn-T040 | FCM 8O* 无轴向 OH 时 Mn–OOH* dz² ICOHP（LOBSTER） | **Claude Code 执行 / Antigravity 核查** | **计算中**：VASP 静态作业 617861 (CS_001, R)；工作目录 `/home/05926/zhaoyue/WORK/FeCoMn_T040_20261120`；收敛后转九州跑 LOBSTER；与 T037 有轴向 OH 的 1.38 eV 对比 | 2026-11-20 | to_agent/FeCoMn-T040_axial_OH_trans_COHP.md |
| FeCoMn-T038b | 补算 A/B/Ap/As 干净结构静态单点与差分电荷/PDOS/Bader | Claude Code 执行 / Antigravity 核查 | **已修订（commit 6f47d72）**：4 项后处理错误已按 Antigravity 核查真值改写；A/As Mn 均 ~3.1 μB 高自旋，A−As Bader +0.007 e，Δdz² +0.013 eV，E_int −4.242 eV，Mn-N4 局域 Δq +0.007 e | 2026-11-20 | from_agent/FeCoMn-T038b/REPORT.md |
| FeCoMn-T039 | 去掉颗粒后 Mn 轴向 OH 与 O 的相对稳定性 | **Antigravity 执行 / Claude Code 核查** | **计算中**：S-OH 作业 617431 (CS_001, R)；617432 为重复作业已终止；S-O 作业 617433 (TP_002, R)；工作目录 `/home/05926/zhaoyue/WORK/FeCoMn_T039_20261120/{S_OH,S_O}`；收敛后 Claude Code 独立复算 ΔG | 2026-11-20 | to_agent/FeCoMn-T039_ligand_preference_without_particle.md |
| FeCoMn-T041 | OOH* 吸附的几何形变 / 电子结合拆分（补 1 个静态） | **Antigravity 执行 / Claude Code 核查** | **已交付（Genkai 7633024 收敛）**：`OOH*` 基底形变增 `+0.432 eV`（`+0.253 → +0.685 eV`），冻结电子结合 `-2.178 → -2.278 eV`；与 `OH*`（`+0.236 / +0.100 eV`）并列写入 [from_agent/FeCoMn-T041/REPORT.md](from_agent/FeCoMn-T041/REPORT.md)，待 Claude Code 复核 OOH* | 2026-11-20 | from_agent/FeCoMn-T041/REPORT.md |


2026-11-16：T014的Claude评审已交回[from_agent/FeCoMn-T014/CLAUDE_REVIEW.md](from_agent/FeCoMn-T014/CLAUDE_REVIEW.md)，后续T015已落实四点基线/两层版式及本轮用户补充，交付3版待赵月选择。

2026-11-16：赵月确认Figure4最终A版，供Claude插入正文。唯一最终文件与尺寸见[from_agent/FeCoMn-T015/CLAUDE_INSERT_FINAL_20261116.md](from_agent/FeCoMn-T015/CLAUDE_INSERT_FINAL_20261116.md)。此前三版待选及C版选择均已被本次A版确认取代。

2026-11-16 20:10：Claude 已将 T016 定稿 Figure 4 插入正文，第 8 段与图注同步更新，新版本见 [manuscript/](manuscript/README.md)。

2026-11-16 用户追加决定：Figure 4 保留白底灰色虚线框版与94%透明度浅紫底无框版，暂待二选一；见[from_agent/FeCoMn-T016/FIGURE4_TWO_OPTIONS_20261116.md](from_agent/FeCoMn-T016/FIGURE4_TWO_OPTIONS_20261116.md)。本次不修改已插图的Word。

2026-11-16 20:15：赵月选定图 4 浅紫底无框版（20261116_option_purple94_no_border），灰色虚线框版不用。Claude 已插入 Word，现行版本 manuscript/FeCoMn_Manuscript_revised_20261116_2015_purple.docx。

2026-11-17 10:00：Claude 已将 T018 定稿图 5 插入正文，0.78 V 相关数值与图注同步，见 manuscript/FeCoMn_Manuscript_revised_20261117_1000.docx。注意：Claude 下达的干净表面数据任务编号为 T017，与智能体图 5 交付 T018 不同。

2026-11-17：FeCoMn-T017 已交付。完成 IMR Tohoku 与 Genkai Kyushu 现有 ORR 计算的只读全量检索、关键路径收敛/参数/能量核查及 S7/S11 口径自由能计算；报告、路径清单和可复核脚本见 [from_agent/FeCoMn-T017/](from_agent/FeCoMn-T017/)。发现 `FCM_cov8O_OOH` 与 S11 FCM–OOH 不是同一构型，已在报告中标出，未擅自替换。


## 第三方核查（Antigravity）

| 任务 | 核查结论 | 日期 | 文件 |
|---|---|---|---|
| FeCoMn-T038b | **不通过（DFT 有效，报告含 4 项后处理硬错待改）**：`A/As/B` Mn 实际均在 `|μ|≈3.11–3.13 μB` 高自旋态；`dz²` 上移仅 `+0.013 eV`（`[-8,0]`）；`E_int = −4.242 eV`；三维 `Mn–N4` Δq `+0.0074 ~ +0.0090 e` | 2026-11-20 | [review/T038b_Antigravity.md](review/T038b_Antigravity.md) |
| FeCoMn-T030 | 待核查 | | |
| FeCoMn-T031 | 待核查（交付后） | | |

- T037 (2026-11-19): 图6补 dz² 机理（统一MnNC静态+dz² PDOS/分项COHP）。Antigravity 执行，Claude Code 核查。
- 2026-11-19 23:00：新版 Manuscript/SI 20261119_2255（标题、摘要、前言三段、结论）；标题未定稿，见 _shared_memory/inbox/20261119_2300_FeCoMn_20261119进展.md
