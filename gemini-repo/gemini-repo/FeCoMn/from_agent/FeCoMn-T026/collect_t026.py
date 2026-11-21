"""Read only: T026 calculations on IMR, writing a local manifest."""
import csv
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REMOTE = r'''
import json,pathlib,re,hashlib
root=pathlib.Path('/home/05926/zhaoyue/WORK/FeCoMn_ch5_recalc_20261007')
names=['S_FeCoMnNC59_clean','FCM_Mn_OOH','FCM_Mn_O','FCM_Mn_OH',
 'FCM_Mn_OHb','FCM_Mn_OOH_OHb','FCM_Mn_O_OHb','FCM_Mn_OH_OHb',
 'MnNC_clean','MnNC_OOH','MnNC_O','MnNC_OH',
 'coverage_6O7O_20261014/FCM_Mn2O','coverage_6O7O_20261014/FCM_Mn2OH',
 'coverage_6O7O_20261014/FCM_4O_MnO','coverage_6O7O_20261014/FCM_4O_MnOH',
 'coverage_final_20261011/FCM_5O_MnO','coverage_final_20261011/FCM_5O_MnOH',
 'coverage_6O7O_20261014/FCM_6O_MnO','coverage_6O7O_20261014/FCM_6O_MnOH',
 'rich8O_joint_20261014/FCM_8O_MnO','rich8O_joint_20261014/FCM_8O_MnOH']
def poscar(p):
 if not p.exists() or p.stat().st_size==0:return {},'', '', '', ''
 ls=p.read_text(errors='replace').splitlines()
 if len(ls)<8:return {},'', '', '', ''
 es=ls[5].split(); ns=list(map(int,ls[6].split())); comp=dict(zip(es,ns))
 scale=float(ls[1].split()[0]);cell=[[round(float(x)*scale,8) for x in ls[i].split()[:3]] for i in (2,3,4)]
 k=7; selective=ls[k].lower().startswith('s')
 if selective:k+=1
 k+=1
 frozen=0;partial=0
 for line in ls[k:k+sum(ns)]:
  tok=line.split()
  if len(tok)>=6:
   flags=[v.upper() for v in tok[3:6]]
   if flags==['F','F','F']:frozen+=1
   elif 'F' in flags:partial+=1
 return comp,json.dumps(cell,separators=(',',':')),str(frozen),str(partial),str(selective)
rows=[]
for name in names:
 p=root/name
 out=(p/'OUTCAR').read_text(errors='replace') if (p/'OUTCAR').exists() else ''
 m=re.findall(r'energy\(sigma->0\)\s*=\s*([-+\d.]+)',out)
 comp,cell,frozen,partial,selective=poscar(p/'CONTCAR')
 inc=(p/'INCAR').read_text(errors='replace') if (p/'INCAR').exists() else ''
 settings={}
 for line in inc.splitlines():
  line=line.split('#')[0].split('!')[0]
  if '=' in line:
   key,val=line.split('=',1);settings[key.strip().upper()]=val.strip()
 pot=(p/'POTCAR').read_bytes() if (p/'POTCAR').exists() else b''
 titles=re.findall(rb'TITEL\s*=\s*([^\n]+)',pot)
 row=dict(machine='IMR',name=name,path=str(p),energy_sigma0=m[-1] if m else '',
  normal_end=str('Elapsed time (sec)' in out),ionic_converged=str('reached required accuracy' in out),
  CONTCAR_composition=json.dumps(comp,separators=(',',':')),cell_A=cell,
  frozen_atoms=frozen,partially_fixed_atoms=partial,selective_dynamics=selective,
  INCAR_settings=json.dumps(settings,separators=(',',':')),
  KPOINTS_sha256=hashlib.sha256((p/'KPOINTS').read_bytes()).hexdigest() if (p/'KPOINTS').exists() else '',
  POTCAR_titles='|'.join(x.decode(errors='replace').strip() for x in titles))
 rows.append(row)
print(json.dumps(rows))
'''
r = subprocess.run(['ssh', 'imr', 'python3', '-'], input=REMOTE,
                   capture_output=True, text=True, check=True)
rows = json.loads(r.stdout)
with (HERE/'manifest.csv').open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]))
    writer.writeheader();writer.writerows(rows)
for x in rows:
    print(x['name'],x['energy_sigma0'],x['CONTCAR_composition'],
          x['normal_end'],x['ionic_converged'],x['frozen_atoms'])
