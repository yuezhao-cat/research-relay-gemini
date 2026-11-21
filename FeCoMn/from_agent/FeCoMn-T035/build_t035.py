"""T035: Re-render SI Figures S17-S22 from verified original CONTCARs with distinct gray C and white dark-rimmed H,
and generate full per-panel verification table (atom counts, CONTCAR SHA256, image SHA256, duplicate checks).
"""
import hashlib
import json
import re
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib._mathtext as _mt
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
F5 = Path(r"D:\OneDrive\Desktop\知识库\papers\FeCoMn\ACS_Catalysis_第三轮投稿\ACS_投稿拼图_Claude重绘_20261027\Figure_5_新覆盖背景_20261031")
LBL = F5.parent.parent / "全文_20261030/覆盖候选_分样品大图_20261030"
POS = Path(r"C:\Users\46775\.gemini\antigravity\brain\4d1b2883-432e-4243-86e4-bcadfd8e7706\scratch\t035_poscars")
FETCH_MANIFEST = json.loads((POS / "fetch_manifest.json").read_text(encoding="utf-8"))

class _ArialScripts(_mt.FontConstantsBase):
    script_space = 0.0
    subdrop = 0.2
    sup1 = 0.35
    sub1 = 0.15
    sub2 = 0.25
    delta = 0.0

_mt._font_constant_mapping["Arial"] = _ArialScripts
plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 7,
    "mathtext.fontset": "custom",
    "mathtext.rm": "Arial",
    "mathtext.default": "regular",
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
})

RAD = {"C": 0.36, "N": 0.40, "O": 0.44, "H": 0.35, "Fe": 0.66, "Co": 0.66, "Mn": 0.66}
COV = {"H": 0.31, "C": 0.76, "N": 0.71, "O": 0.70, "Mn": 1.39, "Fe": 1.32, "Co": 1.26}
METALS = {"Fe", "Co", "Mn"}

def load_base_sprite(el: str) -> np.ndarray:
    a = np.asarray(Image.open(F5 / "结构渲染" / f"key_{el}.png").convert("RGB")).astype(float)
    m = a.min(2) < 250
    ys, xs = np.where(m)
    cy, cx = (ys.min() + ys.max()) / 2, (xs.min() + xs.max()) / 2
    r = (xs.max() - xs.min()) / 2
    return a[int(cy - r):int(cy + r) + 1, int(cx - r):int(cx + r) + 1]

def make_gray_c_sprite(base_c: np.ndarray) -> np.ndarray:
    # Distinct medium gray C (center ~142) with 3D shading preserved
    return np.clip(base_c * 0.62, 40, 210)

def make_white_h_sprite(size: int = 135) -> np.ndarray:
    # Distinct light cyan-mint sphere so H stands out clearly against gray C, blue N, pink Fe, red O, and white background
    yy, xx = np.mgrid[0:size, 0:size]
    c = (size - 1) / 2.0
    nx = (xx - c) / (size / 2.0)
    ny = (yy - c) / (size / 2.0)
    r2 = nx * nx + ny * ny
    nz = np.sqrt(np.clip(1.0 - r2, 0.0, 1.0))
    lx, ly, lz = -0.35, -0.35, 0.87
    diff = np.clip(nx * lx + ny * ly + nz * lz, 0.0, 1.0)
    r_ch = 85.0 + 110.0 * diff
    g_ch = 185.0 + 65.0 * diff
    b_ch = 168.0 + 72.0 * diff
    img = np.stack([r_ch, g_ch, b_ch], axis=-1)
    return np.clip(img, 0, 255)

SPR = {e: load_base_sprite(e) for e in ["Fe", "Co", "Mn", "N", "O"]}
SPR["C"] = make_gray_c_sprite(load_base_sprite("C"))
SPR["H"] = make_white_h_sprite()

def make_legend_icon(el: str, size: int = 120) -> np.ndarray:
    spr = SPR[el]
    sp = np.asarray(Image.fromarray(spr.astype(np.uint8)).resize((size, size), Image.LANCZOS)).astype(float)
    yy, xx = np.mgrid[0:size, 0:size]
    rr = np.hypot(xx - (size - 1) / 2.0, yy - (size - 1) / 2.0)
    r = size / 2.0 - 2.0
    al = np.clip(r - rr, 0, 1)[..., None]
    rim_w = 2.2
    rim_mul = 0.55
    edge = (rr > r - rim_w)[..., None] & (al > 0)
    sp = np.where(edge, sp * rim_mul, sp)
    bg = np.full((size, size, 3), 255.0)
    out = bg * (1.0 - al) + sp * al
    return np.clip(out, 0, 255).astype(np.uint8)

