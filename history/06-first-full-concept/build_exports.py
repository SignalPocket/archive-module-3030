"""Dependency-free reference STL/3MF generator for ARCHIVE MODULE 3030."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

OUT=Path(__file__).parent

def box(x,y,z,dx,dy,dz):
    v=[(x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)]
    f=[(0,2,1),(0,3,2),(4,5,6),(4,6,7),(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),(3,0,4),(3,4,7)]
    return v,f

def mesh(boxes):
    vv=[]; ff=[]
    for b in boxes:
        v,f=box(*b); n=len(vv); vv+=v; ff += [(a+n,b+n,c+n) for a,b,c in f]
    return vv,ff

def stl(name, boxes):
    v,f=mesh(boxes)
    lines=[f"solid {name}"]
    for a,b,c in f:
        lines += [" facet normal 0 0 0","  outer loop",*(f"   vertex {v[i][0]} {v[i][1]} {v[i][2]}" for i in (a,b,c)),"  endloop"," endfacet"]
    lines += [f"endsolid {name}"]
    (OUT/name).write_text("\n".join(lines),encoding="ascii")
    return v,f

parts={
 "shell_black.stl":[(0,0,0,150,3,34),(0,89,0,150,3,34),(0,3,0,3,86,34),(0,3,31,150,86,3),(0,3,0,150,86,3)],
 "drawer_iron_gray.stl":[(0,0,0,126,85.7,3),(0,0,0,126,3,23),(0,82.7,0,126,3,23),(0,0,0,3,85.7,23)],
 "armor_iron_gray.stl":[(0,0,0,116,58,2.4),(4,4,2.4,108,3,1.2),(4,51,2.4,108,3,1.2)],
 "security_bar_yellow.stl":[(0,0,0,34,8,3),(27,-1,0,7,10,6),(24,1,3,5,6,2)],
 "reveal_plate_red.stl":[(0,0,0,100,52,2),(4,5,2,92,4,.8),(4,14,2,92,4,.8),(20,23,2,60,5,.8)],
 "tolerance_test.stl":[(0,0,0,70,24,3),(4,5,3,12,14,3),(20,5,3,11.9,14,3),(36,5,3,11.8,14,3),(52,5,3,11.7,14,3)]
}
meshes={n:stl(n,b) for n,b in parts.items()}

colors={"shell_black.stl":"17191C","drawer_iron_gray.stl":"73777B","armor_iron_gray.stl":"73777B","security_bar_yellow.stl":"E5BF19","reveal_plate_red.stl":"A71930"}
offsets={"shell_black.stl":(0,0,0),"drawer_iron_gray.stl":(20,3.15,3.15),"armor_iron_gray.stl":(17,17,35),"security_bar_yellow.stl":(113,83,14),"reveal_plate_red.stl":(24,20,6.15)}
verts=[]; tris=[]; items=[]
for idx,(n,(v,f)) in enumerate((x for x in meshes.items() if x[0] in colors),1):
    ox,oy,oz=offsets[n]; base=len(verts); verts += [(x+ox,y+oy,z+oz) for x,y,z in v]; tris += [(a+base,b+base,c+base,idx) for a,b,c in f]; items.append((idx,n,colors[n]))
resources=''.join(f'<basematerials id="{100+i}"><base name="{n}" displaycolor="#{c}FF"/></basematerials>' for i,n,c in items)
vx=''.join(f'<vertex x="{x}" y="{y}" z="{z}"/>' for x,y,z in verts)
tx=''.join(f'<triangle v1="{a}" v2="{b}" v3="{c}" pid="{100+p}" p1="0"/>' for a,b,c,p in tris)
model=f'''<?xml version="1.0" encoding="UTF-8"?><model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"><metadata name="Title">ARCHIVE MODULE 3030</metadata><resources>{resources}<object id="1" type="model"><mesh><vertices>{vx}</vertices><triangles>{tx}</triangles></mesh></object></resources><build><item objectid="1"/></build></model>'''
with ZipFile(OUT/'archive_module_3030.3mf','w',ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml','<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>')
    z.writestr('_rels/.rels','<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Target="/3D/3dmodel.model" Id="rel0" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>')
    z.writestr('3D/3dmodel.model',model)
print('Generated',len(parts),'STLs and archive_module_3030.3mf')
