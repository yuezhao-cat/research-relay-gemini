from pathlib import Path
import json,csv,numpy as np
HERE=Path(__file__).resolve().parent
summary=json.loads((HERE/'comparison_24.json').read_text())
raw=[];checks=[];inputs={}
for h in ['imr','genkai']:
 raw+=json.loads((HERE/(h+'_composition_inventory.json')).read_text())
 checks+=json.loads((HERE/(h+'_selected_final_checks.json')).read_text())
 for z in json.loads((HERE/(h+'_input_checks.json')).read_text()):inputs[z['path']]=z
by_path={x['path']:x for x in raw}
names={'MnNC_bare':'Mn–NC，裸Mn–N4','MnNC_axOH':'Mn–NC，轴向OH计算对照','FCM_clean_bare':'FeCoMn–NC，干净颗粒、无轴向OH','FCM_clean_axOH':'FeCoMn–NC，干净颗粒、有轴向OH','FCM_8O_bare':'FeCoMn–NC，8O*、无轴向OH','FCM_8O_axOH':'FeCoMn–NC，8O*、有轴向OH'}
steps_labels=['OOH*生成','OOH*→O*','O*→OH*','OH*脱除']
def calc(e):
 b,a,o,h=e;H=-6.833;W=-14.327
 g=[a-b-2*W+1.5*H+.403,o-b-W+H+.066,h-b-W+.5*H+.343]
 s=[g[0]-4.92,g[1]-g[0],g[2]-g[1],-g[2]]
 return dict(G=g,steps=s,steps_at_078=[v+.78 for v in s],UL=-max(s),eta=1.23+max(s),limiting=s.index(max(s))+1)
old_energies={
 'MnNC_bare':[-1661.25027287,-1676.11661481,-1667.38075636,-1671.92040106],
 'MnNC_axOH':[-1671.92040106,-1686.69437219,-1677.57830354,-1681.84200553],
 'FCM_clean_bare':[-2066.63715092,-2081.57087047,-2072.76808195,-2077.42376589],
 'FCM_clean_axOH':[-2077.44984933,-2092.13380448,-2083.07161085,-2087.89577451],
 'FCM_8O_bare':[-2129.39408315,-2144.26459902,-2135.51628836,-2140.13246015],
 'FCM_8O_axOH':[-2140.14785718,-2154.81243475,-2145.47551691,-2150.55347134]}
results=[]
for family in names:
 ss=[x for x in summary if x['family']==family]
 result=calc([x['best']['energy_sigma0'] for x in ss]);result.update(family=family,name=names[family],old=calc(old_energies[family]))
 results.append(result)