def read_poscar(p: Path):
    L = p.read_text(encoding="utf-8", errors="replace").splitlines()
    sc = float(L[1])
    cell = np.array([[float(x) for x in L[i].split()] for i in (2, 3, 4)]) * sc
    el = L[5].split()
    nn = [int(x) for x in L[6].split()]
    k = 7
    if L[k].strip()[0] in "sS":
        k += 1
    direct = L[k].strip()[0] in "dD"
    k += 1
    xyz = np.array([[float(x) for x in L[k + i].split()[:3]] for i in range(sum(nn))])
    syms = np.array(sum([[e] * c for e, c in zip(el, nn)], []))
    pos = (xyz @ cell) if direct else (xyz * sc)
    return syms, pos, cell

def count_adsorbates(syms: np.ndarray, pos: np.ndarray, cell: np.ndarray):
    """Classify O and H atoms in CONTCAR by actual 3D minimum-image distances."""
    inv_cell = np.linalg.inv(cell)
    frac = pos @ inv_cell
    o_idx = np.where(syms == "O")[0]
    h_idx = np.where(syms == "H")[0]

    def pbc_dist(i, j):
        df = frac[i] - frac[j]
        df -= np.round(df)
        return float(np.linalg.norm(df @ cell))

    # Map each H to an O if d(O-H) < 1.25 A
    o_to_h = {int(o): [] for o in o_idx}
    h_only = 0
    for h in h_idx:
        best_o, best_d = None, 999.0
        for o in o_idx:
            d = pbc_dist(o, h)
            if d < best_d:
                best_d, best_o = d, int(o)
        if best_o is not None and best_d < 1.25:
            o_to_h[best_o].append(int(h))
        else:
            h_only += 1

    # Detect O-O bonds (OOH) if d(O-O) < 1.70 A
    o_pairs = []
    used_o = set()
    for a_i, oa in enumerate(o_idx):
        if int(oa) in used_o:
            continue
        for ob in o_idx[a_i + 1:]:
            if int(ob) in used_o:
                continue
            if pbc_dist(oa, ob) < 1.70:
                o_pairs.append((int(oa), int(ob)))
                used_o.add(int(oa))
                used_o.add(int(ob))
                break

    ooh_count = len(o_pairs)
    oh_count = 0
    o_only = 0
    for o in o_idx:
        oi = int(o)
        if oi in used_o:
            continue
        if len(o_to_h[oi]) >= 1:
            oh_count += 1
        else:
            o_only += 1

    return {
        "O_total": int(len(o_idx)),
        "H_total": int(len(h_idx)),
        "O_only": int(o_only),
        "OH": int(oh_count),
        "OOH": int(ooh_count),
        "H_only": int(h_only),
    }

def bonds_of(syms, pos):
    r = np.array([COV[s] for s in syms]) * 1.08
    d = np.linalg.norm(pos[:, None] - pos[None], axis=-1)
    i, j = np.where(np.triu((d < r[:, None] + r[None]) & (d > 0.1), 1))
    return [(a, b) for a, b in zip(i, j) if not (syms[a] in METALS and syms[b] in METALS and d[a, b] > 3.0)]

def place(syms, pos, cell, wrap):
    if not wrap:
        return pos
    m = np.isin(syms, ["Fe", "Co"])
    c = pos[m].mean(0) if m.any() else pos[syms == "Mn"][0]
    frac = np.linalg.solve(cell.T, (pos - c).T).T
    frac[:, :2] -= np.round(frac[:, :2])
    return c + frac @ cell

def project(syms, pos, cell, elev):
    pos = pos - pos.mean(0)
    e = np.deg2rad(elev)
    X = pos[:, 0]
    Y = pos[:, 2] * np.cos(e) + pos[:, 1] * np.sin(e)
    D = pos[:, 1] * np.cos(e) - pos[:, 2] * np.sin(e)
    return np.c_[X, Y, D]

