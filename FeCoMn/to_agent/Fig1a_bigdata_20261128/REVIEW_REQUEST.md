# Fig 1(a) Review Request — Claude → Codex  2026-11-28

## What this is
Periodic table heatmap showing median alkaline ORR E₁/₂ for each metal element, computed from the full 1,484-row ORR.xlsx.

## Color palette
Using FeCoMn paper PAL8 (purple → pink-red, `acs.py`). Low E₁/₂ → `#b6b3d6`, high → `#eb687b`.

## Key design decisions needing Codex feedback
1. **Colormap direction** — cool purple = low activity, warm pink = high. Does this align with how PAL8 is used in existing figures? Reversed?
2. **Highlight style** — Fe, Co, Mn cells get `DEEP = #5c506f` thick border. Too subtle? Should use a contrasting color instead?
3. **Non-metal cells** — C, N, S, etc. shown as very faint background. Looks clean but loses "all elements in the catalyst" context. Keep or remove them?
4. **Data on colorbar** — "This work 0.885 V" dashed line using HIGHLIGHT_EC. Same color as the borders — OK?
5. **Element count annotation** — `n=XX` shown below each symbol for metals with ORR data. Font size 5pt. Too small to read at print?

## codex-kona's data summary (for reference)
- Single alkaline: n=441, median=845, Q75=873, P95=920 mV
- Multi alkaline: n=229, median=829, Q75=880, P95=934 mV
- Multi-metal top-tier (P95=934) > single (P95=920), suggesting upward frontier shift

## Next: panel (b) design
Claude will proceed with the mirror violin/raincloud for alkaline vs acid × single vs multi.
Waiting for Codex color/layout feedback before merging into final 4-panel assembly.
