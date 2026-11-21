from pathlib import Path
ROOT=Path(r"D:/OneDrive/Desktop/知识库/papers/FeCoMn/ACS_Catalysis_第三轮投稿")
import os
os.environ['ZY_CALC']=str(ROOT/'单图汇总_journal_20261025/10_计算_第三轮')
os.environ['ZY_ATOM']=str(ROOT/'单图汇总_journal_20261025/92_电子结构统一原参考态_20261029/atom_resolved_occupied_d_centers.csv')
os.environ['ZY_CHARGE']=str(ROOT/'电子结构系统核对_20261029/三样品九吸附态_统一口径对照.csv')
os.environ['ZY_OUT']=str(Path(__file__).resolve().parent)
# -*- coding: utf-8 -*-
"""Figure 6 v6 = working version (2026-11-03): v5 data/curve handling + "−ICOHP (eV)" header and "Bonded-metal" label from the parallel preview. v5 was (2026-11-03: a full width; b OOH* PDOS; c OOH*/OH* -pCOHP in one column; d contact-metal Bader; e electron excess; f volcano; g original reaction schematic). v3 was (2026-11-03: a full-width maps; b OOH* PDOS; c OOH*/OH* -pCOHP with bond labels; d contact-metal Bader; e adsorbate electron excess; f volcano; model + structures -> SI). v2 was: a maps; b model with axial OH / reaction side; c OOH* local structures; d OOH* PDOS; e OOH*/OH* -pCOHP; f contact-metal Bader; g adsorbate electron excess; h volcano. FCN OOH* contacts = Fe206/Co235. Earlier: c OOH* PDOS; d OOH* and OH* -pCOHP side by side; f OOH*/OH* electron excess). Earlier layout following the author's reference sketch (2026-10-28), drawn from real data only.
a atom-resolved occupied eps_d maps (3 catalysts x 4 states); b element-resolved eps_d (mean, min-max band);
c OH* PDOS; d OH* -pCOHP; e |dN_Bader| per O-bonded metal atom; f eps_d(OH*) vs DG_OH*; g -ICOHP(OH*) vs DG_OH*;
h FeCoMn-NC working surface + mechanism chain. No regression lines: n = 3."""
import os, sys, csv
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import acs, zyload
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch, FancyBboxPatch
from matplotlib.lines import Line2D
from PIL import Image
C = os.environ['ZY_CALC']; ATOM = os.environ['ZY_ATOM']; OUT = os.environ['ZY_OUT']; STEM = 'Figure_6_T029_20261118_labelgap'
acs.use()
L = lambda n: zyload.load(os.path.join(C, n + '_journal_20261025.csv'))[1]
EK, PK = '$E - E_{\\rm F}$ (eV)', 'PDOS (states eV$^{-1}$)'
SYS = [('FCM', 'FeCoMn–NC'), ('FCN', 'FeCo–NC'), ('MnNC', 'Mn–NC')]   # en dash, as in the manuscript
COL = {k: acs.SAMPLE[n.replace('–', '-')] for k, n in SYS}
EDGE = {'FCM': '#b8475a', 'FCN': '#7f7bab', 'MnNC': '#d9846c'}
ODASH = '#5c506f'
ADS = ['OOH', 'O', 'OH']; ADSL = ['OOH*', 'O*', 'OH*']
ST = ['base', 'OOH', 'O', 'OH']; STL = ['Covered', 'OOH*', 'O*', 'OH*']
CONTACT = {'FCM': {s: [238] for s in ST}, 'MnNC': {s: [179] for s in ST},
           'FCN': {'base': [206, 234, 235], 'OOH': [206, 235], 'O': [206, 234], 'OH': [206, 234, 235]}}
VMIN, VMAX = -3.5, -1.7
CMAP = LinearSegmentedColormap.from_list('zy', ['#b6b3d6', '#d5d3df', '#f7dfd7', '#f1837b', '#eb687b'])
def broaden(e, y, s=0.10):
    de = np.median(np.diff(e)); k = np.arange(-4*s, 4*s + de, de)
    g = np.exp(-k**2/(2*s*s)); g /= g.sum(); return np.convolve(y, g, mode='same')
def mfmt(v, n=2): return f'{v:.{n}f}'.replace('-', '−')
EPS_T = '$\\varepsilon$' + acs.sub('d')

