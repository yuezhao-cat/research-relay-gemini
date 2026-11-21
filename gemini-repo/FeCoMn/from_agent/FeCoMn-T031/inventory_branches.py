"""Read-only first-stage inventory. No job submissions or remote mutations."""
from pathlib import Path
import subprocess,json,csv
HERE=Path(__file__).resolve().parent
CODE=r'''
import os,pathlib,re,json
home=pathlib.Path.home();is_imr='05926' in str(home)
root=pathlib.Path('/home/05926/zhaoyue/WORK') if is_imr else home
roots=[p for p in root.iterdir() if p.is_dir() and (p.name.startswith('FeCoMn') or p.name.startswith('FCM_'))]
rows=[]
target=re.compile(r'(MnNC|FCM|S_FeCoMnNC59|OH_original|OH_outplane)',re.I)
for top in roots:
 for dp,dn,fn in os.walk(str(top)):
  dn[:]=[n for n in dn if not any(s in n.lower() for s in ['frequency','cdd','postprocess','lobster','bader','adsorbate','substrate','particle','support'])]
  p=pathlib.Path(dp)
  if 'OUTCAR' not in fn or 'INCAR' not in fn or not target.search(p.name):continue
  if not any(t in p.name for t in ['MnNC','FCM_Mn_','FCM_cov8O','FCM_bg8O_MnOH','FCMnew','S_FeCoMnNC59','FCM_8O','OH_original','OH_outplane']):continue
  inc={}
  for l in (p/'INCAR').read_text(errors='replace').splitlines():
   l=l.split('#')[0].split('!')[0]
   if '=' in l:
    k,v=l.split('=',1);inc[k.strip().upper()]=v.strip()
  if inc.get('IBRION') in ['5','6','7','8']:continue
  with (p/'OUTCAR').open('rb') as f:
   f.seek(0,2);sz=f.tell();f.seek(max(0,sz-800000));o=f.read().decode(errors='replace')
  energy=re.findall(r'energy\(sigma->0\)\s*=\s*([-+\d.]+)',o)
  cp=p/'CONTCAR'
  if not cp.exists() or not cp.stat().st_size:cp=p/'POSCAR'
  if not cp.exists():continue
  ls=cp.read_text(errors='replace').splitlines()
  try:
   es=ls[5].split();ns=list(map(int,ls[6].split()));els=[e for e,n in zip(es,ns) for _ in range(n)];mi=els.index('Mn')+1
  except:continue
  block=o.split('magnetization (x)')[-1] if 'magnetization (x)' in o else '';moms={}
  for l in block.splitlines():
   t=l.split()
   if len(t)>=5 and t[0].isdigit():moms[int(t[0])]=float(t[-1])
   if len(t)>=5 and t[0]=='tot':break
  osi=(p/'OSZICAR').read_text(errors='replace')[-4000:] if (p/'OSZICAR').exists() else '';mag=re.findall(r'mag=\s*([-+\d.]+)',osi)
  k=7
  if ls[k].lower().startswith('s'):k+=1
  mode=ls[k];k+=1
  rows.append(dict(path=str(p),name=p.name,energy_sigma0=float(energy[-1]) if energy else None,normal_end='Elapsed time (sec)' in o,ionic_converged='reached required accuracy' in o,electronic_converged=('EDIFF is reached' in o or 'aborting loop because EDIFF' in o),composition=dict(zip(es,ns)),cell=[[float(x)*float(ls[1]) for x in ls[i].split()[:3]] for i in [2,3,4]],elements=els,coordinate_mode=mode,coordinates=[[float(x) for x in l.split()[:3]] for l in ls[k:k+sum(ns)]],settings=inc,Mn_index=mi,Mn_local_moment=moms.get(mi),particle_sum_moment=sum(moms.get(i+1,0) for i,e in enumerate(els) if e in ['Fe','Co']) if moms else None,total_moment=float(mag[-1]) if mag else None))
print(json.dumps(rows))
'''
allrows=[]
for host in ['imr','genkai']:
 r=subprocess.run(['ssh',host,'python3','-'],input=CODE,text=True,capture_output=True)
 if r.returncode:raise RuntimeError(r.stderr)
 rows=json.loads(r.stdout)
 for x in rows:x['machine']=host
 (HERE/(host+'_branches.json')).write_text(json.dumps(rows,indent=2),encoding='utf-8')
 allrows+=rows
 print(host,len(rows),'candidate calculations')
with (HERE/'branch_inventory.csv').open('w',encoding='utf-8-sig',newline='') as f:
 keys=['machine','path','energy_sigma0','normal_end','ionic_converged','Mn_local_moment','particle_sum_moment','total_moment','composition','NSW','initial_MAGMOM']
 w=csv.DictWriter(f,fieldnames=keys,lineterminator='\n');w.writeheader()
 for x in allrows:
  row={k:x.get(k) for k in keys};row['composition']=json.dumps(x['composition']);row['NSW']=x['settings'].get('NSW');row['initial_MAGMOM']=x['settings'].get('MAGMOM');w.writerow(row)
