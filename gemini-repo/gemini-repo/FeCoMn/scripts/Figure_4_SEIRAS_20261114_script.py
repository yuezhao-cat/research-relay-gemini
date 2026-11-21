import sys, os, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSC, TwoSlopeNorm
from scipy.signal import savgol_filter

D = sys.argv[1]; OUT = sys.argv[2]
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 7, 'axes.linewidth': 0.7,
                     'xtick.major.width': 0.7, 'ytick.major.width': 0.7, 'xtick.direction': 'in',
                     'ytick.direction': 'in', 'svg.fonttype': 'none', 'axes.unicode_minus': True,
                     'axes.edgecolor': '#404040', 'xtick.color': '#404040', 'ytick.color': '#404040',
                     'text.color': '#404040', 'axes.labelcolor': '#404040'})
CMAP_E = LSC.from_list('E', ['#8f8bc0', '#b6b3d6', '#d6d1d1', '#f1a0a6', '#eb687b'])
CMAP_D = LSC.from_list('D', ['#8f8bc0', '#d0cce5', '#ffffff', '#f6bcc4', '#eb687b'])
INK = '#404040'; RED = '#eb687b'; PUR = '#8f8bc0'
files = ['0.2', '0.1', '0', '-0.1', '-0.2', '-0.3', '-0.4', '-0.5', '-0.6', '-0.7', '-0.8', '-0.9', '-11']
E = np.array([(-1.1 if f == '-11' else float(f)) + 1.011 for f in files])
lab = lambda e: f'{e:.2f} V'.replace('-', '−')

def load(p):
    a = np.genfromtxt(p, delimiter=','); a = a[~np.isnan(a[:, 1])]; return a[np.argsort(a[:, 0])]
def bl(x, y):
    w1 = (x >= 1330) & (x <= 1370); w2 = (x >= 1900) & (x <= 1950)
    x1, y1, x2, y2 = x[w1].mean(), y[w1].mean(), x[w2].mean(), y[w2].mean()
    return y - (y1 + (y2 - y1) * (x - x1) / (x2 - x1))
RAW = []
for f in files:
    a = load(os.path.join(D, f + '.CSV')); x = a[:, 0]; RAW.append(bl(x, a[:, 1]) * 1e3)
RAW = np.array(RAW); REL = RAW - RAW[0]
sm = lambda A: np.array([savgol_filter(s, 21, 2) for s in A])
RAWs, RELs = sm(RAW), sm(REL)
cols = [CMAP_E(1 - k / (len(files) - 1)) for k in range(len(files))]
band = lambda lo, hi: REL[:, (x >= lo) & (x <= hi)].mean(1)
I3307, I1215 = band(3257, 3357), band(1191, 1239)

fig = plt.figure(figsize=(7.1, 6.2))
# ---------- a: broken-axis stacked spectra (as recorded, open-circuit background) ----------
segs = [(3700, 2900, 'OH', 4.0, 3307, 'ν(O–H)', 50), (1720, 1560, 'HOH', 1.0, 1633, 'δ(H–O–H)', 20),
        (1320, 1120, 'C', 1.0, 1215, '1215 cm$^{-1}$ region', 24)]
wid = [800, 300, 340]; L, R, B0, T0 = 0.075, 0.885, 0.585, 0.965; gap = 0.014
span = R - L - gap * 2; tot = sum(wid); xl = L; step = 6.0; n = len(files); axs = []
for (hi, lo, key, sc, c0, txt, hw), wd in zip(segs, wid):
    ww = span * wd / tot; ax = fig.add_axes([xl, B0, ww, T0 - B0]); xl += ww + gap; axs.append(ax)
    m = (x >= lo) & (x <= hi)
    ax.axvspan(c0 - hw, c0 + hw, color=RED if key == 'C' else PUR, alpha=0.10, lw=0)
    for k in range(n):
        ax.plot(x[m], RAWs[k, m] / sc + (n - 1 - k) * step, color=cols[k], lw=0.85)
    if key != 'C': ax.axvline(c0, ls=(0, (3, 2)), color=INK, lw=0.6)
    ax.text(c0, 1.01, txt, transform=ax.get_xaxis_transform(), ha='center', va='bottom')
    ax.set_xlim(hi, lo); ax.set_yticks([]); ax.set_ylim(-14, (n - 1) * step + 16)
    ax.spines['top'].set_visible(True)
    if ax is not axs[0]: ax.spines['left'].set_visible(False)
    if key != 'C': ax.spines['right'].set_visible(False)
    sb = 20.0 if key == 'OH' else 5.0; ytop = (n - 1) * step + 13; xb = hi - (hi - lo) * 0.08
    ax.plot([xb, xb], [ytop - sb / sc, ytop], color=INK, lw=1.0)
    ax.text(xb - (hi - lo) * 0.03, ytop + 3 - sb / sc / 2, f'{sb:g}×10$^{{-3}}$', fontsize=6, va='center')
    ax.set_xticks({'OH': [3600, 3400, 3200, 3000], 'HOH': [1700, 1600], 'C': [1300, 1200]}[key])
