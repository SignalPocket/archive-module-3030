from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape

root = Path(__file__).resolve().parents[1]
models = root / "models"
output = root / "print-files"
output.mkdir(exist_ok=True)


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


def mesh_xml(object_id, filename, name, material_id):
    vertices, triangles = read_ascii_stl(models / filename)
    vertex_xml = "".join(
        f'<vertex x="{x}" y="{y}" z="{z}"/>' for x, y, z in vertices
    )
    triangle_xml = "".join(
        f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in triangles
    )
    return (
        f'<object id="{object_id}" name="{escape(name)}" type="model" '
        f'pid="{material_id}" pindex="0"><mesh><vertices>{vertex_xml}</vertices>'
        f'<triangles>{triangle_xml}</triangles></mesh></object>'
    )


def write_3mf(filename, title, parts):
    resources = []
    object_ids = []
    for index, (stl, name, color) in enumerate(parts, 1):
        material_id = 100 + index
        resources.append(
            f'<basematerials id="{material_id}"><base name="{escape(name)}" '
            f'displaycolor="#{color}FF"/></basematerials>'
        )
        resources.append(mesh_xml(index, stl, name, material_id))
        object_ids.append(index)

    if len(object_ids) == 1:
        build_id = object_ids[0]
    else:
        build_id = len(object_ids) + 1
        components = "".join(f'<component objectid="{item}"/>' for item in object_ids)
        resources.append(
            f'<object id="{build_id}" name="{escape(title)}" type="model">'
            f'<components>{components}</components></object>'
        )

    model = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<model unit="millimeter" xml:lang="en-US" '
        'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">'
        f'<metadata name="Title">{escape(title)}</metadata><resources>'
        f'{"".join(resources)}</resources><build><item objectid="{build_id}"/></build></model>'
    )

    destination = output / filename
    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
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
    print(destination)


jobs = [
    ("01_chassis_black.3mf", "01 Chassis — Black PLA", [("chassis_black.stl", "Chassis — Black PLA", "17191C")]),
    ("02_drawer_gray.3mf", "02 Drawer — Iron Gray PLA", [("drawer_gray.stl", "Drawer — Iron Gray PLA", "73777B")]),
    ("03_lid_black.3mf", "03 Lid — Black PLA", [("lid_black.stl", "Lid — Black PLA", "17191C")]),
    (
        "04_armor_gray_black_ams.3mf",
        "04 Armor — Iron Gray + Black AMS",
        [
            ("armor_gray.stl", "Armor — Iron Gray PLA", "73777B"),
            ("top_text_black.stl", "Top text — Black PLA", "111214"),
        ],
    ),
    ("05_timeline_yellow_petg.3mf", "05 Timeline — Yellow PETG", [("timeline_yellow.stl", "Timeline — Yellow PETG", "F2C300")]),
    ("06_reveal_red.3mf", "06 Reveal — Red PLA", [("reveal_red.stl", "Reveal — Red PLA", "A71930")]),
]

for job in jobs:
    write_3mf(*job)
