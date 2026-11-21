"""FeCoMn-T044 Step 1: Update Figure 6 panel i schematic only (based on v38_axial_parentheses).
Keep panels a-h 100% pixel-identical to FeCoMn-T034/draft_20261118_v38_axial_parentheses.
Changes restricted exclusively to panel i:
- Mn protrudes above the N4 plane toward the axial OH (+z side), with Mn-N coordination lines.
- Dashed Mn outline sits in the N4 plane representing Mn pulled back upon ORR intermediate adsorption on the opposite face.
- Clear downward displacement arrow shows Mn moving back toward the N4 plane (no numeric labels).
"""
from pathlib import Path
import os, sys, json, csv
import numpy as np, pandas as pd

HERE = Path(__file__).resolve().parent
T034_DIR = HERE.parent / 'FeCoMn-T034'
if str(T034_DIR) not in sys.path:
    sys.path.insert(0, str(T034_DIR))

ROOT = Path('D:/OneDrive/Desktop/知识库/papers/FeCoMn/ACS_Catalysis_第三轮投稿')
ORIG = ROOT / 'ACS_投稿拼图_Claude重绘_20261027/Figure_6_三样品OOH_OH_20261103/v6_工作版/fig6_v6_20261103.py'
OUT = HERE
OUT.mkdir(exist_ok=True)
DATA = OUT / 'data'
DATA.mkdir(exist_ok=True)

os.environ.update(
    ZY_CALC=str(ROOT / '单图汇总_journal_20261025/10_计算_第三轮'),
    ZY_ATOM=str(ROOT / '单图汇总_journal_20261025/92_电子结构统一原参考态_20261029/atom_resolved_occupied_d_centers.csv'),
    ZY_CHARGE=str(ROOT / '电子结构系统核对_20261029/三样品九吸附态_统一口径对照.csv'),
    ZY_OUT=str(OUT),
)

source = ORIG.read_text(encoding='utf8').replace('FeCo (8O*)', 'FeCo + 8O*').replace('CY, RC = 7.9, YS - 3.55, 1.6', 'CY, RC = 7.9, YS - 2.75, 1.6')
env = {'__file__': str(ORIG), '__name__': 'original_figure_parts'}
prefix = source.split('# ---------- a: maps ----------')[0].replace('VG = 14.0', 'VG = 19.0')
exec(compile(prefix, str(ORIG), 'exec'), env)

# Reuse original lower six panels; remove bold from OOH*/OH*
retained = source.split('# ---------- c, d: OH* spectra ----------')[1].split('# ---- column alignment:')[0]
retained = retained.replace("fontweight='bold'", "fontweight='normal'")
# User amendment: panel e contains only FeCoMn-NC and Mn-NC.
e_start = retained.index('BOND =')
e_end = retained.index('# ---------- e: Bader ----------')
e_section = retained[e_start:e_end]
e_section = e_section.replace('enumerate(SYS)', 'enumerate([SYS[0], SYS[2]])')
e_section = e_section.replace('(2 - i)', '(1 - i)').replace('(2-i)', '(1-i)').replace('3*OFF', '2*OFF')
e_section = e_section.replace('OFF', 'E_OFF')
e_section = 'E_OFF = 1.6\n' + e_section
e_section = e_section.replace(' / 0.45', ' / 0.66').replace(' + 0.5', ' + 0.68')
e_section = e_section.replace('*E_OFF + 1.2', '*E_OFF + 1.55')
e_section = e_section.replace("for ax, t in ((d_, 'OOH*'), (d2, 'OH*')):",
    "    d_.text(-7.85 if k == 'FCM' else -7.6, (1 - i)*E_OFF + (0.035 if k == 'FCM' else 0.12), nm, ha='left', va='bottom', fontsize=acs.FS, zorder=8)\nfor ax, t in ((d_, 'OOH*'), (d2, 'OH*')):")
retained = retained[:e_start] + e_section + retained[e_end:]

