import sys,os,numpy as np,matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSC
from matplotlib.patches import FancyArrow
from scipy.signal import savgol_filter
D=sys.argv[1]; OUT=sys.argv[2]
plt.rcParams.update({'font.family':'Liberation Sans','font.size':8,'xtick.direction':'in','ytick.direction':'in','axes.unicode_minus':True,'axes.linewidth':0.8,'xtick.major.width':0.8})
INK='#404040'
fs=['0.2','0.1','0','-0.1','-0.2','-0.3','-0.4','-0.5','-0.6','-0.7','-0.8','-0.9','-11']
E=np.array([(-1.1 if f=='-11' else float(f))+1.011 for f in fs])
def load(p):
    a=np.genfromtxt(p,delimiter=','); a=a[~np.isnan(a[:,1])]; return a[np.argsort(a[:,0])]
def bl(x,y):
    w1=(x>=1330)&(x<=1370); w2=(x>=1900)&(x<=1950); x1,y1,x2,y2=x[w1].mean(),y[w1].mean(),x[w2].mean(),y[w2].mean(); return y-(y1+(y2-y1)*(x-x1)/(x2-x1))
raw=[]
for f in fs: a=load(os.path.join(D,f+'.CSV')); x=a[:,0]; raw.append(bl(x,a[:,1])*1e3)
raw=np.array(raw)
CM=LSC.from_list('E',['#8f8bc0','#b6b3d6','#d6d1d1','#f1a0a6','#eb687b']); col=lambda k: CM(1-k/12)
#            hi    lo   scale  SG  title                 width
segs=[(3650,2750,4.0,21,'ν(O–H)',430),
      (1720,1570,1.0,41,'δ(H–O–H)',300),
      (1330,1175,1.0,21,'1215 cm$^{-1}$ region',430)]
step=1.6
fig=plt.figure(figsize=(7.0,4.4))
L,Rr,B,T=0.075,0.84,0.13,0.90; gap=0.014; span=Rr-L-2*gap; xl=L; axs=[]
tops=[]
for i,(hi,lo,sc,sg,t,w) in enumerate(segs):
    ww=span*w/sum(s[5] for s in segs); ax=fig.add_axes([xl,B,ww,T-B]); xl+=ww+gap; axs.append(ax)
    m=(x>=lo)&(x<=hi); Y=np.array([savgol_filter(r,sg,2) for r in raw])/sc
    Y=Y-np.median(Y[:,m][:, :15],axis=1,keepdims=True)*0  # keep raw relative levels
    Ys=np.array([Y[k,m]-k*step for k in range(13)]); lo_y,hi_y=Ys.min(),Ys.max(); pad=(hi_y-lo_y)*0.06
    for k in range(13): ax.plot(x[m],Ys[k],color=col(k),lw=1.2,solid_capstyle='round')
    top=hi_y+pad+ (hi_y-lo_y)*0.12
    ax.set_xlim(hi,lo); ax.set_yticks([]); ax.set_ylim(lo_y-pad,top)
    ax.text(0.5,1.025,t,transform=ax.transAxes,ha='center',va='bottom',fontsize=8.5,color=INK)
    # scale bar, top-right corner
    sb=10.0 if sc>1 else 2.5; xb=lo+(hi-lo)*0.10
    ax.plot([xb,xb],[top-pad-sb/sc,top-pad],color=INK,lw=1.2)
    ax.text(xb+(hi-lo)*0.03,top-pad-sb/sc/2,f'{sb/1000:g}',fontsize=7,va='center',ha='right',color=INK)
for i,ax in enumerate(axs):
    d=0.018
    for yy in (0,1):
        if i<2: ax.plot([1-d,1+d],[yy-0.012,yy+0.012],transform=ax.transAxes,color='k',lw=.8,clip_on=False)
        if i>0: ax.plot([-d,d],[yy-0.012,yy+0.012],transform=ax.transAxes,color='k',lw=.8,clip_on=False)
axs[0].set_xticks([3600,3400,3200,3000,2800]); axs[1].set_xticks([1700,1650,1600]); axs[2].set_xticks([1300,1250,1200])
axs[0].set_ylabel('Absorbance (a.u.)',color=INK)
fig.text((L+Rr)/2,0.035,'Wavenumber (cm$^{-1}$)',ha='center',color=INK)
# gradient arrow with selected labels
cax=fig.add_axes([Rr+0.035,B+0.06,0.018,T-B-0.12])
g=np.linspace(1,0,256)[:,None]; cax.imshow(g,aspect='auto',cmap=CM,extent=[0,1,0,1]); cax.set_axis_off()
fig.patches.append(FancyArrow(Rr+0.044,B+0.06,0,-0.045,width=0.012,head_width=0.03,head_length=0.03,length_includes_head=True,transform=fig.transFigure,color='#8f8bc0',lw=0))
for e in (1.21,0.91,0.71,-0.09):
    yy=B+0.06+(T-B-0.12)*(e-E.min())/(E.max()-E.min())
    fig.text(Rr+0.06,yy,f'{e:.2f} V'.replace('-','−'),fontsize=7,va='center',color=INK)
    fig.lines.append(plt.Line2D([Rr+0.053,Rr+0.057],[yy,yy],transform=fig.transFigure,color=INK,lw=.8))
plt.savefig(OUT,dpi=240)
