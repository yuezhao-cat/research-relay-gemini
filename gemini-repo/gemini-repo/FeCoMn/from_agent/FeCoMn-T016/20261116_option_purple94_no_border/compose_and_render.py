from pathlib import Path
import re
OUT=Path(__file__).resolve().parent
OLD_H=176.97777777792498
GAP=0.
HC=36.
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

for suffix in ['editable','Arial_paths']:
 append_svg(OUT.parent/'20261116_final_gray_dashed/source'/('ab_approved_'+suffix+'.svg'), OUT/('Figure_4c_20261116_option_purple94_no_border_'+suffix+'.svg'), OUT/('Figure_4_20261116_option_purple94_no_border_'+suffix+'.svg'))

import resvg_py,io
from PIL import Image
b=resvg_py.svg_to_bytes(svg_path=str(OUT/'Figure_4_20261116_option_purple94_no_border_Arial_paths.svg'),width=4200,dpi=96,background='white')
Image.open(io.BytesIO(b)).save(OUT/'Figure_4_20261116_option_purple94_no_border_600dpi.png',dpi=(600,600))
