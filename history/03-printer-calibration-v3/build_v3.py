"""Generate three fine-clearance U-channel STL tests."""
from pathlib import Path

OUT=Path(__file__).parent

def box(x,y,z,dx,dy,dz):
    v=[(x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)]
    f=[(0,2,1),(0,3,2),(4,5,6),(4,6,7),(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),(3,0,4),(3,4,7)]
    return v,f

def write(name, boxes):
    vv=[]; ff=[]
    for spec in boxes:
        v,f=box(*spec); q=len(vv); vv.extend(v); ff.extend((a+q,b+q,c+q) for a,b,c in f)
    lines=[f'solid {name}']
    for a,b,c in ff:
        lines += [' facet normal 0 0 0','  outer loop',*(f'   vertex {vv[i][0]:.5f} {vv[i][1]:.5f} {vv[i][2]:.5f}' for i in (a,b,c)),'  endloop',' endfacet']
    lines += [f'endsolid {name}']
    (OUT/name).write_text('\n'.join(lines),encoding='ascii')

for code,c in [('010',.10),('015',.15),('020',.20)]:
    inner=15+2*c
    write(f'rail_clearance_{code}.stl',[
        (0,0,0,52,2.5,9),
        (0,2.5+inner,0,52,2.5,9),
        (0,2.5,0,52,inner,2.5)
    ])

print('Generated three fine-clearance rail tests')
