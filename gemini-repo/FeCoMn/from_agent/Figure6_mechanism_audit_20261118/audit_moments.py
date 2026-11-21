from pathlib import Path
import subprocess,json
HERE=Path(__file__).resolve().parent
CODE=r'''
import pathlib,re,json,hashlib,math
R=pathlib.Path('/home/pj25000114/ku50002299')
jobs=[]
for fam,folder,prefix in [('noOH','FeCoMn_electronic_20261023','FCM'),('OH','FeCoMn_MnOH_electronic_v2_20261031','FCMnew')]:
 for s in ['base','OOH','O','OH']:jobs.append((fam,s,R/folder/(prefix+'_'+s+'_full')))
for s in ['OOH','O']:jobs.append(('noOH_cohp',s,R/'FeCoMn_COHP_20261023'/('FCM_'+s+'_full')/'lobster_post_v2_20261024'))
rows=[]
for fam,s,p in jobs:
 o=(p/'OUTCAR').read_text(errors='replace');ls=(p/'POSCAR').read_text().splitlines();es=ls[5].split();ns=list(map(int,ls[6].split()));els=[e for e,n in zip(es,ns) for _ in range(n)];mi=els.index('Mn')+1
 blocks=o.split('magnetization (x)');moment=None;mtotal=None
 if len(blocks)>1:
  for l in blocks[-1].splitlines()[1:]:
   t=l.split()
   if len(t)>=5 and t[0].isdigit() and int(t[0])==mi:moment=float(t[-1])
   if len(t)>=5 and t[0]=='tot':mtotal=float(t[-1]);break
 osz=(p/'OSZICAR').read_text(errors='replace') if (p/'OSZICAR').exists() else ''
 mags=re.findall(r'mag=\s*([-+\d.]+)',osz)
 energy=re.findall(r'energy\(sigma->0\)\s*=\s*([-+\d.]+)',o)
 inc={}
 for l in (p/'INCAR').read_text().splitlines():
  l=l.split('#')[0].split('!')[0]
  if '=' in l:
   k,v=l.split('=',1);inc[k.strip().upper()]=v.strip()
 def structure(file):
  l=file.read_text().splitlines();k=7
  if l[k].lower().startswith('s'):k+=1
  k+=1
  return [[float(x) for x in line.split()[:3]] for line in l[k:k+sum(ns)]]
 coords=structure(p/'POSCAR')
 acf=None
 if fam=='OH':acf=R/'FeCoMn_MnOH_postprocess_20261031/bader'/p.name/'ACF.dat'
 elif fam=='noOH':acf=p/('bader_format_test_v2_20261024' if s=='base' else 'bader_validated_20261024')/'ACF.dat'
 q={}
 if acf and acf.exists():
  for l in acf.read_text().splitlines():
   t=l.split()
   if len(t)>=7 and t[0].isdigit():q[int(t[0])]=float(t[4])
 # Reaction-side indices are different from retained axial OH indices.
 ads={'OOH':([247,248,249] if fam=='noOH' else [248,249,251]),'O':([247] if fam=='noOH' else [248]),'OH':([247,248] if fam=='noOH' else [248,250])}.get(s,[])
 val={'O':6,'H':1}
 excess=sum(q[i]-val[els[i-1]] for i in ads) if q and ads else None
 rows.append(dict(family=fam,state=s,path=str(p),Mn_index=mi,Mn_local_moment=moment,OUTCAR_sphere_sum_moment=mtotal,total_moment_OSZICAR=float(mags[-1]) if mags else None,energy_sigma0=float(energy[-1]),normal_end='Elapsed time (sec)' in o,settings=inc,coordinates_fractional=coords,composition=dict(zip(es,ns)),Mn_Bader_electrons=q.get(mi),adsorbate_electron_excess=excess,adsorbate_indices=ads,ACF=str(acf) if acf else None))
print(json.dumps(rows))
'''
r=subprocess.run(['ssh','genkai','python3','-'],input=CODE,text=True,capture_output=True,check=True)
rows=json.loads(r.stdout)
(HERE/'moments_and_charge_manifest.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
for x in rows:print(x['family'],x['state'],'Mn moment',x['Mn_local_moment'],'total',x['total_moment_OSZICAR'],'Mn electrons',x['Mn_Bader_electrons'],'ads excess',x['adsorbate_electron_excess'])
