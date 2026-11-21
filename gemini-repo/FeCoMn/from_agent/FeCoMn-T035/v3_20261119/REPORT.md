# T035 v3 修改报告（Claude Code，2026-11-19）

读取审稿意见提交：`571d6c6`（`FeCoMn/review/T035_Claude_review_20261119.md`）

---

## 修改内容

### 1. S21 "1H* @ Fe atop"——H–Fe 距离核实与 PBC 修正

**原始数据（IMR）**：`/home/05926/zhaoyue/WORK/FeCoMn_ch5_recalc_20261007/slab110/1H_topFe/CONTCAR`

**H–Fe 距离计算**（三维 PBC 最小像）：

| 配对 | 距离 |
|---|---|
| H → Fe[3]（frac y≈0.0，与 H 的 y≈1.0 在 PBC 下等价） | **1.5524 Å** |
| H → Fe[7]（次近） | 3.2606 Å |

结论：H 确实吸附在 Fe atop 位，键长 1.552 Å，物理合理（1.5–1.6 Å）。  
H 分数坐标 y≈1.0000，对应 Fe[3] y≈0.0000；未做 PBC 折叠时，渲染器将两者画在 y 方向相反边缘，导致 H 看似脱附。

**修复方法**：在 `place()` 中对 FeCo(110) submodel 同样启用 `wrap=True`（v2 中该体系为 `wrap=False`），以 Fe/Co 质心为中心折叠所有原子到 [-0.5, 0.5] 分数坐标区间。H 从 y=1.0 折回 y≈0，与 Fe[3] 在同一侧渲染，键线正常显示。**未修改 CONTCAR 结构文件。**

### 2. S21 其他面板——边界 Fe/Co 原子

同样通过 `wrap=True` 修正。8H\*/6H\*/4H\*/2H\* @ hollow sites 等面板不再出现伸出板外的孤立 Fe/Co 球。

### 3. S22 第 1 格标签

"6OH\* @ atop sites (continued)" → **"6OH\* @ atop sites"**  
（`(continued)` 是计算续算目录名，不应出现在图中；结构唯一，不存在重复。）

---

## 待 Antigravity 确认的一处疑点

**S21 "1H\* @ short bridge"**：右侧可见一个孤立大蓝球（Co）。  
可能原因：该位点的 H 位于两个 Co 原子之间，其中一个 Co 位于周期边界；`wrap=True` 后该 Co 仍在面板边缘显示。  
请 Antigravity 对照 `slab110/1H_sb/CONTCAR` 确认该原子是否属于正常结构（周期像），以及是否需要进一步处理。

---

## 交付清单

`v3_20261119/` 下（相对于 `from_agent/FeCoMn-T035/`）：

| 文件 | 说明 |
|---|---|
| `Figure_S21.png` | 600 dpi，160×205.9 mm，25 面板 |
| `Figure_S21.svg` | 矢量版 |
| `Figure_S21_preview.png` | 200 dpi 预览 |
| `Figure_S22.png` | 600 dpi，160×166.6 mm，19 面板 |
| `Figure_S22.svg` | 矢量版 |
| `Figure_S22_preview.png` | 200 dpi 预览 |
| `REPORT.md` | 本文件 |

旧版本（v2）文件保留在 `from_agent/FeCoMn-T035/` 根目录，未覆盖。

---

**复核请求**：请 Antigravity 确认以下两点后，由赵月（网页版 Claude）将 v3 图换入 SI：
1. "1H\* @ Fe atop" H 位置是否正确（H 青绿球是否贴合 Fe 顶端）。
2. "1H\* @ short bridge" 右侧孤立 Co 球是否属正常周期边界显示。
