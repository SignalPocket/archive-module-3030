import sys
from collections import defaultdict
from pathlib import Path

path = Path(sys.argv[1])
vertex_ids = {}
triangles = []
current = []

for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
    fields = line.strip().split()
    if len(fields) == 4 and fields[0] == "vertex":
        vertex = tuple(round(float(value), 5) for value in fields[1:])
        vertex_id = vertex_ids.setdefault(vertex, len(vertex_ids))
        current.append(vertex_id)
        if len(current) == 3:
            triangles.append(tuple(current))
            current = []

parents = list(range(len(triangles)))


def find(item):
    while parents[item] != item:
        parents[item] = parents[parents[item]]
        item = parents[item]
    return item


def union(left, right):
    left, right = find(left), find(right)
    if left != right:
        parents[right] = left


owners = defaultdict(list)
for triangle_id, triangle in enumerate(triangles):
    for vertex_id in triangle:
        owners[vertex_id].append(triangle_id)

for connected in owners.values():
    first = connected[0]
    for other in connected[1:]:
        union(first, other)

components = len({find(index) for index in range(len(triangles))})
print(f"{path.name}: triangles={len(triangles)} connected_components={components}")
groups = defaultdict(list)
id_to_vertex = {value: key for key, value in vertex_ids.items()}
for triangle_id, triangle in enumerate(triangles):
    groups[find(triangle_id)].extend(id_to_vertex[item] for item in triangle)
for number, vertices in enumerate(sorted(groups.values(), key=len, reverse=True), 1):
    low = tuple(min(vertex[axis] for vertex in vertices) for axis in range(3))
    high = tuple(max(vertex[axis] for vertex in vertices) for axis in range(3))
    print(f"  component {number}: bounds={low} to {high}")
if components != 1:
    raise SystemExit(1)