def render(syms, P, bonds, s, W, H):
    img = np.full((H, W, 3), 255.0)
    pil = Image.fromarray(img.astype(np.uint8))
    dr = ImageDraw.Draw(pil)
    cx, cy = W / 2, H / 2
    to = lambda p: (cx + p[0] * s, cy - p[1] * s)
    for a, b in sorted(bonds, key=lambda ab: -(P[ab[0], 2] + P[ab[1], 2])):
        dr.line([to(P[a]), to(P[b])], fill=(135, 135, 135), width=max(1, int(0.13 * s)))
    img = np.asarray(pil).astype(float).copy()
    for i in np.argsort(-P[:, 2]):
        el = syms[i]
        r = RAD[el] * s
        spr = SPR[el]
        n = int(2 * r) + 1
        if n < 2:
            continue
        sp = np.asarray(Image.fromarray(spr.astype(np.uint8)).resize((n, n), Image.LANCZOS)).astype(float)
        yy, xx = np.mgrid[0:n, 0:n]
        rr = np.hypot(xx - (n - 1) / 2, yy - (n - 1) / 2)
        al = np.clip(r - rr, 0, 1)[..., None]
        if el == "H":
            rim_w = max(1.2, s * 0.035)
            edge = (rr > r - rim_w)[..., None] & (al > 0)
            sp = np.where(edge, sp * 0.45, sp)
        else:
            edge = (rr > r - 1.2 * max(1, s * 0.03))[..., None] & (al > 0)
            sp = np.where(edge, sp * 0.55, sp)
        x0 = int(round(cx + P[i, 0] * s - n / 2))
        y0 = int(round(cy - P[i, 1] * s - n / 2))
        xa, ya, xb, yb = max(x0, 0), max(y0, 0), min(x0 + n, W), min(y0 + n, H)
        if xa >= xb or ya >= yb:
            continue
        sl = (slice(ya - y0, yb - y0), slice(xa - x0, xb - x0))
        img[ya:yb, xa:xb] = img[ya:yb, xa:xb] * (1 - al[sl]) + sp[sl] * al[sl]
    return img.clip(0, 255).astype(np.uint8)

def fam(l):
    a = l.split(" @")[0]
    if a == "clean" or ("H*" in a and "O" not in a):
        return 0
    nO = sum(int(x) for x in re.findall(r"(\d+)O\*", a))
    if nO == 0:
        return 1
    if "OH*" not in a and nO <= 4:
        return 2
    return 3

u = pd.read_csv(F5 / "coverage_library_reference_with_joint.csv")
JOINT = {
    "rich8O_joint_20261014/FCM_8O_MnO": "8O* @ particle + Mn=O",
    "rich8O_joint_20261014/FCM_8O_MnOH": "8O*+1OH* @ particle + Mn–OH",
    "coverage_6O7O_20261014/FCM_6O_MnO": "7O* @ particle + Mn=O",
}

def items(sample, comp):
    d = pd.read_csv(LBL / f"{sample}_all_candidates_large_20261030_labels.csv")
    d["label"] = d.label.str.split("\n").str[0]
    d = d[d.component == comp][["directory", "label", "G0_eV", "electrons"]]
    if sample == "FeCoMn-NC" and comp == "Full model":
        j = u[u.directory.isin(JOINT)].copy()
        j["label"] = j.directory.map(JOINT)
        d = pd.concat([d, j[["directory", "label", "G0_eV", "electrons"]]])
    d["f"] = d.label.map(fam)
    d["g2"] = d.G0_eV - 2.0 * d.electrons
    d = d.sort_values(["f", "g2"], ascending=[True, False])
    d["path"] = [POS / (x.replace("/", "__") + ".vasp") for x in d.directory]
    d = d[[p.exists() for p in d.path]].copy()
    return d

SETS = [
    ("FeCoMn–NC supported model", items("FeCoMn-NC", "Full model"), 28, 4, ["Figure_S17", "Figure_S18"]),
    ("FeCo–NC supported model", items("FeCo-NC", "Full model"), 28, 4, ["Figure_S19"]),
    ("Mn–NC", items("Mn-NC", "Full model"), 28, 4, ["Figure_S20"]),
    ("FeCo(110) submodel", items("FeCoMn-NC", "Particle submodel"), 40, 5, ["Figure_S21", "Figure_S22"]),
]

MM = 1 / 25.4
FW = 160.0
PER_PAGE = 24
records = []

