"""Read the 13 specified IMR calculations without changing remote files."""
import csv
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REMOTE = r'''
import hashlib, json, pathlib, re
root=pathlib.Path('/home/05926/zhaoyue/WORK/FeCoMn_ch5_recalc_20261007')
names=['FeCoMnNC59_clean','FeCoNC59_clean','MnNC_clean',
 'FCM_Mn_OOH','FCM_Mn_O','FCM_Mn_OH',
 'FCM_Mn_OHb','FCM_Mn_OOH_OHb','FCM_Mn_O_OHb','FCM_Mn_OH_OHb',
 'MnNC_OOH','MnNC_O','MnNC_OH','S_FeCoMnNC59_clean']
def composition(p):
 if not p.exists() or p.stat().st_size==0:return ''
 ls=p.read_text(errors='replace').splitlines()
 if len(ls)<7:return ''
 es=ls[5].split(); ns=ls[6].split()
 return ''.join(e+n for e,n in zip(es,ns))
def sha(p):
 if not p.exists() or p.stat().st_size==0:return ''
 return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for name in names:
 p=root/name
 out=(p/'OUTCAR').read_text(errors='replace') if (p/'OUTCAR').exists() else ''
 m=re.findall(r'energy\(sigma->0\)\s*=\s*([-+\d.]+)',out)
 rows.append(dict(machine='IMR',name=name,path=str(p),
  energy_sigma0=m[-1] if m else '',normal_end='Elapsed time (sec)' in out,
  ionic_converged='reached required accuracy' in out,
  POSCAR_composition=composition(p/'POSCAR'),CONTCAR_composition=composition(p/'CONTCAR'),
  CONTCAR_sha256=sha(p/'CONTCAR'),INCAR_sha256=sha(p/'INCAR')))
print(json.dumps(rows))
'''

result = subprocess.run(['ssh', 'imr', 'python3', '-'], input=REMOTE,
                        capture_output=True, text=True, check=True)
rows = json.loads(result.stdout)
fields = list(rows[0])
with (HERE / 'manifest.csv').open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)
for row in rows:
    print(row['name'], row['energy_sigma0'], row['CONTCAR_composition'],
          row['normal_end'], row['ionic_converged'])
