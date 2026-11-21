from pathlib import Path
import pandas as pd,numpy as np,json,csv
out=Path('research-relay/FeCoMn/from_agent/FeCoMn-T006');raw=Path('research-relay/FeCoMn/data/SEIRAS_20241021_1-2')
results=[]
for f in out.rglob('*Sheet1.csv'):
 raw=Path('research-relay/FeCoMn/data')/('SEIRAS_20241021_1' if f.parent.name in ['1','1-1'] else 'SEIRAS_20241021_1-2')
 refs=[(z.name,pd.read_csv(z,header=None).apply(pd.to_numeric,errors='coerce').to_numpy(dtype=float)) for z in raw.glob('*.CSV')]
 d=pd.read_csv(f);meta=pd.read_csv(f.with_name(f.stem+'__columns.csv')).fillna('');x=None
 for i,c in enumerate(d):
  y=pd.to_numeric(d[c],errors='coerce').to_numpy();row={'project':f.parent.name,'sheet':f.name,'column':c,'label':str(meta.iloc[i].long_name),'comment':str(meta.iloc[i].comments),'finite_count':int(np.isfinite(y).sum())}
  if int(meta.iloc[i].designation_code)==3:
   x=y;row.update(kind='X',min=float(np.nanmin(y)),max=float(np.nanmax(y)));results.append(row);continue
  if row['finite_count']==0:row.update(raw_file='EMPTY_COLUMN',exact_candidates='');results.append(row);continue
  if x is None:results.append(row);continue
  best=None;exact=[]
  for name,a in refs:
   ix=np.searchsorted(a[:,0],x);ix=np.clip(ix,1,len(a)-1);ix-=np.abs(a[ix-1,0]-x)<np.abs(a[ix,0]-x)
   mask=np.isfinite(x)&np.isfinite(y)&(abs(a[ix,0]-x)<.001)
   mask &= np.isfinite(a[ix,1]);
   if mask.sum()<100:continue
   yy=y[mask];rr=a[ix[mask],1];A=np.column_stack([rr,np.ones(len(rr))]);coef=np.linalg.lstsq(A,yy,rcond=None)[0];res=yy-A@coef
   score=float(np.sqrt(np.mean(res**2)));candidate={'raw_file':name,'matched_points':int(mask.sum()),'max_x_difference':float(np.max(abs(a[ix[mask],0]-x[mask]))),'max_abs_direct_difference':float(np.max(abs(yy-rr))),'linear_scale':float(coef[0]),'linear_offset':float(coef[1]),'linear_fit_rmse':score,'linear_fit_max_abs_residual':float(np.max(abs(res)))}
   if candidate['max_abs_direct_difference']==0:exact.append(name)
   if best is None or score<best['linear_fit_rmse']:best=candidate
  row.update(best or {'raw_file':'NO_MATCHING_X_GRID'});row['raw_directory']=str(raw).replace('\\','/');row['exact_candidates']=';'.join(sorted(exact));results.append(row)
pd.DataFrame(results).to_csv(out/'column_pairing.csv',index=False,encoding='utf-8',lineterminator='\n');(out/'column_pairing.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
for pr in sorted(set(r['project'] for r in results)):
 rows=[r for r in results if r['project']==pr and r.get('kind')!='X'];print(pr,[(r['column'],r.get('raw_file'),round(r.get('linear_fit_rmse',0),9)) for r in rows])


