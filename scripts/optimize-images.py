#!/usr/bin/env python3
"""Shrink downloaded images to web-sane sizes.

Wix serves several 2-3 MB PNGs that are really photographs. Cap every image at
MAXDIM px on the long edge, re-encode JPEGs, and convert opaque PNGs to JPEG.
Renames are written back into scripts/images.tsv so fetch-images.sh stays in sync.
"""
import pathlib, sys
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAXDIM, QUALITY = 1200, 85
renames = {}
before = after = 0

for p in sorted((ROOT / "assets/images").rglob("*")):
    if not p.is_file() or p.suffix.lower() == ".gif":
        continue
    before += p.stat().st_size
    try:
        im = Image.open(p)
        im.load()
    except Exception as e:
        print(f"skip {p.name}: {e}", file=sys.stderr)
        after += p.stat().st_size
        continue

    if max(im.size) > MAXDIM:
        im.thumbnail((MAXDIM, MAXDIM), Image.LANCZOS)

    has_alpha = im.mode in ("RGBA", "LA") and im.getchannel("A").getextrema()[0] < 255
    if has_alpha:
        im.save(p, optimize=True)
        dest = p
    else:
        dest = p.with_suffix(".jpg")
        im.convert("RGB").save(dest, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        if dest != p:
            p.unlink()
            renames[str(p.relative_to(ROOT))] = str(dest.relative_to(ROOT))
    after += dest.stat().st_size

if renames:
    tsv = ROOT / "scripts/images.tsv"
    lines = []
    for line in tsv.read_text().splitlines():
        d, u = line.split("\t")
        lines.append(f"{renames.get(d, d)}\t{u}")
    tsv.write_text("\n".join(lines) + "\n")

print(f"{before/1e6:.1f} MB -> {after/1e6:.1f} MB, {len(renames)} converted to jpg")
