"""T033 draft a–e, retained original data; f intentionally undrawn."""
from pathlib import Path
import csv,json,hashlib,sys,re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE=Path(__file__).resolve().parent
OUT=HERE/'draft_20261118_v1';OUT.mkdir(exist_ok=True)
D=OUT/'data';D.mkdir(exist_ok=True)
ROOT=Path('D:/OneDrive/Desktop/知识库/papers/FeCoMn/ACS_Catalysis_第三轮投稿')
CALC=ROOT/'单图汇总_journal_20261025/10_计算_第三轮'
sys.path.insert(0,'C:/Users/46775/.codex/skills/nature-figure/scripts')
from audit_panel_alignment import require_matplotlib_panel_alignment

# Contract: compare the two Mn working environments; no universal causal claim.
# Fixed original sources, no new DFT or charge analysis. House style inherited.
plt.rcParams.update({'font.family':'Arial','font.size':8,'axes.labelsize':8,
 'xtick.labelsize':8,'ytick.labelsize':8,'legend.fontsize':8,
 'mathtext.fontset':'custom','mathtext.rm':'Arial','mathtext.it':'Arial:italic',
 'mathtext.bf':'Arial:bold','axes.linewidth':.8,'lines.linewidth':1,
 'xtick.major.size':3,'ytick.major.size':3,'xtick.major.width':.8,'ytick.major.width':.8,
 'xtick.direction':'out','ytick.direction':'out','xtick.major.pad':2,'ytick.major.pad':2,
 'axes.labelpad':2.5,'pdf.fonttype':42,'svg.fonttype':'none','axes.unicode_minus':True})
FILL={'FCM':'#eb687b','MnNC':'#f6b3a0','FCN':'#b6b3d6'}
LINE={'FCM':'#b8475a','MnNC':'#d9846c','FCN':'#7f7bab'}
NAMES={'FCM':'FeCoMn–NC','MnNC':'Mn–NC','FCN':'FeCo–NC'}
manifest=[]
def record(p,role):
 p=Path(p);manifest.append(dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),role=role))
def savecsv(name,header,rows):
 with (D/name).open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.writer(f);w.writerow(header);w.writerows(rows)
def raw_total(p,metal,oxygen):
 record(p,'raw axial COHP')
 with p.open() as f:
  next(f);head=next(f).split();nb=int(head[0]);ns=int(head[1]);labs=[next(f).strip() for _ in range(nb)];a=np.loadtxt(f)
 match=[i for i,l in enumerate(labs) if f'{metal}->{oxygen}(' in l and '[' not in l]
 assert len(match)==1
 j=match[0];cols=[1+s*2*nb+2*j for s in range(ns)]
 return a[:,0],-a[:,cols].sum(axis=1)
axial={}
p=ROOT/'电子结构后处理核查_20261031/fig6_data/COHPCAR_base.lobster'
axial['FCM']=raw_total(p,'Mn238','O247')
p=HERE/'MnNC_source_trace_20261118/MnNC_axial_COHP_raw_verified_20261118.csv';record(p,'verified MnNC axial total, original COHP static')
df=pd.read_csv(p);axial['MnNC']=(df.E_minus_EF_eV.to_numpy(),df.minus_pCOHP_spin_sum.to_numpy())
reaction={}
for sample in ['FCM','MnNC']:
 for state in ['OOH','OH']:
  p=CALC/f'calc_COHP_{sample}_{state}_journal_20261025.csv';record(p,'retained reaction-side COHP')
  a=np.loadtxt(p,delimiter=',',skiprows=2,encoding='utf-8-sig')
  assert a.shape[1]==2 and np.all(np.diff(a[:,0])>0)
  reaction[sample,state]=(a[:,0],a[:,1])
