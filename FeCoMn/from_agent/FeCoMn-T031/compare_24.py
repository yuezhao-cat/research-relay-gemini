"""Merge existing branches; distinguish topology and numerical settings."""
from pathlib import Path
import json,csv,numpy as np
HERE=Path(__file__).resolve().parent
rows=[]
for host in ['imr','genkai']:rows+=json.loads((HERE/(host+'_composition_inventory.json')).read_text())
rows=[x for x in rows if 'error' not in x]
inputs={}
for host in ['imr','genkai']:
 for z in json.loads((HERE/(host+'_input_checks.json')).read_text()):inputs[z['path']]=z
refs={
 'MnNC_bare':['MnNC_clean','MnNC_OOH','MnNC_O','MnNC_OH'],
 'MnNC_axOH':['MnNC_OH','MnNC_OOH_OHb','MnNC_O_OH','MnNC_OH_OH'],
 'FCM_clean_bare':['S_FeCoMnNC59_clean','FCM_Mn_OOH','FCM_Mn_O','FCM_Mn_OH'],
 'FCM_clean_axOH':['FCM_Mn_OHb','FCM_Mn_OOH_OHb','FCM_Mn_O_OHb','FCM_Mn_OH_OHb'],
 'FCM_8O_bare':['FCM_rich8O_cont1','FCM_cov8O_OOH','FCM_cov8O_O','FCM_cov8O_OH'],
 'FCM_8O_axOH':['FCM_8O_MnOH','FCM_bg8O_MnOH_OOH','FCM_bg8O_MnOH_O','FCM_bg8O_MnOH_OH']}
def geom(x):
 f=np.array(x['coordinates']);cell=np.array(x['cell']);es=x['elements'];mi=es.index('Mn')
 if x['coordinate_mode'].lower().startswith('c'):f=f@np.linalg.inv(cell)
 def v(i,j):
  q=f[i]-f[j];q-=np.round(q);return q@cell
 def d(i,j):return float(np.linalg.norm(v(i,j)))
 N=[i for i,e in enumerate(es) if e=='N'];nv=np.array([v(i,mi) for i in N]);cen=nv.mean(axis=0);normal=np.linalg.svd(nv-cen)[2][-1]
 if normal[2]<0:normal=-normal
 O=[i for i,e in enumerate(es) if e=='O'];H=[i for i,e in enumerate(es) if e=='H'];M=[i for i,e in enumerate(es) if e in ['Fe','Co']]
 particle=[i for i in O if M and min(d(i,j) for j in M)<2.5]
 reactive=[i for i in O if i not in particle]
 sig=dict(particle_O=len(particle),reactive_O=len(reactive),OO=sum(d(i,j)<1.8 for ii,i in enumerate(reactive) for j in reactive[ii+1:]),OH=sum(d(i,j)<1.25 for i in reactive for j in H),MnO=sum(d(i,mi)<2.3 for i in reactive),ON=sum(d(i,j)<1.65 for i in reactive for j in N))
 detail=[dict(atom=i+1,Mn_O=d(i,mi),signed_Mn_plane=float(v(i,mi)@normal),OH=min([d(i,h) for h in H],default=None)) for i in reactive]
 # A particle breaks up/down symmetry. Preserve the reference's reaction/axial side.
 if M:
  sig['positive_MnO']=sum(d(i,mi)<2.3 and v(i,mi)@normal>0 for i in reactive)
  sig['negative_MnO']=sum(d(i,mi)<2.3 and v(i,mi)@normal<0 for i in reactive)
 return sig,detail
for x in rows:
 x['topology'],x['reactive_geometry']=geom(x)
 y=inputs.get(x['path'],{})
 if y.get('POSCAR_composition')==x['composition'] and y.get('POSCAR_coordinates'):
  tmp=dict(x,coordinates=y['POSCAR_coordinates'],coordinate_mode=y['POSCAR_mode']);x['initial_topology'],x['initial_reactive_geometry']=geom(tmp)
 else:x['initial_topology']=None;x['initial_reactive_geometry']=[]
def ref_for(name):
 rr=[x for x in rows if x['name']==name and x['kind']=='relax']
 if not rr:return None
 # Original IMR directory is authoritative unless this state exists only on Genkai.
 rr.sort(key=lambda x:(not (x['normal_end'] and x['ionic_converged']),x['machine']!='imr',len(x['path'])))
 return rr[0]
keys=['ENCUT','PREC','EDIFF','EDIFFG','LREAL','ISPIN','ISMEAR','SIGMA','IVDW','ISYM','ISIF','METAGGA','LHFCALC','LDAU','LDAUU','LDAUJ','NELECT','NUPDOWN','LSORBIT','LNONCOLLINEAR']
def settings_equal(a,b):
 def norm(v):
  if v is None:return None
  try:return float(v)
  except:return v.lower().replace('.','')
 return all(norm(a['settings'].get(k))==norm(b['settings'].get(k)) for k in keys)
