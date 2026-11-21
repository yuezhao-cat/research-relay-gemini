from pathlib import Path
import copy
import hashlib
import subprocess
import sys

import fitz
from PIL import Image
from lxml import etree as ET

here = Path(__file__).resolve().parent
prior = here.parent / 'FeCoMn-T018/20261117_Figure5_078V_final'
source = prior / 'Figure_5_078V_final_editable.svg'
stamp = '20261117_1750'
editable = here / f'Figure_5_T021_{stamp}_editable.svg'
outlined = here / f'Figure_5_T021_{stamp}_Arial_paths.svg'
png = here / f'Figure_5_T021_{stamp}_600dpi.png'
svg_ns = 'http://www.w3.org/2000/svg'
ns = {'s': svg_ns}

tree = ET.parse(str(source))
root = tree.getroot()
figure = tree.xpath('//s:g[@id="figure_1"]', namespaces=ns)[0]
deleted = []
for group in list(tree.xpath('//s:g', namespaces=ns)):
    if group.get('id') in {'text_105', 'text_106', 'text_107'}:
        deleted.append(''.join(group.itertext()).strip())
        group.getparent().remove(group)
assert sorted(deleted) == sorted(['0.004 eV', '0.44 eV', '0.52 eV'])

rows = [
    ('FeCoMn–NC', '0.45 V', '#eb687b', 373.179931),
    ('FeCo–NC', '0.89 V', '#8f8bc0', 382.692275),
    ('Mn–NC', '0.97 V', '#f1a08c', 392.204619),
]
for index, (sample, value, color, y) in enumerate(rows, 1):
    group = ET.SubElement(figure, f'{{{svg_ns}}}g', id=f't021_eta_{index}')
    eta = ET.SubElement(group, f'{{{svg_ns}}}text', x='367', y=f'{y:.6f}', style=f'font-size:8px;font-family:Arial;font-style:italic;fill:{color}')
    eta.text = 'η'
    number = ET.SubElement(group, f'{{{svg_ns}}}text', x='372.6', y=f'{y:.6f}', style=f'font-size:8px;font-family:Arial;fill:{color}')
    number.text = f' = {value}'

tree.write(str(editable), encoding='utf-8', xml_declaration=True)

outline_template = (prior / 'outline_text.py').read_text(encoding='utf-8-sig')
outline_template = outline_template.replace(
    "src=Path(__file__).resolve().parent/'Figure_5_078V_final_editable.svg';out=src.parent",
    f'src=Path({str(editable)!r});out=src.parent',
).replace("outlined=out/'Figure_5_078V_final_Arial_paths.svg'", f'outlined=Path({str(outlined)!r})')
subprocess.run([sys.executable, '-c', outline_template], check=True)
assert not ET.parse(str(outlined)).xpath('//*[local-name()="text" or local-name()="tspan"]')

w, h = map(float, root.get('viewBox').split()[2:])
html = here / 't021_render.html'
html.write_text(
    f'<html><head><style>@page{{size:{w}pt {h}pt;margin:0}}body{{margin:0}}svg{{display:block}}</style></head><body>'
    + ET.tostring(root, encoding='unicode') + '</body></html>', encoding='utf-8'
)
pdf = here / 't021_render.pdf'
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
subprocess.run([chrome, '--headless=new', '--disable-gpu', '--user-data-dir=' + str((here.parents[3] / 'work/t021_chrome').resolve()), '--no-pdf-header-footer', '--print-to-pdf=' + str(pdf), html.resolve().as_uri()], capture_output=True, check=True, timeout=45)
doc = fitz.open(pdf)
doc[0].get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), alpha=False).save(png)
doc.close()
im = Image.open(png)
im.save(png, dpi=(600, 600))
html.unlink()
pdf.unlink()
print('source_sha256', hashlib.sha256(source.read_bytes()).hexdigest())
print('outputs', editable.name, outlined.name, png.name)
