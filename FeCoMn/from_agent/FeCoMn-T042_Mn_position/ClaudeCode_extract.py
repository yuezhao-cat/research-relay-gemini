"""Claude Code (cloud) independent extraction of Mn out-of-plane height.
Source of geometry: FeCoMn/from_agent/FeCoMn-T031/{imr,genkai}_branches.json
(coordinates/cell/elements read by T031 from the original CONTCARs).
Definition: least-squares plane through the 4 N nearest to Mn (minimum image);
signed height h = (r_Mn - centroid_N4) . n, with n chosen so that h > 0 on the
side OPPOSITE the reaction intermediate (= axial-ligand side when a ligand exists).
For a background (no intermediate) the family's intermediate side is used.
Free energies: CHE with G(H2) = -6.83271509, G(H2O) = -14.32745679 eV,
ZPE-TS corrections OOH/O/OH = 0.403/0.066/0.343 eV (as T026/T032)."""
import json, csv, sys, numpy as np
root = sys.argv[1]
recs = {}
for m in ('imr', 'genkai'):
    for x in json.load(open(f'{root}/FeCoMn-T031/{m}_branches.json')):
        key = x['path'].split('/WORK/')[-1].split('ku50002299/')[-1]
        recs[key] = x

def geom(x):
    cell = np.array(x['cell'], float); frac = np.array(x['coordinates'], float)
    el = x['elements']; mi = x['Mn_index'] - 1
    assert el[mi] == 'Mn', (x['path'], el[mi])
    if frac.shape[0] != len(el):
        raise ValueError('coord/element mismatch')
    def mic(i):  # vector Mn -> atom i, minimum image
        d = frac[i] - frac[mi]; d -= np.round(d); return d @ cell
    vec = {i: mic(i) for i in range(len(el)) if i != mi}
    N = sorted([i for i in vec if el[i] == 'N'], key=lambda i: np.linalg.norm(vec[i]))[:4]
    P = np.array([vec[i] for i in N]); c = P.mean(0)
    n = np.linalg.svd(P - c)[2][-1]
    h = -c @ n                      # Mn at origin: height = (0 - c).n
    O = [i for i in vec if el[i] == 'O' and np.linalg.norm(vec[i]) < 2.3]
    Oside = [float(np.sign(vec[i] @ n)) for i in O]
    return h, n, O, Oside, [np.linalg.norm(vec[i]) for i in N], vec

