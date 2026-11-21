"""T034 v2 (reading commit 7448e41): 3x3 nine-panel Figure 6 matching Fig6_layout_preview_20261118.png.
Fixes from v1:
1. Apply identical Gaussian broadening (sigma=0.10 eV, same broaden() as panel d) to panels b and c.
2. Match preview labels in panel a ('FeCoMn–NC  Mn–OH' / 'Mn–NC  Mn=O' on left; '2.64' & '1.88 Å' / '8.03' & '1.58 Å' on right) so labels do not cover bonding peaks.
3. Italicize 3d in panel b/c titles ('Mn 3$d$ before adsorption', 'Metal 3$d$ before adsorption') and subscript B in mu_B.
4. Prevent epsilon_d dashed line in panel c from overlapping 'FeCoMn–NC' label.
5. Fit panel i schematic & element legend cleanly inside column 3 without clipping 'O' on the right edge.
"""
from pathlib import Path
import os, sys, json, csv, hashlib
import numpy as np, pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = Path('D:/OneDrive/Desktop/知识库/papers/FeCoMn/ACS_Catalysis_第三轮投稿')
ORIG = ROOT / 'ACS_投稿拼图_Claude重绘_20261027/Figure_6_三样品OOH_OH_20261103/v6_工作版/fig6_v6_20261103.py'
OUT = HERE / 'draft_20261118_v2'
OUT.mkdir(exist_ok=True)
DATA = HERE / 'data'
DATA.mkdir(exist_ok=True)

os.environ.update(
    ZY_CALC=str(ROOT / '单图汇总_journal_20261025/10_计算_第三轮'),
    ZY_ATOM=str(ROOT / '单图汇总_journal_20261025/92_电子结构统一原参考态_20261029/atom_resolved_occupied_d_centers.csv'),
    ZY_CHARGE=str(ROOT / '电子结构系统核对_20261029/三样品九吸附态_统一口径对照.csv'),
    ZY_OUT=str(OUT),
)

source = ORIG.read_text(encoding='utf8')
env = {'__file__': str(ORIG), '__name__': 'original_figure_parts'}
prefix = source.split('# ---------- a: maps ----------')[0].replace('VG = 14.0', 'VG = 19.0')
exec(compile(prefix, str(ORIG), 'exec'), env)

# Reuse original lower six panels (c, d_, d2, e_, f_, g_, h -> d, e, f, g, h, i); remove bold from OOH*/OH*
retained = source.split('# ---------- c, d: OH* spectra ----------')[1].split('# ---- column alignment:')[0]
retained = retained.replace("fontweight='bold'", "fontweight='normal'")
exec(compile(retained, str(ORIG), 'exec'), env)

acs = env['acs']
cv = env['cv']
fig = cv.fig
COL, EDGE, SYS = env['COL'], env['EDGE'], env['SYS']
L = env['L']
EK, PK = env['EK'], env['PK']
EPS_T = env['EPS_T']
broaden = env['broaden']
XC, CW, R, H1 = env['XC'], env['CW3'], env['R'], env['H1']

old_d, old_e1, old_e2, old_f, old_g, old_h, old_i = [env[k] for k in ['c', 'd_', 'd2', 'e_', 'f_', 'g_', 'h']]

# Keep third-column frame position and width consistent across rows 1, 2, 3
RX, RW = old_f._mm[0], old_f._mm[2]

# Fit panel i cleanly into column 3 row 3 so the right-most legend item 'O' is never clipped outside canvas
old_i.set_position([(RX - 1.5) / acs.W, 1 - (R[2] + H1 + 4.5) / cv.h, (RW + 1.5) / acs.W, (H1 + 4.5) / cv.h])
old_i._mm = (RX, R[2], RW, H1)
old_i.set_xlim(-3.7, 12.1)
for leg in old_i.findobj(__import__('matplotlib').legend.Legend):
    leg.set_bbox_to_anchor((0.14, 0.21))

a = cv.ax(XC[0], R[0], CW, H1, 'a')
b = cv.ax(XC[1], R[0], CW, H1, 'b')
c = cv.ax(RX, R[0], RW, H1, 'c')

def csvout(name, headers, rows):
    with (DATA / name).open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)

# ---------- a: axial bond -pCOHP (FeCoMn-NC Mn-OH vs Mn-NC Mn=O) ----------
axial = {}
for sample in ['FCM', 'MnNC']:
    p = HERE.parent / 'FeCoMn-T033/draft_20261118_v1/data' / f'a_{sample}_axial.csv'
    d = pd.read_csv(p)
    axial[sample] = (d.E_minus_EF_eV.to_numpy(), d.minus_pCOHP.to_numpy())

