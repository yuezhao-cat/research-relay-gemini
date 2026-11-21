"""T013: lossless row preservation, conservative standardized columns, auditable rules.
Run from repository root. Python: openpyxl (read only); CSV output uses stdlib.
"""
from pathlib import Path
import csv, json, re, math, hashlib, collections, unicodedata
import openpyxl

ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/'FeCoMn/data/ORR_database'
OUT=ROOT/'FeCoMn/from_agent/FeCoMn-T013'
OUT.mkdir(parents=True,exist_ok=True)
SOURCE=DATA/'ORR_raw_20261115.xlsx'
original_hash=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
raw=list(openpyxl.load_workbook(SOURCE,read_only=True,data_only=True).active.values)
HEAD=list(raw[0]); ROWS=[dict(zip(HEAD,x)) for x in raw[1:]]
LOG=[]
def txt(x): return '' if x is None else str(x)
def norm(x): return unicodedata.normalize('NFKC',txt(x)).replace('−','-').replace('–','-').replace('‐','-').replace('─','-').strip()
def missing(x): return norm(x).lower() in ('','na','n/a','none','nan','null','-','na@na')
NUMBER=r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
def scalar(x):
 s=norm(x)
 return float(s) if re.fullmatch(NUMBER,s) else None
def log(r,field,old,new,basis):
 LOG.append({'row_id':r['row_id'],'excel_row':r['row_id']+1,'field':field,'original_value':txt(old),'standardized_value':txt(new),'basis':basis})

# Include Al and rare-earths; Ge/Si/As/Sb/Te are metalloids, NOT counted as metals.
METALS=set('Li Be Na Mg Al K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr'.split())
METALLOIDS={'B','Si','Ge','As','Sb','Te'}
NONMETALS=set('H He C N O F Ne P S Cl Ar Se Br Kr I Xe Rn Og'.split())
VALID=METALS|METALLOIDS|NONMETALS
ALIASES={'CO/NC S-1':'Co','CO/NC S-2':'Co','CO/NC S-3':'Co','CO/NC S-4':'Co','NINC-H2-360':'Ni','MWCNT-CUPc-Pd':'Cu','MWCNT-CuPC-Pd':'Cu','MWCNTI-CoPC-Pd':'Co','UDD-CoPC-Pd':'Co'}
def formula_elements(f):
 # Mask abbreviation tokens before symbol recognition; Pc/PPC etc never create P, Pt.
 s=norm(f)
 s=re.sub(r'\b(?:Biomass|Pristine|Molecular|Encapsulated|uncoated|catalyst|activated|including|transition|metal|elements|such|as)\b',' ',s,flags=re.I)
 s=re.sub(r'MWCNTI?|vdWHs|HPCs|CVD|CVM|UNT|UDD|NPY|YP|Acid|Ac(?=-)|Por|Pc|PC(?=-)|KB|US(?=[-/])|COP-Nap|No glucose',' ',s)
 s=re.sub(r'\b(?:MOF|COF|ZIF|PANI|PAN|PPy|MIL|DMOF|IRMOF|MWCNT|CNT|NCNT|SAC|DAC|SAA|SAs?|SAS|NPs?|NPt|AC|AD|DA|DAs|COOH|COCH3|COOCH3|CH3|NH2|NH3|KSCN|Li/K)\b',' ',s)
 s=re.sub(r'\b0(?:\.0+)?\s*%?-?Fe\b',' ',s)
 found=set()
 for m in re.finditer(r'[A-Z][a-z]?',s):
  e=m.group()
  if e not in VALID:continue
  if m.end()<len(s) and s[m.end()].islower():continue
  # Explicit zero stoichiometry should not add a species.
  tail=s[m.end():]
  if re.match(r'0(?![.\d])',tail):continue
  found.add(e)
 if norm(f) in ALIASES:found.add(ALIASES[norm(f)])
 if norm(f)=='MWCNT-CUPc-Pd':found.discard('U')
 if norm(f)=='AQ/U-POCN':found.discard('U')
 if norm(f)=='Fe-Nx-Cs':found.discard('Cs')
 if norm(f)=='ZIF-ZC91@Co(OH)2-VCo':found.discard('V')
 return found
