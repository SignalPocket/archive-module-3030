from pathlib import Path
import re

workspace = Path(r"C:\Users\katie\Documents\Codex\2026-09-10\referenced-chatgpt-conversation-this-is-an")
visuals = Path(r"C:\Users\katie\.codex\visualizations\2026\09\10\01a08b90-6d0b-7942-895a-8eb742630d7a")
destination = workspace / "outputs" / "Latch_Catch_Test_V3"

jobs = {
    "latch-assembly-sketch.html": "assembly-isometric.svg",
    "latch-assembly-top-view.html": "assembly-top-view.svg",
}

replacements = {
    "var(--foreground)": "#111827",
    "var(--background)": "#ffffff",
    "var(--border)": "#374151",
    "var(--muted)": "#a3a3a3",
    "var(--muted-foreground)": "#4b5563",
    "var(--viz-series-3)": "#facc15",
}

for source_name, output_name in jobs.items():
    fragment = (visuals / source_name).read_text(encoding="utf-8")
    match = re.search(r"(<svg[\s\S]*?</svg>)", fragment)
    if not match:
        raise RuntimeError(f"No SVG found in {source_name}")
    svg = match.group(1)
    svg = re.sub(r"color-mix\(in srgb, var\(--foreground\) \d+%, var\(--background\)\)", "#1f2937", svg)
    svg = re.sub(r"color-mix\(in srgb, var\(--muted\) \d+%, var\(--foreground\)\)", "#73777b", svg)
    svg = re.sub(r"color-mix\(in srgb, var\(--viz-series-3\) \d+%, var\(--foreground\)\)", "#a16207", svg)
    svg = re.sub(r"color-mix\(in srgb, var\(--viz-series-3\) \d+%, var\(--background\)\)", "#fde047", svg)
    for old, new in replacements.items():
        svg = svg.replace(old, new)
    svg = '<?xml version="1.0" encoding="UTF-8"?>\n' + svg
    (destination / output_name).write_text(svg, encoding="utf-8")
    print(destination / output_name)