# --- T044 panel i update: Mn out-of-plane toward axial OH + dashed in-plane pulled-back state + arrow ---
old_mn_block = (
    "atom(MX - 0.5, YS, 0.19, 'N'); atom(MX + 0.5, YS, 0.19, 'N'); atom(MX, YS, 0.27, 'Mn', 4)\n"
    "h.plot([MX, MX], [YS + 0.27, YS + 0.50], color='0.25', lw=0.6, zorder=3)\n"
    "atom(MX, YS + 0.64, 0.16, 'O', 5); atom(MX + 0.27, YS + 0.84, 0.10, 'H', 5)"
)
DZ_MN = 0.36
new_mn_block = f"""# Dashed Mn in N4 plane (pulled back upon intermediate adsorption on opposite face)
h.add_patch(Circle((MX, YS), 0.27, fc=(0.843, 0.639, 0.557, 0.25), ec='0.35', ls='--', lw=0.75, zorder=3.2))
# Mn-N bonds to out-of-plane Mn
h.plot([MX - 0.5, MX], [YS, YS + {DZ_MN}], color='0.35', lw=0.6, zorder=2.5)
h.plot([MX + 0.5, MX], [YS, YS + {DZ_MN}], color='0.35', lw=0.6, zorder=2.5)
atom(MX - 0.5, YS, 0.19, 'N', 3.6); atom(MX + 0.5, YS, 0.19, 'N', 3.6)
# Protruding Mn toward axial OH
atom(MX, YS + {DZ_MN}, 0.27, 'Mn', 4.5)
# Mn-O bond, axial O and H shifted upward with protruding Mn
h.plot([MX, MX], [YS + {DZ_MN} + 0.27, YS + {DZ_MN} + 0.50], color='0.25', lw=0.6, zorder=3)
h.plot([MX, MX + 0.27], [YS + {DZ_MN} + 0.64, YS + {DZ_MN} + 0.84], color='0.25', lw=0.6, zorder=4.5)
atom(MX, YS + {DZ_MN} + 0.64, 0.16, 'O', 5); atom(MX + 0.27, YS + {DZ_MN} + 0.84, 0.10, 'H', 5)
# Clear downward displacement arrow showing Mn pulled back toward N4 plane
h.add_patch(FancyArrowPatch((MX, YS + {DZ_MN} - 0.02), (MX, YS - 0.04),
                            arrowstyle='-|>', mutation_scale=7.0, lw=1.0, color='#1f1f1f',
                            shrinkA=0, shrinkB=0, zorder=8))"""

assert old_mn_block in retained, 'old_mn_block not found in retained script'
retained = retained.replace(old_mn_block, new_mn_block, 1)

old_label = "h.text(MX, YS + 1.12, 'Mn–N$_4$–OH', ha='center', va='bottom')"
new_label = f"h.text(MX, YS + {DZ_MN} + 1.06, 'Mn–N$_4$–OH', ha='center', va='bottom')"
assert old_label in retained, 'old_label not found'
retained = retained.replace(old_label, new_label, 1)

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
old_g.set_ylabel('Adsorbate electron gain (e)')
for item in list(old_d.texts):
    if item.get_text().startswith(EPS_T):
        item.remove()
for line in list(old_d.lines):
    xx = np.asarray(line.get_xdata())
    if xx.size == 2 and np.isclose(xx[0], xx[1]) and not np.isclose(xx[0], 0):
        line.remove()

# Keep third-column frame position and width consistent across rows 1, 2, 3
RX, RW = old_f._mm[0], old_f._mm[2]

i_height = H1
old_i.set_position([RX / acs.W, 1 - (R[2] + i_height) / cv.h, RW / acs.W, i_height / cv.h])
old_i._mm = (RX, R[2], RW, i_height)
i_zoom = 1.48
x_left, x_right = old_i.get_xlim()
y_bottom, y_top = old_i.get_ylim()
x_center, y_center = 5.35, 5.55
old_i.set_xlim(x_center - (x_right-x_left)/(2*i_zoom), x_center + (x_right-x_left)/(2*i_zoom))
old_i.set_ylim(y_center - (y_top-y_bottom)/(2*i_zoom), y_center + (y_top-y_bottom)/(2*i_zoom))

i_factor = RW / env['GW'] * i_zoom
for text_item in old_i.texts:
    text_item.set_fontsize(text_item.get_fontsize() * i_factor)
