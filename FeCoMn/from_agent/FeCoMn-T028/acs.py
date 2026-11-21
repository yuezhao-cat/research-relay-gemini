# -*- coding: utf-8 -*-
"""ACS Catalysis main-figure house style for FeCoMn (Claude, 2026-10-27).
Rules: 赵月画图规则_v1 + 期刊专用规则_ACS (ACS Catalysis: text >= 8 pt, width <= 177.8 mm,
height <= 232.8 mm incl. caption, Arial/Helvetica, no inset figures) + locked FeCoMn 8-colour palette.
All geometry in mm, origin at the TOP-LEFT of the canvas, so frames align exactly by construction."""
import glob, json, os, shutil, csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator, AutoMinorLocator, FuncFormatter

for f in glob.glob(os.path.expanduser('~/.fonts/arial*.ttf')):
    fm.fontManager.addfont(f)
# Arial where installed (Windows); metric-identical Liberation Sans as fallback (Linux VM)
FONT = 'Arial' if any(f.name == 'Arial' for f in fm.fontManager.ttflist) else 'Liberation Sans'

MM = 1/25.4
W = 177.8           # ACS double column
FS = 8.0            # ACS Catalysis minimum text size
FL = 10.0           # panel letter, bold (only bold element)
LW_FRAME, LW_DATA, LW_REF = 0.8, 1.0, 0.8

PAL8 = ["#b6b3d6", "#d0cce5", "#d5d3df", "#d6d1d1", "#f7dfd7", "#f6b3a0", "#f1837b", "#eb687b"]
DEEP = "#5c506f"    # existing project deep tone (CDD profile outline; Co in COHP/PDOS)
SAMPLE = {'FeCoMn-NC': '#eb687b', 'FeCo-NC': '#b6b3d6', 'Mn-NC': '#f6b3a0', 'Pt/C': '#9e9e9e'}
ELEM = {'Mn': '#b6b3d6', 'Fe': '#f1837b', 'Co': DEEP, 'O': '#f6b3a0'}
REFC = '0.75'
# axis-label vocabulary (variables italic, units/numbers upright)
E_RHE = r'$E$ (V vs. RHE)'
J_ORR = r'$j$ (mA cm$^{\mathrm{-2}}$)'
def sub(t): return r'$_{\mathrm{%s}}$' % t
def sup(t): return r'$^{\mathrm{%s}}$' % t
H2O2 = 'H' + sub('2') + 'O' + sub('2')


def use():
    plt.rcParams.update({
        'font.family': [FONT], 'font.size': FS,
        'mathtext.fontset': 'custom', 'mathtext.rm': FONT, 'mathtext.it': FONT + ':italic',
        'mathtext.bf': FONT + ':bold', 'mathtext.sf': FONT, 'mathtext.default': 'it',
        'axes.linewidth': LW_FRAME, 'lines.linewidth': LW_DATA, 'axes.labelsize': FS,
        'xtick.labelsize': FS, 'ytick.labelsize': FS, 'legend.fontsize': FS,
        'xtick.direction': 'out', 'ytick.direction': 'out',
        'xtick.major.size': 3.0, 'ytick.major.size': 3.0, 'xtick.minor.size': 1.8, 'ytick.minor.size': 1.8,
        'xtick.major.width': LW_FRAME, 'ytick.major.width': LW_FRAME,
        'xtick.minor.width': LW_FRAME, 'ytick.minor.width': LW_FRAME,
        'xtick.major.pad': 2.0, 'ytick.major.pad': 2.0, 'axes.labelpad': 2.5,
        'xtick.top': False, 'ytick.right': False,
        'legend.frameon': False, 'legend.handlelength': 1.6, 'legend.handletextpad': 0.5,
        'legend.labelspacing': 0.25, 'legend.borderaxespad': 0.4, 'legend.borderpad': 0.2,
        'axes.unicode_minus': True, 'text.color': 'black', 'axes.labelcolor': 'black',
        'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none', 'savefig.dpi': 600,
        'axes.spines.top': True, 'axes.spines.right': True,
    })


