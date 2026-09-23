from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
renders = root / "renders"


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size)


def crop_white(image):
    image = image.convert("RGB")
    background = Image.new("RGB", image.size, "white")
    box = ImageChops.difference(image, background).getbbox()
    return image.crop(box) if box else image


def fit(image, width, height):
    image.thumbnail((width, height), Image.Resampling.LANCZOS)
    return image


closed = fit(crop_white(Image.open(renders / "final_closed.png")), 760, 590)
opened = fit(crop_white(Image.open(renders / "final_open.png")), 760, 590)

canvas = Image.new("RGB", (1800, 900), "#efefeb")
draw = ImageDraw.Draw(canvas)
ink = "#17191c"
muted = "#555a5e"
yellow = "#b88f00"
red = "#a71930"

draw.text((55, 38), "ARCHIVE MODULE 3030 · FINAL CONFIGURATION", font=font(36, True), fill=ink)
draw.rounded_rectangle((45, 105, 875, 820), radius=18, fill="#f9f9f6", outline=ink, width=3)
draw.rounded_rectangle((925, 105, 1755, 820), radius=18, fill="#f9f9f6", outline=ink, width=3)
draw.text((78, 132), "CLOSED", font=font(30, True), fill=ink)
draw.text((958, 132), "REVEAL", font=font(30, True), fill=ink)

canvas.paste(closed, (70 + (760 - closed.width) // 2, 205), closed if closed.mode == "RGBA" else None)
canvas.paste(opened, (950 + (760 - opened.width) // 2, 205), opened if opened.mode == "RGBA" else None)

draw.text((90, 748), "Red plate completely concealed", font=font(23, True), fill=muted)
draw.text((90, 780), "Open fifth node remains unfastened", font=font(21), fill=yellow)
draw.text((970, 748), "Drawer slides from the right side", font=font(23, True), fill=muted)
draw.text((970, 780), "Red reveal and transmission inside", font=font(21), fill=red)

# Simple movement arrow between panels.
draw.line((840, 455, 940, 455), fill=ink, width=7)
draw.polygon([(940, 455), (915, 438), (915, 472)], fill=ink)
draw.text((836, 486), "OPEN", font=font(18, True), fill=ink)

output = renders / "final-assembly-diagram.png"
canvas.save(output, quality=95)
print(output)
