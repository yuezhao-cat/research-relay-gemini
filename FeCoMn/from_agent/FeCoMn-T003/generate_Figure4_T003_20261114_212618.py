"""T003: reuse T002 D_red exactly for a; replace only lower row with 3 aligned maps.
Intermediate exports from the inherited processing are confined to TemporaryDirectory.
No npz or dense CSV is copied into this delivery. Data hashes are in CHECKS.json.
"""
from pathlib import Path
import tempfile,json,hashlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap,Normalize
from matplotlib.ticker import MultipleLocator
from scipy.signal import savgol_filter
OUT=Path(__file__).resolve().parent;REPO=OUT.parents[2]
T002=REPO/'FeCoMn/from_agent/FeCoMn-T002/generate_Figure4_T002_20261114_210528.py'
source=T002.read_text(encoding='utf-8').split('checks=[]')[0]
# Redirect T002 and the inherited T001 processing's intermediate file writes to scratch.
with tempfile.TemporaryDirectory(prefix='FeCoMn_T003_') as tmp:
 target=repr(str(REPO));scratch=repr(tmp)
 source=source.replace("OUT=Path(__file__).resolve().parent",'OUT=Path('+scratch+')').replace('REPO=OUT.parents[2]','REPO=Path('+target+')')
 source=source.replace("source=BASE.read_text(encoding='utf-8')", "source=PATCHED_T001_SOURCE")
 base1=REPO/'FeCoMn/from_agent/FeCoMn-T001/generate_Figure4_20261114_204757.py'
 patched=base1.read_text(encoding='utf-8').replace('OUT=Path(__file__).resolve().parent','OUT=Path('+scratch+')').replace('REPO=OUT.parents[2]','REPO=Path('+target+')')
 outer={'__file__':__file__,'__name__':'__main__','PATCHED_T001_SOURCE':patched}
 exec(compile(source,str(T002),'exec'),outer)
 outer['after'].close();outer['before'].close()
ns=outer['ns'];fig=outer['fig'];axes=outer['a_axes'];gradient=outer['gradient'];curves=outer['curves']
X=ns['X'];E=ns['E'];DS=ns['DS'];COL=ns['COL'];H=ns['H'];W=ns['W']
# Finish T002's D_red recolouring exactly, without changing any upper-row geometry.
cmap=LinearSegmentedColormap.from_list('a_D_red',['#b8394d','#f6bcc4'])
for lines in curves:
 for i,line in enumerate(lines):line.set_color(cmap(i/12))
