from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape

root = Path(__file__).resolve().parents[1] / "models"

# Offsets show the fully assembled object. The armor and top-text meshes share
# one coordinate system so Bambu Studio can treat them as aligned color parts.
parts = [
    ("chassis_black.stl", "Chassis — Black PLA", "17191C", (0, 0, 0)),
    ("lid_black.stl", "Lid — Black PLA", "17191C", (0, 0, 31)),
    ("armor_gray.stl", "Armor — Iron Gray PLA", "73777B", (0, 0, 33)),
    ("top_text_black.stl", "Top text — Black PLA", "111214", (0, 0, 33)),
    ("timeline_yellow.stl", "Timeline — Yellow PETG", "F2C300", (0, 0, 35.4)),
    ("drawer_gray.stl", "Drawer — Iron Gray PLA", "73777B", (24, 3.15, 3.15)),
    ("reveal_red.stl", "Reveal — Red PLA", "A71930", (32, 10, 6.2)),
]


def read_ascii_stl(path):
    vertices, index, triangles, current = [], {}, [], []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        fields = line.strip().split()
        if len(fields) == 4 and fields[0] == "vertex":
            vertex = tuple(round(float(value), 6) for value in fields[1:])
            if vertex not in index:
                index[vertex] = len(vertices)
                vertices.append(vertex)
            current.append(index[vertex])
            if len(current) == 3:
                triangles.append(tuple(current))
                current = []
    return vertices, triangles


resources, build = [], []
for object_id, (filename, name, color, offset) in enumerate(parts, 1):
    vertices, triangles = read_ascii_stl(root / filename)
    material_id = 100 + object_id
    resources.append(
        f'<basematerials id="{material_id}"><base name="{escape(name)}" '
        f'displaycolor="#{color}FF"/></basematerials>'
    )
    vertex_xml = "".join(
        f'<vertex x="{x}" y="{y}" z="{z}"/>' for x, y, z in vertices
    )
    triangle_xml = "".join(
        f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in triangles
    )
    resources.append(
        f'<object id="{object_id}" name="{escape(name)}" type="model" '
        f'pid="{material_id}" pindex="0"><mesh><vertices>{vertex_xml}</vertices>'
        f'<triangles>{triangle_xml}</triangles></mesh></object>'
    )
    x, y, z = offset
    build.append(
        f'<item objectid="{object_id}" transform="1 0 0 0 1 0 0 0 1 {x} {y} {z}"/>'
    )

model = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<model unit="millimeter" xml:lang="en-US" '
    'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">'
    '<metadata name="Title">ARCHIVE MODULE 3030 — Production Candidate V2</metadata>'
    f'<resources>{"".join(resources)}</resources><build>{"".join(build)}</build></model>'
)

output = root / "archive_module_3030_final.3mf"
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    archive.writestr(
        "[Content_Types].xml",
        '<?xml version="1.0" encoding="UTF-8"?><Types '
        'xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>'
        '</Types>',
    )
    archive.writestr(
        "_rels/.rels",
        '<?xml version="1.0" encoding="UTF-8"?><Relationships '
        'xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Target="/3D/3dmodel.model" Id="rel0" '
        'Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>'
        '</Relationships>',
    )
    archive.writestr("3D/3dmodel.model", model)

print(output)