def element_symbols(s):
 return {e for e in re.findall(r'[A-Z][a-z]?',norm(s)) if e in VALID}

def structure(r,title='',abstract=''):
 # Prefer explicit species evidence; @, MOF-derived and "N-doped" alone cannot prove particles.
 fields=[('subType',txt(r['subType'])),('Structural Property',txt(r['Structural Property'])),('Formula',txt(r['Formula'])),('Content',txt(r['Content']))]
 if title:fields.extend([('paper_title',title),('paper_abstract',abstract)])
 atoms=[];parts=[];dual=[]; evidence=[]
 for name,s in fields:
  patterns={
   'atom':r'single[-\s]*atom|\bSACs?\b|\bSAs?\b|\bSAS\b|FeSA|CoSA|CuSA|Ce SAS',
   'particle':r'nano[-\s]*particle|nano[-\s]*cluster|\bclusters?\b|\balloy\b|\bNPs?\b|\bSNPs\b|FeNP|CoNP|FeAC|CoAC|\bcarbide\b|Fe3C(?![a-z])|Co9S8|Ni3S2|NiCo.?O4|Fe.?O[234]|Co3O4|CeO2|ZrO2',
   'dual':r'dual[-\s]*atom|double[-\s]*atom|\bDACs?\b|\bDAs?\b|binuclear|diatomic|Fe2-pPc|Co2-DAs'}
  for k,p in patterns.items():
   if k=='particle' and name=='Formula' and (s.startswith('Ca/NPS-') or s.startswith('Co-N/C+NP')):continue
   m=re.search(p,s,re.I)
   if m:
    evidence.append(name+': '+s[max(0,m.start()-55):m.end()+90].replace('\n',' '))
    {'atom':atoms,'particle':parts,'dual':dual}[k].append(name)
 if r['metal_free_or_unknown']=='metal-free':return 'metal-free','Formula/Elements: explicit carbon/nonmetal composition; no metal evidence'
 strong_atoms=[a for a in atoms if a!='subType']
 if atoms and parts and not strong_atoms:return 'particle-or-cluster','subType says single-atom but sample-specific particle evidence takes priority | '+' | '.join(evidence)
 if atoms and parts and re.search(r'FeNP|CoNP|\bNPs',txt(r['Formula']),re.I) and not any('atom' in e.lower() and ('nanoparticle' in e.lower() or 'cluster' in e.lower()) for e in evidence):return 'unclear','atom/particle conflict in supplied sample annotations | '+' | '.join(evidence)
 if atoms and parts:return 'particle+single-atom',' | '.join(evidence)
 if dual and parts:return 'unclear','dual-atom plus particle evidence; requested taxonomy has no exact category | '+' | '.join(evidence)
 if dual:return 'dual-atom',' | '.join(evidence)
 if atoms:return 'single-atom',' | '.join(evidence)
 if parts:return 'particle-or-cluster',' | '.join(evidence)
 # Pt/C is explicit supported Pt benchmark; not assign every metal/carbon slash a phase.
 if re.fullmatch(r'(?:20\s*wt\.?%?\s*)?Pt/C(?:\s*20%|\(20 wt% Pt\))?',norm(r['Formula'])):
  return 'particle-or-cluster','Formula: '+txt(r['Formula'])+'; conventional supported Pt/C benchmark (provisional)'
 return 'unclear','No unambiguous atom/particle evidence in supplied row'

