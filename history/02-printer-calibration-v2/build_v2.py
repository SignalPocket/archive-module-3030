"""Dependency-free STL generator for neutral calibration parts."""
from pathlib import Path
from math import cos, sin, pi

OUT=Path(__file__).parent

def box(x,y,z,dx,dy,dz):
    v=[(x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)]
    f=[(0,2,1),(0,3,2),(4,5,6),(4,6,7),(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),(3,0,4),(3,4,7)]
    return v,f

def ring(cx,cy,z0,ro,ri,h,n=64):
    v=[]
    for z in (z0,z0+h):
        for r in (ro,ri):
            v += [(cx+r*cos(2*pi*i/n),cy+r*sin(2*pi*i/n),z) for i in range(n)]
    f=[]
    for i in range(n):
        j=(i+1)%n
        f += [(i,j,2*n+j),(i,2*n+j,2*n+i),(n+i,3*n+j,n+j),(n+i,3*n+i,3*n+j)]
        f += [(2*n+i,2*n+j,3*n+j),(2*n+i,3*n+j,3*n+i),(i,n+j,j),(i,n+i,n+j)]
    return v,f

def write(name, solids):
    vv=[]; ff=[]
    for kind,args in solids:
        v,f=box(*args) if kind=='box' else ring(*args)
        q=len(vv); vv.extend(v); ff.extend((a+q,b+q,c+q) for a,b,c in f)
    lines=[f'solid {name}']
    for a,b,c in ff:
        lines += [' facet normal 0 0 0','  outer loop',*(f'   vertex {vv[i][0]:.5f} {vv[i][1]:.5f} {vv[i][2]:.5f}' for i in (a,b,c)),'  endloop',' endfacet']
    lines += [f'endsolid {name}']
    (OUT/name).write_text('\n'.join(lines),encoding='ascii')

write('slider_reference.stl',[('box',(0,0,0,42,15,3)),('box',(4,4.5,3,34,6,2))])

for code,c in [('030',.30),('035',.35),('040',.40)]:
    inner=15+2*c
    write(f'rail_clearance_{code}.stl', [
        ('box',(0,0,0,52,2.5,9)),
        ('box',(0,2.5+inner,0,52,2.5,9)),
        ('box',(0,2.5,0,52,inner,2.5))
    ])

write('magnet_sleeve_610.stl',[('ring',(6,6,0,5.05,3.05,3.2,64))])
write('m2_clearance_230.stl',[('ring',(4,4,0,3.15,1.15,4.0,64))])
write('m2_pilot_170.stl',[('ring',(4,4,0,2.85,.85,6.0,64))])
print('Generated seven V2 calibration STLs')
