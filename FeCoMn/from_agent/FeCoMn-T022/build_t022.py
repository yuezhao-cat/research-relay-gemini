from pathlib import Path
import hashlib
import subprocess
import sys

import fitz
from PIL import Image
from lxml import etree as ET

here = Path(__file__).resolve().parent
source = here.parent / 'FeCoMn-T021/Figure_5_T021_20261117_1750_editable.svg'
outline_source = here.parent / 'FeCoMn-T018/20261117_Figure5_078V_final/outline_text.py'
stem = 'Figure_5_T022_20261117_1740'
editable = here / f'{stem}_editable.svg'
outlined = here / f'{stem}_Arial_paths.svg'
png = here / f'{stem}_600dpi.png'
S = 'http://www.w3.org/2000/svg'
ns = {'s': S}

tree = ET.parse(str(source))
removed = []
for group in list(tree.xpath('//s:g', namespaces=ns)):
    if group.get('id') in {'patch_44', 'patch_45', 'patch_46', 't021_eta_1', 't021_eta_2', 't021_eta_3'}:
        removed.append(group.get('id'))
        group.getparent().remove(group)
assert len(removed) == 6

legend = tree.xpath('//s:g[@id="h_legend_approved"]', namespaces=ns)[0]
for el in legend:
    if el.tag == f'{{{S}}}path':
        el.set('d', el.get('d').replace('430.44 ', '370.44 ').replace('446.16 ', '386.16 '))
    elif el.tag == f'{{{S}}}text':
        el.set('x', '389.88')
        el.text = (el.text or '') + ','

rows = [
    ('0.45 V', '#eb687b', 373.179931, 449),
    ('0.89 V', '#8f8bc0', 382.692275, 438),
    ('0.97 V', '#f6b3a0', 392.204619, 429),
]
for i, (value, color, y, x) in enumerate(rows, 1):
    g = ET.SubElement(legend, f'{{{S}}}g', id=f't022_eta_{i}')
    eta = ET.SubElement(g, f'{{{S}}}text', x=str(x), y=f'{y:.6f}', style=f'font-size:8px;font-family:Arial;font-style:italic;fill:{color}')
    eta.text = 'η'
    val = ET.SubElement(g, f'{{{S}}}text', x=f'{x + 5.6}', y=f'{y:.6f}', style=f'font-size:8px;font-family:Arial;fill:{color}')
    val.text = f' = {value}'

tree.write(str(editable), encoding='utf-8', xml_declaration=True)
outline_code = outline_source.read_text(encoding='utf-8-sig').replace(
    "src=Path(__file__).resolve().parent/'Figure_5_078V_final_editable.svg';out=src.parent",
    f'src=Path({str(editable)!r});out=src.parent',
).replace("outlined=out/'Figure_5_078V_final_Arial_paths.svg'", f'outlined=Path({str(outlined)!r})')
subprocess.run([sys.executable, '-c', outline_code], check=True)
assert not ET.parse(str(outlined)).xpath('//*[local-name()="text" or local-name()="tspan"]')

root = tree.getroot()
w, h = map(float, root.get('viewBox').split()[2:])
html = here / 'render.html'
html.write_text(f'<html><head><style>@page{{size:{w}pt {h}pt;margin:0}}body{{margin:0}}svg{{display:block}}</style></head><body>' + ET.tostring(root, encoding='unicode') + '</body></html>', encoding='utf-8')
pdf = here / 'render.pdf'
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
subprocess.run([chrome, '--headless=new', '--disable-gpu', '--user-data-dir=' + str((here.parents[3] / 'work/t022_chrome').resolve()), '--no-pdf-header-footer', '--print-to-pdf=' + str(pdf), html.resolve().as_uri()], capture_output=True, check=True, timeout=45)
doc = fitz.open(pdf)
doc[0].get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), alpha=False).save(png)
doc.close()
im = Image.open(png)
im.save(png, dpi=(600, 600))
html.unlink()
pdf.unlink()
print('source SHA256:', hashlib.sha256(source.read_bytes()).hexdigest())
print('removed:', removed)
print('outputs:', editable.name, outlined.name, png.name)
