"""Read selected existing calculations. No remote file writes or DFT jobs."""
from pathlib import Path
import subprocess,json
HERE=Path(__file__).resolve().parent
CODE=r'''
from pathlib import Path
import json,re,numpy as np,gzip
R=Path.home(); imr='05926' in str(R)
if imr:R=Path('/home/05926/zhaoyue/WORK')
trap=getattr(np,'trapezoid',np.trapz)
def get(p,kind,state):
 out={'path':str(p),'family':kind,'state':state}
 if not (p/'OUTCAR').exists():return dict(out,missing=True)
 t=(p/'OUTCAR').read_text(errors='replace');c=p/'CONTCAR'
 if not c.exists() or not c.stat().st_size:c=p/'POSCAR'
 ls=c.read_text().splitlines();sp=ls[5].split();ct=list(map(int,ls[6].split()));els=[e for e,n in zip(sp,ct) for _ in range(n)];mi=els.index('Mn');k=7
 if ls[k].lower().startswith('s'):k+=1
 direct=ls[k].lower().startswith('d');k+=1
 cell=np.array([list(map(float,l.split()[:3])) for l in ls[2:5]])*float(ls[1]);xyz=np.array([list(map(float,l.split()[:3])) for l in ls[k:k+sum(ct)]])
 if not direct:xyz=xyz@np.linalg.inv(cell)
 delta=xyz-xyz[mi];delta-=np.rint(delta);cart=delta@cell
 ns=sorted([i for i,e in enumerate(els) if e=='N'],key=lambda i:np.linalg.norm(cart[i]))[:4]
 nn=cart[ns];mean=nn.mean(axis=0);normal=np.linalg.svd(nn-mean)[2][-1]
 if normal[2]<0:normal=-normal
 no=[i for i,e in enumerate(els) if e=='O' and np.linalg.norm(cart[i])<2.7]
 moment={}
 if 'magnetization (x)' in t:
  for l in t.split('magnetization (x)')[-1].splitlines():
   z=l.split()
   if len(z)>=5 and z[0].isdigit():moment[int(z[0])]=float(z[-1])
   if z and z[0]=='tot':break
 ens=re.findall(r'energy\(sigma->0\)\s*=\s*([-+\d.]+)',t)
 osz=(p/'OSZICAR').read_text() if (p/'OSZICAR').exists() else '';mags=re.findall(r'mag=\s*([-+\d.]+)',osz)
 inc=(p/'INCAR').read_text() if (p/'INCAR').exists() else ''
 out.update(composition=dict(zip(sp,ct)),Mn_index=mi+1,energy_sigma0=float(ens[-1]) if ens else None,normal_end='Elapsed time (sec)' in t,ionic_converged='reached required accuracy' in t,Mn_moment=moment.get(mi+1),total_moment=float(mags[-1]) if mags else None,INCAR=inc,Mn_N_distances_A=[float(np.linalg.norm(x)) for x in nn],Mn_N_mean_A=float(np.linalg.norm(nn,axis=1).mean()),Mn_height_signed_A=float(-mean@normal),local_z_angle_deg=float(np.degrees(np.arccos(np.clip(normal[2],-1,1)))),nearby_O=[dict(index=i+1,distance_A=float(np.linalg.norm(cart[i])),height_relative_Mn_A=float(cart[i]@normal),moment=moment.get(i+1)) for i in no])
 f=p/'DOSCAR'
 if f.exists() and f.stat().st_size:
  try:
   with f.open() as h:
    for _ in range(5):next(h)
    head=next(h).split();n=int(head[2]);ef=float(head[3])
    for _ in range(n):next(h)
    for ai in range(mi+1):
     next(h);block=[next(h) for _ in range(n)]
   a=np.array([list(map(float,l.split())) for l in block]);E=a[:,0]-ef
   if a.shape[1]<19:raise ValueError('not orbital resolved spin DOS')
   up=a[:,13];dn=a[:,14];y=up+dn;w=(E>=-8)&(E<=0);z=(E>=-.25)&(E<=.25)
   mass=trap(y[w],E[w]);out['dz2']=dict(path=str(f),fermi_eV=ef,columns=a.shape[1],window_eV=[-8,0],integral= float(mass),center_eV=float(trap(E[w]*y[w],E[w])/mass),spin_difference_integral=float(trap((up-dn)[w],E[w])),EF_pm025_mean_DOS=float(trap(y[z],E[z])/(E[z][-1]-E[z][0])),d_center_eV=float(trap(E[w]*a[w,9:19].sum(axis=1),E[w])/trap(a[w,9:19].sum(axis=1),E[w])))
  except Exception as ex:out['DOS_error']=str(ex)
 return out
rows=[]
if not imr:
 for fam,folder,prefix in [('8O_noOH','FeCoMn_electronic_20261023','FCM'),('8O_OH','FeCoMn_MnOH_electronic_v2_20261031','FCMnew'),('MnNC_O','FeCoMn_electronic_20261023','MnNC')]:
  for state in ['base','OOH','O','OH']:rows.append(get(R/folder/(prefix+'_'+state+'_full'),fam,state))
 rows.append(get(R/'FeCoMn_MnOH_O_magnetic_wavecheck_20261031','8O_OH_wave_continuation','O'))
 for state in ['OOH','O','OH']:
  rows.append(get(R/'FeCoMn_ch5_ORR_real_coverage_20261017/jobs'/('MnNC_cov1O_'+state),'MnNC_O_relax',state))
 # Existing original relaxations, kept distinct from static electronic analyses.
 for state in ['base','OOH','O','OH']:
  name='FCM_bg8O_MnOH' if state=='base' else 'FCM_bg8O_MnOH_'+state
  rows.append(get(R/'FeCoMn_ORR_MnOHbackground_20261030'/name,'8O_OH_relax',state))
else:
 root=R/'FeCoMn_ch5_recalc_20261007'
 groups={'MnNC_bare':['MnNC_clean','MnNC_OOH','MnNC_O','MnNC_OH'],'MnNC_OH':['MnNC_OH','MnNC_OOH_OHb','MnNC_O_OH','MnNC_OH_OH'],'FCM_bare':['S_FeCoMnNC59_clean','FCM_Mn_OOH','FCM_Mn_O','FCM_Mn_OH'],'FCM_OH':['FCM_Mn_OHb','FCM_Mn_OOH_OHb','FCM_Mn_O_OHb','FCM_Mn_OH_OHb']}
 for fam,names in groups.items():
  for state,name in zip(['base','OOH','O','OH'],names):rows.append(get(root/name,fam,state))
print(json.dumps(rows))
'''
for host in ['genkai','imr']:
 r=subprocess.run(['ssh',host,'python3','-'],input=CODE,text=True,capture_output=True,check=True)
 d=json.loads(r.stdout);(HERE/(host+'_selected_outputs.json')).write_text(json.dumps(d,indent=2),encoding='utf-8')
 for x in d:print(host,x['family'],x['state'],x.get('Mn_moment'),x.get('Mn_height_signed_A'),x.get('dz2',{}).get('center_eV'),x.get('DOS_error',''))