def electrolyte(r):
 s=norm(r['Electrolytes']); q=s.lower(); flags=[];std=s
 q=q.replace('hclo4','hclo4')
 formula=None
 for low,proper in [('koh','KOH'),('naoh','NaOH'),('hclo4','HClO4'),('h2so4','H2SO4'),('hcl','HCl'),('pbs','PBS')]:
  if low in q:formula=proper;break
 c=None
 if formula:
  m=re.search(r'('+NUMBER+r')\s*(mM|M|mol\s*[lL][−-]?1)?\s*(?:neutra\s*)?'+re.escape(formula),s,re.I)
  if m:
   c=float(m.group(1)); unit=m.group(2)
   if unit and unit=='mM':c/=1000
   if not unit:flags.append('missing concentration unit; not assumed M');c=None
  if c is not None:std=f'{c:g} M {formula}'
  else:std=formula+' [concentration unconfirmed]'
 if formula in ('KOH','NaOH'):medium='alkaline'
 elif formula in ('HClO4','H2SO4','HCl'):medium='acidic'
 elif formula=='PBS':medium='neutral';flags.append('PBS grouped neutral; actual pH may differ')
 else:medium='other'
 ph=scalar(r['pH']);estimated=0;basis='source pH' if ph is not None else 'not estimated'
 if ph is None and c and c>0:
  if formula in ('KOH','NaOH'):ph=14+math.log10(c);basis='ideal strong base, 25 C, pKw=14';estimated=1
  elif formula in ('HClO4','HCl'):ph=-math.log10(c);basis='ideal monoprotic strong acid, 25 C';estimated=1
  elif formula=='H2SO4':
   ka=.012;h2=(-(c+ka)+math.sqrt((c+ka)**2+4*ka*c))/2;ph=-math.log10(c+h2);estimated=1;basis='ideal H2SO4: first complete, second Ka2=0.012 at 25 C'
 if ph is not None:
  if not -2<=ph<=16:flags.append('pH outside plausibility range')
  pm='acidic' if ph<6 else 'alkaline' if ph>8 else 'neutral'
  if medium=='other':medium=pm
  elif pm!=medium:flags.append('pH/medium disagreement')
 return dict(medium=medium,electrolyte_std=std,pH_est=ph,pH_estimated=estimated,pH_basis=basis,electrolyte_flag='; '.join(flags))

def pair(x,kind,unit):
 s=norm(x);out={'value':None,'at_potential':None,'unit':unit,'reference':'','flag':''}
 if kind=='onset':out['criterion_current_density']=None
 if missing(x):out['flag']='missing';return out
 s=s.replace('@@','@');pieces=s.split('@');left=pieces[0].strip();right=pieces[1].strip() if len(pieces)>1 else ''
 if len(pieces)>2:out['flag']='multiple @; ambiguous';return out
 # Only an entire scalar with optional explicit compatible unit is accepted.
 p=rf'^({NUMBER})\s*(%|V|mV|A\s*mg-1|A/mg|mA\s*cm-2|mA/cm2|s-1)?$'
 m=re.fullmatch(p,left,re.I)
 if m:
  v=float(m.group(1));u=(m.group(2) or '').lower()
  if '%' in u and kind!='h2o2':out['flag']='unit mismatch: percent in non-percent column'
  elif kind=='onset' and u=='mv':out['value']=v/1000
  else:out['value']=v
 else:out['flag']='non-scalar/range/qualifier or unrecognized unit'
 if right and not missing(right):
  if re.search(r'Ag/?AgCl|SCE|SHE|Hg',right,re.I):out['flag']+='; non-RHE reference, no conversion without reference calibration'
  else:
   m=re.fullmatch(rf'({NUMBER})\s*(?:V|\(V/?RHE\)|\(V vs\.? RHE\))?',right,re.I)
   if m:out['at_potential']=float(m.group(1));out['reference']='RHE (source column header)'
   else:out['flag']+='; potential unparsed/range'
 if kind=='onset':
  # Source schema E@j: @ suffix is current criterion, NOT potential.
  out['criterion_current_density']=out['at_potential'];out['at_potential']=None
  if re.search('Ag/?AgCl|SCE',s,re.I):out['value']=None;out['reference']='non-RHE';out['flag']+='; onset reference not RHE'
  elif out['value'] is not None:out['reference']='RHE (source column header)'
 if kind in ('disk_j','ring_j','tof','mass_activity','specific_activity') and out['value'] is not None:
  # Magnitude convention is explicit; source signed values remain untouched.
  out['value']=abs(out['value'])
 if kind=='h2o2' and out['value'] is not None and not 0<=out['value']<=100:out['flag']+='; outside 0-100%'
 return out

