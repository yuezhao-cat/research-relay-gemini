from pathlib import Path
from lxml import etree as E
import copy,re,subprocess,fitz
out=Path('outputs/T019');out.mkdir(exist_ok=True)
ns={'s':'http://www.w3.org/2000/svg'}
src=Path('outputs/图3_ef交换_20261114/Figure_3_e标号对齐_Arial_可编辑.svg')
r=E.parse(str(src)); par=r.xpath('//s:g[@id="figure_1"]',namespaces=ns)[0]
# Generate g at its new physical width using original source settings and data.
code=Path('outputs/图3_稳定性改版_20261113/figure3_equal.py').read_text(encoding='utf-8-sig')
code=code[:code.index('# A true inset')]
code=code.replace('462.047244,300.075591','301.889764,300.075591')
code=code.replace('ylim=(0,110)','ylim=(0,135)').replace('ax.set_yticks([0,50,100])','ax.set_yticks([0,50,100])')
code=code.replace('lw=7.0,alpha=.12','lw=11.0,alpha=.12').replace('lw=4.5,alpha=.18','lw=7.0,alpha=.18')
code=code.replace("ax.text(.02,.05,'238 h, 0.516 V vs. RHE, 1600 rpm',transform=ax.transAxes,ha='left',va='bottom')", "ax.text(.98,.05,'238 h, 0.516 V vs. RHE, 1600 rpm',transform=ax.transAxes,ha='right',va='bottom')")
code+="\nax.text(.02,.93,'FeCoMn–NC',transform=ax.transAxes,ha='left',va='top',fontsize=8,color='black')\nfig.savefig('work/t019_g.svg');plt.close(fig)\n"
exec(compile(code,'g','exec'))
for z in list(par):
 if 'axes' in z.get('id','') and ('238 h' in ''.join(z.itertext()) or 'Magnified view' in ''.join(z.itertext())):par.remove(z)
g=E.parse('work/t019_g.svg')
def prefix(t,p):
 ids={e.get('id'):p+e.get('id') for e in t.iter() if e.get('id')}
 for e in t.iter():
  for k,v in list(e.attrib.items()):
   if k=='id':e.set(k,ids[v]);continue
   for a,b in ids.items():v=v.replace('url(#'+a+')','url(#'+b+')');v=b if False else v;v=('#'+b) if v=='#'+a else v
   e.set(k,v)
prefix(g,'t019_')
par.append(copy.deepcopy(g.xpath('//s:g[@id="t019_axes_1"]',namespaces=ns)[0]))
for d in g.getroot().findall('s:defs',ns):r.getroot().append(copy.deepcopy(d))
s=E.parse('outputs/图S10_仅31.6h_20261114/Figure_S10_仅31.6h_Arial_可编辑.svg')
h=s.xpath('//s:g[@id="oldh_axes_7"]',namespaces=ns)[0];h=copy.deepcopy(h);h.attrib.pop('transform',None);h.set('transform','translate(0 -2.834645)');par.append(h)
for tx in h.xpath('.//s:text',namespaces=ns):
 if ''.join(tx.itertext()).strip()=='After 31.6 h':tx.text='After'
for group in list(h.xpath('.//s:g',namespaces=ns)):
 if group.get('id','').endswith('text_104'):
  group.getparent().remove(group)
for d in s.getroot().findall('s:defs',ns):r.getroot().append(copy.deepcopy(d))
el=E.SubElement(par,'{'+ns['s']+'}text',x='325',y='296',style='font-family:Arial;font-size:10px;font-weight:bold');el.text='h'
r.write(str(out/'Figure3_editable.svg'),encoding='utf-8',xml_declaration=True)
# Align the right-column panel letters and vertical axis labels.
for te in r.xpath('//s:text',namespaces=ns):
 if ''.join(te.itertext()).strip() in ['a','d','g','c','f','h','b','e'] and len(te)==0:
  label=''.join(te.itertext()).strip()
  te.set('x','12.799852' if label in ['a','d','g'] else ('166.509833' if label in ['b','e'] else '326.667313'))
  te.set('style',re.sub(r'text-anchor:\s*\w+','text-anchor: middle',te.get('style',''))+'; text-anchor: middle')
  if label in ['g','h']:
   te.set('y','296')
   te.set('transform',f'rotate(-0 {te.get("x")} 296)')
  yy=te.get('y')
  if te.get('transform') and yy:te.set('transform',f'rotate(-0 {te.get("x")} {yy})')
for el in r.getroot().iter():
 tr=el.get('transform','') or ''
 if 'rotate(-90)' in tr:
  m=re.search(r'translate\(([-\d.]+)[ ,]+([-\d.]+)\)',tr)
  if m and float(m[1])>300:
   el.set('transform',tr[:m.start()]+f'translate(326.667313 {m[2]})'+tr[m.end():])
  elif m and 150<float(m[1])<200:
   el.set('transform',tr[:m.start()]+f'translate(166.509833 {m[2]})'+tr[m.end():])
  elif m and float(m[1])<30:
   el.set('transform',tr[:m.start()]+f'translate(12.799852 {m[2]})'+tr[m.end():])
for te in r.xpath('//s:text',namespaces=ns):
 if ''.join(te.itertext()).strip()=='Relative current (%)' and te.get('x'):
  old=float(te.get('x'));te.set('x','12.799852')
  tr=te.get('transform','') or '';te.set('transform',re.sub(r'rotate\(-90 [\d.-]+ ', 'rotate(-90 12.799852 ',tr))
r.write(str(out/'Figure3_editable.svg'),encoding='utf-8',xml_declaration=True)
# Single panel S10, preserving original a objects and definitions.
for z in list(s.xpath('//s:g[@id="figure_1"]',namespaces=ns)[0]):
 if z.get('id','').startswith('oldh_') or ''.join(z.itertext()).strip()=='a':z.getparent().remove(z)
s.getroot().set('viewBox','0 0 320 145');s.getroot().set('width','320pt')
s.write(str(out/'FigureS10_editable.svg'),encoding='utf-8',xml_declaration=True)
chrome=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
for f in out.glob('*editable.svg'):
 t=E.parse(str(f));w,h=map(float,t.getroot().get('viewBox').split()[2:]);html=out/(f.stem+'.html')
 html.write_text(f'<html><head><style>@page{{size:{w}pt {h}pt;margin:0}}body{{margin:0}}svg{{display:block}}</style></head><body>'+E.tostring(t.getroot(),encoding='unicode')+'</body></html>',encoding='utf-8')
 pdf=f.with_suffix('.pdf').resolve()
 subprocess.run([chrome,'--headless=new','--disable-gpu','--user-data-dir='+str((out/'chrome').resolve()),'--no-pdf-header-footer','--print-to-pdf='+str(pdf),html.resolve().as_uri()],capture_output=True,timeout=45)
 d=fitz.open(pdf);d[0].get_pixmap(matrix=fitz.Matrix(3,3)).save(f.with_suffix('.png'))
