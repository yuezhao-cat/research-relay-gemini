from pathlib import Path
import json,csv,hashlib,collections,re
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'FeCoMn/from_agent/FeCoMn-T013';DATA=ROOT/'FeCoMn/data/ORR_database'
stats=json.loads((OUT/'summary.json').read_text(encoding='utf8'))
rows=list(csv.DictReader((DATA/'ORR_clean_20261115.csv').open(encoding='utf-8-sig',newline='')))
cache=json.loads((OUT/'doi_metadata.json').read_text(encoding='utf8'))
def table(d):return '| 类别 | 行数 |\n|---|---:|\n'+'\n'.join('| '+(k or '空缺').replace('|','/')+' | '+str(v)+' |' for k,v in d.items())
lines=['# T013：ORR 数据库清洗报告','日期：2026-11-15。全量保留、追加标准化列；未改图、Word 或原始 Excel。',
f"## 交付与核验\n\n- 原表 1484 行 × 46 列，清洗表仍为 1484 行；46 个原始列逐单元格 CSV 回读比对一致。Excel 空单元格在 CSV 中表达为空字符串，原始多行文本、空格和大小写保留。\n- 原文件 SHA256：`{stats['raw_sha256']}`，与上传的 SHA256.txt 一致。\n- 按去首尾空格、小写 DOI ＋原 Formula 精确值分组，得到 **895 个催化剂**。没有把 Formula 的大小写或首尾空格合并；任务中的“约898”不是强制目标。\n- `dup_flag=1` 表示所在催化剂组有多行，不等于整行可删除；共有 {stats['duplicate_rows']} 行属于多行组。所有行均保留，催化剂级表的电解液性能 JSON 保留每个 row_id 及疑点，未擅取最大值或求平均。\n- 新增列为空表示不能可靠解析/缺失，不能按 0 使用。表中所有暂定值均须连同 flag、basis、evidence 使用。",
'''数据文件位于 `FeCoMn/data/ORR_database/`：

- `ORR_clean_20261115.csv`：原始列＋标准化列。
- `ORR_catalyst_level_20261115.csv`：895 个催化剂的全量汇总。

本目录另附 `cleaning_log.csv`、金属疑点表、结构未明表、DOI 元数据缓存、统计 JSON、验证结果及平台引用/条款核查。脚本在 `FeCoMn/scripts/T013_*.py`。CSV 为 UTF-8 BOM，以便 Windows Excel 正确显示。''',
'## 字段可用数量\n\n“可数值化”不等于已核实可跨文献比较；无 flag 数值仍可能缺配套测试条件或原论文确认。',
'| 字段 | 原始非空且非 NA | 可数值化 | 数值且无解析 flag |\n|---|---:|---:|---:|']
for k,v in stats['fields'].items():lines.append(f"| {k} | {v['before_nonempty']} | {v['after_numeric']} | {v['after_numeric_unflagged']} |")
lines.extend([f"\npH 有值 {sum(bool(r['pH_est']) for r in rows)} 行，其中估算 {sum(r['pH_estimated']=='1' for r in rows)} 行；来源数值优先。稳定性可解析循环数 {sum(bool(r['stability_cycles']) for r in rows)} 行、时长 {sum(bool(r['stability_hours']) for r in rows)} 行、损失/保留量 {sum(bool(r['stability_loss_value']) for r in rows)} 行。稳定性各指标可能重叠，不能相加当作独立测试。",
'''## 清洗口径与边界

1. `row_id` 从 1 起，对应 Excel 第 row_id+1 行。`doi_std` 仅去首尾空格、统一小写；不擅自修复疑似错误 DOI。
2. `metals` 按元素符号字母排序连接。先屏蔽 CNT、MOF、COF、Pc、KB、Ac、CVD 等缩写及描述词，避免把载体/有机基团误认成 W、K、Ac、Mo 等。另保留 `metals_from_elements`、`metals_from_formula`。两者有冲突时暂保留候选并集且 `metal_uncertain=1`，不是已确认的活性金属组成。模板残留 Zn、元素列疑似复制错行等没有擅自删去。
3. 按化学分类，B、Si、Ge、As、Sb、Te 单列 `metalloids`，不计 `n_metals`；Sb/Ge 等体系不据此直接宣称无金属 N–C。显式 0%-Fe 和 0 Fe 标签不按有 Fe 主样计，原 Elements 保留并留冲突标记。缩写大小写别名仅作有依据的候选识别，未修改 Formula。
4. `medium` 仅用于分组，不用于筛行。pH 缺失时只对浓度明确的强碱/强酸估算；25 °C 理想溶液，pKw=14；硫酸第一步完全、第二步 Ka2=0.012。浓酸活度及实际温度未校正。PBS 不凭名称猜精确 pH；缺浓度单位的电解液不擅补 M。氧气饱和等信息保留于原列，没有在标准化后丢失原信息。
5. `E12_value` 数值化后保留异常并加 flag，不把 Ag/AgCl/SCE 未知校准值转换为 RHE。非数值或可疑参比不填伪造的 RHE 值。
6. 盘/环电流密度、TOF、质量/比活性标准化为幅值，原始正负号仍在原列。单位分别按列头 mA cm⁻²、s⁻¹、A mg⁻¹、mA cm⁻²；显式不兼容单位、范围、比较号和多值不强行压成单值。环电流原列实际是电流密度，不能凭空换成绝对电流。
7. 特别注意起始电位列原格式是 **E@j**，不是 j@E：`onset_*_value` 为电位，`onset_*_criterion_current_density` 为判据电流密度；不能把 @ 后的 0.5 mA cm⁻²误标成测试电位。其他性能列的 `*_at_potential` 才是电位。
8. `10000S` 换为 2.7777778 h，`43200s` 即使存于 cycles 列也解析为 12 h；明确 cycles 不当时长。时长列无单位且 ≥1000 的数字不盲猜小时、秒或循环。保留率与衰减率分别标注，未直接把保留率当衰减量。电位范围、恒电流 @ 条件不强行转成单个 RHE 电位。
9. 结构分类优先样品特定证据。subType 的 single-atom 标签与实际 NP/合金描述冲突时，不据此自动判“颗粒＋单原子”。仅 @、encapsulated、MOF-derived、Fe–N–C 名称不能独立证明结构。少数题名与样品组成匹配的暂定分类在 structure_source 中注明 provisional；相同 DOI 的无金属、颗粒、单原子对照不互相套用。
10. Name / Institute 原值未处理，统计区分原大小写和别名，不能据此当作独立自然人数。
''',
f"## 金属与结构疑点复核\n\n{stats['uncertain_metal_rows']} 行带 metal_uncertain 标记，详见 metal_review_queue.csv；其中既有真正组成冲突，也有元素列缺失、缩写、模板残留或半金属分类问题。不能把候选金属并集统计直接作为已确认成分用于训练。",
f"对最初 unclear 且涉及 Fe/Co/Mn 的 DOI 查询及后续补查，缓存共 {len(cache)} 个 DOI，其中 {sum(bool(m.get('title')) for m in cache.values())} 个成功取得 Crossref 题名（部分有摘要）。两条中文 DOI 未返回可用元数据；见缓存错误。只读题名/摘要，没有用推断冒充全文确认。最终 unclear 为 {stats['structure'].get('unclear',0)} /1484，即 {stats['structure'].get('unclear',0)/1484:.1%}。",
'### 发现的具体问题\n\n- `CoNC-H2-360` 的 Elements 为 Fe,N,C，`MnNC-H2-360` 为 Cu,N,C；保留冲突，不擅自把候选并集当确定双金属。\n- `MWCNT-CoPc` 等多条 Elements 与 Cu/Pd/Pc 混杂，`y-Cu/NC` 的 Elements 却含 Fe；逐行标记。Pc 不是元素符号。\n- 题名核对发现 DOI `10.1016/j.xcrp.2023.101335` 对应生理电信号记录电极，`10.3390/catal12080913` 对应加氢脱硫/储能 CoMoS，均与本表 ORR 样品的对应关系可疑。数据不删，新增 doi_topic_flag，并保留核查题名和来源。\n- 环 TOF 列有大量 `%@电位`，不能按 s⁻¹使用，也没有擅自移入 H₂O₂ 法拉第效率列（产率/选择性/法拉第效率不可无依据混同）。\n- 有 Ag/AgCl 参比、异常大/小半波电位、不同耐久指标及相同催化剂多电解液/多稳定性行。都保留，不能将全表不分条件做性能排名。',
'## 分布（以下均为行数，不是独立催化剂数）'])
for field,title in [('structure','结构类别'),('medium','介质'),('electrolyte','电解液标准写法'),('n_metals','金属种数'),('metals','金属组合（含标记为不确定的候选组成）'),('year','年份'),('submitter_Name','提交者原始 Name'),('submitter_Institute','提交者原始 Institute')]:lines.extend(['### '+title,table(stats[field])])
lines.extend(['## 平台引用与使用条款','详见 [platform_sources.md](platform_sources.md)。已从 DigCat 官网实际展开 User Agreement 核实，平台指定引用为 Zhang 等，Chem Catalysis 6, 101775 (2026)，DOI 10.1016/j.checat.2026.101775。上传者给平台的许可不等于下载者的全库再分发授权；没有查到公开统一的 CC 数据许可。未公开发布数据，也未联系第三方。',
'## 验证结果','原始 Excel 哈希与上传记录一致；1484 行及原始 46 列逐值回读验证一致；895 组覆盖全部 row_id；未删行、未修改图和 Word。所有单文件低于仓库规定 50 MB。`validation.json` 为机器可读核验结果。'])
report='\n\n'.join(lines)+'\n'
report=re.sub(r'(?m)(\|[^\n]*\|)\n\n(?=\|)',r'\1\n',report)
(OUT/'REPORT.md').write_text(report,encoding='utf8',newline='\n')
expected=(DATA/'SHA256.txt').read_text(encoding='utf8').split()[0]
assert stats['raw_sha256']==expected
manifest=[]
for p in sorted([DATA/'ORR_clean_20261115.csv',DATA/'ORR_catalyst_level_20261115.csv']+list(OUT.glob('*'))+list((ROOT/'FeCoMn/scripts').glob('T013_*.py'))):
 if p.is_file() and p.name!='SHA256_outputs.txt':
  assert p.stat().st_size<50_000_000
  manifest.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix())
(OUT/'SHA256_outputs.txt').write_text('\n'.join(manifest)+'\n',encoding='utf8',newline='\n')
print('Report and output checksums written; raw hash verified; all files <50 MB')
