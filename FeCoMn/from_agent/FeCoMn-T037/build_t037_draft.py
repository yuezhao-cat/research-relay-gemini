"""T037 Step 4 draft v2: Minimal edits preserving Figure 6 v38 style, layout, colors, and >=8 pt Arial typography.
- Panel a: keep Genkai 3d PDOS & eps_d untouched; overlay COHP-static Mn dz2 PDOS (bold charcoal) + eps_dz2; add top legend matching panel d.
- Panel b: add dz2 -ICOHP breakdown under total -ICOHP (2.64 / 8.03).
- Panel e (OOH*): add dz2 -ICOHP cleanly in bottom blank region without touching y=0 or antibonding peaks.
"""
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
T034 = HERE.parent / "FeCoMn-T034"
V38_SCRIPT = T034 / "build_t034_v38_axial_parentheses.py"
OUT = HERE / "draft_20261119_v1"
OUT.mkdir(exist_ok=True)
T037_DATA = HERE / "data"

src = V38_SCRIPT.read_text(encoding="utf-8")
src = src.replace("HERE = Path(__file__).resolve().parent", f"HERE = Path(r'{T034}')")
src = src.replace("OUT = HERE / 'draft_20261118_v38_axial_parentheses'", f"OUT = Path(r'{OUT}')")
save_marker = "fig.savefig(OUT / 'Figure6_T034_600dpi.png'"
prefix, _ = src.split(save_marker, 1)

env = {"__file__": str(V38_SCRIPT), "__name__": "t037_draft"}
exec(compile(prefix, str(V38_SCRIPT), "exec"), env)

acs = env["acs"]
fig = env["fig"]
a_ax = env["a"]        # panel b in final layout (axial -pCOHP)
c_ax = env["c"]        # panel a in final layout (metal 3d before reaction)
e1_ax = env["old_e1"]  # panel e left (OOH* -pCOHP)
broaden = env["broaden"]

# 1) Panel a (c_ax): overlay COHP-static Mn dz2 PDOS and mark eps_dz2
OFF = 1.25
dz2_info = [
    ("FCM", 2, -3.17, "FCM_base_Mn_dz2_PDOS.csv"),
    ("MnNC", 0, -5.12, "MnNC_base_Mn_dz2_PDOS.csv"),
]
for s, row_idx, cdz, fname in dz2_info:
    df_dz = pd.read_csv(T037_DATA / fname)
    x = df_dz["E_minus_EF_eV"].to_numpy()
    d3_tot = broaden(x, (df_dz["d3_sum_up"] + df_dz["d3_sum_down"]).to_numpy())
    dz2_tot = broaden(x, (df_dz["dz2_up"] + df_dz["dz2_down"]).to_numpy())
    mask = (x > -8.2) & (x < 4.2)
    y0 = row_idx * OFF
    scale = d3_tot[mask].max() / 0.92
    c_ax.plot(x[mask], y0 + dz2_tot[mask] / scale, color="0.15", lw=1.0, zorder=4.5)
    c_ax.plot([cdz, cdz], [y0, y0 + 0.72], color="0.15", lw=1.2, ls=":", zorder=5.5)
    if s == "FCM":
        # Put eps_dz2 cleanly right below eps_d (-3.42) in top-right blank corner
        c_ax.text(3.9, y0 + 0.86, r"$\varepsilon_{\mathrm{d}_{z^2}}$ −3.17",
                  ha="right", va="top", fontsize=acs.FS, color="0.15", zorder=7,
                  bbox=dict(fc="white", ec="none", pad=0.15))
    else:
        # Put eps_dz2 cleanly in upper-middle blank area next to Mn-NC
        c_ax.text(3.9, y0 + 0.86, r"$\varepsilon_{\mathrm{d}_{z^2}}$ −5.12",
                  ha="right", va="top", fontsize=acs.FS, color="0.15", zorder=7,
                  bbox=dict(fc="white", ec="none", pad=0.15))

# Top legend for panel a matching panel d style (above frame, centered)
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
leg_handles = [
    Patch(fc="0.72", ec="none", label="metal 3$d$"),
    Line2D([0], [0], color="0.15", lw=1.0, label="Mn $d_{z^2}$"),
]
c_ax.legend(handles=leg_handles, loc="lower center", bbox_to_anchor=(0.56, 1.01),
            ncol=2, frameon=False, fontsize=acs.FS, handlelength=1.4, handletextpad=0.4, columnspacing=0.9, borderaxespad=0.0)

# 2) Panel b (a_ax): add dz2 -ICOHP breakdown under total -ICOHP (2.64 / 8.03)
a_ax.text(0.85, 1.89 + 0.25, "$d_{z^2}$ 1.00", ha="right", va="top", fontsize=acs.FS, color="0.25",
          zorder=6, bbox=dict(fc="white", ec="none", pad=0.15))
a_ax.text(0.85, 0.64 + 0.25, "$d_{z^2}$ 2.98", ha="right", va="top", fontsize=acs.FS, color="0.25",
          zorder=6, bbox=dict(fc="white", ec="none", pad=0.15))

# 3) Panel e left (OOH*): place dz2 -ICOHP cleanly in bottom blank region alongside total -ICOHP
for item in list(e1_ax.texts):
    if item.get_text() == "3.12":
        item.set_text("3.12 ($d_{z^2}$ 1.38)")
    elif item.get_text() == "2.65":
        item.set_text("2.65 ($d_{z^2}$ 1.06)")

fig.savefig(OUT / "Figure6_T037_600dpi.png", dpi=600, facecolor="white")
fig.savefig(OUT / "Figure6_T037_preview.png", dpi=300, facecolor="white")
fig.savefig(OUT / "Figure6_T037.pdf", facecolor="white")
acs.plt.rcParams["svg.fonttype"] = "none"
fig.savefig(OUT / "Figure6_T037_editable.svg", facecolor="white")
print("SAVED T037 Step 4 draft v2 to", OUT)
