"""T037 Step 4 draft v2 (Option B / 乙方案):
1. Panel (a): Mn-NC row uses COHP-static total 3d PDOS and eps_d (-3.54 eV) so both total 3d and Mn dz2 in each row are 100% from the same wavefunction.
2. dz2 PDOS is individually normalized (0.85 height) and plotted in a darker same-hue tone (#8f2235 for FCM, #a34930 for MnNC) so the orbital shift (-3.17 vs -5.12 eV) is immediately visible.
3. eps_dz2 vertical dotted lines match the darker dz2 curve color, with a clear two-item legend above panel (a).
4. Panels (b) and (e) retain the dz2 -ICOHP annotations; (c)(d)(f)(g)(h)(i) remain identical to v38.
"""
from pathlib import Path
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
T034 = HERE.parent / "FeCoMn-T034"
V38_SCRIPT = T034 / "build_t034_v38_axial_parentheses.py"
OUT = HERE / "draft_20261119_v2"
OUT.mkdir(exist_ok=True)
T037_DATA = HERE / "data"

src = V38_SCRIPT.read_text(encoding="utf-8")
src = src.replace("HERE = Path(__file__).resolve().parent", f"HERE = Path(r'{T034}')")
src = src.replace("OUT = HERE / 'draft_20261118_v38_axial_parentheses'", f"OUT = Path(r'{OUT}')")
save_marker = "fig.savefig(OUT / 'Figure6_T034_600dpi.png'"
prefix, _ = src.split(save_marker, 1)

env = {"__file__": str(V38_SCRIPT), "__name__": "t037_draft_v2"}
exec(compile(prefix, str(V38_SCRIPT), "exec"), env)

acs = env["acs"]
fig = env["fig"]
a_ax = env["a"]        # panel b in final layout (axial -pCOHP)
c_ax = env["c"]        # panel a in final layout (metal 3d before reaction)
e1_ax = env["old_e1"]  # panel e left (OOH* -pCOHP)
broaden = env["broaden"]
COL = env["COL"]
EDGE = env["EDGE"]
SYS = env["SYS"]
L = env["L"]
EK = env["EK"]
PK = env["PK"]
EPS_T = env["EPS_T"]

# Rebuild panel a (c_ax) cleanly using Option B (Mn-NC row from COHP static, same source as dz2)
c_ax.clear()
OFF = 1.25
DARK_DZ2 = {"FCM": "#8b1e34", "MnNC": "#9c4328"}

# Preload COHP-static PDOS for FCM and MnNC
cohp_pdos = {
    "FCM": pd.read_csv(T037_DATA / "FCM_base_Mn_dz2_PDOS.csv"),
    "MnNC": pd.read_csv(T037_DATA / "MnNC_base_Mn_dz2_PDOS.csv"),
}
EPS_OPT_B = {"FCM": -3.42, "FCN": -2.39, "MnNC": -3.54}
EDZ2 = {"FCM": -3.17, "MnNC": -5.12}

for i, (s, nm) in enumerate(SYS):
    y0 = (2 - i) * OFF
    if s in ["FCM", "MnNC"]:
        df_s = cohp_pdos[s]
        x = df_s["E_minus_EF_eV"].to_numpy()
        y = broaden(x, (df_s["d3_sum_up"] + df_s["d3_sum_down"]).to_numpy())
        dz2 = broaden(x, (df_s["dz2_up"] + df_s["dz2_down"]).to_numpy())
    else:
        dd = L("calc_PDOS_FCN_base")
        y_raw = None
        for lab, v in dd.items():
            if "3d" not in lab:
                continue
            idx = int("".join(q for q in lab.split()[0] if q.isdigit()))
            if idx not in [206, 234, 235]:
                continue
            x = v[EK]
            y_raw = v[PK].copy() if y_raw is None else y_raw + v[PK]
        y = broaden(x, y_raw)
        dz2 = None

    mask = (x > -8.2) & (x < 4.2)
    scale = y[mask].max() / 0.92
    c_ax.fill_between(x[mask], y0, y0 + y[mask] / scale, color=COL[s], alpha=0.50, lw=0)
    c_ax.plot(x[mask], y0 + y[mask] / scale, color=EDGE[s], lw=0.7)
    if i:
        c_ax.axhline(y0 + OFF, color="black", lw=0.5)

    ed = EPS_OPT_B[s]
    c_ax.plot([ed, ed], [y0, y0 + (0.80 if s == "FCM" else 0.90)], color=EDGE[s], lw=1.3, ls=(0, (2.2, 1.2)), zorder=5)
    c_ax.text(-7.7, y0 + 1.2, nm, ha="left", va="top", fontsize=acs.FS, zorder=6, bbox=dict(fc="white", ec="none", pad=0.3))
    c_ax.text(3.9, y0 + 1.2, EPS_T + " " + f"{ed:.2f}".replace("-", "−"), ha="right", va="top", fontsize=acs.FS, zorder=6, bbox=dict(fc="white", ec="none", pad=0.3))

    if dz2 is not None:
        # Individually normalize dz2 to 0.85 height so peak shapes are crystal clear, in darker same-hue tone
        dz2_scale = dz2[mask].max() / 0.85
        dcol = DARK_DZ2[s]
        c_ax.plot(x[mask], y0 + dz2[mask] / dz2_scale, color=dcol, lw=1.15, zorder=5.2)
        cdz = EDZ2[s]
        c_ax.plot([cdz, cdz], [y0, y0 + 0.72], color=dcol, lw=1.4, ls=":", zorder=5.8)
        c_ax.text(3.9, y0 + 0.86, r"$\varepsilon_{\mathrm{d}_{z^2}}$ " + f"{cdz:.2f}".replace("-", "−"),
                  ha="right", va="top", fontsize=acs.FS, color=dcol, zorder=7,
                  bbox=dict(fc="white", ec="none", pad=0.15))

