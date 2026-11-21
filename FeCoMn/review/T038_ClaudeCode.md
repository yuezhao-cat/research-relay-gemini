# T038 Claude Code 核查报告

Claude Code，2026-11-19。  
本次由 Claude Code 同时执行数据查阅和核查，原始来源均为已 commit 至 research-relay 的 T017/T025/T026/T032 数据。  
核查原则：只读 HPC 已提取数据，不跑新 DFT，不改 Word。

---

## 核查结论

**T038 任务因 A（FCM clean）和 B（MnNC clean）缺少 LORBIT=11 静态，无法完整执行。**  
REPORT.md 准确反映了实际数据可用性，无数值错误，无捏造数据。

### 数据溯源核查

| 结论 | 来源文件 | 核查状态 |
|---|---|---|
| A：IMR 优化，无 LORBIT，无 LAECHG | T025/manifest.csv INCAR 字段（LORBIT 缺失）；T032/imr_selected_outputs.json `DOS_error=''` 且 `Mn_moment=null` | **✓ 通过** |
| B：IMR 优化，无 LORBIT，无 LAECHG | 同上，MnNC_clean 条目 | **✓ 通过** |
| C：FCM_base_full，Genkai，LORBIT=11，LAECHG | T032/genkai_selected_outputs.json `LORBIT: 11, LAECHG: .TRUE.`；`normal_end: true` | **✓ 通过** |
| C dz² 中心 −3.013 eV，d 中心 −3.083 eV | T032/genkai_selected_outputs.json `dz.center_eV: -3.0135, d_center_eV: -3.0830` | **✓ 通过** |
| C Mn 局域磁矩 3.116 μB | T032/genkai_selected_outputs.json `Mn_local_moment: 3.116` | **✓ 通过** |
| FCM_base_particle 存在于 Genkai | T017/genkai_inventory_raw.json 包含 `FeCoMn_electronic_20261023/FCM_base_particle` | **✓ 通过** |
| A 颗粒单独静态不存在 | T017 Genkai 全量清单中无对应 FCM_clean 片段目录 | **✓ 通过** |
| C 的 MnNC 载体片段不存在 | T017 Genkai 清单无 FCM_base_substrate 目录 | **✓ 通过** |

### 注意事项

T032 genkai FCM_base_full 条目中 `nearby_O[index=247]` 在 246 原子结构中超出范围（1-based Mn=238，O=239–246）。REPORT 未引用此字段做定量判断，不影响 dz²/d 中心和磁矩的正确性。建议 T032 extraction code 检查 periodic image 处理逻辑。

**核查总结：REPORT.md 数据与来源文件一致，缺项陈述准确，所有需决策事项已明确列出，可提交。**