ICO={('FCM','OOH'):3.11766,('MnNC','OOH'):2.65218,('FCM','OH'):3.05704,('MnNC','OH'):2.71550}
savecsv('a_bond_summary.csv',['sample','bond','distance_A','minus_ICOHP_eV'],[['FCM','Mn238-O247',1.877242172374744,2.64030],['MnNC','Mn179-O180',1.5770846336315383,8.03278]])
savecsv('c_bond_summary.csv',['sample','state','reaction_bond','minus_ICOHP_eV'],[[s,t,'Mn238-O248' if s=='FCM' else 'Mn179-O181',v] for (s,t),v in ICO.items()])
record(HERE.parents[1]/'review/Fig6_Codex_data/combined.json','verified raw bond summary and source paths')
for sample,(x,y) in axial.items():savecsv(f'a_{sample}_axial.csv',['E_minus_EF_eV','minus_pCOHP'],zip(x,y))
for (sample,state),(x,y) in reaction.items():savecsv(f'c_{sample}_{state}.csv',['E_minus_EF_eV','minus_pCOHP'],zip(x,y))

p=ROOT/'单图汇总_journal_20261025/92_电子结构统一原参考态_20261029/atom_resolved_occupied_d_centers.csv';record(p,'original background occupied d centers')
eps=pd.read_csv(p);background=[]
for sample,index,q,m in [('FCM',238,11.457649,3.206),('MnNC',179,11.507781,.287)]:
 e=float(eps[(eps['sample']==sample)&(eps.state=='base')&(eps.atom_1based==index)].occupied_d_center_eV.iloc[0]);background.append([sample,index,q,e,m])
savecsv('b_background.csv',['sample','Mn_index','Bader_electrons','occupied_d_center_eV','local_moment_muB'],background)
p=CALC/'calc_Bader_contact_metal_change_journal_20261025.csv';record(p,'original Mn Bader change')
metal=pd.read_csv(p)
p=ROOT/'电子结构系统核对_20261029/三样品九吸附态_统一口径对照.csv';record(p,'original adsorbate electron excess')
charge=pd.read_csv(p);bad=[]
for state in ['OOH','OH']:
 for sample in ['FCM','MnNC']:
  loss=-float(metal[(metal.system==sample)&(metal.adsorbate==state)].delta_electrons.sum())
  gain=float(charge[(charge['sample']==sample)&(charge.state==state)].adsorbate_electron_excess_vs_neutral.iloc[0]);bad.append([sample,state,loss,gain])
savecsv('d_Bader.csv',['sample','state','Mn_electron_loss','adsorbate_electron_excess'],bad)
vals={}
for name in ['calc_ORR_adsorption_free_energies','calc_ORR_limiting_potential']:
 p=CALC/(name+'_journal_20261025.csv');record(p,'original volcano descriptors')
 a=list(csv.reader(p.open(encoding='utf-8-sig')))[2:]
 for row in a:
  if not row:continue
  sample={'FeCoMn-NC':'FCM','FeCo-NC':'FCN','Mn-NC':'MnNC'}[row[2]]
  vals.setdefault(sample,{})['UL' if 'limiting' in name else 'GOH']=float(row[1] if 'limiting' in name else row[7])
  if 'adsorption' in name:vals[sample]['GOOH']=float(row[1])
savecsv('e_volcano.csv',['sample','GOH_eV','GOOH_eV','UL_V'],[[s,v['GOH'],v['GOOH'],v['UL']] for s,v in vals.items()])
(OUT/'source_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')

W,H=177.8,187.;MM=1/25.4
fig=plt.figure(figsize=(W*MM,H*MM))
left,right,gap=14.,4.,15.
cw=(W-left-right-2*gap)/3;span=2*cw+gap;rx=left+2*(cw+gap)
row=[17.,76.,135.];rh=40.
axes={}
def ax(name,x,y,w,h):
 a=fig.add_axes([x/W,1-(y+h)/H,w/W,h/H],label=name);a._mm=(x,y,w,h);axes[name]=a
 a.tick_params(top=False,right=False);return a
def spectra(a,curves):
 all_y=[]
 for s,(x,y) in curves.items():
  mask=(x>=-8)&(x<=2);a.plot(x[mask],y[mask],color=LINE[s],lw=1)
  all_y.extend(y[mask])
 a.axvline(0,ymin=0,ymax=.64,color='.6',lw=.65,ls=(0,(2,2)),zorder=0);a.axhline(0,color='.7',lw=.55,zorder=0)
 a.set_xlim(-8,2);a.set_xticks([-8,-4,0,2]);a.set_xlabel(r'$E$ − $E$$_{\mathrm{F}}$ (eV)')
 return np.min(all_y),np.max(all_y)
