"""Read-only provenance trace. No new VASP, LOBSTER or Bader calculation."""
from pathlib import Path
import json,subprocess
HERE=Path(__file__).parent/'MnNC_source_trace_20261118'
HERE.mkdir(exist_ok=True)
CODE=r'''
from pathlib import Path
import json,re,hashlib,numpy as np
imr='05926' in str(Path.home());R=Path('/home/05926/zhaoyue/WORK') if imr else Path.home()
paths=['FeCoMn_ch5_recalc_20261007/MnNC_O_MnNbri','FeCoMn_electronic_20261023/MnNC_base_full','FeCoMn_COHP_20261023/MnNC_base_full','FeCoMn_COHP_20261023/MnNC_base_full/lobster_post_v2_20261024'] if imr else ['FeCoMn_electronic_20261023/MnNC_base_full']
rows=[]
for q in paths:
 p=R/q;v=dict(path=str(p));o=(p/'OUTCAR').read_text(errors='replace') if (p/'OUTCAR').exists() else ''
 for key,pattern in [('energy_sigma0',r'energy\(sigma->0\)\s*=\s*([-+\d.]+)'),('NBANDS_actual',r'NBANDS\s*=\s*(\d+)'),('NELECT',r'NELECT\s*=\s*([-+\d.]+)')]:
  a=re.findall(pattern,o);v[key]=float(a[-1]) if a else None
 osz=(p/'OSZICAR').read_text(errors='replace') if (p/'OSZICAR').exists() else '';a=re.findall(r'mag=\s*([-+\d.]+)',osz);v['total_moment']=float(a[-1]) if a else None
 if 'magnetization (x)' in o:
  for l in o.split('magnetization (x)')[-1].splitlines():
   z=l.split()
   if len(z)>=5 and z[0]=='179':v['Mn179_moment']=float(z[-1])
   if z and z[0]=='tot':break
 v['normal_end']='Elapsed time (sec)' in o;v['EDIFF_reached']='aborting loop because EDIFF is reached' in o
 v['vasp_version']=o.splitlines()[0] if o else None;v['files']={};v['INCAR']=(p/'INCAR').read_text() if (p/'INCAR').exists() else None
 for n in ['POSCAR','CONTCAR','POTCAR','KPOINTS','WAVECAR','CHGCAR','AECCAR0','AECCAR2','DOSCAR','COHPCAR.lobster','ICOHPLIST.lobster','ACF.dat']:
  f=p/n
  if not f.exists():v['files'][n]=dict(exists=False);continue
  z=dict(exists=True,size=f.stat().st_size,symlink=f.is_symlink(),resolved=str(f.resolve()))
  if f.stat().st_size and n in ['POSCAR','CONTCAR','POTCAR','KPOINTS']:
   b=f.read_bytes();z['sha256']=hashlib.sha256(b).hexdigest()
   if n=='POTCAR':z['token_sha256']=hashlib.sha256(b' '.join(b.split())).hexdigest();z['TITEL']=re.findall(r'TITEL[^\n]*',b.decode(errors='replace'))
  v['files'][n]=z
 for n in ['migration.json','submission.json','submission_cohp.json','execution_result.json','lobsterin']:
  f=p/n
  if f.exists():v[n]=f.read_text(errors='replace')
 p2=p/'bader_validated_20261024';a=p2/'ACF.dat'
 if a.exists():
  qvals={}
  for l in a.read_text().splitlines():
   z=l.split()
   if len(z)>=7 and z[0].isdigit():qvals[int(z[0])]=float(z[4])
  v['Bader']=dict(path=str(a),Mn_electrons=qvals.get(179),valence_electron_sum=sum(qvals.values()))
 dos=p/'DOSCAR'
 if dos.exists() and dos.stat().st_size>10000 and 'FeCoMn_ch5_recalc' not in q:
  with dos.open() as h:
   for _ in range(5):next(h)
   head=next(h).split();n=int(head[2]);ef=float(head[3])
   for _ in range(n):next(h)
   for _ in range(179):
    next(h);block=[next(h) for _ in range(n)]
  arr=np.array([list(map(float,l.split())) for l in block]);e=arr[:,0]-ef;w=(e>=-8)&(e<=0);d=arr[:,9:19].sum(axis=1)
  v['DOS_occupied_d_center_eV']=float(np.trapz(e[w]*d[w],e[w])/np.trapz(d[w],e[w]));v['DOS_window_eV']=[-8,0]
 # Read the CHGCAR/AECCAR grid header only, not multi-GB density values.
 for n in ['CHGCAR','AECCAR0','AECCAR2']:
  f=p/n
  if f.exists() and f.stat().st_size:
   try:
    with f.open() as h:
     head=[next(h) for _ in range(7)];ns=sum(map(int,head[6].split()));line=next(h)
     if line.lower().startswith('s'):line=next(h)
     for _ in range(ns):next(h)
     line=next(h)
     while not line.strip():line=next(h)
     v['files'][n]['grid']=list(map(int,line.split()))
   except Exception as ex:v['files'][n]['grid_error']=str(ex)
 rows.append(v)
# Explicit check of previously invalidated v1 curve export against raw total bond.
if imr:
 p=R/'FeCoMn_COHP_20261023/MnNC_base_full/lobster_post_v2_20261024';f=p/'COHPCAR.lobster'
 with f.open() as h:
  next(h);meta=next(h).split();nb=int(meta[0]);nsp=int(meta[1]);labels=[next(h).strip() for _ in range(nb)];a=np.loadtxt(h)
 c=[i for i,l in enumerate(labels) if re.search(r'Mn179->O180\(',l) and '[' not in l][0]
 cols=[1+s*2*nb+2*c for s in range(nsp)];ico=[i+1 for i in cols];ix=int(np.abs(a[:,0]).argmin())
 f2=R/'FeCoMn_COHP_20261023/cohp_curves_20261024/MnNC_base_full__Mn179-O180.csv';b=np.loadtxt(f2,delimiter=',',skiprows=1)
 jj=np.array([int(np.abs(a[:,0]-e).argmin()) for e in b[:,0]])
 cmp=dict(raw=str(f),old_csv=str(f2),raw_rows=len(a),old_csv_rows=len(b),nbonds_declared=nb,matched_label=labels[c],zero_based_column=c,cohp_columns=cols,integral_columns=ico,energy_nearest_zero=float(a[ix,0]),integral_at_nearest_zero=-float(a[ix,ico].sum()),missing_raw_rows=[int(i) for i in range(len(a)) if i not in set(jj)],max_export_energy_error=float(np.abs(a[jj,0]-b[:,0]).max()),max_export_curve_error=float(np.abs(a[jj][:,cols]-b[:,1:3]).max()))
 rows.append(dict(curve_export_validation=cmp,verified_curve=np.column_stack([a[:,0],a[:,cols],-a[:,cols].sum(axis=1),-a[:,ico].sum(axis=1)]).tolist()))
print(json.dumps(rows))
'''
for host in ['genkai','imr']:
 r=subprocess.run(['ssh',host,'python3','-'],input=CODE,text=True,capture_output=True,check=True)
 d=json.loads(r.stdout)
 for x in d:
  if 'verified_curve' in x:
   import csv
   with (HERE/'MnNC_axial_COHP_raw_verified_20261118.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['E_minus_EF_eV','pCOHP_spin1','pCOHP_spin2','minus_pCOHP_spin_sum','minus_integrated_COHP_grid']);w.writerows(x.pop('verified_curve'))
 (HERE/(host+'_provenance.json')).write_text(json.dumps(d,indent=2),encoding='utf8')
 for x in d:
  if 'path' in x:print(host,x['path'],x.get('energy_sigma0'),x.get('Mn179_moment'),x.get('total_moment'),x.get('NBANDS_actual'),x.get('Bader'))
  else:print(x)