scales = []
for i, (s, nm) in enumerate([SYS[0], SYS[2]]):
    x, y = axial[s]
    mask = (x >= -8.0) & (x <= 1.0)
    scale = np.abs(y[mask]).max() / 0.45
    yy = y[mask] / scale
    y0 = (1 - i) * 1.25 + 0.5
    a.fill_between(x[mask], y0, y0 + yy, where=(yy > 0) & (x[mask] < 0), color=COL[s], alpha=0.55, lw=0)
    a.plot(x[mask], y0 + yy, color=EDGE[s], lw=0.7)
    a.axhline(y0, color='0.75', lw=0.5, zorder=0)
    if i:
        a.axhline(1.25, color='black', lw=0.5)
    left_lbl = f"{nm}  {'Mn–OH' if s == 'FCM' else 'Mn=O'}"
    icohp_lbl = '2.64' if s == 'FCM' else '8.03'
    dist_lbl = '1.88 Å' if s == 'FCM' else '1.58 Å'
    a.text(-7.65, y0 + 0.68, left_lbl, ha='left', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.2))
    a.text(0.85, y0 + 0.68, icohp_lbl, ha='right', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.2))
    a.text(0.85, y0 + 0.36, dist_lbl, ha='right', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.15))
    scales.append([s, scale])
    csvout(f'a_{s}_axial.csv', ['E_minus_EF_eV', 'raw_minus_pCOHP'], zip(x, y))

acs.ref(a, x=0)
a.set_xlim(-8, 1)
a.set_ylim(0, 2.5)
a.set_yticks([])
acs.frame(a, xmaj=3, xmin=1.5)
a.set_xticks([-6, -3, 0])
a.set_xlabel('$E$ − $E$' + acs.sub('F') + ' (eV)')
a.set_ylabel('Normalized −pCOHP')
a.set_title('Axial bond, −ICOHP (eV)', pad=3, fontsize=acs.FS)
csvout('a_display_scale.csv', ['sample', 'raw_divisor'], scales)

# ---------- b: spin-resolved Mn 3d PDOS before adsorption (with Gaussian broadening sigma=0.10 eV) ----------
spin = json.loads((DATA / 'background_spin_PDOS.json').read_text())
for i, item in enumerate(spin):
    s = item['sample']
    x = np.array(item['E_minus_EF'])
    up_raw = np.array(item['d_up'])
    down_raw = np.array(item['d_down'])
    up = broaden(x, up_raw)
    down = broaden(x, down_raw)
    mask = (x > -8.2) & (x < 4.2)
    scale = max(up[mask].max(), down[mask].max()) / 0.62
    y0 = (1 - i) * 1.8 + 0.9
    b.fill_between(x[mask], y0, y0 + up[mask] / scale, color=COL[s], alpha=0.55, lw=0)
    b.fill_between(x[mask], y0, y0 - down[mask] / scale, color=COL[s], alpha=0.55, lw=0)
    b.plot(x[mask], y0 + up[mask] / scale, color=EDGE[s], lw=0.7)
    b.plot(x[mask], y0 - down[mask] / scale, color=EDGE[s], lw=0.7)
    b.axhline(y0, color='0.75', lw=0.5, zorder=0)
    if i:
        b.axhline(1.8, color='black', lw=0.5)
    b.text(-7.7, y0 + 0.84, dict(SYS)[s], ha='left', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.2))
    b.text(3.9, y0 + 0.84, r'$\mu_{\mathrm{Mn}}$ ' + f"{item['Mn_moment']:.2f}" + r' $\mu_{\mathrm{B}}$',
           ha='right', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.2))
    b.text(-7.75, y0 + 0.22, '↑', color='0.45', zorder=6)
    b.text(-7.75, y0 - 0.52, '↓', color='0.45', zorder=6)
    csvout(f'b_{s}_Mn_spin.csv', ['E_minus_EF_eV', 'Mn_d_up_raw', 'Mn_d_down_raw', 'Mn_d_up_broadened', 'Mn_d_down_broadened'],
           zip(x, up_raw, down_raw, up, down))

acs.ref(b, x=0)
b.set_xlim(-8, 4)
b.set_ylim(0, 3.6)
b.set_yticks([])
acs.frame(b, xmaj=4, xmin=2)
b.set_xlabel('$E$ − $E$' + acs.sub('F') + ' (eV)')
b.set_ylabel('Spin-resolved PDOS')
b.set_title('Mn 3$d$ before adsorption', pad=3, fontsize=acs.FS)

