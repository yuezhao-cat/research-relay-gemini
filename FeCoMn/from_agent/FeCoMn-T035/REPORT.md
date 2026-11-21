# FeCoMn-T035 交付报告：SI 图 S17–S22 重新配色（C/H 拉开对比）与逐面板核对（导师批注 #197）

- **读取任务单提交号**：`0ba2983`（`FeCoMn/to_agent/FeCoMn-T035_SI_S17-S22_legend_check.md`）
- **核对基准**：现行最新 SI 文档 `FeCoMn/manuscript/FeCoMn_SI_revised_20261117_2250.docx`、原始渲染脚本 `cov_structures_20261101.py` 及参考自由能/原子数表 `coverage_library_reference_with_joint.csv`
- **范围确认**：未修改 Word 文档（`.docx`），未提交任何新 DFT 计算，全部 130 个结构均从 IMR / Genkai 原始 `CONTCAR`（经 `E(sigma->0)` 0.000 eV 校验）只读拉取并重新渲染。

---

## 1. 旧版问题原因与本次配色修改

- **旧版原因定位**：原脚本 `cov_structures_20261101.py` 中，`key_C.png` 本身为极浅灰白（中心 RGB `[230, 230, 230]`），而 `SPR['H']` 又设为 `sprite('C') * 1.04 + 6`，导致 `C` 与 `H` 颜色与尺寸几乎无法区分（例如 S17 中 `8H*–NP`、`7H*–NP`、`6H*–NP`、`5H*–NP` 上颗粒边缘的 H 原子与基底 C 混成一片）。
- **本次统一修改**：
  - **C**：调暗为明显中灰色（`sprite('C') * 0.62`，保留 3D 球面高光，半径 `0.36`）。
  - **H**：采用**浅青绿色（cyan-mint）立体球**（不再用白色，在白底图例和灰色 C、浅蓝 N、砖粉 Fe、蓝灰 Co、大红 O 旁均清晰可辨），**半径调大至 `0.35`**，确保 `8H*–5H*` 等高覆盖结构中的每个 H 原子在缩小面板中也可一眼数清。底部图例中的 `C` 与 `H` 球标同步按此配色与尺寸渲染。
  - **Fe / Co / Mn / N / O**：完全沿用正文图 5 / 图 6 的原始 `key_*.png` 球形 sprite 配色不变。

---

## 2. 交付图件清单（对应最新 SI 图号 S17–S22，600 dpi PNG + SVG + 预览 PNG）

| 图号 | 对应体系与内容 | 面板数 | 尺寸 (mm) | 文件 |
|---|---|---:|---:|---|
| **Figure S17** | `FeCoMn–NC` supported-model coverage candidates (part 1) | 24 | 160.0 × 216.5 | `Figure_S17.png`, `Figure_S17.svg`, `Figure_S17_preview.png` |
| **Figure S18** | `FeCoMn–NC` supported-model coverage candidates (part 2) | 22 | 160.0 × 216.5 | `Figure_S18.png`, `Figure_S18.svg`, `Figure_S18_preview.png` |
| **Figure S19** | `FeCo–NC` supported-model coverage candidates | 22 | 160.0 × 213.4 | `Figure_S19.png`, `Figure_S19.svg`, `Figure_S19_preview.png` |
| **Figure S20** | `Mn–NC` coverage candidates | 18 | 160.0 × 117.6 | `Figure_S20.png`, `Figure_S20.svg`, `Figure_S20_preview.png` |
| **Figure S21** | `FeCo(110)` particle-submodel coverage candidates (part 1) | 25 | 160.0 × 203.2 | `Figure_S21.png`, `Figure_S21.svg`, `Figure_S21_preview.png` |
| **Figure S22** | `FeCo(110)` particle-submodel coverage candidates (part 2) | 19 | 160.0 × 164.3 | `Figure_S22.png`, `Figure_S22.svg`, `Figure_S22_preview.png` |

---

## 3. 逐面板结构与图像查重核验结果

详见完整逐面板核对表：`FeCoMn/from_agent/FeCoMn-T035/S17_S22_panel_verification.csv`（共 130 行）。

- **原始 `CONTCAR` 能量一致性**：全部 130 个结构来自 IMR / Genkai 原始计算目录，`OUTCAR` 末步 `energy(sigma->0)` 与 `coverage_library_reference_with_joint.csv` 最大偏差 **`0.000000 eV`**。
- **实际三维几何成键计数核对**：脚本直接读取每个 `CONTCAR` 的三维周期性最小像距离（判定 $\text{O–H} < 1.25\text{ \AA}$、$\text{O–O} < 1.70\text{ \AA}$），逐一数出 `O_total`, `H_total`, `O_only`, `OH`, `OOH`, `H_only`。**130/130 全部与标签及参考表 100% 一致**（例如 `S17` 第一排 `8H* @ particle` 至 `5H* @ particle` 的实测 `H_only` 严格为 `8, 7, 6, 5`）。
- **重复性检查**：
  - 独立 `CONTCAR` SHA256 数量：**130 / 130**（无任何两个面板共用同一结构文件）。
  - 独立单面板渲染图 SHA256 数量：**130 / 130**（无任何两个面板图像相同）。
- **供 GPT（Codex）交叉核对提示**：`S17_S22_panel_verification.csv` 中已附全部 130 个超算 `remote_contcar_path`、`contcar_sha256`、`E_sigma0_eV` 与各吸附物实测原子数，可直接按行复核。
