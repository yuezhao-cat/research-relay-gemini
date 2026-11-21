from pathlib import Path
import subprocess,json,csv,numpy as np
HERE=Path(__file__).resolve().parent
code=r'''
import pathlib,json,re
r=pathlib.Path('/home/05926/zhaoyue/WORK/FeCoMn_ch5_recalc_20261007');rows=[]
for n in ['MnNC_OH','MnNC_OOH_OHb','MnNC_O_OH','MnNC_OH_OH','FCM_Mn_OHb','MnNC_clean']:
 p=r/n;ls=(p/'CONTCAR').read_text().splitlines();es=ls[5].split();ns=list(map(int,ls[6].split()));k=7
 if ls[k].lower().startswith('s'):k+=1
 k+=1
 out=(p/'OUTCAR').read_text(errors='replace');inc={}
 for l in (p/'INCAR').read_text().splitlines():
  l=l.split('#')[0].split('!')[0]
  if '=' in l:
   a,b=l.split('=',1);inc[a.strip().upper()]=b.strip()
 rows.append(dict(name=n,path=str(p),composition=dict(zip(es,ns)),elements=[e for e,c in zip(es,ns) for _ in range(c)],cell=[[float(x)*float(ls[1]) for x in ls[i].split()[:3]] for i in [2,3,4]],fractional=[[float(x) for x in l.split()[:3]] for l in ls[k:k+sum(ns)]],energy=float(re.findall(r'energy\(sigma->0\)\s*=\s*([-+\d.]+)',out)[-1]),normal_end='Elapsed time (sec)' in out,ionic_converged='reached required accuracy' in out,settings=inc))
print(json.dumps(rows))
'''
r=subprocess.run(['ssh','imr','python3','-'],input=code,text=True,capture_output=True,check=True);rows=json.loads(r.stdout)
for x in rows[:4]:
 f=np.array(x['fractional']);cell=np.array(x['cell']);es=x['elements'];mi=es.index('Mn');v=f-f[mi];v-=np.round(v);v=v@cell
 ni=sorted([i for i,e in enumerate(es) if e=='N'],key=lambda i:np.linalg.norm(v[i]))[:4];n=v[ni];center=n.mean(axis=0);normal=np.linalg.svd(n-center)[2][-1]
 if normal[2]<0:normal=-normal
 x['Mn_N4_plane_distance']=float(-center@normal)
 x['O_geometry']=[dict(atom=i+1,Mn_O_distance=float(np.linalg.norm(v[i])),O_signed_plane_position=float((v[i]-center)@normal),O_signed_relative_Mn=float(v[i]@normal),nearest_H_distance=float(min(np.linalg.norm(((f[h]-f[i])-np.round(f[h]-f[i]))@cell) for h,e in enumerate(es) if e=='H'))) for i,e in enumerate(es) if e=='O']
keys=['ENCUT','GGA','IVDW','ISPIN','ISMEAR','SIGMA','EDIFF','EDIFFG']
for x in rows[:4]:
 x['settings_match_C_D']=all(all(x['settings'].get(k)==ref['settings'].get(k) for k in keys) and np.allclose(x['cell'],ref['cell']) for ref in rows[4:])
(HERE/'manifest.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
with (HERE/'manifest.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,lineterminator='\n');w.writerow(['name','path','energy_sigma0','normal_end','ionic_converged','composition','cell','settings_match_C_D','O_geometry'])
 for x in rows[:4]:w.writerow([x['name'],x['path'],x['energy'],x['normal_end'],x['ionic_converged'],json.dumps(x['composition']),json.dumps(x['cell']),x['settings_match_C_D'],json.dumps(x['O_geometry'])])
ener=[x['energy'] for x in rows[:4]];b,a,o,h=ener;H=-6.833;W=-14.327;g=[a-b-2*W+1.5*H+.403,o-b-W+H+.066,h-b-W+.5*H+.343];steps=[g[0]-4.92,g[1]-g[0],g[2]-g[1],-g[2]]
print('All settings pass',all(x['settings_match_C_D'] for x in rows[:4]));print('G',g,'steps',steps,'UL',-max(steps),'eta',1.23+max(steps))
for x in rows[:4]:print(x['name'],x['O_geometry'])