(HERE/'best_existing_orr.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
with (HERE/'all_existing_manifest.csv').open('w',encoding='utf-8-sig',newline='') as f:
 keys=['machine','path','kind','composition','energy_sigma0','normal_end','ionic_converged','initial_Mn_moment','Mn_local_moment','particle_sum_moment','total_moment','cell','frozen_indices','POTCAR_token_sha256']
 w=csv.DictWriter(f,fieldnames=keys,lineterminator='\n');w.writeheader()
 for x in raw:
  row={k:x.get(k) for k in keys};row['POTCAR_token_sha256']=inputs[x['path']].get('POTCAR_token_sha256')
  for k in ['composition','cell','frozen_indices']:row[k]=json.dumps(row[k])
  w.writerow(row)
conv=[]
for x in checks:
 r=by_path[x['path']];f=np.array(x['final_forces']);ids=[i for i in range(len(f)) if i+1 not in r['frozen_indices']]
 conv.append(dict(path=x['path'],last_electronic_iterations=x['last_electronic_iterations'],NELM=int(r['settings'].get('NELM','60')),max_unfrozen_force=float(np.linalg.norm(f[ids],axis=1).max())))
(HERE/'selected_convergence_summary.json').write_text(json.dumps(conv,indent=2),encoding='utf-8')
lines=['# T031：24个目标状态的全部已有结果核查','',
'日期2026-11-18。**本次已完成24个目标状态的现存分支检索、归类、组成/设置/几何核对及统一CHE复算。不是24态均已达到双起始磁态验收，统一高精度静态部分也未执行。** 未新增或提交计算，未改图/Word。',
'', '## 核查范围与接受条件','',
f'两机工作目录按组成而非名字检索，得到{len(raw)}条相关OUTCAR记录（IMR102、九州76）。24个目标对应23个独立结构标签，因为Mn–NC无轴向OH的OH*终态，同时是轴向OH路径的背景。静态、振动、跨机副本、不同约束或吸附位置不当作新的同态磁分支。',
'', '接受条件：C174N4Mn，颗粒为Fe27Co32；O/H增量正确；相同晶胞、PAW原始token SHA256、k网格、ENCUT/PREC/EDIFF/EDIFFG/LREAL/ISPIN/ISMEAR/SIGMA/IVDW/ISYM/ISIF等；无额外U、指定净电荷、固定总自旋或不一致偶极修正；固定原子编号及固定坐标一致；优化正常结束且离子收敛；Mn两侧配体、OOH完整性、O–H、O–O、Mn–O及颗粒O数符合指定态。',
'', '当前选中的23份独立输出，最后SCF迭代2–63步，小于NELM150；未固定原子最大力均小于0.02eV/Å。几条低能候选相对参考的C/N骨架近邻连接未改变，固定坐标未改变。不是把改变组成、拆成O+OH或吸到颗粒上的结构并入原态。',
'', '## 24态逐项结果','',
'下表是**合格现有结果中的最低值**，不声称全局磁基态。初始Mn列的相同数值可能来自不同几何/跨机复算；只有不同起始值才算这里的第二初始条件。±磁矩不是所有模型的统一要求。',
'', '|模型|态|sigma→0/eV|初始Mn值/μB|已见不同起始值|最终体系磁矩/μB|来源编号|','|---|---|---:|---|---|---:|---|']
sources=[]
for i,x in enumerate(summary,1):
 b=x['best'];r=by_path[b['path']];sources.append(dict(id=i,**b))
 lines.append(f"|{names[x['family']]}|{x['state']}|{b['energy_sigma0']:.8f}|{','.join(str(v) for v in x['initial_Mn_values'])}|{'有' if x['has_two_Mn_initial_values'] else '尚缺'}|{r['total_moment']:.4f}|{i}|")
lines+=['','完整路径、初始/最终几何、接受与排除原因见sources_24.json、summary_24.csv、candidate_decisions.json。最终Mn局域与颗粒投影磁矩在多数原优化OUTCAR未输出，不能由初始MAGMOM或整个体系磁矩反推；对应字段留空。已有静态的局域磁矩只作分支辅助，未混作优化输出。',
'',f"24个目标里{sum(x['spin_start_coverage'] for x in summary)}个已覆盖所需的初始自旋条件，其余{sum(not x['spin_start_coverage'] for x in summary)}个尚缺这一层验证。另有含颗粒干净背景见Mn+3/+4，但都是平行起始，不算反平行核查；不能宣称24态全部确定最低磁态。",'','## 六组自由能与新旧对照','',
'同一套优化能量+SI CHE：G(H2)=−6.833、G(H2O)=−14.327eV，OOH/O/OH校正0.403/0.066/0.343eV；总反应4.92eV。采用各状态合格候选最低优化能，未掺入不同精度静态。',
'','|模型|ΔGOOH/eV|ΔGO/eV|ΔGOH/eV|UL/V|η/V|限制步|','|---|---:|---:|---:|---:|---:|---|']
for x in results:lines.append(f"|{x['name']}|{x['G'][0]:.6f}|{x['G'][1]:.6f}|{x['G'][2]:.6f}|{x['UL']:.6f}|{x['eta']:.6f}|{steps_labels[x['limiting']-1]}|")
lines+=['','|模型|旧ΔGOH→合并后/eV|旧UL→合并后/V|旧限制步→合并后|','|---|---|---|---|']
for x in results:lines.append(f"|{x['name']}|{x['old']['G'][2]:.6f}→{x['G'][2]:.6f}|{x['old']['UL']:.6f}→{x['UL']:.6f}|{steps_labels[x['old']['limiting']-1]}→{steps_labels[x['limiting']-1]}|")
lines+=['','四步ΔG及0.78V下四步值见best_existing_orr.json；η由1.23−UL得到，不能与单个ΔGOH数混淆。',
'','## 最重要的分支来源核对','',
'- MnNC_O_MnNbri虽名字写桥位，最终O位于Mn轴向（Mn–O1.57708Å），与原MnNC_O为同终态连接类型；C/N连接不变。它的−1667.74239034eV比旧O态低0.361634eV，改变裸Mn–N4路径的限制步。不能因名字排除，也不能仅按低能接纳。',
'- FCM_reconstruction_check的干净背景为−2066.67661959eV，比原背景低0.039469eV；组成、固定原子及坐标、骨架连接、粒子拓扑匹配。不是234C错误背景。用它统一配对后，干净颗粒无OH的ΔGOH变为0.506354eV。',
'- MnNC_OH_OH_magcheck低0.561047eV，OH两侧保留，ΔGOH从旧1.332降到0.771219eV。此前“只有OH会结合过弱”的证据不成立。',
'- 目录FCM_bg8O_MnO_OH_magcheck不能按名字归类。其**输入和最终坐标**均为+侧O247带H、−侧O248不带H，实际对应指定8O*+轴向OH背景的O*反应态；不是凭质子迁移把另一条路径硬替换。该低能优化−2145.75154261eV比现用优化低0.276026eV，且比既有电子结构静态分支还低。两侧Mn–O最终1.90776/1.60120Å。它已作为这个最终化学态的候选合并，源路径和实际构型同时报告。',
'- 8O无OH路径的O*在指定反应侧；另一个短键轴向O背景位于另一侧，不能混作同一条裸位点ORR路径的O*。轴向O/轴向OH配体稳定性比较单列于下一节。',
'','## 配体排序的独立警报','',
'先前已找到的8O轴向O低能背景为−2135.94582215eV，轴向OH低能背景为−2140.15243322eV；设置、固定原子、覆盖数相同。按覆盖库CHE，在0.78V下G(OH)−G(O)=+0.267389eV。这个对比偏向O，不能把旧−0.18eV偏向OH作为最低磁态排序。该结果不等于已经穷尽全覆盖库，但足以要求重新核查“颗粒使OH最稳定”的前提。',
'','## 颗粒直接影响与OH影响的数值拆分','',
'以下只用干净背景2×2、相同定义的吸附自由能。固定轴向配体，计算有颗粒−无颗粒；再比较两种配体条件。它反映颗粒存在及其引起的几何/自旋/电子重排的合效应，不等于已经证明纯电子转移机制。',
'','|中间体|无轴向OH时颗粒效应/eV|有轴向OH时颗粒效应/eV|两者之差（非加和项）/eV|','|---|---:|---:|---:|']
m={x['family']:x for x in results}
interaction=[]
for j,ads in enumerate(['OOH*','O*','OH*']):
 no=m['FCM_clean_bare']['G'][j]-m['MnNC_bare']['G'][j];yes=m['FCM_clean_axOH']['G'][j]-m['MnNC_axOH']['G'][j];interaction.append(dict(adsorbate=ads,particle_without_OH=no,particle_with_OH=yes,interaction=yes-no));lines.append(f'|{ads}|{no:+.6f}|{yes:+.6f}|{yes-no:+.6f}|')
lines+=['','有无颗粒在固定配体下仍会改变数值，而且对不同中间体方向、幅度不同。不能预设全部通过轴向OH，也不能预设颗粒的直接贡献对所有步骤都大。没有完成第二起始的状态仍存在分支不确定性，上表不应提前写成最终定量机制。',
'','## 尚未满足的T031要求','',
'1. 下列目标尚未见任务要求的两种初始自旋条件（含颗粒需覆盖平行/反平行，无颗粒需不同初始大小，而非仅全局翻号）的合格现有优化分支；本轮没有补算：']
for x in summary:
 if not x['spin_start_coverage']:lines.append('- '+names[x['family']]+' / '+x['state'])
lines+=['','2. 统一高精度静态、局域磁矩、同源PDOS/Bader/COHP尚未完成。旧静态0.05–0.06eV差异及主线O*磁态不一致不能靠拼接数据消除。应在补齐/确定优化分支后统一处理，不自动把任一静态能量替换进优化能量表。',
'3. 因此，本轮“24态全部已有分支核查”已交付，T031整体仍进行中，T029仍待数据，图/Word未改。报告没有宣称已证明全局最低磁态或既定机理。']
(HERE/'REPORT_existing_20261118.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(HERE/'sources_24.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2),encoding='utf-8')
(HERE/'particle_ligand_effects.json').write_text(json.dumps(interaction,indent=2),encoding='utf-8')
print('Report created; states',len(summary),'different initial Mn values',sum(x['spin_start_coverage'] for x in summary))