# ---------- numbers ----------
at = pd.read_csv(ATOM)
# FCN covered state: contact atoms recomputed from the low-spin base PDOS (Genkai 7163241), same -8..0 eV centroid
_b = zyload.load(os.path.join(C, 'calc_PDOS_FCN_base_journal_20261025.csv'))[1]
for lab, v in _b.items():
    if '3d' not in lab: continue
    e, y = v[EK], v[PK]; m = (e >= -8) & (e <= 0); ec = float(np.trapezoid(e[m]*y[m], e[m]) / np.trapezoid(y[m], e[m]))
    idx = int(''.join(ch for ch in lab.split()[0] if ch.isdigit()))
    at.loc[(at['sample'] == 'FCN') & (at.state == 'base') & (at.atom_1based == idx), 'occupied_d_center_eV'] = ec
    print('FCN base', lab, round(ec, 3))
EPS = {(k, s): float(at[(at['sample'] == k) & (at.state == s) & at.atom_1based.isin(CONTACT[k][s])].occupied_d_center_eV.mean())
       for k, _ in SYS for s in ST}
db = L('calc_d_band_center_contact_metals')['bar']['$\\varepsilon_d$ (eV)']
for i, (k, _) in enumerate(SYS):
    for j, a_ in enumerate(ADS): assert (k, a_) == ('FCN', 'OOH') or abs(EPS[(k, a_)] - float(db[3*i+j])) < 2e-3   # FCN OOH*: O bonds Fe206/Co235 only
ic = L('calc_ICOHP_metal_O_total')['bar']['−ICOHP (eV)']
ICO = {(k, a): float(ic[3*i+j]) for i, (k, _) in enumerate(SYS) for j, a in enumerate(ADS)}
bad = pd.read_csv(os.path.join(C, 'calc_Bader_contact_metal_change_journal_20261025.csv'))
badN = pd.read_csv(os.path.join(C, 'calc_Bader_FCN_contact_metal_change_journal_20261025.csv'))
DNA = {}   # |sum dN| over the O-bonded metal atoms (total charge donated to the adsorbate)
for a_ in ADS:
    for k in ('FCM', 'MnNC'):
        DNA[(k, a_)] = abs(float(bad[(bad.system == k) & (bad.adsorbate == a_)].delta_electrons.sum()))
    DNA[('FCN', a_)] = abs(float(badN[(badN.adsorbate == a_) & badN.atom_index_1based.isin(CONTACT['FCN'][a_])].delta_electrons_vs_lowspin_base.sum()))
UL = {}
for line in open(os.path.join(C, 'calc_ORR_limiting_potential_journal_20261025.csv'), encoding='utf-8-sig').read().splitlines()[2:]:
    p = line.split(','); UL[{'FeCoMn-NC': 'FCM', 'FeCo-NC': 'FCN', 'Mn-NC': 'MnNC'}[p[2]]] = float(p[1])
GOH = {}; GOOH = {}
for line in open(os.path.join(C, 'calc_ORR_adsorption_free_energies_journal_20261025.csv'), encoding='utf-8-sig').read().splitlines()[2:]:
    p = line.split(','); GOH[{'FeCoMn-NC': 'FCM', 'FeCo-NC': 'FCN', 'Mn-NC': 'MnNC'}[p[8]]] = float(p[7])
    GOOH[{'FeCoMn-NC': 'FCM', 'FeCo-NC': 'FCN', 'Mn-NC': 'MnNC'}[p[2]]] = float(p[1])

# T029: statistics use the exact atom-resolved array used by the heatmaps.
import json
os.makedirs(OUT,exist_ok=True)
atom_rows=[];summary=[]
for k,nm in SYS[:2]:
    ds=at[at['sample']==k]
    base=ds[ds.state=='base'].set_index('atom_1based')
    for state in ADS:
        values=ds[ds.state==state].set_index('atom_1based')
        contacts=set(CONTACT[k][state])
        delta=values.occupied_d_center_eV-base.occupied_d_center_eV
        for atom,v in delta.items():
            atom_rows.append(dict(sample=k,state=state,atom=int(atom),element=base.loc[atom,'element'],covered=float(base.loc[atom,'occupied_d_center_eV']),adsorbed=float(values.loc[atom,'occupied_d_center_eV']),delta=float(v),bonded=atom in contacts))
        bonded=delta[delta.index.isin(contacts)];other=delta[~delta.index.isin(contacts)]
        above=other[other.abs()>0.1]
        summary.append(dict(sample=k,state=state,bonded_max=float(bonded.abs().max()),nonbonded_max=float(other.abs().max()),nonbonded_above_01=[int(a) for a in above.index]))
