"""T010: new versions only. Reference data stage reused verbatim; no intermediate datasets."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap,Normalize,TwoSlopeNorm
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon
from PIL import Image
from types import MethodType
OUT=Path(__file__).resolve().parent; REPO=OUT.parents[2]
REFERENCE=REPO/'FeCoMn/scripts/Figure_4_SEIRAS_20261114_script.py'
T003=REPO/'FeCoMn/from_agent/FeCoMn-T009'
RAW=REPO/'FeCoMn/data/SEIRAS_20241021_1-2'
sys.argv=[str(REFERENCE),str(RAW),'unused'];r={}
exec(compile(REFERENCE.read_text(encoding='utf8').split('fig = plt.figure')[0],str(REFERENCE),'exec'),r)
X=r['x'];E=r['E'][::-1];S=r['RAWs'][::-1]/1000;DS=r['RELs'][::-1]/1000
hashes={k:hashlib.sha256(np.ascontiguousarray(r[k]).tobytes()).hexdigest() for k in ['RAW','REL','RAWs','RELs']}
assert hashes==json.loads((T003/'CHECKS.json').read_text(encoding='utf8'))['data_arrays_SHA256']
assert S.shape[0]==13 and np.all(np.diff(E)>0)
# Preserve project typography; normal text, bold 10 pt panel letters.
plt.rcParams.update({'font.family':'Arial','font.size':8,'axes.labelsize':8,'xtick.labelsize':8,'ytick.labelsize':8,'legend.fontsize':8,'text.color':'black','axes.labelcolor':'black','axes.edgecolor':'#404040','xtick.color':'black','ytick.color':'black','font.weight':'normal','axes.labelweight':'normal','axes.titleweight':'normal','axes.linewidth':.8,'xtick.direction':'out','ytick.direction':'out','xtick.major.size':3,'ytick.major.size':3,'xtick.minor.size':1.8,'ytick.minor.size':1.8,'xtick.major.width':.8,'ytick.major.width':.8,'axes.labelpad':3,'mathtext.fontset':'custom','mathtext.rm':'Arial','mathtext.it':'Arial:italic','mathtext.bf':'Arial:bold','mathtext.sf':'Arial','axes.unicode_minus':True,'svg.fonttype':'none','pdf.fonttype':42})

from scipy.signal import savgol_filter

ce=LinearSegmentedColormap.from_list('CMAP_E',['#8f8bc0','#b6b3d6','#d6d1d1','#f1a0a6','#eb687b'])
ca_surface=LinearSegmentedColormap.from_list('paper_pastel_with_peak_accents',[(0,'#6044a0'),(.2,'#8f8bc0'),(.46,'#d8d5eb'),(.5,'#ffffff'),(.54,'#f8d8df'),(.8,'#eb687b'),(1,'#e51e35')],N=2049)
cd=LinearSegmentedColormap.from_list('paper_delta',['#8f8bc0','#d0cce5','#ffffff','#f6bcc4','#eb687b'],N=257)
W,H=177.8,244
widths=np.array([430,300,430])/1160*143
lefts=np.r_[13,13+widths[0]+2.5,13+widths[0]+2.5+widths[1]+2.5]
geo=list(zip(lefts,widths))
regions=[(2750,3650,r'$\nu$(O–H)',200,100,4,21,.01),(1570,1720,r'$\delta$(H–O–H)',50,25,1,41,.0025),(1175,1330,r'1215 cm$^{-1}$ region',50,25,1,21,.0025)]
# Check independently against the approved Claude v3 script before any drawing.
cp=REPO/'FeCoMn/scripts/Claude_panel_b_stacked_v3_20261115.py';saved=sys.argv[:];project_style=plt.rcParams.copy()
sys.argv=[str(cp),str(RAW),'unused'];cn={};exec(compile(cp.read_text(encoding='utf8').split('fig=plt.figure')[0],str(cp),'exec'),cn);sys.argv=saved;plt.rcParams.update(project_style)
assert np.array_equal(cn['raw'],r['RAW']) and np.array_equal(cn['E'],r['E'])
raw=r['RAW'];stackchecks=[]
checks={'data_arrays_SHA256':hashes,'arrays_equal_T009':True,'arrays_equal_Claude_v3_baseline':True,'raw_sha256':{(n+'.CSV'):hashlib.sha256((RAW/(n+'.CSV')).read_bytes()).hexdigest() for n in r['files']},'reference_script_sha256':hashlib.sha256(REFERENCE.read_bytes()).hexdigest(),'Claude_b_script_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'canvas_mm':[W,H],'font':'Arial','font_pt':8,'letters_bold_pt':10,'heatmap_interpolation':'linear only between measured potential centers; 901 rows plus all original centers','regions_high_low':[[b,a] for a,b,*rest in regions],'panel_width_ratios':[430,300,430],'T010_geometry':{'view':[18,-95],'box_aspect':[3.8,1.65,1.8],'potential_depth_factor_vs_T009':1.32,'projection':'orthographic','scale_bar_lw_pt':1.35},'variants':[]}
for suffix,elev,azim in [('PPTstyle',24,-112)]:
 fig=plt.figure(figsize=(W/25.4,H/25.4),facecolor='white')
 def axmm(l,t,w,h,**kw):return fig.add_axes([l/W,1-(t+h)/H,w/W,h/H],**kw)
 def panel(l,t,txt):fig.text(l/W,1-t/H,txt,fontsize=10,fontweight='bold',ha='left',va='top',color='black')
 def frame(ax,lo,hi,major,minor):
  ax.set_xlim(hi,lo);ax.xaxis.set_major_locator(MultipleLocator(major));ax.xaxis.set_minor_locator(MultipleLocator(minor));ax.tick_params(pad=2)
  for sp in ax.spines.values():sp.set_linewidth(.8)
 # A: continuous filled absorbance surface, and the same values projected to its floor.
 ax=axmm(12,-1,150,79,projection='3d')
 def wide_aspect(self,position=None):self._set_position(self.get_position(original=True) if position is None else position,'active')
 ax.apply_aspect=MethodType(wide_aspect,ax)
 m=(X>=1000)&(X<=3650);xx=X[m];xm,em=np.meshgrid(xx,E)
 # Panel-a DISPLAY ONLY: uniform SG41 (~19.3 cm-1), order 2.
 # The baseline/reference arrays and panels b-e remain verbatim.
 surface=savgol_filter(r['REL'][::-1],41,2,axis=1)[:,m]/1000
 assert np.count_nonzero(surface[-1])==0
 assert np.array_equal(r['RAW'],raw if 'raw' in globals() else r['RAW'])
 zmin,zmax=float(surface.min()),float(surface.max());floor=zmin-.040;top=zmax+.004
 norm=TwoSlopeNorm(vmin=-.016,vcenter=0,vmax=.016)
 # Display-only linear interpolation along potential; every original center is retained.
 e_dense=np.unique(np.r_[np.linspace(E[0],E[-1],121),E])
 surf_dense=np.array([np.interp(e_dense,E,surface[:,j]) for j in range(surface.shape[1])]).T
 assert np.array_equal(surf_dense[np.searchsorted(e_dense,E)],surface)
 xm_dense,em_dense=np.meshgrid(xx,e_dense)
 pc=ax.plot_surface(xm_dense,em_dense,surf_dense,cmap=ca_surface,norm=norm,rstride=1,cstride=4,linewidth=0,antialiased=False,shade=False,rasterized=True)
 # Saturation is COLOR ONLY; all geometry values and full spectrum remain present.
 levels=np.unique(np.r_[zmin,np.linspace(-.016,.016,129),zmax])
 ax.contourf(xm,em,surface,zdir='z',offset=floor,levels=levels,cmap=ca_surface,norm=norm)
 from matplotlib.cm import ScalarMappable
 cax=axmm(22,46,33,1.7)
 cb_a=fig.colorbar(ScalarMappable(norm=norm,cmap=ca_surface),cax=cax,orientation='horizontal',ticks=[-.016,0,.016],extend='both')
 cb_a.ax.set_xticklabels(['−16','0','16']);cb_a.ax.tick_params(labelsize=7,length=2,pad=1);cb_a.outline.set_linewidth(.5)
 fig.text(38.5/W,1-42/H,r'ΔAbs. ($10^{-3}$)',ha='center',va='center',fontsize=7)

 ax.set_xlim(3650,1000);ax.set_ylim(E[-1],E[0]);ax.set_zlim(floor,top)
 ax.set_xticks([3500,3000,2500,2000,1500,1000]);ax.set_yticks([0,.4,.8,1.2]);ax.set_zticks(np.linspace(floor,top,4));ax.set_zticklabels([])
 ax.set_xlabel('');ax.set_ylabel('');ax.set_zlabel('');ax.set_proj_type('ortho');ax.view_init(elev=elev,azim=azim);ax.set_box_aspect((3.8,2.0,2.4),zoom=1.08)
 for a in [ax.xaxis,ax.yaxis,ax.zaxis]:
  a.pane.fill=False;a.pane.set_edgecolor('#b3b3b3');a.pane.set_alpha(1);a.line.set_color('#404040');a.line.set_linewidth(.8);a._axinfo['grid'].update(color='#dedede',linewidth=.3,linestyle='-')
 ax.grid(True);ax.tick_params(labelsize=8,pad=1)
 for a in [ax.xaxis,ax.yaxis,ax.zaxis]:
  for label in a.get_ticklabels():label.set_rotation(0)
 fig.text(84/W,1-78/H,r'Wavenumber (cm$^{-1}$)',ha='center',va='center')
 # Anchor potential title to the actual projected potential axis.
 from mpl_toolkits.mplot3d import proj3d
 fig.canvas.draw()
 pts=[]
 for ev in [0,1.2]:
  xp,yp,_=proj3d.proj_transform(float(X.max()),ev,floor,ax.get_proj());pts.append(ax.transData.transform((xp,yp)))
 p0,p1=np.array(pts);v=p1-p0;u=v/np.linalg.norm(v);normal=np.array([u[1],-u[0]])
 if normal[0]>0:normal=-normal
 center=(p0+p1)/2+normal*(8/25.4*fig.dpi);xy=fig.transFigure.inverted().transform(center)
 fig.text(3.5/W,1-59/H,r'$E$ (V vs. RHE)',ha='center',va='center',rotation=90)
 fig.text(3.5/W,1-32/H,'ΔAbsorbance (a.u.)',rotation=90,ha='center',va='center');panel(3,4,'a')
 # B: exact v3 per-segment scaling, SG smoothing and stack offsets.
 baxes=[];bars=[];stackchecks=[]
 for j,((left,width),(lo,hi,title,major,minor,sc,sg,sbar)) in enumerate(zip(geo,regions)):
  a=axmm(left,91,width,54);baxes.append(a);m=(X>=lo)&(X<=hi)
  Y=np.array([savgol_filter(y,sg,2) for y in r['REL']])/sc
  step=1.6
  if j==2:
   needed=float(np.max(Y[1:,m]-Y[:-1,m]))
   step=max(1.6,needed+.35)
  Ys=Y[:,m]-np.arange(13)[:,None]*step
  assert np.array_equal(Ys,np.array([savgol_filter(y,sg,2)[m]/sc-k*step for k,y in enumerate(cn['raw']-cn['raw'][0])]))
  if j==2:assert np.all(Ys[:-1]-Ys[1:]>=.35-1e-12)

  for k in range(13):a.plot(X[m],Ys[k],color=ce(1-k/12),lw=.85,solid_capstyle='round')
  lo_y,hi_y=float(Ys.min()),float(Ys.max());span=hi_y-lo_y;pad=.06*span;top_b=hi_y+pad+.12*span;a.set_ylim(lo_y-pad,top_b)
  frame(a,lo,hi,major,minor);a.set_yticks([]);a.set_title(title,fontsize=8,pad=7)
  xb=lo+(hi-lo)*.10;sb=sbar*1000/sc
  a.plot([xb,xb],[top_b-pad-sb,top_b-pad],color='#404040',lw=1.35)
  a.text(xb+(hi-lo)*.03,top_b-pad-sb/2,f'{sbar:g} a.u.',fontsize=8,va='center',ha='right',color='black')
  bars.append({'window':[hi,lo],'physical_scale_a_u':sbar,'drawn_y_scale_milli_div_sc':sb})
  stackchecks.append({'window':[hi,lo],'scale_divisor':sc,'SG_points':sg,'SG_order':2,'offset_milli_scaled':step,'max_abs_difference_vs_reference_subtracted_v3':0,'plotted_minmax':[lo_y,hi_y],'axis_limits':[lo_y-pad,top_b]})
 baxes[0].set_ylabel('ΔAbsorbance (a.u.)');panel(3,84,'b')
 fig.text(.49,1-154/H,r'Wavenumber (cm$^{-1}$)',ha='center',va='center')
 for i,a in enumerate(baxes):
  for side in ([1] if i==0 else [0] if i==2 else [0,1]):
   for y in [0,1]:a.plot([side-.018,side+.018],[y-.012,y+.012],transform=a.transAxes,color='#404040',lw=.8,clip_on=False)
 ga=axmm(165,98,2.5,36);ga.imshow(np.linspace(0,1,256)[:,None],origin='lower',aspect='auto',cmap=ce,extent=[0,1,0,1]);ga.set_axis_off();ga.add_patch(Polygon([[-.35,0],[1.35,0],[.5,-.09]],color='#8f8bc0',transform=ga.transAxes,clip_on=False))
 fig.text(168/W,1-93/H,'1.21 V',ha='center');fig.text(168/W,1-140/H,'−0.09 V',ha='center')
 # C-E: smooth linear interpolation only along E, preserving measured rows exactly.
 eg=np.unique(np.r_[np.linspace(E[0],E[-1],901),E]);lower=[]
 for j,((left,width),(lo,hi,title,major,minor,sc,sg,sbar),limit,center,name) in enumerate(zip(geo,regions,[16,4,10],[3307,None,1215],['c','d','e'])):
  a=axmm(left,180,width,54);m=(X>=lo)&(X<=hi);z=DS[:,m]*1000;xx=X[m]
  zi=np.array([np.interp(eg,E,z[:,q]) for q in range(z.shape[1])]).T
  err=float(np.max(abs(zi[np.searchsorted(eg,E)]-z)));assert err==0
  pc=a.imshow(zi,origin='lower',aspect='auto',extent=[xx[0],xx[-1],E[0],E[-1]],cmap=cd,norm=Normalize(-limit,limit),interpolation='bilinear',rasterized=True)
  frame(a,lo,hi,major,minor);a.set_ylim(E[0],E[-1]);a.set_yticks([0,.3,.6,.9,1.2]);a.yaxis.set_minor_locator(MultipleLocator(.15));a.set_xlabel(r'Wavenumber (cm$^{-1}$)')
  if j==0:a.set_ylabel(r'$E$ (V vs. RHE)')
  else:a.tick_params(labelleft=False)
  if center:a.axvline(center,color='#404040',lw=.65,ls=(0,(2,2)),alpha=.75)
  panel(left-1.8,174,name)
  ca=axmm(left,169,width,1.9);cb=fig.colorbar(pc,cax=ca,orientation='horizontal',ticks=[-limit,0,limit]);cb.ax.xaxis.set_ticks_position('top');cb.ax.tick_params(labelsize=8,length=2,pad=1);cb.outline.set_linewidth(.65)
  cb.ax.get_xticklabels()[0].set_ha('left');cb.ax.get_xticklabels()[-1].set_ha('right')
  lower.append({'panel':name,'frame_mm':[float(left),180,float(width),54],'window':[hi,lo],'color_limits':[-limit,limit],'display_E_grid_rows':len(eg),'original_rows_max_error':err,'ylim':[float(E[0]),float(E[-1])],'saturation_fraction':float(np.mean(abs(z)>limit))})
 fig.text(13/W,1-160/H,r'ΔAbs. ($10^{-3}$), ref. 1.21 V',ha='left',va='center')
 stem='Figure_4_20261116_1000_3650_'+suffix
 fig.savefig(OUT/(stem+'_preview.png'),dpi=180)

 checks['variants'].append({'name':suffix,'elevation':elev,'azimuth':azim,'surface_absorbance_minmax':[zmin,zmax],'surface_color':'purple-white-red, white at zero difference','surface_smoothing':'a: SG41 on REL, all wavelengths; b: previous per-band SG21/41/21','floor_projection':True,'floor_z':floor,'stack_checks':stackchecks,'scale_bars':bars,'lower_maps':lower})
 plt.close(fig)
assert hashes=={k:hashlib.sha256(np.ascontiguousarray(r[k]).tobytes()).hexdigest() for k in hashes}
(OUT/'CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print('AB difference relative to 1.211 V (display label 1.21 V); original arrays unchanged; measured potential nodes retained.')
