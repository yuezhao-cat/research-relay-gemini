import csv, io, numpy as np
def load(path):
    """Read journal single-figure csv: comment lines start with '#', header cols 'panel | series | label'.
    Returns (notes, dict series -> dict label -> np.array)."""
    notes=[]; rows=[]
    with open(path, encoding='utf-8-sig') as f:
        for line in f:
            s=line.strip()
            if s.startswith('#') or s.startswith('"#'): notes.append(s.strip('"')); continue
            rows.append(line)
    r=list(csv.reader(io.StringIO(''.join(rows))))
    hdr=r[0]; data=r[1:]
    out={}
    for j,h in enumerate(hdr):
        parts=[p.strip() for p in h.split(' | ',2)]
        if len(parts)==3: _,ser,lab=parts
        elif len(parts)==2: ser,lab=parts
        else: ser,lab='',parts[0]
        col=[]
        for row in data:
            v=row[j] if j<len(row) else ''
            try: col.append(float(v))
            except: col.append(np.nan)
        a=np.array(col); 
        out.setdefault(ser,{})[lab]=a
    return notes,out
