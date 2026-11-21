
from pathlib import Path
from lxml import etree as E
import json,re,copy
OUT=Path(__file__).resolve().parent
SOURCE=OUT/'source_078V.svg'
NS={'s':'http://www.w3.org/2000/svg'};S=NS['s'];r=E.parse(str(SOURCE));root=r.getroot()
def el(gid):return r.xpath('//*[@id="'+gid+'"]')[0]
def remove(gid):
 q=el(gid);q.getparent().remove(q)
def text(gid,string=None,x=None,y=None,fill=None,rotate=None):
 t=el(gid).find('s:text',NS)
 if string is not None:
  for q in list(t):t.remove(q)
  t.text=string
 if x is not None:t.set('x',str(x))
 if y is not None:t.set('y',str(y))
 t.attrib.pop('transform',None)
 if fill is not None:t.set('style',t.get('style','')+';fill:'+fill)
 if rotate:t.set('transform',f'rotate({rotate} {t.get("x")} {t.get("y")})')
 return t
for gid in ['text_14','text_15','text_17','text_18','text_46','text_74']:remove(gid)
for t in r.xpath('//s:text',namespaces=NS):
 if t.text:
  for a,b in [('FeCoMn-NC','FeCoMn–NC'),('FeCo-NC','FeCo–NC'),('Mn-NC','Mn–NC')]:t.text=t.text.replace(a,b)
# Preserve the approved highlighted-line styles, not the old solid-line source styles.
for gid,color,dash in [('line2d_62','#f2a78d','1.6,1.6'),('line2d_64','#7a2a3a','6.0,2.4')]:
 q=el(gid).find('s:path',NS);q.set('style',f'fill:none;stroke:{color};stroke-width:1.6;stroke-dasharray:{dash}')
# Approved interior labels, near their matching curves.
for gid,x,y,col in [('text_16',63,107,'#8f8bc0'),('text_48',236,105,'#8f8bc0'),('text_47',314,132.5,'#eb687b'),('text_75',471,81.8,'#8c8c8c'),('text_76',401,108,'#8f8bc0'),('text_77',399,65,'#f2a78d'),('text_78',417,49,'#e0846c')]:text(gid,x=x,y=y,fill=col)
text('text_31','8O*+Mn–O*',x=97.5,y=221.5,rotate=10)
text('text_32','8O*+Mn–OH*',x=112.8,y=262.0,rotate=14)
# Name-label backgrounds: exact approved raster positions in SVG coordinates.
for gid,box in [('text_28',[948,1634,1351,1703]),('text_58',[2423,1634,2736,1703]),('text_88',[3879,1634,4120,1702])]:
 a,b,c,d=[v/ (4200/504) for v in box];group=el(gid);parent=group.getparent();rect=E.Element('{'+S+'}rect',x=str(a),y=str(b),width=str(c-a),height=str(d-b),fill='#f2f2f2',id='name_background_'+gid);parent.insert(parent.index(group),rect)
# g title matches the approved parenthesized notation.
text('text_114','FeCoMn–NC (8O* + Mn–OH*)',x=101.82,y=371.1)
# h: move labels and structures, keep all energy values/step positions.
el('text_105').set('transform','translate(0 -9)')
for gid,dy in [('axes_16',-5.77861),('axes_17',-3.812862),('axes_18',-1.847113)]:el(gid).set('transform',f'translate(0 {dy})')
g=el('patch_46')
for q in list(g):g.remove(q)
x=262.034646;tip=410.602807
E.SubElement(g,'{'+S+'}path',d=f'M {x} 421.6 L {x} {tip+2.8}',style='fill:none;stroke:#eb687b;stroke-width:0.9;stroke-linecap:round')
E.SubElement(g,'{'+S+'}path',d=f'M {x-1.4} {tip+2.8} L {x} {tip} L {x+1.4} {tip+2.8} Z',style='fill:#eb687b;stroke:#eb687b;stroke-width:0.9;stroke-linejoin:round')
# h legend: the approved PNG uses names only and right alignment.
remove('legend_1')
legend=E.SubElement(el('axes_15'),'{'+S+'}g',id='h_legend_approved')
for i,(name,color,lw) in enumerate([('FeCoMn–NC','#eb687b',3),('FeCo–NC','#b6b3d6',2.2),('Mn–NC','#f6b3a0',2.2)]):
 y=370.379931+i*9.512344
 E.SubElement(legend,'{'+S+'}path',d=f'M 430.44 {y} L 446.16 {y}',style=f'fill:none;stroke:{color};stroke-width:{lw}')
 t=E.SubElement(legend,'{'+S+'}text',x='449.88',y=str(y+2.8),style="font-size:8px;font-family:Arial;text-anchor:start");t.text=name
# a legend rebuilt as clean vector strokes and editable Arial labels.
legend=E.SubElement(el('axes_1'),'{'+S+'}g',id='a_legend_approved')
for i,(label,color,dash) in enumerate([('8O*','#f2a78d','1.75,1.75'),('8O* + Mn–O*','#7a2a3a','4.5,2.7'),('8O* + Mn–OH*','#eb687b',None)]):
 y=[123.12,132.72,142.32][i];style=f'fill:none;stroke:{color};stroke-width:1.4'
 if dash:style+=';stroke-dasharray:'+dash
 E.SubElement(legend,'{'+S+'}path',d=f'M 51.6 {y} L 72.6 {y}',style=style)
 t=E.SubElement(legend,'{'+S+'}text',x='73.2',y=str(y+2.8),style=f"font-size:8px;font-family:Arial;text-anchor:start;fill:{color}");t.text=label
# Match the approved column alignment, translating text groups only.
shifts={'text_121':16,'text_122':-22,'text_127':-20,'text_123':13,'text_124':-20,'text_128':10,'text_125':16,'text_126':-13}
for gid,dx in shifts.items():el(gid).set('transform',f'translate({dx/(4200/504)} 0)')
# y-axis labels are nested text; identify the final title group of the relevant y-axes.
for axis_id,dx in [('matplotlib.axis_4',-37),('matplotlib.axis_8',-37),('matplotlib.axis_12',-37),('matplotlib.axis_16',-3)]:
 axis=el(axis_id);groups=axis.xpath('./s:g[starts-with(@id,"text_")]',namespaces=NS)
 if groups:groups[-1].set('transform',f'translate({dx/(4200/504)} 0)')
# The approved atom legend includes H in addition to the six original source elements.
import base64
image=E.SubElement(root,'{'+S+'}image',x='168',y='484.0',width='6.6',height='6.6',id='approved_H_legend_atom')
image.set('{http://www.w3.org/1999/xlink}href','data:image/png;base64,'+base64.b64encode((OUT/'H_legend_atom.png').read_bytes()).decode())
t=E.SubElement(root,'{'+S+'}text',x='177',y='489.569457',style='font-family:Arial;font-size:8px;text-anchor:start');t.text='H'
# A raster structure inset remains an image by design; all curves, frames and labels are vector.
r.write(str(OUT/'Figure_5_078V_final_editable.svg'),encoding='utf-8',xml_declaration=True)
print('Native editable vector updated.')
