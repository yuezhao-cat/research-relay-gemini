"""T008: new versions only. Reference data stage reused verbatim; no intermediate datasets."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap,Normalize
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon
from PIL import Image
from types import MethodType
OUT=Path(__file__).resolve().parent; REPO=OUT.parents[2]
REFERENCE=REPO/'FeCoMn/scripts/Figure_4_SEIRAS_20261114_script.py'
T003=REPO/'FeCoMn/from_agent/FeCoMn-T003'
RAW=REPO/'FeCoMn/data/SEIRAS_20241021_1-2'
sys.argv=[str(REFERENCE),str(RAW),'unused'];r={}
exec(compile(REFERENCE.read_text(encoding='utf8').split('fig = plt.figure')[0],str(REFERENCE),'exec'),r)
X=r['x'];E=r['E'][::-1];S=r['RAWs'][::-1]/1000;DS=r['RELs'][::-1]/1000
hashes={k:hashlib.sha256(np.ascontiguousarray(r[k]).tobytes()).hexdigest() for k in ['RAW','REL','RAWs','RELs']}
assert hashes==json.loads((T003/'CHECKS.json').read_text(encoding='utf8'))['data_arrays_SHA256']
assert S.shape[0]==13 and np.all(np.diff(E)>0)
# Preserve project typography; normal text, bold 10 pt panel letters.
plt.rcParams.update({'font.family':'Arial','font.size':8,'axes.labelsize':8,'xtick.labelsize':8,'ytick.labelsize':8,'legend.fontsize':8,'text.color':'black','axes.labelcolor':'black','axes.edgecolor':'#404040','xtick.color':'black','ytick.color':'black','font.weight':'normal','axes.labelweight':'normal','axes.titleweight':'normal','axes.linewidth':.8,'xtick.direction':'out','ytick.direction':'out','xtick.major.size':3,'ytick.major.size':3,'xtick.minor.size':1.8,'ytick.minor.size':1.8,'xtick.major.width':.8,'ytick.major.width':.8,'axes.labelpad':3,'mathtext.fontset':'custom','mathtext.rm':'Arial','mathtext.it':'Arial:italic','mathtext.bf':'Arial:bold','mathtext.sf':'Arial','axes.unicode_minus':True,'svg.fonttype':'none','pdf.fonttype':42})
red=LinearSegmentedColormap.from_list('D_red',['#b8394d','#f6bcc4'])
cd=LinearSegmentedColormap.from_list('paper_delta',['#8f8bc0','#d0cce5','#ffffff','#f6bcc4','#eb687b'],N=257)
W,H=177.8,244
geo=[(13,68),(86,30),(121,40)]
regions=[(2900,3650,r'$\nu$(O–H)',200,100,.02),(1560,1720,r'$\delta$(H–O–H)',80,40,.005),(1120,1320,r'1215 cm$^{-1}$ region',100,50,.005)]
EE=np.r_[E[0]-(E[1]-E[0])/2,(E[:-1]+E[1:])/2,E[-1]+(E[-1]-E[-2])/2]
checks={'arrays_equal_T003':True,'data_arrays_SHA256':hashes,'reference_script':str(REFERENCE.relative_to(REPO)),'reference_script_sha256':hashlib.sha256(REFERENCE.read_bytes()).hexdigest(),'raw_sha256':{(n+'.CSV'):hashlib.sha256((RAW/(n+'.CSV')).read_bytes()).hexdigest() for n in r['files']},'RHE_offset':1.011,'canvas_mm':[W,H],'font':'Arial','font_pt':8,'panel_letters_pt':10,'panel_letters_weight':'bold','heatmap_potential_centers':E.tolist(),'heatmap_potential_edges':EE.tolist(),'heatmap_interpolation':False,'variants':[]}
for suffix,elev,azim in [('view1',25,-66),('view2',34,-78)]:
 fig=plt.figure(figsize=(W/25.4,H/25.4),facecolor='white')
 def axmm(l,t,w,h,**kw):return fig.add_axes([l/W,1-(t+h)/H,w/W,h/H],**kw)
 def panel(l,t,text):fig.text(l/W,1-t/H,text,fontsize=10,fontweight='bold',ha='left',va='top',color='black')
 def frame(ax,lo,hi,major,minor):
  ax.set_xlim(hi,lo);ax.xaxis.set_major_locator(MultipleLocator(major));ax.xaxis.set_minor_locator(MultipleLocator(minor));ax.tick_params(pad=2)
  for sp in ax.spines.values():sp.set_linewidth(.8)
 # A: 13 spectra as independent 3D lines, never a height-coloured surface or floor projection.
 ax=axmm(6,0,150,76,projection='3d')
 # Keep the requested full-row physical viewport instead of Axes3D's default square crop.
 def wide_aspect(self,position=None):self._set_position(self.get_position(original=True) if position is None else position,'active')
 ax.apply_aspect=MethodType(wide_aspect,ax)
 m=(X>=1100)&(X<=1800);xx=X[m]
 for i,e in enumerate(E):ax.plot(xx,np.full(xx.shape,e),S[i,m],color=red(i/12),lw=.9)
 ax.set_xlim(1800,1100);ax.set_ylim(E[0],E[-1]);ax.set_zlim(float(S[:,m].min())-.003,float(S[:,m].max())+.003)
 ax.set_xticks([1800,1600,1400,1200]);ax.set_yticks([0,.4,.8,1.2]);ax.set_zticks([])
 ax.set_xlabel('');ax.set_ylabel('');ax.set_zlabel('')
 fig.text(78/W,1-67/H,r'Wavenumber (cm$^{-1}$)',ha='center',va='center')
 fig.text(149/W,1-69/H,r'$E$ (V vs. RHE)',ha='center',va='center')
 fig.text(172/W,1-33/H,'Absorbance (a.u.)',rotation=90,ha='center',va='center')
 ax.set_proj_type('ortho');ax.view_init(elev=elev,azim=azim);ax.set_box_aspect((3.8,1.25,1.1),zoom=1.04)
 ax.grid(False)
 for a in [ax.xaxis,ax.yaxis,ax.zaxis]:a.pane.set_visible(False);a.line.set_color('#404040');a.line.set_linewidth(.8)
 ax.tick_params(labelsize=8,pad=1);panel(3,5,'a')
 # B: same three RAWs windows, same D-red colours and no vertical spectral offsets.
 baxes=[];bars=[]
 for k,((left,width),(lo,hi,title,major,minor,sbar)) in enumerate(zip(geo,regions)):
  a=axmm(left,91,width,54);baxes.append(a);m=(X>=lo)&(X<=hi);z=S[:,m]
  for i,e in enumerate(E):a.plot(X[m],z[i],color=red(i/12),lw=.85)
  span=float(z.max()-z.min());ymin=float(z.min())-.1*span
  # All three scale bars are exactly 12 mm tall, retaining original .02/.005/.005 magnitudes.
  yrange=sbar*54/12;assert yrange>span*1.1;a.set_ylim(ymin,ymin+yrange)
  frame(a,lo,hi,major,minor);a.set_yticks([]);a.set_title(title,fontsize=8,pad=7)
  sx=hi-(hi-lo)*.045;sy=(ymin+.06*yrange) if k==2 else (ymin+yrange-.05*span-sbar)
  a.plot([sx,sx],[sy,sy+sbar],color='#404040',lw=.9);a.text(sx-(hi-lo)*.025,sy+sbar/2,f'{sbar:g} a.u.',ha='left',va='center',fontsize=8)
  bars.append({'panel':'b','window':[hi,lo],'value_a_u':sbar,'drawn_height_mm':12})
 baxes[0].set_ylabel('Absorbance (a.u.)');panel(3,84,'b')
 fig.text(.49,1-154/H,r'Wavenumber (cm$^{-1}$)',ha='center',va='center')
 for i,a in enumerate(baxes):
  for side in ([1] if i==0 else [0] if i==2 else [0,1]):
   for y in [0,1]:a.plot([side-.014,side+.014],[y-.009,y+.009],transform=a.transAxes,color='#404040',lw=.8,clip_on=False)
 ga=axmm(165,98,2.5,36);ga.imshow(np.linspace(0,1,256)[:,None],origin='lower',aspect='auto',cmap=red,extent=[0,1,0,1]);ga.set_axis_off()
 ga.add_patch(Polygon([[-.35,0],[1.35,0],[.5,-.09]],color='#b8394d',transform=ga.transAxes,clip_on=False))
 fig.text(168/W,1-93/H,'1.21 V',ha='center');fig.text(168/W,1-140/H,'−0.09 V',ha='center');fig.text(174/W,1-116/H,'ORR',rotation=90,ha='center',va='center')
 # C-E: original 13 rows, half-distance boundaries, no interpolation in either axis.
 lower=[]
 for k,((left,width),(lo,hi,title,major,minor,sbar),lim,center,name) in enumerate(zip(geo,regions,[16,4,10],[3307,None,1215],['c','d','e'])):
  a=axmm(left,180,width,54);m=(X>=lo)&(X<=hi);xm=X[m];zz=DS[:,m]*1000
  xe=np.r_[xm[0]-(xm[1]-xm[0])/2,(xm[:-1]+xm[1:])/2,xm[-1]+(xm[-1]-xm[-2])/2]
  pc=a.pcolormesh(xe,EE,zz,shading='flat',cmap=cd,norm=Normalize(-lim,lim),rasterized=True,antialiased=False)
  frame(a,lo,hi,major,minor);a.set_ylim(EE[0],EE[-1]);a.set_yticks([0,.3,.6,.9,1.2]);a.yaxis.set_minor_locator(MultipleLocator(.15));a.set_xlabel(r'Wavenumber (cm$^{-1}$)')
  if k==0:a.set_ylabel(r'$E$ (V vs. RHE)')
  else:a.tick_params(labelleft=False)
  if center:a.axvline(center,color='#404040',lw=.65,ls=(0,(2,2)),alpha=.75)
  panel(left-10,174,name)
  ca=axmm(left,169,width,1.9);cb=fig.colorbar(pc,cax=ca,orientation='horizontal',ticks=[-lim,0,lim]);cb.ax.xaxis.set_ticks_position('top');cb.ax.tick_params(labelsize=8,length=2,pad=1);cb.outline.set_linewidth(.65)
  lower.append({'panel':name,'window':[hi,lo],'frame_mm':[left,180,width,54],'rows':13,'limits_1e3':[-lim,lim],'saturation_fraction':float(np.mean(abs(zz)>lim)),'vertical_lines_cm1':[] if center is None else [center]})
 fig.text(13/W,1-160/H,r'ΔAbs. ($10^{-3}$), ref. 1.21 V',ha='left',va='center',fontsize=8)
 stem='Figure_4_20261115_T008_'+suffix
 fig.savefig(OUT/(stem+'_preview.png'),dpi=180)
 plt.rcParams['svg.fonttype']='none';fig.savefig(OUT/(stem+'_editable.svg'),dpi=600)
 fig.savefig(OUT/(stem+'.png'),dpi=600)
 plt.rcParams['svg.fonttype']='path';fig.savefig(OUT/(stem+'_Arial_paths.svg'),dpi=600)
 checks['variants'].append({'name':suffix,'elevation':elev,'azimuth':azim,'scale_bars':bars,'lower_maps':lower,'top_lines':13,'top_plot':'unsubtracted baseline corrected SG21 absorbance','floor_projection':False})
 plt.close(fig)
(OUT/'CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print('T008: all four array SHA256 match T003. Saved both views.')
