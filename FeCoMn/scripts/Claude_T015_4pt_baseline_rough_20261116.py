import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSC, TwoSlopeNorm
from matplotlib.cm import ScalarMappable
from scipy.signal import savgol_filter as sg
S='/tmp/claude-0/-home-claude/1325c35c-b0d4-5247-b4f1-988064e4fe83/scratchpad'
A=np.load(S+'/ana/A.npy');x=np.load(S+'/ana/x.npy');E=np.load(S+'/ana/E.npy')
anch=[(1330,1370),(1900,1950),(2550,2650),(3850,3950)]
def blk(y):
    px=[x[(x>=a)&(x<=b)].mean() for a,b in anch]; py=[y[(x>=a)&(x<=b)].mean() for a,b in anch]
    return y-np.interp(x,px,py)
R=np.array([blk(a) for a in A]); R=R-R[0]
CE=LSC.from_list('E',['#8f8bc0','#b6b3d6','#d6d1d1','#f1a0a6','#eb687b'])
CD=LSC.from_list('D',['#5b4fa0','#8f8bc0','#d0cce5','#ffffff','#f6bcc4','#eb687b','#d6304a'])
plt.rcParams.update({'font.family':'Liberation Sans','font.size':8,'axes.linewidth':0.8,'xtick.direction':'out','ytick.direction':'out'})
fig=plt.figure(figsize=(7.1,9.6))
# ---- a
ax=fig.add_axes([0.0,0.63,1.0,0.37],projection='3d')
m=(x>=1000)&(x<=3650); xs=x[m]; Z=np.array([sg(r,41,2) for r in R])[:,m]
Eg=np.linspace(E.min(),E.max(),90)
Zi=np.array([np.interp(Eg,E[::-1],Z[::-1,j]) for j in range(Z.shape[1])]).T
X,Y=np.meshgrid(xs,Eg); v=10; nz=TwoSlopeNorm(0,-v,v); zf=-48
ax.contourf(X,Y,np.clip(Zi,-v,v),zdir='z',offset=zf,levels=np.linspace(-v,v,81),cmap=CD,norm=nz)
ax.plot_surface(X,Y,Zi,facecolors=CD(nz(np.clip(Zi,-v,v))),rstride=1,cstride=3,linewidth=0,shade=False,antialiased=False,rasterized=True)
for k in range(13): ax.plot(xs,np.full_like(xs,E[k]),Z[k],color='#555555',lw=0.3,alpha=0.5)
ax.set_xlim(3650,1000); ax.set_ylim(E.max(),E.min()); ax.set_zlim(zf,14)
ax.set_box_aspect((3.8,2.2,1.6),zoom=1.0); ax.view_init(elev=24,azim=-90); ax.set_proj_type('ortho')
ax.set_xticks([3500,3000,2500,2000,1500,1000]); ax.set_yticks([0,0.4,0.8,1.2]); ax.set_zticks([-10,0,10])
ax.set_xlabel('Wavenumber (cm$^{-1}$)',labelpad=4); ax.set_ylabel('$E$ (V vs. RHE)',labelpad=4); ax.set_zlabel('ΔAbs (10$^{-3}$)',labelpad=2)
for a in (ax.xaxis,ax.yaxis,ax.zaxis): a.pane.fill=False; a.pane.set_edgecolor('#cccccc')
ax.grid(False)
from mpl_toolkits.mplot3d import proj3d
L0,R0=0.08,0.86
z=1.0
for it in range(12):
    ax.set_box_aspect((3.8,2.2,1.6),zoom=z); fig.canvas.draw()
    P=[]
    for xv in (3650,1000):
        xp,yp,_=proj3d.proj_transform(xv,E.min(),zf,ax.get_proj()); P.append(fig.transFigure.inverted().transform(ax.transData.transform((xp,yp)))[0])
    z*= (R0-L0)/(P[1]-P[0])
    pos=ax.get_position(); ax.set_position([pos.x0+(L0-P[0]) if it>3 else pos.x0,pos.y0,pos.width,pos.height])
