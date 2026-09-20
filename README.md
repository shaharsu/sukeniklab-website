# Sukenik Lab website

Jekyll port of the lab's Wix site (sukeniklab.com), built for GitHub Pages.

Every publication, team member, news item, and research theme is its own markdown
file, so a routine update is a one-file commit.

## Running locally

```bash
bundle install
bundle exec jekyll serve
# http://127.0.0.1:4000/sukeniklab-website/
```

## Deploying

`.github/workflows/pages.yml` builds and deploys on every push to `main`. In the repo
settings, set **Settings → Pages → Source** to **GitHub Actions** once.

The site is currently configured to serve at `https://<user>.github.io/sukeniklab-website/`.
If the repo is named something else, change `baseurl` in `_config.yml` to match.

### Moving to sukeniklab.com

1. In `_config.yml`, set `url: "https://www.sukeniklab.com"` and `baseurl: ""`.
2. Add a file named `CNAME` at the repo root containing `www.sukeniklab.com`.
3. Point the domain's DNS at GitHub Pages, then enable the custom domain in
   **Settings → Pages**.

## Adding content

Nothing needs to be registered anywhere — drop the file in and it appears.

### A paper → `_publications/`

Filename `YYYY-MM-DD-short-slug.md`. Drop the file in and you are done: the page
sorts on `date:`, newest first, and the year headings are derived from it. Nothing
else needs renumbering.

```markdown
---
title: "Full paper title"
authors: "A Author, B Author, S Sukenik"
venue: "Journal Name, Volume 1, 100000"     # optional
date: 2026-01-15
link_label: Article                          # Article | Preprint | Review
link: "https://doi.org/..."
image: /assets/images/papers/my-figure.jpg   # optional thumbnail
---
```

`date:` is the publication date and is the only thing that controls position. There
is no separate `year:` field — the year heading a paper appears under comes from
`date:`. If the publisher only gives a month, use the 1st; the displayed citation
comes from `venue`, not from `date`. Crossref (`https://api.crossref.org/works/<doi>`)
is a quick way to look a date up.

### A team member → `_people/`

Filename `NN-first-last.md`. `order` sets the position in the grid. The body text is
the one-line project description and accepts markdown links.

```markdown
---
name: New Person
role: Graduate Student
order: 14
photo: /assets/images/team/new-person.jpg
emails:
  - nperson@syr.edu
links:                                       # optional
  - {label: "Scholar", url: "https://..."}
---
What they work on, in a sentence.
```

Photos are displayed at 120×123; anything square-ish works.

When someone leaves, delete their file and add a line to `_data/alumni.yml`.

### A news item → `_news/`

Filename `YYYY-MM-DD.md`. Drop the file in and you are done: the page sorts on the
`date:` field, newest first. Nothing else needs renumbering.

```markdown
---
date: 2026-01-15
date_display: "Jan 15, 2026"
images:                                      # optional
  - src: /assets/images/news/photo.jpg
    caption: "Optional caption"
---
The text of the item, with [links](https://example.com) in markdown.
```

`date:` must be a real ISO date — it drives the sort. `date_display` is the free
text shown on the page and can be anything ("Feb 10-14 '24"). For two items on the
same day, add a letter to the filename (`2026-01-15b.md`).

### A research theme → `_research/`

`title`, `order`, `image`, `image_alt` in front matter; body is the paragraph. Themes
alternate image left/right automatically.

The three summary cards under the intro live in `_data/research_cards.yml`.

## Scripts

| Script | What it does |
|---|---|
| `scripts/fetch-images.sh` | Re-downloads every image from the Wix CDN using `scripts/images.tsv`. Skips files already present. |
| `scripts/optimize-images.py` | Caps images at 1200px, re-encodes, converts opaque PNGs to JPEG. Run after fetching. |
| `scripts/check-links.py` | Audits the built `_site` for broken internal links and missing assets. Run `bundle exec jekyll build` first. |

## Layout notes

- Site-wide text (address, PI email, copyright, Google Scholar URL) lives in `_config.yml`.
- The nav is `_data/nav.yml`.
- Fonts are the Wix ones: Raleway + Poppins. The accent palette is not: the Wix
  greens were replaced with oranges `#e08b2f` / `#f5d9b5` / `#4a2a08`. Navy
  `#17384f` is unchanged. All defined as CSS variables at the top of
  `assets/css/style.css`.