for legend_item in old_i.findobj(__import__('matplotlib').legend.Legend):
    legend_item.set_bbox_to_anchor((0.5, 2.35), transform=old_i.transData)
    for text_item in legend_item.get_texts():
        text_item.set_fontsize(text_item.get_fontsize() * i_factor)
    for handle in legend_item.legend_handles:
        if hasattr(handle, 'get_markersize'):
            handle.set_markersize(handle.get_markersize() * i_factor)
    fig.canvas.draw()
    representative_radii = {'Fe': 0.24, 'Co': 0.24, 'Mn': 0.27, 'O': 0.16, 'N': 0.19, 'C': 0.16, 'H': 0.10}
    for atom_handle, atom_text in zip(legend_item.legend_handles, legend_item.get_texts()):
        atom_radius = representative_radii[atom_text.get_text()]
        atom_left = old_i.transData.transform((0, 0))
        atom_right = old_i.transData.transform((2 * atom_radius, 0))
        atom_handle.set_markersize(abs(atom_right[0] - atom_left[0]) * 72 / fig.dpi)

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
    p = T034_DIR.parent / 'FeCoMn-T033/draft_20261118_v1/data' / f'a_{sample}_axial.csv'
    d = pd.read_csv(p)
    axial[sample] = (d.E_minus_EF_eV.to_numpy(), d.minus_pCOHP.to_numpy())

scales = []
for i, (s, nm) in enumerate([SYS[0], SYS[2]]):
    x, y = axial[s]
    mask = (x >= -8.0) & (x <= 1.0)
    scale = np.abs(y[mask]).max() / 0.62
    yy = y[mask] / scale
    y0 = (1 - i) * 1.25 + 0.64
    a.fill_between(x[mask], y0, y0 + yy, where=(yy > 0) & (x[mask] < 0), color=COL[s], alpha=0.55, lw=0)
    a.plot(x[mask], y0 + yy, color=EDGE[s], lw=0.7)
    a.axhline(y0, color='0.75', lw=0.5, zorder=0)
    if i:
        a.axhline(1.25, color='black', lw=0.5)
    left_lbl = f"{nm} ({'Mn–OH' if s == 'FCM' else 'Mn=O'})"
    icohp_lbl = '2.64' if s == 'FCM' else '8.03'
    a.text(-7.65, y0 + 0.55, left_lbl, ha='left', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.2))
    a.text(0.85, y0 + 0.55, icohp_lbl, ha='right', va='top', zorder=6, bbox=dict(fc='white', ec='none', pad=0.2))
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
csvout('a_display_scale.csv', ['sample', 'raw_divisor'], scales)

# ---------- b: spin-resolved Mn 3d PDOS before adsorption ----------
spin = json.loads((T034_DIR / 'data/background_spin_PDOS.json').read_text())
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
    b.annotate('', xy=(-7.65, y0 + 0.54), xytext=(-7.65, y0 + 0.10), arrowprops=dict(arrowstyle='->', color='0.15', lw=0.95, mutation_scale=9), zorder=6)
    b.annotate('', xy=(-7.65, y0 - 0.54), xytext=(-7.65, y0 - 0.10), arrowprops=dict(arrowstyle='->', color='0.15', lw=0.95, mutation_scale=9), zorder=6)
    csvout(f'b_{s}_Mn_spin.csv', ['E_minus_EF_eV', 'Mn_d_up_raw', 'Mn_d_down_raw', 'Mn_d_up_broadened', 'Mn_d_down_broadened'],
           zip(x, up_raw, down_raw, up, down))

acs.ref(b, x=0)
b.set_xlim(-8, 4)
b.set_ylim(0, 3.6)
b.set_yticks([])
acs.frame(b, xmaj=4, xmin=2)
b.set_xlabel('$E$ − $E$' + acs.sub('F') + ' (eV)')
b.set_ylabel('Spin-resolved PDOS')

# ---------- c: reaction-site metal 3d PDOS before adsorption ----------
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
csvout('c_centroids.csv', ['sample', 'selected_atoms', 'occupied_d_center_atom_mean_eV'],
       [[s, '238' if s == 'FCM' else ('206;234;235' if s == 'FCN' else '179'), env['EPS'][s, 'base']] for s, _ in SYS])