PAIR_FIELDS=[(11,'onset_disk','onset','V vs RHE'),(12,'onset_ring','onset','V vs RHE'),(13,'disk_j','disk_j','mA cm-2'),(14,'disk_tof','tof','s-1'),(15,'ring_j','ring_j','mA cm-2'),(16,'ring_tof','tof','s-1'),(17,'h2o2','h2o2','%'),(19,'mass_activity','mass_activity','A mg-1'),(20,'specific_activity','specific_activity','mA cm-2')]
def stability(r):
 a=norm(r[HEAD[21]]);b=norm(r[HEAD[22]]);d=norm(r[HEAD[23]])
 out={'stability_cycles':None,'stability_hours':None,'stability_at_potential':None,'stability_loss_value':None,'stability_loss_unit':'','stability_metric':'','stability_flag':''}
 flags=[]
 if scalar(a) is not None:out['stability_cycles']=scalar(a)
 for field,s in [('cycles_column',a),('hours_column',b)]:
  if missing(s):continue
  left=s.split('@')[0].strip();m=re.match(rf'^({NUMBER})\s*(s|sec|seconds?|h|hr|hours?)\b',left,re.I)
  if m:
   n=float(m.group(1));out['stability_hours']=n/3600 if m.group(2).lower().startswith('s') else n
  elif field=='hours_column':
   if 'cycle' in s.lower():out['stability_cycles']=scalar(left);flags.append('cycles stored in hours column')
   elif scalar(left) is not None:
    v=scalar(left)
    if v>=1000:flags.append('unitless duration >=1000: seconds/cycles/h ambiguous; not converted')
    else:out['stability_hours']=v;flags.append('unitless duration assumed h from header')
   else:flags.append('duration unparsed')
  if '@' in s:
   rt=s.split('@')[1].strip()
   if re.search(r'mA|mV|AgCl|SCE',rt,re.I):flags.append('stability @ is current or non-RHE/ambiguous')
   else:
    m=re.fullmatch(rf'({NUMBER})\s*(?:V|V/RHE)?',rt,re.I)
    if m:out['stability_at_potential']=float(m.group(1))
    elif not missing(rt):flags.append('stability potential range/unparsed')
 if not missing(d):
  if re.search(r'no decay',d,re.I):out['stability_loss_value']=0;out['stability_metric']='reported no decay'
  else:
   m=re.search(rf'({NUMBER})\s*(mV|V|%)',d,re.I)
   if m:
    out['stability_loss_value']=float(m.group(1));out['stability_loss_unit']=m.group(2)
    out['stability_metric']='retention' if re.search('retention|retain',d,re.I) else 'E1/2 shift' if re.search('E1/2|half.wave',d,re.I) else 'current density loss' if re.search('current',d,re.I) else 'unspecified metric'
   elif scalar(d) is not None:out['stability_loss_value']=scalar(d);flags.append('loss unit/metric unspecified')
   else:flags.append('loss unparsed')
 out['stability_flag']='; '.join(flags);return out