gradient.images[0].set_cmap(cmap);gradient.patches[0].set_facecolor('#b8394d');gradient.patches[0].set_edgecolor('#b8394d')
for ax in list(fig.axes[4:]):fig.delaxes(ax)
axmm=ns['axmm'];frame=ns['frame'];letter=ns['letter'];cd=ns['cd']
eg=ns['eg'];heatchecks=[]
for name,lo,hi,left,width,limit,center,major,minor in [
 ('b',2900,3700,13,68,16,3307,200,100),
 ('c',1560,1720,86,30,4,None,80,40),
 ('d',1120,1320,121,40,10,1215,100,50)]:
 ax=axmm(left,83,width,54);m=(X>=lo)&(X<=hi);xx=X[m];z=DS[:,m]*1000
 zi=np.array([np.interp(eg,E,z[:,j]) for j in range(z.shape[1])]).T
 assert np.allclose(zi[np.searchsorted(eg,E)],z)
 pc=ax.imshow(zi,origin='lower',aspect='auto',extent=[xx[0],xx[-1],E[0],E[-1]],cmap=cd,norm=Normalize(-limit,limit),interpolation='nearest',rasterized=True)
 frame(ax,lo,hi,major,minor);ax.set_ylim(E[0],E[-1]);ax.set_yticks([0,.3,.6,.9,1.2]);ax.yaxis.set_minor_locator(MultipleLocator(.15));ax.tick_params(axis='y',labelsize=8)
 ax.set_xlabel(r'Wavenumber (cm$^{-1}$)')
 if name=='b':ax.set_ylabel(r'$E$ (V vs. RHE)')
 else:ax.tick_params(axis='y',labelleft=False)
 letter(ax,name)
 ax.text(.03,.96,'ref. 1.21 V',transform=ax.transAxes,ha='left',va='top',fontsize=8,color='#000000')
 if center is not None:ax.axvline(center,color=COL,lw=.65,ls=(0,(2,2)),alpha=.75)
 if name in ['b','d']:
  arrow_x=3060 if name=='b' else 1140;text_x=3010 if name=='b' else 1158;text='O–H band weakens' if name=='b' else 'Decreasing potential'
  ax.annotate('',xy=(arrow_x,.02),xytext=(arrow_x,1.08),arrowprops=dict(arrowstyle='-|>',color=COL,lw=.9,mutation_scale=8))
  ax.text(text_x,.55,text,rotation=90,va='center',ha='right',fontsize=8,color='#000000')
 # Three independent colour bars stacked at the far right, no plot area sacrificed.
 idx={'b':0,'c':1,'d':2}[name];bar_top=83+idx*19.3
 ca=axmm(165,bar_top,1.8,15.4);cb=fig.colorbar(pc,cax=ca,ticks=[-limit,0,limit]);cb.ax.tick_params(labelsize=8,length=2,pad=2);cb.outline.set_linewidth(.8)
 title={'b':'O–H','c':'H–O–H','d':'1215'}[name]
 fig.text(175/W,1-(bar_top+7.7)/H,title,rotation=90,ha='center',va='center',fontsize=8,color='#000000')
 heatchecks.append({'panel':name,'window_cm1':[hi,lo],'frame_mm':[left,83,width,54],'color_limits_1e3':[-limit,limit],'display_extrema_1e3':[float(z.min()),float(z.max())],'display_saturation_fraction':float(np.mean(abs(z)>limit))})
fig.text(168.5/W,1-75/H,'ΔAbs.',ha='center',va='center',fontsize=8,color='#000000')
fig.text(168.5/W,1-79/H,r'($10^{-3}$)',ha='center',va='center',fontsize=8,color='#000000')
STEM='Figure_4_20261114_212618'
# H-O-H checks on signed reference differences. Ref itself is identically zero.
m=(X>=1560)&(X<=1720);meanmask=(X>=1613)&(X<=1653);audit=[]
for i,e in enumerate(E):
 y=ns['D'][i]*1000
 row={'E_RHE_V':float(e),'label':f'{e:.2f}','mean_signed_delta_1613_1653_1e3':float(y[meanmask].mean())}
 for win in [21,41]:
  sm=savgol_filter(y,win,2);k=np.argmax(abs(sm[m]));row[f'max_abs_change_SG{win}_cm1']=None if i==12 else float(X[m][k]);row[f'signed_value_at_max_SG{win}_1e3']=float(sm[m][k])
 audit.append(row)
checks={'base_T002_script_relative':str(T002.relative_to(REPO)),'base_T002_script_sha256':hashlib.sha256(T002.read_bytes()).hexdigest(),'input_paths':ns['report']['reference_data_paths'],'input_sha256':ns['meta'],'data_arrays_SHA256':{k:hashlib.sha256(np.ascontiguousarray(ns['ref'][k]).tobytes()).hexdigest() for k in ['RAW','REL','RAWs','RELs']},'data_equal_T001_T002':outer['array_checks'],'lower_maps':heatchecks,'H_O_H_audit':audit,'font':'Arial','font_pt':8,'letters':'bold 10pt','upper_a_D_red_unchanged':True}
(OUT/'CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
plt.rcParams['svg.fonttype']='none';fig.savefig(OUT/(STEM+'_editable.svg'),dpi=600)
fig.savefig(OUT/(STEM+'.png'),dpi=600);fig.savefig(OUT/(STEM+'_preview.png'),dpi=180)
plt.rcParams['svg.fonttype']='path';fig.savefig(OUT/(STEM+'_Arial_paths.svg'),dpi=600)
print('Saved',OUT);print('maps',heatchecks);print('audit',audit)
