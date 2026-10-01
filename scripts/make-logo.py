"""Cut the round logo out of its flattened PNG and write web-sized versions.

The source PNG has a fake "transparent" checkerboard baked into its pixels, so we
find the emblem's outline (flood fill from the edges) and use it as an alpha mask.

Input : ../Logo/Logo Guest House Poleska.png
Output: ../Logo/Logo Guest House Poleska (transparent).png   full size, transparent
        ../Logo/Instagram profile picture.png                1080 px, opaque cream background
        public/logo-<w>.webp                                 header, footer and page use
        public/favicon-64.png, public/apple-touch-icon.png
"""
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
LOGO_DIR = ROOT.parent / "Logo"
SRC = LOGO_DIR / "Logo Guest House Poleska.png"
PUBLIC = ROOT / "public"
CREAM = (251, 248, 241)

im = Image.open(SRC).convert("RGB")
W, H = im.size
r, g, b = im.split()
sat = ImageChops.subtract(
    ImageChops.lighter(ImageChops.lighter(r, g), b),
    ImageChops.darker(ImageChops.darker(r, g), b),
)
warm = sat.point(lambda v: 255 if v > 28 else 0)  # wood and ink are warm, the checkerboard is grey
closed = warm.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))

work = closed.copy()
for x in range(0, W, 7):
    for y in (0, H - 1):
        if work.getpixel((x, y)) == 0:
            ImageDraw.floodfill(work, (x, y), 128)
for y in range(0, H, 7):
    for x in (0, W - 1):
        if work.getpixel((x, y)) == 0:
            ImageDraw.floodfill(work, (x, y), 128)
inside = work.point(lambda v: 0 if v == 128 else 255)
ImageDraw.floodfill(inside, (W // 2, H // 2), 200)  # keep only the blob that holds the centre
mask = inside.point(lambda v: 255 if v == 200 else 0)
mask = mask.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.1))  # trim fringe, soften edge

cut = im.copy()
cut.putalpha(mask)
bb = cut.getbbox()
cx, cy = (bb[0] + bb[2]) // 2, (bb[1] + bb[3]) // 2
s = max(bb[2] - bb[0], bb[3] - bb[1]) + 4
box = (cx - s // 2, cy - s // 2, cx - s // 2 + s, cy - s // 2 + s)
master = Image.new("RGBA", (s, s), (0, 0, 0, 0))
crop = cut.crop((max(box[0], 0), max(box[1], 0), min(box[2], W), min(box[3], H)))
master.paste(crop, (max(-box[0], 0), max(-box[1], 0)))

master.save(LOGO_DIR / "Logo Guest House Poleska (transparent).png")

for w in (96, 192, 384, 768):
    master.resize((w, w), Image.LANCZOS).save(PUBLIC / f"logo-{w}.webp", "WEBP", quality=88, method=6)

def on_cream(size: int, pad: float) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), CREAM + (255,))
    inner = int(size * (1 - 2 * pad))
    canvas.alpha_composite(master.resize((inner, inner), Image.LANCZOS), ((size - inner) // 2, (size - inner) // 2))
    return canvas.convert("RGB")

on_cream(1080, 0.04).save(LOGO_DIR / "Instagram profile picture.png")
on_cream(180, 0.06).save(PUBLIC / "apple-touch-icon.png")
master.resize((64, 64), Image.LANCZOS).save(PUBLIC / "favicon-64.png")
print("logo ready", master.size)
