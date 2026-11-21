import json,subprocess,base64,sys, pathlib
host=sys.argv[1]; inp=pathlib.Path(sys.argv[2]); out=pathlib.Path(sys.argv[3])
paths=json.loads(inp.read_text()); script=pathlib.Path(__file__).with_name('remote_parse.py').read_text()
script=script.replace("paths=json.load(open(sys.argv[1])) if len(sys.argv)>1 else json.load(sys.stdin); out=[]", "paths="+repr(paths)+"; out=[]")
r=subprocess.run(['ssh','-o','BatchMode=yes',host,'python3','-'],input=script,capture_output=True,text=True,timeout=600)
out.write_text(r.stdout,encoding='utf-8'); pathlib.Path(str(out)+'.stderr').write_text(r.stderr,encoding='utf-8'); print(host,r.returncode,len(r.stdout),r.stderr[-500:])