pd.DataFrame(atom_rows).to_csv(os.path.join(OUT,'atom_delta_eps_d.csv'),index=False)
with open(os.path.join(OUT,'delta_summary.json'),'w',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
# ---------- geometry ----------
LM, RM, G3 = 13.0, 3.0, 15.0
TW = acs.W - LM - RM; CW3 = (TW - 2*G3) / 3
XC = [LM + i*(CW3 + G3) for i in range(3)]
TOP = 9.0; H1, H2, H3 = 40.0, 40.0, 40.0; VG = 14.0
R = [TOP, TOP + H1 + 19.0, TOP + H1 + 19.0 + H2 + VG]   # v3: three rows, structures -> SI (Fig. S14)
H = R[2] + H3 + 12.0
cv = acs.Canvas(H)
XC3, CW3c = XC[2] + 1.5, CW3 - 1.5   # column 3 nudged right: room between colorbar name and b's y label

# ---------- a: maps ----------
CBW, CBG, CBT = 1.8, 1.8, 13.5
AW = XC[2] - G3 - CBT - CBW - CBG - LM
SG = 2.5; HB = 3.6
DR = XC[1] + CW3                  # maps span columns 1-2; b back in column 3
CBL = 0.0                         # bar right edge -> d right edge: side label room
CBX = DR - CBL - CBW              # colorbar bar left edge
AW = CBX - CBG - LM               # maps span LM .. colorbar; colorbar label ends on DR
SW = (AW - SG) / 2
SG = 5.0
SW = (AW - SG) / 2
maps = []
for i, (k, nm) in enumerate(SYS[:2]):
    ax = cv.ax(LM + i*(SW + SG), R[0] + HB, SW, H1 - HB, 'a' if i == 0 else None); maps.append(ax); ax.patch.set_visible(False)  # let OH* contact arrows overlap into the next map gap
    d = at[at['sample'] == k]
    order = (d[d.state == 'base'].assign(o=lambda t: t.element.map({'Fe': 0, 'Co': 1, 'Mn': 2}))
             .sort_values(['o', 'atom_1based']).atom_1based.tolist())
    M = np.array([[float(d[(d.state == s) & (d.atom_1based == a)].occupied_d_center_eV.iloc[0]) for s in ST] for a in order])
    full = np.full((60,4), np.nan)
    rows = [a-179 for a in order] if k == 'MnNC' else list(range(len(order)))
    if k == 'MnNC': rows=[59]
    full[rows,:] = M
    im = ax.imshow(np.ma.masked_invalid(full), aspect='auto', cmap=CMAP, vmin=VMIN, vmax=VMAX, interpolation='nearest',
                   extent=(-0.5, 3.5, 59.5, -0.5))
    el = d[d.state == 'base'].set_index('atom_1based').element; els = [el[a] for a in order]
    ticks, labs = [], []
    for e in ('Fe', 'Co', 'Mn'):
        idx = [j for j, v in enumerate(els) if v == e]
        if not idx: continue
        ticks.append((idx[0] + idx[-1]) / 2); labs.append(e)
        if idx[0] > 0: ax.axhline(idx[0] - 0.5, color='white', lw=1.0)
    for col,state in enumerate(ST):
        contact_rows=[59] if k=='MnNC' else [j for j,a in enumerate(order) if a in CONTACT[k][state]]
        groups=[]
        for j in contact_rows:
            if groups and j==groups[-1][-1]+1: groups[-1].append(j)
            else: groups.append([j])
        for group in groups:
            ax.plot(col+0.43,np.mean(group),marker='<',ms=2.6,color='black',clip_on=False,mew=0,zorder=5)
    ax.set_xlim(-0.5, 3.5); ax.set_ylim(59.5, -0.5)
    if k == 'MnNC': ticks,labs=[59],['Mn']
    ax.set_yticks(ticks); ax.set_yticklabels(labs)
    ax.tick_params(axis='y',length=0,pad=1,labelsize=8)
    for txt in ax.get_yticklabels():
        txt.set_bbox(dict(facecolor='white',edgecolor='none',pad=0.1))
    ax.set_xticks(range(4)); ax.set_xticklabels(['Covered', 'OOH*', 'O*', 'OH*'], rotation=55, ha='right', rotation_mode='anchor')
    ax.tick_params(axis='x', length=2)
    for s_ in ax.spines.values(): s_.set_linewidth(acs.LW_FRAME)
    hb = FancyBboxPatch((0, 1.0), 1, HB/(H1 - HB), boxstyle='square,pad=0', transform=ax.transAxes, clip_on=False,
                        fc='0.92', ec='black', lw=acs.LW_FRAME)
    ax.add_patch(hb); ax.text(0.5, 1.0 + HB/(H1 - HB)/2, nm, transform=ax.transAxes, ha='center', va='center')
# Each model retains its own element labels.
cbx = LM + AW + CBG
cb = cv.ax(cbx, R[0] + HB, CBW, H1 - HB, None, kind='cbar')
cbar = cv.fig.colorbar(im, cax=cb); cbar.outline.set_linewidth(acs.LW_FRAME)
cbar.set_ticks([])
cb.text(0.5, 1.03, mfmt(VMAX, 1), transform=cb.transAxes, ha='center', va='bottom', fontsize=acs.FS)
cb.text(0.5, -0.03, mfmt(VMIN, 1), transform=cb.transAxes, ha='center', va='top', fontsize=acs.FS)
cb.tick_params(length=2, pad=1.5)
cbar.set_label('Occupied ' + EPS_T + ' (eV)', labelpad=3.0)

# ---------- b: summary of a — epsilon_d of the OH*-contact metal(s) (rows marked in a) ----------
b = cv.ax(XC3, R[0], CW3c, H1, 'b'); xs = np.arange(4)   # b kept in the main figure: readable form of the triangle rows in a
for k, nm in SYS:
    ys = [EPS[(k, s)] for s in ST]
    b.plot(xs, ys, color=EDGE[k], lw=1.2, marker='o', ms=4.6, mfc=COL[k], mec=EDGE[k], mew=0.7, label=nm, zorder=3)
    print('b', k, [round(v, 3) for v in ys])
b.set_xticks(xs); b.set_xticklabels(STL, rotation=40, ha='right', rotation_mode='anchor')
b.set_xlim(-0.25, 3.25); b.set_ylim(-3.7, -1.4)
acs.frame(b, ymin=0.25); b.set_yticks([-3.5, -3.0, -2.5, -2.0]); b.set_ylim(-3.7, -1.5); b.tick_params(axis='x', which='minor', bottom=False)
b.set_ylabel('Occupied ' + EPS_T + ' (eV)', labelpad=1.0)
b.legend(loc='upper left', ncol=1, handlelength=1.4, borderaxespad=0.25)  # what the lines are (OH*-bonded metal) goes in the caption

# ---------- c, d: OH* spectra ----------
OFF = 1.25
c = cv.ax(XC[0], R[1], CW3, H2, 'c')
for i, (k, nm) in enumerate(SYS):
    dd = L(f'calc_PDOS_site_{k}_OOH'); y0 = (2 - i) * OFF; m3 = None; o2 = None
    for lab, v in dd.items():
        e = v[EK]; y = broaden(e, v[PK])
        if lab.startswith('O'): o2 = (e, y) if o2 is None else (e, o2[1] + y)   # both O atoms of OOH*
        elif int(''.join(ch for ch in lab.split()[0] if ch.isdigit())) in CONTACT[k]['OOH']: m3 = (e, y) if m3 is None else (e, m3[1] + y)
    e = m3[0]; msk = (e > -8.2) & (e < 4.2); s = max(m3[1][msk].max(), o2[1][msk].max())
    c.fill_between(e[msk], y0, y0 + m3[1][msk]/s, color=COL[k], alpha=0.55, lw=0)
    c.plot(e[msk], y0 + m3[1][msk]/s, color=EDGE[k], lw=0.7)
    c.plot(o2[0][msk], y0 + o2[1][msk]/s, color='0.15', lw=1.0, ls=(0, (3, 1.5)), zorder=4)
    if i: c.axhline(y0 + OFF, color='black', lw=0.5)
    ed = EPS[(k, 'OOH')]
    c.plot([ed, ed], [y0, y0 + OFF], color=EDGE[k], lw=1.3, ls=(0, (2.2, 1.2)), zorder=5)
    c.text(-7.7, y0 + 1.2, nm, ha='left', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.3))
    c.text(3.9, y0 + 1.2, EPS_T + ' ' + mfmt(ed), ha='right', va='top', bbox=dict(fc='white', ec='none', pad=0.3))
