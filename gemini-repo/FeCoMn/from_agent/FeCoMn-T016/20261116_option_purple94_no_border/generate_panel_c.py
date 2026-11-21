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
BASE = OUT.parent/'20261116_final_gray_dashed/source'
STEM = 'Figure_4_20261116_A_straight_OOH1_V2'
W, HC, GAP, OLD_H = 177.8, 36.0, 3.0, 178.0
STAMP = '20261116_option_purple94_no_border'
plt.rcParams.update({'font.family':'Arial','font.size':8,'text.color':'black',
 'mathtext.fontset':'custom','mathtext.rm':'Arial','mathtext.it':'Arial:italic',
 'mathtext.bf':'Arial:bold','svg.fonttype':'none','axes.unicode_minus':True})

fig = plt.figure(figsize=(W/25.4, HC/25.4), facecolor='white')
ax = fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(HC,0)
ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(FancyBboxPatch((13,0),148,70,boxstyle='square,pad=0',facecolor='#8f8bc0',edgecolor='none',alpha=0.06,zorder=-10))

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
def sphere(x,y,r,color):
    ax.add_patch(Circle((x,y),r,facecolor=color,edgecolor='#bdb6c3' if color=='#faf9fc' else color,linewidth=.5,zorder=6))

def stick(p1,p2,color):
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color=color,lw=.9,zorder=4,solid_capstyle='round')

def slab(x,y,faded=False,width=8.4):
    ax.add_patch(FancyBboxPatch((x-width/2,y+2.2),width,1.,boxstyle='round,pad=0,rounding_size=.4',
                    facecolor='#c7c3cd' if faded else '#b9b4c0',edgecolor='none',zorder=2))

def model(kind,x,y,faded=False,highlight=False):
    oc='#eb687b'
    bc='#c7c3cd' if faded else '#a5566a'
    def O(xx,yy,r=1.2):sphere(xx,yy,r,oc)
    def H(xx,yy,r=.72):sphere(xx,yy,r,'#faf9fc')
    slab(x,y,faded,width=13.0 if kind=='2water' else 8.4)
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
    elif kind in ('water','2water'):
        for center in (x-3.4,x+3.4) if kind=='2water' else (x,):
            for dx in (-1.7,1.7):stick((center,y-.4),(center+dx,y-1.9),bc)
            O(center,y-.4)
            for dx in (-1.7,1.7):H(center+dx,y-1.9)
        ax.add_patch(FancyArrowPatch((x+(8 if kind=='2water' else 3.4),y),(x+(8 if kind=='2water' else 3.4),y-3.2),arrowstyle='->',shrinkA=0,shrinkB=0,mutation_scale=6,color='#bbb6c3' if faded else '#8f849b',lw=.65))



from matplotlib.patches import FancyArrowPatch
ax.text(7,1,'c',fontsize=10,fontweight='bold',ha='center',va='top')

Ocol='#eb687b'; Hcol='#faf9fc'; purple='#8f8bc0'; red='#eb687b'
def atom(x,y,hydrogen=False):
    ball(x,y,1.2075 if hydrogen else 2.185,Hcol if hydrogen else Ocol,edge='#aaa4ad' if hydrogen else Ocol)
def bond(x1,y1,x2,y2):
    ax.plot([x1,x2],[y1,y2],color='#a49ba6',lw=.9,zorder=3)
def surface(x,y,width=13):
    ax.plot([x-width/2,x+width/2],[y+3.3,y+3.3],color='#a8a4ad',lw=1.1,solid_capstyle='round')
    for xx in np.arange(x-width/2+.5,x+width/2-.4,1.5):
        ax.plot([xx-.65,xx+.25],[y+4.65,y+3.45],color='#a8a4ad',lw=.55,solid_capstyle='round')
