from pathlib import Path
import re,shutil,copy
from lxml import etree as E
from matplotlib.textpath import TextToPath
from matplotlib.font_manager import FontProperties,findfont
from matplotlib.path import Path as MPath
from fontTools.pens.svgPathPen import SVGPathPen
import fitz
import numpy as np
src=Path(__file__).resolve().parent/'Figure_5_078V_final_editable.svg';out=src.parent
editable=src;outlined=out/'Figure_5_078V_final_Arial_paths.svg'
r=E.parse(str(src));ns={'s':'http://www.w3.org/2000/svg'};svg=ns['s'];tp=TextToPath();fonts=set()
def css(s):return dict((a.strip(),b.strip()) for a,b in re.findall(r'([^:;]+):([^;]+)',s or ''))
def draw(el, inherited=None):
 st=dict(inherited or {});st.update(css(el.get('style')))
 size=float(re.search(r'[\d.]+',st.get('font-size','8')).group());prop=FontProperties(family='Arial',weight='bold' if st.get('font-weight') in ['700','bold'] else 'normal',style=st.get('font-style','normal'))
 fonts.add(findfont(prop,fallback_to_default=False));txt=''.join(el.itertext())
 verts,codes=tp.get_text_path(prop,txt,ismath=False);pen=SVGPathPen(None)
 if len(verts):
  for xy,code in MPath(verts,codes).iter_segments(curves=True,simplify=False):
   pts=[tuple(xy[i:i+2]) for i in range(0,len(xy),2)]
   if code==MPath.MOVETO:pen.moveTo(pts[0])
   elif code==MPath.LINETO:pen.lineTo(pts[0])
   elif code==MPath.CURVE3:pen.qCurveTo(*pts)
   elif code==MPath.CURVE4:pen.curveTo(*pts)
   elif code==MPath.CLOSEPOLY:pen.closePath()
 w=tp.get_text_width_height_descent(txt,prop,False)[0]*size/prop.get_size_in_points()
 x=float(el.get('x','0'));y=float(el.get('y','0'));anchor=st.get('text-anchor','start')
 if anchor=='middle':x-=w/2
 elif anchor=='end':x-=w
 scale=size/100
 g=E.Element('{'+svg+'}g')
 if el.get('transform'):g.set('transform',el.get('transform'))
 style='; '.join(f'{k}: {v}' for k,v in st.items() if not k.startswith('font') and k!='text-anchor')
 E.SubElement(g,'{'+svg+'}path',d=pen.getCommands(),transform=f'translate({x:.8f} {y:.8f}) scale({scale:.8f} {-scale:.8f})',style=style or 'fill: #000000')
 return g
texts=r.xpath('//s:text',namespaces=ns)
for el in texts:
 if len(el):
  g=E.Element('{'+svg+'}g');
  for k,v in el.attrib.items():g.set(k,v)
  for span in el:g.append(draw(span,css(el.get('style'))))
 else:g=draw(el)
 g.tail=el.tail;el.getparent().replace(el,g)
assert not r.xpath('//s:text|//s:tspan',namespaces=ns)
r.write(str(outlined),encoding='utf-8',xml_declaration=True)
print('Converted text objects:',len(texts));print('Actual fonts:',fonts);print('SVG text/tspan remaining: 0');print('Files:',editable.name,outlined.name)

