import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSC, TwoSlopeNorm
from scipy.signal import savgol_filter as sg
S='/tmp/claude-0/-home-claude/1325c35c-b0d4-5247-b4f1-988064e4fe83/scratchpad'
A=np.load(S+'/ana/A.npy');x=np.load(S+'/ana/x.npy');E=np.load(S+'/ana/E.npy')
B=np.array([sg(a,21,2) for a in A])
CMD=LSC.from_list('D',['#8f8bc0','#d0cce5','#ffffff','#f6bcc4','#eb687b'])
plt.rcParams.update({'font.family':'Liberation Sans','font.size':8})
fig=plt.figure(figsize=(11,4.2))
for i,lo in enumerate([650,1000]):
    ax=fig.add_subplot(1,2,i+1,projection='3d')
    m=x>=lo; xs=x[m][::6]; Z=B[:,m][:,::6]
    Eg=np.linspace(E.min(),E.max(),50)
    Zi=np.array([np.interp(Eg,E[::-1],Z[::-1,j]) for j in range(Z.shape[1])]).T
    X,Y=np.meshgrid(xs,Eg); v=np.abs(Zi).max(); nz=TwoSlopeNorm(0,-v,v); zf=Zi.min()-0.8*(Zi.max()-Zi.min())
    ax.contourf(X,Y,Zi,zdir='z',offset=zf,levels=80,cmap=CMD,norm=nz)
    ax.plot_surface(X,Y,Zi,facecolors=CMD(nz(Zi)),rstride=1,cstride=1,linewidth=0,shade=False)
    for k in range(13): ax.plot(xs,np.full_like(xs,E[k]),Z[k],color='#606060',lw=0.3,alpha=0.6)
    ax.set_xlim(4000,lo); ax.set_ylim(1.25,-0.12); ax.set_zlim(zf,Zi.max())
    ax.set_box_aspect((3,1.4,1.0)); ax.view_init(elev=22,azim=-62)
    ax.set_xticks([4000,3000,2000,1000]); ax.set_yticks([1.2,0.8,0.4,0.0])
    ax.set_xlabel('Wavenumber (cm$^{-1}$)'); ax.set_ylabel('E (V vs. RHE)'); ax.set_zlabel('Absorbance (10$^{-3}$)')
    ax.set_title(f'raw, {lo}–4000',y=0.95)
    for a in (ax.xaxis,ax.yaxis,ax.zaxis): a.pane.fill=False; a.pane.set_edgecolor('#cccccc')
    ax.grid(False)
fig.subplots_adjust(0,0,1,1,wspace=0); fig.savefig(S+'/f3d2/a_full_raw_whitecentre.png',dpi=200)
