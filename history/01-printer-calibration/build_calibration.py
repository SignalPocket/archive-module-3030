"""Generate innocuous fit-test STLs without third-party dependencies."""
from pathlib import Path
from math import cos,sin,pi

OUT=Path(__file__).parent

def box(x,y,z,dx,dy,dz):
    v=[(x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)]
    f=[(0,2,1),(0,3,2),(4,5,6),(4,6,7),(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),(3,0,4),(3,4,7)]
    return v,f

def ring(cx,cy,z0,ro,ri,h,n=48):
    v=[]
    for z in (z0,z0+h):
        for r in (ro,ri):
            v += [(cx+r*cos(2*pi*i/n),cy+r*sin(2*pi*i/n),z) for i in range(n)]
    f=[]
    for i in range(n):
        j=(i+1)%n
        f += [(i,j,2*n+j),(i,2*n+j,2*n+i)]
        f += [(n+i,3*n+j,n+j),(n+i,3*n+i,3*n+j)]
        f += [(2*n+i,2*n+j,3*n+j),(2*n+i,3*n+j,3*n+i)]
        f += [(i,n+j,j),(i,n+i,n+j)]
    return v,f

def write(name, solids):
    vv=[]; ff=[]
    for kind,args in solids:
        v,f=(box(*args) if kind=='box' else ring(*args)); q=len(vv); vv+=v; ff += [(a+q,b+q,c+q) for a,b,c in f]
    lines=[f'solid {name}']
    for a,b,c in ff:
        lines += [' facet normal 0 0 0','  outer loop',*(f'   vertex {vv[i][0]:.5f} {vv[i][1]:.5f} {vv[i][2]:.5f}' for i in (a,b,c)),'  endloop',' endfacet']
    lines += [f'endsolid {name}']
    (OUT/name).write_text('\n'.join(lines),encoding='ascii')

# Three short U-channel lanes. Nominal 12 mm sliders use 0.30/0.35/0.40 mm clearance per side.
rail=[]
for lane,c in enumerate((.30,.35,.40)):
    y=lane*22
    # The 15 mm slider runs between the inner wall faces, plus clearance on both sides.
    inner_w=15+2*c
    rail += [('box',(0,y,0,52,2.5,9)),('box',(0,y+2.5+inner_w,0,52,2.5,9)),('box',(0,y+2.5,0,52,inner_w,2.5))]
write('storage_case_rail_corrected.stl',rail)
write('storage_case_slider.stl',[('box',(0,0,0,42,15,3)),('box',(4,4.5,3,34,6,2))])

# PETG flex clip: same 3 mm body and 28 mm active flex length as the final latch.
write('cable_clip_flex_test.stl',[('box',(0,0,0,34,8,3)),('box',(27,-1,0,7,10,6)),('box',(24,1,3,5,6,2)),('box',(2,2,3,5,4,4))])

# Open-backed rings avoid unsupported blind-pocket ceilings. IDs: 6.10, 6.25, 6.40 mm.
coupon=[('box',(0,0,0,48,3,3.2)),('box',(0,15,0,48,3,3.2))]
for x,d in zip((9,24,39),(6.10,6.25,6.40)):
    coupon.append(('ring',(x,9,0,d/2+2,d/2,3.2,48)))
write('magnet_fit_coupon.stl',coupon)
print('Generated four neutral calibration STLs')
