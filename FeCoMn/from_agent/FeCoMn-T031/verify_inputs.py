from pathlib import Path
import json,subprocess
HERE=Path(__file__).resolve().parent
for host in ['imr','genkai']:
 rows=json.loads((HERE/(host+'_composition_inventory.json')).read_text())
 paths=[x['path'] for x in rows if 'error' not in x]
 code='import json,pathlib,hashlib\npaths=json.loads('+repr(json.dumps(paths))+')\n'
 code+=r'''
out=[]
for name in paths:
 p=pathlib.Path(name);pot=p/'POTCAR';row=dict(path=name)
 if pot.exists():row['POTCAR_token_sha256']=hashlib.sha256(b' '.join(pot.read_bytes().split())).hexdigest()
 ps=p/'POSCAR'
 if ps.exists() and ps.stat().st_size:
  ls=ps.read_text().splitlines()
  try:
   es=ls[5].split();ns=list(map(int,ls[6].split()));k=7
   if ls[k].lower().startswith('s'):k+=1
   mode=ls[k];k+=1
   row['POSCAR_composition']=dict(zip(es,ns));row['POSCAR_mode']=mode;row['POSCAR_coordinates']=[[float(x) for x in l.split()[:3]] for l in ls[k:k+sum(ns)]]
  except:pass
 out.append(row)
print(json.dumps(out))
'''
 r=subprocess.run(['ssh',host,'python3','-'],input=code,text=True,capture_output=True,check=True)
 (HERE/(host+'_input_checks.json')).write_text(r.stdout,encoding='utf-8')
 print(host,'verified inputs',len(json.loads(r.stdout)),flush=True)