keys={};groups=collections.defaultdict(list)
for i,r in enumerate(ROWS,1):
 r['row_id']=i;r['doi_std']=norm(r['DOI']).lower();key=(r['doi_std'],txt(r['Formula']))
 if key not in keys:keys[key]=f'CAT{len(keys)+1:04d}'
 r['catalyst_id']=keys[key];groups[r['catalyst_id']].append(r)
 es=element_symbols(r['Elements']);fs=formula_elements(r['Formula']);metal=(es|fs)&METALS;reasons=[]
 if (es^fs)&METALS:reasons.append('Elements/Formula metal sets differ; union retained, possible template/precursor residual')
 if metal&{'K','Na','Li'}:reasons.append('alkali element may be electrolyte/precursor; requires paper confirmation')
 if norm(r['Formula']) in ALIASES:reasons.append('reviewed capitalization alias '+norm(r['Formula']))
 if re.search(r'^TM@|transition metal|including',txt(r['Formula']),re.I):reasons.append('generic TM list; composition not a unique catalyst')
 if re.search(r'\bPc\b|Pc|COF|MOF|ZIF',txt(r['Elements'])):reasons.append('non-element abbreviation in Elements; ignored as element')
 if re.match(r'^0(?:\.0+)?\s*%?-?Fe',norm(r['Formula'])):metal.discard('Fe');reasons.append('explicit zero Fe in Formula; source Fe Elements not treated as active Fe')
 r['metals']='-'.join(sorted(metal));r['n_metals']=len(metal);r['metalloids']='-'.join(sorted((es|fs)&METALLOIDS))
 r['metals_from_elements']='-'.join(sorted(es&METALS));r['metals_from_formula']='-'.join(sorted(fs&METALS))
 carbon_only=not metal and not ((es|fs)&{'Sb','Ge','As','Te'}) and bool((es|fs)&{'C','N'}) and not re.search(r'ZIF|MOF|MIL|MN4|MNNC|ELC|CSPP|FBNC|FMC|FCMC|^FC$|^MC$|Shx',txt(r['Formula']),re.I)
 r['metal_free_or_unknown']='metal-present' if metal else 'metal-free' if carbon_only else 'unknown'
 if not metal and not carbon_only:reasons.append('no confirmed metal; coded/precursor formula cannot prove metal-free')
 if not metal and r['metalloids']:reasons.append('metalloid listed separately, not a metal')
 r['metal_uncertain']=int(bool(reasons));r['metal_uncertain_reason']='; '.join(reasons)
 r.update(electrolyte(r))
 e=scalar(r[HEAD[10]]);r['E12_value']=e;r['E12_reference']='RHE (source header)' if e is not None else ''
 r['E12_flag']='missing' if missing(r[HEAD[10]]) else 'non-numeric/reference or unit requires review' if e is None else 'outside 0.3-1.2 V; verify unit/reference' if not .3<=e<=1.2 else ''
 if e is not None and not .3<=e<=1.2:r['E12_reference']='unverified (source header RHE)'
 for idx,prefix,kind,unit in PAIR_FIELDS:
  for k,v in pair(r[HEAD[idx]],kind,unit).items():r[prefix+'_'+k]=v
 r.update(stability(r));r['year_std']=scalar(r['Year']);r['year_flag']='' if r['year_std'] is not None and 1900<=r['year_std']<=2026 and r['year_std']%1==0 else 'missing/invalid'
 r['structure_class'],r['structure_evidence']=structure(r)
 r['structure_source']='supplied row';r['paper_title']='';r['paper_metadata_source']='';r['doi_topic_flag']=''

