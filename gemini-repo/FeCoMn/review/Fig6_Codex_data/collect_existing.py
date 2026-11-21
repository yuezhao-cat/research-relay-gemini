"""Read existing outputs requested in the Fig6 discussion; no jobs or plots."""
from pathlib import Path
import subprocess,json,csv
HERE=Path(__file__).resolve().parent
CODE=r'''
import pathlib,json,re,gzip,math
home=pathlib.Path.home();imr='05926' in str(home);root=pathlib.Path('/home/05926/zhaoyue/WORK') if imr else home
def charges(p):
 q={}
 if p.exists():
  for l in p.read_text().splitlines():
   t=l.split()
   if len(t)>=7 and t[0].isdigit():q[int(t[0])]=float(t[4])
 return q
def raw(p,atoms):
 out=(p/'OUTCAR').read_text(errors='replace') if (p/'OUTCAR').exists() else ''
 en=re.findall(r'energy\(sigma->0\)\s*=\s*([-+\d.]+)',out);moms={}
 if 'magnetization (x)' in out:
  for l in out.split('magnetization (x)')[-1].splitlines():
   t=l.split()
   if len(t)>=5 and t[0].isdigit():moms[int(t[0])]=float(t[-1])
   if len(t)>=5 and t[0]=='tot':break
 cp=p/'CONTCAR'
 if not cp.exists() or not cp.stat().st_size:cp=p/'POSCAR'
 info={}
 if cp.exists():
  ls=cp.read_text().splitlines();es=ls[5].split();ns=list(map(int,ls[6].split()));info['composition']=dict(zip(es,ns));k=7
  if ls[k].lower().startswith('s'):k+=1
  k+=1;coords=[list(map(float,l.split()[:3])) for l in ls[k:k+sum(ns)]];cell=[[float(x)*float(ls[1]) for x in ls[i].split()[:3]] for i in [2,3,4]]
  def dist(i,j):
   v=[coords[i-1][a]-coords[j-1][a] for a in range(3)];v=[x-round(x) for x in v];v=[sum(v[a]*cell[a][b] for a in range(3)) for b in range(3)];return math.sqrt(sum(x*x for x in v))
  info['requested_distances']={str(i)+'-'+str(j):dist(i,j) for i in atoms for j in atoms if i<j}
 return dict(path=str(p),energy_sigma0=float(en[-1]) if en else None,normal_end='Elapsed time (sec)' in out,magnetic_moments={str(i):moms.get(i) for i in atoms},**info)
def ico(p):
 f=p/'ICOHPLIST.lobster';bonds=[]
 if f.exists():
  for l in f.read_text().splitlines():
   t=l.split()
   if len(t)>=9 and t[0].isdigit() and '_' not in t[1]+t[2] and t[4:7]==['0','0','0']:
    bonds.append(dict(atom1=t[1],atom2=t[2],distance_A=float(t[3]),minus_ICOHP_eV=-sum(map(float,t[7:9]))))
 return dict(path=str(p),files={n:(p/n).stat().st_size if (p/n).exists() else 0 for n in ['COHPCAR.lobster','ICOHPLIST.lobster','lobsterout']},bonds=bonds)
result={}
if not imr:
 p=root/'FeCoMn_MnOH_electronic_v2_20261031/FCMnew_base_full';acf=root/'FeCoMn_MnOH_postprocess_20261031/bader/FCMnew_base_full/ACF.dat';q=charges(acf)
 result['FCM_background']=dict(raw(p,[238,247,248]),ACF_path=str(acf),Bader_electrons={str(i):q.get(i) for i in [238,247,248]},cohp=ico(root/'FeCoMn_MnOH_postprocess_corrected_20261031/cohp/FCMnew_base_full'))
 p=root/'FeCoMn_electronic_20261023/MnNC_base_full';acf=p/'bader_validated_20261024/ACF.dat';q=charges(acf)
 result['MnNC_background']=dict(raw(p,[179,180]),ACF_path=str(acf),Bader_electrons={str(i):q.get(i) for i in [179,180]})
 base=root/'FeCoMn_FCN_restart_check_20261024/fcn_lowspin_post_20261025/bader/ACF.dat';q0=charges(base);result['FCN_Bader_base']=dict(path=str(base),electrons={str(i):q0.get(i) for i in [206,234,235]})
 for s,ids in [('OOH',[206,235]),('O',[206,234])]:
  p=root/'FeCoMn_electronic_20261023'/('FCN_'+s+'_full');acf=p/'bader_validated_20261024/ACF.dat';q=charges(acf)
  result['FCN_'+s]=dict(raw(p,ids+[248]),ACF_path=str(acf),Bader_electrons={str(i):q.get(i) for i in ids},Bader_delta_electrons={str(i):q.get(i,0)-q0.get(i,0) for i in ids},cohp=ico(root/'FeCoMn_COHP_20261023'/p.name/'lobster_post_v2_20261024'))
 for model,path in [('FCM',root/'FeCoMn_MnOH_postprocess_corrected_20261031/results/pdos/FCMnew_O_full.json.gz'),('FCN',root/'FeCoMn_electronic_20261023/site_pdos_20261024/FCN_O_full.json.gz'),('MnNC',root/'FeCoMn_electronic_20261023/site_pdos_20261024/MnNC_O_full.json.gz')]:
  d=json.loads(gzip.open(path,'rt').read()) if path.exists() else {}
  result[model+'_O_PDOS']=dict(path=str(path),size=path.stat().st_size if path.exists() else 0,keys=list(d.keys()),selection=d.get('selection'),atom_keys=list(d.get('atoms',{}).keys()) if isinstance(d.get('atoms'),dict) else None)
 result['FCM_O_COHP']=ico(root/'FeCoMn_MnOH_postprocess_corrected_20261031/cohp/FCMnew_O_full')
 result['MnNC_O_COHP']=ico(root/'FeCoMn_COHP_20261023/MnNC_O_full/lobster_post_v2_20261024')
else:
 result['MnNC_background_COHP']=ico(root/'FeCoMn_COHP_20261023/MnNC_base_full/lobster_post_v2_20261024')
 result['MnNC_background_COHP_meta']=raw(root/'FeCoMn_COHP_20261023/MnNC_base_full/lobster_post_v2_20261024',[179,180])
 p=root/'FeCoMn_electronic_20261023/FCN_OH_full';acf=p/'bader_validated_20261024/ACF.dat';q=charges(acf)
 result['FCN_OH']=dict(raw(p,[206,234,235,248]),ACF_path=str(acf),Bader_electrons={str(i):q.get(i) for i in [206,234,235]},cohp=ico(root/'FeCoMn_COHP_20261023/FCN_OH_full/lobster_post_v2_20261024'))
print(json.dumps(result))
'''
all_data={}
for host in ['genkai','imr']:
 r=subprocess.run(['ssh',host,'python3','-'],input=CODE,text=True,capture_output=True)
 if r.returncode:raise RuntimeError(r.stderr)
 data=json.loads(r.stdout)
 (HERE/(host+'_existing_outputs.json')).write_text(json.dumps(data,indent=2),encoding='utf-8')
 all_data.update(data)
base=all_data['FCN_Bader_base']['electrons']
for i,v in all_data['FCN_OH']['Bader_electrons'].items():all_data['FCN_OH'].setdefault('Bader_delta_electrons',{})[i]=v-base[i]
(HERE/'combined.json').write_text(json.dumps(all_data,indent=2),encoding='utf-8')
for name in ['FCM_background','MnNC_background']:
 d=all_data[name];print(name,'electrons',d['Bader_electrons'],'moments',d['magnetic_moments'],'dist',d['requested_distances'])
for name in ['FCN_OOH','FCN_O','FCN_OH']:
 d=all_data[name];print(name,'electrons',d['Bader_electrons'],'delta',d['Bader_delta_electrons'])
 print([x for x in d['cohp']['bonds'] if 'O248' in [x['atom1'],x['atom2']] and any(x['atom1']==e+str(i) or x['atom2']==e+str(i) for e,i in [('Fe',206),('Co',234),('Co',235)])])
