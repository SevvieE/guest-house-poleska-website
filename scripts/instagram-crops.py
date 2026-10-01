"""Crop the photos for the first Instagram posts to 3:4 (1080x1440), the shape of the profile grid.

Only the width is cropped; the full height of each photo is kept. `cx` is the horizontal centre of the
crop as a fraction of the photo's width (0 = far left, 1 = far right).
"""
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent.parent
SRC = ROOT / "Foto's "
OUT = ROOT / "Instagram"
OUT.mkdir(exist_ok=True)

# (file name, source photo, crop centre)
POSTS = [
    ("2 - voordeur met koebel", 29, 0.50),
    ("3 - stoelen en wijn op het gras", 33, 0.50),
    ("4 - sauna", 27, 0.50),
    ("5a - carrousel - woonkamer (cover)", 15, 0.55),
    ("5b - carrousel - keuken", 10, 0.55),
    ("5c - carrousel - slaapkamer", 19, 0.40),
    ("5d - carrousel - dakraam met uitzicht", 25, 0.55),
    ("5e - carrousel - douche", 17, 0.50),
    ("6 - beek en waterval", 36, 0.50),
    ("7 - pizza-oven", 30, 0.50),
    ("8 - houtkachel", 13, 0.50),
    ("9 - cabin en zwembad (hero)", 1, 0.53),
    ("extra - het lange zwembad en de vallei", 8, 0.42),
]

for name, n, cx in POSTS:
    im = ImageOps.exif_transpose(Image.open(SRC / f"{n}.jpg")).convert("RGB")
    w, h = im.size
    cw = round(h * 3 / 4)
    left = min(max(round(w * cx - cw / 2), 0), w - cw)
    crop = im.crop((left, 0, left + cw, h)).resize((1080, 1440), Image.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=3))
    crop.save(OUT / f"{name}.jpg", "JPEG", quality=92, optimize=True)
    print(name, f"<- foto {n}, crop x {left}..{left + cw} of {w}")
