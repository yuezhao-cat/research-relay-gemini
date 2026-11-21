# FeCoMn-T033 图 6 出图（a–e），f 待 T032

依据：discussion/20261118_1500_Fig6_plan_Claude.md 第八、九节；数据路径见 review/Fig6_Antigravity.md（a5a80c1）。取代 T029。

## 出图前核对（先做，写入 REPORT）
- a、b 所用 FeCoMn–NC（Genkai FCMnew_base_full）与 Mn–NC（IMR MnNC_base_full）结构，与 ORR 计算所用工作表面背景（8O* + Mn–OH；Mn=O）为同一 CONTCAR、同一原采用分支。不一致则停下报告，不出图。
- c、d 的 OOH*/O*/OH* 结构与表 S7、S9 所用一致。

## 排布（3×3，六面板）
| 行 | 第 1–2 格 | 第 3 格 |
|---|---|---|
| 一 | a 轴向键 −pCOHP：Mn–OH（FeCoMn–NC，Mn238–O247）vs Mn=O（Mn–NC，Mn179–O180），标键长 1.88/1.58 Å 与 −ICOHP 2.64/8.03 eV | b 吸附前两 Mn 分组柱状图：Bader 电子数 11.46/11.51 e、εd −3.42/−3.44 eV、磁矩 3.21/0.29 μB（可用三个小子坐标） |
| 二 | c 反应侧 Mn–O −pCOHP：OOH*、O*、OH* 三列，标 −ICOHP（3.12/2.65、6.46/6.18、3.06/2.72），与 a 上下对齐、能量轴一致 | d Bader：Mn 失电子与中间体得电子并排（OOH*、OH*） |
| 三 | e 火山图 U_L vs ΔGOH*，三样品 | f 机理示意（跨两格），T032 后另行下发 |

## 要求
- 只比较 FeCoMn–NC 与 Mn–NC；FeCo–NC 只在 e 中出现。
- 沿用原图 6 配色、字体、线宽（FeCoMn–NC 红、Mn–NC 橙、FeCo–NC 紫）。
- f 位置先留空。不新算。不改 Word。
- 原图 6a 热图、FeCo–NC 电子结构、OOH* PDOS、吸附后四态 εd 移 SI（并入 S27–S30），本任务只列出移动清单，SI 图先不改。

## 交付
from_agent/FeCoMn-T033/：Figure6_draft.png、各面板数据表、REPORT.md（含核对结果）。更新 STATUS.md。

## 补充（11-18 15:35，依据 review/Fig6_Antigravity_data_check_Codex_20261118.md，79351a0）
1. Mn–NC 的 COHP 来源静态（Mn 0.001 μB，−1667.7722 eV）与 Bader/PDOS 来源静态（0.287 μB，−1667.7795 eV）不是同一电子态。处理：在 0.287 μB 那次静态上补跑 LOBSTER（同基组、同能量窗口），a 中 Mn=O −pCOHP 与 −ICOHP 改用该结果，使 a、b 出自同一波函数。先核对该静态 CONTCAR 与 ORR 所用 Mn=O 背景一致。新旧 −ICOHP 并列报告。
2. 更正 Bader 错误路径；εd 精确值按 Codex 复读的来源更正（两位小数不变）。
3. FeCoMn–NC 两面板同源（均 3.206 μB，−2140.0967 eV），无需处理。
4. 上述完成并由 Antigravity 复读确认后出图。

## 补充（11-18 15:45，依据 Codex 报告 a875f06，取代 15:35 补充第 1 条）
- 采用 Codex 方案：Mn–NC 以 COHP 独立静态（0.001 μB）为 a、b 共同来源，在其现有波函数和电荷文件上做 Bader 后处理，不跑 DFT。
- 前提：该静态须能提取 Mn 投影 PDOS（DOSCAR 含投影）以得到 εd。能则 a、b 全部用该静态（b 中磁矩写其实际值）。不能则报告，改回在 0.287 μB 静态上补跑 LOBSTER（需确认其 WAVECAR 存在）。
- 曲线使用 Codex 从正确原文件另存的完整曲线，不用 Antigravity 引用的错列 CSV。
- 统一后由 Antigravity 复读确认，再出图。

## 补充（11-18 15:52，赵月定）
c 不放 O*，只画 OOH*、OH* 两列（O* 非核心；FeCoMn–NC O* 电子结构分支未定）。O* 留 SI 图 S29。T032 中 FeCoMn O* 静态核对不再为图 6 所需。

## 补充（11-18 15:53，赵月定，取代 15:35、15:45 补充中的统一要求）
不重新计算、不补后处理。Mn–NC：a 用 COHP 独立静态（0.001 μB），b 用 Bader/PDOS 静态（0.287 μB）的原数据（Bader 11.51 e、εd −3.44 eV、磁矩 0.29 μB）。两静态结构相同、能量差 0.007 eV，差异微小，在 SI 方法中说明两面板来源。曲线用 Codex 另存的正确完整曲线；εd 精确值按 Codex 复读来源更正。数据齐全，可直接出图 a–e。