# DOI title/abstract cache is created independently by a read-only metadata lookup.
cachefile=OUT/'doi_metadata.json';cache=json.loads(cachefile.read_text(encoding='utf8')) if cachefile.exists() else {}
for r in ROWS:
 if r['structure_class']=='unclear' and {'Fe','Co','Mn'}&set(r['metals'].split('-')):
  meta=cache.get(r['doi_std'],{});title=meta.get('title','');abstract=meta.get('abstract','')
  r['paper_title']=title;r['paper_metadata_source']=meta.get('source','')
  if title:
   cl,ev=structure(r,title,abstract)
   # Paper-level morphology is not automatically assigned to every control catalyst.
   title=re.sub('<[^>]+>','',title);r['paper_title']=title
   r['structure_evidence']+=' | DOI title: '+title
   if re.search('electrophysiological|hydrodesulfurization',title,re.I):r['doi_topic_flag']='DOI title appears unrelated to ORR; verify source, row retained'
   # Explicit metal morphology plus a matching, sole metal in the sample label.
   single_match=any(re.search(p,title,re.I) and r['metals']==e and e in formula_elements(r['Formula']) for e,p in [('Fe',r'single[- ](?:iron )?atom.*iron|single iron atoms|atomically dispersed iron|single-atom Fe-N-C|dense Fe.*N.*4 sites'),('Co',r'atomically dispersed Co|atomically dispersed cobalt'),('Mn',r'atomically dispersed manganese')])
   particle_match=any(re.search(p,title,re.I) and re.search(f,txt(r['Formula']),re.I) for p,f in [(r'Ni3Fe nanoalloys',r'Ni3Fe'),(r'CoSn alloy',r'CoSn|Sn@NC|Co@NC'),(r'CoMn alloy',r'CoMn@'),(r'Co.*Ni.*Alloy',r'Co0\.25Ni0\.75'),(r'NiCo Alloy Nanoparticles',r'Ni[0-9]Co[0-9]'),(r'encased Co NPs',r'S,N-Co@CNT')])
   if single_match:
    r['structure_class']='single-atom';r['structure_source']='DOI title: explicit atomic metal + matching sole metal in Formula (provisional)'
   elif particle_match:
    r['structure_class']='particle-or-cluster';r['structure_source']='DOI title: explicit alloy/particle + matching Formula (provisional)'
   if r['structure_class']=='unclear':
    if cl!='unclear':r['structure_evidence']+=' | paper-level candidate '+cl+'; not assigned without sample mapping'
    r['structure_source']='supplied row + DOI title/abstract checked (sample attribution conservative)'
  else:r['structure_evidence']+=' | title lookup unavailable: '+meta.get('error','not retrieved')
for cid,gg in groups.items():
 for r in gg:
  r['dup_flag']=int(len(gg)>1);r['dup_reason']=''
  if len(gg)>1:
   reasons=[]
   if any(all(r[h]==s[h] for h in HEAD) for s in gg if s is not r):reasons.append('exact duplicate original 46 cells')
   if len({txt(s['Electrolytes']) for s in gg})>1:reasons.append('different electrolyte entries')
   if any(len({txt(s[HEAD[k]]) for s in gg})>1 for k in [21,22,23]):reasons.append('different stability entries')
   if any(len({txt(s[HEAD[k]]) for s in gg})>1 for k in range(10,21)):reasons.append('different performance entries')
   if not reasons:reasons.append('same DOI+Formula; other metadata differ')
   r['dup_reason']='; '.join(reasons)
 for r in gg:
  for f in [k for k in r if k not in HEAD and k not in ('row_id','catalyst_id')]:
   if r[f] in ('',None):continue
   sourcecols=['Formula','Elements'] if f.startswith(('metal','n_metal')) else ['subType','Structural Property','Formula','Content'] if f.startswith(('structure','paper','doi_topic')) else ['Electrolytes','pH'] if f.startswith(('medium','electrolyte','pH')) else [HEAD[10]] if f.startswith('E12') else [HEAD[21],HEAD[22],HEAD[23]] if f.startswith('stability') else ['DOI'] if f=='doi_std' else ['Year'] if f.startswith('year') else HEAD if f.startswith('dup') else []
   for idx,prefix,_,_ in PAIR_FIELDS:
    if f.startswith(prefix+'_'):sourcecols=[HEAD[idx]]
   old=json.dumps({h:r[h] for h in sourcecols},ensure_ascii=False,default=str)
   basis='T013_clean_ORR.py rule; '+(r['metal_uncertain_reason'] if f.startswith(('metal','n_metal')) else r['structure_evidence'] if f.startswith('structure') else r['pH_basis'] if f.startswith('pH') else r['stability_flag'] if f.startswith('stability') else 'raw columns unchanged')
   log(r,f,old,r[f],basis)

