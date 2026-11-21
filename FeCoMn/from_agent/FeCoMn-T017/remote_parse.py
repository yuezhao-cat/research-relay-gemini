import os,re,sys,json,hashlib,subprocess
paths=json.load(open(sys.argv[1])) if len(sys.argv)>1 else json.load(sys.stdin); out=[]
def sha(p):
 h=hashlib.sha256()
 try:
  with open(p,'rb') as f:
   for b in iter(lambda:f.read(1<<20),b''):h.update(b)
  return h.hexdigest()
 except:return None
def tail(p,n=120000):
 try:
  with open(p,'rb') as f:
   f.seek(0,2); z=f.tell(); f.seek(max(0,z-n)); return f.read().decode('utf-8','replace')
 except:return ''
def first(p,n=20000):
 try:
  with open(p,'rb') as f:return f.read(n).decode('utf-8','replace')
 except:return ''
for ent in paths:
 p=ent['path']; x={'path':p,'host':os.uname().nodename}
 for fn in ['INCAR','KPOINTS','POSCAR','CONTCAR','OSZICAR','OUTCAR']:
  fp=os.path.join(p,fn); x['has_'+fn]=os.path.isfile(fp)
  if fn in ('CONTCAR','POSCAR','INCAR','KPOINTS') and x['has_'+fn]: x[fn+'_sha256']=sha(fp)
 inc=first(os.path.join(p,'INCAR')); x['incar']=inc[:12000]
 pos=first(os.path.join(p,'CONTCAR')); x['contcar_head']=pos[:8000]
 osi=tail(os.path.join(p,'OSZICAR')); x['oszicar_tail']=osi[-30000:]
 oc=tail(os.path.join(p,'OUTCAR'),500000); x['outcar_tail']=oc[-500000:]
 # final sigma->0 and TOTEN, normal end and convergence markers
 x['energy_sigma0']=re.findall(r'energy\(sigma->0\)\s*=\s*([-+]?\d+(?:\.\d+)?(?:[Ee][-+]?\d+)?)',oc)[-5:]
 x['toten']=re.findall(r'free\s+energy\s+TOTEN\s*=\s*([-+]?\d+(?:\.\d+)?(?:[Ee][-+]?\d+)?)',oc)[-5:]
 x['normal_end']=bool(re.search(r'General timing and accounting informations for this job|Voluntary context switches|Elapsed time',oc))
 x['ediff_reached']=bool(re.search(r'EDIFF is reached|aborting loop because EDIFF',oc))
 x['ionic_converged']=bool(re.search(r'reached required accuracy - stopping structural energy minimisation|reached required accuracy',oc))
 x['electronic_scf_count']=len(re.findall(r'Iteration\s+\d+\(',oc))
 # last magnetic moments blocks, max total moment and per atom lines near end
 mm=list(re.finditer(r'magnetization \(x\)',oc)); x['mag_blocks']=len(mm)
 if mm:
  b=oc[mm[-1].start():mm[-1].start()+40000]; x['mag_last_block']=b[-30000:]
  vals=[]
  for m in re.finditer(r'^\s*\d+\s+[-+]?\d+\.\d+\s+[-+]?\d+\.\d+\s+([-+]?\d+\.\d+)',b,re.M): vals.append(float(m.group(1)))
  x['mag_values_last']=vals[-300:]
 out.append(x)
print(json.dumps(out,separators=(',',':')))
