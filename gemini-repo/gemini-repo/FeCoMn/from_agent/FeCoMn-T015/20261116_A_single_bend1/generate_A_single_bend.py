"""T015, 2026-11-16. Run from any directory. Source CSVs are read-only.
--preview-only creates review PNGs; default exports 600-dpi PNG + two SVGs too.
"""
from pathlib import Path
import argparse,hashlib,json,math,csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap,TwoSlopeNorm,Normalize,Colormap,to_rgba
from matplotlib.cm import ScalarMappable
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d import proj3d
from scipy.signal import savgol_filter
from types import MethodType

OUT=Path(__file__).resolve().parent;REPO=next(p for p in Path(__file__).resolve().parents if (p/'FeCoMn/data/SEIRAS_20241021_1-2').is_dir())
DATA=REPO/'FeCoMn/data/SEIRAS_20241021_1-2'
STAMP='20261116_A_single_bend1'
FILES=['0.2','0.1','0','-0.1','-0.2','-0.3','-0.4','-0.5','-0.6','-0.7','-0.8','-0.9','-11']
ANCHORS=[(1330,1370),(1900,1950),(2550,2650),(3850,3950)]
plt.rcParams.update({'font.family':'Arial','font.size':8,'axes.labelsize':8,'axes.titlesize':8,'xtick.labelsize':8,'ytick.labelsize':8,'legend.fontsize':8,'font.weight':'normal','axes.labelweight':'normal','text.color':'black','axes.labelcolor':'black','axes.edgecolor':'#404040','xtick.color':'black','ytick.color':'black','axes.linewidth':.8,'xtick.direction':'out','ytick.direction':'out','xtick.major.size':3,'ytick.major.size':3,'xtick.minor.size':1.8,'ytick.minor.size':1.8,'xtick.major.width':.8,'ytick.major.width':.8,'mathtext.fontset':'custom','mathtext.rm':'Arial','mathtext.it':'Arial:italic','mathtext.bf':'Arial:bold','svg.fonttype':'none','axes.unicode_minus':True})
CE=LinearSegmentedColormap.from_list('E',['#8f8bc0','#b6b3d6','#d6d1d1','#f1a0a6','#eb687b'])
CD=LinearSegmentedColormap.from_list('D',[(0,'#8f8bc0'),(.30,'#b6b3d6'),(.43,'#d0cce5'),(.5,'#ffffff'),(.60,'#f6bcc4'),(.82,'#eb687b'),(1,'#c9243f')],N=2049)
NORM=TwoSlopeNorm(vmin=-8,vcenter=0,vmax=8)
BASE_CD=CD
BASE_NORM=NORM
class TailColorMap(Colormap):
 def __init__(self):
  super().__init__('tiny_negative_tail',N=2049);self.monochrome=False
 def _init(self):
  self._lut=self(np.linspace(0,1,self.N+3));self._isinit=True;self._set_extremes()
 def __call__(self,X,alpha=None,bytes=False):
  v=np.asarray(X)*18-10
  rgba=np.array(BASE_CD(BASE_NORM(v)),copy=True)
  w=np.clip((-7.4-v)/2.551740327658522,0,1)
  w=w**2.0
  rgba=rgba*(1-w[...,None])+np.array(to_rgba('#655292'))*w[...,None]
  if alpha is not None:rgba[...,3]=alpha
  return (rgba*255).astype('uint8') if bytes else rgba
CD=TailColorMap()
NORM=Normalize(vmin=-10,vmax=8)
W=177.8
WIDTHS=np.array([430,300,430])/1160*143
LEFTS=np.r_[13,13+WIDTHS[0]+2.5,13+WIDTHS[0]+2.5+WIDTHS[1]+2.5]
RIGHT=float(LEFTS[-1]+WIDTHS[-1])
REGIONS=[(2750,3650,r'$\nu$(O–H)',200,100,1,21,.005,3307),(1570,1720,r'$\delta$(H–O–H)',50,25,1,41,.005,1633),(1175,1330,r'OOH*',50,25,1,21,.005,1215)]
VARIANTS=[('V1',24,2.5,2.0,-93),('V2',26,2.9,2.1,-95),('V3',28,2.8,2.3,-97)]

