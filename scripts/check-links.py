#!/usr/bin/env python3
"""Audit the built site: every internal href resolves, every img src exists.

Run `bundle exec jekyll build` first, then `python3 scripts/check-links.py`.
"""
import re, sys, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
if not SITE.is_dir():
    sys.exit("no _site/ — run `bundle exec jekyll build` first")

# baseurl the site was built with, inferred from the first stylesheet link
BASE = ""
for m in re.finditer(r'href="(/[^"]*?)/assets/css/style\.css"', (SITE / "index.html").read_text()):
    BASE = m.group(1)
    break

def resolve(url):
    p = urllib.parse.unquote(urllib.parse.urlparse(url).path)
    if BASE and p.startswith(BASE + "/"):
        p = p[len(BASE):]
    t = SITE / p.lstrip("/")
    return t if t.is_file() else (t / "index.html" if (t / "index.html").is_file() else None)

problems, hrefs, imgs, ext = [], 0, 0, 0
for page in SITE.rglob("*.html"):
    html = page.read_text(encoding="utf-8", errors="replace")
    rel = page.relative_to(SITE)
    for attr, url in re.findall(r'\b(href|src)="([^"]+)"', html):
        if url.startswith(("http://", "https://", "mailto:", "#", "data:")):
            ext += 1
            continue
        if attr == "src":
            imgs += 1
        else:
            hrefs += 1
        if resolve(url) is None:
            problems.append(f"{rel}: {attr}=\"{url}\"")

# images on disk that no page references
referenced = set()
for page in SITE.rglob("*.html"):
    for url in re.findall(r'src="([^"]+)"', page.read_text(encoding="utf-8", errors="replace")):
        if not url.startswith("http"):
            t = resolve(url)
            if t: referenced.add(t.resolve())
orphans = [p.relative_to(SITE) for p in (SITE / "assets/images").rglob("*")
           if p.is_file() and p.resolve() not in referenced]

print(f"checked {hrefs} internal links, {imgs} assets, skipped {ext} external/mailto/anchors")
if orphans:
    print(f"\n{len(orphans)} image(s) on disk but unused on any page:")
    for o in sorted(orphans): print("  ", o)
if problems:
    print(f"\n{len(problems)} BROKEN:")
    for p in problems: print("  ", p)
    sys.exit(1)
print("\nno broken internal links or missing assets")