print('aligned',P)
cax=fig.add_axes([0.80,0.955,0.15,0.008]); cb=fig.colorbar(ScalarMappable(nz,CD),cax=cax,orientation='horizontal',extend='both',ticks=[-10,0,10])
cb.set_label('ΔAbs (10$^{-3}$), ref. 1.21 V',fontsize=7,labelpad=2); cax.xaxis.set_label_position('top')
# ---- b
segs=[(3650,2750,'ν(O–H)',2.0,21,0.005),(1720,1570,'δ(H–O–H)',1.0,41,0.0025),(1330,1175,'1215 cm$^{-1}$ region',1.0,21,0.0025)]
wid=[430,300,430]; L,Rr,B0,T0=0.08,0.86,0.36,0.57; gap=0.012; span=Rr-L-2*gap; xl=L; axb=[]
for (hi,lo,t,sc,w,sbv),wd in zip(segs,wid):
    ww=span*wd/sum(wid); a=fig.add_axes([xl,B0,ww,T0-B0]); xl+=ww+gap; axb.append(a)
    mm=(x>=lo)&(x<=hi); Ys=np.array([sg(r,w,2) for r in R])[:,mm]/sc
    step=2.6 if lo==1175 else 1.6
    for k in range(13): a.plot(x[mm],Ys[k]-k*step,color=CE(1-k/12),lw=0.9)
    a.set_xlim(hi,lo); a.set_yticks([]); a.set_title(t,fontsize=8)
    yl=a.get_ylim(); a.set_ylim(yl[0],yl[1]+1.5)
    xb=hi-(hi-lo)*0.30; yt=yl[1]+1.2; a.plot([xb,xb],[yt-sbv*1e3/sc,yt],color='#404040',lw=1.3)
    a.text(xb-(hi-lo)*0.03,yt-sbv*1e3/sc/2,f'{sbv:g} a.u.',ha='left',va='center',fontsize=7)
axb[0].set_ylabel('ΔAbsorbance (a.u.)'); fig.text((L+Rr)/2,B0-0.035,'Wavenumber (cm$^{-1}$)',ha='center')
axb[0].set_xticks([3600,3400,3200,3000,2800]); axb[1].set_xticks([1700,1650,1600]); axb[2].set_xticks([1300,1250,1200])
g=fig.add_axes([0.905,B0+0.02,0.012,T0-B0-0.06]); g.imshow(np.linspace(0,1,256)[:,None],origin='lower',aspect='auto',cmap=CE); g.set_axis_off()
fig.text(0.911,T0-0.03,'1.21 V',ha='center',fontsize=7); fig.text(0.911,B0+0.0,'−0.09 V',ha='center',fontsize=7)
# ---- c-e
Eg2=np.linspace(E.min(),E.max(),400); xl=L; B1,T1=0.05,0.25
for j,((hi,lo,t,sc,w,sbv),wd,lim,c0) in enumerate(zip(segs,wid,[10,4,10],[3307,1633,1215])):
    ww=span*wd/sum(wid); a=fig.add_axes([xl,B1,ww,T1-B1]); 
    mm=(x>=lo)&(x<=hi); Zm=np.array([sg(r,w,2) for r in R])[:,mm]
    Zg=np.array([np.interp(Eg2,E[::-1],Zm[::-1,q]) for q in range(Zm.shape[1])]).T
    cmap2=LSC.from_list('D2',['#8f8bc0','#d0cce5','#ffffff','#f6bcc4','#eb687b'])
    im=a.imshow(Zg,origin='lower',aspect='auto',extent=[x[mm][0],x[mm][-1],E.min(),E.max()],cmap=cmap2,norm=TwoSlopeNorm(0,-lim,lim),interpolation='bilinear')
    a.set_xlim(hi,lo); a.axvline(c0,ls=(0,(3,2)),color='#404040',lw=0.6)
    a.set_xlabel('Wavenumber (cm$^{-1}$)')
    if j==0: a.set_ylabel('$E$ (V vs. RHE)')
    else: a.set_yticklabels([])
    a.set_xticks(axb[j].get_xticks())
    ca=fig.add_axes([xl,T1+0.03,ww,0.008]); cb=fig.colorbar(im,cax=ca,orientation='horizontal',ticks=[-lim,0,lim]); ca.xaxis.set_ticks_position('top')
    if j==0: fig.text(xl,T1+0.06,'ΔAbs (10$^{-3}$), ref. 1.21 V',fontsize=7)
    fig.text(xl-0.01 if j else xl-0.06,T1+0.012,'cde'[j],fontweight='bold',fontsize=10)
    xl+=ww+gap
fig.text(0.01,0.985,'a',fontweight='bold',fontsize=10); fig.text(0.01,0.59,'b',fontweight='bold',fontsize=10)
fig.savefig(S+'/f15/Figure4_4pt_baseline_preview.png',dpi=200)