def sha(a):return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()
def prepare():
 arr=[];counts={};base=[];rawhash={}
 for name in FILES:
  p=DATA/(name+'.CSV');rawhash[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
  a=np.genfromtxt(p,delimiter=',');good=np.isfinite(a[:,0])&np.isfinite(a[:,1]);counts[p.name]={'rows':len(a),'deleted_nonfinite':int((~good).sum())}
  a=a[good];a=a[np.argsort(a[:,0])]
  if arr:assert np.array_equal(x,a[:,0])
  x=a[:,0];y=a[:,1];arr.append(y)
  px=np.array([x[(x>=lo)&(x<=hi)].mean() for lo,hi in ANCHORS]);py=np.array([y[(x>=lo)&(x<=hi)].mean() for lo,hi in ANCHORS]);base.append(np.interp(x,px,py))
 A=np.array(arr);B=np.array(base);R=A-B;D=(R-R[0])*1000
 E=np.array([(-1.0 if name=='-11' else float(name))+1.016 for name in FILES])
 assert np.all(np.diff(E)<0) and np.count_nonzero(D[0])==0
 expected=[0.,-.3,2.1,-9.8,-3.8,7.0];windows=[(2500,2700),(2000,2200),(3700,3800),(3257,3357),(1613,1653),(1191,1239)]
 means=[]
 for (lo,hi),target in zip(windows,expected):
  value=float(D[-1,(x>=lo)&(x<=hi)].mean());assert abs(value-target)<.051
  means.append({'window_cm-1':[lo,hi],'unsmoothed_mean_delta_milli':value,'Claude_rounded':target,'rounded_match':round(value,1)==target,'SG41_mean_delta_milli':float(savgol_filter(D[-1],41,2)[(x>=lo)&(x<=hi)].mean())})
 checks={'source':'FeCoMn/data/SEIRAS_20241021_1-2/','used_FILES':FILES,'unused_duplicate':'-1.CSV','source_SHA256':rawhash,'read_counts':counts,'E_RHE':E.tolist(),'E_note':'All E_RHE = E_SCE + 1.016 V; -11.CSV is remeasured -1.0 V vs SCE per user correction 2026-11-16, E_RHE=0.016 V, displayed0V','reference':'0.2.CSV=1.216 V; display 1.22 V','anchors_cm-1':ANCHORS,'baseline':'per-spectrum mean x and mean y; piecewise linear np.interp; constant endpoint extension outside anchors, matching supplied Claude script','means':means,'array_SHA256':{'x':sha(x),'instrument_absorbance':sha(A),'four_point_baseline':sha(B),'corrected_absorbance':sha(R),'difference_milli':sha(D)},'SI_note':'Instrument/open-circuit-background absorbance; display SG only; NO additional four-point baseline and NO subtraction of 1.22 V','variants':[],'SI':[]}
 return x,A,R,D,E,checks

def axes_mm(fig,l,t,w,h,H,**kw):return fig.add_axes([l/W,1-(t+h)/H,w/W,h/H],**kw)
def letter(fig,x,t,s,H):fig.text(7.0/W,1-t/H,s,fontsize=10,fontweight='bold',ha='center',va='top')
def export(fig,name,preview):
 fig.savefig(OUT/(name+'_preview.png'),dpi=180,facecolor='white')
 if not preview:
  fig.savefig(OUT/(name+'.png'),dpi=600,facecolor='white')
  plt.rcParams['svg.fonttype']='none';fig.savefig(OUT/(name+'_editable.svg'),dpi=600)
  plt.rcParams['svg.fonttype']='path';fig.savefig(OUT/(name+'_Arial_paths.svg'),dpi=600);plt.rcParams['svg.fonttype']='none'
 print('EXPORTED',name,flush=True)

def stack(fig,x,V,E,H,top=109,height=54,raw=False,panel=True):
 reports=[];axes=[];prepared=[]
 # Same data multiplier AND same y-span/physical height, not merely the same label.
 for j,region in enumerate(REGIONS):
  lo,hi,title,major,minor,_,sg,_,center=region;m=(x>=lo)&(x<=hi)
  Y=savgol_filter(V,sg,2,axis=1)[:,m]
  step=1.6 if raw or j==2 else 2.4
  if j==2 or raw:step=max(step,float(np.max(Y[1:]-Y[:-1]))+.35)
  YY=Y-np.arange(13)[:,None]*step
  if j==2 or raw:assert np.min(YY[:-1]-YY[1:])>=.35-1e-12
  prepared.append((m,Y,YY,step))
 if not raw:
  # Match reference placement: both first bands span the same stack depth as 1215.
  # This is a display translation only; all data multipliers and y-scales stay equal.
  target_low=float(prepared[2][2].min())
  for j in (0,1):
   m,Y,YY,step=prepared[j]
   step=float(np.min((Y[1:]-target_low)/np.arange(1,13)[:,None]))
   YY=Y-np.arange(13)[:,None]*step
   assert abs(float(YY.min())-target_low)<1e-10
   prepared[j]=(m,Y,YY,step)
 if not raw:
  target_span=max(float(np.ptp(q[2])) for q in prepared)
  filled=[]
  for m,Y,YY,step in prepared:
   lower=step;higher=step+target_span
   for _ in range(64):
    trial=(lower+higher)/2
    trialY=Y-np.arange(13)[:,None]*trial
    if np.ptp(trialY)<target_span:lower=trial
    else:higher=trial
   step=(lower+higher)/2;YY=Y-np.arange(13)[:,None]*step;YY-=YY.min()
   assert abs(np.ptp(YY)-target_span)<1e-8
   assert np.min(YY[:-1]-YY[1:])>0
   filled.append((m,Y,YY,step))
  prepared=filled
  # Adjust offsets only, retaining the original physical panel dimensions.
  spaced=[]
  for m,Y,YY,step in prepared:
   step*=1.15
   YY=Y-np.arange(13)[:,None]*step
   YY-=YY.min()
   spaced.append((m,Y,YY,step))
  prepared=spaced
 low=min(float(q[2].min()) for q in prepared);high=max(float(q[2].max()) for q in prepared)
 span=high-low;pad=.06*span;bottom_pad=pad;bar_bottom=high+.06*span;bar_top=bar_bottom+5.;upper=high+pad
 for j,(left,width,region) in enumerate(zip(LEFTS,WIDTHS,REGIONS)):
  lo,hi,title,major,minor,_,sg,_,center=region
  ax=axes_mm(fig,float(left),top,float(width),height,H);axes.append(ax);m=(x>=lo)&(x<=hi)
  m,Y,YY,step=prepared[j]
  if j==2 and not raw:
   YY=YY.copy();YY[0]+=1.0
  for k in range(13):ax.plot(x[m],YY[k],color=CE(1-k/12),lw=.85 if raw else 1.15,solid_capstyle='round')
  ax.set_ylim(low-bottom_pad,upper);ax.set_xlim(3600 if j==0 and not raw else hi,lo);ax.set_yticks([])
  ax.xaxis.set_major_locator(MultipleLocator(major));ax.xaxis.set_minor_locator(MultipleLocator(minor));ax.tick_params(pad=2)
  ax.set_title('')
  ax.text(center,1.035,title,transform=ax.get_xaxis_transform(),fontsize=8,ha='center',va='bottom')
  if not raw:
   if j!=2:
    center_values=np.array([np.interp(center,x[m],row) for row in YY])
    ax.plot([center,center],[float(center_values.min()),float(center_values.max())],color='#404040',lw=.95,ls=(0,(2.5,3)),alpha=.95,zorder=0)
   else:
    bandx=x[m];pm=(bandx>=1191)&(bandx<=1239)
    indices=np.flatnonzero(pm)[np.argmax(Y[:,pm],axis=1)]
    # Reference spectrum is flat: extend the adjacent real peak position through it.
    indices[0]=indices[1]
    peakx=bandx[indices];peaky=YY[np.arange(13),indices]
    # Visual trend guide: quadratic x(y) has one bend, avoiding noisy local wiggles.
    gy=np.linspace(float(peaky.min()),float(peaky.max()),800)
    scale=float(np.ptp(peaky));mid=float(peaky.mean())
    coefficients=np.polyfit((peaky[1:]-mid)/scale,peakx[1:],2)
    from scipy.optimize import brentq
    def endpoint(row):
     def residual(y):
      xx=float(np.polyval(coefficients,(y-mid)/scale))
      return y-float(np.interp(xx,bandx,row))
     a=float(row.min());b=float(row.max())
     return a if abs(b-a)<1e-12 else brentq(residual,a,b)
    gy=np.linspace(endpoint(YY[-1]),endpoint(YY[0]),800)
    gx=np.polyval(coefficients,(gy-mid)/scale)
    ax.plot(gx,gy,color='#404040',lw=.95,ls=(0,(2.5,3)),alpha=.95,zorder=0)
    (OUT/'OOH_peak_positions.json').write_text(json.dumps({'E_RHE':E.tolist(),'peak_cm-1':peakx.tolist(),'reference_note':'reference spectrum is flat; quadratic one-bend visual guide through peak trend, not a new spectral fit; guide restricted to spectral extent','visual_guide_quadratic_x_coefficients':coefficients.tolist()},indent=2),encoding='utf-8')
  for side in ([1] if j==0 else [0] if j==2 else [0,1]):
   for yy in (0,1):ax.plot([side-.018,side+.018],[yy-.012,yy+.012],transform=ax.transAxes,color='#404040',lw=.8,clip_on=False)
  reports.append({'window_cm-1':[hi,lo],'SG_points':sg,'scale_divisor':1,'stack_step_milli_div_sc':step,'min_adjacent_gap':float(np.min(YY[:-1]-YY[1:])),'E_order_top_to_bottom':'high to low','scale_bar_absorbance':None,'common_scale_bar_applies':None,'common_ylim_milli':[low-bottom_pad,upper],'common_absorbance_per_mm':(upper-low+bottom_pad)/height/1000,'bar_bottom_above_curve_max':bar_bottom-high,'frame_mm':[float(left),top,float(width),height],'display_array_SHA256':sha(Y)})
 assert len({q['common_absorbance_per_mm'] for q in reports})==1
 axes[0].set_ylabel('Absorbance' if raw else 'ΔAbsorbance')
 if not raw:
  axes[0].yaxis.set_label_coords((7.0-LEFTS[0])/WIDTHS[0],.5)
  axes[0].yaxis.label.set_horizontalalignment('center');axes[0].yaxis.label.set_verticalalignment('center')
 fig.text((13+RIGHT)/2/W,1-(top+height+9)/H,r'Wavenumber (cm$^{-1}$)',ha='center',va='center')
 gtop=top+7;gh=height-17;ga=axes_mm(fig,165,gtop,2.5,gh,H)
 ga.imshow(np.linspace(0,1,256)[:,None],origin='lower',aspect='auto',cmap=CE,extent=[0,1,0,1]);ga.set_axis_off()
 ga.add_patch(Polygon([[-.35,0],[1.35,0],[.5,-.09]],color='#8f8bc0',transform=ga.transAxes,clip_on=False))
 fig.text(168/W,1-(top+1)/H,'1.2 V',ha='center',va='center');fig.text(168/W,1-(gtop+gh+5)/H,'0 V',ha='center',va='center')
 if panel:letter(fig,3,top-10,'b',H)
 return reports

def project_mm(fig,ax,x,y,z):
 xx,yy,_=proj3d.proj_transform(x,y,z,ax.get_proj());p=fig.transFigure.inverted().transform(ax.transData.transform((xx,yy)))
 return np.array([p[0]*W,(1-p[1])*fig.get_figheight()*25.4])

def main_figure(x,D,E,variant,preview):
 name,elev,depth,zheight,azim=variant;H=178
 fig=plt.figure(figsize=(W/25.4,H/25.4),facecolor='white')
 ax=axes_mm(fig,8,15,160,86,H,projection='3d',computed_zorder=False)
 def free_aspect(self,position=None):self._set_position(self.get_position(original=True) if position is None else position,'active')
 ax.apply_aspect=MethodType(free_aspect,ax)
 mask=(x>=1000)&(x<=3650);xs=x[mask];Z=savgol_filter(D,41,2,axis=1)[:,mask]
 assert np.count_nonzero(Z[0])==0
 # Interpolate E for the surface only; keep all measured centers explicitly.
 ea=E[::-1];eg=np.unique(np.r_[np.linspace(ea[0],ea[-1],91),ea])
 zi=np.array([np.interp(eg,ea,Z[::-1,j]) for j in range(Z.shape[1])]).T
 assert np.array_equal(zi[np.searchsorted(eg,ea)],Z[::-1])
 # Graphics vertex stride ~1.45 cm-1, below the 4 cm-1 acquisition resolution.
 ix=np.unique(np.r_[np.arange(0,len(xs),3),len(xs)-1]);XX,EE=np.meshgrid(xs[ix],eg);ZZ=zi[:,ix]
 floor=-42.;top=max(12.,float(Z.max())+2.5)
 ax.set_xlim(3650,1000);ax.set_ylim(E.max(),E.min());ax.set_proj_type('persp',focal_length=1.6);ax.view_init(elev=elev,azim=azim)
 zoom=1.
 def align():
  nonlocal zoom
  for _ in range(4):
   ax.set_box_aspect((3.8,depth,zheight),zoom=zoom);fig.canvas.draw()
   pp=np.array([project_mm(fig,ax,v,e,z) for v in (3650,1000) for e in (E.min(),E.max()) for z in (floor,top)])
   zoom*=(RIGHT-13)/(pp[:,0].max()-pp[:,0].min());ax.set_box_aspect((3.8,depth,zheight),zoom=zoom);fig.canvas.draw()
   pp=np.array([project_mm(fig,ax,v,e,z) for v in (3650,1000) for e in (E.min(),E.max()) for z in (floor,top)]);pos=ax.get_position();ax.set_position([pos.x0+(13-pp[:,0].min())/W,pos.y0,pos.width,pos.height])
  fig.canvas.draw()
 for _ in range(8):
  ax.set_zlim(floor,top);align()
  # At each wavenumber, entire floor must be below the entire surface on screen.
  cols=np.arange(0,len(xs),40)
  gaps=[]
  for j in cols:
   floor_top=min(project_mm(fig,ax,xs[j],ev,floor)[1] for ev in (E.min(),E.max()))
   surface_bottom=max(project_mm(fig,ax,xs[j],ev,z)[1] for ev,z in zip(E,Z[:,j]))
   gaps.append(floor_top-surface_bottom)
  if min(gaps)>=5.0:break
  floor-=4
 assert min(gaps)>=5.0,('projection obstruction',name,min(gaps))
 ax.contourf(XX,EE,ZZ,zdir='z',offset=floor,levels=np.r_[np.linspace(-10,-8,33)[:-1],np.linspace(-8,8,129)],extend='both',cmap=CD,norm=NORM,zorder=1)
 ax.plot_surface(XX,EE,ZZ,facecolors=CD(NORM(ZZ)),rstride=1,cstride=1,linewidth=0,shade=False,antialiased=False,rasterized=True,zorder=2)
 # User follow-up: no overlay lines on the 3D surface; all 13 E nodes stay in the mesh.
 ax.set_xticks([3500,3000,2500,2000,1500,1000]);ax.set_yticks([E.min(),.4,.8,1.2]);ax.set_yticklabels([]);ax.set_zticks([])
 ax.zaxis.set_ticks_position('upper');ax.zaxis.set_label_position('upper');ax.yaxis.set_ticks_position('lower')
 ax.tick_params(axis='x',pad=1);ax.tick_params(axis='y',pad=1);ax.tick_params(axis='z',pad=1)
 ax.yaxis._axinfo['tick']['inward_factor']=0.0
 ax.yaxis._axinfo['tick']['outward_factor']=0.0
 ax.set_xlabel('');ax.set_ylabel('');ax.set_zlabel('')
 for axis in (ax.xaxis,ax.yaxis,ax.zaxis):
  axis.pane.fill=False;axis.pane.set_edgecolor('#cccccc');axis.pane.set_alpha(1);axis.line.set_color('#777777');axis.line.set_linewidth(.65)
 ax.grid(False);fig.canvas.draw()
 ax.zaxis.line.set_visible(False)
 ends=np.array([project_mm(fig,ax,v,E.max(),floor) for v in (3650,1000)])
 corners=np.array([project_mm(fig,ax,v,e,z) for v in (3650,1000) for e in (E.min(),E.max()) for z in (floor,top)])
 errors=np.array([corners[:,0].min(),corners[:,0].max()])-[13,RIGHT];assert np.max(abs(errors))<.02
 from matplotlib.lines import Line2D
 fig.add_artist(Line2D(ends[:,0]/W,1-ends[:,1]/H,transform=fig.transFigure,color='#404040',linewidth=.8,solid_capstyle='butt',zorder=30))
 xlabel_y=float(max(ends[:,1])+9)
 fig.text((13+RIGHT)/2/W,1-xlabel_y/H,r'Wavenumber (cm$^{-1}$)',ha='center',va='center')
 # Match the visible E edge; label kept outside the tick numbers.
 ep=np.array([project_mm(fig,ax,3650,e,floor) for e in (E.min(),E.max())]);ey=float(np.mean(ep[:,1]))
 fig.add_artist(Line2D(ep[:,0]/W,1-ep[:,1]/H,transform=fig.transFigure,color='#404040',linewidth=.8,zorder=30))
 e_tick_texts=[]
 for ev,lab in [(E.min(),'0'),(.4,'0.4'),(.8,'0.8'),(1.2,'1.2')]:
  p=project_mm(fig,ax,3650,ev,floor)
  fig.add_artist(Line2D(np.array([p[0]-1.2,p[0]])/W,np.array([1-p[1]/H]*2),transform=fig.transFigure,color='#404040',linewidth=.8,zorder=31,solid_capstyle='butt'))
  e_tick_texts.append(fig.text((p[0]-2.0)/W,1-p[1]/H,lab,ha='right',va='center',fontsize=8))
 ey=float(np.mean([project_mm(fig,ax,1000,e,floor)[1] for e in (E.min(),E.max())]))
 e_title=fig.text(7.0/W,1-float(np.mean(ep[:,1]))/H,r'$E$ (V vs. RHE)',ha='center',va='center',rotation=90)
 zp=np.array([project_mm(fig,ax,3650,E.min(),z) for z in (-10,10)]);zy=float(np.mean(zp[:,1]))
 zy=float(project_mm(fig,ax,1000,E.max(),0)[1])
 # Restore the left vertical signal axis without adding numerical z ticks.
 zedge=np.array([project_mm(fig,ax,3650,E.min(),zv) for zv in (floor,top)])
 fig.add_artist(Line2D(zedge[:,0]/W,1-zedge[:,1]/H,transform=fig.transFigure,color='black',linewidth=.8,zorder=30))
 zangle=float(np.degrees(np.arctan2(-(zedge[1,1]-zedge[0,1]),zedge[1,0]-zedge[0,0])))
 fig.text((float(zedge[:,0].mean())-2.5)/W,1-float(zedge[:,1].mean())/H,'ΔAbsorbance',ha='center',va='center',rotation=zangle,rotation_mode='anchor',fontsize=8,color='black')
 # Feature labels float above the complete real surface at their wavenumber.
 labels=[]
 for xv,label in [(3307,r'$\nu$(O–H)'),(2340,r'CO$_2$(g)'),(1633,r'$\delta$(H–O–H)'),(1215,r'OOH*')]:
  j=int(np.argmin(abs(xs-xv)));z=float(Z[:,j].max()+2.7)
  band_projection=np.array([project_mm(fig,ax,xv,ev,zz) for ev,zz in zip(E,Z[:,j])])
  p=np.array([float(np.median(band_projection[:,0])),float(band_projection[:,1].min()-2)])
  if xv!=1215:
   peak_row=int(np.argmax(np.abs(Z[:,j])))
   p[0]=band_projection[peak_row,0]
  if xv==1215:p += np.array([.5,4.5])
  if xv==2340:p += np.array([0.,.5])
  if xv==1633:p += np.array([0.,-1.5])
  p=np.array({'3307': [30.887684415028883, 37.88087656667137], '2340': [79.53665473330726, 31.202381574133362], '1633': [115.03419709454958, 31.55670732561977], '1215': [143.53397990544744, 29.962258720985115]}[str(xv)])
  fig.text(p[0]/W,1-p[1]/H,label,ha='center',va='bottom',fontsize=8,color='black')
  labels.append({'band':xv,'position_mm':p.tolist(),'height_milli':z})
 letter(fig,3,24,'a',H)
 # Exterior to the back/top edge, with space for title and tick labels.
 cax=axes_mm(fig,166,42,1.8,24,H);cb=fig.colorbar(ScalarMappable(norm=NORM,cmap=CD),cax=cax,orientation='vertical',extend='both',ticks=[-10,0,8])
 cb.ax.tick_params(labelsize=8,length=2,pad=1);cb.outline.set_linewidth(.6)
 fig.text(166.9/W,1-37/H,r'ΔAbs ($10^{-3}$)',ha='center',va='center',fontsize=8)
 fig.text(166.9/W,1-32.5/H,'ref. 1.2 V',ha='center',va='center',fontsize=8)
 bcheck=stack(fig,x,D,E,H)
 fig.canvas.draw()
 renderer=fig.canvas.get_renderer()
 from matplotlib.text import Text
 font_audit=[{'text':t.get_text(),'family':t.get_fontfamily(),'pt':t.get_fontsize(),'weight':t.get_fontweight()} for t in fig.findobj(Text) if t.get_visible() and t.get_text()]
 assert all(t['family']==['Arial'] and t['pt'] in (8,10) for t in font_audit),font_audit
 (OUT/'FONT_AUDIT.json').write_text(json.dumps(font_audit,ensure_ascii=False,indent=2),encoding='utf-8')
 title_box=e_title.get_window_extent(renderer)
 for tick in e_tick_texts:
  assert not title_box.overlaps(tick.get_window_extent(renderer)), 'E title and tick labels overlap'
 # Drawn alignment includes final labels, colorbar and b panels.
 final=np.array([project_mm(fig,ax,v,E.max(),floor) for v in (3650,1000)])
 assert np.max(abs(errors))<.02
 filename=f'Figure_4_{STAMP}_{name}'
 export(fig,filename,preview);plt.close(fig)
 return {'name':name,'file_stem':filename,'elev':elev,'azim':azim,'projection':'perspective, focal_length=1.6','box_aspect':[3.8,depth,zheight],'zoom':zoom,'canvas_mm':[W,H],'floor_milli':floor,'top_milli':top,'full_surface_minmax_milli':[float(Z.min()),float(Z.max())],'surface_array_SHA256':sha(Z),'floor_surface_same_values':True,'norm_limits_milli':[-10,8],'accent_only_below_milli':-7.4,'accent_surface_fraction':float(np.mean(Z < -7.4)),'purple_endpoint':'#8f8bc0','color_saturation_fraction':float(np.mean(abs(Z)>8)),'measured_E_line_count':0,'measured_E_node_count':13,'b_line_width_pt':1.15,'surface_display_E_rows':len(eg),'E_interpolation_original_node_max_error':0,'front_axis_endpoints_mm':final.tolist(),'b_outer_edges_mm':[13,RIGHT],'alignment_error_mm':errors.tolist(),'alignment_basis':'entire projected box outermost lines, all eight corners','front_axis_vertical_difference_mm':float(final[1,1]-final[0,1]),'minimum_floor_to_surface_screen_gap_mm':float(min(gaps)),'feature_labels':labels,'b':bcheck,'SI_baseline_applied':False}

def si_figures(x,A,E,preview):
 results=[]
 fig=plt.figure(figsize=(W/25.4,82/25.4),facecolor='white')
 checks=stack(fig,x,A*1000,E,82,top=13,height=54,raw=True,panel=False)
 filename=f'Figure_S_raw_regions_{STAMP}';export(fig,filename,preview);plt.close(fig)
 results.append({'file_stem':filename,'type':'original instrument absorbance, three windows; display smoothing only','checks':checks})
 H=105;fig=plt.figure(figsize=(W/25.4,H/25.4),facecolor='white');ax=axes_mm(fig,13,7,148,83,H)
 m=(x>=1000)&(x<=4000);Y=savgol_filter(A*1000,21,2,axis=1)[:,m]
 step=max(8.,float(np.max(Y[1:]-Y[:-1]))+1.5);YY=Y-np.arange(13)[:,None]*step
 assert float(np.min(YY[:-1]-YY[1:]))>=1.5-1e-12
 for k in range(13):ax.plot(x[m],YY[k],lw=.8,color=CE(1-k/12))
 lo,hi=float(YY.min()),float(YY.max());span=hi-lo;ax.set_ylim(lo-.04*span,hi+.12*span)
 ax.set_xlim(4000,1000);ax.set_yticks([]);ax.xaxis.set_major_locator(MultipleLocator(500));ax.xaxis.set_minor_locator(MultipleLocator(100));ax.set_xlabel(r'Wavenumber (cm$^{-1}$)');ax.set_ylabel('Absorbance')
 bar=20.;xb=1150.;yb=hi+.04*span;ax.set_ylim(lo-.04*span,yb+bar+.04*span);ax.plot([xb,xb],[yb,yb+bar],color='#404040',lw=1.35);ax.text(xb+90,yb+bar/2,r'20 × 10$^{-3}$',ha='right',va='center')
 ga=axes_mm(fig,166,17,2.5,57,H);ga.imshow(np.linspace(0,1,256)[:,None],origin='lower',aspect='auto',cmap=CE);ga.set_axis_off()
 fig.text(168/W,1-12/H,'1.22 V',ha='center');fig.text(168/W,1-80/H,'−0.08 V',ha='center')
 filename=f'Figure_S_raw_full_{STAMP}';export(fig,filename,preview);plt.close(fig)
 results.append({'file_stem':filename,'type':'original instrument absorbance, 1000–4000; display SG21 only','step_milli':step,'min_adjacent_gap':float(np.min(YY[:-1]-YY[1:])),'E_order_top_to_bottom':'high to low','scale_bar_absorbance':.02,'input_raw_array_SHA256':sha(A)})
 return results

def run():
 ap=argparse.ArgumentParser();ap.add_argument('--preview-only',action='store_true');ap.add_argument('--only',choices=['V1','V2','V3','SI','all'],default='all');args=ap.parse_args()
 x,A,R,D,E,checks=prepare()
 # Preserve complete check records when exporting one variant at a time.
 p=OUT/'CHECKS.json'
 if p.exists():
  old=json.loads(p.read_text(encoding='utf8'));checks['variants']=old.get('variants',[]);checks['SI']=old.get('SI',[])
 for v in VARIANTS:
  if args.only not in ('all',v[0]):continue
  rec=main_figure(x,D,E,v,args.preview_only);checks['variants']=[r for r in checks['variants'] if r['name']!=v[0]]+[rec]
  p.write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 if args.only in ('all','SI'):checks['SI']=si_figures(x,A,E,args.preview_only)
 assert sha(A)==checks['array_SHA256']['instrument_absorbance']
 for name,h in checks['source_SHA256'].items():assert hashlib.sha256((DATA/name).read_bytes()).hexdigest()==h
 p.write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('DONE source hashes unchanged; baseline checks match; graphics checks passed.',flush=True)

if __name__=='__main__':run()