acs.ref(c, x=0); c.set_xlim(-8, 4); c.set_ylim(0, 3*OFF); c.set_yticks([])
acs.frame(c, xmaj=4, xmin=2)
c.set_xlabel('$E$ − $E$' + acs.sub('F') + ' (eV)'); c.set_ylabel('Normalized PDOS, OOH*')
c.legend(handles=[Patch(color='0.7', label='metal 3$d$'), Line2D([], [], color='0.15', lw=1.0, ls=(0, (3, 1.5)), label='O 2$p$')],
         loc='lower right', bbox_to_anchor=(1.02, 1.0), ncol=2, borderaxespad=0, handlelength=1.3, columnspacing=0.8)
DG2 = 2.0; DW = (CW3 - DG2) / 2   # v5: c back to one column
BOND = {('FCM', 'OOH'): 'Mn–O 1.89 Å', ('FCM', 'OH'): 'Mn–O 1.87 Å',
        ('FCN', 'OOH'): 'Fe–O 2.00, Co–O 2.08 Å', ('FCN', 'OH'): 'Fe–O 2.01, Co–O 2.29/2.24 Å',
        ('MnNC', 'OOH'): 'Mn–O 1.94 Å', ('MnNC', 'OH'): 'Mn–O 1.90 Å'}
d_ = cv.ax(XC[1], R[1], DW, H2, 'd'); d2 = cv.ax(XC[1] + DW + DG2, R[1], DW, H2, None)
for i, (k, nm) in enumerate(SYS):
    tr = {}
    for a_ in ('OOH', 'OH'):
        dd = L(f'calc_COHP_{k}_{a_}'); tot = None
        for lab, v in dd.items():
            e = v[EK]; tot = v['−pCOHP'].copy() if tot is None else tot + v['−pCOHP']
        tr[a_] = (e, tot)
    for ax, a_ in ((d_, 'OOH'), (d2, 'OH')):
        e, tot = tr[a_]; y0 = (2 - i) * OFF + 0.5
        msk = (e >= -8.0) & (e <= 1.0); sc = np.abs(tot[msk]).max() / 0.45; yy = tot[msk] / sc   # no clipping: each curve scaled to its own max in the shown window (-8..1 eV)
        ax.fill_between(e[msk], y0, y0 + yy, where=(yy > 0) & (e[msk] < 0), color=COL[k], alpha=0.55, lw=0)
        ax.plot(e[msk], y0 + yy, color=EDGE[k], lw=0.7); ax.axhline(y0, color='0.75', lw=0.5, zorder=0)
        if i: ax.axhline((2 - i) * OFF + OFF, color='black', lw=0.5)
        ax.text(0.85, (2 - i)*OFF + 1.2, ('Σ ' if k == 'FCN' else '') + f'{ICO[(k, a_)]:.2f}', ha='right', va='top', bbox=dict(fc='white', ec='none', pad=0.3))
