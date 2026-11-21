from pathlib import Path
import json,win32com.client
out=Path(r'C:/Users/46775/Documents/Codex/2026-11-13/gu/research-relay/FeCoMn/from_agent/FeCoMn-T006')
app=win32com.client.DispatchEx('Origin.ApplicationSI');app.Visible=0
try:
 for folder in [p for p in out.iterdir() if p.is_dir()]:
  m=json.loads((folder/'structure.json').read_text(encoding='utf-8'));app.Load(str(Path('D:/_origin_tmp/T006_readonly')/m['file']))
  for g in m['graphs']:
   cmd=f'win -a {g["short_name"]}; expgraph -sw type:=png filename:="{folder.name}__{g["short_name"]}" path:="{folder}" overwrite:=replace tr2.png.dotsperinch:=300;'
   print(folder.name,g['short_name'],app.Execute(cmd),flush=True)
finally:app.Exit()
