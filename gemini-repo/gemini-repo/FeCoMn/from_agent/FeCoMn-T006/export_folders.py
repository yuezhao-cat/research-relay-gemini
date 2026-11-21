import originpro as op,json
from pathlib import Path
out=Path(r'C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T006')
op.set_show(False)
try:
 for file in out.rglob('structure.json'):
  m=json.loads(file.read_text());op.open(str(Path('D:/_origin_tmp/T006_readonly')/m['file']),readonly=True)
  def walk(r):
   return {'name':r.Name,'path':r.Path,'children':[walk(x) for x in r.Folders]}
  try:m['folder_tree']=walk(op.po.GetRootFolder())
  except Exception as e:m['folder_tree_error']=str(e)
  file.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8');print(m['file'],m.get('folder_tree',m.get('folder_tree_error')),flush=True)
finally:op.exit()
