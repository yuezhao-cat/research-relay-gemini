"""Exhaustive existing-result screening by composition, not directory names."""
from pathlib import Path
import subprocess,json,csv
HERE=Path(__file__).resolve().parent
CODE=r'''
import pathlib,os,re,json,hashlib
home=pathlib.Path.home();root=pathlib.Path('/home/05926/zhaoyue/WORK') if '05926' in str(home) else home
rows=[]
prune={'.git','.cache','.local','node_modules','site-packages','vasp.6.3.2','vasp.6.4.2','vasp.6.5.0'}
for dp,dn,fn in os.walk(str(root)):
 dn[:]=[n for n in dn if n not in prune and not n.startswith('.')]
 if 'OUTCAR' not in fn or 'INCAR' not in fn:continue
 p=pathlib.Path(dp);cp=p/'CONTCAR'
 if not cp.exists() or not cp.stat().st_size:cp=p/'POSCAR'
 if not cp.exists():continue
 try:
  ls=cp.read_text(errors='replace').splitlines();es=ls[5].split();ns=list(map(int,ls[6].split()));comp=dict(zip(es,ns))
  if comp.get('C')!=174 or comp.get('N')!=4 or comp.get('Mn')!=1:continue
  if comp.get('Fe',0) not in [0,27] or comp.get('Co',0) not in [0,32]:continue
  if bool(comp.get('Fe'))!=bool(comp.get('Co')):continue
  if set(comp)-set(['C','N','Mn','Fe','Co','O','H']) or comp.get('O',0)>11 or comp.get('H',0)>2:continue
  inc={}
  for l in (p/'INCAR').read_text(errors='replace').splitlines():
   l=l.split('#')[0].split('!')[0]
   if '=' in l:
    k,v=l.split('=',1);inc[k.strip().upper()]=v.strip()
  with (p/'OUTCAR').open('rb') as f:
   f.seek(0,2);z=f.tell();f.seek(max(0,z-900000));o=f.read().decode(errors='replace')
  en=re.findall(r'energy\(sigma->0\)\s*=\s*([-+\d.]+)',o)
  if not en:continue
  els=[e for e,n in zip(es,ns) for _ in range(n)];mi=els.index('Mn')+1;k=7
  selective=ls[k].lower().startswith('s')
  if selective:k+=1
  mode=ls[k];k+=1;cr=ls[k:k+sum(ns)];frozen=[i+1 for i,l in enumerate(cr) if len(l.split())>=6 and [x.upper() for x in l.split()[3:6]]==['F','F','F']]
  moms={}
  if 'magnetization (x)' in o:
   for l in o.split('magnetization (x)')[-1].splitlines():
    t=l.split()
    if len(t)>=5 and t[0].isdigit():moms[int(t[0])]=float(t[-1])
    if len(t)>=5 and t[0]=='tot':break
  osi=(p/'OSZICAR').read_text(errors='replace')[-6000:] if (p/'OSZICAR').exists() else '';m=re.findall(r'mag=\s*([-+\d.]+)',osi)
  init=[]
  for tok in inc.get('MAGMOM','').split():
   try:
    if '*' in tok:
     n,v=tok.split('*');init.extend([float(v)]*int(n))
    else:init.append(float(tok))
   except:pass
  kind='static' if inc.get('NSW','0')=='0' or inc.get('IBRION')=='-1' else ('frequency' if inc.get('IBRION') in ['5','6','7','8'] else 'relax')
  kp=(p/'KPOINTS').read_text(errors='replace') if (p/'KPOINTS').exists() else ''
  pot=(p/'POTCAR').read_text(errors='replace') if (p/'POTCAR').exists() else ''
  rows.append(dict(path=str(p),name=p.name,kind=kind,composition=comp,elements=els,coordinates=[[float(x) for x in l.split()[:3]] for l in cr],coordinate_mode=mode,cell=[[float(x)*float(ls[1]) for x in ls[i].split()[:3]] for i in [2,3,4]],frozen_indices=frozen,energy_sigma0=float(en[-1]),normal_end='Elapsed time (sec)' in o,ionic_converged='reached required accuracy' in o,electronic_converged='EDIFF is reached' in o,settings=inc,initial_Mn_moment=init[mi-1] if len(init)>=mi else None,Mn_local_moment=moms.get(mi),particle_sum_moment=sum(moms.get(i+1,0) for i,e in enumerate(els) if e in ['Fe','Co']) if moms else None,total_moment=float(m[-1]) if m else None,KPOINTS=kp,POTCAR_titles=re.findall(r'TITEL\s*=\s*([^\n]+)',pot)))
 except Exception as e:
  rows.append(dict(path=str(p),error=str(e)))
print(json.dumps(rows))
'''
for host in ['imr','genkai']:
 r=subprocess.run(['ssh',host,'python3','-'],input=CODE,text=True,capture_output=True)
 if r.returncode:raise RuntimeError(r.stderr)
 rows=json.loads(r.stdout)
 for x in rows:x['machine']=host
 (HERE/(host+'_composition_inventory.json')).write_text(json.dumps(rows,indent=2),encoding='utf-8')
 print(host,len(rows),'composition-matched records',flush=True)
