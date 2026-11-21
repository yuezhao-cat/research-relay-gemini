from pathlib import Path
import hashlib
import shutil
import subprocess
import sys
import fitz
from lxml import etree

root = Path(__file__).resolve().parents[1]
source = root / 'outputs/图3_稳定性改版_20261113'
dest = root / 'research-relay/FeCoMn/from_agent/FeCoMn-T019'
dest.mkdir(parents=True, exist_ok=True)
stamp = '20261117_1650'
template = (source / 'outline_figure3_equal.py').read_text(encoding='utf-8-sig')
for stem, label in [('Figure3', 'Figure_3'), ('FigureS10', 'Figure_S10')]:
    editable = dest / f'{label}_{stamp}_editable.svg'
    outlined = dest / f'{label}_{stamp}_Arial_outlined.svg'
    png = dest / f'{label}_{stamp}_600dpi.png'
    shutil.copyfile(source / f'{stem}_editable.svg', editable)
    if stem == 'Figure3':
        t = etree.parse(str(editable))
        e = t.getroot()
        _, _, w, h = map(float, e.get('viewBox').split())
        target_w = 177.8 / 25.4 * 72
        e.set('width', f'{target_w:.6f}pt')
        e.set('height', f'{target_w * h / w:.6f}pt')
        t.write(str(editable), encoding='utf-8', xml_declaration=True)
    outline_code = template.replace(
        "src=Path('outputs/图3_稳定性改版_20261113/Figure_3_g等高等间距_Arial_可编辑.svg');out=src.parent",
        f'src=Path({str(editable)!r});out=src.parent',
    ).replace(
        "outlined=out/'Figure_3_g等高等间距_Arial_文字转路径.svg'",
        f'outlined=Path({str(outlined)!r})',
    )
    subprocess.run([sys.executable, '-c', outline_code], cwd=root, check=True)
    t = etree.parse(str(editable))
    e = t.getroot()
    width_pt = float(e.get('width').removesuffix('pt'))
    height_pt = float(e.get('height').removesuffix('pt'))
    html = dest / f'{label}_{stamp}_render.html'
    html.write_text(f'<html><head><style>@page{{size:{width_pt}pt {height_pt}pt;margin:0}}body{{margin:0}}svg{{display:block}}</style></head><body>' + etree.tostring(e, encoding='unicode') + '</body></html>', encoding='utf-8')
    pdf = dest / f'{label}_{stamp}_render.pdf'
    chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    subprocess.run([chrome, '--headless=new', '--disable-gpu', '--user-data-dir=' + str((root / 'work/t019_chrome').resolve()), '--no-pdf-header-footer', '--print-to-pdf=' + str(pdf), html.resolve().as_uri()], capture_output=True, check=True, timeout=45)
    doc = fitz.open(pdf)
    doc[0].get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), alpha=False).save(png)
    doc.close()
    html.unlink()
    pdf.unlink()
    tree = etree.parse(str(outlined))
    assert not tree.xpath('//*[local-name()="text" or local-name()="tspan"]')
    print(label, png.stat().st_size, png)

h_source = root / 'outputs/图S10_仅31.6h_20261114/Figure_S10_仅31.6h_Arial_可编辑.svg'
sha = hashlib.sha256(h_source.read_bytes()).hexdigest()
(dest / 'h_source_sha256.txt').write_text(f'{sha}  {h_source}\n', encoding='utf-8')
shutil.copyfile(root / 'work/t019.py', dest / f'Figure_3_{stamp}_source.py')
