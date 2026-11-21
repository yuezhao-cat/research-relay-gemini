"""Validate deliverables, write report and SHA256 manifest after generation."""
from pathlib import Path
import json,hashlib,xml.etree.ElementTree as ET
import numpy as np
from PIL import Image,ImageDraw,ImageFont

OUT=Path(__file__).resolve().parent;REPO=OUT.parents[2]
d=json.loads((OUT/'CHECKS.json').read_text(encoding='utf8'))
assert len(d['variants'])==3 and len(d['SI'])==2
variants=sorted(d['variants'],key=lambda q:q['name'])
assert all(q['file_stem'].startswith('Figure_4_20261116_1215') for q in variants)
all_stems=[q['file_stem'] for q in variants]+[q['file_stem'] for q in d['SI']]
for name,h in d['source_SHA256'].items():assert hashlib.sha256((REPO/d['source'] /name).read_bytes()).hexdigest()==h
checks=[]
for stem in all_stems:
 for suffix in ['.png','_preview.png','_editable.svg','_Arial_paths.svg']:
  p=OUT/(stem+suffix);assert p.exists() and 0<p.stat().st_size<50_000_000
 im=Image.open(OUT/(stem+'.png'));dpi=im.info.get('dpi');assert dpi and all(abs(v-600)<.1 for v in dpi)
 prev=Image.open(OUT/(stem+'_preview.png'));assert prev.width<=1600
 root=ET.parse(OUT/(stem+'_Arial_paths.svg')).getroot();assert not root.findall('.//{http://www.w3.org/2000/svg}text')
 edit=(OUT/(stem+'_editable.svg')).read_text(encoding='utf8')
 assert 'Arial' in edit and 'DejaVu' not in edit and 'Liberation' not in edit
 text=''.join(ET.parse(OUT/(stem+'_editable.svg')).getroot().itertext())
 assert 'a.u.' not in text and '1.21 V' not in text and '−0.09 V' not in text
 checks.append({'stem':stem,'PNG_pixels':[im.width,im.height],'PNG_dpi':dpi,'editable_SVG_Arial':True,'paths_SVG_text_nodes':0,'old_voltage_labels_absent':True})
ref_image=np.asarray(Image.open(OUT/(variants[0]['file_stem']+'_preview.png')))
for q in variants:
 assert max(abs(v) for v in q['alignment_error_mm'])<.02
 assert q['measured_E_node_count']==13 and q['measured_E_line_count']==0
 assert q['minimum_floor_to_surface_screen_gap_mm']>=5
 assert q['b_line_width_pt']==1.15
 assert len({tuple(z['common_ylim_milli']) for z in q['b']})==1
 assert len({z['common_absorbance_per_mm'] for z in q['b']})==1
 assert sum(z['scale_bar_absorbance'] is not None for z in q['b'])==1
 assert q['b'][2]['scale_bar_absorbance']==.005 and q['b'][2]['min_adjacent_gap']>=.35-1e-12
 im=np.asarray(Image.open(OUT/(q['file_stem']+'_preview.png')));y=round(110/190*im.shape[0])
 assert np.array_equal(ref_image[y:],im[y:]),'b changed across variants'
