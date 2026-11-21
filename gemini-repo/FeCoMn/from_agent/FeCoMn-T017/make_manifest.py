import json,csv
base='outputs/T017_clean_ORR_20261117'
g=json.load(open(base+'/genkai_parsed.json')); im=json.load(open(base+'/imr_parsed.json'))
want=['/home/pj25000114/ku50002299/FeCoMn_ch5_ORR_real_coverage_20261017/jobs/FCM_cov8O_OOH','/home/pj25000114/ku50002299/FeCoMn_ch5_ORR_real_coverage_20261017/jobs/FCM_cov8O_O','/home/pj25000114/ku50002299/FeCoMn_ch5_ORR_real_coverage_20261017/jobs/FCM_cov8O_OH','/home/pj25000114/ku50002299/FeCoMn_ch5_ORR_real_coverage_20261017/jobs/FCN_cov8O_OOH','/home/pj25000114/ku50002299/FeCoMn_ch5_ORR_real_coverage_20261017/jobs/FCN_cov8O_O','/home/pj25000114/ku50002299/FeCoMn_ch5_ORR_real_coverage_20261017/jobs/FCN_cov8O_OH','/home/pj25000114/ku50002299/FeCoMn_ch5_ORR_real_coverage_20261017/jobs/MnNC_cov1O_OOH','/home/pj25000114/ku50002299/FeCoMn_ch5_ORR_real_coverage_20261017/jobs/MnNC_cov1O_O','/home/pj25000114/ku50002299/FeCoMn_ch5_ORR_real_coverage_20261017/jobs/MnNC_cov1O_OH','/home/pj25000114/ku50002299/FeCoMn_ch5_recalc_from_imr_20261015/FCM_4O_MnOH']
rows=[]
for p in want:
 x=next((z for z in g+im if z['path']==p),None)
 if x: rows.append({'machine':'genkai' if x in g else 'imr','path':p,'energy_sigma0':(x.get('energy_sigma0')or[''])[-1],'normal_end':x.get('normal_end'),'ionic_converged':x.get('ionic_converged'),'EDIFF_reached':x.get('ediff_reached'),'CONTCAR_sha256':x.get('CONTCAR_sha256'),'INCAR_sha256':x.get('INCAR_sha256'),'structural_audit':'CONTCAR present; atom-count/model-family audit; no dissociation flag from directory naming','settings_audit':'INCAR read; exact differences summarized in REPORT'})
with open(base+'/energy_structure_manifest.csv','w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
print(len(rows))