for ax, t in ((d_, 'OOH*'), (d2, 'OH*')):
    acs.ref(ax, x=0); ax.set_xlim(-8, 1); ax.set_ylim(0, 3*OFF); ax.set_yticks([])
    acs.frame(ax, xmaj=3, xmin=1.5); ax.set_xticks([-6, -3, 0])
    ax.text(-7.6, 3*OFF - 0.06, t, ha='left', va='top', fontweight='bold', bbox=dict(fc='white', ec='none', pad=0.2), zorder=7)
    ax.set_xlabel('$E$ − $E$' + acs.sub('F') + ' (eV)')
d_.set_ylabel('Normalized −pCOHP')
cv.fig.text((XC[1] + CW3 / 2) / acs.W, 1 - (R[1] - 1.5) / H, '−ICOHP (eV)', ha='center', va='bottom', fontsize=acs.FS)   # unit of the numbers in c
# ---------- e: Bader ----------
e_ = cv.ax(XC3, R[1], CW3c, H2, 'e'); w = 0.26; xe = np.arange(2)   # OOH* and OH* only (O* dropped, 2026-11-03)
for j, (k, nm) in enumerate(SYS):
    e_.bar(xe + (j-1)*w, [DNA[(k, a_)] for a_ in ('OOH', 'OH')], w*0.9, color=COL[k], edgecolor=EDGE[k], lw=0.6, label=nm, zorder=2)
