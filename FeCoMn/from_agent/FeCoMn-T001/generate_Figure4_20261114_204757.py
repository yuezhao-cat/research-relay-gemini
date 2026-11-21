from pathlib import Path
import sys,json,hashlib
import numpy as np,pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap,Normalize
from matplotlib.ticker import MultipleLocator
from scipy.signal import savgol_filter
from matplotlib.patches import Rectangle,Polygon
OUT=Path(__file__).resolve().parent
REPO=OUT.parents[2]
RAW=REPO/'FeCoMn/data/SEIRAS_20241021_1-2'
REFERENCE=REPO/'FeCoMn/scripts/Figure_4_SEIRAS_20261114_script.py'
# Execute the unmodified reference's data section only; no reference plot layout.
sys.argv=[str(REFERENCE),str(RAW),'unused']
ref={};exec(compile(REFERENCE.read_text(encoding='utf-8').split('fig = plt.figure')[0],str(REFERENCE),'exec'),ref)
X=ref['x'];E=ref['E'][::-1];A=ref['RAW'][::-1]/1000;D=ref['REL'][::-1]/1000
S=ref['RAWs'][::-1]/1000;DS=ref['RELs'][::-1]/1000
# Independent repeated load/baseline using precisely the reference operations.
ind=[];meta=[]
for n in ref['files']:
 f=RAW/(n+'.CSV');a=np.genfromtxt(f,delimiter=',');a=a[~np.isnan(a[:,1])];a=a[np.argsort(a[:,0])];x=a[:,0];y=a[:,1]
 w1=(x>=1330)&(x<=1370);w2=(x>=1900)&(x<=1950);x1,y1,x2,y2=x[w1].mean(),y[w1].mean(),x[w2].mean(),y[w2].mean()
 ind.append((y-(y1+(y2-y1)*(x-x1)/(x2-x1)))*1000)
 meta.append(dict(file=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
assert np.array_equal(np.array(ind),ref['RAW'])
reference_differences={'baseline_RAW':float(abs(np.array(ind)-ref['RAW']).max()),'display_RAWs':float(abs(np.array([savgol_filter(y,21,2) for y in ind])-ref['RAWs']).max()),'display_RELs':float(abs(np.array([savgol_filter(y,21,2) for y in (np.array(ind)-ind[0])])-ref['RELs']).max())}
assert all(v==0 for v in reference_differences.values())
old_diff=0.0
# O-H peak checks: two SG windows; fit original unsmoothed local peak top with a quadratic.
peakrows=[]
for i,e in enumerate(E):
 y=A[i]*1000;m=(X>=2900)&(X<=3700);p21=X[m][np.argmax(savgol_filter(y,21,2)[m])];p81=X[m][np.argmax(savgol_filter(y,81,2)[m])]
 w=abs(X-p81)<=60;coef,cov=np.polyfit(X[w]-p81,y[w],2,cov=True);qa,qb,qc=coef;vertex=p81-qb/(2*qa);assert qa<0 and abs(vertex-p81)<60
 yp=np.polyval(coef,X[w]-p81);rmse=float(np.sqrt(np.mean((yp-y[w])**2)))
 peakrows.append(dict(E_RHE_V=float(e),SG21_cm1=float(p21),SG81_cm1=float(p81),quadratic_peak_cm1=float(vertex),quadratic_window_low_cm1=float(p81-60),quadratic_window_high_cm1=float(p81+60),fit_RMSE_absorbance_1e3=rmse))
COL='#404040';PAL=['#8f8bc0','#b6b3d6','#d6d1d1','#f1a0a6','#eb687b']
ce=LinearSegmentedColormap.from_list('paper_potential',PAL)
cd=LinearSegmentedColormap.from_list('paper_difference',['#8f8bc0','#d0cce5','#ffffff','#f6bcc4','#eb687b'],N=257)
plt.rcParams.update({'font.family':'Arial','font.size':8,'axes.labelsize':8,'xtick.labelsize':8,'ytick.labelsize':8,'legend.fontsize':8,'text.color':'#000000','axes.labelcolor':'#000000','axes.edgecolor':COL,'xtick.color':'#000000','ytick.color':'#000000','font.weight':'normal','axes.labelweight':'normal','axes.titleweight':'normal','axes.linewidth':.8,'xtick.direction':'out','ytick.direction':'out','xtick.major.size':3,'ytick.major.size':3,'xtick.minor.size':1.8,'ytick.minor.size':1.8,'xtick.major.width':.8,'ytick.major.width':.8,'axes.labelpad':3,'mathtext.fontset':'custom','mathtext.rm':'Arial','mathtext.it':'Arial:italic','mathtext.bf':'Arial:bold','mathtext.sf':'Arial','svg.fonttype':'none','pdf.fonttype':42,'axes.unicode_minus':True})
W,H=177.8,149.;fig=plt.figure(figsize=(W/25.4,H/25.4),facecolor='white')
def axmm(left,top,width,height):return fig.add_axes([left/W,1-(top+height)/H,width/W,height/H])
def frame(ax,lo,hi,major,minor):
    ax.set_xlim(hi,lo);ax.xaxis.set_major_locator(MultipleLocator(major));ax.xaxis.set_minor_locator(MultipleLocator(minor));ax.tick_params(pad=2)
    for sp in ax.spines.values():sp.set_linewidth(.8)
def letter(ax,t):ax.text(-.13,1.06,t,transform=ax.transAxes,fontsize=10,fontweight='bold',va='bottom')
axes=[];geo=[(13,68),(86,30),(121,40)]
regions=[(2900,3700,3307,(3257,3357),r'$\nu$(O–H)',200,100,.02),(1560,1720,1633,(1613,1653),r'$\delta$(H–O–H)',80,40,.005),(1120,1320,None,(1191,1239),r'1215 cm$^{-1}$ region',100,50,.005)]
scalebars=[]
for k,((left,width),(lo,hi,center,band,title,major,minor,sbar)) in enumerate(zip(geo,regions)):
    ax=axmm(left,10,width,54);axes.append(ax);m=(X>=lo)&(X<=hi);xx=X[m];z=S[:,m]
    span=float(np.max(np.ptp(z,axis=1)));offset=0.0
    for i,e in enumerate(E):ax.plot(xx,z[i]+i*offset,color=ce(i/12),lw=.85)
    ymin=float(z.min())-.10*span;ymax=float(z.max())+.30*span;ax.set_ylim(ymin,ymax)
    ax.axvspan(*band,color='#f1a0a6',alpha=.15,zorder=-2)
    if center is not None:ax.axvline(center,color=COL,lw=.7,ls=(0,(2,2)),alpha=.75)
    frame(ax,lo,hi,major,minor);ax.set_yticks([]);ax.set_title(title,fontsize=8,pad=7)
    # Each spectral window has its own explicitly quantified intensity scale.
    sx=hi-(hi-lo)*.045;sy=ymax-.05*span-sbar;ax.plot([sx,sx],[sy,sy+sbar],color=COL,lw=.9)
    ax.text(sx-(hi-lo)*.025,sy+sbar/2,f'{sbar:g}',va='center',ha='left',fontsize=8)
    scalebars.append(dict(window=[hi,lo],scale_absorbance=sbar,stack_offset=offset))
axes[0].set_ylabel('Absorbance (a.u.)');letter(axes[0],'a')
fig.text(.49,1-72/H,r'Wavenumber (cm$^{-1}$)',ha='center',va='center',fontsize=8)
# Diagonal break marks retain a common outer top/bottom boundary.
for i,ax in enumerate(axes):
    for side in ([1] if i==0 else [0] if i==2 else [0,1]):
        for y in [0,1]:ax.plot([side-.014,side+.014],[y-.009,y+.009],transform=ax.transAxes,color=COL,lw=.8,clip_on=False)

ga=axmm(165,17,2.5,36)
ga.imshow(np.linspace(0,1,256)[:,None],origin='lower',aspect='auto',cmap=ce,extent=[0,1,0,1]);ga.set_axis_off()
ga.add_patch(Polygon([[-.35,0],[1.35,0],[.5,-.09]],color=PAL[0],transform=ga.transAxes,clip_on=False))
fig.text(168/W,1-12/H,'1.21 V',ha='center',fontsize=8)
fig.text(168/W,1-59/H,'−0.09 V',ha='center',fontsize=8)
fig.text(174/W,1-35/H,'ORR',rotation=90,ha='center',va='center',fontsize=8)
eg=np.unique(np.r_[np.linspace(E[0],E[-1],901),E])
heatmaps=[]
for label,lo,hi,left,width,barleft,lim,peak,text,major,minor,ticks in [
    ('b',2900,3700,13,59,74.5,16,3307,'O–H band weakens',200,100,[-16,-8,0,8,16]),
    ('c',1120,1320,108,49,159.5,10,1215,'Decreasing potential',100,50,[-10,-5,0,5,10])]:
    ax=axmm(left,83,width,54);m=(X>=lo)&(X<=hi);xx=X[m];z=DS[:,m]*1e3
    zi=np.array([np.interp(eg,E,z[:,j]) for j in range(z.shape[1])]).T
    assert np.allclose(zi[np.searchsorted(eg,E)],z)
    pc=ax.imshow(zi,origin='lower',aspect='auto',extent=[xx[0],xx[-1],E[0],E[-1]],cmap=cd,norm=Normalize(-lim,lim),interpolation='nearest',rasterized=True)
    frame(ax,lo,hi,major,minor);ax.set_ylim(E[0],E[-1]);ax.set_yticks([0,.3,.6,.9,1.2]);ax.yaxis.set_minor_locator(MultipleLocator(.15))
    ax.axvline(peak,color=COL,lw=.65,ls=(0,(2,2)),alpha=.75)
    ax.set_xlabel(r'Wavenumber (cm$^{-1}$)');ax.set_ylabel(r'$E$ (V vs. RHE)');letter(ax,label)
    # Arrow/text share one layout; b is in 3100–3000 cm-1, c is right of the 1215 line.
    arrow_x=3060 if label=='b' else 1140
    text_x=3010 if label=='b' else 1158
    ax.annotate('',xy=(arrow_x,.02),xytext=(arrow_x,1.08),arrowprops=dict(arrowstyle='-|>',color=COL,lw=.9,mutation_scale=8))
    ax.text(text_x,.55,text,rotation=90,va='center',ha='right',fontsize=8,color='#000000')
    ax.text(.03,.96,'ref. 1.21 V',transform=ax.transAxes,ha='left',va='top',fontsize=8,color='#000000')
    if label=='c':
        ax.add_patch(Rectangle((1195,E[0]+.006),40,E[-1]-E[0]-.012,fill=False,edgecolor=COL,lw=.7,ls=(0,(3,2))))
    ca=axmm(barleft,83,2,54);cb=fig.colorbar(pc,cax=ca,ticks=ticks);cb.ax.tick_params(labelsize=8,length=2,pad=2)
    cb.set_label(r'ΔAbsorbance ($10^{-3}$), ref. 1.21 V',fontsize=8,labelpad=3)
    heatmaps.append(dict(panel=label,wavenumber=[hi,lo],display_limits_1e3=[-lim,lim],actual_display_extrema_1e3=[float(z.min()),float(z.max())],unclipped=bool(z.min()>=-lim and z.max()<=lim)))

# Numerical position checks use unsmoothed and display-smoothed curves separately.
m=(X>=1191)&(X<=1239);xp=X[m];positions=[]
for i,e in enumerate(E):
    positions.append(dict(E_RHE_V=float(e),label=f'{e:.2f}',raw_absorption_valley_cm1=float(xp[np.argmin(A[i,m])]),display_absorption_valley_cm1=float(xp[np.argmin(S[i,m])]),difference_positive_max_cm1=None if i==12 else float(xp[np.argmax(D[i,m])]),display_difference_positive_max_cm1=None if i==12 else float(xp[np.argmax(DS[i,m])])) )
pd.DataFrame(positions).to_csv(OUT/'1215区峰谷位置_逐电位.csv',index=False,encoding='utf-8-sig')
report=dict(source=str(RAW),files=meta,RHE_offset_V=1.011,reference_exact_V=float(E[-1]),reference_label='1.21 V',smoothing={'points':21,'order':2,'width_cm1':float(np.median(np.diff(X))*21)},baseline='linear extrapolation between mean(x),mean(A) of 1330–1370 and 1900–1950 cm−1',prior_current_processed_absorption_max_difference=old_diff,user_script_comparison='已取得并按参考脚本数据段逐数值核对，RAW/RAWs/RELs差异均为0',scale_bars=scalebars,heatmaps=heatmaps,positions=positions,font='Arial',font_pt=8,panel_letter_pt=10,text_color='#000000',text_weight='normal_all_including_panel_letters',width_mm=W,height_mm=H)
# c uses requested +/-10; saturation is quantified in REPORT, not data clipping.
report['reference_script_differences']=reference_differences
report['O_H_peak_checks']=peakrows
report['panel_letters_weight']='bold'
report['a_mode']='same-baseline overlay; user delegated choice after contradictory spacing note'
report['text_weight']='regular except a/b/c letters bold'
report['O_H_blue_shift_cm1']={k:float(peakrows[0][k]-peakrows[-1][k]) for k in ['SG21_cm1','SG81_cm1','quadratic_peak_cm1']}
report['c_saturated_pixel_fraction']=float(np.mean(np.abs(DS[:,(X>=1120)&(X<=1320)]*1000)>10))
pd.DataFrame(peakrows).to_csv(OUT/'O_H_peak_checks.csv',index=False,encoding='utf-8-sig')
(OUT/'数值核查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')

report['reference_script_sha256']=hashlib.sha256(REFERENCE.read_bytes()).hexdigest()
report['reference_data_paths']=['FeCoMn/data/SEIRAS_20241021_1-2/'+f['file'] for f in meta]
(OUT/'数值核查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
np.savez_compressed(OUT/'processing_arrays.npz',x=X,E=E,RAW=ref['RAW'],REL=ref['REL'],RAWs=ref['RAWs'],RELs=ref['RELs'])
def save(stem):
 plt.rcParams['svg.fonttype']='none';fig.savefig(OUT/(stem+'_editable.svg'),dpi=600)
 fig.savefig(OUT/(stem+'.png'),dpi=600);fig.savefig(OUT/(stem+'_preview.png'),dpi=180)
 plt.rcParams['svg.fonttype']='path';fig.savefig(OUT/(stem+'_Arial_paths.svg'),dpi=600)
save('Figure_4_20261114_204757')

# Alternative only: measured peak shifts, no change to reference data or the base figure.
px=np.array([r['SG81_cm1'] for r in peakrows]);py=np.array([np.interp(v,X,S[i]) for i,v in enumerate(px)])
axes[0].plot(px,py,color=COL,lw=.8,ls=(0,(3,2)))
axes[0].text(.23,.95,'blue shift',transform=axes[0].transAxes,ha='left',va='top',fontsize=8,color='#000000')
save('Figure_4_20261114_204757_blue_shift_option')
print('Reference differences:',reference_differences);print('Saved:',OUT)
