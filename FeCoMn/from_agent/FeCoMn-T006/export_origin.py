from pathlib import Path
import csv,json,hashlib,shutil,traceback
import win32com.client
import originpro as op
OUT=Path(r'C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T006')
SRC=Path('D:/OneDrive/1a1数据文档/01_原始数据_按技术/FTIR/CoFeMn'); TMP=Path('D:/_origin_tmp/T006_readonly')
def safe(f,*args):
 try:return f(*args)
 except Exception as e:return {'error':str(e)}
def prop(x,k):return safe(getattr,x,k)
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
allmeta=[]

op.set_show(False)
try:
 for name in ['1.opju','1-1.opju','1-2.opju','FeCoMn-NC(1-2).opju']:
  src=SRC/name;dst=TMP/name;shutil.copy2(src,dst)
  stem=name[:-5];folder=OUT/stem;folder.mkdir(exist_ok=True)
  m={'file':name,'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'books':[],'graphs':[],'matrices':[]}
  print('OPEN',name,flush=True);op.open(str(dst),readonly=True)
  for b in op.pages('w'):
   bm={'short_name':b.name,'long_name':b.lname,'sheets':[]}
   for s in b:
    nr,nc=s.shape;sm={'name':s.name,'rows':nr,'columns':nc}
    fn=f'{stem}__{b.name}__{s.name}.csv';sm['csv']=fn
    print('METADATA',fn,nr,nc,flush=True)
    cols=[]
    for i in range(nc):
     c=s.obj[i];co={'index_1based':i+1,'short_name':c.Name,'long_name':s.get_label(i,'L'),'units':s.get_label(i,'U'),'comments':s.get_label(i,'C'),'formula':s.get_label(i,'F'),'designation_code':prop(c,'Type'),'data_format':prop(c,'DataFormat')}
     cols.append(co)
    sm['column_metadata']=cols
    with (folder/f'{stem}__{b.name}__{s.name}__columns.csv').open('w',newline='',encoding='utf-8') as f:
     w=csv.DictWriter(f,fieldnames=list(cols[0]) if cols else []);w.writeheader();w.writerows(cols)
    bm['sheets'].append(sm)
   m['books'].append(bm)
  for b in op.pages('m'):
   m['matrices'].append({'name':b.name,'long_name':b.lname,'sheets':[{'name':s.name,'shape':safe(lambda:s.shape)} for s in b]})
  for g in op.graph_list('p',True):
   gm={'short_name':g.name,'long_name':g.lname,'layers':[]}
   for li,l in enumerate(g):
    lm={'index_1based':li+1,'plots':[],'objects':[]}
    for p in l.plot_list():
     pm={}
     for key in ['GetRange','GetDatasetName']:
      pm[key]=safe(getattr(p.obj,key)) if callable(getattr(p.obj,key,None)) else None
     for d in ['X','Y','Z']:
      pm['dataset_'+d]=safe(p.obj.GetDatasetName,d)
     lm['plots'].append(pm)
    for obj in safe(lambda:list(l.obj.GraphObjects)) if not isinstance(safe(lambda:list(l.obj.GraphObjects)),dict) else []:
     lm['objects'].append({k:prop(obj,k) for k in ['Name','Text','Type']})
    gm['layers'].append(lm)
   cmd=f'expgraph -sw type:=png filename:="{stem}__{g.name}" path:="{str(folder)}" overwrite:=replace tr2.Unit:=1 tr2.Resolution:=300;'
   gm['export_command']=cmd;gm['export_result']=safe(g.obj.LT_execute,cmd)
   print('GRAPH',g.name,flush=True);m['graphs'].append(gm)
  dump(folder/'structure.json',m);allmeta.append(m)
 dump(OUT/'all_structures.json',allmeta)
finally:
 op.exit()
