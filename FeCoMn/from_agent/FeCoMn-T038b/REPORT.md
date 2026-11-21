# T038b Bader Charge Analysis Report

**Date**: 2026-11-20  
**Machine**: Genkai (九州大学)  
**VASP version**: 6.6.0  
**Task**: Static single-point (NSW=0, LAECHG=.TRUE.) for charge decomposition and electronic structure  
**Status**: Revised after Antigravity independent verification (commit c552221); 4 prior extraction errors corrected.

---

## Structures

| Label | Description | Atoms | Formula |
|-------|-------------|-------|---------|
| A | FCM clean (full model) | 238 | C174N4Fe27Co32Mn1 |
| B | MnNC clean | 179 | C174N4Mn1 |
| Ap | FeCo particle only (carved from A) | 59 | Fe27Co32 |
| As | MnNC substrate only (carved from A) | 179 | C174N4Mn1 |
| C | FCM_base_full (8 O* on FeCo) | 246 | C174N4Fe27Co32Mn1O8 |

Ap/As: carved from A CONTCAR (same geometry). B: independent MnNC relaxation.  
C: from FeCoMn_electronic_20261023/FCM_base_full.  
All T038b single points: ISTART=0, ICHARG=2 (start from scratch; no WAVECAR continuation).

**Like-for-like comparison is A vs As** (identical geometry, only FeCo particle added/removed).

---

## Total Energies (Genkai, VASP 6.6.0)

| Structure | E_TOTEN (eV) | Electronic steps |
|-----------|-------------|-----------------|
| A: FCM clean | -2066.61471167 | 53 (converged) |
| B: MnNC clean | -1661.28618832 | 49 (converged) |
| Ap: FeCo particle | -401.30978923 | 46 (converged) |
| As: MnNC substrate | -1661.06300115 | 28 (converged) |

**Frozen-geometry interaction energy** (A vs Ap+As):  
E_int = E(A) − E(Ap) − E(As) = −2066.6147 − (−401.3098) − (−1661.0630) = **−4.242 eV**

> This is the frozen-geometry interaction energy (structures carved from A without relaxation). It differs from the relaxed binding energy reported in SI (−3.73 eV), which allows full structural relaxation of separated fragments.

---

## Mn Magnetic Moments

Mn atom is atom 238 in A/C (238-atom cell) and atom 179 in As/B (179-atom cell).  
Values from OUTCAR `magnetization (x)` section (last SCF cycle, d-column):

| Structure | Mn atom# | tot (μB) | d-only (μB) | Total system (μB) |
|-----------|---------|---------|------------|-----------------|
| A: FCM clean | 238 | **+3.112** | +3.020 | +139.112 |
| As: MnNC substrate | 179 | **+3.125** | +3.032 | +3.052 |
| B: MnNC clean | 179 | **−3.115** | −3.023 | −3.031 |
| C: FCM_base_full | 238 | **+3.116** | — | — |

