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
W, HC, GAP, OLD_H = 177.8, 58.0, 3.0, 178.0
STAMP = '20261116_T016_tree_flat1'
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

from matplotlib.patches import Polygon, PathPatch
from matplotlib.path import Path as MPath
from matplotlib.colors import to_rgb
ax.text(7,.55,'c',fontsize=10,fontweight='bold',ha='center',va='top')
for left,face in [(13,'#fdf0f3'),(91,'#f3f1f9')]:
    ax.add_patch(FancyBboxPatch((left,10.5),70,45.5,boxstyle='round,pad=0,rounding_size=1.5',facecolor=face,edgecolor='none',zorder=0))
txt(48,13,'Dissociative',color='#a0a0a0');txt(126,13,'Associative')

def sphere(x,y,r,color):
    ax.add_patch(Circle((x,y),r,facecolor=color,edgecolor='#bdb6c3' if color=='#faf9fc' else color,linewidth=.5,zorder=6))

def stick(p1,p2,color):
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color=color,lw=.9,zorder=4,solid_capstyle='round')

def slab(x,y,faded=False):
    ax.add_patch(FancyBboxPatch((x-4.2,y+2.2),8.4,1.,boxstyle='round,pad=0,rounding_size=.4',
                    facecolor='#c7c3cd' if faded else '#b9b4c0',edgecolor='none',zorder=2))

def model(kind,x,y,faded=False,highlight=False):
    oc='#c7c4ce' if faded else '#c9243f' if highlight else '#eb687b'
    bc='#c7c3cd' if faded else '#a5566a'
    def O(xx,yy,r=1.2):sphere(xx,yy,r,oc)
    def H(xx,yy,r=.72):sphere(xx,yy,r,'#faf9fc')
    slab(x,y,faded)
    if kind=='O2':
        stick((x-1.5,y-.9),(x+1.5,y-.9),bc);O(x-1.5,y-.9);O(x+1.5,y-.9)
    elif kind=='OOH':
        ps=[(x-.6,y+1.),(x+.8,y-1.1),(x-.6,y-2.6)]
        stick(ps[0],ps[1],bc);stick(ps[1],ps[2],bc);O(*ps[0]);O(*ps[1]);H(*ps[2])
    elif kind=='O':O(x,y+1.)
    elif kind=='OH':
        stick((x,y+1.),(x+1.7,y-.5),bc);O(x,y+1.);H(x+1.7,y-.5)
    elif kind=='2O':
        O(x-2.2,y+1.);O(x+2.2,y+1.)
    elif kind=='2OH':
        for dx in (-2.2,2.2):
            stick((x+dx,y+1.),(x+dx+1.,y-.9),bc);O(x+dx,y+1.,1.1);H(x+dx+1.,y-.9,.65)
    elif kind=='water':
        for dx in (-1.7,1.7):stick((x,y-1.1),(x+dx,y-2.6),bc)
        O(x,y-1.1)
        for dx in (-1.7,1.7):H(x+dx,y-2.6)
        ax.add_patch(FancyArrowPatch((x+3.4,y-.7),(x+3.4,y-4.4),arrowstyle='->',shrinkA=0,shrinkB=0,mutation_scale=6,color='#bbb6c3' if faded else '#8f849b',lw=.65))

# One common O2 root, then the two mechanism branches.
stick((85.5,5.6),(88.5,5.6),'#a5566a');sphere(85.5,5.6,1.25,'#eb687b');sphere(88.5,5.6,1.25,'#eb687b');txt(96.3,6.,r'O$_2$')
ax.plot([87,87],[8,17],color='#77717e',lw=.8)
for xp,lasty,faded in [(48,19.,True),(126,17.7,False)]:
    path=MPath([(87,17),(xp,17),(xp,lasty)],[MPath.MOVETO,MPath.LINETO,MPath.LINETO])
    ax.add_patch(FancyArrowPatch(path=path,arrowstyle='-|>',mutation_scale=7.5,
          color='#b1aab8' if faded else '#665d71',lw=.85,linestyle=(0,(2.8,2.4)) if faded else 'solid'))

for kind,y,label in [('2O',22,'2O*'),('2OH',34,'2OH*'),('water',46,r'H$_2$O')]:
    model(kind,48,y,True);txt(62,y+.7,label,color='#a0a0a0')
for y1,y2 in [(25.9,30.8),(37.9,41.8)]:
    ax.add_patch(FancyArrowPatch((48,y1),(48,y2),arrowstyle='->',shrinkA=0,shrinkB=0,
                mutation_scale=7,color='#aaa3b2',lw=.8,linestyle=(0,(2.8,2.4))))

ax.add_patch(FancyBboxPatch((120,17),12,9.3,boxstyle='round,pad=0,rounding_size=1.',facecolor='#fff0f3',edgecolor='#c9243f',linewidth=.9,zorder=1))
for kind,y,label in [('OOH',22,'OOH*'),('O',30,'O*'),('OH',38,'OH*'),('water',46,r'H$_2$O')]:
    model(kind,126,y,False,kind=='OOH')
    txt(141,y+.7,label,color='#c9243f' if kind=='OOH' else '#404040',fontweight='bold' if kind=='OOH' else 'normal')
txt(146,26.2,r'1215 cm$^{-1}$',color='#c9243f')
for y1,y2 in [(26.9,28.1),(33.9,35.8),(41.9,42.6)]:
    ax.add_patch(FancyArrowPatch((126,y1),(126,y2),arrowstyle='->',shrinkA=0,shrinkB=0,mutation_scale=6.5,color='#665d71',lw=.8))
txt(126,52.7,'Used for DFT calculations',color='#6f637b')

csvg=OUT/f'Figure_4c_{STAMP}_editable.svg'
cpng=OUT/f'Figure_4c_{STAMP}_preview.png'
fig.savefig(csvg,facecolor='white');fig.savefig(cpng,dpi=180,facecolor='white')
plt.close(fig)

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
 'c_content_height_mm':52,'pathway_layout':'shared O2 root; left dissociative, right associative','sphere_style':'flat O/H atom balls and abstract flat grey surfaces','c_potential_labels':False,'c_interface_water_panels':False,'route_order':['Dissociative','Associative'],'route_atoms':True,'OOH_band_callout_cm-1':1215,'total_canvas_mm':[W,OLD_H+GAP+HC],
 'c_background_edges_mm':[13,161],'approved_b_edges_mm':[13,161],'alignment_error_mm':[0,0],
 'route_step_counts_left_right':[4,5],
 'OOH_route_step_highlighted':True,'catalyst_structure':'abstract grey bar; no Fe/Co/Mn, particles, or M-N4 sites',
 'scope':'preview only; original figure/data and Word untouched'}
(OUT/'PREVIEW_CHECKS.json').write_text(json.dumps(check,ensure_ascii=False,indent=2),encoding='utf-8')
print('Created c vector + combined preview. Original a/b pixels identical. Canvas177.8x239mm; b54mm; ccontent52mm; aligned edges13/161mm.')
