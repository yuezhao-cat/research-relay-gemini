# 三套摘要方案（赵月转来）及 Claude Code 云端审阅（2026-11-21）

来源：赵月转来的另一智能体文字，含"核心难点诊断"与方案一（工作态表面配位，204 词）、方案二（保留颗粒共存背景，203 词）、方案三（精炼版，180 词）及各自自查清单。原文见本会话；下面只记方案二全文（推荐底稿）和审阅意见。

## 方案二原文（推荐作为底稿）
Metal particles commonly coexist with single-atom sites in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet catalytic models often rely on bare single-atom surfaces. How the surface state formed under working conditions governs oxygen reduction reaction (ORR) intermediate binding remains unclear. Here, we prepare a FeCoMn–NC catalyst combining bcc FeCo alloy particles with dispersed Mn–N₄ sites. In 0.1 M KOH, FeCoMn–NC delivers a half-wave potential of 0.885 V versus RHE, surpassing commercial Pt/C, FeCo–NC, and Mn–NC. It further retains 96.5% of its initial current over 238 h. Operando infrared spectroscopy tracks potential-dependent interfacial water evolution and OOH* accumulation, showing that ORR proceeds via an associative pathway on a covered surface. Surface-coverage calculations at 0.78 V versus RHE reveal O*-covered FeCo particles alongside Mn–N₄ sites coordinated by an axial OH. Whereas bare Mn–N₄ sites bind ORR intermediates too strongly, the axial OH pulls Mn out of the N₄ plane. When an ORR intermediate adsorbs on the opposite side, it draws Mn back toward the N₄ plane. This opposing displacement offsets part of the adsorption energy and moderates the overly strong binding. Consequently, OH* removal becomes downhill at 0.78 V while OOH* formation remains nearly thermoneutral, placing FeCoMn–NC near the ORR activity volcano apex.

## 审阅意见
三套的机理链（裸 Mn 过强 → 轴向 OH 把 Mn 拉出平面 → 对侧吸附拉回 → 消耗部分结合能 → OH* 脱除下坡、OOH* 近热中性）与 T041/T042 数据一致（带 OH 时 Mn +0.44 Å，吸附后 OOH* 0.00、O* −0.10、OH* −0.01 Å；削弱主要来自形变）。可用。

推荐方案二：保留了赵月最满意版的"颗粒与单原子共存"开头，后面的 bcc FeCo 才有交代。方案一"often modeled as bare"、方案三"rarely remain bare"是大断言，且把颗粒背景丢了。

方案二需改 5 处：
1. "Whereas bare Mn–N₄ sites bind … too strongly, the axial OH pulls Mn out…"：whereas 表对比，这里逻辑是因果，应拆成两句："Without the axial OH, Mn binds ORR intermediates too strongly. The axial OH pulls Mn out of the N4 plane, …"
2. "OOH* accumulation" / "showing that"：1215 cm⁻¹ 带与 Nafion C–F 重叠、1.12/1.02 V 已有信号，"accumulation"偏强；用正文原措辞 "detects OOH*, an intermediate of the associative pathway"。
3. "Mn–N₄ sites"：正文和赵月版都用 "Mn single atoms"，关键词也计划改为 Mn single atom，统一。
4. 结尾缺"→ 活性最高"的落点：赵月版有 "which explains its highest measured activity"，建议加回。
5. "surpassing … FeCo–NC, and Mn–NC"：赵月定的是"Mn–NC 和 FeCo–NC 的对比不放摘要"。实测性能并列不是机理对比，但需赵月确认是否保留。

另："Here, we prepare a FeCoMn–NC" → "an FeCoMn–NC"（读作 eff）。
标题须同时去掉 "Determine"，候选见 20261120_abstract_final_proposal_ClaudeCode_cloud.md。