def writecsv(path,rows,fields=None):
 if fields is None:fields=list(dict.fromkeys(k for r in rows for k in r))
 with path.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
writecsv(DATA/'ORR_clean_20261115.csv',ROWS,HEAD+list(dict.fromkeys(k for r in ROWS for k in r if k not in HEAD)))
cats=[]
for cid,gg in groups.items():
 e=collections.defaultdict(list)
 for r in gg:
  e[r['electrolyte_std']].append({'row_id':r['row_id'],'E12':r['E12_value'],'flag':r['E12_flag'],'pH':r['pH_est']})
 cats.append({'catalyst_id':cid,'DOI':gg[0]['doi_std'],'Formula':gg[0]['Formula'],'row_ids':';'.join(str(r['row_id']) for r in gg),'n_rows':len(gg),'metals':' | '.join(sorted({r['metals'] for r in gg})),'metal_uncertain':max(r['metal_uncertain'] for r in gg),'structure_class':' | '.join(sorted({r['structure_class'] for r in gg})),'E12_by_electrolyte':json.dumps(e,ensure_ascii=False),'aggregation_note':'all observations retained; no arbitrary best value or averaging'})
writecsv(DATA/'ORR_catalyst_level_20261115.csv',cats)
writecsv(OUT/'cleaning_log.csv',LOG)
def dist(field,items=ROWS):return dict(collections.Counter(txt(r[field]) for r in items).most_common())
stats={'raw_sha256':original_hash,'rows':len(ROWS),'catalysts':len(cats),'duplicate_rows':sum(r['dup_flag'] for r in ROWS),'structure':dist('structure_class'),'medium':dist('medium'),'metals':dist('metals'),'n_metals':dist('n_metals'),'year':dist('year_std'),'submitter_Name':dist('Name'),'submitter_Institute':dist('Institute'),'electrolyte':dist('electrolyte_std'),'uncertain_metal_rows':sum(r['metal_uncertain'] for r in ROWS),'fields':{}}
for idx,prefix,kind,unit in [(10,'E12','','')]+PAIR_FIELDS:
 field=prefix+'_value';stats['fields'][prefix]={'before_nonempty':sum(not missing(r[HEAD[idx]]) for r in ROWS),'after_numeric':sum(r[field] is not None for r in ROWS),'after_numeric_unflagged':sum(r[field] is not None and not r.get(prefix+'_flag') for r in ROWS),'flagged_nonmissing':sum(bool(r.get(prefix+'_flag')) and r.get(prefix+'_flag')!='missing' for r in ROWS)}
(OUT/'summary.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
writecsv(OUT/'metal_review_queue.csv',[{k:r[k] for k in ['row_id','catalyst_id','Formula','Elements','metals','metalloids','metal_uncertain_reason','doi_std']} for r in ROWS if r['metal_uncertain']])
writecsv(OUT/'structure_unclear_review.csv',[{k:r[k] for k in ['row_id','catalyst_id','Formula','metals','doi_std','paper_title','structure_evidence','paper_metadata_source']} for r in ROWS if r['structure_class']=='unclear'])
assert len(ROWS)==1484
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==original_hash
with (DATA/'ORR_clean_20261115.csv').open(encoding='utf-8-sig',newline='') as f:back=list(csv.DictReader(f))
assert len(back)==len(ROWS)
assert all(back[i][h]==txt(raw[i+1][j]) for i in range(len(ROWS)) for j,h in enumerate(HEAD))
assert sum(c['n_rows'] for c in cats)==1484
(OUT/'validation.json').write_text(json.dumps({'row_count':1484,'all_original_46_columns_roundtrip_equal':True,'source_sha256_unchanged':True,'catalyst_groups_cover_all_rows':True},indent=2)+'\n',encoding='utf8')
print(json.dumps({'rows':len(ROWS),'catalysts':len(cats),'structure':stats['structure'],'uncertain_metals':stats['uncertain_metal_rows']},ensure_ascii=True))