# ---------- c: reaction-site metal 3d PDOS before adsorption (with Gaussian broadening sigma=0.10 eV) ----------
OFF = 1.25
for i, (s, nm) in enumerate(SYS):
    if s in ['FCM', 'MnNC']:
        item = next(z for z in spin if z['sample'] == s)
        x = np.array(item['E_minus_EF'])
        y_raw = np.array(item['d_up']) + np.array(item['d_down'])
        y = broaden(x, y_raw)
        indices = [item['Mn_index']]
    else:
        dd = L('calc_PDOS_FCN_base')
        y_raw = None
        indices = []
        for lab, v in dd.items():
            if '3d' not in lab:
                continue
            idx = int(''.join(q for q in lab.split()[0] if q.isdigit()))
            if idx not in [206, 234, 235]:
                continue
            x = v[EK]
            y_raw = v[PK].copy() if y_raw is None else y_raw + v[PK]
            indices.append(idx)
        assert sorted(indices) == [206, 234, 235]
        y = broaden(x, y_raw)
    mask = (x > -8.2) & (x < 4.2)
    y0 = (2 - i) * OFF
    scale = y[mask].max() / 0.92
    c.fill_between(x[mask], y0, y0 + y[mask] / scale, color=COL[s], alpha=0.55, lw=0)
    c.plot(x[mask], y0 + y[mask] / scale, color=EDGE[s], lw=0.7)
    if i:
        c.axhline(y0 + OFF, color='black', lw=0.5)
    ed = env['EPS'][s, 'base']
    c.plot([ed, ed], [y0, y0 + (0.80 if s == 'FCM' else 0.90)], color=EDGE[s], lw=1.3, ls=(0, (2.2, 1.2)), zorder=5)
    c.text(-7.7, y0 + 1.2, nm, ha='left', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.3))
    c.text(3.9, y0 + 1.2, EPS_T + ' ' + env['mfmt'](ed), ha='right', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.3))
    csvout(f'c_{s}_metal_d.csv', ['E_minus_EF_eV', 'selected_d_sum_raw', 'selected_d_sum_broadened'], zip(x, y_raw, y))

acs.ref(c, x=0)
c.set_xlim(-8, 4)
c.set_ylim(0, 3 * OFF)
c.set_yticks([])
acs.frame(c, xmaj=4, xmin=2)
c.set_xlabel('$E$ − $E$' + acs.sub('F') + ' (eV)')
c.set_ylabel('Normalized PDOS')
c.set_title('Metal 3$d$ before adsorption', pad=3, fontsize=acs.FS)
csvout('c_centroids.csv', ['sample', 'selected_atoms', 'occupied_d_center_atom_mean_eV'],
       [[s, '238' if s == 'FCM' else ('206;234;235' if s == 'FCN' else '179'), env['EPS'][s, 'base']] for s, _ in SYS])

# ---------- column alignment & panel letters ----------
fig.canvas.draw()
rr = fig.canvas.get_renderer()
column_groups = [[a, old_d, old_g], [b, old_e1, old_h], [c, old_f]]
targets = []
for group in column_groups:
    target = min(z.yaxis.label.get_window_extent(rr).x0 for z in group)
    for z in group:
        lab = z.yaxis.label
        position = lab.get_transform().transform(lab.get_position())
        xx = z.transAxes.inverted().transform(position)[0]
        delta = (target - lab.get_window_extent(rr).x0) / z.get_window_extent(rr).width
        z.yaxis.set_label_coords(xx + delta, 0.5)
    fig.canvas.draw()
    targets.append(target / fig.dpi / acs.MM)

for lab, z, col in [('a', a, 0), ('b', b, 1), ('c', c, 2), ('d', old_d, 0), ('e', old_e1, 1), ('f', old_f, 2), ('g', old_g, 0), ('h', old_h, 1), ('i', old_i, 2)]:
    cv.letter(z, lab, x_mm=targets[col])

# Check text overlaps and bounds
fig.canvas.draw()
rr = fig.canvas.get_renderer()
import matplotlib.text as _mt
_T = [t for t in fig.findobj(_mt.Text) if t.get_visible() and t.get_text().strip()]
_B = [(t, t.get_window_extent(rr)) for t in _T]
_n = 0
for _i in range(len(_B)):
    for _j in range(_i + 1, len(_B)):
        ba, bb = _B[_i][1], _B[_j][1]
        if ba.overlaps(bb):
            ov = (min(ba.x1, bb.x1) - max(ba.x0, bb.x0)) * (min(ba.y1, bb.y1) - max(ba.y0, bb.y0))
            if ov > 4:
                _n += 1
                print('OVERLAP', repr(_B[_i][0].get_text()[:25]), '|', repr(_B[_j][0].get_text()[:25]), round(ov))
_W, _H = fig.canvas.get_width_height()
_out = 0
for t, bb in _B:
    if bb.x0 < 0 or bb.y0 < 0 or bb.x1 > _W or bb.y1 > _H:
        _out += 1
        print('OUTSIDE', repr(t.get_text()[:30]), bb.x0, bb.y0, bb.x1, bb.y1, 'canvas:', _W, _H)
print('text items:', len(_B), 'overlaps:', _n, 'outside:', _out)

fig.savefig(OUT / 'Figure6_T034_600dpi.png', dpi=600, facecolor='white')
fig.savefig(OUT / 'Figure6_T034_preview.png', dpi=300, facecolor='white')
fig.savefig(HERE / 'Figure6_draft.png', dpi=300, facecolor='white')
fig.savefig(OUT / 'Figure6_T034.pdf', facecolor='white')
acs.plt.rcParams['svg.fonttype'] = 'none'
fig.savefig(OUT / 'Figure6_T034_editable.svg', facecolor='white')
acs.plt.rcParams['svg.fonttype'] = 'path'
fig.savefig(OUT / 'Figure6_T034_Arial_paths.svg', facecolor='white')
print('SAVED T034 v2 to', OUT)
