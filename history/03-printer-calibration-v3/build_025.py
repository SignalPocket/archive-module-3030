"""Generate one 0.25 mm-per-side U-channel test."""
from pathlib import Path

out=Path(__file__).parent/'rail_clearance_025.stl'

def box(x,y,z,dx,dy,dz):
    v=[(x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)]
    f=[(0,2,1),(0,3,2),(4,5,6),(4,6,7),(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),(3,0,4),(3,4,7)]
    return v,f

clearance=.25
inner=15+2*clearance
solids=[(0,0,0,52,2.5,9),(0,2.5+inner,0,52,2.5,9),(0,2.5,0,52,inner,2.5)]
vv=[]; ff=[]
for spec in solids:
    v,f=box(*spec); q=len(vv); vv.extend(v); ff.extend((a+q,b+q,c+q) for a,b,c in f)
lines=['solid rail_clearance_025.stl']
for a,b,c in ff:
    lines += [' facet normal 0 0 0','  outer loop',*(f'   vertex {vv[i][0]:.5f} {vv[i][1]:.5f} {vv[i][2]:.5f}' for i in (a,b,c)),'  endloop',' endfacet']
lines += ['endsolid rail_clearance_025.stl']
out.write_text('\n'.join(lines),encoding='ascii')
print(out)