a=ax('a',left,row[0],span,rh);lo,hi=spectra(a,axial);a.set_ylim(min(-2,lo*1.15),hi*1.45)
a.set_ylabel('−pCOHP');a.text(.03,.95,'Axial Mn–O',transform=a.transAxes,va='top')
for sample,yy,text in [('FCM',.88,'Mn–OH: 1.88 Å; −ICOHP = 2.64 eV'),('MnNC',.78,'Mn=O: 1.58 Å; −ICOHP = 8.03 eV')]:
 a.text(.97,yy,text,color=LINE[sample],transform=a.transAxes,ha='right',va='top')
# b: independent units and untruncated baselines; colours carry sample identity.
baxes=[]
for i,(key,col,ylab,lim,ticks) in enumerate([('N',2,'$N$ (e)',(0,14),[0,6,12]),('eps',3,r'$ε$$_{\mathrm{d}}$ (eV)',(-4.4,0),[-4,-2,0]),('m',4,'$m$ (μB)',(0,4.4),[0,2,4])]):
 z=ax('b_'+key,rx,row[0]+i*15,cw,10);baxes.append(z)
 for j,r in enumerate(background):
  v=r[col];s=r[0];z.bar(j,v,width=.6,color=FILL[s],edgecolor=LINE[s],lw=.6)
  if key=='N':z.text(j,v-1.2,f'{v:.2f}',ha='center',va='top')
  elif key=='eps':z.text(j,v/2,f'{v:.2f}'.replace('-','−'),ha='center',va='center')
  elif v>1:z.text(j,v-.45,f'{v:.2f}',ha='center',va='top')
  else:z.annotate(f'{v:.2f}',(j,v),xytext=(0,2),textcoords='offset points',ha='center',va='bottom')
 z.set_ylim(*lim);z.set_yticks(ticks);z.set_xlim(-.7,1.7);z.set_xticks([]);z.set_ylabel(ylab)

# c: two comparable raw-amplitude spectra; neither curve is independently normalized.
inner_gap=13.;sw=(span-inner_gap)/2;caxes=[]
for i,state in enumerate(['OOH','OH']):
 z=ax('c_'+state,left+i*(sw+inner_gap),row[1],sw,rh);caxes.append(z)
 lo,hi=spectra(z,{s:reaction[s,state] for s in ['FCM','MnNC']});z.set_ylim(min(-1,lo*1.15),hi*1.45)
 z.text(.04,.95,state+'*',transform=z.transAxes,va='top')
 for s,yy in [('FCM',.94),('MnNC',.84)]:z.text(.96,yy,f'−ICOHP = {ICO[s,state]:.2f} eV',transform=z.transAxes,ha='right',va='top',color=LINE[s])
 if i==0:z.set_ylabel('−pCOHP')
# Same y scale across OOH/OH, including unoccupied antibonding structure.
ylo=min(z.get_ylim()[0] for z in caxes);yhi=max(z.get_ylim()[1] for z in caxes)
for z in caxes:z.set_ylim(ylo,yhi)

daxes=[]
for i,(col,lab,top) in enumerate([(2,'Mn loss (e)',.16),(3,'Ads. gain (e)',.7)]):
 z=ax('d_'+str(i),rx,row[1]+i*23,cw,17);daxes.append(z)
 for j,s in enumerate(['FCM','MnNC']):
  vv=[next(r[col] for r in bad if r[0]==s and r[1]==state) for state in ['OOH','OH']]
  z.bar(np.arange(2)+(j-.5)*.3,vv,.27,color=FILL[s],edgecolor=LINE[s],lw=.6)
 z.set_xticks([0,1]);z.set_xticklabels(['OOH*','OH*'] if i else []);z.set_ylim(0,top);z.set_xlim(-.6,1.6);z.set_ylabel(lab)
 if i==0:z.set_yticks([0,.05,.10,.15])
 else:z.set_yticks([0,.3,.6])