e_.set_xticks(xe); e_.set_xticklabels(['OOH*', 'OH*']); e_.set_xlim(-0.55, 1.55); e_.set_ylim(0, 0.6)
acs.frame(e_, ymaj=0.2, ymin=0.1); e_.tick_params(axis='x', which='both', bottom=False)
e_.set_yticks([0, 0.2, 0.4, 0.6]); e_.set_ylim(0, 0.6)   # no off-axis tick label
e_.set_ylabel('Bonded-metal |ΣΔ$N$| (e)')
e_.legend(loc='upper left', handlelength=1.0, handletextpad=0.4, borderaxespad=0.25)

# ---------- f, g: descriptors vs DG_OH* ----------
def scat(ax, Y, ylim, ymaj, ylab, offs):
    ax.set_xlim(0, 1.8)
    for k, nm in SYS:
        x, y = GOH[k], Y[k]
        ax.plot(x, y, 'o', ms=6.5, mfc=COL[k], mec=EDGE[k], mew=0.8, zorder=3)
        dx, dy, ha, va = offs[k]; ax.text(x + dx, y + dy, nm, ha=ha, va=va)
    ax.set_xlim(0, 1.8); ax.set_ylim(*ylim)
    acs.frame(ax, xmaj=0.5, xmin=0.25, ymaj=ymaj, ymin=ymaj/2)
    ax.set_xlabel('Δ$G$' + acs.sub('OH*') + ' (eV)'); ax.set_ylabel(ylab)
f_ = cv.ax(XC[0], R[2], CW3, H3, 'f')
charge_table = pd.read_csv(os.environ['ZY_CHARGE'])
EXC = {(k, a_): float(charge_table[(charge_table['sample'] == k) & (charge_table.state == a_)].adsorbate_electron_excess_vs_neutral.iloc[0])
       for k, _ in SYS for a_ in ('OOH', 'OH')}
xs2 = np.arange(2)
for j, (k, nm) in enumerate(SYS):
    f_.bar(xs2 + (j-1)*w, [EXC[(k, a_)] for a_ in ('OOH', 'OH')], w*0.9, color=COL[k], edgecolor=EDGE[k], lw=0.6, label=nm, zorder=2)
f_.set_xticks(xs2); f_.set_xticklabels(['OOH*', 'OH*']); f_.set_xlim(-0.55, 1.55); f_.set_ylim(0, 0.8)
acs.frame(f_, ymaj=0.2, ymin=0.1); f_.tick_params(axis='x', which='both', bottom=False)
f_.set_ylabel('Adsorbate electron excess (e)')
f_.legend(loc='upper left', handlelength=1.0, handletextpad=0.4, borderaxespad=0.25)   # legend in e as well
print('electron excess', {k: round(v, 3) for k, v in EXC.items()})
g_ = cv.ax(XC[1], R[2], CW3, H3, 'g')
# volcano: left leg U_L = dG_OH* (OH* removal limiting); right leg U_L = 4.92 - dG_OOH* with the
# OOH*/OH* scaling fitted to these three samples, dG_OOH* = dG_OH* + C (OOH* formation limiting)
C_SC = float(np.mean([GOOH[k] - GOH[k] for k, _ in SYS])); XAP = (4.92 - C_SC) / 2
print('volcano scaling C =', round(C_SC, 3), ' apex dG_OH* =', round(XAP, 3))
g_.plot([0, XAP, 4.92 - C_SC], [0, XAP, 0], color='0.6', lw=0.9, ls=(0, (3, 1.5)), zorder=1)
scat(g_, UL, (0, 1.0), 0.5, '$U$' + acs.sub('L') + ' (V vs. RHE)',
     {'FCM': (0.08, 0.0, 'left', 'center'), 'FCN': (0.06, -0.05, 'left', 'top'), 'MnNC': (-0.05, 0.05, 'left', 'bottom')})

