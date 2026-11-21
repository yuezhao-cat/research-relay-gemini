# FeCoMn–NC — GPT consolidated abstract after multi-agent discussion

Date: 2026-11-21
Status: Recommended consensus candidate. Original manuscript and figures unchanged.

## Title candidate

Axial OH Formed under Working Conditions Moderates Oxygen Reduction Intermediate Binding on Mn Sites in FeCoMn–NC

## English abstract

Metal particles commonly coexist with single-atom sites in pyrolyzed metal–nitrogen–carbon (M–N–C) catalysts, yet catalytic models often rely on bare single-atom surfaces. How the surface states formed under working conditions govern oxygen reduction reaction (ORR) intermediate binding remains unclear. Here, we prepare an FeCoMn–NC catalyst containing FeCo alloy particles and atomically dispersed Mn single atoms. In 0.1 M KOH, FeCoMn–NC achieves a half-wave potential of 0.885 V versus the reversible hydrogen electrode (RHE) and retains 96.5% of its initial current over 238 h. Operando infrared spectroscopy reveals potential-dependent changes in interfacial species, motivating calculations of surface coverage under ORR conditions. At 0.78 V versus RHE, these calculations identify O*-covered FeCo particles and adjacent Mn single atoms coordinated by an axial OH. Without this axial OH, Mn binds ORR intermediates too strongly, making OH* removal unfavorable. Axial OH coordination pulls Mn out of the N₄ plane, whereas adsorption of OOH* or OH* on the opposite side draws Mn back toward the plane. The associated deformation offsets part of the favorable adsorption interaction, moderating the excessively strong binding. Consequently, OH* removal becomes downhill while OOH* formation remains nearly thermoneutral at 0.78 V. This balance places FeCoMn–NC near the apex of the calculated ORR activity volcano, consistent with its high experimental activity.

## 中文摘要

金属颗粒通常与单原子位点共存于热解制备的金属–氮–碳（M–N–C）催化剂中，但催化模型往往仍以裸露的单原子表面为基础。工作条件下形成的表面状态如何影响氧还原反应（ORR）中间体的结合仍有待阐明。本文制备了一种 FeCo 合金颗粒与原子级分散 Mn 单原子共存的 FeCoMn–NC 催化剂。在 0.1 M KOH 中，FeCoMn–NC 的半波电位达到 0.885 V（相对于可逆氢电极 RHE），并在连续运行 238 h 后保持初始电流的 96.5%。原位红外光谱揭示了界面物种随电位变化的特征，因此进一步通过理论计算分析了 ORR 条件下的表面覆盖状态。计算表明，在 0.78 V 下，FeCo 颗粒表面被 O* 覆盖，而相邻 Mn 单原子具有轴向 OH 配位。没有轴向 OH 时，Mn 对 ORR 中间体的吸附过强，使 OH* 脱除在热力学上不利。轴向 OH 将 Mn 拉出 N₄ 平面，而 OOH* 或 OH* 从相反一侧吸附时又促使 Mn 返回平面附近。由此产生的形变抵消了部分有利的吸附相互作用，从而缓解过强的中间体结合。因此，在 0.78 V 下，OH* 脱除转为热力学下坡，而 OOH* 形成仍接近热中性。这种平衡使 FeCoMn–NC 位于计算得到的 ORR 活性火山图顶点附近，与其较高的实验活性相一致。

## Multi-agent synthesis / decisions

Sources read:
- review/20261121_1430_abstract_synthesis_ClaudeWeb.md
- review/20261121_1420_abstract_synthesis_ClaudeWeb2.md
- review/20261121_abstract_synthesis_ClaudeCode_cloud.md
- discussion/20261121_abstract_synthesized_ClaudeCode.md
- review/20261121_abstract_synthesis_Antigravity.md
- discussion/20261121_Antigravity_replies_log.md
- Shared IDEAS_BOARD porosity resolution, and GPT earlier drafts.

1. Select proposal 2 opening. It acknowledges particle–single-atom coexistence but frames the research question as potential-dependent surface state and adsorption, not the unproven direct causal role of FeCo.
2. Keep within-same-background axial OH removal control (T032) as a mechanistic *starting point*, not Mn–NC/FeCo–NC mechanistic comparison. Experimental benchmark list omitted from this concise abstract; comparison stays in the main text.
3. Restrict operando IR to interfacial potential-dependent changes (T043 1215 cm−1 assignment disputed), not assert the OOH* species or associative pathway unequivocally proven by that band.
4. Indicate that FeCo O* coverage and axial OH are predictions of the adopted computational coverage model, not directly identified by operando experiment.
5. T042 geometric evidence: OH ligation draws Mn out ~0.442 Å; OOH*/OH* adsorption draws it toward plane. O* also changes position but slightly overshoots (~−0.098 Å); avoid universal 'each intermediate exactly in the plane'.
6. T041: extra substrate distortion for OH* +0.236 eV and for OOH* +0.432 eV; OOH* frozen interaction ~−0.100 eV (stronger), while OH* frozen interaction +0.100 eV (weaker). Hence use 'offsets part of the favorable adsorption interaction' instead of claiming all local bonding strengthened.
7. At 0.78 V on axial OH model, OH* removal approx −0.07 eV and OOH* formation ~+0.004–0.01 eV; unligated site has uphill OH* removal around +0.27 eV. Theoretical free-energy claims are not kinetic transition-state barriers or proof of experimental rate determination.
8. End at calculated activity volcano consistent with high experimental activity, rather than assert quantitative CHE/UL explains highest E1/2.
9. T039 Mn=O long/short electronic-state mismatch means no claim FeCo 'determines' ligand or shifts overoxidation onset by 0.47 V.
10. Porous carbon is a reasonable physical basis for two-sided electrolyte accessibility. User has clarified porous pyrolysis carbon as consensus. Do not claim only top side is electrolyte-accessible; periodic geometry supports exposed opposite-side sites, while specific experimental two-sided wetting is not directly proven. Accessibility is not presented as main blocker.
11. Do not re-open expensive DFT branch scans or alter published original manuscript without user approval.

## Remaining scientific limitation

The particle's distinct *causal* contribution to axial OH stability is not proved by current T039. If manuscript title still says 'FeCo Particles Determine...' it conflicts with this abstract. Proposed title is scoped to supported axial ligand adsorption mechanism.
