"""Append a vector schematic to the approved A figure; never redraw a or b."""
from pathlib import Path
import re, json, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from PIL import Image

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
REPO = next((p for p in OUT.parents if (p/'FeCoMn/data/SEIRAS_20241021_1-2').is_dir()), None)
BASE = REPO/'FeCoMn/from_agent/FeCoMn-T015/20261116_A_single_bend1' if REPO else ROOT/'outputs/T015_A_single_bend_20261116'
STEM = 'Figure_4_20261116_A_single_bend1_V2'
W, HC, GAP, OLD_H = 177.8, 45.0, 3.0, 178.0
STAMP = '20261116_T016_horizontal'
plt.rcParams.update({'font.family':'Arial','font.size':8,'text.color':'black',
 'mathtext.fontset':'custom','mathtext.rm':'Arial','mathtext.it':'Arial:italic',
 'mathtext.bf':'Arial:bold','svg.fonttype':'none','axes.unicode_minus':True})

fig = plt.figure(figsize=(W/25.4, HC/25.4), facecolor='white')
ax = fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(HC,0)
ax.set_aspect('equal'); ax.axis('off')

def txt(x,y,s,**kw):
    return ax.text(x,y,s,fontsize=8,ha=kw.pop('ha','center'),va=kw.pop('va','center'),**kw)

def ball(x,y,r,fill,alpha=1,edge=None):
    ax.add_patch(Circle((x,y),r,facecolor=fill,edgecolor=edge or fill,
                        linewidth=.5,alpha=alpha,zorder=5))

def water(x,y,alpha=1):
    # Same five molecules on both sides: fading is not a count measurement.
    for dx in (-1.836,1.836):
        ax.plot([x,x+dx],[y,y-1.494],color='#b0a4a8',lw=.8,alpha=alpha,zorder=3)
    ball(x,y,1.224,'#eb687b',alpha)
    for dx in (-1.836,1.836):
        ball(x+dx,y-1.494,.774,'white',alpha,edge='#a79b9e')

def ooh(x):
    # No catalytic atom or explicit metal/site bond is represented.
    points=[(x,19.272),(x+.99,16.482),(x+2.79,15.006)]
    ax.plot([p[0] for p in points],[p[1] for p in points],color='#c56a78',lw=.9,zorder=4)
    ball(*points[0],1.278,'#eb687b')
    ball(*points[1],1.278,'#eb687b')
    ball(*points[2],.774,'white',edge='#aa9b9e')

ax.text(7,.55,'c',fontsize=10,fontweight='bold',ha='center',va='top')
for left,face in [(13,'#fdf0f3'),(98,'#f3f1f9')]:
    ax.add_patch(FancyBboxPatch((left,4),63,24,boxstyle='round,pad=0,rounding_size=1.5',
                              facecolor=face,edgecolor='none',zorder=0))
    ax.add_patch(FancyBboxPatch((left+3,20.55),57,2.5,boxstyle='round,pad=0,rounding_size=1.1',
                              facecolor='#b9b8bd',edgecolor='none',zorder=2))
    txt(left+31.5,25.5,'FeCoMn–NC')
txt(17,7.1,'1.2 V',ha='left')
txt(102,7.1,'0 V',ha='left')
for x in (21,32.5,44,55.5,67):
    water(x,13.5,1)
    water(x+85,11.8,.34)
for x in (111,128,145): ooh(x)
txt(154,15.8,'OOH*',color='#c9243f')
txt(87,10.3,'potential\nlowered',linespacing=1.15)
ax.add_patch(FancyArrowPatch((79.6,17),(94.4,17),arrowstyle='-|>',
                            mutation_scale=10,color='#68656d',linewidth=1.1,zorder=3))

def pathway(positions,labels,y,color,highlight=False,dashed=False,clearance=5):
    for xp,label in zip(positions,labels):
        is_ooh=highlight and label=='OOH*'
        txt(xp,y,label,color='#c9243f' if is_ooh else color,
            fontweight='bold' if is_ooh else 'normal')
    for x1,x2 in zip(positions[:-1],positions[1:]):
        ax.add_patch(FancyArrowPatch((x1+clearance,y),(x2-clearance,y),arrowstyle='->',
             mutation_scale=8,color='#404040' if highlight else '#a0a0a0',linewidth=.75,
             linestyle=(0,(2.8,2.4)) if dashed else 'solid'))

txt(44.5,33,'Associative')
txt(129.5,33,'Dissociative',color='#a0a0a0')
pathway([17,30.5,44,57.5,71],[r'O$_2$','OOH*','O*','OH*',r'H$_2$O'],39,'black',highlight=True,clearance=4.5)
pathway([103,120,137,154],[r'O$_2$','2O*','2OH*',r'H$_2$O'],39,'#a0a0a0',dashed=True,clearance=4.5)

csvg=OUT/f'Figure_4c_{STAMP}_editable.svg'
cpng=OUT/f'Figure_4c_{STAMP}_preview.png'
fig.savefig(csvg,facecolor='white');fig.savefig(cpng,dpi=180,facecolor='white')
plt.close(fig)

