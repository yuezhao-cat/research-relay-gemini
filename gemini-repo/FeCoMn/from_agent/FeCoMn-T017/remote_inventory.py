
import os,sys,json,re,time
root=os.path.expanduser('~');start=time.time();records=[];archives=[];errors=[]
prune={'.git','.cache','.local','.conda','.vscode-server','node_modules','site-packages','vasp.6.4.2','vasp.6.3.2','vasp.6.5.0'}
for dp,dn,fn in os.walk(root,onerror=lambda e:errors.append(str(e)),followlinks=False):
 dn[:]=[d for d in dn if d not in prune and not d.startswith('.')]
 if 'OUTCAR' in fn or 'OSZICAR' in fn:
  records.append({'path':dp,'has_OUTCAR':'OUTCAR' in fn,'has_OSZICAR':'OSZICAR' in fn,'has_CONTCAR':'CONTCAR' in fn,'has_INCAR':'INCAR' in fn})
 for f in fn:
  if re.search(r'(FeCoMn|MnNC|FCM|FCN)',os.path.join(dp,f),re.I) and f.endswith(('.tar.gz','.tgz','.zip')):archives.append(os.path.join(dp,f))
print(json.dumps({'root':root,'top_dirs':[x for x in os.listdir(root) if os.path.isdir(os.path.join(root,x)) and not x.startswith('.')],'records':records,'archives':archives,'errors':errors,'elapsed_s':time.time()-start}))
