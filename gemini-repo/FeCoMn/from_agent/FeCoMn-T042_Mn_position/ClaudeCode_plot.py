import csv, sys, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
rows = list(csv.DictReader(open(sys.argv[1])))
t032 = {'FCM_8O_bare': {'OOH': 3.9383, 'O': 1.4385, 'OH': 0.5157, 'UL': 0.5157}}
style = {'MnNC_bare': ('#1f77b4','o','Mn–NC, no ligand'), 'FCM_clean_bare': ('#1f77b4','s','FeCoMn–NC clean, no ligand'),
         'FCM_8O_bare': ('#1f77b4','^','FeCoMn–NC 8O*, no ligand'), 'FCM_clean_axOH': ('#2ca02c','s','FeCoMn–NC clean, axial OH'),
         'FCM_8O_axOH': ('#2ca02c','^','FeCoMn–NC 8O*, axial OH (working)'), 'MnNC_axO': ('#d62728','o','Mn–NC, axial O (working)'),
         'MnNC_axOH_hypo': ('#7f7f7f','D','Mn–NC, axial OH (hypothetical)')}
fig, ax = plt.subplots(1, 4, figsize=(14, 3.6))
for k, s in enumerate(['OOH', 'O', 'OH']):
    for f, (c, m, lab) in style.items():
        r = [x for x in rows if x['family'] == f and x['state'] == s][0]
        g = float(r['dG_eV_recalc'] or t032[f][s])
        ax[k].scatter(float(r['h_Mn_A']), g, c=c, marker=m, s=45, label=lab, edgecolors='k', linewidths=0.4,
                      facecolors='none' if f.endswith('hypo') else c)
    ax[k].axvline(0, ls=':', c='k', lw=0.8); ax[k].set_xlabel('Mn height after adsorption / Å'); ax[k].set_ylabel(f'ΔG({s}*) / eV')
for f, (c, m, lab) in style.items():
    r = [x for x in rows if x['family'] == f and x['state'] == 'OOH'][0]
    ul = float(r['UL_V_recalc'] or t032[f]['UL'])
    ax[3].scatter(float(r['h_Mn_A']), ul, c=c, marker=m, s=45, edgecolors='k', linewidths=0.4)
ax[3].axvline(0, ls=':', c='k', lw=0.8); ax[3].set_xlabel('Mn height in OOH* state / Å'); ax[3].set_ylabel('U_L / V')
ax[0].legend(fontsize=6, loc='upper left')
fig.suptitle('Mn out-of-plane height (+ = side opposite the intermediate) vs. free energies, original branches', fontsize=9)
fig.tight_layout(); fig.savefig(sys.argv[2], dpi=200)
