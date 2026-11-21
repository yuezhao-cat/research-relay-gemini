"""Apply the SI CHE reference to composition-matched T025 states."""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
with (HERE / 'manifest.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = {r['name']: r for r in csv.DictReader(f)}

H2, H2O = -6.833, -14.327

def calc(background, ooh, o, oh):
    b, a, c, d = (float(rows[x]['energy_sigma0']) for x in
                  (background, ooh, o, oh))
    g_ooh = a-b-2*H2O+1.5*H2+0.403
    g_o = c-b-H2O+H2+0.066
    g_oh = d-b-H2O+0.5*H2+0.343
    steps = (g_ooh-4.92, g_o-g_ooh, g_oh-g_o, -g_oh)
    ul = -max(steps)
    return dict(background=b, OOH=a, O=c, OH=d,
                G_OOH=g_ooh, G_O=g_o, G_OH=g_oh,
                **{f'dG{i}':v for i,v in enumerate(steps,1)},
                largest_step=steps.index(max(steps))+1, UL=ul, eta=1.23-ul)

for name, args in {
    'C': ('FCM_Mn_OHb','FCM_Mn_OOH_OHb','FCM_Mn_O_OHb','FCM_Mn_OH_OHb'),
    'D': ('MnNC_clean','MnNC_OOH','MnNC_O','MnNC_OH'),
}.items():
    print(name, calc(*args))