allcomparisons=[];summary=[]
for family,names in refs.items():
 for state,name in zip(['base','OOH','O','OH'],names):
  ref=ref_for(name)
  if ref is None:
   summary.append(dict(family=family,state=state,reference_name=name,status='reference_not_found'));continue
  candidates=[]
  for x in rows:
   if x['composition']!=ref['composition']:continue
   reason=[]
   if x['kind']!='relax':reason.append('not_relax')
   if not x['normal_end'] or not x['ionic_converged']:reason.append('not_converged')
   if not np.allclose(x['cell'],ref['cell'],atol=1e-6):reason.append('cell_mismatch')
   if not settings_equal(x,ref):reason.append('settings_mismatch')
   if x['settings'].get('LDIPOL','.FALSE.').upper()!=ref['settings'].get('LDIPOL','.FALSE.').upper():reason.append('dipole_mismatch')
   if x['frozen_indices']!=ref['frozen_indices']:reason.append('fixed_atoms_mismatch')
   elif x['frozen_indices']:
    dv=np.array(x['coordinates'])-np.array(ref['coordinates']);dv-=np.round(dv);dv=dv@np.array(ref['cell']);ix=[i-1 for i in x['frozen_indices']]
    if np.linalg.norm(dv[ix],axis=1).max()>1e-4:reason.append('fixed_coordinates_mismatch')
   if x['topology']!=ref['topology']:reason.append('topology_or_side_changed')
   titles=lambda z:[s.strip() for s in z['POTCAR_titles']]
   if titles(x)!=titles(ref):reason.append('POTCAR_titles_mismatch')
   if inputs[x['path']].get('POTCAR_token_sha256')!=inputs[ref['path']].get('POTCAR_token_sha256'):reason.append('POTCAR_hash_mismatch')
   # Gamma mesh rows, excluding the title line.
   if x['KPOINTS'].splitlines()[1:]!=ref['KPOINTS'].splitlines()[1:]:reason.append('KPOINTS_text_diff_review')
   rr=dict(family=family,state=state,reference_path=ref['path'],path=x['path'],machine=x['machine'],energy_sigma0=x['energy_sigma0'],delta_vs_reference=x['energy_sigma0']-ref['energy_sigma0'],eligible=not reason,reasons=reason,initial_Mn=x['initial_Mn_moment'],Mn_local_moment=x['Mn_local_moment'],particle_sum_moment=x['particle_sum_moment'],total_moment=x['total_moment'],topology=x['topology'],geometry=x['reactive_geometry'],initial_topology=x['initial_topology'],initial_geometry=x['initial_reactive_geometry'],topology_changed_during_relax=x['initial_topology'] is not None and x['initial_topology']!=x['topology'])
   allcomparisons.append(rr)
   if not reason:candidates.append(rr)
  candidates.sort(key=lambda x:x['energy_sigma0'])
  initial=sorted(set(x['initial_Mn'] for x in candidates if x['initial_Mn'] is not None))
  summary.append(dict(family=family,state=state,reference_path=ref['path'],reference_energy=ref['energy_sigma0'],eligible_count=len(candidates),initial_Mn_values=initial,has_two_Mn_initial_values=len(initial)>=2,spin_start_coverage=(any(v<0 for v in initial) and any(v>0 for v in initial)) if ref['composition'].get('Fe',0) else len(set(abs(v) for v in initial))>=2,best=candidates[0] if candidates else None,status='existing_candidates_compared'))
(HERE/'comparison_24.json').write_text(json.dumps(summary,indent=2,default=lambda x:x.item()),encoding='utf-8')
(HERE/'candidate_decisions.json').write_text(json.dumps(allcomparisons,indent=2,default=lambda x:x.item()),encoding='utf-8')
with (HERE/'summary_24.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,lineterminator='\n');w.writerow(['family','state','reference_energy','best_existing_energy','delta','initial_Mn_values','two_initial_values','eligible_count','best_path'])
 for x in summary:
  b=x.get('best') or {};w.writerow([x['family'],x['state'],x.get('reference_energy'),b.get('energy_sigma0'),b.get('delta_vs_reference'),str(x.get('initial_Mn_values')),x.get('has_two_Mn_initial_values'),x.get('eligible_count'),b.get('path')])
for x in summary:
 b=x.get('best') or {};print(x['family'],x['state'],b.get('energy_sigma0'),x.get('initial_Mn_values'),b.get('delta_vs_reference'),x.get('status'))
