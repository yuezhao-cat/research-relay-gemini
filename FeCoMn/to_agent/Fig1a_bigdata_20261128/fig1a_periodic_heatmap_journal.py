#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fig1a_periodic_heatmap_journal.py  —  2026-11-28
Figure 1(a): Periodic Table Heatmap — median alkaline ORR E1/2 by metal element
Data: ORR.xlsx (1,484 records; Li Hao group)
Preset: journal / ACS Catalysis, double-column 177.8 mm, Arial 8 pt

Outputs (all in OUTDIR):
  fig1a_periodic_heatmap_journal_YYYYMMDD_HHMM.pdf
  fig1a_periodic_heatmap_journal_YYYYMMDD_HHMM.png  (600 dpi)
  fig1a_periodic_heatmap_data_YYYYMMDD_HHMM.csv
  fig1a_periodic_heatmap_journal.py  (this script, copied)
"""
import os, re, shutil, sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib.cm as cm
from datetime import datetime

# ─── Paths ───────────────────────────────────────────────────────────────────
XLSX = (r'D:\OneDrive\Desktop\知识库\papers\FeCoMn'
        r'\ACS_Catalysis_第三轮投稿\全文_20261031_主线重写\ORR.xlsx')
OUTDIR = (r'D:\OneDrive\Desktop\知识库\papers\FeCoMn'
          r'\ACS_Catalysis_第三轮投稿\全文_20261031_主线重写\Fig1_bigdata_20261128')
os.makedirs(OUTDIR, exist_ok=True)
TS = datetime.now().strftime('%Y%m%d_%H%M')

# ─── Style ───────────────────────────────────────────────────────────────────
matplotlib.rcParams.update({
    'font.family': 'Arial',
    'font.size': 8,
    'axes.unicode_minus': True,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'savefig.dpi': 600,
    'figure.dpi': 150,
    'axes.linewidth': 0.8,
})

# ─── Periodic table: element → (period, group) 1-indexed ────────────────────
ELEM_POS = {
    'H':(1,1),  'He':(1,18),
    'Li':(2,1), 'Be':(2,2),
    'B':(2,13), 'C':(2,14), 'N':(2,15), 'O':(2,16), 'F':(2,17), 'Ne':(2,18),
    'Na':(3,1), 'Mg':(3,2),
    'Al':(3,13),'Si':(3,14),'P':(3,15), 'S':(3,16), 'Cl':(3,17),'Ar':(3,18),
    'K':(4,1),  'Ca':(4,2),
    'Sc':(4,3), 'Ti':(4,4), 'V':(4,5),  'Cr':(4,6), 'Mn':(4,7), 'Fe':(4,8),
    'Co':(4,9), 'Ni':(4,10),'Cu':(4,11),'Zn':(4,12),
    'Ga':(4,13),'Ge':(4,14),'As':(4,15),'Se':(4,16),'Br':(4,17),'Kr':(4,18),
    'Rb':(5,1), 'Sr':(5,2),
    'Y':(5,3),  'Zr':(5,4), 'Nb':(5,5), 'Mo':(5,6), 'Tc':(5,7), 'Ru':(5,8),
    'Rh':(5,9), 'Pd':(5,10),'Ag':(5,11),'Cd':(5,12),
    'In':(5,13),'Sn':(5,14),'Sb':(5,15),'Te':(5,16),'I':(5,17), 'Xe':(5,18),
    'Cs':(6,1), 'Ba':(6,2),
    'Lu':(6,3), 'Hf':(6,4), 'Ta':(6,5), 'W':(6,6),  'Re':(6,7), 'Os':(6,8),
    'Ir':(6,9), 'Pt':(6,10),'Au':(6,11),'Hg':(6,12),
    'Tl':(6,13),'Pb':(6,14),'Bi':(6,15),'Po':(6,16),'At':(6,17),'Rn':(6,18),
    # Lanthanides row (shown at bottom, row index 7.8)
    'La':(8,3), 'Ce':(8,4), 'Pr':(8,5), 'Nd':(8,6), 'Pm':(8,7), 'Sm':(8,8),
    'Eu':(8,9), 'Gd':(8,10),'Tb':(8,11),'Dy':(8,12),'Ho':(8,13),'Er':(8,14),
    'Tm':(8,15),'Yb':(8,16),
}

# Element categories
NON_METALS = {'H','C','N','O','F','P','S','Cl','Se','Br','I','Te','At'}
NOBLE_GAS  = {'He','Ne','Ar','Kr','Xe','Rn'}
METALLOIDS = {'B','Si','Ge','As','Sb','Po'}
METALS     = set(ELEM_POS.keys()) - NON_METALS - NOBLE_GAS - METALLOIDS

# ─── Load & process data ─────────────────────────────────────────────────────
df = pd.read_excel(XLSX)
print(f"Loaded {len(df)} rows")

def parse_el(s):
    if pd.isna(s): return []
    return [x.strip() for x in str(s).split(',')
            if re.match(r'^[A-Z][a-z]?$', x.strip())]

df['_els'] = df['Elements'].apply(parse_el)
df['_e12'] = pd.to_numeric(df['Half-wave Potential (V/RHE)'], errors='coerce')

def is_alk(row):
    e = str(row.get('Electrolytes', '')).lower()
    return 'koh' in e or 'naoh' in e

df['_alk'] = df.apply(is_alk, axis=1)
df_alk = df[df['_alk'] & df['_e12'].notna()].copy()

# Per-element stats (alkaline, metals only)
el_vals = {}
for _, row in df_alk.iterrows():
    for el in row['_els']:
        if el in METALS:
            el_vals.setdefault(el, []).append(row['_e12'])

el_stats = {el: {'n': len(v), 'median': float(np.median(v)), 'max': float(np.max(v))}
            for el, v in el_vals.items()}

# Save data CSV
rows_csv = []
for el, s in el_stats.items():
    p, g = ELEM_POS.get(el, (None, None))
    rows_csv.append({'Element': el, 'Period': p, 'Group': g,
                     'n_alkaline': s['n'],
                     'median_E12_V': round(s['median'], 4),
                     'max_E12_V': round(s['max'], 4)})
pd.DataFrame(rows_csv).sort_values('n_alkaline', ascending=False).to_csv(
    os.path.join(OUTDIR, f'fig1a_periodic_heatmap_data_{TS}.csv'),
    index=False, encoding='utf-8-sig')

# ─── Colormap & normalization ────────────────────────────────────────────────
# FeCoMn paper PAL8: light lavender → warm gray → peach → deep pink-red
# Low E1/2 = cool purple, High E1/2 = warm deep pink (matches paper palette)
PAL8 = ["#b6b3d6", "#d0cce5", "#d5d3df", "#d6d1d1", "#f7dfd7", "#f6b3a0", "#f1837b", "#eb687b"]
CMAP = LinearSegmentedColormap.from_list('orr_e12_pal8', PAL8, N=512)
VMIN, VMAX = 0.70, 0.90
NORM = Normalize(vmin=VMIN, vmax=VMAX)

# ─── Figure layout ───────────────────────────────────────────────────────────
# ACS Catalysis double column: 177.8 mm
FIG_W_MM = 177.8
FIG_W_IN = FIG_W_MM / 25.4  # 7.0 inches

# Periodic table occupies left ~82% of figure; colorbar right ~8%
TABLE_FRAC  = 0.82
CBAR_FRAC   = 0.07
GAP_FRAC    = 0.03  # gap between table and colorbar
LMARGIN_FRAC = 0.02  # left margin

# In "table" coordinate: x=group (1-18), y=row (0=top=period1, downward)
# Period row mapping: periods 1-6 → rows 0-5; gap → 0.4; lanthanides → row 6.4
PERIOD_ROW = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 8: 6.5}
X_RANGE = (0.3, 18.7)
Y_RANGE = (-0.3, 7.5)
ASPECT = (X_RANGE[1]-X_RANGE[0]) / (Y_RANGE[1]-Y_RANGE[0])

TABLE_W = TABLE_FRAC * FIG_W_IN
TABLE_H = TABLE_W / ASPECT
FIG_H_IN = TABLE_H + 0.25  # small top/bottom margin

fig = plt.figure(figsize=(FIG_W_IN, FIG_H_IN))

# Table axis (left)
ax = fig.add_axes([
    LMARGIN_FRAC,                      # left
    0.03,                              # bottom
    TABLE_FRAC,                        # width
    0.95                               # height
])
ax.set_xlim(*X_RANGE)
ax.set_ylim(Y_RANGE[1], Y_RANGE[0])   # y increases downward
ax.axis('off')

# Colorbar axis (right)
ax_cb = fig.add_axes([
    LMARGIN_FRAC + TABLE_FRAC + GAP_FRAC,  # left
    0.15,                                   # bottom
    CBAR_FRAC,                              # width
    0.70                                    # height
])

# ─── This paper's value annotation ───────────────────────────────────────────
THIS_PAPER_E12 = 0.885  # FeCoMn-NC alkaline

# ─── Paper highlight elements ─────────────────────────────────────────────────
HIGHLIGHT = {'Fe', 'Co', 'Mn'}
HIGHLIGHT_EC = '#5c506f'  # DEEP tone from FeCoMn paper (Co color / CDD outline)

# ─── Draw cells ───────────────────────────────────────────────────────────────
CW = 1.0   # cell width in data units
CH = 0.90  # cell height in data units

for el, (period, group) in ELEM_POS.items():
    if period not in PERIOD_ROW:
        continue
    row_y = PERIOD_ROW[period]
    x0 = group - 0.5 * CW
    y0 = row_y - 0.5 * CH

    # Cell appearance
    if el in el_stats:
        stat = el_stats[el]
        fc = CMAP(NORM(stat['median']))
        brightness = 0.299*fc[0] + 0.587*fc[1] + 0.114*fc[2]
        txt_color = 'white' if brightness < 0.60 else '#2a1a2a'
        cnt_color = 'white' if brightness < 0.60 else '#5c506f'
        ec_color  = HIGHLIGHT_EC if el in HIGHLIGHT else '#888888'
        lw        = 1.6 if el in HIGHLIGHT else 0.5
        alpha     = 1.0
    elif el in METALS:
        fc = '#CBCBCB'
        txt_color = '#888888'
        cnt_color = '#AAAAAA'
        ec_color  = HIGHLIGHT_EC if el in HIGHLIGHT else '#AAAAAA'
        lw        = 1.6 if el in HIGHLIGHT else 0.3
        alpha     = 1.0
    elif el in NON_METALS:
        fc = '#F2F2F2'
        txt_color = '#C0C0C0'
        cnt_color = '#C0C0C0'
        ec_color  = '#E0E0E0'
        lw        = 0.3
        alpha     = 0.6
    elif el in NOBLE_GAS:
        fc = '#F7F4FA'
        txt_color = '#C8C0D0'
        cnt_color = '#C8C0D0'
        ec_color  = '#E0D8E8'
        lw        = 0.3
        alpha     = 0.6
    else:  # metalloids, others
        fc = '#EAEAE0'
        txt_color = '#B0B0A0'
        cnt_color = '#B0B0A0'
        ec_color  = '#CCCCCC'
        lw        = 0.3
        alpha     = 0.6

    rect = mpatches.FancyBboxPatch(
        (x0 + 0.04, y0 + 0.04), CW - 0.08, CH - 0.08,
        boxstyle='round,pad=0.02',
        facecolor=fc, edgecolor=ec_color,
        linewidth=lw, alpha=alpha, zorder=2
    )
    ax.add_patch(rect)

    # Element symbol
    has_data = el in el_stats
    sym_fontsize = 7.5 if has_data else 6.0
    sym_fontweight = 'bold' if el in HIGHLIGHT else ('semibold' if has_data else 'normal')
    ax.text(group, row_y - 0.08 if has_data else row_y,
            el, ha='center', va='center',
            fontsize=sym_fontsize, fontfamily='Arial',
            fontweight=sym_fontweight,
            color=txt_color, zorder=3)

    # Record count (small text below symbol for metals with data)
    if has_data:
        stat = el_stats[el]
        ax.text(group, row_y + 0.30,
                f"n={stat['n']}",
                ha='center', va='center',
                fontsize=5.0, fontfamily='Arial',
                color=cnt_color, zorder=3)

# ─── "*" annotation for lanthanide placeholder cell (period 6, group 3) ──────
ax.text(3, PERIOD_ROW[6], '*', ha='center', va='center',
        fontsize=7, color='#888888', zorder=3)
ax.text(3, PERIOD_ROW[8], '*', ha='center', va='center',
        fontsize=7, color='#888888', zorder=3)

# ─── Colorbar ────────────────────────────────────────────────────────────────
sm = cm.ScalarMappable(norm=NORM, cmap=CMAP)
sm.set_array([])
cbar = fig.colorbar(sm, cax=ax_cb, orientation='vertical')
cbar.set_label(r'$E_{1/2}$ (V vs. RHE)', fontsize=7, fontfamily='Arial', labelpad=4)
cbar.ax.tick_params(labelsize=6, width=0.6, length=2.5, direction='out')
# Set colorbar ticks
cbar.set_ticks([0.70, 0.75, 0.80, 0.85, 0.90])
cbar.ax.set_yticklabels(['0.70', '0.75', '0.80', '0.85', '0.90'], fontsize=6)

# Mark "this work" on colorbar
this_norm = NORM(THIS_PAPER_E12)
ax_cb.axhline(this_norm, color=HIGHLIGHT_EC, linewidth=1.2, linestyle='--', zorder=5)
ax_cb.text(2.6, this_norm, 'This work\n(0.885 V)',
           va='center', ha='left', fontsize=5.5, fontfamily='Arial',
           color=HIGHLIGHT_EC, transform=ax_cb.transAxes)

# ─── Legend patches ───────────────────────────────────────────────────────────
# Draw in figure coordinates, below colorbar
legend_x = LMARGIN_FRAC + TABLE_FRAC + GAP_FRAC
legend_items = [
    (HIGHLIGHT_EC, 'Fe, Co, Mn — this work'),
    ('#CBCBCB',    'Metals, no ORR data'),
    ('#F2F2F2',    'Non-metals / noble gas'),
]
for i, (color, label) in enumerate(legend_items):
    y_pos = 0.12 - i * 0.055
    fig.add_artist(mpatches.FancyBboxPatch(
        (legend_x, y_pos - 0.012), 0.025, 0.030,
        boxstyle='round,pad=0.002',
        facecolor=color,
        edgecolor=HIGHLIGHT_EC if 'this work' in label else '#AAAAAA',
        linewidth=1.2 if 'this work' in label else 0.5,
        transform=fig.transFigure
    ))
    fig.text(legend_x + 0.030, y_pos + 0.003, label,
             ha='left', va='center', fontsize=5.5, fontfamily='Arial',
             color='#333333', transform=fig.transFigure)

# ─── Period numbers (left margin) ────────────────────────────────────────────
for period, row_y in [(p, PERIOD_ROW[p]) for p in [1,2,3,4,5,6]]:
    ax.text(0.0, row_y, str(period),
            ha='center', va='center',
            fontsize=5.5, color='#888888')

# ─── Group numbers (top) ─────────────────────────────────────────────────────
for grp in range(1, 19):
    ax.text(grp, -0.22, str(grp),
            ha='center', va='center',
            fontsize=5.0, color='#999999')

# ─── Save ────────────────────────────────────────────────────────────────────
for ext in ('pdf', 'png'):
    fpath = os.path.join(OUTDIR, f'fig1a_periodic_heatmap_journal_{TS}.{ext}')
    kw = {} if ext == 'pdf' else {'dpi': 600}
    fig.savefig(fpath, **kw, bbox_inches=None)
    print(f"Saved: {fpath}")

plt.close(fig)

# Copy script itself to output directory (rule: script lives with output)
shutil.copy(os.path.abspath(__file__), os.path.join(OUTDIR, os.path.basename(__file__)))
print("Script copied to output dir.")
print("Done.")
