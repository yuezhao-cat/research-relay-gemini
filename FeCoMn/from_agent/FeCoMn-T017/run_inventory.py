
from pathlib import Path
import subprocess,base64,json,sys
out=Path(__file__).resolve().parent;host=sys.argv[1]
code=base64.b64encode((out/'remote_inventory.py').read_bytes()).decode()
cmd=['ssh','-o','BatchMode=yes','-o','ConnectTimeout=20',host,'python3 -c '+"\"import base64;exec(base64.b64decode('"+code+"'))\""]
r=subprocess.run(cmd,capture_output=True,timeout=180)
(out/(host+'_inventory_raw.json')).write_bytes(r.stdout);(out/(host+'_inventory_stderr.txt')).write_bytes(r.stderr)
if r.returncode:raise SystemExit(r.returncode)
data=json.loads(r.stdout);selected=[x for x in data['records'] if __import__('re').search(r'FeCoMn|MnNC|FCM|FCN|MnN4|comparison_Mn|comparison_FeCo',x['path'],__import__('re').I)]
(out/(host+'_selected_paths.json')).write_text(json.dumps(selected,indent=2),encoding='utf-8')
print(host,'all',len(data['records']),'selected',len(selected),'archives',len(data['archives']),'errors',len(data['errors']),'seconds',data['elapsed_s'])
print('TOP:',data['top_dirs'])