assert all(q['rounded_match'] for q in d['means'])
(OUT/'VALIDATION.json').write_text(json.dumps({'files':checks,'all_baseline_checks_match_rounded_Claude_values':True,'original_source_hashes_unchanged':True,'same_b_pixels_across_all_three_views':True,'b_common_data_multiplier_and_common_physical_scale':True,'only_one_b_scale_bar':True,'b_no_AU_unit_suffix':True},ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')

# Light comparison sheet: only panel a, 1600 pixels wide.
tile_w=530;tiles=[]
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',19)
for q in variants:
 im=Image.open(OUT/(q['file_stem']+'_preview.png')).convert('RGB');im=im.crop((0,0,im.width,round(im.height*108/190)))
 im=im.resize((tile_w,round(im.height*tile_w/im.width)),Image.Resampling.LANCZOS)
 tile=Image.new('RGB',(tile_w,im.height+30),'white');tile.paste(im,(0,30));draw=ImageDraw.Draw(tile)
 draw.text((10,5),f"{q['name']}: elev {q['elev']} / azim {q['azim']}",font=font,fill='black');tiles.append(tile)
sheet=Image.new('RGB',(1590,max(t.height for t in tiles)),'white')
for k,t in enumerate(tiles):sheet.paste(t,(k*530,0))
sheet.save(OUT/'Figure_4_T015_view_comparison_20261116_1215.png')

lines=['# FeCoMn-T015：Figure 4 两层差谱图与 SI 原始谱',
'日期：2026-11-16。已完成本任务及仓库两项补充，并合并本轮用户后续修改。所有版本供赵月选择，未视为定稿；Word未改。',
'## 当前版本与后续修改',
'''- 正文只保留 a（三维差谱＋底面映射，1000–3650 cm⁻¹）和 b（三段差谱堆叠），删除 c/d/e。
- 最新电位统一 E(RHE)=E(SCE)+1.016 V；参比为0.2.CSV=1.216 V，显示1.22 V；最低−0.084 V，显示−0.08 V。波谱相减仍用相同原始文件，换算不改变ΔAbs数值。
- 用户后续要求“小幅倾斜”：三个备选分别为azim −93/−95/−97，替代原任务严格水平的−90。前沿3650和1000的**水平投影**仍与b左/右外框对齐；前沿有轻微上下倾斜，见下表，不声称y坐标完全相等。
- 用户后续要求“三维图不要留线”：取消原任务13条细灰叠线，全部13个实测电位仍保留在曲面插值节点中。没有背景网格，也没有人工光照改变颜色含义。
- 用户认为原深紫太深：紫端由原任务#4b3f93改回本文#8f8bc0，经过浅紫、白、浅红到红端#c9243f；0为白，色标±8×10⁻³。超限仅饱和颜色并有三角标示，高度不截断。
- 用户要求b谱线加粗：1.15 pt，细虚线和边框不随之加粗。
- 用户要求简化a刻度：电位刻度仅0.0/1.2，移到左侧；吸收变化刻度−10/0/10在右侧。轴实际范围仍包含所有13个新电位。
- 用户要求说明1215谱带：三维标为“1215 cm⁻¹ (*OOH-related)”，属于**暂归属**，不能当作独立证明*OOH或具体金属位点的证据；此项替代原任务“不标OOH*”。ν(O–H)、δ(H–O–H)同时保留。
- b三段**同一数据倍率、同一ylim跨度、同一物理高度**，不再单独缩小O–H。只有1215段加大堆叠间距；全部三段共用最右段一根5×10⁻³比例尺。纵轴为ΔAbsorbance，无a.u.。
''',
'## 视角、端点对齐与层间间隔',
'a前沿横轴目标水平位置与b外框一致：左13.000 mm，右161.000 mm。以下偏差按最终画布坐标投影计算；600 dpi栅格仍有约0.042 mm/像素的离散精度。',
'| 版本 | elev / azim | box aspect | 左/右偏差（mm） | 前沿上下差（mm） | 最小曲面–底面投影间隔（mm） |\n|---|---|---|---|---:|---:|']
for q in variants:
 lines.append(f"| {q['name']} | {q['elev']}° / {q['azim']}° | {q['box_aspect']} | {q['alignment_error_mm'][0]:.6f} / {q['alignment_error_mm'][1]:.6f} | {q['front_axis_vertical_difference_mm']:.3f} | {q['minimum_floor_to_surface_screen_gap_mm']:.3f} |")
lines.extend(['三版均为轻透视（focal_length=1.6）、线性吸收高度轴。仅视角/box aspect不同，数据、基线、配色、b内容均相同；b预览逐像素相等。',
'## 四点基线与核对数值',
'''读入13个CSV，删除#NaN后按波数排序。每谱在1330–1370、1900–1950、2550–2650、3850–3950四个窗口分别取平均x/平均吸收，连接为折线基线，再减该谱基线。锚点范围之外采用np.interp端值保持，与Claude粗稿代码一致（不是多项式基线，也不是两点外推）。随后减0.2.CSV的同法处理谱，得到带符号差谱。

a显示SG41二阶，b按O–H/H–O–H/1215分别SG21/41/21。对全部波数先处理再取绘图窗口，没有为凑核对值另调参数。下表为**未显示平滑前的窗口均值**，单位10⁻³，−0.08 V相对1.22 V；SG41均值另列于CHECKS.json。3700–3800虽在a显示范围外，仍用完整原始谱核查。
''',
'| 窗口（cm⁻¹） | 本次数值 | Claude一位小数 | 是否一致 |\n|---|---:|---:|---|'])
for q in d['means']:
 lo,hi=q['window_cm-1'];lines.append(f"| {lo}–{hi} | {q['unsmoothed_mean_delta_milli']:.6f} | {q['Claude_rounded']:.1f} | 一位小数一致 |")
lines.extend(['## 新电位对照表','| 原始文件 | SCE（V） | RHE未四舍五入（V） | 图示（V） |\n|---|---:|---:|---:|'])
for name,e in zip(d['used_FILES'],d['E_RHE']):
 sce=-1.1 if name=='-11' else float(name);lines.append(f'| {name}.CSV | {sce:g} | {e:.3f} | {e:.2f} |')
lines.extend(['−1.CSV与0.1.CSV逐字节相同，按任务排除−1.CSV；−11.CSV按−1.1 V vs SCE解释。新换算后0.1.CSV自然对应1.116 V，不再需要旧+1.011口径下的单独例外。',
'## b比例尺与间距核验',
'三段高度均54 mm，ylim完全相同；下表的单位/mm是从实际共享坐标跨度计算的，不是仅把标签改成同一个数。只有1215段扩大堆叠间距，不改变倍率。比例尺底端位于所有谱线上方的独立留白区；虚线只画到谱线区，未穿过比例尺文字。',
'| 波段 | 数据除数 | 堆叠步长（10⁻³） | 吸收量/mm | 最小相邻曲线差（10⁻³） | 比例尺 |\n|---|---:|---:|---:|---:|---|'])
for q in variants[0]['b']:
 lines.append(f"| {q['window_cm-1']} | {q['scale_divisor']} | {q['stack_step_milli_div_sc']:.6f} | {q['common_absorbance_per_mm']:.9f} | {q['min_adjacent_gap']:.6f} | {'5×10⁻³' if q['scale_bar_absorbance'] else '共用右段'} |")
lines.extend(['## SI图的原始谱口径',
'''两张SI均用仪器在已采开路背景下导出的**原始吸收CSV**：删除NaN、相同显示平滑，不另外扣四点基线、不减1.22 V，完整保留原始谱形用于核查。正文a/b则是四点基线后的差谱，两者不能混称。三段SI与b同一物理缩放/单根比例尺；全谱SI为1000–4000 cm⁻¹、SG21、比例尺20×10⁻³。SI图号待后续排入Word时确定，本次不写入Word。
''',
'## 文件索引'])
for q in variants+d['SI']:
 stem=q['file_stem'];lines.append(f"- **{q.get('name',stem)}**：[预览]({stem}_preview.png) · [600 dpi PNG]({stem}.png) · [可编辑SVG]({stem}_editable.svg) · [Arial路径SVG]({stem}_Arial_paths.svg)")
lines.extend(['- [三视角并排比较](Figure_4_T015_view_comparison_20261116_1215.png)',
'- `generate_T015.py`为出图脚本；`CHECKS.json`包含数据/源文件哈希、基线核查、对齐及显示参数；`VALIDATION.json`含文件核验；`DELIVERY_SHA256.json`含本交付所有文件哈希。',
'## 数据与导出验证',
'原始13个源文件SHA256前后不变；不提交重复原始数据或NPZ。正文3版数据数组相同；全部实测节点的电位插值误差为0；未逐谱归一化、未分段改幅度、未人为扣掉细峰。正式PNG均为600 dpi，预览PNG为180 dpi，比较拼图仅供屏幕审阅；可编辑SVG保留Arial文字，路径SVG的text节点为0，无DejaVu/Liberation回退；单文件均低于50 MB。',
'任务原文及补充已核对；用户后续修改优先于任务原文旧要求。报告完成不等于用户已选定图版。'])
report='\n\n'.join(lines)+'\n'
import re
report=re.sub(r'(?m)(\|[^\n]*\|)\n\n(?=\|)',r'\1\n',report)
(OUT/'REPORT.md').write_text(report,encoding='utf8',newline='\n')
manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='DELIVERY_SHA256.json'}
(OUT/'DELIVERY_SHA256.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print('All 5 figures / 15 publication files validated; report and comparison written.')
