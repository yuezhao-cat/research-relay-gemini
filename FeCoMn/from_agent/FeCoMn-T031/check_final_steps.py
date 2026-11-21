from pathlib import Path
import subprocess,json
HERE=Path(__file__).resolve().parent
summary=json.loads((HERE/'comparison_24.json').read_text())
for host in ['imr','genkai']:
 paths=list(dict.fromkeys(x['best']['path'] for x in summary if x.get('best') and x['best']['machine']==host))
 code='import pathlib,re,json\npaths=json.loads('+repr(json.dumps(paths))+')\n'
 code+=r'''
rows=[]
for name in paths:
 p=pathlib.Path(name);osi=(p/'OSZICAR').read_text(errors='replace')[-20000:]
 steps=re.findall(r'^\s*(?:DAV|RMM|CG)\s*:\s*(\d+)',osi,re.M)
 with (p/'OUTCAR').open('rb') as f:
  f.seek(0,2);z=f.tell();f.seek(max(0,z-900000));o=f.read().decode(errors='replace')
 force=[]
 if 'TOTAL-FORCE (eV/Angst)' in o:
  for l in o.split('TOTAL-FORCE (eV/Angst)')[-1].splitlines()[1:]:
   t=l.split()
   if len(t)==6:
    try:force.append([float(v) for v in t[3:]])
    except:pass
   elif force:break
 rows.append(dict(path=name,last_electronic_iterations=int(steps[-1]) if steps else None,last_OSZICAR_lines=osi.splitlines()[-4:],final_forces=force))
print(json.dumps(rows))
'''
 r=subprocess.run(['ssh',host,'python3','-'],input=code,text=True,capture_output=True,check=True)
 (HERE/(host+'_selected_final_checks.json')).write_text(r.stdout,encoding='utf-8')
 print(host,'final steps checked',len(paths))