# g: reaction schematic = the 2026-11-01 version (fig6h_OH同侧_20261101.py): axial OH on the particle side (+z),
# ORR cycle on the opposite face, no 10 A label, atom key below the scene. Same drawing scale and the same
# bottom-right region (59.27 x 52.16 mm) as in Figure_6_20261101_现行.png.
from matplotlib.patches import Circle, FancyArrowPatch
GW, GH = 1400 / 600 * 25.4, 1232 / 600 * 25.4
h = cv.ax(acs.W - GW, H - GH, GW, GH, 'h'); h.axis('off')
PPU, PX0, PY0, X0, Y0, X1, Y1 = 89.7, 3166, 3411, 2800, 2760, 4200, 3992
h.set_xlim(0.2 + (X0 - PX0) / PPU, 0.2 + (X1 - PX0) / PPU); h.set_ylim(3.05 - (Y1 - PY0) / PPU, 3.05 + (PY0 - Y0) / PPU)
AC = {'C': (0.90, 0.90, 0.90), 'N': (0.722, 0.820, 0.902), 'Fe': (0.800, 0.482, 0.525),
      'Co': (0.463, 0.588, 0.729), 'Mn': (0.843, 0.639, 0.557), 'O': (0.894, 0.318, 0.318), 'H': (1.0, 1.0, 1.0)}
def atom(x, y, r, el, z=3):
    h.add_patch(Circle((x, y), r, fc=AC[el], ec='0.25', lw=0.4, zorder=z))
YS = 7.55
h.plot([0.2, 10.4], [YS, YS], color='0.55', lw=0.8, zorder=1)
MX = 8.0
for x in np.arange(0.35, 10.3, 0.5):
    if abs(x - MX) < 0.75: continue
    atom(x, YS, 0.16, 'C', 2)
atom(MX - 0.5, YS, 0.19, 'N'); atom(MX + 0.5, YS, 0.19, 'N'); atom(MX, YS, 0.27, 'Mn', 4)
h.plot([MX, MX], [YS + 0.27, YS + 0.50], color='0.25', lw=0.6, zorder=3)
atom(MX, YS + 0.64, 0.16, 'O', 5); atom(MX + 0.27, YS + 0.84, 0.10, 'H', 5)
rows = [(YS + 0.50, 7), (YS + 0.95, 6), (YS + 1.40, 5), (YS + 1.85, 4)]
surf = []
for j, (y, n) in enumerate(rows):
    x0 = 2.7 - (n - 1) * 0.5 / 2
    for i in range(n):
        atom(x0 + i * 0.5, y, 0.24, 'Fe' if (i + j) % 2 == 0 else 'Co', 3)
    surf += [(x0 - 0.38, y + 0.10), (x0 + (n - 1) * 0.5 + 0.38, y + 0.10)]
surf = surf[2:] + [(2.45, rows[-1][0] + 0.42), (2.95, rows[-1][0] + 0.42)]
for (x, y) in surf[:8]:
    atom(x, y, 0.15, 'O', 5)
h.text(MX, YS + 1.12, 'Mn–N$_4$–OH', ha='center', va='bottom')
h.text(2.7, YS - 0.35, 'FeCo (8O*)', ha='center', va='top')
CX, CY, RC = 7.9, YS - 3.55, 1.6
HALF = 16
for lab, ang in {'O$_2$': 180, 'OOH*': 90, 'O*': 0, 'OH*': 270}.items():
    t = np.deg2rad(ang)
    h.text(CX + RC * np.cos(t), CY + RC * np.sin(t), lab, ha='center', va='center', zorder=6)
for mid in (135, 45, -45, -135):
    t0, t1 = np.deg2rad(mid + HALF), np.deg2rad(mid - HALF)
    h.add_patch(FancyArrowPatch((CX + RC * np.cos(t0), CY + RC * np.sin(t0)), (CX + RC * np.cos(t1), CY + RC * np.sin(t1)),
                                connectionstyle='arc3,rad=%.4f' % -np.tan(np.deg2rad(2 * HALF) / 4), arrowstyle='-|>',
                                mutation_scale=7, lw=0.8, color='0.3', shrinkA=0, shrinkB=0, zorder=7))