for ax in axs[:-1]:
    ax.plot([1 - .006 * 800 / wid[axs.index(ax)], 1 + .006 * 800 / wid[axs.index(ax)]], [-.02, .02],
            transform=ax.transAxes, color=INK, lw=0.7, clip_on=False)
for ax in axs[1:]:
    k = axs.index(ax); ax.plot([-.006 * 800 / wid[k], .006 * 800 / wid[k]], [-.02, .02], transform=ax.transAxes,
                              color=INK, lw=0.7, clip_on=False)
for k in range(n):
    axs[-1].text(1117, (n - 1 - k) * step + 0.5, lab(E[k]), fontsize=5.8, color=cols[k], va='center', clip_on=False)
axs[0].set_ylabel('Absorbance (a.u.)')
fig.text((L + R) / 2, B0 - 0.058, 'Wavenumber (cm$^{-1}$)', ha='center')

# ---------- b, c: colour maps referenced to 1.21 V ; d: band response, shared potential axis ----------
Eg = np.linspace(E.min(), E.max(), 260)
def cmap_panel(rect, lo, hi, c0, title, vmax):
    ax = fig.add_axes(rect); m = (x >= lo) & (x <= hi); xs = x[m]
    Z = np.array([np.interp(Eg, E[::-1], RELs[::-1, j]) for j in np.where(m)[0]]).T
    pc = ax.pcolormesh(xs, Eg, Z, cmap=CMAP_D, norm=TwoSlopeNorm(0, -vmax, vmax), shading='gouraud', rasterized=True)
    ax.axvline(c0, ls=(0, (3, 2)), color=INK, lw=0.6)
    ax.set_xlim(hi, lo); ax.set_ylim(E.min(), E.max())
    ax.text(c0, 1.01, title, transform=ax.get_xaxis_transform(), ha='center', va='bottom')
    ax.set_xlabel('Wavenumber (cm$^{-1}$)')
    return ax, pc
y0, h = 0.075, 0.40
bx, pb = cmap_panel([0.075, y0, 0.36, h], 2900, 3700, 3307, 'ν(O–H)', 16)
cbb = fig.add_axes([0.443, y0, 0.009, h]); c1 = fig.colorbar(pb, cax=cbb); c1.set_ticks([-16, -8, 0, 8, 16]); c1.ax.tick_params(labelsize=6)
cx, pcc = cmap_panel([0.50, y0, 0.37, h], 1120, 1320, 1215, '1215 cm$^{-1}$', 9)
bx.set_ylabel('E (V vs. RHE)'); cx.set_yticklabels([])
bx.set_xticks([3600, 3400, 3200, 3000]); cx.set_xticks([1300, 1250, 1200, 1150])
cbx = fig.add_axes([0.878, y0, 0.009, h]); cb = fig.colorbar(pcc, cax=cbx); cb.set_ticks([-9, -6, -3, 0, 3, 6, 9]); cb.ax.tick_params(labelsize=6)
cb.set_label('ΔAbsorbance (10$^{-3}$), ref. 1.21 V', fontsize=6.5)
# direct annotations: what changes, in words, on the map itself
from matplotlib.patches import FancyArrowPatch
def note(ax, xw, txt, col, up):
    ax.add_patch(FancyArrowPatch((xw, 1.12), (xw, -0.02), arrowstyle='-|>', mutation_scale=9, lw=1.2, color=col))
    ax.text(xw, 0.55, txt, rotation=90, ha='right', va='center', fontsize=7, color=col, fontweight='bold')
note(bx, 3040, 'O–H band weakens', '#5d5aa0', False)
note(cx, 1145, 'Decreasing potential', '#c8384d', True)
for lbl, X, Y in (('a', 0.012, 0.975), ('b', 0.012, 0.495), ('c', 0.475, 0.495)):
    fig.text(X, Y, lbl, fontweight='bold', fontsize=10, color='k')
fig.savefig(OUT + '.png', dpi=600); fig.savefig(OUT + '.svg')