class Canvas:
    def __init__(self, height_mm, width_mm=W):
        self.w, self.h = width_mm, height_mm
        self.fig = plt.figure(figsize=(width_mm*MM, height_mm*MM))
        self.fig.patch.set_facecolor('white')
        self.panels = []   # (letter, ax, kind)

    def ax(self, x, y, w, h, letter=None, kind='plot', **kw):
        """x,y = top-left corner of the FRAME in mm (from canvas top-left)."""
        a = self.fig.add_axes([x/self.w, 1-(y+h)/self.h, w/self.w, h/self.h], **kw)
        a._mm = (x, y, w, h)
        if kind == 'image':
            a.set_xticks([]); a.set_yticks([])
            for s in a.spines.values(): s.set_visible(False)
        self.panels.append((letter, a, kind))
        return a

    def letter(self, ax, s, x_mm=None, dy=1.6, dx=0.0):
        """Panel letter above the frame; left edge aligned to the y-axis label ink (rule 三) unless x_mm given."""
        x, y, w, h = ax._mm
        if x_mm is None:
            self.fig.canvas.draw()
            r = self.fig.canvas.get_renderer()
            lab = ax.yaxis.label
            if lab.get_text() and lab.get_visible():
                bb = lab.get_window_extent(r)
                x_mm = bb.x0 / self.fig.dpi / MM
            else:
                bbs = [t.get_window_extent(r) for t in ax.get_yticklabels() if t.get_text()]
                x_mm = (min(b.x0 for b in bbs) / self.fig.dpi / MM) if bbs else x
        t = self.fig.text((x_mm+dx)/self.w, 1-(y-dy)/self.h, s, fontsize=FL, fontweight='bold',
                          ha='left', va='baseline')
        return t

    def save(self, outdir, stem):
        os.makedirs(outdir, exist_ok=True)
        for ext in ('pdf', 'png', 'svg'):
            self.fig.savefig(os.path.join(outdir, f'{stem}.{ext}'), dpi=600, facecolor='white')
        # frame geometry record (mm, top-left origin) for alignment QA
        rec = {'width_mm': self.w, 'height_mm': self.h, 'panels': []}
        for L, a, k in self.panels:
            x, y, w, h = a._mm
            rec['panels'].append(dict(letter=L, kind=k, left=round(x, 3), top=round(y, 3),
                                      right=round(x+w, 3), bottom=round(y+h, 3)))
        with open(os.path.join(outdir, f'{stem}_frames.json'), 'w', encoding='utf-8') as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
        # single panels (no panel letter), cut from the same canvas at print size
        from matplotlib.transforms import Bbox
        sd = os.path.join(outdir, '单面板'); os.makedirs(sd, exist_ok=True)
        r = self.fig.canvas.get_renderer(); n = 0
        hidden = [t for t in self.fig.texts if t.get_visible()]
        for t in hidden: t.set_visible(False)
        for L, a, k in self.panels:
            if not L: continue
            group = [a] + [b for (L2, b, k2) in self.panels if L2 is None and k2 != 'cbar' and abs(b._mm[0] - a._mm[0]) < 0.01
                           and 0 < b._mm[1] - a._mm[1] < a._mm[3] + 5]
            if k == 'plot':
                group += [b for (L2, b, k2) in self.panels if k2 == 'cbar' and abs(b._mm[1] - a._mm[1]) < 0.01
                          and 0 < b._mm[0] - (a._mm[0] + a._mm[2]) < 4]
            bbs = [g.get_tightbbox(r) for g in group]
            bb = Bbox.union(bbs).transformed(self.fig.dpi_scale_trans.inverted()).padded(0.03)
            for ext in ('pdf', 'png'):
                self.fig.savefig(os.path.join(sd, f'{stem}_panel_{L}.{ext}'), dpi=600, bbox_inches=bb, facecolor='white')
            n += 1
        for t in hidden: t.set_visible(True)
        print('single panels:', n)


def frame(ax, xmaj=None, ymaj=None, xmin=None, ymin=None):
    for s in ax.spines.values():
        s.set_visible(True); s.set_linewidth(LW_FRAME)
    ax.tick_params(which='both', top=False, right=False, direction='out')
    if xmaj: ax.xaxis.set_major_locator(MultipleLocator(xmaj))
    if ymaj: ax.yaxis.set_major_locator(MultipleLocator(ymaj))
    if xmin: ax.xaxis.set_minor_locator(MultipleLocator(xmin))
    if ymin: ax.yaxis.set_minor_locator(MultipleLocator(ymin))


def thousands(axis):
    axis.set_major_formatter(FuncFormatter(lambda v, p: '{:,.0f}'.format(v).replace('-', '−')))


def ref(ax, y=None, x=None):
    if y is not None: ax.axhline(y, color=REFC, lw=LW_REF, ls=':', zorder=0)
    if x is not None: ax.axvline(x, color=REFC, lw=LW_REF, ls=':', zorder=0)


def text_audit(fig):
    """Return smallest font size used anywhere (must be >= 8 except panel letters)."""
    sizes = []
    for t in fig.findobj(matplotlib.text.Text):
        if t.get_text().strip() and t.get_visible():
            sizes.append(t.get_fontsize())
    return min(sizes) if sizes else None


def copy_self(script, outdir):
    shutil.copy(script, os.path.join(outdir, os.path.basename(script)))