t = np.deg2rad(-135)
h.text(CX + (RC + 0.28) * np.cos(t), CY + (RC + 0.28) * np.sin(t), 'H$_2$O', ha='right', va='top')
h.plot([MX, MX], [YS - 0.27, CY + RC + 0.3], color='0.35', lw=0.6, ls=(0, (1.5, 1.2)), zorder=2)
h.legend(handles=[Line2D([], [], ls='none', marker='o', ms=4.6, mfc=AC[e], mec='0.25', mew=0.4, label=e)
                  for e in ('Fe', 'N', 'Co', 'C', 'Mn', 'H', 'O')],
         loc='upper left', bbox_to_anchor=((3160 - X0) / (X1 - X0), 1 - (3560 - Y0) / (Y1 - Y0)), ncol=4, frameon=False,
         handletextpad=0.1, columnspacing=0.6, labelspacing=0.3, borderaxespad=0.0)

# ---- column alignment: y-axis labels in each column share one left edge; panel letters sit on that edge ----
cv.fig.canvas.draw(); _r = cv.fig.canvas.get_renderer()
def _x0(a): return a.yaxis.label.get_window_extent(_r).x0
COLS = [[c, f_], [d_, g_], [e_]]
COLX = []
for axs in COLS:
    tgt = min(_x0(a) for a in axs)
    for a in axs:
        a.yaxis.set_label_coords(-0.2, 0.5); cv.fig.canvas.draw()
        wpx = a.get_window_extent(_r).width
        a.yaxis.set_label_coords(-0.2 + (tgt - _x0(a)) / wpx, 0.5)
    cv.fig.canvas.draw()
    COLX.append(tgt / cv.fig.dpi / acs.MM)
cv.letter(maps[0], 'a', x_mm=COLX[0], dy=1.6 + HB)
cv.letter(h, 'h', x_mm=COLX[2])
cv.letter(b, 'b')
for L_, ax, ci in (('c', c, 0), ('f', f_, 0), ('d', d_, 1), ('g', g_, 1), ('e', e_, 2)):
    cv.letter(ax, L_, x_mm=COLX[ci])

# ---- layout audit: overlapping text boxes (2026-11-03) ----
cv.fig.canvas.draw(); _rr = cv.fig.canvas.get_renderer()
_T = [t for t in cv.fig.findobj(lambda a: hasattr(a, 'get_text') and hasattr(a, 'get_window_extent')) if getattr(a, 'get_visible', lambda: True)() and t.get_text().strip()] if False else None
import matplotlib.text as _mt
_T = [t for t in cv.fig.findobj(_mt.Text) if t.get_visible() and t.get_text().strip()]
_B = [(t, t.get_window_extent(_rr)) for t in _T]
_n = 0
for _i in range(len(_B)):
    for _j in range(_i + 1, len(_B)):
        a, b = _B[_i][1], _B[_j][1]
        if a.overlaps(b):
            ov = (min(a.x1, b.x1) - max(a.x0, b.x0)) * (min(a.y1, b.y1) - max(a.y0, b.y0))
            if ov > 4:
                _n += 1; print('OVERLAP', repr(_B[_i][0].get_text()[:25]), '|', repr(_B[_j][0].get_text()[:25]), round(ov))
_W, _H = cv.fig.canvas.get_width_height()
for t, bb in _B:
    if bb.x0 < 0 or bb.y0 < 0 or bb.x1 > _W or bb.y1 > _H: print('OUTSIDE', repr(t.get_text()[:30]))
print('text items', len(_B), 'overlaps', _n)

print('smallest text pt:', acs.text_audit(cv.fig), ' canvas mm:', acs.W, round(H, 1))
cv.save(OUT, STEM)
import matplotlib as mpl
with mpl.rc_context({'svg.fonttype':'path'}): cv.fig.savefig(os.path.join(OUT,STEM+'_Arial_paths.svg'),facecolor='white')
cv.fig.savefig(os.path.join(OUT,STEM+'_a_preview.png'),dpi=250,bbox_inches=__import__('matplotlib').transforms.Bbox.from_extents(0, H/25.4-2.65, 120/25.4, H/25.4),facecolor='white')
with open(os.path.join(OUT, STEM + '_sources.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['sample'] + [f'eps_d_{s}' for s in ST] + [f'minus_ICOHP_{a}' for a in ADS] + [f'abs_sum_dN_bonded_{a}' for a in ADS] + ['DG_OH_eV', 'U_L_V'])
    for k, nm in SYS:
        w.writerow([nm] + [round(EPS[(k, s)], 4) for s in ST] + [round(ICO[(k, a)], 4) for a in ADS] + [round(DNA[(k, a)], 4) for a in ADS] + [round(GOH[k], 4), round(UL[k], 4)])
