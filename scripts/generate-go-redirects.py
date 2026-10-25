#!/usr/bin/env python3
"""Generate Hugo content/go/<slug>.md redirect pages from links.csv.

Schema (header required):
  slug,url,note

GitHub Pages does not honour Cloudflare/Netlify _redirects. These pages use
meta refresh + visible fallback link instead.

Usage:
  python3 scripts/generate-go-redirects.py --csv links.csv --out content/go
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def page_markdown(slug: str, url: str, note: str) -> str:
    note_safe = (note or "").replace("\n", " ").strip()
    title = f"Redirect: {slug}"
    # rel=sponsored once destinations are affiliate; noopener always for external
    return f"""---
title: "{title}"
slug: "{slug}"
url: "/go/{slug}/"
type: go
layout: redirect
robots: noindex,nofollow
redirect_to: "{url}"
note: "{note_safe}"
---

<meta http-equiv="refresh" content="0; url={url}">

# Redirecting…

If you are not redirected automatically, open:

[{url}]({url}){{{{< /* keep raw for fallback * />}}}}

<p><a href="{url}" rel="noopener noreferrer">Continue to destination</a> — {note_safe}</p>
"""


def clean_page(slug: str, url: str, note: str) -> str:
    """Simpler page body that works with a dedicated redirect layout."""
    note_safe = (note or "").replace('"', "'").replace("\n", " ").strip()
    return f"""---
title: "Go: {slug}"
slug: "{slug}"
url: "/go/{slug}/"
type: "go"
layout: "redirect"
robots: "noindex, nofollow"
redirect_to: "{url}"
note: "{note_safe}"
---

If you are not redirected, [continue here]({url}).
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--csv", required=True, type=Path, help="Path to links.csv")
    ap.add_argument("--out", required=True, type=Path, help="Output dir, e.g. content/go")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.csv.is_file():
        print(f"ERROR: CSV not found: {args.csv}", file=sys.stderr)
        return 1

    args.out.mkdir(parents=True, exist_ok=True)
    written = 0
    with args.csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"slug", "url", "note"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            print(
                f"ERROR: CSV must have header columns {sorted(required)}; got {reader.fieldnames}",
                file=sys.stderr,
            )
            return 1
        for row in reader:
            slug = (row.get("slug") or "").strip()
            url = (row.get("url") or "").strip()
            note = (row.get("note") or "").strip()
            if not slug or not url:
                print(f"WARN: skipping incomplete row: {row}", file=sys.stderr)
                continue
            if not SLUG_RE.match(slug):
                print(f"WARN: skipping bad slug {slug!r}", file=sys.stderr)
                continue
            if not (url.startswith("https://") or url.startswith("http://")):
                print(f"WARN: skipping non-http URL for {slug}: {url}", file=sys.stderr)
                continue
            dest = args.out / f"{slug}.md"
            body = clean_page(slug, url, note)
            if args.dry_run:
                print(f"Would write {dest}")
            else:
                dest.write_text(body, encoding="utf-8")
                print(f"Wrote {dest}")
            written += 1

    print(f"Done. {written} redirect page(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
