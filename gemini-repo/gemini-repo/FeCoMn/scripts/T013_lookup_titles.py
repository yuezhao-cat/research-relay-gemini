"""Read Crossref DOI metadata for unclear Fe/Co/Mn entries; cache every outcome."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import csv,json,re,requests,time
from urllib.parse import quote
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'FeCoMn/from_agent/FeCoMn-T013'
rows=list(csv.DictReader((OUT/'structure_unclear_review.csv').open(encoding='utf-8-sig')))
ds=sorted({r['doi_std'] for r in rows if set(r['metals'].split('-'))&{'Fe','Co','Mn'} and r['doi_std'].startswith('10.')})
p=OUT/'doi_metadata.json';cache=json.loads(p.read_text(encoding='utf8')) if p.exists() else {}
def get(d):
 u='https://api.crossref.org/works/'+quote(d,safe='')
 try:
  res=requests.get(u,timeout=22,headers={'User-Agent':'ResearchRelay/1.0 (academic DOI metadata verification)'})
  res.raise_for_status();m=res.json()['message']
  return d,{'title':' '.join(m.get('title',[])),'abstract':re.sub('<[^>]+>',' ',m.get('abstract','')),'source':u,'retrieved':'2026-11-15','doi_returned':m.get('DOI','')}
 except Exception as e:return d,{'error':str(e),'source':u,'retrieved':'2026-11-15'}
with ThreadPoolExecutor(max_workers=7) as ex:
 futures=[ex.submit(get,d) for d in ds if d not in cache]
 for i,f in enumerate(as_completed(futures),1):
  d,m=f.result();cache[d]=m
  p.write_text(json.dumps(cache,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
  if i%20==0:print(i,'/',len(futures),flush=True)
print('requested',len(ds),'titles',sum(bool(cache.get(d,{}).get('title')) for d in ds),flush=True)

# One sequential retry for transient 429 responses; do not burst-retry.
for d in ds:
 if '429' in cache.get(d,{}).get('error',''):
  time.sleep(1)
  _,cache[d]=get(d)
  p.write_text(json.dumps(cache,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print('after retry titles',sum(bool(cache.get(d,{}).get('title')) for d in ds),flush=True)
