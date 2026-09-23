"""Dependency-free latch/catch prototype STL generator."""
from pathlib import Path

OUT=Path(__file__).parent

def box(x,y,z,dx,dy,dz):
    v=[(x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)]
    f=[(0,2,1),(0,3,2),(4,5,6),(4,6,7),(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),(3,0,4),(3,4,7)]
    return v,f

def write(name, solids):
    vv=[]; ff=[]
    for spec in solids:
        v,f=box(*spec); q=len(vv); vv.extend(v); ff.extend((a+q,b+q,c+q) for a,b,c in f)
    lines=[f'solid {name}']
    for a,b,c in ff:
        lines += [' facet normal 0 0 0','  outer loop',*(f'   vertex {vv[i][0]:.4f} {vv[i][1]:.4f} {vv[i][2]:.4f}' for i in (a,b,c)),'  endloop',' endfacet']
    lines += [f'endsolid {name}']
    (OUT/name).write_text('\n'.join(lines),encoding='ascii')

# Black guide: 0.15 mm clearance per side around a 28 mm-wide slider.
# The right wall is split to create a latch window at x=42..50.
write('latch_test_jig_black.stl',[
    (0,0,0,70,34.3,3),
    (0,0,3,70,3,8),
    (0,31.3,3,42,3,8),
    (50,31.3,3,20,3,8),
    (0,34.3,0,12,5,11),
    (0,39.3,0,12,3,11)
])

# Gray slider: side rail has a 7 mm catch gap aligned with the jig window.
write('catch_slider_gray.stl',[
    (0,0,0,58,28,3),
    (0,0,3,58,3,4),
    (0,25,3,42,3,4),
    (49,25,3,9,3,4),
    (0,3,3,3,22,4)
])

# Proven 1.80 mm cantilever; the 4 mm hook projects inward when installed vertically.
write('security_flexure_180_yellow.stl',[
    (0,0,0,10,8,4),
    (10,0,0,38,8,1.8),
    (43,0,0,5,8,4.0),
    (24,0,1.8,10,8,1.2)
])

print('Generated latch jig, catch slider, and 1.80 mm security flexure')
