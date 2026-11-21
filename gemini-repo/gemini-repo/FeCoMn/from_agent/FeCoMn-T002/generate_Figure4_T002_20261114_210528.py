"""T002 + addendum1: re-use T001 processing/layout; modify only authorized artists.
Changes relative to T001:
1) a's axvspan patches removed (3), axvline markers removed (3307,1633).
2) c's 1235–1195 rectangle removed (1).
3) a's 13 spectrum colors + potential-gradient image/arrowhead changed only.
No T001 file is overwritten. b/c colors, geometry, fonts, data remain unchanged.
"""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
OUT=Path(__file__).resolve().parent
REPO=OUT.parents[2]
BASE=REPO/'FeCoMn/from_agent/FeCoMn-T001/generate_Figure4_20261114_204757.py'
source=BASE.read_text(encoding='utf-8')
# Run exactly T001's processing and layout before its export/blue-shift alternative.
ns={'__file__':__file__,'__name__':'__main__'}
exec(compile(source.split('def save(stem):')[0],str(BASE),'exec'),ns)
fig=ns['fig'];a_axes=ns['axes'];gradient=ns['ga'];c=fig.axes[6]
assert len(a_axes)==3 and len(fig.axes)==8
removed_shadows=0;removed_lines=0
for ax in a_axes:
 for patch in list(ax.patches):patch.remove();removed_shadows+=1
 for line in list(ax.lines):
  x=np.asarray(line.get_xdata())
  if len(x)==2 and np.all(x==x[0]) and x[0] in [3307,1633]:line.remove();removed_lines+=1
assert removed_shadows==3 and removed_lines==2
assert len(c.patches)==1;c.patches[0].remove()
# Exact processing arrays compare to delivered T001 (not only window statistics).
before=np.load(BASE.parent/'processing_arrays.npz');after=np.load(OUT/'processing_arrays.npz')
array_checks={k:bool(np.array_equal(before[k],after[k])) for k in before.files};assert all(array_checks.values())
curves=[]
for ax in a_axes:
 lines=[line for line in ax.lines if len(line.get_xdata())>100]
 assert len(lines)==13;curves.append(lines)
checks=[]
STEM='Figure_4_20261114_210528'
for suffix,deep,light in [('C_purple','#5d5aa0','#d0cce5'),('D_red','#b8394d','#f6bcc4')]:
 cmap=LinearSegmentedColormap.from_list('a_'+suffix,[deep,light])
 for lines in curves:
  for i,line in enumerate(lines):line.set_color(cmap(i/12))
 gradient.images[0].set_cmap(cmap)
 assert len(gradient.patches)==1;gradient.patches[0].set_facecolor(deep);gradient.patches[0].set_edgecolor(deep)
 plt.rcParams['svg.fonttype']='none';fig.savefig(OUT/(STEM+'_editable_'+suffix+'.svg'),dpi=600)
 fig.savefig(OUT/(STEM+'_'+suffix+'.png'),dpi=600)
 fig.savefig(OUT/(STEM+'_preview_'+suffix+'.png'),dpi=180)
 plt.rcParams['svg.fonttype']='path';fig.savefig(OUT/(STEM+'_Arial_paths_'+suffix+'.svg'),dpi=600)
 checks.append({'variant':suffix,'low_E_deep':deep,'high_E_light':light})
(OUT/'MODIFICATION_CHECKS.json').write_text(json.dumps({'base_script_relative':str(BASE.relative_to(REPO)),'base_script_sha256':hashlib.sha256(BASE.read_bytes()).hexdigest(),'identical_arrays_vs_T001':array_checks,'removed_a_shadows':removed_shadows,'removed_a_vertical_lines':removed_lines,'removed_c_box':1,'variants':checks},ensure_ascii=False,indent=2),encoding='utf-8')
print('Data arrays identical:',array_checks)