def species(x,y,kind,label):
    if kind!='O2':surface(x,y,width=16 if kind=='pair' else 13)
    if kind=='O2':
        bond(x-1,y-2.4,x+1,y);atom(x-1,y-2.4);atom(x+1,y)
    elif kind=='OOH':
        bond(x-.9,y,x+.8,y-2.7);bond(x+.8,y-2.7,x-.4,y-4.4)
        atom(x-.9,y);atom(x+.8,y-2.7);atom(x-.4,y-4.4,True)
    elif kind=='O':atom(x,y)
    elif kind=='OH':
        bond(x,y,x-1.7,y-2);atom(x,y);atom(x-1.7,y-2,True)
    elif kind=='water':
        for dx in [-1.8,1.8]:bond(x,y,x+dx,y-1.9)
        atom(x,y)
        for dx in [-1.8,1.8]:atom(x+dx,y-1.9,True)
    elif kind=='2O':
        for dx in [-3,3]:
            bond(x+dx,y,x+dx,y+3);atom(x+dx,y)
    elif kind=='pair':
        for dx in [-3,3]:bond(x+dx,y,x+dx,y+3);atom(x+dx,y)
        bond(x+3,y,x+4.6,y-1.9);atom(x+4.6,y-1.9,True)
    txt(x,y+7.6,label,color='black')
def arrow(p,q,color,rad=0):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=8,linewidth=1.575,color=color,connectionstyle=f'arc3,rad={rad}',shrinkA=0,shrinkB=0))

# Simplified pathway schematic; arrows indicate intermediate sequence, not balanced elementary steps.
species(17,32,'O2',r'O$_2$')
for x,kind,label in [(49,'OOH','OOH*'),(83,'O','O*'),(117,'OH','OH*')]:species(x,21,kind,label)
species(49,48,'2O','O* + O*')
species(83,48,'pair','O* + OH*')
# Separate hydroxyl state for the dissociative route before a shared product.
surface(117,48,16)
for dx in [-3,3]:
    bond(117+dx,48,117+dx-1.7,46);atom(117+dx,48);atom(117+dx-1.7,46,True)
txt(117,55.6,'2OH*')
# Common water product: no adsorption bar on a released molecule.
for dx in [-1.8,1.8]:bond(156,34,156+dx,32.1)
atom(156,34)
for dx in [-1.8,1.8]:atom(156+dx,32.1,True)
txt(156,41.6,r'H$_2$O')
for p,q in [((26,28),(40,22)),((58,21),(74,21)),((92,21),(108,21)),((126,22),(147,31))]:arrow(p,q,red)
for p,q in [((26,36),(40,46)),((59,48),(73,48)),((93,48),(107,48)),((126,47),(147,37))]:arrow(p,q,purple)
ax.add_patch(FancyBboxPatch((42,7.1080139373),14,24.3902439024,boxstyle='round,pad=0,rounding_size=1.1',edgecolor=red,facecolor='#fcf0f3',linewidth=.8,zorder=0))

arrow((123,7.5),(131,7.5),red);txt(133,7.5,'Associative pathway',ha='left')
arrow((123,13.5),(131,13.5),purple);txt(133,13.5,'Dissociative pathway',ha='left')
ball(106,7.5,1.725,Ocol,edge=Ocol)
txt(109.5,7.5,'O',ha='left')
ball(106,13.5,1.2075,Hcol,edge='#aaa4ad')
txt(109.5,13.5,'H',ha='left')
from matplotlib.transforms import Affine2D
# Tighten vertical positions while retaining round atoms, font sizes, and width.
sy=.574
for t in ax.texts:
    x,y=t.get_position();t.set_position((x,y*sy))
for line in ax.lines:
    line.set_ydata(np.asarray(line.get_ydata())*sy)
for patch in ax.patches:
    if isinstance(patch,Circle):
        x,y=patch.center;patch.center=(x,y*sy)
    else:
        patch.set_transform(Affine2D().scale(1,sy)+ax.transData)
fig.savefig(OUT/f'Figure_4c_{STAMP}_editable.svg',facecolor='white')
fig.savefig(OUT/f'Figure_4c_{STAMP}_preview.png',dpi=240,facecolor='white')
plt.rcParams['svg.fonttype']='path'
fig.savefig(OUT/f'Figure_4c_{STAMP}_Arial_paths.svg',facecolor='white')
plt.close(fig)
print('Exported panel c preview and two SVG versions. a/b untouched.')
