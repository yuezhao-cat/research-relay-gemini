# FeCoMn-T007 收集 ATR-SEIRAS 方法综述，整理数据处理要点

- 发起方：Claude
- 日期：2026-11-14
- 用途：作为赵月今后处理原位红外数据的参考（通用资料，不限于本篇论文）

## 1. 找原文（能合法获取的全文放进仓库 `_methods/SEIRAS/`，拿不到全文的只记录书目和摘要）
- Uchida & Osawa, Review of Polarography 2016, 62, 93–100, "Probing the Electrochemical Interface by ATR-SEIRAS"
- Osawa, Bull. Chem. Soc. Jpn. 1997（SEIRAS 研究电化学动态过程的综述；Claude 凭记忆给出，**请核实标题、卷页是否存在**）
- Osawa 关于 SEIRAS 机理和实验方法的其他综述或书章（如 Handbook of Vibrational Spectroscopy、Topics in Applied Physics 中的章节）
- Lyu, Xu, Wang, Front. Chem. 2023, 11, 1231886
- 近 5 年 ACS / RSC / Nature 系列中专门讨论电催化原位红外**数据处理或常见误区**的 tutorial、perspective 或方法论文（2–4 篇）
- Thermo Nicolet OMNIC 手册中关于背景采集和吸光度计算的部分

## 2. 整理成一份中文要点（`_methods/SEIRAS/数据处理要点.md`），每条注明出处页码
1. 背景谱与参比谱：各自是什么、常见选法（开路、高电位、双电层区），各自的优缺点
2. 吸光度和差谱的计算公式、正负号的含义
3. 基线校正的常用方法和注意事项
4. 平滑的常用参数和会带来的风险
5. 常见假信号：Si 棱镜吸收（具体峰位）、金膜变化、水蒸气和 CO₂、溶液本体、Nafion、温度漂移
6. 如何区分表面物种和溶液物种
7. 如何判断变化来自电位而不是时间（重复扫描、正反向电位扫描、空白实验）
8. 文献中推荐或常用的对照实验（空白电极、只有 Nafion、N₂ 饱和对比等）
9. 结果报告时应写明的信息（参比、基线、平滑、扫描次数、分辨率等）

- 只写资料里有出处的内容，没有出处的不写。
- 拿不到全文的资料，在要点里标明"仅据摘要"。

## 交付
- `_methods/SEIRAS/` 下的原文与要点文件（单个文件不超过 50 MB，注意版权，只放开放获取或已有合法副本的全文）
- `FeCoMn/from_agent/FeCoMn-T007/REPORT.md` 简述找到了什么、缺什么
- 更新 STATUS.md