All four static calculations are in the **same high-spin state** (|μ_Mn| ≈ 3.11–3.13 μB).  
B_static is anti-aligned (−3.115 μB vs parent's +3.031 μB): same magnetic branch, opposite spin labeling (time-reversal equivalent).  
A total magnetization (139.112 μB) matches FCM_clean parent (139.109 μB) to <0.003 μB: A is in the same state as the parent.

**A vs As: Δμ_Mn = −0.013 μB** (negligible). The FeCo particle does not change Mn spin state.

> **Correction note**: The prior report (commit da0191a) listed A Mn = 1.788 μB (a Co atom), As Mn = −0.034 μB (an N atom), B Mn = +0.034 μB (an N atom). These were atom-index extraction errors. The correct values are from OUTCAR's magnetization-per-ion block, selecting the Mn atom by its sequence number.

---

## Bader Charges

### Mn charge

| Structure | Mn Bader charge (e) | Note |
|-----------|--------------------|-|
| A: FCM clean | 11.6341 | |
| As: MnNC substrate (carved from A) | 11.6270 | same geometry as A |
| **A − As** | **+0.0070** | FeCo slightly donates electrons to Mn |
| B: MnNC clean (independent geometry) | 11.6672 | different geometry, not direct comparison |
| C: FCM_base_full (8 O* on FeCo) | 11.6319 | |

The FeCo particle slightly donates electron density to Mn (+0.007 e, A vs As).

### 4N Bader charges (supplement)

| Structure | 4N total Bader (e) | Note |
|-----------|------------------|-|
| A | 25.2344 | |
| As | 25.2288 | |
| **A − As (4N)** | **+0.0056** | |
| B | 25.1597 | |

Mn + 4N together gain **+0.0126 e** upon FeCo binding (A vs As).

### Fe and Co charges

| Structure | Fe avg (e) | Co avg (e) |
|-----------|-----------|-----------|
| Ap: FeCo particle alone | 7.8073 | 9.1626 |
| A: FCM full model | 7.7829 | 9.1333 |

Particle Fe/Co become slightly more oxidized in FCM (particle donates electrons to substrate, consistent with +0.007 e gain on Mn).

### Electron count validation

| Structure | Bader total e | Expected | Check |
|-----------|--------------|---------|-------|
| A | 1233.00 | 1233 | ✓ |
| B | 729.00 | 729 | ✓ |
| Ap | 504.00 | 504 | ✓ |
| As | 729.00 | 729 | ✓ |
| C | 1281.00 | 1281 | ✓ |

---

## Mn 3d Band Centers

Recomputed with corrected LORBIT=11 column indices (3d = v[9:19], dz² = v[13]+v[14]; integration window [−8, 0] eV):

| Structure | 3d center (eV) | dz² center (eV) |
|-----------|---------------|----------------|
| A: FCM clean | −3.089 | −3.024 |
| As: MnNC substrate | −3.114 | −3.037 |
| B: MnNC clean | −3.111 | −3.039 |
| **A − As** | **+0.025** | **+0.013** |

The dz² orbital shifts upward by +0.013 eV upon FeCo binding (A vs As). This small but consistent shift indicates weak hybridization between Mn-dz² and FeCo d-states.

> **Correction note**: Prior report listed A dz² = −2.921 eV, As dz² = −3.014 eV (Δ = +0.093 eV). These used wrong column indices (v[10:20] for 3d, v[14]+v[15] for dz²), off-by-one relative to the correct LORBIT=11 format. The corrected values reduce Δdz² by ~7×.

---

## Differential Charge (Δρ = ρ(A) − ρ(Ap) − ρ(As))

Grid: [252, 240, 360], net residual = 7.45 × 10⁻⁸ e (numerical precision).

| Region definition | Δq (e) |
|-------------------|-------|
| Mn sphere (r ≤ 2.0 Å) | +0.0062 |
| Mn sphere (r ≤ 3.0 Å) | +0.0078 |
| Mn(r≤1.8 Å) ∪ 4N(r≤1.5 Å) | +0.0074 |
| Mn-centered cylinder (R_xy ≤ 3.0 Å, \|z−z_Mn\| ≤ 3.0 Å) | +0.0090 |
| **Planar average slab (whole xy, \|z−z_Mn\| ≤ 3.0 Å)** | **(+0.040 e — includes carbon interface, not Mn-N4 specific)** |

The true Mn-N4 local charge gain is **+0.006–0.009 e**, consistent with Bader ΔMn = +0.007 e.

> **Correction note**: Prior report stated "+0.040 e in Mn-N4 region". This was the planar-average slab integral (entire 22 × 21 Å² cross-section), which includes the FeCo/MnNC carbon interface polarization. The correct Mn-N4 local 3D integrals are 6–9 times smaller.

---

## Summary Table

| Property | A (FCM) | As (MnNC carved) | A − As | B (MnNC free) |
|----------|---------|-----------------|--------|--------------|
| Mn Bader (e) | 11.634 | 11.627 | **+0.007** | 11.667 |
| 4N Bader (e) | 25.234 | 25.229 | +0.006 | 25.160 |
| Mn magmom (μB) | +3.112 | +3.125 | −0.013 | −3.115 |
| Mn 3d center (eV) | −3.089 | −3.114 | +0.025 | −3.111 |
| Mn dz² center (eV) | −3.024 | −3.037 | +0.013 | −3.039 |
| Δρ Mn-N4 (e) | — | — | +0.006–0.009 | — |

**Conclusions**:
1. FeCo particle binding slightly donates electrons to Mn (+0.007 e) and to Mn+4N (+0.013 e).
2. Mn remains high-spin (|μ| ≈ 3.1 μB) regardless of FeCo; FeCo does not change Mn spin state (Δ = −0.013 μB).
3. Mn dz² band shifts up 0.013 eV upon FeCo binding (small hybridization signal).
4. Frozen-geometry interaction energy −4.242 eV; relaxed binding energy (SI) −3.73 eV.
5. All effects are small and consistent: the FeCo particle has negligible direct electronic effect on Mn in the absence of O* ligands. This supports the main paper conclusion using C vs C_support as the primary evidence.

---

## Files Location (Genkai)

```
/home/pj25000114/ku50002299/FeCoMn_T038b_20261119/
├── A_static/   ACF.dat, BCF.dat, CHGCAR_sum, bader.log, DOSCAR, OUTCAR
├── B_static/   ACF.dat, BCF.dat, CHGCAR_sum, bader.log, DOSCAR, OUTCAR
├── Ap_static/  ACF.dat, BCF.dat, CHGCAR_sum, bader.log, OUTCAR
└── As_static/  ACF.dat, BCF.dat, CHGCAR_sum, bader.log, DOSCAR, OUTCAR
/home/pj25000114/ku50002299/FeCoMn_electronic_20261023/FCM_base_full/
└── ACF.dat  (C structure Bader, Mn atom 238 = 11.63 e)
```

---

*Generated by Claude Code; independently verified by Antigravity (commit c552221), 2026-11-20.*