for title, d, elev, ncol, fig_names in SETS:
    scenes = []
    counts_list = []
    sha_list = []
    for p in d.path:
        raw_bytes = p.read_bytes()
        sha_list.append(hashlib.sha256(raw_bytes).hexdigest())
        sy, ps, cell = read_poscar(p)
        counts_list.append(count_adsorbates(sy, ps, cell))
        ps = place(sy, ps, cell, "submodel" not in title)
        P = project(sy, ps, cell, elev)
        scenes.append((sy, P, bonds_of(sy, ps)))

    hx = max(np.abs(P[:, 0]).max() + 0.8 for _, P, _ in scenes)
    ylo = min(P[:, 1].min() - 0.8 for _, P, _ in scenes)
    yhi = max(P[:, 1].max() + 0.8 for _, P, _ in scenes)
    scenes = [(sy, P - np.array([0, (ylo + yhi) / 2, 0]), b) for sy, P, b in scenes]

    TW = (FW - 4) / ncol
    TH = TW * (yhi - ylo) / (2 * hx)
    tw_px = int(TW * MM * 600)
    th_px = int(TH * MM * 600)
    s = tw_px / (2 * hx)
    per = 25 if ncol == 5 else PER_PAGE
    pages = [list(range(i, min(i + per, len(d)))) for i in range(0, len(d), per)]
    assert len(pages) == len(fig_names), (title, len(pages), fig_names)

    for pg, idx in enumerate(pages):
        figname = fig_names[pg]
        nrow = int(np.ceil(len(idx) / ncol))
        LH = 4.2
        FH = nrow * (TH + LH) + 9
        fig = plt.figure(figsize=(FW * MM, FH * MM))
        for k, i in enumerate(idx):
            r, c = divmod(k, ncol)
            x0 = 2 + c * TW
            y0 = r * (TH + LH)
            ax = fig.add_axes([x0 / FW, 1 - (y0 + TH) / FH, TW / FW, TH / FH])
            ax.axis("off")
            tile_img = render(*scenes[i], s, tw_px, th_px)
            ax.imshow(tile_img)
            fig.text((x0 + TW / 2) / FW, 1 - (y0 + TH + 0.3) / FH, d.label.iloc[i], ha="center", va="top", fontsize=6.5)

            dir_str = d.directory.iloc[i]
            lbl_str = d.label.iloc[i]
            cnt = counts_list[i]
            fm_info = FETCH_MANIFEST[dir_str]
            tile_sha = hashlib.sha256(tile_img.tobytes()).hexdigest()
            ref_row = u[u.directory == dir_str].iloc[0]
            match_ok = (
                cnt["O_total"] == int(ref_row["O"])
                and cnt["H_total"] == int(ref_row["H"])
                and cnt["O_only"] == int(ref_row["O_only"])
                and cnt["OH"] == int(ref_row["OH"])
                and cnt["OOH"] == int(ref_row["OOH"])
                and cnt["H_only"] == int(ref_row["H_only"])
            )
            records.append({
                "figure": figname,
                "set": title,
                "panel_index_in_fig": k + 1,
                "panel_label": lbl_str,
                "directory": dir_str,
                "host": fm_info["host"],
                "remote_contcar_path": fm_info["remote_path"],
                "contcar_sha256": sha_list[i],
                "E_sigma0_eV": fm_info["e_sigma0"],
                "O_total": cnt["O_total"],
                "H_total": cnt["H_total"],
                "O_only": cnt["O_only"],
                "OH": cnt["OH"],
                "OOH": cnt["OOH"],
                "H_only": cnt["H_only"],
                "matches_reference_counts": match_ok,
                "tile_image_sha256": tile_sha,
            })

        els = ["Fe", "Co", "Mn", "C", "N", "O", "H"] if "submodel" not in title else ["Fe", "Co", "O", "H"]
        if title == "Mn–NC":
            els = ["Mn", "C", "N", "O", "H"]
        kx = FW / 2 - len(els) * 6.5
        for e_, el in enumerate(els):
            icon_sz = 3.1 if el == "H" else 3.2
            pad_y = (3.2 - icon_sz) / 2.0
            ax = fig.add_axes([(kx + e_ * 13 + pad_y) / FW, (1.2 + pad_y) / FH, icon_sz / FW, icon_sz / FH])
            ax.axis("off")
            ax.imshow(make_legend_icon(el))
            fig.text((kx + e_ * 13 + 4.0) / FW, 2.8 / FH, el, va="center", fontsize=7)

        fig.savefig(HERE / f"{figname}.png", dpi=600, facecolor="white")
        fig.savefig(HERE / f"{figname}.svg", facecolor="white")
        fig.savefig(HERE / f"{figname}_preview.png", dpi=200, facecolor="white")
        plt.close(fig)
        print(f"Saved {figname} ({title}, n={len(idx)}, {FW}x{FH:.1f} mm)", flush=True)

df_rec = pd.DataFrame(records)
df_rec.to_csv(HERE / "S17_S22_panel_verification.csv", index=False, encoding="utf-8-sig")

print("Total panels:", len(df_rec))
print("All match reference counts:", bool(df_rec["matches_reference_counts"].all()))
print("Unique CONTCAR SHA256:", df_rec["contcar_sha256"].nunique())
print("Unique tile image SHA256:", df_rec["tile_image_sha256"].nunique())
if df_rec["contcar_sha256"].nunique() != len(df_rec):
    dups = df_rec[df_rec.duplicated("contcar_sha256", keep=False)]
    print("DUPLICATE CONTCARs:", dups[["figure", "panel_label", "directory", "contcar_sha256"]])
if df_rec["tile_image_sha256"].nunique() != len(df_rec):
    dups = df_rec[df_rec.duplicated("tile_image_sha256", keep=False)]
    print("DUPLICATE IMAGES:", dups[["figure", "panel_label", "directory", "tile_image_sha256"]])
