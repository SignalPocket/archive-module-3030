from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape

root = Path(__file__).resolve().parent
models = root / "models"
output = root / "print-files"


def read_stl(path):
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


def write_job(filename, title, parts):
    resources = []
    ids = []
    for object_id, (stl, name, color) in enumerate(parts, 1):
        vertices, triangles = read_stl(models / stl)
        material_id = 100 + object_id
        resources.append(f'<basematerials id="{material_id}"><base name="{escape(name)}" displaycolor="#{color}FF"/></basematerials>')
        vx = "".join(f'<vertex x="{x}" y="{y}" z="{z}"/>' for x, y, z in vertices)
        tx = "".join(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in triangles)
        resources.append(f'<object id="{object_id}" name="{escape(name)}" type="model" pid="{material_id}" pindex="0"><mesh><vertices>{vx}</vertices><triangles>{tx}</triangles></mesh></object>')
        ids.append(object_id)
    build_id = ids[0]
    if len(ids) > 1:
        build_id = len(ids) + 1
        components = "".join(f'<component objectid="{item}"/>' for item in ids)
        resources.append(f'<object id="{build_id}" name="{escape(title)}" type="model"><components>{components}</components></object>')
    model = '<?xml version="1.0" encoding="UTF-8"?>' + '<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">' + f'<metadata name="Title">{escape(title)}</metadata><resources>{"".join(resources)}</resources><build><item objectid="{build_id}"/></build></model>'
    with ZipFile(output / filename, "w", ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>')
        archive.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Target="/3D/3dmodel.model" Id="rel0" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>')
        archive.writestr("3D/3dmodel.model", model)
    print(output / filename)


write_job("01_base_black.3mf", "JOHN 3030 — Black Base", [("base_black.stl", "Base — Black PLA", "17191C")])
write_job("02_face_gray_black_red_ams.3mf", "JOHN 3030 — AMS Face", [
    ("face_gray.stl", "Face — Iron Gray PLA", "73777B"),
    ("text_black.stl", "Lettering — Black PLA", "111214"),
    ("indicator_red.stl", "Indicator — Red PLA", "A71930"),
])
write_job("03_signal_yellow_petg.3mf", "JOHN 3030 — Yellow Signal", [("signal_yellow_petg.stl", "Signal — Yellow PETG", "F2C300")])