e=ax('e',left,row[2],cw,rh)
scale=float(np.mean([v['GOOH']-v['GOH'] for v in vals.values()]));apex=(4.92-scale)/2
e.plot([0,apex,4.92-scale],[0,apex,0],color='.6',lw=.9,ls=(0,(3,2)))
for s,v in vals.items():e.plot(v['GOH'],v['UL'],'o',ms=5.2,mfc=FILL[s],mec=LINE[s],mew=.8,zorder=4)
for s,x,y,ha,va in [('FCM',1.75,.88,'right','center'),('FCN',.48,.13,'left','center'),('MnNC',1.75,.39,'right','center')]:
 e.text(x,y,NAMES[s],ha=ha,va=va,color=LINE[s])
e.set_xlim(0,1.8);e.set_ylim(0,1.02);e.set_xticks([0,.5,1,1.5]);e.set_yticks([0,.5,1]);e.set_xlabel(r'Δ$G$$_{\mathrm{OH*}}$ (eV)');e.set_ylabel(r'$U$$_{\mathrm{L}}$ (V vs. RHE)')

fig.legend(handles=[Line2D([],[],color=LINE[s],lw=1.5,label=NAMES[s]) for s in ['FCM','MnNC']],loc='upper left',bbox_to_anchor=(left/W,1-2/H),ncol=2,frameon=False,borderaxespad=0,columnspacing=2,handlelength=1.8)
fig.canvas.draw();renderer=fig.canvas.get_renderer()
# Align left ink edge of y-axis titles per physical column, and panel letters to that edge.
def align_labels(group):
 target=min(z.yaxis.label.get_window_extent(renderer).x0 for z in group if z.yaxis.label.get_text())
 for z in group:
  if not z.yaxis.label.get_text():continue
  bb=z.yaxis.label.get_window_extent(renderer);delta=(target-bb.x0)/z.get_window_extent(renderer).width
  pos=z.yaxis.label.get_position();z.yaxis.set_label_coords(z.transAxes.inverted().transform(z.yaxis.label.get_transform().transform(pos))[0]+delta,.5)
 fig.canvas.draw();return target/fig.dpi*25.4
lx=align_labels([a,caxes[0],e]);bx=align_labels(baxes+daxes)
letters=[]
for lab,z,xx in [('a',a,lx),('b',baxes[0],bx),('c',caxes[0],lx),('d',daxes[0],bx),('e',e,lx)]:
 y=z._mm[1]-2.5;t=fig.text(xx/W,1-y/H,lab,ha='left',va='bottom',fontsize=10,fontweight='bold');letters.append(t)
fig.canvas.draw()
# Explicit nested comparison groups. Parent span edges checked below.
groups=[dict(id='c-curves',panels=['c_OOH','c_OH'])]
cols=[dict(id='b-miniplots',panels=[z.get_label() for z in baxes]),dict(id='d-miniplots',panels=[z.get_label() for z in daxes])]
require_matplotlib_panel_alignment(fig,json_out=OUT/'alignment.json',axes=list(axes.values()),panel_ids={z:k for k,z in axes.items()},row_groups=groups,column_groups=cols,strict=True)
assert abs(a.get_position().x0-caxes[0].get_position().x0)<1e-10
assert abs(a.get_position().x1-caxes[1].get_position().x1)<1e-10
assert abs(baxes[0].get_position().x0-daxes[0].get_position().x0)<1e-10
frames={k:dict(left_mm=z._mm[0],top_mm=z._mm[1],width_mm=z._mm[2],height_mm=z._mm[3]) for k,z in axes.items()}
(OUT/'frames.json').write_text(json.dumps(dict(width_mm=W,height_mm=H,axes=frames,f_reserved=True),indent=2))
fig.savefig(OUT/'Figure6_draft.png',dpi=600,facecolor='white')
fig.savefig(OUT/'Figure6_preview.png',dpi=300,facecolor='white')
fig.savefig(OUT/'Figure6_draft.pdf',facecolor='white')
plt.rcParams['svg.fonttype']='none';fig.savefig(OUT/'Figure6_editable.svg',facecolor='white')
plt.rcParams['svg.fonttype']='path';fig.savefig(OUT/'Figure6_Arial_paths.svg',facecolor='white')
print('OUTPUT',OUT)
print('b background',background,'d charge',bad,'volcano apex',apex)
