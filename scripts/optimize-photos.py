"""Turn the original photos in ../Foto's into web-sized WebP files.

Writes public/img/<n>-<width>.webp for every photo and a manifest
(src/data/photo-manifest.json) with the aspect ratio and an average colour
that the site uses as a placeholder while an image loads.
"""
import json
import re
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT.parent / "Foto's "
OUT = ROOT / "public" / "img"
MANIFEST = ROOT / "src" / "data" / "photo-manifest.json"
WIDTHS = [640, 1280, 1920]

OUT.mkdir(parents=True, exist_ok=True)
manifest = {}

for path in sorted(SRC.glob("*.jpg"), key=lambda p: int(re.sub(r"\D", "", p.stem) or 0)):
    n = path.stem
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    w, h = im.size
    avg = im.resize((1, 1), Image.LANCZOS).getpixel((0, 0))
    manifest[n] = {"w": w, "h": h, "color": "#%02x%02x%02x" % avg}
    for width in WIDTHS:
        target = OUT / f"{n}-{width}.webp"
        if target.exists() and target.stat().st_mtime > path.stat().st_mtime:
            continue
        scaled = im.copy()
        scaled.thumbnail((width, width * 2), Image.LANCZOS)
        scaled.save(target, "WEBP", quality=78, method=6)
    print("photo", n, f"{w}x{h}", manifest[n]["color"])

# 1200x630 social preview from the hero photo
hero = ImageOps.exif_transpose(Image.open(SRC / "1.jpg")).convert("RGB")
og = ImageOps.fit(hero, (1200, 630), Image.LANCZOS, centering=(0.5, 0.55))
og.save(ROOT / "public" / "og.jpg", "JPEG", quality=82)

MANIFEST.write_text(json.dumps(manifest, indent=1))
print("done:", len(manifest), "photos")