GH2, GH2O = -6.83271509, -14.32745679
fam = {  # family: (base, OOH, O, OH, has_ligand, note)
 'MnNC_bare':      ('FeCoMn_ch5_recalc_20261007/MnNC_clean','FeCoMn_ch5_recalc_20261007/MnNC_OOH','FeCoMn_ch5_recalc_20261007/MnNC_O','FeCoMn_ch5_recalc_20261007/MnNC_OH',False,''),
 'MnNC_axO':       ('FeCoMn_ch5_recalc_20261007/MnNC_O_MnNbri','FeCoMn_ch5_ORR_real_coverage_20261017/jobs/MnNC_cov1O_OOH','FeCoMn_ch5_ORR_real_coverage_20261017/jobs/MnNC_cov1O_O','FeCoMn_ch5_ORR_real_coverage_20261017/jobs/MnNC_cov1O_OH',True,''),
 'FCM_clean_bare': ('FeCoMn_ch5_recalc_20261007/S_FeCoMnNC59_clean','FeCoMn_ch5_recalc_20261007/FCM_Mn_OOH','FeCoMn_ch5_recalc_20261007/FCM_Mn_O','FeCoMn_ch5_recalc_20261007/FCM_Mn_OH',False,''),
 'FCM_clean_axOH': ('FeCoMn_ch5_recalc_20261007/FCM_Mn_OHb','FeCoMn_ch5_recalc_20261007/FCM_Mn_OOH_OHb','FeCoMn_ch5_recalc_20261007/FCM_Mn_O_OHb','FeCoMn_ch5_recalc_20261007/FCM_Mn_OH_OHb',True,''),
 'FCM_8O_bare':    (None,'FeCoMn_ch5_ORR_real_coverage_20261017/jobs/FCM_cov8O_OOH','FeCoMn_ch5_ORR_real_coverage_20261017/jobs/FCM_cov8O_O','FeCoMn_ch5_ORR_real_coverage_20261017/jobs/FCM_cov8O_OH',False,'base FCM_rich8O_cont1 not in T031 JSON'),
 'FCM_8O_axOH':    ('FeCoMn_ch5_recalc_20261007/rich8O_joint_20261014/FCM_8O_MnOH','FeCoMn_ORR_MnOHbackground_20261030/FCM_bg8O_MnOH_OOH','FeCoMn_ORR_MnOHbackground_20261030/FCM_bg8O_MnOH_O','FeCoMn_ORR_MnOHbackground_20261030/FCM_bg8O_MnOH_OH',True,'working state'),
 'MnNC_axOH_hypo': ('FeCoMn_ch5_recalc_20261007/MnNC_OH','FeCoMn_ch5_recalc_20261007/MnNC_OOH_OHb','FeCoMn_ch5_recalc_20261007/MnNC_O_OH','FeCoMn_ch5_recalc_20261007/MnNC_OH_OH',True,'hypothetical; not in conclusion'),
}
t032 = {r['family']: r for r in csv.DictReader(open(f'{root}/FeCoMn-T032/original_ligand_free_energies.csv', encoding='utf-8-sig'))}
out = []
for f, (b, ooh, o, oh, lig, note) in fam.items():
    states = {'base': b, 'OOH': ooh, 'O': o, 'OH': oh}
    g = {s: geom(recs[p]) if p else None for s, p in states.items()}
    # reference normal: direction away from reaction-side O.
    # ligand families: ligand O = the Mn-bound O present in base; reaction O = the other side.
    ref = None
    if lig and g['base']:
        hb, nb, Ob, sb, _, vb = g['base']; ligvec = vb[Ob[0]]
        ref = ligvec / np.linalg.norm(ligvec)          # + toward ligand
    else:
        _, n1, O1, s1, _, v1 = g['OOH']
        ref = -v1[O1[0]] / np.linalg.norm(v1[O1[0]])   # + away from intermediate
    E = {s: recs[p]['energy_sigma0'] if p else None for s, p in states.items()}
    dG = {}
    if E['base'] is not None:
        dG['OOH'] = E['OOH'] - E['base'] - (2*GH2O - 1.5*GH2) + 0.403
        dG['O']   = E['O']   - E['base'] - (GH2O - GH2) + 0.066
        dG['OH']  = E['OH']  - E['base'] - (GH2O - 0.5*GH2) + 0.343
        steps = [dG['OOH']-4.92, dG['O']-dG['OOH'], dG['OH']-dG['O'], -dG['OH']]
        UL = -max(steps)
    else:
        UL = None
    for s in states:
        if g[s] is None:
            out.append(dict(family=f, state=s, path=states[s] or 'n/a', h_Mn_A='', note=note)); continue
        h, n, O, side, dN, _ = g[s]
        hs = h * float(np.sign(n @ ref))
        row = dict(family=f, state=s, path=states[s], h_Mn_A=f'{hs:+.4f}', MnN_mean_A=f'{np.mean(dN):.4f}',
                   E_sigma0=f"{E[s]:.6f}", note=note)
        if s != 'base':
            row['dG_eV_recalc'] = f"{dG[s]:.4f}" if s in dG else ''
            row['dG_eV_T032'] = f"{float(t032[{'FCM_8O_bare':'FCM_8O_bare','MnNC_axOH_hypo':'MnNC_axOH'}.get(f,f)]['G_'+s]):.4f}" if ({'MnNC_axOH_hypo':'MnNC_axOH'}.get(f,f)) in t032 else ''
        row['UL_V_recalc'] = f'{UL:.4f}' if UL is not None else ''
        out.append(row)
keys = ['family','state','h_Mn_A','MnN_mean_A','dG_eV_recalc','dG_eV_T032','UL_V_recalc','E_sigma0','path','note']
w = csv.DictWriter(open(sys.argv[2], 'w', newline=''), fieldnames=keys); w.writeheader()
for r in out: w.writerow({k: r.get(k, '') for k in keys})