for axis, xx, ww in [(c, XC[0], CW), (a, XC[1], CW), (b, RX, RW)]:
    axis.set_position([xx / acs.W, 1 - (R[0] + H1) / cv.h, ww / acs.W, H1 / cv.h])
    axis._mm = (xx, R[0], ww, H1)
for axis, heading in [(old_e1, 'OOH*'), (old_e2, 'OH*')]:
    for item in list(axis.texts):
        text_value = item.get_text()
        if text_value in ('OOH*', 'OH*'):
            item.remove()
        elif text_value in ('FeCoMn–NC', 'Mn–NC'):
            row = 1 if text_value == 'FeCoMn–NC' else 0
            item.set_position((-7.6, row * 1.6 + 1.55))
            item.set_verticalalignment('top')
        elif text_value in ('3.12', '3.06', '2.65', '2.72'):
            row = 1 if text_value in ('3.12', '3.06') else 0
            item.set_position((-7.6, row * 1.6 + 0.12))
            item.set_horizontalalignment('left')
            item.set_verticalalignment('bottom')
    axis.set_title(heading, fontsize=acs.FS, fontweight='normal', pad=3)
for item in fig.texts:
    if item.get_text() == '−ICOHP (eV)':
        item.remove()

import matplotlib.text as _text_module
for text_item in fig.findobj(_text_module.Text):
    if text_item.get_text().strip():
        text_item.set_fontfamily('Arial')
        text_item.set_fontsize(8)
        text_item.set_fontweight('normal')

from matplotlib.patches import Rectangle
orr_label_x = 2.7
square_width = 1.72
pixel_x = old_i.transData.transform((1, 0))[0] - old_i.transData.transform((0, 0))[0]
pixel_y = old_i.transData.transform((0, 1))[1] - old_i.transData.transform((0, 0))[1]
square_height = square_width * abs(pixel_x / pixel_y)
old_i.add_patch(Rectangle((orr_label_x - square_width/2, env['CY'] - square_height/2),
                         square_width, square_height, facecolor='none', edgecolor='none', zorder=8))
old_i.text(orr_label_x, env['CY'], 'ORR', ha='center', va='center',
           fontsize=8, fontfamily='Arial', fontweight='bold', color='black', zorder=9)

# Keep Mn-NC label nudge in panel h identical to v38
for label_item in old_h.texts:
    if label_item.get_text() == 'Mn–NC':
        old_x, old_y = label_item.get_position()
        label_item.set_position((old_x - 0.025, old_y + 0.010))

for atom_legend in old_i.findobj(__import__('matplotlib').legend.Legend):
    atom_legend.set_frame_on(False)
    atom_legend.get_frame().set_facecolor('white')
    atom_legend.get_frame().set_edgecolor('0.65')
    atom_legend.get_frame().set_linewidth(0.6)
    atom_legend.get_frame().set_alpha(1)
    atom_legend.get_frame().set_boxstyle('square', pad=0.25)

fig.canvas.draw()
rr = fig.canvas.get_renderer()
column_groups = [[c, old_d, old_g], [a, old_e1, old_h], [b, old_f]]
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

for lab, z, col in [('a', c, 0), ('b', a, 1), ('c', b, 2), ('d', old_d, 0), ('e', old_e1, 1), ('f', old_f, 2), ('g', old_g, 0), ('h', old_h, 1), ('i', old_i, 2)]:
    cv.letter(z, lab, x_mm=targets[col])

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

fig.savefig(OUT / 'Figure6_T044_600dpi.png', dpi=600, facecolor='white')
fig.savefig(OUT / 'Figure6_T044_preview.png', dpi=300, facecolor='white')
fig.savefig(OUT / 'Figure6_T044.pdf', facecolor='white')
acs.plt.rcParams['svg.fonttype'] = 'none'
fig.savefig(OUT / 'Figure6_T044_editable.svg', facecolor='white')
acs.plt.rcParams['svg.fonttype'] = 'path'
fig.savefig(OUT / 'Figure6_T044_Arial_paths.svg', facecolor='white')
print('SAVED T044 Figure 6 to', OUT)
