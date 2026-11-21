"""Read existing files only; do not run VASP, LOBSTER or Bader."""
from pathlib import Path
import subprocess,json
OUT=Path(__file__).resolve().parent
REMOTE=r'''
import pathlib,json,re,math
root=pathlib.Path('/home/pj25000114/ku50002299')
rows=[]
for family,folder,prefix in [('no_axial_OH','FeCoMn_electronic_20261023','FCM'),('axial_OH','FeCoMn_MnOH_electronic_v2_20261031','FCMnew')]:
 for state in ['base','OOH','O','OH']:
  p=root/folder/(prefix+'_'+state+'_full')
  pos=p/'CONTCAR'
  if not pos.exists() or not pos.stat().st_size:pos=p/'POSCAR'
  if not pos.exists():
   rows.append(dict(family=family,state=state,path=str(p),missing=True));continue
  ls=pos.read_text().splitlines();es=ls[5].split();ns=list(map(int,ls[6].split()));comp=dict(zip(es,ns))
  cell=[[float(x)*float(ls[1]) for x in ls[i].split()[:3]] for i in [2,3,4]]
  k=7
  if ls[k].lower().startswith('s'):k+=1
  direct=ls[k].lower().startswith('d');k+=1
  coords=[list(map(float,l.split()[:3])) for l in ls[k:k+sum(ns)]]
  els=[e for e,n in zip(es,ns) for _ in range(n)]
  def distance(a,b):
   v=[coords[a][i]-coords[b][i] for i in range(3)]
   if direct:
    v=[x-round(x) for x in v];v=[sum(v[j]*cell[j][i] for j in range(3)) for i in range(3)]
   return math.sqrt(sum(x*x for x in v))
  mi=els.index('Mn');near=[dict(atom=i+1,element=e,d_A=distance(mi,i)) for i,e in enumerate(els) if e=='O' and distance(mi,i)<2.5]
  out=(p/'OUTCAR').read_text(errors='replace') if (p/'OUTCAR').exists() else ''
  ener=re.findall(r'energy\(sigma->0\)\s*=\s*([-+\d.]+)',out)
  inc=(p/'INCAR').read_text(errors='replace');settings={}
  for line in inc.splitlines():
   line=line.split('#')[0].split('!')[0]
   if '=' in line:
    a,b=line.split('=',1);settings[a.strip().upper()]=b.strip()
  row=dict(family=family,state=state,path=str(p),composition=comp,cell=cell,Mn_index=mi+1,nearby_O=near,normal_end='Elapsed time (sec)' in out,energy_sigma0=ener[-1] if ener else None,settings=settings,files={f:(p/f).stat().st_size if (p/f).exists() else 0 for f in ['DOSCAR','vasprun.xml','CHGCAR','AECCAR0','AECCAR2','WAVECAR']})
  acf=(root/'FeCoMn_MnOH_postprocess_20261031'/'bader'/p.name/'ACF.dat') if family=='axial_OH' else p/'bader_validated_20261024'/'ACF.dat'
  row['ACF_path']=str(acf);row['ACF_exists']=acf.exists()
  if acf.exists():
   ar=[]
   for line in acf.read_text().splitlines():
    t=line.split()
    if len(t)>=7 and t[0].isdigit():ar.append((int(t[0]),float(t[4])))
   q=dict(ar);row['Mn_Bader_electrons']=q.get(mi+1);row['Bader_sum']=sum(q.values());row['Bader_count']=len(q)
  pp=(root/'FeCoMn_MnOH_postprocess_corrected_20261031'/'results'/'pdos'/(p.name+'.json.gz')) if family=='axial_OH' else root/'FeCoMn_electronic_20261023'/'postprocess_20261023'/(p.name+'.json')
  row['PDOS_processed_path']=str(pp);row['PDOS_processed_exists']=pp.exists()
  cp=(root/'FeCoMn_MnOH_postprocess_corrected_20261031'/'cohp'/p.name) if family=='axial_OH' else root/'FeCoMn_COHP_20261023'/p.name/'lobster_post_v2_20261024'
  row['COHP_path']=str(cp);row['COHP_files']={f:(cp/f).stat().st_size if (cp/f).exists() else 0 for f in ['COHPCAR.lobster','ICOHPLIST.lobster','lobsterout']}
  ico=cp/'ICOHPLIST.lobster';bonds=[]
  if ico.exists():
   for line in ico.read_text().splitlines():
    t=line.split()
    if len(t)>=9 and t[0].isdigit() and '_' not in t[1]+t[2] and t[4:7]==['0','0','0'] and ('Mn'+str(mi+1)) in t[1:3]:
     bonds.append(dict(atom1=t[1],atom2=t[2],distance=float(t[3]),minus_ICOHP=-sum(map(float,t[7:9]))))
  row['Mn_bonds']=bonds
  lo=cp/'lobsterout'
  if lo.exists():row['lobster_quality_lines']=[l.strip() for l in lo.read_text().splitlines() if 'spilling' in l.lower() or 'finished' in l.lower()]
  rows.append(row)
print(json.dumps(rows))
'''
r=subprocess.run(['ssh','genkai','python3','-'],input=REMOTE,capture_output=True,text=True,check=True)
rows=json.loads(r.stdout)
(OUT/'remote_manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
for r in rows:
 print(r['family'],r['state'],r.get('composition'),r.get('normal_end'),'PDOS',r.get('PDOS_processed_exists'),'ACF',r.get('ACF_exists'),'COHP',r.get('COHP_files'))
 print('MnO',r.get('nearby_O'),'MnBader',r.get('Mn_Bader_electrons'),'bonds',r.get('Mn_bonds'))