# Preserve the previous upper schematic exactly; only replace the pathway strip.
UPPER_BASE = (REPO/'FeCoMn/from_agent/FeCoMn-T016/preview_20261116_2' if REPO else ROOT/'outputs/T016_larger_molecules_20261116')
upper_svg=UPPER_BASE/'Figure_4c_20261116_T016_preview2_editable.svg'
upper_png=UPPER_BASE/'Figure_4c_20261116_T016_preview2_preview.png'
new=csvg.read_text(encoding='utf-8');old=upper_svg.read_text(encoding='utf-8')
nm=re.search(r'<svg\b[^>]*>',new);om=re.search(r'<svg\b[^>]*>',old)
upper=old[om.end():old.rfind('</svg>')]
for ident in sorted(set(re.findall(r'\bid="([^"]+)"',upper)),key=len,reverse=True):
    uid='T016_keep_'+ident
    upper=upper.replace('id="'+ident+'"','id="'+uid+'"').replace('href="#'+ident+'"','href="#'+uid+'"').replace('url(#'+ident+')','url(#'+uid+')')
cut=30/25.4*72
clips=f'<defs><clipPath id="keep_upper"><rect width="504" height="{cut}"/></clipPath><clipPath id="replace_lower"><rect y="{cut}" width="504" height="{HC/25.4*72-cut}"/></clipPath></defs>'
newbody=new[nm.end():new.rfind('</svg>')]
csvg.write_text(new[:nm.end()]+clips+'<g clip-path="url(#keep_upper)">'+upper+'</g><g clip-path="url(#replace_lower)">'+newbody+'</g></svg>',encoding='utf-8')
u=Image.open(upper_png).convert('RGB');im=Image.open(cpng).convert('RGB')
cutpx=round(30/25.4*180);im.paste(u.crop((0,0,u.width,cutpx)),(0,0));im.save(cpng,dpi=(180,180))
assert np.array_equal(np.asarray(im)[:cutpx],np.asarray(u)[:cutpx])

def append_svg(original,additional,target):
    old=original.read_text(encoding='utf-8')
    c=additional.read_text(encoding='utf-8')
    cm=re.search(r'<svg\b[^>]*>',c)
    inner=c[cm.end():c.rfind('</svg>')]
    ids=re.findall(r'\bid="([^"]+)"',inner)
    for ident in sorted(set(ids),key=len,reverse=True):
        new='T016c_'+ident
        inner=inner.replace('id="'+ident+'"','id="'+new+'"')
        inner=inner.replace('href="#'+ident+'"','href="#'+new+'"')
        inner=inner.replace('url(#'+ident+')','url(#'+new+')')
    rm=re.search(r'<svg\b[^>]*>',old)
    header=rm.group();new_h=(OLD_H+GAP+HC)/25.4*72
    header=re.sub(r'height="[^"]+"',f'height="{new_h:.9f}pt"',header)
    header=re.sub(r'viewBox="[^"]+"',f'viewBox="0 0 504 {new_h:.9f}"',header)
    old=old[:rm.start()]+header+old[rm.end():]
    start=re.search(r'<svg\b[^>]*>',old).end()
    old=old[:start]+f'\n<rect id="T016_white_canvas" width="504" height="{new_h}" fill="white"/>\n'+old[start:]
    pos=old.rfind('</svg>')
    old=old[:pos]+f'<g id="T016_panel_c" transform="translate(0 {(OLD_H+GAP)/25.4*72:.9f})">\n'+inner+'\n</g>\n'+old[pos:]
    target.write_text(old,encoding='utf-8')

combined=OUT/f'Figure_4_abc_{STAMP}_editable.svg'
append_svg(BASE/f'{STEM}_editable.svg',csvg,combined)

# Exact pixel retention: the approved preview is pasted without scaling/re-rendering.
old=Image.open(BASE/f'{STEM}_preview.png').convert('RGB')
c=Image.open(cpng).convert('RGB')
assert c.width==old.width
height=round((OLD_H+GAP+HC)/25.4*180)
canvas=Image.new('RGB',(old.width,height),'white')
canvas.paste(old,(0,0));canvas.paste(c,(0,round((OLD_H+GAP)/25.4*180)))
preview=OUT/f'Figure_4_abc_{STAMP}_preview.png';canvas.save(preview,dpi=(180,180))
assert np.array_equal(np.asarray(canvas)[:old.height],np.asarray(old))
check={'base':str(BASE/f'{STEM}_editable.svg'),'base_svg_SHA256':hashlib.sha256((BASE/f'{STEM}_editable.svg').read_bytes()).hexdigest(),
 'a_b_preview_pixel_identical':True,'original_canvas_mm':[W,OLD_H],
 'b_height_mm':54,'gap_before_c_mm':GAP,'c_row_mm':[W,HC],
 'c_content_height_mm':37,'pathway_layout':'horizontal','path_row_gap_mm':0,'total_canvas_mm':[W,OLD_H+GAP+HC],
 'c_background_edges_mm':[13,161],'approved_b_edges_mm':[13,161],'alignment_error_mm':[0,0],
 'water_counts_left_right':[5,5],'water_alpha_left_right':[1,.34],
 'OOH_count_right':3,'molecule_linear_scale_vs_preview1':1.8,'water_center_y_left_right_mm':[13.5,11.8],'right_water_to_OOH_vertical_gap_mm':1.208,'catalyst_structure':'abstract grey bar; no Fe/Co/Mn, particles, or M-N4 sites',
 'upper_c_pixels_identical_to_previous_preview':True,'upper_c_original_svg_preserved_by_clip':True,'pathway_strip_starts_mm':30,'scope':'preview only; original figure/data and Word untouched'}
(OUT/'PREVIEW_CHECKS.json').write_text(json.dumps(check,ensure_ascii=False,indent=2),encoding='utf-8')
print('Created c vector + combined preview. Original a/b pixels identical. Canvas177.8x226mm; b54mm; ccontent37mm; aligned edges13/161mm.')