acs.ref(c_ax, x=0)
c_ax.set_xlim(-8, 4)
c_ax.set_ylim(0, 3 * OFF)
c_ax.set_yticks([])
acs.frame(c_ax, xmaj=4, xmin=2)
c_ax.set_xlabel("$E$ − $E$" + acs.sub("F") + " (eV)")
c_ax.set_ylabel("Normalized PDOS")

# Re-align y-axis label of c_ax to column 0 target
c_ax.yaxis.set_label_coords(env["targets"][0] * fig.dpi * acs.MM / c_ax.get_window_extent(fig.canvas.get_renderer()).width * 0 + -0.05, 0.5)
# Actually re-run exact column alignment for column 0 ([c_ax, old_d, old_g])
fig.canvas.draw()
rr = fig.canvas.get_renderer()
col0 = [c_ax, env["old_d"], env["old_g"]]
target0 = min(z.yaxis.label.get_window_extent(rr).x0 for z in col0)
for z in col0:
    lab = z.yaxis.label
    pos = lab.get_transform().transform(lab.get_position())
    xx = z.transAxes.inverted().transform(pos)[0]
    delta = (target0 - lab.get_window_extent(rr).x0) / z.get_window_extent(rr).width
    z.yaxis.set_label_coords(xx + delta, 0.5)

# Clear, matching legend above panel a
leg_handles = [
    Patch(fc="0.72", ec="none", label=r"metal 3$d$ ($\varepsilon_{\mathrm{d}}$ --)"),
    Line2D([0], [0], color="0.25", lw=1.15, label=r"Mn $d_{z^2}$ ($\varepsilon_{\mathrm{d}_{z^2}}$ ··)"),
]
c_ax.legend(handles=leg_handles, loc="lower center", bbox_to_anchor=(0.54, 1.01),
            ncol=2, frameon=False, fontsize=acs.FS, handlelength=1.2, handletextpad=0.35, columnspacing=0.8, borderaxespad=0.0)

# Panel b (a_ax): dz2 -ICOHP breakdown under total -ICOHP (2.64 / 8.03)
a_ax.text(0.85, 1.89 + 0.25, "$d_{z^2}$ 1.00", ha="right", va="top", fontsize=acs.FS, color="0.25",
          zorder=6, bbox=dict(fc="white", ec="none", pad=0.15))
a_ax.text(0.85, 0.64 + 0.25, "$d_{z^2}$ 2.98", ha="right", va="top", fontsize=acs.FS, color="0.25",
          zorder=6, bbox=dict(fc="white", ec="none", pad=0.15))

# Panel e left (OOH*): dz2 -ICOHP alongside total -ICOHP
for item in list(e1_ax.texts):
    if item.get_text() == "3.12":
        item.set_text("3.12 ($d_{z^2}$ 1.38)")
    elif item.get_text() == "2.65":
        item.set_text("2.65 ($d_{z^2}$ 1.06)")

fig.savefig(OUT / "Figure6_T037_v2_600dpi.png", dpi=600, facecolor="white")
fig.savefig(OUT / "Figure6_T037_v2_preview.png", dpi=300, facecolor="white")
fig.savefig(OUT / "Figure6_T037_v2.pdf", facecolor="white")
acs.plt.rcParams["svg.fonttype"] = "none"
fig.savefig(OUT / "Figure6_T037_v2_editable.svg", facecolor="white")
print("SAVED T037 Step 4 draft v2 (Option B) to", OUT)
