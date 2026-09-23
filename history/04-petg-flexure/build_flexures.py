"""Generate three PETG cantilever flexure coupons."""
from pathlib import Path

OUT=Path(__file__).parent

def box(x,y,z,dx,dy,dz):
    v=[(x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)]
    f=[(0,2,1),(0,3,2),(4,5,6),(4,6,7),(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),(3,0,4),(3,4,7)]
    return v,f

def write(name,t):
    # 10 mm anchor, 38 mm active spring, and a low press pad at the free end.
    solids=[(0,0,0,10,10,4),(10,1,0,38,8,t),(43,0,0,7,10,t+1.2)]
    vv=[]; ff=[]
    for spec in solids:
        v,f=box(*spec); q=len(vv); vv.extend(v); ff.extend((a+q,b+q,c+q) for a,b,c in f)
    lines=[f'solid {name}']
    for a,b,c in ff:
        lines += [' facet normal 0 0 0','  outer loop',*(f'   vertex {vv[i][0]:.4f} {vv[i][1]:.4f} {vv[i][2]:.4f}' for i in (a,b,c)),'  endloop',' endfacet']
    lines += [f'endsolid {name}']
    (OUT/name).write_text('\n'.join(lines),encoding='ascii')

for code,t in [('120',1.20),('150',1.50),('180',1.80)]:
    write(f'flexure_{code}.stl',t)
print('Generated three PETG flexure coupons')
