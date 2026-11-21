from pathlib import Path
import csv,json,shutil,win32com.client
OUT=Path(r'C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T006')
SRC=Path('D:/OneDrive/1a1数据文档/01_原始数据_按技术/FTIR/CoFeMn');TMP=Path('D:/_origin_tmp/T006_readonly')
app=win32com.client.DispatchEx('Origin.ApplicationSI');app.Visible=0
try:
 for name in ['1.opju','1-1.opju','1-2.opju','FeCoMn-NC(1-2).opju']:
  shutil.copy2(SRC/name,TMP/name);app.Execute('doc -n;');print('open',name,app.Load(str(TMP/name)),flush=True)
  stem=name[:-5];folder=OUT/stem;folder.mkdir(exist_ok=True)
  for bi in range(app.WorksheetPages.Count):
   b=app.WorksheetPages(bi)
   for si in range(b.Layers.Count):
    s=b.Layers(si);nr=s.Rows;nc=s.Cols
    data=app.GetWorksheet(f'[{b.Name}]{s.Name}',0,0,nr-1,nc-1)
    print(b.Name,s.Name,nr,nc,type(data),flush=True)
    if not isinstance(data,(list,tuple)):raise ValueError(repr(data))
    with (folder/f'{stem}__{b.Name}__{s.Name}.csv').open('w',newline='',encoding='utf-8') as f:
     w=csv.writer(f);w.writerow([s.Columns(i).Name for i in range(nc)]);w.writerows(data)
finally:app.Exit()
